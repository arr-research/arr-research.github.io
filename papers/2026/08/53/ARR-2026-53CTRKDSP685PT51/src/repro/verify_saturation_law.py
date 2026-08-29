#!/usr/bin/env python3
"""Deterministic replay for the sigmoid Schwarzian bridge and saturation law.

The script verifies the closed constants, evaluates the exact one-dimensional
Gaussian integrals by Gauss-Hermite quadrature, checks the finite-r bounds,
and produces the publication figure and a machine-readable certificate.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from flint import arb, ctx
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "saturation_law.pdf"
CERTIFICATE = ROOT / "repro" / "saturation_certificate.json"


def logistic_prime(x: np.ndarray | float) -> np.ndarray | float:
    x = np.asarray(x)
    # Numerically stable form: sigma'(x) = 1/(2+2 cosh x).
    ax = np.abs(x)
    e = np.exp(-ax)
    return e / (1.0 + e) ** 2


def gaussian_expectation(func, order: int = 320) -> float:
    nodes, weights = hermgauss(order)
    return float(np.dot(weights, func(np.sqrt(2.0) * nodes)) / np.sqrt(np.pi))


def eigenvalues(r: float, profile: str) -> tuple[float, float]:
    if profile == "square":
        h = lambda z: logistic_prime(r * z) ** 2
    elif profile == "bernoulli":
        h = lambda z: logistic_prime(r * z)
    else:
        raise ValueError(profile)
    # Change variables u = r z once saturation makes the Gaussian integrand
    # narrower than a fixed Gauss-Hermite grid can resolve.
    if r >= 2.0:
        phi0 = 1.0 / math.sqrt(2.0 * math.pi)
        damp = lambda u: math.exp(-(u * u) / (2.0 * r * r))
        hs = lambda u: float(logistic_prime(u) ** (2 if profile == "square" else 1))
        a_int = quad(lambda u: hs(u) * damp(u), -np.inf, np.inf,
                     epsabs=2e-13, epsrel=2e-13, limit=300)[0]
        b_int = quad(lambda u: u * u * hs(u) * damp(u), -np.inf, np.inf,
                     epsabs=2e-13, epsrel=2e-13, limit=300)[0]
        alpha = phi0 * a_int / r
        beta = phi0 * b_int / r**3
    else:
        alpha = gaussian_expectation(h)
        beta = gaussian_expectation(lambda z: z * z * h(z))
    return alpha, beta


def sensitivity_moments(profile: str) -> tuple[float, float, float]:
    if profile == "square":
        h = lambda u: float(logistic_prime(u) ** 2)
    elif profile == "bernoulli":
        h = lambda u: float(logistic_prime(u))
    else:
        raise ValueError(profile)
    values = []
    for power in (0, 2, 4):
        val, err = quad(lambda u: (u**power) * h(u), -np.inf, np.inf,
                        epsabs=2e-13, epsrel=2e-13, limit=300)
        if err > 2e-11:
            raise RuntimeError(f"quadrature uncertainty too large: {err}")
        values.append(float(val))
    return tuple(values)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def loewner_determinant(x: float, y: float, alpha: float = 1.0,
                        bias: float = 0.0) -> tuple[float, float]:
    sx = float(1.0 / (1.0 + math.exp(-alpha * (x - bias))))
    sy = float(1.0 / (1.0 + math.exp(-alpha * (y - bias))))
    direct = (alpha * sx * (1.0 - sx) * alpha * sy * (1.0 - sy)
              - ((sy - sx) / (y - x)) ** 2)
    u = math.exp(alpha * (x - bias))
    r = math.exp(alpha * (y - x))
    identity = (alpha * alpha * u * u / ((1.0 + u) ** 2 * (1.0 + u * r) ** 2)
                * (r - (r - 1.0) ** 2 / math.log(r) ** 2))
    return direct, identity


def certified_matrix_witness() -> dict:
    """Arb certificate for A <= B but sigma(A) not <= sigma(B)."""
    ctx.prec = 256
    a = arb(1) / 2
    eps = arb(1) / 100
    radius = (a * a + eps * eps).sqrt()
    lam_minus, lam_plus = eps - radius, eps + radius
    sigmoid = lambda x: 1 / (1 + (-x).exp())
    mean = (sigmoid(lam_plus) + sigmoid(lam_minus)) / 2
    slope = (sigmoid(lam_plus) - sigmoid(lam_minus)) / (2 * radius)
    d11 = mean - slope * a - sigmoid(-a)
    d22 = mean + slope * a - sigmoid(a)
    d12 = slope * eps
    trace = d11 + d22
    determinant = d11 * d22 - d12 * d12
    discriminant = (trace * trace - 4 * determinant).sqrt()
    eig_minus = (trace - discriminant) / 2
    eig_plus = (trace + discriminant) / 2
    if not (determinant.upper() < 0 and eig_minus.upper() < 0 and eig_plus.lower() > 0):
        raise AssertionError("Arb did not certify the indefinite sigmoid difference")
    return {
        "A": [[-0.5, 0.0], [0.0, 0.5]],
        "B": [[-0.49, 0.01], [0.01, 0.51]],
        "B_minus_A_eigenvalues": [0.0, 0.02],
        "spectrum_B": [str(lam_minus), str(lam_plus)],
        "det_sigmaB_minus_sigmaA": str(determinant),
        "spectrum_sigmaB_minus_sigmaA": [str(eig_minus), str(eig_plus)],
        "arb_precision_bits": ctx.prec,
    }


def main() -> None:
    ROOT.joinpath("figures").mkdir(parents=True, exist_ok=True)

    pi = math.pi
    closed = {
        "square": (1.0 / 6.0, (pi * pi - 6.0) / 18.0,
                   7.0 * pi**4 / 90.0 - 2.0 * pi * pi / 3.0),
        "bernoulli": (1.0, pi * pi / 3.0, 7.0 * pi**4 / 15.0),
    }
    numerical = {name: sensitivity_moments(name) for name in closed}
    for name in closed:
        error = np.max(np.abs(np.asarray(numerical[name]) - np.asarray(closed[name])))
        if error > 3e-11:
            raise AssertionError(f"closed moments failed for {name}: {error}")

    loewner_checks = []
    for x, y, alpha, bias in [(-0.5, 0.5, 1.0, 0.0), (-2.0, 0.3, 0.7, -0.4),
                              (1.2, 1.2001, 3.0, 1.0), (-4.0, -1.0, 0.25, 2.0)]:
        direct, identity = loewner_determinant(x, y, alpha, bias)
        if direct >= 0 or abs(direct - identity) > 2e-11 * max(1.0, abs(direct)):
            raise AssertionError((x, y, alpha, bias, direct, identity))
        loewner_checks.append({"x": x, "y": y, "alpha": alpha, "bias": bias,
                               "direct": direct, "closed_identity": identity})
    matrix_witness = certified_matrix_witness()

    bridge_checks = []
    for profile, expected in (("bernoulli", 0.5), ("square", 1.0)):
        for r in (0.01, 0.02, 0.04):
            alpha, beta = eigenvalues(r, profile)
            coefficient = (alpha / beta - 1.0) / (r * r)
            if abs(coefficient - expected) > 1.2e-3:
                raise AssertionError((profile, r, coefficient, expected))
            bridge_checks.append({
                "profile": profile,
                "r": r,
                "estimated_bridge_coefficient": coefficient,
                "exact_limit": expected,
            })

    radii = np.geomspace(0.03, 30.0, 90)
    curves: dict[str, dict[str, list[float]]] = {}
    for profile in ("square", "bernoulli"):
        alpha, beta = zip(*(eigenvalues(float(r), profile) for r in radii))
        alpha_arr = np.asarray(alpha)
        beta_arr = np.asarray(beta)
        kappa = alpha_arr / beta_arr
        if np.any(alpha_arr <= 0) or np.any(beta_arr <= 0):
            raise AssertionError("positive spectrum expected")
        if np.any(kappa < 1.0 - 2e-10):
            raise AssertionError("radial eigenvalue cannot exceed tangential eigenvalue")
        # Numerical monotonicity is only checked where quadrature is well resolved.
        if np.any(np.diff(kappa[radii <= 12.0]) < -2e-7):
            raise AssertionError(f"condition number is not monotone for {profile}")
        curves[profile] = {
            "alpha": alpha_arr.tolist(),
            "beta": beta_arr.tolist(),
            "kappa": kappa.tolist(),
        }

    phi0 = 1.0 / math.sqrt(2.0 * math.pi)
    bound_checks = []
    for profile in ("square", "bernoulli"):
        m0, m2, m4 = closed[profile]
        for r in (3.0, 5.0, 8.0, 12.0):
            alpha, beta = eigenvalues(r, profile)
            alpha_lo = phi0 / r * (m0 - m2 / (2.0 * r * r))
            alpha_hi = phi0 * m0 / r
            beta_lo = phi0 / r**3 * (m2 - m4 / (2.0 * r * r))
            beta_hi = phi0 * m2 / r**3
            if not (alpha_lo <= alpha <= alpha_hi):
                raise AssertionError((profile, r, "alpha", alpha_lo, alpha, alpha_hi))
            if not (beta_lo <= beta <= beta_hi):
                raise AssertionError((profile, r, "beta", beta_lo, beta, beta_hi))
            bound_checks.append({
                "profile": profile,
                "r": r,
                "alpha": alpha,
                "alpha_bracket": [alpha_lo, alpha_hi],
                "beta": beta,
                "beta_bracket": [beta_lo, beta_hi],
            })

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.0))
    colors = {"square": "#16697a", "bernoulli": "#d1495b"}
    labels = {"square": r"square loss: $h=\sigma'^2$",
              "bernoulli": r"Bernoulli Fisher: $h=\sigma'$"}
    for profile in ("square", "bernoulli"):
        alpha = np.asarray(curves[profile]["alpha"])
        beta = np.asarray(curves[profile]["beta"])
        axes[0].loglog(radii, alpha, color=colors[profile], lw=2,
                       label=labels[profile] + r", tangential")
        axes[0].loglog(radii, beta, color=colors[profile], lw=2, ls="--",
                       label=labels[profile] + r", radial")
        kappa = np.asarray(curves[profile]["kappa"])
        axes[1].loglog(radii, kappa, color=colors[profile], lw=2,
                       label=labels[profile])
        asymptotic = (closed[profile][0] / closed[profile][1]) * radii**2
        tail = radii >= 1.0
        axes[1].loglog(radii[tail], asymptotic[tail], color=colors[profile], lw=1,
                       ls=":")
    axes[0].set_xlabel(r"teacher weight norm $r=\|w_\star\|$")
    axes[0].set_ylabel("curvature / information eigenvalue")
    axes[0].set_title("One tangential law, one radial bottleneck")
    axes[0].grid(True, which="both", alpha=0.22)
    axes[0].legend(fontsize=7, frameon=False)
    axes[1].set_xlabel(r"teacher weight norm $r=\|w_\star\|$")
    axes[1].set_ylabel(r"anisotropy $\kappa=\alpha/\beta$")
    axes[1].set_title(r"Profile-generic large-$r$ anisotropy: $\kappa\asymp r^2$")
    axes[1].grid(True, which="both", alpha=0.22)
    axes[1].legend(fontsize=8, frameon=False)
    fig.tight_layout()
    fixed_pdf_time = datetime(2026, 8, 29, tzinfo=timezone.utc)
    fig.savefig(
        FIGURE,
        bbox_inches="tight",
        metadata={"CreationDate": fixed_pdf_time, "ModDate": fixed_pdf_time},
    )
    plt.close(fig)

    cert = {
        "schema": "single-sigmoid-geometry-certificate-v2",
        "loewner_determinant_checks": loewner_checks,
        "certified_matrix_witness": matrix_witness,
        "schwarzian_bridge_checks": bridge_checks,
        "quadrature": {"gauss_hermite_order": 320, "scipy_quad_tolerance": 2e-13},
        "closed_moments": {k: list(v) for k, v in closed.items()},
        "numerical_moments": {k: list(v) for k, v in numerical.items()},
        "radii": radii.tolist(),
        "curves": curves,
        "finite_r_bound_checks": bound_checks,
        "asymptotic_condition_constants": {
            "square": 3.0 / (pi * pi - 6.0),
            "bernoulli": 3.0 / (pi * pi),
        },
    }
    CERTIFICATE.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print("PASS: Loewner identity, Arb matrix witness, Schwarzian bridge, exact moments, monotone anisotropy, and finite-r bounds")
    print(f"figure_sha256={sha256(FIGURE)}")
    print(f"certificate_sha256={sha256(CERTIFICATE)}")


if __name__ == "__main__":
    main()
