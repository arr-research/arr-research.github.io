# Certified Verification of Polynomial Decompositions, Discrete Tomography Reconfiguration, and Legendre Cross-Polytope Slice Integrals

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-79HZHAG1VW8AKTS6` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/polynomial-decomposition-reconfig-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `a3fd4ef9371b2c19e5376b419437af30ff9d4323cb9497cc170f3095d739bbbb`

## Abstract

We construct a standalone zero-dependency Lean 4.35.0 formalization of 18 core discrete-tomography, integer-polynomial-ring, Proposition 3.7 Cramer-elimination, Legendre/Murphy, Theorem 1.6 global cross-polytope slice-integral, and cyclotomic-factorization theorems (zero sorry, zero warnings, zero Classical.choice) for Peter Keevash and Jeck Lim (arXiv:2611.33120, Nov 2026), paired with a zero-floating-point exact rational/integer four-mode certificate verifier (POLY-DECOMP-CERT-1.0). Across 16 canonical certificates (0.062-2.740 ms, total 8.07 ms), all exact Theorem 1.6 slice polynomials, m-basic polynomial decompositions, multi-directional discrete tomography switch chains, Proposition 3.7 filling-norm witnesses, and cyclotomic factorizations replay deterministically while rejecting 60/60 live adversarial forgery attacks.

## Full Extracted Text

--- Page 1 ---
Certified Verification of Polynomial Decompositions, Discrete
Tomography Reconfiguration, and Legendre Cross-Polytope
Slice Integrals
Lluis Eriksson∗
November 25, 2026
Abstract
Peter Keevash and Jeck Lim (arXiv:2611.33120, Nov.
2026) resolved polynomial-time reconfiguration and ap-
proximate counting for discrete tomography and gen-
eral k-directional integer matrices via m-basic polyno-
mial decompositions in Z[x](Thms. 1.1–1.4), a filling-
norm lower bound using the witness familyFa,b,ab(x) =
(1 −xa)(1 −xb) −(1 −x)(1 −xab)(Prop. 3.7), cyclo-
tomic divisibility (Sec. 4.1), and a “miraculous” exact
global polynomial theorem for weighted Legendre cross-
polytope slice integralsRl(r,s)(Thm. 1.6). We construct
a standalone zero-dependencyLean 4.35.0formaliza-
tion of 18 core tomography, Z[x]-ring, Proposition 3.7
Cramer-elimination, Legendre/Murphy, Theorem 1.6
global slice-integral, and cyclotomic-factorization theo-
rems (zerosorry, zero warnings, zeroClassical.choice)
paired with a zero-floating-point exact Q/Z verifier
(POLY-DECOMP-CERT-1.0). Across 16 canonical certificates
(0.062–2.740 ms, total8 .07 ms), all exact Legendre slice
polynomials, m-basic decompositions, multi-direction to-
mography switches, and filling-norm witnesses replay deter-
ministically while rejecting 60/60 live adversarial forgery
attacks.
1 Introduction
Efficient reconfiguration and approximate counting of in-
teger matrices with prescribed projections—classical con-
tingency tables [4, 5, 1], transportation polytopes [2], and
discrete tomography [6, 7]—hinge on decomposing zero-
projection differences into elementary switches of bounded
support. Keevash and Lim [8] established a general alge-
braic framework with four central mechanisms:
1. Miraculous Legendre Slice Integrals (Thm. 1.6,
Sec. 1.4 & 2.1):Weighted by Murphy’s Legendre
polynomial Lk−1 [9], the cross-polytope slice integral
Rl(r,s)simplifies globally to a degree-(k−1)polynomial
satisfying Rl(−r,−s) = Rl(s,r) = Rl(r,s)and exact
∗Independent Researcher. Code, Lean 4 proofs, and certifi-
cates: MIT License; manuscript and figures: CC-BY-4.0. Pre-
pared with AI coding, formalization, and drafting assistance
from Google Antigravity; all proofs, exact rational/integer veri-
fiers, and adversarial tests were independently compiled and ver-
ified locally. Repository: https://github.com/lluiseriksson/
polynomial-decomposition-reconfig-certificates
constant marginal
∫1
−1 Rl(r,s) ds= 2/k!despite3 k(k−
1)/2>koverdetermined symmetry constraints.
2.m -Basic Polynomial Decompositions (Thms. 1.2
& 1.4):Reducing multi-directional switches via de-
terminant projections maps zero-X-ray grids to integer
polynomials divisible by(1−x)k, decomposed into sums
of m-basic atoms±xa ∏k
i=1(1 −xmiai )with controlled
L1 norm.
3. Discrete Tomography Reconfiguration (Sec. 1.1,
Thm. 1.1):Multi-directional basic switches annihi-
late X-ray projectionsπv along every primitive lattice
direction v = (a,b)via the line invariantbx−ay , en-
abling bounded-entry reconfiguration paths between
equal-X-ray grids.
4. Filling-Norm Lower Bound & Cyclotomics
(Prop. 3.7, Sec. 4.1):The witness Fa,b,c(x) =
(1 −xa)(1 −xb) −(1 −x)(1 −xc)is divisible by(1 −x)3
iff ab= c, yields4 m+ 3monomial-matching equations
in4 m variables, and resists small decompositions via
base-t Cramer non-vanishing; generalm-weights factor
through cyclotomic polynomialsΦd(x).
Contributions and Scope.We do not formalize asymp-
totic random-walk mixing bounds inside Lean 4; in-
stead, we machine-check the exact algebraic, combi-
natorial, and symbolic core of [8]: (i) 18 zero- sorry,
zero-Classical.choice Lean 4.35.0[ 3] theorems in
PolyDecompReconfig.lean; (ii) the exact Q/Z verifier
POLY-DECOMP-CERT-1.0; (iii) 16 canonical certificates
across all four modes; and (iv) a 60-attack live red-team
suite with 39-artifact SHA-256 manifest enforcement.
2 Constructive Lean 4.35.0 Kernel
The standalone module PolyDecompReconfig.lean (in
lean/) compiles cleanly under Lean 4.35.0 in1.2 swith
zero external dependencies, zero warnings, and zero
sorry. Auditing all 18 theorems via #print axioms
(AuditAxioms.lean) confirms 3 zero-axiom theorems
(none), 1 using only [propext], 14 using [propext,
Quot.sound], and0using Classical.choice or
Lean.ofReduceBool(Table 1).
Proposition 1(Machine-Checked Algebraic Invariants).
The Lean 4.35.0 kernel proves the following universal iden-
1

--- Page 2 ---
Table 1: All 18 machine-checked Lean 4.35.0 theo-
rems in PolyDecompReconfig.lean (zero sorry, zero
Classical.choice).
# Lean Theorem Identifier Paper Ref. Axioms
1basic_switch_2d_zero_line_sumsSec. 1none
2tomography_line_projection_annihilatesSec. 1.1p, Q
3tomography_det_step_identitySec. 1.1p, Q
4poly_eval_one_div_one_minus_xSec. 1.2p, Q
5poly_deriv_at_one_vanishes_k2Sec. 1.3p, Q
6poly_l1_norm_triangleSec. 1.2p, Q
7prop37_witness_divisible_by_cube_iffProp. 3.7p, Q
8prop37_monomial_matching_equation_countProp. 3.7p, Q
9prop37_base_t_cramer_nonzeroProp. 3.7p, Q
10legendre_low_degree_norm_and_paritySec. 1.4p, Q
11legendre_murphy_matches_rodriguesSec. 1.4p, Q
12legendre_orthogonality_exact_k3Sec. 1.4none
13cross_polytope_slice_vol_k2_k3Sec. 2.1p
14thm16_miracle_k2_global_polyThm. 1.6p, Q
15thm16_miracle_k3_global_polyThm. 1.6p, Q
16thm16_symmetry_constraints_exceed_dofSec. 1.4p, Q
17moment_vanishing_implies_zero_polySec. 1.3p, Q
18cyclotomic_phi_factorization_lowSec. 4.1none
Axiom key: none = zero axioms (3);p = [propext] (1); p, Q = [propext, Quot.sound] (14).
tities overIntandList Int:
1. Polynomial Ring & Prop. 3.7 (Thms. 4–9, 17–18):For
every Q∈Z [x],(1 −x)Q vanishes at1,(1 −x)2Q
satisfies F(1) = F′(1) = 0, and|P + Q|1 ≤|P|1 + |Q|1.
In Prop. 3.7,F′′(1) = 2(ab−c) = 0 ⇐⇒ab = c;8 m+6
monomials yield4 m+ 3equations (overdetermined by
3); and whenever|z0|,|z1|,|z2|≤B , t≥ 2B+ 2, and
z3 ̸= 0, z0 + z1t+ z2t2 + z3t3 ̸= 0. Sum-of-squares∑ v2
i = 0 ⇐⇒ ∀i,vi = 0, and xm −1 = ∏
d|m Φd(x)
holds inZ[x]form∈{2,3,4,6}.
2. Legendre Miracle & Tomography (Thms. 1–3, 10–
16):Murphy’s formula matches L1,L2,L3 identically;
cleared integrals prove
∫1
−1 L0L2 = 0,
∫1
−1 L2
2 = 2 /5,∫1
−1 L2
3 = 2/7; for k = 2(2 R0 = 1 −rs) and k = 3
(16R0 = 3 −r 2 −4rs−s 2 + 3r2s2), both symme-
tries R0(−r,−s) = R0(s,r) = R0(r,s)and exact r2-
cancelling marginal
∫1
−1 R0 ds= 2/k!hold globally; and
3k(k−1)>2kfor allk≥2.
3 ExactQ/ZCertificate Verifier
The verifier POLY-DECOMP-CERT-1.0
(src/polydecomp_certifier.py,
src/polydecomp_exact.py) uses pure Python int
and fractions.Fraction exclusively (source-audited for
zero float(, math., or numpy). Every payload enforces
strict JSON typing (rejecting floats, bool-as-int, int-as-
bool), canonical reduced rationals (forbidding"-0" and
"/1"), nesting-depth cap32, full ASCII control-character
filtering, 2048-bit integer caps, and exact container/key
validation across four modes:
1. Mode 1 (Thm. 1.6 Legendre Slice Polynomials):
Symbolically integratesRl(r,s) = T1 + T2 + T3 + T4 in
four variables overQ, verifies Murphy’sLk−1, checks
exact monomials, both global symmetries, degree bound
≤k− 1, exact marginal cancellation
∫1
−1 Rl ds= 2/k!,
Figure 1: (a) Exact Theorem 1.6 slice polynomial
R0(r,s) = (3 −r2 −4rs−s 2 + 3r2s2)/16for k= 3across
r∈{ 0,1/2,1}with constant mean1/6(
∫1
−1 R0 ds= 1/3).
(b) Overdetermined symmetry constraints3
2 k(k−1)ver-
sus polynomial DOFk and nonzero monomial counts for
k∈{2,3,4,5}.
and overdetermination3k(k−1)/2>k.
2. Mode 2 (Thms. 1.2 & 1.4m-Basic Decompo-
sitions):Reconstructs every ±xa ∏k
i=1(1 −xmiai )in
Z[x], verifies exact summation toP, performs k-fold
exact division by(1 −x)verifying quotient P/(1 −x)k,
and checks exact|P|1 and decomposition cost.
3. Mode 3 (Sec. 1.1 Discrete Tomography
Switches):Checks primitive pairwise non-collinear
lattice directions, verifiesπv(A) = πv(B)for every v,
replays every multi-directional basic switch confirming
in-bounds vertices andπv(St) ≡0, verifies final equality
with B, and audits|A−B|1 and peak entry magnitude.
4. Mode 4 (Prop. 3.7 Witnesses & Sec. 4.1 Cyclo-
tomics):Audits prop37_filling_witness (F(1) =
F′(1) = F′′(1) = 0, exact(1 −x)3 quotient degree,|F|1,
4m+3equations, and base-tCramer non-vanishing) and
cyclotomic_factorization (everyΦ d(x)for d|m
and ∏
d|m Φd(x) =xm −1).
4 Empirical Atlas and Red-Team
Audit
Running run_all_experiments.py generates 16 canon-
ical certificates (4 per mode) and four exact datasets,
audited end-to-end byverify_all.py with SHA-256 ver-
ification across all 39 tracked artifacts.
Legendre Miracle & m-Basic Decompositions
(Fig.1).Mode1(0 .856–2.740 ms)certifies Rl(r,s)across
(k,l) ∈{(2,0),(3,0),(3,1),(4,1)}, while Dataset 1 sweeps
all 14 pairs(k,l)for k∈{ 2,3,4,5}(up to 13 monomials,
common denominator3072, exact marginal1 /60, and30
constraints vs.5DOF). Mode 2 (0.079–0.118 ms) certifies
k∈{ 2,3}unit and weighted (m = [2,3], m = [1,2,3])
decompositions with exact(1−x)k quotients andL1 costs
12–26.
Tomography, Prop. 3.7, & Cyclotomics (Fig. 2).
Mode 3 (0.137–0.186 ms) certifies 2- and 3-direction switch
2

--- Page 3 ---
Figure 2: (a) Proposition 3.7 witness familyFa,b,ab(x):
constant |F|1 = 6versus rapidly growing(1 −x)3 quotient
L1 norm (from2at(2 ,2)to300at(5 ,6)). (b) Exact
cyclotomic polynomial degreeφ(m)and L1 norm |Φm|1
acrossm∈[2,24].
Figure 3: (a) ExactQ/Z replay latency (0.062–2.740 ms)
across all 16 canonicalPOLY-DECOMP-CERT-1.0 certificates.
(b) Live adversarial red-team audit rejecting 60/60 forged
payloads across all five categories.
paths on4 ×4through7 ×7grids (including diagonal,
anti-diagonal, and non-unimodular slope(2,1)with peak
entry ≤3). Mode 4 (0.062–0.234 ms) certifies Prop. 3.7
witnesses(2 ,3,6)and(3 ,5,15)( |F|1 = 6, quotient degrees
4and13, exact Cramer non-vanishing) alongside complete
cyclotomic factorizations form= 12and m= 24( |Φ12|1 =
|Φ24|1 = 3).
Replay Latency and 60/60 Red-Team Audit
(Fig. 3).All 16 canonical certificates replay deterministi-
callyin0 .062–2.740 ms (total8 .07 ms). Theliveadversarial
suite (tests/test_suite.py) tests 60 targeted forgeries—
12 global schema/typing/canonical-rational/depth/control-
char attacks plus 12 domain attacks per mode (corrupted
Rl monomials, unreduced rationals, trailing zeros, broken
m-basic sums, non-primitive or collinear X-ray directions,
out-of-bounds switches, c̸= ab, insufficient baset, and
corruptedΦ d coefficients)—achieving60/60 (100%)re-
jection.
5 Conclusion
We delivered a standalone, zero-floating-point verifi-
cation framework for Keevash and Lim’s polynomial-
decomposition and reconfiguration theory [8], combining
18 zero-sorry, zero-Classical.choice Lean 4.35.0 theo-
rems with the exactQ/Z verifier POLY-DECOMP-CERT-1.0,
16 canonical certificates, and 60/60 live adversarial forgery
rejections.
References
[1] Alexander Barvinok. On the number of matrices and a
random matrix with prescribed row and column sums
and 0–1 entries.Advances in Mathematics, 224(1):316–
339, 2010.
[2] Jesús A. De Loera and Edward D. Kim. Combinatorics
and geometry of transportation polytopes: an update.
Discrete Geometry and Algebraic Combinatorics, Con-
temporary Mathematics, 625:37–76, 2014.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, volume 12699 ofLecture
Notes in Computer Science, pages 625–635. Springer,
2021.
[4] Persi Diaconis and Bernd Sturmfels. Algebraic al-
gorithms for sampling from conditional distributions.
Annals of Statistics, 26(1):363–397, 1998.
[5] Martin Dyer, Ravi Kannan, and John Mount. Sampling
contingency tables.Random Structures & Algorithms,
10(4):487–506, 1997.
[6] Richard J. Gardner, Peter Gritzmann, and Dieter
Prangenberg. On the computational complexity of
reconstructing lattice sets from their X-rays.Discrete
Mathematics, 202(1–3):45–71, 1999.
[7] Lajos Hajdu and Rob Tijdeman. Algebraic aspects
of discrete tomography.Journal für die reine und
angewandte Mathematik, 534:119–128, 2001.
[8] Peter Keevash and Jeck Lim. Efficient reconfiguration,
polynomial decompositions and approximate counting.
arXiv:2611.33120 [math.CO], November 2026.
[9] Gábor Szegő.Orthogonal Polynomials, volume 23 of
AMS Colloquium Publications. American Mathemati-
cal Society, 1939.
3
