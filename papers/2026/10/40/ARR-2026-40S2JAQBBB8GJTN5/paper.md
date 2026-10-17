# Constant-precision undecidability for amplified determinants with capacity one

Extracted text; equations are authoritative in paper.pdf.

Constant-precision undecidability for ampliﬁed determinants
with capacity one
Lluis Eriksson
17 October 2026
Working paper
Abstract
We give a computable reduction from the halting problem to approximating a normal-
ized determinant optimized over matrix coeﬃcients of unrestricted auxiliary dimension.
The coeﬃcient matrices are real rational, orthonormal for normalized Hilbert–Schmidt in-
ner product, and have covariance-optimized operator capacity exactly one. Nevertheless,
approximating the determinant optimum to one ﬁxed additive precision is undecidable. The
proof combines the synchronous linear-game hardness theorem of Taller and Vidick with a
homogeneous multiplication block, weighted rational normalization, and two quantitative
rounding arguments. A positional-question normalization handles repeated queries without
identifying distinct answer positions. The constructed pencils have a linear scalar dimen-
sion in the expanded relation list and an explicit constant gap. It follows that even at one
ﬁxed precision no total recursive uniform bound on the required auxiliary dimension exists.
The hardness of the source games is an inherited theorem; the contribution is its transfer
to this constrained determinant objective. The gap constant is very small, and no practical
numerical hardness threshold or globally certiﬁed priority is claimed.
1 The objective and the result
For a tuple B = ( B1, . . . , Bs) in MD(C), deﬁne
Fm(B) = max∑s
ℓ=1 τm(Y ∗
ℓ Yℓ)=1
⏐⏐⏐⏐⏐det
( s∑
ℓ=1
Bℓ ⊗ Yℓ
) ⏐⏐⏐⏐⏐
2/(Dm)
, F∞(B) = sup
m≥1
Fm(B), (1)
where τd = Tr /d. Each ﬁxed- m feasible set is compact. The variables Yℓ are arbitrary complex
matrices: they are not required to be unitary, Hermitian, or mutually commuting.
For a completely positive map Φ : MD(C) → MD(C) let
cap(Φ) = inf
X>0, det X=1
det Φ(X).
For a density matrix Q ∈ Ms(C) put
ΦQ(X) =
∑
ℓ,h
QℓhBℓXB∗
h, C(B) = sup
Q⪰0, TrQ=1
cap(ΦQ)1/D.
We call C the covariance-optimized capacity. The normalization in the following theorem makes
it explicitly computable on every constructed instance.
1

Theorem 1. Set
γ = 1
36 288 000 000 .
There is a computable map from Turing machines T to ﬁnite real rational matrix tuples B(T)
such that
τD(B∗
ℓ Bh) = δℓh, C(B) = 1 , (2)
and
T halts =⇒ F ∞(B(T)) ≥ 1 − γ/4, (3)
T does not halt =⇒ F ∞(B(T)) ≤ 1 − γ. (4)
Thus approximating F∞ to additive error γ/8 is undecidable, even on the class (2).
The reduction is computable in the original machine description. It may explicitly expand
a succinct game into a much larger ﬁnite list; we do not claim polynomial running time in the
machine description. Once that list is given explicitly, the matrix construction has polynomial
size.
Corollary 2.For the same class there is no total recursive function of input length that bounds
a dimension m satisfying
Fm(B) ≥ F∞(B) − γ/8.
In particular, there is no total recursive uniform auxiliary-dimension bound for arbitrary re-
quested precision.
These are approximation statements, stronger than undecidability of exact equality with
an upper bound. A previous construction [ 6] transferred exact and asymptotic saturation
to balanced pencils, but its error bounds did not establish a ﬁxed approximation gap. Here
weighted singleton blocks and rational square normalization keep a constant fraction of the
dimension available to test relations. All proofs of this new transfer are included.
The general phenomenon of noncomputability in quantum correlations and tracial matrix
optimization is established. The source theorem is Taller–Vidick [ 1]; its foundations include
MIP∗ = RE [2]. Goldbring–Hart [ 3] already prove noncomputability of the universal theory
of the hyperﬁnite factor and the absence of computable general matrix-moment approxima-
tion bounds. Cleve–Culf–Taller [ 4] prove ﬁxed-precision hardness for tilted XOR games and a
constrained tracial Max-Cut problem. Our claim concerns the particular homogeneous deter-
minant objective ( 1), with only a quadratic normalization on its variables and with ( 2). It is
not a new general theorem about the noncomputability of tracial optimization.
2 A source game with unambiguous question positions
Throughout, a synchronous strategy means the convention used in [ 1, Sections 2.4 and 5.1]: a
common ﬁnite-dimensional space, a maximally entangled state, and projective measurements
paired with their transposes. For a constraint-variable game, this permits a joint measurement
for each constraint and a separate binary measurement for each variable. The two question
sets can be included in one disjoint union. We use synchronous value throughout this section;
no equality with unrestricted quantum value is assumed.
Theorem 5.2 and its proof in [ 1] provide, for any ﬁxed rational 0 < ε < 1/72, a computable
reduction with synchronous completeness 1 −ε and soundness 71/72. Its veriﬁer receives three
parity-constrained answer bits from Alice and one bit from Bob and compares Bob’s bit with
a speciﬁed Alice position. A folded query can coincide with another query. The following
normalization avoids silently treating three positions as three distinct variables.
2

