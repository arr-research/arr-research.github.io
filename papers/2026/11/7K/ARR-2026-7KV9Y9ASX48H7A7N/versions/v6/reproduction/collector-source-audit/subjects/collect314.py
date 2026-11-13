from pathlib import Path
import json,hashlib,zipfile,shutil
E=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-314')
A=E/'production-a/attempt-a';Z=A/'tep314-build-a-results.zip';R=A/'returned'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,msg):
 if not ok:raise ValueError(msg)
outer=json.loads((A/'outer-report.json').read_bytes())
require(outer['failure'] is None and len(outer['actual_cli_exits'])==4 and all(v==0 for v in outer['actual_cli_exits'].values()),'Actual lifecycle incomplete')
require(not R.exists(),'Preserve earlier extraction')
with zipfile.ZipFile(Z) as z:
 for f in z.infolist():
  target=(R/f.filename).resolve()
  require(target.is_relative_to(R.resolve()) and not f.filename.startswith('/'),'Unsafe zip member')
 z.extractall(R)
B=R/'evidence';rows=json.loads((B/'manifest.json').read_bytes())
for r in rows:
 p=R/r['path'];require(p.resolve().is_relative_to(R.resolve()),'Unsafe manifest member')
 require(p.stat().st_size==r['bytes'] and h(p)==r['sha256'],'Raw member differs '+r['path'])
report=json.loads((B/'report.json').read_bytes())
require(report['source']=='b72cfbcb74275ff7f80b6c262cb003c5cc6ea8eb','Source differs')
require(report['status']=='TWO_FRESH_MATCHING_PDFS_RENDERED_PENDING_ALL_PAGE_VISUAL_AND_FIRST_EXACT_PDF_ASSESSMENT','Inner production failed')
require(len(report['commands'])==27 and all(c['actual_exit']==0 and not c['timed_out'] for c in report['commands']),'Native children incomplete')
require(len(report['cleanup'])==2 and all(c['removed'] for c in report['cleanup']),'Disposable clone cleanup incomplete')
pdf=B/'manuscript314A.pdf'
require(h(pdf)==h(B/'clone-a.pdf')==h(B/'clone-b.pdf'),'Actual PDFs differ')
require(all(x['input_files_verified']==940 and x['pdf_sha256']==h(pdf) for x in report['builds']),'Input/build binding differs')
delivery=Path(r'D:\Entregas\the-eriksson-programme\2026-11-13_attained-cutoff314')
captures=Path(r'D:\Capturas\the-eriksson-programme\2026-11-13_attained-cutoff314')
delivery.mkdir(exist_ok=False);captures.mkdir(exist_ok=False)
for f in [pdf,B/'source-capture/manuscript314A.tex',B/'manuscript314A.txt',Z]:shutil.copy2(f,delivery/f.name)
for f in list(B.glob('page-*.png'))+list(B.glob('contact-*.jpg')):shutil.copy2(f,captures/f.name)
v={'source':report['source'],'PDF_sha256':h(pdf),'PDF_bytes':pdf.stat().st_size,'pages':report['pages'],'archive_sha256':h(Z),'raw_members_verified':len(rows),'actual_native_commands':27,'all_native_exit_zero':True,'two_matching_fresh_clones':True,'clones_removed':True,'visual_review_complete':False,'exact_PDF_assessment':None,'backend_inactivity_readback':'pending separate query','billing_units':None}
(A/'parent-return-validation314.json').write_bytes((json.dumps(v,indent=2)+'\n').encode())
print(json.dumps(v))
