"""Independent small-dimensional checks; no companion verification code imported.
Haar twirls are computed as HS projections onto the permutation commutant,
including the fourth moment (no Clifford-design substitution).
"""
from pathlib import Path
import itertools, math, json, hashlib, datetime
from fractions import Fraction
import numpy as np

OUT=Path(__file__).parent
rng=np.random.default_rng(15102026)
TABLES={
 1:{(1,):{(1,):1}},
 2:{(2,):{(1,1):1,(2,):1},(1,1):{(1,1):1,(2,):-1}},
 3:{(3,):{(1,1,1):1,(2,1):1,(3,):1},(2,1):{(1,1,1):2,(2,1):0,(3,):-1},(1,1,1):{(1,1,1):1,(2,1):-1,(3,):1}},
 4:{(4,):dict(zip([(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)],[1,1,1,1,1])),
    (3,1):dict(zip([(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)],[3,1,-1,0,-1])),
    (2,2):dict(zip([(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)],[2,0,2,-1,0])),
    (2,1,1):dict(zip([(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)],[3,-1,-1,0,1])),
    (1,1,1,1):dict(zip([(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)],[1,-1,1,1,-1]))}}

def cycle(p):
    seen=set(); ls=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; k=0
        while j not in seen: seen.add(j); k+=1; j=p[j]
        ls.append(k)
    return tuple(sorted(ls,reverse=True))

def dims(lam,d):
    hooks=1; content=1
    for i,row in enumerate(lam):
        for j in range(row):
            hooks*=row-j+sum(x>j for x in lam[i+1:])
            content*=d+j-i
    return content//hooks, math.factorial(sum(lam))//hooks

def pmatrix(p,d):
    n=len(p); D=d**n; mat=np.zeros((D,D))
    for j,tup in enumerate(itertools.product(range(d),repeat=n)):
        k=np.ravel_multi_index(tuple(tup[i] for i in p),(d,)*n)
        mat[k,j]=1
    return mat

def jtens(J,d,n):
    X=J
    for _ in range(n-1): X=np.kron(X,J)
    # interleaved O1,I1,...,On,In in rows then columns
    ix=list(range(0,2*n,2))+list(range(1,2*n,2))
    return X.reshape((d,)*(4*n)).transpose(ix+[i+2*n for i in ix]).reshape(d**(2*n),d**(2*n))

def choi(kraus):
    return sum(np.outer(k.reshape(-1),k.reshape(-1).conj()) for k in kraus)

def random_channel(d,k):
    z=rng.normal(size=(d*k,d))+1j*rng.normal(size=(d*k,d))
    q,_=np.linalg.qr(z)
    return [q[i*d:(i+1)*d] for i in range(k)]

