# Exact Classical Rate–Distortion for Phase-Lifted Generalized Coherent States

**Author:** Lluis Eriksson  
**ARR ID:** ARR-2026-6XH6JAS5ZA934A6J  
**Version:** v1

> Machine-readable rendition extracted from the canonical PDF. Mathematical typography may be degraded; verify formulas and quotations against `paper.pdf`.

Exact Classical Rate–Distortion for Phase-Lifted
Generalized Coherent States
Cartan-product Laplace rigidity, universal radial envelopes,
and Slater-determinant transitions
Lluis Eriksson
Independent Researcher, Sweden
lluiseriksson@gmail.com
August 14, 2026
Abstract
Let Vλ be a finite-dimensional irreducible unitary representation of a compact connected
semisimple group, and let X be uniform on the phase-lifted orbit of a highest-weight vector.
We determine the classical Shannon rate–distortion function of X under squared ambient loss
when the description alphabet is arbitrary standard Borel and the decoder is not restricted to
the orbit. The known integer-index generalized Lieb–Wehrl theorem has a decisive information-
theoretic consequence: a Cartan-product identity makes coherent rays maximize the overlap
Laplace transform at every field and every fixed report norm. The full vector problem therefore
reduces exactly to
Cλ(s) =e −s max
0≤b≤1
e−sb2
Lλ(2sb), L λ(κ) =
X
m≥0
(κ2/4)m
(m!)2 dimV mλ
,
and Rλ(D) = sups≥0{−sD−logC λ(s)}. Covariant tilted channels attain exposed points,
while a revealed flag mixing active radii attains every nonexposed point. We derive a universal
representation-dimensional criterion for discontinuous directional- information onset and a
sharp root-system high-fidelity constant. For Vλ = ΛkCn, the sources are phased fermionic
Slater determinants. Their normalizer is an explicit k−1Fk function, their squared Pl¨ ucker
overlap is a product of independent beta variables, and every interior family 2 ≤k≤n− 2
with n≥ 6 has a discontinuous first activation. A separate phase-invariant corollary gives
the intrinsic Pl¨ ucker-distortion frontier on the projective coherent orbit. These are classical
compression theorems for amplitude coordinates, not quantum rate–distortion coding or a
statement about click-only Born data.
1 Introduction
Generalized coherent states form the closed projective orbit of a highest-weight ray. They
include spin coherent states, bosonic product states, fermionic Slater determinants, and Pl¨ ucker
embeddings of complex Grassmannians. Their localization properties are governed by Wehrl
and R´ enyi–Wehrl moments. Sugita proved that coherent states maximize every integer Husimi
moment for compact semisimple groups [1]; the quadratic equality set is the highest-weight orbit
characterized by the Kostant–Lichtenstein quadrics [2, 3]. Those results are inputs here, not
claims of priority.
We ask a different question. Draw a coherent state uniformly, attach an independent phase,
and encode the resulting vector using completely classical memory. How many nats are required
to reconstruct it with a prescribed squared Euclidean error if the decoder may report any vector,
not merely another coherent state? The permission to leave the orbit is substantive. Conditional
1

