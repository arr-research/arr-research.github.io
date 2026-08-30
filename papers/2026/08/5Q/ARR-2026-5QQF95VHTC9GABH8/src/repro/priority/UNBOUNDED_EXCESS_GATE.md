# Paper 32 gate — coarse-grained hives and unbounded optimal-rank excess

**Audit date:** 2026-08-24  
**Decision:** **STANDALONE PAPER GO** for the coarse-graining theorem and its
unbounded-excess application.  The complete all-`k`, all-rank-face curve is
not needed for this headline.  A manuscript/release remains gated on writing
and replaying the coarse-graining proof exactly; nothing is authorized for
publication by this audit.

## Headline now supported

Let

```text
spec(F_k) = (5 repeated 4k times, -4 repeated 5k times),   dim(F_k)=9k.
```

The exact order-27 seed (`k=3`) has

```text
kappa(F_3) = 87,
kappa^(<=17)(F_3) = 88,
r_0(F_3) = 15,
r_*(F_3) = 18.
```

For every integer `t>=1`, coarse-graining gives

```text
kappa(F_(3t)) = 87t,
kappa^(<=17t)(F_(3t)) = 88t,
15t = r_0(F_(3t)),
17t+1 <= r_*(F_(3t)) <= 18t.
```

Consequently

```text
r_*(F_(3t)) - r_0(F_(3t)) >= 2t+1,
```

so the additive gap between inertia and the least rank of a
Hilbert--Schmidt-norm minimizer is unbounded.

This is already a stronger structural theorem than the fixed-dimensional
onset result in Paper 31.  It remains deliberately weaker than the conjectural
formula

```text
kappa^(<=5k+j)(F_k)=30k-j,  0<=j<=k,
```

and must not be advertised as resolving that curve.

## Why the coarse-graining argument is valid

### General amplification principle

Let `F` be a traceless Hermitian target of order `d`.  Let `F^[t]` denote the
order-`dt` target obtained by repeating every eigenvalue of `F` exactly `t`
times; spectrally this is the same target as a direct sum of `t` copies of
`F`.  For every rank cap `r`, the hive reduction yields

```text
kappa_(dt)(F^[t]) = t kappa_d(F),
kappa_(dt)^(<=rt)(F^[t]) = t kappa_d^(<=r)(F).       (A)
```

The upper bounds in (A) are direct sums.  The lower bounds are the genuinely
new direction and follow from coarse-graining any feasible fine hive.

### Coarse hive

Take a feasible hive `H` of order `dt`.  Restrict its vertex array to the
triangular sublattice whose coordinates are multiples of `t`:

```text
Hbar(i,j) = H(ti,tj),   0<=i<=j<=d,
```

up to the harmless coordinate permutation dictated by the chosen hive
convention.  Every elementary rhombus inequality for `Hbar` is a long-rhombus
inequality for `H`.  It is the sum of the fine elementary rhombus inequalities
inside the corresponding `t`-by-`t` parallelogram.  Hence `Hbar` is an
order-`d` hive.  This is a restriction/coarse-graining statement about
*every* feasible fine hive, not merely a construction of a block-diagonal
one.

If the fine positive boundary is

```text
p_1 >= ... >= p_(dt) >= 0,
```

the coarse positive boundary is

```text
q_a = sum_{u=(a-1)t+1}^{at} p_u,   1<=a<=d.          (B)
```

The `q_a` remain nonincreasing and nonnegative.  The opposite isospectral
boundary coarse-grains to the reversed negative of `q`.  Because each target
eigenvalue was repeated `t` times, the target boundary becomes `t` times the
boundary for `F`.  Finally,

```text
(1/2) sum_a q_a = (1/2) sum_u p_u,                    (C)
```

so coarse-graining preserves the fine objective while changing the target to
`tF` in dimension `d`.

If the fine problem has rank at most `rt`, sorted nonnegativity gives
`p_(rt+1)=...=0`; equation (B) then gives `q_(r+1)=...=q_d=0`.  Thus the coarse
point lies on the rank-`r` face.  Positive homogeneity
`kappa^(<=r)(tF)=t kappa^(<=r)(F)` proves the rank-constrained lower bound in
(A).

