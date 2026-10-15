"""Reproducible finite checks, not a substitute for the analytic proof.
Python 3.12; numpy and sympy. All files remain beside this script.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import gcd,ceil,sqrt
import json, itertools, numpy as np, sympy as sp
ROOT=Path(__file__).parent
results={}
def record(name,value): results[name]=value
def W(d,a,b):
    out=np.zeros((d,d),complex);j=np.arange(d)
    out[(j+a)%d,j]=np.exp(2j*np.pi*b*j/d)
    return out
def overlap(S,d):
    counts=Counter(((b[0]-a[0])%d,(b[1]-a[1])%d) for a in S for b in S if a!=b)
    return max(counts.values(),default=0)

# Exact arithmetic for all scalar rank thresholds used in the manuscript.
cases=[(8,3,2,4),(16,6,5,4),(16,7,5,4),(32,5,4,8),(32,11,10,4),(27,6,5,6),(27,7,5,6),(27,14,13,3)]
thresholds=[]
for d,s,mu,r in cases:
    k=1+F(mu*(s-1),s); bound=F(d)/k
    assert ceil(bound)==r
    thresholds.append(dict(d=d,s=s,mu=mu,K=str(k),bound=str(bound),integer_bound=r))
record('exact_thresholds',thresholds)

# Each occupied run in a finite cycle contributes one exit unless the cycle is full.
cycles=0
for q in (2,3,4,8,9,16):
    for mask in range(1<<q):
        S={j for j in range(q) if mask>>j&1}
        exits=len(S)-sum((j+1)%q in S for j in S)
        starts=sum((j-1)%q not in S for j in S)
        assert exits==starts
        if exits==1:
            first=next(j for j in S if (j-1)%q not in S)
            assert S=={(first+t)%q for t in range(len(S))}
        cycles+=1
record('exhaustive_cycle_patterns',cycles)

# Exact integer index/phase verification of the block formula for every Weyl label,
# every sector and every basis vector in each indicated case.
block_checks=0
for d,q in ((16,2),(16,4),(16,8),(16,16),(27,3),(27,9),(27,27),(32,2)):
    n=d//q
    for delta in range(q):
        labels=set()
        for a in range(delta,d,q):
            for b in range(n):
                labels.add(((a-delta)//q,b))
        assert len(labels)==n*n
    for a,b,j,t in itertools.product(range(d),range(d),range(q),range(n)):
        delta=a%q; jp=(j+delta)%q; carry=(j+delta)//q
        tp=(t+(a-delta)//q+carry)%n
        assert (j+q*t+a)%d==jp+q*tp
        assert (b*(j+q*t))%d==(b*j+q*(b%n)*t)%d
        block_checks+=1
record('exact_block_index_and_phase_checks',block_checks)

# Explicit determinant-one normalizers over Z_d: each h=g*v is mapped to (0,g).
# Finite audit is additional to the Bezout proof in the manuscript.
normalizers=0
for d in (8,16,27,32):
    for a,b in itertools.product(range(d),repeat=2):
        if a==b==0:continue
        g=gcd(gcd(a,b),d);v=(a//g,b//g)
        # At least one coordinate is a unit mod p, hence v primitive mod d.
        u=next((x,y) for x in range(d) for y in range(d) if (x*v[0]+y*v[1])%d==1)
        M=((-v[1],v[0]),(u[0],u[1]))
        # determinant -1 for this ordering; use (v_b,-v_a) instead.
        M=((v[1],-v[0]),(u[0],u[1]))
        assert (M[0][0]*M[1][1]-M[0][1]*M[1][0])%d==1
        assert ((M[0][0]*a+M[0][1]*b)%d,(M[1][0]*a+M[1][1]*b)%d)==(0,g)
        normalizers+=1
record('exact_symplectic_normalizers',normalizers)

# Sharp budget witnesses, certified by exact polynomial remainders over Q.
x=sp.Symbol('x');witnesses=[]
for d in (16,32):
    f=sum(x**(j*(d//4)) for j in range(4))
    rank=d-sp.degree(sp.gcd(f,x**d-1),x)
    assert rank==d//4
    witnesses.append(dict(d=d,sparsity=4,rank=int(rank),polynomial=str(f)))
d=27;phi=sp.Poly(sp.cyclotomic_poly(d,x),x);zeros=[]
# (z^18+z^9+1)(z^3-zeta_3), evaluated with zeta_3=x^9, z=x^j.
for j in range(27):
    f=sp.Poly((x**(18*j)+x**(9*j)+1)*(x**(3*j)-x**9),x)
    if f.rem(phi).is_zero:zeros.append(j)
assert len(zeros)==21
witnesses.append(dict(d=27,sparsity=6,rank=6,zero_exponents=zeros))
record('exact_sharp_budget_witnesses',witnesses)

# Numeric diagnostics of the twisted convolution, fourth moment and distance bound.
rng=np.random.default_rng(20261015);worst_identity=0.;numeric_count=0
for d in (4,8,9,16,27,32):
    for k in range(80):
        s=int(rng.integers(1,min(d,15)+1));ids=rng.choice(d*d,s,replace=False)
        S=[divmod(int(v),d) for v in ids];c=rng.normal(size=s)+1j*rng.normal(size=s)
        C=sum((ci*W(d,*g) for ci,g in zip(c,S)),np.zeros((d,d),complex))
        A=C.conj().T@C;coeff={}
        for g,cg in zip(S,c):
            for v,cv in zip(S,c):
                h=((v[0]-g[0])%d,(v[1]-g[1])%d)
                coeff[h]=coeff.get(h,0)+cg.conjugate()*cv*np.exp(-2j*np.pi*g[1]*h[0]/d)
        E=sum(abs(v)**2 for v in coeff.values());M=float(np.vdot(c,c).real);Q=float(sum(abs(c)**4));mu=overlap(S,d)
        fourth=float(np.trace(A@A).real/d)
        rel=abs(E-fourth)/max(E,1);worst_identity=max(worst_identity,rel)
        assert rel<2e-11
        assert E<=M*M+mu*(M*M-Q)+1e-9*max(E,1)
        lam=np.linalg.svd(C,compute_uv=False)**2;lam=lam/lam.sum()
        K=1+mu*(1-1/s)
        for r in (1,max(1,d//4),max(1,d//2)):
            lower=max(0,1-r/d-sqrt(r*(d-r)*max(K-1,0))/d)
            assert lam[r:].sum()+2e-12>=lower
        numeric_count+=1
record('numerical_diagnostics',dict(instances=numeric_count,max_relative_fourth_moment_error=worst_identity,scope='Floating point checks only; not proof of universal rank claims.'))
record('status','PASS')
(ROOT/'verification-results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