means live in the coherent-state orbitope and can shrink radially; their competition produces
linear faces and discontinuous information onsets absent from a same-manifold codebook problem.
Rate–distortion on invariant groups and high-resolution bounds on Grassmann manifolds
are classical subjects [4–6]. For Vλ = Cn the phase-lifted source is exactly the real unit sphere
S2n−1, and our k = 1 formula reduces, with radius one and natural logarithms, to the exact
sphere solution of Dytso and Cardone [7]. Quantum rate–distortion instead optimizes quantum
communication resources and quantum distortion observables [8, 9]; that is not the task considered
here.
The paper’s contribution begins after the known coherent-state moment extremum. We prove:
1. the all-field fixed-radius Laplace order obtained by positive phase–Bessel resummation of
Sugita’s integer-moment extremum, together with its exact equality classification;
2. an exact classical Shannon frontier over the full coherent-state orbitope, including covariant
equality and flagged attainment at nonexposed distortions;
3. a universal criterion dimV 2λ < 1
2(dimV λ)2 forcing a discontinuous first activation;
4. a high-fidelity constant expressed directly by positive roots and the highest weight;
5. an explicit all-(n, k) Slater-determinant specialization with a hypergeometric normalizer,
beta-product overlap law, and a complete classification of the sign responsible for first-order
onset.
The scalar formula is exact even when the radial maximizer is not unique. We do not claim a
unique positive branch or exclude later radial exchanges for every representation. That distinction
keeps the result independent of unproved phase-diagram assumptions.
2 Coherent orbits and the unrestricted problem
Let G be a compact connected semisimple Lie group, let ( π, Vλ) be a nontrivial finite-dimensional
irreducible unitary representation with dominant highest weightλ, and choose a unit highest-weight
vectorv λ. We use the underlying real Hilbert structure
(a, x)R = Re⟨a, x⟩,∥a∥ 2 =⟨a, a⟩.
Definition 2.1(Phase-lifted coherent orbit).The source manifold and its orbitope are
Mλ ={e iθπ(g)vλ :θ∈R/2πZ, g∈G},B λ = conv(Mλ).
The probability µλ is the pushforward of normalized Haar measure on G and normalized Lebesgue
measure on the phase circle.
The independent phase makes EX = 0 for X∼µ λ. It also gives 0 ∈ Bλ, and convexity gives
∥a∥ ≤1 for everya∈ Bλ.
Let Z take values in an arbitrary standard-Borel space and let a : Z→V λ be Borel. We define
Rλ(D) = infI(X;Z),E∥X−a(Z)∥ 2 ≤D,(2.1)
where the infimum is over all joint laws with X-marginal µλ. Mutual information and logarithms
are in nats.
Lemma 2.2(Posterior-mean reduction).The infimum in (2.1) is unchanged if the decoder is
required to lie in Bλ. More precisely, every decoder can be replaced by bX(Z) = E[X|Z ] ∈ Bλ
without increasing distortion or mutual information.
2

Proof. Finite dimensionality makes the Bochner conditional expectation well-defined. Conditional
least squares gives
E[∥X−a(Z)∥ 2 |Z] =E[∥X− bX(Z)∥2 |Z] +∥a(Z)− bX(Z)∥2.
The conditional mean belongs to the closed convex hull of the essential range of X, which is Bλ.
It is a measurable function ofZ, so data processing cannot increase mutual information.
This unrestricted formulation is stronger than a codebook restricted toM λ. The report can
be a proper mixture of coherent states, but theorem 3.2 will show that only one radial coherent
direction is needed in the dual optimum.
3 Cartan products and all-field Laplace rigidity
Let Vmλ denote the irreducible Cartan component generated by v⊗m
λ inside V ⊗m
λ , let Pmλ be its
orthogonal projector, and write
dm =d m(λ) = dimV mλ, d 0 = 1.
Lemma 3.1(Cartan moment identity).For everya∈V λ and integerm≥1,
Z
G
|⟨a, π(g)vλ⟩|2m dg= ∥Pmλa⊗m∥2
dm
≤ ∥a∥2m
dm
.(3.1)
Fora̸= 0, equality atm= 2holds exactly when[a]lies on the projective highest-weight orbit.
Proof.The vectors (π(g)v λ)⊗m spanV mλ. The operator
Tm =
Z
G
|(π(g)vλ)⊗m⟩⟨(π(g)vλ)⊗m|dg
vanishes on the orthogonal complement and commutes with the irreducible G-action on Vmλ.
Schur’s lemma makes it a scalar multiple of Pmλ; its trace is one, so Tm = Pmλ/dm. Contracting
with a⊗m gives the identity and the projection bound. For m = 2, equality says a⊗2 ∈V 2λ.
The highest-weight quadratic criterion identifies precisely the coherent rays [2]. This is also the
projection proof underlying the integer-index generalized Lieb–Wehrl theorem [1].
Define the entire even function
Lλ(κ) =
∞X
m=0
(κ2/4)m
(m!)2dm
.(3.2)
Convergence follows already fromd m ≥1 and comparison withI 0(|κ|).
Theorem 3.2(All-field coherent-ray rigidity).For everya∈V λ and realκ,
Z
Mλ
eκRe⟨a,x⟩ dµλ(x)≤L λ(κ∥a∥).(3.3)
Equality holds for every scalar multiple of a coherent vector. Ifκ∥a∥ ̸= 0, equality forcesato lie
on a coherent ray.
Proof.Forz∈C, phase averaging gives
1
2π
Z 2π
0
(Re(eiθz))2m dθ=
 2m
