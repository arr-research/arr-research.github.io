# Universal optimal tests of unknown unitary dynamics: determinant exponents and tensor stability

Text extraction of canonical paper.pdf; consult PDF for equations.

Universal optimal tests of unknown unitary dynamics:
determinant exponents and tensor stability
Lluis Eriksson
Independent researcher, Sweden
16 October 2026 — Research preprint
Abstract
We study forward-query tests of an arbitrary fixed unitary channel against memoryless
noise with unknown fixed input and output rotations. A Schur–Weyl reduction gives
a family of optimal candidate tests, but leaves a channel-dependent minimization over
partitions. We remove that minimization: the balanced partition is optimal simultaneously
for every channel, every query number and every compact alternative family, even against
adaptive and more general positive physical testers. The key identity expresses each block
acceptance probability as a normalized Schur polynomial averaged over a Gaussian Kraus
matrix. Classical majorization then identifies a universal optimizer. The same identity
determines the exact asymptotic error exponent through the maximum determinant of
a Kraus combination, with explicit polynomial finite-query bounds. Perfect detection is
possible precisely when the Kraus span contains no invertible matrix; its first possible
query number is one more than the maximum matrix rank in that span. For qubits,
all even-query errors are determined by the spin-flip spectrum of the normalized Choi
state. We characterize stability of perfect detection under every tensor partner by a
shrunk-subspace condition, using classical noncommutative-rank theory. A completely
depolarizing partner of dimensiond−1destroys perfect detection whenever this condition
fails. For the qutrit Werner–Holevo channel we compute the exact exponent after adjoining
the smallest possible partner, a depolarizing qubit, and also for its tensor square. The
hypotheses, particularly the independent unknown rotations and the global-unitary null in
the tensor example, are essential.
Keywords:quantum hypothesis testing; Schur polynomials; Gaussian moments; Kraus matrix
spaces; error exponents; noncommutative rank.
1 Introduction and contribution
Can one choose a single experiment that optimally detects any departure from an unknown
unitary dynamics, without knowing the orientation or the type of noise? In general channel
discrimination this is too much to expect. In the rotation-invariant statistical model considered
here, however, the answer is affirmative at every finite query number.
The unitary null is the same unknown channel at every call. The alternative is the same
memoryless CPTP map at every call, with independent unknown input and output rotations
that are fixed throughout the experiment. Performance is measured in the worst case over
these rotations. The experiment we identify depends only on the dimension, the query number
and the permitted false-positive probability. It achieves the optimal failure probability for
each alternative separately, and therefore also for arbitrary compact families of alternatives.
The main mechanism connects quantum testing to classical symmetric-function inequalities.
A Gaussian linear combination of Kraus matrices converts the acceptance probability in
a Schur–Weyl block into an expectation of a normalized Schur polynomial. The balanced
1

partition minimizes these polynomials pointwise. In that block the Schur polynomial reduces
to a determinant power times an elementary symmetric polynomial. This gives an exact error
exponent, a finite-query perfect-detection criterion, and explicit qubit formulas.
What builds on earlier work.Quantum testers and symmetry-based minimax reductions
are established tools [3]. Multiplicity-entangled probes, balanced dimension/multiplicity ratios,
and finite Schmidt-rank truncation appear in Chiribella and Ebler [4], notably their Appendix B.
Antisymmetric probes have also been used for unambiguous unitary comparison [5]. Parallel
optimality for compact-group estimation and subgroup testing has substantial precedents [6, 7].
These constructions and principles are not claimed as new.
The author’s preceding manuscript [8] establishes a complete class for the present two-sided
rotation model, reducing its optimum to a minimum over partitions. It determines the optimizer
for two queries and for complete depolarization, but leaves a general channel-dependent
optimization. We reproduce the needed reduction below and remove that optimization for all
CPTP maps. The resulting determinant exponent and exact rank threshold are additional
conclusions, not consequences of a numerical search.
The majorization inequality itself is classical: Sra [9] proves monotonicity of normalized
Schur functions under dominance. For the particular balanced partition needed here, a short
Muirhead argument suffices. The spin-flip roots used for qubits are the roots in Wootters’
concurrence formula [11]; determinant-based entanglement quantities also occur in Gour’s
work [12]. Our claim is their operational role in this specific minimax testing problem, not a
new symmetric-function inequality or a new concurrence construction.
Werner–Holevo channels are standard examples [13]. Ghosal et al. [14] recently study
testing non-mixed-unitarity, including odd-dimensional Werner–Holevo examples and infinite
Stein exponents. Their null includes mixed-unitary channels, their orientation promise differs,
and their asymptotic error criterion is not the finite perfect-detection problem here. We make
no claim to have first observed the relevance of their parity. Singular matrix spaces and
their behavior under tensor constructions are likewise classical algebraic objects [15, 16]. The
explicit testing consequences below must be read with these distinctions.
An additional question is whether a finite perfect test survives enlarging the system and its
unknown-unitary null. We give a complete answer through shrunk subspaces of the Kraus span.
This is an operational application of classical noncommutative-rank and blow-up theorems, not
a new algebraic characterization. It distinguishes channels whose perfect detection survives
every tensor partner from those for which even a completely depolarizing partner destroys
it. The exact six-dimensional example below quantifies that change and attains the smallest
possible partner dimension.
2 The testing problem and its universal answer
Fix d≥ 2and n≥ 1. LetEbe a CPTP map onCd. WriteUW(X) = WXW †. The hypotheses
are
H0 :UW, W∈U(d),(1)
H1 :UL ◦E◦U R, L,R∈U(d).(2)
The sameW, or the same triple(E,L,R ), is used at all calls. UnderH1 the calls are memoryless.
There is no access to the environment, inverses, or a controlled implementation of an unspecified
dilation. Ancillas, arbitrary causal control and a final binary measurement are allowed.
We use unnormalized Choi matrices,
JE=
∑
i,j
E(|i⟩⟨j|)⊗|i⟩⟨j|,Tr OJE=II.
2

