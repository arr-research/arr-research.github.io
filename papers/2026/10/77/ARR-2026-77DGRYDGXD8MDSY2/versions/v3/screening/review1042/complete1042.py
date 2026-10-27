from pathlib import Path
import json,hashlib,datetime,shutil,sys
ROOT=Path(__file__).resolve().parent
DEST=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_correction1042-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,x):(ROOT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pdf='08efeffda4865e8f2f0b8e78bd0d2b6260c557a299cf5360d9aef1acc4062372'
frozen='150241ae3fb565cc5217c12e2d651e2ecce64020996caf12ce246009ef5e0d93'
oldpdf='50db4efe067fb88a0bef955d4e5b5779bc31a6afe4c1b78b0c16c9f518b89ab3'
criteria={
'correctness_confidence':{'stars':4,'basis':'O1/O2 resueltas en PDF1041. El examen general1031 y la comparación exacta sostienen las partes no cambiadas; control Doeblin reproducido. Sin prueba formal ni nueva voz independiente.'},
'rigor':{'stars':4,'basis':'Definición Doeblin e inferencia NPT precisadas; intervalo de positividad explícito. Permanecen las pruebas, restricciones y límites ordenados inspeccionados en1031.'},
'novelty':{'stars':3,'basis':'No hay teoremas nuevos ni nueva evidencia de prioridad. Candidatos de contribución y búsqueda dirigida de1031 conservan el mismo alcance y sus límites.'},
'significance':{'stars':4,'basis':'Fórmulas exactas y envolvente técnicamente útiles, con el mismo alcance especializado y ausencia de protocolo operacional o codificación unitaria demostrados.'},
'reproducibility':{'stars':5,'basis':'PDF/fuentes nuevos congelados, diff independiente,1031 íntegro, extracción exacta y certificado Doeblin reproducido. Inspectabilidad no atesta independencia.'}}
bases={
'scientific_importance_airr_0_10':'5.8 mantenido tras inspección exacta: correcciones de fuente/alcance no alteran clasificación, rangos, testigos o utilidad científica. La contribución apreciable sigue especializada y sin protocolo operacional probado.',
'overall_millennium_0_10':'5.6 mantenido para1041: se corrigen los puntos que motivaban revisión menor, pero no se añaden resultados o evidencia de prioridad que cambien el juicio global del conjunto. No promedio ni herencia automática.',
'technical_quality_0_10':'8.5 mantenido: O1/O2 están efectivamente corregidas, sin penalización residual por ellas. La arquitectura de demostración y nivel de comprobación permanecen; esta escala de conjunto no suma premios por cada corrección localizada.'}
objections=[
{'id':'O1','status_for_1030':'confirmed_pending_correction','status_for_1041':'resolved','location':'p9 section7','basis':'Primal X=X†, dual Tr_A Y=I y alpha_+ identificada como variante distinta; certificado igualdad reproducido exactamente.','main_claim_invalidating':False},
{'id':'O2','status_for_1030':'scope_precision_recommended_pending','status_for_1041':'resolved','location':'p9 endsection6','basis':'BASE NPT limitada a SLD/minimal chi-square; general finitePetz solo excluye que ambos estados sean PPT.','main_claim_invalidating':False},
{'id':'O3','status_for_1041':'retained_bibliographic_uncertainty','basis':'Búsqueda dirigida1031 no certifica prioridad; no nueva campaña1042.','main_claim_invalidating':False},
{'id':'O4','status_for_1041':'retained_declared_scope_limitation','basis':'No estabilidad experimental ni aplicación unitaria/operacional demostradas; no transferencia automática BKM.','main_claim_invalidating':False},
{'id':'O5','status_for_1041':'retained_provenance_limitation','basis':'Participación Codex, contexto reutilizado y filesystem compartido; runtime e independencia no atestados.','main_claim_invalidating':False}]
verdict={'review_id':'1042','review_kind':'corrective_continuation_of1031_not_new_full_review','assessment_family':'1031','assessed_at':now,'artifact':{'pdf_sha256':pdf,'frozen_manifest_sha256':frozen,'pages':12,'bytes':340706},'predecessor_pdf_sha256':oldpdf,'predecessor_review_sha256':sha(ROOT/'prior/REVIEW1031.txt'),'scientific_importance_airr_0_10':5.8,'overall_millennium_0_10':5.6,'technical_quality_0_10':8.5,'overall_stars':6,'score_bases':bases,'criteria':criteria,'scores_reaffirmed_after_exact_delta_inspection':True,'automatic_score_inheritance':False,'recommendation':'recommend_publication_with_declared_scope','arr_recommendation':'accept','recommendation_meaning':'Scientific recommendation on corrected1041, continuing1031; not editorial acceptance, publication or an independent second vote.','objections':objections,'new_material_objections':[],'unresolved_material_objections':[],'new_scientific_errors_found':False,'other_change':'Aligned domain -1/(L_d-1)<p<1 correct; includes negative physical parameters.','independence':'involved_in_manuscript','effective_model_identity_attested':False,'full_report':'CORRECTION1042.txt','original1031_preserved':True}
put('verdict1042.json',verdict)
oldarr=json.loads((Path(r'C:\Trabajo\airr\2026-10-27_complete1031-review')/'ARR-CONTENT-UNBOUND1031.json').read_text(encoding='utf-8'))
arr={k:oldarr[k] for k in ['provider','model_id','prompt_version','independence']}
arr.update({'canonical_sha256':pdf,'assessed_at':now,'recommendation':'accept','millennium_score':5.6,'overall_stars':6,'criteria':criteria,
'summary':'Continuación correctiva1042 de la misma evaluación1031, sin reiniciar revisión completa ni constituir segunda voz/voto independiente. PDF1041 exacto de12p: O1 resuelta mediante primal hermítico/dual igualdad y distinción alpha_+; O2 resuelta al limitar BASE NPT a SLD/chi_min² y el par Petz a no-ambos-PPT. Intervalo de positividad explicitado sin ampliar teoremas. Tras diff y páginas afectadas, mantengo importancia5.8, global5.6 y técnica8.5 para este PDF por el mismo contenido y arquitectura demostrativa. Certificado Doeblin reproducido;1031 permanece íntegro. accept significa recomendación científica con alcance declarado, no aceptación editorial. Contexto compartido/participación Codex; identidad efectiva, esfuerzo e independencia no atestados.',
'strengths':['O1/O2 corregidas exactamente; la definición y la inferencia corresponden ahora a las pruebas y fuente examinadas.','Se conservan clasificación unital qubit, envolvente y perfiles de orden; la sección qubit es idéntica byte a byte.','Intervalo alineado explícito incluye la rama negativa física y evita extender el límite fuera del dominio positivo.','Hash/diff trazables y antecedente íntegro; control Doeblin exacto reproduce el resultado previo.'],
'weaknesses':['O3 conservada: bibliografía dirigida1031, prioridad abierta; no búsqueda nueva ni certificado de ausencia de teorema cubriente.','O4 conservada: alcance especializado, testigos posiblemente mal condicionados, sin estabilidad experimental ni aplicación unitaria demostrada.','O5 conservada: contexto952/998/1006/1010/1031 y filesystem compartidos, participación Codex y posible sesgo; no aislamiento o independencia verificados.'],
'potential_errors':['O1/O2 permanecen como objeciones históricas del PDF1030; resueltas solamente para el PDF1041 comprobado. No se editan los informes anteriores.','La exactitud de Bell para cada Petz no se extiende automáticamente a la franja rango dos; ni el supremo completo a cada R fijo. Estos límites permanecen expresos.','Esta comprobación correctiva no repite las pruebas generales ni cinco replays de1031; no acredita cambios externos o candidatas posteriores1033/1035/1037.'],
'strong_novelty_candidates':oldarr['strong_novelty_candidates'], 'unresolved_material_objections':[]})
put('ARR-CONTENT-UNBOUND1042.json',arr)
put('BINDING-LIMIT1042.json',{'status':'unbound_scientific_content_not_native_importable','content_sha256':sha(ROOT/'ARR-CONTENT-UNBOUND1042.json'),'target_pdf_sha256':pdf,'parent_assessment':'1031','relationship':'Corrective continuation by same reviewer/context; do not count1031+1042 as independent voices. Preserve full predecessor report and objection history.','missing_authoritative_fields':['paper_id','version','version_id'],'no_identifiers_invented':True,'must_not_bind_to':'ARR-2026-77DGRYDGXD8MDSY2 v1 or PDF1005 hash','score_mapping':{'millennium_score':5.6,'importance_separate':5.8,'technical_separate':8.5,'bases':'Explicitly reaffirmed for corrected1041 after exact diff inspection; not new target-grade search.'},'recommendation_mapping':'recommend_publication_with_declared_scope -> accept, scientific only; no editorial decision.','runtime_and_context':'No operator-controlled runtime_provenance or review_context fabricated.'})
errors=[]
for k,v in criteria.items():
    if not 1<=v['stars']<=5 or not 15<=len(v['basis'])<=600:errors.append(k)
for k in ['strengths','weaknesses','potential_errors','strong_novelty_candidates','unresolved_material_objections']:
    if len(arr[k])>12 or any(not 8<=len(x)<=800 for x in arr[k]):errors.append(k)
if not 40<=len(arr['summary'])<=1600:errors.append('summary')
assert not errors,errors
put('ARR-CONTENT-VALIDATION1042.json',{'content_length_range_checks_passed':True,'native_registry_validation_performed':False,'native_importable':False,'reason':'No authoritative paper/version IDs for1041; no fake binding used.','schema_source':'Read in1031: scripts/assessmentlib.py and prepare_model_assessment.py; source hashes retained in prior/PROVENANCE1031.json.'})
put('PROVENANCE1042.json',{'utc':now,'requested_configuration':{'model':'GPT-6 Astra','effort':'xhigh'},'effective_model_identity':None,'effective_effort':None,'effective_identity_attested':False,'independence_verified':False,'statistical_independence_claimed':False,'participation':'Prior Codex contribution via development/review; involved_in_manuscript.','context_reused':['952','998','1006','1010','1031'],'filesystem_shared':True,'possible_bias':'Familiarity/confirmation; not quantified.','review_kind':'Same reviewer corrective continuation, no new independent vote or full-review restart.','scope':'Only corrections and exact binding1030->1041; no1033/1035/1037.','new_agents':0,'other_chats_opened':0,'other_reviews_initiated':0,'input_verification':['INPUT-INITIAL1042.json','INPUT-FINAL1042.json'],'previous_dossier_integrity':['PRIOR1031-BASELINE1042.json','PRIOR1031-FINAL1042.json'],'scientific_sources':'Prior1031 primary-source reading reused with exact versions/hashes; no new bibliographic campaign.','rubric':'prior/RUBRIC1031.md; AIRR policy read in1031 and retained; no score inheritance by default.','execution':'Single own Doeblin control reexecuted from byte-identical copy; no discovery optimizer or five-checker campaign rerun.','no_mutators_executed':['assemble.py','publication scripts','Git or state update'],'original_inputs_and1031_unchanged':True,'no_editorial_decision_or_publication':True})
put('READINGS1042.json',{'utc':now,'new_reading':['CORRECTIONS1041.json','SOURCE-DIFF1041.txt','PAPER1041.txt entire','Independent diff of main.tex and sections against sealed1031 inputs','Changed TeX passages and context','Pages1,8,9,10,11,12 rendered and visually inspected'],'unchanged_pdf_pages':'Pages2–7 pixel-identical to1030 at100dpi; not claimed as a new full proof audit.','qubit_source_identical':True,'primary_source_reused':{'url':'https://arxiv.org/abs/2503.22823v3','sha256':'61e6049323dda504053d4f4e0204f4306c7fac851179cd200c0208bdc6aefd23','scope':'1031 read PDF13–14 Definition4/Proposition3, HTML Definition7 Eq3.25; source contents reused, not redownloaded or reread whole108p.'},'old_full_report':'prior/REVIEW1031.txt unchanged; prior full readings/scopes in prior/READINGS1031.json','not_checked_anew':['Full primary literature','Whole general proof campaign','Five supplementary replays','External errata','Later candidates1033/1035/1037'],'instructions':'D:\\LEEME.md and globalAGENTS reread; workC/archiveD.'})
assert (ROOT/'input/PAPER1041.txt').read_bytes()==(ROOT/'EXTRACTED1042.txt').read_bytes()
assert (ROOT/'prior/doeblin_definition1031.py').read_bytes()==(ROOT/'controls/doeblin_definition1031.py').read_bytes()
result=json.loads((ROOT/'controls/DOEBLIN-DEFINITION1031.json').read_text(encoding='utf-8'))
assert result['all_passed'] and result==json.loads((ROOT/'prior/DOEBLIN-DEFINITION1031.json').read_text(encoding='utf-8'))
put('CONTROL1042.json',{'utc':now,'script':'controls/doeblin_definition1031.py','script_sha256':sha(ROOT/'controls/doeblin_definition1031.py'),'same_script_and_inputs_as1031':True,'exit_code':0,'all_passed':True,'output_json_equal_to1031':True,'output_sha256':sha(ROOT/'controls/DOEBLIN-DEFINITION1031.json'),'historical_labels':'Output retains historical1031 issue wording; current status O1 resolved is in verdict1042.','PDF_extraction_byte_identical_to_supplied_text':True,'new_runs':1,'reruns_for_favorable_outcome':0})
put('SCOPE1042.json',{'independent_diff':'INDEPENDENT-SOURCE-DIFF1042.txt','source_comparison':'SOURCE-COMPARISON1042.json','changed_source_files':['main.tex','sections/context.tex','sections/order.tex'],'unchanged_source':'sections/qubit.tex','scientific_changes':['Hermitian Doeblin primal/equality dual and alpha_+ distinction','SLD/chi_min baseNPT versus finitePetz not-both-PPT','Aligned positivity interval -1/(L_d-1)<p<1'],'other_changes':['Revision status','1031 history with exact old PDF hash','Paragraph/hash layout and reference reflow'],'new_theorems':False,'later_candidates_included':False,'visual_pages_inspected':[1,8,9,10,11,12],'pixel_identical_pages':[2,3,4,5,6,7],'new_visual_defects_found':False})
put('INCIDENTS1042.json',{'utc':now,'new_execution_failures':[],'scientific_errors_found_in_changes':[],'old_incidents_retained':'1031 original140files unchanged; prior/INCIDENTS1031.json copied verbatim. No old failures erased or relabelled pass.','binding_limitation':'No public IDs for1041 available; unboundARR only.','historical_control_wording':'Original control describes pre-correctionO1; retained for integrity and explicitly distinguished from resolved1041 status.','initial_order':'FROZEN/CORRECTIONS declarations consulted for setup; all hashes verified before substantive diff review.','full_review_restarts':0,'new_scientific_search_campaigns':0,'editorial_observation':'English phrase that that input base is slightly awkward but grammatical/harmless; not a scientific objection.'})
# Final integrity of frozen1041 and original1031; read-only operations.
checks=[]
for base in [Path(r'C:\Trabajo\airr\2026-10-27_corrected1041'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_corrected1041')]:
    assert sha(base/'FROZEN1041.json')==frozen
    m=json.loads((base/'FROZEN1041.json').read_text(encoding='utf-8'))
    for f in m['files']:
        p=base/f['path'];ok=sha(p)==f['sha256'] and p.stat().st_size==f['bytes'];assert ok
        checks.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'pass':ok})
put('INPUT-FINAL1042.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_sha256_C_D':frozen,'all26_payloads_passed':True,'inputs_unchanged':True,'checks':checks})
baseline=json.loads((ROOT/'PRIOR1031-BASELINE1042.json').read_text(encoding='utf-8'))
for base in [Path(r'C:\Trabajo\airr\2026-10-27_complete1031-review'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1031-review')]:
    observed={p.relative_to(base).as_posix():sha(p) for p in base.rglob('*') if p.is_file()}
    assert observed=={r['path']:r['sha256'] for r in baseline['files']}
put('PRIOR1031-FINAL1042.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'C_and_D_each140_files_unchanged':True,'baseline_sha256':sha(ROOT/'PRIOR1031-BASELINE1042.json'),'original_report_sha256':sha(ROOT/'prior/REVIEW1031.txt'),'original_verdict_sha256':sha(ROOT/'prior/verdict1031.json')})
assert ROOT.resolve()==Path(r'C:\Trabajo\airr\2026-10-27_correction1042-review').resolve()
assert DEST.resolve()==Path(r'D:\Proyectos\airr-investigacion\2026-10-27_correction1042-review').resolve()
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_symlink():raise RuntimeError('Unexpected symlink')
    if p.is_file() and p.name not in ['MANIFEST1042.json','ARCHIVE1042.json']:
        files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
put('MANIFEST1042.json',{'utc':now,'scope':'Corrective continuation1042 dossier; all files except manifest and archive receipt','pdf_sha256':pdf,'payload_count':len(files),'files':files})
if DEST.exists() and any(DEST.iterdir()):raise RuntimeError('Unexpected existing archive; no overwrite')
DEST.mkdir(parents=True,exist_ok=True)
for p in sorted(ROOT.rglob('*')):
    q=DEST/p.relative_to(ROOT)
    if p.is_dir():q.mkdir(parents=True,exist_ok=True)
    elif p.is_file():shutil.copy2(p,q)
for f in files:assert sha(ROOT/f['path'])==sha(DEST/f['path'])==f['sha256']
assert sha(ROOT/'MANIFEST1042.json')==sha(DEST/'MANIFEST1042.json')
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_C':str(ROOT),'archive_D':str(DEST),'payload_count':len(files),'total_files':len(files)+2,'all_files_identical_C_D':True,'review_sha256':sha(ROOT/'CORRECTION1042.txt'),'verdict_sha256':sha(ROOT/'verdict1042.json'),'manifest_sha256':sha(ROOT/'MANIFEST1042.json'),'inputs1041_unchanged':True,'all140_prior1031_files_C_D_unchanged':True,'no_publication_or_editorial_acceptance':True,'same_assessment_family':'1031; corrective continuation1042, not independent vote'}
put('ARCHIVE1042.json',receipt);shutil.copy2(ROOT/'ARCHIVE1042.json',DEST/'ARCHIVE1042.json')
assert {p.relative_to(ROOT).as_posix():sha(p) for p in ROOT.rglob('*') if p.is_file()}=={p.relative_to(DEST).as_posix():sha(p) for p in DEST.rglob('*') if p.is_file()}
print(json.dumps(receipt,ensure_ascii=False,indent=2))
