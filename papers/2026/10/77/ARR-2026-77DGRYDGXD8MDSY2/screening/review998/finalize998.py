"""Verify frozen sources again and seal only this review dossier."""
from pathlib import Path
import datetime, hashlib, json

ROOT=Path(__file__).resolve().parent
SOURCE=Path('C:/Trabajo/airr/2026-10-27_sharp-petz995')
ARCHIVE_SOURCE=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp-petz995')
INPUT=Path('C:/Trabajo/airr/2026-10-27_sharp998-input')
ARCHIVE_INPUT=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-input')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name, data):
    with (ROOT/name).open('x',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
        f.write('\n')

assert ROOT==Path('C:/Trabajo/airr/2026-10-27_sharp998-review')
assert not ROOT.is_symlink()
verdict=json.loads((ROOT/'verdict998.json').read_text(encoding='utf-8'))
top=[]
for name,expected in verdict['input_hashes'].items():
    for label,base in [('source_C',INPUT if name in ['INPUT998.json','RUBRIC998.txt'] else SOURCE),
                       ('source_D',ARCHIVE_INPUT if name in ['INPUT998.json','RUBRIC998.txt'] else ARCHIVE_SOURCE),
                       ('own_copy',ROOT/'input')]:
        path=base/name
        actual=sha(path)
        top.append({'location':label,'path':str(path),'sha256':actual,'expected':expected,'valid':actual==expected})

manifest=json.loads((SOURCE/'MANIFEST995.json').read_text(encoding='utf-8-sig'))
payloads=[]
for record in manifest['files']:
    row={'path':record['path'],'expected_sha256':record['sha256'],'expected_bytes':record['bytes']}
    for label,base in [('C',SOURCE),('D',ARCHIVE_SOURCE)]:
        path=base/record['path']
        row[label]={'sha256':sha(path),'bytes':path.stat().st_size}
        row[label]['valid']=row[label]['sha256']==record['sha256'] and row[label]['bytes']==record['bytes']
    payloads.append(row)

checks=json.loads((ROOT/'CONTROLS998.json').read_text(encoding='utf-8'))
replay=json.loads((ROOT/'REPRODUCTION998.json').read_text(encoding='utf-8-sig'))
closing={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'top_files':top,'payloads':payloads,'payload_count':len(payloads),
         'all_top_valid':all(x['valid'] for x in top),
         'all_payloads_valid_C_D':all(x['C']['valid'] and x['D']['valid'] for x in payloads),
         'own_controls_passed':checks['failures']==0,
         'all_reproduced_artifacts_identical':all(x['identical'] for x in replay),
         'unmanifested_source_files':'Not included in scientific input; no deletion or mutation performed.',
         'scope':'Content-hash revalidation; does not attest scientific independence or formal correctness.'}
save('CLOSING-VERIFIED998.json',closing)
assert len(payloads)==40 and closing['all_top_valid'] and closing['all_payloads_valid_C_D']
assert closing['own_controls_passed'] and closing['all_reproduced_artifacts_identical']
assert len(list((ROOT/'qa').glob('page-*.png')))==7
excluded={'MANIFEST998.json','COPY-RECEIPT998.json'}
files=[]
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and path.name not in excluded:
        files.append({'path':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'sha256':sha(path)})
save('MANIFEST998.json',{'review':'998','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                       'scope':'Own review dossier only; frozen source identified by copied INPUT998 and MANIFEST995.',
                       'files':files,'excluded_to_avoid_self_reference':sorted(excluded)})
print(json.dumps({'payloads_revalidated_C_D':40,'dossier_manifest_files':len(files),
                  'review_sha256':sha(ROOT/'REVIEW998.txt'),
                  'verdict_sha256':sha(ROOT/'verdict998.json'),
                  'manifest_sha256':sha(ROOT/'MANIFEST998.json')},indent=2))
