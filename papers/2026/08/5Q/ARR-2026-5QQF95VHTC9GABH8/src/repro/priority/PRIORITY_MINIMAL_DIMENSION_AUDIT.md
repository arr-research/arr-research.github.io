# Priority audit: the sharp dimension-eight onset of super-inertial norm-optimal rank

**Audit date:** 24 August 2026 (Europe/Stockholm)  
**Scope:** external primary literature, the 34 currently visible public
`lluiseriksson` GitHub repositories, the local 18-record ARR mirror, and the
local Paper 28--31 chain.  
**Scientific claim audited:** for every traceless Hermitian target
`F in M_d(C)` with `d<=7`, the minimum of

```text
(1/2)||C||_HS^2  subject to  CC* - C*C = 2F
```

is attained by a factor of rank `max(n_+(F),n_-(F))`; Paper 30 supplies an
exact strict separation at `d=8`. Thus eight is the least ambient dimension
in which **Hilbert--Schmidt norm optimality can force factor rank strictly
above the inertia lower bound**.

## Gate

**PRIORITY GATE: CONDITIONAL GO.** No exact external antecedent for either the
universal `d<=7` theorem or the resulting sharp dimension-eight onset was
located in this bounded audit. The searched classical and recent primary
sources cover self-commutator existence, additive Hermitian eigenvalue
feasibility, or forward commutator-norm inequalities; they do not state the
inverse prescribed-target norm/rank theorem.

This is a negative search result, not proof of absolute novelty. The safe
priority formulation is therefore “we are not aware of a previous result,”
not “the first.”

The gate is conditional for an editorial reason rather than a mathematical
priority defect: **if Paper 30 has not yet been immutably deposited, Paper 31
should absorb and supersede it.** The dimension-eight family is the positive
half of the threshold theorem, while the new `d<=7` theorem is the negative
half. Publishing the two halves consecutively as separate papers would create
substantial salami-slicing risk. The strongest and cleanest research object is
one paper proving the sharp onset.

## Exact scope of the candidate theorem

Let

```text
r_0(F) = max(n_+(F),n_-(F)).
```

The local exact certificate supports the following statement, including
singular spectra and the zero target:

> For every traceless Hermitian `F` in dimension `d<=7`, there exists a
> Hilbert--Schmidt norm-minimizing factor `C` satisfying
> `CC* - C*C = 2F` and `rank(C)=r_0(F)`.

Paper 30 proves that, for the dimension-eight family

```text
spec(F_t) = (4-3t,t,t,t,-1,-1,-1,-1),  0<t<1,
```

the inertia is `(4,4)` but every norm-minimizing factor has rank at least
five; an explicit rank-five minimizer exists. Consequently:

> Dimension eight is the least dimension in which the inertia lower bound
> can fail to be attained on the Hilbert--Schmidt norm-optimal
> self-commutator face.

This wording is narrower and more accurate than “minimum self-commutator rank
first fails in dimension eight.” The latter could be read as an unqualified
algebraic representation-rank claim, whereas the new phenomenon is a
**rank-versus-norm-optimality separation**.

## Theorem-by-theorem priority map

| Layer | Priority finding | Status in Paper 31 | Safe wording |
|---|---|---|---|
| Balanced self-commutator reduction `CC*-C*C=2F` | Already developed in the author's preceding inverse-commutator work; classical algebraic background is older | Foundation, not new | “Using the preceding balanced reduction...” |
| Inertia obstruction `rank(C)>=r_0(F)` | Elementary and already in Papers 28--30 | Lemma for completeness, not a contribution | “The elementary inertia bound gives...” |
| Replacement by positive semidefinite isospectral summands | A Horn-type spectral reformulation built from classical additive-eigenvalue theory | Mechanism, not new as a general Horn theorem | “The inverse problem reduces to a classical Horn feasibility problem with a linear cost.” |
| Equality of unrestricted and inertia-face projected epigraphs for every `d<=7` inertia stratum | **No exact external or public self-authored antecedent found** | Central candidate theorem | “We prove exact epigraph equality in every inertia stratum through dimension seven.” |
| Existence of an inertia-rank norm minimizer for all traceless Hermitian `F`, including singular spectra, in `d<=7` | **No exact antecedent found** | Central qualitative theorem | “Every target through dimension seven has a norm minimizer at the inertia lower-bound rank.” |
| The dimension-eight strict-gap family | Exact self-prior art from Paper 30; Paper 29 is one interior point | Imported positive half of the threshold | Cite/absorb explicitly; do not present as independently new within Paper 31 |
| Sharp threshold `d=8` | **No exact antecedent found**; new synthesis of the `d<=7` theorem and Paper 30 family | Headline candidate theorem | “Dimension eight is the sharp onset of norm-optimal rank strictly above inertia.” |
| Exact projected-polyhedral/Farkas replay | A new certificate package for this theorem, not a new general polyhedral algorithm | Reproducibility contribution | “Exact rational certificates verify all strata.” |

