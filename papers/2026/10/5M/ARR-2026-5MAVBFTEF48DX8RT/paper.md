# A complete class of optimal quantum tests for unknown unitary dynamics

Text extraction of the canonical PDF. Consult paper.pdf for mathematical typography.

A complete class of optimal quantum tests
for unknown unitary dynamics
Lluis Eriksson
Independent researcher, Sweden
15 October 2026 — Research draft
Abstract
We consider repeated forward access to an unknown quantum channel. The null
hypothesis is an arbitrary fixed unitary channel; the alternative is a memoryless channel
whose input and output rotations are unknown but fixed across all uses. We prove a
complete-class theorem: every physical positive tester is dominated, in orbit-averaged
alternative acceptance and worst-case null acceptance, by a classical randomization of
explicitly realizable parallel tests. The tests are indexed by partitions of the query number,
prepare a maximally mixed representation register, entangle the multiplicity register with a
reference, and measure return to that entanglement. Consequently, for any compact family
of noise channels, the exact finite-query minimax problem reduces to a classical optimization
over partitions. For one specified noise channel the complete error tradeoff is a minimum
of explicit Choi-polynomial invariants. Adaptation and any larger positive-tester class
containing parallel protocols give the same optimum. We derive the channel-independent
optimal two-query test and its failure probability in terms of Choi purity and nonunitality.
For complete depolarization we obtain the exact error at every dimension, query number
and parallel reference dimension, recovering the known exponential benefit of multiplicity
entanglement. We also give an error exponent for orthogonal random-unitary noise. The
result requires both unknown rotations and memoryless uses; it does not establish parallel
optimality for calibrated noise or arbitrary channel discrimination.
Keywords:quantum hypothesis testing; unknown unitary channels; Schur–Weyl duality;
quantum testers; minimax risk; reference dimension.
1 Introduction
An unknown unitary transformation can scramble the coordinates of a quantum state while
preserving reversibility. A noisy channel can change both coordinates and purity. Distinguishing
these possibilities is therefore a different task from checking whether a device implements one
prescribed gate. If neither the input nor the output orientation of the noise is calibrated, a
natural performance criterion is the worst case over those orientations.
This paper gives an exact reduction of that problem at finite query number. The reduction
holds simultaneously for every memoryless noise channel, rather than only for an example
chosen in advance. Once the unknown rotations have been accounted for, every admissible
test can be replaced by a lottery over a finite family of parallel tests. The resulting weights
are nonnegative and sum to the test’s Haar-averaged null acceptance. This is stronger than
exhibiting one good probe or an asymptotic scaling: it identifies a complete class of decision
procedures for every rotation-invariant alternative family.
The key point is a joint use of two symmetries. Independent collective unitary rotations
on the input and output identify representation blocks. Simultaneous permutation of the
identical channel uses then singles out a one-dimensional invariant vector in each matched
1

pair of multiplicity spaces. On the support of the unitary null, every twirled noise operator is
scalar on the resulting blocks. Crucially, each scalar block corresponds to a physical parallel
test. Positivity outside the null support completes the converse without requiring the detailed
normalization constraints of an adaptive circuit.
Relation to prior work.Quantum testers, convex duality, symmetry reductions and
minimax process discrimination are established tools; see Nakahira and Kato [1]. Chiribella
and Ebler [2] introduced multiplicity-entangled probes and coherent superpositions of singlet
groupings for causal identification. Their Appendix B also identifies balanced partitions through
dimension/multiplicity ratios and, in Eqs. (43)–(44), the finite Schmidt-rank truncation by
min(K,mλ). Neither these constructions nor the doubled depolarizing exponent are claimed
here as new.
Parallel optimality itself also has substantial precedents. Hayashi [4] proves it for compact-
group unitary estimation. Chen et al. [5] and Hayashi et al. [6] study unitary symmetry
testing, including positive-tester converses and an exact max-relative-entropy formula. Their
hypotheses concern distributions of unitary operations and subgroup membership. Here the
alternative consists of tensor powers of general, potentially nonunital channels, independently
rotated at their input and output. The explicit simultaneous reduction for all such alternatives
is the proposed contribution. The proof uses the additional permutation symmetry of the
memoryless channel Choi operator.
Unitarity estimation [7], testing against a known target under depolarizing noise [8], and
comparison of unknown unitaries [9] address related but different statistical promises. The
null in non-mixed-unitarity testing [10] includes every mixed-unitary channel; our null includes
only a single unknown unitary repeated throughout the experiment. These null families must
not be interchanged. Resource constraints in subgroup testing have recently been studied
in [11]; the reference-dimension result below concerns complete depolarization and a different
null.
Earlier work by the present author used algebraic query support for restricted unitary
families [12], and established a minimax parallel formula for Schur noise with an unknown
phase carrier together with an adaptive advantage after calibration [13]. The present result
handles arbitrary CPTP channels under full, independent input and output rotations. It does
not remove the calibration distinction established in that work. The literature comparison is a
priority assessment for this draft, not an independent confirmation of novelty.
2 Statistical model and notation
Let d≥ 2, n≥ 1, and letE: L(Cd) →L(Cd)be completely positive and trace preserving
(CPTP). WriteUW(X) =WXW †. The two hypotheses are
H0 :U W for an arbitraryW∈U(d),(1)
H1 :U L ◦E◦U R forE∈C, L,R∈U(d),(2)
where Cis a nonempty compact family of CPTP maps. The sameW, or the same triple
(E,L,R ), is used at allncalls. The calls underH1 are memoryless, so their joint Choi operator
is a tensor power. There is no access to inverse gates, controlled versions of an unspecified
dilation, or the environment.
We use the unnormalized Choi convention
JE=
d∑
i,j=1
E(|i⟩⟨j|)⊗|i⟩⟨j|,Tr OJE=II,TrJ E=d.(3)
2

