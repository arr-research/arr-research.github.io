"""Finite diagnostics for the capacity argument; these do not prove its limit theorem.

Run: python verify_capacity_cuts.py [--output finite-checks.json]
Requires numpy. No private paths or external data files are used.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import math
import numpy as np


def cuts(B, c):
    d = len(B)
    masks = ((np.arange(1 << d)[:, None] >> np.arange(d)) & 1).astype(float)
    sizes = masks.sum(axis=1)
    demand = sizes[:, None] - sizes[None, :]
    slack = masks @ B @ (1 - masks).T - c * demand
    assert np.min(slack) >= -2e-11, float(np.min(slack))
    return int(slack.size)


def unitary(rng, d):
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return np.linalg.qr(z)[0]


def inverse_sqrt(X):
    eig, V = np.linalg.eigh(X)
    assert eig.min() > 0
    return (V/eig**.5) @ V.conj().T


def balance_and_mp(rng):
    balance_count = 0
    for m in [2, 3, 4]:
        for _ in range(4):
            d, s = 3, 4
            A = rng.normal(size=(s, d, d)) + 1j*rng.normal(size=(s, d, d))
            Y = rng.normal(size=(s, m, m)) + 1j*rng.normal(size=(s, m, m))
            Y /= np.sqrt(sum(np.linalg.norm(y, 'fro')**2 for y in Y)/m)
            original = sum(np.kron(a, y) for a, y in zip(A, Y))
            _, old_log_abs_det = np.linalg.slogdet(original)
            for side in ['right', 'left']:
                S = sum(y.conj().T@y if side == 'right' else y@y.conj().T for y in Y)
                R = inverse_sqrt(S)
                Z = [y@R if side == 'right' else R@y for y in Y]
                assert abs(sum(np.linalg.norm(z, 'fro')**2 for z in Z)/m-1) < 1e-12
                _, new_log_abs_det = np.linalg.slogdet(sum(np.kron(a, z) for a, z in zip(A, Z)))
                actual = 2*(new_log_abs_det-old_log_abs_det)/(d*m)
                predicted = -np.linalg.slogdet(S)[1]/m
                assert abs(actual-predicted) < 2e-11
                assert predicted >= -1e-12
                balance_count += 1

    mp_moment_checks = 0
    for m in [2, 3, 5]:
        # A mixture of matrix-unit Kraus operators and noncommuting unitaries.
        Y = []
        for a in range(m):
            for b in range(m):
                e = np.zeros((m, m), dtype=complex)
                e[a, b] = np.sqrt(.4/m)
                Y.append(e)
        Y += [np.sqrt(.3)*unitary(rng, m), np.sqrt(.3)*unitary(rng, m)]
        assert np.linalg.norm(sum(y@y.conj().T for y in Y)-np.eye(m)) < 1e-12
        assert np.linalg.norm(sum(y.conj().T@y for y in Y)-np.eye(m)) < 1e-12
        zero = np.zeros((m, m), dtype=complex)
        coeffs = []
        for y in Y:
            coeffs.append(np.block([[zero, y], [y.conj().T, zero]])/np.sqrt(2))
            coeffs.append(np.block([[zero, 1j*y], [-1j*y.conj().T, zero]])/np.sqrt(2))
        def eta(T):
            return sum(a @ T @ a for a in coeffs)
        assert np.linalg.norm(eta(np.eye(2*m))-np.eye(2*m)) < 1e-12
        moments = [np.eye(2*m, dtype=complex)]
        for n in range(1, 9):
            moments.append(sum(eta(moments[r]) @ moments[n-1-r] for r in range(n)))
            catalan = math.comb(2*n, n)//(n+1)
            assert np.linalg.norm(moments[n]-catalan*np.eye(2*m)) < 1e-10*catalan
            mp_moment_checks += 1

    nodes, weights = np.polynomial.legendre.leggauss(400)
    theta = (nodes+1)*np.pi/4
    weights = weights*np.pi/4
    x = 4*np.sin(theta)**2
    density_weights = weights*(4/np.pi)*np.cos(theta)**2
    mp_log_checks = 0
    max_quadrature_error = 0.
    for t in np.logspace(-4, 2, 25):
        integral = float(density_weights @ np.log(x+t))
        ell = -1 + (np.sqrt(t*(t+4))-t)/2 + 2*np.arcsinh(np.sqrt(t)/2)
        error = abs(integral-ell)
        max_quadrature_error = max(error, max_quadrature_error)
        assert error < 3e-9, (t, error)
        assert -1e-12 <= ell+1 <= 2*np.sqrt(t)+1e-12
        mp_log_checks += 1

    gram_checks = 0
    for d, s in [(3, 4), (4, 7), (5, 12)]:
        A = (rng.normal(size=(s, d, d))+1j*rng.normal(size=(s, d, d)))/np.sqrt(2*d)
        G = np.einsum('iab,jab->ij', A.conj(), A)/d
        R = inverse_sqrt(G)
        B = np.einsum('iab,ij->jab', A, R)
        gram = np.einsum('iab,jab->ij', B.conj(), B)/d
        assert np.linalg.norm(gram-np.eye(s), 2) < 1e-12
        MA = sum(np.kron(a.conj(), a) for a in A)/s
        MB = sum(np.kron(b.conj(), b) for b in B)/s
        bound = sum((np.linalg.norm(a, 2)+np.linalg.norm(b, 2))*np.linalg.norm(b-a, 2)
                    for a, b in zip(A, B))/s
        assert np.linalg.norm(MB-MA, 2) <= bound+1e-12
        gram_checks += 1

    return dict(balance_rescaling_identities=balance_count,
                operator_valued_mp_moment_checks=mp_moment_checks,
                mp_regularized_log_quadratures=mp_log_checks,
                mp_maximum_quadrature_error=max_quadrature_error,
                exact_gram_whitening_instances=gram_checks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('finite-checks.json'))
    args = parser.parse_args()
    rng = np.random.default_rng(20261017)
    exact_cases = 0
    for d in range(2, 21):
        for eps in [F(0), F(1, 100), F(1, 20), F(1, 10)]:
            for q in [F(0), F(1, 100), F(1, 40), F(1, 20), F(1, 10)]:
                c = 1 - eps - 2*q
                assert c >= F(1, 2)
                for a in range(1, d+1):
                    for b in range(a):
                        if a <= c*d:
                            slack = (1-eps-q)*a - F(a*b, d) - c*(a-b)
                        elif d-b <= c*d:
                            slack = ((1-eps-q)*(d-b)
                                     - F((d-a)*(d-b), d) - c*(a-b))
                        else:
                            x, y = F(a, d), F(d-b, d)
                            assert q <= c*(1-c)
                            assert x*y >= x+y-1
                            slack = d*x*y*(1-q/c) - c*(a-b)
                        assert slack >= 0
                        exact_cases += 1

    cut_count = 0
    nonnegative_count = 0
    for d in range(2, 8):
        for _ in range(6):
            J = np.ones((d, d))/d
            perm = np.eye(d)[rng.permutation(d)]
            B = .97*J + .05*(perm-J) + .01*rng.random((d, d))/d
            eps = max(0., 1-B.sum(axis=0).min(), 1-B.sum(axis=1).min())
            q = np.linalg.norm(B-J, 2)
            c = 1-eps-2*q
            assert c >= .5
            cut_count += cuts(B, c)
            nonnegative_count += 1

    quantum_records = []
    determinant_samples = 0
    quantum_compressions = 0
    for d in [2, 3, 4, 6]:
        for s in [256, 1024]:
            A = (rng.normal(size=(s, d, d))
                 + 1j*rng.normal(size=(s, d, d)))/np.sqrt(2*d)
            left = sum(a @ a.conj().T for a in A)/s
            right = sum(a.conj().T @ a for a in A)/s
            M = sum(np.kron(a.conj(), a) for a in A)/s
            omega = np.eye(d).reshape(-1, order='F')/np.sqrt(d)
            P = np.outer(omega, omega.conj())
            q = np.linalg.norm(M-P, 2)
            u = np.linalg.norm(M @ (np.eye(d*d)-P), 2)
            v = np.linalg.norm(left-np.eye(d), 'fro')/np.sqrt(d)
            assert q <= np.sqrt(u*u+v*v) + 1e-12
            eps = max(0., 1-np.linalg.eigvalsh(left).min(),
                      1-np.linalg.eigvalsh(right).min())
            c = 1-eps-2*q
            assert c >= .5
            min_log_margin = float('inf')
            for _ in range(8):
                U = unitary(rng, d)
                V = unitary(rng, d)
                B = sum(abs(V.conj().T @ a @ U)**2 for a in A)/s
                assert np.linalg.norm(B-np.ones((d, d))/d, 2) <= q+1e-12
                cut_count += cuts(B, c)
                quantum_compressions += 1
                x = np.exp(rng.uniform(-6, 6, size=d))
                X = (U*x) @ U.conj().T
                Y = sum(a @ X @ a.conj().T for a in A)/s
                eig, W = np.linalg.eigh(Y)
                assert eig.min() > 0
                B_eig = sum(abs(W.conj().T @ a @ U)**2 for a in A)/s
                assert np.allclose(B_eig @ x, eig, rtol=2e-10, atol=1e-10)
                margin = float(np.log(eig).sum()-np.log(x).sum()-d*np.log(c))
                assert margin >= -1e-9
                min_log_margin = min(min_log_margin, margin)
                determinant_samples += 1
            quantum_records.append(dict(D=d, s=s, epsilon=eps, q=q, c=c,
                                        minimum_log_determinant_margin=min_log_margin))

    result = dict(status='PASS', seed=20261017,
                  exact_rational_cut_branch_cases=exact_cases,
                  nonnegative_matrices=nonnegative_count,
                  quantum_compressions=quantum_compressions,
                  enumerated_cuts=cut_count,
                  positive_definite_determinant_samples=determinant_samples,
                  ginibre_instances=quantum_records,
                  balance_mp_gram_checks=balance_and_mp(rng),
                  limitations=['Finite diagnostics only; no verification of an infinite-dimensional probability limit.',
                               'Floating-point checks are separate from the exact rational branch checks.',
                               'No numerical minimization of capacity was performed.'])
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'ginibre_instances'}, indent=2))


if __name__ == '__main__':
    main()
