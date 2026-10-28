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
P=Path(__file__).parent;BITS=1152;S=1<<BITS;N=700
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
