"""Exact Z(d,m) by the flats method (own implementation, python-flint):
for each support S (orbit rep, |S|=m) and each set R of <= m-1 characters, N_R = null space over Q(omega_d)
(computed over Q via the regular representation); if every coordinate block is nonzero somewhere on N_R, the
closure {chi : row_chi annihilates N_R} is a zero set attained by a full-support vector. Max over (S,R) = Z(d,m)."""
import sys, itertools
from math import gcd
import flint
from exact_zeros import ExactRank, orbits

def Z_exact(d, m):
    ER = ExactRank(d); D = ER.deg
    units = [u for u in range(1, d) if gcd(u, d) == 1]
    aff = lambda S: [tuple(sorted(((u*s + t) % d) for s in S)) for u in units for t in range(d)]
    S_reps = orbits((tuple((0,) + r) for r in itertools.combinations(range(1, d), m-1)), aff)
    def block_row(ch, S):
        rows = []
        for a in range(D):
            row = []
            for s in S: row.extend(ER.R[(ch*s) % d][a])
            rows.append(row)
        return rows
    best = 0; bestS = None; bestT = None
    for S in S_reps:
        blocks = {ch: block_row(ch, S) for ch in range(d)}
        Aall = flint.fmpz_mat(d*D, m*D, [x for ch in range(d) for r in blocks[ch] for x in r])
        for j in range(0, m):
            for R in itertools.combinations(range(d), j):
                if j == 0:
                    basis = [[1 if i == t else 0 for i in range(m*D)] for t in range(m*D)]
                else:
                    rows = [r for ch in R for r in blocks[ch]]
                    M = flint.fmpz_mat(len(rows), m*D, [x for r in rows for x in r])
                    X, nul = M.nullspace()
                    if nul == 0: continue
                    basis = [[int(X[i, c]) for i in range(m*D)] for c in range(nul)]
                # full support: each coordinate block nonzero on some basis vector
                if any(all(v[s*D + u] == 0 for v in basis for u in range(D)) for s in range(m)): continue
                Xm = flint.fmpz_mat(m*D, len(basis), [basis[c][i] for i in range(m*D) for c in range(len(basis))])
                P = Aall * Xm
                T = [ch for ch in range(d) if all(P[ch*D + u, c] == 0 for u in range(D) for c in range(len(basis)))]
                if len(T) > best: best, bestS, bestT = len(T), S, tuple(T)
    return best, bestS, bestT

if __name__ == "__main__":
    d, m = int(sys.argv[1]), int(sys.argv[2])
    print(f"d={d} m={m}: Z(d,m) = {Z_exact(d, m)}")
