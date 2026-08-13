from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from arrlib import Paper, validate_paper  # noqa: E402


class PaperValidationTests(unittest.TestCase):
    def make_paper(self, root: Path) -> Paper:
        paper_dir = root / "2026" / "08" / "ARR-2026-000001"
        paper_dir.mkdir(parents=True)
        metadata = {
            "id": "ARR-2026-000001",
            "version": "v1",
            "title": "A complete and testable research title",
            "abstract": "This abstract is deliberately long enough to state a question, method, result, scope, and limitation.",
            "authors": [{"name": "Test Author"}],
            "date": "2026-08-13",
            "status": "accepted",
            "license": "CC-BY-4.0",
            "source_of_truth": "paper.tex",
            "ai_assistance": {"used": False, "statement": "No AI assistance was used for this test record."},
            "screening": {
                "protocol": "ARR-SCREEN-1.0",
                "status": "pass",
                "completed_at": "2026-08-13",
                "critical_objections_unresolved": 0,
                "human_signoff": True,
                "evaluators": [
                    {"provider": "A", "model_id": "model-a", "outcome": "pass", "report": "screening/a.md", "involved_in_creation": False},
                    {"provider": "B", "model_id": "model-b", "outcome": "pass", "report": "screening/b.md", "involved_in_creation": False},
                    {"provider": "C", "model_id": "model-c", "outcome": "pass", "report": "screening/c.md", "involved_in_creation": False},
                ],
            },
            "verification": {
                "protocol": "ARR-SCREEN-1.0",
                "bibliography": "pass",
                "source_integrity": "pass",
                "reproducibility": "not_applicable",
                "lean4": "not_applicable",
            },
        }
        for name, content in {
            "metadata.json": json.dumps(metadata),
            "paper.tex": "\\documentclass{article}\\begin{document}Test\\end{document}",
            "paper.md": "# Test",
            "PROVENANCE.json": "{}",
            "CITATION.cff": "cff-version: 1.2.0",
        }.items():
            (paper_dir / name).write_text(content, encoding="utf-8")
        (paper_dir / "LICENSES").mkdir()
        (paper_dir / "screening").mkdir()
        for filename in ("a.md", "b.md", "c.md"):
            (paper_dir / "screening" / filename).write_text("screening report", encoding="utf-8")
        return Paper(paper_dir, metadata)

    def test_valid_complete_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            self.assertEqual(validate_paper(paper), [])

    def test_missing_machine_readable_paper_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            paper = self.make_paper(Path(temporary))
            (paper.path / "paper.md").unlink()
            errors = validate_paper(paper)
            self.assertTrue(any(error.startswith("paper.md:") for error in errors))


if __name__ == "__main__":
    unittest.main()
