"""Exact initial-block inertia certificates for bounded s, all k>=3."""
from pathlib import Path
import sys,json,sympy as sp
from odd_cycle_ground_kernels import symbolic_ground,ground
from exact_inertia import inertia
R=Path(__file__).parent;u=sp.symbols('u');rows=[]
for s in range(2,20):
    L,k=symbolic_ground(s)
    active=[i for i in range(L.rows) if any(L[i,j]!=0 for j in range(L.cols))]
    records=[]
    for r in range(4,min(len(active),12)+1):
        M=L.extract(active[:r],active[:r]);det=sp.Poly(sp.expand(M.det(method='domain-ge')),k)
        if det.is_zero:continue
        sign=sp.sign(det.LC());threshold=None;cert=None
        for N in [3,4,5,8,12,20,40,80]:
            shifted=sp.Poly(sp.expand(sign*det.as_expr().subs(k,u+N)),u)
            if all(c>=0 for c in shifted.all_coeffs()) and shifted.eval(0)>0:
                threshold=N;cert=[str(c) for c in shifted.all_coeffs()];break
        if threshold is None:continue
        sig,piv=inertia(M.subs(k,threshold))
        records.append(dict(r=r,threshold=threshold,inertia=sig,determinant=str(det.as_expr()),constant_sign=int(sign),shifted_coefficients=cert))
        # With no determinant zero on [N,infinity), inertia is constant.
        if sig[0]>=2 and sig[2]==0:break
    assert records and records[-1]['inertia'][0]>=2,(s,'no tail certificate')
    tail=records[-1];finite=[]
    for kk in range(3,tail['threshold']):
        for r in range(4,min(len(active),12)+1):
            sig,piv=inertia(L.extract(active[:r],active[:r]).subs(k,kk))
            if sig[0]>=2 and sig[2]==0:
                finite.append(dict(k=kk,r=r,inertia=sig,pivots=piv));break
        else:raise AssertionError((s,kk,'no finite initial block'))
    M,N=ground(2,s);aa=[i for i in range(M.rows) if any(M[i,j] for j in range(M.cols))]
    for r in range(4,min(len(aa),12)+1):
        sig,piv=inertia(M.extract(aa[:r],aa[:r]))
        if sig[0]>=2 and sig[2]==0:break
    assert sig[0]>=2 and sig[2]==0
    rows.append(dict(s=s,active=active,tail=tail,finite=finite,k2=dict(r=r,inertia=sig,pivots=piv),maximum_initial_size=max([tail['r'],r]+[x['r'] for x in finite])))
    print(json.dumps(dict(s=s,tail_r=tail['r'],threshold=tail['threshold'],k2_r=r,maximum_r=rows[-1]['maximum_initial_size'])),flush=True)
    (R/'odd-initial-small-certificates.json').write_text(json.dumps(dict(status='in_progress',rows=rows),indent=2)+'\n')
(R/'odd-initial-small-certificates.json').write_text(json.dumps(dict(status='PASS_EXACT_POLYNOMIAL_AND_INERTIA_CERTIFICATES',rows=rows,maximum_initial_size=max(x['maximum_initial_size'] for x in rows),infinite_tail_logic='Symmetric real polynomial matrix with nonzero determinant on a connected real interval has constant inertia.'),indent=2)+'\n')
