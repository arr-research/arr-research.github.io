from pathlib import Path
import json, hashlib, datetime, shutil, sys, platform

ROOT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,value):
    p=ROOT/name
    assert not p.exists(),str(p)
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pdfsha='f805a688fb62e9bb34f4c8f107f906c4f85613f831cfda424d1805b797fffe07'
frozen='406dcccd5be71ac41d6c96a54fe3e415349b64d8c89a29d7fe043801661d835e'
reportsha=sha(ROOT/'REVIEW1048.txt')
criteria={
 'correctness_confidence':{'stars':4,'basis':'No se encontró un error material tras reconstruir las pruebas generales, los cuantificadores, los límites y los controles exactos. Es una revisión por modelo, no una certificación formal ni una voz independiente del contexto previo.'},
 'rigor':{'stars':4,'basis':'Cota Petz general, sharpness SLD/triangular y lower BKM se justifican con argumentos distintos y límites ordenados. El examen incluye fidelidad, presupuesto de ambas entradas, soporte y orientación de Umegaki; no se pretende exactitud BKM.'},
 'novelty':{'stars':3,'basis':'No se encontró cobertura literal de los enunciados concretos en los pasajes primarios examinados. La definición completa, las herramientas métricas y la reducción de resolventes son antecedentes; la ampliación geométrica es incremental y la prioridad sigue abierta.'},
 'significance':{'stars':4,'basis':'Clasificación y cotas útiles para un problema especializado, con una mejora cuantitativa de lower BKM en dimensión general. Sin upper BKM óptimo, consecuencia para capacidad o aplicación operacional demostrada; no constituye una teoría transformadora.'},
 'reproducibility':{'stars':5,'basis':'PDF y fuentes congelados, suplemento público fijado y verificado, cinco verificadores reproducidos con salida idéntica y controles propios exactos/numéricos diferenciados. Se conservan procedencia, incidentes y límites de lectura; esto no implica independencia.'}
}
findings=[
 {'id':'R1','kind':'bibliographic_uncertainty','material':False,'status':'open_and_declared','finding':'La prioridad mundial y la ausencia de un teorema cubriente no quedan certificadas por una búsqueda dirigida.','basis':'Se contrastaron fuentes primarias y se distinguieron definiciones completas, entropía respecto E, correlación con base fija y pares con igual marginal. Véanse REVIEW1048 §7 y READINGS1048.'},
 {'id':'R2','kind':'scope_limit','material':False,'status':'adequately_delimited_in_exact_pdf','finding':'El cap M es exacto para SLD, chi mínima y triangular; el resultado P es un lower BKM/Umegaki y no un upper, exactitud irrestricta, información mutua ordinaria o capacidad.','basis':'Reconstrucción analítica independiente dentro del mismo contexto, incluida la divergencia logarítmica BKM y el orden t, epsilon, theta de los límites.'},
 {'id':'R3','kind':'utility_limit','material':False,'status':'open_and_declared','finding':'El mayor rango usa referencia 2d-1; no se prueba minimalidad ni sharpness a referencia arbitraria fija. Los ejemplos finitos están fuertemente condicionados y no implementan una aplicación unitaria.','basis':'La traza del tangente en proyectores que conmutan con el estado impide presentarlo como conmutador; cuatro gaps intervalares positivos prueban existencia finita, no robustez experimental.'},
 {'id':'R4','kind':'public_evidence_scope','material':False,'status':'documented','finding':'Se verificaron directamente 25 archivos del suplemento fijado, no los31 ni cinco endpoints comunicados por el padre. El informe completo1044 leído localmente no se convierte por ello en evidencia pública ya verificada.','basis':'PUBLIC-VERIFIED1048.json; audit1044 íntegro conservado como evidencia dependiente del expediente.'},
 {'id':'R5','kind':'review_provenance','material':False,'status':'declared_not_remediated','finding':'Contexto y filesystem compartidos, participación de Codex, posible sesgo de familiaridad y ausencia de identidad/effort e independencia atestados.','basis':'Encargo1048 y contexto reutilizado952/998/1006/1010/1031/1042. No se inició otro agente o revisión paralela.'},
 {'id':'R6','kind':'optional_presentation','material':False,'status':'optional_no_change_made','finding':'La página14 tiene mucho espacio blanco antes de la bibliografía en15.','basis':'Inspección visual de las15páginas. No hay pérdida, corte o ilegibilidad de contenido y no afecta al dictamen.'}
]
verdict={
 'review':'1048','created_at':now,'object':'Exact frozen PDF1047, complete new manuscript review; no inherited grade or independent-vote claim',
 'manuscript_title':'Complete contraction of unital qubit channels and order-constrained depolarization',
 'manuscript_sha256':pdfsha,'manuscript_bytes':366879,'manuscript_pages':15,'frozen_sha256':frozen,
 'scientific_importance_airr_0_10':6.1,'overall_millennium_0_10':5.9,'technical_quality_0_10':8.7,'overall_stars_1_10':6,
 'scores_are_separate':True,'scores_are_an_average':False,'prior_scores_inherited':False,'desired_score':None,
 'score_bases':{
 'scientific_importance_airr':'6.1: el conjunto aporta clasificación completa qubit y envolvente exacta, sharpness bajo presupuesto con rango ampliado y un lower BKM/Umegaki cuantitativamente más fuerte en parte del dominio. Es útil como referencia especializada; la ampliación del cap es incremental y no hay upper BKM óptimo ni aplicación operacional.',
 'overall_millennium':'5.9: buena contribución técnica, coherente e inspeccionable, con novedad relativa plausible pero no certificada. El cálculo BKM añade contenido real, aunque usa herramientas espectrales conocidas. La especialización, la prioridad abierta y la ausencia de consecuencia amplia impiden un juicio excepcional o transformador.',
 'technical_quality':'8.7: pruebas generales reconstruidas, límites/regularizaciones legales, cuantificadores y orientación revisados; cinco replays idénticos y nuevos controles exactos. No se encontró fallo material. Restan incertidumbre bibliográfica y ausencia de formalización/independencia, además de mejoras opcionales de presentación.'},
 'criteria_1_5':criteria,
 'recommendation':'recommend_publication_with_declared_scope','arr_recommendation_mapping':'accept',
 'recommendation_basis':'Recomendación científica para este PDF exacto tras examen completo. No es aceptación editorial, publicación, certificación de prioridad o nueva voz independiente del contexto previo.',
 'new_confirmed_mathematical_errors':[], 'unresolved_material_objections':[], 'findings_and_limits':findings,
 'prior_objections_reexamined':[{'id':'1031-O1','status':'resolved_in_current_pdf','basis':'Primal con X hermítico, dual Tr_A Y=I y alpha+ distinto: formulación y alcance del certificado Doeblin correctos.'},{'id':'1031-O2','status':'resolved_in_current_pdf','basis':'Base NPT limitada a SLD/chi mínima; Petz finito solo excluye que ambas entradas sean PPT. No se ha extendido indebidamente la conclusión.'}],
 'major_claims_checked':['Universal positive-kernel Petz harmonic upper including zero weights and physical endpoints','Unital qubit complete contraction, singular regularization, fixed-source equal reference and exact envelope','Actual marginal order budget for both inputs and Bell sharpness range','Rank-two M=d(2d-1)/2 exact SLD/chi_min/triangular range with reference2d-1','BKM logarithmic coefficient with P=d(d-1), Umegaki rho||sigma local transfer, budget maximum and negative-endpoint comparison between two lowers','SEP/PPT/classical resource restrictions, Doeblin signed-primal certificate, nonunitary tangent'],
 'evidence':{'report':'REVIEW1048.txt','report_sha256':reportsha,'reproductions':'REPRODUCTION1048.json','own_controls':'OWN1048.json','readings':'READINGS1048.json','provenance':'PROVENANCE1048.json','incidents':'INCIDENTS1048.json'},
 'editorial_acceptance':False,'published_by_this_review':False
}
put('verdict1048.json',verdict)

