#!/usr/bin/env python3
"""Exact, lightweight checks for the coherent tetrahedral echo package.

The script is intentionally autonomous: it does not import the Paper 14 code.
It expands all 24 eight-pulse words over the quotient
    Q[c,s]/(c**2 + 3*s**2 - 1),
checks the two A4 order orbits, and verifies the moment identities from which
the Gram/Schmidt spectra follow.  Only 2x2 and 4x4 symbolic algebra is used.
"""

from itertools import permutations
import json

import sympy as sp


c, s, z = sp.symbols("c s z", real=True)
ii = sp.I

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -ii], [ii, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
pauli = (sx, sy, sz)

vertices = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)
kicks = tuple(sum((v[j] * pauli[j] for j in range(3)), sp.zeros(2)) for v in vertices)
relation = sp.Poly(c**2 + 3 * s**2 - 1, c)


def red(expr):
    """Canonical remainder modulo c^2+3s^2-1, with degree <2 in c."""
    poly = sp.Poly(sp.expand(expr), c)
    return sp.expand(poly.rem(relation).as_expr())


def red_matrix(matrix):
    return matrix.applyfunc(red)


def pulse(label, sign):
    """exp(-i sign*y*r_label.sigma) = c I - i sign*s*r_label.sigma."""
    return c * I2 - ii * sign * s * kicks[label]


def ordered_half(order, sign):
    """K_{sigma_4} ... K_{sigma_1}; order[0] acts first."""
    out = I2
    for label in order:
        out = red_matrix(pulse(label, sign) * out)
    return out


def echo(order):
    """Paper convention W_sigma=U_sigma U_{sigma^R}^*."""
    return red_matrix(ordered_half(order, +1) * ordered_half(order, -1))


def parity(order):
    inversions = sum(order[i] > order[j] for i in range(4) for j in range(i + 1, 4))
    return inversions % 2


def require_zero(expr, label):
    value = red(expr)
    if value != 0:
        raise AssertionError(f"{label}: {value}")


