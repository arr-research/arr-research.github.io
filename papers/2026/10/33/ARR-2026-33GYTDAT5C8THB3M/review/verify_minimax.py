from pathlib import Path
import sys,json,hashlib,itertools,math
from fractions import Fraction as F
sys.path.insert(0,r'C:\Users\lluis\AppData\Roaming\Python\Python312\site-packages')
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
out={'candidate_sha256':hashlib.sha256((ROOT/'candidate.txt').read_bytes()).hexdigest()}
Q=np.array([[float(F(x)) for x in r] for r in json.loads((ROOT/'phase-certificate-Q.json').read_text())]);R=np.array([[float(F(x)) for x in r] for r in json.loads((ROOT/'phase-certificate-R.json').read_text())]);S=Q-R
words=list(itertools.product(range(2),repeat=5)); e=.7
K=np.array([[e**sum(a!=b for a,b in zip(x,y)) for y in words] for x in words]); weights=np.array([sum(x) for x in words]); mask=weights[:,None]==weights[None,:]
out['five_query_eta_0_7_carrier_average_failure']=float(np.sum(K*S*mask));out['parallel_optimum']=.46603
rng=np.random.default_rng(164257); results=[]
for d,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
 for trial in range(5):
  N=d**n; mem=N//d
  B=np.eye(N,dtype=complex)[:,0:1]
  for k in range(n):
   Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));U=np.linalg.qr(Z)[0];W=U@B
   B=np.zeros((N,d**(k+1)),dtype=complex)
   for a in range(d): B[a*mem:(a+1)*mem,a::d]=W[a*mem:(a+1)*mem,:]
  ws=list(itertools.product(range(d),repeat=n));groups={}
  for i,w in enumerate(ws):groups.setdefault(tuple(w.count(a) for a in range(d)),[]).append(i)
  Us=np.stack([B[:,ix].sum(axis=1) for ix in groups.values()],axis=1)
  assert abs(np.linalg.norm(Us)**2-1)<1e-12
  A=Us@np.linalg.pinv(Us); S=B.conj().T@A@B
  V=rng.normal(size=(d,2))+1j*rng.normal(size=(d,2));V/=np.linalg.norm(V,axis=1)[:,None]; C=V@V.conj().T
  K=np.array([[math.prod(C[x[k],y[k]] for k in range(n)) for y in ws] for x in ws])
  average=0.;lower=0.;Fm=[];blockmin=[]
  for ix in groups.values():
   block=K[np.ix_(ix,ix)];nm=len(ix);f=(block.sum()/nm**2).real;Fm.append(float(f));
   u=B[:,ix].sum(axis=1);lower+=f*np.vdot(u,u).real
   average+=np.trace(block@S[np.ix_(ix,ix)]).real
   blockmin.append(float(np.linalg.eigvalsh(block-f*np.ones((nm,nm))).min()))
  assert average+1e-12>=lower>=min(Fm)-1e-12
  assert min(blockmin)>-1e-12
  # Direct channel evolution and phase quadrature are not needed: the block test
  # exercises complex C and nonorthogonal type sums in the stated lower bound.
  results.append({'d':d,'n':n,'average_failure':float(average),'weighted_lower_bound':float(lower),'min_type':min(Fm),'smallest_block_remainder_eigenvalue':min(blockmin)})
out['random_causal_cases']=results;out['status']='PASS'
(HERE/'minimax-checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='random_causal_cases'},indent=2));print('Random causal cases:',len(results))