prior=Path(r'C:\Trabajo\airr\2026-10-27_complete1031-review')
(ROOT/'prior-scope').mkdir(exist_ok=True)
priorfiles=[]
for name in ['READINGS1031.json','SOURCE_FETCHES1031.jsonl']:
 p=prior/name
 assert p.exists(),str(p)
 q=ROOT/'prior-scope'/name
 assert not q.exists()
 shutil.copy2(p,q)
 priorfiles.append({'path':q.relative_to(ROOT).as_posix(),'sha256':sha(q),'original':str(p),'use':'Prior reading-scope metadata, not foreign corpus and not a fresh full rereading.'})
fetches=[json.loads(x) for x in (ROOT/'SOURCE_FETCHES1048.jsonl').read_text(encoding='utf-8').splitlines()]
byurl={x['url']:x for x in fetches}
descriptions={
 '1508.03551v1':('PDF9 Example1;20–21 Theorem7.1, including the selected proof.','Symmetrized relative-entropy/metric comparison and ordinary-channel context; not a full40-page audit. Representation and earlier qubit results also use prior1031 selected readings.'),
 '2411.19890v3':('PDF9–10 Eq15–19 and full Lemma4.1 proof;15 Proposition5.1 ordinary depolarization comparison;27 Definition7.1.','Weighted segment/local relation and ordinary mutual-information definition, not all32pages. First console attempt failed; same bytes successfully read with UTF-8.'),
 '2608.19685v1':('PDF3,4,11,14,16,17; Theorem1.2/Corollary1.3 and Definition3.7; Proposition3.11 and Lemma3.12 proofs.','Entropy relative to conditional expectation E; selected passages do not literally give the arbitrary equal-marginal pair optimization. Not an absence-of-covering-theorem certificate.'),
 '2608.27171v1':('PDF8–9 Definitions1/2 complete same-reference coefficient;20 ordinary/complete depolarization separation;28 Definition12 and Corollary7. Earlier RAM search snippets5,20,33,45,76.','Corollary7 states a relation to a restricted mutual-information coefficient; its full upstream proof was not audited. Complete equal-reference concept is prior art. No assertion of zero informational meaning.'),
 '2505.15281v3':('This review: RAM search for depolar only; no matches. Earlier1031 selected reading: PDF37 Eq127–128/Proposition60;59–60 Theorem105 and selected proof.','No full new reading and no novelty inference from an empty text search. Prior fixed-base/correlation comparison is explicitly reused.')
}
sources=[]
for key,(scope,limit) in descriptions.items():
 r=dict(byurl['https://arxiv.org/pdf/'+key]);r['version']=key;r['reading_scope']=scope;r['limit']=limit
 sources.append(r)
