# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from arrlib import discover_papers
from assessmentlib import load_assessment_registry, validate_registry
from build_site import render_input_notices


class AssessmentInputNoticeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = discover_papers()
        cls.registry = load_assessment_registry()
        cls.notice = cls.registry["operator_notices"][0]
        cls.paper = next(p for p in cls.papers if p.id == cls.notice["paper_id"] and p.metadata["version_id"] == cls.notice["version_id"])

    def test_clarification_keeps_every_native_report_and_score_unchanged(self):
        registry = copy.deepcopy(self.registry)
        reports = copy.deepcopy(registry["assessments"])
        self.assertEqual(validate_registry(registry, self.papers), [])
        self.assertEqual(registry["assessments"], reports)
        rendered = render_input_notices(self.paper, registry["operator_notices"], "/preview")
        self.assertIn("Review input clarification", rendered)
        self.assertIn("/preview/registry/model-assessments.json", rendered)

    def test_notice_cannot_cross_pdf_or_version_boundaries(self):
        for field, value in (("canonical_sha256", "f" * 64), ("version_id", "arr:version:11111111-2222-4333-8444-555555555555")):
            registry = copy.deepcopy(self.registry)
            registry["operator_notices"][0][field] = value
            errors = validate_registry(registry, self.papers)
            self.assertTrue(any("exact paper and PDF" in e for e in errors))
            self.assertEqual(render_input_notices(self.paper, [registry["operator_notices"][0]], ""), "")

    def test_unknown_report_and_unverified_public_source_are_rejected(self):
        registry = copy.deepcopy(self.registry)
        registry["operator_notices"][0]["affected_assessment_ids"] = ["arr:assessment:unknown"]
        self.assertTrue(validate_registry(registry, self.papers))
        for field, value in (("sha256", "0" * 64), ("path", "papers/../../private-input.json")):
            registry = copy.deepcopy(self.registry)
            registry["operator_notices"][0]["source_files"][0][field] = value
            self.assertTrue(validate_registry(registry, self.papers))

    def test_notice_text_is_rendered_as_text(self):
        notice = copy.deepcopy(self.notice)
        notice["message"] = "<script>alert('untrusted')</script> is untrusted source text, not markup."
        rendered = render_input_notices(self.paper, [notice], "")
        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;", rendered)


if __name__ == "__main__":
    unittest.main()
