# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import openrouter_assessment_round as runner  # noqa: E402
from arrlib import discover_papers  # noqa: E402
from prepare_model_assessment import build_prompt  # noqa: E402


class OpenRouterAssessmentRoundTests(unittest.TestCase):
    def test_structured_schema_excludes_operator_fields(self) -> None:
        schema = runner.model_response_schema()
        for field in runner.OPERATOR_FIELDS:
            self.assertNotIn(field, schema["required"])
            self.assertNotIn(field, schema["properties"])
        self.assertEqual(schema["properties"]["prompt_version"]["const"], "ARR-ASSESS-1.0")
        self.assertNotIn("multipleOf", schema["properties"]["millennium_score"])

    def test_request_locks_pdf_model_privacy_and_schema(self) -> None:
        paper = discover_papers()[0]
        prompt = build_prompt(paper)
        item = {
            "paper_id": paper.id,
            "version": paper.version,
            "version_id": paper.metadata["version_id"],
            "canonical_sha256": paper.metadata["integrity"]["canonical_sha256"],
            "pdf_url": f"https://airr.science/papers/{paper.id}/paper.pdf",
            "model": "anthropic/example-model",
            "reasoning_effort": "max",
            "pdf_engine": "native",
            "prompt_sha256": runner.hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        }
        body = runner.request_body(item, "not_involved_in_manuscript")
        self.assertEqual(body["model"], item["model"])
        self.assertEqual(body["provider"]["data_collection"], "deny")
        self.assertNotIn("zdr", body["provider"])
        self.assertTrue(body["provider"]["allow_fallbacks"])
        self.assertFalse(body["provider"]["require_parameters"])
        self.assertEqual(body["messages"][0]["content"][1]["file"]["file_data"], item["pdf_url"])
        self.assertEqual(body["reasoning"]["max_tokens"], 12000)
        self.assertEqual(body["plugins"][0]["pdf"]["engine"], "native")

    def test_modified_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            old_root = runner.RUNS_ROOT
            runner.RUNS_ROOT = Path(temporary)
            try:
                target = runner.round_dir("test-round")
                target.mkdir()
                plan = {"round_id": "test-round", "requests": []}
                (target / "manifest.json").write_text(json.dumps(plan), encoding="utf-8")
                (target / "manifest.sha256").write_text(runner.digest(plan) + "  manifest.json\n", encoding="ascii")
                runner.load_sealed("test-round")
                plan["requests"].append({"model": "changed/after-sealing"})
                (target / "manifest.json").write_text(json.dumps(plan), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "seal does not match"):
                    runner.load_sealed("test-round")
            finally:
                runner.RUNS_ROOT = old_root


if __name__ == "__main__":
    unittest.main()
