"""Authorization, version isolation and delivery boundaries of the private workflow."""
import io
import json
import re
import qrcode
from unittest.mock import patch

import test_intake as fixtures
from services.intake.app import get_db, iso, model_review_template, totp
from services.intake.workflow import authenticator_uri, digest


class WorkflowTests(fixtures.IntakeTests):
    # Reuse fixtures; inherited tests also exercise the stricter workflow.
    def row(self, case_id):
        with self.app.app_context():
            return get_db().execute('SELECT * FROM submissions WHERE id=?', (case_id,)).fetchone()

    def author_session(self, case_id):
        with self.client.session_transaction() as state:
            state.clear()
            state['csrf_token'] = 'author-csrf'
            state['author_case'] = {'id': case_id, 'expires': '2099-01-01T00:00:00+00:00'}
        return 'author-csrf'

    def test_closed_receiver_cannot_persist_an_upload(self):
        self.app.config['INTAKE_OPEN'] = False
        self.assertEqual(self.client.get('/submit').status_code, 503)
        self.assertEqual(self.client.post('/submit', data={'manuscript': (io.BytesIO(b'%PDF-test'), 'x.pdf')}).status_code, 503)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 0)
        self.assertEqual(self.client.get('/login').status_code, 200)

    def test_production_switch_alone_cannot_bypass_launch_approval(self):
        self.app.config.update(TESTING=False, INTAKE_OPEN=True, LAUNCH_APPROVAL_FILE=str(self.temp.name) + '/missing-approval.json')
        self.assertEqual(self.client.get('/submit').status_code, 503)
        self.assertEqual(self.client.post('/submit').status_code, 503)
        self.assertEqual(self.client.get('/login').status_code, 200)

    def test_independent_editor_cannot_browse_unassigned_private_cases(self):
        case_id = self.upload()
        with self.app.app_context():
            get_db().execute('DELETE FROM case_editors WHERE submission_id=?', (case_id,))
            get_db().commit()
        self.login_session('independent@example.org')
        self.assertNotIn(case_id.encode(), self.client.get('/').data)
        self.assertEqual(self.client.get(f'/admin/submission/{case_id}').status_code, 404)
        self.assertEqual(self.client.get(f'/admin/submission/{case_id}/file').status_code, 404)
        token = self.login_session('operator@example.org')
        self.assertEqual(self.client.post(f'/admin/submission/{case_id}/assign-editor', data={'csrf_token': token, 'editor_id': self.user_id('independent@example.org'), 'unconflicted': 'on'}).status_code, 302)
        self.login_session('independent@example.org')
        self.assertEqual(self.client.get(f'/admin/submission/{case_id}').status_code, 200)

    def test_private_email_link_is_single_use_and_get_does_not_consume(self):
        case_id = self.upload()
        with self.app.app_context():
            body = get_db().execute('SELECT body FROM mail_outbox WHERE submission_id=?', (case_id,)).fetchone()[0]
        link = '/case/access/' + body.split('/case/access/')[1].split()[0]
        outsider = self.app.test_client()
        self.assertEqual(outsider.get('/case/' + case_id).status_code, 404)
        self.assertEqual(outsider.get(link).status_code, 200)
        self.assertEqual(outsider.get(link).status_code, 200)
        with outsider.session_transaction() as state:
            csrf = state['csrf_token']
        self.assertEqual(outsider.post(link, data={'csrf_token': csrf}).status_code, 302)
        self.assertEqual(outsider.get('/case/' + case_id).status_code, 200)
        self.assertEqual(self.app.test_client().get(link).status_code, 404)

    def test_plan_requires_author_confirmation_and_locks_after_report(self):
        case_id = self.upload()
        token = self.login_session('operator@example.org')
        providers = json.dumps([{'provider': 'Provider 1', 'model_id': 'frontier-model-1'}])
        data = {'csrf_token': token, 'providers': providers, 'notice': 'Confidential assessment using the named service. No training, defined retention and reviewed transfer safeguards apply to this exact manuscript.'}
        self.assertEqual(self.client.post(f'/admin/submission/{case_id}/plan', data=data).status_code, 302)
        self.assertEqual(self.client.post(f'/admin/submission/{case_id}/model-review', data={'csrf_token': token, 'response_json': '{}'}).status_code, 409)
        csrf = self.author_session(case_id)
        with self.app.app_context():
            plan_id = get_db().execute('SELECT id FROM assessment_plans WHERE submission_id=?', (case_id,)).fetchone()[0]
        self.assertEqual(self.client.post('/case/' + case_id, data={'csrf_token': csrf, 'action': 'authorize', 'authorization': 'on', 'plan_id': str(plan_id)}).status_code, 302)
        with self.app.app_context():
            self.assertTrue(get_db().execute('SELECT authorization_hash FROM assessment_plans WHERE id=?', (plan_id,)).fetchone()[0])
        self.add_model_review(case_id, 1)
        token = self.login_session('operator@example.org')
        data['csrf_token'] = token
        self.assertEqual(self.client.post(f'/admin/submission/{case_id}/plan', data=data).status_code, 409)

    def test_corrected_pdf_preserves_original_and_does_not_inherit_review(self):
        old_id = self.upload()
        self.add_model_review(old_id, 1)
        token = self.login_session('operator@example.org')
        self.client.post(f'/admin/submission/{old_id}/decision', data={'csrf_token': token, 'action': 'request_changes', 'reason': 'Specify a hypothesis.'})
        old_row = self.row(old_id)
        csrf = self.author_session(old_id)
        self.client.get('/submit?revision_of=' + old_id)
        with patch('services.intake.app.scan_file', return_value=('clean', 'test scanner')):
            response = self.client.post('/submit', data={
                'csrf_token': csrf, 'revision_of': old_id, 'display_name': 'Direct Author', 'email': 'direct-author@example.org',
                'title': 'Corrected title', 'authors': 'Author Example', 'abstract': 'Corrected and supported. ' * 10,
                'primary_subject': 'airr-quantum-information', 'adult': 'on', 'terms': 'on', 'privacy': 'on',
                'authority': 'on', 'ai_review_opt_in': 'on', 'manuscript': (io.BytesIO(b'%PDF-1.7\ncorrected bytes'), 'corrected.pdf')}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 302)
        with self.client.session_transaction() as state:
            new_id = state['receipt_submission_id']
        self.assertNotEqual(new_id, old_id)
        self.assertEqual(self.row(old_id)['sha256'], old_row['sha256'])
        self.assertEqual(self.row(old_id)['status'], 'superseded')
        self.assertEqual(self.row(new_id)['parent_id'], old_id)
        self.assertEqual(self.row(new_id)['revision_number'], 2)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM model_reviews WHERE submission_id=?', (new_id,)).fetchone()[0], 0)
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM model_reviews WHERE submission_id=?', (old_id,)).fetchone()[0], 1)

    def test_adjudication_preserves_model_score_and_requires_evidence(self):
        case_id = self.upload()
        self.add_model_review(case_id, 1, recommendation='reject', material=True)
        token = self.login_session('operator@example.org')
        with self.app.app_context():
            review = get_db().execute('SELECT * FROM model_reviews WHERE submission_id=?', (case_id,)).fetchone()
        path = f"/admin/submission/{case_id}/adjudicate/{review['id']}"
        self.assertEqual(self.client.post(path, data={'csrf_token': token, 'basis': 'ignore it'}).status_code, 400)
        self.assertEqual(self.client.post(path, data={'csrf_token': token, 'basis': 'The alleged missing hypothesis is explicitly stated in theorem 2 on page 4. All of this report’s blocking findings refer to that same stated assumption.',
                                                    'evidence': 'Page 4, theorem 2, line 3 contains the strict positivity hypothesis and the appendix supplies its use.', 'all_objections_addressed': 'on'}).status_code, 302)
        self.assertEqual(self.client.post(f'/admin/submission/{case_id}/decision', data={'csrf_token': token, 'action': 'accept', 'reason': 'Every objection has been checked against the exact manuscript.'}).status_code, 302)
        with self.app.app_context():
            saved = get_db().execute('SELECT * FROM model_reviews WHERE id=?', (review['id'],)).fetchone()
        self.assertEqual(saved['response_sha256'], review['response_sha256'])
        self.assertEqual(saved['millennium_score'], 2.0)
        self.assertEqual(saved['recommendation'], 'reject')

    def test_original_editor_cannot_resolve_appeal_and_retention_is_paused(self):
        case_id = self.upload()
        token = self.login_session('operator@example.org')
        self.client.post(f'/admin/submission/{case_id}/decision', data={'csrf_token': token, 'action': 'decline', 'reason': 'Missing evidence'})
        csrf = self.author_session(case_id)
        self.assertEqual(self.client.post('/case/' + case_id, data={'csrf_token': csrf, 'action': 'appeal', 'body': 'The original decision overlooked the independently reproducible evidence in appendix B.'}).status_code, 302)
        self.assertIsNone(self.row(case_id)['delete_after'])
        token = self.login_session('operator@example.org')
        data = {'csrf_token': token, 'outcome': 'reopen', 'resolution': 'Independent inspection confirms that appendix B contains relevant evidence and the submission should be reopened for a corrected presentation.'}
        path = f'/admin/submission/{case_id}/appeal'
        self.assertEqual(self.client.post(path, data=data).status_code, 403)
        data['csrf_token'] = self.login_session('independent@example.org')
        self.assertEqual(self.client.post(path, data=data).status_code, 302)
        self.assertEqual(self.row(case_id)['status'], 'changes_requested')

    def test_release_handoff_requires_publication_permission_and_excludes_contact(self):
        case_id = self.upload()
        self.add_model_review(case_id, 1)
        token = self.login_session('operator@example.org')
        self.client.post(f'/admin/submission/{case_id}/decision', data={'csrf_token': token, 'action': 'accept', 'reason': 'Checks complete'})
        path = f'/admin/submission/{case_id}/release-package'
        self.assertEqual(self.client.get(path).status_code, 409)
        csrf = self.author_session(case_id)
        self.assertEqual(self.client.post('/case/' + case_id, data={'csrf_token': csrf, 'action': 'publication', 'license': 'CC-BY-4.0', 'publication_confirm': 'on'}).status_code, 302)
        self.login_session('operator@example.org')
        result = self.client.get(path)
        self.assertEqual(result.status_code, 200)
        self.assertNotIn(b'direct-author@example.org', result.data)
        self.assertNotIn(b'/case/access/', result.data)
        self.assertEqual(result.json['sha256'], self.row(case_id)['sha256'])

    def test_smtp_ambiguity_is_recorded_without_blind_retry(self):
        case_id = self.upload()
        self.app.config.update(SMTP_HOST='smtp.example.org', SMTP_FROM='submissions@example.org')
        with self.app.app_context(), patch('services.intake.app.send_mail', return_value=False) as sending:
            message_id = get_db().execute('SELECT id FROM mail_outbox WHERE submission_id=?', (case_id,)).fetchone()[0]
            deliver = self.app.extensions['editorial']['deliver']
            self.assertFalse(deliver(message_id))
            self.assertFalse(deliver(message_id))
            self.assertEqual(sending.call_count, 1)
            self.assertEqual(get_db().execute('SELECT state FROM mail_outbox WHERE id=?', (message_id,)).fetchone()[0], 'uncertain')

    def test_editor_setup_requires_totp_does_not_put_secret_in_cookie_or_overwrite_user(self):
        result = self.app.test_cli_runner().invoke(args=['invite-editor', 'new-editor@example.org', '--name', 'New Editor', '--role', 'independent_editor'])
        self.assertEqual(result.exit_code, 0, result.output)
        path = '/editor/setup/' + result.output.strip().split('/editor/setup/')[1]
        page = self.client.get(path)
        self.assertEqual(page.status_code, 200)
        with self.app.app_context():
            secret = get_db().execute('SELECT totp_secret FROM enrollments').fetchone()[0]
        qr_path = path + '/qr.svg'
        self.assertIn(qr_path.encode(), page.data)
        with patch('services.intake.workflow.qrcode.make', wraps=qrcode.make) as encoder:
            qr = self.client.get(qr_path)
        self.assertEqual(qr.status_code, 200)
        self.assertEqual(qr.mimetype, 'image/svg+xml')
        self.assertEqual(qr.headers['Cache-Control'], 'no-store')
        self.assertIn(b'<svg', qr.data)
        self.assertIn(b'<path', qr.data)
        self.assertIn(b'fill="white"', qr.data)
        self.assertEqual(encoder.call_args.args[0], authenticator_uri('new-editor@example.org', secret))
        other = self.app.test_client()
        self.assertEqual(other.get(qr_path).status_code, 404)
        self.assertEqual(other.get(path).status_code, 409)
        self.assertEqual(other.get(qr_path).status_code, 404)
        self.assertEqual(self.client.get(path).status_code, 200)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT totp_secret FROM enrollments').fetchone()[0], secret)
        with self.client.session_transaction() as state:
            token = state['csrf_token']
            self.assertNotIn(secret, str(dict(state)))
        data = {'csrf_token': token, 'password': 'new-password-strong-123', 'confirm_password': 'new-password-strong-123', 'totp': totp(secret)}
        result = self.client.post(path, data=data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Your account is ready', result.data)
        self.assertEqual(self.client.get(path).status_code, 404)
        self.assertEqual(self.client.get(qr_path).status_code, 404)
        again = self.app.test_cli_runner().invoke(args=['invite-editor', 'new-editor@example.org', '--name', 'Bad replacement', '--role', 'operator'])
        self.assertNotEqual(again.exit_code, 0)
        self.assertNotIn('setup/', again.output)
