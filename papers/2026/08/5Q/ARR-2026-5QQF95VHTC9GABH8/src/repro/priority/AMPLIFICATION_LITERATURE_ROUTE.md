# Paper 32: literature route for Horn/hive amplification

**Audit date:** 2026-08-24  
**Scope:** primary or authoritative sources; no novelty claim is inferred from
failure to find an antecedent.  
**Status:** the literature supplies an exact way to certify the *Horn
membership* of uniformly block-inflated rows, but it does **not** supply the
rank-face lower bound needed for the all-`k` theorem.

## Executive verdict

There is a materially relevant published construction that should replace any
informal assertion that “replacing every selected index by a block of `k`
indices preserves the Horn property.”  Knutson--Tao--Woodward define puzzle
`N`-inflation by stretching every `1`-edge by `N`, define dual inflation by
doing the same to `0`-edges, and then define commuting `(N,M)`-inflation.  If
`N=M=k`, every bit of each Horn indicator word is repeated `k` times.  Hence a
base puzzle for `(I,J,K)` in `Gr(r,n)` gives an explicit puzzle for

```text
I^[k] = union over i in I of {(i-1)k+1,...,ik},
J^[k] and K^[k] analogously,
```

in `Gr(kr,kn)`.  Puzzle existence proves positivity of the relevant
Littlewood--Richardson coefficient, and rigidity is preserved when the base
puzzle is rigid.  This is exactly the dimension-changing membership lemma
needed for the uniformly inflated `d=9` Horn rows, and it is stronger and more
appropriate here than scalar stretching or the LR semigroup property.

This does **not**, by itself, prove

```text
kappa_(9k)^(<=5k+j)(F_k) = 30k-j.
```

The reason is simple: LR membership validates an inequality; it does not show
that a chosen collection of inequalities has a nonnegative combination equal
to the half-trace objective on the global rank face.  A local rerun of
`math/inflated_horn_certificate_search.py` confirms the distinction.  The
uniformly inflated `d=9` rows attain the desired dual value `30k` on the
`rank<=5k` endpoint.  On the decisive `rank<=6k-1` face they give only `29k`
in the tested cases (`58` rather than `59` for `k=2`, and `87` rather than
`88` for `k=3`).  Thus the published inflation theorem closes the LR-validity
gate for those rows, but the endpoint rows alone do not close the all-`k`
rank-excess gate.

**Recommended route:** prove a new, explicit rank-face Farkas certificate on
the order-`9k` hive, using `(N,M)`-inflated puzzles to certify every Horn row
that appears.  If the complete curve is too expensive, an equality-rigidity
lemma for the `29k` optimal face would suffice for the headline
`r_*(F_k)=6k`, but it would not establish the displayed `30k-j` curve.

## Three operations that must not be conflated

| Operation | Fixed or changing dimension? | What the literature gives | Relevance to Paper 32 |
|---|---:|---|---|
| Scalar stretching `(lambda,mu,nu) -> (N lambda,N mu,N nu)` | Fixed number of parts / same hive grid | Saturation, polynomiality of stretched LR coefficients, and rigidity/multiplicity-one results | Does not replicate eigenvalue multiplicities or move the face from `5`/`6` to `5k+j` |
| LR-semigroup or hive addition | Fixed order `n` | Adding two same-order hives adds their boundary weights; nonzero LR triples form a semigroup | Proves feasibility/nonvanishing after coordinatewise addition, not concatenation into order `9k` and not a lower bound |
| Puzzle `(N,M)`-inflation | Changes puzzle size from `n` to `Nr+M(n-r)` when the boundary has `r` ones | Explicit dimension-changing puzzle with `1`-edges stretched by `N` and `0`-edges by `M`; rigidity is preserved under the component inflations | With `N=M=k`, gives precisely the block-repeated indicator strings in `Gr(kr,kn)` |

The third operation is the genuinely useful one.  It appears in Lemma 8 and
Sections 5--6.2 of Knutson--Tao--Woodward.  Their paper also proves that
puzzles compute the relevant Grassmannian Schubert intersections, so the
construction is a proof of LR/Horn membership rather than a visual analogy.

## The published lemma that can be used verbatim

The following is a direct specialization of the puzzle results, not a new
claim of Paper 32.

> **Uniform bit-block inflation lemma (Knutson--Tao--Woodward).** Let
> `(pi,rho,sigma)` be the three `0/1` boundary strings of a size-`n` puzzle,
> each with `r` ones.  Replace every `1` in each string by `k` ones and every
> `0` by `k` zeros.  The resulting three strings bound a size-`kn` puzzle and
> therefore index a nonzero Schubert intersection in `Gr(kr,C^(kn))`.  If the
> original puzzle is rigid, the inflated puzzle is rigid.