## Exact-collision screen

No inspected external record states any of the following:

- universal attainment of the inertia lower-bound rank for every traceless
  Hermitian target through dimension seven;
- a change of that universal property specifically between dimensions seven
  and eight;
- the phrase-equivalent claim that dimension eight is the least dimension in
  which minimum Hilbert--Schmidt self-commutator cost forces rank above
  inertia;
- equality of the unrestricted and inertia-face Horn epigraph projections in
  all low-dimensional inertia strata.

Searches included combinations of “minimum rank,” “minimum norm,” “prescribed
self-commutator,” “Hilbert--Schmidt self-commutator,” “nuclear norm,” “Horn,”
“inertia,” and the literal expression `CC* - C*C`. The closest recent hit was
Teng Zhang's 2026 paper on the behavior of the **forward** self-commutator norm
under Aluthge transforms; its optimization variable and question are
different.

## Mechanism and adjacent-result collisions

### Additive Hermitian eigenvalues: strong mechanism collision

The projected epigraph proof relies on the classical characterization of
spectra of Hermitian sums. This machinery must be attributed, and neither the
Horn inequalities nor their completeness can be claimed as new:

- Alfred Horn, “Eigenvalues of sums of Hermitian matrices,” *Pacific Journal
  of Mathematics* **12** (1962), 225--241,
  <https://doi.org/10.2140/pjm.1962.12.225>.
- A. A. Klyachko, “Stable bundles, representation theory and Hermitian
  operators,” *Selecta Mathematica* **4** (1998), 419--445,
  <https://doi.org/10.1007/s000290050037>.
- Allen Knutson and Terence Tao, “The honeycomb model of `GL_n(C)` tensor
  products I: Proof of the saturation conjecture,” *Journal of the American
  Mathematical Society* **12** (1999), 1055--1090,
  <https://doi.org/10.1090/S0894-0347-99-00299-4>;
  preprint <https://arxiv.org/abs/math/9807160>.
- William Fulton, “Eigenvalues, invariant factors, highest weights, and
  Schubert calculus,” *Bulletin of the American Mathematical Society* **37**
  (2000), 209--249,
  <https://doi.org/10.1090/S0273-0979-00-00865-X>.
- Allen Knutson, Terence Tao, and Christopher Woodward, “The honeycomb model
  of `GL_n(C)` tensor products II: Puzzles determine facets of the
  Littlewood--Richardson cone,” *Journal of the American Mathematical Society*
  **17** (2004), 19--48, <https://arxiv.org/abs/math/0107011>.

Moitra, Postnikov, and Woodruff's 2026 *Honeycombs and Sums of Hermitian
Matrices, Revisited*, <https://arxiv.org/abs/2607.06710>, supplies a new proof
of the classical honeycomb/Hermitian-triple equivalence. It is current and
methodologically relevant, but it does not formulate the inverse
self-commutator cost, factor rank, or dimension threshold.

### Self-commutator existence: adjacent, not exact

P. Fan and C.-K. Fong, “Which operators are the self-commutators of compact
operators?”, *Proceedings of the American Mathematical Society* **80**
(1980), 58--60,
<https://doi.org/10.1090/S0002-9939-1980-0574508-X>, is existence background.
The historical context is surveyed by D. Beltiță, S. Patnaik, and G. Weiss,
<https://arxiv.org/abs/1303.4844>. Neither source performs the finite-dimensional
prescribed-target double optimization of norm and implementing rank.

