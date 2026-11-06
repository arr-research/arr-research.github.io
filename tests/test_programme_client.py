# SPDX-License-Identifier: AGPL-3.0-or-later
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from unittest.mock import patch

from scripts import airr_programme as client
from scripts import airr_submit as intake


class ProgrammeClientTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.credential = self.root/'programme.dpapi'
        self.pdf = self.root/'paper.pdf'
        self.pdf.write_bytes(b'%PDF-1.4\nsynthetic client fixture\n')
        self.digest = hashlib.sha256(self.pdf.read_bytes()).hexdigest()
        self.job = self.root/'job.json'
        self.data = {'pdf': str(self.pdf), 'metadata': {'sha256': self.digest, 'authors': 'Fixture author'},
                     'idempotency_key': 'programme-client-fixture-001'}
        intake.atomic_json(self.job, self.data)

    def test_direct_script_help_outside_repository_import_context(self):
        before = {p.name for p in self.root.iterdir()}
        result = subprocess.run([sys.executable, str(Path(client.__file__).resolve()), '--help'],
                                cwd=self.root, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('initialize', result.stdout)
        self.assertEqual({p.name for p in self.root.iterdir()}, before)

    def test_initialize_reuses_protected_secret_and_exposes_only_fingerprint(self):
        first = client.initialize(self.credential)
        raw = self.credential.read_bytes()
        token = intake.load_credential(self.credential)['agent_token']
        second = client.initialize(self.credential)
        self.assertEqual(first, second)
        self.assertEqual(self.credential.read_bytes(), raw)
        self.assertNotIn(token, json.dumps(first))
        self.assertFalse(first['server_authorization_performed'])
        self.assertEqual(first['controller_token_sha256'], hashlib.sha256(token.encode()).hexdigest())
        ordinary = self.root/'ordinary.dpapi'
        intake.save_credential(ordinary, {'agent_token': 'A'*43})
        with self.assertRaises(intake.ClientError):
            client.fingerprint(ordinary)

    def test_exact_revision_routing_binding_and_cached_receipt(self):
        client.initialize(self.credential)
        binding = {'sha256': self.digest, 'paper_id': 'ARR-2026-'+'A'*16, 'version': 'v2'}
        bp = self.root/'binding.json'
        bp.write_text(json.dumps(binding))
        issued = {'request_id': 'AGT-'+'B'*24, 'agent_token': 'C'*43, 'expires_at': '2026-11-07T00:00:00+00:00'}
        with patch.object(intake, 'call', return_value=issued) as network:
            public = client.grant(self.job, self.credential, 'Real declared agent', 'backend unexposed', bp)
        self.assertNotIn(issued['agent_token'], json.dumps(public))
        self.assertEqual(network.call_args.args[1], '/api/v1/programme-artifact-grants')
        receipt = {'registration_number': 'SUB-'+'D'*16, 'sha256': self.digest,
                   'size_bytes': self.pdf.stat().st_size, 'historical_revision': binding}
        with patch.object(intake, 'call', side_effect=[{'state': 'approved', 'intake_open': True}, receipt]) as network:
            self.assertEqual(client.submit(self.job), receipt)
            self.assertEqual(network.call_args.args[1], '/api/v1/revisions')
            self.assertEqual(network.call_args.args[4]['Idempotency-Key'], self.data['idempotency_key'])
        with patch.object(intake, 'call', side_effect=AssertionError('Cached receipt must avoid network')):
            self.assertEqual(client.submit(self.job), receipt)
        with patch.object(intake, 'call') as network:
            with self.assertRaises(intake.ClientError):
                client.grant(self.job, self.credential, 'Changed identity', 'different', bp)
            network.assert_not_called()
        permission = {'submission_id': receipt['registration_number'], 'sha256': self.digest,
                      'publication_permission_recorded': True, 'public_status': 'working_paper', 'published': False}
        with patch.object(intake, 'call', return_value=permission):
            self.assertEqual(client.working_permission(self.job, self.credential), permission)

    def test_wrong_receipt_binding_and_changed_pdf_do_not_save_receipt(self):
        client.initialize(self.credential)
        binding = {'sha256': self.digest, 'paper_id': 'ARR-2026-'+'A'*16, 'version': 'v2'}
        bp = self.root/'binding.json'
        bp.write_text(json.dumps(binding))
        issued = {'request_id': 'AGT-'+'B'*24, 'agent_token': 'C'*43}
        with patch.object(intake, 'call', return_value=issued):
            client.grant(self.job, self.credential, 'Declared agent', 'declared version', bp)
        bad = {'registration_number': 'SUB-'+'D'*16, 'sha256': self.digest,
               'size_bytes': self.pdf.stat().st_size, 'historical_revision': {**binding, 'version': 'v9'}}
        with patch.object(intake, 'call', side_effect=[{'state': 'approved', 'intake_open': True}, bad]):
            with self.assertRaises(intake.ClientError):
                client.submit(self.job)
        self.assertFalse(Path(str(self.job)+'.receipt.json').exists())
        self.pdf.write_bytes(b'%PDF-altered fixture')
        with patch.object(intake, 'call') as network:
            with self.assertRaises(intake.ClientError):
                client.submit(self.job)
            network.assert_not_called()


if __name__ == '__main__':
    unittest.main()