All output legs precede all input legs; a tensor power of a Choi matrix includes this fixed
regrouping. A physical accepting tester effectT⪰ 0has acceptance probability aT(E) =
Tr(TJ⊗n
E ). The accepting outcome acceptsH0. Define
α(T) = 1−inf
W
aT(UW), β E(T) = sup
L,R
aT(UL ◦E◦U R).
Let βn,E(α)be the optimum atα(T) ≤α. For a familyC, also take the supremum overE∈C .
The converse applies to any physically normalized positive-tester class containing parallel
protocols and having the displayed Choi representation. It does not identify arbitrary positive
matrices with physical experiments.
For partitionsλ⊢nwith at mostdrows, Schur–Weyl duality gives
Hn = (Cd)⊗n =
⨁
λ
Vλ ⊗Mλ, q λ = dimVλ =sλ(1d), m λ = dimMλ.
Heres λ is the Schur polynomial. Writen=ad+r,0≤r<d, and
λ∗= ((a+ 1) r,ad−r), q ∗=
(
d
r
)
.
Choose any Kraus representationE(X) = ∑k
j=1 KjXK†
j. Let gj be independent standard
circular complex Gaussian variables, withE|gj|2 = 1, and putG= ∑
j gjKj. For a positive
matrix,e r denotes the elementary symmetric polynomial of its eigenvalues;e0 = 1.
Theorem 2.1(One optimal test for every noise channel).For every0≤α≤1,
βn,E(α) = (1−α)b n(E), b n(E) = E
[
|detG|2aer(G†G)
]
n!
(d
r
) . (3)
At a= 0the determinant factor is1, including for singularG. The same parallel test attains
this optimum for allE: prepare
IV∗
q∗
⊗|ϕm∗ ⟩⟨ϕm∗ |,|ϕ m⟩=m −1/2
m∑
j=1
|j,j⟩,
where one multiplicity register is a bypass reference. After then parallel calls, accept upon
return to the same isotypic block and the same maximally entangled multiplicity state, then
retain acceptance with probability1−α.
For any nonempty compact familyCof CPTP maps,
βn,C(α) = (1−α) max
E∈C
bn(E).(4)
Adaptation and any larger physical positive-tester class as specified above give the same optimum.
The probe and measurement do not depend onEor onC. Their reference dimensionm∗
can grow exponentially withn; the theorem does not claim optimality with a smaller reference.
At n≤d , λ∗= (1n)and m∗= 1: the optimal input is the normalized antisymmetric projector
and the output test is that projector, without a bypass reference. Atn= 1, b1 = 1for every
channel.
3