Classical trace-zero commutator results, such as A. A. Albert and B.
Muckenhoupt, “On matrices of trace zero,” *Michigan Mathematical Journal* **4**
(1957), 1--3, <https://doi.org/10.1307/mmj/1028990168>, concern ordinary
commutators and do not imply the claimed rank-optimal self-commutator theorem.

### Forward commutator norms: adjacent, not inverse

Albrecht Böttcher and David Wenzel, “How big can the commutator of two matrices
be and how big is it typically?”, *Linear Algebra and its Applications* **403**
(2005), 216--228, <https://doi.org/10.1016/j.laa.2005.02.012>, and “The
Frobenius norm and the commutator,” *Linear Algebra and its Applications*
**429** (2008), 1864--1885,
<https://doi.org/10.1016/j.laa.2008.05.020>, bound the norm of a commutator
given its factors. They do not minimize a factor norm for a prescribed
self-commutator target or study the rank of norm minimizers.

Teng Zhang, “On a conjecture of lambda-Aluthge transforms and Hilbert--Schmidt
self-commutators,” <https://arxiv.org/abs/2603.04655>, studies contraction of
the forward self-commutator Frobenius norm under a matrix transform. It is not
an antecedent for the inverse problem.

## Public and local self-prior-art audit

### Public GitHub and ARR

The GitHub API returned 34 public repositories for `lluiseriksson`. Authenticated
GitHub code searches for `selfcommutator`, `self-commutator`, `"Horn epigraph"`
and `"inertia lower-bound rank"` returned no matching public file. The local
ARR mirror contains 18 record metadata files; none has a self-commutator,
inverse-commutator, or dimension-eight rank-threshold title, and a full-text
search found no exact theorem. Web searches restricted to the public GitHub
account and ARR likewise produced no match.

This establishes only that no collision was found in the inspected public
surface. It does not prove that an unindexed release, private repository, or
external deposit does not exist.

### Papers 28--30: mandatory disclosure

The local programme has substantial, direct self-prior art:

1. **Paper 28** supplies the one-spike exact cost/rigidity result and earlier
   general rank-adaptive inverse-self-commutator analysis. Its balanced
   reduction, inertia lemma, and equality families are foundations here.
2. **Paper 29** supplies one exact `d=8` strict-gap target,
   `(11,3,3,3,-5,-5,-5,-5)`, with unrestricted value 30 attained first at
   rank five and rank-at-most-four value 32.
3. **Paper 30** absorbs that point into the exact family
   `(4c-3b,b,b,b,-c,-c,-c,-c)`, `0<=b<=c`, and proves rank five throughout
   the interior. It is precisely the dimension-eight witness needed by the
   threshold theorem.
4. Earlier dimension-three, dimension-four, and dimension-five exact papers
   already use related inverse-commutator/Horn reductions. They prevent broad
   phrases such as “the first exact inverse self-commutator solution” or “the
   first application of Horn theory to this optimization.”

The `d<=7` universal epigraph theorem is not contained in Papers 28--30. In
fact, Paper 30's audit explicitly treated it as an open gate. This makes the
new low-dimensional closure a genuine increment, while also making explicit
self-citation indispensable.

## Mathematical support inspected

The singular-stratum-aware replay
`math/verify_d_le_7_epigraph.py` covers 33 inequivalent strata:

```text
d=3:  2 strata,   6 projected facets total
d=4:  4 strata,  18 projected facets total
d=5:  6 strata,  37 projected facets total
d=6:  9 strata,  77 projected facets total
d=7: 12 strata, 134 projected facets total
```

For each stratum it constructs the inertia-rank face epigraph, projects it to
spectral gaps and cost, and certifies every projected facet on the unrestricted
Horn cone by an exact nonnegative rational Farkas identity. Each prescribed
zero eigenvalue is enforced in both orientations, so the certificate really
uses `max(n_+,n_-)`, not a chamber cut that incorrectly counts zeros on one
side. Sign reflection covers the omitted ordering of positive and negative
counts. Dimensions one and two are elementary.

