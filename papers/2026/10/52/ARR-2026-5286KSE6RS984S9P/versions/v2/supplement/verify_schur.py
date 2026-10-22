"""Diagnostics for the square-root Schur residual manuscript.

The analytic argument, not these finite checks, proves the universal theorem.
Run in a directory containing no verification-results.json; results are immutable.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib
import json
import math
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
rng = random.Random(18102612)
root = Path(__file__).parent
target = root / 'verification-results.json'
if target.exists():
    raise SystemExit('Refusing to overwrite existing results')

t = sp.Symbol('t')
newton = 0
for n in range(2, 9):
    for _ in range(12):
        z = [sp.Rational(rng.choice([-1, 1])*rng.randint(4, 12), 4)
             + sp.I*sp.Rational(rng.randint(-6, 6), 4) for j in range(n)]
        P = sp.Poly(sp.prod(1-zj*t for zj in z), t)
        S = sp.Poly(sum(sum(zj**k for zj in z)*t**(k-1)
                        for k in range(2, n+2)), t)
        product = P*S
        projected = sp.Poly(sum(product.nth(k)*t**k for k in range(n+1)), t)
        assert sp.Poly(P.diff().as_expr()-P.nth(1)*P.as_expr()
                       + projected.as_expr(), t).is_zero
        newton += 1

geometry = []
for eta0 in ['0.001', '0.01', '0.1', '0.5', '1', '1.8']:
    eta = mp.mpf(eta0)
    a = 2*eta
    K = int(mp.ceil(mp.mpf('2.1')/eta))
    largest_w = largest_test_ratio = mp.mpf(0)
    for _ in range(80):
        while True:
            rad = math.sqrt(rng.random())
            theta = 2*math.pi*rng.random()
            beta = mp.mpc(str(rad*math.cos(theta)), str(rad*math.sin(theta)))
            if beta.real <= 1-eta:
                break
        v = 1/(1-beta)
        w = 1-a*v
        psi = (1-w**K)/(K*a)
        assert abs(w) <= 1+mp.mpf('1e-80')
        assert abs(psi) <= 2/(K*a)+mp.mpf('1e-80')
        assert v.real >= mp.mpf('0.5')
        largest_w = max(largest_w, abs(w))
        largest_test_ratio = max(largest_test_ratio, abs(psi)*K*a/2)
    geometry.append(dict(eta=eta0, K=K, samples=80,
                         max_abs_w=str(largest_w),
                         max_test_ratio=str(largest_test_ratio)))

v, a = sp.symbols('v a')
for K in range(2, 25):
    psi = sp.cancel((1-(1-a*v)**K)/(K*a))
    expected = sum((-1)**(k+1)*sp.binomial(K,k)*a**(k-1)*v**k/K
                   for k in range(1, K+1))
    assert sp.expand(psi-expected) == 0
    assert psi.subs(v, 0) == 0 and sp.diff(psi, v).subs(v, 0) == 1

# Exact elementary constants used by the simplified finite-threshold proof.
def exp_partial(x, degree):
    total = term = Q(1)
    for k in range(1, degree+1):
        term *= x/k
        total += term
    return total

assert exp_partial(Q(3), 5) > 18 > 17
assert 256**2 > 4*10001  # e^8 > 2^8 > 2 sqrt(10001)
assert -Q(9,4)+Q(14,19)*3 == -Q(3,76)
assert -Q(3,76)*100+3+Q(3,800) < 0
assert Q(25,784)*Q(10001,10000) < Q(1,25)
assert Q(9,64)*Q(10001,10000) < Q(1,4)
assert Q(1,50000) < Q(1,42)
exact = dict(exp3_partial_degree5=str(exp_partial(Q(3),5)),
             exponent_upper_at_10000=str(-Q(3,76)*100+3+Q(3,800)),
             prefactor_square_bound=True, q_prefactor_bound=True,
             B_below_margin=True,
             scope='Rational checks of displayed constants. Monotonicity and all-n claims use the analytic proof.')

def certificate(n):
    n = mp.mpf(n)
    y = 3*mp.sqrt(n)
    r = 3/(8*mp.sqrt(n))
    eta = (y-2-mp.log(2*mp.sqrt(n+1)))/n
    a = 2*eta
    K = int(mp.ceil(mp.mpf('2.1')/eta))
    logq = mp.log(r*mp.sqrt(n+1))-y+(2*n+1)*r
    logB = (mp.log(2*mp.sqrt(n+1)*r/(K*a*n))-y+(2*n+1)*r
            + K*mp.log1p(a/r))
    margin = mp.mpf('.5')-1/(K*eta)
    passed = bool(0 < eta <= 2 and mp.log(n+1)/2-y <= 0 and
                  logq <= -mp.log(2) and K >= 2 and margin > 0 and
                  logB < mp.log(margin))
    assert passed
    return dict(n=str(int(n)), y=str(y), r=str(r), eta=str(eta), K=str(K),
                log_q=str(logq), log_B=str(logB), margin=str(margin),
                pass_diagnostic=passed)

rows = [certificate(n) for n in
        [10000, 10001, 11000, 20000, 10**5, 10**6, 10**8, 10**12, 10**24, 10**48]]
out = dict(created_at=datetime.now(timezone.utc).isoformat(),
           script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           exact_gaussian_rational_newton_identities=newton,
           reciprocal_zero_geometry=geometry, exact_test_polynomial_checks=23,
           exact_rational_checks=exact, finite_certificate_diagnostics=rows,
           asymptotic_constant=str(mp.sqrt(mp.mpf(8)*mp.log(17)/3)),
           scope='Finite reproducible diagnostics; not a formal proof or historical priority certificate.')
target.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(dict(newton=newton, geometry=480, test_identities=23,
                     finite_certificates=len(rows), all_checks_passed=True)))
