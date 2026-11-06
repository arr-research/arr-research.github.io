# SPDX-License-Identifier: AGPL-3.0-or-later
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from reviewnotelib import load_review_note


class NarrativeReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paper = SimpleNamespace(path=self.root, metadata={'version_id': 'arr:version:test', 'integrity': {'canonical_sha256': 'a'*64}})
        self.note = {'schema_version': '1.0', 'version_id': 'arr:version:test', 'canonical_sha256': 'a'*64,
                     'provider': 'Provider fixture', 'ui_label': 'Observed UI label', 'backend_identity': None,
                     'recorded_at': '2026-11-06T02:30:00+00:00', 'score': 7.6,
                     'scale': 'Original narrative rubric; no inferred criterion stars',
                     'recommendation': 'Working paper with retained minor-revision qualification',
                     'context': 'Nonblind; independence unestablished', 'summary': 'Original report with all objections preserved.', 'report_files': []}
        for name in ('original.txt', 'context.json'):
            raw = ('Original '+name).encode()
            (self.root/name).write_bytes(raw)
            self.note['report_files'].append({'label': name, 'path': name, 'sha256': hashlib.sha256(raw).hexdigest()})

    def write(self):
        (self.root/'MODEL-REVIEW-CONTEXT.json').write_text(json.dumps(self.note))

    def test_preserves_original_score_and_unknown_backend_without_criterion_stars(self):
        self.assertIsNone(load_review_note(self.paper))
        self.write()
        result = load_review_note(self.paper)
        self.assertEqual(result['score'], 7.6)
        self.assertIsNone(result['backend_identity'])
        self.assertNotIn('criteria', result)

    def test_rejects_inherited_pdf_and_version_identity(self):
        for key, bad in [('version_id', 'another version'), ('canonical_sha256', 'b'*64), ('backend_identity', 'invented backend'), ('score', True)]:
            original = self.note[key]
            self.note[key] = bad
            self.write()
            with self.assertRaises(ValueError):
                load_review_note(self.paper)
            self.note[key] = original

    def test_rejects_altered_original_report_and_path_escape(self):
        self.write()
        (self.root/'original.txt').write_text('altered report')
        with self.assertRaises(ValueError):
            load_review_note(self.paper)
        self.note['report_files'][0]['path'] = '../outside.txt'
        self.write()
        with self.assertRaises(ValueError):
            load_review_note(self.paper)
