# Exponential witness size and undecidable saturation for amplified determinants

Extracted text; equations are authoritative in paper.pdf.

Exponential witness size and undecidable saturation
for amplified determinants
Lluis Eriksson
Independent researcher, Sweden
17 October 2026 — research preprint
Abstract
W e construct real rational matrix tuples whose covariance-optimized operator capacity
is explicitly known, but whose amplified determinant witnesses have large or undecidable
dimension requirements. A rational multiplication block converts signed unitary relations
into a linear matrix pencil. Its unequal coeﬀicients keep every unitary-labelled block uni-
formly invertible, allowing quantitative control of the logarithmic determinant. Balancing
gives both a doubly stochastic coeﬀicient map and a scalar Gram matrix. Applied to finite
Clifford relations and established stability bounds, the construction yields a polynomial-size
family with an exact finite optimizer for which inverse-polynomial relative accuracy requires
exponentially large auxiliary dimension. Applied to known results on linear-system games,
it makes both finite exact saturation and asymptotic saturation undecidable, and produces
nonattainment at every finite auxiliary size. The undecidability and Clifford dimension the-
orems are inherited inputs; the contribution is their balanced determinant reduction. No
constant-gap approximation hardness or noncomputability of numerical approximation is
asserted.
1 V alue and witness size
F orA= ( A1,...,A s) ∈ MD(C)s, put τm = Tr /m and
Fm(A) = max∑
i τm(Y ∗
i Yi)=1
det
 X
i
Ai ⊗ Yi
!
2/(Dm)
, F∞(A) = sup
m≥1
Fm(A). (1)
The maximum at fixed m exists by compactness. Define
ΦQ(X) =
X
i,j
QijAiXA∗
j , C(A) = max
Q⪰0, TrQ=1
cap(ΦQ)1/D, (2)
cap(Φ) = inf
X>0, det X=1
det Φ(X).
This is operator-scaling capacity , not a communication capacity . Our tuples satisfy the exact
promises X
i
AiA∗
i =
X
i
A∗
i Ai = ID, τ D(A∗
i Aj) = δij
s . (3)
All their entries belong to the fixed alphabet
A = {0,±1,±3/5,±4/5} ⊂ Q.
Theorem 1 (Exponential size at inverse-polynomial accuracy) . There is an explicit family
A(n) ∈ MDn(Q)sn, n≥ 2, with entries in A, satisfying (3), such that sn = O(n2), Dn = O(n4),
and
F∞(A(n)) = C(A(n)) = 1 /sn.
1

This value is attained at auxiliary dimension 2⌊n/2⌋. Set
εn =

