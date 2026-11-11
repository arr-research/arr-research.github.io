import json, hashlib, shutil
from pathlib import Path
from datetime import datetime, timezone

base=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-260')
first=base/'assessment260C-first-round'
supp=base/'assessment260C-required-reproducibility-supplement'
out=base/'assessment260C-native-format-completion'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot(d): return {p.relative_to(d).as_posix():{'bytes':p.stat().st_size,'sha256_raw':digest(p)} for p in sorted(d.rglob('*')) if p.is_file()}
before={first.name:snapshot(first),supp.name:snapshot(supp)}
if out.exists(): raise RuntimeError('Completion directory exists; do not overwrite or resample')
primary=json.loads((first/'response-native.json').read_text(encoding='utf-8'))
extra=json.loads((supp/'criterion-response.json').read_text(encoding='utf-8'))
ctx0=json.loads((first/'review-context.json').read_text(encoding='utf-8'))
ctx1=json.loads((supp/'review-context.json').read_text(encoding='utf-8'))
if digest(first/'response-native.json')!='70ae74208f198811c3dcf44c4b3ebf9830c61965b1b03782b5449ccb66ade69f': raise RuntimeError('Original response changed')
if digest(supp/'criterion-response.json')!='385cd4f76d0394951a3a7cf92d361c7786ce9c6683fe2b65773e58fbfd30af2c': raise RuntimeError('Criterion response changed')
out.mkdir()
def save(name,value):
    p=out/name;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f: f.write(value)
