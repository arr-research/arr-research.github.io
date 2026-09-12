import hashlib
import json
import unittest
from pathlib import Path

import test_intake
from services.intake.app import get_db, iso, model_review_template, validate_model_review


class FounderReviewTests(unittest.TestCase):
    setUp = test_intake.IntakeTests.setUp
    tearDown = test_intake.IntakeTests.tearDown
    user_id = test_intake.IntakeTests.user_id
    login_session = test_intake.IntakeTests.login_session
    upload = test_intake.IntakeTests.upload
    add_model_review = test_intake.IntakeTests.add_model_review

    def declare(self, case_id):
        token = self.login_session('operator@example.org')
        return self.client.post(f'/admin/submission/{case_id}/founder-authorship', data={'csrf_token':token,'founder_author':'on','reason':'The configured founder explicitly confirms authorship of this exact manuscript.'})

    def decide(self, case_id):
        token = self.login_session('operator@example.org')
        return self.client.post(f'/admin/submission/{case_id}/decision', data={'csrf_token':token,'action':'accept','reason':'Signed after inspecting both actual reports.'})

    def test_two_models_required_and_author_editor_acceptance(self):
        case_id = self.upload(conflict=True)
        self.assertEqual(self.declare(case_id).status_code,302)
        self.add_model_review(case_id,1)
        self.assertEqual(self.decide(case_id).status_code,409)
        self.add_model_review(case_id,2)
        with self.app.app_context():
            db=get_db()
            db.execute('UPDATE assessment_plans SET providers_json=? WHERE id=(SELECT MAX(id) FROM assessment_plans)',(json.dumps([{'provider':f'Provider {n}','model_id':f'frontier-model-{n}'} for n in [1,2]]),))
            db.commit()
        self.assertEqual(self.decide(case_id).status_code,302)
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            self.assertEqual(row['status'],'accepted_for_publication')
            self.assertIsNone(row['public_released_at'])
            event=get_db().execute("SELECT detail_json FROM audit_log WHERE event='editorial_decision' ORDER BY id DESC LIMIT 1").fetchone()[0]
            self.assertTrue(json.loads(event)['founder_author_editor'])

    def test_other_conflict_still_requires_independent_editor(self):
        case_id=self.upload(conflict=True)
        self.add_model_review(case_id,1)
        self.assertEqual(self.decide(case_id).status_code,302)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT status FROM submissions WHERE id=?',(case_id,)).fetchone()[0],'awaiting_independent_decision')

    def test_independent_editor_cannot_declare_founder_exception(self):
        case_id=self.upload(conflict=True)
        token=self.login_session('independent@example.org')
        result=self.client.post(f'/admin/submission/{case_id}/founder-authorship',data={'csrf_token':token,'founder_author':'on','reason':'A sufficiently long explanation cannot authorize another operator role.'})
        self.assertEqual(result.status_code,403)

    def test_another_conflict_blocks_founder_self_decision(self):
        case_id=self.upload(conflict=True)
        self.assertEqual(self.declare(case_id).status_code,302)
        token=self.login_session('operator@example.org')
        result=self.client.post(f'/admin/submission/{case_id}/conflict',data={'csrf_token':token,'reason':'An additional financial conflict beyond authorship was identified.'})
        self.assertEqual(result.status_code,302)
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            actor=get_db().execute("SELECT * FROM users WHERE email='operator@example.org'").fetchone()
            self.assertTrue(row['founder_authored'])
            self.assertTrue(row['other_operator_conflict'])
            self.assertFalse(self.app.extensions['editorial']['founder_may_decide'](row,actor))

    def test_prior_involvement_is_eligible_without_changing_founder_authorship(self):
        case_id=self.upload(conflict=True)
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            report=model_review_template(row)
            report.update(provider='OpenAI',model_id='gpt-6-astra',assessed_at=iso(),independence='involved_in_manuscript')
            self.assertEqual(validate_model_review(report,row),[])
            self.assertFalse(row['founder_authored'])
        self.assertEqual(self.declare(case_id).status_code,302)
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            self.assertEqual(validate_model_review(report,row),[])

    def evidence_file(self, case_id):
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            value=dict(submission_id=case_id,manuscript_sha256=row['sha256'],notice='The author authorizes the exact PDF and sources for the named models in their existing Codex/OpenAI account, with its current settings and service conditions.',author_instruction='Yes, Astra and GPT-5.6 Sol in Codex/OpenAI.',source_reference='Explicit user instruction in the dated private task transcript.',authorization_recorded_at=iso(),models=[{'provider':'OpenAI','model_id':m} for m in ['gpt-6-astra','gpt-5.6-sol']],founder_authorship_basis='The author explicitly states that this is their work and requests its corrected version before formal assessment.')
        path=Path(self.temp.name)/'authorization.json'
        path.write_text(json.dumps(value),encoding='utf-8')
        return path,value

    def test_external_authorization_is_audited_and_cannot_replace_round(self):
        case_id=self.upload(conflict=True)
        path,value=self.evidence_file(case_id)
        cli=self.app.test_cli_runner()
        result=cli.invoke(args=['prepare-founder-round',case_id,str(path),'--request-changes'])
        self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['accepted'])
        with self.app.app_context():
            db=get_db()
            self.assertEqual(db.execute('SELECT status FROM submissions WHERE id=?',(case_id,)).fetchone()[0],'changes_requested')
            audit=json.loads(db.execute("SELECT detail_json FROM audit_log WHERE event='external_author_instruction_recorded'").fetchone()[0])
            self.assertEqual(audit['evidence'],value)
            self.assertEqual(audit['method'],'operator_recorded_external_instruction')
        self.assertNotEqual(cli.invoke(args=['prepare-founder-round',case_id,str(path)]).exit_code,0)

    def test_reject_duplicate_models_or_wrong_artifact_before_mutation(self):
        case_id=self.upload(conflict=True)
        path,value=self.evidence_file(case_id)
        value['models'][1]=value['models'][0]
        path.write_text(json.dumps(value),encoding='utf-8')
        cli=self.app.test_cli_runner()
        self.assertNotEqual(cli.invoke(args=['prepare-founder-round',case_id,str(path)]).exit_code,0)
        with self.app.app_context():
            self.assertEqual(get_db().execute('SELECT COUNT(*) FROM assessment_plans').fetchone()[0],0)

    def test_cli_preserves_rejection_and_validates_runtime_provenance(self):
        case_id=self.upload(conflict=True)
        path,value=self.evidence_file(case_id)
        cli=self.app.test_cli_runner()
        self.assertEqual(cli.invoke(args=['prepare-founder-round',case_id,str(path),'--request-changes']).exit_code,0)
        with self.app.app_context():
            row=get_db().execute('SELECT * FROM submissions WHERE id=?',(case_id,)).fetchone()
            report=model_review_template(row)
        report.update(provider='OpenAI',model_id='gpt-6-astra',assessed_at=iso(),independence='involved_in_manuscript',recommendation='reject',millennium_score=2.0,overall_stars=2,unresolved_material_objections=['The stated central lemma does not follow from the supplied hypotheses.'])
        report_path=Path(self.temp.name)/'report.json'
        report_path.write_text(json.dumps(report),encoding='utf-8')
        evidence={'provider':'OpenAI','model_id':'gpt-5.6-sol','report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest(),'source_reference':'Recorded platform invocation identifier and actual response.'}
        runtime=Path(self.temp.name)/'runtime.json'
        runtime.write_text(json.dumps(evidence),encoding='utf-8')
        self.assertNotEqual(cli.invoke(args=['record-assessment',str(report_path),str(runtime)]).exit_code,0)
        evidence['model_id']='gpt-6-astra'
        runtime.write_text(json.dumps(evidence),encoding='utf-8')
        result=cli.invoke(args=['record-assessment',str(report_path),str(runtime)])
        self.assertEqual(result.exit_code,0,result.output)
        self.assertFalse(json.loads(result.output)['model_gate_ready'])
        with self.app.app_context():
            self.assertEqual(json.loads(get_db().execute('SELECT response_json FROM model_reviews').fetchone()[0]),report)
            self.assertEqual(get_db().execute('SELECT status FROM submissions WHERE id=?',(case_id,)).fetchone()[0],'changes_requested')
        self.assertNotEqual(cli.invoke(args=['record-assessment',str(report_path),str(runtime)]).exit_code,0)
