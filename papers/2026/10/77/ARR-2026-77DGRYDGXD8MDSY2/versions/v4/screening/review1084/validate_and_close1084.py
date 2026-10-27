from pathlib import Path
import json,hashlib,datetime,re,shutil,sys
P=Path(__file__).resolve().parent
C=Path(r'C:\Trabajo\airr\2026-10-27_complete1060')
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_combined1083')
OUT=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_combined1084-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def get(n):return json.loads((P/n).read_text(encoding='utf-8'))
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert not OUT.exists(),'Fresh own archive destination required; do not overwrite.'
assert P.resolve()==Path(r'C:\Trabajo\airr\2026-10-27_combined1084-review').resolve()
assert OUT.parent.resolve()==Path(r'D:\Proyectos\airr-investigacion').resolve()
incs=get('INCIDENTS1084.json')
incs['incidents'][5]['detail']+=' The later RAM hash fetch for dongmin.dev returned HTTP403; earlier browser record reading and unavailable hash are distinguished in WEB-READINGS1084.json.'
incs['incidents'].append({'id':'I7','type':'metadata_warning','detail':'metadata1084.py emitted SyntaxWarning invalid escape sequence in D:\\LEEME.md literal, then completed successfully. Path and JSON inspected; no scientific rerun, source mutation or score change.','preserved':['metadata1084.py','METADATA-RUN1084.txt']})
put('INCIDENTS1084.json',incs)
with (P/'INCIDENTS1084.txt').open('a',encoding='utf-8') as f:f.write('\nI7 — '+incs['incidents'][-1]['detail']+'\n')
(P/'METADATA-RUN1084.txt').write_text("Observed run: python -X utf8 metadata1084.py, exit0. SyntaxWarning: invalid escape sequence '\\L' in provenance literal D:\\LEEME.md. Seven sources and six objections serialized. No exception. This receipt transcribes the tool output; it is not raw stderr capture.\n",encoding='utf-8')
v=get('verdict1084.json');v['report_sha256']=sha(P/'REVIEW1084.txt');put('verdict1084.json',v)
pr=get('PROVENANCE1084.json');pr['report_sha256']=sha(P/'REVIEW1084.txt');pr['verdict_sha256']=sha(P/'verdict1084.json');put('PROVENANCE1084.json',pr)
b=get('ARR-BINDING-LIMITS1084.json');b['report_sha256']=sha(P/'REVIEW1084.txt');b['verdict_sha256']=sha(P/'verdict1084.json');put('ARR-BINDING-LIMITS1084.json',b)
arr=get('ARR-CONTENT-UNBOUND1084.json');errors=[]
assert not set(['paper_id','version','version_id','assessment_id','source_response_sha256','runtime_provenance','review_context'])&set(arr)
assert arr['canonical_sha256']==sha(P/'input/main.pdf')==v['exact_artifact']['pdf_sha256']
assert arr['millennium_score']==v['overall_millennium_0_10']==6.1 and arr['overall_stars']==6
assert v['scientific_importance_airr_0_10']==6.3 and v['technical_quality_0_10']==8.7
assert arr['independence']=='involved_in_manuscript' and 'unattested' in arr['model_id']
assert arr['recommendation']=='accept' and not arr['unresolved_material_objections']
assert set(arr['criteria'])=={'correctness_confidence','rigor','novelty','significance','reproducibility'}
for c in arr['criteria'].values():assert set(c)=={'stars','basis'} and isinstance(c['stars'],int) and 1<=c['stars']<=5 and 15<=len(c['basis'].strip())<=600
assert 40<=len(arr['summary'].strip())<=1600
for key in ['strengths','weaknesses','potential_errors','strong_novelty_candidates','unresolved_material_objections']:
 assert isinstance(arr[key],list) and len(arr[key])<=12
 for item in arr[key]:assert isinstance(item,str) and 8<=len(item.strip())<=800
assert [x['id'] for x in v['objections']]==['O1','O2','O3','O4','O5','O6']
assert len(arr['weaknesses'])==6 and all(arr['weaknesses'][j].startswith('O'+str(j+1)+':') for j in range(6))
put('ARR-VALIDATION1084.json',{'utc':now(),'content_subset_valid':True,'errors':errors,'native_registry_validation_performed':False,'native_record_importable':False,'reason':'No public exact1083 identity supplied; no synthetic Paper or IDs invented. Content-only constraints from read-only assessmentlib.py.','repository_mutated':False,'report_verdict_content_mapping_consistent':True,'content_sha256':sha(P/'ARR-CONTENT-UNBOUND1084.json')})
rows=[]
for root in [C,D,P/'input']:
 mf=root/'FROZEN1083.json';assert sha(mf)=='6f43e3d85b5d781f5f47b57aa7a439f5e1afad4294f70d67fa969ae27968ef04'
 m=json.loads(mf.read_text(encoding='utf-8'));assert len(m['files'])==16
 names={'FROZEN1083.json'}
 for x in m['files']:
  q=root/x['path'];assert sha(q)==x['sha256'] and q.stat().st_size==x['bytes'];names.add(x['path'])
 extras=sorted(q.relative_to(root).as_posix() for q in root.rglob('*') if q.is_file() and q.relative_to(root).as_posix() not in names)
 inputs=re.findall(r'\\input\{([^}]+)\}',(root/'main.tex').read_text(encoding='utf-8'))
 assert len(inputs)==7 and all(n+'.tex' in names for n in inputs)
 rows.append({'root':str(root),'frozen_sha256':sha(mf),'payloads':m['files'],'all16_passed':True,'latex_inputs':inputs,'latex_all7_manifested':True,'nonmanifest_names_only':extras,'extras_not_inputs':True})
