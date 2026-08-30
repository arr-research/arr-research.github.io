# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from arrlib import discover_papers, group_paper_versions  # noqa: E402
from assessmentlib import aggregate_assessments, normalize_model_response, validate_assessment  # noqa: E402
import build_site  # noqa: E402


class AssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_versions = discover_papers()
        cls.paper = next(iter(group_paper_versions(cls.all_versions).values()))[-1]

    def response(self, *, score: float = 5.0, independence: str = "not_involved_in_manuscript", recommendation: str = "accept", material: bool = False) -> dict:
        metadata = self.paper.metadata
        response = {
            "paper_id": self.paper.id,
            "version": self.paper.version,
            "version_id": metadata["version_id"],
            "canonical_sha256": metadata["integrity"]["canonical_sha256"],
            "provider": "Test Provider",
            "model_id": f"test-frontier-{score}-{independence}",
            "assessed_at": "2026-08-30T12:00:00+00:00",
            "prompt_version": "ARR-ASSESS-1.0",
            "independence": independence,
            "recommendation": recommendation,
            "millennium_score": score,
            "overall_stars": max(1, int(score + 0.5)),
            "criteria": {
                name: {"stars": 4, "basis": "The report gives a concise claim-linked evidentiary basis."}
                for name in ("correctness_confidence", "rigor", "novelty", "significance", "reproducibility")
            },
            "summary": "A hostile inspection of the exact canonical artifact found a substantive and independently inspectable contribution.",
            "strengths": ["The main result is stated with an inspectable scope."],
            "weaknesses": ["One expository dependency could be stated more directly."],
            "potential_errors": [],
            "strong_novelty_candidates": ["The central construction may provide an unusually strong result."],
            "unresolved_material_objections": ["A central lemma may fail under the stated assumptions."] if material else [],
        }
        return normalize_model_response(response)

    def test_valid_exact_version_assessment(self) -> None:
        self.assertEqual(validate_assessment(self.response(), self.all_versions), [])

    def test_tampering_breaks_response_hash(self) -> None:
        assessment = self.response()
        assessment["summary"] = "This altered summary is long enough to pass length validation but no longer matches the source response digest."
        self.assertTrue(any("source_response_sha256" in error for error in validate_assessment(assessment, self.all_versions)))

    def test_evidenced_runtime_provenance_preserves_source_hash(self) -> None:
        assessment = self.response()
        assessment["runtime_provenance"] = {
            "provider": "OpenAI",
            "model_id": "gpt-5.6-sol",
            "reasoning_effort": "high",
            "basis": "author_verified_ui",
            "evidence_sha256": "a" * 64,
        }
        self.assertEqual(validate_assessment(assessment, self.all_versions), [])

    def test_invalid_runtime_reasoning_effort_is_rejected(self) -> None:
        assessment = self.response()
        assessment["runtime_provenance"] = {
            "provider": "OpenAI",
            "model_id": "gpt-5.6-sol",
            "reasoning_effort": "very-high",
            "basis": "author_verified_ui",
            "evidence_sha256": "a" * 64,
        }
        self.assertTrue(any("runtime_provenance.reasoning_effort" in error for error in validate_assessment(assessment, self.all_versions)))

    def test_public_report_prefers_evidenced_runtime_identity(self) -> None:
        assessment = self.response()
        assessment["model_id"] = "incorrect-self-report"
        assessment["runtime_provenance"] = {
            "provider": "OpenAI",
            "model_id": "gpt-5.6-sol",
            "reasoning_effort": "high",
            "basis": "author_verified_ui",
            "evidence_sha256": "a" * 64,
        }
        page = build_site.paper_assessment_section(self.paper, [assessment], None, "")
        self.assertIn("OpenAI · gpt-5.6-sol · High", page)
        self.assertNotIn("incorrect-self-report</strong>", page)
        self.assertIn("reasoning effort: high", page)

    def test_material_objection_cannot_recommend_accept(self) -> None:
        errors = validate_assessment(self.response(material=True), self.all_versions)
        self.assertTrue(any("unresolved material objections" in error for error in errors))

    def test_aggregate_is_median_of_independent_exact_reports(self) -> None:
        reports = [self.response(score=4.0), self.response(score=6.0), self.response(score=10.0, independence="involved_in_manuscript")]
        aggregate = aggregate_assessments(reports)
        self.assertEqual(aggregate["score"], 5.0)
        self.assertEqual(aggregate["stars"], 5)
        self.assertEqual(aggregate["count"], 2)
        self.assertEqual(aggregate["tier"], "Very good")

    def test_public_scale_explains_five_is_very_good(self) -> None:
        page = build_site.build_assessments([self.paper], [], [], "", "https://arr.example", {self.paper.metadata["authors"][0]["name"]: {"id": "test-author"}})
        self.assertIn("Five is very good, not a failing grade", page)
        self.assertIn("Not yet rated", page)
        self.assertNotIn("0 rated current versions</span><span>0 not yet rated", page)


if __name__ == "__main__":
    unittest.main()
