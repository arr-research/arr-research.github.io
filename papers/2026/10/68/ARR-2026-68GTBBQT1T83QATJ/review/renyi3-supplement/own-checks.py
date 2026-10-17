from pathlib import Path
from fractions import Fraction as Q
import json
import sympy as sp
import mpmath as mp
root=Path(__file__).parent
x,y,z=sp.symbols('x y z',positive=True)
f=lambda x:x*(1+3*x*x)
n=lambda x:1-3*x*x
A=lambda x:2*n(x)/f(x)
e2=x*y+x*z+y*z;e3=x*y*z
N=sp.expand(f(x)*n(y)*n(z)+f(y)*n(x)*n(z)+f(z)*n(x)*n(y))
target=4-12*e2-9*e2**2+36*e3+18*e2*e3+27*e3**2
assert sp.factor((N-target).subs(z,1-x-y))==0
schur_decomp=4*(1-4*e2+9*e3)+e2*(4-9*e2)+18*e2*e3+27*e3**2
assert sp.expand(target-schur_decomp)==0
# A separate elementary certificate of Schur, ordered x>=y>=z:
S=(x+y+z)**3+9*x*y*z-4*(x+y+z)*(x*y+x*z+y*z)
assert sp.expand(S-((x-y)**2*(x+y-z)+z*(z-x)*(z-y)))==0
# Rational points avoid the singular endpoints; no floating eigenvalue subtraction.
count=0;det_min=None
for i in range(1,80):
 for j in range(1,80-i):
  q=[Q(i,80),Q(j,80),Q(80-i-j,80)]
  aa=[Q(2)*(1-3*t*t)/(t*(1+3*t*t)) for t in q]
  m11=aa[0]+aa[2];m22=aa[1]+aa[2];off=aa[2]
  det=m11*m22-off*off
  assert m11>0 and m22>0 and det>0
  count+=1;det_min=det if det_min is None else min(det_min,det)
# High precision line checks near both the cap interface and singular outer edge.
mp.mp.dps=100
h3=lambda p:-mp.log(1-3*p+3*p*p,2)/2
phi3=lambda u:(3-mp.sqrt(12*mp.power(2,-2*u)-3))/6
G=lambda a,b:mp.mpf(1) if phi3(a)+phi3(b)<=mp.mpf('.5') else h3(1-phi3(a)-phi3(b))
checks=0;min_gap=None
points=[mp.mpf(0),mp.mpf('1e-30'),mp.mpf('.1'),mp.mpf('.4'),mp.mpf('.9'),1-mp.mpf('1e-30'),mp.mpf(1)]
pairs=[]
for a in points:
 for b in points:pairs.append((a,b))
for i,left in enumerate(pairs):
 right=pairs[(i*19+7)%len(pairs)]
 for t in [mp.mpf('.01'),mp.mpf('.5'),mp.mpf('.99')]:
  mix=[t*left[k]+(1-t)*right[k] for k in range(2)]
  gap=G(*mix)-t*G(*left)-(1-t)*G(*right)
  assert gap>-mp.mpf('1e-90')
  min_gap=gap if min_gap is None else min(min_gap,gap);checks+=1
f4=lambda p:p**4+(1-p)**4
exact=f4(Q(1,4))**2-f4(Q(1,5))*f4(Q(3,10))
assert exact==Q(3457649,6400000000)>0
h4=lambda p:-mp.log(p**4+(1-p)**4,2)/3
phi4=lambda u:(1-mp.sqrt(-3+mp.sqrt(8+8*mp.power(2,-3*u))))/2
c=(h4(mp.mpf(1)/5)+h4(mp.mpf(3)/10))/2
lo,hi=mp.mpf(0),mp.mpf(1)
for _ in range(300):
 t=(lo+hi)/2
 if 2*phi4(t*c)+phi4(t)<=1:lo=t
 else:hi=t
out={'status':'PASS','new_symbolic_checks':['Tangent determinant numerator identity','Positive decomposition using Schur','Elementary Schur identity under ordered variables'],
 'rational_interior_triples':count,'minimum_tangent_determinant_exact':str(det_min),
 'endpoint_and_near_endpoint_jensen_checks':checks,'working_decimal_digits':100,'minimum_gap_numeric':mp.nstr(min_gap,25),
 'order_four_w3':{'exact_midpoint_polynomial_gap':str(exact),'xi_first_numeric':mp.nstr(c,40),'original_log_radial_numeric':mp.nstr((lo+hi)/2,40),'convexified_log_radial_exact':'1','strict_gap_numeric':mp.nstr(1-hi,40),'numeric_values_are_not_interval_certificates':True}}
(root/'own-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
