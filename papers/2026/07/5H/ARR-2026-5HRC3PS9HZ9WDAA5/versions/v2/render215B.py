import json,hashlib
SOURCE='5bbfae4429123ebb876a979b31a124acdf73b25f'
INPUTS={'parity_positive.tex': {'path': 'papers/parity-barriers/revision215/parity_positive.tex', 'sha256': '2447304d7e46f5183bc4ab7f212769e2a1538692314644a703a6153169790518'}, 'STRICT-POSITIVE-SPECTRUM214.md': {'path': 'papers/parity-barriers/revision214/STRICT-POSITIVE-SPECTRUM214.md', 'sha256': '1a748cb849ce2796baf986f673e982325999c54616fece9caf0fc3453619e415'}, 'verified-diagnostic214.json': {'path': 'papers/parity-barriers/revision214/verified-diagnostic214.json', 'sha256': 'fa7b7fb87e1446b0862527392f7daf85c18fb51b52d8582820b4a70b910647c8'}, 'source-binding214.json': {'path': 'papers/parity-barriers/revision214/source-binding214.json', 'sha256': '751b1e571bd598f197577b24a6cd1c1fb1b3e4e0f7d44a45be6e8f1272dc1364'}}
import os,sys,time,traceback,subprocess,resource,zipfile,urllib.request
from datetime import datetime,timezone
from pathlib import Path
if not Path('/content').is_dir():raise RuntimeError('Own Colab Linux required')
out=Path('/content/tep215B');out.mkdir(exist_ok=False);os.chdir(out)
start=time.monotonic();report={'source_sha':SOURCE,'source_inputs':INPUTS,'started_utc':datetime.now(timezone.utc).isoformat(),'tool_exits':{},'compute_units_billed':None,'formal_or_scientific_replay':False}
def run(args,name,timeout=240):
 p=subprocess.run(args,capture_output=True,timeout=timeout)
 (out/(name+'.stdout')).write_bytes(p.stdout);(out/(name+'.stderr')).write_bytes(p.stderr)
 tmp=out/(name+'.exit.tmp');tmp.write_text(str(p.returncode)+'\n');code=int(tmp.read_text().strip());os.replace(tmp,out/(name+'.exit'));report['tool_exits'][name]=code
 if code:raise RuntimeError(name+' exited '+str(code))
 return p.stdout.decode(errors='replace')
try:
 for name,spec in INPUTS.items():
  raw=urllib.request.urlopen('https://raw.githubusercontent.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/'+SOURCE+'/'+spec['path'],timeout=45).read()
  if hashlib.sha256(raw).hexdigest()!=spec['sha256']:raise RuntimeError('Input hash mismatch '+name)
  (out/name).write_bytes(raw)
 run(['apt-get','-qq','update'],'apt-update',600)
 run(['apt-get','install','-y','-qq','texlive-latex-base','texlive-latex-recommended','texlive-fonts-recommended','lmodern','poppler-utils'],'apt-install',900)
 os.environ['SOURCE_DATE_EPOCH']='1794096000';os.environ['FORCE_SOURCE_DATE']='1'
 report['tex_version']=run(['pdflatex','--version'],'tex-version')
 run(['pdftoppm','-v'],'poppler-version');report['poppler_version']=(out/'poppler-version.stderr').read_text()
 for stage in ['first','second','final']:run(['pdflatex','-interaction=nonstopmode','-halt-on-error','parity_positive.tex'],'latex-'+stage)
 report['pdfinfo']=run(['pdfinfo','parity_positive.pdf'],'pdfinfo')
 run(['pdftotext','-layout','parity_positive.pdf','parity_positive.txt'],'text')
 joined=' '.join((out/'parity_positive.txt').read_text().split())
 for expected in ['Model assessments and review context','32736','Theorem']:
  if expected not in joined:raise RuntimeError('Missing current content '+expected)
 log=(out/'parity_positive.log').read_text(errors='replace');warnings=[x for x in log.splitlines() if any(s in x for s in ['Overfull','Undefined','undefined references','LaTeX Warning'])];report['layout_warnings']=warnings
 run(['pdftoppm','-r','110','-png','parity_positive.pdf','page'],'render')
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
 pdf=out/'parity_positive.pdf';report.update(status='RENDERED_PENDING_VISUAL_REVIEW',pages=len(pages),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pdf_bytes=pdf.stat().st_size)
 if warnings:raise RuntimeError('Final layout warnings preserved')
except Exception:
 report['status']='FAILED_PRESERVED';(out/'failure.txt').write_text(traceback.format_exc())
finally:
 report.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,child_maxrss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
 (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
 manifest=[{'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(out.iterdir()) if p.is_file()]
 (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 zpath=Path('/content/tep215B-review.zip')
 with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(out.iterdir()):
   if p.is_file():z.write(p,p.name)
 print(json.dumps(report));print('ZIP_SHA256='+hashlib.sha256(zpath.read_bytes()).hexdigest())
 if report['status']=='FAILED_PRESERVED':sys.exit(1)
