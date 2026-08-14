#!/usr/bin/env python3
"""Lightweight checks for the semiclassical coherent-orbit RDF theorem.

The examples are Weyl dimension polynomials

    dim V_{k lambda} = product_i (1 + k / a_i),

where a_i=<rho,alpha^vee>/<lambda,alpha^vee> over the active roots.
Only O(log N) Bessel-series terms carry appreciable mass at the contact,
so the checks remain tiny even for very large N.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.special import logsumexp


def log_dimension(k: int, active_root_ratios: tuple[float, ...]) -> float:
    if k == 0:
        return 0.0
    return sum(math.log1p(k / a) for a in active_root_ratios)


def cumulants(kappa: float, N: int, ratios: tuple[float, ...]) -> tuple[float, float, float]:
    """Return K, K', K'' for the exact positive series."""
    # The Bessel weights peak at m=kappa/2 with standard deviation O(sqrt(kappa)).
    # A generous deterministic cutoff is enough at the tested fields.
    mmax = max(80, int(kappa / 2 + 18 * math.sqrt(kappa / 2 + 1) + 30))
    m = np.arange(mmax + 1, dtype=float)
    log_terms = np.zeros(mmax + 1, dtype=float)
    if kappa > 0:
        log_terms[1:] = (
            2 * m[1:] * math.log(kappa / 2)
            - 2 * np.array([math.lgamma(x + 1) for x in m[1:]])
            - np.array([log_dimension(int(x) * N, ratios) for x in m[1:]])
        )
    else:
        log_terms[1:] = -np.inf
    K = float(logsumexp(log_terms))
    weights = np.exp(log_terms - K)
    mean = float(np.dot(weights, m))
    var = float(np.dot(weights, (m - mean) ** 2))
    b = 2 * mean / kappa
    kpp = (4 * var - 2 * mean) / (kappa * kappa)
    return K, b, kpp


def contact(N: int, ratios: tuple[float, ...]) -> dict[str, float]:
    ell = log_dimension(N, ratios)
    p = len(ratios)
    q = p + 0.5
    prediction = 2 * ell + 2 * q * math.log(ell) + math.log(4 * math.pi) - q

    cache: dict[float, tuple[float, float, float]] = {}

    def state(kappa: float) -> tuple[float, float, float]:
        key = float(kappa)
        if key not in cache:
            cache[key] = cumulants(key, N, ratios)
        return cache[key]

    def equation(kappa: float) -> float:
        K, b, _ = state(kappa)
        return kappa * b - 2 * K

    # Search a deliberately wider interval than the asymptotic contact
    # window.  The proof excludes its complement globally; inside this
    # interval we enumerate every stationary crossing and select by the
    # actual chord slope, not by root order.
    low = max(0.5, 0.25 * ell)
    high = max(3 * prediction, prediction + 120)
    grid = np.unique(
        np.concatenate(
            [
                np.geomspace(low, high, 90),
                np.linspace(low, high, 140),
            ]
        )
    )
    values = [equation(float(x)) for x in grid]
    all_brackets = [
        (float(grid[i]), float(grid[i + 1]))
        for i in range(len(grid) - 1)
        if values[i] * values[i + 1] < 0
    ]
    roots: list[dict[str, float | str]] = []
    for bracket in all_brackets:
        root = brentq(equation, *bracket, xtol=2e-12, rtol=2e-14)
        if roots and abs(root - float(roots[-1]["kappa"])) < 1e-8:
            continue
        K_root, b_root, _ = state(root)
        roots.append(
            {
                "kappa": root,
                "slope": (root * b_root - K_root) / (b_root * b_root),
                "kind": "minimum" if equation(root * (1 - 1e-6)) > 0 else "maximum",
            }
        )
    minima = [row for row in roots if row["kind"] == "minimum"]
    if not minima:
        raise RuntimeError(f"no nonzero contact bracket for N={N}")
    selected = min(minima, key=lambda row: float(row["slope"]))
    kappa = float(selected["kappa"])
    K, b, kpp = state(kappa)
    slope = kappa / (2 * b)
    result: dict[str, object] = {
        "N": N,
        "ell": ell,
        "kappa": kappa,
        "kappa_prediction": prediction,
        "kappa_error": kappa - prediction,
        "b": b,
        "D_contact": 1 - b * b,
        "scaled_D_contact": ell * (1 - b * b),
        "q": q,
        "slope": slope,
        "slope_centered": slope - ell - q * math.log(ell),
        "slope_constant": math.log(2 * math.sqrt(math.pi)),
        "contact_identity_error": abs(kappa * b - 2 * K),
        "high_field_convexity_margin": b - kappa * kpp,
        "stationary_roots": roots,
    }
    # A direct grid check guards against choosing a merely local stationary
    # minimum.  Endpoint values are much larger; the grid minimum must be
    # no lower than the selected exact stationary value up to discretization.
    sampled_slopes = []
    for point in grid:
        K_point, b_point, _ = state(float(point))
        if b_point > 1e-14:
            sampled_slopes.append((float(point) * b_point - K_point) / (b_point * b_point))
    result["diagnostic_grid_slope_gap"] = min(sampled_slopes) - slope
    if result["diagnostic_grid_slope_gap"] < -1e-7:
        raise AssertionError("a sampled point beats the selected stationary contact")
    return result  # type: ignore[return-value]


def psi(q: float, x: float) -> float:
    constant = math.log(2 * math.sqrt(math.pi))
    if x <= q:
        return q * math.log(q / x) + constant - q
    return constant - x


def log_expm1(value: float) -> float:
    """Stable log(exp(value)-1) for positive value."""
    if value > 40:
        return value + math.log1p(-math.exp(-value))
    return math.log(math.expm1(value))


