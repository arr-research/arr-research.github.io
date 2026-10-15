from pathlib import Path
import numpy as np,json,math,itertools
from fractions import Fraction
p=Path(__file__).parent;n=5;N=32
Q=np.array([[float(Fraction(x)) for x in row] for row in json.loads((p/'phase-certificate-Q.json').read_text())]);R=np.array([[float(Fraction(x)) for x in row] for row in json.loads((p/'phase-certificate-R.json').read_text())])
Qs={n:Q}
for k in range(n,0,-1):Qs[k-1]=Qs[k][0::2,0::2]+Qs[k][1::2,1::2]
Vs={0:np.ones((1,1))};Ws={};errs=[]
for k in range(1,n+1):
 half=2**(k-1);B0=np.linalg.cholesky(Qs[k][0::2,0::2]).T;B1=np.linalg.cholesky(Qs[k][1::2,1::2]).T
 V=np.zeros((2*half,2*half));V[:half,0::2]=B0;V[half:,1::2]=B1;Vs[k]=V
 W=np.vstack([B0,B1])@np.linalg.inv(Vs[k-1]);Ws[k]=W;errs += [np.linalg.norm(W.T@W-np.eye(half)),np.linalg.norm(V.T@V-Qs[k])]
invV=np.linalg.inv(Vs[n]);M=invV.T@R@invV
rng=np.random.default_rng(20261015)
def final(phases):
 v=np.ones(1,dtype=complex)
 for k,phi in enumerate(phases,1):
  v=Ws[k]@v;v[2**(k-1):]*=np.exp(1j*phi)
 return v
false=[];polyerr=[]
for theta in rng.uniform(-10000,10000,200):
 v=final([theta]*5);false.append(abs(np.vdot(v,M@v)))
for phases in rng.uniform(-10,10,(100,5)):
 v=final(phases);z=np.array([np.exp(1j*sum(phases[j] for j in range(5) if (x>>(4-j))&1)) for x in range(32)]);polyerr.append(np.linalg.norm(v-Vs[n]@z))
alt=[]
coef=[float(Fraction(v)) for v in json.loads((p/'phase-certificate-summary.json').read_text())['rejection_coefficients']]
for eta in np.linspace(0,1,21):
 rho=np.ones((1,1))
 for k in range(1,6):
  rho=Ws[k]@rho@Ws[k].T;z=np.diag([1]*(2**(k-1))+[-1]*(2**(k-1)));rho=(1+eta)/2*rho+(1-eta)/2*z@rho@z
 exact=sum(c*eta**j for j,c in enumerate(coef));alt.append(abs(np.trace(M@rho)-exact))
report={'isometry_and_gram_max_error':max(errs),'measurement_eigenvalues':[float(np.linalg.eigvalsh(M).min()),float(np.linalg.eigvalsh(M).max())],'static_trials':len(false),'max_false_positive_roundoff':float(max(false)),'independent_phase_trials':len(polyerr),'max_coefficient_error':float(max(polyerr)),'kraus_density_trials':len(alt),'max_probability_error':float(max(alt))}
assert max(errs)<1e-10 and max(false)<1e-10 and max(polyerr)<1e-10 and max(alt)<1e-10
np.savez(p/'circuit-realization.npz',M=M,**{f'W{k}':v for k,v in Ws.items()})
(p/'circuit-verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
