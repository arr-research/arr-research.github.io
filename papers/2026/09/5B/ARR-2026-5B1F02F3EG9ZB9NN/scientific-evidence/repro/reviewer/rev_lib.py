"""rev_lib.py -- reviewer's own tools (written independently of the author's code).

Horn triples (recursive definition), LR coefficients (tableau rule), Horn LP (float), hive LP (float, h-only
formulation), exact hive primal/dual checkers (Fractions), geometry helpers.
"""
from fractions import Fraction as Q
import itertools, functools, json, gzip
import numpy as np
from scipy.optimize import linprog

# ----------------------------------------------------------------------------- Horn triples (recursive)
@functools.lru_cache(None)
def horn_list(r, n):
    """T^n_r as a tuple of (I,J,K), each an increasing tuple of 1-based indices."""
    if r >= n:
        return tuple()
    lower = [(q, horn_list(q, r)) for q in range(1, r)]
    subs = list(itertools.combinations(range(1, n + 1), r))
    tri = r * (r + 1) // 2
    out = []
    for I in subs:
        sI = sum(I)
        for J in subs:
            sIJ = sI + sum(J)
            for K in subs:
                if sum(K) + tri != sIJ:
                    continue
                if _lower_ok(I, J, K, lower):
                    out.append((I, J, K))
    return tuple(out)

def _lower_ok(I, J, K, lower):
    for q, Tq in lower:
        tq = q * (q + 1) // 2
        for F, G, H in Tq:
            if sum(I[f - 1] for f in F) + sum(J[g - 1] for g in G) > sum(K[h - 1] for h in H) + tq:
                return False
    return True

def horn_member(I, J, K, n):
    """Membership of (I,J,K) in T^n_r by the recursive definition (does not build T^n_r itself)."""
    I, J, K = tuple(sorted(I)), tuple(sorted(J)), tuple(sorted(K))
    r = len(I)
    if not (len(J) == len(K) == r and r >= 1):
        return False
    for S in (I, J, K):
        if len(set(S)) != r or min(S) < 1 or max(S) > n:
            return False
    if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2:
        return False
    return _lower_ok(I, J, K, [(q, horn_list(q, r)) for q in range(1, r)])

def all_horn(n):
    return [t for r in range(1, n) for t in horn_list(r, n)]

# ----------------------------------------------------------------------------- LR coefficients
def part_of(S, n):
    """Partition attached to an index set S subset [n], |S| = r: (s_r - r, ..., s_1 - 1)."""
    S = sorted(S); r = len(S)
    return tuple(S[r - 1 - k] - (r - k) for k in range(r))

def lr_coeff(lam, mu, nu):
    """Littlewood-Richardson coefficient c^nu_{lam,mu}: number of semistandard skew tableaux of shape nu/lam and
    content mu whose reverse reading word (rows top to bottom, each row right to left) is a lattice word."""
    lam = [x for x in lam]; nu = [x for x in nu]; mu = [x for x in mu]
    L = max(len(lam), len(nu))
    lam += [0] * (L - len(lam)); nu += [0] * (L - len(nu))
    if any(lam[i] > nu[i] for i in range(L)):
        return 0
    if sum(nu) - sum(lam) != sum(mu):
        return 0
    m = len(mu)
    while m and mu[m - 1] == 0:
        m -= 1
    mu = mu[:m]
    if m == 0:
        return 1 if sum(nu) == sum(lam) else 0
    # cells to fill: row i, columns lam[i]..nu[i]-1 ; fill order: row by row, right to left
    cells = []
    for i in range(L):
        for c in range(nu[i] - 1, lam[i] - 1, -1):
            cells.append((i, c))
    ncell = len(cells)
    fill = {}
    counts = [0] * (m + 1)   # counts[k] = number of k placed so far (1-based letters)
    total = [0]

    def rec(t):
        if t == ncell:
            total[0] += 1
            return
        i, c = cells[t]
        # constraints: row weakly increasing left->right => entry <= right neighbour (filled earlier, at c+1)
        hi = m
        if (i, c + 1) in fill:
            hi = min(hi, fill[(i, c + 1)])
        # column strict: entry > entry above (if above cell is in the skew shape)
        lo = 1
        if i > 0 and (i - 1, c) in fill:
            lo = max(lo, fill[(i - 1, c)] + 1)
        for k in range(lo, hi + 1):
            if counts[k] >= mu[k - 1]:
                continue
            if k > 1 and counts[k] + 1 > counts[k - 1]:
                continue     # lattice condition
            fill[(i, c)] = k; counts[k] += 1
            rec(t + 1)
            counts[k] -= 1; del fill[(i, c)]
    rec(0)
    return total[0]

