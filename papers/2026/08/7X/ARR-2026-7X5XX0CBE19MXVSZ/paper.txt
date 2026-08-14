Finite-Sample-Valid Tests for Structured Matricial
Hausdorff Moments
Joint Gaussian Grams, Strict Half-Time Separation,
and Sharp Tangent-Cone Power
Lluis Eriksson
August 14, 2026
Abstract
We give a finite-sample test for whether one joint Gaussian sketch covariance is
compatible with a positive-semidefinite matrix-valued measure supported on a prescribed
interval. The observed vector contains several exponent blocks, so its population covariance
is one block-Hankel Gram matrix rather than a list of unrelated moment estimates. The
classical truncated matricial Hausdorff theorem supplies the exact parity-dependent null.
A single Gaussian singular-value event gives a simultaneous Loewner band for the whole
covariance; intersecting that band with the structured moment cone yields a nonasymptotic
level-αsemidefinite test without sample splitting.
The full joint Gram is strictly more informative than the integer-time localizer used
in the preceding finite-sample method. Forν = (1 −w)δ0 + wδt, with0 <s<t≤ 1and
w<s 2/t2, the previous conditions2M0 −M2 >0holds, whereas the half-time condition
sM1 −M2 = wt(s−t ) <0. We prove that the old test has power at mostα, while the full
test has power at least1−α above an explicit sample threshold on the same acquisition.
At a positive-definite covariance on a singular null face, the Wishart experiment is locally
asymptotically normal. The constrained likelihood ratio converges to squared Gaussian
distance from an explicit spectrahedral tangent cone, giving its pointwise local power
function and a matchingn−1/2 separation boundary. We give auditable dual semantics
and an exact rational certificate for the strict fixture.
The moment characterization, Gaussian covariance bounds, and generic constrained-
likelihood theory are established ingredients. The contribution is their structured joint-
sketch integration, the analytic same-data separation, and the exact certificate layer. This
work explicitly extends ARR recordARR-2026-77QM18J2KG9679B7.
1 Introduction
Finite moment tests turn support claims into positive-semidefinite constraints, but several
shortcuts destroy their meaning. A single scalar localizer does not test the complete truncated
moment cone; independently estimated moments ignore the cross-covariances in a joint sketch;
and a negative floating-point eigenvalue is not a certificate. These distinctions are most
important on singular faces, precisely where support restrictions become informative.
The matrix Hausdorff moment problem on a compact interval is classical. Parity-complete
block-Hankel characterizations and matrix canonical moments are developed in [5, 2, 3, 7].
Moment and localizing matrices are standard in polynomial optimization [11, 9]. We specialize
those results without discarding the off-diagonal moment information present in the experiment.
The statistical starting point is the previous record [6]. Its integer-time support component
retains
[θBi+j −Bi+j+1]N
i,j=0 ⪰0.(1.1)
1

Here we puty= √x and retain the half-time covariance blocks already acquired. The whole
covariance becomes a block-Hankel matrix ofy-moments, and the correct support localizer
uses every polynomial direction on that grid. No extra sample or multiple-testing correction is
needed: all constraints are optimized inside one simultaneous band.
Our contributions are: an operational joint Gaussian model; a parity-exact structured
test; an analytic old-versus-full power separation; consistency against every fixed covariance
alternative; an active-kernel tangent formula and Gaussian cone-projection likelihood limit;
and exact dual semantics. Rejection falsifies compatibility of the visible matrix measure with
the declared support. Non-rejection does not prove a physical spectral gap.
2 Joint Gaussian exponent sketches
LetTbe a positive contraction on a real Hilbert space and letψ1,...,ψ c be fixed probes. For
k= 0,...,q , assumeTk/2ψa is defined. LetW = {W(h) : h∈H} be an isonormal Gaussian
process, soEW(h)W(k) =⟨h,k⟩, and set
zk,a =W(T k/2ψa), z= (z 0,1,...,z q,c)∈R d, d= (q+ 1)c.(2.1)
In finite dimension one may realizeW(h) = ⟨g,h⟩ with g∼N (0,I). If ET is the spectral
resolution ofT, define the real-symmetric matrix measure
νab(B) =⟨ψ a,ET({λ:
√
λ∈B})ψ b⟩.
The vector is jointly Gaussian of known mean zero, and its covariance blocks are
Ezk,azℓ,b =⟨ψa,T (k+ℓ)/2ψb⟩=: (Mk+ℓ)ab.(2.2)
Consequently
K:=Ezz T =Hq(M) := [Mi+j]q
i,j=0.(2.3)
The spectral theorem gives a positive-semidefinitec×c matrix-valued measureν on[0 ,1]with
Mj =
∫1
0
yj dν(y).(2.4)
The visible support claim issuppν⊂[0,s].
Observe iid copiesz1,...,z n and form
S= 1
n
n∑
r=1
zrzT
r .(2.5)
Sampling noise makes the empirical anti-diagonal blocks unequal. We do not projectS onto
the Hankel subspace. Instead, the structured population moments remain primal variables and
Hq(M)is required to lie in a confidence band aroundS. This preserves coverage independently
of any projection rule.
Remark 2.1.The blocks Mj are not independently sampled covariances: they are repeated
anti-diagonals of oneK. The off-diagonal blocks contain the half-time moments. Replacing
them by independent moment oracles destroys the same-data comparison proved below.
2

