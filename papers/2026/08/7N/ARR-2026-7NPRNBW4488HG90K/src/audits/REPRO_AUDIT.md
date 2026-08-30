# Paper 28 reproducibility audit

Date: 24 August 2026

`REPRO_AUDIT_STATUS: COMPLETE`

## Verdict

**PASS for the current manuscript and reproducibility layer.**  Both inherited
replays execute successfully, and the new independent exact checker passes.
The preliminary viability memo contained a false middle inequality in the
four-kick lower bound.  It was caught by this audit; the current manuscript
now uses the valid shear/Gram-determinant replacement below and explicitly
records why the discarded shortcut fails.

## Replays run

```text
python work/one-spike-selfcommutator-rigidity/verify_one_spike.py --max-n 20
python work/paper27-one-spike-four-kick/verify_four_kick_bridge.py
python work/paper28-one-spike-four-kick/repro/run_replay.py
```

Observed results:

```text
PASS: exact cost, Horn tails, and singular spectrum through n=20
PASS: both sharp trace-distance constants are attained
PASS: four-level multi-spike nonextension counterexample

PASS: 2 exact generic balanced-quadrilateral flux identities
PASS: perimeter lower-chain diagnostics
PASS: exact weighted-shift square constructors through n=6

PASS: 160 exact balanced-quadrilateral and flux identities
PASS: corrected shear/Gram-determinant lower certificate
PASS: exact noncommuting counterexample to the preliminary middle step
PASS: 15 one-spike/reflected/zero-padded constructors

PASS: exact one-spike matrices, singular spectra, stability, triangles, and squares
PASS: corrected Gram certificate and exact counterexample to the discarded step
PASS: both frozen replay SHA-256 values
```

Both independent outputs were regenerated and matched their frozen hashes.

| Artifact | SHA-256 |
|---|---|
| inherited `verification.json` | `1025eecb1be56ed27694b2d5e653e48608b595887e877055bd58487a634b17e2` |
| inherited `four_kick_bridge.json` | `84dcfc2ed7853f2772526f6841919eeebdfd22e0972a8526c39c51767a2baa9a` |
| combined fail-closed runner | `ae32aa52a89d0040830f85cecb67530ace674ce96b416f2b7195b2067432578c` |
| independent checker | `467a71f058b9640d1c6ab65c7c5081b330513672086c7e167c563ecada59cf53` |
| independent `four_kick_gram.json` | `7095534026866159b37de40e2055b30ca9e765401a38f3fca4809bac2bf3d9cd` |
| symbolic checker | `be9be92b0d3b1cb7067618a5cadd0da726966a2d14b2a97a7936a8a3f615185e` |
| symbolic `symbolic_constructors.json` | `b455b13c193dfbe101bf53632da046ff08575d507b7c104286470f9af0c35b5a` |

## P0: invalid preliminary lower-bound step

The viability memo asserted

```text
(||D1+D2|| + ||D1-D2||)^2
    >= 4(||D1||^2+||D2||^2)
    >= 8||D1||||D2||.
```

The first displayed inequality is false.  Set

```text
D1 = diag(1,-1),
D2 = [[1,1/10],[1/10,-1]].
```

These Hermitian matrices do not commute.  With

```text
a=||D1||^2=2, b=||D2||^2=101/50, c=<D1,D2>=2,
A=||D1+D2||^2, B=||D1-D2||^2,
```

the claimed comparison would require `sqrt(A B) >= a+b`, whereas exact
rational arithmetic gives

```text
A B = 401/2500 < 40401/2500 = (a+b)^2.
```

The exploratory SymPy checker tested the false inequality on only two
fixtures that happened to satisfy it.  Passing those fixtures does not cover
the universal claim.

## Correct lower-bound certificate

Let

```text
a=||D1||^2, b=||D2||^2, c=<D1,D2>,
q=sqrt(ab-c^2).
```

For a nonzero target, `a>0`.  Replace `D2` by its orthogonal shear

```text
D2_perp = D2 - (c/a)D1.
```

The commutator is unchanged and therefore, using
`F=-(i/2)[D1,D2]`,

```text
kappa_d(F) <= (1/2) sqrt(ab-c^2) = q/2.               (1)
```

Balance and two triangle inequalities still give

```text
S_2 >= sqrt(A)+sqrt(B),
A=a+b+2c, B=a+b-2c.
```

Now

```text
A B = (a-b)^2 + 4q^2,
a+b >= 2q,
sqrt(A B) >= 2q.
```

Consequently

```text
S_2^2
  >= A+B+2sqrt(A B)
   = 2(a+b)+2sqrt(A B)
  >= 8q
  >= 16 kappa_d(F).                                   (2)
```

This repair also explains the equality constructor: an optimal pair can be
sheared to Hilbert--Schmidt orthogonality and reciprocally scaled to equal
norms.  Then `a=b=2 kappa_d(F)`, `c=0`, and the centrally symmetric square
attains equality throughout.

## Coverage comparison

| Claim / edge case | Inherited replay | Independent replay |
|---|---:|---:|
| exact one-spike tail identity | yes, sampled compositions through `n=20` | yes, distinct construction through `n=12` plus repeated data |
| exact weighted-shift square | yes, SymPy through `n=6` | scalar certificate through `n=12` plus repeated spectra |
| generic flux identity | two fixed fixtures | 80 general and 80 central deterministic rational fixtures in dimensions 2 and 3 |
| lower-bound metric step | tests the invalid step on two favorable fixtures | disproves old step and checks corrected Gram certificate |
| orthogonal shear preserves commutator | not checked | exact on every fixture |
| `n=1` | bridge only | explicit |
| repeated negative eigenvalues | not explicit in bridge | explicit |
| sign-reflected cone | not explicit | explicit scalar invariance |
| zero padding | not explicit | explicit scalar invariance |
| deterministic output | not stated | regenerated twice; identical SHA-256 |

## Remaining limits

- Finite replay does not prove the arbitrary-dimensional Horn lower bound or
  optimizer rigidity; those remain deductive manuscript claims.
- The sign-reflection and zero-padding checks are scalar invariance checks,
  not independent symbolic matrix constructions.
- The checker certifies the repaired algebra and many exact fixtures; it does
  not numerically solve the global optimization defining `kappa_d`.
- Dependency-free exact arithmetic avoids floating-point tolerance.  The
  included runner regenerates the JSON and fails closed on frozen-hash drift.

The false proof step has been replaced in the current manuscript.  The
four-kick reproducibility layer is strong enough for manuscript production;
the fail-closed runner invokes both the rational and symbolic implementations.
This audit does not assess priority and does not authorize publication.
