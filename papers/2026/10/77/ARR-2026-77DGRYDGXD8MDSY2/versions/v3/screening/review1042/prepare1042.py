from pathlib import Path
import hashlib,json,datetime,shutil,difflib
ROOT=Path(__file__).resolve().parent
C=Path(r'C:\Trabajo\airr\2026-10-27_corrected1041');D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_corrected1041')
old=Path(r'C:\Trabajo\airr\2026-10-27_complete1031-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(name,o):(ROOT/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
expected='150241ae3fb565cc5217c12e2d651e2ecce64020996caf12ce246009ef5e0d93'
checks=[]
for base in [C,D]:
    assert sha(base/'FROZEN1041.json')==expected
    m=json.loads((base/'FROZEN1041.json').read_text(encoding='utf-8'))
    for f in m['files']:
        p=base/f['path'];r={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'pass':sha(p)==f['sha256'] and p.stat().st_size==f['bytes']};checks.append(r);assert r['pass']
put('INPUT-INITIAL1042.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_sha256_C_D':expected,'checks':checks,'all_passed':True})
for f in m['files']+[{'path':'FROZEN1041.json'}]:
    q=ROOT/'input'/f['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(C/f['path'],q)
oldfiles=[]
for p in sorted(old.rglob('*')):
    if p.is_file():
        q=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1031-review')/p.relative_to(old)
        assert sha(p)==sha(q)
        oldfiles.append({'path':p.relative_to(old).as_posix(),'sha256':sha(p)})
assert len(oldfiles)==140 and sha(old/'REVIEW1031.txt')=='bb4833edd109d00c475289fa3d77fa9d85d025f756fb835b9347aca4ef70fe6e'
put('PRIOR1031-BASELINE1042.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all140_C_D_identical':True,'files':oldfiles})
ref=ROOT/'prior';ref.mkdir(exist_ok=True)
for name in ['REVIEW1031.txt','verdict1031.json','PROVENANCE1031.json','DOEBLIN-DEFINITION1031.json','doeblin_definition1031.py','READINGS1031.json','RUBRIC1031.md','INCIDENTS1031.json']:
    shutil.copy2(old/name,ref/name)
rows=[];diff=[]
for name in ['main.tex','sections/context.tex','sections/order.tex','sections/qubit.tex']:
    a=old/'input'/name;b=C/name
    rows.append({'path':name,'old_sha256':sha(a),'new_sha256':sha(b),'identical':sha(a)==sha(b)})
    diff.extend(difflib.unified_diff(a.read_text(encoding='utf-8').splitlines(True),b.read_text(encoding='utf-8').splitlines(True),fromfile='1030/'+name,tofile='1041/'+name))
(ROOT/'INDEPENDENT-SOURCE-DIFF1042.txt').write_text(''.join(diff),encoding='utf-8')
put('SOURCE-COMPARISON1042.json',{'scope':'Independent source diff, exact predecessor source copies in sealed1031 dossier','files':rows})
(ROOT/'qa').mkdir(exist_ok=True)
print('Initial checks passed:26 input payloads, two frozen manifests,140 prior dossier files inC/D. Own copy and independent source diff created.')
