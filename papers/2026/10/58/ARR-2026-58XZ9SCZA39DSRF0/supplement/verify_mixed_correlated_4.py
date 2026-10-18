"""Finite diagnostics only; asymptotic coding and cited theorems are not simulated."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
rng=np.random.default_rng(181020266)
def ent(x):
    v=np.linalg.eigvalsh((x+x.conj().T)/2).real
    v=v[v>1e-13]
    return float(-np.dot(v,np.log2(v)))
def h(x):return 0. if x<=0 or x>=1 else float(-x*np.log2(x)-(1-x)*np.log2(1-x))
def b(a,c):return (a+c)*h(c/(a+c)) if a+c else 0.
def dens(d,r):
    z=rng.normal(size=(d,r))+1j*rng.normal(size=(d,r));v=z@z.conj().T
    return v/np.trace(v)
rows=[]
for i in range(480):
    d=int(rng.integers(2,10));s=d if i%3 else int(rng.integers(1,d+1))
    t=np.zeros((d,d),complex);t[:s,:s]=dens(s,1 if i%2 else int(rng.integers(1,s+1)))
    if i%5==0:t=.93*t+.07*np.diag(np.diag(t))
    theta=np.zeros((d*d,d*d),complex);eq=np.arange(d)*(d+1)
    theta[np.ix_(eq,eq)]=t
    inds=np.array([j*d+k for j in range(s) for k in range(d)])
    chi=np.zeros_like(theta);chi[np.ix_(inds,inds)]=dens(len(inds),int(rng.integers(1,len(inds)+1)))
    a=float(rng.uniform(.05,.999));rho=a*theta+(1-a)*chi
    X=np.trace(rho.reshape(d,d,d,d),axis1=1,axis2=3);sig=np.diag(np.diag(t))
    u=ent(sig)-ent(t)
    vals,vecs=np.linalg.eigh(X[:s,:s]);assert min(vals)>0
    logX=(vecs*np.log2(vals))@vecs.conj().T
    D=-ent(sig)-float(np.trace(sig[:s,:s]@logX).real)
    red=np.kron(X,np.eye(d))-rho
    redmin=float(np.linalg.eigvalsh(red[np.ix_(inds,inds)]).min())
    seed=bool(a*2**u>1+1e-9)
    L=float(a*u-h(a)-(1-a)*np.log2(5))
    kap=float(np.trace(chi[np.ix_(eq,eq)]).real);P0=a+(1-a)*kap
    survivor=(a*t+(1-a)*chi[np.ix_(eq,eq)])/P0
    yield_margin=P0*(ent(np.diag(np.diag(survivor)))-ent(survivor))-a*u+b(a,(1-a)*kap)
    row={'case':i,'d':d,'alice_support':s,'rank_good':int(np.linalg.matrix_rank(t,tol=1e-10)),
         'a':a,'coherent_information_good':u,'seed_condition':seed,'net_bound':L,
         'reduction_min_eigenvalue':redmin,'relative_entropy_marginals':D,
         'survivor_yield_margin':yield_margin,'log_condition':float(np.log2(a)+u),
         'log_condition_with_relative_entropy':float(np.log2(a)+u+D)}
    assert u>-1e-10 and D>-1e-10 and yield_margin>-1e-10,row
    if seed:assert redmin<-1e-10,row
    if L>1e-9:assert seed,row
    rows.append(row)
summary={'cases':len(rows),'mixed_good_cases':sum(x['rank_good']>1 for x in rows),
         'singular_alice_marginal_cases':sum(x['alice_support']<x['d'] for x in rows),
         'positive_net_cases':sum(x['net_bound']>1e-9 for x in rows),
         'sufficient_seed_cases':sum(x['seed_condition'] for x in rows),
         'min_relative_entropy_marginals':min(x['relative_entropy_marginals'] for x in rows),
         'min_survivor_yield_margin':min(x['survivor_yield_margin'] for x in rows)}
out={'created_at':datetime.now(timezone.utc).isoformat(),'seed':181020266,
     'scope':__doc__,'summary':summary,'cases':rows}
Path(__file__).with_name('mixed-correlated-verification-4.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(summary))
