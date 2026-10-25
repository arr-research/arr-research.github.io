"""Exact finite-block candidate certificate, not yet externally audited.
The motivating numerical spectra are not used as evidence after this check.
"""
from pathlib import Path
import json,hashlib,time
import sympy as s
ROOT=Path(__file__).resolve().parent
started=time.time();d=4;D=d*d;N=D*D
I=s.SparseMatrix(s.eye(N))
def split(k):return (k//(d**3),(k//d**2)%d,(k//d)%d,k%d)
def flat(t):
 r=0
 for x in t:r=d*r+x
 return r
flips=[]
for slot in [0,1]:
 entries={}
 for k in range(N):
  z=list(split(k));z[slot],z[slot+2]=z[slot+2],z[slot];entries[flat(z),k]=1
 flips.append(s.SparseMatrix(N,N,entries))
A=(I-flips[0]/2)*(I-flips[1]/2)
Ainv=(4*I/3+2*flips[0]/3)*(4*I/3+2*flips[1]/3)
assert Ainv*A==I
a=s.SparseMatrix(D,1,{(i*d+i,0):1 for i in range(d)})
# Unnormalized Bell anchor; the map Psi is invariant under scaling of a.
H=(d-1)*s.eye(D)+a*a.T/4
Hinv=s.eye(D)/(d-1)-a*a.T/((d-1)*(5*d-4))
assert H*Hinv==s.eye(D)
md={}
for (rr,cc),v in A.todok().items():
 r,t=divmod(rr,D);source,j=divmod(cc,D)
 if a[source]:md[j*D+r,t]=md.get((j*D+r,t),0)+v
M=s.SparseMatrix(N,D,md)
CP=M*s.SparseMatrix(Hinv)*M.T
bd={}
for (rr,cc),v in CP.todok().items():
 j,r=divmod(rr,D);k,t=divmod(cc,D);bd[k*D+r,j*D+t]=v
B=s.SparseMatrix(N,N,bd)
assert B==B.T
R=Ainv*B
adj=[set() for _ in range(N)]
for (i,j),v in R.todok().items():
 if i!=j and v:adj[i].add(j);adj[j].add(i)
remaining=set(range(N));components=[]
while remaining:
 todo=[min(remaining)];seen=set(todo)
 while todo:
  u=todo.pop()
  for v in adj[u]-seen:seen.add(v);todo.append(v)
 remaining-=seen;components.append(sorted(seen))
roots=[-21,-9,-3,3,9,11,27]
checks=[]
for indices in components:
 r=R.extract(indices,indices);ident=s.eye(len(indices));p=ident
 for root in roots:p=p*(27*r-root*ident)
 assert p==s.zeros(len(indices)),('annihilator failed',indices)
 checks.append({'dimension':len(indices),'minimum_index':min(indices),'polynomial_zero_exact':True})
out={'status':'PASS','block_local_dimension':d,'two_slot_dimension':D,'Choi_dimension':N,'anchor':'unnormalized Omega4 on two slots','normalization_invariant_map':True,'R_equals_A_inverse_B':True,'A_positive_analytic_reason':'A=(I-F1/2)(I-F2/2); commuting Hermitian swaps','B_symmetric_exact':True,'annihilator_scaled_roots':roots,'eigenvalues_contained_in':[[r,27] for r in roots],'A_plus_B_and_A_minus_B_PSD_consequence':'Conditional on the stated Choi construction, exact annihilator plus A-self-adjointness gives signed order -A<=B<=A. Construction and downstream sector still require audit.','components':checks,'R_nonzero_entries':len(R.todok()),'seconds':time.time()-started,'scope':'Exact finite block certificate only; not proof of full Werner positivity or novelty','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'werner337-bell4-exact-certificate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
(ROOT/'werner337-bell4-R-triplets.json').write_text(json.dumps({'shape':[N,N],'entries':[[int(i),int(j),str(v)] for (i,j),v in sorted(R.todok().items())]},separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='components'},indent=2));print('component sizes:',[x['dimension'] for x in checks])
