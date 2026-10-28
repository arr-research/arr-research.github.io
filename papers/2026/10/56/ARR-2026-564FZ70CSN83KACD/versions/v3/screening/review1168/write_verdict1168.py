from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads((R/'PROVENANCE1168.json').read_text(encoding='utf-8'))
findings=[
 {'id':'F1','pages':[2,3,4,5],'claim':'Cota armónica para todo Petz operator-convexo normalizado y exactitud en las cinco clases enumeradas','result':'supported_within_review','basis':'Cancelación cíclica en Hilbert–Schmidt complejo, extremo cuadrático conservado, pesos cero tratados por DPI; testigos simplex y límites locales ordenados. No se extiende exactitud a todo Petz.'},
 {'id':'F2','pages':[5,6,7,8,9],'claim':'Reducción binaria clásica y testigos finitos con lectura binaria','result':'supported_within_review','basis':'Entrada binaria, hipótesis binaria y salida binaria son restricciones distintas. Bloques fieles y marginal real; denominador cuántico, orientación y complementos mantenidos. Modo inactivo ausente en n2 y calificado para n>=3.'},
 {'id':'F3','pages':[9,10,11,12,13],'claim':'eta_D^c de cualquier canal CQ finito es1 iff intersección de soportes cero','result':'supported_within_review','basis':'Dirección positiva reemplazante previa. Converse: W inyectiva en suma de soportes, Z*T^+Z=S también después de blanqueo por factorización, resolvente en ranZ, complemento de Schur positivo y proyector gráfico normalizado. Para cada canal fijo, Di,Do,Db->log2.'},
 {'id':'F4','pages':[12,13],'claim':'Separación finita respecto de traza y límites de uniformidad/LOCC','result':'supported_within_review','basis':'Pareja pura no ortogonal k16 con Db/Di>0.66199617>2/sqrt13; efecto concreto NPT. T0=I en familia binaria real, condicionamiento de S controla el fallo uniforme del testigo; no se afirma imposibilidad de toda medida alternativa.'},
 {'id':'F5','pages':[13,14,15,16,17],'claim':'Uniformidad sobre canales clásicos de Doeblin cero a n fijo','result':'supported_within_review','basis':'Identidades en soportes propios y norma inversa aplicada a z independiente del menor peso; mínimo propio por raíz Schur/interlazado; cotas p/q suman usando sum t_y=n. No uniforme en n o recursos.'},
 {'id':'F6','pages':[17,18,19,20,21],'claim':'Límites operacionales, fixed-point decay y procedencia','result':'appropriately_delimited','basis':'No fórmula general1-d, no prioridad acreditada, no allPetz exactitud, no capacidad/robustez/LOCC general. Distinto segundo estado de entropía hacia expectativa. Adversos e incidencias anteriores conservados.'}
]
objections=[
 {'id':'O1','severity':'moderate','material_mathematical_error_established':False,'pages':[1,2,9,10,11,12,13,20,21],'title':'Cobertura bibliográfica y prioridad','statement':'No se ha excluido un teorema general cubriente que haga equivalentes contracción completa Umegaki estricta y componente CP reemplazante positiva; Lee–Makur full text no inspeccionado. La búsqueda dirigida no prueba prioridad mundial.','status':'open_priority_reservation','pending_resolution':'Comparación literal con cualquier fuente cubriente que aparezca; modificar novedad si procede. No fuente cubriente identificada en pasajes efectivamente leídos.'},
 {'id':'O2','severity':'moderate','material_mathematical_error_established':False,'pages':[7,8,9,11,12,13,16,17,18],'title':'Cuantificadores puntuales y coste de aproximación','statement':'Dimensión de referencia fija no implica marginal, piso espectral o coste fijo. Condicionamiento~4k2^k, q~2^-k/k; construcción CQ puntual en canal y clásica uniforme solo a n fijo.','status':'acknowledged_scope_limit','pending_resolution':'Ninguna corrección matemática exigida para alcance actual; ampliarlo requeriría nuevos resultados de recursos.'},
 {'id':'O3','severity':'moderate','material_mathematical_error_established':False,'pages':[7,11,12,13,17,18],'title':'Lectura conjunta y sentido operacional del cociente','statement':'Denominador cuántico, efecto dependiente de canal/pareja/k, complemento y orientación esenciales. Efecto CQ concreto NPT, no LOCC; estados SEP no eliminan ese recurso. No comparación universal de capacidad o protocolos a iguales recursos.','status':'acknowledged_scope_limit','pending_resolution':'Conservar estas restricciones; no se exige demostrar una ventaja operacional no reclamada.'},
 {'id':'O4','severity':'minor','material_mathematical_error_established':False,'pages':[12,17,19,20],'title':'Alcance limitado de verificación computacional','statement':'Replay e intervalos acotados, biblioteca/contexto compartidos; controles propios de alta precisión diagnósticos. No toda campaña ni aritmética independiente ni prueba formal.','status':'review_confidence_limit','pending_resolution':'Mantener recibos, alcance y adversos públicos junto al informe. No presentar coincidencias JSON como prueba universal.'},
 {'id':'O5','severity':'minor','material_mathematical_error_established':False,'pages':[19,20,21],'title':'Carga de trazabilidad histórica','statement':'Muchos dossiers e incidencias dificultan localizar la evidencia actual. Identificadores técnicos no equivalen a revisores independientes.','status':'nonblocking_presentation_suggestion','pending_resolution':'Una tabla externa teorema/archivo/replay facilitaría lectura; no exige modificar PDF para sostener pruebas.'}
]
v={
 'schema':'review1168-scientific-verdict-1.0',
 'assessment_id_local':'1168',
 'assessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'assessment_kind':'one_full_exact_manuscript_scientific_review',
 'manuscript':{'title':'Common support and complete contraction with quantum side information','author':'Lluis Eriksson','pdf_path':'input/manuscript.pdf','pdf_sha256':'6d4f64b0b9423852ad2831e551edf467a6fbca14d30991b517084978573455c5','bytes':452673,'pages':21,'manifest_sha256':'0614ff2eddca97659c85577629718c6c82c6a3cfe0203a0ca6fec2f848774100','main_tex_sha256':sha(R/'input/main.tex'),'cq_section_sha256':sha(R/'input/sections/cq-support.tex'),'general_section_sha256':sha(R/'input/sections/general-support.tex')},
 'requested_configuration':p['requested_configuration'],
 'observed_configuration':p['observed_configuration'],
 'review_context':p['context'],
 'scientific_importance_airr_0_10':7.3,
 'scientific_importance_basis':'Relevancia del criterio necesario y suficiente para toda la clase CQ finita, testigo universal de entradas con límite positivo y lectura binaria, separación de traza y uniformidad clásica. No priorización mundial acreditada ni robustez/capacidad/aplicación experimental demostrada.',
 'overall_millennium_0_10':7.0,
 'overall_stars':7,
 'overall_basis':'Juicio global según anclaje excepcional de la escala pública: criterio constructivo amplio y separación concreta con pruebas inspeccionables. No media de criterios, no probabilidad ni comparación numérica heredada. No evidencia suficiente para anclajes field-shaping/historic.',
 'technical_quality_0_10':9.0,
 'technical_quality_basis':'Alta precisión en definiciones, rango, pseudoinversas, fidelidad, proyector, límites y adversos, respaldada por inspección analítica y controles acotados. No formalización ni biblioteca independiente ni auditoría bibliográfica completa. No equivale a probabilidad de corrección.',
 'criteria':{
   'correctness_confidence':{'rating_1_5':4,'basis':'Pruebas principales reconstruidas y controles concordantes; límites de revisión, sin certificado formal o independencia.'},
   'rigor_and_completeness':{'rating_1_5':4,'basis':'Cuantificadores, rangos, normalización y límites correctamente tratados; algunas pruebas condensadas y ampliaciones expresamente excluidas.'},
   'novelty_relative_to_checked_sources':{'rating_1_5':4,'basis':'Criterio CQ/testigo/separación no cubiertos por pasajes consultados; prioridad pendiente, LM full text y posible teorema general cubriente no descartados.'},
   'significance_if_correct':{'rating_1_5':4,'basis':'Clarifica una clase completa de canales y distingue Umegaki de traza; utilidad física condicionada por recursos y falta de robustez.'},
   'reproducibility_or_inspectability':{'rating_1_5':4,'basis':'Fuentes y adversos conservados, replay acotado y controles propios; no todos los scripts ni segunda aritmética independiente.'}
 },
 'no_implicit_criterion_average':True,
 'no_prior_score_inheritance':True,
 'grade_target':None,
 'scientific_recommendation':'recommend_publication_with_declared_scope',
 'compatible_recommendation_enum_if_later_serialized':'accept',
 'recommendation_basis':'No objeción material matemática confirmada en la inspección; mantener O1-O5 y procedencia visibles. Es recomendación científica de esta única evaluación, no Accepted, decisión editorial o gate nativo satisfecho.',
 'editorial_decision':None,
 'confirmed_material_objections':[],
 'findings':findings,
 'objections':objections,
 'historical_issues':[
  {'issue':'Modo inactivo n2','current_state':'Calificado n>=3; n2 tiene multiplicidad cero. No reaparece objeción histórica.'},
  {'issue':'Explicación de coste por Gram1152','current_state':'Corregida en sección6.5: T0=I, pueden divergir condicionamientoS yA^-1Z. Error original preservado.'},
  {'issue':'Recibo supuesto de stop1152','current_state':'Corrección1164 leída; narra terminal posterior mismo handle. Hash de salida lenta original desconocido; no se inventa y no se observó ahora ese evento.'}
 ],
 'reading_scope':{'all_pdf_pages_read':True,'all_sources_read':['main.tex','sections/cq-support.tex','sections/general-support.tex'],'visual_pages':21,'all_929_auxiliary_files_read_line_by_line':False,'primary_readings':'READINGS1168.json','source_coverage_limited':True,'lee_makur_full_text_read':False,'hirche_appendix_A1_read_this_review':True,'whole_hirche_article_audited':False,'general_quantum_covering_theorem_excluded':False},
 'reproduction':{'status':'pass','receipt':'REPRODUCTION1168.json','inherited_scope':'12checkers + CQexact + 7intervalcases','own_scope':'4exact geometry +8ambient120digit controls','own_first_implementation_failure_preserved':True,'independent_arithmetic':False,'universal_theorem_proved_by_controls':False},
 'confidence_limits':['No fresh/blind/independent context; prior participation and score exposure','Effective model/effort unknown','Directed primary literature search only','No formal proof or independent arithmetic implementation','No empirical robustness/capacity or optimal resource claim'],
 'report':{'path':'REVIEW1168.txt','sha256':sha(R/'REVIEW1168.txt'),'bytes':(R/'REVIEW1168.txt').stat().st_size},
 'attachments':{'provenance':'PROVENANCE1168.json','readings':'READINGS1168.json','incidents':'INCIDENTS1168.json','reproduction':'REPRODUCTION1168.json','final_input_reverification':'INPUT-FINAL1168.json','manifest':'MANIFEST1168.json','closure':'C_D-CLOSURE1168.json'},
 'native_arr_paper_id':None,'native_arr_version_id':None,
 'no_publication_performed':True,'no_new_agents_or_chats':True,'no_resampling_or_grade_restart':True
}
(R/'verdict1168.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'report_sha256':sha(R/'REVIEW1168.txt'),'verdict_sha256':sha(R/'verdict1168.json'),'scores':[v['scientific_importance_airr_0_10'],v['overall_millennium_0_10'],v['technical_quality_0_10']]}))
