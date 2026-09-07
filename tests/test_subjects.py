# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from arrlib import discover_papers
from build_site import build_subjects, search_records, subject_groups, subject_slug
from subjectlib import (vocabulary, direct_subject_ids, record_subject_ids, subject_counts,
                        public_vocabulary, validate_classification)


class SubjectTests(unittest.TestCase):
    def test_vocabulary_has_six_source_families_and_emerging_fallback(self):
        data = vocabulary()
        self.assertEqual(len([t for t in data["roots"] if t["id"].startswith("eu-")]), 6)
        self.assertGreater(len(data["terms"]), 1000)
        self.assertIn("airr-other-or-emerging-research-areas", data["by_id"])
        for t in data["terms"]:
            self.assertTrue(t["path"].endswith(t["label"]))
            self.assertEqual(len(t["ancestors"]), len(set(t["ancestors"])))
            self.assertTrue(all(a in data["by_id"] for a in t["ancestors"]))

    def test_every_existing_subject_is_mapped_without_rewriting_metadata(self):
        for p in discover_papers():
            original = copy.deepcopy(p.metadata)
            for label in p.metadata.get("subjects", []):
                self.assertTrue(direct_subject_ids([label]), label)
            record_subject_ids(p.metadata)
            self.assertEqual(original, p.metadata)

    def test_aliases_and_parent_counts_deduplicate_the_same_paper(self):
        p = SimpleNamespace(id="P", version="v1", metadata={"subjects": ["Quantum information", "Quantum information theory", "Quantum Physics"]})
        ids = record_subject_ids(p.metadata)
        counts = subject_counts([p, p])
        self.assertTrue(all(counts[i] == 1 for i in ids))
        self.assertEqual(direct_subject_ids(["Quantum information theory"]), ["airr-quantum-information"])
        self.assertIn(vocabulary()["lookup"]["natural sciences"], ids)
        self.assertEqual(len(subject_groups([p])), 3)  # Old deposited-label routes remain available.
        self.assertEqual(subject_slug("Quantum Physics"), subject_slug(" quantum physics "))

    def test_unknown_labels_are_not_inferred(self):
        self.assertEqual(direct_subject_ids(["unreviewed new discipline"]), [])
        p = SimpleNamespace(id="P",version="v1",metadata={"subjects":["unreviewed new discipline"]})
        self.assertEqual(subject_groups([p])[0]["label"], "unreviewed new discipline")

    def test_directory_contains_zero_count_fields_and_preserves_base_path(self):
        html = build_subjects([], "/preview", "https://example.test/preview")
        self.assertIn("Medical and health sciences", html)
        self.assertIn("No papers yet", html)
        self.assertIn('href="/preview/submit/?subject=', html)
        self.assertIn('src="/preview/assets/subjects.js?v=', html)
        self.assertIn("CC BY 4.0", html)
        self.assertIn("does not guarantee admission", html)

    def test_public_export_has_no_private_manuscript_fields(self):
        data = public_vocabulary()
        self.assertTrue(all(t["count"] == 0 for t in data["terms"]))
        self.assertNotIn("classification_json", json.dumps(data))
        self.assertTrue(any("es" in t["labels"] for t in data["terms"]))

    def test_interdisciplinary_selection_is_versioned_and_bounded(self):
        value = validate_classification("airr-quantum-information", ["airr-number-theory", "airr-ai-agents-and-multi-agent-systems"], "New method")
        self.assertEqual(value["version"], "AIRR-SUBJECTS-1")
        self.assertEqual(len(value["secondary"]), 2)
        self.assertEqual(value["primary"]["label"], "Quantum information")
        for primary,secondary,topic in [
            ("forged",[],""), ("airr-number-theory",["forged"],""),
            ("airr-number-theory",["airr-number-theory"],""),
            ("airr-number-theory",["airr-quantum-information"]*3,""),
            ("airr-other-or-emerging-research-areas",[],""),
            ("airr-number-theory",[],"x"*201)]:
            with self.subTest(primary=primary,secondary=secondary,topic=topic), self.assertRaises(ValueError):
                validate_classification(primary,secondary,topic)


if __name__ == "__main__":
    unittest.main()
