"""Block and entropy diagnostics for dossiers7/8, not operational-rate verification."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import json,numpy as np
rng=np.random.default_rng(181020267)
def ent(x):
    p=np.linalg.eigvalsh((x+x.conj().T)/2).real;p=p[p>1e-13]
    return float(-np.dot(p,np.log2(p)))
def h(x):return 0. if x<=0 or x>=1 else float(-x*np.log2(x)-(1-x)*np.log2(1-x))
def density(n,rank):
    z=rng.normal(size=(n,rank))+1j*rng.normal(size=(n,rank));a=z@z.conj().T
    return a/np.trace(a)
rows=[]
def check(rho,d,label):
    eq=np.arange(d)*(d+1);B=rho[np.ix_(eq,eq)];w=float(np.trace(B).real)
    w=float(np.clip(w,0,1));q=1-w
    u=ent(np.diag(np.diag(B/w)))-ent(B/w) if w>1e-14 else 0.
    v=w*u;c=0.
    for i in range(d):
        for j in range(i+1,d):
            inds=[i*d+j,j*d+i];b=rho[np.ix_(inds,inds)];p=float(np.trace(b).real)
            if p>1e-14:c+=p*(ent(np.diag(np.diag(b/p)))-ent(b/p))
    C=ent(np.diag(np.diag(rho)))-ent(rho)
    tw=np.diag(np.diag(rho)).astype(complex);tw[np.ix_(eq,eq)]=B
    tw_error=0.
    if d<=4:
        exact=np.zeros_like(rho)
        for a in product(range(3),repeat=d):
            phases=np.exp(2j*np.pi*np.array(a)/3);z=np.kron(phases,phases.conj())
            exact+=z[:,None]*rho*z.conj()[None,:]
        exact/=3**d;tw_error=float(np.max(np.abs(exact-tw)))
    lower=max(0.,v-h(w)-2*q);upper=v+c
    X=np.trace(tw.reshape(d,d,d,d),axis1=1,axis2=3)
    reduction_min=float(np.linalg.eigvalsh(np.kron(X,np.eye(d))-tw).min())
    row={'label':label,'d':d,'w':w,'u':u,'v':v,'swap_coherence':float(c),
         'full_dephasing_entropy':C,'entropy_identity_error':abs(C-v-c),
         'twirl_max_error':tw_error,'twirl_entropy_identity_error':abs(ent(np.diag(np.diag(tw)))-ent(tw)-v),
         'analytic_lower':lower,'analytic_upper':upper,'interval_width':upper-lower,
         'ldoi_log9_margin':np.log2(9)-(upper-lower),'cldui_log5_margin':np.log2(5)-(v-lower),
         'reduction_min_eigenvalue_after_twirl':reduction_min}
    assert abs(C-v-c)<1e-10 and tw_error<1e-10,row
    assert -1e-10<=c<=q+1e-10 and upper+1e-10>=lower,row
    assert row['ldoi_log9_margin']>-1e-10 and row['cldui_log5_margin']>-1e-10,row
    if lower>1e-8:assert reduction_min<0,row
    rows.append(row)
for i in range(240):
    d=int(rng.integers(2,9));eq=np.arange(d)*(d+1);rho=np.zeros((d*d,d*d),complex)
    w=float(rng.uniform(.001,.999));B=w*density(d,1 if i%2 else int(rng.integers(1,d+1)))
    rho[np.ix_(eq,eq)]=B;pairs=[(j,k) for j in range(d) for k in range(j+1,d)]
    weights=(1-w)*rng.dirichlet(np.ones(len(pairs)))
    for (j,k),weight in zip(pairs,weights):
        inds=[j*d+k,k*d+j];rho[np.ix_(inds,inds)]=weight*density(2,1 if i%4 else 2)
    check(rho,d,'random_'+str(i))
for d in [2,3,4,8]:
    eq=np.arange(d)*(d+1);phi=np.zeros((d*d,d*d),complex);phi[np.ix_(eq,eq)]=np.ones((d,d))/d
    check(phi,d,'pure_maximally_entangled')
    for a in [.1,.4,.8,.99]:check(a*phi+(1-a)*np.eye(d*d)/(d*d),d,'isotropic_mix_'+str(a))
    swap=np.zeros_like(phi)
    for j in range(d):
        for k in range(d):swap[j*d+k,k*d+j]=1
    check((np.eye(d*d)-swap)/(d*(d-1)),d,'antisymmetric_werner_control')
summary={'cases':len(rows),'random_cases':240,'explicit_controls':len(rows)-240,
         'positive_lower_cases':sum(x['analytic_lower']>1e-8 for x in rows),
         'full_phase_averages':sum(x['d']<=4 for x in rows),
         'max_entropy_identity_error':max(x['entropy_identity_error'] for x in rows),
         'max_twirl_error':max(x['twirl_max_error'] for x in rows),
         'max_twirl_entropy_identity_error':max(x['twirl_entropy_identity_error'] for x in rows),
         'min_log9_margin':min(x['ldoi_log9_margin'] for x in rows),
         'min_log5_margin':min(x['cldui_log5_margin'] for x in rows)}
out={'created_at':datetime.now(timezone.utc).isoformat(),'seed':181020267,'scope':__doc__,'summary':summary,'cases':rows}
Path(__file__).with_name('diagonal-invariant-verification-5.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(summary))
