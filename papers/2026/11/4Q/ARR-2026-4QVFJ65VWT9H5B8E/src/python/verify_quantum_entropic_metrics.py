"""Exact rational verification suite for Quantum Entropic Metric Geometry.

Independently constructs and certifies in exact integer / Fraction arithmetic:
1. The CB_4^+ triangle-inequality violation under pairwise S(i|j) >= 0.
2. Theorem 1 (n <= 6 phase hierarchy):
   - MET_3, MET_4, MET_5 exact extreme rays via cdd.gmp + K_{2,3} over F_2^2.
   - MET_6 exact 296 extreme rays in 8 S_6-orbits; Orbits 1-7 in SUB_6;
     all 296 rays in CB_6^+ (proving M_6^{cb,+} = M_6^{q,+} = MET_6).
   - 10-orbit D_4-symmetrized Shannon Farkas proof of I_{K_{3,3}-e}(d) >= 0
     and exact kappa_{POLY_6}(K_{3,3}-e) = 9/8.
   - Exact Fukuda-Prodon DD of MET_6 cap {90 conjugates} (1736 rays, 12 orbits,
     exact rank-14 tightness on every ray) and exact polymatroids for all 12 orbits.
   - Orbit 9 Zhang-Yeung non-Shannon separation (kappa_{POLY+ZY} = 31/30) and CB_6^+ realization.
   - Exhaustive classification of all 112 connected 6-vertex graphs.
3. Theorem 2 (Segre quadric & n = 7 separation):
   - Segre quadric Q^+(3, F_q) realization of K_{q+1, q+1} for q = 2, 3, 5, 7.
   - Exhaustive exact rational classification of all 853 connected 7-vertex graphs
     against POLY_7, CB_7, and Q_7 (38 fail POLY_7, 128 fail CB_7, 16 fail both, 2 fail Q_7).
   - Exact Rem #4 (G800) certification: kappa_{POLY_7} = 17/16, F_4 = -1 (min >= 0 over
     126 cuts & 21 Bell pairs), kappa_{CB_7} = kappa_{CB_7^+} = 13/12, and exact isometric
     binary-qubit realization in M_7^{q,+} with min_{i != j} S(i|j) >= 0.
4. Theorem 3 (QFail1, QFail2, & K_{m,m}-M Parity Staircase):
   - Exact SSA+WM Farkas certificates for QFail1 (G708, kappa_{Q_7} = 21/20) and
     QFail2 (G873, kappa_{Q_7} = 41/40).
   - Exact Z_2 x S_m-symmetrized rational certification of kappa_{POLY_{2m}} and
     kappa_{Q_{2m}} for m = 3..18, plus kappa_{CUT_{2m}} for m = 3..12, and exact
     m = 5 (11, -8, -3) SSA+WM identity (12/11 < 9/8 < 4/3).

Floating-point LP (scipy.optimize.linprog) is used solely to discover candidate
supports; every primal and dual claim is verified strictly in exact int / Fraction.
"""

from __future__ import annotations

import itertools
import json
import math
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import cdd.gmp as cdd
import networkx as nx
import numpy as np
from scipy.linalg import qr
from scipy.optimize import linprog
from sympy import QQ
from sympy.polys.matrices import DomainMatrix