3 The parity-complete matricial cone
For real-symmetric blocks define
Hr(M) = [Mi+j]r
i,j=0, G r(M) = [Mi+j+1]r
i,j=0,
Lr,s(M) = [sMi+j −Mi+j+1]r
i,j=0, Cr,s(M) = [sMi+j+1 −Mi+j+2]r
i,j=0.
(3.1)
Theorem 3.1(truncated matricial Hausdorff criterion).The blocks M0,...,M 2r have a
positive matrix-valued representing measure on[0,s]if and only if
Hr(M)⪰0, C r−1,s(M)⪰0,(3.2)
with the second condition absent atr= 0. The blocks throughM2r+1 have such a measure if
and only if
Gr(M)⪰0, L r,s(M)⪰0.(3.3)
Both statements include rank-deficient sequences.
Proof.Necessity follows from vector-polynomial Gram identities. Forp(y) =∑r
i=0 yivi,
v∗Hr(M)v=
∫
p(y)∗dν(y)p(y)≥0,(3.4)
and the remaining matrices inserty,s−y, ory(s−y).
For sufficiency, defineLM(∑
j Fjyj) = ∑
j tr(FjMj). Every real-symmetric matrix polyno-
mial nonnegative on[0,s]of degree at most2rfactors as
F=A TA+y(s−y)B TB,degA≤r,degB≤r−1,(3.5)
and at degree at most2r+ 1as
F=yA TA+ (s−y)B TB,degA,degB≤r.(3.6)
Here Aand B may be rectangular matrix polynomials; equivalently, each term denotes a finite
sum of real-symmetric polynomial squares. Thus the displayed LMIs makeLM nonnegative
on every positive matrix polynomial of the declared degree.
The truncated matrix-measure cone is closed. BoundedM0 bounds total scalar mass;
positivity bounds the variation of every entry; weak-star compactness supplies a matrix-measure
limit. IfM lay outside that cone, strict separation would produce a positive matrix polynomial
with negativeLM value, contradicting equations (3.5) and (3.6).
The theorem is established literature, not our novelty claim. Entrywise scalar tests are
insufficient because independently chosen scalar measures need not assemble into one positive
matrix measure.
For the acquisitionq= 2N + 1, the covariance exposesM0,...,M 2q = M4N+2 . The exact
even null is
K=H q(M), C q−1,s(M)⪰0.(3.7)
The Loewner band already enforcesK⪰ 0; the new ingredients are the anti-diagonal identities
and full half-time localizer.
3

