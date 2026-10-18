"""Reproducible numerical checks; these checks are not proofs of capacity."""
from pathlib import Path
from datetime import datetime, timezone
import json, math
import numpy as np
from scipy.linalg import block_diag

R = Path(__file__).resolve().parent
rng = np.random.default_rng(18102026)
def entropy(a):
    p = np.linalg.eigvalsh((a+a.conj().T)/2)
    p = p[p>1e-14]
    return float(-np.dot(p, np.log2(p)))
def h(x):
    if x <= 0 or x >= 1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def g(x):
    if x == 0: return 0.0
    return math.log2(x+1)+x*math.log1p(1/x)/math.log(2)
def f(x,d):
    return 2*x*math.log2(d)+(1+x)*h(x/(1+x))
def state(n):
    a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    a=a@a.conj().T
    return a/np.trace(a)
def ptrace_b(a,r,d):
    return np.einsum('ijkj->ik',a.reshape(r,d,r,d))
def ptrace_r(a,r,d):
    return np.einsum('ijil->jl',a.reshape(r,d,r,d))

rows=[]
for case in range(200):
    d=int(rng.integers(2,8)); k=int(rng.integers(1,5)); L=k+d+3
    lam=float(rng.random()); tau=state(L); taup=tau[k:k+d,k:k+d]
    eps=float(np.trace(taup).real); delta=(1-lam)*eps
    reference=int(rng.integers(1,5)); rho=state(reference*d)
    rho_r=ptrace_b(rho,reference,d)
    tau_dec=block_diag(taup,np.array([[1-eps]]))
    erase_dec=np.diag([0.0]*d+[1.0])
    # Embed the input into the transmitted block of R tensor (B+flag).
    rho_emb=np.zeros((reference*(d+1),)*2,dtype=complex)
    ix=np.array([i*(d+1)+j for i in range(reference) for j in range(d)])
    rho_emb[np.ix_(ix,ix)]=rho
    actual=lam*rho_emb+(1-lam)*np.kron(rho_r,tau_dec)
    ideal=lam*rho_emb+(1-lam)*np.kron(rho_r,erase_dec)
    halfnorm=float(np.abs(np.linalg.eigvalsh(actual-ideal)).sum()/2)
    markov=float(np.dot(np.arange(L),np.diag(tau).real)/k-eps)
    p=rng.dirichlet(np.ones(d)); s=float(-np.dot(p,np.log2(p)))
    psi=np.zeros(d*(d+1),complex)
    for i in range(d): psi[i*(d+1)+i]=math.sqrt(p[i])
    pure=np.outer(psi,psi.conj())
    actual=lam*pure+(1-lam)*np.kron(np.diag(p),tau_dec)
    ideal=lam*pure+(1-lam)*np.kron(np.diag(p),erase_dec)
    ia=entropy(ptrace_r(actual,d,d+1))-entropy(actual)
    ie=entropy(ptrace_r(ideal,d,d+1))-entropy(ideal)
    # Number measurement with label X; reset can fall inside the code window.
    transition=np.tile((1-lam)*np.r_[np.diag(taup).real,1-eps],(d,1))
    transition[np.arange(d),np.arange(d)]+=lam
    py=p@transition
    mutual=sum(p[i]*transition[i,j]*math.log2(transition[i,j]/py[j])
               for i in range(d) for j in range(d+1) if transition[i,j]>0)
    rows.append(dict(case=case,d=d,k=k,lam=lam,
        halfnorm_error=abs(halfnorm-delta),markov_margin=markov,
        erasure_ic_error=abs(ie-(2*lam-1)*s),
        continuity_margin=f(delta,d)-abs(ia-ie),
        classical_margin=mutual-lam*s+h(delta)))

asym=[]
for N in [100,1000,10000,100000,1000000,100000000]:
    K=math.ceil(math.sqrt(N)); m=N-K
    logr=-math.log1p(1/m); d=math.ceil(2*(m+1)*math.log(N+1)); t=math.exp(d*logr)
    mean=m-d*t/(1-t)
    s=g(m)+math.log1p(-t)/math.log(2)+d*t/(1-t)*logr/math.log(2)
    delta=0.3*10/K
    asym.append(dict(N=N,K=K,d=d,physical_mean=K+mean,s=s,
        entropy_deficit=g(N)-s,truncation_t=t,
        classical_gap_bound=.7*(g(N)-s)+h(delta),
        quantum_gap_bound=.4*(g(N)-s)+f(delta,d),
        ea_gap_bound=1.4*(g(N)-s)+f(delta,d)))

summary=dict(random_cases=len(rows),
    max_halfnorm_error=max(x['halfnorm_error'] for x in rows),
    max_erasure_ic_error=max(x['erasure_ic_error'] for x in rows),
    min_markov_margin=min(x['markov_margin'] for x in rows),
    min_continuity_margin=min(x['continuity_margin'] for x in rows),
    min_classical_margin=min(x['classical_margin'] for x in rows))
assert summary['max_halfnorm_error']<1e-12
assert summary['max_erasure_ic_error']<1e-12
assert min(summary[k] for k in ['min_markov_margin','min_continuity_margin','min_classical_margin'])>-1e-12
assert all(x['physical_mean'] <= x['N']+1e-10 for x in asym)
assert all(x['truncation_t'] <= (x['N']+1)**-2*(1+1e-10) for x in asym)
result=dict(seed=18102026,generated_at=datetime.now(timezone.utc).isoformat(),
    scope='Numerical checks of finite matrices and input formulas, not proofs or capacity estimates.',
    summary=summary,asymptotics=dict(lam=.7,reset_mean_bound=10,rows=asym),cases=rows)
(R/'verification-1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(summary=summary,asymptotic_bounds=asym)))
