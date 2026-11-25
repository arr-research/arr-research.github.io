# Machine-Checked Exact-Rational Adjugate Perron, Treeplex Stability, and UTC Separation Certificates for Sub-Sqrt(T) Linear Swap Regret in Polyhedral Games

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5G4EGTRH2N9FGTXD` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/linear-swap-regret-polyhedral-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `7d8f53a08a575ab7832dc382e23dc6a893cd46033626b18ff59f100b92aa3f9d`

## Abstract

Vasilis Pollatos and Alberto Marchesi (arXiv:2611.33081, November 24, 2026) broke the sqrt(T) cumulative regret barrier for linear swap regret in self-play over polyhedral games: their deterministic uncoupled optimistic log-barrier dynamics achieve O~(poly(D) T^{1/3}) cumulative linear Phi-regret on arbitrary compact H-polytopes (independent of vertex count) and O(n^2 M^4 log(T+1)) in n-player perfect-recall extensive-form games (EFGs) with at most M terminal sequences per player, extending logarithmic trigger-regret rates to all untimed-communication (UTC) linear deviations. We present a machine-checked, zero-floating-point formalization and exact-Q certificate auditor for the algebraic, adjugate-Perron, stability-to-regret, and UTC-vs-trigger separation core of this breakthrough. First, an 18-theorem zero-dependency Lean 4 kernel (LinearSwapRegretPolyhedral.lean, Lean 4.35.0; 0 sorry, 0 warnings, 0 Classical.choice) formalizes the Lemma 3 path-length bridge (a+b)^2 <= 2(a^2+b^2), Theorem 4 self-play energy cancellation gamma^2 >= 128 n^2 C_*, Eq. (13) parameter choice gamma = 320 n M^2 with 4x exact square margin, T^{1/3} exponent balance at lambda = T^{-2/3}, Appendix G's exact sensitivity chain (2r^2 + r/2 <= (5/2)r^2, (5/2)^2 * 32 = 200, exact Mercator certification log 2 < 23581/34020 < 11/15 => g(2) > 4/15 > 1/16), exact 2x2 column-stochastic adjugate Perron fixed-point and monotonicity identities, Euler derivative bounds |rho'(0)| <= r rho(0), multi-player Cauchy-Schwarz, reset fixed-point contraction, and an exhaustive 16-trigger proof of the Student-Professor UTC gain 3T/2. Second, SWAP-POLYHEDRAL-CERT-1.0 audits four exact-Q modes across 16 canonical certificates (0.192-6.384 ms) and rejects 62/62 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Constructive Lean 4 Algebraic Kernel and Exact-Rational
Certificate Auditor for Sub-
√
TLinear Swap Regret in
Polyhedral Games
Lluis Eriksson*
November 25, 2026
Abstract
Vasilis Pollatos and Alberto Marchesi
(arXiv:2611.33081, November 24, 2026) broke the√
Tcumulative regret barrier for linear swap regret in
self-play over polyhedral games: their deterministic
uncoupled optimistic log-barrier dynamics achieve
˜O(poly(D)T 1/3) cumulative linear Φ-regret on arbi-
trary compactH-polytopes (independent of vertex
count) andO(n 2M4 log(T+ 1)) inn-player perfect-
recall extensive-form games (EFGs) with at mostM
terminal sequences per player, extending logarithmic
trigger-regret rates to all untimed-communication
(UTC) linear deviations. We present a companion
zero-floating-point verification suite combining
an 18-theorem zero-dependency Lean 4.35.0
kernel (LinearSwapRegretPolyhedral.lean;
0sorry, 0 warnings, 0Classical.choice) with
a pure-stdlib exact-Qruntime certificate auditor
(SWAP-POLYHEDRAL-CERT-1.0). The Lean 4 kernel
mechanizes cleared-integer scalar inequalities for
Lemma 3, Theorem 4, Eq. (13), and Appendix G,
exact 2×2 adjugate Perron fixed-point and mono-
tonicity identities, finiter≤6 exponential-factor
checks, inductive Cauchy–Schwarz, and an exhaus-
tive 16-trigger proof of the Student–Professor UTC
gain 3T/2 (explicitly leaving general-mmatrix
Perron theory, FTRL regret dynamics, and recursive
treeplex induction outside Lean 4). Complemen-
tarily,SWAP-POLYHEDRAL-CERT-1.0audits concrete
m×minstances across four exact-Qmodes using
Gaussian determinants, cofactor adjugates, and
certified 5-term Mercator Bregman brackets, replay-
* Independent researcher; manuscript prepared
with transparent AI assistance via Google Anti-
gravity. Source code, Lean 4 proofs, and exact
certificates:https://github.com/lluiseriksson/
linear-swap-regret-polyhedral-certificates.
ing 16 canonical certificates in 0.192–6.384 ms and
rejecting 62/62 live adversarial forgeries.
1 Introduction
In online learning in games, minimizing linear Φ-
regret [4, 3] over compact polyhedral strategy sets
drives play toward linear correlated equilibria, which
in perfect-recall extensive-form games (EFGs) cor-
respond exactly to untimed-communication (UTC)
deviations [6]. Prior efficient algorithms scaled as
O(
√
T), while logarithmic self-play rates [1] were re-
stricted to trigger deviations. Pollatos and March-
esi [5] broke both barriers via three structural pillars
whose notation we fix explicitly:
1.Self-play energy cancellation (Theorem 4):For
strictly positivem×mcolumn-stochastic lifts
A, B, define the scalar log-barrier Bregman gen-
eratorg(u) :=u−1−logu(u >0) and entry-
wise log-barrier Bregman divergenceD R(B, A) :=Pm
a,b=1 g(Bab/Aab)≥0. For reset rateλ∈[0,1),
letx λ
A solve the Gordon reset fixed-point equation
xλ
A = (1−λ)Ax λ
A +λx 0 with total-variation norm
∥sB −s A∥P := 1
2 ∥sB −s A∥1 =∥s B −s A∥TV. Cou-
pling optimistic log-barrier FTRL with fixed-point
stability∥x λ
B −xλ
A∥2
i ≤C ∗DRi(B, A) cancels path-
length prediction error wheneverγ 2 ≥128n 2C∗,
yielding
X
i
LinRegi(T)≤γ
 X
i
m2
i
!
log(T+ 1)
+ 4n
γ + 2n(λT+ 1).
(1)
On generalH-polytopes, reset contraction yields
C∗(λ) =O(poly(D)/λ) and henceγ=
Θ(n√C∗) = Θ(poly(D)λ −1/2); balancingλ −1/2
1

--- Page 2 ---
againstλTin (1) atλ=T −2/3 yields
˜O(poly(D)T 1/3).
2.Adjugate Perron monotonicity & treeplex stability
(Lemmas 7–8, Theorem 9):Given twom×m
column-stochastic treeplex lift matricesA +, A−
(withU= (1−ϵ) ˜Afor the convex combination
˜A= αA++βA−
α+β andϵ∈(0,1)), define the homoge-
neous degree-(m−1) Laplacian pencilL(α, β) :=
α(I−A +) +β(I−A −) and trace denominator
a(α, β) := tr(adjL(α, β)). The resolvent trace
inequality tr((I−U) −1(I−A ±))≥0 implies
∂αa, ∂βa≥0, which via Bernstein’s inequality and
(5/2)2 ·32 = 200 yields theλ= 0 treeplex stability
bound (withC ∗ = 200M4 andγ= 320nM 2):
∥sB −s A∥2
P ≤200m 4DR(B, A),(2)
givingO(n 2M4 log(T+1)) cumulative linear swap
regret inn-player EFGs.
3.UTC vs. trigger separation (Section 1, p. 3):In
the 4-state Student–Professor EFG, each cycle vis-
its 4 equiprobable recommendation pairs (g, b)∈
{0,1}2 with payoff 4·1[a g =b] + 3·1[a b =g]. Ev-
ery one of the 16 pure block-diagonal trigger devi-
ations (ag, ab) = (fg(g), fb(b)) achieves cycle sum
14 (expected payoff 7/2 per cycle, 7T/2 overT
cycles, zero trigger regret), whereas the UTC lin-
ear deviation (ag, ab) = (g, g) (Bad copies Good’s
recommendation) achieves cycle sum 20 (expected
payoff 5T)—a strict UTC swap gain of 3T/2.
Contributions and Explicit Scope.We mecha-
nize the finite scalar/algebraic invariants in Lean 4
while verifying concrete general-mmatrix instances
in a pure-stdlib exact-QPython auditor. We explic-
itly scope our Lean 4 kernelawayfrom FTRL/RVU
regret dynamics, generalm×mPerron monotonicity,
continuous-interval log-barrier calculus, Lemma 5’s
Legendre dual, and Lemma 7’s recursive treeplex-
norm induction:
1.Zero-dependency Lean 4 algebraic
kernel (§2):18 constructive theorems
inLinearSwapRegretPolyhedral.lean
(Lean 4.35.0 [2]), 0sorry, 0 warnings, and
0Classical.choice, with exact formalized
statements reported in Table 1.
2.Pure-stdlib exact-Qverifier (§3):
SWAP-POLYHEDRAL-CERT-1.0, auditing finite
m×madjugate Perron traces, Theorem 9
stability via certified Mercator Bregman brack-
ets, reset-RVU cancellation, and finite EFG
UTC-vs-trigger separation with zero floats.
3.Empirical atlas & red-team audit (§4):16
canonical certificates (0.192–6.384 ms), exact Per-
ron trace profiles, Theorem 9 headroom curves,
closed-form theoretical regret-rate scaling curves,
and 62/62 rejected live adversarial forgeries.
2 Zero-Dependency Lean 4 Kernel
We formalize 18 constructive theorems in
lean/LinearSwapRegretPolyhedral.lean
(Lean 4.35.0, zero external libraries), audited via
lean/AuditAxioms.leanwith 0 warnings, 0sorry,
0Classical.choice, and 0Lean.ofReduceBool
(Table 1: 1 zero-axiom, 3[propext], and 14
[propext, Quot.sound]).
Proposition 1(Constructive Linear-Swap Alge-
braic Kernel).
1.Self-play RVU & rate-balance scalar bounds (The-
orems 1–5, 17–18):Path-length bridge(a+b) 2 ≤
2(a2 +b2); energy cancellation(128n 2C∗ −γ 2)E≤
0; Eq. (13) choiceγ= 320nM 2 attainingγ 2 =
4(128n2 ·200M 4)and4n/γ= 1/(80M 2); induc-
tive nonnegativity boundx∈xs⇒x≤B;T 1/3
balanceT=k·k 2 withk 2 < Tfork≥2; and
scalar reset-contraction stepq d≤(q−p)(d+δ)⇒
p d≤(q−p)δ.
2.Appendix G stability constants & two-sided Mer-
cator check (Theorems 6–10, 14):Quotient bound
4r2 +r≤5r 2; segment floor2((D−t)A+tB)≥
DA; exact constant25·32 = 4·200and large-
divergence bound16≤200m 4; two-sided Merca-
tor arithmetic at endpointsu∈ { 1
2 ,2}: the 2-
term lower bound2( 1
3 + 1
81 ) = 56
81 <log 2cer-
tifiesg( 1
2 ) = log 2− 1
2 > 31
162 > 1
16 , while the
3-term plusk= 3geometric-tail upper bound
log 2< 23581
34020 < 11
15 certifiesg(2) = 1−log 2> 4
15 >
1
16 ; Taylor denominator bound2ξ 2 ≤8D 2; and
(2r+1) r <2(2r) r for the six base casesr= 1. . .6
plus(2r+ 1)/(2r)≤3/2for allr≥1.
3.Exact 2×2 adjugate Perron, Cauchy–Schwarz,
& 16-trigger UTC gap (Theorems 11–13, 15–
16):Exact2×2column-stochastic fixed point
A·(q, p) =D·(q, p)and monotone denomi-
natorα(p 1 +q 1) +β(p 2 +q 2); Euler monotone
derivative bound|d α −d β| ≤rρ 0 fromd α +
dβ =rρ 0 (dα, dβ ≥0); inductive Cauchy–Schwarz
(Pdj)2 ≤ |ds|Pd2
j ; and exhaustive case-split
proof over all 16 pure Student–Professor triggers
(14vs. UTC20, gain6Tover4Tstates= 3T/2).
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 kernel inLinearSwapRegretPolyhedral.lean(0sorry, 0 warn-
ings, 0Classical.choice), with exact formalized statements and#print axiomsfootprints.
# Lean 4 Theorem Identifier Exact Formalized Statement (Cleared Integer / Inductive Type) Axioms
1path length bridge ineq∀a, b:Z,(a+b) 2 ≤2(a2 +b2)[p, Q]
2self play energy cancellation0≤E∧128n 2C∗ ≤γ 2 ⇒(128n2C∗ −γ 2)E≤0[p, Q]
3treeplex eq13 parameterchoiceγ= 320nM 2, C∗ = 200M4 ⇒γ 2 = 4(128n2C∗)∧4n·80M 2 =γ[p]
4individual regret le sumx∈xs∧AllNonnegIntxs∧sumListIntxs≤B⇒x≤B[p]
5t one third exponentbalance2≤k⇒k 3 =k·k 2 ∧k 2 < k3 [p, Q]
6quotient rule five halves bound1≤r⇒4r 2 +r≤5r 2 [p, Q]
7segment entry half lb0≤A,0≤t≤D, A≤2B⇒DA≤2((D−t)A+tB)[p, Q]
8theorem9 constant200 and diameterbranch1≤m⇒25·32 = 4·200∧(m−1) 4 ≤m 4 ∧16≤200m 4 [p, Q]
9log barrierg threshold1 16Two-sided Mercator arithmetic: 56
81−1
2 = 31
162 > 1
16 & 1−23581
34020 > 4
15 > 1
16 none
10log barriersecond deriv floor0≤ξ≤2D⇒2ξ 2 ≤8D 2 [p, Q]
11perron 2x2 adjugateexacts 01+s02 = 1⇒Ladj(L) = 0∧adj(L)s 0 = (q, p)∧A(q, p) =D(q, p)[p, Q]
12perron 2x2 monotonedenominatorp i, qi ≥0, α1 ≤α 2, β1 ≤β 2 ⇒a(α1, β1)≤a(α 2, β2) (2×2)[p, Q]
13euler monotonederivativebound0≤d α, dβ ∧dα +dβ =rρ 0 ⇒ −rρ0 ≤d α −dβ ≤rρ 0 [p, Q]
14rho intervalfactor lt two1≤r⇒2(2r+ 1)≤3(2r), plus (2j+ 1) j <2(2j)j forj∈ {1..6}[p, Q]
15cauchy schwarzsum sq∀ds:ListZ,(sumListIntds) 2 ≤lenIntds·sumSqListIntds[p, Q]
16student professorutc vs triggergap∀f g, fb : Bool→Bool, T≥1 : Trig = 14∧UTC = 20∧∆·T= 6T >0[p, Q]
17reset fixed point contractionq d≤(q−p)(d+δ)⇒p d≤(q−p)δ[p, Q]
18efg logarithmicregret constants(320nM 2)(nM2) = 320n2M4 ∧320nM2 = (4n)(80M2)[p]
Axiom key:none= zero axioms (1);[p]=[propext](3);[p, Q]=[propext, Quot.sound](14).
3 Exact-QVerifier Architecture
SWAP-POLYHEDRAL-CERT-1.0
(src/swap certifier.py) is a pure-stdlib zero-float
verifier using exact Gaussian determinants, classical
cofactor adjugates, Gauss–Jordan inverses, and
certified 5-term Mercator rational brackets for
log(u) across four modes:
1.Mode 1 (perron adjugate monotone cert):
Independently computesL(α, β), adjL,a(α, β) =
tr(adjL), verifies detL= 0, exact Gordon fixed
point ˜As=sfor the normalized convex com-
bination ˜A= αA++βA−
α+β (generalizing the 2×2
unnormalized equationA(q, p) =D(q, p)), mono-
tonicity in (α, β), and Lemma 7’s resolvent traces
tr((I−U) −1(I−A ±))≥0.
2.Mode 2 (treeplex stability theorem9 cert):
Computes exact fixed pointss A, sB, TV-norm
squared∥s B −s A∥2
P , certified rational interval
[Dlb
R , Dub
R ] containingD R(B, A), and verifies∥sB−
sA∥2
P ≤200(m−1) 4Dlb
R ≤200m 4Dlb
R (2).
3.Mode 3 (reset stability and
rvu regret cert):Solves (I−(1−λ)M)x λ =λx 0
exactly overQ, certifiesλ∥x λ
B −x λ
A∥TV ≤
(1−λ)∥(B−A)x λ
A∥TV, checksC ∗ = 200M 4 and
λT≥1, and audits Theorem 4’s energy margin
γ2 −128n 2C∗ ≥0.
4.Mode 4 (utc vs trigger efg
separation cert):Audits finite treeplex
flow partitions, enforces block-diagonal column-
stochasticity on all supplied triggers, indepen-
dently computes the exact global optimum over
all Q
g |g||g| pure block-diagonal triggers to certify
zero trigger regret, verifies vertex-wide invariance
of the UTC map, and certifies strict positive
UTC swap gain.
4 Empirical Atlas and Red-Team
Audit
Runningscripts/run all experiments.pypro-
duces 16 canonical certificates (4 per mode)
and four exact-Qstudies, audited end-to-end by
scripts/verify all.pywith SHA-256 verification
across all 41 tracked artifacts.
Adjugate Perron Profile and Stability Head-
room (Fig. 1).On the 4×4 coupled lift (ρ(0) =
554/125, degreer= 3),ρ(t)/ρ(0) varies monoton-
ically from 1.554621 att=−9/10 to 0.579892 at
t= 9/10, staying well below the Appendix G ceil-
ing 2 across the entire Bernstein window|t| ≤1/6
(and even on [−9/10,9/10]). On the asymmetric
3×3 perturbation familyB τ = (1−τ)A+τB
(τ= 2 −1 . . .2−6), exact certified Mercator brackets
yield empirical stability ratios∥s B −sA∥2
P /Dlb
R (B, A)
rising smoothly from 0.028791 to 0.053589—over four
orders of magnitude below Theorem 9’s worst-case
constant 200(m−1) 4 = 3200 (200m4 = 16200).
3

--- Page 4 ---
Figure 1: (a) Exact adjugate Perron traceρ(t)/ρ(0)
for a 4×4 treeplex lift (ρ(0) = 554/125) staying
strictly below 2 throughout the Bernstein window
|t| ≤1/(2r) = 1/6. (b) Empirical Theorem 9 sta-
bility ratio∥s B −s A∥2
P /Dlb
R (B, A) on an asymmetric
3×3 Markov family acrossτ= 2 −1 . . .2−6 vs. the-
oretical ceilings 200(m−1) 4 = 3200 and 200m 4 =
16200.
Figure 2: (a) Closed-form theoretical regret-rate
curves across horizonsT=k 3 (k= 2. . .128): adver-
sarialT 1/2 vs. generalH-polytopeT 1/3 (λ= 1/k 2)
vs. perfect-recall EFG log(T+ 1) (λ= 0). (b) Ex-
act Student–Professor cumulative payoff (5TUTC
vs. 7T/2 obey/trigger, gain 3T/2).
Sub-
√
TScaling and Student–Professor UTC
Gap (Fig. 2).Mode 3 (0.192–0.637 ms) audits
strictly nonzero reset contractions and RVU can-
cellation across horizonsT∈ {64,125,1000,8000},
including the sharp zero-margin boundaryγ 2 =
12802 = 128·2 2 ·3200. Mode 4 (2.893–6.384 ms)
independently certifies zero global trigger regret over
all Q
g |g||g| pure block-diagonal triggers on the exact
Page 3 Student–Professor separation (35 and 350 for
T= 10,100 vs. UTC 50 and 500, gain 15 and 150),
plus bidirectional and 3-signal (6-sequence) cross-
type UTC separations.
Replay Atlas and Red-Team Audit (Fig. 3,
Table 2).All 16 canonical certificates replay in
0.192–6.384 ms with zero floats (and strictly posi-
tive fixed-point shifts on every Mode 2/3 instance).
Our adversarial suite (tests/test suite.py) tests
Figure 3: (a) Exact zero-float replay latency across
all 16 canonicalSWAP-POLYHEDRAL-CERT-1.0certifi-
cates (0.192–6.384 ms). (b) Red-team adversarial au-
dit rejecting 62/62 live forgery attacks across five at-
tack classes.
Table 2: Summary of all 16 canonical
SWAP-POLYHEDRAL-CERT-1.0certificates and 62/62
live adversarial red-team audit.
Verification Mode Certs Latency (ms) Attacks Rejected
Mode 1: Lemmas 7–8 Adjugate Perron 4 0.255–4.176 12/12Mode 2: Thm. 9 Treeplex Stability 4 0.260–2.812 12/12Mode 3: Reset Contraction & RVU 4 0.192–0.637 12/12Mode 4: UTC vs. Trigger EFG Gap 4 2.893–6.384 14/14Global Schema / Type / Rational – – 12/12
Total 16 0.192–6.384 62/62
62 live forgery attacks—including float/None/bool
injection, unreduced fractions, oversized rational-
string and integer bit-length DoS, non-stochastic or
zero-sum lift matrices, broken energy cancellation
(γ2 <128n 2C∗), cross-group or non-stochastic trig-
gers, hidden omitted-trigger regret bypasses, infeasi-
ble UTC vertex maps, and nonzero trigger-regret in-
stances—achieving62/62 rejectionswith zero by-
passes.
5 Conclusion
We delivered an 18-theorem zero-dependency
Lean 4 kernel (0sorry, 0 warnings,
0Classical.choice) and the exact-Qverifier
SWAP-POLYHEDRAL-CERT-1.0for the adjugate-
Perron, treeplex-stability, RVU energy-cancellation,
and UTC-vs-trigger separation core of Pollatos
and Marchesi [5]. Mechanizing the full recur-
sive treeplex-norm induction of Lemma 7 and
the exponential-family Legendre comparison of
Lemma 5 in Lean 4 remain compelling targets for
future formalized algorithmic game theory.
4

--- Page 5 ---
References
[1] Ioannis Anagnostides, Gabriele Farina, Christian
Kroer, Chung-Wei Lee, Haipeng Luo, and Tuo-
mas Sandholm. Near-optimal no-regret learn-
ing dynamics for general convex games. InAd-
vances in Neural Information Processing Systems
(NeurIPS), volume 36, 2023.
[2] Leonardo de Moura and Sebastian Ullrich. The
Lean 4 theorem prover and programming lan-
guage. InAutomated Deduction – CADE 28,
pages 625–635, 2021.
[3] Gabriele Farina and Charilaos Pipis. Polynomial-
time linear-swap regret minimization in
imperfect-information sequential games. In
Advances in Neural Information Processing
Systems (NeurIPS), volume 36, 2023.
[4] Geoffrey J. Gordon, Amy Greenwald, and Casey
Marks. No-regret learning in convex games. In
Proceedings of the 25th International Conference
on Machine Learning (ICML), pages 360–367,
2008.
[5] Vasilis Pollatos and Alberto Marchesi. Break-
ing the square-root barrier for linear swap regret
in polyhedral games. arXiv:2611.33081 [cs.GT],
November 2026.
[6] Brian Hu Zhang, Gabriele Farina, Ioannis Anag-
nostides, Federico Cacciamani, Stephen McAleer,
Andreas Haupt, Andrea Celli, Nicola Gatti, Vin-
cent Conitzer, and Tuomas Sandholm. Mediator
interpretation and faster learning algorithms for
linear correlated equilibria in general sequential
games. InInternational Conference on Learning
Representations (ICLR), 2024.
5
