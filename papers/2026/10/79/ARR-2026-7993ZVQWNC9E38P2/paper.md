# Rank-two obstructions to Lorentzian graph partition functions

Extracted text; equations are authoritative in paper.pdf.

Rank-two obstructions to Lorentzian
graph partition functions
Lluis Eriksson
Independent researcher, Sweden
17 October 2026
Research draft
Abstract
We give rank-two antiferromagnetic obstructions to the Lorentzian property of graph
partition functions. A connected noncomplete source of maximum degree ∆ has a strictly
positive rational obstruction on ∆ + 1 spins whenever no two maximum-degree vertices
have equal closed neighbourhoods. Consequently, the connected-source characterization
holds for graphs without true twins, graphs with a unique maximum-degree vertex, and all
connected edge-regular graphs, including strongly regular graphs. The proof uses a small-
parameter limit of explicit conditioned-set Hessian kernels. A diﬀerent endpoint yields a
neighbourhood-independence-gap criterion. One ﬁxed nonnegative four-spin matrix char-
acterizes cliques among connected diamond-free sources and among connected complete
multipartite sources. A ﬁxed ﬁve-spin matrix does the same for joins of a nonempty clique
with disjoint nonempty cliques. Positive rational perturbations exist for each source, but
may depend on it; for triangle-free sources a single strictly positive three-spin matrix
suﬃces. Further obstructions use degree-class adjacency and triangle counts. Exact ra-
tional certiﬁcates cover all 989 connected noncliques of orders three through seven. The
maximum-degree theorem has 821 exact checks, including 819 direct partition-coeﬃcient
comparisons. An explicit ten-vertex graph proves that the small-parameter criterion alone
is incomplete, while the full hierarchy detects it. These results are partial progress toward
the connected-source conjecture of Lee–Oh–Seo; the conjecture and completeness of the
full hierarchy remain unproved.
1. Problem and scope
For a ﬁnite simple graph G = ( V, E) and an entrywise nonnegative symmetric q × q matrix H,
write
ZG(x; H) =
∑
σ:V →{0,...,q−1}
∏
uv∈E
Hσ(u),σ(v)
∏
v∈V
xσ(v). (1)
It is homogeneous of degree n = |V |. We call H antiferromagnetic when it has at most one
positive eigenvalue, counting multiplicity. This is the spectral convention used in [ 2, 3].
Lee–Oh–Seo prove that ZG is Lorentzian for every antiferromagnetic H when G is a clique
[2, Theorem 3.1]. They conjecture a converse; the connected-source formulation is stated
explicitly in [ 3, Section 6]. We use that formulation:
If G is connected and ZG(x; H) is Lorentzian for every antiferromagnetic H, must
G be a clique?
The restriction to connected graphs matters, since partition functions factor over components
and Lorentzian polynomials are closed under products. The present paper establishes obstruc-
tions for several classes of source graphs, using only matrices of rank two.
1

These questions concern all antiferromagnetic targets, rather than only proper-colouring
targets. Matherne–Morales–Selover establish Lorentzianity of chromatic symmetric functions
for abelian Dyck paths [ 4, Theorem 1.5]. Lee–Oh–Seo already give a non-Lorentzian three-
vertex-path example with target
( 0 0 1
0 0 2
1 2 0
)
, as well as a K3,3 example [ 2, Section 7]. We do not
claim those small obstructions as new. A research note by Zeng [ 5] gives a ﬁxed rank-three,
three-spin obstruction for bistable bipartite graphs with a two-vertex cut. Our triangle-free
result uses a strictly positive rank-two target and requires neither bistability nor a two-vertex
cut; it does not claim Zeng’s coeﬃcient formula relating the obstruction to vertex connectivity.
Our proposed contributions are a maximum-degree criterion excluding true twins at that
degree (Theorem 14), the resulting obstructions for all connected noncomplete edge-regular
graphs, and ﬁxed targets for triangle-free, connected diamond-free and complete multipartite
sources, a ﬁxed ﬁve-spin target for joins of a clique with disjoint cliques, the neighbourhood-
independence-gap criterion, the degree-count identity and its compression certiﬁcate, and the
parameterized conditioned-set identities below. A diamond means an induced copy of K4
with one edge removed. The four-spin target for this class has one zero entry; the positive
perturbations are allowed to depend on the source graph.
The arguments are elementary counting and real symmetric linear algebra. Their com-
putational corroboration uses exact arithmetic. A targeted prior-art search does not certify
worldwide priority; a separate referee assessment of this draft remains pending.
2. A rank-two family and the Hessian test
We use a necessary consequence of the deﬁnition of Lorentzian polynomials [ 1]. If a homoge-
neous polynomial f of degree n ≥ 2 with nonnegative coeﬃcients is Lorentzian, then
Hess(∂αf) has at most one positive eigenvalue for every α ∈ Nq
0, |α| = n − 2. (2)
The derivative is quadratic, so its Hessian is constant. We need only this necessary condition
for the general obstructions. For the ﬁnite ﬁxed-target limits reported below, we also use
the full characterization: nonnegative homogeneous polynomials with M-convex support are
Lorentzian precisely when all these quadratic derivatives satisfy the Hessian condition [ 1,
Theorem 2.25].
Lemma 1. For a nonconstant vector t ∈ (0, ∞)q, the matrix
H(t)ij = ti + tj (3)
is positive entrywise and has inertia (1, 1, q −2), where inertia lists positive, negative and zero
eigenvalues.
Proof. Write H = 1t⊤+t1⊤. Its rank is at most two, and its quadratic form vanishes on 1⊥. A
positive deﬁnite two-dimensional subspace would intersect 1⊥ nontrivially, which is impossible.
For ti ̸= tj, the corresponding principal determinant is 4titj − (ti + tj)2 = −(ti − tj)2 < 0.
Thus there are a positive and a negative eigenvalue, and rank is exactly two.
For integer r ≥ 0, introduce
zi = 1 + ti
2 , k i = ti − 1
ti + 1 , k izr
i = zr
i − zr−1
i (r ≥ 1). (4)
A baseline spin of value t = 1 has self-interaction 2. If two free vertices are adjacent, the
correction to their separate baseline changes is
2(ti + tj)
(1 + ti)(1 + tj) = 1 − kikj. (5)
All denominators in these identities are positive.
2

3. A ﬁxed target for all triangle-free sources
It is useful to normalize the interaction with the baseline spin. For distinct ai ∈ (−1, 1), set
K(a) = 11⊤ − aa⊤, K ij = 1 − aiaj. (6)
This matrix is positive entrywise and has rank two and exactly one positive eigenvalue. Indeed,
its quadratic form is nonpositive on 1⊥, and a principal 2 × 2 determinant for ai ̸= aj equals
−(ai − aj)2 < 0.
For a graph with n ≥ 3 vertices, m edges, degrees dv and T triangles, abbreviate
N = n(n − 1)(n − 2), E = 2 m(n − 2), W =
∑
v
dv(dv − 1), U = 6 T. (7)
Here W counts ordered wedges, including those inside triangles. Use a = ( ℓ, 0, 1/2), with
−1 < ℓ < 0, and let Vi· = (1 , ai, a2
i ).
Theorem 2 (Edge–wedge–triangle identity) . For every ﬁnite simple graph G on n ≥ 3 ver-
tices,
Hess
(
∂0∂ n−3
1 ZG(x; K(a))
)
= ( n − 3)! V ˆBℓV ⊤, (8)
ˆBℓ =


N −ℓE 0
−ℓE ℓ 2W − E ℓW
0 ℓW −ℓ2U

