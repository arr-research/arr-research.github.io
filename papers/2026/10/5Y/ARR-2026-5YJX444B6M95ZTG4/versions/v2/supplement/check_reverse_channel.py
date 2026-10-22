"""Research diagnostics for the reverse-normalization argument, not proofs."""
from pathlib import Path
import json, math
import numpy as np
from scipy.special import xlogy
from scipy.optimize import minimize_scalar
R=Path(__file__).resolve().parent

def V_davies(a,b,l2):
    den=(1-a)*(1-b);c=math.sqrt(max(0,l2/den)) if den else 0
    u=np.array([1.,0,0,0]);v=np.array([c,math.sqrt(max(0,1-c*c)),0,0])
    ep=np.array([0,0,1.,0]);em=np.array([0,0,0,1.])
    V=np.zeros((2,4,2),complex)
    V[0,:,0]=math.sqrt(1-a)*u;V[1,:,0]=math.sqrt(a)*ep
    V[0,:,1]=math.sqrt(b)*em;V[1,:,1]=math.sqrt(1-b)*v
    return V

def reverse(a,b,l2,p):
    k=1-a-b;t=a+k*p;s=1-t
    return p*b/s,(1-p)*a/t,l2*p*(1-p)/(s*t),t

def h(x):return -xlogy(x,x)-xlogy(1-x,1-x)
def formation_at_p(a,b,l2,p,grid=12000):
    if p<=0 or p>=1:return 0.
    t=a+(1-a-b)*p
    if t<=0 or t>=1:return float(h(p))
    ap,bp,lp,t=reverse(a,b,l2,p);kp=1-ap-bp
    q=np.linspace(0,1,grid+1)
    det=np.clip((ap+kp*q)*(1-ap-kp*q)-lp*q*(1-q),0,.25)
    e=h((1+np.sqrt(1-4*det))/2)
    hull=[]
    for i in range(grid+1):
        while len(hull)>1:
            u,v=hull[-2:]
            if (e[v]-e[u])*(i-v)>=(e[i]-e[v])*(v-u):hull.pop()
            else:break
        hull.append(i)
    return float(np.interp(t,q[hull],e[hull]))

rng=np.random.default_rng(20261017991)
errors={k:0. for k in ('isometry','reverse_channel','state_reconstruction','k_identity')}
min_slack=1.
for i in range(500):
    a,b=rng.dirichlet([1.,1.,1.])[:2];k=1-a-b;l2=k*rng.random();p=.001+.998*rng.random()
    V=V_davies(a,b,l2)
    # Psi on R,B,E; discard B to obtain the complementary reference-output state.
    psi=np.zeros((2,2,4),complex)
    psi[0]=math.sqrt(1-p)*V[:,:,0];psi[1]=math.sqrt(p)*V[:,:,1]
    t=a+k*p
    W=np.stack([psi[:,0,:]/math.sqrt(1-t),psi[:,1,:]/math.sqrt(t)],axis=-1)
    Wm=W.reshape(8,2)
    errors['isometry']=max(errors['isometry'],float(np.max(np.abs(Wm.conj().T@Wm-np.eye(2)))))
    target=np.einsum('rbe,sbf->resf',psi,psi.conj()).reshape(8,8)
    recovered=Wm@np.diag([1-t,t])@Wm.conj().T
    errors['state_reconstruction']=max(errors['state_reconstruction'],float(np.max(np.abs(target-recovered))))
    ap,bp,lp,_=reverse(a,b,l2,p);kp=1-ap-bp
    errors['k_identity']=max(errors['k_identity'],abs(kp-k*p*(1-p)/(t*(1-t))))
    min_slack=min(min_slack,kp-lp)
    q=rng.random();z=math.sqrt(q*(1-q))*rng.random()*np.exp(2j*np.pi*rng.random())
    rho=np.array([[1-q,z],[z.conjugate(),q]])
    out=np.einsum('rei,ij,sej->rs',W,rho,W.conj());pop=ap+kp*q
    expected=np.array([[1-pop,math.sqrt(lp)*z],[math.sqrt(lp)*z.conjugate(),pop]])
    errors['reverse_channel']=max(errors['reverse_channel'],float(np.max(np.abs(out-expected))))
assert max(errors.values())<2e-13 and min_slack>=-1e-13
examples=[]
for a,b,l2 in ((.1,.3,.6),(.1,.3,.5),(.1,.3,.1),(.02,.3,.514624),(0,0,1),(0,0,.4),(.3,.7,0)):
    opt=minimize_scalar(lambda p:-formation_at_p(a,b,l2,p),bounds=(.0001,.9999),method='bounded',options={'xatol':1e-9})
    examples.append(dict(a=a,b=b,lambda_squared=l2,grid_intervals=12000,p_approx=float(opt.x),parallel_complement_cost_ebits_approx=float(-opt.fun/np.log(2)),optimizer_success=bool(opt.success)))
out=dict(status='Research diagnostics only; no formal proof or interval certificate',cases=500,max_errors=errors,min_davies_slack=min_slack,examples=examples)
(R/'reverse-channel-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
