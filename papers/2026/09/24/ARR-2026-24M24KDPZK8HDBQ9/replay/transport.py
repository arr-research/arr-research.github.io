# SPDX-License-Identifier: Apache-2.0
"""Exact certificates for the flat-block transportation refinement.

No floating-point solver, matrix-optimum oracle or third-party dependency.
Run: python src/transport.py
"""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import hashlib
import json

if not __debug__:
    raise SystemExit("Refusing -O: exact certificates require enabled assertions.")


def cost(k, l):
    assert k >= 1 and l >= 1
    return Q((k + l) * (k + l - gcd(k, l)), 2 * k * l)


def margins(plan):
    m, n = len(plan), len(plan[0])
    assert all(len(row) == n for row in plan)
    return ([sum(row) for row in plan],
            [sum(plan[i][j] for i in range(m)) for j in range(n)])


def coefficients(spectrum):
    total = sum(spectrum)
    assert total > 0 and all(x >= 0 for x in spectrum)
    assert all(a >= b for a, b in zip(spectrum, spectrum[1:]))
    padded = list(spectrum) + [Q(0)]
    return [Q(i + 1) * (padded[i] - padded[i + 1]) / total
            for i in range(len(spectrum))]


def reconstruct(alpha):
    return [sum(alpha[k] / (k + 1) for k in range(i, len(alpha)))
            for i in range(len(alpha))]


def certificate(alpha, beta, plan, u, v):
    m, n = len(alpha), len(beta)
    assert len(plan) == m and all(len(row) == n for row in plan)
    assert sum(alpha) == sum(beta) == 1
    assert all(x >= 0 for row in plan for x in row)
    assert margins(plan) == (list(alpha), list(beta))
    assert len(u) == m and len(v) == n
    assert all(u[i] + v[j] <= cost(i + 1, j + 1)
               for i in range(m) for j in range(n))
    primal = sum(plan[i][j] * cost(i + 1, j + 1)
                 for i in range(m) for j in range(n))
    dual = sum(a * x for a, x in zip(alpha, u)) + sum(b * y for b, y in zip(beta, v))
    assert primal == dual
    assert all(plan[i][j] == 0 or u[i] + v[j] == cost(i + 1, j + 1)
               for i in range(m) for j in range(n))
    product = sum(alpha[i] * beta[j] * cost(i + 1, j + 1)
                  for i in range(m) for j in range(n))
    assert primal <= product
    r = sum(a > 0 for a in alpha)
    s = sum(b > 0 for b in beta)
    support = sum(x > 0 for row in plan for x in row)
    assert support <= r + s - 1  # These explicitly supplied plans are sparse.
    return dict(primal=str(primal), dual=str(dual), product=str(product),
                improvement=str(product - primal), positive_entries=support)


def spectrum_check(plan, padding):
    alpha, beta = margins(plan)
    assert sum(alpha) == sum(beta) == 1
    a, b = reconstruct(alpha), reconstruct(beta)
    assert coefficients(a) == alpha and coefficients(b) == beta
    m, n = len(alpha), len(beta)
    d = m + n + padding
    target = a + [Q(0)] * padding + [-x for x in reversed(b)]
    actual = [Q(0)] * d
    for i in range(m):
        for j in range(n):
            k, l = i + 1, j + 1
            block = [Q(1, k)] * k + [Q(0)] * (d - k - l) + [-Q(1, l)] * l
            assert all(x >= y for x, y in zip(block, block[1:]))
            actual = [x + plan[i][j] * y for x, y in zip(actual, block)]
    assert actual == target
    assert sum(target) == 0
    assert all(x >= y for x, y in zip(target, target[1:]))
    # Unnormalized marginals have mass P and reconstruct P times the target.
    p = Q(7)
    scaled_alpha, scaled_beta = margins([[p * x for x in row] for row in plan])
    assert sum(scaled_alpha) == sum(scaled_beta) == p
    assert reconstruct(scaled_alpha) == [p * x for x in a]
    assert reconstruct(scaled_beta) == [p * x for x in b]


def run():
    half, zero = Q(1, 2), Q(0)
    a = [Q(3, 4), Q(1, 4)]
    alpha = coefficients(a)
    assert alpha == [half, half]
    paired = certificate(alpha, alpha, [[half, zero], [zero, half]],
                         [zero, zero], [Q(1), Q(1)])
    assert paired['primal'] == '1' and paired['product'] == '5/4'
    # Independent paired factor cost: half the sum of its squared entries.
    assert (Q(3, 2) + Q(1, 2)) / 2 == 1

    b = [Q(5, 12), Q(5, 12), Q(1, 6)]
    beta = coefficients(b)
    assert beta == [zero, half, half]
    rectangular = certificate(alpha, beta,
                              [[zero, zero, half], [zero, half, zero]],
                              [zero, -half], [Q(1), Q(3, 2), Q(2)])
    assert rectangular['primal'] == '3/2' and rectangular['product'] == '37/24'

    grid_count = 0
    for i in range(11):
        for j in range(11):
            x, y = Q(i, 10), Q(j, 10)
            if x >= y:
                plan = [[y, x - y], [zero, 1 - x]]
                u, v = [half, zero], [half, Q(1)]
            else:
                plan = [[x, zero], [y - x, 1 - y]]
                u, v = [zero, half], [Q(1), half]
            result = certificate([x, 1 - x], [y, 1 - y], plan, u, v)
            assert Q(result['primal']) == 1 + abs(x - y) / 2
            assert Q(result['improvement']) == min(x * (1 - y), y * (1 - x))
            spectrum_check(plan, 2)
            grid_count += 1

    reconstruction_count = 0
    for m in range(1, 9):
        for n in range(1, 9):
            weights = [[Q(((i + 1) * (j + 2) + m + 2 * n) % 7 + 1)
                        for j in range(n)] for i in range(m)]
            total = sum(sum(row) for row in weights)
            plan = [[x / total for x in row] for row in weights]
            spectrum_check(plan, 3)
            reconstruction_count += 1

    non_monge = cost(1, 2) + cost(2, 3) - cost(1, 3) - cost(2, 2)
    non_anti_monge = cost(1, 1) + cost(2, 2) - cost(1, 2) - cost(2, 1)
    assert non_monge == Q(1, 6) and non_anti_monge == -1
    assert (cost(1, 2) + cost(2, 3)) / 2 == Q(19, 12) > Q(3, 2)

    flat_count = 0
    for k in range(1, 33):
        for l in range(1, 33):
            c = cost(k, l)
            assert c >= 1
            assert (c == 1) == (k == l)
            if min(k, l) == 1:
                assert c == Q(max(k, l) + 1, 2)
            else:
                assert c < Q(max(k, l) + 1, 2)
            flat_count += 1

    result = dict(status='PASS', exact_arithmetic='fractions.Fraction',
                  named_examples={'paired_2_by_2': paired, 'nonpaired_2_by_3': rectangular},
                  grid_2_by_2_certificates=grid_count,
                  rectangular_reconstructions=reconstruction_count,
                  additional_grid_reconstructions=grid_count,
                  flat_arithmetic_checks=flat_count,
                  non_Monge_contrast=str(non_monge),
                  non_anti_Monge_contrast=str(non_anti_monge),
                  scope='Exact finite certificates and reconstructions; no general matrix optimum or Horn theorem verified by this script.',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (Path(__file__).resolve().parents[1]/'certificates'/'transport.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