, (9)
det ˆBℓ = ℓ2[
N(EU − W2) + ℓ2U(E2 − NW )
]
. (10)
If W2 > EU , a positive rank-two three-spin target makes ZG non-Lorentzian.
Proof. Place the conditioned spin 0 at v and baseline spin 1, with a1 = 0 , everywhere else.
Every initial edge weight is one. After assigning free spins i, j to distinct vertices u, w ̸= v,
the exact edge product is
(1 − ℓaiAuv)(1 − ℓajAvw)(1 − aiajAuw).
Summing over ordered distinct triples gives counts N for the constant term, E for every
single-edge indicator, W for each two-edge product, and U for the three-edge product. This
is exactly V ˆBℓV ⊤. The derivative multiplicity is (n − 3)!. Expanding the 3 × 3 determinant
proves ( 10).
If A∗ = N(W2 − EU ) > 0 and R∗ = U(E2 − NW ), choose L = 2 + ⌈max(R∗, 0)/A∗⌉ and
ℓ = −1/L. Then ℓ2R∗ < A∗, so the determinant is negative. The entry ( ˆBℓ)00 = N is positive,
and hence its inertia is (2, 1, 0). The Vandermonde matrix V is invertible, so ( 2) proves the
conclusion.
Corollary 3 (One ﬁxed positive target) . Let
K∗ = 1
4


3 4 5
4 4 4
5 4 3

. (11)
For a triangle-free ﬁnite simple graph G, ZG(x; K∗) is Lorentzian if and only if every compo-
nent of G is an isolated vertex or a single edge. In particular, every connected triangle-free
graph on at least three vertices fails the universal-target property.
3

Proof. The target is K(−1/2, 0, 1/2) and has eigenvalues 3, −1/2, 0. If G contains two adjacent
edges, then n ≥ 3, W > 0 and U = 0 . Thus ( 10) becomes −NW 2/4 < 0, proving the
obstruction for this ﬁxed target. Otherwise every component is a vertex or an edge. Their
partition functions are respectively a nonnegative linear form and a quadratic form with
Hessian 2K∗. They are Lorentzian, as is their product [ 1, Corollary 2.32]. The empty graph,
if allowed, contributes the constant one.
For a regular graph, E = nd(n−2), W = nd(d−1) and U = nτ; the inequality W2 > EU
is exactly ( 22) below. The general inequality also applies to irregular graphs with triangles.
4. The degree-count kernel
Let m = |E|, let dv denote vertex degree, and let ∆ = max v dv ≥ 2. For 0 ≤ r ≤ ∆, let
νr = |{v : dv = r}|, and put ν = ( ν0, . . . , ν∆)⊤. For 1 ≤ r, s ≤ ∆, let
Crs = |{(u, v) : uv ∈ E , d u = r, d v = s}|. (12)
These are ordered edge counts; in particular an edge inside a degree class contributes two to
its diagonal entry. Let e0, . . . , e∆ be the standard basis, and let L be the (∆ + 1) × ∆ matrix
with column Lr = er − er−1 for 1 ≤ r ≤ ∆. Deﬁne the symmetric integer matrix
BG = νν⊤ − diag(ν) − LCL⊤. (13)
Theorem 4(Degree-count identity). Take q = ∆+1 , ti = i+1 for 0 ≤ i ≤ ∆, and H = H(t).
With Vir = zr
i , one has
Hess
(
∂ n−2
0 ZG(x; H)
)
= ( n − 2)! 2m V BGV ⊤. (14)
The matrix V is invertible. Consequently, two positive eigenvalues of BG certify that ZG(x; H)
is not Lorentzian.
Proof. The (i, j) entry of the Hessian is (n − 2)! times a sum over ordered distinct vertices
(u, v), giving them spins i, j and every other vertex the baseline spin 0, whose value is t0 = 1 .
This interpretation is valid even if a free spin equals the baseline or the two free spins agree:
ordered placements give precisely the falling-factorial multiplicities of diﬀerentiation.
The baseline edge product is 2m. Changing the two free vertices separately gives zdu
i zdv
j ;
if uv ∈ E , ( 5) supplies the correction. After dividing by (n − 2)!2m, the Hessian entry is
therefore ∑
u̸=v
zdu
i zdv
j −
∑
(u,v):uv∈E
kizdu
i kjzdv
j .
The ﬁrst sum is the (i, j) entry of V (νν⊤ − diag(ν))V ⊤. Using ( 4), the second is the cor-
responding entry of V LCL⊤V ⊤. This proves ( 14). The zi = ( i + 2) /2 are distinct, so the
square Vandermonde matrix V is invertible. Sylvester’s law of inertia and ( 2) complete the
proof.
Theorem 5(Independent minimum-degree class) . Suppose G has positive minimum degree δ
and its minimum-degree vertices form an independent set. Then BG has at least two positive
eigenvalues. In particular, ZG(x; H(1, 2, . . . , ∆ + 1)) is not Lorentzian.
Proof. Put p = 1 ∈ R∆+1 and u = eδ−1. Since L⊤p = 0 , νδ−1 = 0 and Cδδ = 0 ,
a := p⊤BGp = n(n − 1) > 0, u ⊤BGp = 0 , u ⊤BGu = 0 . (15)
4

In computing L⊤u, a possible component indexed δ−1 is harmless: that degree class is empty.
Hence
BGu = LCeδ ̸= 0 ,
where on the right eδ denotes the column basis vector in R∆ indexed by the degree δ. For the
inequality, a minimum-degree vertex has a neighbour, and every such neighbour has degree
greater than δ. Choose the largest s for which Csδ > 0; the coeﬃcient of es in LCeδ is then
positive.
Set w = BGu and c = u⊤BGw = ∥BGu∥2
2 > 0. The compression to the columns (p, u, w)
has the form
Q =


a 0 b
0 0 c
b c e

, det Q = −ac2 < 0. (16)
Its positive diagonal entry a excludes three negative eigenvalues, so its inertia is (2, 1, 0). In
particular its three columns are independent, and its two-dimensional positive subspace gives
one for BG. Apply Theorem 4.
Corollary 6. Every connected graph on at least three vertices with a leaf has a positive rank-
two antiferromagnetic target for which its partition function is not Lorentzian. This holds for
every tree of order at least three.
Proof. Two degree-one vertices cannot be adjacent in a connected graph of order at least three.
Thus its minimum-degree class is independent. Every tree of that order has a leaf.
The certiﬁcate ( 16) uses integer matrices of size at most ∆ + 1 , followed by a 3 × 3
determinant. It does not require expanding the qn terms in ( 1).
5. A parameterized obstruction for regular graphs
The preceding criterion is not suﬃcient for regular graphs. Indeed, for a d-regular graph its
kernel is
BG = n(n − 1)ede⊤
d − nd(ed − ed−1)(ed − ed−1)⊤, (17)
which has at most one positive eigenvalue. We therefore use a diﬀerent quadratic derivative.
Let G be d-regular, with n ≥ 3 and d ≥ 2, and let T be its number of unordered triangles.
Set τ = 6 T/n. Choose s > 0, s /∈ {1, 2}, and take three spin values
(t0, t1, t2) = ( s, 1, 2), ℓ = s − 1
s + 1 .
Deﬁne zi, ki by ( 4), and set
Vi· = (1 , ki, k2
i ), D z = diag( zd
0, zd
1, zd
2).
The three ki are distinct, and Dz is positive and invertible.
Theorem 7 (Regular-graph identity) . For the target H = H(s, 1, 2),
Hess
(
∂0∂ n−3
1 ZG(x; H)
)
= cG(s)DzV BℓV ⊤Dz, (18)
cG(s) = ( n − 3)! n 2m−d(s + 1)d > 0,
Bℓ =


(n − 1)(n − 2) −ℓd(n − 2) 0
−ℓd(n − 2) ℓ2d(d − 1) − d(n − 2) ℓd(d − 1)
0 ℓd(d − 1) −ℓ2τ

. (19)
Its determinant is
det Bℓ = ℓ2d(n − 2)
[
(n − 1)
(
(n − 2)τ − d(d − 1)2)
+ ℓ2τ(n − 1 − d)
]
. (20)
5