def pairs(n: int) -> list[tuple[int, int]]:
    """Return lexicographically ordered pairs (i, j) with 0 <= i < j < n."""
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def normalize_int_ray(vec: list[Any] | tuple[Any, ...]) -> tuple[int, ...]:
    """Scale rational vector to a primitive integer vector with positive gcd."""
    fracs = [Fraction(x) for x in vec]
    lcm_den = 1
    for f in fracs:
        lcm_den = math.lcm(lcm_den, f.denominator)
    ints = [int(f * lcm_den) for f in fracs]
    g = 0
    for v in ints:
        g = math.gcd(g, abs(v))
    if g > 0:
        ints = [v // g for v in ints]
    return tuple(ints)


def canonical_orbit_rep(
    ray: tuple[int, ...],
    n: int,
    plist: list[tuple[int, int]],
    pidx: dict[tuple[int, int], int],
) -> tuple[int, ...]:
    """Return lexicographically minimal S_n conjugate of ray."""
    best = None
    for perm in itertools.permutations(range(n)):
        permuted = tuple(
            ray[pidx[(min(perm[i], perm[j]), max(perm[i], perm[j]))]]
            for i, j in plist
        )
        if best is None or permuted < best:
            best = permuted
    assert best is not None
    return best


def _to_qq(x: int | Fraction) -> Any:
    if isinstance(x, int):
        return QQ(x)
    return QQ(x.numerator, x.denominator)


def dm_rref_solve(A_rows: list[list[int | Fraction]], b_vec: list[int | Fraction]) -> list[Fraction]:
    """Solve consistent rational linear system A x = b exactly via sparse SymPy DomainMatrix(QQ)."""
    m = len(A_rows)
    n = len(A_rows[0])
    sparse: dict[int, dict[int, Any]] = {}
    for i in range(m):
        row_d: dict[int, Any] = {}
        row = A_rows[i]
        for j in range(n):
            v = row[j]
            if v != 0:
                row_d[j] = _to_qq(v)
        bv = b_vec[i]
        if bv != 0:
            row_d[n] = _to_qq(bv)
        if row_d:
            sparse[i] = row_d
    R, pivs = DomainMatrix(sparse, (m, n + 1), QQ).rref()
    R_dok = R.to_dok()
    for r in range(len(pivs), m):
        if (r, n) in R_dok and R_dok[(r, n)] != 0:
            raise ValueError("Inconsistent rational linear system")
    x = [Fraction(0)] * n
    for r, c in enumerate(pivs):
        if c == n:
            raise ValueError("Inconsistent rational system (pivot in RHS)")
        val = R_dok.get((r, n))
        if val is not None:
            x[c] = Fraction(int(val.numerator), int(val.denominator))
    return x


def dm_rank(A_rows: list[list[int]]) -> int:
    """Compute exact rational rank of an integer matrix via sparse DomainMatrix(QQ)."""
    if not A_rows:
        return 0
    m = len(A_rows)
    n = len(A_rows[0])
    sparse = {
        i: {j: QQ(v) for j, v in enumerate(row) if v != 0}
        for i, row in enumerate(A_rows)
        if any(row)
    }
    _, pivs = DomainMatrix(sparse, (m, n), QQ).rref()
    return len(pivs)


def metric_inequalities(n: int, include_nonneg: bool = False) -> tuple[list[list[int]], list[tuple[int, int]], dict[tuple[int, int], int]]:
    """Return H-matrix rows [0, a_0, ...] for MET_n."""
    plist = pairs(n)
    pidx = {p: idx for idx, p in enumerate(plist)}
    dim = len(plist)
    rows: list[list[int]] = []
    if include_nonneg:
        for idx in range(dim):
            row = [0] * (dim + 1)
            row[idx + 1] = 1
            rows.append(row)
    for i, j, k in itertools.combinations(range(n), 3):
        ij = pidx[(i, j)]
        ik = pidx[(i, k)]
        jk = pidx[(j, k)]
        for a, b, c in [(ik, jk, ij), (ij, jk, ik), (ij, ik, jk)]:
            row = [0] * (dim + 1)
            row[a + 1] = 1
            row[b + 1] = 1
            row[c + 1] = -1
            rows.append(row)
    return rows, plist, pidx


def dq_projection_matrix(n: int, plist: list[tuple[int, int]]) -> list[list[int]]:
    """Matrix D mapping S(X) (masks 1..2^n-1) to d_Q(i,j) = 2 S(ij) - S(i) - S(j)."""
    dim = (1 << n) - 1
    D = [[0] * dim for _ in range(len(plist))]
    for r, (i, j) in enumerate(plist):
        D[r][((1 << i) | (1 << j)) - 1] += 2
        D[r][(1 << i) - 1] -= 1
        D[r][(1 << j) - 1] -= 1
    return D


def cond_entropy_matrix(n: int) -> tuple[list[list[int]], list[tuple[int, int]]]:
    """Rows for S(i|j) = S(ij) - S(j) for all ordered pairs i != j."""
    dim = (1 << n) - 1
    rows: list[list[int]] = []
    labels: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            row = [0] * dim
            row[((1 << i) | (1 << j)) - 1] += 1
            row[(1 << j) - 1] -= 1
            rows.append(row)
            labels.append((i, j))
    return rows, labels


def poly_ineqs(n: int) -> list[tuple[str, tuple[int, ...], list[int]]]:
    """Elemental Shannon inequalities (monotonicity + submodularity) for Gamma_n."""
    dim = (1 << n) - 1
    ineqs: list[tuple[str, tuple[int, ...], list[int]]] = []
    full = (1 << n) - 1
    for i in range(n):
        row = [0] * dim
        row[full - 1] = 1
        row[(full ^ (1 << i)) - 1] = -1
        ineqs.append(("MONO", (i,), row))
    for i in range(n):
        for j in range(i + 1, n):
            rest = [k for k in range(n) if k != i and k != j]
            for rmask in range(1 << len(rest)):
                K = 0
                for idx, bit in enumerate(rest):
                    if (rmask >> idx) & 1:
                        K |= 1 << bit
                row = [0] * dim
                row[(K | (1 << i)) - 1] += 1
                row[(K | (1 << j)) - 1] += 1
                row[(K | (1 << i) | (1 << j)) - 1] -= 1
                if K > 0:
                    row[K - 1] -= 1
                ineqs.append(("SUBMOD", (i, j, K), row))
    return ineqs


def qcone_ineqs(n: int) -> list[tuple[str, tuple[int, ...], list[int]]]:
    """Elemental SSA + Weak Monotonicity inequalities defining Pippenger's QCONE_n."""
    dim = (1 << n) - 1
    ineqs: list[tuple[str, tuple[int, ...], list[int]]] = []
    for i in range(n):
        for j in range(i + 1, n):
            rest = [k for k in range(n) if k != i and k != j]
            for rmask in range(1 << len(rest)):
                K = 0
                for idx, bit in enumerate(rest):
                    if (rmask >> idx) & 1:
                        K |= 1 << bit
                row = [0] * dim
                row[(K | (1 << i)) - 1] += 1
                row[(K | (1 << j)) - 1] += 1
                row[(K | (1 << i) | (1 << j)) - 1] -= 1
                if K > 0:
                    row[K - 1] -= 1
                ineqs.append(("SSA", (i, j, K), row))
    full = (1 << n) - 1
    for i in range(n):
        others = full ^ (1 << i)
        rest = [k for k in range(n) if k != i]
        for rmask in range(1 << len(rest)):
            K = 0
            for idx, bit in enumerate(rest):
                if (rmask >> idx) & 1:
                    K |= 1 << bit
            L = others ^ K
            if K > L:
                continue
            row = [0] * dim
            row[(K | (1 << i)) - 1] += 1
            row[(L | (1 << i)) - 1] += 1
            if K > 0:
                row[K - 1] -= 1
            if L > 0:
                row[L - 1] -= 1
            ineqs.append(("WM", (i, K, L), row))
    return ineqs


def zy98_ineqs(n: int = 6) -> list[tuple[str, tuple[int, int, int, int], list[int]]]:
    """All distinct Zhang-Yeung (1998) non-Shannon inequalities on disjoint nonempty (A,B,C,D)."""
    seen: set[tuple[int, ...]] = set()
    out: list[tuple[str, tuple[int, int, int, int], list[int]]] = []
    dim = (1 << n) - 1
    for assign in itertools.product(range(5), repeat=n):
        masks = [0, 0, 0, 0]
        for idx, b in enumerate(assign):
            if b > 0:
                masks[b - 1] |= 1 << idx
        if not all(masks):
            continue
        A, B, C, D = masks
        row = [0] * dim
        for msk, coef in [
            (A, -1), (A | B, -1), (A | C, 3), (A | D, 3), (A | C | D, -4),
            (B | C, 1), (B | D, 1), (B | C | D, -1), (C, -2), (D, -2), (C | D, 3),
        ]:
            row[msk - 1] += coef
        t = tuple(row)
        if t not in seen:
            seen.add(t)
            out.append(("ZY98", (A, B, C, D), row))
    return out


def cb_entropy_generators(n: int) -> tuple[list[tuple[str, Any]], list[list[int]]]:
    """Return (labels, S_vecs) for all 2^n - 2 classical cuts and n(n-1)/2 Bell pairs."""
    labels: list[tuple[str, Any]] = []
    vecs: list[list[int]] = []
    full = (1 << n) - 1
    for S in range(1, full):
        vecs.append([1 if (X & S) != 0 else 0 for X in range(1, 1 << n)])
        labels.append(("cut", S))
    for i in range(n):
        for j in range(i + 1, n):
            mask = (1 << i) | (1 << j)
            vecs.append([1 if (X & mask).bit_count() == 1 else 0 for X in range(1, 1 << n)])
            labels.append(("bell", (i, j)))
    return labels, vecs


def exact_certify_cone_H(
    d_target: list[int],
    ineqs: list[tuple[str, Any, list[int]]],
    D_rows: list[list[int]],
    need_dual_if_fail: bool = True,
    _cache: dict[int, tuple[Any, ...]] = {},
) -> dict[str, Any]:
    """Certify min distortion kappa >= 1 of d_target in {D s : M s >= 0} using exact Fraction arithmetic."""
    key = (id(ineqs), id(D_rows))
    if key not in _cache:
        M_rows = [r for _, _, r in ineqs]
        tags = [(k, info) for k, info, _ in ineqs]
        M = np.array(M_rows, dtype=float)
        D = np.array(D_rows, dtype=float)
        M_sparse = [[(v, r[v]) for v in range(len(r)) if r[v] != 0] for r in M_rows]
        D_sparse = [[(v, r[v]) for v in range(len(r)) if r[v] != 0] for r in D_rows]
        n_vars = M.shape[1]
        n_ineq = M.shape[0]
        n_p = D.shape[0]
        A_base = np.vstack([
            np.hstack([-M, np.zeros((n_ineq, 1))]),
            np.hstack([-D, np.zeros((n_p, 1))]),
        ])
        _cache[key] = (M_rows, tags, M, D, M_sparse, D_sparse, n_vars, n_ineq, n_p, A_base)
    M_rows, tags, M, D, M_sparse, D_sparse, n_vars, n_ineq, n_p, A_base = _cache[key]

    d_arr = np.array(d_target, dtype=float)
    A_ub = np.vstack([
        A_base,
        np.hstack([D, -d_arr.reshape(-1, 1)]),
    ])
    b_ub = np.concatenate([np.zeros(n_ineq), -d_arr, np.zeros(n_p)])
    c = np.zeros(n_vars + 1)
    c[-1] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * n_vars + [(1.0, None)], method="highs")
    if not res.success:
        raise RuntimeError(f"LP failed: {res.message}")

    # 1. Recover exact dual certificate if kappa > 1
    kappa_exact: Fraction | None = None
    dual_cert = None
    if res.fun > 1.0 + 1e-7:
        marg = -res.ineqlin.marginals
        y_flt = marg[:n_ineq]
        a_flt = marg[n_ineq : n_ineq + n_p]
        b_flt = marg[n_ineq + n_p :]
        nz_y = [i for i in range(n_ineq) if y_flt[i] > 1e-8]
        nz_a = [r for r in range(n_p) if a_flt[r] > 1e-8]
        nz_b = [r for r in range(n_p) if b_flt[r] > 1e-8]
        eq_rows = [
            [M_rows[i][v] for i in nz_y] + [D_rows[r][v] for r in nz_a] + [-D_rows[r][v] for r in nz_b]
            for v in range(n_vars)
        ]
        eq_rhs = [0] * n_vars
        eq_rows.append([0] * len(nz_y) + [0] * len(nz_a) + [d_target[r] for r in nz_b])
        eq_rhs.append(1)
        sol = dm_rref_solve(eq_rows, eq_rhs)
        assert all(x >= 0 for x in sol), "Negative dual multiplier"
        y_ex = sol[: len(nz_y)]
        a_ex = sol[len(nz_y) : len(nz_y) + len(nz_a)]
        b_ex = sol[len(nz_y) + len(nz_a) :]
        kappa_exact = sum((a_ex[i] * d_target[nz_a[i]] for i in range(len(nz_a))), Fraction(0))
        # Exact Farkas identity check: M^T y == D^T (beta - alpha)
        for v in range(n_vars):
            lhs = sum((y_ex[i] * M_rows[nz_y[i]][v] for i in range(len(nz_y))), Fraction(0))
            rhs = sum((b_ex[i] * D_rows[nz_b[i]][v] for i in range(len(nz_b))), Fraction(0)) - sum(
                (a_ex[i] * D_rows[nz_a[i]][v] for i in range(len(nz_a))), Fraction(0)
            )
            assert lhs == rhs
        assert sum((b_ex[i] * d_target[nz_b[i]] for i in range(len(nz_b))), Fraction(0)) == 1
        assert kappa_exact > 1
        if need_dual_if_fail:
            dual_cert = {
                "y": [(tags[nz_y[i]], y_ex[i]) for i in range(len(nz_y)) if y_ex[i] > 0],
                "alpha": [(nz_a[i], a_ex[i]) for i in range(len(nz_a)) if a_ex[i] > 0],
                "beta": [(nz_b[i], b_ex[i]) for i in range(len(nz_b)) if b_ex[i] > 0],
            }
    else:
        kappa_exact = Fraction(1)

    # 2. Recover exact primal realization achieving kappa_exact!
    slacks = M @ res.x[:-1]
    active_ineq = [i for i in range(n_ineq) if abs(float(slacks[i])) < 1e-6]
    d_est = D @ res.x[:-1]
    P_cand: list[list[int]] = []
    P_rhs: list[int] = []
    for r in range(n_p):
        val = float(d_est[r])
        if abs(val - d_target[r]) < 1e-6:
            P_cand.append(D_rows[r] + [0])
            P_rhs.append(d_target[r])
        if abs(val - res.fun * d_target[r]) < 1e-6:
            P_cand.append(D_rows[r] + [-d_target[r]])
            P_rhs.append(0)
    P_cand.append([0] * n_vars + [kappa_exact.denominator])
    P_rhs.append(kappa_exact.numerator)
    for i in active_ineq:
        P_cand.append(M_rows[i] + [0])
        P_rhs.append(0)

    P_arr = np.array(P_cand, dtype=float)
    _, R_qr, perm = qr(P_arr.T, pivoting=True)
    diag = np.abs(np.diag(R_qr)) if R_qr.size else np.array([])
    rank = int(np.sum(diag > 1e-8))
    sel = perm[: min(len(P_cand), rank + 6)]
    primal_sol = dm_rref_solve([P_cand[i] for i in sel], [P_rhs[i] for i in sel])
    s_ex = primal_sol[:-1]
    k_primal = primal_sol[-1]
    assert k_primal == kappa_exact
    for sp_row in M_sparse:
        assert sum((coef * s_ex[v] for v, coef in sp_row), Fraction(0)) >= 0
    for r, sp_row in enumerate(D_sparse):
        dv = sum((coef * s_ex[v] for v, coef in sp_row), Fraction(0))
        assert d_target[r] <= dv <= kappa_exact * d_target[r]

    return {"kappa": kappa_exact, "primal_s": s_ex, "dual": dual_cert}


