"""Check exact archive copy, then create the same copy receipt in C and D."""
from pathlib import Path
import datetime, hashlib, json
ROOT=Path(__file__).resolve().parent
DEST=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert ROOT==Path('C:/Trabajo/airr/2026-10-27_sharp998-review')
def paths(base):
    return {p.relative_to(base).as_posix():p for p in base.rglob('*') if p.is_file() and p.name!='COPY-RECEIPT998.json'}
c,d=paths(ROOT),paths(DEST)
assert set(c)==set(d), {'only_C':sorted(set(c)-set(d)),'only_D':sorted(set(d)-set(c))}
comparisons=[{'path':k,'sha256_C':sha(c[k]),'sha256_D':sha(d[k]),'identical':sha(c[k])==sha(d[k])} for k in sorted(c)]
assert all(x['identical'] for x in comparisons)
manifest=json.loads((ROOT/'MANIFEST998.json').read_text(encoding='utf-8'))
for row in manifest['files']:
    assert sha(ROOT/row['path'])==row['sha256']
    assert (ROOT/row['path']).stat().st_size==row['bytes']
receipt={'review':'998','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'source':str(ROOT),'destination':str(DEST),
         'method':'robocopy /E /XJ followed by path-set and SHA256 comparison',
         'manifest_sha256':sha(ROOT/'MANIFEST998.json'),
         'files_compared_before_receipt':len(comparisons),
         'final_files_in_each_copy':len(comparisons)+1,
         'all_identical':True,
         'receipt_itself':'Same serialized bytes written to both copies; excluded from self hash.',
         'comparisons':comparisons}
data=(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
for base in [ROOT,DEST]:
    with (base/'COPY-RECEIPT998.json').open('xb') as f: f.write(data)
assert sha(ROOT/'COPY-RECEIPT998.json')==sha(DEST/'COPY-RECEIPT998.json')
print(json.dumps({'all_files_identical':True,'files_in_each_copy':len(comparisons)+1,
                  'review_sha256':sha(ROOT/'REVIEW998.txt'),
                  'verdict_sha256':sha(ROOT/'verdict998.json'),
                  'manifest_sha256':sha(ROOT/'MANIFEST998.json'),
                  'receipt_sha256':sha(ROOT/'COPY-RECEIPT998.json')},indent=2))
