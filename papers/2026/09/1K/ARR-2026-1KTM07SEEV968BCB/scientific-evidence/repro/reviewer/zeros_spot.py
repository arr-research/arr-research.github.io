"""Exact spot checks of the composite tables Z(d,m) (cyclic, exponents mod d) and of the (Z/4)^2 plane values.
Z(d,m) = max #{zeta in mu_d : f(zeta)=0} over f with EXACTLY m nonzero coefficients.
For each claimed value v: (i) refute v+1 zeros for every (S,T) with |S|=m, |T|=v+1 (orbit-reduced),
(ii) confirm attainment at |T| = v.  Exact over Q(omega_d).
"""
import sys, itertools, time
from math import gcd
from exact_zeros import ExactRank, orbits

def cyclic_check(d, m, v):
    ER = ExactRank(d)
    units = [u for u in range(1, d) if gcd(u, d) == 1]
    def aff_images(S):
        return [tuple(sorted(((u*s + t) % d) for s in S)) for u in units for t in range(d)]
    S_reps = orbits((tuple((0,) + r) for r in itertools.combinations(range(1, d), m-1)), aff_images)
    def check_size(tsize):
        T_reps = orbits((T for T in itertools.combinations(range(d), tsize)), aff_images)
        found = None; n = 0
        for S in S_reps:
            for T in T_reps:
                E = [[(t*s) % d for s in S] for t in T]
                n += 1
                if ER.full_support_solution_exists(E):
                    found = (S, T)
                    return found, n
        return found, n
    t0 = time.time()
    f1, n1 = check_size(v+1)
    f0, n0 = check_size(v)
    print(f"cyclic d={d} m={m}: claimed Z={v}. |T|={v+1}: witness={f1} ({n1} pairs checked); |T|={v}: witness={f0} ({n0} pairs). "
          f"=> {'CONFIRMED Z(d,m) = %d' % v if f1 is None and f0 is not None else 'PROBLEM'}  [{time.time()-t0:.1f}s]")

def plane4_check(m, v):
    d = 4
    ER = ExactRank(4)
    pts = [(x, y) for x in range(4) for y in range(4)]
    # GL_2(Z/4)
    GL = [((a, b), (c, e)) for a in range(4) for b in range(4) for c in range(4) for e in range(4) if (a*e - b*c) % 2 == 1]
    def aff_images(S):
        out = []
        for ((a, b), (c, e)) in GL:
            for (tx, ty) in pts:
                out.append(tuple(sorted((((a*x + b*y + tx) % 4, (c*x + e*y + ty) % 4) for (x, y) in S))))
        return out
    def transl_images(T):
        return [tuple(sorted((((x + tx) % 4, (y + ty) % 4) for (x, y) in T))) for (tx, ty) in pts]
    S_reps = orbits((tuple(((0, 0),) + r) for r in itertools.combinations(pts[1:], m-1)), aff_images)
    def check_size(tsize):
        T_reps = orbits((T for T in itertools.combinations(pts, tsize)), transl_images)
        n = 0
        for S in S_reps:
            for T in T_reps:
                E = [[(w[0]*s[0] + w[1]*s[1]) % 4 for s in S] for w in T]
                n += 1
                if ER.full_support_solution_exists(E):
                    return (S, T), n
        return None, n
    t0 = time.time()
    f1, n1 = check_size(v+1)
    f0, n0 = check_size(v)
    print(f"plane (Z/4)^2 m={m}: claimed Z={v}. |T|={v+1}: witness={f1} ({n1} pairs); |T|={v}: witness={f0} ({n0} pairs). "
          f"=> {'CONFIRMED Z = %d' % v if f1 is None and f0 is not None else 'PROBLEM'}  [{time.time()-t0:.1f}s]")

if __name__ == "__main__":
    which = sys.argv[1]
    if which == "cyclic":
        for (d, m, v) in [(6,3,4),(10,3,4),(10,4,6),(10,5,8),(12,4,9),(14,4,8),(14,3,4)]:
            cyclic_check(d, m, v)
    else:
        for (m, v) in [(2,8),(3,8),(4,12),(5,8),(6,12)]:
            plane4_check(m, v)
