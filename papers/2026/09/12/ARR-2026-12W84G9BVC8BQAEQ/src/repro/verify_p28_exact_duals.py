#!/usr/bin/env python3
"""Standard-library verification of the exact p=28 hive duals.

The discovery path used HiGHS and python-flint to reconstruct rational simplex
bases.  This replay uses neither dependency: it regenerates every integer hive
row, checks the sparse rational stationarity identities and dual signs, and
combines them with the independently verified p=28 LR upper certificate.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
FULL = HERE / "basis_dual_l1_p28.json"
RANK60 = HERE / "basis_dual_l1_p28_rank60.json"
LR_AUDIT = HERE / "lr_frontier_bundle_audit.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def q(value) -> Q:
    return Q(str(value))


def canonical_hash(payload: dict) -> str:
    body = dict(payload)
    expected = body.pop("certificate_sha256")
    stream = json.dumps(body, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(stream.encode()).hexdigest()
    require(actual == expected, "certificate canonical hash mismatch")
    return actual


class HiveRows:
    def __init__(self, p: int, q_mult: int) -> None:
        self.p = p
        self.q = q_mult
        self.n = p + q_mult
        self.nodes = [(i, level) for level in range(self.n + 1) for i in range(level + 1)]
        self.node_index = {node: index for index, node in enumerate(self.nodes)}
        self.p_offset = len(self.nodes)
        self.variable_count = self.p_offset + self.n - 1
        self.gamma = [q_mult] * p + [-p] * q_mult
        self.equalities: dict[tuple, tuple[dict[int, int], int]] = {}
        self.inequalities: dict[tuple, dict[int, int]] = {}
        self.build()

    def t(self, i: int, level: int) -> int:
        return self.node_index[(i, level)]

    def pv(self, one_based: int) -> int:
        require(1 <= one_based < self.n, "invalid spectrum index")
        return self.p_offset + one_based - 1

    @staticmethod
    def row(terms: list[tuple[int, int]], negate: bool = False) -> dict[int, int]:
        sign = -1 if negate else 1
        out: dict[int, int] = {}
        for index, coefficient in terms:
            out[index] = out.get(index, 0) + sign * coefficient
        return {index: value for index, value in out.items() if value}

    def eq(self, name: tuple, terms: list[tuple[int, int]], rhs: int = 0) -> None:
        require(name not in self.equalities, f"duplicate equality {name}")
        self.equalities[name] = (self.row(terms), rhs)

    def ge(self, name: tuple, terms: list[tuple[int, int]]) -> None:
        # Store the same A_ub*x <= 0 sign convention as the discovery LP.
        require(name not in self.inequalities, f"duplicate inequality {name}")
        self.inequalities[name] = self.row(terms, negate=True)

    def build(self) -> None:
        n = self.n
        self.eq(("origin",), [(self.t(0, 0), 1)])
        for j in range(1, n + 1):
            terms = [(self.t(0, j), 1), (self.t(0, j - 1), -1)]
            if j < n:
                terms.append((self.pv(j), -1))
            self.eq(("alpha", j), terms)
        for j in range(1, n + 1):
            terms = [(self.t(j, n), 1), (self.t(j - 1, n), -1)]
            if j >= 2:
                terms.append((self.pv(n - j + 1), 1))
            self.eq(("beta", j), terms)
        for j in range(1, n + 1):
            self.eq(
                ("gamma", j),
                [(self.t(j, j), 1), (self.t(j - 1, j - 1), -1)],
                self.gamma[j - 1],
            )
        for level in range(1, n):
            for i in range(1, level + 1):
                self.ge(("rhombus", 1, level, i), [
                    (self.t(i, level + 1), 1), (self.t(i - 1, level), 1),
                    (self.t(i - 1, level + 1), -1), (self.t(i, level), -1),
                ])
                self.ge(("rhombus", 2, level, i), [
                    (self.t(i, level + 1), 1), (self.t(i, level), 1),
                    (self.t(i + 1, level + 1), -1), (self.t(i - 1, level), -1),
                ])
                self.ge(("rhombus", 3, level, i), [
                    (self.t(i, level), 1), (self.t(i - 1, level), 1),
                    (self.t(i, level + 1), -1), (self.t(i - 1, level - 1), -1),
                ])
        for j in range(1, n - 1):
            self.ge(("order", j), [(self.pv(j), 1), (self.pv(j + 1), -1)])
        self.ge(("nonnegative",), [(self.pv(n - 1), 1)])


def add_scaled(target: list[Q], row: dict[int, int], multiplier: Q) -> None:
    for index, coefficient in row.items():
        target[index] += multiplier * coefficient


def verify_dual(path: Path, rows: HiveRows, expected_rank_cap: int | None,
                expected_kappa: int) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("status") == "PASS", f"{path.name}: status is not PASS")
    require(payload["p"] == rows.p and payload["q"] == rows.q, f"{path.name}: wrong parameters")
    require(payload["rank_cap"] == expected_rank_cap, f"{path.name}: wrong rank cap")
    require(q(payload["paper_kappa_for_2F"]) == expected_kappa, f"{path.name}: wrong kappa")
    certificate_hash = canonical_hash(payload)
    stationarity = [Q(0)] * rows.variable_count
    dual_value = Q(0)
    equality_seen = set()
    for raw_name, raw_value in payload["equality_dual"]:
        name = tuple(raw_name)
        require(name in rows.equalities, f"unknown equality {name}")
        require(name not in equality_seen, f"duplicate equality multiplier {name}")
        equality_seen.add(name)
        value = q(raw_value)
        row, rhs = rows.equalities[name]
        add_scaled(stationarity, row, value)
        dual_value += value * rhs
    inequality_seen = set()
    for raw_name, raw_value in payload["inequality_dual"]:
        name = tuple(raw_name)
        require(name in rows.inequalities, f"unknown inequality {name}")
        require(name not in inequality_seen, f"duplicate inequality multiplier {name}")
        inequality_seen.add(name)
        value = q(raw_value)
        require(value < 0, f"inequality multiplier is not strictly negative: {name}")
        add_scaled(stationarity, rows.inequalities[name], value)
    fixed_seen = set()
    for raw_index, raw_value in payload["fixed_bound_dual"]:
        index = int(raw_index)
        require(index not in fixed_seen, f"duplicate fixed-bound multiplier {index}")
        fixed_seen.add(index)
        require(expected_rank_cap is not None, "unrestricted certificate has fixed-bound multiplier")
        first_fixed = rows.pv(expected_rank_cap + 1)
        require(first_fixed <= index < rows.variable_count, f"invalid fixed-bound variable {index}")
        stationarity[index] += q(raw_value)
    objective = [Q(0)] * rows.variable_count
    for j in range(1, rows.n):
        objective[rows.pv(j)] = Q(1, 2)
    require(stationarity == objective, f"{path.name}: stationarity failure")
    require(dual_value == Q(expected_kappa, 2), f"{path.name}: dual objective failure")
    spectrum = [q(value) for value in payload["positive_spectrum"]]
    require(len(spectrum) == rows.n, f"{path.name}: wrong spectrum length")
    require(spectrum == sorted(spectrum, reverse=True), f"{path.name}: unordered spectrum")
    require(sum(spectrum) == expected_kappa, f"{path.name}: spectrum trace mismatch")
    if expected_rank_cap is not None:
        require(all(value == 0 for value in spectrum[expected_rank_cap:]), "rank-face spectrum tail is nonzero")
    return {
        "file": path.name,
        "certificate_sha256": certificate_hash,
        "dual_support": len(equality_seen) + len(inequality_seen) + len(fixed_seen),
        "dual_lower_bound": expected_kappa,
        "rank_cap": expected_rank_cap,
    }


def main() -> None:
    if not __debug__:
        raise SystemExit("refusing optimized Python: exact replay requires __debug__")
    rows = HiveRows(28, 57)
    full = verify_dual(FULL, rows, None, 2546)
    rank60 = verify_dual(RANK60, rows, 60, 2547)
    lr = json.loads(LR_AUDIT.read_text(encoding="utf-8"))
    require(lr.get("status") == "PASS", "LR audit is not PASS")
    p28 = next(record for record in lr["records"] if record["p"] == 28)
    require(p28["kappa_upper"] == 2546 and p28["attaining_rank"] == 61,
            "LR p=28 upper certificate mismatch")
    report = {
        "status": "PASS",
        "scope": "standard-library exact p=28 primal-dual and rank replay",
        "hive_dimension": rows.n,
        "hive_variables": rows.variable_count,
        "equalities_available": len(rows.equalities),
        "inequalities_available": len(rows.inequalities),
        "unrestricted_dual": full,
        "rank60_dual": rank60,
        "lr_upper": {
            "kappa": p28["kappa_upper"],
            "attaining_rank": p28["attaining_rank"],
        },
        "theorem": "kappa(F_(28,57)) = 2546 and the minimum attaining rank is 61",
        "logic": (
            "LR gives value <=2546 at rank 61; the unrestricted dual gives value >=2546; "
            "the rank<=60 dual gives value >=2547, and smaller rank faces are nested."
        ),
    }
    destination = HERE / "p28_exact_dual_audit.json"
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS kappa(F_(28,57))=2546 minimum_attaining_rank=61")
    print(f"WROTE {destination.resolve()}")


if __name__ == "__main__":
    main()
