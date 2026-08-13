"""Lightweight checks for the large-d complex-projective RDF candidate.

The script only performs scalar root finding and bounded scalar minimization.
It is not a proof and deliberately refuses dimensions above 250.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.special import hyp1f1


def constants() -> tuple[float, float, float, float, float]:
    y_star = brentq(lambda y: y - 1.0 - 2.0 * math.log(y), 2.000001, 10.0)
    phi_star = math.log(y_star)  # equals (y_star-1)/2 at coexistence
    alpha_star = y_star * y_star / (4.0 * phi_star)
    b_star = 1.0 - 1.0 / y_star
    delta_star = 1.0 - b_star * b_star
    return y_star, phi_star, alpha_star, b_star, delta_star


def finite_d_onset(d: int) -> tuple[float, float, float]:
    if not 3 <= d <= 250:
        raise ValueError("this lightweight checker enforces 3 <= d <= 250")
    radius_sq = (d - 1.0) / d

    def threshold(s: float) -> float:
        k = math.log(float(hyp1f1(1.0, float(d), s))) - s / d
        return radius_sq * s * s / (4.0 * k)

    result = minimize_scalar(
        threshold,
        bounds=(1.001 * d, 8.0 * d),
        method="bounded",
        options={"xatol": 1e-10},
    )
    if not result.success:
        raise RuntimeError(result.message)
    s = float(result.x)
    lam = float(result.fun)
    k = math.log(float(hyp1f1(1.0, float(d), s))) - s / d
    b = 2.0 * k / (radius_sq * s)
    return lam, s, b


def limiting_rate(delta: float, alpha_star: float, y_star: float) -> float:
    if not 0.0 < delta <= 1.0:
        raise ValueError("delta must lie in (0,1]")
    b_star = 1.0 - 1.0 / y_star
    delta_star = 1.0 - b_star * b_star
    if delta >= delta_star:
        return alpha_star * (1.0 - delta)
    return -math.log(1.0 - math.sqrt(1.0 - delta))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-d", type=int, default=200)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "repro",
    )
    args = parser.parse_args()
    if not 3 <= args.max_d <= 250:
        raise SystemExit("--max-d must be between 3 and 250")

    y_star, phi_star, alpha_star, b_star, delta_star = constants()
    log_coefficient = alpha_star / (2.0 * phi_star)
    print(f"y_*       = {y_star:.12f}")
    print(f"alpha_*   = {alpha_star:.12f}")
    print(f"b_*       = {b_star:.12f}")
    print(f"delta_*   = {delta_star:.12f}")
    print(f"r_*       = {phi_star:.12f}")
    print(f"log coeff = {log_coefficient:.12f}")
    print()
    print(" d     lambda_c/d       s_c/d          b_c       leading+log")
    dims = [d for d in (3, 4, 5, 10, 20, 50, 100, 200) if d <= args.max_d]
    if args.max_d not in dims:
        dims.append(args.max_d)
    rows = []
    for d in sorted(set(dims)):
        lam, s, b = finite_d_onset(d)
        leading_log = alpha_star * d - log_coefficient * math.log(d)
        rows.append(
            {
                "d": d,
                "lambda_c": lam,
                "lambda_c_over_d": lam / d,
                "s_c_over_d": s / d,
                "b_c": b,
                "leading_plus_log": leading_log,
            }
        )
        print(
            f"{d:3d}   {lam/d:14.10f}  {s/d:14.10f}  "
            f"{b:11.9f}  {leading_log:14.8f}"
        )

    print("\nlimiting normalized RDF")
    for delta in (0.1, 0.25, delta_star, 0.75, 0.9, 1.0):
        print(f"delta={delta:.9f}  r_inf={limiting_rate(delta, alpha_star, y_star):.10f}")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "constants": {
            "y_star": y_star,
            "phi_star": phi_star,
            "alpha_star": alpha_star,
            "b_star": b_star,
            "delta_star": delta_star,
            "log_coefficient": log_coefficient,
        },
        "finite_dimension_diagnostics": rows,
        "scope": {
            "proof_dependency": False,
            "max_dimension_guard": 250,
            "computation": "bounded scalar root finding and minimization",
        },
    }
    (output_dir / "thermodynamic_diagnostics.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )

    deltas = np.linspace(0.01, 1.0, 500)
    rates = np.array(
        [limiting_rate(float(delta), alpha_star, y_star) for delta in deltas]
    )
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.55))
    axes[0].plot(deltas, rates, color="#1f5aa6", lw=2.2)
    axes[0].axvline(delta_star, color="#b53a3a", ls="--", lw=1.2)
    axes[0].scatter([delta_star], [phi_star], color="#b53a3a", s=28, zorder=3)
    axes[0].set_xlabel(r"normalized distortion $\delta$")
    axes[0].set_ylabel(r"$r_\infty(\delta)$ (nats per dimension)")
    axes[0].set_xlim(0.0, 1.0)
    axes[0].set_ylim(bottom=0.0)
    axes[0].grid(alpha=0.25)

    plot_dims = np.array([3, 4, 5, 10, 20, 50, 100, min(args.max_d, 200)])
    plot_dims = np.unique(plot_dims[plot_dims <= args.max_d])
    onset = np.array([finite_d_onset(int(d))[0] / d for d in plot_dims])
    corrected = alpha_star - log_coefficient * np.log(plot_dims) / plot_dims
    axes[1].plot(plot_dims, onset, "o-", color="#1f5aa6", lw=1.8, ms=4.5,
                 label=r"exact scalar $\lambda_{c,d}/d$")
    axes[1].plot(plot_dims, corrected, "s--", color="#d07a20", lw=1.4, ms=4,
                 label=r"$\alpha_*-c_*\log(d)/d$")
    axes[1].axhline(alpha_star, color="#333333", ls=":", lw=1.2,
                    label=r"$\alpha_*$")
    axes[1].set_xscale("log")
    axes[1].set_xlabel(r"Hilbert-space dimension $d$")
    axes[1].set_ylabel(r"scaled onset multiplier")
    axes[1].grid(alpha=0.25)
    axes[1].legend(frameon=False, fontsize=7.5)
    fig.tight_layout()
    fig.savefig(output_dir / "thermodynamic_frontier.pdf", bbox_inches="tight")
    fig.savefig(output_dir / "thermodynamic_frontier.png", dpi=220,
                bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
