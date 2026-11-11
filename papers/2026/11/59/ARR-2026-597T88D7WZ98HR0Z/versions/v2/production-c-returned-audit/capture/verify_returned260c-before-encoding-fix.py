import json,hashlib,re,shutil
from pathlib import Path
A=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-260'); O=A/'production-c/attempt-c'; R=Path(r'C:\Trabajo\the-eriksson-programme\perron-spec-210-20261108\_tmp\returned260c')
z=O/'tep260-build-c-results.zip'
if hashlib.sha256(z.read_bytes()).hexdigest()!='6bfa6a96638612868b07bb42ad1c9d77232d2cc67506bdc03456df920b314a7b':raise RuntimeError('Archive hash mismatch')
m=json.loads((R/'evidence/manifest.json').read_bytes());count=0
for x in m:
    f=R/x['path']; b=f.read_bytes()
    if not f.resolve().is_relative_to(R.resolve()) or len(b)!=x['bytes'] or hashlib.sha256(b).hexdigest()!=x['sha256']:raise RuntimeError('Returned member differs: '+x['path'])
    count+=1
r=json.loads((R/'evidence/report.json').read_bytes())
if r['source']!='fb3ba8d2c0ae52d4a2e909b0fb2df02b2f953bc4' or r['tex_raw_sha256']!='9c24b70685a5a7ae9301555170fa84acafd9f17524734775b1e9bca7cce822d9':raise RuntimeError('Source mismatch')
if r['status']!='TWO_FRESH_MATCHING_PDFS_RENDERED_PENDING_ALL_PAGE_VISUAL_AND_FIRST_EXACT_PDF_ASSESSMENT':raise RuntimeError('Inner execution did not succeed')
if len(r['builds'])!=2 or len({x['pdf_sha256'] for x in r['builds']})!=1 or len({x['pdf_bytes'] for x in r['builds']})!=1:raise RuntimeError('Clone mismatch')
if r['pages']!=14 or any(x['input_files_verified']!=201 or x['overfull_lines'] for x in r['builds']):raise RuntimeError('Actual C input/page/overflow evidence differs')
pdf=R/'evidence/checkerboard_observations260.pdf';raw=pdf.read_bytes();digest=hashlib.sha256(raw).hexdigest()
if len(raw)!=397040 or digest!='f9d3a44e4811a28ec11af3577a4218dad1cb2b3bc0482e2528f5ff80ffdc3892':raise RuntimeError('Exact PDF differs')
for c in r['commands']:
    sentinel=(R/'evidence'/(c['name']+'.exit')).read_bytes()
    if re.fullmatch(rb'-?[0-9]+\n',sentinel) is None or int(sentinel)!=c['actual_exit'] or int(sentinel)!=0 or c['timed_out']:raise RuntimeError('Command failed: '+c['name'])
if not all(x['removed'] for x in r['cleanup']):raise RuntimeError('Clone cleanup debt')
for mode in ['allocation','execution','download','release','backend-readback']:
    if (O/(mode+'.exit')).read_bytes()!=b'0\n':raise RuntimeError('Outer command failed: '+mode)
if 'No active sessions found on server.' not in (O/'backend-readback.log').read_text():raise RuntimeError('Backend inactivity not observed')
text=(R/'evidence/checkerboard_observations260.txt').read_text()
for token in ['36n','A separate counterexample for nonwrapping chart cells','Model assessments and review context']:
    if token not in ' '.join(text.split()):raise RuntimeError('Final extraction missing required new content')
shutil.copytree(R,O/'returned')
result={'status':'TWO_MATCHING_FINAL_C_PDFS_AND_ACTUAL_LIFECYCLE_VERIFIED_ALL14PAGES_VISUALLY_ACCEPTED_PENDING_FIRST_EXACT_PDF_ASSESSMENT','source':r['source'],'PDF_sha256_raw':digest,'PDF_bytes':len(raw),'pages':14,'returned_raw_members_verified':count,'inner_commands_verified':len(r['commands']),'actual_outer_exits':[0,0,0,0,0],'both_disposable_clones_removed':True,'own_backend_inactive':True,'actual_billed_units':None,'individual_full_pages_visually_inspected':list(range(1,15)),'visual_observations':'All14 actual110dpi pagePNGs individually read. No clipping/overlap/black boxes/illegible equations; margins/footer/numbering intact. Former wave/hash overflow absent; complete four-entry bibliography now together on page14 with provenance continuation, no orphan single reference. New chart construction/count/threshold legible on pages11-12.','overfull_log_lines':[],'residual_copyediting':'Minor compressed source-reference wording and261C remains a nonblocking typographic residual disclosed by source auditor; no mathematical/layout acceptance beyond stated checks','numerical_assessment_performed':False,'grade':None,'runtime_open_requested':(O/'runtime-open-requested.txt').read_text().strip(),'runtime_release_finished':(O/'runtime-release-finished.txt').read_text().strip()}
(O/'parent-return-validation260C.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
shutil.copyfile(__file__,A/Path(__file__).name)
print(json.dumps(result))
