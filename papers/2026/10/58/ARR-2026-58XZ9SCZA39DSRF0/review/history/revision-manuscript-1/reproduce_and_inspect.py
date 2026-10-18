from pathlib import Path
from zipfile import ZipFile
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, urllib.request
import numpy, scipy, mpmath as mp
from pypdf import PdfReader

OUT = Path(__file__).resolve().parent
INPUT = OUT.parent / 'input'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
original = {p.name:dict(bytes=p.stat().st_size,sha256=digest(p)) for p in INPUT.iterdir()}
(OUT/'reviewed-inputs').mkdir(exist_ok=True)
for p in INPUT.iterdir(): shutil.copy2(p, OUT/'reviewed-inputs'/p.name)
frozen=OUT/'supplement-frozen'; frozen.mkdir(exist_ok=True)
rerun=OUT/'supplement-rerun'; rerun.mkdir(exist_ok=True)
with ZipFile(INPUT/'supplement.zip') as z:
    members=z.namelist()
    assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in members)
    for n in members:
        assert len(Path(n).parts)==1
        (frozen/n).write_bytes(z.read(n))
        (rerun/n).write_bytes(z.read(n))
manifest=json.loads((frozen/'manifest.json').read_text(encoding='utf-8'))
print('MANIFEST',json.dumps(manifest))
run=subprocess.run([sys.executable,'-B',str(rerun/'verify_escape.py')],cwd=rerun,capture_output=True,text=True)
(OUT/'reproduction-stdout.txt').write_text(run.stdout,encoding='utf-8')
(OUT/'reproduction-stderr.txt').write_text(run.stderr,encoding='utf-8')
assert run.returncode==0,run.stderr
before=json.loads((frozen/'verification-1.json').read_text())
after=json.loads((rerun/'verification-1.json').read_text())
time_before=before.pop('generated_at');time_after=after.pop('generated_at')
assert before==after, 'Unexpected differences besides generated_at'

mp.mp.dps=90
def g(x): return mp.log(x+1,2)+x*mp.log1p(1/x)/mp.log(2)
def h(x): return -x*mp.log(x,2)-(1-x)*mp.log(1-x,2) if 0<x<1 else mp.mpf(0)
def f(x,d): return 2*x*mp.log(d,2)+(1+x)*h(x/(1+x))
published=[['0.988103','6.902738','7.055326'],['0.481708','3.050744','3.097662'],['0.204542','1.250089','1.264588'],['0.080424','0.479120','0.483701'],['0.030475','0.178365','0.179808'],['0.004045','0.023069','0.023213']]
table=[]
for i,row in enumerate(after['asymptotics']['rows']):
    N=mp.mpf(row['N']); K=int(mp.ceil(mp.sqrt(N)));m=N-K
    d=int(mp.ceil(2*(m+1)*mp.log(N+1))); logr=-mp.log1p(1/m);t=mp.exp(d*logr)
    s=g(m)+mp.log1p(-t)/mp.log(2)+d*t/(1-t)*logr/mp.log(2)
    a=g(N)-s;delta=mp.mpf(3)/K
    bounds=[mp.mpf('.7')*a+h(delta),mp.mpf('.4')*a+f(delta,d),mp.mpf('1.4')*a+f(delta,d)]
    ceilings=[mp.ceil(x*10**6)/10**6 for x in bounds]
    assert ceilings==list(map(mp.mpf,published[i]))
    assert int(row['d'])==d and t<=(N+1)**-2
    table.append(dict(N=int(N),K=K,d=d,bounds_60_digits=[mp.nstr(x,60) for x in bounds],published_upward_rounding=published[i],all_upward_rounding_correct=True))
save('reproduction-results.json',dict(generated_at=datetime.now(timezone.utc).isoformat(),python=sys.version,numpy=numpy.__version__,scipy=scipy.__version__,mpmath=mp.__version__,exit_code=run.returncode,comparison_excluded_fields=['generated_at'],original_generated_at=time_before,rerun_generated_at=time_after,all_other_json_fields_identical=True,summary=after['summary'],table_independent_precision_digits=90,table=table,input_hashes=original))

sources=OUT/'sources';sources.mkdir(exist_ok=True)
url='https://arxiv.org/pdf/quant-ph/0211170v2'
pdf=sources/'holevo-2003-v2.pdf'
with urllib.request.urlopen(url,timeout=45) as response: data=response.read()
assert data.startswith(b'%PDF');pdf.write_bytes(data)
r=PdfReader(pdf)
(sources/'holevo-2003-v2.txt').write_text('\n\n'.join(f'PAGE {i+1}\n'+(p.extract_text() or '') for i,p in enumerate(r.pages)),encoding='utf-8')
save('new-source.json',dict(url=url,downloaded_at=datetime.now(timezone.utc).isoformat(),sha256=digest(pdf),bytes=pdf.stat().st_size,pages=len(r.pages),checked='Proposition 3, output-entropy condition (14), formula (20). Bibliography correction verified independently on publisher SIAM DOI 10.1137/S0040585X97980415.'))
main=PdfReader(INPUT/'main.pdf')
(OUT/'main-extracted.txt').write_text('\n\n'.join(f'PAGE {i+1}\n'+(p.extract_text() or '') for i,p in enumerate(main.pages)),encoding='utf-8')
assert len(main.pages)==7
assert original=={p.name:dict(bytes=p.stat().st_size,sha256=digest(p)) for p in INPUT.iterdir()}
save('input-integrity-initial.json',dict(inputs=original,unchanged_after_execution=True))
print(json.dumps(dict(summary=after['summary'],table_checks=len(table),identical_except_generated_at=True,source_sha256=digest(pdf),pages=len(main.pages))))
