"""Validity / exposedness LPs for general (m,n,z) (port of m3_tools.JointLP and radius to n negatives).
JointLP.validity(f): min over the P=1 stratum of kappa_d - f  (>= 0 iff f is a valid lower bound).
radius(f, others, m, n): Chebyshev-type radius of {f >= g for all g in others} inside the stratum (> 0 iff exposed)."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, lil_matrix
from hive_core import HiveLP

class JointLP:
    def __init__(self, m, n, z):
        self.m, self.n, self.z = m, n, z; d = m + z + n; self.d = d
        M = HiveLP(d); self.M = M; H = M.H; nv = M.nv
        self.nx = nv + m + n
        Aub = lil_matrix((M.Aub.shape[0] + (m - 1) + (n - 1), self.nx))
        Aub[:M.Aub.shape[0], :nv] = M.Aub
        r = M.Aub.shape[0]
        for j in range(m - 1):
            Aub[r, nv + j] = -1; Aub[r, nv + j + 1] = 1; r += 1
        for j in range(n - 1):
            Aub[r, nv + m + j] = -1; Aub[r, nv + m + j + 1] = 1; r += 1
        self.Aub = csr_matrix(Aub); self.bub = np.zeros(Aub.shape[0])
        Aeq = lil_matrix((M.neq + 2, self.nx)); Aeq[:M.neq, :nv] = M.Aeq
        for t, row in enumerate(M.lam_rows):
            if t < m: Aeq[row, nv + t] = -1.0
            elif t < m + z: pass
            else:
                k = t - m - z                     # 0 -> -b_n, ..., n-1 -> -b_1
                Aeq[row, nv + m + (n - 1 - k)] = 1.0
        Aeq[M.neq, nv:nv + m] = 1.0; Aeq[M.neq + 1, nv + m:nv + m + n] = 1.0
        self.Aeq = csr_matrix(Aeq); self.beq = np.zeros(M.neq + 2); self.beq[M.neq] = 1; self.beq[M.neq + 1] = 1
        self.bounds = [(None, None)] * H + [(0, None)] * d + [(0, None)] * (m + n)

    def validity(self, f):
        c = np.zeros(self.nx); nv = self.M.nv; c[self.M.H:nv] = 1.0
        for j in range(self.m): c[nv + j] = -f[j]
        for i in range(self.n - 1): c[nv + self.m + i] = -f[self.m + i]
        res = linprog(c, A_ub=self.Aub, b_ub=self.bub, A_eq=self.Aeq, b_eq=self.beq, bounds=self.bounds, method='highs')
        if res.status != 0: return None, None
        x = res.x; a = x[nv:nv + self.m]; b = x[nv + self.m:nv + self.m + self.n]
        return res.fun, (a, b)

def radius(f, others, m, n, strict=False):
    """max t s.t. f - g >= t for all g in others on the P=1 stratum (variables a (m), b (n), t); with strict=True the
    stratum inequalities also get slack t, so the returned point is interior to the stratum and to the chamber."""
    N = m + n + 1; A = []; ub = []; st = 1.0 if strict else 0.0
    f = np.array(f, float)
    for g in others:
        g = np.array(g, float); row = np.zeros(N)
        row[:m] = g[:m] - f[:m]; row[m:m + n - 1] = g[m:m + n - 1] - f[m:m + n - 1]; row[-1] = 1
        A.append(row); ub.append(0.0)
    for j in range(m - 1):
        row = np.zeros(N); row[j] = -1; row[j + 1] = 1; row[-1] = st; A.append(row); ub.append(0.0)
    row = np.zeros(N); row[m - 1] = -1; row[-1] = st; A.append(row); ub.append(0.0)
    for j in range(n - 1):
        row = np.zeros(N); row[m + j] = -1; row[m + j + 1] = 1; row[-1] = st; A.append(row); ub.append(0.0)
    row = np.zeros(N); row[m + n - 1] = -1; row[-1] = st; A.append(row); ub.append(0.0)
    Aeq = np.zeros((2, N)); Aeq[0, :m] = 1; Aeq[1, m:m + n] = 1
    c = np.zeros(N); c[-1] = -1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(ub), A_eq=Aeq, b_eq=[1, 1],
                  bounds=[(0, None)] * (m + n) + [(None, 1)], method='highs')
    if res.status != 0: return None, None
    return -res.fun, (res.x[:m], res.x[m:m + n])
