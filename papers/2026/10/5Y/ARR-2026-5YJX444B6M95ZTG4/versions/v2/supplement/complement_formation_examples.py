"""Exploratory float illustrations of the proposed dilation extension, not proofs.
Compare explicit Stinespring matrices with analytical complement spectra;
calculate a sampled moment program for state formation and a complementary
channel capacity. No interval certification or channel entanglement cost.
"""
from pathlib import Path
import json, math
import numpy as np
from scipy.optimize import minimize_scalar, linprog
from scipy.special import xlogy
from capacity_scalar_screen import curve
R=Path(__file__).resolve().parent

def entropy_spectrum(x):
    x=np.clip(np.asarray(x),0,1)
    return float(-np.sum(xlogy(x,x)))

def dilation(a,b,l2):
    # Four-dimensional environment, including zero unused sectors at boundaries.
    den=(1-a)*(1-b)
    c=math.sqrt(l2/den) if den>0 else 0
    u=np.array([1.,0,0,0]);v=np.array([c,math.sqrt(max(0,1-c*c)),0,0])
    plus=np.array([0.,0,1,0]);minus=np.array([0.,0,0,1])
    V=np.zeros((2,4,2),complex)
    V[0,:,0]=math.sqrt(1-a)*u;V[1,:,0]=math.sqrt(a)*plus
    V[0,:,1]=math.sqrt(b)*minus;V[1,:,1]=math.sqrt(1-b)*v
    return V.reshape(8,2)

def outputs(V,rho):
    omega=(V@rho@V.conj().T).reshape(2,4,2,4)
    return np.einsum('abcb->ac',omega),np.einsum('abad->bd',omega)

def env_spectrum(a,b,l2,p):
    w=(1-a)*(1-p)+(1-b)*p
    d=p*(1-p)*((1-a)*(1-b)-l2)
    rad=math.sqrt(max(0,w*w-4*d))
    return np.array([a*(1-p),b*p,(w+rad)/2,(w-rad)/2])

def convex_hull(p,e):
    hull=[]
    for i in range(len(p)):
        while len(hull)>1:
            u,v=hull[-2:]
            if (e[v]-e[u])*(i-v)>=(e[i]-e[v])*(v-u):hull.pop()
            else:break
        hull.append(i)
    return hull

def example(a,b,l2,n=60000):
    p=np.linspace(0,1,n+1);e=curve(a,b,l2,p);hull=convex_hull(p,e)
    fun=lambda t: entropy_spectrum(env_spectrum(a,b,l2,t))-np.interp(t,p[hull],e[hull])
    opt=minimize_scalar(lambda t:-fun(t),bounds=(0,1),method='bounded',options={'xatol':2e-13})
    m=float(opt.x)
    capacity=max(fun(m),fun(0),fun(1))/np.log(2)
    return dict(a=a,b=b,lambda_squared=l2,grid_intervals=n,complement_capacity_bits_approx=capacity,mean_population_approx=m,optimizer_success=bool(opt.success))

rng=np.random.default_rng(20261017721)
errors={k:0. for k in ('isometry','channel','spectrum','covariance')}
for i in range(500):
    a,b=rng.dirichlet([.8,.8,.8])[:2];k=1-a-b;l2=float(k*rng.random())
    V=dilation(a,b,l2);errors['isometry']=max(errors['isometry'],float(np.max(np.abs(V.conj().T@V-np.eye(2)))))
    p=float(rng.random());z=math.sqrt(p*(1-p))*rng.random()*np.exp(2j*np.pi*rng.random())
    rho=np.array([[1-p,z],[z.conjugate(),p]])
    out,env=outputs(V,rho);t=a+k*p
    target=np.array([[1-t,math.sqrt(l2)*z],[math.sqrt(l2)*z.conjugate(),t]])
    errors['channel']=max(errors['channel'],float(np.max(np.abs(out-target))))
    _,envdiag=outputs(V,np.diag([1-p,p]))
    errors['spectrum']=max(errors['spectrum'],float(np.max(np.abs(np.sort(np.linalg.eigvalsh(envdiag))-np.sort(env_spectrum(a,b,l2,p))))))
    theta=float(2*np.pi*rng.random());U=np.diag([1,np.exp(1j*theta)]);W=np.diag([1,1,np.exp(-1j*theta),np.exp(1j*theta)])
    errors['covariance']=max(errors['covariance'],float(np.max(np.abs(V@U-np.kron(U,W)@V))))
assert max(errors.values())<1e-12
examples=[example(*x) for x in ((.1,.3,.6),(.1,.3,.5),(.1,.3,.1),(.02,.3,.514624))]

# A moment LP at fixed input with coherence outside the f(p)-saturation region.
a,b,l2=.02,.3,.514624;pbar=.44
q=np.linspace(0,1,20001);e=curve(a,b,l2,q);r=np.sqrt(q*(1-q))
formation=[]
for z in (0,.05,.1,.25,.45):
    result=linprog(e,A_ub=np.array([-r]),b_ub=np.array([-z]),A_eq=np.stack([np.ones_like(q),q]),b_eq=[1,pbar],bounds=(0,None),method='highs',options={'dual_feasibility_tolerance':1e-10,'primal_feasibility_tolerance':1e-10})
    assert result.success
    ix=np.where(result.x>1e-8)[0];weights=result.x[ix]
    radius=float(weights@r[ix]);phase_mean=min(1.,max(0.,z/radius)) if radius else 0
    # Reconstruct the input from the finite, two-phase population ensemble.
    rho=np.zeros((2,2),complex);entropy=0.
    V=dilation(a,b,l2)
    for idx,weight in zip(ix,weights):
        for sign,phaseweight in ((1,(1+phase_mean)/2),(-1,(1-phase_mean)/2)):
            vec=np.array([math.sqrt(1-q[idx]),sign*math.sqrt(q[idx])])
            pure=np.outer(vec,vec);w=float(weight*phaseweight)
            rho+=w*pure;out,_=outputs(V,pure)
            entropy+=w*entropy_spectrum(np.linalg.eigvalsh(out))
    assert np.max(np.abs(rho-np.array([[1-pbar,z],[z,pbar]])))<2e-8
    assert abs(entropy-result.fun)<2e-8
    formation.append(dict(p=pbar,z=z,formation_bits_grid_approx=float(result.fun/np.log(2)),populations=q[ix].tolist(),weights=weights.tolist(),coherence_radius=radius,reconstruction_error=float(np.max(np.abs(rho-np.array([[1-pbar,z],[z,pbar]]))))))
record=dict(status='floating-point illustrations only; sampled LP is restricted, not exact continuous certificate',matrix_cases=500,max_errors=errors,complement_examples=examples,formation_examples=formation,claim_scope='state entanglement formation/cost, never channel simulation cost')
(R/'complement-formation-results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