Write π(x, y, i) for the rational joint probability of an Alice question x, a Bob question y,
and the answer position i ∈ {1, 2, 3} checked by the veriﬁer. If the position is a deterministic
function of (x, y), this notation simply has support on that function. Alice’s three answers
must have product σx ∈ {±1}. Let πX be the Alice marginal.
Lemma 3 (Positional normalization) . Such a game can be transformed computably into a
rationally weighted constraint-variable game with contexts of two or three distinct variables. If
the old game has a synchronous strategy of error e, the new one has a synchronous strategy of
error at most e/4. Every synchronous strategy of error e′ for the new game yields one of error
at most 18e′ for the old game. Dimensions are unchanged.
Proof. Introduce three distinct local variables ux,1, ux,2, ux,3 for every Alice question, and a
variable vy for every Bob question. These two families are disjoint. Give the parity row
ux,1ux,2ux,3 = σx
weight πX(x)/2. Give the equality row ux,ivy = 1 weight π(x, y, i)/2. Zero weights may be
omitted; duplicate rows may be combined. A row is sampled according to these weights, and
a variable uniformly within that row.
For completeness, let Px,i be Alice’s commuting parity observables and let Vy be Bob’s
observables on the common space. For the new variables use Px,i and Vy. Alice uses the
original joint measurement on parity rows; on an equality row she measures Px,i and returns
the same bit twice. The ﬁrst equality position agrees perfectly and the second has exactly
the old disagreement probability. The equality rows have total weight 1/2, giving error e/4.
Invalid parity answers of an old strategy can ﬁrst be replaced by a ﬁxed valid answer without
decreasing success.
For soundness, write Ux,i and Vy for the new variable observables. On each parity row
let Alice’s commuting observables be Px,i, with product σxI. On each equality row her two
valid answers coincide, so they are generated by one involution Ex,y,i. Let epar and eeq be the
conditional errors on the two types of rows; then e′ = ( epar + eeq)/2. In normalized Hilbert–
Schmidt norm,
epar =
∑
x
πX(x)
12
3∑
i=1
∥Px,i − Ux,i∥2
2,
and
eeq =
∑
x,y,i
π(x, y, i)
8
(
∥Ex,y,i − Ux,i∥2
2 + ∥Ex,y,i − Vy∥2
2
)
.
Decode with Alice’s parity measurement Px,i and Bob’s Vy. The squared triangle inequality
gives
∥Px,i − Vy∥2
2 ≤ 2∥Px,i − Ux,i∥2
2 + 2∥Ux,i − Vy∥2
2.
Since ∑
y π(x, y, i) ≤ πX(x) and ∥U − V ∥2
2 ≤ 2∥U − E∥2
2 + 2∥E − V ∥2
2, the decoded error is at
most
6epar + 8eeq ≤ 16e′ ≤ 18e′.
The conservative constant 18 will suﬃce.
Enumerate the bounded ﬁnite sampler and aggregate probabilities of identical original ques-
tions, retaining the position actually checked; do not reveal its hidden random seed to Alice.
The resulting probabilities are rational. After positional normalization, duplicating rows with
a common denominator gives a uniform row list. Variables retain their global names across
copies. For ﬁxed Bob observables, identical copies have the same local optimization for Alice,
so choosing a least-error measurement among the copies shows that this duplication does not
change the supremal value. This may be very large but is a terminating computation. Keep
3