For the unrestricted lower bound, a coarse `q_d` can be positive even when
the normalized fine spectrum has `p_(dt)=0`.  This causes no gap: subtract
`q_d I` from both coarse PSD summands.  Their difference and common-spectrum
property are unchanged, nonnegativity is preserved, and the cost only
decreases.  The resulting normalized coarse point is feasible for `tF`, so
the original fine cost is still at least `t kappa(F)`.  This normalization
detail should be explicit in the proof if the paper's hive LP omits the last
common eigenvalue.

### Application to the exact seed

Use `(d,r,F)=(27,17,F_3)`.  Since repeating every eigenvalue of `F_3` `t`
times gives `F_(3t)`, equation (A) and the exact seed values give

```text
kappa(F_(3t)) = 87t,
kappa^(<=17t)(F_(3t)) = 88t.
```

The unrestricted upper bound is attained by the direct sum of `t` seed
rank-18 minimizers, hence `r_*<=18t`.  Since every factor of rank at most
`17t` costs at least `88t>87t`, an optimal factor has rank at least `17t+1`.
The target has positive/negative inertia `(12t,15t)`, so `r_0=15t` and the
displayed unbounded excess follows.

## Exact local evidence rechecked

The dependency-free frozen verifier was rerun during this audit.  It reports:

```text
PASS exact hive primal+dual: k=2 j=1 rank=11 value=59
PASS exact hive primal+dual: k=3 j=1 rank=16 value=89
PASS exact hive primal+dual: k=3 j=2 rank=17 value=88
PASS finite exact hive audit; no all-k claim
```

The last `k=3,j=2` line is the seed lower certificate used here.  The separate
endpoint verifier also rechecked the all-`k` unrestricted identity
`kappa(F_k)=29k`, hence `kappa(F_(3t))=87t`, and the explicit rank-`18t`
primal.  The present infinite theorem does not extrapolate a solver dual: it
pulls every putative large feasible point back to the already exact finite
seed.

Current frozen seed artifacts retain the hashes recorded in
`repro/EXACT_HIVE_DUAL_AUDIT.md`:

```text
extractor F65B826AFEF3C943330A22770025D52F281E43BBD8B8C5C2C64989C69231530D
verifier  E353F0F65D7EDC2B3274BA2842263747FE5A5728F65C0E1FF4CF05407FDE09E2
JSON      C6B3588A2415DB067F7FF34F7E23592AC9D85F3E10399DD0F8838FC244352B69
```

## Standalone value and salami-slicing audit

### Why this is a standalone result

Paper 31 answers a threshold question: equality with the inertia rank holds
through dimension seven, while exact separation first occurs in dimension
eight, with an additional two-valued witness in dimension nine.  Paper 32
answers a different global question: whether the additive optimal-rank excess
can remain universally bounded.  The coarse-graining theorem gives a negative
answer and a linear explicit lower bound along an infinite family.

The proof mechanism is also new relative to Paper 31.  Paper 31 uses exact
finite Horn certificates and low-dimensional classification.  Paper 32 uses
a reverse, dimension-reducing map on arbitrary hives to amplify one exact
finite obstruction.  Direct sums alone would only provide upper bounds; the
coarse restriction is what turns the seed into a global lower theorem.

This combination—general amplification principle plus explicit unboundedness
corollary—is enough for a standalone research paper even though it neither
determines `r_*` exactly nor proves the full rank-cost curve.

### Conditions that keep it from becoming salami slicing

- State Paper 31's dimension-eight onset and dimension-nine two-valued witness
  in the introduction, with explicit provenance rather than presenting the
  seed lineage as newly discovered from scratch.
- State that the `k=3`, rank-17 exact certificate is the finite seed for the
  new theorem and preserve its complete replay.
- Make the general coarse-graining identity (A), not another finite table, the
  main theorem.
- Keep all endpoint, seed, and unboundedness claims in one Paper 32.  Do not
  split the general amplification lemma from the `F_(3t)` application.
- Cite or briefly restate only the spectral/Horn reduction needed for
  self-containment; do not reproduce Paper 31's full dimension-eight phase
  diagram.
