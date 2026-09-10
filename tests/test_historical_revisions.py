import hashlib
import io
import json
from pathlib import Path
import uuid
from unittest.mock import patch

import test_intake as fixtures
from services.intake.app import get_db, iso


class HistoricalRevisionTests(fixtures.IntakeTests):
    def setUp(self):
        super().setUp()
        self.pdf=b'%PDF-1.7\nnew exact revision'
        self.parent={'record_id':'arr:record:'+str(uuid.uuid4()),'version_id':'arr:version:'+str(uuid.uuid4()),'version':'v1','canonical_sha256':'a'*64,'authors':['Operator Author']}
        self.catalog=Path(self.temp.name)/'catalog.json'
        self.catalog.write_text(json.dumps({'ARR-2026-3AJ7W5BS3N9VR8KM':self.parent}))
        self.app.config.update(HISTORICAL_REVISIONS_ENABLED=True,HISTORICAL_REVISION_CATALOGUE=str(self.catalog),HISTORICAL_OPERATOR_AUTHOR='Operator Author')
        self.binding={'paper_id':'ARR-2026-3AJ7W5BS3N9VR8KM','record_id':self.parent['record_id'],'supersedes_version_id':self.parent['version_id'],'parent_sha256':'a'*64,'version':'v2','version_id':'arr:version:'+str(uuid.uuid4()),'sha256':hashlib.sha256(self.pdf).hexdigest(),'changelog':{k:'Explicit unchanged statement' for k in ['mathematics','scope','reproducibility','version','editorial']}}

    def issue(self,changes=None,expected=0):
        with self.app.app_context():
            owner=get_db().execute("SELECT id FROM users WHERE email='direct-author@accounts.invalid'").fetchone()[0]
        from services.intake import app as a
        evidence={'owner_user_id':owner,'agent_name':'Revision agent','agent_version':'test model','binding':self.binding,'author_instruction':'I explicitly authorize this exact revision PDF and record its historical parent and grant scope.','source_reference':'Authenticated operator instruction fixture','recorded_at':iso(),'scope':['revision:create','submission:receipt'],'terms_version':a.TERMS_VERSION,'privacy_version':a.PRIVACY_VERSION,'operator_authorship_confirmed':True}
        evidence.update(changes or {})
        path=Path(self.temp.name)/'evidence.json';path.write_text(json.dumps(evidence))
        result=self.app.test_cli_runner().invoke(args=['authorize-historical-revision',str(path)])
        self.assertEqual(result.exit_code,expected,result.output)
        return json.loads(result.output) if expected==0 else None

    def send_revision(self,grant,path='/api/v1/revisions',key='revision-test-001',pdf=None):
        metadata={'title':'Revision of a historical paper','authors':'Operator Author','abstract':'A'*120,'primary_subject':'airr-quantum-information','secondary_subjects':[],'specific_topic':'','sha256':self.binding['sha256'],'ai_disclosure':'Test fixture model contribution explicitly declared.','operator_conflict':True,'rights_confirmed':True}
        with patch('services.intake.app.scan_file',return_value=('clean','test scanner')):
            response=self.client.post(path,headers={'Authorization':'Bearer '+grant['agent_token'],'Idempotency-Key':key},data={'metadata':json.dumps(metadata),'manuscript':(io.BytesIO(self.pdf if pdf is None else pdf),'v2.pdf')})
        response.request.environ['wsgi.input'].close()
        return response

    def test_historical_receipt_preserves_parent_without_fictional_case(self):
        before=self.catalog.read_bytes();g=self.issue();r=self.send_revision(g)
        self.assertEqual(r.status_code,201,r.data)
        receipt=r.get_json();self.assertEqual(receipt['historical_revision'],self.binding)
        self.assertEqual(receipt['sha256'],self.binding['sha256']);self.assertFalse(receipt['published'])
        with self.app.app_context():
            db=get_db();self.assertEqual(db.execute('SELECT COUNT(*) FROM submissions').fetchone()[0],1)
            row=db.execute('SELECT * FROM submissions').fetchone();self.assertIsNone(row['parent_id'])
            self.assertEqual(db.execute('SELECT COUNT(*) FROM model_reviews').fetchone()[0],0)
        self.assertEqual(self.catalog.read_bytes(),before)
        page=self.client.get('/case/'+receipt['registration_number'])
        self.assertEqual(page.status_code,200)
        self.assertIn(self.binding['supersedes_version_id'].encode(),page.data)
        repeat=self.send_revision(g);self.assertEqual(repeat.status_code,200);self.assertEqual(repeat.get_json()['registration_number'],receipt['registration_number'])
        self.assertEqual(self.send_revision(g,key='second-key-002').status_code,403)
        self.assertEqual(self.send_revision(g,pdf=b'%PDF-corrupt-retry').status_code,400)

    def test_revision_scope_does_not_grant_new_deposits_or_editor_access(self):
        g=self.issue();self.assertEqual(self.send_revision(g,path='/api/v1/submissions').status_code,403)
        status=self.client.get('/api/v1/agent-authorization',headers={'Authorization':'Bearer '+g['agent_token']}).get_json()
        self.assertEqual(status['scope'],['revision:create','submission:receipt']);self.assertEqual(status['uploads_remaining'],1)
        self.assertNotEqual(self.app.test_client().get('/admin/statistics',headers={'Authorization':'Bearer '+g['agent_token']}).status_code,200)

    def test_new_deposit_grant_cannot_create_revision(self):
        from test_agent_intake import AgentIntakeTests
        helper=AgentIntakeTests();helper.__dict__.update(self.__dict__)
        g=helper.request_grant();helper.approve(g)
        self.assertEqual(self.send_revision(g).status_code,403)

    def test_fail_closed_disabled_stale_wrong_hash_and_revoked(self):
        self.app.config['HISTORICAL_REVISIONS_ENABLED']=False;self.issue(expected=1)
        self.app.config['HISTORICAL_REVISIONS_ENABLED']=True;g=self.issue()
        self.assertEqual(self.send_revision(g,pdf=b'%PDF-wrong').status_code,400)
        with self.app.app_context():self.assertEqual(get_db().execute('SELECT COUNT(*) FROM submissions').fetchone()[0],0)
        self.catalog.write_text(self.catalog.read_text()+'\n');self.assertEqual(self.send_revision(g).status_code,409)
        with self.app.app_context():
            get_db().execute("UPDATE agent_grants SET state='revoked' WHERE id=?",(g['request_id'],));get_db().commit()
        self.assertEqual(self.send_revision(g).status_code,403)

    def test_author_and_predecessor_must_match_catalogue(self):
        self.binding['record_id']='other';self.issue(expected=1)
        self.binding['record_id']=self.parent['record_id'];self.app.config['HISTORICAL_OPERATOR_AUTHOR']='Other Author';self.issue(expected=1)

    def test_expired_permission_rejected(self):
        g=self.issue()
        with self.app.app_context():
            get_db().execute("UPDATE agent_grants SET expires_at='2000-01-01T00:00:00+00:00' WHERE id=?",(g['request_id'],));get_db().commit()
        self.assertEqual(self.send_revision(g).status_code,403)

    def test_duplicate_version_rolls_back_and_other_grant_cannot_read_receipt(self):
        first=self.issue();received=self.send_revision(first)
        self.assertEqual(received.status_code,201)
        second=self.issue()
        self.assertEqual(self.send_revision(second).status_code,409)
        headers={'Authorization':'Bearer '+second['agent_token']}
        self.assertEqual(self.client.get('/api/v1/submissions/'+received.get_json()['registration_number'],headers=headers).status_code,404)
        with self.app.app_context():
            from services.intake.historical_revisions import migrate
            db=get_db();migrate(db);migrate(db)
            self.assertEqual(db.execute('SELECT COUNT(*) FROM submissions').fetchone()[0],1)
            self.assertEqual(db.execute('SELECT uses FROM agent_grants WHERE id=?',(second['request_id'],)).fetchone()[0],0)
        self.assertEqual(len(list(Path(self.app.config['QUARANTINE']).glob('*.pdf'))),1)