m

4m |z|2m,
and all odd moments vanish. Expand the exponential, apply theorem 3.1, and use
 2m
m

/(2m)! =
1/(m!)2. Every term is nonnegative. Coherent a saturates each projection inequality. Conversely,
equality of the sum at a nonzero argument forces equality of its m = 2 term, and the final claim
follows from theorem 3.1.
The theorem is an all-field consequence of known integer moment rigidity. It is useful because
exponential loss duals require the entire transform, not a fixed R´ enyi index.
3

4 Exact Shannon rate–distortion
Fors≥0 anda∈ B λ of normb,
Z
e−s∥x−a∥2
dµλ(x) =e −s(1+b2)
Z
e2sRe⟨a,x⟩ dµλ(x).(4.1)
Becausebv λ ∈ Bλ for 0≤b≤1, theorem 3.2 makes the supremum exact.
Theorem 4.1(Universal coherent-orbit RDF).Put
Cλ(s) =e −s max
0≤b≤1
n
e−sb2
Lλ(2sb)
o
.(4.2)
Then
Rλ(D) = sup
s≥0
{−sD−logC λ(s)}. (4.3)
This identity holds for arbitrary standard-Borel classical descriptions and all D≥ 0. In particular,
Rλ(D) = 0forD≥1.
At every exposed point, an active radius b is attained by a covariant tilted channel supported on
bMλ. At a nonexposed point, a revealed independent flag mixing at most two active radii attains
the frontier.
Proof. We give the standard-Borel converse and equality construction explicitly. By theorem 2.2,
assume from the outset that every report az lies in Bλ. Regular conditional laws νz = PX|Z=z
exist. For every report az and s≥ 0, the entropy variational inequality gives, with extended
values,
D(νz∥µλ) +sEνz ∥X−a z∥2 ≥ −log
Z
e−s∥x−az∥2
dµλ(x)≥ −logCλ(s).(4.4)
Averaging and using I(X; Z) = EZD(PX|Z ∥µλ) yields I(X; Z) ≥ −sD−logCλ(s). Optimization
in s proves the lower bound. This is the constant Shannon dual written without a hidden finite-
alphabet or absolute-continuity assumption [10, 11].
Fix a maximizing radiusband letYbe Haar onM λ. Define the reverse kernel
dPX|Y=y
dµλ
(x) = e−s∥x−by∥2
Cλ(s) .(4.5)
The denominator is correct because b is active. Averaging the numerator over y gives a G×U (1)-
invariant function of x and is therefore constant on the transitive source orbit. Its integral is
Cλ(s), so the X-marginal of the joint law is exactly µλ. Reporting A = bY , direct evaluation gives
I(X;Y) =−sD b −logC λ(s), D b =E∥X−bY∥ 2.(4.6)
For an interior active radius, differentiation ofK λ(2sb)−sb 2 gives
b=K ′
λ(2sb).(4.7)
The gradient of the log partition at a fixed-norm coherent maximizer is radial, and its radial
component is K′
λ(2sb); hence E[X|Y = y] = by. Thus the displayed report is also the posterior
mean. At b = 0 the same statement follows from phase symmetry; b = 1 is excluded at finite
field below. Thus every distortion in −∂logC λ(s) is attained. If several radii are active, choose
an independent revealed flag J and use the corresponding kernel conditionally on J. Each
component has the same X-marginal, hence I(X; J) = 0 and both distortion and conditional
mutual information mix linearly. One-dimensional convexity requires at most two radii.
At s = 0, b = 0 gives D = 1 and zero rate. As s→ ∞, active radii approach one and the
distortion approaches zero; this follows also from the high-field estimate in theorem 6.2. Convex
closure supplies the endpoints and completes Fenchel equality.
4

