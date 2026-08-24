# Exterior-power list decoding of strictly scalable full-spark rays

## Known learning width and its physical-space cone

Johnston--Lovitz--Russo--Sikora (arXiv:2510.20789) define this exact
candidate-list task as `k`-learnability and prove that its minimum perfect
list size (learning width) equals the factor width of the state Gram matrix.
The general feasibility criterion below is therefore not new.  Its role here
is to translate sparse Gram factors into physical annihilators and expose the
weighted Hodge construction on the closed full-spark branch.

The full-spark theorem is the sharp closed branch of a more general exact
criterion.  Let nonzero pure-state vectors `f_1,...,f_N` span `C^r`, and for
`v!=0` define its frame zero set

```text
Z(v)={i : <f_i,v>=0}.
```

There is a perfect decoder with lists of size at most `ell` if and only if

```text
I_r belongs to cone{ |v><v| : |Z(v)| >= N-ell }.              (AC)
```

This is a realization-sensitive annihilator cone.  Maximal allowed zero sets
are hyperplane flats of the represented matroid, while membership of the
identity in their projector cone is additional positive geometry not
determined by ranks.

For sufficiency, write `I=sum_a c_a|v_a><v_a|` with `c_a>0`, use these
summands as POVM effects, and on outcome `a` report `[N]\Z(v_a)`.  Conversely,
spectrally decompose every effect `M_L` of a perfect list POVM.  Positivity and
zero error imply that every eigenvector in the support of `M_L` is orthogonal
to all `f_i` with `i notin L`, so every resulting rank-one summand satisfies
`|Z(v)|>=N-|L|>=N-ell`.  Summing the decompositions gives (AC).

Conic Caratheodory immediately shows that whenever perfect decoding is
possible, it is possible with at most `r^2` outcomes.  This physical form
also explains the two independent gates in the closed theorem below:
full spark fixes the largest possible zero set at `r-1`, whereas strict
scalability puts the identity inside the corresponding boundary cone.

## Headline theorem

Let `F={f_1,...,f_N}` be a finite nonzero tight frame in `C^r`,
`sum_i |f_i><f_i|=alpha I`, with `N>r`, and assume it is full spark: every
`r` frame vectors are linearly independent.  The physical pure states are
the normalized rays `rho_i=|g_i><g_i|`, where `g_i=f_i/||f_i||`.  Equivalently,
the unit ray ensemble is strictly scalable by positive weights.  A list
decoder is a POVM `{M_L}` whose
outcome is a subset `L` of the labels with `|L|<=ell`; it succeeds perfectly
when

```text
Tr(rho_i M_L)=0 whenever i is not in L.
```

Then the smallest list size allowing perfect decoding is exactly

```text
ell_0 = N-r+1.
```

At the threshold there is an explicit exterior-power POVM.  For every
`E subset [N]` with `|E|=r-1`, let

```text
w_E = star(f_(i_1) wedge ... wedge f_(i_(r-1))) in C^r,
```

where `star` is the conjugate-linear Hodge identification
`wedge^(r-1) C^r -> C^r`.  With the general frame bound
`alpha=(1/r)sum_i ||f_i||^2`,

```text
M_E = alpha^(-(r-1)) |w_E><w_E|
```

is a POVM.  On outcome `E`, report the complementary list
`L_E=[N]\E`, of size `N-r+1`.

The construction has `binom(N,r-1)` displayed outcomes.  The general
annihilator-cone criterion and conic Caratheodory give a sub-POVM using at most
`r^2` of the same complementary lists.

## Robust subthreshold theorem

For arbitrary density operators `rho_i` on `C^r` with nonnegative priors
`p_i`,
define

```text
Q_L = sum_(i notin L) p_i rho_i,
gamma_ell = min_(|L|<=ell) lambda_min(Q_L).
```

Every list POVM obeys the spectral converse

```text
P_err >= r gamma_ell.
```

For a full-spark pure ensemble with full-support priors, `gamma_ell>0`
whenever `ell<=N-r`, because each omitted set contains `r` spanning rays.  If
`||rho_i_tilde-rho_i||_op<=epsilon_i`, the stable version is

```text
P_err_tilde >= r max(0, gamma_ell-sum_i p_i epsilon_i).
```

This is a general quantitative converse, not a claim that the lower bound is
always attained.

## Complete proof

### Converse

Suppose `ell<=N-r`.  Every reported list `L` omits at least `r` labels.
Perfect success implies

```text
M_L f_i = 0  for every i not in L.
```

The implication follows from positivity: if
`<f_i,M_L f_i>=0`, then `M_L^(1/2)f_i=0`.  By full spark, any `r` omitted
vectors span `C^r`, so `M_L=0`.  Thus every POVM effect would vanish, a
contradiction.  Hence `ell>=N-r+1` is necessary.

