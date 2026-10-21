"""Independent finite-dimensional checks; floating-point evidence, not proofs."""
from pathlib import Path
import json, hashlib, platform
import numpy as np
import scipy
from scipy.special import xlogy
from scipy.optimize import linprog, minimize_scalar

OUT=Path(__file__).parent
RNG=np.random.default_rng(20261017417)
checks={}
def add(key,value): checks.setdefault(key,[]).append(float(value))
def entropy(rho):
    eig=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    assert eig.min()>-1e-10
    eig=np.clip(eig,0,1)
    return float(-np.sum(xlogy(eig,eig)))
def h(x): return -xlogy(x,x)-xlogy(1-x,1-x)
def e(q,a,b,l2):
    k=1-a-b
    v=np.clip((a+k*q)*(1-a-k*q)-l2*q*(1-q),0,.25)
    return h((1+np.sqrt(np.maximum(0,1-4*v)))/2)
def r(q): return np.sqrt(np.maximum(0,q*(1-q)))
def ket(q,phase=0): return np.array([np.sqrt(1-q),np.exp(1j*phase)*np.sqrt(q)])
def outer(x): return np.outer(x,x.conj())
def random_ket(n):
    x=RNG.normal(size=n)+1j*RNG.normal(size=n)
    return x/np.linalg.norm(x)
def dilation(a,b,l2):
    den=np.sqrt((1-a)*(1-b))
    t=np.sqrt(l2)/den if den>0 else 0
    assert -1e-14<=t<=1+1e-12
    t=min(1,t)
    u=np.array([1,0,0,0.])
    v=np.array([t,np.sqrt(max(0,1-t*t)),0,0.])
    vp=np.array([0,0,1,0.]); vm=np.array([0,0,0,1.])
    V=np.zeros((2,4,2),complex)
    V[0,:,0]=np.sqrt(1-a)*u; V[1,:,0]=np.sqrt(a)*vp
    V[0,:,1]=np.sqrt(b)*vm; V[1,:,1]=np.sqrt(1-b)*v
    return V
def outputs(V,sigma):
    joint=np.einsum('aei,ij,bfj->aebf',V,sigma,V.conj())
    return np.einsum('aebe->ab',joint),np.einsum('aeaf->ef',joint)
def spectrum(p,a,b,l2):
    w=(1-a)*(1-p)+(1-b)*p
    d=p*(1-p)*((1-a)*(1-b)-l2)
    root=np.sqrt(max(0,w*w-4*d))
    return np.array([a*(1-p),b*p,(w+root)/2,(w-root)/2])
def env_entropy(p,a,b,l2):
    # Vectorized version of the diagonal environment spectrum.
    p=np.asarray(p); w=(1-a)*(1-p)+(1-b)*p
    d=p*(1-p)*((1-a)*(1-b)-l2)
    root=np.sqrt(np.maximum(0,w*w-4*d))
    eig=np.clip(np.array([a*(1-p),b*p,(w+root)/2,(w-root)/2]),0,1)
    return -np.sum(xlogy(eig,eig),axis=0)
def phase_decomposition(p,z):
    if r(p)<1e-15: return [(1.,ket(p))]
    ratio=np.clip(abs(z)/r(p),0,1)
    phase=-np.angle(z) if abs(z)>0 else 0
    return [((1+ratio)/2,ket(p,phase)),((1-ratio)/2,ket(p,phase+np.pi))]