put('INPUT-FINAL1084.json',{'utc':now(),'all_passed':True,'scope':'16manifest payloads+self only; never entire Cdirectory','receipts':rows})
deps=json.loads((D/'SOURCE-INPUTS1083.json').read_text(encoding='utf-8'))['inputs'];dr=[]
for dep in deps:
 root=Path(dep['path']);mf=root/dep['manifest'];assert sha(mf)==dep['manifest_sha256']
 dm=json.loads(mf.read_text(encoding='utf-8'));payloads=dm.get('files',dm.get('payloads',[]));assert payloads
 for x in payloads:
  p=root/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 dr.append({**dep,'all_payloads_passed':True,'payload_count':len(payloads)})
put('DEPENDENCIES-FINAL1084.json',{'utc':now(),'all_passed':True,'unchanged_from_initial':True,'dependencies':dr})
assert get('OWN1084.json')['all_passed'] and get('REPLAY1084.json')['all_passed'] and get('FINITE-CERTIFICATES1084.json')['all_six_passed']
assert len(list((P/'qa').glob('page-*.png')))==23
# All generated JSON is parsed before sealing; no scientific tests are re-sampled.
json_count=0
for q in P.rglob('*.json'):json.loads(q.read_text(encoding='utf-8-sig'));json_count+=1
put('DOSSIER-QA1084.json',{'utc':now(),'parsed_json_before_self':json_count,'23page_images':True,'own_and_replay_and_six_certificates_pass':True,'all_objections_retained':True,'frozen_scope_separate_from_auxiliaries':True,'current_material_objections':0,'full_review_readable_path':'REVIEW1084.txt','not_a_formal_proof_or_priority_certificate':True})
(P/'README1084.txt').write_text('Dossier1084: una evaluación completa del PDF1083 exacto.\nEntrada inmutable: input/ (16payloads y FROZEN).\nEvidencia dependiente e historia: dependencies/ y prior-scope/.\nReproducciones acotadas: replay/.\nRender propio del PDF: qa/.\nScripts, controles y metadatos propios: raíz del dossier.\nNo confundir auxiliares del dossier con auxiliares no sellados de la carpetaC de origen.\nLeer REVIEW1084.txt, verdict1084.json y reservasO1–O6 completos.\nARR-CONTENT-UNBOUND no es importable sin IDs reales y no es otro voto.\nMANIFEST1084 excluye sólo sí mismo y ARCHIVE1084, enumerados en el recibo de cierre.\nCierre terminal únicamente tras ARCHIVE1084.json con igualdad totalC/D comprobada.\n',encoding='utf-8')
exclusions={'MANIFEST1084.json','ARCHIVE1084.json'}
files=[]
for q in sorted(P.rglob('*')):
 if q.is_file() and q.relative_to(P).as_posix() not in exclusions:
  assert not q.is_symlink();files.append({'path':q.relative_to(P).as_posix(),'bytes':q.stat().st_size,'sha256':sha(q)})
put('MANIFEST1084.json',{'utc':now(),'review':'1084','canonical_pdf_sha256':arr['canonical_sha256'],'payload_count':len(files),'files':files,'self_and_closure_excluded':sorted(exclusions),'input_scope':'input/17files; all other dossier material separate','no_publication_or_editorial_acceptance':True})
OUT.mkdir()
for q in sorted(P.rglob('*')):
 if q.is_file():
  dest=OUT/q.relative_to(P);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(q,dest)
def all_files(root):return {p.relative_to(root).as_posix():(p.stat().st_size,sha(p)) for p in root.rglob('*') if p.is_file()}
cfiles=all_files(P);dfiles=all_files(OUT);assert cfiles==dfiles
archive={'utc':now(),'terminal':True,'source':str(P),'destination':str(OUT),'payload_count':len(files),'files_before_closure_receipt':len(cfiles),'files_including_closure_receipt':len(cfiles)+1,'all_C_D_files_equal':True,'canonical_pdf_sha256':arr['canonical_sha256'],'manifest_sha256':sha(P/'MANIFEST1084.json'),'report_sha256':sha(P/'REVIEW1084.txt'),'verdict_sha256':sha(P/'verdict1084.json'),'input_final_sha256':sha(P/'INPUT-FINAL1084.json'),'dependencies_final_sha256':sha(P/'DEPENDENCIES-FINAL1084.json'),'self_hash_excluded':'Receipt cannot hash itself; identical bytes copied and compared after creation. Manifest covers every other payload; its hash is here.','scope':'Frozen16inputpayloads verified before/after;Cauxiliaryinventory excluded frominput. Own dossier auxiliary files included in archive and manifest.'}
put('ARCHIVE1084.json',archive);shutil.copy2(P/'ARCHIVE1084.json',OUT/'ARCHIVE1084.json')
assert all_files(P)==all_files(OUT)
assert len(all_files(P))==archive['files_including_closure_receipt']
print(json.dumps({**archive,'archive_receipt_sha256':sha(P/'ARCHIVE1084.json')},ensure_ascii=False,indent=2))
