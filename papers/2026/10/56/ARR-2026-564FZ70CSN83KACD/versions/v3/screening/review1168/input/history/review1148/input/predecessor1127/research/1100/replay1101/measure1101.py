from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,traceback
C=Path(__file__).parent
sp=importlib.util.spec_from_file_location('own_interval1077',C/'integer_arithmetic1077.py');lib=importlib.util.module_from_spec(sp);sp.loader.exec_module(lib)
iv,saved,S,log=lib.iv,lib.saved,lib.S,lib.log
def plane(a,b,c2):
 tr=a+b;det=a*b-c2;assert tr>0 and det>0
 g=iv(tr*tr-4*det).sqrt();h=(iv(tr)+g)/2;l=iv(det)/h
 return h,l,g,(log(h)-log(l))/g
def kl(p,q):return p*log(p/q)+(1-p)*log((1-p)/(1-q))
cases=[(n,z) for n in [3,10,100,10000] for z in [4,12]]+[(3,8)]
rows=[]
try:
 for n,z in cases:
  beta=F(1,n**5);eps=F(1,n**(z+4));delta=F(1,n**z);alpha=F(1,n)-(n-2)*eps-beta
  assert alpha>0 and eps>0 and delta<1
  lam=-F(1,n-1);ap=(alpha+n*(n-2)*eps)/(n-1)**2;c2=alpha*beta*(1-delta)
  epout=(n*alpha+(n*n-3*n+1)*eps)/(n-1)**2;assert epout>0
  hi,li,gi,ei=plane(alpha,beta,c2);ho,lo,go,eo=plane(ap,beta,lam*lam*c2)
  assert li.h<iv(eps).l<hi.l
  din=4*n*iv(c2)*ei;dout=4*n*iv(lam*lam*c2)*eo
  q=n*lo;p=n*(lo+4*iv(lam*lam*c2)/go)
  assert 0<q.l<q.h<p.l<p.h<S
  measured=kl(p,q);ret=measured/din;qr=dout/din;fraction=measured/dout;gap=ret-iv(F(1,n-1))
  assert measured.l>0 and gap.l>0 and fraction.h<S and qr.h<S
  normdu=din/(4*(z+4)*log(iv(n))/n**4)
  rows.append(dict(n=n,z=z,alpha=str(alpha),beta=str(beta),epsilon=str(eps),delta=str(delta),coherence_squared=str(c2),input_Umegaki=saved(din),output_Umegaki=saved(dout),binary_D=saved(measured),q_under_sigma=saved(q),p_under_rho=saved(p),quantum_retention=saved(qr),measured_retention=saved(ret),fraction_of_output=saved(fraction),ordinary=str(F(1,n-1)),strict_measured_gap=saved(gap),input_condition=saved(hi/li),normalized_input_asymptotic=saved(normdu),limits=dict(quantum_retention=str(F(z+2,z+4)),measured_retention=str(F(z,z+4)),binary_fraction=str(F(z,z+2))),label_only_and_reference_only_tests='identical marginals, zero distinguishability'))
 out={'scope':'9 predeclared finite integer interval cases. No floating point establishes a sign; original1077 primitives reused, not independent implementation. General asymptotic proof remains root candidate, no external audit or grade.','cases':rows,'input_geometry':'n-symbol classical register, n-dimensional quantum reference; CQ separable pairs; no postselection; two-outcome effect controlled by classical output label'}
 (C/'MEASUREMENT1101.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'certified_cases':len(rows),'all_measured_gaps_positive':True,'n3z4_measured':rows[0]['measured_retention']['decimal_display_only'],'n3z4_inputD':rows[0]['input_Umegaki']['decimal_display_only']}))
except Exception as e:
 (C/'FAILURE1101.json').write_text(json.dumps({'error':repr(e),'traceback':traceback.format_exc(),'completed':rows},indent=2)+'\n',encoding='utf-8');raise
