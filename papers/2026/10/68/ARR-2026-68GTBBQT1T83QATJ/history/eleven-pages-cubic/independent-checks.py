from fractions import Fraction as Q
from pathlib import Path
import json, sys, itertools
import numpy as np
from scipy.optimize import brentq,linprog
import sympy, scipy, mpmath, pypdf
root=Path(__file__).parent
hq=lambda p:p+p*p/Q(10)-p*p*p
hp=lambda p:1+p/Q(5)-3*p*p
hpp=lambda p:Q(1,5)-6*p
# Independent, rational quantitative separation for the manuscript's cubic W4 witness.
a,b=Q(1,50),Q(12,25)
c=Q(5009,250000); w=Q(5009,98112); d=hq(b)
eps=Q(19,5000000); delta=Q(3,2000000)
t0=d-delta
slacks=[t0*w-hq(a+eps), t0-hq(b-eps)]
assert all(x>0 for x in slacks)
assert 2*(a+eps)+2*(b-eps)==1
# Thus any feasible state at t0 would have each mu strictly above the indicated lower bounds, sum>1.
# Exact rational Hessians on a boundary mesh, including endpoint/near-corner values.
n=100; count=0; min_det=None
for i in range(n+1):
 for j in range(n+1):
  p1,p2=Q(i,2*n),Q(j,2*n); p3=1-p1-p2
  if not 0<=p3<=Q(1,2):continue
  g11=hpp(p3)/hp(p1)**2+hp(p3)*hpp(p1)/hp(p1)**3
  g22=hpp(p3)/hp(p2)**2+hp(p3)*hpp(p2)/hp(p2)**3
  g12=hpp(p3)/(hp(p1)*hp(p2))
  det=g11*g22-g12*g12
  assert g11<=0 and g22<=0 and det>=0
  min_det=det if min_det is None else min(min_det,det)
  count+=1
rng=np.random.default_rng(2026101719)
# Inactive-weight cases. LP uses the one-excitation probabilities; actual matrices give attainment.
weighted=0; worst=0
for k in range(2,9):
 for s in range(1,k+1):
  for repeat in range(2):
   xi=np.zeros(k); active=rng.choice(k,s,replace=False)
   xi[active]=rng.uniform(.05,1,s);xi/=xi.max()
   fun=lambda t:sum(t**(-xi[active]))-(s-1)
   value=2. if fun(2)>=0 else brentq(fun,1,2,xtol=1e-14)
   lower=1-value**(-xi)
   lp=linprog(np.zeros(k),A_eq=np.ones((1,k)),b_eq=[1],bounds=list(zip(lower,np.full(k,.5))),method='highs')
   assert lp.success
   r=lp.x; psi=np.zeros((2,)*k,complex)
   for j in range(k):
    ix=[0]*k;ix[j]=1;psi[tuple(ix)]=np.sqrt(max(0,r[j]))
   lam=[]
   for j in range(k):
    mat=np.moveaxis(psi,j,0).reshape(2,-1);lam.append(np.linalg.eigvalsh(mat@mat.conj().T)[-1])
   actual=np.min(np.asarray(lam)[active]**(-1/xi[active]))
   worst=max(worst,abs(actual-value));assert abs(actual-value)<1e-9
   weighted+=1
# Arbitrary compact finite E, active-coordinate LP and its support/radial dual.
convex_cases=0; worst_dual=0; max_extra_support=0
for k in range(2,8):
 for s in range(1,k+1):
  for rep in range(3):
   E=rng.uniform(0,2,(19,k)); xi=np.zeros(k);I=rng.choice(k,s,False);xi[I]=rng.uniform(.1,1,s);xi/=xi.max()
   A=np.column_stack((-E[:,I].T,xi[I]));obj=np.r_[np.zeros(19),-1.]
   primal=linprog(obj,A_ub=A,b_ub=np.zeros(s),A_eq=np.array([np.r_[np.ones(19),0.]]),b_eq=[1.],bounds=[(0,None)]*20,method='highs')
   dual=linprog(np.r_[np.zeros(s),1.],A_ub=np.column_stack((E[:,I],-np.ones(19))),b_ub=np.zeros(19),A_eq=np.array([np.r_[xi[I],0.]]),b_eq=[1.],bounds=[(0,None)]*(s+1),method='highs')
   assert primal.success and dual.success
   err=abs(-primal.fun-dual.fun);worst_dual=max(worst_dual,err);assert err<1e-9
   support=np.count_nonzero(primal.x[:19]>1e-9);max_extra_support=max(max_extra_support,support-s);assert support<=s
   theta=rng.dirichlet(np.ones(k));f=max(E@theta)
   candidate=[]
   for e in E:
    xx=e/e.max();gg=max(np.min(E/xx,axis=1));candidate.append(gg*(theta@xx))
   assert abs(max(candidate)-f)<1e-10
   convex_cases+=1
out={'status':'PASS','scope':'Checks written in this review; finite diagnostics are not universal proofs.',
 'rational_cubic_w4':{'d':str(d),'xi_first':str(w),'t0':str(t0),'certified_gap_strictly_greater_than':str(delta),'comparison_points':[str(a+eps),str(b-eps)],'positive_slacks':[str(x) for x in slacks]},
 'rational_hessian_mesh':{'tested':count,'mesh_step':'1/200','minimum_determinant':str(min_det)},
 'inactive_weight_cases':{'tested':weighted,'k_range':[2,8],'all_support_sizes':True,'max_attainment_error':worst},
 'finite_E_duality':{'tested':convex_cases,'maximum_error':worst_dual,'support_excess':max_extra_support},
 'seed':2026101719,
 'versions':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__,'mpmath':mpmath.__version__,'pypdf':pypdf.__version__}}
(root/'independent-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
