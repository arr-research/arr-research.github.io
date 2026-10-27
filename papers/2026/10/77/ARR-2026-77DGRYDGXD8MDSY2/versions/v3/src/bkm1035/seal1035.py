from pathlib import Path
import json,datetime,hashlib,urllib.request,concurrent.futures,shutil
P=Path(__file__).parent;D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_bkm1035');assert not D.exists();H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
spec=[('https://arxiv.org/html/1508.03551v1','Example1 andSection7.1/Theorem7.1 proof reread; distinguish2015open remark from later resolved general reduction'),('https://arxiv.org/html/2610.29373v1','SelectedSection2.2 Lemma1/Eqs18-32 and abstract reread; already inventoried/read in917, not a newly discovered reference; whole AD/convergence proofs not audited'),('https://api.github.com/repos/openai/math/commits?per_page=1','latest commit metadata only'),('https://api.github.com/repos/google-deepmind/formal-conjectures/commits?per_page=1','latest commit metadata only'),('https://www.anthropic.com/research','index only'),('https://airr.science/','catalogue index only'),('https://www.ai.vixra.org/author/lluis_eriksson','author index only'),('https://api.github.com/users/lluiseriksson/repos?type=owner&sort=updated&per_page=100','first100 public repository metadata only')]
def one(item):
 url,depth=item;out=dict(url=url,read_depth=depth,retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AIRR-directed-primary-research/1.0'}),timeout=40) as r:b=r.read();out.update(status=r.status,etag=r.headers.get('ETag'),last_modified=r.headers.get('Last-Modified'))
  out.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),foreign_body_saved=False)
  if '/commits?' in url:out['commit']=json.loads(b)[0]['sha']
 except Exception as ex:out['error']=str(ex)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(one,spec))
readings=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Directed primary sweep and targeted rereading, not exhaustive. Inventoried/abstract/statement/proof scopes are not conflated.',sources=rows,deduplication='HanLi2610.29373v1 and BKM/RE equivalence already recorded in research-radar/evidence/2026-10-27-complete914/READINGS917.json and complete-noise-and-kernel note. Current reading adds selected BKM comparison scope, not a new source or new general Bregman theorem.',not_relied_on='Search results from secondary aggregators used only as leads; technical attribution relies on primary arXiv passages.',new_manuscript_grade=None)
(P/'READINGS1035.json').write_text(json.dumps(readings,indent=2)+'\n',newline='\n')
prov=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='exploratory post-start1030/1031 material, not technically audited, no manuscript score',input1033_manifest_sha256=H(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1033\MANIFEST1033.json')),input1033_proof_sha256=H(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1033\PROOF1033.txt')),confidence='speculative analytic lower; bounded interval comparisons are computational evidence, not universal or formal proof',reuse='Parent1033 coordinates and1025BKM asymptotic diagnostic adapted; not independent checking',not_established=['exact BKM or Umegaki optimum','all-Petz transfer','actualMI','worldwide novelty','unitary protocol','practical robustness'],incidents=['Attempt to read a guessed D complete914 path failed; actual repository evidence READINGS917.json located and read. Source deduplicated against existing registry; no new-source claim.'],math_runs='Both bounded programs passed on first mathematical invocation; no optimization or restart for grade',frozen1030_unchanged=True)
(P/'PROVENANCE1035.json').write_text(json.dumps(prov,indent=2)+'\n',newline='\n')
files=[dict(path=p.relative_to(P).as_posix(),bytes=p.stat().st_size,sha256=H(p)) for p in sorted(P.rglob('*')) if p.is_file()]
(P/'MANIFEST1035.json').write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Own exploratory packet, self hash excluded',files=files),indent=2)+'\n',newline='\n')
shutil.copytree(P,D)
for p in P.rglob('*'):
 if p.is_file():assert H(p)==H(D/p.relative_to(P))
print(json.dumps(dict(files=len(files)+1,manifest_sha256=H(P/'MANIFEST1035.json'),proof_sha256=H(P/'PROOF1035.txt'),interval_sha256=H(P/'INTERVAL1035.json'),sweep_errors=[r['url'] for r in rows if 'error' in r],C_D_identical=True)))
