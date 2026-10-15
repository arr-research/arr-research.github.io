# Phase calibration unlocks adaptive tests for renewed quantum noise

Text extraction of the canonical PDF. Consult paper.pdf for mathematical typography.

Phase calibration unlocks adaptive tests
for renewed quantum noise
Lluis Eriksson
Independent researcher
15 October 2026
Working manuscript
Abstract
Can interventions distinguish an unknown phase that is frozen throughout an experiment
from phase noise renewed at every use? We study ordinary forward queries, arbitrary
quantum memory, and exactly zero false positives for every frozen diagonal unitary. For
any Schur channel with correlation matrix C, the optimal parallel failure probability is
min|m|=n per(C[m])/n!, where C[m] repeats rows and columns according to the occupation
vector m. The same formula is the exact optimum over all causal strategies when the
renewed channel has an unknown common phase carrier and failure is evaluated in the
worst case over that carrier. Calibration changes this conclusion: for qubit dephasing we
give a rational ﬁve-query certiﬁcate that beats every parallel strategy for 0.5331424052 ...<
η <1. At η = 0 .7, failure decreases from 0.46603 to 0.4602957928558. We prove physical
realizability of the certiﬁcate, obtain exact causal limits at complete dephasing, and show
that adaptation cannot improve the asymptotic failure exponent. The separation concerns
ﬁnite-query performance under a calibrated statistical promise; it neither quantiﬁes the
hardware cost of a phase reference nor certiﬁes a quantum environment.
1 Question, contribution, and scope
A random phase can be sampled once and retained, or sampled anew at each interaction. These
mechanisms can have identical one-use channels and diﬀerent multi-time behavior. The oper-
ational role of interventions and multi-time descriptions is well established [ 10]. Our question
is more speciﬁc: how much can coherent control between uses improve unambiguous exclusion
of all frozen phases ?
There are two distinct promises for the renewed alternative. With a calibrated carrier,
its channel is known. With an uncalibrated carrier, the channel is known only up to a ﬁxed
diagonal unitary applied at every slot, and a test must perform well for every such carrier.
This distinction determines whether a ﬁnite-query adaptive advantage can occur. Theorem 4.1
rules out any advantage in the uncalibrated minimax problem, in every dimension and at every
query count. Theorem 7.1 supplies a calibrated counterpoint using commuting qubit noise.
Here and below, adaptive includes coherent intermediate controls and memory; it does not
require a recorded intermediate measurement.
The permanent itself is not new to unambiguous comparison: Cheﬂes, Andersson, and
Jex obtained per(Gram)/N! as a symmetric-projector failure probability [ 1, Eq. (4.10)]. Our
parallel theorem optimizes the input, including arbitrary ancillas, for a channel problem indexed
by occupation types. Its extension to all causal tests under a common unknown carrier is
the principal structural result. Likewise, causal Gram reconstruction is a specialization of
established query methods, notably Block Sets [ 2, Deﬁnition 2, Theorems 2–3], semideﬁnite
query characterizations [ 3], and quantum networks [ 4]. We provide the specialized construction
because a numerical matrix inequality alone would not prove a physical adaptive separation.
1

