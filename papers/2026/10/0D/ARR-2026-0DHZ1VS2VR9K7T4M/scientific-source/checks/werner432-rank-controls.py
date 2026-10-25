from pathlib import Path
import sympy as s,json
r=Path(__file__).resolve().parent;d,t,k=s.symbols('d t k',positive=True)
a3=1-3*t/d;b3=3*t*t/d-t**3;u3=a3+k*b3
a5=1-5*t/d+10*t*t/d**2;b5=-10*t**3/d**2+5*t**4/d-t**5;u5=a5+k*b5
assert s.expand(s.diff(u3,t)+3*k*(t-1/d)**2+3*(d-k)/d**2)==0
v3=s.factor(u3.subs(t,s.Rational(1,2)));v5=s.factor(u5.subs(t,s.Rational(1,2)))
assert s.expand(v3-((8-k)*d+6*(k-2))/(8*d))==0
assert s.expand(v5-((32-k)*d*d+(10*k-80)*d+80-40*k)/(32*d*d))==0
assert v3.subs({d:43,k:9})==-s.Rational(1,344)
assert v5.subs({d:245,k:33})==-s.Rational(3,384160)
beta5=s.Rational(17,16)-3/d+s.Rational(5,2)/d**2;gamma5=1-s.Rational(45,16)/d+s.Rational(5,2)/d**2
x=s.symbols('x',nonnegative=True)
assert s.expand(16*d*d*beta5-(17*(d-2)**2+20*(d-2)+12))==0
assert s.expand(16*d*d*gamma5-(16*(d-2)**2+19*(d-2)+14))==0
assert s.simplify(v5.subs(k,32)-15*(d-5)/(2*d*d))==0
out={'status':'PASS_EXACT_RANK_LADDER_SCALAR_CONTROLS','n3_rank9_d43_ratio':str(v3.subs({d:43,k:9})),'n3_rank9_d43_q':str(9*v3.subs({d:43,k:9})),'n5_rank33_d245_ratio':str(v5.subs({d:245,k:33})),'n5_rank33_d245_q':str(33*v5.subs({d:245,k:33})),'rank_boundaries':[{'d':i,'n5_max_k':min(i,int(s.floor((32*i*i-80*i+80)/(s.Integer(i*i-10*i+40)))))} for i in [2,3,13,38,39,43,100,244,245,1000]],'outside_CP_positive_polynomials':[str(s.expand(16*d*d*beta5)),str(s.expand(16*d*d*gamma5))],'scope':'Scalar identities only. The universal output-code block decomposition and CP complement require the proof and a separate audit, not these checks.'}
(r/'werner432-rank-controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
