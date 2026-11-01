# Coarse information and finite rank obstructions for flat lattice Hodge forms

Working paper — not admitted to the AIRR accepted collection. Exact canonical15page PDF e5e9ddcf…4b220e05. [First exact-v4 preparing-agent assessment:7/10](SCORED-ASSESSMENT.md), with rubric, complete objections and model/context disclosure. This is not an independent review, an AIRR frontier-model gate grade or acceptance.

The frozen PDF states candidate/not deposited as of its preparation on31October; native deposit and author permission followed on1November2026. These later events do not change its bytes. No later volume-density/support-local results are attributed to this version.

Canonical source: paper.pdf. Extracted text below; consult the exact PDF for mathematical layout.

         Coarse information and finite rank obstructions
                      for flat lattice Hodge forms
                                            Lluis Eriksson

                  31 October 2026 — candidate revision v4, not deposited


                                                Abstract
         On a finite periodic lattice with unit spacing, a flat Hodge form cannot have a positive
     coercivity constant uniform under refinement if it is supplemented only by linear observations
     in a fixed finite-dimensional real space and linear fine-space repairs of uniformly bounded rank.
     The linear observations may vary arbitrarily with the refinement, and their penalty need only
     vanish at zero. We prove the same obstruction directly on kernels of uniformly bounded rank
     constraints. The proof constructs a real physical Fourier subspace of dimension 2(2R + 1)d
     with Hodge energy at most 4π 2 dR2 /n2 times its squared norm. Its intersection with the
     unobserved directions gives a necessary rank budget. We also explain why this budget is not
     sufficient, using a two-dimensional cross-coupling example and a classical complete criterion
     for a fixed map. The Fourier construction, finite budget, and uniform obstructions have
     Lean proofs. We also construct derivative repairs, prove a differentiable-observation tangent
     obstruction, and derive an exact nonlinear regular-sector obstruction using the implicit
     function theorem. The operator, full-space tangent and later regular-sector endpoints have
     separately pinned Lean evidence; the fixed-map criterion remains analytic here. We derive
     output-rank divergence on the actual divergence-free space under a subquadratic directional
     spatial mean of nonnegative repair weights, allowing their pointwise maximum to be large. A
     constructed quadratic-weight mean observation and explicit penalty counterexamples delimit
     this result. These are finite flat statements, with no interacting or continuum mass-gap claim.


1    Purpose and relation to the existing record
This text consolidates a continuation of the exact-kernel obstruction in [1]. That paper exhibits
fields in the kernel of a particular line-integral block map. Changing the map can remove a
particular witness. Here the obstruction depends instead on the amount of coarse information: a
whole low-energy subspace is too large to be seen by a fixed-dimensional measurement together
with a bounded-rank repair. The map need not factor through the original block variable, be
local, or obey a norm bound; it is real-linear in the unrestricted-penalty results. The penalty
applied to its output may be nonlinear. Later sections treat differentiable observations with a
locally upper-quadratic penalty and exact nonlinear regular sectors. The restricted-sector result
is proved separately and does not follow merely from failure of an estimate on the full space.
    Fourier diagonalization, rank-nullity and finite-dimensional Schur complements are classical.
For the singular Schur complement and pseudoinverse background, see Albert and Carlson–
Haynsworth–Markham [3, 4]. Finite-difference Hodge theory has a long history; Dodziuk’s work
[2] provides historical context, rather than this paper’s specific lattice normalization. We make
no claim to a new general spectral principle or an exhaustive priority search. The contribution is


                                                    1
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

The last equality is finite translation invariance. The exclusive two plaquette incidences and the
divergence term account for every direction exactly once, with no extra factor two.




                                                        2
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

forces CP (ℓ) ≥ λ−1       2     2
                   ℓ ≥ ℓ /(4π ). No fixed CP > 0 before all block sides can work. This includes
                2
