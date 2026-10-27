from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parent
DEST=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp1006-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert ROOT==Path('C:/Trabajo/airr/2026-10-27_sharp1006-review')
def files(base):return {p.relative_to(base).as_posix():p for p in base.rglob('*') if p.is_file() and p.name!='COPY-RECEIPT1006.json'}
c,d=files(ROOT),files(DEST)
assert set(c)==set(d),{'only_C':sorted(set(c)-set(d)),'only_D':sorted(set(d)-set(c))}
rows=[{'path':name,'sha256':sha(c[name]),'identical':sha(c[name])==sha(d[name])} for name in sorted(c)]
assert all(x['identical'] for x in rows)
manifest=json.loads((ROOT/'MANIFEST1006.json').read_text(encoding='utf-8'))
assert all(sha(ROOT/x['path'])==x['sha256'] and (ROOT/x['path']).stat().st_size==x['bytes'] for x in manifest['files'])
receipt={'review':'1006','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(ROOT),'destination':str(DEST),
 'method':'robocopy /E /XJ followed by exact path-set and SHA256 comparison',
 'manifest_sha256':sha(ROOT/'MANIFEST1006.json'),'files_compared_before_receipt':len(rows),'final_files_in_each_copy':len(rows)+1,'all_identical':True,
 'receipt_itself':'Same serialized bytes written in C and D, excluded from self hash.','comparisons':rows}
data=(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
for base in [ROOT,DEST]:
    with (base/'COPY-RECEIPT1006.json').open('xb') as f:f.write(data)
assert sha(ROOT/'COPY-RECEIPT1006.json')==sha(DEST/'COPY-RECEIPT1006.json')
print(json.dumps({'all_files_identical':True,'files_in_each_copy':len(rows)+1,
 'review_sha256':sha(ROOT/'REVIEW1006.txt'),'verdict_sha256':sha(ROOT/'verdict1006.json'),'manifest_sha256':sha(ROOT/'MANIFEST1006.json'),'receipt_sha256':sha(ROOT/'COPY-RECEIPT1006.json')},indent=2))
