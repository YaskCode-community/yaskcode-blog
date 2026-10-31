#!/usr/bin/env python3
"""Build a cumulative and 30-day web-analytics snapshot without Workers.

Only GitHub Actions reads Cloudflare. Daily totals persist on the separate
analytics-history Git branch, not in browser storage or a Cloudflare Worker.
"""

import argparse
from datetime import date, datetime, time, timedelta, timezone
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://api.cloudflare.com/client/v4/analytics/sql"
SITE_TAG = "be709aa5de734c88b005566cf0338c82"  # Public site identifier, not secret
HOST = "yaskcode-community.github.io"
BASE = "/yaskcode-blog/"
WINDOW_DAYS = 30
REFRESH_DAYS = 7
MAX_BACKFILL_DAYS = 160  # Fail safely if durable data is missing beyond retention
STARTED_AT = "2026-10-31T06:39:51Z"
FIRST_DAY = date.fromisoformat(STARTED_AT[:10])
PUBLIC_PATHS = (
    BASE,
    BASE + "posts/historia-campus-yaskcode/",
    BASE + "posts/hugging-face-modelos-datasets-ciencia-de-datos/",
    BASE + "posts/por-que-aprender-poo-en-la-era-de-la-ia/",
    BASE + "posts/rag-fundamentos-arquitectura/",
)
SQL = """SELECT toDate(timestamp) AS day, requestPath, COUNT(*) AS views
FROM events.rumPageloadEvents
WHERE siteTag = $tag AND requestHost = $host AND bot = 0
  AND timestamp >= $start AND timestamp < $end
GROUP BY day, requestPath ORDER BY day ASC LIMIT 10000"""


def normalized_path(value):
    """Normalize Quarto /index.html paths; ignore query parameters."""
    if not isinstance(value, str):
        return ""
    path = value.split("?", 1)[0]
    if path.endswith("/index.html"):
        path = path[:-len("index.html")]
    if path.endswith("/") or not path.startswith(BASE):
        return path
    return path + "/"


def aggregate(rows):
    """Backward-compatible helper for verifying canonical URL normalization."""
    counts = {path: 0 for path in PUBLIC_PATHS}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Unexpected row")
        path = normalized_path(row.get("requestPath"))
        if path not in counts:
            continue
        views = row.get("views")
        if isinstance(views, bool) or not isinstance(views, int) or views < 0:
            raise ValueError("Invalid views")
        counts[path] += views
    return counts


def day_counts(rows):
    """Return per-day aggregates with a strictly whitelisted path list."""
    grouped = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Unexpected analytics row")
        day = row.get("day")
        if not isinstance(day, str):
            raise ValueError("Missing analytics day")
        parsed = date.fromisoformat(day)
        if parsed < FIRST_DAY:
            continue
        path = normalized_path(row.get("requestPath"))
        if path not in PUBLIC_PATHS:
            continue
        count = row.get("views")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("Invalid analytics count")
        grouped.setdefault(parsed.isoformat(), {p: 0 for p in PUBLIC_PATHS})[path] += count
    return grouped


def read_history(path):
    if not path.exists():
        return None
    record = json.loads(path.read_text(encoding="utf-8"))
    if record.get("schema_version") != 1 or record.get("measurement_started_at") != STARTED_AT:
        raise ValueError("Incompatible historical archive; refusing to reset totals")
    if not isinstance(record.get("daily"), dict):
        raise ValueError("Historical archive is malformed")
    if not record.get("refreshed_through"):
        raise ValueError("Historical archive is missing its coverage marker")
    for day, values in record["daily"].items():
        date.fromisoformat(day)
        if not isinstance(values, dict):
            raise ValueError("Invalid historical day")
        if any(not isinstance(v, int) or isinstance(v, bool) or v < 0
               for v in values.values()):
            raise ValueError("Invalid historical pageviews")
    return record