def soft_activation(
    N: int, ratios: tuple[float, ...], y: float
) -> dict[str, float]:
    """Check the raw and canonically recentered soft-activation windows."""
    ell = log_dimension(N, ratios)
    p = len(ratios)
    q = p + 0.5
    cp = 2**p / math.sqrt(2 * math.pi)
    theta = cp * math.exp(y) / (1 + cp * math.exp(y))
    raw_kappa = ell + q * math.log(ell) + y
    raw_K, raw_b, _ = cumulants(raw_kappa, N, ratios)

    target_log_s = math.log(cp) + y

    def mass_equation(kappa: float) -> float:
        K, _, _ = cumulants(kappa, N, ratios)
        return log_expm1(K) - target_log_s

    lo, hi = raw_kappa - 4.0, raw_kappa + 4.0
    while mass_equation(lo) > 0:
        lo -= 4
    while mass_equation(hi) < 0:
        hi += 4
    refined_kappa = brentq(mass_equation, lo, hi, xtol=2e-12, rtol=2e-14)
    refined_K, refined_b, _ = cumulants(refined_kappa, N, ratios)
    refined_j = refined_kappa * refined_b - refined_K
    refined_prediction = (
        theta * ell
        + q * theta * math.log(ell)
        + theta * (y - q)
        - math.log1p(cp * math.exp(y))
    )
    return {
        "y": y,
        "C_p": cp,
        "theta": theta,
        "raw_kappa": raw_kappa,
        "raw_S": math.expm1(raw_K),
        "raw_S_limit": cp * math.exp(y),
        "raw_K": raw_K,
        "raw_K_limit": math.log1p(cp * math.exp(y)),
        "raw_b": raw_b,
        "raw_b_limit": theta,
        "refined_kappa": refined_kappa,
        "refined_kappa_offset": refined_kappa - raw_kappa,
        "refined_b": refined_b,
        "refined_j": refined_j,
        "refined_j_prediction": refined_prediction,
        "refined_j_error": refined_j - refined_prediction,
    }


def boundary_point(
    N: int, ratios: tuple[float, ...], contact_row: dict[str, float], x: float
) -> dict[str, float | str]:
    ell = contact_row["ell"]
    q = contact_row["q"]
    D = x / ell
    target_b = math.sqrt(1 - D)
    if D >= contact_row["D_contact"]:
        raw_rate = contact_row["slope"] * (1 - D)
        branch = "coexistence_chord"
    else:
        def saddle(kappa: float) -> float:
            return cumulants(kappa, N, ratios)[1] - target_b

        lo = contact_row["kappa"]
        hi = max(2 * lo, 4 * q / max(1 - target_b, 1e-12))
        while saddle(hi) < 0:
            hi *= 2
        kappa = brentq(saddle, lo, hi, xtol=2e-12, rtol=2e-14)
        K, b, _ = cumulants(kappa, N, ratios)
        raw_rate = kappa * b - K
        branch = "raw_coherent_tilt"
    centered = raw_rate - ell - q * math.log(ell)
    limit = psi(q, x)
    return {
        "x": x,
        "x_over_q": x / q,
        "branch": branch,
        "raw_rate": raw_rate,
        "centered_rate": centered,
        "limit": limit,
        "error": centered - limit,
    }


def main() -> None:
    families = {
        "SU2_SymN": (1.0,),
        "SU3_SymN": (1.0, 2.0),
        "Gr_2_4_rectangular_N": (1.0, 2.0, 2.0, 3.0),
    }
    # Powers far apart make the deliberately slow 1/log(dim) convergence
    # visible without increasing the series length beyond a few hundred terms.
    Ns = (10**4, 10**8, 10**16, 10**32, 10**64)
    report: dict[str, list[dict[str, float]]] = {}
    for name, ratios in families.items():
        rows = [contact(N, ratios) for N in Ns]
        for row in rows:
            q = row["q"]
            row["boundary_layer"] = [
                boundary_point(N=int(row["N"]), ratios=ratios, contact_row=row, x=q * ratio)
                for ratio in (0.4, 0.7, 1.0, 1.4, 2.0)
            ]
            row["soft_activation"] = [
                soft_activation(N=int(row["N"]), ratios=ratios, y=y)
                for y in (-2.0, 0.0, 2.0)
            ]
        report[name] = rows
        # Convergence is logarithmic; demand direction and conservative terminal accuracy.
        assert abs(rows[-1]["kappa_error"]) < abs(rows[0]["kappa_error"])
        assert abs(rows[-1]["scaled_D_contact"] - rows[-1]["q"]) < 0.25
        assert abs(rows[-1]["slope_centered"] - rows[-1]["slope_constant"]) < 0.25
        assert rows[-1]["contact_identity_error"] < 1e-9
        assert min(row["high_field_convexity_margin"] for row in rows) > 0
        assert max(abs(point["error"]) for point in rows[-1]["boundary_layer"]) < 0.3
        assert max(
            abs(point["refined_j_error"]) for point in rows[-1]["soft_activation"]
        ) < 0.22
        assert max(
            abs(point["raw_b"] - point["raw_b_limit"])
            for point in rows[-1]["soft_activation"]
        ) < 0.08

    destination = Path(__file__).with_name("semiclassical_frontier_verification.json")
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: exact Weyl-series contacts approach the universal semiclassical laws")
    for name, rows in report.items():
        last = rows[-1]
        print(
            f"{name}: N={last['N']}, kappa error={last['kappa_error']:.6g}, "
            f"ell*D_c={last['scaled_D_contact']:.6g} (q={last['q']:.6g}), "
            f"centered slope={last['slope_centered']:.6g}"
        )


if __name__ == "__main__":
    main()
