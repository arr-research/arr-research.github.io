from pathlib import Path
import json,hashlib,datetime,shutil,sys
R=Path(__file__).resolve().parent
BASE=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
P=BASE/'papers/2026/10/56/ARR-2026-564FZ70CSN83KACD/versions/v3'
C=Path(r'C:\Trabajo\airr\2026-10-28_cq1168-review')
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_cq1168-review')
STAGED=Path(r'C:\Trabajo\airr\2026-10-28_cq1176-publication\STAGED1176.json')
PH='6d4f64b0b9423852ad2831e551edf467a6fbca14d30991b517084978573455c5'
RH='b7b317a25a901ae1201bf490832dff576de9d2b7ba8696b3de220535ff741007'
VH='5025584653155c16566fe8f5857c36db007cf47a5ff9a8bb828761164394369e'
MH='c23cec64ad534bcac4cdf761218ac7bb4c30c51b5a43d081cef11b92cfe8ae7c'
WHEN='2026-10-28T01:14:36.368051+00:00'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,obj):
    p=R/name;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def inv(root):
    return [{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file()]
def check_originals():
    ic,id_=inv(C),inv(D)
    assert ic==id_ and len(ic)==1070
    assert sha(C/'REVIEW1168.txt')==RH and sha(C/'verdict1168.json')==VH and sha(C/'MANIFEST1168.json')==MH
    table={x['path']:x for x in ic}
    manifest=json.loads((C/'MANIFEST1168.json').read_text(encoding='utf-8'))
    assert len(manifest['files'])==1068
    for row in manifest['files']: assert row==table[row['path']]
    assert set(table)=={x['path'] for x in manifest['files']}|{'MANIFEST1168.json','C_D-CLOSURE1168.json'}
    return {'utc':utc(),'C_D_identical':True,'files':len(ic),'manifest_payloads':1068,'inventory_sha256':hashlib.sha256(json.dumps(ic,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'manifest_sha256':MH,'report_sha256':RH,'verdict_sha256':VH}

assert not (R/'model-response.json').exists(),'Preserve existing response; no silent overwrite'
original_check=check_originals()
dump('ORIGINALS-INITIAL1177.json',original_check)
for name in ['REVIEW1168.txt','verdict1168.json','PROVENANCE1168.json','READINGS1168.json','INCIDENTS1168.json','REPRODUCTION1168.json','MANIFEST1168.json','C_D-CLOSURE1168.json']:
    target=R/'original1168'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(D/name,target)
assert sha(R/'original1168/REVIEW1168.txt')==RH and sha(R/'original1168/verdict1168.json')==VH
meta_raw=(P/'metadata.json').read_bytes();meta=json.loads(meta_raw)
assert meta['id']=='ARR-2026-564FZ70CSN83KACD' and meta['version']=='v3'
assert meta['record_id']=='arr:record:a623fe70-3335-40e6-a637-b365287b12bd'
assert meta['version_id']=='arr:version:f8d02e4f-50fa-41f8-9113-4c3c832d0618'
assert meta['supersedes_version_id']=='arr:version:12e58b0b-3848-46ef-8dd1-656797e934f5'
assert meta['source_of_truth']=='paper.pdf' and meta['integrity']['canonical_sha256']==PH
assert sha(P/'paper.pdf')==PH and (P/'paper.pdf').stat().st_size==452673
(R/'local-record').mkdir(exist_ok=True)
(R/'local-record/metadata-v3.initial.json').write_bytes(meta_raw)
shutil.copyfile(STAGED,R/'local-record/STAGED1176.json')
tools=['assessmentlib.py','arrlib.py','ratinglib.py','prepare_model_assessment.py','record_model_assessment.py']
guards=[P/'metadata.json',P/'paper.pdf',BASE/'registry/model-assessments.json']+[BASE/'scripts'/x for x in tools]
dump('READONLY-SOURCES-INITIAL1177.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in guards])
v=json.loads((D/'verdict1168.json').read_text(encoding='utf-8'))
assert v['assessed_at']==WHEN
assert [v[x] for x in ['scientific_importance_airr_0_10','overall_millennium_0_10','technical_quality_0_10']]==[7.3,7.0,9.0]
mapping={'correctness_confidence':'correctness_confidence','rigor':'rigor_and_completeness','novelty':'novelty_relative_to_checked_sources','significance':'significance_if_correct','reproducibility':'reproducibility_or_inspectability'}
criteria={k:{'stars':v['criteria'][old]['rating_1_5'],'basis':v['criteria'][old]['basis']} for k,old in mapping.items()}
summary=('Serialización1177 del mismo juicio completo1168, sin nueva revisión, nota ni voto. PDF exacto de21p/452673bytes. '
 'Importancia científicaAIRR7.3/10; globalMillennium7.0/10 (7estrellas); calidad técnica9.0/10: juicios distintos, no promediados ni probabilidades. '
 'Se conservan cinco criterios4/5, sus bases yO1–O5. Publicación científica con alcance declarado: accept no significa Accepted ni decisión editorial. '
 'No se confirmó un fallo matemático material; prioridad bibliográfica abierta. La fecha assessed_at es la original1168. '
 'OpenAI Codex, participación previa, contexto952 reutilizado, filesystem compartido y exposición a notas previas; posible sesgo, no fresh/blind/independent ni revisión humana. '
 'GPT-6 Astra xhigh fue solicitado; identidad y esfuerzo efectivos, aislamiento e independencia no atestados: model_id unknown. '
 'Auditorías de componentes y valoraciones de otros PDFs no son votos actuales. No se acredita gate de dos modelos identificados. '
 'V3 y su UUID son candidato local, sin nuevo expediente nativo ni publicación acreditada. La frase de§A sobre evaluación pendiente es histórica al congelado. '
 'Informe1168 íntegro y anexos originales acompañan esta proyección; no se atribuyen nuevas lecturas o ejecuciones científicas al serializar.')
strengths=[f"{f['id']} (pp.{','.join(map(str,f['pages']))}). {f['claim']}. {f['basis']}" for f in v['findings']]
strengths += ['Base original de importancia científica7.3/10: '+v['scientific_importance_basis'],'Base original de valoración global7.0/10: '+v['overall_basis'],'Base original de calidad técnica9.0/10: '+v['technical_quality_basis']]
weaknesses=[f"{o['id']} [{o['severity']}; pp.{','.join(map(str,o['pages']))}; {o['status']}]. {o['title']}: {o['statement']} Resolución/alcance: {o['pending_resolution']}" for o in v['objections']]
weaknesses+=['Límite del informe, no penalización automática de la IA: contexto involucrado y reutilizado, participación previa, exposición a notas y filesystem compartido; identidad/esfuerzo efectivos e independencia desconocidos. No se ha aislado ni repetido el juicio para mejorar la nota.']
potential=[h['issue']+': '+h['current_state'] for h in v['historical_issues']]
potential+=[
 'Incidente propioI2 de1168: el constructor inicial de mpmath produjo producto tensorial nulo y fallo singular deA; se conservó código/salida/plan inicial y se corrigió solo el helper, repitiendo los mismos casos, precisión y tolerancia. Es error del control del revisor, no refutación del manuscrito ni nueva ejecución1177.',
 'Adversos preservados en1168: primer protocolo con fondo marcado fallido, selector de máximo solapamiento, regularizadores alternativos, parejas finitas bajo el comparador clásico y camino n=k. Los replays acotados y controles de alta precisión no son pruebas universales ni aritmética independiente.',
 'O1 permanece abierta: no se excluye una fuente general cubriente; Lee–Makur full text no inspeccionado. La lectura de HircheA.1 y los demás niveles de lectura pertenecen a1168; no hay nueva búsqueda bibliográfica1177.',
 'Incidentes de visualización truncada y consulta de proceso ya finalizado fueron documentados y recuperados en1168. No se borran de los anexos originales ni se convierten en evidencia científica adicional.'
]
novelty=[
 'Candidata relativa a las fuentes revisadas en1168: criterio necesario y suficiente de soporte para todos los canalesCQ finitos, con familia de entradas independiente del canal y divergencias de entrada/salida/medida tendiendo a log2 para cada canal fijo. Prioridad mundial no certificada.',
 'Candidata relativa: realización clásica uniforme sobre canales de Doeblin cero a n fijo, separada de la convergenciaCQ puntual. Las herramientas de simplex, Schur, resolventes y DPI son previas; no se atribuye novedad a ellas por sí solas.',
 'Candidata relativa: separación finita de Umegaki completo respecto de traza con hipótesis fieles, lectura binaria conjunta y denominador cuántico. No es una fórmula para capacidad, ventaja experimental robusta o exactitud para todo Petz.'
]
response={'paper_id':meta['id'],'version':meta['version'],'version_id':meta['version_id'],'canonical_sha256':PH,'provider':'OpenAI','model_id':'unknown','assessed_at':v['assessed_at'],'prompt_version':'ARR-ASSESS-1.0','independence':'involved_in_manuscript','recommendation':'accept','millennium_score':v['overall_millennium_0_10'],'overall_stars':v['overall_stars'],'criteria':criteria,'summary':summary,'strengths':strengths,'weaknesses':weaknesses,'potential_errors':potential,'strong_novelty_candidates':novelty,'unresolved_material_objections':v['confirmed_material_objections']}
dump('model-response.json',response)
sys.path.insert(0,str(BASE/'scripts'))
from assessmentlib import normalize_model_response,validate_assessment,source_hash,canonical_json
from arrlib import Paper,sha256
normalized=normalize_model_response(response)
errors=validate_assessment(normalized,[Paper(P,meta)])
canonical=canonical_json(response)
(R/'model-response.canonical.json').write_bytes(canonical)
validation={'utc':utc(),'scope':'format and local artifact binding only, not a scientific review or publication validation','status':'pass' if not errors else 'fail','official_functions':['assessmentlib.normalize_model_response','assessmentlib.validate_assessment','assessmentlib.source_hash','assessmentlib.canonical_json','arrlib.Paper','arrlib.sha256'],'errors':errors,'response_byte_sha256':sha256(R/'model-response.json'),'response_canonical_sha256':source_hash(response),'canonical_file_sha256':sha256(R/'model-response.canonical.json'),'normalization_assessment_id':'generated by official function in memory for validation only; discarded, never persisted or registered','record_id':meta['record_id'],'paper_id':meta['id'],'version_id':meta['version_id'],'version':meta['version'],'pdf_actual_sha256':sha256(P/'paper.pdf'),'pdf_actual_bytes':(P/'paper.pdf').stat().st_size,'pdf_pages_from_original1168':21,'metadata_sha256':hashlib.sha256(meta_raw).hexdigest(),'assessed_at_unchanged':WHEN,'no_registry_write':True,'no_scientific_checks_run':True,'summary_characters':len(summary),'list_lengths':{key:[len(x) for x in response[key]] for key in ['strengths','weaknesses','potential_errors','strong_novelty_candidates']}}
dump('VALIDATION1177.json',validation)
assert not errors,errors
assert sha256(R/'model-response.canonical.json')==source_hash(response)
dump('BINDING1177.json',{
 'task':'1177','operation':'faithful serialization only of closed full review1168; same scientific judgment, not another vote',
 'serialized_at':utc(),'original_assessed_at':WHEN,
 'source_report_sha256':RH,'source_verdict_sha256':VH,'source_review_manifest_sha256':MH,
 'local_record':{'paper_id':meta['id'],'record_id':meta['record_id'],'version':meta['version'],'version_id':meta['version_id'],'supersedes_version_id':meta['supersedes_version_id'],'metadata_source':str(P/'metadata.json'),'metadata_snapshot':'local-record/metadata-v3.initial.json','metadata_sha256':hashlib.sha256(meta_raw).hexdigest(),'pdf_source':str(P/'paper.pdf'),'pdf_sha256':PH,'bytes':452673,'pages_from_original_review':21,'uuid_origin':'actual local new_version.py candidate per metadata/STAGED1176; not evidence of public or native publication'},
 'publication_context':{'source':'local-record/STAGED1176.json and parent instruction; no fresh service query','local_unpublished_candidate':True,'new_native_case':None,'parent_native_case':'SUB-6FE1A863DE23202D','author_POST_reported_result':'429; reconciled no new child','parent_status_reported':'changes_requested, author_requested_major_revision','quota_reported':'10 in24h; next slot estimate04:26UTC, not independently queried','server_scan_for_v3':None,'exact_version_release_permission_timestamp':None,'no_alternative_route_used':True,'no_commit_PR_push_release_performed':True,'historical_pdf_appendix_phrase':'Assessment pending described the freeze before1168; no PDF edit or new reading here.'},
 'field_mappings':{
  'paper_id/version/version_id/canonical_sha256':'Copied from verified actual localv3 metadata; PDF bytes independently hashed without scientific rereading. record_id retained here because response schema lacks that field.',
  'provider/model_id/independence':'OpenAI; unknown effective model; involved_in_manuscript, as1168 provenance. Requested Astraxhigh remains only a request in summary; no runtime_provenance fabricated.',
  'assessed_at':'Copied exactly from verdict1168, not serialization time.',
  'prompt_version':'ARR-ASSESS-1.0 describes this later format; it does not claim the original1168 assessment was prompted with a new review.',
  'millennium_score/overall_stars':'Copied7.0/7 from1168; no arithmetic combining other scores.',
  'criteria':mapping,
  'criteria_values_and_bases':'Each criterion4 and basis copied verbatim from verdict1168.',
  'importance_and_technical_quality':'Separate original7.3/9.0 placed in summary; full original bases plus overall basis retained as labelled entries in strengths because schema has no separate numeric fields. Not folded into millennium_score.',
  'recommendation':'Original recommend_publication_with_declared_scope -> compatible accept, already specified by1168. Scientific recommendation only, not Accepted/editorial decision or gate satisfied.',
  'summary':'Condensed faithful provenance/scope/context, with local binding status; no new scientific judgment.',
  'strengths':'F1-F6 original claims/bases/page lists, plus exact original bases of the three distinct judgments.',
  'weaknesses':'O1-O5 statements, severities, page lists, status and pending resolution copied, plus known review-context limitation.',
  'potential_errors':'Original historical corrections and reviewer incidents/adverse controls summarized without relabelling them as new manuscript errors; complete originals attached.',
  'strong_novelty_candidates':'Condensed candidates already identified in1168 with priority/tool-prior limitations intact, no new novelty search.',
  'unresolved_material_objections':'Original empty confirmed-material list copied; O1-O5 remain in weaknesses/potential_errors, not suppressed.'
 },
 'originals_attached':[x['path'] for x in inv(R/'original1168')],
 'complete_original_dossier_paths':[str(C),str(D)],'complete_dossier_files':1070,'no_duplicate_full_inputs_required':True,
 'raw_response_sha256':sha(R/'model-response.json'),'canonical_response_sha256':source_hash(response),'canonical_definition':'assessmentlib.canonical_json: UTF8 JSON sorted keys, ensure_ascii=False, separators comma/colon; source_hash=SHA256 thereof. Raw pretty UTF8+LF byte hash is distinct. arrlib.sha256 used to verify files.',
 'validation':'VALIDATION1177.json','operator_controlled_fields_omitted':['assessment_id','source_response_sha256','runtime_provenance','review_context','intake_source'],
 'no_ids_invented':True,'no_native_record_claim':True,'no_new_scientific_reading_or_reproduction':True,'no_new_score_or_recommendation':True,'originals_immutable':True
 })
dump('PROVENANCE1177.json',{'utc':utc(),'scope':'serialization only','origin':'original1168 report/verdict/provenance/readings/incidents/reproduction/manifest/closure byte copies','original_assessed_at':WHEN,'serialization_time_location':'BINDING1177.json serialized_at','effective_model_id':'unknown','effective_effort':'unknown','requested_configuration':'GPT-6 Astra xhigh; request only','independence':'involved_in_manuscript','context_reused':True,'fresh_or_blind':False,'shared_filesystem':True,'prior_score_exposure':True,'no_new_sources_or_scientific_controls':True,'official_validator_read_only':True,'no_registry_or_Git_or_publication':True,'format_tools':{name:sha(BASE/'scripts'/name) for name in tools}})
dump('INCIDENTS1177.json',{'utc':utc(),'items':[{'id':'F1','kind':'display_limit','description':'Initial broad metadata output was truncated because of its long attached-file license list. Identifiers, integrity, local publication status and full metadata bytes were subsequently read programmatically and snapshotted. No scientific reading or metadata alteration.'},{'id':'H1','kind':'preserved1168','description':'All original1168 incidents/adverses remain attached unchanged; no new scientific rerun.'}], 'schema_errors':errors,'no_judgment_changes':True})
print(json.dumps({'status':'serialized_and_format_validated','raw_response_sha256':sha(R/'model-response.json'),'canonical_response_sha256':source_hash(response),'summary_characters':len(summary),'errors':errors}))
