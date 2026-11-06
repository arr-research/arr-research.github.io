# SPDX-License-Identifier: AGPL-3.0-or-later
import hashlib
import io
import json
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch

from services.intake import app as a
from services.intake.app import get_db, iso
from test_historical_revisions import HistoricalRevisionTests


class ProgrammeDelegationTests(HistoricalRevisionTests):
    def setUp(self):
        super().setUp()
        self.app.config['PROGRAMME_DELEGATIONS_ENABLED'] = True
        with self.app.app_context():
            self.owner = get_db().execute("SELECT id FROM users WHERE email='direct-author@accounts.invalid'").fetchone()[0]
        self.evidence = {
            'owner_user_id': self.owner, 'programme': 'Author research programme',
            'author': 'Operator Author',
            'author_instruction': 'I authorize this programme to prepare and deposit my own manuscripts and linked revisions continuously until I revoke this initial instruction. I confirm rights and current terms/privacy and Working paper CC BY 4.0 / CC0 scope.',
            'source_reference': 'Actual initial author instruction test fixture',
            'recorded_at': iso(), 'terms_version': a.TERMS_VERSION,
            'privacy_version': a.PRIVACY_VERSION, 'rights_confirmed': True,
            'operator_authorship_confirmed': True,
            'paper_ids': [self.binding['paper_id']], 'allow_new_submissions': True,
            'pdf_license': 'CC-BY-4.0', 'metadata_license': 'CC0-1.0',
            'publication_status': 'working_paper'}

    def controller(self, changes=None, success=True):
        evidence = {**self.evidence, **(changes or {})}
        path = Path(self.temp.name)/'initial-authority.json'
        path.write_text(json.dumps(evidence))
        result = self.app.test_cli_runner().invoke(args=['authorize-programme', str(path)])
        if success:
            self.assertEqual(result.exit_code, 0, result.output)
            return json.loads(result.output)
        self.assertNotEqual(result.exit_code, 0, result.output)

    def child(self, controller, kind='revision', **changes):
        data = {'sha256': self.binding['sha256'], 'kind': kind,
                'binding': self.binding if kind == 'revision' else None,
                'agent_name': 'Actual preparing agent', 'agent_version': 'Declared test model'}
        data.update(changes)
        return self.client.post('/api/v1/programme-artifact-grants', json=data,
                                headers={'Authorization': 'Bearer '+controller['controller_token']})

    def test_one_initial_instruction_multiple_exact_pdfs_no_new_human_reply(self):
        controller = self.controller()
        self.assertIsNone(controller['expires_at'])
        issued = self.child(controller)
        self.assertEqual(issued.status_code, 200, issued.data)
        self.assertEqual(issued.headers['Cache-Control'], 'no-store')
        first = issued.get_json()
        self.assertEqual(self.child(controller).get_json(), first)
        received = self.send_revision(first)
        self.assertEqual(received.status_code, 201, received.data)
        self.assertEqual(self.child(controller).get_json()['uploads_remaining'], 0)
        self.assertEqual(self.send_revision(first).status_code, 200)
        self.pdf += b'\nsecond exact candidate'
        self.binding['sha256'] = hashlib.sha256(self.pdf).hexdigest()
        import uuid
        self.binding['version_id'] = 'arr:version:'+str(uuid.uuid4())
        second = self.child(controller).get_json()
        self.assertNotEqual(first['agent_token'], second['agent_token'])
        self.assertEqual(self.send_revision(second, key='second-exact-001').status_code, 201)
        with self.app.app_context():
            db = get_db()
            self.assertEqual(db.execute('SELECT COUNT(*) FROM programme_delegations').fetchone()[0], 1)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM programme_artifact_grants').fetchone()[0], 2)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM model_reviews').fetchone()[0], 0)
            self.assertTrue(all(row[0] is None for row in db.execute('SELECT public_released_at FROM submissions')))
            original = json.loads(db.execute('SELECT evidence_json FROM programme_delegations').fetchone()[0])
            self.assertEqual(original, self.evidence)

    def test_exact_new_deposit_one_use_and_retry_bytes(self):
        controller = self.controller()
        response = self.child(controller, 'submission')
        self.assertEqual(response.status_code, 200, response.data)
        grant = response.get_json()
        self.assertEqual(self.send_revision(grant).status_code, 403)
        first = self.send_revision(grant, path='/api/v1/submissions')
        self.assertEqual(first.status_code, 201, first.data)
        self.assertEqual(self.send_revision(grant, path='/api/v1/submissions').status_code, 200)
        self.assertEqual(self.send_revision(grant, path='/api/v1/submissions', pdf=b'%PDF-different').status_code, 400)
        self.assertEqual(self.send_revision(grant, path='/api/v1/submissions', key='exhausted-child-001').status_code, 403)

    def test_private_programme_intake_needs_no_public_licence(self):
        controller = self.controller({'pdf_license':None,'metadata_license':None,
                                      'publication_status':'private',
                                      'author_instruction':'I authorize continuous preparation and private deposit of my own exact PDFs. I give no public licence, model transfer consent or publication permission.'})
        issued = self.child(controller,'submission')
        self.assertEqual(issued.status_code,200,issued.data)
        received = self.send_revision(issued.get_json(),path='/api/v1/submissions')
        self.assertEqual(received.status_code,201,received.data)
        self.assertFalse(received.get_json()['published'])
        with self.app.app_context():
            evidence=json.loads(get_db().execute('SELECT evidence_json FROM programme_delegations').fetchone()[0])
            self.assertIsNone(evidence['pdf_license'])
            self.assertIsNone(evidence['metadata_license'])
            self.assertEqual(evidence['publication_status'],'private')
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0],0)

    def test_private_and_public_licence_scopes_cannot_be_mixed(self):
        self.controller({'publication_status':'private'},success=False)
        self.controller({'pdf_license':None,'metadata_license':None},success=False)

    def test_controller_is_not_an_upload_or_editorial_credential(self):
        controller = self.controller()
        fake_child = {'agent_token': controller['controller_token']}
        self.assertEqual(self.send_revision(fake_child).status_code, 401)
        self.assertEqual(self.send_revision(fake_child, path='/api/v1/submissions').status_code, 401)
        headers = {'Authorization': 'Bearer '+controller['controller_token']}
        self.assertNotEqual(self.app.test_client().get('/admin/statistics', headers=headers).status_code, 200)
        ordinary = self.issue()
        self.assertEqual(self.child({'controller_token': ordinary['agent_token']}).status_code, 401)

    def test_disabled_unknown_and_scope_mismatch(self):
        self.app.config['PROGRAMME_DELEGATIONS_ENABLED'] = False
        self.controller(success=False)
        self.app.config['PROGRAMME_DELEGATIONS_ENABLED'] = True
        controller = self.controller({'paper_ids': [], 'allow_new_submissions': False})
        self.assertEqual(self.child(controller).status_code, 400)
        self.assertEqual(self.child(controller, 'submission').status_code, 400)
        self.assertEqual(self.child({'controller_token': 'x'*43}).status_code, 401)
        self.controller({'rights_confirmed': False}, success=False)
        self.controller({'author': 'Different Author'}, success=False)
        self.controller({'terms_version': 'old'}, success=False)
        self.controller({'publication_status': 'accepted'}, success=False)
        self.controller({'recorded_at': iso(a.now()-timedelta(days=8))}, success=False)

    def test_revocation_stops_controller_child_and_receipt(self):
        controller = self.controller()
        grant = self.child(controller).get_json()
        result = self.send_revision(grant)
        case = result.get_json()['registration_number']
        revoked = self.app.test_cli_runner().invoke(args=['revoke-programme', controller['programme_id']])
        self.assertEqual(revoked.exit_code, 0, revoked.output)
        self.assertEqual(self.child(controller).status_code, 403)
        self.assertEqual(self.send_revision(grant).status_code, 403)
        self.assertEqual(self.client.get('/api/v1/submissions/'+case, headers={'Authorization': 'Bearer '+grant['agent_token']}).status_code, 403)

    def test_changed_contract_account_operator_and_catalogue_stop_children(self):
        controller = self.controller()
        grant = self.child(controller).get_json()
        self.catalog.write_text(self.catalog.read_text()+'\n')
        self.assertEqual(self.send_revision(grant).status_code, 409)
        with patch.object(a, 'TERMS_VERSION', 'new contract'):
            self.assertEqual(self.child(controller).status_code, 403)
            self.assertEqual(self.send_revision(grant).status_code, 403)
        with self.app.app_context():
            get_db().execute('UPDATE users SET active=0 WHERE id=?', (self.owner,))
            get_db().commit()
        self.assertEqual(self.child(controller).status_code, 403)

    def test_initial_authority_survives_seven_days_but_child_expiry_not_renewed(self):
        controller = self.controller()
        with patch.object(a, 'now', return_value=a.now()+timedelta(days=8)):
            response = self.child(controller)
            self.assertEqual(response.status_code, 200, response.data)
            grant = response.get_json()
            self.assertEqual(self.child(controller).get_json(), grant)
        with self.app.app_context():
            get_db().execute("UPDATE agent_grants SET expires_at='2000-01-01T00:00:00+00:00' WHERE id=?", (grant['request_id'],))
            get_db().commit()
        self.assertEqual(self.child(controller).status_code, 409)
        renewed = self.child(controller, renew_expired_unused=True)
        self.assertEqual(renewed.status_code, 200, renewed.data)
        self.assertEqual(renewed.get_json()['request_id'], grant['request_id'])

    def test_changed_agent_identity_cannot_duplicate_same_pdf(self):
        controller = self.controller()
        self.assertEqual(self.child(controller).status_code, 200)
        self.assertEqual(self.child(controller, agent_version='Changed identity').status_code, 409)

    def test_owner_can_revoke_from_normal_workspace_and_other_owner_cannot(self):
        controller = self.controller()
        grant = self.child(controller).get_json()
        page = self.client.get('/account')
        self.assertIn(controller['programme_id'].encode(), page.data)
        self.assertEqual(self.client.post('/account/programmes/'+controller['programme_id']+'/revoke', data={}).status_code, 400)
        response = self.client.post('/account/programmes/'+controller['programme_id']+'/revoke', data={'csrf_token': 'csrf-for-tests'})
        self.assertEqual(response.status_code, 302, response.data)
        self.assertEqual(self.child(controller).status_code, 403)
        self.assertEqual(self.send_revision(grant).status_code, 403)

    def test_existing_account_quota_is_still_enforced(self):
        controller = self.controller()
        grant = self.child(controller).get_json()
        original = a.enforce_rate
        def deny_account(action, *args, **kwargs):
            if action == 'submit-account':
                from flask import abort
                abort(429, 'Fixture account quota exhausted')
            return original(action, *args, **kwargs)
        with patch.object(a, 'enforce_rate', side_effect=deny_account):
            self.assertEqual(self.send_revision(grant).status_code, 429)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 0)

    def test_wrong_exact_bytes_and_other_author_cannot_use_child(self):
        grant = self.child(self.controller(), 'submission').get_json()
        self.assertEqual(self.send_revision(grant, path='/api/v1/submissions', pdf=b'%PDF-not-authorized').status_code, 400)
        metadata = {'title': 'A different author manuscript', 'authors': 'Other Author', 'abstract': 'A'*120,
                    'primary_subject': 'airr-quantum-information', 'secondary_subjects': [], 'specific_topic': '',
                    'sha256': self.binding['sha256'], 'ai_disclosure': 'Actual preparing agent disclosure.',
                    'operator_conflict': True, 'rights_confirmed': True}
        with patch('services.intake.app.scan_file', return_value=('clean', 'test scanner')):
            response = self.client.post('/api/v1/submissions', headers={'Authorization': 'Bearer '+grant['agent_token'], 'Idempotency-Key': 'wrong-author-001'}, data={'metadata': json.dumps(metadata), 'manuscript': (io.BytesIO(self.pdf), 'paper.pdf')})
        response.request.environ['wsgi.input'].close()
        self.assertEqual(response.status_code, 400)

    def permit_working(self, controller, case, sha=None):
        return self.client.post('/api/v1/programme-working-paper-permissions',
                                headers={'Authorization': 'Bearer '+controller['controller_token']},
                                json={'submission_id': case, 'sha256': sha or self.binding['sha256']})

    def test_standing_working_permission_is_exact_separate_and_does_not_publish(self):
        controller = self.controller()
        grant = self.child(controller).get_json()
        case = self.send_revision(grant).get_json()['registration_number']
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 0)
        response = self.permit_working(controller, case)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertFalse(response.get_json()['published'])
        self.assertEqual(response.get_json()['public_status'], 'working_paper')
        self.assertEqual(self.permit_working(controller, case).get_json(), response.get_json())
        with self.app.app_context():
            db = get_db()
            self.assertEqual(db.execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 1)
            row = db.execute('SELECT * FROM submissions WHERE id=?', (case,)).fetchone()
            self.assertEqual(row['status'], 'eligible')
            self.assertIsNone(row['public_released_at'])
            self.assertIsNone(row['decision_by'])
            audit = json.loads(db.execute("SELECT detail_json FROM audit_log WHERE event='publication_permission_recorded' ORDER BY id DESC").fetchone()[0])
            self.assertEqual(audit['initial_recorded_at'], self.evidence['recorded_at'])
            self.assertEqual(audit['method'], 'standing_programme_instruction')

    def test_public_permission_rejects_other_programme_wrong_hash_and_blocked_case(self):
        controller = self.controller()
        other = self.controller()
        case = self.send_revision(self.child(controller).get_json()).get_json()['registration_number']
        self.assertEqual(self.permit_working(other, case).status_code, 404)
        self.assertEqual(self.permit_working(controller, case, '0'*64).status_code, 409)
        for status in ('declined', 'withdrawn', 'removed', 'legal_hold', 'accepted_for_publication'):
            with self.app.app_context():
                get_db().execute('UPDATE submissions SET status=? WHERE id=?', (status, case))
                get_db().commit()
            self.assertEqual(self.permit_working(controller, case).status_code, 409)
        with self.app.app_context():
            db = get_db()
            db.execute("UPDATE submissions SET status='eligible',scan_status='error' WHERE id=?", (case,))
            db.commit()
        self.assertEqual(self.permit_working(controller, case).status_code, 409)
        with self.app.app_context():
            db = get_db()
            db.execute("UPDATE submissions SET scan_status='clean' WHERE id=?", (case,))
            db.commit()
            row = db.execute('SELECT * FROM submissions WHERE id=?', (case,)).fetchone()
            (Path(self.app.config['QUARANTINE'])/row['stored_name']).write_bytes(b'changed')
        self.assertEqual(self.permit_working(controller, case).status_code, 409)

    def test_public_permission_does_not_overwrite_existing_license_and_respects_revocation(self):
        controller = self.controller()
        case = self.send_revision(self.child(controller).get_json()).get_json()['registration_number']
        with self.app.app_context():
            get_db().execute('INSERT INTO publication_permissions VALUES(?,?,?,?)', (case, self.binding['sha256'], 'CC-BY-SA-4.0', iso()))
            get_db().commit()
        self.assertEqual(self.permit_working(controller, case).status_code, 409)
        self.app.test_cli_runner().invoke(args=['revoke-programme', controller['programme_id']])
        self.assertEqual(self.permit_working(controller, case).status_code, 403)
