# Universal Average-Mixing Barriers, Conference-Graph Extremality, and Exact Diophantine Uniformization for Continuous-Time Quantum Walks on Strongly Regular Graphs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0W80EN2QVQ8HDSED` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/ctqw-average-mixing-barriers-srg-conference-extremality (`v1.0.0`)  
**Canonical PDF SHA-256:** `67f65e8b64f9d7d5a1f8dc970a4e47592d53c41b5b3dd2ea1a73bcf564bf01bb`

## Abstract

We establish three exact structural theorems governing the Cesaro average mixing matrix and generalized uniform average mixing (UAM) of continuous-time quantum walks U(t) = exp(-itA) on primitive strongly regular graphs SRG(n, k, lambda, mu). First, we prove that the Cesaro average mixing matrix M_hat = sum_theta E_theta^{o 2} is strictly rational for every SRG (even for irrational conference spectra) and satisfies the unconditional return-probability barrier M_hat_{uu} = (1 + m_r^2 + m_s^2)/n^2 >= (n^2 - 2n + 3)/(2n^2) > 1/n for all n >= 4, attaining equality if and only if G is a conference graph (n = 4t + 1, k = 2t, lambda = t - 1, mu = t). Furthermore, the off-diagonal mixing imbalance satisfies the closed-form identity M_hat_adj - M_hat_nonadj = 2(n - 2k + lambda - mu)/(n Delta), which negates identically under graph complementation and vanishes if and only if the Seidel eigenvalue theta_0 = n - 1 - 2k equals the exact midpoint (theta_r + theta_s)/2. Second, solving the non-conference off-diagonal Cesaro uniformity Diophantine system (n - 1) Delta = n((2k - n + 1)^2 + (n - 1)), we discover an infinite polynomial parameter family n(t) = (t + 1)(4t + 1)^2, k(t) = t(2t + 1)(4t + 3), mu(t) = 2t(t + 1)(2t + 1), r = t, s = -(2t + 1)^2, m_s = t(4t + 3) whose Cesaro mixing matrix has constant off-diagonal probability; both Krein inequalities hold unconditionally for all t >= 1, while the absolute bound fails uniquely at t = 1 (50 > 35) and holds strictly for every t >= 2 (realized at t = 2 by the ternary Golay dual coset graph SRG(243, 110, 37, 60)). Exhaustive zero-float search up to n <= 1200 certifies that only t = 2 (n = 243) and t = 3 (n = 676) (and complements) survive Krein and absolute-bound filtering. Third, formulating generalized UAM over arbitrary observation-time distributions via exact rational affine moment lines c_1(c_3), c_2(c_3) in [-1, 1]^3, we prove unconditionally that every member t >= 1 of our off-diagonal Cesaro-uniform family obeys max c_1(c_3) = -(16t^3 + 8t^2 + t - 1)/2 <= -12 < -1 and hence admits NO UAM under any time law (separating off-diagonal Cesaro uniformity from UAM), alongside empty-polytope UAM obstructions on Schlafli and Higman-Sims, exact 16x16 Hadamard involution instantaneous uniform mixing at t = pi/4 on Clebsch, L_2(4), and Shrikhande, and a 16-graph zero-float mixing atlas. A two-layer verification artifact accompanies the paper: 20 constructive, axiom-free Lean 4.36.0 theorems formalizing the barrier, complement, t-family, Krein, absolute-bound, and moment-line kernel, paired with 16 zero-float Python certificates and 56 adversarial tests.

## Full Extracted Text

