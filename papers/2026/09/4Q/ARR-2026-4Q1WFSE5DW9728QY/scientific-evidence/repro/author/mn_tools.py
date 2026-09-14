"""Tools for the inertia-(m,n) stratum: spectra, random sampling, hive LP wrapper, ordered layerings and their costs,
canonical form coordinates (beta_n := 0), level layerings of forms.

Spectrum: lambda = (a_1 >= ... >= a_m > 0, 0^z, -b_n, ..., -b_1), b_1 >= ... >= b_n > 0, sum a = sum b.
Spectrum index of a_j is j; of -b_i is d+1-i.
Form: (alpha_1..alpha_m; beta_1..beta_{n-1}) meaning sum alpha_j a_j + sum_{i<n} beta_i b_i (beta_n normalised to 0 via sum a = sum b).

Layering: list of layers, each a list of tokens ('a', j) / ('b', i) / ('z', 0). Layer 0 first.
cost(L) = sum_{u>=1} tail_u = sum_x t(x) x  (Lemma 2.1 of the (m,3) manuscript, valid for any n).
Ordered full-capacity layering: b-schedule u = (u_1..u_n) (layer index of b_i), c_u = #{i: u_i < u}; a_1, a_2, ... placed
in order, layer u >= 1 receiving exactly c_u a's while a's remain; the final layer receives the rest (<= its capacity, else split)."""
from __future__ import annotations
import itertools, numpy as np
from fractions import Fraction as Q
from hive_core import HiveLP

def spec(a, b, z=0):
    return np.array(list(a) + [0.0] * z + [-x for x in b[::-1]], float)

def rand_ab(m, n, rng, law='exp'):
    if law == 'exp':
        a = rng.exponential(size=m); b = rng.exponential(size=n)
    elif law == 'unif':
        a = rng.uniform(size=m); b = rng.uniform(size=n)
    elif law == 'sq':
        a = rng.normal(size=m) ** 2; b = rng.normal(size=n) ** 2
    elif law == 'tie':   # tie-heavy: few distinct values
        a = rng.integers(1, 4, size=m).astype(float); b = rng.integers(1, 4, size=n).astype(float)
    elif law == 'dom':   # dominant a_1, flat b
        a = rng.exponential(size=m); a[0] += 3 * a.sum(); b = 1 + 0.2 * rng.uniform(size=n)
    else:
        raise ValueError(law)
    a = np.sort(a)[::-1]; b = np.sort(b)[::-1]
    return a / a.sum(), b / b.sum()

LAWS = ['exp', 'unif', 'sq', 'tie', 'dom']

def canon(grad, m, n, z):
    """grad = d kappa / d lambda_k (length d). Returns (alpha_1..alpha_m, beta_1..beta_{n-1}) with beta_n := 0."""
    d = m + z + n
    alpha = np.array(grad[:m], float)
    beta = np.array([-grad[d - i] for i in range(1, n + 1)])   # beta_i = -grad at index of -b_i (0-based d-i)
    t = -beta[n - 1]
    return np.concatenate([alpha - t, beta[:n - 1] + t])

def form_val(f, a, b):
    m = len(a); n = len(b)
    return float(np.dot(f[:m], a) + np.dot(f[m:m + n - 1], b[:n - 1]))

# ---------- layerings ----------
def cost(L, a, b):
    """sum_x t(x) x."""
    tot = 0.0
    for t, layer in enumerate(L):
        for kind, i in layer:
            if kind == 'a': tot += t * a[i - 1]
            elif kind == 'b': tot -= t * b[i - 1]
    return tot

def form_of_layering(L, m, n):
    """Canonical form of a layering: alpha_j = t(a_j) - t(b_n), beta_i = t(b_n) - t(b_i)."""
    t = {}
    for u, layer in enumerate(L):
        for x in layer: t[x] = u
    tn = t[('b', n)]
    alpha = [t[('a', j)] - tn for j in range(1, m + 1)]
    beta = [tn - t[('b', i)] for i in range(1, n)]
    return tuple(alpha + beta)