10000Dn(n+ 1)2−2. (4)
F or every m,
Fm(A(n)) ≥ (1 − εn)F∞(A(n)) = ⇒ m≥ 2⌊n/2⌋−1.
Consequently no polynomial in the rational input length and 1/ε bounds the auxiliary dimension
needed for relative ε approximation of F∞ on al l tuples.
Theorem 2 (Undecidable saturation). On an effectively constructed subclass of tuples satisfying
(3) with entries in A, each of the fol lowing questions is undecidable:
∃m≥ 1 : Fm(A) = C(A), F∞(A) = C(A).
F or every tuple in this subclassC(A) = 1 /sis explicitly known. Some tuples satisfy F∞(A) = 1 /s
while Fm(A) <1/s for every finite m. There is no total recursive bound, in the rational input
length, on the least exactly saturating m among instances where such an m exists.
Theorem 1 is a family statement, not a growth assertion for one fixed tuple. It is stronger
than an exact-attainment obstruction in its treatment of positive error, but weaker than a
nonrecursive approximation bound. Theorem 2 concerns equality with a specified threshold;
an undecidable equality test does not by itself make approximation of a real-valued function
uncomputable.
The construction below is independent of the author’s earlier constant-factor capacity com-
parison [ 5]. It does not preclude polynomial-size witnesses at a fixed ratio such as 1/e, nor
polynomial algorithms for the capacity value or for detecting noncommutative invertibility .
Closest antecedents and scope. Undecidability for variable-size matrix equations is estab-
lished: Herrmann, T sukamoto and Ziegler [ 6, Theorem 2(b)–(d)] treat quadratic systems, a
single quartic equation with adjoints, and nonrecursive dimension bounds. Lee and W atrous
[7, Section 3] prove hardness of unitary quadratic minimization in a prescribed matrix dimen-
sion. Our reduction addresses a more constrained target: a homogeneous rational pencil with
both identities in ( 3), an explicitly known capacity , and quantitative determinant control in un-
changed auxiliary dimension. These antecedents rule out claiming generic matrix undecidability
or generic unitary optimization hardness as new results.
Musat and Rørdam [9, Proposition 3.2 and Theorems 3.6, 4.1] connect projection constraints
with unitary correlations and obtain nonclosure and channels requiring infinite-dimensional an-
cillas. Herrmann and Ziegler [ 8, Theorem 4.10] discuss the connection between matrix fea-
sibility and recursive dimension bounds. The present claims concern the specified determi-
nant functional and its rational balanced encoding; the general phenomena and the dimension-
enumeration argument have these antecedents.
2 A rational block for multiplication
All 2-norms below are normalized: ∥T∥2
2 = τm(T∗T) on Mm. Let
a= 3 /5, b = 4 /5, c = ab= 12 /25.
F orm× m unitaries U,V,W,Z define
H(U,V,W,Z ) =
aU bW
bZ −aV

. (5)
2

Lemma 3. The block H is unitary if and only if
(UZ∗)(VZ∗) = WZ∗.
F or al l unitary labels, whether or not this relation holds,
1
25I ⪯ HH∗ ⪯ 49
25I, −log |det H|1/m ≤ 72
49 ∥UZ∗ − WV ∗∥2
2 . (6)
Proof. Put R= UZ∗ − WV ∗. Direct multiplication gives
HH∗ =
 I cR
cR∗ I

.
The off-diagonal block vanishes precisely when the asserted relation holds. Since ∥R∥op ≤ 2, the
spectral bounds follow from 1 ± 2c= 1 /25,49/25. The block determinant formula gives
det(HH∗) = det( I− c2R∗R).
Thus, with normalized trace on Mm,
−log |det H|1/m = −1
2 τm log(I− c2R∗R) ≤ c2
2(1 − 4c2)τm(R∗R) = 72
49 ∥R∥2
2 .
W e used−log(1 − x) ≤ x/(1 − 4c2) for 0 ≤ x≤ 4c2.
In particular ∥H∥op ≤ 7/5 and σmin(H) ≥ 1/5. The unequal coeﬀicients prevent a logarith-
mic singular-value tail from appearing in the later approximation argument.
3 Compiling signed relations into a balanced pencil
A signed presentation is a finite list of requirements
xi1 · · ·xik = σI, σ ∈ {1,−1}, (7)
on unitary generators. Repetitions and empty words are permitted. Its size counts the generators
and the total listed word length, together with the number of relations.
Add a new generator t, impose t2 = I, and append tt to every original word. This leaves
exact solvability unchanged and preserves existence of arbitrarily accurate normalized- 2-norm
solutions. Every padded word now has length at least two. W e call the maximum padded length
r; include r≥ 2 to cover the extra relation t2 = I.
Introduce a reference label z, all generator labels, and fresh labels for proper prefixes of
lengths 2,...,k − 1 of each padded word of length k. Labels are new for each occurrence of a
word. Use k− 1 blocks ( 5): multiply the first two letters, then each prefix by the next letter.
Intermediate outputs have fresh labels; the final output is σz. The lower-left label is always z.
Include one singleton block for every label. The pencil is homogeneous and linear in its labels;
it contains no fixed identity matrix entry . At a unitary solution, right multiplication of every
label by Z∗ fixes the reference and recovers ( 7).
Lemma 4 (Balancing). This construction can be completed in polynomial time to a pencil
L(Y) =
sX
ℓ=1
Aℓ ⊗ Yℓ
with Aℓ ∈ MD(Q), entries in A, and (3). A unitary in this pencil is equivalent, in the same
auxiliary dimension, to a unitary solution of the signed presentation.
3

