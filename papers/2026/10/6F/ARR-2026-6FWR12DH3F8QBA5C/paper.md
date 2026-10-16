# Sharp determinant bounds for amplified antisymmetric channels and a noise law for noncommutative rank

Text extraction of canonical paper.pdf; consult PDF for equations.

Sharp determinant bounds for amplified antisymmetric channels
and a noise law for noncommutative rank
Lluis Eriksson
16 October 2026
Abstract
We study the largest normalized determinant in a Kraus matrix space after amplification
by a completely depolarizing channel. For the three-dimensional antisymmetric channel,
we prove a bound uniform in the auxiliary dimension, identify its exact value22/9/4,
and show that a finite amplification attains it if and only if its dimension is divisible
by three. The proof balances a determinant maximizer, fixes its second and fourth
singular-value moments, and uses a quadratic majorant of the logarithm. Combined
with known unitary constructions, this determines the regularized value for every Holevo–
Werner channel: dimension three is the unique exceptional case. We also prove that
adding depolarizing noise of strengthε produces a power law whose exponent is the
normalized noncommutative-rank defect of the original Kraus space. The latter estimate
is uniform over all auxiliary dimensions and has a matching lower bound at one fixed finite
dimension. These results sharpen finite-dimensional examples and an exact-rank criterion
into, respectively, an infinite-amplification optimum and a quantitative noise law. We state
the operational interpretation for tests of an unknown global unitary separately from free
ancillary assistance.
1 Introduction and scope
A matrix space can contain only singular matrices and yet acquire an invertible element
after its scalar coefficients are replaced by matrices. This distinction between ordinary and
noncommutative rank is classical [2, 3, 4]. For quantum channels it has a direct manifestation:
a test that can reject every unknown unitary perfectly can lose that property when the
alternative channel is tensored with another noisy channel and the null is enlarged to all
unitaries on the joint system [1]. Rank decides whether the obstruction vanishes. It does not
quantify the determinant remaining after it vanishes, or the effect of a small full-rank noise
component.
The present paper addresses these two quantitative questions. Our first result solves an
optimization overallmatrix amplification sizes for the three-dimensional Holevo–Werner
channel. A fixed3 ×3auxiliary system attains the regularized optimum; equality is impossible
at dimensions not divisible by three. Thus a small witness is certified globally optimal, rather
than merely being the best example among a finite list. The exact constant is strictly below
the elementary Choi spectral ceiling.
Our second result applies to every finite-dimensional channel. The order of vanishing under
depolarizing noise is the noncommutative-rank defect divided by the input dimension. Its
proof gives an upper bound independent of auxiliary dimension and a constructive lower bound
from a single rank witness. In particular, the result controls a regularization taken before the
small-noise limit.
The surrounding ingredients are not new. Matrix-space blow-ups and shrunk subspaces
come from noncommutative-rank theory [2, 3]; determinant maximization is closely related
1

