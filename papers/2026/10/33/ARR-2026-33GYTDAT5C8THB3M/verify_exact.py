"""Replay the five-query certificate using Python's standard library only.

Run: python verify_exact.py
Inputs are the two adjacent phase-certificate-*.json matrices.
No numerical solver, floating point PSD test, or external package is used.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
N = 32


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read_matrix(name):
    a = [[F(x) for x in row] for row in json.loads((HERE / name).read_text())]
    check(len(a) == N and all(len(row) == N for row in a), "matrix shape")
    return a


def psd(a):
    """Exact symmetric Schur elimination, including singular matrices."""
    a = [row[:] for row in a]
    n = len(a)
    check(all(a[i][j] == a[j][i] for i in range(n) for j in range(n)),
          "matrix is not symmetric")
    pivots = []
    for k in range(n):
        pivot = a[k][k]
        check(pivot >= 0, f"negative Schur pivot at {k}")
        pivots.append(pivot)
        if pivot == 0:
            check(all(a[k][j] == 0 for j in range(k + 1, n)),
                  f"zero pivot with nonzero remaining row at {k}")
            continue
        for i in range(k + 1, n):
            for j in range(i, n):
                a[i][j] -= a[i][k] * a[k][j] / pivot
                a[j][i] = a[i][j]
    return {"rank": sum(x > 0 for x in pivots),
            "exact_pivots": [str(x) for x in pivots]}


def causal(q):
    q = [row[:] for row in q]
    for k in range(5, 0, -1):
        check(len(q) == 2**k, "causal size")
        check(all(q[i][j] == 0 for i in range(len(q)) for j in range(len(q))
                  if (i & 1) != (j & 1)), f"last-symbol orthogonality level {k}")
        m = len(q) // 2
        q = [[q[2*i][2*j] + q[2*i+1][2*j+1]
              for j in range(m)] for i in range(m)]
    check(q == [[F(1)]], "causal normalization")


def null_condition(r):
    for i in range(N):
        for w in range(6):
            check(sum(r[i][j] for j in range(N) if j.bit_count() == w) == 0,
                  f"null condition row {i}, weight {w}")


def evaluate(coef, x):
    return sum(c * x**k for k, c in enumerate(coef))


def must_fail(fn, label):
    try:
        fn()
    except ValueError:
        return label
    raise ValueError(f"negative control incorrectly accepted: {label}")


def main():
    q = read_matrix("phase-certificate-Q.json")
    r = read_matrix("phase-certificate-R.json")
    causal(q)
    null_condition(r)
    ranks = {
        "Q": psd(q),
        "R": psd(r),
        "Q-R": psd([[q[i][j] - r[i][j] for j in range(N)] for i in range(N)])
    }
    check([ranks[x]["rank"] for x in ("Q", "R", "Q-R")] == [32, 26, 32],
          "unexpected rank")
    coef = [sum(r[i][j] for i in range(N) for j in range(N)
                if (i ^ j).bit_count() == h) for h in range(6)]
    expected = list(map(F, ("1086981/1250000", "3225799/50000000",
                           "-3784393/6250000", "-585391/25000000",
                           "-103157/390625", "-2055017/50000000")))
    check(coef == expected, "rejection polynomial")
    parallel = [F(1, 10), F(0), F(3, 5), F(0), F(3, 10), F(0)]
    gap = [parallel[k] + coef[k] - (1 if k == 0 else 0) for k in range(6)]
    cubic = list(map(F, (-1520760, 3225799, -1795904, 2055017)))
    factored = [F(0)] * 6
    for k, c in enumerate(cubic):
        factored[k] += c / 50000000
        factored[k+2] -= c / 50000000
    check(gap == factored, "gap factorization")
    derivative_discriminant = (2*cubic[2])**2 - 4*(3*cubic[3])*cubic[1]
    check(derivative_discriminant == -66647776694132 and cubic[3] > 0,
          "strict monotonicity of cubic")
    bracket = (F(53314, 100000), F(53315, 100000))
    check(evaluate(cubic, bracket[0]) < 0 < evaluate(cubic, bracket[1]),
          "root bracket")
    eta = F(7, 10)
    bpar, bcert = evaluate(parallel, eta), 1 - evaluate(coef, eta)
    check(bpar == F(46603, 100000), "parallel value")
    check(bcert == F(2301478964279, 5000000000000), "certificate value")
    check(bpar-bcert == F(28671035721, 5000000000000), "strict gap")

    # Meaningful negative controls: detect broken normalization, broken null,
    # negative eigenvalue, and a forbidden nonzero row at a zero pivot.
    badq = [row[:] for row in q]
    badq[0][0] += 1
    badr = [row[:] for row in r]
    badr[0][0] += 1
    controls = [
        must_fail(lambda: causal(badq), "altered causal normalization"),
        must_fail(lambda: null_condition(badr), "altered null condition"),
        must_fail(lambda: psd([[F(-1)]]), "negative PSD pivot"),
        must_fail(lambda: psd([[F(0), F(1)], [F(1), F(0)]]),
                  "zero pivot with nonzero row")
    ]
    report = {
        "status": "all exact checks passed",
        "arithmetic": "Python standard-library Fraction; no solver",
        "input_sha256": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                         for name in ("phase-certificate-Q.json",
                                      "phase-certificate-R.json")},
        "causal_constraints": "exact at all five levels; Q0=1",
        "null_annihilation": "R V=0 exactly for all six types",
        "psd": ranks,
        "rejection_coefficients": list(map(str, coef)),
        "gap_factorization": "(1-eta^2) g(eta) / 50000000",
        "cubic_coefficients_ascending": list(map(str, cubic)),
        "derivative_discriminant": str(derivative_discriminant),
        "root_bracket": list(map(str, bracket)),
        "eta": str(eta),
        "parallel_failure": str(bpar),
        "certificate_failure": str(bcert),
        "strict_improvement": str(bpar-bcert),
        "negative_controls_rejected": controls
    }
    (HERE/"verification-exact.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(report["status"])
    print("PSD ranks:", {k: v["rank"] for k, v in ranks.items()})
    print("Exact advantage at eta=7/10:", bpar-bcert)


if __name__ == "__main__":
    main()