For Paper 32, encode a subset `I subset [9]` by its nine-bit indicator.  The
inflated subset in `[9k]` is exactly `I^[k]` above.  Therefore every base Horn
triple used in the `d=9` certificate can be lifted to a valid Horn triple in
dimension `9k`, provided an explicit base puzzle (or equivalently a positive
Schubert intersection) is supplied.  If the manuscript wants an essential
facet rather than merely a valid inequality, use a rigid base puzzle and cite
the rigidity/facet results rather than merely citing saturation.

Two qualifications are essential:

1. The theorem certifies each inflated row separately.  It says nothing about
   the nonnegative multipliers needed to synthesize the cost functional.
2. Uniform `(k,k)` inflation makes the selected cardinality a multiple of
   `k`.  Intermediate rank faces `5k+j`, especially `j=k-1`, may require
   genuinely global or seam-sensitive puzzles not obtained by uniformly
   inflating the small endpoint list.

## Exact new lemma that would close the complete all-`k` curve

Let `p_1 >= ... >= p_(9k) >= 0` be the common nonzero spectral variable for
the two positive semidefinite matrices in the Horn reduction, and impose
`p_(5k+j+1)=...=p_(9k)=0`.  Write every valid Horn inequality after substituting
the fixed target boundary as

```text
<a_t(k,j), p> >= b_t(k,j).
```

An exact theorem sufficient for the paper is:

> **Rank-face Horn certificate lemma (new; preferred target).** For every
> `k>=1` and `0<=j<=k`, there is an explicitly indexed finite family of valid
> order-`9k` puzzle/Horn rows and nonnegative rational multipliers
> `alpha_t(k,j)`, together with nonnegative multipliers for the order rows
> `p_i-p_(i+1)>=0` and `p_(5k+j)>=0`, such that their coefficient identity is
> exactly
>
> ```text
> (1/2) sum_(i=1)^(5k+j) p_i >= 30k-j.
> ```
>
> Every Horn row in the family is certified by an explicit puzzle (uniformly
> inflated when possible), and the coefficient and right-hand-side identities
> hold over `Q`, symbolically in `(k,j)`.

Together with the already explicit direct-sum primal of rank `5k+j` and cost
`30k-j`, this lemma proves the full curve by strong LP duality without any
assumption that an optimizer respects the nine-dimensional block
decomposition.

For publication-grade rigor the lemma should be presented as an actual
telescoping identity, not as “the solver returns the same pattern.”  A suitable
proof object is either:

- a formula for nonnegative weights on the three orientations of order-`9k`
  hive rhombi, including all seam and boundary weights, whose internal hive
  variables cancel; or
- a short list of explicit puzzle families with rational multipliers, plus
  an exact coefficient-vector identity on the rank face.

The current finite exact hive duals are useful discovery fixtures, but their
supports and denominators do not yet display a stable formula.  Uniformly
inflating only the existing `d=9` endpoint rows is insufficient on the key
`6k-1` face, as the local tests above show.  The new ingredient must therefore
be a seam/global face gadget or a different structural argument.

## Weaker exact lemma sufficient for unbounded rank excess

The complete curve is not logically necessary for the headline result.  The
following would also close unbounded additive excess:

> **Optimal-face rank lemma (new; weaker conclusion).** Every feasible
> order-`9k` Horn/hive point with half-trace cost `29k` has at least `6k`
> positive `p_i`; equivalently, no point on the face `p_(6k)=0` attains the
> unrestricted optimum.

The inflated full-cost certificate can establish `cost>=29k`, and the explicit
rank-`6k` primal attains it.  The new equality statement then proves
`r_*(F_k)=6k` even without the stronger quantitative bound `29k+1` on
`rank<=6k-1`.

There is relevant equality/factorization machinery, but it is not turnkey.
Knutson--Tao describe direct sums of Hermitian triples as honeycomb overlays
and relate generic facet equality to a clockwise overlay.  King--Tollu--
Toumazet prove factorization of LR coefficients when an essential Horn
inequality is saturated.  These results suggest examining simultaneous
equality in the inflated full-cost rows.  However, Paper 32 has heavily
repeated spectra, hence lies on chamber walls; generic or regular-boundary
block-diagonalization statements cannot simply be invoked.  A proof must show
directly that equality in the particular collection of rows forces
`p_(6k)>0`, or give a degeneration argument that preserves the required rank
conclusion.

## What the other cited theories contribute—and what they do not

### LR semigroups and same-grid hive addition

Zelevinsky formulates the semigroup `LR_r` of nonzero triples of partitions of
length at most `r`; Derksen--Weyman identify the relevant saturated
semi-invariant cone.  At the hive level, adding two hives of the same order
adds their boundary values and preserves all rhombus inequalities.

This is useful for combining or checking fixed-order certificates.  It does
not transform a nine-part spectrum into a `9k`-part spectrum with repeated
entries, and it gives feasibility rather than the reverse inequality needed
for an optimum.

