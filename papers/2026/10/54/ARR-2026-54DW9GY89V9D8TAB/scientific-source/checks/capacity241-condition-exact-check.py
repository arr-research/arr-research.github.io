"""Exact algebra and finite spectral-order diagnostics for candidate240."""
import sympy as s,itertools,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parent
x,t,lam=s.symbols('x t lam',real=True)
a,b,c,e=s.symbols('a b c e',real=True)
v=s.Matrix([a,b,c,e]);K=a*a+a*b+b*b+c*c+c*e+e*e
M=s.hessian(2*K,v)/2;L=a+b+c+e;z=x-1
want={
 'same':-lam*(lam*x-x+1)*(-9*lam**2+3*lam*x+3*lam-x+1)/x,
 'cross':-lam*(3*lam*x-2*x+2)*(-3*lam**2+2*lam*x-x+1)/x}
for name,u,w in [('same',a,b),('cross',a,e)]:
    W=x*L**2/2-z*L*(u+w)+z*(u*u+w*w)-z*z*(w-u)**2/(2*x)
    N=s.hessian(W,v)/2
    assert s.factor((N-lam*M).det()-want[name])==0
# Universal algebraic attainer identities, in the quotient by t's quadratic.
relation=t*t+2*(x-1)*t+x-2
Lambda=(2*x+t-1)/3
ratio_num=(1+t)**2+x-1
ratio_den=2*(1+t+t*t)
assert s.rem(s.expand(ratio_num-Lambda*ratio_den),relation,t)==0
rows=[x+t,1-x,-1-t]
projection_energy=s.Rational(2,3)*sum(q*q for q in rows)
D_energy=2*((1+t)**2+x-1)
assert s.rem(s.expand(projection_energy-Lambda*D_energy),relation,t)==0
assert s.rem(s.expand(3*Lambda**2-2*x*Lambda+x-1),relation,t)==0
# Finite direct sorted-grid check, independently computing the centering theta.
small=middle=0
for gaps in itertools.product(range(3),repeat=4):
    aa,bb,cc,ee=gaps
    if not any(gaps):continue
    f=[F(2*aa+bb,3),F(bb-aa,3),F(-aa-2*bb,3)]
    g=[F(2*cc+ee,3),F(ee-cc,3),F(-cc-2*ee,3)]
    LL=sum(gaps);u=min(aa,cc);w=min(bb,ee)
    for n in range(1,6):
        spectrum=sorted([fi+gj for fi in f for gj in g for _ in range(n)],reverse=True)
        for r in range(1,2*n):
            chosen=spectrum[:r]+spectrum[-r:]
            theta=sum(chosen)/len(chosen)
            actual=sum((h-theta)**2 for h in chosen)
            if r<=n:
                assert actual==F(r,2)*(spectrum[0]-spectrum[-1])**2
                small+=1
            if r>=n:
                xx=F(r,n);zz=xx-1
                Q=xx*LL**2/2-zz*LL*(u+w)+zz*(u*u+w*w)-zz*zz*(w-u)**2/(2*xx)
                assert actual/n==Q
                middle+=1
out=dict(status='PASS_EXACT_PENCILS_ATTAINERS_AND_FINITE_SPECTRAL_SORTING',
         universal_symbolic_pencil_identities=2,
         universal_attainer_quotient_identities=3,
         direct_first_range_spectral_checks=small,
         direct_second_range_spectral_checks=middle,
         gap_vectors=80,n_values=[1,2,3,4,5],
         limits='Exact polynomial identities are universal for their algebraic statements; finite sorting checks do not replace the universal rank/inertia duality proof or literature assessment. No score.')
(root/'capacity241-condition-exact-check.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
