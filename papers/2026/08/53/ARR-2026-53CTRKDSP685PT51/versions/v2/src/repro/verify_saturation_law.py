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
from scipy.special import gamma, polygamma


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


def eigenvalues_p(r: float, p: float) -> tuple[float, float]:
    if p <= 0:
        raise ValueError("p must be positive")
    h = lambda z: logistic_prime(r * z) ** p
    # Change variables u = r z once saturation makes the Gaussian integrand
    # narrower than a fixed Gauss-Hermite grid can resolve.
    if r >= 2.0:
        phi0 = 1.0 / math.sqrt(2.0 * math.pi)
        damp = lambda u: math.exp(-(u * u) / (2.0 * r * r))
        hs = lambda u: float(logistic_prime(u) ** p)
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


def eigenvalues(r: float, profile: str) -> tuple[float, float]:
    powers = {"square": 2.0, "bernoulli": 1.0}
    if profile not in powers:
        raise ValueError(profile)
    return eigenvalues_p(r, powers[profile])


def sensitivity_moments_p(p: float) -> tuple[float, float, float]:
    h = lambda u: float(logistic_prime(u) ** p)
    values = []
    for power in (0, 2, 4):
        val, err = quad(lambda u: (u**power) * h(u), -np.inf, np.inf,
                        epsabs=2e-13, epsrel=2e-13, limit=300)
        if err > 1e-9:
            raise RuntimeError(f"quadrature uncertainty too large: {err}")
        values.append(float(val))
    return tuple(values)


def sensitivity_moments(profile: str) -> tuple[float, float, float]:
    powers = {"square": 2.0, "bernoulli": 1.0}
    if profile not in powers:
        raise ValueError(profile)
    return sensitivity_moments_p(powers[profile])


def closed_moments_p(p: float) -> tuple[float, float, float]:
    m0 = float(gamma(p) ** 2 / gamma(2.0 * p))
    psi1 = float(polygamma(1, p))
    psi3 = float(polygamma(3, p))
    return m0, 2.0 * psi1 * m0, (12.0 * psi1**2 + 2.0 * psi3) * m0


def weighted_gaussian_moment(r: float, p: float, j: int) -> float:
    """E[Z^(2j) sigma'(rZ)^p], using the saturation-stable variable s=rZ."""
    phi0 = 1.0 / math.sqrt(2.0 * math.pi)
    integrand = lambda s: (
        s ** (2 * j)
        * float(logistic_prime(s) ** p)
        * math.exp(-(s * s) / (2.0 * r * r))
    )
    value = quad(integrand, -np.inf, np.inf, epsabs=2e-13, epsrel=2e-13, limit=400)[0]
    return phi0 * value / r ** (2 * j + 1)


def fixed_sphere_eigenvalues(r: float, p: float, d: int) -> tuple[float, float]:
    """Exact 1D quadrature for X uniform on the sphere of radius sqrt(d)."""
    if d < 2:
        raise ValueError("d must be at least two")
    radius = math.sqrt(d)
    normalizer = float(gamma(d / 2.0) / (math.sqrt(math.pi) * gamma((d - 1.0) / 2.0) * radius))

    def density(z: float) -> float:
        base = max(0.0, 1.0 - z * z / d)
        return normalizer * base ** ((d - 3.0) / 2.0)

    beta = quad(
        lambda z: z * z * float(logistic_prime(r * z) ** p) * density(z),
        -radius,
        radius,
        epsabs=2e-13,
        epsrel=2e-13,
        limit=300,
    )[0]
    alpha = quad(
        lambda z: ((d - z * z) / (d - 1.0))
        * float(logistic_prime(r * z) ** p)
        * density(z),
        -radius,
        radius,
        epsabs=2e-13,
        epsrel=2e-13,
        limit=300,
    )[0]
    return float(alpha), float(beta)


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


