"""Lightweight replay of the exact one-dimensional Bingham envelope.

The script evaluates dimensions d=2,3,4,5, forms

    c_d(lambda) = -lambda*a + max_{0<=b<=1}
                  [K_d(2*lambda*b) - lambda*a*b**2],

and then takes the numerical Legendre envelope

    R_d(D) = max_lambda [-lambda*D - c_d(lambda)].

It writes a publication PDF/PNG and JSON consistency checks.  The bounded
grids are a reproducibility diagnostic, not a proof of spectral axialization,
global root uniqueness, or a single phase transition.

Runtime target: under 30 seconds and 512 MiB on an ordinary laptop.  The code
uses no pools, branch-and-bound, subprocesses, or adaptive high-memory jobs.
"""

from __future__ import annotations

import json
import platform
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.optimize import brentq, minimize_scalar
from scipy.special import hyp1f1


DIMENSIONS = (2, 3, 4, 5)
B_GRID_SIZE = 1201
DISTORTION_GRID_SIZE = 361
NORMALIZED_DISTORTION_MIN = 0.04
LAMBDA_MAX = 250.0
SELF_CONSISTENCY_CUTOFF = 1.0e-6


def lambda_grid() -> np.ndarray:
    """Resolve the transition region and retain a modest high-rate tail."""

    near = np.linspace(0.0, 20.0, 401)
    tail = np.geomspace(20.05, LAMBDA_MAX, 260)
    return np.unique(np.concatenate((near, tail)))


def log_moment_generating(d: int, kappa: np.ndarray | float) -> np.ndarray:
    """Return log 1F1(1; d; kappa) on the bounded numerical domain."""

    values = hyp1f1(1.0, float(d), kappa)
    if not np.all(np.isfinite(values)) or np.any(values <= 0.0):
        raise FloatingPointError(f"non-finite hypergeometric value for d={d}")
    return np.log(values)


def tilted_mean(d: int, kappa: np.ndarray | float) -> np.ndarray:
    """Derivative of log M_d, evaluated by the contiguous-function ratio."""

    denominator = hyp1f1(1.0, float(d), kappa)
    numerator = hyp1f1(2.0, float(d + 1), kappa)
    return numerator / (float(d) * denominator)


def radial_gain(d: int, lam: float, b: np.ndarray | float) -> np.ndarray:
    """G_lambda(b), with the common -lambda*a factor removed."""

    a = (d - 1.0) / d
    kappa = 2.0 * lam * b
    centered_cumulant = log_moment_generating(d, kappa) - kappa / d
    return centered_cumulant - lam * a * b * b


def global_radius(d: int, lam: float, b_grid: np.ndarray) -> tuple[float, float]:
    """Bounded-grid global search followed by a local scalar refinement."""

    if lam == 0.0:
        return 0.0, 0.0

    values = radial_gain(d, lam, b_grid)
    index = int(np.argmax(values))
    candidates: list[tuple[float, float]] = [
        (0.0, float(values[0])),
        (1.0, float(values[-1])),
    ]

    left = float(b_grid[max(0, index - 1)])
    right = float(b_grid[min(len(b_grid) - 1, index + 1)])
    if right > left:
        result = minimize_scalar(
            lambda radius: -float(radial_gain(d, lam, radius)),
            bounds=(left, right),
            method="bounded",
            options={"xatol": 2.0e-12, "maxiter": 80},
        )
        if result.success:
            refined = float(result.x)
            if 0.0 < refined < 1.0:
                def stationarity(radius: float) -> float:
                    mean = float(tilted_mean(d, 2.0 * lam * radius))
                    beta = (d * mean - 1.0) / (d - 1.0)
                    return beta - radius

                left_sign = stationarity(left)
                right_sign = stationarity(right)
                if left_sign * right_sign <= 0.0:
                    refined = float(
                        brentq(stationarity, left, right, xtol=2.0e-14, rtol=1.0e-14)
                    )
            candidates.append((refined, float(radial_gain(d, lam, refined))))
        else:
            candidates.append((float(b_grid[index]), float(values[index])))
    else:
        candidates.append((float(b_grid[index]), float(values[index])))

    # Deterministic tie-break toward the smaller radius.  This makes the
    # no-memory side of a numerical branch exchange visually stable.
    best_value = max(value for _, value in candidates)
    tolerance = 2.0e-13 * max(1.0, abs(best_value))
    tied = [pair for pair in candidates if best_value - pair[1] <= tolerance]
    return min(tied, key=lambda pair: pair[0])


