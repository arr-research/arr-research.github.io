"""Finite algebra checks of an UNAUDITED partial-breeding candidate.
Does not test asymptotic source coding, bootstrap, security or capacity.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math,itertools
import numpy as np
R=Path(__file__).resolve().parent;rng=np.random.default_rng(181020263)
def H(p):
    p=np.asarray(p).real;p=p[p>1e-14];return float(-np.dot(p,np.log2(p)))
def S(x):return H(np.linalg.eigvalsh((x+x.conj().T)/2))
def h(x):return H([x,1-x])
def b(lam,delta):return (lam+delta)*h(delta/(lam+delta)) if lam+delta else 0.
def rank2(a):
    a=a.copy();rank=0
    for c in range(a.shape[1]):
        piv=next((r for r in range(rank,len(a)) if a[r,c]),None)
        if piv is None:continue
        a[[rank,piv]]=a[[piv,rank]]
        for r in range(len(a)):
            if r!=rank and a[r,c]:a[r]^=a[rank]
        rank+=1
    return rank
matrices={}
for m in [1,2,3]:
    matrices[m]=[np.array(v,dtype=np.uint8).reshape(m,m) for v in itertools.product([0,1],repeat=m*m) if rank2(np.array(v,dtype=np.uint8).reshape(m,m))==m]
records=[]
for case in range(120):
    d=int(rng.integers(2,9));m=(d-1).bit_length();p=rng.dirichlet(np.ones(d))
    z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));theta=z@z.conj().T;theta/=np.trace(theta)
    lam=float(rng.uniform(.1,.95));delta=float(rng.uniform(0,1-lam));P=lam+delta;q=delta/P
    diag=theta.diagonal().real;s=H(p);kap=float(p@diag)
    v=np.zeros(d*d,complex);ix=np.arange(d)*(d+1);v[ix]=np.sqrt(p);psi=np.outer(v,v.conj())
    om=(lam*psi+delta*np.kron(np.diag(p),theta))/P
    twirl=np.zeros_like(om)
    for k in range(d):
        phase=np.exp(2j*np.pi*k*np.arange(d)/d);joint=np.kron(phase,phase.conj())
        twirl+=(joint[:,None]*om*joint.conj()[None,:])/d
    expected=(lam*psi+delta*np.kron(np.diag(p),np.diag(diag)))/P
    survival=twirl[np.ix_(ix,ix)]*P;P0=lam+delta*kap
    mc=lam*np.outer(np.sqrt(p),np.sqrt(p))+delta*np.diag(p*diag)
    ic=H(np.diag(survival).real/P0)-S(survival/P0)
    mismatch=np.zeros(2**m);mismatch[0]=lam/P
    for j in range(d):
        for k in range(d):mismatch[j^k]+=q*p[j]*diag[k]
    vectors=np.array([[(i>>k)&1 for k in range(m)] for i in range(2**m)],dtype=np.uint8)
    laws=[];costs=[];chain=[]
    for A in matrices[m]:
        out=(vectors@A.T)%2
        label=np.array([next((j+1 for j,x in enumerate(vv) if x),0) for vv in out])
        law=np.bincount(label,weights=mismatch,minlength=m+1);laws.append(law);costs.append(H(law))
        chain.append(sum((law[0]+sum(law[j:]))*h(law[j]/(law[0]+sum(law[j:]))) for j in range(1,m+1)))
    e=q*(1-kap);theory=np.r_[1-e,[e*2**(m-j)/(2**m-1) for j in range(1,m+1)]]
    A=matrices[m][int(np.argmin(costs))];bit=(vectors@A[0])%2
    parity=np.array([bit[j]^bit[k] for j in range(d) for k in range(d)])
    # Actual ancilla amplitudes after the two controlled X operations.
    kraus=[]
    for aout,bout in itertools.product([0,1],repeat=2):
        diagonal=[]
        for j in range(d):
            for k in range(d):
                amp=sum(1/math.sqrt(2) for vbit in [0,1] if (vbit^int(bit[j]))==aout and (vbit^int(bit[k]))==bout)
                diagonal.append(amp)
        kraus.append((aout^bout,np.array(diagonal)))
    kraus_error=max(np.max(abs(k-(parity==y)/math.sqrt(2))) for y,k in kraus)
    preserved=sum(k[:,None]*psi*k[None,:] for y,k in kraus)
    row=dict(case=case,d=d,lambda_survival=lam,delta=delta,kappa=kap,
        twirl_error=float(np.max(abs(twirl-expected))),
        survivor_error=float(np.max(abs(survival-mc))),
        hashing_margin=float(P0*ic-lam*s+b(lam,delta*kap)),
        gl_average_law_error=float(np.max(abs(np.mean(laws,axis=0)-theory))),
        entropy_average_margin=float(H(theory)-np.mean(costs)),
        good_matrix_margin=float(h(e)+2*e-min(costs)),
        prefix_chain_error=float(max(abs(x-y) for x,y in zip(costs,chain))),
        kraus_error=float(kraus_error),good_state_preservation_error=float(np.max(abs(preserved-psi))))
    records.append(row)
errors=['twirl_error','survivor_error','gl_average_law_error','prefix_chain_error','kraus_error','good_state_preservation_error']
margins=['hashing_margin','entropy_average_margin','good_matrix_margin']
summary={k:max(r[k] for r in records) for k in errors}
summary.update({k:min(r[k] for r in records) for k in margins})
assert max(summary[k] for k in errors)<2e-11
assert min(summary[k] for k in margins)>-2e-11
result=dict(created_at=datetime.now(timezone.utc).isoformat(),seed=181020263,cases=records,summary=summary,
    GL_counts={str(m):len(aa) for m,aa in matrices.items()},
    scope='Finite algebra diagnostics only: no operational/asymptotic proof, no new grade or manuscript acceptance.')
(R/'mismatch-verification-1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(summary=summary,GL_counts=result['GL_counts'])))
