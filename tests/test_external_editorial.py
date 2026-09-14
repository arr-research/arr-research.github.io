import json
from pathlib import Path
from test_historical_revisions import HistoricalRevisionTests
from services.intake.app import get_db, iso


class ExternalEditorialTests(HistoricalRevisionTests):
    def prepared_case(self, complete=True, ordinary=False):
        if ordinary:
            from test_agent_intake import AgentIntakeTests
            helper=AgentIntakeTests();helper.__dict__.update(self.__dict__)
            grant=helper.request_grant();helper.approve(grant)
            response=helper.upload(grant,metadata_changes={'authors':'Operator Author','operator_conflict':True},pdf=self.pdf)
            self.assertEqual(response.status_code,201,response.data)
            case_id=response.get_json()['registration_number']
        else:
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

    def test_ordinary_founder_case_uses_real_deposit_and_separate_public_permission(self):
        e=self.prepared_case(ordinary=True);sid=e['submission_id']
        with self.app.app_context():
            db=get_db()
            self.assertIsNone(db.execute('SELECT 1 FROM historical_revisions WHERE submission_id=?',(sid,)).fetchone())
            self.assertIsNone(db.execute('SELECT parent_id FROM submissions WHERE id=?',(sid,)).fetchone()[0])
        result=self.invoke_evidence('record-external-founder-decision',e)
        self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['published'])
        p={k:v for k,v in e.items() if k not in {'decision','reason','report_sha256'}}
        p.update(license='LicenseRef-Author-Retained',distribution_scope=['exact_manuscript','assessment_reports','associated_sources'],rights_basis='The sole author retains copyright and authorizes distribution of this exact manuscript and its associated reports and sources.')
        result=self.invoke_evidence('record-external-founder-publication',p)
        self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['published'])

    def test_ordinary_case_cannot_skip_owner_authorship_or_review_guards(self):
        e=self.prepared_case(ordinary=True);sid=e['submission_id'];cmd='record-external-founder-decision'
        with self.app.app_context():
            db=get_db();owner=db.execute('SELECT user_id FROM submissions WHERE id=?',(sid,)).fetchone()[0]
            db.execute('UPDATE users SET active=0 WHERE id=?',(owner,));db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE users SET active=1 WHERE id=?',(owner,));db.execute("UPDATE submissions SET authors='Operator Author; Another Author' WHERE id=?",(sid,));db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute("UPDATE submissions SET authors='Operator Author' WHERE id=?",(sid,));db.execute("UPDATE model_reviews SET unresolved_material_objections=1 WHERE submission_id=?",(sid,));db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,e).exit_code,0)

    def test_external_minor_disposition_preserves_report_and_gate(self):
        e=self.prepared_case();sid=e['submission_id']
        with self.app.app_context():
            db=get_db();review=db.execute('SELECT * FROM model_reviews WHERE submission_id=? ORDER BY id DESC',(sid,)).fetchone()
            db.execute("UPDATE model_reviews SET recommendation='minor_revision' WHERE id=?",(review['id'],));db.commit()
        cmd='record-external-founder-adjudication'
        v={k:x for k,x in e.items() if k not in {'decision','reason','report_sha256'}}
        v.update(report_sha256=review['response_sha256'],basis='The minor source documentation issue was corrected in a separate associated-source note, preserving every original report and exact PDF.',resolution_evidence='Preserved source diff and reviewer correction receipt identify the original and corrected source hashes.',all_objections_addressed=True)
        self.assertNotEqual(self.invoke_evidence('record-external-founder-decision',e).exit_code,0)
        for update in [{'manuscript_sha256':'0'*64},{'report_sha256':'0'*64},{'human_name':'Other person'},{'all_objections_addressed':False},{'basis':'short'},{'recorded_at':'2000-01-01T00:00:00Z'}]:
            self.assertNotEqual(self.invoke_evidence(cmd,{**v,**update}).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE model_reviews SET unresolved_material_objections=1 WHERE id=?',(review['id'],));db.commit()
        self.assertNotEqual(self.invoke_evidence(cmd,v).exit_code,0)
        with self.app.app_context():
            db=get_db();db.execute('UPDATE model_reviews SET unresolved_material_objections=0 WHERE id=?',(review['id'],));db.commit()
        result=self.invoke_evidence(cmd,v);self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['accepted'])
        self.assertNotEqual(self.invoke_evidence(cmd,v).exit_code,0)
        with self.app.app_context():
            db=get_db();preserved=db.execute('SELECT * FROM model_reviews WHERE id=?',(review['id'],)).fetchone()
            self.assertEqual(preserved['response_json'],review['response_json']);self.assertEqual(preserved['response_sha256'],review['response_sha256']);self.assertEqual(preserved['recommendation'],'minor_revision')
            self.assertNotEqual(db.execute('SELECT status FROM submissions WHERE id=?',(sid,)).fetchone()[0],'accepted_for_publication')
        accepted=self.invoke_evidence('record-external-founder-decision',e);self.assertEqual(accepted.exit_code,0,accepted.output)

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
