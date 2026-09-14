"""Tools for the (m,3) stratum: joint hive LP with lambda as variables (validity of a form),
chamber-radius LP (exposedness relative to a form set), chamber-vertex completeness check.
Form f = (alpha_1..alpha_m, beta_1, beta_2): f(lam) = alpha.a + beta_1 b_1 + beta_2 b_2 (beta_3 = 0)."""
import numpy as np, itertools
from fractions import Fraction as Q
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, lil_matrix, hstack, vstack
from hive_core import HiveLP, hive_index, rhombi
from m3_forms import spec_m3

class JointLP:
    """min  sum s - f(a,b)  over hive h, s, a (m), b (3): rhombus ineqs, boundary equalities with lambda = (a, 0^z, -b3,-b2,-b1),
    a_1>=..>=a_m>=0, b_1>=b_2>=b_3>=0, sum a = 1, sum b = 1.  Value >= 0 iff f is a valid lower bound on the (P=1) stratum."""
    def __init__(self, m, z):
        self.m, self.z = m, z; d = m + z + 3; self.d = d
        M = HiveLP(d); self.M = M; H = M.H; nv = M.nv
        self.nx = nv + m + 3   # extra columns: a_1..a_m, b_1,b_2,b_3
        # inequality block: hive rows (pad columns), then a-order, b-order
        Aub = lil_matrix((M.Aub.shape[0] + (m - 1) + 2, self.nx))
        Aub[:M.Aub.shape[0], :nv] = M.Aub
        r = M.Aub.shape[0]
        for j in range(m - 1):
            Aub[r, nv + j] = -1; Aub[r, nv + j + 1] = 1; r += 1     # a_{j+1} - a_j <= 0
        for j in range(2):
            Aub[r, nv + m + j] = -1; Aub[r, nv + m + j + 1] = 1; r += 1
        self.Aub = csr_matrix(Aub); self.bub = np.zeros(Aub.shape[0])
        # equality block: M.Aeq with lambda rows getting -a_t / +b coefficients; plus sum a = 1, sum b = 1
        Aeq = lil_matrix((M.neq + 2, self.nx)); Aeq[:M.neq, :nv] = M.Aeq
        for t, row in enumerate(M.lam_rows):
            if t < m: Aeq[row, nv + t] = -1.0                       # h(q)-h(p) - a_t = 0
            elif t < m + z: pass                                     # zero
            else:
                k = t - m - z                                        # 0 -> -b3, 1 -> -b2, 2 -> -b1
                Aeq[row, nv + m + (2 - k)] = 1.0                     # h(q)-h(p) + b = 0
        Aeq[M.neq, nv:nv + m] = 1.0; Aeq[M.neq + 1, nv + m:nv + m + 3] = 1.0
        self.Aeq = csr_matrix(Aeq); self.beq = np.zeros(M.neq + 2); self.beq[M.neq] = 1; self.beq[M.neq + 1] = 1
        self.bounds = [(None, None)] * H + [(0, None)] * d + [(0, None)] * (m + 3)

    def validity(self, f):
        """Return (min value, argmin lambda). f valid iff value >= -tol."""
        c = np.zeros(self.nx); nv = self.M.nv; c[self.M.H:nv] = 1.0
        for j in range(self.m): c[nv + j] = -f[j]
        c[nv + self.m] = -f[self.m]; c[nv + self.m + 1] = -f[self.m + 1]
        res = linprog(c, A_ub=self.Aub, b_ub=self.bub, A_eq=self.Aeq, b_eq=self.beq, bounds=self.bounds, method='highs')
        if res.status != 0: return None, None
        x = res.x; a = x[nv:nv + self.m]; b = x[nv + self.m:nv + self.m + 3]
        return res.fun, (a, b)

def form_val(f, a, b):
    m = len(a); return float(np.dot(f[:m], a) + f[m] * b[0] + f[m + 1] * b[1])

def radius(f, others, m, strict=False):
    """max t s.t. f(lam) - g(lam) >= t for all g in others, lam in the P=1 stratum. t>0 <=> f is a unique max on an open set.
    Variables a (m), b (3), t."""
    n = m + 4
    A = []; ub = []
    for g in others:
        row = np.zeros(n); row[:m] = g[:m] - f[:m]; row[m] = g[m] - f[m]; row[m + 1] = g[m + 1] - f[m + 1]; row[n - 1] = 1
        A.append(row); ub.append(0.0)          # g - f + t <= 0
    st = 1.0 if strict else 0.0
    for j in range(m - 1):
        row = np.zeros(n); row[j] = -1; row[j + 1] = 1; row[n - 1] = st; A.append(row); ub.append(0.0)
    row = np.zeros(n); row[m - 1] = -1; row[n - 1] = st; A.append(row); ub.append(0.0)
    for j in range(2):
        row = np.zeros(n); row[m + j] = -1; row[m + j + 1] = 1; row[n - 1] = st; A.append(row); ub.append(0.0)
    row = np.zeros(n); row[m + 2] = -1; row[n - 1] = st; A.append(row); ub.append(0.0)
    Aeq = np.zeros((2, n)); Aeq[0, :m] = 1; Aeq[1, m:m + 3] = 1
    c = np.zeros(n); c[-1] = -1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(ub), A_eq=Aeq, b_eq=[1, 1],
                  bounds=[(0, None)] * (m + 3) + [(None, 1)], method='highs')
    if res.status != 0: return None, None
    return -res.fun, (res.x[:m], res.x[m:m + 3])