def ordered_layering(u, m, n, split_last=True):
    """Ordered full-capacity layering for the b-schedule u (tuple of n nonneg ints).
    Returns the list of layers or None if degenerate (some b placed after all a's are exhausted -> dominated, skip)."""
    T = max(u)
    layers = [[] for _ in range(T + 1)]
    for i, ui in enumerate(u): layers[ui].append(('b', i + 1))
    j = 1; t = 1
    while j <= m:
        if t >= len(layers): layers.append([])
        c = sum(1 for ui in u if ui < t)
        if c == 0:
            if t > T: return None      # capacity 0 forever: cannot place
            t += 1; continue
        for _ in range(c):
            if j > m: break
            layers[t].append(('a', j)); j += 1
        t += 1
    # b's placed after the a's are exhausted (in a layer with no a) are dominated; also require last layer to have an a
    if not any(k == 'a' for k, _ in layers[-1]): return None
    return layers

def all_schedules(m, n, umax=None, nondecreasing=False):
    if umax is None: umax = m
    rng_u = range(0, umax + 1)
    for u in itertools.product(rng_u, repeat=n):
        if min(u) != 0: continue
        if nondecreasing and any(u[i] > u[i + 1] for i in range(n - 1)): continue
        yield u

def ordered_forms(m, n, nondecreasing=False, umax=None):
    """dict form -> (schedule, layering) over all ordered full-capacity layerings (deduplicated by form)."""
    out = {}
    for u in all_schedules(m, n, umax, nondecreasing):
        L = ordered_layering(u, m, n)
        if L is None: continue
        f = form_of_layering(L, m, n)
        out.setdefault(f, (u, L))
    return out

def max_ordered(forms, a, b):
    m = len(a); n = len(b)
    best = -np.inf; arg = None
    for f in forms:
        v = form_val(np.array(f, float), a, b)
        if v > best: best, arg = v, f
    return best, arg

def level_layering(f, m, n):
    """Level layering of a form f = (alpha; beta_1..beta_{n-1}) (integer entries): layers = level sets of
    t(a_j) = alpha_j - min, t(b_i) = -beta_i - min (beta_n = 0). Returns list of layers (tokens), layer 0 first."""
    ta = [int(round(x)) for x in f[:m]]; tb = [-int(round(x)) for x in f[m:m + n - 1]] + [0]
    lo = min(ta + tb); ta = [x - lo for x in ta]; tb = [x - lo for x in tb]
    T = max(ta + tb); L = [[] for _ in range(T + 1)]
    for i in range(n): L[tb[i]].append(('b', i + 1))
    for j in range(m): L[ta[j]].append(('a', j + 1))
    return L

def classify_layering(L, m, n):
    """Returns dict: ordered (a's in nondecreasing layer order), full (non-final layers hold exactly c_u a's),
    sched (b-schedule), binv (# b-inversions), maxsize, last_has_b, sizes."""
    t = {}
    for u, layer in enumerate(L):
        for x in layer: t[x] = u
    sched = tuple(t[('b', i)] for i in range(1, n + 1))
    ta = [t[('a', j)] for j in range(1, m + 1)]
    ordered = all(ta[j] <= ta[j + 1] for j in range(m - 1))
    T = len(L) - 1
    full = True
    for u in range(1, T):
        c = sum(1 for s in sched if s < u)
        na = sum(1 for k, _ in L[u] if k == 'a')
        if na != c: full = False
    binv = sum(1 for i in range(n) for j in range(i + 1, n) if sched[i] > sched[j])
    sizes = [len(layer) for layer in L]
    return dict(ordered=ordered, full=full, sched=sched, binv=binv, maxsize=max(sizes), sizes=sizes,
                last_has_b=any(k == 'b' for k, _ in L[-1]), layer0_pure_b=all(k == 'b' for k, _ in L[0]))

def show(L):
    return " ".join("{" + ",".join(f"{k}{i}" for k, i in layer) + "}" for layer in L)

def rat(x, den=720):
    return Q(x).limit_denominator(den)
