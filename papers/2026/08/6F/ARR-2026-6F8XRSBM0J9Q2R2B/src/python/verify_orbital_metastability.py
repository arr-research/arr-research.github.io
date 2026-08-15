"""Lightweight exact replay for the orbital-stability manuscript.

The moment identities use exact symbolic arithmetic.  The final Bessel-mode
screen is diagnostic floating-point evaluation and is not used as proof.
"""

from __future__ import annotations

import json
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp


def partitions(total: int, max_len: int, cap: int | None = None):
    if total == 0:
        yield ()
        return
    if max_len == 0:
        return
    cap = total if cap is None else min(cap, total)
    for first in range(cap, 0, -1):
        for tail in partitions(total - first, max_len - 1, first):
            yield (first,) + tail


def tableau_dimension(lam: tuple[int, ...]) -> sp.Expr:
    hooks = sp.Integer(1)
    for i, row in enumerate(lam):
        for j in range(row):
            below = sum(1 for lower in lam[i + 1 :] if lower > j)
            hooks *= row - j + below
    return sp.factorial(sum(lam)) / hooks


def schur_at_ones(lam: tuple[int, ...], k: sp.Symbol) -> sp.Expr:
    out = sp.Integer(1)
    for i, row in enumerate(lam):
        for j in range(row):
            below = sum(1 for lower in lam[i + 1 :] if lower > j)
            hook = row - j + below
            out *= (k + j - i) / hook
    return sp.factor(out)


def generalized_pochhammer(a: sp.Expr, lam: tuple[int, ...]) -> sp.Expr:
    out = sp.Integer(1)
    for i, row in enumerate(lam):
        out *= sp.rf(a - i, row)
    return sp.factor(out)


def raw_trace_moment(order: int, r: sp.Symbol, k: sp.Symbol) -> sp.Expr:
    if order == 0:
        return sp.Integer(1)
    value = sp.Integer(0)
    for lam in partitions(order, order):
        value += (
            tableau_dimension(lam)
            * schur_at_ones(lam, k)
            * generalized_pochhammer(r, lam)
            / generalized_pochhammer(2 * r, lam)
        )
    return sp.factor(value)


def centered_moment(order: int, r: sp.Symbol, k: sp.Symbol) -> sp.Expr:
    raw = [raw_trace_moment(j, r, k) for j in range(order + 1)]
    return sp.factor(
        sum(
            sp.binomial(order, j)
            * (-k / sp.Integer(2)) ** (order - j)
            * raw[j]
            for j in range(order + 1)
        )
    )


