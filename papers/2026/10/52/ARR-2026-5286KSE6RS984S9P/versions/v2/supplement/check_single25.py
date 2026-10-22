from pathlib import Path
from datetime import datetime,timezone
import sympy as sp,mpmath as mp,json,hashlib
root=Path(__file__).parent;out=root/'single-checks-25.json'
if out.exists():raise SystemExit('Refusing overwrite')
a,c,s=sp.symbols('a c s',real=True)
D=-30*a-4*c-17;T=-15*a/(1-a)-2*c/(1-c)
base={a:-sp.Rational(2,3),c:sp.Rational(3,4)}
J=sp.Matrix([D,T]).jacobian([a,c]).subs(base)
assert J.det()==sp.Rational(4692,5) and D.subs(base)==T.subs(base)==0
H=(1-sp.Rational(6,5)*s)**30*(1-8*s)**4
assert sp.diff(H,s).subs(s,sp.Rational(5,24))==0
assert H.subs(s,sp.Rational(5,24))==(sp.Rational(3,4))**30*sp.Rational(2,3)**4
assert sp.diff(H,s).subs(s,0)==-68
y=sp.symbols('y',real=True);v=sp.Rational(1,2)+sp.I*y
assert sp.simplify(2*sp.re(v**3)-sp.Rational(3,2)*2*sp.re(v**2)+sp.Rational(1,2))==0
mp.mp.dps=100;rows=[]
for n0 in (10**6,10**9):
 for k in (0,1,7,17,32,33):
  m=(n0-1)//34;n=34*m+k+1
  vv=mp.findroot(lambda v:v**3-mp.mpf('1.5')*v**2-mp.mpf(n-1)/4,mp.root(mp.mpf(n-1)/4,3)+mp.mpf('.5'),tol=mp.mpf('1e-90'))
  tarD=(vv**2/(vv-1)-mp.mpf(k)/2)/m;tarT=(-vv**2-mp.mpf(k)/4)/m
  aa,cc=mp.findroot(lambda aa,cc:(-30*aa-4*cc-17-tarD,-15*aa/(1-aa)-2*cc/(1-cc)-tarT),(-mp.mpf(2)/3,mp.mpf(3)/4),tol=mp.mpf('1e-90'))
  errD=m*(-30*aa-4*cc-17)+mp.mpf(k)/2-vv**2/(vv-1)
  err2=m*(-15*aa/(1-aa)-2*cc/(1-cc))+mp.mpf(k)/4+vv**2
  err3=vv**3-mp.mpf('1.5')*vv**2-mp.mpf(n-1)/4
  assert max(abs(errD),abs(err2),abs(err3))<mp.mpf('1e-75')
  assert -1<aa<1 and -1<cc<1 and 0<1-1/vv<1
  rows.append(dict(n=n,m=m,k=k,v=mp.nstr(vv,50),a=mp.nstr(aa,50),c=mp.nstr(cc,50),root=mp.nstr(1-1/vv,50),max_equation_error=mp.nstr(max(abs(errD),abs(err2),abs(err3))),scope='Finite high-precision equation/geometry diagnostics, not certified inequalities or full integrals.'))
data=dict(created_at=datetime.now(timezone.utc).isoformat(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),jacobian_determinant='4692/5',exact_symbolic_checks='PASS',cases=rows,quadrature_performed=False)
out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exact_symbolic_checks='PASS',cases=len(rows),output=str(out))))
