"""Comprehensive exact & numerical verification suite + 3 bespoke 300-DPI figures for Frontier F4:
   'The Log-Concave and kappa-Concave Steinhaus-Trybula Barriers'.
   Author: Lluis Eriksson (editor@airr.science), with Google Antigravity assistance.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(r"C:\Users\lluis\.gemini\antigravity\scratch\airr-mitochondria-frontier\logconcave-nontransitive")
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# 1. Exact kappa-concave median barriers M(kappa; u)
# ---------------------------------------------------------------------------
def M_convex_k(k: int, u: float = 1.0) -> float:
    """Exact P(X^* > Y^*) for kappa = 1/k (k-dim convex body projection), scale ratio u."""
    a = 2.0 ** (-1.0 / k)
    pts = sorted(set([a - 1.0, a] + [p for p in (-a * u, (1.0 - a) * u) if a - 1.0 < p < a]))
    nodes, weights = np.polynomial.legendre.leggauss(32)
    tot = 0.0
    for L, R in zip(pts[:-1], pts[1:]):
        xs = 0.5 * (R - L) * nodes + 0.5 * (R + L)
        ws = 0.5 * (R - L) * weights
        fx = k * np.maximum(a - xs, 0.0) ** (k - 1)
        Sy = np.minimum(1.0, np.maximum(a + xs / u, 0.0) ** k)
        tot += float(np.sum(ws * fx * Sy))
    return tot


def M_convex_k_binomial(k: int) -> float:
    """Exact closed-form binomial evaluation of M(1/k; 1)."""
    a = 2.0 ** (-1.0 / k)
    t = 2.0 * a - 1.0
    return t**k + sum(
        math.comb(k, j) * ((2.0 * a) ** (k - j)) * ((-1) ** j) * (k / (k + j)) * (1.0 - t ** (k + j))
        for j in range(k + 1)
    )


def M_pareto(gam: float, u: float = 1.0) -> float:
    """Exact smooth P(X^* > Y^*) for kappa = -1/gamma (Pareto tail), scale ratio u."""
    a = 2.0 ** (1.0 / gam)
    yb = a + u * (a - 1.0)
    wb = yb ** (-gam)
    nodes, weights = np.polynomial.legendre.leggauss(64)
    ws_pts = 0.5 * (1.0 - wb) * nodes + 0.5 * (1.0 + wb)
    wts = 0.5 * (1.0 - wb) * weights
    y = ws_pts ** (-1.0 / gam)
    Sy = (a - (y - a) / u) ** (-gam)
    return float(wb + np.sum(wts * Sy))


def G_logconcave(lam: float, u: float) -> float:
    """Exact P(E1 + u*E2 > (1+u)*lam) for iid Exp(1)."""
    if abs(u - 1.0) < 1e-7:
        return (1.0 + 2.0 * lam) * math.exp(-2.0 * lam)
    return (math.exp(-(1.0 + u) * lam) - u * math.exp(-(1.0 + 1.0 / u) * lam)) / (1.0 - u)


# ---------------------------------------------------------------------------
# 2. Exact Exponential-Chain Recurrence (Two-Sided and One-Sided)
# ---------------------------------------------------------------------------
def T_exp(c: float, p: float) -> float:
    if c < 1.0:
        return 1.0 - c + math.log(c) - math.log(1.0 - p)
    return -math.log(1.0 - p)


def solve_odd_exp_chain(m: int) -> tuple[float, float]:
    """Exact n = 2m + 1 two-sided shifted-exponential chain value and c_m."""
    lo, hi = 0.5, 1.0 - math.exp(-1.0) - 1e-12
    for _ in range(90):
        p = 0.5 * (lo + hi)
        c = -math.log(1.0 - p)
        for _ in range(m - 1):
            c = T_exp(c, p)
        if (1.0 + 2.0 * c) * math.exp(-2.0 * c) >= p:
            lo = p
        else:
            hi = p
    p = 0.5 * (lo + hi)
    c = -math.log(1.0 - p)
    for _ in range(m - 1):
        c = T_exp(c, p)
    return p, c


def solve_even_exp_chain(m: int) -> float:
    """Exact n = 2m asymmetric two-sided shifted-exponential chain (0 + m right + (m-1) left)."""
    lo, hi = 0.5, 1.0 - math.exp(-1.0) - 1e-12
    us = np.geomspace(0.3, 3.3, 250)
    for _ in range(70):
        p = 0.5 * (lo + hi)
        c = -math.log(1.0 - p)
        cs = [c]
        for _ in range(m - 1):
            c = T_exp(c, p)
            cs.append(c)
        ca, cb = cs[m - 1], cs[m - 2]
        best_cr = 0.0
        for u in us:
            d = ca + u * cb
            cr = (1.0 + d) * math.exp(-d) if abs(u - 1.0) < 1e-6 else (math.exp(-d) - u * math.exp(-d / u)) / (1.0 - u)
            if cr > best_cr:
                best_cr = cr
        if best_cr >= p:
            lo = p
        else:
            hi = p
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# 3. Unimodal Zero-Penalty Exact Evaluator
# ---------------------------------------------------------------------------
def unimodal_win(L1: float, M1: float, q1: float, eps1: float, L2: float, M2: float, q2: float, eps2: float) -> float:
    nodes, weights = np.polynomial.legendre.leggauss(16)

    def u_win(a1: float, b1: float, a2: float, b2: float) -> float:
        if a1 >= b2:
            return 1.0
        if b1 <= a2:
            return 0.0
        xs = 0.5 * (b1 - a1) * nodes + 0.5 * (a1 + b1)
        ws = 0.5 * (b1 - a1) * weights / (b1 - a1)
        F2 = np.clip((xs - a2) / (b2 - a2), 0.0, 1.0)
        return float(np.sum(ws * F2))

    return (
        (1.0 - q1) * (1.0 - q2) * u_win(L1, L1 + eps1, L2, L2 + eps2)
        + (1.0 - q1) * q2 * u_win(L1, L1 + eps1, L2, M2)
        + q1 * (1.0 - q2) * u_win(L1, M1, L2, L2 + eps2)
        + q1 * q2 * u_win(L1, M1, L2, M2)
    )


# ---------------------------------------------------------------------------
# 4. Random Log-Concave Density Stress Test (3,000 random pairs + cycles)
# ---------------------------------------------------------------------------
def random_lc_density(rng: np.random.Generator, gx: np.ndarray, K: int = 8) -> tuple[np.ndarray, np.ndarray, float]:
    """Generate a random continuous log-concave density on a random subinterval of gx, shifted to median 0."""
    L = float(rng.uniform(-4.0, 0.0))
    length = float(np.exp(rng.uniform(-0.5, 2.0)))
    s0 = float(rng.normal(0.0, 4.0))
    D = rng.exponential(1.2, size=K - 2)
    slopes = np.empty(K - 1)
    slopes[0] = s0
    slopes[1:] = s0 - np.cumsum(D)
    v_k = np.zeros(K)
    v_k[1:] = np.cumsum(slopes) / (K - 1)
    v_k -= v_k.max()
    # Evaluate on fine local grid, compute exact median, then shift to gx
    t_loc = np.linspace(0.0, 1.0, 401)
    idx = np.clip((t_loc * (K - 1)).astype(int), 0, K - 2)
    frac = t_loc * (K - 1) - idx
    pdf_loc = np.exp(v_k[idx] * (1.0 - frac) + v_k[idx + 1] * frac)
    x_loc = L + length * t_loc
    cdf_loc = np.zeros_like(x_loc)
    cdf_loc[1:] = np.cumsum(0.5 * (pdf_loc[:-1] + pdf_loc[1:]) * (x_loc[1] - x_loc[0]))
    cdf_loc /= cdf_loc[-1]
    med = float(np.interp(0.5, cdf_loc, x_loc))
    # Shift by -med onto gx
    L_sh = L - med
    t = (gx - L_sh) / length
    inside = (t >= 0.0) & (t <= 1.0)
    pdf = np.zeros_like(gx)
    ti = t[inside]
    ix = np.clip((ti * (K - 1)).astype(int), 0, K - 2)
    fr = ti * (K - 1) - ix
    pdf[inside] = np.exp(v_k[ix] * (1.0 - fr) + v_k[ix + 1] * fr)
    dx = gx[1] - gx[0]
    area = float(np.trapezoid(pdf, gx))
    pdf /= area
    cdf = np.zeros_like(gx)
    cdf[1:] = np.cumsum(0.5 * (pdf[:-1] + pdf[1:]) * dx)
    cdf /= cdf[-1]
    return pdf, cdf, med


def main() -> None:
    report: dict[str, object] = {}

    # A. Exact closed-form kappa-concave constants
    M_half_exact = (13.0 - 8.0 * math.sqrt(2.0)) / 3.0
    M_zero_exact = (1.0 + 2.0 * math.log(2.0)) / 4.0
    M_neg1_exact = 0.5 + math.log(3.0) / 8.0
    phi_inv = (math.sqrt(5.0) - 1.0) / 2.0
    grunbaum = 1.0 - math.exp(-1.0)

    assert abs(M_convex_k(1, 1.0) - 0.5) < 1e-12
    assert abs(M_convex_k(2, 1.0) - M_half_exact) < 1e-12
    assert abs(M_convex_k_binomial(2) - M_half_exact) < 1e-12
    assert abs(M_pareto(1.0, 1.0) - M_neg1_exact) < 1e-12
    assert 0.5 < M_half_exact < M_zero_exact < phi_inv < grunbaum < M_neg1_exact < 0.75

    # Verify M(1/k) and M(-1/gamma) maximize at u = 1 across u in [0.05, 20]
    us_chk = np.geomspace(0.05, 20.0, 81)
    convex_table = []
    for k in [1, 2, 3, 4, 5, 6, 10, 20, 50]:
        m1 = M_convex_k(k, 1.0)
        mb = M_convex_k_binomial(k) if k <= 10 else m1
        assert abs(m1 - mb) < 1e-11
        mx = max(M_convex_k(k, float(u)) for u in us_chk)
        assert mx <= m1 + 1e-10
        convex_table.append({"k": k, "kappa": 1.0 / k, "M": m1})

    pareto_table = []
    for gam in [50.0, 10.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.1, 0.02, 0.005]:
        m1 = M_pareto(gam, 1.0)
        mx = max(M_pareto(gam, float(u)) for u in us_chk)
        assert mx <= m1 + 1e-10
        pareto_table.append({"gamma": gam, "kappa": -1.0 / gam, "M": m1})

    # Exact golden-ratio crossing gamma_*
    lo, hi = 1.0, 5.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if M_pareto(mid, 1.0) > phi_inv:
            lo = mid
        else:
            hi = mid
    gamma_gold = 0.5 * (lo + hi)

    report["landmarks"] = {
        "M_1_uniform": 0.5,
        "M_half_2d_convex": M_half_exact,
        "M_0_logconcave": M_zero_exact,
        "golden_ratio_inv": phi_inv,
        "grunbaum_1_minus_inv_e": grunbaum,
        "M_neg1_pareto": M_neg1_exact,
        "M_neginf_unimodal": 0.75,
        "gamma_golden_crossing": gamma_gold,
        "kappa_golden_crossing": -1.0 / gamma_gold,
    }
    report["convex_body_barriers"] = convex_table
    report["pareto_barriers"] = pareto_table

    # B. Exact Quantile Phase Transition lambda_* and q_*
    lo, hi = 0.5, 2.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if (1.0 + 2.0 * mid) * math.exp(-mid) > 1.0:
            lo = mid
        else:
            hi = mid
    lam_star = 0.5 * (lo + hi)
    q_star = 1.0 - math.exp(-lam_star)
    # Verify Theorem 3.1 numerically across lam in [0.2, 2.5]
    us_q = np.geomspace(1e-3, 1e3, 400)
    for lam in [0.4, 0.693147, 0.776732, 1.0, 1.2, lam_star, 1.4, 1.8, 2.5]:
        g1 = G_logconcave(lam, 1.0)
        el = math.exp(-lam)
        mx = max(G_logconcave(lam, float(u)) for u in us_q)
        pred = g1 if lam <= lam_star else el
        assert abs(mx - pred) < 1e-3 if lam > lam_star else mx <= pred + 1e-11

    # C. Exact Exponential-Chain Spectrum (C_3, C_4, ..., C_inf) + One-Sided Limit
    lo, hi = 0.5, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if (1.0 + (math.e + 2.0) * mid) * math.exp(-2.0 * mid) > 1.0:
            lo = mid
        else:
            hi = mid
    c_star = 0.5 * (lo + hi)
    p_exp_star = (1.0 + 2.0 * c_star) * math.exp(-2.0 * c_star)

    lo, hi = 0.5, 0.6
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if math.e * mid * mid * (-math.log(mid)) <= 1.0 - mid:
            lo = mid
        else:
            hi = mid
    p_exp_pos = 0.5 * (lo + hi)

    chain_table = []
    for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 21, 51, 201]:
        if n % 2 == 1:
            p_val, c_val = solve_odd_exp_chain((n - 1) // 2)
        else:
            p_val = solve_even_exp_chain(n // 2)
            c_val = float("nan")
        usiskin = 1.0 - 1.0 / (4.0 * math.cos(math.pi / (n + 2)) ** 2)
        chain_table.append({"n": n, "p_exp_chain": p_val, "usiskin": usiskin})
    assert abs(chain_table[-1]["p_exp_chain"] - p_exp_star) < 1e-10
    p_c3_exact = chain_table[0]["p_exp_chain"]
    lam3_exact = -math.log(1.0 - p_c3_exact)

    report["quantile_phase_transition"] = {
        "lambda_star": lam_star,
        "q_star": q_star,
        "lambda_3_point_mass": lam3_exact,
        "tau_LC_pt_C3": p_c3_exact,
    }
    report["exponential_chains"] = {
        "c_star": c_star,
        "p_exp_two_sided_limit": p_exp_star,
        "p_exp_one_sided_limit": p_exp_pos,
        "by_n": chain_table,
    }

    # D. Unimodal Zero-Penalty Verification (n = 3..10)
    unimodal_table = []
    for n in [3, 4, 5, 6, 8, 10]:
        p_us = 1.0 - 1.0 / (4.0 * math.cos(math.pi / (n + 2)) ** 2)
        qs = [0.0, 1.0 - p_us]
        for _ in range(2, n):
            qs.append((1.0 - p_us) / (1.0 - qs[-1]))
        assert abs(qs[-1] - p_us) < 1e-10
        eps = 1e-7
        params = [(0.0, eps, 0.0, eps)]
        for k in range(2, n + 1):
            params.append((-float(k - 1), 10.0 ** (4 * (n - k + 1)), qs[k - 1], eps))
        ws = [unimodal_win(*params[i], *params[(i + 1) % n]) for i in range(n)]
        assert abs(min(ws) - p_us) < 1e-6
        unimodal_table.append({"n": n, "usiskin": p_us, "unimodal_min": min(ws), "gap": p_us - min(ws)})
    report["unimodal_usiskin"] = unimodal_table

    # E. Monte Carlo / Random Continuous Log-Concave Stress Test (1,500 median-matched pairs!)
    rng = np.random.default_rng(2026)
    gx = np.linspace(-12.0, 12.0, 1201)
    max_rand_pair = 0.0
    max_rand_c3 = 0.0
    n_pairs = 1500
    for _ in range(n_pairs):
        p1, c1, _ = random_lc_density(rng, gx)
        p2, c2, _ = random_lc_density(rng, gx)
        w12 = float(np.trapezoid(p1 * c2, gx))
        if w12 > max_rand_pair:
            max_rand_pair = w12
        assert w12 <= M_zero_exact + 1e-3, f"Violation: {w12}"
    for _ in range(400):
        ds = [random_lc_density(rng, gx) for _ in range(3)]
        ws = [float(np.trapezoid(ds[i][0] * ds[(i + 1) % 3][1], gx)) for i in range(3)]
        if min(ws) > max_rand_c3:
            max_rand_c3 = min(ws)
        assert min(ws) <= M_zero_exact + 1e-3
    report["random_lc_stress_test"] = {
        "n_median_matched_pairs": n_pairs,
        "max_pair_win": max_rand_pair,
        "theoretical_ceiling_M0": M_zero_exact,
        "n_random_c3_triples": 400,
        "max_c3_min_win": max_rand_c3,
    }

    # F. Odd-Cumulant Edgeworth Asymptotics (m = 1 and m = 2) + Finite-k Flip of Extremal C_3 Triple
    edgeworth_m1 = []
    for k in [5, 10, 25, 50, 100, 250, 500, 1000]:
        t = 2.0 * k
        ex = sum(math.exp(-t + j * math.log(t) - math.lgamma(j + 1)) for j in range(2 * k))
        pr = 0.5 - 1.0 / (6.0 * math.sqrt(math.pi * k))
        edgeworth_m1.append({"k": k, "exact_diff": ex - 0.5, "pred_diff": pr - 0.5, "ratio": (ex - 0.5) / (pr - 0.5)})

    a_m2 = 1.0
    b_m2 = 2.0 ** (1.0 / 3.0)
    var_X = 2.0 * a_m2**2 + b_m2**2
    k5_X = 24.0 * (2.0 * a_m2**5 - b_m2**5)
    coef_m2 = (3.0 / (120.0 * math.sqrt(2.0 * math.pi))) * k5_X / ((var_X + 1.0) ** 2.5)
    edgeworth_m2 = []
    for k in [10, 20, 40, 80, 150, 300]:
        T = 10.0 / math.sqrt(k)
        ts = np.linspace(1e-9, T, 8000)
        phi_X = np.exp(-1j * ts * (2.0 * a_m2 - b_m2)) / (((1.0 - 1j * a_m2 * ts) ** 2) * (1.0 + 1j * b_m2 * ts))
        phi_Z = (phi_X * np.exp(-0.5 * ts**2)) ** k
        ex = 0.5 + float(np.trapezoid(np.imag(phi_Z) / ts, ts)) / math.pi
        pr = 0.5 + coef_m2 / (k ** 1.5)
        edgeworth_m2.append({"k": k, "exact_diff": ex - 0.5, "pred_diff": pr - 0.5, "ratio": (ex - 0.5) / (pr - 0.5)})

    # Check k-fold convolution of the extremal log-concave triple (0, E - lam3, lam3 - E)!
    # P(0 > S_2^{(k)}) = P(Gamma(k,1) < k*lam3) = 1 - sum_{j=0}^{k-1} e^{-k lam3} (k lam3)^j / j!
    # P(S_2^{(k)} > S_3^{(k)}) = P(Gamma(2k,1) > 2*k*lam3) = sum_{j=0}^{2k-1} e^{-2k lam3} (2k lam3)^j / j!
    triple_conv = []
    for k in range(1, 13):
        t1 = k * lam3_exact
        t2 = 2.0 * k * lam3_exact
        p12 = 1.0 - sum(math.exp(-t1 + j * math.log(t1) - math.lgamma(j + 1)) for j in range(k))
        p23 = sum(math.exp(-t2 + j * math.log(t2) - math.lgamma(j + 1)) for j in range(2 * k))
        triple_conv.append({"k": k, "P_1_gt_2": p12, "P_2_gt_3": p23, "P_3_gt_1": p12, "nontransitive": min(p12, p23) > 0.5})
    assert triple_conv[0]["nontransitive"] is True
    assert triple_conv[1]["nontransitive"] is False  # Already flips to transitive at k = 2!!
    report["edgeworth_asymptotics"] = {"m1_kappa3": edgeworth_m1, "m2_kappa5": edgeworth_m2}
    report["extremal_triple_convolution"] = triple_conv

    with open(DATA_DIR / "verification_summary.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # -----------------------------------------------------------------------
    # Generate 3 bespoke 300-DPI journal-grade figures
    # -----------------------------------------------------------------------
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.labelsize": 10.6,
        "axes.titlesize": 11.1,
        "legend.fontsize": 8.4,
        "figure.dpi": 300,
    })

    # Figure 1: (a) Full kappa-concave spectrum M(kappa); (b) Cycle capacity C_n: Unimodal vs Log-Concave
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 4.3))
    # Smooth kappa grid mapped via signed transform u = kappa for kappa >= 0 and -log(1 - kappa) for kappa < 0?
    # Better: plot M(kappa) vs kappa on [-4, 1] cleanly!
    ks_pos = np.linspace(1.0, 40.0, 80)
    kappas_pos = 1.0 / ks_pos
    Ms_pos = []
    for kv in ks_pos:
        a = 2.0 ** (-1.0 / kv)
        nodes, weights = np.polynomial.legendre.leggauss(32)
        t = 2.0 * a - 1.0
        ys = 0.5 * (1.0 - t) * nodes + 0.5 * (1.0 + t)
        ws = 0.5 * (1.0 - t) * weights
        val = (t ** kv) + float(np.sum(ws * kv * (ys ** (kv - 1.0)) * ((2.0 * a - ys) ** kv)))
        Ms_pos.append(val)
    kappas_neg = -np.geomspace(0.01, 4.0, 80)[::-1]
    Ms_neg = [M_pareto(-1.0 / kap, 1.0) for kap in kappas_neg]
    kappas_all = np.concatenate([kappas_neg, [0.0], kappas_pos[::-1]])
    Ms_all = np.concatenate([Ms_neg, [M_zero_exact], Ms_pos[::-1]])

    ax1.plot(kappas_all, Ms_all, "-", color="#1f4e79", lw=2.2, label=r"Sharp barrier $M(\kappa)$")
    ax1.axhline(phi_inv, color="#b2182b", ls="--", lw=1.4, label=r"Golden ratio $\phi^{-1} \approx 0.6180$")
    ax1.axhline(grunbaum, color="#762a83", ls=":", lw=1.4, label=r"Grünbaum $1 - e^{-1} \approx 0.6321$")
    ax1.axhline(0.75, color="#555555", ls="-.", lw=1.2, label=r"Unimodal / Trybuła ceiling $3/4$")
    pts_lm = [
        (1.0, 0.5, r"$\kappa=1$: $1/2$", (0.28, 0.503)),
        (0.5, M_half_exact, r"$\kappa=\frac{1}{2}$: $\frac{13-8\sqrt{2}}{3}$", (-0.82, 0.526)),
        (0.0, M_zero_exact, r"$\kappa=0$: $\frac{1+2\ln 2}{4}$", (-1.35, 0.572)),
        (-1.0, M_neg1_exact, r"$\kappa=-1$: $\frac{1}{2}+\frac{\ln 3}{8}$", (-2.85, 0.648)),
    ]
    for kx, my, lbl, txtpos in pts_lm:
        ax1.scatter([kx], [my], color="#b2182b", s=42, zorder=6)
        ax1.annotate(lbl, xy=(kx, my), xytext=txtpos,
                     arrowprops=dict(arrowstyle="->", color="#222222", lw=0.85), fontsize=8.3)
    ax1.scatter([-1.0 / gamma_gold], [phi_inv], color="#1b7837", marker="D", s=40, zorder=6)
    ax1.set_xlabel(r"Borell concavity index $\kappa$ ($\kappa=0$: log-concave)")
    ax1.set_ylabel(r"Sharp median-crossing barrier $M(\kappa)$")
    ax1.set_title(r"(a) Universal $\kappa$-Concave Barrier Spectrum $M(\kappa)$")
    ax1.set_xlim(-4.1, 1.15)
    ax1.set_ylim(0.485, 0.765)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper right", frameon=True, framealpha=0.94, fontsize=7.9)

    # Panel (b): Cycle length n = 3..25
    ns_plot = np.arange(3, 26)
    y_us = [1.0 - 1.0 / (4.0 * math.cos(math.pi / (n + 2)) ** 2) for n in ns_plot]
    y_exp = [solve_odd_exp_chain((int(n) - 1) // 2)[0] if n % 2 == 1 else solve_even_exp_chain(int(n) // 2) for n in ns_plot]
    ax2.plot(ns_plot, y_us, "o-", color="#b2182b", lw=1.9, ms=4.2, label=r"Unimodal & general: $1 - \frac{1}{4\cos^2(\pi/(n+2))}$")
    ax2.axhline(grunbaum, color="#762a83", ls=":", lw=1.4, label=r"Grünbaum LC bound $1 - e^{-1} \approx 0.6321$")
    ax2.axhline(M_zero_exact, color="#1f4e79", ls="--", lw=2.0, label=r"Universal LC barrier $\frac{1+2\ln 2}{4} \approx 0.5966$")
    ax2.plot(ns_plot, y_exp, "s-", color="#1b7837", lw=1.8, ms=4.0, label=r"Two-sided Exp chain ($0.5401 \to 0.5491$)")
    ax2.axhline(p_exp_pos, color="#d95f02", ls="-.", lw=1.4, label=r"One-sided Exp limit $p_{\mathrm{Exp}}^+ \approx 0.5195$")
    ax2.fill_between(ns_plot, y_exp, M_zero_exact, color="#1f4e79", alpha=0.09)
    ax2.set_xlabel(r"Directed cycle length $n$")
    ax2.set_ylabel(r"Steinhaus–Trybuła cycle margin $\tau(C_n)$")
    ax2.set_title(r"(b) Unimodal Zero-Penalty vs. Log-Concave Rigidity")
    ax2.set_xlim(2.5, 25.5)
    ax2.set_ylim(0.505, 0.765)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="center right", frameon=True, framealpha=0.95, fontsize=7.8)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_kappa_concave_spectrum.png", dpi=300)
    plt.close(fig)

    # Figure 2: Log-Concave Quantile Phase Transition at q_* = 1 - exp(-lam_*) ~ 0.7153
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 4.2))
    qs = np.linspace(0.05, 0.96, 300)
    lams = -np.log(1.0 - qs)
    y_sym = (1.0 + 2.0 * lams) * np.exp(-2.0 * lams)
    y_col = 1.0 - qs
    y_exact = np.where(qs <= q_star, y_sym, y_col)

    ax1.plot(qs, y_sym, "--", color="#1f4e79", lw=1.5, label=r"Equal-scale branch $(1-q)^2(1-2\ln(1-q))$")
    ax1.plot(qs, y_col, ":", color="#b2182b", lw=1.6, label=r"Scale-collapse branch $1 - q$")
    ax1.plot(qs, y_exact, "-", color="#111111", lw=2.3, label=r"Exact supremum $\sup \mathbb{P}(X > Y)$")
    ax1.axvline(q_star, color="#1b7837", ls="-.", lw=1.3)
    ax1.scatter([0.5, q_star], [M_zero_exact, 1.0 - q_star], color=["#1f4e79", "#1b7837"], s=48, zorder=6)
    ax1.annotate(r"Median $q=\frac{1}{2}$: $\frac{1+2\ln 2}{4}$", xy=(0.5, M_zero_exact), xytext=(0.14, 0.44),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=0.85), fontsize=8.4)
    ax1.annotate(rf"Phase transition $q_* \approx {q_star:.4f}$", xy=(q_star, 1.0 - q_star), xytext=(0.24, 0.14),
                 arrowprops=dict(arrowstyle="->", color="#1b7837", lw=0.9), fontsize=8.4)
    ax1.set_xlabel(r"Quantile level $q = F_X(0) = S_Y(0)$")
    ax1.set_ylabel(r"Sharp crossing probability $\sup \mathbb{P}(X > Y)$")
    ax1.set_title(r"(a) Exact Quantile-Crossing Phase Transition")
    ax1.set_xlim(0.04, 0.98)
    ax1.set_ylim(0.0, 1.02)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper right", frameon=True, framealpha=0.95, fontsize=8.0)

    # Panel (b): G(lam, lam; u) vs log10(u) across lam below, at, and above lam_*
    log_u = np.linspace(-2.0, 2.0, 300)
    u_grid = 10.0 ** log_u
    for lv, col, lbl in [
        (math.log(2.0), "#1f4e79", r"$\lambda = \ln 2 \approx 0.693$ (median)"),
        (1.0, "#762a83", r"$\lambda = 1.000 < \lambda_*$"),
        (lam_star, "#1b7837", rf"$\lambda = \lambda_* \approx {lam_star:.3f}$ (critical)"),
        (1.5, "#b2182b", r"$\lambda = 1.500 > \lambda_*$ (collapse)"),
    ]:
        vals = [G_logconcave(lv, float(u)) / math.exp(-lv) for u in u_grid]
        ax2.plot(log_u, vals, "-", color=col, lw=1.9, label=lbl)
    ax2.axhline(1.0, color="#555555", ls=":", lw=1.2)
    ax2.axvline(0.0, color="#555555", ls=":", lw=1.0)
    ax2.set_xlabel(r"Log scale ratio $\log_{10}(u)$ ($u = 1$ at $0$)")
    ax2.set_ylabel(r"Normalized crossing $G(\lambda, \lambda; u) / e^{-\lambda}$")
    ax2.set_title(r"(b) Symmetry Breaking from $u = 1$ to $u \to 0^+, \infty$")
    ax2.set_xlim(-2.0, 2.0)
    ax2.set_ylim(0.84, 1.24)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="upper right", frameon=True, framealpha=0.95, fontsize=8.0)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_quantile_phase_transition.png", dpi=300)
    plt.close(fig)

    # Figure 3: Convolution Transitivity Collapse & Odd-Cumulant Edgeworth Rates
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 4.2))
    ks_tr = [row["k"] for row in triple_conv]
    p12s = [row["P_1_gt_2"] for row in triple_conv]
    p23s = [row["P_2_gt_3"] for row in triple_conv]
    ax1.plot(ks_tr, p23s, "o-", color="#b2182b", lw=2.0, ms=5.0, label=r"$\mathbb{P}(S_2^{(k)} > S_3^{(k)})$ (mean $+ > -$)")
    ax1.plot(ks_tr, p12s, "s-", color="#1f4e79", lw=2.0, ms=5.0, label=r"$\mathbb{P}(S_1^{(k)} > S_2^{(k)}) = \mathbb{P}(S_3^{(k)} > S_1^{(k)})$")
    ax1.axhline(0.5, color="#333333", ls="--", lw=1.3, label=r"Transitivity threshold $1/2$")
    ax1.axvspan(0.7, 1.5, color="#b2182b", alpha=0.10, label="Non-transitive ($k=1$ only)")
    ax1.set_xlabel(r"Number of i.i.d. convolved copies $k$")
    ax1.set_ylabel(r"Pairwise win probability")
    ax1.set_title(r"(a) Convolution Collapse of Extremal Triple $(0, E-\lambda_3, \lambda_3-E)$")
    ax1.set_xticks(ks_tr)
    ax1.set_xlim(0.7, 12.3)
    ax1.set_ylim(0.0, 1.02)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="center right", frameon=True, framealpha=0.95, fontsize=8.0)

    # Panel (b): Log-log plot of |P(S_X^{(k)} > S_Y^{(k)}) - 1/2| for m=1 (k^{-1/2}) and m=2 (k^{-3/2})
    k1s = np.array([r["k"] for r in edgeworth_m1], dtype=float)
    d1_ex = np.abs([r["exact_diff"] for r in edgeworth_m1])
    d1_pr = np.abs([r["pred_diff"] for r in edgeworth_m1])
    k2s = np.array([r["k"] for r in edgeworth_m2], dtype=float)
    d2_ex = np.abs([r["exact_diff"] for r in edgeworth_m2])
    d2_pr = np.abs([r["pred_diff"] for r in edgeworth_m2])

    ax2.loglog(k1s, d1_pr, "--", color="#1f4e79", lw=1.7, label=r"$m=1$ ($\kappa_3 \neq 0$): $\frac{1}{6\sqrt{\pi}} k^{-1/2}$")
    ax2.loglog(k1s, d1_ex, "o", color="#1f4e79", ms=5.5, label=r"$m=1$ exact ($\mathrm{Gamma}(2k) > 2k$)")
    ax2.loglog(k2s, d2_pr, "--", color="#b2182b", lw=1.7, label=r"$m=2$ ($\kappa_1=\kappa_3=0, \kappa_5 \neq 0$): $c_5 k^{-3/2}$")
    ax2.loglog(k2s, d2_ex, "s", color="#b2182b", ms=5.5, label=r"$m=2$ exact (Gil–Pelaez inversion)")
    ax2.set_xlabel(r"Convolved copies $k$")
    ax2.set_ylabel(r"Margin $|\mathbb{P}(S_X^{(k)} > S_Y^{(k)}) - \frac{1}{2}|$")
    ax2.set_title(r"(b) Exact Odd-Cumulant Edgeworth Decay ($k^{-(m-1/2)}$)")
    ax2.grid(True, which="both", alpha=0.25)
    ax2.legend(loc="lower left", frameon=True, framealpha=0.95, fontsize=7.9)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_convolution_transitivity.png", dpi=300)
    plt.close(fig)

    print("VERIFY_LOGCONCAVE_BARRIERS_OK")
    print(f"  M(1/2) = {M_half_exact:.10f}, M(0) = {M_zero_exact:.10f}, M(-1) = {M_neg1_exact:.10f}")
    print(f"  q_* = {q_star:.10f} (lam_* = {lam_star:.10f}), tau_LC^pt(C3) = {p_c3_exact:.10f}")
    print(f"  p_Exp^* = {p_exp_star:.10f}, p_Exp^+ = {p_exp_pos:.10f}, max_rand_pair = {max_rand_pair:.6f}")


if __name__ == "__main__":
    main()
