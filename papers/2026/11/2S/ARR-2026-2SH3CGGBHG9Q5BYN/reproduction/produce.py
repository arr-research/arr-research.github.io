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

def build_supplement():
    pin = "6b0f3b6a5990912514fc980ab18f30abd4ca876f"
    source_dir = "papers/stationary-weighting354/research/2026-11-18-small-support"
    title = "local-return-supplement"
    hashes = {
        "endpoint-concentration.tex": "81bbd86cad822cecb9de4033c3c60f40917ff1eab9240f211b47a79dcdd80f2e",
        "finite-stationary-levels.tex": "8b1baa99c15a30a7d1fc2f6a3273edf9b1b492456ffa831cb0b8dfcd749335ce",
        "fractional-basis-recovery.tex": "4c4b7f4d864b71e4378145f48c97c8ec9beb48a7d84573d3364ff8c76c10c4df",
        "gap-without-matching.tex": "e4630908cde62d42cf5d13803701e484125a3e4d93da649f2478907def993dc0",
        "local-return-supplement.tex": "f84ef33debd61537eefdd526cff343d9ab289b89e06b50bad9d50f1c8b94c1ef",
        "single-stationary-spike.tex": "b39f8716b44b8aa587bcbf04dfae89a9887d6266e138b9693c52f17b8a1d5b63",
        "three-stationary-values.tex": "461e2b8d40d7c90ab205469f5a773c03179494cfcaa9d9478c85b28f0983d5d3",
    }
    os.environ.update(TZ="UTC", LC_ALL="C", FORCE_SOURCE_DATE="1", GIT_TERMINAL_PROMPT="0", DEBIAN_FRONTEND="noninteractive")
    root = Path(tempfile.mkdtemp(dir="/content", prefix="tep293-"))
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
    dest = Path("/content/tep293-supplement-proof.zip")
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
build_supplement()

