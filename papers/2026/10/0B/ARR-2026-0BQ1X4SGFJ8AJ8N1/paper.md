# Rigidity and strongly polynomial equality tests for unimodular fiber counts

Machine-readable extraction of the canonical six-page PDF. Mathematical layout is governed by paper.pdf, SHA256 7fee08dcca98b04bad1208d28957f56391acc137a9d90fd95a25b32dba536593.

Rigidity and strongly polynomial equality tests
for unimodular ﬁber counts
Lluis Eriksson
27 October 2026
Abstract
Leake and Mohammadi Yekta proved coeﬃcientwise midpoint log-concavity for lattice-
point enumerators of unimodular box ﬁbers. We characterize its equality cases. For three
nonempty ﬁbers in one integer coordinate box, equality at one positive external ﬁeld
is equivalent to symmetric integral translation of the three real ﬁber polytopes. Thus
equality is independent of the ﬁeld, and unweighted equality forces all three counts to
coincide. The proof uses a squarefreeness lemma for the complete lattice-point enumerator
of any lattice polytope. More generally, a product of k such enumerators can be the k-th
power of another only when their polytopes are integral translates with shifts summing
to zero. Coordinate extrema yield an equality test using 6n linear optimizations and no
lattice-point enumeration. Basis normalization and Tardos’s algorithm give a strongly
polynomial number of arithmetic operations under the integer-box promise. We explain
the rational-box boundary, strictness consequences and a weighted realization obstruction.
No global Jensen inequality is established.
1
Setting and dependence on prior work
Let M ∈Zr×n have full row rank, with every nonzero maximal minor equal to +1 or −1. This
is the rectangular unimodular convention used here. Fix ﬁnite integer bounds ℓ, u ∈Zn and
deﬁne
Pb = {x ∈Rn : Mx = b, ℓ≤x ≤u},
Fb(z) =
∑
x∈Pb∩Zn
zx.
Vector inequalities are coordinatewise; exponents may be negative. We use the ring
Ln = C[z±1
1 , . . . , z±1
n ].
An external ﬁeld is w ∈Rn
>0.
For integral b−+ b+ = 2b0, the essential input is Leake–Mohammadi Yekta [1, Theorem
3.1]:
D(z) = Fb0(z)2 −Fb−(z)Fb+(z)
has nonnegative coeﬃcients.
(1)
Their Lemma 3.4 gives integrality of these box ﬁbers. We use their coeﬃcientwise theorem
directly, not a new proof of that inequality. Equality is distinct from their open global Jensen
question [1, Question 1.7].
The proposed additions are an equality characterization, its reduction to linear optimiza-
tion and the supporting enumerator lemma. Bounded source comparison does not certify
worldwide priority. Csikvári–Imolay [3] already study equality between Eulerian orientation
and half-graph counts; their pair-decomposition methods are antecedents of the source ar-
gument.
That comparison concerns diﬀerent combinatorial objects rather than the three
ﬁxed-matrix ﬁbers here. Tardos’s algorithm [2] is an existing optimization tool.
1


2
Squarefreeness and multiplicative rigidity
For a nonempty lattice polytope P, let EP (z) = ∑
a∈P∩Zn za. All lattice points, including
boundary points, occur with coeﬃcient one. Squarefree means no repeated nonunit irreducible
factor in Ln. Laurent monomials are units.
Lemma 2.1. If polytopes Q, R are given and e is an edge of Q, there is a functional v such
that Qv = e, Rv is a vertex or an edge parallel to e, and (2Q + R)v is an edge. Superscripts
denote maximizing faces.
Proof. Work in the direction space of Q + R, of dimension d, translating the summands. The
normal cone of e has dimension d −1. Choose v in its relative interior. Exclude normal cones
of faces of R of dimension at least two; they have dimension at most d −2. Also exclude
intersections with normal cones of edges f not parallel to e: these lie in e⊥∩f⊥, again of
dimension at most d −2. Finitely many such sets cannot cover the relative interior of the
edge cone. The remaining face Rv is a vertex or a parallel edge. Maximizing faces commute
with Minkowski addition. For d = 1, use the zero functional: the nonpoint summands are
parallel segments. Passing to the direction space removes common normal lineality and covers
lower-dimensional polytopes.
Theorem 2.2. The complete lattice-point enumerator EP of any nonempty lattice polytope
is squarefree in Ln.
Proof. A point gives a unit. Suppose otherwise that EP = G2H, with G a nonunit Laurent
polynomial. Newton polytopes satisfy P = 2Q + R, where Q = Newt(G) and R = Newt(H).
The nonunit G has at least two exponent vectors, so Q has an edge e. Lemma 2.1 gives a
functional whose face in P is the edge 2e + Rv. Let a be an endpoint and q ∈Zn its primitive
integer direction. The lattice points of that edge are exactly a, a+q, . . . , a+mq for an integer
m ≥1. Its face polynomial is
inv(EP ) = za(1 + t + · · · + tm),
t = zq.
Face products also give inv(EP ) = inv(G)2 inv(H). Up to a Laurent monomial, inv(G) is a
nonconstant polynomial g(t) with nonzero constant coeﬃcient: its edge endpoint terms are
present.
Thus g(t)2 divides 1 + t + · · · + tm in C[t±1].
But (tm+1 −1)/(t −1) has only
simple nonzero roots in characteristic zero, a contradiction. The primitive direction makes
the univariate edge Laurent representation injective.
Both complete support and coeﬃcient one matter. For instance,
1 + x + x3 + x4 = (1 + x)2(1 −x + x2)
omits the lattice point 2 of its Newton segment and has a repeated factor, despite having only
zero or one coeﬃcients. The full-support polynomial (1+x)2 instead has a nonunit coeﬃcient.
Theorem 2.2 is not a statement about Ehrhart or h∗-polynomials.
Theorem 2.3 (Multiplicative rigidity). For nonempty lattice polytopes P1, . . . , Pk, Q and
k ≥2,
k
∏
i=1
EPi = Ek
Q
if and only if Pi = Q + hi for integral vectors hi with ∑
i hi = 0.
2


