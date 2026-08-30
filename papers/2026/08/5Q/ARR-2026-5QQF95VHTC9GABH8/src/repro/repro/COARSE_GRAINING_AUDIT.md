# Hive coarse-graining audit and unbounded-rank corollary

**Date:** 2026-08-24 (Europe/Stockholm)  
**Decision:** **PASS for an all-`t` unboundedness theorem on the subsequence
`F_(3t)`; no claim that the optimal rank is exactly `18t`.**  Nothing was
published and no Paper 31 file was modified.

## Statement closed by the audit

Let

```text
spec(F_k) = (5 repeated 4k times, -4 repeated 5k times),  dim(F_k)=9k.
```

Using the same normalization of the inverse self-commutator cost as Papers
31--32, for every integer `t>=1` the audited argument proves

```text
kappa(F_(3t)) = 87t,
17t < r_*(F_(3t)) <= 18t.
```

Since the inertia lower bound is `r_0(F_(3t))=15t`, this gives

```text
r_*(F_(3t)) - r_0(F_(3t)) > 2t,
```

and hence unbounded additive rank excess.  The result does **not** identify
the exact value of `r_*` between `17t+1` and `18t`, does not prove the full
curve `30k-j`, and makes no statement for indices not divisible by three.

## Exact coarse-graining identity

For a fine hive `h(i,l)` and positive block size `t`, set

```text
H(I,L) = h(tI,tL).
```

With the three elementary rhombus functionals in the convention used by the
LP, exact cancellation gives

```text
R1_H(I,L)
 = sum R1_h(i,l),
   i=t(I-1)+1,...,tI,  l=tL,...,tL+t-1;

R2_H(I,L)
 = sum R2_h(a+q,tL+q),
   a=t(I-1)+1,...,tI,  q=0,...,t-1;

R3_H(I,L)
 = sum R3_h(t(I-1)+a,t(L-1)+a+q),
   a=1,...,t,  q=0,...,t-1.
```

Every coefficient is `+1` in these sums.  Thus fine rhombus nonnegativity
implies coarse rhombus nonnegativity.  The checker represents every row as a
dictionary from an exact node label to an integer coefficient and compares
the two sides after all internal nodes cancel.  It uses neither floating
point nor a computer-algebra library.

The Python loops implement these identities for any supplied positive block
size.  The default replay checks all rhombi for the two theorem routes and
`t=1,...,5`.  Those finite executions are regression tests of the formula;
the all-`t` proof is the displayed telescoping identity itself, whose ranges
partition the appropriate rectangle or diagonal strip.

## Boundary blocks and necessary normalization

Let `A_J` be the sum of the fine alpha entries in block `J`, and let `G_J`
be the corresponding gamma-block sum.  Direct telescoping gives coarse
boundaries

```text
alpha = (A_1,...,A_N),
beta  = (-A_N,...,-A_1),
gamma = (G_1,...,G_N).
```

Although the fine normalized spectrum has final entry `p_n=0`, its last
block sum `A_N` need not vanish.  Treating it as zero would make the
unrestricted argument invalid.  The correct normalization is

```text
Q_J = A_J - A_N,
H'(I,L) = H(I,L) + A_N(I-L).
```

The added function is affine, so every rhombus functional is unchanged.
The transformed boundaries are `(Q,-reverse(Q),G)`, with `Q_N=0`.  Equal
block sizes and the fine ordering imply `Q_1>=...>=Q_N=0`.  More explicitly,
the checker verifies each `Q_J-Q_(J+1)` as a positive telescoping sum of fine
order rows `p_r-p_(r+1)`.

The exact objective identity is

```text
sum(fine p_i) - sum_(J=1)^(N-1) Q_J = N A_N >= 0.
```

Consequently the normalized coarse cost never exceeds the fine cost.

All alpha, beta and gamma boundary identities, the affine normalization, the
order identities, and the objective identity are independently compared as
exact dictionaries by the replay.

## Rank-face corollary

Use coarse dimension `N=27` and block size `t`.  If the fine singular-square
spectrum has rank at most `17t`, then all fine coordinates after `17t`
vanish.  Therefore

```text
A_27 = 0,
Q_18 = ... = Q_27 = 0,
rank(Q) <= 17,
coarse cost = fine cost.
```

The checker performs this substitution symbolically in its dictionaries.
Since the frozen exact `k=3`, rank-at-most-17 hive optimum is `88`,
homogeneity gives

```text
cost(fine rank<=17t) >= 88t.
```

## Proof of the theorem