def roof_lp(p,z,a,b,l2,n=1600,extra=()):
    # At the pure-state boundary strict concavity of r forces the point mass.
    # Handle it analytically; HiGHS can report an infeasible nearly degenerate
    # model even when the included q=p column is exactly feasible in real arithmetic.
    if abs(abs(z)-r(p))<1e-13:
        return float(e(p,a,b,l2)),np.array([p]),np.array([1.])
    q=np.unique(np.r_[np.linspace(0,1,n+1),p,extra])
    result=linprog(e(q,a,b,l2),A_ub=-r(q)[None,:],b_ub=[-abs(z)],
      A_eq=np.array([np.ones_like(q),q]),b_eq=[1,p],bounds=(0,None),method='highs',
      options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    assert result.success,result.message
    nz=result.x>1e-8
    return float(result.fun),q[nz],result.x[nz]
def wootters(rho):
    sy=np.array([[0,-1j],[1j,0]])
    flip=np.kron(sy,sy)@rho.conj()@np.kron(sy,sy)
    val,vec=np.linalg.eigh(rho)
    sq=(vec*np.sqrt(np.clip(val,0,None)))@vec.conj().T
    lam=np.sqrt(np.clip(np.linalg.eigvalsh(sq@flip@sq),0,None))
    concurrence=np.clip(lam[-1]-lam[:-1].sum(),0,1)
    return float(h((1+np.sqrt(1-concurrence**2))/2))

fixed=[(.1,.3,.5),(.02,.3,.514624),(.1,.3,.1),(0.,0.,0.),
       (0.,0.,1.),(.3,.7,0.),(1.,0.,0.),(0.,1.,0.)]
for j in range(240):
    if j<len(fixed): a,b,l2=fixed[j]
    else:
        a,b,k=RNG.dirichlet([1,1,1]); l2=k*RNG.random()
    V=dilation(a,b,l2)
    add('isometry_error',np.max(abs(V.reshape(8,2).conj().T@V.reshape(8,2)-np.eye(2))))
    p=RNG.random(); z=r(p)*RNG.random()*np.exp(2j*np.pi*RNG.random())
    sigma=np.array([[1-p,z],[z.conjugate(),p]])
    B,E=outputs(V,sigma)
    expected=np.array([[1-a-(1-a-b)*p,np.sqrt(l2)*z],
       [np.sqrt(l2)*z.conjugate(),a+(1-a-b)*p]])
    add('channel_realization_error',np.max(abs(B-expected)))
    parts=phase_decomposition(p,z)
    reconstructed=sum(w*outer(vec) for w,vec in parts)
    add('constant_population_decomposition_error',np.max(abs(reconstructed-sigma)))
    add('constant_population_cost_error',abs(sum(w*entropy(outputs(V,outer(vec))[0]) for w,vec in parts)-e(p,a,b,l2)))
    diagE=outputs(V,np.diag([1-p,p]))[1]
    add('environment_spectrum_error',np.max(abs(np.sort(np.linalg.eigvalsh(diagE))-np.sort(spectrum(p,a,b,l2)))))
    add('environment_phase_entropy_gap',entropy(diagE)-entropy(E))
    theta=RNG.random()*6
    U=np.diag([1,np.exp(1j*theta)]); W=np.diag([1,1,np.exp(-1j*theta),np.exp(1j*theta)])
    add('environment_covariance_error',np.max(abs(np.kron(U,W)@V.reshape(8,2)-V.reshape(8,2)@U)))
    # Random pure extension on A (2), B' (2), E' (2).
    psi=random_ket(8).reshape(2,2,2)
    p=float(np.sum(abs(psi[1])**2))
    sigma=psi.reshape(2,4)@psi.reshape(2,4).conj().T
    tau=psi.reshape(2,4).T@psi.reshape(2,4).conj()
    full=np.einsum('aei,ijk->aejk',V,psi)
    output_BB=full.transpose(0,2,1,3).reshape(4,8)
    output_EB=full.transpose(1,2,0,3).reshape(8,4)
    SB=entropy(output_BB@output_BB.conj().T)
    SE=entropy(output_EB@output_EB.conj().T)
    branchB=0.; branchE=0.
    for i in range(2):
        branchB+=entropy(psi[i]@psi[i].conj().T/np.vdot(psi[i],psi[i]).real)*np.vdot(psi[i],psi[i]).real
        branchE+=entropy(psi[i].T@psi[i].conj()/np.vdot(psi[i],psi[i]).real)*np.vdot(psi[i],psi[i]).real
    add('original_one_step_gap',SB-e(p,a,b,l2)-branchB)
    add('complement_one_step_gap',SE-e(p,a,b,l2)-branchB)
    add('pure_branch_complement_entropy_error',abs(branchB-branchE))
    add('partner_formation_upper_bound_gap',branchB-wootters(tau))
    if j<80:
        form,_,_=roof_lp(p,abs(sigma[0,1]),a,b,l2)
        add('first_marginal_formation_vs_e_gap',e(p,a,b,l2)-form)
        add('strong_superadditivity_pure_extension_gap_with_discrete_roof',SB-form-wootters(tau))

# Exact independent benchmark: completely dephasing channel's Stinespring
# states are two-qubit maximally correlated states. Their concurrence is 2|z|.
benchmark=[]
for p,z in [(.2,.1),(.5,.3),(.7,.2),(.5,0.),(.5,.5)]:
    exact=float(h((1+np.sqrt(1-4*z*z))/2))
    value,q,weights=roof_lp(p,z,0,0,0,n=6000)
    add('dephasing_roof_upper_approximation_error',value-exact)
    benchmark.append(dict(p=p,z=z,f=0.,exact_formation_nats=exact,discrete_moment_value=value,
      populations=q.tolist(),weights=weights.tolist()))

# Original mixed-hull example, using independently verified contact endpoint.
a,b,l2=.02,.3,.514624
contact=.958864969577434878625385387391883008
p=.441064892388533588098669492696277066
f=float((1-p/contact)*e(0,a,b,l2)+(p/contact)*e(contact,a,b,l2))
radius=float(p/contact*r(contact))
mixed=[]
for z in [0.,radius*.7,radius,.2,.35,float(r(p))]:
    value,q,weights=roof_lp(p,z,a,b,l2,n=6000,extra=[contact])
    mixed.append(dict(p=p,z=z,radius=radius,scalar_lower_bound=f,formation_grid_nats=value,
      pure_population_entropy=float(e(p,a,b,l2)),populations=q.tolist(),weights=weights.tolist()))

# Complement capacities: lower hull of sampled e, then concave maximization
# over p. Values are illustrations, not certified scalar optimizer bounds.
def hull(x,y):
    ix=[]
    for j in range(len(x)):
        while len(ix)>=2:
            l,m=ix[-2:]
            if (y[m]-y[l])*(x[j]-x[m]) >= (y[j]-y[m])*(x[m]-x[l]): ix.pop()
            else: break
        ix.append(j)
    return np.array(ix)
capacities=[]
for a,b,l2 in fixed:
    q=np.linspace(0,1,20001); vals=e(q,a,b,l2); ix=hull(q,vals)
    def objective(p): return float(env_entropy(p,a,b,l2)-np.interp(p,q[ix],vals[ix]))
    opt=minimize_scalar(lambda p:-objective(p),bounds=(0,1),method='bounded',options={'xatol':1e-13})
    candidates=[(0.,objective(0)),(1.,objective(1)),(float(opt.x),-float(opt.fun))]
    pp,value=max(candidates,key=lambda t:t[1])
    j=int(np.clip(np.searchsorted(q[ix],pp),1,len(ix)-1))
    q0,q1=q[ix[j-1]],q[ix[j]]; w=(pp-q0)/(q1-q0)
    V=dilation(a,b,l2)
    ens=[((1-w)/2,ket(q0)),((1-w)/2,ket(q0,np.pi)),(w/2,ket(q1)),(w/2,ket(q1,np.pi))]
    average=sum(prob*outputs(V,outer(vec))[1] for prob,vec in ens)
    chi=entropy(average)-sum(prob*entropy(outputs(V,outer(vec))[1]) for prob,vec in ens)
    add('complement_capacity_ensemble_attainment_error',abs(chi-value))
    capacities.append(dict(a=a,b=b,lambda_squared=l2,p=pp,capacity_grid_bits=value/np.log(2),
       attaining_pair_populations=[float(q0),float(q1)],attaining_upper_population_weight=float(w)))

# Algebraic match with Hellmund-Uhlmann Eq. (29), sampled in the Davies domain.
for _ in range(1000):
    a,b,k=RNG.dirichlet([1,1,1]); x=k*RNG.random()
    A=a*(1-a); B=k*(1-2*a)-x; D=x-k*k
    lo=k+2*a*b-2*np.sqrt(a*b*(k+a*b)); hi=k+2*a*b+2*np.sqrt(a*b*(k+a*b))
    add('criterion_factorization_error',abs(4*A*D-B*B+(x-lo)*(x-hi)))
    assert (D>=0 and 4*A*D>=B*B)==(x>=lo)

summary={key:dict(count=len(values),minimum=min(values),maximum=max(values)) for key,values in checks.items()}
payload=dict(seed=20261017417,runtime=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
 checks=summary,exact_dephasing_benchmarks=benchmark,mixed_hull_states=mixed,complement_capacity_examples=capacities,
 limitations=['Floating-point diagnostics are not formal proofs or interval certificates.',
 'Discrete moment programs give upper approximations to the continuous convex roof; no exact solver is claimed.',
 'Global mixed-state E_F was not numerically optimized; its proof uses pure decomposition and convexity.',
 'No claim that sampled counterexample searches establish universal additivity.',
 'An initial HiGHS run reported an unknown/infeasible status at a pure-state moment boundary; final code evaluates that exact point-mass case analytically.'])
(OUT/'independent-results.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps(payload,indent=2))