Earlier unitary-comparison work [ 5, 6, 7] provides direct context, but uses diﬀerent al-
ternatives or access models. In particular, the updated multi-query comparison theorem of
Hashimoto, Soeda, and Murao [ 7] establishes parallel optimality for comparison of two Haar-
unitary blocks, including general testers. Exact adaptive sensing limits for bosonic dephasing
[8] and adaptive discrimination of speciﬁed channels [ 9] also predate this work. We claim
neither a general invention of adaptive discrimination nor the ﬁrst exact dephasing limit.
The author’s earlier work concerns sampling static disorder without interventions within
one realization [ 12], polynomial query support [ 13], and an exact two-query adaptive separation
for tetrahedral echoes [ 14]. The present contribution is the all- d,n,C calibration dichotomy
together with its certiﬁed qubit separation. Unlike the tetrahedral example, the calibrated
causal optimum here remains open.
2 Model and notation
Fix d ≥ 2 and n ≥ 1. A query acts on a d-dimensional register in a known basis. Under the
null, every slot applies the same unknown
Dθ = diag( eiθ0 ,...,e iθd−1 ), θ ∈ Td.
It may be sampled from any distribution once per run. The experiment outputs either rejec-
tion of the frozen-phase null or an inconclusive outcome. Its rejection probability must be
exactly zero for every θ. We call the inconclusive probability under the alternative the failure
probability β. This is a one-sided test; it does not unambiguously certify the null.
The calibrated alternative consists of independent uses of the Schur channel
EC(|a⟩⟨b|) = Cab|a⟩⟨b|, C ⪰ 0, C aa = 1 . (1)
A dilation sends |a⟩to |a⟩|ea⟩, with ⟨eb,ea⟩= Cab, using a fresh environment at each slot. For
a classical random-phase interpretation one additionally needs
C ∈ conv{zz† : |za|= 1 }.
This extra condition holds for the qubit channels below, but does not follow from positive
semideﬁniteness and unit diagonal in general dimension d ≥ 4 [11]. Our general theorems
concern Schur channels; their classical phase-renewal interpretation has this restriction.
Allowed tests use ordinary forward queries, ﬁnite ancillary systems, ideal controls, and a
ﬁnal two-outcome measurement. Intermediate instruments and randomness may be puriﬁed
and stored in memory. We do not allow inverse queries, controlled bypass of the queried
device, environment access, or indeﬁnite causal order. A parallel test prepares all n inputs
jointly, queries them without intervening controls, and measures jointly. Write βpar(n,C) and
βcausal(n,C) for the inﬁma over parallel and all causal tests respectively.
A word x= ( x1,...,x n) ∈ {0,...,d − 1}n has occupation m(x) = ( m0,...,m d− 1). Let
Ωm = {x: m(x) = m}, N m = |Ωm|= n!∏
a ma!, |m|= n.
For a representative word x∈ Ωm, let C[m] be the n× nmatrix with entries Cxixj ; its permanent
is independent of the representative. Set
Fm(C) = per(C[m])
n! . (2)
2

3 The exact parallel optimum
Theorem 3.1 (Optimized permanent law) . For every correlation matrix C, every d, and
n≥ 1,
βpar(n,C) = min
|m|=n
Fm(C). (3)
An optimum uses no ancilla: prepare |Dm⟩= N− 1/2
m
∑
x∈ Ωm |x⟩for a minimizing type, and use
the inconclusive eﬀect |Dm⟩⟨Dm|.
Proof. Purify an arbitrary parallel probe and write it as |ψ⟩= ∑
x |x⟩|ax⟩, with px = ∥|ax⟩∥2
and ∑
x px = 1 . Its null output is
∑
m
eim·θ|ψm⟩, |ψm⟩=
∑
x∈ Ωm
|x⟩|ax⟩.
Distinct characters are linearly independent, and the nonzero ψm are orthogonal. Thus the null
span is their direct sum. If A is the inconclusive eﬀect, zero rejection forces it to be identity
on that span; since 0 ⪯ A⪯ I, it dominates the corresponding orthogonal projector.
Put K = C⊗ n and pm = ∑
x∈ Ωm px. The resulting lower bound on failure is
∑
m:pm>0
1
pm
∑
x,y∈ Ωm
pxpyKxy. (4)
This expression retains arbitrary ancillas: the orthogonal word registers make the two inner
products in each projector expectation equal to px and py. Each principal block Km = K|Ωm
is positive semideﬁnite. Consequently q ↦→q†Kmq is convex on the real probability simplex.
Slot permutations preserve Km and act transitively on Ωm; averaging qx = px/pm over those
permutations gives the uniform distribution without increasing the energy.
The uniform energy is the constant row sum of Km divided by Nm. In the permanent of
C[m], each distinct word of type m occurs ∏
a ma! times. Hence this energy is
per(C[m])
Nm
∏
a ma! = Fm(C).
Equation ( 4) is bounded below by ∑
m pmFm(C), and thus by the smallest Fm(C). The stated
uniform-type probe and projector attain equality.
Remark 3.2. The argument includes complex and singular C. It does not assume entrywise
nonnegativity. Its permanent is the familiar Gram-permanent quantity from state comparison
[1]; the additional statement is global optimization over channel probes and ancillas.
4 Unknown carrier: a minimax theorem for all causal tests
Suppose the alternative is known only up to a ﬁxed common carrier ϕ∈ Td:
C(ϕ) = DϕCD†
ϕ, EC(ϕ) = Uϕ ◦ EC, Uϕ(X) = DϕXD†
ϕ.
Conditional on ϕ, the n uses are independent. The carrier is ﬁxed throughout the run, rather
than drawn anew at every slot. Deﬁne
βwc
causal(n,C) = inf
T : zero null error
sup
ϕ∈ Td
βT (C(ϕ)).
The inﬁmum includes strategies that attempt to learn ϕ within their n queries.
3

