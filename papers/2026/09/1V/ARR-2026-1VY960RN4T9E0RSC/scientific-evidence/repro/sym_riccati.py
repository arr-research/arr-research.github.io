"""Symbolic identities for the one-fold criterion (Fable 5.1, cycle 2, B3).
1F1(a;c;k) Riccati reduction, phase-plane identities, small-k expansions,
0F1 (sphere) case, and the even-part (7H9F) system.  All exact with sympy."""
import sympy as sp
k, a, c, m, mu = sp.symbols('kappa a c m mu', positive=True)
q = sp.symbols('q', positive=True)

# --- 1F1(a;c;k): series to order N, check Kummer ODE and Riccati for m=M'/M
N = 12
M = sum(sp.rf(a, j)/sp.rf(c, j)*k**j/sp.factorial(j) for j in range(N+1))
kummer = sp.expand(k*sp.diff(M, k, 2) + (c-k)*sp.diff(M, k) - a*M)
kummer_trunc = sum(kummer.coeff(k, j)*k**j for j in range(N))  # drop truncation tail
assert sp.simplify(kummer_trunc) == 0, "Kummer ODE fails"
print("Kummer ODE verified to order", N-1)

# Riccati: k m' = a - (c-k) m - k m^2, m = M'/M  (exact consequence of Kummer)
Mf = sp.Function('M')(k)
mf = sp.diff(Mf, k)/Mf
ric = k*sp.diff(mf, k) - (a - (c-k)*mf - k*mf**2)
ric = ric.subs(sp.diff(Mf, k, 2), (a*Mf - (c-k)*sp.diff(Mf, k))/k)
assert sp.simplify(ric) == 0
print("Riccati k m' = a - (c-k) m - k m^2 verified")

# H = (m - mu) - k m' with mu=a/c, using Riccati:
H = (m - a/c) - (a - (c-k)*m - k*m**2)
H2 = -k*m*(1-m) + (c+1)*(m - a/c)
assert sp.simplify(H - H2) == 0
print("H = -k m(1-m) + (c+1)(m - a/c)  [quadratic in m]")

# Psi(m) = (c+1)(m-mu)/(m(1-m)); Delta = Psi' - Psi/(m-mu)
Psi = (c+1)*(m-mu)/(m*(1-m))
Psip = sp.diff(Psi, m)
assert sp.simplify(Psip - (c+1)*((m-mu)**2 + mu*(1-mu))/(m*(1-m))**2) == 0
Delta = sp.simplify(Psip - Psi/(m-mu))
Delta_claim = -(c+1)*(m-mu)*(1-2*m)/(m*(1-m))**2
assert sp.simplify(Delta - Delta_claim) == 0
print("Psi' = (c+1)[(m-mu)^2 + mu(1-mu)]/(m(1-m))^2 > 0 ;  Delta = -(c+1)(m-mu)(1-2m)/(m(1-m))^2")

# dk/dm = 1/m' = k/(a - c m + k m(1-m)) =: G(m,k); dG/dk = (a - c m)/den^2 (<0 for m>mu)
den = a - c*m + k*m*(1-m)
G = k/den
assert sp.simplify(sp.diff(G, k) - (a - c*m)/den**2) == 0
# denominator on the curve k = Psi(m) (mu = a/c): equals m - mu
assert sp.simplify(den.subs(k, Psi.subs(mu, a/c)) - (m - a/c)) == 0
print("dG/dk = (a-cm)/den^2 ; den|_{k=Psi} = m - mu > 0")
# D'(m) at a zero: G(m,Psi) = Psi/(m-mu)  -> D' = Psi' - Psi/(m-mu) = Delta  (consistent)
assert sp.simplify(G.subs(k, Psi.subs(mu, a/c)) - Psi.subs(mu, a/c)/(m - a/c)) == 0

# small-k expansion of H via cumulants of Beta(a, c-a): H = -mu3/2 k^2 - kappa4/3 k^3 + ...
Mser = sp.series(M, k, 0, 6).removeO()
Kser = sp.series(sp.log(Mser), k, 0, 6).removeO()
mser = sp.diff(Kser, k)
Hser = sp.expand(sp.series(mser - a/c - k*sp.diff(mser, k), k, 0, 5).removeO())
mu3 = 2*a*(c-a)*(c-2*a)/(c**3*(c+1)*(c+2))
c2 = sp.simplify(Hser.coeff(k, 2)); c3 = sp.simplify(Hser.coeff(k, 3))
assert sp.simplify(c2 + mu3/2) == 0
print("[k^2]H = -mu3/2, mu3 =", sp.factor(mu3))
print("[k^3]H =", sp.factor(c3))
print("[k^3]H at c=2a:", sp.factor(c3.subs(c, 2*a)), " (must be >0 for the symmetric case)")

# --- 0F1(;c;k^2/4) (real sphere S^{2c-1}): Riccati m' = 1 - (2c-1) m/k - m^2 ; H = k(m^2-1) + 2c m
Z = sum((k**2/4)**j/(sp.rf(c, j)*sp.factorial(j)) for j in range(N+1))
bess = sp.expand(k*sp.diff(Z, k, 2) + (2*c-1)*sp.diff(Z, k) - k*Z)
bess_trunc = sum(bess.coeff(k, j)*k**j for j in range(2*N))
assert sp.simplify(bess_trunc) == 0
Psi0 = 2*c*m/(1-m**2)
Delta0 = sp.simplify(sp.diff(Psi0, m) - Psi0/m)
assert sp.simplify(Delta0 - 4*c*m**2/(1-m**2)**2) == 0
print("0F1: Kummer-type ODE verified; H = k(m^2-1)+2c m; Psi = 2cm/(1-m^2); Delta = 4c m^2/(1-m^2)^2 > 0")

# --- even part L = (E+O)/2, E=M_{q+1}(k), O=M_{q+1}(-k); first-order system
E, O = sp.Function('E')(k), sp.Function('O')(k)
L = (E+O)/2; S = (E-O)/2
subsE = {sp.diff(E, k): ((k-q)*E + q)/k}
subsO = {sp.diff(O, k): (q-(k+q)*O)/k}
def d(expr):
    return sp.diff(expr, k).subs(subsE).subs(subsO)
Lp = sp.simplify(d(L)); Lpp = sp.simplify(d(Lp)); 
assert sp.simplify(k*Lp - (k*S - q*L + q)) == 0
Sp = sp.simplify(d(S)); assert sp.simplify(k*Sp - (k*L - q*S)) == 0
J = sp.simplify(L*Lp - k*L*Lpp + k*Lp**2)
kJ = sp.expand(sp.simplify(k*J))
Ls, Ss = sp.symbols('L S')
kJ_LS = sp.expand(kJ.subs({E: Ls+Ss, O: Ls-Ss}))
print("k*J in (L,S):", sp.collect(kJ_LS, [Ls, Ss]))
