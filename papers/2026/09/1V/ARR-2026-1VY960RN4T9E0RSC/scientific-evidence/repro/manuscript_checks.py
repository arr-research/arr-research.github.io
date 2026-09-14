"""Symbolic checks for selected manuscript identities and finite Taylor coefficients
(written for the manuscript, independent of the work-directory and reviewer scripts).
sympy exact; exits with status 0 only if all assertions hold."""
import sympy as sp, sys
k, a, c, m, q, x = sp.symbols('kappa a c m q x', positive=True)
mu = a/c
out = []
def chk(name, cond):
    out.append((name, bool(cond)))

# ---------- Section 3: Riccati reduction (Theorem 3.1) ----------
M = sp.Function('M')(k)
Mp, Mpp = sp.diff(M, k), sp.diff(M, k, 2)
kummer_Mpp = (a*M - (c-k)*Mp)/k                       # Kummer: k M'' + (c-k) M' - a M = 0  (DLMF 13.2.1)
mm = Mp/M
chk("(3.1) Riccati k m' = a-(c-k)m-k m^2", sp.simplify((k*sp.diff(mm, k)).subs(Mpp, kummer_Mpp) - (a-(c-k)*mm-k*mm**2)) == 0)
mp_ric = (a-(c-k)*m-k*m**2)/k
H = (m-mu) - k*mp_ric
chk("(3.2) H = -k m(1-m)+(c+1)(m-mu)", sp.simplify(H - (-k*m*(1-m)+(c+1)*(m-mu))) == 0)
Psi = (c+1)*(m-mu)/(m*(1-m))
chk("(3.3) H = m(1-m)(Psi(m)-k)", sp.simplify(H - m*(1-m)*(Psi-k)) == 0)

# ---------- Section 4: phase-plane identities (a)-(d) ----------
Psip = sp.diff(Psi, m)
chk("(a) Psi' = (c+1)[(m-mu)^2+mu(1-mu)]/(m(1-m))^2", sp.simplify(Psip - (c+1)*((m-mu)**2+mu*(1-mu))/(m*(1-m))**2) == 0)
den = a - c*m + k*m*(1-m)
G = k/den
chk("(b) den on curve = m-mu", sp.simplify(den.subs(k, Psi) - (m-mu)) == 0)
chk("(b) G(m,Psi) = Psi/(m-mu)", sp.simplify(G.subs(k, Psi) - Psi/(m-mu)) == 0)
Delta = sp.simplify(Psip - G.subs(k, Psi))
chk("(c) Delta = -(c+1)(m-mu)(1-2m)/(m(1-m))^2", sp.simplify(Delta + (c+1)*(m-mu)*(1-2*m)/(m*(1-m))**2) == 0)
chk("(d) dG/dk = (a-cm)/den^2", sp.simplify(sp.diff(G, k) - (a-c*m)/den**2) == 0)
chk("Psi(1/2) = 2(c+1)(c-2a)/c", sp.simplify(Psi.subs(m, sp.Rational(1, 2)) - 2*(c+1)*(c-2*a)/c) == 0)

# ---------- small-kappa expansion of H, moments of Beta(a,c-a) ----------
al, be = a, c-a
E = lambda n: sp.rf(al, n)/sp.rf(al+be, n)
var = sp.simplify(E(2)-E(1)**2)
mu3 = sp.simplify(E(3)-3*E(1)*E(2)+2*E(1)**3)
mu4 = sp.simplify(E(4)-4*E(1)*E(3)+6*E(1)**2*E(2)-3*E(1)**4)
k4 = sp.simplify(mu4-3*var**2)
chk("v = a(c-a)/(c^2(c+1))", sp.simplify(var - a*(c-a)/(c**2*(c+1))) == 0)
chk("mu3 = 2a(c-a)(c-2a)/(c^3(c+1)(c+2))", sp.simplify(mu3 - 2*a*(c-a)*(c-2*a)/(c**3*(c+1)*(c+2))) == 0)
chk("lambda_0 = (1-mu)/(2v) = c(c+1)/(2a)", sp.simplify((1-mu)/(2*var) - c*(c+1)/(2*a)) == 0)
Mser = sum(sp.rf(a, j)/sp.rf(c, j)*k**j/sp.factorial(j) for j in range(8))
Kser = sp.series(sp.log(Mser) - mu*k, k, 0, 6).removeO()
mser = sp.diff(Kser, k)
Hser = sp.expand(sp.series(mser - k*sp.diff(mser, k), k, 0, 5).removeO())
chk("[k^0]H=[k^1]H=0", sp.simplify(Hser.coeff(k, 0)) == 0 and sp.simplify(Hser.coeff(k, 1)) == 0)
chk("[k^2]H = -mu3/2", sp.simplify(Hser.coeff(k, 2) + mu3/2) == 0)
chk("[k^3]H = -kappa4/3", sp.simplify(Hser.coeff(k, 3) + k4/3) == 0)
chk("[k^3]H at c=2a = 1/(8(2a+1)^2(2a+3))", sp.simplify((-k4/3).subs(c, 2*a) - 1/(8*(2*a+1)**2*(2*a+3))) == 0)
# generic cumulant form H = sum_{j>=2} kappa_j (2-j) k^{j-1}/(j-1)!
kap = sp.symbols('kappa2:7')
Kgen = sum(kap[j-2]*k**j/sp.factorial(j) for j in range(2, 7))
Hgen = sp.expand(sp.diff(Kgen, k) - k*sp.diff(Kgen, k, 2))
chk("H = sum kappa_j (2-j) k^{j-1}/(j-1)!", sp.simplify(Hgen - sum(kap[j-2]*(2-j)*k**(j-1)/sp.factorial(j-1) for j in range(2, 7))) == 0)

