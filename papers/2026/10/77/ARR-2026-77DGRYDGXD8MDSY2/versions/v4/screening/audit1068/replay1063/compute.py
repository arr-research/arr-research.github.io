from pathlib import Path
from fractions import Fraction
import datetime,hashlib,json,shutil
import mpmath as mp
import sympy as sp
P=Path(__file__).parent
mp.mp.dps=100
rows=[]
for d in [2,3,4,8,16,32,64,128,256,1024,65536]:
 dd=mp.mpf(d);e=1/dd;th=1-1/dd;lam=-1/(dd*dd-1);a=dd-1;q=a+e*e
 def stats(p):
  A=1+(dd*a-1)*p;F=1+a*p
  tr=(A+F*e*e)/(dd*q)
  det=e*e*(1-p)*(1+(dd*dd-1)*p)/(dd*dd*q*q)
  gap=mp.sqrt(tr*tr-4*det);hi=(tr+gap)/2;lo=det/hi
  ell=mp.log(hi/lo)/(hi-lo)
  return tr,det,hi,lo,ell
 T=stats(th);O=stats(lam*th);ratio=lam*lam*O[4]/T[4];csq=th*th*e*e*a/(q*q)
 du=4*csq*T[4];minimum=(1-th)*e*e/(dd*q)
 # Full state max is active-block hi: other Schmidt modes have (1-th)/(dq), and other coordinates no larger.
 assert T[2] >= (1-th)/(dd*q)
 condition=T[2]/minimum;bell=1/(dd*dd-1)
 rows.append(dict(d=d,retention=str(ratio),bell=str(bell),beats_bell=bool(ratio>bell),d_times_retention=str(dd*ratio),scaled_input=str(dd**3*du/mp.log(dd)),scaled_condition=str(condition/dd**5),scaled_distance=str(dd**mp.mpf('1.5')*2*mp.sqrt(csq)),input_trace=str(T[0]),scaled_input_det=str(dd**5*T[1]),scaled_output_trace=str(dd**3*O[0]),scaled_output_det=str(dd**7*O[1])))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='fixed high-precision scalar diagnostics, not interval/formal proof or reproducible campaign',precision=100,rows=rows,failures=[],score=None)
(P/'CHECK1063.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