multiplicities rather than replacing them by an unweighted set. Thus the source theorem and
Lemma 3 give a uniform list with
YES error ≤ ε/4, NO synchronous value ≤ σ := 1 − 1
1296. (5)
The soundness follows because a new value greater than 1 − 1/1296 would give an old value
greater than 71/72. Suprema need not be attained.
3 From game errors to averaged unitary relations
Allow nonempty contexts of sizes 1, 2, 3; this slightly generalizes the normalized source. Let
there be N ≥ 1 rows and remove unused variables. For each row, list the square relation for
each variable, the signed product relation, and one positive commutator xjxkxjxk = I for each
pair. Complete this list to seven relations with empty words equal to I. There are
R = 7 N
listed relations, each of length at most four. Occurrences in diﬀerent rows remain distinct. For
unitary variables V = ( Vj) let
ξ(V ) = 1
R
R∑
r=1
∥Vi1(r) · · · Vik(r)(r) − σrI∥2
2.
Lemma 4. A synchronous strategy of error e yields unitary variables with ξ ≤ 34e in the same
dimension. Conversely, unitary variables with averaged error ξ yield a synchronous strategy of
error at most 50ξ in the same dimension.
Proof. For the ﬁrst direction let Ai
j be the row observables and Xj the variable involutions.
Put dij = ∥Ai
j − Xj∥2
2. The normalized-trace expression for a maximally entangled strategy
gives
e = 1
N
∑
i
1
4ki
∑
j∈Si
dij,
∑
i,j
dij ≤ 12Ne.
Unitary telescoping bounds a product residual squared by 3 ∑
j dij. A pair commutator residual
squared is at most 8(dij + dik). Summing pairs costs at most 16 ∑
j dij. Squares and empty
words have zero error. Consequently Rξ ≤ 228Ne, so ξ ≤ (228/7)e < 34e.
For the reverse direction, round each unitary Vj spectrally to the closest Hermitian involu-
tion Xj. Eigenvalue by eigenvalue,
∥Vj − Xj∥2
2 ≤ ∥V 2
j − I∥2
2.
For each row, the new product residual squared is at most four times the sum of its old
product residual squared and the individual rounding errors. Write ejk = ∥VjVkVjVk − I∥2 for
the original pair residual. A new pair commutator residual squared is at most
3e2
jk + 12∥Vj − Xj∥2
2 + 12∥Vk − Xk∥2
2.
Each variable appears in at most two pairs. Its squared rounding error therefore has coeﬃcient
at most 4 + 2 · 12 = 28 ; the old product and pair residuals have coeﬃcients at most four and
three. Hence the sum of the new product and pair commutator squared errors is at most 28
times the original seven-relation squared-error sum for that row.
For a row of size three write its rounded variables as X, Y, Z . Pinch Y to the algebra
commuting with X:
T = ( Y + XY X )/2, Y ′ = sign( T),
4