Proof. Initially include 25 copies of each multiplication block and one singleton of every label.
In a multiplication block, its two input labels are distinct from z, and its output is either a fresh
label or ±z. The two input labels may coincide. Each scalar entry contains exactly one label.
F or the coeﬀicient matrices of this block, both sumsPAℓA∗
ℓ and PA∗
ℓ Aℓ equal I2: the diagonal
sums are a2 + b2 = 1 , and the off-diagonal sums vanish because an input never coincides with
the reference or its own output. Singleton blocks have the same property .
Different coeﬀicient matrices have disjoint entry supports. Let qℓ be the squared F robenius
norm of coeﬀicient ℓ. Each qℓ is a positive integer: the 25 repeated blocks contribute 9 per
diagonal occurrence and 16 per off-diagonal occurrence; the initial singleton contributes 1. Set
M = max ℓ qℓ and append M − qℓ singleton blocks of label ℓ. All coeﬀicient norms now equal
M. Their squared norms sum to the scalar dimension D, so D= sM. The stochastic identities
persist block by block, and disjoint supports give the Gram identity in ( 3). The dimensions and
number of entries are polynomial in the presentation size.
If the completed pencil is unitary , its singleton blocks make all labels unitary and Lemma 3
recovers the relations after the common right gauge. Conversely , a solution extends to unitary
prefix labels, making every block unitary . Added singleton blocks impose no further constraints.
F or arbitrary labels the construction gives
τDm
 
L(Y)∗L(Y)

= 1
s
X
ℓ
τm(Y∗
ℓ Yℓ). (8)
This identity , as well as both stochastic identities, is important; norm balancing alone would
not imply them.
4 Capacity and exact equality
Proposition 5. F or every compiled tuple, C(A) = 1 /s, Fm(A) ≤ 1/s, and
Fm(A) = 1 /s ⇐ ⇒ the signed presentation has an m-dimensional unitary solution .
Proof. W riteΨ(X) = P
ℓ AℓXA∗
ℓ . By ( 3), Ψ is unital and trace preserving. Operator concavity
of the logarithm gives Tr log Ψ(X) ≥ Tr Ψ(log X) = Tr log X for X > 0; unitality ensures
Ψ(X) > 0. Thus cap(Ψ) = 1 , with the upper bound witnessed by X = I. This is also the
standard doubly stochastic capacity identity [ 1]. At Q= Is/s it yields a capacity root 1/s.
F or any density Q, normalized trace and ( 3) give τDΦQ(I) = 1 /s. Evaluating capacity at
I and applying determinant arithmetic–geometric mean proves the reverse bound. The same
inequality with ( 8) gives Fm ≤ 1/s. Equality in this scalar AM–GM holds precisely when√sL(Y) is unitary . Apply Lemma 4 to the labels √sYℓ. Conversely , unitary labels Uℓ give
feasible coeﬀicients Yℓ = Uℓ/√s and attain equality .
5 Quantitative transfer without a logarithmic-tail assumption
Let a relation error mean the normalized 2-norm distance of its word from its signed identity .
Proposition 6. Suppose the padded signed presentation has an m-dimensional unitary assign-
ment with al l relation errors at most η. Then
sFm(A) ≥ exp(−72η2/49). (9)
Conversely, if sFm(A) ≥ 1 − ε, 0 < ε <1, then its original unpadded presentation has an
m-dimensional unitary assignment with every relation error at most
KD,r
√ε, K D,r = 5 r
√
D(
√
D+ 1). (10)
4