All output legs are placed before all input legs. In this ordering,J⊗n
E always means the tensor
product followed by that fixed regrouping. For a unitary,JUW = |W⟩⟩⟨⟨W|, with vectorization
in the displayed basis.
The outcome calledacceptaccepts H0. Every ordinary adaptive protocol withn calls has
a positive tester effectTsuch that its acceptance probability on a channelFis
aT(F) = Tr
(
TJ⊗n
F
)
.(4)
The converse will use onlyT⪰ 0and0 ≤aT(UW) ≤1. It therefore also applies to any more
general physically normalized positive-tester model, including indefinite-order models with this
multilinear Choi representation. This is not a claim that every positive matrix is a physical
protocol.
Define the errors
α(T) = 1−inf
W∈U(d)
aT(UW),(5)
βC(T) = sup
E∈C
sup
L,R∈U(d)
aT(UL ◦E◦U R).(6)
For a strategy classS, letβS
n,C(α)be the infimum of the latter error subject toα(T) ≤α .
Randomized decisions are allowed. Haar measures below have mass one.
2.1 Schur blocks and explicit invariants
LetYn,d be the partitionsλ⊢nwith at mostdrows. Schur–Weyl duality gives
Hn = (Cd)⊗n =
⨁
λ∈Yn,d
Vλ ⊗Mλ, q λ = dimVλ, m λ = dimMλ.(7)
WriteΠ λ for the isotypic projector. IfPπ permutes thenphysical factors, define
Sn = 1
n!
∑
π∈Sperm
n
PO
π ⊗P I
π, D λ = (ΠO
λ ⊗Π I
λ)Sn.(8)
Here Sperm
n denotes the permutation group, to distinguish it from the averaging projector
Sn. The permutation matrices in the computational basis are real. Input Schur spaces are
identified with the conjugate spaces in the vectorization convention. In compatible Schur
bases,
Dλ =IVO
λ
⊗IV
I
λ
⊗Φ mλ,Φ m =|ϕm⟩⟨ϕm|,|ϕ m⟩= 1√m
m∑
a=1
|a,a⟩.(9)
Thus theDλ are orthogonal projectors of rankq2
λ.
The quantities that determine the answer are
bλ(E) = Tr
(
DλJ⊗n
E
)
qλmλ
. (10)
They are explicitly defined degree-n polynomials in the Choi entries. They lie in[0,1]and are
invariant under independent unitary rotations at the input and output, as also follows from
the physical realization below. Their definition does not entail a polynomial-time evaluation
algorithm innandd.
3

