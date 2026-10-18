from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, math
import numpy as np
from scipy.optimize import minimize_scalar
import mpmath as mp

ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(2026101811)
def entropy(p):
    p=np.asarray(p,dtype=float)
    p=p[p>1e-16]
    return float(-np.dot(p,np.log2(p)))
def S(a): return entropy(np.linalg.eigvalsh((a+a.conj().T)/2))
def h(x): return entropy([x,1-x])
def F(lam,x):
    q=1-lam;a=lam+q*x
    disc=max(0,a*a-4*lam*q*x*(1-x))
    mus=[(a+math.sqrt(disc))/2,(a-math.sqrt(disc))/2,q*(1-x)]
    return h(x)+h(lam*(1-x))-entropy(mus)
def e(lam,x): return 2*lam*h(x)-F(lam,x)
def c(lam,x):
    q=1-lam
    return (q+lam*x)*h(q/(q+lam*x))-x*h(lam)
def mi_reset(rho,lam):
    d=rho.shape[0]
    val,vec=np.linalg.eigh(rho)
    sq=(vec*np.sqrt(np.maximum(val,0)))@vec.conj().T
    psi=sq.reshape(-1)
    tau=np.zeros((d,d));tau[0,0]=1
    # Row-major vec(sqrt(rho)) has reference marginal rho and
    # channel-input marginal rho.T. The formulas below use that convention.
    joint=lam*np.outer(psi,psi.conj())+(1-lam)*np.kron(rho,tau)
    out=lam*rho.T+(1-lam)*tau
    return S(rho)+S(out)-S(joint)

# Direct joint-state eigenvalue check for diagonal inputs.
diag_res=[];phase_margins=[]
for d in range(2,10):
    for _ in range(25):
        p=rng.dirichlet(np.ones(d));lam=rng.uniform(.02,.98)
        x=p[0];sr=entropy(p[1:]/(1-x))
        diag_res.append(abs(mi_reset(np.diag(p),lam)-(2*lam*(1-x)*sr+F(lam,x))))
        z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        rho=z@z.conj().T;rho/=np.trace(rho)
        phase_margins.append(mi_reset(np.diag(np.diag(rho)),lam)-mi_reset(rho,lam))
assert max(diag_res)<1e-11
assert min(phase_margins)>-1e-11

strict=[]
for lam in [.01,.1,.25,.5,.75,.9,.99]:
    for x in np.linspace(.001,.999,401):
        strict.append((e(lam,x),c(lam,x),e(lam,x)-c(lam,x)))
assert min(t[0] for t in strict)>0
assert min(t[1] for t in strict)>0
assert min(t[2] for t in strict)>-1e-11

# Compare the two variational forms, then solve the explicit plateau
# independently at 80 decimal digits. These are diagnostics, not proofs
# that no other extrema occur; the dossier uses a compact minimum.
variational=[]
for lam in [.1,.25,.5,.75,.9]:
    for zp in [.01,.1,1,10,100]:
        pc=1/(1+zp)
        def bernD(x):
            return -h(x)-x*math.log2(pc)-(1-x)*math.log2(1-pc)
        left=lambda x:2*lam*math.log2(1+zp)-(2*lam*(1-x)*math.log2(zp)+F(lam,x))
        right=lambda x:2*lam*bernD(x)+e(lam,x)
        residual=max(abs(left(x)-right(x)) for x in np.linspace(0,1,101))
        fit=minimize_scalar(left,bounds=(1e-12,1-1e-12),method='bounded',options={'xatol':1e-13})
        gap=min(left(0),left(1),fit.fun)
        assert gap>0 and residual<2e-11
        variational.append(dict(lam=lam,Z_plus=zp,x=float(fit.x),gap=float(gap),identity_residual=residual))

mp.mp.dps=80
def hm(x):
    return -sum(t*mp.log(t,2) for t in [x,1-x] if t>0)
