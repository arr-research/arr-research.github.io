import sympy as sp
from math import comb
d=4; t=sp.Rational(1,16)
def Q(k,d,t): return sp.jacobi(k,d-2,0,2*t-1)/sp.binomial(k+d-2,k)
g={k: sp.Rational(16,5)*(1+4*Q(k,4,t)) for k in range(2,41)}
for k in range(2,11): print(k, g[k], float(g[k]))
kmin=min(g,key=lambda k:g[k]); print("min k",kmin,g[kmin])
print("Q6", Q(6,4,t), "diff 22018975/7340032-14/5 =", sp.Rational(22018975,7340032)-sp.Rational(14,5), float(sp.Rational(22018975,7340032)-sp.Rational(14,5)), "report says 1466335/7340032 =", float(sp.Rational(1466335,7340032)))
# ONB d=4
gO={k: 4*(1+3*sp.Integer(-1)**k/sp.binomial(k+2,k)) for k in range(2,41)}
print("ONB min", min(gO.values()), [ (k,gO[k]) for k in range(2,8)])
# d=3 simplex
g3={k: sp.Rational(9,4)*(1+3*Q(k,3,sp.Rational(1,9))) for k in range(2,41)}
print("d3 simplex min", min(g3.values()), min(g3,key=lambda k:g3[k]), "Q4,3(1/9)=",Q(4,3,sp.Rational(1,9)))
# record (13) check
dd=sp.symbols('d')
print(sp.factor(sp.Rational(1,1)*sp.jacobi(3,dd-2,0,2/dd**2-1)))
for D in (3,4,5):
    val=sp.Rational(D*D,D+1)*(1+D*Q(3,D,sp.Rational(1,D*D)))
    print(D, val, (D+3)*(D**4-4*D**3+7*D**2+2*D-8)/sp.Integer(D)**4)