with sign +1 on a zero eigenvalue. Then Y ′ is an involution commuting with X, and
∥Y − Y ′∥2
2 ≤ 1
2 ∥XY − Y X ∥2
2. (6)
Indeed the oﬀ-diagonal part of Y in the X-eigenspaces has squared norm ∥XY − Y X ∥2
2/4.
The sign-rounding error of the diagonal Hermitian contraction is no larger than this: use
(1 − |λ|)2 ≤ 1 − λ2 and Y 2 = I. The two errors are orthogonal.
Alice uses the commuting involutions X, Y ′, σXY ′ and their joint measurement. The sum
of squared distances to X, Y, Z is at most
2∥XY Z − σI∥2
2 + 3∥Y − Y ′∥2
2.
Thus this row’s game error is at most one sixth of its new product-plus-commutator error
sum. For a size-two row use X, σX , giving error ∥XY − σI∥2
2/8; for size one use the constant
σ, giving error ∥X − σI∥2
2/4. All cases are bounded by one quarter of the new error sum.
Averaging yields at most 28 · 7ξ/4 = 49 ξ ≤ 50ξ. Bob uses the Xj and Alice the transposed
joint measurements on a maximally entangled state. These extend to a synchronous strategy
on the disjoint union of question sets.
4 A homogeneous multiplication block
Put a = 3 /5, b = 4 /5, c = ab = 12 /25, and deﬁne
H(U, V, W, Z ) =
(
aU bW
bZ −aV
)
.
Lemma 5. For unitary m × m labels, set E = UZ ∗ − WV ∗. Then
HH ∗ =
(
I cE
cE∗ I
)
.
In particular H is unitary precisely when (UZ ∗)(V Z∗) = WZ ∗. Its squared singular values
belong to [1/25, 49/25], its operator norm is at most 7/5, and
− 1
m log | det H| ≤ 72
49∥E∥2
2. (7)
Proof. Direct multiplication proves the identity. Since ∥E∥op ≤ 2, the eigenvalues are 1±csj(E),
giving the interval. Also
− 1
m log | det H| = − 1
2m
∑
j
log(1 − c2sj(E)2).
For 0 ≤ u ≤ 4c2 = 576 /625, − log(1 − u) ≤ u/(1 − 4c2). Its coeﬃcient is c2/[2(1 − 4c2)] =
72/49.
Uniform invertibility is essential here: a Hilbert–Schmidt estimate alone would not control
a logarithmic determinant near zero.
For each original signed word add two padding letters pp and use fresh preﬁx labels of
lengths 2, . . . , k − 1 for its padded length k. Introduce one common reference label z. A
multiplication gate has lower-left label z, takes two successive factors as its diagonal labels,
and has a fresh preﬁx as output, except that the ﬁnal output is σz. The two input labels may
coincide, but neither equals z or its own output.
For each original word include its own extra gate imposing p2 = I, with the same label
p shared across words. This deliberate repetition prevents an error in one padding gate from
5

