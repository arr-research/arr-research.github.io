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
P=Path(__file__).parent;BITS=1600;S=1<<BITS;N=1000
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
Z=I.q(0);ONE=I.q(1);ID=[[ONE,Z],[Z,ONE]]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def scale(k,a):return [[k*a[i][j] for j in range(2)] for i in range(2)]
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),Z) for j in range(2)] for i in range(2)]
def logmat(a):
 delta=((a[0][0]-a[1][1]).square()+4*a[0][1]*a[1][0]).sqrt();hi=(a[0][0]+a[1][1]+delta)/2
 lo=(a[0][0]*a[1][1]-a[0][1]*a[1][0])/hi;assert lo.l>0 and (hi-lo).l>0
 return add(scale(log(lo),ID),scale((log(hi)-log(lo))/(hi-lo),add(a,scale(-lo,ID))))
def pair(W,T,t):
 lw=logmat(W);out=Z
 for sign in [-1,1]:
  a=add(W,scale(sign*t,T));b=mul(a,add(logmat(a),scale(-ONE,lw)));out+=b[0][0]+b[1][1]
 return out
def binaryfraction(t):
 sign,man,exp,bc=t
 return Fraction((-1 if sign else 1)*man*(1<<exp),1) if exp>=0 else Fraction((-1 if sign else 1)*man,1<<(-exp))
def display(x):
 with localcontext() as c:
  c.prec=55;return [str(Decimal(x.l)/Decimal(S)),str(Decimal(x.h)/Decimal(S))]
def saved(x):return {'lower_integer':str(x.l),'upper_integer':str(x.h),'denominator_power_of_2':BITS,'display_only_55_digits':display(x)}
rows=[]
try:
 source=json.loads(Path(r'D:\Proyectos\airr-investigacion\2026-10-27_bkm1035\INTERVAL1035.json').read_text())['cases']
 for d in [3,4]:
  a=d-1;e=I.q(1,10**30);t=I.q(1,10**90);theta=I.q(99,100);q=a+e.square()
  def W(p):return scale(ONE/(2*d*q),[[1+(d*a-1)*p,d*p*e],[d*p*e*a,(2+(d-2)*p)*e.square()]])
  T=[[Z,ONE],[I.q(a),2*e]]
  for lam,label in [(-ONE/(d*d-1),'negative_CP_endpoint'),(ONE/2,'one_half')]:
   before=pair(W(theta),T,t);after=pair(W(lam*theta),T,lam*t);assert before.l>0 and after.l>0
   ratio=after/before;bell=lam.square()*I.q(d*d,2)/(1+lam*(I.q(d*d,2)-1));gap=ratio-bell;assert gap.l>0
   ref=next(x for x in source if x['d']==d and x['lambda_case']==label)
   contains={}
   for key,iv in [('input_divergence',before),('output_divergence',after),('ratio',ratio),('positive_gap',gap)]:
    lo,hi=[binaryfraction(z) for z in ref[key]['binary_endpoints']]
    contains[key]=lo<=Fraction(iv.l,S)<=Fraction(iv.h,S)<=hi
   assert all(contains.values())
   rows.append({'d':d,'lambda_case':label,'input_divergence':saved(before),'output_divergence':saved(after),'ratio':saved(ratio),'Bell_endpoint':saved(bell),'positive_gap':saved(gap),'own_enclosures_inside_original_binary_intervals':contains})
   (P/'INTEGER_INTERVAL1044.json').write_text(json.dumps({'method':'Exact integer directed dyadic rounding; log range reduction and1000-term atanh with explicit tail; rational similar-coordinate matrices, no surd inputs or mpmath','bits':BITS,'cases':rows},indent=2)+'\n',encoding='utf-8');print(d,label,display(gap),flush=True)
 print('All four own enclosures strictly positive and contained in supplied binary endpoints.')
except Exception as ex:
 (P/'INTEGER_INTERVAL_FAILURE1044.json').write_text(json.dumps({'completed_cases':rows,'error':repr(ex),'traceback':traceback.format_exc()},indent=2)+'\n',encoding='utf-8');raise
