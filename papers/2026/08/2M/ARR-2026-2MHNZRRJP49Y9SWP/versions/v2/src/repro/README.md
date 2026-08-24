# Exact replays for the arbitrary-characteristic projection floor

The three primary scripts accompany manuscript version 0.7. They use only the
Python standard library. The characteristic-zero fixtures use exact
`fractions.Fraction` arithmetic; the finite-field fixture uses exact modular
Gaussian elimination.

Run from the repository workspace:

```powershell
python src/repro/run_all_replays.py
```

Or run the individual fixtures:

```powershell
python src/repro/verify_exact_projection_floor.py
python src/repro/verify_common_tangent_extremizer.py
python src/repro/verify_perfect_field_fattening.py
```

Write deterministic JSON evidence:

```powershell
python src/repro/verify_exact_projection_floor.py `
  --output src/repro/last_exact_projection_floor_v0.7.json
python src/repro/verify_common_tangent_extremizer.py `
  --output src/repro/last_common_tangent_extremizer_v0.7.json
python src/repro/verify_perfect_field_fattening.py `
  --output src/repro/last_perfect_field_fattening_v0.7.json
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

`verify_perfect_field_fattening.py` enumerates every nonempty support in
`P^1(F_2)`, `P^1(F_3)`, and `P^2(F_2)`. In each stated degree range it builds
the homogeneous value matrix and affine-chart first-neighbourhood matrix. It
checks `alpha(I^(2)) >= alpha(I)+1` and the stronger degreewise implication
used in the proof: equal kernels can occur only when the value kernel is zero.
It also records explicit `F=G^p` fixtures where all formal partials vanish but
the radical ideal contains the lower-degree root `G`.

## Scope

The replays verify finite linear algebra and explicit local identities. They
are not a universal proof, a smoothness certificate, a Lean artifact, peer
review, or a novelty/priority certification.
