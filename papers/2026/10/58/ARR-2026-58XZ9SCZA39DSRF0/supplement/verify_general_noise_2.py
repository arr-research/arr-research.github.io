"""Finite algebra diagnostics, not a proof of operational achievability."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import numpy as np

rng=np.random.default_rng(181020264)
def entropy(x):
    v=np.linalg.eigvalsh((x+x.conj().T)/2).real
    v=v[v>1e-14]
    return float(-np.sum(v*np.log2(v)))
def h(x):
    return 0.0 if x<=0 or x>=1 else float(-x*np.log2(x)-(1-x)*np.log2(1-x))
def b(l,x): return (l+x)*h(x/(l+x)) if l+x>0 else 0.0
def density(d):
    g=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    a=g@g.conj().T
    return a/np.trace(a)
def ptrace(x,d,side):
    return np.trace(x.reshape(d,d,d,d),axis1=1 if side=='A' else 0,axis2=3 if side=='A' else 2)
rows=[]
for i in range(240):
    d=2+i%4; p=rng.dirichlet(np.ones(d)); sig=np.diag(p); root=np.diag(np.sqrt(p))
    v=np.zeros(d*d,complex); v[np.arange(d)*(d+1)]=np.sqrt(p); psi=np.outer(v,v.conj())
    l=float(rng.uniform(.1,.98)); delta=float(rng.uniform(.00001,1-l)); P=l+delta
    if i%2==0:
        chi=density(d*d); noise_kind='arbitrary'
    else:
        z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); u,_=np.linalg.qr(z)
        chi=sum(np.kron(root@np.outer(u[:,k].conj(),u[:,k])@root,density(d)) for k in range(d))
        noise_kind='separable_matching_marginal'
    eq=np.arange(d)*(d+1); block=chi[np.ix_(eq,eq)]; kap=float(np.trace(block).real)
    twirl=np.diag(np.diag(chi)).astype(complex); twirl[np.ix_(eq,eq)]=block
    exact=np.zeros_like(chi)
    for a in product(range(3),repeat=d):
        phase=np.exp(2j*np.pi*np.array(a)/3); w=np.kron(phase,phase.conj())
        exact+=w[:,None]*chi*w.conj()[None,:]
    exact/=3**d
    noise_mc=block/kap; s=entropy(sig); P0=l+delta*kap
    survivor=(l*np.outer(np.sqrt(p),np.sqrt(p))+delta*block)/P0
    ic_surv=entropy(np.diag(np.diag(survivor)))-entropy(survivor)
    loss1=b(l,delta*kap)+P*h(delta*(1-kap)/P)+2*delta*(1-kap)
    loss2=b(l,delta)+delta*(h(kap)+2*(1-kap))
    acc=(l*psi+delta*chi)/P
    seed_lb=l*s-delta*entropy(ptrace(chi,d,'A'))-b(l,delta)
    row={'case':i,'dimension':d,'kind':noise_kind,
         'phase_twirl_error':float(np.max(np.abs(exact-twirl))),
         'mc_noise_coherent_information':entropy(np.diag(np.diag(noise_mc)))-entropy(noise_mc),
         'survivor_lower_bound_margin':P0*ic_surv-l*s+b(l,delta*kap),
         'seed_lower_bound_margin':P*(entropy(ptrace(acc,d,'B'))-entropy(acc))-seed_lb,
         'loss_identity_error':abs(loss1-loss2),
         'log5_upper_margin':b(l,delta)+delta*np.log2(5)-loss1}
    if i%2: row['matching_marginal_error']=float(np.max(np.abs(ptrace(chi,d,'A')-sig)))
    rows.append(row)
max_keys=['phase_twirl_error','loss_identity_error','matching_marginal_error']
min_keys=['mc_noise_coherent_information','survivor_lower_bound_margin','seed_lower_bound_margin','log5_upper_margin']
summary={k:max(r[k] for r in rows if k in r) for k in max_keys}
summary.update({k:min(r[k] for r in rows) for k in min_keys})
assert all(summary[k]<1e-10 for k in max_keys),summary
assert all(summary[k]>-1e-10 for k in min_keys),summary
out={'created_at':datetime.now(timezone.utc).isoformat(),'seed':181020264,'number_of_cases':len(rows),
     'scope':'Finite algebra only; no simulation of asymptotic coding, seed bootstrapping, security, or capacities.',
     'summary':summary,'cases':rows}
path=Path(__file__).with_name('general-noise-verification-2.json')
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'path':str(path),'number_of_cases':len(rows),'summary':summary}))
