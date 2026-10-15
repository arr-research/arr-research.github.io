"""Checks by the referee. Numerical checks are diagnostics, not universal proofs."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib,json,math
import numpy as np

P=Path(__file__).resolve().parent
rng=np.random.default_rng(15102026)
groups=[]
def record(name,**kw):groups.append({'name':name,'status':'PASS',**kw})

def W(d,a,b):
    z=np.exp(2j*np.pi/d)
    out=np.zeros((d,d),complex)
    t=np.arange(d)
    out[(t+a)%d,t]=z**(b*t)
    return out

# Exact permutation/phase comparison for blocks, including the carry in j+delta.
block_checks=0
for d in (4,8,9,16,27,32):
    for q in range(2,d+1):
        if d%q:continue
        n=d//q
        for delta in range(q):
            cosets=[(a,b) for a in range(delta,d,q) for b in range(n)]
            labels=[((a-delta)//q%n,b%n) for a,b in cosets]
            assert len(set(labels))==len(cosets)==n*n
            for a,b in cosets:
                for j in range(q):
                    carry=(j+delta)//q
                    for t in range(n):
                        direct=(j+q*t+a)%d
                        formula=(j+delta)%q+q*((t+(a-delta)//q+carry)%n)
                        assert direct==formula
                        assert (b*(j+q*t)-(b*j+q*b*t))%d==0
                        block_checks+=1
record('exact block labels, action and common carries',identities=block_checks)

# The phases of W_g^* W_{g+h}, tested as exact exponents on columns 0 and 1.
phase_checks=0
for d in (4,8,9,16,27,32):
    for a in range(d):
      for b in range(d):
       for ah in range(d):
        for bh in range(d):
         for t in (0,1):
          direct=((b+bh)*t-b*(t+ah))%d
          assert direct==(-b*ah+bh*t)%d
          phase_checks+=1
record('exact adjoint-product phases',identities=phase_checks)

# A single directed cycle: exits equal number of nonempty proper occupied chains.
cycle_checks=0
for q in (2,3,4,8,9,16):
    for mask in range(1<<q):
        bits=[(mask>>j)&1 for j in range(q)]
        count=sum(bits)
        overlap=sum(bits[j]*bits[(j+1)%q] for j in range(q))
        exits=sum(bits[j]*(1-bits[(j+1)%q]) for j in range(q))
        assert count-overlap==exits
        if exits==0:assert count in (0,q)
        if exits==1:
            start=next(j for j in range(q) if bits[j] and not bits[(j-1)%q])
            expected={(start+t)%q for t in range(count)}
            assert expected=={j for j in range(q) if bits[j]}
        cycle_checks+=1
record('exact one-exit orbit classification',binary_cycles=cycle_checks)

# Exact arithmetic for all claimed cases and the two extra coprime cases.
claims=[(16,6,5,4),(16,7,5,4),(32,5,4,8),(32,11,10,4),
        (27,6,5,6),(27,7,5,6),(27,14,13,3),(8,3,2,4)]
bounds=[]
for d,s,mu,target in claims:
    k=1+Q(mu*(s-1),s)
    r=math.ceil(Q(d)/k)
    assert r==target
    bounds.append({'d':d,'s':s,'mu':mu,'K':str(k),'rank_bound':r})
record('exact claimed rounded rank bounds',bounds=bounds)

# Symplectic normalizer for each nonzero label. Build M directly over Z/d.
# h=n(a0,b0), n=gcd(d,a,b), and at least one of a0,b0 is a unit for prime powers.
normalizers=0
for d,p in ((4,2),(8,2),(9,3),(16,2),(27,3),(32,2)):
 for a in range(d):
  for b in range(d):
   if a==b==0:continue
   n=math.gcd(d,math.gcd(a,b)); a0=a//n;b0=b//n
   if math.gcd(a0,d)==1:
    u=pow(a0,-1,d)
    M=(b0,-a0,u,0) # det a0*u=1; M*h=(0,n)
   else:
    u=pow(b0,-1,d)
    M=(b0,-a0,0,u)
   x,y,z,w=M
   assert (x*w-y*z)%d==1
   assert ((x*a+y*b)%d,(z*a+w*b)%d)==(0,n)
   normalizers+=1
record('exact SL2 maps h itself to vertical generator',labels=normalizers)

# Check representative Fourier/chirp conjugations as matrices, including even d.
clifford_err=0.
for d,p in ((4,2),(8,2),(9,3),(16,2),(27,3),(32,2)):
    z=np.exp(2j*np.pi/d);t=np.arange(d)
    F=z**np.outer(t,t)/math.sqrt(d)
    for a,b in ((1,0),(0,1),(1,1),(d//p,2),(d-1,d-1)):
        A=W(d,a,b)
        clifford_err=max(clifford_err,float(np.max(abs(F@A@F.conj().T-z**(-a*b)*W(d,-b,a)))))
        for slope in (1,2,d-1):
            if p==2:
                qdiag=np.exp(1j*np.pi*slope*t*t/d)
                phase=np.exp(1j*np.pi*slope*a*a/d)
            else:
                half=pow(2,-1,d)
                qdiag=z**(slope*half*t*t)
                phase=z**(slope*half*a*a)
            actual=qdiag[:,None]*A*qdiag.conj()[None,:]
            predicted=phase*W(d,a,(b+slope*a)%d)
            clifford_err=max(clifford_err,float(np.max(abs(actual-predicted))))
assert clifford_err<1e-8
record('numerical Fourier/chirp covariance',max_error=clifford_err)

moment_err=0.;moment_excess=-1.;tail_excess=-1.;examples=0
for d,s in ((8,3),(16,6),(16,7),(27,6),(27,7),(27,14),(32,5),(32,11)):
 for _ in range(12):
    labels=rng.choice(d*d,s,replace=False)
    S=[(int(g)//d,int(g)%d) for g in labels]
    c=rng.normal(size=s)+1j*rng.normal(size=s)
    A=sum((v*W(d,*g) for g,v in zip(S,c)),np.zeros((d,d),complex))
    H=A.conj().T@A
    coeff={}
    mult=Counter()
    z=np.exp(2j*np.pi/d)
    for i,(a,b) in enumerate(S):
     for j,(aa,bb) in enumerate(S):
        h=((aa-a)%d,(bb-b)%d)
        coeff[h]=coeff.get(h,0)+c[i].conjugate()*c[j]*z**(-b*h[0])
        if h!=(0,0):mult[h]+=1
    expansion=sum((v*W(d,*h) for h,v in coeff.items()),np.zeros((d,d),complex))
    moment_err=max(moment_err,float(np.max(abs(H-expansion))))
    M=float(sum(abs(c)**2));Q4=float(sum(abs(c)**4));mu=max(mult.values(),default=0)
    fourth=float(np.trace(H@H).real/d)
    upper=M*M+mu*(M*M-Q4)
    moment_excess=max(moment_excess,(fourth-upper)/(M*M))
    singular=np.linalg.svd(A,compute_uv=False)
    weights=singular**2/sum(singular**2)
    K=1+mu*(1-1/s)
    for r in (1,3,min(5,d-1)):
        lower=max(0,1-r/d-math.sqrt(r*(d-r)*(K-1))/d)
        tail=float(sum(weights[r:]))
        tail_excess=max(tail_excess,lower-tail)
    examples+=1
assert moment_err<1e-8 and moment_excess<1e-10 and tail_excess<1e-10
record('numerical moment and spectral-tail diagnostics',examples=examples,max_expansion_error=moment_err,max_normalized_moment_excess=moment_excess,max_tail_excess=tail_excess)

# Budget sharpness for d16: subgroup polynomial has exactly m terms and rank 16/m.
for m in (1,2,4,8,16):
    A=sum((W(16,0,j*(16//m)) for j in range(m)),np.zeros((16,16),complex))
    assert np.linalg.matrix_rank(A,tol=1e-10)==16//m
record('numerical d16 budget-attainment examples',budgets=[1,2,4,8,16])

data={'status':'PASS','groups':groups,
 'candidate_sha256':hashlib.sha256((P/'proof-candidate.txt').read_bytes()).hexdigest(),
 'd16_rank3_squared_distance_bounds':{str(s):1-Q(3,16)-math.sqrt(3*13*(float(1+Q(5*(s-1),s))-1))/16 for s in (6,7)},
 'limitations':'Exact finite arithmetic checks confirm formulas and case arithmetic; numerical matrix checks are diagnostics, not proofs over arbitrary supports or coefficients.'}
(P/'astra-independent-checks.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(data,ensure_ascii=False,indent=2))
