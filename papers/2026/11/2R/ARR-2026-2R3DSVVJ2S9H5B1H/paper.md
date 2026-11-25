# Machine-Checked Exact-Integer Simultaneous Tiling, Hole-Move Repair, and Laurent Divisibility-Boosting Certificates for Dominoes Tiling a Common Figure

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-2R3DSVVJ2S9H5B1H` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/dominoes-common-figure-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `90757a4acf2ed9a6e71df18e2d738114e4dcb1ab82208cdc4df669fb199ed497`

## Abstract

Peter Keevash and Jeck Lim (arXiv:2611.33154, November 24, 2026) resolved Sagdeev's problem affirmatively (Theorem 1.2): for any finite collection of arithmetic progressions (in particular, dominoes) D_1,...,D_k in Z^2, there exists a finite non-empty lattice figure B in Z^2 partitioned into disjoint translates of every D_i. We present a machine-checked, zero-floating-point formalization and exact-Z certificate auditor for the finite combinatorial, algebraic, and repair core of this work. An 18-theorem zero-dependency Lean 4 kernel (Lean 4.35.0; 0 sorry, 0 warnings, 0 Classical.choice, 2 zero-axiom theorems) formalizes primitive-stretch and common-length LCM partitions, (1-t)D_d(t) = 1-t^d, explicit d=2 and d=3 tile-divisible-yet-untileable gap witnesses (1+t^2+t^3+t^5 and 1+t^2+t^4), exact single step-d hole-move repairs, unimodular det=1 Cramer basis decomposition, Laurent divisibility boosting, and parallel-line conservation. DOMINO-AP-TILING-CERT-1.0 audits four exact modes—including an 8-connected D_4-symmetric 48-cell 4-direction Sagdeev queen-domino figure tiled simultaneously by 24 dominoes in each of (1,0),(0,1),(1,1),(1,-1)—replaying 16 canonical certificates in 0.030-0.292 ms, quantifying the growing Step 5-6 gap (64.9% for d=2, L=10; 82.9% for d=3, L=12), and rejecting 61/61 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Machine-Checked Exact-Integer Simultaneous Tiling,
Hole-Move Repair, and Laurent Divisibility-Boosting
Certificates for Dominoes Tiling a Common Figure
Lluis Eriksson*
November 25, 2026
Abstract
Peter Keevash and Jeck Lim (arXiv:2611.33154,
November 24, 2026) resolved Sagdeev’s problem af-
firmatively (Theorem 1.2): for any finite collec-
tion of arithmetic progressions (in particular, domi-
noes)D 1, . . . , Dk ⊂Z 2, there exists a finite non-
empty lattice figureB⊂Z 2 that can be partitioned
into disjoint translates of everyD i. Their proof
reduces allD i to primitive directions and a com-
mon lengthd, relaxes{0,1}-tileability to integral
Laurent-polynomialtile divisibilityinZ[x ±1
1 , x±1
2 ]
(Step 5, via unimodular basis-change divisibility
boosting), and repairs tile-divisible lines into gen-
uinely tileable lines via step-dhole moves (Step 6).
We present a machine-checked, zero-floating-point
formalization and exact-Zcertificate auditor for the
finite combinatorial, algebraic, and repair core of this
work. First, an 18-theorem zero-dependency Lean 4
kernel (DominoesCommonFigure.lean, Lean 4.35.0;
0sorry, 0 warnings, 0Classical.choice, 2 zero-
axiom theorems) formalizes primitive-stretch and
common-length LCM partitions, (1−t)D d(t) =
1−t d, explicitd= 2 andd= 3 tile-divisible-
yet-untileable gap witnesses (1 +t 2 +t 3 +t 5 and
1+t2 +t4), exact single step-dhole-move repairs, uni-
modular det = 1 Cramer basis decomposition, Lau-
rent divisibility boosting, and parallel-line conser-
vation. Second,DOMINO-AP-TILING-CERT-1.0au-
dits four exact modes—including aD 4-symmetric
48-cell 4-direction Sagdeev queen-domino figure
tiled simultaneously by 24 dominoes in each of
(1,0),(0,1),(1,1),(1,−1)—replaying 16 canonical
certificates in 0.030–0.292 ms, quantifying the grow-
* Independent researcher; manuscript prepared with trans-
parent AI assistance via Google Antigravity. Source code,
Lean 4 proofs, and exact certificates:https://github.com/
lluiseriksson/dominoes-common-figure-certificates.
ing Step 5–6 gap (64.9% ford= 2, L= 10; 82.9% for
d= 3, L= 12), and rejecting 61/61 live adversarial
forgeries.
1 Introduction
A two-element subsetD={0, v} ⊂Z 2 is adomino,
and more generallyD={0, v, . . . ,(d−1)v}(d≥2)
is anarithmetic progression (AP). Sagdeev [5] asked
whether every finite family of dominoesD1, . . . , Dk ⊂
Z2 tiles a common finite non-empty figureB⊂Z 2,
noting simple solutions for standard dominoes (2×2
square) and queen dominoes, while adding a sin-
gle gap dominoD 5 ={(0,0),(2,0)}already re-
quired a SAT-discovered 416-cell figure. Keevash
and Lim [3] proved the full general theorem for arbi-
trary APs (Theorem 1.2), coupling the polynomial-
decomposition machinery of their companion pa-
per [4] with a six-step algebraic hypergraph absorp-
tion scheme extending classical Conway–Lagarias
tiling algebra [1].
Three finite algebraic mechanisms drive [3]:
(i) preprocessing arbitrary APs to primitive direc-
tions (v=cv ′ 7→lengthcd) and a common length
L= lcm(c idi) (Section 2); (ii) boosting integral Lau-
rent divisibility inZ[X ±1
1 , X±1
2 ] via unimodular basis
changes det(X1, X2) = 1 and modulo-(X d
1 −1) poly-
nomial lifting (Step 5, Section 2.1); and (iii) bridg-
ing the strict gap between signed integral divisibility
(Q∈Z[t]) and true{0,1}-tileability (Q∈Z ≥0[t]) via
step-dhole moves (Step 6).
Contributions.We formally verify and audit the
finite tiling, preprocessing, gap-repair, and Laurent
divisibility-boosting core of [3] (explicitly scoping our
Lean 4 proofs away from the Markov-chain jagged
boundary construction, almost-perfect matching hy-
1

--- Page 2 ---
pergraph nibble, and asymptoticO(n 1−δ) absorption
constants of Steps 1–4):
1.Zero-dependency Lean 4 kernel
(§3):18 constructive theorems in
DominoesCommonFigure.lean(Lean 4.35.0 [2]),
0sorry, 0 warnings, 0Classical.choice, 2
zero-axiom theorems.
2.Exact-Ztiling & boosting verifier (§4):
DOMINO-AP-TILING-CERT-1.0, auditing simulta-
neous AP tilings, Step 5–6 gap/hole-move repairs,
Section 2.1 unimodular Laurent divisibility lifts,
and primitive/LCM reductions with zero floats.
3.48-cell Sagdeev figure, gap census, & red-
team audit (§5):16 canonical certificates
(including aD 4-symmetric 48-cell 4-direction
Sagdeev figure) replayed in 0.030–0.292 ms, ex-
haustive 1D gap censuses, and 61/61 rejected ad-
versarial forgeries.
2 Algebraic Structure of
Common-Figure Tilings
Identify a finite setB⊂Z 2 withP B(x1, x2) =P
(a1,a2)∈B xa1
1 xa2
2 ∈Z[x ±1
1 , x±1
2 ] and an APD=
{0, v, . . . ,(d−1)v}withPD(x) = Pd−1
j=0 xjv . A
disjoint-translate tiling ofBbyDis equivalent to
PB =P D ·QwithQ∈ {0,1}[x ±1
1 , x±1
2 ], whereastile
divisibility(Step 5) relaxesQtoZ[x ±1
1 , x±1
2 ]. Along
a 1D line, even simple sets exhibit a strict gap:
1 +t 2 +t 3 +t 5 = (1 +t)(1−t+ 2t 2 −t 3 +t 4),
1 +t 2 +t 4 = (1 +t+t 2)(1−t+t 2),
(1)
both divisible inZ[t] yet untileable (sinceq 0 = 1
forcesq 0 +q 1 ≥1̸= 0 for anyq 0, q1 ∈N). Moving a
single hole by a multiple ofd(17→5 ford= 2; 17→4
ford= 3) preserveshmoddwhile eliminating every
negative coefficient ofQ.
In Step 5 divisibility boosting (Section 2.1 of [3]),
fix a unimodular lattice basis (e1, e2) ofZ 2 withe 1 =
vi, det(e 1, e2) = 1, and express prior directions as
vj =u (j)
1 e1 +u (j)
2 e2 (j < i). Associating formal Lau-
rent indeterminates (X 1, X2) to (e 1, e2) and writing
π:Z[X ±1
1 , X±1
2 ]→Z[X ±1
1 , X±1
2 ]/(Xd
1 −1) for reduc-
tion moduloX d
1 −1, letF ∗ ∈Z[X ±1
1 , X±1
2 ] denote a
canonical reduced representative withX 1-exponents
in{0, . . . , d−1}satisfying (Xd
1 −1)|(f−F ∗). Given
fdivisible byX du(j)
−1 for allj < i, liftingF∗ to any
Fwithπ(F) =π(F ∗) and (X du(j)
−1)|F(j < i)
produces the boosted differencef−Fsatisfying
(Xd
1 −1)|(f−F),
(Xdu(j)
−1)|(f−F) (∀j < i).
(2)
3 Zero-Dependency Lean 4 Kernel
We formalize 18 constructive theorems
inlean/DominoesCommonFigure.lean
(Lean 4.35.0, zero external libraries), audited via
lean/AuditAxioms.leanwith 0 warnings, 0sorry,
0Classical.choice, and 0Lean.ofReduceBool
(Table 1, which gives the exact Lean 4 statement
and axiom footprint of every theorem).
Proposition 1(Constructive Domino & Boosting
Kernel).
1.Tiling & preprocessing partitions (Thms. 1–4, 16–
18):Provesd|qd, disjoint horizontal/vertical
tilings of the2×2square, bijective residue-class
partitionr+jc < cdfor primitive stretch-
ing, consecutive LCM block partitionsjd+r <
qd, Minkowski product divisibility,lcm(d 1, d2)|
|B|, and inductive parallel-line sum conservation
AllDiv d slices→d|listSumNat slices.
2.Laurent gap & hole-move repair (Thms. 5–12):
DefiningevalAP t d= Pd−1
j=0 tj, provesD d(1) =
d,(1−t)D d(t) = 1−t d, domino checkerboard bal-
ance, both exact gap witnesses(1)with¬∃q 0, q1 :
N, q0 = 1∧q 0 +q1 = 0,(h+rd) modd=hmodd,
and single-move repairs ford= 2,3.
3.Unimodular basis & divisibility boosting
(Thms. 13–15):Certifies exact integer Cramer de-
compositionu 1e1 +u 2e2 =vfromdet(e 1, e2) = 1,
simultaneous divisibility boosting(2)via
Int.dvd sub, andmod(X d
1 −1)lift congru-
enceM|(F−F ∗)∧M|(f−F ∗)→M|(f−F).
4 Exact-Integer Certificate Archi-
tecture
The pure-stdlib verifiersrc/domino certifier.py
auditsDOMINO-AP-TILING-CERT-1.0certificates
with zero floating-point arithmetic and strict JSON
AST typing (rejectingfloat,bool,Decimal,
complex, tuples, and non-string keys) across four
exact modes:
Definition 1(FourDOMINO-AP-TILING-CERT-1.0
Modes).
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 kernel inDominoesCommonFigure.lean(0sorry, 0 warnings,
0Classical.choice), showing exact formalized statements and#print axiomsfootprints.
# Lean 4 Theorem Identifier Exact Formalized Statement (Cleared / Inductive Type) Axioms
1ap tiling cardinality divisible∀q, d:N, d|q·dnone
2standard 2x2 square tiled both2×2 disjoint (1,0) and (0,1) domino covers (decide)none
3ap primitive stretch partitionr 1, r2 < c, j1 < d⇒r 1+j1c < cd∧injective[p, Q]
4ap lcm common length dividesr 1, r2 < d, j1 < q⇒j 1d+r1 < qd∧injective[p, Q]
5laurent ap poly eval one∀d:N,evalAP1d= (d:Z)[p, Q]
6laurent ap poly times diff telescope∀t:Z, d:N,(1−t)·evalAPt d= 1−t d [p, Q]
7laurent domino checkerboard balance∀Q:Z,(1 + (−1))·Q= 0[p]
8tile divisible gap witness d21+t 2+t3+t5 = (1+t)(1−t+2t2−t3+t4)∧ ¬∃q0, q1 :N, q0=1∧q 0+q1=0[p, Q]
9tile divisible gap witness d31+t 2+t4 = (1+t+t2)(1−t+t2)∧ ¬∃q0, q1 :N, q0=1∧q 0+q1=0[p, Q]
10hole move step d preserves mod d∀h, r, d:N,(h+r·d) modd=hmodd[p]
11hole move repairs d2 gap∀t:Z,(1+t 2+t3+t5) + (t−t 5) = (1+t)(1+t2)[p, Q]
12hole move repairs d3 gap∀t:Z,(1+t 2+t4) + (t−t 4) = 1+t+t2 [p, Q]
13unimodular basis change det onex 11x22 −x 12x21 = 1⇒u 1e1 +u 2e2 =v(Cramer coords)[p, Q]
14divisibility boost transitivityA|f∧A|F∧B|(f−F)⇒A|(f−F)∧B|(f−F)[p]
15mod Xd minus 1 lift congruenceM|(F−F ∗)∧M|(f−F ∗)⇒M|(f−F)[p, Q]
16minkowski product tiling divd 1 |n 1 ∧d 2 |n 2 ⇒d 1 |n 1n2 ∧d 2 |n 1n2 [p]
17common figure lcm divides sized 1 | |B| ∧d2 | |B| ⇒lcm(d1, d2)| |B|[p, Q]
18line partition sum conservation∀slices:ListN,AllDivdslices⇒d|listSumNat slices [p]
Axiom key:none= zero axioms (2);[p]=[propext](5);[p, Q]=[propext, Quot.sound](11).
1.Mode 1(common figure ap tiling exact): Au-
dits a finite figureB⊂Z 2, APsD 1, . . . , Dk,
disjoint translate tilings coveringBidentically,
bivariate Laurent productsP Di Qi =P B, and
lcm(di)| |B|.
2.Mode 2(tile divisible vs tileable exact):
Audits an initial 1D set that isD d-divisible in
Z[t]yet untileable (minQ 0 <0), applies exact
step-dhole moves(h new −h old)≡0 (modd),
and verifies the repaired set is{0,1}-tileable
(minQ 1 ≥0).
3.Mode 3(divisibility boosting lift exact):
Auditsdet(X 1, X2) = 1, non-parallel prior direc-
tionsu (j), reducedF ∗ (0≤e 1 < d), preconditions
(Xdu(j)
−1)|fand(X d
1 −1)|(f−F ∗), exact
lift congruenceπ(F) =π(F ∗), non-zero boosted
remainderf−F̸= 0, and boosted divisibility(2)
along allu (j) andX 1.
4.Mode 4(ap primitive lcm reduction
exact): Audits primitive scalingv=cv ′
(c= gcd(|v x|,|v y|)), explicit disjoint stretch
partition of[0, cd), common lengthL= lcm(c idi),
and tile countsL/(c idi).
5 Empirical Atlas and Red-Team
Verification
All 16 canonical certificates and four experi-
ment logs are generated deterministically by
scripts/run all experiments.pyand audited
end-to-end byscripts/verify all.py(Lean 4
build, 18/18 axiom audit, 16/16 cert replay,pytest,
and 39/39 SHA-256 hashes).
1. Exact 48-cellD 4-symmetric 4-direction
Sagdeev figure.By exhaustiveD 4-orbit search on
[0..9]2, we construct an 8-connected (king-connected;
four color-coded 12-cell 4-connected lobes touching
diagonally at corners around a central 2×2 void
{4,5}2 and four corner-adjacent voids, with sym-
metric row sizes|B y|= (2,4,4,6,8,8,6,4,4,2) sum-
ming to 48),D 4-symmetric 48-cell common figure
simultaneously tiled by 24 dominoes ineachof
the four queen directions (1,0),(0,1),(1,1),(1,−1)
(Keevash–Lim Theorem 1.2 places no 4-connectivity
requirement onB⊂Z 2). Figure 1 dis-
plays its exact horizontal and diagonal tilings;
fig 48cell 4dir sagdeevverifies all 96 domino
placements and all four bivariate Laurent identities
PDi Qi =P B in 0.292 ms.
2. Quantifying the Step 5–6 gap and Sec-
tion 2.1 lifts.Figure 2(a) exhaustively counts 1D
3

--- Page 4 ---
Figure 1: ExactD 4-symmetric 48-cell 4-direction
Sagdeev queen-domino figure (four color-coded 12-
cell lobes; row sizes|B y|= (2,4,4,6,8,8,6,4,4,2),
total 48 cells): (a) 24 disjoint (1,0) tiles; (b) 24 dis-
joint (1,1) diagonal tiles covering every cell (vertical
and anti-diagonal tilings follow byD 4 symmetry and
are independently audited).
Figure 2: (a) Exhaustive 1D census of tileable ver-
sus strictly tile-divisible-only subsets ford= 2 (L=
4..10) andd= 3 (L= 6..12). (b) Monomial support
sizes across our four Section 2.1 Laurent divisibility-
boosting lifts.
Dd-divisible versus{0,1}-tileable subsets across box
lengthsL∈ {4,6,8,10}(d= 2) andL∈ {6,9,12}
(d= 3): the strict gap fraction grows rapidly withL,
reaching 163/251 (64.9%) atd= 2, L= 10 and
286/345 (82.9%) atd= 3, L= 12, demonstrat-
ing why Step 6 hole-move repair is essential. Fig-
ure 2(b) tracks nonzero Laurent monomials off,F ∗,
and liftedFacross our four Section 2.1 divisibility-
boosting certificates up to 4 directions (i= 4).
3. 16-certificate atlas and 61-attack red-
team suite.Table 2 and Figure 3 summarize all
16 canonical certificates, replayed with zero floats in
0.030–0.292 ms. Intests/test suite.py, indepen-
dent tests verify the exhaustived= 2,3 gap censuses,
confirm exactD 4 symmetry and 24-tile counts on the
48-cell Sagdeev figure, replay all 16 certificates, and
confirm 61/61 live adversarial forgeries (overlapping
Figure 3: (a) Zero-float replay latency across all 16
canonicalDOMINO-AP-TILING-CERT-1.0certificates
(0.030–0.292 ms, log scale). (b) Balanced 4-per-mode
coverage across all four verification modes.
Table 2: Summary of all 16 exact-Z
DOMINO-AP-TILING-CERT-1.0certificates (zero
floating-point arithmetic; reference-machine replay
latency in ms).
Certificate File (stem) Mode Key Exact Witness ms
fig2x2standarddominoesM1 4 cells, 2 dirs, lcm = 2 0.060fig2x3mixedap23M1 6 cells,d∈ {2,3}, lcm = 6 0.057fig8cell3dirknightM1 8 cells, 3 dirs incl. (2,1) 0.066fig48cell4dirsagdeevM1 48 cells, 4 queen dirs (D4) 0.292gaprepaird2singleM2d= 2: minQ:−1→0 (1 move) 0.039gaprepaird3singleM2d= 3: minQ:−1→1 (1 move) 0.033gaprepaird2doubleM2d= 2: minQ:−2→0 (2 moves) 0.040gaprepaird4doubleM2d= 4 (2-hole gap): minQ:−1→1 (1 move) 0.030boostd21prevdiagM3d= 2, 1 prev dir,|f−F|1= 8 0.073boostd31prevshearM3d= 3, 1 prev dir,|f−F|1= 8 0.069boostd22prevqueensM3d= 2, 2 prev dirs,|f−F|1= 6 0.085boostd23prev4dirM3d= 2, 3 prev dirs,|f−F|1= 8 0.109reducegapdominod5M4 5 APs (incl.D5),L= 4 0.054reducemixedaps234M4d∈ {2,3,4} →L= 12 0.036reducescaledvectorsM4 non-prim (2,2),(3,0),(0,−2)→12 0.036reducecoprimeprimeapsM4d∈ {2,3,5} →L= 30 0.033
tiles, duplicate/sign-reversed APs, non-multiple-d
hole moves, already-tileable inputs, det(X1, X2)̸= 1,
vacuous zero-remainder or unreduced-F ∗ lifts, bro-
ken lift congruences, and wrong LCM counts) are
rejected withDominoTilingCertificateError.
6 Scope, Limitations, and Conclu-
sion
This work machine-checks the finite tiling, prepro-
cessing, tile-divisibility gap, step-dhole-move repair,
unimodular basis-change, and Laurent divisibility-
boosting core of Keevash and Lim [3], providing a
zero-float exact-Zcertificate auditor and an explicit
48-cellD 4-symmetric 4-direction Sagdeev figure. It
doesnotformalize the probabilistic Markov-chain
jagged boundary construction, hypergraph almost-
perfect matching nibble, or general existence proof
of Theorem 1.2 in Lean 4. Within its verified scope,
the Lean 4 kernel andDOMINO-AP-TILING-CERT-1.0
4

--- Page 5 ---
auditor deliver exact, manifest-locked verification for
simultaneous lattice AP tilings and absorption lifts.
References
[1] John H. Conway and Jeffrey C. Lagarias. Tiling
with polyominoes and combinatorial group the-
ory.Journal of Combinatorial Theory, Series A,
53(2):183–208, 1990.
[2] Leonardo de Moura and Sebastian Ullrich. The
Lean 4 theorem prover and programming lan-
guage. InAutomated Deduction – CADE 28,
pages 625–635. Springer, 2021.
[3] Peter Keevash and Jeck Lim. Dominoes tiling a
common figure, 2026. arXiv:2611.33154, Novem-
ber 24, 2026.
[4] Peter Keevash and Jeck Lim. Efficient reconfig-
uration, polynomial decompositions and approx-
imate counting, 2026. arXiv:2611.33120, Novem-
ber 24, 2026.
[5] Andrey Sagdeev. Dominoes tiling a common fig-
ure. MathOverflow Question, 2024.
5