Theorem 4.1 (Calibration-free minimax equality) . For every d,n,C as above,
βwc
causal(n,C) = βpar(n,C) = min
|m|=n
Fm(C). (5)
Thus a uniform-type parallel test is minimax optimal among all causal tests.
Proof. A puriﬁed causal circuit has a phase-history expansion
|Ψ(z1,...,z n)⟩=
∑
x


n∏
j=1
zj,xj

|vx⟩, |zj,a|= 1 . (6)
Let um = ∑
x∈ Ωm vx. Under the frozen null the output is ∑
m eim·θum, of norm one for every θ.
Haar integration and Parseval give ∑
m
∥um∥2 = 1 . (7)
The vectors um need not be orthogonal.
Let A be the inconclusive eﬀect. Zero rejection gives AΨθ = Ψ θ. Fourier extraction then
implies
√
Aum = um. Write ax =
√
Avx, so that ∑
x∈ Ωm ax = um. The alternative output, by
the fresh-environment dilation of ( 1), has acceptance probability
∑
x,y
Kxyei(m(x)− m(y))·ϕ⟨ay,ax⟩.
Averaging ϕ deletes only cross-type terms. On one type block, slot-permutation invariance
implies Km1 = NmFm(C)1. Decompose
ax = um
Nm
+ bx,
∑
x∈ Ωm
bx = 0 .
The mixed terms vanish by the constant row sum, and positivity of Km gives
∑
x,y∈ Ωm
Kxy⟨ay,ax⟩= Fm(C)∥um∥2 +
∑
x,y∈ Ωm
Kxy⟨by,bx⟩ ≥ Fm(C)∥um∥2. (8)
For complex C, the last energy is nonnegative because it is the contraction of two positive
Gram matrices (equivalently, a sum of squared tensor-product norms). Sum ( 8) and apply
(7). The mean failure over ϕ, hence its supremum, is at least minm Fm(C). No interchange of
inﬁmum and supremum is required. The uniform-type test in Theorem 3.1 has the same failure
for every carrier, since m(x) = m(y) throughout its support. It attains the lower bound.
Corollary 4.2 (Complete dephasing) . For C = Id, even with a calibrated carrier,
βcausal(n,Id) = βpar(n,Id) = 1
max|m|=n
( n
m0,...,md−1
). (9)
The maximum occurs when occupations diﬀer by at most one.
Proof. The channel is invariant under carrier shifts, so its minimax and calibrated problems
coincide. Here Km is identity and Fm = 1 /Nm. If ma ≥ mb + 2, moving one count from ato b
decreases ∏
a ma!; iterating proves the balancing assertion.
4

5 Qubit formulas and the asymptotic limit
For qubits take a known zero carrier and
Cη =
(
1 η
η 1
)
, 0 ≤ η≤ 1, Eη = pId + qZ, p = 1 + η
2 , q = 1 − η
2 , (10)
where Z(X) = ZXZ and Z = diag(1 ,−1). For a known nonzero carrier, a compensating
control gives this model while preserving the composite frozen null.
Proposition 5.1 (Balanced qubit formula) . With w= ⌊n/2⌋,
βpar(n,η) =
w∑
j=0
(
w
j
)(
n− w
j
)
η2j
(n
w
) . (11)
Proof. In a weight- w block, a ﬁxed binary word has
(w
j
)(n− w
j
)
words at Hamming distance 2j,
giving the displayed value for that weight. Let Jw have probabilities πw(j) =
(w
j
)(n− w
j
)
/
(n
w
)
.
For w< (n− 1)/2, the likelihood ratio on the common support is
πw+1(j)
πw(j) = (w+ 1)2(n− w− j)
(n− w)2(w+ 1 − j),
which increases with j; any new support lies at the upper end. Thus Jw+1 stochastically
dominates Jw. Since η2j decreases in j, the block value decreases toward the balanced weight.
Symmetry handles the other half. At η = 0 the value is 1/
(n
w
)
, and at η = 1 all values are
one.
Proposition 5.2 (No improvement of the failure exponent) . For n≥ 1 and 0 ≤ η≤ 1,
pn + qn ≤ βcausal(n,η) ≤ βpar(n,η) ≤ (n+ 1)pn. (12)
Consequently, for ﬁxed 0 ≤ η <1, both optimal failure exponents are − log((1 + η)/2).
Proof. The Kraus trajectories consisting entirely of I, or entirely of Z, have probabilities pn
and qn. Each is a frozen null and must be inconclusive with certainty, for any causal protocol.
This proves the lower bound. In ( 11), the numerator is at most (1 + η)n: it is a sub-sum of
the product (1 + η)w(1 + η)n− w with nonnegative terms. Also
( n
⌊n/2⌋
)
≥ 2n/(n+ 1) . Taking
logarithms and dividing by n proves the limit.
6 Causal certiﬁcates and physical realization
For completeness we specialize known query-decomposition methods [ 2, 3, 4] to the present
continuous-phase setting. Index level k by words of length k, with the last symbol appended
on the right. Let V be the dn ×
(n+d− 1
d− 1
)
matrix whose columns are the type indicators 1Ωm.
Lemma 6.1(Causal Gram realization) . The following conditions characterize causal rejection
statistics:
Q0 = [1] , Q k ⪰ 0, (13)
(Qk)xa,yb = 0 ( a̸= b),
∑
a
(Qk)xa,ya = ( Qk− 1)x,y, (14)
0 ⪯ R⪯ Qn, RV = 0 . (15)
5