def main():
    orders = list(permutations(range(4)))
    q_target_s = 1 - 32 * s**4 + 128 * s**6 - 256 * s**8
    q_target_z = 1 - 32 * z**2 + 128 * z**3 - 256 * z**4

    data = []
    for order in orders:
        word = echo(order)
        q = red(sp.trace(word) / 2)
        require_zero(q - q_target_s, f"half trace {order}")
        vector = tuple(red(ii * sp.trace(p * word) / 2) for p in pauli)
        require_zero(q * q + sum(component * component for component in vector) - 1,
                     f"SU(2) norm {order}")
        data.append((order, parity(order), q, vector))

    orbit_report = {}
    for p, name in ((0, "even"), (1, "odd")):
        orbit = [item for item in data if item[1] == p]
        if len(orbit) != 12:
            raise AssertionError(f"{name} orbit has {len(orbit)} elements")

        mean = [red(sum(item[3][a] for item in orbit)) for a in range(3)]
        for a, value in enumerate(mean):
            require_zero(value, f"{name} first moment component {a}")

        second = sp.Matrix(3, 3, lambda a, b: red(sum(
            item[3][a] * item[3][b] for item in orbit
        )))
        target_second = 4 * (1 - q_target_s**2) * sp.eye(3)
        for a in range(3):
            for b in range(3):
                require_zero(second[a, b] - target_second[a, b],
                             f"{name} second moment ({a},{b})")

        # Hilbert--Schmidt/Bell feature frame.  The -i on vector coordinates
        # is unitary and does not alter its eigenvalues, so a real frame is enough.
        frame = sp.zeros(4)
        for _, _, q, vector in orbit:
            feature = sp.Matrix((q,) + vector)
            frame += feature * feature.T
        frame = red_matrix(frame)
        target_frame = sp.diag(
            12 * q_target_s**2,
            4 * (1 - q_target_s**2),
            4 * (1 - q_target_s**2),
            4 * (1 - q_target_s**2),
        )
        for a in range(4):
            for b in range(4):
                require_zero(frame[a, b] - target_frame[a, b],
                             f"{name} feature frame ({a},{b})")

        orbit_report[name] = {
            "cardinality": len(orbit),
            "first_moment": [str(v) for v in mean],
            "frame_eigenvalues": [
                "12*q^2",
                "4*(1-q^2) [multiplicity 3]",
            ],
        }

    # The displayed representative factorization used in the hand proof.
    representative_factor = (c**2 - s**2) * (
        c**6 + 13 * c**4 * s**2 + 35 * c**2 * s**4 + 79 * s**6
    )
    require_zero(representative_factor - q_target_s, "representative factorization")

    # Tight-frame points q=+/-1/2 and their fundamental-pulse locations.
    A = 512 * z**4 - 256 * z**3 + 64 * z**2
    roots = {}
    for sign, rhs in (("plus", 1), ("minus", 3)):
        candidates = []
        for root in sp.nroots(A - rhs, n=40, maxsteps=100):
            if abs(float(sp.im(root))) < 1e-25:
                value = float(sp.re(root))
                if 0 < value < 1 / 3:
                    candidates.append(value)
        if len(candidates) != 1:
            raise AssertionError(f"{sign} tight equation has candidates {candidates}")
        zv = candidates[0]
        yv = float(sp.asin(sp.sqrt(3 * zv)) / sp.sqrt(3))
        roots[sign] = {"z": zv, "y_fundamental_interval": yv, "A_rhs": rhs}

    derivative = sp.factor(sp.diff(q_target_z, z))
    require_zero(q_target_z.subs(z, sp.Rational(1, 4)), "q(1/4)")

    # Complete pair-collision audit on the fundamental branch s,c >= 0.
    # Every squared distance is at most linear in c after quotient reduction.
    distance_types = {}
    for left, right in __import__("itertools").combinations(range(24), 2):
        distance = sp.factor(red(sum(
            (data[left][3][axis] - data[right][3][axis]) ** 2
            for axis in range(3)
        )))
        if sp.Poly(distance, c).degree() > 1:
            raise AssertionError("collision distance has degree > 1 in c")
        distance_types.setdefault(str(distance), (distance, []))[1].append((left, right))
    if len(distance_types) != 17:
        raise AssertionError(f"expected 17 collision types, got {len(distance_types)}")

    physical_collision_roots = []
    for distance, _pairs in distance_types.values():
        poly_c = sp.Poly(distance, c)
        coeff_c = poly_c.coeff_monomial(c)
        constant = poly_c.coeff_monomial(1)
        eliminated = (constant**2 - coeff_c**2 * (1 - 3 * s**2)
                      if coeff_c != 0 else constant)
        poly_s = sp.Poly(sp.expand(eliminated), s)
        if any(power[0] % 2 for power, coefficient in poly_s.terms() if coefficient):
            raise AssertionError("collision eliminant is not even in s")
        poly_z_expr = sum(
            coefficient * z ** (power[0] // 2)
            for power, coefficient in poly_s.terms()
        )
        square_free = sp.Poly(poly_z_expr, z).sqf_part()
        try:
            candidate_roots = sp.nroots(square_free, n=30, maxsteps=200)
        except Exception:
            candidate_roots = []
            for factor, _multiplicity in sp.factor_list(square_free.as_expr())[1]:
                candidate_roots.extend(sp.nroots(factor, n=30, maxsteps=300))
        for candidate in candidate_roots:
            if abs(float(sp.im(candidate))) > 1e-12:
                continue
            zv = float(sp.re(candidate))
            if not (-1e-12 <= zv <= 1 / 3 + 1e-12):
                continue
            zv = min(max(zv, 0.0), 1 / 3)
            sv = zv**0.5
            cv = max(0.0, 1 - 3 * zv) ** 0.5
            if abs(float(distance.subs({s: sv, c: cv}).evalf())) < 1e-7:
                if not any(abs(zv - known) < 1e-9 for known in physical_collision_roots):
                    physical_collision_roots.append(zv)

    physical_collision_roots.sort()
    expected_collision_roots = [
        0.0,
        0.25,
        0.3311794893111865,
        0.3328743311850982,
    ]
    if len(physical_collision_roots) != 4 or any(
        abs(actual - expected) > 1e-9
        for actual, expected in zip(physical_collision_roots, expected_collision_roots)
    ):
        raise AssertionError(f"unexpected collision roots {physical_collision_roots}")

    def collision_class_sizes(zv):
        sv = zv**0.5
        cv = max(0.0, 1 - 3 * zv) ** 0.5
        parent = list(range(24))

        def find(index):
            while parent[index] != index:
                parent[index] = parent[parent[index]]
                index = parent[index]
            return index

        def union(left, right):
            left, right = find(left), find(right)
            if left != right:
                parent[right] = left

        for left, right in __import__("itertools").combinations(range(24), 2):
            squared = sum(abs(complex(
                (data[left][3][axis] - data[right][3][axis])
                .subs({s: sv, c: cv}).evalf(30)
            )) ** 2 for axis in range(3))
            if squared < 1e-16:
                union(left, right)
        classes = {}
        for index in range(24):
            classes.setdefault(find(index), []).append(index)
        return sorted((len(group) for group in classes.values()), reverse=True)

    expected_unitary_classes = {
        0.0: [24],
        0.25: [4] * 6,
        expected_collision_roots[2]: [2] * 12,
        expected_collision_roots[3]: [2] * 6 + [1] * 12,
    }
    for point, expected in expected_unitary_classes.items():
        actual = collision_class_sizes(point)
        if actual != sorted(expected, reverse=True):
            raise AssertionError(f"collision multiplicities at z={point}: {actual}")

    report = {
        "status": "PASS",
        "word_count": len(data),
        "echo_convention": "W_sigma=U_sigma U_{sigma^R}^*",
        "q_z": str(q_target_z),
        "q_derivative": str(derivative),
        "orbits": orbit_report,
        "tight_points": roots,
        "collision_audit": {
            "distance_types": len(distance_types),
            "physical_z_roots_fundamental_branch": physical_collision_roots,
            "unitary_class_sizes": {
                str(point): collision_class_sizes(point)
                for point in expected_unitary_classes
            },
            "exceptional_polynomials": [
                "4*z-1",
                "64*z^3-4*z-1",
                "256*z^5-64*z^4-16*z^3+12*z^2-1",
            ],
        },
        "zero_point": {
            "z": 0.25,
            "y_fundamental_interval": float(sp.asin(sp.sqrt(sp.Rational(3, 4))) / sp.sqrt(3)),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
