import sys; sys.path.insert(0, '.')
import grassmann_degree_exact as G
import inner_interpolant_numeric as NUM
from sympy import Matrix
z = G.z
zetas, Ws, Qs, P0 = G.instance_from_curve(4, 2, 4, (1, 2), seed=5)
Fb4 = Matrix.hstack(P0[:, 0], z**2 * P0[:, 0] + P0[:, 1])   # column degrees (1,3), leading coefficients dependent: base point at infinity
fd, g = G.forney_degree(Fb4, 4, 2)
lead = Matrix.hstack(Matrix([Fb4[a,0].coeff(z,1) for a in range(4)]), Matrix([Fb4[a,1].expand().coeff(z,3) for a in range(4)]))
print("base point at infinity witness: column degrees (1,3), Forney degree", fd, "gcd", g.as_expr(), "rank of leading-coefficient matrix", lead.rank())
NUM.run_instance("same (1,2)-data, witness [f1, z^2 f1 + f2]: base point at infinity, col degrees (1,3)", 4, 2, zetas, Ws, Qs, F_witness=Fb4)