3 Proof: positive testers, Gaussian moments and majorization
3.1 The complete-class reduction
LetP π permute thenphysical factors and letΠ λ project onto an isotypic block. Define
Sn = 1
n!
∑
π∈Sn
PO
π ⊗P I
π, D λ = (ΠO
λ ⊗Π I
λ)Sn.
Permutation matrices are real in the computational basis; the input Schur spaces are the
conjugate spaces appropriate to vectorization. In compatible Schur bases,
Dλ =IVO
λ
⊗IV
I
λ
⊗|ϕmλ⟩⟨ϕmλ|.
These are orthogonal projectors of rankq2
λ and sum toSn. Define
bλ(E) = Tr(DλJ⊗n
E )
qλmλ
.
Lemma 3.1(Block reduction, following [8]).For each physical T⪰ 0, there are weights
wλ ≥0such that
∑
λ
wλ =c:=
∫
aT(UW)dW≤1,(5)
∫
aT(UL ◦E◦U R)dLdR≥
∑
λ
wλbλ(E).(6)
Each bλ is the acceptance probability of a physical parallel test with null acceptance one. The
same weights work for every CPTP map.
Proof.The Haar null moment is
M0 =
∫
J⊗n
UW dW=
∑
λ
mλ
qλ
Dλ.
Twirl J⊗n
E independently by collective output and input unitaries, obtainingBE. Schur’s
lemma makesBE the identity on each pair of representation factors, tensored with an operator
on their multiplicity factors. The original tensor power, and hence the twirl, commutes with
simultaneous permutations. InMλ ⊗Mµ, the trivial permutation representation occurs only
whenλ=µ, with multiplicity one and vectorϕmλ. Thus everyDλ reducesB E, and
BE=
∑
λ
mλ
qλ
bλ(E)Dλ +B⊥
E, B ⊥
E ⪰0.
Setw λ = (mλ/qλ) Tr(TDλ). Positivity gives the inequality and∑ wλ = Tr(TM0) =c.
To realize a block, prepareIVλ/qλ and a maximally entangled pair betweenMλ and a
reference, and project the output multiplicity and reference back onto that pair, accepting only
in blockλ. Its accepting tester isDλ/(qλmλ). Collective unitaries act trivially on multiplicity,
giving null acceptance one. The accepting tester is invariant under both collective rotations.
This verifies its probability and its physical normalization.
The preceding lemma yields(1−α) minλbλ for a single channel, sincec≥ 1 −α. The next
identity identifies its minimum simultaneously for all channels.
4

3.2 A Gaussian identity
Lemma 3.2(Gaussian–Schur representation).For every partition in the decomposition,
bλ(E) = Esλ(G†G)
n!sλ(1d) .(7)
Proof. Write v= |G⟩⟩= ∑
j gj|Kj⟩⟩, soEvv†= JE. The complex Gaussian moment formula,
obtained by pairing eachgwith a conjugateg, gives
E
[
(vv†)⊗n]
=n!SnJ⊗n
E Sn.
The permutation symmetry makes the two expressions with one or twoSn equal. Since
Dλ ≤Sn,
Tr(DλJ⊗n
E ) = 1
n!E∥Dλ|G⊗n⟩⟩∥2.
For invertibleG, its Schur decomposition isG⊗n = ⨁
λRλ(G)⊗IMλ. Consequently the squared
norm on the right is
mλTr
(
Rλ(G)†Rλ(G)
)
=mλsλ(G†G).
The same formula holds for singularG by polynomial continuity. Division byqλmλ proves the
identity. It also shows that the Gaussian law, and hence the expression, is independent of the
chosen Kraus representation.
3.3 The balanced partition is always minimal
Lemma 3.3(Balanced normalized Schur minimum).For x∈ [0,∞)d and everyλ⊢n with at
mostdrows,
sλ(x)
sλ(1d) ≥ sλ∗ (x)
sλ∗ (1d) = (x1 ···x d)aer(x)
(d
r
) .(8)
Proof. This follows from Sra’s dominance theorem [9], since every partition ofninto at mostd
parts dominatesλ∗. Here is a direct proof of the needed special case. Expandsλ = ∑
µKλµmµ
in monomial symmetric polynomials. The Kostka coefficients are nonnegative integers. After
normalizing at1 d, the result is a convex combination ofmµ(x)/mµ(1d). Every exponent
partition µ has total n and dominates λ∗. Muirhead’s inequality bounds each normalized
monomial mean below by that of λ∗. Finally sλ∗ = mλ∗ = ( x1 ···x d)aer(x), since the
representation is a determinant power times an exterior power. The assertion follows, including
zero coordinates by continuity.
Taking expectations in Lemma 3.3 and using Lemma 3.2 givesbλ(E) ≥bλ∗ (E)for every
channel. Lemma 3.1 now implies
βE(T)≥
∑
λ
wλbλ(E)≥cb λ∗ (E)≥(1−α)b λ∗ (E).
The balanced parallel test attains equality. The same inequalities hold for eachEbefore taking
a supremum, proving both parts of Theorem 2.1. Notice that domination compares with the
original tester’s orbit average, not its error at every specified orientation.
5

