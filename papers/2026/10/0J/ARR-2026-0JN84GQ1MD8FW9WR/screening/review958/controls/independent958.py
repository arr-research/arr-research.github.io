"""Independent bounded checks for exact sharp957 PDF. Samples are not proofs."""
from pathlib import Path
import json, platform, sys, hashlib
from datetime import datetime, timezone
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.integrate import quad_vec
import mpmath as mp

OUT=Path(__file__).parent
rng=np.random.default_rng(958)
failures=[]
def check(ok, label, **data):
    if not ok: failures.append(dict(label=label, **data))
def pure(n):
    z=rng.normal(size=n)+1j*rng.normal(size=n)
    return z/np.linalg.norm(z)
def dm(n, rank=None):
    z=rng.normal(size=(n,rank or n))+1j*rng.normal(size=(n,rank or n))
    a=z@z.conj().T
    return a/np.trace(a)
def marginal(rho,d,r):
    v=rho.reshape(d,r,d,r)
    return np.trace(v,axis1=1,axis2=3),np.trace(v,axis1=0,axis2=2)
def ent(a):
    vals=np.linalg.eigvalsh((a+a.conj().T)/2)
    check(min(vals)>-1e-11,'negative_state',minimum=float(min(vals)))
    vals=vals[vals>0]
    return -float(sum(vals*np.log(vals)))
def mi(rho,d,r):
    a,b=marginal(rho,d,r)
    return ent(a)+ent(b)-ent(rho)
def trial(rho,d,r,tau,l,label):
    a,b=marginal(rho,d,r)
    out=l*rho+(1-l)*np.kron(tau,b)
    ii=mi(rho,d,r); oo=mi(out,d,r)
    spec,vec=np.linalg.eigh(b)
    inv=(vec*(1/np.sqrt(spec)))@vec.conj().T
    white=np.kron(np.eye(d),inv)@rho@np.kron(np.eye(d),inv)
    k=float(np.linalg.eigvalsh(white)[-1])
    small=max(0,float(np.linalg.eigvalsh(tau)[0]))
    bound=l*l/(l+(1-l)*small)
    kb=l*l*k/(l*k+(1-l)*small)
    redmin=float(np.linalg.eigvalsh(np.kron(np.eye(d),b)-rho)[0])
    q=oo/ii
    check(q<=kb+1e-10,'kappa_violation',q=q,bound=kb,label_case=label)
    if redmin>=-1e-12:check(q<=bound+1e-10,'reduction_violation',q=q,bound=bound,label_case=label)
    return dict(label=label,d=d,r=r,lambda_=l,a=small,Iin=ii,Iout=oo,ratio=q,
                sep_bound=bound,kappa=k,kappa_bound=kb,reduction_min=redmin)

rows=[]
for d in [2,3,4]:
  for r in [2,3]:
    for i in range(30):
      p=rng.dirichlet(np.ones(6));rho=np.zeros((d*r,d*r),complex)
      for w in p:
        a=pure(d);b=pure(r);z=np.kron(a,b);rho+=w*np.outer(z,z.conj())
      for mode,tau in [('identity',np.eye(d)/d),('pure',dm(d,1)),('mixed',dm(d)),('singular',dm(d,d-1))]:
        l=[.03,.25,.5,.9][i%4]
        rows.append(trial(rho,d,r,tau,l,f'sep-{mode}-{i}'))

special=[]
for d in [3,4]:
    flip=np.zeros((d*d,d*d))
    for i in range(d):
      for j in range(d):flip[i*d+j,j*d+i]=1
    rho=(np.eye(d*d)-flip)/(d*(d-1))
    pt=rho.reshape(d,d,d,d).transpose(2,1,0,3).reshape(d*d,d*d)
    for l in [.1,.5,.9]:
      rec=trial(rho,d,d,np.eye(d)/d,l,'NPT-antisymmetric-reduction')
      rec['partial_transpose_min']=float(np.linalg.eigvalsh(pt)[0]);special.append(rec)

