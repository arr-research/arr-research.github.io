from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).parent
def write(name,obj):(P/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
inputs=json.loads((P/'INPUT_VERIFIED1068.json').read_text());cert=json.loads((P/'INTERVAL1068.json').read_text())
write('verdict1068.json',{
 'audit':'1068','date':'2026-10-27','scope':'Technical incremental audit of1063,1064,1066. No manuscript evaluation, score, vote or editorial recommendation.',
 'requested_configuration':'GPT-6 Astra xhigh','effective_configuration_attested':False,'independence_attested':False,'shared_context_and_filesystem':True,'prior_involvement':True,
 'input_manifests':{r['id']:r['manifest_sha256'] for r in inputs['packages']},
 'components':[
  {'id':'1063_limits','verdict':'valid','quantifiers':'integer d>=2, d->infinity; e=1/d,theta=1-1/d,lambda=-1/(d^2-1),phasepi','limits':{'d_times_retention':'1/10','d3_inputDU_over_logd':'20','condition_over_d5':'1','d_to_3over2_trace_distance':'2'},'proof':'Exact rational expressions, separated positive roots, logarithmic ratios; no exchange of fixed-d limits.','actual_order':'d^2-d+1/d'},
  {'id':'1064_certificates','verdict':'valid_reproduced_and_enclosed','original_cases':8,'original_adverse_dimensions':[2,3,4],'own_additional_adverse_dimensions':[5,6,7],'warning':'A finite table does not prove that every integer d>=8 beats Bell.'},
  {'id':'1066_limits','verdict':'valid_for_fixed_parameters','quantifiers':'t>0 and beta>1 fixed independently of d; nu=beta+3; e^2=t/d,theta=1-d^-beta; lambda=-1/(d^2-1)','limits':{'d_times_retention':'(nu-4)/((1+t)*nu)','d2_inputDU_over_logd':'4*t*nu','condition_over_dnu':'1/t','d_times_trace_distance':'2*sqrt(t)'},'proof':'Joint rational limit in u=1/d,y=d^(1-beta), then separated roots and logarithmic exponents.','actual_order':'d^2-d^(2-beta)+d^-beta','original_interval_cases':32,'original_adverse_cases':cert['adverse_original1066'],'uniform_in_t_beta_or_target':False},
  {'id':'state_H_spectrum_order','verdict':'valid','facts':['Actual marginal diag(e^2,1,...,1)/(d-1+e^2)','H_d=diag(0,1,...,1) on A, fixed along each orbit; norm and spectral diameter1','Faithful input/output for every finite dimension and declared parameters','Exact input minimum delta*min(1,e^2)/(d*q)','Whitened pure component has rank1 and eigenvalue d^2','Exact order1+(d^2-1)*theta','Output minimum is active smaller root; output maximum=(1-p)*max(1,e^2)/(d*q) forp<0'],'limit':'Local relative to A:R, not a claim of few-body locality or implementation complexity in qubit encoding.'},
  {'id':'Umegaki_BKM_identity','verdict':'valid_for_this_family','orientation':'D(U_pi S U_pi* || S)','identity':'Dpi=4*c^2*ell(W); BKM tangent=2*c^2*ell(W)','scope':'Subnormalized plane masses cancel. Imaginary physical tangent; prior real-tangent obstruction and generic phase/BKM counterexample remain.'},
  {'id':'tradeoff_and_resources','verdict':'achievable_family_not_optimal_frontier','comparison':'t=1,beta=2 improves input scale by factor d over1063 at same leading alpha and conditioning exponent, but has larger order budget.','fixed_fraction':'Any fixed target in(0,1) is exceeded with parameter-dependent t,nu; exponent diverges as target approaches1.','noise':'lambda varies with d and tends to replacement; no fixed-noise statement.','absolute_information':'Input and output divergences vanish; retention itself is order1/d.','qubits':'For d=2^m, conditioning grows exponentially in m and information decays exponentially up to a factor m.','not_proved':['Robustness','Efficient preparation or control','Optimal frontier','Absolute Fisher advantage','Unrestricted quantum upper or optimum','MI or capacity','All quantum Petz generators']},
  {'id':'primary_coverage_and_merit','verdict':'specific_covering_theorem_not_established;priority_not_certified','judgment':'Quantitative diagonal-sequence refinement of1051/1054. Once exact plane identity is given, proof is direct rational/root/log asymptotics. Not a new physical family or autonomous large discovery.','sources':'Selected primary passages ofGao-Zhao2608.19685v1,Chapeau1904.01904v1,Frey1008.1557v1 read; hypotheses differ. Classical Makur/Lee scope inherited1058; no novelty claim.','search_exhaustive':False}
 ],
 'actual_counterexample_to_scoped_claim_found':False,
 'scope_falsifiers':[
  {'extension':'Allow t to vary with d','parameters':'t_d=1/d,beta=2','actual_dR_limit':'1/3','wrong_fixed_t_substitution_limit':'1/5','actual_input_constant':'24 at d^3/logd','wrong_constant':'20'},
  {'extension':'Use beta>1 root argument atbeta1','actual_scaled_output_trace':'2+t','wrong_trace':'1+t','actual_dR_limit':'0'},
  {'extension':'Use delta*e^2/(d*q) minimum for e^2>1','parameters':'d3,t6,beta2','actual_min':'1/108','wrong_min':'1/54'}
 ],
 'own_controls':{'full_ambient_exact_and_90digit_cases':7,'integer_interval_cases':57,'original_interval_cases_enclosed':40,'general_joint_symbolic_limits':True,'replay':'Allthree computational portions match exceptutc; creation/sealing/copying removed.'},
 'preserved_failure':'Initial ambient checker used mpmath matrix negative index eo[-1], which returned0. Initial script, traceback and diagnosis retained. Repair used eo[n-1]; no parameter changed.',
 'ready_claims':['Four1063limits','Four1066limits at fixedt,beta>1','Exact faithful states,marginal,H,order and spectral resource formulas','Relative eventual common-Bell separation at dimension-dependent negative endpoint','Certified finite cases with adverse signs','Achievable fixed-fraction tradeoff with costs explicit'],
 'not_ready_or_unsupported':['Uniform parameters or target limits','Every d>=8 from table','Fixed noise','Absolute advantage or efficient qubit resources','Experimental robustness or preparation complexity','Pareto optimality or necessary conditioning exponent','Fixed-order domination','Unrestricted quantum upper/equality','AllPetz phase sharpness','MI/capacity','1070measurement','Priority or novel classical theorem'],
 'report':'AUDIT1068.txt'
})
priorbase=Path(r'C:\Trabajo\airr');prior={}
for folder,names in [('2026-10-27_local-phase1054-audit',['AUDIT1054.txt','verdict1054.json','MANIFEST1054.json','integer_intervals1054.py']),('2026-10-27_bell-allnoise1058-audit',['AUDIT1058.txt','verdict1058.json','MANIFEST1058.json','integer_intervals1058.py'])]:
 prior[folder]={name:sha(priorbase/folder/name) for name in names}
write('PROVENANCE1068.json',{
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'task':'1068','requested_configuration':'GPT-6 Astra xhigh','effective_identity_effort_attested':False,'independence_isolation_attested':False,'shared_context_filesystem':True,'prior_involvement':True,
 'context_reused':['1018','1025','1044','1054','1058'],'one_scientific_review_active':True,'new_agents_or_chats':False,
 'instructions_read':['C:\\Users\\lluis\\.codex\\AGENTS.md','D:\\LEEME.md'],'input_records':['INPUT_VERIFIED1068.json','INPUT_FINAL1068.json'],'input_manifest_hashes_externally_supplied_at_start':False,
 'previous_immutable_artifact_hashes':prior,'replay_adaptation':'REPLAY1068.json; only computational portions, no original creation/sealing/copying executed.','arithmetic_lineage':'Own1054/1058 integer primitives, precision changed to1024bits/600terms. Same lineage as1064/1066; no independence claim.',
 'excluded':['Manuscript1060','Review1048','Later1070measurement proposal','Git','Rootstate','Publication','Contactauthors','Newagents/chats'],
 'later_steering':'Parent clarified thatlambda varies withd and gain is relative to vanishingbenchmark. Incorporated without changing inputs;1070excluded.',
 'foreign_corpus_policy':'PDF bodies read in memory only; retained URL/version/hash and own synthesis/receipts, no foreign PDFs or text caches.',
 'work_C':str(P),'archive_D':r'D:\Proyectos\airr-investigacion\2026-10-27_phase-tradeoff1068-audit'
})
write('READINGS1068.json',{
 'scope':'Directed primary comparison; not exhaustive; no priority inference from empty search.',
 'sources':[
  {'source':'Gao-Zhao','url':'https://arxiv.org/pdf/2608.19685v1','version':'2608.19685v1','sha256':'9f3000d679d6be4f7483c91cf19aa8b50942cc7b35a6202eece158023f88243c','bytes':419652,'pages':24,'PDF_pages_read':[2,3,4,16,17],'levels':['definitions','Theorem1.2 and Corollary1.3 statements','Proposition3.11 statement and proof','Lemma3.12 statement and proof','Theorem3.13 statement'],'coverage_summary':'AUDIT1068 section9','whole_paper_audited':False},
  {'source':'Chapeau-Blondeau','url':'https://arxiv.org/pdf/1904.01904v1','version':'1904.01904v1','sha256':'cb0716f339793d78ee21229de6810b8fda7ff77c9ce96915d5075ca0dbff5ae4','bytes':406878,'pages':23,'PDF_pages_read':[1,2,3,4],'levels':['abstract','introduction','phase/noise model and definitions'],'coverage_summary':'AUDIT1068 section9','whole_optimization_audited':False},
  {'source':'Frey-Collins-Gerlach','url':'https://arxiv.org/pdf/1008.1557v1','version':'1008.1557v1','sha256':'ca619694802c9d0c6e50cc0a8462bcbccc617099f943db12d3b9136270900c7d','bytes':252418,'pages':10,'PDF_pages_read':[1,2],'levels':['abstract','channel-identification model','SLD definitions and noise parameter range'],'coverage_summary':'AUDIT1068 section9','whole_paper_audited':False},
  {'source':'Makur-Zheng and Lee-Makur','status':'Inherited1058audit; no new primary retrieval1068','scope':'Classical benchmark/equivalence not novel; precise inaccessible Lee-Makur formula coverage remains unresolved.','previous_report_hash':prior['2026-10-27_bell-allnoise1058-audit']['AUDIT1058.txt']},
  {'source':'Inputs1063/1064/1066','texts_scripts':'Read completely','JSON':'Parsed and computational replay compared, not every digit manually read.','hashes':'INPUT_VERIFIED1068.json'}
 ],
 'search_queries':[
  'quantum depolarizing relative entropy contraction coefficient ancillary phase unitary dimension conditioning',
  '"relative entropy" "conditioning" "depolarizing" contraction',
  '"quantum Fisher" "depolarizing" "dimension" ancilla Chapeau1904.01904',
  '"depolarizing" "condition number" "relative entropy" site:arxiv.org',
  '"phase" "relative entropy" "contraction" "dimension" site:arxiv.org',
  '"depolarizing" "polynomial" "Fisher" "ancilla" site:arxiv.org'
 ],'search_result_limit':'Lastthree queries returned no results. Secondary hits in firstbatch were locators only; substantive comparisons use primary PDFs. This is not evidence of absence or novelty.','foreign_corpus_saved':False
})
write('INCIDENTS1068.json',{
 'incidents':[
  {'id':'ambient_negative_index','kind':'own_control_implementation_failure','preserved':['ambient1068_initial.py','AMBIENT_FAILURE1068.json','AMBIENT_FAILURE_DIAGNOSIS1068.json'],'cause':'mpmath matrix index[-1] returned0 rather than last eigenvalue; firstcase outputmax assertion failed.','repair':'Replace with index[n-1]; no mathematical parameter changed.','result':'Seven cases pass after repair.'},
  {'id':'generator_side_effects','kind':'replay_safety_adaptation','facts':'All three original scripts create and seal packages and copyC/D. Only extracted computation executed under ownfolders; modifications recorded.','receipt':'REPLAY1068.json'},
  {'id':'finite_adverses','kind':'mathematical_adverse_controls','original1064':[2,3,4],'own1063additional':[5,6,7],'original1066':cert['adverse_original1066'],'omitted_or_deleted':False},
  {'id':'quantifier_falsifiers','kind':'scope_limits','receipt':'SYMBOLIC1068.json','facts':'Moving t, beta=1 and small dimensions with e^2>1 invalidate specified extensions, not correctly scoped inputs.'},
  {'id':'later_parent_steering','kind':'scope_clarification','facts':'lambda_d varies and tends to replacement; relativebenchmarkvanishes. Later1070measurement excluded; no newinputbytes.'},
  {'id':'empty_searches','kind':'literature_limit','facts':'No identified literalcovering theorem in selected sources; empty queries do not establish novelty.'},
  {'id':'inherited_adverses','kind':'preserved_prior_context','facts':'Prior real-tangent obstruction and genericfinitephase/BKM counterexample remain in immutable1054; no re-audit or erasure.'}
 ],'actual_mathematical_counterexample_to_scoped_inputs_found':False,'prior_failures_not_erased':True
})
write('CONTROL_INDEX1068.json',{
 'universal_proof':'AUDIT1068 sections2-6 plus symbolic identities; finite controls do not prove all dimensions.',
 'runs':[
  {'script':'verify1068.py','outputs':['INPUT_VERIFIED1068.json','INPUT_FINAL1068.json'],'purpose':'Allthree manifests,payloadhashes,C/Didentity,inventory and finalimmutability'},
  {'script':'replay1068.py','outputs':['REPLAY1068.json','replay1063/CHECK1063.json','replay1064/CONTROL1064.json','replay1066/CONTROL1066.json'],'purpose':'Adapted computational replay; allfields exceptutc identical'},
  {'script':'symbolic1068.py','outputs':['SYMBOLIC1068.json'],'purpose':'Exact general expressions, joint limits and quantifierfalsifiers'},
  {'script':'ambient1068.py','outputs':['AMBIENT1068.json'],'purpose':'Seven full ambient matrices: exact marginals,characteristicpolynomials,physicalH,90digitlogarithms/BKM','failure_preserved':['ambient1068_initial.py','AMBIENT_FAILURE1068.json','AMBIENT_FAILURE_DIAGNOSIS1068.json']},
  {'script':'intervals1068.py','outputs':['INTERVAL1068.json'],'dependencies':['integer_arithmetic1068.py'],'purpose':'57 integerintervalcases;40sourceintervals contained;large dimensions,nonintegerbeta and adverses'},
  {'script':'primary1068.py','outputs':[f.name for f in sorted(P.glob('PRIMARY_*.json'))],'purpose':'In-memory primaryPDF reading and metadata receipts'}
 ],'integer_arithmetic':{'bits':1024,'log_series_terms':600,'tail_bound':'4/[3*(1201)*2^1200]','same_lineage_as1054':True,'small_eigenvalue':'det/largest','decimals':'display only'},
 'control_counts':{'ambient':7,'integer_cases':57,'original_integer_certificates_enclosed':40,'original1063diagnostics_reproduced':11,'original1064intervals_reproduced':8,'original1066intervals_reproduced':32}
})
print('Metadata written.')