4 A structured Loewner confidence test
Let G be ad×n standard real Gaussian matrix. On the range ofK, the sample covariance
has the congruence representation
S=K 1/2
(1
nGGT
)
K1/2.(4.1)
For0<α<1, put
η=
√
d+
√
2 log(2/α)√n ,(4.2)
assumeη <1, and define
a= (1 +η) −2, b= (1−η) −2.(4.3)
The Gaussian singular-value inequality [4, 10] yields
Pr
K
{aS⪯K⪯bS}≥1−α.(4.4)
This is a nonasymptotic valid Gaussian Loewner band. It is generally conservative, so we do
not call it an exact-coverage Wishart interval. Exact Wishart eigenvalue quantiles may replace
(a,b)without changing the primal geometry.
GivenS, solve
findM 0,...,M 2q ∈Sym c
such thataS⪯H q(M)⪯bS,
Cq−1,s(M)⪰0.
(4.5)
Reject exactly when this structured feasibility problem is infeasible. Using moment blocks
as variables enforces all anti-diagonal equalities by construction and makes the adjoint map
auditable.
Theorem 4.1(finite-sample validity).Under the joint Gaussian model,
sup
suppν⊂[0,s]
Prν {reject}≤α.(4.6)
The optimization may inspect every parity-appropriate constraint and matrix witness formed
from the acquired truncationM0,...,M 2q adaptively. No further multiplicity correction is
required.
Proof. On the single event equation (4.4), the true blocks satisfy the band withHq(M) = K.
Under the null, theorem 3.1 givesCq−1,s(M) ⪰0. The true sequence is feasible, so rejection is
contained in the complement of the coverage event.
Remark 4.2(singular covariance).The level argument does not invertK and is valid on
singular covariance faces. Implementations should compress to the exact common range implied
by the band or use facial reduction. Adding a numerical ridge changes the null.
5 Strict same-data power separation
Consider the scalar measure
ν= (1−w)δ 0 +wδt,0<s<t≤1,0<w<s 2/t2.(5.1)
Its first moments and jointN= 0covariance are
M0 = 1, M 1 =wt, M 2 =wt2, K=
(
1wt
wt wt2
)
≻0.(5.2)
4

The preceding integer-time method usesx=y2,θ=s 2, and retains
θM0 −M2 =s2 −wt2 >0.(5.3)
Its finite-window population null is therefore true despitet>s . The complete half-time null
contains instead
C0,s =sM1 −M2 =wt(s−t)<0.(5.4)
Both tests use the sameK; the predecessor discards its off-diagonalM1.
For a self-contained comparison, define the precedingN = 0test on the same observedS
as follows: accept whenever there is a symmetricQ=
(
B0 u
u B1
)
satisfying aS⪯Q⪯bS and
s2B0 −B1 ≥0. Thus it retains the two integer-time diagonal blocks and leaves the half-time
cross blockuunconstrained. On the event equation (4.4), the trueQ=Kis feasible for this
old test whenever equation (5.3) holds.
Theorem 5.1(strict old-versus-full separation).For equation(5.1), the preceding N = 0
integer-time test has rejection probability at mostα whenever its level theorem applies. Define
γ=wt(t−s), A=
(
0s/2
s/2−1
)
,(5.5)
W= tr|K 1/2AK1/2|=
√
γ2 +s2w(1−w)t 2, r=γ/W.(5.6)
The full structured test has rejection probability at least1−αwhenever
n>
(√
2 +
√
2 log(2/α)
)2 (√1 +r+ 1) 4
r2 . (5.7)
The scalar construction embeds algebraically in every channel dimension by tensoring with
a known rank-one channel projector. For the uncompressedc-channel test, replace
√
2 in
equation(5.7)by
√
2c. If the known common range is first compressed exactly to the rank-two
covariance range, equation(5.7)remains valid unchanged.
Proof. The old test’s population null holds by equation (5.3); its coverage argument bounds
rejection byα.
For the full test,
⟨A,K⟩=sM 1 −M2 =−γ.(5.8)
Suppose the Gaussian event equation (4.4) holds and a covarianceQ inside the test band is
full-null feasible. Putρ= (1 +η)/(1−η). Transitivity of Loewner order gives
ρ−2K⪯Q⪯ρ 2K.(5.9)
Let B = K1/2AK1/2, p = trB+, and m = trB−. Then p+ m = W and m−p = γ. The
support function of equation (5.9) gives
⟨A,Q−K⟩≤(ρ 2 −1)p+ (1−ρ −2)m.(5.10)
Substituting p = (W−γ )/2and m = (W + γ)/2shows that the right side is less thanγ
whenever
η < r
(√1 +r+ 1) 2 .(5.11)
Hence ⟨A,Q⟩< 0. But for a structuredQ = H1( ˜M), ⟨A,Q⟩ = s˜M1 −˜M2, which must be
nonnegative under the full null. Therefore the primal is infeasible on the coverage event.
Solving equation (5.11) fornwithd= 2gives equation (5.7).
5