The older `verify_low_dimension_minimality_exact.py` is a useful independent
route for the six nontrivial **nonsingular** chambers, but it is not by itself a
proof for singular targets. The separate 33-stratum replay repairs that scope
gap. Paper 31 should retain this distinction and must not present the older
script alone as proving the all-spectrum theorem.

The exact replay establishes the mathematical statement conditional on the
standard Horn reduction already proved in the programme. It does not classify
the minimizing matrices, prove a universal rank-excess bound above dimension
seven, or establish any persistence under zero-padding into higher dimensions.

## Anti-salami decision

**Recommendation: merge Paper 30 into Paper 31 before any immutable deposit.**

Reasons:

1. Paper 30 proves existence of the dimension-eight separation; Paper 31
   proves its impossibility below dimension eight. These are complementary
   halves of one natural threshold theorem.
2. Paper 31 necessarily repeats Paper 30's reduction, inertia obstruction,
   Horn formulation, and explicit family.
3. The combined statement is substantially stronger and easier to evaluate:
   not merely a counterexample family, but the exact dimensional onset.
4. The local ARR and GitHub checks found no public Paper 30 record, so a clean
   merge appears possible. This is negative evidence only; publication status
   must still be checked immediately before deposit.

If Paper 30 is already immutable or independently submitted, Paper 31 may
proceed only with prominent citation and an explicit `extends` relationship.
Its abstract should say that Paper 30 supplied the `d=8` family and that the
new contribution is the complete `d<=7` theorem closing dimensional
minimality. It must not recycle the family as though new.

## Recommended and prohibited claims

### Recommended headline

> We prove that every traceless Hermitian target in dimension at most seven
> admits a Hilbert--Schmidt norm-minimizing self-commutator factor whose rank
> equals the elementary inertia lower bound. An exact dimension-eight family
> has minimum optimal rank five despite inertia `(4,4)`. Hence dimension eight
> is the sharp onset of norm-optimal factor rank strictly above inertia.

### Conservative priority sentence

> We are not aware of a previous theorem locating this dimensional onset. Our
> claim is the exact low-dimensional attainment theorem and its combination
> with the displayed dimension-eight family, not a new Horn theorem or a
> general classification above dimension eight.

### Prohibit

- “the first” or “the smallest-dimensional self-commutator” without the
  norm-optimality qualifier;
- “minimum self-commutator rank equals inertia for `d<=7`” if the norm
  minimization and existence quantifiers are not stated;
- a classification of all dimension-eight spectra;
- a universal rank-excess-at-most-one theorem;
- persistence of the dimension-eight failure in every higher dimension by
  zero-padding, unless separately proved;
- novelty claims for Horn/Klyachko inequalities, the inertia obstruction,
  self-commutator existence, or the balanced reduction;
- representing the nonsingular six-case script alone as covering singular
  spectra;
- describing bounded literature and repository searches as proof of novelty.

## Audited artifacts and frozen hashes

```text
work/paper31-frontier/math/verify_d_le_7_epigraph.py
e5009d579933af66283de296ac8aa46b8f0b35bae1e43dd300768ef625129bd6

work/paper31-frontier/math/results/d_le_7_epigraph_certificate.json
0103a643644977400052a68738102a7633d6371db8717383ddefa687da8a18a0

work/paper31-frontier/math/verify_low_dimension_minimality_exact.py
552697bf43cbbae52cf9f087b63a7ea0f59070007fb71f03e0099b4fd46fb6e5

work/paper31-frontier/math/INDEPENDENT_LOW_DIMENSION_AUDIT.md
5e6fd8f27d81719173b1f427ba34347294c1137e451dcad876e459668e4bdaac

work/paper30-frontier/results/parametric_family_certificate.json
390fe0686df8939a6b64683acce1a977bfc21ab402054f039bbb4e3fc597c2ff
```

Any change to the theorem, scripts, or certificate invalidates the associated
hash and requires a focused re-audit.

## Final decision

**GO for a single merged sharp-threshold paper.** The `d<=7` exact epigraph
closure is the genuinely new theorem; Paper 30's `d=8` family supplies the
matching sharpness example. No exact external or public self-authored
antecedent was found, but that absence must remain qualified. **HOLD a separate
Paper 30 deposit while merging is still possible.**
