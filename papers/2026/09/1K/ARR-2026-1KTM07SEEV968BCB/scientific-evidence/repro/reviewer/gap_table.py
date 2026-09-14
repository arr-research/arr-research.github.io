"""(1) Recompute the Conjecture-C gap table: for d = p^k, sparsities l with Omega_k(l) < d - ceil(d/l) and l > 2p-1.
(2) Check closed formulas for Omega_k.  (3) Sanity of 0WE Theorem 2 sector formula vs numerical nullity for random
trinomials in composite d, and the T3 attainment examples; (4) T2 numerical check d<=15."""
import numpy as np, random
from math import ceil, gcd

def digit_weight(r, p):
    w = 1
    while r: w *= (r % p) + 1; r //= p
    return w
def omega_k(p, k, m): return max(r for r in range(p**k) if digit_weight(r, p) <= m)

print("== gap table ==")
for (p, k) in [(2,2),(2,3),(3,2),(2,4),(3,3),(5,2),(2,5),(7,2)]:
    d = p**k
    gaps = [l for l in range(2*p, d+1) if omega_k(p, k, l) < d - ceil(d/l)]
    # closed formulas
    for m in range(1, d+1):
        if m <= p: assert omega_k(p,k,m) == (m-1)*p**(k-1)
        elif m < p*p and k >= 2: assert omega_k(p,k,m) == (p-1)*p**(k-1) + (m//p - 1)*p**(k-2), (p,k,m)
    a = 1
    while p**a <= d:
        assert omega_k(p,k,p**a) == d - p**(k-a); a += 1
    print(f"d={d}: open l = {gaps}")

def weyl(d, a, b):
    om = np.exp(2j*np.pi/d)
    W = np.zeros((d, d), dtype=complex)
    for j in range(d): W[(j+a) % d, j] = om**(b*j % d)
    return W

def nullity(M):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-9*max(s[0], 1)))

def order(g, d): return d // gcd(gcd(g[0], g[1]), d)

print("== T2: binomial nullities, all label pairs, d<=15 ==")
for d in range(2, 16):
    pmin = min(q for q in range(2, d+1) if d % q == 0)
    best = 0
    for a in range(d):
        for b in range(d):
            if (a, b) == (0, 0): continue
            W = weyl(d, a, b)
            ev = np.linalg.eigvals(W)
            # nullity of I + c W maximal = max eigenvalue multiplicity
            vals, counts = np.unique(np.round(ev, 6), return_counts=True)
            best = max(best, counts.max())
    print(f"  d={d}: max binomial nullity = {best}, d/p_min = {d//pmin}")

print("== T3: 0WE Theorem 2 formula vs numerical nullity (random trinomials) ==")
rng = random.Random(7)
def sector_nullity(d, u, v, a, b, c):
    om = np.exp(2j*np.pi/d)
    U, V = weyl(d, *u), weyl(d, *v)
    # commutator U V = zeta V U
    zeta = (U @ V)[np.nonzero(V @ U)][0] / (V @ U)[np.nonzero(V @ U)][0]
    q = 1
    while abs(zeta**q - 1) > 1e-9: q += 1
    # joint eigenvalues of U^q, V^q (both central on H): enumerate joint spectrum via simultaneous diag
    Uq, Vq = np.linalg.matrix_power(U, q), np.linalg.matrix_power(V, q)
    # they commute; diagonalize Uq + rand*Vq
    M = Uq + 0.37*Vq + 0.11j*np.linalg.matrix_power(Uq, 2)
    ev, P = np.linalg.eig(M)
    Pi = np.linalg.inv(P)
    s = np.diag(Pi @ Uq @ P); t = np.diag(Pi @ Vq @ P)
    pairs = {}
    for x, y in zip(s, t):
        key = (round(x.real, 6), round(x.imag, 6), round(y.real, 6), round(y.imag, 6))
        pairs[key] = pairs.get(key, 0) + 1
    h = len(pairs)
    m = d // (q*h)
    nsing = sum(1 for (sr, si, tr, ti) in pairs if abs(a**q*(sr+1j*si) + b**q*(tr+1j*ti) - (-1)**q*c**q) < 1e-7)
    return m*nsing, q, h, m
nbad = 0
for trial in range(60):
    d = rng.choice([6, 8, 9, 10, 12, 14, 15])
    labels = [(x, y) for x in range(d) for y in range(d) if (x, y) != (0, 0)]
    u = rng.choice(labels); v = rng.choice(labels)
    if v == u: continue
    a, b = rng.choice([1, 1j, -1, 2, 0.5+0.5j]), rng.choice([1, 1j, -1, 2, 0.3j])
    # choose c to make a sector singular sometimes
    pred, q, h, m = sector_nullity(d, u, v, a, b, 1.0)
    D = np.eye(d) + a*weyl(d, *u) + b*weyl(d, *v)
    num = nullity(D)
    if num != pred: nbad += 1; print("  mismatch", d, u, v, a, b, num, pred)
print(f"  random trinomials: formula mismatches = {nbad} (of 60 trials, c = 1)")
# T3 attainment examples
for d in (6, 10, 12, 14, 15):
    r3 = min(q for q in range(3, d+1) if d % q == 0)
    om = np.exp(2j*np.pi/d)
    g = (0, d//r3); T = weyl(d, *g)
    xi = np.exp(2j*np.pi/r3)
    D = (T - np.eye(d)) @ (T - xi*np.eye(d))
    n1 = nullity(D)
    line = f"  d={d}: collinear (T-I)(T-xi I), T order {r3}: nullity {n1} (2d/r3 = {2*d//r3})"
    if d % 4 == 2:
        U, V = weyl(d, 0, d//2), weyl(d, d//2, 0)
        D2 = np.sqrt(2)*np.eye(d) + U + V
        line += f"; anticommuting sqrt2 I + Z^{d//2} + X^{d//2}: nullity {nullity(D2)} (d/2 = {d//2})"
    print(line)
