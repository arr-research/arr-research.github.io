"""Diagnostics for hidden-branch, reverse-hashing and entropy-tail bounds.

This is a reproducible finite-matrix check, not a proof or capacity solver.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, math
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(181020262)

def entropy(a):
    v = np.linalg.eigvalsh((a+a.conj().T)/2)
    v = v[v > 1e-14]
    return float(-np.dot(v,np.log2(v)))

def state(d, rank=None):
    z = rng.normal(size=(d,rank or d))+1j*rng.normal(size=(d,rank or d))
    a = z@z.conj().T
    return a/np.trace(a)

def h(x):
    return 0. if x <= 0 or x >= 1 else -x*math.log2(x)-(1-x)*math.log2(1-x)

def marginal_b(a,d,b):
    return np.einsum('ijil->jl',a.reshape(d,b,d,b))

rows=[]
for case in range(500):
    d=int(rng.integers(2,8)); L=d+3
    tau=state(L,1 if case%7==0 else None)
    if case%11==0:
        tau=np.zeros((L,L),complex);tau[-1,-1]=1
    tp=tau[:d,:d]; eps=float(np.trace(tp).real)
    lam=[0.,1.,.5][case] if case<3 else float(rng.random())
    delta=(1-lam)*eps; p=lam+delta; q=delta/p if p else 0.; b=p*h(q)
    sig=state(d,1 if case%13==0 else None)
    e,u=np.linalg.eigh(sig);root=(u*np.sqrt(np.maximum(e,0)))@u.conj().T
    v=root.reshape(-1);v/=np.linalg.norm(v);psi=np.outer(v,v.conj())
    sr=np.einsum('ijkj->ik',psi.reshape(d,d,d,d));s=entropy(sr)
    acc=(lam*psi+(1-lam)*np.kron(sr,tp))/p if p else np.zeros_like(psi)
    dec=np.zeros((d+1,d+1),complex);dec[:d,:d]=tp;dec[-1,-1]=1-eps
    om=(1-lam)*np.kron(sr,dec)
    ix=np.array([i*(d+1)+j for i in range(d) for j in range(d)])
    om[np.ix_(ix,ix)]+=lam*psi
    ic=entropy(marginal_b(om,d,d+1))-entropy(om)
    theta_s=entropy(tp/eps) if eps else 0.
    reverse=p*(s-entropy(acc)) if p else 0.
    forward=p*(entropy(marginal_b(acc,d,d))-entropy(acc)) if p else 0.
    tq=tau[d:,d:];sq=entropy(tq/(1-eps)) if eps<1 else 0.
    # Classical code with the eigenvalue distribution of sigma; number measurement.
    probs=np.maximum(e,0);probs/=sum(probs)
    transition=np.tile((1-lam)*np.r_[np.diag(tp).real,1-eps],(d,1))
    transition[np.arange(d),np.arange(d)]+=lam
    def H(vv):
        vv=vv[vv>1e-14];return float(-np.dot(vv,np.log2(vv)))
    classical=H(probs@transition)-sum(probs[j]*H(transition[j]) for j in range(d))
    rows.append(dict(case=case,d=d,lam=lam,epsilon=eps,b=b,
        coherent_gap=ic-(2*lam-1)*s+b,
        classical_gap=classical-lam*H(probs)+b,
        reverse_hashing_gap=reverse-lam*s+delta*theta_s+b,
        forward_hashing_gap=forward-(lam-delta)*s+b,
        entropy_tail_gap=entropy(tau)-(1-eps)*sq-eps*theta_s,
        binary_comparison_gap=h(delta)-b))
fields=['coherent_gap','classical_gap','reverse_hashing_gap','forward_hashing_gap','entropy_tail_gap','binary_comparison_gap']
summary={k:min(r[k] for r in rows) for k in fields}
assert min(summary.values())>-2e-11,summary

mp.mp.dps=90
def mh(x):
    return mp.mpf(0) if x==0 or x==1 else -x*mp.log(x,2)-(1-x)*mp.log(1-x,2)
def g(x):
    return mp.mpf(0) if x==0 else ((x+1)*mp.log1p(x)-x*mp.log(x))/mp.log(2)
def up6(x):
    return f'{int(mp.ceil(x*10**6))/10**6:.6f}'
table=[]
lam=mp.mpf('0.7');M=mp.mpf(10)
for n in [100,1000,10000,100000,1000000,100000000]:
    N=mp.mpf(n);K=int(mp.ceil(mp.sqrt(N)));m=N-K;r=m/(m+1)
    d=int(mp.ceil(2*(m+1)*mp.log(N+1)));t=r**d
    s=g(m)+mp.log(1-t,2)+d*t/(1-t)*mp.log(r,2);a=g(N)-s
    eps=min(mp.mpf(1),M/K);delta=(1-lam)*eps;p=lam+delta;b=p*mh(delta/p)
    vals=[lam*a+b,(2*lam-1)*a+b,2*lam*a+b,lam*a+delta*g(M/eps)+b]
    table.append(dict(N=n,K=K,d=d,entropy_loss=mp.nstr(a,85),
        exact_bounds=[mp.nstr(x,85) for x in vals],upward_6=[up6(x) for x in vals]))
record=dict(created_at=datetime.now(timezone.utc).isoformat(),seed=181020262,
    cases=rows,summary=summary,analytic_table=table,precision_decimal=90,
    scope='Finite numerical diagnostics and high-precision analytic evaluations, not formal verification or exact capacity calculation.')
(ROOT/'extension-verification-2.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(summary=summary,table=[dict(N=r['N'],upward_6=r['upward_6']) for r in table])))
