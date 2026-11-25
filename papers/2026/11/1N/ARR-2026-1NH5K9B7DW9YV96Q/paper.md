# Exact-Fp/Z Cartier-Operator, Laurent Pole-Cancellation, and Residue-Pin Eigenvector Certificates with a Machine-Checked Integer Kernel

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1NH5K9B7DW9YV96Q` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/border-vp-vnp-residue-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `d957dbce4d0735c50b93976c89517fdfdf2d5906b470ef0d8a5d2617453d7e28`

## Abstract

Motivated by characteristic-p Cartier-operator boundary extraction and residue-pin eigenvector constructions in border algebraic complexity, we present an explicitly scoped, standalone, zero-floating-point verification stack pairing two layers. Layer 1 (BorderVPVNPResidues.lean, Lean 4.35.0; 18 theorems, 0 sorry, 0 Classical.choice, 0 warnings) proves exact integral Frobenius additivity defects for p in {2,3,5}, Fermat's little theorem on Z/3Z and Z/5Z, elementary Cartier exponent-index arithmetic (p(-1)+(p-1)=-1, injectivity, shift, non-(p-1) exclusion), scalar pole cancellation (r_1+P)+(r_2-P)=r_1+r_2, 2x2 integer eigenvector linearity, explicit hinge-shortening gap amplification (gap := 2Dm - (w + 2D*l) >= 1), batched query list-sum budgets, the 2x2 entrywise determinant triangle bound |a00*a11 - a01*a10| <= 2B^2, and inductive 2^{u^5} > (2^{u^4})^k over u, k in N. Layer 2 (BORDER-VPVNP-CERT-1.0, pure-stdlib Python exact-Fp/Z auditor) provides a self-contained four-mode verifier checking exact prime-field Cartier semilinearity C_p(A^p eta) = A C_p(eta) and Res(C_p eta) = Res(eta) across p = 3..29, cancelling Laurent poles up to order 10, d x d (d in {3,4,6,8}) pin-eigenvector systems over F_p, and finite hinge/2x2-minor/exponent witnesses across 16 canonical certificates (0.024-0.305 ms) while rejecting 54/54 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Exact-Fp/ZCartier-Operator, Laurent Pole-Cancellation, and
Residue-Pin Eigenvector Certificates with a Machine-Checked
Integer Kernel
Lluis Eriksson∗
November 25, 2026
Abstract
Motivated by characteristic-p Cartier-operator boundary
extraction and residue-pin eigenvector constructions in bor-
der algebraic complexity, we present an explicitly scoped,
standalone, zero-floating-pointverificationstackpairingtwo
layers. Layer 1 (BorderVPVNPResidues.lean, Lean 4.35.0;
18 theorems,0 sorry,0 Classical.choice,0warnings)
proves exact integral Frobenius additivity defects forp∈
{2,3,5}, Fermat’s little theorem onZ/3Z and Z/5Z, ele-
mentary Cartier exponent-index arithmetic (p(−1) + (p−
1) = −1, injectivity, shift, non-(p− 1)exclusion), scalar
pole cancellation(r1 +P) + (r2 −P) = r1 +r2,2 ×2integer
eigenvector linearity, explicit hinge-shortening gap ampli-
fication (gap := 2Dm− (w+ 2Dℓ) ≥1), batched query
list-sum budgets, the2 ×2entrywise determinant triangle
bound |a00a11 −a01a10|≤ 2B2, and inductive2u5
>(2u4
)k
over u,k∈N . Layer 2 (BORDER-VPVNP-CERT-1.0, pure-
stdlib Python exact-Fp/Z auditor) provides a self-contained
four-mode verifier checking exact prime-field Cartier semi-
linearity Cp(Apη) = ACp(η)and Res(Cpη) = Res(η)across
p= 3 ... 29, cancelling Laurent poles up to order10,d×d
(d∈{ 3,4,6,8}) pin-eigenvector systems overFp, and finite
hinge/2 ×2-minor/exponent witnesses across16/16canoni-
cal certificates (0.024–0.305 ms) while rejecting54/54live
adversarial forgeries.
1 Introduction and Scope Calibra-
tion
The characteristic-p Cartier operator on Laurent differen-
tials over a prime fieldFp [4], defined byCp
(∑
jvjtjdt
)
:=
∑
iv1/p
pi+p−1tidt, satisfies v1/p = v on the prime field Fp
(by Fermat’s little theoremvp = v), whenceRes(Cpη) =
Res(η)1/p = Res(η)on Fp and Cp(Apη) = ACp(η). When-
ever a sum of Laurent pathsA(t) = ∑
µAµ(t) ∈F p[t,t−1]
is regular att = 0with boundary value A(0) = z∈F p
(even when individualAµ carry arbitrary cancelling poles),
(A(t) −z)p = A(t)p −z∈t pFp[t], so pairing against any
test differentialη of pole order≤p recovers Res(Apη) =
∗Independent researcher (Sweden). Manuscript and figures: CC-
BY-4.0; code, Lean 4 proofs, and exact-Fp/Z certificates: MIT. Pre-
pared with transparent AI assistance via Google Antigravity. Reposi-
tory: https://github.com/lluiseriksson/border-vp-vnp-residue
-certificates.
zRes (η). These algebraic identities underlie boundary-
value extraction and residue-pin systems in border com-
plexity [5, 1, 3, 2].
Honest Two-Layer Scope Calibration.Every the-
orem and exact-Fp/Z check in this paper is completely
self-contained and independent of any unrefereed external
proof:
1. Layer 1 (Lean 4.35.0 Integer Kernel, Table 1):
Formalizes exact integral Frobenius quotients forp∈
{2,3,5}, Fermat’s little theorem forp∈ {3,5}, inte-
ger index-arithmetic laws motivatingCp, scalar pole
cancellation,2 ×2integer eigenvector linearity, ex-
plicit hinge-shortening gap algebra, list-sum query bud-
gets, the2 ×2entrywise determinant triangle bound
|a00a11 −a01a10|≤ 2B2, and inductive2u5
>(2u4
)k over
u,k∈N.
2. Layer 2 (BORDER-VPVNP-CERT-1.0 Auditor, Defi-
nition 3.1):Performs exact finite-field Fp Laurent
polynomial arithmetic, repeated-squaring Frobenius
checks, Cartier semilinearity (p∈ [2,97]), cancelling-
pole boundary recovery (pole orders up to10),d×d
(d∈ [2,12]) pin-eigenvector verification, and exact big-
integer hinge/exponent audits with zero floats.
3. Explicit Non-Claims:Our Lean 4 kernel doesnotfor-
malize general finite fieldsFp, Laurent series rings, differ-
entials, d×d matrices (d≥ 3), generald×d Hadamard
determinant bounds, or the curve-slicing Zariski-closure
geometry of [3]; multi-termFp Laurent andd×d checks
are executed byBORDER-VPVNP-CERT-1.0.
2 Machine-Checked Lean 4.35.0 In-
teger Kernel
lean/BorderVPVNPResidues.lean compiles standalone
under Lean 4.35.0 with0external dependencies,0 sorry,
0 Classical.choice, and0warnings: 1 [propext] theo-
rem (#12) and 17[propext, Quot.sound] theorems (Ta-
ble 1). In particular, defining the integer hinge shorten-
ing gap gap := 2 Dm− (w + 2Dℓ), Theorem 13 proves
gap≥ 1 ∧w < 2Dm whenever D≥ 1,ℓ≥ 0,w + 2Dℓ <
2Dm, Theorem 14 provest-th tensor-power amplification
tw+2D(tℓ)+ t·gap≤ 2D(tm)for t≥ 1, Theorem 16 proves
1

--- Page 2 ---
the2 ×2entrywise triangle bound |a00a11 −a01a10|≤ 2B2
whenever |aij|≤B , and Theorem 17 proves inductively
overu,k∈Nthatu≥k+ 1 =⇒2 u5
>(2 u4
)k.
3 Specification of
BORDER-VPVNP-CERT-1.0
The pure-stdlib zero-float verifier
src/cartier_certifier.py enforces strict JSON
typing (rejecting floats, booleans, non-string keys, and non-
canonical integer/exponent strings), exact trial-division
primality verification forp∈ [2,97], and canonical sparse
Laurent encodings {e↦→ce ∈{1,...,p− 1}}across four
modes:
Definition 3.1( BORDER-VPVNP-CERT-1.0 Acceptance
Predicates).A certificate is accepted iff its schema, mode,
primep∈[2,97], and exactF p/Zchecks satisfy:
1. Mode 1 (cartier_operator_semilinear_exact ):
Given non-emptyA,η∈F p[t,t−1], computes Ap inde-
pendently via naive repeated multiplication and via
Frobenius substitution (tj ↦→tpj) and verifies equal-
ity, computesCp(η)(extracting cpi+p−1 since c1/p = c
on Fp), checksCp(Apη) = ACp(η)term-by-term, and
checksRes(Cpη) = Res(η)(coefficient oft −1).
2. Mode 2 (boundary_pole_cancellation_residue
_exact ):Given ≥ 2Laurent paths Aµ ∈F p[t,t−1]
with at least one negative-exponent pole, verifies that
A= ∑
µAµ hasno negative exponents(complete pole
cancellation) withz= A(0) modp. Given test differen-
tial η with minimum exponent≥−p (pole order ≤p )
and Res(η) ̸≡0 ( modp ), verifiesRes(Apη) ≡zRes (η)
(modp)and recoversz≡Res(A pη) Res(η)p−2 (modp).
3. Mode 3 (residue_pin_eigenvector_exact ):Given
d∈ [2,12], nonzeroΩ ∈F d
p, matricesW1,...,W r ∈F d×d
p ,
scalars λk,ak ∈F p: verifies WkΩ ≡λ kΩ ( modp )for
every k, forms Wsum = ∑
kakWk modp, and verifies
WsumΩ≡( ∑
kakλk)Ω (modp).
4. Mode 4 (hinge_shortening_and_border_barrier_
exact):Verifies gap := 2Dm− (w+ 2Dℓ) ≥1( D≥
2,m≥ 1,w,ℓ≥ 0,t≥ 1) and exact amplificationtw+
2D(tℓ)+t·gap = 2D(tm); checks|aij|≤B and |a00a11−
a01a10|≤ 2B2 for a2 ×2integer minor; checks batched
query sum∑ qi ≤Qdmax; and verifies exact big-integer
dominance2 u5
>(2 u4
)k (1≤k<u≤12).
4 Experiments, Atlas, and Red-
Team Audit
All experiments (scripts/run_all_experiments.py) re-
produce via python scripts/verify_all.py. Table 2
summarizes all16canonical certificates verified in0 .024–
0.305 ms. Figures 1–3 benchmark Cartier semilinear-
ity across p = 3 ... 29, cancelling-pole recovery up to
Figure 1: (a) Exact-Fp Cartier semilinearity replay la-
tency across primes p = 3 ... 29. (b) Superpolynomial
exp((lnn) 5/4)overtaking fixed polynomialsn2,n4.
Figure 2: (a) Verification latency and maximal canceled
poleorder kmax = 2 ... 10across p= 5 ... 23. (b)Cancelling
Laurent path countm and recovered boundary valuesz∈
Fp.
pole order kmax = 10, exp((lnn)5/4)scaling, and at-
las latencies. tests/test_suite.py cross-checks Frobe-
nius/Cartier identities acrossp∈{ 2,3,5,7,11}and rejects
54/54live adversarial attacks (including compositep, un-
canceled poles, test differentials with pole order>p, zero
Ω, tampered pin matrices, closed hinge gaps, and2×2
entry-bound violations).
5 Conclusion
We delivered an explicitly scoped 18-theorem Lean 4.35.0
integer kernel paired with the fully specified exact-Fp/Z
verifier BORDER-VPVNP-CERT-1.0, 16 canonical certificates
(0.024–0.305 ms), multi-prime Frobenius/Cartier cross-
checks, and 54/54 rejected live adversarial attacks.
References
[1] Ketan D. Mulmuley and Milind Sohoni. Geometric
complexity theory I: An approach to the P vs. NP
and related problems.SIAM Journal on Computing,
31(2):496–526, 2001.
[2] OpenAI. Paths, treesandgridsseparateValiant’shierar-
chy. OpenAI Math Preprint (openai/math), November
24, 2026.
[3] OpenAI. VP and VNP are different. OpenAI Math
Preprint (openai/math), November 23, 2026.
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 integer kernel in lean/BorderVPVNPResidues.lean (0 sorry,
0Classical.choice,0warnings;P,Qabbreviates[propext, Quot.sound]).
# Lean 4 Theorem Identifier Exact Machine-Checked Statement & Hypotheses Axioms
1freshman_dream_p2∀u,v∈Z,(u+v) 2 −u2 −v2 = 2uv.P,Q
2freshman_dream_p3∀u,v∈Z,(u+v) 3 −u3 −v3 = 3(u2v+uv 2).P,Q
3freshman_dream_p5∀u,v∈Z,(u+v) 5 −u5 −v5 = 5(u4v+ 2u3v2 + 2u2v3 +uv4).P,Q
4fermat_little_p3∀a∈Z,(a 3 −a) mod 3 = 0(Fermat onF 3).P,Q
5fermat_little_p5∀a∈Z,(a 5 −a) mod 5 = 0(Fermat onF 5).P,Q
6cartier_index_fixes_residue∀p∈Z, p(−1) + (p−1) =−1(index step forRes(C pη) = Res(η)1/p = Res(η)onF p).P,Q
7cartier_index_injective∀p,i,j∈Z, p≥1∧pi+ (p−1) =pj+ (p−1) =⇒i=j.P,Q
8cartier_semilinear_shift∀p,i,m∈Z, p(i+m) + (p−1) = (pi+ (p−1)) +pm(index arithmetic).P,Q
9cartier_kills_non_residue_mod_p∀p,i,j∈Z, p≥2∧jmodp̸=p−1 =⇒j̸=pi+ (p−1).P,Q
10pole_cancellation_residue_invar∀r 1,r2,P∈Z,(r 1 +P) + (r2 −P) =r 1 +r2 (scalar cancellation).P,Q
11residue_pin_eigenvalue_add2×2overZ:W 1Ω =z1Ω∧W 2Ω =z2Ω =⇒(W 1 +W2)Ω = (z1 +z2)Ω.P,Q
12residue_pin_eigenvalue_scale2×2overZ:WΩ =zΩ =⇒(sW)Ω = (sz)Ω.propext
13hinge_shortening_strict_gapD≥1,ℓ≥0,w+ 2Dℓ<2Dm=⇒gap := 2Dm−(w+ 2Dℓ)≥1∧w<2Dm.P,Q
14hinge_tensor_power_amplificationt≥1,w+ 2Dℓ+g≤2Dm=⇒tw+ 2D(tℓ) +tg≤2D(tm).P,Q
15batch_query_degree_budget_listInductiveList Nat:Qentries≤d=⇒
∑
≤Qd.P,Q
16hadamard_det2_entry_bound2×2entrywise triangle bound:|a ij|≤B=⇒ −2B 2 ≤a00a11 −a01a10 ≤2B2.P,Q
17exp_five_fourths_beats_polyInductive overu,k∈N:u≥k+ 1 =⇒2 u5
>(2 u4
)k.P,Q
18degree_homogenization_add∀d 1,d2,n,d low ∈N, d1 +d2 =n∧d low <n=⇒d low <d1 +d2.P,Q
Table 2: Atlas of16exact-Fp/ZBORDER-VPVNP-CERT-1.0
certificates (results/exp1_certified_atlas.json; all 16
verified).
Certificate File M Certified Exact-Fp/ZWitness Summary ms
cartier_semilin_p3M1F3:C3(A3η)=AC3(η),Res =20.079
cartier_semilin_p5M1F5:C5(A5η)=AC5(η),Res =30.098
cartier_semilin_p7M1F7:C7(A7η)=AC7(η),Res =40.121
cartier_semilin_p13M1F13:C13(A13η)=AC13(η),Res =50.260
pole_cancel_p5_k3M2F 5, 3 paths (polet−2 cancels):z=3,Res =20.070
pole_cancel_p7_k4M2F 7, 4 paths (polet−3 cancels):z=5,Res =20.082
pole_cancel_p11_k5M2F11, 5 paths (polet−4 cancels):z=7,Res =10.113
pole_cancel_p17_k6M2F17, 6 paths (polet−5 cancels):z=11,Res =130.189
pin_eigen_p5_d3M3F 5,d=3, 3 pin matrices:(
∑
akWk)Ω=1Ω0.073
pin_eigen_p7_d4M3F 7,d=4, 4 pin matrices:(
∑
akWk)Ω=3Ω0.093
pin_eigen_p11_d6M3F 11,d=6, 5 pin matrices:(
∑
akWk)Ω=9Ω0.174
pin_eigen_p19_d8M3F 19,d=8, 6 pin matrices:(
∑
akWk)Ω=18Ω0.305
hinge_barrier_D2_u3M4D=2, gap4→16(t=4),det2 =83,235
>(234
)2 0.024
hinge_barrier_D3_u4M4D=3, gap4→24(t=6),det2 =−402,245
>(244
)3 0.025
hinge_barrier_D4_u5M4D=4, gap8→64(t=8),det2 =2850,255
>(254
)4 0.024
hinge_barrier_D5_u6M4D=5, gap20→200(t=10),det2 =15350,265
>(264
)5 0.036
[4] Karl-Otto Stöhr and José Felipe Voloch. A formula for
the Cartier operator on plane algebraic curves.Journal
für die reine und angewandte Mathematik, 377:49–64,
1987.
[5] Leslie G. Valiant. Completeness classes in algebra. In
Proceedings of the 11th Annual ACM Symposium on
Theory of Computing (STOC), pages 249–261, 1979.
Figure 3: (a) Zero-float replay latencies across all
16 BORDER-VPVNP-CERT-1.0 certificates (0.024–0.305 ms).
(b) Balanced 4-per-mode coverage.
3
