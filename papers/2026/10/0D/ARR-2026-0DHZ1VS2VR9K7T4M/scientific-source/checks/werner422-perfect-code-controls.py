from pathlib import Path
from itertools import product,combinations
import json,time
import sympy as s
r=Path(__file__).resolve().parent;start=time.time();records=[]
for d in [3,5]:
 words=list(product(range(d),repeat=3));flat={w:i for i,w in enumerate(words)};N=d**4
 code=[[(t,(t+j)%d,(t+2*j)%d) for t in range(d)] for j in range(d)]
 coeff=[]
 for k in range(4):
  G=s.SparseMatrix(N,N,{})
  for sub in combinations(range(3),k):
   keep=[j for j in range(3) if j not in sub];n=d**len(keep);entries={}
   for i,t in product(range(d),range(d**3)):
    for u in code[i]:
     if any(u[j]!=words[t][j] for j in sub):continue
     a=sum(u[j]*d**(len(keep)-1-l) for l,j in enumerate(keep));b=sum(words[t][j]*d**(len(keep)-1-l) for l,j in enumerate(keep))
     key=(a*n+b,i*d**3+t);entries[key]=entries.get(key,0)+1
   D=s.SparseMatrix(n*n,N,entries);G+=(D.T*D)/d
  coeff.append(G)
 I=s.eye(N);P=coeff[3]/d;E=coeff[2]-3*P;Z=I-E-P
 assert coeff[0]==I and coeff[1]==s.Rational(3,d)*I
 for Q in [P,E,Z]:assert Q*Q==Q and Q==Q.T
 assert P*E==s.zeros(N) and P*Z==s.zeros(N) and E*Z==s.zeros(N)
 assert [s.trace(Q) for Q in [Z,E,P]]==[d**4-3*d*d+2,3*(d*d-1),1]
 for t in [s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(1)]:
  alpha=1-3*t/d;eta=alpha+3*t*t-d*t**3
  G=sum(((-t)**k*coeff[k] for k in range(4)),s.zeros(N))
  assert G==alpha*Z+(alpha+t*t)*E+eta*P
 records.append({'d':d,'full_complex_Gram_dimension':N,'coefficient_identity_all_t':True,'orthogonal_projection_ranks':[int(s.trace(Q)) for Q in [Z,E,P]],'four_exact_parameter_controls':True})
 print('matrix',d,'PASS',flush=True)
# Independent sparse projector controls in larger odd dimensions.
large=[]
for d in [3,5,7,11,13,15,17]:
 entries={}
 for j,t,u in product(range(d),repeat=3):entries[((t,(t+j)%d,(t+2*j)%d),(u,(u+j)%d,(u+2*j)%d))]=s.Rational(1,d)
 norms=[]
 for k in range(4):
  values=[]
  for sub in combinations(range(3),k):
   keep=[j for j in range(3) if j not in sub];out={}
   for (a,b),v in entries.items():
    if any(a[j]!=b[j] for j in sub):continue
    key=(tuple(a[j] for j in keep),tuple(b[j] for j in keep));out[key]=out.get(key,0)+v
   values.append(sum(v*v for v in out.values()))
  assert values==[[d],[1,1,1],[d,d,d],[d*d]][k]
  norms.append(values)
 value=sum((-s.Rational(1,2))**k*sum(v) for k,v in enumerate(norms));eta=s.Rational(7,4)-s.Rational(3,2*d)-s.Rational(d,8)
 assert value==d*eta
 large.append({'d':d,'partial_trace_norms':[[str(x) for x in v] for v in norms],'q_projector':str(value),'eta_half':str(eta)})
out={'status':'PASS_EXACT_PERFECT_CODE_GRAM_AND_PROJECTOR_CONTROLS','full_Gram_checks':records,'large_sparse_controls':large,'scope':'Producer checks of proposed universal AME4 spectral theorem. General proof relies on two-body uniformity, not interpolation in d; code construction is prior.','seconds':time.time()-start}
(r/'werner422-perfect-code-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
