from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).parent
def write(name,data):
 (P/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def hashfile(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
verdict={
 'audit':'1058','date':'2026-10-27','scope':'Technical incremental audit of1057; no manuscript evaluation, score, vote or editorial recommendation.',
 'requested_configuration':'GPT-6 Astra xhigh','effective_model_effort_attested':False,'independence_attested':False,'shared_context_and_filesystem':True,'prior_involvement':True,
 'input_manifest_sha256':'9df12df851c66114f0e295cac751f87c1d19d8132f2e85cbdebf4a3335df1d31',
 'components':[
  {'id':'classical_global','verdict':'valid_with_explicit_domain_and_boundary_clarifications','formula':'lambda^2/(lambda+2*(1-lambda)/n)','domain':'integer n>=2; -1/(n-1)<=lambda<=1; fixed nonaffine operator-convex f on(0,infinity), f(1)=0; global supremum over both probability vectors,0<D_f<infinity','proof':'Fisher restriction to sum-zero tangents; dominant-coordinate Cauchy argument; positive resolvents including u=0 and quadratic endpoint; common uniform regularization; local two-ray lower.','novel_classical_theorem_claim_supported':False},
  {'id':'endpoints','verdict':'valid','facts':['n=1 excluded','h=lambda+2c positive throughout range','n=2: h=1, negative endpoint is a permutation','lambda=0:0;lambda=1:1','No singularity at n=2,lambda=-1']},
  {'id':'each_operator_convex_f','verdict':'valid_and_prior_global_equivalence','prior':'Makur-Zheng1510.01844v4 Proposition6, definition and selected proof read','limit':'Each fixed f and supremum; no common finite saturator, no extension to every convex f.'},
  {'id':'Bell_reduction','verdict':'valid','domain':'Pairs diagonal in one common orthonormal maximally entangled basis of A_d R_d; n=d^2; shared marginalI/d; full local depolarizing CP range','exclusions':['All commuting quantum pairs','All equal-reference states','Independently chosen incompatible bases','Fixed uniform source distribution']},
  {'id':'positive_phase_d3','verdict':'certified_dependent_on1051_1054','parameters':{'d':3,'lambda':'1/2','theta':'99/100','e':'1/10^30','phase':'pi'},'ratio_approx':'0.41495890226843458493','benchmark':'9/22','gap_approx':'0.00586799317752549402','input_D_approx':'2.84915094230353e-58','condition_approx':'5.95e62','actual_order':'223/25','certificate':'INTEGER_INTERVAL1058.json'},
  {'id':'positive_phase_d4','verdict':'certified_dependent_on1051_1054','parameters':{'d':4,'lambda':'1/2','theta':'99/100','e':'1/10^30','phase':'pi'},'ratio_approx':'0.44684466269731793122','benchmark':'4/9','gap_approx':'0.00240021825287348678','input_D_approx':'1.91171103788928e-58','condition_approx':'1.189e63','actual_order':'317/20','certificate':'INTEGER_INTERVAL1058.json'},
  {'id':'all_noise_phase_consequence','verdict':'valid_conditional_on_audited1051_geometry','statement':'For d>=3 and each fixed physical lambda other than0,1, known local-phase lower C_{d(d-1)} exceeds exact Bell C_{d^2/2}. Finite separating parameters exist by limits.','limits':['No single finite parameter set uniform inlambda','Only two positive phase points checked here','No lower for every quantum Petz f','No general quantum upper or unrestricted optimum','No MI,capacity,experimental robustness or absolute Fisher optimum']},
  {'id':'Lee_Makur_coverage','verdict':'specific_formula_coverage_unresolved_primary_text_inaccessible','doi':'10.1109/ALLERTON63246.2024.10735307','read':'Author publication metadata and author conference abstract only; no formula,hypotheses or proof.','access':'IEEE418; DOI unavailable in web tool; no bypass,purchase or contact.','consequence':'Do not claim classical formula novelty or priority; close possibly covering antecedent remains.'}
 ],
 'controls':{'replay':'192 rational Fisher controls and two intervals; all fields match exceptutc','own_whole_tangent_forms':90,'own_oriented_resolvent_pairs':60,'own_lower_checks':16,'own_full_Bell_matrices':4,'own_positive_phase_integer_intervals':2,'universal_proof':'analytic,not finite controls'},
 'actual_counterexample_to_scoped_claim_found':False,
 'scope_falsifiers':['TV is convex but outside operator-convex class:1/2>3/10','Dropping sum-zero:6/17>3/10','Global coefficient cannot be replaced by fixed-uniform value:441/1082>1/4'],
 'preserved_failure':'Auxiliary own Bell script initially mixed Python float with SymPy Rational; structural equality failed at lambda=0 despite zero difference. Initial script, traceback and diagnosis retained; correction only to rational types.',
 'ready_claims':['Scoped global classical formula withn>=2 and boundary extension','Exact common-ME-basis benchmark over fullCP range','Two certified finite positive-phase separations with1051/1054 dependency','Fixed-lambda asymptotic separation and finite existence for d>=3,lambda!=0,1'],
 'not_ready_or_unsupported':['Classical novelty or worldwide priority','Claim to have read Lee-Makur formula or proved its precise coverage','All commuting quantum pairs bound','Simultaneous finite sharpness for allf','Quantum all-Petz phase lower','Quantum general upper C_P or unrestricted optimum','MI,capacity,experimental robustness or maximal absolute QFI'],
 'report':'AUDIT1058.txt','full_limits':'AUDIT1058.txt sections1,4,5,7,8,9'
}
write('verdict1058.json',verdict)
prior=Path(r'C:\Trabajo\airr\2026-10-27_local-phase1054-audit')
write('PROVENANCE1058.json',{
 'created_utc':now,'task':'1058 incremental audit','requested_configuration':'GPT-6 Astra xhigh','effective_configuration_attested':False,'independence_or_isolation_attested':False,'shared_filesystem':True,'context_reused':['1018','1025','1044','1054'],'previous_involvement':True,
 'authorization':'Current delegated audit of sealed 1057 only; one scientific review active; no new agents/chats.','global_instructions':'Global AGENTS and D:\\LEEME.md read in reused 1054 context; work C, archive D; task explicitly requires identical retained C/D copy.',
 'input_integrity':['INPUT_VERIFIED1058.json','INPUT_FINAL1058.json'],'manifest_hash_externally_supplied_at_start':False,'unlisted_input_C_only':'seal1057.py hashed but not executed; sealed five files C/D identical, whole folder inventories differ.',
 'immutable_previous_audit':{name:hashfile(prior/name) for name in ['AUDIT1054.txt','verdict1054.json','MANIFEST1054.json']},
 'code_reuse':{'integer_arithmetic_source':str(prior/'integer_intervals1054.py'),'sha256':hashfile(prior/'integer_intervals1054.py'),'scope':'Reused own interval primitives; new two-case driver. No claim of independent code or geometry.','primary_helper':'Copied own1054 primary retrieval helper; in-memory foreigndocumentonly.'},
 'excluded':['1047 manuscript','1048 manuscript review','1060 draft mentioned afterstart','Git','rootstate','publication','authorcontact','new agents or chats','re-audit of full1051phasecampaign'],
 'foreign_material_policy':'Only metadata, URL, version, hash and own synthesis retained. PDFs and webpage bodies read in memory; no foreign corpus written. User-supplied checker copied only to own replay directory.',
 'audit_C':str(P),'archive_D':r'D:\Proyectos\airr-investigacion\2026-10-27_bell-allnoise1058-audit'
})
write('READINGS1058.json',{
 'scope':'Directed primary checks, not exhaustive literature review; distinguish metadata, abstract, statement, selected proof.',
 'records':[
  {'source':'Makur-Zheng','url':'https://arxiv.org/pdf/1510.01844v4','version':'1510.01844v4','sha256':'a971a7a1af7322afa9648ccd9f62ec86c3a663a65763388722363bca5efeaa47','bytes':1128813,'pages':37,'read_levels':['abstract','Definition5','Proposition6 statement','Theorem12 statement','selectedproof inclLemma22 and Proposition6'],'PDF_pages_read':[11,12,18,28,29,30],'PDF_pages_reread_after_truncation':[29,30],'whole_paper_audited':False,'summary_location':'AUDIT1058.txt section8','coverage':'Global operator-convex f equivalence; specific symmetric-channel formula not attributed tothispaper.'},
  {'source':'Lee-Makur2024','title':'Contraction Coefficients of Product Symmetric Channels','doi':'10.1109/ALLERTON63246.2024.10735307','url':'https://doi.org/10.1109/ALLERTON63246.2024.10735307','read_levels':['authorpublicationmetadata','authorconferenceabstract'],'formula_read':False,'full_hypotheses_read':False,'proof_read':False,'access_error':'IEEE418; DOI unavailable throughwebtool','public_alternatives_checked':['https://www.cs.purdue.edu/homes/amakur/publications.html','https://dongmin.dev/','https://easychair.org/smart-program/2024Allerton/2024-09-25.html','https://easychair.org/smart-program/2024Allerton/slides.html'],'page_hash_receipts':'PRIMARY_PAGES1058.json','specific_formula_and_negative_range_coverage':'unresolved','summary_location':'AUDIT1058.txt section8'},
  {'source':'Makur-Polyanskiy2018','url':'https://people.lids.mit.edu/yp/homepage/data/symch_dom.pdf','origin':'InheritedREADINGS1057','fresh_body_read1058':False,'relied_on_for_exact_coverage':False},
  {'source':'1057 user package','read_complete_texts':['PROOF1057.txt','check1057.py','READINGS1057.json'],'CHECK1057':'Fully parsed and replayed; not manual reading of every digit.','hash_receipts':'INPUT_VERIFIED1058.json'},
  {'source':'Own1054audit','status':'Reusedauditcontextandimmutableartifacthashes;notnewauditof1051or1052','dependencies':['localphasegeometry','genericphase/BKMcounterexample','prioradversediagnostics'],'hash_receipt':'PROVENANCE1058.json'}
 ],'foreign_corpus_saved':False,'priority_claim':False,'exhaustive_search_claim':False
})
write('INCIDENTS1058.json',{
 'incidents':[
  {'id':'own_bell_type_failure','kind':'control_implementation_failure','preserved':['bell_controls1058_initial.py','BELL_FAILURE1058.json','BELL_FAILURE_DIAGNOSIS1058.json'],'cause':'Python int lambda=0 yielded float 0.25; structural SymPy comparison against Rational failed; difference zero.','repair':'Use SymPy Rational for lambda=0 and 1; no mathematical parameter change.','result':'Four corrected cases pass BELL_CONTROLS1058.json'},
  {'id':'source_access','kind':'bibliographic_limitation','facts':['DOI open unavailable','IEEE 418','Public slides index contains only two other presentations'],'response':'No purchase, bypass or contact; formula and range unread; priority unsupported.'},
  {'id':'truncated_primary_output','kind':'tool_output_limit','facts':'Combined PDF read truncated tail; pages 29 and 30 reread completely.','receipts':['PRIMARY_1510.01844v4_201459489705.json','PRIMARY_1510.01844v4_201524161370.json']},
  {'id':'retired_parent_alert','kind':'retracted_warning','facts':'Parent initially suggested binary negative endpoint denominator issue and corrected it in the same message; own h=1 confirms no issue.','n1':'Must explicitly exclude.'},
  {'id':'unlisted_input_sealer','kind':'inventory_qualification','facts':'seal1057.py only in C outside MANIFEST1057; hash recorded; not executed; not changed.'},
  {'id':'replay_timestamp','kind':'expected_output_difference','facts':'All CHECK1057 fields identical except utc; no byte-identical output claim.','receipt':'REPLAY1058.json'},
  {'id':'old_adverse_evidence','kind':'preserved_dependency','facts':['1051 initial wrong B^-1 sigma eigenvector check and UTF8 incident remain in sealed 1054','Prior 14 of 24 adverse diagnostics remain in 1054','Prior 3x3 generic finite phase/BKM equality counterexample remains in 1054'],'fresh_reaudit':False,'scope':'No erasures or transfer of generic phase equality to this family.'},
  {'id':'later1060notice','kind':'out_of_scope_input','facts':'Parent mentioned new draft 1060 after start; not read or evaluated; input 1057 unchanged.'}
 ],'mathematical_failure_of_scoped1057_claim_found':False,'scope_counterexamples':'CONTROLS1058.json','all_failure_artifacts_preserved':True
})
write('CONTROL_INDEX1058.json',{
 'universal_reasoning':'AUDIT1058.txt sections 2-5; finite controls are not a universal proof.',
 'runs':[
  {'script':'verify1058.py','outputs':['INPUT_VERIFIED1058.json','INPUT_FINAL1058.json'],'purpose':'Input manifest hash, all payloads, C/D identity, extras and final immutability'},
  {'script':'replay1058.py','outputs':['REPLAY1058.json','replay/CHECK1057.json','replay/stdout.txt','replay/stderr.txt'],'purpose':'Unmodified provided checker in own folder; 192 Fisher controls and two intervals; compare except utc'},
  {'script':'controls1058.py','outputs':['CONTROLS1058.json'],'purpose':'General algebra; 90 whole tangent forms, 60 oriented resolvents, 16 lower checks, three scope falsifiers'},
  {'script':'bell_controls1058.py','outputs':['BELL_CONTROLS1058.json'],'purpose':'Four rational full ambient Bell marginal/channel identities','failure_preserved':['bell_controls1058_initial.py','BELL_FAILURE1058.json','BELL_FAILURE_DIAGNOSIS1058.json']},
  {'script':'integer_intervals1058.py','outputs':['INTEGER_INTERVAL1058.json'],'purpose':'Only two 1057 positive phase points; 768 bit integer intervals, 400 term log tail; input/output/conditioning; original binary containment'},
  {'script':'primary1058.py','outputs':['PRIMARY_1510.01844v4_201447834727.json','PRIMARY_1510.01844v4_201459489705.json','PRIMARY_1510.01844v4_201524161370.json'],'purpose':'ForeignPDFinmemoryonly;hashandreadreceipts'},
  {'script':'primary_pages1058.py','outputs':['PRIMARY_PAGES1058.json'],'purpose':'Publicprimarypagehashesandaccessreceipts;noforeignbody'}
 ],'interval_arithmetic':{'grid':'2^-768','log':'range reduction;2atanhseries;400terms;tail<=4/[3*(801)*2^800]','square_root':'integerisqrtoutward','small_eigenvalue':'det/largest','endpoint_arithmetic':'integersonly;decimaldisplaynotcertificate'}
})
print('Wrote verdict,provenance,readings,incidents and controlindex.')
