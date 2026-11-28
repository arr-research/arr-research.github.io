"""MATVER-BORDERRANK-CERT-1.0: Zero-Float Exact-Z/Q Verifier for Paper M3-2.

Strict AST hygiene:
  - Zero float literals or float() calls
  - Zero numeric '/' (BinOp Div) or '**' (BinOp Pow) operators
  - Zero Fraction.limit_denominator calls
  - Standard library only (fractions.Fraction, hashlib, json)
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json


def q(n: int, d: int = 1) -> Fraction:
    return Fraction(n, d)


def int_pow(base: int, exp: int) -> int:
    if exp < 0:
        raise ValueError("Exponent must be non-negative")
    res = 1
    b = base
    e = exp
    while e > 0:
        if (e & 1) == 1:
            res = res * b
        b = b * b
        e = e >> 1
    return res


def q_pow(x: Fraction, exp: int) -> Fraction:
    return Fraction(int_pow(x.numerator, exp), int_pow(x.denominator, exp))


def q_div(a: Fraction, b: Fraction) -> Fraction:
    if b == 0:
        raise ZeroDivisionError("Exact rational division by zero")
    return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)


def q_to_pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def strassen_2x2_tensor_cert() -> dict[str, object]:
    """Exact verification of Strassen's 7-product bilinear decomposition of <2, 2, 2> over Z.

    Flattening indices: 0=(0,0), 1=(0,1), 2=(1,0), 3=(1,1) for A, B, C = A*B.
    Target tensor T[i][j][k] = 1 iff C_k contains A_i * B_j.
    """
    # Exact Strassen 7 products:
    # M1 = (a00 + a11)(b00 + b11)
    # M2 = (a10 + a11) b00
    # M3 = a00 (b01 - b11)
    # M4 = a11 (b10 - b00)
    # M5 = (a00 + a01) b11
    # M6 = (a10 - a00)(b00 + b01)
    # M7 = (a01 - a11)(b10 + b11)
    u_mat = [
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [-1, 0, 1, 0],
        [0, 1, 0, -1],
    ]
    v_mat = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, -1],
        [-1, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
    ]
    # c00 = M1 + M4 - M5 + M7
    # c01 = M3 + M5
    # c10 = M2 + M4
    # c11 = M1 - M2 + M3 + M6
    w_mat = [
        [1, 0, 0, 1],
        [0, 0, 1, -1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [-1, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
    ]
    # Build exact <2,2,2> target tensor
    exact_matches = 0
    for i in range(4):
        ai, aj = i // 2, i % 2
        for j in range(4):
            bi, bj = j // 2, j % 2
            for k in range(4):
                ci, cj = k // 2, k % 2
                target = 1 if (ai == ci and aj == bi and bj == cj) else 0
                got = 0
                for r in range(7):
                    got = got + u_mat[r][i] * v_mat[r][j] * w_mat[r][k]
                assert got == target
                exact_matches = exact_matches + 1
    # Exact rational exponent ceiling: 7^100 < 2^281 => log2(7) < 281/100 = 2.81
    lhs = int_pow(7, 100)
    rhs = int_pow(2, 281)
    assert lhs < rhs
    return {
        "tensor": "<2,2,2>",
        "rank_upper_bound": 7,
        "naive_rank": 8,
        "entries_verified": exact_matches,
        "omega_upper_rational": [281, 100],
        "power_cert_7_100_lt_2_281": lhs < rhs,
    }


def strassen_recursive_cost_cert(k_level: int) -> dict[str, object]:
    """Exact multiplication & addition counts for n = 2^k Strassen vs naive."""
    if k_level < 1:
        raise ValueError("Require k_level >= 1")
    n = int_pow(2, k_level)
    strassen_muls = int_pow(7, k_level)
    strassen_adds = 6 * (strassen_muls - int_pow(4, k_level))
    strassen_total = strassen_muls + strassen_adds
    naive_muls = int_pow(8, k_level)
    naive_adds = n * n * (n - 1)
    naive_total = naive_muls + naive_adds
    return {
        "k_level": k_level,
        "n": n,
        "strassen_muls": strassen_muls,
        "strassen_adds": strassen_adds,
        "strassen_total_ops": strassen_total,
        "naive_muls": naive_muls,
        "naive_adds": naive_adds,
        "naive_total_ops": naive_total,
        "strictly_fewer_muls": strassen_muls < naive_muls,
    }


def dual_number_border_rank_cert() -> dict[str, object]:
    """Exact Z[eps] border-rank-2 witness for dual-number multiplication T_dual(a,b) = (a1*b1, a1*b2 + a2*b1).

    Exact tensor rank R(T_dual) = 3, whereas border rank R_border(T_dual) = 2:
      M1(eps) = (a1 + eps*a2) * (b1 + eps*b2)
      M2(eps) = a1 * b1
      eps * c1 = eps * M2(eps)                   => eps^1: a1*b1,       eps^0=0, eps^2=0
      eps * c2 = M1(eps) - M2(eps)               => eps^1: a1*b2+a2*b1, eps^0=0, eps^2=a2*b2
    """
    # Represent polynomial in (ai, bj, eps_deg) -> int
    # Basis: a0=a1, a1=a2; b0=b1, b1=b2
    def mul_lin(a_terms: list[tuple[int, int, int]], b_terms: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
        out: dict[tuple[int, int, int], int] = {}
        for ai, ae, ac in a_terms:
            for bi, be, bc in b_terms:
                key = (ai, bi, ae + be)
                out[key] = out.get(key, 0) + ac * bc
        return {k: v for k, v in out.items() if v != 0}

    m1 = mul_lin([(0, 0, 1), (1, 1, 1)], [(0, 0, 1), (1, 1, 1)])
    m2 = mul_lin([(0, 0, 1)], [(0, 0, 1)])
    # c1_scaled = eps * m2
    c1_scaled = {(ai, bi, d + 1): v for (ai, bi, d), v in m2.items()}
    # c2_scaled = m1 - m2
    c2_scaled: dict[tuple[int, int, int], int] = dict(m1)
    for k, v in m2.items():
        c2_scaled[k] = c2_scaled.get(k, 0) - v
    c2_scaled = {k: v for k, v in c2_scaled.items() if v != 0}

    # Check eps^0 vanishes, eps^1 matches exact target, eps^2 is pure residual
    c1_e0 = {k: v for k, v in c1_scaled.items() if k[2] == 0}
    c1_e1 = {(k[0], k[1]): v for k, v in c1_scaled.items() if k[2] == 1}
    c2_e0 = {k: v for k, v in c2_scaled.items() if k[2] == 0}
    c2_e1 = {(k[0], k[1]): v for k, v in c2_scaled.items() if k[2] == 1}
    c2_e2 = {(k[0], k[1]): v for k, v in c2_scaled.items() if k[2] == 2}

    assert c1_e0 == {} and c2_e0 == {}
    assert c1_e1 == {(0, 0): 1}
    assert c2_e1 == {(0, 1): 1, (1, 0): 1}
    assert c2_e2 == {(1, 1): 1}
    return {
        "tensor": "T_dual = R[x]/(x^2)",
        "exact_rank": 3,
        "border_rank": 2,
        "strict_gap": 1,
        "eps0_vanishes_identically": True,
        "eps1_exact_recovery": True,
        "eps2_residual_monomials": 1,
    }


def schonhage_border_rank_cert(m: int, n: int) -> dict[str, object]:
    """Exact Z[eps] border-rank witness for Schonhage (1981) direct-sum tensor:
      T_{m,n} = <m, 1, n> (+) <1, (m-1)*(n-1), 1>
    has exact border rank <= m*n + 1 (vs trivial direct-sum rank m*n + (m-1)*(n-1))!

    Explicit rank-(m*n+1) family over Z[eps] recovering eps^2 * T_{m,n} + O(eps^3):
      M_{i,j} = (u_i + eps*x_{i,j}) * (v_j + eps*y_{i,j})       for 0 <= i < m-1, 0 <= j < n-1
      R_i     = u_i * (v_{n-1} - eps * sum_{j=0..n-2} y_{i,j})  for 0 <= i < m-1
      C_j     = (u_{m-1} - eps * sum_{i=0..m-2} x_{i,j}) * v_j  for 0 <= j < n-1
      P_last  = u_{m-1} * v_{n-1}
      P_tot   = (sum_{i=0..m-1} u_i) * (sum_{j=0..n-1} v_j)
    Outputs:
      c_{i,j} (0<=i<m, 0<=j<n): eps^2 * corresponding product = eps^2 * u_i*v_j + O(eps^3)
      S_inner: sum(M) + sum(R) + sum(C) + P_last - P_tot = eps^2 * sum_{i,j} x_{i,j}*y_{i,j} (EXACT, zero O(eps^3)!)
    """
    if m < 2 or n < 2:
        raise ValueError("Require m >= 2 and n >= 2")

    def poly_mul(p1: dict[tuple[str, int], int], p2: dict[tuple[str, int], int]) -> dict[tuple[str, str, int], int]:
        out: dict[tuple[str, str, int], int] = {}
        for (v1, e1), c1 in p1.items():
            for (v2, e2), c2 in p2.items():
                key = (v1, v2, e1 + e2)
                out[key] = out.get(key, 0) + c1 * c2
        return {k: v for k, v in out.items() if v != 0}

    prods: list[tuple[int, dict[tuple[str, str, int], int]]] = []
    # Check outer-product eps^0 terms match u_i * v_j identically
    outer_verified = 0
    for i in range(m - 1):
        for j in range(n - 1):
            p = poly_mul({(f"u{i}", 0): 1, (f"x{i}_{j}", 1): 1}, {(f"v{j}", 0): 1, (f"y{i}_{j}", 1): 1})
            e0 = {(a, b): c for (a, b, d), c in p.items() if d == 0}
            assert e0 == {(f"u{i}", f"v{j}"): 1}
            outer_verified = outer_verified + 1
            prods.append((1, p))
    for i in range(m - 1):
        vpart: dict[tuple[str, int], int] = {(f"v{n-1}", 0): 1}
        for j in range(n - 1):
            vpart[(f"y{i}_{j}", 1)] = -1
        p = poly_mul({(f"u{i}", 0): 1}, vpart)
        e0 = {(a, b): c for (a, b, d), c in p.items() if d == 0}
        assert e0 == {(f"u{i}", f"v{n-1}"): 1}
        outer_verified = outer_verified + 1
        prods.append((1, p))
    for j in range(n - 1):
        upart: dict[tuple[str, int], int] = {(f"u{m-1}", 0): 1}
        for i in range(m - 1):
            upart[(f"x{i}_{j}", 1)] = -1
        p = poly_mul(upart, {(f"v{j}", 0): 1})
        e0 = {(a, b): c for (a, b, d), c in p.items() if d == 0}
        assert e0 == {(f"u{m-1}", f"v{j}"): 1}
        outer_verified = outer_verified + 1
        prods.append((1, p))
    p_last = poly_mul({(f"u{m-1}", 0): 1}, {(f"v{n-1}", 0): 1})
    assert p_last == {(f"u{m-1}", f"v{n-1}", 0): 1}
    outer_verified = outer_verified + 1
    prods.append((1, p_last))
    p_tot = poly_mul({(f"u{i}", 0): 1 for i in range(m)}, {(f"v{j}", 0): 1 for j in range(n)})
    prods.append((-1, p_tot))

    s_sum: dict[tuple[str, str, int], int] = {}
    for sign, poly in prods:
        for k, v in poly.items():
            s_sum[k] = s_sum.get(k, 0) + sign * v
    s_sum = {k: v for k, v in s_sum.items() if v != 0}
    expected_s = {(f"x{i}_{j}", f"y{i}_{j}", 2): 1 for i in range(m - 1) for j in range(n - 1)}
    assert s_sum == expected_s
    assert outer_verified == m * n

    inner_len = (m - 1) * (n - 1)
    border_rank_ub = m * n + 1
    direct_sum_trivial = m * n + inner_len
    return {
        "m": m,
        "n": n,
        "tensor": f"<{m},1,{n}> (+) <1,{inner_len},1>",
        "outer_outputs_verified": outer_verified,
        "inner_product_len": inner_len,
        "border_rank_upper_bound": border_rank_ub,
        "trivial_direct_sum_rank": direct_sum_trivial,
        "rank_savings": direct_sum_trivial - border_rank_ub,
        "inner_product_exact_at_eps2": True,
    }


def schonhage_tau_exponent_cert(
    vol1: int, vol2: int, border_r: int, tau_num: int, tau_den: int, lb1: Fraction, lb2: Fraction
) -> dict[str, object]:
    """Exact zero-float certificate for Schonhage's asymptotic sum inequality:
      vol1^tau + vol2^tau = border_r  =>  omega <= 3 * tau.
    If lb1 < vol1^(tau_num/tau_den)  (checked via lb1^tau_den < vol1^tau_num)
    and lb2 < vol2^(tau_num/tau_den) (checked via lb2^tau_den < vol2^tau_num)
    and lb1 + lb2 > border_r, then since f(tau) is strictly increasing,
    the unique root tau_0 satisfies tau_0 < tau_num/tau_den, certifying omega < 3*tau_num/tau_den!
    """
    if vol1 <= 1 or vol2 <= 1 or border_r <= 2 or tau_num <= 0 or tau_den <= 0:
        raise ValueError("Invalid tau-theorem parameters")
    c1 = q_pow(lb1, tau_den) < Fraction(int_pow(vol1, tau_num), 1)
    c2 = q_pow(lb2, tau_den) < Fraction(int_pow(vol2, tau_num), 1)
    c3 = (lb1 + lb2) > Fraction(border_r, 1)
    omega_ub = Fraction(3 * tau_num, tau_den)
    return {
        "vol1": vol1,
        "vol2": vol2,
        "border_r": border_r,
        "tau_bound": q_to_pair(Fraction(tau_num, tau_den)),
        "omega_upper_bound": q_to_pair(omega_ub),
        "lb1": q_to_pair(lb1),
        "lb2": q_to_pair(lb2),
        "lb_sum": q_to_pair(lb1 + lb2),
        "cert_lb1_valid": c1,
        "cert_lb2_valid": c2,
        "cert_sum_exceeds_r": c3,
        "certified_omega_lt_bound": c1 and c2 and c3,
    }


def verification_to_border_rank_cert(
    n: int, cost_s: int, tree_const_c: int, claimed_border_lb: int
) -> dict[str, object]:
    """Exact algebraic check of Chen (arXiv:2611.34814v1) decision-tree reduction:
      R_border(T_n) <= tree_const_c * cost_s  =>  cost_s >= ceil(R_border(T_n) / tree_const_c).
    """
    if n < 1 or cost_s < 1 or tree_const_c < 1 or claimed_border_lb < 1:
        raise ValueError("All parameters must be positive integers")
    feasible = tree_const_c * cost_s >= claimed_border_lb
    min_cost = (claimed_border_lb + tree_const_c - 1) // tree_const_c
    return {
        "n": n,
        "cost_s": cost_s,
        "tree_const_c": tree_const_c,
        "border_rank_lb": claimed_border_lb,
        "min_required_cost": min_cost,
        "cost_feasible": feasible,
    }


def conditional_9_over_4_separation_cert(k_quartic: int, freivalds_trials: int) -> dict[str, object]:
    """Exact integer separation at n = 2^(4*k) under the conditional hypothesis omega_C = 9/4
    (explicitly cited as an unrefereed conditional assumption from Chen arXiv:2611.34814v1
    referencing the Nov 24 2026 OpenAI preprint):
      n = 2^(4k)  =>  n^(9/4) = 2^(9k),  n^2 = 2^(8k),  ratio n^(9/4) / n^2 = 2^k (exact integer!).
    Compares against Freivalds k_trials * (6*n^2 - 2*n) arithmetic ops.
    """
    if k_quartic < 1 or freivalds_trials < 1:
        raise ValueError("Require k_quartic >= 1 and freivalds_trials >= 1")
    n = int_pow(2, 4 * k_quartic)
    n_9_4 = int_pow(2, 9 * k_quartic)
    n_sq = int_pow(2, 8 * k_quartic)
    assert n_sq == n * n
    ratio = int_pow(2, k_quartic)
    assert n_9_4 == n_sq * ratio
    freivalds_ops = freivalds_trials * (6 * n_sq - 2 * n)
    freivalds_err_den = int_pow(2, freivalds_trials)
    return {
        "k_quartic": k_quartic,
        "n": n,
        "n_sq": n_sq,
        "n_9_4_exact": n_9_4,
        "asymptotic_gap_ratio_n_1_4": ratio,
        "freivalds_trials": freivalds_trials,
        "freivalds_exact_ops": freivalds_ops,
        "freivalds_f2_error_bound": [1, freivalds_err_den],
        "conditional_on_omega_C_eq_9_4": True,
    }


def linear_probe_kernel_barrier_cert(probe_matrix: list[list[Fraction]]) -> dict[str, object]:
    """Constructive exact-Q Gaussian elimination barrier for deterministic linear probes.

    Given R in Q^(n x r) with r < n, finds an exact nonzero vector v in Q^n such that
    v^T * R = 0 (equivalently R^T * v = 0), and builds rank-1 adversarial error E = e_0 * v^T != 0
    satisfying E * R = 0 identically!
    """
    n = len(probe_matrix)
    if n < 2:
        raise ValueError("Require n >= 2")
    r = len(probe_matrix[0])
    if r >= n:
        raise ValueError("Require r < n for guaranteed nontrivial kernel")
    for row in probe_matrix:
        if len(row) != r:
            raise ValueError("Ragged probe matrix")

    # Build A = R^T (r x n) and reduce to RREF over Q
    mat = [[probe_matrix[col][row] for col in range(n)] for row in range(r)]
    pivots: list[int] = []
    cur_row = 0
    for col in range(n):
        if cur_row >= r:
            break
        piv = -1
        for i in range(cur_row, r):
            if mat[i][col] != 0:
                piv = i
                break
        if piv == -1:
            continue
        mat[cur_row], mat[piv] = mat[piv], mat[cur_row]
        pv = mat[cur_row][col]
        mat[cur_row] = [q_div(x, pv) for x in mat[cur_row]]
        for i in range(r):
            if i != cur_row and mat[i][col] != 0:
                factor = mat[i][col]
                mat[i] = [mat[i][j] - factor * mat[cur_row][j] for j in range(n)]
        pivots.append(col)
        cur_row = cur_row + 1

    pivot_set = set(pivots)
    free_cols = [c for c in range(n) if c not in pivot_set]
    assert len(free_cols) >= n - r >= 1
    free_c = free_cols[0]
    v = [Fraction(0, 1) for _ in range(n)]
    v[free_c] = Fraction(1, 1)
    for row_idx, pcol in enumerate(pivots):
        v[pcol] = -mat[row_idx][free_c]

    # Verify v != 0 and v^T * R == 0 exactly
    assert any(x != 0 for x in v)
    for j in range(r):
        dot = Fraction(0, 1)
        for i in range(n):
            dot = dot + v[i] * probe_matrix[i][j]
        assert dot == 0

    return {
        "n": n,
        "r_probes": r,
        "rank_R": len(pivots),
        "kernel_dim_lower_bound": n - r,
        "witness_v": [q_to_pair(x) for x in v],
        "adversarial_E_nonzero": True,
        "adversarial_ER_zero_exact": True,
    }


def freivalds_schwartz_zippel_cert(k_trials: int, domain_size: int) -> dict[str, object]:
    """Exact rational false-positive ceiling (1/|S|)^k for k independent Freivalds probes
    drawn uniformly from finite set S subset Q (|S| >= 2).
    """
    if k_trials < 1 or domain_size < 2:
        raise ValueError("Require k_trials >= 1 and domain_size >= 2")
    err_den = int_pow(domain_size, k_trials)
    return {
        "k_trials": k_trials,
        "domain_size": domain_size,
        "error_bound_exact": [1, err_den],
        "strictly_below_1e_minus_9": err_den > 1000000000,
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