Proof. The Laurent ring is a unique factorization domain. Every irreducible factor of EQ has
multiplicity k on the right. Each of the k squarefree enumerators on the left contributes at
most once, so every one contributes once. No other factor can appear. Hence EPi = cizhiEQ.
Coeﬃcient one forces ci = 1. Supports and then convex hulls give Pi = Q + hi; cancellation
gives ∑
i hi = 0. Monomial enumerators cause no exception. The converse follows directly
from translation.
3
The equality characterization
Theorem 3.1. In the setting of Section 1, suppose the three ﬁbers are nonempty. The fol-
lowing are equivalent:
1. Fb0(w)2 = Fb−(w)Fb+(w) for some w ∈Rn
>0;
2. F 2
b0 = Fb−Fb+ as Laurent polynomials;
3. for an h ∈Zn, Pb+ = Pb0 + h and Pb−= Pb0 −h.
Equality therefore holds at every positive ﬁeld or the inequality is strict at every positive ﬁeld.
Proof. A nonzero Laurent polynomial with nonnegative coeﬃcients evaluates positively at
every positive ﬁeld. Thus (1) proves 1 ⇒2.
Each box ﬁber is a lattice polytope. Indeed, at a vertex select n −r independent active
coordinate constraints complementary to the row equations. These coordinates are at integer
bounds. The remaining coordinates solve a system with a nonsingular r-column submatrix of
M, of determinant ±1; they are integers. Boundedness now gives Pb = conv(Pb ∩Zn).
Apply Theorem 2.3 with k = 2 to obtain 2 ⇒3. Translations give the polynomial identity
and equality at every positive ﬁeld. If equality fails, the nonzero defect in (1) is positive at
every such ﬁeld.
Corollary 3.2. Unweighted equality for three nonempty ﬁbers forces their three lattice-point
counts to be equal.
Proof. Use Theorem 3.1 at w = 1; integral translation preserves lattice-point counts.
Thus a nonconstant geometric progression of three counts cannot be an equality case.
Positive ﬁelds are essential: zero coordinate weights can erase a nonzero coeﬃcient defect.
Equality need not mean singleton ﬁbers. For M = [1 0], box [0, 2]2, and RHS 0, 1, 2, each
ﬁber has three lattice points and Fb(z) = zb
1(1 + z2 + z2
2). The ﬁbers are symmetric translates,
so equality holds in every positive ﬁeld; the three weighted values need not themselves coincide.
4
An equality algorithm using linear optimization
Let ms,i and Us,i be the minimum and maximum of coordinate i on Pbs, for s = −, 0, +. These
extrema are integers.
Theorem 4.1. Equality can be decided by 6n linear optimizations without evaluating any
lattice-point count. Set h = m+ −m0. The decision is equality precisely when
Mh = b+ −b0,
U+ = U0 + h,
m−= m0 −h,
U−= U0 −h.
(2)
Under the integer-input and nonempty-unimodular promises above, the decision admits a
strongly polynomial number of rational arithmetic operations, with intermediate encoding
lengths polynomial in total input length.
3


