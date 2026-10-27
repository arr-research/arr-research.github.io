from pathlib import Path
import json, hashlib, datetime, shutil, urllib.request, platform
P=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
PDF='255ca15a68df24944e2f3623265e9912ca7cad1d75e96074fadb304c0f83eb7e'
FROZEN='6f43e3d85b5d781f5f47b57aa7a439f5e1afad4294f70d67fa969ae27968ef04'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
criteria={
 'correctness_confidence':{'stars':4,'basis':'Reconstrucción de pruebas generales, geometría ambiental y límites; cinco replays coincidentes y controles propios. No hay error material confirmado, pero no es verificación formal ni humana independiente.'},
 'rigor':{'stars':4,'basis':'Distingue supremum/realización finita, SLD/triangular/all-Petz/BKM, orden del marginal real y límites ordenados. Los óptimos abiertos no se prometen como resultados.'},
 'novelty':{'stars':3,'basis':'Candidatas: clasificación exacta y rangos/constantes de familias explícitas. Definiciones, preparaciones, maquinaria clásica y metrología son previas. Lee–Makur completo no leído; búsqueda dirigida, no exhaustiva.'},
 'significance':{'stars':4,'basis':'Contribución especializada relevante con una separación medida explícita. No determina BKM/Umegaki generales, una frontera de recursos, capacidad ni ventaja experimental a ruido fijo.'},
 'reproducibility':{'stars':4,'basis':'PDF/fuentes congelados, informes y adversos conservados, cinco reproducciones idénticas, controles exactos e intervalos. No se reprodujo toda la campaña ni se certifica independencia de bibliotecas o revisores.'}}
