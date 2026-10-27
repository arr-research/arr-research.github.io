"""Close only review1006 after revalidating frozen sources and prior998."""
from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    with (ROOT/name).open('x',encoding='utf-8') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
assert ROOT==Path('C:/Trabajo/airr/2026-10-27_sharp1006-review')
initial=json.loads((ROOT/'INPUT-VERIFIED1006.json').read_text(encoding='utf-8'))
tops=[]
for row in initial['top']:
    actual=sha(Path(row['path']))
    tops.append({'path':row['path'],'sha256':actual,'unchanged':actual==row['expected']})
source_rows=[]
for loc,base in [('C',Path('C:/Trabajo/airr/2026-10-27_sharp-petz1005')),('D',Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp-petz1005'))]:
    manifest=json.loads((base/'MANIFEST1005.json').read_text(encoding='utf-8-sig'))
    for row in manifest['files']:
        p=base/row['path'];actual=sha(p)
        source_rows.append({'location':loc,'path':row['path'],'sha256':actual,'valid':actual==row['sha256'] and p.stat().st_size==row['bytes']})
prior=[]
for loc,base in [('C',Path('C:/Trabajo/airr/2026-10-27_sharp998-review')),('D',Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review'))]:
    manifest=json.loads((base/'MANIFEST998.json').read_text(encoding='utf-8'))
    valid=all(sha(base/x['path'])==x['sha256'] and (base/x['path']).stat().st_size==x['bytes'] for x in manifest['files'])
    mh=sha(base/'MANIFEST998.json');rh=sha(base/'COPY-RECEIPT998.json')
    prior.append({'location':loc,'manifest_payloads':len(manifest['files']),'all_payloads_intact':valid,
                  'manifest_sha256':mh,'manifest_intact':mh=='c972b8f464d772b757661288bb8c4c984daa9d9c29e59d9d684193a8c346f5d3',
                  'receipt_sha256':rh,'receipt_intact':rh=='009bc6d880cebb4e29f6a8f9186a030160045f1ad1ef815feca860be2f9ee10e'})
public=json.loads((ROOT/'PUBLIC-VERIFIED1006-run01.json').read_text(encoding='utf-8'))
public_unchanged=all(sha(ROOT/'public-supplement'/x['name'])==x['sha256'] for x in public['selected_files'] if x['persisted'])
public_manifest_unchanged=sha(ROOT/'public-supplement'/'MANIFEST1001.json')==public['manifest_fetch']['sha256']
verdict=json.loads((ROOT/'verdict1006.json').read_text(encoding='utf-8'))
copied_inputs=all(sha(ROOT/'input'/name)==value for name,value in verdict['input_hashes'].items())
all_ok=all(x['unchanged'] for x in tops) and all(x['valid'] for x in source_rows) and all(x['all_payloads_intact'] and x['manifest_intact'] and x['receipt_intact'] for x in prior) and public_unchanged and public_manifest_unchanged and copied_inputs
save('CLOSING-VERIFIED1006.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'top_files':tops,'payloads':source_rows,'prior998':prior,
 'public_downloads_unchanged':public_unchanged,'public_manifest_unchanged':public_manifest_unchanged,'own_input_copies_unchanged':copied_inputs,'all_valid':all_ok})
assert all_ok and len(source_rows)==42
excluded={'MANIFEST1006.json','COPY-RECEIPT1006.json'}
files=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in excluded]
save('MANIFEST1006.json',{'review':'1006','scope':'Review-owned dossier of exact PDF1005; prior998 remains separate and unchanged.','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files,'excluded_to_avoid_self_reference':sorted(excluded)})
print(json.dumps({'payloads1005_valid_C_D':21,'prior998_intact_C_D':True,'manifest_files':len(files),
 'review_sha256':sha(ROOT/'REVIEW1006.txt'),'verdict_sha256':sha(ROOT/'verdict1006.json'),'manifest_sha256':sha(ROOT/'MANIFEST1006.json')},indent=2))
