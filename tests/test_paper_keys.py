"""Real Flask/SQLite boundary tests for anonymous paper capabilities."""
import io
import json
import re
import unittest
from unittest.mock import patch
from pathlib import Path
import test_intake as fixtures
from services.intake.app import get_db, init_db


class PaperKeyTests(unittest.TestCase):
    def setUp(self):
        fixtures.IntakeTests.setUp(self)
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def token(self, client):
        client.get('/manage')
        with client.session_transaction() as state:
            return state['csrf_token']

    def create(self, client=None):
        client = client or self.client
        r = client.post('/paper/new', data={'csrf_token': self.token(client)})
        self.assertEqual(r.status_code, 200, r.data)
        key = re.search(rb'value="(AIRR-[A-Za-z0-9_-]{43})"', r.data).group(1).decode()
        draft = re.search(rb'/paper/draft/([a-f0-9]+)', r.data).group(1).decode()
        return key, draft

    def send(self, draft, client=None, **fields):
        client = client or self.client
        data = dict(csrf_token=self.token(client), title='A test paper', abstract='A' * 100,
                    primary_subject='airr-quantum-information', agreement='on', key_saved='on', action='send',
                    manuscript=(io.BytesIO(b'%PDF-1.7\nprivate manuscript'), 'paper.pdf'))
        data.update(fields)
        with patch('services.intake.app.scan_file', return_value=('clean', 'Clean')):
            return client.post('/paper/draft/' + draft, data=data)

    def test_no_account_secret_hash_only_and_repeat_submission(self):
        key, draft = self.create()
        r = self.send(draft)
        self.assertEqual(r.status_code, 302, r.data)
        case = r.location
        self.assertEqual(self.client.get(case).status_code, 200)
        self.assertEqual(self.send(draft).location, case)
        with self.app.app_context():
            db = get_db()
            self.assertEqual(db.execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 1)
            self.assertNotIn(key, str(tuple(db.execute('SELECT * FROM paper_keys').fetchone())))
            self.assertEqual(db.execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0], 0)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM private_accounts').fetchone()[0], 1)
            init_db()  # idempotent migration, preserves key and case

    def test_inline_start_creates_only_a_draft_and_preserves_selected_subject(self):
        response = self.client.get('/submit?subject=airr-quantum-information')
        self.assertIn('subject=airr-quantum-information', response.location)
        page = self.client.get(response.location)
        self.assertIn(b'Choose your PDF', page.data)
        self.assertIn(b'value="airr-quantum-information" selected', page.data)
        response = self.client.post('/paper/new', headers={'X-Paper-Start':'1'},
                                    data={'csrf_token':self.token(self.client), 'subject':'airr-quantum-information'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Cache-Control'], 'no-store')
        key, draft_url = response.json['key'], response.json['draft_url']
        self.assertRegex(key, r'^AIRR-[A-Za-z0-9_-]{43}$')
        with self.client.session_transaction() as state:
            self.assertNotIn(key, str(dict(state)))
        with self.app.app_context():
            db = get_db()
            self.assertEqual(db.execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 0)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 0)
            draft = db.execute('SELECT * FROM paper_drafts').fetchone()
            self.assertEqual(json.loads(draft['data_json'])['primary_subject'], 'airr-quantum-information')
        self.assertEqual(list(Path(self.app.config['QUARANTINE']).iterdir()), [])
        self.assertEqual(self.app.test_client().get(draft_url).status_code, 401)
        sent = self.send(draft_url.rsplit('/',1)[-1])
        self.assertEqual(sent.status_code, 302)
        returning = self.app.test_client()
        returning.post('/manage', data={'csrf_token':self.token(returning), 'key':key})
        self.assertEqual(returning.get(sent.location).status_code, 200)

    def test_inline_start_does_not_bypass_csrf_or_closed_intake(self):
        self.assertEqual(self.client.post('/paper/new', headers={'X-Paper-Start':'1'}).status_code, 400)
        token = self.token(self.client)
        self.app.config['INTAKE_OPEN'] = False
        self.assertEqual(self.client.post('/paper/new', headers={'X-Paper-Start':'1'}, data={'csrf_token':token}).status_code, 503)

    def test_cross_paper_isolation_login_rotation_and_expiration(self):
        key, draft = self.create()
        case = self.send(draft).location
        other = self.app.test_client()
        self.create(other)
        self.assertEqual(other.get(case).status_code, 404)
        self.assertEqual(other.get('/paper/draft/' + draft).status_code, 404)
        self.assertEqual(other.post('/paper/remove/' + case.split('/')[-1], data={'csrf_token': self.token(other), 'confirm':'on'}).status_code, 404)
        stranger = self.app.test_client()
        self.assertEqual(stranger.post('/manage', data={'csrf_token': self.token(stranger), 'key': key}).status_code, 302)
        self.assertEqual(stranger.get(case).status_code, 200)
        rotated = self.client.post('/paper/rotate', data={'csrf_token': self.token(self.client), 'confirm':'on'})
        self.assertEqual(rotated.status_code, 200)
        replacement = re.search(rb'value="(AIRR-[A-Za-z0-9_-]{43})"', rotated.data).group(1).decode()
        self.assertEqual(stranger.get(case).status_code, 200)  # Not invalidated before the replacement is saved.
        self.assertEqual(self.client.post('/paper/activate-key', data={'csrf_token':self.token(self.client), 'new_key':replacement,'saved':'on'}).status_code,302)
        self.assertEqual(stranger.get(case).status_code, 404)
        self.assertEqual(stranger.post('/manage', data={'csrf_token': self.token(stranger), 'key': key}).status_code, 401)
        self.assertEqual(self.client.get(case).status_code, 200)
        self.assertEqual(self.client.get('/receipt').status_code, 200)
        with self.client.session_transaction() as state:
            state['paper_access'] = dict(state['paper_access'], expires=0)
        self.assertEqual(self.client.get(case).status_code, 404)
        self.assertEqual(self.client.get('/receipt').status_code, 404)
        self.assertEqual(self.client.get('/receipt/download').status_code, 404)

    def test_revision_is_prefilled_keeps_predecessor_and_requires_new_permissions(self):
        _, draft = self.create()
        case = self.send(draft, authors='A pseudonym').location
        r = self.client.post('/paper/revise/' + case.split('/')[-1], data={'csrf_token':self.token(self.client)})
        self.assertEqual(r.status_code, 302, r.data)
        page = self.client.get(r.location)
        self.assertIn(b'A pseudonym', page.data)
        result = self.send(r.location.split('/')[-1], change_summary='Corrects the proof.')
        self.assertEqual(result.status_code, 302, result.data)
        with self.app.app_context():
            rows = get_db().execute('SELECT * FROM submissions ORDER BY revision_number').fetchall()
            self.assertEqual(rows[1]['parent_id'], rows[0]['id'])
            self.assertEqual(rows[1]['revision_number'], 2)
            self.assertEqual(rows[0]['status'], 'eligible')
            self.assertIsNone(rows[0]['delete_after'])
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0], 0)

    def test_csrf_closed_intake_invalid_pdf_and_draft_persistence(self):
        self.assertEqual(self.client.post('/paper/new').status_code, 400)
        _, draft = self.create()
        r = self.client.post('/paper/draft/' + draft, data={'csrf_token': self.token(self.client), 'action':'save','title':'Saved title'})
        self.assertEqual(r.status_code, 302)
        self.assertIn(b'Saved title', self.client.get('/paper/draft/' + draft).data)
        r = self.send(draft, manuscript=(io.BytesIO(b'not a PDF'), 'bad.pdf'))
        self.assertEqual(r.status_code, 400)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0], 0)
        self.app.config['INTAKE_OPEN'] = False
        self.assertEqual(self.client.get('/paper/new').status_code, 503)
        self.assertEqual(self.send(draft).status_code, 503)

    def test_withdrawal_and_legal_hold(self):
        _, draft = self.create()
        case = self.send(draft).location.split('/')[-1]
        r = self.client.post('/paper/remove/' + case, data={'csrf_token':self.token(self.client), 'confirm':'on'})
        self.assertEqual(r.status_code, 302)
        with self.app.app_context():
            db=get_db()
            row=db.execute('SELECT * FROM submissions WHERE id=?',(case,)).fetchone()
            self.assertEqual(row['status'], 'withdrawn')
            self.assertIsNotNone(row['delete_after'])
            db.execute("UPDATE submissions SET status='legal_hold' WHERE id=?",(case,)); db.commit()
        self.assertEqual(self.client.post('/paper/remove/' + case, data={'csrf_token':self.token(self.client), 'confirm':'on'}).status_code, 409)

    def test_metadata_correction_reuses_pdf_and_keeps_original_bytes(self):
        _, draft = self.create()
        first = self.send(draft).location.split('/')[-1]
        r = self.client.post('/paper/revise/' + first, data={'csrf_token':self.token(self.client)})
        result = self.send(r.location.split('/')[-1], manuscript=None, reuse_pdf='on', title='Corrected title', change_summary='Corrects title.')
        self.assertEqual(result.status_code, 302, result.data)
        with self.app.app_context():
            rows = get_db().execute('SELECT * FROM submissions ORDER BY revision_number').fetchall()
            self.assertEqual(rows[0]['sha256'], rows[1]['sha256'])
            self.assertNotEqual(rows[0]['stored_name'], rows[1]['stored_name'])
            self.assertEqual(rows[0]['title'], 'A test paper')
            self.assertEqual(rows[1]['title'], 'Corrected title')

    def test_public_withdrawal_is_a_request_not_silent_deletion(self):
        _, draft = self.create()
        case = self.send(draft).location.split('/')[-1]
        with self.app.app_context():
            db = get_db()
            db.execute('UPDATE submissions SET public_release_url=? WHERE id=?', ('https://airr.science/papers/example/',case))
            db.commit()
        self.client.post('/paper/remove/' + case, data={'csrf_token':self.token(self.client),'confirm':'on'})
        with self.app.app_context():
            db = get_db()
            row = db.execute('SELECT * FROM submissions WHERE id=?',(case,)).fetchone()
            self.assertEqual(row['status'], 'eligible')
            self.assertIsNone(row['delete_after'])
            self.assertEqual(db.execute("SELECT COUNT(*) FROM correspondence WHERE kind='withdrawal_requested'").fetchone()[0],1)

    def test_extraction_requires_scan_and_deletes_temporary_files(self):
        self.create()
        def payload():
            return {'csrf_token':self.token(self.client), 'manuscript':(io.BytesIO(b'%PDF-1.7\nbytes'), 'paper.pdf')}
        with patch('services.intake.app.scan_file', return_value=('infected','Infected')), patch('services.intake.paper_keys.subprocess.run') as process:
            self.assertEqual(self.client.post('/paper/extract',data=payload()).status_code,422)
            process.assert_not_called()
        def extract(command, **kwargs):
            Path(command[-1]).write_text('A proposed title\nAbstract\n' + 'Relevant research. '*12 + '\n1 Introduction\nBody',encoding='utf-8')
            from types import SimpleNamespace
            return SimpleNamespace(returncode=0)
        with patch('services.intake.app.scan_file', return_value=('clean','Clean')), patch('services.intake.paper_keys.subprocess.run',side_effect=extract):
            response = self.client.post('/paper/extract',data=payload())
            self.assertEqual(response.status_code,200,response.data)
            self.assertEqual(response.json['title'],'A proposed title')
            self.assertNotIn('Introduction',response.json['abstract'])
        self.assertEqual(list(Path(self.app.config['QUARANTINE']).iterdir()), [])

    def test_key_does_not_grant_editor_or_legacy_link_access(self):
        _, draft = self.create()
        case = self.send(draft).location.split('/')[-1]
        self.assertNotEqual(self.client.get('/admin/submission/' + case).status_code,200)
        outsider = self.app.test_client()
        from services.intake.app import iso, now
        from datetime import timedelta
        with outsider.session_transaction() as state:
            state['author_case']={'id':case,'expires':iso(now()+timedelta(hours=1))}
        self.assertEqual(outsider.get('/case/' + case).status_code,404)

    def test_draft_deletion_and_expiry_do_not_delete_submitted_versions(self):
        _, draft = self.create()
        self.assertEqual(self.client.post('/paper/delete-draft/' + draft, data={'csrf_token':self.token(self.client),'confirm':'on'}).status_code,302)
        self.assertEqual(self.client.get('/paper/draft/' + draft).status_code,404)
        _, draft = self.create()
        case = self.send(draft).location
        with self.app.app_context():
            db=get_db();db.execute("UPDATE paper_drafts SET created_at='2000-01-01T00:00:00+00:00'");db.commit()
        self.assertEqual(self.app.test_cli_runner().invoke(args=['paper-draft-sweep']).exit_code,0)
        self.assertEqual(self.client.get(case).status_code,200)
