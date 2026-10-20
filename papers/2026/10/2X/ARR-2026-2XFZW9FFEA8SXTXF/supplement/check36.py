"""Exact finite identities for proposal36, not a proof of all analytic steps."""
from pathlib import Path
from datetime import datetime,timezone
import json,sympy as s
R=Path(__file__).resolve().parent;out=R/'checks-36.json';assert not out.exists()
x,y,t,e,m,ef,z,alpha,r=s.symbols('x y t e m ef z alpha r',real=True)
f=-x**5+16*x**3*y**2-3*x*y**4;g=x**4*y+20*x**2*y**3-y**5
rho=x*x+y*y
assert s.expand(x*f+y*g-(-rho**3+20*x*x*y*y*rho))==0
assert s.expand(x*g-y*f-2*x*y*rho**2)==0
expanded=s.expand((-1+5*t*t+ef)-6*(t+e)*(t+e-m))
expected=-1-t*t+ef-12*t*e-6*e*e+6*m*t+6*m*e
assert s.expand(expanded-expected)==0
epsilon=s.Rational(1,20)
assert -1+epsilon+87*epsilon**2==-s.Rational(293,400)
assert s.Rational(1,2)-7*epsilon==s.Rational(3,20)
assert 12*s.Rational(1,240)==epsilon
# Completing the square bounds -t^2+18epsilon|t| by81epsilon^2.
u=s.symbols('u',nonnegative=True)
assert s.expand(-u*u+18*epsilon*u-81*epsilon**2+(u-9*epsilon)**2)==0
# General finite Fourier moment identity using formal Laurent polynomials.
a,b=s.symbols('a b',real=True);beta=a+s.I*b
moment_checks=[]
for degree in range(1,7):
    c=s.symbols('c0:'+str(degree+1),real=True)
    d=s.symbols('d0:'+str(degree+1),real=True)
    G=c[0]
    h_im=0
    for k in range(1,degree+1):
        gamma=c[k]+s.I*d[k]
        G+=gamma*z**k+s.conjugate(gamma)*z**(-k)
        h_im+=(beta**k*z**k-s.conjugate(beta)**k*z**(-k))/s.I
    mean=s.expand(G*h_im).coeff(z,0)
    target=sum(2*s.im((c[k]-s.I*d[k])*beta**k) for k in range(1,degree+1))
    assert s.simplify(mean-target)==0
    moment_checks.append(degree)
# Explicit boundary cancellation for G=sin(phi), alpha=+1,-1.
co,si=s.symbols('co si',real=True)
for sign in [-1,1]:
    numerator=2*sign*si**2;denominator=2-2*sign*co
    rem=s.rem(s.Poly(numerator-(sign+co)*denominator,si),s.Poly(si**2+co**2-1,si))
    assert rem.is_zero
result={'at':datetime.now(timezone.utc).isoformat(),'polar_identities':True,
 'robust_Lie_margin':'293/400','obstruction_margin':'3/20',
 'cartesian_coefficient_radius':'1/240','fourier_identity_degrees':moment_checks,
 'boundary_factor_examples':[-1,1],
 'scope':'Exact symbolic identities only; general factorization, dominated convergence and Lyapunov implications require the written proof and review. No grade.'}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