to operator scaling [5]; the exceptional factorizability and fourth-moment geometry of the
three-dimensional Holevo–Werner channel are known [6]; and determinants already occur
in entanglement measures [7]. Valuations of noncommutative determinants also have an
established theory [9]. We do not claim a new rank algorithm, a resolution of a random-
matrix determinant conjecture, or a classification of all channel factorizations. The proposed
contributions are the sharp amplified determinant bound with its attainment criterion, and
the uniform noise exponent for this determinant functional. Our search for earlier versions of
these statements was bounded; it is not a certificate of priority.
2 The amplified determinant functional
All vector spaces are complex. Writeτm = Tr/m, and letE: Md(C) →Md(C)be completely
positive and trace preserving, with Kraus operatorsK1,...,K k:
E(X) =
k∑
j=1
KjXK†
j,
∑
j
K†
jKj =Id.
The Kraus space isSE= span{Kj}. Define
δ(E) = max∑
j |zj|2=1
⏐⏐⏐⏐⏐⏐
det
(∑
j
zjKj
)
⏐⏐⏐⏐⏐⏐
2/d
.(1)
Isometric changes of Kraus representation leave this quantity invariant. Equivalently, if
JE= ∑
j |Kj⟩⟩⟨⟨Kj|is the unnormalized Choi matrix,
δ(E) = max
|B⟩⟩⟨⟨B|⪯JE
|detB|2/d.
Using a closed unit ball instead of a sphere makes the equality immediate also for a redundant
representation or a singular matrix space.
LetDm(X) = Tr(X)Im/m. Our amplified quantity is
am(E) =m 2δ(E⊗D m) = max∑
j τm(Y†
j Yj)=1
|detH(Y)|2/(dm) , H(Y) =
∑
j
Kj ⊗Yj.(2)
Indeed the Kraus operators ofDm are Eab/√m. If Zj = (zjab), then∑
j ∥Zj∥2
F = 1; putting
Yj = √mZj gives the second expression, including the factorm2. Set
A∞(E) = sup
m≥1
am(E).
The maxima at fixed m exist by compactness. The factor m2 removes the elementary
normalization cost of the depolarizing partner;A∞is not a communication capacity.
Lemma 1(Spectral ceiling and direct sums).For everym,
0≤a m(E)≤ λmax(JE)
d ≤1.
Moreover,
am+n(E)≥a m(E)m/(m+n)an(E)n/(m+n), a ℓm(E)≥a m(E).
2

Proof.The Hilbert–Schmidt Gram matrix of theKj has the nonzero spectrum ofJE. Conse-
quently
TrH†H
dm ≤λmax(JE)
d
∑
j
τm(Y†
j Yj).
Apply the arithmetic–geometric mean inequality to the eigenvalues ofH†H, and useTrJE= d.
For direct sums putYj = Y(m)
j ⊕Y(n)
j . The normalized energy remains one and the determinant
factors.
Lemma 2(Balancing at a nonsingular maximum).Ifam(E)>0, every maximizing tuple in
(2)satisfies ∑
j
Y†
j Yj =Im,
∑
j
YjY†
j =Im.(3)
Proof. Let T = T† be traceless and replaceYj by YjetT. The unnormalized determinant is
unchanged because H is multiplied byId ⊗etT, whose determinant is one. Writee(t) =∑
j τm(etTY†
j YjetT). After normalization the objective is am(E)/e(t). Maximality implies
e′(0) = 0, hence Tr(T∑
j Y†
j Yj) = 0for every such T. The sum is scalar and its trace ism,
proving the first identity. The variationsetTYj prove the second.
This is a stationary-point argument on a compact sphere, not an assumption that an
arbitrary tuple has already been scaled. A maximum with zero determinant requires no
balancing argument.
3 The unique antisymmetric exception
Ford≥2, consider the Holevo–Werner channel
Wd(X) = Tr(X)Id −XT
d−1 .
Its Kraus operators are(Eij −Eji)/
√
d−1,i<j, and
JWd = 2
d−1 P−, a m(Wd)≤L d := 2
d(d−1) .
Ford= 3use real skew matrices(A i)ab =ϵiab andK i =Ai/
√
2. Put
B∗= 22/9
4 = 0.291632....
Theorem 3(Sharp bound in dimension three).For every positive integerm,
am(W3)≤B ∗.
Equality holds if and only if3|m. In particular
A∞(W3) =B∗< 1
3,min{m:a m(W3) =A∞(W3)}= 3.
At any maximizing tuple attainingB∗, the spectrum ofH†H consists of1with multiplicity
m/3and1/4with multiplicity8m/3.
3

