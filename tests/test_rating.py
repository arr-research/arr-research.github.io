# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
import csv
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import test_assessments
from assessmentlib import assessments_for, normalize_model_response, validate_assessment, validate_registry
from ratinglib import aggregate_ratings, load_benchmark, weight_for, SNAPSHOT
import build_site


class RatingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_assessments.AssessmentTests.setUpClass()
        cls.fixture = test_assessments.AssessmentTests()
        cls.papers = cls.fixture.all_versions
        cls.paper = cls.fixture.paper
        cls.benchmark = load_benchmark()

    def report(self, score=6, model="gpt-6-astra", effort="high"):
        report = self.fixture.response(score=score, independence="involved_in_manuscript")
        report["runtime_provenance"] = {"provider":"OpenAI", "model_id":model, "reasoning_effort":effort,
            "basis":"operator_verified_ui", "evidence_sha256":"a"*64}
        return report

    def context(self):
        return {"mode":"fresh_blind", "history_isolated":True, "memory_disabled":True,
                "other_reports_withheld":True, "basis":"operator_verified_ui",
                "evidence_sha256":"b"*64, "recorded_at":"2026-09-12T14:00:00Z"}

    def test_native_snapshot_attribution_hash_and_values(self):
        raw = SNAPSHOT.with_suffix(".csv").read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.benchmark["raw_csv_sha256"])
        rows=list(csv.DictReader(raw.decode("utf-8-sig").splitlines()))
        self.assertEqual(len(rows),len(self.benchmark["results"]))
        lookup={r["id"]:r for r in rows}
        for r in self.benchmark["results"]:
            native=lookup[r["run_id"]]
            self.assertEqual(r["model_version"],native["Model version"])
            self.assertEqual(r["accuracy"],float(native["mean_score"]))
            self.assertEqual(r["standard_error"],float(native["stderr"]))
            self.assertEqual(r["organization"],native["Organization"])

    def test_stronger_configuration_influences_score_without_rewriting_reports(self):
        reports=[self.report(6),self.report(8,"gpt-5.6-sol")]
        original=copy.deepcopy(reports)
        result=aggregate_ratings(reports)
        self.assertAlmostEqual(next(w["weight"] for w in result["weights"] if w["model"][1]=="gpt-6-astra"),2.904)
        self.assertAlmostEqual(result["score"],(6*2.904+8)/3.904)
        self.assertEqual(reports,original)
        self.assertIsNone(result["confidence_probability"])
        self.assertFalse(result["acceptance_determined"])

    def test_unknown_effort_does_not_borrow_max_or_self_reported_identity(self):
        r=self.report(6,"gpt-5.6-sol","high")
        r["model_id"]="gpt-6-astra"
        self.assertEqual(weight_for(r,self.benchmark)["weight"],1)
        r.pop("runtime_provenance")
        self.assertEqual(weight_for(r,self.benchmark)["weight"],1)
        r=self.report()
        r["runtime_provenance"]["evidence_sha256"]="unverified"
        self.assertEqual(weight_for(r,self.benchmark)["weight"],1)

    def test_weights_bounded_and_score_is_convex(self):
        for row in self.benchmark["results"]:
            model,effort=row["model_version"].rsplit("_",1) if "_" in row["model_version"] else (row["model_version"],"none")
            r=self.report(model=model,effort=effort)
            r["runtime_provenance"]["provider"]=row["organization"]
            w=weight_for(r,self.benchmark)["weight"]
            self.assertGreaterEqual(w,1)
            self.assertLessEqual(w,3)
        for x,y in [(0,10),(3,4),(10,0),(6,6)]:
            agg=aggregate_ratings([self.report(x),self.report(y,"gpt-5.6-sol")])
            self.assertGreaterEqual(agg["score"],min(x,y))
            self.assertLessEqual(agg["score"],max(x,y))

    def test_effort_variants_do_not_multiply_votes_and_latest_is_not_best(self):
        early=self.report(8,effort="max")
        later=self.report(4,effort="high")
        later["assessed_at"]="2026-08-30T11:01:00-01:00"
        result=aggregate_ratings([later,early])
        self.assertEqual(result["score"],4)
        self.assertEqual(result["count"],1)
        self.assertEqual(result["preserved_reports"],2)
        with self.assertRaisesRegex(ValueError,"Conflicting simultaneous"):
            aggregate_ratings([early,self.report(4)])

    def test_hashes_versions_invalid_scores_and_naive_dates_fail_closed(self):
        for key,value in [("canonical_sha256","f"*64),("version_id","other")]:
            r=self.report(4,"gpt-5.6-sol")
            r[key]=value
            with self.assertRaisesRegex(ValueError,"cannot pool"):
                aggregate_ratings([self.report(),r])
        for score in [float("nan"),float("inf"),-1,11,True]:
            r=self.report();r["millennium_score"]=score
            with self.assertRaisesRegex(ValueError,"Invalid rating"):
                aggregate_ratings([r])
        r=self.report();r["assessed_at"]="2026-09-12T14:00:00"
        with self.assertRaisesRegex(ValueError,"timezone"):
            aggregate_ratings([r])
        self.assertIsNone(aggregate_ratings([]))

    def test_same_version_identifier_with_wrong_pdf_is_not_attached(self):
        r=self.report();r["canonical_sha256"]="f"*64
        self.assertEqual(assessments_for([r],self.paper),[])

    def test_source_first_review_uses_exact_pdf_and_preserves_involvement(self):
        from assessmentlib import assessment_artifact_sha256
        from prepare_model_assessment import build_prompt
        p=next(p for p in self.papers if p.id=="ARR-2026-2MHNZRRJP49Y9SWP")
        pdf_digest=hashlib.sha256((p.path/"paper.pdf").read_bytes()).hexdigest()
        self.assertEqual(assessment_artifact_sha256(p),pdf_digest)
        self.assertNotEqual(pdf_digest,p.metadata["integrity"]["source_sha256"])
        prompt=build_prompt(p,"involved_in_manuscript")
        self.assertIn(pdf_digest,prompt)
        self.assertIn('"independence": "involved_in_manuscript"',prompt)
        self.assertIn("missing memory in a fresh thread is not evidence",prompt)

    def test_later_positive_score_does_not_dispose_of_old_objection(self):
        negative=self.report(2)
        negative["recommendation"]="reject"
        negative["unresolved_material_objections"]=["A counterexample invalidates Lemma 1."]
        later=self.report(8)
        later["assessed_at"]="2026-09-01T12:00:00Z"
        result=aggregate_ratings([negative,later])
        self.assertEqual(result["score"],8)
        self.assertIn(negative["assessment_id"],result["blocking_report_ids"])
        self.assertEqual(result["evidence_backing"],"Limited")
        self.assertFalse(result["acceptance_determined"])

    def test_context_is_operator_evidence_preserving_native_hash(self):
        r=self.report();before=r["source_response_sha256"]
        r["review_context"]=self.context()
        self.assertEqual(validate_assessment(r,self.papers),[])
        self.assertEqual(r["source_response_sha256"],before)
        native={k:v for k,v in r.items() if k not in {"assessment_id","source_response_sha256","runtime_provenance"}}
        with self.assertRaisesRegex(ValueError,"operator-controlled"):
            normalize_model_response(native)
        for key,value in [("memory_disabled",False),("history_isolated",1),("evidence_sha256","made up"),("basis","model_claim")]:
            changed=copy.deepcopy(r);changed["review_context"][key]=value
            self.assertTrue(any("review_context" in e for e in validate_assessment(changed,self.papers)))

    def test_broader_support_requires_context_diversity_and_matching_evidence(self):
        a=self.report()
        b=self.report(6,"other-model")
        b["runtime_provenance"]["provider"]="Other provider"
        bench=copy.deepcopy(self.benchmark)
        bench["results"].append({"organization":"Other provider","model_version":"other-model_high","accuracy":.8,"standard_error":.1,"run_id":"synthetic-test-only"})
        for r in [a,b]:r["review_context"]=self.context()
        result=aggregate_ratings([a,b],benchmark=bench)
        self.assertEqual(result["evidence_backing"],"Broader model support")
        self.assertIsNone(result["confidence_probability"])
        b.pop("review_context")
        self.assertEqual(aggregate_ratings([a,b],benchmark=bench)["evidence_backing"],"Limited")

    def test_subject_scope_uses_curated_math_and_not_arbitrary_keywords(self):
        from arrlib import Paper
        metadata=copy.deepcopy(self.paper.metadata)
        metadata["subjects"]=["Mind Science"]
        metadata["keywords"]=["math", "quantum", "lattice"]
        p=Paper(self.paper.path,metadata)
        self.assertEqual(build_site.paper_rating(p,[self.report()])["weights"][0]["weight"],1)
        metadata["subjects"]=["Matrix analysis"]
        self.assertAlmostEqual(build_site.paper_rating(p,[self.report()])["weights"][0]["weight"],2.904)

    def test_public_intake_projection_preserves_native_report_and_rejects_tampering(self):
        from import_public_intake_assessment import project_report
        from assessmentlib import source_hash
        p=next(p for p in self.papers if p.id=="ARR-2026-1K33A7K90T87AREF")
        source=p.path/"screening/model-1-gpt-6-astra-report.json"
        native=json.loads(source.read_bytes())
        report=project_report(p,source)
        self.assertEqual(report["prompt_version"],"ARR-INTAKE-ASSESS-1.1")
        self.assertEqual(report["source_response_sha256"],source_hash(native))
        for key in ("millennium_score","summary","assessed_at","independence"):
            self.assertEqual(report[key],native[key])
        self.assertNotIn("review_context",report)
        self.assertNotIn("runtime_provenance",report)
        self.assertEqual(validate_assessment(report,self.papers),[])
        tampered=copy.deepcopy(report);tampered["millennium_score"]=5
        self.assertTrue(any("intake_source" in e for e in validate_assessment(tampered,self.papers)))
        tampered=copy.deepcopy(report);tampered["intake_source"]["path"]="registry/model-assessments.json"
        self.assertTrue(any("intake_source" in e for e in validate_assessment(tampered,self.papers)))
        with self.assertRaisesRegex(ValueError,"already-public"):
            project_report(self.paper,source)
        self.assertEqual(json.loads(source.read_bytes()),native)

    def test_existing_reports_unchanged_and_every_paper_has_coverage(self):
        from arrlib import group_paper_versions
        registry=json.loads((ROOT/"registry/model-assessments.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_registry(registry,self.papers),[])
        papers=[v[-1] for v in group_paper_versions(self.papers).values()]
        _,lookup=build_site.load_authors(papers)
        page=build_site.build_assessments(papers,registry["assessments"],[],"","https://example.test",lookup)
        coverage=page.split('id="coverage"',1)[1]
        for p in papers:self.assertIn(p.id,coverage)
        self.assertIn("8 rated current versions",page)
        self.assertIn("12 preserved reports",page)
        self.assertIn("Assessment pending",page)
        self.assertNotIn("Median assessment",page)
        self.assertNotIn("marked independent of manuscript",page)
        for r in registry["assessments"]:
            self.assertNotIn("review_context",r)
            self.assertEqual(aggregate_ratings([r])["evidence_backing"],"Limited")

if __name__=="__main__":unittest.main()
