"""Independent fail-closed audit of the d<=7 projected-epigraph replay.

This script does not modify or trust the serialized facet list.  It preserves
pycddlib's ``lin_set`` and, for every projected equality, verifies *both*
orientations as exact nonnegative Farkas combinations of the unrestricted
cone.  This closes a proof-bookkeeping gap in the canonical serializer, which
records the row but not its linearity flag.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import cdd.gmp as cdd_exact


HERE = Path(__file__).resolve().parent
CANONICAL = HERE / "verify_d_le_7_epigraph.py"
CERTIFICATE = HERE / "results" / "d_le_7_epigraph_certificate.json"


def load_canonical():
    spec = importlib.util.spec_from_file_location("paper31_epigraph", CANONICAL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def projected_h_representation(module, n: int, generators):
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
    return facets


def lift(module, facet, gap_count: int):
    row = tuple(module.qvalue(x) for x in facet)
    row = module.normalized(row)
    return row[: 1 + gap_count] + (Q(0),) * gap_count + (row[-1],)


def main() -> None:
    module = load_canonical()
    saved = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    saved_by_case = {
        (item["dimension"], item["positive_count"], item["negative_count"]): item
        for item in saved["chambers"]
    }
    expected_cases = []
    equality_count = 0
    opposite_certificates = 0
    generator_total = 0
    facet_total = 0

    for n in range(3, 8):
        for positive in range(1, n):
            for negative in range(positive, n - positive + 1):
                expected_cases.append((n, positive, negative))
                zero = n - positive - negative
                rank = max(positive, negative)
                gap_count = n - 1
                face_rows = module.cone_rows(n, positive, negative, True)
                full_rows = module.cone_rows(n, positive, negative, False)

                # Structural orientation and rank-face gates.
                assert all(len(row) == 1 + gap_count + rank + 1 for _, row in face_rows)
                assert all(len(row) == 1 + gap_count + gap_count + 1 for _, row in full_rows)
                assert face_rows[-1][0] == "epigraph"
                assert face_rows[-1][1][-rank - 1 : -1] == (Q(-1, 2),) * rank
                assert face_rows[-1][1][-1] == 1
                for index in range(positive, positive + zero):
                    positive_label = f"zero_eigenvalue:{index + 1}:positive"
                    negative_label = f"zero_eigenvalue:{index + 1}:negative"
                    positive_row = next(row for label, row in full_rows if label == positive_label)
                    negative_row = next(row for label, row in full_rows if label == negative_label)
                    assert tuple(-x for x in positive_row) == negative_row

                generators, reduced_count = module.exact_face_generators(face_rows)
                facets = projected_h_representation(module, n, generators)
                generator_total += len(generators.array)
                facet_total += len(facets.array)
                equality_count += len(facets.lin_set)

                # Check every H row in its declared orientation.  Equality rows
                # additionally require the opposite orientation.
                for index, facet in enumerate(facets.array):
                    target = lift(module, facet, gap_count)
                    module.exact_farkas(full_rows, target)
                    if index in facets.lin_set:
                        module.exact_farkas(full_rows, tuple(-x for x in target))
                        opposite_certificates += 1

                saved_case = saved_by_case[(n, positive, negative)]
                assert saved_case["zero_count"] == zero
                assert saved_case["inertia_rank"] == rank
                assert saved_case["reduced_face_row_count"] == reduced_count
                assert saved_case["face_generator_count"] == len(generators.array)
                assert saved_case["projected_facet_count"] == len(facets.array)

    assert len(expected_cases) == 33
    assert set(expected_cases) == set(saved_by_case)
    assert generator_total == 813
    assert facet_total == 272
    assert equality_count == opposite_certificates
    print("PASS: 33 sign/zero strata audited through d=7")
    print(f"PASS: exact face generators={generator_total}, projected H rows={facet_total}")
    print(
        "PASS: preserved lin_set and verified both exact Farkas orientations "
        f"for {equality_count} projected equalities"
    )
    print("PASS: Horn orientation, epigraph sign, inertia face and saved census agree")


if __name__ == "__main__":
    main()