- Explain explicitly that Paper 32 supersedes the exploratory all-`k`
  conjecture as the publishable headline, while leaving the finer curve open.

With these disclosures, the overlap is a normal theorem dependency rather
than artificial fragmentation.

## Priority audit

### Exact collision

No exact collision was found in the previously inspected ARR/local archive,
public `lluiseriksson` repositories, or the updated bounded web searches for
the phrases “unbounded self-commutator rank,” “minimum optimal rank
self-commutator,” “prescribed self-commutator minimum Hilbert--Schmidt norm
rank,” and “rank excess self-commutator.”  No located source states the
coarse-graining identity (A) for the inverse self-commutator cost, the family
`F_(3t)`, or the lower bound `r_*-r_0>=2t+1`.

This is negative evidence from a bounded search, not proof of novelty.

### Mechanism collision

The ingredients surrounding the new step are classical:

- Knutson--Tao identify Hermitian sum feasibility with honeycombs/hives and
  prove saturation: <https://doi.org/10.1090/S0894-0347-99-00299-4>.
- Knutson--Tao describe honeycomb overlay as the spectral counterpart of
  direct sum: <https://arxiv.org/abs/math/0009048>.
- Knutson--Tao--Woodward classify facets with puzzles and introduce puzzle
  inflation: <https://doi.org/10.1090/S0894-0347-03-00441-7>.
- Horn and Klyachko supply the eigenvalue-sum inequalities underlying the
  reduction: <https://doi.org/10.2140/pjm.1962.12.225> and
  <https://doi.org/10.1007/s000290050037>.

These sources cover feasibility, direct-sum upper constructions, saturation,
and dimension-changing *puzzle construction*.  They do not state the reverse
coarse-grid restriction as an optimization tensorization theorem, do not
track the common PSD support/rank face, and do not derive unbounded minimum
norm-optimal self-commutator rank excess.

The claim should therefore be framed as a new application and exact
optimization consequence of classical hive concavity, not as a new hive
model or a new Horn theorem.

## Mandatory claim limits

The manuscript may claim:

- exact linear tensorization of the unrestricted and `rt`-rank-constrained
  inverse costs under eigenvalue replication;
- the exact values `87t` and `88t` on the two stated faces;
- `17t+1<=r_*<=18t` for `F_(3t)`;
- unbounded **additive** excess, quantitatively at least `2t+1`;
- a uniform ratio lower bound `r_*/r_0 > 17/15` along this subsequence, if
  useful and clearly distinguished from an unbounded ratio.

It must not claim:

- `r_*(F_(3t))=18t`;
- the exact excess is `3t`;
- the complete `30k-j` curve;
- any result for every `k` rather than the subsequence `k=3t`, except the
  already proved unrestricted endpoint;
- that dimension `27t` is minimal for excess `2t+1`;
- that the family maximizes excess in its dimension;
- unbounded **relative** excess or an unbounded rank ratio;
- additivity of minimum optimal rank;
- that puzzle inflation alone proves the lower bound.

## Remaining reproducibility/publication gates

The scientific theorem is **GO**, but a finished submission should still:

1. state the coarse-hive restriction lemma in the manuscript with one fixed
   coordinate convention and exhibit the exact sum of fine rhombi giving
   each coarse rhombus inequality;
2. implement a small dependency-free checker for the boundary block sums,
   rank implication, objective identity, and the `F_3 -> F_(3t)` arithmetic;
3. preserve and run the exact `k=3,rank<=17,value=88` primal/dual seed plus
   the unrestricted endpoint replay;
4. include an independent check of the base Horn/hive orientation and the
   self-commutator spectral reduction;
5. state provenance, AI use, limitations, and the unresolved all-`k` curve;
6. perform ordinary manuscript, bibliography, PDF, and package QA before any
   deposit.

## Final gate

**Scientific gate: PASS / STANDALONE PAPER GO.**  The infinite
coarse-graining theorem and unbounded-excess corollary are sufficient and are
not contingent on solving every intermediate rank face.

**Publication gate: pending implementation and manuscript QA.**  The proof
must be written with the normalization nuance and exact coarse-rhombus
telescoping; the result must remain limited to the stated subsequence and
bounds.
