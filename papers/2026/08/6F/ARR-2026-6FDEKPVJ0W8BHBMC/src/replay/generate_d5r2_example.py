"""Deterministic d=5, r=2 canonical-branch example.

This script evaluates the one-spike branch with the scalar Kummer function and
the rank-two branch with tensor Gauss-Jacobi quadrature for the exact Jacobi
eigenvalue density.  It creates the manuscript figure and a JSON replay file.
The calculation illustrates the comparator crossing; it is not used in any
proof and does not locate the nonanalytic point of the optimized envelope.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.special import hyp1f1, roots_jacobi


D = 5
RANK = 2
RADIUS = 1.0
BASE_DIR = Path(__file__).resolve().parent


class RankTwoBranch:
    """Exact-density Gauss-Jacobi evaluator for the rank-two comparator."""

    def __init__(self, order: int) -> None:
        # For Gr_C(2,5), the two overlap eigenvalues have unnormalized density
        # (x_1-x_2)^2 (1-x_1)(1-x_2) on [0,1]^2.
        nodes, weights = roots_jacobi(order, D - 2 * RANK, 0)
        x = (nodes + 1.0) / 2.0
        weight = weights[:, None] * weights[None, :] * (
            x[:, None] - x[None, :]
        ) ** 2
        self.trace = x[:, None] + x[None, :]
        self.weight = weight / np.sum(weight)

    def __call__(self, field: float | np.ndarray) -> np.ndarray:
        fields = np.atleast_1d(np.asarray(field, dtype=np.float64))
        scale = RADIUS * np.sqrt(D / (RANK * (D - RANK)))
        shift = -RADIUS * RANK * np.sqrt(RANK / (D * (D - RANK)))
        result = np.empty_like(fields)
        for index, value in enumerate(fields):
            exponent = value * scale * self.trace
            maximum = float(np.max(exponent))
            log_mgf = maximum + np.log(
                np.sum(self.weight * np.exp(exponent - maximum))
            )
            result[index] = value * shift + log_mgf
        return result if np.ndim(field) else result[0]


def one_spike_branch(field: float | np.ndarray) -> np.ndarray:
    fields = np.asarray(field, dtype=np.float64)
    shift = -RADIUS * RANK / np.sqrt(D * (D - 1))
    argument = fields * RADIUS * np.sqrt(D / (D - 1))
    return fields * shift + np.log(hyp1f1(RANK, D, argument))


def build_example(order: int, output_dir: Path, json_path: Path) -> dict:
    branch = RankTwoBranch(order)
    reference = RankTwoBranch(order + 48)

    def difference(field: float) -> float:
        return float(branch(field) - one_spike_branch(field))

    crossing = brentq(difference, 3.0, 7.0, xtol=1e-13, rtol=1e-13)
    fields = np.linspace(0.0, 12.0, 481)
    one_values = one_spike_branch(fields)
    rank_values = branch(fields)
    reference_values = reference(fields)
    quadrature_error = float(np.max(np.abs(rank_values - reference_values)))

    sample_fields = np.array([1.0, 4.0, crossing, 6.0, 10.0])
    sample_one = one_spike_branch(sample_fields)
    sample_rank = branch(sample_fields)

    output_dir.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(6.45, 5.15),
        sharex=True,
        gridspec_kw={"height_ratios": [2.05, 1.0], "hspace": 0.08},
    )
    axes[0].plot(fields, one_values, color="#1f5aa6", lw=2.0, label="one-spike")
    axes[0].plot(fields, rank_values, color="#b33a2b", lw=2.0, label="rank-2 block")
    axes[0].axvline(crossing, color="0.35", lw=1.0, ls="--")
    axes[0].set_ylabel(r"$F_{5,2}(s,A)$")
    axes[0].legend(frameon=False, loc="upper left")
    axes[0].grid(alpha=0.18, lw=0.6)

    delta = rank_values - one_values
    axes[1].plot(fields, delta, color="#542788", lw=2.0)
    axes[1].axhline(0.0, color="0.25", lw=0.9)
    axes[1].axvline(crossing, color="0.35", lw=1.0, ls="--")
    axes[1].scatter([crossing], [0.0], s=24, color="black", zorder=3)
    axes[1].annotate(
        rf"$s_\times={crossing:.6f}$",
        xy=(crossing, 0.0),
        xytext=(crossing + 0.65, 0.105),
        arrowprops={"arrowstyle": "->", "lw": 0.8},
        fontsize=9,
    )
    axes[1].set_xlabel(r"field $s$ (with $R=1$)")
    axes[1].set_ylabel(r"$F(A_{2,1})-F(A_{1,1})$")
    axes[1].grid(alpha=0.18, lw=0.6)
    axes[1].set_xlim(0.0, 12.0)

    for axis in axes:
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)

    fig.align_ylabels(axes)
    pdf_path = output_dir / "d5r2_canonical_branches.pdf"
    png_path = output_dir / "d5r2_canonical_branches.png"
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    plt.close(fig)

    result = {
        "parameters": {
            "d": D,
            "r": RANK,
            "R": RADIUS,
            "quadrature_order": order,
            "reference_order": order + 48,
        },
        "jacobi_density": "proportional to (x1-x2)^2 (1-x1)(1-x2)",
        "canonical_crossing": crossing,
        "max_grid_difference_from_reference": quadrature_error,
        "table": [
            {
                "s": float(field),
                "one_spike": float(one),
                "rank_two": float(rank_two),
                "rank_two_minus_one_spike": float(rank_two - one),
            }
            for field, one, rank_two in zip(sample_fields, sample_one, sample_rank)
        ],
        "scope": (
            "Comparator-only diagnostic; the crossing is not asserted to be "
            "the nonanalytic point of the optimized envelope."
        ),
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=96)
    parser.add_argument(
        "--output-dir", type=Path, default=BASE_DIR / "generated"
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=BASE_DIR / "d5r2_canonical_branches.json",
    )
    args = parser.parse_args()
    result = build_example(args.order, args.output_dir, args.json)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
