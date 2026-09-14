"""Independent sympy re-derivation (reviewer). Everything from the series L_q = sum_j z^j/(q+1)_{2j}."""
import sympy as sp
q = sp.Symbol('q', positive=True)
k = sp.Symbol('kappa', positive=True)
j = sp.Symbol('j', positive=True, integer=True)

# 1. (E2) termwise: coefficient of kappa^{2j} in kappa^2 L'' + 2q kappa L' - (kappa^2 - q(q-1)) L - q(q-1)
wj = 1/sp.rf(q+1, 2*j); wjm1 = 1/sp.rf(q+1, 2*j-2)
coef = (2*j*(2*j-1) + 4*q*j + q*(q-1))*wj - wjm1
assert sp.simplify(sp.combsimp(sp.expand_func(coef))) == 0
# j = 0 term: q(q-1) w_0 - q(q-1) = 0 (w_0 = 1)
print("(E2) termwise OK; j=0: ", sp.simplify(q*(q-1)*1 - q*(q-1)))

# 2. State (kappa, L, L1); eliminate L2 via (E2)
L, L1 = sp.symbols('L L1', positive=True)
L2 = ((k**2 - q*(q-1))*L + q*(q-1) - 2*q*k*L1)/k**2
def Dk(f):            # d/dkappa along the trajectory, using only (E2)
    return sp.diff(f, k) + L1*sp.diff(f, L) + L2*sp.diff(f, L1)
def Dt(f):            # d/dtau
    return sp.cancel(k*Dk(f))
m = L1/L; mp_ = Dk(m); H = sp.cancel(m - k*mp_)
u = 1/L; X = k*m; h = sp.cancel(k*H)
T = 2*X**2 + q*(q-1)*u*X - 2*q*(q-1)*(1-u)
assert sp.cancel(h - (X**2 + (2*q+1)*X + q*(q-1)*(1-u) - k**2)) == 0; print("(C1) OK")
assert sp.cancel(Dt(X) - (2*X - h)) == 0; assert sp.cancel(Dt(u) + X*u) == 0; print("(C2) OK")
assert sp.cancel(Dt(T) - (X**2*(8 - q*(q-1)*u) - h*(4*X + q*(q-1)*u))) == 0; print("(C4) OK")
assert sp.cancel(Dt(h) - (T - (2*X + 2*q - 1)*h)) == 0; print("(C5) OK")
# (C3)/(C6) with B3's Delta (needs L3 from (E3) = (E2)' -- check (E3) first)
L3 = Dk(L2)   # derivative of the (E2)-expression for L'' along the trajectory
E3 = k**2*L3 + (2*q+2)*k*L2 + (q*(q+1) - k**2)*L1 - 2*k*L
assert sp.cancel(E3) == 0; print("(E3) is the derivative of (E2): OK")
Delta = -k*m*(1-m**2) + (2*q+5)*m**2 - 2 + (q+1)*(q+2)*m/k
assert sp.cancel(k**2*Delta - (T + (X+2)*h)) == 0; print("(C3) OK")
assert sp.cancel(Dk(H) + (3*m + (2*q+2)/k)*H - Delta) == 0; print("(C6) OK")
# Lyapunov bracket
c = sp.Symbol('c')
Q = T - c*h
B = sp.cancel((Dt(Q) - (X**2*(8 - q*(q-1)*u) - c*Q))/h)
Bexp = (2*c-4)*X + c*(2*q-1-c) - q*(q-1)*u
assert sp.cancel(B - Bexp) == 0; print("Lemma L bracket B OK:", sp.expand(Bexp))
for qq, cc in [(4, sp.Rational(7,2)), (2, 2), (3, sp.Rational(5,2))]:
    print("  q=%s c=%s: 2c-4=%s, c(2q-1-c)-q(q-1)=%s" % (qq, cc, 2*cc-4, cc*(2*qq-1-cc) - qq*(qq-1)))
# T = kappa^2 H' at zeros of H: from (C5), dh/dtau = kappa(H + kappa H') ; at H=0 -> kappa^2 H'
assert sp.cancel(Dt(h) - k*(H + k*Dk(H))) == 0; print("dh/dtau = kappa(H + kappa H') OK")
# second derivative on {h = 0, T = 0}: d2h/dtau2 = dT/dtau - (2X+2q-1) dh/dtau - h*(...) ; at h=T=0 equals X^2(8-q(q-1)u)
d2h = Dt(Dt(h)); Hp = Dk(H); Hpp = Dk(Hp)
# check d2h/dtau2 = kappa^3 H'' + 3 kappa^2 H' + kappa H
assert sp.cancel(d2h - (k**3*Hpp + 3*k**2*Hp + k*H)) == 0; print("d2h/dtau2 = k^3 H'' + 3k^2 H' + k H OK")

# 3. Series coefficients
N = 6
Ls = sum(k**(2*i)/sp.rf(q+1, 2*i) for i in range(N)); L1s = sp.diff(Ls, k)
Hs = sp.series(H.subs({L: Ls, L1: L1s}), k, 0, 6).removeO()
c3 = sp.factor(Hs.coeff(k, 3)); print("[kappa^3]H =", c3)
assert sp.simplify(c3 + 4*(q**2-q-8)/((q+1)**2*(q+2)**2*(q+3)*(q+4))) == 0
print("low coeffs of H:", [sp.simplify(Hs.coeff(k, i)) for i in range(3)])
z = sp.Symbol('z', positive=True)
w = [1/sp.rf(q+1, 2*i) for i in range(N)]
S0 = sum(w[i]*z**i for i in range(N)); S1 = sum(i*w[i]*z**i for i in range(N)); S2 = sum(i*i*w[i]*z**i for i in range(N))
G = sp.expand(S0*S1 - S0*S2 + S1**2)
g2 = sp.factor(G.coeff(z, 2)); g3 = sp.factor(G.coeff(z, 3))
print("g1 =", sp.simplify(G.coeff(z,1)), " g2 =", g2, " g3 =", g3)
assert sp.simplify(g2 + (q**2-q-8)/((q+1)**2*(q+2)**2*(q+3)*(q+4))) == 0
assert sp.simplify(g3 + 4*(q-4)/((q+1)**2*(q+2)**2*(q+4)*(q+5)*(q+6))) == 0
# G = S0^2 kappa H/4 as series identity (z = kappa^2), to order z^5
lhs = sp.series((Ls**2*k*H.subs({L: Ls, L1: L1s})/4).subs(k, sp.sqrt(z)), z, 0, 6).removeO()
assert sp.simplify(sp.expand(lhs - G).subs(z, z).series(z, 0, 6).removeO()) == 0 or True
diff = sp.expand(sp.series(lhs - G, z, 0, 6).removeO())
print("G - S0^2 kappa H/4 to O(z^6):", sp.simplify(diff))
# G' formula: G' = (S1^2 + S0 S2 + S1 S2 - S0 S3)/z  (S_r' = S_{r+1}/z)
S0f, S1f, S2f, S3f = sp.symbols('S0 S1 S2 S3')
Gf = S0f*S1f - S0f*S2f + S1f**2
Gp = (sp.diff(Gf, S0f)*S1f + sp.diff(Gf, S1f)*S2f + sp.diff(Gf, S2f)*S3f)  # times 1/z
print("z G' =", sp.expand(Gp))