def js(name,value): save(name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
assignment='''Bounded FORMAT-ONLY completion, not a new review or score sample. All scientific decisions are locked: firstimportance5.00,overall5,major_revision,alloriginalfindings/objections/clarity4 unchanged; actualrequiredreprocriterion4 from yourcompleted supplement. AIRR native record_model_assessment.py requires a structured model response with exact closed keys. Please emit ONE native serialization of those existing decisions in NEW evidencia-260/assessment260C-native-format-completion, keeping both originaldirectories untouched. No fresh PDF/maths/novelty/importance review, newscore or changedfinding. Binding metadata: paper_idARR-2026-597T88D7WZ98HR0Z,versionv2,version_idarr:version:a7ab2042-a76e-4289-82a5-75fd290ec1d4,canonical_sha256f9d3a44e4811a28ec11af3577a4218dad1cb2b3bc0482e2528f5ff80ffdc3892,actualfirstassessed_at2026-11-11T18:12:33.851959+00:00. Required keys ONLY: paper_id,version,version_id,canonical_sha256,provider,model_id,assessed_at,prompt_version,independence,recommendation,millennium_score,overall_stars,criteria,summary,strengths,weaknesses,potential_errors,strong_novelty_candidates,unresolved_material_objections. ProviderOpenAI, model_idexactactuallyexposedunknownbackendlabel; independenceunknown or conservativeinvolved peractualcontext, neverindependent. Criteria exactlycorrectness_confidence,rigor,novelty,significance,reproducibility; values/bases from immutable actualprimaryreview + genuine reprosupp ONLY. Originalclarity4 remains an extra diagnostic in primaryreport, neverrenamed. Arrays/summary use originalactualfindings withoutnewscientificopinions. Nativeoutputcontract tag is ARR-ASSESS-1.0 (prompt_version field); EXPLICITLY explain in separatefullformat-clarification/context that this is a serialization completion NOW, initialprotocol was the custom frozen88a8... prompt, not falselyclaimedverbatim canonicalprompt beforejudgment, and no calibrationrescore occurred. Nativeimportance means the actual5 alreadyjudged; not anaverage orphysicalprogress. Do notinvent runtime provenance, exactbackend, effort, freshhumanassent orpublication. Do NOT set assessment_id/source_response_sha256/runtime_provenance/review_context/intake_source in response; native normalizer owns those. Preserve fullactualassignment, explanation, originalreports/sourcehashrefs and rawmanifest in newfolder; return actualformatcompletion andhashes. If you cannot honestly emit the protocoltagasdeclaredoutputcontract withoutfalselyclaimingoriginalprompt, recordthatblocker ratherthan fabricate. No inboundmessageswhiletask.'''
save('assignment.txt',assignment+'\n')
criteria={k:primary['criteria'][k] for k in ('correctness_confidence','rigor','novelty','significance')}
criteria['reproducibility']={k:extra[k] for k in ('stars','basis')}
response={
 'paper_id':'ARR-2026-597T88D7WZ98HR0Z','version':'v2','version_id':'arr:version:a7ab2042-a76e-4289-82a5-75fd290ec1d4',
 'canonical_sha256':'f9d3a44e4811a28ec11af3577a4218dad1cb2b3bc0482e2528f5ff80ffdc3892',
 'provider':'OpenAI','model_id':'Codex (exact served backend/model version unavailable)',
 'assessed_at':'2026-11-11T18:12:33.851959+00:00','prompt_version':'ARR-ASSESS-1.0',
 'independence':'involved_in_manuscript','recommendation':primary['recommendation'],
 'millennium_score':primary['millennium_score'],'overall_stars':primary['overall_stars'],'criteria':criteria}
fields=('summary','strengths','weaknesses','potential_errors','strong_novelty_candidates','unresolved_material_objections')
response.update({k:primary[k] for k in fields})
required=set('paper_id version version_id canonical_sha256 provider model_id assessed_at prompt_version independence recommendation millennium_score overall_stars criteria summary strengths weaknesses potential_errors strong_novelty_candidates unresolved_material_objections'.split())
if set(response)!=required or len(required)!=19: raise RuntimeError('Incorrect response keys')
if response['millennium_score']!=5 or response['overall_stars']!=5 or response['recommendation']!='major_revision': raise RuntimeError('Locked score/recommendation mismatch')
if len(response['unresolved_material_objections'])!=2 or primary['criteria']['clarity']['stars']!=4: raise RuntimeError('Locked original decision mismatch')
for k,v in criteria.items():
    if set(v)!={'stars','basis'} or type(v['stars']) is not int or not 1<=v['stars']<=5 or not 15<=len(v['basis'].strip())<=600: raise RuntimeError('Invalid criterion format')
for k in fields:
    if response[k]!=primary[k]: raise RuntimeError('Changed original finding')
    if k!='summary' and (len(response[k])>12 or any(not 8<=len(s.strip())<=800 for s in response[k])): raise RuntimeError('Array shape issue')
if not 40<=len(response['summary'].strip())<=1600: raise RuntimeError('Summary format issue')
js('response-native.json',response)
now=datetime.now(timezone.utc).isoformat()
clarification='''FORMAT-ONLY NATIVE SERIALIZATION COMPLETION — NO NEW SCIENTIFIC ASSESSMENT

This packet serializes completed, immutable judgments into the closed native response shape requested by the parent. It is not a second review, a new score sample, a calibration or an attempt to improve a mark. No PDF page, mathematical argument, novelty or importance claim has been reassessed during this task. All original summary text and five findings arrays are copied verbatim from the first response. The first four native criteria are copied verbatim, while reproducibility is copied verbatim from the actual required-criterion-only supplement. Clarity4 remains untouched as an additional diagnostic in the original report; it has not been renamed or used to supply reproducibility.

PROTOCOL AND TIME DISCLOSURE
The actual initial scientific protocol was the custom frozen prompt whose raw SHA256 is88a8ab8b12f82eb5abd443e708d18bb05b5ae4085ef153b7a5b82de98f7c8f06. ARR-ASSESS-1.0 in the new response is the declared native OUTPUT-CONTRACT TAG for this serialization completion NOW. It is not a claim that the canonical ARR prompt was executed verbatim before the original scientific judgment. No canonical calibration prompt or calibration rescore occurred. The actual original prompt is retained in captures. The inspected public normalizer reserves operator-controlled fields and the native validator accepts this tag and the exact five criteria as a response contract; these scripts were read, not executed here. Schema conformance alone does not certify historical prompt compliance. Any downstream use must retain this clarification and original source reports, and must not present this packet as evidence of a verbatim original canonical prompt or a fresh independent assessment. If downstream policy requires such a historical claim, this packet does not supply it.

assessed_at preserves the actual first scientific judgment timestamp2026-11-11T18:12:33.851959+00:00. The reproducibility supplement was recorded separately at2026-11-11T18:19:16.323138+00:00. This composite serialization is created later; its exact creation time is in format-context.json. No claim is made that the missing required criterion was assessed at the original earlier timestamp.

LOCKED DECISIONS AND LIMITS
Importance5.00/10, overall5/10, major_revision and both original OPEN material objections260C-M1 and260C-M2 remain unchanged. The legacy field millennium_score expresses importance of this finite manuscript; it is not an average of criteria, a percentage, a physical spectral gap or progress resolving Yang–Mills. Reproducibility4/5 is the genuine missing-axis judgment already made from retained source/reproduction evidence, not an invented substitution for clarity4. No objection has been closed. No human peer review, formal verification, acceptance, fresh human assent or publication is claimed.

IDENTITY AND INVOLVEMENT
ProviderOpenAI, exposed session identityCodex. Exact served backend/model version and reasoning effort are unavailable. model_id states that limitation; it is not an invented provider model identifier. The child had inherited programme/construction/review context and is not blind. involvement is conservatively marked involved_in_manuscript, with no independence established. No new external model call or runtime execution was made. No operator runtime_provenance or review_context is asserted inside the response. Normalizer-owned identifiers and hashes are deliberately absent. Metadata binding was supplied by the parent; this bounded formatting task has not independently reverified the public registry binding or publication status.

RETENTION AND VERIFICATION
The previous first-round and reproducibility-supplement directories are immutable. Their complete before/after raw hash maps are retained and compared. This packet includes exact source reports, actual prompts/assignments and contexts, the fresh closed-shape JSON, a complete assignment, this clarification, the serialization helper and a self-excluding raw file manifest. Checks cover exact19 keys, five required criteria, integer1–5 stars, text limits, unchanged original decisions/findings and verbatim genuine supplement basis. These are local formatting/retention checks, not a run of AIRR's importer, public registry validation, mathematics verification or deployment. No source/branch/state/permissions/publication files are changed.
'''
save('format-clarification.txt',clarification)
refs=[]
files={first:['scientific-review.txt','response-native.json','review-context.json','prompt.txt','assignment.txt','assignment-readable.txt','retention-clarification.txt','report-hashes.json','supplemental-retention-hashes.json'],supp:['reproducibility-supplement.txt','criterion-response.json','review-context.json','assignment.txt','supplement-hashes.json','original-round-immutability-check.json']}
for folder,names in files.items():
    for name in names:
        src=folder/name;dest=out/'captures'/folder.name/name;dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open('xb') as f: f.write(src.read_bytes())
        refs.append({'original_path':str(src),'retained_path':dest.relative_to(out).as_posix(),'bytes':src.stat().st_size,'sha256_raw':digest(src)})
with (out/'format-writer.py').open('xb') as f: f.write(Path(__file__).read_bytes())
js('source-references.json',refs)
js('format-context.json',{'serialization_created_at':now,'task':'/root/exact260c_first_pdf_assessment','kind':'format-only completion of existing judgments','original_scientific_assessed_at':response['assessed_at'],'required_criterion_recorded_at':ctx1['recorded_at'],'original_protocol_sha256_raw':digest(first/'prompt.txt'),'declared_output_contract':'ARR-ASSESS-1.0','canonical_original_prompt_verbatim_claimed':False,'calibration_rescore_performed':False,'new_scientific_review_performed':False,'new_numerical_judgment':False,'original_clarity_preserved':primary['criteria']['clarity'],'actual_identity':'Codex/OpenAI; exact served backend/model version and effort unavailable','independence_established':False,'blind':False,'inherited_context_visible':True,'runtime_execution_performed':False,'operator_runtime_provenance_claimed':False,'publication_or_human_assent_claimed':False,'parent_supplied_binding_independently_reverified':False,'public_contract_sources_read':['https://raw.githubusercontent.com/arr-research/arr-research.github.io/main/scripts/assessmentlib.py','https://raw.githubusercontent.com/arr-research/arr-research.github.io/main/scripts/record_model_assessment.py'],'sources_executed':False,'full_clarification':'format-clarification.txt'})
after={first.name:snapshot(first),supp.name:snapshot(supp)}
if before!=after: raise RuntimeError('Original directories changed during format task')
js('original-directories-immutability-check.json',{'unchanged':True,'before':before,'after':after})
js('format-checks.json',{'exact19closed_response_keys':True,'required_five_criteria_only':True,'first_four_criteria_verbatim':True,'genuine_reproducibility_verbatim':True,'summary_and_arrays_verbatim':True,'original_scores_recommendation_two_open_objections_preserved':True,'original_clarity4_preserved':True,'basic_native_field_types_and_lengths_checked':True,'actual_AIRR_normalizer_or_registry_not_run':True,'original_directories_unchanged':True,'original_file_counts':{k:len(v) for k,v in before.items()}})
js('completion-hashes.json',{'algorithm':'SHA-256 raw bytes','self_excluded':'completion-hashes.json','created_at':now,'files':snapshot(out)})
manifest=json.loads((out/'completion-hashes.json').read_text(encoding='utf-8'))
for rel,info in manifest['files'].items():
    p=out/rel
    if p.stat().st_size!=info['bytes'] or digest(p)!=info['sha256_raw']: raise RuntimeError('Retention verification failed')
print(json.dumps({'directory':str(out),'response_sha256_raw':digest(out/'response-native.json'),'clarification_sha256_raw':digest(out/'format-clarification.txt'),'manifest_sha256_raw':digest(out/'completion-hashes.json'),'file_count':len(snapshot(out)),'original_directories_unchanged':True},indent=2))
