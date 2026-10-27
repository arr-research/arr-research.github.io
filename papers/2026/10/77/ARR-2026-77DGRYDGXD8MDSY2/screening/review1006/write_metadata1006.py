"""Create exact1005 assessment metadata without altering prior assessments."""
from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parent
PRIOR=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,data):
    with (ROOT/name).open('x',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
inp=json.loads((ROOT/'input'/'INPUT1006.json').read_text(encoding='utf-8-sig'))
integrity=json.loads((ROOT/'INPUT-VERIFIED1006.json').read_text(encoding='utf-8'))
public=json.loads((ROOT/'PUBLIC-VERIFIED1006-run01.json').read_text(encoding='utf-8'))
replay=json.loads((ROOT/'PUBLIC-REPLAY1006.json').read_text(encoding='utf-8'))
controls=json.loads((ROOT/'CONTROLS1006.json').read_text(encoding='utf-8'))
input_hashes={p.name:sha(p) for p in (ROOT/'input').iterdir() if p.is_file()}
old=json.loads((PRIOR/'READINGS998.json').read_text(encoding='utf-8'))
sources=[]
for x in old['sources']:
    row={k:x[k] for k in ['key','id','authors','title','url','pdf_url','pdf_sha256','pdf_pages','level','locations','full_paper_read']}
    row['prior_reading_provenance']='review998, reused context; source hashes measured during998, not remeasured in1006.'
    if x['id']=='1508.03551v1':
        row['current1006_reading']='Theorem6.1 statement and nearby context via primary PDF; no full AppendixB audit.'
    elif x['id']=='2505.15281v3':
        row['current1006_reading']='Definitions127–128, Theorem105, Algorithm1 and displayed correctness passages via primary PDF; not full paper/proof audit.'
        row['now_in_frozen1005_bibliography']=True
    else:row['current1006_reading']='No new substantive reading; prior998 partial reading reused and declared.'
    sources.append(row)
save('READINGS1006.json',{'utc':NOW,'manuscript':{'pdf_pages_read':8,'all_page_renders_inspected':True,'all_tex_read':True,'source_diff_read':True,'changes1005_json_read':True},
 'sources':sources,'search_scope':'Targeted recheck of corrected citations and public supplement; no fresh exhaustive global novelty search.',
 'full_external_papers_read_in1006':0,'prior_literature_context_reused':True,
 'public_supplement':{'commit':public['commit'],'manifest_sha256':public['manifest_fetch']['sha256'],'manifest_entries':30,'selected_files_hash_checked':13,'public_scripts_read_and_run':3,'audit988_bodies_scientifically_read':False,'extensions997_1003_read':False},
 'external_corpus_persisted':False,'note':'Public user-authored supplement files copied for requested reproduction are not an external literature corpus.'})

objections=[
 {'id':'O1','status':'resolved','pdf_pages':[7],'basis':'Actual PDF URI pins full commit; manifest and13selected public files anonymously accessible and hash-valid; three downloaded scripts reproduce stored outputs.','limits':'Only selected relevant public entries checked; no scientific endorsement of audit988 or later extensions.'},
 {'id':'O2','status':'resolved','pdf_pages':[7,8],'basis':'George–Tomamichelv3 is cited and fixed-base/ordinary/constrained-complete domains are distinguished consistently with re-read passages.','limits':'Priority worldwide remains unestablished; selected passages only.'},
 {'id':'O3','status':'resolved','pdf_pages':[5],'basis':'0<xi<1 explicitly stated; both eigenvalue classes positive; targeted exact regularization limit passes.'},
 {'id':'O4','status':'resolved','pdf_pages':[5,6],'basis':'Finite convex combination, nonnegative normalizedq_j and removal of zero-weight atoms explicit; r=0 remains well-defined.'},
 {'id':'O5','status':'resolved','optional_in998':True,'pdf_pages':[5],'basis':'Ordinarylambda² and1/4 versus3/8 comparison added; checked against Hiai–Ruskai Theorem6.1 for T=lambdaI.'}]
criteria={
 'correctness_confidence':{'stars_1_5':4,'basis':'Current complete proof inspection, corrected hypotheses and public exact replay reveal no central error; no formal or attested independent verification.'},
 'rigor_and_completeness':{'stars_1_5':4,'basis':'Declared finite-reference quantifiers and ordered boundary limits are covered; precision objections resolved. Compact proof and certificates remain a model-inspected argument, not formal verification.'},
 'novelty_relative_to_sources_checked':{'stars_1_5':3,'basis':'Specific exact coefficient and sharp family not identified in checked passages; tools are established and search remains directed and partial.'},
 'significance_if_claims_hold':{'stars_1_5':3,'basis':'Clear specialized reference-assisted result; broader operational and entropy implications not demonstrated.'},
 'reproducibility_or_independent_inspectability':{'stars_1_5':4,'basis':'Pinned public code, manifest and dependencies now available and replayed; inspectable evidence without an independently certified campaign or formal whole-corpus validation.'}}
save('verdict1006.json',{
 'review':'1006','utc':NOW,'scope':'One final full assessment of exact corrected PDF1005 only.',
 'input_hashes':input_hashes,'pdf_pages':8,
 'scientific_importance_airr_0_10':4.3,'overall_millennium_0_10':4.4,'technical_quality_0_10':8.6,
 'overall_public_whole_stars':4,'overall_public_label':'Strong',
 'score_bases':{
  'scientific_importance_airr':'The exact constrained complete coefficient and constructive sharpness remain a clear specialized contribution; corrected access and wording do not enlarge demonstrated consequence.',
  'overall_millennium':'Strong follows from current full proof inspection, verified corrections and public reproduction; limited scope and provisional novelty remain.',
  'technical_quality':'Universal harmonic proof, explicit lower family, ordered faithful regularization and rational evidence remain sound under corrected hypotheses; no formal or attested independent verification.',
  'same_numbers_as998':'Maintained after reading exact1005 and checking actual changes. The mathematical contribution, proof burden and evidence scope are materially unchanged. Corrections remove the minor-revision condition without automatically changing research importance or scale category.',
  'no_automatic_transfer':True,'no_averaging_of_axes_or_criteria':True,'not_probabilities':True,'not_school_grades':True,'no_target_grade':True},
 'five_criteria':criteria,'recommendation':'recommend_publication_with_declared_scope',
 'recommendation_spanish':'Recomiendo publicar el PDF1005 dentro de su alcance declarado; O1–O5 resueltas, sin nuevas correcciones condicionantes.',
 'recommendation_is_editorial_acceptance':False,'publication_performed':False,
 'objections':objections,'new_objections':[],
 'main_conclusions':{
  'universal_Petz_upper':'No invalidating error found; faithful states, nonaffine operator-convex generators, positive weights and equal twirl images as stated.',
  'qubit_exact':'SLD, minimal chi-square and triangular complete equal-reference suprema equal3lambda²/(1+2lambda); qutrit reference sufficient to approach.',
  'uniform_sharpness':'Optimal bound over the generator family, not equality for every generator.',
  'scalar_barrier':'Applies to specified common convex representation and single scalar centering only.',
  'not_solved':['relative-entropy complete coefficient','mutual-information coefficient','minimal sufficient reference dimension','general higher-dimensional sharpness','operational applications']},
 'evidence':{'frozen_payloads_verified_C_D':21,'local_artifacts_unchanged_from998':10,
  'public_commit':public['commit'],'public_manifest_sha256':public['manifest_fetch']['sha256'],
  'public_selected_files_checked':13,'public_files_all_match_manifest':True,
  'public_math_environment_files_LF_equivalent_to_local':9,
  'public_calculation_files_with_original_hash_bridge':8,
  'public_readme_is_different_synthesis':True,
  'public_replay_runs':replay['runs'],'public_outputs_semantically_and_LF_equal':True,
  'symbolic_identities':9,'faithful_pairs_75_digits':9,'rational_certificates':2,
  'triangular_ratio_lower':'0.3489139697972439575435340','variance_ratio_lower':'2.993112832240518731193607',
  'own_focused_exact_controls':4,'own_focused_control_failures':0,
  'prior998_controls_not_rerun_as_new_evidence':True,
  'later_extensions_not_evaluated':True},
 'uncertainties':['Worldwide originality not certified by directed partial source reading.','No formal proof verification or independent human peer review is established.','Context952/998 is reused and filesystem shared; independence is unattested.','Finite diagnostics do not replace universal analytic arguments.'],
 'prior_review':{'id':'998','subject':'earlier exact PDF995','report_sha256':inp['prior_report_sha256'],'intact':True,'not_another_vote_on1005':True,'no_automatic_score_transfer':True},
 'reports':{'review':'REVIEW1006.txt','readings':'READINGS1006.json','provenance':'PROVENANCE1006.json','incidents':'INCIDENTS1006.json','manifest':'MANIFEST1006.json','copy_receipt':'COPY-RECEIPT1006.json'}})

save('PROVENANCE1006.json',{
 'review':'1006','utc':NOW,'input_hashes':input_hashes,
 'requested_configuration':{'model':'GPT-6 Astra','effort':'xhigh'},
 'effective_identity_attested':False,'effective_effort_attested':False,
 'context_reused':['952','998'],'filesystem_shared':True,'independence_attested':False,'isolation_attested':False,
 'prior998_report_dependency':'Used to identify O1–O5 and declared prior reading/control scope; current full PDF independently re-inspected within same reused context, not independent review.',
 'audit988':'Availability and original/public hashes of AUDIT988.txt, INCIDENTS988.txt and verdict988.json checked in memory only; bodies not read for scientific conclusions.',
 'extensions997_1003':'Not read or evaluated; filenames and hashes seen in public inventory only.',
 'other_chats_opened':False,'subagents_spawned':False,'forbidden_mutators_executed':False,
 'input_or_other_work_modified':False,'published_or_deposited':False,
 'public_downloads_anonymous':True,'public_replay_only_in_review_owned_copy':True,
 'runtime':replay['runtime'],
 'pdf_skill':'C:/Users/lluis/.codex/plugins/cache/openai-primary-runtime/pdf/26.1020.11348/skills/pdf/SKILL.md; applied from earlier reading in same conversation.',
 'storage':{'work':str(ROOT),'archive':'D:/Proyectos/airr-investigacion/2026-10-27_sharp1006-review','copy_receipt':'COPY-RECEIPT1006.json'}})
save('INCIDENTS1006.json',{
 'utc':NOW,'scientific_control_failures':0,'hash_mismatches':0,'public_verifier_failures':0,
 'incidents':[
  {'id':'I1','stage':'initial file read','error':'CHANGES1005.txt does not exist.','resolution':'Used CHANGES1005.json identified in input and manifest.','effect':'Read-only error, no scientific effect; INITIAL-INCIDENT1006.json retained.'},
  {'id':'I2','stage':'first PDF extraction','error':'TypeError: Object of type Rect is not JSON serializable','resolution':'Prepared explicit Rect serialization.','retained':'Empty PDF-TEXT1006.json retained; failure recorded here.'},
  {'id':'I3','stage':'second PDF extraction','error':'ImportError: DLL load failed while importing _extra; Windows reported paging file too small to complete operation.','resolution':'Kept failed inspect_pdf1006.py and used pure-Python pypdf fallback successfully.','effect':'Eight Poppler renders were already complete; text and actual URI verified with fallback.'},
  {'id':'I4','stage':'public file comparison','type':'expected_difference_not_failure','description':'README is a distinct public synthesis; requirements and JSON outputs use LF rather than local CRLF. All selected public hashes match manifest; nine math/environment files match normalized local content.'}
 ],
 'retained_adverse_history':'998 originals remain intact. This final review did not rerun historical optimizers or erase their failures.',
 'restarts_to_favor_score':0,'mathematical_runs_restarted':0,'notes':'PDF-tool fallback is an explicitly retained operational repair, not a restarted scientific search.'})
print('Wrote full verdict, provenance, readings and incidents for exact1005.')