han=json.loads((ROOT/'HAN-LI-HTML1048.json').read_text(encoding='utf-8'))
sources.append({'url':'https://arxiv.org/html/2610.29373v1','version':'2610.29373v1','sha256':'baf015500852d2f136b16b2b590f8972dafead61dc85a8f5844c494110fab051','reading_scope':'Abstract and section2.2, definitions and Lemma1 Eq29–32 with attribution to Belzig.','limit':'No amplitude-damping proof audit. HTML was read remotely and fetched in RAM for hashing only.','foreign_corpus_saved':False,'receipt':'HAN-LI-HTML1048.json'})
put('READINGS1048.json',{
 'utc':now,'exact_manuscript':{'pdf':'input/main.pdf','sha256':pdfsha,'complete_text_read':True,'all_15_pages_visually_inspected':True,'tex_complete':['main.tex','sections/qubit.tex','sections/order.tex','sections/bkm.tex','sections/context.tex'],'source_diff':'SOURCE-DIFF1048.txt','extraction_byte_identical_to_frozen_text':True},
 'audit1044':{'full_report_read':True,'files_verified_C_D':44,'manifest_payloads_verified':41,'report_sha256':'4626addd8089c2d7acac69ec58f3a0cfa4d5bc3e38e51e3312994d6426462294','shared_context_dependent_evidence':True,'independent_manuscript_vote':False},
 'project_proofs_read_in_full':['public-supplement/principal1033/PROOF1033.txt','public-supplement/bkm1035/PROOF1035.txt'],
 'primary_sources':sources,'prior_reading_records':priorfiles,
 'prior_scope_reused':'Selected1031 readings of Hiai–Ruskai, Ruskai–Szarek–Werner, Horodecki–Horodecki–Horodecki, Cao–Lu, Hirche–Rouze–Franca, quantum Doeblin, George–Tomamichel, and introductory Chapeau-Blondeau. Exact versions/hashes and limits remain in prior-scope/READINGS1031.json; not claimed newly read in full1048.',
 'search_queries_primary_arxiv_only':['"depolarizing" "complete" "relative entropy" "contraction"','"quantum" "same marginal" "contraction coefficient"','"BKM" "contraction" "reference"','"depolarizing" "d(d-1)" "entropy"','quantum relative entropy contraction coefficient ancillary equal marginal depolarization','"complete" "contraction" "minimal" "Fisher" quantum','"strong data processing" "depolarizing" "reference"','"contraction" "principal" "BKM"'],
 'search_limits':'Directed, nonexhaustive primary-source comparison. No priority certificate or inference of novelty from empty search results. Irrelevant tomography/continuity/search hits were not used as scientific support. No foreign paper corpus persisted.',
 'public_check':'PUBLIC-VERIFIED1048.json: directly verified25files at34400956487e21509b5196884caa320907b26f58; does not attest parent31files/5Pages/CI.'
})

