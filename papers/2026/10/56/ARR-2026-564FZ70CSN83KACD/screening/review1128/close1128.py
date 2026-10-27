from pathlib import Path
import json,hashlib,datetime,shutil
from pypdf import PdfReader
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1128-review')
CIN=Path(r'C:\Trabajo\airr\2026-10-27_simplex1127')
DIN=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1127')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x): (P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def inv(root):
    return {p.relative_to(root).as_posix():dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(root.rglob('*')) if p.is_file()}
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
expected_manifest='aeca3b9649d3785ec5f6db930d2d08a2a7b24234b43a0fad14b7a3c4a554b7cf'
input_receipts=[]
inventories=[]
for root in [CIN,DIN,P/'input']:
    assert sha(root/'MANIFEST1127.json')==expected_manifest
    m=read(root/'MANIFEST1127.json');assert len(m['files'])==223
    actual=inv(root);expected={row['path']:dict(bytes=row['bytes'],sha256=row['sha256']) for row in m['files']}
    expected['MANIFEST1127.json']=dict(bytes=(root/'MANIFEST1127.json').stat().st_size,sha256=expected_manifest)
    assert actual==expected and len(actual)==224
    inventories.append(actual)
    input_receipts.append(dict(root=str(root),file_count=224,payload_count=223,exact_inventory=True,all_bytes_and_hashes_passed=True,files=[dict(path=p,**v) for p,v in actual.items()]))
assert inventories[0]==inventories[1]==inventories[2]
assert len(PdfReader(P/'input/manuscript.pdf').pages)==12
put('INPUT-FINAL1128.json',dict(utc=utc(),all_passed=True,original_C_D_and_review_copy_identical=True,original_inputs_unchanged=True,roots=input_receipts))
v=read(P/'verdict1128.json')
assert v['report']['sha256']==sha(P/'REVIEW1128.txt')
assert v['artifact']['pdf_sha256']==sha(P/'input/manuscript.pdf')
assert v['artifact']['pdf_bytes']==(P/'input/manuscript.pdf').stat().st_size==383617
assert v['artifact']['tex_sha256']==sha(P/'input/main.tex')
assert v['scientific_importance_airr_0_10']==6.5 and v['overall_millennium_0_10']==6.3 and v['technical_quality_0_10']==8.8
assert len(v['criteria_1_5'])==5 and all(1<=x['rating_1_5']<=5 for x in v['criteria_1_5'].values())
assert len(v['objections'])==5 and not v['unresolved_material_objections']
assert all(v['observed_configuration'][k] is None for k in ['effective_model_id','effective_reasoning_effort'])
assert v['recommendation']['editorial_acceptance'] is False
assert read(P/'replay/REPLAY1124.json')['status']=='pass' and read(P/'OWN1128.json')['all_passed']
assert sha(P/'RUBRIC1128.md')=='41829e068687a57afd35eaa9aa5afd99a1f09a8f651bc522dbd871f0b31ff750'
for n in ['OWN-FAILURE-INITIAL1128.json','OWN-FAILURE-SECOND1128.json','own1128_initial.py','own1128_second.py']:
    assert (P/n).is_file()
required=['REVIEW1128.txt','verdict1128.json','PROVENANCE1128.json','READINGS1128.json','INCIDENTS1128.json','REPRODUCTION1128.json','INPUT-INITIAL1128.json','INPUT-FINAL1128.json','CURATION-RECEIPT1128.json','HISTORY-CHECK1128.json']
assert all((P/n).is_file() for n in required)
# No corpus downloaded to this review: primary source byte receipts only.
# Validate only own JSON metadata; archival originals remain untouched, even if historical failures.
validated=[]
for q in P.glob('*.json'):
    read(q);validated.append(q.name)
put('VALIDATION1128.json',dict(utc=utc(),all_passed=True,own_JSON_files_parsed=sorted(validated),report_verdict_binding_valid=True,exact_PDF_binding_valid=True,all_five_objections_preserved=True,three_separate_scores_and_five_criteria_valid=True,failure_versions_retained=True,replay_and_own_controls_pass=True,scope='Local scientific dossier checks, not ARR native schema validation or editorial eligibility determination.'))
assert not (P/'MANIFEST1128.json').exists() and not (P/'CLOSURE1128.json').exists()
assert not D.exists(), 'Archive target already exists; do not overwrite another dossier.'
payload=inv(P)
assert 'MANIFEST1128.json' not in payload and 'CLOSURE1128.json' not in payload
put('MANIFEST1128.json',dict(utc=utc(),scope='All review dossier payloads including immutable input copy, own evidence, failed attempts and scripts; excludes this manifest and closure to avoid self-reference.',payload_count=len(payload),files=[dict(path=p,**v) for p,v in payload.items()],source_pdf_sha256=v['artifact']['pdf_sha256'],source_manifest_sha256=expected_manifest))
shutil.copytree(P,D)
assert inv(P)==inv(D)
closure=dict(utc=utc(),terminal=True,work_root=str(P),archive_root=str(D),review_payload_count=len(payload),review_total_files=len(payload)+2,manifest_sha256=sha(P/'MANIFEST1128.json'),report_sha256=sha(P/'REVIEW1128.txt'),verdict_sha256=sha(P/'verdict1128.json'),pdf_sha256=v['artifact']['pdf_sha256'],full_input_reverification=dict(file='INPUT-FINAL1128.json',sha256=sha(P/'INPUT-FINAL1128.json'),source_C_and_D_224_files_exact=True,review_input_copy_identical=True),archive_C_D_byte_identical=True,closure_hash_self_reference_avoided=True,failed_attempts_and_all_adverses_retained=True,scientific_judgment_final=True,editorial_acceptance=False,publication=False,Git_root_state_or_original_inputs_modified=False)
put('CLOSURE1128.json',closure)
shutil.copy2(P/'CLOSURE1128.json',D/'CLOSURE1128.json')
ci=inv(P);di=inv(D)
assert ci==di and len(ci)==closure['review_total_files']
assert {p:v for p,v in ci.items() if p not in ['MANIFEST1128.json','CLOSURE1128.json']}==payload
# One last read-only integrity comparison of both original roots after archive copy.
assert inv(CIN)==inv(DIN)==inventories[0]
print(json.dumps(dict(terminal=True,C_D_identical_files=len(ci),payload_files=len(payload),input_C_D_224_reverified=True,report_sha256=sha(P/'REVIEW1128.txt'),verdict_sha256=sha(P/'verdict1128.json'),manifest_sha256=sha(P/'MANIFEST1128.json'),closure_sha256=sha(P/'CLOSURE1128.json'),archive=str(D))))
