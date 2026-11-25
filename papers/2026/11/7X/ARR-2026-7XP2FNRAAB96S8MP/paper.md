# Certified Verification of Expansion Testing without Connectivity via Lazy-Walk Return Probabilities

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-7XP2FNRAAB96S8MP` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/expansion-return-prob-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `da33d47e20cb2055727350955a1400ce85be8b3b3eb71fcfd709da98187d865f`

## Abstract

We construct a standalone zero-dependency Lean 4.35.0 formalization of 18 core lazy-walk, finite Cauchy-Schwarz, Dirichlet-energy, trace-gap, integer Bernoulli, induced-expander trimming, balanced-cut farness, non-backtracking polynomial, and three-squares parity theorems (zero sorry, zero warnings, zero Classical.choice) for Nikolas Melissaris (arXiv:2611.32677, Nov 2026), paired with a zero-floating-point exact rational/integer four-mode certificate verifier (EXP-RETPROB-CERT-1.0). Across 16 canonical certificates (0.180-2.195 ms, total 14.53 ms), all exact lazy-walk return probabilities, Lemma 5.3 trimming maximizers, Lemma 7.3 balanced-cut farness lower bounds, Lemma 7.5 non-backtracking polynomials, and Lemma 7.4 three-squares scaling witnesses replay deterministically while rejecting 60/60 live adversarial forgery attacks.

## Full Extracted Text

--- Page 1 ---
Certified Verification of Expansion Testing without
Connectivity via Lazy-Walk Return Probabilities
Lluis Eriksson∗
November 25, 2026
Abstract
Nikolas Melissaris (arXiv:2611.32677, Nov. 2026) broke
Dinur and Goldreich’sn2/3 barrier for testing edge ex-
pansion in every connected component of an arbitrary
bounded-degree graph, achieving˜Od,c,β(n1/2+β/ε+√n/ε4)
queries via two-time lazy-walk return probabilitiesAs =
P2t(s,s)and Bs = P4t(s,s)(Thm. 1.1), alongside an
Ω(
√
n/logn )Cayley-graph lower bound via cyclic lifts
of LPS Ramanujan graphs (Thm. 1.2). We construct a
standalone zero-dependencyLean 4.35.0formalization of
18 core lazy-walk, finite Cauchy–Schwarz, Dirichlet-energy,
trace-gap, integer Bernoulli, induced-expander trimming,
balanced-cut farness, non-backtracking polynomial, and
three-squares parity theorems (zerosorry, zero warnings,
zero Classical.choice) paired with a zero-floating-point
exact Q/Z verifier (EXP-RETPROB-CERT-1.0). Across 16
canonical certificates (0.180–2.195 ms, total14 .53 ms), all
exact lazy-walk return probabilities, Lemma 5.3 trim-
ming maximizers, Lemma 7.3 farness lower bounds, and
Lemma 7.5 non-backtracking polynomials replay deter-
ministically while rejecting 60/60 live adversarial forgery
attacks.
1 Introduction
Testing expansion in bounded-degree graphs [6, 7] nor-
mally assumes connectivity so random walks mix globally
toward1 /n. DinurandGoldreich[ 3]posedtheunrestricted
problemΞ c(n)—testing whether every connected compo-
nent has edge expansion≥c without knowing component
sizes—obtaining n2/3+o(1) queries via three-way collisions.
Melissaris [9] bypassed three-way collisions through four
core mechanisms:
1. Two-Time Return Probabilities & Heavy-Return
Control (Sec. 2.1–2.2, Lem.5.1):Forlazy walkP =
I−L G/(2d), As = P2t(s,s)and Bs = P4t(s,s)satisfy
ps(v)2 ≤AsAv and 1
2d
∑
{u,v}∈E(ps(u)−ps(v))2 ≤As−
Bs. A startsisgoodwhenA s ≤(1 + 2η)Bs andJ s =∑
v∈Ds
ps(v)2 ≤ηB s (Ds = {v : Av > (1 + 8η)As}),
∗Independent Researcher. Code, Lean 4 proofs, and certifi-
cates: MIT License; manuscript and figures: CC-BY-4.0. Pre-
pared with AI coding, formalization, and drafting assistance
from Google Antigravity; all proofs, exact rational/integer veri-
fiers, and adversarial tests were independently compiled and ver-
ified locally. Repository: https://github.com/lluiseriksson/
expansion-return-prob-certificates
certifyinganearlyuniformset Hs = {v: ps(v) ≥3
4 Bs}\
Ds with small boundary andtr(K2t
s )≤ ∑
v∈Hs Av.
2. Trimming to an Induced Expander (Lem. 5.3):
Maximizing F(R) = h
4 |R|−|E (R,H\R )|over |R|≤
|H|/2deletes at most4τ
3h|H|vertices to yield an induced
(h/4)-expanderU=H\R.
3. Balanced-Cut Farness Lower Bound (Lem. 7.2–
7.3):Any connected graph with h(G) ≥h 0 and a
balanced cut|E(A,V\A )|≤h 1|A|(h1 <c∗) requires
M≥min (h0n
2 ,h0|A|,h0(c∗−h1)
h0+c∗ |A|)edge edits to reach
Ξc∗ (n).
4. Non-Backtracking Polynomials,r3(4N) = r3(N),
& Walk-Regularity (Lem. 7.4–7.5, App. A):On
d-regular LPS Cayley graphs [8], non-backtracking poly-
nomials Qk(A)[ 1] and Gauss’s r3(4N) = r3(N)[ 4]
bound adaptive transcript distance, while walk-regular
inputs [5] omit collision-location walks.
Contributions and Scope.We do not formalize ran-
domized query-complexity concentration inequalities in-
side Lean 4; instead, we machine-check the exact al-
gebraic, spectral, cut-trimming, and number-theoretic
core of [9]: (i) 18 zero-sorry, zero-Classical.choice
Lean 4.35.0[2] theorems inExpansionReturnProb.lean;
(ii) the exactQ/Z verifierEXP-RETPROB-CERT-1.0; (iii) 16
canonical certificates across all four modes; and (iv) a
60-attack live red-team suite with 39-artifact SHA-256
manifest enforcement.
2 Constructive Lean 4.35.0 Kernel
The standalone moduleExpansionReturnProb.lean (in
lean/) compiles cleanly under Lean 4.35.0 in1 .2 s
with zero external dependencies, zero warnings, and
zero sorry. Auditing all 18 theorems via #print
axioms (AuditAxioms.lean) confirms 1 zero-axiom theo-
rem (none), 1 using only[propext], 16 using[propext,
Quot.sound], and0using Classical.choice or
Lean.ofReduceBool(Table 1).
Proposition 1(Machine-Checked Spectral & Cut Invari-
ants).The Lean 4.35.0 kernel establishes the following
universal theorems overIntandList Int:
1. Return Probabilities, Bernoulli, & Trimming (Thms. 1–
12):Finite-vector Cauchy–Schwarz( ∑ aibi)2 ≤
(∑ a2
i)(∑ b2
i)and uniform floor( ∑ pi)2 ≤n ∑ p2
i
hold for arbitrary equal-length lists;(1 /2,1/2)and
1

--- Page 2 ---
Table 1: All 18 machine-checked Lean 4.35.0 theo-
rems in ExpansionReturnProb.lean (zero sorry, zero
Classical.choice).
# Lean Theorem Identifier Paper Ref. Axioms
1lazy_walk_row_stochastic_sumSec. 3.1p, Q
2lazy_walk_dirichlet_nonnegLem. 5.1p, Q
3cauchy_schwarz_return_bound_finiteEq. (2)p, Q
4collision_prob_uniform_lower_boundEq. (7)p, Q
5two_point_vs_three_point_collision_ambiguitySec. 1none
6good_vertex_dirichlet_energy_monotonicityLem. 5.1p, Q
7heavy_return_set_size_boundLem. 5.1p, Q
8restricted_trace_le_unrestricted_sumEq. (9)p, Q
9bernoulli_lower_bound_intLem. 5.4p, Q
10second_eigenvalue_trace_gap_boundLem. 5.4p, Q
11trimming_maximizer_size_boundLem. 5.3p, Q
12trimming_maximizer_contradictionLem. 5.3p, Q
13farness_balanced_cut_tradeoffLem. 7.3p, Q
14fixed_neighbor_table_compaction_boundRem. 6.2p, Q
15cayley_cyclic_cut_edge_countLem. 7.2p
16nonbacktracking_poly_recurrence_deg3Lem. 7.5p, Q
17three_squares_scaling_invariance_stepLem. 7.4p, Q
18walk_regular_short_walk_spectral_diffLem. A.2p, Q
Axiom key: none = zero axioms (1);p = [propext] (1); p, Q = [propext, Quot.sound] (16).
(2/3,1/6,1/6)share collision probability1 /2with dis-
tinct F3; cleared spectral inequalities x4(D−x ) ≤
D3x2(D2 −x2)and( D−b )k Bernoulli lower bounds
hold universally;3 B≤ 4pi ⇒9B2|S|≤ 16 ∑ p2
i; and
Lemma 5.3 trimming satisfies3h|R|≤ 4τm and strict
improvementF(R∪S)−F(R)>0.
2. Farness, Non-Backtracking, & Three-Squares
(Thms. 13–18):Eliminating s from M≥h 0s and
M≥ (c∗−h1)A−c∗syields( h0 +c∗)M≥h 0(c∗−h1)A;
Q2(p + 1) = ( p + 1)p and Q3(p + 1) = ( p + 1)p2;
x2
1 + x2
2 + x2
3 = 4N forces all three coordinates even;
and x2(D−x )2 ≤x2(D2 −x2)holds for all0 ≤x≤D .
3 ExactQ/ZCertificate Verifier
The verifier EXP-RETPROB-CERT-1.0
(src/expansion_certifier.py,
src/expansion_exact.py) uses pure Python int
and fractions.Fraction exclusively (source-audited for
zero float(, math., or numpy). Every payload enforces
strict JSON typing (rejecting floats, bool-as-int, int-as-
bool), canonical reduced rationals (forbidding"-0" and
"/1"), nesting-depth cap32, full ASCII control-character
filtering, 2048-bit integer caps, and exact container/key
validation across four modes:
1. Mode 1 (Sec. 2.1–2.2 & Lem. 5.1 Good-Start
Return Audit):Builds P = I−L G/(2d)over Q,
computes Pt,P2t,P4t, checks Eq. (1), (2), (7), Dirichlet
energy ≤A s −Bs, exact Ds,Js,Hs, total variation
dTV(ps,uHs ),|∂H s|, andtr(K2t
s )≤ ∑
v∈Hs Av.
2. Mode 2 (Lem. 5.3 Induced-Expander Trimming):
Exhaustively checks|E(S,V\S )|≥h|S| for everyS⊆
H (|S| ≤ |H|/2), computes exact maximizer R∗ of
F(R), checks|R∗|≤ 4τ
3h|H|, and certifies exact induced
expansionh(G[H\R ∗])≥h/4.
3. Mode 3 (Lem. 7.3 Balanced-Cut Farness):Com-
putes exact global expansionh0 = h(G) >0, cut ratio
Figure 1: (a) Exact lazy-walk return ratioAs/Bs across
walk lengths t∈ {1,..., 6} on disjoint K4 + K4, 1-
bridge barbell K4 −K4, and path P8. (b) Exact non-
backtracking return probabilitiesRG(k)from Qk(A)on
Petersen (girth 5),Q3, andK3,3 (girth 4).
h1 < c∗, and exact rational edit/distance floorsMlb
andε lb =Mlb/(2dn).
4. Mode 4 (Lem. 7.4–7.5 Non-Backtracking &
Three-Squares):Audits exact d-regular matrices
Qk(A)(row sums d(d− 1)k−1, traces, return proba-
bilities RG(k), walk-regularity) and Gauss’sr3(4N) =
r3(N)paired with equal- F2, unequal- F3 collision-
ambiguity distributions.
4 Empirical Atlas and Red-Team
Audit
Running run_all_experiments.py generates 16 canon-
ical certificates (4 per mode) and four exact datasets,
audited end-to-end byverify_all.py with SHA-256 ver-
ification across all 39 tracked artifacts.
Return Ratios & Non-Backtracking Polynomials
(Fig. 1).Mode 1 (1 .700–2.195 ms) certifies good starts
on disjointK4 + K4 (As/Bs = 4288/4099 <1.10, |Hs|=
4,|∂Hs|= 0) and asymmetricK5 + K3 (|Hs|= 5,|Ds|=
3,Js = 0), while rejecting both the 1-bridge barbellK4−K4
(whose ratio rebounds from1 .172at t = 4to1 .205at
t = 6) and path P8 (As/Bs > 1.34). Mode 4 (0 .180–
0.501 ms) certifiestr(Qk(A)) = 0below girth on Petersen
(k≤ 4, tr(Q5) = 120, R5 = 1/4) andK3,3 (tr(Q4) = 72,
R4 = 1/2), both walk-regular.
Trimming, Farness, & Three-Squares (Fig. 2).
Mode 2 (0.280–0.620 ms) certifies exact Lemma 5.3 trim-
ming across cleanK5 (R∗= ∅), dangling boundary vertices
on K5 and K6 (|R∗|= 1, h(G[U]) = 3), and a 2-vertex
appendage on K4 (|R∗| = 2, h(G[U]) = 2). Mode 3
(0.433–1.979 ms) certifies exact farness floors Mlb ∈
{3/5,22/19,4/3,4/5}(εlb ∈{3/320,11/950,1/36,1/90}).
Mode 4 also certifiesr3(56) = r3(14) = 48and r3(108) =
r3(27) = 32alongside exact equal- F2 ambiguity pairs
(F2 = 1/2,∆F3 = 1/18;F 2 = 1/3,∆F3 = 1/36).
2

--- Page 3 ---
Figure 2: (a) Exact Lemma 7.3 balanced-cut farness edit
floors Mlb versus internal expansion h0(G)across four
connected graphs. (b) Exact three-squares representation
count r3(N) = r3(4N)verified for allN∈ [1,30]( r3(N) =
0atN∈{7,15,23,28}).
Figure 3: (a) ExactQ/Z replay latency (0.180–2.195 ms)
across all 16 canonicalEXP-RETPROB-CERT-1.0 certificates.
(b) Live adversarial red-team audit rejecting 60/60 forged
payloads across all five categories.
Replay Latency and 60/60 Red-Team Audit
(Fig. 3).All 16 canonical certificates replay deter-
ministically in0 .180–2.195 ms (total14 .53 ms). The
live adversarial suite (tests/test_suite.py) tests 60
targeted forgeries—12 global schema/typing/canonical-
rational/depth/control-char attacks plus 12 domain at-
tacks per mode (self-loops, degree overflows, corrupted
As/Bs, unsorted sets, invalidh-bounds, disconnected cuts,
c∗≤h1, non-regularQk, mismatchedr3(4N), and identi-
calF 3 pairs)—achieving60/60 (100%)rejection.
5 Conclusion
We delivered a standalone, zero-floating-point verifica-
tion framework for Melissaris’s return-probability expan-
sion testing theory [9], combining 18 zero-sorry, zero-
Classical.choice Lean 4.35.0 theorems with the exact
Q/Z verifier EXP-RETPROB-CERT-1.0, 16 canonical certifi-
cates, and 60/60 live adversarial forgery rejections.
References
[1] Noga Alon, Itai Benjamini, Eyal Lubetzky, and
Sasha Sodin. Non-backtracking random walks mix
faster.Communications in Contemporary Mathemat-
ics, 9(4):585–603, 2007.
[2] Leonardo de Moura and Sebastian Ullrich. The Lean 4
theorem prover and programming language. InAuto-
mated Deduction – CADE 28, volume 12699 ofLecture
Notes in Computer Science, pages 625–635. Springer,
2021.
[3] Irit Dinur and Oded Goldreich. Expansion without
connectivity: A property testing perspective. Technical
Report TR25-129, Electronic Colloquium on Compu-
tational Complexity (ECCC), 2025.
[4] Michael Filaseta, Jonah Klein, and Cihan Sabuncu.
On extreme values ofr3(n)in arithmetic progressions.
The Ramanujan Journal, 69(2):Article 42, 2026.
[5] Chris D. Godsil and Brendan D. McKay. Feasibility
conditions for the existence of walk-regular graphs.
Linear Algebra and its Applications, 30:51–61, 1980.
[6] Oded Goldreich and Dana Ron. Property testing in
bounded degree graphs.Algorithmica, 32(2):302–343,
2002.
[7] Satyen Kale and C. Seshadhri. An expansion tester for
bounded degree graphs.SIAM Journal on Computing,
40(3):709–720, 2011.
[8] Alexander Lubotzky, Ralph Phillips, and Peter Sar-
nak. Ramanujan graphs.Combinatorica, 8(3):261–277,
1988.
[9] Nikolas Melissaris. Testing expansion without con-
nectivity via return probabilities. arXiv:2611.32677
[cs.DS], November 2026.
3