def chamber_vertices(f, others, m, tol=1e-9):
    """Vertices of C_f = {lam in stratum(P=1): f >= g for all g in others}, by brute-force basis enumeration in the
    (m+1)-dimensional affine space (a_1..a_m, b_1, b_2 with b_3 = 1 - b_1 - b_2, a_m = 1 - sum a_{<m}).
    Returns list of (a, b) as float arrays (deduplicated). Feasible for m <= 6 or so."""
    # coordinates x = (a_1..a_{m-1}, b_1, b_2); a_m = 1 - sum; b_3 = 1 - b1 - b2
    n = m + 1
    def lift(x):
        a = np.concatenate([x[:m - 1], [1 - x[:m - 1].sum()]]); b = np.array([x[m - 1], x[m], 1 - x[m - 1] - x[m]])
        return a, b
    def lin(coef_a, coef_b):   # coef.a + coef.b as affine in x: returns (row, const)
        row = np.zeros(n); row[:m - 1] = coef_a[:m - 1] - coef_a[m - 1]; row[m - 1] = coef_b[0] - coef_b[2]; row[m] = coef_b[1] - coef_b[2]
        const = coef_a[m - 1] + coef_b[2]
        return row, const
    ineq = []   # row.x + const >= 0
    for g in others:
        ca = f[:m] - g[:m]; cb = np.array([f[m] - g[m], f[m + 1] - g[m + 1], 0.0]); ineq.append(lin(ca, cb))
    for j in range(m - 1):   # a_j - a_{j+1} >= 0
        ca = np.zeros(m); ca[j] = 1; ca[j + 1] = -1; ineq.append(lin(ca, np.zeros(3)))
    ca = np.zeros(m); ca[m - 1] = 1; ineq.append(lin(ca, np.zeros(3)))          # a_m >= 0
    for j in range(2):
        cb = np.zeros(3); cb[j] = 1; cb[j + 1] = -1; ineq.append(lin(np.zeros(m), cb))
    cb = np.zeros(3); cb[2] = 1; ineq.append(lin(np.zeros(m), cb))              # b_3 >= 0
    A = np.array([r for r, c in ineq]); C = np.array([c for r, c in ineq])
    verts = []
    for S in itertools.combinations(range(len(ineq)), n):
        Asub = A[list(S)]
        if abs(np.linalg.det(Asub)) < 1e-12: continue
        x = np.linalg.solve(Asub, -C[list(S)])
        if np.all(A @ x + C >= -tol):
            if not any(np.linalg.norm(x - v) < 1e-7 for v in verts): verts.append(x)
    return [lift(v) for v in verts]


def chamber_vertices_qhull(f, others, m, tol=1e-9):
    """Same as chamber_vertices but via scipy HalfspaceIntersection (needs a strictly interior point)."""
    from scipy.spatial import HalfspaceIntersection
    n = m + 1
    def lift(x):
        a = np.concatenate([x[:m - 1], [1 - x[:m - 1].sum()]]); b = np.array([x[m - 1], x[m], 1 - x[m - 1] - x[m]])
        return a, b
    def lin(coef_a, coef_b):
        row = np.zeros(n); row[:m - 1] = coef_a[:m - 1] - coef_a[m - 1]; row[m - 1] = coef_b[0] - coef_b[2]; row[m] = coef_b[1] - coef_b[2]
        const = coef_a[m - 1] + coef_b[2]
        return row, const
    ineq = []
    for g in others:
        ca = f[:m] - g[:m]; cb = np.array([f[m] - g[m], f[m + 1] - g[m + 1], 0.0]); ineq.append(lin(ca, cb))
    for j in range(m - 1):
        ca = np.zeros(m); ca[j] = 1; ca[j + 1] = -1; ineq.append(lin(ca, np.zeros(3)))
    ca = np.zeros(m); ca[m - 1] = 1; ineq.append(lin(ca, np.zeros(3)))
    for j in range(2):
        cb = np.zeros(3); cb[j] = 1; cb[j + 1] = -1; ineq.append(lin(np.zeros(m), cb))
    cb = np.zeros(3); cb[2] = 1; ineq.append(lin(np.zeros(m), cb))
    A = np.array([r for r, c in ineq]); C = np.array([c for r, c in ineq])
    # halfspaces in qhull form: A x + C >= 0  ->  (-A) x - C <= 0 : rows [-A, -C]
    H = np.hstack([-A, -C[:, None]])
    # interior point: Chebyshev centre via LP
    norms = np.linalg.norm(A, axis=1)
    cc = np.zeros(n + 1); cc[-1] = -1
    Aub = np.hstack([-A, norms[:, None]]); bub = C
    res = linprog(cc, A_ub=Aub, b_ub=bub, bounds=[(None, None)] * n + [(0, None)], method='highs')
    if res.status != 0 or res.x[-1] < 1e-9: return []
    hs = HalfspaceIntersection(H, res.x[:n])
    verts = []
    for x in hs.intersections:
        if not any(np.linalg.norm(x - v) < 1e-7 for v in verts): verts.append(x)
    return [lift(v) for v in verts]
