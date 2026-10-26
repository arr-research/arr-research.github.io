"""Finite state and Gaussian algebra diagnostics; not a coding/priority proof."""
import numpy as np,mpmath as mp,json
from pathlib import Path
rng=np.random.default_rng(64120261026)
def state(d):
    a=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    x=a@a.conj().T;return x/np.trace(x)
def ent(x):
    e=np.linalg.eigvalsh((x+x.conj().T)/2);e=e[e>1e-14]
    return float(-np.sum(e*np.log2(e)))
def partials(x,dr,db):
    y=x.reshape(dr,db,dr,db)
    return np.einsum("ibjb->ij",y),np.einsum("iaib->ab",y)
def infos(x,dr,db,u):
    rr,bb=partials(x,dr,db)
    y=(np.kron(u,np.eye(db))@x@np.kron(u.conj().T,np.eye(db))).reshape(dr,db,dr,db)
    conditional=0.
    for j in range(dr):
        z=y[j,:,j,:];p=float(np.trace(z).real)
        if p>1e-14:conditional+=p*ent(z/p)
    return ent(rr)+ent(bb)-ent(x),ent(bb)-conditional
rows=[]
for dr in [2,3,4]:
 for db in [2,3,5]:
  for j in range(12):
    w=state(dr*db)
    if j==0:
        a=np.zeros(dr*db,complex)
        for i in range(min(dr,db)):a[i*db+i]=1/np.sqrt(min(dr,db))
        w=np.outer(a,a.conj())
    rr,bb=partials(w,dr,db)
    if j==1:w=np.kron(rr,bb);rr,bb=partials(w,dr,db)
    u,_=np.linalg.qr(rng.normal(size=(dr,dr))+1j*rng.normal(size=(dr,dr)))
    i,jj=infos(w,dr,db,u)
    for la in [.01,.1,.5,.9,.99]:
        tau=state(db);z=la*w+(1-la)*np.kron(rr,tau)
        iz,jz=infos(z,dr,db,u)
        ds=i-jj;dz=iz-jz;slack=la*ds-dz
        assert ds>=-2e-12 and dz>=-2e-12 and slack>=-2e-12
        rows.append(dict(dr=dr,db=db,lambda_=la,Delta_signal=ds,Delta_mix=dz,slack=slack))
mp.mp.dps=110
ln2=mp.log(2)
def g(x):return ((x+1)*mp.log1p(1/x)+mp.log(x))/ln2
gauss=[]
for kk in ["0.001","0.1","0.5","0.9","0.999999"]:
 k=mp.mpf(kk);de=1-k
 for ee in ["0.1","1","10","1e3","1e6"]:
  E=mp.mpf(ee)
  for nn in ["1e-6",".01","1","100","1e6","1e12"]:
    n=mp.mpf(nn);t=de*n;A=de*(E+n)+1;V=de*E+(1+k)*n+1
    D=mp.sqrt(V*V-4*k*n*(n+1))
    ul=(D+de*(E-n)-1)/2;us=(D-de*(E-n)-1)/2
    product=de*E*n*(1-2*k/(D+A))
    assert abs(ul*us-product)<=mp.mpf("1e-80")*max(1,product)
    gap=g(E)+g(t)-g(ul)-g(us)
    bound=mp.log1p(1/t)/ln2+(1/E+1/t)/(2*ln2)
    assert gap>=-mp.mpf("1e-80") and gap<=bound+mp.mpf("1e-80")
    gauss.append(dict(k=kk,E=ee,n=nn,gap=mp.nstr(gap,25),bound=mp.nstr(bound,25)))
out=dict(seed=64120261026,finite_states=len(rows),Gaussian_cases=len(gauss),all_passed=True,
 min_finite_slack=min(x["slack"] for x in rows),rows=rows,Gaussian=gauss,
 scope="Finite noncommuting measurements and explicit Gaussian identities only, not infinite limits, common codes or novelty")
Path(__file__).with_name("checks641.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k not in ["rows","Gaussian"]}))
