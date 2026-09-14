"""Third-order ODE for L_q, the linear identity (k^{2q+2} L^3 H)' = k^{2q+2} L^3 Delta(m,k),
and the analogous identity for the 1F1 family."""
import sympy as sp
k, q = sp.symbols('kappa q', positive=True)
Lf = sp.Function('L')(k)
# second-order inhomogeneous ODE from the (L,S) system
S = sp.diff(Lf, k) + q*(Lf-1)/k
ode2 = sp.simplify(k*sp.diff(S, k) - (k*Lf - q*S))
ode2 = sp.simplify(ode2*k)
print("k*(kS' - (kL - qS)) =", sp.collect(sp.expand(ode2), [sp.diff(Lf,k,2), sp.diff(Lf,k), Lf]))
# claim: k^2 L'' + 2 q k L' - (k^2 - q(q-1)) L - q(q-1) = 0
claim2 = k**2*sp.diff(Lf,k,2) + 2*q*k*sp.diff(Lf,k) - (k**2 - q*(q-1))*Lf - q*(q-1)
assert sp.simplify(ode2 - claim2) == 0
# third-order homogeneous ODE
ode3 = sp.expand(sp.diff(claim2, k))
claim3 = k**2*sp.diff(Lf,k,3) + (2*q+2)*k*sp.diff(Lf,k,2) + (q*(q+1) - k**2)*sp.diff(Lf,k) - 2*k*Lf
assert sp.simplify(ode3 - claim3) == 0
print("third-order ODE: k^2 L''' + (2q+2) k L'' + (q(q+1) - k^2) L' - 2k L = 0  (verified)")
# in terms of m = L'/L: L''/L = m' + m^2, L'''/L = m'' + 3 m m' + m^3
m = sp.Function('m')(k)
mp1, mp2 = sp.diff(m, k), sp.diff(m, k, 2)
ode3m = k**2*(mp2 + 3*m*mp1 + m**3) + (2*q+2)*k*(mp1 + m**2) + (q*(q+1) - k**2)*m - 2*k
H = m - k*mp1
Hp = sp.diff(H, k)            # = -k m''
mpp_sol = sp.solve(ode3m, mp2)[0]
Hp_sub = sp.simplify(Hp.subs(mp2, mpp_sol))
Delta = -k*m*(1-m**2) + (2*q+5)*m**2 - 2 + (q+1)*(q+2)*m/k
alpha = 3*m + (2*q+2)/k
assert sp.simplify(Hp_sub + alpha*H - Delta) == 0
print("H' + (3m + (2q+2)/k) H = Delta(m,k)  with Delta = -k m(1-m^2) + (2q+5)m^2 - 2 + (q+1)(q+2)m/k  (verified)")
print("hence (k^{2q+2} L^3 H)' = k^{2q+2} L^3 Delta(m(k),k)")

# same for 1F1(a;c): Riccati k m' = a - (c-k) m - k m^2 ; H = m - a/c - k m'
a, c = sp.symbols('a c', positive=True)
mp1_sol = (a - (c-k)*m - k*m**2)/k
H1 = m - a/c - k*mp1
H1p = sp.diff(H1, k)  # involves m', m''
mpp1 = sp.diff(mp1_sol, k).subs(mp1, mp1_sol)   # m'' from Riccati
H1p_sub = sp.simplify(H1p.subs(mp2, mpp1).subs(mp1, mp1_sol))
H1_sub = sp.simplify(H1.subs(mp1, mp1_sol))
# find alpha, Delta1 with H1' + alpha H1 = Delta1 where Delta1 has no m' : both already functions of (m,k)
alpha1 = (c+1)/k - (1-2*m)
Delta1 = sp.simplify(H1p_sub + alpha1*H1_sub)
print("1F1: H' + ((c+1)/k - (1-2m)) H =", sp.factor(Delta1))