--- Page 1 ---
Universal Average-Mixing Barriers,
Conference-Graph Extremality,
and Exact Diophantine Uniformization for
Continuous-Time
Quantum Walks on Strongly Regular Graphs
Lluis Eriksson∗
November 27, 2026
Abstract
We establish three exact structural theorems governing the Cesàro average mixing
matrix and generalized uniform average mixing (UAM) of continuous-time quantum walks
U(t) = e−itA on primitive strongly regular graphsSRG(n,k,λ,µ ). First, we prove that the
Cesàro average mixing matrixˆM := limT→∞ 1
T
∫T
0 |U(t)|◦2 dt= ∑
θE◦2
θ is strictly rational
for every SRG (including irrational conference spectra) and obeys the unconditional return-
probability barrier ˆMuu = (1 + m2
r + m2
s)/n2 ≥(n2 −2n+ 3)/(2n2) >1/n for all primitive
SRGs (n≥ 5, and algebraically for alln≥ 4), attaining equality if and only ifGis a conference
graph (n= 4t+ 1, k= 2t, λ= t−1, µ= t). Moreover, the off-diagonal mixing imbalance
satisfies the closed-form lawˆMadj−ˆMnonadj = 2(n−2k+λ−µ)/(n∆), which negates identically
under graph complementation and vanishes if and only if the Seidel eigenvalueθ0 = n−1−2k
equals the exact midpoint( θr + θs)/2. Second, solving the non-conference off-diagonal
Cesàro uniformity Diophantine system(n−1)∆ = n
(
(2k−n + 1)2 + (n−1)
)
, we introduce
an infinite polynomial parameter familyn(t) = ( t+ 1)(4t+ 1)2, k(t) = t(2t+ 1)(4t+ 3),
µ(t) = 2t(t+ 1)(2t+ 1), r = t, s = −(2t+ 1)2, ms = t(4t+ 3)whose Cesàro matrix has
constant off-diagonal probability; both Krein inequalities hold unconditionally for allt≥ 1,
whereas the absolute bound fails uniquely att= 1(50 >35) and holds strictly for everyt≥ 2
(realized att= 2by the ternary Golay dual coset graphSRG(243,110,37,60)). Exhaustive
zero-float search up ton≤ 1200certifies that only t= 2( n= 243) andt= 3( n= 676) (and
complements) survive Krein and absolute-bound filtering. Third, formulating generalized
UAM over arbitrary observation-time laws via exact affine moment linesc1(c3),c2(c3)in
[−1,1]3, we prove unconditionally that every membert≥ 1of our off-diagonal Cesàro-
uniform family obeys maxc3∈[−1,1] c1(c3) = −(16t3 + 8t2 + t− 1)/2 ≤ −12 <− 1and
therefore admitsnoUAM under any time law—sharply separating off-diagonal Cesàro
uniformity from UAM—complemented by empty-polytope UAM no-go proofs for Schläfli and
Higman–Sims, exact16 ×16Hadamard-involution instantaneous uniform mixing att= π/4
on Clebsch, L2(4), and Shrikhande, and a16-graph zero-float mixing atlas. A two-layer
verification artifact accompanies the paper: Layer 1 formalizes the barrier, complement,
t-family, absolute-bound, Diophantine, and moment-line kernel in20constructive Lean 4.36.0
theorems (0 sorry,0 Classical.choice, no custom axioms beyond standard constructive
propext/Quot.sound); Layer 2 verifies all16atlas graphs, the exhaustiven≤ 1200scan, and
explicit16 ×16Hadamard involutions in16zero-float Python certificates and56adversarial
tests.
∗Independent Researcher. Code, Lean 4.36.0 proofs, and zero-float certificates archived athttps://github.com
/lluiseriksson/ctqw-average-mixing-barriers-srg-conference-extremality (v1.0.0, MIT / CC-BY-4.0,
AIRR-FOUNDER-1.0). Manuscript and verification artifacts prepared with Google Antigravity assistance.
1
AIRR:ARR-2026-0W80EN2QVQ8HDSED v1  [Mathematics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
1 Introduction
The continuous-time quantum walk (CTQW) on a simple graphG = (V,E)with adjacency
matrix A evolves unitarily asU(t) = e−itA, with time-t transition probability matrixM(t) :=
|U(t)|◦2 = U(t) ◦U(t) [5, 6, 7]. Because unitary dynamics is quasi-periodic rather than ergodic,
mixing is studied both through the long-timeCesàro average mixing matrix
ˆM:= lim
T→∞
1
T
∫T
0
M(t)dt=
∑
θ∈spec(A)
E◦2
θ (1)
(where A = ∑
θθEθ is the spectral decomposition) and throughgeneralized uniform average
mixing(UAM), which asks whether there exists a probability distributionν on observation times
T≥ 0such that ET∼ν[M(T)] = 1
nJn, or at a single deterministic timet∗(instantaneous uniform
mixing, IUM) [8, 3, 4, 9].
Primitive strongly regular graphsSRG(n,k,λ,µ )provide the canonical testing ground because
their adjacency algebra is the3-dimensional Bose–Mesner algebraspan{I,A, ¯A}with exactly
three distinct eigenvaluesk>r>s and multiplicities1,mr,ms (mr + ms = n−1) [2]. Building
on Godsil’s spectral framework [7] and Kang’s recent moment-line analysis [9], we prove three
exact, zero-float algebraic theorems:
1. Universal Cesàro Return Barrier, Conference Extremality, and Complement
Sign-Flip (Theorem 1).Every primitive SRG (n≥5) has strictly rationalˆMobeying
ˆMuu = (1 + m2
r + m2
s)/n2 ≥(n2 −2n+ 3)/(2n2) >1/n, with equality iffG is a conference
graph, while the off-diagonal imbalance obeysˆMadj −ˆMnonadj = 2(n−2k+ λ−µ )/(n∆),
flipping sign underG↦→Gand vanishing iff the Seidel eigenvalueθ0 bisectsθ r andθ s.
2. Infinite Non-Conference Off-Diagonal Cesàro-Uniform Family andn≤ 1200
Classification (Theorem 2).Solving the exact Diophantine condition for non-conference
off-diagonal uniformity uncovers an infinite polynomial parameter familyn(t) = (t+ 1)(4t+
1)2 passing both Krein inequalities for allt≥ 1and passing the absolute bound ifft≥ 2
(realized att= 2by the ternary Golay dual coset graphSRG(243,110,37,60)[ 1]), and
exhaustive zero-float search up ton≤1200rules out every non-family parameter set.
3. Moment-Line Polytope Dichotomy, Universalt-Family UAM No-Go, and16-
Vertex IUM (Theorem 3).Expressing generalized UAM via affine cosine moment
lines c1(c3),c2(c3)in[ −1,1]3 proves thateverymember t≥ 1of our off-diagonal Cesàro-
uniform family—including the ternary Golay graph—has empty polytope intersection
(maxc1(c3) = −(16t3 + 8t2 + t− 1)/2 ≤−12 <−1), proving that off-diagonal Cesàro
uniformitydoesnotimplyUAM.Wecontrastthisagainstexact16 ×16Hadamard-involution
IUM att= π/4on Clebsch,L2(4), and Shrikhande, empty-polytope obstructions on Schläfli
and Higman–Sims, and a16-graph exact mixing atlas.
2 Universal Cesàro Return Barrier and Off-Diagonal Imbalance
For a primitiveSRG(n,k,λ,µ ), the non-trivial eigenvaluesr>s are the roots ofx2 −(λ−µ )x−
(k−µ ) = 0with discriminant∆ := ( λ−µ )2 + 4(k−µ ) = ( r−s )2 > 0, r+ s = λ−µ , and
rs=µ−k. The spectral idempotentsE k = 1
nJn,E r, andEs lie in the Bose–Mesner algebra:
Er = 1
r−s
(
A−sI− k−s
n J
)
, E s = 1
r−s
(
rI−A+ k−r
n J
)
.(2)
Theorem 1(Universal Cesàro Return Barrier, Conference Extremality, and Off-Diagonal Law).
Let G be any primitiveSRG(n,k,λ,µ )( n≥ 5) with discriminant∆and multiplicities1 ,mr,ms.
2

--- Page 3 ---
(a) Strict rationality and universal return barrier:The Cesàro average mixing matrixˆM =
E◦2
k + E◦2
r + E◦2
s has strictly rational entries inspanQ{I,A, ¯A}(even whenr,s /∈Q), with
constant diagonal entry
ˆMuu = 1 +m2
r +m2
s
n2 = n2 −2n+ 3 + (mr −ms)2
2n2 ≥ n2 −2n+ 3
2n2 > 1
n.(3)
Equality ˆMuu = ( n2 −2n+ 3)/(2n2)holds if and only if mr = ms = ( n− 1)/2, i.e.,
if and only ifG is a conference graph (n = 4 t+ 1, k = 2 t, λ = t− 1, µ = t, where
ˆMadj = ˆMnonadj = (n+ 3)/(2n2)).
(b) Exact off-diagonal imbalance and complement sign-flip:LetˆMadj and ˆMnonadj denote the
entries of ˆMon adjacent and distinct non-adjacent vertex pairs, respectively. Then
ˆMadj −ˆMnonadj = 2(n−2k+λ−µ)
n∆ .(4)
Under graph complementationG↦→G, ˆMuu(G) = ˆMuu(G)and ˆMadj(G) −ˆMnonadj(G) =
−
(ˆMadj(G)−ˆMnonadj(G)
)
. Moreover, ˆMadj = ˆMnonadj holds if and only ifn−2k+λ−µ = 0,
equivalently iff the Seidel matrixS = J−I− 2A has its regular eigenvalueθ0 = n−1 −2k
equal to the exact midpoint1
2 (θr + θs)of its non-trivial eigenvalues θr = −1 −2r and
θs =−1−2s.
Proof. Proof of(a).Since Gis walk-regular, every diagonal entry ofEθ equals tr(Eθ)/n= mθ/n,
giving ˆMuu = (1 +m2
r +m2
s)/n2. Becausemr +ms =n−1, the algebraic identity
2(1 +m2
r +m2
s) = 2 + (mr +ms)2 + (mr −ms)2 =n2 −2n+ 3 + (mr −ms)2 (5)
yields (3) immediately, with equality iffmr = ms = (n− 1)/2(the defining condition of a
conference SRG [2]). Since( n2 −2n+3) −2n= (n−1)(n−3) >0for all n≥ 4, ˆMuu >1/nholds
unconditionally. To see strict rationality for irrational conference graphs (r,s = (−1 ±√n)/2),
note thatEr and Es are Galois conjugates overQ(√n), soE◦2
r + E◦2
s is fixed byGal(Q(√n)/Q)
and hence strictly rational; explicitly,(Er)uv = ±1
2√n−1
2n for u̸= v, giving(Er)2
uv+(Es)2
uv = n+1
2n2
and ˆMadj = ˆMnonadj = 1
n2 + n+1
2n2 = n+3
2n2 .
Proof of(b).From (2), the adjacent and non-adjacent entries ofEr andE s are
ar = 1−(k−s)/n
r−s , na r = −(k−s)/n
r−s ,(6)
as = −1 + (k−r)/n
r−s , na s = (k−r)/n
r−s .(7)
Computing differences of squares viaa2
θ −na2
θ = (aθ −naθ)(aθ +naθ)gives
ˆMadj −ˆMnonadj = (a2
r −na2
r) + (a2
s −na2
s)
= 1
(r−s) 2
[(
1− 2(k−s)
n
)
+
(
1− 2(k−r)
n
)]
= 2(n−2k+r+s)
n∆ ,(8)
which equals (4) since r+ s = λ−µ . The complement G has parameters ¯k = n− 1 −k,
¯λ−¯µ = −(λ−µ ) −2, identical∆, and swapped multiplicities( m¯r,m¯s) = ( ms,mr), so
n−2¯k+ ¯λ−¯µ= −(n−2k+λ−µ), proving the sign-flip law. Finally,θr+θs = −2−2(r+s) = 2θ0
iff−2−2(λ−µ) = 2(n−1−2k), i.e., iffn−2k+λ−µ= 0.
3

--- Page 4 ---
Figure 1:Universal Cesàro return barrier and complement sign-flip law.(a) Exact
Cesàro return probabilityˆMuu across all16atlas SRGs (Certificate cert15): conference graphs
lie tightly on(n2 −2n+ 3)/(2n2) →1/2(green), while all non-conference SRGs lie strictly above
(red), with the entire region below the curve unconditionally forbidden. (b) Exact complement
sign-flip ˆMadj −ˆMnonadj across6non-self-complementary SRG pairs (Certificatecert02).
3 Infinite Non-Conference Off-Diagonal Uniform Family and
n≤1200Classification
Conference graphs achieveˆMadj = ˆMnonadj trivially viak = (n−1)/2and λ−µ = −1. Can
non-conferenceSRGs also achieve constant off-diagonal Cesàro transition probability? Setting
n−2k+λ−µ = 0imposes a rigid Diophantine constraint that isolates a single infinite polynomial
family anchored by the ternary Golay graph.
Theorem 2(Infinite Non-Conference Off-Diagonal Cesàro-Uniform Family and n≤ 1200
Classification).
(a) Exact Diophantine reduction:A primitive non-conferenceSRG(n,k,λ,µ )satisfies ˆMadj =
ˆMnonadj if and only ifλ−µ= 2k−n, which forces
(n−1)µ=k(n−k−1),(n−1)∆ =n
(
(2k−n+1) 2+(n−1)
)
,(n−1)|(2k−n+1) 2,
(9)
with∆a perfect integer square.
(b) Infinite polynomial family and absolute-bound dichotomy:For every integert≥ 1, the
parameter tuple
n(t) = (t+ 1)(4t+ 1) 2, k(t) =t(2t+ 1)(4t+ 3),
λ(t) = 4t3 + 2t2 −t−1, µ(t) = 2t(t+ 1)(2t+ 1)(10)
(and its complement) solves (9) identically with eigenvalues r = t, s = −(2t + 1)2,
multiplicities ms = t(4t+ 3), mr = 2k(t) = 2 t(2t+ 1)(4t+ 3), and exact constant off-
diagonal Cesàro mixingˆMadj = ˆMnonadj. Both Krein inequalities hold unconditionally for
all t≥ 1, while the absolute bound2n≤m s(ms + 3)fails uniquely at t= 1( n= 50 >35)
and holds strictly for everyt≥ 2. At t = 2,(243 ,110,37,60)is realized by the ternary
Golay dual coset graph [1], withˆMuu = 16295/19683and ˆMadj = ˆMnonadj = 14/19683.
(c) Exhaustiven≤ 1200classification:Exhaustive zero-float enumeration over all5 ≤n≤ 1200
(Certificate cert04) finds exactly4integral non-conference solutions withk< (n−1)/2:
4

--- Page 5 ---
Figure 2:Infinite non-conference off-diagonal uniform family and universal UAM
obstruction.(a) Absolute-bound dichotomy on n(t) = ( t + 1)(4t + 1)2: fails at t = 1
(n= 50 >35) and holds for allt≥ 2, anchored by the ternary Golay graph att= 2(243 ≤275).
(b) Unconditional UAM polytope violation|max c3∈[−1,1] c1(c3)|= 16t3+8t2+t−1
2 ≥12 >1across
allt≥1(Theorem 3(b)).
n = 50( t = 1, ruled out by absolute bound),n = 289((289 ,120,21,70), ruled out by
both KreinK2 and absolute bound289 >44), and uniquely thet-family survivorst= 2
(n= 243) andt= 3(n= 676).
Proof. Proof of(a).Substituting λ = 2 k−n + µ into k(k−λ− 1) = µ(n−k− 1)yields
k(n−k−µ− 1) = µ(n−k− 1), which rearranges to(n− 1)µ = k(n−k− 1). Multiplying
∆ = (2k−n) 2 + 4(k−µ)by(n−1)and substituting(n−1)µ=k(n−k−1)gives
(n−1)∆ = (n−1)(2k−n) 2 + 4(n−1)k−4k(n−k−1)
= (n−1)(2k−n) 2 + 4k2 =n
(
(2k−n+ 1) 2 + (n−1)
)
.(11)
Sincegcd(n,n−1) = 1, integrality of∆forces(n−1)|(2k−n+ 1) 2.
Proof of(b).Direct polynomial expansion (machine-checked in Lean Theoremsthm07–thm09)
confirms k(k−λ−1) = µ(n−k−1), r+s= t−(2t+1)2 = λ−µ = 2k−n, rs= −t(2t+1)2 = µ−k,
and mrr+mss= 2kt−t(4t+3)(2t+1)2 = −k. For KreinK1:( r+1)(k+r+2rs) ≤(k+r)(s+1)2;
since s= −(2t+ 1)2 and r= t, k+ r+ 2rs= 8t3 + 10t2 + 4t−2t(2t+ 1)2 = 2t2 + 2t> 0while
(s+1)2 = 16t2(t+1)2 andk+r= 4t(2t2+5t/2+1) ≥4t, giving(r+1)(2t2+2t) ≪(k+r)·16t2(t+1)2.
For Krein K2:( s+ 1)(k + s+ 2rs) ≤(k + s)(r + 1)2; note s+ 1 = −4t(t+ 1) < 0and
k+s+2rs= 8t3 +10t2 +3t−(4t2 +4t+1) −2t(4t2 +4t+1) = −2t2 −3t−1 = −(t+1)(2t+1) <0,
so LHS= 4 t(t+ 1)2(2t+ 1) = 8t4 + 20t3 + 16t2 + 4t, whilek+ s= 8t3 + 6t2 −t− 1and RHS
= (8t3 + 6t2 −t−1)(t+ 1) 2 = 8t5 + 22t4 + 19t3 + 3t2 −3t−1; subtracting yields RHS−LHS
= 8t5 + 14t4 −t3 −13t2 −7t−1 = (t−1)(8t4 + 22t3 + 21t2 + 8t+ 1) ≥0for all t≥ 1(with exact
equality att= 1). For the absolute bound2n≤m s(ms + 3): writingt=u+ 2(u≥0) gives
ms(ms + 3)−2n= 16u 4 + 120u3 + 309u2 + 299u+ 64>0 (∀u≥0),(12)
while att= 1, ms(ms + 3) = 70 <100 = 2n (machine-checked in Leanthm10). Part (c) follows
directly from Certificatecert04.
5

--- Page 6 ---
4 Moment-Line Polytope Dichotomy, Universalt-Family UAM
No-Go, and 16-Vertex IUM
ExpandingM(t) =|e −itkEk +e−itrEr +e−itsEs|◦2 gives the exact spectral transition law
M(t) = ˆM+ 2 cos
(
(k−r)t
)
(Ek◦Er) + 2 cos
(
(k−s)t
)
(Ek◦Es) + 2 cos
(
(r−s)t
)
(Er◦Es).(13)
Given any observation-time probability distributionνonR ≥0, define the cosine moment triple
c1 := E[cos((k−r )T)], c2 := E[cos((k−s )T)], c3 := E[cos((r−s )T)] ∈[−1,1]3. Because
E[M(T)]is doubly stochastic inspan{I,A, ¯A}, generalized UAM (E[M(T)] = 1
nJ) holds if and
only if its diagonal and adjacent entries both equal1/n [9], defining an exact rational affine line
(c1(c3),c2(c3))inR 3.
Theorem 3(Moment-Line Polytope Dichotomy, Universalt-Family UAM No-Go, and 16-Vertex
IUM).
(a) Universal UAM impossibility for the off-diagonal Cesàro-uniformt-family:For every t≥ 1,
the UAM moment line of the family(10)(and its complement) satisfies
c1(c3) =c 2(c3) =− 16t3 + 16t2 + 5t−1
2 −2t(2t+ 1)c 3.(14)
Consequently, for everyc3 ∈[−1,1]and everyt≥1,
c1(c3)≤ −16t3 + 8t2 +t−1
2 ≤ −12<−1,(15)
proving unconditionally thatnomember of the t-family (in particular, not the ternary
Golay graph SRG(243,110,37,60), where maxc1 = −161/2) admits UAM under any
observation-time distribution.
(b) Exact16 ×16Hadamard-involution IUM on Clebsch,L2(4), and Shrikhande:For both
SRG(16,5,0,2)(Clebsch) and the non-isomorphic cospectral pairSRG(16,6,2,2)( L2(4) =
K4□K4 with8copies of K4, and Shrikhande with0copies of K4), the moment linec1 =
−4−3c 3,c 2 =−3−4c 3 intersects[−1,1] 3 at the unique point(c1,c2,c3) = (−1,+1,−1),
attained instantaneously att∗ = π/4where eirπ/4U(π/4) = 2Er −I16 ∈{±1
4 }16×16 is a
real symmetric Hadamard involution with|U(π/4)xy|2 = 1/16for allx,y.
(c) Zero-float16-graph SRG UAM polytope atlas:Table 1 certifies the exact moment-line
intersections across16canonical SRGs, establishing empty-polytope UAM impossibility
for Schläfli(27 ,16,10,8)and its complement (requiringc3 ≤−14/9 <−1), Higman–Sims
(100,22,0,6)( c3 ≤−2 <−1), and Ternary Golay (c3 ≤−199/40 <−1), alongside
nonempty polytope intervals for all conference graphs (c1 = c2 = −n−3
4 −n−1
4 c3, passing
through( 1
2 ,1
2 ,−1)), Petersen (c3 ∈[−4/5,−11/16]), andGQ(2,2)(c 3 ∈[−1,−19/25]).
Proof. Proof of(a).In any off-diagonal Cesàro-uniform SRG (including the entiret-family (10)),
subtracting the non-adjacent entry of (13) from the adjacent entry uses ˆMadj = ˆMnonadj,
ar −nar = 1/(r−s ), as−nas = −1/(r−s ), andaras−narnas = −(n−2k+ λ−µ )/(n∆) = 0,
leaving 2
n(r−s) (c1 −c2) = 0and thus forcing c1 = c2 =: c. Evaluating the diagonal condition
1/n= ˆMuu+ 2mr
n2 c+ 2ms
n2 c+ 2mrms
n2 c3 and notingmr + ms = n−1, nˆMuu−1 = 1+m2
r+m2
s−n
n , we
obtain
2(n−1)c+ 2m rmsc3 =n−1−m 2
r −m2
s.(16)
6

--- Page 7 ---
Table 1: Zero-float16-graph SRG Cesàro average mixing and UAM moment-line atlas (Certifi-
catecert15).
GraphG(n,k,λ,µ) ˆMuu ˆMadj ˆMnonadj Off-unif? UAMc 3 bound Polytope?
C5 (Conf.)(5,2,0,1) 9/25 4/25 4/25Yes[−1,1/2]Nonempty
Paley(9)(Conf.)(9,4,1,2) 11/27 2/27 2/27Yes[−1,−1/4]Nonempty
Petersen(10,3,0,1) 21/50 49/450 19/450No[−4/5,−11/16]Nonempty
Paley(13)(Conf.)(13,6,2,3) 73/169 8/169 8/169Yes[−1,−1/2]Nonempty
GQ(2,2) (15,6,1,3) 107/225 19/450 61/1800No[−1,−19/25]Nonempty
Clebsch(16,5,0,2) 63/128 7/128 3/128No{−1}(IUM)t ∗ =π/4
L2(4)/Shrikh.(16,6,2,2) 59/128 7/128 3/128No{−1}(IUM)t ∗ =π/4
Paley(17)(Conf.)(17,8,3,4) 129/289 10/289 10/289Yes[−1,−5/8]Nonempty
T(7) (21,10,5,4) 233/441 302/11025 218/11025Noc 3 ≤−229/196Empty
Paley(25)(Conf.)(25,12,5,6) 289/625 14/625 14/625Yes[−1,−3/4]Nonempty
L2(5) (25,8,3,2) 321/625 26/625 6/625Noc 3 ≤−13/8Empty
Schläfli comp.(27,10,1,5) 437/729 14/729 19/1458Noc 3 ≤−14/9Empty
Schläfli(27,16,10,8) 437/729 19/1458 14/729Noc 3 ≤−14/9Empty
Chang /T(8) (28,12,6,4) 225/392 79/3528 37/3528Noc 3 ≤−17/10Empty
Higman–Sims(100,22,0,6) 3207/5000 57/5000 7/5000Noc 3 ≤−2Empty
Ternary Golay(243,110,37,60) 16295/19683 14/19683 14/19683Yesc 3 ≤−199/40Empty
Here n−1 = t(16t2 + 24t+ 9) = t(4t+ 3)2, ms = t(4t+ 3), andmr = 2t(2t+ 1)(4t+ 3), so every
term shares the exact common factor2t(4t+ 3). Dividing by2(n−1) = 2t(4t+ 3) 2:
mrms
n−1 = 2t(2t+ 1)(4t+ 3)·t(4t+ 3)
t(4t+ 3) 2 = 2t(2t+ 1),(17)
m2
r +m2
s −(n−1)
2(n−1) = t2(4t+ 3) 2(
4(2t+ 1) 2 + 1
)
−t(4t+ 3) 2
2t(4t+ 3) 2 = t(16t2 + 16t+ 5)−1
2 ,(18)
yielding (14) identically. Because−2t(2t+ 1) <0, the maximum ofc1(c3)on[ −1,1]occurs at
c3 = −1, where2c1(−1) = −(16t3 +16t2 +5t−1)+4 t(2t+1) = −(16t3 +8t2 +t−1) ≤−24 <−2
for allt≥1(Leanthm11).
Proof of(b)and(c).Forboth(16 ,5,0,2)(k= 5,r = 1,s = −3) and(16,6,2,2)(k= 6,r = 2,s =
−2), the frequency gaps arek−r = 4, r−s = 4, k−s = 8. Att∗= π/4, e−i(k−r)π/4 = e−iπ = −1
and e−i(s−r)π/4 = eiπ = −1, soeirπ/4U(π/4) = −Ek+ Er−Es = 2Er−I16. Certificates cert06–
cert08 explicitly construct the three16 ×16adjacency matrices over Z, verify E2
r = Er,
(2Er−I16)2 = I16, and every squared entry equals1/16in pure Q arithmetic, while distinguishing
L2(4)(8copies of K4) from Shrikhande (0copies ofK4). Part (c) follows from solving the2×2
rational affine moment system in Certificatescert01andcert09–cert15.
Remark1 (Polytope Nonemptiness vs. Realizability).Intersecting the moment line with[−1,1]3
is a necessary condition for UAM (sufficient to yield unconditional impossibility proofs whenever
empty, as in Theorem 3(a) and on Schläfli and Higman–Sims). When nonempty, exact realizability
by a probability law onR≥0 additionally depends on the trigonometric moment curve{(cos((k−
r)t),cos ((k−s )t),cos ((r−s )t)) : t≥ 0}(e.g., atc3 = −1,( k−s )t= (k−r )t+ (2j+ 1)π forces
c1 + c2 = 0, matching Clebsch’s(−1,+1,−1)while ruling out the conference endpoint(1
2 ,1
2 ,−1)
in favor of interiorc3 >−1[9]).
5 Formal Verification Architecture and Scope
Our verification artifact cleanly separates machine-checked algebraic identities from exact rational
matrix and parameter enumerations:
7

--- Page 8 ---
Figure 3:Exact UAM moment lines and16×16Hadamard IUM involution.(a) Affine
moment linesc1(c3),c2(c3)against the[ −1,1]cosine band: Paley(9)and Petersen intersect cleanly,
Clebsch/L2(4)( c1 solid, c2 dashed) meets uniquely at the IUM corner(c3,c1,2) = ( −1,∓1),
while Schläfli lies strictly below−5/2 <−1. (b) Exact16 ×16Clebsch Hadamard involution
2E1 −I16 ∈{±1
4 }16×16 achieving instantaneous uniform mixing att∗=π/4.
• Layer 1 — Constructive Lean 4.36.0 Kernel(lean/CtqwSrgAverageMixing.lean):
Twenty theorems compiled withlean-DwarningAsError=true, zero external dependencies,
zero sorry, zerogrind, zeroClassical.choice, and no custom axioms beyond standard
constructive propext/Quot.sound (audited via#print axioms). Layer 1 machine-checks
the Cesàro return-barrier identity, sharp lower bound, and strict non-uniformity forn≥ 4
(thm01–thm03), the complement sign-flip law, conference uniformity, and Seidel midpoint
equivalence (thm04–thm06), the infinitet-family SRG feasibility, eigenvalue, multiplicity,
absolute-bound dichotomy (t= 1vs. t≥ 2), and universal UAM impossibility identities
(thm07–thm11), exact Ternary Golay, conference, Clebsch/Shrikhande, Petersen,GQ(2,2),
Schläfli/Higman–Sims, and spurious-289obstructions (thm12–thm19), and the general
Diophantine discriminant identity(9) (thm20). The Bose–Mesner projector algebra, Galois-
conjugation rationality, and unitary evolutionU(t) = e−itA derivations are proved in full
detail in Sections 2–4.
• Layer 2 — Zero-Float Exact Python Verifier(verification/verify_ctqw_s
rg_mixing.py ): An AST-audited pure standard-library verifier using strictlyint and
fractions.Fraction (zero floats, zero numeric division or exponentiation, zerolimit_
denominator ), emitting16SHA-256 certificates under certificates/MANIFEST.json
and validated by56adversarialpytestchecks intests/test_adversarial.py. Layer 2
independently executes the exhaustiven≤ 1200Diophantine scan (cert04), verifies the
t-family closed-form moment line fort= 1,..., 12( cert03), directly builds and checks the
10×10Petersen projectors and16×16Clebsch,L 2(4), and Shrikhande Hadamard IUM
involutions overQ (cert06–cert09), and computes the16-graph exact SRG mixing atlas
(cert15).
References
[1] E. R. Berlekamp, J. H. van Lint, and J. J. Seidel,A strongly regular graph derived from
the perfect ternary Golay code, inA Survey of Combinatorial Theory, North-Holland, 1973,
pp. 25–30.
8

--- Page 9 ---
[2] A. E. Brouwer and H. Van Maldeghem,Strongly Regular Graphs, Encyclopedia of Mathe-
matics and its Applications, vol. 182, Cambridge University Press, 2022.
[3] A. Chan,Complex Hadamard matrices, instantaneous uniform mixing and cubes, Algebr.
Comb.3(2020), 757–774 (arXiv:1102.5601).
[4] G. Coutinho, C. Godsil, K. Guo, and F. Vanhove,Perfect state transfer on distance-regular
graphs and association schemes, Linear Algebra Appl.478(2015), 108–130.
[5] E. Farhi and S. Gutmann,Quantum computation and decision trees, Phys. Rev. A58
(1998), 915–928.
[6] C. Godsil,State transfer on graphs, Discrete Math.312(2012), 129–147.
[7] C. Godsil,Average mixing of continuous quantum walks, J. Combin. Theory Ser. A120
(2013), 1649–1662.
[8] C. Godsil, N. Mullin, and A. Roy,Uniform mixing and association schemes, Electron. J.
Combin.24(2017), #P3.22.
[9] M. Kang,Moment methods for uniform average mixing on strongly regular graphs,
arXiv:2610.10017 (2026).
9
