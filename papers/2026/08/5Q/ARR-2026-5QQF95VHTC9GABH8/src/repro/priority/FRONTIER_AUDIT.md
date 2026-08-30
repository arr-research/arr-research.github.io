# Paper 32 frontier audit — unbounded norm-optimal rank excess

**Audit date:** 24 August 2026 (Europe/Stockholm)  
**Scope:** read-only comparison of 28 saved local repositories, the 34
currently visible public `lluiseriksson` repositories, the local 18-record ARR
mirror, Papers 28--31, the current amplification assets, and bounded searches
of primary/authoritative literature. Nothing was published and Paper 31 was
not modified.

## Executive decision

**CURRENT GATE: RESEARCH GO / MANUSCRIPT NO-GO.** The exact direct-sum
constructions and a genuinely different hive LP give unusually strong
evidence, but the required all-`k` lower bound is not proved.

**IF THE SYMBOLIC ALL-`k` THEOREM CLOSES: STANDALONE PAPER GO.** The family

```text
F_k:  spec(F_k) = (5 repeated 4k times, -4 repeated 5k times),  d=9k
```

would then give an unbounded additive separation between the elementary
inertia lower bound and the least rank on the Hilbert--Schmidt norm-optimal
self-commutator face. That is a qualitative theorem, not another isolated
Horn example. It directly answers the open question left at the end of Paper
31 and is scientifically sufficient for one focused paper, provided that the
global lower bound is exact and the Paper 31 base case is disclosed rather
than repackaged.

The preferred result is the complete rank--cost curve, not merely the claim
that direct sums exist.

## Exact proposed theorem

For a traceless Hermitian target `F`, write

```text
kappa_d^(<=r)(F)
  = (1/2) min { ||C||_HS^2 : CC* - C*C = 2F, rank(C)<=r },
```

with value `+infinity` if the rank face is infeasible. The clean Paper 32
target is:

> **Proposed all-`k` theorem.** For every integer `k>=1` and every
> `0<=j<=k`,
>
> ```text
> kappa_(9k)^(<=5k+j)(F_k) = 30k-j.
> ```

It would follow that

```text
kappa_(9k)(F_k) = 29k,
r_0(F_k) = 5k,
r_*(F_k) = 6k,
r_*(F_k)-r_0(F_k) = k.
```

Thus the additive excess is unbounded. Within this family the relative rank
ratio remains `r_*/r_0=6/5`; the theorem would **not** show unbounded relative
excess.

The minimal headline theorem needed for a paper is slightly weaker than the
full curve but still requires three exact statements for every `k`:

1. unrestricted cost at least `29k`;
2. every rank-at-most-`6k-1` factor costs at least `29k+1`;
3. an explicit rank-`6k` factor has cost `29k`.

Those statements already prove `r_*=6k` and unbounded excess. The complete
`5k+j` curve is strongly preferred because it exposes one unit of cost saved
per added singular direction and makes the mechanism substantially more than
an endpoint separation.

## What is already exact

Paper 31 contains the `k=1` two-valued target and two exact feasible squared
singular-value spectra:

```text
p_full = (16,12,10,10,8,2,0,0),  rank 6, cost 29;
p_face = (16,14,12,10,8,0,0,0),  rank 5, cost 30.
```

For each `0<=j<=k`, a direct sum of `j` full branches and `k-j` face branches
is an exact construction. After sorting, its positive squared singular values
are

```text
16^k, 14^(k-j), 12^k, 10^(k+j), 8^k, 2^j,
```

where exponents denote multiplicities. It has

```text
rank = 5k+j,
cost = 30k-j.
```

These are rigorous upper bounds for every `k,j`. They do not imply matching
lower bounds because a globally mixed realization in dimension `9k` need not
respect the nine-dimensional block decomposition. Additivity of the inverse
minimum or of its rank-constrained faces cannot be assumed.

## Fresh falsification replay

The independent hive implementation was rerun during this audit:

```text
python work/paper31-frontier/math/excess2/hive_amplification_scan.py \
  --copies 1 2 3 4 5
```

It reproduced the Paper 31 `k=1` values and returned the following entire
curve through five copies:

