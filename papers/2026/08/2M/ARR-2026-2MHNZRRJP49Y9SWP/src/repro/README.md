# Exact replays for the universal projection floor

The two primary scripts accompany manuscript version 0.6. They use only the
Python standard library and exact `fractions.Fraction` Gaussian elimination.

Run from the repository workspace:

```powershell
python work/quadric_tangent_absorption/repro/verify_exact_projection_floor.py
python work/quadric_tangent_absorption/repro/verify_common_tangent_extremizer.py
```

Write deterministic JSON evidence:

```powershell
python work/quadric_tangent_absorption/repro/verify_exact_projection_floor.py `
  --output work/quadric_tangent_absorption/repro/last_exact_projection_floor_v0.6.json
python work/quadric_tangent_absorption/repro/verify_common_tangent_extremizer.py `
  --output work/quadric_tangent_absorption/repro/last_common_tangent_extremizer_v0.6.json
```

## What is checked

`verify_exact_projection_floor.py` builds the simplex lattice

```text
A_(d,m) = {alpha in N^d : |alpha| <= m}
```

and the degree-at-most-`m` monomial evaluation matrix. It verifies exact rank
`binom(d+m,d)` for a grid of dimensions and degrees. It also removes one node
and checks that the value rank drops by one while adjoining the first-jet rows
increases it again. This is a finite falsification-boundary witness for the
fattening step.

`verify_common_tangent_extremizer.py` uses the local model

```text
F(t,y) = f(t) + y,
f(t) = product_p l_p(t)^2.
```

At each simplex-lattice support, `f` and its tangential gradient vanish while
the normal derivative of `F` is one. Hence on `X=(F=0)`, the normal coordinate
`y=-f` lies in the square of the local maximal ideal. Exact value and
first-jet matrices then have the same rank `binom(d+m,d)`, strictly below the
number of ambient degree-`m` columns.

The local fixture does not claim global smoothness of its particular
homogenization. Global existence of a smooth member is the separate Bertini
argument in the manuscript.

## Historical scripts

The earlier quadric and line scripts remain preserved for audit history:

- `verify_quadric_tangent_absorption.py`
- `verify_linear_p1_sharpness.py`

They test the weaker v0.1--v0.4 route and are no longer the primary evidence
for the exact v0.6 theorem.

## Scope

The replays verify finite linear algebra and explicit local identities. They
are not a universal proof, a smoothness certificate, a Lean artifact, peer
review, or a novelty/priority certification.
