import json,hashlib
SOURCE='5e56b36a514357d4598f9b7f12c7d33b38b78628'
PREFIX='papers/phi-lemma/revision207/'
FILES={'phi_lemma.tex': '89237f2e1466764381265bdf5feccbc28b554a10f7f03931eaa5cb2766b08a2d', 'PhiMonotone.lean': 'ab9fc594ae6e87d8255cfeb01d7a6fe3875408706046d2f26dd1d8a8c88d8c1b', 'LEAN-VERIFICATION-LOG.txt': '7b2501b0ff34cb0ab8da49a5d081b1e6a13be7712c2079ce53bc6bb7b3645bc8', 'SOURCE207.json': 'a2025b83c621e561da049346532e8fc8d1b51c7dddf13581dba04fcd50de1462'}

import os,sys,time,traceback,subprocess,resource,zipfile,urllib.request
from datetime import datetime,timezone
from pathlib import Path
if not Path('/content').is_dir():raise RuntimeError('Own Colab Linux required')
out=Path('/content/tep207D');out.mkdir(exist_ok=False);os.chdir(out)
start=time.monotonic();report={'source_sha':SOURCE,'source_prefix':PREFIX,'source_hashes':FILES,'started_utc':datetime.now(timezone.utc).isoformat(),'tool_exits':{},'compute_units_billed':None,'formal_or_scientific_replay':False}
def run(args,name,timeout=240):
 p=subprocess.run(args,capture_output=True,timeout=timeout)
 (out/(name+'.stdout')).write_bytes(p.stdout);(out/(name+'.stderr')).write_bytes(p.stderr)
 tmp=out/(name+'.exit.tmp');tmp.write_text(str(p.returncode)+'\n');code=int(tmp.read_text().strip());os.replace(tmp,out/(name+'.exit'));report['tool_exits'][name]=code
 if code:raise RuntimeError(name+' exited '+str(code))
 return p.stdout.decode(errors='replace')
try:
 for name,digest in FILES.items():
  raw=urllib.request.urlopen('https://raw.githubusercontent.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/'+SOURCE+'/'+PREFIX+name,timeout=45).read()
  if hashlib.sha256(raw).hexdigest()!=digest:raise RuntimeError('Input hash mismatch '+name)
  (out/name).write_bytes(raw)
 run(['apt-get','-qq','update'],'apt-update',600)
 run(['apt-get','install','-y','-qq','texlive-latex-base','texlive-latex-recommended','texlive-fonts-recommended','lmodern','poppler-utils'],'apt-install',900)
 os.environ['SOURCE_DATE_EPOCH']='1794096000';os.environ['FORCE_SOURCE_DATE']='1'
 report['tex_version']=run(['pdflatex','--version'],'tex-version')
 run(['pdftoppm','-v'],'poppler-version');report['poppler_version']=(out/'poppler-version.stderr').read_text()
 for stage in ['first','second','final']:run(['pdflatex','-interaction=nonstopmode','-halt-on-error','phi_lemma.tex'],'latex-'+stage)
 report['pdfinfo']=run(['pdfinfo','phi_lemma.pdf'],'pdfinfo')
 run(['pdftotext','-layout','phi_lemma.pdf','phi_lemma.txt'],'text')
 joined=' '.join((out/'phi_lemma.txt').read_text().split())
 for expected in ['absolute convergence','Model assessments and review context','Ponnusamy','Reproducibility and computational scope','No numerical cancellation rate','not new run results']:
  if expected not in joined:raise RuntimeError('Missing current content '+expected)
 log=(out/'phi_lemma.log').read_text(errors='replace');warnings=[x for x in log.splitlines() if any(s in x for s in ['Overfull','Undefined','undefined references','LaTeX Warning'])];report['layout_warnings']=warnings
 run(['pdftoppm','-r','110','-png','phi_lemma.pdf','page'],'render')
 from PIL import Image,ImageDraw
 pages=sorted(out.glob('page-*.png'))
 if not pages:raise RuntimeError('No exact PDF pages')
 for block,offset in enumerate(range(0,len(pages),6),1):
  sheet=Image.new('RGB',(840,1740),'#dddddd')
  for i,page in enumerate(pages[offset:offset+6]):
   with Image.open(page) as im:
    im=im.convert('RGB');im.thumbnail((400,540));sheet.paste(im,((i%2)*420+(420-im.width)//2,(i//2)*580+10))
   ImageDraw.Draw(sheet).text(((i%2)*420+10,(i//2)*580+558),page.name,fill='black')
  sheet.save(out/('contact-'+str(block).zfill(2)+'.jpg'),quality=90)
 pdf=out/'phi_lemma.pdf';report.update(status='RENDERED_PENDING_VISUAL_REVIEW',pages=len(pages),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pdf_bytes=pdf.stat().st_size)
 if warnings:raise RuntimeError('Final layout warnings preserved')
except Exception:
 report['status']='FAILED_PRESERVED';(out/'failure.txt').write_text(traceback.format_exc())
finally:
 report.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,child_maxrss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
 (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
 manifest=[{'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(out.iterdir()) if p.is_file()]
 (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 zpath=Path('/content/tep207D-review.zip')
 with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(out.iterdir()):
   if p.is_file():z.write(p,p.name)
 print(json.dumps(report));print('ZIP_SHA256='+hashlib.sha256(zpath.read_bytes()).hexdigest())
 if report['status']=='FAILED_PRESERVED':sys.exit(1)