Proof. The Hessian entry is (n−3)! times a sum over ordered distinct vertices (v, u, w): assign
spin 0 to v, free spins i, j to u, w, and baseline spin 1 to all remaining vertices. The initial edge
weight, before changing u, w, is 2m−d(s + 1)d, independent of v. For a free vertex adjacent to
v, its change has an additional factor
2(s + ti)
(s + 1)(1 + ti) = 1 − ℓki.
The correction for adjacency of the two free vertices is still ( 5). Divide out (n − 3)!2m−d(s +
1)dzd
i zd
j . The remaining entry is
∑
v,u,w
all distinct
(1 − ℓkiAuv)(1 − ℓkjAvw)(1 − kikjAuw), (21)
where A is the adjacency matrix of G.
In this sum there are n(n − 1)(n − 2) ordered triples. Each single-edge indicator has sum
nd(n−2). Each product of two diﬀerent edge indicators has sum nd(d−1): choose its common
vertex, then two ordered distinct neighbours. The product of all three indicators has sum 6T.
Expanding ( 21) and dividing by n gives
(n − 1)(n − 2) − ℓd(n − 2)(ki + kj)
+
(
ℓ2d(d − 1) − d(n − 2)
)
kikj
+ ℓd(d − 1)(k2
i kj + kik2
j ) − ℓ2τk2
i k2
j ,
which is Vi·BℓV ⊤
j· . This proves ( 18). Expanding the determinant of ( 19) gives ( 20).
Corollary 8 (Triangle threshold). If
6T
n < d(d − 1)2
n − 2 , (22)
then a positive three-spin rank-two antiferromagnetic target makes ZG non-Lorentzian. Con-
versely, if (22) fails, none of the Hessians in Theorem 7 has two positive eigenvalues. This
converse concerns only that derivative and target family.
Proof. Write
A∗ = ( n − 1)
(
d(d − 1)2 − (n − 2)τ
)
, R ∗ = τ(n − 1 − d) ≥ 0.
Under ( 22), A∗ > 0. The entirely rational choice
K = 2 + ⌈R∗/A∗⌉ , ℓ = −1/K, s = ( K − 1)/(K + 1) (23)
has 0 < s < 1 and ℓ2R∗ < A ∗. Indeed, for r = R∗/A∗ ≥ 0, (2 + ⌈r⌉)2 > r . Equation ( 20)
is therefore negative. Since (Bℓ)00 > 0, its inertia is (2, 1, 0). The invertible congruence ( 18),
followed by ( 2), proves the obstruction.
If ( 22) fails, then A∗ ≤ 0, τ > 0, and ( 20) is nonnegative for every allowed ℓ. The diagonal
entries (Bℓ)00 > 0 and (Bℓ)22 = −ℓ2τ < 0 force at least one positive and one negative
eigenvalue. A nonnegative determinant then forces the third to be nonpositive. The same
holds for the congruent Hessian.
Corollary 9. Every regular triangle-free graph of degree at least two has a non-Lorentzian
partition function for the ﬁxed positive target H(1/3, 1, 2).
Proof. For T = 0 , ( 20) is negative for every ℓ ̸= 0 . Take ℓ = −1/2, equivalently s = 1 /3.
Remark 10. The strict threshold is exact for this one-conditioned-spin family, not an optimal
condition among all targets or derivatives. For a clique d = n−1 and τ = d(d−1), the bracket
in ( 20) vanishes identically, consistent with the known Lorentzian result.
6

6. Conditioning larger vertex sets
The single conditioned vertex can be replaced by a set. This yields an explicit hierarchy of
tests; no assertion is made that the hierarchy detects every connected nonclique.
Fix any ﬁnite simple graph G, an integer 1 ≤ h ≤ n − 2, and −1 < ℓ < 0. Take q = h + 2
distinct values ai ∈ (−1, 1) with a0 = ℓ, a1 = 0 , and the positive target K(a). For S ⊆ V ,
|S| = h, write
rS(v) = |N(v) ∩ S| (v /∈ S), ν S
r = |{v /∈ S : rS(v) = r}| (0 ≤ r ≤ h).
Let CS
ab count ordered edges of G[V \ S] between vertices of proﬁles a, b, and let e(S) be the
number of edges inside S. Deﬁne the (h + 2) × (h + 1) coeﬃcient matrix
Fjr =
(
r
j
)
(−ℓ)j (0 ≤ j ≤ h + 1, 0 ≤ r ≤ h),
where
( r
j
)
= 0 for j > r . Let J be the (h + 2) × (h + 2) matrix that shifts coordinates down
by one, with zeros in the ﬁrst row. Set
Bh(ℓ) =
∑
|S|=h
(1 − ℓ2)e(S)[
F
(
νS(νS)⊤ − diag(νS)
)
F⊤
− (JF )CS(JF )⊤]
.
(24)
All matrices in the brackets have size h + 2.
Theorem 11 (Conditioned-set identity) . With Vij = aj
i for 0 ≤ i, j ≤ h + 1, one has
Hess
(
∂h
0 ∂ n−h−2
1 ZG(x; K(a))
)
= chV Bh(ℓ)V ⊤, (25)
ch = h!(n − h − 2)! > 0.
Thus Bh(ℓ) and the quadratic-derivative Hessian have the same inertia. For h = 1 , B1(ℓ) = ˆBℓ;
for a d-regular graph this is nBℓ.
Proof. Assign spin 0 to S and baseline spin 1 to its complement. All edges outside G[S] have
weight one, and its e(S) internal edges have weight 1 − ℓ2. The baseline product is therefore
(1−ℓ2)e(S). Changing a free vertex u /∈ S to spin i multiplies its separate baseline contribution
by (1 − ℓai)rS(u). For two adjacent free vertices the additional correcting factor is 1 − aiaj, as
before.
The coeﬃcient vector of (1 − ℓk)r in powers of k is the rth column of F; the vector for
k(1 − ℓk)r is the corresponding column of JF . Summing over distinct free vertices ﬁrst gives
the ﬁrst matrix in ( 24), and subtracting the adjacency correction gives the second. Summing
the baseline weights over S gives Bh(ℓ). The derivative multiplicity is h!(n−h−2)!: it counts
ordered placements of the h conditioned spins and the remaining baseline spins. This also
accounts for coincidences between free and conditioned spin labels. These observations prove
(25). The ai are distinct, so the congruence is invertible. For h = 1 , expanding the proﬁles
gives precisely the triple counts in Theorem 2.
For ﬁxed h, the kernel can be assembled by examining the
( n
h
)
conditioned sets and their
degree proﬁles; no expansion over all (h + 2) n spin assignments is needed. The formulas
extend continuously to ℓ = −1, where (1 − ℓ2)e(S) retains exactly the independent sets S
(with exponent zero interpreted as weight one).
For comparison with the additive targets, ( 4) gives H(t) = 2 diag( z)K(k) diag(z). When
G is d-regular,
ZG(x; H(t)) = 2 mZG((zd
i xi)i; K(k)). (26)
Thus the additive-target version of ( 25) has the additional positive factor 2m−hd(s + 1)hd and
the diagonal congruence Dz, when t0 = s and t1 = 1 . Such a source-independent diagonal
change is not asserted for irregular graphs.
7

