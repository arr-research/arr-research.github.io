# Uniform ten-spin Lorentzian obstructions for cycle clique blowups

Extracted text; the canonical PDF controls mathematical notation.

Uniform ten-spin Lorentzian obstructions
for cycle clique blowups
Lluis Eriksson
Independent researcher, Sweden
17 October 2026
Working-paper manuscript
Abstract
For every m ≥ 4 and s ≥ 2, we construct a strictly positive rational antiferromagnetic
target of rank two on at most ten states whose partition polynomial for Cm[Ks] is not
Lorentzian. The state bound is independent of both parameters; seven states suﬃce when
s ≥ 9, and six suﬃce for even m. The new case is an odd cycle, whose edges are critical
for its independence number and hence fall outside the earlier independence-stable blowup
theorem. We classify the minimum-induced-edge occupations and compress their leading
Hessian kernel to an initial block of at most eight proﬁles. For s ≥ 20, a ﬁve-proﬁle block
has inertia (2, 3, 0), proved by six exact coeﬃcient certiﬁcates in the cycle length, clique
size and central binomial coeﬃcient. Eighteen bounded clique sizes are covered by polyno-
mial certiﬁcates for inﬁnite cycle-length tails and 42 explicit integer exceptions. We retain
failures of smaller blocks and give a positive seven-state witness for C5[K9]. The target
may depend on m, s; neither optimality nor the general connected-source characterization
is claimed.
1 The result and its scope
For a ﬁnite simple graph G = ( V, E) and a symmetric nonnegative q × q matrix K, write
ZG(x; K) =
∑
σ:V →{ 0,...,q− 1}
∏
uv∈E
Kσ(u),σ(v)
∏
v∈V
xσ(v). (1)
We call K antiferromagnetic when it has at most one positive eigenvalue. Inertia is written in
the order positive, negative, zero. The graph Cm[Ks] replaces each vertex of a simple cycle by
a clique of order s, joining all pairs across adjacent classes.
For a homogeneous polynomial with strictly positive coeﬃcients on the full degree simplex,
Lorentzianity is equivalent to every quadratic partial derivative having a Hessian with at most
one positive eigenvalue [ 1, Theorem 2.25]. Positive targets in ( 1) give this full support. Lee–Oh–
Seo proved that clique sources are Lorentzian for every antiferromagnetic target [ 2, Theorem
3.1]. The connected-source converse discussed in [ 3, Section 6] asks whether only cliques have
this property. We address one two-parameter family.
Theorem 1. Let m ≥ 4 and s ≥ 2 be integers. There are q ≤ 10 distinct rational nodes
a0, . . . , aq− 1 ∈ (−1, 1), one of them zero, such that
K = 11⊤ − aa⊤
has inertia (1, 1, q − 2) and ZCm[Ks](x; K) is not Lorentzian. One may take q ≤ 7 if s ≥ 9 and
q = 6 if m is even. The matrix is strictly positive entrywise.
1

