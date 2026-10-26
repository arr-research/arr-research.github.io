import base64
import json
import unittest

from test_external_editorial import ExternalEditorialTests
from services.intake import app as a
from services.intake.deploy.editorial_ssh import parse_request, dispatch, MAX_REQUEST


class EditorialSSHParserTests(unittest.TestCase):
    def test_rejects_shell_paths_duplicate_fields_and_unbounded_input(self):
        good = {'operation': 'inspect-case', 'submission_id': 'SUB-'+'A'*16,
                'manuscript_sha256': 'a'*64}
        raw = json.dumps(good).encode()
        self.assertEqual(parse_request(raw, 'airr-editorial-v1')[0], good)
        for command in ['', 'sh', 'airr-editorial-v1; id', 'scp -t /root/file']:
            with self.assertRaises(ValueError):
                parse_request(raw, command)
        for update in [{'operation': 'shell'}, {'path': '/etc/shadow'},
                       {'submission_id': '../../etc/shadow'}, {'manuscript_sha256': '0'},
                       {'operation': ['inspect-case']}]:
            with self.assertRaises(ValueError):
                parse_request(json.dumps({**good, **update}).encode(), 'airr-editorial-v1')
        for raw in [b' '* (MAX_REQUEST+1), b'{"operation":"shell","operation":"inspect-case"}', b'[]']:
            with self.assertRaises(ValueError):
                parse_request(raw, 'airr-editorial-v1')


class EditorialSSHWorkflowTests(ExternalEditorialTests):
    def call(self, operation, e, **kwargs):
        request = {'operation': operation, 'submission_id': e['submission_id'],
                   'manuscript_sha256': e['manuscript_sha256'], **kwargs}
        request, blobs = parse_request(json.dumps(request).encode(), 'airr-editorial-v1')
        return dispatch(self.app, a, request, blobs)

    def encoded(self, value):
        return base64.b64encode(json.dumps(value).encode()).decode()

    def test_exact_bound_decision_and_permission_remain_separate(self):
        e = self.prepared_case()
        initial = self.call('inspect-case', e)
        self.assertTrue(initial['model_gate_ready'])
        self.assertIsNone(initial['publication_permission'])
        self.assertNotIn('stored_name', initial['submission'])
        self.assertNotIn('email', initial['submission'])
        with self.assertRaises(ValueError):
            self.call('inspect-case', {**e, 'manuscript_sha256':'0'*64})
        with self.assertRaises(ValueError):
            self.call('record-external-founder-decision', e, evidence=self.encoded({**e, 'manuscript_sha256':'0'*64}))
        result = self.call('record-external-founder-decision', e, evidence=self.encoded(e))
        self.assertEqual(result['status'], 'accepted_for_publication')
        self.assertIsNone(self.call('inspect-case', e)['publication_permission'])
        with self.assertRaises(ValueError):
            self.call('record-external-founder-decision', e, evidence=self.encoded(e))
        p = {k:v for k,v in e.items() if k not in {'decision','reason','report_sha256'}}
        p.update(license='LicenseRef-Author-Retained', distribution_scope=['exact_manuscript','assessment_reports','associated_sources'], rights_basis='The author retains copyright and explicitly permits AIRR to distribute these exact files; no additional public reuse licence is granted.')
        self.call('record-external-founder-publication', e, evidence=self.encoded(p))
        self.assertEqual(self.call('inspect-case', e)['publication_permission']['license'], 'LicenseRef-Author-Retained')

    def test_no_release_without_permission_or_for_another_paper(self):
        e = self.prepared_case()
        binding = self.call('inspect-case', e)['historical_binding']
        url = 'https://github.com/arr-research/arr-research.github.io/releases/tag/' + binding['paper_id'] + '-' + binding['version']
        for bad in ['https://evil.example/release', url + '?token=secret', url.replace(binding['paper_id'], 'ARR-2026-'+'Z'*16)]:
            with self.assertRaises(ValueError):
                self.call('mark-published', e, release_url=bad)
        with self.assertRaises(ValueError):
            self.call('mark-published', e, release_url=url)

    def test_material_objections_and_non_founder_still_block(self):
        e = self.prepared_case(False)
        with self.assertRaises(ValueError):
            self.call('record-external-founder-decision', e, evidence=self.encoded(e))
        with self.app.app_context():
            a.get_db().execute("UPDATE submissions SET authors='Another author' WHERE id=?", (e['submission_id'],))
            a.get_db().commit()
        with self.assertRaises(ValueError):
            self.call('inspect-case', e)


def load_tests(loader, tests, pattern):
    # Reuse fixtures without rerunning their inherited suites in this module.
    suite = unittest.TestSuite()
    for cls in [EditorialSSHParserTests, EditorialSSHWorkflowTests]:
        for name in cls.__dict__:
            if name.startswith('test_'):
                suite.addTest(cls(name))
    return suite
