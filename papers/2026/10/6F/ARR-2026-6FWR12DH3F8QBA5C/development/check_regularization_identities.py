"""Independent normalization and finite-matrix checks. No author scripts imported."""
from pathlib import Path
import json, datetime
import numpy as np

rng=np.random.default_rng(1610202603)
root=Path(__file__).resolve().parent
def choi(k):
    return sum(np.outer(a.ravel(),a.ravel().conj()) for a in k)
def detroot(h):
    return float(np.exp(2*np.linalg.slogdet(h)[1]/len(h)))
errs=[]; count=0
for d,m,k in [(2,2,3),(3,2,4),(3,3,3)]:
    for _ in range(15):
        v=rng.normal(size=(k*d,d))+1j*rng.normal(size=(k*d,d))
        v=np.linalg.qr(v)[0]; ks=v.reshape(k,d,d)
        y=rng.normal(size=(k,m,m))+1j*rng.normal(size=(k,m,m))
        y*=np.sqrt(m/np.vdot(y,y).real)
        h=sum(np.kron(a,b) for a,b in zip(ks,y))
        w,s,z=np.linalg.svd(h); u=w@z
        blocks=u.reshape(d,m,d,m)
        fu=[blocks[:,a,:,b]/np.sqrt(m) for a in range(m) for b in range(m)]
        inner=np.trace(choi(ks)@choi(fu)).real/(d*d)
        contractions=np.einsum('irs,rasb->iab',ks.conj(),blocks)
        dual=sum(np.vdot(c,c).real for c in contractions)/(m*d*d)
        errs.append(abs(inner-dual))
        assert detroot(h)<=(s.mean())**2+1e-12
        assert (s.mean())**2<=inner+1e-12
        assert inner<=np.linalg.eigvalsh(choi(ks))[-1]/d+1e-12
        # Check Jensen covariance upper bound at a random det-one X.
        q=np.einsum('iab,jab->ij',y.conj(),y)/m
        b=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        x=b@b.conj().T+np.eye(d); x/=np.linalg.det(x).real**(1/d)
        tq=sum(q[i,j]*ks[i].conj().T@x@ks[j] for i in range(k) for j in range(k))
        assert detroot(h)<=np.linalg.det(tq).real**(1/d)+1e-11
        count+=1

pinching=[]
for m in [1,2,3,5]:
    p=np.diag([1,1,0]); q=np.diag([0,0,1])
    h=np.kron(p,np.eye(m)*np.sqrt(2/3))+np.kron(q,np.eye(m)/np.sqrt(3))
    assert abs(detroot(h)-2**(2/3)/3)<1e-12
    pinching.append({'m':m,'a':detroot(h)})

# Haagerup-Musat's Clifford construction gives a skew-block unitary for d=5,m=4.
i2=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1])
cliff=[np.kron(sz,i2),np.kron(sx,i2),np.kron(sy,sx),np.kron(sy,sy),np.kron(sy,sz)]
alpha=np.exp(2j*np.pi/3); beta=alpha.conjugate()
sigma=np.array([[0,alpha,beta,beta,alpha],[alpha,0,alpha,beta,beta],
 [beta,alpha,0,alpha,beta],[beta,beta,alpha,0,alpha],[alpha,beta,beta,alpha,0]])/2
u5=np.block([[sigma[i,j]*cliff[i]@cliff[j] for j in range(5)] for i in range(5)])
assert np.linalg.norm(u5.conj().T@u5-np.eye(20))<1e-12
assert np.linalg.norm(u5+u5.reshape(5,4,5,4).transpose(2,1,0,3).reshape(20,20))<1e-12
assert abs(detroot(u5/np.sqrt(10))-0.1)<1e-12

out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'random_cptp_cases':count,'max_choi_duality_identity_error':max(errs),
 'covariance_jensen_inequalities_passed':True,'pinching_examples':pinching,
 'W5_Haagerup_Musat_clifford_unitary_error':float(np.linalg.norm(u5.conj().T@u5-np.eye(20))),
 'W5_a4_exact':'1/10','passed':True}
(root/'regularization-identity-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
