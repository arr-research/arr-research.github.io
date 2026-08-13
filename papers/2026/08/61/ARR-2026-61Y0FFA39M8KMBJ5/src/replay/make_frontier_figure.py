"""Generate the complete scalar phase diagram shown in the manuscript.

The phase and RDF theorems are analytic.  This script only visualizes their
one-dimensional formulas and reports no proof certificate.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


def log_l(k: float) -> float:
    if abs(k) < 0.15:
        u = k * k
        return math.log1p(u / 30 + u * u / 1680 + u**3 / 151200)
    if k > 20:
        correction = 1 - (k * k + 2) * math.exp(-k) + math.exp(-2 * k)
        return math.log(12) + k - 4 * math.log(k) + math.log(correction)
    return math.log(12 * (2 * math.cosh(k) - 2 - k * k) / k**4)


def phi(lam: float, b: float) -> float:
    return -lam * b * b / 4 + log_l(lam * b / 2)


def k_prime(k: float) -> float:
    if k < 0.2:
        return k / 15 + k**3 / 1050 + k**5 / 113400
    if k > 30:
        correction = 1 - (k * k + 2) * math.exp(-k) + math.exp(-2 * k)
        correction_prime = (k * k - 2 * k + 2) * math.exp(-k) - 2 * math.exp(-2 * k)
        return 1 - 4 / k + correction_prime / correction
    a = 2 * math.cosh(k) - 2 - k * k
    return (2 * math.sinh(k) - 2 * k) / a - 4 / k


def contact(k: float) -> float:
    return 2 * log_l(k) - k * k_prime(k)


def lambda_branch(k: float) -> float:
    return 2 * k / k_prime(k)


def main() -> None:
    out = Path(__file__).resolve().parents[1] / "paper" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    kappa_c = brentq(contact, 5.0, 6.0)
    b_c = k_prime(kappa_c)
    lambda_c = lambda_branch(kappa_c)
    d_c = (1 - b_c * b_c) / 4

    lam = np.linspace(0, 36, 720)
    b = np.zeros_like(lam)
    for i, value in enumerate(lam):
        if value > lambda_c:
            hi = max(12.0, value)
            while lambda_branch(hi) < value:
                hi *= 2
            root = brentq(lambda k: lambda_branch(k) - value, kappa_c, hi)
            b[i] = k_prime(root)

    dgrid = np.linspace(0.0007, 0.25, 550)
    rdf = np.empty_like(dgrid)
    for i, distortion in enumerate(dgrid):
        if distortion >= d_c:
            rdf[i] = lambda_c * (0.25 - distortion)
        else:
            target_b = math.sqrt(1 - 4 * distortion)
            hi = max(12.0, 3.0 / distortion)
            while k_prime(hi) < target_b:
                hi *= 2
            kappa = brentq(lambda k: k_prime(k) - target_b, kappa_c, hi)
            rdf[i] = kappa * target_b - log_l(kappa)

    plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 8})
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.55))
    axes[0].plot(lam, b, color="#1557a0", lw=1.8, label="global radius")
    axes[0].axvline(lambda_c, color="#a8342e", ls=":", lw=1.2, label=r"contact $\lambda_c$")
    axes[0].axvline(30, color="#777777", ls="--", lw=1, label=r"spinodal $\lambda=30$")
    axes[0].set(xlabel=r"dual field $\lambda$", ylabel=r"active radius $b$", xlim=(0, 36), ylim=(-0.02, 0.72))
    axes[0].legend(frameon=False, loc="upper left")
    axes[0].grid(alpha=0.2)

    axes[1].plot(dgrid, rdf, color="#a8342e", lw=1.8)
    axes[1].plot([d_c], [lambda_c * (0.25 - d_c)], "o", ms=3.5, color="#1557a0")
    axes[1].set(xlabel=r"distortion $D$", ylabel=r"rate $\mathcal{R}_{4,2}(D)$ (nats)", xlim=(0, 0.25), ylim=(0, 8.5))
    axes[1].grid(alpha=0.2)
    fig.tight_layout(w_pad=2.2)
    fig.savefig(out / "exact_scalar_frontier.pdf", bbox_inches="tight")
    fig.savefig(out / "exact_scalar_frontier.png", dpi=220, bbox_inches="tight")
    print(f"wrote {out / 'exact_scalar_frontier.pdf'}")


if __name__ == "__main__":
    main()
