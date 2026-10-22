"""Symbolic initial five-profile block for large uniform odd-cycle blowups.
Exploration: identities are checked against exact classified patterns.
"""
from pathlib import Path
import sympy as sp,json,time
from odd_cycle_ground_kernels import ground
R=Path(__file__).parent;s,k,B,t=sp.symbols('s k B t',integer=True,positive=True)
def split_pattern(kk,ss,tt,partial=None):
    a=[0]*(2*kk+1);a[0]=tt;a[1]=(ss-1 if partial is None else ss)-tt
    for j in range(kk-1):a[3+2*j]=ss-int(j==partial)
    return a
def endpoint_pattern(kk,ss,j):
    a=[0]*(2*kk+1)
    for i in range(kk):a[2*i]=ss-int(i==j)
    return a
def low(a):
    m=len(a);b=[sp.expand(s-x) for x in a]
    rr=[sp.expand(a[(i-1)%m]+a[i]+a[(i+1)%m]) for i in range(m)]
    nu=sp.zeros(5,1);C=sp.zeros(5)
    vectors=[]
    for i in range(m):
        v=sp.zeros(5,1)
        for j in range(5):
            if sp.expand(rr[i]-(s-1+j))==0:nu[j]+=b[i];v[j]+=1
            if sp.expand(rr[i]+1-(s-1+j))==0:v[j]-=1
        vectors.append(v)
        C+=b[i]*(b[i]-1)*(v*v.T)
    for i in range(m):
        j=(i+1)%m
        C+=b[i]*b[j]*(vectors[i]*vectors[j].T+vectors[j]*vectors[i].T)
    return (nu*nu.T-sp.diag(*nu)-C).applyfunc(sp.expand)
def choose(j):
    return sp.prod(s-i for i in range(j))/sp.factorial(j)
def A(kk):
    base=low(split_pattern(kk,s,t));M=s*B/(s+1)*base
    for j in range(5):
        w=choose(j)*choose(j+1)
        for val in [j,s-1-j]:M+=w*(low(split_pattern(kk,s,val))-base)
    return M.applyfunc(sp.factor)
def BB(kk,partial):
    base=low(split_pattern(kk,s,t,partial));M=s*B*base
    for j in range(5):
        w=s*choose(j)**2
        for val in [j,s-j]:M+=w*(low(split_pattern(kk,s,val,partial))-base)
    return M.applyfunc(sp.factor)
def full(kk):
    if kk==2:return (A(2)+BB(2,0)-s*low(endpoint_pattern(2,s,0))-s*low(endpoint_pattern(2,s,1))).applyfunc(sp.factor)
    return (A(4)+2*BB(4,0)+(k-3)*BB(4,1)-2*s*low(endpoint_pattern(4,s,0))-(k-2)*s*low(endpoint_pattern(4,s,1))).applyfunc(sp.factor)
out=[]
for mode in [2,3]:
    M=full(mode)
    checks=[]
    for ss in [11,12,13,17,25]:
        for kk in ([2] if mode==2 else [3,4,8,20]):
            L,N=ground(kk,ss);a=list(range(ss-1,ss+4))
            assert M.subs({s:ss,k:kk,B:sp.binomial(2*ss,ss)})*(2*kk+1)==L.extract(a,a),(mode,ss,kk)
            checks.append([kk,ss])
    print(json.dumps(dict(mode=mode,identity_checks=len(checks))),flush=True)
    dets=[]
    for r in [2,3,4,5]:
        dd=sp.factor(M[:r,:r].det(method='domain-ge'))
        dets.append(dict(r=r,det=str(dd)))
        print('mode',mode,'r',r,'len',len(str(dd)),flush=True)
    out.append(dict(mode=mode,matrix=[[str(x) for x in row] for row in M.tolist()],checks=checks,determinants=dets))
(R/'odd-initial-five-symbolic.json').write_text(json.dumps(dict(status='identities checked; signs not yet proved',domain='integer s>=11; k=2 or k>=3',rows=out),indent=2)+'\n')