4 Determinant geometry gives the exact error exponent
Let k= rankJE and take a minimal Kraus representation. Forz∈C k, putK(z) = ∑
j zjKj,
and define
δ(E) = max
∥z∥2=1
|detK(z)|2/d.(9)
This number does not depend on the minimal Kraus basis. Equivalently,
δ(E) = max{|detA| 2/d :|A⟩⟩⟨⟨A|⪯J E}.(10)
Indeed, for the matrixV whose columns are|Kj⟩⟩, xx†⪯VV † holds exactly whenx= Vz
for some∥z∥≤ 1. Homogeneity permits replacing the ball by its sphere. This also allows
redundant Kraus representations with zero coefficients.
Theorem 4.1(Finite bounds and exact exponent).Ifδ(E)>0, then, forn=ad+r,
δ(E)n ≤bn(E)≤
(
n+k−1
k−1
)
δ(E)n−r. (11)
In particular, at multiples ofd the two bounds differ only by the displayed polynomial. For
fixeddand0≤α<1,
limn→∞−1
nlogβn,E(α) =−logδ(E).(12)
Moreover0 ≤δ≤ 1, andδ= 1exactly for unitary channels. Ifδ= 0, bn = 0for every n≥d .
Proof.FirstK(z)is a contraction for∥z∥= 1: Cauchy–Schwarz gives
∥K(z)v∥2 ≤
∑
j
∥Kjv∥2 =∥v∥2.
Let σ be normalized surface measure on the complex unit sphere andNn,k =
(n+k−1
k−1
)
. The
radial decomposition g = Rz of a complex Gaussian givesER2n = n!Nn,k. Formula (3)
becomes
bn = Nn,k
(d
r
)
∫
|detK(z)|2aer(K(z)†K(z))dσ(z).(13)
The contraction property boundser/
(d
r
)
≤1and gives the upper bound in (11).
For the lower bound, consider the vector-valued homogeneous polynomial of degreen
F(z) = det(K(z)) a ⋀r
K(z).
Forr= 0, the exterior power is the scalar1. Its squared Hilbert–Schmidt norm is the integrand
of (13). For every degree-nhomogeneous polynomial with values in a finite-dimensional Hilbert
space,
∥F(z)∥2 ≤Nn,k
∫
∥F(u)∥2 dσ(u),∥z∥= 1.(14)
To see this directly, use the orthogonal monomialszν, |ν|= n, whose sphere norms squared
are ν!/(n!Nn,k). Cauchy–Schwarz and the multinomial theorem give the evaluation normNn,k.
Applying the scalar inequality componentwise proves the vector case.
Choose a maximizingz in (9). Maclaurin’s inequality giveser(K†K)/
(d
r
)
≥|detK| 2r/d.
Combining this with (14) provesbn ≥δn. Taking logarithms proves (12).
If δ = 1, the maximizing contraction A has every singular value one, so is unitary.
Equation (10) implies JE−|A⟩⟩⟨⟨A|⪰0, with zero partial trace; hence it is zero andE= UA.
The converse is immediate. Finally, δ = 0means the determinant polynomial vanishes
identically, so (3) is zero whenevera≥1.
6

Corollary 4.2(Robust exponent).Fix0 ≤α < 1. For a nonempty compact familyC, let
δC= maxE∈Cδ(E). If δC>0, the worst-case exponent is−logδ C, with the uniform bounds(11)
using k= d2 and δ= δC. If δC= 0, the universal test is perfect for every member atn= d. In
particular, every compact family containing no unitary channel has a strictly positive exponent,
or finite perfect detection.
Proof. Use ad2-column square root of the Choi matrix to parameterize(10). Continuity of
the positive square root and maximization over a fixed compact ball show thatδ is continuous.
Take suprema in (11), use (4), and apply Theorem 4.1.
The determinant maximum can be a difficult polynomial optimization. The theorem gives
an exact invariant and bounds; it does not provide an efficient general algorithm. Nor isδ the
maximum weight of a unitary channel belowEin the CP order. For nontrivial qubit amplitude
damping that weight is zero, whileδis positive, as Section 8 shows.
5 An exact criterion and threshold for perfect detection
Let
ρ(E) = max{rankA:A∈span C(K1,...,K k)}.
This is ordinary matrix-space rank over commuting coefficients. It is independent of Kraus
representation and is not noncommutative rank.
Theorem 5.1(First perfect query number).For0≤α< 1, a finite-query test withβn,E(α) = 0
exists if and only ifρ(E) < d. In that case its smallest query number, for all the strategy
classes in Theorem 2.1, is
nperfect =ρ(E) + 1.(15)
The threshold is attained with an antisymmetric input and output projector, without a bypass
reference.
Proof. For n<d , formula(3) reduces toEen(G†G)/(n!
(d
n
)
). Its integrand is a sum of squared
n×n minors. The expectation is zero exactly when all these polynomials vanish identically,
equivalently when every Kraus combination has rank belown. A nonzero polynomial has
positive squared Gaussian integral. Atn= d the same argument uses the determinant. If an
invertible combination exists,δ >0and Theorem 4.1 rules out zero at everyn. If none exists,
zero is attained atρ+ 1 ≤d, while all smallern have strictly positive error. The balanced
block at that threshold is antisymmetric with multiplicity one.
Thus a question about all adaptive discrimination experiments becomes a question about
the largest nonvanishing minor of a matrix pencil. This is a structural equivalence, not a claim
of deterministic polynomial-time solution of general symbolic determinant identity testing.
6 Which perfect tests survive every tensor partner?
Let S = span{Kj}⊆M d(C)be the Kraus matrix space. ForU⊆C d, writeS(U) = span{Au:
A∈S,u∈U}, and define
c(S) = max
U⊆Cd
(
dimU−dimS(U)
)
.
The zero subspace givesc(S) ≥0. A subspace with positive deficiency is called ashrunk
subspace. For a square channelFon Cm, testingE⊗F means the original model in dimension
dm: the null contains every fixedU(dm)unitary, and the alternative has independent unknown
global input and output rotations. This is not the task obtained by adding a freely bypassing
reference or retaining a product-unitary null.
7