obs=[
 {'id':'O1','severity':'moderate_novelty_uncertainty','material':False,'scope':'Prioridad y posible teorema cubriente','finding':'Herramientas, definición completa y preparaciones son previas; falta la fórmula/prueba íntegra de Lee–Makur. Una búsqueda vacía no acredita novedad.','status':'open_priority_uncertainty_explicitly_limited','requested_action':'Mantener prioridad abierta; comparación primaria más amplia antes de alegarla.'},
 {'id':'O2','severity':'moderate_if_extrapolated','material':False,'scope':'Teoremas10–13 y comparación Bell medida','finding':'Ruido dependiente de dimensión, denominador cuántico e información absoluta decreciente; no capacidad, MI ordinaria, óptimo, ventaja experimental ni canal clásico binario nuevo.','status':'scope_satisfied_in_exact_pdf','requested_action':'Conservar estas limitaciones en cualquier resumen o publicación.'},
 {'id':'O3','severity':'minor_presentation','material':False,'scope':'Transición posterior a proposición11','finding':'Tras el benchmark all-Petz convendría repetir Umegaki/triangular al invocar la familia de fase; los enunciados completos delimitan la clase y no se confirma error.','status':'optional_clarification','requested_action':'Nombrar localmente las cantidades del teorema10, sin ampliar su alcance.'},
 {'id':'O4','severity':'moderate_evidence_limit','material':False,'scope':'Revisión, auditorías y suplementos','finding':'Contexto compartido y bibliotecas dependientes; replays no son revisores independientes. No se revalidaron todos los archivos remotos ni programas históricos.','status':'declared_evidence_limit','requested_action':'Conservar informes completos, alcances y adversos, sin afirmar independencia atestada.'},
 {'id':'O5','severity':'minor_presentation','material':False,'scope':'Abstract e historia de auditorías','finding':'Abstract largo, abundantes identificadores internos y carga histórica. No impide reconstruir pruebas, pero dificulta la lectura científica continua.','status':'optional_editing','requested_action':'Concentrar procedencia en apéndice y resumir cantidades/recursos, conservando evidencia.'},
 {'id':'O6','severity':'moderate_if_uniformity_is_claimed','material':False,'scope':'Costes y límites de teoremas10–13','finding':'t fijo no puede reemplazarse por t_d; vector límite constante y orientación inversa pierden información; tolerancia angular sólo suficiente dentro del plano.','status':'adverse_cases_preserved_and_scope_satisfied','requested_action':'No extrapolar a frontera óptima, ruido fijo o robustez uniforme.'}
]
strengths=[
 'Clasificación completa SLD/chi_min/triangular de canales unitales qubit con normalizaciónChoi y regularizaciones correctas.',
 'Rangos separados Bell d²/2 all-Petz, rango dos M=d(2d−1)/2 SLD/triangular y lowerBKM/Umegaki P=d(d−1), con presupuesto del marginal real.',
 'Familia de fase local finita con identidades exactas, separación comúnBell para ambos signos y costes cuantificados.',
 'Escalado a parámetros fijos y proyector binario ambiental explícito que conserva la información de salida principal; falsadores a extensiones preservados.',
 'Pruebas legibles, seis certificados finitos reproducidos con intervalos, cinco replays coincidentes y controles propios con geometría ambiental.'
]
novelty=[
 'Candidata condicionada a prioridad: fórmula completa de canales unitales qubit y envolvente exacta.',
 'Candidatos condicionados a prioridad: rango principal de orden y constante logarítmica P con cuantificadores separados.',
 'Candidata constructiva: realización finita de fase, constantes de costes a parámetros fijos y proyector simplificado con probabilidades exactas que conserva el leading output. Preparación, asistencia por ancilla y teoría de entropía medida son previas.'
]
potential=[
 'No se confirmó un error material en el PDF1083; esto no certifica inexistencia de errores.',
 'Un teorema primario no identificado puede cubrir parte de la contribución; cobertura precisa Lee–Makur no comprobada.',
 'No transferir exactitudSLD/triangular al BKM/Umegaki general ni al conjunto all-Petz de rango mayor.',
 'No extrapolar el modelo especial de fase a todas las órbitas unitarias, ni intercambiar límites o medir la entrada manteniendo el denominador cuántico.',
 'La reproducción acotada comparte código e historia; no acredita aislamiento, independencia ni toda la campaña o publicación remota.'
]
summary=('Revisión completa1084 del PDF1083 exacto de23p, SHA256 '+PDF+'. No se confirmó objeción matemática material tras lectura completa, reconstrucción analítica y controles acotados. Recomiendo publicación científica con alcance declarado; accept no significa aceptación editorial. Clasificación exacta qubit, perfiles de orden y familias explícitas de fase/medición aportan resultados especializados; herramientas y preparaciones son previas, prioridad abierta. ImportanciaAIRR6.3, globalMillennium6.1 y técnica8.7 son juicios separados, no promedios ni probabilidades. Contexto952/1048 y antecedentes reutilizados, filesystem compartido y participaciónCodex declarada; identidad/effort efectivos e independencia no atestados. No se heredan notas. LímitesO1–O6 y adversos íntegros en informe/veredicto. No IDs públicos suministrados: contenido sin vinculación nativa y sin relación con1005v1.')
verdict={
 'review':'1084','type':'single_new_complete_scientific_assessment','assessed_at':NOW,
 'exact_artifact':{'title':'Complete contraction of unital qubit channels and order-constrained depolarization','pdf_sha256':PDF,'pdf_bytes':432959,'pdf_pages':23,'frozen_sha256':FROZEN,'manifest_payloads':16},
 'scientific_importance_airr_0_10':6.3,'overall_millennium_0_10':6.1,'technical_quality_0_10':8.7,'overall_stars':6,
 'score_bases':{
  'scientific_importance_airr':'Clasificación exacta, perfil de orden y separación medida concreta relevantes; ámbito especializado, sin óptimo general ni beneficio operacional robusto demostrado.',
  'overall_millennium':'Trabajo convincente y con resultados concretos; prioridad abierta, métodos de ampliación principalmente algebraicos y aplicaciones limitadas. No es un promedio de criterios ni transferencia de1048.',
  'technical_quality':'Cuantificadores, geometría ambiental, límites y certificados bien sustentados. Reservas de inspección independiente/bibliográfica y presentación densa; ninguna objeción material confirmada.'},
 'criteria':criteria,'recommendation':'recommend_publication_with_declared_scope','arr_recommendation':'accept','editorial_decision':None,
 'summary':summary,'strengths':strengths,'objections':obs,'weaknesses':[o['id']+': '+o['finding'] for o in obs],
 'potential_errors':potential,'strong_novelty_candidates':novelty,'unresolved_material_objections':[],
 'reviewer_disclosure':{'requested_configuration':'GPT-6 Astra xhigh','effective_identity_attested':False,'effective_reasoning_effort_attested':False,'independence':'involved_in_manuscript','shared_filesystem':True,'reused_context':['952','998','1006','1010','1031','1042','1048','component audits and ensuing task history'],'possible_bias':'Prior participation, shared history and reports can bias interpretation; no isolated or independent second voice is claimed.','AI_participation_numeric_penalty':False},
 'prior_reviews':'1031/1042/1048 concern predecessor PDFs, preserved as history; component audits are dependent evidence, not additional votes for1083.',
 'proof_status':'Analytical reconstruction plus bounded controls, not formal verification or worldwide priority certificate.',
 'report':'REVIEW1084.txt','report_sha256':sha(P/'REVIEW1084.txt'),'controls':['OWN1084.json','REPLAY1084.json','FINITE-CERTIFICATES1084.json'],
 'terminal_condition':'Only terminal after successful INPUT-FINAL1084, DEPENDENCIES-FINAL1084 and ARCHIVE1084 receipts.'}
