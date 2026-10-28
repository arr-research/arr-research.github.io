from pathlib import Path
import json,hashlib,datetime,shutil
from pypdf import PdfReader
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1148-review')
roots=[Path(r'C:\Trabajo\airr\2026-10-28_support1147'),Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1147'),P/'input']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def inv(root):return {q.relative_to(root).as_posix():dict(bytes=q.stat().st_size,sha256=sha(q)) for q in sorted(root.rglob('*')) if q.is_file()}
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
receipts=[];invs=[]
for root in roots:
    assert sha(root/'MANIFEST1147.json')=='c56573d0dfdb11418250f3f3377b1e5dee7ed98c53c85c0e9d196c43ebf31c82'
    m=read(root/'MANIFEST1147.json');assert len(m['files'])==311
    expected={r['path']:dict(bytes=r['bytes'],sha256=r['sha256']) for r in m['files']}
    expected['MANIFEST1147.json']=dict(bytes=(root/'MANIFEST1147.json').stat().st_size,sha256=sha(root/'MANIFEST1147.json'))
    actual=inv(root);assert actual==expected and len(actual)==312
    receipts.append(dict(root=str(root),all_passed=True,exact_files=312,files=actual));invs.append(actual)
assert invs[0]==invs[1]==invs[2]==read(P/'INPUT-INITIAL1148.json')['files']
assert len(PdfReader(P/'input/manuscript.pdf').pages)==15
v=read(P/'verdict1148.json')
assert sha(P/'input/manuscript.pdf')==v['artifact']['pdf_sha256'] and (P/'input/manuscript.pdf').stat().st_size==421986
assert sha(P/'input/main.tex')==v['artifact']['tex_sha256'] and sha(P/'input/sections/general-support.tex')==v['artifact']['section_sha256']
assert sha(P/'REVIEW1148.txt')==v['report']['sha256']
assert v['scientific_importance_airr_0_10']==7 and v['overall_millennium_0_10']==6.7 and v['technical_quality_0_10']==8.8
assert len(v['criteria_1_5'])==5 and all(c['stars']==4 for c in v['criteria_1_5'].values())
assert v['recommendation']['value']=='minor_revision' and not v['unresolved_material_objections'] and v['unresolved_minor_corrections']==['O1']
assert [o['id'] for o in v['objections']]==['O1','O2','O3','O4','O5']
assert v['observed_configuration']['effective_model_id'] is None and v['observed_configuration']['effective_reasoning_effort'] is None
assert read(P/'replay/REPLAY1147.json')['status']=='pass' and read(P/'replay/REPLAY1147.json')['checkers']==12
assert read(P/'OWN1148.json')['all_passed'] and len(read(P/'OWN1148.json')['records'])==13
for n in ['OWN-FAILURE-INITIAL1148.json','own1148_initial.py','OWN-DIAGNOSIS1148.json']:
    assert (P/n).is_file()
put('INPUT-FINAL1148.json',dict(utc=utc(),all_passed=True,initial_and_final_identical=True,source_C_D_and_own_copy_identical=True,original_inputs_unchanged=True,roots=receipts))
parsed=[]
for q in P.glob('*.json'):
    read(q);parsed.append(q.name)
put('VALIDATION1148.json',dict(utc=utc(),all_passed=True,local_JSON_files_parsed=sorted(parsed),report_verdict_binding=True,PDF_exact_binding=True,separate_three_scores_and_five_criteria=True,O1_minor_and_all_reservations_retained=True,own_failed_attempt_preserved=True,bounded_replay_and_own_controls_pass=True,no_native_ARR_validation_or_editorial_acceptance_claim=True))
assert not D.exists() and not (P/'MANIFEST1148.json').exists() and not (P/'CLOSURE1148.json').exists()
payload=inv(P)
put('MANIFEST1148.json',dict(utc=utc(),scope='All review payloads including frozen input copy, own controls/failures, source reading metadata and QA; excludes manifest and closure to avoid self-reference.',payload_count=len(payload),files=[dict(path=n,**r) for n,r in payload.items()],reviewed_PDF_sha256=v['artifact']['pdf_sha256'],source_manifest_sha256=v['artifact']['input_manifest_sha256']))
shutil.copytree(P,D)
assert inv(P)==inv(D)
put('CLOSURE1148.json',dict(utc=utc(),terminal=True,work_C=str(P),archive_D=str(D),payload_files=len(payload),total_files=len(payload)+2,C_D_byte_identical=True,report_sha256=sha(P/'REVIEW1148.txt'),verdict_sha256=sha(P/'verdict1148.json'),manifest_sha256=sha(P/'MANIFEST1148.json'),full_input_reverified=dict(file='INPUT-FINAL1148.json',sha256=sha(P/'INPUT-FINAL1148.json'),files_each_C_D=312,own_input_copy_identical=True),PDF_sha256=v['artifact']['pdf_sha256'],one_exact_manuscript_judgment=True,all_failures_and_adverses_preserved=True,no_input_Git_root_state_or_publication_mutation=True,no_editorial_acceptance=True))
shutil.copy2(P/'CLOSURE1148.json',D/'CLOSURE1148.json')
ci=inv(P);assert ci==inv(D) and len(ci)==len(payload)+2
assert {k:r for k,r in ci.items() if k not in ['MANIFEST1148.json','CLOSURE1148.json']}==payload
assert inv(roots[0])==inv(roots[1])==invs[0]
print(json.dumps(dict(terminal=True,C_D_identical_files=len(ci),payloads=len(payload),inputs312_C_D_reverified=True,report_sha256=sha(P/'REVIEW1148.txt'),verdict_sha256=sha(P/'verdict1148.json'),manifest_sha256=sha(P/'MANIFEST1148.json'),closure_sha256=sha(P/'CLOSURE1148.json'))))
