import sympy as sp
k,a,c,m,mu,q = sp.symbols('kappa a c m mu q', positive=True)
Mf = sp.Function('M')(k)
# T1: Riccati from Kummer
M1 = sp.diff(Mf,k); M2 = sp.diff(Mf,k,2)
kummer_M2 = (a*Mf - (c-k)*M1)/k
mm = M1/Mf
ric_lhs = k*sp.diff(mm,k)
ric_rhs = a - (c-k)*mm - k*mm**2
print("T1 Riccati residual:", sp.simplify((ric_lhs-ric_rhs).subs(M2,kummer_M2)))
# H with paper's convention K = log M - mu k, mu=a/c: H = K' - k K'' = (m-mu) - k m'
mp_ = (a-(c-k)*m-k*m**2)/k
H = (m-a/c) - k*mp_
print("T1 H:", sp.factor(sp.simplify(H - (-k*m*(1-m)+(c+1)*(m-a/c)))))
# lambda' = H/(2R^2 b^2) with b=K'/R^2, lambda=k/(2b): check symbolically with K generic
Kf = sp.Function('K')(k); R2 = sp.symbols('R2',positive=True)
b = sp.diff(Kf,k)/R2; lam = k/(2*b)
print("lambda' check:", sp.simplify(sp.diff(lam,k) - (sp.diff(Kf,k)-k*sp.diff(Kf,k,2))/(2*R2*b**2)))
# F' = H, G = F/2 at stationary, G'' = -(2 lam/b) H
F = 2*Kf - k*sp.diff(Kf,k)
print("F'=H:", sp.simplify(sp.diff(F,k) - (sp.diff(Kf,k)-k*sp.diff(Kf,k,2))))
bb, ll = sp.symbols('b lambda', positive=True)
G = Kf.subs(k, 2*ll*bb) - ll*R2*bb**2
Gpp = sp.diff(G,bb,2)
# at stationary: K'(kap)=R2 b, ll = kap/(2b)
kap = sp.symbols('kap',positive=True)
Gpp_s = Gpp.subs(ll, kap/(2*bb)).doit()
Gpp_s = Gpp_s.subs(sp.Subs(sp.Derivative(Kf,(k,2)), k, kap), sp.Symbol('K2'))
print("G'' at stationary (raw):", sp.simplify(Gpp_s))
# expected: 4 lam^2 K'' - 2 lam R2 = 2lam(2 lam K'' - R2) ; with R2 = K'/b: -(2lam/b)(K' - kap K'')
# T2 identities
Psi = (c+1)*(m-a/c)/(m*(1-m))
Psip = sp.diff(Psi,m)
print("Psi':", sp.factor(sp.simplify(Psip - (c+1)*((m-a/c)**2 + (a/c)*(1-a/c))/(m*(1-m))**2)))
den = a - c*m + k*m*(1-m); Gm = k/den
print("den at Psi:", sp.simplify(den.subs(k,Psi) - (m-a/c)))
Delta = sp.simplify(Psip - Gm.subs(k,Psi))
print("Delta:", sp.factor(Delta), " claim diff:", sp.simplify(Delta + (c+1)*(m-a/c)*(1-2*m)/(m*(1-m))**2))
print("dG/dk:", sp.factor(sp.simplify(sp.diff(Gm,k))))
print("Psi(1/2) =", sp.factor(Psi.subs(m,sp.Rational(1,2))), " claim 2(c+1)(c-2a)/c")
mu_u = a*(c+1)/(c*(a+1))
print("Psi(m_u) =", sp.factor(sp.simplify(Psi.subs(m,mu_u))))
# small-k: cumulants of Beta(a,c-a)
N=8
Mser = sum(sp.rf(a,j)/sp.rf(c,j)*k**j/sp.factorial(j) for j in range(N+1))
K = sp.series(sp.log(Mser) - a/c*k, k, 0, 6).removeO()
Hs = sp.expand(sp.series(sp.diff(K,k) - k*sp.diff(K,k,2), k, 0, 5).removeO())
print("[k^0,k^1] H:", sp.simplify(Hs.coeff(k,0)), sp.simplify(Hs.coeff(k,1)))
c2 = sp.factor(sp.simplify(Hs.coeff(k,2))); c3 = sp.factor(sp.simplify(Hs.coeff(k,3)))
print("[k^2] H =", c2); print("[k^3] H =", c3); print("[k^3] H at c=2a:", sp.factor(c3.subs(c,2*a)))
# third central moment via Beta moments
al, be = a, c-a
EX = lambda r: sp.rf(al, r)/sp.rf(al+be, r)
mu3 = sp.factor(sp.simplify(EX(3) - 3*EX(1)*EX(2) + 2*EX(1)**3))
print("mu3 =", mu3, " check -mu3/2 - c2 =", sp.simplify(-mu3/2 - c2))
v = sp.factor(sp.simplify(EX(2)-EX(1)**2)); print("v =", v, " lambda0 = R2/(2v) =", sp.factor(sp.simplify((1-a/c)/(2*v))))
# T5: 0F1(;c;k^2/4)
z = sp.symbols('z', positive=True); w = sp.Function('w')(z)
Zf = w.subs(z, k**2/4)
ode = k*sp.diff(Zf,k,2) + (2*c-1)*sp.diff(Zf,k) - k*Zf
ode = ode.doit()
# use 0F1 ODE: z w'' + c w' - w = 0
D2 = sp.Derivative(w, (z,2)); D1 = sp.Derivative(w, z)
ode_s = ode.subs(sp.Subs(D2, z, k**2/4), sp.Symbol('W2')).subs(sp.Subs(D1, z, k**2/4), sp.Symbol('W1')).subs(Zf, sp.Symbol('W0'))
print("0F1 ODE in kappa (should be k*(z W2 + c W1 - W0) form):", sp.factor(ode_s))
# Kummer's second theorem check numerically-symbolically via series
cc = sp.Rational(7,3)
Z0 = sum((k**2/4)**j/(sp.rf(cc,j)*sp.factorial(j)) for j in range(12))
ap = cc - sp.Rational(1,2)
M2a = sum(sp.rf(ap,j)/sp.rf(2*ap,j)*(2*k)**j/sp.factorial(j) for j in range(24))
print("Kummer 2nd thm residual (series to k^10):", sp.series(Z0 - sp.exp(-k)*M2a, k, 0, 11))
# T7: L_q third-order ODE and identity
Lf = sp.Function('L')(k)
S = sp.diff(Lf,k) + q*(Lf-1)/k
ode2 = sp.expand(k*(k*sp.diff(S,k) - (k*Lf - q*S)))
claim2 = k**2*sp.diff(Lf,k,2) + 2*q*k*sp.diff(Lf,k) - (k**2 - q*(q-1))*Lf - q*(q-1)
print("2nd order:", sp.simplify(ode2-claim2))
claim3 = k**2*sp.diff(Lf,k,3) + (2*q+2)*k*sp.diff(Lf,k,2) + (q*(q+1)-k**2)*sp.diff(Lf,k) - 2*k*Lf
print("3rd order:", sp.simplify(sp.diff(claim2,k)-claim3))
mfun = sp.Function('m')(k)
m1, m2 = sp.diff(mfun,k), sp.diff(mfun,k,2)
ode3m = k**2*(m2+3*mfun*m1+mfun**3) + (2*q+2)*k*(m1+mfun**2) + (q*(q+1)-k**2)*mfun - 2*k
H7 = mfun - k*m1; H7p = sp.diff(H7,k)
m2sol = sp.solve(ode3m, m2)[0]
Dq = -k*mfun*(1-mfun**2) + (2*q+5)*mfun**2 - 2 + (q+1)*(q+2)*mfun/k
res = sp.simplify(H7p.subs(m2, m2sol) + (3*mfun+(2*q+2)/k)*H7 - Dq)
print("T7 identity residual (symbolic q):", res)
for qq in [2,3]:
    print(" q=",qq, sp.simplify(res.subs(q,qq)))
# weight: w'/w = 3m + (2q+2)/k with w = k^{2q+2} L^3
wgt = k**(2*q+2)*Lf**3
print("weight check:", sp.simplify(sp.diff(wgt,k)/wgt - (3*sp.diff(Lf,k)/Lf + (2*q+2)/k)))
# (s,u) form of u^2 k J with J = L L' - k L L'' + k L'^2 = L^2 H
Ls, Ss = sp.symbols('L S')
Lp = (k*Ss - q*Ls + q)/k; Sp = (k*Ls - q*Ss)/k
Lpp = sp.diff(Lp, k) + sp.diff(Lp, Ls)*Lp + sp.diff(Lp, Ss)*Sp
J = Ls*Lp - k*Ls*Lpp + k*Lp**2
s,u = sp.symbols('s u', positive=True)
expr = sp.expand(sp.simplify((k*J).subs(Ss, s*Ls).subs(Ls, 1/u)*u**2))
claim = -k**2*(1-s**2) + k*s*(1+2*q*u) - q*(1-u)*(q*u+2)
print("u^2 k J claim residual:", sp.simplify(expr - claim))
print("u^2 k J =", sp.collect(expr, k))
