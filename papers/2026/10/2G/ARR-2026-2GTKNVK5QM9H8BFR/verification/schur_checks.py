"""Reproducible checks of the orbit-testing conjecture. Not a proof assistant."""
from pathlib import Path
import itertools, math, json, time
from fractions import Fraction
from functools import reduce
import numpy as np
import scipy.linalg as la
ROOT=Path(__file__).parent
rng=np.random.default_rng(20261015)
def kron(xs): return reduce(np.kron,xs)
def parts(n, d, cap=None):
    if d==0:
        if n==0: yield ()
        return
    if cap is None:cap=n
    for k in range(min(n,cap),-1,-1):
        for t in parts(n-k,d-1,k):yield (k,)+t
def dims(lam):
    d=len(lam);n=sum(lam)
    q=Fraction(1)
    for i in range(d):
        for j in range(i+1,d):q*=Fraction(lam[i]-lam[j]+j-i,j-i)
    m=q*math.factorial(n)*math.prod(math.factorial(j) for j in range(d))
    m/=math.prod(math.factorial(lam[i]+d-i-1) for i in range(d))
    assert q.denominator==m.denominator==1
    return int(q),int(m)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);k+=1;j=p[j]
        out.append(k)
    return out
def char(lam,cyc):
    d=len(lam);poly={(0,)*d:1}
    for k in cyc:
        new={}
        for x,v in poly.items():
            for i in range(d):
                y=list(x);y[i]+=k;y=tuple(y);new[y]=new.get(y,0)+v
        poly=new
    target=[lam[i]+d-i-1 for i in range(d)]
    return sum(sign(p)*poly.get(tuple(target[i]-(d-p[i]-1) for i in range(d)),0) for p in itertools.permutations(range(d)))
def perm_matrix(d,p):
    n=len(p);a=np.arange(d**n).reshape((d,)*n).transpose(p).ravel()
    return np.eye(d**n)[a]
def projectors(d,n):
    perms=list(itertools.permutations(range(n)));ps=[perm_matrix(d,p) for p in perms]
    S=sum(np.kron(p,p) for p in ps)/math.factorial(n)
    out=[]
    for lam in parts(n,d):
        q,m=dims(lam)
        P=sum(char(lam,cycles(p))*a for p,a in zip(perms,ps))*m/math.factorial(n)
        D=np.kron(P,np.eye(d**n))@S
        assert la.norm(D@D-D)<1e-10 and la.norm(D-D.T)<1e-10
        assert abs(np.trace(D)-q*q)<1e-10
        out.append((lam,q,m,D))
    assert la.norm(sum(x[3] for x in out)-S)<1e-10
    return out
def random_channel(d,k=None):
    k=k or d*d
    z=rng.normal(size=(d*k,d))+1j*rng.normal(size=(d*k,d))
    v=la.qr(z,mode='economic')[0]
    return [v[i*d:(i+1)*d,:] for i in range(k)]
def choi(ks):return sum(np.outer(k.ravel(),k.ravel().conj()) for k in ks)
def product_choi(J,d,n):
    a=kron([J]*n).reshape([d]*(4*n))
    order=list(range(0,2*n,2))+list(range(1,2*n,2))
    return a.transpose(order+[i+2*n for i in order]).reshape(d**(2*n),d**(2*n))
def cliffords():
    H=np.array([[1,1],[1,-1]])/np.sqrt(2);S=np.diag([1,1j]);out=[np.eye(2,dtype=complex)];seen=set()
    def key(u):
        v=u.ravel();w=v[np.where(abs(v)>1e-8)[0][0]];u=u*np.conj(w)/abs(w)
        return tuple(np.round(np.r_[u.real.ravel(),u.imag.ravel()],8))
    seen.add(key(out[0]))
    for a in out:
        for g in [H,S]:
            b=g@a;k=key(b)
            if k not in seen:seen.add(k);out.append(b)
    assert len(out)==24
    return out
CLIFF=cliffords()
def twirl(A,n):
    N=2**n
    for side in [0,1]:
        B=np.zeros_like(A,dtype=complex)
        for u in CLIFF:
            v=kron([u]*n);v=np.kron(v,np.eye(N)) if side==0 else np.kron(np.eye(N),v)
            B+=v@A@v.conj().T
        A=B/24
    return A