put('verdict1084.json',verdict)
arr={'canonical_sha256':PDF,'provider':'OpenAI','model_id':'effective-model-unattested; requested GPT-6 Astra xhigh','assessed_at':NOW,'prompt_version':'ARR-ASSESS-1.0','independence':'involved_in_manuscript','recommendation':'accept','millennium_score':6.1,'overall_stars':6,'criteria':criteria,'summary':summary,'strengths':strengths,'weaknesses':verdict['weaknesses'],'potential_errors':potential,'strong_novelty_candidates':novelty,'unresolved_material_objections':[]}
put('ARR-CONTENT-UNBOUND1084.json',arr)
repo=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
put('ARR-BINDING-LIMITS1084.json',{'utc':NOW,'purpose':'Projection of the same1084 assessment, not another vote or new grade','report_sha256':sha(P/'REVIEW1084.txt'),'verdict_sha256':sha(P/'verdict1084.json'),'content_sha256':sha(P/'ARR-CONTENT-UNBOUND1084.json'),'canonical_pdf_sha256':PDF,'missing_identity_fields':['paper_id','version','version_id','assessment_id','source_response_sha256'],'native_importable':False,'identity_reason':'No public identity was supplied for exact1083. No v2, fake case or1005v1 binding invented.','recommendation_mapping':'recommend_publication_with_declared_scope -> accept, scientific recommendation only, never editorial Accepted.','score_mapping':'Global6.1 -> millennium_score6.1 and overall_stars6. Importance6.3 and technical8.7 remain separately in summary/full verdict. No implicit averaging.','disclosure_mapping':'model_id explicitly unattested; involvement retained. No invented runtime_provenance or operator review_context.','format_mapping':'ARR-ASSESS-1.0 is a content serialization format here, not evidence of fresh blind review.','schema_sources':[{'path':str(repo/'scripts'/n),'sha256':sha(repo/'scripts'/n)} for n in ['assessmentlib.py','prepare_model_assessment.py']]})
old=P/'dependencies'/'2026-10-27_complete1048-review'
scope=P/'prior-scope';scope.mkdir(exist_ok=True)
oldroot=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1048-review')
for n in ['READINGS1031.json','SOURCE_FETCHES1031.jsonl']:
 shutil.copy2(oldroot/'prior-scope'/n,scope/n)
