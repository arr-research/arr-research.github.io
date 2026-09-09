import sys; sys.path.insert(0, '.')
import grassmann_degree_exact as G
import inner_interpolant_numeric as NUM
from sympy import Matrix, Rational, Poly, zeros
z = G.z
# (a) base point outside the closed disc (z=2) and at infinity (leading-coefficient drop)
zetas, Ws, Qs, P0 = G.instance_from_curve(4, 2, 4, (1, 2), seed=5)
Fb2 = Matrix.hstack(P0[:, 0], (z - 2) * P0[:, 1])
NUM.run_instance("same (1,2)-data, witness with base point z=2 (outside closed disc), col degrees (1,3)", 4, 2, zetas, Ws, Qs, F_witness=Fb2)
Fb3 = Matrix.hstack(P0[:, 0], P0[:, 1] + z * P0[:, 0])   # column degrees (1,2) but leading coefficients dependent -> base point at infinity
fd, g = G.forney_degree(Fb3, 4, 2)
print("witness with base point at infinity: column degrees (1,2), Forney degree", fd, "gcd", g.as_expr())
NUM.run_instance("same (1,2)-data, witness with base point at infinity (dependent leading coefficients)", 4, 2, zetas, Ws, Qs, F_witness=Fb3)
# (b) Gr(2,3) = P^2 duality: 2-planes in C^3 <-> annihilator lines; compare with 6M3V generic ⌊L(r-1)/r⌋
for L in [4, 5, 6]:
    zetas, Ws, Qs = G.instance_random(3, 2, L, 100 + L)
    res = G.delta_gr_k2(3, Qs, zetas, Ws, verbose=False)
    print(f"Gr(2,3), L={L}: delta_Gr = {res[0]} (column degrees {res[1]}); 6M3V generic line law floor(L*2/3) = {2*L//3}; k=1 exact check on the dual lines:")
    # dual: lines ell_i = Q_i^T (annihilator, 1x3) in C^3; least degree of vector polynomial p (3x1) with p(zeta_i) ∝ ell_i^T
    ells = [Matrix(Q).T for Q in Qs]      # 3x1 each
    Qd = [G.left_annihilator(l) for l in ells]  # 2x3 annihilators of the lines
    for e in range(0, 6):
        V = G.V_space(3, e, Qd, zetas)
        if V.shape[1] > 0:
            # need a vector nonzero at all nodes: generic element works iff evaluation at each node is not identically zero on V
            ok = all(not (G.eval_matrix(3, e, zt) * V).is_zero_matrix for zt in zetas)
            if ok:
                print(f"   dual k=1 projective degree = {e}"); break