def run():
    start=time.time();records=[];sdp_cases=[];worst={'block_error':0.,'psd_violation':0.,'two_use_formula_error':0.}
    for d,n in [(2,1),(2,2),(2,3),(2,4),(3,2)]:
        projs=projectors(d,n);M=sum(m/q*D for _,q,m,D in projs)
        channels=[('identity',[np.eye(d)]),('depolarizing',[np.outer(np.eye(d)[i],np.eye(d)[j])/np.sqrt(d) for i in range(d) for j in range(d)]),('pure_replacer',[np.outer(np.eye(d)[0],np.eye(d)[j]) for j in range(d)])]
        channels += [(f'random-{j}',random_channel(d)) for j in range(12)]
        if d==2:
            for g in [.1,.5,.9]:channels.append((f'amplitude-{g}',[np.diag([1,np.sqrt(1-g)]),np.array([[0,np.sqrt(g)],[0,0]])]))
            channels.append(('dephasing',[np.diag([1,0]),np.diag([0,1])]))
        for name,ks in channels:
            J=choi(ks);A=product_choi(J,d,n)
            bs=[float(np.trace(D@A).real/(q*m)) for _,q,m,D in projs];b=min(bs)
            assert -1e-10<=b<=1+1e-10
            row=dict(d=d,n=n,channel=name,sectors=[list(x[0]) for x in projs],failure=bs,optimal=min(range(len(bs)),key=bs.__getitem__))
            if n==2:
                s=np.trace(sum(k@k.conj().T for k in ks)@sum(k@k.conj().T for k in ks)).real
                p=np.trace(J@J).real
                formula=(d*d-d-s+p)/(2*d*(d-1))
                err=abs(b-formula);worst['two_use_formula_error']=max(worst['two_use_formula_error'],err);assert err<1e-10
            if d==2 and n<=3:
                B=twirl(A,n)
                berr=max(la.norm(B@D-(np.trace(D@A).real/(q*q))*D) for _,q,m,D in projs)
                ev=float(la.eigvalsh(B-b*M)[0]);worst['block_error']=max(worst['block_error'],berr);worst['psd_violation']=max(worst['psd_violation'],-ev)
                assert berr<1e-9 and ev>-1e-9
                row.update(block_error=berr,min_dual_eigenvalue=ev)
                if n==2 and name in ['depolarizing','amplitude-0.5','random-0','pure_replacer']:
                    sdp_cases.append((name,B,M,b))
            records.append(row)
        print('matrix checks',d,n,flush=True)
    # Test the unrestricted two-query causal SDP, in O2,I2,O1,I1 order.
    import cvxpy as cp
    sdps=[]
    def reorder(a):return a.reshape([2]*8).transpose([1,3,0,2,5,7,4,6]).reshape(16,16)
    for name,B,M,b in sdp_cases:
        B=reorder(B);M=reorder(M)
        for alpha in [0.,.2,.6]:
            T=cp.Variable((16,16),hermitian=True);Xi=cp.Variable((8,8),hermitian=True);rho=cp.Variable((2,2),hermitian=True)
            cons=[T>>0,Xi>>0,rho>>0,cp.kron(np.eye(2),Xi)-T>>0,cp.partial_trace(Xi,[2,2,2],axis=0)==cp.kron(np.eye(2),rho),cp.trace(rho)==1,cp.real(cp.trace(T@M))>=1-alpha]
            prob=cp.Problem(cp.Minimize(cp.real(cp.trace(T@B))),cons)
            prob.solve(solver='CLARABEL',tol_gap_abs=1e-8,tol_feas=1e-8,tol_gap_rel=1e-8,max_iter=200)
            expected=(1-alpha)*b;err=abs(prob.value-expected)
            assert prob.status in ['optimal','optimal_inaccurate'] and err<2e-6,(name,alpha,prob.value,expected,prob.status)
            sdps.append(dict(channel=name,alpha=alpha,status=prob.status,value=prob.value,expected=expected,error=err))
        print('SDP checks',name,flush=True)
    # Exact rational balanced-partition dominance, including finite reference.
    partition_count=0;parameter_cases=0
    for d in range(2,8):
        for n in range(1,25):
            q,r=divmod(n,d);bal=(q+1,)*r+(q,)*(d-r);qb,mb=dims(bal)
            assert qb==math.comb(d,r)
            for lam in parts(n,d):
                ql,ml=dims(lam);partition_count+=1
                assert ql>=qb and Fraction(ql,ml)>=Fraction(qb,mb)
                for K in {1,2,3,mb,max(1,mb-1),mb+1,2*mb}:
                    parameter_cases+=1
                    assert Fraction(ql,min(K,ml))>=Fraction(qb,min(K,mb))
    report=dict(seed=20261015,matrix_cases=len(records),worst_errors=worst,sector_checks=records,causal_sdp=sdps,exact_partition_checks=partition_count,exact_reference_checks=parameter_cases,seconds=time.time()-start,scope='Numerical and exact finite checks, not an independent peer review or a proof-assistant formalization.')
    (ROOT/'verification-minimax.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['sector_checks','causal_sdp']}),flush=True)
if __name__=='__main__':run()
