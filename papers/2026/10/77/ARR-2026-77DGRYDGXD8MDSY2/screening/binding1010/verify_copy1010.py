from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parent
DEST=Path('D:/Proyectos/airr-investigacion/2026-10-27_petz1010-binding')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert ROOT==Path('C:/Trabajo/airr/2026-10-27_petz1010-binding')
def files(base):return {p.relative_to(base).as_posix():p for p in base.rglob('*') if p.is_file() and p.name!='COPY-RECEIPT1010.json'}
c,d=files(ROOT),files(DEST)
assert set(c)==set(d)
rows=[{'path':k,'sha256':sha(c[k]),'identical':sha(c[k])==sha(d[k])} for k in sorted(c)]
assert all(x['identical'] for x in rows)
manifest=json.loads((ROOT/'MANIFEST1010.json').read_text(encoding='utf-8'))
assert all(sha(ROOT/x['path'])==x['sha256'] for x in manifest['files'])
receipt={'binding':'1010','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(ROOT),'destination':str(DEST),
 'method':'robocopy /E /XJ and exact relative-path/SHA256 comparison','all_identical':True,'final_files_per_copy':len(rows)+1,
 'manifest_sha256':sha(ROOT/'MANIFEST1010.json'),'comparisons':rows,'receipt_itself':'Same serialized bytes written to both copies; excluded from self hash.'}
data=(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
for base in [ROOT,DEST]:
    with (base/'COPY-RECEIPT1010.json').open('xb') as f:f.write(data)
assert sha(ROOT/'COPY-RECEIPT1010.json')==sha(DEST/'COPY-RECEIPT1010.json')
print(json.dumps({'all_identical':True,'files_per_copy':len(rows)+1,'response_sha256':sha(ROOT/'model-response.json'),
 'binding_sha256':sha(ROOT/'BINDING1010.json'),'manifest_sha256':sha(ROOT/'MANIFEST1010.json'),'receipt_sha256':sha(ROOT/'COPY-RECEIPT1010.json')},indent=2))
