"""Generate the bounded diagnostic figure for Paper 12.

The figure evaluates only the exact one-dimensional overlap normalizer.  No
plotted value is used in an analytic proof.
"""

from __future__ import annotations

import json
from math import log, pi
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.special import hyp1f1


def cumulants(q: int, kappa: float) -> tuple[float, float, float]:
    lp = float(hyp1f1(1.0, q + 1.0, kappa))
    lm = float(hyp1f1(1.0, q + 1.0, -kappa))
    l = 0.5 * (lp + lm)
    l1 = 0.5 / (q + 1.0) * (
        float(hyp1f1(2.0, q + 2.0, kappa))
        - float(hyp1f1(2.0, q + 2.0, -kappa))
    )
    l2 = 1.0 / ((q + 1.0) * (q + 2.0)) * 0.5 * (
        float(hyp1f1(3.0, q + 3.0, kappa))
        + float(hyp1f1(3.0, q + 3.0, -kappa))
    )
    k = log(l)
    m = l1 / l
    v = l2 / l - m * m
    return k, m, v


def contact(q: int) -> dict[str, float]:
    def free(kappa: float) -> float:
        k, m, _ = cumulants(q, kappa)
        return 2.0 * k - kappa * m

    root = brentq(free, 1.01 * q, 6.0 * q, xtol=2e-12, rtol=2e-14)
    k, b, _ = cumulants(q, root)
    return {"q": q, "kappa_c": root, "b_c": b,
            "D_c": 1.0 - b * b, "R_c": root * b - k,
            "lambda_c": root / (2.0 * b)}


def make_figure(output: Path) -> dict[str, object]:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.0))

    contacts: list[dict[str, float]] = []
    for n in (6, 8, 12, 22):
        q = n - 2
        c = contact(q)
        contacts.append(c)
        kappas = np.geomspace(c["kappa_c"], max(12.0 * q, c["kappa_c"] * 5), 440)
        dvals, rvals = [], []
        for kappa in kappas:
            k, b, _ = cumulants(q, float(kappa))
            dvals.append(1.0 - b * b)
            rvals.append(kappa * b - k)
        line, = axes[0].plot(dvals, rvals, label=fr"$n={n}$")
        axes[0].plot([c["D_c"], 1.0], [c["R_c"], 0.0], "--",
                     color=line.get_color(), lw=1.2)
        axes[0].scatter([c["D_c"]], [c["R_c"]], color=line.get_color(), s=24)

    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(bottom=0)
    axes[0].set_xlabel(r"distortion $D$")
    axes[0].set_ylabel(r"rate $R$ (nats)")
    axes[0].set_title("Complete RDF: one face, one branch")
    axes[0].grid(alpha=0.22)
    axes[0].legend(frameon=False, ncol=2)

    ystar = brentq(lambda y: y - 1.0 - 2.0 * log(y), 2.01, 6.0)
    alpha = ystar * ystar / (2.0 * (ystar - 1.0))
    qs = np.arange(4, 81)
    all_contacts = [contact(int(q)) for q in qs]
    raw = np.array([c["lambda_c"] / c["q"] for c in all_contacts])
    corrected = np.array([
        (c["lambda_c"]
         + ystar**2 / (2.0 * (ystar - 1.0) ** 2) * log(pi * c["q"] / 2.0))
        / c["q"] for c in all_contacts
    ])
    axes[1].plot(qs, raw, label=r"$\lambda_c/q$", lw=1.8)
    axes[1].plot(qs, corrected, label="log-shift corrected", lw=1.8)
    axes[1].axhline(alpha, color="black", ls="--", lw=1.1,
                    label=fr"$\alpha_*={alpha:.4f}$")
    axes[1].set_xlabel(r"$q=n-2$")
    axes[1].set_ylabel("normalized coexistence field")
    axes[1].set_title("Thermodynamic contact convergence")
    axes[1].grid(alpha=0.22)
    axes[1].legend(frameon=False)

    fig.tight_layout()
    fig.savefig(output, bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=180, bbox_inches="tight")
    plt.close(fig)
    return {"scope": "one-dimensional diagnostics only",
            "y_star": ystar, "alpha_star": alpha,
            "selected_contacts": contacts,
            "max_q": int(qs[-1])}


def main() -> None:
    here = Path(__file__).resolve().parent
    output = here / "paper" / "figures" / "complete_phase.pdf"
    payload = make_figure(output)
    json_path = here / "complete_phase_diagnostics.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"PASS: wrote {output} and {json_path}")


if __name__ == "__main__":
    main()
