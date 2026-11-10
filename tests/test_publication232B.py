# SPDX-License-Identifier: AGPL-3.0-or-later
"""Colab/CI only: real-field controls for the exact Working paper producer.

No normalizer is called here, so normal/-O runs cannot manufacture extra report
IDs. The public input inventory is refreshed for the edited field in each control:
the semantic guard, not merely a stale file digest, must reject the mutation.
"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import finalize_rectangular_v15_232B as producer


class Publication232BTests(unittest.TestCase):
    def test_positive_exact_candidate_keeps_all_material_entries(self):
        meta, bound, checks = producer.check_candidate()
        self.assertGreaterEqual(len(checks), 170)
        self.assertEqual(bound['recommendation'], 'major_revision')
        self.assertEqual(len(bound['unresolved_material_objections']), 3)
        self.assertFalse(meta['screening']['human_signoff'])

    def reject_changed_field(self, relative, change, expected):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            path = target / relative
            value = json.loads(path.read_text())
            change(value)
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
            inventory_path = target / 'PACKAGE-INPUTS232B.json'
            inventory = json.loads(inventory_path.read_text())
            entries = [item for item in inventory['files'] if item['path'] == relative]
            self.assertEqual(len(entries), 1)
            entries[0]['bytes'] = path.stat().st_size
            entries[0]['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
            inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
            with self.assertRaisesRegex(ValueError, expected):
                producer.check_candidate(target)

    def test_grade_inflation_is_rejected_even_with_updated_input_digest(self):
        self.reject_changed_field('bound-model-response232B.json',
                                  lambda value: value.update(millennium_score=9.0),
                                  'Only actual version_id')

    def test_dropping_material_entry_is_rejected(self):
        self.reject_changed_field('bound-model-response232B.json',
                                  lambda value: value['unresolved_material_objections'].pop(),
                                  'Only actual version_id')

    def test_false_human_signoff_is_rejected(self):
        self.reject_changed_field('metadata.json',
                                  lambda value: value['screening'].update(human_signoff=True),
                                  'No false screening pass')

    def test_different_native_license_is_rejected(self):
        self.reject_changed_field('NATIVE-AUTHORITY-EVIDENCE.json',
                                  lambda value: value['working_permission'].update(license='CC0-1.0'),
                                  'Actual exact Working permission')

    def test_private_bearer_key_cannot_enter_public_projection(self):
        self.reject_changed_field('NATIVE-AUTHORITY-EVIDENCE.json',
                                  lambda value: value.update(agent_token='SYNTHETIC-NEGATIVE-CONTROL'),
                                  'Only non-secret')
