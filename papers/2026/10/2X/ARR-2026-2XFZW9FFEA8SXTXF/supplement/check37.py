"""Exact finite checks of the proposed oracle, kernel, and inner-ball construction.
Does not implement GLS or prove its complexity theorem.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import factorial
import json,sympy as s
R=Path(__file__).resolve().parent;out=R/'checks-37.json';assert not out.exists()
I=s.I;z,w=s.symbols('z w')
def clean(v):return s.cancel(s.expand_complex(v))
def kernel(a,b,Z,W):
    return clean(sum(s.Rational(factorial(a+b-h),factorial(a-h)*factorial(b-h)*factorial(h))*W**(a-h)*Z**(b-h)/(1-Z*W)**(a+b-h+1) for h in range(min(a,b)+1)))
kernel_checks=0
for Z,W in [(s.Rational(1,3),-s.Rational(1,4)),((1+I)/4,(1-I)/5),(s.Integer(0),s.Rational(1,2))]:
 for a in range(3):
  for b in range(3):
   exact=s.diff(1/(1-z*w),z,a,w,b).subs({z:Z,w:W})/(s.factorial(a)*s.factorial(b))
   assert clean(exact-kernel(a,b,Z,W))==0;kernel_checks+=1
def pick(nodes,mults,jets):
    keys=[(j,p) for j,n in enumerate(mults) for p in range(n)]
    v={j:[sum(jets[(j,h)]*jets[(j,p-h)] for h in range(p+1)) for p in range(n)] for j,n in enumerate(mults)}
    return s.Matrix([[clean((sum(v[j][a]*kernel(p-a,l,nodes[j],s.conjugate(nodes[k])) for a in range(p+1))-sum(s.conjugate(v[k][b])*kernel(p,l-b,nodes[j],s.conjugate(nodes[k])) for b in range(l+1)))/I) for k,l in keys] for j,p in keys])
def exact_psd(A):
    assert A==A.conjugate().T
    A=A.copy()
    while A.rows:
        for j in range(A.rows):
            assert s.im(A[j,j])==0
            if A[j,j]<0:return False
            if A[j,j]==0 and any(A[j,k]!=0 for k in range(A.rows)):return False
        inds=[j for j in range(A.rows) if A[j,j]>0]
        if not inds:return True
        j=inds[0];others=[k for k in range(A.rows) if k!=j]
        A=s.Matrix([[clean(A[a,b]-A[a,j]*A[j,b]/A[j,j]) for b in others] for a in others])
    return True
assert exact_psd(s.Matrix([[1,I],[-I,1]]))
assert not exact_psd(s.Matrix([[0,1],[1,0]]))
assert not exact_psd(s.diag(1,-1))
assert exact_psd(s.zeros(3))

# Rank-one confluent data from g=2i(1+z)/(1-z), f the quadrant square root.
fseries=s.series((1+I)*s.sqrt((1+z)/(1-z)),z,0,5).removeO().expand()
j0={(0,p):fseries.coeff(z,p) for p in range(5)}
P0=pick([s.Integer(0)],[5],j0);assert P0.rank()==1 and exact_psd(P0)
midpoint_checks=0
for lam in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
    jt={(0,p):lam*j0[(0,p)]+(1-lam)*(1+I if p==0 else 0) for p in range(5)}
    assert exact_psd(pick([s.Integer(0)],[5],jt));midpoint_checks+=1

nodes=[s.Integer(0),(1+I)/4,-s.Rational(1,3)];mults=[2,1,2]
keys=[(j,p) for j,nj in enumerate(mults) for p in range(nj)];m=len(keys)
V=s.Matrix([[s.binomial(ell,p)*nodes[j]**(ell-p) if ell>=p else 0 for ell in range(m)] for j,p in keys]);inv=V.inv().applyfunc(clean)
T=max(s.Integer(1),sum(abs(s.re(v))+abs(s.im(v)) for v in inv));r0=1/(4*T)
coords=[(key,part) for key in keys for part in ['real','imag'] if not(key==(0,0) and part=='imag')]
inner_checks=0
for key,part in coords:
 for sign in [-1,1]:
    delta=s.zeros(m,1);delta[keys.index(key)]=sign*r0*(1 if part=='real' else I)
    coeff=inv*delta
    assert sum(abs(s.re(v))+abs(s.im(v)) for v in coeff)<=s.Rational(1,4)
    jt={k:(1+I if k[1]==0 else 0)+delta[idx] for idx,k in enumerate(keys)}
    assert exact_psd(pick(nodes,mults,jt));inner_checks+=1

# Concrete constants for the rational-profile two-node example.
nodes2=[s.Integer(0),-s.Rational(1,3)]
radii=[(1+abs(v)**2)/2 for v in nodes2]
Us=[(1+r)/(1-r) for r in radii]
B=1+s.Rational(25,4)*sum(Us);eps=s.Rational(1,1024)
delta=eps/(4*(B+1));C=2*B+2
assert B==s.Rational(333,8) and delta< s.Rational(1,2) and C>=4
assert delta*(B+1)==eps/4
result={'at':datetime.now(timezone.utc).isoformat(),'kernel_coefficient_checks':kernel_checks,
 'exact_psd_negative_and_singular_controls':4,'confluent_rank_one_size':5,
 'convex_midpoint_checks':midpoint_checks,'inner_ball_coordinate_checks':inner_checks,
 'hermite_nodes':[str(v) for v in nodes],'hermite_multiplicities':mults,
 'inner_radius':str(r0),'two_node_B':str(B),'two_node_epsilon':str(eps),
 'two_node_delta':str(delta),'exact_truncation_error_bound':str(eps/4),
 'scope':'Exact finite identities/instances; no GLS implementation,no general QE,no formal proof,no grade.'}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
