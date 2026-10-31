"""Pure offline tests for the public web-analytics snapshot, with no API access."""

import unittest
from scripts.update_views import aggregate, normalized_path, PUBLIC_PATHS


class ViewsTest(unittest.TestCase):
    def test_canonical_path(self):
        self.assertEqual(
            normalized_path("/yaskcode-blog/posts/rag-fundamentos-arquitectura/index.html"),
            "/yaskcode-blog/posts/rag-fundamentos-arquitectura/",
        )
        self.assertEqual(normalized_path("/yaskcode-blog/"), "/yaskcode-blog/")

    def test_aggregation_only_known_pages(self):
        base = "/yaskcode-blog/posts/rag-fundamentos-arquitectura/"
        values = aggregate([
            {"requestPath": base, "views": 4},
            {"requestPath": base + "index.html", "views": 2},
            {"requestPath": "/other-site/private/", "views": 77},
            {"requestPath": "/yaskcode-blog/", "views": 1},
        ])
        self.assertEqual(values[base], 6)
        self.assertEqual(values["/yaskcode-blog/"], 1)
        self.assertEqual(len(values), len(PUBLIC_PATHS))
        self.assertEqual(values["/yaskcode-blog/posts/historia-campus-yaskcode/"], 0)

    def test_invalid_input_rejected(self):
        with self.assertRaises(ValueError):
            aggregate([{"requestPath": "/yaskcode-blog/", "views": -1}])
        with self.assertRaises(ValueError):
            aggregate([{"requestPath": "/yaskcode-blog/", "views": "100"}])


if __name__ == "__main__":
    unittest.main()