Ψℓ (y) = ∥Tℓ y∥ for arbitrary linear postconditioners, and all critical or faster scalar rescalings.
There is no regularity or sign assumption on the scalar function Ψℓ .
    The original spectral strengthening is retained analytically. For 1 ≤ r ≤ R ≤ ⌊(ℓ − 1)/2⌋,
replace the profile by ι(ce2πirxq /ℓ ), c ∈ C. These are mutually orthogonal real two-dimensional
spaces in ker Qℓ . Derivative orthogonality must be checked too: every forward difference multiplies
a character by its frequency multiplier, so the same root-of-unity Gram sum annihilates cross
terms between distinct frequencies. Thus for Hℓ = K0,n + (Tℓ Qℓ )∗ (Tℓ Qℓ ) the sum of these
spaces has dimension 2R and maximum Rayleigh quotient at most 4 sin2 (πR/ℓ) ≤ 4π 2 R2 /ℓ2 .
Finite-dimensional min–max gives µ2R (Hℓ ) ≤ 4π 2 R2 /ℓ2 . Taking R = ⌊ℓα ⌋, 0 < α < 1, for
sufficiently large ℓ, yields a growing cluster below 4π 2 ℓ−2(1−α) . Eigenvalue language is restricted
to this linear self-adjoint operator, not applied to a general nonlinear penalty.



                                                      3
                                                e ℓ , linear postconditioner Tℓ and positive
    Finally, for any linear changed measurement Q
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
then εℓ = ℓ ηℓ . In dimension four and with Vℓ = 0, leakage o(ℓ−1 ) cannot even repair this
        2     d−2  2

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
Thus output dimension one suffices even when Qn = 0. No finite local quadratic upper constant
for Φ exists, since c|y|/y 2 = c/|y|. Likewise, C(A) = ∥A∥3/2 and Φ(y) = c|y|4/3 are both C 1 with
zero derivatives at zero, yet their composition is exactly quadratic. These are complete analytic
counterexamples, not new Lean claims.
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


10     Why dimension is not a sufficiency criterion
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

Proposition 10.1. A finite real-valued function Φ with Φ(0) = 0 can make ⟨x, Bx⟩ + Φ(Cx) ≥ 0
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

    For a concrete counterexample let H = diag(0, 2), c = 1 and C(x, y) = x + y. On ker C,
⟨x, (H − I)x⟩ = 0, and C detects the negative eigendirection of H − I. Nevertheless, on (t, 1 − t)
the repaired form is 1 − 2t + Φ(1), unbounded below for every finite Φ(1). Kernel nonnegativity
and low-mode detection alone do not suffice; cross-coupling must be checked.

                                                11
11     Operator scaling and the actual consumer
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


12     Formal evidence and publication context
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
The corrected map is declaration-map.json and the preserved evidence is reproducibility/.
Exact source SHAs, not moving branch heads, identify the formal claims. The revised map and
manuscript have their own revision SHA in the accompanying package.
    The geometric and Fourier modules are ordinary proof dependencies, not assumptions about
a newly supplied band. Each development stage has complete same-source fresh-clone Colab
evidence. For the uniform endpoints the tested source is

                                                 12
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

Its two own fresh Colab Linux clones 076/076b pass six exact standard-axiom reports and all
nine stages. Compiled module SHA-256 is
            28fcc004795a1d8ab74ca87b5e67cdf90f557551bc02b1bb912da38324c26e50.

Raw oracle and LF-source-manifest hashes also match; full records and the strict mutation-tested
validator are preserved in the mean-weight reproduction package. The proof composes the actual
character strip, its exact trace, positivity, local derivative-kernel bound and multiplier estimate;
these are derived lemmas, not desired conclusions supplied as hypotheses. Nonnegative weights,
fixed positive c and the quadratic penalty upper bound remain. The constructed quadratic-weight
mean observation instead uses tested source

                                                13
                          7f37d6437a8f69a1d3fddf3dc0bcfad74c6bf9b6.