An equivalent primal form is useful for geometry. Define the Cram´ er transform and its
squared-radius parametrization by
jλ(b) = sup
κ≥0
{κb−K λ(κ)}, g λ(u) =j λ(√u),0≤u <1.(4.8)
Corollary 4.2(Convex-envelope form).For0≤D≤1,
Rλ(D) = (cog λ)(1−D),(4.9)
where co denotes the lower convex envelope. Every chord is attained by time sharing between two
covariant coherent tilts.
Proof. For a posterior law ν with mean a and b = ∥a∥, entropy variation with the field κa/b and
theorem 3.2 gives D(ν∥µλ) ≥j λ(b). Conditional means satisfy E∥X−E [X|Z ]∥2 = 1 −Eb (Z)2.
The function cog λ is nonnegative, convex, vanishes at zero, and is therefore nondecreasing.
Jensen’s inequality consequently gives
Egλ(b(Z)2)≥E(cog λ)(b(Z)2)≥(cog λ)(1−D),
which is the converse. Conversely, a coherent exponential tilt of parameter κ has mean K′
λ(κ)y,
divergence jλ(K′
λ(κ)), and the invariant source marginal after Haar mixing of y. Strict convexity
makes K′
λ increasing; phase symmetry gives K′
λ(0) = 0. The high-field estimate in theorem 6.1
gives Kλ(κ)/κ→ 1, and convexity then forces K′
λ(κ) → 1 without differentiating its remainder.
Hence it maps κ∈ [0,∞) onto b∈ [0, 1), so all points of gλ are attained. A revealed binary flag
mixing two such joint laws preserves the same source marginal, is independent of X, and attains
every lower-hull chord.
Remark 4.3(Finite-field boundary).The endpoint b = 1is not active at finite s >0. Writing
K = logL and differentiating the radial objective gives2 s[K′(2sb)−b]. Under every finite coherent
tilt the overlap is strictly less than one almost surely, so K′(2s) < 1; moving left from b = 1
strictly increases the objective.
5 A representation-dimensional phase criterion
The radial problem is
ϕs(b) =K λ(2sb)−sb 2, K λ = logL λ.(5.1)
The zero report always has value zero. Its quadratic stability changes ats 0 = dimV λ.
Proposition 5.1(Fourth-cumulant criterion).LetN=d 1 = dimV λ. ForY= Re⟨v λ, X⟩,
EY 2 = 1
2N ,cum 4(Y) = 3
8
 1
d2
− 2
N2

.(5.2)
If d2 < N2/2, the first global activation of a nonzero report occurs at some sc < N with a
radius bounded away from zero. Hence Rλ has a linear coexistence face adjacent to D = 1and a
discontinuous onset of directional information.
Proof.The moments follow from theorem 3.1 and phase averaging. Since
Kλ(t) = t2
4N + cum4(Y)
24 t4 +O(t 6),
the coefficient of b2 in (5.1) is s(s/N− 1). Thus b = 0 is a strict local maximum for 0 < s < N.
At s = N the quadratic term vanishes; if cum4(Y ) > 0, every sufficiently small nonzero b has
ϕN (b) > 0. For small s > 0, zero is the unique global maximizer: |Re⟨a, X⟩| ≤ ∥a∥and
5