records=[]
for d,n in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)]:
    D=d**n; perm=list(itertools.permutations(range(n)))
    mats=[pmatrix(p,d) for p in perm]; ctypes=[cycle(p) for p in perm]
    comm=np.stack([p.reshape(-1) for p in mats],axis=1)
    us,sv,_=np.linalg.svd(comm,full_matrices=False)
    A=us[:,sv>1e-10]
    S=sum(np.kron(p,p) for p in mats)/math.factorial(n)
    blocks={}
    for lam,chars in TABLES[n].items():
        if len(lam)>d: continue
        q,m=dims(lam,d)
        Pi=sum(chars[c]*p for c,p in zip(ctypes,mats))*m/math.factorial(n)
        block=np.kron(Pi,np.eye(D))@S
        blocks[lam]=(q,m,Pi,block)
    M0=sum(m/q*bl for q,m,pi,bl in blocks.values())
    nullvec=np.eye(D).reshape(-1)
    # Compute M0 independently: one-sided collective twirl of identity Choi.
    pure=np.outer(nullvec,nullvec)
    real=pure.reshape(D,D,D,D).transpose(0,2,1,3).reshape(D*D,D*D)
    m0check=(A@(A.T@real)).reshape(D,D,D,D).transpose(0,2,1,3).reshape(D*D,D*D)
    m0err=float(np.linalg.norm(M0-m0check))
    channels=[('unitary',choi(random_channel(d,1))),('depolarizing',np.eye(d*d)/d),
              ('replacement',np.kron(np.diag([1]+[0]*(d-1)),np.eye(d))),
              ('random_rank_d',choi(random_channel(d,d))),('random_full_rank',choi(random_channel(d,d*d)))]
    if d==2:
        g=.37
        channels.append(('amplitude_damping',choi([np.diag([1,np.sqrt(1-g)]),np.array([[0,np.sqrt(g)],[0,0]])])))
    for name,J in channels:
        X=jtens(J,d,n)
        real=X.reshape(D,D,D,D).transpose(0,2,1,3).reshape(D*D,D*D)
        B=(A@(A.T@real@A)@A.T).reshape(D,D,D,D).transpose(0,2,1,3).reshape(D*D,D*D)
        vals={str(lam):float(np.trace(bl@X).real/(q*m)) for lam,(q,m,pi,bl) in blocks.items()}
        b=min(vals.values()); residual=0; normalization=0; feasibility=0
        for lam,(q,m,pi,bl) in blocks.items():
            residual=max(residual,float(np.linalg.norm(B@bl-(m/q)*vals[str(lam)]*bl)))
            normalization=max(normalization,abs(float(np.trace(bl@M0).real/(q*m))-1))
            feasibility=min(feasibility,float(np.linalg.eigvalsh(np.kron(np.eye(D),pi)-bl)[0]))
        dualmin=float(np.linalg.eigvalsh((B+B.conj().T)/2-b*M0)[0])
        two_error=None
        if n==2:
            E_I=np.einsum('aibi->ab',J.reshape(d,d,d,d))
            s=float(np.trace(E_I@E_I).real); p=float(np.trace(J@J).real)
            formula=(d*d-d-s+p)/(2*d*(d-1))
            two_error=abs(formula-b)
        rec=dict(d=d,n=n,channel=name,commutant_dimension=A.shape[1],b_values=vals,
            null_twirl_error=m0err,block_residual=residual,null_normalization_error=normalization,
            min_tester_feasibility_eigenvalue=feasibility,min_dual_eigenvalue=dualmin,two_query_error=two_error)
        records.append(rec)
    print('Finished',d,n,flush=True)

def partitions(n,k,cap=None):
    if n==0: yield (); return
    if k==0: return
    cap=min(n,n if cap is None else cap)
    for a in range(cap,0,-1):
        for tail in partitions(n-a,k-1,a): yield (a,)+tail

count=0; comparisons=0; failures=[]
for d in range(2,7):
    for n in range(1,31):
        a,r=divmod(n,d); star=tuple([a+1]*r+[a]*(d-r)); star=tuple(x for x in star if x)
        qs,ms=dims(star,d)
        assert qs==math.comb(d,r)
        for lam in partitions(n,d):
            q,m=dims(lam,d); count+=1
            if q<qs or Fraction(q,m)<Fraction(qs,ms): failures.append([d,n,lam,'dimension'])
            for K in set([1,2,3,max(1,ms//2),ms,ms+1,m,m+1]):
                comparisons+=1
                if Fraction(q,min(K,m))<Fraction(qs,min(K,ms)): failures.append([d,n,lam,K])

report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),seed=15102026,
 method='Independent HS commutant projection for both Haar twirls; independently authored code',
 manuscript_sha256=hashlib.sha256(Path(r'D:\Entregas\airr\2026-10-15_tests-unitarios-optimos\optimal-unitary-tests.pdf').read_bytes()).hexdigest(),
 cases=records,exact_partition_cases=count,exact_finite_reference_comparisons=comparisons,exact_failures=failures,
 summary=dict(channel_cases=len(records),max_block_residual=max(x['block_residual'] for x in records),
 max_null_twirl_error=max(x['null_twirl_error'] for x in records),
 max_null_normalization_error=max(x['null_normalization_error'] for x in records),
 min_dual_eigenvalue=min(x['min_dual_eigenvalue'] for x in records),
 min_tester_feasibility_eigenvalue=min(x['min_tester_feasibility_eigenvalue'] for x in records),
 max_two_query_error=max(x['two_query_error'] or 0 for x in records)))
(OUT/'independent-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))