def horn_member_lr(I, J, K, n):
    """Membership in T^n_r via Knutson-Tao: c^{part(K)}_{part(I),part(J)} > 0 (plus size/sum sanity)."""
    I, J, K = tuple(sorted(I)), tuple(sorted(J)), tuple(sorted(K))
    r = len(I)
    if not (len(J) == len(K) == r) or any(len(set(S)) != r or min(S) < 1 or max(S) > n for S in (I, J, K)):
        return False
    return lr_coeff(part_of(I, n), part_of(J, n), part_of(K, n)) > 0

# ----------------------------------------------------------------------------- Horn LP (float)
def horn_lp(lam, T=None):
    """kappa_d(lam) = min sum s : s_1>=...>=s_d>=0, sum_K lam_k <= sum_I s_i - sum_J s_{d+1-j}."""
    d = len(lam)
    if T is None:
        T = all_horn(d)
    lamf = [float(x) for x in lam]
    A = []; b = []
    for I, J, K in T:
        row = np.zeros(d)
        for i in I: row[i - 1] -= 1
        for j in J: row[d - j] += 1
        A.append(row); b.append(-sum(lamf[k - 1] for k in K))
    for i in range(d - 1):
        row = np.zeros(d); row[i] = -1; row[i + 1] = 1
        A.append(row); b.append(0.0)
    res = linprog(np.ones(d), A_ub=np.array(A), b_ub=np.array(b), bounds=[(0, None)] * d, method='highs')
    assert res.status == 0, res.message
    return res.fun, res.x

# ----------------------------------------------------------------------------- hive geometry (own)
def hpoints(n):
    return [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]

def rhombi(n):
    """Unit rhombi of the order-n hive as (obtuse frozenset, acute frozenset), derived from the three lattice
    directions e1=(1,0), e2=(0,1), e3=e2-e1=(-1,1) with 60 degrees between e1,e2 and between e2,e3, 120 between e1,e3."""
    inside = lambda p: p[0] >= 0 and p[1] >= 0 and p[0] + p[1] <= n
    add = lambda p, v: (p[0] + v[0], p[1] + v[1])
    out = set()
    for p in hpoints(n):
        # family A: spanned by e1,e2 (60 deg at p): acute p, p+e1+e2 ; obtuse p+e1, p+e2
        quad = [p, add(p, (1, 0)), add(p, (0, 1)), add(p, (1, 1))]
        if all(inside(x) for x in quad):
            out.add((frozenset((quad[1], quad[2])), frozenset((quad[0], quad[3]))))
        # family B: spanned by e2,e3 (60 deg at p): acute p, p+e2+e3 = p+(-1,2); obtuse p+e2, p+e3
        quad = [p, add(p, (0, 1)), add(p, (-1, 1)), add(p, (-1, 2))]
        if all(inside(x) for x in quad):
            out.add((frozenset((quad[1], quad[2])), frozenset((quad[0], quad[3]))))
        # family C: spanned by e1,e3 (120 deg at p): obtuse p, p+e1+e3 = p+(0,1); acute p+e1, p+e3
        quad = [p, add(p, (1, 0)), add(p, (-1, 1)), add(p, (0, 1))]
        if all(inside(x) for x in quad):
            out.add((frozenset((quad[0], quad[3])), frozenset((quad[1], quad[2]))))
    return out

def hive_lp(lam):
    """Own float hive LP in the h variables only: s_i := h(i,0)-h(i-1,0); objective h(n,0)."""
    n = len(lam); pts = hpoints(n); idx = {p: k for k, p in enumerate(pts)}; nv = len(pts)
    R = rhombi(n)
    A = []; b = []
    for ob, ac in R:
        row = np.zeros(nv)
        for p in ac: row[idx[p]] += 1
        for p in ob: row[idx[p]] -= 1
        A.append(row); b.append(0.0)
    # ordering s_i >= s_{i+1} (redundant) and s_n >= 0
    for i in range(1, n):
        row = np.zeros(nv); row[idx[(i + 1, 0)]] += 1; row[idx[(i, 0)]] -= 2; row[idx[(i - 1, 0)]] += 1
        A.append(row); b.append(0.0)
    row = np.zeros(nv); row[idx[(n, 0)]] -= 1; row[idx[(n - 1, 0)]] += 1; A.append(row); b.append(0.0)
    Aeq = []; beq = []
    row = np.zeros(nv); row[idx[(0, 0)]] = 1; Aeq.append(row); beq.append(0.0)
    for j in range(1, n + 1):
        row = np.zeros(nv); row[idx[(0, j)]] += 1; row[idx[(0, j - 1)]] -= 1; Aeq.append(row); beq.append(float(lam[j - 1]))
    for k in range(1, n + 1):   # h(n-k,k)-h(n-k+1,k-1) = -(h(n+1-k,0)-h(n-k,0))
        row = np.zeros(nv); row[idx[(n - k, k)]] += 1; row[idx[(n - k + 1, k - 1)]] -= 1
        row[idx[(n + 1 - k, 0)]] += 1; row[idx[(n - k, 0)]] -= 1
        Aeq.append(row); beq.append(0.0)
    c = np.zeros(nv); c[idx[(n, 0)]] = 1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(b), A_eq=np.array(Aeq), b_eq=np.array(beq),
                  bounds=[(None, None)] * nv, method='highs')
    assert res.status == 0, res.message
    return res.fun