Proof. F or the first assertion choose Z = I, and assign each proper prefix its exact generator
product. Every internal gate is exact and every final gate has error at most η. Singleton blocks
are unitary . Lemma 3 bounds each gate’s normalized log-determinant loss by 72η2/49 and
ensures uniform invertibility , including erroneous gates. T aking the dimension-weighted average
over all blocks proves ( 9); (8) normalizes the labels by √s.
F or the converse choose a maximizing feasible tuple and putX = √sL(Y). Then τ(X∗X) = 1
and its squared determinant root is at least 1 − ε. A block diagonal polar unitary P satisfies
δ2 := ∥X− P∥2
2 = 2(1 − τ|X|) ≤ 2(1 −
√
1 − ε) ≤ 2ε. (11)
Here the geometric mean of singular values is at most their arithmetic mean.
Let Vℓ be a polar unitary of Zℓ = √sYℓ. An original singleton block is present for each label,
so
d2
ℓ := ∥Zℓ − Vℓ∥2
2 ≤ Dδ2.
Set B = L(V). By ( 8),
∥B− X∥2
2 = 1
s
X
ℓ
d2
ℓ ≤ Dδ2.
Every label of B is unitary , hence ∥B∥op ≤ 7/5, and
∥BB∗ − I∥2 ≤ (∥B∥op + 1) ∥B− P∥2 ≤ 12
5 (
√
D+ 1)δ.
No operator-norm bound on the original Yℓ has been assumed.
F or any individual gate, Lemma 3 identifies its normalized squared defect as c2 ∥R∥2
2. It
contributes 2/D times this quantity to the global squared defect. Therefore every gate error is
at most
5
p
D/2(
√
D+ 1)δ.
Right gauge all Vℓ by V∗
z . T elescoping unitary products over a padded word uses at most r− 1
gate errors. Removing the appended ttcosts at most one more, from the explicit padding-square
relation. Inserting ( 11) proves (10).
In particular, F∞(A) = 1 /sif and only if the signed presentation admits arbitrarily accurate
finite matrix solutions. The auxiliary dimension is unchanged in both transfers. The lower
bound on gate singular values is what makes the forward implication valid for the determinant,
rather than merely for distance to the unitary group.
6 The Clifford family: large witnesses for an easy value
Use the n unitary generators with relations
x2
i = I, x ixjxixj = −I (i<j ). (12)
Exact solutions are the standard Clifford representations. In dimension 2⌊n/2⌋ they exist, and
their dimension is minimal. These established representation facts supply the exact witness; we
do not claim a new Clifford dimension theorem.
W e use the following robust version, in the formulation of Slofstra [ 4, Lemmas 3.1 and 3.4].
F or the finite Clifford group with central involution J, a θ-approximate representation of its
defining relations induces an (n+ 1)2θ-almost-homomorphism by normal forms. If an u-almost-
homomorphism has ∥ψ(J) − I∥2 > 42u, its dimension is at least 2⌊n/2⌋−1. This follows from
finite-group representation stability; the dimension lower bound is an external input.
5

Proof of Theorem 1. Compile (12). There are O(n2) words of length at most four, so the padded
maximum length is r= 6 . Counting the labels and the reference coeﬀicient’s weight gives
sn = 2 n2 + n+ 2, Mn = 48 n2 + 16n+ 33,
Dn = snMn = 96 n4 + 80n3 + 178n2 + 65n+ 66.
The reference weight is maximal: original generators have weight 18n+ 1 , fresh prefixes have
weight 26, and the padding generator has weight 18
 
n+
 n
2

+ 1

+ 1 ≤ Mn. These formulas give
sn = O(n2) and Dn = O(n4) and bound the dense rational encoding length by a polynomial in
n. Proposition 5 and an exact Clifford representation give the claimed value and attainment.
Assume near-saturation in dimension m. Proposition 6 gives unitary Xi obeying all original
signed words within
η= 30
p
Dn(
p
Dn + 1)√ε≤ 60Dn
√ε.
F or a unitary ,
X−1
i − Xi

2 =
X2
i − I

2 ≤ η. Replacing the two inverses therefore gives
XiXjX−1
i X−1
j + I

