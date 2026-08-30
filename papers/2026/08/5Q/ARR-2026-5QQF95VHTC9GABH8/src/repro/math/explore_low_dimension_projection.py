"""Explore the low-dimensional rank-optimality question by polyhedral projection.

For a fixed dimension ``d`` and inertia split ``m+(d-m)``, compare two
homogeneous epigraph cones in the variables ``(lambda,z)``:

* the full Horn cone for singular-value vectors ``p``; and
* its face ``p_{r+1}=...=p_{d-1}=0``, where
  ``r=max(m,d-m)`` is the inertia lower bound.

Equality of the projections says that every trace-zero spectrum in that
inertia chamber has a nuclear-norm minimizer of rank exactly ``r``.  cddlib is
used only to discover/project generators in floating arithmetic.  A later
canonical verifier must rationalize and certify every resulting containment;
this exploratory file is deliberately not itself a proof certificate.
"""

from __future__ import annotations

import argparse
import itertools
import time
from functools import lru_cache

import cdd


@lru_cache(None)
def horn_t(r: int, n: int):
    subsets = tuple(itertools.combinations(range(1, n + 1), r))
    out = []
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
                    out.append((I, J, K))
    return tuple(out)


def horn_row(n: int, I, J):
    row = [0] * (n - 1)
    for i in I:
        if i < n:
            row[i - 1] += 1
    for j in J:
        if j > 1:
            row[n - j] -= 1
    return row


def lambda_coefficient(d: int, K):
    """Coefficients of ``-2 sum_{k in K} lambda_k`` after eliminating lambda_d."""

    has_last = int(d in K)
    return [-2 * (int(j in K) - has_last) for j in range(1, d)]


def chamber_rows(d: int, m: int, p_count: int):
    """Return cdd H rows ``[0, lambda variables, p variables, z]``."""

    assert 1 <= m < d
    nvars = (d - 1) + p_count + 1
    rows = []

    def emit(coeff):
        assert len(coeff) == nvars
        rows.append([0, *coeff])

    # Ordered lambda_1 >= ... >= lambda_d, with lambda_d=-sum_{j<d} lambda_j.
    for j in range(d - 2):
        coeff = [0] * nvars
        coeff[j] = 1
        coeff[j + 1] = -1
        emit(coeff)
    coeff = [0] * nvars
    for j in range(d - 2):
        coeff[j] = 1
    coeff[d - 2] = 2
    emit(coeff)

    # Inertia chamber: lambda_m >= 0 >= lambda_{m+1}.  Boundary points are allowed.
    coeff = [0] * nvars
    coeff[m - 1] = 1
    emit(coeff)
    coeff = [0] * nvars
    if m + 1 < d:
        coeff[m] = -1
    else:
        for j in range(d - 1):
            coeff[j] = 1
    emit(coeff)

    # Horn inequalities for gamma=2 lambda.
    for q in range(1, d):
        for I, J, K in horn_t(q, d):
            coeff = lambda_coefficient(d, K)
            pcoeff = horn_row(d, I, J)[:p_count]
            emit(coeff + pcoeff + [0])

    # p is decreasing and nonnegative on the retained face.
    for j in range(p_count - 1):
        coeff = [0] * nvars
        coeff[d - 1 + j] = 1
        coeff[d - 1 + j + 1] = -1
        emit(coeff)
    coeff = [0] * nvars
    coeff[d - 1 + p_count - 1] = 1
    emit(coeff)

    # Epigraph: z >= (1/2) sum p.  Clear denominators.
    coeff = [0] * nvars
    for j in range(p_count):
        coeff[d - 1 + j] = -1
    coeff[-1] = 2
    emit(coeff)
    return rows


def generators_from_h(rows, reduce_rows: bool = True):
    mat = cdd.matrix_from_array(rows, rep_type=cdd.RepType.INEQUALITY)
    if reduce_rows:
        redundant, _positions = cdd.matrix_redundancy_remove(mat)
        print(
            f"  redundancy removal: removed={len(redundant)}, retained={len(mat.array)}",
            flush=True,
        )
    poly = cdd.polyhedron_from_matrix(mat, row_order=cdd.RowOrderType.MIN_CUTOFF)
    return cdd.copy_generators(poly)


def project_generators(generators, d: int, p_count: int):
    """Keep homogeneous coordinate, lambda_1..lambda_{d-1}, and z."""

    keep = [0, *range(1, d), d + p_count]
    projected = []
    projected_lin = set()
    for old_index, row in enumerate(generators.array):
        new = [row[j] for j in keep]
        if all(abs(x) <= 1e-12 for x in new[1:]):
            continue
        if old_index in generators.lin_set:
            projected_lin.add(len(projected))
        projected.append(new)
    mat = cdd.matrix_from_array(
        projected,
        lin_set=projected_lin,
        rep_type=cdd.RepType.GENERATOR,
    )
    poly = cdd.polyhedron_from_matrix(mat)
    return mat, cdd.copy_inequalities(poly)


def minimum_slack(h_rows, generators):
    minimum = float("inf")
    worst = None
    violations = 0
    for hi, h in enumerate(h_rows.array):
        for gi, g in enumerate(generators.array):
            value = sum(a * b for a, b in zip(h, g))
            if gi in generators.lin_set:
                value = -abs(value)
            if value < minimum:
                minimum = value
                worst = (hi, gi, value)
            if value < -1e-7:
                violations += 1
    return minimum, worst, violations


def run(d: int, m: int, face_only: bool = False):
    r = max(m, d - m)
    if r >= d:
        raise ValueError("empty inertia chamber")
    print(f"case d={d}, m={m}, inertia rank r={r}", flush=True)

    full_h = chamber_rows(d, m, d - 1)
    face_h = chamber_rows(d, m, r)
    print(f"H rows: full={len(full_h)}, face={len(face_h)}", flush=True)

    start = time.perf_counter()
    face_g = generators_from_h(face_h)
    print(
        f"face H->V: {len(face_g.array)} generators, "
        f"{len(face_g.lin_set)} lines, {time.perf_counter()-start:.3f}s",
        flush=True,
    )

    face_proj_v, face_proj_h = project_generators(face_g, d, r)
    print(
        f"face projected: V={len(face_proj_v.array)}, H={len(face_proj_h.array)}, "
        f"{time.perf_counter()-start:.3f}s",
        flush=True,
    )
    if face_only:
        for row in face_proj_h.array:
            print("H", " ".join(f"{x:.12g}" for x in row))
        return True

    start = time.perf_counter()
    full_g = generators_from_h(full_h)
    print(
        f"full H->V: {len(full_g.array)} generators, "
        f"{len(full_g.lin_set)} lines, {time.perf_counter()-start:.3f}s",
        flush=True,
    )
    start = time.perf_counter()
    full_proj_v, _full_proj_h = project_generators(full_g, d, d - 1)
    print(
        f"projected: full V={len(full_proj_v.array)}, "
        f"face V={len(face_proj_v.array)}, face H={len(face_proj_h.array)}, "
        f"{time.perf_counter()-start:.3f}s",
        flush=True,
    )
    minimum, worst, violations = minimum_slack(face_proj_h, full_proj_v)
    print(f"full subset face: min_slack={minimum:.12g}, worst={worst}, violations={violations}")
    return violations == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("d", type=int)
    parser.add_argument("m", type=int)
    parser.add_argument("--face-only", action="store_true")
    args = parser.parse_args()
    raise SystemExit(0 if run(args.d, args.m, args.face_only) else 1)
