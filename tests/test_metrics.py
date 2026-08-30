# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import sync_metrics  # noqa: E402


class MetricsTests(unittest.TestCase):
    def test_snapshot_sums_only_exact_canonical_pdf_assets(self) -> None:
        paper_id = "ARR-2026-0123456789ABCDEF"
        releases = [
            {
                "tag_name": f"{paper_id}-v1",
                "draft": False,
                "assets": [
                    {"name": f"{paper_id}-v1.pdf", "download_count": 7},
                    {"name": f"{paper_id}-v1-sources.zip", "download_count": 200},
                    {"name": "paper.pdf", "download_count": 300},
                ],
            },
            {
                "tag_name": f"{paper_id}-v2",
                "draft": False,
                "assets": [{"name": f"{paper_id}-v2.pdf", "download_count": 5}],
            },
            {
                "tag_name": f"{paper_id}-v3",
                "draft": True,
                "assets": [{"name": f"{paper_id}-v3.pdf", "download_count": 999}],
            },
            {
                "tag_name": "unrelated-v1",
                "draft": False,
                "assets": [{"name": "unrelated-v1.pdf", "download_count": 999}],
            },
        ]

        snapshot = sync_metrics.build_snapshot("owner/repository", releases)

        self.assertEqual(snapshot["papers"][paper_id]["pdf_downloads"], 12)
        self.assertIsNone(snapshot["papers"][paper_id]["page_views"])
        self.assertFalse(snapshot["views"]["available"])

    def test_privacy_reviewed_view_export_keeps_its_window(self) -> None:
        paper_id = "ARR-2026-0123456789ABCDEF"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "views.json"
            path.write_text(
                json.dumps(
                    {
                        "provider": "Example no-cookie analytics",
                        "window_start": "2026-08-01T00:00:00+00:00",
                        "window_end": "2026-08-30T00:00:00+00:00",
                        "papers": {paper_id: {"page_views": 41, "unique_visitors": 29}},
                    }
                ),
                encoding="utf-8",
            )

            snapshot = sync_metrics.build_snapshot("owner/repository", [], path)

        self.assertTrue(snapshot["views"]["available"])
        self.assertEqual(snapshot["papers"][paper_id]["page_views"], 41)
        self.assertEqual(snapshot["papers"][paper_id]["unique_visitors"], 29)


if __name__ == "__main__":
    unittest.main()
