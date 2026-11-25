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

    def test_numbered_statement_must_exist_in_the_cited_version(self):
        # Theorem 2.2 and Proposition 3.2 belong to the second cited record; the first has no Proposition 3.2.
        registry = copy.deepcopy(self.registry)
        cites = registry["citations"][0]["cites"]
        source = next(cited for cited in cites if cited.get("results_cited"))
        other = next(cited for cited in cites if cited is not source)
        other["results_cited"] = list(source["results_cited"])
        errors = validate_external_citations(registry, self.versions)
        self.assertTrue(any("is not a numbered statement of" in error and other["paper_id"] in error for error in errors))

    def test_reference_record_and_check_are_required(self):
        registry = copy.deepcopy(self.registry)
        entry = registry["citations"][0]
        entry["reference_record"]["id"] = "ARR-2026-NOTOURS"
        entry["reference_record"]["versions"][0]["pdf_sha256"] = "abc"
        del entry["cites"][0]["check"]
        errors = validate_external_citations(registry, self.versions)
        self.assertTrue(any("never ARR-" in error for error in errors))
        self.assertTrue(any("pdf_sha256" in error for error in errors))
        self.assertTrue(any("cites.check is required" in error for error in errors))
        del entry["reference_record"]
        self.assertTrue(any("reference_record is required" in error for error in validate_external_citations(registry, self.versions)))

    def test_citing_documents_are_never_rated(self):
        registry = copy.deepcopy(self.registry)
        registry["citations"][0]["rating"] = 7
        self.assertTrue(any("does not assess a citing document" in error for error in validate_external_citations(registry, self.versions)))

    def test_pages_show_who_cites_the_use_and_the_reference_record(self):
        item = self.registry["citations"][0]
        reference = item["reference_record"]
        with patch.object(build_site, "EXTERNAL_CITATIONS", self.registry["citations"]), patch.object(build_site, "EXTERNAL_CITED", {}):
            home = build_site.external_citations_home("")
            page = build_site.build_citations("", "")
        self.assertIn("Tsinghua University", home)
        self.assertEqual(home.count("Beijing Institute of Mathematical Sciences and Applications"), 1)
        self.assertIn("Citation checked", home)
        self.assertIn(reference["id"], home)
        for cited in item["cites"]:
            self.assertIn(build_site.esc(cited["use"]), home)
            self.assertIn(build_site.esc(cited["check"]["detail"]), page)
        self.assertIn(reference["versions"][0]["pdf_sha256"], page)
        self.assertIn("not submitted to AIRR by its authors", page)
        self.assertIn("AIRR hosts no copy", page)
        self.assertIn("does not rate or review a citing paper", page)
        differing = copy.deepcopy(item)
        differing["cites"][0]["check"]["outcome"] = "discrepancy"
        self.assertEqual(build_site.citation_check_stamp(differing), "")

    def test_nothing_is_shown_without_citations(self):
        with patch.object(build_site, "EXTERNAL_CITATIONS", []):
            self.assertEqual(build_site.external_citations_home(""), "")
            self.assertNotIn("/citations/", build_site.page_shell(title="t", description="d", content="", base=""))
        self.assertEqual(citations_by_paper({"citations": []}), {})


if __name__ == "__main__":
    unittest.main()
