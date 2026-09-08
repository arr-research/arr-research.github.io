"""Submission boundaries across browser, delegated agents and shared networks."""
import io
import time
import unittest
from unittest.mock import patch

import test_intake as fixtures
import test_agent_intake as agents
from services.intake.app import get_db, rate_subject


class SubmissionLimitTests(unittest.TestCase):
    setUp = fixtures.IntakeTests.setUp
    tearDown = fixtures.IntakeTests.tearDown
    request_grant = agents.AgentIntakeTests.request_grant
    begin_confirmation = agents.AgentIntakeTests.begin_confirmation
    approve = agents.AgentIntakeTests.approve
    agent_upload = agents.AgentIntakeTests.upload

    def human_upload(self, client):
        client.get('/submit')
        with client.session_transaction() as state:
            csrf = state['csrf_token']
        with patch('services.intake.app.scan_file', return_value=('clean', 'test scanner')):
            response = client.post('/submit', data={
                'csrf_token': csrf, 'title': 'A test research paper',
                'authors': 'Test author', 'abstract': 'A' * 120,
                'primary_subject': 'airr-quantum-information',
                'adult': 'on', 'authority': 'on', 'terms': 'on',
                'privacy': 'on', 'ai_review_opt_in': 'on',
                'manuscript': (io.BytesIO(b'%PDF-1.7\ntest bytes'), 'test.pdf'),
            })
        response.request.environ['wsgi.input'].close()
        return response

    def test_tenth_mixed_submission_succeeds_eleventh_fails_and_other_account_can_submit(self):
        grant = self.request_grant()
        human, _, _ = self.approve(grant)
        for _ in range(4):
            self.assertEqual(self.human_upload(human).status_code, 302)
        for index in range(3):
            response = self.agent_upload(grant, key=f'mixed-paper-{index}')
            self.assertEqual(response.status_code, 201, response.data)
        for _ in range(2):
            self.assertEqual(self.human_upload(human).status_code, 302)
        tenth = self.agent_upload(grant, key='mixed-tenth-paper')
        self.assertEqual(tenth.status_code, 201, tenth.data)
        self.assertEqual(self.human_upload(human).status_code, 429)
        self.assertEqual(self.agent_upload(grant, key='mixed-eleventh-paper').status_code, 429)
        retry = self.agent_upload(grant, key='mixed-tenth-paper')
        self.assertEqual(retry.status_code, 200, retry.data)
        self.assertEqual(retry.get_json()['registration_number'], tenth.get_json()['registration_number'])
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 10)
        other, _, _ = self.approve(self.request_grant(), email='other@example.org')
        self.assertEqual(self.human_upload(other).status_code, 302)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 11)

    def test_ten_form_submissions_and_rolling_window_expiry(self):
        for _ in range(10):
            self.assertEqual(self.human_upload(self.client).status_code, 302)
        self.assertEqual(self.human_upload(self.client).status_code, 429)
        with self.app.app_context():
            get_db().execute('UPDATE rate_events SET occurred_at=occurred_at-86401')
            get_db().commit()
        self.assertEqual(self.human_upload(self.client).status_code, 302)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 11)

    def test_existing_connection_counters_enforce_fiftieth_attempt_boundary(self):
        grant = self.request_grant()
        self.approve(grant)
        with self.app.app_context():
            rows = [(bucket, rate_subject('127.0.0.1'), int(time.time()))
                    for bucket in ('submit', 'agent-submit-ip') for _ in range(49)]
            get_db().executemany('INSERT INTO rate_events(bucket,subject_hash,occurred_at) VALUES(?,?,?)', rows)
            get_db().commit()
        self.assertEqual(self.human_upload(self.client).status_code, 302)
        self.assertEqual(self.human_upload(self.client).status_code, 429)
        self.assertEqual(self.agent_upload(grant, key='network-fiftieth').status_code, 201)
        self.assertEqual(self.agent_upload(grant, key='network-fifty-first').status_code, 429)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 2)
