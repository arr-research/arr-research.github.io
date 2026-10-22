from pathlib import Path
from datetime import datetime, timezone
import json
import cvxpy as cp
import numpy as np

out = Path(__file__).resolve().parent
if (out/'toeplitz-diagnostic.json').exists():
    raise FileExistsError('Run in a fresh directory without the saved output JSON.')
out.mkdir(parents=True, exist_ok=True)
rows=[]
for a in [0.125, 1.0, 8.0]:
    for degree in [1,2,4,8,16,24]:
        m=cp.Variable(degree, complex=True)
        b=cp.Variable()
        w=cp.hstack([1j*m[k]-(b/2 if k==0 else 0) for k in range(degree)])
        def toeplitz(seq, mass):
            return cp.bmat([[mass if j==k else seq[k-j-1] if k>j else cp.conj(seq[j-k-1]) for k in range(degree+1)] for j in range(degree+1)])
        tm=toeplitz(m,1)
        tw=toeplitz(w,a)
        prob=cp.Problem(cp.Maximize(b),[tm >> 0,tw >> 0,b >= 0])
        prob.solve(solver='CLARABEL',max_iter=150)
        rows.append(dict(a=a,degree=degree,status=prob.status,maximum_b=float(b.value),
                         proposed_limit=float((1+a**(2/3))**1.5),
                         min_eig_m=float(np.linalg.eigvalsh(tm.value).min()),
                         min_eig_w=float(np.linalg.eigvalsh(tw.value).min())))
        print(json.dumps(rows[-1]),flush=True)
result=dict(at=datetime.now(timezone.utc).isoformat(),
            scope='Necessary finite Toeplitz relaxations only, numerical not certified. No existence or sharpness conclusion.',rows=rows)
(out/'toeplitz-diagnostic.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
