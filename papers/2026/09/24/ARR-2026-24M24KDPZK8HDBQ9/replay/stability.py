# SPDX-License-Identifier: Apache-2.0
"""Finite exact replay for the fixed-inertia stability extension.

Uses Fraction throughout; no matrix optimization or claim of all-dimensional
computer verification. The accompanying note contains the general proofs.
"""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise SystemExit('FAIL: ' + message)


def c(k, l):
    return Q((k + l) * (k + l - gcd(k, l)), 2 * k * l)


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def probabilities(n, denominator):
    return [tuple(Q(x, denominator) for x in z)
            for z in compositions(denominator, n)]


def spectrum(alpha):
    return [sum(alpha[k-1] / k for k in range(i, len(alpha)+1))
            for i in range(1, len(alpha)+1)]


def spike_distance(a):
    return 2 * (1 - a[0])


def flat_distance(a):
    return sum(abs(x - Q(1, len(a))) for x in a)


def horn_deficit_upper(a, b):
    n = len(b)
    return Q(n+1, 2) - sum((j+1)*v for j, v in enumerate(b)) + n*(1-a[0])


def main():
    if not __debug__:
        raise SystemExit('Refusing python -O; run without optimization.')
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1]/'certificates'/'stability.json')
    args = parser.parse_args()
    max_index, denominator, grid_max = 12, 4, 4
    counts = {'gap_cells': 0, 'unbalanced_grid_pairs': 0,
              'balanced_grid_pairs': 0, 'exact_one_spike_pairs': 0}
    constants = {}
    for n in range(2, max_index+1):
        H = Q(n+1, 2)
        for m in range(1, n+1):
            equalities = {(1, n)} if m < n else {(1, n), (n, 1)}
            gaps = {}
            for k in range(1, m+1):
                for l in range(1, n+1):
                    t = H - c(k, l)
                    require(t >= 0, 'nonnegative gap')
                    require((t == 0) == ((k, l) in equalities), 'exact equality cells')
                    if t:
                        gaps[(k, l)] = t
                    counts['gap_cells'] += 1
            if m < n:
                C = max(2*(2-Q(1, k)-Q(l, n))/t for (k, l), t in gaps.items())
                constants[f'{m},{n}'] = {'C': str(C), 'reverse': str(Q(n, 2))}
                if m == 1:
                    require(C == Q(4, n), 'one-spike antecedent constant')
            else:
                gamma = min(gaps.values())
                constants[f'{m},{n}'] = {'gamma': str(gamma),
                    'distance_coefficient': str(4*(1-Q(1, n))/gamma),
                    'reverse': str(Q(n, 2))}
    for n in range(2, grid_max+1):
        H = Q(n+1, 2)
        for m in range(1, n+1):
            for alpha in probabilities(m, denominator):
                a = spectrum(alpha)
                require(sum(a) == 1 and all(a[i] >= a[i+1] for i in range(m-1)),
                        'decreasing positive spectrum')
                for beta in probabilities(n, denominator):
                    b = spectrum(beta)
                    require(sum(b) == 1 and all(b[i] >= b[i+1] for i in range(n-1)),
                            'decreasing negative magnitudes')
                    G = sum(alpha[k-1]*beta[l-1]*(H-c(k, l))
                            for k in range(1, m+1) for l in range(1, n+1))
                    D1 = spike_distance(a) + flat_distance(b)
                    reverse1 = horn_deficit_upper(a, b)
                    require(reverse1 <= Q(n, 2)*D1, 'reverse Horn-expression inequality')
                    if m < n:
                        C = Q(constants[f'{m},{n}']['C'])
                        require(D1 <= C*G, 'unbalanced distance versus certificate gap')
                        counts['unbalanced_grid_pairs'] += 1
                        if m == 1:
                            actual_delta = H-sum((j+1)*x for j, x in enumerate(b))
                            require(D1/C <= actual_delta <= Q(n, 2)*D1,
                                    'actual one-spike cost stability')
                            counts['exact_one_spike_pairs'] += 1
                    else:
                        h = 1-Q(1, n)
                        gamma = Q(constants[f'{m},{n}']['gamma'])
                        D2 = flat_distance(a)+spike_distance(b)
                        D = min(D1, D2)
                        p, r, q, s = alpha[0], alpha[-1], beta[-1], beta[0]
                        w, A, B = p*q+r*s, p+q, r+s
                        S = max(A, B)
                        require(2*w <= S, 'product equality mass')
                        require(D <= 2*h*(2-S) <= 4*h*(1-w), 'factor four distance bound')
                        require(gamma*(1-w) <= G, 'mass outside equality cells')
                        require(D <= 4*h*G/gamma, 'balanced final bound')
                        require(min(reverse1, horn_deficit_upper(b, a)) <= Q(n, 2)*D,
                                'balanced reverse bound')
                        counts['balanced_grid_pairs'] += 1
    # N=1 has no off-equality cells and both deficit and distance are zero.
    require(c(1, 1) == 1 and spike_distance([Q(1)]) == 0, 'degenerate (1,1)')
    result = {'status': 'PASS', 'arithmetic': 'exact rational', 'counts': counts,
        'parameters': {'flat_cell_max_index': max_index, 'simplex_denominator': denominator,
                       'simplex_max_index': grid_max},
        'constants': constants,
        'scope': 'Finite arithmetic replay. General proof and antecedent Horn input are in paper.md; interior kappa is not computed.',
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'counts': counts, 'output': str(args.output.resolve())}))


if __name__ == '__main__':
    main()