Theorem 6.1(Tensor stability via a classical matrix-space criterion).Fix0≤α< 1. The
following are equivalent:
1. For everym≥ 1and every CPTP mapFon Cm, the channelE⊗F admits a finite perfect
test in the global model.
2.Shas a shrunk subspace, or equivalentlyc(S)>0.
3. The noncommutative rank ofSis less thand.
Ifc=c(S)>0, then for every such partner
ρ(S⊗S F)≤m(d−c), n perfect(E⊗F)≤m(d−c) + 1.(16)
Ifc= 0, the completely depolarizing partnerDd−1 already gives
δ(E⊗D d−1)>0,(17)
so no finite perfect test exists for that partner. HereD1 is the one-dimensional identity channel.
Proof. If U has deficiencyc, every matrix inS⊗S F maps U⊗C m into S(U) ⊗C m. Its kernel
therefore has dimension at leastmc. This proves the rank bound, and Theorem 5.1 gives the
query bound. The resulting antisymmetric test requires no bypass reference since its query
number is at mostdm.
For completeness, the classical noncommutative-rank characterization says
ncrk(S) =d−c(S),
and ncrk(S) = d if and only if a tensor blow-upS⊗M m(C)contains an invertible matrix.
These are established results of matrix-space theory; see the attributions and equivalent
formulations in Ivanyos–Qiao–Subrahmanyam [18] and Li et al. [19], Section II.2 and Theorem
9. Derksen–Makam [17], Theorem 1.8, further shows that when the rank is full an invertible
element exists in every blow-up sizem≥d− 1. Since the Kraus span ofDm is exactlyMm(C),
taking m= d−1gives an invertible Kraus combination forE⊗D d−1. Theorems 4.1 and 5.1
prove (17) and rule out condition 1. The same classical identity proves equivalence with
condition 3.
Corollary 6.2(Unital perfect detection is fragile).IfEis unital, thenc(S) = 0. In particular,
whenever a unital channel admits a finite perfect test, some depolarizing partner of dimension
at mostd−1removes that possibility in the global model.
Proof. For the orthogonal projectionPU, positivity and unitality give0 ⪯E(PU) ⪯I . Its
support isS(U)and trace preservation givesTrE(PU) = dimU. Hence dimU≤dimS (U)for
allU.
The distinction has an algorithmic consequence. When the Kraus span is supplied by a
rational matrix basis, deterministic polynomial-time noncommutative-rank algorithms [15, 18]
decide tensor stability. This invokes those algorithms rather than solving commutative symbolic
determinant identity testing. It also does not supply an efficient optimizer forδ or an efficient
physical implementation of a large-query test.
The stable class is nonempty: for a pure replacer onCd, S(Cd)is one-dimensional, so
c = d−1. Equation (16) yields nperfect ≤m + 1for every m-dimensional partner. For the
partner Dm, the matrix space consists of all maps into a fixedm-dimensional output space
and has maximum rankm, so this bound is attained.
8

7 Qubit channels: the spin-flip spectrum determines every
even error
Let d= 2and choose a minimal Kraus representation, sok≤ 4. Define the complex symmetric
matrixCby
detK(z) =z TCz, C jj = detKj, C ij = 1
2
(
det(Ki +Kj)−detK i −detK j
)
(i̸=j).
Let σ1 ≥···≥σ k ≥0be its Takagi singular values, padded with zeros to four values when
necessary.
Theorem 7.1(Exact qubit formulas).Fora≥1,
δ(E) =σ 1,(18)
b2a(E) = (a!)2
(2a)![ta]
k∏
j=1
(1−4σ 2
jt)−1/2.(19)
If ω= JE/2and ˜ω= (Y⊗Y )ω(Y⊗Y ), whereY is PauliY, then theseσj are the eigenvalues
of √√ω˜ω√ω.
They are the spin-flip roots entering Wootters’ concurrence formula, although here the exponent
depends on their largest value, not on the concurrence combination.
Proof. Takagi factorization and unitary invariance of the complex Gaussian reducedetG to∑
j σjg2
j. Its maximum absolute value on the unit sphere isσ1. Expanding itsath power and
pairing the independent phases gives
E
⏐⏐⏐⏐⏐⏐
∑
j
σjg2
j
⏐⏐⏐⏐⏐⏐
2a
= (a!)2 ∑
a1+···+ak=a
∏
j
(2aj)!
(aj!)2 σ2aj
j .
The generating series of the central binomial coefficients is(1−4t)−1/2, proving (19).
For the spectral identification, set vj = |Kj⟩⟩/
√
2, so ω = ∑
j vjv†
j. The symmetric
preconcurrence matrixτij = v†
i(Y⊗Y )vj equals −Cij in this vectorization convention, by the
polarized determinant identity. Its singular values are therefore those ofC. The standard
ensemble identity in Wootters’ proof [11], or the equality of nonzero spectra of rectangular
matrix products, identifies these with the displayed spin-flip roots.
For example,b2 = ∑
j σ2
j, while
b4 =
∑
j
σ4
j + 2
3
∑
i<j
σ2
iσ2
j.
These formulas require no minimization over experiments. Odd-query errors remain given
exactly by (3); the even-query spin-flip formula alone does not assert that the same four
numbers determine every odd-query error.
8 Examples and a tensor-product obstruction
8.1 Standard channels and normalization checks
For complete depolarization,Kij = |i⟩⟨j|/
√
d. A unit coefficient vector gives∥K(z)∥2
HS = 1/d,
so arithmetic–geometric mean yieldsδ= d−2, attained byK(z) = I/d. The exact finite error
recovers
bn = q∗
dnm∗
,
9

