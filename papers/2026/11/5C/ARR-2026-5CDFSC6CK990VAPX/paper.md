# Exact Closed-Form Copy-Complexity Step Points, the Consecutive-Node Phase Boundary, and Sharpened Blaschke Duals in Local Quantum State Certification

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5CDFSC6CK990VAPX` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/local-certification-phase-boundary (`v1.0.0`)  
**Canonical PDF SHA-256:** `bbfe936512ee2b42a64934227e2a8daf87ae5a5cc8a04dec57182ecf336097c1`

## Abstract

We resolve the exact phase structure of sharp copy-complexity transitions in local certification of typical pure states introduced by Cao and Bai (arXiv:2611.34742v1). First (Theorem A), we extend Cao and Bai's consecutive-node formula from r <= 2 to all integers r >= 0 and all d > 0: gamma_r(d) >= 2/((d+2)^{r+1} + d^{r+1}) with equality if and only if (d+2)^{r+1} - d^{r+1} <= 2(d+1)^{r+1}. We derive the exact phase-boundary asymptotics d_crit(r) = (r+1)/arsinh(1) - 1 - 1/(2*sqrt(2)) + O(1/r) and discover the first integer-dimension d = r+1 bifurcation jump at r = 9, d = 10 (where 12^{10} - 10^{10} exceeds 2*11^{10} by 0.082%, and fails for every r >= 9). Second (Theorem B), we derive the exact closed-form second-regime step-point formula gamma_r^(2)(d) = 2(r+1)/(2(d+1)^{r+2} + (r-d)(d+2)^{r+1} + (d+r+2)d^{r+1}) for all r >= 2 on the split-node support {1,...,r,r+2,infinity}, unifying Cao and Bai's qubit entries gamma_2(2)=1/35 and gamma_3(2)=4/427 with new exact qudit entries gamma_3(3)=1/337, gamma_4(3)=5/6752, gamma_6(6)=1/1103479, and post-jump gamma_9(10)=10/359352988499. Third (Theorem C), decoupling the +2 constant and optimizing the Cauchy-Schwarz weight lambda* = (1-alpha^2)/(1+alpha^2) in the Blaschke dual reduces the asymptotic constant in Proposition S25 by >21.8% uniformly across all d > 0. The algebraic cores are constructively formalized in Lean 4.35.0 (14 theorems, 0 sorry, 0 Classical.choice, 0 warnings), audited by an AST-verified zero-float exact rational verifier across 16 SHA-256 certificates (LOCAL-CERT-PHASE-1.0) and 47/47 passing tests.

## Full Extracted Text

--- Page 1 ---
Exact Closed-Form Copy-Complexity Step Points, the
Consecutive-Node Phase Boundary, and Sharpened
Blaschke Duals in Local Quantum State Certification
Lluis Eriksson∗
November 2026
Abstract
Cao and Bai [1] recently resolved the asymptotic copy complexityΘ(nr log(1/δ))of local
tensor-product certification for Haar-typicaln-qudit pure states in terms of a decreasing sequence
of rational step pointsγr(d) = 2/(1 +Br(d)), whereBr(d) = sup{G(0) :G∈V r(d),∥G∥X ≤1}
onX=N ≥1 ∪{∞}. While [1] derived closed forms only forr∈{0,1,2}—noting an unexplained
anomalyγ 2(2) = 1/35̸= 1/36atd= 2—and relied on finite enumeration for higher degrees,
we determine the exact analytical phase structure ofγr(d)across all degreesr∈Nand local
dimensionsd>0.
Theorem Aproves the universal exact lower boundγr(d)≥2/
(
(d+ 2) r+1 +dr+1)
for all
r≥0,d>0and establishes anecessary and sufficientalgebraic phase boundary:
γr(d) = 2
(d+ 2) r+1 +dr+1 ⇐⇒(d+ 2) r+1 −dr+1 ≤2(d+ 1) r+1.
This four-line binomial-and-ratio proof generalizes Proposition S33 of [1] fromr≤2to allr∈N,
yields the exact asymptotic phase lined crit(r) = (r+ 1)/arsinh(1)−1− 1
2
√
2 +O(1/r)(≈
1.13459(r+1)−1.35355), and predicts an unexpected integer threshold jump: whiled=r+1lies
in the consecutive-node regime for everyr∈{2,...,8}, it fails for the first time atr= 9,d= 10
(1210 −10 10 = 51,917,364,224>51,874,849,202 = 2·11 10, a0.082%overshoot) and for every
r≥9.Theorem Bderives the exact closed-form formula for the first post-bifurcation regime
(nodes{1,...,r,r+ 2,∞}) for allr≥2:
γ(2)
r (d) = 2(r+ 1)
2(d+ 1) r+2 + (r−d)(d+ 2) r+1 + (d+r+ 2)d r+1 ,
together with an exact crossover identity atd=dcrit(r), unifying Cao and Bai’s isolated qubit
valuesγ2(2) = 1/35andγ 3(2) = 4/427with new exact qudit step points includingγ3(3) = 1/337,
γ4(3) = 5/6752,γ 6(6) = 1/1,103,479, and the post-jump valueγ 9(10) = 10/359,352,988,499.
Theorem Ccombines keeping theO(1)additive term outside √swith optimizing the weighted
Cauchy–Schwarz parameter in Lemma S24 of [1] toλ∗= (1−α 2)/(1 +α2), strictly sharpening
both their Proposition S25 constantDd =
√
(2 +π)/(1−α 2)and the un-loosenedλ= 1bound
for everyd>0ands≥1via1−α 4 <1, reducing the asymptotic constant by>21.8%uniformly
across alld>0.
All 14 core algebraic, binomial-induction, termwise-decay, crossover-identity, integer-jump,
and Blaschke-dominance theorems are formalized constructively in Lean 4.35.0 (0 sorry,0
warnings, zeroClassical.choice); the analytic Chebyshev-space, real-parameter, and integral-
comparison steps are proved in the text and cross-verified by an AST-audited zero-float Python
verifier (LOCAL-CERT-PHASE-1.0, 16 SHA-256 certificates:C01–C13replaying full Lemma S30
shifted-tail certificates andC14–C16verifying exact Blaschke-dual bounds, 47/47 pytest checks).
∗Independent Researcher. Code, Lean 4 proofs, and certificates: MIT License; manuscript and figures: CC-BY-4.0.
Repository:https://github.com/lluiseriksson/local-certification-phase-boundary.
1

--- Page 2 ---
1 Introduction
In local tolerant quantum state certification of a Haar-typicaln-qudit pure target state|ψ⟩∈(Cd)⊗n
under arbitrary (possibly copy-adaptive) tensor-product measurements—building on single-qubit
Pauli certification [4, 2]—Cao and Bai [1] proved that for acceptance and rejection fidelity thresholds
0< b < a≤1with normalized gapg= (a−b)/(1−b), the optimal copy complexity scales as
Θ(nrlog(1/δ))wherer=r d(g) = min{j∈N 0 :g >γj(d)}. The critical transition step pointsγr(d)
aredeterminedbyapurelyreal-analyticextremalproblem(closelylinkedtoWienerinterpolation[5])
on the one-point compactificationX=N ≥1 ∪{∞}:
Vr(d) :=
{
G(x) =h+ (d+ 1) −xR(x) :h∈R, R∈R[x],degR≤r
}
, G(∞) =h,(1)
Br(d) := sup
{
G(0) :G∈V r(d),∥G∥X ≤1
}
, γ r(d) = 2
1 +Br(d).(2)
By Chebyshev-system alternation (Theorem S5 and Lemma S30 of [1]),Br(d)is attained by a unique
extremal functionG∈V r(d)alternating between±1onr+1finite integer nodes1≤j 1 <···<j r+1
andG(∞) = (−1) r+1, matched by a unique finite alternating dual measure(µ1,...,µ r+1,µ∞)with
total variationBr(d).
In Proposition S33 and Table I of [1], closed forms were established only forr∈{0,1,2}:
γ0(d) = 1
d+ 1 (d>0), γ 1(d) = 1
(d+ 1) 2 + 1 (d≥1), γ 2(d) = 1
(d+ 1)((d+ 1) 2 + 3) (d≥3),
together with the isolated qubit exceptionγ2(2) = 1/35(for which the formula atd= 2would give
1/36). Higher values were obtained via finite rational search (Table S1 of [1] ford= 2,r≤10).
This paper explains and resolves the complete phase structure behind these formulas:
1.Exact Consecutive-Node Phase Diagram (Theorem 1):The three formulas of Propo-
sition S33 are ther= 0,1,2instances of a single universal formulaγ r(d) = 2/
(
(d+ 2) r+1 +
dr+1)
, which is an exact lower bound for allr≥0,d >0and holds with equalityif and only
if(d+ 2) r+1 −dr+1 ≤2(d+ 1) r+1. This yields the exact asymptotic phase lined crit(r) =
(r+ 1)/arsinh(1)−1− 1
2
√
2 +O(1/r)and uncovers a striking integer transition:d=r+ 1
lies inside the consecutive regime for allr∈ {2,...,8}yet crosses outside atr= 9,d= 10
(dcrit(9)≈10.0076>10).
2.Exact Second-Regime Formula (Theorem 2):Immediately belowd crit(r), the rightmost
finite contact node shifts fromr+1tor+2. We derive the exact closed-form dual formulaγ(2)
r (d)
for{1,...,r,r+ 2,∞}for allr≥2and an exact algebraic crossover identity atd=d crit(r),
unifyingγ 2(2) = 1/35andγ 3(2) = 4/427with exact new qudit step points up toγ 9(10) =
10/359,352,988,499.
3.Sharpened Blaschke-Dual Constant (Theorem 3):Decoupling the additiveO(1)term
from √sand optimizing the Cauchy–Schwarz weight in Lemma S24 of [1] fromλ= 1toλ ∗ =
(1−α2)/(1+α2)strictly improves both Proposition S25’s constantDd and the un-loosenedλ= 1
bound for everyd>0ands≥1, yielding a>21.8%asymptotic reduction across alld>0.
2 Theorem A: Exact Consecutive-Node Phase Boundary for All
r∈N
Theorem 1(Universal Consecutive-Node Formula and Exact Phase Boundary).Letr≥0be an
integer and letd>0be real.
1.Universal lower bound:For everyr≥0andd>0,
Br(d)≤(d+ 2) r+1 +dr+1 −1, γ r(d)≥ 2
(d+ 2) r+1 +dr+1 .(3)
2

--- Page 3 ---
2.Necessary and sufficient phase boundary:Equality holds in(3)if and only if
(d+ 2) r+1 −dr+1 ≤2(d+ 1) r+1.(4)
Equivalently,γ r(d) = 2/
(
(d+ 2) r+1 +dr+1)
if and only ifd≥d crit(r), wheredcrit(0) = 0and for
r≥1,d crit(r)is the unique positive root of(d+ 2)r+1 −dr+1 = 2(d+ 1) r+1.
3.Asymptotics and first integer jump atr= 9:Asr→∞,
dcrit(r) = r+ 1
arsinh(1) −1− 1
2
√
2 +O
(1
r
)
≈1.134592657 (r+ 1)−1.353553391 +O
(1
r
)
.(5)
Among integer local dimensionsd=r+1, condition(4)holds forr∈{1,...,8}(withd crit(r)>r
for allr≥2, so⌈d crit(r)⌉=r+ 1forr∈{2,...,8}), fails for the first time atr= 9,d= 10
(1210 −10 10 = 51,917,364,224>51,874,849,202 = 2·11 10), and fails for everyr≥9.
Proof.Setx:=d+ 1>1. For anyG(w) =h+x −wR(w)∈V r(d)withdegR≤r, the(r+ 1)-st
forward difference ofRat0vanishes identically:
0 =
r+1∑
j=0
(−1)j
(
r+ 1
j
)
R(j) =⇒R(0) =
r+1∑
j=1
(−1)j−1
(
r+ 1
j
)
xj(
G(j)−h
)
.
Using the binomial identity1−∑r+1
j=1(−1)j−1(r+1
j
)
xj = (1−x)r+1 = (−1)r+1dr+1 (Lean 4 Theorems 1
and 3), everyG∈V r(d)obeys the exact extrapolation formula
G(0) =
r+1∑
j=1
(−1)j−1
(
r+ 1
j
)
xjG(j) + (−1)r+1dr+1G(∞).(6)
Taking absolute values under∥G∥X ≤1and summing by the binomial theorem (Lean 4 Theorem 2)
yields
Br(d)≤
r+1∑
j=1
(
r+ 1
j
)
xj +dr+1 = (x+ 1) r+1 −1 +d r+1 = (d+ 2) r+1 +dr+1 −1,
proving (3) viaγr(d) = 2/(1 +Br(d)).
For Part 2, the caser= 0hasd+ 2−d= 2<2(d+ 1)andγ 0(d) = 1/(d+ 1)unconditionally.
Assumer≥1, and letG(w) =h+x −wR(w)∈V r(d)be the unique interpolant matching the signs
of the dual weights in (6):G(j) = (−1)j−1 forj∈{1,...,r+ 1}andG(∞) =h:= (−1) r+1. Setting
Q(w) := (−1)rR(w), we haveQ(j) = 2xj whenr+ 1−jis even andQ(j) = 0whenr+ 1−jis odd
(1≤j≤r+ 1). By Lagrange interpolation at{1,...,r+ 1},
Q(w) =
∑
1≤j≤r+1
r+1−jeven
Tj(w), T j(w) := 2xj ∏
1≤k≤r+1
k̸=j
w−k
j−k .(7)
Becauser+ 1−jis even, ∏
k̸=j(j−k) = (j−1)!(r+ 1−j)!>0, so every summandT j(w)is strictly
positive for allw≥r+ 2. Note that(−1) rG(w) =−1 +x −wQ(w)satisfies|G(w)|≤1if and only if
0≤a w :=x−wQ(w)≤2.
Necessity.Evaluating (7) atw=r+ 2gives ∏
k̸=j
r+2−k
j−k = (r+1)!
(j−1)!(r+2−j)! =
(r+1
r+2−j
)
. Summing
over evenr+ 1−j(i.e. oddr+ 2−j) yields
Q(r+ 2) = 2x
∑
1≤m≤r+1
modd
(
r+ 1
m
)
xr+1−m =x
(
(x+ 1) r+1 −(x−1) r+1)
=x
(
(d+ 2) r+1 −dr+1)
.(8)
Hencea r+2 =x −(r+2)Q(r+ 2) =
(
(d+ 2) r+1 −dr+1)
/(d+ 1) r+1. If (4) fails, thena r+2 >2, so
|G(r+ 2)|=a r+2 −1>1. Because any functionH∈V r(d)with∥H∥ X ≤1achievingH(0) =
(d+ 2) r+1 +dr+1 −1must saturate every term in (6) and therefore coincide withG(Lemma S1
of [1]), equality in (3) is impossible whenever (4) fails.
Sufficiency (three-step algebraic tail proof).Suppose (4) holds.
3

--- Page 4 ---
1.Lower boundx≥r+ 1:From the odd-index binomial expansion(x+ 1) r+1 −(x−1) r+1 =
2 ∑
k≥0
(r+1
2k+1
)
xr−2k ≥2(r+1)x r (Lean 4 Theorems 4 and 5 for integerx), (4) implies2(r+1)xr ≤
2xr+1, whencex≥r+ 1; forr≥2thek= 1term2
(r+1
3
)
xr−2 >0makes the inequality strict, so
x>r+ 1and henced crit(r)>r.
2.Boundary feasibility atw=r+ 2:By (8) and (4),0<a r+2 ≤2.
3.Monotone decay for allw≥r+ 2:For every integerw≥r+ 2and everyj∈{1,...,r+ 1}with
r+ 1−jeven, the exact ratio of consecutive positive summands in (7) obeys
Tj(w+ 1)
Tj(w) = w
w−(r+ 1) · w−j
w+ 1−j ≤ w
w−(r+ 1) ·w−1
w = w−1
w−(r+ 1) ≤r+ 1≤x,
where(w−j)/(w+ 1−j)≤(w−1)/wholds sincej≥1and(w−1)/(w−r−1)≤r+ 1holds
sincew≥r+ 2(Lean 4 Theorem 6 for integerx). SummingT j(w+ 1)≤xT j(w)over alljyields
Q(w+ 1)≤xQ(w), hence0<a w+1 ≤aw ≤ar+2 ≤2for every integerw≥r+ 2.
Thus∥G∥X ≤1, attaining (3) and proving (4) is both necessary and sufficient.
For Part 3, rewrite (4) asfr(u) := (1 +u)r+1 −(1−u) r+1 ≤2withu= 1/x= 1/(d+ 1)∈(0,1).
Sincef r(0) = 0,f ′
r(u) = (r+ 1)
(
(1 +u) r + (1−u) r)
>0, andf r(1) = 2 r+1 ≥4>2(r≥1),
there is a unique rootur ∈(0,1), hence a uniqued crit(r) = 1/ur −1>0. By Step 1 (x≥r+ 1),
cr := (r+1)ur ∈(0,1]isuniformlybounded. Expanding(1±c r/(r+1))r+1 =e±cr
(
1− c2
r
2(r+1) +O(r−2)
)
gives2 sinh(cr)
(
1− c2
r
2(r+1) +O(r−2)
)
= 2. Settingc 0 := arsinh(1) = ln(1 +
√
2)(wheresinhc 0 = 1
andcoshc 0 =
√
2), implicit inversion gives
cr =c0 + c2
0
2
√
2 (r+ 1) +O(r−2),
whence
dcrit(r) = r+ 1
cr
−1 = r+ 1
c0
(
1− c0
2
√
2 (r+ 1) +O(r−2)
)
−1 = r+ 1
arsinh(1) −1− 1
2
√
2 +O
(1
r
)
,
proving (5) (this− 1
2
√
2 ≈−0.3536shift also explains why the integer crossingd crit(r)> r+ 1is
delayed untilr= 9). Ford=r+ 1(u= 1/(r+ 2)), direct exact integer arithmetic verifies that
r∈{1,...,8}satisfy (4) whiler= 9violates it (Lean 4 Theorem 7), and together withd crit(r)>r
from Step 1 this gives⌈dcrit(r)⌉=r+ 1forr∈{2,...,8}. Moreover, form:=r+ 1≥1, set
g(m) := (1 + 1
m+1 )m andh(m) := (1− 1
m+1 )m. Differentiatinglng(m) =mln(1 + 1
m+1 )and
applyingln(1 +t)>t−t 2/2fort>0gives
d
dmlng(m) = ln
(
1 + 1
m+ 1
)
− m
(m+ 1)(m+ 2)
> 1
m+ 1 − 1
2(m+ 1) 2 − m
(m+ 1)(m+ 2) = 3m+ 2
2(m+ 1) 2(m+ 2) >0,
sog(m)is strictly increasing, whereaslnh(m) =−mln(1 + 1
m)obeys d
dm lnh(m) =−ln(1 + 1
m) +
1
m+1 <− 1
m+1 + 1
m+1 = 0(usingln(1 +t)> t
1+t fort>0), soh(m)is strictly decreasing. Therefore
g(m)−h(m)is strictly increasing for allm≥1. Sinceg(10)−h(10) = (12 10 −10 10)/1110 >2, we
obtaing(m)−h(m)>2for everym=r+ 1≥10, i.e. everyr≥9.
3 Theorem B: Exact Second-Regime Closed-Form Step Points
Immediately below the phase boundarydcrit(r)(r≥2), the rightmost finite contact node shifts from
r+ 1tor+ 2, producing the node configurationN (2)
r ={1,2,...,r,r+ 2,∞}.
4

--- Page 5 ---
Figure 1:Theorem A phase diagram.(a) Exact consecutive-node regiond≥d crit(r)versus
the bifurcated region, with the exact asymptote(r+ 1)/arsinh(1)−1− 1
2
√
2 and the integer line
d=r+ 1. (b) Sign flip ofd crit(r)−(r+ 1)betweenr= 8(−0.125,d= 9valid,C03) andr= 9
(+0.0076,d= 10fails by0.082%,C07).
Theorem 2(Exact Second-Regime Dual Formula and Crossover Identity).For every integerr≥2
and reald>0, define the scaled second-regime denominator
D(2)
r (d) := 2(d+ 1) r+2 + (r−d)(d+ 2) r+1 + (d+r+ 2)d r+1, γ (2)
r (d) := 2(r+ 1)
D(2)
r (d)
.(9)
1.Universal second-regime lower bound:For everyr≥2andd>0,γ r(d)≥γ (2)
r (d)(equiva-
lently1+B r(d)≤D (2)
r (d)/(r+1)). Equalityγr(d) =γ (2)
r (d)holds whenever the unique alternating
interpolantG(2) ∈Vr(d)onN (2)
r satisfies∥G (2)∥X ≤1.
2.Exact phase-boundary crossover identity:For allr≥2andd∈R,
D(2)
r (d)−(r+ 1)
(
(d+ 2) r+1 +dr+1)
= (d+ 1)
(
2(d+ 1) r+1 −
(
(d+ 2) r+1 −dr+1))
.(10)
Consequently,γ (2)
r (d)>2/
(
(d+ 2) r+1 +dr+1)
strictly whenever0< d < dcrit(r), and the two
formulas coincide identically on the phase boundaryd=dcrit(r).
Proof.Setx=d+ 1. For any polynomialRof degree≤r, Lagrange extrapolation to0from nodes
{1,...,r,r+ 2}givesR(0) = ∑
j∈N(2)
r \{∞}cjR(j), where direct product simplification yields
cj = (−1)j−1 r+ 1−j
r+ 1
(
r+ 2
j
)
(1≤j≤r), c r+2 = (−1)r
r+ 1 .
The corresponding dual weights onVr(d)areµ j =cjxj (j∈{1,...,r,r+ 2}) andµ ∞= 1− ∑ µj,
alternating in sign with(−1) r+1µ∞ >0. By the binomial theorem and its weighted derivative
identity ∑r+2
k=0 k
(r+2
k
)
akbr+2−k = (r+ 2)a(a+b) r+1 (Lean 4 Theorems 1 and 10),
r+2∑
j=0
(r+ 1−j)
(
r+ 2
j
)
zj = (r+ 1)(1 +z) r+2 −(r+ 2)z(1 +z) r+1 = (1 +z) r+1(r+ 1−z).
Notice that thej=r+ 1term vanishes identically, while thej=r+ 2term is−z r+2. Evaluating
atz=xand correcting thej= 0term(r+ 1)and the flippedj=r+ 2sign+x r+2 gives
(r+ 1)
∑
j∈{1,...,r,r+2}
|µj|= (x+ 1) r+1(r+ 1−x)−(r+ 1) + 2x r+2.
5

--- Page 6 ---
Table 1: Exact certified step pointsγr(d)from Theorems 1–2 (all replayed via Lemma S30 inC01–
C13).
(r,d)Regime Active finite nodes Exactγ r(d)Consec. LB Cert
(2,2)Second (d<2.104){1,2,4}1/35 1/36C06, C09
(3,2)Second (d<3.224){1,2,3,5}4/427 1/136C10
(3,3)Second (d<3.224){1,2,3,5}1/337 1/353C11
(3,4)Consecutive (d>3.224){1,2,3,4}1/776 1/776C01
(4,3)Second (d<4.351){1,2,3,4,6}5/6752 1/1684C12
(4,5)Consecutive (d>4.351){1,2,3,4,5}1/9966 1/9966C02
(6,6)Second (d<6.611){1,2,3,4,5,6,8}1/1,103,479 1/1,188,544C13
(8,9)Consecutive (d>8.875){1,...,9}1/1,372,684,090 1/1,372,684,090C03
(9,10)Second (jump!d<10.008){1,...,9,11}10/359,352,988,499 1/35,958,682,112C07
(9,11)Consecutive (d>10.008){1,...,10}1/81,897,958,225 1/81,897,958,225C04
Figure 2:Theorem B bifurcation mechanism.(a) Atr= 2,d= 2, the consecutive interpolant
on{1,2,3}overshoots|G(4)|= 29/27>1, while shifting to{1,2,4}restores feasibility and attains
γ2(2) = 1/35(C06, C09). (b) Exact crossover ratioγ (2)
r (d)/γconsec
r (d)meeting unity precisely at
d=d crit(r)per (10).
Evaluating atz=−xgivesµ ∞ = 1
r+1 (1−x) r+1(r+ 1 +x)(thej=r+ 2contributions cancel
identically), so(r+1)|µ∞|= (x−1) r+1(x+r+1). Summing(r+1)(1+ ∑ |µj|+|µ∞|)and substituting
x=d+ 1givesD (2)
r (d)in (9) (in particular,D (2)
r (d) = (r+ 1)(1 + ∑ |µj|+|µ ∞|)> r+ 1>0
unconditionally for everyd >0, even whenr−d <0), proving1 +B r(d)≤D (2)
r (d)/(r+ 1)and
γr(d)≥γ (2)
r (d)with equality whenever∥G (2)∥X ≤1. Subtracting(r+ 1)((d+ 2) r+1 +dr+1)from
D(2)
r (d)directly yields (10) (Lean 4 Theorem 12).
Table 1 lists exact step points certified via Theorems 1–2 and full Lemma S30 shifted-tail replay
(C01–C13). Notably, Theorem 2 reproduces both isolated qubit entriesγ2(2) = 1/35andγ 3(2) =
4/427of [1] and resolves the exact post-jump valueγ9(10) = 10/359,352,988,499atr= 9,d= 10
(C07).
4 Theorem C: Sharpened Blaschke-Dual Asymptotic Constant
In Section VI.A (Lemma S24 and Proposition S25) of [1], the asymptotic lower boundγr(d)≥
2αr+1/(1 +D d
√r+ 1)(α= (d+ 1) −1) is proved by expanding the Blaschke powerb α(z)s =∑
w≥0 cwzw (s=r+1), proving Parseval moments ∑
w≥0 |cw|2 = 1and ∑
w≥0 w2|cw|2 =s2 1+α2
1−α2 , and
applying Cauchy–Schwarz with unweighted factor(1 +w2/s2), yieldingDCB
d =
√
(2 +π)/(1−α 2).
6

--- Page 7 ---
Optimizing the Cauchy–Schwarz balance weight strictly sharpens this bound for everyd >0and
everys≥1.
Theorem 3(Sharpened Blaschke-Dual Lower Bound).For every reald>0(α= (d+1) −1 ∈(0,1))
and every integers=r+ 1≥1, the Blaschke coefficientsc w ofb α(z)s satisfy
∑
w≥0
|cw| ≤
√2 +πs
√
1 +α2
1−α 2 <
√
2 +πs
1−α 2 ≤
√
2 +π
1−α 2 s=D CB
d
√s.(11)
Consequently, for everyr≥0andd>0,
γr(d)≥ 2(d+ 1) −(r+1)
1 +
√
2 +π(r+ 1)
√
(1 +α2)/(1−α 2)
,(12)
reducing the asymptotic constantDd uniformly by1−
√
π
√
1−α 4/(2 +π)>21.8%for every real
d>0(and approaching1−
√
π/(2 +π)≈21.83%asd→∞). Here the gain overD CB
d decomposes
cleanly into two contributions: keeping+2outside√s(which already accounts for the21.83%large-d
limit) and optimizingλ= 1→λ ∗ = (1−α 2)/(1 +α2)(which strictly beats even the un-loosened
λ= 1bound
√
(2 +πs)/(1−α 2)for everyd>0,s≥1, cutting theO(1)term from2/(1−α 2)to2
and shrinking the√scoefficient by(1−α 4)1/4 <1).
Proof.Setλ ∗:= (1−α 2)/(1 +α2)∈(0,1). By Cauchy–Schwarz with weight1 +λ ∗w2/s2 and the
exact Parseval identities Eq. (S115) of [1],

∑
w≥0
|cw|


2
≤

∑
w≥0
(
1 + λ∗w2
s2
)
|cw|2



∑
w≥0
1
1 +λ∗w2/s2

= 2
∑
w≥0
1
1 +λ∗w2/s2 .
Becauset↦→(1 +λ ∗t2/s2)−1 is strictly decreasing on[0,∞), the integral comparison gives
∑
w≥0
1
1 +λ∗w2/s2 ≤1 +
∫∞
0
dt
1 +λ∗t2/s2 = 1 + πs
2
√
λ∗ = 1 + πs
2
√
1 +α2
1−α 2 ,
yielding the first inequality in (11). For strict dominance over both the un-loosenedλ= 1bound√
(2 +πs)/(1−α 2)andD CB
d
√sat everyd>0ands≥1, observe that(1−α 2)(1 +α2) = 1−α 4 <
1 =⇒
√
(1 +α2)/(1−α 2)<(1−α 2)−1, while2<2/(1−α 2)≤2s/(1−α 2)(Lean 4 Theorem 13).
Substituting into Eq. (S120) of [1] proves (12).
5 Constructive Lean 4.35.0 Formalization and Zero-Float Audit
Our verification architecture separates machine-checked core algebra from analytic lifting transpar-
ently:
•Lean 4.35.0 Kernel (lean/LocalCertPhase.lean, 14 theorems, 0sorry, 0 warn-
ings [3]):Pure Lean 4 core with zeroClassical.choiceacross all 14 theorems (axioms strictly
⊆{propext,Quot.sound}). Theorems 1–9 prove the integer binomial theorem, consecutive-node
dual mass and total-variation identities for allr∈N, the odd binomial difference lower bound
(x+ 1)m ≥(x−1) m+ 2mxm−1, the implication(x+ 1)r+1 −(x−1) r+1 ≤2xr+1 =⇒x≥r+ 1,
the exact termwise tail-decay inequalityw(w−j)≤x(w−r−1)(w+ 1−j)for allw≥r+ 2, the
exact integer threshold jump atr= 9,d= 10(and post-jump checks throughr= 14), and the
unification of Proposition S33 forr= 0,1,2(note that Theorems 4–6 are formalized overNat, i.e.
integerx=d+1, while the general reald>0statements are proved analytically in Sections 2–3).
Theorems 10–12 prove the weighted binomial identity, exact second-regime evaluations, and the
7

--- Page 8 ---
Figure 3:Theorem C visual audit.(a) Normalized Blaschke dual constant( ∑ |cw|)/√sfor
d= 2,3, strictly dominating Cao & Bai’sD d for everys≥1. (b) Uniform>21.8%asymptotic
reduction across all integer local dimensionsd≥2(C14–C16).
crossover identity (10). Theorems 13–14 prove the Blaschke strict dominanceuv= 1−α4 <1
and the squared-ratio bound(Dopt
2 /DCB
2 )2 <61/100(certifying>21.89%reduction atd= 2).
Analytic Chebyshev-space uniqueness, the asymptotic expansion (5), the calculus monotonicity
ofg(m)−h(m)form≥10, and the Parseval integral comparison are proved in Sections 2–4.
•AST-Audited Zero-Float Verifier (src/local_cert_phase_verifier.py):Rejects all
float/complex literals,float(),complex(),eval(),exec(),from_float,from_decimal, float
libraries,/, and**. The 16 SHA-256 certificates compriseC01–C13, which replay full Lemma S30
exact rational Lagrange interpolation (including independent Lagrange replay of|Gconsec(r+ 2)|
on bifurcation certificates), dual moment equations, prefix feasibility|G(w)|≤1, and shifted-
polynomial nonnegativityQ(M+t),S(M+t)≥0(including rational boundary stress tests at
d= 263/125,403/125and ther= 9,d= 10jump certificateC07), together withC14–C16, which
verify exact rational Blaschke-dual bounds for Theorem C. The test suite (tests/test_local_c
ert_phase.py) passes 47/47 tests including 25 adversarial forgery attacks in<0.5s.
AI Assistance Disclosure.Mathematical exploration, Lean 4 proof engineering, zero-float ver-
ification software, and manuscript preparation were conducted by the author with assistance from
Google Antigravity; all theorems, proofs, formalizations, and numerical certificates were indepen-
dently machine-checked by Lean 4.35.0 and the zero-float verifier.
References
[1] Yimeng Cao and Ge Bai. Sharp transitions of copy complexity in local certification of typical
pure states.arXiv preprint arXiv:2611.34742v1, November 2026.
[2] Andrea Coladangelo, Jiahui Li, and Joseph Slote. Robust quantum state certification and un-
certainty principles for total influence.arXiv preprint arXiv:2607.27184, 2026.
[3] Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming lan-
guage. InAutomated Deduction – CADE 28, volume 12699 ofLNCS, pages 625–635. Springer,
2021.
[4] Hsin-Yuan Huang, John Preskill, and Mehdi Soleimanifar. Certifying almost all quantum states
with few single-qubit measurements.Nature Physics, 21:1834–1841, 2025.
8

--- Page 9 ---
[5] Oleg Szehr and Rachid Zarouf. Explicit counterexamples to Schäffer’s conjecture.Journal de
Mathématiques Pures et Appliquées, 146:1–30, 2021.
9
