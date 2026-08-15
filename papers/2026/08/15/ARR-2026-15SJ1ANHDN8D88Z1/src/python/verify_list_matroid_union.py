#!/usr/bin/env python3
"""Exact, lightweight checks for the Paper 21 research memo.

Only the Python standard library is used.  All scalar arithmetic is rational.
The script deliberately fails closed on the first discrepancy.
"""

from fractions import Fraction as Q
from itertools import combinations, product


def subsets(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield tuple(items[j] for j in range(len(items)) if mask & (1 << j))


def rank(columns):
    """Column rank over Q; columns are equal-length rational tuples."""
    if not columns:
        return 0
    a = [list(row) for row in zip(*columns)]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [x - scale * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matmul(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def scale_matrix(c, a):
    return [[c * x for x in row] for row in a]


def add_matrix(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def d_function(supports):
    ground = tuple(range(len(supports)))

    def d(a):
        cols = []
        for i in a:
            cols.extend(supports[i])
        return rank(cols)

    return ground, d


def rado_rank(a, d):
    a = tuple(a)
    return min(len(a) - len(c) + d(c) for c in subsets(a))


def closed_union_rank(a, ell, d):
    a = tuple(a)
    return min(len(a) - len(c) + ell * d(c) for c in subsets(a))


def brute_union_rank(a, ell, d):
    """Max size colorable by ell Rado-independent colors."""
    a = tuple(a)
    best = 0
    # color 0 means omitted; colors 1..ell are the independent parts.
    for colors in product(range(ell + 1), repeat=len(a)):
        used = sum(c != 0 for c in colors)
        if used <= best:
            continue
        ok = True
        for color in range(1, ell + 1):
            block = tuple(a[j] for j, c in enumerate(colors) if c == color)
            if rado_rank(block, d) != len(block):
                ok = False
                break
        if ok:
            best = used
    return best


def check_union_rank_identity():
    e0 = (Q(1), Q(0), Q(0))
    e1 = (Q(0), Q(1), Q(0))
    e2 = (Q(0), Q(0), Q(1))
    fixtures = [
        [[e0], [e0], [e1], [e0, e1]],
        [[e0], [e1], [e0, e1], [e2], [e1, e2]],
        [[e0, e1], [e1, e2], [e0, e2], [e0], [e2]],
    ]
    checked = 0
    for supports in fixtures:
        ground, d = d_function(supports)
        for a in subsets(ground):
            for ell in (1, 2, 3):
                lhs = brute_union_rank(a, ell, d)
                rhs = closed_union_rank(a, ell, d)
                assert lhs == rhs, (supports, a, ell, lhs, rhs)
                checked += 1
    return checked


def check_exact_list_fixture():
    # Three labels: two share e0, one is e1.  The two-list POVM reports
    # {0,1} on e0 and {2} on e1, so s=(1,1,1).
    e0 = (Q(1), Q(0))
    e1 = (Q(0), Q(1))
    ground, d = d_function([[e0], [e0], [e1]])
    s = {0: Q(1), 1: Q(1), 2: Q(1)}
    for a in subsets(ground):
        assert sum((s[i] for i in a), Q(0)) <= closed_union_rank(a, 2, d)
    assert closed_union_rank(ground, 2, d) == 3


def simplex_gram(m):
    return [
        [Q(1) if i == j else -Q(1, m - 1) for j in range(m)]
        for i in range(m)
    ]


def check_simplex(m):
    g = simplex_gram(m)
    assert rank([tuple(col) for col in zip(*g)]) == m - 1

    # Tight-frame identity for the one-guess POVM: c G^2 = G.
    c1 = Q(m - 1, m)
    assert scale_matrix(c1, matmul(g, g)) == g
    assert c1 == Q(m - 1, m)  # each correct probability

    # Edge-root coefficient frame B=sum (2/m)/norm^2 vv^T.
    norm2 = Q(2 * m, m - 1)
    coeff = Q(2, m) / norm2
    b = [[Q(0) for _ in range(m)] for _ in range(m)]
    pairs = []
    for i, j in combinations(range(m), 2):
        v = [Q(0)] * m
        v[i], v[j] = Q(1), Q(-1)
        outer = [[v[r] * v[c] for c in range(m)] for r in range(m)]
        b = add_matrix(b, scale_matrix(coeff, outer))
        pairs.append((i, j, v))
    # Equality on the simplex span is equivalent to G B G = G.
    assert matmul(matmul(g, b), g) == g

    # Exact conditional probabilities: excluded labels have zero probability;
    # probabilities over pairs containing the true label sum to one.
    for k in range(m):
        success = Q(0)
        failure = Q(0)
        for i, j, v in pairs:
            overlap = sum((v[t] * g[t][k] for t in range(m)), Q(0))
            prob = Q(2, m) * overlap * overlap / norm2
            if k in (i, j):
                success += prob
            else:
                failure += prob
        assert success == 1
        assert failure == 0


def check_two_time_correlation_fixture():
    """Exact quaternion audit of the two-time maximally entangled simplex."""
    # Coordinates are stored without the common factor 1/sqrt(3).
    quaternions = (
        (1, 1, 1, 0),
        (1, -1, -1, 0),
        (-1, 1, -1, 0),
        (-1, -1, 1, 0),
    )

    def dot(x, y):
        return sum(a * b for a, b in zip(x, y))

    assert all(dot(q, q) == 3 for q in quaternions)
    assert all(
        dot(quaternions[i], quaternions[j]) == -1
        for i, j in combinations(range(4), 2)
    )
    assert tuple(sum(q[j] for q in quaternions) for j in range(4)) == (0, 0, 0, 0)

    # Dividing the Gram matrix by 3 gives diagonal 1 and off-diagonal -1/3:
    # the normalized Choi vectors are the m=4 regular simplex.  The generic
    # simplex replay checks the exact one-list value 3/4 and the perfect
    # two-list root-frame POVM.  Maximally entangled unitary Choi states have
    # both reduced states I/2, so either single-time marginal is label-blind.
    assert simplex_gram(4) == [
        [Q(dot(quaternions[i], quaternions[j]), 3) for j in range(4)]
        for i in range(4)
    ]


def check_counterexample():
    # Squared overlaps of the exact qubit vectors in the memo.
    overlaps2 = (Q(4, 5), Q(4, 5), Q(17, 25))
    assert all(x < 1 for x in overlaps2)  # every pair independent: U_(2,3)
    z = (Q(1), Q(3, 5), Q(3, 5))
    assert min(z) > 0  # no nonnegative nonzero barycentre can have z=0

    # Exact primal--dual exclusion certificate.  R^2=1/3 is retained
    # algebraically, so no floating-point square root is used.
    n = (
        (Q(0), Q(0), Q(1)),
        (Q(4, 5), Q(0), Q(3, 5)),
        (Q(0), Q(4, 5), Q(3, 5)),
    )
    u = (Q(1, 3), Q(1, 3), Q(2, 3))
    weights = (Q(1, 3), Q(5, 6), Q(5, 6))

    def dot(x, y):
        return sum((a * b for a, b in zip(x, y)), Q(0))

    def sub(x, y):
        return tuple(a - b for a, b in zip(x, y))

    assert all(dot(sub(u, ni), sub(u, ni)) == Q(1, 3) for ni in n)
    assert all(dot(u, ni) == Q(2, 3) for ni in n)
    assert sum(weights, Q(0)) == 2
    weighted_n = tuple(
        sum((weights[i] * n[i][j] for i in range(3)), Q(0))
        for j in range(3)
    )
    assert weighted_n == tuple(2 * x for x in u)
    # These identities imply |m_i|=1, sum_i w_i m_i=0, and
    # m_i.n_i=-R for R^2=1/3.  Hence primal and dual costs both equal
    # (1-R)/3 and P_list=(2+R)/3.

    e0, e1 = (Q(1), Q(0)), (Q(0), Q(1))
    # Any rational representatives with all pairs independent have the same
    # vector matroid; these avoid complex arithmetic in the rank check.
    ground, d = d_function([[e0], [(Q(2), Q(1))], [(Q(2), Q(-1))]])
    assert all(d(a) == min(2, len(a)) for a in subsets(ground))
    assert closed_union_rank(ground, 2, d) == 3


def check_strict_flat_fixture():
    # Five distinct lines in Q^2 plus one orthogonal coloop in Q^3.
    supports = []
    for t in range(5):
        supports.append([(Q(1), Q(t), Q(0))])
    supports.append([(Q(0), Q(0), Q(1))])
    ground, d = d_function(supports)
    assert d(ground) == 3
    assert closed_union_rank(ground, 2, d) == 5
    priors = (Q(19, 100),) * 5 + (Q(5, 100),)
    # Maximum weight in U_(4,5) direct-sum U_(1,1).
    union_cap = 4 * priors[0] + priors[5]
    assert union_cap == Q(81, 100)
    assert sum(priors, Q(0)) == 1
    assert 2 * d(ground) == len(ground)  # total-dimension cap is 1


def check_process_congruence_rank():
    # A rectangular linear map can only lower the dimension of every support
    # sum.  This exact fixture also checks a strict drop.
    e0, e1, e2 = (Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1))
    supports = [[e0], [e1], [e2], [e0, e1]]
    ground, d0 = d_function(supports)
    # L(x0,x1,x2)=(x0+x2,x1).
    def image(v):
        return (v[0] + v[2], v[1])
    image_supports = [[image(v) for v in space] for space in supports]
    _, dt = d_function(image_supports)
    strict = False
    for a in subsets(ground):
        assert dt(a) <= d0(a)
        strict |= dt(a) < d0(a)
    assert strict


def main():
    checked = check_union_rank_identity()
    check_exact_list_fixture()
    for m in range(3, 9):
        check_simplex(m)
    check_two_time_correlation_fixture()
    check_counterexample()
    check_strict_flat_fixture()
    check_process_congruence_rank()
    print(f"PASS: {checked} exhaustive union-rank cases")
    print("PASS: exact list fixture")
    print("PASS: simplex m=3,...,8 (one-guess and perfect two-list POVMs)")
    print("PASS: two-time correlation-only SU(2)-Choi simplex fixture")
    print("PASS: exact union-full counterexample and primal-dual optimum")
    print("PASS: strict-flat cap 81/100 versus total-dimension cap 1")
    print("PASS: process-congruence rank monotonicity")


if __name__ == "__main__":
    main()