def exact_checks() -> dict[str, str | int]:
    r, k, j = sp.symbols("r k j", integer=True, positive=True)
    n = 2 * r
    m = n - k

    mu2 = centered_moment(2, r, k)
    mu4 = centered_moment(4, r, k)
    mu6 = centered_moment(6, r, k)

    expected_mu2 = k * m / (4 * (n**2 - 1))
    expected_mu4 = 3 * k * m * (k * m - 2) / (
        16 * (n - 3) * (n - 1) * (n + 1) * (n + 3)
    )
    assert sp.factor(mu2 - expected_mu2) == 0
    assert sp.factor(mu4 - expected_mu4) == 0

    a_plus = n * (n * k - 1) / m
    a_minus = n * (n * m - 1) / k
    h2_plus = sp.factor(
        (mu4 * (1 + a_plus / 3) - (k**2 / 4) * mu2) / 2
    )
    h2_minus = sp.factor(
        (mu4 * (1 + a_minus / 3) - (m**2 / 4) * mu2) / 2
    )
    expected_h2_plus = k * (4 * r - 3 * k) * (k**2 - 1) / (
        16 * (2 * r - 3) * (2 * r - 1) * (2 * r + 1) * (2 * r + 3)
    )
    expected_h2_minus = -(2 * r - 3 * k) * m * (m**2 - 1) / (
        16 * (2 * r - 3) * (2 * r - 1) * (2 * r + 1) * (2 * r + 3)
    )
    assert sp.factor(h2_plus - expected_h2_plus) == 0
    assert sp.factor(h2_minus - expected_h2_minus) == 0

    k_edge = 2 * r / 3
    m_edge = 4 * r / 3
    mu4_edge = sp.factor(mu4.subs(k, k_edge))
    mu6_edge = sp.factor(mu6.subs(k, k_edge))
    expected_mu6_edge = 10 * r**2 * (4 * r**4 - 27 * r**2 + 9) / (
        243
        * (2 * r - 5)
        * (2 * r - 1) ** 2
        * (2 * r + 1) ** 2
        * (2 * r + 5)
    )
    assert sp.factor(mu6_edge - expected_mu6_edge) == 0
    a_minus_edge = sp.factor(a_minus.subs(k, k_edge))
    h4_edge = sp.factor(
        (mu6_edge * (1 + a_minus_edge / 5) - (m_edge**2 / 4) * mu4_edge)
        / 24
    )
    expected_h4_edge = -4 * r**2 * (4 * r - 3) * (4 * r + 3) / (
        5832
        * (2 * r - 5)
        * (2 * r - 1) ** 2
        * (2 * r + 1) ** 2
        * (2 * r + 5)
    )
    assert sp.factor(h4_edge - expected_h4_edge) == 0

    stein_bound = (k**2 / 4) * (2 * j + 1) / (2 * j + 1 + 2 * r * k)
    target = (m**2 / 4) * (2 * j + 1) / (
        2 * j + 1 + n * (n * m - 1) / k
    )
    numerator = sp.factor(sp.together(target - stein_bound)).as_numer_denom()[0]
    expected_tail_factor = sp.factor(2 * j * (m - k) - m * (k**2 - 1))
    assert sp.factor(numerator / expected_tail_factor) > 0

    dims = {
        "real": sp.expand(r * (2 * r + 1) - 1),
        "complex": sp.expand(4 * r**2 - 1),
        "quaternionic": sp.expand(8 * r**2 - 2 * r - 1),
    }
    for rv in range(2, 12):
        for kv in range(1, rv):
            if kv > 1:
                assert expected_h2_plus.subs({r: rv, k: kv}) > 0
            sign = sp.sign(expected_h2_minus.subs({r: rv, k: kv}))
            assert sign == -sp.sign(2 * rv - 3 * kv)

    return {
        "symbolic_mu2": "PASS",
        "symbolic_mu4": "PASS",
        "symbolic_mu6_boundary": "PASS",
        "symbolic_h2_plus_minus": "PASS",
        "symbolic_h4_boundary": "PASS",
        "symbolic_tail_equivalence": "PASS",
        "integer_sign_cases": sum(rv - 1 for rv in range(2, 12)),
        "ambient_dimensions": {name: str(expr) for name, expr in dims.items()},
    }


def bessel_screen() -> dict[str, float | int | str]:
    mp.mp.dps = 50
    minimum = mp.inf
    cases = 0
    for ambient_dimension in (9, 15, 27, 35, 63):
        nu = mp.mpf(ambient_dimension - 2) / 2
        rho = mp.mpf("1.3")
        for ell in (1, 2, 4, 7):
            for t in (mp.mpf("0.1"), mp.mpf("0.7"), mp.mpf("3.0")):
                a = t ** (-nu) * mp.besseli(ell + nu, rho * t)
                mode = ell * (ell + ambient_dimension - 2) * a / t**2
                minimum = min(minimum, mode)
                assert mode > 0
                cases += 1
    return {
        "status": "PASS",
        "cases": cases,
        "minimum_positive_mode": float(minimum),
    }


def criticality_counterexample() -> dict[str, float | str]:
    """Check the torus-orbit guard added to the repaired universal theorem."""
    mp.mp.dps = 50
    t = mp.mpf(1)
    a = mp.sqrt(mp.mpf(3) / 4)
    b = mp.mpf(1) / 2
    derivative = t * a * b * (
        mp.besseli(1, t * b**2) / mp.besseli(0, t * b**2)
        - mp.besseli(1, t * a**2) / mp.besseli(0, t * a**2)
    )
    assert derivative < 0
    assert abs(derivative) > mp.mpf("0.09")
    return {
        "status": "PASS",
        "log_potential_derivative_at_t_1": float(derivative),
    }


def main() -> None:
    payload = {
        "exact": exact_checks(),
        "diagnostic_bessel": bessel_screen(),
        "criticality_counterexample": criticality_counterexample(),
        "scope": "Exact algebra, an explicit criticality-counterexample check, and a bounded diagnostic Bessel positivity screen; no numerical global optimizer claim.",
    }
    output = Path(__file__).with_name("orbital_metastability_verification.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