3 A complete class and the exact minimax formula
Theorem 3.1(Simultaneous parallel domination).For every physical positive testerT, put
c=
∫
aT(UW)dW, w λ = mλ
qλ
Tr(TDλ).(11)
Then wλ ≥0and ∑
λwλ = c≤ 1. There is a parallel randomized test˜T, depending only on
these weights, such that
a˜T(UW) =cfor everyW,(12)
a˜T(UL ◦E◦U R) =
∑
λ
wλbλ(E)≤
∫
aT(UL′◦E◦U R′)dL′dR′ (13)
for every CPTP channelEand everyL,R.
The inequality is with the original test’sorbit average, not its performance at each
particular orientation. Since an average is at most a supremum, the theorem gives simultaneous
domination for the worst-case risk used here. At the null, the constantcis at least the original
test’s minimum acceptance.
Corollary 3.2(Robust alternatives).For0 ≤α≤ 1, let∆( Yn,d)denote the probability
simplex onYn,d. Then
βS
n,C(α) = (1−α) min
p∈∆(Yn,d)
sup
E∈C
∑
λ∈Yn,d
pλbλ(E). (14)
This holds for parallel strategies, all causal strategies, and any physically normalized positive-
tester classSbetween them and the positivity relaxation used in Theorem 3.1. A minimizingp
is implemented by selecting a partition with probabilitypλ, performing its parallel test, and
accepting a successful outcome with probability1−α.
Proof. For α <1, an admissible T has c≥ 1 −α > 0. Set pλ = wλ/c in Theorem 3.1.
Nonnegativity of everybλ gives the lower bound in(14). The stated construction attains the
upper bound. The objective is continuous on a compact simplex, so a minimizer exists. At
α= 1, always rejecting gives zero.
For finitely many canonical noise modelsE1,...,E k, the remaining optimization is the
ordinary linear program
min
p,t
tsubject top≥0,
∑
λ
pλ = 1,
∑
λ
pλbλ(Ej)≤t(1≤j≤k).(15)
The same theorem applies to any compact alternative set invariant under independent input
and output rotations, including distance-based promises invariant under those rotations.
Computing its supremum over channels can remain difficult. If the alternative contains a
unitary channel, the optimum is necessarily1−α; a nontrivial uniform testing problem requires
a separated alternative.
Corollary 3.3(A specified channel up to rotations).ForC={E},
βn,E(α) = (1−α) min
λ∈Yn,d
bλ(E). (16)
One partition, with a reference of dimensionmλ, suffices. The entire optimal error tradeoff is
linear in1−α.
4

4 Proof of the complete-class theorem
4.1 The support of the unitary null
Define
M0 =
∫
|W⊗n⟩⟩⟨⟨W⊗n|dW.(17)
In (7), W⊗n = ⨁
λWλ⊗IMλ. Schur orthogonality eliminates cross terms between inequivalent
U(d)representations and sends |Wλ⟩⟩⟨⟨Wλ|to I/qλ. The vectorization ofIMλ has squared
normm λ. Hence
M0 =
∑
λ∈Yn,d
mλ
qλ
Dλ.(18)
The identity(9) follows independently by averaging the diagonal permutation action: the trivial
representation occurs inMλ ⊗Mµ precisely whenλ= µ, and then with multiplicity one. This
uses the real self-duality of symmetric-group irreducibles. In particularsuppM0 = ⨁
λranDλ.
4.2 The noise block lemma
Let
BE=
∫
J⊗n
UL◦E◦UR dLdR.(19)
In the chosen conventionJUL◦E◦UR = (L⊗R T)JE(L⊗R T)†. Both Haar twirls are therefore
collective unitary twirls on the two sides.
Lemma 4.1.For every CPTPE,
BE=
∑
λ∈Yn,d
mλ
qλ
bλ(E)Dλ +B⊥
E, B ⊥
E ⪰0, B ⊥
EDλ = 0.(20)
Proof. The independent twirls makeBE block diagonal in the labels(λ,µ)and proportional to
the identity onVO
λ ⊗VI
µ. Moreover,J⊗n
E is invariant under conjugation byPO
π ⊗P I
π, because
these operations jointly permute identical Choi factors. The twirls preserve this invariance.
In the( λ,λ)block, the multiplicity operator thus commutes with the diagonal symmetric-
group action. Its trivial subrepresentation is the single vector|ϕmλ⟩. It cannot couple that
vector to a nontrivial subrepresentation. ConsequentlyDλ is a reducing subspace on which
BE is scalar. SinceDλ commutes with both twirls,
BEDλ = Tr(DλBE)
q2
λ
Dλ = Tr(DλJ⊗n
E )
q2
λ
Dλ = mλ
qλ
bλ(E)Dλ.(21)
The restriction to the orthogonal complement is positive, which proves (20).
Taking the trace againstT⪰0proves
Tr(TBE)≥
∑
λ
wλbλ(E).(22)
Equation (18) gives∑ wλ =c. These are the only facts needed for the converse.
5