being charged to every relation. Empty original words require one padded gate and their own
square gate. A word of length at most four uses at most six gates including the square gate.
Gates assigned to diﬀerent words are disjoint occurrences.
Take 25 copies of each gate and initially one singleton block for every label. Write the
resulting coeﬃcient matrices as A(0)
ℓ . Each entry has only one label. The sums ∑
ℓ A(0)
ℓ A(0)∗
ℓ
and ∑
ℓ A(0)∗
ℓ A(0)
ℓ are the identity block by block. For a gate this follows from a2 + b2 = 1 and
the stated label separation, even when its two inputs coincide. Coeﬃcient supports are disjoint.
Let
qℓ = Tr(A(0)∗
ℓ A(0)
ℓ ) ∈ N.
These are positive integers: the 25 copies contribute 9 per diagonal occurrence and 16 per
oﬀ-diagonal occurrence, while the singleton contributes 1.
5 Weighted rational normalization
Lemma 6. The construction can be completed to rational matrices Aℓ ∈ MD(Q) and positive
integers wℓ, t such that
D = t2 =
∑
ℓ
w2
ℓ ,
∑
ℓ
AℓA∗
ℓ =
∑
ℓ
A∗
ℓ Aℓ = ID, Tr(A∗
ℓ Ah) = δℓhw2
ℓ , (8)
label ℓ has at least w2
ℓ /2 singleton blocks , 200R ≤ D ≤ 8000R. (9)
The tuple Bℓ = tAℓ/wℓ is real rational and satisﬁes (2).
Proof. For each initial label choose wℓ = ⌈√2qℓ⌉ and append w2
ℓ − qℓ singleton blocks. Its
squared coeﬃcient norm becomes w2
ℓ and its singleton count is 1 + w2
ℓ − qℓ ≥ w2
ℓ /2. Moreover
2qℓ ≤ w2
ℓ < 6qℓ. Let D0 = ∑
ℓ w2
ℓ and t = ⌈√D0⌉. Append t2 − D0 entirely new labels, each
appearing in one singleton only, and give each weight w = 1 . This makes D = t2 and preserves
all identities. New labels obey the singleton condition as well.
If n is the number of original variables, n ≤ 3N = 3 R/7. There are at most 4R preﬁx
labels, so the initial label count is s0 ≤ n + 2 + 4 R ≤ 33R/7 < 5R. The number G of gates
before replication obeys 2R ≤ G ≤ 6R. Thus the initial scalar dimension is
d0 =
∑
ℓ
qℓ = s0 + 50G ≤ 305R.
We have 2d0 ≤ D0 < 6d0 and D ≤ 4D0, proving ( 9) with conservative constants. The construc-
tion and dense rational encoding have polynomial size in the expanded row list. Coeﬃcient
numerators and denominators have O(log R) bits.
For Bℓ = tAℓ/wℓ, ( 8) gives τD(B∗
ℓ Bh) = δℓh. Therefore, for any density Q, τDΦQ(I) = 1
and
cap(ΦQ)1/D ≤ det ΦQ(I)1/D ≤ 1.
For Q0 = diag( w2
ℓ /D), we instead have ΦQ0 (X) = ∑
ℓ AℓXA∗
ℓ , a unital trace-preserving map.
Its capacity is one: operator concavity of log gives Tr log ΦQ0 (X) ≥ Tr log X for X > 0, and
X = I gives the reverse bound. This is also the standard doubly stochastic capacity identity
[5]. Hence C(B) = 1 .
It is the intermediate tuple A, not generally B, whose coeﬃcient map is doubly stochastic.
The ﬁnal rational coeﬃcients Bℓ do not belong to a ﬁxed ﬁnite alphabet. These distinctions
are needed for the ﬁxed-gap result.
6

6 The averaged determinant transfer
Let ρ = R/D, so 1/8000 ≤ ρ ≤ 1/200, and write LA(Z) = ∑
ℓ Aℓ ⊗Zℓ (likewise for LB). For an
original relation r, let er denote its normalized Hilbert–Schmidt residual norm in the deﬁnition
of ξ.
Proposition 7. For the tuple B above, unitary variables of mean relation error ξ in dimension
m give
Fm(B) ≥ exp
(
−(3600/49)ρξ
)
. (10)
Conversely, if Fm(B) ≥ 1−δ with 0 < δ < 1, there are unitary variables in the same dimension
with
ξ < 35δ/ρ. (11)
In particular the source constraint-variable game has a synchronous strategy of error at most
1750δ/ρ.
Proof. For the forward direction choose z = p = I as matrix labels. Assign exact generator
products to preﬁxes and I to the added free labels. Every gate except the ﬁnal gate of an
original relation is unitary. Set Yℓ = ( wℓ/
√
D)Vℓ, where Vℓ are the unitary labels. Then∑ τm(Y ∗
ℓ Yℓ) = ∑ w2
ℓ /D = 1 , and the pencil equals LA(V ). Each original ﬁnal gate occurs 25
times. Equation ( 7) gives
− log |det LA(V )|2/(Dm) ≤ 50
D
72
49
R∑
r=1
e2
r = 3600
49 ρξ.
For the reverse direction choose a maximizing feasible tuple Y . Write
Zℓ =
√
D
wℓ
Yℓ, X = LA(Z) = LB(Y ).
The Gram identity gives τDm(X∗X) = 1 . A block diagonal polar unitary P satisﬁes
∆2 := ∥X − P∥2
2 = 2(1 − τDm|X|) ≤ 2(1 −
√
1 − δ) ≤ 2δ. (12)
This uses arithmetic–geometric mean on the singular values, and allows arbitrary nonunitary
starting labels.
Let Vℓ be polar unitaries of Zℓ. The singleton multiplicities in ( 9) give
∑
ℓ
w2
ℓ
D ∥Zℓ − Vℓ∥2
2 ≤ 2∆2.
With H = LA(V ), orthogonal supports therefore imply ∥H − X∥2 ≤
√
2∆ and ∥H − P∥2 ≤
(1 +
√
2)∆. Lemma 5 gives ∥H∥op ≤ 7/5, including all singleton blocks, so
∥HH ∗ − I∥2
2 ≤ C0∆2, C 0 = 144
25 (3 + 2
√
2).
For a gate g with unitary labels U, V, W, Vz, put eg = ∥UV ∗
z − WV ∗∥2. Its normalized squared
unitarity defect is c2e2
g. Its 25 copies contribute 50c2e2
g/D to the global squared defect. Thus
50c2
D
∑
g
e2
g ≤ C0∆2.
7