fetches=[json.loads(x) for x in (P/'SOURCE_FETCHES1084.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
details={
 '1008.1557v1':('Frey–Collins–Gerlach','2,3,5,6,7','Preparation/Schmidt blocks and binary joint measurement prior; selected calculations/statements, not full appendix audit.'),
 '1510.01844v4':('Makur–Zheng','11,12,29,30','Definition5, Proposition6 and selected proof via less-noisy erasure comparison; not all37pages.'),
 '1512.02615v2':('Berta–Fawzi–Tomamichel','2,3,4,7,8','Lemma1, Theorem2 and Proposition5 selected statements/proofs; not all22pages.'),
 'quant-ph/0110125v1':('Ogawa–Hayashi','1,2','Model and Theorems1/2 statements only; no full proof audit.'),
 '2608.27171v1':('Hirche–George–Nuradha–Wilde','8,9,20,28','Definitions1/2 and selected lemma proof, comparison example and Definition12/Corollary7; not upstream full proof ofCor7 or84pages.'),
 '2608.19685v1':('Gao–Zhao','15,16,17','Proposition3.11, Lemma3.12 proof and Theorem3.13 index asymptotics; old introductory scope separately reused.'),
 '1904.01904v1':('Chapeau-Blondeau','3,4,7,8,16,17,18','Phase blocks/SLD, Eq29 and inactive ancillary modes Eq44;17–18 recovered separately after truncation; not full23pages.')}
sources=[]
for version,(author,pages,limit) in details.items():
 r=next(x for x in fetches if x['url'].endswith(version))
 sources.append({**r,'author':author,'version':version,'read_pages':list(map(int,pages.split(','))),'reading_scope':limit,'full_source_read':False})
web=[]
for url in ['https://easychair.org/smart-program/2024Allerton/2024-09-25.html','https://www.cs.purdue.edu/homes/amakur/publications.html','https://dongmin.dev/']:
 try:
  data=urllib.request.urlopen(url,timeout=30).read()
  web.append({'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'foreign_corpus_saved':False,'reading':'Lee–Makur record/abstract only; full formula/proof unread','hash_fetch_only':True})
 except Exception as e: web.append({'url':url,'hash_unavailable':repr(e),'reading':'Earlier web record/abstract only','foreign_corpus_saved':False})
web.append({'url':'https://doi.org/10.1109/ALLERTON63246.2024.10735307','web_result':'not accessible via web tool','full_text_read':False,'hash':None})
put('WEB-READINGS1084.json',{'utc':NOW,'sources':web,'foreign_corpus_persisted':False})
put('READINGS1084.json',{'utc':NOW,'exact_pdf':{'sha256':PDF,'all23pages_visually_read':True,'PAPER1083_complete_read':True,'main_and_all7sections_complete_read':True,'text_comparison':'TEXT-CHECK1084.json'},'component_reports_read_current_in_full':['1054','1058','1068','1077'],'report1044':'Full reading reused from1048; core proof reconstructed currently from exact manuscript.','history_scope':{'metadata':str(old/'READINGS1048.json'),'sha256':sha(old/'READINGS1048.json'),'prior1031_metadata':[{'path':str(q.relative_to(P)),'sha256':sha(q)} for q in scope.iterdir()],'no_new_full_read_claim':True},'primary_sources_current':sources,'primary_records_and_abstracts':web,'prior_primary_scope_reused':'Hiai–Ruskai, Ruskai–Szarek–Werner, HHH, Cao–Lu, Hirche–Rouze–Franca, Doeblin, George–Tomamichel, Belzig et al. and Han–Li: exact versions/hashes and limitations in historical metadata; not newly read in full.','queries':['"complete contraction" "qubit" "minimal" quantum','"depolarizing" "relative entropy" "binary measurement"','"Contraction Coefficients of Product Symmetric Channels" Lee Makur','"phase" "relative entropy" "depolarizing" ancilla','"relative entropy" "unitary orbit" "contraction" depolarizing','"measured relative entropy" "single copy" "binary" dimension'],'search_limits':'Directed, nonexhaustive primary comparison; last broad output truncated, not counted as read or no-result evidence. No empty-search novelty inference. Lee–Makur full text unavailable.','public_transport_verification':'Parent/source claims remote files/Pages match; not all rechecked1084. No new public/Git/CI action.'})
incs=[
 {'id':'I1','type':'preparation_schema','detail':'Initial preparer assumed files key;1077 uses payloads. Original script and first input receipt preserved. Both keys accepted on same exact inputs.','preserved':['prepare1084_initial.py','INPUT-FIRST-PASS1084.json']},
 {'id':'I2','type':'read_command_syntax','detail':'Read-only ad hoc Python text-comparison command had unmatched closing parenthesis; corrected query without input mutation. Tool output showed SyntaxError.','preserved':['TEXT-CHECK1084.json']},
 {'id':'I3','type':'own_control_implementation','detail':'Structural unsimplified trace equality failed on the fourth complex-phase case; failure handler also could not JSON-serialize SymPy BooleanTrue. Same parameters show trace1/unitarity after simplification. Only simplification/bool conversion repaired; no parameter search or mathematical counterexample removed.','preserved':['own1084_initial.py','OWN-INITIAL-FAILURE1084.txt','diagnose1084.py','DIAGNOSIS1084.json','own1084.py','OWN1084.json']},
 {'id':'I4','type':'output_truncation','detail':'Aggregated outputs truncated. Needed manuscript/source portions reread separately. Unrecovered search output not counted as evidence of reading or absence.','preserved':['SOURCE_FETCHES1084.jsonl','READINGS1084.json']},
 {'id':'I5','type':'text_format_comparison','detail':'Poppler-layout text not byte-identical; PyPDF extraction matches frozen text modulo whitespace. Format difference, not input corruption.','preserved':['EXTRACTED1084.txt','TEXT-CHECK1084.json']},
 {'id':'I6','type':'bibliographic_access_limit','detail':'Lee–Makur DOI not accessible through web tool. Primary program abstract read, complete formula/proof not read; priority remains open. This I6 is local to1084, not the historical inventory incident.','preserved':['WEB-READINGS1084.json','READINGS1084.json']}
]
shutil.copy2(P/'INCIDENTS1084.txt',P/'INCIDENTS-FIRST1084.txt')
put('INCIDENTS1084.json',{'utc':NOW,'incidents':incs,'no_original_input_modified':True,'no_review_restart_or_grade_search':True,'no_adverse_result_discarded':True,'scope_boundary':'InputC132auxiliaries outside16payloads separated from start; historic I6 not repeated.'})
(P/'INCIDENTS1084.txt').write_text('\n\n'.join(i['id']+' — '+i['detail'] for i in incs)+'\n',encoding='utf-8')
put('PROVENANCE1084.json',{'utc':NOW,'requested_configuration':'GPT-6 Astra xhigh','effective_model_identity':None,'effective_reasoning_effort':None,'effective_runtime_attestation_available':False,'provider_context':'OpenAI Codex','participation':'involved_in_manuscript','shared_filesystem':True,'reused_context':verdict['reviewer_disclosure']['reused_context'],'history_blinded':False,'other_reports_withheld':False,'statistical_independence_attested':False,'isolation_attested':False,'possible_bias':verdict['reviewer_disclosure']['possible_bias'],'new_agents_or_chats':False,'new_models':False,'single_current_assessment':True,'prior_reports_other_pdfs':True,'no_grade_target':True,'no_grade_inheritance':True,'AI_assistance_automatic_penalty':False,'input_C':r'C:\Trabajo\airr\2026-10-27_complete1060','input_D':r'D:\Proyectos\airr-investigacion\2026-10-27_combined1083','input_scope':'16manifest payloads+self only;C132unsealed auxiliaries excluded','own_work':str(P),'archive':r'D:\Proyectos\airr-investigacion\2026-10-27_combined1084-review','report_sha256':sha(P/'REVIEW1084.txt'),'verdict_sha256':sha(P/'verdict1084.json'),'rubric_sha256':sha(P/'RUBRIC1084.md'),'rubric_fresh_context_requirement':'Not met; explicit authorized reused context disclosed. No operator-controlled evidence fabricated.','global_instructions':'User globalAGENTS supplied/current; D:\LEEME.md read in reused context. WorkC/saveD; no roots or other dossiers altered.','runtime':{'python':platform.python_version(),'sympy':'1.14.0','mpmath':'1.3.0'},'source_policy':'External primary corpus in RAM only; saved URLs/version/hash/synthesis and own controls.','reproduction_scope':'5bounded replays plus own exact/symbolic/numeric controls and6directed integer certificates; not all historical scripts or remote publication endpoints.','no_publication_or_editorial_acceptance':True,'no_git_or_root_state_changes':True})
put('CONTROL-INDEX1084.json',{'own':'OWN1084.json','own_initial_failure':'OWN-INITIAL-FAILURE1084.txt','own_diagnosis':'DIAGNOSIS1084.json','bounded_replays':'REPLAY1084.json','six_printed_finite_certificates':'FINITE-CERTIFICATES1084.json','source_read_receipts':'SOURCE_FETCHES1084.jsonl','numerical_vs_certified':'85digit fullambient evaluation is numerical; geometry and rational forms exact;1024bit600term integer interval code certifies6printed cases.','shared_code_lineage':True,'unexecuted_current':'Old4BKMfiniteintervalcertificates, full1054genericorbitfalsifier, fullhistoricaloptimizers and publictransportcampaign notrerun1084; evidencehashverified and analyticalproofsreconstructed.'})
print(json.dumps({'verdict_sha256':sha(P/'verdict1084.json'),'report_sha256':sha(P/'REVIEW1084.txt'),'content_sha256':sha(P/'ARR-CONTENT-UNBOUND1084.json'),'sources':len(sources),'objections':len(obs)},indent=2))
