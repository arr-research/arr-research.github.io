from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile

def build_from_pin(pin, source_dir, title, hashes):
    os.environ.update(TZ="UTC", LC_ALL="C", FORCE_SOURCE_DATE="1", GIT_TERMINAL_PROMPT="0", DEBIAN_FRONTEND="noninteractive")
    root = Path(tempfile.mkdtemp(dir="/content", prefix="programme-pdf-"))
    evidence = root / "evidence"
    evidence.mkdir()
    def run(*cmd, cwd=root, filename=None):
        with (evidence/(filename or "setup.log")).open("ab") as log:
            subprocess.run(cmd, cwd=cwd, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=600)
    def digest(data):
        return hashlib.sha256(data).hexdigest()
    def out(*cmd, cwd=root):
        return subprocess.check_output(cmd, cwd=cwd, timeout=180)
    report = dict(source_sha=pin, inputs=hashes, started_at=datetime.now(timezone.utc).isoformat())
    dest = Path("/content/programme-pdf-proof.zip")
    if dest.exists():
        raise RuntimeError("Existing archive must be reconciled before another run")
    try:
        if not (shutil.which("pdflatex") and shutil.which("pdftoppm") and shutil.which("kpsewhich") and subprocess.run(["kpsewhich","lmodern.sty"],capture_output=True).returncode==0):
            run("apt-get","-o","Acquire::Retries=1","-o","Acquire::http::Timeout=20","update","-qq")
            run("apt-get","-o","Acquire::Retries=1","-o","Acquire::http::Timeout=20","install","-y","--no-install-recommends","texlive-latex-extra","texlive-fonts-recommended","lmodern","poppler-utils")
        pdfs=[]
        for label in ("a","b"):
            clone=root/("clone-"+label)
            run("git","init","-q",str(clone))
            run("git","remote","add","origin","https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git",cwd=clone)
            run("git","-c","protocol.version=2","fetch","-q","--depth=1","--filter=blob:none","origin",pin,cwd=clone)
            if out("git","rev-parse","FETCH_HEAD",cwd=clone).decode().strip()!=pin:
                raise ValueError("Fetched source commit differs")
            run("git","checkout","FETCH_HEAD","--",source_dir,cwd=clone)
            build=clone/"build"
            build.mkdir()
            for name, expected in hashes.items():
                raw=(clone/source_dir/name).read_bytes()
                if digest(raw)!=expected: raise ValueError(name)
                (build/name).write_bytes(raw)
            os.environ["SOURCE_DATE_EPOCH"]=out("git","show","-s","--format=%ct",pin,cwd=clone).decode().strip()
            (build/"driver.tex").write_text("\\pdfinfoomitdate=1\\relax\n\\pdftrailerid{}\n\\pdfsuppressptexinfo=15\\relax\n\\input{"+title+".tex}\n")
            for n in range(3):
                run("pdflatex","-no-shell-escape","-halt-on-error","-interaction=nonstopmode","driver.tex",cwd=build,filename=f"build-{label}-pass-{n+1}.txt")
            log=(build/"driver.log").read_bytes()
            (evidence/f"build-{label}.log").write_bytes(log)
            if re.search(rb"undefined references|Reference .*undefined|Citation .*undefined|multiply defined|Rerun to get cross-references right",log,re.I):raise ValueError("Unresolved final TeX references")
            pdfs.append((build/"driver.pdf").read_bytes())
        if pdfs[0]!=pdfs[1] or not pdfs[0].startswith(b"%PDF-"): raise ValueError("The two PDFs differ or are invalid")
        pdf=evidence/"paper.pdf";pdf.write_bytes(pdfs[0])
        (evidence/"toolchain.txt").write_bytes(out("pdflatex","--version"))
        (evidence/"pdfinfo.txt").write_bytes(out("pdfinfo",str(pdf)))
        run("pdftotext","-layout",str(pdf),str(evidence/"paper.txt"))
        pages=evidence/"pages";pages.mkdir()
        run("pdftoppm","-scale-to","1500","-jpeg","-jpegopt","quality=86",str(pdf),str(pages/"page"))
        count=int(re.search(rb"(?m)^Pages:\s+(\d+)",(evidence/"pdfinfo.txt").read_bytes()).group(1))
        if len(list(pages.glob("*.jpg")))!=count: raise ValueError("Rendered page count differs")
        report.update(status="reproduced",pages=count,pdf_sha256=[digest(x) for x in pdfs],pdf_bytes=len(pdfs[0]))
    except Exception as exc:
        report.update(status="failed",error=str(exc))
    report["finished_at"]=datetime.now(timezone.utc).isoformat()
    (evidence/"production.json").write_text(json.dumps(report,indent=2)+"\n")
    with zipfile.ZipFile(dest,"w",zipfile.ZIP_DEFLATED) as z:
        for path in sorted(evidence.rglob("*")):
            if path.is_file(): z.write(path,path.relative_to(evidence))
    print(json.dumps(report,sort_keys=True),flush=True)
    print("archive_sha256",digest(dest.read_bytes()),flush=True)

build_from_pin(*json.loads('["59794083537c96743b7b8582b9c8734ccbea42a1", "papers/stationary-weighting354/research/2026-11-19-bulk-shell-threshold", "bulk-shell", {"bulk-shell.tex": "aa186fa288784a80ef7ff7fad59f99dcd53770f506d81eef421fa661bf09057a"}]'))