Right multiply all labels by V ∗
z to ﬁx the reference, and denote the gauged labels by ˜Vℓ. Let
Gr be the occurrences of gates assigned to relation r, including its own copy of the square gate
p2 = I. Telescoping the padded product and then removing its two padding factors gives
∥˜Vi1(r) · · · ˜Vik(r)(r) − σrI∥2 ≤
∑
g∈Gr
eg, |Gr| ≤ 6.
The last summand can be chosen as the residual of that relation’s square gate. Cauchy–Schwarz
bounds the squared left-hand side by |Gr| ∑
g∈Gr e2
g. The sets Gr are disjoint sets of occurrences,
even when their labels coincide. Consequently
ξ ≤ 6
R
∑
g
e2
g ≤ 12C0
50c2
δ
ρ = (18 + 12
√
2) δ
ρ < 35 δ
ρ.
Apply Lemma 4 for the game strategy.
7 A ﬁxed gap and nonrecursive witnesses
Proof of Theorem 1. Fix ε = 2 −40 in the source theorem and perform the positional normal-
ization. Let
β = 1 − σ
3500 = 1
4 536 000 , γ = β/8000.
For a YES instance, ( 5) and Lemma 4 yield averaged unitary errors approaching at most 34ε/4.
Taking the supremum in ( 10) gives
F∞(B) ≥ exp
(
−3600
49 ρ34ε
4
)
≥ 1 − 3600
49
1
200
34
4 2−40.
The last loss equals 153/(49 ·240) < 1/145152000000 = γ/4, by direct rational arithmetic. This
establishes ( 3) without assuming an attaining strategy or perfect completeness.
For a NO instance, suppose F∞(B) > 1 − βρ. There would be a ﬁnite m and a feasible
witness with Fm(B) > 1 − βρ. Proposition 7 would give a synchronous game strategy of error
less than
1750β = (1 − σ)/2,
contradicting (5). Thus F∞(B) ≤ 1−βρ ≤ 1−γ. Lemma 6 proves the promised rationality and
capacity identity. A γ/8 approximation separates the two cases, for example by comparison
with 1 − 5γ/8, and would decide the halting problem.
Proof of Corollary 2. At ﬁxed m, ( 1) is a compact semialgebraic optimization in the real and
imaginary parts of the entries. For a rational threshold r ≥ 0, comparison with r can be
expressed using the squared determinant polynomial and rDm; real quantiﬁer elimination makes
Fm uniformly computable. This is a computability statement, not an eﬃciency claim.
Suppose a total recursive bound b(L) guaranteed a witness with additive deﬁcit at most γ/8
for every encoded instance of length L. Evaluate all Fm with 1 ≤ m ≤ b(L) to error at most
γ/16, and take their maximum. On a YES instance this is at least 1 −7γ/16; on a NO instance
it is at most 1 − 15γ/16. Comparing with 1 − 3γ/4 decides halting, a contradiction.
The absence of a uniform recursive bound does not say that every ﬁxed tuple has a non-
computable real optimum, or that every instance is diﬃcult. At every ﬁxed dimension the
optimization remains decidable. Nor does the proof produce non-hyperlinear groups: its source
completeness is strictly less than one.
8

