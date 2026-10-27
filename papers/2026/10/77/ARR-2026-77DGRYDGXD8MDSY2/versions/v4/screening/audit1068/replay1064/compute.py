from pathlib import Path
from fractions import Fraction
import datetime,hashlib,json,shutil
import mpmath as mp
import sympy as sp
P=Path(__file__).parent
src=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1054-audit\integer_intervals1054.py')
prefix=src.read_text().split('rows=[]')[0]
(P/'reused_integer_prefix1054.py').write_text(prefix,encoding='utf-8')
ns={'__file__':str(P/'reused_integer_prefix1054.py')};exec(prefix,ns)
iv,plane,saved=ns['iv'],ns['plane'],ns['saved']
rows=[]
for d in [2,3,4,8,16,32,64,128]:
 e=Fraction(1,d);th=1-e;lam=-Fraction(1,d*d-1);a=d-1;q=a+e*e
 ei,hi,lo,ti,di=plane(d,th,e);eo,ho,lowo,to,do=plane(d,lam*th,e)
 ratio=iv(lam*lam)*eo/ei;bell=iv(Fraction(1,d*d-1));gap=ratio-bell
 ci=th*th*e*e*a/(q*q);din=4*iv(ci)*ei;emin=(1-th)*e*e/(d*q);cond=hi/iv(emin)
 rows.append(dict(d=d,ratio=saved(ratio),gap=saved(gap),positive_gap=gap.l>0,negative_gap=gap.h<0,input=saved(din),condition=saved(cond),min_eigenvalue_exact=str(emin),order_exact=str(1+(d*d-1)*th)))
assert [r['d'] for r in rows if r['negative_gap']]==[2,3,4]
assert all(r['positive_gap'] for r in rows if r['d']>=8)
d=sp.symbols('d',positive=True);e=1/d;th=1-1/d;lam=-1/(d*d-1);a=d-1;q=a+e*e
def rational(p):
 A=1+(d*a-1)*p;F=1+a*p
 return sp.factor((A+F*e*e)/(d*q)),sp.factor(e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q))
ti,di=rational(th);to,do=rational(lam*th);ci=th*th*e*e*a/(q*q);emin=(1-th)*e*e/(d*q)
exprs=dict(input_trace=ti,input_det_scaled=d**5*di,output_trace_scaled=d**3*to,output_det_scaled=d**7*do,physical_coherence_squared_scaled=d**3*ci,minimum_scaled=d**5*emin,lambda_squared_scaled=d**4*lam**2)
expected=[1,1,2,1,1,1,1];limits={k:str(sp.limit(v,d,sp.oo)) for k,v in exprs.items()}
assert [int(x) for x in limits.values()]==expected
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='own supplemental controls of1063; no external audit, grade, priority or formal-proof-assistant claim',method='768bit directed integer intervals; reused1054 arithmetic, same implementation lineage and not independent; exact SymPy rational limits',source1054_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),rational_expressions={k:str(sp.factor(v)) for k,v in exprs.items()},exact_rational_limits=limits,cases=rows,adverse_dimensions=[2,3,4])
(P/'CONTROL1064.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
