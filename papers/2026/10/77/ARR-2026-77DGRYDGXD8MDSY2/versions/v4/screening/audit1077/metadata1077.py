from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).parent
def write(n,x):(P/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
inputs=json.loads((P/'INPUT_VERIFIED1077.json').read_text());ic=json.loads((P/'INTERVAL1077.json').read_text())
write('verdict1077.json',{
 'audit':'1077','scope':'Technical audit of sealed1070/1073; no manuscript, score, vote or editorial recommendation.','requested_configuration':'GPT-6 Astra xhigh','effective_configuration_attested':False,'independence_attested':False,'shared_context_filesystem':True,'prior_involvement':True,
 'input_manifests':{r['id']:r['manifest_sha256'] for r in inputs['packages']},
 'components':[
  {'id':'exact_projector_probabilities','verdict':'valid','definition':'Pi=(hQ-Q sigma_out Q)/(h-l), zero on Q_perp','probabilities':'q0=l,p0=l+4b^2/(h-l)','complement':'1-q0,1-p0 including all ambient modes','orientation':'D(Ber(p0)||Ber(q0))','limit':'Replacing Q with full ambient identity produces an invalid effect.'},
  {'id':'asymptotic_measurement','verdict':'valid_for_fixed_t_beta','parameters':'t>0,beta>1 fixed; nu=beta+3; lambda=-1/(d^2-1)','limits':{'binary_over_quantum_output':'1','d_binary_over_quantum_input':'(beta-1)/((1+t)*(beta+3))','d3_binary_over_logd':'4*t*(beta-1)/(1+t)'},'finite_equality':False,'proof':'Rare-event Bernoulli expansion using separated roots from1068; full complement retained.'},
  {'id':'1073_ambient_controls','verdict':'valid_with_finite_scope','ambient_dimensions':[4,9,16],'replay':'Fields identical exceptutc; generator creation/sealing/copying removed.','not_claimed':'Universal asymptotics from these finite matrices.'},
  {'id':'Bell_comparison','verdict':'valid_only_with_quantum_input_denominator','scope':'All pairs diagonal in one common ME basis, any output measurement, negativeCP endpoint','not_a_claim':['New classical binary contraction coefficient','All commuting quantum pairs','General separability/NPT witness','Free postselection or changed denominator']},
  {'id':'exactness_and_alternative','verdict':'original_valid_but_exact_diagonalization_not_necessary_for_leading_limit','limiting_vector':'(sqrt(t),1)/sqrt(1+t) loses fraction whenbeta>3; limiting fractionmin(beta-1,2)/(beta-1)','own_additional_projector':'K_d onto(sqrt((d-1)*x),1)/sqrt(1+(d-1)*x), kernel at theta1','own_probabilities':'qK=delta*x/[q*(1+(d-1)*x)];pK=qK+4*theta*(d-1)*x/[(d^2-1)*q*(1+(d-1)*x)]','own_conclusion':'Same leading limits for fixedt,beta>1; no beta-dependent diagonalization needed.','provenance':'Derived during1077, not input1070/1073 or prior1068 bytes. No finite optimality claim.'},
  {'id':'uniformity','verdict':'not_uniform','falsifier':'t_d=1/d,beta2 gives binary/quantumoutput->1/2 and d*binary/quantuminput->1/6, not1 and1/5','orientation_falsifier':'Reverse Bernoulli divergence over quantum output tends0.'},
  {'id':'operational_scope','verdict':'mathematical_experiment_not_robustness_or_efficiency_theorem','costs':['Joint parameter-dependent measurement','Rare p~d^-3,q~d^-(beta+2)','Quantum input denominator requires model or certification','Input condition~d^(beta+3)/t','Dimension-polynomial costs exponential for d=2^m','lambda changes with d; absolute information and retention vanish'],'not_proved':['LOCC/local implementation','Efficient preparation or control','Fixed precision robustness','Optimal sample complexity','MI/capacity','Unrestricted quantum optimum','Noncircular entanglement witness']},
  {'id':'primary_antecedents','verdict':'DPI_measured_entropy_and_Stein_are_prior; specific_priority_unestablished','sources':'Berta-Fawzi-Tomamichel1512.02615v2 selected statements/proofs; Ogawa-Nagaoka9906090v1 selected proof; Ogawa-Hayashi0110125v1 statements; Hiai-Petz1991 abstract only.','limits':'Finite strict inequality and fixed-state many-copy limits differ from varying-dimensional single-copy ratio. No exhaustive search or priority claim.'}
 ],
 'actual_counterexample_to_scoped1070_found':False,
 'controls':{'original_intervals_reproduced_and_contained':36,'original_adverse_count':12,'own_interval_cases':57,'own_full_ambient_cases':4,'general_symbolic_identities':True},
 'original_adverse':ic['original_adverse'],
 'incidents':'UTF8 locator print failure preserved and repaired; no mathematical control failure in1077.',
 'ready_claims':['Exact supported projector and probabilities','Both limits at fixedt,beta','Strict finite binaryD<quantumD with ratio->1','Measured-output/quantum-input Bell comparison','36 certificates with12adverses','Own separated endpoint-kernel simplification with stated provenance'],
 'unsupported_claims':['Finite measured=Umegaki equality','Finite/global optimality ofPi','Necessity of exact diagonalization forleadinglimit','Uniformt/beta limits','Constant-vector replacement forbeta>3','Reversed orientation','Free block normalization','Classical denominator interchangeability','Global binary stochastic map','Efficient/robust/local measurement','Optimal samples','General entanglement witness','Fixed noise','Absolute advantage','MI/capacity','Priority or newDPI/Stein'],
 'report':'AUDIT1077.txt'
})
prior={}
for folder,files in [('2026-10-27_phase-tradeoff1068-audit',['AUDIT1068.txt','verdict1068.json','MANIFEST1068.json','integer_arithmetic1068.py']),('2026-10-27_bell-allnoise1058-audit',['AUDIT1058.txt','MANIFEST1058.json'])]:prior[folder]={f:sha(Path(r'C:\Trabajo\airr')/folder/f) for f in files}
write('PROVENANCE1077.json',{
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requested_configuration':'GPT-6 Astra xhigh','effective_identity_effort_attested':False,'independence_isolation_attested':False,'shared_context_filesystem':True,'prior_involvement':True,'one_scientific_audit_active':True,'new_agents_chats':False,
 'context_reused':['1054','1058','1068','earlier chain'],'global_instructions':'GlobalAGENTS and D:\\LEEME.md read completely in1068 context and reused.','external_input_manifest_hashes_verified':True,'input_records':['INPUT_VERIFIED1077.json','INPUT_FINAL1077.json'],'prior_immutable_hashes':prior,
 'own_new_control':'Endpoint-kernel projector K_d and exact probabilities derived within1077; not attributed to original1070/1073 or1068 inputs.','replay':'Computation extracted into own folders; no original generators/sealers run.','arithmetic':'Own1024bit primitives reused from1068, same1054 lineage; not independent implementation.',
 'later_parent_message':'Berta1512.02615v2 suggested after own retrieval began; parent had read abstract only. This audit read statements and selected proofs independently of that summary, without claiming independent reviewer status.',
 'excluded':['Manuscript1060','Review1048','Git','Rootstate','Publication','Authors contact','Other chats/agents'],'foreign_corpus':'Read in memory; only own synthesis,URL/version/hash and receipts retained.',
 'C':str(P),'D':r'D:\Proyectos\airr-investigacion\2026-10-27_binary1077-audit'
})
write('READINGS1077.json',{
 'scope':'Directed primary reading, not exhaustive; no priority inference from missing specific match.',
 'sources':[
  {'source':'Berta-Fawzi-Tomamichel','url':'https://arxiv.org/pdf/1512.02615v2','version':'1512.02615v2,final published version2017','sha256':'ea9783f7fdafb2dcd96a08d3f40106b7303a3adcafd5b65b054d99b39a461632','bytes':286613,'pages':22,'PDF_pages_read':[1,2,3,4,7,8],'levels':['abstract','definitions','Lemma1','Theorem2 and proof','Proposition5 and proof'],'whole_paper_audited':False,'summary':'AUDIT1077 section9'},
  {'source':'Ogawa-Nagaoka','url':'https://arxiv.org/pdf/quant-ph/9906090v1','version':'quant-ph/9906090v1','sha256':'ff95d23c83d72e074e22016d18f7b4a70f7916da747779b1a9185a37bdae5bbd','bytes':123907,'pages':12,'PDF_pages_read':[1,2,3,4,5],'levels':['abstract','hypothesis model','Lemma1','Theorem1 and proof','Theorem2 and argument'],'endpoint_caveat':'v1 prints epsilon0; not adopted. Faithful null state and zero typeI error force identity test, so standard interpretation used with0<epsilon<1. No claim about journal revision.','summary':'AUDIT1077 section9'},
  {'source':'Ogawa-Hayashi','url':'https://arxiv.org/pdf/quant-ph/0110125v1','version':'quant-ph/0110125v1','sha256':'784c1fa277b32cfea167593a2770e99ef4106bd1872891f4bcb8b27c527fd937','bytes':124629,'pages':6,'PDF_pages_read':[1,2],'levels':['abstract','model','Theorems1-2 statements'],'whole_proof_read':False,'summary':'AUDIT1077 section9'},
  {'source':'Hiai-Petz1991','url':'https://doi.org/10.1007/BF02100287','levels':['public abstract','bibliographic metadata'],'original_article_body_read':False,'access':'Subscription/purchase; no purchase or bypass','hash_receipt':'PRIMARY_HIAIPETZ1077.json','restatement_read_in':'Ogawa-Hayashi0110125v1 Theorem2'},
  {'source':'Makur/Lee classical benchmark','status':'Inherited1058 audit; not freshly retrieved1077','novelty_claim':False},
  {'source':'Inputs1070/1073','proof_and_scripts':'Complete reading','JSON':'Parsed and replay compared; not each digit manually read','hashes':'INPUT_VERIFIED1077.json'}
 ],
 'search_queries':['Berta Fawzi Tomamichel variational expressions quantum relative entropies measured relative entropy arxiv','Ogawa Nagaoka strong converse quantum hypothesis testing quantum Stein lemma arxiv9906090','Hiai Petz proper formula relative entropy asymptotics quantum probability1991 measurement','"measured relative entropy" "binary" "depolarizing" phase','"relative entropy" "limiting eigenvector" measurement depolarizing'],
 'search_limit':'Unrelated/secondary hits not used as evidence. No identified literal covering theorem for this specific sequence, no absence or priority conclusion.','foreign_corpus_saved':False
})
write('INCIDENTS1077.json',{
 'incidents':[
  {'id':'locator_encoding','kind':'tool_output_failure','receipt':'PRIMARY_LOCATOR_FAILURE1077.json','facts':'Ad hoc locator used cp1252 and failed on Unicode; UTF8 repair and complete subsequent passage reads.'},
  {'id':'generator_side_effects','kind':'adaptation','facts':'Only computational fragments executed under ownfolders; original creation/sealing/C-Dcopying omitted.','receipt':'REPLAY1077.json'},
  {'id':'original_adverses','kind':'negative_finite_results','count':12,'cases':ic['original_adverse'],'omitted':False},
  {'id':'source_epsilon_endpoint','kind':'literal_source_caveat','facts':'Ogawa-Nagaokav1 Theorem2 includes epsilon0 in extracted text. Own faithful-state argument excludes that endpoint; only standard0<epsilon<1 interpretation used. No claim about journal version.'},
  {'id':'Hiai_original_access','kind':'reading_limit','facts':'Public abstract only; subscription body not obtained; no purchase,bypass or contact.','receipt':'PRIMARY_HIAIPETZ1077.json'},
  {'id':'own_simpler_projector','kind':'scope_qualification','facts':'K_d derived within audit shows exact diagonalization not necessary for leading asymptotic. Constant limiting vector still fails forbeta>3. Original finiteidentity remainsvalid.'},
  {'id':'uniformity_and_normalization','kind':'scope_falsifiers','facts':['Moving t gives fraction1/2 and scaledratio1/6','Reverse orientation loses logarithmic factor','Unweighted conditional block divergence can exceed ambientD','Fullambientidentity gives invalidPOVM','Measured-input affine map has negative entry'],'receipts':['SYMBOLIC1077.json','AMBIENT1077.json','INTERVAL1077.json']}
 ],'mathematical_control_failure1077':False,'earlier_failures_preserved_in_immutable_prior_audits':True
})
write('CONTROL_INDEX1077.json',{
 'universal_proof':'AUDIT1077 sections2-6; finitecontrols do not prove universality.',
 'runs':[
  {'script':'verify1077.py','outputs':['INPUT_VERIFIED1077.json','INPUT_FINAL1077.json'],'purpose':'External manifest hashes,allpayloads,C/Didentity,inventory and immutability'},
  {'script':'replay1077.py','outputs':['REPLAY1077.json','replay1070/CONTROL1070.json','replay1073/AMBIENT1073.json'],'purpose':'Adapted replay,allfields exceptutc match'},
  {'script':'symbolic1077.py','outputs':['SYMBOLIC1077.json'],'purpose':'General projector/probability identities,endpoint kernel,limiting vector leakage,moving-t rational scalings'},
  {'script':'ambient1077.py','outputs':['AMBIENT1077.json'],'purpose':'Four full ambient cases,alternative eigenvector construction,exact complements,100digit logarithms,denominator/normalization falsifiers'},
  {'script':'intervals1077.py','outputs':['INTERVAL1077.json'],'dependencies':['integer_arithmetic1077.py'],'purpose':'57certificates,36originals enclosed,12adverses retained,alternative projectors/orientation/uniformity'},
  {'script':'primary1077.py','outputs':[f.name for f in sorted(P.glob('PRIMARY_*.json'))],'purpose':'Primary read/hash receipts and encodingincident'}
 ],'arithmetic':{'bits':1024,'atanh_terms':600,'tail_bound':'4/[3*(1201)*2^1200]','lineage':'1054/1058/1068 own primitives','decimal_displays':'Not exact endpoints'}
})
print('Verdict and audit metadata written.')
