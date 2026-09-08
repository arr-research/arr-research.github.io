import json
import os
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch

os.environ.setdefault('ARR_SESSION_SECRET', 'test-import-secret-' * 4)
from services.intake.app import create_app, get_db, init_db, iso, now
from services.intake.pageviews import validate_manifest


class PageviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        manifest = root / 'pages.json'
        manifest.write_text(json.dumps({'/': 'AIRR', '/papers/': 'Papers'}))
        self.app = create_app(dict(TESTING=True, SECRET_KEY='test-pageviews-secret',
            DATABASE=str(root/'db.sqlite3'), QUARANTINE=str(root/'quarantine'),
            SESSION_COOKIE_SECURE=False, ANALYTICS_ENABLED=True,
            ANALYTICS_MANIFEST=str(manifest)))
        with self.app.app_context():
            init_db()
            for role, secret in [('operator', 'TEST'), ('independent_editor', 'TEST'), ('depositor', None)]:
                get_db().execute('INSERT INTO users(email,display_name,password_hash,role,totp_secret,created_at) VALUES(?,?,?,?,?,?)',
                                 (role+'@example.test', role, 'not-used-in-test', role, secret, iso()))
            get_db().commit()
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def post(self, payload=None, origin='https://airr.science', **kwargs):
        return self.client.post('/api/v1/pageviews', json=payload if payload is not None else
            {'path':'/', 'consent':'aggregate-v1'}, headers={'Origin':origin}, **kwargs)

    def rows(self):
        with self.app.app_context():
            return [tuple(row) for row in get_db().execute('SELECT * FROM public_pageviews')]

    def login(self, role):
        with self.app.app_context():
            uid = get_db().execute('SELECT id FROM users WHERE role=?', (role,)).fetchone()[0]
        with self.client.session_transaction() as session:
            session['user_id'] = uid

    def test_aggregates_without_event_or_identity_fields(self):
        for _ in range(2):
            response = self.post()
            self.assertEqual(response.status_code, 204)
            self.assertEqual(response.headers['Access-Control-Allow-Origin'], 'https://airr.science')
            self.assertNotIn('Access-Control-Allow-Credentials', response.headers)
            self.assertNotIn('Set-Cookie', response.headers)
        self.assertEqual(self.rows(), [(now().date().isoformat(), '/', 2)])
        with self.app.app_context():
            self.assertEqual([r[1] for r in get_db().execute('PRAGMA table_info(public_pageviews)')], ['day','path','views'])
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM rate_events').fetchone()[0], 0)
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM mail_outbox').fetchone()[0], 0)

    def test_default_disabled_and_no_preflight_counts(self):
        self.assertEqual(self.client.options('/api/v1/pageviews', headers={'Origin':'https://www.airr.science'}).status_code,204)
        self.assertEqual(self.rows(), [])
        self.app.config['ANALYTICS_ENABLED'] = False
        self.assertEqual(self.post().status_code,503)
        self.assertEqual(self.rows(), [])

    def test_rejects_origins_private_paths_queries_and_extra_data(self):
        for origin in ['', 'null', 'https://evil.test', 'https://submit.airr.science']:
            self.assertEqual(self.post(origin=origin).status_code,403)
        bad = [None, '/', {'path':'/'}, {'path':'/','consent':'no'},
               {'path':'/','consent':'aggregate-v1','email':'private@example.test'}]
        for path in ['/admin/statistics', '/case/SECRET/', '/unknown/', '/?q=private@example.test', '/papers/#private']:
            bad.append({'path':path, 'consent':'aggregate-v1'})
        for payload in bad:
            response = self.client.post('/api/v1/pageviews', data=json.dumps(payload),
                content_type='application/json', headers={'Origin':'https://airr.science'})
            self.assertEqual(response.status_code,400, str(payload))
        self.assertEqual(self.rows(), [])

    def test_size_mime_and_burst_limits(self):
        headers={'Origin':'https://airr.science'}
        self.assertEqual(self.client.post('/api/v1/pageviews', data='x'*513, headers=headers).status_code,413)
        self.assertEqual(self.client.post('/api/v1/pageviews', data='x', headers=headers).status_code,415)
        with patch('services.intake.pageviews.time.monotonic', return_value=60):
            for _ in range(120):
                self.assertEqual(self.post().status_code,204)
            self.assertEqual(self.post().status_code,429)
        self.assertEqual(self.rows()[0][2],120)

    def test_operator_only_dashboard_and_ranges(self):
        self.assertEqual(self.client.get('/admin/statistics').status_code,302)
        for role in ['depositor','independent_editor']:
            self.login(role)
            self.assertEqual(self.client.get('/admin/statistics').status_code,403)
        self.login('operator')
        self.post()
        for days in [7,30,90,365]:
            response = self.client.get('/admin/statistics?days='+str(days))
            self.assertEqual(response.status_code,200)
            self.assertIn(b'not a unique person',response.data)
            self.assertIn(b'no-store',response.headers['Cache-Control'].encode())
        for days in ['0','-1','100000','hello']:
            self.assertEqual(self.client.get('/admin/statistics?days='+days).status_code,400)
        with self.app.app_context():
            get_db().execute("UPDATE users SET totp_secret=NULL WHERE role='operator'")
            get_db().commit()
        self.assertEqual(self.client.get('/admin/statistics').status_code,403)

    def test_retention_sweep_without_new_traffic(self):
        today=now().date()
        with self.app.app_context():
            for age in [0,399,400,700]:
                get_db().execute('INSERT INTO public_pageviews VALUES(?,?,?)',((today-timedelta(days=age)).isoformat(),'/',1))
            get_db().commit()
        result=self.app.test_cli_runner().invoke(args=['retention-sweep'])
        self.assertEqual(result.exit_code,0, result.output)
        self.assertEqual(len(self.rows()),2)

    def test_refresh_keeps_good_catalogue_on_network_error(self):
        self.app.config['TESTING']=False
        with patch('services.intake.pageviews.urllib.request.urlopen', side_effect=OSError('offline')) as request:
            self.assertEqual(self.post().status_code,204)
            self.assertEqual(self.post().status_code,204)
            self.assertEqual(request.call_count,1)

    def test_manifest_rejects_private_or_unbounded_data(self):
        for value in [{}, {'/api/token/':'private'}, {'/papers/?q=x/':'query'}, {'/':'x'*401}, {'//':'x'}]:
            with self.assertRaises(ValueError):
                validate_manifest(value)

