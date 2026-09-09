# Sign pattern via the exact recursion q_{n+1} = 2(d+n)(q_n+1)/(2d-2+n), q_n = W_{n-1}/u_n, q_3=(d+2)(3d+1)/(d(d-1)).
# chat_n < 0  <=>  q_n > g_n := d n (n+2d)/((d-1)(2d+2-n))   for n <= 2d+1.
# Sub-solution test: Pi(n,d) = 2(d+n)(g_n+1)/(2d-2+n) - g_{n+1} >= 0 ?
import sympy as sp
n,d=sp.symbols('n d',positive=True)
g=lambda m: d*m*(m+2*d)/((d-1)*(2*d+2-m))
Pi=sp.factor(sp.together(2*(d+n)*(g(n)+1)/(2*d-2+n)-g(n+1)))
print("Pi =",Pi)
num=sp.numer(sp.together(Pi)); den=sp.denom(sp.together(Pi))
print("numerator expanded:",sp.expand(num))
print("denominator:",sp.factor(den))
# evaluate sign of numerator on 3<=n<=2d for d=3..60
from fractions import Fraction as Fr
numf=sp.lambdify((n,d),num)
bad=[]
for dd in range(3,61):
    for nn in range(3,2*dd+1):
        v=sp.Rational(num.subs({n:nn,d:dd}))
        if v<=0: bad.append((dd,nn,v))
print("violations of Pi>=0 (d,n,num):",bad[:40], "count",len(bad))

assert sp.simplify(Pi-n*(n-1)*(2*d**2-d*n-d-2)/((d-1)*(2*d+1-n)*(2*d+2-n)))==0
assert {(dd,nn) for dd,nn,v in bad}=={(dd,nn) for dd in range(3,61) for nn in (2*dd-1,2*dd)}
