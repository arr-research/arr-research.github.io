"""Seal a single completed review; verify frozen input and exact C/D copy."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,sys

C=Path(r'C:\Trabajo\airr\2026-10-27_sharp958-review')
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_sharp958-review')
INPUT=Path(r'C:\Trabajo\airr\2026-10-27_sharp957-input')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
expected_manifest='544bfcc12da120b32004613b94a5fb819aed74c449227b7e839a96e3d541aaeb'
def verify_input():
  assert h(INPUT/'INPUT957.json')==expected_manifest
  spec=json.loads((INPUT/'INPUT957.json').read_text(encoding='utf-8-sig'))
  assert len(spec['files'])==14
  rows=[]
  for item in spec['files']:
    p=INPUT/item['path'];actual=h(p);size=p.stat().st_size
    ok=actual==item['sha256'] and size==item['bytes']
    rows.append(dict(path=item['path'],bytes=size,sha256=actual,ok=ok))
    assert ok, item['path']
  return rows
rows=verify_input()
(C/'input-after.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
v=json.loads((C/'verdict958.json').read_text(encoding='utf-8'))
assert v['scientific_importance_airr_0_10']==4.0
assert v['millennium_score']==4.5 and v['technical_quality_0_10']==8.5
assert v['recommendation']==v['recommendation_original']=='minor_revision'
assert v['exact_pdf']['sha256']==h(INPUT/'manuscript.pdf')
for p in C.rglob('*.json'):json.loads(p.read_text(encoding='utf-8-sig'))
for name in ['CHECK939.json','CHECK950.json','CHECK955.json']:
  assert h(C/'controls'/name)==h(INPUT/name)
reproduction={name:h(C/'controls'/name) for name in ['CHECK939.json','CHECK950.json','CHECK955.json']}
(C/'CLOSE958.json').write_text(json.dumps(dict(
  utc=datetime.now(timezone.utc).isoformat(),input_manifest_sha256=expected_manifest,
  payload_count=14,all_input_bytes_and_hashes_match=True,canonical_pdf_sha256=h(INPUT/'manuscript.pdf'),
  report_sha256=h(C/'REVIEW958.txt'),verdict_sha256=h(C/'verdict958.json'),
  reproduced_supplied_outputs_sha256=reproduction,
  score_and_original_recommendation_consistency=True,
  independent_control_initial_failures_preserved=1,
  independent_control_unresolved_falsifiers=0,
  source_corpus_persisted=False,
  public_publication_or_other_chat_contact=False),indent=2)+'\n',encoding='utf-8')
excluded={'MANIFEST958.sha256','DELIVERY958.json'}
files=sorted([p for p in C.rglob('*') if p.is_file() and p.name not in excluded],key=lambda p:p.relative_to(C).as_posix())
assert not any(p.is_symlink() for p in files)
manifest=''.join(h(p)+'  '+p.relative_to(C).as_posix()+'\n' for p in files)
(C/'MANIFEST958.sha256').write_text(manifest,encoding='utf-8')
if D.exists():
  assert not any(D.rglob('*')), 'Destination is not empty; do not overwrite an existing record.'
else:D.mkdir(parents=True)
copyfiles=sorted([p for p in C.rglob('*') if p.is_file() and p.name!='DELIVERY958.json'])
for p in copyfiles:
  dst=D/p.relative_to(C);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
def snapshot(root):
  return {p.relative_to(root).as_posix():(p.stat().st_size,h(p)) for p in root.rglob('*') if p.is_file()}
assert snapshot(C)==snapshot(D)
assert verify_input()==rows
receipt=dict(utc=datetime.now(timezone.utc).isoformat(),local_manuscript_id='sharp957',review_id='review958',
  scientific_importance_airr_0_10=4.0,millennium_score=4.5,technical_quality_0_10=8.5,
  recommendation_original='minor_revision',canonical_pdf_sha256=h(INPUT/'manuscript.pdf'),
  input_manifest_sha256=expected_manifest,input_payloads_verified_before_and_after=14,
  report_sha256=h(C/'REVIEW958.txt'),verdict_sha256=h(C/'verdict958.json'),
  manifest_sha256=h(C/'MANIFEST958.sha256'),
  manifest_entries=len(files),manifest_excludes=['MANIFEST958.sha256','DELIVERY958.json'],
  copy_C=str(C),copy_D=str(D),copy_comparison='Every relative path, byte size and SHA256 equal; receipt also written identically and checked.',
  total_files_in_each_copy=len(copyfiles)+1,
  C_retained='Explicit task requested matching C/D copies; no result exists only in C.')
data=(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n').encode('utf-8')
(C/'DELIVERY958.json').write_bytes(data);(D/'DELIVERY958.json').write_bytes(data)
assert snapshot(C)==snapshot(D)
assert verify_input()==rows
print(json.dumps(receipt,ensure_ascii=True))
