# Formal Certification of Non-Additivity of Polytope Extension Complexity Under Cartesian Products

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6F2FCZYGK691XS5S` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/extension-complexity-nonadditivity-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `e776eecbc5bb1b0f1b034b6b5a2b16b2a83b615635a1cb94db7e53d4e5e93aff`

## Abstract

We present a machine-checked formal verification and zero-float rational certificate suite (XC-NONADD-CERT-1.0) auditing Minhao Liu's disproof of Conjecture 1.2 of Grande, Padrol, and Sanyal (arXiv:2611.33631v1), establishing that linear extension complexity is strictly subadditive under Cartesian products of polytopes. Our artifact comprises an 18-theorem constructive Lean 4.35.0 kernel (0 sorry, 0 custom axioms, 0 Classical.choice, 0 warnings), an AST-audited zero-float Python verifier over Z and Q, 16 canonical JSON certificates (C01-C16), and 34 unit and forgery-rejection tests covering the 24x39 six-cycle matrix S, exact rank-14 and rank-27 (all 1,521 columns of S x_1 S) nonnegative factorizations, Proposition 9 contraction budgets (663/2500<1 and 62412/76523<1), explicit 24-dimensional 50-facet 150-vertex rational polytope P with xc(P)=40, xc(P x P)=79, and 7-bit zero-error channel savings (128<129), plus Theorem 2 unbounded linear ceil(5n/27) and identical-square deficits.

## Full Extracted Text

--- Page 1 ---
Formal Certification of Non-Additivity of Polytope Extension
Complexity Under Cartesian Products
Lluis Eriksson
Independent Researcher, AIRR Frontier Verification Lab
https://airr.science
November 26, 2026
Abstract
We present a machine-checked formal verification and zero-
float rational certificate suite ( XC-NONADD-CERT-1.0) au-
diting Minhao Liu’s disproof of Conjecture 1.2 of Grande,
Padrol, and Sanyal ( arXiv:2611.33631v1), which estab-
lishes that linear extension complexity is strictly subaddi-
tive under Cartesian products of polytopes. Our artifact
consists of an 18-theorem constructive Lean 4.35.0 kernel
(0 sorry, 0 custom axioms, 0 Classical.choice, 0 warn-
ings), an AST-audited zero-float Python verifier over Z
and Q, 16 canonical JSON certificates ( C01–C16), and 32
unit and forgery-rejection tests. Across four modes, we
independently reconstruct and verify: (i) the 24 × 39 six-
cycle matrix S (L = 106), its exact rank-14 nonnegative
factorization, its exact rank-27 nonnegative factorization
across all 392 = 1,521 columns of the 1-product S⊗ 1 S, its
ordinary rank rankQ(S) = 12, and the alternating 6-cycle
functional D; (ii) all rational contraction budgets of Propo-
sition 9 proving rank+ S = 14 and rank+(S⊗ 1 S) = 27
(663/2500 < 1 and 62412/76523 < 1); (iii) the explicit 24-
dimensional 50-facet rational polytope P with all 150 lifted
vertices verified directly from Eq. (5.3), yieldingxc(P) = 40,
xc(P×P ) = 79, and a 7-bit (128 < 129) zero-error chan-
nel simulation saving; and (iv) Theorem 2’s unbounded
linear deficit δ(Un, Vn) ≥ ⌈5n/27⌉ (Proposition 11) and
unbounded identical-factor square deficit δ(Rt, Rt) ≥t
(Lemmas 12–13).
1 Introduction
The linear extension complexity xc(Q) of a polytope Q is
the minimum number of facets of any polytope projecting
linearly onto Q, equal by Yannakakis’ theorem [ 2] to the
nonnegative rank rank+ SQ of its facet–vertex slack matrix.
Because the facets of a Cartesian product U×V decou-
ple, it was conjectured since the 2013 Dagstuhl Seminar
and formalized as Conjecture 1.2 of Grande, Padrol, and
Sanyal [3] that xc(U×V ) = xc(U)+ xc(V ) for all polytopes
U, V.
In arXiv:2611.33631v1, Liu [ 1] disproves this conjec-
ture via a clean facet-wedge transfer theorem (Theorem 3)
paired with an explicit 24 × 39 matrix S on a doubled
hexagon graph: rank+ S = 14 while rank+(S⊗ 1 S) = 27 <
28, transferring via 13 facet wedges to a 24-dimensional, 50-
facet, 150-vertex rational polytope P with xc(P) = 40 and
xc(P×P ) = 79 (Theorem 1), and further to unbounded
linear-fraction deficits δ(Un, Vn) ≥ ⌈5n/27⌉ and unbounded
Cartesian-square deficitsδ(R t, Rt)≥t(Theorem 2).
Every discrete, algebraic, rational-inequality, and poly-
hedral witness in [ 1] admits complete zero-float machine
verification. Our formal artifact independently reconstructs
the exact matrices, 1-products, vertex lifts, and quanti-
tative contraction inequalities in Lean 4.35.0 and exact
rational Python. We explicitly distinguish scope: our ar-
tifact formally verifies all finite algebraic factorizations,
rational contraction constants, vertex/facet counts, and
combinatorial counting inequalities of Theorems 1–3 and
Propositions 9–11; the real-analysis existence of arbitrary
real nonnegative factorizations in the continuum proofs of
Lemma 5, Proposition 9, and Proposition 11 follows the
analytic arguments of [1] supported by our machine-checked
rational bounds.
2 Constructive Lean 4.35.0 Kernel
The file lean/ExtensionComplexityNonaddCert.lean
proves 18 constructive arithmetic and counting identi-
ties in Lean 4 [ 5] with 0 sorry, 0 custom axioms, 0
Classical.choice, and 0 compiler warnings (audited via
#print axioms), while the companion zero-float Python
verifier independently reconstructs the matrices, 1-products,
and 150-vertex polytope P. Table 1 maps each theorem
to [1].
3 Zero-Float Verifier and Four Cer-
tification Modes
The verifier src/xc nonadd verifier.py operates strictly
over Python int and fractions.Fraction (AST-audited
zero-float).
Mode 1: Six-Cycle Matrix Factorizations ( C01–C04).
From the 12-node, 24-edge doubled hexagon G, Mode 1
constructs R∈ {0, 1}24×12, A0, A1, A2, X0, X1, X2, and
1

--- Page 2 ---
Table 1: All 18 constructive Lean 4.35.0 arithmetic and counting theorems in ExtensionComplexityNonaddCert.lean
(0 sorry,0 Classical.choice,0warnings).
# Theorem Identifier Ref. in [1] Certified Arithmetic / Counting Identity
1wedge transfer deficit invarianceTheorem 3 (r1+2k1)+(r2+2k2)−(r12+2k1+2k2) = r1+r2−r12
2theorem1 polytope invariantsTheorem 1 Wedge counts: 11+13 = 24, 24+26 = 50, 3·2+36·4 =
150, 14 + 26 = 40, 27 + 52 = 79
3prop9 claim2 probe boundProp. 9 Cl. 2 Exact rational check 26( τ + 2β) = 663 /2500 < 1
(L= 10 6)
4prop9 claim2 deficient contradictionProp. 9 Cl. 2 Deficient-node count 12 d + {3, 5, b}> 13d for all
d∈ {1,2}
5prop9 claim3 alternating boundProp. 9 Cl. 3 Exact alternating-sum contraction 26 · 6ε/(1 −ε ) =
62412/76523<1
6prop9 claim4 nine targets contradictionProp. 9 Cl. 4 Two unassigned extras cover at most 2·(2·2) = 8 < 9
targets
7six cycle alternating functionalEq. (4.1) Sign cancellation 1 + (−1) = 0, (−1) + 1 = 0, and
triple 1 + (−1) + 1 = 1
8two subsets of three intersectLemma 7 Constructive witness ∀t1, t2 ∈N,∃s < 3, s̸= t1 ∧
s̸=t 2
9corollary14 even power savingsCor. 14 79m+m= 2m·40 (xc(P 2m)≤2mxc(P)−m)
10corollary15 simplex product gapCor. 15 79 + 2(k+ 1) + 1 = 2(40 +k+ 1) for allk≥0
11zero error channel seven bitsSec. 7.2 40 + 89 = 129>128 = 2 7 = xc(P×P×∆ 48)
12face bound deficit ceilingSec. 7.1δ(U, V)≤min(xc(U)−dimU,xc(V)−dimV)
13prop11 rho three quarters maxProp. 11 Discrete maximum d(3/4)d−1 ≤ 27/16 attained at
d∈ {3,4}
14prop11 rho tail decreasingProp. 11 (d+ 1)·3≤d·4 for alld≥3 (monotone tail)
15prop11 linear deficit five twenty seventhsProp. 11N = 6 star cancellation 1−(3+ ck)/6 ≥ 0 and deficit
3 + 32/27−4 = 5/27
16prop11 n6 sharp witnessSec. 6.2 Sharpn= 6 witness: 450 + 440−888 = 2
17lemma12 cover separation b0 zeroLemma 12j≥2C∧3j≤2m 0 =⇒C+j≤m 0
18theorem2 square unbounded deficitLemma 13 2(p⋆ + S) −r prod ≥t whenever rprod ≤ 2p⋆ + 2S−t
the 24 × 39 matrix S (Eq. (3.1)). It verifies both dual
representations of Lemma 7 (Eq. (3.2)), reconstructs every
column of S as an exact nonnegative integer combination of
the 14 generators {Rv} ∪ {A0, A1}, computes rankQ(S) =
12 via exact Gaussian elimination (Remark 8; Fig. 1(a)),
checks D(Rv) = 0 and D(As) = D(Xt) = 1 (Eq. (4.1)), and
on C01 (L = 106) verifies the exact rank-27 nonnegative
integer factorization of Eq. (3.3) across all 39 × 39 = 1,521
columns (73,008 matrix entries) ofS⊗ 1 S.
Mode 2: Proposition 9 Quantitative Lower Bounds
(C05–C08).Mode 2 audits all four claims of Proposition 9
for d∈ { 1, 2} across multiple probe scales L∈ { 5 ×
105, 106, 2×106}: exact rational computation of β = 1/(Lτ),
ε = 1/L+13dτ, Claim 2’s probe contraction 13d(τ +2β) < 1
(663/2500 at d = 2, L= 106), exhaustive deficient-node
checking over all 1 ≤b≤ 12d, Claim 3’s alternating-
sum bound 13 dmax (6β, 6ε/(1 −ε )) < 1 (62412/76523 at
d = 2, L= 106; Fig. 2(a)), and Claim 4’s hitting-set con-
tradiction 8<9.
Mode 3: Explicit 24D Polytope P & Wedge Transfer
(C09–C12).Mode 3 enforces Proposition 9’s contraction
bounds (L≥ 106) and k≥ 1, reconstructs the gauge-fixed
node potentials y∈Z 12 (yv0 = 0) of all 39 base vertices ofB,
checks that their 24 edge slacks matchS entry-for-entry and
all 13 omitted-facet slacks are nonnegative (Proposition 10),
enumerates all binary wedge lifts of Eq. (5.3) to verify
exactly 3·2+36·4 = 150 distinct vertices, computesdimP =
24 directly via exact rational rank on vertex differences,
proves all 50 inequalities define distinct facets via 50 explicit
single-tight interior witness points, and certifies Theorem 1
(xc(P) = 40,xc (P×P ) = 79), Corollary 15 (contrasting
with pyramid additivity [4]) across k∈ {1, 10, 48, 100}, and
Section 7.2’s 7-bit channel simulation saving (128 < 129;
Fig. 1(b)).
Mode 4: Unbounded Linear & Identical-Square
Deficits (C13–C16).Submode linear deficit prop11
(C13–C14) verifies Proposition 11’s exact parameters ( N =
6, p = 72 , H = 75 n, Λ = 10 5H3), contraction in-
equalities H(2β + τ) < 1 and 2 Hmax (10β, 10ε/(1 −
ε)) ≤ 20/89 < 1, discrete kernel maximum 27 /16
(Fig. 2(b)), and exact deficits δ(U6, V6) ≥ 2 (450 + 440 −
888 = 2) and δ(U27, V27) ≥ 5 (Fig. 3(a)). Submode
identical square Rt (C15–C16) certifies Lemma 12–13’s
alphabet recurrence j1 = 2, ji = 2 P
h<i jh ([2, 4, 12] for
t = 3, [2 , 4, 12, 36, 108] for t = 5) and exact cover/deficit
boundsC t = Pji andδ(R t, Rt)≥t(Fig. 3(b)).
4 Verification Results and Forgery
Resistance
All 16 canonical certificates pass verification in < 0.2 s (Ta-
ble 2). The test suite tests/test verifier.py runs 34
tests covering all 16 certificates, an AST zero-float audit,
and 16 adversarial forgery checks (wrong schema, forged
ordinary rank, out-of-range d = 3, forged Proposition 9
contraction bound, undersized L = 100 in Mode 2 and
2

--- Page 3 ---
Figure 1: Modes 1 and 3 certification [ 1]: (a) separation between ordinary rank / rectangle covering (12 and 24) and
exact nonnegative rank (14 and 27) on S and S⊗ 1 S; (b) Theorem 1 savings (80 → 79) and Section 7.2 zero-error
channel simulation reduction from 129 (8 bits) to 128 = 2 7 (7 bits).
Figure 2: Modes 2 and 4 certification [ 1]: (a) Proposition 9 Claim 2 and Claim 3 contraction budgets versus scale L
at d = 2 (β = 1/200), showing strict clearance below 1 at certified instances C06–C07; (b) Proposition 11 conditional
counting kerneldρ d−1 attaining exact maxima 1 (ρ= 1/2) and 27/16 (ρ= 3/4, atd= 3,4).
L = 10 in Mode 3, non-positive k = 0 in Corollary 15,
non-reduced rationals, forged xc(P2) = 80 or vertex count
149, forged Proposition 11 deficits/ranks, forged Rt recur-
rence/deficit, and boolean/integer type-coercion attacks);
all 34 pass cleanly (34 passed).
5 Reproducibility and Trans-
parency
All source code, Lean 4.35.0 proofs, JSON
certificates, figures, and MANIFEST.sha256 are
archived at https://github.com/lluiseriksson/
extension-complexity-nonadditivity-certificates
(tag v1.0.0). Independent replay uses Lean 4.35.0 and
standard-library Python≥3.10:
(cd lean && lake build)
python -m src.xc_nonadd_verifier certificates
pytest -q
AI Assistance Disclosure:Formalization, zero-float ver-
ifier engineering, and manuscript preparation were con-
ducted by Lluis Eriksson using Google Antigravity, with
every claim independently machine-checked by Lean 4.35.0
and the deterministic verifier. Code/certificates are MIT;
manuscript/figures are CC-BY-4.0.
3

--- Page 4 ---
Figure 3: Mode 4 certification of Theorem 2 [ 1]: (a) unbounded linear-fraction deficit δ(Un, Vn) ≥ ⌈5n/27⌉ with certified
instances C13 (n = 6, δ≥2) and C14 (n = 27, δ≥5); (b) exponentially separated alphabet hitting sizes jt and cover
numbersC t yielding identical-factor Cartesian squares withδ(R t, Rt)≥t.
Table 2: Summary of all 16 canonical certificates (C01–C16) verified underXC-NONADD-CERT-1.0.
ID Mode / Submode Key Parameters Certified Output / Witness
C01–C04 six cycle matrix factorizationsL∈ {5·10 5,10 6,2·10 6,10 7}Rank-14S, rank-27S⊗ 1 S(1,521 cols), 64D-cycles
C05–C08 lower bound proposition9d∈ {1,2},L∈ {5·10 5,10 6,2·10 6}Exact Cl. 2 (663/2500<1) & Cl. 3 (62412/76523<1)
C09–C12 polytope p and transferk∈ {1,10,48,100}24D, 50 facets, 150 verts, xc(P) = 40,xc(P 2) = 79
C13–C14 unbounded(linear prop11)n∈ {6,27},N= 6, p= 72δ(U 6, V6)≥2 (450 + 440−888),δ(U 27, V27)≥5
C15–C16 unbounded(identical square Rt)t∈ {3,5}j= [2,4,12,(36,108)],C t ∈ {18,162},δ≥t
References
[1] M. Liu, “Extension complexity is not additive under
Cartesian products,” arXiv:2611.33631v1 [cs.DM], 25
Nov 2026.
[2] M. Yannakakis, “Expressing combinatorial optimization
problems by linear programs,”J. Comput. System Sci.
43(1991) 441–466.
[3] F. Grande, A. Padrol, and R. Sanyal, “Extension com-
plexity and realization spaces of hypersimplices,”Dis-
crete Comput. Geom.59(2018) 621–642.
[4] H. R. Tiwary, S. Weltge, and R. Zenklusen, “Extension
complexities of Cartesian products involving a pyramid,”
Inform. Process. Lett.128(2017) 11–13.
[5] L. de Moura and S. Ullrich, “The Lean 4 theorem prover
and programming language,”Proc. CADE-28, LNCS
12699 (2021) 625–635.
4