Proof. The eﬀective bounds describe each ﬁber exactly:
Pbs = {x : Mx = bs, ms ≤x ≤Us}.
One inclusion is the deﬁnition of the extrema; the other uses ms ≥ℓand Us ≤u. Translation
must shift every minimum and maximum by the same vector, uniquely ﬁxing h = m+ −m0.
The exact eﬀective-box descriptions show that (2) is necessary and suﬃcient for the two
symmetric translations. Here b−−b0 = −(b+ −b0). Apply Theorem 3.1.
For the complexity bound select a nonsingular column basis B of M. By Cramer’s rule
every entry of A = B−1M is in {0, ±1}: each numerator is a maximal minor and det B =
±1.
Basis selection, inversion and RHS transformation take polynomially many rational
arithmetic operations with polynomial intermediate encoding lengths.
Replace Mx = bs
by Ax = B−1bs. The inequality matrix [A; −A; I; −I] has constant-sized entries. Tardos’s
theorem [2] bounds the number of arithmetic operations polynomially in this matrix’s encoding
length, independently of the RHS and objective encodings. That length is polynomial in r, n.
Apply it to the 6n coordinate optimizations and then perform the tests. This is the strongly
polynomial arithmetic model, not a bit-time claim independent of input lengths.
The ﬁeld w need not be an algorithm input: the decision applies simultaneously to all
positive ﬁelds. We promise nonempty ﬁbers and unimodularity rather than claiming a new
recognition algorithm. Standard exact primal–dual LP certiﬁcates can verify the extrema
and comparisons without enumerating lattice points or expanding the defect polynomial. The
ﬁnite controls below do not implement Tardos’s algorithm.
5
Strictness and the boundary of the hypotheses
Corollary 5.1. For an integer box with ui −ℓi ≤1, distinct feasible endpoint right-hand sides
with integral midpoint have strict midpoint inequality at every positive ﬁeld.
Proof. Equality would provide an integer central point x and an integral h with x−h, x, x+h
all in the same box. Thus 2|hi| ≤1, forcing h = 0 and equal endpoint right-hand sides.
Corollary 5.2. Let P = {x ≥0 : Mx = b} be nonempty and bounded for integral b and
full-row-rank unimodular M. If d = dim P > 0, then for all integers t ≥1,
|tP ∩Zn|2 > |(t −1)P ∩Zn| |(t + 1)P ∩Zn|.
For a point P, all these counts are one.
Proof. Boundedness and nonemptiness make the nonnegative recession cone {x ≥0 : Mx = 0}
equal to {0}. Hence the ﬁber at RHS tb is tP, also for t = 0. For any ﬁxed t, choose a common
ﬁnite integer box containing the three scaled polytopes. Equality would make tP and (t+1)P
translates by Theorem 3.1.
Their relative volumes are td and (t + 1)d times the positive
relative volume of P, which diﬀer when d > 0. Integrality handles the point case. The weak
inequality is already [1, Corollary 3.5].
The translation claim is false for arbitrary rational real ﬁbers. Take M = [1 1], bounds
0 ≤x ≤1/2, 0 ≤y ≤2, and RHS 0, 1, 2.
The integer-point enumerators are 1, zy, z2
y,
satisfying equality identically. The ﬁrst real ﬁber is a point; the other two are segments. They
cannot be symmetric translates. This counterexample arose in component review and refutes
an ambiguous rational-input extension in our original memo.
For ﬁnite rational bounds a diﬀerent, valid interface is to round them ﬁrst to ⌈ℓ⌉, ⌊u⌋.
Integer-point sets are unchanged, and the theorem concerns the rounded ﬁbers, not the original
4


real ones. Use feasibility LPs to handle empty rounded ﬁbers. If the central ﬁber is empty,
both endpoints cannot be nonempty: their average would make the integral central polytope
nonempty.
Equality is then 0 = 0. If the center is nonempty and an endpoint is empty,
the inequality is strict. Otherwise use Theorem 4.1. This gives a polynomial bit-complexity
decision for ﬁnite rational boxes. Rational rounding is not included in our strongly polynomial
arithmetic assertion for integer input.
6
A variable-wise log-concave array excluded by rigidity
Deﬁne f on {−1, 0, 1}2, with rows indexed by the ﬁrst coordinate, by
(f(i, j)) =


6/5
5/6
1/10
5/6
1
6/5
1/10
6/5
5/6