### Scalar stretching and hive dilation

Knutson--Tao prove saturation.  Derksen--Weyman and Rassart prove polynomiality
properties for `c_(N lambda,N mu)^(N nu)` (with Rassart working on chambers of
a fixed-rank vector partition function).  Knutson--Tao--Woodward prove the
multiplicity-one stretching statement using puzzle inflation/dual inflation.

These results keep the number of weight coordinates fixed when interpreted as
ordinary scalar stretching.  They count or certify integer hives; they do not
identify the optimum of the Paper 32 LP, its supporting dual functional, or
the number of positive entries of `p`.

### Tensor-product and combined-eigenvalue inequalities

Fomin--Fulton--Li--Poon give Horn-type characterizations involving the
combined eigenvalue list of summands.  Their Proposition 2.9 can redistribute
the combined list of eigenvalues among several same-size Hermitian matrices
while preserving their sum.  This is a useful warning that global mixing can
beat a prescribed block assignment.

It does not force two summands to retain the same spectrum, preserve the
Paper 32 rank face, or prove additivity of the inverse self-commutator cost.
It therefore cannot justify reducing all optimizers to direct sums of `d=9`
optimizers.

### Bounded-rank eigenvalue cones

Buch gives a minimal set of Schubert-calculus inequalities for Hermitian
matrices whose *sum* is positive semidefinite of rank at most `r`.  The extra
rank inequalities live on Grassmannians of complementary dimension `n-r`.
This is the closest published model for how a rank restriction can create a
second family of Horn-type inequalities, and it may inspire the indexing of a
rank-face dual.

It is not the Paper 32 constraint.  Here the fixed difference is indefinite
and the zeros occur in the common spectra of two individual PSD summands.  No
direct substitution into Buch's theorem turns this into a bounded-rank PSD
*sum*.  A reduction would itself need proof.

### Facets and Levi induction

Knutson--Tao--Woodward classify regular facets of a fixed eigencone by rigid
puzzles.  Belkale--Kiers describe extremal rays on regular faces by induction
from Levi subgroups.  These are useful languages for a large-order dual face
or for a seam decomposition.

They do not provide a functor taking the specific `n=9` optimal face to the
specific degenerate face in `n=9k`, and they do not automatically preserve the
linear objective or the support size of `p`.

## Explicit non-implications to state in the manuscript or proof notes

- Direct sums and honeycomb overlays prove the candidate **upper bounds**;
  they do not exclude non-block-diagonal optimizers.
- `kappa` has not been proved additive in the reverse direction required for
  a lower bound.
- LR-semigroup closure and hive addition are fixed-order feasibility
  statements, not block-replication lower bounds.
- Saturation concerns scalar dilation of weights in fixed rank; it does not
  by itself validate indicator-block inflation.  Cite `(k,k)` puzzle
  inflation for that step.
- Validity of each inflated Horn row does not imply that the endpoint list
  spans the desired rank-face dual.  It demonstrably misses one unit on the
  tested `6k-1` faces.
- Polynomiality of stretched LR coefficients counts lattice points; it does
  not locate a supporting facet, an LP optimum, or an optimal rank.
- Multiplicity one under stretching is not an equality-rigidity theorem for
  the present repeated real spectra.
- A generic facet equality can force a honeycomb overlay, but the Paper 32
  boundary is nonregular.  Generic block-diagonalization cannot be invoked
  without a degeneration/equality argument tailored to this boundary.
- Buch's bounded-rank theorem constrains the rank of a PSD sum, not the ranks
  of the two isospectral PSD summands in a fixed indefinite difference.
- Tensoring representations adds highest weights in a fixed group; a block
  direct sum concatenates spectra and changes the group dimension.
- Matrix tensor/Kronecker products multiply spectra and are unrelated to the
  block direct sum used here.
- Finite rational hive duals for `k<=5` remain finite certificates; no amount
  of denominator rationalization proves a symbolic all-`k` pattern.

## Concrete proof program

1. Encode every `d=9` full-cost and rank-five Horn row by a concrete rigid
   puzzle; freeze the three boundary bitstrings and verify their Schubert
   coefficient exactly.
2. Apply `(k,k)` puzzle inflation and prove in one line that it produces the
   exact block-expanded subsets used by the code.  This closes the uniform-row
   LR gate for arbitrary `k`.
3. Use the inflated rows to write the exact endpoint certificates
   `cost>=29k` and `cost>=30k` on `rank<=5k`; check coefficients symbolically.
4. Study the exact finite duals specifically on `j=k-1`.  Search for a
   bounded-width seam gadget rather than for a global list of hundreds of
   rhombi.  A candidate gadget must contribute exactly one to the right side
   while correcting the coefficient of the last active `p` variable.
