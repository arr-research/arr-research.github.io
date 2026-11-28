"""PAULI-AC0-BQAC0-CERT-1.0: Zero-Float Exact-Q Verifier for Paper M3-3.

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


def q_inv(a: Fraction) -> Fraction:
    return q_div(Fraction(1, 1), a)


def q_abs(a: Fraction) -> Fraction:
    return -a if a < 0 else a


def q_to_pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def q_decimal_str(x: Fraction, digits: int = 6) -> str:
    sign = "-" if x < 0 else ""
    ax = q_abs(x)
    scale = int_pow(10, digits)
    scaled = (ax.numerator * scale) // ax.denominator
    int_part = scaled // scale
    frac_part = scaled % scale
    return f"{sign}{int_part}.{str(frac_part).zfill(digits)}"


def binom(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    kk = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, kk + 1):
        num = num * (n - kk + i)
        den = den * i
    return num // den


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative factorial")
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


def pauli_weight_distribution_cert(n: int, max_deg: int) -> dict[str, object]:
    """Exact n-qubit Pauli weight distribution N_k = C(n, k) * 3^k and degree-d subspace count."""
    if n < 1 or max_deg < 0 or max_deg > n:
        raise ValueError("Require n >= 1 and 0 <= max_deg <= n")
    counts = [binom(n, k) * int_pow(3, k) for k in range(n + 1)]
    total = sum(counts)
    assert total == int_pow(4, n)
    low_deg_count = sum(counts[: max_deg + 1])
    high_deg_count = total - low_deg_count
    frac_low = Fraction(low_deg_count, total)
    return {
        "n_qubits": n,
        "max_deg": max_deg,
        "total_paulis_4_n": total,
        "low_deg_count": low_deg_count,
        "high_deg_count": high_deg_count,
        "low_deg_fraction": q_to_pair(frac_low),
        "low_deg_fraction_dec": q_decimal_str(frac_low, 6),
        "weight_counts": counts if n <= 10 else counts[: max_deg + 1],
    }


def symplectic_inner_mod2(x1: int, z1: int, x2: int, z2: int, n: int) -> int:
    """Exact symplectic inner product <P1, P2>_sp = sum_i (x1_i*z2_i + z1_i*x2_i) mod 2."""
    acc = 0
    for i in range(n):
        a = ((x1 >> i) & 1) * ((z2 >> i) & 1)
        b = ((z1 >> i) & 1) * ((x2 >> i) & 1)
        acc = acc + a + b
    return acc & 1


def pauli_z_twirling_projection_cert(n: int, coeffs: list[Fraction]) -> dict[str, object]:
    """Exact Z-group Pauli twirling T_Z(O) = (1/2^n) sum_{z in {0,1}^n} Z^z O Z^z on n qubits.

    Index Pauli P_{x,z} by idx = (x << n) | z in [0, 4^n).
    Z-group commutes with P_{x,z} iff x == 0 (purely diagonal I/Z Pauli strings!).
    Verifies Parseval Frobenius contraction ||T_Z(O)||_F^2 <= ||O)||_F^2 and exact elimination of all x != 0.
    """
    if n < 1 or n > 4:
        raise ValueError("Require 1 <= n <= 4 for exhaustive 4^n Pauli table")
    n_paulis = int_pow(4, n)
    if len(coeffs) != n_paulis:
        raise ValueError("Coefficient vector must have length 4^n")
    two_n = int_pow(2, n)
    frob_sq_before = Fraction(0, 1)
    frob_sq_after = Fraction(0, 1)
    surviving = 0
    eliminated = 0
    for idx in range(n_paulis):
        x = idx >> n
        z = idx & (two_n - 1)
        c = coeffs[idx]
        frob_sq_before = frob_sq_before + c * c
        # Exact average over all Z^s (x2=0, z2=s)
        twirl_factor = 0
        for s in range(two_n):
            sp = symplectic_inner_mod2(x, z, 0, s, n)
            twirl_factor = twirl_factor + (1 if sp == 0 else -1)
        if x == 0:
            assert twirl_factor == two_n
            surviving = surviving + 1
            frob_sq_after = frob_sq_after + c * c
        else:
            assert twirl_factor == 0
            eliminated = eliminated + 1
    assert surviving == two_n and eliminated == n_paulis - two_n
    assert frob_sq_after <= frob_sq_before
    return {
        "n_qubits": n,
        "total_paulis": n_paulis,
        "surviving_diagonal_paulis": surviving,
        "eliminated_offdiag_paulis": eliminated,
        "normalized_frob_sq_before": q_to_pair(frob_sq_before),
        "normalized_frob_sq_after": q_to_pair(frob_sq_after),
        "strict_contraction": frob_sq_after < frob_sq_before,
        "nonexpansive": frob_sq_after <= frob_sq_before,
    }


def monotone_cnf_fourier_spectrum_cert(m_clauses: int, w_width: int, deg_cutoff: int) -> dict[str, object]:
    """Exact Boolean Fourier / diagonal-Pauli weight spectrum of the P-uniform linear-size
    monotone depth-2 CNF f_{m,w}(x) = AND_{j=1..m} OR_{i=1..w} x_{j,i} on n = m*w qubits.

    Exact closed-form Fourier weight at degree k:
      W_k = sum_{r=0..m} C(m, r) * (1 - 2^-w)^(2*(m-r)) * 2^(-2*w*r) * N(r, w, k)
    where N(r, w, k) = [t^k] ((1+t)^w - 1)^r!
    Verifies Parseval: sum_{k=0..n} W_k == p = (1 - 2^-w)^m (since f_{m,w} is {0,1}-valued, f^2 = f)!
    Computes exact L2 approximation error sum_{k > deg_cutoff} W_k and variance fraction lost!
    """
    if m_clauses < 1 or w_width < 1:
        raise ValueError("Require m_clauses >= 1 and w_width >= 1")
    n = m_clauses * w_width
    if deg_cutoff < 0 or deg_cutoff > n:
        raise ValueError("Require 0 <= deg_cutoff <= m*w")

    # Build polynomial P_1(t) = (1+t)^w - 1 (degree w, coeff of t^0 is 0)
    p1 = [0] + [binom(w_width, j) for j in range(1, w_width + 1)]

    def poly_mul_int(a: list[int], b: list[int]) -> list[int]:
        out = [0] * (len(a) + len(b) - 1)
        for i, va in enumerate(a):
            if va == 0:
                continue
            for j, vb in enumerate(b):
                if vb == 0:
                    continue
                out[i + j] = out[i + j] + va * vb
        return out

    # Powers P_1(t)^r for r = 0..m
    powers: list[list[int]] = [[1]]
    for _ in range(m_clauses):
        powers.append(poly_mul_int(powers[-1], p1))

    two_w = int_pow(2, w_width)
    p_clause = Fraction(two_w - 1, two_w)
    q_clause = Fraction(1, two_w)
    p_clause_sq = p_clause * p_clause
    q_clause_sq = q_clause * q_clause

    # Accumulate exact Fourier weights W_0 .. W_n
    weights = [Fraction(0, 1) for _ in range(n + 1)]
    for r in range(m_clauses + 1):
        pref = Fraction(binom(m_clauses, r), 1) * q_pow(p_clause_sq, m_clauses - r) * q_pow(q_clause_sq, r)
        poly = powers[r]
        for k, cnt in enumerate(poly):
            if cnt != 0:
                weights[k] = weights[k] + pref * cnt

    acc_prob = q_pow(p_clause, m_clauses)
    total_w = sum(weights, Fraction(0, 1))
    assert total_w == acc_prob  # Exact Parseval for {0,1}-valued function: E[f^2] = E[f] = p!
    variance = acc_prob * (Fraction(1, 1) - acc_prob)
    assert total_w - weights[0] == variance

    low_weight = sum(weights[: deg_cutoff + 1], Fraction(0, 1))
    tail_error_l2_sq = sum(weights[deg_cutoff + 1 :], Fraction(0, 1))
    assert low_weight + tail_error_l2_sq == acc_prob
    # Exact operator-norm lower bound on any degree-d Hermitian approximator A_d:
    # Since ||A_d - f||_op >= ||A_d - f||_F / 2^(n/2) >= sqrt(tail_error_l2_sq),
    # we certify the exact squared operator-norm lower bound: ||A_d - f||_op^2 >= tail_error_l2_sq!
    var_tail_ratio = q_div(tail_error_l2_sq, variance) if variance > 0 else Fraction(0, 1)
    return {
        "m_clauses": m_clauses,
        "w_width": w_width,
        "n_qubits": n,
        "deg_cutoff": deg_cutoff,
        "acceptance_prob_exact": q_to_pair(acc_prob),
        "acceptance_prob_dec": q_decimal_str(acc_prob, 6),
        "variance_exact": q_to_pair(variance),
        "variance_dec": q_decimal_str(variance, 6),
        "parseval_exact_match": total_w == acc_prob,
        "tail_l2_sq_error_exact": q_to_pair(tail_error_l2_sq),
        "tail_l2_sq_error_dec": q_decimal_str(tail_error_l2_sq, 6),
        "tail_fraction_of_variance": q_to_pair(var_tail_ratio),
        "tail_fraction_of_variance_dec": q_decimal_str(var_tail_ratio, 6),
    }


def stretched_exp_decay_cert(
    m_param: int, alpha_num: int, alpha_den: int, m_alpha_exact: int, taylor_k: int, multiplier: int = 1
) -> dict[str, object]:
    """Zero-float exact-Q upper bound on multiplier * exp(-m^(alpha_num/alpha_den))
    when m^(alpha_num) == m_alpha_exact^(alpha_den) (so x = m^alpha is an exact positive integer!).

    Since exp(x) > sum_{j=0..K} x^j / j! for all x > 0, we have the strict certified bound:
      multiplier * exp(-x) < multiplier / (sum_{j=0..K} x^j / j!).
    """
    if m_param < 1 or alpha_num < 1 or alpha_den < 1 or m_alpha_exact < 1 or taylor_k < 1 or multiplier < 1:
        raise ValueError("Invalid stretched-exponential parameters")
    if int_pow(m_param, alpha_num) != int_pow(m_alpha_exact, alpha_den):
        raise ValueError("Exact integer power condition m^alpha_num == x^alpha_den failed")
    exp_lb = Fraction(0, 1)
    for j in range(taylor_k + 1):
        exp_lb = exp_lb + Fraction(int_pow(m_alpha_exact, j), factorial(j))
    upper_bound = q_div(Fraction(multiplier, 1), exp_lb)
    return {
        "m_param": m_param,
        "alpha": [alpha_num, alpha_den],
        "x_exact": m_alpha_exact,
        "taylor_order_K": taylor_k,
        "multiplier": multiplier,
        "exp_x_lower_bound": q_to_pair(exp_lb),
        "decay_upper_bound_exact": q_to_pair(upper_bound),
        "decay_upper_bound_dec": q_decimal_str(upper_bound, 10),
        "below_1e_minus_5": upper_bound < Fraction(1, 100000),
        "below_1e_minus_9": upper_bound < Fraction(1, 1000000000),
    }


def pauli_advantage_ceiling_cert(
    eps_approx: Fraction, advice_indep_adv: Fraction
) -> dict[str, object]:
    """Exact worst-case advantage ceiling from operator-norm Pauli approximation (arXiv:2611.34803v1):
    If ||M_circuit - H_deg||_op <= eps_approx and H_deg achieves advantage <= advice_indep_adv,
    then the circuit's worst-case advantage is at most advice_indep_adv + 2 * eps_approx!
    """
    if eps_approx < 0 or advice_indep_adv < 0:
        raise ValueError("Error and advantage bounds must be non-negative")
    total_adv = advice_indep_adv + 2 * eps_approx
    return {
        "eps_approx": q_to_pair(eps_approx),
        "advice_indep_adv": q_to_pair(advice_indep_adv),
        "total_advantage_ceiling": q_to_pair(total_adv),
        "total_advantage_dec": q_decimal_str(total_adv, 6),
        "strictly_below_half": total_adv < Fraction(1, 2),
    }


def canonical_json_sha256(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
