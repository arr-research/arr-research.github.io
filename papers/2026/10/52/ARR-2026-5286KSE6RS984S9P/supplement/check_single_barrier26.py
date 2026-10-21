from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).parent;out=R/'single-barrier-checks-26.json'
if out.exists():raise SystemExit('Refusing overwrite')
x,y,t=s.symbols('x y t',real=True);v=x+s.I*y;w=s.Rational(1,2)+s.I*t
assert s.simplify(s.re(w**3)-s.Rational(3,2)*s.re(w**2)+s.Rational(1,4))==0
assert s.simplify(s.re(v**3)-s.Rational(3,2)*s.re(v**2)-(x**3-s.Rational(3,2)*x**2-3*(x-s.Rational(1,2))*y**2))==0
assert s.simplify(s.re(w**4)-((t*t-s.Rational(3,4))**2-s.Rational(1,2)))==0
assert s.simplify(s.re(v**4)-(x**4-6*x*x*y*y+y**4))==0
assert s.Rational(6,65536)<s.Rational(1,64)
assert s.Rational(1,4)-s.Rational(1,256)-s.Rational(1,8)>0
assert (s.Rational(1,4)-s.Rational(1,256)-s.Rational(1,8))*3-s.Rational(1,4)-s.Rational(3,512)>0
rows=[]
for q in (16,17,20,50,100,1000,10000):
 n=s.Integer(q)**3
 lo=(n-1)/4-s.Rational(1,256)*q-s.Rational(3,512)/q**2
 fourth=q**4/s.Integer(16)-s.Rational(6,65536)/q**4-(n-1)/2
 assert lo>=n/8 and fourth>=q**4/s.Integer(64)
 rows.append(dict(n=int(n),third_margin=str(lo-n/8),fourth_margin=str(fourth-q**4/s.Integer(64))))
data=dict(created_at=datetime.now(timezone.utc).isoformat(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),exact_symbolic_checks='PASS',rational_threshold_cases=rows,scope='Symbolic identities and rational cases; complete universal bound rests on the analytic proof. No norm computation or manuscript score.')
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps(data,indent=2))
