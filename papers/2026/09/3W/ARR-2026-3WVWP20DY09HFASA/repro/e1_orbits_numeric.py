"""E1: exhaustive numerical search per AGL(2,p)-orbit of supports.
For each orbit of l-subsets S of F_p^2 under AGL(2,p) = GL_2(F_p) x translations (the symmetry group of
the rank problem: SL_2 x translations via Clifford conjugation and W_h multiplication, det -1 via transpose,
general det via Galois), and each target nullity k = 1..l, minimise
     phi_k(c) = sum_{i > p-k} sigma_i(C(c))^2   on   ||c|| = 1
by alternating minimisation (c -> k smallest right singular vectors V of C(c); V -> smallest right singular
vector of the linear map c -> C(c)V) with many random restarts, then report the best observed singular-value residual among finite restart endpoints (not a certified global minimum).
A value ~ 0 means nullity >= k is (numerically) attainable on that support.
Usage: python e1_orbits_numeric.py p l [restarts]
"""
import sys, itertools, time
import numpy as np

def orbits(p, l):
    """Orbit representatives of l-subsets of F_p^2 under AGL(2,p), via canonical forms.
    Every l-set (l>=2) can be moved so that it contains 0 and e1=(1,0); canonical form = lexicographically
    smallest image under (choice of ordered pair mapped to (0,e1)) x Stab(0,e1) = {[[1,x],[0,y]]: y != 0}."""
    pts = [(a, b) for a in range(p) for b in range(p)]
    def enc(S): return tuple(sorted(a*p+b for a, b in S))
    stab = [(x, y) for x in range(p) for y in range(1, p)]   # M = [[1,x],[0,y]] acting (a,b) -> (a + x b, y b)
    def canon(S):
        best = None
        for P, Q in itertools.permutations(S, 2):
            # affine map sending P->0, Q->e1: first translate by -P, then a GL2 map sending v=Q-P to e1
            v = ((Q[0]-P[0]) % p, (Q[1]-P[1]) % p)
            # choose A with A v = e1: if v0 != 0: A = [[inv v0, 0],[-v1 inv v0, 1]] ; else v1 != 0: A = [[0, inv v1],[1, 0]]
            if v[0]:
                i0 = pow(v[0], -1, p); A = ((i0, 0), ((-v[1]*i0) % p, 1))
            else:
                i1 = pow(v[1], -1, p); A = ((0, i1), (1, 0))
            T = []
            for (a, b) in S:
                a1, b1 = (a-P[0]) % p, (b-P[1]) % p
                T.append(((A[0][0]*a1 + A[0][1]*b1) % p, (A[1][0]*a1 + A[1][1]*b1) % p))
            for x, y in stab:
                img = enc(((a + x*b) % p, (y*b) % p) for a, b in T)
                if best is None or img < best: best = img
        return best
    reps = {}
    others = [q for q in pts if q not in ((0, 0), (1, 0))]
    for rest in itertools.combinations(others, l-2):
        S = [(0, 0), (1, 0)] + list(rest)
        c = canon(S)
        if c not in reps: reps[c] = S
    # orbit sizes by brute-force stabiliser count (group order p^2 (p^2-1)(p^2-p))
    G = p*p*(p*p-1)*(p*p-p)
    out = []
    for c, S in reps.items():
        Sset = set(enc(S))
        stabsize = 0
        s0 = S[0]
        for m in itertools.product(range(p), repeat=4):
            if (m[0]*m[3]-m[1]*m[2]) % p == 0: continue
            ms0 = ((m[0]*s0[0]+m[1]*s0[1]) % p, (m[2]*s0[0]+m[3]*s0[1]) % p)
            for s1 in S:   # translation must send m(s0) to some point of S
                t = ((s1[0]-ms0[0]) % p, (s1[1]-ms0[1]) % p)
                img = enc(((m[0]*a+m[1]*b+t[0]) % p, (m[2]*a+m[3]*b+t[1]) % p) for a, b in S)
                if set(img) == Sset: stabsize += 1
        out.append((S, G//stabsize))
    return out

def describe(S, p):
    """configuration invariants: max number of collinear points, number of directions with all points separated."""
    mx = 1
    for u, v in itertools.combinations(S, 2):
        d = ((v[0]-u[0]) % p, (v[1]-u[1]) % p)
        cnt = 0
        for w in S:
            e = ((w[0]-u[0]) % p, (w[1]-u[1]) % p)
            if (d[0]*e[1]-d[1]*e[0]) % p == 0: cnt += 1
        mx = max(mx, cnt)
    return mx

def weyl_np(p, a, b):
    X = np.roll(np.eye(p), 1, axis=0); Z = np.diag(np.exp(2j*np.pi*np.arange(p)/p))
    return np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b)

def min_sigma(Ws, p, k, restarts, rng, iters=300):
    l = len(Ws)
    Wstack = np.stack(Ws)                      # (l, p, p)
    best = np.inf; bestc = None
    for _ in range(restarts):
        c = rng.normal(size=l) + 1j*rng.normal(size=l); c /= np.linalg.norm(c)
        prev = np.inf
        for it in range(iters):
            C = np.tensordot(c, Wstack, axes=(0, 0))
            U, s, Vh = np.linalg.svd(C)
            V = Vh[p-k:].conj().T             # p x k, k smallest right singular vectors
            M = np.stack([(W @ V).ravel() for W in Ws], axis=1)   # (p k) x l
            _, sm, Vm = np.linalg.svd(M, full_matrices=False)
            c = Vm[-1].conj(); c /= np.linalg.norm(c)
            val = sm[-1]
            if abs(prev - val) < 1e-14: break
            prev = val
        C = np.tensordot(c, Wstack, axes=(0, 0))
        s = np.linalg.svd(C, compute_uv=False)
        val = s[p-k]                            # sigma_{p-k+1}, ||c|| = 1
        if val < best: best, bestc = val, c.copy()
    return best, bestc

def main():
    p = int(sys.argv[1]); l = int(sys.argv[2]); restarts = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    rng = np.random.default_rng(12345)
    t0 = time.time()
    reps = orbits(p, l)
    tot = sum(sz for _, sz in reps)
    from math import comb
    print(f"p={p} l={l}: {len(reps)} AGL(2,p)-orbits of supports; sum of orbit sizes {tot} vs C(p^2,l)={comb(p*p,l)} [{time.time()-t0:.1f}s]", flush=True)
    assert tot == comb(p*p, l)
    print(f"target law: nullity <= l-1 = {l-1}, i.e. sigma_{p-l+1} bounded away from 0; trivial bound: nullity <= p - ceil(p/l) = {p - (-(-p//l))}")
    summary = []
    for S, sz in reps:
        Ws = [weyl_np(p, a, b) for a, b in S]
        mx = describe(S, p)
        vals = []
        for k in range(1, l+1):
            v, c = min_sigma(Ws, p, k, restarts, rng)
            vals.append(v)
        attained = max([k for k in range(1, l+1) if vals[k-1] < 1e-9], default=0)
        line = f"S={S} orbit={sz} maxcollinear={mx} | min sigma_(p-k+1) for k=1..{l}: " + " ".join(f"{v:.2e}" for v in vals) + f" | max numerically detected nullity = {attained}"
        print(line, flush=True)
        summary.append((S, sz, mx, vals, attained))
    worst = min(v[3][l-1] for v in summary)
    print(f"RESULT p={p} l={l}: max numerically detected nullity over tested representatives = {max(v[4] for v in summary)} (law requires <= {l-1}); "
          f"best observed sigma_(p-l+1) residual over tested representatives = {worst:.3e}; representatives detecting l-1: {[v[0] for v in summary if v[4] == l-1]}  [{time.time()-t0:.1f}s]")

if __name__ == '__main__':
    main()
