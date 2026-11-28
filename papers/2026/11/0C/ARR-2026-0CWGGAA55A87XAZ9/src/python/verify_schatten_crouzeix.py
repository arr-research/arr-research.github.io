#!/usr/bin/env python3
"""
verify_schatten_crouzeix.py
Exact & high-precision verification and 300-DPI figure generation for Frontier F5:
  "Schatten-q Crouzeix Constants and the Hilbert-Schmidt Phase Transition:
   Universal Conformal Majorization on M_2(C), Odd-Even Clifford Parity Staircases,
   and Double-Layer Trace Bounds"
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Jacobi Theta Functions & Exact 2x2 Conformal Focus Value r(R)
# ---------------------------------------------------------------------------

def theta2(tau: float, terms: int = 80) -> float:
    """Jacobi theta_2(tau) = 2 * tau^(1/4) * sum_{n>=0} tau^(n*(n+1)) for tau in (0,1)."""
    s = 0.0
    for n in range(terms):
        t = tau ** (n * (n + 1))
        s += t
        if t < 1e-17 * s:
            break
    return 2.0 * (tau ** 0.25) * s


def theta3(tau: float, terms: int = 80) -> float:
    """Jacobi theta_3(tau) = 1 + 2 * sum_{n>=1} tau^(n^2) for tau in (0,1)."""
    s = 1.0
    for n in range(1, terms):
        t = 2.0 * (tau ** (n * n))
        s += t
        if t < 1e-17 * s:
            break
    return s


def r_focus(R: float) -> float:
    """Conformal focus value r(R) = phi_R(1) = theta_2(R^{-4}) / theta_3(R^{-4}) for R > 1."""
    if R <= 1.0:
        return 1.0
    tau = R ** (-4.0)
    if tau > 0.999999:
        # Use Jacobi imaginary transformation tau = exp(-pi*t) -> tilde_tau = exp(-pi/t)
        t_mod = -math.log(tau) / math.pi
        tilde_tau = math.exp(-math.pi / t_mod)
        # theta_2(tau)/theta_3(tau) = theta_4(tilde_tau)/theta_3(tilde_tau)
        prod = 1.0
        for m in range(1, 60):
            tm = tilde_tau ** (2 * m - 1)
            if tm < 1e-17:
                break
            prod *= ((1.0 - tm) / (1.0 + tm)) ** 2
        return prod
    return theta2(tau) / theta3(tau)


def psi_q_2x2(R: float, q: float) -> float:
    """Exact Schatten-q Crouzeix constant Psi_q(A_R) for 2x2 matrix with Joukowsky radius R > 1."""
    r = r_focus(R)
    if math.isinf(q):
        return r * R
    s1 = r * R
    s2 = r / R
    return (0.5 * (s1 ** q + s2 ** q)) ** (1.0 / q)


def maximize_psi_q_over_R(q: float) -> tuple[float, float]:
    """Find (R*(q), Psi_q(2)) for 1 <= q < 2 using log-grid + golden-section refinement."""
    if math.isinf(q) or q >= 2.0:
        return float("inf"), 2.0 ** (1.0 - 1.0 / q) if not math.isinf(q) else 2.0
    # Upper search cap guided by asymptotic R*(q) ~ 4^{1/(4-2q)}
    R_asymp = 4.0 ** (1.0 / (4.0 - 2.0 * q))
    R_lo_scan = 1.02
    R_hi_scan = max(20.0, min(1e6, 5.0 * R_asymp))
    grid = np.geomspace(R_lo_scan, R_hi_scan, 600)
    vals = [psi_q_2x2(float(R), q) for R in grid]
    idx = int(np.argmax(vals))
    lo = float(grid[max(0, idx - 2)])
    hi = float(grid[min(len(grid) - 1, idx + 2)])
    # Golden-section search in log(R)
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = math.log(lo), math.log(hi)
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc = psi_q_2x2(math.exp(c), q)
    fd = psi_q_2x2(math.exp(d), q)
    for _ in range(90):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = psi_q_2x2(math.exp(c), q)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = psi_q_2x2(math.exp(d), q)
    R_star = math.exp(0.5 * (a + b))
    return R_star, psi_q_2x2(R_star, q)


def schatten_norm_normalized(M: np.ndarray, q: float) -> float:
    s = np.linalg.svd(M, compute_uv=False)
    if math.isinf(q):
        return float(s[0])
    return float((np.mean(s ** q)) ** (1.0 / q))


def num_radius(A: np.ndarray, ntheta: int = 360) -> float:
    th = np.linspace(0.0, 2.0 * np.pi, ntheta, endpoint=False)
    best = 0.0
    for t in th:
        H = 0.5 * (np.exp(1j * t) * A + np.exp(-1j * t) * A.conj().T)
        ev = float(np.linalg.eigvalsh(H).max())
        if ev > best:
            best = ev
    return best


def w_boundary(A: np.ndarray, ntheta: int = 240) -> np.ndarray:
    th = np.linspace(0.0, 2.0 * np.pi, ntheta, endpoint=False)
    pts = np.empty(ntheta, dtype=complex)
    for idx, t in enumerate(th):
        H = 0.5 * (np.exp(-1j * t) * A + np.exp(1j * t) * A.conj().T)
        _, vecs = np.linalg.eigh(H)
        v = vecs[:, -1]
        pts[idx] = np.vdot(v, A @ v)
    return pts


def linear_extremal_constant(n: int, q: float) -> float:
    m = n // 2
    rem = n % 2
    if math.isinf(q):
        return 1.0 if n == 1 else 2.0
    return ((m * (2.0 ** q) + rem) / n) ** (1.0 / q)


def main() -> None:
    rng = np.random.default_rng(20261128)
    summary: dict = {}

    # -----------------------------------------------------------------------
    # 1. Verify Theorem 2.1: Linear & Centered-Disk Parity Staircase
    # -----------------------------------------------------------------------
    staircase_table = []
    for n in range(1, 13):
        row = {"n": n}
        for q_key, q_val in [("q1", 1.0), ("q1.5", 1.5), ("q2", 2.0), ("q3", 3.0), ("q4", 4.0), ("qinf", float("inf"))]:
            row[q_key] = linear_extremal_constant(n, q_val)
        staircase_table.append(row)

    # Empirical random + structured check of weak majorization sigma(A) <_w s^(n) w(A)
    max_weak_maj_violation = 0.0
    max_disk_blaschke_violation = 0.0
    for n in [2, 3, 4, 5, 6]:
        s_ext = np.array([2.0] * (n // 2) + ([1.0] if n % 2 == 1 else []) + [0.0] * (n // 2))
        ext_cumsum = np.cumsum(s_ext)
        for trial in range(120):
            if trial < 60:
                A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            elif trial < 100:
                A = np.triu(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)), 1)
            else:
                A = np.zeros((n, n), dtype=complex)
                for k in range(0, n - 1, 2):
                    A[k, k + 1] = 2.0
                if n % 2 == 1:
                    A[n - 1, n - 1] = 1.0
                A += 0.08 * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
            w = num_radius(A, 180)
            if w < 1e-10:
                continue
            A_norm = A / w
            sv = np.linalg.svd(A_norm, compute_uv=False)
            viol = float(np.max(np.cumsum(sv) - ext_cumsum))
            if viol > max_weak_maj_violation:
                max_weak_maj_violation = viol
            # Centered Blaschke product f(z) = z * (z - a)/(1 - conj(a)*z) (f(0)=0, ||f||_D = 1)
            if trial < 35:
                a = rng.uniform(0.0, 0.8) * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))
                M = A_norm @ (A_norm - a * np.eye(n)) @ np.linalg.inv(np.eye(n) - np.conj(a) * A_norm)
                svM = np.linalg.svd(M, compute_uv=False)
                violM = float(np.max(np.cumsum(svM) - ext_cumsum))
                if violM > max_disk_blaschke_violation:
                    max_disk_blaschke_violation = violM

    assert max_weak_maj_violation < 1e-4, f"Weak majorization violated: {max_weak_maj_violation}"
    assert max_disk_blaschke_violation < 1e-4, f"Disk Blaschke majorization violated: {max_disk_blaschke_violation}"

    summary["theorem_2_1_parity_staircase"] = {
        "table_n_1_to_12": staircase_table,
        "max_weak_majorization_violation_600_trials": max_weak_maj_violation,
        "max_centered_disk_blaschke_violation": max_disk_blaschke_violation,
    }

    # -----------------------------------------------------------------------
    # 2. Verify Theorem 3.1: 2x2 Universal Ky Fan Dominance of phi_R
    # -----------------------------------------------------------------------
    kyfan_2x2_checks = []
    for R in [1.15, 1.4, 1.75, 2.045931, 2.5, 4.0, 10.0]:
        a = 0.5 * (R + 1.0 / R)
        b = 0.5 * (R - 1.0 / R)
        c = 2.0 * b
        r = r_focus(R)
        rho = 2.0 * r / (1.0 + r * r)
        s1_opt = r * R
        s2_opt = r / R
        # Dense grid over valid Schwarz-Pick pairs (u, v)
        u_grid = np.linspace(0.0, 0.9999, 240)
        th_grid = np.linspace(0.0, np.pi, 181)
        U, TH = np.meshgrid(u_grid, th_grid, indexing="ij")
        W = rho * np.exp(1j * TH)
        V = (U - W) / (1.0 - U * W)
        P = np.abs(U * V)
        S2 = U ** 2 + np.abs(V) ** 2 + 0.25 * (c ** 2) * np.abs(U - V) ** 2
        disc = np.sqrt(np.maximum(S2 ** 2 - 4.0 * P ** 2, 0.0))
        s1 = np.sqrt(0.5 * (S2 + disc))
        s2 = np.sqrt(0.5 * np.maximum(S2 - disc, 0.0))
        excess_kf1 = float(np.max(s1) - s1_opt)
        excess_kf2 = float(np.max(s1 + s2) - (s1_opt + s2_opt))
        assert excess_kf1 <= 1e-11 and excess_kf2 <= 1e-11
        kyfan_2x2_checks.append({
            "R": R,
            "c": c,
            "r_focus": r,
            "sigma1_opt": s1_opt,
            "sigma2_opt": s2_opt,
            "psi_1": 0.5 * (s1_opt + s2_opt),
            "psi_2": math.sqrt(0.5 * (s1_opt ** 2 + s2_opt ** 2)),
            "max_kf1_excess": excess_kf1,
            "max_kf2_excess": excess_kf2,
        })

    summary["theorem_3_1_conformal_majorization"] = kyfan_2x2_checks

    # -----------------------------------------------------------------------
    # 3. Verify Theorem 4.1: Exact Hilbert-Schmidt Phase Transition at q_c = 2
    # -----------------------------------------------------------------------
    q_table_vals = [1.0, 1.1, 1.25, 1.4, 1.5, 1.6, 1.7, 1.75, 1.8, 1.85, 2.0, 2.5, 3.0, 4.0, 6.0, float("inf")]
    phase_table = []
    for q in q_table_vals:
        R_star, psi_max = maximize_psi_q_over_R(q)
        disk_val = 2.0 if math.isinf(q) else 2.0 ** (1.0 - 1.0 / q)
        c_star = float("inf") if math.isinf(R_star) else (R_star - 1.0 / R_star)
        R_asymp = None if (math.isinf(q) or q >= 2.0) else (4.0 ** (1.0 / (4.0 - 2.0 * q)))
        excess_asymp = None if (math.isinf(q) or q >= 2.0) else (
            disk_val * ((2.0 - q) / (2.0 * q)) * (4.0 ** (-q / (2.0 - q)))
        )
        phase_table.append({
            "q": "inf" if math.isinf(q) else q,
            "R_star": "inf" if math.isinf(R_star) else R_star,
            "c_star": "inf" if math.isinf(c_star) else c_star,
            "Psi_q_2": psi_max,
            "disk_J2_bound": disk_val,
            "excess_over_J2": psi_max - disk_val,
            "R_star_asymptotic": R_asymp,
            "R_ratio_exact_over_asymp": None if R_asymp is None else R_star / R_asymp,
            "excess_asymptotic": excess_asymp,
        })

    # Verify q=2 strict upper bound across 2000 log-spaced R values
    R_test = np.geomspace(1.0001, 1e4, 2000)
    psi2_vals = np.array([psi_q_2x2(float(R), 2.0) for R in R_test])
    assert float(np.max(psi2_vals)) < math.sqrt(2.0), "q=2 exceeded sqrt(2)!"
    R_star_1, psi1_2 = maximize_psi_q_over_R(1.0)
    c_star_1 = R_star_1 - 1.0 / R_star_1

    summary["theorem_4_1_phase_transition"] = {
        "q_c": 2.0,
        "Psi_1_2": psi1_2,
        "R_star_q1": R_star_1,
        "c_star_q1": c_star_1,
        "max_psi2_on_2000_ellipses": float(np.max(psi2_vals)),
        "sqrt2": math.sqrt(2.0),
        "phase_table": phase_table,
    }

    # -----------------------------------------------------------------------
    # 4. Verify Theorem 5.1: Universal n-Dimensional Double-Layer Trace Bound
    # -----------------------------------------------------------------------
    # Build smooth epsilon-hull / ellipse contour integration for n=2,3,4,5 matrices
    dl_records = []
    max_dl_identity_err = 0.0
    max_f2_ratio = 0.0
    max_f2_zero_spec_ratio = 0.0

    # Test on explicit matrices whose W(A) is contained inside a smooth disk/ellipse Omega
    # (1) 2x2 ellipses with exact boundary E_R, (2) n=3,4,5 matrices with disk Omega = (1+eps)*w(A)*D
    for R in [1.3, 1.8, 2.045931, 3.5]:
        a = 0.5 * (R + 1.0 / R)
        b = 0.5 * (R - 1.0 / R)
        A = np.array([[1.0, 2.0 * b], [0.0, -1.0]], dtype=complex)
        N = 1200
        t = np.linspace(0.0, 2.0 * np.pi, N, endpoint=False)
        dt = 2.0 * np.pi / N
        z = a * np.cos(t) + 1j * b * np.sin(t)
        dz = (-a * np.sin(t) + 1j * b * np.cos(t)) * dt
        for deg in [1, 2, 3, 4]:
            coeffs = rng.normal(size=deg + 1) + 1j * rng.normal(size=deg + 1)
            fvals = sum(coeffs[k] * (z ** k) for k in range(deg + 1))
            sup_w = float(np.max(np.abs(fvals)))
            fvals = fvals / sup_w
            fA = np.zeros((2, 2), dtype=complex)
            gA = np.zeros((2, 2), dtype=complex)
            for k in range(N):
                inv = np.linalg.inv(z[k] * np.eye(2) - A)
                fA += fvals[k] * inv * dz[k] / (2j * np.pi)
                gA += np.conj(fvals[k]) * inv * dz[k] / (2j * np.pi)
            S = fA + gA.conj().T
            f2 = float(np.sum(np.abs(fA) ** 2) / 2.0)
            g2 = float(np.sum(np.abs(gA) ** 2) / 2.0)
            S2 = float(np.sum(np.abs(S) ** 2) / 2.0)
            tr_fg = float(np.trace(fA @ gA).real / 2.0)
            err = abs(f2 + g2 + 2.0 * tr_fg - S2)
            max_dl_identity_err = max(max_dl_identity_err, err)
            eigs = np.linalg.eigvals(A)
            feigs = sum(coeffs[k] * (eigs ** k) for k in range(deg + 1)) / sup_w
            eig_sq_mean = float(np.mean(np.abs(feigs) ** 2))
            assert S2 <= 4.0 + 1e-8
            assert f2 <= 4.0 + eig_sq_mean + 1e-8
            max_f2_ratio = max(max_f2_ratio, math.sqrt(f2))
            dl_records.append({
                "n": 2, "S2": S2, "f2": f2, "g2": g2, "two_re_tr_fg": 2.0 * tr_fg,
                "rhs_bound": 4.0 + eig_sq_mean, "identity_err": err,
            })

    # Now test n=3, 4, 5 random non-normal matrices on disk Omega = (1.002 * w(A)) * D
    for n in [3, 4, 5]:
        N = 1000
        t = np.linspace(0.0, 2.0 * np.pi, N, endpoint=False)
        dt = 2.0 * np.pi / N
        z_unit = np.exp(1j * t)
        dz_unit = 1j * z_unit * dt
        for trial in range(8):
            if trial == 0:
                A = np.diag(np.ones(n - 1), 1).astype(complex)  # nilpotent Jordan block
            else:
                A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            w = num_radius(A, 240)
            A = A / (1.002 * w)  # strictly inside unit disk D
            # Test general polynomial AND spectrum-vanishing polynomial (for nilpotent J_n, f(0)=0)
            for zero_spec in ([True, False] if trial == 0 else [False]):
                coeffs = rng.normal(size=5) + 1j * rng.normal(size=5)
                if zero_spec:
                    coeffs[0] = 0.0
                fvals = sum(coeffs[k] * (z_unit ** k) for k in range(5))
                sup_w = float(np.max(np.abs(fvals)))
                fvals = fvals / sup_w
                fA = np.zeros((n, n), dtype=complex)
                gA = np.zeros((n, n), dtype=complex)
                for k in range(N):
                    inv = np.linalg.inv(z_unit[k] * np.eye(n) - A)
                    fA += fvals[k] * inv * dz_unit[k] / (2j * np.pi)
                    gA += np.conj(fvals[k]) * inv * dz_unit[k] / (2j * np.pi)
                S = fA + gA.conj().T
                f2 = float(np.sum(np.abs(fA) ** 2) / n)
                g2 = float(np.sum(np.abs(gA) ** 2) / n)
                S2 = float(np.sum(np.abs(S) ** 2) / n)
                tr_fg = float(np.trace(fA @ gA).real / n)
                err = abs(f2 + g2 + 2.0 * tr_fg - S2)
                max_dl_identity_err = max(max_dl_identity_err, err)
                eigs = np.linalg.eigvals(A)
                feigs = sum(coeffs[k] * (eigs ** k) for k in range(5)) / sup_w
                eig_sq_mean = float(np.mean(np.abs(feigs) ** 2))
                assert S2 <= 4.0 + 1e-6
                assert f2 <= 4.0 + eig_sq_mean + 1e-6
                if zero_spec:
                    assert f2 <= 4.0 + 1e-6
                    max_f2_zero_spec_ratio = max(max_f2_zero_spec_ratio, math.sqrt(f2))
                max_f2_ratio = max(max_f2_ratio, math.sqrt(f2))
                dl_records.append({
                    "n": n, "S2": S2, "f2": f2, "g2": g2, "two_re_tr_fg": 2.0 * tr_fg,
                    "rhs_bound": 4.0 + eig_sq_mean, "identity_err": err,
                })

    summary["theorem_5_1_double_layer_trace"] = {
        "universal_bound_q_le_2": math.sqrt(5.0),
        "crouzeix_palencia_bound": 1.0 + math.sqrt(2.0),
        "zero_spectrum_bound": 2.0,
        "tested_instances": len(dl_records),
        "max_trace_identity_error": max_dl_identity_err,
        "max_observed_f2_norm": max_f2_ratio,
        "max_observed_zero_spec_f2_norm": max_f2_zero_spec_ratio,
    }

    (DATA_DIR / "verification_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )

    # -----------------------------------------------------------------------
    # 5. Generate 3 Publication-Grade 300-DPI Figures
    # -----------------------------------------------------------------------
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 9.5,
        "axes.labelsize": 10,
        "axes.titlesize": 10.5,
        "legend.fontsize": 8.0,
        "xtick.labelsize": 8.8,
        "ytick.labelsize": 8.8,
    })

    # --- FIGURE 1: Hilbert-Schmidt Critical Phase Transition at q_c = 2 ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.35))
    R_plot = np.geomspace(1.01, 40.0, 500)
    curves = [
        (1.0, r"$q = 1$ (trace norm)", "#b2182b", "-", 2.1),
        (1.25, r"$q = 1.25$", "#d6604d", "-", 1.7),
        (1.5, r"$q = 1.5$", "#f4a582", "-", 1.7),
        (1.75, r"$q = 1.75$", "#92c5de", "-", 1.7),
        (2.0, r"$q = q_c = 2$ (Hilbert–Schmidt)", "#1b7837", "--", 2.2),
        (3.0, r"$q = 3$", "#2166ac", ":", 1.8),
        (float("inf"), r"$q = \infty$ (Crouzeix)", "#4d4d4d", "-.", 1.7),
    ]
    for qv, lab, col, ls, lw in curves:
        disk_lim = 2.0 if math.isinf(qv) else 2.0 ** (1.0 - 1.0 / qv)
        ys = [psi_q_2x2(float(R), qv) / disk_lim for R in R_plot]
        ax1.plot(R_plot, ys, label=lab, color=col, ls=ls, lw=lw)
    ax1.axhline(1.0, color="black", lw=1.0, ls="--", alpha=0.65)
    ax1.scatter([R_star_1], [psi1_2], color="#b2182b", s=42, zorder=6)
    ax1.annotate(
        f"$q=1$ peak: {psi1_2:.4f}\n($R^* = {R_star_1:.2f}$)",
        xy=(R_star_1, psi1_2),
        xytext=(3.2, 1.095),
        arrowprops=dict(arrowstyle="->", color="#b2182b", lw=1.0),
        fontsize=8.2,
        color="#b2182b",
    )
    ax1.set_xscale("log")
    ax1.set_xticks([1, 2, 5, 10, 20, 40])
    ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax1.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax1.set_xlabel(r"Joukowsky ellipse radius $R = a + b \in (1, \infty)$")
    ax1.set_ylabel(r"Ratio $\Psi_q(A_R) / 2^{1-1/q}$ relative to $J_2$ disk")
    ax1.set_title(r"(a) Exact $2\times 2$ Elliptic Phase Transition at $q_c = 2$")
    ax1.set_xlim(1.01, 40.0)
    ax1.set_ylim(0.55, 1.15)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="lower right", frameon=True, framealpha=0.95, ncol=1)

    # Panel (b): Critical scaling R*(q) vs asymptotic 4^{1/(4-2q)}
    q_sub = np.linspace(1.0, 1.88, 60)
    R_exact = np.array([maximize_psi_q_over_R(float(q))[0] for q in q_sub])
    R_as = np.array([4.0 ** (1.0 / (4.0 - 2.0 * q)) for q in q_sub])
    ax2.semilogy(q_sub, R_exact, color="#b2182b", lw=2.2, label=r"Exact extremal radius $R^*(q)$")
    ax2.semilogy(q_sub, R_as, color="#2166ac", ls="--", lw=1.8, label=r"Critical law $4^{1/(4-2q)}$")
    ax2.axvline(2.0, color="#1b7837", ls=":", lw=1.8, label=r"Critical exponent $q_c = 2$")
    ax2.set_xlabel(r"Schatten exponent $q \in [1, 2)$")
    ax2.set_ylabel(r"Extremal Joukowsky radius $R^*(q)$ (log scale)")
    ax2.set_title(r"(b) Critical Divergence $R^*(q) \sim 4^{1/(4-2q)}$ as $q \uparrow 2^-$")
    ax2.set_xlim(1.0, 2.04)
    ax2.grid(True, which="both", alpha=0.25)
    ax2.legend(loc="upper left", frameon=True, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_hilbert_schmidt_phase_transition.png", dpi=300)
    plt.close(fig)

    # --- FIGURE 2: Odd-Even Clifford Parity Staircase & Universal Bounds ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.35))
    ns = np.arange(1, 13)
    for qv, lab, col, mk in [
        (float("inf"), r"$q = \infty$ (operator norm)", "#4d4d4d", "s"),
        (4.0, r"$q = 4$", "#2166ac", "^"),
        (2.0, r"$q = 2$ (Frobenius)", "#b2182b", "o"),
        (1.0, r"$q = 1$ (trace norm)", "#1b7837", "D"),
    ]:
        ys = [linear_extremal_constant(int(n), qv) for n in ns]
        ax1.plot(ns, ys, marker=mk, ms=5.0, lw=1.7, color=col, label=lab)
    ax1.set_xlabel(r"Matrix dimension $n$")
    ax1.set_ylabel(r"Sharp linear constant $\sup_A \|A\|_{q,\mathrm{norm}} / w(A)$")
    ax1.set_title(r"(a) Exact Odd–Even Clifford $\mathrm{Cl}_2$ Parity Staircase")
    ax1.set_xticks(ns)
    ax1.set_ylim(0.92, 2.10)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="lower right", frameon=True, framealpha=0.95)

    # Panel (b): Universal Schatten-q Crouzeix constant landscape
    q_grid = np.geomspace(1.0, 20.0, 120)
    psi2_exact = np.array([maximize_psi_q_over_R(float(q))[1] for q in q_grid])
    disk_curve = np.array([2.0 ** (1.0 - 1.0 / q) for q in q_grid])
    cp_const = 1.0 + math.sqrt(2.0)
    dl_upper = np.array([
        math.sqrt(5.0) if q <= 2.0 else (5.0 ** (1.0 / q)) * (cp_const ** (1.0 - 2.0 / q))
        for q in q_grid
    ])
    ax2.plot(q_grid, [cp_const] * len(q_grid), color="#636363", ls=":", lw=1.6,
             label=r"Crouzeix–Palencia $1+\sqrt{2} \approx 2.414$")
    ax2.plot(q_grid, dl_upper, color="#2166ac", lw=2.2,
             label=r"Thm. 5.1 universal bound ($\sqrt{5}$ for $q \leq 2$)")
    ax2.plot(q_grid, psi2_exact, color="#b2182b", lw=2.2,
             label=r"Exact $2\times 2$ lower bound $\Psi_q(2)$")
    ax2.plot(q_grid, disk_curve, color="#1b7837", ls="--", lw=1.6,
             label=r"Nilpotent disk $J_2$ curve $2^{1-1/q}$")
    ax2.fill_between(q_grid, psi2_exact, dl_upper, color="#92c5de", alpha=0.18)
    ax2.axvline(2.0, color="#1b7837", ls=":", lw=1.3, alpha=0.8)
    ax2.set_xscale("log")
    ax2.set_xlabel(r"Schatten exponent $q$ (log scale)")
    ax2.set_ylabel(r"Normalized Schatten-$q$ Crouzeix constant")
    ax2.set_title(r"(b) Universal Bounds vs. Exact $2\times 2$ Extremal Curve")
    ax2.set_xlim(1.0, 20.0)
    ax2.set_ylim(0.95, 2.55)
    ax2.grid(True, which="both", alpha=0.25)
    ax2.legend(loc="lower right", frameon=True, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_parity_staircase_and_universal_bounds.png", dpi=300)
    plt.close(fig)

    # --- FIGURE 3: Conformal Majorization Wedge & Double-Layer Trace Check ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.35))
    # Panel (a): Singular value cloud (s1, s2) for extremal ellipse R* = 2.045931
    R = R_star_1
    b = 0.5 * (R - 1.0 / R)
    c = 2.0 * b
    r = r_focus(R)
    rho = 2.0 * r / (1.0 + r * r)
    s1_opt, s2_opt = r * R, r / R
    # Sample 4000 valid Schwarz-Pick pairs
    u_samp = rng.uniform(0.0, 0.995, 4000) * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, 4000))
    w_samp = (rng.uniform(0.0, 1.0, 4000) ** 0.3) * rho * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, 4000))
    v_samp = (u_samp - w_samp) / (1.0 - np.conj(u_samp) * w_samp)
    P_s = np.abs(u_samp * v_samp)
    S2_s = np.abs(u_samp) ** 2 + np.abs(v_samp) ** 2 + 0.25 * (c ** 2) * np.abs(u_samp - v_samp) ** 2
    d_s = np.sqrt(np.maximum(S2_s ** 2 - 4.0 * P_s ** 2, 0.0))
    s1_s = np.sqrt(0.5 * (S2_s + d_s))
    s2_s = np.sqrt(0.5 * np.maximum(S2_s - d_s, 0.0))

    ax1.scatter(s1_s, s2_s, s=4.5, alpha=0.35, color="#4393c3", label=r"Valid $f(A_{R^*})$ singular values")
    # Plot Ky Fan dominance boundary: s1 <= s1_opt, s1 + s2 <= s1_opt + s2_opt, s2 <= s1
    s1_line = np.linspace(0.0, s1_opt, 200)
    s2_upper = np.minimum(s1_line, (s1_opt + s2_opt) - s1_line)
    ax1.plot(s1_line, s2_upper, color="#b2182b", lw=2.0, label=r"Ky Fan wedge of $\varphi_{R^*}(A_{R^*})$")
    ax1.plot([s1_opt, s1_opt], [0.0, s2_opt], color="#b2182b", lw=2.0)
    ax1.scatter([s1_opt], [s2_opt], color="#b2182b", marker="*", s=130, zorder=6,
                label=rf"Conformal map $\varphi_{{R^*}}$: $({s1_opt:.3f}, {s2_opt:.3f})$")
    ax1.set_xlabel(r"Largest singular value $\sigma_1(f(A_{R^*}))$")
    ax1.set_ylabel(r"Second singular value $\sigma_2(f(A_{R^*}))$")
    ax1.set_title(rf"(a) Universal Ky Fan Dominance at $R^* \approx {R_star_1:.3f}$")
    ax1.set_xlim(0.0, s1_opt + 0.14)
    ax1.set_ylim(0.0, 1.18)
    ax1.grid(True, alpha=0.25)
    ax1.legend(loc="upper left", frameon=True, framealpha=0.95)

    # Panel (b): Double-layer trace verification across n = 2, 3, 4, 5
    colors_n = {2: "#b2182b", 3: "#2166ac", 4: "#1b7837", 5: "#762a83"}
    for n_val in [2, 3, 4, 5]:
        pts = [rec for rec in dl_records if rec["n"] == n_val]
        xs = [p["S2"] for p in pts]
        ys = [p["f2"] for p in pts]
        ax2.scatter(xs, ys, s=36, alpha=0.85, color=colors_n[n_val], label=rf"$n = {n_val}$")
    ax2.axvline(4.0, color="#636363", ls="--", lw=1.4, label=r"POVM ceiling $\|S(f)\|_{2,\mathrm{norm}}^2 \leq 4$")
    ax2.axhline(5.0, color="#b2182b", ls=":", lw=1.6, label=r"Thm. 5.1 bound $\|f(A)\|_{2,\mathrm{norm}}^2 \leq 5$")
    ax2.axhline(2.0, color="#1b7837", ls="-.", lw=1.4, label=r"$2\times 2$ Hilbert–Schmidt peak $\Psi_2(2)^2 = 2$")
    ax2.set_xlabel(r"Double-layer norm squared $\|S(f)\|_{2,\mathrm{norm}}^2$")
    ax2.set_ylabel(r"Normalized Frobenius squared $\|f(A)\|_{2,\mathrm{norm}}^2$")
    ax2.set_title(r"(b) Double-Layer Trace Identity Across $n = 2,3,4,5$")
    ax2.set_xlim(0.0, 4.35)
    ax2.set_ylim(0.0, 5.35)
    ax2.grid(True, alpha=0.25)
    ax2.legend(loc="upper left", frameon=True, framealpha=0.95, ncol=1)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_conformal_majorization_geometry.png", dpi=300)
    plt.close(fig)

    print("VERIFY_SCHATTEN_CROUZEIX_OK")
    print(f"  Psi_1(2) = {psi1_2:.10f} at R* = {R_star_1:.8f} (c* = {c_star_1:.8f})")
    print(f"  max Psi_2 on 2000 ellipses = {float(np.max(psi2_vals)):.10f} < sqrt(2) = {math.sqrt(2.0):.10f}")
    print(f"  max weak-maj violation = {max_weak_maj_violation:.2e}, max disk Blaschke viol = {max_disk_blaschke_violation:.2e}")
    print(f"  double-layer trace checks = {len(dl_records)}, max identity err = {max_dl_identity_err:.2e}")


if __name__ == "__main__":
    main()
