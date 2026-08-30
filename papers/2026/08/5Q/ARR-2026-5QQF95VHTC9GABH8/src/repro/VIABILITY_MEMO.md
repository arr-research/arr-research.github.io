# Paper 32 viability memo: amplified two-valued self-commutators

**Date:** 2026-08-24  
**Status:** unbounded additive rank excess proved on the subsequence `F_(3t)`;
the complete all-`k` rank-cost curve remains a conjecture  
**Publication gate:** **MATHEMATICAL GO**, manuscript and final independent
audit still pending  

No Paper 31 file was modified and nothing was published.

## Family and target statement

Let `F_k` be traceless Hermitian of order `9k` with

```text
spec(F_k) = (5 repeated 4k times, -4 repeated 5k times).
```

Write `kappa^(<=r)(F)` for the minimum inverse self-commutator cost on the
rank-`r` face.  The desired theorem is

```text
kappa^(<=5k+j)(F_k) = 30k-j,       0<=j<=k.              (C)
```

It would imply `kappa(F_k)=29k`, minimum norm-optimal rank `6k`, inertia rank
`5k`, and therefore unbounded additive excess `k`.

## Main theorem now proved: unbounded excess by hive coarse-graining

The full conjecture (C) is no longer needed for the headline result.  The
following exact subsequence theorem closes unboundedness.

> **Theorem (coarse-grained amplification).**  For every integer `t>=1`,
> let `F_(3t)` have order `27t` and spectrum
> `(5^(12t),-4^(15t))`.  Then
>
> ```text
> kappa(F_(3t))                    = 87t,
> kappa^(<=15t)(F_(3t))           = 90t,
> kappa^(<=16t)(F_(3t))           = 89t,
> kappa^(<=17t)(F_(3t))           = 88t.
> ```
>
> Consequently its least norm-optimal rank satisfies
>
> ```text
> 17t+1 <= r_*(F_(3t)) <= 18t,
> r_0(F_(3t)) = 15t,
> r_*(F_(3t))-r_0(F_(3t)) >= 2t+1.
> ```
>
> In particular the additive excess is unbounded.

The theorem deliberately does **not** assert `r_*=18t`; the current argument
leaves the ranks `17t+1,...,18t-1` unresolved.

### Coarse-graining lemma

Let `h` be a triangular hive of order `nt`, and define its restriction to the
`t`-sublattice by

```text
H(i,l)=h(ti,tl),       0<=i<=l<=n.
```

Then `H` is an order-`n` hive.  In each of the three lattice orientations, a
coarse rhombus slack is the sum of the `t^2` fine rhombus slacks in the
corresponding parallelogram.  Hence it is nonnegative.  The three coarse
boundary increments are exactly consecutive block sums of the fine boundary
increments.

This is not a numerical approximation or an appeal to matrix block
diagonality.  It is an exact linear map of hive cones.  The formal identities
are replayed by `math/verify_hive_coarse_graining.py`: the current default run
checks all three orientations and all three boundaries for coarse order `27`
and scales `1,...,6` (`6,804` exact integer linear-form identities).

### Application to the frozen `k=3` seed

For a fine feasible point for `F_(3t)`, group the ordered squared singular
values into blocks

```text
P_s = sum_{q=(s-1)t+1}^{st} p_q,       1<=s<=27.
```

The coarse alpha boundary is `P`; the coarse beta boundary is its negative
reverse; and the coarse target boundary is

```text
(10t repeated 12 times, -8t repeated 15 times),
```

which is `t` times the `k=3` target.  If the fine rank is at most
`(15+s)t`, then `P_(15+s+1)=...=P_27=0`, so the coarse point lies on the
literal rank-`15+s` face.  Moreover

```text
(1/2) sum_s P_s = (1/2) sum_q p_q,
```

so the cost is preserved, not merely bounded.