4.3 Realization of every block
For a selected partitionλ, prepare on then input systems and a referenceA≃C mλ the state
ρλ = IVλ
qλ
⊗Φ MλA,(23)
embedded in theλ sector ofHn. Apply then channel calls in parallel and accept with the
effect
Fλ =IVO
λ
⊗Φ MO
λ A,(24)
extended by zero on the other output sectors. No purification of the maximally mixed
representation register needs to be retained.
The null channel acts only onVλ, so acceptance is exactly one for everyW. The input
state is invariant under collective input rotations and the measurement under collective output
rotations. Acceptance underEis therefore orientation independent. A direct Choi contraction
of (23) and (24) gives the tester
Tλ = Dλ
qλmλ
, a Tλ(E) =b λ(E).(25)
For example Tr(TλM0) = 1, checking all normalization factors. Choosing this test with
probabilitywλ and otherwise rejecting yields Theorem 3.1.
Remark4.2 (Why both rotations matter).The proof does not symmetrize an adaptive
circuit and assert that it becomes parallel. It first proves a positive-operator decomposition,
then realizes each surviving block in parallel. An output twirl alone need not make the
multiplicity/input operator scalar onDλ. Likewise, correlated noise need not have the required
permutation symmetry or tensor-power Choi operator. Neither case is covered by the theorem.
5 The universal optimal two-query test
At n= 1there is only one sector andb(1)(E) = TrJE/d= 1: one call has no power for this
minimax problem. Atn = 2, write+and −for the symmetric and antisymmetric sectors.
Their multiplicities are one and their representation dimensions areq±=d(d±1)/2.
Theorem 5.1.For everyd-dimensional CPTP channel, set
s= Tr
[
E(I) 2]
, p= Tr(J 2
E).(26)
Then
b±(E) = d2 ±(s+d) +p
2d(d±1) ,(27)
β2,E(α) = (1−α) d2 −d−s+p
2d(d−1) .(28)
Antisymmetric probes have antecedents in unambiguous unitary comparison [3]. In the present
two-sided rotation model, the antisymmetric test is optimal simultaneously for everyE. It uses
the normalized antisymmetric projector as input and checks antisymmetry at the output, with
no retained reference system.
Proof.LetF O,FI swap the two output and input registers. Sincem±= 1,
D±= 1
4 (I±F O)(I±F I).(29)
6

The four contractions againstJ⊗2
E are respectivelyd2, s, d, andp, proving(27). Subtracting
gives
b+(E)−b −(E) = ds−p
d(d2 −1) ≥0.(30)
Indeed E(I) ⪰ 0has trace d, so s≥d , while JE ⪰ 0has trace d, so p≤d 2. Apply
Corollary 3.3.
For qubits, write the Bloch action asx↦→Ax+t, with a real3×3matrixA. Then
β2,E(α) = (1−α) 1 +∥A∥2
F −∥t∥2
2
4 .(31)
This is an operational meaning of a familiar combination of purity and nonunitality invariants;
the SWAP contraction itself is standard. For amplitude damping with damping probability
γ, the value atα= 0is1 −γ. For a replacement channelX↦→Tr(X)σ, it is(1 −Trσ 2)/2,
so a pure-state replacement is perfectly distinguishable using two queries. For complete
depolarization, it is(d−1)/(2d)in dimensiond.
The formula also immediately solves any two-query robust alternative: take the supremum
of (28) over its canonical channels. No optimization over a different input state for each
channel is necessary.
6 Exact reference cost for complete depolarization
LetD(X) = Tr(X)I/d. ThenJ D=I/d, and
bλ(D) = qλ
dnmλ
.(32)
We refine this benchmark by bounding the dimensionK≥ 1of the quantum reference retained
outside then parallel calls. Probe entanglement among then inputs is unrestricted. This
constraint is not the incoherent-access model of [7], nor a bound on all working memory in an
adaptive circuit.
Theorem 6.1(Finite reference dimension).Writen=ad+r, where0≤r<d, and define
λ∗= (a+ 1,...,a+ 1  
r
,a,...,a 
d−r
), q ∗=
(
d
r
)
, m ∗= dimMλ∗.(33)
For parallel tests with reference dimension at mostK,
βpar,K
n,D (α) = (1−α) min
λ∈Yn,d
qλ
dnmin(K,mλ) = (1−α)
(d
r
)
dnmin(K,m∗). (34)
With unrestricted reference, this is also the optimum for all the tester classes in Corollary 3.2.
Proof. First twirl an arbitrary parallel input by a collective unitary. This does not change
the alternative output. Its null acceptance, for a fixed measurement and anyW, becomes the
original Haar-averaged null acceptance, which is at least1−α. The input can thus be written
ρ=
⨁
λ
IVλ
qλ
⊗Xλ, X λ ⪰0,
∑
λ
TrXλ = 1.(35)
The reference marginal isρA = ∑
λTrMλ Xλ. Twirling the measurement at the output changes
neither acceptance probability, and gives blocksIVλ ⊗Qλ, with0⪯Q λ ⪯I.
7