3.1 Two moments and a norm bound
Lemma 4.For a balanced tripleY1,Y2,Y3 andH= ∑
iKi ⊗Yi,
0⪯H †H⪯I 3m, τ 3m(H†H) = 1
3, τ 3m((H†H)2) = 1
6.
Proof. The row operator with entriesKi⊗Im has norm one since∑
iKiK†
i = I3. The column
operator with entriesI3 ⊗Yi also has norm one. Their product isH, so∥H∥≤ 1. The skew
matrices obey
Tr(K†
iKj) =δij,(4)
Tr(K†
iKjK†
kKl) = δijδkl +δilδjk
4 .(5)
The first identity givesTrH†H=m. The second gives
Tr((H†H)2) = 1
4 Tr
(∑
i
Y†
i Yi
)2
+ 1
4 Tr
(∑
i
YiY†
i
)2
= m
2 .
Lemma 5(Logarithmic moment bound).If a positive definite matrixX satisfies X⪯ 3I,
τ(X) = 1, andτ(X 2) = 3/2, then
τ(logX)≤log(3/4) + log 4
9 .
Equality holds exactly when the spectrum is contained in{3/4,3}.
Proof.Letu= 3/4and
q(x) = logu+ x−u
u + log 4−3
(3−u) 2 (x−u) 2.
This polynomial agrees withlogx and its first derivative atu, and agrees withlogx at3. The
Hermite interpolation remainder has sign
logx−q(x) = (log)′′′(ξ)
3! (x−u) 2(x−3)≤0 (0<x≤3)
for an intermediate positiveξ; equality occurs only atu and3. The same sign follows directly
by differentiatingq−log. Sinceτ((X−uI) 2) = 3/2−2u+u 2 = 9/16,
τ(q(X)) = log(3/4) + 1
3 + log 4−3
9 = log(3/4) + log 4
9 .
Functional calculus completes the proof.
3.2 Proof of the sharp theorem
If the maximum determinant is zero, the upper bound is immediate. Otherwise apply Lemma 2
to a maximizing tuple and putX= 3H†H. Lemmas 4 and 5 imply
logam(W3) =τ3mlog(H†H)≤−log 3 + log(3/4) + log 4
9 = logB∗.
For equality the eigenvalues ofH†H are1 /4and1. If the multiplicity of1is r, the first
moment givesr+ (3m−r)/4 =m, hencer=m/3. Thus3|m.
4

For sufficiency takem= 3andY i =Ki. The tuple is balanced and
H= 1
2
∑
i
Ai ⊗Ai = |Ω⟩⟨Ω|−F
2 ,|Ω⟩=
3∑
a=1
|aa⟩,
where F swaps the two factors. Its eigenvalues are1onΩ, −1/2on the five-dimensional
symmetric orthogonal complement, and1/2on the three-dimensional antisymmetric subspace.
Therefore detH = −1/256and |detH|2/9 = B∗. Direct sums give every multiple of three.
This also proves the spectral assertion.
Corollary 6(Finite-size approach).Letb 2 = 1/(3 21/3). Form≥2, choose
rm =



