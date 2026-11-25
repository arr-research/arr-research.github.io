# Machine-Checked Exact-Rational Tower Transition, d-Closed Barrier, and Outward-Witness Certificates for Majority Bootstrap Percolation

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6J82K19XZT9GTR9V` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/bootstrap-tower-transition-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `17e650e4b0e750500b3137f500780b85f3e6619059226a677444637ef327879f`

## Abstract

Vyacheslav Koval and Yuval Peres (arXiv:2611.33087, November 24, 2026) resolved the high-dimensional phase transition of majority (d-neighbour) bootstrap percolation on the discrete torus Z_n^d, proving a sharp tower transition (Theorem 1.1): when H(n)/d -> rho in [0,1] (with H(n) = log*_2 n), the critical density converges to p_rho = (1-rho)/(2-rho), recovering Morris's p = 1/4 <-> rho = 2/3 threshold (Corollary 1.2) and contrasting sharply with the dyadic box limit p_c([n]^d) -> 1 - 2^{-m} at n/d = 1/m (Eq. 1.2). We present a machine-checked, zero-floating-point formalization and exact-Q certificate auditor for the algebraic, combinatorial, barrier-closure, and finite-scale geometric core of these results. An 18-theorem zero-dependency Lean 4 kernel (BootstrapTowerTransition.lean, Lean 4.35.0; 0 sorry, 0 warnings, 0 Classical.choice, 3 zero-axiom theorems) formalizes the tetration tower T_0..T_4, strict monotonicity, the exact cleared bijection p_rho <-> rho_p, Morris's (2/3,1/4) point, expected-support balance v+(2d-v)p=d, inductive Eq. (2.3) d-closed layer closure over arbitrary lists, abstract monotone closure, Lemma 2.1 geodesic overlap margins, Eq. (1.2) dyadic box gaps 1-2^{-m} > 1/2, and Lemma 2.3 rectangle-merge hull bounds. BOOTSTRAP-TOWER-CERT-1.0 audits four exact-Q modes—tower-curve bijections, exact finite Z_n^d/[n]^d filling and Eq. (2.3) d-closed barriers, exact rational Lemma 2.1 binomial tails w_0, and dyadic box limits with l_inf > 2t separated rectangles—replaying 16 canonical certificates in 0.036-0.446 ms and rejecting 60/60 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Machine-Checked Exact-Rational Tower Transition,
d-Closed Barrier, and Outward-Witness Certificates for
Majority Bootstrap Percolation
Lluis Eriksson*
November 25, 2026
Abstract
Vyacheslav Koval and Yuval Peres
(arXiv:2611.33087, November 24, 2026) re-
solved the high-dimensional phase transition of
majority (d-neighbour) bootstrap percolation on
the discrete torusZ d
n, proving a sharptower tran-
sition(Theorem 1.1): whenH(n)/d→ρ∈[0,1]
(withH(n) = log ∗
2 n), the critical density con-
verges top ρ = (1−ρ)/(2−ρ), recovering Morris’s
p= 1/4↔ρ= 2/3 threshold (Corollary 1.2)
and contrasting sharply with the dyadic box limit
pc([n]d)→1−2 −m atn/d= 1/m(Eq. 1.2).
We present a machine-checked, zero-floating-point
formalization and exact-Qcertificate auditor for
the algebraic, combinatorial, barrier-closure, and
finite-scale geometric core of these results. First,
an 18-theorem zero-dependency Lean 4 kernel
(BootstrapTowerTransition.lean, Lean 4.35.0;
0sorry, 0 warnings, 0Classical.choice, 3
zero-axiom theorems) formalizes the tetration
towerT 0, . . . , T4, strict monotonicity, the exact
cleared bijectionp ρ ↔ρ p, Morris’s (2/3,1/4)
point, expected-support balancev+ (2d−v)p=d,
inductive Eq. (2.3)d-closed layer closure over arbi-
trary lists, abstract monotone closure, Lemma 2.1
geodesic overlap margins, Eq. (1.2) dyadic box gaps
1−2 −m >1/2, and Lemma 2.3 rectangle-merge
hull bounds. Second,BOOTSTRAP-TOWER-CERT-1.0
audits four exact-Qmodes—tower-curve bijections,
exact finiteZ d
n/[n]d filling and Eq. (2.3)d-closed
barriers, exact rational Lemma 2.1 binomial tails
w0, and dyadic box limits withℓ ∞ >2tseparated
* Independent researcher; manuscript prepared
with transparent AI assistance via Google Anti-
gravity. Source code, Lean 4 proofs, and exact
certificates:https://github.com/lluiseriksson/
bootstrap-tower-transition-certificates.
rectangles—replaying 16 canonical certificates in
0.036–0.446 ms and rejecting 60/60 live adversarial
forgeries.
1 Introduction
In majority (r=d) bootstrap percolation [3, 2, 1, 6],
vertices of a finite lattice graphZ d
n or [n] d are ini-
tially infected independently with probabilityp, and
at each discrete round any healthy vertex with at
leastdinfected nearest neighbours becomes perma-
nently infected. Koval and Peres [5] uncovered a
strikingtower transitionon thed-dimensional torus
Zd
n: wheneverH(n)/d→ρ∈[0,1]—whereH(n) =
log∗
2 n= min{k:n≤T k}is the iterated base-2 log-
arithm inverting the tetration towerT 0 = 1, Tk+1 =
2Tk—the critical filling probability converges to
pρ = 1−ρ
2−ρ ⇐⇒ρ p = 1−2p
1−p ,(1)
resolving Morris’sp= 1/4 benchmark atρ= 2/3
(Corollary 1.2). By contrast, on the open box [n] d
withn/d= 1/m, boundary corners of degreedforce
a strictly super-half dyadic thresholdp c([n]d)→1−
2−m (Eq. 1.2 of [5]).
The subcritical lower-bound architecture of [5]
rests on deterministic and exact rational pillars:
expected-support balancev+ (2d−v)p=d, the
multi-layerd-closed barrierB(V) =I∪E 0 ∪ ··· ∪
Eh−1 (Eq. 2.3) guaranteeingA ∞ ⊆B(V) whenever
Eh(V)⊆B(V), the exact binomial outward-witness
probabilityw 0 (Lemma 2.1, Eq. 2.4), andℓ ∞ >2t
separated-rectangle merges (Lemma 2.3). Auditing
these finite mechanisms over exactZ/Qarithmetic
eliminates floating-point rounding in deep binomial
tails (>140-bit numerators) and produces indepen-
dently replayable proofs of both finite filling and bar-
rier containment.
1

--- Page 2 ---
Contributions and Scope.We formally verify
and audit the finite algebraic, combinatorial, barrier-
closure, and rational-tail core of [5]. We explicitly
scope our Lean 4 formalization away from the asymp-
totic probabilistic couplings, multiscale renormaliza-
tion, and infinite-dimension limit theorems of [5]:
1.Zero-dependency Lean 4 ker-
nel (§3):18 constructive theorems
inBootstrapTowerTransition.lean
(Lean 4.35.0 [4]), 0sorry, 0 warnings,
0Classical.choice, 3 zero-axiom theorems.
2.Exact-Qfour-mode verifier (§4):
BOOTSTRAP-TOWER-CERT-1.0, auditing tower
bijections, exact finite bootstrap dynamics
and Eq. (2.3)d-closed barriers, exact rational
Lemma 2.1w 0 tails, and Eq. (1.2)/Lemma 2.3
dyadic box and separated-rectangle certificates
with zero floats.
3.Empirical atlas, exact filling polynomials, &
red-team audit (§5):16 canonical certificates
(0.036–0.446 ms), exhaustive 29-configuration fill-
ing polynomials onZ 2
3 vs. [3] 2, Eq. (2.3) barrier
census onZ 3
4, exact-Qw 0 decay sweeps (d=
10..32), and 60/60 rejected live adversarial forg-
eries.
2 Tower Curve,d-Closed Barriers,
and Outward Witnesses
At infection densityp∈(0,1/2), a vertex
withvforced neighbours and 2d−vindependent
Bernoulli(p) neighbours has expected infected degree
v+ (2d−v)p, which equals the thresholddprecisely
atv=ρ pdwhereρ p = (1−2p)/(1−p). On a finite
graphG= (Z d
n or [n]d) with initial seed setIand
integersh, g≥1 satisfyingG bud :=hg < d, define
the Eq. (2.3) layers inductively:
E0 ={v /∈I: degI(v)≥d−hg},
Ei ={v: deg Ei−1 (v)> g}(1≤i≤h), (2)
and setB(V) =I∪E 0 ∪ ··· ∪Eh−1. Whenever
Eh ⊆B(V), any vertexv /∈B(V) has at most
d−hg−1 neighbours inIand at mostgneighbours in
each ofE 0, . . . , Eh−1, hence degB(V) (v)≤d−1< d;
thusB(V) isd-closed and traps the entire percola-
tion closureA ∞ ⊆B(V). In Lemma 2.1 (Eq. 2.4),
forg >2h(u=g−2h≥1) andHforced directions,
the exact single-site outward-witness probability is
w0 = (1−p) Pr

Bin(2d−H, p)≥d−hg−2h−H

,
(3)
which evaluates identically inQvia exact integer bi-
nomial coefficients.
3 Zero-Dependency Lean 4 Kernel
We formalize 18 constructive theorems
inlean/BootstrapTowerTransition.lean
(Lean 4.35.0, zero external packages), audited via
lean/AuditAxioms.leanwith 0 warnings, 0sorry,
0Classical.choice, and 0Lean.ofReduceBool
(Table 1).
Proposition 1(Constructive Tower-Transition Ker-
nel).
1.Tetration tower & bijection:Theorems 1–7 es-
tablish exactT 0, . . . , T4, inductive monotonicity
Tk < Tk+1, the exact cleared rational inverse
pρ ↔ρ p, Morris’s(2/3,1/4)benchmark, strict
monotonicity ofp ρ, exact expected-support balance
v+ (2d−v)p=d, and unit step gain1−p.
2.Eq. (2.3) closure & Lemma 2.1 margins:
Theorems 8–12 prove thed-closed neighbour
sum, inductive arbitrary-length layer sums
d closed layer sum list, abstract monotone
d-closed invariance (A⊆B=⇒A 1 ⊆B),
u=g−2h≥1, and geodesic overlap exponent
⌊u/(2(i+ 1))⌋ ≥1.
3.Eq. (1.2) dyadic box gap & Lemma 2.3 geome-
try:Theorems 13–18 prove exact dyadic thresh-
olds1−2 −m (m= 1..4), inductive strict dom-
inance1−2 −m >1/2for allm≥2, rectangle-
merge hull bound<2L+2t, projection-gap preser-
vation, corner degree deficit2d−d=d, and finite-
graph termination rounds≤ |V| − |A0|.
4 Zero-Float Verifier Architecture
BOOTSTRAP-TOWER-CERT-1.0
(src/bootstrap certifier.py) is a pure-stdlib
Python verifier rejecting all floats, booleans-as-ints,
unreduced fractions, duplicate coordinates, oversized
domains, and schema mismatches across four exact
modes:
1.Mode 1 (tower curve bijection exact):Re-
computesH(n) = log ∗
2 n,ρ= min(H(n)/d,1),
pρ = (1−ρ)/(2−ρ), verifiesρ pρ =ρ, and checks
exact support balancev+ (2d−v)p ρ =dinQ.
2.Mode 2 (bootstrap dynamics closure exact):
Replays exact deterministicd-neighbour boot-
strap percolation onZ d
n or [n] d (|V| ≤256),
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 ker-
nel inBootstrapTowerTransition.lean(0sorry,
0 warnings, 0Classical.choice).
# Lean 4 Theorem Identifier Axiom Footprint
1tower valuesexact none
2tower strictlyincreasing [propext, Quot.sound]
3tower curveinversecleared [propext, Quot.sound]
4tower curvemorrisquarterexact none
5tower curvestrictlydecreasing [propext, Quot.sound]
6expectedsupportbalanceexact [propext, Quot.sound]
7mean deficitstepreduction [propext, Quot.sound]
8d closedbarrierneighboursum [propext, Quot.sound]
9d closedlayersumlist [propext, Quot.sound]
10bootstrapmonotoneclosurestep [propext, Quot.sound]
11outwardwitnessuposandmargin [propext, Quot.sound]
12outwardwitnessgeodesicoverlap [propext, Quot.sound]
13box transitiondyadicexact none
14box vstorussharpgap [propext, Quot.sound]
15rectanglemergehullbound [propext, Quot.sound]
16rectangleprojectiongappreserved [propext, Quot.sound]
17torusvsboxdegreebound [propext, Quot.sound]
18bootstrapfiniteterminationbound [propext, Quot.sound]
certifying either full filling (|A ∞|=n d, exact
rounds) or a non-vacuous Eq. (2.3)d-closed bar-
rier (Eh ⊆B(V),|B(V)|< n d,A ∞ ⊆B(V)).
3.Mode 3 (outward witness geodesic exact):
Validates 4≤d≤32,p∈(0,1/2)∩Q(den(p)≤
1000),g >2h, and recomputes the exact rational
binomial tailw 0 of Eq. (3).
4.Mode 4 (box dyadic and rect merge exact):
Certifies 1−2 −m (Eq. 1.2) and Lemma 2.3 sepa-
rated rectangles: every mark covered, every rect-
angle non-empty with side< L, and exact pair-
wiseℓ ∞ separation>2t.
5 Empirical Atlas and Red-Team
Audit
Runningscripts/run all experiments.pygener-
ates 16 canonical certificates (4 per mode) and
four exact-Qexperiments, all verified end-to-end
byscripts/verify all.pywith SHA-256 manifest
checking across all 41 tracked repository artifacts.
Tower Curve and Dyadic Box Gap (Fig. 1).
Mode 1 replays Morris’s exact benchmark atd=
6, n= 65536 (H(65536) = 4, ρ= 2/3, p ρ =
1/4, 0.051 ms), intermediate points (d= 8, n=
16)7→(3/8,5/13) and (d= 10, n= 65536)7→
(2/5,3/8), and the saturated boundary (d= 4, n=
65536)7→(1,0) (0.036 ms). Mode 4 pairs the ex-
act dyadic box limits 1/2,3/4,7/8,15/16 (m= 1..4)
Figure 1: (a) Exact-QTheorem 1.1 torus tower curve
pρ = (1−ρ)/(2−ρ) with Morris’s (2/3,1/4) point
and certified Mode 1 instances. (b) Sharp Eq. (1.2)
dyadic box limit 1−2 −m strictly exceeding the torus
envelopep≤1/2 for allm≥2.
Figure 2: (a) Exact filling probability polynomials
over all 29 = 512 configurations onZ2
3 vs. [3]2, quanti-
fying the finite boundary deficit. (b) Exact Eq. (2.3)
barrier census onZ 3
4 (|V|= 64) for 2×2×2 subcube
prefixes of sizes 4..8.
with Lemma 2.3 separated-rectangle configurations
ind= 2,3,4 attaining exact pairwise separations
ℓ∞ ∈ {3,6,6,8}>2t(0.061–0.072 ms).
Exact Filling Polynomials and Eq. (2.3) Bar-
riers (Fig. 2).Exhaustive enumeration over all
29 = 512 initial configurations onZ 2
3 vs. [3]2 yields
exact rational filling polynomials: atp= 1/4,
Pr1/4(fills) = 17459/32768≈0.5328 onZ 2
3 ver-
sus 18995/131072≈0.1449 on [3] 2; atp= 1/2,
239/256≈0.9336 versus 39/64 = 0.6094, directly re-
flecting the corner degree deficitdvs. 2d. In Mode 2,
Z2
6 fills from a 6-site diagonal in 3 rounds (0.108 ms)
andZ 3
4 fills in 2 rounds (0.175 ms), while punctured
subcubes onZ 3
4 (7→8 sites) and [3] 4 (14→16 sites)
are certified trapped by tight Eq. (2.3)d-closed bar-
riers (|A∞|=|B(V)|<|V|, 0.365–0.446 ms). OurZ 3
4
subcube-prefix census (Fig. 2b) reveals a sharp bud-
get trade-off:h= 1, g= 1 (d−hg= 2) certifies tight
closure (|B|= 4 or 8) on 4/5 prefixes (failing only on
the asymmetric 5-seed prefix), whereash= 2, g= 1
(d−hg= 1) over-expands to 44–56 vertices without
3

--- Page 4 ---
Figure 3: (a) Exact-QLemma 2.1 outward-witness
probabilityw 0(d, p) acrossd= 10..32 (H= 2, h=
1, g= 3). (b) Zero-float replay latency across
all 16 canonicalBOOTSTRAP-TOWER-CERT-1.0certifi-
cates (0.036–0.446 ms).
Table 2: Summary of all 16 canonical
BOOTSTRAP-TOWER-CERT-1.0certificates and 60/60
live adversarial red-team audit.
Verification Mode Certs Latency (ms) Attacks Rejected
Mode 1: Tower-Curve Bijection 4 0.036–0.051 10/10Mode 2: Dynamics & Eq. (2.3) Barrier 4 0.108–0.446 16/16Mode 3: Outward-Witness Tailw0 4 0.134–0.266 10/10Mode 4: Dyadic Box & Rectangles 4 0.061–0.072 12/12Global Schema / Type / Rational – – 12/12
Total 16 0.036–0.446 60/60
closing.
Exact-QOutward-Witness Decay and Red-
Team Audit (Fig. 3, Table 2).In Mode 3, ex-
act rational evaluation of Eq. (3) certifiesw 0 <1/2
acrossd∈ {16,20,24,30}with exact numerators up
to 141 bits in 0.134–0.266 ms. Acrossd= 10..32
(H= 2, h= 1, g= 3),w 0 decays exponentially from
0.4978 (d= 10) to 7.036×10 −6 (d= 32, exact 145-bit
numerator) atp= 1/6. Finally, our adversarial test
suite (tests/test suite.py) mounts 60 live forgery
attacks—including float injection, bool-as-int type
confusion, unreduced fractions, huge-denominator
DoS, false filling claims, unclosed Eq. (2.3) barri-
ers, violatedg >2hmargins, duplicate/uncovered
marks, andℓ ∞ ≤2trectangle collisions—achieving
60/60 rejectionswith zero bypasses.
6 Conclusion
We have delivered a zero-dependency 18-theorem
Lean 4 kernel and an exact-Qcertificate auditor for
the finite algebraic, barrier-closure, outward-witness,
and geometric core of Koval and Peres’s tower tran-
sition in majority bootstrap percolation [5]. Extend-
ing the Lean 4 formalization to quantitative Azuma–
Hoeffding / Talagrand concentration bounds and
multi-scale renormalization couplings remains an at-
tractive direction for future formalized probability.
References
[1] J´ ozsef Balogh, B´ ela Bollob´ as, Hugo Duminil-
Copin, and Robert Morris. The sharp thresh-
old for bootstrap percolation in all dimensions.
Transactions of the American Mathematical So-
ciety, 364(5):2667–2701, 2012.
[2] J´ ozsef Balogh, B´ ela Bollob´ as, and Robert Morris.
Majority bootstrap percolation on the hypercube.
Combinatorics, Probability and Computing, 18(1-
2):17–51, 2009.
[3] John Chalupa, Paul L. Leath, and Gary R. Reich.
Bootstrap percolation on a Bethe lattice.Journal
of Physics C: Solid State Physics, 12(1):L31–L35,
1979.
[4] Leonardo de Moura and Sebastian Ullrich. The
Lean 4 theorem prover and programming lan-
guage. InAutomated Deduction – CADE 28,
pages 625–635. Springer, 2021.
[5] Vyacheslav Koval and Yuval Peres. The tower
transition in majority bootstrap percolation.
arXiv preprint arXiv:2611.33087, 2026.
[6] Robert Morris. Bootstrap percolation, and other
automata.European Journal of Combinatorics,
66:250–263, 2017.
4