5.1 Exact rational fixture
Take
s= 1
2, t= 3
4, w= 1
8.(5.12)
Then
K=
(
1 3/32
3/32 9/128
)
,detK= 63
1024 >0,(5.13)
s2M0 −M2 = 23
128 >0, sM 1 −M2 =− 3
128 <0,(5.14)
and
γ= 3
128, W 2 = 261
16384, r= 3√
261.(5.15)
These opposing margins andW2 are verified over exact rationals.
5.2 Full exponent Grams
For this paragraph define generalized momentsMβ =
∫1
0 yβdν(y)for every real β≥ 0. For
any exponentsa0,...,a R ≥0, the support null implies
KA
s = [sMai+aj+1 −Mai+aj+2]R
i,j=0 ⪰0,(5.16)
because this is the Gram matrix ofyai in L2(y(s−y)dν). Half-integer exponents couple integer
and half-time data. Separate-grid constraints are principal submatrices and cannot dominate
the full joint Gram. Equation (5.16) is operationally testable only when the corresponding
exponent blocks have also been acquired; it is not an additional constraint available from the
integer grid0,...,qalone.
6 Global separation of fixed alternatives
Let Cq,c,s be the closed cone of structured covariancesHq(M)compatible with a positive matrix
measure on[0,s]. For fixedK /∈Cq,c,s, set
δ(K) = distF(K,Cq,c,s)>0.(6.1)
Theorem 6.1(fixed-alternative consistency).For every fixedK /∈Cq,c,s, the rejection probabil-
ity tends to one. Uniformity holds on sets satisfying∥K∥op ≤B and distF(K,Cq,c,s) ≥δ0 >0.
If
(1−u) 2K⪯S⪯(1 +u) 2K, u<1,(6.2)
then everyQin the test band lies in a Frobenius ball aboutKof radius
√
dΓ(u,η)∥K∥op,(6.3)
where
Γ(u,η) = max
{
(1 +u) 2
(1−η) 2 −1,1− (1−u) 2
(1 +η) 2
}
.(6.4)
If this radius is less thanδ(K), rejection is forced.
Proof. Combining the event with aS⪯Q⪯bS gives scalar lower and upper Loewner
multiples ofK. Hence ∥Q−K∥ F ≤
√
dΓ∥K∥op. If that ball misses the closed null cone, no
structured sequence is feasible. Choosetn →∞ with tn/√n→ 0and put un = (
√
d+ tn)/√n.
The corresponding Gaussian singular-value event has probability at least1−2e−t2
n/2, while
un,ηn →0. Hence the displayed radius is eventually below the fixed positive distance; the
same argument is uniform under the two stated bounds.
6