| `k` | dimension | unrestricted | rank `<=5k` | `<=5k+1` | `<=5k+2` | `<=5k+3` | `<=5k+4` | `<=6k` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9  | 29  | 30  | 29  | -- | -- | -- | 29  |
| 2 | 18 | 58  | 60  | 59  | 58 | -- | -- | 58  |
| 3 | 27 | 87  | 90  | 89  | 88 | 87 | -- | 87  |
| 4 | 36 | 116 | 120 | 119 | 118 | 117 | 116 | 116 |
| 5 | 45 | 145 | 150 | 149 | 148 | 147 | 146 | 145 |

Every returned optimizer had the direct-sum multiplicity pattern to displayed
precision. The LP uses triangular Knutson--Tao hives rather than the recursive
Horn enumerator used in Papers 29--31. This makes it a valuable independent
discovery/falsification route, but it is still floating-point evidence and
cannot be a proof object.

## Proof gate

### Mandatory exact route

The main proof must supply an all-`k` rational lower certificate. Plausible
forms are:

- an explicit family of hive dual weights whose rhombus and boundary
  coefficients telescope to
  `cost>=30k-j` on the face `rank<=5k+j`;
- named Horn triples in dimension `9k` with exact nonnegative multipliers;
- a representation-theoretic or polyhedral product theorem that proves the
  required global face inequality without assuming block diagonality.

For any proposed inflated Horn triple, membership in the relevant
Littlewood--Richardson/Horn set must itself be proved. Replacing each base
index by a block of `k` indices is not automatically a valid LR inflation
argument.

### Independent verification route

At least one route independent of the main symbolic derivation should:

1. generate the relevant LR coefficient by direct tableaux or an exact hive
   construction;
2. verify every primal residual and every dual coefficient identity over
   integers/rationals;
3. recover `k=1,...,5` as frozen regression cases;
4. test reflected spectra and boundary rank faces;
5. fail closed if a named Horn row or a coefficient does not match.

An exact dual extracted from the same hive system is not fully independent of
a hive proof. The best package is a symbolic hive/telescoping proof plus a
separately written LR-tableau or recursive-Horn checker.

### Abort conditions

Paper 32 remains **NO-GO** if the strongest result is any of the following:

- numerical agreement for more finite values of `k`;
- direct-sum upper bounds without global lower bounds;
- an exact proof only for `k=2` or another fixed copy number;
- a rationalized dual whose pattern is not proved for arbitrary `k`;
- an all-`k` unrestricted cost formula without proving the minimum optimal
  rank;
- a second isolated spectrum with excess two.

Those outcomes are useful research notes or regression fixtures, not a paper
stronger than the integrated Paper 31.

## External priority screen

### Exact collision

No inspected primary or authoritative source states the displayed family, the
formula `30k-j`, the conclusion `r_*(F_k)=6k`, or unbounded additive excess of
minimum norm-optimal self-commutator rank over inertia. Exact-spectrum and
phrase searches for “minimum optimal rank,” “rank above inertia,” “prescribed
self-commutator,” and the `5^4/-4^5` target returned no mathematical match.

No exact collision was found in the 34 public `lluiseriksson` repositories or
the 18-record ARR mirror. Authenticated GitHub code searches for the family,
`30k-j`, “unbounded rank excess,” and the hive script name returned no public
file. Locally, the idea appears only in the Paper 31 exploratory shortlist,
mathematical shortlist, hive scan, and direct-sum audit. This is negative
evidence from a bounded search, not proof of novelty or nonpublication.

### Strong mechanism collision

The feasibility and lower-bound language is built on the classical additive
Hermitian eigenvalue problem:

- A. Horn, “Eigenvalues of sums of Hermitian matrices,” *Pacific J. Math.*
  **12** (1962), 225--241,
  <https://doi.org/10.2140/pjm.1962.12.225>.
- A. A. Klyachko, “Stable bundles, representation theory and Hermitian
  operators,” *Selecta Math.* **4** (1998), 419--445,
  <https://doi.org/10.1007/s000290050037>.
- A. Knutson and T. Tao, “The honeycomb model of `GL_n(C)` tensor products I:
  Proof of the saturation conjecture,” *J. Amer. Math. Soc.* **12** (1999),
  1055--1090, <https://doi.org/10.1090/S0894-0347-99-00299-4>, preprint
  <https://arxiv.org/abs/math/9807160>.
