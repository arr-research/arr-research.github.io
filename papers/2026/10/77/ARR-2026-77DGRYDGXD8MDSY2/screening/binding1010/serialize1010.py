"""Format-only serialization of the same review1006. No reassessment or publication."""
from pathlib import Path
import datetime,hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
REPO=Path('C:/Trabajo/airr-publicacion/reviewed-publications-20261026')
OLD=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp1006-review')
HISTORY=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review')
PDF_SHA='b4728f44f7af59809be26e0eba957336695ff34cfc3cb10c17fcfa06ffb93381'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    with (ROOT/name).open('x',encoding='utf-8') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
expected={'REVIEW1006.txt':'b179331da60c87e842db4156280f9ac90430de85d4daa0a5e18073c9f4ce15eb',
 'verdict1006.json':'481786d96a45ca2b393b11cd569d3ee3605207b4db50ce09c9a9fba9a8cf5732',
 'MANIFEST1006.json':'6c26d3f926ada0834dfb237f040ced2035141a371fddccb1e2f7d5a0695422e4'}
assert all(sha(OLD/n)==h for n,h in expected.items())
manifest=json.loads((OLD/'MANIFEST1006.json').read_text(encoding='utf-8'))
assert all(sha(OLD/x['path'])==x['sha256'] for x in manifest['files'])
assert sha(OLD/'input'/'main.pdf')==PDF_SHA
v=json.loads((OLD/'verdict1006.json').read_text(encoding='utf-8'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
mapping={'correctness_confidence':'correctness_confidence','rigor':'rigor_and_completeness','novelty':'novelty_relative_to_sources_checked','significance':'significance_if_claims_hold','reproducibility':'reproducibility_or_independent_inspectability'}
criteria={target:{'stars':v['five_criteria'][source]['stars_1_5'],'basis':v['five_criteria'][source]['basis']} for target,source in mapping.items()}
summary=(
 'Serialización posterior1010 del MISMO informe1006, fechado2026-10-27T15:14:22.419803+00:00; no nueva revisión, nota ni voto. '
 'ARR-ASSESS-1.0 designa sólo este formato y assessed_at la serialización. '
 '1006 recomienda publicar el PDF exacto1005 dentro de su alcance: O1–O5 resueltas, sin nuevas objeciones condicionantes. '
 'accept es esa recomendación científica, NO un estado Accepted ni decisión editorial. '
 'Global Millennium4,4/10 (Strong,4estrellas); importancia científica4,3/10; calidad técnica8,6/10: ejes distintos, sin promedio. '
 'La aportación especializada es la constante completa exacta y su construcción; el alcance e importancia amplios y la prioridad mundial no están acreditados. '
 'La calidad técnica se apoya en la cota universal, familia explícita, límites fieles ordenados y certificados racionales. '
 'Participación sustancial de OpenAI Codex en derivación/escritura/trabajo numérico declarada; contexto952/998 y filesystem compartidos. '
 'Se solicitó GPT-6 Astra xhigh; identidad/esfuerzo efectivos, aislamiento e independencia no atestados. '
 'El informe íntegro REVIEW1006.txt y BINDING1010.json deben acompañar esta proyección.998 pertenece al PDF995 anterior, no es otro voto sobre1005.'
)
response={
 'paper_id':'ARR-2026-77DGRYDGXD8MDSY2','version':'v1','version_id':'arr:version:6a10a005-19c7-4d57-91e1-f7bbf66cb3ac','canonical_sha256':PDF_SHA,
 'provider':'OpenAI','model_id':'unattested-effective-model; requested GPT-6 Astra xhigh via Codex',
 'assessed_at':now,'prompt_version':'ARR-ASSESS-1.0','independence':'unknown',
 'recommendation':'accept','millennium_score':v['overall_millennium_0_10'],'overall_stars':v['overall_public_whole_stars'],'criteria':criteria,'summary':summary,
 'strengths':[
  '1006 inspeccionó la prueba de la cota armónica para todos los generadores de Petz operator-convexos no afines, estados fieles, pesos positivos y referencias finitas, sin identificar un error invalidante.',
  'La familia qubit–qutrit y los límites ordenados muestran el supremo3lambda²/(1+2lambda) para SLD, chi-cuadrado mínimo y Petz triangular; la optimalidad uniforme no se atribuye a cada generador.',
  '1006 verificó los21payloads congelados en C/D, los10artefactos locales sin cambios,13archivos públicos seleccionados y los3verificadores públicos. Reprodujo9identidades,9pares a75dígitos,2certificados racionales y4controles exactos focalizados.',
  'El suplemento está fijado al commit f0b3642b196b9de6d51b31cca49a69818522ee91, con manifiesto y dependencias. Las diferencias LF/CRLF y el README público distinto están declarados;998 permanece íntegro.'
 ],
 'weaknesses':[
  'O1 RESUELTA en1005,p.7: el URI real fija el commit, el manifiesto y13archivos públicos coinciden, y3scripts descargados reproducen las salidas. Sólo se comprobaron las entradas pertinentes seleccionadas; no se avalan científicamente988 ni las extensiones posteriores.',
  'O2 RESUELTA en1005,pp.7–8: cita George–Tomamichelv3 y distingue base fija, coeficiente ordinario y completo restringido. Se contrastaron pasajes seleccionados; la prioridad mundial sigue sin establecerse.',
  'O3 RESUELTA en1005,p.5: ahora0<xi<1 garantiza autovalores positivos; el control exacto del límite de regularización pasa. El orden t→0,xi→0,e→0 permanece explícito.',
  'O4 RESUELTA en1005,pp.5–6: combinación convexa finita, pesos no negativos normalizados y eliminación de átomos de peso cero explícitos; el caso r=0 está bien definido.',
  'O5 RESUELTA, originalmente opcional, en1005,p.5: comparación ordinaria lambda² y1/4 frente a3/8 añadida y contrastada con Hiai–Ruskai para T=lambdaI.',
  'Las herramientas de representación, convexidad y cálculo espectral son conocidas. La búsqueda bibliográfica fue dirigida y parcial, con lecturas anteriores de998 reutilizadas; no certifica originalidad mundial.',
  'No se determinan el coeficiente completo de entropía relativa o información mutua, la dimensión mínima suficiente de referencia, la exactitud en dimensiones mayores ni aplicaciones operacionales amplias.',
  'El contexto952/998 y el filesystem se comparten, y hubo participación sustancial de Codex. Identidad/esfuerzo efectivos e independencia no están atestados. unknown no significa ausencia de participación ni revisión independiente.',
  '998 evaluó otro PDF y1006 es la única evaluación actual.1010 sólo serializa1006. Las extensiones997/1003 no se leyeron ni evaluaron; nombres y hashes del listado público no constituyen revisión.',
  'La evaluación conserva incidentes de preparación PDF y diferencias esperadas de transporte. No hubo fallos matemáticos, discrepancias de hashes ni fallos en los tres verificadores públicos; el detalle íntegro permanece en el informe y registros1006.'
 ],
 'potential_errors':[
  '1006 no identificó errores centrales ni nuevas objeciones condicionantes. Eso no constituye verificación formal ni arbitraje humano independiente; la inspección del modelo puede no detectar un error.',
  'Los diagnósticos finitos y la reproducción racional no reemplazan las pruebas universales y los argumentos de límite ordenado. No se afirma optimalidad a partir de optimizadores ni una campaña computacional exhaustiva.',
  'Un antecedente que cubra los mismos cuantificadores podría afectar la novedad; los pasajes consultados no certifican su ausencia en toda la literatura. La búsqueda y sus límites constan en READINGS1006.json.',
  'La optimalidad uniforme sobre Petz no fija la constante de cada generador; ordenar métricas no ordena sus cocientes. El resultado no debe trasladarse a BKM, entropía relativa, información mutua o extensiones posteriores sin prueba.'
 ],
 'strong_novelty_candidates':[
  'Candidata provisional ya identificada por1006: constante completa exacta de qubit para SLD, chi-cuadrado mínimo y Petz triangular con familia qubit–qutrit que aproxima el supremo, junto a la cota armónica uniforme. Novedad mundial no certificada; no se cuenta la maquinaria conocida como aportación adicional.'
 ],
 'unresolved_material_objections':[]}
assert len(summary)<=1600
save('model-response.json',response)
for folder in ['original1006','history998']:(ROOT/folder).mkdir(exist_ok=False)
copies=[]
for n in ['REVIEW1006.txt','verdict1006.json','PROVENANCE1006.json','READINGS1006.json','INCIDENTS1006.json','MANIFEST1006.json','COPY-RECEIPT1006.json']:
    dest=ROOT/'original1006'/n;shutil.copy2(OLD/n,dest)
    copies.append({'path':dest.relative_to(ROOT).as_posix(),'original_path':str(OLD/n),'sha256':sha(dest),'role':'same current assessment1006, not another vote'})
for n in ['REVIEW998.txt','verdict998.json','MANIFEST998.json']:
    dest=ROOT/'history998'/n;shutil.copy2(HISTORY/n,dest)
    copies.append({'path':dest.relative_to(ROOT).as_posix(),'original_path':str(HISTORY/n),'sha256':sha(dest),'role':'history of different PDF995; excluded from current-v1 assessment count'})
schema_files=['scripts/assessmentlib.py','scripts/prepare_model_assessment.py','scripts/arrlib.py','scripts/ratinglib.py','schema/model-assessment.schema.json','templates/frontier-model-assessment-response.json']
schema_hashes=[{'path':n,'sha256':sha(REPO/n)} for n in schema_files]
paper_rel='papers/2026/10/77/ARR-2026-77DGRYDGXD8MDSY2'
metadata_path=REPO/paper_rel/'metadata.json'
metadata=json.loads(metadata_path.read_text(encoding='utf-8'))
save('REGISTRY-SNAPSHOT1010.json',{'utc':now,'path':str(metadata_path),'sha256':sha(metadata_path),'metadata':metadata,'note':'Read-only snapshot, not modified by this binding.'})
fields={
 'paper_id':'Operator-supplied new public record, matched to local metadata identifier.',
 'version':'Operator-supplied v1, matched to local metadata.',
 'version_id':'Operator-supplied immutable version identifier, matched to local metadata.',
 'canonical_sha256':'Exact reviewed PDF1005 bytes, rehashed from preserved1006 input. This is the reviewed PDF hash, not a substituted source hash.',
 'provider':'OpenAI as disclosed assistance/provider context; no runtime evidence object is manufactured.',
 'model_id':'Explicitly unattested effective model; requested GPT-6 Astra xhigh is descriptive provenance, not a certified exact runtime identifier.',
 'assessed_at':'Current serialization timestamp only. Original scientific assessment timestamp retained separately and in summary.',
 'prompt_version':'ARR-ASSESS-1.0 applied only as later output format. Does not claim the original1006 review was prompted or executed under this schema.',
 'independence':'unknown: effective reviewer identity and independence unattested. Codex participation, prior review contributions and shared context remain explicit; this is not a declaration of non-involvement.',
 'recommendation':'recommend_publication_with_declared_scope -> accept, the compatible scientific-recommendation enum. Not Accepted, editorial acceptance, deposit approval or an instruction to publish.',
 'millennium_score':'overall_millennium_0_10 ->4.4 unchanged. Not scientific_importance_airr_0_10 or technical_quality_0_10.',
 'overall_stars':'overall_public_whole_stars ->4 unchanged; nearest-whole rendering, not criterion average.',
 'criteria':'Five criterion names mapped only, preserving every star and basis verbatim from verdict1006.',
 'summary':'Format-only origin, original date, three separate axes, scientific recommendation, Codex participation and lack of attestation preserved within1600characters.',
 'strengths':'Condensed findings and evidence already in1006; no new scientific claims or runs.',
 'weaknesses':'Each O1–O5 retained individually and explicitly resolved, followed by all declared scope, novelty and provenance limitations. Historical resolved issues are not represented as current failures.',
 'potential_errors':'Residual uncertainty and prohibited extrapolations already present in1006, not invented present counterexamples.',
 'strong_novelty_candidates':'The provisional specialized candidate already in1006, with explicit priority uncertainty.',
 'unresolved_material_objections':'Empty because1006 resolvesO1–O5 and finds no new conditioning objection; not a claim of formal certainty.'}
binding={'binding':'1010','kind':'format_only_serialization_of_same_assessment','serialized_at':now,
 'original_scientific_assessment':{'id':'1006','assessed_at':v['utc'],'pdf_sha256':PDF_SHA,'report_sha256':sha(OLD/'REVIEW1006.txt'),'verdict_sha256':sha(OLD/'verdict1006.json'),'new_review':False,'new_grade':False,'additional_vote':False},
 'public_binding':{k:response[k] for k in ['paper_id','version','version_id','canonical_sha256']},
 'submission':{'submission_id':'SUB-DDD4EBE32883B252','provenance':'Deposit clean status, author authority, CC-BY-4.0/CC0 and founder disclosure supplied by coordinator; not independently re-fetched or changed in1010.'},
 'model_response_file_sha256':sha(ROOT/'model-response.json'),
 'model_response_canonical_sha256':hashlib.sha256(json.dumps(response,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 'field_mapping':fields,'criterion_key_mapping':mapping,
 'scores_preserved':{'scientific_importance_airr_0_10':v['scientific_importance_airr_0_10'],'overall_millennium_0_10':v['overall_millennium_0_10'],'technical_quality_0_10':v['technical_quality_0_10'],'bases_verbatim':v['score_bases'],'no_averaging':True},
 'schema_omissions':{'extra_numeric_axes':'Native schema forbids these top-level fields; values are explicit in summary and preserved structurally here and in original verdict.',
  'full_report':'Native summary and findings have length limits; entire unchanged report is included as companion original1006/REVIEW1006.txt and must be displayed alongside this projection.',
  'assessment_id':'Operator-controlled; intentionally absent from model-response. A transient ID may be used in memory solely for validation.',
  'source_response_sha256':'Operator-controlled; intentionally absent from model-response. Canonical response digest is documented here.',
  'runtime_provenance':'Omitted: no attested platform/operator runtime evidence is available.',
  'review_context':'Operator-controlled schema object omitted: cannot invent verified isolation flags or an evidence basis. Shared context952/998 and filesystem are disclosed in human-readable fields and source provenance.',
  'intake_source':'Not an ARR-INTAKE report projection; deposit identity supplied as external binding metadata only.'},
 'objections_original':v['objections'],'uncertainties_original':v['uncertainties'],'not_solved_original':v['main_conclusions']['not_solved'],
 'public_display_requirements':['Show unchanged original1006/REVIEW1006.txt in full, with its hash and linked structured verdict/provenance/reading/incident files.','Display each resolved O1–O5 and all limitations; do not collapse to stars or accept alone.','Treat model-response1010 and original1006 as one scientific assessment, not two votes.','Keep998 as history of the different PDF995 only; do not aggregate it as an additional assessment of current1005/v1.','Do not present requested model/effort or shared context as runtime attestation or independent review.','Recommendation accept is scientific only; no editorial or publication state change is authorized by this file.'],
 'source_files_copied_unchanged':copies,'schema_sources':schema_hashes,
 'validation':'See VALIDATION1010-run*.json for native read-only validator outcome; any pending production-record artifact binding must remain explicit.',
 'no_scientific_search_or_reassessment':True,'repo_modified':False,'originals_modified':False,'published':False,'accepted_editorially':False}
save('BINDING1010.json',binding)
print(json.dumps({'summary_characters':len(summary),'response_sha256':sha(ROOT/'model-response.json'),'binding_sha256':sha(ROOT/'BINDING1010.json'),'current_record_has_pdf_hash':bool(metadata.get('integrity',{}).get('pdf_sha256'))},indent=2))
