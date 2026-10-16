from pathlib import Path
import itertools,json
import numpy as np
import scipy.linalg as la
from verify_minimax import projectors,random_channel,choi,product_choi,kron,rng
R=Path(__file__).parent
def unitary(d):return la.qr(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))[0]
def protocol(n,lam,K=None):
    _,q,m,D=next(x for x in projectors(2,n) if x[0]==lam)
    # Trace over input legs recovers q/m times the physical isotypic projector.
    N=2**n;P=np.trace(D.reshape(N,N,N,N),axis1=1,axis2=3)*m/q
    if q==1:
        ev,vec=la.eigh(P);W=vec[:,ev>.5]
    elif n==3 and lam==(2,1):
        ids=[i for i in range(N) if i.bit_count()==1]
        ev,vec=la.eigh(P[np.ix_(ids,ids)]);up=np.zeros((N,m));up[ids,:]=vec[:,ev>.5]
        lowering=sum(kron([np.array([[0,0],[1,0]]) if j==i else np.eye(2) for j in range(n)]) for i in range(n))
        W=np.column_stack([up,lowering@up])
    else:raise ValueError((n,lam))
    assert la.norm(W.conj().T@W-np.eye(q*m))<1e-10
    K=min(m,K or m);vecs=[]
    for v in range(q):
        z=sum(np.kron(W[:,v*m+a],np.eye(K)[a]) for a in range(K))/np.sqrt(K);vecs.append(z)
    F=sum(np.outer(z,z.conj()) for z in vecs);rho=F/q
    return rho,F,D,q,m,K
rows=[]
for n,lam,K in [(3,(2,1),2),(4,(2,2),1),(4,(2,2),2)]:
    rho,F,D,q,m,K=protocol(n,lam,K)
    channels=[('depolarizing',[np.outer(np.eye(2)[i],np.eye(2)[j])/np.sqrt(2) for i in range(2) for j in range(2)])]
    channels += [(f'random-{i}',random_channel(2)) for i in range(4)]
    for name,ks in channels:
        J=choi(ks);formula=np.trace(D@product_choi(J,2,n)).real/(q*m)
        for trial in range(5):
            L=unitary(2);U=unitary(2);V=unitary(2)
            full=np.kron(kron([U]*n),np.eye(K));null=np.trace(F@full@rho@full.conj().T).real
            assert abs(null-1)<1e-10
            oriented=[L@a@V for a in ks];out=np.zeros_like(rho,dtype=complex)
            for seq in itertools.product(oriented,repeat=n):
                A=np.kron(kron(seq),np.eye(K));out+=A@rho@A.conj().T
            prob=np.trace(F@out).real
            if K==m:assert abs(prob-formula)<1e-10
            if name=='depolarizing':assert abs(prob-q/(2**n*K))<1e-10
            rows.append(dict(n=n,lambda_=lam,K=K,channel=name,trial=trial,null_acceptance=float(null),alternative_acceptance=float(prob),full_reference_formula=float(formula)))
(R/'verification-physical.json').write_text(json.dumps(dict(seed=20261015,cases=len(rows),results=rows),indent=2)+'\n')
print('Direct circuit checks passed:',len(rows))