7 Tangent geometry
FixK 0 =Hq(M0)≻0in the null; its localizer may be singular. Put
V= (Sym c)2q+1,H(M) =H q(M),C(M) =C q−1,s(M).(7.1)
The mapHis injective because every moment occurs on an anti-diagonal. Let U0 span
kerC(M0)and define
T0 ={H(D) :D∈V, U ∗
0 C(D)U0 ⪰0}.(7.2)
Theorem 7.1(exact tangent preimage).The Bouligand tangent cone ofCq,c,s at K0 equals
T0.
Proof.ForC 0 ⪰0,
TS+ (C0) ={E:U ∗
0 EU0 ⪰0}.(7.3)
Necessity follows by differentiating a feasible sequence and compressing tokerC0. Conversely,
choose an interior moment sequenceMint generated by a positive density on(0,s)times Ic.
BothH(M int)andC(M int)are positive definite. ThereforeDsl =M int −M 0 satisfies
U∗
0 C(Dsl)U0 ≻0.(7.4)
Robinson’s constraint qualification gives
T{M:C(M)⪰0}(M0) ={D:U ∗
0 C(D)U0 ⪰0}.(7.5)
The Hq positivity constraint is inactive atK0 ≻0. In factC(M0) +C( Dsl) =C( Mint) ≻0, so
the affine semidefinite constraint satisfies Robinson’s condition. Applying the injective mapH
proves the claim.
If K0 is singular, its PSD constraint is active and the experiment lives on a smaller range.
One must add its kernel compression and exact facial reduction. The regular likelihood theorem
below is restricted toK0 ≻0.
8 Wishart LAN and local asymptotic power
For real zero-mean Gaussian observations, the Fisher metric is
⟨H,J⟩I0 = 1
2 tr[(K0)−1H(K0)−1J].(8.1)
LetI 1/2
0 be a whitening isometry and putK0 =I 1/2
0 T0.
Theorem 8.1(LAN and cone-projection likelihood).Under
Kn =K 0 + H√n +o(n−1/2),(8.2)
log dP⊗n
Kn
dP⊗n
K0
=⟨Zn,H⟩I0 −1
2∥H∥2
I0 +oPK0 (1),(8.3)
where Zn is the Fisher–Riesz representation of the central score: for every fixedJ, ⟨Zn,J⟩I0 is
the normalized score in directionJ. Thus I1/2
0 Zn ⇒G, standard Gaussian inSymd. Twice
the log-likelihood ratio between the unrestricted covariance model and the structured null obeys
Λn ⇒dist 2(G+I 1/2
0 H,K0). (8.4)
7

Proof.Up to constants,
ℓn(K) =−n
2 {log detK+ tr(K −1S)}.(8.5)
InsertK=K 0 +H/√nand use
log det(K0 +E) = log detK 0 + tr((K0)−1E)− 1
2 tr[((K0)−1E)2] +o(∥E∥2),
(K0 +E) −1 = (K0)−1 −(K0)−1E(K0)−1
+ (K0)−1E(K0)−1E(K0)−1 +o(∥E∥2).
(8.6)
The covariance CLT supplies the Gaussian score and Fisher quadratic term. The local
unrestricted likelihood ish↦→⟨G+ I1/2
0 H,h⟩−∥h∥ 2/2. By theorem 7.1 and linearized Slater,
local null sets converge toK0. Completing the square after unrestricted and constrained
maximization gives equation (8.4).
For proper complex Gaussian observations the factor1/2in the Fisher metric is absent,
the covariance is complex Wishart, andG is standard in the real Hilbert spaceHermd; all
tangent and polar cones are then taken inHermd. This is a separate extension, not a change
of one scalar factor in the real experiment.
Letc α(K0)be an upperαquantile ofdist 2(G,K0).
Corollary 8.2(local size and power).The cone-likelihood test has asymptotic size at mostα
for every local null sequence. Its local power againstHis
πK0 (H) = Pr{dist2(G+I 1/2
0 H,K0)>c α(K0)}.(8.7)
Proof.Every local null limithbelongs toK 0. Since the cone is closed under addition,
dist(G+h,K 0)≤dist(G,K 0)(8.8)
pointwise. The vertex is least favorable. Randomization at a quantile atom gives exact
asymptotic size; otherwise the test is conservative.
At H = 0, Moreau decomposition gives∥ΠK◦
0 G∥2. For general spectrahedral preimages, we
retain the description as a Gaussian cone-projection law.
Theorem 8.3(matching n−1/2 boundary).At each regular boundary point, for a fixed
outward direction V /∈ T0 and a sequence Kn = K0 + εnV≻ 0with εn = o(n−1/2), no
level-α test has power above α+ o(1). Displacement H/√n has the nontrivial power in
theorem 8.2; and alternatives that remain in a compact positive-definite neighborhood and
satisfy √ndist I0 (Kn,Cq,c,s) →∞ are detected by the structured Loewner-feasibility test with
probability tending to one.
Proof.For an outwardV /∈T0,
D(P⊗n
K0+εV∥P⊗n
K0 ) = nε2
2 ∥V∥2
I0 +o(nε2).(8.9)
Pinsker proves the lower bound, theorem 8.1 gives the local limit, and theorem 6.1 plus
covariance concentration gives the upper bound.
If0 < α <1/2, then at a full-dimensional smooth halfspace faceK0 = {h : ⟨a,h⟩≥ 0},
∥a∥= 1, with outwardρ=−⟨a,I 1/2
0 H⟩>0, the exact local power is
π(ρ) = 1−Φ(z 1−α −ρ). (8.10)
This is the Neyman–Pearson envelope in the limiting one-dimensional normal experiment. At
the atom, includingα≥ 1/2, the critical rule must be randomized. If the Hankel image is a
proper subspace ofSymd, the formula applies conditionally inside that structured submodel;
the unrestricted test also contains the orthogonal equality-constraint component.
8

