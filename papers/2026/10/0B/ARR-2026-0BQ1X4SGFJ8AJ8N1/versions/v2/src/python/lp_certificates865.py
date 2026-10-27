from pathlib import Path
from itertools import product
import json,hashlib
from datetime import datetime,timezone
M=[[1,2,3],[0,1,1]];lower=[0,0,0];upper=[4,4,4]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
# c=M^T lambda+mu-nu, mu,nu>=0 certifies min c*x >= lambda*b+mu*l-nu*u.
patterns=[(0,'min',[1,-3],[0,1,0],2),(0,'max',[-1,2],[0,0,1],0),(1,'min',[0,0],[0,1,0],2),(1,'max',[0,-1],[0,0,1],0),(2,'min',[0,0],[0,0,1],0),(2,'max',[0,-1],[0,1,0],2)]
certificates=[];extrema={};counts={}
for label,b in [('minus',[6,2]),('center',[7,2]),('plus',[8,2])]:
 a=b[0]-2*b[1];points=[x for x in product(range(5),repeat=3) if [dot(row,x) for row in M]==b]
 assert len(points)==3;counts[label]=len(points);minimum=[];maximum=[]
 for i,direction,lam,mu,t in patterns:
  c=[int(j==i)*(1 if direction=='min' else -1) for j in range(3)];nu=[0,0,0];x=[a-t,2-t,t]
  assert [dot(row,x) for row in M]==b and all(l<=z<=u for l,z,u in zip(lower,x,upper))
  assert all(v>=0 for v in mu+nu)
  assert c==[sum(M[k][j]*lam[k] for k in range(2))+mu[j]-nu[j] for j in range(3)]
  bound=dot(lam,b)+dot(mu,lower)-dot(nu,upper);assert dot(c,x)==bound
  optimum=bound if direction=='min' else -bound
  assert optimum==(min if direction=='min' else max)(point[i] for point in points)
  certificates.append({'fiber':label,'rhs':b,'coordinate':i,'direction':direction,'minimization_cost':c,'row_multiplier':lam,'lower_multiplier':mu,'upper_multiplier':nu,'primal_point':x,'certified_min_cost':bound,'coordinate_optimum':optimum})
 extrema[label]={'minimum':[min(x[i] for x in points) for i in range(3)],'maximum':[max(x[i] for x in points) for i in range(3)]}
h=[x-y for x,y in zip(extrema['plus']['minimum'],extrema['center']['minimum'])]
assert h==[1,0,0] and [dot(row,h) for row in M]==[1,0]
assert extrema['plus']['maximum']==[x+y for x,y in zip(extrema['center']['maximum'],h)]
assert extrema['minus']['minimum']==[x-y for x,y in zip(extrema['center']['minimum'],h)]
assert extrema['minus']['maximum']==[x-y for x,y in zip(extrema['center']['maximum'],h)]
assert len(certificates)==18
result={'utc':datetime.now(timezone.utc).isoformat(),'scope':'Post-review optional author supplement addressing review861 R4. Not part of the evaluated PDF or original861 review; no new model score or Tardos implementation.','M':M,'box_lower':lower,'box_upper':upper,'certificate_identity':'c=M^T lambda+mu-nu; mu,nu>=0; lower bound lambda*b+mu*l-nu*u; feasible primal attaining it proves optimality','certificates':certificates,'all18_primal_dual_equalities_verified':True,'coordinate_extrema':extrema,'lattice_counts':counts,'translation_h':h,'equality_test':'passed','arithmetic':'exact Python integers; enumeration only cross-checks this small example','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=Path(__file__).parent/'LP-CERTIFICATES865.json';out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'certificates':18,'primal_dual_equalities':'passed','translation_h':h,'lattice_counts':counts,'no_regrade':True}))