and the exponent is2 logd. Balanced multiplicity probes and this exponential gain have
precedents [4]; they serve here as a check.
For qubit amplitude damping with0≤γ≤1, take
K0 =
(
1 0
0 √1−γ
)
, K 1 =
(
0 √γ
0 0
)
.
ThendetK(z) = √1−γz 2
0, so
δ=
√
1−γ, b 2a = (1−γ) a.
For0 <γ <1the Kraus span contains no nonzero scalar multiple of a unitary: orthogonality
of its columns forces the off-diagonal entry to vanish, and the two diagonal moduli then
differ. Thus no positive unitary CP component exists, despite the finite positive determinant
exponent.
For an orthogonal random-unitary channelE= ∑
j pjUUj, withTr(U†
iUj) =dδij,
|detK(z)|2/d ≤∥K(z)∥2
HS
d =
∑
j
pj|zj|2 ≤pmax.
Selecting a largest-weight Kraus unitary attains equality, soδ = pmax. A pure replacer has
matrix-space rank one and first perfect query number two.
8.2 Werner–Holevo parity
Consider
Wd(X) = Tr(X)I−X T
d−1 , K ij = |i⟩⟨j|−|j⟩⟨i|√
d−1 (i<j).
Its Kraus span is the space of complex skew-symmetric matrices. Ifd is odd, its maximum
rank isd−1, so the first perfect query number is exactlyd. If d is even, an invertible skew
matrix exists. Every unit coefficient vector has squared Frobenius norm2/(d−1), and an
equal-block skew matrix attains equal singular values. Therefore
δ(Wd) = 2
d(d−1) (deven), ξ(W d) = log d(d−1)
2 .(20)
At d= 2this is a unitary channel and the exponent correctly vanishes. Atd= 3, the first
three optimal errors atα= 0are1,1/2,0.
8.3 Perfect detection need not survive a tensor product
The next example changes the null from arbitrary local unitaries on a qutrit to arbitrary global
unitaries on two qutrits. This enlarged null is essential. The underlying rank phenomenon is
already known: Li, Qiao, Wang and Duan [19], Theorem 12, show that the odd-dimensional
skew space has maximum rankd−1while its tensor square has full matrix rankd2, using the
same sum of tensor products of skew basis matrices. We use that established phenomenon
and compute the exact determinant maximum for the qutrit channel, which fixes the testing
exponent.
Theorem 8.1(An exact tensor-square example).The channel W3 has δ = 0and admits
perfect detection in three queries. For the nine-dimensional channelW3 ⊗W3, tested against
arbitrary fixedU(9)dynamics with the corresponding full input and output rotations,
δ(W3 ⊗W3) = 22/9
12 >0, ξ= log 12− 2
9 log 2.(21)
10