,
p(x, y) =
1
∑
i,j=−1
f(i, j)xiyj.
It satisﬁes variable-wise log-concavity [1, Deﬁnition 2.1]. Each coeﬃcient slice is log-concave
without internal zeros. After y = t > 0, let A−, A0, A+ be the three coeﬃcients in x. Exactly,
900t2(A2
0 −A−A+) = 517 + 129t + 891t2 + 1427t3 + 1221t4 > 0.
Symmetry handles evaluations of x; extractions outside the support are zero, as allowed by
the source convention.
The points v1 = (−1, −1), v2 = (1, 0), v3 = (0, 1) have mean zero and coeﬃcients 6/5 >
f(0) = 1. Thus this class alone does not imply global Jensen. The distinction between line
and global concavity is already explicit in [1]; that distinction is not a new discovery claimed
here.
Proposition 6.1. The exact array cannot be the weighted counts at one positive ﬁeld of a
single ﬁxed integer-box unimodular family whose right-hand sides depend aﬃnely on the two
array indices, even after common positive scaling and exponential output rescaling.
Proof. For each i, f(vi)f(−vi) = f(0)2 = 1. Theorem 3.1 would therefore give Pvi = P0 + hi
and P−vi = P0 −hi for integral shifts. The RHS parametrization may be aﬃne, with auxiliary
RHS coordinates ﬁxed; it must preserve the indicated barycenters.
By convexity of the common box and linearity of the constraints,
Pv1 + Pv2 + Pv3
3
= P0 + h1 + h2 + h3
3
⊆P0.
A bounded nonempty polytope cannot contain a nonzero translate of itself: maximize the
functional in that translation direction.
Thus ∑
i hi = 0. The corresponding enumerator
translations imply ∏
i Fvi(w) = F0(w)3, contradicting (6/5)3 > 1.
Common scaling and
exponential output rescaling cancel at these barycenters.
This excludes the exact array, not nearby strictly perturbed arrays, and does not answer
the global Jensen question for unimodular ﬁbers.
7
Controls, review context and limitations
Six explicitly supplied unimodular matrices, in boxes of widths one, two and three, gave 1,160
nontrivial midpoint triples. All nonzero maximal minors were checked. Polynomial equality,
symmetric support translation and the extrema criterion agreed in all cases, including 72
equalities. All coeﬃcient defects were nonnegative. These ﬁnite enumerations are controls,
not a general proof or an LP implementation.
5


A separate exact rational-polynomial check covered all 213 distinct lattice polytopes with
vertices in {0, 1, 2}2: nine points, 36 segments and 168 polygons. After clearing monomial
units, the gcd with the two partial derivatives was constant in every case. The nonsaturated
negative control 1+x+x3+x4 gave gcd x+1 with its derivative. This supplies ﬁnite arithmetic
checks, not higher-dimensional or proof-assistant veriﬁcation.
Model assessments and review context
Component audit822 examined the rational-array calculation with Fraction and integer repli-
cations. It supported the class-membership and arithmetic claims, supplied no unimodular
realization and assigned no score. Component audit824 supported the squarefreeness, integer-
box equality and precise nonrealization arguments in the frozen proof memo, and separately
supported multiplicative rigidity and the reduction to Tardos. It required an explicit integer-
box restriction and refuted the extension to original rational real ﬁbers. That objection and
the corrected hypotheses are preserved above. The rounded rational-box interface, the strict
Ehrhart corollary and the 213-polytope control were not in that component audit’s scope;
they require examination in full-manuscript review. No importance score is assigned here. A
full assessment must refer to the exact PDF and accompany its full report and context; a
component audit cannot be relabeled as that assessment. At the time this version was frozen,
no full-manuscript assessment had yet been obtained.
AI and responsibility disclosure.
The named author directed substantial OpenAI Codex
assistance in derivation, writing and numerical work. GPT-6 Astra xhigh was requested for
the component audits. The reviewer reused prior context and a shared ﬁlesystem; eﬀective
runtime identity, eﬀort and independence are not independently attested. No runtime isola-
tion, independent human peer review, Lean formalization, certiﬁed worldwide originality or
predicted assessment score is claimed. Responsibility remains with the named author.
Limits.
The coeﬃcientwise midpoint inequality is a cited input. Our algorithm does not
count general ﬁbers or produce a ﬁxed positive numerical gap uniform over unbounded ﬁelds.
No solution of global Jensen is claimed. Strong polynomiality is an arithmetic operation bound
under integer-box promises, with input-dependent bit costs.
Signiﬁcance and antecedent
overlap require full-manuscript review.
References
[1] J. Leake and M. Mohammadi Yekta, Log-concavity and Approximate Counting for To-
tally Unimodular Polytopes, arXiv:2609.39917v1 (30 September 2026). https://arxiv.
org/html/2609.39917v1.
[2] É. Tardos, A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs,
Operations Research 34(2) (1986),250–256. doi:10.1287/opre.34.2.250.
[3] P. Csikvári and A. Imolay, Covers, orientations and factors, Electronic Journal of Com-
binatorics 27(3) (2020), Paper 3.25; arXiv:1905.06678v5. https://arxiv.org/abs/1905.
06678v5.
6
