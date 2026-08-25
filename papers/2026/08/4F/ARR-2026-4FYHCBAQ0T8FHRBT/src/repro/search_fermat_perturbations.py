"""Search semiquasihomogeneous Fermat perturbations over exact prime fields.

This is exploratory code, not a proof of characteristic-zero sharpness.  For
each displayed polynomial it computes the dimension of

    k[x_1,...,x_d] / (f, df/dx_1, ..., df/dx_d, m^L)

by sparse Gaussian elimination over two large primes.  A stable tail in L is
reported, and agreement of both primes guards against accidental modular rank
drops for the tested fixture.
"""

from __future__ import annotations

from itertools import product
from random import Random


PRIMES = (1_000_000_007, 1_000_000_009)


def monomials(d: int, max_total: int):
    if max_total < 0:
        return []
    return [a for a in product(range(max_total + 1), repeat=d) if sum(a) <= max_total]


def add_exp(a, b):
    return tuple(x + y for x, y in zip(a, b))


def rank_mod(rows, prime: int):
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
            for j, c in pivots[col].items():
                value = (row.get(j, 0) - factor * c) % prime
                if value:
                    row[j] = value
                else:
                    row.pop(j, None)
    return rank


def derivatives(poly, d: int):
    result = []
    for i in range(d):
        derivative = {}
        for exponent, coefficient in poly.items():
            if exponent[i]:
                target = list(exponent)
                target[i] -= 1
                target = tuple(target)
                derivative[target] = derivative.get(target, 0) + coefficient * exponent[i]
        result.append(derivative)
    return result


def truncated_colength(poly, d: int, cutoff: int, include_f: bool):
    basis = monomials(d, cutoff - 1)
    index = {exponent: i for i, exponent in enumerate(basis)}
    generators = derivatives(poly, d) + ([poly] if include_f else [])
    rows = []
    for generator in generators:
        min_degree = min(map(sum, generator))
        for multiplier in monomials(d, cutoff - 1 - min_degree):
            row = {}
            for exponent, coefficient in generator.items():
                target = add_exp(exponent, multiplier)
                if sum(target) < cutoff:
                    j = index[target]
                    row[j] = row.get(j, 0) + coefficient
            if row:
                rows.append(row)
    ranks = [rank_mod(rows, prime) for prime in PRIMES]
    if ranks[0] != ranks[1]:
        raise AssertionError((cutoff, ranks))
    return len(basis) - ranks[0]


def evaluate(poly, d: int, s: int):
    history = []
    for cutoff in range(s + 2, d * s + 8):
        mu = truncated_colength(poly, d, cutoff, False)
        tau = truncated_colength(poly, d, cutoff, True)
        history.append((cutoff, mu, tau))
        if len(history) >= 3 and len({x[1:] for x in history[-3:]}) == 1:
            break
    return history[-1][1], history[-1][2], history[-3:]


def polynomial(d: int, s: int, terms):
    poly = {}
    for i in range(d):
        exponent = [0] * d
        exponent[i] = s + 1
        poly[tuple(exponent)] = 1
    for exponent, coefficient in terms.items():
        if coefficient:
            poly[exponent] = coefficient
    return poly


def candidates(d: int, s: int):
    # Terms surviving in the monomial Milnor box and of order > s+1.
    return [a for a in product(range(s), repeat=d) if sum(a) >= s + 2]


def e_floor(d: int, s: int):
    from math import comb

    def choose(n, k):
        return comb(n, k) if n >= k >= 0 else 0

    values = []
    for k in range(0, d * s + 2):
        value = choose(d + k, d) - d * choose(d + k - s, d) - choose(d + k - s - 2, d)
        values.append((value, k))
    return max(values)


def exhaustive_binary(d: int, s: int):
    terms = candidates(d, s)
    if len(terms) > 16:
        raise ValueError("binary search deliberately limited to 16 optional terms")
    best = None
    records = []
    for mask in range(1, 1 << len(terms)):
        chosen = {terms[i]: 1 for i in range(len(terms)) if mask & (1 << i)}
        mu, tau, tail = evaluate(polynomial(d, s, chosen), d, s)
        record = (tau, mu, tuple(chosen), tail)
        records.append(record)
        if best is None or record < best:
            best = record
    return terms, best, sorted(records)[:10]


def random_search(d: int, s: int, trials: int, seed: int = 20260825):
    rng = Random(seed)
    pool = candidates(d, s)
    best = None
    for _ in range(trials):
        chosen = {a: rng.choice((-2, -1, 0, 0, 0, 1, 2)) for a in pool}
        chosen = {a: c for a, c in chosen.items() if c}
        if not chosen:
            continue
        mu, tau, tail = evaluate(polynomial(d, s, chosen), d, s)
        record = (tau, mu, tuple(sorted(chosen.items())), tail)
        if best is None or record < best:
            best = record
            print({"event": "new_best", "d": d, "s": s, "floor": e_floor(d, s), "record": best})
    return best


if __name__ == "__main__":
    terms, best, leaders = exhaustive_binary(3, 3)
    print({"search": "exhaustive_binary", "d": 3, "s": 3, "candidate_terms": terms})
    print({"floor": e_floor(3, 3), "best": best, "leaders": leaders})
    for s, trials in ((4, 40), (5, 20)):
        print({"search": "random", "d": 3, "s": s, "trials": trials})
        print({"final_best": random_search(3, s, trials)})
