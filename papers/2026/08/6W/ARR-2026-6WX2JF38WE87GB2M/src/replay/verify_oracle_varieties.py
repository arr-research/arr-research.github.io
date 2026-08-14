"""Fail-closed exact checks for the algebraic oracle-support paper."""

from fractions import Fraction as Q
from math import comb, factorial
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def double_factorial(n):
    if n <= 0:
        return 1
    out = 1
    for j in range(n, 0, -2):
        out *= j
    return out


def legendre_moment(j, ell):
    if j < ell or (j - ell) % 2:
        return Q(0)
    return Q(factorial(j), double_factorial(j - ell) * double_factorial(j + ell + 1))


def sphere_eigenvalue(k, ell, a):
    b = 1 - a
    return sum(
        Q(comb(k, j)) * a ** (k - j) * b**j * legendre_moment(j, ell)
        for j in range(ell, k + 1)
    )


def circle_eigenvalue(k, m, a):
    b = 1 - a
    return sum(
        Q(comb(k, j) * comb(j, (j - m) // 2), 2**j) * a ** (k - j) * b**j
        for j in range(abs(m), k + 1)
        if (j - m) % 2 == 0
    )


def sphere_purity(k, a):
    b = 1 - a
    if b == 0:
        return Q(1)
    return (Q(1) - (a - b) ** (2 * k + 1)) / (2 * b * (2 * k + 1))


def main():
    priors = [Q(7, 20), Q(1, 4), Q(1, 5), Q(3, 20), Q(1, 20)]
    for d in range(1, len(priors) + 1):
        exact_rank_cap = sum(sorted(priors, reverse=True)[:d])
        require(exact_rank_cap <= min(Q(1), d * max(priors)), "nonuniform prior cap")

    for k in range(1, 13):
        ambient = comb(k + 3, 3)
        sphere_rank = (k + 1) ** 2
        require(ambient - comb(k + 1, 3) == sphere_rank, "quadric Hilbert rank")
        require(ambient - sphere_rank == comb(k + 1, 3), "ambient deficit")
        require(sum(2 * ell + 1 for ell in range(k + 1)) == sphere_rank, "harmonic rank")
        require(
            sum(2 * ell + 1 for ell in range(k % 2, k + 1, 2)) == comb(k + 2, 2),
            "traceless rank",
        )
        require(comb(k + 2, 2) - comb(k, 2) == 2 * k + 1, "conic Hilbert rank")

        for a in (Q(1, 11), Q(1, 4), Q(2, 5), Q(3, 4)):
            values = [sphere_eigenvalue(k, ell, a) for ell in range(k + 1)]
            require(all(value > 0 for value in values), "sphere spectrum positivity")
            require(sum((2 * ell + 1) * values[ell] for ell in range(k + 1)) == 1, "sphere trace")
            require(
                sum((2 * ell + 1) * values[ell] ** 2 for ell in range(k + 1))
                == sphere_purity(k, a),
                "sphere purity",
            )
            leverage = sum(Q(2 * ell + 1) for ell, value in enumerate(values) if value > 0)
            require(leverage == sphere_rank, "constant orbit leverage")

        traceless = [sphere_eigenvalue(k, ell, Q(0)) for ell in range(k + 1)]
        for ell, value in enumerate(traceless):
            require((value > 0) == ((k - ell) % 2 == 0), "traceless parity")
            if (k - ell) % 2:
                linear_coefficient = k * legendre_moment(k - 1, ell)
                expected = Q(
                    factorial(k),
                    double_factorial(k - ell - 1) * double_factorial(k + ell),
                )
                require(linear_coefficient == expected, "traceless linear cascade")

        for a in (Q(1, 11), Q(1, 4), Q(2, 5)):
            circle = [circle_eigenvalue(k, m, a) for m in range(-k, k + 1)]
            require(all(value > 0 for value in circle), "circle spectrum positivity")
            require(sum(circle) == 1, "circle trace")
        circle_zero = [circle_eigenvalue(k, m, Q(0)) for m in range(-k, k + 1)]
        require(sum(value > 0 for value in circle_zero) == k + 1, "traceless circle rank")

    for d in range(2, 9):
        for k in range(1, 9):
            segre = comb(k + d - 1, d - 1) ** 2
            ambient = comb(k + d * d - 1, d * d - 1)
            require(segre <= ambient, "Segre support exceeds ambient support")
            if k == 1:
                require(segre == d * d, "one-query Segre support")
            if k == 2:
                require(
                    ambient - segre == d * d * (d - 1) ** 2 // 4,
                    "two-query qudit defect",
                )
        require(comb(d + 1, d - 1) ** 2 <= comb(d * d + 1, d * d - 1), "qutrit fixture")

    require(sphere_eigenvalue(1, 0, Q(1, 4)) == Q(1, 4), "one-query scalar sector")
    require(sphere_eigenvalue(1, 1, Q(1, 4)) == Q(1, 4), "one-query vector sector")
    require(sphere_eigenvalue(1, 1, Q(0)) == Q(1, 3), "traceless tight endpoint")

    for k in range(2, 50):
        a = Q(1, 2 * k + 2)
        top = sphere_eigenvalue(k, k, a)
        require(sphere_eigenvalue(k, k - 1, a) / top == 1, "forced top-pair equality")
        third = sphere_eigenvalue(k, k - 2, a) / top
        require(third == Q(k * (2 * k + 3), 2 * k + 1), "third-sector ratio")
        require(third != 1, "false higher-query tightness")

    print("PASS oracle-variety exact checks")
    print("quadric/conic/Segre ranks; sphere/circle spectra; purity; endpoints; harmonic support/leverage value")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
