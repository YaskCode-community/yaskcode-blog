"""Offline tests: cumulative views, 30-day windows and idempotent history."""

import unittest
from datetime import datetime, timedelta, timezone
from scripts.update_views import (
    aggregate, normalized_path, day_counts, merge_history, public_snapshot, PUBLIC_PATHS,
)

RAG = "/yaskcode-blog/posts/rag-fundamentos-arquitectura/"
HUGGING = "/yaskcode-blog/posts/hugging-face-modelos-datasets-ciencia-de-datos/"
START = datetime(2026, 10, 31, 12, 0, tzinfo=timezone.utc)


class ViewsTest(unittest.TestCase):
    def test_canonical_paths(self):
        self.assertEqual(normalized_path(RAG + "index.html"), RAG)
        self.assertEqual(normalized_path("/yaskcode-blog/"), "/yaskcode-blog/")

    def test_only_whitelisted_paths(self):
        counts = aggregate([
            {"requestPath": RAG, "views": 4},
            {"requestPath": RAG + "index.html", "views": 2},
            {"requestPath": "/other-site/private/", "views": 77},
        ])
        self.assertEqual(counts[RAG], 6)
        self.assertEqual(len(counts), len(PUBLIC_PATHS))
        self.assertEqual(counts[HUGGING], 0)

    def test_daily_aggregation_cumulative_and_idempotent(self):
        rows = [
            {"day": "2026-10-31", "requestPath": RAG, "views": 3},
            {"day": "2026-10-31", "requestPath": RAG + "index.html", "views": 2},
            {"day": "2026-10-31", "requestPath": HUGGING, "views": 1},
            {"day": "2026-10-31", "requestPath": "/other-site/private/", "views": 100},
        ]
        self.assertEqual(day_counts(rows)["2026-10-31"][RAG], 5)
        history = merge_history(None, rows, START.date(), START)
        self.assertEqual(public_snapshot(history, START)["paths"][RAG]["total"], 5)
        self.assertEqual(public_snapshot(history, START)["paths"][HUGGING]["total"], 1)

        # A second run querying the same day must replace, not add its counts.
        again = merge_history(history, rows, START.date(), START)
        self.assertEqual(public_snapshot(again, START)["paths"][RAG]["total"], 5)

        # Late-arriving event: one past day changes from 5 to 7; no double counting.
        new_rows = [{"day": "2026-10-31", "requestPath": RAG, "views": 7}]
        again = merge_history(history, new_rows, START.date(), START)
        self.assertEqual(public_snapshot(again, START)["paths"][RAG]["total"], 7)

    def test_cumulative_keeps_views_older_than_30_days(self):
        end = START + timedelta(days=40)
        history = merge_history(None,
            [{"day": "2026-10-31", "requestPath": RAG, "views": 9}],
            START.date(), end)
        record = public_snapshot(history, end)["paths"][RAG]
        self.assertEqual(record["total"], 9)
        self.assertEqual(record["last_30_days"], 0)

    def test_missing_archive_days_fail_closed(self):
        future = START + timedelta(days=2)
        with self.assertRaises(ValueError):
            merge_history(
                {"daily": {"2026-10-31": {RAG: 3}}},
                [], future.date(), future,
            )

    def test_invalid_counts_rejected(self):
        with self.assertRaises(ValueError):
            aggregate([{"requestPath": RAG, "views": -1}])
        with self.assertRaises(ValueError):
            aggregate([{"requestPath": RAG, "views": "100"}])
        with self.assertRaises(ValueError):
            day_counts([{"day": "2026-10-31", "requestPath": RAG, "views": -1}])


if __name__ == "__main__":
    unittest.main()