The rejection probability under E⊗ n
C is
s(C) = Tr( C⊗ nR). (16)
Every feasible collection has a realization using a d-dimensional query register and memory of
dimension at most dn− 1.
Proof. Expand the puriﬁed output immediately after each query into its phase histories, with
coeﬃcient vectors v(k)
x , and set (Qk)x,y = ⟨v(k)
x ,v(k)
y ⟩. Projection onto the last queried symbol
makes distinct last-symbol branches orthogonal. Summing these projections preserves the pre-
vious inner products, proving ( 13)–(14). For a ﬁnal rejection eﬀect M, set Rx,y = ⟨v(n)
x ,Mv(n)
y ⟩.
Then 0 ⪯ R⪯ Qn. Fourier extraction of the null characters shows that zero rejection is equiva-
lent to annihilating all type sums; by positivity this is RV = 0 . The channel dilation contracts
two histories with (C⊗ n)xy, giving ( 16), including for complex C.
Conversely, factor the same-last-symbol blocks of Qk as B†
aBa. If previous coeﬃcient vectors
have Gram Qk− 1, deﬁne on their span
v(k− 1)
x ↦− →
∑
a
|a⟩ ⊗ Ba|x⟩.
The Gram recursion makes this map well deﬁned and isometric, including when the previous
vectors are linearly dependent. Extend the isometry to a unitary after completing the ambient
spaces. Applying the next diagonal query produces exactly the required next coeﬃcient vectors.
This constructs all levels.
If S has the terminal vectors as columns, S†S = Qn. The inequality 0 ⪯ R⪯ S†S ensures
that R annihilates ker S. The eﬀect M = ( S+)†RS+ on ran S, extended by zero, satisﬁes
0 ⪯ M ⪯ I and S†MS = R. Each same-symbol block has size at most dk− 1. Embedding all
levels in a space of dimension dn proves the stated suﬃcient memory bound.
This lemma is an exact physical characterization, not a relaxation based only on polynomial
normalization. It supplies a convenient specialization of the earlier reconstruction principles;
we do not claim their general equivalence as new. The suﬃcient memory bound also says
nothing about eﬃcient compilation into a restricted gate set.
7 A certiﬁed calibrated separation
At n= 5 , ( 11) becomes
βpar(5,η) = 1 + 6 η2 + 3η4
10 . (17)
The supplementary ﬁles phase-certificate-Q.json and phase-certificate-R.json specify
rational 32 × 32 matrices, in binary lexicographic order. They deﬁne a single ﬁxed strategy,
independent of η.
Theorem 7.1(Five-query calibrated advantage) . There is a causal ﬁve-query test with exactly
zero rejection of every frozen phase, whose rejection probability is
s∗(η) = 1086981
1250000 + 3225799
50000000η− 3784393
6250000η2
− 585391
25000000η3 − 103157
390625η4 − 2055017
50000000η5. (18)
It strictly improves on every parallel test for η∗ <η <1, where η∗ is the unique real root of
g(η) = 2055017 η3 − 1795904η2 + 3225799η− 1520760
and 0.53314 <η∗ <0.53315. At η= 7 /10, its failure and improvement are respectively
1 − s∗(7/10) = 2301478964279
5000000000000, β par(5,7/10) − (1 − s∗(7/10)) = 28671035721
5000000000000. (19)
6

