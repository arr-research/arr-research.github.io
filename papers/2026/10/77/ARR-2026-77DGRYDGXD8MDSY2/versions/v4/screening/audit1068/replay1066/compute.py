from pathlib import Path
from fractions import Fraction
import datetime,hashlib,json,shutil
import mpmath as mp
import sympy as sp
P=Path(__file__).parent
src=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1054-audit\integer_intervals1054.py');prefix=src.read_text().split('rows=[]')[0]
(P/'reused_integer_prefix1054.py').write_text(prefix,encoding='utf-8');ns={'__file__':str(P/'reused_integer_prefix1054.py')};exec(prefix,ns)
iv,plane,saved=ns['iv'],ns['plane'],ns['saved'];rows=[]
# plane contains e only through eÂ²; setting e=sqrt(t/d) symbolically is avoided by evaluating the rational formulas directly.
def rational_plane(d,p,x):
 a=d-1;q=a+x;A=1+(d*a-1)*p;F=1+a*p;tr=(A+F*x)/(d*q);det=x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 z=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+z)/2;lo=iv(det)/hi;ell=(ns['log'](hi)-ns['log'](lo))/z
 return ell,hi,tr,det
for t in [Fraction(1),Fraction(1,4)]:
 for beta in [2,4]:
  for d in [2,3,4,8,16,32,64,128]:
   x=t/d;th=1-Fraction(1,d**beta);lam=-Fraction(1,d*d-1);a=d-1;q=a+x
   ei,hi,ti,di=rational_plane(d,th,x);eo,ho,to,do=rational_plane(d,lam*th,x)
   ratio=iv(lam*lam)*eo/ei;gap=ratio-iv(Fraction(1,d*d-1));ci=th*th*x*a/(q*q)
   rows.append(dict(d=d,t=str(t),beta=beta,ratio=saved(ratio),gap=saved(gap),positive=gap.l>0,negative=gap.h<0,input=saved(4*iv(ci)*ei),condition=saved(hi/iv((1-th)*x/(d*q)))))
d=sp.symbols('d',positive=True);limits=[]
for t in [sp.Integer(1),sp.Rational(1,4)]:
 for beta in [2,4]:
  x=t/d;theta=1-d**(-beta);lam=-1/(d*d-1);a=d-1;q=a+x;nu=beta+3
  def td(p):return sp.factor((1+(d*a-1)*p+(1+a*p)*x)/(d*q)),sp.factor(x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q))
  ti,di=td(theta);to,do=td(lam*theta)
  expr=[ti,d**nu*di,d**3*to,d**(nu+2)*do,d**2*theta**2*x*a/q**2,d**nu*(1-theta)*x/(d*q)]
  vals=[sp.limit(v,d,sp.oo) for v in expr];assert vals==[1,t,1+t,t,t,t]
  limits.append(dict(t=str(t),beta=beta,limits=list(map(str,vals)),predicted_dR=str(sp.Rational(nu-4,nu)/(1+t)),input_constant=str(4*t*nu)))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='own rational-limit and directed-integer controls; same interval implementation lineage1054, no external audit',source1054_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),limits=limits,cases=rows,adverse=[dict(d=r['d'],t=r['t'],beta=r['beta']) for r in rows if r['negative']],uncertain=[dict(d=r['d'],t=r['t'],beta=r['beta']) for r in rows if not r['negative'] and not r['positive']],score=None)
(P/'CONTROL1066.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