Table 1: Exact depolarizing failure probabilities for qubits at zero false positives. The reference
dimension is K; the last column is the unrestricted optimum, also valid against adaptive
testers.
n q ∗ m∗ K= 1K≥m ∗
2 1 11/4 1/4
3 2 21/4 1/8
4 1 21/16 1/32
5 2 51/16 1/80
6 1 51/64 1/320
8 1 141/256 1/3584
For every positiveXonC m ⊗C K, the Schmidt-rank inequality gives
X⪯min(m,K)I m ⊗TrCm X.(36)
For a rank-oneX this is the Cauchy–Schwarz inequality on its Schmidt expansion; summing a
rank-one decomposition proves the general case. In particular,
Xλ ⪯min(mλ,K)I Mλ ⊗ρA.(37)
The alternative acceptance consequently satisfies
1
dn
∑
λ
qλTr
[
Qλ(IMλ ⊗ρA)
]
≥min
λ
qλ
dnmin(K,mλ)
∑
λ
Tr(QλXλ)(38)
≥(1−α) min
λ
qλ
dnmin(K,mλ).(39)
Equality is attained in any selected sector by usingIVλ/qλ, a maximally entangled state of
Schmidt rankmin(K,mλ)in Mλ ⊗A, its return projector, and acceptance thinning by1−α.
It remains to optimize the partition. The standard dimension formulas imply
qλ
mλ
=
∏d
i=1(λi +d−i)!
n! ∏d−1
j=0 j!
.(40)
Moving a box from a longer row to a shorter row, while keeping a partition and with row
lengths differing by at least two, strictly decreases the numerator. Repeated balancing reaches
λ∗. This is the balanced-ratio property also proved in [2, Appendix B].
We also needqλ ≥q∗. Every partition ofn with at mostd parts dominatesλ∗. By the
classical dominance criterion for Kostka numbers [14, Chapter I], theU(d)representation
Vλ contains the weightλ∗. Its distinct coordinate permutations are also weights, each with
positive multiplicity. There are
(d
r
)
such permutations. On the other handVλ∗ is a determinant
twist of⋀rCd, soq∗=
(d
r
)
.
Thus qλ ≥q∗and qλ/mλ ≥q∗/m∗. If K≤m ∗the first inequality givesqλ/min (K,mλ) ≥
q∗/K. IfK≥m ∗the second givesqλ/min(K,m λ)≥q ∗/m∗. Both cases prove (34).
For fixedd, Stirling’s formula applied to (40) gives
m∗
q∗
= Θd
(
dnn−(d2−1)/2
)
, β n,D(0) = Θd
(
n(d2−1)/2d−2n
)
.(41)
IfK n = exp(κn+o(n))withκ≥0, then
limn→∞−1
nlogβpar,Kn
n,D (0) = logd+ min(κ,logd).(42)
8

