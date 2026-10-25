from pathlib import Path
from functools import lru_cache
import sympy as s,json,time
from sympy.polys.matrices import DomainMatrix
root=Path(__file__).resolve().parent;z=s.Symbol('d');started=time.time()
def pairing(edges):return tuple(sorted(tuple(sorted(e)) for e in edges))
@lru_cache(None)
def join(p,q,n,m,k):
 # Upper row vertices0..n-1, shared vertices n..n+m-1, lower n+m..n+m+k-1.
 parent=list(range(n+m+k))
 def find(a):
  while parent[a]!=a:a=parent[a]
  return a
 def unite(a,b):parent[find(a)]=find(b)
 for a,b in p:unite(a,b)
 for a,b in q:unite(n+a,n+b)
 groups={}
 for a in range(n+m+k):groups.setdefault(find(a),[]).append(a)
 edges=[];loops=0
 for group in groups.values():
  ends=[a if a<n else a-m for a in group if a<n or a>=n+m]
  if not ends:loops+=1
  else:assert len(ends)==2;edges.append(ends)
 return pairing(edges),loops
def add(*terms):
 out={}
 for c,x in terms:
  for p,v in x.items():out[p]=s.expand(out.get(p,0)+c*v)
 return {p:v for p,v in out.items() if v!=0}
def mul(x,y,n,m,k):
 out={}
 for p,a in x.items():
  for q,b in y.items():
   r,loops=join(p,q,n,m,k);out[r]=out.get(r,0)+a*b*z**loops
 return {p:s.expand(v) for p,v in out.items() if s.expand(v)!=0}
def perm(x,order):return {pairing([(order[a],order[b]) for a,b in p]):v for p,v in x.items()}
I={pairing([(i,4+i) for i in range(4)]):s.Integer(1)}
f1=perm(I,[2,1,0,3,4,5,6,7]);f2=perm(I,[0,3,2,1,4,5,6,7])
ainv=mul(add((4,I),(2,f1)),add((4,I),(2,f2)),4,4,4)
# M has row(j1,j2,r1,r2) and col(t1,t2), the exact contraction of A with Omega.
M={pairing([(2,3),(4,0),(5,1)]):s.Integer(1),pairing([(2,0),(4,3),(5,1)]):-s.Rational(1,2),pairing([(3,1),(5,2),(4,0)]):-s.Rational(1,2),pairing([(2,0),(3,1),(4,5)]):s.Rational(1,4)}
Mt=perm(M,[2,3,4,5,0,1])
MMt=mul(M,Mt,4,2,4)
omega={pairing([(0,1)]):s.Integer(1)}
v=mul(M,omega,4,2,0)
vt=perm(v,[0,1,2,3])
vv={pairing(list(p)+[(a+4,b+4) for a,b in q]):a0*b0 for p,a0 in v.items() for q,b0 in vt.items()}
Bnum=perm(add((5*z-4,MMt),(-1,vv)),[4,5,2,3,0,1,6,7])
T=mul(ainv,Bnum,4,4,4)
scale=9*(z-1)*(5*z-4)
powers=[I]
for j in range(8):
 powers.append(mul(T,powers[-1],4,4,4));print('power',j+1,'terms',len(powers[-1]),'seconds',time.time()-started,flush=True)
basis=sorted(set().union(*[set(x) for x in powers]))
K=s.Matrix([[x.get(p,0) for x in powers[:8]] for p in basis])
_,pivots=K.subs(z,7).T.rref();assert len(pivots)==8
square=K.extract(list(pivots),list(range(8)))
rhs=s.Matrix([-powers[8].get(basis[i],0) for i in pivots])
print('solve',time.time()-started,flush=True)
inv,den=DomainMatrix.from_Matrix(square).inv_den()
coeff=inv.to_Matrix()*rhs
den=inv.domain.to_sympy(den)
coeff=[s.cancel(x/den) for x in coeff]
for p in basis:assert s.cancel(powers[8].get(p,0)+sum(coeff[j]*powers[j].get(p,0) for j in range(8)))==0
lam=s.Symbol('lambda')
poly=s.factor((scale*lam)**8+sum(coeff[j]*(scale*lam)**j for j in range(8)))
monic=s.cancel(poly/scale**8)
g=s.cancel(monic/(lam-1))
gc=s.Poly(g,lam)
def diagram_trace(p):
 parent=list(range(8))
 def find(a):
  while parent[a]!=a:a=parent[a]
  return a
 for a,b in list(p)+[(i,i+4) for i in range(4)]:parent[find(a)]=find(b)
 return z**len({find(a) for a in range(8)})
traces=[s.expand(sum(v*diagram_trace(p) for p,v in power.items())) for power in powers[:8]]
projector_trace=s.cancel(sum(gc.nth(j)*traces[j]/scale**j for j in range(8))/g.subs(lam,1))
assert projector_trace==z**2
# Verify all remaining roots lie in[-8/9,2/3] for integer d>=3.
# Substitute d=u+3; nonnegative coefficients prove endpoint signs.
u=s.Symbol('u',nonnegative=True)
factors=s.factor_list(monic,lam)[1]
endpoint_checks=[]
for f,mult in factors:
 if s.degree(f,lam)==1 and s.cancel(f.subs(lam,1))==0:continue
 degree=s.degree(f,lam)
 if degree==1:
  lead=s.Poly(f,lam).LC();r=s.cancel(-f.subs(lam,0)/lead)
  expressions=[s.cancel(r+s.Rational(8,9)),s.cancel(s.Rational(2,3)-r)]
 else:
  assert degree==2
  expressions=[s.Poly(f,lam).LC(),-f.subs(lam,0),f.subs(lam,-s.Rational(8,9)),f.subs(lam,s.Rational(2,3))]
 checks=[]
 for x in expressions:
  num,den=s.fraction(s.cancel(x));pn=s.Poly(s.expand(num.subs(z,u+3)),u);pd=s.Poly(s.expand(den.subs(z,u+3)),u)
  if pd.LC()<0:pn=-pn;pd=-pd
  assert all(v>=0 for v in pn.all_coeffs()) and pn.eval(0)>=0 and pn.as_expr()!=0
  assert all(v>=0 for v in pd.all_coeffs()) and pd.eval(0)>0
  checks.append({'numerator_at_d_u_plus3':str(pn.as_expr()),'denominator_at_d_u_plus3':str(pd.as_expr())})
 endpoint_checks.append({'factor':str(f),'degree':int(degree),'positive_checks':checks})
out={'status':'AUTHOR_DIAGRAM_IDENTITY_TRACE_AND_SPECTRAL_BOUNDS_PASS','dimension_parameter':str(z),'R_scaling':str(scale),'annihilator_of_R':str(poly),'identity_basis_terms':len(basis),'power_coefficients':[str(x) for x in coeff],'eigenvalue1_projector_trace':str(projector_trace),'other_roots_interval':['-8/9','2/3'],'spectral_endpoint_checks':endpoint_checks,'seconds':time.time()-started,'scope':'Author formal diagram-algebra identity and analytic coefficient-sign bounds for d>=3. Not Lean formalization, independent audit, priority or score; construction comparison still required.'}
(root/'werner370-brauer.json').write_bytes((json.dumps(out,indent=2)+'\n').encode());print(json.dumps(out),flush=True)
