from pathlib import Path
import hashlib,json,shutil,datetime,subprocess
from pypdf import PdfReader
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
roots=[Path(r'C:\Trabajo\airr\2026-10-28_support1147'),Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1147')]
inventories=[]
for root in roots:
 assert sha(root/'MANIFEST1147.json')=='c56573d0dfdb11418250f3f3377b1e5dee7ed98c53c85c0e9d196c43ebf31c82'
 m=json.loads((root/'MANIFEST1147.json').read_text(encoding='utf-8'));assert len(m['files'])==311
 observed={q.relative_to(root).as_posix():{'bytes':q.stat().st_size,'sha256':sha(q)} for q in sorted(root.rglob('*')) if q.is_file()}
 expected={r['path']:{'bytes':r['bytes'],'sha256':r['sha256']} for r in m['files']}
 expected['MANIFEST1147.json']={'bytes':(root/'MANIFEST1147.json').stat().st_size,'sha256':sha(root/'MANIFEST1147.json')}
 assert observed==expected and len(observed)==312
 inventories.append(observed)
assert inventories[0]==inventories[1]
put('INPUT-INITIAL1148.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_passed=True,files_C_D_exact=312,roots=list(map(str,roots)),files=inventories[0]))
shutil.copytree(roots[0],P/'input')
for n in ['RUBRIC1148.md','SOURCE1148.json']:
 q=Path(r'C:\Trabajo\airr\2026-10-28_review1148-preparation')/n
 if n.endswith('.md'):assert sha(q)=='41829e068687a57afd35eaa9aa5afd99a1f09a8f651bc522dbd871f0b31ff750'
 shutil.copy2(q,P/n)
r=PdfReader(P/'input/manuscript.pdf');assert len(r.pages)==15
(P/'PDF-TEXT1148.txt').write_text('\n\n'.join('=== PAGE '+str(i+1)+' ===\n'+pg.extract_text() for i,pg in enumerate(r.pages)),encoding='utf-8')
(P/'qa').mkdir()
subprocess.run(['pdftoppm','-r','95','-png',str(P/'input/manuscript.pdf'),str(P/'qa/page')],check=True,capture_output=True)
print('312files C/D exact; own copy complete; PDF15pages extracted/rendered.')
