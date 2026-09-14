"""Symbolic verification (sympy, symbolic q) of the (X,u,kappa) reduction for L_q.
State variables: kappa, L, L1 (=L'); L'' and L''' eliminated through
  (E2)  kappa^2 L'' + 2 q kappa L' - (kappa^2 - q(q-1)) L - q(q-1) = 0        (B3 Prop 8.1(ii))
  (E3)  kappa^2 L''' + (2q+2) kappa L'' + (q(q+1) - kappa^2) L' - 2 kappa L = 0 (B3 eq. (8.1))
Checks (C1)-(C6) listed in the report, plus the small-kappa coefficients.
"""
import sympy as sp
q, k, L, L1 = sp.symbols('q kappa L L1', positive=True)

L2 = sp.solve(sp.Eq(k**2*sp.Symbol('L2') + 2*q*k*L1 - (k**2 - q*(q-1))*L - q*(q-1), 0), sp.Symbol('L2'))[0]
L3 = sp.solve(sp.Eq(k**2*sp.Symbol('L3') + (2*q+2)*k*L2 + (q*(q+1) - k**2)*L1 - 2*k*L, 0), sp.Symbol('L3'))[0]
# (E3) must be the kappa-derivative of (E2): check
E2 = k**2*sp.Symbol('L2') + 2*q*k*L1 - (k**2 - q*(q-1))*L - q*(q-1)
def Dk(f):
    """d/dkappa of f(kappa, L, L1) along the trajectory."""
    return sp.diff(f, k) + L1*sp.diff(f, L) + L2*sp.diff(f, L1)
dE2 = sp.diff(E2, k).subs(sp.Symbol('L2'), L2) + L1*sp.diff(E2, L) + L2*sp.diff(E2, L1) + sp.diff(E2, sp.Symbol('L2'))*L3
assert sp.simplify(dE2) == 0
print("(E3) = d/dkappa (E2): OK")

def D(f):
    return sp.cancel(k*Dk(f))          # d/dtau, tau = log kappa

m = L1/L
mp = Dk(m)
H = sp.cancel(m - k*mp)
u = 1/L
X = k*m
h = k*H
T = 2*X**2 + q*(q-1)*u*X - 2*q*(q-1)*(1-u)
Delta = -k*m*(1-m**2) + (2*q+5)*m**2 - 2 + (q+1)*(q+2)*m/k

assert sp.cancel(h - (X**2 + (2*q+1)*X + q*(q-1)*(1-u) - k**2)) == 0; print("(C1) OK")
assert sp.cancel(D(X) - (2*X - h)) == 0 and sp.cancel(D(u) + X*u) == 0; print("(C2) OK")
assert sp.cancel(k**2*Delta - (T + (X+2)*h)) == 0; print("(C3) OK")
assert sp.cancel(D(T) - (X**2*(8 - q*(q-1)*u) - h*(4*X + q*(q-1)*u))) == 0; print("(C4) OK")
assert sp.cancel(D(h) - (T - (2*X + 2*q - 1)*h)) == 0; print("(C5) OK")
# B3 identity (8.2): H' + (3m + (2q+2)/kappa) H = Delta
assert sp.cancel(Dk(H) + (3*m + (2*q+2)/k)*H - Delta) == 0; print("B3 (8.2) OK")
# (C6) factorization
mm, uu = sp.symbols('m u', positive=True)
Hmu = k*mm**2 + (2*q+1)*mm - k + q*(q-1)*(1-uu)/k
assert sp.cancel(H.subs(L1, mm*L).subs(L, 1/uu) - Hmu) == 0
mplus = (-(2*q+1) + sp.sqrt((2*q+1)**2 + 4*k**2 - 4*q*(q-1)*(1-uu)))/(2*k)
assert sp.simplify(sp.expand(k*Hmu) - sp.expand((k*mm - k*mplus)*(k*mm + k*mplus + 2*q + 1))) == 0
print("(C6) OK")
# Lemma A bracket: c = q - 1/2
c = q - sp.Rational(1, 2)
Q = T - c*h
br = sp.cancel((D(Q) - (X**2*(8 - q*(q-1)*u) - c*Q))/h)
br_expected = (2*c - 4)*X + c*(2*q - 1 - c) - q*(q-1)*u
assert sp.cancel(br - br_expected) == 0
print("Lemma A bracket =", sp.expand(br_expected))

# Small-kappa coefficients from the series of L_q (J-law: w_j = z^j/(q+1)_{2j})
N = 5
Ls = sum(k**(2*j)/sp.rf(q+1, 2*j) for j in range(N))
L1s = sp.diff(Ls, k)
Hs = sp.series((m - k*mp).subs({L: Ls, L1: L1s}), k, 0, 6).removeO()
c3 = sp.factor(Hs.coeff(k, 3))
print("[kappa^3] H_q =", c3)
assert sp.simplify(c3 + 4*(q**2-q-8)/((q+1)**2*(q+2)**2*(q+3)*(q+4))) == 0
# Independent termwise verification of (E2) from the series L_q = sum_j z^j/(q+1)_{2j}
j = sp.Symbol('j', positive=True, integer=True)
wj = 1/sp.rf(q+1, 2*j)
wjm1 = 1/sp.rf(q+1, 2*j-2)
coef = sp.simplify(((2*j)*(2*j-1) + 4*q*j + q*(q-1))*wj - wjm1)   # coefficient of kappa^{2j}, j>=1, in (E2)
assert sp.simplify(sp.combsimp(coef)) == 0, coef
print("(E2) verified termwise from the series: OK")

import sys
if '--phi' in sys.argv:   # optional, slow (symbolic-q series of T on the zero locus); not used by any proof
  us = sp.series(1/Ls, k, 0, 8).removeO()
  yy = (4*k**2 - 4*q*(q-1)*(1-us))/(2*q+1)**2
  sqrt1y = sum(sp.binomial(sp.Rational(1,2), n)*yy**n for n in range(4))   # sqrt(1+y) to O(y^4), y = O(kappa^2)
  Xp = (2*q+1)*(sqrt1y - 1)/2
  Phi = 2*Xp**2 + q*(q-1)*us*Xp - 2*q*(q-1)*(1-us)
  Ps = sp.series(Phi, k, 0, 6).removeO()
  print("[kappa^2] Phi =", sp.simplify(Ps.coeff(k, 2)), "  [kappa^4] Phi =", sp.factor(Ps.coeff(k, 4)))
# G(z) = S0*S1 - S0*S2 + S1^2 (= S0^2 kappa H/4), z = kappa^2: first coefficients
z = sp.Symbol('z', positive=True)
w = [1/sp.rf(q+1, 2*j) for j in range(N)]
S0 = sum(w[j]*z**j for j in range(N)); S1 = sum(j*w[j]*z**j for j in range(N)); S2 = sum(j*j*w[j]*z**j for j in range(N))
G = sp.expand(S0*S1 - S0*S2 + S1**2)
print("G coefficients: z^1:", sp.simplify(G.coeff(z, 1)), " z^2:", sp.factor(G.coeff(z, 2)), " z^3:", sp.factor(G.coeff(z, 3)))