Proof with a ﬁnite rational certiﬁcate. Reduce Q = Q5 recursively by (Qk− 1)xy = ( Qk)x0,y0 +
(Qk)x1,y1. The supplied entries satisfy all oﬀ-last-symbol zeros and Q0 = [1] . Exact rational
Schur-complement elimination establishes
Q≻ 0, Q − R≻ 0, R ⪰ 0, rank Q= rank( Q− R) = 32 , rank R= 26 .
The six type-indicator columns are annihilated exactly by R. Lemma 6.1 therefore supplies a
physical test with one query qubit and at most a 16-dimensional memory.
Summing Rxy over each Hamming distance gives the six coeﬃcients in ( 18). Subtracting
its failure from ( 17) gives the exact identity
βpar(5,η) − (1 − s∗(η)) = (1 − η2)g(η)
50000000 . (20)
The derivative of ghas positive leading coeﬃcient and negative discriminant −66647776694132,
so g increases on the real line. Exact substitution at 0.53314 and 0.53315 brackets its root.
Equations ( 20) and ( 19) follow.
The included veriﬁer replays all checks in exact rational arithmetic. No semideﬁnite op-
timizer is needed. Positive semideﬁniteness is checked by successive Schur complements: a
negative pivot fails, and a zero pivot is allowed only if its remaining row is identically zero.
This yields an exact ﬁnite-arithmetic proof for the supplied entries.
Test at η= 0 .7 Failure Detection
Optimal parallel 0.4660300000000 0 .5339700000000
Certiﬁed causal 0.4602957928558 0 .5397042071442
The improvement is about 0.5734 percentage points of detection. It is mathematically strict
but modest. The theorem does not identify the optimal causal test, prove that ﬁve queries are
necessary, or improve the exponent in Proposition 5.2. In particular, a ﬂoating-point optimizer
value is not an additional exact theorem. At η = 0 , the exact optimum is 1/
(5
2
)
= 0 .1 by
Corollary 4.2; the displayed certiﬁcate is not optimal there. At η = 1 , the alternative is itself
a frozen unitary.
8 Equal marginals and perturbations
Proposition 8.1 (Matched one-use channels) . For 0 ≤ η <1, requiring zero rejection against
every frozen qubit phase law with ﬁrst moment η is equivalent to requiring zero rejection for
each deterministic frozen phase.
Proof. Fix a point z on the unit circle. Choose 0 < ϵ ≤ (1 − η)/2. The residual mean
(η− ϵz)/(1 − ϵ) lies in the unit disk, because |η− ϵz| ≤ η+ ϵ≤ 1 − ϵ. It is a convex combination
of two circle points. Thus a phase law of mean ηcan assign positive mass ϵto any prescribed z.
Zero rejection averaged over every such law, together with nonnegativity, forces zero rejection
at that point. The converse is immediate.
In particular, sampling I or Z once with probabilities p,q and retaining it has the same
one-use channel as independently sampling them at every slot. The proposition concerns all
compatible frozen laws, rather than a known two-point null law alone. Rejection excludes the
speciﬁed frozen-phase null within the promise; it does not establish universal Markovianity, an
intrinsically quantum bath, or a unique physical noise mechanism.
7

Proposition 8.2 (Qubit null perturbations) . For any zero-null-error qubit test, suppose the
relative phase at slot j is θ+ δj, with |δj| ≤ π. Its false-positive probability is at most
min



1,

1
2
n∑
j=1
|δj|


2


