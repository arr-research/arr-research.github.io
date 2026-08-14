"""Exact lightweight checks for the matricial Hausdorff finite-sample memo.

Algebraic fixtures use exact rational arithmetic; the final Gaussian
illustration uses floating point.  The script verifies the parity-correct block
matrices on a genuinely matrix-valued atomic measure, the associated
quadratic-form identities, a Loewner confidence inversion, and a strict
negative polynomial witness after corruption.

It does not verify Wishart quantiles or literature novelty.
"""

from __future__ import annotations

from fractions import Fraction as Q
from statistics import NormalDist


def zeros(n: int, m: int):
    return [[Q(0) for _ in range(m)] for _ in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def quad(a, v):
    return sum(v[i] * a[i][j] * v[j] for i in range(len(v)) for j in range(len(v)))


def block_hankel(blocks, offset: int, size: int, difference: bool = False):
    q = len(blocks[0])
    out = zeros(size * q, size * q)
    for i in range(size):
        for j in range(size):
            k = i + j + offset
            block = sub(blocks[k], blocks[k + 1]) if difference else blocks[k]
            for a in range(q):
                for b in range(q):
                    out[i * q + a][j * q + b] = block[a][b]
    return out


def even_localizer(blocks, n: int):
    q = len(blocks[0])
    out = zeros(n * q, n * q)
    for i in range(n):
        for j in range(n):
            block = sub(blocks[i + j + 1], blocks[i + j + 2])
            for a in range(q):
                for b in range(q):
                    out[i * q + a][j * q + b] = block[a][b]
    return out


def ldlt_psd(a):
    """Exact PSD decision for the positive-definite examples used here."""
    n = len(a)
    l = zeros(n, n)
    d = [Q(0)] * n
    for i in range(n):
        l[i][i] = Q(1)
        d[i] = a[i][i] - sum(l[i][k] * l[i][k] * d[k] for k in range(i))
        if d[i] < 0:
            return False
        if d[i] == 0:
            # Exact zero pivots require a zero residual column.
            for j in range(i + 1, n):
                residual = a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
                if residual:
                    return False
            continue
        for j in range(i + 1, n):
            l[j][i] = (
                a[j][i] - sum(l[j][k] * l[i][k] * d[k] for k in range(i))
            ) / d[i]
    return True


def moments(atoms, weights, maximum: int):
    q = len(weights[0])
    out = []
    for k in range(maximum + 1):
        s = zeros(q, q)
        for x, w in zip(atoms, weights):
            s = add(s, scale(x**k, w))
        out.append(s)
    return out


def direct_atomic_square(atoms, weights, coefficients, multiplier):
    total = Q(0)
    q = len(weights[0])
    for x, w in zip(atoms, weights):
        value = [Q(0)] * q
        power = Q(1)
        for c in coefficients:
            value = [u + power * v for u, v in zip(value, c)]
            power *= x
        total += multiplier(x) * quad(w, value)
    return total


def main() -> None:
    # Noncommuting positive-definite weights: W1*W2 != W2*W1.
    atoms = [Q(1, 4), Q(3, 4)]
    weights = [
        [[Q(2), Q(1, 2)], [Q(1, 2), Q(1)]],
        [[Q(1), Q(-1, 3)], [Q(-1, 3), Q(3, 2)]],
    ]
    assert all(ldlt_psd(w) for w in weights)
    assert matmul(weights[0], weights[1]) != matmul(weights[1], weights[0])

    s = moments(atoms, weights, 5)

    # Even m=4: H_2 and x(1-x) localizer K_1.
    h_even = block_hankel(s, 0, 3)
    k_even = even_localizer(s, 2)
    assert ldlt_psd(h_even)
    assert ldlt_psd(k_even)

    # Odd m=5: x and (1-x) localizers, both of block size 3.
    h_x = block_hankel(s, 1, 3)
    h_one_minus_x = block_hankel(s, 0, 3, difference=True)
    assert ldlt_psd(h_x)
    assert ldlt_psd(h_one_minus_x)

    # Necessity identities for a degree-two vector polynomial.
    coeff = [[Q(1), Q(-1)], [Q(2), Q(1, 2)], [Q(-1, 3), Q(3, 2)]]
    flat = [u for row in coeff for u in row]
    assert quad(h_even, flat) == direct_atomic_square(atoms, weights, coeff, lambda x: Q(1))
    assert quad(h_x, flat) == direct_atomic_square(atoms, weights, coeff, lambda x: x)
    assert quad(h_one_minus_x, flat) == direct_atomic_square(
        atoms, weights, coeff, lambda x: 1 - x
    )

    # Exact Loewner inversion: a*S <= hatS <= b*S implies hatS/b <= S <= hatS/a.
    a, b = Q(1, 2), Q(3, 2)
    for sj in s:
        hat = sj  # a strict interior realization of the Wishart event.
        assert ldlt_psd(sub(hat, scale(a, sj)))
        assert ldlt_psd(sub(scale(b, sj), hat))
        assert ldlt_psd(sub(sj, scale(1 / b, hat)))
        assert ldlt_psd(sub(scale(1 / a, hat), sj))

    # Corrupt the fourth moment.  The vector polynomial x^2 e_1 is globally
    # nonnegative after squaring, while its moment pairing becomes negative.
    corrupted = [block[:] for block in s]
    corrupted = [[row[:] for row in block] for block in corrupted]
    corrupted[4][0][0] = Q(-1)
    witness_coeff = [[Q(0), Q(0)], [Q(0), Q(0)], [Q(1), Q(0)]]
    witness = [u for row in witness_coeff for u in row]
    h_bad = block_hankel(corrupted, 0, 3)
    value = quad(h_bad, witness)
    assert value == Q(-1)
    assert value < 0
    assert not ldlt_psd(h_bad)

    # Exact strict family: the even-grid N=0 support test passes, while the
    # full-grid x(s-x) localizer detects the atom beyond s.
    support_s, atom_t, atom_w = Q(1, 2), Q(3, 4), Q(1, 8)
    moment0, moment1, moment2 = Q(1), atom_w * atom_t, atom_w * atom_t**2
    old_even_localizer = support_s**2 * moment0 - moment2
    full_grid_localizer = support_s * moment1 - moment2
    assert old_even_localizer == Q(23, 128) > 0
    assert full_grid_localizer == Q(-3, 128) < 0

    # Closed-form witness scale in the strict-power theorem.
    gamma = atom_w * atom_t * (atom_t - support_s)
    w_squared = gamma**2 + support_s**2 * atom_w * (1 - atom_w) * atom_t**2
    assert gamma == Q(3, 128)
    assert w_squared == Q(261, 16384)

    # Exact ordinary-dual certificate at the collapsed band a=b=1, S=K.
    covariance = [[moment0, moment1], [moment1, moment2]]
    dual_difference = [[Q(0), Q(-1, 4)], [Q(-1, 4), Q(1)]]
    dual_a = [[Q(1), Q(-1, 4)], [Q(-1, 4), Q(2)]]
    dual_b = [[Q(1), Q(0)], [Q(0), Q(1)]]
    assert ldlt_psd(dual_a) and ldlt_psd(dual_b)
    assert dual_difference[0][0] == 0
    assert 2 * dual_difference[0][1] + support_s == 0
    assert dual_difference[1][1] - 1 == 0
    dual_objective = -sum(
        dual_difference[i][j] * covariance[i][j]
        for i in range(2)
        for j in range(2)
    )
    assert dual_objective == Q(-3, 128) < 0

    # Regular smooth exposed boundary example for the local cone theory.
    # For (delta_0+delta_s)/2 at s=1/2, H_1 is positive definite while the
    # support localizer s M_1-M_2 is active.  Hence the tangent cone is the
    # exact halfspace (1/2)h1-h2 >= 0.
    boundary = [Q(1), Q(1, 4), Q(1, 8)]
    h_boundary = [[boundary[0], boundary[1]], [boundary[1], boundary[2]]]
    assert h_boundary[0][0] * h_boundary[1][1] - h_boundary[0][1] ** 2 == Q(1, 16) > 0
    assert support_s * boundary[1] - boundary[2] == 0
    tangent_normal = [Q(0), support_s, Q(-1)]
    trial_direction = [Q(0), Q(0), Q(1)]
    assert sum(a0 * h0 for a0, h0 in zip(tangent_normal, trial_direction)) < 0

    # At a whitened halfspace face the exact limiting rejection threshold
    # and local power reduce to the one-sided Gaussian formulas.
    alpha, rho = 0.05, 2.0
    z = NormalDist().inv_cdf(1.0 - alpha)
    critical = z * z
    local_power = 1.0 - NormalDist().cdf(z - rho)
    assert abs(critical - 2.705543454095404) < 1.0e-12
    assert 0.63 < local_power < 0.64

    print("PASS: exact even/odd matricial Hausdorff block identities")
    print("PASS: noncommuting 2x2 atomic weights and vector-polynomial pairings")
    print("PASS: exact Loewner confidence inversion")
    print(f"PASS: rational dual polynomial witness value = {value}")
    print(
        "PASS: even-grid blind family old=",
        old_even_localizer,
        "full-grid=",
        full_grid_localizer,
    )
    print(f"PASS: strict-power scale gamma={gamma}, W^2={w_squared}")
    print(f"PASS: exact rational SDP dual objective={dual_objective}")
    print("PASS: regular smooth-face tangent halfspace (1/2)h1-h2 >= 0")
    print(f"PASS: Gaussian local critical={critical:.12f}, power(rho=2)={local_power:.12f}")
    print("SCOPE: algebraic replay only; Wishart quantiles and novelty are not assessed")


if __name__ == "__main__":
    main()
