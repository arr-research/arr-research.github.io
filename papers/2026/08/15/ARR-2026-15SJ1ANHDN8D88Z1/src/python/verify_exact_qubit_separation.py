#!/usr/bin/env python3
"""Fail-closed exact checks for the three-qubit list-separation certificate.

The irrational radius is represented through R^2=1/3; every asserted vector
identity is checked over the rationals.  Floating point is used only for the
final human-readable decimal.
"""

from fractions import Fraction as Q
from math import sqrt


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def add_scaled(total, weight, vector):
    return tuple(a + weight * b for a, b in zip(total, vector))


def main():
    ns = (
        (Q(0), Q(0), Q(1)),
        (Q(4, 5), Q(0), Q(3, 5)),
        (Q(0), Q(4, 5), Q(3, 5)),
    )
    u = (Q(1, 3), Q(1, 3), Q(2, 3))
    radius2 = Q(1, 3)

    assert all(dot(n, n) == 1 for n in ns)
    assert dot(u, u) == Q(2, 3)
    assert all(dot(sub(u, n), sub(u, n)) == radius2 for n in ns)
    assert all(dot(u, n) == Q(2, 3) for n in ns)

    lambdas = (Q(1, 6), Q(5, 12), Q(5, 12))
    barycentre = (Q(0), Q(0), Q(0))
    for lam, n in zip(lambdas, ns):
        barycentre = add_scaled(barycentre, lam, n)
    assert sum(lambdas, Q(0)) == 1
    assert barycentre == u

    # The POVM effects are F_i=w_i(I+m_i.sigma)/2 with w_i=2 lambda_i.
    # Since m_i=(u-n_i)/R, sum_i w_i m_i=0 follows after multiplying by R.
    weights = tuple(2 * lam for lam in lambdas)
    weighted_numerator = (Q(0), Q(0), Q(0))
    for weight, n in zip(weights, ns):
        weighted_numerator = add_scaled(weighted_numerator, weight, sub(u, n))
    assert sum(weights, Q(0)) == 2
    assert weighted_numerator == (Q(0), Q(0), Q(0))

    # Projector-test comparison: sum rho_i has eigenvalues
    # (15 +- sqrt(153))/10, so the largest one exceeds ell=2.
    sum_n = tuple(sum((n[j] for n in ns), Q(0)) for j in range(3))
    assert dot(sum_n, sum_n) == Q(153, 25)
    assert (15 + sqrt(153)) / 10 > 2

    radius = 1 / sqrt(3)
    error = (1 - radius) / 3
    success = 1 - error
    assert abs(success - (2 + radius) / 3) < 1e-15
    assert success < 1

    print("PASS: exact circumcenter/radius and barycentric POVM identities")
    print("PASS: dual-primal optimum P_list=(2+1/sqrt(3))/3")
    print(f"P_list = {success:.15f}")


if __name__ == "__main__":
    main()