The parameters of K may depend on both m and s. Adding distinct nodes in (−1, 1) allows
exactly ten states: the restriction to the old variables preserves the old Hessian obstruction.
Combining the theorem with the clique result gives a characterization within this family.
Corollary 2. For m ≥ 3 and s ≥ 2, the polynomial ZCm[Ks](x; K) is Lorentzian for every
antiferromagnetic target K if and only if m = 3 .
Proof. For m = 3 the source is K3s, so [ 2, Theorem 3.1] applies. Theorem 1 supplies the
converse.
The earlier conditioned-proﬁle method [ 4] and its six-spin reﬁnement [ 5] are inputs, not
new claims here. The latter covers bases F for which α(F − e) = α(F) for every edge. Even
cycles satisfy this hypothesis. An odd cycle C2k+1 does not: deleting any edge gives a path
with independence number k+1, whereas α(C2k+1) = k. Thus the odd case requires a diﬀerent
ground-layer analysis. Each nontrivial clique class also contains maximum-degree true twins,
so the earlier no-maximum-degree-twins criterion does not settle this family.
The contribution is the uniform odd-cycle construction and the bound on its number of
states. Turan equality, generalized Vandermonde invertibility and continuity of inertia are clas-
sical. The homomorphism inequalities for clique blowups in [ 2, 3] concern a diﬀerent assertion
and are not contradicted by a failure of Lorentzianity of the full source partition polynomial.
Our checks of these sources and the preceding manuscripts support this comparison; they do
not establish exhaustive worldwide priority.
2 From an initial proﬁle block to a small target
We give the transfer argument for an arbitrary number of active proﬁles, including the order
of its two limiting operations.
Let n = |V (G)|, 0 ≤ h ≤ n − 2, a0 = ℓ ̸= 0 and a1 = 0 . Put θ = ℓ2. For S ⊆ V (G) of
size h, let rS(v) = |N(v) ∩ S|for v /∈ S. Let νS
r count such vertices of proﬁle r, and let CS
rt
count ordered adjacent pairs of distinct outside vertices with proﬁles r, t. Pad νS by a zero in
coordinate h + 1. The matrix D of size (h + 2) × (h + 1) is given by Der = er − er+1. Deﬁne
Qh(θ) =
∑
|S|=h
(1 − θ)e(G[S])
[
θ{νS(νS)⊤ − diag νS} −DCSD⊤
]
. (2)
With Uir = (1 − ℓai)r, direct diﬀerentiation gives
Hess
(
∂h
0 ∂n− h− 2
1 ZG
)
= h!(n − h − 2)!
θ UQh(θ)U⊤ . (3)
Indeed, ﬁxing the h vertices assigned to the pin spin contributes (1 − θ)e(G[S]). The two
undiﬀerentiated vertices give the proﬁle products, and νν⊤ − diag ν counts all ordered distinct
pairs. The edge correction is aiaj times the ordered edge count; the identity (UD)ir = ℓai(1 −
ℓai)r produces the second term. Edges involving vertices diﬀerentiated in the zero-node spin
have weight one. This also accounts for the factorials, including coincident residual spins.
Set e0 = min |S|=h e(G[S]). The leading kernel is
L = lim
θ↑1
Qh(θ)
(1 − θ)e0
=
∑
|S|=h
e(G[S])=e0
{νS(νS)⊤ − diag νS − DCSD⊤ }. (4)
An index is active if its row in L is nonzero. In particular, activity is not deﬁned just by νr > 0.
2

Lemma 3 (Initial-proﬁle compression) . Suppose the principal submatrix of L on its ﬁrst r
active indices is nonsingular and has at least two positive eigenvalues. Then G has a strictly
positive rational rank-two antiferromagnetic obstruction on r + 2 states.
Proof. Let the ﬁrst active indices be b1 < · · ·< b r. For rational δ > 0, use the r auxiliary
nodes ai+1 = −1 + δi, i = 1 , . . . , r. At ℓ = −1 their proﬁle evaluation matrix has entries (δi)b.
Its columns on the selected indices form
Vδ = W diag(δb1, . . . , δbr ), W ij = ibj .
The matrix W is invertible: a nonzero polynomial with at most r monomials has at most r − 1
distinct positive roots, by Descartes’ rule of signs. For every omitted active index b > b r, the
jth entry of V − 1
δ ((δi)b)i is a constant times δb− bj , and therefore tends to zero. Inactive rows
contribute nothing. Congruencing the auxiliary restriction of ULU ⊤ by V − 1
δ thus gives the
selected block in the limit δ ↓0.
Choose rational δ, with 0 < δ < 1/r, suﬃciently small to retain its inertia. Now ﬁx δ
and put ℓ = −1 + ε with ε ↓ 0. The positive normalization in ( 3) and ( 4) and continuity
retain at least two positive eigenvalues for rational ℓ suﬃciently close to −1. We also impose
0 < ℓ + 1 < δ , so the pin, zero node and auxiliary nodes are distinct. All nodes lie in
(−1, 1), hence Kij = 1 − aiaj > 0. The two vectors 1, a are linearly independent; Sylvester’s
law of inertia gives (1, 1, r) for K. The oﬀending principal Hessian restriction proves non-
Lorentzianity.
No evaluation at a zero-entry boundary target is asserted. The target construction is
terminating in principle by rational search and exact inertia, but no useful denominator bound
is proved.
3 Minimum-edge occupations on an odd cycle
For the rest of the proof put m = 2 k + 1, k ≥ 2, and
n = (2 k + 1)s, h = ks − 1, e 0 = (s − 1)(ks − 2)
2 . (5)
Both derivative orders h and n − h − 2 = ( k + 1)s − 1 are nonnegative.
An occupation vector c = ( c0, . . . , cm− 1) records how many vertices of each clique class
belong to S. Its weight, the number of labelled subsets it represents, is ∏
i
(s
ci
)
.
Lemma 4. The minimum number of edges in an h-vertex induced subgraph of Cm[Ks] is (5).
Every minimizing subgraph is a union of k clique components, one of size s − 1 and the others
of size s. Its occupation is either
1. one component occupying two consecutive cycle classes, with all other components occu-
pying one class and all intervening gaps having length one; or
2. every component occupying one class, with one gap of length two and all other gaps of
length one.
Proof. The independence number of the source is k. Turan’s theorem applied to the complement
of an induced h-vertex graph gives the minimum in ( 5); equality requires k balanced clique
components [ 6]. Selecting full classes of a maximum independent set except for one omitted
vertex attains equality. Since m ≥ 5, a clique component can use at most two consecutive cycle
classes. Diﬀerent components require at least one empty class between them. There are 2k + 1
classes and k components, so at most one component can occupy two classes. If there is one,
all k gaps have length one. If there is none, precisely one gap has length two. These conditions
are also suﬃcient.
3