Hoeffding’s lemma give Kλ(2sb) ≤ 2s2b2, so ϕs(b) < 0 for 0 < s <1/2 and b >0. Compactness
and continuity therefore give an attained first contact 0< s c < N.
Were positive maximizers at contact to converge to zero, the locally uniform expansion at
sc < Nwould make ϕs(b) < 0 for all sufficiently small nonzero b, a contradiction. The contact
radius is therefore positive. Mixing the zero and positive covariant channels in theorem 4.1
produces the linear face.
This criterion proves existence, not uniqueness, of coexistence. A global one-fold theorem
requires additional information about the full dimension sequence dm and is deliberately not
assumed.
6 Root-system high-fidelity asymptotics
Letρbe the Weyl vector and let
Φ+
λ ={α >0 :

λ, α∨
>0}, p=|Φ +
λ |, A λ =
Y
α∈Φ+
λ
⟨ρ, α∨⟩
⟨λ, α∨⟩.(6.1)
The projective coherent orbit has real dimension 2p; its phase lift has dimensionq= 2p+ 1.
Lemma 6.1(Bessel-weighted polynomial saddle).Suppose dm is given by Weyl’s formula for
Vmλ. Then, witha=p+ 1/2,
Lλ(κ) = 2pAλ√
2π eκκ−a(1 +o(1)),(6.2)
Proof.Weyl’s dimension formula is
dm =
Y
α>0
m⟨λ, α∨⟩+⟨ρ, α∨⟩
⟨ρ, α∨⟩ = mp
Aλ
(1 +O(m −1)).(6.3)
Putz=κ/2 and letM z have probability masses
Pr{Mz =m}= z2m
(m!)2I0(2z) .(6.4)
If N1, N2 are independent Poisson(z) variables, then Mz
d=N 1 | {N1 = N2}. For fixed 0 < ϵ <1,
Poisson Chernoff bounds and Stirling’s lower bound atm 0 =⌊z⌋give
Pr(|N1 −z|> ϵz)≤2e −cϵz,Pr(N 1 =N 2)≥Pr(N 1 =m 0)2 ≥cz −1.(6.5)
Consequently
Pr(|Mz −z|> ϵz)≤Cze −cϵz.(6.6)
The Weyl asymptotic in (6.3) is uniform on every tail interval. On |Mz −z| ≤ϵz, it squeezes
zp/dMz between quantities converging to Aλ as first z→ ∞and then ϵ↓ 0. On the complement,
d−1
m ≤ 1 and (6.6) is exponentially smaller than z−p; the m = 0 mass is also exponentially small.
Hence
Ed−1
Mz ∼A λz−p.(6.7)
Finally Lλ(2z) = I0(2z)Ed−1
Mz and I0(2z) ∼e 2z/
√
4πz, which proves (6.2) with the displayed
constant. This drifting-saddle argument is uniform and does not interchange an unbounded limit
with a merely pointwise Weyl estimate.
6

Proposition 6.2(Sharp high-fidelity constant).AsD↓0,
Rλ(D) = q
2 log q
D − q
2 −log
2pAλ√
2π

+o(1). (6.8)
Proof. By theorem 6.1, K(κ) = κ− (q/2) logκ + log(2pAλ/
√
2π) + o(1). Put a = q/2, C =
2pAλ/
√
2π, andt=δκ. Uniformly fortin compact subsets of (0,∞),
κ(1−δ)−K(κ) =alog(1/δ) +alogt−t−logC+o(1).
The deterministic function alogt−t has its unique maximum at t = a. The same asymptotic
excludes t→ ∞and excludes t→ 0 whenever κ→ ∞, while bounded κ gives only O(1) and cannot
compete with the diverging value alog (1/δ). Hence δκδ →a and direct Legendre optimization
gives
jλ(1−δ) = q
2 log q/2
δ − q
2 −log
2pAλ√
2π

