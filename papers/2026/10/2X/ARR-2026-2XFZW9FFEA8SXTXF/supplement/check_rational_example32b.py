"""Exact rational elimination and Sturm checks; analytic reduction audited separately."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json
out=Path(__file__).resolve().parent/'rational-checks-32b.json'
assert not out.exists(),'Preserve output; execute a copy in a fresh directory.'
c,x,y,t=s.symbols('c x y t');C=s.Rational(25,4)
D=s.expand(18*c*x*y-(c*c-1-x*x+y*y)**2-4*(c+x*y)**2)
assert D.subs({c:1,x:1,y:s.Rational(3,5)})==s.Rational(94,625)
g1real=x*x-y*y;g1imag=2*x*y
disk=(s.Rational(3,2)*c)**2-(g1real-(c*c-1))**2-(g1imag-s.Rational(5,2)*c)**2
assert s.expand(disk-D)==0
polys=[D,s.diff(D,x),4*s.diff(D,y)-25*s.diff(D,c),4*t-4*c-25*y]
G=s.groebner(polys,x,c,y,t,order='grevlex');assert G.is_zero_dimensional
L=G.fglm('lex')
R=16777216*t**12-8141930496*t**10+1537904087040*t**8-104707265987520*t**6+2126206939995165*t**4-15011745808074246*t**2+81397225546445341
E=t*t*(4*t-25)**2*(4*t+25)**2*(t*t+1)**2*R
assert s.expand(L.polys[-1].as_expr()-E)==0
assert G.reduce(E)[1]==0
assert all(L.reduce(p)[1]==0 for p in polys)
lo=s.Rational(4592782689292,10**12);hi=s.Rational(4592782689293,10**12)
P=s.Poly(R,t)
assert P.count_roots(0,s.Rational(19,4))==1
assert P.count_roots(lo,hi)==1
assert R.subs(t,lo)>0 and R.subs(t,hi)<0
X,Y,a=s.symbols('X Y a');rho=X*X+Y*Y;H=rho+s.Rational(3,5)*(X*X-Y*Y);K=(-a+s.Rational(5,4))*H+3*(X*X-Y*Y)
vf1=K*X-H*Y;vf2=K*Y+H*X
assert s.expand(X*vf1+Y*vf2-K*rho)==0
assert s.expand(X*vf2-Y*vf1-H*rho)==0
data={'created_at':datetime.now(timezone.utc).isoformat(),'scope':'Exact rational algebra, Groebner/FGLM elimination, Sturm root counting and polar identities. The analytic proof of reduction/compactness is separate.','rational_feasible_witness':{'c':'1','x':'1','y':'3/5','D':'94/625','t':'19/4'},'disk_identity':True,'critical_system':[str(p) for p in polys],'zero_dimensional':True,'exact_elimination_factorization':str(E),'R_coefficients':P.all_coeffs(),'groebner_E_remainder_zero':True,'original_equations_reduce_zero_in_lex_basis':True,'sturm_count_0_to_19over4':1,'sturm_count_isolating_interval':1,'t_interval':[str(lo),str(hi)],'A_interval':[str(C-hi),str(C-lo)],'A_decimal_interval':['1.657217310707','1.657217310708'],'polar_identities':2}
data['R_coefficients']=[int(k) for k in data['R_coefficients']]
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(data,indent=2))
