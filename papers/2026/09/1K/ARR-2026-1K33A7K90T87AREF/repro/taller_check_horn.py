"""Targeted checks from Horn's recursive definition; author code not supplied."""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from fractions import Fraction as Q
import json, random, time
import numpy as np
import scipy
from scipy.optimize import linprog

start=time.time()
@lru_cache(None)
def horn(n,r):
    subs=list(combinations(range(1,n+1),r))
    bysum={}
    for K in subs:bysum.setdefault(sum(K),[]).append(K)
    tests=[(A,B,C,p*(p+1)//2) for p in range(1,r) for A,B,C in horn(r,p)]
    result=[]
    for I in subs:
        for J in subs:
            for K in bysum.get(sum(I)+sum(J)-r*(r+1)//2,[]):
                if all(sum(I[a-1] for a in A)+sum(J[b-1] for b in B)<=sum(K[c-1] for c in C)+limit for A,B,C,limit in tests):
                    result.append((I,J,K))
    return tuple(result)

def forms(a,b2):
    m=len(a);b1=sum(a)-b2
    F=[k*b1+sum((j-k if j<=k else (j-k+1)//2)*x for j,x in enumerate(a,1)) for k in range(m)]
    G=[b2+sum((j//2)*x for j,x in enumerate(a,1))+a[j-1]-(a[j] if j<m else 0) for j in range(1,m+1,2)]
    return max(F+G)

counts={};generators={}
for n in range(2,8):
    counts[n]=[len(horn(n,r)) for r in range(1,n)]
    generators[n]=[t for r in range(1,n) for t in horn(n,r)]
    print('Horn',n,counts[n],flush=True)
assert counts[6]==[21,126,228,126,21]
assert counts[7]==[28,252,751,751,252,28]

def horn_matrix(n):
    rows=[]
    for I,J,K in generators[n]:
        row=[0]*n
        for i in I:row[i-1]+=1
        for j in J:row[n-j]-=1
        rows.append(row)
    return np.array(rows,dtype=float)

rng=random.Random(20260908)
trials=[]
for n in range(4,8):
    H=horn_matrix(n)
    order=np.zeros((n-1,n))
    for i in range(n-1):order[i,i]=-1;order[i,i+1]=1
    A=np.vstack([-H,order])
    for m in range(2,n-1):
        largest_error=0
        for t in range(20):
            a=sorted([Q(rng.randint(1,25),rng.randint(1,5)) for _ in range(m)],reverse=True)
            P=sum(a);b2=P*Q(rng.randint(1,50),100);b1=P-b2
            lam=a+[Q(0)]*(n-m-2)+[-b2,-b1]
            rhs=[-float(sum(lam[k-1] for k in K)) for I,J,K in generators[n]]+[0]*(n-1)
            result=linprog(np.ones(n),A_ub=A,b_ub=rhs,bounds=[(0,None)]*(n-1)+[(0,0)],method='highs')
            assert result.success,result.message
            error=abs(result.fun-float(forms(a,b2)))
            largest_error=max(largest_error,error)
            assert error<1e-8,(n,m,a,b2,result.fun,forms(a,b2))
        trials.append({'d':n,'m':m,'zeros':n-m-2,'cases':20,'max_abs_error':largest_error})

def exact_check(lam,spec):
    assert sorted(spec,reverse=True)==spec and min(spec)>=0
    vals=[]
    for I,J,K in generators[len(lam)]:
        slack=sum(spec[i-1] for i in I)-sum(spec[len(lam)-j] for j in J)-sum(lam[k-1] for k in K)
        assert slack>=0,(I,J,K,slack)
        vals.append(slack)
    return {'inequalities':len(vals),'minimum_slack':str(min(vals))}

family=[]
for t in [Q(0),Q(1,4),Q(1,2)]:
    lam=[Q(2),Q(2),Q(3,2),Q(0),Q(-5,2),Q(-3)]
    spec=[Q(7,2)-t,Q(5,2),Q(3,2),t,Q(0),Q(0)]
    check=exact_check(lam,spec)
    assert sum(spec)==Q(15,2)
    family.append(dict(t=str(t),cost=str(sum(spec)),rank=sum(x>0 for x in spec),**check))
for sigma in [Q(2),Q(9,4),Q(5,2)]:
    lam=[Q(4),Q(3),Q(2),Q(1),Q(-5,2),Q(-15,2)]
    spec=[Q(15,2),6-sigma,sigma,Q(1),Q(0),Q(0)]
    exact_check(lam,spec)

C=np.zeros((6,6))
C[1,0]=.5244;C[2,0]=2.1737
C[3,1]=2.4665;C[3,2]=.3224;C[4,1]=.4375;C[4,2]=.7881
C[5,3]=-1.4790;C[5,4]=-.9014
F=np.diag([-2.5,-3,2,2,0,1.5])
res=np.linalg.norm(C@C.T-C.T@C-2*F)
output={'date':'2026-09-08','scipy':scipy.__version__,'horn_counts':counts,'lp_trials':trials,'lp_total_cases':sum(t['cases'] for t in trials),'exact_rank_family':family,'other_exact_spectra_checked':3,'printed_rounded_matrix_residual':float(res),'printed_rounded_matrix_cost':float(np.linalg.norm(C)**2/2),'elapsed_seconds':time.time()-start,'limits':'Finite numerical LP checks do not prove the dimension-free formula. Exact inequalities certify only the listed spectra.'}
(Path(__file__).resolve().parent/'checks-horn.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
print(json.dumps(output,indent=2),flush=True)
