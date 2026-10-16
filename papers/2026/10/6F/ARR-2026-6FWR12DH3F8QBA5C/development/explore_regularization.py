"""Exploratory reviewer calculations; numerical optimization is not a proof."""
from pathlib import Path
import json, datetime
import numpy as np
from scipy.optimize import minimize

root=Path(__file__).resolve().parent
rng=np.random.default_rng(1610202602)
K=[]
for i,j in [(0,1),(0,2),(1,2)]:
    a=np.zeros((3,3),complex); a[i,j]=1/np.sqrt(2); a[j,i]=-1/np.sqrt(2); K.append(a)
K=np.array(K)

def fg(x,m):
    t=3*m*m
    y=(x[:t]+1j*x[t:]).reshape(3,m,m)
    h=sum(np.kron(k,z) for k,z in zip(K,y))
    sign,logdet=np.linalg.slogdet(h)
    norm=np.vdot(y,y).real
    val=2*logdet/(3*m)-np.log(norm/m)
    inv=np.linalg.inv(h).reshape(3,m,3,m)
    deriv=np.einsum('irs,sbra->iab',K,inv)
    gr=2*deriv.real/(3*m)-2*y.real/norm
    gi=-2*deriv.imag/(3*m)-2*y.imag/norm
    return -float(val),-np.r_[gr.ravel(),gi.ravel()]

# Check analytic gradient on a nonsingular random point.
m=2; x=rng.normal(size=6*m*m); f,g=fg(x,m)
errs=[]
for j in [0,3,11,14,19,23]:
    xp=x.copy(); xm=x.copy(); xp[j]+=1e-6; xm[j]-=1e-6
    fd=(fg(xp,m)[0]-fg(xm,m)[0])/2e-6
    errs.append(abs(fd-g[j]))
assert max(errs)<1e-6

records=[]
for m in [2,3,4,5,6]:
    for trial in range(3):
        x0=rng.normal(size=6*m*m)
        sol=minimize(lambda x:fg(x,m),x0,jac=True,method='L-BFGS-B',
            options={'maxiter':900,'ftol':1e-12,'gtol':1e-8})
        rec={'m':m,'trial':trial,'a_found':float(np.exp(-sol.fun)),
             'converged':bool(sol.success),'iterations':int(sol.nit),
             'max_gradient':float(np.max(abs(sol.jac)))}
        records.append(rec); print(json.dumps(rec),flush=True)
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'purpose':'Exploratory local optimization only; not a certificate of global optimum.',
     'gradient_max_finite_difference_error':max(errs),
     'W3_a2_exact':float(2**(2/3)/6),
     'W3_a3_witness':float(2**(2/9)/4),
     'W3_uniform_upper_from_Haagerup_Musat':25/81,
     'pinching_2_plus_1_a_all_m':float(2**(2/3)/3),
     'pinching_2_plus_1_frobenius_upper':2/3,
     'results':records}
(root/'regularization-numerical-exploration.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