def scalar_envelope(d: int, lambdas: np.ndarray) -> dict[str, np.ndarray]:
    """Compute c_d(lambda), active radii, and active-channel checks."""

    a = (d - 1.0) / d
    b_grid = np.linspace(0.0, 1.0, B_GRID_SIZE)
    radii = np.empty_like(lambdas)
    gains = np.empty_like(lambdas)
    for index, lam in enumerate(lambdas):
        radii[index], gains[index] = global_radius(d, float(lam), b_grid)

    c_values = -a * lambdas + gains
    kappa = 2.0 * lambdas * radii
    means = tilted_mean(d, kappa)
    beta = (d * means - 1.0) / (d - 1.0)
    distortions = a * (1.0 - radii * radii)
    rates = kappa * means - log_moment_generating(d, kappa)
    dual_rates = -lambdas * distortions - c_values

    informative = radii > SELF_CONSISTENCY_CUTOFF
    self_consistency = np.zeros_like(radii)
    self_consistency[informative] = np.abs(radii[informative] - beta[informative])

    return {
        "radius": radii,
        "gain": gains,
        "c": c_values,
        "kappa": kappa,
        "distortion": distortions,
        "rate": rates,
        "dual_rate": dual_rates,
        "self_consistency": self_consistency,
    }


def legendre_curve(
    d: int, lambdas: np.ndarray, c_values: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Take the bounded-grid Legendre envelope on a common D/a grid."""

    a = (d - 1.0) / d
    normalized = np.linspace(
        NORMALIZED_DISTORTION_MIN, 1.0, DISTORTION_GRID_SIZE
    )
    distortions = a * normalized
    objective = -distortions[:, None] * lambdas[None, :] - c_values[None, :]
    active = np.argmax(objective, axis=1)
    rates = objective[np.arange(len(distortions)), active]
    rates[np.abs(rates) < 5.0e-13] = 0.0
    return normalized, rates, active


def minimum_secant_increment(x: np.ndarray, y: np.ndarray) -> float:
    slopes = np.diff(y) / np.diff(x)
    if len(slopes) < 2:
        return 0.0
    return float(np.min(np.diff(slopes)))


def first_informative_row(
    lambdas: np.ndarray, radii: np.ndarray
) -> dict[str, float] | None:
    indices = np.flatnonzero(radii > 1.0e-3)
    if len(indices) == 0:
        return None
    index = int(indices[0])
    return {
        "lambda_grid": float(lambdas[index]),
        "radius": float(radii[index]),
        "lambda_over_d": float(lambdas[index]),
    }


def make_figure(
    output_pdf: Path,
    output_png: Path,
    lambdas: np.ndarray,
    curves: dict[int, dict[str, np.ndarray]],
) -> None:
    matplotlib.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 9.0,
            "axes.labelsize": 9.0,
            "axes.titlesize": 9.5,
            "legend.fontsize": 8.0,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    colors = plt.get_cmap("tab10").colors
    figure, axes = plt.subplots(1, 2, figsize=(7.15, 3.05), constrained_layout=True)

    for color_index, d in enumerate(DIMENSIONS):
        data = curves[d]
        color = colors[color_index]
        axes[0].plot(
            data["normalized_distortion"],
            data["rdf_rate"],
            color=color,
            linewidth=1.8,
            label=rf"$d={d}$",
        )
        mask = lambdas / d <= 6.0
        axes[1].plot(
            lambdas[mask] / d,
            data["radius"][mask],
            color=color,
            linewidth=1.7,
            label=rf"$d={d}$",
        )

    axes[0].set_xlabel(r"normalized distortion $D/R_0^2$")
    axes[0].set_ylabel(r"rate $R_d(D)$ (nats)")
    axes[0].set_xlim(1.0, NORMALIZED_DISTORTION_MIN)
    axes[0].set_ylim(bottom=0.0)
    axes[0].set_title("Numerical Legendre envelope")
    axes[0].grid(alpha=0.22, linewidth=0.6)
    axes[0].legend(frameon=False)

    axes[1].set_xlabel(r"scaled multiplier $\lambda/d$")
    axes[1].set_ylabel(r"active radius $b_*(\lambda)$")
    axes[1].set_xlim(0.0, 6.0)
    axes[1].set_ylim(-0.02, 1.02)
    axes[1].set_title("Selected global radial maximizer")
    axes[1].grid(alpha=0.22, linewidth=0.6)

    figure.savefig(output_pdf, bbox_inches="tight")
    figure.savefig(output_png, dpi=300, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    started = time.perf_counter()
    output_dir = Path(__file__).resolve().parent
    output_json = output_dir / "frontier_verification.json"
    output_pdf = output_dir / "scalar_envelope.pdf"
    output_png = output_dir / "scalar_envelope.png"

    lambdas = lambda_grid()
    curves: dict[int, dict[str, np.ndarray]] = {}
    dimension_checks: list[dict[str, object]] = []

    for d in DIMENSIONS:
        data = scalar_envelope(d, lambdas)
        normalized, rdf_rate, rdf_active = legendre_curve(d, lambdas, data["c"])
        data["normalized_distortion"] = normalized
        data["rdf_rate"] = rdf_rate
        data["rdf_active_lambda_index"] = rdf_active
        curves[d] = data

        c_slopes = np.diff(data["c"]) / np.diff(lambdas)
        rdf_d = ((d - 1.0) / d) * normalized
        first = first_informative_row(lambdas, data["radius"])
        if first is not None:
            first["lambda_over_d"] = first["lambda_grid"] / d

        dimension_checks.append(
            {
                "d": d,
                "R0_squared": (d - 1.0) / d,
                "c_at_lambda_zero": float(data["c"][0]),
                "minimum_c_secant_slope_increment": float(np.min(np.diff(c_slopes))),
                "maximum_active_self_consistency_residual": float(
                    np.max(data["self_consistency"])
                ),
                "maximum_gibbs_dual_identity_residual": float(
                    np.max(np.abs(data["rate"] - data["dual_rate"]))
                ),
                "rdf_at_no_memory_endpoint": float(rdf_rate[-1]),
                "rdf_minimum": float(np.min(rdf_rate)),
                "maximum_monotonicity_violation": float(
                    max(0.0, float(np.max(np.diff(rdf_rate))))
                ),
                "minimum_rdf_secant_slope_increment": minimum_secant_increment(
                    rdf_d, rdf_rate
                ),
                "selected_radius_minimum": float(np.min(data["radius"])),
                "selected_radius_maximum": float(np.max(data["radius"])),
                "approximate_first_informative_grid_point": first,
            }
        )

    make_figure(output_pdf, output_png, lambdas, curves)
    elapsed = time.perf_counter() - started

    result = {
        "schema_version": 1,
        "formula": {
            "a": "(d-1)/d",
            "K_d(kappa)": "log(1F1(1;d;kappa))-kappa/d",
            "c_d(lambda)": "-lambda*a + max_{0<=b<=1}[K_d(2*lambda*b)-lambda*a*b^2]",
            "R_d(D)": "sup_{lambda>=0}[-lambda*D-c_d(lambda)]",
        },
        "configuration": {
            "dimensions": list(DIMENSIONS),
            "b_grid_size": B_GRID_SIZE,
            "lambda_grid_size": int(len(lambdas)),
            "lambda_max": LAMBDA_MAX,
            "distortion_grid_size": DISTORTION_GRID_SIZE,
            "normalized_distortion_minimum": NORMALIZED_DISTORTION_MIN,
            "parallel_workers": 1,
            "designed_peak_memory_mib_below": 64,
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "runtime_seconds": elapsed,
        "dimensions": dimension_checks,
        "artifacts": {
            "pdf": output_pdf.name,
            "png": output_png.name,
            "json": output_json.name,
        },
        "scope": (
            "Bounded-grid numerical replay of the exact scalar max/sup formula. "
            "These checks and figures do not prove the fixed-radius spectral "
            "extremum, uniqueness of radial roots, or a single phase transition."
        ),
    }
    output_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

    if elapsed >= 30.0:
        raise RuntimeError(f"runtime budget exceeded: {elapsed:.3f} seconds")


if __name__ == "__main__":
    main()