def Fm(lam,x):
    q=1-lam;a=lam+q*x
    disc=mp.sqrt(a*a-4*lam*q*x*(1-x))
    p=[(a+disc)/2,(a-disc)/2,q*(1-x)]
    return hm(x)+hm(lam*(1-x))+sum(t*mp.log(t,2) for t in p if t>0)
plateau=[]
for ls in ['0.1','0.25','0.5','0.75','0.9']:
    lam=mp.mpf(ls)
    guess=next(t['x'] for t in variational if t['lam']==float(lam) and t['Z_plus']==1)
    x=mp.findroot(lambda t:mp.diff(lambda u:Fm(lam,u),t),(mp.mpf(guess)-mp.mpf('.005'),mp.mpf(guess)+mp.mpf('.005')))
    val=2*lam-Fm(lam,x)
    plateau.append(dict(lam=ls,x=mp.nstr(x,60),gap=mp.nstr(val,60),stationary_residual=mp.nstr(abs(mp.diff(lambda u:Fm(lam,u),x)),5)))

# Exact critical moments for the explicit shell spectrum use geometric
# identities sum 2^-n=1, sum n 2^-n=2, sum n^2 2^-n=6.
# Construct finite-support, disjoint high-shell mixtures at fixed mean
# energy. All dimensions enter as log2 dimension, never allocated.
shell=[]
L=35
for include_ground,Ec in [(True,4),(False,8)]:
    ns=np.arange(1,L+1,dtype=float)
    probs=np.exp2(-ns)
    energies=ns*ns+ns
    logs=ns*ns
    if include_ground:
        probs=np.r_[1.,probs];energies=np.r_[0.,energies];logs=np.r_[0.,logs]
    probs/=sum(probs)
    eb=float(np.dot(probs,energies));sb=entropy(probs)+float(np.dot(probs,logs))
    for E in [Ec+1,Ec+8,Ec+40]:
        losses=[]
        for m in [50,100,200,500,1000,5000,20000]:
            em=m*m+m;p=(E-eb)/(em-eb)
            ent=h(p)+(1-p)*sb+p*m*m
            mean=(1-p)*eb+p*em
            gap=E+(1 if include_ground else 0)-ent
            assert abs(mean-E)<1e-10 and gap>-1e-10
            losses.append(dict(shell=m,mean_energy=mean,entropy=ent,gap=gap))
        assert losses[-1]['gap']<losses[0]['gap']
        shell.append(dict(include_ground=include_ground,E=E,base_cutoff=L,rows=losses))

def bosonic(E): return (E+1)*math.log2(E+1)-E*math.log2(E) if E else 0.
divergent=[]
for m in [1,3,10]:
    divergent.append(dict(removed_shells=m,rows=[dict(E=E,gap=bosonic(E)-bosonic(E-m)) for E in [20,100,1000,10000,1000000]]))
out=dict(created_at=datetime.now(timezone.utc).isoformat(),seed=2026101811,
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    direct_diagonal_cases=len(diag_res),diagonal_max_error=max(diag_res),
    complex_phase_cases=len(phase_margins),minimum_phase_gain=min(phase_margins),
    strict_deficit_cases=len(strict),minimum_e_minus_c=min(t[2] for t in strict),
    variational=variational,plateau_80_digits=plateau,
    explicit_critical_spectrum=dict(beta_c=1,Z_c=2,Z_plus=1,critical_mean_all=4,critical_mean_excited=8),
    finite_shell_constructions=shell,divergent_partition_example=divergent,
    scope='Numerical diagnostics and explicit finite-support constructions only; not a proof of coding, infinite-dimensional converses, novelty, or global optimum.')
(ROOT/'spectral-checks-11.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['direct_diagonal_cases','diagonal_max_error','complex_phase_cases','minimum_phase_gain','strict_deficit_cases','minimum_e_minus_c','plateau_80_digits']},indent=2))