7. Structural consequences of the proﬁle identity
A change of polynomial basis makes the boundary of the hierarchy particularly useful. Retain
the notation rS, νS and CS from Theorem 11. Let νS append a zero to νS, and let Dh be
the (h + 2) × (h + 1) matrix with column r equal to er − er+1, for 0 ≤ r ≤ h. For 0 ≤ θ ≤ 1
deﬁne
Qh(θ) =
∑
|S|=h
(1 − θ)e(S)[
θ
(
νS(νS)⊤ − diag(νS)
)
− DhCSD⊤
h
]
.
(27)
At θ = 1 , the convention 00 = 1 leaves precisely the independent h-sets.
Lemma 12 (Proﬁle-basis identity) . Let θ = ℓ2, with −1 < ℓ < 0. For any q ≥ 2, take q
distinct parameters in (−1, 1) with a0 = ℓ, a1 = 0 , and the target K(a). Put Uir = (1 − ℓai)r
for 0 ≤ i < q and 0 ≤ r ≤ h + 1. Then
Hess
(
∂h
0 ∂n−h−2
1 ZG(x; K(a))
)
= h!(n − h − 2)!
θ UQh(θ)U⊤. (28)
The matrix U is invertible when q = h + 2 ; for other q the identity is a rectangular matrix
factorization. It extends to ℓ = −1 when a0 = −1 and the remaining ai stay distinct in
(−1, 1).
Proof. In the polynomial basis 1, y, . . . , y h+1, where y = 1 − ℓk, the proﬁle factor is yr, and
k(1 − ℓk)r = yr − yr+1
ℓ .
Thus the adjacency correction in the proof of Theorem 11 has coeﬃcient matrix DhCSD⊤
h /ℓ2.
The other term is the embedded proﬁle-count matrix in ( 27). This proves ( 28), with the
same derivative multiplicity. The counting argument does not require the evaluation matrix
to be square. The nodes 1 − ℓai are distinct, so U is an invertible Vandermonde matrix when
q = h + 2. All coeﬃcients are continuous at ℓ = −1, proving the boundary statement; in the
square case invertibility also persists there.
7.1. The small-parameter limit and true twins
The other endpoint of the proﬁle kernel gives a diﬀerent structural criterion. Deﬁne the
unweighted edge-proﬁle matrix
Th =
∑
|S|=h
CS, 1 ≤ h ≤ n − 2. (29)
The sum here includes all h-sets, whether or not they are independent.
Lemma 13 (A small-parameter obstruction) . If Th has a negative eigenvalue, a strictly
positive rational antiferromagnetic target of rank two on h+2 spins makes ZG non-Lorentzian.
Proof. Choose f with f⊤Thf < 0. The matrix Dh has full column rank, so there is y ∈ Rh+2
with D⊤
h y = f. Let p = 1 ∈ Rh+2 and R = n − h ≥ 2. Polynomial continuation of ( 27) to
zero gives
Qh(0) = −DhThD⊤
h , Q h(0)p = 0 , d 0 := y⊤Qh(0)y = −f⊤Thf > 0.
8

For θ ≥ 0, direct evaluation gives
p⊤Qh(θ)p = θA(θ), A(θ) = R(R − 1)
∑
|S|=h
(1 − θ)e(S),
p⊤Qh(θ)y = θB(θ), B(θ) = ( R − 1)
∑
|S|=h
(1 − θ)e(S)(νS)⊤y. (30)
In particular A(0) =
( n
h
)
R(R − 1) > 0. The determinant of the compression of Qh(θ) to
columns p, y is
θA(θ)y⊤Qh(θ)y − θ2B(θ)2 = θA(0)d0 + O(θ2).
For all suﬃciently small θ > 0, this determinant and the ﬁrst diagonal entry are positive.
Hence the compression is positive deﬁnite, and Qh(θ) has at least two positive eigenvalues.
Choose ℓ = −1/m for a suﬃciently large integer m, so that θ = 1 /m2, and put q = h + 2.
Take a0 = ℓ, a1 = 0 and, for example, ai = ( i − 1)/(q + 1) for 2 ≤ i < q . These rational
parameters are distinct and lie in (−1, 1). For each such nonzero ℓ, the matrix U in Lemma 12
is invertible. Thus the Hessian in ( 28) has two positive eigenvalues, and ( 2) proves the claim.
The argument does not assume that U remains invertible at ℓ = 0 .
Two distinct vertices are true twins if their closed neighbourhoods are equal. Such vertices
are adjacent and have equal degree.
Theorem 14 (Maximum degree and true twins) . Let G be a connected noncomplete graph
with maximum degree ∆. If no two vertices of degree ∆ are true twins, a strictly positive
rational antiferromagnetic target of rank two on ∆ + 1 spins has a non-Lorentzian partition
polynomial on G.
Proof. Put h = ∆ − 1. Connectedness and noncompleteness imply ∆ ≥ 2, and hence 1 ≤ h ≤
n − 2. If an ordered edge uv outside an h-set S contributes to (Th)hh, both endpoints are
adjacent to every vertex of S and to one another. The degree bound forces
du = dv = ∆ , N (u) \ {v} = S = N(v) \ {u}.
Then N[u] = N[v], contrary to the hypothesis. Therefore (Th)hh = 0 . Take a vertex u of
degree ∆ and a neighbour v, and use S = N(u) \ {v}. The edge uv contributes to (Th)hj with
j = |N(v) ∩ S| < h, by the same argument. Thus (Th)hj > 0. The principal matrix on indices
h, j has determinant −(Th)2
hj < 0, so Th has a negative eigenvalue. Apply Lemma 13, with
h + 2 = ∆ + 1 .
This proof is constructive. For c = ( Th)hj > 0 and a = ( Th)jj , the rational vector
f = ej −(a+1)eh/(2c) satisﬁes f⊤Thf = −1. Set yh+1 = 0 and yr = ∑h
k=r fk, so that D⊤
h y = f.
Testing ℓ = −2−k with exact arithmetic eventually gives a positive deﬁnite compression in
(30).
Corollary 15. The conclusion of Theorem 14 holds for every connected noncomplete graph
without true twins, for every connected graph of order at least three with a unique maximum-
degree vertex, and for every connected noncomplete edge-regular graph. In particular it holds
for all connected noncomplete strongly regular graphs.
Proof. The ﬁrst two statements follow directly. For the third, edge-regular means regular of
degree d, with a constant number λ of common neighbours for each adjacent pair. A true-
twin edge would give λ = d − 1, making every edge a true-twin edge. Equality of closed
neighbourhoods along paths would then make the connected graph complete. Thus no such
edge exists. Strong regularity implies edge regularity.
9

For an inﬁnite family outside the earlier triangle threshold, take the line graph of Km,
m ≥ 6. It has n = m(m − 1)/2, d = 2( m − 2) and λ = m − 2; its ordered triangle count per
vertex is τ = dλ. Since
λ(n − 2) − (d − 1)2 = (m − 3)(m2 − 8m + 14)
2 > 0,
the threshold ( 22) fails, while Corollary 15 still gives an obstruction. Any nonclique counterex-
ample to the full connected-source conjecture must therefore contain true twins of maximum
degree. Neither the number of spins nor the parameter choice in this theorem is asserted
uniform over all graphs.
7.2. The independent-set endpoint
For a graph with an edge, let α denote independence number, with α(∅) = 0 , and set
b(G) = max
(u,v):uv∈E
α
(
G[N(u) \ {v}]
)
, (31)
c(G) = max
uv∈E
α
(
G[N(u) ∩ N(v)]
)
. (32)
The ﬁrst maximum uses both orientations of each edge.
Theorem 16(Neighbourhood independence gap) . If b(G) > c(G), a strictly positive rational
antiferromagnetic matrix of rank two on c(G)+3 spins has a non-Lorentzian partition function
on G.
Proof. Put h = c(G)+1 . Since b(G) ≥ h, some edge uv and independent h-set S ⊆ N(u)\{v}
exist. In particular, h ≤ n − 2. Let
C∗ =
∑
|S|=h
S independent
CS, Q = Qh(1).
One has (C∗)hh = 0 . Otherwise the two endpoints of an edge would be adjacent to every
vertex in an independent h-set, contradicting c(G) < h . The chosen u, v, S gives (C∗)hj > 0
for some j < h , so C∗eh ̸= 0 .
Take p = 1 ∈ Rh+2 and u0 = eh+1. Since D⊤
h p = 0 , D⊤
h u0 = −eh, and the last entry of
νS is zero,
s0 := p⊤Qp = Ih(G)(n − h)(n − h − 1) > 0, (33)
p⊤Qu0 = 0 , u ⊤
0 Qu0 = 0 , Qu 0 = DhC∗eh ̸= 0 , (34)
where Ih(G) counts independent h-sets. The last inequality uses injectivity of Dh. Put
w = Qu0 and c0 = ∥Qu0∥2
2 > 0. The compression of Q to the columns (p, u0, w) has the form