9 Auditable semidefinite dual certificates
The primal test is useful only if rejection can be checked independently of the floating-point
solver that found it. We therefore spell out its ordinary semidefinite Farkas dual. For block
matricesY= [Y ij]q
i,j=0 andZ= [Z ij]q−1
i,j=0 define
[H∗
qY] k =
∑
i+j=k
Yij,
[C∗
q−1,sZ]k =s
∑
i+j+1=k
Zij −
∑
i+j+2=k
Zij,
(9.1)
where empty sums are zero and symmetric symmetrization is understood. These are the exact
adjoints because⟨Y,H q(M)⟩= ∑
k⟨[H∗
qY] k,Mk⟩, and similarly forC.
Proposition 9.1(checkable rejection certificate).If there are positive semidefinite block
matricesYA,YB,YC satisfying
H∗
q(YA −YB) +C ∗
q−1,sYC = 0(9.2)
and
−a⟨YA,S⟩+b⟨Y B,S⟩<0,(9.3)
then the confidence feasibility problem is infeasible. Conversely, every infeasible instance of
this bounded structured-band problem admits a certificate of this form.
Proof.For any primal-feasibleM, positivity gives
0≤⟨Y A,Hq(M)−aS⟩+⟨Y B,bS−H q(M)⟩+⟨Y C,Cq−1,s(M)⟩.(9.4)
Stationarity cancels every moment block, leaving exactly the strictly negative number in
equation (9.3), a contradiction. For the converse, suppose approximate feasibility had residual
tending to zero. The sandwich constraints boundHq(M); injectivity ofHq then bounds the
moment variables. A convergent subsequence would be exactly feasible because the PSD
cones are closed, a contradiction. Thus the affine image and product PSD cone have positive
distance, and strong separation yields the displayed ordinary multipliers. This compact
sandwich argument is special to the present bounded band; generic singular semidefinite
systems may require facial reduction or Ramana’s extended dual [13].
9.1 An exact rational dual certificate
Collapse the band toa= b= 1and set S = K from equation (5.1) with the rational values in
section 5. Let
D=
(
0−1/4
−1/4 1
)
, Y A =D+I=
(
1−1/4
−1/4 2
)
, Y B =I, Y C = 1.(9.5)
Both matrix multipliers are positive definite. Sinces= 1/2, the three moment coefficients of
H∗
1D+C ∗
0,s1are
D00 = 0,2D 01 +s= 0, D 11 −1 = 0.(9.6)
Thus stationarity holds over the rationals, while
−⟨YA,K⟩+⟨Y B,K⟩=−⟨D,K⟩=− 3
128 <0.(9.7)
This is a solver-independent certificate that the full constraint rejects the population covariance.
Its entries, principal minors, stationarity residuals, and objective are replayed exactly by the
companion script.
9

