# Machine-Checked Exact-Rational Koashi-Imoto Decomposition, Qubit Dichotomy, and Pure-Atom Certificates for Holevo-Rate Visible Compression

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1YD5GXKHN68H0ASP` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/koashi-imoto-holevo-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `b9ab870809f7fc0e212782dec7a5a1a605a458422c418c966f02a73d83e8aca8`

## Abstract

Polloreno (arXiv:2611.33129, November 24, 2026) resolved when visible compression of a finite memoryless quantum source {p_x, omega_x} with shared classical randomness achieves the Holevo rate R_cr = chi: in the maximal Koashi-Imoto (KI) decomposition omega_x = direct_sum_j p(j|x) rho_x^j (x) xi_j, achievability holds if and only if every occupied quantum core rho_x^j is pure, reducing for qubits to the dichotomy that all signals are pure or commute pairwise. We present a machine-checked, zero-floating-point formalization and certificate auditing framework for the finite-dimensional algebraic core of this criterion. First, we build an 18-theorem zero-dependency Lean 4 kernel (KoashiImotoHolevo.lean, Lean 4.35.0; 0 sorry, 0 warnings, 0 Classical.choice) certifying exact Bloch purity and linear-entropy defects, cross-product commutator antisymmetry/collinearity, the 3D Lagrange identity |a x b|^2 + (a.b)^2 = |a|^2 |b|^2, strict convex purity drop along off-center chords, 2x2 Cayley-Hamilton rank-1 idempotence and commutator criteria, full 16-entry 4x4 KI Kronecker purity multiplicativity, the visible/blind rate sandwich and separation (R_cr = chi < R_blind), decomposition-cost excess, Proposition 9 partial additivity, inductive Proposition 10 sector-splitting excess and all-cores-zero biconditional rigidity, and Lemma 3 Caratheodory positivity |X|d^2 + 1 >= 2. Second, we define KOASHI-IMOTO-CERT-1.0 and a pure-stdlib zero-float verifier (using exact rational LDL^T PSD checks and Wedderburn/Schur trivial-commutant Gaussian elimination) spanning four modes. Across 16 canonical certificates, zero-float replay executes in 0.075-0.655 ms, passes independent exact-Q[i] Hermitian and PSD cross-checks, and rejects 57/57 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Machine-Checked Exact-Rational Koashi–Imoto
Decomposition, Qubit Dichotomy, and Pure-Atom
Certificates for Holevo-Rate Visible Compression
Lluis Eriksson*
November 25, 2026
Abstract
Polloreno (arXiv:2611.33129, November 24, 2026)
resolved when visible compression of a finite mem-
oryless quantum source{p x, ωx}with shared clas-
sical randomness achieves the Holevo rateR cr =
χ: in the maximal Koashi–Imoto (KI) decompo-
sitionω x = L
j p(j|x)ρ j
x ⊗ξ j, achievability holds
if and only if every occupied quantum coreρ j
x is
pure—reducing for qubits to the dichotomy that all
signals are pure or commute pairwise. We present
a machine-checked, zero-floating-point formalization
and certificate auditing framework for the finite-
dimensional algebraic core of this criterion. First, we
build an 18-theorem zero-dependency Lean 4 kernel
(KoashiImotoHolevo.lean, Lean 4.35.0; 0sorry,
0 warnings, 0Classical.choice) certifying ex-
act Bloch purity and linear-entropy defects, cross-
product commutator antisymmetry/collinearity, the
3D Lagrange identity|⃗ a×⃗b|2 + (⃗ a·⃗b)2 =|⃗ a|2|⃗b|2,
strict convex purity drop along off-center chords,
2×2 Cayley–Hamilton rank-1 idempotence and com-
mutator criteria, KI Kronecker trace and purity
multiplicativity, the visible/blind rate sandwich and
separation (R cr =χ < R blind), decomposition-
cost excess, Proposition 9 partial additivity, in-
ductive Proposition 10 sector-splitting excess and
all-cores-zero biconditional rigidity, and Lemma 3
Carath´ eodory positivity|X|d 2 + 1≥2. Second,
we defineKOASHI-IMOTO-CERT-1.0and a pure-stdlib
zero-float verifier (using exact rationalLDL T PSD
checks and Wedderburn/Schur trivial-commutant
Gaussian elimination) spanning four modes: qubit
Bloch dichotomies, multi-sector block-tensor KI de-
* Independent researcher; manuscript prepared with trans-
parent AI assistance via Google Antigravity. Source code,
Lean 4 proofs, and exact certificates:https://github.com/
lluiseriksson/koashi-imoto-holevo-certificates.
compositions (up to 6×6), pure-atom Carath´ eodory
mixtures without square roots, and sector-splitting /
partial-additivity audits. Across 16 canonical certifi-
cates, zero-float replay executes in 0.075–0.655 ms,
passes independent exact-Q[i] Hermitian and PSD
cross-checks, and rejects 57/57 live adversarial forg-
eries (including reducible 3×3 direct sums, hidden
4×4 redundant factors, and partially commuting
mixed cores).
1 Introduction
In visible quantum source compression, an encoder
who knows the classical source labelxtransmits
a quantum message to a decoder using unlimited
shared classical randomness (and no shared entan-
glement) to reproduce the ensemble{p x, ωx}x∈X on
a finite-dimensional registerW[6]. While the opti-
mal rateR cr is always bounded below by the Holevo
informationχ=S(¯ω)− P
x pxS(ωx), it remained
open whether shared randomness suffices to attain
Rcr =χfor arbitrary mixed ensembles. Polloreno [5]
settled this question via the maximal Koashi–Imoto
(KI) decomposition [4, 3]:R cr =χif and only if ev-
ery occupied quantum coreρ j
x is pure, whereas any
mixed occupied quantum core induces a uniform rate
gapR cr > χ(proved via Fawzi–Renner recovery [2]
and blind-compression decoupling).
Crucially, checking the KI criterion numerically in
floating-point arithmetic is brittle: a tiny numeri-
cal perturbation can falsely declare a rank-1 core
ρj
x mixed (Tr((ρj
x)2) = 1−10 −15), overlook a hid-
den block diagonalization where a supposedly mixed
sector actually commutes pairwise, or accept a non-
positive-semidefinite (indefinite) forged density ma-
trix. Because purity (ρ 2 =ρ), pairwise commu-
tativity ([ρx, ρy] = 0), exact block-tensor factoriza-
1

--- Page 2 ---
tion L
j p(j|x)(ρj
x ⊗ξ j), and exact positive semidef-
initeness (via rationalLDL T pivoting) are purely
algebraic overQ, they admit zero-floating-point,
machine-checkable certificates.
Contributions.We formally verify and audit the
finite-dimensional algebraic structure of [5], explic-
itly scoping our claims to exact finite-dimensional al-
gebraic invariants, rational density-matrix witnesses,
and cleared linear entropy/rate identities rather than
the asymptotic Fawzi–Renner converse and regular-
ized multi-copy entropy limits of [5]:
1.Zero-dependency Lean 4 kernel (§3):18 con-
structive theorems inKoashiImotoHolevo.lean
(Lean 4.35.0 [1]), 0sorry, 0 warnings,
0Classical.choice.
2.Exact-Qverifier and schema (§4):
KOASHI-IMOTO-CERT-1.0, audited purely via
Python’sfractions.Fractionand arbitrary-
precisionint(zero floats, exact rationalLDL T
PSD test) across four modes.
3.Empirical atlas, Hermitian cross-checks,
and red-team audit (§5):16 canonical cer-
tificates—including Polloreno’s Fig. 2(a,b,c) qubit
regimes, the exact qutrit erasure separationR cr =
χ < Rblind, and 4D/6D multi-sector KI decom-
positions—replayed in 0.075–0.655 ms, plus 57/57
rejected adversarial forgeries.
2 Algebraic Koashi–Imoto Crite-
rion
Let{p x, ωx}x∈X (px >0, P
x px = 1) be a finite
quantum ensemble onH W (dimW=d). In a
Koashi–Imoto decompositionH W ∼= LJ
j=1(HQj ⊗
HNj ) (Eq. (3) of [5]), every signal takes the exact
block-tensor form
ωx =
JM
j=1
p(j|x)ρ j
x ⊗ξ j,(1)
whereξ j is strictlyindependent ofxand P
j p(j|x) =
1. Writingr mix =S(Q|XJ) = P
x,j pxp(j|x)S(ρj
x),
Theorem 1 of [5] establishes the sandwichχ≤R cr ≤
χ+r mix withR cr =χ⇐⇒r mix = 0, whereas
blind compression obeysR blind −χ=H(J|X)+r mix.
OverQ, exact core purityS(ρ j
x) = 0 is algebraically
equivalent to idempotence (ρ j
x)2 =ρ j
x and vanishing
linear-entropy mixing defect
rlin =
X
x,j
pxp(j|x)

1−Tr
 
(ρj
x)2
∈Q ≥0,(2)
sor lin = 0⇐⇒r mix = 0. For a qubit ensem-
bleω x = 1
2 (I+⃗ rx ·⃗ σ) with rational Bloch vectors
⃗ rx ∈Q 3 (∥⃗ rx∥2
2 ≤1), purity is Tr(ω 2
x) = 1+∥⃗ rx∥2
2
2 and
[ωx, ωy] = i
2 (⃗ rx ×⃗ ry)·⃗ σ, yielding the exact algebraic
qubit dichotomy:
Rcr =χ⇐⇒
 
∀x,∥⃗ rx∥2
2 = 1

∨
 
∀x, y, ⃗ rx ×⃗ ry = ⃗0

.
(3)
Furthermore, by Lemma 3 of [5], the decomposition
costF(σ) = inf U [I(X:U) +S(W|U)] is attained
by pure conditional atomsω x = P
u p(u|x)ϕxu with
|U| ≤ |X|d2 +1; for any nonzero rational state vector
|ψxu⟩ ∈Qd, the rank-1 projectorϕ xu = |ψxu⟩⟨ψxu|
⟨ψxu|ψxu⟩ ∈
Qd×d is exact overQwith zero square roots.
3 Zero-Dependency Lean 4 Kernel
We formalize 18 constructive theorems in
lean/KoashiImotoHolevo.lean(Lean 4.35.0,
zero external libraries), audited via
lean/AuditAxioms.lean. All 18 compile cleanly
with 0 warnings, 0sorry, 0Classical.choice,
and 0Lean.ofReduceBool(all 18 depend solely on
[propext, Quot.sound]). Table 1 enumerates the
complete theorem suite.
Theorem 1(Constructive Koashi–Imoto & Com-
pression Kernel).
1.Bloch geometry & off-center chords:Theorems 1–
7 prove exact cleared purity equivalenceS2+|⃗ r|2 =
2S2 ⇐⇒ |⃗ r|2 =S 2, strict mixed defect,
cross-product antisymmetry, self-commutativity,
collinearity commutativity, the 3D Lagrange iden-
tity|⃗ a×⃗b|2 + (⃗ a·⃗b)2 =|⃗ a|2|⃗b|2, and strict convex
purity drop|p⃗ u+q⃗ v|2 <(p+q) 2S2 along non-
degenerate chords (p, q >0,⃗ u̸=⃗ v).
2.Matrix idempotence & Kronecker blocks:Theo-
rems 8–11 prove2×2Cayley–Hamilton rank-1
idempotenceM 2 =SM(Tr =S,det = 0), the
2×2commutator criterion, and exact KI tensor-
factor trace and purity multiplicativityTr((ρ⊗
ξ)2) = Tr(ρ2)Tr(ξ2).
3.Rate bounds, sector splitting, & Carath´ eodory:
Theorems 12–18 formalize Theorem 1 equality
Rcr =χatr mix = 0, the blind-vs-visible separa-
tionR cr =χ < Rblind whenH(J|X)>0, Eq. (12)
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 kernel
inKoashiImotoHolevo.lean(0sorry, 0 warnings,
0Classical.choice).
# Lean 4 Theorem Identifier Axiom Footprint
1blochpuritypureiffunitnorm [propext, Quot.sound]
2blochpuritystrictmixeddefect [propext, Quot.sound]
3blochcrossantisymm [propext, Quot.sound]
4blochcrossselfzero [propext, Quot.sound]
5blochcollinearcommute [propext, Quot.sound]
6lagrangecrossdotidentity [propext, Quot.sound]
7blochchordconvexpuritydrop [propext, Quot.sound]
8qubit2x2traceidempotentrank1 [propext, Quot.sound]
9qubit2x2commutatorzeroiffcollin [propext, Quot.sound]
10ki kroneckertracemultiplicative [propext, Quot.sound]
11ki kroneckerpuritymultiplicative [propext, Quot.sound]
12holevovisiblesandwichequality [propext, Quot.sound]
13blindvsvisiblegapdecomposition [propext, Quot.sound]
14decompositioncostidentityexcess [propext, Quot.sound]
15partialadditivitypurecoreexact [propext, Quot.sound]
16sectorsplittingexcesslist [propext, Quot.sound]
17sectorexcesszeroiffallcoreszero [propext, Quot.sound]
18caratheodorypureatomboundpos [propext, Quot.sound]
excess, Proposition 9 exact additivity for pure-core
factors, inductive Proposition 10 sector-splitting
excess and all-cores-zero rigidity overList, and
Lemma 3 Carath´ eodory positivity|X|d2 + 1≥2.
4 Exact-Rational Certificate Ar-
chitecture
The pure-stdlib verifiersrc/ki certifier.pyau-
ditsKOASHI-IMOTO-CERT-1.0certificates with zero
floating-point arithmetic, strict JSON AST type
enforcement (rejectingfloat,bool,Decimal,
complex, tuples, non-string keys, unreduced frac-
tions, denominator-1 strings, and"-0"), and an
exact symmetric-pivoting rationalLDL T positive-
semidefiniteness checker (mat is psd exact) for ev-
ery real-symmetric density matrix.
Definition 1(FourKOASHI-IMOTO-CERT-1.0Audit
Modes).
1.Mode 1(qubit bloch dichotomy exact): Au-
dits positive priors ( Ppx = 1) and rational
Bloch vectors∥⃗ rx∥2
2 ≤1, recomputing exactr lin,
maxx,y ∥⃗ rx ×⃗ ry∥2
2, and exact dichotomy classifica-
tion(3).
2.Mode 2(ki block tensor criterion exact):
Checks PSD/unit-trace on allω x, ρj
x, ξj
(dW ∈[2,8]), bit-exact direct-sum Kronecker
reconstruction(1), exact core idempotence
(ρj
x)2 =ρ j
x andr lin, and—whenever claiming
strict gap mixed core—verifies exact trivial
commutantdim Q{X: [X, ρ j
x] = 0∀x}= 1
via rational Gaussian elimination forevery
mixed occupied sector (ruling out reducible direct
sums, hidden redundant factors, and partially
commuting sectors!).
3.Mode 3(pure atom caratheodory decomp exact):
Audits pure-atom convex reconstructionsω x =P
u p(u|x)ϕxu from rational state vectors|ψ xu⟩ ∈
QdW (zero square roots), exact projector idem-
potenceϕ 2
xu =ϕ xu, and Lemma 3 cardinality
1≤ |U| ≤ |X|d2
W + 1.
4.Mode 4(sector splitting and partial
additivity exact): Audits exact algebraic
consistency of externally supplied rational
rate/entropy witness tuples against Proposi-
tion 10 sector-splitting totals (F, χ, visible excessPqj(Fj −χj)≤r mix, blind excessH(J|X)+r mix)
and the Proposition 9 partial-additivity sandwich
χ1 +F 2 ≤F 12 ≤F 1 +F 2 (enforcing exact
additivityF 12 =F 1 +F 2 wheneverF 1 =χ 1).
5 Empirical Verification and Red-
Team Results
All 16 canonical certificates and four ex-
periments are produced deterministically by
scripts/run all experiments.pyand verified
end-to-end byscripts/verify all.py(Lean 4
build, 18/18 axiom audit, 16/16 zero-float cert
replays,pytest, and 39/39 SHA-256 manifest
hashes).
1. Off-center qubit chord rates and exact pu-
rity defect.Figure 1(a)–(b) sweeps the mixing pa-
rametert 0 ∈ {0,1
12 , 1
6 , 1
4 , 1
3 , 5
12 , 1
2 }along the exact ra-
tional off-center Bloch chord joining pure endpoints
⃗ u= (3
5 ,0, 4
5 ) and⃗ v= (− 3
5 ,0, 4
5 ) (exact projectors
from|ψ ±⟩= (3,±1) T ). Att 0 = 0 (pure non-
orthogonal),r lin = 0 and Schumacher compression
attainsχ= 0.468996 qubits; att 0 = 1/2 (identical
commuting states),∥⃗ r0 ×⃗ r1∥2
2 = 0 andχ= 0. Every-
where in the open interior 0< t0 <1/2—such as our
certified pointt 0 = 1/6 with exactr lin = 1/10 and
∥⃗ r0 ×⃗ r1∥2
2 = 256/625—both pure endpoints and pair-
wise commutativity fail simultaneously, yielding a
strict gap betweenχ= 0.170878 and min(C, S(¯ω)) =
0.349978 (upper gap 0.179099 qubits).
2. Qutrit erasure separation and
Carath´ eodory scaling.Figure 2(a) il-
3

--- Page 4 ---
Figure 1: (a) Off-center qubit chord compression
rates: endpoint simulationC=I(X:U), Schu-
macher boundS(¯ω), and Holevo informationχ.
(b) Exact rational linear-entropy mixing defectr lin ∈
Qversus protocol gap min(C, S(¯ω))−χ.
Figure 2: (a) Qutrit erasure separation: visible
compression attainsR cr =χacross alle∈[0,1],
while blind compression suffers gapH(J|X) =h 2(e).
(b) Lemma 3 Carath´ eodory pure-atom flag ceiling
|X|d2
W + 1 versus redundant dimensiond N .
lustrates Polloreno’s qutrit erasure source
ωx =e|e⟩⟨e| ⊕(1−e)|ψ x⟩⟨ψx|(|⟨ψ 0|ψ1⟩|= 3/5,
pure occupied cores in both sectors): because
rmix = 0, visible compression with shared ran-
domness tracksχ(e) = (1−e)h 2(4/5) identically
(Rcr =χ, zero gap), whereas unassisted blind
compression pays the full sector-uncertainty
penaltyR blind −χ=H(J|X) =h 2(e), peaking
at 1.0 qubit excess ate= 1/2 (χ= 0.360964
vs.R blind = 1.360964). Figure 2(b) tracks
the Lemma 3 Carath´ eodory pure-atom bound
|X|d2
W + 1∈ {9,33,73,129}as redundant factor
dimensiond N grows from 1 to 4 while the pure
quantum core keepsr lin = 0 identically.
3. 16-certificate atlas, Hermitian cross-
checks, and 57-attack red-team suite.Ta-
ble 2 and Figure 3 summarize all 16 canonical
certificates across all four modes, replayed with
zero floating-point arithmetic in 0.075–0.655 ms (in-
cluding 6×6 two-sector mixed-core KI reconstruc-
tion and 4×4 pure-core⊗mixed-redundant states
Figure 3: (a) Zero-float replay latency across all
16 canonicalKOASHI-IMOTO-CERT-1.0certificates
(0.075–0.655 ms). (b) Balanced 4-per-mode coverage
across all four verification modes.
Table 2: Summary of all 16 exact-Q
KOASHI-IMOTO-CERT-1.0certificates (zero floating-
point arithmetic; reference-machine replay latency
in ms).
Certificate File (stem) Mode Key Exact Witness ms
qubitfig2amixedcommutingM1 commuting,rlin= 51/200,| × |2= 0 0.110qubitfig2bpurenonorthogonalM1 pure,rlin= 0,| × |2= 576/625 0.097qubitfig2cmixednoncommutingM1 gap,rlin= 1/10,| × |2= 256/625 0.077qubittrinemixed3signalM1 gap,r lin= 11/50,| × |2= 144/625 0.138kiqutriterasurepurecoresM2d W= 3, J= 2, rcorelin= 0 0.313ki4dpurecoremixedredundantM2dW= 4, J= 1, rcorelin= 0 0.306ki3dmixednoncommcoregapM2d W= 3, J= 2, rcorelin= 1/15 0.318ki6dtwosectormixedcoregapM2d W= 6, J= 2, rcorelin= 3/40 0.576pureatomchordendpointsU2M3d W= 2,|U|= 2≤9 0.312pureatomqutriterasureU2M3d W= 3,|U|= 2≤19 0.406pureatom4dredundantU2M3d W= 4,|U|= 2≤33 0.655pureatom3signalqubitU3M3d W= 2,|U|= 3≤13 0.340sectorspliterasureblindsepM4 vis = 0, blind = 1, additive 0.075sectorsplittwosectormixedM4 vis = 3/40, blind = 1/2, additive 0.078sectorsplitthreesectornonaddM4 vis = 9/50, blind = 1/2, non-add 0.082sectorsplitfoursectorpurecoresM4 vis = 0, blind = 3/2, additive 0.091
where globalω x is mixed yetr core
lin = 0). In
tests/test suite.py, independent exact Gaussian-
rationalQ[i] 2×2 Hermitian arithmetic cross-checks
exact purity Tr(M 2
0 ) = 9/10 and Frobenius com-
mutator norm Tr([M 0, M1]†[M0, M1]) = 1
2 ∥⃗ r0 ×
⃗ r1∥2
2, confirms exactLDL T PSD rejection of indef-
inite zero-diagonal matrices and exact commutant-
dimension detection (dim = 2) on reducible 3×3
ensembles, and verifies that 57/57 live adversar-
ial forgeries—including Bloch vectors outside the
unit ball, non-PSD matrices, reducible 3×3 direct
sums, hidden 4×4 redundant factors, partially com-
muting multi-sector cores, exceeded Carath´ eodory
bounds, and violated Proposition 9 pure-core ad-
ditivity—raiseKoashiImotoCertificateError(3
passed in 0.05s).
4

--- Page 5 ---
6 Scope, Limitations, and Conclu-
sion
This work machine-checks the finite-dimensional
algebraic structure underlying Polloreno’s Koashi–
Imoto criterion for Holevo-rate visible compres-
sion [5], certifying qubit Bloch dichotomies,
exact block-tensor KI decompositions, pure-
atom Carath´ eodory mixtures, and sector-
splitting/additivity relations overQ. It does
notformalize the von Neumann entropy continuity
bounds, Fawzi–Renner recovery map, or asymptotic
decoupling converse in Lean 4, and Mode 2/Mode 3
certificates restrict to real-symmetric rational
density matrices (while Mode 1 covers full 3D
rational Bloch vectors). Within this exact al-
gebraic scope, our Lean 4 kernel and zero-float
KOASHI-IMOTO-CERT-1.0auditor deliver sub-
millisecond, manifest-locked verification for visible
quantum compression witnesses.
References
[1] Leonardo de Moura and Sebastian Ullrich. The
Lean 4 theorem prover and programming lan-
guage. InAutomated Deduction – CADE 28,
volume 12699 ofLNCS, pages 625–635. Springer,
2021.
[2] Omar Fawzi and Renato Renner. Quantum
conditional mutual information and approximate
Markov chains.Communications in Mathemati-
cal Physics, 340(2):575–611, 2015.
[3] Patrick Hayden, Richard Jozsa, D´ enes Petz, and
Andreas Winter. Structure of states which sat-
isfy strong subadditivity of quantum entropy
with equality.Communications in Mathematical
Physics, 246(2):359–374, 2004.
[4] Masato Koashi and Nobuyuki Imoto. Opera-
tions that do not disturb partially known quan-
tum states.Physical Review A, 66:022318, 2002.
[5] Anthony M. Polloreno. A Koashi–Imoto crite-
rion for Holevo-rate visible compression. arXiv
preprint arXiv:2611.33129, November 2026.
[6] Benjamin Schumacher. Quantum coding.Physi-
cal Review A, 51(4):2738–2747, 1995.
5