# ----------------------------------------------------------------------------- exact hive checkers
def hive_from_json(n, h_den, h_int):
    pts = hpoints(n)
    assert len(h_int) == len(pts), (len(h_int), len(pts))
    return {p: Q(v, h_den) for p, v in zip(pts, h_int)}

def check_hive_primal(n, lam, s, h, R=None):
    """Exact: returns (ok, reason)."""
    if R is None: R = rhombi(n)
    if len(s) != n: return False, 'len s'
    if any(x < 0 for x in s): return False, 's<0'
    if any(s[i] < s[i + 1] for i in range(n - 1)): return False, 's not decreasing'
    if h[(0, 0)] != 0: return False, 'h(0,0)'
    for i in range(1, n + 1):
        if h[(i, 0)] - h[(i - 1, 0)] != s[i - 1]: return False, f'edge A {i}'
    for k in range(1, n + 1):
        if h[(n - k, k)] - h[(n - k + 1, k - 1)] != -s[n - k]: return False, f'edge B {k}'
    for j in range(1, n + 1):
        if h[(0, j)] - h[(0, j - 1)] != lam[j - 1]: return False, f'edge C {j}'
    for ob, ac in R:
        if sum(h[p] for p in ob) < sum(h[p] for p in ac): return False, f'rhombus {sorted(ob)} {sorted(ac)}'
    return True, ''

def check_hive_dual(n, lam, dual, R=None):
    """Exact weak-duality identity.  dual = {'y': [[o1,o2,a1,a2,val],...], 'z': [...], 'mu': [3n+1 values]}.
    We form  L(h,s) = sum s - sum_y y*(h(ob1)+h(ob2)-h(ac1)-h(ac2)) - sum_z z_k (s_k - s_{k+1}) - sgn*sum_mu mu_r*(row_r(h,s)-b_r)
    and require L == sum_i nu_i s_i with nu >= 0 and no h terms (for sgn = +1 or -1).  Then sum s >= value :=
    sgn*sum_r mu_r b_r for every feasible (h,s).  Returns (value or None, reason)."""
    if R is None: R = rhombi(n)
    y = []
    for o1, o2, a1, a2, v in dual['y']:
        v = Q(v)
        if v < 0: return None, 'y<0'
        key = (frozenset((tuple(o1), tuple(o2))), frozenset((tuple(a1), tuple(a2))))
        if key not in R: return None, f'not a rhombus {key}'
        y.append((key, v))
    z = [Q(v) for v in dual['z']]
    if len(z) != n - 1 or any(v < 0 for v in z): return None, 'z'
    mu = [Q(v) for v in dual['mu']]
    if len(mu) != 3 * n + 1: return None, 'mu len'
    # rows: r=0: h(0,0) = 0 ; r=i (1..n): h(i,0)-h(i-1,0)-s_i = 0 ; r=n+k: h(n-k,k)-h(n-k+1,k-1)+s_{n+1-k} = 0 ;
    # r=2n+j: h(0,j)-h(0,j-1) = lam_j
    for sgn in (Q(1), Q(-1)):
        ch = {p: Q(0) for p in hpoints(n)}; cs = [Q(1)] * n
        for (ob, ac), v in y:
            for p in ob: ch[p] -= v
            for p in ac: ch[p] += v
        for k in range(n - 1):
            cs[k] -= z[k]; cs[k + 1] += z[k]
        m = sgn * mu[0]; ch[(0, 0)] -= m
        for i in range(1, n + 1):
            m = sgn * mu[i]; ch[(i, 0)] -= m; ch[(i - 1, 0)] += m; cs[i - 1] += m
        for k in range(1, n + 1):
            m = sgn * mu[n + k]; ch[(n - k, k)] -= m; ch[(n - k + 1, k - 1)] += m; cs[n - k] -= m
        value = Q(0)
        for j in range(1, n + 1):
            m = sgn * mu[2 * n + j]; ch[(0, j)] -= m; ch[(0, j - 1)] += m; value += m * lam[j - 1]
        if all(v == 0 for v in ch.values()) and all(v >= 0 for v in cs):
            return value, f'sgn={sgn}'
    return None, 'identity fails'

# ----------------------------------------------------------------------------- misc
def load_json(fn):
    if fn.endswith('.gz'):
        with gzip.open(fn, 'rt', encoding='utf-8') as f: return json.load(f)
    with open(fn, encoding='utf-8') as f: return json.load(f)

def E_(a): return 2 * (1 - a[0])
def U_(a):
    N = len(a); return sum(abs(x - Q(1, N)) for x in a)
def Dstar(a, b): return min(E_(a) + U_(b), U_(a) + E_(b))
