from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as sp
import numpy as np

dest = Path(__file__).resolve().parent
if (dest/'phase-checks-30.json').exists():
    raise FileExistsError('Run in a fresh directory without the saved output JSON.')
c=sp.symbols('c',positive=True); z=sp.symbols('z',nonzero=True)
s=sp.sqrt(1+c*c); eta=(c+sp.I)/s; etabar=(c-sp.I)/s
M=c*c-1+2*sp.I*c*(1+eta*z)/(1-eta*z)
q=1-c**4+s**3/2*((c-sp.I)*z+(c+sp.I)/z)
factor=sp.simplify(q+s*s/2*M*(1-eta*z)*(1-etabar/z))
constant=sp.simplify(sp.I*c**3+sp.I*(1-c**4)/(c+sp.I)-sp.I*s**3/2*(2*sp.I*c/s)/(c+sp.I))
assert factor==0 and constant==1
rows=[]
Ngrid=32768
phi=2*np.pi*(np.arange(Ngrid)+.371)/Ngrid
zz=np.exp(1j*phi)
for cc in [.125,.5,1.,2.,8.]:
    ss=np.sqrt(1+cc*cc); ee=(cc+1j)/ss; aa=cc**3; bb=ss**3
    mm=cc*cc-1+2j*cc*(1+ee*zz)/(1-ee*zz)
    ff=np.sqrt(np.maximum(mm.real,0))+1j*np.sqrt(np.maximum(-mm.real,0))
    qq=1-cc**4+bb*np.real((cc-1j)*zz)
    hh=1j*aa-1j*bb/2*(zz+1/zz)+1j*qq/ff
    uu=hh.real; ww=aa-bb*np.cos(phi)-hh.imag
    row=dict(c=cc,a=aa,b=bb,min_u=float(uu.min()),min_w=float(ww.min()),
             mean_h_real=float(hh.mean().real),mean_h_imag=float(hh.mean().imag),
             max_complementarity=float(np.abs(uu*ww).max()),
             max_factorization_error=float(np.abs(qq+ss*ss/2*mm.real*np.abs(1-ee*zz)**2).max()))
    assert row['min_u']>-1e-8 and row['min_w']>-1e-8
    assert abs(hh.mean()-1)<.003
    rows.append(row)

# Construct actual finite products by empirical approximation in one interior
# parameter case. The test evaluates the analytic logarithmic derivative;
# it is a floating point boundary-grid diagnostic, not a positivity proof.
cc=1.;aa0=1.;bb=2*np.sqrt(2);rr=.98;aa=1.2
ee=(1+1j)/np.sqrt(2)
mm=2j*(1+ee*zz)/(1-ee*zz)
ff=np.sqrt(np.maximum(mm.real,0))+1j*np.sqrt(np.maximum(-mm.real,0))
qq=bb*np.real((1-1j)*zz)
hh=1j-1j*bb/2*(zz+1/zz)+1j*qq/ff
density=np.maximum(hh.real,0);cdf=np.cumsum(density);cdf/=cdf[-1]
N=2048
ix=np.searchsorted(cdf,(np.arange(N)+.5)/N)
alpha=rr*np.exp(-1j*phi[ix])
angles=2*np.pi*np.arange(8192)/8192
values=[]
for j in range(0,len(angles),128):
    t=alpha[:,None]*np.exp(1j*angles[j:j+128])[None,:]
    values.extend(np.mean((1+t)/(1-t),axis=0))
values=np.asarray(values)
margin=aa-bb*np.cos(angles)-values.imag
assert margin.min()>.05
theta=np.array([0.,.13,.61,1.3,2.4]);x=np.cos(theta);y=np.sin(theta)
qvals=(1+abs(alpha[:,None])**2)-2*alpha.real[:,None]*np.cos(2*theta)+2*alpha.imag[:,None]*np.sin(2*theta)
dq=4*alpha.real[:,None]*np.sin(2*theta)+4*alpha.imag[:,None]*np.cos(2*theta)
g=np.mean(dq/qvals,axis=0)/2
t=alpha[:,None]*np.exp(2j*theta)
g2=np.mean((1+t)/(1-t),axis=0).imag
assert np.max(abs(g-g2))<1e-12
res=dict(at=datetime.now(timezone.utc).isoformat(),symbolic=dict(factorization='exact_zero',removable_constant='exact_one'),
         boundary_diagnostics=rows,
         finite_product=dict(a=aa,b=float(bb),quadratic_factors=N,degree=2*N,root_modulus=rr,
                             grid_points=len(angles),minimum_sampled_margin=float(margin.min()),
                             logarithmic_derivative_identity_error=float(np.max(abs(g-g2)))),
         caveat='Floating point sampling is not interval-certified global positivity. Proposed theorem is justified only by the separate analytic argument and awaits independent audit.')
(dest/'phase-checks-30.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps(res,indent=2))