s0 0 b0
0 0 c0
b0 c0 e0

, det = −s0c2
0 < 0.
Its positive diagonal entry excludes three negative eigenvalues, so the compression has two
positive eigenvalues. Hence so does Q. Choose any distinct rational remaining ai ∈ (−1, 1)
with a1 = 0 . Lemma 12 ﬁrst gives an obstruction at ℓ = −1. The two positive eigenvalues
persist when the rational parameter ℓ > −1 is suﬃciently close to −1. All ai then lie in (−1, 1),
so K(a) is strictly positive and has rank two. The Hessian test ( 2) proves the result.
10

The proof is constructive: with the remaining rational ai ﬁxed, exactly testing ℓ = −1+1/k
for integers k ≥ 2 eventually ﬁnds a positive target. It does not assert a uniform bound on k
over all source graphs.
Corollary 17 (One target for connected diamond-free sources) . Let
K⋄ = 1
9


0 9 12 15
9 9 9 9
12 9 8 7
15 9 7 5

. (35)
For every connected diamond-free ﬁnite simple graph G, ZG(x; K⋄) is Lorentzian if and only
if G is a clique. Thus the connected-source characterization conjecture holds on diamond-free
graphs. For each nonclique, a strictly positive rational rank-two target on at most four spins
also gives an obstruction.
Proof. The displayed target is K(−1, 0, 1/3, 2/3); it is nonnegative, has rank two and inertia
(1, 1, 2). For a clique the result is [ 2, Theorem 3.1].
Suppose G is not complete. If G is triangle-free, then c(G) = 0 and b(G) ≥ 1, because
a connected nonclique contains two adjacent edges. The proof of Theorem 16, at h = 1 and
ℓ = −1, gives a two-positive-eigenvalue Hessian for the principal target K(−1, 0, 1/3). This
Hessian is a principal submatrix of the same quadratic derivative for K⋄, so the latter also
fails ( 2).
Otherwise G contains a triangle. Diamond-freeness implies c(G) = 1 : a common neigh-
bourhood of an edge cannot contain an independent pair, while a triangle gives a common
neighbour. There is a nonsimplicial vertex u of degree at least three. Indeed, if every vertex
of degree at least three were simplicial and such a vertex v existed, its closed neighbourhood
N[v] would be a clique of size at least four. Every vertex of that clique has degree at least
three and is simplicial. An outside neighbour of any of them would therefore also be adjacent
to v, a contradiction. Hence N[v] would be a whole component, making G complete. If no
vertex has degree at least three, a connected graph containing a triangle is just K3, again
complete.
Choose nonadjacent x, y ∈ N(u) and a third neighbour v. Then {x, y} ⊆ N(u) \ {v}, so
b(G) ≥ 2 > c(G). The proof of Theorem 16, now at h = 2 and ℓ = −1, applies directly to K⋄.
Finally perturb its ﬁrst parameter from −1 into (−1, 0); the two positive Hessian eigenvalues
persist and all target entries become positive.
The ﬁxed matrix ( 35) has one zero entry. Its strictly positive perturbation may depend
on G; no ﬁxed positive four-spin target for the entire class is asserted. The gap condition in
Theorem 16 is suﬃcient, not necessary for an obstruction or for failure of the universal-target
property.
8. Clique separators with disjoint complete branches
The independent-set boundary also treats sources containing diamonds that need not satisfy
the neighbourhood-gap criterion. Write ∨ for graph join and ⊔ for disjoint union.
Proposition 18 (Two branches). For integers a, b, s ≥ 1, let G = Ks ∨ (Ka ⊔ Kb). Then
ZG(x; K⋄) is not Lorentzian. More generally, the same conclusion holds for any four-spin
target K(−1, 0, c, d) with −1 < c, d < 1 and all four parameters distinct.
Proof. Put A = a−1, B = b−1, L = A+ B and C = A(A−1) + B(B −1). Suppose ﬁrst that
L > 0 and use h = 2 , θ = 1 in Lemma 12. Every independent two-set contains one vertex in
11

each branch, so there are ab such sets. Outside each one the proﬁle counts are ν1 = L, ν2 = s,
and the ordered edge counts are C11 = C, C12 = C21 = sL and C22 = s(s − 1). Consequently,
Q2(1) = ab(0 ⊕ M), M =


2AB C sL
C 2sL − C s (s − 1 − L)
sL s (s − 1 − L) −s(s − 1)

. (36)
Direct expansion gives
det M = −s(L + s − 1)
[
L2(L + 2s − 1) + 2 AB(s − 1)(L + s)
]
< 0, (37)
1⊤M1 = ( L + s)(L + s − 1) > 0.
Thus M has inertia (2, 1, 0). The square evaluation matrix U is invertible for the four distinct
parameters, so the Hessian in ( 28) has two positive eigenvalues. Here n − h = L + s ≥ 2, as
required.
If L = 0 , then a = b = 1 and G is Ks+2 with one edge removed. The counts in ( 7) are
N = s(s + 1)(s + 2), E = s2(s + 3), W = s(s2 + 3s − 2), U = s(s + 4)(s − 1).
They satisfy W2 − EU = E2 − NW = 4 s2. The polynomial counting identity ( 8) extends to
ℓ = −1, and its coeﬃcient matrix does not depend on the third spin parameter. Therefore,
at h = 1 ,
det ˆB−1 = N(EU − W2) + U(E2 − NW ) = −24s3 < 0.
Its ﬁrst diagonal entry N is positive. The three distinct parameters (−1, 0, c) give an invertible
evaluation matrix, hence a principal Hessian submatrix with two positive eigenvalues. The
four-spin Hessian has at least as many positive directions. In both cases ( 2) proves the
conclusion.
Theorem 19 (One ﬁxed ﬁve-spin target) . Let
K5 = 1
16


0 16 20 24 28
16 16 16 16 16
20 16 15 14 13
24 16 14 12 10
28 16 13 10 7


= K(−1, 0, 1/4, 1/2, 3/4). (38)
For every s ≥ 1, r ≥ 2 and a1, . . . , ar ≥ 1, the connected noncomplete graph
G = Ks ∨
(
Ka1 ⊔ · · · ⊔ Kar
)
has non-Lorentzian partition polynomial ZG(x; K5). The target is nonnegative of rank two,
with exactly one zero entry. For each such G, a strictly positive rational ﬁve-spin perturbation
also gives an obstruction.
Proof. The target has inertia (1, 1, 3) by the argument for ( 6). For r = 2 , Proposition 18
applies to the ﬁrst four spins; its quadratic-derivative Hessian is a principal submatrix of the
ﬁve-spin Hessian. We therefore assume r ≥ 3.
Put Ai = ai − 1, L = ∑
i Ai, and C = ∑
i Ai(Ai − 1). If L > 0, use h = r at the boundary
θ = 1 in Lemma 12, now with q = 5 . Every independent h-set chooses one vertex from each
branch, and there are P = ∏
i ai choices. The remaining branch vertices have proﬁle 1, and
separator vertices have proﬁle h. The only nonzero part of Qh(1) is on indices (1, 2, h, h + 1),
where it is P times
M =