- A. Knutson, T. Tao and C. Woodward, “The honeycomb model ... II: Puzzles
  determine facets of the Littlewood--Richardson cone,” *J. Amer. Math. Soc.*
  **17** (2004), 19--48, <https://arxiv.org/abs/math/0107011>.
- W. Fulton, “Eigenvalues, invariant factors, highest weights, and Schubert
  calculus,” *Bull. Amer. Math. Soc.* **37** (2000), 209--249,
  <https://doi.org/10.1090/S0273-0979-00-00865-X>.

These sources make the Horn cone, hive model, saturation machinery and
piecewise-linear feasibility classical. They do not state the inverse
self-commutator objective, the rank-constrained curve, or its unbounded
excess. Any hive “inflation lemma” in Paper 32 must be distinguished from the
classical saturation theorem: the present operation changes dimension and
rank faces, not merely a scalar multiple of one fixed LR triple.

### Adjacent self-commutator and norm literature

- P. Fan and C.-K. Fong, “Which operators are the self-commutators of compact
  operators?”, *Proc. AMS* **80** (1980), 58--60,
  <https://doi.org/10.1090/S0002-9939-1980-0574508-X>, concerns existence.
- N. Filonov and Y. Safarov, “On the relation between an operator and its
  self-commutator,” *J. Functional Analysis* **260** (2011), 2902--2932,
  <https://doi.org/10.1016/j.jfa.2011.02.011>, concerns operator approximation
  and almost-normality.
- A. Böttcher and D. Wenzel, “The Frobenius norm and the commutator,” *Linear
  Algebra Appl.* **429** (2008), 1864--1885,
  <https://doi.org/10.1016/j.laa.2008.05.020>, is a forward norm inequality.
- T. Zhang, “On a conjecture of lambda-Aluthge transforms and
  Hilbert--Schmidt self-commutators,”
  <https://arxiv.org/abs/2603.04655>, is also a forward-norm problem.

None is an exact antecedent for minimizing factor norm and then rank at a
prescribed finite Hermitian target.

## Self-prior-art and salami audit

### Exact relationship to Paper 31

Paper 31 already proves the `k=1` statement:

```text
spec(F_1)=(5,5,5,5,-4,-4,-4,-4,-4),
kappa_9(F_1)=29,
kappa_9^(<=5)(F_1)=30,
r_*(F_1)=6.
```

It also ends by asking how large `r_*(F)-r_0(F)` can become. Paper 32 would
answer that question by proving an all-`k` theorem. Accordingly:

- the `k=1` target is a cited base case, not new content;
- Paper 32 must not re-present Paper 31's `d<=7` threshold or dimension-eight
  cone as new;
- shared Horn reduction and inertia lemmas should be cited or summarized
  briefly;
- the new unit is the global mixing lower bound for every copy number and the
  consequent unboundedness theorem.

### Is a separate paper defensible?

**Yes, if the all-`k` theorem is proved.** The onset theorem (“failure begins
at dimension eight”) and the growth theorem (“the additive excess is
unbounded”) answer different structural questions and require different
certificates. An exact all-`k` rank--cost curve is a material extension, not a
minor parameter variation.

The salami risk is nevertheless **medium** because the family starts from
Paper 31's dimension-nine witness and reuses the same inverse-Horn framework.
To keep the risk controlled:

1. cite Paper 31 in the abstract and introduction;
2. state explicitly that its `k=1` theorem is the seed;
3. put the all-`k` inequality/inflation lemma first among the contributions;
4. omit a repeated exposition of the low-dimensional threshold proof;
5. include a comparison table: Paper 31 = sharp onset, Paper 32 = unbounded
   growth and complete copy-number curve;
6. do not split the endpoint unboundedness and the intermediate-face curve
   into two further papers.

If the all-`k` proof closes **before** Paper 31 receives a public/immutable
record, a merged capstone would have the lowest editorial risk and greatest
single-paper strength. A separate Paper 32 remains scientifically defensible
only if the development chronology is explicit and the unboundedness theorem
is the unmistakable center. A finite-`k` result should instead be folded into
Paper 31's reproducibility material, not deposited separately.

## Comparison with the other live frontiers

