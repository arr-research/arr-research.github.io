import numpy as np, cvxpy as cp, json, math, time
from scipy.linalg import null_space
from pathlib import Path
out=[]
for n in range(2,7):
 N=2**n
 V=np.zeros((N,n+1))
 for x in range(N): V[x,x.bit_count()]=1
 B=null_space(V.T)
 for eta in [0.,.3,.7]:
  K=np.array([[eta**((x^y).bit_count()) for y in range(N)] for x in range(N)])
  levels=[cp.Variable((2**k,2**k),symmetric=True) for k in range(1,n+1)]
  con=[]
  for k,Q in enumerate(levels,1):
   con += [Q >> 0,Q[0::2,1::2]==0]
   if k==1: con += [cp.trace(Q)==1]
   else: con += [Q[0::2,0::2]+Q[1::2,1::2]==levels[k-2]]
  X=cp.Variable((B.shape[1],B.shape[1]),symmetric=True)
  R=B@X@B.T
  con += [X >> 0,levels[-1]-R >> 0]
  prob=cp.Problem(cp.Maximize(cp.trace(K@R)),con)
  prob.solve(solver='CLARABEL',tol_gap_abs=2e-8,tol_feas=2e-8,max_iter=150)
  w=n//2
  f=sum(math.comb(w,j)*math.comb(n-w,j)*eta**(2*j) for j in range(w+1))/math.comb(n,w)
  row=dict(n=n,eta=eta,failure=1-prob.value,parallel=f,status=prob.status,normalization=float(np.trace(K@levels[-1].value)))
  print(json.dumps(row),flush=True);out.append(row)
  np.savez(Path(__file__).parent/f'phase-sdp-n{n}-eta{eta}.npz',Q=levels[-1].value,R=R.value,K=K,B=B)
  (Path(__file__).parent/'phase-sdp-results.json').write_text(json.dumps(out,indent=2))
