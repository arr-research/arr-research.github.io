from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,traceback
C=Path(__file__).parent
sp=importlib.util.spec_from_file_location('own1077',C/'integer_arithmetic1077.py');lib=importlib.util.module_from_spec(sp);sp.loader.exec_module(lib)
iv,log,S,saved=lib.iv,lib.log,lib.S,lib.saved
def plane(a,b,c2):
 tr=a+b;det=a*b-c2;assert tr>0 and det>0
 gap=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+gap)/2;lo=iv(det)/hi
 return hi,lo,gap,(log(hi)-log(lo))/gap
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
# Fixed predeclared grid. All outcomes retained; no threshold-driven rerun.
cases=[(3,k) for k in [8,16,32,64,128,256]]+[(4,16),(4,64),(10,64)]
rows=[]
try:
 for n,k in cases:
  beta=F(1,4*n*k);delta=F(1,2**k);eps=beta*delta
  alpha=F(1,n)-(n-2)*eps-beta;c2=alpha*beta*(1-delta)
  lam=-F(1,n-1);ap=(alpha+n*(n-2)*eps)/(n-1)**2
  assert alpha>0 and c2>0 and alpha*beta-c2==alpha*beta*delta
  assert ap*beta-lam*lam*c2==beta*delta*(alpha+n*(n-2)*beta)/(n-1)**2
  hi,li,gi,ellin=plane(alpha,beta,c2);ho,lo,go,ellout=plane(ap,beta,lam*lam*c2)
  assert li.h<iv(eps).l<hi.l
  din=4*n*iv(c2)*ellin;dout=4*n*iv(lam*lam*c2)*ellout
  q=n*lo;p=n*(lo+4*iv(lam*lam*c2)/go)
  assert 0<q.l<q.h<p.l<p.h<S
  dm=kl(p,q);ret=dm/din;qr=dout/din;gap=ret-iv(F(1,n-1))
  assert dm.l>0 and gap.l>0 and ret.h<qr.l and qr.h<S
  rows.append(dict(n=n,k=k,beta=str(beta),epsilon=str(eps),delta=str(delta),alpha=str(alpha),coherence_squared=str(c2),input_Umegaki=saved(din),output_Umegaki=saved(dout),binary_D=saved(dm),measured_retention=saved(ret),quantum_retention=saved(qr),strict_measured_gap=saved(gap),p=saved(p),q=saved(q),input_condition=saved(hi/li),input_trace_distance=saved(2*n*iv(c2).sqrt()),condition_normalized=saved((hi/li)/(4*k*2**k)),input_D_over_log2=saved(din/log(iv(2))),binary_D_over_log2=saved(dm/log(iv(2)))))
 (C/'CONTROL1110.json').write_text(json.dumps({'scope':'9 predeclared integer-directed interval cases, reused1077 library; no float establishes signs, no external audit yet','cases':rows},indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'certified':len(rows),'first':rows[0]['measured_retention']['decimal_display_only'],'n3_k256':rows[5]['measured_retention']['decimal_display_only'],'inputD_k256':rows[5]['input_Umegaki']['decimal_display_only'],'binaryD_k256':rows[5]['binary_D']['decimal_display_only']}))
except Exception as e:
 (C/'FAILURE1110.json').write_text(json.dumps({'exception':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise
