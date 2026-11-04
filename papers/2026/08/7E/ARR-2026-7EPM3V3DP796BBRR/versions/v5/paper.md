# Integrated v5 Working paper

This citable Working paper has not been admitted to the AIRR accepted collection. The unrestricted critical rectangular construction and interacting/continuum Yang-Mills gap remain open. Mechanism-specific counterexamples do not refute every rectangular construction.

## Model assessments and review context

The complete first assessment of this exact PDF is [SCORED-ASSESSMENT.md](SCORED-ASSESSMENT.md): 6/10, preparing-agent self-assessment, with all eight material objections retained. The assessor participated extensively in preparation. The system describes GPT-6-based Codex; actual served backend identifier and reasoning setting are unexposed. There is no claimed independent/blind/external or human peer review. Earlier version scores and Sonnet reports are not inherited. This qualitative judgment is not a weighted average or an AIRR screening result.

Canonical PDF: 33 pages, 503478 bytes, SHA256 69d802bfea8f8f23bfe6aba03cdc4835feac777e024c939040c7f099a11462c8. The PDF was frozen before deposit; preparation-time wording inside it is not the later deposit/publication record.

Manuscript TeX source commit: d199a0977eca581b2e0d00c1afd84233a8db361d. Exact PDF/review/reproducibility archive commit: 5c33368d51448cfa04b6adf42e313305a065dfa2 in [THE-ERIKSSON-PROGRAMME](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/5c33368d51448cfa04b6adf42e313305a065dfa2/papers/flat-coarse-rank/integrated-revision).

The [reproducibility ZIP](https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/blob/5c33368d51448cfa04b6adf42e313305a065dfa2/papers/flat-coarse-rank/integrated-revision/integrated-revision125-reproducibility.zip) has SHA256 b65748bcbe6764e0527baa1c9c1c42e8d4fecd735ae367790f03119ebae8a2ca. Its code retains its repository license; manuscript CC BY 4.0 and metadata CC0 do not relicense external code.

Native receipt SUB-254C871C2EB3099F was received 2026-11-04T17:14:57+00:00, scan clean, eligible. Exact-version publication permission was recorded 2026-11-04T17:19:03+00:00 (CC BY 4.0 / metadata CC0). Founder-author conflict declaration recorded 2026-11-04T17:20:27+00:00. These are distinct from acceptance. Private credentials, grant secrets and consent records are not part of this public package.

## Extracted manuscript text

        Coarse information and finite rank obstructions
                     for flat lattice Hodge forms
                                            Lluis Eriksson

                  4 November 2026 — integrated candidate, not deposited


                                               Abstract
         On a finite periodic lattice with unit spacing, a flat Hodge form cannot have a positive
     coercivity constant uniform under refinement when supplemented only by linear observations
     in a fixed finite-dimensional real space and linear fine-space repairs of uniformly bounded
     rank. We construct a real physical Fourier band, prove a necessary information budget
     and a separate bounded-rank sector obstruction, and explain why a classical singular-Schur
     condition prevents reversing that budget. Constructed derivative repairs and differentiable
     observations with locally upper-quadratic penalties admit tangent obstructions, including an
     exact regular nonlinear-sector argument. For nonnegative weights, a subquadratic directional
     spatial mean forces output-rank divergence. For signed weights, the spatial mean of the
     pointwise positive part gives a sufficient condition; ordinary signed means do not, as an actual
     fixed-output counterexample with every mean zero shows. An attributed classical square
     cancellation delimits the sufficient criterion; a finite-sum extension covering every eligible
     pair is displayed analytically. A full volume coexact packet also gives a quantitative rank
     budget under spatial means of the pointwise positive total coefficient on its two occupied
     field components. A derived integer cutoff yields positive output rank density on every
     sufficiently large lattice, while exact trace averaging improves a sufficient low frequency
     constant. Formal endpoints are separately pinned, and additional analytic arguments are
     identified. These are finite flat statements, with no interacting or continuum Yang–Mills
     mass-gap claim or new general spectral-principle claim. The integrated continuation also
     proves a critical inverse-moment sufficient condition for global spectral observations, together
     with limits on spatial localization. Rectangular means have a general upper bound with
     exponent d/4 and the target exponent d/2 for an explicitly restricted scaled-cube class. Two
     constructive counterexamples exclude a single-global-threshold algorithm and a universal
     exact cube decomposition, while preserving successful rectangular partitions for those same
     profiles. The general critical rectangular question remains open.


1    Purpose and relation to the existing record
This text consolidates a continuation of the exact-kernel obstruction in [1]. That paper exhibits
fields in the kernel of a particular line-integral block map. Changing the map can remove a
particular witness. Here the obstruction depends instead on the amount of coarse information: a
whole low-energy subspace is too large to be seen by a fixed-dimensional measurement together
with a bounded-rank repair. The map need not factor through the original block variable, be
local, or obey a norm bound; it is real-linear in the unrestricted-penalty results. The penalty
applied to its output may be nonlinear. Later sections treat differentiable observations with a



                                                    1
locally upper-quadratic penalty and exact nonlinear regular sectors. The restricted-sector result
is proved separately and does not follow merely from failure of an estimate on the full space.
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
from a torus with small spacing, equivalently a large unit-spacing volume. Our unrestricted, unit-
spacing flat form is not identified with every constrained fluctuation form in those constructions.
This negative diagnostic does not refute their gauge-fixed estimates or establish an interacting
bound.


2    Spaces and the actual flat form
Fix integers d ≥ 1, n ≥ 1 and Nc ≥ 2. Set Xn = (Z/nZ)d and m = Nc2 − 1. The real one-cochain
space is
                                                                               d
                                                                             X X
              En = {A : Xn × {1, . . . , d} −→ Rm },               ∥A∥2 =              ∥Ai (x)∥2 .
                                                                            x∈Xn i=1

The internal coordinates are those of the repository’s Euclidean Lie-coordinate model. No
identification with a matrix Lie algebra is required here. For positive unordered plaquettes i < k,
define

                      (dA)ik (x) = Ak (x + ei ) − Ak (x) − Ai (x + ek ) + Ai (x),
                                        X                          
                        (δA)(x) =            Ai (x) − Ai (x − ei ) .
                                         i

The flat operator K0,n is the actual repository Hodge operator, with

                                        ⟨A, K0,n A⟩ = ∥dA∥2 + ∥δA∥2 .                                          (1)

The plaquette norm sums each pair once. All differences have unit spacing; there is no hidden n2
or block-side squared factor.
    Choose a direction j and two distinct internal unit coordinates u, v. They exist since m ≥ 3.
For f : Xn → C, put                      (
                                          (ℜf (x))u + (ℑf (x))v, i = j,
                          (Ej f )i (x) =
                                          0,                     i ̸= j.
This is a real-linear injection and ∥Ej f ∥2 =                   2
                                                        x |f (x)| . Writing Di f (x) = f (x + ei ) − f (x), the
                                                    P

actual curl and divergence give
                               XX                       X                              XX
        ⟨Ej f, K0,n Ej f ⟩ =            |Di f (x)|2 +       |f (x) − f (x − ej )|2 =           |Di f (x)|2 .   (2)
                               i̸=j x                   x                              i   x


                                                        2
The last equality is finite translation invariance. The exclusive two plaquette incidences and the
divergence term account for every direction exactly once, with no extra factor two.


3    The original block kernel and its repair budget
We retain the principal results of the historical paper [1] before explaining the new information-
budget obstruction. The original Appendix A (an even-block square-wave witness with quotient
8/ℓ) remains in the preserved v1; it is not reproduced here. Use positive integers ℓ, N ′ , set
n = ℓN ′ , and for a coarse site y put By = {ℓy + r : 0 ≤ ri < ℓ}. The original line-integral map is
                                                        ℓ−1
                                (Qℓ A)i (y) = ℓ−d
                                                      X X
                                                                    Ai (x + kei ).
                                                     x∈By k=0

                                                           2 > 0,
                                                 i ∥vi ∥
                                             P
For a constant field Ai (x) = vi and S =

                          ∥A∥2 = ℓd (N ′ )d S,       ∥ℓσ Qℓ A∥2 = ℓ2σ+2 (N ′ )d S.

A uniform Poincare estimate must therefore have σ ≥ (d − 2)/2 if it is to survive this sector.
Equality alone makes the two powers identical. Larger exponents pass this necessary test too;
neither equality nor the inequality is a sufficient full-space condition. This follows by cancelling
(N ′ )d S to obtain ℓd−2−2σ ≤ CP . The real-exponent comparison is analytic here.
     For d ≥ 2 choose distinct directions p, q and the real isometry ι(z) = (ℜz)u + (ℑz)v from
Section 2. For ℓ ≥ 2 define
                   (ℓ)
                  Ai (x) = 1i=p ι e2πixq /ℓ ,          λℓ = |e2πi/ℓ − 1|2 = 4 sin2 (π/ℓ).
                                             


The character is well defined on XℓN ′ . The sum over the q-offset in every block is a nontrivial
root-of-unity sum and vanishes. Shifts in the line direction p do not change the profile. Hence

           Qℓ A(ℓ) = 0,    δA(ℓ) = 0,    ∥A(ℓ) ∥2 = (ℓN ′ )d ,         ⟨A(ℓ) , K0,n A(ℓ) ⟩ = (ℓN ′ )d λℓ .   (3)

Only the plaquette pair containing p, q contributes to the curl energy; its difference has constant
squared norm λℓ at every site. This also explains the exact energy in (3), including periodic
boundary jumps.
   Consequently any scale-wise estimate

                     ∥A∥2 ≤ CP (ℓ) ⟨A, K0,n A⟩ + Ψℓ (Qℓ A) ,
                                                                        
                                                                                Ψℓ (0) = 0,

forces CP (ℓ) ≥ λ−1      2     2
                   ℓ ≥ ℓ /(4π ). No fixed CP > 0 before all block sides can work. This includes
Ψℓ (y) = ∥Tℓ y∥2 for arbitrary linear postconditioners, and all critical or faster scalar rescalings.
There is no regularity or sign assumption on the scalar function Ψℓ .
    The original spectral strengthening is retained analytically. For 1 ≤ r ≤ R ≤ ⌊(ℓ − 1)/2⌋,
replace the profile by ι(ce2πirxq /ℓ ), c ∈ C. These are mutually orthogonal real two-dimensional
spaces in ker Qℓ . Derivative orthogonality must be checked too: every forward difference multiplies
a character by its frequency multiplier, so the same root-of-unity Gram sum annihilates cross
terms between distinct frequencies. Thus for Hℓ = K0,n + (Tℓ Qℓ )∗ (Tℓ Qℓ ) the sum of these
spaces has dimension 2R and maximum Rayleigh quotient at most 4 sin2 (πR/ℓ) ≤ 4π 2 R2 /ℓ2 .
Finite-dimensional min–max gives µ2R (Hℓ ) ≤ 4π 2 R2 /ℓ2 . Taking R = ⌊ℓα ⌋, 0 < α < 1, for

                                                      3
sufficiently large ℓ, yields a growing cluster below 4π 2 ℓ−2(1−α) . Eigenvalue language is restricted
to this linear self-adjoint operator, not applied to a general nonlinear penalty.
    Finally, for any linear changed measurement Q      e ℓ , linear postconditioner Tℓ and positive
self-adjoint fine term Vℓ , put
                                         e ℓ A(ℓ) ∥
                                     ∥Tℓ Q                               ⟨A(ℓ) , Vℓ A(ℓ) ⟩
                              εℓ =                  ,           νℓ =                       .
                                       ∥A(ℓ) ∥                             ∥A(ℓ) ∥2
Set H                e ℓ )∗ (Tℓ Q
    e ℓ = K0,n + (Tℓ Q          e ℓ ) + Vℓ . Expansion gives the exact repaired quotient

                                      ⟨A(ℓ) , H
                                              e ℓ A(ℓ) ⟩
                                                         = λℓ + ε2ℓ + νℓ .
                                         ∥A(ℓ) ∥2
A full-space constant c > 0 therefore requires ε2ℓ +νℓ ≥ c−λℓ at every scale, hence lim inf ℓ→∞ (ε2ℓ +
νℓ ) ≥ c. On the single witness line, uniform coercivity is equivalent to inf ℓ≥2 (λℓ +ε2ℓ +νℓ ) > 0; this
                                                e ℓ = Qℓ +Rℓ , Tℓ = ℓ(d−2)/2 I and ηℓ = ∥Rℓ A(ℓ) ∥/∥A(ℓ) ∥,
is not full-space sufficiency. In particular if Q
then ε2ℓ = ℓd−2 ηℓ2 . In dimension four and with Vℓ = 0, leakage o(ℓ−1 ) cannot even repair this
line. The liminf, real-exponent, spectral multiplicity and witness-line equivalence are analytic
statements. The older exact kernel, norm-form energy, finite budget and dimension-four factorized
no-go have their own preserved formal source and reproductions, separately anchored below.


4    A constructed low band
For a nonnegative integer R with 2R < n, let ΛR = {−R, . . . , R}d and B = |ΛR | = (2R + 1)d .
Define
                                                     X
        χk (x) = exp(2πi k · x/n),         fa =             ak χk ,            SR = {Ej fa : a ∈ CΛR } ⊂ En .
                                                     k∈ΛR

Lemma 4.1. The real subspace SR has dimension 2B, and for every A ∈ SR ,
                                                                                     4π 2 dR2
                          ⟨A, K0,n A⟩ ≤ bR (n)∥A∥2 ,                     bR (n) =             .                 (4)
                                                                                        n2
Proof. For k, ℓ ∈ ΛR , the product root-of-unity sum is x χk (x)χℓ (x) = nd 1k=ℓ . The no-alias
                                                                           P

condition ensures that coordinate differences, of absolute value at most 2R < n, cannot be
nonzero multiples of n. Thus synthesis is injective and its complex image has dimension B.
As a real space that image has dimension 2B; applying the real-linear injection Ej preserves
dimension. The factor two represents independent real and imaginary coefficients stored in two
real internal coordinates, not two copies of a real scalar band.
    For completeness, energy orthogonality is needed as well as mass orthogonality. For each i,
                                                X
                                                      ak e2πiki /n − 1 χk .
                                                                               
                                     Di fa =
                                                 k
Applying the same Gram sum to these derivative amplitudes gives
                                                            X
                                     ∥Ej fa ∥2 = nd             |ak |2 ,
                                                            k
                                                            X            X
                                                        d
                          ⟨Ej fa , K0,n Ej fa ⟩ = n             |ak |2         |e2πiki /n − 1|2 .
                                                            k              i

Since |eit − 1| ≤ |t| and |ki | ≤ R, each sum of multipliers is at most 4π 2 dR2 /n2 . This proves the
bound for every member of the constructed image, not only its individual generators.

                                                            4
5     The finite information budget
Let F be a finite-dimensional real vector space, C : En → F a linear measurement and
V : En → En a linear operator. No symmetry or positivity of V is needed. Let Φ : F → R be
any function with Φ(0) = 0.

Theorem 5.1. If c > bR (n) and

                   c∥A∥2 ≤ ⟨A, K0,n A⟩ + Φ(CA) + ⟨A, V A⟩      for all A ∈ En ,                (5)

then 2(2R + 1)d ≤ dim F + rank V .

Proof. If the budget is smaller than dim SR , restrict the map (C, V ) to SR . Its image has
dimension at most dim F + rank V . Rank-nullity yields a nonzero A ∈ SR with CA = V A = 0.
Equation (5) and Lemma 4.1 imply c∥A∥2 ≤ bR (n)∥A∥2 , a contradiction.

   The codomain dimension is a conservative measurement budget. We do not label this formal
endpoint as a sharper theorem with rank C in its place. No regularity, sign, polynomial form or
growth restriction on Φ enters.

Proposition 5.2. If P : En → En is linear, c > bR (n) and dim F + rank P < 2(2R + 1)d , the
inequality
                      c∥A∥2 ≤ ⟨A, K0,n A⟩ + Φ(CA)       (A ∈ ker P )
is false.

Proof. Apply the same rank-nullity argument to (C, P )|SR . Its nonzero kernel vector belongs to
the stipulated sector as well as the unobserved band.

    For example, d = 4, n = 16, R = 1 gives dimension 162 and bR (n) = π 2 /16 < 1. Twelve
measurement coordinates and a repair of rank at most 149 cannot yield (5) with c = 1. This
illustrates a necessary budget, not the programme’s chosen target constant.


6     Uniform refinement and sector exclusion
Fix a positive integer N ′ and put nL = (L + 1)N ′ for nonnegative integers L. The finite-
dimensional space F is fixed. Allow arbitrary families of linear maps CL : EnL → F , arbitrary
functions ΦL : F → R with ΦL (0) = 0, and linear maps VL : EnL → EnL with rank VL ≤ r for
one fixed nonnegative integer r.

Theorem 6.1. There is no c > 0 for which (5) holds for every L and every A ∈ EnL with these
families. Likewise, for linear PL of rank at most r, there is no positive uniform c for the sector
estimates of Proposition 5.2 on all ker PL .

Proof. Set M = dim F and R = M + r + 1. Since d ≥ 1, 2(2R + 1)d > M + r. Choose L
so large that 2R < nL and bR (nL ) < c. Here is a fully finite choice argument, without an
assumed limit theorem: with a = 4π 2 dR2 , take an integer L > max{2R, a/c, 1}. Since N ′ ≥ 1,
nL ≥ L + 1 > L > 1, and a < cL ≤ cn2L . Theorem 5.1 now contradicts the rank bound. Use
Proposition 5.2 for the separate sector conclusion.



                                                5
   The constants c, r precede the quantifier over L. Arbitrary rescalings of CL preserve its fixed
codomain and do not escape the theorem. Removing harmonic or constant directions is covered
only when a concrete linear constraint describing the proposed sector has uniformly bounded
rank. A quotient or its norm is not silently identified with such a sector. Linearity is essential: if
nonlinear observations were allowed, the single real observation CL (A) = ∥A∥2 , with ΦL (y) = y
and VL = 0, would give the uniform lower bound c = 1 since K0,nL ⪰ 0. This counterexample
explains why finite-dimensional output alone is not the hypothesis.


7    Constructed derivative repairs and tangent observations
The bounded-rank obstruction does not exhaust the available repairs. For the actual component-
wise forward gradient GA = (Dk Ai )x,i,k , finite periodic summation and cancellation of the mixed
differences give
                                      ∥GA∥2 = ⟨A, K0,n A⟩.
This is an identity on the whole cochain space, with unordered plaquettes counted once; it is
not an assumed comparison on a supplied band. Let W be the diagonal multiplication by real
weights wx,i,k , and construct Vw = G ∗ W G. If wx,i,k ≤ M and M ≥ 0, then
                                     X
                       ⟨A, Vw A⟩ =           wx,i,k ∥(Dk Ai )(x)∥2 ≤ M ⟨A, K0,n A⟩.                (6)
                                     x,i,k

A lower bound on the weights is unnecessary for this upper estimate. Consequently the constructed
Fourier band satisfies

                qw (A) := ⟨A, (K0,n + Vw )A⟩ ≤ (1 + M )bR (n)∥A∥2              (A ∈ SR ).

These operator identities and inequalities are formally proved in the separately pinned source
reported below.

Theorem 7.1 (Finite-dimensional tangent obstruction). Let E be a finite-dimensional real
inner-product space, F a finite-dimensional real normed space, and S ⊆ E a linear subspace
with dim S > dim F . Let q : E → R satisfy q(x) ≤ b∥x∥2 on S. Suppose C : E → F is Fréchet
differentiable at zero, C(0) = 0, and for some δ > 0 and finite K ∈ R,

                                   Φ(y) ≤ K∥y∥2             (∥y∥ < δ).                             (7)

If c > b, the full-space estimate c∥x∥2 ≤ q(x) + Φ(C(x)) is impossible.

Proof. Put L = DC(0). Rank-nullity applied to the actual restriction L|S produces v ∈ S ∩ ker L,
v ̸= 0. Differentiability gives ∥C(tv)∥/∥tv∥ → 0 as nonzero real t → 0. For small such t, (7)
applies and the proposed bound implies

                                                       ∥C(tv)∥2
                                             c≤b+K              .
                                                        ∥tv∥2

Taking the limit gives c ≤ b, a contradiction. The kernel vector and the remainder limit are
derived, not introduced as hypotheses of the theorem.



                                                      6
    The three focal Lean endpoints include this theorem, its remainder lemma and the actual
physical specialization with threshold (1 + M )bR (n). The proof does not require an explicit
assumption Φ(0) = 0. A local-ball version is also valid by the same shrinking-ray argument,
while the original formal endpoint above is stated on the full space. The later local kernel and
average-weight endpoint in Section 9 has its own separately reproduced proof.
    This result trades hypotheses. The global linearity of C is replaced by differentiability at
zero, while an arbitrary zero-vanishing penalty is replaced by genuine quadratic upper control.
Merely asking C and Φ to be C 1 with zero derivatives at zero is insufficient: for 1 < α < 2,

                   C(x) = ∥x∥α ,        Φ(y) = |y|2/α     =⇒      Φ(C(x)) = ∥x∥2 .

Both derivatives at zero vanish. Off zero, ∥DC(x)∥ = α∥x∥α−1 and |Φ′ (y)| = (2/α)|y|2/α−1 tend
to zero, so both maps are indeed C 1 there and at zero. But Φ(y)/|y|2 = |y|2/α−2 is unbounded
above near zero. On the actual lattice, setting w = 0 gives a uniform lower bound with c = 1
because K0,n ⪰ 0. This is an exact counterexample, not a numerical test.


8    Exact nonlinear regular sectors
The next theorem is an analytic consequence of rank-nullity and the classical implicit function
theorem. The actual curve construction and local-energy obstruction now have separately pinned
formal proofs, identified in the evidence section. The pinned formal library supplies an implicit
parametrization with derivative the inclusion of the derivative kernel [6]; we construct and use
that parametrization explicitly below rather than assuming the curve needed for the conclusion.
Theorem 8.1 (Regular-sector tangent obstruction). Let E be a finite-dimensional real inner-
product space and F, G finite-dimensional real normed spaces. Let T : E → E be linear and
set q(x) = ⟨x, T x⟩. Suppose a linear subspace S satisfies q(v) ≤ b∥v∥2 on S and dim S >
dim F + dim G. Let C be differentiable at zero with C(0) = 0 and let Φ satisfy (7). Let
P : E → G be C 1 on a neighborhood of zero with P (0) = 0 and A = DP (0) surjective. For every
c > b and every r > 0, there is no estimate

                        c∥x∥2 ≤ q(x) + Φ(C(x))
                                                                               
                                                         P (x) = 0, ∥x∥ < r .                     (8)

Proof. Put L = DC(0). Apply rank-nullity to (L, A)|S : S → F × G to obtain v ∈ S, v ̸= 0, with
Lv = Av = 0. Choose a linear complement W of H = ker A. Surjectivity implies A|W : W → G
is bijective. Apply the implicit function theorem to (u, w) 7→ P (u + w) at (0, 0) ∈ H × W . It
produces a C 1 map ψ near zero in H with

                  ψ(0) = 0,    P (u + ψ(u)) = 0,       Dψ(0) = −(A|W )−1 A|H = 0.

Thus γ(t) = tv + ψ(tv) lies in the exact sector for small real t, γ(0) = 0, and γ(t) = tv + e(t) with
∥e(t)∥ = o(|t|). In particular ∥γ(t)∥/|t| → ∥v∥ > 0, so the nonzero points of this curve eventually
lie in the stipulated ball.
     The curve need not remain in S. This is why the quadratic form assumption is used: direct
expansion gives

                    q(γ(t)) = t2 q(v) + t⟨v, T e(t)⟩ + t⟨e(t), T v⟩ + ⟨e(t), T e(t)⟩.

Since T is bounded in finite dimension, division by t2 gives q(γ(t))/t2 → q(v). Differentiability
of C and Lv = 0 give C(γ(t)) = Le(t) + o(|t|) = o(|t|). Apply the assumed bound along this

                                                   7
exact curve and use (7). Division by t2 and the limit yield c∥v∥2 ≤ q(v) ≤ b∥v∥2 , contrary to
c > b.

     Unlike the preceding full-space result, an arbitrary energy with an upper bound only on S
would not justify this proof: the constructed exact-sector curve generally leaves S. The displayed
expansion supplies the missing comparison for the actual quadratic energy.
     A concrete curved example also shows why an exact vector in S is not the right object. Write
E = R4 with coordinates (u1 , u2 , y, z), put P (u, y, z) = z − ∥u∥2 , C(u, y, z) = y, Φ(y) = y 2 ,
S = {z = 0} and q(u, y, z) = z 2 . Then DP (0) is surjective and dim S = 3 > 1 + 1. But
S ∩ ker C ∩ P −1 (0) = {0}: the linear band contains no nonzero exact-sector unseen vector.
Nevertheless γ(t) = (t, 0, 0, t2 ) lies in the exact sector and has repaired Rayleigh quotient
t2 /(1 + t2 ) → 0. The implicit-curve argument is genuinely needed.
     Nor can quadratic q in Theorem 8.1 be replaced merely by a C 1 energy stationary at zero
with the same upper bound on S. With the same E, C, Φ, S, instead put

                         P (u, y, z) = z − ∥u∥4/3 ,    e(u, y, z) = |z|3/2 .

Both maps are C 1 , DP (0)(u, y, z) = z is surjective, De(0) = 0, and e = 0 on S, so b = 0. On the
exact sector,
                e(x) + Φ(C(x)) = ∥u∥2 + y 2 ,          ∥x∥2 = ∥u∥2 + y 2 + ∥u∥8/3 .
For ∥x∥ < 1, ∥u∥8/3 ≤ ∥u∥2 , so the local sector bound with c = 1/2 > b holds. Differentiability
of the norm powers at zero follows from their exponents being greater than one; their gradients
off zero tend to zero. This exact counterexample refutes a proposed C 1 -energy weakening, while
the actual quadratic Hodge/repair energy retains the required expansion.
    The regularity condition cannot simply be dropped. Take E = R3 , F = G = R, C = 0, Φ = 0,
T = 0, S = E, and P (x) = ∥x∥2 . Then P is smooth, DP (0) = 0, and the strict dimension budget
holds, but P −1 (0) = {0} and the estimate with c = 1 is vacuous on the sector. This refutes the
proposal to replace submersion by bounded derivative rank. It does not refute Theorem 8.1,
because DP (0) is not surjective. Critical constraint maps require a separate analysis.

Proposition 8.2 (Uniform physical consequence). Let nL → ∞ with fixed d, Nc , and let F, G
have fixed finite dimensions. For each L, allow its own CL , PL , ΦL satisfying the hypotheses
of Theorem 8.1. Let qL be the actual flat Hodge form plus the constructed weighted derivative
repair with weights wL ≤ ML , ML ≥ 0, and ML /n2L → 0. Even on the exact sectors PL = 0 and
arbitrarily small balls of positive radius rL , no positive uniform coercivity constant exists.

Proof. Choose a fixed integer R with 2(2R + 1)d > dim F + dim G. For all large L, 2R < nL and
the constructed band obeys qL ≤ (1 + ML )bR (nL )∥ · ∥2 . Its coefficient tends to zero. For any
proposed c > 0, choose one such L with this coefficient below c and apply Theorem 8.1 at that
fixed lattice. The curve is shrunk only after choosing L: no uniform implicit-function radius,
inverse-derivative norm, penalty constant or rL is required.

   These are finite unit-spacing obstructions for regular nonlinear sectors, not identifications of
a physical gauge-fixed domain or a quotient norm.




                                                 8
9    Directional mean weights and local nonlinear observations
Pointwise bounds on a derivative repair are stronger than the following actual spatial-mean
condition. Fix d ≥ 2, Nc ≥ 2, and distinct directions i, j. For nonnegative componentwise
weights wn (k, (x, l)), put

                                                                                 bij (n) = n−d
                         X                                                                       X
Qn (A) = ⟨A, K0,n A⟩ +           wn (k, (x, l))∥Al (x + ek ) − Al (x)∥2 ,                              wn (i, (x, j)).
                         x,k,l                                                                   x

The repair is the actual G∗ Wn G of the componentwise forward gradient. In particular Qn ≥ 0;
signed weights are not included in this section. Let Dn = ker δ be the actual flat divergence-free
space.

Theorem 9.1 (Local nonlinear average-weight obstruction). For each n ≥ 1, let Fn be a finite-
dimensional real normed space, Cn : En → Fn be Fréchet differentiable at zero with Cn (0) = 0,
and let Φn : Fn → R satisfy

                             Φn (y) ≤ Kn ∥y∥2         (∥y∥ < δn ),          δn > 0.

Suppose one fixed c > 0 and positive radii rn satisfy

                      c∥A∥2 ≤ Qn (A) + Φn (Cn (A))             (A ∈ Dn , ∥A∥ < rn ).                              (9)

For every integer 0 ≤ R < n,
                                                    R
                                                    X                         8π 2 (1 + bij (n))R3
             c(2R − dim Fn ) ≤ 2(1 + bij (n))             |e2πis/n − 1|2 ≤                         .             (10)
                                                    s=1
                                                                                       n2

Consequently, if (1 + bij (n))/n2 → 0, then dim Fn → ∞. No uniform bound on Kn , δn−1 or rn−1
is required.

Proof. Write Ln = DCn (0). If v ∈ Dn ∩ ker Ln , differentiability gives Cn (tv) = o(|t|). For all
sufficiently small nonzero t, both the local coercivity and penalty bound apply. Divide by t2 and
let t → 0 to get
                                          c∥v∥2 ≤ Qn (v).                                     (11)
This argument is performed separately at each n; it does not impose uniform neighborhoods or
derivative remainder rates.
    Use the two internal coordinates u, v of Section 2 to regard a complex number as a real
internal vector. For 1 ≤ s ≤ R and a ∈ {1, i}, define ψs,a by taking only component j nonzero
and setting it to n−d/2 times the internal vector corresponding to ae2πisxi /n . The finite-character
orthogonality identity and the real orthogonality of the two quadratures give an orthonormal
family of 2R fields. This also covers even n; the two quadratures use two internal coordinates,
not two allegedly independent scalar sine and cosine functions. Since i ̸= j, these fields are
independent of xj , so δψs,a = 0. Their span SR,n is thus an actual 2R-dimensional subspace of
Dn .
    Every nonzero forward difference of ψs,a is in direction i and has the same squared norm at
every site, namely n−d |e2πis/n − 1|2 . The exact Hodge and repair energies are therefore

                                   Qn (ψs,a ) = (1 + bij (n))|e2πis/n − 1|2 .

                                                        9
In particular the trace of the compression of Qn to SR,n is the middle expression in (10); no
invariance of SR,n under the weighted operator is asserted or needed.
    For completeness, the positive trace/rank argument is as follows. Set U = SR,n ∩ ker Ln .
Rank-nullity gives dim U ≥ 2R − dim Fn . Extend an orthonormal basis of U to one of SR,n .
Equation (11) bounds the terms on U below by c; positivity of Qn makes every remaining diagonal
term nonnegative. Hence c(2R − dim Fn ) ≤ trSR,n Qn . Finally |e2πis/n − 1| ≤ 2πs/n ≤ 2πR/n,
which proves the last inequality in (10).
    Fix R. The right side tends to zero under the stated mean condition. Eventually it is less
than c. If dim Fn < 2R, integrality would make the left side at least c. Thus dim Fn ≥ 2R
eventually. Arbitrarily large fixed R prove the claimed divergence.

   The condition concerns one directional spatial average, not the maximum of all weights. For
example, a weight of size nd+1 at one site in component (i, j) and zero elsewhere has bij (n) = n,
while its maximum is not subquadratic. Theorem 9.1 still excludes bounded output dimension
under its other hypotheses. This example is a direct calculation, not an additional formal
endpoint. The nonnegative-weight condition is essential to the trace argument as used here: the
complement of the derivative kernel must contribute nonnegative energy. This is not a universal
extension of older statements allowing signed weights with a pointwise absolute cap.

9.1   A constructed quadratic-weight boundary example
The exponent 2 cannot be replaced by an unrestricted allowance of quadratic-size mean weights.
                                                                         2
Let µj (A) = n−d x Aj (x), with output in the same fixed space F = (RNc −1 )d for every n. A
                 P

finite path comparison on the actual periodic lattice gives
                 ∥A − lift µ(A)∥2 ≤ dn2 ∥GA∥2 ,        ∥ lift µ(A)∥2 = nd ∥µ(A)∥2 .
One way to obtain the first inequality is to write each difference of site values as a path of at
most dn forward edges, apply finite Cauchy–Schwarz, and average the pairs of sites; the displayed
constant is deliberately nonoptimal. The exact modular-torus reindexing and its transport
to the physical cochain norm are also proved in the companion formal construction. Using
∥x + y∥2 ≤ 2∥x∥2 + 2∥y∥2 , choose actual weights wn (k, (x, l)) = 2dn2 and the quadratic penalty
Φn (y) = 2nd ∥y∥2 . Then
                   ∥A∥2 ≤ ⟨A, G∗ Wn GA⟩ + Φn (µ(A)) ≤ Qn (A) + Φn (µ(A))
on the entire space, hence also on Dn . The mean observation is an actual continuous linear map
with finite-dimensional output type independent of n, not a postulated observation certificate.
Here bij (n) = 2dn2 and the subquadratic hypothesis fails. The example allows Kn = 2nd to vary,
exactly as the obstruction does. It proves neither an optimal boundary constant nor positive
coercivity for an interacting gauge operator. The path/mean mechanism is classical; see the
primary exposition in [8].

9.2   Why the penalty assumption remains
The C 1 counterexample after Theorem 7.1 also applies to the actual nonnegative Qn and to
Dn . A second useful counterexample retains a polynomial observation and a globally Lipschitz
penalty:
          C(A) = ∥A∥2 ∈ R,        Φ(y) = c|y|,        DC(0) = 0,      Φ(C(A)) = c∥A∥2 .

                                                 10
This example already gives the bound for the actual admissible choice w = 0, with Qn = K0,n ⪰ 0.
The zero-form interpretation is only an abstract illustration, not an instance of this nonnegative-
weight lattice family. No finite local quadratic upper constant for Φ exists, since c|y|/y 2 = c/|y|.
Likewise, C(A) = ∥A∥3/2 and Φ(y) = c|y|4/3 are both C 1 with zero derivatives at zero, yet their
composition is exactly quadratic. These are complete analytic counterexamples, not new Lean
claims.
    There is a distinct analytic regularity tradeoff, not a hypothesis removal for merely differ-
entiable observations. If, on each fixed derivative-kernel direction, C(tv) = t2 Hv + o(t2 ), and
Φ(0) = 0, DΦ(0) = 0, then Φ(C(tv)) = o(t2 ). Indeed ∥C(tv)∥/t2 is bounded and |Φ(y)| ≤ ϵ∥y∥
near zero, including at zero; multiply the two estimates and let ϵ ↓ 0. A C 2 observation and a
nonnegative differentiable penalty vanishing at zero suffice for this step, because a differentiable
local minimum has zero derivative. No actual observation’s C 2 regularity is proved here, and no
formal composition of this alternate route is claimed.
    The strengthened mean-weight result is an output-rank divergence theorem. Its fixed-R
argument does not assert a positive density of observations per lattice volume. Fixed c > 0,
nonnegative weights and the stated penalty condition remain explicit. In particular no interacting
or continuum Yang–Mills hypothesis, ultraviolet activity estimate, or physical spectral gap is
supplied by this section.


10     Signed weights and the limits of mean criteria
Write Rw = G∗ W G and Qw (A) = ⟨A, K0,n A⟩ + ⟨A, Rw A⟩. For signed weights this form need not
be nonnegative. Its spatial means alone no longer supply the positive trace comparison used
above. The following sufficient condition is nevertheless available without a lower bound on any
original weight. Define the pointwise positive part and its selected directional mean by
                                                                              −d
                                                                                   X
             w+ (k, (x, l)) = max{w(k, (x, l)), 0},               b+
                                                                   ij (n) = n          w+ (i, (x, j)).
                                                                                   x

In general b+
            ij is not the positive part of the signed mean.

Theorem 10.1 (A sufficient signed-weight condition). Keep the observation, penalty, local
divergence-free domain and fixed c > 0 of Theorem 9.1, but use arbitrary signed actual weights in
the local coercivity inequality. For every 0 ≤ R < n,

                                                     8π 2 (1 + b+
                                                                ij (n))R
                                                                         3
                                   c(2R − dim Fn ) ≤                       .
                                                              n2
If (1 + b+        2
         ij (n))/n → 0, then dim Fn → ∞. The original Cn , Ln , Φn , c, Kn , δn , rn are retained.

Proof. The exact weighted-gradient energy gives, for every actual cochain,
                    X                                    X
      ⟨A, Rw A⟩ =           w(k, (x, l))∥Dk Al (x)∥2 ≤           w+ (k, (x, l))∥Dk Al (x)∥2 = ⟨A, Rw+ A⟩.
                    x,k,l                                x,k,l

The inequality uses only nonnegativity of the squared differences. Thus the original local coercivity
inequality transfers upward to the constructed nonnegative repair Rw+ , and Theorem 9.1 applies.
Nonnegativity of w+ and the comparison are proved from their actual definitions, not supplied
as fields of a comparison structure.

                                                      11
   This changes the explicit mean hypothesis for signed weights. It neither proves the original
weights nonnegative nor removes the local regularity, quadratic penalty or fixed positive coercivity
requirements.

10.1    Zero signed means with fixed output
There is no counterpart using only ordinary signed directional means, even when every such
mean is zero. Fix a site o ∈ Xn , set V = nd , a = 2dn2 , and construct actual weights
                                                                  
                                   wn (k, (x, l)) = a 1 − V 1x=o .

Since |Xn | = V , their ordinary spatial means are all exactly zero. Let µ(A) be the directional
mean above, and let Jn (A) = (Dk Al (o))k,l collect all actual forward differences at o. Use the
same finite output type for every side:

       F = (Rm )d × (Rm )d×d ,     Cn (A) = (µ(A), Jn (A)),   ∥(y, z)∥F = max{∥y∥2 , ∥z∥2 }.

Its dimension is (d + d2 )m, independent of n. The companion code proves the fixed finite output
type; this displayed numerical dimension is an analytic calculation, not an additional named
oracle endpoint.
Proposition 10.2. The actual continuous linear observation Cn and the nonnegative quadratic
penalty
                              Φn (y, z) = 2V ∥y∥22 + aV ∥z∥22
satisfy Cn (0) = 0, DCn (0) = Cn , Φn (y, z) ≤ V (2 + a)∥(y, z)∥2F , and

                           ∥A∥2 ≤ Qwn (A) + Φn (Cn (A))        (A ∈ En ).

Consequently all the original local observation and penalty hypotheses can hold with fixed output
and c = 1, although all signed means vanish.
Proof. Linearity follows directly from the finite sums and differences. The penalty bound follows
from each projection norm being at most the specified product max norm. The exact energy
expansion is
                              ⟨A, Rwn A⟩ = a∥GA∥2 − aV ∥Jn (A)∥22 .
Adding the penalty cancels the negative term and leaves

              Qwn (A) + Φn (Cn (A)) = ⟨A, K0,n A⟩ + a∥GA∥2 + 2V ∥µ(A)∥22 ≥ ∥A∥2 .

The last step is the actual mean/path estimate of the preceding section, with a = 2dn2 , together
with K0,n ⪰ 0.

   The coefficient Kn = V (2 + a) may grow with the lattice side, exactly as allowed by the
proposed ordinary-mean extension. This is not a transfer of the desired coercivity into an assumed
observation certificate. The weights, observation, penalty and cancellation are constructed. For
n > 1 their positive-part mean is a(1 − V −1 ), of quadratic rather than subquadratic order, so
they do not contradict Theorem 10.1.
   As an analytic diagnostic, take n ≥ 3, i ̸= j, a unit internal vector u, and Aj (x) = u1xi =oi ,
with other components zero. Then δA = 0, ∥GA∥2 = 2nd−1 and ∥Jn (A)∥2 = 1, giving

                                 Qwn (A) = nd−1 2 − a(n − 2) < 0.
                                                              


                                                 12
This explains the failure of the original positive trace argument. The diagnostic field calculation
is analytic; the formal fixed-output family theorem does not claim to check this additional field
explicitly.

10.2    An attributed square cancellation
Fix distinct directions i, k, a component j ̸= i (for instance j = k), and o ∈ Xn . For an amplitude
A0 ≥ 0, define the repair weights additively by

                          w(p) = A0 1p=(i,(o,j)) − 3A0 1p=(k,(o,j))
                                  − 3A0 1p=(i,(o+ek ,j)) − 3A0 1p=(k,(o+ei ,j)) .

Writing Ds Aj (x) = Aj (x + es ) − Aj (x), commuting shifts give

                       Di Aj (o) = Dk Aj (o) + Di Aj (o + ek ) − Dk Aj (o + ei ).

The squared norm of this sum is at most three times the sum of the three squared norms. The
actual finite weighted-energy sum therefore proves ⟨A, Rw A⟩ ≤ 0 for every cochain. For n ≥ 2 the
positive edge is separate from all negative contributions, so w+ = A0 1p=(i,(o,j)) and b+          d
                                                                                         ij = A0 /n .
Choosing A0 = nd n2 gives b+         2
                              ij = n .
    If the original local coercivity hypotheses hold for this actual repair, they imply the same
hypotheses with zero repair, since Qw (A) ≤ ⟨A, K0,n A⟩. Applying Theorem 9.1 with zero weights
again forces dim Fn → ∞. The selected normalized positive-part mean is 1 + n−2 and does not
tend to zero. This last limit interpretation is an elementary analytic consequence of the formal
exact mean identity, not a separate negated-limit oracle endpoint. This single sparse cycle does
not make every directional criterion fail: other eligible means are zero. Its formal endpoints
establish the selected mean and derived order, not an all-directions counterexample.
    There is, however, a finite sum that covers every eligible pair. This extension is analytic here.
For every j and every i ̸= j, use the preceding cycle with k = j, the same site o and amplitude
A0 , and add all its weight functions to obtain w. Linearity of the exact weighted-energy sum
gives ⟨A, Rw A⟩ ≤ 0. For every off-diagonal pair i ̸= j, direct inspection of the four indicators
gives
                                 w(i, (x, j)) = A0 1x=o − 3A0 1x=o+ej .
Every diagonal component has only nonpositive contributions. For n ≥ 2 the two displayed sites
                                         +
are distinct, so each eligible pair has bij = A0 /nd . With A0 = nd n2 , all off-diagonal positive-part
means equal n2 , while the derived domination by zero still gives the original rank obstruction.
Thus no eligible mean condition in Theorem 10.1 applies to this sum. The conclusion follows
from its actual energy order, not from an assumed comparison field. The finite sum and its
all-pairs mean calculation are not silently included in the single-cycle formal oracle reports.
    The cancellation mechanism is classical, rather than a new general spectral principle. Re-
stricted to the four active vertices, the negative of this scalar repair has three positive path
conductances 3A0 and a direct negative conductance −A0 . For A0 > 0 the path resistance is
1/A0 , so this is the critical case of Zelazo and Bürger’s Theorem III.3 [9]. Isolated vertices
contribute zero blocks; the internal vector coordinates sum scalar copies. This comparison
attributes the mechanism; it does not establish originality of the whole consolidated dossier.
    The conditional obstruction is nonvacuous. An analytic check takes Fn = En , Cn = I and
Φn (y) = ∥y∥2 − ⟨y, Rw y⟩ ≥ 0 (or replace w by w). The operator norm gives the upper quadratic

                                                   13
bound (1 + ∥Rw ∥)∥y∥2 , while Qw (A) + Φn (A) = ⟨A, K0,n A⟩ + ∥A∥2 ≥ ∥A∥2 . This example has
growing output, as the theorem requires; it is not an additional formal endpoint or a compressed
observation construction. None of these signed-weight statements proves a volume-density bound,
identifies an interacting Hessian, or supplies a physical mass gap.


11     Full volume rank from signed total coefficient means
The directional strip in Section 9 detects divergence of the observation dimension. A full
dimensional coexact packet yields a positive volume density under a stronger, explicitly stated
mean hypothesis. Original weights may have either sign. The relevant quantity is the spatial
mean of max{1 + w, 0}, not an ordinary signed mean or a positive part taken after averaging.
The extra 1 is the actual flat Hodge coefficient, already absorbed into the envelope; it must not
be added a second time.
    In this section write D ≥ 2 for the number of lattice directions, Vn = nD , and En for the
actual real cochain space on (Z/nZ)D , with fixed Nc ≥ 2. Use field components 0, 1 and the
internal real plane representing a complex scalar from Section 2. Put Di Al (x) = Al (x+ei )−Al (x)
and retain the original form
                                                     X
                         Qwn (A) = ⟨A, K0,n A⟩ +             wn (i, (x, l))∥Di Al (x)∥2 .
                                                     x,i,l

The actual all-cochain flat Hodge identity gives Qwn (A) =
                                                                       P                                       2
                                                                          x,i,l (1 + wn (i, (x, l)))∥Di Al (x)∥ .

Theorem 11.1 (Finite full volume mean budget). Let 1 ≤ R and 2R < n. Assume m ≥ 0 and
                  X
                        max{1 + wn (i, (x, l)), 0} ≤ Vn m            (0 ≤ i < D, l = 0, 1).                   (12)
                    x

No mean bound on the other field components, original weight lower bound or prescribed uniform
pointwise cap is assumed. Let Cn : En → Fn be Fréchet differentiable at zero, Cn (0) = 0, with
Fn finite dimensional. Suppose Φn (y) ≤ Kn ∥y∥2 for ∥y∥ < δn , δn > 0, and the original small
divergence-free coercivity inequality holds with c ≥ 0 and some radius rn > 0. Set
                                          D−1
                                          X
 H = 2R(2R + 1)D−1 ,           Λ(k) = 4         sin2 (πki /n),         K = {1, . . . , R} × {−R, . . . , R}D−1 .
                                          i=0

Then
                                                     X                          4π 2 DR2
                        c(H − dimR Fn ) ≤ m                      Λ(k) ≤ mH               .                    (13)
                                                (k,q)∈K×{0,1}
                                                                                   n2

Proof. For k ∈ K use the actual scalar character χk and the coexact field with components
given by its backward differences in directions 1, 0, with opposite signs. Commuting differences
give actual divergence zero. Since k0 =     ̸ 0 (mod n), the normalization denominator is positive.
Counting Fourier orthogonality and both internal real quadratures produce an orthonormal
family of H actual real fields, spanning Sn . The condition 2R < n prevents aliasing of their
scalar frequencies; no scalar real-valued conjugacy constraint is imposed on the internal plane.
Every vector of Sn is supported on field components 0, 1.
    Define actual coefficients vn (i, (x, l)) = max{1+wn (i, (x, l)), 0} for l = 0, 1, and zero otherwise,
and the positive form Pn = G∗ Vnwt G with those coefficients. The notation Vnwt here denotes

                                                     14
the weight multiplication operator, not lattice volume. Then Pn ⪰ 0 on all cochains and
Qwn (A) ≤ ⟨A, Pn A⟩ on Sn . This comparison is needed only on the actual packet image, and is
not asserted on every cochain or every divergence-free field.
   Write Ln = DCn (0). The same shrinking-ray proof as in Section 9, now followed by the
proved envelope comparison, gives c∥v∥2 ≤ ⟨v, Pn v⟩ on Sn ∩ ker Ln . Its dimension is at least
H − dim Fn . Complete an orthonormal basis of that kernel within Sn . Positivity of Pn controls
the complementary trace terms. Thus c(H − dim Fn ) ≤ tr(Pn |Sn ), where the restriction means
the genuine orthogonal compression.
   For an individual normalized packet Uk,q , its squared component amplitudes are constant in
x and are Vn−1 ak,l for l = 0, 1, where ak,l ≥ 0 and ak,0 + ak,1 = 1. Consequently
                             D−1 1
  ⟨Uk,q , Pn Uk,q ⟩ = Vn−1
                             XX                               X                        X
                                       |χk (ei ) − 1|2 ak,l       vn (i, (x, l)) ≤ m       |χk (ei ) − 1|2 = mΛ(k).
                             i=0 l=0                          x                        i

Sum over all H basis vectors. Finally every signed integer frequency satisfies |ki | ≤ R, and
| sin t| ≤ |t| gives Λ(k) ≤ 4π 2 DR2 /n2 . All D derivative directions remain in this sum even though
only two field components are occupied.

Theorem 11.2 (One positive density on the full integer tail). Fix D, Nc , c > 0 and m ≥ 0.
For each integer n under consideration, allow its own Fn , Cn , Ln , Φn , Kn , δn , rn , wn satisfying the
original local hypotheses and (12), with these same c, m. There are k ≥ 3 and ε > 0, depending
only on D, m, c, such that
                                   dimR Fn ≥ εnD       (n ≥ k)
whenever those finite-side hypotheses hold. If the original family hypotheses hold only for n ≥ n0 ,
the conclusion applies for n ≥ max{n0 , k}. One may take ε = 1/(2k D ) for any integer k ≥ 3
satisfying 2m 4π 2 D/k 2 ≤ c. No common quadratic penalty constant, differentiability neighborhood
or coercivity radius is required.

Proof. Choose such a k by the Archimedean property. For each n ≥ k put R = ⌊n/k⌋. Integer
division yields
                 R ≥ 1,      kR ≤ n < k(R + 1) ≤ 2kR,     2R < kR ≤ n.
Hence the actual packet is admissible and R/n ≤ 1/k. The finite theorem gives c(H − dim Fn ) ≤
(c/2)H, so H ≤ 2 dim Fn . Also H ≥ (2R)D ≥ (n/k)D . Combining these gives the displayed
density. Each shrinking-ray argument was applied at a fixed n before using these integer
inequalities. No limit of derivatives or local neighborhoods is taken.

Proposition 11.3 (Exact trace average and a sharper analytic constant). For R ≥ 1, put
AR (x) = R       2
        P
          r=1 sin (rx). The actual multiplier average in (13) is

                                           1 X                    2DR + 1
                             BD,R,n =            Λ(k) = 4AR (π/n)           ,
                                           H k,q                  R(2R + 1)
                                     R sin(Rx) cos((R + 1)x)
                              AR (x) =  −                    ,
                                     2           2 sin x
                                     2π 2
                             BD,R,n ≤ 2 (R + 1)(2DR + 1).
                                     3n



                                                          15
For fixed 0 < α < 1/2 and R = ⌊αn⌋, the original family hypotheses therefore imply the analytic
bound
                             dim Fn              m          sin(2πα)
                                                                    
                                          D
                     lim inf        ≥ (2α) 1 − 2D 1 −                    .
                      n→∞      nD                c             2πα
Its elementary quadratic lower estimate replaces the bracket by 1 − 4π 2 Dmα2 /(3c). This improves
the low-frequency quadratic coefficient of the maximum-coordinate estimate by a factor three.

Proof. The positive first coordinate contributes 4AR /R to the average; each of the D − 1
centered coordinates contributes 8AR /(2R + 1). Both real quadratures occur in numerator and
denominator. The cosine sum follows by summing 2 sin x cos(2rx) = sin((2r +1)x)−sin((2r −1)x)
and telescoping; sin2 (rx) = (1 − cos(2rx))/2 gives the formula for AR . Bounding sin2 (rx) ≤ r2 x2
and summing r2 gives the finite upper bound, including its lower-order terms. Floor inequalities
give H/nD → (2α)D , and sin x/x → 1 gives BD,R,n → 2D[1 − sin(2πα)/(2πα)]. Divide the finite
rank bound by nD and take the lower limit. Negative right sides are merely weak bounds. For
m = 0, taking α ↑ 1/2 gives lower density one.

   These are classical Fourier and finite trace arguments, with the standard discrete-torus
spectrum already present in the literature [10]. The exact average and its improved constant are
analytic calculations here, not extra formal endpoints or sharp optimal observation-rank claims.
They do not identify an interacting background or a continuum Yang–Mills spectral gap.


12     Why dimension is not a sufficiency criterion
The following analytic statement is included to prevent the reverse inference from a necessary
rank budget. It is not a new Lean-verified endpoint here. The proof below is the classical
singular-Schur range condition [3, 4], expressed as boundedness below on each measurement fiber;
we claim no new general matrix criterion. Let E be a finite-dimensional real inner-product space,
H = H ∗ and B = H − cI. Fix linear C : E → F , and decompose E = N ⊕ W with N = ker C,
W = N ⊥ . In this decomposition write
                                                       !
                                               A D
                                        B=          .
                                               D∗ G

Proposition 12.1. A finite real-valued function Φ with Φ(0) = 0 can make ⟨x, Bx⟩ + Φ(Cx) ≥ 0
for every x if and only if A ⪰ 0 and ker A ⊆ ker D∗ . In that event a quadratic penalty suffices.

Proof. Taking x ∈ N proves A ⪰ 0. For z ∈ ker A and fixed w ∈ W , the value at tz + w contains
2t⟨z, Dw⟩, while C(tz + w) = Cw is fixed. Boundedness below for all real t forces this coefficient
to vanish.
    Conversely, ker A ⊆ ker D∗ implies D(W ) ⊆ ran A. Let A† be the inverse on ran A and zero
on ker A. Completing the square gives

            ⟨n + w, B(n + w)⟩ = ⟨n + A† Dw, A(n + A† Dw)⟩ + ⟨w, (G − D∗ A† D)w⟩.

The restriction C|W is injective; extend its inverse on C(W ) to a linear map T : F → W . The
quadratic function Φ(y) = ⟨T y, (D∗ A† D − G)T y⟩ cancels the second term and vanishes at zero.
If F has a chosen Euclidean norm, a sufficiently large nonnegative multiple of ∥y∥2 also suffices,
by finite-dimensional norm bounds.

                                                16
    For a concrete counterexample let H = diag(0, 2), c = 1 and C(x, y) = x + y. On ker C,
⟨x, (H − I)x⟩ = 0, and C detects the negative eigendirection of H − I. Nevertheless, on (t, 1 − t)
the repaired form is 1 − 2t + Φ(1), unbounded below for every finite Φ(1). Kernel nonnegativity
and low-mode detection alone do not suffice; cross-coupling must be checked.


13     Operator scaling and the actual consumer
In the repository, the flat fixed-volume covariance endpoint uses K0 + aQ∗ Q with the physical
counting ℓ2 norm and the same unscaled flat Hodge operator. More precisely, the declared
precision shell includes −Σ. Specializing every perturbation and its summable majorant to zero
and taking a > 0 gives the available certified coercivity lower bound min(1, a)/CP , with CP > 0
from the full-periodic block-Poincare estimate. This is not a claim that this value is optimal.
At fixed d, Nc , N ′ the block codomain is fixed and finite. Inspection therefore identifies the
unscaled flat base route with the setting of Theorem 6.1, with ΦL (y) = aL ∥y∥2 and no fine repair.
Even allowing arbitrary scalar aL or rescaling QL does not yield a positive uniform full-space
constant. This is a source-level specialization in this text; no new Lean adapter to that consumer
is claimed. At the new source anchor below, the module PhysicalGaugeFixedPrecision defines
flatGaugeFixedPrecisionCLM; its explicit-Poincare coercivity theorem is recorded by its full
name and specialization in the linked declaration map.
     The inspected endpoint is explicitly fixed-volume. Its positive rate may depend on L, N ′
and CP , so there is no contradiction. Nor does the obstruction exclude all possible uniform
Combes–Thomas arguments. Its locality radius and matrix-entry bounds also vary with L;
coercivity alone would not settle the rate. An interacting Hessian, a growing measurement
budget, a different sector norm or a physically rescaled operator must each be audited separately.
     In particular, writing ℓ = L + 1 so that nL = ℓN ′ , replacing K0 by ℓ2 K0 changes the band
threshold exactly to 4π 2 dR2 /(N ′ )2 . The proof above no longer drives it below every fixed c > 0.
This observation is an escape from this proof, not an established coercivity theorem for the
programme’s physical operator. No ultraviolet activity estimate, continuum limit, Wilson-Hessian
identification or Yang–Mills mass gap is obtained.


14     Formal evidence and publication context
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
here; they are not all silently included in that formalization claim. The external declaration
map keeps both anchors. The public source repository is THE-ERIKSSON-PROGRAMME on

                                                 17
GitHub. The preserved parent v5 map is declaration-map.json and the preserved evidence is
reproducibility/. Exact source SHAs, not moving branch heads, identify the formal claims.
That parent map does not certify the new full volume extension. The map packaged with this
manuscript records each added anchor and the separately reproduced full-tail extension. The
accompanying exact-artifact report binds the final source and PDF hashes.
    The geometric and Fourier modules are ordinary proof dependencies, not assumptions about
a newly supplied band. Each previously verified stage identified below has complete same-source
fresh-clone Colab evidence; the new extension boundary is stated separately. For the uniform
endpoints the tested source is
                         17ca395d4e9de992b1c575454a112da9e6f97e86.

Its two runs agree in compiled object, raw oracle log and source-manifest hashes. The standalone
budget lemma uses propext, Quot.sound; the other four uniform-module reports also use
Classical.choice. No extra axiom is reported. Actual-log acceptance and three real-field
rejection tests pass under normal and optimized Python. These tests concern evidence handling,
not mathematical independence.
    The additional whole-space gradient/Hodge identity and constructed weighted repair bounds
use tested source
                         dfd49d0b0730a4d36f58a4cbb7a17d6a41fb60bc.

The full-space tangent endpoints in Section 7 use tested source
                         81cf07b2e0d30543682c4073a4a2d82950d638b7.

Each has two complete same-source fresh Colab Linux reconstructions with matching compiled
object, raw oracle and LF-source-manifest hashes. For the tangent source, all three named
endpoints use only propext, Classical.choice and Quot.sound. Its oracles and pinned Colab
reproduction drivers are separate from the manuscript render. Failed source candidates and their
full logs are retained in the programme evidence archive. Later, separately reproduced sources
formalize the actual implicit-function curve construction at
                         ef81f028ce6e7e8aaca7e9229eb00aa683752a41.

The local quadratic-energy regular-sector obstruction uses
                         9bb90cfd77ec5cea5c4447667fe8baf8c21429a1.

The displayed sector proofs remain readable analytic arguments; their uniform consequence is
not silently included in those four-endpoint reports. No theorem about a nonlinear sector is
inferred from a full-space no-go alone.
    Short labels and an external declaration map replace long wrapped Lean names in this
manuscript. The companion source map records exact names, source SHAs, and evidence
directories. Reproduction commands remain in the existing copyable notebooks rather than
being split into misleading line fragments. The fixed-map Schur criterion, its counterexample
calculation and consumer specialization above are analytic or source-inspection arguments; the
whole manuscript is not described as machine checked.
    The actual mean-weight finite/asymptotic theorem of Section 9 uses tested source
                         ac60c0df885d8866329a839e2b4e73c90595d806.


                                              18
Its two own fresh Colab Linux clones 076/076b pass six exact standard-axiom reports and all
nine stages. Compiled module SHA-256 is
            28fcc004795a1d8ab74ca87b5e67cdf90f557551bc02b1bb912da38324c26e50.

Raw oracle and LF-source-manifest hashes also match; full records and the strict mutation-tested
validator are preserved in the mean-weight reproduction package. The proof composes the actual
character strip, its exact trace, positivity, local derivative-kernel bound and multiplier estimate;
these are derived lemmas, not desired conclusions supplied as hypotheses. Nonnegative weights,
fixed positive c and the quadratic penalty upper bound remain. The constructed quadratic-weight
mean observation instead uses tested source
                          7f37d6437a8f69a1d3fddf3dc0bcfad74c6bf9b6.

It has two same-source fresh-clone reproductions 067/067b with six exact standard-axiom reports
and matching compiled, raw-oracle and LF-source hashes. The formal output is an actual fixed
finite-dimensional type; the displayed numeric dimension and nonoptimal path explanation are
not additional oracle endpoints. The penalty examples and regularity tradeoff are analytic only.
Classical quadratic-form, Fourier and trace mechanisms, as discussed in [7], establish no new
general principle or priority here.
    The signed-weight results in Section 10 have distinct exact formal anchors. The positive-part
construction, actual energy order and finite/asymptotic sufficient condition use
                          810785b17b2f1bb14dd6caa5435865eb51a86ef3.

Its fresh own Colab Linux clones 077/077b pass six exact standard-axiom reports. The actual
zero-signed-mean fixed-output family instead uses
                          497e3b4ef4046cee25b1069b8aa0fd8c0cfaa178.

Its clones 079/079b pass ten exact reports, including actual Hodge coercivity and the constructed
family on one fixed finite output type. The individual square-cycle order, selected positive-part
mean and rank consequence use
                          4c5728d147721523f5a521011351ac4bf2d3cf86.

Its clones 081/081b pass ten exact reports. In every pair the compiled module, raw oracle and LF-
source-manifest hashes match, with real mutation controls under normal and optimized Python.
The declaration map records exact names and hashes, and links the complete reproduction
packages. Failed probes 078 and 080, their sources, full diagnostics and corrections remain
preserved; no passing result is inherited across source changes.
    The individual cycle has zero positive-part means in other pairs. Its formal selected-pair
identity is not an all-directions counterexample. The finite sum covering all off-diagonal pairs,
its displayed mean calculation, the negative hyperplane diagnostic, numerical output dimension,
normalized critical-mean limit interpretation and full-state identity-observation non-vacuity check
are analytic here. They are not additional oracle endpoints. No density conclusion from ordinary
signed spatial means alone has been established. The code indexes positive side length by k + 1,
equivalent to the positive integer indexing used in the text.




                                                19
14.1    Evidence boundary for the full volume extension
The actual normalized image and genuine compression trace are separately reproduced at source
9a8946b7, the whole-image support and constructed positive total envelope at 88445ac6, and the
original local nonlinear finite rank composition at 3a2d5305. The actual numerical bound and
constructed uniform dilation density have two matching own Colab reproductions at 031ca274,
with five exact standard-axiom reports and full manifests. These are distinct source artifacts,
not grades inherited by this manuscript.
    The full integer-tail source 067fed75 now has two fresh own Colab reproductions, 094/094b,
with all nine stages exiting zero and five exact standard-axiom reports. Their compiled module,
raw oracle and LF-source manifest hashes match. Real mutation controls pass under both normal
and optimized Python. The earlier browser loss and absent saved output are preserved separately;
no outcome is reconstructed for that earlier event. The live session manager reported no active
sessions before and after these fresh runs. This is execution reproducibility, not independent
scientific review. The exact averaged multiplier and sinc limit remain analytic calculations.
Preparation and rendering alone do not constitute a completed exact-artifact review.


Historical model assessments and review context
This candidate was prepared by the Codex agent in the author’s continuing programme chat,
with access to earlier objections, source audits and supplied reproduction records. The served
backend model identifier and reasoning setting are not exposed, and no technical isolation or
scientific independence is claimed for this preparation.
    The public v2 of this record has canonical PDF SHA-256
            b37f2fe86b7a8a526ad02f8b28491c300a9ff72d5653536bc5532e8c9468ed8f.

A subagent explicitly authorized by the author and configured as gpt-6-astra assessed that
exact eight-page artifact after first preserving the earlier candidate’s objections. Actual backend
identity and reasoning setting were not exposed. The workflow used the same account, provider
and programme context; it was not blind or organizationally independent. The complete earlier
and corrected-artifact reports remain in the v2 package. The corrected-artifact report regarded
O1–O5 as resolved and retained O6: no independent complete Lean rebuild or dependency-closure
audit. No numerical score or human peer review was supplied.
    The prior internal candidate v6 retained the signed sufficient condition, fixed-output coun-
terexample and individual cancellation, the analytic all-pairs sum and diagnostics, and adds the
actual full volume mean-budget consequences. The prior internal v5 PDF had eighteen pages
and an unscored preparing-agent report. Neither that report nor the finite-source numerical
assessments apply to this changed PDF. Its accompanying exact-artifact report identifies every
page inspected, its first numerical assessment and complete objections by the hash of the exact
PDF. Rendering alone is not an assessment. The companion report must be complete before
delivery or deposit. No new external model has assessed this candidate; no independent scientific
or human peer review is claimed. Complete older model reports and objections remain version-
specific in the preserved dossier. Lluis Eriksson is both author and AIRR operator. The last
verified public v4 record is a fifteen-page Working paper, not admitted to the accepted collection,
under CC BY 4.0 with CC0 metadata, at its immutable version page. Its exact frozen PDF
SHA-256 is


                                                20
            e5e9ddcf044ddcfab0e4cae8e2c6ac1a3dca39ff21bf23b20989aaff4b220e05.

Earlier public versions remain preserved. The internal v5 PDF, SHA-256
            003be55040d84fbd5dc8cf88caa56bd25ddafaaf575409314e6430521ed4ce61,

is a distinct unpublished artifact. Internal label v6 is not a newly issued public AIRR version
or private submission number. That source preparation had not been deposited, accepted or
published. Earlier exact-artifact permissions, licenses and reviews are not transferred to a
changed PDF. No new historical grant, legal acceptance, external-model transfer or editorial
outcome is claimed.


15     From necessary rank budgets to sufficient observations
The preceding sections establish necessary information budgets and their formal and analytic
boundaries. The continuation below asks when actual coefficient distributions suffice to construct
observations of the same order. It is integrated into this revision, not a second paper or deposit.
For these sections set D = d ≥ 3 and g = Nc2 − 1, h = Dg. The symbol µ ≥ 1 denotes the scalar
coefficient mean budget here; it does not replace the earlier symbol m = Nc2 − 1 for internal
dimension. The field is denoted U instead of A. All norms and original forward-edge occurrences
use the same counting, unit-spacing flat convention. Restrictions on scalar coefficients and the
distinction between spectral coordinates and rectangular means are stated explicitly below.
    The historical main candidate and appendix were individually reviewed on different exact
PDF bytes. Neither assessment transfers to this integrated artifact. Its first complete exact-PDF
review is a separate hash-linked sidecar after visual inspection of every page. No new external
model review, human peer review, historical grant, deposit or publication is claimed.


16     Actual objects and the original observation problem
Fix D ≥ 3, Nc ≥ 2, c > 0, and the unit-spacing torus Xn = (Z/nZ)D . The actual real adjoint
coefficient space has dimension g = Nc2 − 1; there are D field components, so write h = Dg.
For the actual forward difference di u(x) = u(x + ei ) − u(x), take one scalar total coefficient
a(x) = 1 + wi,x,j > 0 shared by all derivative directions and field components. Use counting
norms and the actual componentwise flat energy
                                                   X
                             Qw (U ) = Ea (U ) =           a(x)∥di Uj (x)∥2 .                 (14)
                                                   x,i,j

The existing flat Hodge identity identifies these forms; its formal source is listed in Section 22.
All new adapters in this appendix remain analytic. There is no substitution of a covariant or
interacting derivative in (14).
    The original local data consist of a differentiable map C at zero, with C(0) = 0, into an
actual finite-dimensional real normed space F , and a penalty satisfying Φ(y) ≤ K∥y∥2 near zero,
such that
                                   c∥U ∥2 ≤ Qw (U ) + Φ(C(U ))                                 (15)
for sufficiently small actual divergence-zero fields. “Local” here means a configuration-space
neighbourhood; spatial support of C is an additional condition. The constant c is fixed, while
observation maps and neighbourhoods may depend on n.

                                                21
    A useful necessary condition follows directly. If an actual J-dimensional divergence-zero
subspace has Qw (U ) ≤ λ∥U ∥2 with λ < c, then dim F ≥ J. Otherwise a nonzero U in that
subspace lies in ker DC(0). Along tU , C(tU ) = o(t) and the penalty is at most o(t2 ). Dividing
(15) by t2 and taking t → 0 contradicts λ < c. No rank or band certificate is supplied as an extra
hypothesis in this argument.


17     The critical global moment theorem
Put p = D/2 > 1. For µ ≥ 1 suppose that

                                 n−D
                                       X
                                              (µ/a(x))p ≤ M < ∞.                              (16)
                                       x∈Xn

Theorem 17.1. Under (16), there is an actual real linear spectral observation C such that

                   c∥U ∥2 ≤ Qw (U ) + c∥C(U )∥2       for every actual cochain U,

and
                               dim F ≤ C∗ max{1, (n/ 1 + µ)D },
                                                         p
                                                                                              (17)
                                                p      −(p−1)
where, with Ip = (p − 1)2 /[p(p + 1)] and Γp = p−1 Ip           , one safe choice is
                                       h                               i
                              C∗ = h 1 + Γp (3/4)D Dp+1 cp M 2p .

Thus Φ(y) = c∥y∥2 , K = c and any positive neighbourhood radii supply the original local data. In
particular the assertion holds on the actual divergence-zero subspace.

     The original subclass 1 ≤ a ≤ 2µ with exact arithmetic mean µ is included, but those extra
normalizations are not needed for sufficiency. The distribution condition (16) remains additional;
it is not derived from an arithmetic mean.

17.1    A finite normalized Fourier lemma
For a finite abelian group of size V , let F be its counting-unitary Fourier matrix, whose entries
have modulus V −1/2 . For a frequency multiplier g put

                                L = V −1 sup tp #{k : |g(k)|2 > t}.
                                           t>0

For a nonnegative matrix B, write n(s, B) for its number of eigenvalues strictly greater than s,
counted with ordinary multiplicity.

Lemma 17.2. For K = Mf F ∗ Mg F and s > 0,

                                n(s, K ∗ K) ≤ Γp Ls−p
                                                        X
                                                             |f (x)|2p .
                                                         x

The trace and eigenvalue counts are not volume-normalized.




                                                 22
Proof. Remove phases by unitaries and set A = F ∗ M|g|2 F. If L = 0 the assertion is immediate.
Otherwise let B0 = pL/(p − 1) and let A+ be the inverse on ran A, zero on its kernel. For
0 ≤ γ ≤ A write ρ(x) = ⟨δx , γδx ⟩. Positivity makes γ annihilate ker A. On the range let
PE = 1{A+ ≤E} and RE = 1{A+ >E} . The weak-frequency tail gives

                        ⟨δx , PE APE δx ⟩ = V −1
                                                         X
                                                                    |g(k)|2 ≤ B0 E p−1 .
                                                     |g(k)|2 ≥1/E

Indeed the tail above t is t times its count plus the integral of counts above t; the resulting bound
is V Lp t1−p /(p − 1). Non-strict thresholds follow by limits. The triangle inequality for γ 1/2 δx
split by PE + RE yields
                                                    q                              2
                                                                      B0 E (p−1)/2 + .
                                                                 p
                            ⟨δx , RE γRE δx ⟩ ≥        ρ(x) −

Exact spectral layer integration consequently gives
                                                    −1/(p−1) X
                               Tr(A+ γ) ≥ Ip B0                       ρ(x)p/(p−1) .                         (18)
                                                                x

The scalar integral reduces to 01 (1−t(p−1)/2 )2 dt = Ip . Now take P to be the spectral projection of
                                R

A1/2 M|f |2 A1/2 above s, with rank ν > 0, and set γ = A1/2 P A1/2 . Then 0 ≤ γ ≤ A, Tr(A+ γ) ≤ ν,
and
                        X                     X              1/p    X                 (p−1)/p
                 sν <       |f (x)|2 ρ(x) ≤         |f (x)|2p               ρ(x)p/(p−1)             .
                        x                       x                       x
                                                                 −(p−1)
Insert (18) and raise to p. The constant becomes B0 Ip                      = Γp L. This also explicitly handles
a zero-frequency kernel.

   The density method is classical and follows the Rumin–Frank approach [13, Section 2]. The
proof above supplies its finite normalization and kernel adapter; it is not a claim of a new Cwikel
mechanism or independent discovery.

17.2    Actual lattice frequencies and the weighted inverse
For n ≥ 2 let L0 = d∗ d and work first on the actual counting-mean-zero scalar space H0 . Its
Fourier symbols are
                                                                       X
                        zi (k) = e2πiki /n − 1,         λ(k) = 4            sin2 (πki /n).
                                                                        i

Choose centred integer representatives ri with |ri | ≤ n/2, using only one representative at an
even endpoint. Concavity of sine implies

                λ(k) ≥ 16|r|2 /n2 ,          |gi (k)| := |zi (k)/λ(k)| ≤ n/(4|r|),           k ̸= 0.

Set gi (0) = 0. If |gi | > τ , then 0 < |r| < R = n/(4τ ). For R ≤ 1 there are none, and for R > 1
there are at most (3R)D representatives. Thus

                                 n−D sup tD/2 #{|gi |2 > t} ≤ (3/4)D .                                      (19)
                                       t>0

This is uniform in n, including n = 2, not an imported infinite-volume bound.

                                                       23
    Let La = d∗ Ma d. On H0 it is positive definite. For f ∈ H0 , the flow j∗ = Ma dL−1
                                                                                     a f minimizes
⟨j, Ma−1 j⟩ among d∗ j = f : write j = j∗ + k, d∗ k = 0, and the cross term is ⟨dL−1    a f, k⟩ = 0.
                                           −1
Inserting the explicit feasible flow j = dL0 f gives the actual quadratic-form comparison
                                     D
                              L−1          Ti∗ Ti ,       Ti = Ma−1/2 di L−1
                                     X
                               a ≤                                        0 .                               (20)
                                     i=1

Extend L−1                                                            ∗
        0 by zero on constants. Lemma 17.2 and (19) bound each n(s, Ti Ti ) by


                                         Γp (3/4)D s−p           a(x)−p .
                                                             X

                                                             x

   For nonnegative matrices, the count of their sum above t is no larger than the sum of their
counts above t/D: intersect the complements of their high spectral subspaces and apply min–max.
No commutation is required. With t = 1/c in (20), inversion on H0 and the single scalar constant
mode yield
                        #{λ(La ) < c} ≤ 1 + Γp (3/4)D Dp+1 cp M nD /µp .                    (21)
No spectral-band dimension is assumed in this derivation.

Completion of Theorem 17.1. Choose an actual real counting-orthonormal eigenbasis of the real
symmetric matrix La . Retain the coordinates with eigenvalue < c, separately in each of the
h real field coordinates. Complexification used in the Fourier proof preserves real eigenvalue
multiplicities; it does not double them. Energy controls coefficients at eigenvalues ≥ c, while
c∥C(U )∥2 controls the rest. Equation (21), p = D/2, and (1 + µ)/µ ≤ 2 give (17). For n = 1
take the identity on all h coordinates. This constructs the actual global spectral observation.


18     Every lower positive inverse exponent is insufficient
Theorem 18.1. For every fixed 0 < r < D/2, the analogue of Theorem 17.1 is false uniformly
under the conditions

                      mean((µ/a)r ) ≤ 2,              1 ≤ a ≤ 2µ,           mean(a) = µ.

Proof. Choose a fixed integer ℓ > 3D/c, and put P = 2ℓ + 2, B = (2ℓ + 1)D . The triangular
window t(s) = (1 − |s|/ℓ)+ has finite sums

                                                       (d− t)2 = 2/ℓ,                 (d+ d− t)2 = 6/ℓ2 .
              X                                  X                                X
        T =       t2 = (2ℓ2 + 1)/(3ℓ),     V =                              W =

For a product window ψy (x) = i t(xi − yi ) and nonzero actual adjoint H, the actual curl
                                    Q

U1 = d−                −
      2 ψy H, U2 = −d1 ψy H, other components zero, has backward divergence zero. Its field
support and all nonzero forward-gradient start sites lie in the box y + [−ℓ, ℓ]D . Direct separable
sums give

                                     E0 (U )   W          V 3 6(D − 1)   3D
       ∥U ∥2 = 2V T D−1 ∥H∥2 ,            2
                                             =   + (D − 1) = +   2
                                                                       ≤    < c.
                                     ∥U ∥      V          T ℓ  2ℓ + 1     ℓ

Take sufficiently large multiples n of P , set µ = n2 and J = ⌊nD−2r /B⌋. These J boxes fit on
the separated P -grid eventually, since P D ≤ Bn2r . They satisfy J ≥ nD−2r /(2B) → ∞. Put


                                                        24
s = BJ/nD ≤ µ−r and set a = 1 on their union, a = A = (µ − s)/(1 − s) elsewhere. Eventually
s ≤ 1/2, so

            mean(a) = µ,      1 ≤ a ≤ 2µ,    A ≥ µ,       mean((µ/a)r ) ≤ smr + 1 ≤ 2.

Each curl’s gradients start only in its weak box. The actual J-dimensional span has that
same Rayleigh quotient, because both field and gradient supports are disjoint. Section 1 forces
dim F ≥ J, whereas the target maximum at µ = n2 is 1. This proves the refutation using original
nonlinear data.

    Together the two theorems give the sharp inverse-moment exponent for this specified family
of global scalar conditions. They do not identify all sufficient coefficient criteria, prove a physical
coefficient hypothesis, or impose spatial locality on C.


19     Spatial means and the critical dyadic obstruction
For a partition P into integer rectangles, its actual normalized means are
                                        q
                         CP (U )R,j =    |R| meanR Uj ,      dim F = h#P.

A full dyadic cube tree splits each selected cube into all 2D equal children and retains unsplit
siblings. The origin of the torus coordinate cube may be translated. This class excludes arbitrary
anisotropic rectangle cuts and compressed observations.

Proposition 19.1. There are fixed critical-moment profiles with target maximum 1 for which
every coercive full dyadic cube-tree mean partition has Ω(log n) leaves, even after choosing a
translated origin. The same profiles admit an explicit constant-size rectangular mean partition
satisfying the global inequality for every actual cochain.

Proof. Keep ℓ > 3D/c fixed. Choose a dyadic L = 2q ≥ 4ℓ + 2, put γ = max(1, c/4), n = 2J
with J ≥ q + 1, µ = γn2 , and S = {0, . . . , L − 1}D . Set a = 1 on S and a = A = (µ − s)/(1 − s)
elsewhere, s = LD /nD . Then 1 ≤ a ≤ 2µ, its mean is exactly µ, and

                              mean((µ/a)D/2 ) ≤ 1 + LD γ D/2 =: M0 .

All these parameters except n are fixed, and the target maximum is 1.
    In the hypothetical complete level j∗ = J − q of any translated dyadic grid, cells have side L.
Each coordinate interval of S meets at most two such cyclic grid intervals, so one intersection
has integer length at least L/2 ≥ 2ℓ + 1. Taking these intersections independently places a
whole gradient-start box for a compact curl inside S and inside one level-j∗ cell. If the proposed
partition had maximum depth at most j∗ , that cell would lie in one actual leaf. The curl then
has zero means on every leaf, since each component has total sum zero, yet its weighted Rayleigh
quotient is < c. This contradicts coercivity. A single zero-extended window needs no packing
divisibility assumption on n; n ≥ 2L suffices here. The field may depend on the partition, since
coercivity is asserted for every field. Thus maximum depth is at least J − q + 1, and the full-arity
tree identity gives
                                    #P ≥ 1 + (2D − 1)(J − q + 1).                               (22)



                                                  25
   For a successful unrestricted partition, isolate all LD vertices of S as singletons, and use the
D disjoint complement rectangles
                            Ri = [0, L − 1]i−1 × [L, n − 1] × [0, n − 1]D−i .
Coverage follows from the unique first coordinate outside [0, L − 1]. Every internal edge starts
at a strong vertex with coefficient A. On a length-l interval, counting variance and path
Cauchy–Schwarz give
                                X              l(l − 1) X
                                   ∥u − ū∥2 ≤             A∥du∥2 .
                                                  4A
Indeed the path resistance is at most (l − 1)/A, and a cut at t is crossed by t(l − t) ≤ l2 /4
pairs in the variance identity. Product-variance tensorization on original fibres yields a rectangle
constant n2 /(4A), with no extra factor D. Singletons have zero residual, internal edge sets are
disjoint, and omitted edges have positive energy. Since cn2 /(4A) ≤ c/(4γ) ≤ 1, exact orthogonal
decomposition proves
                       c∥U ∥2 ≤ Qw (U ) + c∥CP (U )∥2 ,         #P = LD + D.
These rectangles have potentially unbounded aspect ratio; they leave the cube-tree class.

   The general critical moment question for unrestricted rectangular means remains open.
Changing only the stopping rule within full cube trees cannot resolve it. Classical weighted
Sobolev inequalities [14] also yield block observations for inverse moments of finite order strictly
greater than D/2; the dossier contains the explicit balanced-box proof. Proposition 19.1 explains
why its critical tree-counting loss cannot be removed merely by choosing a better cube-tree
stopping criterion.


20     What a spatial observation proof must still establish
The preceding positive spectral result does not construct a rectangular mean map. Three
further checks prevent substitutions for that missing construction. They concern local geometry,
the penalty coefficient, and support of observations, respectively. They are collected here as
limitations of the same dossier, not as additional papers.

20.1    Critical inverse mass does not remove rectangle geometry
For a rectangle R of side lengths li , set V = i li , L = maxi li , κ = L2 /V 2/D and ηR = R a−D/2 .
                                               Q                                           P

The endpoint Sobolev estimate on balanced cubes, with q = 2D/(D + 2), transfers to arbitrary
rectangles by repeated coordinate reflection and gives
                               X                             2/D
                                    |u − ūR |2 ≤ AD D2/D κηR Ea,R (u).                          (23)
                                R

Here the energy uses original internal edges and their actual starting-vertex weights. The full
reflection multiplicities and graph adapters to the classical estimate [14, Section 2.2] are preserved
in the companion geometric note; this is an analytic adapter, not a new Lean theorem.
    The factor cannot be discarded even for uniform coefficients. With u(x) = xi − (L − 1)/2
along a longest side, direct sums give
                       X
                            u2 = V (L2 − 1)/12,         Ea,R (u) = aV (L − 1)/L.
                        R


                                                   26
                                   2/D
Their ratio is L(L + 1)/(12a) ≥ κηR /12. On the thin rectangle of lengths (L, 1, . . . , 1), choosing
a = L2/D makes ηR = 1 while this ratio diverges. Thus compressing a cube-tree chain into thin
rectangles cannot simply reuse a shape-independent inverse-mass certificate. This prescribed-
block test does not defeat every global partition: omitted crossing edges and a different partition
may help. The successful partition in Proposition 19.1 is not contradicted.

20.2    Fixed and free penalties are different obligations
Let C be normalized means on a fixed partition of a finite real Euclidean space. Then CC ∗ = I;
P = C ∗ C is the orthogonal block-mean projection and Q = I − P . For the actual positive
stiffness La , write the blocks on ran P ⊕ ran Q as

                          A = P La P,      B = P La Q,       D0 = QLa Q.

Positivity implies ker A ⊆ ker B ∗ : otherwise the energy of tp + v would have a nonzero linear
coefficient with zero quadratic coefficient in t. Completing the square with the finite spectral
pseudoinverse A† shows

                      La + cP ≥ cI       ⇐⇒    D0 − B ∗ A† B ≥ cI on ran Q.                     (24)

Indeed the first inequality is exactly La − cQ ≥ 0, and its quadratic form is ⟨p + A† Bv, A(p +
A† Bv)⟩ + ⟨v, (D0 − cI − B ∗ A† B)v⟩. This is classical shorted-operator algebra [12]; it supplies no
spatial partition or target count. In particular D0 ≥ cI alone is insufficient.

Proposition 20.1. On the four-cycle with edge weights (1, 6, 4, 1) and blocks {0, 1}, {2, 3},
coercivity holds on zero block sums with c = 19/5, but La + cP ≥ cI fails.

Proof. For v = (x, −x, y, −y), with the counting Euclidean norm,
                                                          2
                                 19      17   35                   84 2
                                                
                         Ea (v) − ∥v∥2 =    x+ y               +      y ≥ 0.
                                 5        5   17                   85
The actual normalized observation is
                                              √              √ 
                              Cu = (u0 + u1 )/ 2, (u2 + u3 )/ 2 .

For u = (19, −9, −5, −5)/14, direct exact evaluation gives

                       Ea (u) = 52/7,    ∥u∥2 = 123/49,     ∥Cu∥2 = 25/49,

and hence Ea (u) + (19/5)∥Cu∥2 − (19/5)∥u∥2 = −6/35. The weights have mean 3 and lie between
1 and 6. Ten focal Lean theorems preserve the constructed weights, normalized observations,
projection identities, kernel square identity and exact negative witness; Section 22 identifies the
successful immutable source. This is a finite four-cycle result, not a proved embedding into the
full physical divergence-zero kernel.

    For the original class allowing an arbitrary finite K, put J = D0 − cI. The necessary and
sufficient condition is instead

                   ∃K ≥ 0 : La + KP ≥ cI         ⇐⇒      J ≥ 0 and B ker J = 0.                 (25)


                                                 27
Necessity follows by testing v ∈ ker C, then v + tp with v ∈ ker J. For sufficiency, B ker J = 0
implies B ∗ p ∈ ran J. Completing the square in v + J † B ∗ p leaves A + (K − c)I − BJ † B ∗ , so
K = c + ∥BJ † B ∗ ∥ suffices. In particular a proved all-cochain margin D0 ≥ (c + ϵ)I gives
K = c + ∥La ∥2 /ϵ. For actual a ≤ 2µ, the elementary edge estimate |r − s|2 ≤ 2|r|2 + 2|s|2 gives
∥La ∥ ≤ 8Dm, including the parallel edge occurrences at n = 2. A margin 2c therefore permits
K = c + 64D2 µ2 /c, without increasing the number of observations. No margin or partition is
proved by this conditional implication. Ordinary block averaging need not preserve divergence,
so an estimate only on the physical kernel cannot silently replace the all-cochain hypothesis in
this decomposition.                                                       √
    Even free K needs care at equality. On the same cycle let s = 85, c∗ = (17 − s)/2 and
v = (7, −7, 6 − s, s − 6). Its kernel defect at c∗ is zero, since for general (x, −x, y, −y) it equals
(s − 6)[x + 7y/(s − 6)]2 . For p = (δ/2, δ/2, −δ/2, −δ/2) the full defect is

            Ea (v + p) + K∥C(v + p)∥2 − c∗ ∥v + p∥2 = (7 + K − c∗ )δ 2 − 10(13 − s)δ.

For each finite K ≥ 0 a sufficiently small positive δ makes it negative. This additional equality
example is exact analytic algebra and finite diagnostic evidence, not one of the ten Lean theorems
of Proposition 20.1.

20.3    Sparse point samples cannot replace stable averages
For uniform a = µ, if an observation depends only on vertex values on a set S, |S| = s, and
C(0) = 0, then the scalar field u = 1 off S and 0 on S has zero observation. At most 2Ds
forward-edge occurrences cross S, so Eµ (u) ≤ 2Dms. Consequently all-cochain coercivity requires

                                                  cnD
                                           s≥           .
                                                2Dm + c
For an actual divergence-zero test, fix a component direction j and let the field be constant along
every j-line, equal to zero on each line meeting S and one on the other lines, in one fixed internal
coordinate. There are at most s hit lines. Its backward divergence is zero, its norm squared is at
least n(nD−1 − s), and transverse crossing energy is at most 2(D − 1)mns. Thus necessarily

                                                cnD−1
                                        s≥                 .
                                             2(D − 1)µ + c

If every transverse line is hit, the second bound is immediate without a nonzero test. These
bounds give the required obstruction: at a = µ = n2 and critical moment M = 1, bounded
samples fail for all cochains when D ≥ 3 and for these physical tests when D ≥ 4. For the
same uniform coefficients one global mean succeeds for 0 < c ≤ 16, by the nonzero Fourier gap
n2 λ(k) ≥ 16. This comparison rules out a point-sampling shortcut, not rectangular averages or
singletons supplemented by complementary block means. A nonlinear local observation is tested
on sufficiently small multiples of these fields.


21     Constructive rectangular bounds and their limits
Retain µ ≥ 1, 1 ≤ a ≤ 2µ, exact mean µ, (16), and p = D/2. All assertions in this section
remain analytic.


                                                 28
21.1    A general threshold construction
For an interval of length l, the identity Var(u) = l−1 x<y |u(x) − u(y)|2 and path Cauchy–
                                                               P

Schwarz give coefficient at most l(l − 1)/4 per edge: each crossing pair has distance at most
l − 1, and at most l2 /4 pairs cross any edge. Product variance tensorization therefore yields, for
a rectangle of maximal side L,
                   X                       L(L − 1)             X
                        |u − meanR u|2 ≤                                        |du|2 .               (26)
                    R
                                              4     internal forward edges of R

There is no additional factor D in this tensorization.                 p
    Fix τ ≥ 1. If τ < c/4 use singletons. Otherwise set ℓ = min{n, ⌊2 τ /c⌋} and start with a
grid whose sides have length at most ℓ. Isolate each vertex with a < τ as a singleton. Its current
rectangle minus that vertex splits into at most 2D rectangles by the first coordinate differing
from that vertex. Delete empty pieces and preserve earlier singletons. Remaining rectangles
have a ≥ τ and side at most ℓ. Equation (26), nonnegative omitted edges and normalized-mean
orthogonality give
                                                                        q
                         2                      2
                   c∥U ∥ ≤ Ea (U ) + c∥CP U ∥ ,          (CP U )R,j =       |R| meanR Uj              (27)

for ALL cochains. Singleton residuals vanish, including n = 1; parallel edge occurrences for n = 2
                                                                                      √
are counted separately, and wrap edges can be omitted positively. With Bc = (1 + c)D ,

              |P| ≤ Bc max{1, nD /τ p } + 2D#{a < τ },           #{a < τ } ≤ M nD τ p /µp .
                                                                                      √
The singleton branch satisfies this count since Bc τ −p > 1 there. Taking τ =          µ yields the weaker
general bound
                            dim F ≤ h(Bc + 2DM ) max{1, nD /µD/4 }.

21.2    Every global threshold can lose the target order
Let γ = max{1, c/4}, n = t2 , t ≥ 2, µ = γn2 , b = γn, S = {0, . . . , t − 1}D , and f = n−p . Set
a = b on S, a = A = (µ − f b)/(1 − f ) outside. Then 1 ≤ a ≤ 2µ, the mean is µ, and the critical
moment is less than 2 − f . The target maximum is one. For any global τ ≥ 1, consider the
preceding algorithm with any translated initial grid or excision order, retaining grid boundaries
and every excised singleton. If τ ≤ b, no vertex is weak and the grid volume bound gives
                                            q
                              |P| ≥ nD /(2 b/c)D = (c/(4γ))p nD/2 ,

or the singleton branch is larger. For large n the grid side is less than n. If τ > b, all tD = nD/2
weak vertices remain distinct singletons. Every such threshold therefore loses the target order.
    For the SAME profile retain the whole weak cube and split its complement by the first
coordinate outside it, giving D + 1 rectangles. On S, ct2 /(4b) = c/(4γ) ≤ 1; outside, A ≥ µ and
cn2 /(4A) ≤ 1. Equation (26) proves (27) for this constant-size partition. This is a mechanism
obstruction, not a counterexample to every rectangular partition.




                                                    29
21.3    Supplied scaled cubes attain the target order
Suppose additionally that disjoint integer cubes Sk of side Lk , nonwrapping in one common root,
satisfy for fixed β ≥ 1

                            cLk (Lk − 1)/4 ≤ a(x) ≤ βL2k      (x ∈ Sk ),
                                                                                                   (28)
                                       a(x) ≥ cn(n − 1)/4     (x ∈
                                                                 / ∪k Sk ).

These are extra coefficient and geometric assumptions. Each cluster charges at least β −p to
         −p              p    D    p
   x a(x) ; thus J ≤ β M n /µ .
P

     The solid-fat-object BSP construction of de Berg [11] has linear size in fixed dimension. Its first
stage uses axis-parallel cuts; its second uses object facet planes. For solid axis-aligned cubes both
stages are axis-parallel. Replace Sk = i {bki , . . . , bki +Lk −1} by Qk = i [bki −1/4, bki +Lk −3/4].
                                        Q                                   Q

These are positive-side solid cubes of fixed fatness, strictly disjoint even for touching integer-cell
interpretations; their integer points are precisely Sk and are interior, including when Lk = 1.
     Clip BSP leaves to [−1/2, n − 1/2]D , assign each cut boundary consistently to one child, take
integer points and delete empty cells. If an assigned integer point belongs to Sk , a ball about it
lies in Qk , so the open leaf also meets Qk . Hence one leaf’s integer points belong to at most one
cluster. Refine it with that cube’s 2D facets, at most 3D subrectangles, each inside one cluster
or outside all clusters. Fragmentation is permitted; whole-cluster preservation is unnecessary.
Consequently, for dimension-only AD ≥ 1,

           |P| ≤ AD max{1, J},         dim F ≤ hAD (1 + 2p β p M ) max{1, nD /(1 + µ)p }.

Inside a cluster fragment maximal side is at most Lk , outside at most n. Equations (28) and (26)
prove (27). Projection separation and a high-budget restriction are unnecessary. This uses
classical geometry; it does not derive the supplied cubes from the original moment.

21.4    The exact cube decomposition is not universal
For fixed c, β take arbitrarily large integer n ≥ 3, µ = n, W = {e1 , −e1 }, f = 2/nD , with a = 1
on W and a = A = (n − f )/(1 − f ) elsewhere. Then n < A ≤ 2n, mean a = n, and the critical
moment is less than 2n−p + 1 − f ≤ 2. Choose also n > max{β, 8β/c, 1 + 8/c} and n ≥ c. Every
vertex has a < cn(n − 1)/4, so any family satisfying (28) must cover zero. A side-one cube
containing zero would require A ≤ β < n. A cube of side L ≥ 2 contains at least one of e1 , −e1 ,
in every translated root. Its lower bound forces L2 ≤ 8/c, while its upper bound at zero requires
A ≤ βL2 ≤ 8β/c < n < A. Even allowing overlap cannot repair this exact decomposition.
                                                                                 p
    The SAME profile nevertheless admits a strong grid with ℓ = min{n, ⌊2 A/c⌋} and two
singleton excisions. Equation (27) holds and
                                          √
                      dim F ≤ h 2p (1 + c)D + 4D max{1, nD /(1 + µ)p }.
                                                     


There are at most ⌈n/ℓ⌉D + 4D blocks. If ℓ < n, ℓ ≥ A/c; if ℓ = n, there is one grid
                                                                p

box. Remaining rectangles have coefficient A and weak residuals are singletons. The universal
supplied-cube route is refuted. The original unrestricted rectangular question is neither proved
nor refuted.




                                                  30
22     Evidence provenance and verification limits
The analytic sources, their exact revisions and the executable finite diagnostics are collected in a
hash-allowlisted companion package. Its map gives full SHAs and SHA256 values; short forms
below are identifiers, not substitute hashes.
                 Item                         Source revision   Verification status
                 Actual flat Hodge identity   dfd49d0b0730      earlier formal source
                 Critical spectral theorem    527fcdcd119a      analytic adapters
                 Dyadic spatial separation    fb65a67af360      analytic adapters
                 Higher moment block proof    6dcb893155e5      analytic adapters
                 Exact finite fixture code    4bb460e1537e      own Colab109
                 Full diagnostic report       602ae3f0b59a      finite rational batch

Colab109 checked four actual profiles on (Z/2Z)4 using rational arithmetic. Each normal
and optimized Python mode accepted four profiles and rejected 16 real matrix, inverse or
flow mutations, with matching outputs and exit code zero. It checked the constant mode,
forward symbols, actual pseudoinverse identities, feasible/minimizing flow energy, comparison
inertia, strict low-spectrum multiplicities and noncommuting counts. There are 12 distinct
density examples, evaluated again for each profile: 48 evaluations per mode, not 48 independent
examples.
    All eight files in the diagnostic archive’s inner manifest were rehashed. Runtime execution was
recorded at 17:13:06.300923–17:13:16.201862 UTC on 2 November2026, with automatic runtime
release and zero sessions verified afterwards. Rounded resource units do not prove zero cost. No
local Windows mathematical execution occurred. This single embedded-SHA finite batch is not
two fresh matching clones, a Lean proof, a theorem about arbitrary dimensions or odd lattices,
or independent mathematical review. No new Lean run occurs in this appendix’s PDF assembly.
Operational repository checks on unchanged Lean files do not verify these new analytic proofs.
    There is also subsequent, strictly focal formal evidence. Source 41f8492c6190 supplies the
ten four-cycle theorems and their oracle. Own Colab118 compiled that same source in two fresh
clones; both actual oracle logs and compiled module hashes agree. Each of four normal/optimized
validator runs accepted ten readouts and rejected three real corruptions. All readouts use only
propext, Classical.choice, and Quot.sound. The full archive has 69 manifest files and is
included with the failed Colab116/117 compiler attempts. Source hashes, complete logs and
exact reports are allowlisted. This verifies Proposition 20.1’s finite identities, not the geometric,
shorted-operator, free-penalty or general rectangular adapters. Own Colab115 separately checked
18 finite diagnostics and eight real mutations in each mode of two fresh clones. Finite examples
do not establish their general claims. Section 21 consolidates analytic sources at 0fa0d91000f6,
312f476ea6e5, f52ae344f61f, 1850be2aa6d5 and b348f4488b3a. These new spatial proofs
have no Lean certificate or new numerical verification. PDF assembly does not change that
status. The earlier exact PDF and its assessment remain preserved.


23     Model assessments and review context
The prior analytic-source first self-assessments were 6/10 for the critical spectral note, 5/10 for
the dyadic note, and 5/10 for the exact finite diagnostic package. They apply only to their own
exact source versions. All were by the preparing Codex agent; the served backend identity and
effort were unexposed. They are neither independent model reviews nor human peer review.


                                                 31
No earlier score is inherited by this appendix. The previous appendix PDF and its first exact
assessment remain historical artifacts; their assessment does not transfer to this consolidated
revision. This revision’s first exact-PDF review is a separate SHA-linked sidecar after visual
inspection. No grade-seeking repeated review, editorial acceptance or publication status is
implied.
    The principal limitations and objections are these. The new finite Fourier, inverse, field and
partition adapters are analytic rather than kernel-verified. The classical Rumin–Frank method
and elementary refinement geometry limit any novelty claim; a complete priority comparison is
unfinished. The sufficient theorem uses one shared scalar coefficient profile, and its distribution
condition is not proved from arithmetic means. Spectral coordinates are global; unrestricted
critical rectangular means remain unresolved. Exact finite diagnostics cover a small selected
family, and some count bounds are loose. The constants are safe rather than sharp. This
appendix makes no statement about an interacting or continuum physical mass gap. PR29
remains 20/41 and TermSource=0.


24     The single remaining bounded question
For fixed D ≥ 3, c > 0, Nc ≥ 2, M , do all actual scalar profiles 1 ≤ a ≤ 2µ, exact mean
µ, satisfying (16), admit (17) using normalized means on an unrestricted axis-aligned integer
rectangular partition? The mechanism must leave full cube trees, for example through anisotropic
cuts with a proved variance bound. A falsifier must defeat every such rectangular partition,
not merely every dyadic cube tree. After three substantive units without a proved reduction
or useful falsifier, the route must be changed or its concrete blocker identified. Formalization
and consolidation of the existing results are preserved work, not additional active new research
questions.


References
 [1] L. Eriksson, Exact-Kernel Fourier Families Obstruct Every Penalty Factored Through a Block Map in
     a Flat Lattice Gauge Form, ai.viXra 2608.0015v1 (2026), AIRR ARR-2026-7EPM3V3DP796BBRR
     v1. https://airr.science/papers/ARR-2026-7EPM3V3DP796BBRR/versions/v1/. Historical
     import, not peer reviewed or assessed by AIRR; checked 30 October 2026.

 [2] J. Dodziuk, Finite-difference approach to the Hodge theory of harmonic forms, American Journal of
     Mathematics 98 (1976), 79–104. https://doi.org/10.2307/2373615. Institutional source:
     https://academicworks.cuny.edu/gc_pubs/180/.

 [3] A. Albert, Conditions for Positive and Nonnegative Definiteness in Terms of Pseudoinverses, SIAM
     Journal on Applied Mathematics 17 (1969), 434–440. https://doi.org/10.1137/0117041.

 [4] D. Carlson, E. Haynsworth and T. Markham, A Generalization of the Schur Complement by Means
     of the Moore–Penrose Inverse, SIAM Journal on Applied Mathematics 26 (1974), 169–175.
     https://doi.org/10.1137/0126013.

 [5] J. Dimock, Covariant Axial Gauge, arXiv:1410.2798v2 (2014).
     https://arxiv.org/abs/1410.2798v2.

 [6] Y. Kudryashov and Mathlib contributors, Implicit function theorem, Mathlib source at commit
     07642720480157414db592fa85b626dafb71355b. Pinned primary formal source, particularly
     HasStrictFDerivAt.to_implicitFunction and its exact level-set identity; inspected 30 October


                                                 32
    2026. This attributes the classical parametrization; the separately pinned sector formalizations are
    identified in the evidence section.

 [7] D. A. Spielman, Graphs, Vectors, and Matrices, Bulletin of the American Mathematical Society 54
     (2017), 45–61. Author-hosted primary exposition:
     https://cs-www.cs.yale.edu/homes/spielman/PAPERS/bull1557.pdf.

 [8] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, Markov Chains and Mixing Times,
     second edition, American Mathematical Society (2017), Chapter 13. Author-hosted text:
     https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf.

 [9] D. Zelazo and M. Bürger, On the Definiteness of the Weighted Laplacian and its Connection to
     Effective Resistance, arXiv:1408.2187v1 (2014), Theorem III.3.
     https://arxiv.org/pdf/1408.2187.

[10] Y. Lin, S. Wan and H. Zhang, Connection Laplacian on discrete tori with converging property,
     arXiv:2403.06105v1 (2024), Theorem 1.2. https://arxiv.org/html/2403.06105v1. The
     sin-squared discrete-torus spectrum is attributed prior work, not a new general spectral principle
     here.

[11] M. de Berg, Linear Size Binary Space Partitions for Uncluttered Scenes, UU-CS-1998-12 (1998),
     Section2.1, Lemmas2.1 and2.4, Theorem2.5 and Corollary2.9.
     https://ics-archive.science.uu.nl/research/techreps/repo/CS-1998/1998-12.pdf.

[12] W. N. Anderson, Jr. and G. E. Trapp, Shorted Operators. II, SIAM J. Appl. Math. 28(1) (1975),
     60–71. https://doi.org/10.1137/0128007.

[13] R. L. Frank, Cwikel’s theorem and the CLR inequality, arXiv:1206.3325v1 (2012), Section2,
     Theorem2.1, Corollary2.2, Lemmas2.4–2.5. https://arxiv.org/abs/1206.3325.

[14] S. Andres, J.-D. Deuschel and M. Slowik, Harnack inequalities on weighted graphs and some
     applications to the random conductance model, arXiv:1312.5473v6 (2019), Section2.2, equation(2.5)
     and Proposition2.1. https://arxiv.org/abs/1312.5473.




                                                  33
