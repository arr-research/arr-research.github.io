# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from arrlib import Paper
from assessmentlib import normalize_model_response, validate_public_assessments
import test_assessments


class PublicRatingCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_assessments.AssessmentTests.setUpClass()
        cls.fixture = test_assessments.AssessmentTests()

    def paper(self, status="accepted", *, revision=False):
        metadata = copy.deepcopy(self.fixture.paper.metadata)
        metadata["status"] = status
        if revision:
            metadata["version"] = f"v{self.fixture.paper.version_number + 1}"
            metadata["version_id"] = "arr:version:11111111-2222-4333-8444-555555555555"
        return Paper(self.fixture.paper.path, metadata)

    def report(self, paper, *, score=5, recommendation="accept", material=False):
        report = self.fixture.response(score=score, recommendation=recommendation, material=material)
        native = {k: v for k, v in report.items() if k not in {"assessment_id", "source_response_sha256"}}
        native.update(version=paper.version, version_id=paper.metadata["version_id"], model_id="test-reviewer")
        return normalize_model_response(native)

    def registry(self, *reports):
        return {"schema_version": "1.0", "protocol": "ARR-ASSESS-1.0", "license": "CC-BY-4.0", "assessments": list(reports)}

    def test_approved_current_versions_require_real_reports(self):
        for status in ("accepted", "corrected"):
            paper = self.paper(status)
            errors = validate_public_assessments(self.registry(), [paper])
            self.assertEqual(len(errors), 1)
            self.assertIn(paper.id, errors[0])
            self.assertIn("exact version and PDF", errors[0])

    def test_working_paper_can_remain_unrated(self):
        self.assertEqual(validate_public_assessments(self.registry(), [self.paper("working_paper")]), [])

    def test_predecessor_report_cannot_satisfy_new_version_even_with_same_pdf(self):
        predecessor, current = self.paper(), self.paper("corrected", revision=True)
        errors = validate_public_assessments(self.registry(self.report(predecessor)), [predecessor, current])
        self.assertEqual(len(errors), 1)
        self.assertIn(current.version, errors[0])

    def test_current_report_does_not_require_retroactive_predecessor_rating(self):
        predecessor, current = self.paper(), self.paper("corrected", revision=True)
        self.assertEqual(validate_public_assessments(self.registry(self.report(current)), [predecessor, current]), [])

    def test_coverage_does_not_forge_acceptance_or_erase_adverse_findings(self):
        paper = self.paper()
        registry = self.registry(self.report(paper, score=2, recommendation="major_revision", material=True))
        original = copy.deepcopy(registry)
        self.assertEqual(validate_public_assessments(registry, [paper]), [])
        self.assertEqual(registry, original)
        self.assertEqual(paper.metadata["status"], "accepted")

    def test_wrong_pdf_and_tampered_scores_cannot_satisfy_coverage(self):
        paper = self.paper()
        for field, value in (("canonical_sha256", "f" * 64), ("millennium_score", 6)):
            report = self.report(paper)
            report[field] = value
            self.assertTrue(validate_public_assessments(self.registry(report), [paper]))

    def test_ambiguous_simultaneous_scores_prevent_publication(self):
        paper = self.paper()
        errors = validate_public_assessments(self.registry(self.report(paper, score=5), self.report(paper, score=6)), [paper])
        self.assertTrue(any("Conflicting simultaneous" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
