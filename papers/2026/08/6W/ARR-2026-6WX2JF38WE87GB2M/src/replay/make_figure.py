"""Generate the paper's rank/spectrum figure deterministically."""

from math import comb, factorial
import numpy as np
import matplotlib.pyplot as plt


def double_factorial(n):
    if n <= 0:
        return 1
    out = 1
    for j in range(n, 0, -2):
        out *= j
    return out


def eigenvalue(k, ell, a):
    b = 1.0 - a
    total = 0.0
    for j in range(ell, k + 1):
        if (j - ell) % 2:
            continue
        moment = factorial(j) / (double_factorial(j - ell) * double_factorial(j + ell + 1))
        total += comb(k, j) * a ** (k - j) * b**j * moment
    return total


def effective_rank(k, a):
    b = 1.0 - a
    return 2.0 * b * (2 * k + 1) / (1.0 - (2 * a - 1) ** (2 * k + 1))


def main():
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(7.15, 2.8), constrained_layout=True)

    ks = np.arange(1, 21)
    axes[0].plot(ks, [comb(int(k) + 3, 3) for k in ks], color="#777777", lw=2, label=r"ambient $\binom{k+3}{3}$")
    axes[0].plot(ks, [(k + 1) ** 2 for k in ks], color="#1261a0", lw=2.4, label=r"sphere $(k+1)^2$")
    axes[0].plot(ks, [2 * k + 1 for k in ks], color="#d17c00", lw=2.2, label=r"circle $2k+1$")
    axes[0].plot(ks, [effective_rank(int(k), 0.25) for k in ks], color="#26965c", lw=2, ls="--", label=r"$R_{\rm eff}$ at $q^2=1/4$")
    axes[0].set_xlabel("queries $k$")
    axes[0].set_ylabel("dimension")
    axes[0].set_title("Algebraic and effective support")
    axes[0].legend(frameon=False, fontsize=7.5)

    k = 6
    a = 0.25
    ells = np.arange(k + 1)
    vals = np.array([eigenvalue(k, int(ell), a) for ell in ells])
    axes[1].bar(ells, vals, color="#1261a0", width=0.72)
    axes[1].set_yscale("log")
    axes[1].set_xticks(ells)
    axes[1].set_xlabel(r"harmonic rank $\ell$")
    axes[1].set_ylabel(r"eigenvalue $\lambda_{k\ell}$")
    axes[1].set_title(r"Bell-frame spectrum: $k=6$, $q^2=1/4$")

    fig.savefig(
        "../paper/oracle_variety_spectrum.pdf",
        bbox_inches="tight",
        metadata={"Creator": "Paper 19 reproducibility script", "CreationDate": None, "ModDate": None},
    )
    fig.savefig(
        "../paper/oracle_variety_spectrum.png",
        dpi=220,
        bbox_inches="tight",
        metadata={"Software": "Paper 19 reproducibility script"},
    )


if __name__ == "__main__":
    main()
