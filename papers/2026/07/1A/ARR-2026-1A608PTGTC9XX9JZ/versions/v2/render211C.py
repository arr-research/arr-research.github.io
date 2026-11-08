import json,hashlib
SOURCE='6dff378ea8c6f74eab50564375a828ba96a618e5'
INPUTS={'perron_gap.tex': {'path': 'papers/perron-gap/revision211/perron_gap.tex', 'sha256': '091779820a74b9cfcaec2789e54cfcac690352185633f6375543c0f95e40f801'}, 'SOURCE-AUDIT210.json': {'path': 'papers/perron-gap/revision210/SOURCE-AUDIT210.json', 'sha256': 'a9181154ae9a3d7f0ec66160af2ccf187c7e8dc03bd35cf2f7c939f9b48c10bc'}, 'FINITE-DIAGNOSTICS210.json': {'path': 'papers/perron-gap/revision210/FINITE-DIAGNOSTICS210.json', 'sha256': '275739fadd01f853edc54dc568ad23174932293a020cc79621b2f3687010bd88'}, 'HISTORICAL-SIGNATURES210.txt': {'path': 'papers/perron-gap/revision210/HISTORICAL-SIGNATURES210.txt', 'sha256': 'eeef66ae68f780dffa04759d68bc25852b067a1f2a04bd3c2a0c65760234d1d6'}}
import os,sys,time,traceback,subprocess,resource,zipfile,urllib.request
from datetime import datetime,timezone
from pathlib import Path
if not Path('/content').is_dir():raise RuntimeError('Own Colab Linux required')
out=Path('/content/tep211C');out.mkdir(exist_ok=False);os.chdir(out)
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
 for stage in ['first','second','final']:run(['pdflatex','-interaction=nonstopmode','-halt-on-error','perron_gap.tex'],'latex-'+stage)
 report['pdfinfo']=run(['pdfinfo','perron_gap.pdf'],'pdfinfo')
 run(['pdftotext','-layout','perron_gap.pdf','perron_gap.txt'],'text')
 joined=' '.join((out/'perron_gap.txt').read_text().split())
 for expected in ['Model assessments and review context','Walsh','0.908247','LDL','Any numerical assessment']:
  if expected not in joined:raise RuntimeError('Missing current content '+expected)
 log=(out/'perron_gap.log').read_text(errors='replace');warnings=[x for x in log.splitlines() if any(s in x for s in ['Overfull','Undefined','undefined references','LaTeX Warning'])];report['layout_warnings']=warnings
 run(['pdftoppm','-r','110','-png','perron_gap.pdf','page'],'render')
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
 pdf=out/'perron_gap.pdf';report.update(status='RENDERED_PENDING_VISUAL_REVIEW',pages=len(pages),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pdf_bytes=pdf.stat().st_size)
 if warnings:raise RuntimeError('Final layout warnings preserved')
except Exception:
 report['status']='FAILED_PRESERVED';(out/'failure.txt').write_text(traceback.format_exc())
finally:
 report.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,child_maxrss_kib=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
 (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
 manifest=[{'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(out.iterdir()) if p.is_file()]
 (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 zpath=Path('/content/tep211C-review.zip')
 with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(out.iterdir()):
   if p.is_file():z.write(p,p.name)
 print(json.dumps(report));print('ZIP_SHA256='+hashlib.sha256(zpath.read_bytes()).hexdigest())
 if report['status']=='FAILED_PRESERVED':sys.exit(1)
