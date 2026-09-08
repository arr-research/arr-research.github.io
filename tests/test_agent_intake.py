"""Delegation ownership, private-workspace authorization, upload integrity, retries and revocation."""
from datetime import timedelta
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import urlsplit
import unittest
import tempfile
from unittest.mock import patch

import test_intake as fixtures
from services.intake.app import get_db, iso, now


class AgentIntakeTests(unittest.TestCase):
    def setUp(self):
        fixtures.IntakeTests.setUp(self)

    def tearDown(self):
        self.temp.cleanup()

    def request_grant(self):
        response = self.client.post('/api/v1/agent-requests',json={
            'agent_name':'Research assistant','agent_version':'test-model-1',
            'purpose':'Submit the research PDF authorized by its corresponding author.'})
        self.assertEqual(response.status_code,201,response.data)
        grant = response.get_json()
        self.assertEqual(grant['state'],'pending')
        return grant

    def begin_confirmation(self,grant,email='responsible@example.org'):
        human = self.app.test_client()
        alias = email.split('@')[0]
        human.get('/account/register')
        with human.session_transaction() as state:
            csrf = state['csrf_token']
        response = human.post('/account/register', data={'csrf_token':csrf,'alias':alias,
            'password':'a-long-test-password-123','confirm_password':'a-long-test-password-123',
            'identity_kind':'human','adult':'on','authority':'on','terms':'on','privacy':'on'})
        self.assertEqual(response.status_code,200,response.data)
        path = urlsplit(grant['authorization_url']).path
        self.assertEqual(human.get(path).status_code,200)
        return human,path

    def approve(self,grant,email='responsible@example.org'):
        human,path = self.begin_confirmation(grant,email)
        with human.session_transaction() as state:
            csrf = state['csrf_token']
        response = human.post(path,data={'csrf_token':csrf,'adult':'on','authority':'on','terms':'on','privacy':'on','screening':'on'})
        self.assertEqual(response.status_code,200,response.data)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0],0)
        return human,'/account/grants/' + grant['request_id'] + '/revoke',csrf

    def upload(self,grant,key='paper-retry-001',metadata_changes=None,pdf=b'%PDF-1.7\nagent fixture',scan='clean'):
        value = {'title':'An exact research result','authors':'Responsible Author','abstract':'A' * 120,
            'primary_subject':'airr-quantum-information','secondary_subjects':[],'specific_topic':'',
            'sha256':hashlib.sha256(pdf).hexdigest(),'ai_disclosure':'The named agent prepared and submitted the PDF under the author permission.',
            'operator_conflict':False,'rights_confirmed':True}
        value.update(metadata_changes or {})
        with patch('services.intake.app.scan_file',return_value=(scan,'fixture scanner')):
            response = self.client.post('/api/v1/submissions',headers={'Authorization':'Bearer ' + grant['agent_token'],
                'Idempotency-Key':key},data={'metadata':json.dumps(value),'manuscript':(io.BytesIO(pdf),'paper.pdf')})
        # Werkzeug's test client may spool its synthetic outgoing multipart body.
        response.request.environ['wsgi.input'].close()
        return response

    def test_an_agent_cannot_upload_before_workspace_confirmation(self):
        grant = self.request_grant()
        self.assertEqual(self.upload(grant).status_code,403)
        human,path = self.begin_confirmation(grant)
        self.assertEqual(self.upload(grant).status_code,403)
        # A page preview and a forged POST do not approve anything.
        human.get(path)
        self.assertEqual(self.upload(grant).status_code,403)
        self.assertEqual(human.post(path,data={'action':'approve'}).status_code,400)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0],0)

    def test_approved_agent_receives_private_receipt_and_disclosed_provenance(self):
        grant = self.request_grant()
        self.approve(grant)
        response = self.upload(grant)
        self.assertEqual(response.status_code,201,response.data)
        receipt = response.get_json()
        self.assertFalse(receipt['published'])
        self.assertTrue(receipt['donation']['optional'])
        with self.app.app_context():
            row = get_db().execute('SELECT * FROM submissions').fetchone()
            self.assertEqual(row['submission_channel'],'agent')
            self.assertEqual(row['status'],'eligible')
            self.assertEqual(json.loads(row['agent_provenance_json'])['name'],'Research assistant')
            self.assertIsNone(get_db().execute("SELECT actor_user_id FROM audit_log WHERE event='submission_received'").fetchone()[0])
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM assessment_plans').fetchone()[0],0)
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0],0)
        self.assertEqual(self.client.get(response.headers['Location']).status_code,401)
        own = self.client.get(response.headers['Location'],headers={'Authorization':'Bearer ' + grant['agent_token']})
        self.assertEqual(own.status_code,200)

    def test_retries_do_not_create_duplicate_papers_or_consume_another_permission(self):
        grant = self.request_grant()
        self.approve(grant)
        first = self.upload(grant)
        second = self.upload(grant)
        self.assertEqual(first.status_code,201,first.data)
        self.assertEqual(second.status_code,200,second.data)
        self.assertEqual(first.get_json()['registration_number'],second.get_json()['registration_number'])
        self.assertEqual(self.upload(grant,metadata_changes={'title':'Different paper'}).status_code,409)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0],1)
            self.assertEqual(get_db().execute('SELECT uses FROM agent_grants').fetchone()[0],1)
        self.assertEqual(len(list(Path(self.app.config['QUARANTINE']).glob('*.pdf'))),1)

    def test_revoke_works_while_intake_is_paused_and_cannot_be_undone_by_replay(self):
        grant = self.request_grant()
        human,path,csrf = self.approve(grant)
        self.app.config['INTAKE_OPEN'] = False
        self.assertEqual(human.post(path,data={'csrf_token':csrf,'action':'revoke'}).status_code,302)
        self.app.config['INTAKE_OPEN'] = True
        self.assertEqual(self.upload(grant).status_code,403)
        self.assertEqual(human.post(urlsplit(grant['authorization_url']).path,data={'csrf_token':csrf,'action':'approve'}).status_code,409)

    def test_expired_exhausted_and_outdated_delegations_cannot_receive_a_pdf(self):
        grant = self.request_grant()
        self.approve(grant)
        for sql in ("UPDATE agent_grants SET expires_at='2000-01-01T00:00:00+00:00'",
                    "UPDATE agent_grants SET expires_at='2099-01-01T00:00:00+00:00',uses=5",
                    "UPDATE agent_grants SET uses=0,terms_version='old'"):
            with self.app.app_context():
                get_db().execute(sql)
                get_db().commit()
            self.assertEqual(self.upload(grant).status_code,403)
        self.assertEqual(list(Path(self.app.config['QUARANTINE']).glob('*.pdf')),[])

    def test_pdf_checksum_and_signature_failure_leave_no_case_or_file(self):
        grant = self.request_grant()
        self.approve(grant)
        self.assertEqual(self.upload(grant,metadata_changes={'sha256':'0' * 64}).status_code,400)
        self.assertEqual(self.upload(grant,pdf=b'not a PDF').status_code,400)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0],0)
            self.assertEqual(get_db().execute('SELECT uses FROM agent_grants').fetchone()[0],0)
        self.assertEqual(list(Path(self.app.config['QUARANTINE']).glob('*.pdf')),[])

    def test_scanner_failure_preserves_quarantine_and_infection_erases_the_bytes(self):
        grant = self.request_grant()
        self.approve(grant)
        error = self.upload(grant,scan='error')
        infected = self.upload(grant,key='infected-002',scan='infected')
        self.assertEqual(error.status_code,201,error.data)
        self.assertEqual(error.get_json()['status'],'quarantined')
        self.assertEqual(infected.get_json()['status'],'removed')
        self.assertEqual(len(list(Path(self.app.config['QUARANTINE']).glob('*.pdf'))),1)

    def test_another_grant_and_editor_cookie_cannot_read_or_upload(self):
        first = self.request_grant()
        self.approve(first)
        response = self.upload(first)
        second = self.request_grant()
        self.approve(second,'second@example.org')
        self.assertEqual(self.client.get(response.headers['Location'],headers={
            'Authorization':'Bearer ' + second['agent_token']}).status_code,404)
        with self.app.app_context():
            operator = get_db().execute("SELECT id FROM users WHERE role='operator'").fetchone()[0]
        with self.client.session_transaction() as session:
            session['user_id'] = operator
        self.assertEqual(self.client.post('/api/v1/submissions').status_code,401)

    def test_no_configuration_switch_bypasses_the_production_launch_gate(self):
        for changes in ({'INTAKE_OPEN':False},{'INTAKE_OPEN':True,'TESTING':False,'LAUNCH_APPROVAL_FILE':'missing.json'}):
            self.app.config.update(changes)
            self.assertEqual(self.client.post('/api/v1/agent-requests',json={}).status_code,503)
            self.assertEqual(self.client.post('/api/v1/submissions').status_code,503)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM agent_grants').fetchone()[0],0)

    def test_contact_and_confirmation_secrets_are_erased_after_pending_expiry(self):
        grant = self.request_grant()
        self.begin_confirmation(grant)
        with self.app.app_context():
            get_db().execute('UPDATE agent_grants SET request_expires_at=?',(iso(now()-timedelta(days=1)),))
            get_db().commit()
        result = self.app.test_cli_runner().invoke(args=['retention-sweep'])
        self.assertEqual(result.exit_code,0,result.output)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM agent_grants').fetchone()[0],0)
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM agent_mail').fetchone()[0],0)
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0],0)

    def test_large_multipart_temporary_file_stays_inside_private_storage(self):
        grant = self.request_grant()
        self.approve(grant)
        with patch('services.intake.app.tempfile.SpooledTemporaryFile',wraps=tempfile.SpooledTemporaryFile) as spool:
            response = self.upload(grant,pdf=b'%PDF-' + b'x' * 700000)
        self.assertEqual(response.status_code,201,response.data)
        self.assertTrue(spool.called)
        self.assertEqual(spool.call_args.kwargs['dir'],self.app.config['QUARANTINE'])
        self.assertEqual(list(Path(self.app.config['QUARANTINE']).glob('.upload-*')),[])