L(L − 1) − C C 0 sL
C −C sL −sL
0 sL 0 s(s − 1)
sL −sL s (s − 1) −s(s − 1)

. (39)
12

Its determinant and the principal determinant on proﬁle indices 2, h are
det M = Ls2(L + s − 1)
[
sL2 − (s − 1)C
]
> 0, (40)
det M[{2, h}] = −s2L2 < 0.
Indeed 0 ≤ C ≤ L(L − 1), so the bracket in ( 40) is at least L(L + s − 1) > 0. The negative
principal determinant gives a positive and a negative direction. The positive full determinant
then forces inertia (2, 2, 0).
The four active columns of U have degrees 1, 2, h, h + 1 . On the four positive nodes
1, 5/4, 3/2, 7/4 they are linearly independent. To see this, a nonzero polynomial with four
distinct powers has at most three positive roots by Descartes’ sign rule; dependence would
give four distinct positive roots. Thus the 5 ×4 active evaluation matrix has full column rank.
Multiplication on its two sides preserves the nonzero inertia of M, and ( 28) gives two positive
eigenvalues. The derivative is valid because n − h = L + s ≥ 2.
If L = 0 , all branches are singletons. Choose h = r −1 ≥ 2. Each independent h-set leaves
one branch vertex of proﬁle 0 and s vertices of proﬁle h. There are r such sets, and Qh(1) is
r times the following matrix on indices (0, 1, h, h + 1):
M0 =


0 0 0 s
0 0 s −s
0 s 0 s(s − 1)
s −s s (s − 1) −s(s − 1)

. (41)
Here det M0 = s4 > 0, whereas its principal determinant on indices 1, h is −s2. Hence its
inertia is again (2, 2, 0). The active powers 0, 1, h, h + 1 are distinct, and the same four-node
argument gives full column rank. The Hessian therefore has two positive eigenvalues. Now
n − h = s + 1 ≥ 2.
Finally, perturb the ﬁrst parameter from −1 into (−1, 0). The two strictly positive Hessian
eigenvalues persist by continuity. Choose a rational perturbation; all target entries become
strictly positive, with rank two and one positive eigenvalue.
When r = 1 the source is a clique and its partition polynomial is Lorentzian by [ 2, Theorem
3.1]. Thus the ﬁxed target ( 38) characterizes the complete members of the whole family with
s ≥ 1, r ≥ 1 and nonempty branches. The number of target states is independent of the
number and sizes of the branches. We do not assert that ﬁve is minimal, that one strictly
positive perturbation works for every source, or that the four-spin target of Proposition 18
suﬃces for the entire family.
Remark 20 (A limit of a four-spin restriction) . Full column rank in the preceding proof is
essential. Take G = Ks ∨ (K2 ⊔ K1 ⊔ K1) and h = 3 . For K⋄ the ﬁrst row and column of the
boundary Hessian vanish. After removing its positive scalar factor, the remaining matrix is
V MV ⊤, where M is ( 39) with L = 1 , C = 0 and V evaluates powers 1, 2, 3, 4 at 1, 4/3, 5/3.
Its determinant is
det(V MV ⊤) = 12800
4782969s3(185s − 473) > 0 ( s ≥ 3).
The original M has two positive and two negative eigenvalues, so the restriction has at most
two positive eigenvalues. Its positive determinant and positive trace therefore give inertia
(1, 2, 0). This derivative is inconclusive for s ≥ 3. Other derivatives may still detect these
graphs; this is not a counterexample to universality of K⋄.
13

9. Complete multipartite sources
The same four-spin target also detects a family not contained in the diamond-free class. In
this section a complete multipartite graph has nonempty parts, and two vertices are adjacent
exactly when they belong to diﬀerent parts.
Theorem 21(One ﬁxed target for complete multipartite sources) . For every connected com-
plete multipartite graph G, the partition polynomial ZG(x; K⋄) is Lorentzian if and only if
G is a clique. For every noncomplete such G, a strictly positive rational four-spin rank-two
perturbation of K⋄ also has a non-Lorentzian partition polynomial. The perturbation may
depend on G.
Proof. The clique direction follows from [ 2, Theorem 3.1]. For the converse, write the part
sizes as a1, . . . , ar. Connectedness and noncompleteness give r ≥ 2 and α = max i ai ≥ 2. Put
h = α − 1; then 1 ≤ h ≤ n − 2. Apply Lemma 12 at ℓ = −1, θ = 1 , and q = 4 . Only
independent h-sets contribute.
Such a set S lies in one part i with ai ≥ h. There are wi =
( ai
h
)
choices. Outside S, the
ki = ai −h ∈ {0, 1} vertices in that part have proﬁle 0, and the other yi = n−ai vertices have
proﬁle h. Every pair between these two classes is an edge, there are no edges within proﬁle 0,
and the ordered edge count within proﬁle h is
ti = y2
i −
∑
j̸=i
a2
j .
Summing over all i with ai ≥ h, deﬁne
A =
∑
i
wi
∑
j̸=i
aj(aj − 1), B =
∑
i
wikiyi, C =
∑
i
witi. (42)
All three numbers are nonnegative. Moreover B > 0: a largest part has ki = 1 and yi > 0.
First let h ≥ 2. Substitution into ( 27) shows that Qh(1) is supported on indices (0, 1, h, h+
1), where it is the matrix
M =


0 0 0 B
0 0 B −B
0 B A C
B −B C −C

. (43)
Indeed, the proﬁle- 0 diagonal is zero because ki(ki − 1) = 0 , and its pair term with proﬁle h
cancels the corresponding edge term. The proﬁle- h diagonal is yi(yi − 1) − ti, whose sum is A.
All other entries follow from the two diﬀerences in the columns of Dh. Now det M = B4 > 0,
while its principal determinant on indices 1, h is −B2 < 0. Thus M has inertia (2, 2, 0).
The active evaluation matrix in ( 28) evaluates the powers 0, 1, h, h+1 at 0, 1, 4/3, 5/3. It is
invertible. In fact, a vanishing linear combination has zero constant coeﬃcient by evaluation
at zero. Dividing by the variable leaves at most three nonzero monomials, which by Descartes’
sign rule have at most two positive roots unless the polynomial is zero. The three distinct
positive evaluation nodes therefore force all coeﬃcients to vanish. The quadratic-derivative
Hessian has two positive eigenvalues.
If h = 1 , the middle two proﬁle indices coincide. Direct substitution instead gives the 3×3
kernel
M1 =


0 0 B
0 A + 2B C − B
B C − B −C

.
Its determinant is −B2(A + 2B) < 0, and its middle diagonal entry is positive, so its inertia
is (2, 1, 0). The evaluation matrix on powers 0, 1, 2 at the same four nodes has full column
rank. Again the Hessian has two positive eigenvalues.
14

Both cases violate ( 2). Finally, replace the ﬁrst target parameter −1 by a rational ℓ ∈
(−1, 0) suﬃciently close to −1. The two positive eigenvalues persist by continuity. All target
entries become strictly positive, and its rank and inertia are those of the rank-two family
already proved above.
The theorem includes arbitrarily many parts and arbitrarily large part sizes. Its proof uses
only four active proﬁle columns even when h > 2; a square evaluation matrix of size h + 2 is
unnecessary. The Lorentzian characterization of complete multipartite graphs by Choudhury–
Khare [ 6, Theorem 2.3] concerns instead the homogenized determinant of a distance-matrix
blowup. It is not a statement about the spin partition polynomial ( 1) or the ﬁxed target here.
10. Examples and limits
10.1. A second-level obstruction beyond the triangle threshold
Start with two disjoint copies of K4 on vertices {0, 1, 2, 3} and {4, 5, 6, 7}. Delete edges (0, 1)
and (4, 5), and add (0, 4) and (1, 5). The resulting graph is connected, cubic, and has four
triangles. Hence τ = 3 , while the right side of ( 22) is 2. The one-conditioned-spin test cannot
detect it for any of its allowed parameter values.
For h = 2 and the boundary value ℓ = −1, direct evaluation gives
B2(−1) =