def exact_certify_CB(
    d_target: list[int],
    dq_cols: list[list[int]],
    cond_cols: list[list[int]] | None = None,
    labels: list[tuple[str, Any]] | None = None,
) -> dict[str, Any]:
    """Certify min distortion of d_target in CB_n (or CB_n^+ if cond_cols given) in exact Fraction."""
    m_gen = len(dq_cols)
    n_p = len(d_target)
    G = np.array(dq_cols, dtype=float).T  # n_p x m_gen
    d_arr = np.array(d_target, dtype=float)
    A_blocks = [
        np.hstack([-G, np.zeros((n_p, 1))]),
        np.hstack([G, -d_arr.reshape(-1, 1)]),
    ]
    b_blocks = [-d_arr, np.zeros(n_p)]
    n_cond = 0
    if cond_cols is not None:
        C = np.array(cond_cols, dtype=float).T  # n_cond x m_gen
        n_cond = C.shape[0]
        A_blocks.append(np.hstack([-C, np.zeros((n_cond, 1))]))
        b_blocks.append(np.zeros(n_cond))

    A_ub = np.vstack(A_blocks)
    b_ub = np.concatenate(b_blocks)
    c = np.zeros(m_gen + 1)
    c[-1] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0.0, None)] * m_gen + [(1.0, None)], method="highs")
    if not res.success:
        raise RuntimeError(f"CB LP failed: {res.message}")

    kappa_exact: Fraction
    dual_cert = None
    if res.fun > 1.0 + 1e-7:
        marg = -res.ineqlin.marginals
        a_flt = marg[:n_p]
        b_flt = marg[n_p : 2 * n_p]
        g_flt = marg[2 * n_p :]
        nz_a = [r for r in range(n_p) if a_flt[r] > 1e-8]
        nz_b = [r for r in range(n_p) if b_flt[r] > 1e-8]
        nz_g = [k for k in range(n_cond) if g_flt[k] > 1e-8]

        # Dual of min kappa s.t. G w >= d, -G w + kappa d >= 0, C w >= 0, w >= 0, kappa >= 1:
        # max alpha.d s.t. G^T(beta - alpha) - C^T gamma >= 0, beta.d = 1, alpha,beta,gamma >= 0.
        # Include ALL generators j whose dual slack is ~0 (not just w_j > 0, to handle primal degeneracy!).
        dual_tight = []
        for j in range(m_gen):
            slack_j = sum(b_flt[i] * dq_cols[j][i] for i in range(n_p)) - sum(a_flt[i] * dq_cols[j][i] for i in range(n_p))
            if cond_cols is not None:
                slack_j -= sum(g_flt[k] * cond_cols[j][k] for k in range(n_cond))
            if abs(slack_j) < 1e-6:
                dual_tight.append(j)
        eq_rows = []
        eq_rhs = []
        for j in dual_tight:
            row = [dq_cols[j][r] for r in nz_a] + [-dq_cols[j][r] for r in nz_b]
            if cond_cols is not None:
                row += [cond_cols[j][k] for k in nz_g]
            eq_rows.append(row)
            eq_rhs.append(0)
        eq_rows.append([0] * len(nz_a) + [d_target[r] for r in nz_b] + [0] * len(nz_g))
        eq_rhs.append(1)
        sol = dm_rref_solve(eq_rows, eq_rhs)
        if any(x < 0 for x in sol):
            # Fallback: use active basis of dual LP via cdd.gmp exact rational LP!
            # Wait: solve dual LP directly with scipy using tiny L1 regularization or cdd.gmp!
            n_dvars = len(nz_a) + len(nz_b) + len(nz_g)
            A_du = []
            b_du = []
            for j in range(m_gen):
                row = [dq_cols[j][r] for r in nz_a] + [-dq_cols[j][r] for r in nz_b]
                if cond_cols is not None:
                    row += [cond_cols[j][k] for k in nz_g]
                A_du.append(row)
                b_du.append(0)
            res_d = linprog(
                [-d_target[r] for r in nz_a] + [0] * (len(nz_b) + len(nz_g)),
                A_ub=np.array(A_du, dtype=float),
                b_ub=np.zeros(m_gen),
                A_eq=np.array([[0] * len(nz_a) + [d_target[r] for r in nz_b] + [0] * len(nz_g)], dtype=float),
                b_eq=np.array([1.0]),
                bounds=(0, None),
                method="highs",
            )
            assert res_d.success
            keep = [k for k, v in enumerate(res_d.x) if v > 1e-8]
            nz_a_k = [nz_a[k] for k in keep if k < len(nz_a)]
            nz_b_k = [nz_b[k - len(nz_a)] for k in keep if len(nz_a) <= k < len(nz_a) + len(nz_b)]
            nz_g_k = [nz_g[k - len(nz_a) - len(nz_b)] for k in keep if k >= len(nz_a) + len(nz_b)]
            dual_tight_k = [
                j for j in range(m_gen)
                if abs(float(np.dot(A_du[j], res_d.x))) < 1e-6
            ]
            eq_rows_k = [
                [dq_cols[j][r] for r in nz_a_k] + [-dq_cols[j][r] for r in nz_b_k]
                + ([cond_cols[j][k] for k in nz_g_k] if cond_cols is not None else [])
                for j in dual_tight_k
            ] + [[0] * len(nz_a_k) + [d_target[r] for r in nz_b_k] + [0] * len(nz_g_k)]
            eq_rhs_k = [0] * len(dual_tight_k) + [1]
            nz_a, nz_b, nz_g = nz_a_k, nz_b_k, nz_g_k
            sol = dm_rref_solve(eq_rows_k, eq_rhs_k)
        assert all(x >= 0 for x in sol)
        a_ex = sol[: len(nz_a)]
        b_ex = sol[len(nz_a) : len(nz_a) + len(nz_b)]
        g_ex = sol[len(nz_a) + len(nz_b) :]
        kappa_exact = sum((a_ex[i] * d_target[nz_a[i]] for i in range(len(nz_a))), Fraction(0))
        # Check G^T(beta - alpha) - C^T gamma >= 0 for ALL generators j!
        for j in range(m_gen):
            val = sum((b_ex[i] * dq_cols[j][nz_b[i]] for i in range(len(nz_b))), Fraction(0)) - sum(
                (a_ex[i] * dq_cols[j][nz_a[i]] for i in range(len(nz_a))), Fraction(0)
            )
            if cond_cols is not None:
                val -= sum((g_ex[i] * cond_cols[j][nz_g[i]] for i in range(len(nz_g))), Fraction(0))
            assert val >= 0
        assert kappa_exact > 1
        dual_cert = {
            "alpha": [(nz_a[i], a_ex[i]) for i in range(len(nz_a)) if a_ex[i] > 0],
            "beta": [(nz_b[i], b_ex[i]) for i in range(len(nz_b)) if b_ex[i] > 0],
            "gamma": [(nz_g[i], g_ex[i]) for i in range(len(nz_g)) if g_ex[i] > 0],
        }
    else:
        kappa_exact = Fraction(1)

    # Exact primal w >= 0 realizing kappa_exact
    nz_w = [j for j, v in enumerate(res.x[:-1]) if v > 1e-7]
    P_cand: list[list[int]] = []
    P_rhs: list[int] = []
    w_est = res.x[:-1]
    for r in range(n_p):
        val = float(np.dot(G[r], w_est))
        if abs(val - d_target[r]) < 1e-6:
            P_cand.append([dq_cols[j][r] for j in nz_w] + [0])
            P_rhs.append(d_target[r])
        if abs(val - res.fun * d_target[r]) < 1e-6:
            P_cand.append([dq_cols[j][r] for j in nz_w] + [-d_target[r]])
            P_rhs.append(0)
    if cond_cols is not None:
        C_arr = np.array(cond_cols, dtype=float).T
        for k in range(n_cond):
            if abs(float(np.dot(C_arr[k], w_est))) < 1e-6:
                P_cand.append([cond_cols[j][k] for j in nz_w] + [0])
                P_rhs.append(0)
    P_cand.append([0] * len(nz_w) + [kappa_exact.denominator])
    P_rhs.append(kappa_exact.numerator)

    sol_p = dm_rref_solve(P_cand, P_rhs)
    w_ex = sol_p[:-1]
    assert sol_p[-1] == kappa_exact
    assert all(w >= 0 for w in w_ex)
    for r in range(n_p):
        dv = sum((w_ex[i] * dq_cols[nz_w[i]][r] for i in range(len(nz_w))), Fraction(0))
        assert d_target[r] <= dv <= kappa_exact * d_target[r]
    if cond_cols is not None:
        for k in range(n_cond):
            cv = sum((w_ex[i] * cond_cols[nz_w[i]][k] for i in range(len(nz_w))), Fraction(0))
            assert cv >= 0

    weights = [
        (labels[nz_w[i]] if labels else nz_w[i], w_ex[i])
        for i in range(len(nz_w))
        if w_ex[i] > 0
    ]
    return {"kappa": kappa_exact, "weights": weights, "dual": dual_cert}


def verify_cb4_plus() -> dict[str, Any]:
    """Verify the 4-party CB_4^+ triangle violation with pairwise S(i|j) >= 0."""
    n = 4
    plist = pairs(n)
    # rho = 1/4 cut(0) + 1/4 cut(2,3) + 1/4 |Phi^+>_{01} + 1/4 |Phi^+>_{12}
    atoms = [
        (Fraction(1, 4), lambda X: 1 if (X & 0b0001) != 0 else 0),
        (Fraction(1, 4), lambda X: 1 if (X & 0b1100) != 0 else 0),
        (Fraction(1, 4), lambda X: 1 if (X & 0b0011).bit_count() == 1 else 0),
        (Fraction(1, 4), lambda X: 1 if (X & 0b0110).bit_count() == 1 else 0),
    ]
    S = {}
    for X in range(1, 16):
        S[X] = sum((w * fn(X) for w, fn in atoms), Fraction(0))
    S[0] = Fraction(0)
    conds = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                conds[(i, j)] = S[(1 << i) | (1 << j)] - S[1 << j]
                assert conds[(i, j)] >= 0
    dQ = {
        (i, j): 2 * S[(1 << i) | (1 << j)] - S[1 << i] - S[1 << j]
        for i, j in plist
    }
    assert dQ[(0, 1)] == 0
    assert dQ[(1, 2)] == 0
    assert dQ[(0, 2)] == 1
    assert dQ[(0, 1)] + dQ[(1, 2)] < dQ[(0, 2)]
    return {
        "S_cond_min": str(min(conds.values())),
        "dQ": {f"{i}-{j}": str(v) for (i, j), v in dQ.items()},
    }