def empirical_block_check(
    *, p: float, r: float, d: int, n: int, delta: float, seed: int
) -> dict:
    """Replay one declared realization of the blockwise finite-sample theorem."""
    m = d - 1
    alpha, beta = eigenvalues_p(r, p)
    gamma0 = weighted_gaussian_moment(r, 2.0 * p, 0)
    gamma1 = weighted_gaussian_moment(r, 2.0 * p, 1)
    gamma2 = weighted_gaussian_moment(r, 2.0 * p, 2)
    hmax = 4.0 ** (-p)
    k1 = math.exp(-2.0) / (p * p * r * r)
    k2 = 4.0 * math.exp(-2.0) / (p * p * r * r)
    t = math.log(12.0 / delta)
    u0 = m * math.log(9.0) + t
    s0_plus = (
        n * gamma0
        + math.sqrt(2.0 * n * hmax * hmax * gamma0 * t)
        + hmax * hmax * t / 3.0
    )
    s1_plus = (
        n * gamma1
        + math.sqrt(2.0 * n * k1 * gamma1 * t)
        + k1 * t / 3.0
    )
    e_t = (
        math.sqrt(2.0 * gamma0 * t / n)
        + hmax * t / (3.0 * n)
        + 4.0 * (math.sqrt(s0_plus * u0) + hmax * u0) / n
    )
    e_r = math.sqrt(2.0 * gamma2 * t / n) + k2 * t / (3.0 * n)
    q_n = math.sqrt(s1_plus) / n * (math.sqrt(m) + math.sqrt(2.0 * t))

    rng = np.random.default_rng(seed)
    x = rng.standard_normal((n, d))
    weights = logistic_prime(r * x[:, 0]) ** p
    radial = float(np.mean(weights * x[:, 0] ** 2))
    cross = np.mean((weights * x[:, 0])[:, None] * x[:, 1:], axis=0)
    tangential = (x[:, 1:].T * weights) @ x[:, 1:] / n
    tangential_error = float(np.linalg.norm(tangential - alpha * np.eye(m), ord=2))
    radial_error = abs(radial - beta)
    cross_error = float(np.linalg.norm(cross))
    if tangential_error > e_t or radial_error > e_r or cross_error > q_n:
        raise AssertionError(
            ("empirical block replay outside theorem event", tangential_error, e_t,
             radial_error, e_r, cross_error, q_n)
        )
    population = np.diag([beta] + [alpha] * m)
    empirical = (x.T * weights) @ x / n
    scale = np.diag([1.0 / math.sqrt(beta)] + [1.0 / math.sqrt(alpha)] * m)
    relative_error = float(np.linalg.norm(scale @ (empirical - population) @ scale, ord=2))
    epsilon_n = max(e_t / alpha, e_r / beta) + q_n / math.sqrt(alpha * beta)
    if relative_error > epsilon_n:
        raise AssertionError(("relative Loewner replay failed", relative_error, epsilon_n))
    return {
        "p": p,
        "r": r,
        "d": d,
        "n": n,
        "delta": delta,
        "seed": seed,
        "population": {"alpha": alpha, "beta": beta},
        "bounds": {"e_T": e_t, "e_R": e_r, "q_n": q_n, "epsilon_n": epsilon_n},
        "realized_errors": {
            "tangential_operator": tangential_error,
            "radial": radial_error,
            "cross": cross_error,
            "relative_operator": relative_error,
        },
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

    all_p_moment_checks = []
    for p in (0.5, 1.0, 1.7, 2.0, 3.25):
        numerical_p = sensitivity_moments_p(p)
        closed_p = closed_moments_p(p)
        error = float(np.max(np.abs(np.asarray(numerical_p) - np.asarray(closed_p))))
        if error > 8e-10:
            raise AssertionError(("all-p moments", p, numerical_p, closed_p, error))
        all_p_moment_checks.append({
            "p": p,
            "numerical": list(numerical_p),
            "gamma_polygamma": list(closed_p),
            "max_abs_error": error,
        })

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
    for p in (0.5, 1.0, 1.7, 2.0, 3.25):
        expected = p / 2.0
        for r in (0.01, 0.02, 0.04):
            alpha, beta = eigenvalues_p(r, p)
            coefficient = (alpha / beta - 1.0) / (r * r)
            if abs(coefficient - expected) > 2.5e-3:
                raise AssertionError((p, r, coefficient, expected))
            bridge_checks.append({
                "p": p,
                "r": r,
                "estimated_bridge_coefficient": coefficient,
                "exact_limit": expected,
            })

    spherical_bridge_checks = []
    sphere_dimension = 5
    sphere_q = sphere_dimension / (sphere_dimension + 2.0)
    for p in (0.7, 1.0, 2.3):
        for r in (0.01, 0.02, 0.04):
            alpha, beta = fixed_sphere_eigenvalues(r, p, sphere_dimension)
            coefficient = (alpha / beta - 1.0) / (r * r)
            expected = sphere_q * p / 2.0
            if abs(coefficient - expected) > 2.5e-3:
                raise AssertionError(("spherical bridge", p, r, coefficient, expected))
            spherical_bridge_checks.append({
                "distribution": f"uniform_sphere_radius_sqrt_{sphere_dimension}",
                "dimension": sphere_dimension,
                "q_X": sphere_q,
                "p": p,
                "r": r,
                "estimated_coefficient": coefficient,
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

    all_p_endpoint_checks = []
    for p in (0.5, 1.0, 1.7, 2.0, 3.25):
        small_r = 0.08
        alpha, beta = eigenvalues_p(small_r, p)
        kappa = alpha / beta
        small_jet = (
            1.0
            + p * small_r**2 / 2.0
            - p * small_r**4 / 8.0
            + p * (p + 1.0) * small_r**6 / 16.0
        )
        if abs(kappa - small_jet) > 2e-8:
            raise AssertionError(("small all-p jet", p, kappa, small_jet))
        large_r = 30.0
        alpha, beta = eigenvalues_p(large_r, p)
        kappa_large = alpha / beta
        psi1 = float(polygamma(1, p))
        psi3 = float(polygamma(3, p))
        refined = large_r**2 / (2.0 * psi1) + 1.0 + psi3 / (4.0 * psi1**2)
        if abs(kappa_large - refined) > 0.08:
            raise AssertionError(("large all-p refinement", p, kappa_large, refined))
        all_p_endpoint_checks.append({
            "p": p,
            "small_r": small_r,
            "kappa_small": kappa,
            "small_r_series_through_r6": small_jet,
            "large_r": large_r,
            "kappa_large": kappa_large,
            "large_r_refined_formula": refined,
        })

    quantitative_bridge_checks = []
    logistic_a = 0.25
    logistic_c = -0.125
    logistic_d4 = 0.0
    logistic_m5_bound = 1082.0
    delta0 = 0.1
    loewner_k = (
        abs(logistic_c) / 6.0
        + abs(logistic_d4) * delta0 / 24.0
        + logistic_m5_bound * delta0**2 / 120.0
    )
    loewner_d = (
        abs(logistic_a * logistic_d4) / 12.0
        + 7.0 * logistic_a * logistic_m5_bound * delta0 / 120.0
        + delta0 * loewner_k**2
    )
    for p in (0.5, 1.0, 2.0, 3.25):
        h0 = 4.0 ** (-p)
        h2 = -p * h0 / 2.0
        q4 = p / 2.0 + 11.0 * p**2 / 4.0 + 3.0 * p**3 + p**4
        m4_bound = h0 * q4
        r0 = 0.08
        if 1.5 * abs(h2) * r0**2 + 0.625 * m4_bound * r0**4 > h0 / 2.0:
            raise AssertionError(("r0 condition", p))
        c_h = (
            3.0 * m4_bound / (2.0 * h0)
            + 3.0 * (h2 / h0) ** 2
            + 5.0 * abs(h2) * m4_bound * r0**2 / (4.0 * h0**2)
        )
        for r, delta in ((0.02, 0.03), (0.05, 0.07), (0.08, 0.1)):
            alpha, beta = eigenvalues_p(r, p)
            kappa = alpha / beta
            gaussian_error = abs(kappa - 1.0 - p * r * r / 2.0)
            if gaussian_error > c_h * r**4:
                raise AssertionError(("quantitative kappa", p, r, gaussian_error, c_h * r**4))
            determinant, _ = loewner_determinant(0.0, delta)
            loewner_error = abs(determinant + delta**2 / 192.0)
            if loewner_error > loewner_d * abs(delta) ** 3:
                raise AssertionError(("quantitative Loewner", delta, loewner_error, loewner_d * abs(delta) ** 3))
            direct_error = abs(
                (kappa - 1.0) / r**2
                + 6.0 * p * determinant / (logistic_a**2 * delta**2)
            )
            direct_bound = c_h * r**2 + 6.0 * p * loewner_d * abs(delta) / logistic_a**2
            if direct_error > direct_bound:
                raise AssertionError(("direct finite bridge", p, r, delta, direct_error, direct_bound))
            quantitative_bridge_checks.append({
                "p": p,
                "r": r,
                "delta": delta,
                "kappa_remainder": gaussian_error,
                "kappa_bound": c_h * r**4,
                "loewner_remainder": loewner_error,
                "loewner_bound": loewner_d * abs(delta) ** 3,
                "direct_bridge_error": direct_error,
                "direct_bridge_bound": direct_bound,
            })

    empirical_checks = [
        empirical_block_check(p=1.0, r=4.0, d=6, n=60000, delta=0.05, seed=2026082901),
        empirical_block_check(p=2.0, r=5.0, d=7, n=80000, delta=0.05, seed=2026082902),
        empirical_block_check(p=1.5, r=6.0, d=5, n=90000, delta=0.05, seed=2026082903),
    ]

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
        "schema": "single-sigmoid-geometry-certificate-v3",
        "loewner_determinant_checks": loewner_checks,
        "certified_matrix_witness": matrix_witness,
        "schwarzian_bridge_checks": bridge_checks,
        "spherical_bridge_checks": spherical_bridge_checks,
        "quantitative_bridge_checks": quantitative_bridge_checks,
        "quadrature": {"gauss_hermite_order": 320, "scipy_quad_tolerance": 2e-13},
        "closed_moments": {k: list(v) for k, v in closed.items()},
        "numerical_moments": {k: list(v) for k, v in numerical.items()},
        "all_p_moment_checks": all_p_moment_checks,
        "all_p_endpoint_checks": all_p_endpoint_checks,
        "radii": radii.tolist(),
        "curves": curves,
        "finite_r_bound_checks": bound_checks,
        "empirical_block_checks": empirical_checks,
        "asymptotic_condition_constants": {
            "square": 3.0 / (pi * pi - 6.0),
            "bernoulli": 3.0 / (pi * pi),
        },
    }
    CERTIFICATE.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        "PASS: Loewner/Arb witness; spherical and quantitative bridge grids; "
        "all-p moment/endpoint test points; p=1,2 anisotropy grids; three "
        "fixed-seed empirical block realizations; and finite-r brackets"
    )
    print(f"figure_sha256={sha256(FIGURE)}")
    print(f"certificate_sha256={sha256(CERTIFICATE)}")


if __name__ == "__main__":
    main()
