from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
rng=np.random.default_rng(181020265)
def entropy(p):
    p=p[p>0];return float(-np.dot(p,np.log2(p)))
def h(x):return 0. if x in (0.,1.) else float(-x*np.log2(x)-(1-x)*np.log2(1-x))
def density(d,rank):
    z=rng.normal(size=(d,rank))+1j*rng.normal(size=(d,rank));x=z@z.conj().T
    return x/np.trace(x)
rows=[]
for i in range(1000):
    d=int(rng.integers(2,13));r=int(rng.integers(1,d+1))
    p=np.r_[rng.dirichlet(np.full(r, .5 if i%3 else 2.)),np.zeros(d-r)]
    a=float(rng.uniform(.001,1.));chi=density(d*d,int(rng.integers(1,d*d+1)))
    v=np.zeros(d*d,complex);v[np.arange(d)*(d+1)]=np.sqrt(p);psi=np.outer(v,v.conj())
    rho=a*psi+(1-a)*chi;X=np.einsum('ijkj->ik',rho.reshape(d,d,d,d))
    Xinv=np.linalg.inv(X);t=float(np.trace(np.diag(p)@Xinv).real);s=entropy(p)
    w=np.kron(Xinv,np.eye(d))@v
    ev=float(np.vdot(w,(np.kron(X,np.eye(d))-rho)@w).real)
    rank1=float(np.vdot(w,(np.kron(X,np.eye(d))-a*psi)@w).real)
    L=float(a*s-h(a)-(1-a)*np.log2(5))
    row={'case':i,'d':d,'r':r,'a':a,'L':L,'t':t,'entropy':s,
         'trace_sqrt_bound_margin':t-float(np.sum(np.sqrt(p))**2),
         'entropy_bound_margin':t-2**s,
         'rank_one_identity_relative_error':abs(rank1-(t-a*t*t))/max(1,abs(rank1)),
         'reduction_expectation':ev,'rank_one_expectation':rank1,
         'seed_condition':a*2**s>1}
    if L>0:assert row['seed_condition'] and ev<0,row
    if row['seed_condition']:assert ev<0,row
    assert row['trace_sqrt_bound_margin']>-1e-9,row
    assert row['entropy_bound_margin']>-1e-9,row
    assert ev<=rank1+1e-8*max(1,abs(rank1)),row
    rows.append(row)
summary={'cases':len(rows),'positive_L_cases':sum(r['L']>0 for r in rows),'sufficient_seed_cases':sum(r['seed_condition'] for r in rows),
         'min_trace_sqrt_margin':min(r['trace_sqrt_bound_margin'] for r in rows),'min_entropy_margin':min(r['entropy_bound_margin'] for r in rows),
         'max_relative_rank_one_error':max(r['rank_one_identity_relative_error'] for r in rows)}
out={'created_at':datetime.now(timezone.utc).isoformat(),'seed':181020265,'scope':'Finite algebra diagnostics for the reduction-criterion seed. Does not verify the cited operational distillation theorem or novelty.','summary':summary,'cases':rows}
path=Path(__file__).with_name('reduction-seed-verification-3.json');path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(summary))