def merge_history(previous, rows, start_day, now):
    """Replace whole days in a lookback range; never double-count repeat runs."""
    today = now.date()
    if start_day < FIRST_DAY:
        start_day = FIRST_DAY
    if start_day > today:
        raise ValueError("Invalid range")
    daily = dict(previous["daily"]) if previous else {}
    grouped = day_counts(rows)
    day = start_day
    while day <= today:
        # An empty day in an otherwise successful Cloudflare query is a real zero.
        daily[day.isoformat()] = grouped.get(day.isoformat(), {p: 0 for p in PUBLIC_PATHS})
        day += timedelta(days=1)

    first = FIRST_DAY
    day = first
    while day <= today:
        if day.isoformat() not in daily:
            raise ValueError("Missing historic day; refusing to publish incomplete totals")
        day += timedelta(days=1)
    return {
        "schema_version": 1,
        "measurement_started_at": STARTED_AT,
        "refreshed_through": today.isoformat(),
        "generated_at": utc_iso(now),
        "daily": dict(sorted(daily.items())),
    }


def public_snapshot(history, now):
    """Two metrics per page: cumulative since start and trailing 30 UTC days."""
    totals = {path: {"total": 0, "last_30_days": 0} for path in PUBLIC_PATHS}
    recent_from = now.date() - timedelta(days=WINDOW_DAYS - 1)
    for day, values in history["daily"].items():
        when = date.fromisoformat(day)
        if when > now.date():
            raise ValueError("Future day in historical data")
        for path in PUBLIC_PATHS:
            count = values.get(path, 0)
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("Invalid historic count")
            totals[path]["total"] += count
            if when >= recent_from:
                totals[path]["last_30_days"] += count
    return {
        "schema_version": 2,
        "window_days": WINDOW_DAYS,
        "generated_at": utc_iso(now),
        "measurement_started_at": STARTED_AT,
        "source": "Cloudflare Web Analytics (Analytics SQL API)",
        "metric": "recorded_pageviews_non_bot",
        "paths": totals,
    }


def utc_iso(value):
    return value.isoformat(timespec="seconds").replace("+00:00", "Z")


def query_rows(token, account_id, start, end):
    body = {
        "query": SQL,
        "params": {
            "tag": SITE_TAG, "host": HOST,
            "start": utc_iso(datetime.combine(start, time.min, tzinfo=timezone.utc)),
            "end": utc_iso(end),
        },
        "scope": {"accountTag": account_id},
    }
    req = Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "User-Agent": "YaskCode-Daily-Analytics",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=45) as response:
            result = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError("Cloudflare analytics unavailable: history left unchanged") from exc
    if (not isinstance(result, dict) or not isinstance(result.get("data"), list)
            or result.get("errors")):
        raise RuntimeError("Cloudflare returned an invalid analytics response")
    if result.get("rows", len(result["data"])) >= 10000:
        raise RuntimeError("Analytics query hit the row cap; refusing incomplete totals")
    return result["data"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site/assets/views.json")
    parser.add_argument("--history", default="views-history.json")
    args = parser.parse_args()
    token = os.environ.get("CF_WEB_ANALYTICS_TOKEN", "").strip()
    account_id = os.environ.get("CF_WEB_ANALYTICS_ACCOUNT_ID", "").strip()
    if not token:
        parser.error("Missing CF_WEB_ANALYTICS_TOKEN secret")
    if len(account_id) != 32 or any(c not in "0123456789abcdef" for c in account_id):
        parser.error("Missing or invalid CF_WEB_ANALYTICS_ACCOUNT_ID secret")

    now = datetime.now(timezone.utc).replace(microsecond=0)
    history_path = Path(args.history)
    previous = read_history(history_path)
    if previous:
        last = date.fromisoformat(previous["refreshed_through"])
        if last > now.date():
            raise ValueError("Historical archive is dated in the future")
        # Refresh recent days to correct late beacon delivery; backfill missed days.
        start = min(last - timedelta(days=REFRESH_DAYS), now.date() - timedelta(days=REFRESH_DAYS))
        start = max(start, FIRST_DAY)
    else:
        start = FIRST_DAY

    if (now.date() - start).days > MAX_BACKFILL_DAYS:
        raise RuntimeError("History gap too old for safe backfill; manual repair required")

    rows = query_rows(token, account_id, start, now)
    history = merge_history(previous, rows, start, now)
    public = public_snapshot(history, now)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    history_path.parent.mkdir(parents=True, exist_ok=True)
    # Both are written only after querying and validating all data.
    output.write_text(json.dumps(public, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    history_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Updated", len(history["daily"]), "UTC days and", len(public["paths"]), "public page totals.")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
