"""Discover finite evaluation witnesses, then certify identities over Q.

Numerical feasibility only chooses support; all asserted obstructions are
subsequently proved by rational linear algebra and positive rational weights.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import numpy as np
import sympy as s
from scipy.optimize import linprog

base=Path(__file__).resolve().parent
out=base/'degree-obstruction-33.json'
assert not out.exists()
records=[]
parameters=[s.Rational(j,20) for j in range(-100,101)]+[s.Rational(j) for j in [-100,-20,-10,10,20,100]]

def row(M,t,kind):
    if t is None: co,si=s.Integer(-1),s.Integer(0)
    else: co,si=(1-t*t)/(1+t*t),2*t/(1+t*t)
    cs=[s.Integer(1)];sn=[s.Integer(0)]
    for k in range(1,M+1):
        cs.append(s.expand(cs[-1]*co-sn[-1]*si))
        sn.append(s.expand(sn[-1]*co+cs[-2]*si))
    p=s.Matrix([1]+[v for k in range(1,M+1) for v in [2*cs[k],-2*sn[k]]])
    dp=s.Matrix([0]+[v for k in range(1,M+1) for v in [-2*k*sn[k],-2*k*cs[k]]])
    F=-s.Rational(3,4)+s.Rational(51,20)*co
    G=1+s.Rational(3,5)*co
    return p if kind=='p' else -M*F*p-G*dp

for M in [1,2,3]:
    specs=[(t,kind) for t in parameters+[None] for kind in ['p','d']]
    columns=[row(M,t,kind) for t,kind in specs]
    mat=np.array(s.Matrix.hstack(*columns),dtype=float)
    scales=np.max(np.abs(mat),axis=0)
    rhs=np.zeros(2*M+1);rhs[0]=-1
    lp=linprog(np.ones(len(specs)),A_eq=mat/scales,b_eq=rhs,bounds=(0,None),method='highs')
    record={'M':M,'degree':2*M,'floating_status':lp.message,'exact_obstruction':False}
    if lp.success:
        support=np.where(lp.x>1e-8)[0].tolist()
        exact=s.Matrix.hstack(*(columns[j] for j in support))
        target=s.Matrix([-1]+[0]*(2*M))
        weights=exact.gauss_jordan_solve(target)[0]
        assert not any(w.free_symbols for w in weights)
        assert all(w>0 for w in weights)
        assert exact*weights==target
        record.update(exact_obstruction=True,coefficient_order='p0,Re(p1),Im(p1),...,Re(pM),Im(pM)',identity='Sum weights*p(phi) or weights*d(phi) equals -p0 identically in profile coefficients.',support=[{'t':str(specs[j][0]) if specs[j][0] is not None else 'infinity','kind':specs[j][1],'weight':str(w),'row':[str(v) for v in columns[j]]} for j,w in zip(support,weights)])
    records.append(record)
    print(json.dumps({'M':M,'lp_success':bool(lp.success),'exact_obstruction':record['exact_obstruction'],'support_size':len(record.get('support',[]))}),flush=True)

assert all(r['exact_obstruction'] for r in records)
result={'at':datetime.now(timezone.utc).isoformat(),'definition':'p(phi)=p0+2 Re(sum pk exp(ik phi));d=-M F p-G dp/dphi;F=-3/4+51/20 cos(phi),G=1+3/5 cos(phi).','scope':'For each M=1,2,3 finite positive rational evaluations prove no nonzero nonnegative profile p with d>=0. Combined with the separately certified degree8 polynomial this proves minimum homogeneous degree8; with the analytic leading-term lemma it also excludes nonhomogeneous polynomial degrees below8.','records':records}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
