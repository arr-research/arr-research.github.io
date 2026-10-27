from pathlib import Path
from fractions import Fraction
import datetime,json,hashlib,shutil
import sympy as s
P=Path(__file__).parent
src=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1054-audit\integer_intervals1054.py');prefix=src.read_text().split('rows=[]')[0]
(P/'reused_integer_prefix1054.py').write_text(prefix,encoding='utf-8');ns={'__file__':str(P/'reused_integer_prefix1054.py')};exec(prefix,ns)
iv,saved,log=ns['iv'],ns['saved'],ns['log'];rows=[]
for t in [Fraction(1),Fraction(1,4)]:
 for beta in [2,4]:
  for d in [2,3,4,8,16,32,64,128,1024]:
   x=t/d;theta=1-Fraction(1,d**beta);lam=-Fraction(1,d*d-1);a=d-1;q=a+x;csq=theta*theta*x*a/(q*q)
   def plane(p):
    A=1+(d*a-1)*p;F=1+a*p;tr=(A+F*x)/(d*q);det=x*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
    delta=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+delta)/2;lo=iv(det)/hi;ell=(log(hi)-log(lo))/delta
    return hi,lo,delta,ell
   hi,lo,delta,ell=plane(lam*theta);_,_,_,ellin=plane(theta)
   b2=iv(lam*lam*csq);p0=lo+4*b2/delta;q0=lo
   assert q0.l>0 and p0.l>q0.h and p0.h<ns['S']
   db=p0*log(p0/q0)+(1-p0)*log((1-p0)/(1-q0));duout=4*b2*ell;duin=4*iv(csq)*ellin
   gain=db/duin;gap=gain-iv(Fraction(1,d*d-1));fraction=db/duout
   # A directed interval may overlap1; reject only a proved DPI violation.
   assert db.l>0 and fraction.l<=ns['S']
   rows.append(dict(d=d,t=str(t),beta=beta,p0=saved(p0),q0=saved(q0),binary_D=saved(db),fraction_of_quantum_output=saved(fraction),measured_output_over_quantum_input=saved(gain),gap_over_Bell=saved(gap),positive=gap.l>0,negative=gap.h<0))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='own fixed scalar certificates linked to analytic ambient projector; no actual experiment, external audit or sample-complexity theorem',method='768bit directed integer arithmetic reused1054, not independent implementation',source1054_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),cases=rows,adverse=[dict(d=r['d'],t=r['t'],beta=r['beta']) for r in rows if r['negative']],score=None)
(P/'CONTROL1070.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
