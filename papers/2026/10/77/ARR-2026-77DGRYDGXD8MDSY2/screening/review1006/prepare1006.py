"""Validate frozen1006/1005 inputs and create review-owned copies only."""
from pathlib import Path
import datetime,difflib,hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
SRC=Path('C:/Trabajo/airr/2026-10-27_sharp-petz1005')
D_SRC=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp-petz1005')
INP=Path('C:/Trabajo/airr/2026-10-27_sharp1006-input')
D_INP=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp1006-input')
PRIOR=Path('D:/Proyectos/airr-investigacion/2026-10-27_sharp998-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
    with (ROOT/n).open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2)
expected={'INPUT1006.json':'fdb81ba8044f76644e9a7a207c7b00a679cfd561f4ca21390a186932a02221e7',
 'RUBRIC1006.txt':'3b9a30f541ff57e69cd02b73dac706358d24d5244f3a0ecf94050c3ecfe4ab5b',
 'main.pdf':'b4728f44f7af59809be26e0eba957336695ff34cfc3cb10c17fcfa06ffb93381',
 'main.tex':'12be5b4e8de9b004082f822b43adc0ae08d4718f8e4449bacdd18683040b7d8a',
 'MANIFEST1005.json':'7a990d013c1318008357ecbdbb907da9eb0f7e09d383558c32e426f00f465842'}
top=[]
for n,h in expected.items():
    for loc,base in [('C',INP if n.startswith(('INPUT','RUBRIC')) else SRC),('D',D_INP if n.startswith(('INPUT','RUBRIC')) else D_SRC)]:
        p=base/n
        top.append({'location':loc,'path':str(p),'sha256':sha(p),'expected':h,'valid':sha(p)==h})
manifest=json.loads((SRC/'MANIFEST1005.json').read_text(encoding='utf-8-sig'))
rows=[]
for x in manifest['files']:
    row={'path':x['path'],'expected':x['sha256']}
    for label,base in [('C',SRC),('D',D_SRC)]:
        p=base/x['path']
        row[label]={'sha256':sha(p),'bytes':p.stat().st_size,'valid':sha(p)==x['sha256'] and p.stat().st_size==x['bytes']}
    rows.append(row)
artifact_identity=[]
for p in sorted((SRC/'artifacts').iterdir()):
    old=PRIOR/'reproduction'/p.name
    artifact_identity.append({'name':p.name,'current':sha(p),'prior998_copy':sha(old),'identical':sha(p)==sha(old)})
prior_manifest=json.loads((PRIOR/'MANIFEST998.json').read_text(encoding='utf-8-sig'))
prior_valid=all(sha(PRIOR/x['path'])==x['sha256'] for x in prior_manifest['files'])
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'top':top,'payloads':rows,'artifact_identity_to998':artifact_identity,
 'prior998_manifest_files_valid':prior_valid,'prior998_report_sha256':sha(PRIOR/'REVIEW998.txt')}
save('INPUT-VERIFIED1006.json',result)
assert len(rows)==21 and all(x['valid'] for x in top)
assert all(x['C']['valid'] and x['D']['valid'] for x in rows)
assert len(artifact_identity)==10 and all(x['identical'] for x in artifact_identity)
assert prior_valid and sha(PRIOR/'REVIEW998.txt')=='a490d74c3b6b6c4f7cbace1898e55835845c7058d754b3fdaeb51319569fe855'
for directory in ['input','qa','reproduction','public-supplement']:(ROOT/directory).mkdir(exist_ok=False)
for n in expected:
    base=INP if n.startswith(('INPUT','RUBRIC')) else SRC
    shutil.copy2(base/n,ROOT/'input'/n)
shutil.copy2(SRC/'CHANGES1005.json',ROOT/'input'/'CHANGES1005.json')
for p in (SRC/'artifacts').iterdir():shutil.copy2(p,ROOT/'reproduction'/p.name)
old=(PRIOR/'input'/'main.tex').read_text(encoding='utf-8')
new=(ROOT/'input'/'main.tex').read_text(encoding='utf-8')
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='frozen995/main.tex',tofile='frozen1005/main.tex'))
(ROOT/'SOURCE-DIFF1006.txt').write_text(diff,encoding='utf-8')
save('INITIAL-INCIDENT1006.json',{'incident':'First read attempted CHANGES1005.txt, which does not exist. INPUT1006 and manifest identify CHANGES1005.json; subsequent access uses that actual path.','effect':'Read-only file-not-found; no mutation or scientific result affected.','retained':True})
print(json.dumps({'payloads_verified_C_D':len(rows),'unchanged_artifacts':len(artifact_identity),'prior998_intact':prior_valid,'diff_lines':len(diff.splitlines())}))