# ---------- Section 5: bounds ----------
m_u = a*(c+1)/(c*(a+1))
chk("Psi(m_u) = c(a+1)", sp.simplify(Psi.subs(m, m_u) - c*(a+1)) == 0)
chk("H = m[(c-a)-k(1-m)] + (a+1)m-(c+1)mu", sp.simplify((-k*m*(1-m)+(c+1)*(m-mu)) - (m*((c-a)-k*(1-m)) + (a+1)*m-(c+1)*mu)) == 0)
chk("m_u - 1/2 = (c(a-1)+2a)/(2c(a+1))", sp.simplify(m_u - sp.Rational(1, 2) - (c*(a-1)+2*a)/(2*c*(a+1))) == 0)
# integration by parts integrand: d/dx[x^{a-1}e^{kx}] (1-x)^{c-a}
g = x**(a-1)*sp.exp(k*x)
chk("IBP integrand", sp.simplify((1-x)**(c-a)*sp.diff(g, x) - ((a-1)*x**(a-2)*(1-x)**(c-a) + k*x**(a-1)*(1-x)**(c-a))*sp.exp(k*x)) == 0)

# ---------- Section 7: Bessel family ----------
W0, W1, W2 = sp.symbols('W0 W1 W2')
Zp, Zpp = k/2*W1, k**2/4*W2 + W1/2                    # Z(k) = w(k^2/4), z w'' + c w' - w = 0
e = (k*Zpp + (2*c-1)*Zp - k*W0).subs(W2, (W0 - c*W1)/(k**2/4))
chk("(7.1) k Z'' + (2c-1) Z' - k Z = 0", sp.simplify(e) == 0)
mp0 = (k*(1-m**2) - (2*c-1)*m)/k
H0 = m - k*mp0
chk("(7.2) H_Z = k(m^2-1) + 2cm", sp.simplify(H0 - (k*(m**2-1) + 2*c*m)) == 0)
Psi0 = 2*c*m/(1-m**2)
den0 = k*(1-m**2) - (2*c-1)*m
chk("(7.3) den0 on curve = m", sp.simplify(den0.subs(k, Psi0) - m) == 0)
chk("(7.3) Delta0 = 4c m^2/(1-m^2)^2", sp.simplify(sp.diff(Psi0, m) - Psi0/m - 4*c*m**2/(1-m**2)**2) == 0)
chk("(7.4) k m' at m=1 equals 1-2c", sp.simplify((k*mp0).subs(m, 1) - (1-2*c)) == 0)
Zs = sum((k**2/4)**j/(sp.rf(c, j)*sp.factorial(j)) for j in range(6))
Ks = sp.series(sp.log(Zs), k, 0, 7).removeO(); ms = sp.diff(Ks, k)
Hs0 = sp.expand(sp.series(ms - k*sp.diff(ms, k), k, 0, 6).removeO())
chk("0F1: [k^3]H = 1/(4c^2(c+1)), lower orders 0", sp.simplify(Hs0.coeff(k, 3) - 1/(4*c**2*(c+1))) == 0 and Hs0.coeff(k, 1) == 0 and Hs0.coeff(k, 2) == 0)
# Kummer's second theorem 0F1(;c;k^2/4) = e^{-k} 1F1(c-1/2; 2c-1; 2k)  (DLMF 13.6.9 with nu=c-1)
ap = c - sp.Rational(1, 2)
lhs = sum((k**2/4)**j/(sp.rf(c, j)*sp.factorial(j)) for j in range(6))
rhs = sp.exp(-k)*sum(sp.rf(ap, j)/sp.rf(2*ap, j)*(2*k)**j/sp.factorial(j) for j in range(11))
chk("Kummer second theorem to O(k^10)", sp.simplify(sp.series(lhs - rhs, k, 0, 11).removeO()) == 0)
# H_Z(k) = 2 H_{a',2a'}(2k) with a' = c-1/2 (chain rule; symbolic)
Kf = sp.Function('K')(k)
Ht = lambda f: sp.diff(f, k) - k*sp.diff(f, k, 2)
F2 = Kf.subs(k, 2*k) - k        # log Z(k) = K(2k) - k + const, with K = log 1F1 - mu k, mu = 1/2 (c=2a)  => log Z = K_{a',2a'}(2k)
chk("H_{Z}(k) = 2 H_K(2k)", sp.simplify(Ht(Kf.subs(k, 2*k)) - 2*(sp.diff(Kf, k) - k*sp.diff(Kf, k, 2)).subs(k, 2*k)) == 0)

