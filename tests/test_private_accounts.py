"""Authentication, isolation and no-email editorial workflow regressions."""
import re
import unittest
from unittest.mock import patch

import test_intake as fixtures
from services.intake.app import get_db, iso


class PrivateAccountTests(unittest.TestCase):
    def setUp(self):
        fixtures.IntakeTests.setUp(self)

    def tearDown(self):
        self.temp.cleanup()

    def form_token(self, client, path):
        client.get(path)
        with client.session_transaction() as state:
            return state['csrf_token']

    def register(self, alias='quiet-researcher', kind='human'):
        client = self.app.test_client()
        token = self.form_token(client, '/account/register')
        response = client.post('/account/register', data={'csrf_token':token, 'alias':alias,
            'password':'long-password-for-testing', 'confirm_password':'long-password-for-testing',
            'identity_kind':kind, 'adult':'on', 'authority':'on', 'terms':'on', 'privacy':'on'})
        self.assertEqual(response.status_code, 200, response.data)
        recovery = re.search(rb'Recovery code: ([A-Za-z0-9_-]{43})', response.data).group(1).decode()
        return client, recovery

    def test_alias_is_private_and_only_hashes_are_stored(self):
        client, recovery = self.register(kind='agent')
        with self.app.app_context():
            row = get_db().execute("SELECT p.*,u.email,u.password_hash FROM private_accounts p JOIN users u ON u.id=p.user_id WHERE alias='quiet-researcher'").fetchone()
            self.assertEqual(row['identity_kind'], 'agent')
            self.assertTrue(row['email'].endswith('@accounts.invalid'))
            self.assertNotEqual(row['recovery_hash'], recovery)
            self.assertNotIn('long-password-for-testing', row['password_hash'])
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0], 0)
        with client.session_transaction() as state:
            self.assertNotIn(recovery, str(dict(state)))
        page = client.get('/submit')
        self.assertNotIn(b'name="email"', page.data)
        self.assertNotIn(b'name="display_name"', page.data)

    def test_case_id_and_other_account_cannot_access_private_case_or_file(self):
        owner = fixtures.IntakeTests('runTest')
        # Reuse the same underlying fixture without invoking another setUp.
        owner.__dict__.update(self.__dict__)
        case_id = owner.upload(fields={'authors':''})
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT authors FROM submissions').fetchone()[0], 'Anonymous')
        other, _ = self.register()
        for path in ('/case/'+case_id, '/case/'+case_id+'/file'):
            self.assertEqual(other.get(path).status_code, 404)
            self.assertEqual(self.app.test_client().get(path).status_code, 404)
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            response.close()
        self.assertEqual(other.post('/case/'+case_id, data={'csrf_token':self.form_token(other,'/account'), 'action':'withdraw'}).status_code, 404)
        self.assertEqual(other.get('/admin/submission/'+case_id).status_code, 403)

    def test_recovery_invalidates_existing_sessions_and_revokes_grants(self):
        original, recovery = self.register()
        with original.session_transaction() as state:
            user_id = state['user_id']
        with self.app.app_context():
            get_db().execute("INSERT INTO agent_grants(id,claim_hash,setup_hash,agent_name,agent_version,purpose,state,created_at,request_expires_at,owner_user_id) VALUES('AGT-test','claim','setup','test','1','test grant','approved',?,?,?)", (iso(),iso(),user_id))
            get_db().commit()
        fresh = self.app.test_client()
        csrf = self.form_token(fresh, '/account/recover')
        data = {'csrf_token':csrf,'alias':'quiet-researcher','recovery_code':recovery,
                'password':'replacement-password-123','confirm_password':'replacement-password-123'}
        response = fresh.post('/account/recover', data=data)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertNotIn(recovery.encode(), response.data)
        self.assertEqual(original.get('/account').status_code, 302)
        with self.app.app_context():
            self.assertEqual(get_db().execute("SELECT state FROM agent_grants WHERE id='AGT-test'").fetchone()[0], 'revoked')
        data['csrf_token'] = self.form_token(fresh,'/account/recover')
        self.assertEqual(fresh.post('/account/recover',data=data).status_code, 400)

    def test_login_works_while_intake_is_paused_and_does_not_use_editor_login(self):
        client,_ = self.register()
        self.app.config['INTAKE_OPEN'] = False
        outsider = self.app.test_client()
        token = self.form_token(outsider,'/account/login')
        response = outsider.post('/account/login', data={'csrf_token':token,'alias':'QUIET-RESEARCHER','password':'long-password-for-testing'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(outsider.get('/account').status_code,200)
        self.assertEqual(outsider.get('/submit').status_code,503)
        self.assertEqual(outsider.get('/account/register').status_code,503)

    def test_contact_fields_and_missing_csrf_cannot_create_an_account(self):
        client = self.app.test_client()
        self.assertEqual(client.post('/account/register',data={}).status_code,400)
        token = self.form_token(client,'/account/register')
        self.assertEqual(client.post('/account/register',data={'csrf_token':token,'email':'person@example.org'}).status_code,400)

    def test_editor_and_author_messages_stay_in_the_case_without_email(self):
        owner = fixtures.IntakeTests('runTest')
        owner.__dict__.update(self.__dict__)
        case_id = owner.upload()
        csrf = owner.login_session('operator@example.org')
        with patch('services.intake.app.send_mail') as smtp:
            response = self.client.post('/admin/submission/'+case_id+'/message', data={'csrf_token':csrf,'body':'Please explain the assumptions of your main theorem.'})
            self.assertEqual(response.status_code,302)
            smtp.assert_not_called()
        owner.login_session('direct-author@accounts.invalid')
        self.assertIn(b'Please explain', self.client.get('/case/'+case_id).data)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0],0)

    def test_newly_discovered_conflict_is_disclosed_without_reversing_acceptance(self):
        owner = fixtures.IntakeTests('runTest')
        owner.__dict__.update(self.__dict__)
        case_id = owner.upload()
        with self.app.app_context():
            get_db().execute("UPDATE submissions SET status='accepted_for_publication' WHERE id=?", (case_id,))
            get_db().commit()
        csrf = owner.login_session('operator@example.org')
        result = self.client.post('/admin/submission/'+case_id+'/conflict', data={'csrf_token':csrf,'reason':'The founder is an author under a private alias.'})
        self.assertEqual(result.status_code,302)
        with self.app.app_context():
            row = get_db().execute('SELECT status,operator_conflict FROM submissions WHERE id=?', (case_id,)).fetchone()
            self.assertEqual(tuple(row), ('accepted_for_publication',1))
        self.assertEqual(self.client.get('/admin/submission/'+case_id+'/release-package').status_code,409)

    def test_password_change_requires_current_secret_and_replaces_recovery(self):
        client, recovery = self.register()
        csrf = self.form_token(client,'/account')
        data = {'csrf_token':csrf,'current_password':'wrong-password','password':'changed-password-long','confirm_password':'changed-password-long'}
        self.assertEqual(client.post('/account/password',data=data).status_code,400)
        data['current_password'] = 'long-password-for-testing'
        response = client.post('/account/password',data=data)
        self.assertEqual(response.status_code,200)
        self.assertNotIn(recovery.encode(),response.data)
        stranger=self.app.test_client()
        csrf=self.form_token(stranger,'/account/login')
        self.assertEqual(stranger.post('/account/login',data={'csrf_token':csrf,'alias':'quiet-researcher','password':'changed-password-long'}).status_code,302)
