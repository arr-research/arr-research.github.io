from pathlib import Path
import hashlib,json,datetime,difflib,shutil,subprocess
from pypdf import PdfReader
from PIL import Image,ImageChops
P=Path(__file__).resolve().parent
roots=[Path(r'C:\Trabajo\airr\2026-10-28_support1155'),Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1155')]
OLD=Path(r'C:\Trabajo\airr\2026-10-28_support1148-review')
OLDD=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1148-review')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def inv(root):return {p.relative_to(root).as_posix():dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(root.rglob('*')) if p.is_file()}
invs=[]
for root in roots:
 assert sha(root/'MANIFEST1155.json')=='7f8afab0e1749764ec7157eb1cf144b618813bbbf8b6e50de86a859f507f1231'
 m=json.loads((root/'MANIFEST1155.json').read_text(encoding='utf-8'));assert len(m['files'])==23
 expected={r['path']:dict(bytes=r['bytes'],sha256=r['sha256']) for r in m['files']}
 expected['MANIFEST1155.json']=dict(bytes=(root/'MANIFEST1155.json').stat().st_size,sha256=sha(root/'MANIFEST1155.json'))
 actual=inv(root);assert actual==expected and len(actual)==24;invs.append(actual)
assert invs[0]==invs[1]
oldinv=inv(OLD);assert oldinv==inv(OLDD) and len(oldinv)==435
oldm=json.loads((OLD/'MANIFEST1148.json').read_text(encoding='utf-8'))
for r in oldm['files']:assert oldinv[r['path']]==dict(bytes=r['bytes'],sha256=r['sha256'])
assert sha(OLD/'REVIEW1148.txt')=='bda1b7625f92a44f7dd23eeac524929b4f485d518e977a015276b3f6ef2493f8'
assert sha(OLD/'verdict1148.json')=='a00ba996be7defcd9230f34fb0398fd9673cbf521907a8a3c28a39911aba5c1c'
put('INPUT-INITIAL1156.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),new_input_C_D_exact24=True,source_paths=list(map(str,roots)),files=invs[0],prior1148_C_D_exact435=True,prior1148_report_sha256=sha(OLD/'REVIEW1148.txt'),prior1148_verdict_sha256=sha(OLD/'verdict1148.json')))
shutil.copytree(roots[0],P/'input')
(P/'source1148').mkdir()
for n in ['REVIEW1148.txt','verdict1148.json','PROVENANCE1148.json','INCIDENTS1148.json','MANIFEST1148.json','CLOSURE1148.json','OWN1148.json']:
 shutil.copy2(OLD/n,P/'source1148'/n)
oldtex=OLD/'input/main.tex';newtex=P/'input/main.tex';a=oldtex.read_text(encoding='utf-8');b=newtex.read_text(encoding='utf-8')
diff=list(difflib.unified_diff(a.splitlines(),b.splitlines(),fromfile='1147/main.tex',tofile='1155/main.tex',lineterm=''))
changes=[x for x in diff if x[:1] in ['+','-'] and not x.startswith(('---','+++'))]
expected_old='-coherence $\\pm\\lambda c$, $\\lambda=-1/(n-1)$, and inactive eigenvalue'
expected_new='+coherence $\\pm\\lambda c$, $\\lambda=-1/(n-1)$, and, only for $n\\geq3$, inactive eigenvalue'
assert changes==[expected_old,expected_new],changes
(P/'OBSERVED-DELTA1156.diff').write_text('\n'.join(diff)+'\n',encoding='utf-8')
assert (P/'input/sections/general-support.tex').read_bytes()==(OLD/'input/sections/general-support.tex').read_bytes()
assert sha(newtex)=='b8c8304be70cd5c3d9bdf5c795e362e51c7561870bedd42bb2d7fa51a1ede314'
assert sha(P/'input/manuscript.pdf')=='5cf3e9a66c6d86063d68b92bb0494bb5186a73506da60935819ff9d0265be361'
ro=PdfReader(OLD/'input/manuscript.pdf');rn=PdfReader(P/'input/manuscript.pdf');assert len(ro.pages)==len(rn.pages)==15
textdiff=[]
for i,(x,y) in enumerate(zip(ro.pages,rn.pages),1):
 tx=x.extract_text();ty=y.extract_text()
 if tx!=ty:textdiff.append(i)
 if i==6:(P/'PAGE6-TEXT1156.txt').write_text(ty,encoding='utf-8')
assert textdiff==[6],textdiff
(P/'qa').mkdir()
subprocess.run(['pdftoppm','-r','95','-png',str(P/'input/manuscript.pdf'),str(P/'qa/page')],check=True,capture_output=True)
pixels=[]
for i in range(1,16):
 oldpng=OLD/f'qa/page-{i:02d}.png';newpng=P/f'qa/page-{i:02d}.png'
 x=Image.open(oldpng).convert('RGB');y=Image.open(newpng).convert('RGB');assert x.size==y.size
 box=ImageChops.difference(x,y).getbbox()
 pixels.append(dict(page=i,identical_pixels=box is None,difference_box=box,old_png_sha256=sha(oldpng),new_png_sha256=sha(newpng)))
assert [x['page'] for x in pixels if not x['identical_pixels']]==[6]
rawold=oldtex.read_bytes();rawnew=newtex.read_bytes()
put('VALIDATION1156.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_automated_passed=True,scope='O1delta/source/link/pixels only; not a new full scientific review',old_pdf_sha256=sha(OLD/'input/manuscript.pdf'),new_pdf_sha256=sha(P/'input/manuscript.pdf'),new_pdf_bytes=(P/'input/manuscript.pdf').stat().st_size,pages=15,semantic_source_changes=changes,section6_byte_identical=True,source_line_endings=dict(old_CRLF=rawold.count(b'\r\n'),new_CRLF=rawnew.count(b'\r\n'),old_LF=rawold.count(b'\n'),new_LF=rawnew.count(b'\n'),old_bytes=len(rawold),new_bytes=len(rawnew)),PDF_text_changed_pages=textdiff,pixel_comparison=pixels,own_original_compilation=False,source_input_unchanged=inv(roots[0])==invs[0] and inv(roots[1])==invs[1],prior_dossier_unchanged=inv(OLD)==oldinv and inv(OLDD)==oldinv))
print(json.dumps(dict(hashes_pass=True,only_semantic_change=changes,text_changed_pages=textdiff,pixel_changed_pages=[6],source_line_endings=dict(oldCRLF=rawold.count(b'\r\n'),newCRLF=rawnew.count(b'\r\n')),prior435files_unchanged=True)))