Here is an exact summation with convenient endpoint corrections. Anchor a possible split
at classes 0, 1 and place the other components at 3, 5, . . . , 2k − 1.
• Type A has occupations (t, s−1−t) at 0, 1 and all other components full, with 0 ≤ t ≤ s−1.
Its weight is
(s
t
)( s
t+1
)
.
• Type B has occupations (t, s − t) at 0, 1, with 0 ≤ t ≤ s, and one of the k − 1 other
components partial of size s − 1. Its weight is s
(s
t
)2.
Take all m rotations. Strict splits occur exactly once. Each unsplit conﬁguration occurs twice
among the endpoints: one can regard either class next to its unique double gap as the degenerate
split. Subtract one copy of all unsplit conﬁgurations. They are the m rotations of the k choices
of a partial class in {0, 2, . . . , 2k − 2}, each with weight s. Thus the number of minimizing
labelled subsets is
N = m
[(
2s
s − 1
)
+ (k − 1)s
(
2s
s
)
− ks
]
. (6)
The signed representation counts a positive combinatorial set exactly once; it does not assign
negative physical weights.
For an occupation deﬁne the remaining class size and its proﬁle by
bi = s − ci, ρ i = ci− 1 + ci + ci+1.
Indices are cyclic. With zero padding as needed, put
ν =
∑
i
bieρi , C =
∑
i
bi(bi − 1)eρi e⊤
ρi +
∑
i
bibi+1(eρi e⊤
ρi+1 + eρi+1e⊤
ρi ).
The occupation contributes its weight times
M(c) = νν⊤ − diag ν − DCD⊤ . (7)
The internal edges of an empty clique class contribute s(s − 1) ordered pairs and must be
retained. Summing ( 7) over the above types and corrections is an explicit formula for L. All
active indices lie between s − 1 and 2s + 1 : the remaining part of a selected component has
proﬁle s − 1 or s, an empty class has proﬁle between s − 1 and 2s, and D shifts upwards by at
most one.
4 Five initial proﬁles for all large clique sizes
Let B =
(2s
s
)
and
A = ( s − 1, s, s + 1, s + 2, s + 3), T = L[A, A]/m.
We describe a ﬁnite symbolic construction of T, rather than ﬁtting its entries from numerical
examples. For a pattern c, let P(c) be the restriction of ( 7) to A, with
P(c) = νAν⊤
A − diag νA −
∑
i
bi(bi − 1)did⊤
i
−
∑
i
bibi+1(did⊤
i+1 + di+1d⊤
i ), d i = ( eρi − eρi+1)|A.
(8)
For a type A pattern, let P◦
A be its generic projected matrix when the two variable boundary
proﬁles lie outside A. The sum over all split parameters is
A = sB
s + 1 P◦
A +
4∑
j=0
(
s
j
)(
s
j + 1
)
(
PA(j) + PA(s − 1 − j) − 2P◦
A
)
. (9)
4

