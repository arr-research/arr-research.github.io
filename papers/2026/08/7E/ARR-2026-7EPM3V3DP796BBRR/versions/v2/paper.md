# Coarse information and finite rank obstructions for flat lattice Hodge forms

Canonical source: paper.pdf. Machine-readable text follows; mathematical layout and formulas should be checked against the exact PDF.

Coarse information and finite rank obstructions
for flat lattice Hodge forms
Lluis Eriksson
30 October 2026
Abstract
On a finite periodic lattice with unit spacing, a flat Hodge form cannot have a positive
coercivity constant uniform under refinement if it is supplemented only by linear observations
in a fixed finite-dimensional real space and linear fine-space repairs of uniformly bounded rank.
The linear observations may vary arbitrarily with the refinement, and their penalty need only
vanish at zero. We prove the same obstruction directly on kernels of uniformly bounded rank
constraints. The proof constructs a real physical Fourier subspace of dimension2(2R+ 1)d
with Hodge energy at most4π2dR2/n2 times its squared norm. Its intersection with the
unobserved directions gives a necessary rank budget. We also explain why this budget is not
sufficient, using a two-dimensional cross-coupling example and a classical complete criterion
for a fixed map. The Fourier construction, finite budget, and uniform obstructions have Lean
proofs; the fixed-map criterion is an analytic result here. These are finite flat statements,
with no interacting or continuum mass-gap claim.
1 Purpose and relation to the existing record
This text consolidates a continuation of the exact-kernel obstruction in [1]. That paper exhibits
fields in the kernel of a particular line-integral block map. Changing the map can remove a
particular witness. Here the obstruction depends instead on the amount of coarse information: a
whole low-energy subspace is too large to be seen by a fixed-dimensional measurement together
with a bounded-rank repair. The map need not factor through the original block variable, be
local, or obey a norm bound; it is always real-linear. The penalty applied to its output may
be nonlinear. The restricted-sector result is proved separately and does not follow merely from
failure of an estimate on the full space.
Fourier diagonalization, rank-nullity and finite-dimensional Schur complements are classical.
For the singular Schur complement and pseudoinverse background, see Albert and Carlson–
Haynsworth–Markham [3, 4]. Finite-difference Hodge theory has a long history; Dodziuk’s work
[2] provides historical context, rather than this paper’s specific lattice normalization. We make
no claim to a new general spectral principle or an exhaustive priority search. The contribution is
a concrete, reproducibly checked constraint on proposed repair routes in this programme. This
consolidation is intended for the existing paper dossier, rather than an additional deposit for
each lemma.
Gauge-fixing and block averaging in renormalization-group constructions require their own
domain and scaling analysis. Dimock [5] develops covariant axial gauge for an abelian model and
discusses its relation to Balaban’s programme. His introduction distinguishes a finite unit lattice
1