incidents=[
 {'id':'I1','type':'console_encoding','status':'recovered_without_scientific_reset','detail':'First Belzig2411.19890v3 fetch hashed successfully, then printing Greek characters failed with UnicodeEncodeError under cp1252. It was not counted as body reading. The same URL/bytes were retried with Python -X utf8 and requested pages were read. SOURCE_FETCHES1048 preserves both fetch receipts.'},
 {'id':'I2','type':'tool_output_truncation','status':'decisive_passages_recovered','detail':'Some aggregated reads truncated context/audit or remote-source output. Omitted decisive context tail, audit introductory47lines and Han–Li section2.2 were read separately. The long report patch result was also truncated by the tool; saved report existence, length and complete ending were checked.'},
 {'id':'I3','type':'historical_incidents_preserved','status':'not_repeated_or_erased','detail':'audit1044 records the earlier1033 inline-shell quoting SyntaxError and subsequent saved-script sweep, guessed-version URL404 and earlier incorrect local-path lookup. Those originals remain intact; they are not1048 mathematical failures.'},
 {'id':'I4','type':'scope_steering_after_start','status':'excluded','detail':'Parent informed that publication1046 and registry/sweep1049 postdate freeze1047, and that candidate1051 is separate. No1051 content was read or incorporated; no scope change or score restart.'},
 {'id':'I5','type':'negative_findings_retention','status':'all_retained','detail':'No mathematical failure occurred in the five1048 replays or own1048 controls. Their full outputs are retained; that empirical outcome does not replace proof. Historical1031-O1/O2 remain preserved and were found corrected in this PDF.'}
]
put('INCIDENTS1048.json',{'utc':now,'incidents':incidents,'no_restarts_for_preferred_result':True,'all_adverse_findings_retained':True})

instructions=[]
for p in [Path(r'C:\Users\lluis\.codex\AGENTS.md'),Path(r'D:\LEEME.md')]:
 instructions.append({'path':str(p),'sha256':sha(p),'read_scope':'Read in shared context and reconfirmed in1048 before archival closure.'})
