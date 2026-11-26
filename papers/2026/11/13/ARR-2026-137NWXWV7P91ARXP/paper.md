# Exact Optimal 3^k Generalized-Toffoli Decomposition, N-Independent Chebyshev Filters, and Minimax Advice for AC0 not subset BQAC0/qpoly

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-137NWXWV7P91ARXP` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/qac0-toffoli-chebyshev-sharp-bounds (`v1.0.0`)  
**Canonical PDF SHA-256:** `7964b6fcd3c36166583745126114dfaa5925e31109fa2f694569fbb5ef7b0af7`

## Abstract

We sharpen three core quantitative ingredients in the recent unconditional separation AC^0 not subset BQAC^0/qpoly of Sun and Wang (arXiv:2611.34803v1). First (Theorem A), we improve the product-projection L1-norm upper bound for k generalized Toffoli gates from 18^k to the exact optimal constant 3^k (a 6^k exponential sharpening) via disjoint-gate factorization, 2x2 diagonal cancellation (m=1), Cauchy-Schwarz (m=2), and a real XY-parity expansion with a sum-of-squares bound 27 - 16(1-s)(1+s)^3 = (2s-1)^2(4s^2+12s+11) >= 0 (m>=3), and we prove a matching universal lower bound >= 3^k over all real and complex product-projection decompositions via a multiplicative dual witness W^{otimes k} on CCZ^{otimes k}, reducing the backward layer-peeling exponent from 1 + ln 18 < 4 to 1 + ln 3 < 2.1. Second (Theorem B), retaining the 1/r! prefix and 1/(R-r) scaling in the Chebyshev filter removes the spurious ln N factor from the degree completely (64.9x smaller at N=10^9, R=100, r=10) and collapses ln mu_N(q) from quadratic to linear in ln N (78.2x smaller analytically, 78.3x with exact prefix sum at N=10^9). Third (Theorem C), we establish the unique minimax optimal advice bias a* = M/(2M-1) and repair a clause-vs-literal conflation on H_n (M(H_n) <= n clauses rather than 3n), boosting the classical-advice advantage from 1/(12n) to >= 1/(4n-2). The algebraic cores are constructively formalized in Lean 4.35.0 (20 theorems, 0 sorry, 0 Classical.choice, 0 warnings), backed by an AST-audited zero-float exact rational verifier, 16 SHA-256 certificates (QAC0-SHARP-CERT-1.0), and 51/51 passing tests.

## Full Extracted Text

--- Page 1 ---
Exact Optimal3 k Generalized-Toffoli Decomposition,
N-Independent Chebyshev Filters, and Minimax
Advice forAC 0 ̸⊆BQAC 0/qpoly
Lluis Eriksson∗
November 2026
Abstract
Sun and Wang [5] recently established the unconditional separationAC0 ̸⊆BQAC 0/qpoly
via advice-independent operator-norm Pauli approximation, building on product-projection lo-
calization [3, 1, 2]. Three quantitative pillars govern their backward layer-peeling proof and
classical-advice comparison: (i) a single-layer generalized-Toffoli product-projection expansion
withℓ 1 weight18 k (Lemma 3.3), (ii) a Chebyshev integer-spectrum filter of degree11
√
Rrln Λ0
and weighted log-norm11
√
Rrln 2 Λ0 withΛ 0 = 2 +N+R(Lemma 3.4), and (iii) a classical
randomized-advice protocol achieving worst-case advantage≥1/(12n)on the monotone universal
selector CNFHn (Section 1.2).
We establish three sharp improvements to these bounds.Theorem Areduces the single-layer
generalized-Toffoliℓ1 product-projection weight from18k to theexact optimal constant3 k—an
exponential6 k sharpening—via disjoint-gate tensor factorization, exact2×2spectral diagonal
cancellation (m= 1), and a realXY-parity expansion bounded by the sum-of-squares identity
27−16(1−s)(1 +s) 3 = (2s−1) 2(4s2 + 12s+ 11)≥0(m≥2). We prove a matching universal
lower bound≥3 k over all real and complex linear combinations of product projections using
the explicit multiplicative dual witnessW⊗k withW= diag(0,1,1,−1,0,0,−1,1)onCCZ ⊗k.
This cuts the backward peeling exponent in Section 3.4 from1 + ln 18<4to1 + ln 3<2.1.
Theorem Beliminates the spuriouslnNdependence from the Chebyshev filter degree by re-
tainingthedropped1/r!prefixfactorand1/(R−r)scalingofφ, yieldinganN-independentdegree
degq=r+⌈ 1
2
√
Rr(4+ln(R/r)+ ln 2
r )⌉(64.9×smaller atN= 10 9,R= 100,r= 10) and collapsing
lnµN (q)from quadraticln 2 Λ0 to linearln(R/r) ln(N/R)(78.2×smaller analytically,78.3×with
exact prefix sum atN= 109).Theorem Cdetermines the unique minimax-optimal classical ad-
vice biasa∗ =M/(2M−1)(strictly beating1/2+1/(4M)for everyM≥1) and identifies a clause-
versus-literal conflation in Section 1.2 of [5]:Hn has at mostM(Hn) =n− ∑ mw ≤nclauses
rather than3n, boosting the guaranteed classical-advice advantage from1/(12n)to≥1/(4n−2)
(>3×, and≈4×asymptotically).
All 20 core algebraic, sum-of-squares, 27-corner Bloch-projection dual-bound, Chebyshev re-
currence, and minimax-optimality statements are formalized constructively in Lean 4.35.0 (0
sorry,0warnings, zeroClassical.choice); the operator-level Hilbert-space lifting is proved
analytically in the text and audited on exact rational8×8,32×32, and64×64matrices by an
AST-audited zero-float Python verifier (QAC0-SHARP-CERT-1.0, 16 SHA-256 certificates, 51/51
pytest checks).
1 Introduction
The recent resolution ofPARITY/∈BQAC 0 via product-projection localization [3, 1, 2] opened
a new analytical pathway for constant-depth quantum circuits with unbounded fan-in generalized
Toffoli gates (QAC0). Sun and Wang [5] lifted this localization framework via Pauli twirling and
backward layer peeling to prove an advice-independent operator-norm Pauli-degree approximation
∗Independent Researcher. Code, Lean 4 proofs, and certificates: MIT License; manuscript and figures: CC-BY-4.0.
Repository:https://github.com/lluiseriksson/qac0-toffoli-chebyshev-sharp-bounds.
1

--- Page 2 ---
Table 1: Summary of sharp improvements to Sun & Wang [5] (arXiv:2611.34803v1).
Quantity Sun & Wang [5] This Work (Exact / Sharp) Gain
Lemma 3.3ℓ1 weight18 k 3k (exact optimum, LB=UB)6 k exponential
Sec. 3.4 peeling exp.e 4sj−1 (1+ln 18<4)e 2.1sj−1 (1+ln 3<21/10)1.90×exponent
Lemma 3.4degq11
√
Rrln(2+N+R)r+⌈ 1
2
√
Rr(4+ln R
r + ln 2
r )⌉NolnN;64.9×(N=10 9)
Lemma 3.4lnµ N (q) 11
√
Rrln 2 Λ0 O(
√
Rrln R
r ln(7+ 8N
R ))LinearlnN;78.2×(N=10 9)
Sec. 1.2 bias (Mcl.)a SW = 1
2 + 1
4M a∗ = M
2M−1 (unique minimax)+ 1
4M(2M−1) (2×atM=1)
Sec. 1.2Hn clauses≤3n(literal bound)M(H n) =n−
∑
mw ≤n >3×(≈4×asymp.)
(Theorem 1.2 of [5]), yieldingAC0 ̸⊆BQAC 0/qpolythrough a linear-sizeP-uniform monotone uni-
versal selector CNFHn built atop Sherstov’s approximate-degree lower bound [4].
Although the asymptotic separationAC 0 ̸⊆BQAC 0/qpolyholds for any constant exponential
base in single-layer Toffoli expansion and any polylogarithmic overhead in Chebyshev filtering, the
concrete constants directly control the backward peeling recurrence (sj = 4sj−1 +b(rj)in Section 3.4
of [5]), the crossover input sizem 0(d,κw,α,η), and the quantitative gap between classical and
quantum advice onHn. Inspecting the proof architecture of [5] reveals three substantial, structurally
independent inefficiencies—each admitting a clean, sharp, elementary repair:
1.Single-layer Toffoli expansion (Lemma 3.3 of [5], cf. [1, 2]):ExpandingG†KGby multi-
plying out∑
S,T⊆G(−2)|S|+|T|ΠSKΠT (weight9 k) and applying four-phase complex polarization
on every qubit ofsuppK(weight2 k) yielded18 k. This misses two structural facts: disjoint
gates factor completely as a tensor product, and within each gate the diagonal4ΠgKgΠg cancels
against−2(Π gKg +KgΠg)form= 1while higher-overlap terms admit a realXY-parity expan-
sion. We prove the exact optimal constant is3k, matching a constructive dual lower bound≥3k
(Theorem 1).
2.Chebyshev integer-spectrum filter (Lemma 3.4 of [5]):Bounding| ∏r
j=1(1−x/j)| ≤
(1 +R) r discarded1/r!, forcingh=⌈4
√
Rrln Λ0⌉to grow withlnNeven though the filter
q(x)is purely a function of(R,r). Simultaneously, boundingµ N(φ)≤3 + 2Ndiscarded the
1/(R−r)≤2/Rdenominator, inflatinglnµ N(q)to11
√
Rrln 2 Λ0. Retaining both factors removes
lnNfromdegqentirely and collapseslnµ N(q)to linear inln(N/R)(Theorem 3).
3.Classical-advice benchmark onH n (Section 1.2 of [5]):Sampling a uniform clause with
biasa= 1
2 + 1
4M leaves 1-input acceptance (1
2 + 1
4M) strictly below 0-input rejection (1
2 + 1
4M+ 1
4M2 ).
Moreover, Section 1.2 bounds the clause count ofHn by its literal-occurrence bound3n, whereas
by Section 4.2 each clause ofHn uses a dedicated selector or unused variable, soM(H n) =
n− ∑
wmw ≤n. Equalizing at the unique minimax optimuma ∗ =M/(2M−1)boosts the
classical-advice advantage from1/(12n)to≥1/(4n−2)(Theorem 4).
Table 1 summarizes the improvements alongside their Lean 4.35.0 and certificate coverage.
2 Theorem A: Exact Optimal3 k Generalized-Toffoli Expansion
Recall that a product projection onNqubits is an orthogonal projectorK= ⨂N
i=1 Ki where each
Ki is eitherI 2 or a rank-1 single-qubit projector, with supportsuppK={i∈[N] :K i ̸=I 2}.
A single layerGof pairwise disjoint generalized Toffoli gates (preceded and followed by arbitrary
single-qubit unitaries) conjugatesKbyG †KG. Single-qubit unitaries preserve product projections
and|suppK|, so it suffices to analyze a layerG= ∏
g∈G(I−2Π g)of pairwise disjoint multi-qubit
reflections where eachΠg is a product projection.
Theorem 1(Exact Optimal Generalized-Toffoli Product-Projection Bound).LetKbe anN-qubit
product projection with|suppK|=k≥1, and letGbe a single layer of pairwise disjoint generalized
Toffoli gates preceded and followed by arbitrary single-qubit unitaries.
2

--- Page 3 ---
1.Tight Upper Bound:G †KGadmits a real linear combination of product projectionsG†KG=∑
ιcιPι (cι ∈R) with totalℓ 1 weight
∑
ι
|cι| ≤
∏
g∈G
Wmg ≤3 k,(1)
whereGis the set of gates intersectingsuppK,m g =|supp Π g ∩suppK|≥1( ∑
g∈Gmg ≤k),
and each gate contributes at mostW1 ≤3,W 2 ≤9, andW m ≤7 + 2(3
√
3/4)m <3 m for every
m≥3.
2.Matching Universal Lower Bound:For everyk≥1, onN= 3kqubits withG= CCZ ⊗k
andK= (|+⟩⟨+|⊗I 2 ⊗I2)⊗k (|suppK|=k),everyreal or complex linear combinationG †KG=∑
ιcιPι of3k-qubit product projections satisfies
∑
ι
|cι| ≥3k.(2)
Proof. Part 1 (Upper bound).Gates disjoint fromsuppKcommute withKand cancel inG †KG.
Because the remaining gatesg∈Gact on pairwise disjoint qubit subsets, the conjugation factors
exactly across gates:
G†KG=

⨂
g∈G
(I−2Π g)Kg(I−2Π g)

⊗Krest,
whereK g is the restriction ofKtosupp Π g andK rest is a product projection ofℓ1 weight1. By
multiplicativity of theℓ1 product-projection norm under tensor products, it suffices to prove that
a single gategwith overlap sizem=|supp Π g ∩suppK|≥1admits a real product-projection
expansion ofℓ1 weight at most3m.
WriteΠ g = Πin ⊗Πout andKg =Kin ⊗Iout relative to the partition ofsupp Πg into themoverlap
qubitsS g = supp Πg ∩suppKand the exterior qubitssupp Π g \Sg. On eachi∈S g, let(Π g)i =
|ai⟩⟨ai|and(K g)i =|w i⟩⟨wi|. Choosing global phases on|wi⟩so thatc i :=⟨a i|wi⟩∈[0,1], write
|wi⟩=c i|ai⟩+s i|a⊥
i ⟩withs i =
√
1−c 2
i ∈[0,1]and⟨a i|a⊥
i ⟩= 0. Expanding(I−2Π g)Kg(I−2Π g)
yields
(I−2Π g)Kg(I−2Π g) =Kin ⊗Iout +
(
4ΠinKinΠin −2(Π inKin +KinΠin)
)
⊗Π out.(3)
The first termK in ⊗Iout is a single product projection of weight1. We analyze the bracketed
operatorM g on themqubitsS g by cases:
Casem= 1(Exact2×2diagonal cancellation):In the orthonormal basis{|a 1⟩,|a⊥
1 ⟩},
we haveΠ in = diag(1,0)andΠ inKin +KinΠin =
(
2c2
1 c1s1
c1s1 0
)
, so the diagonal entry4c2
1 cancels
identically:
Mg = 4c2
1
(
1 0
0 0
)
−2
(
2c2
1 c1s1
c1s1 0
)
=−2c1s1
(
0 1
1 0
)
= 2c1s1
(
|ϕ−⟩⟨ϕ−|−|ϕ +⟩⟨ϕ+|
)
,
where|ϕ ±⟩= (|a 1⟩±|a ⊥
1 ⟩)/
√
2. Hence (3) expands into three product projections with totalℓ1
weight
W1(c1) = 1 + 4c1s1 = 3−2(c 1 −s1)2 ≤3 = 3 1,
with equality if and only ifc1 =s1 = 1/
√
2(Lean 4 Theorems 1–2).
Casem≥2(RealXY-parity expansion):Notice thatΠ inKinΠin = (∏m
i=1 c2
i)Πin is a single
product projection of weight4∏m
i=1 c2
i, while the cross term satisfies
ΠinKin +KinΠin =
(m∏
i=1
ci
)(m⨂
i=1
|ai⟩⟨wi|+ h.c.
)
.
3

--- Page 4 ---
On each qubiti∈S g, define the two Hermitian operators
Xi :=|ai⟩⟨wi|+|w i⟩⟨ai|, Y i :=−i
(
|ai⟩⟨wi|−|w i⟩⟨ai|
)
,
so|a i⟩⟨wi|= 1
2 (Xi +iYi). Direct2×2diagonalization givesspec(X i) ={ci + 1,ci −1}(trace norm
|1 +ci|+|1−c i|= 2) andspec(Y i) ={+si,−si}(trace norm2s i). EachXi andYi therefore expands
into two rank-1 orthogonal projectors with real weights summing to2and2si, respectively. Taking
the real part of the tensor product gives
m⨂
i=1
|ai⟩⟨wi|+ h.c.= 1
2m−1
∑
S⊆Sg
|S|even
(−1)|S|/2

⨂
i/∈S
Xi ⊗
⨂
i∈S
Yi

.
Summing theℓ1 product-projection weights of each parity term yields
1
2m−1
∑
S⊆Sg
|S|even
2m ∏
i∈S
si =
m∏
i=1
(1 +si) +
m∏
i=1
(1−s i).
Multiplying by2 ∏m
i=1 ci and adding1 + 4 ∏m
i=1 c2
i bounds the total single-gate weight by
Wm(c1,...,c m) = 1 + 4
m∏
i=1
c2
i + 2
m∏
i=1
ci(1 +si) + 2
m∏
i=1
ci(1−s i).(4)
Form= 2, expanding2(1 +s 1)(1 +s2) + 2(1−s1)(1−s 2) = 4(1 +s1s2)and using Cauchy–Schwarz
c1c2 +s1s2 ≤1together withc 1c2 ≤1gives
W2 = 1 + 4c1c2(1 +c1c2 +s1s2)≤1 + 4·1·(1 + 1) = 9 = 3 2
(Lean 4 Theorems 3–4). Form≥3, every factor satisfies the exact sum-of-squares identity
27−16
(
ci(1 +si)
)2 = 27−16(1−s i)(1 +si)3 = (2si −1) 2(4s2
i + 12si + 11)≥0,
whencec i(1 +s i)≤3
√
3/4<3/2for alls i ∈[0,1](Lean 4 Theorem 5). Becausec i ≤1and
ci(1−s i)≤1, Eq. (4) givesW m ≤1 + 4 + 2(3
√
3/4)m + 2<7 + 2(3/2) m <3 m for everym≥3
(basem= 3:7 + 27/4 = 55/4<27; inductive step multiplies the left side by<3while multiplying
3m by3; Lean 4 Theorem 6). Thus every gate satisfiesWmg ≤3 mg , proving (1).
Part 2 (Matching lower bound via multiplicative dual witness).LetA:= CCZ(|+⟩⟨+|⊗I 2 ⊗
I2)CCZon 3 qubits. In the orthonormal product basisB={|+⟩,|−⟩}⊗{|0⟩,|1⟩}⊗{|0⟩,|1⟩},A
is diagonal with entries(1,1,1,0,0,0,0,1). Define the Hermitian operatorWdiagonal inBwith
diagonal entries
W= diag B(0,1,1,−1,0,0,−1,1).(5)
Directly,Tr(WA) = 0+1+1+0+0+0+0+1 = 3(Lean 4 Theorem 8). Now letP=P 1 ⊗P2 ⊗P3 be
any3-qubit product projection (arbitrary complex rank-1 Bloch-sphere projectors orI2). Because
Wis diagonal inB,Tr(WP)depends solely on the diagonal pairs(p j,qj)ofP j in thej-th factor
basis ofB. EitherP j =I 2, giving(p j,qj) = (1,1), orrank(P j) = 1, giving(p j,qj) = (tj,1−t j)
for somet j ∈[0,1]. SinceTr(WP)is trilinear in(p 1,q1),(p2,q2),(p3,q3), its extrema over all
product projections lie at the33 = 27corners{(1,1),(1,0),(0,1)} 3, where direct inspection (Lean 4
Theorems 9–10) establishes|Tr(WP)|≤1everywhere.
For generalk≥1, setW k :=W ⊗k on3kqubits. For every3k-qubit product projectionP=⨂k
r=1 P(r), multiplicativity of the trace gives|Tr(WkP)|= ∏k
r=1 |Tr(WP (r))|≤1. Therefore any
real or complex expansionA⊗k = ∑
ιcιPι obeys
3k =
(
Tr(WA)
)k =
⏐⏐Tr(WkA⊗k)
⏐⏐=
⏐⏐⏐⏐⏐
∑
ι
cιTr(WkPι)
⏐⏐⏐⏐⏐≤
∑
ι
|cι|·|Tr(W kPι)|≤
∑
ι
|cι|,
completing the proof (the real/integer dualℓ1 inequality is formalized in Lean 4 Theorem 11, while
complex-coefficient triangle inequality andk-fold tensor multiplicativity follow analytically above).
4

--- Page 5 ---
Figure 1:Theorem A visual audit.(a) Exponential6k sharpening from Sun & Wang’s18k to the
exact optimal constant3k, alongside the single-gatem=koverlap bound7 + 2(3
√
3/4)k. (b) Exact
m= 1weight1 + 2 sin(2θ), matching theCCZdual witnessLB = UB = 3atθ= 45 ◦ (C01), the
3-4-5Pythagorean certificateℓ 1 = 73/25(C02), and the 2-qubitCZoptimum2(C03).
Remark2 (Two-qubit vs. three-qubit threshold and backward peeling impact).On 2 qubits, the
expansionCZ(|+⟩⟨+|⊗I 2)CZ =|+⟩⟨+|⊗|0⟩⟨0|+|−⟩⟨−|⊗|1⟩⟨1|attainsℓ 1 weight2<3(Cer-
tificateC03) becauseI 2 −|1⟩⟨1|=|0⟩⟨0|is a single product projection; three qubits (CCZ) is the
exact threshold at whichI−Π out ceases to be a single product projection and theℓ1 optimum
jumps to3. Moreover, sincee 11/10 >3(certified by degree-6 Taylor truncation in Lean 4 Theo-
rem 15), the single-layer peeling weight bound in Section 3.4 of [5] drops fromesj−1 18sj−1 ≤e4sj−1
toe sj−1 3sj−1 < e2.1sj−1 ; ensuring the single-step error conditione2.1sj−1−2rj ≤e −2sj−1 (replacing
e4sj−1−2rj ≤e−2sj−1 in [5]) reduces the required filter order fromrj ≥3sj−1 tor j ≥2.05sj−1.
3 Theorem B:N-Independent Chebyshev Integer-Spectrum Filter
For a real polynomialq(x) =∑
j qjxj, recall Sun and Wang’sN-weighted coefficient normµN(q) =∑
j |qj|Nj, which obeysµ N(pq)≤µ N(p)µN(q)and bounds theℓ 1 product-projection weight of
q(D)for anyN-qubit mismatch counterD. Lemma 3.4 of [5] constructedq(x) =
(∏r
j=1(1−
x/j)
)
Th(φ(x))/Th(φ(0))withφ(x) = (R+r−2x)/(R−r), obtainingdegq≤11
√
Rrln Λ0 and
lnµN(q)≤11
√
Rrln 2 Λ0 whereΛ 0 = 2 +N+R. Both bounds carry avoidable width penalties that
we remove completely.
Theorem 3(N-Independent Chebyshev Filter and Linear-lnNCoefficient Norm).LetN,R,rbe
positive integers with1≤r≤R/2. Set
h=


1
2
√
Rr
(
4 + ln R
r
)
+ ln 2
2
√
R
r


, q(x) =


r∏
j=1
(
1− x
j
)
Th(φ(x))
Th(φ(0)) ,(6)
whereφ(x) = (R+r−2x)/(R−r). Thenq(0) = 1,|q(j)|≤e −3r for allj∈{1,...,R}, and:
1.N-independent degree:
degq=r+h≤ 1
2
√
Rr
(
4 + ln R
r
)
+r+ ln 2
2
√
R
r + 1,(7)
which haszero dependenceon the circuit widthN.
5

--- Page 6 ---
2.Linear-in-ln(N/R)weighted log-norm:Settingµ φ :=µN(φ) = R+r+2N
R−r ≤3 + 4N
R ,
lnµN(q)≤rln
(
e+ eN
r
)
+hln
(
µφ +
√
µ2φ + 1
)
−2h
√ r
R + ln 2
=O
(√
Rrln R
r ln
(
7 + 8N
R
))
.(8)
Proof.Clearlyq(0) = 1andq(j) = 0forj∈{1,...,r}. Forx∈(r,R], we haveφ(x)∈[−1,1], so
|Th(φ(x))|≤1. Rather than discarding the denominatorsjas in [5] (which gave(1 +R) r), observe
that0<x−j≤R−j <Rfor every1≤j≤r(Lean 4 Theorem 14), and by the elementary series
bounde r >rr/r!we haver!>(r/e) r, hence
⏐⏐⏐⏐⏐⏐
r∏
j=1
(
1− x
j
)⏐⏐⏐⏐⏐⏐
= 1
r!
r∏
j=1
(x−j)< Rr
(r/e)r =
(eR
r
)r
.
Withξ=
√
r/R∈(0,1/
√
2],φ(0) = (1 +ξ 2)/(1−ξ 2) = cosh(ln 1+ξ
1−ξ)andln 1+ξ
1−ξ ≥2ξ, soT h(φ(0))≥
1
2 e2h
√
r/R. Choosinghas in (6) ensures2h
√
r/R≥r(4 + ln(R/r)) + ln 2, giving
|q(x)|≤2
(eR
r
)r
e−2h
√
r/R ≤er(1+ln(R/r))+ln 2−r(4+ln(R/r))−ln 2=e−3r,
withdegq=r+hcompletely independent ofN.
For (8), retaining the denominatorR−r≥R/2inφ(x) = R+r
R−r − 2
R−rxyieldsµ φ = R+r+2N
R−r ≤
3 +4N
R (Lean 4 Theorem 13, strictly sharper than3 + 2Nfor allR≥3). Letaj :=µN(Tj(φ)). From
Tj+1(z) = 2zTj(z)−T j−1(z)and submultiplicativity,a 0 = 1,a 1 =µ φ, andaj+1 ≤2µ φaj +aj−1.
Writingu:= arsinh(µ φ) = ln(µφ +
√
µ2φ + 1), the linear recurrenceb0 = 1,b1 =µφ,bj+1 = 2µφbj +
bj−1 has the exact closed formbh =|T h(iµφ)|= 1
2
(
ehu + (−1)he−hu)
(i.e.cosh(hu)for evenhand
sinh(hu)for oddh), soa h ≤b h ≤cosh(hu)≤e hu = (µφ +
√
µ2φ + 1)h <(2µ φ + 1)h (the coarser
integer-parameter recurrence boundbh ≤(2y+ 1) h is formalized in Lean 4 Theorem 12, while the
tightere hu bound used in (8) follows analytically here). For the prefix, sincet↦→ln(1 +N/t)is
decreasing on(0,∞)andln(1 +u)≤uforu>0,
ln
r∏
j=1
(
1 + N
j
)
≤
∫r
0
ln
(
1 + N
t
)
dt=rln
(
1 + N
r
)
+Nln
(
1 + r
N
)
≤rln
(
1 + N
r
)
+r=rln
(
e+ eN
r
)
.
Dividing byTh(φ(0))≥ 1
2 e2h
√
r/R completes (8). (The exact rational product∏r
j=1(1 +N/j)and
full expandedµN(q)are directly verified in CertificatesC09–C10.)
4 Theorem C: Minimax Classical Advice and Exact Clause Count
ofH n
In Section 1.2 of [5], the authors contrast their quantum-advice lower bound with a constant-depth
O(n)-width circuit using randomized classical advice on anyM-clause CNF: the advice samples a
uniformly random clause together with an independent coinC∈{0,1}withPr[C= 1] =a, and the
circuit outputs1iff the sampled clause is satisfied andC= 1. Every1-input satisfies allMclauses
and is accepted with probabilitya, while every0-input falsifies at least one clause and is rejected
with probability at least1−a(1−1/M).
Sun and Wang selectedaSW = 1
2 + 1
4M and stated: “SinceH n has at most3nclauses, this
achieves worst-case advantage at least1/(12n).” We sharpen both the bias choice and the clause
count.
6

--- Page 7 ---
Figure 2:Theorem B visual auditat fixed(R,r) = (100,10)across widthsN∈[10 2,10 9].
(a)degq= 111is strictly constant inN, versus Sun & Wang’s11
√
Rrln Λ0 (64.9×larger at
N= 10 9). (b)lnµ N(q)grows only linearly inln(N/R), cutting the quadraticln2 Λ0 bound by78.3×
with the exact prefix sum (78.2×via the analytic bound (8)) atN= 109.
Theorem 4(Unique Minimax Advice Bias and Exact Clause Count ofHn).
1.Unique minimax bias:ForM≥1, the worst-case successS M(a) := min(a,1−a(1−M −1))
on[0,1]attains its unique global maximum at
a∗ = M
2M−1 = 1
2 + 1
4M−2 ,(9)
yielding worst-case advantagea∗−1
2 = 1
4M−2 and strictly dominatingaSW = 1
2 + 1
4M by
a∗−aSW = 1
4M(2M−1) >0 (∀M≥1).
In particular,a∗= 1(deterministic,2×advantage) atM= 1anda ∗= 2/3(+33.3%advantage
over5/8) atM= 2.
2.Exact clause count of the universal selector CNFHn:Under the disjoint-block allocation
of Section 4.2 of [5] (Bw =⌊n/2 w⌋, where active blocks allocatemw input variables andMw =
(mw + 1)w selector variables withmw +Mw ≤Bw, plus|Un|=n− ∑
w(mw +Mw)unused unit
clauses), the exact number of clauses ofHn is
M(Hn) =
∑
wactive
Mw +|Un|=n−
∑
wactive
mw ≤n,(10)
with strict inequalityM(Hn)<nfor everyn≥6(and asymptoticallyM(H n)≤ 3
4 n+O(1)from
blockw= 1alone, sincem 1 =⌊(B 1 −1)/2⌋=⌊n/4⌋−O(1)). Consequently, the randomized
classical-advice protocol achieves worst-case advantage onHn at least
1
4M(Hn)−2 ≥ 1
4n−2 > 3
12n (11)
for everyn≥1(>3×Sun & Wang’s1/(12n), and≈4×for largen).
Proof.For Part 1,a↦→ais strictly increasing whilea↦→1−a(1−1/M)is nonincreasing (strictly
decreasing forM≥2). Their unique intersection on[0,1]solvesa= 1−a(1−1/M)⇐⇒a(2−
1/M) = 1⇐⇒a=M/(2M−1); atM= 1,1−a·0 = 1somin(a,1) =ais uniquely maximized
on[0,1]ata ∗ = 1(Lean 4 Theorems 16–18). Subtracting gives M
2M−1 −2M+1
4M = 4M2−(4M2−1)
4M(2M−1) =
1
4M(2M−1) >0.
7

--- Page 8 ---
Figure 3:Theorem C visual audit.(a) Worst-case success probabilitymin(a,1−a(1−1/M))
forM∈{2,4}, illustrating unique minimax equalization ata ∗=M/(2M−1)strictly abovea SW.
(b)Exactadvantageratioadv ∗(Hn)/(1/12n)acrossn∈[6,10 4], exceedingtheuniversal3×threshold
everywhere and converging to≈4×becauseM(H n)≈0.75n(C15–C16).
For Part 2, by Eq. (19) of [5], each clause ofHmw,w(x(w),y(w))is indexed bijectively by a distinct
selector variabley⃗ℓ (Mw = (mw + 1)w clauses per active blockw), while each unused indexi∈Un
contributes one unit clausezi. Because the active blocks andUn partition[n], ∑
w(mw+Mw)+|Un|=
n, immediately giving (10) (Lean 4 Theorem 19). By contrast,3nis the width-(w+ 1)upper bound
on totalliteral occurrences≤ ∑
w(w+ 1)Mw +|Un|≤3n(omitting zero entries in Eq. (19) of [5]
leaves ∑
w(Mw +wmw(mw + 1)w−1) +|Un|literals), not the clause count. SubstitutingM(Hn)≤n
into 1
4M−2 yields (11) (Lean 4 Theorem 20).
5 Constructive Lean 4.35.0 Formalization and Zero-Float Audit
To guarantee machine-checked rigor while maintaining full transparency regarding formalization
boundaries, we pair a pure-core Lean 4.35.0 kernel with an AST-audited zero-float rational Python
verifier (QAC0-SHARP-CERT-1.0):
•Lean 4.35.0 Kernel (lean/Qac0SharpCert.lean, 20 theorems, 0sorry, 0 warnings):
Uses only Lean 4 core (Int,Nat,Fin,List) withzeroClassical.choiceacross all 20 theorems
(axiomsstrictly⊆{propext,Quot.sound}). Specifically: Theorems1–7provethem= 1diagonal
cancellation identity and equality iff, circle Cauchy–Schwarz,m= 2boundW 2 ≤9, degree-4
sum-of-squares certificate27q 4 −16(q−s)(q+s) 3 = (2s−q) 2(4s2 + 12sq+ 11q 2), universal
m≥3induction7·2 m + 2·3 m <6 m, and18 k = 6 k3k; Theorems 8–11 proveTr(WA) = 3,
the 27-corner check, the universal scaled Bloch-sphere bound|Tr(WP)|≤Q3 for all single-qubit
diagonals(Q,Q)and(t,Q−t), and the dualℓ 1 lower-bound inequality; Theorems 12–15 prove
the Chebyshev recurrence bound, strictµN(φ)sharpening, falling-product bound, ande11/10 >3;
Theorems 16–20 prove unique minimax optimality ofa∗,M(H n)≤n, and the>3×advantage
bound. Analytic Hilbert-space tensor-product lifting (Eq. (3), spectral decompositions ofXi,Yi,
complex triangle inequality andk-fold tensor multiplicativity,er > rr/r!, the hyperbolic bound
bh ≤eharsinhµ φ, and the integral bound on∑r
j=1 ln(1 +N/j)) is proved in Sections 2–4 above.
•AST-Audited Zero-Float Verifier (src/qac0_sharp_verifier.py):Enforces an AST self-
audit rejecting all float/complex literals,float(),complex(),eval(),exec(),from_float,
from_decimal, floating-point libraries,/, and**. All 16 SHA-256-sealed certificates (C01–C16)
replayexactrational4×4,8×8,32×32, and64×64matrices(k= 1,2dualwitnessTr(W ⊗kA⊗k) =
3k,CCZ,CZ,C 4Z), exact rational Chebyshev filter checks with rigorous geometric-remainder
8

--- Page 9 ---
upper bounds one3r (full monomial expansion ofµN(q)inC09–C10atN∈{10 2,10 3}and exact
pointwise evaluation on{1,...,R}inC11–C12atN∈{10 6,10 9}), and exactHn block allocations
up ton= 10 4 (M(H10000) = 7438≤10000, padded literal upper bound20363≤30000). The test
suite (tests/test_qac0_sharp.py) passes 51/51 tests including 28 adversarial forgery rejections
in<2s.
AI Assistance Disclosure.Mathematical exploration, Lean 4 proof engineering, zero-float ver-
ification software, and manuscript preparation were conducted by the author with assistance from
Google Antigravity; all theorems, proofs, formalizations, and numerical certificates were indepen-
dently machine-checked by Lean 4.35.0 and the zero-float verifier.
References
[1] Minbo Gao, Zhengfeng Ji, and Chenghua Liu. A simplified proof ofPARITY/∈QAC0. Technical
Report TR26-258, Electronic Colloquium on Computational Complexity (ECCC), October 2026.
[2] Shiva Kintali.PARITY/∈QAC0 (via polarization and direct induction). Preprint, October 2026.
[3] OpenAI. Product-projection localization and theQAC0 parity lower bound. Preprint, September
2026.
[4] Alexander A. Sherstov. The approximate degree of DNF and CNF formulas.SIAM Journal on
Computing, 54(3):702–774, 2025.
[5] Xiaoming Sun and Jingheng Wang.AC0 ̸⊆BQAC 0/qpolyvia sublinear-degree pauli approxima-
tion.arXiv preprint arXiv:2611.34803v1, November 2026.
9
