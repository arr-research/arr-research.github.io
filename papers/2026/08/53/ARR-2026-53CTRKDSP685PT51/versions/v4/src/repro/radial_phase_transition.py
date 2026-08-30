"""Deterministic quadrature for the exact spherical three-phase theorem.

The diagnostic uses d=3, h=sigma', and isotropic Gamma radii
R=s_a Q, Q~Gamma(a,1), s_a=sqrt(d/[a(a+1)]).  In d=3 the angular
kernel is J(q)=q^{-3} int_{-q}^q s^2 h(s) ds, reducing beta to one
adaptive integral.  No simulation is used.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid, quad
from scipy.interpolate import PchipInterpolator
from scipy.special import beta as beta_function
from scipy.special import exp1, gamma, gammaincc


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "radial_phase_transition.pdf"
CERTIFICATE = ROOT / "repro" / "radial_phase_transition.json"
D = 3
C_D = 0.5
M2 = math.pi**2 / 3.0


def logistic_prime(x: np.ndarray | float) -> np.ndarray | float:
    x_arr = np.asarray(x)
    z = np.exp(-np.abs(x_arr))
    value = z / (1.0 + z) ** 2
    return value if isinstance(x, np.ndarray) else float(value)


def build_truncated_moment() -> PchipInterpolator:
    grid = np.linspace(0.0, 40.0, 200_001)
    density = 2.0 * grid**2 * logistic_prime(grid)
    cumulative = np.concatenate(([0.0], cumulative_trapezoid(density, grid)))
    if abs(cumulative[-1] / M2 - 1.0) > 2e-10:
        raise AssertionError((cumulative[-1], M2))
    return PchipInterpolator(grid, cumulative, extrapolate=False)


TRUNCATED_M2 = build_truncated_moment()


def m2_truncated(q: float) -> float:
    if q <= 0.0:
        return 0.0
    if q >= 40.0:
        return M2
    return float(TRUNCATED_M2(q))


def absolute_profile_moment(power: float) -> float:
    value, error = quad(
        lambda s: 2.0 * s**power * logistic_prime(s),
        0.0,
        40.0,
        epsabs=2e-12,
        epsrel=2e-12,
        limit=300,
    )
    if error > 2e-10:
        raise AssertionError((power, value, error))
    return value


def exact_beta(r: float, a: float) -> float:
    scale = math.sqrt(D / (a * (a + 1.0)))
    c = 1.0 / (gamma(a) * scale**a)
    cutoff = r * scale

    def integrand(q: float) -> float:
        if q == 0.0:
            return 0.0
        return q ** (a - 2.0) * math.exp(-q / cutoff) * m2_truncated(q)

    pieces = ((0.0, 1.0), (1.0, 10.0), (10.0, 40.0))
    integral = 0.0
    error = 0.0
    for left, right in pieces:
        value, err = quad(integrand, left, right, epsabs=2e-10, epsrel=3e-10, limit=500)
        integral += value
        error += err
    # Above q=40 the omitted logistic second-moment tail is below 2e-14,
    # so M2(q) can be replaced by its exact full value.  Closed or compactified
    # tails avoid loss of accuracy when the Gamma cutoff r*scale is very large.
    if a < 1.0:
        tail, tail_error = quad(
            lambda u: u ** (-a) * math.exp(-1.0 / (u * cutoff)) if u > 0.0 else 0.0,
            0.0,
            1.0 / 40.0,
            epsabs=2e-11,
            epsrel=2e-11,
            limit=500,
        )
        error += tail_error * M2
    elif a == 1.0:
        tail = float(exp1(40.0 / cutoff))
    else:
        tail = cutoff ** (a - 1.0) * gamma(a - 1.0) * gammaincc(a - 1.0, 40.0 / cutoff)
    integral += M2 * tail
    beta_value = C_D * c * r ** (-(a + 2.0)) * integral
    if not beta_value > 0.0 or error > max(2e-7 * integral, 2e-10):
        raise AssertionError((r, a, beta_value, integral, error))
    return beta_value


def asymptotic_constant(a: float) -> tuple[str, float]:
    scale = math.sqrt(D / (a * (a + 1.0)))
    c = 1.0 / (gamma(a) * scale**a)
    if a < 1.0:
        moment = absolute_profile_moment(a + 1.0)
        constant = 0.5 * C_D * c * beta_function((1.0 - a) / 2.0, (D - 1.0) / 2.0) * moment
        return "subcritical", constant
    if a == 1.0:
        return "critical", C_D * c * M2
    er_inverse = 1.0 / (scale * (a - 1.0))
    return "integrable", C_D * er_inverse * M2


def normalized_ratio(r: float, a: float, beta_value: float, phase: str, constant: float) -> float:
    if phase == "subcritical":
        return beta_value * r ** (a + 2.0) / constant
    if phase == "critical":
        return beta_value * r**3 / (constant * math.log(r))
    return beta_value * r**3 / constant


def main() -> None:
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    radii = np.geomspace(10.0, 100_000.0, 17)
    colors = {0.5: "#1f77b4", 1.0: "#d95f02", 2.0: "#2ca02c"}
    records: list[dict[str, object]] = []

    fig, ax = plt.subplots(figsize=(7.4, 4.45), constrained_layout=True)
    for a in (0.5, 1.0, 2.0):
        phase, constant = asymptotic_constant(a)
        ratios = []
        betas = []
        for r in radii:
            beta_value = exact_beta(float(r), a)
            ratio = normalized_ratio(float(r), a, beta_value, phase, constant)
            betas.append(beta_value)
            ratios.append(ratio)
        if not all(0.0 < value < 1.02 for value in ratios):
            raise AssertionError((a, ratios))
        ax.plot(radii, ratios, marker="o", markersize=3.3, linewidth=1.7,
                color=colors[a], label=rf"$a={a:g}$ ({phase})")
        records.append({
            "a": a,
            "phase": phase,
            "leading_constant": constant,
            "radii": [float(x) for x in radii],
            "beta": betas,
            "normalized_ratio": ratios,
        })

    ax.axhline(1.0, color="#333333", linewidth=1.0, linestyle="--", label="asymptotic limit")
    ax.set_xscale("log")
    ax.set_ylim(0.42, 1.025)
    ax.set_xlabel(r"teacher norm $r$")
    ax.set_ylabel(r"$\beta(r)$ divided by its exact leading law")
    ax.set_title(r"Three inverse-radius phases ($d=3$, $h=\sigma'$)")
    ax.grid(True, which="both", alpha=0.18)
    ax.legend(frameon=False, ncol=2, fontsize=8.5)
    fig.savefig(
        FIGURE,
        metadata={
            "Creator": "ARR deterministic radial-phase replay",
            "CreationDate": datetime(2026, 8, 30, tzinfo=timezone.utc),
        },
    )
    plt.close(fig)

    payload = {
        "schema": "arr.radial-phase-transition.v1",
        "dimension": D,
        "profile": "logistic derivative",
        "radius_family": "sqrt(d/[a(a+1)]) * Gamma(a,1)",
        "m2": M2,
        "records": records,
    }
    CERTIFICATE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: exact constants and deterministic quadrature for a=1/2,1,2")
    print(f"figure_sha256={hashlib.sha256(FIGURE.read_bytes()).hexdigest()}")
    print(f"certificate_sha256={hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()}")
    for record in records:
        print(record["a"], record["phase"], record["leading_constant"], record["normalized_ratio"][-1])


if __name__ == "__main__":
    main()
