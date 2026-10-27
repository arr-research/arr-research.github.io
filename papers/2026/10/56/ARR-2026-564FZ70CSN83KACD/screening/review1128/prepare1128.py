from pathlib import Path
import hashlib,json,shutil,datetime,subprocess
from pypdf import PdfReader
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
C=Path(r'C:\Trabajo\airr\2026-10-27_simplex1127');D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1127')
rows=[]
for root in [C,D]:
 assert sha(root/'MANIFEST1127.json')=='aeca3b9649d3785ec5f6db930d2d08a2a7b24234b43a0fad14b7a3c4a554b7cf'
 m=json.loads((root/'MANIFEST1127.json').read_text(encoding='utf-8'));assert len(m['files'])==223
 expected={x['path'] for x in m['files']}|{'MANIFEST1127.json'}
 observed={q.relative_to(root).as_posix() for q in root.rglob('*') if q.is_file()};assert expected==observed
 for x in m['files']:
  q=root/x['path'];assert q.stat().st_size==x['bytes'] and sha(q)==x['sha256']
 rows.append({'root':str(root),'exact_inventory':True,'file_count':224,'all_sizes_hashes_passed':True,'manifest_sha256':sha(root/'MANIFEST1127.json'),'payloads':m['files']})
put('INPUT-INITIAL1128.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_passed':True,'roots':rows})
shutil.copytree(C,P/'input')
rubric=Path(r'C:\Trabajo\airr\2026-10-27_review1128-preparation')
assert sha(rubric/'RUBRIC1128.md')=='41829e068687a57afd35eaa9aa5afd99a1f09a8f651bc522dbd871f0b31ff750'
for n in ['RUBRIC1128.md','SOURCE1128.json']:shutil.copy2(rubric/n,P/n)
r=PdfReader(P/'input/manuscript.pdf');assert len(r.pages)==12
(P/'PDF-TEXT1128.txt').write_text('\n\n'.join('=== PAGE '+str(i+1)+' ===\n'+p.extract_text() for i,p in enumerate(r.pages)),encoding='utf-8')
(P/'qa').mkdir()
subprocess.run(['pdftoppm','-r','95','-png',str(P/'input/manuscript.pdf'),str(P/'qa/page')],check=True,capture_output=True)
put('PREPARATION1128.json',{'input_file_count':224,'page_count':12,'pdf_sha256':sha(P/'input/manuscript.pdf'),'tex_sha256':sha(P/'input/main.tex'),'rubric_sha256':sha(P/'RUBRIC1128.md'),'external_input_mutated':False})
print('Input224filesC/Dverified, copied, PDF12pages extracted/rendered.')
