"""AST-pure zero-float exact-Q/Z verifier for M7-1:
Sharpened Discrete Min-Cut Recurrence, Generalized s-Rank Palette-Order Flexibility,
Universal All-d 4-Request Mutual-Exclusion Gadgets, and Sharp Forest Flexibility
for d-Degenerate Graphs (strictly advancing Adak et al., arXiv:2611.34348v1).
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import hashlib
import json
from typing import Any


def int_pow(base: int, exp: int) -> int:
    """Exact non-negative integer power without using ast.Pow."""
    if exp < 0:
        raise ValueError("exp must be non-negative")
    res = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res *= b
        b *= b
        e >>= 1
    return res


def frac_pow(base: Fraction, exp: int) -> Fraction:
    """Exact rational power without using ast.Pow."""
    if exp < 0:
        raise ValueError("exp must be non-negative")
    return Fraction(int_pow(base.numerator, exp), int_pow(base.denominator, exp))


def canonical_json_sha256(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def exact_inv_e_bracket(terms: int = 24) -> tuple[Fraction, Fraction]:
    """Return exact rational interval (lo, hi) strictly bracketing 1/e via alternating series."""
    if terms < 6 or terms % 2 != 0:
        raise ValueError("terms must be an even integer >= 6")
    s = Fraction(0, 1)
    fact = 1
    for n in range(terms):
        if n > 0:
            fact *= n
        term = Fraction(1, fact)
        if n % 2 == 0:
            s += term
        else:
            s -= term
    # For even N = terms, partial sum up to N-1 (odd) is < 1/e, and adding 1/N! is > 1/e.
    lo = s
    hi = s + Fraction(1, fact * terms)
    return (lo, hi)


def adak_thm3_list_size(d: int) -> int:
    """Exact floor((d + 2) * (2 - 1/e)) verified via rigorous rational bracketing."""
    if d < 1:
        raise ValueError("d must be >= 1")
    lo_inv_e, hi_inv_e = exact_inv_e_bracket(24)
    val_lo = (d + 2) * (Fraction(2, 1) - hi_inv_e)
    val_hi = (d + 2) * (Fraction(2, 1) - lo_inv_e)
    f_lo = val_lo.numerator // val_lo.denominator
    f_hi = val_hi.numerator // val_hi.denominator
    if f_lo != f_hi:
        raise RuntimeError(f"Bracket precision insufficient at d={d}")
    return f_lo


def adak_baseline_list_size(d: int) -> int:
    """Minimum of Adak et al. Theorem 2 (2d) and Theorem 3 (floor((d+2)(2-1/e)))."""
    if d < 1:
        raise ValueError("d must be >= 1")
    t2 = 2 * d
    t3 = adak_thm3_list_size(d)
    return t2 if t2 < t3 else t3


def sharp_min_cut_holds(d: int, k: int, M: int) -> bool:
    """Exact integer verification of Theorem 1 sharpened discrete min-cut criterion.

    Checks:
      1. Base feasibility: k >= d + M (which also implies M * d <= (d + 1) * (k - 1)).
      2. For every S in {1, ..., d}:
         let ell = max(0, d + S + M - k);
         ((d + 2) * M - 1) * (M^ell - (M - 1)^ell) <= S * M^(ell + 1).
    """
    if d < 1 or M < 2 or k < d + M:
        return False
    if M * d > (d + 1) * (k - 1):
        return False
    for S in range(1, d + 1):
        ell = d + S + M - k
        if ell <= 0:
            continue
        lhs = ((d + 2) * M - 1) * (int_pow(M, ell) - int_pow(M - 1, ell))
        rhs = S * int_pow(M, ell + 1)
        if lhs > rhs:
            return False
    return True


def exact_discrete_min_k(d: int, m_max: int = 80) -> dict[str, Any]:
    """Find minimum list size k and smallest witness M >= 2 achieving weighted (k, 1/(d+1))-flexibility."""
    if d < 1:
        raise ValueError("d must be >= 1")
    if d == 1:
        return {
            "d": 1,
            "min_k": 2,
            "witness_M": None,
            "method": "forest_double_optimum_thm4",
            "adak_thm2": 2,
            "adak_thm3": adak_thm3_list_size(1),
            "adak_best": 2,
            "gain_over_adak_best": 0,
        }
    for k in range(d + 1, 2 * d + 1):
        upper_m = m_max if m_max < k else k
        for M in range(2, upper_m + 1):
            if sharp_min_cut_holds(d, k, M):
                t2 = 2 * d
                t3 = adak_thm3_list_size(d)
                best = t2 if t2 < t3 else t3
                return {
                    "d": d,
                    "min_k": k,
                    "witness_M": M,
                    "method": "sharpened_discrete_min_cut_thm1",
                    "adak_thm2": t2,
                    "adak_thm3": t3,
                    "adak_best": best,
                    "gain_over_adak_best": best - k,
                }
    t2 = 2 * d
    t3 = adak_thm3_list_size(d)
    best = t2 if t2 < t3 else t3
    return {
        "d": d,
        "min_k": t2,
        "witness_M": None,
        "method": "fallback_2d",
        "adak_thm2": t2,
        "adak_thm3": t3,
        "adak_best": best,
        "gain_over_adak_best": best - t2,
    }


def verify_pade_log_bound(M: int, series_terms: int = 40) -> dict[str, Any]:
    """Certify exact rational inequality: -ln(1 - 1/M) < 1 / (M - 1/2 - 1/(6M)) for M >= 2.

    Uses exact Taylor tail upper bound:
      -ln(1 - 1/M) = sum_{n=1}^N 1/(n M^n) + R_N,
      with R_N < 1 / ((N+1) * M^(N+1) * (1 - 1/M)) = 1 / ((N+1) * M^N * (M - 1)).
    """
    if M < 2:
        raise ValueError("M must be >= 2")
    partial = Fraction(0, 1)
    m_pow = 1
    for n in range(1, series_terms + 1):
        m_pow *= M
        partial += Fraction(1, n * m_pow)
    tail_upper = Fraction(1, (series_terms + 1) * m_pow * (M - 1))
    neg_log_upper = partial + tail_upper
    pade_rhs = Fraction(6 * M, 6 * M * M - 3 * M - 1)
    adak_rhs = Fraction(1, M - 1)
    return {
        "M": M,
        "neg_log_upper_str": f"{neg_log_upper.numerator}/{neg_log_upper.denominator}",
        "pade_rhs_str": f"{pade_rhs.numerator}/{pade_rhs.denominator}",
        "adak_rhs_str": f"{adak_rhs.numerator}/{adak_rhs.denominator}",
        "pade_strictly_holds": neg_log_upper < pade_rhs,
        "pade_strictly_tighter_than_adak": pade_rhs < adak_rhs,
    }


def sweep_discrete_gains(d_min: int = 1, d_max: int = 100) -> dict[str, Any]:
    """Compute exact Theorem 1 vs Adak et al. Theorems 2 & 3 comparison across [d_min, d_max]."""
    if d_min < 1 or d_max < d_min:
        raise ValueError("invalid d range")
    rows = []
    strict_gain_ds = []
    sub_2d_ds = []
    for d in range(d_min, d_max + 1):
        row = exact_discrete_min_k(d)
        rows.append(row)
        if row["gain_over_adak_best"] > 0:
            strict_gain_ds.append(d)
        if row["min_k"] < 2 * d:
            sub_2d_ds.append(d)
    first_sub_2d = sub_2d_ds[0] if sub_2d_ds else None
    gains_from_8 = [d for d in strict_gain_ds if d >= 8]
    total_from_8 = max(0, d_max - max(8, d_min) + 1) if d_max >= 8 else 0
    return {
        "d_min": d_min,
        "d_max": d_max,
        "first_sub_2d_d": first_sub_2d,
        "adak_first_sub_2d_d": 9,
        "strict_gain_count": len(strict_gain_ds),
        "strict_gain_count_from_8": len(gains_from_8),
        "total_d_from_8": total_from_8,
        "first_twenty_strict_gain_ds": strict_gain_ds[:20],
        "rows_summary_first_30": rows[:30],
    }


def s_rank_flexibility_bound(d: int, s: int, chi_hr: int | None = None) -> dict[str, Any]:
    """Compute exact Theorem 2 weighted flexibility ratio s / (chi(H_r) * (1 + d*(d+s))) for d >= 1."""
    if d < 1 or s < 1:
        raise ValueError("require d >= 1 and s >= 1")
    chi_val = (d + 1) if chi_hr is None else chi_hr
    if chi_val < 1 or chi_val > d + 1:
        raise ValueError("chi(H_r) must satisfy 1 <= chi_hr <= d + 1")
    union_size = 1 + d * (d + s)
    eps = Fraction(s, chi_val * union_size)
    adak_t1 = Fraction(1, (d + 1) * (d * d + d + 1))
    kaul_exp = Fraction(1, int_pow(2, d + 1))
    gain_vs_adak = Fraction(eps.numerator * adak_t1.denominator, eps.denominator * adak_t1.numerator)
    return {
        "d": d,
        "s": s,
        "k": d + 1 + s,
        "chi_Hr": chi_val,
        "union_size_bound": union_size,
        "epsilon_num": eps.numerator,
        "epsilon_den": eps.denominator,
        "adak_thm1_num": adak_t1.numerator,
        "adak_thm1_den": adak_t1.denominator,
        "kaul_exp_den": kaul_exp.denominator,
        "strictly_beats_adak_thm1": eps > adak_t1,
        "at_least_adak_thm1": eps >= adak_t1,
        "ratio_vs_adak_num": gain_vs_adak.numerator,
        "ratio_vs_adak_den": gain_vs_adak.denominator,
    }


def build_universal_Gd(d: int) -> dict[str, Any]:
    r"""Construct our universal (2d + 3)-vertex d-degenerate 4-request mutual-exclusion family G_d (Theorem 3).

    Vertex indexing (2d + 3 vertices):
      0         : v_1
      1..d      : A = {a_1, ..., a_d}
      d+1       : v_4
      d+2..2d+1 : B = {b_1, ..., b_d}
      2d+2      : v_7
    Palette of size d + 2: {0:'a', 1:'b', 2:'c', 3:'d_col', 4..d+1: E (size d - 2)}.
    Lists of size d + 1:
      L(v_1)       = palette \ {3}
      L(a_i), L(v_7) = palette \ {2}
      L(v_4), L(b_j) = palette \ {1}
    Requests (4 vertices):
      r(v_1) = 0, r(v_4) = 3, r(b_d) = 0, r(v_7) = 3.
    """
    if d < 2:
        raise ValueError("d must be >= 2")
    n = 2 * d + 3
    v1 = 0
    A = list(range(1, d + 1))
    v4 = d + 1
    B = list(range(d + 2, 2 * d + 2))
    bd = 2 * d + 1
    v7 = 2 * d + 2

    adj: list[set[int]] = [set() for _ in range(n)]

    def add_edge(u: int, v: int) -> None:
        if u == v:
            raise ValueError("self-loop")
        adj[u].add(v)
        adj[v].add(u)

    # K_d on A and K_d on B
    for i in range(d):
        for j in range(i + 1, d):
            add_edge(A[i], A[j])
            add_edge(B[i], B[j])
    # v1 adjacent to all A and all B
    for a in A:
        add_edge(v1, a)
    for b in B:
        add_edge(v1, b)
    # v4 adjacent to all A and to B \ {b_d}
    for a in A:
        add_edge(v4, a)
    for b in B[:-1]:
        add_edge(v4, b)
    # v7 adjacent to all B
    for b in B:
        add_edge(v7, b)

    # Verify d-degeneracy in canonical ordering 0, 1, ..., n-1
    back_degrees = []
    for u in range(n):
        bd_u = sum(1 for v in adj[u] if v < u)
        back_degrees.append(bd_u)
    max_back_deg = max(back_degrees)
    is_d_degenerate = max_back_deg <= d

    palette = list(range(d + 2))
    lists: list[list[int]] = []
    for u in range(n):
        if u == v1:
            lists.append([c for c in palette if c != 3])
        elif u in A or u == v7:
            lists.append([c for c in palette if c != 2])
        else:
            lists.append([c for c in palette if c != 1])

    requests = {v1: 0, v4: 3, bd: 0, v7: 3}
    for u, rc in requests.items():
        if rc not in lists[u]:
            raise RuntimeError("request not in list")

    edge_list = sorted((u, v) for u in range(n) for v in adj[u] if u < v)
    return {
        "d": d,
        "num_vertices": n,
        "num_edges": len(edge_list),
        "list_size": d + 1,
        "palette_size": d + 2,
        "max_back_degree": max_back_deg,
        "is_d_degenerate": is_d_degenerate,
        "request_vertices": sorted(requests.keys()),
        "requests": requests,
        "lists": lists,
        "edges": edge_list,
    }


def exhaustively_verify_Gd_max_sat(d: int) -> dict[str, Any]:
    """Exhaustively prove by exact backtracking that G_d satisfies at most 1 of its 4 requests."""
    if d < 2 or d > 4:
        raise ValueError("exhaustive backtracking supported for d in {2, 3, 4}")
    g = build_universal_Gd(d)
    n = g["num_vertices"]
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in g["edges"]:
        adj[u].append(v)
        adj[v].append(u)
    lists = g["lists"]
    requests = g["requests"]
    req_verts = list(requests.keys())

    # Check all 6 pairs of requests simultaneously cannot be extended to any proper L-coloring
    pair_results = []
    for idx_i in range(len(req_verts)):
        for idx_j in range(idx_i + 1, len(req_verts)):
            u0 = req_verts[idx_i]
            u1 = req_verts[idx_j]
            col: list[int] = [-1] * n
            col[u0] = requests[u0]
            col[u1] = requests[u1]
            # Check direct conflict
            conflict = u1 in adj[u0] and col[u0] == col[u1]
            nodes_visited = 0
            found = False

            if not conflict:
                def dfs() -> bool:
                    nonlocal nodes_visited
                    nodes_visited += 1
                    best_v = -1
                    best_opts: list[int] = []
                    for v in range(n):
                        if col[v] != -1:
                            continue
                        forb = {col[w] for w in adj[v] if col[w] != -1}
                        opts = [c for c in lists[v] if c not in forb]
                        if not opts:
                            return False
                        if best_v == -1 or len(opts) < len(best_opts):
                            best_v = v
                            best_opts = opts
                            if len(best_opts) == 1:
                                break
                    if best_v == -1:
                        return True
                    for c in best_opts:
                        col[best_v] = c
                        if dfs():
                            return True
                        col[best_v] = -1
                    return False

                found = dfs()
            pair_results.append({
                "pair": [u0, u1],
                "extendable": found,
                "nodes_visited": nodes_visited,
            })

    # Also verify 1 request IS extendable (so G_d is (d+1)-list-colorable and max_sat == 1 exactly!)
    single_witness: list[int] | None = None
    col1: list[int] = [-1] * n
    col1[req_verts[0]] = requests[req_verts[0]]

    def dfs_one() -> bool:
        best_v = -1
        best_opts: list[int] = []
        for v in range(n):
            if col1[v] != -1:
                continue
            forb = {col1[w] for w in adj[v] if col1[w] != -1}
            opts = [c for c in lists[v] if c not in forb]
            if not opts:
                return False
            if best_v == -1 or len(opts) < len(best_opts):
                best_v = v
                best_opts = opts
        if best_v == -1:
            return True
        for c in best_opts:
            col1[best_v] = c
            if dfs_one():
                return True
            col1[best_v] = -1
        return False

    if dfs_one():
        single_witness = list(col1)

    all_pairs_unsat = all(not pr["extendable"] for pr in pair_results)
    return {
        "d": d,
        "num_vertices": n,
        "num_edges": g["num_edges"],
        "is_d_degenerate": g["is_d_degenerate"],
        "list_size": d + 1,
        "num_requests": 4,
        "all_6_pairs_unsat": all_pairs_unsat,
        "max_satisfiable_requests": 1 if (all_pairs_unsat and single_witness is not None) else -1,
        "max_ratio_str": "1/4",
        "refutes_d_plus_1_1_over_d_plus_1": (d == 2 and all_pairs_unsat),
        "single_request_coloring_witness": single_witness,
        "pair_checks": pair_results,
    }


def solve_forest_weighted_2_half_flexible(
    n: int,
    edges: list[tuple[int, int]],
    lists: list[list[int]],
    requests: dict[int, int],
    weights: dict[int, int],
) -> dict[str, Any]:
    """Constructively build two proper L-colorings (C1, C2) of a forest with 2-lists
    such that every vertex v has r(v) in {C1(v), C2(v)}, guaranteeing max(W(C1), W(C2)) >= ceil(W_tot / 2)
    (Theorem 4, sharp forest double-optimum).
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if len(lists) != n:
        raise ValueError("lists length mismatch")
    for v in range(n):
        if len(lists[v]) != 2 or lists[v][0] == lists[v][1]:
            raise ValueError("every vertex must have a 2-list of distinct colors")
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        if u == v or u < 0 or v < 0 or u >= n or v >= n:
            raise ValueError("invalid edge")
        adj[u].append(v)
        adj[v].append(u)

    # Verify forest (acyclic) and build BFS parent order
    visited = [False] * n
    c1 = [-1] * n
    c2 = [-1] * n
    for root in range(n):
        if visited[root]:
            continue
        q: deque[tuple[int, int]] = deque([(root, -1)])
        visited[root] = True
        while q:
            u, parent = q.popleft()
            a, b = lists[u][0], lists[u][1]
            if parent == -1:
                c1[u], c2[u] = a, b
            else:
                p1, p2 = c1[parent], c2[parent]
                if a != p1 and b != p2:
                    c1[u], c2[u] = a, b
                else:
                    c1[u], c2[u] = b, a
            for w in adj[u]:
                if w == parent:
                    continue
                if visited[w]:
                    raise ValueError("input graph contains a cycle (not a forest)")
                visited[w] = True
                q.append((w, u))

    # Verify both colorings are proper L-colorings
    for u in range(n):
        if c1[u] not in lists[u] or c2[u] not in lists[u] or c1[u] == c2[u]:
            raise RuntimeError("list/distinctness invariant failed")
    for u, v in edges:
        if c1[u] == c1[v] or c2[u] == c2[v]:
            raise RuntimeError("proper coloring invariant failed")

    total_w = 0
    w1 = 0
    w2 = 0
    for v, rc in requests.items():
        wv = weights.get(v, 1)
        if wv < 0:
            raise ValueError("weights must be non-negative")
        total_w += wv
        if c1[v] == rc:
            w1 += wv
        if c2[v] == rc:
            w2 += wv

    best_w = w1 if w1 >= w2 else w2
    return {
        "n": n,
        "num_edges": len(edges),
        "total_weight": total_w,
        "w_C1": w1,
        "w_C2": w2,
        "best_weight": best_w,
        "meets_half_bound": 2 * best_w >= total_w,
        "C1": c1,
        "C2": c2,
    }