. (21)
A common phase change across all slots remains an exact null.
Proof. After removing a global scalar, the operator-norm change of one qubit phase query is
2|sin(δj/4)| ≤ |δj|/2. Telescoping the puriﬁed isometric circuit bounds the ﬁnal vector change
by the sum. The square root of the rejection eﬀect annihilates the ideal null vector and is a
contraction. Squaring gives ( 21).
This is a bound on a ﬁxed test’s false positives. It does not prove superiority to the best
parallel test allowed a positive false-positive level. Translating time errors into δj requires
a frequency or phase-width bound. The result is not a claim of clock robustness without a
physical scale, and it does not include arbitrary state preparation, measurement, or memory
errors.
9 Reproducibility and remaining questions
The certiﬁcate matrices were obtained by numerical semideﬁnite search, interior mixing, ratio-
nal rounding, and exact constraint repair. The ﬁnal proof depends on the rational entries and
their veriﬁer, not on optimizer tolerances. The two matrix ﬁles have SHA-256 hashes
Q: 18ecfa37bc84e3b0ca40efdc9dbdda6b87442479d76a17f4f7ff04563f088463
R: 8a3bc80cdc93463652359b7145a095ac528c1469486173fb3f3cc3ad8e4000be
The standard-library veriﬁer checks causal constraints, positivity, null annihilation, coeﬃcient
aggregation, and the exact separation. A separate numerical reconstruction checks the circuit
against frozen phases, independent phase histories, and direct Kraus evolution; its largest
probability discrepancy was below 10− 14. These numerical checks are diagnostics, not proofs
of continuum claims.
A separate GPT-6 Astra review context checked the candidate proofs, reimplemented ra-
tional veriﬁcation, reconstructed the circuit, and tested the minimax argument. That review
shares the model provider and was coordinated with the authoring process; it is neither blind
review nor human peer review. Its report and scope are included with the supplement. AI
systems assisted literature triage, mathematical development, coding, drafting, and review. No
formal proof-assistant veriﬁcation is claimed.
The literature search renewed indexes from frontier-AI mathematics collections and the
author’s repositories, followed by targeted reading of the closest quantum-information sources.
Index coverage is not full-text mathematical veriﬁcation. The accompanying search audit
records that distinction; the absence of a located identical result is not a guarantee of priority.
Three questions remain especially concrete. First, what is the exact calibrated causal
optimum, and what is the smallest query count admitting a strict advantage? Second, can the
ﬁve-query certiﬁcate be replaced by a low-memory analytic circuit that explains the beneﬁcial
interference between occupation sectors? Third, does a useful advantage persist after jointly
optimizing both test classes at a positive false-positive allowance and with realistic control costs?
The present results settle the uncalibrated minimax problem and exhibit a ﬁnite calibrated
separation, while leaving these stronger claims open.
8

References
[1] A. Cheﬂes, E. Andersson, and I. Jex, Unambiguous comparison of the states of multiple
quantum systems , J. Phys. A 37, 7315 (2004). arXiv:quant-ph/0402125.
[2] S. A. Grillo and F. L. Marquezino, Quantum Query as a State Decomposition , Theoretical
Computer Science (2018), doi:10.1016/j.tcs.2018.03.017. arXiv:1602.07716v2.
[3] H. Barnum, Semideﬁnite programming characterization and spectral adversary method for
quantum complexity with noncommuting unitary queries (2007). arXiv:quant-ph/0703141.
[4] G. Chiribella, G. M. D’Ariano, and P. Perinotti, Theoretical framework for quantum net-
works, Phys. Rev. A 80, 022339 (2009). arXiv:0904.4483.
[5] E. Andersson, I. Jex, and S. M. Barnett, Comparison of unitary transforms , J. Phys. A
36 (2003), doi:10.1088/0305-4470/36/9/310. arXiv:quant-ph/0208153.
[6] M. Sedlák and M. Ziman, Unambiguous comparison of unitary channels , Phys. Rev. A 79,
012303 (2009). arXiv:0809.4401.
[7] Y. Hashimoto, A. Soeda, and M. Murao, Comparison of unknown unitary channels with
multiple queries , arXiv:2208.12519v2 (version of 7 September 2026).
[8] Z. Huang, L. Lami, and M. M. Wilde, Exact Quantum Sensing Limits for Bosonic De-
phasing Channels , PRX Quantum 5, 020354 (2024). arXiv:2402.05793.
[9] S. Sieniawski and R. Demkowicz-Dobrzański, Adaptive quantum channel discrimination
using methods of quantum metrology , New J. Phys. 28, 024502 (2026). arXiv:2510.15506.
[10] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, and K. Modi, Op-
erational Markov condition for quantum processes , Phys. Rev. Lett. 120, 040405 (2018).
arXiv:1801.09811.
[11] K. Dykema and K. Juschenko, Matrices of unitary moments (2009). arXiv:0901.0288.
[12] L. Eriksson, The arithmetic of sampling static quantum disorder: exact aliases, ﬁnite
witnesses, and clock robustness , working paper. AIRR ARR-2026-7PEKNEDVH38HV8PX,
v1 (2026) .
[13] L. Eriksson, Algebraic Query Support for Unitary Oracles: Exact Hilbert Laws,
Harmonic Spectra, and General-Tester Bounds , working paper. AIRR ARR-2026-
6WX2JF38WE87GB2M, v1 (2026) .
[14] L. Eriksson, Two-Query Chirality in Tetrahedral Quantum Echoes: Exact Parallel Readout,
a Nine-Dimensional Query Defect, and a Certiﬁed Adaptive Advantage , working paper.
AIRR ARR-2026-5KS70GV7KK9DYA69, v1 (2026) .
9