0, m≡0 (mod 3),
2, m≡2 (mod 3),
4, m≡1 (mod 3).
Then
B∗
(b2
B∗
)rm/m
≤am(W3)≤B ∗,0≤log B∗
am(W3) ≤ 4
mlog B∗
b2
.
Thuslim m→∞am(W3) =B∗.
Proof. The balanced tripleYi = σi/
√
3, with the three Pauli matrices, yields squared singular
values2 /3,2/3,1/6,1/6,1/6,1/6and objective b2. Combine blocks of size three and two using
Lemma 1. The displayed choices use zero, one or two blocks of size two. The bound is valid
also atm= 2,4. No monotonicity in every consecutive dimension is asserted.
Theorem 7(All antisymmetric dimensions).Ford≥2,
A∞(Wd) =
{
22/9/4, d= 3,
2/[d(d−1)], d̸= 3.
For evendthe second value is attained atm= 1. For oddd≥5it is attained atm= 4.
Proof. The cased= 3is Theorem 3. For evend, the skew space contains the unitary direct
sum of
(0 1
−1 0
)
, so the Choi spectral ceiling is attained.
For oddd≥ 5, Haagerup–Musat [6, Lemma 5.1 and Theorem 5.2(1), equations (5.17)–
(5.19)] construct a unitary in the dimension-five skew space tensored withM4. Add blocks(0 1
−1 0
)
⊗I4 to reach every oddd≥ 5. If U = ∑
i<j(Eij −Eji) ⊗Zij is such a unitary, then
∑
i<j τm(Z†
ijZij) = d/2. Taking Yij =
√
2/dZij in (2) gives H =
√
2/[d(d−1)]U , attaining
the ceiling.
The non-exceptional construction in this theorem is an application of known factorizations,
not a new factorization theorem. The new sharp calculation concerns dimension three.
Haagerup–Musat’s obstruction to factorization and their trace-norm bounds concern different
functionals; non-factorizability alone does not determine the determinant value above.
4 Depolarizingnoisemeasuresthenoncommutative-rankdefect
For a matrix spaceS⊆M d, put
ρm(S) = max{rankA:A∈S⊗M m}, r(S) = ncrk(S) = sup
m≥1
ρm(S)
m .
5

OverC, noncommutative-rank theory identifiesr(S)with the integer
d−max
U⊆Cd
(
dimU−dimS(U)
)
, S(U) = span{Au:A∈S, u∈U},
and guarantees attainment at a finite matrix size [2, 3]. In particularρm(S) ≤mr(S)for every
m. No dimension bound for the smallest rank witness is needed below.
For0<ε<1, set
Eε = (1−ε)E+εD d, θ= d−r(S E)
d , θ m = 1− ρm(SE)
dm .
Since a channel has a nonzero Kraus operator,0≤θ≤θm <1.
Theorem 8(Uniform noise law).There are positive constantscE,Cd,θ, independent ofε, such
that for0<ε≤1/2,
cEεθ ≤A∞(Eε)≤C d,θεθ.(6)
The lower bound is attained as a lower estimate at one fixed finite amplification size. Conse-
quently
lim
ε↓0
logA∞(Eε)
logε =θ.
At every fixedm there likewise are positive constants, depending onE,m, with am(Eε) =
ΘE,m(εθm ).
4.1 Upper bound uniform in the amplification
Use the Kraus representation{√1−εK j,
√
ε/dEab}. Every feasible amplified matrix can be
written
H=
√
1−εA+ √εB, A=
∑
j
Kj ⊗Yj, B= 1√
d
∑
a,b
Eab ⊗Zab,
where ∑
j
τm(Y†
j Yj) +
∑
a,b
τm(Z†
abZab) = 1.
In particular
rankA≤mr(S E) = (1−θ)dm, ∥B∥2
F
dm ≤ 1
d2 .
The first inequality simply statesrankA≤mr (SE). Let N = dm, q = (1 −θ)N, and order
the singular values ofHdecreasingly. The best low-rank approximation inequality gives
∑
ℓ>q
sℓ(H)2 ≤ε∥B∥2
F ≤εN
d2 .
Also ∥H∥2
F/N≤ 1by the argument of Lemma 1, applied to the channelEε. For0 <θ <1,
applying arithmetic–geometric mean separately to the firstq and lastN−q squared singular
values yields
|detH|2/N ≤
( 1
1−θ
)1−θ( ε
d2θ
)θ
.(7)
This proves the uniform upper bound. Forθ= 0, useam ≤1. Replacing q by ρm(SE)gives
the fixed-size upper bound withθm.
6

4.2 A finite witness for the lower bound
Choose m0 and a feasible tuple producingA∈S E⊗Mm0 of rankq= r(SE)m0. WriteN = dm0,
p = q/N = 1 −θ, and lets1,...,s q > 0be the nonzero singular values ofA. Assume first
θ >0. In an SVD ofA, letV0 be the partial isometry carrying its right kernel onto its left
kernel, and put
B= V0
d
√
θ
.
This matrix has a depolarizing-noise representation with normalized coefficient energy one: if
B= (B ab)d
a,b=1, takeZab =
√
dBab, giving
∑
a,b
τm0 (Z†
abZab) = d
m0
∥B∥2
F = 1.
Allocate coefficient energyptoAandθtoB. The feasible matrix
Hε =
√
(1−ε)pA+
√
εθB
is block diagonal in the left and right SVD bases. Its determinant therefore satisfies
|detH ε|2/N = [(1−ε)p] p
( q∏
ℓ=1
s2
ℓ
)1/N(ε
d2
)θ
.(8)
The prefactor is bounded below by a positive constant for0<ε≤ 1/2. Forθ= 0, the witnessA
is invertible and using only the original Kraus coefficients givesam0 (Eε) ≥(1−ε)|detA|2/N >0.
The same construction at any fixedm, using a matrix of rankρm(SE), proves the fixed-size
lower bound. Taking logarithms in the two-sided estimates proves the theorem.
The uniform upper bound is essential: convergence at each fixed auxiliary dimension would
not by itself justify the statement about the supremum over all dimensions. No exchange of
an unproved random-matrix determinant limit is used.
4.3 Two different kinds of singularity
ForSW3 , ordinary rank is two but noncommutative rank is three. Hence
a1((W3)ε) = Θ(ε1/3), A ∞((W3)ε) = Θ(1).
Already at every fixedm≥ 2, the exponent is zero: the size-two and size-three witnesses and
their direct sums give full rank. This contrasts with a genuinely shrunk Kraus space, whose
positive exponent persists under arbitrary amplification.
For an exact example of the latter, letEρ(X) = Tr(X)ρ, withρ a density matrix. At every
m,
am(Eρ) = (detρ) 1/d
d .(9)
To see this, diagonalizeρand writeH = (√ρ⊗Im)Z, where∥Z∥2
F = m. Arithmetic–geometric
mean gives|detZ|2/(dm) ≤1/d, attained byZ = Idm/
√
d. For a pure replacer with depolarizing
noise,
am((Epure)ε) = 1
d
(
1−ε+ ε
d
)1/d(ε
d
)(d−1)/d
.
Its Kraus space has noncommutative rank one, so the exponent(d−1)/d agrees exactly with
Theorem 8.
7

5 Operational meaning and limitations
The determinant in(1) is the error exponent in the following composite testing problem [1].
The null is one unknown fixed unitary, used on every call. The alternative is an i.i.d. channel
with independent unknown fixed input and output changes of basis. Arbitrary ancillary
memory and adaptive testers are allowed; the optimal test can be parallel. Ifbn(E)is its
minimum type-II error at zero type-I error, then forδ(E)>0,
limn→∞−1
nlogbn(E) =−logδ(E).
This statement uses the precise null and orbit model in the cited theorem. It is not a claim
about every form of channel discrimination.
For the alternativeE⊗D m, the null in that theorem becomes all unknown unitaries on
Cdm. Thus
−logδ(E⊗D m) = 2 logm−loga m(E).
Theorem 3 computes the exact supremum of the normalized determinant over the auxiliary
dimension. Theorem 8 identifies the coefficient of log(1/ε)in its regularized, normalized
exponent:
−logA ∞(Eε) = d−ncrk(S E)
d log(1/ε) +OE(1).
The order of limits here is: obtain then-query exponent for each fixed channel and auxiliary
size, remove the explicit2logm term, take the supremum definingA∞, then letε decrease.
We make no uniform finite-nclaim whenmgrows withn.
The auxiliary depolarizing channel changes the physical alternative and enlarges the null.
It isnota free bypass ancilla for the same hypothesis test. The error-exponent interpretation
consequently does not assert that adding free memory worsens an otherwise fixed testing task.
6 Relation to earlier results and reproducibility
The companion manuscript [1] gives a universal optimal test, identifies its determinant exponent,
characterizes finite perfect detection by ordinary Kraus rank, and connects tensor stability
with noncommutative rank. It evaluates selected low-dimensional tensor examples. It does
not bound every auxiliary dimension in the three-dimensional antisymmetric case, prove the
divisibility criterion for equality, or establish the uniform depolarizing-noise law proved here.
Haagerup–Musat [6] establish the exceptional factorization behavior ofW3 and finite
factorizations for the other odd-dimensional Holevo–Werner channels. We use the latter
construction explicitly. Their Lemma 5.3 already exploits the fourth moment of skew block
matrices in a trace-norm argument. Our proof uses this same special moment geometry,
combined with determinant-maximizer balancing and a sharp logarithmic majorant; the fourth-
moment identity itself is not a new claim. The stationary balancing argument is consistent
with the established operator-scaling perspective [5]. For a general channel, balancing alone
does not fix this moment.
The general connection between rank defects and orders of determinant vanishing is also
established algebraic territory. Hirai–Iwamasa–Oki–Soma [9] study degrees of noncommutative
determinants and their optimization. Theorem 8 concerns a different quantitative assertion: a
two-sided estimate for the energy-normalized determinant maximum, with an upper constant
uniform over every matrix amplification and a fixed-size lower witness. We do not claim the
underlying rank–valuation principle as new.
Mai–Speicher [8] compute a Fuglede–Kadison determinant in terms of operator capacity.
Their finite random-matrix determinant convergence statement is a conjecture; the more recent
8

variational treatment [10] also distinguishes free determinants from finite-matrix determinant
convergence. Neither convergence statement is assumed in our proofs. This distinction
ruled out a tempting but unjustified route to a general constant-factor approximation during
development.
The accompanying verification files check the finite trace identities symbolically, the
two explicit saturation witnesses, scalar majorant values, direct-sum constructions, and
the rank/noise estimates on reproducible finite examples. Such calculations are checks on
normalization and implementation, not replacements for the all-dimension proofs. Numerical
searches used to discover the dimension-three optimum establish no global upper bound; the
proof above does.
This manuscript was developed with OpenAI models, including GPT-6 Astra in a separate
development context. Its final review, if supplied, must identify the exact PDF and disclose
model involvement and context reuse. No human peer review, formal proof-assistant certi-
fication, model score, or journal acceptance is claimed by this document. The author also
operates AIRR; publication as a Working paper must retain that conflict disclosure. Opus did
not contribute a completed review to this draft.
References
[1] L. Eriksson,Universal optimal tests of unknown unitary dynamics: determinant exponents
and tensor stability, AIRR Working paper, ARR-2026-2GTKNVK5QM9H8BFR, v1 (2026).
https://airr.science/papers/ARR-2026-2GTKNVK5QM9H8BFR/versions/v1/.
[2] H. Derksen and V. Makam,Polynomial degree bounds for matrix semi-invariants, Advances
in Mathematics310(2017), 44–63.https://arxiv.org/abs/1512.03393.
[3] G. Ivanyos, Y. Qiao and K. V. Subrahmanyam,Constructive non-commutative rank
computation is in deterministic polynomial time, Computational Complexity27(2018),
561–593.https://arxiv.org/abs/1512.03531.
[4] Y. Li, Y. Qiao, X. Wang and R. Duan,Tripartite-to-bipartite entanglement transformation
by stochastic local operations and classical communication and the structure of matrix
spaces,https://arxiv.org/abs/1612.06491.
[5] A. Garg, L. Gurvits, R. Oliveira and A. Wigderson,Operator scaling: theory and applica-
tions,https://arxiv.org/abs/1511.03730.
[6] U. Haagerup and M. Musat,An asymptotic property of factorizable completely positive
maps and the Connes embedding problem, Communications in Mathematical Physics338
(2015), 721–752.https://arxiv.org/abs/1408.6476.
[7] G. Gour,Family of concurrence monotones and its applications, Physical Review A71
(2005), 012318.https://arxiv.org/abs/quant-ph/0410148.
[8] T. Mai and R. Speicher,Fuglede–Kadison determinants of matrix-valued semicircular
elements and capacity estimates,https://arxiv.org/abs/2406.15922.
[9] H. Hirai, Y. Iwamasa, T. Oki and T. Soma,Algebraic combinatorial optimization on the
degree of determinants of noncommutative symbolic matrices,https://arxiv.org/abs/
2310.15502.
[10] V. Kargin,Fuglede–Kadison Determinants of Shifted Matrix Semicircles,https://arxiv.
org/abs/2610.15180(2026).
9