"""Offline algebra checks for the six-capacity minimax application.
This does not prove coding/privacy or certify novelty. Run in a copied folder.
Requires numpy and sympy. No network access or source downloads.
"""
from pathlib import Path
import json,datetime
import numpy as np
import sympy as sp
rng=np.random.default_rng(180026)
def h(x):
    if x<=0 or x>=1:return 0.
    return -x*np.log2(x)-(1-x)*np.log2(1-x)
def entropy(a):
    ev=np.linalg.eigvalsh((a+a.conj().T)/2);ev=ev[ev>1e-14]
    return -sum(ev*np.log2(ev))
errors={k:0. for k in ['tp','f_overlap','extremal_choi','postprocess','isotropic_block','width_identity','classical_formula']}
records=[]
for d in [2,3,4,5,7,10]:
    phi=np.eye(d).reshape(-1)/np.sqrt(d);P=np.outer(phi,phi)
    Id=np.eye(d*d)
    J0=(Id-P)/(d*d-1)
    assert np.linalg.eigvalsh(J0).min()>-1e-13
    errors['tp']=max(errors['tp'],np.linalg.norm(np.einsum('iaja->ij',J0.reshape(d,d,d,d))-np.eye(d)/d))
    # Independent Kraus construction of the noise from nonidentity Weyl operators.
    z=np.diag(np.exp(2j*np.pi*np.arange(d)/d));x=np.roll(np.eye(d),1,axis=0)
    JW=np.zeros_like(Id,dtype=complex)
    for a in range(d):
        for b in range(d):
            if a==0 and b==0:continue
            W=np.linalg.matrix_power(x,a)@np.linalg.matrix_power(z,b)
            v=W.T.reshape(-1)/np.sqrt(d)
            JW+=np.outer(v,v.conj())/(d*d-1)
    errors['extremal_choi']=max(errors['extremal_choi'],np.linalg.norm(JW-J0))
    for lam in sorted(set([0.,1/d**2,1/d,.25,.5,.8,.99,1.])):
        if lam<1/d**2:
            JM=(Id/d**2-lam*P)/(1-lam)
            assert np.linalg.eigvalsh(JM).min()>-1e-13
            assert np.linalg.norm(lam*P+(1-lam)*JM-Id/d**2)<1e-13
            records.append(dict(d=d,lam=lam,zero_regime=True));continue
        q=1-lam;p=(d*d*lam-1)/(d*d-1)
        J=lam*P+q*J0
        errors['f_overlap']=max(errors['f_overlap'],abs(phi@J@phi-lam))
        for k in range(8):
            Z=rng.normal(size=(d*d,d*d))+1j*rng.normal(size=(d*d,d*d))
            X=Z@Z.conj().T;X/=np.trace(X)
            fm=float(np.real(phi@X@phi));f=lam+q*fm;pf=(d*d*f-1)/(d*d-1)
            if pf>1e-14:
                a=p/pf
                errors['postprocess']=max(errors['postprocess'],abs(a*pf-p))
                assert -1e-13<=a<=1+1e-13
        ix=np.arange(d)*(d+1);B=J[np.ix_(ix,ix)];w=float(np.trace(B));t=q/(d+1)
        direct_v=w*(np.log2(d)-entropy(B/w))
        formula_v=w*np.log2(d)-w*h(lam/w)-t*np.log2(d-1)
        errors['isotropic_block']=max(errors['isotropic_block'],abs(direct_v-formula_v))
        raw=formula_v-h(w)-2*(1-w)
        U=np.log2(d)-h(lam)-q*np.log2(d-1)
        Ad=2*d/(d+1)+np.log2(d+1)-d/(d+1)*np.log2(d-1)
        errors['width_identity']=max(errors['width_identity'],abs(U-raw-q*Ad))
        if lam>=1/d:assert max(0,raw)<=U+1e-12
        a=(d*lam+1)/(d+1)
        vals=np.r_[p+(1-p)/d,np.repeat((1-p)/d,d-1)]
        C=np.log2(d)+sum(v*np.log2(v) for v in vals if v>0)
        errors['classical_formula']=max(errors['classical_formula'],abs(C-(np.log2(d)-h(a)-(1-a)*np.log2(d-1))))
        records.append(dict(d=d,lam=lam,w=w,v=direct_v,lower=max(0,raw),isotropic_ER=U if lam>1/d else 0.,width_formula=q*Ad))

# Exact rational Choi spectra, normalization and extremal mixture coefficients.
exact=[]
for d in range(2,15):
    for lam in [sp.Rational(0),sp.Rational(1,d*d),sp.Rational(1,d),sp.Rational(2,3),sp.Rational(1)]:
        if lam<sp.Rational(1,d*d):
            e0=(sp.Rational(1,d*d)-lam)/(1-lam);e1=sp.Rational(1,d*d)/(1-lam)
            assert e0>=0 and e1>=0 and e0+(d*d-1)*e1==1
        else:
            p=(d*d*lam-1)/(d*d-1)
            assert p+(1-p)/d**2==lam
            assert (1-p)/d**2==(1-lam)/(d*d-1)
            assert p+(1-p)/d==(d*lam+1)/(d+1)
        exact.append([d,str(lam)])
assert max(errors.values())<1e-10,errors
result=dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Algebraic matrix/formula checks only; not a proof of capacities, twirl security, novelty, or seed derandomization.',errors=errors,exact_cases=exact,numeric_cases=records)
target=Path(__file__).with_name('minimax-verification-6.json')
assert not target.exists(), 'Refusing to overwrite a verification record; run in a fresh copy.'
target.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(dict(errors=errors,exact_cases=len(exact),numeric_cases=len(records)),indent=2))
