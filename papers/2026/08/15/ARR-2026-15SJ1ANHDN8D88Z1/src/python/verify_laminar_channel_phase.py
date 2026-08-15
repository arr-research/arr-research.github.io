#!/usr/bin/env python3
"""Fail-closed exact replay for the laminar-channel architecture theorem."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations


def leaves(h: int) -> tuple[str, ...]:
    return tuple(format(i, f"0{h}b") for i in range(2**h))


def prefixes(h: int) -> tuple[str, ...]:
    return tuple(
        format(i, f"0{d}b") if d else ""
        for d in range(h)
        for i in range(2**d)
    )


def answer(u: str, v: str) -> int:
    return int(u.startswith(v + "1"))


def cells_for_queries(h: int, queries: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    buckets: dict[tuple[int, ...], list[str]] = {}
    for u in leaves(h):
        signature = tuple(answer(u, v) for v in queries)
        buckets.setdefault(signature, []).append(u)
    return tuple(tuple(bucket) for bucket in buckets.values())


def parallel_covered(h: int, ell: int, queries: tuple[str, ...]) -> int:
    return sum(min(ell, len(cell)) for cell in cells_for_queries(h, queries))


def exact_parallel_max(h: int, ell: int, q: int) -> int:
    xs = prefixes(h)
    if q >= len(xs):
        return 2**h
    return max(parallel_covered(h, ell, qs) for qs in combinations(xs, q))


def exact_adaptive_max(h: int, ell: int, q: int) -> int:
    xs = prefixes(h)

    @lru_cache(maxsize=None)
    def value(candidates: tuple[str, ...], rounds: int) -> int:
        if rounds == 0 or len(candidates) <= ell:
            return min(ell, len(candidates))
        best = min(ell, len(candidates))
        for v in xs:
            zero = tuple(u for u in candidates if not answer(u, v))
            one = tuple(u for u in candidates if answer(u, v))
            best = max(best, value(zero, rounds - 1) + value(one, rounds - 1))
        return best

    return value(leaves(h), q)


def check_laminarity(h: int) -> None:
    sets = [{u for u in leaves(h) if answer(u, v)} for v in prefixes(h)]
    for a, b in combinations(sets, 2):
        assert not (a & b) or a <= b or b <= a


def check_exact_phase() -> int:
    cases = 0
    for h in range(1, 5):
        check_laminarity(h)
        m = 2**h
        for s in range(h + 1):
            ell = 2**s
            for q in range(min(len(prefixes(h)), 5) + 1):
                par = exact_parallel_max(h, ell, q)
                ada = exact_adaptive_max(h, ell, q)
                assert par == min(m, ell * (q + 1)), (h, s, q, par)
                assert ada == min(m, ell * (2**q)), (h, s, q, ada)
                cases += 1
    return cases


def check_partition_matroid_fixture() -> None:
    h, ell = 3, 2
    queries = ("", "0")
    cells = cells_for_queries(h, queries)
    sizes = sorted(map(len, cells))
    assert sizes == [2, 2, 4]
    assert parallel_covered(h, ell, queries) == 6

    # Arbitrary-prior cellwise optimum: sum the ell largest weights per cell.
    weights = {u: i + 1 for i, u in enumerate(leaves(h))}
    direct = sum(
        sum(sorted((weights[u] for u in cell), reverse=True)[:ell])
        for cell in cells
    )
    assert direct == 25


def main() -> None:
    cases = check_exact_phase()
    check_partition_matroid_fixture()
    print("PASS: laminar channel theorem")
    print(f"exact phase cases: {cases}")
    print("arbitrary-prior partition fixture: PASS")
    print("no floating-point or SDP assumptions used")


if __name__ == "__main__":
    main()
