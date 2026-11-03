# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from arrlib import discover_papers
from assessmentlib import load_assessment_registry, aggregate_assessments, assessments_for
from legacyreviewlib import load_preserved_reviews, read_preserved_review, validate_preserved_reviews
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


if __name__ == "__main__":
    unittest.main()
