"""Exact modular exploration of local Milnor/Tjurina quotients.

The quotient is truncated by m^L.  Stabilization in L certifies the local
colength for the displayed finite fixtures.  Two large primes are used to
guard against an accidental rank drop in one characteristic.
"""

from itertools import product


PRIMES = (1_000_000_007, 1_000_000_009)


def monomials(d, max_total):
    return [a for a in product(range(max_total + 1), repeat=d) if sum(a) <= max_total]


def add_exp(a, b):
    return tuple(x + y for x, y in zip(a, b))


def rank_mod(rows, ncols, prime):
    pivots = {}
    rank = 0
    for sparse in rows:
        row = {j: c % prime for j, c in sparse.items() if c % prime}
        while row:
            col = min(row)
            if col not in pivots:
                inv = pow(row[col], prime - 2, prime)
                row = {j: (c * inv) % prime for j, c in row.items()}
                pivots[col] = row
                rank += 1
                break
            factor = row[col]
            pivot = pivots[col]
            for j, c in pivot.items():
                value = (row.get(j, 0) - factor * c) % prime
                if value:
                    row[j] = value
                elif j in row:
                    del row[j]
    return rank


def generators(d, s, a, include_f):
    zero = (0,) * d
    f = {}
    for i in range(d):
        exponent = list(zero)
        exponent[i] = s + 1
        f[tuple(exponent)] = 1
    f[tuple(a)] = f.get(tuple(a), 0) + 1

    gens = []
    for i in range(d):
        derivative = {}
        exponent = list(zero)
        exponent[i] = s
        derivative[tuple(exponent)] = s + 1
        if a[i]:
            exponent = list(a)
            exponent[i] -= 1
            derivative[tuple(exponent)] = derivative.get(tuple(exponent), 0) + a[i]
        gens.append(derivative)
    if include_f:
        gens.append(f)
    return gens


def truncated_colength(d, s, a, cutoff, include_f):
    basis = monomials(d, cutoff - 1)
    index = {exponent: i for i, exponent in enumerate(basis)}
    rows = []
    for generator in generators(d, s, a, include_f):
        min_degree = min(map(sum, generator))
        for multiplier in monomials(d, cutoff - 1 - min_degree):
            row = {}
            for exponent, coefficient in generator.items():
                target = add_exp(exponent, multiplier)
                if sum(target) < cutoff:
                    row[index[target]] = row.get(index[target], 0) + coefficient
            if row:
                rows.append(row)
    ranks = [rank_mod(rows, len(basis), prime) for prime in PRIMES]
    if ranks[0] != ranks[1]:
        raise AssertionError((d, s, a, cutoff, ranks))
    return len(basis) - ranks[0]


def fixture(d, s, a):
    values = []
    for cutoff in range(s + 2, d * s + sum(a) + 5):
        mu = truncated_colength(d, s, a, cutoff, False)
        tau = truncated_colength(d, s, a, cutoff, True)
        values.append((cutoff, mu, tau))
        if len(values) >= 3 and len({item[1:] for item in values[-3:]}) == 1:
            break
    cutoff, mu, tau = values[-1]
    predicted = 1
    for exponent in a:
        predicted *= s - exponent
    return {
        "d": d,
        "s": s,
        "a": a,
        "degree": sum(a),
        "cutoff": cutoff,
        "mu": mu,
        "tau": tau,
        "defect": mu - tau,
        "naive_product": predicted,
        "stable_tail": values[-3:],
    }


if __name__ == "__main__":
    cases = [
        (2, 4, (3, 3)),
        (2, 5, (3, 4)),
        (2, 6, (4, 4)),
        (3, 3, (2, 2, 2)),
        (3, 4, (2, 2, 2)),
        (3, 5, (3, 2, 2)),
        (3, 5, (3, 3, 3)),
        (3, 6, (3, 3, 3)),
        (4, 2, (1, 1, 1, 1)),
        (4, 3, (2, 1, 1, 1)),
        (4, 5, (2, 2, 2, 2)),
    ]
    for case in cases:
        print(fixture(*case))
