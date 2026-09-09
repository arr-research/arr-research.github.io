"""Independent symbolic verification of the workshop's counterexample to the last clause of Theorem 6.1,
and of the new explicit witness data Y_i = graph(zeta_i^e I_2) used to prove Theorem 7.4 for all L."""
import sympy as s, itertools
z = s.symbols('z')
def sharp(M): return M.subs(z, 1/s.conjugate(z)).H  # F^sharp(z) = F(1/conj z)^*  (paraconjugate)
# --- workshop counterexample ---
P = s.Matrix([z+1, z*(z-1)])
S1 = s.Matrix([[z+1, z-1],[z-1, z+1]])/2
S2 = s.diag(1, z)*S1
th = s.symbols('theta', real=True); w = s.exp(s.I*th)
def on_circle(M): return s.simplify((M.H*M).subs(z, w).subs(s.conjugate(w), 1/w)) if False else s.simplify(s.expand((M.subs(z,w)).H*(M.subs(z,w))))
print("S1^*S1 on T:", on_circle(S1))
print("S2^*S2 on T:", on_circle(S2))
print("det S1 =", s.factor(S1.det()), "; det S2 =", s.factor(S2.det()))
print("gcd of coordinates of P:", s.gcd(P[0], P[1]))
print("P^*P on T:", s.simplify(s.expand((P.subs(z,w)).H*(P.subs(z,w)))))
print("P(1) =", list(P.subs(z,1)), " P(-1) =", list(P.subs(z,-1)))
print("S1(1)e1 =", list(S1.subs(z,1)[:,0]), " S1(-1)e1 =", list(S1.subs(z,-1)[:,0]))
print("S2 first column == P/2:", s.simplify(S2[:,0]-P/2) == s.zeros(2,1))
# McMillan degrees via Hankel rank of Taylor coefficients
def mcmillan(F, terms=8):
    Fs = [F.subs(z,0)]
    G = F
    for t in range(1, terms):
        G = s.diff(G, z)
        Fs.append((G.subs(z,0))/s.factorial(t))
    n = terms//2
    H = s.BlockMatrix([[Fs[a+b+1] for b in range(n)] for a in range(n)]).as_explicit()
    return H.rank()
print("deg S1 =", mcmillan(S1), "; deg S2 =", mcmillan(S2), "; deg P/2 =", mcmillan(P/2))
# fdeg(P) = 2 (max coordinate degree 2, gcd 1); delta_Gr = 1 (witness (z+1, z-1))
Q = s.Matrix([z+1, z-1]); print("degree-1 witness Q(1), Q(-1):", list(Q.subs(z,1)), list(Q.subs(z,-1)))
# --- new witness construction for Gr(2,4): Y_i = graph(zeta_i^e I_2) ---
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix
CIRCLE = [s.Rational(3,5)+s.Rational(4,5)*s.I, s.Rational(5,13)+s.Rational(12,13)*s.I, s.Rational(8,17)+s.Rational(15,17)*s.I,
          s.Rational(7,25)+s.Rational(24,25)*s.I, s.Rational(20,29)+s.Rational(21,29)*s.I, s.Rational(9,41)+s.Rational(40,41)*s.I,
          s.Rational(12,37)+s.Rational(35,37)*s.I, 1, s.I, -1, -s.I, s.Rational(-3,5)+s.Rational(4,5)*s.I]
def nullity(A):
    D = DomainMatrix.from_Matrix(A.applyfunc(s.expand)).convert_to(QQ_I)
    return A.shape[1]-D.rank()
def dimV(N, e, Qs, zetas):
    rows = [Qm*s.Matrix.hstack(*[zt**t*s.eye(N) for t in range(e+1)]) for Qm, zt in zip(Qs, zetas)]
    return nullity(s.Matrix.vstack(*rows))
print("\nGr(2,4) witness Y_i = graph(zeta_i^e I_2), e = floor(L/2):")
for L in range(1, 13):
    e = L//2; zetas = CIRCLE[:L]
    Qs = [s.Matrix.hstack(-zt**e*s.eye(2), s.eye(2)) for zt in zetas]   # annihilator rows of graph(zt^e I)
    dims = [dimV(4, ee, Qs, zetas) for ee in range(0, e+2)]
    m0 = 4*(e+1)-2*L
    print(f"  L={L:2d} e0={e} m0={m0}  dim V_0..V_{e+1} = {dims}   (expect V_e'=0 for e'<e, dim V_e = m0)")
    assert all(d == 0 for d in dims[:e]) and dims[e] == m0
    # generalised r=2k check for k=3
    Qs3 = [s.Matrix.hstack(-zt**e*s.eye(3), s.eye(3)) for zt in zetas]
    dims3 = [dimV(6, ee, Qs3, zetas) for ee in range(0, e+1)]
    m03 = 6*(e+1)-3*L
    assert all(d == 0 for d in dims3[:e]) and dims3[e] == m03, (L, dims3, m03)
print("k=3, r=6 graph witness: V_e'=0 for e'<e and dim V_e = m0 for L=1..12: OK")
# Forney degree of the witness pencil [e1; z^e e1], [e2; z^e e2]
for e in range(1,4):
    Pw = s.Matrix([[1,0],[0,1],[z**e,0],[0,z**e]])
    minors = [Pw.extract(list(r), [0,1]).det() for r in itertools.combinations(range(4),2)]
    nz = [m for m in minors if m != 0]
    g = nz[0]
    for m in nz[1:]: g = s.gcd(g, m)
    print(f"  e={e}: minors {minors}, gcd {g}, fdeg {max(s.degree(m, z) for m in nz) - s.degree(g, z)}")