The frozen exact hive certificates at `k=3` give costs `89` and `88` on ranks
`16` and `17`; the endpoint certificates give `90` at rank `15` and `87`
unrestricted.  Homogeneity therefore gives the four lower bounds above.
Direct sums of the exact `d=9` full and face primals attain each value:
choose respectively `0,t,2t,3t` full branches among `3t` branches.  Thus all
four equalities follow.

Finally, cost `87t` is attainable at rank `18t`, while every rank at most
`17t` costs `88t`.  This yields the stated rank interval and the unbounded
excess over inertia `15t`.

## New exact all-k result: the two endpoints

The following part is now a theorem, not numerical evidence:

```text
kappa(F_k) = 29k,
kappa^(<=5k)(F_k) = 30k,            for every k>=1.       (E)
```

### Upper bounds

The exact `d=9` seed has feasible squared-singular-value spectra

```text
(16,12,10,10,8,2,0,0,0), cost 29, rank 6,
(16,14,12,10,8,0,0,0,0), cost 30, rank 5.
```

Direct sums give the two upper bounds in (E).  More generally, `j` full
branches and `k-j` face branches give the exact candidate

```text
16^k, 14^(k-j), 12^k, 10^(k+j), 8^k, 2^j,
```

of rank `5k+j` and cost `30k-j`.  Thus the upper half of (C) is exact for all
`k,j`.

### Dimension-changing Horn membership

For a Horn subset `I={i_1<...<i_r}` let `lambda(I)` be its Grassmannian
partition.  Replacing each selected index `i` by the full block

```text
{(i-1)k+1,...,ik}
```

maps the partition to

```text
D_k(lambda)=(k lambda_1 repeated k, k lambda_2 repeated k, ...).
```

This operation preserves LR positivity.  Indeed, if `H_k` multiplies every
partition part by `k` and `C` denotes conjugation, then

```text
D_k = C o H_k o C o H_k.
```

`H_k` preserves positivity by the LR-semigroup property, and simultaneous
conjugation preserves LR coefficients.  Equivalently, this is the uniform
`(k,k)` puzzle inflation of Knutson--Tao--Woodward.  Hence every block-inflated
base row is a valid order-`9k` Horn row; this step is not an appeal to scalar
stretching alone.

### Exact dual identities

Inflating the five Horn rows of the `d=9` unrestricted certificate gives
right side `29k`.  Their combined coefficient is `1/2` on the first seven
blocks, `-1/2` on block eight, and `-3` on the truncated ninth block.  The
difference from the half-trace objective has nonnegative prefix sums, so it
is exactly a nonnegative combination of the order rows
`p_i-p_(i+1)>=0` and terminal nonnegativity.  This proves the unrestricted
lower bound `29k`.

Inflating the five rank-five rows gives right side `30k`, and its combined
coefficient is exactly `1/2` on the first `5k` coordinates.  On the face
`p_(5k+1)=...=0`, this is the half-trace objective and proves the second lower
bound in (E).

`math/verify_block_inflation_endpoints.py` checks the seven distinct base Horn
triples, the subset/partition dilation identity, both rational coefficient
identities, the order-cone prefix sums, and the primal ranks and costs.  Its
default replay checks `1<=k<=32`; the LR argument proves arbitrary `k`.

## Exact finite intermediate faces

The conjectured lower bounds are exactly certified for all 20 faces with
`1<=k<=5` by `math/verify_finite_hive_duals.py`.  HiGHS only proposes a dual;
the script rationalizes it and then checks the full stationarity and objective
identities over `Fraction`.  The summary digest from the current replay is

```text
3feff8512d65de8a241218c0db08a1fa800a5db8e3456290d19ba895de0514ad.
```

The independent frozen package in `repro/` stores exact rational primal and
dual witnesses for `(k,j)=(2,1),(3,1),(3,2)`.  Its dependency-free checker
passes, with JSON SHA-256

```text
c6b3588a2415db067f7ff34f7e23592ac9d85f3e10399dd0f8838fc244352b69.
```

