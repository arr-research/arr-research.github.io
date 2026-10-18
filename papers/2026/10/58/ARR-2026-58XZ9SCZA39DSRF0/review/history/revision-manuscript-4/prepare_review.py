from pathlib import Path
import hashlib,json,zipfile,shutil,subprocess,datetime
from pypdf import PdfReader
root=Path(r"C:\Trabajo\airr\2026-10-18_escape-energetico\review-manuscript-4")
inp=root/"input";out=root/"output";out.mkdir(exist_ok=False)
for n in ["reviewed-inputs","supplement","visual","reproduction","reused-evidence"]:(out/n).mkdir()
expected={"main.tex":"98b459adb42322fb564e10a581c816895ccfe6c5edf4cd97ab04e7a4416badf2",
"main.pdf":"04d8bb0d944fb667d67ab0a9fd59f1bcd2f8d79175d5a3de885274c250c25c5c",
"supplement.zip":"75d174a77777b584273a084442bb9cdfc5872e35785645183c2f4301da165aec"}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={}
for p in inp.iterdir():
 if p.is_file():
  h=sha(p)
  if p.name in expected:assert h==expected[p.name]
  files[p.name]=dict(bytes=p.stat().st_size,sha256=h)
  shutil.copy2(p,out/"reviewed-inputs"/p.name)
reader=PdfReader(inp/"main.pdf");assert len(reader.pages)==15
text="\n\n".join("PAGE "+str(i+1)+"\n"+(p.extract_text() or "") for i,p in enumerate(reader.pages))
(out/"main-extracted.txt").write_text(text,encoding="utf-8")
with zipfile.ZipFile(inp/"supplement.zip") as z:
 for item in z.infolist():
  target=(out/"supplement"/item.filename).resolve()
  assert target.is_relative_to((out/"supplement").resolve())
 z.extractall(out/"supplement")
old=root.parent/"review-manuscript-3"/"output"/"supplement"
zipinventory=[]
for p in sorted((out/"supplement").rglob("*")):
 if p.is_file():
  rel=p.relative_to(out/"supplement")
  oldp=old/rel
  zipinventory.append(dict(file=rel.as_posix(),bytes=p.stat().st_size,sha256=sha(p),
       identical_previous=oldp.is_file() and sha(oldp)==sha(p)))
(out/"input-check.json").write_text(json.dumps(dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=files,pages=15,supplement=zipinventory),indent=2),encoding="utf-8")
poppler=r"C:\Users\lluis\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"
subprocess.run([poppler,"-png","-r","100",str(inp/"main.pdf"),str(out/"visual"/"page")],check=True,capture_output=True)
print(json.dumps(dict(pages=15,files=files,supplement=zipinventory),indent=2))

