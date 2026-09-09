"""Check the (unproved) formula of prove_D2 Sec. 2.3:
   deg(P H_P^{-1}) = fdeg(P) + #{zeros of det U in D},   P = M U,
using the author's own numerical pipeline on more witnesses than the report tested
(double base point, two base points, non-diagonal U, one inside + one outside)."""
import sys
sys.path.insert(0, '../scratch_D2')
import grassmann_degree_exact as G
import inner_interpolant_numeric as NUM
from sympy import Matrix, Rational
z = G.z
zetas, Ws, Qs, P0 = G.instance_from_curve(4, 2, 4, (1, 2), seed=5)
p1, p2 = P0[:, 0], P0[:, 1]
cases = [
    ("U=diag(1,(z-1/2)(z-1/3)): two base points in D, predict 3+2=5", Matrix.hstack(p1, (z - Rational(1, 2)) * (z - Rational(1, 3)) * p2), 5),
    ("U=(z-1/2) I: double base point, predict 3+2=5", Matrix.hstack((z - Rational(1, 2)) * p1, (z - Rational(1, 2)) * p2), 5),
    ("U=diag(z-1/2, z-2): one inside one outside, predict 3+1=4", Matrix.hstack((z - Rational(1, 2)) * p1, (z - 2) * p2), 4),
    ("U=[[z-1/2, 1],[0,1]] non-diagonal, det=z-1/2, predict 4", P0 * Matrix([[z - Rational(1, 2), 1], [0, 1]]), 4),
    ("U=[[z-1/2, z],[1,1]] unimodular-ish det=-1/2, col degrees (2,3), predict 3", P0 * Matrix([[z - Rational(1, 2), z], [1, 1]]), 3),
    ("U=diag(1, z^2-1/4): base points +-1/2, predict 5", Matrix.hstack(p1, (z ** 2 - Rational(1, 4)) * p2), 5),
]
for name, F, pred in cases:
    F = F.applyfunc(lambda x: x.expand())
    fd, g = G.forney_degree(F, 4, 2)
    print(f"##### {name}: Forney degree {fd}, gcd {g.as_expr()}")
    NUM.run_instance(name, 4, 2, zetas, Ws, Qs, F_witness=F)
    print(f"##### predicted compiler degree {pred}\n")
