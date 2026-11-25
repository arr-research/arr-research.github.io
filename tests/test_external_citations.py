# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import build_site
from arrlib import discover_papers
from externalcitationlib import citations_by_paper, load_external_citations, validate_external_citations


class ExternalCitationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.versions = discover_papers()
        cls.registry = load_external_citations()

    def test_published_registry_is_valid(self):
        self.assertEqual(validate_external_citations(self.registry, self.versions), [])
        self.assertTrue(self.registry["citations"])

    def test_unknown_version_is_rejected(self):
        registry = copy.deepcopy(self.registry)
        registry["citations"][0]["cites"][0]["version"] = "v999"
        self.assertTrue(any("not a published AIRR version" in error for error in validate_external_citations(registry, self.versions)))

    def test_self_citation_is_rejected(self):
        registry = copy.deepcopy(self.registry)
        cited = registry["citations"][0]["cites"][0]
        paper = next(p for p in self.versions if (p.id, p.version) == (cited["paper_id"], cited["version"]))
        registry["citations"][0]["authors"].append({"name": paper.metadata["authors"][0]["name"]})
        self.assertTrue(any("self-citations" in error for error in validate_external_citations(registry, self.versions)))

    def test_reference_must_name_the_identifier_and_links_must_be_https(self):
        registry = copy.deepcopy(self.registry)
        registry["citations"][0]["cites"][0]["reference"] = "A paper."
        registry["citations"][0]["url"] = "http://example.test/paper"
        errors = validate_external_citations(registry, self.versions)
        self.assertTrue(any("must contain" in error for error in errors))
        self.assertTrue(any("https" in error for error in errors))

    def test_pages_link_the_source_and_the_exact_cited_version(self):
        item = self.registry["citations"][0]
        cited = item["cites"][0]
        known = {(cited["paper_id"], cited["version"]): {"title": "Cited <title>", "route": "papers", "pdf": True}}
        with patch.object(build_site, "EXTERNAL_CITATIONS", self.registry["citations"]), patch.object(build_site, "EXTERNAL_CITED", known):
            home = build_site.external_citations_home("/preview")
            page = build_site.build_citations("/preview", "https://example.test/preview")
            cited_by = build_site.paper_cited_by(cited["paper_id"], "/preview")
        version_page = f'/preview/papers/{cited["paper_id"]}/versions/{cited["version"]}/'
        for markup in (home, page):
            self.assertIn(f'href="{item["url"]}"', markup)
            self.assertIn(f'href="{version_page}"', markup)
            self.assertIn("Cited &lt;title&gt;", markup)
        self.assertIn(f'{version_page}{cited["paper_id"]}-{cited["version"]}.pdf', page)
        self.assertIn('<link rel="canonical" href="https://example.test/preview/citations/">', page)
        self.assertIn("not an endorsement", page)
        self.assertIn(f'/preview/citations/#{item["id"]}', cited_by)
        self.assertEqual(build_site.paper_cited_by("ARR-0000-NOTCITED", "/preview"), "")

    def test_nothing_is_shown_without_citations(self):
        with patch.object(build_site, "EXTERNAL_CITATIONS", []):
            self.assertEqual(build_site.external_citations_home(""), "")
            self.assertNotIn("/citations/", build_site.page_shell(title="t", description="d", content="", base=""))
        self.assertEqual(citations_by_paper({"citations": []}), {})


if __name__ == "__main__":
    unittest.main()
