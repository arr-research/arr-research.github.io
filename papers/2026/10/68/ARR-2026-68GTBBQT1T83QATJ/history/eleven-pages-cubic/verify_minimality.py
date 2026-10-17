"""Author-context diagnostics for the four-qubit minimality theorem.

Exact identities and finite numerical checks supplement, not replace, the proof.
Run in a writable copy; writes minimality-diagnostics.json beside this script.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
import sympy as sp

root=Path(__file__).parent
p=sp.symbols('p', real=True)
h=p+p**2/10-p**3
hp=sp.diff(h,p); hpp=sp.diff(hp,p)
assert sp.simplify(hp-(1+p/5-3*p*p))==0
assert hp.subs(p,sp.Rational(1,2))==sp.Rational(7,20)
assert hp.subs(p,sp.Rational(1,30))==sp.Rational(301,300)
assert hpp.subs(p,sp.Rational(1,30))==0
assert h.subs(p,sp.Rational(1,2))==sp.Rational(2,5)
H=lambda p:p+p*p/10-p*p*p
D=lambda p:1+p/5-3*p*p
A=lambda p:(6*p-.2)/D(p)
def inverse(y):
    y=np.asarray(y,dtype=float)
    lo=np.zeros_like(y); hi=np.full_like(y,.5)
    for _ in range(60):
        mid=(lo+hi)/2
        take=H(mid)<y
        lo=np.where(take,mid,lo); hi=np.where(take,hi,mid)
    return (lo+hi)/2

x,y,a,b=Q(1,100),Q(3,100),Q(1,50),Q(12,25)
HQ=lambda p:p+p*p/Q(10)-p*p*p
c=(HQ(x)+HQ(y))/2
assert c-HQ(a)==Q(1,250000)
assert c/HQ(b)==Q(5009,98112)
assert x+y+2*b==1 and all(Q(0)<t<Q(1,2) for t in [x,y,b])
assert Q(13,11)-Q(1,5)==Q(54,55)>0

rng=np.random.default_rng(2026101709)
# Uniform surface sampling of the capped simplex, plus near-vertex probes.
states=[]
while len(states)<5000:
    batch=rng.dirichlet(np.ones(3),size=10000)
    states.extend(batch[np.max(batch,axis=1)<=.5].tolist())
states=np.asarray(states[:5000])
near=[]
for e in [0,1e-12,1e-8,1e-5,.001,.01,1/30]:
    for t in [0,.1,.5,.9,1]:
        q=np.array([e,.5-t*e,.5-(1-t)*e])
        for shift in range(3):near.append(np.roll(q,shift))
states=np.vstack([states,np.asarray(near)])
# Tangent quadratic form with v=(u,v,-u-v).
curvature=A(states)
minimum=1e9
for aa in curvature:
    M=np.array([[aa[0]+aa[2],aa[2]],[aa[2],aa[1]+aa[2]]])
    minimum=min(minimum,float(np.linalg.eigvalsh(M)[0]))
assert minimum>0
idx=rng.integers(0,len(states),size=(10000,2)); t=rng.random((10000,1))
z=t*H(states[idx[:,0]])+(1-t)*H(states[idx[:,1]])
budgets=inverse(z).sum(axis=1)
assert float(budgets.max())<=1+1e-13

# Check the capped graph on the full rectangle, not only its curved patch.
uv=rng.random((15000,4))*.4
weights=rng.random(15000)
def graph(z):
    s=inverse(z).sum(axis=1)
    return np.where(s<=.5,.4,H(1-s))
left,right=uv[:,:2],uv[:,2:]
mix=weights[:,None]*left+(1-weights[:,None])*right
gaps=graph(mix)-weights*graph(left)-(1-weights)*graph(right)
assert gaps.min()>-2e-14

z4=np.array([float(c),float(c),float(HQ(b)),float(HQ(b))])
witness_budget=float(inverse(z4).sum())
assert witness_budget>1
report={'status':'PASS','scope':'Proposed supplement; author-context exact identities and finite diagnostics, not independent review or a formal universal proof.',
 'polynomial':'h(p)=p+p^2/10-p^3, 0<=p<=1/2',
 'exact_facts':{'h_max':'2/5','h_prime_min':'7/20','h_prime_max':'301/300','curvature_sign_change':'1/30','midpoint_gap':'1/250000','w4_weights':['5009/98112','5009/98112','1','1'],'tangent_lower_bound_in_nonconcave_case':'54/55 times the square of the exceptional coordinate'},
 'boundary_points_tested':len(states),'minimum_tangent_matrix_eigenvalue_numeric':minimum,
 'midpoint_pairs_tested':10000,'maximum_inverse_entropy_budget_numeric':float(budgets.max()),
 'graph_jensen_pairs_tested':15000,'minimum_graph_jensen_gap_numeric':float(gaps.min()),
 'w4_inverse_entropy_budget_numeric':witness_budget,
 'seed':2026101709,'priority_confirmed':False,'independent_review':False}
(root/'minimality-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