+o(1).
Since D = 1 −b 2 = 2δ + o(δ), this is (6.8) on the deterministic-radius curve. Lower convexification
does not improve its leading term. Indeed, for a mixed squared radius U put ∆ = 1 −U and
assume E∆ = D. On AD = {∆ ≤
√
D}, Markov gives P(AD) = 1 −o (1) and the preceding
asymptotic is uniform. Conditional Jensen for−log ∆ yields
P(AD)E[−log ∆|A D]≥P(A D) log P(AD)
E[∆;A D] ≥P(A D) log P(AD)
D = log(1/D) +o(1).
The complement contributes nonnegatively. This gives the matching lower bound, while the
deterministic choice gives the upper bound. No differentiation of the o(1) saddle remainder is
used.
7 Complex Grassmannians and Slater determinants
Take G = SU (n), Vλ = ΛkCn, and λ = ωk, with 1 ≤k≤n/ 2 by duality. A coherent vector is a
unit decomposable form u1 ∧ ··· ∧uk: a phased fermionic Slater determinant [12]. The projective
orbit is the Pl¨ ucker embedding of GrC(k, n).
Proposition 7.1(Rectangular dimensions and normalizer).Let p = k(n−k )and N =
 n
k

. Then
dm(n, k) =
kY
i=1
(n−k+i) m
(i)m
,(7.1)
and
Ln,k(κ) = k−1Fk
 2,3, . . . , k
n−k+ 1, n−k+ 2, . . . , n; κ2
4

. (7.2)
Fork= 1the empty numerator gives 0F1(;n;κ 2/4), the complex sphere normalizer.
Proof. Apply the Weyl dimension formula to the rectangular highest weight ( mk). Substitution
into (3.2) and cancellation of (1) m = m! gives (7.2). Formula (7.1) is invariant under k↔n−k ,
as required by Hodge duality.
Proposition 7.2(Exact overlap product).If X, Yare independent Haar Slater determinants
andT=|⟨X, Y⟩| 2, then
T d=
kY
i=1
Bi, B i independent, B i ∼Beta(i, n−k).(7.3)
7

Proof.The Cartan identity gives
ETm = 1
dm(n, k)=
kY
i=1
(i)m
(n−k+i) m
.
The right side is exactly the moment product of the beta variables in (7.3). Both laws are supported
on [0, 1], where the Hausdorff moment problem is determinate. This representation-theoretic
derivation of the beta-product identity is included for the Slater specialization and is not itself
presented as a priority claim.
The fourth cumulant has a simple complete classification.
Theorem 7.3(Slater activation threshold).For the phased Slater source,
d2(n, k) n
k
2 = n+ 1
(k+ 1)(n−k+ 1) .(7.4)
Consequently:
1. fork= 1, the fourth cumulant is negative;
2. for(n, k) = (4,2)it is negative;
3. for(n, k) = (5,2)it vanishes, and the sixth cumulant is−1/11200;
4. for every2 ≤k≤n− 2with n≥ 6, it is positive and the first activation is discontinuous at
somes c <
 n
k

.
Proof. The hook formula for the rectangle (2k) gives (7.4). By theorem 5.1, positivity is equivalent
to
2(n+ 1)<(k+ 1)(n−k+ 1).
For 2 ≤k≤n− 2, the right side is minimized at k = 2 or n− 2 and is 3( n− 1). The inequality is
strict exactly for n≥ 6; equality at the remaining interior boundary is (5 , 2) up to duality. Direct
use ofd 1 = 10, d2 = 50, d3 = 175 in the phase-averaged moments gives
cum6(Y) =EY 6 −15EY 4EY 2 + 30(EY 2)3 =− 1
11200.
The case (4,2) andk= 1 follow directly from (7.4).
The high-fidelity constant is also explicit:
An,k =
kY
i=1
Γ(n−k+i)
Γ(i) , q= 2k(n−k) + 1.(7.5)
Thus theorem 6.2 gives a closed rate offset for every particle number and one-particle dimension.
8 The phase-invariant quotient
Global phase is part of the source in theorem 4.1. When only the projective coherent state matters,
use the intrinsic Pl¨ ucker distortion
δ([x],[y]) = 1− |⟨x, y⟩|2.(8.1)
Here reproduction is restricted to the same projective homogeneous space; there is no radial
orbitope report.
8