### Exterior tightness identity

Let `T:C^N->C^r` be the synthesis operator, `T e_i=f_i`.  Tightness gives

```text
T T^* = alpha I_r.
```

Apply the `(r-1)`-st exterior-power functor.  Its columns in the canonical
basis of `wedge^(r-1) C^N` are the wedges `f_E`, and

```text
(wedge^(r-1)T)(wedge^(r-1)T)^*
 = wedge^(r-1)(T T^*)
 = alpha^(r-1) I_(wedge^(r-1) C^r).
```

The Hodge identification is antiunitary, so

```text
sum_(|E|=r-1) |w_E><w_E| = alpha^(r-1) I_r.
```

Therefore the stated effects sum to the identity.

### Zero-error property

For every `i in E`, the Hodge vector `w_E` is orthogonal to `f_i`.
Consequently

```text
Tr(rho_i M_E)=0  for i in E=[N]\L_E.
```

The decoder never omits the true label, proving sufficiency at
`ell=N-r+1`.  Together with the converse this proves the exact threshold.

Full spark is used only for the converse; strict scalability is used only for
the explicit positive resolution of the identity.  If unit representatives
`g_i` satisfy `sum_i lambda_i |g_i><g_i|=I` with all `lambda_i>0`, the Hodge
wedges use `f_i=sqrt(lambda_i)g_i`.  Individual normalization need not preserve
tightness.  This separation is important for the counterexamples below.

## Weyl-channel corollary: exact Schmidt-rank/list frontier

Let `d>=2` and let the uniformly distributed channel be one of the `d^2`
Weyl channels

```text
Ad_(X^a Z^b),  (a,b) in Z_d^2.
```

Use the fixed rank-`r` flat-Schmidt probe

```text
|Phi_r> = r^(-1/2) sum_(x=0)^(r-1) |x>|x>,  1<=r<=d.
```

The outputs split into `d` mutually orthogonal shift sectors.  In each
sector the `d` phase states are the harmonic frame

```text
|phi_b> = r^(-1/2) sum_(x=0)^(r-1) exp(2 pi i bx/d)|x>.
```

This is a unit-norm tight frame with bound `d/r`.  Every `r by r` minor is a
Vandermonde determinant on distinct `d`-th roots, hence it is full spark.
Applying the theorem sectorwise gives the exact fixed-probe frontier

```text
perfect Weyl list decoding  iff  ell >= d-r+1.
```

Necessity remains valid for a global measurement: after pinching into the
orthogonal shift sectors, each nonzero block would have to annihilate at least
`r` phase states if `ell<=d-r`.  Sufficiency first measures the shift sector
and then uses its exterior POVM.

Thus each additional flat Schmidt coefficient decreases the exact zero-error
list cost by one:

```text
r=1: ell_0=d,        r=d: ell_0=1.
```

This is a fixed-probe theorem.  It does not claim that a nonflat rank-`r`
probe or an arbitrary adaptive tester has the same frontier.

## Strict separation from rank and projector obstructions

For one harmonic sector, the `ell`-fold support-matroid obstruction disappears
when

```text
ell >= ceil(d/r),
```

and the projector inequality gives the same necessary condition because
`sum_b rho_b=(d/r)I`.  The exact physical threshold is instead

```text
d-r+1.
```

It can be strictly larger.  For `(d,r)=(4,2)`, both coarse obstructions vanish
at `ell=2`, while perfect decoding requires `ell=3`.  More broadly, this
provides an infinite exact family showing that support rank and the summed
projector test can both miss a zero-error obstruction.

## Exact support-pattern counterexample

The value `d-r+1` is specific to the consecutive-support probe.  If `r|d`,
write `q=d/r` and use the equally entangled arithmetic-support probe

```text
Psi_r = r^(-1/2) sum_(t=0)^(r-1) |qt>|t>.
```

The output identifies `a` and `b mod r` exactly, while each observed vector is
shared by precisely `q` labels.  Its exact threshold is therefore `d/r`.
For `(d,r)=(4,2)`, this is list two, compared with list three for consecutive
support.  Schmidt rank alone does not determine the frontier.

## Global Weyl optimization in the divisor branch

The arithmetic probe is globally optimal among all pure rank-`r` probes when
`r|d`.  For any such probe, all `d^2` output vectors lie in a subspace of
dimension `D<=dr`.  If `{M_L}` is a perfect list POVM of size `ell`, compress
it to that output support.  Since every output state is at most the support
identity,

```text
1 = d^(-2) sum_L Tr[M_L sum_(i in L) rho_i]
  <= ell*d^(-2) sum_L Tr M_L
  = ell*D/d^2
  <= ell*r/d.
```