480 480 60 0
480 264 −120 −12
60 −120 −148 −16
0 −12 −16 −4

.
Symmetric elimination without permutations has consecutive pivots
480, −216, −11
2 , 106
33 .
Its inertia is therefore (2, 2, 0). Theorem 11 at the continuous boundary supplies a non-
Lorentzian Hessian. Its two positive eigenvalues persist for ℓ > −1 suﬃciently close to −1,
giving positive rank-two targets as well. The supplement checks explicitly that ℓ = −99/101
works, using rational elimination of B2(−99/101) and direct comparison with the additively
scaled target H(1/100, 1, 2, 3) via ( 26).
10.2. Parameter variation enlarges the test
Allowing the boundary value s = 0 in the counting identity gives ℓ = −1 and the more
restrictive suﬃcient condition
τ < (n − 1)d(d − 1)2
(n − 1)2 − d . (44)
For a concrete strict improvement, take the graph on {0, . . . , 11} with edges
(0, 1), (0, 2), (0, 8), (0, 9), (1, 4), (1, 7), (1, 9), (2, 5),
(2, 8), (2, 11), (3, 6), (3, 7), (3, 8), (3, 11), (4, 5), (4, 7),
(4, 10), (5, 6), (5, 9), (6, 10), (6, 11), (7, 10), (8, 9), (10, 11).
It is connected and 4-regular, and has 7 triangles. Thus n = 12 , d = 4 , τ = 7 /2. At s = 0 ,
det B−1 = 540 > 0, so this Hessian has at most one positive eigenvalue. At s = 2 /3, ℓ = −1/5
and
det B−1/5 = −2004
125 < 0.
15

The positive target is
H(2/3, 1, 2) =


4/3 5 /3 8 /3
5/3 2 3
8/3 3 4

.
The supplement veriﬁes the full Hessian identity for this graph with rational arithmetic.
10.3. The degree-count test does not settle all irregular graphs
Consider the connected six-vertex graph with edge set
{(0, 1), (0, 4), (0, 5), (1, 2), (1, 5), (2, 3), (2, 5), (3, 4)}.
Its degree counts are ν2 = 2 , ν3 = 4 , and its kernel is
BG =


0 0 0 0
0 −2 0 2
0 0 −6 16
0 2 16 2

.
The characteristic polynomial is λ(λ3 + 6λ2 −264λ −560). The cubic has exactly one positive
root by Descartes’ rule of signs and a sign change between zero and suﬃciently large positive
λ. Thus this kernel has only one positive eigenvalue. It does not establish Lorentzianity of
the partition function. A diﬀerent derivative supplies a countermodel in the ﬁnite certiﬁcates
described below.
Graphs with many triangles can also fail ( 22). The condition b(G) > c (G) also leaves
cases untreated. These suﬃcient criteria do not prove the full connected-source conjecture,
and their failure is not evidence against that conjecture.
10.4. Limits of three ﬁxed subtargets
The same ﬁxed four-spin target K⋄ has an exact quadratic-derivative obstruction for every
connected nonclique of orders three through seven in the graph atlas: 989 graphs. This is
a stronger ﬁnite assertion than allowing a diﬀerent target for each graph, but it is not an
arbitrary-order theorem. An additional deterministic sample of 64 graphs, with orders up to
ten, also yields exact obstructions. This sample is not an exhaustive census beyond order
seven.
Deleting one of the last three states can destroy this property. For the principal target on
states (0, 1, 2), the seven-vertex graph with edge set
{(0, 1), (0, 4), (1, 2), (1, 4), (2, 3), (4, 5), (5, 6)}
has a Lorentzian partition polynomial. For the principal targets on states (0, 1, 3) and
(0, 2, 3), the six-vertex graph in Section 10.3 has that property. The supplement records
every quadratic-derivative Hessian: 21 in the ﬁrst case and 15 in each of the other two. Exact
rational congruences give at most one positive eigenvalue in each, and the full M-convex ex-
change condition is veriﬁed on each support. The full characterization cited after ( 2) proves
these ﬁnite claims. They concern three speciﬁc ﬁxed targets; they do not show that every
three-spin target fails or that four spins are necessary in general.
16

10.5. The small-parameter criterion is not complete
Let G = C5[K2]: replace each vertex of a ﬁve-cycle by a two-vertex clique, and join all
vertices in two replacement cliques whenever the original cycle vertices are adjacent. This is
a connected noncomplete 5-regular graph on ten vertices, and each replacement pair is a pair
of true twins. Every matrix Th, 1 ≤ h ≤ 8, is positive semideﬁnite, so Lemma 13 does not
detect G. Here this is an exact ﬁnite claim with a short coeﬃcient certiﬁcate.
For an ordered edge uv, put c = |N(u) ∩ N(v)|, a = du − 1 − c, b = dv − 1 − c, and
d = n − du − dv + c. Partitioning the other vertices by their adjacency to u, v gives the
contribution
∑
k
(
c
k
)(
a
r − k
)(
b
t − k
)(
d
h − r − t + k
)
(45)
to (Th)rt, with out-of-range binomial coeﬃcients zero. For this graph, ten ordered edges have
c = 4 and forty have c = 2 . Thus (Th)rt is the coeﬃcient of xrytzh in
10(1 + xyz)4(1 + z)4 + 40(1 + xyz)2(1 + xz)2(1 + yz)2(1 + z)2.
For h = 1 , 2, 3, 4, ordinary symmetric elimination without permutations has the following
positive diagonal pivots:
h Pivots of Th
1 120, 200/3
2 100, 224, 300/7
3 40, 480, 360, 200/9
4 10, 320, 600, 592/3, 250/37
For each ﬁxed outside edge, complementing S in its other eight vertices replaces h by 8 − h
and each proﬁle r by 4 − r. It therefore relates Th and T8−h by reversal of the active proﬁle
indices and zero padding. This proves positive semideﬁniteness for h = 5 , 6, 7; for h = 8 the
sole nonzero entry is (T8)44 = 50 .
This failure does not extend to the full proﬁle hierarchy. Use q = h+ 2, a0 = ℓ, a1 = 0 and
ai = ( i−1)/(h+2) for i ≥ 2. At ℓ = −99/100, its kernels for h = 3 , 4, 5 have respective inertias
(2, 3, 0), (2, 4, 0) and (2, 3, 2), veriﬁed by exact congruences and direct partition-coeﬃcient
identities. All three targets are strictly positive. Since α(G) = 2 , the unscaled endpoint Qh(1)
vanishes at these levels. The ﬁrst nonzero term after dividing by the smallest power of 1 − θ
has two positive eigenvalues for h = 3 , 4, but only one for h = 5 . The nearby kernel at h = 5
nevertheless has two. Thus neither the zero-parameter test nor the leading endpoint term
alone supplies a general completeness argument.
11. Exact checks and reproducibility
The accompanying supplement contains the source scripts, their data, and a manifest of ﬁle
hashes. All checks were run in the authoring context; none is a formal proof-assistant veri-
ﬁcation or an independent model assessment. The general proofs are the counting identities
and compression arguments above.
17

