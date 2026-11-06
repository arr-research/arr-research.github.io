"""Agent-client recovery tests use synthetic PDFs and a fake API; no real cases."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import airr_submit as client


class AgentClientTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.pdf = self.root / 'manuscript.pdf'
        self.pdf.write_bytes(b'%PDF-1.7\nsynthetic client fixture\n%%EOF')
        self.meta = self.root / 'metadata.json'
        self.meta.write_text(json.dumps({
            'title': 'Synthetic client test', 'authors': 'Test author',
            'abstract': 'A synthetic abstract used only by the isolated client tests. ' * 2,
            'primary_subject': 'airr-matrix-analysis', 'secondary_subjects': [],
            'specific_topic': '', 'ai_disclosure': 'Synthetic test; no real manuscript or model assessment.',
            'operator_conflict': False, 'rights_confirmed': True}), encoding='utf-8')
        self.job = self.root / 'deposit.json'
        self.cred = self.root / 'credential'
        self.token = 't' * 43
        self.permission = {'agent_token': self.token, 'request_id': 'AGT-' + 'A' * 24,
                           'authorization_url': client.ORIGIN + '/agents/authorize/' + 's' * 43}
        self.state = {'state': 'approved', 'uploads_remaining': 5, 'intake_open': True}

    def prepare(self):
        return client.prepare(self.pdf, self.meta, self.job)

    def receipt(self):
        return {'registration_number': 'SUB-' + 'B' * 16,
                'sha256': hashlib.sha256(self.pdf.read_bytes()).hexdigest(),
                'size_bytes': self.pdf.stat().st_size, 'published': False}

    def test_prepare_is_local_and_does_not_replace_retry_key(self):
        with patch.object(client, 'call') as api:
            result = self.prepare()
            self.assertFalse(result['sent'])
            original = self.job.read_bytes()
            with self.assertRaises(client.ClientError):
                self.prepare()
            self.assertEqual(original, self.job.read_bytes())
            api.assert_not_called()

    def test_modified_pdf_is_refused_before_any_network_call(self):
        self.prepare()
        self.pdf.write_bytes(b'%PDF-1.7\nchanged\n%%EOF')
        with patch.object(client, 'call') as api:
            with self.assertRaisesRegex(client.ClientError, 'PDF changed'):
                client.submit(self.job, self.cred)
            api.assert_not_called()

    def test_uncertain_upload_reuses_key_and_saves_verified_receipt(self):
        self.prepare()
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call') as api:
            api.side_effect = [self.state, client.ClientError('Response uncertain.')]
            with self.assertRaisesRegex(client.ClientError, 'uncertain'):
                client.submit(self.job, self.cred)
            first = api.call_args
            self.assertEqual(json.loads(self.job.read_text())['grant_id'], self.permission['request_id'])
            api.side_effect = [self.state, self.receipt()]
            received = client.submit(self.job, self.cred)
            second = api.call_args
            self.assertEqual(first.args[4]['Idempotency-Key'], second.args[4]['Idempotency-Key'])
            self.assertIn(self.pdf.read_bytes(), second.args[3])
            self.assertEqual(received, self.receipt())
            self.assertTrue(Path(str(self.job) + '.receipt.json').exists())
            api.reset_mock()
            self.assertEqual(client.submit(self.job, self.cred), received)
            api.assert_not_called()

    def test_wrong_receipt_is_not_saved(self):
        self.prepare()
        wrong = {**self.receipt(), 'sha256': '0' * 64}
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call', side_effect=[self.state, wrong]):
            with self.assertRaisesRegex(client.ClientError, 'does not match'):
                client.submit(self.job, self.cred)
        self.assertFalse(Path(str(self.job) + '.receipt.json').exists())

    def test_uncertain_job_cannot_be_replayed_with_a_new_grant(self):
        self.prepare()
        job = json.loads(self.job.read_text())
        job['grant_id'] = 'AGT-' + 'C' * 24
        client.atomic_json(self.job, job)
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call') as api:
            with self.assertRaisesRegex(client.ClientError, 'different grant'):
                client.submit(self.job, self.cred)
            api.assert_not_called()

    def test_pending_or_usable_grant_is_reused_even_when_replacement_requested(self):
        self.cred.write_bytes(b'old protected credential')
        for state in ['approved', 'pending']:
            with self.subTest(state=state), patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call', return_value={**self.state, 'state': state}) as api, patch.object(client, 'save_credential') as save:
                result = client.authorize(self.cred, replace=True)
                self.assertTrue(result['reused'])
                self.assertEqual(api.call_count, 1)
                save.assert_not_called()

    def test_unrecognized_credential_requires_explicit_recovery_and_preserves_old_bytes(self):
        self.cred.write_bytes(b'old protected credential')
        fresh = {**self.permission, 'state': 'pending', 'expires_at': '2026-11-01T00:00:00Z'}
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call', side_effect=client.ClientError('invalid', 401)) as api:
            with self.assertRaises(client.ClientError):
                client.authorize(self.cred)
            self.assertEqual(api.call_count, 1)
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call', side_effect=[client.ClientError('invalid', 401), fresh]), patch.object(client, 'save_credential') as save:
            result = client.authorize(self.cred, replace=True)
            self.assertNotIn('agent_token', result)
            save.assert_called_once()
        backups = list(self.root.glob('credential.previous-*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), b'old protected credential')

    def test_network_failure_never_replaces_credential(self):
        self.cred.write_bytes(b'old protected credential')
        with patch.object(client, 'load_credential', return_value=self.permission), patch.object(client, 'call', side_effect=client.ClientError('uncertain')) as api, patch.object(client, 'save_credential') as save:
            with self.assertRaises(client.ClientError):
                client.authorize(self.cred, replace=True)
            self.assertEqual(api.call_count, 1)
            save.assert_not_called()
            self.assertFalse(list(self.root.glob('credential.previous-*')))

    def test_windows_existing_helper_credential_roundtrip(self):
        client.save_credential(self.cred, self.permission)
        self.assertEqual(client.load_credential(self.cred), self.permission)
        if client.os.name == 'nt':
            self.assertNotIn(self.token.encode(), self.cred.read_bytes())


if __name__ == '__main__':
    unittest.main()
