import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import test_validation as fixtures
from scripts import build_site, arrlib

ROOT = Path(__file__).resolve().parents[1]


class IndependentDiscoveryTests(unittest.TestCase):
    def test_independent_and_delegated_routes_remain_distinct_and_discoverable(self):
        page = build_site.build_agents('/preview', 'https://example.test/preview', 'https://submit.airr.science')
        for link in ('/preview/independent-agents.md', '/preview/independent-agents.openapi.json',
                     '/preview/.well-known/airr-submission.json', '/preview/agent-submissions.md',
                     'https://submit.airr.science/api/v1/independent-agents/policy'):
            self.assertIn(link, page)
        self.assertIn('id="independent"', page)
        self.assertIn('id="anonymous"', page)
        self.assertIn('A human sponsor is not required', page)
        self.assertIn('does not mean intake is currently open', page)
        self.assertNotIn('only archive', page.lower())
        with tempfile.TemporaryDirectory() as directory, patch.object(build_site, 'OUTPUT_DIR', Path(directory)):
            build_site.write_llm_guides([], 'https://example.test/preview')
            guide = (Path(directory)/'llms.txt').read_text(encoding='utf-8')
            self.assertIn('independent-agents.openapi.json', guide)
            self.assertIn('No human sponsor or email is required', guide)

    def test_machine_contract_has_every_case_action_and_no_editor_powers(self):
        spec = json.loads((ROOT/'site/independent-agents.openapi.json').read_text())
        self.assertEqual(spec['openapi'], '3.1.0')
        prefix = '/api/v1/independent-agents'
        for suffix in ('', '/policy', '/me', '/token', '/revoke', '/submissions', '/cases/{case_id}', '/cases/{case_id}/actions'):
            self.assertIn(prefix+suffix, spec['paths'])
        actions = {r['properties']['action']['const'] for r in spec['components']['schemas']['Action']['oneOf']}
        self.assertEqual(actions, {'reply','authorize_plan','request_publication','appeal','withdraw'})
        self.assertFalse(any('/admin' in path for path in spec['paths']))
        self.assertEqual(spec['components']['schemas']['Metadata']['properties']['secondary_subjects']['maxItems'], 2)

    def test_public_anonymous_record_requires_scoped_exact_pdf_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            paper = fixtures.PaperValidationTests.make_paper(self, Path(directory))
            paper.metadata['publication_mode'] = 'anonymous'
            self.assertTrue(any('originality_review' in e for e in arrlib.validate_paper(paper)))
            paper.metadata['integrity']['canonical_sha256'] = 'a'*64
            paper.metadata['originality_review'] = {
                'policy':'AIRR-ORIGINALITY-1.0', 'manuscript_sha256':'a'*64,
                'checked_at':'2026-09-27T10:00:00Z', 'outcome':'no_unresolved_concerns_in_checked_sources',
                'limitations':'Documented specified-source checks, not a guarantee of global originality.'}
            self.assertFalse(any('originality_review' in e for e in arrlib.validate_paper(paper)))
            paper.metadata['originality_review']['manuscript_sha256'] = 'b'*64
            self.assertTrue(any('exact canonical PDF hash' in e for e in arrlib.validate_paper(paper)))
            paper.metadata['originality_review']['private_notes'] = 'must never be public'
            self.assertTrue(any('scoped public summary' in e for e in arrlib.validate_paper(paper)))


if __name__ == '__main__':
    unittest.main()
