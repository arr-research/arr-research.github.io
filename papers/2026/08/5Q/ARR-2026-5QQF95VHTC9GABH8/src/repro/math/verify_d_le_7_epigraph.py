"""Exact projected-epigraph proof of inertia-rank optimality for d <= 7.

For each non-equivalent sign chamber, this script constructs the Horn primal
cone on the inertia-rank face, projects it to (spectral gaps, cost), and obtains
an exact GMP-rational facet description.  It then proves every projected
facet valid on the unrestricted Horn cone by an exact nonnegative Farkas
certificate.

Floating-point cdd/scipy calls are used only to propose redundant rows and
sparse supports.  Every proposed reduction and every Farkas identity is
subsequently checked over exact rationals; the replay fails closed otherwise.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from functools import lru_cache

import cdd
import cdd.gmp as cdd_exact
import numpy as np
import sympy as sp
from scipy.optimize import linprog


@lru_cache(None)
def horn_t(r: int, n: int):
    subsets = tuple(itertools.combinations(range(1, n + 1), r))
    triples = []
    for I in subsets:
        for J in subsets:
            for K in subsets:
                if sum(I) + sum(J) != sum(K) + r * (r + 1) // 2:
                    continue
                valid = True
                for q in range(1, r):
                    for F, G, H in horn_t(q, r):
                        lhs = sum(I[f - 1] for f in F)
                        lhs += sum(J[g - 1] for g in G)
                        rhs = sum(K[h - 1] for h in H)
                        rhs += q * (q + 1) // 2
                        if lhs > rhs:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    triples.append((I, J, K))
    return tuple(triples)


def lambda_rows(n: int):
    """Rows expressing ordered trace-zero eigenvalues in adjacent gaps."""

    return tuple(
        tuple(Q(int(i >= k)) - Q(i, n) for i in range(1, n))
        for k in range(1, n + 1)
    )


def horn_row(n: int, I, J):
    row = [Q(0)] * (n - 1)
    for i in I:
        if i < n:
            row[i - 1] += 1
    for j in J:
        if j > 1:
            row[n - j] -= 1
    return tuple(row)


def spectral_constraints(n: int):
    """Rows a.p >= b.g in the suppressed-final-zero Horn program."""

    lam = lambda_rows(n)
    rows = []
    for r in range(1, n):
        for I, J, K in horn_t(r, n):
            rhs = tuple(
                sum((2 * lam[k - 1][u] for k in K), Q(0))
                for u in range(n - 1)
            )
            rows.append((f"H{r}:{I}:{J}:{K}", horn_row(n, I, J), rhs))
    for i in range(n - 2):
        row = [Q(0)] * (n - 1)
        row[i], row[i + 1] = Q(1), Q(-1)
        rows.append((f"order:{i + 1}", tuple(row), (Q(0),) * (n - 1)))
    row = [Q(0)] * (n - 1)
    row[-1] = Q(1)
    rows.append(("nonnegative", tuple(row), (Q(0),) * (n - 1)))
    return tuple(rows)


def qvalue(x):
    return Q(str(x))


def qtext(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def normalized(row):
    row = tuple(qvalue(x) for x in row)
    pivot = next(x for x in row if x)
    # H-row orientation is meaningful: only positive rescaling preserves the
    # inequality.  Normalize by the absolute pivot, never by a negative pivot.
    return tuple(x / abs(pivot) for x in row)


def cone_rows(n: int, positive_count: int, negative_count: int, face: bool):
    """Homogeneous H rows in variables (g,p,z), with leading constant zero."""

    gap_count = n - 1
    zero_count = n - positive_count - negative_count
    assert positive_count >= 1 and negative_count >= 1 and zero_count >= 0
    inertia_rank = max(positive_count, negative_count)
    p_count = inertia_rank if face else gap_count
    rows = []
    seen = set()
    for label, a, b in spectral_constraints(n):
        truncated = a[:p_count]
        key = (truncated, b)
        if key not in seen:
            seen.add(key)
            rows.append(
                (
                    label,
                    (Q(0),) + tuple(-x for x in b) + truncated + (Q(0),),
                )
            )

    # Ordered-spectrum gap cone.
    for i in range(gap_count):
        row = [Q(0)] * (1 + gap_count + p_count + 1)
        row[1 + i] = Q(1)
        rows.append((f"gap_nonnegative:{i + 1}", tuple(row)))

    lam = lambda_rows(n)
    # Exact inertia stratum: positive block, an optional zero block, then the
    # negative block.  Each prescribed zero is encoded by both orientations
    # so later Farkas certificates can retain nonnegative multipliers only.
    rows.append(
        (
            "chamber_positive_edge",
            (Q(0),) + lam[positive_count - 1] + (Q(0),) * (p_count + 1),
        )
    )
    for index in range(positive_count, positive_count + zero_count):
        rows.append(
            (
                f"zero_eigenvalue:{index + 1}:positive",
                (Q(0),) + lam[index] + (Q(0),) * (p_count + 1),
            )
        )
        rows.append(
            (
                f"zero_eigenvalue:{index + 1}:negative",
                (Q(0),)
                + tuple(-x for x in lam[index])
                + (Q(0),) * (p_count + 1),
            )
        )
    negative_edge = positive_count + zero_count
    rows.append(
        (
            "chamber_negative_edge",
            (Q(0),)
            + tuple(-x for x in lam[negative_edge])
            + (Q(0),) * (p_count + 1),
        )
    )

    # Epigraph coordinate z >= (1/2) sum p_j.
    rows.append(
        (
            "epigraph",
            (Q(0),)
            + (Q(0),) * gap_count
            + (Q(-1, 2),) * p_count
            + (Q(1),),
        )
    )
    return tuple(rows)


def exact_face_generators(rows):
    """Numerically suggest a reduction, then validate it exactly."""

    array = [row for _, row in rows]
    floating = cdd.matrix_from_array(
        [[float(x) for x in row] for row in array],
        rep_type=cdd.RepType.INEQUALITY,
    )
    redundant, _ = cdd.matrix_redundancy_remove(floating)
    kept = [i for i in range(len(array)) if i not in redundant]
    reduced = cdd_exact.matrix_from_array(
        [array[i] for i in kept], rep_type=cdd_exact.RepType.INEQUALITY
    )
    generators = cdd_exact.copy_generators(cdd_exact.polyhedron_from_matrix(reduced))
    assert not generators.lin_set

    # Exact fail-closed proof that every discarded row was redundant.
    for label, row in rows:
        for generator in generators.array:
            assert dot(row, tuple(qvalue(x) for x in generator)) >= 0, label
    return generators, len(kept)


def projected_face_facets(n: int, generators):
    gap_count = n - 1
    projected = [
        [row[0]] + list(row[1 : 1 + gap_count]) + [row[-1]]
        for row in generators.array
    ]
    matrix = cdd_exact.matrix_from_array(
        projected,
        rep_type=cdd_exact.RepType.GENERATOR,
        lin_set=generators.lin_set,
    )
    facets = cdd_exact.copy_inequalities(cdd_exact.polyhedron_from_matrix(matrix))
    cdd_exact.matrix_canonicalize(facets)
    return tuple(sorted({normalized(row) for row in facets.array}))


def exact_farkas(rows, target):
    """Recover and verify a sparse nonnegative exact conic combination."""

    arrays = [row for _, row in rows]
    matrix = np.asarray([[float(x) for x in row] for row in arrays], dtype=float).T
    result = linprog(
        np.zeros(len(arrays)),
        A_eq=matrix,
        b_eq=np.asarray([float(x) for x in target]),
        bounds=(0.0, None),
        method="highs-ds",
    )
    assert result.success, result.message

    for tolerance in (1e-8, 1e-10, 1e-12):
        support = [i for i, value in enumerate(result.x) if value > tolerance]
        if not support:
            continue
        exact_matrix = sp.Matrix(
            [
                [sp.Rational(arrays[i][j].numerator, arrays[i][j].denominator) for i in support]
                for j in range(len(target))
            ]
        )
        exact_target = sp.Matrix(
            [sp.Rational(x.numerator, x.denominator) for x in target]
        )
        solution_set = sp.linsolve((exact_matrix, exact_target))
        solution = next(iter(solution_set), None)
        if solution is None or any(x.free_symbols for x in solution):
            continue
        weights = tuple(Q(int(x.p), int(x.q)) for x in solution)
        if any(x < 0 for x in weights):
            continue
        reconstructed = tuple(
            sum((weights[u] * arrays[index][j] for u, index in enumerate(support)), Q(0))
            for j in range(len(target))
        )
        if reconstructed == target:
            return tuple((rows[index][0], qtext(weights[u])) for u, index in enumerate(support))
    raise AssertionError("failed to recover an exact nonnegative Farkas certificate")


def verify_chamber(n: int, positive_count: int, negative_count: int):
    gap_count = n - 1
    zero_count = n - positive_count - negative_count
    inertia_rank = max(positive_count, negative_count)
    face_rows = cone_rows(n, positive_count, negative_count, True)
    generators, reduced_count = exact_face_generators(face_rows)
    facets = projected_face_facets(n, generators)

    full_rows = cone_rows(n, positive_count, negative_count, False)
    certificates = []
    for facet in facets:
        # Lift (constant,g,z) to (constant,g,p,z) with zero p coefficients.
        target = facet[: 1 + gap_count] + (Q(0),) * gap_count + (facet[-1],)
        certificates.append(exact_farkas(full_rows, target))

    canonical = {
        "dimension": n,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "zero_count": zero_count,
        "inertia_rank": inertia_rank,
        "horn_counts_by_size": [len(horn_t(r, n)) for r in range(1, n)],
        "full_cone_row_count": len(full_rows),
        "face_cone_row_count": len(face_rows),
        "reduced_face_row_count": reduced_count,
        "face_generator_count": len(generators.array),
        "projected_facet_count": len(facets),
        "projected_facets": [[qtext(x) for x in row] for row in facets],
        "farkas_certificates": certificates,
    }
    stream = json.dumps(canonical, sort_keys=True, separators=(",", ":"))
    canonical["certificate_sha256"] = hashlib.sha256(stream.encode()).hexdigest()
    return canonical


def main():
    chambers = []
    # Sign reflection covers positive_count > negative_count.  We enumerate
    # every possible zero multiplicity explicitly, so the face rank is the
    # literal inertia max(n_+,n_-), including singular spectra.
    for n in range(3, 8):
        for positive_count in range(1, n):
            for negative_count in range(positive_count, n - positive_count + 1):
                chambers.append(verify_chamber(n, positive_count, negative_count))

    payload = {
        "status": "PASS",
        "claim": (
            "for every traceless Hermitian target in dimensions d<=7, the "
            "unrestricted inverse self-commutator optimum is attained at the "
            "inertia lower-bound rank"
        ),
        "method": "exact projected face epigraphs plus exact Farkas containment",
        "dimension_1_and_2": "elementary; no nontrivial chamber enumeration needed",
        "sign_reflection": "covers the omitted positive_count > negative_count strata",
        "chambers": chambers,
        "limitations": [
            "does not classify optimizer matrices",
            "does not prove a universal rank-excess bound above dimension seven",
            "uses pycddlib GMP, scipy, sympy, and numpy",
            "does not assess novelty or priority",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
