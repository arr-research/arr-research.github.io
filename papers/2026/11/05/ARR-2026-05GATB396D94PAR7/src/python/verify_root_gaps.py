#!/usr/bin/env python3
"""
verify_root_gaps.py
Exact rational + high-precision verification and figure generation for:
  "Finite Free Root-Gap Dynamics: Universal Marcel Riesz Monotonicity,
   Sharp Degree-3-to-4 Euclidean and Hyperbolic Pythagorean Transitions,
   and Exact Heat-Flow Compression"
"""

from __future__ import annotations
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Exact Rational Finite Free Convolutions
# ---------------------------------------------------------------------------

def poly_from_roots_exact(roots: list[Fraction]) -> list[Fraction]:
    """Return monic coefficients [c_0=1, c_1, ..., c_d] for prod(x - r_i)."""
    coeffs = [Fraction(1)]
    for r in roots:
        nxt = [Fraction(0)] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            nxt[i] += c
            nxt[i + 1] -= c * r
        coeffs = nxt
    return coeffs


def boxplus_exact(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    d = len(p) - 1
    assert len(q) - 1 == d
    out = [Fraction(0)] * (d + 1)
    for k in range(d + 1):
        s = Fraction(0)
        for i in range(k + 1):
            j = k - i
            w = Fraction(
                math.factorial(d - i) * math.factorial(d - j),
                math.factorial(d) * math.factorial(d - k),
            )
            s += w * p[i] * q[j]
        out[k] = s
    return out


def boxtimes_exact(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    d = len(p) - 1
    assert len(q) - 1 == d
    out = [Fraction(0)] * (d + 1)
    for k in range(d + 1):
        sign = -1 if (k % 2 == 1) else 1
        out[k] = Fraction(sign) * (sign * p[k]) * (sign * q[k]) / Fraction(math.comb(d, k))
    return out


# ---------------------------------------------------------------------------
# Floating-point helpers for high-degree exploration & asymptotics
# ---------------------------------------------------------------------------

def poly_from_roots_f(roots: np.ndarray) -> np.ndarray:
    return np.poly(roots).astype(np.float64)


def boxplus_f(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    d = len(p) - 1
    out = np.zeros(d + 1, dtype=np.float64)
    for k in range(d + 1):
        s = 0.0
        for i in range(k + 1):
            j = k - i
            w = math.factorial(d - i) * math.factorial(d - j) / (math.factorial(d) * math.factorial(d - k))
            s += w * p[i] * q[j]
        out[k] = s
    return out


def roots_sorted_f(p: np.ndarray) -> np.ndarray:
    r = np.roots(p)
    assert np.max(np.abs(r.imag)) < 1e-5, f"Non-real roots: {r}"
    return np.sort(r.real)


def gap_f(p: np.ndarray) -> float:
    return float(np.min(np.diff(roots_sorted_f(p))))


def hermite_e_roots(d: int) -> np.ndarray:
    c = np.zeros(d + 1, dtype=np.float64)
    c[d] = 1.0
    return np.sort(np.polynomial.hermite_e.hermeroots(c).real)


def solve_u_k(k: int) -> float:
    """Solve u * cot(u) = (k - 1) / k on (0, pi/2) by bisection to machine precision."""
    target = (k - 1.0) / k
    lo, hi = 1e-12, math.pi / 2.0 - 1e-12
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        val = mid / math.tan(mid)
        if val > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    report: dict = {}

    # 1. Exact rational verification of d=4 and d=5 AP self-convolutions
    p4_ap = poly_from_roots_exact([Fraction(-3, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(3, 2)])
    c4_ap = boxplus_exact(p4_ap, p4_ap)
    assert p4_ap == [Fraction(1), Fraction(0), Fraction(-5, 2), Fraction(0), Fraction(9, 16)]
    assert c4_ap == [Fraction(1), Fraction(0), Fraction(-5), Fraction(0), Fraction(13, 6)]
    gap4_sq_exact = 10.0 - 14.0 / math.sqrt(3.0)
    gap4_sq_num = gap_f(np.array([float(c) for c in c4_ap])) ** 2
    assert abs(gap4_sq_exact - gap4_sq_num) < 1e-12

    p5_ap = poly_from_roots_exact([Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)])
    c5_ap = boxplus_exact(p5_ap, p5_ap)
    assert p5_ap == [Fraction(1), Fraction(0), Fraction(-5), Fraction(0), Fraction(4), Fraction(0)]
    assert c5_ap == [Fraction(1), Fraction(0), Fraction(-10), Fraction(0), Fraction(31, 2), Fraction(0)]
    gap5_sq_exact = 5.0 - math.sqrt(19.0 / 2.0)
    gap5_sq_num = gap_f(np.array([float(c) for c in c5_ap])) ** 2
    assert abs(gap5_sq_exact - gap5_sq_num) < 1e-12

    report["exact_counterexamples"] = {
        "d4_p_ap": [str(x) for x in p4_ap],
        "d4_conv": [str(x) for x in c4_ap],
        "d4_gap_sq": gap4_sq_exact,
        "d4_ratio": gap4_sq_exact / 2.0,
        "d5_p_ap": [str(x) for x in p5_ap],
        "d5_conv": [str(x) for x in c5_ap],
        "d5_gap_sq": gap5_sq_exact,
        "d5_ratio": gap5_sq_exact / 2.0,
    }

    # 2. Hermite heat-flow sharp constant table kappa_d for d = 2..30
    hermite_table = []
    for d in range(2, 31):
        r_he = hermite_e_roots(d)
        g2 = float(np.min(np.diff(r_he)) ** 2)
        c_heat = 8.0 / d if d % 2 == 0 else (8.0 * d) / (d * d - 1.0)
        kappa = c_heat / g2
        sturm_lo = (math.pi ** 2) / (d + 0.5)
        assert g2 > sturm_lo - 1e-12, f"Sturm failed at d={d}"
        if d >= 4:
            assert kappa < 1.0, f"kappa_d >= 1 at d={d}"
        hermite_table.append({
            "d": d,
            "c_heat": c_heat,
            "gap_He_sq": g2,
            "sturm_lb": sturm_lo,
            "kappa_d": kappa,
        })
    report["hermite_heat_flow"] = {
        "limit_8_over_pi2": 8.0 / (math.pi ** 2),
        "kappa_4_exact": (3.0 + math.sqrt(6.0)) / 6.0,
        "kappa_5_exact": (5.0 + math.sqrt(10.0)) / 9.0,
        "table": hermite_table,
    }

    # 3. Finite-d AP self-convolution ratios for d = 2..20
    ap_self_table = []
    for d in range(2, 21):
        r = np.arange(d, dtype=np.float64)
        r -= np.mean(r)
        p = poly_from_roots_f(r)
        c = boxplus_f(p, p)
        g2 = gap_f(c) ** 2
        ap_self_table.append({"d": d, "ratio": g2 / 2.0})
    report["ap_self_convolution"] = ap_self_table

    # 4. Voiculescu R-transform curve: k-fold free convolution U^{boxplus k}
    u2 = solve_u_k(2)
    r_transform_table = []
    for k in [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 50, 100, 500]:
        if k == 1:
            uk = math.pi / 2.0
            ratio = 1.0
        else:
            uk = solve_u_k(k)
            ratio = (math.pi ** 2) / (4.0 * k * uk * uk)
        r_transform_table.append({
            "k": k,
            "u_k": uk,
            "rho_k_0": 2.0 * uk / math.pi,
            "compression_ratio": ratio,
        })
    report["voiculescu_asymptotics"] = {
        "u_2": u2,
        "k2_limit": (math.pi ** 2) / (8.0 * u2 * u2),
        "basel_limit_pi2_over_12": (math.pi ** 2) / 12.0,
        "table": r_transform_table,
    }

    # 5. Multiplicative-to-additive infinitesimal limit check at d = 4
    mult_limit_table = []
    r4_base = np.array([-1.5, -0.5, 0.5, 1.5])
    for eps in [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
        roots_m = np.exp(eps * r4_base)
        p_m = np.poly(roots_m)
        d = 4
        c_m = np.array([
            ((-1) ** k) * (((-1) ** k) * p_m[k]) ** 2 / math.comb(d, k)
            for k in range(d + 1)
        ])
        rc = roots_sorted_f(c_m)
        rat_c = float(np.min(rc[1:] / rc[:-1]))
        log_rat_sq_ratio = (math.log(rat_c) ** 2) / (2.0 * eps * eps)
        hyp_ratio = math.cosh(0.5 * math.log(rat_c)) / (math.cosh(0.5 * eps) ** 2)
        mult_limit_table.append({
            "eps": eps,
            "log_rat_sq_ratio": log_rat_sq_ratio,
            "cosh_ratio": hyp_ratio,
        })
    report["multiplicative_d4_limit"] = mult_limit_table

    # 6. Randomized validation of Theorems 1, 2, 3 (zero violations)
    rng = np.random.default_rng(20261128)
    min_mr_add = {d: 1e9 for d in [2, 3, 4, 5, 6]}
    min_pyth_d3 = 1e9
    min_mu_d3 = 1e9
    min_hyp_d3 = 1e9
    for d in [2, 3, 4, 5, 6]:
        for _ in range(1500):
            g1 = 1.0 + rng.exponential(2.0, d - 1)
            g2 = 1.0 + rng.exponential(2.0, d - 1)
            s = 10.0 ** rng.uniform(-1.0, 1.0)
            g2 *= s
            r1 = np.concatenate([[0.0], np.cumsum(g1)]); r1 -= np.mean(r1)
            r2 = np.concatenate([[0.0], np.cumsum(g2)]); r2 -= np.mean(r2)
            gc = gap_f(boxplus_f(poly_from_roots_f(r1), poly_from_roots_f(r2)))
            gm1, gm2 = float(np.min(g1)), float(np.min(g2))
            min_mr_add[d] = min(min_mr_add[d], gc / max(gm1, gm2))
            if d == 3:
                min_pyth_d3 = min(min_pyth_d3, (gc * gc) / (gm1 * gm1 + gm2 * gm2))

    for _ in range(5000):
        lr1 = rng.uniform(0.02, 2.5, 2)
        lr2 = rng.uniform(0.02, 2.5, 2)
        r1 = np.exp(np.concatenate([[0.0], np.cumsum(lr1)])); r1 /= np.cbrt(np.prod(r1))
        r2 = np.exp(np.concatenate([[0.0], np.cumsum(lr2)])); r2 /= np.cbrt(np.prod(r2))
        p1, p2 = poly_from_roots_f(r1), poly_from_roots_f(r2)
        c = np.array([1.0, -p1[1] * p2[1] / 3.0, p1[2] * p2[2] / 3.0, -p1[3] * p2[3]])
        rc = roots_sorted_f(c)
        rat_c = float(min(rc[1] / rc[0], rc[2] / rc[1]))
        rho1, rho2 = float(math.exp(np.min(lr1))), float(math.exp(np.min(lr2)))
        mu1, mu2, muc = rho1 + 1 + 1 / rho1, rho2 + 1 + 1 / rho2, rat_c + 1 + 1 / rat_c
        min_mu_d3 = min(min_mu_d3, 3.0 * muc / (mu1 * mu2))
        min_hyp_d3 = min(
            min_hyp_d3,
            math.cosh(0.5 * math.log(rat_c)) / (math.cosh(0.5 * math.log(rho1)) * math.cosh(0.5 * math.log(rho2))),
        )

    assert all(v >= 1.0 - 1e-9 for v in min_mr_add.values())
    assert min_pyth_d3 >= 1.0 - 1e-9
    assert min_mu_d3 >= 1.0 - 1e-9
    assert min_hyp_d3 >= 1.0 - 1e-9
    report["empirical_checks"] = {
        "min_marcel_riesz_additive": min_mr_add,
        "min_d3_pythagorean": min_pyth_d3,
        "min_d3_mu_law": min_mu_d3,
        "min_d3_hyperbolic": min_hyp_d3,
    }

    with open(DATA_DIR / "verification_summary.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # -----------------------------------------------------------------------
    # Generate 3 bespoke 300-DPI journal-grade figures
    # -----------------------------------------------------------------------
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 11.5,
        "legend.fontsize": 9,
        "figure.dpi": 300,
    })

    # Figure 1: The d = 3 -> d = 4 Phase Transition (AP self-convolution & Hermite heat-flow kappa_d)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.1))
    ds_ap = [row["d"] for row in ap_self_table]
    rs_ap = [row["ratio"] for row in ap_self_table]
    k2_lim = report["voiculescu_asymptotics"]["k2_limit"]

    ax1.axhline(1.0, color="#555555", ls="--", lw=1.0, label="Pythagorean threshold ($1.0$)")
    ax1.axhline(k2_lim, color="#b22222", ls=":", lw=1.3,
                label=rf"Voiculescu $k=2$ limit $\pi^2/(8u_2^2) \approx {k2_lim:.4f}$")
    ax1.plot(ds_ap[:2], rs_ap[:2], "o-", color="#1b7837", ms=6.5, lw=1.8, label=r"Superadditive ($d \leq 3$)")
    ax1.plot(ds_ap[1:], rs_ap[1:], "o-", color="#1f5a99", ms=5.5, lw=1.6, label=r"$p_{\mathrm{AP}}^{(d)} \boxplus_d p_{\mathrm{AP}}^{(d)}$ ($d \geq 4$)")
    ax1.annotate(r"$d=4$: $5 - \frac{7}{\sqrt{3}} \approx 0.9585$",
                 xy=(4, rs_ap[2]), xytext=(6.2, 0.968),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.8)
    ax1.annotate(r"$d=5$: $\frac{10-\sqrt{38}}{4} \approx 0.9589$",
                 xy=(5, rs_ap[3]), xytext=(7.2, 0.946),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.8)
    ax1.set_xlabel("Polynomial degree $d$")
    ax1.set_ylabel(r"$\mathrm{gap}(p_{\mathrm{AP}}^{(d)} \boxplus_d p_{\mathrm{AP}}^{(d)})^2 \,/\, 2$")
    ax1.set_title(r"(a) Self-Convolution of Arithmetic Progressions")
    ax1.set_xlim(1.5, 20.5)
    ax1.set_ylim(0.898, 1.018)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper right", frameon=True, framealpha=0.95, fontsize=8.4)

    ds_h = [row["d"] for row in hermite_table]
    ks_h = [row["kappa_d"] for row in hermite_table]
    lim_h = 8.0 / (math.pi ** 2)
    ax2.axhline(1.0, color="#555555", ls="--", lw=1.0, label="Pythagorean threshold ($1.0$)")
    ax2.axhline(lim_h, color="#b22222", ls=":", lw=1.3,
                label=rf"Asymptotic limit $8/\pi^2 \approx {lim_h:.4f}$")
    ax2.plot(ds_h[:2], ks_h[:2], "s-", color="#1b7837", ms=6.5, lw=1.8, label=r"Exact Pythagoras ($\kappa_2=\kappa_3=1$)")
    ax2.plot(ds_h[1:], ks_h[1:], "s-", color="#762a83", ms=4.8, lw=1.6, label=r"Sharp heat-flow constant $\kappa_d$")
    ax2.annotate(r"$\kappa_4 = \frac{3+\sqrt{6}}{6} \approx 0.9082$",
                 xy=(4, ks_h[2]), xytext=(8.0, 0.925),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.8)
    ax2.set_xlabel("Polynomial degree $d$")
    ax2.set_ylabel(r"Sharp heat-flow constant $\kappa_d = c_d^{\mathrm{heat}} / \mathrm{gap}(\mathrm{He}_d)^2$")
    ax2.set_title(r"(b) Finite Free Heat-Flow Expansion Constant $\kappa_d$")
    ax2.set_xlim(1.5, 30.5)
    ax2.set_ylim(0.795, 1.02)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="upper right", frameon=True, framealpha=0.92)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_phase_transition_and_heat_flow.png", dpi=300)
    plt.close(fig)

    # Figure 2: Voiculescu R-transform k-fold curve -> pi^2/12 + Multiplicative d=4 infinitesimal limit
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.1))
    ks_curve = np.arange(1, 41)
    rats_curve = [1.0 if k == 1 else (math.pi ** 2) / (4.0 * k * solve_u_k(int(k)) ** 2) for k in ks_curve]
    basel = (math.pi ** 2) / 12.0
    ax1.plot(ks_curve, rats_curve, "o-", color="#005a32", ms=4.0, lw=1.7,
             label=r"$\pi^2 / (4 k u_k^2)$ where $u_k \cot u_k = \frac{k-1}{k}$")
    ax1.axhline(basel, color="#b22222", ls="--", lw=1.3,
                label=rf"Free-CLT Basel limit $\pi^2/12 \approx {basel:.4f}$")
    ax1.axhline(lim_h, color="#762a83", ls=":", lw=1.2,
                label=rf"Heat-flow limit $8/\pi^2 \approx {lim_h:.4f}$")
    ax1.annotate(rf"$k=2$: ${k2_lim:.4f}$", xy=(2, rats_curve[1]), xytext=(6, 0.935),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9), fontsize=8.8)
    ax1.set_xlabel("Free convolution order $k$")
    ax1.set_ylabel(r"Asymptotic compression ratio $1 / (k \rho_k(0)^2)$")
    ax1.set_title(r"(a) Voiculescu $R$-Transform Law for $U^{\boxplus k}$")
    ax1.set_xlim(0.5, 40.5)
    ax1.set_ylim(0.795, 1.015)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper right", frameon=True, framealpha=0.92)

    eps_grid = np.geomspace(0.01, 2.0, 45)
    y_d2, y_d3, y_d4 = [], [], []
    for eps in eps_grid:
        for d_cur, store in [(2, y_d2), (3, y_d3), (4, y_d4)]:
            rb = np.arange(d_cur, dtype=np.float64); rb -= np.mean(rb)
            pm = np.poly(np.exp(eps * rb))
            cm = np.array([((-1) ** k) * (((-1) ** k) * pm[k]) ** 2 / math.comb(d_cur, k) for k in range(d_cur + 1)])
            rc = roots_sorted_f(cm)
            rat_c = float(np.min(rc[1:] / rc[:-1]))
            store.append((math.log(rat_c) ** 2) / (2.0 * eps * eps))
    ax2.semilogx(eps_grid, y_d2, "-", color="#1b7837", lw=1.9, label=r"$d=2$ ($\cosh c = \cosh a \cosh b$)")
    ax2.semilogx(eps_grid, y_d3, "--", color="#2166ac", lw=1.9, label=r"$d=3$ (Theorem 3: $\mu/3$ supermult.)")
    ax2.semilogx(eps_grid, y_d4, "-", color="#b2182b", lw=2.0, label=r"$d=4$ (breaks for small $\varepsilon$)")
    ax2.axhline(1.0, color="#555555", ls=":", lw=1.0)
    ax2.axhline(5.0 - 7.0 / math.sqrt(3.0), color="#b2182b", ls=":", lw=1.1,
                label=r"$5 - 7/\sqrt{3} \approx 0.9585$ ($\varepsilon \to 0^+$)")
    ax2.set_xlabel(r"Log-spacing parameter $\varepsilon = \log \rho$ (log scale)")
    ax2.set_ylabel(r"$(\log \mathrm{rat}(p_\varepsilon \boxtimes_d p_\varepsilon))^2 \,/\, (2 \varepsilon^2)$")
    ax2.set_title(r"(b) Multiplicative $\boxtimes_d$ Infinitesimal Limit ($\varepsilon \to 0^+$)")
    ax2.set_ylim(0.94, 1.32)
    ax2.grid(True, which="both", alpha=0.22)
    ax2.legend(loc="upper left", frameon=True, framealpha=0.92, fontsize=8.3)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_voiculescu_and_multiplicative_limit.png", dpi=300)
    plt.close(fig)

    # Figure 3: Geometry of the cubic semigroup domain K_mu in (alpha, beta) coordinates
    fig, ax = plt.subplots(figsize=(6.0, 5.2))
    grid = np.linspace(0.005, 0.995, 400)
    A, B = np.meshgrid(grid, grid)
    PHI = (A - B) ** 2 / ((1.0 - A) * (1.0 - B)) + A + B + A * B
    levels = [1.0, 2.0, 3.0, 5.0, 10.0]
    cs = ax.contour(A, B, PHI, levels=levels, colors=["#2b83ba", "#4dac26", "#d7191c", "#fdae61", "#762a83"], linewidths=[1.3, 1.3, 2.2, 1.5, 1.4])
    ax.clabel(cs, inline=True, fontsize=8.5, fmt={lvl: rf"$\Phi={int(lvl)}$" for lvl in levels})
    ax.contourf(A, B, PHI, levels=[0.0, 3.0], colors=["#d7191c"], alpha=0.10)
    # Plot an explicit product pair (a1, b1), (a2, b2) -> (a1*a2, b1*b2)
    a1, b1 = 0.72, 0.35
    a2, b2 = 0.42, 0.78
    a12, b12 = a1 * a2, b1 * b2
    ax.scatter([a1, a2], [b1, b2], s=55, color="#1f5a99", zorder=5, label=r"Inputs $(\alpha_1,\beta_1), (\alpha_2,\beta_2)$")
    ax.scatter([a12], [b12], s=70, marker="*", color="#b2182b", zorder=6, label=r"Product $(\alpha_1\alpha_2, \beta_1\beta_2)$")
    ax.annotate("", xy=(a12, b12), xytext=(a1, b1), arrowprops=dict(arrowstyle="->", color="#1f5a99", ls="--", lw=1.0))
    ax.annotate("", xy=(a12, b12), xytext=(a2, b2), arrowprops=dict(arrowstyle="->", color="#1f5a99", ls="--", lw=1.0))
    ax.plot([0, a12], [0, b12], color="#b2182b", ls=":", lw=1.2, label=r"Star-shaped ray $\tau(\alpha_1\alpha_2,\beta_1\beta_2)$")
    ax.set_xlabel(r"$\alpha = \tilde{v}/\tilde{u}^2 \in (0, 1)$")
    ax.set_ylabel(r"$\beta = \tilde{u}/\tilde{v}^2 \in (0, 1)$")
    ax.set_title(r"Cubic Multiplicative Semigroup Level Sets $\Phi(\alpha,\beta) \leq \mu$")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.22)
    ax.legend(loc="lower right", bbox_to_anchor=(0.73, 0.02), frameon=True, framealpha=0.95, fontsize=8.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_cubic_semigroup_geometry.png", dpi=300)
    plt.close(fig)

    print("VERIFY_ROOT_GAPS_OK")
    print(f"  d=4 exact ratio = {gap4_sq_exact/2:.12f}")
    print(f"  d=5 exact ratio = {gap5_sq_exact/2:.12f}")
    print(f"  kappa_4 = {(3+math.sqrt(6))/6:.12f}, kappa_5 = {(5+math.sqrt(10))/9:.12f}, 8/pi^2 = {8/math.pi**2:.12f}")
    print(f"  u_2 = {u2:.12f}, k=2 limit = {k2_lim:.12f}, pi^2/12 = {basel:.12f}")
    print(f"  empirical mins: MR={min(min_mr_add.values()):.8f}, pyth3={min_pyth_d3:.8f}, mu3={min_mu_d3:.8f}, hyp3={min_hyp_d3:.8f}")


if __name__ == "__main__":
    main()
