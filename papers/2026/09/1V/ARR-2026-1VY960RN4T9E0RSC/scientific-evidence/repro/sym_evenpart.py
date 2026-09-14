"""Even part L_q = (E+O)/2, E=M_{q+1}(k), O=M_{q+1}(-k): exact first-order system and the
fold numerator J = L L' - k L L'' + k L'^2 in the variables (L,S) and (s,u)=(S/L,1/L)."""
import sympy as sp
k, q = sp.symbols('kappa q', positive=True)
E, O = sp.Function('E')(k), sp.Function('O')(k)
subs = {sp.diff(E, k): ((k-q)*E + q)/k, sp.diff(O, k): (q - (k+q)*O)/k}
def d(x): return sp.diff(x, k).subs(subs)
L = (E+O)/2; S = (E-O)/2
Lp, Sp = sp.simplify(d(L)), sp.simplify(d(S))
assert sp.simplify(k*Lp - (k*S - q*L + q)) == 0
assert sp.simplify(k*Sp - (k*L - q*S)) == 0
print("system: k L' = k S - q L + q ;  k S' = k L - q S   (verified)")
Lpp = sp.simplify(d(Lp))
J = sp.simplify(L*Lp - k*L*Lpp + k*Lp**2)
Ls, Ss = sp.symbols('L S')
kJ = sp.expand(sp.simplify(k*J).subs({E: Ls+Ss, O: Ls-Ss}))
print("k*J =", sp.collect(kJ, [Ls, Ss]))
# check small-k order: substitute series
Eser = sum(k**j/sp.rf(q+1, j) for j in range(8)); Oser = Eser.subs(k, -k)
kJser = sp.series(kJ.subs({Ls: (Eser+Oser)/2, Ss: (Eser-Oser)/2}), k, 0, 6)
print("k*J small-k:", sp.factor(kJser.removeO()))
# (s,u) coordinates: s=S/L, u=1/L
s, u = sp.symbols('s u', positive=True)
kJ_su = sp.simplify(kJ.subs({Ss: s*Ls}).subs(Ls, 1/u)*u**2)
print("u^2 k J =", sp.collect(sp.expand(kJ_su), k))
# dynamics of (s,u): s' = S'/L - s L'/L ; u' = -u L'/L
sp_ = sp.simplify((k*Sp/k)/L - (S/L)*(Lp/L))
up_ = sp.simplify(-(1/L)*(Lp/L))
sp_su = sp.simplify(sp_.subs({E: (1+s)/u, O: (1-s)/u}))
up_su = sp.simplify(up_.subs({E: (1+s)/u, O: (1-s)/u}))
print("k s' =", sp.factor(sp.simplify(k*sp_su)), ";  k u' =", sp.factor(sp.simplify(k*up_su)))
