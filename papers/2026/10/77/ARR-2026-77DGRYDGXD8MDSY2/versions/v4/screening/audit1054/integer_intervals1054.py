"""Own directed dyadic interval arithmetic, exact integers only.
No mpmath or floating point is used for any bound. Log by range reduction
and positive atanh series with an explicit remainder. Rational nonsymmetric
2x2 coordinates are similar to the symmetric normalized principal plane.
"""
from pathlib import Path
from math import isqrt
from fractions import Fraction
from decimal import Decimal,localcontext
import json,traceback
P=Path(__file__).parent;BITS=768;S=1<<BITS;N=400
def ceildiv(n,d):return -((-n)//d)
class I:
 def __init__(self,l,h):assert l<=h;self.l=l;self.h=h
 @staticmethod
 def q(n,d=1):
  assert d>0;return I((n*S)//d,ceildiv(n*S,d))
 def __neg__(self):return I(-self.h,-self.l)
 def __add__(self,o):
  o=o if isinstance(o,I) else I.q(o);return I(self.l+o.l,self.h+o.h)
 __radd__=__add__
 def __sub__(self,o):return self+(-o if isinstance(o,I) else -o)
 def __rsub__(self,o):return -self+o
 def __mul__(self,o):
  o=o if isinstance(o,I) else I.q(o);v=[self.l*o.l,self.l*o.h,self.h*o.l,self.h*o.h];return I(min(v)//S,ceildiv(max(v),S))
 __rmul__=__mul__
 def recip(self):
  assert self.l>0 or self.h<0;return I((S*S)//self.h,ceildiv(S*S,self.l))
 def __truediv__(self,o):return self*(o if isinstance(o,I) else I.q(o)).recip()
 def __rtruediv__(self,o):return (o if isinstance(o,I) else I.q(o))*self.recip()
 def square(self):
  if self.l>=0:return I((self.l*self.l)//S,ceildiv(self.h*self.h,S))
  if self.h<=0:return (-self).square()
  return I(0,ceildiv(max(self.l*self.l,self.h*self.h),S))
 def sqrt(self):
  assert self.l>=0;lo=isqrt(self.l*S);hi=isqrt(self.h*S);return I(lo,hi if hi*hi==self.h*S else hi+1)
def atanh2(u):
 assert 0<=u.l<=u.h<=S//2
 u2=u.square();term=u;ans=I.q(0)
 for j in range(N):ans+=term/(2*j+1);term*=u2
 # remainder <=4/[3(2N+1)2^(2N)], for 0<=u<=1/2.
 tail=I.q(4,3*(2*N+1)*(1<<(2*N)))
 return I(2*ans.l,2*ans.h+tail.h)
LOG2=atanh2(I.q(1,3))
def log(x):
 assert x.l>0;k=x.l.bit_length()-1-BITS
 m=x/I.q(1<<k) if k>=0 else x*(1<<(-k))
 u=(m-1)/(m+1);return atanh2(u)+k*LOG2

def iv(x):
 x=Fraction(x);return I.q(x.numerator,x.denominator)
def binary(t):
 sign,man,exp,bc=map(int,t)
 return Fraction((-1 if sign else 1)*man*(1<<exp),1) if exp>=0 else Fraction((-1 if sign else 1)*man,1<<(-exp))
def saved(x):
 with localcontext() as c:
  c.prec=50;display=[str(Decimal(x.l)/Decimal(S)),str(Decimal(x.h)/Decimal(S))]
 return {'lo_integer':str(x.l),'hi_integer':str(x.h),'denominator_power_of_2':BITS,'decimal_display_only':display}
def plane(d,p,e):
 a=d-1;q=a+e*e;A=1+(d*a-1)*p;F=1+a*p;tr=(A+F*e*e)/(d*q);det=e*e*(1-p)*(1+(d*d-1)*p)/(d*d*q*q)
 assert tr>0 and det>0
 z=iv(tr*tr-4*det).sqrt();hi=(iv(tr)+z)/2;lo=iv(det)/hi;ell=(log(hi)-log(lo))/z
 return ell,hi,lo,tr,det
rows=[]
source=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_local-phase1051\INTERVAL1051.json').read_text())['rows']
for d in [3,4]:
 for e in [Fraction(1,100),Fraction(1,1000)]:
  th=Fraction(99,100);lam=-Fraction(1,d*d-1);a=d-1;q=a+e*e;ci=th*th*e*e*a/(q*q)
  ei,hi,lo,ti,di=plane(d,th,e);eo,ho,lowo,to,do=plane(d,lam*th,e)
  ratio=iv(lam*lam)*eo/ei;bench=iv(Fraction(1,d*d-1));gap=ratio-bench;din=4*iv(ci)*ei;dout=4*iv(lam*lam*ci)*eo
  assert gap.l>0 and din.l>0 and dout.l>0
  # The exact smallest ambient eigenvalue is attained on off-Schmidt coordinates with R label0.
  emin=(1-th)*e*e/(d*q);condition=hi/iv(emin);distance=2*iv(th*e/q)*I.q(a).sqrt();sld=iv(4*ci/ti)
  ref=next(x for x in source if x['d']==d and x['e']==str(e));contained={}
  for key,value in [('ratio',ratio),('gap',gap),('input',din)]:
   l,h=map(binary,ref['exact_binary_endpoints'][key]);contained[key]=l<=Fraction(value.l,S)<=Fraction(value.h,S)<=h
  assert all(contained.values())
  rows.append({'d':d,'e':str(e),'theta':str(th),'lambda':str(lam),'phase':'pi','actual_order':str(1+(d*d-1)*th),'input':saved(din),'output':saved(dout),'ratio':saved(ratio),'gap':saved(gap),'benchmark':saved(bench),'input_BKM_metric':saved(din/2),'input_SLD_QFI':saved(sld),'input_trace_distance_phase_pi':saved(distance),'input_condition_number':saved(condition),'exact_min_input_eigenvalue':str(emin),'rational_plane_determinants':[str(di),str(do)],'inside_original_binary_intervals':contained})
  print(d,str(e),saved(ratio)['decimal_display_only'],saved(condition)['decimal_display_only'],flush=True)
(P/'INTEGER_INTERVAL1054.json').write_text(json.dumps({'method':'768-bit directed integer dyadic intervals;400-term atanh log plus explicit tail; no floating-point arithmetic for endpoints','inherited_arithmetic_from_own_audit1044':True,'source_code_sha2561044':'91b68b9a54cdbfca9bfb7710597fe313364df939ec5a9d9627468134f83c43e5','cases':rows,'all_four_positive_gaps':True},indent=2)+'\n',encoding='utf-8')