2
≤ 3η.
Put J = −I. Its square and centrality relations are exact; the assignments form a3η-approximate
representation of the finite Clifford group. Its normal-form map is an u-almost-homomorphism
with
u≤ 3(n+ 1)2η≤ 180Dn(n+ 1)2√ε.
At (4), u≤ 0.018 <1/16 and 42u≤ 0.756 <2 = ∥−I− I∥2. The cited robust dimension bound
proves the result.
Both the full input length and 1/εn = O(n12) are polynomial in n, whereas the necessary
m grows exponentially . A putative polynomial bound in these two input parameters would
contradict this family .
The tolerance is intentionally conservative. No optimal dependence on n or ε is claimed.
A scalar witness and the precision regime. The family also admits a simple witness
illustrating this limitation. Set every label to 1 and normalize by √sn. All singleton, internal
and positive final blocks are unitary . Each negative relation contributes only its final block,
whose determinant magnitude is 7/25, repeated 25 times. Hence
snF1(A(n)) ≥ (7/25)50(n
2)/Dn = 1 − O(n−2).
Thus a scalar witness already approaches the optimal value along the family . The exponential
lower bound concerns the much smaller error (4); it supplies no fixed-gap separation from scalar
witnesses.
7 Linear-system games: two different undecidable questions
F or a binary system Bx = b, its operator solutions satisfy
x2
j = I,
Y
j:Bij=1
xj = ( −1)biI, x jxkxjxk = I when j,k occur in the same row .
With the square relations, the last equations impose commutation. This is the solution-group
presentation with its central involution J fixed to −I.
W e require three established facts. Perfect finite-dimensional strategies for binary linear-
system games are undecidable, and so are perfect strategies in the closure of finite-dimensional
correlations; a game can have the latter without the former [ 2, Theorems 1.1–1.2 and Corollary
6

1.4]. Exact strategies correspond to finite matrix solutions [ 2, Theorem 3.2]. Arbitrarily near-
perfect quantum strategies correspond to arbitrarily accurate matrix representations with J =
−I [3, Theorem 5.1, Corollaries 5.2–5.3 and Proposition 2.7]. The last converse uses the general-
state result in Section 5, not just the maximally entangled case in Section 4. Remove zero
columns before applying that result, assigning the unused generators I when restoring them.
Replacing inverse commutators by the positive words above preserves approximate solvability:
when square errors are at most η, each replacement costs at most 2η. Conversely a solution with
J nontrivial can be restricted to its negative eigenspace in the exact case; the approximate
correspondence cited above handles the limiting case. Unused variables can be assigned the
identity .
Proof of Theorem 2. Compile this signed presentation. Proposition 5 makes finite exact satura-
tion equivalent to a finite matrix solution; Proposition 6 makes asymptotic saturation equivalent
to arbitrarily accurate matrix solutions. The cited game results transfer both undecidability as-
sertions and the existence of asymptotic saturation without any finite exact saturation.
If a total recursive bound on the least exactly saturating auxiliary dimension existed as a
function of input length, enumerate all dimensions up to that bound. At any fixed m, the
equations L(U)∗L(U) = I are a finite system of polynomial equations over the real and imag-
inary parts of the unknown entries, with rational coeﬀicients. Quantifier elimination over real
closed fields decides their feasibility . The bounded enumeration would decide finite saturation,
contradicting the first assertion.
8 Diagnostics, attribution and limits
The accompanying implementation generates a compact block description instead of materializ-
ing a large dense tuple. F or the magic-square relations, it produces s= 119 labels, 142 multipli-
cation gates before replication, M = 2817 and D= 335223 . With the standard four-dimensional
Pauli-product assignment, every gate is exactly unitary . All 512 scalar sign assignments fail the
magic-square row/column requirements. This is an illustration of the reduction, not a new
nonlocality example.
Exact symbolic checks verify the local stochastic identities, disjoint supports and balancing,
including empty words, one-letter words, repetitions and contradictory relations. Three hundred
complex unitary tests check the gate spectral and logarithmic bounds; two hundred erroneous-
gate controls are detected. These finite checks do not prove an undecidability theorem, establish
novelty , or replace the general proof.
A separate implementation written during the Astra construction review checks 160 ad-
ditional word lists, 360 complex blocks and 48 tests of the two quantitative transfers. Its
Clifford checks verify the size formulas for n = 2 ,..., 10 and 5440 products of normal forms
for n = 2 ,3,4,5. The implementations were written separately , but the review used shared
conversational context; this is not a claim of independent human validation.
The word-problem and nonlocal-game results, finite Clifford representations, and stability
theorem belong to the cited authors. Our claimed contribution is the rational homogeneous
block reduction with simultaneous balancing and logarithmic control, and its consequences for
(1). T argeted searches have not established global priority . Related work on factorizable channels,
unitary correlations and noncommutative optimization may contain equivalent formulations.
Theorem 1 does not imply nonrecursive approximation complexity , fixed-ratio hardness or
one fixed tuple with superpolynomial accuracy growth. Theorem 2 does not imply a constant
separation between yes and no instances. The capacity is easy on all constructed examples; it
is the requested determinant witness that carries the obstruction.
7

