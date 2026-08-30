# Exact finite hive-dual audit

**Date:** 2026-08-24 (Europe/Stockholm)  
**Decision:** **PASS for the three finite LP statements below; NO-GO for an
all-`k` theorem from these certificates alone.**  Nothing was published and
no Paper 31 file was modified.

## Certified statements

For the hive LP associated with

```text
gamma = (10 repeated 4k times, -8 repeated 5k times)
```

and objective `(1/2) sum_i p_i`, the frozen exact certificates prove:

| copies `k` | face parameter `j` | rank cap `5k+j` | exact optimum |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 11 | 59 |
| 3 | 1 | 16 | 89 |
| 3 | 2 | 17 | 88 |

Thus all three values agree with `30k-j`.  This is a finite theorem only.

## Exact proof object

The primal is stored in the convention

```text
minimize c.x
Aeq.x = b
Aub.x <= 0
p_(rank+1) = ... = p_(9k-1) = 0.
```

For every case, the JSON contains an exact rational primal `x` and exact
rational dual multipliers `(y,z,w)`.  The dependency-free verifier rebuilds
all triangular hive boundary rows, all three elementary-rhombus
orientations, all order rows, the nonnegative terminal row, and the rank
face without importing the extractor.  Using `Fraction`, it checks:

```text
Aeq.x = b,
Aub.x <= 0,
c.x = 30k-j,
z <= 0,
support(w) subset of the coordinates fixed to zero,
c = Aeq^T y + Aub^T z + w,
b^T y = 30k-j.
```

For any feasible `x`, stationarity gives

```text
c.x = b^T y + z^T(Aub.x) >= b^T y,
```

because both `z` and `Aub.x` are componentwise nonpositive and the fixed
coordinate term vanishes.  The exact primal attains the same value, so
strong duality is not being assumed numerically: equality follows directly
from the two rational witnesses.

HiGHS is used only by `extract_exact_hive_duals.py` to propose the vectors.
The extractor refuses to write the JSON until the same identities pass over
`Fraction`.  The second checker uses only the Python standard library and
verifies the frozen JSON without SciPy, NumPy, or an LP solver.

## Support and pattern comparison

| `(k,j)` | equality dual support | rhombus/order support | fixed-face support | largest denominator |
| --- | ---: | ---: | ---: | ---: |
| `(2,1)` | 49 | 136 | 6 | 8 |
| `(3,1)` | 78 | 287 | 10 | 16 |
| `(3,2)` | 76 | 276 | 8 | 4 |

The orientation counts among nonzero rhombus multipliers are respectively

```text
(k,j)=(2,1): orientation 1/2/3 = 45/62/29
(k,j)=(3,1): orientation 1/2/3 = 90/125/72
(k,j)=(3,2): orientation 1/2/3 = 85/117/74.
```

These particular dual vertices are not literal block repetitions or nested
extensions.  Their denominators change from `8` to `16` and back to `4`, the
three orientation supports scale differently, and the gamma-boundary
multipliers are not repeated nine-entry blocks.  This does **not** refute the
existence of a structured all-`k` dual: hive duals have equality-gauge freedom
and the optimal face is degenerate, so HiGHS may select unrelated vertices.
It does mean that raw solver output does not yet expose a defensible symbolic
pattern.

The appropriate next gate is a gauge-fixed or explicitly telescoping family
of multipliers parameterized by `(k,j)`, followed by this same exact
stationarity test for symbolic indices.  Merely adding more rationalized
finite vertices would not close that gate.

## Reproduction

From the workspace root:

```text
python work/paper32-frontier/repro/extract_exact_hive_duals.py
python work/paper32-frontier/repro/verify_exact_hive_duals.py
```

The extractor deterministically regenerated the byte-identical JSON twice in
the audited environment.  The dependency-free verifier reports:

```text
PASS exact hive primal+dual: k=2 j=1 rank=11 value=59 supports=49+136+6
PASS exact hive primal+dual: k=3 j=1 rank=16 value=89 supports=78+287+10
PASS exact hive primal+dual: k=3 j=2 rank=17 value=88 supports=76+276+8
PASS finite exact hive audit; no all-k claim
```

Frozen SHA-256 values:

```text
extractor F65B826AFEF3C943330A22770025D52F281E43BBD8B8C5C2C64989C69231530D
verifier  E353F0F65D7EDC2B3274BA2842263747FE5A5728F65C0E1FF4CF05407FDE09E2
JSON      C6B3588A2415DB067F7FF34F7E23592AC9D85F3E10399DD0F8838FC244352B69
```

## Boundary of the result

This audit proves optimality in the three reconstructed finite hive LPs.  Its
interpretation as the corresponding Horn spectral feasibility problem uses
the classical hive/Horn equivalence and the preceding self-commutator
spectral reduction.  It is not a proof-assistant formalization, an
independent LR-tableau derivation, a priority determination, or a proof of
`kappa^(<=5k+j)=30k-j` for arbitrary `k`.