For a type B partial-position category p, the analogous sum is
Bp = sBP ◦
B,p +
4∑
j=0
s
(
s
j
)2(
PB,p(j) + PB,p(s − j) − 2P◦
B,p
)
. (10)
These formulas hold for s ≥ 11. For example, in type A the variable proﬁles are s + t and
2s− 1 − t. In type B they are s+ t and 2s− 1 − t for a nearby partial class, and s+ t and 2s− t
for a distant partial class. For k = 2 the unique partial class touches both boundaries, giving
s + t − 1 and 2s − 1 − t instead. Solving for when either ρ or ρ + 1 enters A puts all exceptions
in the two endpoint lists in ( 9)–(10). For s ≥ 11 these lists are disjoint. The weights outside
them sum by Vandermonde’s identity; the correction sums add the exact weighted diﬀerence
from the generic matrix.
For k ≥ 3 there are two near partial positions and k−3 far positions. The two near positions
have equal summed matrices by reﬂection and t ↔ s − t. For unsplit endpoint patterns there
are two near partial positions and k − 2 far positions. Therefore
T = A + 2Bnear + (k − 3)Bfar − 2sPE,near − (k − 2)sPE,far. (11)
Representatives may be drawn on C9. Extra full components contribute only proﬁle 2s, outside
the projection for s ≥ 11. The local near pattern is valid already at k = 3 ; the absent far B
category has multiplier zero. For k = 2 , compute the A pattern and the single B position on
C5 and subtract its two distinct unsplit endpoint patterns. It is not obtained by substituting
k = 2 into ( 11).
This deﬁnes every entry of the two rational-polynomial matrices in s, k, B. Their expanded
entries and determinant factorizations are in odd-initial-five-symbolic.json. The ﬁrst
row in both branches, with the appropriate value of k, is
(
0, Bks 2, 2ks4, ks4(s − 1)2
2 , ks4(s − 1)2(s − 2)2
18
)
. (12)
All four displayed couplings are positive in the domain used below. There are no lower proﬁles,
so A consists of the ﬁrst ﬁve active indices.
Proposition 5. For every integer s ≥ 20 and k ≥ 2, T has inertia (2, 3, 0).
Proof. Let ∆j be its leading j × j determinant. Exact expansion of ( 8)–(11) gives
∆2 = −B2k2s4 < 0
in both branches, including k = 2 . For ∆3, ∆4, ∆5 the required signs are +, −, −. Here is the
exact ﬁnite certiﬁcate for those signs. Take the numerator of the signed determinant, retaining
its positive constant denominator separately. Factor out only powers of s, s − 1, s − 2, k, B,
which are positive in the domain. Denote the remaining signed polynomial by F. Substitute
B = s8 + w, k = 3 + v, s = 20 + u, (13)
omitting v in the k = 2 branch. Every nonzero coeﬃcient of the resulting six polynomials is
positive, and every constant term is positive. The complete integer coeﬃcient lists are provided,
with the following counts.
Branch ∆3 −∆4 −∆5
k = 2 56 64 80
k ≥ 3 112 196 328
5

