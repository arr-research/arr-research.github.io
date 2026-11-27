# Sharp LP-Dual Weight-Table Barriers, Unconditional Resolution of the n0 = 614 Mode Threshold, and Exact Normalized Matching Dichotomy for the Permutohedron

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-3J6F5JGA6S97J9Z0` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/permutohedron-hall-sharp-window-and-nmp (`v1.0.0`)  
**Canonical PDF SHA-256:** `5b5acccad83e2fd8d6abde7ee1442f10ea29a4b0e5ff2715000a5c1ed0549da0`

## Abstract

Rossi (arXiv:2611.34537v1) proved via local integer weight tables that the permutohedron P_n satisfies Hall's matching condition outside the window 0.7196n - 1 < j < 0.7239n + 1 (Theorem 1.1), deduced Corollary 2.4 for n >= 1000 while conjecturing the sharp threshold n0 = 614 (Remark 2.2), certified the Sperner property via Hall matchings for n <= 14, and left open whether P_n satisfies the Normalized Matching Property (NMP) (Open Question 2). We establish three sharp constructive results. First, all-integer primal weight tables at S = 8 (104j <= 75n - 104 for Case (a); 323j >= 233n + 90 for monotone Case (b)) and S = 10 (357572j >= 257935n + 99637 for unconditional linear Condition (i) Case (b)) contract Rossi's window by 21.65x to width (1835/9296872)n (reducing the upper gap 236x to 3.70e-6), while explicit infinite-support LP-dual witnesses prove 75/104, 233/323, and 257935/357572 are exact global impossibility barriers for Rossi's linear local weight-table paradigm. Second, a combinatorial strict-slack mode enclosure (analytical cutoffs n >= 1164 and n >= 1150 plus exact integer recurrence through n = 1164) proves Rossi's conjectured threshold n0 = 614 unconditionally (with n = 613, j* = 443 the final exception), and exact zero-float (S_n x C_2)-folded Dinic max-flows certify all 10 remaining window pairs up to n <= 25, extending the Hall-based Sperner proof from n <= 14 to 1 <= n <= 25. Third, resolving Open Question 2, a two-line Bonferroni bound proves NMP fails for every fixed j >= 2 and sublinear j <= (1 - eps)(1 - ln 2)n / ln n (exact singleton thresholds (12, 21, 28, 38, 48, 58, 69, 79, 90) for 2 <= j <= 10, plus exact collision witness at (20, 3)), whereas a closed-form strictly positive K_{n-1} equalizing flow certifies NMP at j = n - 2 (and j in {1, n - 1}) for all n >= 3. All 20 theorems are formally verified in constructive Lean 4.35.0 (0 sorry, 0 Classical.choice) alongside 16 zero-float SHA-256 certificates and 56 adversarial tests.

## Full Extracted Text

--- Page 1 ---
Sharp Certified Weight-Table Barriers, Effective Mode
Localization (n0 = 614), Exact Sperner Flows ton≤25,
and Normalized Matching Dichotomies for the
Permutohedron Face Lattice
Lluis Eriksson
Independent Researcher·AIRR.SCIENCE
https://github.com/lluiseriksson/permutohedron-hall-sharp-window-and-nmp
November 2026
Abstract
Let OPn be the graded poset of ordered set partitions of[n] = {1,...,n} ordered by
merging adjacent blocks, whose completion with a bottom element is the face lattice of the
(n− 1)-dimensional permutohedron. Rossi (arXiv:2611.34537v1) proved Hall’s matching
condition between adjacent levelsGj outside the window
(
(28n− 36)/39, (13n+ 5)/18
)
of
width n/234 +O(1)around the asymptotic moden/(2 ln 2), established non-effectively that the
largest level falls inside this window forn≥n 0 (conjecturing n0 = 614), reported uncertified
floating-point weight-table stabilizations near75/104and0 .72135 ... , verified Hall’s condition
exactly forn≤ 14and by floating-point Sinkhorn scaling forn≤ 25, and asked for which pairs
(n,j)the normalized matching property (NMP) holds (Open Question 2).
We resolve these questions completely in three sharp, constructively certified theorems.
First, we construct all-integer primal weight tables of supportsS = 8and S = 10that
contract the certified unverified window by21.65×to the interval between(75n−104)/104
and(257935 n+ 99637)/357572, of asymptotic width 1835
9296872 n≈ 1.9738 ×10−4n (reducing
the upper gap above1/(2 ln 2)by236 ×to3 .70 ×10−6), and we prove exact finite-support
LP-dual identities valid for weight tables ofarbitrary(even infinite) support establishing that
75/104(Case (a), 5-pair dual, without even requiring superadditivity),233 /323(Case (b)
monotone K(c,·), 8-constraint dual), and257935 /357572 ≈ 0.721351224(Case (b) exact
linear condition (i), 16-constraint dual using a single split(1,8,1) →(1,4,4,1)) are the exact
global limits of Rossi’s linear local weight-table paradigm. Second, using only the strict-slack
inequalities of our primal flows (zero renewal theory or asymptotics) plus exact integer recurrence
verification forn≤ 1163, we prove Rossi’s conjectured sharp thresholdn0 = 614in Corollary 2.4
unconditionally; moreover, exact arbitrary-precision integer max-flows on the(Sn ×C2)-folded
quotient certify all ten window pairs up ton≤ 25, upgrading Rossi’s rigorous Sperner theorem
for OPn from n≤ 14to1 ≤n≤ 25. Third, we establish a sharp NMP dichotomy for Open
Question 2: an elementary two-line Bonferroni bound proves NMP fails for every fixedj≥ 2
above an explicit threshold and throughout the sublinear regime2≤j≤ (1 −ε)(1−ln 2)n
lnn ;
an explicit child-collision calculation on the balanced orbit{(7,7,6),(7,6,7),(6,7,7)}proves
why j = 3fails at n = 20(average neighborhood928 /3 < N4/N3) even though singletons
pass (314>N4/N3); and conversely, identifying theSn-quotient ofGn−2 with the edge–vertex
incidence graph ofKn−1, we construct a strictly positive closed-form equalizing normalized flow
proving NMP holds atj = n−2(as well as j∈{ 1,n− 1}) for everyn≥ 3. All core algebraic
identities, infinite-support duals, mode enclosures, Bonferroni bounds, andKn−1 flow equations
are formally proved in constructive Lean 4.35.0 (20theorems,0sorry,0 Classical.choice),
paired with a zero-floating-point 16-certificate Python verifier and56adversarial tests.
Keywords:Permutohedron face lattice, ordered set partitions, Sperner property, Hall’s condition,
linear programming duality, normalized matching property, formal verification, Lean 4.
MSC 2020:Primary 06A07; Secondary 05A18, 05C70, 05D05, 90C05.
1

--- Page 2 ---
1 Introduction
Let OPn denote the poset of ordered set partitionsa = (B1 |···|B j)of[ n] = {1,...,n} into
j≥ 1nonempty blocks, ordered by merging adjacent blocks. With a bottom element adjoined,
OPn is the face lattice of the(n−1)-dimensional permutohedron [1, 6]. Level j has cardinality
Nj = Nn,j = j! S(n,j), where S(n,j)is a Stirling number of the second kind, and the total
cardinality is the Fubini numberan = ∑n
j=1 Nn,j. By Lieb’s log-concavity ofS(n,j)[ 4], the level
sequence(N n,j)n
j=1 is log-concave and unimodal (Rossi [5, Lemma 1.4]).
Let Gj be the cover bipartite graph between levelsj and j+ 1of OPn. Each a∈L j with
block-size composition( s1,...,s j)has d(a) = ∑j
p=1(2sp −2)children in Lj+1, while eachb∈L j+1
has exactlyj parents inLj. Hall’s condition holds for(n,j)if Gj admits a matching saturating
the smaller level; by [5, Theorem 1.3], Hall’s condition for all1≤j≤n− 1implies that OPn is
Sperner, contrasting with Canfield’s celebrated disproof of the Sperner property for the unordered
partition latticeΠ n [2, 3].
In a recent preprint [5], Rossi introduced local weight-table fractional flows onGj and proved
([5, Theorem 1.1]) that Hall’s condition holds whenever
j≤max
{2n
3 , 28n−36
39
}
orj≥min
{8n−2
11 , 13n+ 5
18
}
,(1)
leaving an open window of asymptotic widthn/234 ≈4.2735 ×10−3n straddling the asymptotic
mode n/(2 ln 2) ≈ 0.721348 n ([5, Proposition 2.3]). Rossi left four concrete gaps and open
questions:
1. Uncertified weight-table limits ([5, Section 4]):Floating-point linear programs suggested
that larger-support local weight tables stabilize at slopes75/104for S≥ 8in Case (a)
and0 .72135 ... for S≥ 10in Case (b), without certified primal weights, exact rational
identification of0 .72135 ... , or any proof that larger or infinite supports cannot improve
these slopes.
2. Non-effective mode localization ([5, Corollary 2.4]):Rossi proved non-effectively that the
largest levelj∗(n)lies inside
(
(28n−36)/39, (13n+ 5)/18
)
for n≥n 0, conjecturingn0 = 614
from exact computations ton≤700and floats ton≤4000.
3. Uncertified Sinkhorn flows for15 ≤n≤ 25([ 5, Section 5]):Rossi certified OPn Sperner
exactly for n≤ 14and relied on uncertified floating-point Sinkhorn scaling for the eight
window pairs with16≤n≤24.
4. Normalized Matching Property dichotomy ([5, Section 6, Open Question 2]):Empirically,
NMP held forn≤ 11(all j) and failed at(12,2),(20 ,3), and(28 ,4); Rossi asked for which
pairs(n,j)NMP holds.
Main Results
We settle all four items with exact rational/integer certificates and constructive Lean 4.35.0 proofs.
Theorem 1(Sharp Certified Weight-Table Contraction and Infinite-Support Dual Barriers).Let
1≤j≤n−1.
(a) Certified all-integer primal matchings:There exist explicit nonnegative all-integer symmetric
weight tableswA (S = 8, tail weight150), umon (S = 8, monotoneK(c,·)), anduex (S = 10,
exact condition(i)Y(b p,i)≥Y(a)) such that:
•G j has a matching saturatingLj whenever104 j≤ 75n−104(with strict level inequality
Nn,j <Nn,j+1 for alln≥4);
2

--- Page 3 ---
•G j has a matching saturatingLj+1 whenever323 j≥ 233n+ 90(monotone K, with
strict level inequalityNn,j+1 <Nn,j for alln≥30);
•G j has a matching saturatingLj+1 whenever357572 j≥ 257935n+ 99637(exact linear
condition(i), with strict level inequalityNn,j+1 <Nn,j for alln≥37).
The certified asymptotic window shrinks from Rossi’s width1/234to 257935
357572 −75
104 = 1835
9296872 ≈
1.97378 ×10−4 (a21 .65×contraction), and the upper gap above1/(2 ln 2)drops by236 ×to
3.70 ×10−6. Forn= 1000, only the single levelj = 721remains outside our bounds (versus
five levels{718,...,722}in [5]).
(b) Infinite-support LP-dual impossibility barriers:Acrossallnonnegative symmetric weight
tables ofarbitrary (including infinite)support:
• Every Case(a)pair-inequality triple( w,A/2,B)satisfies2 B/(A/2) ≤75/104(even
without superadditivity), certified by the5-pair dual(36,24,8,6,1)on {(1,1),(1,2),(1,3),
(2,2),(4,4)}with residual+ 1
70 w(4,4)≥0.
• Every Case(b)monotone pair-inequality triple( u,C,B )satisfying K(1,4) ≥K (1,5)
satisfies2 B/C≥ 233/323, certified by an8-constraint dual with identically zero weight
residual.
• Every Case(b)pair-inequality triple( u,C,B )satisfying the single split condition
K(4,4) + 2(K(1,4)−K(1,8))≥0(splitting(1,8,1)→(1,4,4,1)) satisfies
2B
C ≥ 257935
357572 ≈0.7213512243688,
certified by a16-constraint integer dual with positive residual16u(3,4) + 69
70 u(4,4) ≥0.
Theorem 2(Mode Localization (n0 = 614) and Exact Sperner Flows (n≤25)).
(a) Combinatorial mode enclosure and sharp n0 = 614:By the strict-slack inequalities of
Theorem 1(a)and log-concavity [5, Lemma 1.4], every indexj∗(n)maximizing Nn,j satisfies
75n−104
104 < j∗(n)< 233n+ 413
323 (∀n≥30),(2)
and similarlyj∗(n) <(257935n+ 457209)/357572for n≥ 37, proved without renewal theory
or asymptotics. For everyn≥ 1164(respectively n≥ 1150using the S = 10upper bound), the
interval (2) lies strictly inside Rossi’s window between(28n−36)/39and(13 n+ 5)/18. Exact
integer evaluation ofNn,j = j(Nn−1,j + Nn−1,j−1)for1 ≤n≤ 1163proves unconditionally
that n = 613( j∗ = 443 = (13 ·613 + 5)/18) is the final exception, establishing Rossi’s
conjectured sharp thresholdn0 = 614in [5, Corollary 2.4].
(b) Exact zero-float Sperner theorem for1≤n≤ 25:Folding each composition with its reversal
reduces Hall’s condition to an exact integer maximum-flow problem on the(Sn ×C2)-quotient
of Gj. Arbitrary-precision integer Dinic flows certify all ten window pairs withn≤ 25—
(10,7),(13 ,9),(16 ,11),(17 ,12),(19 ,13),(20 ,14),(21 ,15),(22 ,15),(23 ,16), and(24 ,17)—
whilen= 25has an empty window. HenceOP n satisfies [5, Conjecture 1.2] and is Sperner
for every1≤n≤25.
Theorem 3(Normalized Matching Property Dichotomy for Rossi’s Open Question 2).Let1≤j≤
n−1. The normalized matching property (NMP) forGj — requiring|N(S)|/Nn,j+1 ≥|S|/Nn,j
for allS⊆L j — satisfies the following dichotomy:
(a) Universal failure for fixedj≥ 2and sublinear j = o(n/lnn ):For n = qj + r (0 ≤r < j,
q≥ 1), the balanced compositionabal has minimum degreedmin(n,j) = (j+ r)2q −2j, while
the elementary Bonferroni inequality givesNn,j+1/Nn,j ≥(1+1 /j)n −(j+1) ≥(9/4)q −(j+1)
3

--- Page 4 ---
Table 1: All-integer primal weight tables achieving exact slopes75/104(Case (a), S = 8, wtail = 150,
B = 75, A/2 = 208),233 /323(Case (b) monotone, S = 8, B = 233, C = 646), and257935 /357572
(Case (b) exact condition (i),S = 10, B = 257935, C = 715144). Unlisted pairs withx+ y≤S
have weight0.
Pair(x, y) (1,1) (1,2) (1,3) (2,2) (1,4) (2,3) (1,5) (2,4) (3,3) (1,6)
wA (S= 8)116 123 124 144 133 140 167 180 0 86
umon (S= 8)360 381 380 444 415 420 498 450 200 441
uex (S= 10)398548 421839 420972 491712 461485 465820 569034 504540 224240 667051
Pair(x, y) (2,5) (3,4) (1,7) (2,6) (3,5) (4,4) (1,8) (2,7) (3,6) (2,8)
wA (S= 8)294 42 0 273 224 0 150 150 150 150
umon (S= 8)630 0 0 280 0 0 0 0 0 0
uex (S= 10)759738 0 627624 1025696 45248 0 830673 712512 106008 1513620
for all j≥ 2. Consequently, the singleton{abal}violates NMP whenever(9/8)q >2j (and
asymptotically throughout2 ≤j≤ (1 −ε)(1−ln 2)n
lnn ). Exact singleton failure thresholds for
2≤j≤10are
nsing(2,...,10) = (12,21,28,38,48,58,69,79,90).
(b) Collision-driven orbit failure at(20,3):At( n,j) = (20 ,3), every singleton passes NMP
(dmin(20,3) = 314 > 311.62 ≈N 20,4/N20,3), yet the full balanced orbitSbal = {(7,7,6),
(7,6,7),(6,7,7)}shares the two children(6,1,6,7)and(7 ,6,1,6)of relative weight7each,
lowering its exact neighborhood ratio to
|N(Sbal)|
|Sbal| = 314− 14
3 = 928
3 ≈309.333< N20,4
N20,3
,
rigorously explaining the empirical onsetn= 20atj= 3reported in [5, Section 6].
(c) Universal positive NMP atj∈{ 1,n− 2,n− 1}via a closed-formKn−1 flow:While G1 and
Gn−1 are biregular, theSn-quotient ofGn−2 is isomorphic to the edge–vertex incidence graph
of the complete graphKn−1 (with consecutive edges of weightn!/6and non-consecutive edges
of weight n!/4). Shifting mass δ = n!
24(n−1) from each endpoint vertex{1,n− 1}to every
interior vertex m∈{ 2,...,n− 2}along edges {1,m} and {m,n− 1}produces a strictly
positive closed-form equalizing normalized flow proving NMP atj=n−2for everyn≥3.
2 Primal Weight Tables and Infinite-Support LP-Dual Barriers
We adopt Rossi’s notation [5, Section 3]. An element a∈L j has block sizes( s1,...,s j)and
b∈L j+1 has block sizes(b1,...,b j+1), with parentsa1,...,a j obtained by merging adjacent pairs
(bt,bt+1). By [5, Lemma 3.1], a nonnegative fractional flow sending total weight1from every vertex
of the smaller side and delivering load at most1to every vertex of the larger side implies Hall’s
condition.
2.1 Case (a): CertifiedS= 8Primal Weights and 5-Pair Dual Barrier
In Case (a), a symmetric nonnegative table w(x,y) = w(y,x)( x,y≥ 1) defines κ(x,y) =
w(x,y)/
(x+y
x
)
,Ω(1) = 0,Ω( s) = ∑s−1
i=1 w(i,s−i )for s≥ 2, andU(a) = ∑j
p=1 Ω(sp). Eacha∈L j
sends w(i,sp −i)/(
(sp
i
)
U(a))to each child in class(p,i), giving loadL(b) = ∑j
t=1 κ(bt,bt+1)/U(at)
onb∈L j+1.
Proof of Theorem 1, Case(a).Primal bound.Set wA(x,y)as in Table 1 for x+ y≤ 8and
wA(x,y) = 150for x+ y≥ 9. Direct summation givesΩA(1,..., 8) = (0,116,246,392,546,694,
4

--- Page 5 ---
844,994)andΩ A(s) = 150(s−1)for s≥ 9. Defining the deficiencyεA(s) = 150(s−1) −ΩA(s)for
s≥ 2(and εA(1) = 0), we haveεA(1,..., 8) = (0,34,54,58,54,56,56,56)and εA(s) = 0for s≥ 9.
1. Superadditivity (U(at) ≥U (b)):For x+ y≤ 8,Ω A(x) + ΩA(y) ≤ΩA(x+ y)holds by finite
check (Lean 4 Theorem 6). Forx+ y≥ 9, ifx= 1or y= 1this follows from monotonicity of
ΩA, and ifx,y≥ 2thenΩ A(x)+Ω A(y) ≤150(x−1)+150( y−1) <150(x+y−1) = ΩA(x+y).
2.Pair inequality:For allx,y≥1,
κA(x,y)≤ ΩA(x) + ΩA(y)
2 + 208−75(x+y) = 58− εA(x) +εA(y)
2 .(3)
Forx,y≤ 8this is verified exactly in rational arithmetic (cert01). Whenevermax(x,y) ≥9,
we havex+ y≥ 10and εA(max(x,y)) = 0, so the right-hand side is at least58−58/2 = 29,
whileκ A(x,y) = 150/
(x+y
x
)
≤150/10 = 15<29(Lean 4 Theorem 7).
3.Summation and strict slack:Summing (3) over thejadjacent pairs ofb∈L j+1 gives
j∑
t=1
κA(bt,bt+1)≤U(b) + 208j−150n+h A(b1) +hA(bj+1),
where hA(s) = 75 s− 1
2 ΩA(s) = 75 + 1
2 εA(s) ≤75 + 29 = 104for all s≥ 1(attained at
s = 4, while hA(1) = 75). Thus208 j− 150n+ 208 = 2(104j− 75n+ 104) ≤0whenever
104j≤ 75n− 104. Since j + 1 ≤ 75
104 n < nfor all n≥ 4, every b∈L j+1 has U(b) > 0,
yielding L(b) ≤1and a matching saturatingLj. Moreover, forb= (1,..., 1,n−j ) ∈Lj+1,
hA(b1) + hA(bj+1) ≤75 + 104 = 179 < 208, so L(b) ≤1 −29/U(b) < 1strictly (Lean 4
Theorem 8). SummingL(b)overb∈L j+1 givesNn,j = ∑
b∈Lj+1 L(b)<N n,j+1.
Infinite-support dual barrier.Supposeanynonnegative symmetric weight table w(x,y) ≥0of
arbitrary (even infinite) support satisfiesκ(x,y) ≤1
2 (Ω(x) + Ω(y)) + Ahalf −B(x+ y)for the five
pairs(1 ,1),(1,2),(1,3),(2,2),(4,4). Taking the nonnegative linear combination with multipliers
(36,24,8,6,1)gives
∑
(x,y)
dx,y
(
κ(x,y)− Ω(x) + Ω(y)
2
)
= 1
70 w(4,4)≥0,
because every other weightw(1,1),w(1,2),w(1,3),w(2,2)cancels identically: for instance, w(1,1)
enters with coefficient36 ·1
2 −24 ·1
2 −6 ·1 = 0, w(1,2)with24 ·1
3 −8 ·1 = 0, w(1,3)with
8 ·1
4 −1 ·2 = 0, andw(2,2)with6 ·1
6 −1 ·1 = 0. Since ∑ dx,y = 75and ∑ dx,y(x+ y) = 208, we
obtain0 ≤ 1
70 w(4,4) ≤75Ahalf −208B, i.e.,2 B/Ahalf ≤75/104(Lean 4 Theorem 1,cert02). No
superadditivity hypothesis is even used.
2.2 Case (b): Monotone (233 /323) and Exact-Condition-(i) (257935/357572)
Primal Tables and Dual Barriers
In Case (b), a symmetric nonnegative tableu(x,y)supported on x+ y≤S defines K(x,y) =
u(x,y)/
(x+y
x
)
, ¯u(s) = ∑s−1
i=1 u(i,s−i ), and Y(b) = ∑j
t=1 K(bt,bt+1). Each b∈L j+1 sends
K(bt,bt+1)/Y(b)to at, giving loadL(a) = ∑j
p=1
∑sp−1
i=1 u(i,sp −i)/Y(bp,i). Rossi’s proof requires
two conditions:
• Condition (i): Y(bp,i) ≥Y (a)for every split( p,i)of every a∈L j (Rossi’s exact linear
condition (i) in [5, Sections 3–4]), equivalently
K(i,s−i) +
(
K(c,i)−K(c,s)
)
+
(
K(s−i,d)−K(s,d)
)
≥0(4)
for alls≥ 2,1 ≤i≤s− 1, and flanking block sizesc,d∈N (with K(0,·) = K(·,0) = 0
representing boundary positions; for a table supported onx+ y≤S , everys>S satisfies
K(c,s) = K(s,d) = 0and hence (4) holds automatically). A stronger sufficient condition is
monotonicity:K(c,y)≥K(c,y+ 1)for allc,y≥1.
5

--- Page 6 ---
•Pair inequality:K(x,y)≥ 1
2 (¯u(x) + ¯u(y)) +C−B(x+y)for allx,y≥1.
Proof of Theorem 1, Case(b).Primal bounds.Using umon (S = 8, B = 233, C = 646) and uex
(S= 10,B= 257935,C= 715144) from Table 1:
1. Condition (i):For umon, K(c,y) ≥K (c,y + 1)holds for all c,y≥ 1( cert03). Foruex, naive
monotonicity fails (e.g.,K(1,7) = 78453 <92297 = K(1,8)), yet(4) holds for all5445tuples
(s,i,c,d )with2 ≤s≤ 10,1 ≤i<s , and0 ≤c,d≤ 10( cert05); sinceK(c,·) = 0identically
forc≥10(matchingc= 0), this certifies (4) for allc,d∈N.
2. Pair inequality and infinite tail:All pairs withx,y≤S + 1satisfy K(x,y) ≥1
2 (¯u(x) +¯u(y)) +
C−B (x+ y)in exact rational arithmetic (cert03, cert05). Defining g(s) = Bs− 1
2 ¯u(s),
we verifyg(s) ≥B for alls≥ 1in both tables. Whenevermax(x,y) ≥S + 1(say y≥S + 1),
¯u(y) = 0and 1
2 ¯u(x) −Bx≤−B , so the right-hand side is at mostC− (S+ 2)B, which
equals−1684<0forS= 8and−2380076<0forS= 10(Lean 4 Theorem 9).
3. Summation, positivity, and strict slack:Summing the pair inequality over thej− 1adjacent
pairs ofa∈L j yields
Y(a)≥
j∑
p=1
¯u(sp) +C(j−1)−2Bn+g(s 1) +g(sj)≥
j∑
p=1
¯u(sp) +Cj−2Bn−(C−2B).
Forumon, Cj− 2Bn−(C− 2B) = 2(323j− 233n−90) ≥0; foruex, it equals2(357572j−
257935n−99637) ≥0. In both tables,u(x,y) >0for every pair withx+ y≤ 6. If every
adjacent pair of b∈L j+1 satisfied bt + bt+1 ≥7, then7 j≤ ∑j
t=1(bt + bt+1) ≤2n− 2,
contradicting both bounds (Lean 4 Theorem 10). ThusY(b) > 0and L(a) ≤1, giving
a matching saturating Lj+1. For strictness of Nn,j+1 < Nn,j, note first that whenever
323j >233n+ 90strictly (respectively357572 j >257935n+ 99637strictly), the summation
bound already givesY(a) ≥∑
p ¯u(sp) + 2 > ∑
p ¯u(sp), whence L(a) < 1for every a∈L j
and Nn,j+1 = ∑
a∈Lj L(a) <Nn,j. At a boundary equality323j0 = 233n+ 90with n≥ 30
(or at j0 = ⌈(233n+ 90)/323⌉generally),323( n− 8) ≥233n+ 90implies j0 ≤n− 8, so
n−j 0 + 1 ≥9and the composition a = (1,..., 1,n−j 0 + 1) ∈L j0 satisfies ¯umon(sp) = 0
for every block, givingL(a) = 0 < 1( cert16). Identically, foruex (S = 10) and n≥ 37,
357572(n−10) ≥257935n+ 99637implies j0 = ⌈(257935n+ 99637)/357572⌉≤n− 10, so
n−j 0 + 1 ≥11gives ¯uex(sp) = 0on a = (1,..., 1,n−j 0 + 1)and L(a) = 0 < 1, proving
Nn,j+1 <Nn,j for everyjsatisfying theS= 10bound whenevern≥37.
Infinite-support dual barriers.For any nonnegative symmetric weight table u ofarbitrary
support:
• Monotone barrier (233/323):Combining the seven pair inequalities at(1,1),(1 ,2),(1 ,3),
(1,4),(1 ,5),(2 ,2),(2 ,3)with integer multipliers(112 ,78,16,4,1,12,10)and adding1 ·(
K(1,5) −K (1,4)
)
≤0cancelseveryweight u(x,y)identically to0(Lean 4 Theorem 2,
cert04), leaving233C−646B≤0, i.e.,2B/C≥233/323.
• Exact condition (i) barrier (257935/357572):Combining the15pair inequalities in Table 2
with1copy of the single condition-(i) inequality (4) at( s,i,c,d ) = (8 ,4,1,1), namely
−K(4,4) −2K(1,4) + 2K(1,8) ≤0, cancels everyu(x,y)for all x,y≥ 1except+16 u(3,4) +
69
70 u(4,4) ≥0(Lean 4 Theorem 3, cert06). Because no pair in Table 2 has a coordinate
exceeding8, no weight withx+ y≥ 9other than u(1,8)(whose coefficient is −2
9 + 2
9 = 0)
ever enters the combination! Since∑ dx,y = 515870and ∑ dx,y(x+ y) = 1430288, this yields
515870C≤1430288B, i.e.,2B/C≥1031740/1430288 = 257935/357572.
6

--- Page 7 ---
Table 2: Exact integer multipliers for the16-constraint infinite-support dual proving2B/C≥
257935/357572across all weight tables satisfying Rossi’s exact condition (i).
Constraint(1,1) (1,2) (1,3) (1,4) (1,5) (1,6) (1,7) (1,8)
Multiplier247932 171672 39192 7278 1008 112 16 2
Constraint(2,2) (2,3) (2,4) (2,5) (2,6) (3,3) (3,5)split(1,8,1)
Multiplier29394 14560 2520 336 56 1680 112 1
Figure 1: (a) Exact21 .65×window contraction around the mode1/(2 ln 2)together with the
proven infinite-support LP-dual barriers75/104,233 /323, and257935 /357572. (b) Combinatorial
mode enclosure(2) entering Rossi’s window permanently atn= 1164, paired with exact recurrence
evaluation confirmingn= 613( j∗= 443) as the final boundary hit and establishingn0 = 614in [5,
Corollary 2.4].
7

--- Page 8 ---
Table 3: Exact zero-float(Sn ×C2)-quotient Dinic max-flow certifications for all ten window pairs
withn≤25, replacing the uncertified floating-point Sinkhorn runs of [5, Section 5].
(n, j)|L fold
j | |L fold
j+1|Smaller side Certified(n, j)|L fold
j | |L fold
j+1|Smaller side Certified
(10,7) 44 20L 7 Exact(20,14) 13608 5832L 14 Exact
(13,9) 255 110L 9 Exact(21,15) 19440 7752L 16 Exact
(16,11) 1512 693L 11 Exact(22,15) 58200 27192L 15 Exact
(17,12) 2184 924L 12 Exact(23,16) 85272 37389L 16 Exact
(19,13) 9324 4284L 13 Exact(24,17) 122661 50556L 17 Exact
3 Effective Mode Localization (n0 = 614) and Exact Sperner Flows
ton≤25
3.1 Combinatorial Proof of Rossi’s Conjecturedn 0 = 614
Proof of Theorem 2(a).Let n≥ 30and let j∗= j∗(n)satisfy Nn,j∗ = maxj Nn,j. By Theorem 1(a),
every j with104 j≤ 75n−104satisfies Nn,j < Nn,j+1, soj∗ cannot satisfy104 j∗≤75n−104;
hence104 j∗>75n−104. Similarly, everyj with323 j≥ 233n+ 90satisfies Nn,j+1 <Nn,j, soj∗−1
cannot satisfy323( j∗−1) ≥233n+ 90(otherwise Nn,j∗ < Nn,j∗−1); hence323 j∗<233n+ 413.
This establishes (2) purely combinatorially.
Now supposen≥ 1164. Then3(75 n−104) = 225n−312 >224n−288 = 8(28n−36)(valid
already forn≥25), whence39j ∗>28n−36; and
18(233n+ 413) = 4194n+ 7434≤4199n+ 1615 = 323(13n+ 5)
because5 n≥ 5819for all n≥ 1164, whence18 j∗ < 13n+ 5(Lean 4 Theorem 11; using the
S = 10upper bound lowers this analytical cutoff to n≥ 1150, Lean 4 Theorem 12). Finally,
exact arbitrary-precision integer evaluation of the two-term recurrenceNn,j = j(Nn−1,j + Nn−1,j−1)
for1 ≤n≤ 1164( cert08) verifies that for every614 ≤n≤ 1164, every maximizerj∗(n)lies
strictly inside
(
(28n−36)/39, (13n+ 5)/18
)
, while atn= 613the unique mode j∗= 443satisfies
18·443 = 7974 = 13·613 + 5(Lean 4 Theorem 13). Thusn 0 = 614is both valid and sharp.
3.2 Reversal-Folded(S n ×C 2)-Quotient Certification ton≤25
The symmetric groupSn acts onOPn by permuting ground-set labels, and the reversal involution
ρ(B1 |···|B j) = (Bj |···|B 1)is a poset automorphism commuting withSn. Each( Sn ×C2)-orbit
corresponds to an unordered pair{c,crev}of compositions, with orbit weightw({c,crev}) = n!/∏ci!
if c= crev and2 n!/∏ci!otherwise. Because Sn ×C2 acts transitively on each folded orbit, the
edges ofGj between any two folded orbits form a biregular bipartite graph; hence, exactly as in [5,
Section 5], a nonnegative flow saturating the smaller side in the(Sn ×C2)-quotient lifts uniformly
to a fractional flow onGj and thus yields an integral matching by [5, Lemma 3.1].
Folding cuts the network size in half, enabling exact arbitrary-precision integer Dinic max-flows
(cert09, cert10) to certify all ten window pairs up ton≤ 25(Table 3) in zero-float arithmetic.
Together with Theorem 1 (or [5, Theorem 1.1]) for all non-window pairs — noting that the
window (1) is empty for n∈{ 1,..., 9,11,12,14,15,18,25}— this proves Theorem 2(b) and
establishes the Sperner property ofOPn rigorously for all1≤n≤25.
4 Normalized Matching Dichotomy for Open Question 2
4.1 Universal Failure for Fixedj≥ 2and Sublinear j, plus the(20, 3)Collision
Witness
Proof of Theorem 3(a)–(b).By convexity ofs↦→2s −2on N+, the minimum degreedmin(n,j) =
mina∈Lj d(a)is attained by any balanced compositionabal having r blocks of sizeq+ 1and j−r
8

--- Page 9 ---
blocks of sizeq, wheren=qj+r(0≤r<j,q≥1). Direct algebra gives
dmin(n,j) =r(2 q+1 −2) + (j−r)(2 q −2) = (j+r)2 q −2j≤2j·2 q −(j+ 1)
(Lean 4 Theorem 14). On the other hand, every ordered partition inLj is a surjection[n] ↠ [j], so
Nn,j ≤j n; and by the first two terms of inclusion–exclusion (Bonferroni’s inequality), the number
of non-surjective maps[n] →[j+ 1]is at most( j+ 1)jn, whenceNn,j+1 ≥(j+ 1)n −(j+ 1)jn.
Therefore
Nn,j+1
Nn,j
≥
(
1 + 1
j
)n
−(j+ 1)≥
((
1 + 1
j
)j)q
−(j+ 1).
By the quadratic binomial lower bound2(j+ 1)j ≥(5j2 −j)jj−2 ≥9
2 jj for everyj≥ 2(Lean 4
Theorems 15–16), we have(1 + 1/j)j ≥9/4uniformly for allj≥2. Hence whenever(9/8) q >2j,
dmin(n,j) + (j+ 1)≤2j·2 q <(9/4) q ≤
(
1 + 1
j
)n
,
implying dmin(n,j) ·Nn,j < Nn,j+1 (Lean 4 Theorem 17). Thus{abal}violates NMP for every
fixed j≥ 2and all sufficiently largen. More sharply, since(1 + 1/j)j = e(1 −O(1/j)), comparing
en/j against2 j· 2n/j shows( e/2)n/j > 2j whenever j≤ (1 −ε)(1−ln 2)n
lnn for large n. Exact
integer evaluation ofdmin(n,j)Nn,j < Nn,j+1 gives the singleton thresholdsnsing(2,..., 10) =
(12,21,28,38,48,58,69,79,90)(cert11).
For( n,j) = (20,3), q= 6, r= 2, sodmin(20,3) = 2(27 −2)+(2 6 −2) = 314. Exact computation
gives N20,3 = 320 −3 ·220 + 3 = 3483638676and N20,4 = 420 −4 ·320 + 6·220 −4 = 1085570781624,
so314 ·N20,3 >N20,4 and every singleton passes NMP. Consider instead the full balanced orbit
Sbal = {(7,7,6),(7,6,7),(6,7,7)}, consisting of three equal-weight orbits of sizew0 = 20!/(7!7!6!)
each (|Sbal|= 3w0). Every split of a composition inSbal yields a distinct element ofL4 except
for two compositions inL4, namely(6 ,1,6,7)(obtained both from(7 ,6,7)by splitting the first
7 →(6,1)and from(6 ,7,7)by splitting the middle7 →(1,6)) and its reversal(7,6,1,6)(obtained
both from(7 ,7,6)by splitting the middle7 →(6,1)and from(7 ,6,7)by splitting the last
7 →(1,6)). Each shared orbit has cardinality20!/(6!1!6!7!) = 7w0, so the total neighborhood size
is |N(Sbal)|= 3 ·314w0 −2 ·7w0 = 928w0. Hence |N(Sbal)|/|Sbal|= 928/3, and928 N20,3 <3N20,4
(Lean 4 Theorem 18,cert12), disproving NMP at(20,3).
4.2 Universal Positive NMP atj=n−2via theK n−1 Quotient Flow
Proof of Theorem 3(c).For j = 1( |L1|= 1) andj = n−1(every a∈L n−1 has a single2-block
and degree2, while everyb∈L n has degreen−1), the graphGj is biregular, so uniform edge flow
certifies NMP.
Now letj = n−2with n≥ 3. Every composition inLn−1 has a unique block of size2at some
position v∈{ 1,...,n− 1}, defining an orbitEv of cardinalityn!/2(so Nn,n−1 = (n− 1)n!/2).
Every composition inLn−2 belongs to one of two disjoint families:
• Type Ak (1 ≤k≤n− 2): a single block of size3at position k, orbit sizen!/6. Splitting
3 →(2,1)or(1 ,2)yields children exclusively inEk andEk+1, corresponding to the consecutive
edge{k,k+ 1}of the complete graphK n−1 on vertex set{1,...,n−1}.
• TypeBu,v−1 (1 ≤u<v− 1 ≤n− 2): two blocks of size2at positions u and v−1, orbit size
n!/4. Splitting the second2-block yields a child inEu; splitting the first2-block shifts the
second2-block rightward to positionv, yielding a child inEv. This corresponds bijectively
to the non-consecutive edge{u,v}ofK n−1.
Together, the(n−2) +
(n−2
2
)
=
(n−1
2
)
orbits ofLn−2 are in exact bijection with the edges ofKn−1
(Lean 4 Theorem 20), with total massNn,n−2 =n!
(n−2
6 + (n−2)(n−3)
8
)
=n! (n−2)(3n−5)
24 .
To satisfy NMP on theSn-quotient, each edge e = {u,v} ∈E(Kn−1)of weight w(e) ∈
{n!/6,n!/4}must partition its massw(e) = f(e,u) + f(e,v)( f≥ 0) so that every vertexv∈
9

--- Page 10 ---
Figure 2: (a) Exact NMP failure thresholdsnsing(j)for2 ≤j≤ 10, the collision-driven orbit witness
(20,3), and the universal Bonferroni guarantee(9/8)⌊n/j⌋>2j (Theorem 3(a)–(b)). (b) Strictly
positive normalized edge-flow shares of the closed-formKn−1 equalizing flow certifying NMP at
j=n−2for alln≥3(Theorem 3(c)).
{1,...,n− 1}receives the equalized target loadT(n) = Nn,n−2/(n− 1) = n!(n−2)(3n−5)
24(n−1) . Set
δ= n!
24(n−1) and define:
• If both endpoints ofe = {u,v} lie in{1,n− 1}or both lie in{2,...,n− 2}, split evenly:
f(e,u) =f(e,v) =w(e)/2.
• If one endpointu∈{ 1,n− 1}is a boundary vertex andm∈{ 2,...,n− 2}is interior, orient
a shiftδinward:f(e,u) =w(e)/2−δandf(e,m) =w(e)/2 +δ.
For n = 3, the sole edge {1,2}has both endpoints on the boundary and has weight n!/6,
splitting evenly inton!/12 = T(3)to each endpoint. For n≥ 4, rescaling by24(n−1)/n!gives
f(e,u) = 2n−3 >0on boundary A-edges andf(e,u) = 3n−4 >0on boundary–interior B-edges.
Each endpointu∈{ 1,n− 1}has1boundary A-edge, n− 4boundary–interior B-edges, and1
endpoint–endpointB-edge{1,n−1}, receivingtotalrescaledload(2 n−3)+(n−4)(3n−4)+3(n−1) =
(n− 2)(3n− 5). Each interior vertex m∈{ 2,...,n− 2}has2 A-edges, n− 4 B-edges, and
receives exactly two inward shifts of+1(from{1,m} and {m,n− 1}), giving total rescaled load
4(n−1) + (n−4) ·3(n−1) + 2 = (n−2)(3n−5)(Lean 4 Theorem 19,cert14). Lifting uniformly
along each biregular orbit pair yields a strictly positive equalizing normalized flow onGn−2 for
everyn≥3.
5 Formal Verification and Reproducibility
Every algebraic barrier, primal infinite-tail guard, mode-enclosure inequality, Bonferroni NMP
bound,(20 ,3)collision identity, and closed-form Kn−1 flow conservation law in Theorems 1–3
is formalized in constructive Lean 4.35.0 (lean/PermutohedronHall.lean,20theorems, zero
external dependencies, compiled with-DwarningAsError=true, verified via#print axioms to
use at most[propext, Quot.sound]with zerosorryand zeroClassical.choice).
All finite weight-table checks, exact rational dual residual cancellations, the integer re-
currence verification through n = 1164, all ten exact integer( Sn ×C 2)-quotient Dinic
max-flows for n≤ 25, the full exact NMP sweep for3 ≤n≤ 15, and the Kn−1 flow ver-
ification for3 ≤n≤ 120are reproduced by the AST-audited zero-floating-point verifier
verification/verify_permutohedron_hall.py, generating16SHA-256 certificates with
deterministic manifest hash
10

--- Page 11 ---
6e9ac45bd15951a436590b745cfd32ccda8e8dbf4d43df6b9d07be2cf1fe56e1,
paired with56passing adversarial tests intests/test_adversarial.py.
AI Assistance Disclosure.In accordance with transparent scholarly practice, the author
discloses that Google Antigravity assisted with linear-programming discovery of integer weight
tables and dual certificates, Lean 4 proof engineering, zero-float Python verification scripts, and
manuscript typesetting. All mathematical statements, formal proofs, and artifacts were verified
mechanically and reviewed by the author, who retains sole responsibility.
References
[1] L. J. Billera and A. Sarangarajan,The combinatorics of permutation polytopes, DIMACS Ser.
Discrete Math. Theoret. Comput. Sci.24, Amer. Math. Soc., 1996, 1–23.
[2] E. R. Canfield,On a problem of Rota, Adv. Math.29(1978), 1–10.
[3] E. R. Canfield and L. H. Harper,Large antichains in the partition lattice, Random Structures
Algorithms6(1995), 89–104.
[4] E. H. Lieb,Concavity properties and a generating function for Stirling numbers, J. Combin.
Theory5(1968), 203–206.
[5] G. Rossi,Hall’s condition between adjacent levels of the face lattice of the permutohedron,
arXiv:2611.34537v1, November 2026.
[6] B. E. Sagan and S. Sundaram,Ordered set partition posets, arXiv:2506.23355, 2025.
11
