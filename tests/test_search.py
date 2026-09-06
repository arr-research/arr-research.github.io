# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_site


class SearchExportTests(unittest.TestCase):
    def test_search_export_keeps_public_fields_and_base_path(self):
        paper = SimpleNamespace(id="ARR-2026-EXAMPLE", version="v3", record_type="research_paper", metadata={
            "title": 'An SU(2) identity with <symbols>', "abstract": "Exact result.",
            "authors": [{"name": "Lluís Eriksson", "private_field": "not exported"}],
            "keywords": ["SU(2)"], "subjects": ["Mathematical physics"],
            "date": "2026-09-06", "status": "archived", "private_field": "not exported",
        })
        records = build_site.search_records([paper], "/preview")
        self.assertEqual(records[0]["url"], "/preview/papers/ARR-2026-EXAMPLE/")
        self.assertEqual(records[0]["version"], "v3")
        self.assertEqual(records[0]["status"], "archived")
        self.assertEqual(records[0]["authors"], ["Lluís Eriksson"])
        self.assertNotIn("private_field", json.dumps(records))

    def test_search_page_wires_complete_index_and_accessible_get_form(self):
        page = build_site.build_search("/preview", "https://example.test/preview", "catalogue-hash")
        self.assertIn('action="/preview/search/" method="get"', page)
        self.assertIn('name="q" type="search"', page)
        self.assertIn('data-index-url="/preview/assets/search-index.json?v=catalogue-hash"', page)
        self.assertIn('src="/preview/assets/search.js?v=', page)
        self.assertIn('href="https://example.test/preview/search/"', page)
        self.assertIn('aria-live="polite"', page)
        self.assertIn('<noscript>', page)
        self.assertIn('search-more" type="button" hidden', page)


if __name__ == "__main__":
    unittest.main()
