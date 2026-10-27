"""Freeze and validate review-owned copies, without running manuscript code."""
from pathlib import Path
import datetime,hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
SOURCES=[Path('C:/Trabajo/airr/2026-10-27_complete1030'),Path('D:/Proyectos/airr-investigacion/2026-10-27_complete1030')]
EXPECTED='720d64a12bd1847a33fbfe0d581bda4d4fa37d0e43f5684996449a968b5a07eb'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert all(sha(p/'FROZEN1030.json')==EXPECTED for p in SOURCES)
frozen=json.loads((SOURCES[0]/'FROZEN1030.json').read_text(encoding='utf-8'))
rows=[]
for base in SOURCES:
    for x in frozen['files']:
        p=base/x['path'];actual=sha(p)
        rows.append({'source':str(base),'path':x['path'],'sha256':actual,'bytes':p.stat().st_size,'valid':actual==x['sha256'] and p.stat().st_size==x['bytes']})
with (ROOT/'INPUT-VERIFIED1031.json').open('x',encoding='utf-8') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_sha256':EXPECTED,'payloads_per_copy':len(frozen['files']),'files':rows},f,ensure_ascii=False,indent=2)
assert all(x['valid'] for x in rows)
for name in ['input','qa','replay','sources']:(ROOT/name).mkdir(exist_ok=False)
for x in frozen['files']+[{'path':'FROZEN1030.json'}]:
    out=ROOT/'input'/x['path'];out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SOURCES[0]/x['path'],out)
print(json.dumps({'valid':True,'payloads_per_copy':len(frozen['files']),'pdf_sha256':sha(ROOT/'input/main.pdf')}))