0.0 0.2 0.4 0.6 0.8 1.0 1.2
normalized field s/(n
k)
0.00
0.02
0.04
0.06
0.08
0.10
optimized gain maxb
ϕs(b)/(n
k)
Dual gain
Λ2ℂ4
Λ2ℂ5
Λ2ℂ6
Λ3ℂ6
0.0 0.2 0.4 0.6 0.8 1.0 1.2
normalized field s/(n
k)
0.0
0.2
0.4
0.6
0.8
1.0
active radius b* (s)
Global report radius
Figure 1: Scalar dual envelope for representative phased Slater families. The plotted quantity is
maxb ϕs(b); dots mark the local stability field s0 =
 n
k

. Interior families with n≥ 6 already have
a positive-radius global phase ats 0, as proved by theorem 7.3. The plot is diagnostic and is not
used in any proof.
Corollary 8.1(Projective coherent-orbit frontier).Let[ X]be Haar on the compact projective
highest-weight orbit G/Kλ ≃G C/Pλ, and put N = dimV λ. With reproduction restricted to this
same orbit, under (8.1),
Rproj
λ (D) = sup
s≥0
{−sD+s−logH λ(s)}, H λ(s) =
∞X
m=0
sm
m!dm
.(8.2)
for0 < D <1 − 1/N. Moreover Rproj
λ (D) = 0for D≥ 1 − 1/N, and the value at D = 0is the
limiting value+∞for a positive-dimensional orbit. ForGr C(k, n), substitute (7.1).
Proof.For fixed [y], invariance makes
Ee−sδ([X],[y]) =e −sEes|⟨X,y⟩|2
=e −sHλ(s)
independent of [y]. The constant Shannon dual is therefore feasible, and the covariant exponential
reverse channel has the Haar source marginal and saturates it. Its distortion is D(s) = 1 −
H′
λ(s)/Hλ(s); strict log-convexity makes D(s) continuous and strictly decreasing from 1 − 1/N to
zero, so every stated interior distortion is covered. This is the same invariant-partition mechanism
used for compact groups [4], applied here directly to the transitive projective orbit; the explicit
dimension sequence is the representation-theoretic specialization.
The quotient result answers an intrinsic subspace-compression question. It must not be
conflated with theorem 4.1, whose decoder may report any point of the orbitope and whose radial
shrinkage causes coexistence.
9 Reproducibility and claim boundaries
The lightweight replay accompanying this paper checks:
728 exact rectangular-dimension and Hodge-complement identities;
the hook identity (7.4) and every quartic sign forn≤12;
the exceptional cumulants, including−1/11200 at (5,2);
thek= 1 0F1 reduction to relative error below 2.1×10 −15;
9

representative high-field constants and scalar activation diagnostics.
These checks replay algebra and numerics; they do not certify theorems 3.1 and 4.1 or the uniform
saddle proof. Those arguments are analytic and are stated in full above.
Several boundaries are essential. First, the integer moment maximization is due to Sugita; our
new use is the all-field transform and exact classical RDF. Second, the phase-lifted source is a
classical random amplitude vector. It is not a quantum message, so no quantum coding rate is
claimed. Third, the squared ambient distortion is not click-only Born calibration. Fourth, the
discontinuity criterion proves a first coexistence event but not a universal one-fold or no-reentrance
theorem. Finally, the intrinsic quotient corollary restricts reproduction to the homogeneous space
and is formally a different operational problem.
10 Conclusion
The Cartan product turns a large family of apparently high-dimensional compression problems
into one scalar envelope. The key geometric fact is simultaneous: coherent rays maximize every
integer overlap moment and hence the complete Laplace transform at every field. Conditional
means and Shannon duality then promote that rigidity to an exact unrestricted rate–distortion
theorem for every phase-lifted generalized coherent-state orbit.
Representation theory remains visible in the operational answer. The full dimension sequence
dimV mλ is the scalar partition function; dimV 2λ decides whether directional information turns
on discontinuously; positive roots determine the exact high-fidelity offset. For fermionic Slater
determinants these data become elementary rectangular dimensions, a beta-product overlap, and
a sharp all-(n, k) transition criterion. This higher-exterior-degree family is qualitatively broader
than a single Grassmannian or low-rank spectral case while retaining a complete, falsifiable
formula.
The natural next problem is phase-diagram rigidity: identify highest weights for which the
scalar radial envelope has a unique positive branch and no reentrance. That question is not needed
for the exact frontier proved here, and it remains open outside special dimension sequences.
Data and code availability
The source package contains the LaTeX manuscript, bibliography, the bounded Python replay, its
JSON output, and the figure-generation script. No external data set is used. All floating-point
output is diagnostic; the theorems do not depend on numerical optimization.
Use of AI tools
AI tools assisted with literature discovery, algebraic replay, drafting, and adversarial checking.
The named author takes responsibility for the claims, proofs, citations, and release artifacts. No
peer review or independent experimental validation is claimed.
References
[1] Ayumu Sugita. “Proof of the Generalized Lieb–Wehrl Conjecture for Integer Indices Larger
than One”. In:Journal of Physics A: Mathematical and General35.42 (2002), pp. L621–L626.
doi:10.1088/0305-4470/35/42/105. arXiv:nlin/0208007.
[2] Woody Lichtenstein. “A System of Quadrics Describing the Orbit of the Highest Weight
Vector”. In:Proceedings of the American Mathematical Society84.4 (1982), pp. 605–608.
doi:10.1090/S0002-9939-1982-0643758-8.
10