8 Diagnostics and scope
The accompanying compact compiler stores scalar blocks and multiplicities rather than allo-
cating the full dense tuple. Exact rational checks cover 70 context lists, all ﬁve encountered
local label patterns, the stochastic identities, coeﬃcient orthogonality, square normalization
and singleton proportions. Forty-eight complex-matrix cases check each of the forward bound,
reverse bound and unitary-to-strategy rounding, with 48 inexact relation controls. These are
ﬁnite diagnostics, not a proof of undecidability.
For the six-row magic square, the compiler produces R = 42 , 210 multiplication gates
before replication, D = 23409 , and 438 ﬁnal labels. The standard four-dimensional Pauli
assignment makes the determinant objective exactly one; all 512 scalar sign assignments fail
the row system. A separate positional-normalization veriﬁer covers a nonuniform rational
distribution with coincident Bob queries, including exhaustive scalar cases and complex-matrix
tests of both error transfers. This is a familiar illustration of the construction, not a new
nonlocality result; neither veriﬁer implements the full machine-to-game source reduction.
The proof has several explicit limits. The gap γ ≈ 2.76 · 10−11 is a conservative theoreti-
cal constant, not a claim about achievable numerical experiments. The source-to-explicit-list
expansion need not be eﬃcient. The ﬁnal coeﬃcients are rational with controlled bit length,
but are not uniformly bounded in one ﬁxed alphabet and do not themselves form a doubly
stochastic tuple. The capacity-one identity uses a displayed covariance Q0. The source game
hardness, quantum logic background and general noncomputability of tracial approximation are
credited to prior work. Targeted source searches do not certify worldwide novelty or establish
an importance rating.
Assistance and assessment. Developed with substantial OpenAI Codex assistance in deriva-
tion, writing, source checking and ﬁnite computations. GPT-6 Astra at xhigh eﬀort was re-
quested to review the candidate construction in reused context; runtime model identity was not
separately attested. Any ﬁnal exact-version assessment is recorded separately and must not be
inferred from an earlier paper’s score. No human peer review, certiﬁed independent context or
proof-assistant veriﬁcation is claimed.
References
[1] A. Taller and T. Vidick, Approximating the quantum value of an LCS game is RE-hard ,
arXiv:2507.22444v2 (1 April 2026), especially Sections 2.4, 3.2 and 5.1, Theorem 5.2 and
its proof. https://arxiv.org/abs/2507.22444v2.
[2] Z. Ji, A. Natarajan, T. Vidick, J. Wright and H. Yuen, MIP*=RE, arXiv:2001.04383. https:
//arxiv.org/abs/2001.04383.
[3] I. Goldbring and B. Hart, The universal theory of the hyperﬁnite II1 factor is not computable ,
Bulletin of Symbolic Logic 30(2) (2024), 181–198. https://doi.org/10.1017/bsl.2024.
7.
[4] R. Cleve, E. Culf and A. Taller, XOR Games at Full Tilt: The Hardness of Binary Nonlocal
Games, arXiv:2607.06876v1 (8 July 2026), especially Section 6.4. https://arxiv.org/abs/
2607.06876v1.
[5] A. Garg, L. Gurvits, R. Oliveira and A. Wigderson, Operator Scaling: Theory and Applica-
tions, Foundations of Computational Mathematics 20 (2020), 223–290. https://doi.org/
10.1007/s10208-019-09417-z .
9

[6] L. Eriksson, Exponential witness size and undecidable saturation for ampliﬁed determi-
nants, AIRR working paper, ARR-2026-438PTRJA439VSRTW, v1 (2026). https://airr.
science/papers/ARR-2026-438PTRJA439VSRTW/versions/v1/.
[7] W. Slofstra, The set of quantum correlations is not closed , Forum of Mathematics, Pi 7
(2019), e1. https://arxiv.org/abs/1703.08618.
10