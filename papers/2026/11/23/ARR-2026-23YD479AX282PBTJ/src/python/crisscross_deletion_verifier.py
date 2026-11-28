"""
Exact zero-float integer & rational verifier for Sharp Non-Asymptotic
Sphere-Packing Bounds on (1,1)-Criss-Cross Deletion-Correcting Codes via
Run-Tiered Bad-Array Packing and Exact Levenshtein Indel-Pair Deduplication
(strictly advancing Li, Sun, and Ge, arXiv:2611.34447v1).

Strict AST purity: zero float literals, zero '/', zero '**', zero floating-point
libraries. Every calculation uses exact integers and reduced rational pairs.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from typing import Any

Rat = tuple[int, int]


def canonical_json_sha256(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def ipow(base: int, exp: int) -> int:
    if exp < 0:
        raise ValueError("Negative exponent")
    res = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res *= b
        b *= b
        e >>= 1
    return res


def q(num: int, den: int = 1) -> Rat:
    if den == 0:
        raise ZeroDivisionError("Zero denominator")
    if den < 0:
        num = -num
        den = -den
    g = math.gcd(abs(num), den)
    return (num // g, den // g)


def q_add(a: Rat, b: Rat) -> Rat:
    return q(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def q_mul(a: Rat, b: Rat) -> Rat:
    return q(a[0] * b[0], a[1] * b[1])


def q_div(a: Rat, b: Rat) -> Rat:
    if b[0] == 0:
        raise ZeroDivisionError("Division by zero")
    return q(a[0] * b[1], a[1] * b[0])


def q_cmp(a: Rat, b: Rat) -> int:
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    return -1 if lhs < rhs else (1 if lhs > rhs else 0)


def q_list(a: Rat) -> list[int]:
    return [a[0], a[1]]


# ---------------------------------------------------------------------------
# Theorem 1: Exact Single-Indel Confusable Pair Count P_indel(q, L)
# ---------------------------------------------------------------------------


def exact_indel_confusable_pairs_bruteforce(q_val: int, L: int) -> dict[str, Any]:
    """
    Exhaustively count ordered pairs (u, v) in Sigma_q^L x Sigma_q^L satisfying
    D_1(u) cap D_1(v) != empty, and compare against:
      - Li-Sun-Ge Lemma 6 bound: q^{L+1} * L^2
      - Our Theorem 1 Levenshtein diagonal+swap deduplicated bound:
          P_sharp(q, L) = q^{L-1} * (L^2 * (q-1)^2 + 2*q - 1).
    """
    if q_val < 2 or L < 2:
        raise ValueError("Require q >= 2, L >= 2")
    strs = list(itertools.product(range(q_val), repeat=L))
    d1 = {s: {s[:i] + s[i + 1 :] for i in range(L)} for s in strs}
    exact_cnt = sum(1 for u in strs for v in strs if d1[u] & d1[v])
    our_bound = ipow(q_val, L - 1) * (L * L * (q_val - 1) * (q_val - 1) + 2 * q_val - 1)
    lsg_bound = ipow(q_val, L + 1) * L * L
    if exact_cnt > our_bound:
        raise AssertionError("Theorem 1 bound violated!")
    if our_bound >= lsg_bound:
        raise AssertionError("Theorem 1 failed to strictly beat Li-Sun-Ge Lemma 6!")
    return {
        "q": q_val,
        "L": L,
        "exact_confusable_pairs": exact_cnt,
        "our_theorem1_bound": our_bound,
        "lsg_lemma6_bound": lsg_bound,
        "exact_equality_at_L2": (L == 2 and exact_cnt == our_bound),
        "tightening_ratio_exact": q_list(q(lsg_bound, our_bound)),
    }


# ---------------------------------------------------------------------------
# Theorem 2 & Theorem 3: Three-Tier Run-Decomposed Sphere-Packing Bounds
# (Square n x n and Rectangular m x n)
# ---------------------------------------------------------------------------


def lsg_epsilon_square(q_val: int, n: int) -> Rat:
    """Li-Sun-Ge Theorem 1 exact rational epsilon_{q,n}^{LSG} = 2(n-2)(n-1)^3(n+1) / q^{n-2}."""
    num = 2 * (n - 2) * ipow(n - 1, 3) * (n + 1)
    den = ipow(q_val, n - 2)
    return q(num, den)


def sharp_epsilon_rectangular(q_val: int, m: int, n: int, s_r: int, s_c: int) -> Rat:
    """
    Exact rational Ironclad Three-Tier Run-Decomposed Sphere-Packing overhead epsilon_{q,m,n}^{sharp}(s_r, s_c)
    for rectangular m x n q-ary arrays (m, n >= 3):
      |C| <= (q^{(m-1)(n-1)} / (m*n)) * (1 + epsilon^{sharp}).
    Exact proof-matched components:
      - Bad subarray space B_{m-1,n-1} (Li-Sun-Ge Def. 2: adjacent rows or cols with intersecting D_1 balls),
        bounded via our Theorem 1 deduplicated P_indel:
          |B_row|/Q <= (m-2) * ((n-1)^2*(q-1)^2 + 2q - 1) / q^n,
          |B_col|/Q <= (n-2) * ((m-1)^2*(q-1)^2 + 2q - 1) / q^m.
      - Exact Tier-C_2b superset L_{q,m,n}^{exact}(s_r, s_c):
        Every X in C_2b (|D_{1,1}(X) cap B_{m-1,n-1}| <= s - 1) has EITHER some column j in [1..n]
        with rho_row(X^{(-j)}) <= s_r + 1 OR some row i in [1..m] with rho_col(X^{(-i)}) <= s_c + 1:
          L_row(s_r) = n * q^m * sum_{r=1}^{min(m, s_r+1)} C(m-1, r-1) * q^{n-1} * (q^{n-1} - 1)^{r-1},
          L_col(s_c) = m * q^n * sum_{r=1}^{min(n, s_c+1)} C(n-1, r-1) * q^{m-1} * (q^{m-1} - 1)^{r-1}.
      With s = min(s_r, s_c) and Q = q^{(m-1)(n-1)}:
        epsilon^{sharp}(s_r, s_c) = ((mn - s) / s) * ((|B_row| + |B_col|) / Q)
                                  + (mn - 1) * ((L_row(s_r) + L_col(s_c)) / Q).
    """
    if m < 3 or n < 3 or q_val < 2:
        raise ValueError("Require m >= 3, n >= 3, q >= 2")
    s = min(s_r, s_c)
    if s < 1:
        raise ValueError("Require s >= 1")
    mn = m * n
    b_row_rat = q((m - 2) * ((n - 1) * (n - 1) * (q_val - 1) * (q_val - 1) + 2 * q_val - 1), ipow(q_val, n))
    b_col_rat = q((n - 2) * ((m - 1) * (m - 1) * (q_val - 1) * (q_val - 1) + 2 * q_val - 1), ipow(q_val, m))
    b_tot_rat = q_add(b_row_rat, b_col_rat)

    Q_val = ipow(q_val, (m - 1) * (n - 1))
    qn1 = ipow(q_val, n - 1)
    qm1 = ipow(q_val, m - 1)
    rmax_r = min(m, s_r + 1)
    l_row = 0
    for r in range(1, rmax_r + 1):
        l_row += math.comb(m - 1, r - 1) * qn1 * ipow(qn1 - 1, r - 1)
    l_row *= n * ipow(q_val, m)

    rmax_c = min(n, s_c + 1)
    l_col = 0
    for r in range(1, rmax_c + 1):
        l_col += math.comb(n - 1, r - 1) * qm1 * ipow(qm1 - 1, r - 1)
    l_col *= m * ipow(q_val, n)

    low_rat = q(l_row + l_col, Q_val)
    term_a = q_mul(q(mn - s, s), b_tot_rat)
    term_b = q_mul(q(mn - 1, 1), low_rat)
    return q_add(term_a, term_b)


def _seq_runs(seq: list[tuple[int, ...]]) -> int:
    if not seq:
        return 0
    cnt = 1
    for idx in range(1, len(seq)):
        if seq[idx] != seq[idx - 1]:
            cnt += 1
    return cnt


def _is_bad_subarray_lsg_def2(mat: list[tuple[int, ...]]) -> bool:
    """Exact Li-Sun-Ge Definition 2: two adjacent rows or two adjacent columns share a single-deletion output."""
    mr = len(mat)
    nc = len(mat[0])
    # Adjacent rows
    for i in range(mr - 1):
        r1, r2 = mat[i], mat[i + 1]
        d1 = {r1[:k] + r1[k + 1 :] for k in range(nc)}
        d2 = {r2[:k] + r2[k + 1 :] for k in range(nc)}
        if d1 & d2:
            return True
    # Adjacent columns
    cols = [tuple(mat[i][j] for i in range(mr)) for j in range(nc)]
    for j in range(nc - 1):
        c1, c2 = cols[j], cols[j + 1]
        d1 = {c1[:k] + c1[k + 1 :] for k in range(mr)}
        d2 = {c2[:k] + c2[k + 1 :] for k in range(mr)}
        if d1 & d2:
            return True
    return False


def verify_three_tier_inclusion_on_array(grid: list[list[int]], s: int) -> dict[str, Any]:
    """Verify our Ironclad Three-Tier Inclusion on any concrete m x n array X and threshold s."""
    m = len(grid)
    n = len(grid[0])
    ball: set[tuple[tuple[int, ...], ...]] = set()
    bad_in_ball: set[tuple[tuple[int, ...], ...]] = set()
    for r in range(m):
        for c in range(n):
            sub = tuple(tuple(grid[i][j] for j in range(n) if j != c) for i in range(m) if i != r)
            ball.add(sub)
            if _is_bad_subarray_lsg_def2(list(sub)):
                bad_in_ball.add(sub)
    min_row_runs_del_col = min(
        _seq_runs([tuple(grid[i][j] for j in range(n) if j != c) for i in range(m)]) for c in range(n)
    )
    min_col_runs_del_row = min(
        _seq_runs([tuple(grid[i][j] for i in range(m) if i != r) for j in range(n)]) for r in range(m)
    )
    in_c1 = len(ball) == m * n
    in_c2a = (not in_c1) and len(bad_in_ball) >= s
    in_c2b = (not in_c1) and len(bad_in_ball) < s
    in_L_exact = (min_row_runs_del_col <= s + 1) or (min_col_runs_del_row <= s + 1)
    return {
        "m": m,
        "n": n,
        "s": s,
        "ball_size": len(ball),
        "bad_ball_size": len(bad_in_ball),
        "min_row_runs_after_col_del": min_row_runs_del_col,
        "min_col_runs_after_row_del": min_col_runs_del_row,
        "in_C1": in_c1,
        "in_C2a": in_c2a,
        "in_C2b": in_c2b,
        "in_L_exact": in_L_exact,
        "theorem_holds": (not in_c2b) or in_L_exact,
    }


def optimize_sharp_epsilon_square(q_val: int, n: int) -> dict[str, Any]:
    """Find optimal integer tier parameter s in [1, n-2] minimizing sharp_epsilon_rectangular(q, n, n, s, s)."""
    best_eps: Rat | None = None
    best_s = 1
    for s in range(1, max(2, n - 1)):
        eps = sharp_epsilon_rectangular(q_val, n, n, s, s)
        if best_eps is None or q_cmp(eps, best_eps) < 0:
            best_eps = eps
            best_s = s
    assert best_eps is not None
    lsg = lsg_epsilon_square(q_val, n)
    speedup = q_div(lsg, best_eps)
    return {
        "q": q_val,
        "n": n,
        "optimal_s": best_s,
        "our_eps_sharp": q_list(best_eps),
        "our_eps_lt_1": q_cmp(best_eps, (1, 1)) < 0,
        "lsg_eps": q_list(lsg),
        "lsg_eps_lt_1": q_cmp(lsg, (1, 1)) < 0,
        "speedup_ratio_exact": q_list(speedup),
    }


# ---------------------------------------------------------------------------
# Theorem 3: Rectangular Parity-Completion Bijection Delta_{r,c}
# ---------------------------------------------------------------------------


def verify_rectangular_parity_bijection(q_val: int, m: int, n: int) -> dict[str, Any]:
    """
    Verify exact bijection Delta_{r,c}: A_{q,m,n} -> Sigma_q^{(m-1)x(n-1)}
    on zero-row-sum & zero-column-sum rectangular m x n arrays over Z/qZ!
    Tests all (r, c) in [0..m-1] x [0..n-1] on exhaustive or structured subarrays.
    """
    sub_size = (m - 1) * (n - 1)
    total_subs = ipow(q_val, sub_size)
    if total_subs > 512:
        raise ValueError("Keep exhaustive bijection verification <= 512 subarrays")
    subs = list(itertools.product(range(q_val), repeat=sub_size))
    checked_pairs = 0
    for r in range(m):
        for c in range(n):
            reconstructed: set[tuple[int, ...]] = set()
            for flat in subs:
                # Reconstruct unique X in A_{q,m,n} with Delta_{r,c}(X) == flat
                grid = [[0] * n for _ in range(m)]
                ri = 0
                for i in range(m):
                    if i == r:
                        continue
                    cj = 0
                    row_sum = 0
                    for j in range(n):
                        if j == c:
                            continue
                        val = flat[ri * (n - 1) + cj]
                        grid[i][j] = val
                        row_sum += val
                        cj += 1
                    grid[i][c] = (-row_sum) % q_val
                    ri += 1
                for j in range(n):
                    col_sum = sum(grid[i][j] for i in range(m) if i != r)
                    grid[r][j] = (-col_sum) % q_val
                # Check ALL row sums and ALL col sums == 0 mod q!
                for i in range(m):
                    if sum(grid[i]) % q_val != 0:
                        raise AssertionError("Row sum != 0 mod q")
                for j in range(n):
                    if sum(grid[i][j] for i in range(m)) % q_val != 0:
                        raise AssertionError("Col sum != 0 mod q")
                # Check Delta_{r,c}(grid) == flat!
                del_flat = tuple(grid[i][j] for i in range(m) if i != r for j in range(n) if j != c)
                if del_flat != flat:
                    raise AssertionError("Inverse deletion mismatch")
                reconstructed.add(tuple(grid[i][j] for i in range(m) for j in range(n)))
            if len(reconstructed) != total_subs:
                raise AssertionError("Bijection injectivity failed")
            checked_pairs += 1
    return {
        "q": q_val,
        "m": m,
        "n": n,
        "subarray_count": total_subs,
        "positions_checked": checked_pairs,
        "exact_bijection_verified": True,
        "parity_redundancy_symbols": m + n - 1,
    }


# ---------------------------------------------------------------------------
# Theorem 4: Exact Small-Array Optimal Binary (1,1)-Criss-Cross Code Sizes
# ---------------------------------------------------------------------------


def exact_optimal_small_code_capacity(m: int, n: int) -> dict[str, Any]:
    """
    Build the exact binary (1,1)-criss-cross deletion conflict graph on 2^{m*n} arrays
    and find the exact maximum independent set size |C*_{max}(2, m, n)| + witness codewords!
    """
    if m * n > 9:
        raise ValueError("Keep exhaustive conflict graph <= 2^9 = 512 vertices")
    arrs = list(itertools.product([0, 1], repeat=m * n))
    balls: list[frozenset[tuple[int, ...]]] = []
    min_ball = m * n + 1
    max_ball = 0
    for bits in arrs:
        grid = [bits[i * n : (i + 1) * n] for i in range(m)]
        out = set()
        for r in range(m):
            for c in range(n):
                out.add(tuple(grid[i][j] for i in range(m) if i != r for j in range(n) if j != c))
        fs = frozenset(out)
        balls.append(fs)
        if len(fs) < min_ball:
            min_ball = len(fs)
        if len(fs) > max_ball:
            max_ball = len(fs)

    num_v = len(arrs)
    adj = [0] * num_v
    edge_count = 0
    for i in range(num_v):
        bi = balls[i]
        for j in range(i + 1, num_v):
            if bi & balls[j]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
                edge_count += 1

    best_set: list[int] = []

    def bt(cand: int, chosen: list[int]) -> None:
        if len(chosen) + cand.bit_count() <= len(best_set):
            return
        if cand == 0:
            best_set[:] = chosen
            return
        lsb = cand & -cand
        v = lsb.bit_length() - 1
        bt(cand & ~adj[v] & ~lsb, chosen + [v])
        bt(cand & ~lsb, chosen)

    bt((1 << num_v) - 1, [])
    # Independently verify pairwise disjointness of deletion balls of best_set!
    seen_subs: set[tuple[int, ...]] = set()
    for idx in best_set:
        if seen_subs & balls[idx]:
            raise AssertionError("Witness codewords have overlapping deletion balls!")
        seen_subs |= balls[idx]

    return {
        "q": 2,
        "m": m,
        "n": n,
        "total_arrays": num_v,
        "target_subarrays": ipow(2, (m - 1) * (n - 1)),
        "conflict_edges": edge_count,
        "min_ball_size": min_ball,
        "max_ball_size": max_ball,
        "exact_max_code_size": len(best_set),
        "witness_codewords": [list(arrs[idx]) for idx in best_set],
    }
