"""Finite diagnostics for the external unitary-distance consequence.

Run: python check_unitary_distance.py [--out results.json]
Dependencies: numpy, sympy. No private paths, manuscript imports, or network access.
These checks do not prove the global optimum identity or undecidability.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
import platform
import numpy as np
import sympy as sp

SEED = 202610171337
TOL = 3e-10
rng = np.random.default_rng(SEED)


def hs2(a):
    return float(np.vdot(a, a).real / a.shape[0])


def unitary(n):
    q, r = np.linalg.qr(rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def polar(a):
    left, _, right = np.linalg.svd(a)
    return left @ right


def blocks(a, d, m):
    # (system-row, system-col, ancilla-row, ancilla-col)
    return a.reshape(d, m, d, m).transpose(0, 2, 1, 3).reshape(d*d, m*m)


def unblocks(a, d, m):
    return a.reshape(d, d, m, m).transpose(0, 2, 1, 3).reshape(d*m, d*m)


def run():
    worst = {}

    def eq(name, a, b):
        err = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
        worst[name] = max(worst.get(name, 0), err)
        assert err < TOL, (name, err)

    def le(name, a, b):
        violation = max(0.0, float(a-b))
        worst[name] = max(worst.get(name, 0), violation)
        assert violation < TOL, (name, violation)

    # Exact rational projection with overlapping coefficient supports.
    columns = sp.Matrix([[1, 0], [2, 1], [0, 1], [1, -1]])
    exact_p = columns*(columns.T*columns).inv()*columns.T
    exact_k = sp.eye(4)-exact_p
    assert exact_p == exact_p.T and exact_k*exact_k == exact_k
    amp_k = sp.kronecker_product(exact_k, sp.eye(4))
    assert amp_k*amp_k == amp_k and amp_k == amp_k.T

    count = 0
    for d in (2, 3, 4):
        for m in (1, 2, 3):
            for trial in range(20):
                rank = 1 + trial % (d*d-1)
                raw = rng.normal(size=(d*d, rank)) + 1j*rng.normal(size=(d*d, rank))
                q, _ = np.linalg.qr(raw)
                p = q @ q.conj().T
                k = np.eye(d*d)-p
                u = unitary(d*m)
                ub = blocks(u, d, m)
                x = unblocks(p @ ub, d, m)
                h = hs2(u-x)
                eq('projection_pythagoras', hs2(x)+h, 1)
                w = x/np.sqrt(hs2(x))
                eq('normalized_projection_distance', hs2(w-u), 2-2*np.sqrt(1-h))
                le('normalized_projection_bound', hs2(w-u), 2*h)
                pw = polar(w)
                le('polar_is_closer', hs2(w-pw), hs2(w-u))
                eq('polar_singular_distance', hs2(w-pw), np.mean((np.linalg.svd(w, compute_uv=False)-1)**2))
                # Choi matrix in output-first order vec(E_ij)=e_i tensor e_j.
                choi = ub @ ub.conj().T / m
                eq('choi_cost', np.trace(k @ choi).real/d, h)
                j = choi.reshape(d, d, d, d)
                eq('choi_partial_trace_output', np.trace(j, axis1=0, axis2=2), np.eye(d))
                eq('choi_partial_trace_input', np.trace(j, axis1=1, axis2=3), np.eye(d))
                v = ub.reshape(-1)
                eq('vectorized_amplification', np.vdot(v, np.kron(k, np.eye(m*m)) @ v).real/(d*m), h)
                # GM-to-mean singular bound for arbitrary normalized subspace elements.
                yb = p @ (rng.normal(size=(d*d, m*m))+1j*rng.normal(size=(d*d, m*m)))
                y = unblocks(yb, d, m)
                y /= np.sqrt(hs2(y))
                s = np.linalg.svd(y, compute_uv=False)
                gm2 = 0.0 if np.any(s == 0) else float(np.exp(2*np.mean(np.log(s))))
                le('gm_to_mean_singular', gm2, float(np.mean(s)**2))
                # Unnormalized radial minimum, underlying Yu-Duan-Xu C_Phi.
                a = float(np.mean(s))
                eq('radial_distance', hs2(a*y-polar(y)), 1-a*a)
                count += 1

    # Rank-one S=span(diag(2,1)): exact optimum h_m=1/10 for every m.
    rankone_count = 0
    for m in (1, 2, 3, 5, 8):
        a = np.diag([2.0, 1.0])
        u = np.kron(np.eye(2), unitary(m))
        p = np.outer(a.reshape(-1), a.reshape(-1))/np.vdot(a, a)
        x = unblocks(p @ blocks(u, 2, m), 2, m)
        eq('rank_one_exact_value', hs2(u-x), 0.1)
        rankone_count += 1

    # Singular block-diagonal W: polar extensions need not leave the block algebra.
    w = np.diag([0.0, 1.0, 0.0, 3.0]).astype(complex)
    w /= np.sqrt(hs2(w))
    pw = np.zeros_like(w)
    pw[:2, :2] = polar(w[:2, :2])
    pw[2:, 2:] = polar(w[2:, 2:])
    eq('singular_block_polar_unitarity', pw.conj().T @ pw, np.eye(4))
    eq('singular_block_polar_distance', hs2(w-pw), 2-2*np.mean(np.linalg.svd(w, compute_uv=False)))

    # Direct forward bound, without a determinant: each homogeneous gate.
    gate_count = 0
    for m in (1, 2, 3, 4):
        for _ in range(16):
            u, v, w, z = (unitary(m) for _ in range(4))
            gate = np.block([[0.6*u, 0.8*w], [0.8*z, -0.6*v]])
            residual = hs2(u @ z.conj().T-w @ v.conj().T)
            defect = hs2(gate @ gate.conj().T-np.eye(2*m))
            distance = hs2(gate-polar(gate))
            eq('gate_defect_identity', defect, (12/25)**2*residual)
            le('gate_polar_to_defect', distance, (25/36)*defect)
            le('gate_direct_forward_bound', distance, (4/25)*residual)
            gate_count += 1

    # CP frontier: singular Phi(I), random amplified unitary inputs.
    cp_count = 0
    for d in (2, 3, 4):
        for m in (1, 2, 3):
            output_support = np.diag([1.]*(d-1)+[0.])
            kraus = [output_support @ (rng.normal(size=(d, d))+1j*rng.normal(size=(d, d))) for _ in range(3)]
            amplified = [np.kron(a, np.eye(m)) for a in kraus]
            a = sum(k @ k.conj().T for k in kraus)
            for _ in range(10):
                u = unitary(d*m)
                value = sum(k @ u @ k.conj().T for k in amplified)
                le('cp_singular_frontier', hs2(value), hs2(a))
                cp_count += 1
            # Orthogonal CP projection T(X)=PXP: identity attains 1-rank(P)/d.
            support_amplified = np.kron(output_support, np.eye(m))
            eq('cp_projection_identity_witness', hs2(np.eye(d*m)-support_amplified), 1-(d-1)/d)

    # Exact constants and strict inequality (18+12 sqrt(2)) < 35.
    gamma = F(1, 36_288_000_000)
    beta = F(1, 4_536_000)
    source_gap = F(1, 1296)
    assert gamma == beta/8000
    assert 1750*gamma/(F(1, 8000)) == source_gap/2
    assert F(17, 12)**2 > 2  # 12 sqrt(2) < 17
    assert F(153, 49*2**40) < gamma/4
    assert F(25, 36)*F(12, 25)**2 == F(4, 25)
    assert 25*2*F(4, 25) == 8
    assert 8*F(1, 200)*F(34, 4) == F(17, 50)
    assert F(17, 50*2**40) < gamma/4
    # NO remains at least gamma; YES approximation error gamma/8 separates.
    assert gamma/4+gamma/8 < 5*gamma/8 < gamma-gamma/8

    return {
        'status': 'PASS', 'seed': SEED, 'tolerance': TOL,
        'random_matrix_cases': count, 'rank_one_analytic_cases': rankone_count,
        'direct_forward_gate_cases': gate_count,
        'cp_singular_output_cases': cp_count,
        'exact_rational_projection_and_amplification': True,
        'singular_block_polar_case': True, 'exact_constants': True,
        'maximum_absolute_errors_or_inequality_violations': worst,
        'gamma': str(gamma), 'python': platform.python_version(),
        'numpy': np.__version__, 'sympy': sp.__version__,
        'limitations': ['No numerical global-optimization certificate.',
                        'No machine-to-game implementation.',
                        'Finite diagnostics do not prove undecidability or novelty.'],
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path(__file__).with_name('finite-checks.json'))
    args = parser.parse_args()
    result = run()
    args.out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
