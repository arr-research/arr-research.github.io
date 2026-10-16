"""Checks of normalization and finite witnesses for the noise law; no author code imported."""
from pathlib import Path
import json, datetime
import numpy as np

root=Path(__file__).resolve().parent
rng=np.random.default_rng(2026101605)
records=[]
for d,r in [(2,1),(3,1),(3,2),(5,2),(5,4)]:
    lam=np.zeros(d); lam[:r]=1/r
    ks=[]
    for a in range(r):
        for b in range(d):
            k=np.zeros((d,d),complex); k[a,b]=np.sqrt(lam[a]); ks.append(k)
    for m in [1,2,3]:
        n=d*m; q=r*m; theta=(d-r)/d; p=r/d
        y=rng.normal(size=(len(ks),m,m))+1j*rng.normal(size=(len(ks),m,m))
        y*=np.sqrt(m/np.vdot(y,y).real)
        aa=sum(np.kron(k,z) for k,z in zip(ks,y))
        u,s,vh=np.linalg.svd(aa)
        assert np.sum(s>1e-10)==q
        v0=u[:,q:]@vh[q:,:]
        bb=v0/(d*np.sqrt(theta))
        noise_energy=d*np.vdot(bb,bb).real/m
        assert abs(noise_energy-1)<1e-12
        slopes=[]
        for eps in [1e-2,1e-4,1e-6]:
            h=np.sqrt((1-eps)*p)*aa+np.sqrt(eps*theta)*bb
            val=np.exp(2*np.linalg.slogdet(h)[1]/n)
            formula=((1-eps)*p)**p*np.prod(s[:q]**2)**(1/n)*(eps/d**2)**theta
            assert abs(val/formula-1)<1e-9
            sharp_constant=((1/r)/r)**(r/d)*(1/(d*(d-r)))**theta
            assert val <= sharp_constant*eps**theta+1e-12
            # Exact replacer value, also attained by a finite matrix witness.
            eig=(1-eps)*lam+eps/d
            exact=np.prod(eig)**(1/d)/d
            hopt=np.kron(np.diag(np.sqrt(eig)),np.eye(m))/np.sqrt(d)
            computed=np.exp(2*np.linalg.slogdet(hopt)[1]/n)
            assert abs(computed/exact-1)<1e-12
            assert val <= exact+1e-12
            slopes.append({'eps':eps,'witness_value':float(val),'exact_replacer':float(exact)})
        records.append({'d':d,'rank':r,'m':m,'theta':theta,'noise_energy':float(noise_energy),'values':slopes})

# Independent random feasible tuple checks of the uniform head/tail bound.
count=0; tail_max_ratio=0.
for d,r,m in [(3,1,2),(3,2,3),(5,2,2),(5,4,3)]:
    ks=[]
    for a in range(r):
        for b in range(d):
            k=np.zeros((d,d),complex); k[a,b]=1/np.sqrt(r); ks.append(k)
    for _ in range(20):
        eps=10**rng.uniform(-7,-0.30103)
        y=rng.normal(size=(len(ks),m,m))+1j*rng.normal(size=(len(ks),m,m))
        z=rng.normal(size=(d,d,m,m))+1j*rng.normal(size=(d,d,m,m))
        factor=np.sqrt(m/(np.vdot(y,y).real+np.vdot(z,z).real))
        y*=factor; z*=factor
        aa=sum(np.kron(k,b) for k,b in zip(ks,y))
        bb=z.transpose(0,2,1,3).reshape(d*m,d*m)/np.sqrt(d)
        h=np.sqrt(1-eps)*aa+np.sqrt(eps)*bb
        s=np.linalg.svd(h,compute_uv=False)
        tail=np.sum(s[r*m:]**2)
        rhs=eps*np.vdot(bb,bb).real
        tail_max_ratio=max(tail_max_ratio,float(tail/rhs))
        assert tail<=rhs+1e-12
        assert np.vdot(h,h).real<=m/r+1e-12
        theta=(d-r)/d
        bound=((1/r)/r)**(r/d)*(1/(d*(d-r)))**theta*eps**theta
        val=np.exp(2*np.linalg.slogdet(h)[1]/(d*m))
        assert val<=bound+1e-12
        count+=1

out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'passed':True,'svd_completion_examples':len(records),'random_feasible_cases':count,
     'largest_tail_to_Eckart_Young_bound_ratio':tail_max_ratio,'examples':records,
     'scope':'Finite identity/normalization checks; uniform theorem is proved separately.'}
(root/'noise-law-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='examples'},indent=2))
