"""High-precision checks of explicit uniform remainder envelopes, not a capacity proof."""
import mpmath as mp
import hashlib,json
from pathlib import Path
mp.mp.dps=220 # Resolve E-1 and g(E)-g(E-1) even at the largest E=1e100.
def h(x):return -x*mp.log(x,2)-(1-x)*mp.log(1-x,2) if 0<x<1 else mp.mpf(0)
def b(u,v):return (u+v)*h(u/(u+v)) if u+v else mp.mpf(0)
def g(e):return mp.log(e+1,2)+e*mp.log1p(1/e)/mp.log(2)
rows=[];cases=0
for es in ('2','10','1000','1e6','1e20','1e100'):
 E=mp.mpf(es);A=mp.log(E+1,2);G=g(E);p0=1/(E+1)
 m=int(mp.floor(E/mp.log(E+1)));Lm=mp.log(m+1,2)
 dp=1-Lm/A;dm=min(mp.mpf(1),(G-A+1)/G)
 for ls in ('.01','.1','.5','.9','.99'):
  lam=mp.mpf(ls);q=1-lam;c=(1+h(lam)/(2*lam))/A;rr=min(1,c)
  J=min(h(lam),h(q*rr**2)) if q*rr**2<=mp.mpf('.5') else h(lam)
  minus=q*h(p0)+J
  # Evaluate truncation tail using expm1/log1p to avoid catastrophic cancellation.
  logr=mp.log1p(-1/E);L=mp.ceil(4*E*mp.log(E+1));eps=mp.exp(L*logr)
  # Exact gap computed without subtracting two large thermal entropies.
  gap=g(E)-g(E-1)-mp.log1p(-eps)/mp.log(2)+L*eps/(1-eps)*(-logr/mp.log(2))
  assert gap>=0
  plus=2*lam*gap+b(min(lam,lam*(m+1)/(E*(1-eps))),q)
  for B in (0,mp.mpf('.1'),1,A/2,A,G,G+1,100*G):
   t=min(1,B/A);a=min(1,max(0,(B-1)/G));upper=min(1,B/Lm)
   assert -mp.mpf('1e-60')<=t-a<=dm+mp.mpf('1e-60')
   assert -mp.mpf('1e-60')<=upper-t<=dp+mp.mpf('1e-60')
   assert b(lam,q*t)-b(lam,q*a)<=b(lam,q*dm)+mp.mpf('1e-60')
   assert b(lam,q*upper)-b(lam,q*t)<=b(lam,q*dp)+mp.mpf('1e-60')
   cases+=1
  rows.append(dict(E=es,lam=ls,shannon_lower_error=str(minus+b(lam,q*dm)),shannon_upper_error=str(plus+b(lam,q*dp))))
root=Path(__file__).parent
result={'status':'PASS','precision_digits':mp.mp.dps,'cases':cases,'scope':'Scalar remainder and clipping diagnostics only; not capacities, coding or formal proof','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
(root/'bounds585.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
