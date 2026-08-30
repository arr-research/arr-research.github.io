#!/usr/bin/env python3
"""Exact dictionary replay for hive coarse-graining and its rank corollary.

The row identities are integer identities.  ``--max-t`` controls regression
instances only; the accompanying audit proves the same telescoping formulas
for an arbitrary positive block size.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
PAPER31_FRONTIER = HERE.parent / "math" / "verify_rank_gap_frontier.py"
PAPER31_SHA256 = "00bdbbfd8adbf3aff8f847ae3574241fc7bed887573c8fa6142bb242cf874be7"
FINITE_CERT = HERE / "exact_hive_duals.json"
FINITE_CERT_SHA256 = "c6b3588a2415db067f7ff34f7e23592ac9d85f3e10399dd0f8838fc244352b69"


Vector = dict[tuple, Fraction]


def clean(vector: Vector) -> Vector:
    return {key: value for key, value in vector.items() if value}


def add(*vectors: Vector) -> Vector:
    result: Vector = {}
    for vector in vectors:
        for key, value in vector.items():
            result[key] = result.get(key, Fraction(0)) + value
    return clean(result)


def scale(coefficient: int | Fraction, vector: Vector) -> Vector:
    return clean({key: Fraction(coefficient) * value for key, value in vector.items()})


def atom(kind: str, *indices: int) -> Vector:
    return {(kind, *indices): Fraction(1)}


def h(i: int, level: int) -> Vector:
    if not 0 <= i <= level:
        raise AssertionError((i, level))
    return atom("h", i, level)


def p(index: int, fine_n: int) -> Vector:
    # The normalized final singular square p_n is the literal zero vector.
    if not 1 <= index <= fine_n:
        raise AssertionError(index)
    return {} if index == fine_n else atom("p", index)


def gamma(index: int, fine_n: int) -> Vector:
    if not 1 <= index <= fine_n:
        raise AssertionError(index)
    return atom("gamma", index)


def row1(node, i: int, level: int) -> Vector:
    return add(node(i, level + 1), node(i - 1, level), scale(-1, node(i - 1, level + 1)), scale(-1, node(i, level)))


def row2(node, i: int, level: int) -> Vector:
    return add(node(i, level + 1), node(i, level), scale(-1, node(i + 1, level + 1)), scale(-1, node(i - 1, level)))


def row3(node, i: int, level: int) -> Vector:
    return add(node(i, level), node(i - 1, level), scale(-1, node(i, level + 1)), scale(-1, node(i - 1, level - 1)))


def block_p(factor: int, coarse_index: int, coarse_n: int) -> Vector:
    fine_n = factor * coarse_n
    start = factor * (coarse_index - 1) + 1
    return add(*(p(index, fine_n) for index in range(start, start + factor)))


def block_gamma(factor: int, coarse_index: int, coarse_n: int) -> Vector:
    fine_n = factor * coarse_n
    start = factor * (coarse_index - 1) + 1
    return add(*(gamma(index, fine_n) for index in range(start, start + factor)))


def coarse_h(factor: int, i: int, level: int) -> Vector:
    return h(factor * i, factor * level)


def normalized_h(factor: int, coarse_n: int, i: int, level: int) -> Vector:
    # H'(I,L)=H(I,L)+A_N(I-L), where A_N is the last alpha block.
    last = block_p(factor, coarse_n, coarse_n)
    return add(coarse_h(factor, i, level), scale(i - level, last))


def normalized_p(factor: int, coarse_index: int, coarse_n: int) -> Vector:
    return add(block_p(factor, coarse_index, coarse_n), scale(-1, block_p(factor, coarse_n, coarse_n)))


def fine_alpha(fine_n: int, j: int) -> Vector:
    return add(h(0, j), scale(-1, h(0, j - 1)), scale(-1, p(j, fine_n)))


def fine_beta(fine_n: int, j: int) -> Vector:
    boundary = p(fine_n - j + 1, fine_n)
    return add(h(j, fine_n), scale(-1, h(j - 1, fine_n)), boundary)


def fine_gamma(fine_n: int, j: int) -> Vector:
    return add(h(j, j), scale(-1, h(j - 1, j - 1)), scale(-1, gamma(j, fine_n)))


def fine_order(fine_n: int, j: int) -> Vector:
    if not 1 <= j < fine_n:
        raise AssertionError(j)
    return add(p(j, fine_n), scale(-1, p(j + 1, fine_n)))


def check_rows(coarse_n: int, factor: int) -> int:
    if factor < 1:
        raise ValueError(factor)
    checked = 0
    node = lambda i, level: normalized_h(factor, coarse_n, i, level)
    for level in range(1, coarse_n):
        for i in range(1, level + 1):
            a0 = factor * (i - 1) + 1
            a1 = factor * i

            fine = add(*(
                row1(h, a, ell)
                for a in range(a0, a1 + 1)
                for ell in range(factor * level, factor * level + factor)
            ))
            assert row1(node, i, level) == fine

            fine = add(*(
                row2(h, a + q, factor * level + q)
                for a in range(a0, a1 + 1)
                for q in range(factor)
            ))
            assert row2(node, i, level) == fine

            fine = add(*(
                row3(h, factor * (i - 1) + a, factor * (level - 1) + a + q)
                for a in range(1, factor + 1)
                for q in range(factor)
            ))
            assert row3(node, i, level) == fine
            checked += 3
    return checked


def check_boundaries(coarse_n: int, factor: int) -> int:
    fine_n = coarse_n * factor
    node = lambda i, level: normalized_h(factor, coarse_n, i, level)
    checked = 0
    for j in range(1, coarse_n + 1):
        start = factor * (j - 1) + 1
        stop = factor * j + 1
        coarse = add(node(0, j), scale(-1, node(0, j - 1)), scale(-1, normalized_p(factor, j, coarse_n)))
        assert coarse == add(*(fine_alpha(fine_n, index) for index in range(start, stop)))

        coarse = add(
            node(j, coarse_n), scale(-1, node(j - 1, coarse_n)),
            normalized_p(factor, coarse_n - j + 1, coarse_n),
        )
        assert coarse == add(*(fine_beta(fine_n, index) for index in range(start, stop)))

        coarse = add(node(j, j), scale(-1, node(j - 1, j - 1)), scale(-1, block_gamma(factor, j, coarse_n)))
        assert coarse == add(*(fine_gamma(fine_n, index) for index in range(start, stop)))
        checked += 3
    return checked


def check_order(coarse_n: int, factor: int) -> int:
    fine_n = coarse_n * factor
    for j in range(1, coarse_n):
        coarse = add(normalized_p(factor, j, coarse_n), scale(-1, normalized_p(factor, j + 1, coarse_n)))
        # Pair the q-th entry of block j with the q-th entry of block j+1,
        # then telescope each difference across factor adjacent fine orders.
        fine = add(*(
            fine_order(fine_n, adjacent)
            for q in range(1, factor + 1)
            for adjacent in range(factor * (j - 1) + q, factor * j + q)
        ))
        assert coarse == fine
    # Q_N is identically zero; hence the preceding coarse order rows imply
    # Q_1>=...>=Q_(N-1)>=Q_N=0.
    assert not normalized_p(factor, coarse_n, coarse_n)
    return coarse_n - 1


def check_objective_and_rank(factor: int) -> None:
    coarse_n = 27
    fine_n = factor * coarse_n
    fine_twice_cost = add(*(p(index, fine_n) for index in range(1, fine_n)))
    coarse_twice_cost = add(*(normalized_p(factor, j, coarse_n) for j in range(1, coarse_n)))
    last = block_p(factor, coarse_n, coarse_n)
    assert add(fine_twice_cost, scale(-1, coarse_twice_cost)) == scale(coarse_n, last)

    # On rank<=17t, substitute p_i=0 for every i>17t.  Then A_N=0,
    # every normalized coarse coordinate Q_J with J>=18 vanishes, and the
    # fine/coarse costs agree exactly.
    cutoff = 17 * factor
    def impose_rank(vector: Vector) -> Vector:
        return clean({key: value for key, value in vector.items() if not (key[0] == "p" and key[1] > cutoff)})

    assert not impose_rank(last)
    for j in range(18, coarse_n + 1):
        assert not impose_rank(normalized_p(factor, j, coarse_n))
    assert not impose_rank(add(fine_twice_cost, scale(-1, coarse_twice_cost)))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_finite_inputs() -> None:
    if hashlib.sha256(PAPER31_FRONTIER.read_bytes()).hexdigest() != PAPER31_SHA256:
        raise AssertionError("Paper 31 d9 verifier hash mismatch")
    d9 = load_module(PAPER31_FRONTIER, "paper31_rank_gap_frontier").d9_package()
    assert d9["full_value"] == 29 and d9["minimum_optimal_rank"] == 6

    raw = FINITE_CERT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == FINITE_CERT_SHA256
    payload = json.loads(raw)
    rank17 = [case for case in payload["cases"] if (case["copies"], case["j"]) == (3, 2)]
    assert len(rank17) == 1
    assert rank17[0]["rank_cap"] == 17 and rank17[0]["expected_value"] == 88
    exact = load_module(HERE / "verify_exact_hive_duals.py", "paper32_exact_hive_duals")
    exact.verify_case(rank17[0])
    print("PASS frozen finite inputs: d9 full=29/rank=6; k=3 rank<=17=88")


def check_theorem_arithmetic(max_t: int) -> None:
    for t in range(1, max_t + 1):
        # Unrestricted lower: coarse-grain F_(3t) by blocks of 3t to 3t F_1.
        lower = 3 * t * 29
        # Direct sum of 3t exact d9 witnesses.
        upper = 3 * t * 29
        upper_rank = 3 * t * 6
        # Rank-face lower: blocks of t give t F_3 with coarse rank<=17.
        rank_face_lower = t * 88
        assert lower == upper == 87 * t
        assert upper_rank == 18 * t and rank_face_lower == 88 * t > lower
    print(f"PASS theorem arithmetic regressions t=1..{max_t}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-t", type=int, default=5)
    args = parser.parse_args()
    if args.max_t < 1:
        raise SystemExit("--max-t must be positive")

    row_count = boundary_count = order_count = 0
    for t in range(1, args.max_t + 1):
        # The unrestricted argument uses coarse dimension 9, block size 3t.
        row_count += check_rows(9, 3 * t)
        boundary_count += check_boundaries(9, 3 * t)
        order_count += check_order(9, 3 * t)
        # The rank-face argument uses coarse dimension 27, block size t.
        row_count += check_rows(27, t)
        boundary_count += check_boundaries(27, t)
        order_count += check_order(27, t)
        check_objective_and_rank(t)
    print(
        f"PASS exact dictionary identities: {row_count} rhombi, "
        f"{boundary_count} boundary rows, {order_count} coarse order rows"
    )
    check_finite_inputs()
    check_theorem_arithmetic(args.max_t)
    print("PASS theorem replay: kappa(F_(3t))=87t and 17t<r_*(F_(3t))<=18t")
    print("NOTE: no claim that r_*(F_(3t))=18t")


if __name__ == "__main__":
    main()