Consequently no finite number of queries gives perfect detection in this global model. In
particular, the invariantδis not multiplicative under tensor products.
Proof. Let A1,A2,A3 be the standard real skew basis with nonzero pairs(1,2),(1,3),(2,3)
and entries+1 ,−1. The Kraus matrices of the tensor square areAi ⊗Aj/2. For a coefficient
matrixZ= (z ij),∥Z∥HS = 1, write
G(Z) = 1
2
3∑
i,j=1
zijAi ⊗Aj.
We claim
|detG(Z)|= |detZ|3
256 .(22)
Congruence A↦→UAU T acts on the three-dimensional skew space through ⋀2 U. The
map ⋀2 : U(3) →U (3)is surjective: in a fixed exterior basis it is unitarily equivalent to
U↦→det (U)U, and any target admits such a preimage by choosing a square root of its
determinant. Thus arbitrary left and right unitary transformations ofZ correspond to unitary
congruences of G(Z), preserving both determinant moduli. Singular-value decomposition
reduces (22) toZ= diag(s 1,s2,s3).
In this caseG(Z)preserves the diagonal subspace spanned by|11⟩,|22⟩,|33⟩and the three
two-dimensional subspaces spanned by|ij⟩,|ji⟩. Their block determinants multiply to
detG(diags) =− s3
1s3
2s3
3
256 ,
proving the claim. Under∑ s2
i = 1, the maximum ofs1s2s3 is3 −3/2. Substitution into(9)
with dimension nine gives256−2/9/3 = 2 2/9/12. The exponent and impossibility of finite
perfect detection follow from Theorems 4.1 and 5.1.
There is no contradiction with applying a local perfect test when the null is promised to be a
product unitary. A general entanglingU(9)does not preserve the local antisymmetric structures
used by that test. The example quantifies the effect of enlarging the nuisance group, not a loss
caused by freely adding a known ancillary system. The underlying matrix-space nonsingularity
phenomenon was established in [19] and is related to commutative/noncommutative rank
distinctions [15, 16]; the exact operational exponent is the conclusion established here.
8.4 The smallest partner: an exact depolarizing-qubit exponent
Let D2(X) = Tr(X)I2/2. Theorem 6.1 predicts that a depolarizing qubit suffices forW3, since
the latter is unital. The following calculation evaluates the exponent and proves that partner
dimension two is minimal.
Theorem 8.2(Exact minimal-partner example).In the six-dimensional global-unitary model,
δ(W3 ⊗D2) = 22/3
24 , ξ(W 3 ⊗D2) = log 24−2
3 log 2. (23)
Thus W3 has a three-query perfect test, whereasW3 ⊗D2 has no finite perfect test. No
one-dimensional partner can produce this change.
Proof. Use the skew basisA1,A2,A3 defined above. The twelve Kraus matrices of the product
channel areAi ⊗Eab/2. A normalized combination isG=H/2, where
H=
3∑
i=1
Ai ⊗Xi =


0X 1 X2
−X1 0X 3
−X2 −X3 0

,
∑
i
∥Xi∥2
HS = 1.
11

Let W be the3 ×4matrix whose ith row lists the entries ofXi in the order(00,01,10,11),
and let pabc be its minor on columnsa < b < c, numbered0 ,1,2,3. Expanding the block
determinant gives the polynomial identity
detH=p 013p023 −p012p123.(24)
This identity holds overC without invertibility assumptions on the blocks; it can also be
checked by substituting their twelve entries and collecting terms. The degree-six polynomial is,
up to sign convention, the classical2×2 ×3hyperdeterminant: see Lim’s minors expression [1],
slide 32, and Bremner [2]. Neither that invariant nor the minors expression is claimed as new
here. The triangle inequality,2|uv|≤|u|2 +|v|2, and Cauchy–Binet give
|detH|≤ 1
2
∑
a<b<c
|pabc|2 = 1
2 det(WW†)≤ 1
2
(
TrWW †
3
)3
= 1
54.
Equality is attained by(X1,X2,X3) = ( I2,σx,σz)/
√
6. Before the factor1 /
√
6, the corre-
spondingHhas determinant4and singular values2,2,1,1,1,1. Consequently
max|detG|= 1
26 54 = 1
3456.
Taking the power2/6gives (23), and Theorem 4.1 gives its exponent. Every channel on a
one-dimensional system is the identity, leaving the singular skew space unchanged; hence
dimension two is minimal.
The stable and unstable cases now have explicit representatives with sharp constants. A
pure replacer retains a finite perfect test under every partner, while the unital qutrit example
loses perfect detection under the smallest possible nontrivial depolarizing partner. The blow-
up criterion and the skew-space rank phenomenon are established algebra [19, 17]; the test
interpretation and the two exact determinant maxima are the specific conclusions proved here.
9 Verification, limitations and research provenance
The proofs above are analytic. The accompanying programs provide reproducible finite
checks by different expressions: direct Choi contractions in permutation projectors, Gaussian
polynomial coefficient moments, normalized Schur evaluations, Takagi spectra and spin-flip
spectra. The checks include 99 direct channel/query cases, 90 even-query qubit moment
comparisons through twelve queries, and 252 exact rational Schur inequalities. The maximum
discrepancy between direct balanced-block contractions and Gaussian moments is2.23 ×10−16.
An exact symbolic calculation verifies the diagonal tensor-square determinant, and 100 complex
coefficient matrices verify its general form numerically, with maximum absolute discrepancy
below2 .4 ×10−20. The latter checks supplement the congruence proof; they do not establish a
polynomial identity on their own. For the new six-dimensional example, symbolic expansion
verifies the full twelve-variable determinant identity, and 300 random complex coefficient arrays
check both that identity and the sharp upper bound. An exact pure-replacer example checks
the stable-class rank bound.
The general spin-flip square root was evaluated through a Hermitian positive spectral
decomposition. A preliminary generic matrix-square-root computation on rank-deficient
matrices produced spurious small roots; that numerical implementation was corrected before
recording these results. No proof-assistant formalization is claimed.
The result requires independent unknown common input and output rotations, memoryless
calls, arbitrary reference size and a fixed false-positive tolerance. It does not assert parallel
12

