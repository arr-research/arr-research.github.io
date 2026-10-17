# SPDX-License-Identifier: Apache-2.0
"""Pure helpers for independent sets, bounded occupations, and leading kernels."""
import math

def all_independent(G):
    n = len(G)
    edges = list(G.edges())
    best = []
    alpha = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size < alpha:
            continue
        if any((mask >> u & 1 and mask >> v & 1 for u, v in edges)):
            continue
        if size > alpha:
            best = []
            alpha = size
        best.append(tuple((i for i in range(n) if mask >> i & 1)))
    return (alpha, best)

def bounded_compositions(n, s, total):
    if n == 0:
        if total == 0:
            yield ()
        return
    for a in range(max(0, total - s * (n - 1)), min(s, total) + 1):
        for rest in bounded_compositions(n - 1, s, total - a):
            yield ((a,) + rest)

def kernel(G, s, patterns):
    n = len(G)
    q = max(dict(G.degree()).values()) * s + s + 1
    M = [[0] * q for _ in range(q)]
    for a in patterns:
        b = [s - x for x in a]
        rs = [a[i] + sum((a[j] for j in G[i])) for i in range(n)]
        nu = [0] * q
        C = {}
        for i in range(n):
            r = rs[i]
            nu[r] += b[i]
            C[r, r] = C.get((r, r), 0) + b[i] * (b[i] - 1)
        for i, j in G.edges():
            r, t = (rs[i], rs[j])
            C[r, t] = C.get((r, t), 0) + b[i] * b[j]
            C[t, r] = C.get((t, r), 0) + b[i] * b[j]
        w = math.prod((math.comb(s, x) for x in a))
        for i in range(q):
            for j in range(q):
                M[i][j] += w * (nu[i] * nu[j] - (nu[i] if i == j else 0))
        for (i, j), c in C.items():
            if c:
                M[i][j] -= w * c
                M[i + 1][j] += w * c
                M[i][j + 1] += w * c
                M[i + 1][j + 1] -= w * c
    return M
