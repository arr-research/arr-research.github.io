from pathlib import Path
import json,datetime,hashlib,urllib.request,shutil
P=Path(__file__).parent;D=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_principal1033');assert not D.exists()
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
readings=[]
for id_,title,scope in [('1008.1557v1','Probing the qudit depolarizing channel','Abstract read: channel identification/noise-parameter estimation with unentangled, external-ancilla and entangled-pair schemes. Not a proof audit or a covering-theorem exclusion.'),('2204.09963v1','A Fisher information-based incompatibility criterion for quantum channels','Abstract read: channel incompatibility through Fisher information, Schur/depolarizing tuples and cloning comparisons. Not the same optimization by definition; body not proof-audited.')]:
 url='https://arxiv.org/abs/'+id_
 with urllib.request.urlopen(url,timeout=35) as r:b=r.read();status=r.status
 readings.append(dict(url=url,title=title,version=id_,status=status,retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),depth='abstract and metadata only',scope=scope))
(P/'PRIMARY1033.json').write_text(json.dumps(dict(utc=utc,sources=readings,selection='Additional directed search, not exhaustive; primary bodies not copied'),indent=2)+'\n',newline='\n')
incidents=dict(utc=utc,mathematical_controls='First check1033 run passed all declared controls; no optimization used',incidents=['Initial inline shell command for building the sweep script failed with Python SyntaxError due to quoting; no sweep output produced; replaced with saved script and successful seven-endpoint sweep.','Two speculative v2 HTML URLs returned404; authoritative arXiv metadata then resolved both papers to v1. Only abstracts are recorded as read, no unavailable-body claim.'],new_score=None)
(P/'INCIDENTS1033.json').write_text(json.dumps(incidents,indent=2)+'\n',newline='\n')
prov=dict(utc=utc,status='Own analytical candidate with bounded exact controls, awaiting later technical audit after current1031review ends',dependencies=['1021 ranktwo geometry, modified allocation of principal/common coordinates','1025 invariant-plane/Sylvester/ordered-limit proof method','prior operator-order/resolvent upper and normalized Petz representation'],checker_dependency=dict(path='2026-10-27_ranktwo1021/check1021.py',sha256=H(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_ranktwo1021\check1021.py')),reuse='SymPy full connected-block Sylvester and positive-slack control method reused with new coordinates; not independent verification'),removed_restriction='proposed budget cap from d(d+1)/2 to d(2d-1)/2, at reference cost d+1 to2d-1',no_score=True,not_in1030=True,one_current_review='1031 on exact1030; do not mix post-start1033input',confidence='speculative until technical audit; not formal',falsifiers='partial trace, Gram normalization, missing modes, Sylvester limit, faithful perturbation, covering literature',program_control_scope='2 symbolic general-d identities, full d2/3/4 geometry,4finite exact rational pairs with full ambient residuals and rational LDL positivity',prior_endpoint_comparison='Not an upper on every earlier-family finite state; comparison only to its certified limiting endpoint formula')
(P/'PROVENANCE1033.json').write_text(json.dumps(prov,indent=2)+'\n',newline='\n')
files=[dict(path=p.relative_to(P).as_posix(),sha256=H(p),bytes=p.stat().st_size) for p in sorted(P.rglob('*')) if p.is_file()]
(P/'MANIFEST1033.json').write_text(json.dumps(dict(utc=utc,scope='Own frozen exploratory payload; self hash excluded',files=files),indent=2)+'\n',newline='\n')
shutil.copytree(P,D)
for p in P.rglob('*'):
 if p.is_file():assert H(p)==H(D/p.relative_to(P))
print(json.dumps(dict(files=len(files)+1,manifest_sha256=H(P/'MANIFEST1033.json'),proof_sha256=H(P/'PROOF1033.txt'),check_sha256=H(P/'CHECK1033.json'),C_D_identical=True)))
