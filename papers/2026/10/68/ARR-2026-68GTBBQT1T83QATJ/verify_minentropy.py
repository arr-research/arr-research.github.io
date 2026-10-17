"""Author-context finite diagnostics; not a formal verification of the proofs."""
import itertools
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, linprog

ROOT = Path(__file__).resolve().parent
rng = np.random.default_rng(2026101707)

def marginal(psi, axis):
    mat = np.moveaxis(psi, axis, 0).reshape(psi.shape[axis], -1)
    return mat @ mat.conj().T / np.vdot(psi, psi).real

def apply_local(psi, matrix, axis):
    return np.moveaxis(np.tensordot(matrix, psi, axes=(1, axis)), 0, axis)

def wstate(n, weights=None):
    psi = np.zeros((2,) * n, dtype=complex)
    weights = np.ones(n) / n if weights is None else weights
    for j in range(n):
        index = [0] * n
        index[j] = 1
        psi[tuple(index)] = np.sqrt(weights[j])
    return psi

# Exact checks of the three-qubit contradiction and a three-copy restriction.
assert Fraction(3, 2)**3 == Fraction(27, 8) < 4
assert Fraction(3, 4)**2 > Fraction(1, 2)  # H_inf(midpoint) < average H_inf.
terms = []
for excitations in itertools.product(range(3), repeat=3):
    if any(excitations[copy] == copy for copy in range(3)):
        continue
    local = tuple(sum((excitations[c] == party) << (2-c) for c in range(3)) for party in range(3))
    terms.append(local)
assert len(terms) == 8
exact_marginals = []
for party in range(3):
    mat = np.zeros((8, 64), dtype=np.int64)
    for triple in terms:
        other = [triple[j] for j in range(3) if j != party]
        mat[triple[party], other[0] * 8 + other[1]] += 1
    rho = mat @ mat.T
    assert np.array_equal(rho, np.diag(np.diag(rho)))
    assert sorted(np.diag(rho).tolist()) == [0, 0, 0, 0, 2, 2, 2, 2]
    exact_marginals.append(np.diag(rho).tolist())

normal_cases = 0
largest_sum_deficit = -1
functional_violation = -1
for n in range(3, 8):
    for _ in range(40):
        psi = wstate(n)
        for j in range(n):
            a = rng.normal(size=(2,2)) + 1j * rng.normal(size=(2,2))
            psi = apply_local(psi, a, j)
            psi /= np.linalg.norm(psi)
        lambdas = np.array([np.linalg.eigvalsh(marginal(psi,j))[-1] for j in range(n)])
        largest_sum_deficit = max(largest_sum_deficit, n-1-lambdas.sum())
        assert lambdas.sum() >= n-1-2e-11
        theta = rng.dirichlet(np.ones(n))
        observed = -theta @ np.log2(lambdas)
        upper = np.sort(theta)[-2:].sum()
        functional_violation = max(functional_violation, observed-upper)
        assert observed <= upper+2e-11
        normal_cases += 1

weighted_cases = 0
max_lp_error = 0
for n in range(3, 7):
    for run in range(8):
        xi = np.ones(n) if run == 0 else rng.uniform(.08, 1, n)
        xi /= xi.max()
        # Proposed closed formula in multiplicative units.
        val = lambda z: np.sum(z**(-xi)) - (n-1)
        prediction = 2.0 if val(2) >= 0 else brentq(val, 1, 2, xtol=1e-14)
        # Independent feasibility implementation: LP on excitation probabilities.
        low, high = 0., 1.
        for _ in range(36):
            mid = (low+high)/2
            lower = 1-2**(-mid*xi)
            lp = linprog(np.zeros(n), A_ub=-np.eye(n), b_ub=-lower,
                         A_eq=np.ones((1,n)), b_eq=[1.], bounds=[(0,.5)]*n,
                         method='highs', options={'primal_feasibility_tolerance':1e-9})
            if lp.success: low = mid
            else: high = mid
        max_lp_error = max(max_lp_error, abs(2**low-prediction))
        assert abs(2**low-prediction) < 2e-8
        upper = prediction**(-xi)
        lam = np.full(n, .5)
        remaining = n-1-lam.sum()
        for j in range(n):
            step = min(remaining, max(0, upper[j]-.5))
            lam[j] += step
            remaining -= step
        assert abs(remaining) < 2e-12
        psi = wstate(n, 1-lam)
        measured = np.array([np.linalg.eigvalsh(marginal(psi,j))[-1] for j in range(n)])
        achieved = np.min(measured**(-1/xi))
        assert abs(achieved-prediction) < 2e-9
        weighted_cases += 1

# Finite checks of the simultaneous typical-projector domination inequality.
projector_checks = 0
for _ in range(8):
    psi = rng.normal(size=(2,2,2)) + 1j*rng.normal(size=(2,2,2))
    psi /= np.linalg.norm(psi)
    tensor = np.kron(psi.reshape(-1), np.kron(psi.reshape(-1), psi.reshape(-1)))
    tensor = tensor.reshape((2,)*9).transpose(0,3,6,1,4,7,2,5,8).reshape(8,8,8)
    projectors, reference, bounds = [], [], []
    for j in range(3):
        rho = marginal(psi,j)
        p, u = np.linalg.eigh(rho)
        H = -p @ np.log2(p)
        eigenvalues = np.kron(p,np.kron(p,p))
        basis = np.kron(u,np.kron(u,u))
        keep = eigenvalues <= 2**(-3*(H-.35))
        P = (basis*keep) @ basis.conj().T
        projectors.append(P)
        reference.append((basis*(eigenvalues*keep)) @ basis.conj().T)
        bounds.append(2**(-3*(H-.35)))
    projected = tensor.copy()
    for j, P in enumerate(projectors): projected = apply_local(projected,P,j)
    q = np.vdot(projected,projected).real
    if q < 1e-12: continue
    for j in range(3):
        rho_new = marginal(projected,j)
        assert np.linalg.eigvalsh(reference[j]-q*rho_new)[0] >= -2e-12
        assert q*np.linalg.eigvalsh(rho_new)[-1] <= bounds[j]+2e-12
        projector_checks += 1

report = {'status':'PASS','seed':2026101707,
 'exact_counterexample':{'G_W':'3/2','min_F_W':'2^(2/3)', 'cubed_gap':'5/8'},
 'exact_three_copy_restriction':{'terms':terms,'unnormalized_marginal_diagonals':exact_marginals,
                                'norm_squared':8,'largest_local_eigenvalue':'1/4','G_lower_bound':4},
 'normal_form_random_cases':normal_cases,'largest_sum_deficit':float(largest_sum_deficit),
 'largest_F_bound_violation':float(functional_violation),
 'weighted_root_vs_LP_cases':weighted_cases,'largest_LP_error':float(max_lp_error),
 'typical_projector_domination_checks':projector_checks,
 'scope':'Author-context exact finite witness and numerical diagnostics; not independent review, a priority certificate, or formal proof verification.'}
(ROOT/'diagnostics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
