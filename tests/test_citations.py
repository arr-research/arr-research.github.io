# SPDX-License-Identifier: AGPL-3.0-or-later
import json
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from citationlib import citation_exports
from build_site import paper_card, subject_groups, subject_slug


class CitationTests(unittest.TestCase):
    def metadata(self, **changes):
        return {"id": "ARR-2026-EXAMPLE", "version": "v1", "title": "Exact SU(2) bounds",
                "authors": [{"name": "Lluís Eriksson"}, {"name": "Research Consortium"}],
                "date": "2025-02-03", "abstract": "Exact bounds.", "status": "accepted", **changes}

    def test_citation_targets_exact_version_not_mutable_latest_page(self):
        first = citation_exports(self.metadata(), "https://airr.science")
        second = citation_exports(self.metadata(version="v2", date="2026-09-07"), "https://airr.science")
        for suffix in first:
            self.assertIn("/versions/v1/", first[suffix])
            self.assertNotIn("/versions/v2/", first[suffix])
            self.assertIn("/versions/v2/", second[suffix])
        csl = json.loads(first["csl.json"])[0]
        self.assertEqual(csl["issued"]["date-parts"], [[2025, 2, 3]])
        self.assertEqual(csl["author"], [{"literal": "Lluís Eriksson"}, {"literal": "Research Consortium"}])
        self.assertNotIn("DOI", csl)
        self.assertNotIn("container-title", csl)
        self.assertNotIn("journal", first["bib"])
        self.assertNotIn("TY  - JOUR", first["ris"])

    def test_exports_preserve_title_and_do_not_allow_ris_field_injection(self):
        metadata = self.metadata(title='SU(2): {A & B} #1\\test', abstract="First line\nDO  - 10.0000/forged")
        exports = citation_exports(metadata, "https://example.test/preview")
        self.assertEqual(json.loads(exports["csl.json"])[0]["title"], metadata["title"])
        self.assertIn(r"\{A \& B\}", exports["bib"])
        self.assertNotIn("\nDO  -", exports["ris"])
        self.assertIn("https://example.test/preview/papers/", exports["txt"])

    def test_existing_doi_and_historical_withdrawn_status_are_retained(self):
        exports = citation_exports(self.metadata(doi="10.1234/example", archival_source={"id": "old"}, status="withdrawn"), "https://airr.science")
        csl = json.loads(exports["csl.json"])[0]
        self.assertEqual(csl["DOI"], "10.1234/example")
        self.assertEqual(csl["genre"], "Archived manuscript")
        for suffix in ("txt", "ris", "csl.json", "bib"):
            self.assertIn("Withdrawn", exports[suffix])
        self.assertIn("\nDO  - 10.1234/example\n", exports["ris"])

    def test_technical_note_has_its_own_version_route(self):
        csl = json.loads(citation_exports(self.metadata(record_type="technical_note"), "https://airr.science")["csl.json"])[0]
        self.assertEqual(csl["URL"], "https://airr.science/notes/ARR-2026-EXAMPLE/versions/v1/")

    def test_catalogue_cite_link_keeps_the_version_shown_on_the_card(self):
        timestamp = {"publication_state": "published", "published_at": "2025-02-03T10:00:00+00:00", "deposit_recorded_at": "2025-02-02T10:00:00+00:00"}
        card = paper_card(self.metadata(), timestamp, "/preview")
        self.assertIn('href="/preview/papers/ARR-2026-EXAMPLE/versions/v1/#cite"', card)
        self.assertNotIn('href="/preview/papers/ARR-2026-EXAMPLE/#cite"', card)


class SubjectTests(unittest.TestCase):
    def test_case_variants_share_a_subject_without_duplicating_papers(self):
        papers = [SimpleNamespace(metadata={"subjects": ["Mathematical Physics", "Mathematical physics"]}), SimpleNamespace(metadata={"subjects": ["Mathematical physics"]})]
        groups = subject_groups(papers)
        self.assertEqual(len(groups), 1)
        self.assertEqual(len(groups[0]["papers"]), 2)
        self.assertEqual(subject_slug(" Mathematical Physics "), subject_slug("mathematical physics"))

    def test_subject_routes_are_safe_distinct_and_stable(self):
        self.assertNotEqual(subject_slug("A/B"), subject_slug("A B"))
        self.assertRegex(subject_slug("../../<script>SU(2)</script>"), r"^[a-z0-9-]+$")


if __name__ == "__main__":
    unittest.main()
