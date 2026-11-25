# Exact-Q Valiant Coupling-Gadget Certificates, Characteristic-2 Permanent/Hamiltonian Dichotomies, and Machine-Checked Boson-Sampling Permanent Verification

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-16BTPH7EP28MCT91` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/permanent-hamiltonian-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `f16dc95b557bd61f89a89bcb9ad01a7309ed45176e8a6e41959c3dcddb69207b`

## Abstract

On November 24, 2026, OpenAI (openai/math) proved unconditional superpolynomial arithmetic circuit lower bounds exp(c (log N)^2 / (log log N)^2) for the directed Hamiltonian cycle polynomial HC_N over every field and for the permanent Per_N over every field of characteristic different from two, attained already on sparse graphs of maximum degree three via an explicit 3x3 rational Valiant coupling gadget (Lemma 3.4) and Strassen tensor-price wire inequalities (Lemma 2.1). Here we formalize and operationalize the core algebraic, parity-dichotomy, coupling-gadget, Ryser, and Boson-Sampling certification mechanisms in an 18-theorem zero-dependency Lean 4 kernel (v4.35.0, 0 sorry, 0 Classical.choice, 0 warnings) paired with a pure-stdlib exact-Q verifier (PERM-HAM-CERT-1.0). We prove exact characteristic-2 permanent/determinant collapse alongside symbolic 4x4 block-diagonal Per_4/HC_4 separation and characteristic-2 non-collapse of HC; machine-check OpenAI Lemma 3.4's 3x3 rational coupling gadget including its symbolic 0/2-coupling expansion identity and char-2 obstruction; formalize Ryser inclusion-exclusion, multilinearity/symmetry, inductive wire-distance price subadditivity, and dominant (log N)^2 superpolynomial degree dominance; and deploy exact Cayley-orthogonal matrices to certify collision-free Boson-Sampling amplitudes strictly over Q up to 351-bit denominators (n=8 photons in 12.91 ms). Our verifier replays 16/16 certificates in 0.064-27.32 ms with zero floats, cross-checks all three exact evaluators against brute-force S_n summation, and rejects 54/54 live adversarial attacks.

## Full Extracted Text

--- Page 1 ---
Exact-QValiant Coupling-Gadget Certificates,
Characteristic-2Permanent/Hamiltonian Dichotomies,
and Machine-Checked Boson-Sampling Permanent
Verification
Lluis Eriksson∗
November 2026
Abstract
On November 24, 2026, OpenAI (openai/math) proved unconditional superpolynomial arith-
metic circuit lower boundsexp(c(logN )2/(log logN )2)for the directed Hamiltonian cycle polyno-
mial HCN over every field and for the permanentPerN over every field of characteristic different
from two—attained already on sparse graphs of maximum degree three via an explicit3×3rational
Valiant coupling gadget (Lemma 3.4) and Strassen tensor-price wire inequalities (Lemma 2.1).
Here we formalize and operationalize the core algebraic, parity-dichotomy, coupling-gadget, Ryser,
and Boson-Sampling certification mechanisms in an18-theorem zero-dependency Lean 4 kernel
(v4.35.0,0 sorry,0 Classical.choice,0warnings) paired with a pure-stdlib exact- Q veri-
fier (PERM-HAM-CERT-1.0). First, we prove exact characteristic-2permanent collapsePern(A) ≡
detn(A) ( mod 2)alongside the exact decomposition of Per3 −HC 3 into non-Hamiltonian cycle
covers, exact symbolic4 ×4block-diagonal factorization Per4(diag(B1, B2)) = Per2(B1) Per2(B2)
with HC4(diag(B1, B2)) = 0, and explicit characteristic-2separationHC̸≡Per (mod 2)(Lean 4
Theorems 1–7). Second, we machine-check OpenAI Lemma 3.4’s3×3coupling gadget AVal ∈Q 3×3
(Per(AVal) = 1, all four single-edge2 ×2minors identically0, double-edge minor( AVal)33 = 1
with the symbolic0/2-coupling expansion identity, and cleared-denominatorchar2obstruction
2 Per(AVal) ≡0 ( mod 2); Lean 4 Theorems 8–11) and verify live coupled-graph permanent preser-
vation up to10 ×10matrices. Third, we formalize exact Ryser inclusion–exclusion identities,
row multilinearity/symmetry, inductive wire-distance price subadditivity, and dominant(logN )2
superpolynomial degree dominance (Lean 4 Theorems 12–18), and deploy exact Cayley-orthogonal
matrices Q = ( I−S )(I + S)−1 ∈Q m×m to certify collision-free Boson-Sampling amplitudes
and probabilities strictly overQ up to351-bit denominators (n = 8photons in12 .91 ms). Our
pure-stdlib verifier replays16/16exact- Q certificates across all four modes in0.064–27.32 ms with
zero floats, cross-checks all three exact evaluators against brute-forceSn summation, and rejects
54/54live adversarial attacks in0.12 s.
1 Introduction
Valiant’s algebraic complexity program [5, 6] places the permanentPerN(X) = ∑
π∈SN
∏N
i=1 Xi,π(i)
and the directed Hamiltonian cycle polynomialHCN(X) = ∑
N-cyclesσ
∏N
i=1 Xi,σ(i) at the apex ofVNP,
contrasting starkly with the determinantdetN(X)in VP. Outside characteristic two,PerN governs
linear-optical Boson-Sampling transition amplitudes [1], where Ryser’sO(N2N)inclusion–exclusion
formula [4] and Held–Karp’sO(N22N)dynamic program for HCN [2] remain the standard exact
evaluators.
In November 2026, OpenAI [3] proved that over every fieldF, the degree-component border
circuit size satisfiesL[N]
F (HCN) ≥exp (c(logN )2/(log logN )2)(and identically for PerN whenever
∗Independent researcher (Sweden). Manuscript licensed under CC-BY-4.0. Prepared with AI-assisted formal
verification, code generation, and mathematical drafting (Google Antigravity). Code, zero-dependency Lean 4 proofs,
and exact-Q certificates (MIT license):https://github.com/lluiseriksson/permanent-hamiltonian-certificates.
1

--- Page 2 ---
charF̸= 2), already on sparse graphs of maximum degree three (Corollary 3.5). Two elementary
algebraic pillars anchor the sparse completeness transfer and the lower-bound engine: (i) the explicit
3 ×3rational coupling gadget AVal of Lemma 3.4 (which enforces exact0/2-edge coupling using1
2
and therefore requirescharF̸= 2), and (ii) Strassen tensor-price wire-distance Lipschitz and sum-of-
supplies bounds (Lemma 2.1). We mechanize these exact algebraic laws in zero-dependency Lean 4
(lean/PermanentHamiltonian.lean) and build a pure-stdlib zero-float verifier (PERM-HAM-CERT-1.0,
src/perm_certifier.py) certifying four exact-Q witness classes, including exact Cayley-orthogonal
Boson-Sampling permanent amplitudes whose exact rational denominators exceed350bits.
2 Main Exact-Z/QTheorems
2.1 Characteristic-2Permanent Collapse vs. Hamiltonian Cycle Non-Collapse
Theorem 2.1(Characteristic-2Parity Dichotomy and Cycle-Cover Separation).For any integer
matrixA∈Z n×n:
1. Permanent–Determinant Collapse Modulo2:Every odd permutation contributes+1to
Pern(A)and−1todet n(A), so
Pern(A)−detn (A) = 2
∑
sgn(π)=−1
n∏
i=1
Ai,π(i) ≡0 (mod 2)
identically overZ(exact2×2and3×3identities machine-checked in Lean 4 Theorems 1–3).
2. Non-Collapse of HCn in Characteristic2:For n≥ 3, Pern(A) −HC n(A)sums all non-
Hamiltonian cycle covers (at n = 3: a00a11a22 + a00a12a21 + a11a02a20 + a22a01a10; Lean 4
Theorems 4–5). On any symbolic4 ×4block-diagonal matrix diag(B1, B2)( B1, B2 ∈Z 2×2),
Per4(diag(B1, B2)) = Per2(B1) Per2(B2)while all six directed4-cycles in HC4(diag(B1, B2))
vanish identically; in particular, onI3, Per3(I3) ≡det 3(I3) ≡1 ̸≡0 ≡HC 3(I3) ( mod 2)(Lean 4
Theorems 6–7).
Proof. Splitting Sn = An ⊔(Sn \A n)gives Pern(A) −det n(A) = 2 ∑
π/∈An
∏
iAi,π(i) ∈2Z, yielding
Pern ≡det n (mod 2). Removing the( n−1)!single n-cycles fromSn leaves all permutations with
≥2disjoint cycles; on diag(B1, B2), every singlen-cycle must cross between blocks and thus contains
a zero entry, forcingHCn = 0while Pern = Per(B1) Per(B2). At A = I3, Per3(I3) = det3(I3) = 1
whereasHC 3(I3) = 0.
2.2 Exact Soundness of OpenAI’s Lemma 3.4 Valiant Coupling Gadget
Theorem 2.2(Exact0 /2-Coupling Soundness andchar2Obstruction of AVal).Consider OpenAI
Lemma 3.4’s3×3rational coupling gadget [3]
AVal =


1
2
1
2 −1
2
−1−1 1
1 1 1

∈Q 3×3.
1. Exact0 /2Internal Permanent Weights:Over every field of characteristic̸= 2, Per(AVal) =
1, all four single-edge minorsPer(A(r,c)
Val ) = 0for( r, c) ∈{1, 2}2, and the double-edge minor
(AVal)33 = 1(cleared integer matrix ˜A= diag(2,1,1)A Val verified in Lean 4 Theorems 8–10).
2. Coupled-Graph Preservation andchar2Obstruction:Given any n×n matrix B and two
vertex-disjoint nonzero edgese1 = (r1, c1), e2 = (r2, c2)of weights w1, w2, deletinge1, e2 and wiring
r1
w1
−→coln+ 1, rown+ 1 1− →c1 and r2
w2
−→coln+ 2, rown+ 2 1− →c2 onto a private3 ×3block
AVal produces an(n+3) ×(n+3)matrix E whose exact permanent equals the sum over matchings
using eitherneitherorbothof {e1, e2}. Because2 Per(AVal) = Per( ˜A) = 2 ≡0 ( mod 2)(Lean 4
Theorem 11), the gadget requires2to be invertible (charF̸= 2).
2

--- Page 3 ---
Proof. Direct cofactor expansion of˜A =
(1 1−1
−1−1 1
1 1 1
)
gives Per( ˜A) = 1(−1+1)+1( −1+1)+( −1)(−1−
1) = 2, soPer(AVal) = 1. Deleting rowr∈{ 1, 2}and columnc∈{ 1, 2}leaves
(−1 1
1 1
)
or
(1/2−1/2
1 1
)
,
both of permanent0; deleting rows{1, 2}and columns{1, 2}leaves A33 = 1. Expanding Per(E)by
the subset S⊆{e 1, e2}entering the private block multiplies the complement permanent inB by
Per(AVal) = 1(S=∅),0(|S|= 1), andw 1w2(AVal)33 =w 1w2 (S={e 1, e2}).
2.3 Ryser Evaluation, Exact Cayley Boson-Sampling, and Tensor-Price Barriers
Theorem 2.3(Ryser Soundness, Cayley Boson-Sampling, and Wire-Price Barriers).1. Exact
Ryser Inclusion–Exclusion and Symmetry:For everyM∈Q n×n,
Pern(M) =
∑
∅̸=S⊆[n]
(−1)n−|S|
n∏
i=1
∑
j∈S
Mij
(n = 2, 3identities, row multilinearity, and row-swap invariance formalized overZ in Lean 4
Theorems 12–15). For any skew-symmetricS = −S⊤∈Q m×m with det(I + S) ̸= 0, the Cayley
transform Q = (I−S )(I + S)−1 ∈Q m×m is strictly orthogonal (Q⊤Q = Im), certifying exact
collision-free Boson-Sampling amplitudesPer(Qsub) ∈Q and probabilitiesPer(Qsub)2 ∈Q∩ [0, 1]
without floating-point rounding.
2. Strassen Wire-Price Inequalities and Dominant Superpolynomial Dominance (Ope-
nAI Lemma 2.1 & Theorem 1.1):Summing per-site wire transport shifts∆i ≤d ilogq i bounds
total price shift by∑
idilogq i (inductive list proof in Lean 4 Theorem 16), any target tensor price
P > M+ W (W≥ 0) refutes supply by summands of price≤M with selector wireW (Lean 4
Theorem 17), and at scaleN = 2m the dominant quadratic-exponent regime2m2
(modeling the
leading( logN )2 exponent without the subleading(log logN )2 divisor of OpenAI Theorem 1.1)
strictly exceeds every fixed polynomialNk = (2m)k wheneverm≥k+ 1(Lean 4 Theorem 18).
3 Zero-Dependency Lean 4 Kernel andPERM-HAM-CERT-1.0
All18parity-collapse, cycle-cover, Valiant-gadget, Ryser, multilinearity, wire-price, and superpolyno-
mial theorems are formally verified inlean/PermanentHamiltonian.lean (v4.35.0) with0external
dependencies,0 sorry,0 Classical.choice, and0warnings; four theorems (Theorems 7, 8, 9,
and 11) depend on zero axioms whatsoever (Table 1). Exact-N Ryser permanents, Held–Karp
Hamiltonian polynomials, Gaussian determinants, Cayley orthogonality checks, and wire-price audits
are executed by our pure-stdlib zero-float verifiersrc/perm_certifier.py (PERM-HAM-CERT-1.0),
recursively rejectingfloat, bool, Decimal, complex, tuple, non-str keys, malformed names, and
non-canonical rationals.
4 Experiments, Certified Atlas, and Adversarial Red-Teaming
All four deterministic experiments ( scripts/run_all_experiments.py) reproduce via python
scripts/verify_all.py. Table 2 summarizes all16exact-Q certificates verified with zero floats in
0.064–27.32 ms each. Figure 1 tracks exactPerN,HC N,|det N |on sparse max-degree-3circulants
for N = 3 . . .10on a symmetric log scale preserving exact zeros (confirming PerN −det N ≡ 0
(mod 2)at every N, detN = 0at N∈{ 3, 6, 9}, and HCN ̸≡Per N (mod 2)at N∈{ 5, 6, 7}, e.g.
Per6 = 20,det 6 = 0,HC 6 = 1) alongside illustrative OpenAI Theorem 1.1 scaling. Figure 2 shows
exact-Q Cayley-orthogonal Boson-Sampling verification acrossn = 2 . . .8photons (m = n + 1modes),
where exact rational amplitude denominators grow from16bits (n = 2) to351bits ( n = 8, verified in
12.91 ms with zero float64 truncation), contrasted against exponential Ryser/Held–Karp runtimes
vs. polynomial Gaussian elimination. Figure 3 summarizes per-certificate replay latencies. Finally,
tests/test_suite.py cross-checks our exact Ryser, Held–Karp, and Gaussian evaluators against
brute-force Sn permutation summation (n = 3, 4, 5) and runs54live adversarial attacks across all
3

--- Page 4 ---
Table 1: Zero-dependency Lean 4 theorem ledger (lean/PermanentHamiltonian.lean, v4.35.0:
18/18theorems,0sorry,0Classical.choice,0warnings).
# Lean 4 Theorem Identifier Exact Integer/List Statement Verified Axioms
1per2_eq_det2_mod2Per 2(A)−det 2(A) = 2a01a10 overZpropext, Quot.sound
2per3_eq_det3_mod2Per 3(A)−det 3(A) = 2(odd permutations)overZpropext, Quot.sound
3per3_sub_det3_evenPer 3(A) mod 2 = det3(A) mod 2(∀A∈Z 3×3)propext, Quot.sound
4hc3_exact_formulaCycle-reversal symmetry ofHC 3 overZpropext, Quot.sound
5per3_minus_hc3_nonham_decompPer 3 −HC3 =exact sum of4non-Hamiltonian coverspropext, Quot.sound
6hc_vanishes_on_disconnected_2x2Symbolic4×4:Per 4(diag(B1,B2)) = Per2(B1) Per2(B2)∧HC 4 = 0propext
7hc_ne_per_mod2_witnessOnI 3:Per 3 ≡det 3 ≡1̸≡0≡HC 3 (mod 2)none
8valiant_gadget_per_fullCleared OpenAI Lemma 3.4 gadget:Per( ˜AVal) = 2none
9valiant_gadget_minors_zeroAll four2×2coupling minors(r,c)∈{1,2} 2 vanishnone
10valiant_gadget_double_minor_one( ˜AVal)33 = 1& symbolic0/2-coupling expansion= 2(P0 +w1w2P12)propext
11valiant_gadget_char2_obstructionPer( ˜AVal)≡0 (mod 2)(char-2obstruction)none
12ryser_2x2_exact_identityExact2×2Ryser inclusion–exclusion overZpropext, Quot.sound
13ryser_3x3_exact_identityExact3×3Ryser inclusion–exclusion overZpropext, Quot.sound
14per3_row_scalingRow multilinearityPer 3(kr1,r2,r3) =kPer 3(r1,r2,r3)propext
15per3_row_swap_invariantRow-swap invariancePer 3(r2,r1,r3) = Per3(r1,r2,r3)propext, Quot.sound
16price_wire_lipschitz_addInductiveList Int:∆ i ≤ci =⇒
∑
∆i ≤
∑
ci propext
17price_sum_overhead_boundW≥0∧P >M+W=⇒ ¬(P≤M+W)∧P >Mpropext, Quot.sound
18superpoly_circuit_beats_polyDominant(logN) 2 regime:m≥k+ 1 =⇒2 m2
>(2 m)k propext, Quot.sound
Table 2: Atlas of16exact- QPERM-HAM-CERT-1.0 certificates verified with zero floats
(results/exp1_certified_atlas.json).
Certificate File Mode Certified Exact-QClaim Time (ms)
valiant_gadget_4to7.cert.jsonMode 14→7coupled wiring viaA Val: exactPer = 13 2.498
valiant_gadget_5to8.cert.jsonMode 15→8coupled wiring viaA Val: exactPer = 52 5.808
valiant_gadget_6to9.cert.jsonMode 16→9coupled wiring viaA Val: exactPer = 12 12.088
valiant_gadget_7to10.cert.jsonMode 17→10coupled wiring viaA Val: exactPer = 17 27.324
sparse_deg3_circulant_n4.cert.jsonMode 2N= 4,deg≤3:Per = 9,det = 3,HC = 1 0.238
sparse_deg3_circulant_n6.cert.jsonMode 2N= 6,deg≤3:Per = 20,det = 0,HC = 1(HC̸≡Per mod2)1.010
sparse_deg3_circulant_n8.cert.jsonMode 2N= 8,deg≤3:Per = 49,det = 3,HC = 1 5.463
sparse_deg3_weighted_n6.cert.jsonMode 2N= 6,deg≤3:Per = 130,det =−56,HC = 65(HC̸≡Per)0.992
sparse_deg3_disconn_n6.cert.jsonMode 2N= 6disconnected:Per = 4,det = 4,HC = 0 0.859
boson_cayley_m4_n3.cert.jsonMode 3m= 4,n= 3:Q ⊤Q=I 4, exact37-bit-denPer(Q sub) 0.239
boson_cayley_m5_n4.cert.jsonMode 3m= 5,n= 4:Q ⊤Q=I 5, exact80-bit-denPer(Q sub) 0.485
boson_cayley_m6_n5.cert.jsonMode 3m= 6,n= 5:Q ⊤Q=I 6, exact127-bit-denPer(Q sub) 0.964
boson_cayley_m8_n6.cert.jsonMode 3m= 8,n= 6:Q ⊤Q=I 8, exact270-bit-denPer(Q sub) 2.810
price_barrier_m5_k3.cert.jsonMode 44sites, price gap8>0,2 25 >(2 5)3 0.073
price_barrier_m8_k5.cert.jsonMode 46sites, price gap18>0,2 64 >(2 8)5 0.064
price_barrier_m12_k8.cert.jsonMode 48sites, price gap32>0,2 144 >(2 12)8 0.070
four modes—including float/bool/Decimal/complex/tuple/non-str-key injection, malformed names,
unreduced fractions, tampered Valiant gadget entries/wiring, sparsity-bound violations, non-integer
Mode 2 entries, broken Cayley orthogonalityQ⊤Q̸= I, collision-index duplicates, wire-Lipschitz
violations, and closed price gaps—rejecting all54/54in0.12 s.
5 Scope Boundaries and Outlook
This work certifies exact algebraic coupling gadgets, finite-orderPer/det/HC parity dichotomies,
Cayley-orthogonal Boson-Sampling amplitudes, and finite wire-price separation budgets rather than
formalizing the full asymptotic CAT(0) Hadamard-space and border-complexity machinery of [3].
Because exact Ryser and Held–Karp replay scales asO(N2N)and O(N22N)( MAX_N = 12), certifying
larger sparse Valiant gadgets or photonic submatrices in pure Python requires either finite-field
Chinese-remainder certificates or interactive sum-check proofs, which are natural extensions of
PERM-HAM-CERT-1.0.
4

--- Page 5 ---
Figure 1: Sparse parity dichotomy and asymptotic circuit lower bound. (a) ExactPerN,HC N,|det N |
on sparse max-degree-3circulants (N = 3 . . .10) on a symmetric log scale preserving exactdetN = 0at
N∈{ 3, 6, 9}. (b) Illustrative scaling of OpenAI Theorem 1.1’sexp(c(logN )2/(log logN )2)exponent
(c= 1) versus fixed polynomial degreesN2, N4.
Figure 2: Boson-Sampling exact-Q certification and evaluator separation. (a) Exact Cayley-orthogonal
Boson-Sampling replay time and rational denominator bit-length (16→351bits) for n = 2 . . .8
photons. (b) Exponential Ryser/Held–Karp times versus polynomial Gaussian determinant evaluation.
Figure 3: Certified atlas performance. (a) Zero-float exact-Q replay latencies across all16certificates
(0.064–27.32 ms). (b) Coverage across all four certification modes.
5

--- Page 6 ---
References
[1] Scott Aaronson and Alex Arkhipov. The computational complexity of linear optics. InProceedings
of the 43rd Annual ACM Symposium on Theory of Computing (STOC), pages 333–342, 2011.
[2] Michael Held and Richard M. Karp. A dynamic programming approach to sequencing problems.
Journal of the Society for Industrial and Applied Mathematics, 10(1):196–210, 1962.
[3] OpenAI. Circuit lower bounds for Hamiltonian cycle and the permanent. Preprint, https:
//github.com/openai/math, November 2026.
[4] Herbert J. Ryser.Combinatorial Mathematics, volume 14 ofCarus Mathematical Monographs.
Mathematical Association of America, 1963.
[5] Leslie G. Valiant. Completeness classes in algebra. InProceedings of the 11th Annual ACM
Symposium on Theory of Computing (STOC), pages 249–261, 1979.
[6] Leslie G. Valiant. The complexity of computing the permanent.Theoretical Computer Science,
8(2):189–201, 1979.
6
