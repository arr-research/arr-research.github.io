# (H6) and Remark 6.3 of version 2.
#  1. Symbolic: the expansion G_{d,lambda}(b) = lambda(2 lambda v_d - R0^2) b^2 + (4/3) lambda^3 mu_{3,d} b^3 + O(b^4) with d, lambda symbolic;
#     the d = 2, lambda = 3 expansion G_{2,3}(b) = -(9/20) b^4 + (9/35) b^6 + O(b^8) (b = 0 remains a strict local maximum).
#  2. Numeric (mpmath, 30 digits): for d = 3, 4, 5, 6, Q(k) = Ntilde_d(k)/k^(n_d+1) has Q' > 0 on a grid and Q -> -infinity as k -> 0+.
import sympy as sp, mpmath as mp
b,k,lam=sp.symbols('b kappa lambda',positive=True); d=sp.symbols('d',positive=True)
Mser=sum(k**j/sp.rf(d,j) for j in range(6))           # M_d(kappa) to O(kappa^6)
G=(sp.log(Mser)-k/d).subs(k,2*lam*b)-lam*(1-1/d)*b**2
ser=sp.series(G,b,0,4).removeO()
c2=sp.factor(ser.coeff(b,2)); c3=sp.factor(ser.coeff(b,3))
vd=(d-1)/(d**2*(d+1)); mu3=2*(d-1)*(d-2)/(d**3*(d+1)*(d+2))
print("b^2 coefficient == lambda(2 lambda v_d - R0^2):", sp.simplify(c2-lam*(2*lam*vd-(1-1/d)))==0, "  b^3 coefficient == (4/3) lambda^3 mu_{3,d}:", sp.simplify(c3-sp.Rational(4,3)*lam**3*mu3)==0)
M2=(sp.exp(k)-1)/k; G23=(sp.log(M2)-k/2).subs(k,6*b)-sp.Rational(3,2)*b**2
print("G_{2,3}(b) =", sp.series(G23,b,0,8))
mp.mp.dps=30
for dd,nd in [(3,5),(4,7),(5,10),(6,12)]:
    Nt=lambda x:(x-2*dd)*mp.hyp1f1(1,dd,x)**2+dd*(x-dd+3)*mp.hyp1f1(1,dd,x)+dd*(dd-1)
    Q=lambda x:Nt(x)/x**(nd+1)
    grid=[mp.mpf(i)/8 for i in range(1,8*6*dd)]
    inc=all(mp.diff(Q,x)>0 for x in grid)
    assert inc, dd
    print(f"d={dd}, n_d={nd}: Q'>0 on grid (0,{6*dd}) step 1/8: {inc};  Q(1e-3)={mp.nstr(Q(mp.mpf('1e-3')),4)}, Q(6d)={mp.nstr(Q(mp.mpf(6*dd)),4)}")

assert sp.simplify(c2-lam*(2*lam*vd-(1-1/d)))==0
assert sp.simplify(c3-sp.Rational(4,3)*lam**3*mu3)==0
assert sp.expand(sp.series(G23,b,0,8).removeO()+sp.Rational(9,20)*b**4-sp.Rational(9,35)*b**6)==0