Check Cases
Normalized three-spin identity, including irregular
sources
288
Degree identity, all connected graphs of orders 3–5,
original nonnegative target
29
Degree identity, strictly positive target of Theorem 4 29
Independent minimum-degree compression, connected
graph atlas of orders 3–7
806
Original regular identity, exact enumeration 13
Parameterized regular identity: 18 graphs, 5 rational
parameters
90
Additive-target conditioned-set identity for h = 1 , 2, 3 26
Normalized conditioned-set identity, including irregu-
lar sources
24
Certiﬁcate census Cases
Exact three-spin countermodels for all connected non-
cliques of orders 3–6 in the atlas
137
Positive rank-two hierarchy certiﬁcates for all con-
nected noncliques of orders 3–7
989
Characteristic-polynomial audit of those kernels 989
Neighbourhood-gap compression and positive continu-
ation
634
Fixed diamond-free target, direct identities 255
Positive perturbations of the diamond-free target, di-
rect identities
255
Fixed four-spin certiﬁcates on all connected noncliques
of orders 3–7
989
Clique-separator and ﬁxed-target checks Cases
Two-branch sources: direct ﬁxed four-spin boundary
identities
64
Two-branch sources: direct positive continuations 46
Clique–cluster joins: direct ﬁxed ﬁve-spin boundary
identities
64
Clique–cluster joins: direct positive continuations 27
Additional seeded ﬁxed four-spin obstructions, orders
up to ten
64
Exact Lorentzian counterexamples to three ﬁxed sub-
targets
3
Four-spin restriction: direct checks of Remark 20 6
Complete multipartite sources: direct ﬁxed four-spin
identities
36
Complete multipartite sources: direct positive contin-
uations
17
18

Small-parameter checks Cases
Maximum-degree theorem: exact compression certiﬁ-
cates
821
Maximum-degree theorem: direct positive Hessian
identities
819
Unweighted proﬁle-kernel probe, atlas and selected
blowups
1001
C5[K2]: exact semideﬁnite kernels, all valid h 8
C5[K2]: direct positive full-hierarchy identities 3
The maximum-degree checks cover all 817 eligible connected noncliques of orders three
through seven, two larger wheels, the line graph of K6, and the 4-by-4 rook graph. Each
records a rational negative direction for Th and a positive deﬁnite two-dimensional compres-
sion of a nearby Qh. The 15- and 16-vertex examples use exact kernels and the proved identity;
the other 819 also use direct partition enumeration. Among these 821 graphs, 244 fail the
earlier edge–wedge–triangle suﬃcient criterion. The separate unweighted probe ﬁnds an indef-
inite Th for every atlas nonclique, but fails on nine selected clique blowups beyond the atlas.
Section 10.5 proves the ﬁrst such limitation explicitly. Neither this probe nor the theorem
asserts completeness of the unweighted criterion.
The three-spin census contains 141 connected graphs, including four complete-graph con-
trols. Each of the 137 certiﬁcates records the edge set, integer target Hij = ti + tj, derivative
multi-index, integer Hessian, its negative determinant and positive trace. These signs prove
inertia (2, 1, 0). The ﬁnite census does not establish the conjecture at arbitrary order; absence
of a detected obstruction in the clique controls is not its proof.
The larger census contains all 994 connected graphs of orders three through seven, of which
ﬁve are cliques. For each of the 989 noncliques it gives a strictly positive rational rank-two
target, an integer-scaled proﬁle kernel, a rational congruence certiﬁcate, and direct agreement
with a Hessian obtained by partition-coeﬃcient enumeration. A separate audit checks the
characteristic polynomial of every stored kernel. Its real roots are counted exactly using
Descartes bounds for positive and negative roots together with the exact zero multiplicity;
the bounds sum to the degree and agree with the congruence inertia. These are separate
computations within the same authoring context, not a separate referee.
The gap check covers 634 graphs in the same atlas. All 255 connected diamond-free
noncliques there satisfy the criterion; 88 are triangle-free and 167 contain triangles. For these
255 sources, both the ﬁxed boundary target and strictly positive rational perturbations were
checked by direct partition-coeﬃcient enumeration. The ﬁnite checks corroborate the general
proof of Corollary 17; they do not replace it.
The clique-separator checks expand the determinant identities symbolically and compare
the predicted Hessians with direct partition-coeﬃcient enumeration. The ﬁxed-ﬁve sample
includes r = 2 , 3, 4, 5, 6, so the number of conditioned vertices can exceed the number of
nonbaseline target states. The full proof uses the rectangular identity and the four-column
rank argument, rather than extrapolating from these checks. The complete multipartite
sample has largest parts from two through six. Its 36 boundary identities and 17 positive
identities were checked by direct partition-coeﬃcient enumeration; the symbolic determinants
in Theorem 21 were expanded separately.
19

The main scripts are:
verify_degree_kernel.py verify_neighbourhood_gap.py
verify_normalized_target.py verify_fixed_diamond.py
verify_regular_obstruction.py verify_two_clique_extension.py
verify_parametric_obstruction.py verify_fixed_five_cluster.py
verify_conditioning_hierarchy.py probe_fixed_diamond_scope.py
certify_source_witnesses.py probe_larger_fixed_target.py
certify_profile_hierarchy.py probe_three_spin_targets.py
audit_profile_certificates.py verify_four_spin_restriction.py
verify_multipartite_extension.py verify_maximum_degree_twins.py
verify_blowup_layer.py probe_zero_parameter_kernels.py
The source-witness script reads the preserved ﬁnite-search candidates and recomputes
their Hessians by exact enumeration. The parameterized script separately checks the sym-
bolic determinant, the rational parameter selection, and the positive-target identity. Python,
SymPy and NetworkX suﬃce for these checks; NumPy is used only by the exploratory witness
search. The supplementary README gives invocation and provenance details.
12. Remaining question
The obstructions extract degree-to-degree adjacency and edge, wedge and triangle counts.
The conditioned-set hierarchy uses ﬁner adjacency proﬁles. Its small-parameter limit gives
the maximum-degree criterion: any nonclique counterexample to the source conjecture must
have true twins of maximum degree. The explicit C5[K2] limitation shows why that limit
alone is insuﬃcient. Its independent-set boundary gives the neighbourhood-gap theorem
and the diamond-free characterization. Its rectangular evaluation also gives a ﬁxed ﬁve-spin
obstruction for joins of a clique with any number of complete branches, and a ﬁxed four-spin
obstruction for all noncomplete complete multipartite sources. A general argument would
have to prove that a suitable test detects every connected nonclique; no such suﬃciency
is established here. The distinction between bounded countermodel search and a proof for
graphs of arbitrary order remains essential.
Authorship and AI assistance.Lluis Eriksson is the responsible human author. Codex as-
sisted with literature searches, derivations, manuscript preparation and computational checks.
Any model assessments are maintained separately, bound to the exact manuscript hash; they
do not constitute human peer review or formal veriﬁcation. No numerical rating forms part of
this manuscript. The author operates AIRR, the intended repository; this relationship does
not constitute external peer review.
20

References
[1] P. Brändén and J. Huh, Lorentzian polynomials, Annals of Mathematics 192 (2020), 821–
891. doi:10.4007/annals.2020.192.3.4.
[2] J. Lee, J. Oh and J. Seo, Counting homomorphisms in antiferromagnetic graphs
via Lorentzian polynomials , arXiv:2506.13659v2 (2025). https://arxiv.org/html/2506.
13659v2.
[3] J. Lee and J. Seo, Antiferromagnetic models are clique-minimizing , arXiv:2608.17920v1
(2026). https://arxiv.org/html/2608.17920v1.
[4] J. P. Matherne, A. H. Morales and J. Selover, The Newton polytope and Lorentzian
property of chromatic symmetric functions , Selecta Mathematica 30 (2024), article 42;
arXiv:2201.07333v4. https://arxiv.org/html/2201.07333v4.
[5] X. Zeng, Two-vertex cuts and a Lorentzian obstruction for bistable bipartite graphs , re-
search note, AI-Has-Taste, BW2-PR20260914-lorentzian_cliques (2026). Archived source,
accessed 17 October 2026 .
[6] P. N. Choudhury and A. Khare, Blowup polynomials and delta-matroids of graphs , Sémi-
naire Lotharingien de Combinatoire 86B (2022), article 42, 12 pp.; arXiv:2203.04105.
https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/42.pdf.
21