Assistance and review status. Developed with substantial OpenAI Codex assistance in
mathematical reasoning, source checking and computational diagnostics. GPT-6 Astra at xhigh
effort was requested for adversarial review of the construction in reused context. Requested
model and effort were not separately attested at runtime. Any exact-version assessment is
recorded separately with the deposited files; no human review, certified model isolation or proof-
assistant verification is claimed.
References
[1] A. Garg, L. Gurvits, R. Oliveira and A. Wigderson, Operator Scaling: Theory and Applica-
tions, F oundations of Computational Mathematics 20 (2020), 223–290. https://doi.org/
10.1007/s10208-019-09417-z .
[2] W. Slofstra, The set of quantum correlations is not closed , F orum of Mathematics, Pi 7
(2019), e1. Numbered references here use arXiv:1703.08618v2 (2017). https://arxiv.org/
abs/1703.08618v2.
[3] W. Slofstra and T. Vidick, Entanglement in non-local games and the hyperlinear pro-
file of groups , Annales Henri Poincaré 19 (2018), 2979–3005. Numbered references use
arXiv:1711.10676v2. https://arxiv.org/abs/1711.10676v2.
[4] W. Slofstra, A group with at least subexponential hyperlinear profile , arXiv:1806.05267v1
(2018), Lemmas 3.1 and 3.4. https://arxiv.org/abs/1806.05267v1.
[5] L. Eriksson, A universal capacity bound for amplified determinants and polynomial witnesses
in the Hermitian case, AIRR working paper, ARR-2026-1DGGW5KX2M9R4VJT, v1 (2026).
https://airr.science/papers/ARR-2026-1DGGW5KX2M9R4VJT/versions/v1/ .
[6] C. Herrmann, Y. T sukamoto and M. Ziegler, Progress on the Computability, Complexity,
and Expressiveness of Geometric Quantum Logic , author-hosted manuscript, Theorem 2(b)–
(d), accessed 17 October 2026. https://www2.mathematik.tu-darmstadt.de/~herrmann/
qex38.pdf.
[7] C. Do-Y an Lee and J. W atrous, Detecting mixed-unitary quantum channels is NP-hard ,
Quantum 4 (2020), 253. https://doi.org/10.22331/q-2020-04-16-253 .
[8] C. Herrmann and M. Ziegler, Computational Complexity of Quantum Satisfiability , Jour-
nal of the ACM 63(2) (2016), Article 19. https://www2.mathematik.tu-darmstadt.de/
~herrmann/X3.pdf.
[9] M. Musat and M. Rørdam, with an appendix by N. Ozawa, Non-closure of quantum
correlation matrices and factorizable channels that require infinite dimensional ancil la ,
arXiv:1806.10242v4 (2019). https://arxiv.org/abs/1806.10242v4.
8