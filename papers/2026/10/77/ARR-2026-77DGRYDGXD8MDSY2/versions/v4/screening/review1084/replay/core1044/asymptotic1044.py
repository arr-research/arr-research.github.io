from pathlib import Path
import sympy as s, json
P=Path(__file__).parent
d,p=s.symbols('d p',real=True);a=d-1;M=d*(2*d-1)/2;Q=d*a
A=1+(Q-1)*p;C=2+(d-2)*p
high=A/(2*d*a)
low=s.factor((A*C-d*d*p*p*a)/(2*d*a*A))
assert s.factor(low-(1-p)*(1+(M-1)*p)/(d*a*A))==0
angle=d*p*s.sqrt(a)/A
zh=s.simplify(2*s.sqrt(a)*angle)
zl=s.simplify(2-zh)
assert s.factor(zl-2*(1-p)/A)==0
log_coefficient=s.factor(4*a/high)
assert s.factor(log_coefficient-8*d*a*a/A)==0
lam=s.symbols('lambda',real=True);theta=s.symbols('theta',real=True)
ratio=s.factor(lam**2*log_coefficient.subs(p,lam*theta)/log_coefficient.subs(p,theta))
assert s.factor(ratio-lam**2*(1+(Q-1)*theta)/(1+lam*(Q-1)*theta))==0
cp=-1/(d*d-1)
assert s.factor(A.subs(p,cp)-d/(d*d-1))==0
assert s.factor((1+(M-1)*p).subs(p,cp)-d/(2*(d*d-1)))==0
def c(k):return lam**2*k/(1+lam*(k-1))
assert s.factor(c(Q).subs(lam,cp)-1/(d+1))==0
assert s.factor(c(d*d/2).subs(lam,cp)-1/(d*d-1))==0
out={'scope':'General symbolic coefficients supporting the separately reconstructed fixed-p BKM expansion; not a numerical universal proof',
 'large_eigenvalue_leading':str(high),'small_eigenvalue_coefficient_of_e2':str(low),
 'rotation_coefficient_of_e':str(angle),'Z_high_diagonal_coefficient_of_e':str(zh),
 'Z_low_diagonal_coefficient_of_e':str(zl),'H_coefficient_of_log_1_over_e':str(log_coefficient),
 'limiting_ratio':str(ratio),'CP_A_positive_for_d_ge_2':str(s.factor(A.subs(p,cp))),
 'CP_M_denominator_positive_for_d_ge_2':str(s.factor((1+(M-1)*p).subs(p,cp))),
 'CP_lower':str(s.factor(c(Q).subs(lam,cp))),'CP_Bell_endpoint':str(s.factor(c(d*d/2).subs(lam,cp))),
 'all_assertions_passed':True}
(P/'ASYMPTOTIC1044.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