The endpoints recover the known exponential advantage of multiplicity entanglement [2]. The
finite-K identity applies the Schmidt-rank truncation of [2, Appendix B, Eqs. (43)–(44)] to
the present asymmetric testing problem and establishes its corresponding converse, including
query numbers not divisible byd.
7 An exponent and a stability bound
Proposition 7.1(Orthogonal random-unitary noise).SupposeE= ∑s
a=1 paUUa, wherepa >0,∑ pa = 1, andTr(U†
aUb) =dδab. Setpmax = maxapa. For any fixed0≤α<1,
limn→∞−1
nlogβn,E(α) =−logp max.(43)
Proof. The channel tensor power contains the componentU⊗n
Ua with probability pn
a. This
component is an admissible null, also after input and output rotations. Positivity gives the
lower bound(1−α)p n
max for every admissible tester.
For the upper bound, send one half of a maximally entangledd-dimensional pair through
each channel call. The null output is a tensor power of the same pure state inCd2
. Accepting
its full symmetric subspace has null acceptance one. For the alternative, the normalized Choi
state has eigenvaluesp1,...,p s, unaffected by the two rotations. The symmetric-projector
acceptance is the complete homogeneous polynomial
hn(p) =
∑
k1+···+ks=n
∏
a
pka
a ≤
(
n+s−1
s−1
)
pn
max.(44)
Thin acceptance by1 −α and take logarithms. The polynomial prefactor does not affect the
exponent.
This benchmark uses the standard pure-state symmetric-subspace test. It is not asserted
to be optimal at finiten. In particular it can be far from the balanced-sector optimum for
complete depolarization.
Proposition 7.2(Model perturbation).For two canonical CPTP mapsE,F,
|βn,E(α)−β n,F(α)|≤(1−α) min
{
1,n
2 ∥E−F∥ ⋄
}
.(45)
Proof. The tensor-power telescoping identity gives∥E⊗n −F⊗n∥⋄≤n∥E−F∥ ⋄. For a fixed
probe and effect the probability difference is at most half the trace-norm difference of the
output states, and at most one. Apply this to every test(23)–(24), take minima overλ, and
use (16).
8 Verification, scope and remaining questions
The results above are analytic consequences of finite-dimensional representation theory and
tester positivity. Computation was used to challenge normalization, feasibility and small-
parameter consequences, not to replace the all-parameter proofs. The accompanying scripts
and machine-readable reports record:
• 91 channel/dimension/query cases, including random CPTP maps, unitary channels, com-
plete depolarization, pure replacement, amplitude damping and dephasing; projectors were
built from permutation characters for(d,n) = (2,1),(2,2),(2,3),(2,4),(3,2);
9

• exact-design twirl checks for qubits up to three queries, with maximum block residual
3.1 ×10−15 and worst negative eigenvalue magnitude1.5 ×10−15 in the predicted dual
inequality;
• 12 unrestricted two-query causal semidefinite programs, using four channels and three
false-positive allowances, agreeing with(16) to within4 .5 ×10−8; some solver outcomes
were marked numerically inaccurate and are retained as such in the report;
• 75 direct probe/channel/measurement calculations with explicit three- and four-qubit
multiplicity spaces, random input/output rotations and reference dimensions one or two;
• 11,626 exact rational partition comparisons and 80,909 exact finite-reference comparisons
for2≤d≤7,1≤n≤24.
Thechecksarereproduciblebutarenotindependentpeerrevieworproof-assistantformalization.
The numerical twirl checks use the 24-element single-qubit Clifford group only in its valid
unitary-three-design range; they do not substitute a Clifford twirl for a fourth Haar moment.
The principal limitation is the statistical promise. Full uncertainty in both collective
orientations makes the complete-class reduction possible. The theorem neither says that
adaptation is useless for general noisy-channel discrimination nor supplies an efficient laboratory
implementation of every large Schur transform. Preparation and measurements are ideal, the
system dimension is known, and the noise has no temporal memory. Reference dimension in
Theorem 6.1 constrains only a parallel bypass system.
For a general channel, the minimizing partition in(16)remains a finite optimization problem.
We do not claim that the balanced partition is universally optimal outside the depolarizing
benchmark. Determining useful closed forms for broader noise families, the computational
complexity of the robust optimization, and the extent to which partial calibration restores an
adaptive advantage are natural next questions. A specialist assessment of the complete-class
theorem and its relationship to existing covariant testing theory remains necessary before
assigning a strong novelty or impact claim.
A Evaluation without Haar integration
The central projector is
Πλ = mλ
n!
∑
σ∈Sperm
n
χλ(σ)Pσ.(46)
Because diagonal permutation invariants pair only identical labels,(Πλ ⊗I)Sn = Dλ. Conse-
quently
bλ(E) = 1
qλ(n!)2
∑
σ,π∈Sperm
n
χλ(σ) Tr
[
(PO
σ PO
π ⊗P I
π)J⊗n
E
]
.(47)
This is a finite expression in permutation contractions, independent of a choice of Kraus
representation. It gives a direct evaluation method for smalln.
For another expression, let{Ka}be any Kraus family andKa = Ka1 ⊗···⊗K an. Regard
the compressionKa,λ = ΠλKaΠλ as an operator onVλ ⊗Mλ. Projection of its vectorization
onto|ϕmλ⟩contracts the multiplicity indices and supplies a factorm−1/2
λ . Thus
bλ(E) = 1
qλm2
λ
∑
a
∥TrMλ Ka,λ∥2
HS .(48)
This expression makes positivity transparent, whereas the physical test proves the upper bound
one.
10