It has two same-source fresh-clone reproductions 067/067b with six exact standard-axiom reports
and matching compiled, raw-oracle and LF-source hashes. The formal output is an actual fixed
finite-dimensional type; the displayed numeric dimension and nonoptimal path explanation are
not additional oracle endpoints. The penalty examples and regularity tradeoff are analytic only.
Classical quadratic-form, Fourier and trace mechanisms, as discussed in [7], establish no new
general principle or priority here.


Model assessments and review context
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
    This v4 candidate adds the mean-weight theorem and quadratic boundary construction,
with later separately anchored formal sector results and analytic penalty counterexamples. No
previous report, score or approval is an assessment of these new bytes, and no new external
model has reviewed this candidate. The preparing agent’s displayed mathematical arguments,
source inspections and eventual visual layout checks are not independent review. The formal
results above are separately anchored; the whole manuscript is not machine checked.
    Lluis Eriksson is both author and AIRR operator. The current public v3 is a Working paper,
not admitted to the AIRR accepted collection, released on 31 October 2026 under CC BY 4.0
with CC0 metadata. Its exact PDF SHA-256 is
            c9de923a66038ed66c3f68ecf8256b3f738a3ccf27e41f77e470bf7dc3efb5b9.

Public v1 and v2 remain preserved. This v4 candidate has not been deposited, accepted or
published. No previous assessment, public license permission or exact-artifact deposit grant is
represented as covering the new PDF bytes. No external model has assessed this candidate. The
full prior reports and objections remain version-specific; no score or approval is inherited. No
new human peer review or independent organizational review is claimed.


References
[1] L. Eriksson, Exact-Kernel Fourier Families Obstruct Every Penalty Factored Through a
    Block Map in a Flat Lattice Gauge Form, ai.viXra 2608.0015v1 (2026), AIRR

                                                14
   ARR-2026-7EPM3V3DP796BBRR v1.
   https://airr.science/papers/ARR-2026-7EPM3V3DP796BBRR/versions/v1/. Historical
   import, not peer reviewed or assessed by AIRR; checked 30 October 2026.

[2] J. Dodziuk, Finite-difference approach to the Hodge theory of harmonic forms, American
    Journal of Mathematics 98 (1976), 79–104. https://doi.org/10.2307/2373615.
    Institutional source: https://academicworks.cuny.edu/gc_pubs/180/.

[3] A. Albert, Conditions for Positive and Nonnegative Definiteness in Terms of Pseudoinverses,
    SIAM Journal on Applied Mathematics 17 (1969), 434–440.
    https://doi.org/10.1137/0117041.

[4] D. Carlson, E. Haynsworth and T. Markham, A Generalization of the Schur Complement by
    Means of the Moore–Penrose Inverse, SIAM Journal on Applied Mathematics 26 (1974),
    169–175. https://doi.org/10.1137/0126013.

[5] J. Dimock, Covariant Axial Gauge, arXiv:1410.2798v2 (2014).
    https://arxiv.org/abs/1410.2798v2.

[6] Y. Kudryashov and Mathlib contributors, Implicit function theorem, Mathlib source at
    commit 07642720480157414db592fa85b626dafb71355b. Pinned primary formal source,
    particularly HasStrictFDerivAt.to_implicitFunction and its exact level-set identity;
    inspected 30 October 2026. This attributes the classical parametrization; the separately
    pinned sector formalizations are identified in the evidence section.

[7] D. A. Spielman, Graphs, Vectors, and Matrices, Bulletin of the American Mathematical
    Society 54 (2017), 45–61. Author-hosted primary exposition:
    https://cs-www.cs.yale.edu/homes/spielman/PAPERS/bull1557.pdf.

[8] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, Markov Chains and Mixing
    Times, second edition, American Mathematical Society (2017), Chapter 13. Author-hosted
    text: https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf.




                                              15