e=np.eye(3);s=np.ones(3)/np.sqrt(3)
upb=[np.kron(e[0],(e[0]-e[1])/np.sqrt(2)),np.kron((e[0]-e[1])/np.sqrt(2),e[2]),
     np.kron(e[2],(e[1]-e[2])/np.sqrt(2)),np.kron((e[1]-e[2])/np.sqrt(2),e[0]),np.kron(s,s)]
rho=(np.eye(9)-sum(np.outer(z,z) for z in upb))/4
pt=rho.reshape(3,3,3,3).transpose(2,1,0,3).reshape(9,9)
check(min(np.linalg.eigvalsh(pt))>-1e-12,'tiles_PPT_failed')
for l in [.1,.5,.9]:
    rec=trial(rho,3,3,dm(3),l,'PPT-tiles');special.append(rec)

general=[]
for d,r in [(2,3),(3,2),(3,4),(4,4)]:
  for i in range(20):
    rho=dm(d*r)
    general.append(trial(rho,d,r,dm(d),.5,f'general-{i}'))

def g(base,x):
    w,u=np.linalg.eigh(base);z=u.conj().T@x@u
    ell=np.empty((len(w),len(w)))
    for i,a in enumerate(w):
      for j,b in enumerate(w):ell[i,j]=1/a if abs(a-b)<1e-12*max(a,b) else np.log(a/b)/(a-b)
    return float(np.sum(abs(z)**2*ell))
metric=[]
for i in range(100):
    v=dm(5)+.02*np.eye(5);c=.2+2*rng.random();w=c*v+dm(5)
    z=dm(5)-dm(5);ratio=c*g(w,z)/g(v,z)
    check(ratio<=1+1e-12,'BKM_order',ratio=ratio);metric.append(ratio)

finite=[]
for l,a,b in [('0.1','0','1'),('0.5','0','0'),('0.4','0.01','0.99'),('0.7','0.2','0.3'),('0.5','0.5','0.5')]:
  for n in [3,5,10,20,50]:
    mp.mp.dps=int(2*n*n*mp.log10(2))+150
    lm,am,bm=map(mp.mpf,[l,a,b]);x=1/mp.mpf(n);r=mp.power(2,-n*n);ep=r/n**2
    def blockD(c,d,z):
      disc=mp.sqrt((c-d)**2+4*z*z);large=(c+d+disc)/2;small=(c*d-z*z)/large
      return large*mp.log(large)+small*mp.log(small)-c*mp.log(c)-d*mp.log(d)
    ai=(1-x)*(1-r);bi=x*r;u=lm*(1-x)+(1-lm)*am;v=lm*x+(1-lm)*bm
    din=blockD(ai,bi,ep);dout=blockD(u*(1-r),v*r,lm*ep)
    ell=lambda c,d:mp.log(c/d)/(c-d)
    gm=lm**2*ell(u*(1-r),v*r)/ell(ai,bi)
    q=dout/din;target=lm**2/(lm+(1-lm)*am)
    lower=mp.mpf(n-1)/(n+1)*gm;upper=mp.mpf(n+1)/(n-1)*gm
    check(lower<q<upper and q<=target,'finite_family',n=n,lambda_=l,a=a,b=b)
    finite.append(dict(n=n,lambda_=l,a=a,b=b,ratio=mp.nstr(q,30),target=mp.nstr(target,30),
        input_MI=mp.nstr(din,30),lower=mp.nstr(lower,30),upper=mp.nstr(upper,30),
        separable_filter_t=mp.nstr(ep/mp.sqrt(x*(1-x)*r*(1-r)),12)))

