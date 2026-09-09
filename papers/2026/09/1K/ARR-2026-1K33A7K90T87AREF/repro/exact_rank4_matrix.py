"""Exact (algebraic) rank-(m+1) optimizer of Section 7 for lambda = (2, 2, 3/2, 0, -5/2, -3)  [m = 3, z = 1].
Layering L'_3 = {-5/2}, {-3, 2}, {2, 0}, {3/2} with sigma_2(S_2) = 1/4 (the midpoint of the admissible interval [0, 1/2]).
Every entry of C is a Q-linear combination of square roots of integers; the residual C C^T - C^T C - 2F is
verified to be exactly zero in sympy.  Writes data/rank4_optimizer_exact.json and data/rank4_optimizer_30digits.txt.
Run: python exact_rank4_matrix.py   (about 3 s)."""
import json, itertools, os
import sympy as sp
from sympy import Rational as R, sqrt, Matrix, diag
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))
b2, b1, a1, a2, a3 = R(5, 2), R(3), R(2), R(2), R(3, 2)
# S_1 = b2 (scalar).  R_1 (on the layer {-b1, a1}) is rank one with trace b2:  R_1 = [[p, q], [q, b2 - p]], q^2 = p(b2 - p).
# S_2 = R_1 - diag(-b1, a1) has trace A_2 = 7/2; we prescribe its spectrum (13/4, 1/4), i.e. det = 13/16:
#     det(R_1 - D_1) = (p + b1)(b2 - a1 - p) - p(b2 - p) = b1(b2 - a1) - p(b1 + a1)  ->  p = (b1(b2 - a1) - 13/16)/(b1 + a1) = 11/80.
sigma = R(1, 4)
p = (b1 * (b2 - a1) - sigma * (R(7, 2) - sigma)) / (b1 + a1)
q = sqrt(p * (b2 - p))
R1 = Matrix([[p, q], [q, b2 - p]]); D1 = diag(-b1, a1); S2 = R1 - D1
assert S2.eigenvals() == {R(13, 4): 1, R(1, 4): 1}
# R_2 (on the layer {a2, 0}) has the spectrum of S_2 and S_3 = R_2 - diag(a2, 0) must be rank one (trace a3 = 3/2):
#     R_2 = [[u, w], [w, 7/2 - u]], u(7/2 - u) - w^2 = 13/16, det(R_2 - D_2) = 0  ->  u = 99/32, w^2 = 455/1024.
u = (R(7, 2) * a2 - R(13, 16)) / a2 if False else R(99, 32)
w = sqrt(u * (R(7, 2) - u) - R(13, 16))
R2 = Matrix([[u, w], [w, R(7, 2) - u]]); D2 = diag(a2, 0); S3 = R2 - D2
assert R2.eigenvals() == {R(13, 4): 1, R(1, 4): 1} and S3.eigenvals() == {a3: 1, 0: 1}
# blocks M_t with M_t M_t^T = 2 R_t and M_t^T M_t = 2 S_t
c = Matrix([sqrt(2 * p), sqrt(2) * q / sqrt(p)]).applyfunc(sp.radsimp)          # M_1 (column)
r = (-sqrt(2) * Matrix([[sqrt(S3[0, 0]), S3[0, 1] / sqrt(S3[0, 0])]])).applyfunc(sp.radsimp)   # M_3 (row)
def eigvecs(M, vals):
    cols = []
    for lam in vals:
        v = (M - lam * sp.eye(2)).nullspace()[0]; v = v / sp.sqrt(v.dot(v)); cols.append(v.applyfunc(sp.radsimp))
    return Matrix.hstack(*cols)
vals = [R(13, 4), R(1, 4)]
U, V = eigvecs(R2, vals), eigvecs(S2, vals)
M2 = (sqrt(2) * U * diag(sqrt(vals[0]), sqrt(vals[1])) * V.T).applyfunc(lambda x: sp.radsimp(sp.expand(x)))
assert sp.simplify(M2 * M2.T - 2 * R2) == sp.zeros(2) and sp.simplify(M2.T * M2 - 2 * S2) == sp.zeros(2)
C = sp.zeros(6, 6); C[1:3, 0:1] = c; C[3:5, 1:3] = M2; C[5:6, 3:5] = r
F = diag(-b2, -b1, a1, a2, 0, a3)
res = (C * C.T - C.T * C - 2 * F).applyfunc(lambda x: sp.simplify(sp.radsimp(x)))
assert res == sp.zeros(6, 6), "exact residual is not zero"
cost = sp.simplify(sum(x ** 2 for x in C) / 2); assert cost == R(15, 2)
spec = (C * C.T / 2).applyfunc(sp.simplify).eigenvals(); assert spec == {R(13, 4): 1, R(5, 2): 1, R(3, 2): 1, R(1, 4): 1, 0: 2}
print("basis order: (-b2, -b1, a1, a2, 0, a3) = (-5/2, -3, 2, 2, 0, 3/2)")
print("exact residual C C^T - C^T C - 2F == 0 : True;  cost 1/2||C||^2 =", cost, ";  common spectrum", spec)
entries = {}
for i in range(6):
    for j in range(6):
        if C[i, j] != 0:
            entries[f"C[{i+1},{j+1}]"] = {"exact": str(C[i, j]), "decimal30": str(sp.N(C[i, j], 30))}
            print(f"C[{i+1},{j+1}] = {C[i, j]}  =  {sp.N(C[i, j], 30)}")
Cf = np.array(C.evalf(20).tolist(), dtype=float); Ff = np.diag([-2.5, -3, 2, 2, 0, 1.5])
r64 = np.linalg.norm(Cf @ Cf.T - Cf.T @ Cf - 2 * Ff); Cr = np.round(Cf, 4); r4 = np.linalg.norm(Cr @ Cr.T - Cr.T @ Cr - 2 * Ff)
print("float64 residual of the exact entries: %.2e ;  residual after rounding to 4 decimals: %.3e ;  rank %d" % (r64, r4, np.linalg.matrix_rank(Cf, tol=1e-9)))
json.dump({"lambda": ["-5/2", "-3", "2", "2", "0", "3/2"], "basis_order": "(-b2,-b1,a1,a2,0,a3)", "layering": "{-5/2},{-3,2},{2,0},{3/2}",
           "sigma2_S2": "1/4", "cost": "15/2", "common_spectrum": ["13/4", "5/2", "3/2", "1/4", "0", "0"], "entries": entries,
           "float64_residual": r64, "residual_rounded_4_decimals": r4}, open("data/rank4_optimizer_exact.json", "w"), indent=1)
with open("data/rank4_optimizer_30digits.txt", "w") as f:
    f.write("# C for lambda=(2,2,3/2,0,-5/2,-3), basis (-b2,-b1,a1,a2,0,a3); 30 significant digits; row-major, 6 x 6\n")
    for i in range(6): f.write(" ".join(str(sp.N(C[i, j], 30)) if C[i, j] != 0 else "0" for j in range(6)) + "\n")
print("written data/rank4_optimizer_exact.json, data/rank4_optimizer_30digits.txt")
