# Constructive Lean 4 Kernel and Exact Zero-Float Certificates for Google Research Cogentic's Deterministic Subexponential Factoring and QNR Breakthrough

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-4RHFZFBVBA886AX3` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/cogentic-deterministic-factoring-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `8f3aa75e082b87ea55f361c9e39dd811a730148b28e5602fa1508c1126867ba2`

## Abstract

A November 25, 2026 companion preprint from Google Research's Cogentic framework proposes an unconditional deterministic subexponential general integer factoring algorithm with claimed worst-case bit complexity O(exp(3 (ln N)^(3/4))), together with deterministic subexponential order splitting and prime quadratic nonresidue (QNR) construction in O(exp(C_split (ln p)^(1/2) ln ln(p+16))). Rather than assuming peer-reviewed endorsement of the preprint's analytic pillars, we deliver an independent, explicitly scoped, zero-floating-point verification companion uniting 18 constructive Lean 4.35.0 algebraic and arithmetic sub-lemmas (zero sorry, zero axiom, zero Classical.choice, zero warnings; 3 zero-axiom and 15 [propext, Quot.sound]) with a pure-stdlib Python int/Fraction 4-mode auditor (DETFACT-COGENTIC-CERT-1.0) that certifies 16 canonical finite witnesses in 0.010-1.978 ms and rejects 66/66 live adversarial forgeries with exact branch assertions (72/72 pytest checks).

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Kernel and Exact Zero-Float Certificates
for Google Research Cogentic’s Deterministic Subexponential
Factoring and QNR Breakthrough
Lluis Eriksson∗
November 25, 2026
Abstract
A November 25, 2026 companion preprint from Google
Research’s Cogentic framework [4, 2] proposes an un-
conditional deterministic subexponential general integer
factoring algorithm with claimed worst-case bit com-
plexity O(exp(3(lnN)3/4)), together with deterministic
subexponential order splitting and prime quadratic non-
residue (QNR) construction inO(exp(Csplit(lnp)1/2 ln ln(p+
16)))—targeting improvements over both Harvey’s exponen-
tial N1/5+o(1) factoring bound and Burgess–Vinogradov’s
exponential ˜O(p1/(4√e))QNR bound with zero random-
ness and zero Riemann-hypothesis assumptions. Rather
than assuming peer-reviewed endorsement of the preprint’s
analytic pillars, we deliver an independent, explicitly
scoped, zero-floating-point verification companion for its
finite algebraic, congruence, fixed-point, and combinato-
rial mechanisms. Layer 1 (CogenticDetFactoring.lean)
proves 18 standalone constructive Lean 4.35.0 algebraic
and arithmetic sub-lemmas (zerosorry, zeroaxiom, zero
Classical.choice, zero warnings; 3 zero-axiomnone and
15 [propext, Quot.sound]), covering divisor soundness,
biquadratic square-root compatibility, the integer floor step
81 < 4D⇒ 21 ≤D , fixed-point recurrence inequali-
ties,2 ×2unimodular Bézout elimination, primorial prod-
uct and rational density margins, Miller 2-Sylow splitting,
Gauss reduction ideal closure, biquadraticF2-linearity and
K = 2Walsh–Hadamard orthogonality, Burgess exponent
gap arithmetic,2 ×2bordered-adjugate Schur complements,
two-field unit annihilation, base-m evaluation invariance,
subgroup-index saturation, and Theorem 1.3 numeric guard
inequalities. Layer 2 (DETFACT-COGENTIC-CERT-1.0) is a
pure-stdlib Python int/Fraction 4-mode auditor certi-
fying 16 canonical finite witnesses in0.010–1.978 ms and
rejecting 66/66 live adversarial forgeries with exact branch
assertions (72/72 pytest checks).
∗Independent Researcher. Code, Lean 4 proofs, and certificates:
MIT License; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI coding, formalization, and drafting assistance via
Google Antigravity; all Lean 4 theorems, exact zero-float verifiers,
and adversarial tests were independently compiled and verified locally.
Repository: github.com/lluiseriksson/cogentic-deterministic
-factoring-certificates.
1 Introduction and Scope Calibra-
tion
Unconditional deterministic general integer factoring
stalled at exponentialNc+o(1) complexity for half a cen-
tury—improving from Pollard–Strassen’sN1/4+o(1) to Har-
vey’s N1/5+o(1) [5]—while unconditional deterministic con-
struction of a prime quadratic nonresidue (or a Miller
order-splitting witness [7]) stalled at Burgess–Vinogradov’s
˜O(p1/(4√e)) ≈p 0.151633 [1]. The companion Cogentic
preprint [4, 2] proposes breaking both exponential walls
unconditionally via two coupled deterministic engines:
1. Part 1 (Multiquadratic Infrastructure, Walsh–
Hadamard Positivity & Order Splitting, Sec. 2–
6):Running Miller’s 2-Sylow test onq0 = −1,q1,...,q K
either splitsN immediately or extracts2K −1pairwise-
compatible modular square roots(dℓ,sℓ)across quadratic
fields Fℓ = Q(√dℓ)and biquadratic composita Eℓ1,ℓ2 .
Enumerating units and short ideals via Gauss reduction
and 4D weighted LLL [6] yields Walsh–Hadamard pos-
itivity b0(n) + ∑
ℓ̸=0 bℓ(n) = 2 Kˆb0(n) ≥0(amplifying
Y-smooth integers by2K), which [4] contrasts against a
sixteenth-moment quadratic-field Burgess bound to claim
QNR/order-splitting timeO(exp(Csplit(lnp)1/2 ln ln(p+
16))).
2. Part 2 (Base-m Pairs, Two-Field Unit Annihila-
tion & Saturation, Sec. 7–11):Deterministic pre-
conditioned base-m pairs( f1,f2)produce joint square-
free smooth relations; bordered-adjugate linear algebra
and two-field localization (TryPair) extract even prime-
annihilating exponentsEℓ (ℓEℓ ≡1 ( modN )); and mul-
tiplying byLidx = lcm(1,...,K idx)saturates( p−1) | ˜M
across everyp|Nin claimed timeO(exp(3(lnN) 3/4)).
Honest Two-Layer Verification Scope.
1. Layer 1 (Lean 4.35.0 Kernel, Standalone Sub-
Lemmas): lean/CogenticDetFactoring.lean proves
18 standalone constructive algebraic, congruence, and
exact rational-margin sub-lemmas (Table 1) extracted
from Sections 1–11 of [4].
2. Layer 2 (Exact Zero-Float Auditor): DETFACT-
COGENTIC-CERT-1.0 audits 16 finite exact instances
(N≤ 4,028,033) across Miller 2-Sylow splitting and
compatible multiquadratic roots, real-quadratic Gauss
1

--- Page 2 ---
cycles and Walsh–Hadamard sums (K≤ 4), fixed-point
ApproxLog/ApproxSqrt + ModHNF (m≤ 4) + bordered-
adjugate TryPair (k≤ 5), and Lemma 8.1 base-m pairs
+ Lemma 11.1 saturation.
3. Explicit Non-Claims:We donotformalize in Lean 4
Minkowski’s discriminant bound, Chebyshev’s primo-
rial theorem, Bertrand density, generalm-dimensional
ModHNF or k×k bordered adjugates (Table 1 #3, #6–
#8, #12–#14, #18 formalize only the elementary
arithmetic/2D/K = 2steps explicitly printed in Table 1),
4D LLL regulator walks (Lemma 4.2(2)), Weil–Schmidt
character sums/16th-moment Burgess bounds (Proposi-
tion 6.2, Lemma 6.3), Landau–Page/Montgomery esti-
mates (Section 9), or centered Gram peeling (Section 10);
those analytic pillars remain unverified outside the com-
panion preprint [4].
2 Constructive Lean 4.35.0 Kernel
lean/CogenticDetFactoring.lean compiles in1.4 sunder
Lean 4.35.0 [3] with zero external imports, zero warnings,
zero sorry, and zero Classical.choice. Auditing via
AuditAxioms.lean confirms 3 zero-axiom theorems (none:
#8, #13, #18) and 15[propext, Quot.sound] theorems
(P,Q; Table 1).
Proposition 1(Constructive Lean 4 Kernel Scope).
All 18 theorems in Table 1 compile constructively un-
der Lean 4.35.0 without external libraries or classical ax-
ioms (Classical.choice). Notably, Theorem 2 proves
biquadratic modular square-root compatibility overZ, The-
orem 10 proves closed-form Gauss reduction ideal closure
4a′ |(D−b ′2), Theorem 15 proves two-field localization
annihilation( L2 −1)P2 ≡0 ( modN ), and Theorem 17
proves subgroup-index saturation(pj −1)|M ∗Lidx.
3 Exact Zero-Float Certificate Au-
ditor
The modules detfact_exact.py and detfact_
certifier.py (under src/) use exclusively Pythonint,
fractions.Fraction, and exact integermath.gcd/isqrt
(statically audited via ast.walk for zero floating-point
literals or imports). Deterministic primality uses 13-
base Miller–Rabin (bases2 ... 41, proven exact below
3.317 ×1024). Strict JSON loading rejects duplicate keys,
floats, NaN/Infinity, nesting depth>16, and non-ASCII
digits.
Definition 1(DETFACT-COGENTIC-CERT-1.0 Predicates).
A certificate with schema_version="DETFACT-COGENTIC-
CERT-1.0" is accepted iff every claimed value matches exact
recomputation and its mode predicate holds:
• Mode 1 ( miller_multiquadratic_compat_cert):
Runs exact Section 3 Miller 2-Sylow order testing on
{−1,q1,...,q K}given oddN≥ 9and even ˜M (including
Figure 1:(a)Leading-term bit-operation exponents:
Pollard–Strassen (N1/4), Harvey (N1/5), and Cogentic
(exp(3(lnN)3/4), crossing N1/5 at log2 N≈ 73,036).
(b)Prime QNR scaling: Burgess–Vinogradov p1/(4√e)
vs. the subexponential curveexp((lnp)1/2(ln lnp)1/2)(for
reference; the companion preprint’s Theorem 1.2 states
O(exp(Csplit(lnp) 1/2 ln ln(p+ 16)))).
deterministic ratio-splitting on non-cyclic 2-Sylow sub-
groups), verifyingeitherSPLIT (1 <d<N , N%d= 0)or
COMPATIBLE_FAMILY (2K −1squarefree dℓ ̸= 1, s2
ℓ ≡dℓ
(modN ), and all
(2K−1
2
)
pairwise biquadratic congru-
encess ℓ1 sℓ2 ≡η12sℓ1+ℓ2 (modN)).
• Mode 2 (quadratic_infrastructure_wh_cert):Au-
dits odd primeq, exact QNR witness(z/q) = −1via
Euler’s criterion, biquadratic family compatibility modq
with dℓ |PK, exact Lemma 4.2(1) real-quadratic Gauss
reductioncycle RD andfundamentalunit x2
u−Dy2
u = ±4,
and exact Lemma 5.1(2)–(3) Walsh–Hadamard nonnega-
tivity b0(n) + ∑
ℓ̸=0 bℓ(n) = 2Kˆb0(n) ≥0( ˆb0(n) ≥1for
Y-smoothn) with(2 K −1) maxℓSℓ ≥2 KΨ−∑ b0.
• Mode 3 ( fixedpoint_hnf_and_trypair_cert):
Verifies Lemma 2.2(1) ApproxLog, Lemma 2.2(3)
ApproxSqrt with direct integer squaring brackets
(ns −1)2v≤u· 22M < (ns + 1)2v, Lemma 2.2(4)
upper-triangular column ModHNF in Zm (m≤ 4),
and Lemmas 7.4–7.5 exact bordered-adjugate
Badj (B) = (detB)Ik plus two-field localization annihi-
lationℓ 2E0Qlcm ≡1 (modN).
• Mode 4 (base_m_saturation_and_factor_cert):Au-
dits non-perfect-power semiprimeN = p1p2, Lemma 8.1
base-m pair( f1,f2)(( m−1)d < N < md, shared odd
cd ≥4P0ℓ, Rabin irreducibility inF2[X], fi(m) = kiN,
fi(a) ≡1 ( modP 0), f1 splits intod simple roots mod
ℓ, f2 root-free mod ℓ), and Lemma 11.1 saturation
(ℓM∗
≡1 ( modN )for ℓ∈P ok, Lidx = lcm(1..Kidx),
(p1 −1),(p 2 −1)|M ∗Lidx).
4 Exact Findings, Worked Wit-
nesses, and Audit
All experiments ran locally on Windows 11 (Python 3.12.6,
Lean 4.35.0; 7-run means after warm-up).
1. Complexity Crossovers, Walsh–Hadamard Sums
& Gauss Cycles (Figs. 1–2).Equating leading expo-
2

--- Page 3 ---
Table 1: Complete inventory of all 18 constructive Lean 4.35.0 theorems inlean/CogenticDetFactoring.lean (zero
sorry, zeroaxiom, zeroClassical.choice, zero warnings;none for #8, #13, #18 and[propext, Quot.sound] (P,Q)
for the remaining 15).
# Theorem Identifier Ref. [4] Exact Machine-Checked Statement & Hypotheses Ax.
1thm11_factor_divisor_soundThm. 1.11<d<N∧N%d= 0 =⇒ ∃k,1<k<N∧dk=N.P,Q
2lem21_biquadratic_compat_normSec. 2.1s 2
i ≡di, d1d2=η2
12d3, s1s2≡η12s3 (modN) =⇒N|η 2
12(s2
3 −d3).P,Q
3lem21_minkowski_biquadratic_disc_21Lem. 2.1∀D∈N,81<4D=⇒21≤D(integer floor step).P,Q
4lem22_approx_log_recurrence_errorLem. 2.2e<2S, f <S,9p 2 ≤q2, q≥1 =⇒ep 2 +fq 2 <2Sq 2.P,Q
5lem22_approx_exp_squaring_errorLem. 2.2∀a,S,d∈N, a≤S=⇒S 2 −(S−a) 2 +dS≤2aS+dS.P,Q
6lem22_mod_hnf_unimodular_detLem. 2.2g≥1, p i=ga′, ci=gb′, upi +vci=g=⇒ua ′+vb′= 1∧(−b′)pi +a′ci = 0.P,Q
7lem23_chebyshev_primorial_stepLem. 2.3∀k∈N, P≤4 k+1 ∧Q≤4 k =⇒PQ≤4 2k+1.P,Q
8lem23_bertrand_density_2048Lem. 2.32/3−781/2048 = 1753/6144>1/4and12·2047·69>16384·100.none
9lem31_miller_2sylow_split_soundSec. 3N|(x−1)(x+1), N∤(x−1), N∤(x+1) =⇒ ¬Cop(N,x−1)∧¬Cop(N,x+1).P,Q
10lem42_gauss_reduction_ideal_normLem. 4.2D−b 2 = 4aa′∧b′= 2a′q0 −b=⇒ ∃m∈Z, D−b ′2 = 4a′m.P,Q
11lem51_biquadratic_cocycle_f2_linearLem. 5.1u 2
++ = 1 =⇒(u++u+−)(u++u−+)(u++u−−) =u++u+−u−+u−−.P,Q
12lem51_walsh_hadamard_orthogonality_2Lem. 5.1∀h 0,h1,h2,h3 ∈Z,
∑
ℓ∈F2
2
∑
w hw(−1)ℓ·w = 4h0.P,Q
13lem63_burgess_exponent_gapLem. 6.340000 + 2·16825 = 73650<100000(WA 2 <q) and25/4000<40/4000.none
14lem74_bordered_adjugate_schur_2x2Lem. 7.5∀B 1,u,r,a∈Z,
[
B1 u
r a
][a−u
−r B1
]
= (B1a−ru)I 2.P,Q
15lem74_two_field_unit_annihilationLem. 7.4LP≡s 1, P≡s 2 (modN), s2
i = 1 =⇒ ∃Q∈Z,(L2 −1)P 2 =NQ.P,Q
16lem81_base_m_polynomial_evalLem. 8.1N|f 0(m) =⇒f 0(m) +P0ℓ(m−m)g(m) =f 0(m)∧N|f(m).P,Q
17lem111_subgroup_index_saturationLem. 11.1G|M ∗∧G·I j =pj −1∧I j |Lidx =⇒(p j −1)|M ∗Lidx.P,Q
18thm13_exponent_bound_constantsThm. 1.32.7 7 >2 10,28 2 <800,24 10 <2 13 ·10 10, and14<20.none
Figure 2:(a)Exact Lemma 5.1(3) Walsh–Hadamard
amplification(2 K −1) maxSℓ (solid) strictly dominating
2KΨ −∑ b0 (dashed) forq∈{ 71,311,479,1559}.(b)Ex-
act real-quadratic Gauss periodsL vs. fundamental unit
integer bit-length⌊log 2 |xu|⌋+ 1for squarefreed≤61.
nents3( lnN)3/4 = 0.20 lnN yields the exact asymptotic
crossover lnN = 154 = 50,625( log2 N≈ 73,036.4), beyond
which Cogentic’sO(exp(3(lnN)3/4))strictly outperforms
Harvey’s N1/5 (at log2 N = 262,144, log2 ops = 38,091vs.
52,429). Across q∈{ 71,311,479,1559}and K = 1 ... 4,
exact integer Walsh–Hadamard amplification grows from
13to1 ,140( q = 1559,K = 4, 15 fields,Ψ = 6) with zero
negative-tail violations. Real-quadratic Gauss reduction
over 24 tested squarefree discriminants2≤d≤ 61reaches
period L = 10at d = 43( D = 172, xu = 6964 ,yu =
531,N(ε) = +1) and L = 12at d = 46( D = 184, 16-bit
xu).
2. Hand-Verifiable Worked Exact Witnesses (One
per Mode).
• Mode 1 (C01 & C04):In C01 (N = 323 = 17 ·19, ˜M =
144 = 24 ·9),2 9 ≡189 ( mod 323)squares via189 2 ≡191,
1912 ≡305,305 2 ≡1 ( mod 323), yielding gcd(305 −
1,323) = gcd(304,323) = 19. In C04 (N = 311 ·479 =
148,969,K = 4), all2 4 −1 = 15squarefree dℓ yield exact
modular roots sℓ satisfying all
(15
2
)
= 105biquadratic
congruences.
Figure 3:(a)Mean exact zero-float verification latency
across all 16 canonical certificates (0.010–1.978 ms, log
scale).(b)Live adversarial red-team audit rejecting 66/66
forgeries across five attack classes with exact error-branch
assertions.
• Mode 2 (C05, q= 71,K = 2,Y = 6,X = 120):Every
a∈{ 1,..., 6}is a QR mod 71 while735 ≡−1 ( mod 71)
certifies QNRz= 7; Gauss cycle ond= 2( D= 8) gives
period L= 1,( xu,yu) = (2,1),2 2−8·12 = −4( N = −1);
exact Walsh–Hadamard sums giveΨ = 3, ∑ b0 = 35,
maxSℓ = 19, satisfying3·19 = 57≥4·3−35 =−23.
• Mode 3 (C09, N = 323,ℓ = 7): ApproxSqrt(13,3,32)
yields ns = 8,940,687,389satisfying( ns −1)2 ·3 ≤13 ·
264 < (ns + 1)2 ·3; 2D ModHNF mod 60 hasdet = 180;
B =
[3 1
2 5
]
has detB = 13 = E0, Qlcm = 48,7 624 ≡1
(mod 323), certifyingE7 = 2·13·48 = 1,248with7 1248 ≡
1 (mod 323).
• Mode 4 (C13, N = 251 ·257 = 64 ,507,d = 4 ,m =
16,ℓ = 7):15 4 = 50,625 < N <65,536 = 164, P0 = 6,
cd = 243 ≥4 ·6 ·7 = 168; both f1,f2 are irreducible
in F2[X], satisfyfi(16) = 283 N (gcd(283,42) = 1) and
fi(a) ≡1 ( mod 6); f1 splits into 4 simple roots mod 7
while f2 is root-free mod 7;Pok = {11,13,17,19}has
M∗= 32,000, Kidx = 20gives Lidx = 232,792,560(28-
bit), and250,256|M ∗Lidx (43-bit ˜M).
3

--- Page 4 ---
Table 2: Canonical 16-certificateDETFACT-COGENTIC-CER
T-1.0 atlas (results/exp1_certificate_atlas.json ;
all 16 verified).
Certificate ID M Exact Certified Witness Summary ms
m1_miller_split_n323M1N=323, ˜M=144: Miller split19·170.010
m1_miller_split_n10403M1N=10403, ˜M=5100: Miller split103·1010.010
m1_compat_family_p211_k3M1p=211,K=3: 7 fields, 21 biquad. pairs 0.081
m1_compat_family_semi148969_k4M1N=311·479,K=4: 15 fields, 105 pairs 0.251
m2_wh_q71_gauss_d2M2q=71(QNR 7),d=2(L=1),maxS ℓ=190.190
m2_wh_q311_gauss_d13M2q=311(QNR 11),d=13,maxS ℓ=320.491
m2_wh_q479_gauss_d29M2q=479(QNR 13),d=29,maxS ℓ=520.793
m2_wh_q1559_gauss_d43M2q=1559(QNR 17),d=43(L=10),maxSℓ=761.978
m3_fp_hnf2_trypair_n323M3M=32, 2D HNF (det 180),E7=12480.057
m3_fp_hnf3_trypair_n899M3M=48, 3D HNF (det 200),E11=75600.089
m3_fp_hnf4_trypair_n1763M3M=64, 4D HNF (det 7056),E13=16800.135
m3_fp_hnf4_trypair5_n3599M3M=96, 4D HNF,5×5B,E17=174000.228
m4_basem_sat_n64507_d4M4251·257,d=4,m=16,K idx=20, 43-b˜M0.066
m4_basem_sat_n256027_d4M4503·509,d=4,m=23,Kidx=30, 59-b˜M0.071
m4_basem_sat_n1022117_d4M41009·1013,d=4,m=32,Kidx=40, 71-b˜M0.097
m4_basem_sat_n4028033_d5M42003·2011,d=5,m=21,Kidx=50, 93-b˜M0.097
3. 16-Certificate Atlas & 72-Test Red-Team Au-
dit (Table 2, Fig. 3).Table 2 lists all 16 canonical
certificates (0.010–1.978 ms). tests/test_suite.py runs
72 pytest functions: 1 full replay of all 16 certificates,
3 raw-JSON parser guards (IEEE-754 float, NaN, dupli-
cate keys), 2 regression tests (non-cyclic 2-Sylow split on
N = 3601 = 13 ·277and 12-base strong-pseudoprime re-
jection), and 66 parametrized live adversarial forgeries
(12 schema/parser + 12 Mode 1 + 14 each Modes 2–
4), each asserting an exact regex match on its intended
CertificateError branch. scripts/verify_all.py en-
forces all 5 gates including strict axiom whitelisting and a
40-file SHA-256 manifest.
5 Conclusion
We built an independent, explicitly scoped, zero-
floating-point verification companion for the determinis-
tic algebraic and combinatorial mechanisms of the Co-
gentic factoring (O(exp(3(lnN)3/4))) and prime QNR
(O(exp(Csplit(lnp)1/2 ln ln(p+ 16)))) preprint [4, 2], pair-
ing 18 constructive Lean 4.35.0 sub-lemmas (zerosorry,
zero Classical.choice) with the pure-int/Fraction 4-
mode auditorDETFACT-COGENTIC-CERT-1.0, 16 canonical
exact finite witnesses, and 66/66 live adversarial forgery
rejections.
References
[1] D. A. Burgess. On character sums andL-series. II.Proceedings
of the London Mathematical Society, s3-13(1):524–536, 1963.
[2] Yang Cai, Vishal Gupta, Yiding Jiang, Christopher Liaw, Aranyak
Mehta, Grigoris Velegkas, and Di Wang. Cogentic: Multi-agent
orchestration for automated proof discovery. arXiv preprint
arXiv:2609.40324, 2026.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem
prover and programming language. InAutomated Deduction –
CADE 28, volume 12699 ofLNCS, pages 625–635. Springer, 2021.
[4] Google Research Cogentic. Unconditional deterministic subex-
ponential integer factoring and quadratic nonresidue construc-
tion. Unrefereed Companion Preprint (Google Research Cogen-
tic), November 2026. Proposes unconditional deterministic fac-
toring in O(exp(3(lnN )3/4))and prime QNR construction in
O(exp(Csplit(lnp) 1/2 ln ln(p+ 16))).
[5] David Harvey. An exponent one-fifth algorithm for deterministic
integer factorisation.Mathematics of Computation, 90(332):2937–
2950, 2021.
[6] A. K. Lenstra, H. W. Lenstra, and L. Lovász. Factoring polyno-
mials with rational coefficients.Mathematische Annalen, 261:515–
534, 1982.
[7] Gary L. Miller. Riemann’s hypothesis and tests for primality.
Journal of Computer and System Sciences, 13(3):300–317, 1976.
4