| Rank if theorem closes | Frontier | Scientific ceiling | Operational value | Exact-collision risk | Self/salami risk | Current distance to theorem | Decision |
|---:|---|---:|---:|---:|---:|---:|---|
| **1** | **All-`k` self-commutator excess `r_*-r_0=k`**, preferably full `30k-j` curve | **9.3/10** | **6.4/10** | Low in bounded search | Medium | One symbolic global lower-bound family plus independent checker | **Best near-term Paper 32; research GO** |
| **2** | Uniform all-prime Weyl rank--support law or exact structural failure | **9.5/10** | **8.3/10** | Low exact, strong adjacent uncertainty literature | Medium/high across Papers 23--25 | Major analytic theorem still missing | **Highest ceiling, farther from closure** |
| **3** | Heavy-tail-valid structured spectral-edge exclusion | **8.8/10** | **9.6/10** | High/dense robust-covariance field | High against two ARR papers | New computable confidence set, post-selection level and nonvacuous power | **Best operational frontier, high collision** |
| **4** | End-to-end Lean SU(2) Makeenko--Migdal crossing theorem | **8.4/10** formal value | **8.7/10** | Classical theorem externally | High against component formalizations | Concrete crossing theorem without target-equivalent package hypotheses | **Formalization GO, ordinary novelty lower** |

The all-prime Weyl theorem has a slightly higher abstract ceiling, but the
self-commutator amplification is the strongest **near-term** frontier: it has
exact primals for every parameter, an independently implemented LP matching
the full conjectured curve through `k=5`, a clear falsification target, and a
single missing symbolic family of lower certificates. It is also much less
self-colliding than the heavy-tail spectral route and more mathematically new
than a formalization of a classical loop equation.

## Safe and prohibited claims

### Safe after proof

> We determine the exact rank-constrained inverse self-commutator cost for the
> two-valued family `spec(F_k)=(5^(4k),-4^(5k))`. The optimum at rank
> `5k+j` is `30k-j`; hence minimum-norm factors first occur at rank `6k`, while
> inertia forces only `5k`. Consequently the additive optimal-rank excess is
> unbounded.

A conservative priority sentence is:

> We are not aware of a previous prescribed-target self-commutator family with
> unbounded additive separation between minimum norm-optimal rank and the
> inertia lower bound. The claim is this exact family and curve, not a general
> additivity theorem or an extremal classification.

### Prohibit

- “direct sums prove the optimum”;
- “self-commutator cost is additive” in general;
- “rank excess grows linearly for every target family”;
- “dimension `9k` is minimal for excess `k`”;
- “this is the maximal excess possible in dimension `9k`”;
- “relative rank excess is unbounded”;
- “all two-valued targets behave this way”;
- “the first” or absolute novelty language;
- presenting Knutson--Tao saturation or the Horn cone as new;
- treating numerical hives as exact certificates.

## Recommended Paper 32 shape after proof

One focused paper is enough:

1. concise reduction and Paper 31 base case;
2. exact direct-sum primal family;
3. new all-`k` global lower-bound/inflation theorem;
4. complete rank--cost curve and unbounded-excess corollary;
5. exact independent LR/Horn replay;
6. limitations: no dimension-minimality for excess `k`, no global
   extremality, no general additivity.

Do not add unrelated repository results merely to increase length. The
unboundedness theorem, if exact, is already a sufficient standalone research
unit.

## Frozen local assets

```text
work/paper31-frontier/math/excess2/hive_amplification_scan.py
3b8d30edb13cababce5360daf10677b1e1df9d0ec6b0fc58259ff4d0b2271b29

work/paper31-frontier/math/excess2/DIRECT_SUM_AMPLIFICATION_AUDIT.md
d9598a1afd0f9c68b269a3a4b9c8648ee24596e40590070f322881310724662f

work/paper31-frontier/paper.tex
43f1dfbd30520e23e8fa6668f7de23d1339531244977bf190fa494754e7691e3
```

## Final verdict

**The family is sufficiently strong for a unique Paper 32 if, and only if, an
exact all-`k` global lower bound is proved.** The complete `30k-j` curve would
be the best version; exact unboundedness via the `6k-1` face is the minimum
publishable theorem. Until then, the status is **RESEARCH GO / MANUSCRIPT
NO-GO**. More finite scans, direct sums, or isolated excess-two examples do
not cross the paper threshold.
