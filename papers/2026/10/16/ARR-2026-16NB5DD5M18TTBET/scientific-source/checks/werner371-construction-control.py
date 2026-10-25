from pathlib import Path
import runpy,itertools,json,hashlib,time
import sympy as s
root=Path(__file__).resolve().parent;started=time.time()
e=runpy.run_path(str(root/'werner370-brauer.py'))
source=Path(__file__).resolve().parent/'prior337-bell4-construction.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='cf967c095027ec9bc050072b247673dc85ee68174c2267d8226a4e4c658bdf21'
head=source.read_text().split('roots=[',1)[0]
def evaluate(diagrams,n,m,d):
 entries={}
 def flat(xs):
  value=0
  for x in xs:value=d*value+x
  return value
 for p,coefficient in diagrams.items():
  coefficient=coefficient.subs(e['z'],d)
  for labels in itertools.product(range(d),repeat=len(p)):
   indices=[None]*(n+m)
   for (a,b),label in zip(p,labels):indices[a]=indices[b]=label
   key=(flat(indices[:n]),flat(indices[n:]))
   entries[key]=entries.get(key,0)+coefficient
 return s.SparseMatrix(d**n,d**m,{k:v for k,v in entries.items() if v})
checks=[]
for d in [2,3,4,5]:
 env={'__file__':str(source)}
 exec(compile(head.replace('d=4;D=d*d;N=D*D',f'd={d};D=d*d;N=D*D'),'earlier-contraction-construction','exec'),env)
 assert evaluate(e['M'],4,2,d)==env['M']
 assert evaluate(e['Bnum'],4,4,d)==(d-1)*(5*d-4)*env['B']
 assert evaluate(e['T'],4,4,d)==9*(d-1)*(5*d-4)*env['R']
 checks.append({'dimension':d,'M_exact_match':True,'B_numerator_exact_match':True,'scaled_R_exact_match':True})
out={'status':'AUTHOR_EXACT_CONSTRUCTION_CONTROLS_PASS','checks':checks,'diagram_identity_and_projector_trace_pass':True,'source_construction_reused':True,'independent_audit':False,'seconds':time.time()-started}
(root/'werner371-construction-control.json').write_bytes((json.dumps(out,indent=2)+'\n').encode());print(json.dumps(out))