B A single operator certificate
Letb= min λbλ(E). Equations (18) and (20) give
BE−bM0 ⪰0.(49)
For everyT⪰ 0satisfying Tr(TM0) ≥1 −α, this certifiesTr(TBE) ≥b (1 −α). Equality
is attained by the explicitly physical test in any minimizing sector. In max-relative-entropy
notation, with the usual support convention,
b= exp[−Dmax(M0∥BE)], D max(A∥B) = log inf{t:A⪯tB}.(50)
The use of this divergence for exact unitary hypothesis testing has antecedents in [5, 6].
Here the block lemma computes it for rotated memoryless CPTP alternatives and proves
simultaneous attainability, including the caseb= 0.
Reproducibility and assistance.The companion directory contains the verification scripts,
their output reports, the search-coverage audit and a claim-by-claim proof audit. OpenAI
Codex assisted with retrieval, mathematical development, computation and typesetting. A
separate GPT-6 Astra xhigh assessment and an exact-file addendum accompany the revised
manuscript. They are AI assessments from the same provider, not human peer review or an
external publication decision. The present revision adds bibliographic attributions without
changing the mathematical statements or proofs.
References
[1] K. Nakahira and K. Kato, Generalized quantum process discrimination problems,Phys. Rev. A
103, 062606 (2021); erratum104, 069902 (2021). arXiv:2104.09759.
[2] G. Chiribella and D. Ebler, Quantum speedup in the identification of cause–effect relations,Nature
Communications10, 1472 (2019). doi:10.1038/s41467-019-09383-8; arXiv:1806.06459.
[3] M. Sedlák and M. Ziman, Unambiguous comparison of unitary channels,Phys. Rev. A79, 012303
(2009). arXiv:0809.4401.
[4] M. Hayashi, Indefinite causal order strategy does not improve the estimation of group action,
Quantum9, 1891 (2025). arXiv:2501.09312.
[5] Y.-A. Chen, C. Zhu, K. He, Y. Liu and X. Wang, Hypothesis testing of symmetry in quantum
dynamics (2024). arXiv:2411.14292.
[6] M. Hayashi, Y.-A. Chen, C. Zhu and X. Wang, Predicting symmetries of quantum dynamics with
optimal samples (2025). arXiv:2502.01464.
[7] K. Chen, Q. Wang, P. Long and M. Ying, Unitarity estimation for quantum channels,IEEE Trans.
Inf. Theory69, 5116–5134 (2023). arXiv:2212.09319.
[8] H. Ghosh, A. Jackson and A. Datta, Unitary channel testing under a depolarizing noise assumption
(2026). arXiv:2606.10730.
[9] Y. Hashimoto, A. Soeda and M. Murao, Comparison of unknown unitary channels with multiple
queries (2022; revised 2026). arXiv:2208.12519.
[10] P. Ghosal, P. Halder, A. Patra and A. Sen(De), Quantum hypothesis testing of non-mixed-unitarity:
A multifaceted hierarchy of quantum channel discrimination (2026). arXiv:2609.40355.
[11] Y. Cao, R. Chen, C. Zhu and X. Wang, Resource compatibility in optimal quantum symmetry
testing (2026). arXiv:2609.38134.
11

[12] L. Eriksson, Algebraic query support for unitary oracles: Exact Hilbert laws, harmonic spectra,
and general-tester bounds (2026). AIRR ARR-2026-6WX2JF38WE87GB2M, v1.
[13] L. Eriksson, Phase calibration unlocks adaptive tests for renewed quantum noise (2026). AIRR
ARR-2026-33GYTDAT5C8THB3M, v1.
[14] I. G. Macdonald,Symmetric Functions and Hall Polynomials, second edition, Oxford University
Press (1995). doi:10.1093/oso/9780198534891.001.0001.
12