Thus `ell>=d/r`; the arithmetic-support construction attains equality.  Hence

```text
min_(pure probe psi: Schmidt rank r) ell_min(psi) = d/r,   when r|d.
```

For `r` not dividing `d`, only the universal lower bound `ceil(d/r)` and the
consecutive-support upper bound `d-r+1` are claimed here.

## Exact complete rank-two Weyl Bayes curve

For the consecutive-support rank-two probe, the optimum is closed for every
list size, not only at zero error:

```text
P_succ^*(d,ell)
 = [ell + sin(pi ell/d)/sin(pi/d)]/d,    1<=ell<=d.
```

Within each orthogonal shift sector the phase states are the regular
equatorial `d`-gon.  The largest eigenvalue of the sum over a phase list is
`[|L|+|sum_(b in L) omega^b|]/2`.  The root sum is largest for consecutive
vertices and equals `sin(pi ell/d)/sin(pi/d)`, giving the upper bound.  A
translated top eigenvector produces a covariant POVM that attains it.  The
covariance machinery is classical; the claim here is the list-valued closed
curve for this Weyl probe.

## Counterexamples showing both hypotheses are essential

### Tight but not full spark

In `C^2`, take the duplicated orthonormal basis

```text
f_1=f_2=e_1,  f_3=f_4=e_2.
```

It is unit-norm tight but not full spark.  A basis measurement reports
`{1,2}` or `{3,4}`, so perfect decoding uses `ell=2`, below
`N-r+1=3`.  Full spark cannot be deleted from the converse.

### Full spark but not strictly scalable

In `C^2`, take

```text
f_1=|0>,
f_2=(3|0>+|1>)/sqrt(10),
f_3=(3|0>-|1>)/sqrt(10).
```

Every pair is independent, so the frame is full spark, but all three Bloch
vectors lie strictly in the positive `z` hemisphere.  Perfect list-two
decoding would be single-state exclusion.  Every effect excluding `f_i` is a
nonnegative multiple of the projector onto `f_i^perp`, whose Bloch vector has
strictly negative `z` component.  Such effects cannot sum to the identity,
whose Bloch vector is zero.  Therefore `ell=2=N-r+1` is impossible.  The same
positive-hemisphere argument rules out every strictly positive tight
rescaling of these rays.  Strict scalability cannot be deleted from the
attainment theorem.

### Further claim boundaries

* Zero prior labels must first be removed; otherwise the operational support
  is not the displayed `N`-label frame.
* Full-rank mixed states cannot be annihilated by a nonzero effect; the pure
  frame theorem does not extend by replacing vectors with density matrices.
* Near-tight frames do not inherit exact zero error by continuity.  The robust
  theorem gives a positive error floor only while its explicit perturbation
  budget remains below `gamma_ell`.
* The full minimum-error curve is closed only for the consecutive rank-two
  Weyl family, not for arbitrary frames or higher rank.

## Why this is autonomous rather than Paper 21 salami

Paper 21 supplies support-polymatroid upper bounds.  The present theorem uses
a different invariant and proof mechanism: the `(r-1)`-st compound of a
tight synthesis operator produces the decoder itself.  It also proves an
infinite strict gap after both the matroid and projector obstructions have
already vanished.  The Weyl corollary is an operational application, not the
source of the theorem.  A standalone paper would center exterior geometry,
exact zero-error thresholds, POVM compression, and the Schmidt-rank/list
frontier; Paper 21 would appear only as a comparison.

## Gates and ranking

| Gate | Status |
|---|---|
| learning width = factor width (prior result) | CITED / USED |
| physical-space cone translation | PASS |
| exact converse from full spark | PASS |
| exterior-power tight-frame identity | PASS |
| explicit threshold POVM | PASS |
| at-most-`r^2` outcome compression | PASS, constructive nullspace elimination |
| harmonic-frame/Weyl reduction | PASS |
| arithmetic-support same-rank counterexample | PASS |
| global divisor-branch probe optimum | PASS |
| robust spectral error floor and perturbation law | PASS |
| exact rank-two Weyl Bayes curve | PASS |
| necessity of both hypotheses | PASS |
| lightweight numerical/exact replay | PASS |
| primary-source priority audit | PASS, scoped; general criterion withdrawn from novelty |
| no-salami/autonomy | PASS provisionally |

Mathematical closure: **9.0/10**.  Operational strength: **8.5/10**.
Priority confidence: **6.8/10** until the multi-state-exclusion and exterior
frame literatures are searched claim by claim.  Provisional standalone paper
strength: **7.8--8.2/10** if priority survives; otherwise the safe result is a
strong Paper 21 theorem rather than a separate paper.