10 Algorithm and reproducible replay
For exponent depthq, channel sizec, support cutoffs, and levelα, the operational procedure
is:
1. Acquirenindependent joint sketch vectorszj = (zj,0,...,z j,q)and form S = n−1 ∑
j zjzT
j .
2. Set d= (q+ 1)c, computeη,a,b from equation (4.4), and stop as sample-size unresolved
ifη≥1.
3. Introduce real-symmetric variablesM0,...,M 2q and solve the structured Loewner feasi-
bility problem in Section 4. Reject if and only if infeasible.
4. On rejection, request PSD multipliers from the solver, rationalize or outward-round them,
and verify PSD, stationarity, and a strictly negative objective independently. If a solver
fails to recover the guaranteed ordinary certificate numerically, use facial reduction to
expose and preserve the relevant face before reconstructing it.
The data path uses a single sample covariance, hence cross-exponent blocks and their
sampling correlations are never discarded. Complexity is that of an SDP with2q+ 1real-
symmetric c×c variables, two PSD constraints of order( q + 1)c, and one of order qc.
Anti-diagonal consistency is exact becauseHq(M)is assembled from shared variables, rather
than imposed by noisy equality tests.
The lightweight replay fileverify_matricial_hausdorff.py uses exact rational arith-
metic for the algebraic fixtures and floating-point normal quantiles only for the reported
Gaussian illustration. It checks the even and odd block criteria on noncommuting positive2×2
atomic weights, vector-polynomial identities, Loewner inversion, an intentionally corrupted
moment witness, the strict two-atom fixture, the dual certificate, and a regular smooth-face
tangent fixture. It does not simulate coverage, optimize over scientific models, or certify novelty.
A successful run therefore certifies the paper’s algebraic fixtures, not its empirical scope.
11 Independent-moment observations as a secondary variant
Some experiments produce independent covariance estimatesˆMk rather than one joint exponent
vector. If simultaneous bands
Mk ⪯Mk ⪯Mk,0≤k≤m,(11.1)
have joint coverage at least1−α, intersecting those bands with the parity-appropriate LMIs
in theorem 3.1 gives the same finite-sample level argument. Bonferroni, a joint bootstrap with
proved coverage, or exact Wishart bounds may construct the simultaneous event. This variant
is useful but strictly less informative for the present separation question: estimating blocks
independently obscures the joint covariance geometry and may fail to retain the half-time
cross blocks that make theorem 5.1 possible.
The joint model is therefore the primary theorem, not an example of the independent oracle.
Conversely, joint acquisition does not manufacture unobserved moments: with exponents
0,...,q it exposes exactly sums0 ,..., 2q. Claims about a larger truncated cone require
additional exponents or assumptions.
12 Relation to prior work and scope boundaries
The matricial Hausdorff equivalences themselves are classical [5, 2, 3, 7]; scalar moment and
localizing matrices belong to the established truncated-moment framework [11, 9]. Gaussian
10

covariance concentration, constrained likelihood limits, and exact rational SDP certification
likewise have substantial precedents [4, 10, 1, 14, 8, 12]. We do not rename any of those
components as new.
This paper explicitly extends the finite-sample spectral support framework archived as
ARR-2026-77QM18J2KG9679B7 [6]. Its increment is the integrated theorem chain: one opera-
tional exponent sketch produces the entire block-Hankel covariance; the parity-complete matrix
cone uses every cross block; a closed rational family proves strict same-data power over the
preceding integer-time localizer; a single Loewner event gives a multiplicity-free conic test; and
the tangent preimage identifies its sharpn−1/2 boundary law. The strictness claim is relative
to the precisely stated predecessor constraint, not to all conceivable support tests.
Several limitations are structural.
•Gaussian sketches give the stated finite-sample band. Sub-Gaussian or dependent data
need a separately proved covariance region.
• The cutoff hypothesis concerns existence of a positive matrix measure on[0,s]. It does
not identify a unique measure, dynamical generator, or physical microscopic mechanism.
• Finite truncation cannot detect every alternative distribution. The consistency theorem
is against covariances outside the exposed truncated cone, not against alternatives sharing
all observed blocks with a null law.
• The LAN theorem assumes a positive-definite covariance and the stated linearized Slater
condition. More singular intersections can have different rates and require stratified
facial analysis.
• Ordinary floating-point infeasibility is not a proof. A preserved dual certificate, preferably
rational or interval verified, is required for an auditable individual rejection.
13 Conclusion
Ajointhalf-timeexponentsketchturnsamatrix-valuedsupportquestionintoasinglestructured
Wishart problem. The full block-Hankel covariance and its Hausdorff localizer yield finite-
sample validity, strict same-data power, global fixed-alternative consistency, and an exact
Gaussian tangent-cone limit. The rational fixture isolates why the gain occurs: the discarded
cross moment is negative in the support localizer even while the older integer-grid condition is
strictly feasible. The result is thus stronger than an additional moment inequality: it gives
an operational acquisition, a sharp boundary theory, and independently checkable rejection
witnesses.
References
[1] Herman Chernoff. “On the Distribution of the Likelihood Ratio”. In:The Annals of
Mathematical Statistics25.3 (1954), pp. 573–578.doi:10.1214/aoms/1177728725.
[2] Abdon E. Choque Rivero, Yurii M. Dyukarev, Bernd Fritzsche, and Bernd Kirstein. “A
Truncated Matricial Moment Problem on a Finite Interval”. In:Interpolation, Schur
Functions and Moment Problems. Vol. 165. Operator Theory: Advances and Applications.
2006, pp. 121–173.doi:10.1007/3-7643-7547-7_4.
11