Two applications of the identity suffice.

1. **Unrestricted lower bound.** Coarse-grain a hive for `F_(3t)` to
   dimension nine with block size `3t`.  Its normalized target is `3t F_1`
   and its cost is no larger than the fine cost.  The canonical exact Paper
   31 certificate gives `kappa(F_1)=29`; homogeneity therefore yields the
   lower bound `87t`.
2. **Matching upper bound and rank.** The direct sum of `3t` exact
   dimension-nine minimizers has cost `3t*29=87t` and rank `3t*6=18t`.
   Hence `kappa(F_(3t))=87t` and `r_*<=18t`.
3. **Excluding rank `<=17t`.** The rank-face corollary gives cost at least
   `88t`, strictly above the optimum `87t`.  Hence `r_*>17t`.

This proof uses direct sums only for the upper construction.  The lower
bounds apply to globally mixed hives and do not assume block diagonality.

## Frozen finite inputs

The replay fail-closes on and re-executes the byte-identical vendored copy of
the canonical standard-library Paper 31 dimension-nine verifier.  It is now a
Paper 32-local input and the replay has no sibling-worktree dependency:

```text
work/paper32-frontier/math/verify_rank_gap_frontier.py
SHA-256 00BDBBFD8ADBF3AFF8F847AE3574241FC7BED887573C8FA6142BB242CF874BE7
```

It checks `full_value=29` and `minimum_optimal_rank=6`.  It also loads the
Paper 32 exact hive JSON, checks its frozen hash, selects `(k,j)=(3,2)`, and
runs the dependency-free exact primal/dual verifier on the rank-17 value 88:

```text
work/paper32-frontier/repro/exact_hive_duals.json
SHA-256 C6B3588A2415DB067F7FF34F7E23592AC9D85F3E10399DD0F8838FC244352B69
```

## Reproduction

From the workspace root:

```text
python work/paper32-frontier/repro/verify_coarse_graining_theorem.py
```

Audited coarse-graining checker SHA-256:

```text
B1EA0D5DAD40B56D217CBBE32054110A63267EC7BE0E862AF964B17CF0CDA91F
```

Expected final markers:

```text
PASS exact dictionary identities
PASS frozen finite inputs: d9 full=29/rank=6; k=3 rank<=17=88
PASS theorem replay: kappa(F_(3t))=87t and 17t<r_*(F_(3t))<=18t
NOTE: no claim that r_*(F_(3t))=18t
```

## Independent endpoint inflation replay

`math/verify_block_inflation_endpoints.py` checks a complementary exact
all-`k` endpoint route.  For every base Horn triple in the two sparse endpoint
duals, it verifies recursive Horn membership in dimension nine and the exact
partition identity

```text
partition(inflate(I,k)) = D_k(partition(I)),
D_k(lambda) = ((k lambda)' scaled by k)',
```

equivalently `D_k = conjugate o H_k o conjugate o H_k`, where `H_k`
multiplies every part by `k`.  LR positivity is preserved by `H_k` through
the LR semigroup property and by simultaneous conjugation.  Thus every
block-inflated triple used by the endpoint dual is Horn for arbitrary `k`.

The remaining dual algebra is checked over `Fraction`: the unrestricted
combination has RHS `29k`, and its difference from the half-sum objective is
a nonnegative combination of order rows because every prefix sum is
nonnegative.  On the rank-`5k` face the combined coefficients are exactly
`1/2` on all active coordinates and the RHS is `30k`.  The direct-sum primal
lists have the displayed ranks and costs `6k,29k` and `5k,30k`.

This proves the two endpoint costs for all `k`, but does not inspect the
intermediate faces and therefore does not prove `r_*=6k`.  The executable
regression checks `1<=k<=32` by default.  The frozen supports and exact row
construction are inlined, so this route uses only the Python standard library
and invokes no numerical solver.

```text
work/paper32-frontier/math/verify_block_inflation_endpoints.py
SHA-256 F7C66A937E100E293EE68794606036AFC09E6EB4E603E1A275BFB9F8D3978D80
```

## Remaining limitations

- The dictionary checker is a transparent exact replay, not a proof-assistant
  formalization.
- The spectral interpretation remains conditional on the classical
  Knutson--Tao hive/Horn equivalence and the self-commutator reduction already
  stated and audited in Paper 31.
- The dimension-nine verifier is vendored locally and frozen by hash; the
  coarse-graining replay can run without the Paper 31 sibling directory.
- This audit does not adjudicate novelty, priority, exposition, or peer
  review, and performs no publication action.