5. Prove the seam gadget is a valid puzzle/Horn row (or a nonnegative sum of
   rhombus inequalities) for every `k`; then telescope `k` bulk cells plus the
   seam.
6. Replay the coefficient identity over integers/rationals and independently
   verify each puzzle boundary with an LR tableau or exact hive checker.
7. If Step 4 fails, switch to the weaker optimal-face rank lemma and analyze
   equality in the uniformly inflated full-cost rows using saturated-facet
   factorization, explicitly treating repeated spectra.

## Primary and authoritative bibliography

1. A. Knutson and T. Tao, “The honeycomb model of `GL_n(C)` tensor products I:
   proof of the saturation conjecture,” *J. Amer. Math. Soc.* **12** (1999),
   1055--1090. DOI: <https://doi.org/10.1090/S0894-0347-99-00299-4>;
   preprint: <https://arxiv.org/abs/math/9807160>.
2. A. Knutson, T. Tao and C. Woodward, “The honeycomb model of `GL_n(C)`
   tensor products II: Puzzles determine facets of the
   Littlewood--Richardson cone,” *J. Amer. Math. Soc.* **17** (2004), 19--48.
   DOI: <https://doi.org/10.1090/S0894-0347-03-00441-7>; preprint:
   <https://arxiv.org/abs/math/0107011>.  See especially Lemma 8 and Sections
   5, 6.1 and 6.2 for puzzle, dual, and `(N,M)` inflation.
3. A. Knutson and T. Tao, “Honeycombs and sums of Hermitian matrices,”
   *Notices Amer. Math. Soc.* **48** (2001), 175--186. Preprint:
   <https://arxiv.org/abs/math/0009048>.  See the overlay/direct-sum discussion
   and the generic facet-equality discussion.
4. A. Zelevinsky, “Littlewood--Richardson semigroups,” MSRI preprint 1997-044,
   <https://arxiv.org/abs/math/9704228>.
5. H. Derksen and J. Weyman, “Semi-invariants of quivers and saturation for
   Littlewood--Richardson coefficients,” *J. Amer. Math. Soc.* **13** (2000),
   467--479. DOI: <https://doi.org/10.1090/S0894-0347-00-00331-3>.
6. H. Derksen and J. Weyman, “On the Littlewood--Richardson polynomials,”
   *J. Algebra* **255** (2002), 247--257. DOI:
   <https://doi.org/10.1016/S0021-8693(02)00125-4>.
7. E. Rassart, “A polynomiality property for Littlewood--Richardson
   coefficients,” *J. Combin. Theory Ser. A* **107** (2004), 161--179. DOI:
   <https://doi.org/10.1016/j.jcta.2004.04.003>; preprint:
   <https://arxiv.org/abs/math/0308101>.
8. I. Pak and E. Vallejo, “Combinatorics and geometry of
   Littlewood--Richardson cones,” *European J. Combin.* **26** (2005),
   995--1008. DOI: <https://doi.org/10.1016/j.ejc.2004.06.008>; preprint:
   <https://arxiv.org/abs/math/0407170>.
9. S. Fomin, W. Fulton, C.-K. Li and Y.-T. Poon, “Eigenvalues, singular
   values, and Littlewood--Richardson coefficients,” *Amer. J. Math.* **127**
   (2005), 101--127. DOI: <https://doi.org/10.1353/ajm.2005.0005>; preprint:
   <https://arxiv.org/abs/math/0301307>.  See Propositions 2.2 and 2.9 for
   combined-list redistribution.
10. A. S. Buch, “Eigenvalues of Hermitian matrices with positive sum of
    bounded rank,” *Linear Algebra Appl.* **418** (2006), 480--488. DOI:
    <https://doi.org/10.1016/j.laa.2006.02.024>; preprint:
    <https://arxiv.org/abs/math/0411063>.
11. R. C. King, C. Tollu and F. Toumazet, “Factorisation of
    Littlewood--Richardson coefficients,” *J. Combin. Theory Ser. A* **116**
    (2009), 314--333. DOI:
    <https://doi.org/10.1016/j.jcta.2008.06.005>.
12. P. Belkale and J. Kiers, “Extremal rays in the Hermitian eigenvalue
    problem for arbitrary types,” *Transformation Groups* **25** (2020),
    667--706. DOI: <https://doi.org/10.1007/s00031-019-09547-2>; preprint:
    <https://arxiv.org/abs/1803.03350>.

## Gate

**GO for the uniform Horn-membership sublemma:** cite and instantiate
Knutson--Tao--Woodward `(k,k)` puzzle inflation with explicit base puzzles.

**NO-GO for the all-`k` Paper 32 theorem on literature alone:** none of the
sources above yields the required half-trace lower certificate or optimal-rank
statement.  The paper becomes mathematically ready only after the new
rank-face certificate lemma (preferred) or the weaker optimal-face rank lemma
is proved exactly.
