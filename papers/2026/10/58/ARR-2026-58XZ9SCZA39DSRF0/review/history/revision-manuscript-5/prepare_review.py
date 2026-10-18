from pathlib import Path
import hashlib,json,zipfile,difflib,shutil,subprocess
import fitz
root=Path(__file__).parent
out=root/'output'; out.mkdir(exist_ok=True)
work=out/'work'; work.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
inputs={p.name:{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted((root/'input').iterdir()) if p.is_file()}
(out/'input-hashes.json').write_text(json.dumps(inputs,indent=2),encoding='utf-8')
old=root.parent/'review-manuscript-4'
diff=''.join(difflib.unified_diff((old/'input/main.tex').read_text(encoding='utf-8').splitlines(True),(root/'input/main.tex').read_text(encoding='utf-8').splitlines(True),fromfile='manuscript-4',tofile='manuscript-5'))
(out/'changes-from-manuscript-4.diff').write_text(diff,encoding='utf-8')
for name,src in [('supplement',root/'input/supplement.zip'),('prior-supplement',old/'input/supplement.zip')]:
    dest=work/name; dest.mkdir(exist_ok=True)
    with zipfile.ZipFile(src) as z:
        for n in z.namelist():
            p=(dest/n).resolve()
            assert p.is_relative_to(dest.resolve())
        z.extractall(dest)
newfiles={str(p.relative_to(work/'supplement')).replace('\\','/'):p for p in (work/'supplement').rglob('*') if p.is_file()}
oldfiles={str(p.relative_to(work/'prior-supplement')).replace('\\','/'):p for p in (work/'prior-supplement').rglob('*') if p.is_file()}
comparison=[]
for n,p in newfiles.items():
    comparison.append({'path':n,'bytes':p.stat().st_size,'sha256':sha(p),'identical_to_manuscript_4':n in oldfiles and sha(p)==sha(oldfiles[n])})
(out/'supplement-comparison.json').write_text(json.dumps(comparison,indent=2),encoding='utf-8')
doc=fitz.open(root/'input/main.pdf')
(out/'pdf-text.txt').write_text('\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
pages=work/'pages'; pages.mkdir(exist_ok=True)
poppler=Path(r'C:\Users\lluis\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
subprocess.run([str(poppler),'-r','100','-png',str(root/'input/main.pdf'),str(pages/'page')],check=True,capture_output=True)
print(json.dumps({'pages':len(doc),'diff_lines':len(diff.splitlines()),'supplement':comparison},indent=2))
