"""Exact supplementary verification for Eriksson's RLE relaxation manuscript.

Run: python verify.py
Requires Python 3.10+ and SymPy 1.14.0. No network or floating-point tests.
The analytical proof is in paper.tex / paper.pdf.
"""
from __future__ import annotations

import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import sympy as S

ROOT = Path(__file__).resolve().parent
R = S.Rational
u, z = S.symbols("u z")
checks = []


def check(condition, name):
    if not condition:
        raise AssertionError(name)
    checks.append(name)
    print("PASS:", name, flush=True)


def block(rows):
    return S.BlockMatrix(rows).as_explicit()


def family_gram(parameter):
    a = R(4, 3) * (1 - parameter) ** 2
    b = (1 - 2 * parameter) ** 2
    c = (1 - parameter) * (4 * parameter - 1) / 3
    d = S.Matrix([[a, b], [b, a]])
    f = S.Matrix([[b, a], [a, b]])
    o = c * S.ones(2)
    p12 = block([[d, o, o], [o, d, o], [o, o, d]])
    p23 = block([[o, d, o], [o, o, d], [d, o, o]])
    p31 = block([[o, o, f], [f, o, o], [o, f, o]])
    j = S.ones(6) / 6
    q = S.eye(6) - j
    zero = S.zeros(6)
    return block([[q, zero, zero, zero],
                  [zero, q, p12 - j, (p31 - j).T],
                  [zero, (p12 - j).T, q, p23 - j],
                  [zero, p31 - j, (p23 - j).T, q]])


def unitary_bases(x, t):
    w = (-1 + S.I * S.sqrt(3)) / 2
    f = S.Matrix([[1, 1], [1, -1]])
    zz = S.diag(1, -1)
    xx = S.diag(S.conjugate(x), x)
    h = S.Matrix([[1, w * t * t], [1, -w * t * t]])
    m1 = S.diag(xx, S.I * S.conjugate(w) * t * zz * xx.conjugate() ** 2, xx)
    m1 *= block([[f, f, f], [f, w * f, S.conjugate(w) * f],
                 [h, S.conjugate(w) * h, w * h]]) / S.sqrt(6)
    m2 = block([[f, f, f], [h, w * h, S.conjugate(w) * h],
                [h, S.conjugate(w) * h, w * h]]) / S.sqrt(6)
    m3 = S.diag(xx.conjugate(), S.conjugate(w) * xx.conjugate(),
                -S.I * t * zz * xx ** 2)
    m3 *= block([[f, f, f], [h, w * h, S.conjugate(w) * h],
                 [f, S.conjugate(w) * f, w * f]]) / S.sqrt(6)
    return [S.eye(6)] + [v.applyfunc(S.expand) for v in (m1, m2, m3)]


def gram_from_bases(bases):
    result = S.zeros(24)
    for a in range(4):
        for b in range(a, 4):
            overlap = (bases[a].conjugate().T * bases[b]).applyfunc(S.expand)
            if a == b:
                check(overlap == S.eye(6), f"exact unitarity of basis {a}")
            values = overlap.applyfunc(lambda v: S.expand(v * S.conjugate(v)) - R(1, 6))
            result[a * 6:(a + 1) * 6, b * 6:(b + 1) * 6] = values
            result[b * 6:(b + 1) * 6, a * 6:(a + 1) * 6] = values.T
    return result


def distance(gram):
    defect = sum(sum(v * v for v in gram[a * 6:(a + 1) * 6, b * 6:(b + 1) * 6])
                 for a in range(4) for b in range(a + 1, 4))
    return S.factor(1 - defect / 30)


G = family_gram(u)
s = (1 + 4 * u - 8 * u ** 2) / 3
k = 8 * u ** 2 - 10 * u + 3
expected = (z ** 4 * (z - 1) ** 5 * (z - (1 - 2 * s)) ** 3
            * (z - (1 + s)) ** 6 * (z - (1 + 2 * k)) ** 2
            * (z - (1 - k)) ** 4)
actual = G.charpoly(z).as_expr()
check(S.factor(actual - expected) == 0, "generic characteristic polynomial over Q[u]")
check(G == G.T, "generic Gram symmetry")
check(S.simplify(S.trace(G)) == 20, "generic traceless frame trace")

opt = R(7, 10)
x = (S.sqrt(30) + S.I * S.sqrt(70)) / 10
q = -2 * S.sqrt(70) / 35
t = S.expand((1 - S.I * S.sqrt(3)) * (q + S.I * S.sqrt(1 - q * q)) / 2)
direct = gram_from_bases(unitary_bases(x, t))
check(direct == G.subs(u, opt), "direct algebraic bases match polynomial Gram at optimum")
eigenvalues = direct.eigenvals()
check(eigenvalues == {S.Integer(0): 4, S.Integer(1): 5,
                     R(21, 25): 2, R(24, 25): 6, R(27, 25): 7},
      "exact Gram eigenvalues and multiplicities at optimum")
check(1 - max(eigenvalues) / 4 == R(73, 100), "exact relaxation rate 73/100")
check(direct.rank() == 20, "rank 20 implies traceless channel nullity 15")

# These identities are used in the three-interval analytical lower bound.
check(s.subs(u, R(3, 5)) == R(13, 75), "first-interval endpoint")
check(S.expand(S.diff(s, u) - R(4, 3) * (1 - 4 * u)) == 0, "monotonicity on first interval")
check(S.expand(-k - R(2, 25) + 8 * (u - R(11, 20)) * (u - opt)) == 0,
      "middle-interval factorization")
check(S.expand(-2 * s - R(2, 25) - R(16, 3) * (u - opt) * (u + R(1, 5))) == 0,
      "last-interval factorization")

dbar = distance(G)
expected_distance = -(448 * u ** 4 - 1024 * u ** 3 + 888 * u ** 2 - 352 * u + 25) / 30
check(S.expand(dbar - expected_distance) == 0, "distance polynomial from overlap blocks")
check(S.diff(dbar, u).subs(u, opt) == -R(12, 625), "nonzero distance derivative at gap optimum")
alternative = R(139, 200)
ss, kk = s.subs(u, alternative), k.subs(u, alternative)
alternative_gap = 1 - (1 + max(0, -2 * ss, ss, 2 * kk, -kk)) / 4
check(alternative_gap == R(14571, 20000), "exact comparison relaxation rate")
check(dbar.subs(u, alternative) - dbar.subs(u, opt) == R(38513, 750000000),
      "strict rational distance improvement")
check(R(73, 100) - alternative_gap == R(29, 20000), "strict rational relaxation decrease")

report = {"status": "PASS", "generated_utc": datetime.now(timezone.utc).isoformat(),
          "python_version": platform.python_version(), "sympy_version": S.__version__,
          "scope": "Specified one-parameter RLE family; equal probabilities; total event rate one",
          "checks": checks, "optimum_parameter": "7/10", "optimum_gap": "73/100",
          "generic_characteristic_polynomial": str(S.factor(actual)),
          "exact_gram_characteristic_polynomial": str(S.factor(direct.charpoly(z).as_expr())),
          "exact_gap_comparison": {"u=7/10": "73/100", "u=139/200": "14571/20000"},
          "files_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                           for name in ("verify.py", "paper.tex")}}
(ROOT / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
(ROOT / "exact-gram.json").write_text(json.dumps([[str(v) for v in row] for row in direct.tolist()], indent=2) + "\n")
print(f"Completed {len(checks)} exact checks. Report: verification.json")
