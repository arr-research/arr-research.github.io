"""Bounded exact replay for the coherent-orbit RDF derivation.

This script checks finite representation identities and scalar diagnostics.
It is not a proof of the Cartan-product theorem, Fenchel attainment, or the
uniform saddle estimate.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gammaln, hyp0f1


def rising(a: int, m: int) -> int:
    out = 1
    for j in range(m):
        out *= a + j
    return out


def dim_rect(n: int, k: int, m: int) -> int:
    """Weyl dimension of the SU(n) representation m*omega_k."""
    out = Fraction(1)
    for i in range(1, k + 1):
        out *= Fraction(rising(n - k + i, m), rising(i, m))
    assert out.denominator == 1
    return out.numerator


def d2_hook(n: int, k: int) -> Fraction:
    N = math.comb(n, k)
    return Fraction(N * N * (n + 1), (k + 1) * (n - k + 1))


def even_moment_y(n: int, k: int, m: int) -> Fraction:
    # E[Re <v,X>]^(2m) after uniform phase averaging.
    return Fraction(math.comb(2 * m, m), 4**m * dim_rect(n, k, m))


def cumulants_4_6(n: int, k: int) -> tuple[Fraction, Fraction]:
    mu2 = even_moment_y(n, k, 1)
    mu4 = even_moment_y(n, k, 2)
    mu6 = even_moment_y(n, k, 3)
    kap4 = mu4 - 3 * mu2**2
    kap6 = mu6 - 15 * mu4 * mu2 + 30 * mu2**3
    return kap4, kap6


def log_dim_rect(n: int, k: int, m: int) -> float:
    return sum(
        gammaln(n - k + i + m)
        - gammaln(n - k + i)
        - gammaln(i + m)
        + gammaln(i)
        for i in range(1, k + 1)
    )


def L_series(n: int, k: int, kap: float, tol: float = 2e-15) -> float:
    z = kap * kap / 4.0
    term = 1.0
    total = 1.0
    for m in range(1, 10000):
        # term_m / term_{m-1}
        ratio = z / (m * m)
        for i in range(1, k + 1):
            ratio *= (i + m - 1) / (n - k + i + m - 1)
        term *= ratio
        total += term
        if term < tol * total and m > kap:
            return total
    raise RuntimeError("series failed to converge")


def active_radius(n: int, k: int, s: float) -> tuple[float, float]:
    def objective(b: float) -> float:
        return -(math.log(L_series(n, k, 2.0 * s * b)) - s * b * b)

    grid = np.linspace(0.0, 1.0, 301)
    vals = np.array([-objective(float(b)) for b in grid])
    j = int(np.argmax(vals))
    lo = float(grid[max(0, j - 2)])
    hi = float(grid[min(len(grid) - 1, j + 2)])
    res = minimize_scalar(objective, bounds=(lo, hi), method="bounded")
    b = float(res.x)
    candidates = [(0.0, 0.0), (b, -float(res.fun))]
    return max(candidates, key=lambda pair: pair[1])


def main() -> None:
    checked = 0
    complement_checks = 0
    transition_table = []

    for n in range(2, 15):
        for k in range(1, n):
            for m in range(0, 8):
                d = dim_rect(n, k, m)
                dc = dim_rect(n, n - k, m)
                assert d == dc
                checked += 1
                complement_checks += 1
            assert Fraction(dim_rect(n, k, 2), 1) == d2_hook(n, k)

    for n in range(3, 13):
        for k in range(1, n // 2 + 1):
            kap4, kap6 = cumulants_4_6(n, k)
            expected = "negative" if k == 1 or (n, k) == (4, 2) else (
                "zero" if (n, k) == (5, 2) else "positive"
            )
            actual = "positive" if kap4 > 0 else "negative" if kap4 < 0 else "zero"
            assert actual == expected, (n, k, kap4, expected)
            transition_table.append(
                {
                    "n": n,
                    "k": k,
                    "N": math.comb(n, k),
                    "d2": dim_rect(n, k, 2),
                    "kappa4": str(kap4),
                    "kappa6": str(kap6),
                    "quartic_sign": actual,
                }
            )

    # The k=1 series must be the complex-sphere Bessel normalizer 0F1(;n;k^2/4).
    sphere_errors = []
    for n in (2, 3, 5, 9):
        for kap in (0.2, 1.0, 4.0, 10.0):
            lhs = L_series(n, 1, kap)
            rhs = float(hyp0f1(n, kap * kap / 4.0))
            sphere_errors.append(abs(lhs - rhs) / rhs)
    assert max(sphere_errors) < 2e-13

    # Check the exact high-field constant numerically for representative Slater families.
    asymptotic = []
    for n, k in ((5, 2), (6, 2), (6, 3), (8, 3)):
        p = k * (n - k)
        log_A = sum(gammaln(n - k + i) - gammaln(i) for i in range(1, k + 1))
        log_C = log_A + p * math.log(2.0) - 0.5 * math.log(2.0 * math.pi)
        for kap in (40.0, 80.0):
            log_ratio = math.log(L_series(n, k, kap)) - (
                kap - (p + 0.5) * math.log(kap) + log_C
            )
            asymptotic.append({"n": n, "k": k, "kappa": kap, "log_ratio": log_ratio})
        assert abs(asymptotic[-1]["log_ratio"]) < abs(asymptotic[-2]["log_ratio"])

    # Dual diagnostics: interior families n>=6 should activate before s0=N.
    activation = []
    for n, k in ((6, 2), (6, 3), (7, 2), (8, 3)):
        s0 = float(math.comb(n, k))
        b, value = active_radius(n, k, s0)
        assert b > 1e-3 and value > 1e-10
        activation.append({"n": n, "k": k, "s0": s0, "active_b_at_s0": b, "gain": value})

    output = {
        "status": "PASS",
        "scope": "finite exact identities and scalar diagnostics; not a proof of the general theorem",
        "dimension_checks": checked,
        "complement_checks": complement_checks,
        "max_k1_hypergeometric_relative_error": max(sphere_errors),
        "transition_table": transition_table,
        "high_field_diagnostics": asymptotic,
        "activation_diagnostics": activation,
    }
    out = Path(__file__).with_name("coherent_orbit_rdf_verification.json")
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