[3] Abdon E. Choque Rivero, Yuriy M. Dyukarev, Bernd Fritzsche, and Bernd Kirstein. “A
Truncated Matricial Moment Problem on a Finite Interval. The Case of an Odd Number
of Prescribed Moments”. In:System Theory, the Schur Algorithm and Multidimensional
Analysis. Vol. 176. Operator Theory: Advances and Applications. 2007, pp. 99–164.doi:
10.1007/978-3-7643-8137-0_2.
[4] Kenneth R. Davidson and Stanislaw J. Szarek. “Local Operator Theory, Random Matrices
and Banach Spaces”. In:Handbook of the Geometry of Banach Spaces. Vol. 1. Elsevier,
2001, pp. 317–366.doi:10.1016/S1874-5849(01)80010-3.
[5] Holger Dette and William J. Studden. “Matrix Measures, Moment Spaces and Favard’s
Theorem for the Interval[0,1]and[0 ,∞)”. In:Linear Algebra and its Applications345
(2002), pp. 169–193.doi:10.1016/S0024-3795(01)00493-1.
[6] Lluis Eriksson.Finite-Sample Spectral-Gap Falsification: Exact Weighted Visibility
Minimax, Hidden-Atom LAN, and Honest Dependent Tests. ARR record ARR-2026-
77QM18J2KG9679B7. 2026.url: https://arr-research.github.io/papers/ARR-
2026-77QM18J2KG9679B7/.
[7] Bernd Fritzsche, Bernd Kirstein, and Conrad Mädler. “Matricial Canonical Moments
and Parametrization of Matricial Hausdorff Moment Sequences”. In:Complex Analysis
and Operator Theory13 (2019), pp. 2123–2169.doi: 10.1007/s11785-017-0754-5 .
arXiv:1711.00797.
[8] Charles J. Geyer. “On the Asymptotics of ConstrainedM-Estimation”. In:The Annals
of Statistics22.4 (1994), pp. 1993–2010.doi:10.1214/aos/1176325768.
[9] J. William Helton and Jiawang Nie. “A Semidefinite Approach for TruncatedK-Moment
Problems”. In:Foundations of Computational Mathematics12 (2012), pp. 851–881.doi:
10.1007/s10208-012-9132-x. arXiv:1105.0410.
[10] Vladimir Koltchinskii and Karim Lounici. “Concentration Inequalities and Moment
Bounds for Sample Covariance Operators”. In:Bernoulli23.1 (2017), pp. 110–133.doi:
10.3150/15-BEJ730. arXiv:1405.2468.
[11] Jean B. Lasserre. “Global Optimization with Polynomials and the Problem of Mo-
ments”. In:SIAM Journal on Optimization11.3 (2001), pp. 796–817.doi: 10.1137/
S1052623400366802.
[12] Helfried Peyrl and Pablo A. Parrilo. “Computing Sum of Squares Decompositions with
Rational Coefficients”. In:Theoretical Computer Science409 (2008), pp. 269–281.doi:
10.1016/j.tcs.2008.09.025.
[13] Motakuri V. Ramana. “An Exact Duality Theory for Semidefinite Programming and Its
Complexity Implications”. In:Mathematical Programming77 (1997), pp. 129–162.doi:
10.1007/BF02614433.
[14] Alexander Shapiro. “Asymptotic Distribution of Test Statistics in the Analysis of Moment
Structures under Inequality Constraints”. In:Biometrika72.1 (1985), pp. 133–144.doi:
10.1093/biomet/72.1.133.
12