optimality for calibrated noise, correlated environments, or a fixed memory budget. The
determinant formula is not a channel capacity and does not imply an efficient solution of
its maximization. The finite-query bounds are explicit but can be loose; a sharp polynomial
prefactor for general channels remains open.
The 16 October refresh searched 909 available complete texts and 122 supplementary
texts, refreshed 58 repository trees and the official source indices, and checked the current
Erdős problem index. Existing remote PDFs were not all downloaded again. The search
preceding this manuscript revisited the OpenAI mathematical corpus, the author’s AIRR
and viXra-indexed works and research repositories, and the cited DeepMind and Anthropic
research indices. The delivered search audit distinguishes automatic indexing and text triage
from proof-level reading. It does not claim that every frontier publication or every proof has
been examined. The proposed contribution is the universal optimizer and its determinant/rank
consequences in the stated model. Worldwide novelty and research impact remain subject to
expert scrutiny.
AI assistance.OpenAI Codex assisted substantially with research selection, mathematical
development, writing and computation. A separate GPT-6 Astra xhigh context challenged
the developing argument and contributed the signed-minor derivation and saturation check in
Theorem 8.2. That context therefore participated in development; its calculations are not an
independent review of that result. Any additional retained review is identified by its exact
manuscript hash and remains advisory and from the same provider. This is not independent
human peer review. No report is attributed to Claude unless an actual report is produced and
retained. The author is responsible for the submitted claims and references.
References
[1] L.-H. Lim, Hyperdeterminants, secant varieties, and tensor approximations, lecture slides
(23 April 2008), slide 32 of 37. Author-hosted slides.
[2] M. R. Bremner, A hyperdeterminant for2×2×3arrays, arXiv:1106.2988v1 (2011).
[3] K. Nakahira and K. Kato, Generalized quantum process discrimination problems,Phys.
Rev. A103, 062606 (2021); erratum104, 069902. arXiv:2104.09759.
[4] G. Chiribella and D. Ebler, Quantum speedup in the identification of cause–effect relations,
Nature Communications10, 1472 (2019). arXiv:1806.06459, especially Appendix B.
[5] M. Sedlák and M. Ziman, Unambiguous comparison of unitary channels,Phys. Rev. A
79, 012303 (2009). arXiv:0809.4401.
[6] M. Hayashi, Indefinite causal order strategy does not improve the estimation of group
action,Quantum9, 1891 (2025). arXiv:2501.09312.
[7] M. Hayashi, Y.-A. Chen, C. Zhu and X. Wang, Predicting symmetries of quantum
dynamics with optimal samples, arXiv:2502.01464 (2025).
[8] L. Eriksson, A complete class of optimal quantum tests for unknown unitary dynam-
ics, AIRR Working paper ARR-2026-5MAVBFTEF48DX8RT, v1 (16 October 2026).
Permanent version.
[9] S. Sra, On inequalities for normalized Schur functions,European Journal of Combinatorics
51, 492–494 (2016). arXiv:1502.04753v3.
13

[10] I. G. Macdonald,Symmetric Functions and Hall Polynomials, second edition, Oxford
University Press (1995).
[11] W. K. Wootters, Entanglement of formation of an arbitrary state of two qubits,Phys.
Rev. Lett.80, 2245–2248 (1998). arXiv:quant-ph/9709029.
[12] G. Gour, Mixed-state entanglement of assistance and the generalized concurrence,Phys.
Rev. A72, 042318 (2005). arXiv:quant-ph/0506229.
[13] R. F. Werner and A. S. Holevo, Counterexample to an additivity conjecture for output pu-
rity of quantum channels,J. Math. Phys.43, 4353–4357 (2002). arXiv:quant-ph/0203003.
[14] P. Ghosal, P. Halder, A. Patra and A. Sen(De), Quantum hypothesis testing of
non-mixed-unitarity: A multifaceted hierarchy of quantum channel discrimination,
arXiv:2609.40355v2 (2026).
[15] A. Garg, L. Gurvits, R. Oliveira and A. Wigderson, Operator scaling: theory and
applications, arXiv:1511.03730v4 (2019).
[16] H. Derksen and V. Makam, On non-commutative rank and tensor rank, arXiv:1606.06701
(2016).
[17] H. Derksen and V. Makam, Polynomial degree bounds for matrix semi-invariants,Advances
in Mathematics310, 44–63 (2017). arXiv:1512.03393, Theorem 1.8.
[18] G. Ivanyos, Y. Qiao and K. V. Subrahmanyam, Constructive noncommutative rank
computation is in deterministic polynomial time, arXiv:1512.03531v6 (2018).
[19] Y. Li, Y. Qiao, X. Wang and R. Duan, Tripartite-to-bipartite entanglement transformation
by stochastic local operations and classical communication and the structure of matrix
spaces, arXiv:1612.06491v2 (2017), Section II.2 and Theorems 9 and 12.
14