def subspace_entropy_vec(subspaces: list[list[Any]], F_q: int = 2) -> list[int]:
    """Compute exact subspace rank entropy vector rank(sum_{i in X} V_i) over F_q."""
    n = len(subspaces)
    vecs = []
    if F_q == 2:
        for X in range(1, 1 << n):
            basis: list[int] = []
            for i in range(n):
                if (X >> i) & 1:
                    for row_int in subspaces[i]:
                        v = row_int
                        for b in basis:
                            v = min(v, v ^ b)
                        if v:
                            basis.append(v)
                            basis.sort(reverse=True)
            vecs.append(len(basis))
    else:
        for X in range(1, 1 << n):
            rows = []
            for i in range(n):
                if (X >> i) & 1:
                    rows.extend(subspaces[i])
            mat = [list(r) for r in rows]
            rk = 0
            if mat:
                ncols = len(mat[0])
                for col in range(ncols):
                    piv = next((r for r in range(rk, len(mat)) if mat[r][col] % F_q != 0), None)
                    if piv is None:
                        continue
                    mat[rk], mat[piv] = mat[piv], mat[rk]
                    inv = pow(mat[rk][col] % F_q, -1, F_q)
                    mat[rk] = [(x * inv) % F_q for x in mat[rk]]
                    for r in range(len(mat)):
                        if r != rk and mat[r][col] % F_q != 0:
                            f = mat[r][col]
                            mat[r] = [(mat[r][c] - f * mat[rk][c]) % F_q for c in range(ncols)]
                    rk += 1
            vecs.append(rk)
    return vecs


