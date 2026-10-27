"""Write review998 metadata. New files only; no mutation of frozen inputs."""
from pathlib import Path
import datetime, json

ROOT=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name, data):
    with (ROOT/name).open('x',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
        f.write('\n')

hashes={
 'INPUT998.json':'1f2f99491608f419d3684fdefc5531a884789a6137973e27c2730371912f5514',
 'main.pdf':'37926f59287d95e7eb2c005713504d7339e1142a170f70ba1f8cb2734caf7db3',
 'main.tex':'4f8abcd76386c190c06ed54c198823ce3f0a654ce6d6b411325c46893e14f4d2',
 'MANIFEST995.json':'b1f7779dddc90a7129f9cd2099ec8a64b16eb861032a96301b78abc2a1f5e220',
 'RUBRIC998.txt':'3b9a30f541ff57e69cd02b73dac706358d24d5244f3a0ecf94050c3ecfe4ab5b'}

provenance={
 'review':'998','utc_metadata_written':NOW,
 'scope':'One full manuscript assessment of the exact frozen seven-page PDF995; no assessment of later extensions.',
 'requested_configuration':{'model':'GPT-6 Astra','reasoning_effort':'xhigh'},
 'effective_model_identity_attested':False,'effective_effort_attested':False,
 'reused_conversation_context':'agent952','shared_filesystem':True,
 'independence_attested':False,'isolation_attested':False,
 'no_target_grade':True,'prior_scores_transferred':False,
 'audit988_consulted':False,
 'audit988_metadata_only':'Existence and hashes disclosed in assignment and INPUT998; not scientific evidence used here.',
 'prior952':'Context reused; earlier component audit provides no proof or score for995.',
 'delegated_subagents':False,'other_chats_opened':False,
 'input_hashes':hashes,
 'frozen_payloads_verified_initially':40,
 'full_manuscript_read':{'pdf_pages':7,'all_page_images_inspected':True,'all_tex_read':True},
 'artifact_scripts_read':['symbolic993.py','verify993.py','verify-certificates991.py'],
 'artifact_scripts_executed_only_in_own_copy':['symbolic993.py','verify993.py','verify-certificates991.py'],
 'historical_records_read':['research-provenance/INCIDENTS991.json','research-provenance/INCIDENTS993.json','research-provenance/LADDER-OPT993.json','research-provenance/NOTE991.txt'],
 'not_claimed':'No scientific audit of every historical payload, no optimizer replay, no complete proof audit of external papers.',
 'forbidden_mutators_executed':False,
 'input_or_manuscript_modified':False,'publication_or_deposit':False,
 'late_lead':{'id':'2505.15281v3','url':'https://arxiv.org/abs/2505.15281v3','received':'Coordinator message after review began; exact receipt time not separately logged.','part_of_frozen_input':False,'included_as_separate_bibliographic_observation':True},
 'runtime':{'python':'3.12.6','sympy':'1.14.0','mpmath':'1.3.0'},
 'skills':[{'name':'pdf:pdf','path':'C:/Users/lluis/.codex/plugins/cache/openai-primary-runtime/pdf/26.1020.11348/skills/pdf/SKILL.md','application':'Read, render and inspect exact PDF copy.'}],
 'storage':{'work':'C:/Trabajo/airr/2026-10-27_sharp998-review','archive':'D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review','copy_status':'See COPY-RECEIPT998.json after finalization.'}}
save('PROVENANCE998.json',provenance)

readings=[
 {'key':'S1','id':'1508.03551v1','authors':'Hiai–Ruskai','title':'Contraction coefficients for noisy quantum channels','level':'Abstract, selected statements, representation formulas and surrounding derivation; not complete proof audit.','locations':['Proposition2.1','equations12–13','Theorem6.1'],'use':'Established representation and ordinary qubit comparison.','full_paper_read':False},
 {'key':'S2','id':'1904.06562v2','authors':'Cao–Lu','title':'Tensorization of the strong data processing inequality for quantum chi-square divergences','level':'Abstract, selected theorem and example; not full proofs.','locations':['Theorem1','Section5.2'],'use':'Contrast fixed product-base tensorization with manuscript scope.','full_paper_read':False},
 {'key':'S3','id':'2503.22823v3','authors':'George–Hirche–Nuradha–Wilde','title':'Quantum Doeblin Coefficients: Interpretations and Applications','level':'Abstract, definitions, selected statements and Proposition30 proof passage.','locations':['Definition11, equation6.2','Proposition30','Corollary7, equation6.29'],'use':'Earlier equal-reference definition; divergence-family distinction.','full_paper_read':False},
 {'key':'S4','id':'2411.19890v3','authors':'Belzig–Gao–Smith–Wu','title':'Reverse-type Data Processing Inequality','version_date_verified':'2025-10-08','level':'Abstract, introduction and selected discussion; not full theorem proofs.','locations':['ordinary coefficient definition in introduction','quantum-reference discussion in Section2 and conclusion'],'use':'Separate ordinary comparison from quantum-reference mutual information.','full_paper_read':False},
 {'key':'S5','id':'2608.27171v1','authors':'Hirche–George–Nuradha–Wilde','title':'Conditional contraction coefficients and their applications to quantum networks','level':'Abstract, definitions, selected examples and distinctions; not all proofs.','locations':['Definitions1–2, equations2.12–2.14','Sections3.3 and3.7'],'use':'Check optimization domains and divergence families.','full_paper_read':False},
 {'key':'S6','id':'2608.19685v1','authors':'Gao–Zhao','title':'Tight Entropy Contraction of Generalized Quantum Depolarization','level':'Abstract, introduction and theorem statement; no full proof audit.','locations':['Theorem1.2','conditional-expectation context in introduction'],'use':'Distinguish contraction toward conditional expectation.','full_paper_read':False},
 {'key':'S7','id':'2505.15281v3','authors':'George–Tomamichel','title':'A Unified Approach to Quantum Contraction and Correlation Coefficients','version_date_verified':'2026-03-29','level':'Abstract, selected definitions and theorem statements, displayed proof passages and algorithm; not full proofs or complete paper.','locations':['equations127–128','Theorems93–94 and proof passages','Theorem105, Algorithm1 and correctness proof passage'],'use':'Late lead on fixed-base and ordinary optimized coefficients; inspectability and priority comparison.','full_paper_read':False,'late_lead':True,'part_of_frozen_input':False}
]
source_hashes=json.loads((ROOT/'SOURCE-HASHES998-run01.json').read_text(encoding='utf-8'))
index={row['id']:row for row in source_hashes['sources']}
for entry in readings:
    entry['url']='https://arxiv.org/abs/'+entry['id']
    entry['pdf_url']=index[entry['id']]['url']
    entry['pdf_sha256']=index[entry['id']].get('sha256')
    entry['pdf_pages']=index[entry['id']].get('pages')
    entry['full_external_text_persisted']=False
save('READINGS998.json',{
 'utc':NOW,'sources':readings,
 'primary_sources_only_for_technical_comparison':True,
 'search_scope':'Directed checks of the six manuscript references and one later supplied primary source; targeted keyword searches. No exhaustive forward/backward citation or worldwide-priority search.',
 'search_results_not_evidence':'Broad searches returned irrelevant medical/noisy results; these were ignored. An ancilla-free quantum-Fisher metrology lead (arXiv2402.18765) was seen as a search snippet only, not read as a paper and not used as priority evidence.',
 'reading_vs_retrieval':'Downloading all bytes to hash a PDF does not mean reading every page or verifying every proof.',
 'corpus_policy':'Version-pinned PDFs hashed in memory only; persistent dossier contains own synthesis, URLs, versions, hashes and own controls.'})

objections=[
 {'id':'O1','location':'PDF page6, finite certificates','severity':'minor_required','topic':'Supplement availability','finding':'PDF lacks stable locator/index linking the accompanying evidence to exact scripts and certificates; local package was reproducible.','requested_change':'Add stable supplement access, version/manifest and minimal replay instructions.','invalidates_central_theorem':False},
 {'id':'O2','location':'PDF page7, prior work','severity':'minor_required','topic':'Late primary-source comparison','finding':'George–Tomamichel2505.15281v3 should be explicitly contrasted; no duplication established by selected passages.','requested_change':'Distinguish fixed-base, ordinary optimized and constrained complete equal-reference coefficients before asserting priority.','invalidates_central_theorem':False,'lead_outside_frozen_input':True},
 {'id':'O3','location':'PDF page5, Theorem4 faithful regularization','severity':'minor_required','topic':'Range of xi','finding':'xi>0 alone includes nonstates: support eigenvalue is1/2−xi/3. The xi→0 argument remains valid.','requested_change':'State0<xi<1 or xi sufficiently small.','invalidates_central_theorem':False},
 {'id':'O4','location':'PDF page5, Proposition6','severity':'minor_required','topic':'Convex-representation assumptions','finding':'Positivity of q_j, normalization and finite support are implicit but needed by proof.','requested_change':'Stateq_j≥0, sumq_j=1, finite convex representation and omit zero-weight atoms.','invalidates_central_theorem':False},
 {'id':'O5','location':'PDF page5, ordinary comparison','severity':'optional','topic':'Quantitative exposition','finding':'Explicit ordinarylambda² comparison would make the reference effect easier to assess.','requested_change':'Write1/4 versus3/8 atlambda=1/2 or general comparison.','invalidates_central_theorem':False}]
criteria={
 'correctness_confidence':{'stars_1_5':4,'basis':'Central proofs checked, exact replay and own controls agree. Minor hypothesis precision remains; no formal or attested independent verification.'},
 'rigor_and_completeness':{'stars_1_5':4,'basis':'All finite-reference quantifiers, singular-kernel handling and ordered limits are supplied. Clarify regularization interval and convex weights.'},
 'novelty_relative_to_sources_checked':{'stars_1_5':3,'basis':'Exact constrained complete value and ladder not identified in selected primary passages. Machinery is established; no worldwide-priority certification.'},
 'significance_if_claims_hold':{'stars_1_5':3,'basis':'Clear specialized exact result and reference effect; broader operational, entropy and tensorization consequences not demonstrated.'},
 'reproducibility_or_independent_inspectability':{'stars_1_5':4,'basis':'Analytic proof, replayed scripts and rational certificates are inspectable. Public supplement locator missing; inspectability is not an independence claim.'}}
verdict={
 'review':'998','manuscript':'exact PDF995','utc':NOW,'input_hashes':hashes,
 'scientific_importance_airr_0_10':4.3,
 'overall_millennium_0_10':4.4,
 'technical_quality_0_10':8.6,
 'overall_public_whole_stars':4,'overall_public_label':'Strong',
 'score_bases':{
  'scientific_importance_airr':'Exact specialized complete coefficient and constructive sharpness have clear research value; wider consequences and world priority remain unestablished.',
  'overall_millennium':'A clear technically serious contribution, with bounded scope and provisional novelty. It supports Strong on the supplied high-ceiling scale, without evidence for exceptional or field-shaping impact.',
  'technical_quality':'Correctly structured universal upper, explicit sharp family, ordered faithful limits and rational certificates; small statement and availability issues remain.',
  'axes':'Importance, overall research assessment and technical quality are distinct judgments; technical quality is not itself a Millennium rating.',
  'not_probabilities':True,'not_school_grades':True,'no_implicit_or_explicit_average_of_criteria':True,
  'no_target_grade':True,'no_prior_grade_transfer':True,'decimal_scores_not_statistical_precision':True},
 'five_criteria':criteria,
 'recommendation':'minor_revision_before_publication',
 'recommendation_spanish':'Revisión menor antes de publicación: atenderO1–O4; O5 opcional.',
 'central_findings':{
  'harmonic_upper_all_nonaffine_operator_convex_Petz_generators':'No invalidating error found under faithful-state, equal-twirl-image and positive-weight hypotheses.',
  'qubit_exact_SLD_min_chi_square_triangular':'No invalidating error found; exact value3lambda²/(1+2lambda), qutrit reference sufficient to approach.',
  'uniform_generator_sharpness':'Valid uniform-family statement; not equality for each Petz generator.',
  'scalar_method_barrier':'Valid for specified induced common convex representation and single scalar cancellation.',
  'relative_entropy_or_MI_coefficient':'Not solved by exact995 and not inferred here.'},
 'objections':objections,
 'reproduction':{
  'supplied_scripts':3,'supplied_scripts_passed':3,'artifact_files_byte_identical_after_replay':10,
  'symbolic_family_identities':9,'supplied_faithful_pairs_75_digits':9,
  'rational_certificates':2,
  'triangular_certificate_ratio_lower':'0.3489139697972439575435340',
  'variance_certificate_ratio_lower':'2.993112832240518731193607',
  'own_control_groups':4,'own_control_groups_passed':4,
  'own_exact_resolvent_endpoint_cases':15,
  'own_full_spectral_pair_ratio':'0.373355055494860694377237836318418848646034850696708169935828351344680929755',
  'finite_tests_are_not_universal_proof':True,
  'optimizer_runs_in998':0,'own_control_failures':0,'restarts_to_favor_result':0},
 'uncertainties':[
  'Directed partial primary-source reading cannot certify worldwide originality.',
  'No independent human review or formal proof verification is established.',
  'Reused context and shared filesystem preclude an independence attestation.',
  'The true relative-entropy and mutual-information complete coefficients are not determined here.',
  'Minimum sufficient reference dimension and sharpness in dimensions greater than2 are not established by this paper.',
  'Finite controls do not extend scope beyond the analytic theorem.'
 ],
 'provenance':{'effective_identity_and_effort_unattested':True,'reused_context952':True,'shared_filesystem':True,'audit988_consulted':False,'late_lead_separate_from_frozen_input':True},
 'reports':{'full_review':'REVIEW998.txt','readings':'READINGS998.json','provenance':'PROVENANCE998.json','incidents':'INCIDENTS998.json','initial_integrity':'INPUT-VERIFIED998.json','closing_integrity':'CLOSING-VERIFIED998.json','reproduction':'REPRODUCTION998.json','own_controls':'CONTROLS998.json','manifest':'MANIFEST998.json','copy_receipt':'COPY-RECEIPT998.json'}}
save('verdict998.json',verdict)

save('INCIDENTS998.json',{
 'utc':NOW,
 'initial_hash_mismatches':0,'supplied_replay_failures':0,'own_controls_failures':0,
 'source_hash_fetch_failures':[x for x in source_hashes['sources'] if x['status']!='ok'],
 'search_limitation':'Initial broad keyword searches included irrelevant results. Directed primary-source inspection followed; no irrelevant result was used as evidence.',
 'adverse_findings_retained':['O1: unavailable stable supplement locator inside PDF','O2: late relevant bibliography requiring contrast','O3: xi>0 too broad as written','O4: implicit convex-weight conditions','Outside equal-reference scope, coefficient can be1'],
 'historical_incidents_read_not_reexecuted':{
  '991':['Coarse rational rounding failed to preserve variance violation.','Dense symbolic inversion was deliberately interrupted.','One inline syntax failure.','Four r3 optimizer runs reached iteration/evaluation budgets.'],
  '993':['Eight fixed-budget starts include five abnormal terminations and three successful terminations.','Fifteen local-Pauli commutator trials did not attain the harmonic target.'],
  'treatment':'Preserved originals, no universal optimum inferred; rely on explicit analytic proof and exact rational replay.'},
 'editorial_correction_during_report_draft':'Corrected displayed equation-reference range for output/ratio/gap to16–18 before sealing; no scientific result changed.',
 'mutators_package995_and_seal996_executed':False,
 'restarts_to_improve_evaluation':0,
 'original_files_preserved':True,
 'external_corpus_persisted':False})
print('Wrote PROVENANCE998.json, READINGS998.json, verdict998.json and INCIDENTS998.json')
