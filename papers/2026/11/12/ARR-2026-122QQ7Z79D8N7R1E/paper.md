# Torus-Holonomy Obstructions, Complex-vs-Real Signing Dichotomies, and Clifford-Cube Lifting Beyond Huang

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-122QQ7Z79D8N7R1E` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/torus-holonomy-unitary-signings-beyond-huang (`v1.0.0`)  
**Canonical PDF SHA-256:** `cb30c5a97fcc76127e2aa28b573828ac21dd96bf3f07a8bce7a1e10ee79962ca`

## Abstract

Huang's proof of the Sensitivity Conjecture rests on constructing a real +-1 signing S of the hypercube Q_n satisfying S^2 = n I. We determine exact topological, algebraic, and spectral boundaries for extending Huang-optimal signings S^2 = d I (both real symmetric and complex Hermitian with unit-modulus edge weights |S_{xy}| = 1) to general d-regular graphs and their Cartesian products. First, we prove a universal complex torus-holonomy no-go theorem: for any two non-bipartite regular graphs G and H, no Hermitian unit-modulus signing S of G box H — even over all of C — satisfies S^2 = (d_G + d_H) I. Every odd-cycle discrete torus C_{2a+1} box C_{2b+1} in G box H forces the product of its (2a+1)(2b+1) elementary 4-cycle holonomies to equal both (-1)^((2a+1)(2b+1)) = -1 and +1 (since every edge cancels via S_{xy} conj(S_{xy}) = |S_{xy}|^2 = 1). For real +-1 signings, v elementary-4-cycle-disjoint odd-cycle tori enforce the quantitative Frobenius defect ||S^2 - d I||_F^2 >= 8v. On H(2,3) = K_3 box K_3, exhaustive zero-float Faddeev-LeVerrier and Sturm isolation across all 2^10 = 1,024 real switching classes (43 distinct spectra) certifies min ||S||_op = (1 + sqrt(17))/2 > 2 = sqrt(4) (exact characteristic polynomial x(x^4 - 9x^2 + 16)^2), max lambda_5(S) = 1 < 2 (factor-2 collapse on 5-vertex interlacing), and max lambda_4(S) = 2 (attained by -A at ||S||_op = 4). Second, we prove a sharp complex-vs-real signing dichotomy on complete graphs K_q: real symmetric +-1 signings S^2 = (q-1)I_q force q === 2 (mod 4) (symmetric conference matrices), ruling out all odd q and all q === 0 (mod 4), whereas purely imaginary Hermitian signings H_q = i A_q in {0, +-i}^{q x q} from skew-Hadamard matrices achieve H_q^2 = (q-1)I_q across q in {4, 8, 12, 16, 20, 24, ...}. Furthermore, the block-Clifford lift S_{k+1} = [[S_k, I], [I, -S_k]] preserves S_k^2 = (d_0 + k) I along G_0 box Q_n without requiring G_0 to be bipartite, proving Delta((G_0 box Q_n)[U]) >= ceil(sqrt(d_0 + n)) for every induced subgraph with |U| > |V|/2 across infinite non-bipartite families seeded by conference, skew-Hadamard, and octahedron graphs. Third, we present an exhaustive zero-float switching-class atlas across 11 canonical regular graphs separating all 4 real Huang-optimal cases from 7 obstructed graphs. A two-layer verification artifact accompanies the paper: 20 constructive, axiom-free Lean 4.36.0 theorems formalizing the parity, modular, lifting, and Sturm-isolation arithmetic kernel, paired with 16 zero-float Python certificates and 56 adversarial tests.

## Full Extracted Text

--- Page 1 ---
Torus-Holonomy Obstructions, Complex-vs-Real
Signing
Dichotomies, and Clifford-Cube Lifting Beyond
Huang
Lluis Eriksson∗
November 27, 2026
Abstract
Huang’s proof of the Sensitivity Conjecture rests on constructing a real±1signing S of
the hypercubeQn obeying the spectral involutionS2 = nI. We establish sharp topological,
algebraic, and spectral boundaries for extending Huang-optimal signingsS2 = dI—both real
symmetric (Sxy ∈{±1}) and complex Hermitian unitary (S∗= S, |Sxy|= 1)—to general
d-regular graphs and Cartesian products. First, we prove a universal complex torus-holonomy
no-go theorem: for any two non-bipartite regular graphsG and H,noHermitian unit-
modulus signingS of G□H over C satisfies S2 = (dG+ dH)I. Every odd-cycle discrete torus
C2a+1□C2b+1 ⊆G□H forces the product of its(2a+1)(2b+1)elementary4-cycle holonomies
to equal both(−1)(2a+1)(2b+1) = −1and+1(since every edge cancels with its conjugate
via SxySxy = |Sxy|2 = 1). For real ±1signings, v elementary-4-cycle-disjoint odd-cycle
tori enforce the quantitative Frobenius defect∥S2 −dI∥2
F ≥8v. On the Hamming graph
H(2,3) = K3□K3, exhaustive zero-float Faddeev–LeVerrier and Sturm isolation across all
210 = 1,024real switching classes (43distinct spectra) provesmin∥S∥op = 1+
√
17
2 >2 =
√
4
(characteristic polynomialx(x4 −9x2 + 16)2), maxλ5(S) = 1 <2(exact factor-2collapse on
5-vertex Cauchy interlacing), andmaxλ4(S) = 2(attained by −Aat ∥S∥op = 4). Second, we
establish a sharp complex-vs-real signing dichotomy on complete graphsKq: real symmetric
±1signings with S2 = ( q− 1)Iq force q≡ 2 ( mod 4)(symmetric conference matrices),
ruling out all oddq and allq≡ 0 ( mod 4), whereas purely imaginary Hermitian signings
Hq = iAq ∈{0,±i}q×q derived from skew-Hadamard matrices solveH2
q = (q− 1)Iq for
q∈{ 4,8,12,16,20,24,...} . Furthermore, the block-Clifford recurrenceSk+1 =
(Sk I
I−S k
)
preserves S2
k = ( d0 + k)I along G0□Qn without requiring G0 to be bipartite, certifying
∆((G0□Qn)[U]) ≥⌈√d0 +n⌉ for every induced subgraph with|U|>|V|/ 2across infinite
non-bipartite families seeded by conference, skew-Hadamard, and octahedron graphs. Third,
we compile an exhaustive zero-float switching-class atlas across11canonical regular graphs
separating all4real Huang-optimal graphs from7obstructed graphs. A two-layer verification
artifact accompanies the paper: Layer 1 formalizes the parity, modular, Clifford-lifting,
and Sturm-isolation arithmetic kernel in20constructive, axiom-free Lean 4.36.0 theorems
(0 sorry,0 Classical.choice); Layer 2 verifies all exhaustive switching-class enumerations,
skew-Hadamard/conference signings, and non-bipartite Clifford lifts in16zero-float Python
certificates and56adversarial tests.
1 Introduction
In his celebrated resolution of the Sensitivity Conjecture [7], Hao Huang constructed a real
symmetric ±1signing Sn of then-dimensional hypercubeQn satisfying S2
n = nI2n . Because Sn
∗Independent Researcher. Code, Lean 4.36.0 proofs, and zero-float certificates archived athttps://gith
ub.com/lluiseriksson/torus-holonomy-unitary-signings-beyond-huang (v1.0.0, MIT / CC-BY-4.0,
AIRR-FOUNDER-1.0). Manuscript and verification artifacts prepared with Google Antigravity assistance.
1

--- Page 2 ---
has zero trace and minimal polynomialx2 −n, its eigenvalues are+√n and −√n, each with
multiplicity2 n−1. By Cauchy’s interlacing theorem, every induced subgraph ofQn on2 n−1 + 1
vertices has maximum eigenvalue—and hence maximum degree—at least√n.
More generally, given ad-regular simple graphG= (V,E)on n= |V| vertices, aunitary
signing(or Hermitian unit-modulus signing [6, 11]) of G is a Hermitian matrixS∈C V×V
(S∗= S) supported onE with |Sxy|= 1for every {x,y}∈E and Sxy = 0otherwise. When
Sxy ∈{±1}on edges,S is areal signing. Becausetr(S2) = ∑
{x,y}∈E 2|Sxy|2 = nd, every unitary
signing satisfies∥S∥op ≥
√
d, with equality if and only if
S2 =dI n.(1)
We call a signing obeying(1) Huang-optimal. Since tr(S) = 0, any Huang-optimal signing forces
n to be even and has balanced spectrum{+
√
d
n/2
,−
√
d
n/2
}, yielding∆( G[U]) ≥⌈
√
d⌉for
every induced subgraphG[U]with |U|≥n/ 2 + 1via Cauchy interlacing (which holds identically
for Hermitian matrices overC). Equivalently,λ1(S[U]) ≤∆(G[U])follows from the triangle
inequality on the Perron–Frobenius bound for|S[U]|=A(G[U]).
Which regular graphs admit Huang-optimal signings overR or overC? Recent work has
investigated signed adjacency matrices of Hamming graphs, Cayley graphs, and Cartesian
products [1, 9, 4, 2], often using bipartiteness or real±1signings. In this paper we resolve three
structural questions with exact, zero-float algebraic proofs:
1. Universal Complex Torus-Holonomy No-Go on Non-Bipartite Products (Theo-
rem 1).Passing fromR to arbitrary unit-modulus complex phasesU(1) ⊂C cannotrescue
Cartesian productsG□H of two non-bipartite regular graphs: a discrete-torus holonomy
obstruction rules outS2 = dI unconditionally over all ofC, enforces a quantitative real
Frobenius defect∥S2 −dI∥2
F ≥8v, and onH(2,3) = K3□K3 produces exact spectral gaps
across all1,024real switching classes.
2. Complex-vs-Real Signing Dichotomy onKq and Non-Bipartite Clifford-Cube
Lifting (Theorem 2).On complete graphsKq, real±1Huang-optimal signings force
q≡ 2 ( mod 4)(symmetric conference matrices [3, 8, 5]), whereas allowing purely imaginary
weights {±i}from skew-Hadamard matrices [10] unlocks every skew-Hadamard order
q≡ 0 ( mod 4)( q = 4 ,8,12,16,20,24,... ). Moreover, the block-Clifford recurrence
Sk+1 =
(Sk I
I−S k
)
liftsanyreal or complex Huang-optimal seed G0 (even non-bipartite!) to
G0□Qn without bipartiteness, pinpointing the exact bipartite-vs-non-bipartite boundary
with Theorem 1.
3. Exhaustive Zero-Float 11-Graph Switching-Class Atlas (Theorem 3).Using
exact integer Faddeev–LeVerrier characteristic polynomials and exact rational Sturm
root isolation overQ, we exhaustively classify every real switching class of11canonical
regular graphs, separating the4Huang-optimal real graphs (K6,Q3,J(4,2),K 4,4) from7
obstructed graphs (K3,K4,K5,K3□K2,KG(5,2),C 5□K2,H(2,3)).
2 Universal Complex Torus-Holonomy Obstruction on Non-
Bipartite Products
Recall that the Cartesian productG□H of graphsG= (VG,EG)and H = (VH,EH)has vertex
set VG ×VH, with( u1,v1) ∼(u2,v2)iff either u1 = u2 and {v1,v2}∈E H, or{u1,u2}∈E G and
v1 =v2. IfGisd G-regular andHisd H-regular, thenG□Hisd-regular withd=d G +dH.
Theorem 1(Universal Complex Torus-Holonomy No-Go, Frobenius Defect, and ExactH(2,3)
Gap).Let G and H be regular graphs of degreesdG,dH ≥2that are both non-bipartite, and set
d:=d G +dH.
2

--- Page 3 ---
(a) Universal complex unitary impossibility:No Hermitian unit-modulus signingS of G□H
over C (indexed byVG ×VH) satisfiesS2 = dI. Equivalently, every unitary signingS of
G□Hobeys strict spectral excess∥S∥op >
√
d.
(b) Quantitative real Frobenius defect:If G□H contains v≥ 1odd-cycle discrete tori
C(r)
G □C(r)
H whose sets of elementary4-cycles are pairwise disjoint, then every real symmetric
±1signingSofG□Hsatisfies
∥S2 −dI∥2
F ≥8v >0.(2)
(c) Exact resolution ofH(2,3) = K3□K3:Exhaustive zero-float classification over all210 =
1,024real switching classes (43distinct spectra) of the4-regular9-vertex graph H(2,3)
certifies:
min
S∈SR(H(2,3))
∥S∥op = 1 +
√
17
2 ≈2.56155>2 =
√
4,(3)
max
S∈SR(H(2,3))
λ5(S) = 1<2 =
√
4,(4)
max
S∈SR(H(2,3))
λ4(S) = 2 =
√
4,(5)
where (3) is attained by a symmetric spectrum with characteristic polynomialx(x4 −9x2 +
16)2 = x(x2 −x− 4)2(x2 + x−4)2, and (5) is attained by the skewed signing−A(H(2,3))
with characteristic polynomial(x−2) 4(x+ 1) 4(x+ 4)(so∥S∥ op = 4).
Proof. Proof of(a).Suppose for contradiction that a Hermitian unit-modulus signing S of
G□H satisfies S2 = dI. Take any edgee= {u1,u2}∈E G and any edgef = {v1,v2}∈E H. In
G□H, the opposite vertices(u1,v1)and( u2,v2)are non-adjacent (since u1 ̸= u2 and v1 ̸= v2)
and possessexactcommon neighborhood {(u2,v1), (u1,v2)}of size2: any common neighbor
must differ from(u1,v1)in exactly one coordinate and from(u2,v2)in exactly one coordinate,
leaving only those two vertices. Hence the off-diagonal entry ofS2 = dI at(( u1,v1),(u2,v2))
reads
0 = (S2)(u1,v1),(u2,v2) =S(u1,v1),(u2,v1) S(u2,v1),(u2,v2) +S(u1,v1),(u1,v2) S(u1,v2),(u2,v2).(6)
Multiplying (6) by S(u1,v1),(u1,v2) S(u1,v2),(u2,v2) and using Hermiticity (Sxy = Syx) together with
unit modulus (|Sxy|2 = 1), we obtain the plaquette holonomy constraint
W(Ce,f) :=S (u1,v1),(u2,v1) S(u2,v1),(u2,v2) S(u2,v2),(u1,v2) S(u1,v2),(u1,v1) =−1.(7)
Because G and H are both non-bipartite,G contains an odd cycleCG = (u0,u1,...,u 2a,u0)
of lengthm1 = 2a+1and H contains an odd cycleCH = (v0,v1,...,v 2b,v0)of length m2 = 2b+1.
Consider the discrete torusCG□CH ⊆G□H , tiled by them1m2 = (2a+ 1)(2b+ 1)oriented
elementary4-cycles
Ci,j :=
(
(ui,vj)→(u i+1,vj)→(u i+1,vj+1)→(u i,vj+1)→(u i,vj)
)
(i∈Z m1 , j∈Z m2 ).
Taketheproductof W(Ci,j)overall( i,j) ∈Z m1 ×Zm2 . Everyhorizontaledge {(ui,vj),(ui+1,vj)}
appears exactly twice across the tiling: once oriented forward as the bottom edge ofCi,j and
once oriented backward as the top edge ofCi,j−1, contributingS(ui,vj),(ui+1,vj)S(ui+1,vj),(ui,vj) =
|S(ui,vj),(ui+1,vj)|2 = 1. Symmetrically, every vertical edge {(ui,vj),(ui,vj+1)}appears once
upward onCi−1,j and once downward onCi,j, contributing|S(ui,vj),(ui,vj+1)|2 = 1. Therefore
m1−1∏
i=0
m2−1∏
j=0
W(Ci,j) = 1.(8)
3

--- Page 4 ---
Figure 1:Universal complex torus-holonomy obstruction and exactH(2,3)spectral
gap.(a) Discrete torus C3□C3 tiled by9elementary4-cycles: every edge cancels with its
Hermitian conjugate (w¯w= |w|2 = 1), forcing ∏Wij = +1in contradiction to( −1)9 = −1
over all ofC. (b) Exhaustive switching-class separation onH(2,3) = K3□K3 (1,024classes,
43spectra): min-norm signing achieves ∥S∥op = 1+
√
17
2 > 2, skewed −A attains λ4 = 2at
∥S∥op = 4, whilemax Sλ5(S) = 1<2.
On the other hand, substituting (7) into the left-hand side of (8) yields
m1−1∏
i=0
m2−1∏
j=0
(−1) = (−1) (2a+1)(2b+1) =−1,(9)
since(2 a+ 1)(2b+ 1) = 4ab+ 2a+ 2b+ 1is odd. This yields −1 = 1, a contradiction. Since
tr(S2) = d|VG||VH|and S2 ̸= dI, at least one eigenvalue ofS2 strictly exceedsd, so∥S∥op >
√
d.
Proof of(b).For a real symmetric ±1signing S, every plaquette holonomy satisfiesW(Ci,j) ∈
{±1}. Within each odd-cycle torusC(r)
G □C(r)
H , the identity(8) forces an even number of+1
or −1plaquettes—specifically, since m1m2 is odd, at least one elementary4-cycleCer,fr must
have W(Cer,fr ) = +1. For that4-cycle, the two terms in (6) have the same sign ±1, so
|(S2)(u1,v1),(u2,v2)|= |(S2)(u2,v2),(u1,v1)|= 2. Distinct elementary4-cycles Ce,f correspond to
distinct unordered opposite-vertex pairs{(u1,v1),(u2,v2)}(the unique coordinate differences
recover e= {u1,u2}and f = {v1,v2}). Hence v elementary-4-cycle-disjoint odd-cycle tori yield
at least2vdistinct off-diagonal entries ofS 2 of magnitude2, giving∥S 2 −dI∥2
F ≥2v·2 2 = 8v.
Proof of(c).The graph H(2,3) = K3□K3 has |V| = 9, |E|= 18, and cycle-space dimension
β1 = 18 −9 + 1 = 10. Since diagonal sign conjugationS↦→DSD preserves eigenvalues, every
real ±1signing is spectrally equivalent to a signing fixed to+1on a spanning tree, yielding
210 = 1,024switching classes. Certificate cert11 computes the exact integer characteristic
polynomial of all1,024representatives via Faddeev–LeVerrier, finding exactly43distinct spectra,
and isolates min∥S∥op, maxλ5(S), and maxλ4(S)via exact rational Sturm counting with
multiplicity. The minimum operator norm is uniquely achieved by the symmetric polynomial
x(x4 −9x2 + 16)2 = x(x2 −x− 4)2(x2 + x−4)2, whose largest root is1+
√
17
2 ∈(5
2 ,26
10 )(Sturm-
certified byp(5/2) = −1/4 <0 <4/25 = p(26/10)for p(x) = x2 −x−4). The Cauchy-interlacing
median eigenvalueλ5(S)(governing5-vertex induced subgraphs via9 −5 + 1 = 5) never exceeds
1across all43spectra, whereas the skewed signing −A(H(2,3))has characteristic polynomial
(x−2) 4(x+ 1) 4(x+ 4), attainingλ 4 = 2 =
√
4while incurring∥S∥ op = 4.
4

--- Page 5 ---
3 Complex-vs-Real Signing Dichotomy onKq and Non-Bipartite
Clifford-Cube Lifting
Theorem 1 showed that complex phases cannot overcome the odd-cycle torus obstruction on
G□H. By sharp contrast, on complete graphsKq (single factors) and on productsG0□Qn with
a bipartite hypercube, moving from real{±1}to purely imaginary Hermitian{±i}signings
unlocks infinite new Huang-optimal families—and our Clifford-cube recurrence liftsarbitrary
non-bipartite seeds without requiring bipartiteness.
Recall that aq×q symmetric conference matrixC has0diagonal, ±1off-diagonal, C⊤= C,
and C2 = (q− 1)Iq [3, 5]; aq×q skew-Hadamard matrix W = Iq + Aq has A⊤
q = −Aq, zero
diagonal,±1off-diagonal, andA ⊤
q Aq = (q−1)I q [10].
Theorem 2(Real-vs-Complex Kq Signing Dichotomy and Non-Bipartite Clifford-Cube Lifting).
(a) Exact real vs. purely imaginary{±i}signing dichotomy onKq:A complete graph Kq
(q≥ 2) admits a real symmetric±1Huang-optimal signing S2 = (q−1)Iq if and only if
a symmetric conference matrix of orderq exists, which forcesq≡ 2 ( mod 4)(ruling out
every oddq and everyq≡ 0 ( mod 4), as well as non-sum-of-two-squares orders such as
q = 22by Belevitch’s theorem [3]). Conversely, for every skew-Hadamard orderq≡ 0
(mod 4)(in particular every Paley orderq= p+ 1with prime p≡ 3 ( mod 4), and doubling
orders such asq= 16), the purely imaginary Hermitian signing
Hq :=iA q ∈ {0,±i}q×q (10)
satisfies H∗
q = Hq and H2
q = (q−1)Iq, achieving the exact Huang spectrum±√q−1 (each
with multiplicityq/2) where no real±1signing exists. At q= 4, real signings are strictly
obstructed (maxSλR
2 = 1 <
√
3 and minS∥S∥R
op =
√
5>
√
3), whereasH4 = iA4 achieves
λC
2 =∥H4∥op =
√
3.
(b) Non-bipartiteClifford-cubelifting:Let G0 beany(not necessarily bipartite)d0-regular graph
(d0 ≥1) onm vertices admitting a Hermitian unit-modulus signingS0 with S2
0 = d0Im
(automatically m is even). Define recursively onGk := G0□Qk (m·2k vertices, degree
d0 +k) the block-Clifford signing
Sk+1 :=
(
Sk Im2k
Im2k −Sk
)
(k≥0).(11)
Then for everyn≥ 0, Sn is a Hermitian unit-modulus signing ofG0□Qn (strictly real
±1if S0 is real±1) satisfyingS2
n = (d0 + n)Im2n . Consequently, every induced subgraph
H= (G 0□Qn)[U]on|U|≥m·2 n−1 + 1vertices satisfies
∆(H)≥
⌈√
d0 +n
⌉
.(12)
Proof. Proof of(a).A real symmetric ±1signing S of Kq has zero diagonal and±1off-diagonal
entries, so S2 = ( q− 1)Iq is by definition the symmetric conference-matrix condition. If
q= 2k+1 ≥3is odd, any two distinct rows share2k−1off-diagonal columns, whose±1product
sum2 p−(2k−1)is odd and hence nonzero, ruling out all oddq. If q≥ 4is even, conjugate S
by a diagonal sign matrix so that row1hasS1j = +1for all j≥ 2. Orthogonality of row1with
rows2and3forces both rows to have exactly( q−2)/2entries equal to+1on their off-diagonal
positions outside column1. On the remainingq−3columns {4,...,q} , leta,b,c,e count the
sign pairs(+ ,+),(+,−),(−,+),(−,−)of rows2and3, and set δ:= 1if S23 = +1and δ:= 0
if S23 = −1. Then a+ b+ δ= a+ c+ δ= (q−2)/2and a+ b+ c+ e= q−3. Orthogonality
5

--- Page 6 ---
⟨r2,r3⟩= 0gives S21S31 + (a+ e) −(b+ c) = 0, i.e.,b+ c= a+ e+ 1, whenceb+ c= (q−2)/2.
Therefore2 a= (a+ b) + (a+ c) −(b+ c) = (q− 2) −2δ− (q− 2)/2 = (q− 2)/2 −2δ, which
rearranges toq= 4(a+ δ) + 2 ≡2 ( mod 4). Hence no real±1signing satisfies S2 = (q−1)Iq
for anyq≡0 (mod 4).
Over C, let Wq = Iq + Aq be any skew-Hadamard matrix of orderq≡ 0 ( mod 4), so
A⊤
q = −Aq,( Aq)rr = 0,( Aq)rc ∈{±1}for r̸= c, and A⊤
q Aq = (q− 1)Iq. Then Hq := iAq
satisfies H∗
q = (−i)A⊤
q = (−i)(−Aq) = iAq = Hq, has zero diagonal and unit-modulus entries±i
on every edge ofKq, and obeys
H2
q = (iAq)(iAq) =−A 2
q =A ⊤
q Aq = (q−1)I q.(13)
For every primep≡ 3 ( mod 4), the Paley skew-conference matrixAp+1 with border(+1 ,−1)
and Legendre core(r−c
p )supplies Hp+1 explicitly; forq= 16, skew-Hadamard doublingA16 =
( A8 W8
−W⊤
8 −A8
)
(using A8W8 = W8A8 since W8 = I8 + A8) givesH2
16 = 15I16 (verified overZ[i]in
Certificatecert12forq∈{4,8,12,16,20,24}).
Proof of(b).We proceed by induction on k≥ 0. The base casek = 0holds by hypothesis
(S∗
0 = S0 and S2
0 = d0Im). Given Sk on Gk = G0□Qk with S∗
k = Sk and S2
k = (d0 + k)Im2k ,
the block matrixSk+1 in (11) is supported precisely on the edges ofGk□K2 = G0□Qk+1 (two
copies ofGk linked by a perfect matching with weight+1), has unit-modulus entries on every
edge, satisfiesS∗
k+1 =Sk+1, and obeys
S2
k+1 =
(
Sk I
I−S k
)(
Sk I
I−S k
)
=
(
S2
k +I S k −Sk
Sk −Sk I+S 2
k
)
= (d0 +k+ 1)I m2k+1 .(14)
Notice that the off-diagonal cancellationSk −Sk = 0is purely algebraic andnever invokes
bipartiteness of G0. Finally, since tr(Sn) = 0and S2
n = (d0 + n)Im2n , the eigenvalues ofSn
are+ √d0 +n and −√d0 +n, each with multiplicitym·2n−1. For anyU⊆V (G0□Qn)with
|U|≥m·2 n−1 + 1, Cauchy interlacing for Hermitian matrices gives
∆(H)≥λ 1(A(H))≥λ 1(Sn[U])≥λ m2n−|U|+1 (Sn)≥λ m2n−1 (Sn) =
√
d0 +n,(15)
where λ1(Sn[U]) ≤∆(H)follows from the triangle inequality|⟨x,Sn[U]x⟩|≤⟨|x|,A (H)|x|⟩≤
∆(H)∥x∥2
2 for every unit vectorx∈C U. Since∆(H)is an integer, (12) follows.
Remark1 (Sharp Bipartiteness Boundary).Theorems 1 and 2(b) sharply delimit Huang-optimal
signings of Cartesian productsG□H: if both factors are non-bipartite,G□H admitsnoHuang-
optimal unitary signing overC; if one factor is a hypercubeQn (bipartite) and the other factorG0
admits a Huang-optimal signing (even non-bipartite, such asK4,K6,K8,J(4,2)), thenG0□Qn
inherits a Huang-optimal signing for alln≥ 0(verified explicitly overZ[i]for11lifts across4
non-bipartite seeds in Certificatecert14).
4 Exhaustive Zero-Float Switching-Class Atlas Across 11 Regu-
lar Graphs
Beyond H(2,3), we exhaustively classify all2β1 real switching classes of11canonical regular
graphs using strictly integer and rational arithmetic.
Theorem 3(Exhaustive 11-Graph Zero-Float Real Switching-Class Atlas).Across the11
canonicald-regular graphs listed in Table 1, exhaustive zero-float Faddeev–LeVerrier characteristic-
polynomial evaluation and rational Sturm root isolation over all2β1 real switching classes certify:
6

--- Page 7 ---
Figure 2:Complex-vs-real signing dichotomy onKq and non-bipartite Clifford-cube
lifting.(a) Exact Huang-optimal signings onKq (2 ≤q≤ 26): real symmetric±1conference
signings atq≡ 2 ( mod 4)(blue), purely imaginary Hermitian{±i}skew-Hadamard signings at
q≡ 0 ( mod 4)(purple), and real-obstructed orders (red crosses, including oddq and Belevitch
q= 22). (b) Certified spectral degree threshold√d0 +n along non-bipartite Clifford-cube lifts
G0□Qn forG 0 ∈{K4,J(4,2),K 6,K8}, strictly dominating Huang’s hypercube baseline√n.
(a) Four real Huang-optimal graphs (S2 = dI): K6 (β1 = 10,16distinct spectra, characteristic
polynomial( x2 −5)3), Q3 (β1 = 5,6spectra,( x2 −3)4), the non-bipartite octahedron
J(4,2) =K 2,2,2 (β1 = 7,14spectra,(x 2 −4) 3), andK4,4 (β1 = 9,10spectra,(x 2 −4) 4).
(b) Seven real-obstructed graphs (∥S∥op >
√
d for every real signing):K3 (min∥S∥op = 2,
maxλ2 = 1), K4 (
√
5,1), K5 (
√
5, maxλ3 = 1), the triangular prism K3□K2 (
√
5,
maxλ3 =
√
2), the Petersen graphKG(5,2)(
√
5, maxλ5 = 1), the pentagonal prism
C5□K2 (
√
5, maxλ5 ≈1.1756), andH(2,3) = K3□K3 (1+
√
17
2 , maxλ5 = 1, maxλ4 = 2).
Proof. For each connected graphG = (V,E), any two real±1signings with identical cycle
parities are diagonally sign-conjugate (S′= DSD) and hence cospectral [11]. Fixing+1on all
n−1edges of a spanning tree leavesβ1 = |E|−|V| + 1chord edges and exactly2β1 canonical
switching-class representatives. Certificatescert01–cert11 (summarized incert16) evaluate
det(xI−S ) ∈Z [x]via exact integer Faddeev–LeVerrier for every mask0≤m < 2β1 , verify
exact divisibility at every trace step, and apply squarefree-decomposed rational Sturm chains
to bracketmin∥S∥op and maxλ⌈n/2⌉(S)(as well as maxλ⌊n/2⌋(S)) to20bisection steps over Q,
plus direct integer matrix squaringS2 = dI on witnesses. All exact values and strict separations
in Table 1 follow directly from the certified rational brackets.
5 Formal Verification Architecture and Scope
To keep formal proof guarantees transparent and distinct from computational enumeration, our
verification artifact is organized in two layers:
• Layer 1 — Constructive Lean 4.36.0 Kernel(lean/TorusHolonomyUnitarySig
nings.lean ): Twenty theorems compiled with lean-DwarningAsError=true , zero
external dependencies, zerosorry, zerogrind, and zeroClassical.choice (audited via
#print axioms). Layer 1 machine-checks the odd-times-odd parity and universal torus-
holonomy contradiction(−1)(2a+1)(2b+1) ̸= 1( thm01–thm02), theKq modular obstructions
ruling out oddq and q = 4m (thm03–thm05), the Clifford-cube lifting scalar recurrence
and half-space vertex doubling (thm06–thm07), the exact spectral gap inequalities for
7

--- Page 8 ---
Table 1: Exhaustive zero-float real switching-class atlas across11canonicald-regular graphs
(Certificates cert01–cert11, cert16). Here kmed = ⌈n/2⌉is the Cauchy-interlacing index for
induced subgraphs of size>n/2.
GraphG n d β 1 2β1 Spectramin∥S∥ op maxλ⌈n/2⌉ RealS 2 =dI?
K3 3 2 1 2 2 2>
√
2 1No (oddn)
K4 4 3 3 8 3
√
5>
√
3 1No (Complex±i: Yes)
K5 5 4 6 64 7
√
5>2 1No (oddn)
K6 6 5 10 1,024 16
√
5
√
5Yes(PaleyC 6)
Q3 8 3 5 32 6
√
3
√
3Yes(Huang)
J(4,2) 6 4 7 128 14 2 2Yes(non-bipartite)
K4,4 8 4 9 512 10 2 2Yes(Hadamard)
K3□K2 6 3 4 16 6
√
5>
√
3
√
2No
PetersenKG(5,2) 10 3 6 64 6
√
5>
√
3 1No
C5□K2 10 3 6 64 12
√
5>
√
3≈1.1756No
H(2,3) =K 3□K3 9 4 10 1,024 43 1+
√
17
2 >2 1(λ 4 = 2) No (Complex no-go, Thm. 1)
Figure 3:Normalized spectral ratios across all11exhaustively classified regular
graphs.Red/green bars show min∥S∥op/
√
d (green = Huang-optimal realS2 = dI attained
on K6,Q3,J(4,2),K4,4); blue bars show the Cauchy-interlacing median ratiomaxλ⌈n/2⌉(S)/
√
d,
revealing the exact factor-2collapse onK5 and H(2,3)and1 /
√
3 collapse onK4 and Petersen.
K4,K3□K2, Petersen,C5□K2, andH(2,3)( thm08–thm12), the skewedH(2,3)spectral
moment identities and rational Sturm sign-change isolation ofx2 −x− 4( thm13–thm14),
the quantitative Frobenius defect bound8v≥ 8( thm15), and the skew-Hadamard Paley
orders, cycle-space dimensions, octahedron/K4,4 moments, lifted degree thresholds, and
exhaustive switching-class counts (thm16–thm20). The matrix-level plaquette cancellation,
Hermitian interlacing, and conference sign-counting derivations are proved in full detail in
Sections 2–3.
• Layer 2 — Zero-Float Exact Python Verifier(verification/verify_unitar
y_signings_huang.py ): An AST-audited pure standard-library verifier using strictly
int and fractions.Fraction (zero floating-point literals or calls, zero numeric division
or exponentiation, zerolimit_denominator ), emitting16SHA-256 certificates under
certificates/MANIFEST.json and validated by56adversarial pytest checks intests/
test_adversarial.py. Layer 2 independently executes exact integer Faddeev–LeVerrier
characteristic polynomials and squarefree rational Sturm isolation across all11graphs
(Certificates cert01–cert11, cert16), exactZ[i]Hermitian verification H2
q = (q− 1)Iq
8

--- Page 9 ---
for q∈ {4,8,12,16,20,24}(cert12), real Paley conference matrices C6,C14,C18,C30
(cert13),11non-bipartite Clifford-cube lifts G0□Qn across4seeds ( cert14), and direct
discrete-torus edge cancellation across5odd-by-odd tori (cert15).
References
[1] N. Alon and K. Zheng,Unitary signings and induced subgraphs of Cayley graphs ofZn
2 , Adv.
Comb.2020:12, 12 pp.
[2] F. Belardo, S. M. Cioabă, J. H. Koolen, and J. Wang,Open problems in the spectral theory
of signed graphs, Art Discrete Appl. Math.1(2018), #P2.10.
[3] V. Belevitch,Theory of2 n-terminal networks with applications to conference telephony,
Electr. Commun.27(1950), 231–244.
[4] D. Dong, N. Mani, and Y. Zhao,Enumeratingk-SAT functions, inProc. 32nd ACM–SIAM
Symp. on Discrete Algorithms (SODA), 2021, pp. 1362–1376.
[5] J. M. Goethals and J. J. Seidel,Orthogonal matrices with zero diagonal, Canad. J. Math.
19(1967), 1001–1010.
[6] K. Guo and B. Mohar,Hermitian adjacency matrix of digraphs and mixed graphs, J. Graph
Theory85(2017), 217–248.
[7] H. Huang,Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture, Ann.
of Math.190(2019), 949–955.
[8] R. E. A. C. Paley,On orthogonal matrices, J. Math. Phys.12(1933), 311–320.
[9] T. Tao,Twisted convolution and the Sensitivity Conjecture, blog post, July 2019,https:
//terrytao.wordpress.com/2019/07/26/.
[10] W. D. Wallis, A. P. Street, and J. S. Wallis,Combinatorics: Room Squares, Sum-Free Sets,
Hadamard Matrices, Lecture Notes in Mathematics, vol. 292, Springer, 1972.
[11] T. Zaslavsky,Signed graphs, Discrete Appl. Math.4(1982), 47–74.
9
