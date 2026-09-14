import json
from pathlib import Path
from test_historical_revisions import HistoricalRevisionTests
from services.intake.app import get_db, iso


class ExternalEditorialTests(HistoricalRevisionTests):
    def prepared_case(self, complete=True):
        case_id=self.send_revision(self.issue()).get_json()['registration_number']
        token=self.login_session('operator@example.org')
        with self.app.app_context():
            get_db().execute("UPDATE users SET display_name='Operator Author' WHERE email='operator@example.org'");get_db().commit()
        self.assertEqual(self.client.post('/admin/submission/'+case_id+'/founder-authorship',data={'csrf_token':token,'founder_author':'on','reason':'Explicit sole author declaration for the exact historical fixture.'}).status_code,302)
        self.add_model_review(case_id,1)
        if complete:self.add_model_review(case_id,2)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE assessment_plans SET providers_json=?',(json.dumps([{'provider':f'Provider {n}','model_id':f'frontier-model-{n}'} for n in [1,2]]),));db.commit()
            row=db.execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            hashes=[r[0] for r in db.execute('SELECT response_sha256 FROM model_reviews WHERE submission_id=?',(case_id,))]
        return dict(submission_id=case_id,manuscript_sha256=row['sha256'],human_name='Operator Author',human_instruction='I have received the concrete two-review result and explicitly accept this exact paper; this is my editorial instruction.',source_reference='Dated direct operator instruction in the test fixture.',recorded_at=iso(),decision='accept',reason='Accepted on explicit human instruction after the two-report gate.',report_sha256=hashes)

    def invoke_evidence(self, command, value):
        p=Path(self.temp.name)/'external.json';p.write_text(json.dumps(value))
        return self.app.test_cli_runner().invoke(args=[command,str(p)])

    def test_external_decision_preserves_all_guards(self):
        e=self.prepared_case();cmd='record-external-founder-decision'
        for update in [{'manuscript_sha256':'0'*64},{'human_instruction':''},{'human_name':'Someone else'},{'report_sha256':[]},{'recorded_at':'2000-01-01T00:00:00Z'}]:
            self.assertNotEqual(self.invoke_evidence(cmd,{**e,**update}).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE submissions SET other_operator_conflict=1 WHERE id=?',(e['submission_id'],));db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE submissions SET other_operator_conflict=0 WHERE id=?',(e['submission_id'],));db.execute("UPDATE model_reviews SET recommendation='major_revision' WHERE id=(SELECT MAX(id) FROM model_reviews)");db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute("UPDATE model_reviews SET recommendation='accept'");db.commit()
            row=db.execute('SELECT * FROM submissions WHERE id=?',(e['submission_id'],)).fetchone();pdf=Path(self.app.config['QUARANTINE'])/row['stored_name'];original=pdf.read_bytes();pdf.write_bytes(b'changed')
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0);pdf.write_bytes(original)
        result=self.invoke_evidence(cmd,e);self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['published'])
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)
        with self.app.app_context():
            db=get_db();self.assertEqual(db.execute('SELECT COUNT(*) FROM publication_permissions').fetchone()[0],0)
            audit=json.loads(db.execute("SELECT detail_json FROM audit_log WHERE event='editorial_decision'").fetchone()[0]);self.assertEqual(audit['method'],'operator_recorded_external_instruction');self.assertEqual(audit['evidence'],e)

    def test_external_incomplete_round_cannot_accept(self):
        self.assertNotEqual(self.invoke_evidence('record-external-founder-decision',self.prepared_case(False)).exit_code,0)

    def test_external_public_permission_is_separate_and_immutable(self):
        e=self.prepared_case();p={k:v for k,v in e.items() if k not in {'decision','reason','report_sha256'}}
        p.update(license='LicenseRef-Author-Retained',distribution_scope=['exact_manuscript','assessment_reports','associated_sources'],rights_basis='The author retains copyright and explicitly permits AIRR to distribute these exact files; no additional public reuse licence is granted.')
        cmd='record-external-founder-publication'
        self.assertNotEqual(self.invoke_evidence(cmd,p).exit_code,0)
        result=self.invoke_evidence('record-external-founder-decision',e);self.assertEqual(result.exit_code,0,result.output)
        self.assertNotEqual(self.invoke_evidence(cmd,{**p,'manuscript_sha256':'0'*64}).exit_code,0)
        self.assertNotEqual(self.invoke_evidence(cmd,{**p,'distribution_scope':[]}).exit_code,0)
        result=self.invoke_evidence(cmd,p);self.assertEqual(result.exit_code,0,result.output);self.assertFalse(json.loads(result.output)['published'])
        self.assertNotEqual(self.invoke_evidence(cmd,p).exit_code,0)
