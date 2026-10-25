from pathlib import Path
import hashlib,json,time
import sympy as s
base=Path(__file__).resolve().parent
source=Path(__file__).resolve().parent/'prior337-bell4-construction.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='cf967c095027ec9bc050072b247673dc85ee68174c2267d8226a4e4c658bdf21'
head=source.read_text(encoding='utf-8').split('roots=[',1)[0]
results=[]
for d in [3,5]:
 started=time.time()
 env={'__file__':str(source)}
 exec(compile(head.replace('d=4;D=d*d;N=D*D',f'd={d};D=d*d;N=D*D'),'reused-Bell-construction','exec'),env)
 R=env['R'];spectra={};checks=[]
 for indices in env['components']:
  block=R.extract(indices,indices)
  poly=block.charpoly();factor=s.factor_list(poly.as_expr())[1]
  roots=s.roots(poly.as_expr())
  assert sum(roots.values())==len(indices)
  for v,m in roots.items():spectra[str(v)]=spectra.get(str(v),0)+int(m)
  checks.append({'size':len(indices),'minimum_index':min(indices),'factorization':str(s.factor(poly.as_expr()))})
 out={'dimension':d,'construction_reused_not_independent':True,'matrix_dimension':d**4,'spectrum':spectra,'signed_gate_pass':all(bool(-1<=s.sympify(v)) and bool(s.sympify(v)<=1) for v in spectra),'components':checks,'seconds':time.time()-started}
 results.append(out)
 print(json.dumps({k:v for k,v in out.items() if k!='components'}),flush=True)
 (base/'werner369-bell-dimensions.json').write_bytes((json.dumps(results,indent=2)+'\n').encode())