# ---------- Section 8: L_q identities ----------
Lf = sp.Function('L')(k)
Sf = sp.diff(Lf, k) + q*(Lf-1)/k
ode2 = sp.expand(k*(k*sp.diff(Sf, k) - (k*Lf - q*Sf)))
claim2 = k**2*sp.diff(Lf, k, 2) + 2*q*k*sp.diff(Lf, k) - (k**2 - q*(q-1))*Lf - q*(q-1)
chk("(8.2) second-order ODE for L_q", sp.simplify(ode2 - claim2) == 0)
claim3 = k**2*sp.diff(Lf, k, 3) + (2*q+2)*k*sp.diff(Lf, k, 2) + (q*(q+1)-k**2)*sp.diff(Lf, k) - 2*k*Lf
chk("(8.3) third-order ODE = derivative of (8.2)", sp.simplify(sp.diff(claim2, k) - claim3) == 0)
mf = sp.Function('m')(k); m1, m2 = sp.diff(mf, k), sp.diff(mf, k, 2)
ode3m = k**2*(m2+3*mf*m1+mf**3) + (2*q+2)*k*(m1+mf**2) + (q*(q+1)-k**2)*mf - 2*k
m2sol = sp.solve(ode3m, m2)[0]
Hq = mf - k*m1
Dq = -k*mf*(1-mf**2) + (2*q+5)*mf**2 - 2 + (q+1)*(q+2)*mf/k
chk("(8.4) H' + (3m+(2q+2)/k)H = Delta_q", sp.simplify(sp.diff(Hq, k).subs(m2, m2sol) + (3*mf+(2*q+2)/k)*Hq - Dq) == 0)
Hf = sp.Function('H')(k)
Wf = k**(2*q+2)*Lf**3*Hf
chk("(8.5) integrating factor k^{2q+2} L^3", sp.simplify(sp.diff(Wf, k) - k**(2*q+2)*Lf**3*(sp.diff(Hf, k) + (3*sp.diff(Lf, k)/Lf + (2*q+2)/k)*Hf)) == 0)
# 1F2 form: q! k^{2j}/(q+2j)! = (k^2/4)^j / (((q+1)/2)_j ((q+2)/2)_j)
j = sp.symbols('j', integer=True, nonnegative=True)
chk("L_q = 1F2(1;(q+1)/2,(q+2)/2;k^2/4) termwise (j<=6)", all(sp.simplify(sp.factorial(qq)/sp.factorial(qq+2*jj) - sp.Rational(1, 4**jj)/(sp.rf(sp.Rational(qq+1, 2), jj)*sp.rf(sp.Rational(qq+2, 2), jj))) == 0 for qq in range(1, 7) for jj in range(0, 7)))
# Proposition 8.2 (reviewer's formula): small-k coefficients of Delta_q(m(k),k) and H_q
Lq = sum(k**(2*jj)/sp.rf(q+1, 2*jj) for jj in range(6))
mq = sp.series(sp.diff(Lq, k)/Lq, k, 0, 8).removeO()
Dq_ser = sp.expand(sp.series(-k*mq*(1-mq**2) + (2*q+5)*mq**2 - 2 + (q+1)*(q+2)*mq/k, k, 0, 5).removeO())
den_q = (q+1)**2*(q+2)**2*(q+3)*(q+4)
chk("(8.6) [k^0]Delta_q = 0, [k^1]Delta_q = 0", sp.simplify(Dq_ser.coeff(k, 0)) == 0 and sp.simplify(Dq_ser.coeff(k, 1)) == 0)
chk("(8.6) [k^2]Delta_q = -4(2q+5)(q^2-q-8)/den", sp.simplify(Dq_ser.coeff(k, 2) + 4*(2*q+5)*(q**2-q-8)/den_q) == 0)
Hq_ser = sp.expand(sp.series(mq - k*sp.diff(mq, k), k, 0, 6).removeO())
chk("(8.6) [k^3]H_q = -4(q^2-q-8)/den, [k^1]=0", sp.simplify(Hq_ser.coeff(k, 3) + 4*(q**2-q-8)/den_q) == 0 and sp.simplify(Hq_ser.coeff(k, 1)) == 0)
chk("q^2-q-8 <0 for q<=3, >0 for q>=4", all((qq**2-qq-8 < 0) for qq in (1, 2, 3)) and all((qq**2-qq-8 > 0) for qq in range(4, 100)))
# L_1, L_2 identifications
chk("L_1 = sinh k / k", sp.simplify(sp.series(Lq.subs(q, 1) - sp.sinh(k)/k, k, 0, 11).removeO()) == 0)
chk("L_2 = (sinh(k/2)/(k/2))^2", sp.simplify(sp.series(Lq.subs(q, 2) - (sp.sinh(k/2)/(k/2))**2, k, 0, 11).removeO()) == 0)
Z32 = lambda z: sum((z**2/4)**jj/(sp.rf(sp.Rational(3, 2), jj)*sp.factorial(jj)) for jj in range(7))
chk("sinh k/k = 0F1(;3/2;k^2/4)", sp.simplify(sp.series(sp.sinh(k)/k - Z32(k), k, 0, 12).removeO()) == 0)
# q=4 normalizer equals the 61Y0 normalizer 12(2cosh k - 2 - k^2)/k^4
chk("L_4 = 12(2cosh k-2-k^2)/k^4", sp.simplify(sp.series(Lq.subs(q, 4) - 12*(2*sp.cosh(k)-2-k**2)/k**4, k, 0, 11).removeO()) == 0)