On the headline face `j=k-1`, exact rationalized certificates pass through
`k=8`.  Floating hive solves continue to give `29k+1` at `k=9,10,12` (values
`262,291,349`), but these three larger cases are evidence only because their
solver-selected dual vertices were not recovered exactly.

Finite exact certificates do not interpolate to an all-`k` proof.

## Falsified simplifications

### Weyl, complementary Weyl, and Ky Fan rows are insufficient

The relaxation containing all Weyl rows, all complementary-Weyl rows, and all
Ky Fan top-sum rows gives only

```text
k=2: 54 instead of 58--60,
k=3: 81 instead of 87--90.
```

Thus standard upper-sum inequalities cannot prove the theorem.

### Uniformly inflated seed support misses intermediate faces

The union of the uniformly inflated `d=9` full and face supports proves the
two endpoints, but at `(k,j)=(2,1)` its best dual value is `58`, not `59`.
The same defect occurs for `k=3` (`87`, not `88`, on `j=2`).  More Horn/hive
structure is genuinely necessary.

### Convex mixing has the right right-hand side but the wrong coefficients

For the critical face `j=k-1`, the mixture

```text
(1-1/k) * full_inflated + (1/k) * face_inflated
```

has right side `29k+1`.  However, it puts coefficient
`1/2+1/(2k)` uniformly on `p_(5k+1),...,p_(6k)`.  On the face `p_(6k)=0`, the
order-row completion has negative prefix weights on the preceding active
coordinates (`-1/4` at `k=2`; `-1/6,-1/3` at `k=3`).  The surplus must be
localized at the zero coordinate, not averaged over the whole sixth block.

### Raw finite hive duals do not reveal a stable formula

The exact solver vertices are dense and gauge-dependent: support sizes and
denominators vary irregularly across `(k,j)`.  This does not refute a simple
telescoping dual, but copying or extrapolating raw supports is not defensible.

## Best remaining route for the stronger complete curve

The missing object can be sharply stated.

> **Seam certificate lemma (open).**  On the face `p_(6k)=0`, construct valid
> order-`9k` Horn/puzzle rows and nonnegative rational multipliers whose
> combined coefficient is the half-trace objective on
> `p_1,...,p_(6k-1)` and whose right side is `29k+1`.

The endpoint mixture shows exactly what the new gadget must do: transport a
total coefficient surplus `1/2` from the first `k-1` positions of the sixth
block onto the final zero coordinate, without producing a negative prefix.
A bounded-width seam puzzle joining `k-1` full tiles to one face tile is the
most concrete route.  Uniform puzzle inflation validates the bulk rows; only
the seam must be new.  A symbolic hive proof would assign nonnegative weights
to the three rhombus orientations and telescope all internal vertices.

Two fallbacks remain:

1. construct the analogous seam for every `j`, yielding the full curve (C);
2. prove only that equality in the inflated `29k` certificate forces
   `p_(6k)>0`.  This weaker equality-rigidity lemma would still prove
   minimum optimal rank `6k` and unbounded excess, though not the quantitative
   `29k+1` gap or the intermediate curve.

Generic facet factorization cannot simply be quoted for fallback 2 because
the target spectra are highly repeated and lie on chamber walls.

## Scientific decision

The coarse-grained subsequence theorem is qualitatively stronger than Paper
31: it converts a fixed excess-one seed into an explicit family with
unbounded additive excess.  It is therefore sufficient as the mathematical
center of Paper 32 even without solving the complete curve (C).

**Mathematical GO; no publication yet.**  A manuscript may safely claim the
four displayed values on `F_(3t)`, the rank interval
`17t+1<=r_*<=18t`, and additive excess at least `2t+1`.  It must not claim
`r_*=18t`, exact excess `3t`, the full `30k-j` curve, dimension minimality for
a prescribed excess, or unbounded relative excess.  The seam/rigidity program
now becomes an optional strengthening rather than a publication gate.
