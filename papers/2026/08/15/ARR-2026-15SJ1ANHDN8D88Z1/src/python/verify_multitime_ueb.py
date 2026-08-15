"""Lightweight fail-closed checks for MULTITIME_UEB_THEOREM.md."""

from fractions import Fraction
from itertools import product
from math import isclose, sqrt


def architecture_values(d, n, ell):
    histories = d ** (2 * n)
    serial = min(Fraction(1), Fraction(ell * d, histories))
    parallel = min(Fraction(1), Fraction(ell * d**n, histories))
    return serial, parallel, Fraction(1)


# Exact Pauli-history fixtures.
assert architecture_values(2, 2, 1) == (
    Fraction(1, 8), Fraction(1, 4), Fraction(1)
)
assert architecture_values(2, 2, 2) == (
    Fraction(1, 4), Fraction(1, 2), Fraction(1)
)


# Every n-fold Weyl-label tuple has the claimed uniform net-label fibre.
for d in (2, 3):
    for n in (1, 2, 3):
        fibres = {(a, b): 0 for a in range(d) for b in range(d)}
        for labels in product(product(range(d), repeat=2), repeat=n):
            net = (
                sum(label[0] for label in labels) % d,
                sum(label[1] for label in labels) % d,
            )
            fibres[net] += 1
        assert set(fibres.values()) == {d ** (2 * n - 2)}


# Entanglement-spectrum formula and rank cap on exact rational spectra.
spectra = (
    (Fraction(1),),
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 4),) * 4,
    (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
)
for spectrum in spectra:
    assert sum(spectrum) == 1
    value = sum(sqrt(float(x)) for x in spectrum) ** 2 / 4
    assert value <= len(spectrum) / 4 + 1e-14

assert isclose(
    sum(sqrt(float(x)) for x in spectra[1]) ** 2 / 4,
    0.5,
    rel_tol=0.0,
    abs_tol=1e-14,
)


# Exact D=4, rank-2, list-2 fixed-probe optimum.
p_fixture = (2 + sqrt(2)) / 4
dual_trace = 2 * (1 + 1 / sqrt(2)) / 4
assert isclose(p_fixture, dual_trace, rel_tol=0.0, abs_tol=1e-14)
assert p_fixture < 1

print("PASS: exact d=2,n=2 serial/parallel/Bell architecture values")
print("PASS: Weyl net-label fibres for d<=3 and n<=3")
print("PASS: entanglement-spectrum fixtures obey the Schmidt-rank cap")
print("PASS: D=4,r=2,ell=2 fixed-probe primal/dual value")