# ---------- Section 6: chain identities with generic K ----------
R2, bb, ll, kap_ = sp.symbols('R2 b lambda kap', positive=True)
Kg = sp.Function('K')(k)
bfun = sp.diff(Kg, k)/R2; lam = k/(2*bfun)
Hg = sp.diff(Kg, k) - k*sp.diff(Kg, k, 2)
chk("(6.1) lambda' = H/(2 R^2 b^2)", sp.simplify(sp.diff(lam, k) - Hg/(2*R2*bfun**2)) == 0)
chk("(6.1) F' = H", sp.simplify(sp.diff(2*Kg - k*sp.diff(Kg, k), k) - Hg) == 0)
K1, K2, K0 = sp.symbols('K1 K2 K0')
Gq = K0 - ll*R2*bb**2       # value at stationary radius: K(kap) with K'(kap) = R2 b, ll = kap/(2b)
chk("(6.1) G = F/2 at stationary radius", sp.simplify((K0 - (kap_/(2*bb))*R2*bb**2).subs(R2, K1/bb) - (2*K0 - kap_*K1)/2) == 0)
Gpp = 4*ll**2*K2 - 2*ll*R2   # d^2/db^2 [K(2 lam b) - lam R2 b^2]
chk("(6.1) G'' = -(2 lam/b) H at stationary radius", sp.simplify(Gpp.subs(R2, K1/bb).subs(ll, kap_/(2*bb)) + (2*(kap_/(2*bb))/bb)*(K1 - kap_*K2)) == 0)
lam_, b_ = sp.symbols('lambda_ b_', positive=True)
Gexp = sp.expand(var/2*(2*lam_*b_)**2 + mu3/6*(2*lam_*b_)**3 - lam_*(1-mu)*b_**2)
chk("(H6) G = lam(2 lam v - R^2) b^2 + (4/3) lam^3 mu3 b^3 + ...", sp.simplify(Gexp - (lam_*(2*lam_*var-(1-mu))*b_**2 + sp.Rational(4, 3)*lam_**3*mu3*b_**3)) == 0)

for name, ok in out:
    print(("OK   " if ok else "FAIL ") + name)
allok = all(o for _, o in out)
print("ALL OK" if allok else "SOME FAIL")
sys.exit(0 if allok else 1)