These are 836 retained coeﬃcients, not sampled values or rounded eigenvalues. The supplement
reconstructs the matrices, determinants, stripped factors and all coeﬃcients using exact integer
and rational arithmetic.
It remains to justify w > 0 in ( 13). At s = 20 ,
(
40
20
)
− 208 = 112246528820 > 0.
The polynomial (4s + 2) s8 − (s + 1) 9 has strictly positive coeﬃcients in s − 20, as the exact
expansion in the supplement shows. The recurrence B(s + 1) /B(s) = (4 s + 2) /(s + 1) then
proves B(s) > s 8 by induction. Thus all six signed determinants are strictly positive for the
claimed integer parameters.
The initial 2 × 2 block is nonsingular with inertia (1, 1, 0). The subsequent Schur pivots
have signs ∆3/∆2 < 0, ∆4/∆3 < 0 and ∆5/∆4 > 0, proving (2, 3, 0). We do not use the zero
ﬁrst diagonal entry as a scalar pivot.
5 Bounded clique sizes and inﬁnite cycle tails
For 2 ≤ s ≤ 19, a separate exact polynomial certiﬁcate avoids the overlapping endpoints of the
large-s formula. For ﬁxed s, the full matrix L/m is polynomial in k for k ≥ 3. To construct it,
use the same A, B and endpoint categories as before, now retaining all proﬁle coordinates. A
representative on C9 is extended symbolically by
ν2s ↦− →ν2s + (k − 4)s, C 2s,2s ↦− →C2s,2s + (k − 4)s(s − 1). (14)
An additional full component leaves no outside vertices in its class; its following empty class
contributes precisely the vertices and internal ordered edges in ( 14). No other remaining
adjacency or local proﬁle changes. The multipliers of the near and far B categories are 2 and
k − 3; those of the endpoint corrections are 2 and k − 2. Reﬂection identiﬁes the near categories
only after summing over t. At k = 3 the far B term is absent; the other local patterns have
the same formula with one fewer ordinary empty class. This is a combinatorial derivation of a
polynomial matrix, not interpolation. The case k = 2 is evaluated directly.
For each s, take its ﬁrst active r coordinates. The following table gives a certiﬁed block for
the inﬁnite tail k ≥ N, the largest block needed in the ﬁnitely many integers 3 ≤ k < N , and
the size for k = 2 .
s Tail size r N Largest ﬁnite size k = 2 size
2 4 3 – 4
3 5 3 – 4
4 5 8 6 5
5 6 3 – 5
6 7 3 – 6
7 6 40 8 6
8 6 3 – 6
9–19 5 3 – 5
For each row, the determinant of the indicated initial block is a nonzero polynomial
ds(k). Its leading sign ηs ∈ {− 1, 1} is chosen so that every coeﬃcient of ηsds(N + u) is
nonnegative and its constant coeﬃcient is positive. These complete coeﬃcient lists are in
odd-initial-small-certificates.json. Hence the block is nonsingular throughout the real
interval [N, ∞ ). Exact symmetric elimination at N gives at least two positive eigenvalues.
6

Since inertia cannot change along a continuous nonsingular real symmetric family, that iner-
tia persists throughout the interval. The polynomial continuation at nonintegral k need not
represent a graph.
There are exactly 42 exceptional integers before the thresholds: k = 3 , . . . , 7 for s = 4 and
k = 3 , . . . , 39 for s = 7 . Each is certiﬁed by rational congruence, as are all eighteen k = 2 cases.
The table therefore covers every k ≥ 2 for each 2 ≤ s ≤ 19. The size never exceeds eight, and
is ﬁve throughout 9 ≤ s ≤ 19.
These exceptional block sizes are substantive. For s = 7 and 6 ≤ k ≤ 24, the initial seven-
proﬁle block has inertia (1, 6, 0), whereas the initial eight-proﬁle block has inertia (2, 6, 0). For
s = 4 and k = 3 , 4, 5, the ﬁve-proﬁle block also fails and the six-proﬁle block works. This does
not prove a lower bound on the number of target states for other constructions.
Proof of Theorem 1. If m is even, deleting an edge of Cm leaves its independence number
unchanged. The six-state theorem of [ 5] applies. For odd m = 2 k + 1, Lemma 4 and ( 7) give
the exact leading kernel. Proposition 5 and the bounded-size certiﬁcates produce a nonsingular
initial block with at least two positive eigenvalues, of size at most eight for every s ≥ 2 and of
size ﬁve for every s ≥ 9. Lemma 3 supplies at most ten and seven states, respectively.
6 An exact positive target and reproducible evidence
For C5[K9], take seven nodes
a =
(
− 4095
4096, 0, − 15
16, − 7
8, − 13
16, − 3
4, − 11
16
)
. (15)
The target K = 11⊤ − aa⊤ is strictly positive and has inertia (1, 1, 5). For h = 17 , the
restriction to the ﬁve auxiliary variables of
Hess(∂17
0 ∂26
1 ZC5[K9])
has inertia (2, 3, 0). This is a full ﬁnite-parameter computation using all 4335 occupation vectors
of total size 17, rather than just the leading layer. The supplementary certiﬁcate retains the
rational target, scaled integer Hessian, positive normalization and rational elimination pivots.
It is possible to check its inertia without any ﬂoating-point spectral calculation.
The pin value matters. With the same auxiliary nodes, the earlier trial ℓ = −255/256 gives
auxiliary inertia (1, 4, 0) and fails to certify the desired obstruction. That failed trial is retained.
Likewise, a prior noninitial four-proﬁle choice fails at (k, s) = (3 , 6); the initial seven-proﬁle
block used here succeeds. Neither failed trial is silently discarded from the reproducibility
record.
The supplement contains the classiﬁed-pattern kernel, symbolic ﬁve-proﬁle construction,
large-size coeﬃcient certiﬁcates, bounded-size tail and exception certiﬁcates, exact inertia rou-
tine and an executable veriﬁer. The veriﬁer checks identities and sign coeﬃcients rather than
trusting stored PASS labels. Source-audit reports and their independently written code are kept
separately from the author computations. The source audit reconstructed the six large-size cer-
tiﬁcates, their 836 positive coeﬃcients, all 42 exceptional integers and the positive target ( 15).
Its further ﬁnite cross-checks corroborate the classiﬁcation; the proof of the inﬁnite parameter
ranges is the symbolic argument above.
All exact certiﬁcates are supplementary parts of this argument. They do not amount to a
proof-assistant formalization. The ﬁnite census of other bases from earlier work is not used to
extrapolate the present theorem. The original failed trials and separate audit outputs remain
preserved.
7

