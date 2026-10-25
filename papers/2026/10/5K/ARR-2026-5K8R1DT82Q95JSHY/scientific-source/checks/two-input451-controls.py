from fractions import Fraction as Q
from math import comb
import json

checks=[]
for d in range(2,301):
    t=Q(1,2)
    a=1-4*t/d
    cs=[sum((Q(comb(4-r,u-r))*Q(d)**(2-u)*(-t)**(4-u)
             for u in range(r,3)),Q(0)) for r in range(3)]
    assert cs==[Q((d-4)**2+8,16),Q(6-d,8),Q(1,4)]
    assert a>=0 and cs[0]>0
    if d>=7:
        eigen=a+cs[1]
        assert eigen==Q(-d*d+14*d-16,8*d)
        assert (eigen>=0)==(d<=12)
    if d>=13:
        K=(Q(2*d*(d-2),d-6)).__floor__()
        assert K<d*d
        assert a+cs[1]*min(Q(1),Q(4*K,d*d))>=0
        # The same elementary lower bound fails at K+1; not an actual
        # negative witness and not a proof that the true threshold fails.
        assert a+cs[1]*min(Q(1),Q(4*(K+1),d*d))<0
        checks.append({'d':d,'guaranteed_k':K,'negative_Choi_eigenvalue':str(a+cs[1])})
assert checks[0]=={'d':13,'guaranteed_k':40,'negative_Choi_eigenvalue':'-3/104'}
print(json.dumps({'status':'PASS','scalar_dimensions':299,'non_CP_dimensions':len(checks),'scope':'Scalar coefficient, sign and floor checks only. No full Choi construction or independent audit.','cases':checks},indent=2))
