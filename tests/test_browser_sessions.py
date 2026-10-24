"""Two authenticated roles may be retained; their permissions never merge."""
import unittest
from datetime import timedelta
from unittest.mock import patch

import test_intake as fixtures
from services.intake.app import get_db, now, totp
from services.intake.workflow import digest


class BrowserSessionTests(unittest.TestCase):
    setUp = fixtures.IntakeTests.setUp
    tearDown = fixtures.IntakeTests.tearDown
    user_id = fixtures.IntakeTests.user_id

    def token(self, path='/'):
        self.client.get(path)
        with self.client.session_transaction() as state:
            return state['csrf_token']

    def editor_login(self, keep=True, independent=False):
        fields = {'csrf_token': self.token('/login'), 'email': 'operator@example.org',
                  'password': 'operator-password-123', 'totp': totp('JBSWY3DPEHPK3PXP')}
        if independent:
            fields.update(email='independent@example.org', password='independent-password-123',
                          totp=totp('JBSWY3DPEHPK3PXQ'))
        if keep:
            fields['keep_other_account'] = 'on'
        return self.client.post('/login', data=fields)

    def author_login(self, keep=True):
        fields = {'csrf_token': self.token('/account/login'), 'alias': 'direct-author',
                  'password': 'workspace-password-123'}
        if keep:
            fields['keep_other_account'] = 'on'
        return self.client.post('/account/login', data=fields)

    def switch(self, role):
        return self.client.post('/session/switch', data={'csrf_token': self.token(), 'role': role})

    def update_user(self, email, **changes):
        with self.app.app_context():
            db = get_db()
            for column, value in changes.items():
                self.assertIn(column, {'active'})
                db.execute(f'UPDATE users SET {column}=? WHERE email=?', (value, email))
            db.commit()

    def revoke_workspace(self):
        with self.app.app_context():
            get_db().execute('UPDATE private_accounts SET credential_version=credential_version+1')
            get_db().commit()

    def test_opt_in_keeps_both_but_only_selected_role_has_permissions(self):
        self.assertIn(b'Add editorial sign-in', self.client.get('/').data)
        self.assertEqual(self.editor_login().status_code, 302)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 200)
        self.assertEqual(self.client.get('/account').status_code, 302)
        page = self.client.get('/')
        self.assertIn(b'Switch to my author workspace', page.data)
        self.assertEqual(self.switch('depositor').status_code, 302)
        self.assertEqual(self.client.get('/account').status_code, 200)
        self.assertEqual(self.client.get('/submit').status_code, 200)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 403)
        self.assertIn(b'Switch to administration', self.client.get('/').data)
        self.assertEqual(self.switch('operator').status_code, 302)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 200)

    def test_reverse_login_order_retains_editor_after_author_password(self):
        self.editor_login(keep=False)
        self.assertEqual(self.author_login().status_code, 302)
        self.assertEqual(self.client.get('/account').status_code, 200)
        self.assertEqual(self.switch('operator').status_code, 302)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 200)

    def test_without_opt_in_login_still_replaces_previous_account(self):
        self.editor_login(keep=False)
        with self.client.session_transaction() as state:
            self.assertNotIn('other_user_id', state)
        self.assertEqual(self.switch('depositor').status_code, 403)
        self.author_login(keep=False)
        self.assertEqual(self.switch('operator').status_code, 403)

    def test_author_password_and_role_parameters_cannot_create_editor_access(self):
        self.author_login()
        response = self.client.post('/session/switch', data={
            'csrf_token': self.token(), 'role': 'operator', 'user_id': self.user_id('operator@example.org')})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 403)

    def test_failed_second_factor_does_not_save_editor_identity(self):
        with patch('services.intake.app.verify_totp', return_value=False):
            self.assertEqual(self.editor_login().status_code, 200)
        with self.client.session_transaction() as state:
            self.assertNotIn('other_user_id', state)
            self.assertEqual(state['user_id'], self.user_id('direct-author@accounts.invalid'))
        self.assertEqual(self.switch('operator').status_code, 403)

    def test_switch_requires_csrf_post_and_exact_retained_role(self):
        self.editor_login()
        self.assertEqual(self.client.get('/session/switch').status_code, 405)
        self.assertEqual(self.client.post('/session/switch', data={'role': 'depositor'}).status_code, 400)
        self.assertEqual(self.switch('independent_editor').status_code, 403)

    def test_recovered_workspace_cannot_be_restored_from_saved_identity(self):
        self.editor_login()
        self.revoke_workspace()
        self.assertEqual(self.client.get('/admin/statistics').status_code, 200)
        self.assertEqual(self.switch('depositor').status_code, 403)
        with self.client.session_transaction() as state:
            self.assertNotIn('other_user_id', state)

    def test_revoked_active_workspace_keeps_independently_authenticated_editor(self):
        self.editor_login()
        self.switch('depositor')
        self.revoke_workspace()
        self.assertEqual(self.client.get('/account').status_code, 302)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 200)
        with self.client.session_transaction() as state:
            self.assertNotIn('other_user_id', state)

    def test_disabled_retained_editor_cannot_be_selected(self):
        self.editor_login()
        self.switch('depositor')
        self.update_user('operator@example.org', active=0)
        self.assertEqual(self.client.get('/account').status_code, 200)
        self.assertEqual(self.switch('operator').status_code, 403)

    def test_disabled_active_editor_preserves_valid_author_only(self):
        self.editor_login()
        self.update_user('operator@example.org', active=0)
        self.assertEqual(self.client.get('/account').status_code, 200)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 403)

    def test_author_activity_does_not_extend_the_retained_editor_idle_timeout(self):
        self.editor_login()
        self.switch('depositor')
        base = now()
        with patch('services.intake.app.now', return_value=base + timedelta(hours=7)):
            self.assertEqual(self.client.get('/account').status_code, 200)
        with patch('services.intake.app.now', return_value=base + timedelta(hours=8, seconds=1)):
            self.assertEqual(self.client.get('/account').status_code, 200)
            self.assertEqual(self.switch('operator').status_code, 403)

    def test_the_active_account_still_expires_after_its_idle_timeout(self):
        self.token()
        with patch('services.intake.app.now', return_value=now() + timedelta(hours=8, seconds=1)):
            self.assertEqual(self.client.get('/account').status_code, 302)

    def test_explicit_logout_clears_both_authenticated_accounts(self):
        self.editor_login()
        self.assertEqual(self.client.post('/logout', data={'csrf_token': self.token()}).status_code, 302)
        with self.client.session_transaction() as state:
            self.assertNotIn('user_id', state)
            self.assertNotIn('other_user_id', state)
        self.assertEqual(self.client.get('/admin/statistics').status_code, 302)

    def test_editor_reauthentication_preserves_author_and_rotates_csrf(self):
        self.editor_login()
        old_token = self.token()
        self.editor_login()
        self.assertNotEqual(self.token(), old_token)
        self.assertEqual(self.switch('depositor').status_code, 302)

    def test_two_editor_accounts_are_not_merged_and_login_audit_uses_actual_actor(self):
        self.editor_login(keep=False)
        self.editor_login(independent=True)
        with self.client.session_transaction() as state:
            self.assertNotIn('other_user_id', state)
        with self.app.app_context():
            actor = get_db().execute("SELECT actor_user_id FROM audit_log WHERE event='login' ORDER BY id DESC LIMIT 1").fetchone()[0]
            expected = get_db().execute("SELECT id FROM users WHERE email='independent@example.org'").fetchone()[0]
            self.assertEqual(actor, expected)

    def test_editor_recovery_still_consumes_code_once_and_can_retain_author(self):
        with self.app.app_context():
            db = get_db()
            db.execute('INSERT INTO recovery_codes(user_id,code_hash) VALUES(?,?)',
                       (self.user_id('operator@example.org'), digest('test-unused-code')))
            db.commit()
        fields = {'csrf_token': self.token('/login'), 'email': 'operator@example.org',
                  'password': 'operator-password-123', 'recovery_code': 'test-unused-code',
                  'keep_other_account': 'on'}
        self.assertEqual(self.client.post('/login/recovery', data=fields).status_code, 302)
        self.assertEqual(self.switch('depositor').status_code, 302)
        fields['csrf_token'] = self.token('/login')
        self.assertEqual(self.client.post('/login/recovery', data=fields).status_code, 403)


if __name__ == '__main__':
    unittest.main()
