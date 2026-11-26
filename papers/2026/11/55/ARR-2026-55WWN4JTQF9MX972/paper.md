# Exact Rational LDL^T Block Certification and Constructive Lean 4 Formalization of Negative-Partial-Transpose Bound Entanglement in C^8 x C^8

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-55WWN4JTQF9MX972` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/npt-bound-entanglement-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `6eadc94aced81f34af94b00fade069e5fe3270198ec1e68899799720640c9435`

## Abstract

Islam Faisal (arXiv:2611.34921v1, Nov. 2026) settles the 28-year-old negative-partial-transpose (NPT) bound entanglement conjecture by proving that the explicit d=8 Werner state rho = (23 I - 3 SWAP)/1448 on C^8 x C^8 is NPT yet undistillable under all separable operations (two-qubit Bell fidelity <= (1+sqrt(2))/4 < 0.61 for every copy number n). We provide an independent, unrefereed companion certification suite (NPT-BOUND-ENT-CERT-1.0) comprising: (i) exact rational pivoted LDL^T factorizations over Q across all 15 symmetry blocks (5 orbit types of sizes 1, 3, 6, 22, 42 for 40(J+Q), 40(J-Q), and 40 Q^(Gamma_in)), establishing full rank 4096 for both J+Q and Q^(Gamma_in) and exact rank 4032 = 4096 - 64 with ker(J-Q) = im(|u> x I); (ii) an exhaustive integer check of all 4096 x 64 = 262,144 entries of Eq. (2d); (iii) 18 constructive Lean 4.35.0 theorems (0 sorry, 0 custom axioms, 0 Classical.choice); and (iv) 16 canonical JSON certificates and 49 unit/forgery/AST tests.

## Full Extracted Text

--- Page 1 ---
Exact RationalLDL T Block Certification and Constructive
Lean 4 Formalization of Negative-Partial-Transpose Bound
Entanglement inC 8 ⊗C 8
Lluis Eriksson
Independent Researcher (https://github.com/lluiseriksson)
Companion Preprint to Islam Faisal (arXiv:2611.34921v1) — Unrefereed Formal-Verification Artifact
November 26, 2026
Abstract
Islam Faisal (arXiv:2611.34921v1, Nov. 2026) settles the
28-year-old negative-partial-transpose (NPT) bound entan-
glement conjecture by proving that the explicit d = 8 Werner
state ρ = (23I− 3 SWAP)/1448 on C8 ⊗C8 is NPT yet undis-
tillable under all separable operations (two-qubit Bell fidelity
≤ (1+
√
2)/4 < 0.61 for every copy number n). The sole com-
putational step in [ 3] (Lemma 3 and Appendix A) exhibits
a 24-integer Hermitian Choi matrix Q = 1
40
P
π∈S4 mπBπ
on (C8)⊗4 (dim = 4096) satisfying J + Q⪰ 0, J−Q⪰ 0,
QΓin ⪰ 0, and ( J−Q )(|u⟩ ⊗I) = 0. We provide an in-
dependent, zero-floating-point companion certification suite
(NPT-BOUND-ENT-CERT-1.0) comprising: (i) exact rational
pivoted LDLT factorizations over Q across all 15 symmetry
blocks (5 orbit types of sizes 1 , 3, 6, 22, 42 for 40( J + Q),
40(J−Q ), and 40QΓin ), establishing strictly positive-definite
full rank 4096 for both J + Q and QΓin and exact rank
4032 = 4096 − 64 with ker(J−Q ) = im(|u⟩ ⊗I) for J−Q ;
(ii) an exhaustive integer check of all 4096 × 64 = 262,144 en-
tries of Eq. (2d); (iii) 18 constructive theorems in Lean 4.35.0
(0 sorry, 0 custom axioms, 0 Classical.choice); and
(iv) 16 canonical JSON certificates and 49 unit/forgery/AST
tests.
1 Introduction and Scope
Since Peres [6] introduced the partial-transpose separability
criterion, Horodecki, Horodecki, and Horodecki [4] discovered
bound entanglement in 1998, and DiVincenzo et al. [ 1] and
D¨ ur et al. [2] conjectured in 2000 that certain NPT Werner
states [9] are undistillable, the existence of NPT bound en-
tanglement has stood as Problem 4 of Horodecki, Rudnicki,
and ˙Zyczkowski [5]. In [ 3], Faisal resolves the conjecture af-
firmatively using the explicit state ρ = (23I− 3 SWAP)/1448
on C8 ⊗C8, proving that for every n≥ 1 and every separable
operation from ρ⊗n to two qubits, the Bell fidelity never
exceeds (1 +
√
2)/4 ≈ 0.6036 < 0.61, whence ED(ρ) = 0 and
distillable entanglement is neither additive nor convex [7].
Scope and attribution.This note is anunrefereed com-
panion verification preprintto [ 3]. All primary mathematical
discoveries, the Werner state ρ, the local maps L, M, the
24-integer Choi matrix Q, and the n-copy coherence proof
belong exclusively to Islam Faisal [ 3]. Because the initial
preprint [3] explicitly notes that verification code was not
yet posted, our contribution is an independent, deterministic,
zero-floating-point audit layer: we verify every symmetry
block of Lemma 3/Appendix A over exact Q, exhaustively
check all 262,144 entries of Eq. (2d) overZ, establish the exact
full-space ranks (4096, 4032, 4096) of (J +Q, J−Q, QΓin ), and
mechanize all 18 algebraic/combinatorial pillars of Lemmas 1–
6 and Corollary 2 in constructive Lean 4.35.0. Operator-
theoretic infinite-dimensional/functional-calculus steps (e.g.,
matrix square roots and spectral projections in Appendix B
of [3]) lie outside our finite algebraic Lean kernel and are
audited at the level of their exact population, rescaling, and
tensor-power inequalities.
2 Exact Mathematical Definitions
and Full-Space Rank Discovery
On C8 ⊗C 8 with maximally entangled unnormalized vector
|u⟩= P8
i=1 |i, i⟩(⟨u|u⟩= 8), Faisal defines
ρ= 23I−3 SWAP
1448 ,
L(X) = 5Tr(X)I−3X T , M(X) = 18Tr(X)I+ 37X,
(1)
and C = L⊗M , whose Choi matrix on ( C8)⊗4 (or-
dered Ain, Bin, Aout, Bout) is J = W(JL ⊗J M )W† with
JL = 5I− 3 SWAP (spec = {2, 8}) and JM = 18I + 37|u⟩⟨u|
(spec = {18, 314}) [8]. Directly, C(|u⟩⟨u|) = (90 · 8 + 185−
54)I− 111 SWAP = 37(23I− 3 SWAP) = 37 · 1448 ρ. In Ap-
pendix A of [3], Q = 1
40
P
π∈S4 mπBπ where Bπ = UΓ2
π is the
partial transpose on the second system of the permutation
operator (Uπ)r,c = Q4
t=1 δrt,cπ(t) , and in lexicographic order
of (π(1), π(2), π(3), π(4)) the 24 exact integer coefficients are
mπ = (88,77,16,24,24,16,380,40,
−288,128,−525,760,−288,−525,884,−876,
612,−756,128,760,−876,2060,−756,−172),
whose sum is P
π∈S4 mπ = 935. Because both J and
Q commute with ¯U⊗U⊗ ¯U⊗ ¯U for all U∈U (8),
40(J±Q ) decompose into five symmetry-orbit block types
B1, B3, B6, B22, B42 of sizes 1, 3, 6, 22, 42 with multiplicities
56, 336, 280, 8, 28 (56+1008+1680+176+1176 = 4096), and
40QΓin shares the exact same blocks after swapping input
indices (i, j).
1

--- Page 2 ---
Table 1: Exact rational LDLT audit of all 15 symmetry
blocks across 40(J + Q), 40(J−Q ), and 40QΓin (live verifier
output).
Orbit Dim×Mult rk(J+Q) rk(J−Q) dim ker(J−Q) rk(Q Γin )
B1 1×56 = 56 1 (PD) 1 (PD) 0 1 (PD)
B3 3×336 = 1008 3 (PD) 3 (PD) 0 3 (PD)
B6 6×280 = 1680 6 (PD) 6 (PD) 0 6 (PD)
B22 22×8 = 176 22 (PD) 21 (PSD) 1×8 = 8 22 (PD)
B42 42×28 = 1176 42 (PD) 40 (PSD) 2×28 = 56 42 (PD)
Total 4096 4096 4032 64 4096
Exact full-space rank characterization.Running exact
rational pivoted LDLT factorization over Q across all 15
representative blocks (Table 1 and Fig. 1) proves not only
positive semidefiniteness (conditions (2a)–(2c) of Lemma 3)
but also the exact rank structure:
J +Q≻ 0 isstrictly positive definite( rank = 4096/4096,
every rational pivot strictly positive).
Q Γin ≻ 0 isstrictly positive definite( rank = 4096/4096,
every rational pivot strictly positive).
J−Q⪰ 0 has full rank on B1, B3, B6, rank 21 /22
(nullity 1) on each of the 8 copies of B22, and rank
40/42 (nullity 2) on each of the 28 copies of B42. Hence
rank(J−Q ) = 56·1+336 ·3+280 ·6+8 ·21+28 ·40 = 4032
and dim ker(J−Q ) = 8 ·1 + 28·2 = 64. Combined with
our exhaustive integer verification of Eq. (2d) across
all 4096 × 64 = 262,144 entries (C13, 0 violations), this
proves ker(J−Q ) = im(|u⟩ ⊗I) withexact equalityand
zero spurious null directions.
3 Constructive Lean 4.35.0 Formal-
ization
We formalize 18 core algebraic, spectral, tensor-
power, coherence, and Bell-fidelity theorems in
lean/NptBoundEntCert.lean under Lean 4.35.0 with-
out Mathlib, audited via #print axioms to depend
exclusively on propext and Quot.sound (0 sorry, 0 custom
axioms, 0 Classical.choice, 0 warnings). Table 2 lists
every theorem and its exact formalized statement.
Two constructive proof highlights eliminate all floating-
point and transcendental steps. First, Theorem 7 establishes
the simultaneous inductive positivity of Jn −Qn and Jn +Qn
for all n≥ 0 from J = P + M, Q= P−M (P, M≥ 0) via
(P + M)k+1 ∓ (P−M )k+1 = P((P + M)k ∓ (P−M )k) +
M((P +M)k ±(P−M )k), mirroring Lemma 4(iii)’s odd-sign
expansion. Second, instead of trigonometric substitution
s = cos2 θ, Theorem 16 proves the exact Bell-fidelity ceiling
F = 1
2 (s + u) ≤ 1+
√
2
4 N (for u2 ≤s (N−s )) algebraically
via (2s−N )2 + 4s(N−s ) = N2 and (a + b)2 ≤ 2(a2 + b2),
yielding (4F−N )2 = (2s−N +2u)2 ≤ 2N2, while Theorem 17
brackets 0.6035<(1 +
√
2)/4<0.6036<0.61 overZ.
4 Zero-Float Verifier, Canonical
Certificates, and Worked Wit-
nesses
Our standalone verifier src/npt_bound_ent_verifier
.py enforces a strict zero-float invariant audited by AST
inspection (zero float literals, zero float() calls, zero /
or /=, zero math/numpy imports), pre-read is file() and
106-byte guards, duplicate-key rejection, and lowest-terms
rational parsing. All 16 canonical certificates ( C01–C16)
generated by scripts/generate_certificates.py pass
python -m src.npt_bound_ent_verifier certificates ,
and all 49 unit, exhaustive 15-block LDLT , forgery, and AST
tests pass under pytest -q. Table 3 reports the live verified
metrics.
Worked Witness 1 (BlockB1 and 1-Copy Werner Pro-
jection, C03 & C16).On the 1-dimensional orbit B1 =
{|0, 1, 0, 0⟩} (j = 1 /∈ {0}, i = k = l = 0), JL(0, 0; 0, 0) =
5 − 3 = 2 and JM (1, 0; 1, 0) = 18, so 40JB1 = 40 · 36 = 1440.
For 40QB1 , rpt = (0, 1, 0, 0) = cpt, which matches the 6 per-
mutations with π(2) = 2 (0-based indices {0, 1, 14, 15, 20, 21}
in S4): 40 QB1 = 88 + 77 + 884− 876 − 876 + 2060 = 1357,
whence 40( J + Q)B1 = 2797 > 0 ( C03), 40( J−Q )B1 =
83 > 0, and 40 QΓin
B1 = 245 > 0. Projecting one copy of
1448ρ = 23I− 3 SWAP onto span{|0⟩,|1⟩}⊗2 gives diagonal
(20, 23, 23, 20) (trace 86) and ⟨01| · |10⟩ = −3, yielding exact
singlet fidelity ⟨Ψ−|τ|Ψ−⟩ = 23+23+6
2·86 = 13
43 ≈ 0.3023 (C16,
Fig. 3b).
Worked Witness 2 (Near-Tight Lemma 5–6 Bell Fi-
delity, C15).Taking p00 = p11 = 17
40 , p01 = p10 = 3
40
(s = 17
20 , r = 3
20 ) with valid Step 1 split a = ( 17
40 , 3
40 , 1
40 , 3
40 )
and b = (0 , 0, 2
40 , 14
40 ) satisfies a0j ≥a 1j, b0j ≤b 1j,
and aij + bij = pij. At rational coherence K = 71
400 ,
K4 = 25411681
25600000000 ≤ 2601
2560000 = p00p01p10p11, giving F =
1
2 (17
20 + 71
200 ) = 241
400 = 0 .6025 (99 .83% of (1 +
√
2)/4) and
(4F−1) 2 = 19881
10000 = 1.9881≤2 (Fig. 3a).
5 Reproducibility and Availability
All source code, Lean 4 proofs, certificates, figure scripts, and
SHA-256 manifest (MANIFEST.sha256) are archived at http
s://github.com/lluiseriksson/npt-bound-entanglem
ent-certificates under MIT (code/Lean/data) and CC-
BY-4.0 (manuscript/figures) licenses. Reproduction requires
three commands: (cd lean && lake build), python -m
src.npt_bound_ent_verifier certificates, and pytest
-q.
AI Assistance Disclosure.Google Antigravity assisted
with Lean 4 proof engineering, zero-float verifier implemen-
tation, test/figure automation, and LaTeX drafting. The
author verified every mathematical derivation, Lean axiom
audit, certificate check, and visual figure inspection, and
takes full responsibility for all contents.
2

--- Page 3 ---
Table 2: All 18 constructive Lean 4.35.0 theorems in NptBoundEntCert.lean (0 sorry, 0 Classical.choice), with exact
statements.
# Lean Theorem Identifier Exact Formalized Statement (overZorN)
1lemma1 werner trace and spectrum23·64−3·8 = 1448∧0<20∧0<26∧23−3·8 =−1
2lemma2 local choi spectra5−3 = 2∧5 + 3 = 8∧18>0∧18 + 37·8 = 314
3lemma2 map c on u identity90·8 + 185−54 = 37·23∧3·37 = 111∧37(23·64−3·8) = 37·1448
4appendix a block partition 409656·1 + 336·3 + 280·6 + 8·22 + 28·42 = 4096∧8 4 = 4096
5appendix a jminusq exact kernel 6456·1 + 336·3 + 280·6 + 8·21 + 28·40 = 4032∧8·1 + 28·2 = 64∧4032 + 64 = 4096
6appendix a m pi invariants P
π∈S4 mπ = 935∧24 = 4!
7lemma4 tensor power nonnegP, M≥0 =⇒ ∀n∈N,(P+M) n −(P−M) n ≥0∧(P+M) n + (P−M) n ≥0
8lemma4 congruence block transformu 2 −vu−uv+v 2 = (u−v) 2 ∧vu−v 2 =v(u−v)∧uv−v 2 = (u−v)v
9sec4 not completely copositive5−24 =−19∧18 + 37 = 55∧18−37 =−19∧ ∀k,(−19)·55·275 k <0
10lemma5 step4 population dominationa 1j ≤a 0j, b0j ≤b 1j =⇒a 00a11 ≤p 00p01 ∧b 00b11 ≤p 10p11 ∧b 00a11 ≤p 01p10
11lemma5 step5 rescaling invariance(λp 00)(λp01)(p10p11) =λ 2(p00p01p10p11)∧(λp 01)p10 =λ(p 01p10)
12lemma5 step5 h gt g branch0< g < h∧g 4 =p 00p11h2 ∧K 2 ≤p 00p11 =⇒K < g
13lemma5 step5 bernoulli amplification∀a, t∈N,1 +ta≤(a+ 1) t (tensor-power amplificationK t ≤4g t =⇒K≤g)
14lemma6 am gm coherence boundp ij ≥0 =⇒16(p 00p11)(p01p10)≤(p 00 +p 11)2(p01 +p 10)2
15lemma6 cauchy schwarz kraus sum4(s 1r1)(s2r2)≤(s 1r2 +s 2r1)2 (√s1r1 + √s2r2 ≤
p
(s1 +s 2)(r1 +r 2))
16lemma6 bell fidelity exact algebraic boundu 2 ≤s(N−s) =⇒(2s−N+ 2u) 2 ≤2N 2 (radical-freeF≤ 1+
√
2
4 )
17lemma6 fidelity strictly below 061(4·6035−10 4)2 <2·10 8 <(4·6036−10 4)2 ∧2·10 4 <(4·61−100) 2
18corollary2 superactivation nonconvexitye ρ =e σ = 0∧e ρ⊗σ >0∧e mix >0 =⇒e ρ⊗σ ̸=e ρ +e σ ∧e ρ +e σ <2e mix
Table 3: Summary of all 16 verified NPT-BOUND-ENT-CERT-1.0 canonical certificates ( C01–C16), with live outputs from
verify file. The remaining 5 small blocks ( B1, B3 for J−Q and B1, B3, B6 for QΓin ) are exhaustively certified via exact-Q
LDLT intests/test_verifier.py(Table 1).
ID Mode Verified Instance Exact Certified Metrics
C01M1 Werner/Mapsd= 8,ρ= (23I−3SWAP)/1448,n= 1 spec(1448ρ) ={20,26},ρ Γ|u⟩=− 1
1448 |u⟩,λ neg(JC◦T ) =−1045
C02M1 Werner/Mapsd= 8 multi-copy non-coCP,n= 5J L :{2,8},J M :{18,314},λ neg(JC5◦T ) =−5976501953125
C03M2 BlockLDL T 40(J+Q) onB 1 (dim 1) PSD, rank 1/1 (PD), tr = 2797, min pivot 2797
C04M2 BlockLDL T 40(J+Q) onB 3 (dim 3) PSD, rank 3/3 (PD), tr = 11925, min pivot 2412
C05M2 BlockLDL T 40(J+Q) onB 6 (dim 6) PSD, rank 6/6 (PD), tr = 22128, min pivot≈2172.42
C06M2 BlockLDL T 40(J+Q) onB 22 (dim 22) PSD, rank 22/22 (PD), tr = 115774, min pivot≈2710.46
C07M2 BlockLDL T 40(J+Q) onB 42 (dim 42) PSD, rank 42/42 (PD), tr = 283594, min pivot≈1996.78
C08M2 BlockLDL T 40(J−Q) onB 6 (dim 6) PSD, rank 6/6 (PD), tr = 21072, min pivot≈49.50
C09M2 BlockLDL T 40(J−Q) onB 22 (dim 22) PSD, rank 21/22 (nullity 1), tr = 55426, min pos pivot≈44.60
C10M2 BlockLDL T 40(J−Q) onB 42 (dim 42) PSD, rank 40/42 (nullity 2), tr = 246966, min pos pivot≈55.36
C11M2 BlockLDL T 40QΓin onB 22 (dim 22) PSD, rank 22/22 (PD), tr = 30174, min pivot≈6.85
C12M2 BlockLDL T 40QΓin onB 42 (dim 42) PSD, rank 42/42 (PD), tr = 55482, min pivot≈8.94
C13M3a Eq. (2d) Full 40(J−Q)(|u⟩ ⊗I) = 0 4096×64 = 262,144 entries checked overZ, 0 violations, dim ker = 64
C14M3b TensorJ 6 −Q 6,J + = 17
5 ,J − = 9
7 32 odd-sign terms exact,J 6 −Q 6 = 551206299456
52521875 , congruence exact
C15M4a Coherences= 17
20 ,r= 3
20 ,K= 71
400 K4 = 25411681
2.56×1010 ≤ 2601
2.56×106 ,F= 241
400 = 0.6025, (4F−1) 2 = 19881
10000 ≤2
C16M4b Kraus/Proj 3-Kraus sum + 1-copyρproj SumF= 281
480 ≈0.5854, (4F−1) 2 = 25921
14400 ≤2; 1-copy|Ψ −⟩F= 13
43
References
[1] David P. DiVincenzo, Peter W. Shor, John A. Smolin,
Barbara M. Terhal, and Ashish V. Thapliyal. Evidence for
bound entangled states with negative partial transpose.
Physical Review A, 61:062312, 2000.
[2] Wolfgang D¨ ur, J. Ignacio Cirac, Maciej Lewenstein, and
Dagmar Bruß. Distillability and partial transposition in
bipartite systems.Physical Review A, 61:062313, 2000.
[3] Islam Faisal. Bound entanglement with negative partial
transpose exists, November 2026. arXiv:2611.34921v1, 25
Nov 2026.
[4] Micha l Horodecki, Pawe l Horodecki, and Ryszard
Horodecki. Mixed-state entanglement and distillation:
Is there a “bound” entanglement in nature?Physical
Review Letters, 80:5239–5242, 1998.
[5] Pawe l Horodecki, Lukasz Rudnicki, and Karol ˙Zyczkowski.
Five open problems in quantum information theory.PRX
Quantum, 3:010101, 2022.
[6] Asher Peres. Separability criterion for density matrices.
Physical Review Letters, 77:1413–1415, 1996.
[7] Peter W. Shor, John A. Smolin, and Barbara M. Terhal.
Nonadditivity of bipartite distillable entanglement follows
from a conjecture on bound entangled Werner states.
Physical Review Letters, 86:2681–2684, 2001.
[8] John Watrous.The Theory of Quantum Information.
Cambridge University Press, Cambridge, 2018.
[9] Reinhard F. Werner. Quantum states with Einstein-
Podolsky-Rosen correlations admitting a hidden-variable
model.Physical Review A, 40:4277–4281, 1989.
3

--- Page 4 ---
Figure 1:Exact Symmetry-Block Audit of Appendix A.(a) Hilbert-space decomposition of ( C8)⊗4 (P = 4096) with
exact dim ker(J−Q ) per orbit summing to 64 = dim im(|u⟩ ⊗I). (b) Minimum strictly positive unscaled rational LDLT
pivot across all 15 blocks ofJ+Q,J−Q, andQ Γin .
Figure 2:Werner Spectra and Multi-Copy Non-Complete-Copositivity.(a) Exact integer eigenvalues of 1448 ρ,
1448ρΓ, JL, JL◦T , and JM◦T (C01). (b) Exponential growth of |λneg(JCn◦T )| = 1045 · 275n−1, highlighting why Lemma 4
cannot rely on complete copositivity (C01,C02).
Figure 3:Exact Bell-Fidelity Ceiling and Certified Witnesses.(a) Lemma 6 envelope 1
2 (s +
p
s(1−s) ) ≤ (1 +
√
2)/4
with peak at s = (2 +
√
2)/4 and near-tight rational witness C15 (F = 241/400 = 0.6025). (b) Certified two-qubit fidelities
including direct rank-2 projection ofρonto|Φ +⟩(10/43) and|Ψ −⟩(13/43,C16).
4
