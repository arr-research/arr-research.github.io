Universal Semiclassical Coexistence in Classical
Compression
of Phase-Lifted Coherent States
Dimension-Normalized Contacts and a Matched High-Fidelity Boundary
Layer
Lluis Eriksson
August 14, 2026

Abstract
Fix a nonzero dominant weight λ and let the highest weight grow along the ray N λ.
We study the exact classical Shannon rate–distortion function of the invariant phase-lifted
coherent orbit in VN λ under squared ambient Hilbert-space loss. The finite-N scalar
formula is known; the new problem is the coupled large-weight and distortion limit. If
dN = dim VN λ , ℓN = log dN , and a = dimC (GC /Pλ ) + 12 , we prove that the unique global
origin-tangent contact, for all sufficiently large N , obeys
tc,N = 2ℓN + 2a log ℓN + log(4π) − a + o(1),

Dc,N =

a
+ o(ℓ−1
N ),
ℓN

√
and that its time-sharing slope is ℓN + a log ℓN + log(2 π) + o(1). All root-system and
Weyl leading constants cancel in these dimension variables. For fixed 0 < D ≤ 1 the exact
unrestricted RDF satisfies RN (D)/ℓN → 1 − D. On the noncommuting boundary scale
D = x/ℓN , the centered rate converges to an explicit two-branch profile:
(
√
a log(a/x) + log(2 π) − a, 0 < x ≤ a,
√
log(2 π) − x,
x ≥ a.
We also identify the intervening soft-activation window, including an exact fixed-radius
Legendre expansion. The proof combines a differentiated Weyl–Bessel saddle, global
contact localization, and convex-envelope attainment. The result is classical rate–distortion
for an embedded coherent-amplitude source, not quantum rate–distortion or a derivation
of Born’s rule.

1

Introduction

Coherent-state families connect compact representation theory, semiclassical geometry, and
information theory. Their integer moments are controlled by Cartan products, while highestweight scaling produces a classical localization regime. These ingredients are familiar separately:
coherent moment extremality belongs to the generalized Lieb–Wehrl line [10, 17, 11], Weyl’s
formula governs the growth of irreducible representations [7], and entropy duality governs rate–
distortion functions [4, 3]. What is not contained in those components is the convex-envelope
phase transition of an exact coherent-orbit rate–distortion problem when the embedding itself
becomes semiclassical.
The finite-dimensional starting point was established in [6]. For a fixed irreducible representation, its Cartan-product Laplace theorem reduces arbitrary standard-Borel memories and
1

arbitrary square-integrable Euclidean reports to a scalar lower convex envelope. This paper
studies a different question: fix the abstract projective orbit but replace λ by N λ and send N
to infinity. The orbit’s embedding sharpens, its Hilbert dimension diverges, and the scalar
envelope develops three separated regimes:
1. a soft activation at field ℓN + a log ℓN + O(1);
2. a global origin-tangent contact at twice the leading field;
3. a high-fidelity layer DℓN = O(1) in which the curved coherent branch and the time-sharing
line remain simultaneously visible.
Our principal finding is universality in the correct coordinate. If one works in log N , the
leading orbit dimension and the Weyl constant appear. If one instead uses the observable
Hilbert dimension dN = dim VN λ , all representation-specific constants cancel from the contact
through order one. The complete boundary profile then depends only on
1
a=p+ ,
2

p = dimC (GC /Pλ ),

half the real dimension of the phase-lifted source.
General high-resolution results for random variables on manifolds provide power-law and
dimensional bounds [9, 12, 15]. Here the object is different: the ambient embedding changes
with N , the exact finite-N RDF is retained, and the critical distortion is of order 1/ log dN ,
rather than being obtained by first fixing a source and then taking distortion to zero.
The tensor-power classical limit itself is also established territory in Berezin–Toeplitz
and semiclassical free-energy theory [16, 2]. The recent SU (2) coherent-state majorization
theorem of Abreu [1] is a particularly close geometric neighbor, but it contains neither a
Shannon RDF nor the contact and boundary-layer problem treated here. At N = 1, the SU (2)
phase lift is the unit sphere in C2 ≃ R4 , so its finite-dimensional RDF is also the radius-one,
four-real-dimensional case of the exact sphere result of Dytso and Cardone [5]. Visible quantum
compression [8] is operationally different from the classical Euclidean reporting problem studied
below.
Claims boundary. We prove eventual uniqueness only for the global minimizing origintangent contact. We do not claim that every finite-N radial stationary equation has one
root, nor do we exclude every metastable radial branch. We make no statement at fixed zero
distortion, where every finite-N continuous orbit has infinite exact-reproduction rate.

2

Finite-dimensional input and notation

Let G be a compact connected semisimple group and let λ be a nonzero dominant integral
weight. For each integer N ≥ 1, let VN λ be the irreducible unitary representation of highest
weight N λ, with unit highest-weight vector vN . The phase-lifted coherent orbit is
MN = {eiθ πN (g)vN : g ∈ G, θ ∈ [0, 2π)},
equipped with invariant probability µN . We regard VN λ as a real Hilbert space with squared
Euclidean loss.
For a random XN ∼ µN , an encoder may use an arbitrary standard-Borel memory Z and
b
a square-integrable report X(Z).
The classical RDF is
2
b
RN (D) = inf{I(XN ; Z) : E∥XN − X(Z)∥
≤ D}.

2

No restriction to coherent reports is imposed.
Write
dm,N = dim VmN λ ,

dN = d1,N ,

and define
LN (t) =

∞
X

(t2 /4)m
,
(m!)2 dm,N
m=0

jN (b) = sup{tb − KN (t)},

KN (t) = log LN (t),

(1)

√
gN (u) = jN ( u).

(2)

t≥0

We import the following exact result, with attribution explicit because the finite-N theorem
is not the novelty of this paper.
Theorem 2.1 (Exact coherent-orbit RDF, [6]). For every N and 0 ≤ D ≤ 1,
RN (D) = (co gN )(1 − D).

(2.3)

Every exposed point is attained by a covariant exponential posterior. Every nonexposed chord
is attained by revealing an independent binary time-sharing flag. The converse allows arbitrary
standard-Borel memories and arbitrary square-integrable reports.
The theorem follows from the Cartan-component identity
Z

∥w∥2m
∥PmN λ w⊗m ∥2
≤
,
dm,N
dm,N

|⟨w, πN (g)vN ⟩|2m dg =

G

with equality classified by coherent rays, followed by conditional least squares and entropy
duality. We use its scalar conclusion, not a restricted coding ansatz.
Let
1
∨
Φ+
p = |Φ+
a=p+ ,
ℓN = log dN .
λ = {α > 0 : ⟨λ, α ⟩ > 0},
λ |,
2
Then p = dimC (GC /Pλ ). We assume p ≥ 1 throughout.

3

A differentiated Weyl–Bessel saddle

The asymptotic analysis must be simultaneous in the Cartan index m and the scaling parameter
N . A pointwise use of Weyl’s formula at fixed m would not control the Bessel saddle m ≍ t.

3.1

Exact Weyl factorization

For each active root define

⟨λ, α∨ ⟩
> 0.
⟨ρ, α∨ ⟩
Inactive roots contribute one, so Weyl’s formula is the exact product
cα =

dm,N =

Y

(1 + mN cα ).

α∈Φ+
λ

Consequently, uniformly for all integers m ≥ 1,
1
dm,N

=

1 −p Y m(1 + N cα )
1 −p
m
=
m {1 + O(N −1 )}.
dN
1
+
mN
c
d
α
N
+
α∈Φλ

The uniformity in m is elementary and crucial.
Put HN (t) = LN (t) − 1 and

2p
Bp = √ .
2π
3

Lemma 3.1 (Uniform differentiated saddle). Fix c > 0. Uniformly for t ≥ cℓN ,
log HN (t) = t − a log t − ℓN + log Bp + O(t−1 + N −1 ),
a
(log HN )′ (t) = 1 − + O(t−2 + (N t2 )−1 ),
t
a
′′
(log HN ) (t) = 2 + O(t−3 + (N t3 )−1 ).
t

(3)
(4)
(5)

Proof. Let
Tp (t) =

X (t2 /4)m
m≥1

(m!)2 mp

.

Put z = t/2 and introduce the Bessel law
Pr(Mz = m) =

z 2m
,
(m!)2 I0 (2z)

m ≥ 0.

It is the law of either of two independent Poisson(z) variables conditioned to be equal. Define
fp (0) = 0 and fp (m) = m−p for m ≥ 1. Then
Tp (2z) = I0 (2z) Efp (Mz ).

(6)

We record the moment calculation because two differentiated orders are used later. From
EMz = z

I1 (2z)
,
I0 (2z)

Var(Mz ) =

z d
EMz
2 dz

and the standard Debye expansions [13, 14],
1
E(Mz − z) = − + O(z −1 ),
4
z
2
E(Mz − z) = + O(1).
2

(7)

Repeated application of (z/2)∂z to log I0 (2z) bounds every fixed higher cumulant by O(z).
Chernoff’s inequality for the conditioned Poisson pair gives exponentially small tails outside
√
|Mz − z| ≤ z log z. Taylor expansion of fp through fourth order on that window, with
equation (7) and the corresponding third and fourth central moments, therefore yields
Efp (Mz ) = z

−p



p(p + 2)
1+
+ O(z −2 ) .
4z


(8)

The same calculation after inserting (2Mz )j , j = 1, 2, proves the differentiated form
"

∂tj

#

e−t ta Tp (t)
Ap
−1−
= O(t−2−j ),
Bp
t

j = 0, 1, 2.

(9)

where Ap = p(p + 2)/2 + 1/8. Thus no differentiation of an unspecified o(1) is being used.
Taking logarithms in equation (9) gives
log Tp (t) = t − a log t + log Bp + Ap /t + O(t−2 ),
(log Tp )′ (t) = 1 − a/t − Ap /t2 + O(t−3 ),
(log Tp )′′ (t) = a/t2 + 2Ap /t3 + O(t−4 ).

(10)

It remains to track the Weyl correction without hiding its m-independent part. The factor
in section 3.1 splits exactly as
Y m(1 + N cα )
α

1 + mN cα

= CN Qm,N ,

CN =

Y

1
,
N cα


1+

α

4

Qm,N =

Y
α

1+

1
mN cα

−1

. (11)

Hence log CN = O(N −1 ) and, if νp,t denotes the probability law on m ≥ 1 proportional to the
summands of Tp (t),
HN (t) = d−1
(12)
N CN Tp (t) Eνp,t QM,N .
On the Bessel window, Qm,N = 1 + O((N m)−1 ) and its first two discrete differences are
respectively O((N m2 )−1 ) and O((N m3 )−1 ). The moment bounds above then give, uniformly
for t ≥ cℓN ,
Eν QM,N = 1 + O((N t)−1 ),
Eν Q M − Eν M = O((N t)−1 ),
Varν Q (M ) − Varν (M ) = O((N t)−1 ),

(13)

where ν Q (m) ∝ Qm,N ν(m). For completeness, exponential-family differentiation now gives the
exact identities
2
∂t log Eν Q = {Eν Q M − Eν M },
t
2
4
2
∂t log Eν Q = − 2 {Eν Q M − Eν M } + 2 {Varν Q M − Varν M }.
t
t

(14)

Using equations (10) and (12) to (14) produces errors O(t−1 + N −1 ), O(t−2 + (N t2 )−1 ), and
O(t−3 + (N t3 )−1 ) at logarithmic derivative orders zero, one, and two, respectively. This proves
equations (3) to (5) and makes explicit why the O(N −1 ) part disappears after logarithmic
differentiation.
One coarse consequence is the logarithmic transition
KN (cℓN )
−→ (c − 1)+ ,
ℓN

c > 0,

locally uniformly away from c = 1.

4

The soft-activation window

The normalizer first becomes order one well before the global contact. This intermediate
regime supplies a full three-scale theorem and prevents an incorrect direct jump from the
Gaussian origin to the contact field.
Theorem 4.1 (Soft activation). Fix y ∈ R and set
tN (y) = ℓN + a log ℓN + y.
Then
HN (tN (y)) −→ Bp ey ,

(15)
y

KN (tN (y)) −→ log(1 + Bp e ),
Bp e y
′
KN
(tN (y)) −→ ϑy :=
.
1 + Bp ey
More precisely, define the activation-normalized field τN (y) by
HN (τN (y)) = Bp ey .

5

(16)
(17)

Then τN (y) = ℓN + a log ℓN + y + o(1) and
a
1−
+ o(ℓ−1
N ),
τN (y)
′
jN (KN
(τN (y))) = ϑy ℓN + aϑy log ℓN + ϑy (y − a) − log(1 + Bp ey ) + o(1).
′
KN
(τN (y)) = ϑy





(18)
(19)

Equivalently, for every fixed b ∈ (0, 1), the exact conjugate field and cost obey
tN (b) = ℓN + a log ℓN + log

b
+ o(1),
Bp (1 − b)

(20)

jN (b) = bℓN + ab log ℓN + b log b + (1 − b) log(1 − b) − b log Bp + o(1).

(21)

′ = H ′ (1 + H )−1 .
Proof. The first three limits follow directly from equation (3) and KN
N
N
Monotonicity of HN gives the unique field in theorem 4.1; equation (3) then gives its expansion.
At that field, the amplitude of HN is exact, so the O(log ℓN /ℓN ) correction that would otherwise
be amplified by multiplication by t is absent. Using equations (4) and (18) and j = tb − K yield
equation (19). Solving for fixed b requires one further order. Put ϑN = HN (t)/(1 + HN (t)).
Uniformly for b in compact subsets of (0, 1),



b = ϑN

a
1−
t



+ O(t−2 ),

ϑN = b +

ab
+ o(ℓ−1
N ).
ℓN

Moreover,
t = ℓN + a log t + log

ϑN
− log Bp + o(1).
1 − ϑN

Since KN (t) = − log(1 − ϑN ) and tb = tϑN − aϑN + o(1), substitution gives
jN (b) = ϑN ℓN + aϑN log ℓN + ϑN log

ϑN
− ϑN log Bp − aϑN + log(1 − ϑN ) + o(1).
1 − ϑN

Here ℓN (ϑN − b) = ab + o(1) cancels −aϑN = −ab + o(1). Letting ϑN → b in the remaining
order-one terms proves equations (20) and (21). This cancellation is why no extra −ab occurs
in equation (21).
Remark 4.2 (Why the centering matters). The leading limits at the naive field tN (y) are valid,
′ (t (y)) = ϑ + o(1) into tK ′ − K and claim an O(1) expansion: an
but one may not insert KN
y
N
O(log ℓN /ℓN ) error in K ′ is multiplied by t ≍ ℓN . The exact activation coordinate theorem 4.1,
or the fixed-b formula equation (21), removes this ambiguity.

5

Global contact and dimension-universal constants

Define the best origin-supported slope
jN (b)
.
0<b<1 b2

ρN = inf

The quotient tends to dN at the origin and diverges at b ↑ 1. The trial field t = 2ℓN has
hN (t) = O(ℓN ) < dN , so for all sufficiently large N the infimum is attained at a positive
′ (t) and put
interior field. Parameterize b = KN
hN (t) =

′ (t) − K (t)
tKN
N
.
′ (t)2
KN

6

Direct differentiation gives the exact identity
h′N (t) =

′′ (t)
KN
′
′ (t)3 {2KN (t) − tKN (t)}.
KN

The denominator is the third power; replacing it by a square would be an algebraic error,
though it would not change the stationary equation.
Lemma 5.1 (Global localization). Every global minimizer tc,N of hN satisfies
tc,N
−→ 2,
ℓN

′
KN
(tc,N ) −→ 1.

For all sufficiently large N , the global minimizing contact is unique. This does not assert
uniqueness of all stationary roots outside the global contact window.
Proof. For t = cℓN with c > 1 fixed, HN is a positive power of dN . When c is bounded away
from one it is in fact much larger than ℓN , so replacing log(1 + HN ) by log HN incurs o(1/ℓN )
in the calculation of hN . Uniformly on compact subsets of (1, ∞),
hN (cℓN ) = ℓN + a log ℓN + Fa (c) + o(1),
where

2a
− a − log Bp .
c
Since Fa′ (c) = a(c − 2)/c2 , its unique minimum is c = 2.
It remains to exclude other field scales. For t ≤ (1 − ε)ℓN , the positive series and
equation (3) make HN exponentially small. Indeed, dm,N ≥ dN for m ≥ 1, hence HN (t) ≤
{I0 (t) − 1}/dN ≤ et−ℓN ; the exact quotient is then exponentially larger than its value at 2ℓN
(bounded t follows from the quadratic origin expansion). In the soft window, equation (21)
gives jN (b)/b2 = ℓN /b + O(log ℓN ), strictly larger than the candidate slope for every radius
bounded away from one. Radii tending to zero are excluded by combining the quadratic origin
hN (0+) = dN with the subactivation estimate.
It remains to control the full transition window t/ℓN → 1. Put S = HN (t) and A =
(log HN )′ (t). If S → 0, the exact formulas give hN (t) ∼ t/S, hence hN /ℓN → ∞. If S
stays bounded away from both zero and infinity, then along every convergent subsequence
bN → S/(1 + S) < 1, and the fixed-radius expansion gives hN /ℓN → 1/bN > 1. Finally
suppose S → ∞ and define
tA − log S
.
h̄N =
A2
With δ = S −1 , direct algebra gives the exact difference
Fa (c) = a log c +

hN − h̄N =

tAδ − (2δ + δ 2 ) log S − (1 + δ)2 log(1 + δ)
.
A2

(5.5)

Because t ∼ ℓN , log S = o(ℓN ), and A → 1, this difference is nonnegative for all sufficiently
large N . Meanwhile the saddle expansion gives
h̄N = ℓN + a log ℓN + a − log Bp + o(1).
Its order-one constant exceeds the c = 2 constant by a(1 − log 2) > 0. Thus no sequence
in the transition window can minimize globally. If t/ℓN → ∞, equation (3) gives an excess
a log(t/ℓN ) → ∞. Thus every global minimizer lies in the c = 2 + o(1) window.
There HN ≫ ℓN , so logistic corrections are uniformly negligible, and equations (4) and (5)
gives
2a
′
′′
KN
(t) − tKN
(t) = 1 −
+ o(t−1 ) > 0.
t
7

′ is strictly increasing throughout the localized window. Together with
Hence 2KN − tKN
section 5, this proves uniqueness of the global minimizing contact for all sufficiently large
N.
′ (t
2
Theorem 5.2 (Universal global contact). Let bc,N = KN
c,N ) and Dc,N = 1 − bc,N . Then

tc,N = 2ℓN + 2a log ℓN + log(4π) − a + o(1),
a
bc,N = 1 −
+ o(ℓ−1
N ),
tc,N
a
Dc,N =
+ o(ℓ−1
N ),
ℓN
√
ρN = ℓN + a log ℓN + log(2 π) + o(1).

(22)
(23)
(24)
(25)

The rate at the positive end of the coexistence face is
√
jN (bc,N ) = ℓN + a log ℓN + log(2 π) − a + o(1).
Proof. At an interior minimum, section 5 gives the contact equation
′
2KN (tc,N ) = tc,N KN
(tc,N ).

By theorem 5.1, HN (tc,N ) ≫ ℓN . Therefore
KN (t) = t − a log t − ℓN + log Bp + o(1),
′
KN
(t) = 1 − a/t + o(t−1 )

at contact. Substitution in section 5 gives
tc,N = 2ℓN + 2a log tc,N − 2 log Bp − a + o(1).
√
Since tc,N /ℓN → 2 and Bp = 2p / 2π, the identity a − p = 1/2 yields
2a log 2 − 2 log Bp = log(4π),
which proves equation (22). Equations equations (23) and (24) follow from the derivative
saddle. At contact, jN = tb − K = tb/2, hence ρN = t/(2b); expanding 1/b proves equation (25)
and theorem 5.2.
Proposition 5.3 (Exact convex-envelope gluing). For all sufficiently large N , put uc,N = b2c,N .
Then
(
ρN u,
0 ≤ u ≤ uc,N ,
(co gN )(u) =
gN (u), uc,N ≤ u < 1.
Proof. Global minimality in section 5 gives gN (u) ≥ ρN u for every u. At contact, gN (uc,N ) =
ρN uc,N and
tc,N
′
gN
(uc,N ) =
= ρN .
2bc,N
√
′ (b), so that b = K ′ (t) and j ′′ (b) = 1/K ′′ (t). Direct differentiation
Write b = u and let t = jN
N
N
N
gives
′′ (t)
b − tKN
′′
gN
(u) =
′′ (t) .
4b3 KN

8

′′ (t) > 0, since it is the variance of a nondegenerate tilted overlap law. Uniformly on
Here KN
the post-contact branch, equations (4) and (5) and HN (t) → ∞ give
′′
′
′′
b − tKN
(t) = KN
(t) − tKN
(t) = 1 −



2a
+ O t−2 + (N t2 )−1 + tHN (t)−1 > 0
t

′′ > 0 on [u
for all sufficiently large N . Thus gN
c,N , 1). Hence the function equal to ρN u before
contact and gN (u) after contact is convex and lies below gN , so it is a convex minorant.
Conversely, every convex minorant lies below the chord from (0, 0) to (uc,N , gN (uc,N )) on the
first interval and lies below gN on the second. This proves theorem 5.3 and explicitly rules out
a later chord lowering the high-fidelity branch.

6

Macroscopic law and matched boundary layer

Theorem 6.1 (Macroscopic exact-RDF limit). For every fixed 0 < D ≤ 1,
RN (D)
−→ 1 − D.
log dN
The convergence is uniform on D ∈ [δ, 1] for every δ > 0. Equivalently, since ℓN = p log N +
O(1),
RN (D)
−→ p(1 − D).
log N
Proof. By theorem 5.3, the lower convex envelope equals the contact line on 0 ≤ u ≤ b2c,N , and
every such point is attained by the time-sharing construction in theorem 2.1. For fixed D > 0,
equation (24) gives 1 − D < b2c,N eventually, so
RN (D) = ρN (1 − D).
Now use equation (25). At D = 1 both sides vanish exactly. The point D = 0 is excluded
because RN (0) = +∞ for every finite-N continuous orbit.
The macroscopic line hides the transition. Its complete nontrivial remnant appears when
DℓN stays finite.
Theorem 6.2 (Matched high-fidelity boundary layer). Fix x > 0 and put DN = x/ℓN . Then
RN (DN ) − ℓN − a log ℓN −→ Ha (x),
locally uniformly for x ∈ (0, ∞), where

Ha (x) =


√
a log(a/x) + log(2 π) − a,


√
log(2 π) − x,

0 < x ≤ a,
x ≥ a.

The branches have matching value and derivative at x = a.
Proof. For the deterministic coherent-radius branch set b =
′ (t) and equation (4) give
b = KN
2aℓN
t=
+ O(1).
x
Substitution in jN (b) = tb − KN (t) yields

p

1 − x/ℓN . The saddle equation

√
gN (1 − x/ℓN ) = ℓN + a log ℓN + a log(a/x) + log(2 π) − a + o(1).
9

Universal matched boundary profiles
a = 1.5
a = 2.5
a = 4.5

2
0

−2
−4
−6

2 × 100
absolute error (nats)

centered rate Ha(x) (nats)

4

Exact Weyl-series contact diagnostics

100
6 × 10−1

−8

SU(2) |tc − tasy|
SU(2) |ρc − ρasy|
SU(3) |tc − tasy|
SU(3) |ρc − ρasy|

6 × 100

0.5
1.0
1.5
2.0
boundary coordinate x/a = Dlog dN/a

101
ellN = log dN

Figure 1: Left: the universal centered boundary profile Ha (x), with the horizontal coordinate
normalized by its contact value a. Dots mark the tangencies. Right: bounded deterministic
diagnostics from the exact Weyl series for symmetric powers of SU (2) and SU (3). Slow
convergence is expected because the theorem contains a log log dN correction. Numerics
illustrate the analytic theorem but are not used in its proof.
The cancellation uses again a − p = 1/2.
By equation (24), contact occurs at x = a + o(1). For x > a, the requested point lies on
the origin-to-contact face, and equation (25) gives
√
RN (x/ℓN ) = ρN (1 − x/ℓN ) = ℓN + a log ℓN + log(2 π) − x + o(1).
For 0 < x < a, the point lies beyond contact toward high fidelity, so theorem 5.3 makes the
high-fidelity branch the exact lower hull and gives section 6. Both the raw-branch expansion
and the contact-line expansion are uniform for x in any compact subset of (0, ∞). The exact
selector changes at xc,N = ℓN Dc,N → a, and the two limiting expressions agree at a; hence
their piecewise selection converges uniformly on every such compact set. At x = a, both
√
formulas give log(2 π) − a, and both derivatives equal −1.
The difference between the curved branch and the continuation of the tangent line is
a{− log(x/a) − 1 + x/a} ≥ 0,
with equality only at contact.

7

Examples

7.1

Symmetric powers of SU (q)

For G = SU (q) and λ = ω1 ,
!

N

q

VN ω1 = Sym (C ),

dN =

N +q−1
,
q−1

p = q − 1,

1
a=q− .
2

+q−1
Thus the macroscopic law is universal after division by log N q−1
, while the boundary contact
occurs at Dc log dN → q − 1/2.



10

For SU (2), the scalar normalizer has the exact integral fixture
LN (t) =

(t2 /4)m
=
(m!)2 (mN + 1)
m≥0
X

Z 1

I0 (txN/2 ) dx.

0

This follows by inserting (mN + 1)−1 = 01 xmN dx term by term. It provides a transparent
one-dimensional check of every scale in the theorem.
For SU (3),
5
(mN + 1)(mN + 2)
,
p = 2,
a= .
dm,N =
2
2
The exact positive series remains inexpensive even for symbolic values of N spanning many
orders of magnitude.
R

7.2

Cartan powers of Slater-determinant orbits

For G = SU (n) and λ = ωk , the abstract projective coherent orbit is GrC (k, n) and
p = k(n − k),

1
a = k(n − k) + .
2

At N = 1 the coherent vectors are unit Slater determinants in Λk Cn . The ray N ωk is the N th
Cartan-power embedding of the same projective orbit. The present theorem applies to this
embedding sequence. It should not be misread as an assertion that a single physical fermionic
Hilbert space has changed particle number without changing the representation.

8

Reproducibility and numerical scope

′ exactly
The accompanying script evaluates equation (1) by a positive recurrence, computes KN
from the normalized weights, and solves the global contact equation
′
2KN (t) − tKN
(t) = 0

inside the analytically localized window. It includes two exact Weyl sequences:
family

dm,N

(p, a)

SU (2) symmetric powers
SU (3) symmetric powers

mN + 1
(mN + 1)(mN + 2)/2

(1, 3/2)
(2, 5/2)

The replay is deterministic, uses no Monte Carlo, and finishes in less than one second on the
reference machine. The JSON output records the exact contact residual, distortion, slope,
asymptotic predictions, and convergence errors. Figure 1 is generated from that frozen output
and the closed form theorem 6.2. These checks diagnose constants and code paths; they do
not replace the proofs.

9

Scope, novelty boundary, and open problems

The theorem concerns a sequence of classical random vectors supported on phase-lifted
coherent orbits. Mutual information and rates are classical. It is not quantum rate–distortion,
a quantum channel-capacity theorem, a click-only hidden-variable simulation, or a derivation
of Born probabilities.
The following ingredients are prior machinery and are not claimed as new: Weyl’s dimension
formula, Cartan components, integer-index coherent moment extremality, Bessel asymptotics,
11

entropy variational duality, and the exact finite-N RDF of [6]. The contribution is the
coupled highest-weight asymptotic theorem: its global contact localization, dimension-universal
constants, soft-activation expansion, dimension-normalized exact-RDF limit, and matched
boundary profile.
Three boundaries are important.
1. Eventual uniqueness is proved for the global minimizing origin tangent only. Other
finite-N stationary roots are not classified.
2. The limit theorem 6.1 requires fixed D > 0. The boundary theorem handles D ≍ 1/ log dN ,
but exact zero distortion remains infinite.
3. The abstract orbit is fixed while its Cartan embedding changes. Results for a fixed
representation followed by D ↓ 0 are a different asymptotic problem.
Natural next questions include third-order contact expansions retaining the root-systemdependent N −1 terms, moderate deviations between the soft window and global contact, and
extensions to sign-quotiented or projective losses whose posterior-mean bodies differ from the
phase-lifted orbitope.

10

Conclusion

Highest-weight scaling turns the exact coherent-orbit compression problem into a universal
phase diagram. The normalizer first activates at ℓN + a log ℓN + O(1), but the best time-sharing
tangent waits until a field twice as large to leading order. The critical distortion shrinks as
a/ℓN , the fixed-distortion RDF becomes the line (1 − D)ℓN , and a matched DℓN boundary
layer retains the curved coherent branch and its tangent in one explicit profile. Writing the
result in terms of the actual Hilbert dimension removes every Weyl leading constant and
leaves only half the real source dimension. The universality is therefore not an artifact of
one group or one orbit: it is the common semiclassical signature of the exact Cartan-product
rate–distortion mechanism.

Data and code availability
The source package contains the LaTeX manuscript, bibliography, vector figure and its
generator, the bounded verification script, and frozen JSON output. No external data set is
used. All floating-point values are diagnostic.

Use of AI tools
AI tools assisted with literature discovery, algebraic replay, adversarial checking, drafting, and
layout inspection. The named author takes responsibility for the claims, proofs, citations, and
release artifacts. No peer review or independent scientific validation is claimed.

References
[1] Luis Daniel Abreu. Isospectral Majorization and Isoperimetric Inequalities for Coherent
States on the Bloch Sphere. 2026. arXiv: 2608.12248 [quant-ph].
[2] Zied Ammari, Michele Correggi, Marco Falconi, and Raphaël Gautier. Semiclassical
Limit of Entropies and Free Energies. 2025. arXiv: 2510.15777 [math-ph].

12

[3] Thomas M. Cover and Joy A. Thomas. Elements of Information Theory. 2nd ed. Hoboken:
Wiley, 2006. doi: 10.1002/047174882X.
[4] Imre Csiszár. “On an Extremum Problem of Information Theory”. In: Studia Scientiarum
Mathematicarum Hungarica 9 (1974), pp. 57–61.
[5] Alex Dytso and Martina Cardone. “Uniform Distribution on (n − 1)-Sphere: RateDistortion under Squared Error Distortion”. In: 2024 IEEE International Symposium
on Information Theory. 2024, pp. 873–878. doi: 10.1109/ISIT57864.2024.10619427.
arXiv: 2401.04248 [cs.IT].
[6] Lluis Eriksson. “Exact Classical Rate–Distortion for Phase-Lifted Generalized Coherent States: Cartan-Product Laplace Rigidity, Universal Radial Envelopes, and
Slater-Determinant Transitions”. In: Archive for Rigorous Research (2026). ARR-20266XH6JAS5ZA934A6J, version 1. url: https://arr-research.github.io/papers/
ARR-2026-6XH6JAS5ZA934A6J/.
[7] William Fulton and Joe Harris. Representation Theory: A First Course. New York:
Springer, 1991. doi: 10.1007/978-1-4612-0979-9.
[8] Patrick Hayden, Richard Jozsa, and Andreas Winter. “Trading Quantum for Classical
Resources in Quantum Data Compression”. In: Journal of Mathematical Physics 43.9
(2002), pp. 4404–4444. doi: 10.1063/1.1497239. arXiv: quant-ph/0204038.
[9] Tsutomu Kawabata and Amir Dembo. “The Rate-Distortion Dimension of Sets and
Measures”. In: IEEE Transactions on Information Theory 40.5 (1994), pp. 1564–1572.
doi: 10.1109/18.333868.
[10] Elliott H. Lieb. “Proof of an Entropy Conjecture of Wehrl”. In: Communications in
Mathematical Physics 62 (1978), pp. 35–41. doi: 10.1007/BF01940328.
[11] Elliott H. Lieb and Jan Philip Solovej. “Proof of the Wehrl-Type Entropy Conjecture
for Symmetric SU(N) Coherent States”. In: Communications in Mathematical Physics
348 (2016), pp. 567–578. doi: 10.1007/s00220-016-2596-9.
[12] Tamás Linder and Ram Zamir. “High-Resolution Source Coding for Non-Difference Distortion Measures: The Rate-Distortion Function”. In: IEEE Transactions on Information
Theory 45.2 (1999), pp. 533–547. doi: 10.1109/18.749001.
[13] NIST Digital Library of Mathematical Functions. Modified Bessel Functions, Chapter
10. https://dlmf.nist.gov/10. Accessed 2026-08-14.
[14]

Frank W. J. Olver. Asymptotics and Special Functions. Wellesley: A K Peters, 1997.

[15] Erwin Riegler, Günther Koliander, and Helmut Bölcskei. “Lossy Compression of General
Random Variables”. In: Information and Inference: A Journal of the IMA 12.3 (2023),
pp. 1759–1829. doi: 10.1093/imaiai/iaac035.
[16] Martin Schlichenmaier. “Berezin–Toeplitz Quantization for Compact Kähler Manifolds:
A Review of Results”. In: Advances in Mathematical Physics 2010 (2010), p. 927280.
doi: 10.1155/2010/927280.
[17] Ayumu Sugita. “Proof of the Generalized Lieb–Wehrl Conjecture for Integer Indices
Larger Than One”. In: Journal of Physics A: Mathematical and General 35.42 (2002),
pp. L621–L626. doi: 10.1088/0305-4470/35/42/105.

13