continuous=[]
for d in [2,3,4,5]:
  for mode in ['cyclic','missing','degenerate']:
    z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));Q,_=np.linalg.qr(z)
    energies=np.arange(d,dtype=float)
    if mode=='degenerate':energies[1]=energies[0]
    H=(Q*energies)@Q.conj().T;v=np.ones(d)/np.sqrt(d)
    if mode=='missing':v[1]=0;v/=np.linalg.norm(v)
    psi=Q@v;tau=np.outer(psi,psi.conj());gamma=.73;t=1.31;lam=np.exp(-gamma*t)
    def integrand(u):
      v=expm(-1j*u*H)@psi
      return gamma*np.exp(-gamma*u)*np.outer(v,v.conj())
    S,err=quad_vec(integrand,0,t,epsabs=1e-12,epsrel=1e-12)
    U=expm(-1j*t*H);ident=np.eye(d)
    gen=-1j*(np.kron(ident,H)-np.kron(H.T,ident))+gamma*(tau.reshape(-1,order='F')[:,None]@ident.reshape(-1,order='F')[None,:]-np.eye(d*d))
    direct=expm(t*gen)
    predicted=lam*np.kron(U.conj(),U)+S.reshape(-1,order='F')[:,None]@ident.reshape(-1,order='F')[None,:]
    residual=float(np.max(abs(direct-predicted)))
    rank_expected=d if mode=='cyclic' else d-1
    rank_observed=int(np.sum(np.linalg.eigvalsh(S)>1e-10))
    check(residual<1e-11 and rank_expected==rank_observed,'continuous',d=d,mode=mode,residual=residual,ranks=[rank_expected,rank_observed])
    continuous.append(dict(d=d,mode=mode,residual=residual,integration_error=float(err),
        expected_rank=rank_expected,observed_rank=rank_observed,smallest_eigenvalue=float(np.linalg.eigvalsh(S)[0])))

gap16=F(17,1004000)-F(2,126875)
d=128;l=F(1,d**3);a=F(1,d)
lower=l*l*(d*d-1)/(20*(1+(d*d-1)*l));c6=l*l*6/(l*6+(1-l)*a);gap128=lower-c6
check(gap16==F(1191,1019060000),'rational_gap16')
check(gap128==F(1906309377,185976497736620441600),'rational_gap128')
mp.mp.dps=100
asymptotic=[]
for d in [16,128,1024,8192]:
    d=mp.mpf(d);l=d**-3;h=d*d-1
    info=(1+h*l)/(d*d)*mp.log1p(h*l)+h*(1-l)/(d*d)*mp.log1p(-l)
    q=info/(2*mp.log(d));sep=d*l*l/(1+(d-1)*l)
    asymptotic.append(dict(d=int(d),Iout=mp.nstr(info,18),Iout_scaled=mp.nstr(info*2*d**4,18),
        advantage=mp.nstr(q/sep,18),advantage_scaled=mp.nstr(q/sep*4*mp.log(d)/d,18)))

out=dict(timestamp=datetime.now(timezone.utc).isoformat(),seed=958,python=sys.version,
    libraries=dict(numpy=np.__version__,scipy=scipy.__version__,mpmath=mp.__version__),
    scope='Bounded floating/high-precision/exact diagnostics, not universal certificates',
    random_separable=rows,special_reduction_and_PPT=special,general_kappa=general,
    BKM_order=metric,general_finite_sequence=finite,continuous_quadrature_vs_generator=continuous,
    rational_gaps=dict(d16=str(gap16),d128=str(gap128)),asymptotic=asymptotic,failures=failures)
(OUT/'INDEPENDENT958.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
summary=dict(separable_cases=len(rows),special_cases=len(special),general_kappa=len(general),
    BKM_cases=len(metric),finite_sequence_cases=len(finite),continuous_cases=len(continuous),
    maximum_continuous_residual=max(x['residual'] for x in continuous),
    maximum_separable_ratio_fraction=max(x['ratio']/x['sep_bound'] for x in rows),
    failures=failures)
print(json.dumps(summary))
