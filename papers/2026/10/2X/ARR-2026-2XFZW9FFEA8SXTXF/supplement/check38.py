from pathlib import Path
from datetime import datetime, timezone
from math import isqrt
import json
import sympy as s

R=Path(__file__).resolve().parent
z=s.symbols('z'); rt=s.sqrt(3); a=-2+rt; b=-2-rt
D=z*z+4*z+1
assert s.simplify(2/D-(1/rt/(z-a)-1/rt/(z-b)))==0
assert s.simplify(4*z/D**2-(2/(3*rt)/(z-a)+(a/3)/(z-a)**2-2/(3*rt)/(z-b)+(b/3)/(z-b)**2))==0
assert s.simplify(s.diff(4*z/(z-b)**2,z).subs(z,a)-2/(3*rt))==0

# Certified rational enclosure, not a floating root finder.
k=32; den=2**k; low=s.Rational(isqrt(3*den*den),den); high=low+s.Rational(1,den)
assert low**2<3<high**2
at=-2+(low+high)/2; delta=s.Rational(1,den)
assert -s.Rational(1,2)<at<0

def pos(v):
    v=s.radsimp(s.expand_complex(s.simplify(v)))
    A=s.simplify(s.expand(v).coeff(rt,0)); B=s.simplify(s.expand(v).coeff(rt,1))
    assert s.simplify(v-A-B*rt)==0 and A.is_Rational and B.is_Rational, v
    if B==0:return A>0
    if A==0:return B>0
    if A>0 and B>0:return True
    if A<0 and B<0:return False
    return A*A>3*B*B if A>0 else 3*B*B>A*A

def norm2(v):return s.simplify(s.expand_complex(v*s.conjugate(v)))
assert pos(delta**2-(a-at)**2)
funcs=[('simple',[(0,0,-1/rt),(a,0,1/rt)],[(0,0,-1/(at+2)),(at,0,1/(at+2))],20*delta),
       ('double',[(0,0,-2/(3*rt)),(a,0,2/(3*rt)),(a,1,a/3)],[(0,0,-2/(3*(at+2))),(at,0,2/(3*(at+2))),(at,1,at/3)],68*delta)]
tests=[]; coeffchecks=0
ts=[s.S(0),s.S(1),s.S(-1),s.I,-s.I,(3+4*s.I)/5,(-5+12*s.I)/13,s.Rational(1,2),(1+s.I)/3]
for name, exact, approx, bound in funcs:
    assert s.simplify(sum(c for w,p,c in exact if p==0))==0
    assert s.simplify(sum(c for w,p,c in approx if p==0))==0
    for (_,p,c),(_,pt,ct) in zip(exact,approx):
        assert p==pt and pos((2*delta)**2-norm2(c-ct)); coeffchecks+=1
    for t in ts:
        H=lambda w,p:(1+t*w)/(1-t*w) if p==0 else 2*t/(1-t*w)**2
        ev=sum(c*H(w,p) for w,p,c in exact)
        av=sum(c*H(w,p) for w,p,c in approx)
        assert pos(bound**2-norm2(ev-av)),(name,t)
        tests.append({'functional':name,'cayley_parameter':str(t),'certified_error_bound':str(bound),'exact_Qsqrt3_comparison':True})

# General residue recurrence at rational and algebraic repeated poles.
cases=[]
for pole,mult,N,Q in [
    (a,1,2,D), (a,2,4*z,D**2),
    (s.Rational(1,3)+s.I/4,3,z*z+2*z+3,(z-(s.Rational(1,3)+s.I/4))**3*(z-2)),
    (s.S(0),4,z*z+1,z**4*(z-2)**2)]:
    e=[s.simplify(s.diff(Q,z,mult+j).subs(z,pole)/s.factorial(mult+j)) for j in range(mult)]
    num=[s.simplify(s.diff(N,z,j).subs(z,pole)/s.factorial(j)) for j in range(mult)]
    t=[]
    for j in range(mult):t.append(s.simplify((num[j]-sum(e[h]*t[j-h] for h in range(1,j+1)))/e[0]))
    E=s.cancel(Q/(z-pole)**mult,extension=rt)
    for p in range(mult):
        independent=s.diff(N/E,z,mult-1-p).subs(z,pole)/s.factorial(mult-1-p)
        assert s.simplify(t[mult-1-p]-independent)==0
    cases.append({'pole':str(pole),'multiplicity':mult,'coefficients':[str(v) for v in t],'verified':True})

out={'at':datetime.now(timezone.utc).isoformat(),'status':'all_exact_diagnostics_passed',
     'partial_fraction_identities':2,'double_residue_derivative_identity':True,
     'sqrt3_rational_bracket':[str(low),str(high)],'coefficient_error_checks':coeffchecks,
     'uniform_error_kernel_checks':tests,'residue_recurrence_cases':cases,
     'general_complexity_proof_not_machine_verified':True,'GLS_or_root_isolation_solver_not_implemented':True}
(R/'checks-38.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'kernel_checks':len(tests),'residue_cases':len(cases)}),flush=True)