[3] Karin Baur. “Cartan Components and Decomposable Tensors”. In:Transformation Groups
8.4 (2003), pp. 309–319.doi:10.1007/s00031-003-1203-2.
[4] Peter Harremo¨ es. “Maximum Entropy on Compact Groups”. In:Entropy11.2 (2009),
pp. 222–237.doi:10.3390/e11020222. arXiv:0901.0015 [cs.IT].
[5] Wei Dai, Youjian Liu, and Brian Rider. “Quantization Bounds on Grassmann Manifolds and
Applications to MIMO Communications”. In:IEEE Transactions on Information Theory
54.3 (2008), pp. 1108–1123.doi:10.1109/TIT.2007.915691.
[6] Erwin Riegler, G¨ unther Koliander, and Helmut B¨ olcskei. “Lossy Compression of General
Random Variables”. In:Information and Inference: A Journal of the IMA12.3 (2023),
pp. 1759–1829.doi:10.1093/imaiai/iaac035. arXiv:2111.12312 [cs.IT].
[7] Alex Dytso and Martina Cardone. “Uniform Distribution on the ( n− 1)-Sphere: Rate–
Distortion under Squared Error Distortion”. In:2024 IEEE International Symposium on
Information Theory (ISIT). 2024, pp. 873–878.doi: 10.1109/ISIT57864.2024.10619427.
arXiv:2401.04248 [cs.IT].
[8] Howard Barnum. “Quantum Rate-Distortion Coding”. In:Physical Review A62 (2000),
p. 042309.doi:10.1103/PhysRevA.62.042309. arXiv:quant-ph/9806065.
[9] Zahra Baghali Khanian and Andreas Winter. “A Rate-Distortion Perspective on Quantum
State Redistribution”. In:IEEE Transactions on Information Theory72.4 (2026), pp. 2307–
2318.doi:10.1109/TIT.2024.3516505. arXiv:2112.11952 [quant-ph].
[10] Toby Berger.Rate Distortion Theory: A Mathematical Basis for Data Compression. Engle-
wood Cliffs, NJ: Prentice-Hall, 1971.
[11] Imre Csisz´ ar. “On an Extremum Problem of Information Theory”. In:Studia Scientiarum
Mathematicarum Hungarica9 (1974), pp. 57–61.
[12] Per-Olov L¨ owdin. “Quantum Theory of Many-Particle Systems. I. Physical Interpretations
by Means of Density Matrices, Natural Spin-Orbitals, and Convergence Problems in the
Method of Configurational Interaction”. In:Physical Review97 (1955), pp. 1474–1489.doi:
10.1103/PhysRev.97.1474.
11