7 Limitations and further questions
The theorem concerns uniform cycle clique blowups. It does not establish the general connected-
source conjecture, unequal clique sizes, an optimal state bound, a ﬁxed target for the entire
family, or a useful uniform denominator bound. The restriction s ≥ 2 is the domain of the
present occupation argument; no statement about s = 1 is inferred from its formulas.
The proof separates two diﬃculties: ﬁnding an initial proﬁle block with two positive eigen-
values and realizing it with a bounded number of spins. For odd cycles, the total number
of possible proﬁles grows with s, but ﬁve initial proﬁles suﬃce once s ≥ 9. An arbitrary
later principal minor would not alone justify this state bound. The eight-proﬁle exceptions at
s = 7 suggest a speciﬁc optimization problem, but their inertia does not exclude more eﬃcient
auxiliary-node choices.
Assistance and assessment. OpenAI Codex assisted with the proofs, writing and exact
computation. The author operates AIRR. The source argument received a GPT-6 Astra tech-
nical audit, requested at eﬀort xhigh; it found no unresolved material mathematical objection
within the stated scope. That source audit is not an exact-version manuscript score. Any sub-
sequent assessment must identify the ﬁnal PDF hash. Prior model participation is disclosed;
runtime identity and technical context isolation are not independently attested. No human
peer review, formal veriﬁcation or worldwide-priority certiﬁcate is claimed.
References
[1] P. Brändén and J. Huh. Lorentzian polynomials. Annals of Mathematics 192 (2020), 821–
891. arXiv:1902.03719.
[2] J. Lee, J. Oh and J. Seo. Counting homomorphisms in antiferromagnetic graphs via
Lorentzian polynomials. arXiv:2506.13659, version 2.
[3] J. Lee and J. Seo. Antiferromagnetic models are clique-minimizing . arXiv:2608.17920, ver-
sion 1.
[4] L. Eriksson. Rank-two obstructions to Lorentzian graph partition functions . AIRR, ARR-
2026-7993ZVQWNC9E38P2, version 1, 17 October 2026. Permanent record. Working paper.
[5] L. Eriksson. Six-spin Lorentzian obstructions for clique blowups of independence-stable
graphs. AIRR, ARR-2026-0VEP5BTYB99VNSC0, version 1, 17 October 2026. Version
record. Working paper.
[6] P. Turán. On an extremal problem in graph theory (in Hungarian). Matematikai és Fizikai
Lapok 48 (1941), 436–452.
8