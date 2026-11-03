# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from arrlib import discover_papers
from assessmentlib import load_assessment_registry, aggregate_assessments, assessments_for
from legacyreviewlib import load_preserved_reviews, read_preserved_review, validate_preserved_reviews, preserved_review_family
from build_site import render_preserved_reviews


class PreservedReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = discover_papers()
        cls.registry = load_preserved_reviews()
        cls.record = cls.registry["reviews"][0]
        cls.paper = next(p for p in cls.papers if p.id == cls.record["paper_id"] and p.metadata["version_id"] == cls.record["version_id"])

    def test_original_five_is_not_technical_nine_or_a_new_aggregate(self):
        self.assertEqual(validate_preserved_reviews(self.registry, self.papers), [])
        native = read_preserved_review(self.record, self.paper)
        self.assertEqual(native["importance_airr"]["score"], 5)
        self.assertEqual(native["technical_quality"]["score"], 9)
        self.assertIsNone(aggregate_assessments(assessments_for(load_assessment_registry()["assessments"], self.paper)))
        rendered = render_preserved_reviews(self.paper, [self.record])
        for text in ("5.00 / 10", "separate native measure: 9.00", "not included in the current aggregate", "2026-10-25 (day precision)", "not authenticated", "O1", "O2", "O3"):
            self.assertIn(text, rendered)

    def test_wrong_pdf_version_and_public_path_fail_closed(self):
        for field, value in (("canonical_sha256", "0" * 64), ("version_id", "wrong-version")):
            registry = copy.deepcopy(self.registry)
            registry["reviews"][0][field] = value
            self.assertTrue(validate_preserved_reviews(registry, self.papers))
            self.assertEqual(render_preserved_reviews(self.paper, registry["reviews"]), "")
        for value in ("../private-report.txt", self.record["sources"]["receipt"]["path"].replace("/review/", "/")):
            registry = copy.deepcopy(self.registry)
            registry["reviews"][0]["sources"]["report"]["path"] = value
            self.assertTrue(validate_preserved_reviews(registry, self.papers))

    def test_native_bytes_and_sealed_bindings_cannot_be_replaced(self):
        registry = copy.deepcopy(self.registry)
        registry["reviews"][0]["sources"]["report"]["sha256"] = "0" * 64
        self.assertTrue(validate_preserved_reviews(registry, self.papers))
        registry = copy.deepcopy(self.registry)
        registry["reviews"][0]["sources"]["report"] = registry["reviews"][0]["sources"]["verdict"]
        self.assertTrue(validate_preserved_reviews(registry, self.papers))
        registry = copy.deepcopy(self.registry)
        registry["reviews"].append(copy.deepcopy(self.record))
        self.assertTrue(validate_preserved_reviews(registry, self.papers))

    def test_historical_findings_are_text_not_markup(self):
        native = read_preserved_review(self.record, self.paper)
        native["importance_airr"]["basis"] = "<script>alert(1)</script>"
        with patch("build_site.read_preserved_review", return_value=native):
            rendered = render_preserved_reviews(self.paper, [self.record])
        self.assertIn("&lt;script&gt;", rendered)
        self.assertNotIn("<script>", rendered)

    def bounded_case(self, paper_id):
        record = next(r for r in self.registry["reviews"] if r["paper_id"] == paper_id)
        paper = next(p for p in self.papers if p.id == paper_id and p.metadata["version_id"] == record["version_id"])
        return record, paper

    def test_bounded_reconfirmation_is_explicit_and_not_a_second_full_review(self):
        record, paper = self.bounded_case("ARR-2026-16NB5DD5M18TTBET")
        native = read_preserved_review(record, paper)
        self.assertEqual(preserved_review_family(native), "bounded_reconfirmation")
        self.assertTrue(native["ratings"]["explicitly_reconfirmed_for_this_pdf"])
        self.assertFalse(native["ratings"]["automatic_transfer_from_draft1"])
        rendered = render_preserved_reviews(paper, [record])
        for text in ("5.00 / 10", "separate native measure: 9.00", "relies on audit 390", "not a new full or independent review", "Review date is not recorded", "C1", "C2", "C3"):
            self.assertIn(text, rendered)
        self.assertIsNone(aggregate_assessments(assessments_for(load_assessment_registry()["assessments"], paper)))

    def test_scoreless_followup_preserves_empty_scores_and_correction_scope(self):
        record, paper = self.bounded_case("ARR-2026-5K8R1DT82Q95JSHY")
        native = read_preserved_review(record, paper)
        self.assertEqual(preserved_review_family(native), "scoreless_followup")
        self.assertIsNone(native["airr_importance_0_10"])
        self.assertIsNone(native["technical_quality_0_10"])
        self.assertFalse(native["prior_scores_transferred"])
        rendered = render_preserved_reviews(paper, [record])
        for text in ("No score issued", "2026-10-25 (day precision)", "O1", "O2", "O3", "N1"):
            self.assertIn(text, rendered)
        for text in ("3.80", "8.50", "0.00 / 10"):
            self.assertNotIn(text, rendered)
        self.assertIsNone(aggregate_assessments(assessments_for(load_assessment_registry()["assessments"], paper)))

    def test_bounded_reports_require_the_original_manifest_and_matching_receipt(self):
        for paper_id in ("ARR-2026-16NB5DD5M18TTBET", "ARR-2026-5K8R1DT82Q95JSHY"):
            record, paper = self.bounded_case(paper_id)
            incomplete = copy.deepcopy(record)
            del incomplete["sources"]["manifest"]
            with self.assertRaises(ValueError):
                read_preserved_review(incomplete, paper)
            swapped = copy.deepcopy(record)
            swapped["sources"]["receipt"] = self.record["sources"]["receipt"]
            with self.assertRaises(ValueError):
                read_preserved_review(swapped, paper)


if __name__ == "__main__":
    unittest.main()
