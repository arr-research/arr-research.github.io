import csv
import io
import json
import unittest
from datetime import datetime, timedelta, UTC
from unittest.mock import patch, MagicMock

import test_intake_pageviews as fixtures
from services.intake.app import get_db, iso, totp
from services.intake.admin_statistics import install_download_reader, validate_downloads
from services.intake.workflow import digest
from werkzeug.security import generate_password_hash

STAMP = datetime(2026, 10, 11, 10, 0, tzinfo=UTC)
PAPER = 'ARR-2026-2GSA1YTZR39XN9WJ'
SNAPSHOT = {'schema_version':'1.0','generated_at':'2026-10-11T05:48:00+00:00',
            'downloads':{'provider':'GitHub Releases'},
            'papers':{PAPER:{'pdf_downloads':137}}}


class AdminStatisticsTests(unittest.TestCase):
    setUp = fixtures.PageviewTests.setUp
    tearDown = fixtures.PageviewTests.tearDown
    login = fixtures.PageviewTests.login

    def seed(self):
        with self.app.app_context():
            db = get_db()
            for day,path,count in [('2026-10-01','/',7),('2026-10-02','/',3),
                                   ('2026-10-02',fixtures.PDF,2),('2026-10-03','/',99),
                                   ('2026-09-29','/',4),('2026-09-30','/',2)]:
                db.execute('INSERT INTO public_pageviews VALUES(?,?,?)',(day,path,count))
            db.execute("INSERT INTO private_accounts VALUES(3,'reader-one','human','never-show-recovery',1,'2026-10-02T12:00:00+00:00','2026-10-10T08:00:00+00:00','T','P')")
            db.execute("UPDATE users SET password_hash='never-show-password',totp_secret='never-show-totp' WHERE role='operator'")
            db.commit()
        self.login('operator')

    def test_protected_routes_and_export_do_not_leak(self):
        for route in ['/admin','/admin/statistics','/admin/statistics.csv']:
            self.client = self.app.test_client()
            self.assertEqual(self.client.get(route).status_code,302)
            for role in ['depositor','independent_editor']:
                self.login(role)
                self.assertEqual(self.client.get(route).status_code,403)
        self.login('operator')
        for route in ['/admin','/admin/statistics.csv']:
            res=self.client.get(route)
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.headers['Cache-Control'],'no-store')
            self.assertIn('noindex',res.headers['X-Robots-Tag'])
        with self.app.app_context():
            get_db().execute("UPDATE users SET totp_secret=NULL WHERE role='operator'")
            get_db().commit()
        self.assertEqual(self.client.get('/admin/statistics.csv').status_code,403)

    def test_normal_and_recovery_login_landings_preserve_authentication(self):
        with self.app.app_context():
            db=get_db()
            db.execute("UPDATE users SET password_hash=?,totp_secret=? WHERE role IN ('operator','independent_editor')",
                       (generate_password_hash('test-dashboard-password'),'JBSWY3DPEHPK3PXP'))
            db.execute('INSERT INTO recovery_codes(user_id,code_hash) VALUES(1,?)',(digest('test-one-use-code'),))
            db.commit()
        for role,target in [('operator','/admin/statistics'),('independent_editor','/')]:
            self.client=self.app.test_client()
            self.client.get('/login')
            with self.client.session_transaction() as session: csrf=session['csrf_token']
            data={'csrf_token':csrf,'email':role+'@example.test','password':'test-dashboard-password','totp':'invalid'}
            self.assertEqual(self.client.post('/login',data=data).status_code,200)
            data['totp']=totp('JBSWY3DPEHPK3PXP')
            response=self.client.post('/login',data=data)
            self.assertEqual((response.status_code,response.headers['Location']),(302,target))
        self.client=self.app.test_client()
        self.client.get('/login')
        with self.client.session_transaction() as session: csrf=session['csrf_token']
        data={'csrf_token':csrf,'email':'operator@example.test','password':'test-dashboard-password','recovery_code':'test-one-use-code'}
        response=self.client.post('/login/recovery',data=data)
        self.assertEqual((response.status_code,response.headers['Location']),(302,'/admin/statistics'))
        self.client.get('/admin')
        with self.client.session_transaction() as session: data['csrf_token']=session['csrf_token']
        self.assertEqual(self.client.post('/login/recovery',data=data).status_code,403)

    @patch('services.intake.app.now', return_value=STAMP)
    def test_custom_period_exact_csv_and_comparison(self, clock):
        self.seed()
        with patch('services.intake.pageviews.render_template',return_value='') as render:
            self.assertEqual(self.client.get('/admin?start=2026-10-01&end=2026-10-02').status_code,200)
        c=render.call_args.kwargs
        self.assertEqual(c['total'],10)
        self.assertEqual(c['pdf_total'],2)
        self.assertEqual(c['totals']['accounts'],1)
        self.assertEqual(c['charts'][0]['previous'],6)
        self.assertEqual(c['charts'][0]['change'],4)
        self.assertFalse(c['includes_today'])
        res=self.client.get('/admin/statistics.csv?start=2026-10-01&end=2026-10-02')
        rows=list(csv.DictReader(io.StringIO(res.get_data(as_text=True))))
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['consenting_page_views'],'7')
        self.assertEqual(rows[1]['consenting_page_views'],'3')
        self.assertEqual(rows[1]['consenting_pdf_opens'],'2')
        self.assertEqual(rows[1]['registered_workspaces'],'1')
        self.assertNotIn('reader-one',res.get_data(as_text=True))

    @patch('services.intake.app.now', return_value=STAMP)
    def test_month_zero_days_and_incomplete_today(self, clock):
        self.seed()
        with patch('services.intake.pageviews.render_template',return_value='') as render:
            self.assertEqual(self.client.get('/admin?period=month').status_code,200)
        c=render.call_args.kwargs
        self.assertEqual(c['start'],'2026-10-01')
        self.assertEqual(len(c['series']),11)
        self.assertEqual(c['series'][-1]['views'],0)
        self.assertTrue(c['includes_today'])
        self.assertFalse(c['comparison_available'])
        res=self.client.get('/admin?period=month')
        self.assertIn('Hoy está incompleto',res.get_data(as_text=True))

    @patch('services.intake.app.now', return_value=STAMP)
    def test_invalid_bounds_and_pagination(self, clock):
        self.login('operator')
        queries=['start=oops&end=2026-10-01','start=2026-10-01',
                 'start=2026-10-03&end=2026-10-01','start=2026-10-01&end=2026-10-12',
                 'start=2024-01-01&end=2026-10-01']
        for query in queries:
            for route in ['/admin','/admin/statistics.csv']:
                self.assertEqual(self.client.get(route+'?'+query).status_code,400)
        for page in ['0','-1','no','2','99999999999999999999999']:
            self.assertEqual(self.client.get('/admin?accounts_page='+page).status_code,400)

    @patch('services.intake.app.now', return_value=STAMP)
    def test_accounts_are_escaped_and_credentials_excluded(self, clock):
        self.seed()
        with self.app.app_context():
            db=get_db()
            db.execute("UPDATE private_accounts SET alias='<script>bad</script>' WHERE user_id=3")
            db.commit()
        res=self.client.get('/admin')
        html=res.get_data(as_text=True)
        self.assertEqual(res.status_code,200)
        self.assertIn('&lt;script&gt;bad&lt;/script&gt;',html)
        for secret in ['never-show-password','never-show-totp','never-show-recovery','operator@example.test']:
            self.assertNotIn(secret,html)
        self.assertIn('Registros conservados',html)
        self.assertIn('Clics e impresiones',html)
        self.assertIn('no están disponibles',html)

    def test_downloads_are_cumulative_and_unavailable_is_not_zero(self):
        self.login('operator')
        self.app.config['ADMIN_DOWNLOADS_SNAPSHOT']=SNAPSHOT
        res=self.client.get('/admin?days=7')
        self.assertEqual(res.status_code,200)
        html=res.get_data(as_text=True)
        self.assertIn('137',html)
        self.assertIn('independiente del periodo seleccionado',html)
        self.assertIn('2026-10-11T05:48:00+00:00',html)
        for count in [-1,True,'12',2.5]:
            bad={**SNAPSHOT,'papers':{PAPER:{'pdf_downloads':count}}}
            with self.assertRaises(ValueError):validate_downloads(bad)

    @patch('services.intake.app.now', return_value=STAMP)
    def test_pagination_agent_accounts_and_submission_totals(self, clock):
        self.seed()
        with self.app.app_context():
            db=get_db()
            db.execute("UPDATE users SET created_at='2026-10-02T12:00:00+00:00'")
            for n in range(50):
                db.execute("INSERT INTO users(email,display_name,password_hash,role,created_at) VALUES(?,?,?,'depositor',?)",
                           (f'fixture-{n}@example.test',f'Fixture {n}','unused','2026-10-03T12:00:00+00:00'))
            db.execute("INSERT INTO independent_agents(id,user_id,token_hash,name,version,purpose,created_at,expires_at,policy_version) VALUES('AG-test',3,'never-show-token','Example agent','1','Test','2026-10-02','2026-11-02','P')")
            db.execute("UPDATE private_accounts SET identity_kind='agent' WHERE user_id=3")
            for n,day in enumerate(['2026-10-01','2026-10-02','2026-10-03']):
                db.execute('''INSERT INTO submissions(id,user_id,title,authors,abstract,original_filename,
                    stored_name,sha256,size_bytes,scan_status,scan_detail,status,terms_version,privacy_version,
                    created_at,updated_at) VALUES(?,3,'Synthetic submission','Alias','Test','test.pdf',?,'hash',1,
                    'clean','Test','eligible','T','P',?,?)''',
                    (f'SUB-test-{n}',f'test-{n}.pdf',day+'T12:00:00+00:00',day+'T12:00:00+00:00'))
            db.commit()
        with patch('services.intake.pageviews.render_template',return_value='') as render:
            self.client.get('/admin?start=2026-10-01&end=2026-10-02&accounts_page=2')
        c=render.call_args.kwargs
        self.assertEqual((c['account_count'],c['account_pages'],len(c['accounts'])),(53,2,3))
        self.assertEqual((c['workspaces'],c['workspace_counts']['agent']),(1,1))
        self.assertEqual((c['totals']['submissions'],c['submission_count'],c['submitters']),(2,3,1))
        agent=next(a for a in c['accounts'] if a['agent_id'])
        self.assertEqual((agent['name'],agent['submissions']),('Example agent',3))
        html=self.client.get('/admin?accounts_page=2').get_data(as_text=True)
        self.assertNotIn('never-show-token',html)
        self.assertIn('Example agent',html)

    def test_download_refresh_cached_and_failed_refresh_keeps_dated_copy(self):
        read=install_download_reader(self.app)
        self.app.config['TESTING']=False
        response=MagicMock()
        response.__enter__.return_value=response
        response.geturl.return_value='https://airr.science/metrics.json'
        response.read.return_value=json.dumps(SNAPSHOT).encode()
        with patch('services.intake.admin_statistics.time.monotonic',return_value=1), patch('services.intake.admin_statistics.urllib.request.urlopen',return_value=response) as fetch:
            self.assertEqual(read()[0]['total'],137)
            self.assertEqual(read()[1],False)
            self.assertEqual(fetch.call_count,1)
        with patch('services.intake.admin_statistics.time.monotonic',return_value=700), patch('services.intake.admin_statistics.urllib.request.urlopen',side_effect=OSError('offline')):
            value,failed=read()
            self.assertTrue(failed)
            self.assertEqual(value['total'],137)
            self.assertEqual(value['generated_at'],SNAPSHOT['generated_at'])
