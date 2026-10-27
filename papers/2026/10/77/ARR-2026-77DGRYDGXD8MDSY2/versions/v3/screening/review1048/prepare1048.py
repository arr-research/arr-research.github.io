from pathlib import Path
import json,hashlib,datetime,shutil,difflib
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checks=[]
for base in [Path(r'C:\Trabajo\airr\2026-10-27_complete1047'),Path(r'D:\Proyectos\airr-investigacion\2026-10-27_complete1047')]:
    assert sha(base/'FROZEN1047.json')=='406dcccd5be71ac41d6c96a54fe3e415349b64d8c89a29d7fe043801661d835e'
    m=json.loads((base/'FROZEN1047.json').read_text(encoding='utf-8'))
    for f in m['files']:
        p=base/f['path'];ok=sha(p)==f['sha256'] and p.stat().st_size==f['bytes'];assert ok
        checks.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'pass':ok})
put('INPUT-INITIAL1048.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'payloads_per_copy':len(m['files']),'frozen_sha256':'406dcccd5be71ac41d6c96a54fe3e415349b64d8c89a29d7fe043801661d835e','all_passed':True,'checks':checks})
C=Path(r'C:\Trabajo\airr\2026-10-27_complete1047')
for f in m['files']+[{'path':'FROZEN1047.json'}]:
    q=ROOT/'input'/f['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(C/f['path'],q)
A=Path(r'C:\Trabajo\airr\2026-10-27_principal1044-audit');B=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1044-audit')
assert sha(A/'AUDIT1044.txt')=='4626addd8089c2d7acac69ec58f3a0cfa4d5bc3e38e51e3312994d6426462294'
assert sha(A/'MANIFEST1044.json')=='d3cd6160de60c3a8e79864767bff002ce7303ec95848427f7de1ebd7cbc354c3'
ac=[]
for p in sorted(A.rglob('*')):
    if p.is_file():
        assert sha(p)==sha(B/p.relative_to(A))
        q=ROOT/'audit1044'/p.relative_to(A);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
        ac.append({'path':p.relative_to(A).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
assert len(ac)==44
put('AUDIT1044-INITIAL1048.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'44_files_C_D_identical':True,'files':ac,'dependency':'Component audit read as shared-context evidence; not independent manuscript vote.'})
pol=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026\docs\MODEL_ASSESSMENT_POLICY.md')
shutil.copy2(pol,ROOT/'RUBRIC1048.md')
old=Path(r'C:\Trabajo\airr\2026-10-27_corrected1041');d=[]
for name in ['main.tex','sections/qubit.tex','sections/order.tex','sections/context.tex','sections/bkm.tex']:
    a=old/name;b=C/name
    d.extend(difflib.unified_diff(a.read_text(encoding='utf-8').splitlines(True) if a.exists() else [],b.read_text(encoding='utf-8').splitlines(True),fromfile='1041/'+name,tofile='1047/'+name))
(ROOT/'SOURCE-DIFF1048.txt').write_text(''.join(d),encoding='utf-8')
(ROOT/'qa').mkdir(exist_ok=True)
print('Verified20payloads plus frozen manifestC/D;44audit filesC/D. Created own input/audit copies, rubric and source diff.')