import sympy,mpmath
put('PROVENANCE1048.json',{
 'utc':now,'task':'One authorized full review1048 of exact PDF1047','requested_configuration':{'model':'GPT-6 Astra','reasoning_effort':'xhigh'},
 'effective_model_identity_attested':False,'effective_reasoning_effort_attested':False,'runtime_evidence':None,
 'reviewer_environment':'Codex; continuing agent /root/astra_reset952_audit; no assertion of independent reviewer identity',
 'shared_context':['952','998','1006','1010','1031','1042'],'shared_filesystem':True,'codex_participation_in_manuscript_evolution':True,
 'possible_bias':['familiarity','confirmation','shared historical reports and component derivations'],
 'history_isolation_verified':False,'independence_verified':False,'blinding_verified':False,'other_reports_withheld':False,
 'independence_enum':'involved_in_manuscript','new_delegation':False,'other_chats_or_models_used':False,
 'originals_mutated':False,'git_or_root_state_changed':False,'publication_performed':False,'editorial_acceptance':False,
 'input_binding':{'pdf_sha256':pdfsha,'frozen_sha256':frozen,'initial':'INPUT-INITIAL1048.json','final':'INPUT-FINAL1048.json'},
 'audit_dependency':{'audit':'1044','copy':'audit1044/','initial':'AUDIT1044-INITIAL1048.json','final':'AUDIT1044-FINAL1048.json','not_an_independent_manuscript_vote':True},
 'rubric':{'source':r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\docs\MODEL_ASSESSMENT_POLICY.md','local_copy':'RUBRIC1048.md','sha256':sha(ROOT/'RUBRIC1048.md'),'fresh_blind_preference_not_satisfied':'User expressly requested reused context; no operator evidence fabricated.'},
 'instructions':instructions,'skill_applied':'pdf:pdf, read before PDF inspection; no generated replacement manuscript',
 'software':{'python':sys.version,'platform':platform.platform(),'sympy':sympy.__version__,'mpmath':mpmath.__version__},
 'foreign_corpus_saved':False,'prior_scope_metadata':priorfiles,
 'excluded_later_work':['1046publication status as scientific input','1049registry/sweep','1051candidate'],
 'full_review':'REVIEW1048.txt','full_review_sha256':reportsha,
 'archive_target':r'D:\Proyectos\airr-investigacion\2026-10-27_complete1048-review',
 'retention':'Both requested C/D copies retained; no file lives only in C after closure.'
})

own=json.loads((ROOT/'OWN1048.json').read_text(encoding='utf-8'))
rep=json.loads((ROOT/'REPRODUCTION1048.json').read_text(encoding='utf-8'))
assert own['all_passed'] and rep['all_passed']
assert (ROOT/'EXTRACTED1048.txt').read_bytes()==(ROOT/'input/PAPER1047.txt').read_bytes()
put('CONTROL-INDEX1048.json',{'utc':now,'reproduced_verifiers':rep['jobs'],'replay_all_passed':True,
 'own_script':'own_controls1048.py','own_output':'OWN1048.json','own_log':'OWN1048.log','own_all_passed':True,
 'own_checks':[x['name'] for x in own['checks']],
 'distinction':'Symbolic/exact algebra and reproduced integer interval certificates are separated from90-digit numerical global-complex checks. No finite check proves a universal theorem; analytical reconstruction is in REVIEW1048.',
 'not_executed':['check1024.py archival tail','1037optimizer/grid','manuscript packaging/mutating scripts','later1051work'],
 'qa':{'pages':15,'render_dpi':100,'all_inspected':True,'text_extract_byte_equal':True,'text_sha256':sha(ROOT/'EXTRACTED1048.txt'),'content_clipped':False,'optional_note':'Large whitespace on page14 before bibliography15; no scientific content loss.'}})

arr={
 'canonical_sha256':pdfsha,'provider':'OpenAI','model_id':'unattested (requested GPT-6 Astra xhigh; Codex participation)',
 'assessed_at':now,'prompt_version':'ARR-ASSESS-1.0','independence':'involved_in_manuscript','recommendation':'accept',
 'millennium_score':5.9,'overall_stars':6,'criteria':criteria,
 'summary':'Revisión completa1048 del PDF1047 exacto de15páginas. Recomiendo científicamente publicar con alcance declarado: clasificación completa qubit, sharpness SLD/chi mínima/triangular bajo presupuesto y lower BKM/Umegaki adicional; no encontré objeción material pendiente. Importancia AIRR6.1/10, global Millennium5.9/10 y técnica8.7/10 son juicios distintos, no promedio ni notas heredadas. El lower BKM no es upper ni exactitud irrestricta, información mutua ordinaria o capacidad. Prioridad abierta y utilidad operacional no demostrada. Configuración solicitada Astra xhigh; identidad y esfuerzo efectivos no atestados. Participación de Codex, contexto952/998/1006/1010/1031/1042 y filesystem compartidos; posible sesgo y ninguna independencia verificada. Accept representa esta recomendación científica, no aceptación editorial. Este contenido carece de identidad pública vinculada y no debe importarse como un registro completo.',
 'strengths':['Clasificación qubit y envolvente exacta con regularización de pesos cero y cuantificadores de igual referencia explícitos.','La construcción rank-two amplía el rango exacto SLD/chi mínima/triangular a M=d(2d-1)/2; se verifican marginal, presupuesto y límites.','El cálculo logarítmico BKM independiente produce P=d(d-1), un perfil presupuestado combinado con Bell y una mejora negativa de factor d-1 entre dos lowers.','Cinco verificadores con salida idéntica, cuatro gaps intervalares contrastados y controles propios exactos y complejos; PDF y fuentes íntegros.'],
 'weaknesses':[x['id']+': '+x['finding'] for x in findings],
 'potential_errors':['No se identificó un error matemático confirmado. La búsqueda dirigida no excluye un teorema anterior cubriente o prioridad compartida.','Sería incorrecto transferir la exactitud SLD a BKM, interpretar el factor d-1 como cociente de óptimos, o convertir el resultado en información mutua ordinaria/capacidad. El PDF inspeccionado no hace esas afirmaciones.','Sería incorrecto llamar independientes a este contexto o a la auditoría1044, o tomar los controles finitos como prueba universal.','Las objeciones1031-O1 y O2 están resueltas en el PDF actual: primal Doeblin hermítico/dual con igualdad, y NPT de la base restringida al argumento SLD/chi mínima. Sus originales permanecen intactos.'],
 'strong_novelty_candidates':['Clasificación completa qubit y envolvente, en sus cuantificadores exactos; prioridad sujeta a contraste bibliográfico no exhaustivo.','Cap M=d(2d-1)/2 exacto SLD/chi mínima/triangular: mejora geométrica incremental con mayor referencia, no nueva teoría.','Lower BKM/Umegaki P=d(d-1) y perfil combinado con Bell: contenido cuantitativo sustantivo, no upper ni óptimo demostrado.'],
 'unresolved_material_objections':[]
}
put('ARR-CONTENT-UNBOUND1048.json',arr)
put('ARR-BINDING-LIMITS1048.json',{
 'utc':now,'purpose':'Content-only projection of the same1048 report, not another assessment or grade',
 'source_report':'REVIEW1048.txt','source_report_sha256':reportsha,'source_verdict':'verdict1048.json','source_verdict_sha256':sha(ROOT/'verdict1048.json'),
 'reviewed_pdf_sha256':pdfsha,'content_sha256':sha(ROOT/'ARR-CONTENT-UNBOUND1048.json'),
 'not_native_importable':True,'absent_identity_fields':['paper_id','version','version_id','assessment_id','source_response_sha256'],
 'reason':'No exact public1047 record identity was supplied or invented. No binding to old1005v1, no fabricated v2, no synthetic Paper object for validation.',
 'recommendation_mapping':'recommend_publication_with_declared_scope -> accept; scientific recommendation only, not Accepted editorial status.',
 'score_mapping':'millennium_score=5.9 and rounded overall_stars=6; importance6.1 and technical8.7 remain separate in summary and full verdict. Criteria are diagnostic, not averaged.',
 'provenance_mapping':'model_id explicitly unattested; independence=involved_in_manuscript. Runtime and operator-evidence fields omitted rather than fabricated.',
 'source_schema_read_only':r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\scripts\assessmentlib.py',
 'source_schema_sha256':sha(Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\scripts\assessmentlib.py')),
 'validation':'validate_content1048.py checks the content subset only; full native identity validation is intentionally not claimed.'
})
print(json.dumps({'created_metadata':True,'report_sha256':reportsha,'verdict_sha256':sha(ROOT/'verdict1048.json'),'utc':now},indent=2))