from a torus with small spacing, equivalently a large unit-spacing volume. Our unrestricted, unit-
spacing flat form is not identified with every constrained fluctuation form in those constructions.
This negative diagnostic does not refute their gauge-fixed estimates or establish an interacting
bound.
2 Spaces and the actual flat form
Fix integersd≥1, n≥1 and Nc ≥2. Set Xn = (Z/nZ)d and m= N2
c −1. The real one-cochain
space is
En = {A: Xn ×{1,...,d }−→Rm}, ∥A∥2 =
∑
x∈Xn
d∑
i=1
∥Ai(x)∥2.
The internal coordinates are those of the repository’s Euclidean Lie-coordinate model. No
identification with a matrix Lie algebra is required here. For positive unordered plaquettesi<k ,
define
(dA)ik(x) = Ak(x+ ei) −Ak(x) −Ai(x+ ek) + Ai(x),
(δA)(x) =
∑
i
(
Ai(x) −Ai(x−ei)
)
.
The flat operatorK0,n is the actual repository Hodge operator, with
⟨A,K0,nA⟩= ∥dA∥2 + ∥δA∥2. (1)
The plaquette norm sums each pair once. All differences have unit spacing; there is no hiddenn2
or block-side squared factor.
Choose a directionj and two distinct internal unit coordinatesu,v. They exist sincem≥3.
Forf : Xn →C, put
(Ejf)i(x) =
{
(ℜf(x))u+ (ℑf(x))v, i = j,
0, i ̸= j.
This is a real-linear injection and∥Ejf∥2 = ∑
x|f(x)|2. WritingDif(x) = f(x+ ei) −f(x), the
actual curl and divergence give
⟨Ejf,K0,nEjf⟩=
∑
i̸=j
∑
x
|Dif(x)|2 +
∑
x
|f(x) −f(x−ej)|2 =
∑
i
∑
x
|Dif(x)|2. (2)
The last equality is finite translation invariance. The exclusive two plaquette incidences and the
divergence term account for every direction exactly once, with no extra factor two.
3 The original block kernel and its repair budget
We retain the principal results of the historical paper [1] before explaining the new information-
budget obstruction. The original Appendix A (an even-block square-wave witness with quotient
8/ℓ) remains in the preserved v1; it is not reproduced here. Use positive integersℓ,N′, set
n= ℓN′, and for a coarse sitey put By = {ℓy+ r: 0 ≤ri <ℓ}. The original line-integral map is
(QℓA)i(y) = ℓ−d ∑
x∈By
ℓ−1∑
k=0
Ai(x+ kei).
2

For a constant fieldAi(x) = vi and S = ∑
i∥vi∥2 >0,
∥A∥2 = ℓd(N′)dS, ∥ℓσQℓA∥2 = ℓ2σ+2(N′)dS.
A uniform Poincare estimate must therefore haveσ ≥(d−2)/2 if it is to survive this sector.
Equality alone makes the two powers identical. Larger exponents pass this necessary test too;
neither equality nor the inequality is a sufficient full-space condition. This follows by cancelling
(N′)dS to obtainℓd−2−2σ ≤CP. The real-exponent comparison is analytic here.
For d≥2 choose distinct directionsp,q and the real isometryι(z) = (ℜz)u+ (ℑz)v from
Section 2. Forℓ≥2 define
A(ℓ)
i (x) = 1i=pι
(
e2πixq/ℓ)
, λ ℓ = |e2πi/ℓ −1|2 = 4 sin2(π/ℓ).
The character is well defined onXℓN′ . The sum over theq-offset in every block is a nontrivial
root-of-unity sum and vanishes. Shifts in the line directionp do not change the profile. Hence
QℓA(ℓ) = 0, δA (ℓ) = 0, ∥A(ℓ)∥2 = (ℓN′)d, ⟨A(ℓ),K0,nA(ℓ)⟩= (ℓN′)dλℓ. (3)
Only the plaquette pair containingp,q contributes to the curl energy; its difference has constant
squared normλℓ at every site. This also explains the exact energy in(3), including periodic
boundary jumps.
Consequently any scale-wise estimate
∥A∥2 ≤CP(ℓ)
(
⟨A,K0,nA⟩+ Ψℓ(QℓA)
)
, Ψℓ(0) = 0,
forces CP(ℓ) ≥λ−1
ℓ ≥ℓ2/(4π2). No fixedCP >0 before all block sides can work. This includes
Ψℓ(y) = ∥Tℓy∥2 for arbitrary linear postconditioners, and all critical or faster scalar rescalings.
There is no regularity or sign assumption on the scalar functionΨℓ.
The original spectral strengthening is retained analytically. For1 ≤r ≤R ≤⌊(ℓ−1)/2⌋,
replace the profile byι(ce2πirxq/ℓ), c∈C. These are mutually orthogonal real two-dimensional
spaces inkerQℓ. Derivative orthogonality must be checked too: every forward difference multiplies
a character by its frequency multiplier, so the same root-of-unity Gram sum annihilates cross
terms between distinct frequencies. Thus for Hℓ = K0,n + (TℓQℓ)∗(TℓQℓ) the sum of these
spaces has dimension2R and maximum Rayleigh quotient at most4 sin2(πR/ℓ) ≤4π2R2/ℓ2.
Finite-dimensional min–max givesµ2R(Hℓ) ≤4π2R2/ℓ2. Taking R = ⌊ℓα⌋, 0 < α <1, for
sufficiently largeℓ, yields a growing cluster below4π2ℓ−2(1−α). Eigenvalue language is restricted
to this linear self-adjoint operator, not applied to a general nonlinear penalty.
Finally, for any linear changed measurement˜Qℓ, linear postconditioner Tℓ and positive
self-adjoint fine termVℓ, put
εℓ = ∥Tℓ ˜QℓA(ℓ)∥
∥A(ℓ)∥ , ν ℓ = ⟨A(ℓ),VℓA(ℓ)⟩
∥A(ℓ)∥2 .
Set ˜Hℓ = K0,n + (Tℓ ˜Qℓ)∗(Tℓ ˜Qℓ) + Vℓ. Expansion gives the exact repaired quotient
⟨A(ℓ), ˜HℓA(ℓ)⟩
∥A(ℓ)∥2 = λℓ + ε2
ℓ + νℓ.
A full-space constantc> 0 therefore requiresε2
ℓ+νℓ ≥c−λℓ at every scale, hencelim infℓ→∞(ε2
ℓ+
νℓ) ≥c. On the single witness line, uniform coercivity is equivalent toinfℓ≥2(λℓ+ε2
ℓ+νℓ) >0; this
3

isnotfull-spacesufficiency. Inparticularif ˜Qℓ = Qℓ+Rℓ, Tℓ = ℓ(d−2)/2Iandηℓ = ∥RℓA(ℓ)∥/∥A(ℓ)∥,
then ε2
ℓ = ℓd−2η2
ℓ. In dimension four and withVℓ = 0, leakageo(ℓ−1) cannot even repair this
line. The liminf, real-exponent, spectral multiplicity and witness-line equivalence are analytic
statements. The older exact kernel, norm-form energy, finite budget and dimension-four factorized
no-go have their own preserved formal source and reproductions, separately anchored below.
4 A constructed low band
For a nonnegative integerR with 2R <n, letΛR = {−R,...,R }d and B = |ΛR|= (2R+ 1)d.
Define
χk(x) = exp(2πi k·x/n), f a =
∑
k∈ΛR
akχk, S R = {Ejfa : a∈CΛR}⊂ En.
Lemma 4.1. The real subspaceSR has dimension2B, and for everyA∈SR,
⟨A,K0,nA⟩≤ bR(n)∥A∥2, b R(n) = 4π2dR2
n2 . (4)
Proof. For k,ℓ ∈ΛR, the product root-of-unity sum is∑
xχk(x)χℓ(x) = nd1k=ℓ. The no-alias
condition ensures that coordinate differences, of absolute value at most2R < n, cannot be
nonzero multiples ofn. Thus synthesis is injective and its complex image has dimensionB.
As a real space that image has dimension2B; applying the real-linear injectionEj preserves
dimension. The factor two represents independent real and imaginary coefficients stored in two
real internal coordinates, not two copies of a real scalar band.
For completeness, energy orthogonality is needed as well as mass orthogonality. For eachi,
Difa =
∑
k
ak
(
e2πiki/n −1
)
χk.
Applying the same Gram sum to these derivative amplitudes gives
∥Ejfa∥2 = nd∑
k
|ak|2,
⟨Ejfa,K0,nEjfa⟩= nd∑
k
|ak|2 ∑
i
|e2πiki/n −1|2.
Since |eit −1|≤| t|and |ki|≤ R, each sum of multipliers is at most4π2dR2/n2. This proves the
bound for every member of the constructed image, not only its individual generators.
5 The finite information budget
Let F be a finite-dimensional real vector space, C : En → F a linear measurement and
V : En →En a linear operator. No symmetry or positivity ofV is needed. LetΦ : F →R be
any function withΦ(0) = 0.
Theorem 5.1. If c>b R(n) and
c∥A∥2 ≤⟨A,K0,nA⟩+ Φ(CA) + ⟨A,VA ⟩ for all A∈En, (5)
then 2(2R+ 1)d ≤dim F + rankV.
4

Proof. If the budget is smaller thandim SR, restrict the map (C,V ) to SR. Its image has
dimension at mostdim F + rank V. Rank-nullity yields a nonzeroA∈SR with CA = VA = 0.
Equation (5) and Lemma 4.1 implyc∥A∥2 ≤bR(n)∥A∥2, a contradiction.
The codomain dimension is a conservative measurement budget. We do not label this formal
endpoint as a sharper theorem withrank C in its place. No regularity, sign, polynomial form or
growth restriction onΦ enters.
Proposition 5.2. If P : En →En is linear,c>b R(n) and dim F + rank P <2(2R+ 1)d, the
inequality
c∥A∥2 ≤⟨A,K0,nA⟩+ Φ(CA) ( A∈kerP)
is false.
Proof. Apply the same rank-nullity argument to(C,P)|SR. Its nonzero kernel vector belongs to
the stipulated sector as well as the unobserved band.
For example,d = 4,n = 16,R = 1 gives dimension162 and bR(n) = π2/16 < 1. Twelve
measurement coordinates and a repair of rank at most149 cannot yield(5) with c= 1. This
illustrates a necessary budget, not the programme’s chosen target constant.
6 Uniform refinement and sector exclusion
Fix a positive integerN′ and put nL = ( L+ 1)N′ for nonnegative integers L. The finite-
dimensional spaceF is fixed. Allow arbitrary families of linear mapsCL : EnL →F, arbitrary
functions ΦL : F →R with ΦL(0) = 0, and linear mapsVL : EnL →EnL with rank VL ≤r for
one fixed nonnegative integerr.
Theorem 6.1. There is noc> 0 for which (5) holds for everyL and everyA∈EnL with these
families. Likewise, for linearPL of rank at mostr, there is no positive uniformc for the sector
estimates of Proposition 5.2 on allker PL.
Proof. Set M = dim F and R = M + r+ 1. Since d ≥1, 2(2R+ 1)d > M+ r. Choose L
so large that2R < nL and bR(nL) < c. Here is a fully finite choice argument, without an
assumed limit theorem: witha= 4π2dR2, take an integerL> max{2R,a/c, 1}. Since N′≥1,
nL ≥L+ 1 > L >1, anda < cL≤cn2
L. Theorem 5.1 now contradicts the rank bound. Use
Proposition 5.2 for the separate sector conclusion.
The constantsc,r precede the quantifier overL. Arbitrary rescalings ofCL preserve its fixed
codomain and do not escape the theorem. Removing harmonic or constant directions is covered
only when a concrete linear constraint describing the proposed sector has uniformly bounded
rank. A quotient or its norm is not silently identified with such a sector. Linearity is essential: if
nonlinear observations were allowed, the single real observationCL(A) = ∥A∥2, withΦL(y) = y
and VL = 0, would give the uniform lower boundc= 1 since K0,nL ⪰0. This counterexample
explains why finite-dimensional output alone is not the hypothesis.
5

7 Why dimension is not a sufficiency criterion
The following analytic statement is included to prevent the reverse inference from a necessary
rank budget. It is not a new Lean-verified endpoint here. The proof below is the classical
singular-Schur range condition [3, 4], expressed as boundedness below on each measurement fiber;
we claim no new general matrix criterion. LetE be a finite-dimensional real inner-product space,
H = H∗and B = H−cI. Fix linearC : E →F, and decomposeE = N ⊕W with N = kerC,
W = N⊥. In this decomposition write
B =
(
A D
D∗ G
)
.
Proposition 7.1. A finite real-valued functionΦ with Φ(0) = 0 can make⟨x,Bx⟩+ Φ(Cx) ≥0
for everyx if and only ifA⪰0 and ker A⊆kerD∗. In that event a quadratic penalty suffices.
Proof. Takingx∈N proves A⪰0. Forz∈ker Aand fixedw∈W, the value attz+ w contains
2t⟨z,Dw⟩, whileC(tz+ w) = Cw is fixed. Boundedness below for all realtforces this coefficient
to vanish.
Conversely,kerA⊆ker D∗implies D(W) ⊆ran A. Let A†be the inverse onran A and zero
on kerA. Completing the square gives
⟨n+ w,B(n+ w)⟩= ⟨n+ A†Dw,A(n+ A†Dw)⟩+ ⟨w,(G−D∗A†D)w⟩.
The restrictionC|W is injective; extend its inverse onC(W) to a linear mapT : F →W. The
quadratic functionΦ(y) = ⟨Ty, (D∗A†D−G)Ty⟩cancels the second term and vanishes at zero.
If F has a chosen Euclidean norm, a sufficiently large nonnegative multiple of∥y∥2 also suffices,
by finite-dimensional norm bounds.
For a concrete counterexample letH = diag(0,2), c = 1 and C(x,y) = x+ y. On kerC,
⟨x,(H−I)x⟩= 0, andC detects the negative eigendirection ofH−I. Nevertheless, on(t,1 −t)
the repaired form is1 −2t+ Φ(1), unbounded below for every finiteΦ(1). Kernel nonnegativity
and low-mode detection alone do not suffice; cross-coupling must be checked.
8 Operator scaling and the actual consumer
In the repository, the flat fixed-volume covariance endpoint usesK0 + aQ∗Q with the physical
counting ℓ2 norm and the same unscaled flat Hodge operator. More precisely, the declared
precision shell includes−Σ. Specializing every perturbation and its summable majorant to zero
and takinga> 0 gives the available certified coercivity lower boundmin(1,a)/CP, withCP >0
from the full-periodic block-Poincare estimate. This is not a claim that this value is optimal.
At fixed d,Nc,N′ the block codomain is fixed and finite. Inspection therefore identifies the
unscaled flat base route with the setting of Theorem 6.1, withΦL(y) = aL∥y∥2 and no fine repair.
Even allowing arbitrary scalaraL or rescalingQL does not yield a positive uniform full-space
constant. This is a source-level specialization in this text; no new Lean adapter to that consumer
is claimed. At the new source anchor below, the modulePhysicalGaugeFixedPrecision defines
flatGaugeFixedPrecisionCLM; its explicit-Poincare coercivity theorem is recorded by its full
name and specialization in the linked declaration map.
The inspected endpoint is explicitly fixed-volume. Its positive rate may depend onL,N′
and CP, so there is no contradiction. Nor does the obstruction exclude all possible uniform
6

Combes–Thomas arguments. Its locality radius and matrix-entry bounds also vary withL;
coercivity alone would not settle the rate. An interacting Hessian, a growing measurement
budget, a different sector norm or a physically rescaled operator must each be audited separately.
In particular, writingℓ= L+ 1 so thatnL = ℓN′, replacingK0 by ℓ2K0 changes the band
threshold exactly to4π2dR2/(N′)2. The proof above no longer drives it below every fixedc> 0.
This observation is an escape from this proof, not an established coercivity theorem for the
programme’s physical operator. No ultraviolet activity estimate, continuum limit, Wilson-Hessian
identification or Yang–Mills mass gap is obtained.
9 Formal evidence and publication context
The source-tree anchor for the new physical-band and uniform-rank results is
e31b428917aa767b4a1aad097db5cf92fb9cd23e.
The original factorized-kernel and repair development in Section 3 instead has the distinct tested
source anchor
7b25bfb39357406cf61880e3ac0428d7d1ba3449.
Its exact modules are not present in the new main tree merely because a reproduction supplement
is present there. The two full preserved focal runs at that older SHA agree in compiled object,
oracle log and source manifest; their six named reports use only the three standard axioms. The
reproduced factorized endpoint is dimension four. The general-dimensional witness calculation,
trigonometric closed form, spectral multiplicity, liminf and witness-line statements are analytic
here; they are not all silently included in that formalization claim. The external declaration map
keeps both anchors. The public source repository is THE-ERIKSSON-PROGRAMME on GitHub.
The corrected map isdeclaration-map.json and the preserved evidence isreproducibility/.
Exact source SHAs, not moving branch heads, identify the formal claims. The revised map and
manuscript have their own revision SHA in the accompanying package.
The geometric and Fourier modules are ordinary proof dependencies, not assumptions about
a newly supplied band. Each development stage has complete same-source fresh-clone Colab
evidence. For the uniform endpoints the tested source is
17ca395d4e9de992b1c575454a112da9e6f97e86.
Its two runs agree in compiled object, raw oracle log and source-manifest hashes. The standalone
budget lemma uses propext, Quot.sound; the other four uniform-module reports also use
Classical.choice. No extra axiom is reported. Actual-log acceptance and three real-field
rejection tests pass under normal and optimized Python. These tests concern evidence handling,
not mathematical independence.
Short labels and an external declaration map replace long wrapped Lean names in this
manuscript. The companion source map records exact names, source SHAs, and evidence
directories. Reproduction commands remain in the existing copyable notebooks rather than
being split into misleading line fragments. The fixed-map Schur criterion, its counterexample
calculation and consumer specialization above are analytic or source-inspection arguments; the
whole manuscript is not described as machine checked.
7

Model assessments and review context
This text was prepared with the Codex agent in the author’s ongoing research chat. The exact
served model identifier is not exposed in this preparation record; a different named reviewer or
reasoning setting is not inferred. The agent had the prior manuscript objections, source audits
and reproduction records, and was not blind to the programme. An earlier eight-page PDF
(SHA256 recorded in the accompanying report) was assessed once by a subagent configured as
gpt-6-astra, with express author authorization. Actual backend identity and reasoning setting
were not exposed. The reviewer saw the exact PDF and prior context; the workflow used the
same chat, account and provider and was not blind or organizationally independent. Its complete
report and six objections are preserved with this revision. This revised artifact incorporates
scope and attribution corrections; the earlier assessment does not apply to its new bytes. No
numerical score, independent human peer review or editorial acceptance is claimed. The reviewer
did not rebuild Lean or independently audit the complete evidence/dependency closure; formal
reproduction statements above describe the supplied records. Fresh runs of the same workflow
are reproducibility checks, not independent scientific assessments. Previous version scores, if any,
do not transfer to a revised artifact.
Lluis Eriksson is both the author and operator of AIRR.science. Any later founder-author
editorial decision must be recorded separately from model assessments and from independent
review. The existing record [1] is an author-authorized historical import, not assessed under
the current AIRR screening. This preparation does not change its public version or publication
status. Code and manuscript licensing must be recorded separately; no new license grant for the
historical PDF is inferred.
References
[1] L. Eriksson,Exact-Kernel Fourier Families Obstruct Every Penalty Factored Through a
Block Map in a Flat Lattice Gauge Form, ai.viXra 2608.0015v1 (2026), AIRR
ARR-2026-7EPM3V3DP796BBRR v1.
https://airr.science/papers/ARR-2026-7EPM3V3DP796BBRR/versions/v1/. Historical
import, not peer reviewed or assessed by AIRR; checked 30 October 2026.
[2] J. Dodziuk,Finite-difference approach to the Hodge theory of harmonic forms, American
Journal of Mathematics98 (1976), 79–104.https://doi.org/10.2307/2373615.
Institutional source: https://academicworks.cuny.edu/gc_pubs/180/.
[3] A. Albert,Conditions for Positive and Nonnegative Definiteness in Terms of Pseudoinverses,
SIAM Journal on Applied Mathematics17 (1969), 434–440.
https://doi.org/10.1137/0117041.
[4] D. Carlson, E. Haynsworth and T. Markham,A Generalization of the Schur Complement by
Means of the Moore–Penrose Inverse, SIAM Journal on Applied Mathematics26 (1974),
169–175. https://doi.org/10.1137/0126013.
[5] J. Dimock,Covariant Axial Gauge, arXiv:1410.2798v2 (2014).
https://arxiv.org/abs/1410.2798v2.
8