def verify_theorem_1() -> dict[str, Any]:
    """Certify Theorem 1: exact n <= 6 cone hierarchy, 296 MET_6 rays, 1736 POLY_6 rays, ZY98, 112 graphs."""
    out: dict[str, Any] = {}
    # 1. n = 3, 4, 5 exact MET_n extreme rays via cdd.gmp
    for n, expected_rays, expected_orbits in [(3, 3, 1), (4, 7, 2), (5, 25, 3)]:
        rows, plist, pidx = metric_inequalities(n, include_nonneg=True)
        poly = cdd.polyhedron_from_matrix(cdd.matrix_from_array(rows, rep_type=cdd.RepType.INEQUALITY))
        rays = [normalize_int_ray(r[1:]) for r in cdd.copy_generators(poly).array if r[0] == 0]
        assert len(rays) == expected_rays
        orbits: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
        for r in rays:
            rep = canonical_orbit_rep(r, n, plist, pidx)
            orbits.setdefault(rep, []).append(r)
        assert len(orbits) == expected_orbits
        if n == 5:
            # Verify Orbit 3 is K_{2,3} and is realized over F_2^2!
            non_cut = [rep for rep in orbits if set(rep) != {0, 1}]
            assert len(non_cut) == 1
            k23_rep = non_cut[0]
            assert len(orbits[k23_rep]) == 10
            # Realization over F_2^2: two parts are {0, 4} -> (0, F_2^2) and {1,2,3} -> 3 lines
            D5 = dq_projection_matrix(5, plist)
            s_k23 = subspace_entropy_vec([[], [0b01], [0b10], [0b11], [0b01, 0b10]], F_q=2)
            d_k23 = tuple(sum(D5[r][k] * s_k23[k] for k in range(31)) for r in range(10))
            assert d_k23 == k23_rep
            # Explicit 5-atom CB_5^+ witness for K_{2,3} on {0,4} U {1,2,3}
            s_k23_cb5 = {0: Fraction(0)}
            for X in range(1, 32):
                s_k23_cb5[X] = (
                    Fraction(1, 2) * (1 if (X & 8) else 0)
                    + Fraction(1, 2) * (1 if (X & 27) else 0)
                    + Fraction(1, 1) * (1 if (X & 28) else 0)
                    + Fraction(1, 2) * (1 if (X & 5).bit_count() == 1 else 0)
                    + Fraction(1, 2) * (1 if (X & 9).bit_count() == 1 else 0)
                )
            k23_conds = [s_k23_cb5[(1 << i) | (1 << j)] - s_k23_cb5[1 << j] for i in range(5) for j in range(5) if i != j]
            assert min(k23_conds) == 0
            k23_cb5_d = tuple(2 * s_k23_cb5[(1 << i) | (1 << j)] - s_k23_cb5[1 << i] - s_k23_cb5[1 << j] for i, j in plist)
            assert k23_cb5_d == k23_rep
            out["K23_CB5_plus_min_cond"] = str(min(k23_conds))
            out["K23_CB5_plus_singletons"] = [str(s_k23_cb5[1 << i]) for i in range(5)]

    # 2. MET_6 exact DD (296 rays, 8 S_6-orbits)
    rows6, plist6, pidx6 = metric_inequalities(6, include_nonneg=False)
    poly6 = cdd.polyhedron_from_matrix(cdd.matrix_from_array(rows6, rep_type=cdd.RepType.INEQUALITY))
    rays6 = [normalize_int_ray(r[1:]) for r in cdd.copy_generators(poly6).array if r[0] == 0]
    assert len(rays6) == 296
    orbits6: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for r in rays6:
        rep = canonical_orbit_rep(r, 6, plist6, pidx6)
        orbits6.setdefault(rep, []).append(r)
    reps6 = sorted(orbits6.keys())
    assert len(reps6) == 8
    assert [len(orbits6[rep]) for rep in reps6] == [6, 15, 10, 60, 90, 15, 10, 90]

    # Verify Orbits 1-7 lie in SUB_6 (explicit F_2 / F_3 subspace realizations)
    D6 = dq_projection_matrix(6, plist6)
    sub6_witnesses = [
        # Orbit 1: cut({5})
        ([[], [], [], [], [], [0b1]], 2, 1),
        # Orbit 2: cut({4,5})
        ([[], [], [], [], [0b1], [0b1]], 2, 1),
        # Orbit 3: cut({3,4,5})
        ([[], [], [], [0b1], [0b1], [0b1]], 2, 1),
        # Orbit 4: collapsed K_{2,3} over F_2^2
        ([[], [], [0b01], [0b10], [0b11], [0b01, 0b10]], 2, 1),
        # Orbit 5: collapsed K_{2,3} over F_2^2
        ([[0b01], [0b01], [], [0b01, 0b10], [0b10], [0b11]], 2, 1),
        # Orbit 6: K_{2,4} over F_3^2
        ([[], [[1, 0]], [[0, 1]], [[1, 1]], [[1, 2]], [[1, 0], [0, 1]]], 3, 1),
        # Orbit 7: K_{3,3} via Q^+(3, F_2) in F_2^{2x2} (scaled by 2)
        ([[0b1000, 0b0010], [0b1000, 0b0100], [0b1010, 0b0101], [0b0010, 0b0001], [0b1100, 0b0011], [0b0100, 0b0001]], 2, 2),
    ]
    for idx in range(7):
        subs, fq, scale = sub6_witnesses[idx]
        s_vec = subspace_entropy_vec(subs, F_q=fq)
        d_vec = tuple(sum(D6[r][k] * s_vec[k] for k in range(63)) // scale for r in range(15))
        assert d_vec == reps6[idx], f"SUB_6 mismatch on Orbit {idx+1}"

    # Verify ALL 8 orbits of MET_6 lie in CB_6^+ (proving all 296 extreme rays lie in CB_6^+)
    labels6, gens6_S = cb_entropy_generators(6)
    dq_cb6 = [[sum(D6[r][k] * S_vec[k] for k in range(63)) for r in range(15)] for S_vec in gens6_S]
    cond_rows6, _ = cond_entropy_matrix(6)
    cond_cb6 = [[sum(cond_rows6[c][k] * S_vec[k] for k in range(63)) for c in range(30)] for S_vec in gens6_S]
    cb6_orbit_certs = []
    for idx, rep in enumerate(reps6):
        cert = exact_certify_CB(list(rep), dq_cb6, cond_cb6, labels6)
        assert cert["kappa"] == 1
        cb6_orbit_certs.append({"orbit": idx + 1, "size": len(orbits6[rep]), "n_atoms": len(cert["weights"])})

    # 3. Orbit 8 = K_{3,3}-e, 10-orbit D_4 Shannon Farkas proof, and kappa_POLY = 9/8
    orbit8 = reps6[7]
    # Check edges of length 1 in Orbit 8 form K_{3,3}-e
    G_orb8 = nx.Graph()
    G_orb8.add_nodes_from(range(6))
    for r, (i, j) in enumerate(plist6):
        if orbit8[r] == 1:
            G_orb8.add_edge(i, j)
    G_k33e = nx.complete_bipartite_graph(3, 3)
    G_k33e.remove_edge(2, 5)
    assert nx.is_isomorphic(G_orb8, G_k33e)

    ineqs_p6 = poly_ineqs(6)
    res_k33e = exact_certify_cone_H(list(orbit8), ineqs_p6, D6)
    assert res_k33e["kappa"] == Fraction(9, 8)

    # Explicitly verify closed-form D_4-symmetric primal polymatroid h in Gamma_6
    # achieving d_{K_{3,3}-e} <= Pi_6(h) <= (9/8) * d_{K_{3,3}-e}
    # (9/8 on edges, 2 on same-side pairs, 3 on missing edge (2,5))
    def _h_k33e_primal(X: int) -> Fraction:
        if (X & ((1 << 2) | (1 << 5))) == ((1 << 2) | (1 << 5)):
            return Fraction(3)
        p = (X & 0b000111).bit_count()
        q = (X & 0b111000).bit_count()
        if p + q == 1:
            return Fraction(3, 2)
        if p == 1 and q == 1:
            return Fraction(33, 16)
        pair = (max(p, q), min(p, q))
        if pair == (2, 0):
            return Fraction(5, 2)
        if pair == (2, 1):
            return Fraction(21, 8)
        if pair == (2, 2):
            return Fraction(11, 4)
        return Fraction(23, 8)

    h_k33e_vec = [_h_k33e_primal(m) for m in range(1, 64)]
    assert len(ineqs_p6) == 246
    for _, _, row in ineqs_p6:
        assert sum((row[k] * h_k33e_vec[k] for k in range(63)), Fraction(0)) >= 0
    d_k33e_primal = [sum((D6[r][k] * h_k33e_vec[k] for k in range(63)), Fraction(0)) for r in range(15)]
    d_k33e_raw = [nx.shortest_path_length(G_k33e, i, j) for i, j in plist6]
    for r, (i, j) in enumerate(plist6):
        expected_val = Fraction(9, 8) if G_k33e.has_edge(i, j) else (Fraction(3) if (i, j) == (2, 5) else Fraction(2))
        assert d_k33e_primal[r] == expected_val
        assert d_k33e_raw[r] <= d_k33e_primal[r] <= Fraction(9, 8) * d_k33e_raw[r]

    # Construct and verify the exact integer 10-orbit D_4-symmetrized Shannon Farkas proof of I_{K_{3,3}-e} >= 0!
    d_k33e = [nx.shortest_path_length(G_k33e, i, j) for i, j in plist6]
    # Canonical K_{3,3}-e separating inequality:
    # 2 * sum(edges) - sum(same-side) - 2 * d(2,5) >= 0
    c_k33e = []
    for i, j in plist6:
        if G_k33e.has_edge(i, j):
            c_k33e.append(2)
        elif (i, j) == (2, 5):
            c_k33e.append(-2)
        else:
            c_k33e.append(-1)
    assert sum(c_k33e[r] * d_k33e[r] for r in range(15)) == -2

    aut_k33e = [
        perm for perm in itertools.permutations(range(6))
        if all(G_k33e.has_edge(i, j) == G_k33e.has_edge(perm[i], perm[j]) for i, j in plist6)
    ]
    assert len(aut_k33e) == 8

    def act_mask(perm: tuple[int, ...], mask: int) -> int:
        out_m = 0
        for b in range(6):
            if (mask >> b) & 1:
                out_m |= 1 << perm[b]
        return out_m

    ineq_orbits: dict[tuple[int, ...], list[tuple[str, tuple[int, ...], list[int]]]] = {}
    for kind, info, row in ineqs_p6:
        best_row = None
        for perm in aut_k33e:
            new_row = [0] * 63
            for m in range(1, 64):
                if row[m - 1] != 0:
                    new_row[act_mask(perm, m) - 1] += row[m - 1]
            t = tuple(new_row)
            if best_row is None or t < best_row:
                best_row = t
        assert best_row is not None
        ineq_orbits.setdefault(best_row, []).append((kind, info, row))

    orb_keys = sorted(ineq_orbits.keys())
    orb_sums = []
    for ok in orb_keys:
        s = [0] * 63
        for _, _, r in ineq_orbits[ok]:
            for v in range(63):
                s[v] += r[v]
        orb_sums.append(s)
    M_orb_arr = np.array(orb_sums, dtype=float)
    D6_arr = np.array(D6, dtype=float)
    res_d4 = linprog(
        np.ones(len(orb_keys)),
        A_eq=M_orb_arr.T,
        b_eq=D6_arr.T @ np.array(c_k33e, dtype=float),
        bounds=(0, None),
        method="highs",
    )
    assert res_d4.success
    nz_d4 = [i for i, v in enumerate(res_d4.x) if v > 1e-7]
    assert len(nz_d4) == 10
    rhs_d4 = [sum(D6[r][v] * c_k33e[r] for r in range(15)) for v in range(63)]
    y_d4 = dm_rref_solve([[orb_sums[i][v] for i in nz_d4] for v in range(63)], rhs_d4)
    assert all(w > 0 and w.denominator == 1 for w in y_d4)
    for v in range(63):
        assert sum(y_d4[idx] * orb_sums[nz_d4[idx]][v] for idx in range(10)) == rhs_d4[v]
    d4_proof = [
        {
            "orbit_idx": nz_d4[idx],
            "multiplicity": len(ineq_orbits[orb_keys[nz_d4[idx]]]),
            "weight": int(y_d4[idx]),
            "rep": (ineq_orbits[orb_keys[nz_d4[idx]]][0][0], ineq_orbits[orb_keys[nz_d4[idx]]][0][1]),
        }
        for idx in range(10)
    ]

    # 4. Exact Fukuda-Prodon DD of MET_6 cap {90 conjugates of I_{K_{3,3}-e} >= 0}
    conjugates = sorted({
        tuple(c_k33e[pidx6[(min(perm[i], perm[j]), max(perm[i], perm[j]))]] for i, j in plist6)
        for perm in itertools.permutations(range(6))
    })
    assert len(conjugates) == 90

    dd_ineqs = [tuple(r[1:]) for r in rows6]  # 60 triangle inequalities
    dd_rays = list(rays6)
    tight_masks = []
    for r in dd_rays:
        mask = 0
        for idx_i, a in enumerate(dd_ineqs):
            if sum(x * y for x, y in zip(a, r)) == 0:
                mask |= 1 << idx_i
        tight_masks.append(mask)

    dim6 = 15
    for a in conjugates:
        ineq_bit = 1 << len(dd_ineqs)
        dd_ineqs.append(a)
        vals = [sum(x * y for x, y in zip(a, r)) for r in dd_rays]
        pos_idx = [i for i, v in enumerate(vals) if v > 0]
        neg_idx = [i for i, v in enumerate(vals) if v < 0]
        zero_idx = [i for i, v in enumerate(vals) if v == 0]
        if not neg_idx:
            for i in zero_idx:
                tight_masks[i] |= ineq_bit
            continue
        new_rays = [dd_rays[i] for i in pos_idx] + [dd_rays[i] for i in zero_idx]
        new_masks = [tight_masks[i] for i in pos_idx] + [tight_masks[i] | ineq_bit for i in zero_idx]
        for ip in pos_idx:
            mp = tight_masks[ip]
            rp = dd_rays[ip]
            vp = vals[ip]
            for ineg in neg_idx:
                common = mp & tight_masks[ineg]
                if common.bit_count() < dim6 - 2:
                    continue
                if any(k != ip and k != ineg and (common & mk) == common for k, mk in enumerate(tight_masks)):
                    continue
                vn = -vals[ineg]
                rn = dd_rays[ineg]
                comb = [vn * rp[j] + vp * rn[j] for j in range(dim6)]
                new_rays.append(normalize_int_ray(comb))
                new_masks.append(common | ineq_bit)
        dd_rays = new_rays
        tight_masks = new_masks

    assert len(dd_rays) == 1736
    # Verify independently that EVERY one of the 1736 rays satisfies all 150 inequalities and has tight rank 14 (= dim - 1)!
    for r, mask in zip(dd_rays, tight_masks):
        tight_rows = []
        for idx_i, a in enumerate(dd_ineqs):
            dot = sum(x * y for x, y in zip(a, r))
            assert dot >= 0
            if dot == 0:
                tight_rows.append(list(a))
        assert dm_rank(tight_rows) == dim6 - 1

    orbits_90: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    for r in dd_rays:
        rep = canonical_orbit_rep(r, 6, plist6, pidx6)
        orbits_90.setdefault(rep, []).append(r)
    reps_90 = sorted(orbits_90.keys())
    assert len(reps_90) == 12
    assert [len(orbits_90[rep]) for rep in reps_90] == [6, 15, 10, 60, 90, 15, 10, 90, 360, 360, 360, 360]

    # Verify all 12 orbits lie in POLY_6 and test Zhang-Yeung (1680 inequalities) on all 12!
    ineqs_zy6 = ineqs_p6 + zy98_ineqs(6)
    orbit12_summary = []
    for idx, rep in enumerate(reps_90):
        c_poly = exact_certify_cone_H(list(rep), ineqs_p6, D6)
        assert c_poly["kappa"] == 1
        c_zy = exact_certify_cone_H(list(rep), ineqs_zy6, D6)
        c_cb = exact_certify_CB(list(rep), dq_cb6, cond_cb6, labels6)
        assert c_cb["kappa"] == 1
        if idx == 8:  # Orbit 9!
            assert c_zy["kappa"] == Fraction(31, 30)
        else:
            assert c_zy["kappa"] == 1
        orbit12_summary.append({
            "orbit": idx + 1,
            "size": len(orbits_90[rep]),
            "rep": list(rep),
            "kappa_POLY": str(c_poly["kappa"]),
            "kappa_POLY_ZY": str(c_zy["kappa"]),
            "in_CB6_plus": c_cb["kappa"] == 1,
        })

    # 5. Exhaustive classification of all 112 connected 6-vertex graphs
    atlas = nx.graph_atlas_g()
    g6 = [g for g in atlas if g.number_of_nodes() == 6 and nx.is_connected(g)]
    assert len(g6) == 112
    g6_fails = []
    for idx, G in enumerate(g6):
        d = [nx.shortest_path_length(G, i, j) for i, j in plist6]
        c_p = exact_certify_cone_H(d, ineqs_p6, D6)
        if c_p["kappa"] > 1:
            c_cb = exact_certify_CB(d, dq_cb6, cond_cb6, labels6)
            assert c_cb["kappa"] == 1
            g6_fails.append({
                "atlas_idx": idx,
                "name": G.name,
                "edges": list(G.edges()),
                "kappa_POLY": str(c_p["kappa"]),
                "in_CB6_plus": True,
            })
    assert len(g6_fails) == 2
    assert {g6_fails[0]["kappa_POLY"], g6_fails[1]["kappa_POLY"]} == {"9/8", "17/16"}

    out["MET6_rays"] = len(rays6)
    out["MET6_orbits"] = len(reps6)
    out["CB6_plus_orbits"] = cb6_orbit_certs
    out["D4_K33e_proof"] = d4_proof
    out["K33e_primal_h_verified"] = True
    out["K33e_primal_num_ineqs"] = len(ineqs_p6)
    out["K33e_primal_d"] = [str(x) for x in d_k33e_primal]
    out["POLY6_rays"] = len(dd_rays)
    out["POLY6_orbits"] = orbit12_summary
    out["n6_graphs_total"] = len(g6)
    out["n6_graphs_fail_POLY"] = g6_fails
    return out


def verify_segre_quadric(q: int) -> dict[str, Any]:
    """Verify Q^+(3, F_q) in F_q^{2x2} yields exact K_{q+1, q+1} for prime q."""
    pts = [(1, t) for t in range(q)] + [(0, 1)]
    L_subs = [[[u0, u1, 0, 0], [0, 0, u0, u1]] for u0, u1 in pts]
    M_subs = [[[v0, 0, v1, 0], [0, v0, 0, v1]] for v0, v1 in pts]
    all_subs = L_subs + M_subs
    m = len(pts)

    def rk_mod_q(rows: list[list[int]]) -> int:
        mat = [list(r) for r in rows]
        rc = 0
        for col in range(4):
            piv = next((r for r in range(rc, len(mat)) if mat[r][col] % q != 0), None)
            if piv is None:
                continue
            mat[rc], mat[piv] = mat[piv], mat[rc]
            inv = pow(mat[rc][col] % q, -1, q)
            mat[rc] = [(x * inv) % q for x in mat[rc]]
            for r in range(len(mat)):
                if r != rc and mat[r][col] % q != 0:
                    f = mat[r][col]
                    mat[r] = [(mat[r][c] - f * mat[rc][c]) % q for c in range(4)]
            rc += 1
        return rc

    for i in range(2 * m):
        assert rk_mod_q(all_subs[i]) == 2
        for j in range(i + 1, 2 * m):
            d_ij = 2 * rk_mod_q(all_subs[i] + all_subs[j]) - 4
            expected = 4 if ((i < m) == (j < m)) else 2
            assert d_ij == expected
    return {"q": q, "m": m, "vertices": 2 * m}


def verify_rem4_quantum_state(d_rem4: list[int], plist7: list[tuple[int, int]]) -> dict[str, Any]:
    """Verify exact isometric binary-qubit realization of Rem #4 (G800) in M_7^{q,+}."""
    # Exact 4-atom state (multiplied by 4 for pure integer qubits/bits, then normalized by 1/4):
    # Atom 1: 2 copies of Bell pair |Phi^+>_{34}  (weight 1/2)
    # Atom 2: 2 copies of private classical bit at party 3 (weight 1/2)
    # Atom 3: 2 copies of F_2^2-subspace atom: 0->{e1}, 1->{e2}, 2->{e1+e2}, 3->{e1+e2}, {4,5,6}->{0} (weight 1/2)
    # Atom 4: 1 copy of F_2^4-spread K_{2,4} atom (dim 0,2,4): 0->W_0, 1->W_1, 2->W_2, 3->W_2, 4->W_4, 5->F_2^4, 6->{0}
    # (Here S(X) = 1/4 * [2 S_Bell(3,4) + 2 S_cut(3) + 2 S_{F_2^2} + S_{F_2^4}]).
    def s_f2_2(X: int) -> int:
        # 0: e1, 1: e2, 2: e1+e2, 3: e1+e2, 4,5,6: 0
        basis = []
        vecs = {0: 0b01, 1: 0b10, 2: 0b11, 3: 0b11}
        for v, vec in vecs.items():
            if (X >> v) & 1:
                if vec not in basis:
                    basis.append(vec)
        if not basis:
            return 0
        if len(basis) == 1:
            return 1
        return 2

    def s_f2_4(X: int) -> int:
        # Explicit 2-planes in F_2^4 = F_4^2 (dim 0, 2, 4):
        # 0 -> W_0, 1 -> W_1, 2 -> W_2, 3 -> W_2, 4 -> W_4, 5 -> full F_2^4, 6 -> 0
        if (X >> 5) & 1:
            return 4
        w_blocks = set()
        for v, b in [(0, 0), (1, 1), (2, 2), (3, 2), (4, 4)]:
            if (X >> v) & 1:
                w_blocks.add(b)
        if len(w_blocks) >= 2:
            return 4
        if len(w_blocks) == 1:
            return 2
        return 0

    S: dict[int, Fraction] = {0: Fraction(0)}
    for X in range(1, 128):
        s_bell = 1 if (X & ((1 << 3) | (1 << 4))).bit_count() == 1 else 0
        s_bit3 = 1 if (X & (1 << 3)) != 0 else 0
        val = Fraction(2 * s_bell + 2 * s_bit3 + 2 * s_f2_2(X) + s_f2_4(X), 4)
        S[X] = val

    # Check all 42 pairwise conditional entropies S(i|j) >= 0!
    min_cond = None
    cond_matrix = {}
    for i in range(7):
        for j in range(7):
            if i == j:
                continue
            cij = S[(1 << i) | (1 << j)] - S[1 << j]
            cond_matrix[f"{i}|{j}"] = str(cij)
            if min_cond is None or cij < min_cond:
                min_cond = cij
    assert min_cond is not None and min_cond >= 0

    # Check all 21 pairwise distances match d_rem4!
    for r, (i, j) in enumerate(plist7):
        dij = 2 * S[(1 << i) | (1 << j)] - S[1 << i] - S[1 << j]
        assert dij == d_rem4[r], f"Distance mismatch on ({i},{j}): got {dij}, expected {d_rem4[r]}"

    return {
        "min_conditional_entropy": str(min_cond),
        "singletons_S": [str(S[1 << i]) for i in range(7)],
        "total_state_entropy": str(S[127]),
        "verified_21_distances": True,
    }


def verify_theorem_2_and_qfail() -> dict[str, Any]:
    """Certify Theorem 2 (Segre quadric, all 853 n=7 graphs, Rem #4) and QFail1/QFail2."""
    segre = [verify_segre_quadric(q) for q in [2, 3, 5, 7]]

    atlas = nx.graph_atlas_g()
    g7 = [g for g in atlas if g.number_of_nodes() == 7 and nx.is_connected(g)]
    assert len(g7) == 853
    plist7 = pairs(7)
    pidx7 = {p: i for i, p in enumerate(plist7)}
    D7 = dq_projection_matrix(7, plist7)
    ineqs_poly7 = poly_ineqs(7)
    ineqs_q7 = qcone_ineqs(7)
    labels7, gens7_S = cb_entropy_generators(7)
    dq_cb7 = [[sum(D7[r][k] * S_vec[k] for k in range(127)) for r in range(21)] for S_vec in gens7_S]
    cond_rows7, _ = cond_entropy_matrix(7)
    cond_cb7 = [[sum(cond_rows7[c][k] * S_vec[k] for k in range(127)) for c in range(42)] for S_vec in gens7_S]

    fail_poly7 = []
    fail_cb7 = []
    fail_both7 = []
    fail_q7 = []

    for idx, G in enumerate(g7):
        d = [nx.shortest_path_length(G, i, j) for i, j in plist7]
        c_cb = exact_certify_CB(d, dq_cb7, None, labels7)
        c_poly = exact_certify_cone_H(d, ineqs_poly7, D7, need_dual_if_fail=(idx == 409))
        # Note: if c_cb == 1, then d in CB_7 subset Q_7 automatically, yet we also verify Q_7 directly!
        c_q = exact_certify_cone_H(d, ineqs_q7, D7, need_dual_if_fail=True)

        if c_poly["kappa"] > 1:
            fail_poly7.append((idx, G.name, str(c_poly["kappa"])))
        if c_cb["kappa"] > 1:
            fail_cb7.append((idx, G.name, str(c_cb["kappa"])))
        if c_poly["kappa"] > 1 and c_cb["kappa"] > 1:
            fail_both7.append((idx, G.name, str(c_poly["kappa"]), str(c_cb["kappa"])))
        if c_q["kappa"] > 1:
            # Verify an exact Aut(G)-symmetric pure-state primal in QCONE_7 (S([7])=0, S(X)=S([7]\X))
            aut_g = [
                perm for perm in itertools.permutations(range(7))
                if all(G.has_edge(i, j) == G.has_edge(perm[i], perm[j]) for i, j in plist7)
            ]
            pure_orbs: dict[int, list[int]] = {}
            for m in range(1, 127):
                c1 = min(sum((1 << perm[b]) for b in range(7) if (m >> b) & 1) for perm in aut_g)
                m2 = 127 ^ m
                c2 = min(sum((1 << perm[b]) for b in range(7) if (m2 >> b) & 1) for perm in aut_g)
                pure_orbs.setdefault(min(c1, c2), []).append(m)
            orb_keys_p = sorted(pure_orbs.keys())
            m_to_orb_p = {m: oi for oi, ok in enumerate(orb_keys_p) for m in pure_orbs[ok]}
            P_red = np.zeros((127, len(orb_keys_p)), dtype=int)
            for m in range(1, 127):
                P_red[m - 1, m_to_orb_p[m]] = 1
            M_full = np.array([r for _, _, r in ineqs_q7], dtype=int)
            uniq_M = np.unique(M_full @ P_red, axis=0)
            D_red = np.array(D7, dtype=int) @ P_red
            iq_red = [("Q", i, [int(x) for x in row]) for i, row in enumerate(uniq_M)]
            D_red_list = [[int(x) for x in row] for row in D_red]
            rc_pure = exact_certify_cone_H(d, iq_red, D_red_list, need_dual_if_fail=False)
            assert rc_pure["kappa"] == c_q["kappa"]
            h_orb = rc_pure["primal_s"]
            h_pure_full = [Fraction(0) if m == 127 else h_orb[m_to_orb_p[m]] for m in range(1, 128)]
            # Explicitly assert ALL 896 elemental SSA+WM inequalities (672 SSA + 224 WM) and ALL 21 distances hold on h_pure_full!
            assert len(ineqs_q7) == 896
            for _, _, r in ineqs_q7:
                assert sum((r[k] * h_pure_full[k] for k in range(127)), Fraction(0)) >= 0
            for r_idx in range(21):
                dv = sum((D7[r_idx][k] * h_pure_full[k] for k in range(127)), Fraction(0))
                assert d[r_idx] <= dv <= c_q["kappa"] * d[r_idx]
            lcm_p = 1
            for x in h_orb:
                lcm_p = math.lcm(lcm_p, x.denominator)
            pure_orbit_table = []
            for oi, ok in enumerate(orb_keys_p):
                rep_m = min(pure_orbs[ok], key=lambda x: (x.bit_count(), x))
                pure_orbit_table.append({
                    "orb": oi,
                    "mult": len(pure_orbs[ok]),
                    "rep": [b for b in range(7) if (rep_m >> b) & 1],
                    "val": str(h_orb[oi]),
                    "scaled": int(h_orb[oi] * lcm_p),
                })
            fail_q7.append({
                "atlas_idx": idx,
                "name": G.name,
                "edges": list(G.edges()),
                "kappa_POLY": str(c_poly["kappa"]),
                "kappa_CB": str(c_cb["kappa"]),
                "kappa_Q": str(c_q["kappa"]),
                "n_dual_terms": len(c_q["dual"]["y"]),
                "n_ssa": sum(1 for (k, _), _ in c_q["dual"]["y"] if k == "SSA"),
                "n_wm": sum(1 for (k, _), _ in c_q["dual"]["y"] if k == "WM"),
                "pure_primal_verified": True,
                "num_ineq_checked": len(ineqs_q7),
                "pure_primal_lcm": lcm_p,
                "pure_primal_orbits": pure_orbit_table,
            })

    assert len(fail_poly7) == 38
    assert len(fail_cb7) == 128
    assert len(fail_both7) == 16
    assert len(fail_q7) == 2
    assert {q["name"]: q["kappa_Q"] for q in fail_q7} == {"G708": "21/20", "G873": "41/40"}

    # Identify Rem #4 (index 4 among the 14 remaining graphs in Fail(POLY_7) cap Fail(CB_7) \ Fail(Q_7))
    qfail_idxs = {q["atlas_idx"] for q in fail_q7}
    rem_list = [x for x in fail_both7 if x[0] not in qfail_idxs]
    assert len(rem_list) == 14
    rem4_idx, rem4_name, kp_r4, kcb_r4 = rem_list[4]
    assert rem4_name == "G800" and kp_r4 == "17/16" and kcb_r4 == "13/12"
    G_rem4 = g7[rem4_idx]
    d_rem4 = [nx.shortest_path_length(G_rem4, i, j) for i, j in plist7]

    # Check CB_7^+ distortion on Rem #4 is also 13/12
    c_cbp_rem4 = exact_certify_CB(d_rem4, dq_cb7, cond_cb7, labels7)
    assert c_cbp_rem4["kappa"] == Fraction(13, 12)

    # Verify F_4 inequality directly on Rem #4, all 126 cuts, and all 21 Bell pairs
    def eval_F4(dvec: list[int]) -> int:
        pos = sum(dvec[pidx7[(min(x, u), max(x, u))]] for x in [0, 1, 2, 3, 4] for u in [5, 6])
        neg = dvec[pidx7[(5, 6)]] + sum(
            dvec[pidx7[(min(a, b), max(a, b))]] for a, b in [(0, 3), (3, 1), (1, 2), (2, 4), (4, 0)]
        )
        return pos - neg

    f4_rem4 = eval_F4(d_rem4)
    assert f4_rem4 == -1
    # Exhaustive check over ALL 126 cuts and ALL 21 Bell pairs
    cut_F4_vals = []
    for S in range(1, 127):
        d_cut = [1 if (((S >> i) & 1) != ((S >> j) & 1)) else 0 for i, j in plist7]
        cut_F4_vals.append(eval_F4(d_cut))
    bell_F4_vals = []
    for a, b in plist7:
        d_bell = [
            -2 if (i, j) == (a, b) else (1 if (i in (a, b)) != (j in (a, b)) else 0)
            for i, j in plist7
        ]
        bell_F4_vals.append(eval_F4(d_bell))
    assert min(cut_F4_vals) == 0
    assert min(bell_F4_vals) == 0

    rem4_state = verify_rem4_quantum_state(d_rem4, plist7)

    # Also verify Open Problem 1 (Sep #0 = G550, and 6 vs 8 split of Rem over GHZ + F_2^4-spread)
    rem0_idx, rem0_name, kp_r0, kcb_r0 = rem_list[0]
    G_sep0 = g7[rem0_idx]
    assert rem0_name == "G550" and kp_r0 == "9/8" and kcb_r0 == "8/7"
    sep0_info = {
        "atlas_idx": rem0_idx,
        "name": rem0_name,
        "edges": list(G_sep0.edges()),
        "kappa_POLY": kp_r0,
        "kappa_CB": kcb_r0,
        "kappa_Q": "1",
    }

    # Build GHZ (2..7 parties) + F_2^4-spread subspace atoms (which include cuts via {0, full})
    spread_atoms_set: set[tuple[int, ...]] = set()

    def _bt_spread(v_idx: int, max_b: int, cur: list[int]) -> None:
        if v_idx == 7:
            s_vec = []
            for X in range(1, 128):
                has_full = False
                w_mask = 0
                for u in range(7):
                    if (X >> u) & 1:
                        lab = cur[u]
                        if lab == -2:
                            has_full = True
                            break
                        if lab >= 0:
                            w_mask |= 1 << lab
                if has_full or w_mask.bit_count() >= 2:
                    s_vec.append(2)
                elif w_mask != 0:
                    s_vec.append(1)
                else:
                    s_vec.append(0)
            if any(s_vec):
                spread_atoms_set.add(tuple(s_vec))
            return
        for lab in [-1, -2] + list(range(min(5, max_b + 2))):
            cur.append(lab)
            _bt_spread(v_idx + 1, max(max_b, lab), cur)
            cur.pop()

    _bt_spread(0, -1, [])
    spread_atoms_list = [list(s) for s in sorted(spread_atoms_set)]
    ghz_atoms_list = [
        [1 if 0 < (X & mask) < mask else 0 for X in range(1, 128)]
        for mask in range(1, 128)
        if mask.bit_count() >= 2
    ]
    sg_atoms = ghz_atoms_list + spread_atoms_list
    sg_labels = [("ghz", mask) for mask in range(1, 128) if mask.bit_count() >= 2] + [
        ("spread", i) for i in range(len(spread_atoms_list))
    ]
    dq_sg = [[sum(D7[r][k] * S_vec[k] for k in range(127)) for r in range(21)] for S_vec in sg_atoms]
    cond_sg = [[sum(cond_rows7[c][k] * S_vec[k] for k in range(127)) for c in range(42)] for S_vec in sg_atoms]

    rem_realized = []
    rem_separated = []
    for r_pos, (r_idx, r_name, _, _) in enumerate(rem_list):
        d_rem = [nx.shortest_path_length(g7[r_idx], i, j) for i, j in plist7]
        c_sg = exact_certify_CB(d_rem, dq_sg, cond_sg, sg_labels)
        if c_sg["kappa"] == 1:
            rem_realized.append({"rem_num": r_pos, "name": r_name, "n_atoms": len(c_sg["weights"])})
        else:
            rem_separated.append({"rem_num": r_pos, "name": r_name, "kappa_sg": str(c_sg["kappa"])})
    assert len(rem_realized) == 6
    assert len(rem_separated) == 8
    assert rem_separated[0]["name"] == "G550"

    return {
        "segre_quadrics": segre,
        "n7_total": len(g7),
        "n7_fail_POLY": len(fail_poly7),
        "n7_fail_CB": len(fail_cb7),
        "n7_fail_both_POLY_CB": len(fail_both7),
        "n7_fail_Q": fail_q7,
        "n7_rem_count": len(rem_list),
        "rem_ghz_spread_realized_count": len(rem_realized),
        "rem_ghz_spread_separated_count": len(rem_separated),
        "sep0": sep0_info,
        "rem4": {
            "atlas_idx": rem4_idx,
            "name": rem4_name,
            "edges": list(G_rem4.edges()),
            "kappa_POLY": kp_r4,
            "kappa_CB": kcb_r4,
            "kappa_CB_plus": str(c_cbp_rem4["kappa"]),
            "F4_value": f4_rem4,
            "min_F4_126_cuts": min(cut_F4_vals),
            "min_F4_21_bells": min(bell_F4_vals),
            "quantum_realization": rem4_state,
        },
    }


def _canon(k11: int, k10: int, k01: int) -> tuple[int, int, int]:
    return (k11, k01, k10) if k10 < k01 else (k11, k10, k01)


def build_kmm_sym_model(m: int, include_wm: bool, include_mono: bool) -> tuple[list[tuple[int, int, int]], list[tuple[str, Any, list[int]]], list[list[int]]]:
    """Build Z_2 x S_m-reduced model for K_{m,m} - M."""
    states = [
        (k11, k10, k01)
        for k11 in range(m + 1)
        for k10 in range(m - k11 + 1)
        for k01 in range(min(k10, m - k11 - k10) + 1)
        if (k11, k10, k01) != (0, 0, 0)
    ]
    s_idx = {s: idx for idx, s in enumerate(states)}
    n_vars = len(states)
    ineqs_meta: dict[tuple[int, ...], tuple[str, Any]] = {}

    def add_ineq(tag: tuple[str, Any], pos_terms: list[tuple[int, int, int]], neg_terms: list[tuple[int, int, int]]) -> None:
        vec = [0] * n_vars
        for t in pos_terms:
            c = _canon(*t)
            if c != (0, 0, 0):
                vec[s_idx[c]] += 1
        for t in neg_terms:
            c = _canon(*t)
            if c != (0, 0, 0):
                vec[s_idx[c]] -= 1
        if any(vec):
            tv = tuple(vec)
            if tv not in ineqs_meta:
                ineqs_meta[tv] = tag

    for k11 in range(m):
        for k10 in range(m - k11):
            for k01 in range(m - k11 - k10):
                add_ineq(
                    ("SSA-match", (k11, k10, k01)),
                    [(k11, k10 + 1, k01), (k11, k10, k01 + 1)],
                    [(k11 + 1, k10, k01), (k11, k10, k01)],
                )
    for u, v in [(0, 0), (1, 0), (1, 1)]:
        for k11 in range(m - 1):
            for k10 in range(m - 1 - k11):
                for k01 in range(m - 1 - k11 - k10):
                    add_ineq(
                        ("SSA-same", (u, v, k11, k10, k01)),
                        [(k11 + u, k10 + 1 - u, k01 + v), (k11 + v, k10 + 1 - v, k01 + u)],
                        [(k11 + u + v, k10 + 2 - u - v, k01), (k11, k10, k01 + u + v)],
                    )
    for u in (0, 1):
        for v in (0, 1):
            for k11 in range(m - 1):
                for k10 in range(m - 1 - k11):
                    for k01 in range(m - 1 - k11 - k10):
                        add_ineq(
                            ("SSA-edge", (u, v, k11, k10, k01)),
                            [(k11 + u, k10 + 1 - u + v, k01), (k11 + v, k10, k01 + u + 1 - v)],
                            [(k11 + u + v, k10 + 1 - u, k01 + 1 - v), (k11, k10 + v, k01 + u)],
                        )
    if include_wm:
        for k11 in range(m):
            for k10 in range(m - k11):
                for k01 in range(m - k11 - k10):
                    k00 = (m - 1) - k11 - k10 - k01
                    add_ineq(
                        ("WM", (k11, k10, k01)),
                        [(k11, k10 + 1, k01), (k00 + 1, k01, k10)],
                        [(k11, k10, k01), (k00, k01, k10 + 1)],
                    )
    if include_mono:
        add_ineq(("MONO", ()), [(m, 0, 0)], [(m - 1, 0, 1)])

    ineqs = [(tag[0], tag[1], list(vec)) for vec, tag in sorted(ineqs_meta.items())]
    D_rows = [[0] * n_vars for _ in range(3)]
    D_rows[0][s_idx[(0, 1, 1)]] += 2
    D_rows[0][s_idx[(0, 1, 0)]] -= 2
    D_rows[1][s_idx[(0, 2, 0)]] += 2
    D_rows[1][s_idx[(0, 1, 0)]] -= 2
    D_rows[2][s_idx[(1, 0, 0)]] += 2
    D_rows[2][s_idx[(0, 1, 0)]] -= 2
    return states, ineqs, D_rows


def verify_theorem_3_staircase() -> dict[str, Any]:
    """Certify exact rational K_{m,m}-M parity staircase (m=3..18 POLY/Q, m=3..12 CUT)."""
    staircase = []
    # Analytic step formula check for POLY_{2m}:
    # kappa_POLY(m) = 1 + sum_{k=3}^{floor((m+1)/2)} 1 / (2 (k-1)! (k-1)(k-2))
    m5_dual = None
    for m in range(3, 19):
        _, ineqs_p, D_p = build_kmm_sym_model(m, include_wm=False, include_mono=True)
        _, ineqs_q, D_q = build_kmm_sym_model(m, include_wm=True, include_mono=False)
        res_p = exact_certify_cone_H([1, 2, 3], ineqs_p, D_p, need_dual_if_fail=(m <= 8))
        res_q = exact_certify_cone_H([1, 2, 3], ineqs_q, D_q, need_dual_if_fail=(m <= 8))
        kp, kq = res_p["kappa"], res_q["kappa"]

        formula_p = Fraction(1) + sum(
            (Fraction(1, 2 * math.factorial(k - 1) * (k - 1) * (k - 2)) for k in range(3, (m + 1) // 2 + 1)),
            Fraction(0),
        )
        assert kp == formula_p, f"Formula mismatch at m={m}: {kp} vs {formula_p}"
        if m % 2 == 0:
            assert kq == kp
        elif m >= 5:
            assert kq < kp

        k_cut_str = None
        if m <= 12:
            cuts_vec: set[tuple[Fraction, Fraction, Fraction]] = set()
            for n11 in range(m + 1):
                for n10 in range(m - n11 + 1):
                    for n01 in range(m - n11 - n10 + 1):
                        n00 = m - n11 - n10 - n01
                        sA, cA = n11 + n10, n01 + n00
                        sB, cB = n11 + n01, n10 + n00
                        cut_match = n10 + n01
                        cut_edge = (sA * cB + cA * sB) - cut_match
                        cut_same = sA * cA + sB * cB
                        if cut_edge == cut_same == cut_match == 0:
                            continue
                        cuts_vec.add((
                            Fraction(cut_edge, m * (m - 1)),
                            Fraction(cut_same, m * (m - 1)),
                            Fraction(cut_match, m),
                        ))
            # Scale cuts_vec by m*(m-1) to pass exact integers into exact_certify_CB!
            scale = m * (m - 1)
            c_list = sorted(cuts_vec)
            dq_cut_cols = [[int(v * scale) for v in vec] for vec in c_list]
            # Wait: scaling generators leaves cone invariant, and target [1,2,3] stays [1,2,3]
            c_cut = exact_certify_CB([1, 2, 3], dq_cut_cols)
            k_cut = c_cut["kappa"]
            expected_cut = Fraction(1) if m <= 4 else Fraction(2 * ((m + 1) // 2 - 1), (m + 1) // 2)
            assert k_cut == expected_cut
            k_cut_str = str(k_cut)

        if m == 5:
            assert kq == Fraction(12, 11) and kp == Fraction(9, 8)
            # Check per-pair (11, -8, -3) inequality from m=5 dual:
            # beta=(0->1), alpha=(1->3/11, 2->2/11) => per-orbit (11, -3, -2),
            # dividing by orbit sizes (20, 20, 5) * 20 => per-pair (11, -3, -8)!
            m5_dual = {
                "n_orbits": len(res_q["dual"]["y"]),
                "alpha": [(r, str(w)) for r, w in res_q["dual"]["alpha"]],
                "beta": [(r, str(w)) for r, w in res_q["dual"]["beta"]],
                "y": [(k, info, str(w)) for (k, info), w in res_q["dual"]["y"]],
            }

        staircase.append({
            "m": m,
            "n": 2 * m,
            "kappa_CUT": k_cut_str,
            "kappa_POLY": str(kp),
            "kappa_Q": str(kq),
            "kappa_POLY_float": float(kp),
            "kappa_Q_float": float(kq),
        })

    return {"staircase": staircase, "m5_Q_dual": m5_dual}


def run_all(save_json: Path | None = None) -> dict[str, Any]:
    """Run full exact rational verification of all theorems."""
    t0 = time.time()
    print("[1/4] Verifying CB_4^+...", flush=True)
    cb4 = verify_cb4_plus()
    print(f"[2/4] Verifying Theorem 1 (elapsed {time.time()-t0:.1f}s)...", flush=True)
    thm1 = verify_theorem_1()
    print(f"[3/4] Verifying Theorem 2 & 853 graphs (elapsed {time.time()-t0:.1f}s)...", flush=True)
    thm2 = verify_theorem_2_and_qfail()
    print(f"[4/4] Verifying Theorem 3 staircase (elapsed {time.time()-t0:.1f}s)...", flush=True)
    thm3 = verify_theorem_3_staircase()
    results = {
        "cb4_plus": cb4,
        "theorem_1": thm1,
        "theorem_2_and_qfail": thm2,
        "theorem_3_staircase": thm3,
        "elapsed_seconds": round(time.time() - t0, 2),
    }
    if save_json is not None:
        save_json.parent.mkdir(parents=True, exist_ok=True)
        save_json.write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


if __name__ == "__main__":
    out_path = Path(__file__).resolve().parent / "certified_results.json"
    res = run_all(save_json=out_path)
    print(f"ALL EXACT RATIONAL VERIFICATIONS PASSED in {res['elapsed_seconds']}s!")
    print(f"MET_6 rays={res['theorem_1']['MET6_rays']} ({res['theorem_1']['MET6_orbits']} orbits)")
    print(f"POLY_6 rays={res['theorem_1']['POLY6_rays']} ({len(res['theorem_1']['POLY6_orbits'])} orbits)")
    print(f"n=7 graphs: {res['theorem_2_and_qfail']['n7_total']} total, "
          f"{res['theorem_2_and_qfail']['n7_fail_POLY']} fail POLY_7, "
          f"{res['theorem_2_and_qfail']['n7_fail_CB']} fail CB_7, "
          f"{len(res['theorem_2_and_qfail']['n7_fail_Q'])} fail Q_7")
    for row in res["theorem_3_staircase"]["staircase"]:
        print(f"  m={row['m']:2d} (n={row['n']:2d}): CUT={str(row['kappa_CUT']):>6}, POLY={row['kappa_POLY']:>14}, Q={row['kappa_Q']:>14}")
