#!/usr/bin/env python3
"""Build a 30-day, public-safe snapshot from Cloudflare Web Analytics.

Runs in GitHub Actions, never in visitors' browsers and never in a Worker.
Secrets are CF_WEB_ANALYTICS_TOKEN (Account Analytics: Read) and CF_WEB_ANALYTICS_ACCOUNT_ID.
The site tag below is a resource identifier, NOT a credential.
"""

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://api.cloudflare.com/client/v4/analytics/sql"
SITE_TAG = "be709aa5de734c88b005566cf0338c82"
HOST = "yaskcode-community.github.io"
BASE = "/yaskcode-blog/"
WINDOW_DAYS = 30
STARTED_AT = "2026-10-31T06:39:51Z"
PUBLIC_PATHS = (
    BASE,
    BASE + "posts/historia-campus-yaskcode/",
    BASE + "posts/hugging-face-modelos-datasets-ciencia-de-datos/",
    BASE + "posts/por-que-aprender-poo-en-la-era-de-la-ia/",
    BASE + "posts/rag-fundamentos-arquitectura/",
)
SQL = """SELECT requestPath, COUNT(*) AS views
FROM events.rumPageloadEvents
WHERE siteTag = $tag AND requestHost = $host AND bot = 0
  AND timestamp >= $start AND timestamp < $end
GROUP BY requestPath ORDER BY views DESC LIMIT 1000"""


def normalized_path(value):
    """Treat slash and /index.html URLs as the same canonical Quarto page."""
    if not isinstance(value, str):
        return ""
    path = value.split("?", 1)[0]
    if path.endswith("/index.html"):
        path = path[:-len("index.html")]
    if path.endswith("/") or not path.startswith(BASE):
        return path
    return path + "/"


def aggregate(rows):
    """Expose only vetted blog paths; no URL parameters or individual user data."""
    counts = {key: 0 for key in PUBLIC_PATHS}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Cloudflare returned an unexpected analytics row")
        path = normalized_path(row.get("requestPath"))
        if path not in counts:
            continue
        views = row.get("views")
        if isinstance(views, bool) or not isinstance(views, (int, float)):
            raise ValueError("Cloudflare returned a nonnumeric pageview count")
        if views < 0:
            raise ValueError("Cloudflare returned a negative pageview count")
        counts[path] += int(round(views))
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site/assets/views.json")
    args = parser.parse_args()
    token = os.environ.get("CF_WEB_ANALYTICS_TOKEN", "").strip()
    if not token:
        parser.error("CF_WEB_ANALYTICS_TOKEN is missing (store it only in GitHub Actions secrets)")
    account_id = os.environ.get("CF_WEB_ANALYTICS_ACCOUNT_ID", "").strip()
    if len(account_id) != 32 or any(char not in "0123456789abcdef" for char in account_id):
        parser.error("CF_WEB_ANALYTICS_ACCOUNT_ID is missing or invalid (store it in GitHub Actions secrets)")

    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(days=WINDOW_DAYS)
    iso = lambda dt: dt.isoformat().replace("+00:00", "Z")

    body = {
        "query": SQL,
        "params": {
            "tag": SITE_TAG,
            "host": HOST,
            "start": iso(start),
            "end": iso(end),
        },
        "scope": {"accountTag": account_id},
    }
    req = Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "User-Agent": "YaskCode-Web-Analytics-Snapshot",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=30) as response:
            result = json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError("Cloudflare Analytics SQL request failed; no snapshot written") from exc

    if not isinstance(result, dict) or not isinstance(result.get("data"), list):
        raise RuntimeError("Cloudflare returned no valid analytics rows; no snapshot written")
    if result.get("errors"):
        raise RuntimeError("Cloudflare returned an analytics error; no snapshot written")

    snapshot = {
        "schema_version": 1,
        "window_days": WINDOW_DAYS,
        "generated_at": iso(end),
        "measurement_started_at": STARTED_AT,
        "source": "Cloudflare Web Analytics (Analytics SQL API)",
        "metric": "recorded_pageviews_non_bot",
        "paths": aggregate(result["data"]),
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Public-safe analytics snapshot: {len(snapshot['paths'])} paths, {sum(snapshot['paths'].values())} pageviews (30 days).")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
