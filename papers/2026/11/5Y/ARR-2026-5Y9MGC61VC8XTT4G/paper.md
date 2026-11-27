# Orthogonal Minimax Coherence, Conference-Matrix Rigidity, and Cyclotomic MUB Obstructions

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5Y9MGC61VC8XTT4G` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/orthogonal-minimax-coherence-and-conference-rigidity (`v1.0.0`)  
**Canonical PDF SHA-256:** `276468304d3e33d22dff0985248b4a09ffa98ecb890a0fb84e55b9cfe079742e`

## Abstract

We resolve the orthogonal minimax coherence problem mu_R(d) = min_{U in O(d)} ||U||_max across the entire non-Hadamard residue class d === 2 (mod 4) and establish a sharp polynomial secant lower bound with spectral rigidity for all odd dimensions d >= 3. First, via a three-line pure-polynomial identity paired with a Hadamard three-row sign-parity obstruction, we prove mu_R(d) >= 1/sqrt(d - 1) for every d = 4k + 2 >= 6, together with a complete rigidity theorem: equality holds if and only if sqrt(d - 1) U is a conference matrix up to column permutation. Combining this rigidity with the Paley constructions and Belevitch's sum-of-two-squares necessary condition yields an exact arithmetic dichotomy: mu_R(d) = 1/sqrt(d - 1) for every conference-matrix order (realized rationally in O(10, Q) and O(26, Q)), while strict inequality mu_R(d) > 1/sqrt(d - 1) holds unconditionally whenever d - 1 is not a sum of two squares (d = 22, 34, 58, 70, 78, ...). Second, for every odd d >= 3, a pure-polynomial secant inequality yields mu_R(d) >= 2/sqrt(4d - 3), strictly sharpening both the Welch bound 1/sqrt(d) and the quadratic bound sqrt(2/(2d - 1)). Analyzing the equality locus reduces attainment to a symmetric Seidel matrix satisfying S^2 + S = (d - 1)I_d; zero trace forces s = sqrt(4d - 3) to divide d and hence s | 3, proving that equality holds if and only if d = 3 (mu_R(3) = 2/3, rigidly attained by I_3 - (2/3)J_3) and strict inequality mu_R(d) > 2/sqrt(4d - 3) holds for every odd d >= 5. Using rational skew-Cayley transforms, we exhibit exact rational circulant witnesses in SO(5, Q) (mu = 6/11 < 3/5) and SO(7, Q) (mu = 1188/2437 < 5/7). Third, translating these results to real mutually unbiased bases (MUBs) quantifies the unavoidable real two-basis coherence excess over the complex Welch bound 1/d, contrasted against an exhaustive exact Z[zeta_24] cyclotomic ring search over all 24^5 phase vectors unbiased to {I_6, F_6} in C^6, which certifies exactly 12 rays forming 4 orthonormal bases with distinct-ray overlap spectrum strictly {0, 1/3} and zero pairs at 1/6. A two-layer verification artifact accompanies the paper: 20 constructive, axiom-free Lean 4.36.0 theorems formalizing the scalar-algebraic, parity, divisibility, and exact-witness kernel, paired with 16 zero-float Python certificates verifying the matrix constructions, Belevitch classification, and exhaustive cyclotomic search.

## Full Extracted Text

--- Page 1 ---
Orthogonal Minimax Coherence, Conference-Matrix
Rigidity,
and Cyclotomic MUB Obstructions
Lluis Eriksson∗
November 27, 2026
Abstract
We resolve the orthogonal minimax coherence problemµR(d) := minU∈O(d) maxi,j |Uij|
across the entire non-Hadamard residue classd≡ 2 ( mod 4)and establish a sharp polynomial
secant lower bound with spectral rigidity for all odd dimensionsd≥ 3. First, combining
a three-line pure-polynomial identity with a Hadamard three-row sign-parity obstruction,
we proveµR(d) ≥1/
√
d−1 for everyd = 4k+ 2 ≥6, together with a complete rigidity
theorem: equality holds if and only if
√
d−1U is a conference matrix up to column
permutation. Pairing this rigidity with Paley constructions and Belevitch’s sum-of-two-
squares necessary condition yields an exact arithmetic dichotomy:µR(d) = 1/
√
d−1 for
every conference-matrix order (realized rationally inO(10,Q)and O(26,Q)), whereas strict
inequalityµR(d) >1/
√
d−1 holds unconditionally wheneverd−1is not a sum of two squares
(d = 22,34,58,70,78,... ). Second, for every oddd≥ 3, a pure-polynomial secant bound
yields µR(d) ≥2/
√
4d−3 , strictly sharpening both the Welch bound1/
√
dand the quadratic
bound
√
2/(2d−1) . Analyzing the equality locus reduces attainment to a symmetric Seidel
matrix satisfyingS2 +S = (d−1)Id; zero trace forcess=
√
4d−3 to dividedand hences| 3,
proving that equality holds if and only ifd= 3( µR(3) = 2/3, rigidly attained byI3 −2
3 J3)
and strict inequalityµR(d) >2/
√
4d−3 holds for every oddd≥ 5. Via rational skew-Cayley
transforms we construct exact rational circulant witnesses inSO(5,Q)( µ = 6/11 < 3/5)
and SO(7,Q)( µ = 1188/2437 < 5/7). Third, translating these bounds to real mutually
unbiased bases (MUBs) quantifies the unavoidable real two-basis coherence excess over the
complex Welch bound1/d, contrasted against an exhaustive exactZ[ζ24]cyclotomic ring
search over all245 = 7,962,624normalized phase vectors unbiased to{I6,F6}in C6, certifying
exactly12rays forming4orthonormal bases whose distinct-ray overlaps lie strictly in{0,1/3}
with zero pairs at1/6. A two-layer verification artifact accompanies the paper: Layer 1
formalizes the scalar-algebraic, parity, divisibility, and exact-witness arithmetic kernel in
20constructive, axiom-free Lean 4.36.0 theorems (0sorry,0 Classical.choice); Layer 2
verifies all full matrix constructions, Belevitch classifications, and the exhaustiveZ[ζ24]search
in16zero-float Python certificates and56adversarial tests.
1 Introduction
For every integerd≥ 1, how delocalized can ad-by-d real orthogonal matrix be? Formally,
define theorthogonal minimax coherence
µR(d) := min
U∈O(d)
∥U∥max,∥U∥ max := max
1≤i,j≤d
|Uij|.(1)
∗Independent Researcher. Code, Lean 4.36.0 proofs, and zero-float certificates archived athttps://github.c
om/lluiseriksson/orthogonal-minimax-coherence-and-conference-rigidity (v1.0.0, MIT / CC-BY-4.0,
AIRR-FOUNDER-1.0). Manuscript and verification artifacts prepared with Google Antigravity assistance.
1

--- Page 2 ---
Since each row of U∈O (d)has unit Euclidean norm, the Welch lower bound [13] gives
µR(d) ≥1/
√
d. Over Cd, the discrete Fourier transformFd = 1√
d(ωjk
d )attains the unitary
minimum1 /
√
d in every dimension. OverRd, equality µR(d) = 1 /
√
d holds if and only if a
real Hadamard matrix of orderd exists, which is impossible unlessd∈{ 1,2}or4 |d. Outside
Hadamard orders, the exact value ofµR(d)has remained largely open apart from the elementary
dimensiond= 3, whereµ R(3) = 2/3is attained by the Householder reflectionI3 −2
3 J3.
The same quantity governs the geometry of real mutually unbiased bases (MUBs) [14, 4, 8].
For two orthonormal basesB1,B2 of Rd (or Cd) with change-of-basis matrixU, the maximum
squared transition probability isµ2(B1,B2) := maxu∈B1,v∈B2 |⟨u,v⟩|2 = ∥U∥2
max. Thus µR
2 (d) :=
minB1,B2 µ2(B1,B2) = µR(d)2 measures the optimal approximation to a pair of real MUBs when
no Hadamard matrix of orderd exists. In dimension d = 6, the smallest non-prime-power
dimension where the maximal number of complex MUBs is famously conjectured to be3rather
than7[ 3, 5, 6, 10], comparing the real obstruction (µR
2 (6) = 1/5 >1/6) against the complex
cyclotomic obstruction highlights two sharply distinct algebraic mechanisms.
Main Contributions
1. Complete Resolution and Rigidity ford≡ 2 ( mod 4)(Theorem 1).We prove
µR(d) ≥1/
√
d−1 for everyd= 4k+ 2 ≥6via a three-line pure-polynomial inequality and
a Hadamard three-row sign-parity obstruction, with zero calculus. We further establish
completerigidity: ∥U∥max = 1/
√
d−1 ifandonlyif
√
d−1U isaconferencematrix[ 1,9,7]
up to column permutation (closing all partial-zero cases|N0|≥ 3, |N0|= 1, and|N0|= 2).
Combining this rigidity with Paley constructions [11] and Belevitch’s theorem [1, 2] yields
an exact arithmetic dichotomy: µR(d) = 1 /
√
d−1 for every conference-matrix order
(d= 6,10,14,18,26,30,... ), whileµR(d) >1/
√
d−1 strictly wheneverd−1is not a sum
of two squares (d= 22,34,58,70,78,94,...).
2. Secant Bound, Unique d = 3Rigidity, and Rational Circulants for Odd d
(Theorem 2).For every oddd≥ 3, we proveµR(d) ≥2/
√
4d−3 using a pure-polynomial
secant identity. Analyzing the equality locus forces2µ−1U (up to signed permutations) to
take the formId+ 2S where S is a symmetric Seidel matrix [12] obeyingS2 +S = (d−1)Id.
Trace vanishing forcess=
√
4d−3 to be an integer dividingd, hences| (4d−s 2) = 3,
proving that equality holds if and only ifd = 3( µR(3) = 2 /3) and strict inequality
µR(d) > 2/
√
4d−3 holds for every oddd≥ 5. Using rational skew-Cayley transforms
(I−A )(I + A)−1, we construct explicit exact rational circulant witnesses inSO(5,Q)
(µ= 6/11) andSO(7,Q)( µ= 1188/2437), beating the Householder reflections3/5and
5/7.
3. Real MUB Defect vs. Exact Z[ζ24]MUB-6 Obstruction (Theorem 3).We
translate Theorems 1–2 into exact real two-basis MUB coherence excess bounds over1/d,
and contrast them with an exhaustive exact ring computation inZ[ζ24] = Z[x]/(x8 −x4 +1)
over all245 = 7,962,624normalized24th-root phase vectors unbiased to {I6,F6}. Exactly
12rays survive, forming4orthonormal bases (an8-regular orthogonality graph whose
complement is2K3,3) with distinct-ray overlaps strictly in{0,1/3}and zero pairs at the
MUB-6 target1/6.
2 Minimax Coherence and Conference-Matrix Rigidity ford≡ 2
(mod 4)
Recall that ad×d conference matrixC has0on the diagonal, ±1off the diagonal, and satisfies
C⊤C = (d−1)Id [1, 9]. For d≡ 2 ( mod 4), any conference matrix can be normalized to be
2

--- Page 3 ---
symmetric, and Belevitch’s theorem [1, 2] states that a conference matrix of orderd≡ 2 ( mod 4)
can exist only ifd−1 =a 2 +b2 is a sum of two integer squares.
Theorem 1(Complete Minimax Coherence and Conference Rigidity ford≡ 2 ( mod 4)).Let
d= 4k+ 2≥6.
(a) Unconditional lower bound:For everyU∈O(d),
∥U∥max ≥ 1√
d−1 .(2)
(b) Complete rigidity:An orthogonal matrixU∈O (d)attains ∥U∥max = 1/
√
d−1 if and only
if there exists a permutation matrixΠsuch that
√
d−1UΠis ad×dconference matrix.
(c) Belevitch–Paley arithmetic dichotomy:Whenever a conference matrix of orderd exists (in
particular for everyd= q+1with q≡ 1 ( mod 4)a prime power via the Paley construction,
including rational orthogonal realizations1
3 C10 ∈O(10,Q)and 1
5 C26 ∈O(26,Q)), we have
exact equalityµR(d) = 1/
√
d−1 . Conversely, wheneverd−1is not a sum of two integer
squares (for instanced∈{ 22,34,58,70,78,94}and every d≡ 4,7 ( mod 9)with d≡ 2
(mod 4)), strict inequality holds:
µR(d)> 1√
d−1 .(3)
Proof.We first record two elementary scalar facts for any real numbers0≤x,y≤µ:
xy−(x 2 +y2 −µ2) = (µ−x)(µ−y) +x(µ−x) +y(µ−y)≥0,(4)
x2 +y2 +xy≤3µ 2.(5)
Both (4) and (5) are immediate algebraic identities/bounds, with equality in(5) iff x= y= µ,
and equality in (4) forx,y >0iffx=y=µ.
Proof of(a).Suppose for contradiction that U∈O (d)has µ := ∥U∥max < 1/
√
d−1 , so
(d−1)µ 2 <1. For every entryUij, unit row norm implies
U2
ij = 1−
∑
ℓ̸=j
U2
iℓ ≥1−(d−1)µ 2 >0,(6)
so every entry ofU is strictly nonzero and has a well-defined signσij ∈{+1,−1}. Consider
the first three rowsr1,r2,r3 of U (valid sinced≥ 6). Multiplying columnj by σ1j preserves
O(d)and ∥U∥max while ensuringσ1j = +1for all j∈{ 1,...,d} . Partition{1,...,d} by the sign
pairs( σ2j,σ3j)into four cardinalities a,b,c,e corresponding to(+ ,+),(+,−),(−,+),(−,−), so
a+ b+ c+ e= d= 4k+ 2. The counts of positive entrywise products among the three pairs of
rows arep12 =a+b,p 13 =a+c, andp 23 =a+e, whose sum is
p12 +p13 +p23 = 2a+ (a+b+c+e) = 2a+ 4k+ 2≡0 (mod 2).(7)
Since3(2 k+ 1) = 6k+ 3is odd, we cannot havep12 = p13 = p23 = 2k+ 1. Hence some pair of
rows( u,v)among {r1,r2,r3}(after replacingv by −v if necessary) satisfies|P|= p≥ 2k+ 2and
|N|=q=d−p≤2k, whereP:={j:u jvj >0}andN:={j:u jvj <0}partition{1,...,d}.
Writexj := |uj|∈ (0,µ]and yj := |vj|∈ (0,µ]. Using⟨u,v⟩= 0, (4) on P, ∑d
j=1(x2
j+y2
j) = 2,
and (5) onN:
0 =
∑
j∈P
xjyj −
∑
j∈N
xjyj ≥
∑
j∈P
(x2
j +y2
j −µ2)−
∑
j∈N
xjyj
= 2−pµ 2 −
∑
j∈N
(x2
j +y2
j +xjyj)
≥2−(p+ 3q)µ 2 = 2−(d+ 2q)µ 2.(8)
3

--- Page 4 ---
Because q≤ 2k= (d−2)/2, we haved+2q≤ 2(d−1), whence2 ≤2(d−1)µ2, i.e.,µ2 ≥1/(d−1),
contradictingµ<1/
√
d−1.
Proof of(b).If
√
d−1U Πis a conference matrix, clearlyU∈O (d)and ∥U∥max = 1/
√
d−1 .
Conversely, supposeU∈O (d)attains µ = ∥U∥max = 1/
√
d−1 . Call a rowzero-bearingif it
contains at least one zero entry, and letZ⊆{ 1,...,d} be the set of zero-bearing rows and
N0 :={1,...,d}\Zthe set of strictly nonzero rows.
Step 1 (Zero-bearing rows and distinct zero columns).If row i∈Z has Uij = 0, then
1 = ∑
ℓ̸=j U2
iℓ ≤(d−1)µ2 = 1, forcing|Uiℓ|= µ for allℓ̸= j; thus every row inZ has aunique
zero entry andd−1entries in {±µ}. Moreover, two distinct rowsi1,i2 ∈Z cannot have their
unique zero in the same columnj: otherwise µ−2⟨ri1 ,ri2 ⟩would be a sum ofd−1 = 4k+ 1
(odd) numbers in{±1}, which can never equal0. Therefore the zeros ofZ occupy |Z|distinct
columns CZ ⊆{1,...,d} . Applying the same unit-norm argument to each columnc∈C Z shows
that every columnc∈C Z has a unique zero (inZ) and all remainingd−1entries in {±µ}; in
particular, every entry inN0 ×CZ has magnitudeµ.
Step 2 (Eliminating|N0|≥ 3).If |N0|≥ 3, every entry of any three rows inN0 is strictly
nonzero, so the exact sign-parity and polynomial derivation(8) applies verbatim to some pair
u,v∈N 0 with q≤ 2k. Since2 −2(d−1)µ2 = 0, equality must hold throughout(8). Because
xj,yj > 0for all j, equality in(4) on P and in(5) on N forces xj = µ for allj∈{ 1,...,d} ,
yielding∥u∥2
2 =dµ2 =d/(d−1)>1, a contradiction. Thus|N 0|≤2.
Step 3 (Eliminating|N0|= 1).If N0 = {r1}, letC0 = {1,...,d}\C Z = {c1}. By Step 1,
row r1 has |CZ|= d−1entries of magnitude µ, whose sum of squares is already(d−1)µ2 = 1.
HenceU r1,c1 = 0, contradictingr1 ∈N0.
Step 4 (Eliminating|N0|= 2).If N0 = {r1,r2}, letC0 = {c1,c2}. By Step 1, rowr1 has
|CZ|= d−2entries of magnitude µ, soU2
r1,c1 + U2
r1,c2 = 1 −(d−2)µ2 = µ2. WriteUr1,c1 = µα
and Ur1,c2 = µβ with α2 + β2 = 1and α̸= 0, β̸= 0. Since |Z|= d−2 ≥4, pick any rowi∈Z ;
let ji ∈CZ be its unique zero column. Rowi has entries±µ in alld−3 = 4k−1columns of
CZ \{ji}and inc1,c2 (with signsσ1,σ2 ∈{±1}). Orthogonality ⟨r1,ri⟩= 0divides by µ2 to
give
0 =mi +σ1α+σ 2β,(9)
where mi is a sum of4k−1(odd) numbers in {±1}, hence an odd integer. Yet(σ1α+ σ2β)2 =
α2 + β2 + 2σ1σ2αβ = 1 + 2 σ1σ2αβ≤ 2 < 9, so the odd integermi must satisfy m2
i = 1.
Consequently1 + 2σ1σ2αβ= 1, forcingαβ= 0, contradictingα,β̸= 0.
Therefore N0 = ∅: every row and column contains a unique zero, and all off-zero entries lie
in {±1/
√
d−1}. Permuting columns to place the zeros on the diagonal makes
√
d−1U Πa
conference matrix.
Proof of(c).Because O(d)is compact and U↦→∥U∥max is continuous,µR(d)is attained by
some U∗ ∈O (d). By (b), µR(d) = 1 /
√
d−1 if and only if a conference matrix of orderd
exists. For every prime powerq≡ 1 ( mod 4), Paley’s quadratic-residue construction [11] yields
a symmetric conference matrix of orderd= q+ 1; whenq is an odd square (q= 9,25,49,... ),
1√qCq+1 ∈O (q+ 1,Q)is rational orthogonal. Conversely, by Belevitch’s theorem [1, 2], no
conference matrix of order d≡ 2 ( mod 4)exists unless d− 1is a sum of two squares, so
compactness and (b) force strict inequalityµR(d)>1/
√
d−1.
3 Odd Dimensions: Secant Bound, Spectral Rigidity, and Ra-
tional Circulants
For odd dimensions d = 2 k + 1 ≥3, every pair of orthogonal rows automatically has an
unbalanced sign partition (|P|̸= |N|) whenever all entries are nonzero, eliminating the need
4

--- Page 5 ---
Figure 1:Orthogonal minimax coherence landscape across residue classes.(a) Welch-
normalized coherence
√
dµR(d)for2 ≤d≤ 34: Hadamard orders achieve1, conference
orders (d≡ 2 ( mod 4), d− 1 = a2 + b2) achieve
√
d/(d−1) (Theorem 1), red triangles
mark the lower bound
√
d/(d−1) at Belevitch-obstructed orders (d = 22 ,34) where strict
inequality µR(d) >1/
√
d−1 holds, and odd orders satisfy the secant lower bound2
√
d/(4d−3)
(Theorem 2) with exact rational witnesses atd = 3 ,5,7. (b) Relative real two-basis MUB
coherence excessdµR
2 (d) −1comparing the odd secant bound3/(4d−3), the quadratic bound
1/(2d−1), and the conference bound1/(d−1).
for three rows. Replacing the quadratic bound(4) by an exact secant linearization of
√
µ2 −s
sharpens the lower bound uniformly and yields a complete spectral-divisibility rigidity theorem.
Theorem 2(Odd-Dimension Secant Bound, Uniqued= 3Tightness, and Rational Witnesses).
Letd= 2k+ 1≥3be odd.
(a) Unconditional secant lower bound:For everyU∈O(d),
∥U∥max ≥ 2√
4d−3 >
√
2
2d−1 > 1√
d
.(10)
(b) Uniqued= 3tightness via spectral divisibility:Equalityµ R(d) = 2/
√
4d−3holds if and
only ifd= 3(where µR(3) = 2/3, rigidly attained up to signed row/column permutations
byI 3 −2
3 J3). For every oddd≥5, strict inequality holds unconditionally:
µR(d)> 2√
4d−3 .(11)
(c) Exact rational circulant upper bounds:Rational skew-Cayley transforms yield explicit
special orthogonal circulant witnessesU5 = 1
11 circ(3,6,2,−6,6) ∈SO (5,Q)and U7 =
1
2437 circ(−939,−522,1158,−384,1188,894,1042)∈SO(7,Q), certifying
2√
17 <µR(5)≤ 6
11 < 3
5, 2
5 <µR(7)≤ 1188
2437 < 5
7,(12)
strictly improving the Householder upper bounds(d−2)/d.
Proof. Proof of(a).Let U∈O (d)with µ:= ∥U∥max, and assumeµ≤ 2/
√
4d−3 (otherwise (a)
is immediate). Since4(d−1) <4d−3, we have(d−1)µ2 ≤4(d−1)/(4d−3) <1, so every entry
satisfies U2
ij ≥1 −(d−1)µ2 >0(strictly nonzero). Set∆ := dµ2 −1. Because d is odd, the
5

--- Page 6 ---
row entries cannot all equal±1/
√
d (else two rows would have inner product1
d
∑d
j=1(±1) ̸= 0),
so0 < ∆ < µ2. Let r :=
√
µ2 −∆ =
√
1−(d−1)µ 2 > 0and c := (µ−r )/∆ > 0. Since
2cµ−c 2∆ =c(2µ−(µ−r)) = (µ−r)(µ+r)/∆ = 1, we have the exact polynomial identity
(µ2 −s)−(µ−cs) 2 =c2s(∆−s)≥0∀s∈[0,∆],(13)
with equality iff s∈ {0,∆}. Taking square roots (as µ−cs≥µ−c ∆ = r > 0) gives√
µ2 −s≥µ−cson[0,∆].
Now pick any two distinct rowsu,v of U. Since all entries are nonzero andd= 2k+ 1is
odd, replacing v by −v if necessary gives|P|= p≥k + 1and |N|= q = d−p≤k . Define
sj := µ2 −u2
j ∈[0,∆]and tj := µ2 −v2
j ∈[0,∆], so∑d
j=1 sj = ∑d
j=1 tj = ∆. On P, multiplying
|uj|≥µ−cs j and|v j|≥µ−ct j yields
|ujvj|≥(µ−cs j)(µ−ct j) =µ2 −cµ(sj +tj) +c2sjtj ≥µ2 −cµ(sj +tj).(14)
Summing (14) overj∈P, noting ∑
j∈P(sj +tj)≤2∆andc∆ =µ−r, gives
∑
j∈P
|ujvj|≥pµ 2 −2µc∆ = (p−2)µ 2 + 2µr.(15)
OnN, ∑
j∈N |ujvj|≤qµ 2. Since⟨u,v⟩= 0andq−p≤−1, we obtain
2µr≤(q−p+ 2)µ 2 ≤µ2 =⇒2r≤µ=⇒4
(
1−(d−1)µ 2)
≤µ2,(16)
which rearranges to(4d−3)µ2 ≥4, provingµ≥ 2/
√
4d−3 . The strict comparisons4/(4d−3) >
2/(2d−1) >1/dhold for alld≥ 3because4(2 d−1)−2(4d−3) = 2 >0and4 d−(4d−3) = 3 >0.
Proof of(b).Suppose U∈O (d)attains equality µ= 2/
√
4d−3 . Then r= µ/2, and for every
pair of rows(u,v)(oriented so p≥k + 1), equality must hold in every step of (a):p= k+ 1,
q= k; sj = tj = 0for all j∈N ; ∑
j∈P sj = ∑
j∈P tj = ∆; sj,tj ∈{0,∆}by (13); andsjtj = 0
for allj∈P by (14). Consequently, every row ofU hasexactly oneentry of magnitude r= µ/2
andd−1entries of magnitudeµ, and no two rows share the column of their(µ/2)-entry.
Permuting columns so the(µ/2)-entries lie on the diagonal, and scalingM := 2
µU, we obtain
an integer matrixM with diagonal entriesσii ∈{±1}, off-diagonal entries2σij (σij ∈{±1}), and
MM⊤= (4d−3)Id. Multiplying rowi by σii preserves orthogonality and sets every diagonal
entry ofMto+1. For any distinct rowsi̸=j, orthogonality⟨M i,Mj⟩= 0gives
2(σij +σji) + 4
∑
ℓ̸=i,j
σiℓσjℓ = 0 =⇒ σij +σji
2 =−
∑
ℓ̸=i,j
σiℓσjℓ.(17)
Because d−2is odd, the right-hand side is an odd integer; since(σij + σji)/2 ∈{−1,0,+1}, it
cannot be0, forcing σij = σji for alli̸= j. ThusM = Id + 2S, whereS is a symmetric Seidel
matrix (S=S ⊤,S ii = 0,S ij ∈{±1}fori̸=j). ExpandingM 2 = (4d−3)I d yields
Id + 4S+ 4S2 = (4d−3)I d ⇐⇒S 2 +S= (d−1)I d.(18)
Every eigenvalue ofS therefore belongs to
{−1+
√
4d−3
2 , −1−
√
4d−3
2
}
, with integer multiplicities
m+,m−summing tod. Sincetr(S) = 0,
0 =−d
2 + (m+ −m−)
√
4d−3
2 =⇒(m + −m−)
√
4d−3 =d.(19)
Because d> 0and m+ −m−∈Z , the quantitys:=
√
4d−3 = d/(m+ −m−)is rational and its
square4 d−3is an integer, sos∈Z >0 and s|d . Therefore s| (4d−s 2) = 3, forcings∈{ 1,3}.
Since d≥ 3,4 d−3 ≥9, so uniquelys= 3and d= 3. Atd= 3, S2 + S = 2I3 forces S to have
6

--- Page 7 ---
Figure 2:Exact rational witnesses and Belevitch arithmetic dichotomy.(a) Rational
orthogonal Paley conference matrix1
3 C10 ∈O(10,Q)achieving µR(10) = 1/3. (b) Exact rational
circulant U5 ∈SO (5,Q)achieving µ = 6 /11 < 3/5. (c) Belevitch dichotomy across all25
dimensions d≡ 2 ( mod 4)with6 ≤d≤ 102: Paley prime-power orders (blue), remaining
sum-of-two-squares orders (green), and Belevitch-obstructed ordersd∈{ 22,34,58,70,78,94}
proving strict gapµR(d)>1/
√
d−1(red).
eigenvalues1(multiplicity2) and −2(multiplicity1), hence S = −(J3 −I3)up to diagonal sign
conjugation, recoveringU = I3 −2
3 J3 uniquely up to signed permutations. For every oddd≥ 5,
compactness ofO(d)then yields strict inequalityµ R(d)>2/
√
4d−3.
Proof of(c).For any skew-symmetricA∈Q d×d, the Cayley transformU = (Id−A)(Id+A)−1 lies
in SO(d,Q). Taking circulant skew-symmetric generators onZ5 with( a1,a2) = (1/2,−1)gives
U5 = 1
11 circ(3,6,2,−6,6), satisfyingU⊤
5 U5 = I5, det(U5) = +1, and ∥U5∥max = 6/11. Taking
(a1,a2,a3) = (4,−1,−2)on Z7 gives U7 = 1
2437 circ(−939,−522,1158,−384,1188,894,1042) ∈
SO(7,Q)with ∥U7∥max = 1188/2437. Direct integer arithmetic confirms4·112 = 484 <612 =
17·6 2,6/11<3/5,2/5<1188/2437<5/7.
4 Real MUB Coherence Defect vs. ExactZ[ζ24]MUB-6 Obstruc-
tion
In quantum information theory, two orthonormal basesB1,B2 of Fd (F∈{R,C} ) are mutually
unbiased if|⟨u,v⟩|2 = 1/d for all u∈B 1,v∈B 2 [14, 8]. While complex MUB pairs exist in
every dimension viaFd, real MUB pairs fail wheneverd /∈{1,2}∪ 4Z [4]. In C6, pairs and
triples of MUBs exist (including infinite continuous families of MUB-triplets [3, 10]), whereas
no quadruple of MUBs has ever been found [5, 6]. We pair our exact real two-basis coherence
defects with an exhaustive, zero-float algebraic certification of the24th-root cyclotomic sector
unbiased to{I6,F6}.
Theorem 3(Real MUB Excess and ExhaustiveZ[ζ24]MUB-6 Cyclotomic Obstruction).
(a) Unavoidable real two-basis MUB coherence excess:Over all pairs of orthonormal bases
(B1,B2)ofR d, letµR
2 (d) := minB1,B2 maxu∈B1,v∈B2 ⟨u,v⟩2. Then:
µR
2 (d)− 1
d ≥ 1
d(d−1) (d≡2 (mod 4), d≥6;strict ifd−1̸=a 2 +b2),(20)
µR
2 (d)− 1
d ≥ 3
d(4d−3) (dodd, d≥3;exact1/9atd= 3,strict ford≥5).(21)
(b) Exhaustive Z[ζ24]MUB-6 sector classification:Let V24 ⊂C 6 be the subset of the245 =
7,962,624normalized24th-root phase vectors v = 1√
6 (1,ζe1
24,...,ζ e5
24)⊤ (ej ∈Z/24Z) that
7

--- Page 8 ---
Figure3:Exhaustive Z[ζ24]cyclotomicMUB-6obstruction.(a)ExactGramoverlapmatrix
|⟨ui,uj⟩|2 across all12rays in V24 unbiased to{I6,F6}. (b) Distinct-ray overlap distribution (48
orthogonal pairs at0,18pairs at1/3, and strictly0pairs at the MUB-6 target1/6).
are unbiased to bothI6 and the6-point Fourier basisF6. Exhaustive exact arithmetic in
the cyclotomic ringZ[ζ24] ∼= Z[x]/(x8 −x4 + 1)certifies:
(i)|V24|= 12exactly;
(ii) the orthogonality graph onV24 is8-regular (complement isomorphic to2 K3,3) and
contains exactly4orthonormal bases (6-cliques);
(iii) across all
(12
2
)
= 66distinct pairs in V24, the exact squared overlap spectrum is
{0 (48 pairs),1/3 (18 pairs)}, and across all216vector pairs between distinct bases
the spectrum is{0 (132), 1/3 (72), 1 (12)}. In particular,zeropairs attain|⟨u,v⟩|2 =
1/6: no fourth basis unbiased to{I6,F6}and any third basis inV24 exists within the
24th-root cyclotomic sector.
Proof. Part (a) follows directly by squaring Theorems 1 and 2 sinceµR
2 (d) = µR(d)2 and
1
d−1 −1
d = 1
d(d−1) , 4
4d−3 −1
d = 3
d(4d−3) .
For (b), note that the(j,k)-entry of
√
6F6 is ωjk
6 = ζ4jk
24 . Unbiasedness ofv = 1√
6 (ζej
24)5
j=0
(e0 = 0) to F6 is equivalent inZ[ζ24]to |Sk|2 = 6for k = 0,..., 5, whereSk := ∑5
j=0 ζej −4jk
24 .
Splitting Sk = Ek + Ok into even (j∈ {0,2,4}) and odd (j∈ {1,3,5}) indices satisfies
Sk+3 =Ek −Ok fork= 0,1,2becauseζ −12j
24 = (−1)j. By the parallelogram law inZ[ζ24],
|Sk|2 +|Sk+3|2 = 2(|Ek|2 +|Ok|2) = 12 =⇒ |Ek|2 +|Ok|2 = 6 (k= 0,1,2).(22)
This exact necessary invariant permits a lossless meet-in-the-middle partition of all245 =
7,962,624phase tuples: indexing all242 = 576even pairs( e2,e4)by( |E0|2,|E1|2,|E2|2) ∈Z [ζ24]3
and matching against all243 = 13,824odd triples( e1,e3,e5)with complementary norm triple
(6 −|Ek|2)2
k=0, then checking|Ek±Ok|2 = 6exactly in Z[x]/(x8 −x4 + 1). The exhaustive search
(Certificate cert16) returns exactly12rays, partitions into two blocks of3 + 3rays generating
2 ×2 = 4orthonormal bases, and certifies every exact squared inner product in{0,1/3}for
distinct rays.
5 Formal Verification Architecture and Scope
To prevent ambiguity between machine-checked proof scope and computational certification, our
artifact separates two complementary verification layers:
8

--- Page 9 ---
Table 1: Summary of exact minimax coherence bounds, witnesses, and arithmetic regimes verified
across Certificatescert01–cert15.
dClass Lower boundµ R(d)Exact / upper witness Status Excessµ R
2 −1
d
3odd2/3I 3 −2
3 J3 Exact tight (Thm. 2)1/9
5odd2/
√
17(strict) 1
11 circ(3,6,2,−6,6)∈(2/
√
17,6/11]>3/85
6 2 mod 4 1/
√
5 1√
5 C6 (Paleyp= 5) Exact tight (Thm. 1)1/30
7odd2/5(strict) 1
2437 circ(...)∈(2/5,1188/2437]>3/175
10 2 mod 4 1/3 1
3 C10 ∈O(10,Q)Exact rational tight1/90
14 2 mod 4 1/
√
13 1√
13 C14 (Paleyp= 13) Exact tight1/182
18 2 mod 4 1/
√
17 1√
17 C18 (Paleyp= 17) Exact tight1/306
22 2 mod 4 1/
√
21(strict) Belevitch (21̸=a 2 +b2) Strict gap>1/
√
21>1/462
26 2 mod 4 1/5 1
5 C26 ∈O(26,Q)Exact rational tight1/650
30 2 mod 4 1/
√
29 1√
29 C30 (Paleyp= 29) Exact tight1/870
34 2 mod 4 1/
√
33(strict) Belevitch (33̸=a 2 +b2) Strict gap>1/
√
33>1/1122
• Layer 1 — Constructive Lean 4.36.0 Kernel(lean/OrthogonalMinimaxCoherenc
e.lean): Twenty theorems compiled withlean-DwarningAsError=true , zero external
dependencies, zero sorry, and zero Classical.choice (audited via #print axioms).
Layer 1 machine-checks the complete scalar-algebraic, parity, divisibility, and exact-
witness arithmetic kernel: polynomial identity(4) and non-negativity (thm01–thm03), the
Hadamard three-row sign-parity obstruction andd= 4k+ 2coherence inequality (thm04–
thm07), the odd-dimension secant identity(13) and dominance over quadratic/Welch
bounds (thm08–thm10), the uniqued= 3spectral-divisibility theorem s2 = 4d−3 ∧s|
d⇒d = 3( thm11), exact rational orthogonality and entry inequalities forU3,U5,U7
(thm12–thm14), infinite Belevitch mod-9and mod-49sum-of-two-squares obstructions
(thm15–thm18), rational conference squares (thm19), and MUB coherence excesses (thm20).
The finite-sum matrix/vector aggregation steps (such as summing(4) over P,N, applying
matrix orthogonality toN0 ×CZ, and taking eigenvalues/trace ofS) are proved in full
mathematical detail in Sections 2–3.
• Layer 2 — Zero-Float Exact Python Verifier(verification/verify_orthog
onal_coherence.py ): An AST-audited pure standard-library verifier using strictly
int and fractions.Fraction (zero floating-point operations, zero numeric division
or exponentiation, zerolimit_denominator ), emitting16SHA-256 certificates under
certificates/MANIFEST.json and validated by56adversarial pytest checks. Layer 2
independently verifies Paley conference matrices ford∈{ 6,10,14,18,26,30,38,42,54,62}
(including GF(9)and GF(25)constructions), the complete Belevitch classification for
6 ≤d≤ 102, exact matrix orthogonality forU3,U5,U7 (together withdet(U3) = −1and
det(U5) = det(U7) = +1in the adversarial test suite), the spectral-divisibility scan for all
odd d≤ 1001in Certificate cert13 (extended tod≤ 5001in tests/test_adversarial
.py), and the exhaustive245-vectorZ[ζ24]ring search of Theorem 3(b).
Remark1 (OpenDirections).TwosharpopenquestionsremaindirectlyhighlightedbyTheorems1
and 2: (i) determining the exact value ofµR(5) ∈(2/
√
17, 6/11](and general odd µR(2k+ 1)
for k≥ 2), where our spectral-divisibility obstruction rules out2/
√
4d−3 uniformly; and
(ii) quantifying the Belevitch coherence gapµR(d) −1/
√
d−1> 0at the first obstructed order
d= 22, where conference-matrix rigidity proves no zero-diagonal±1/
√
21minimizer can exist.
9

--- Page 10 ---
References
[1] V. Belevitch,Theory of2 n-terminal networks with applications to conference telephony,
Electr. Commun.27(1950), 231–244.
[2] V. Belevitch,Conference networks and Hadamard matrices, Ann. Soc. Sci. Bruxelles Sér. I
82(1968), 13–32.
[3] I. Bengtsson, W. Bruzda, Å. Ericsson, J.-Å. Larsson, W. Tadej, and K. Życzkowski,Mutually
unbiased bases and Hadamard matrices of order six, J. Math. Phys.48(2007), 052106.
[4] P. O. Boykin, M. Sitharam, M. Tarifi, and P. Wocjan,Real mutually unbiased bases,
arXiv:quant-ph/0502024 (2005).
[5] S. Brierley and S. Weigert,Maximal sets of mutually unbiased quantum states in dimension
6, Phys. Rev. A78(2008), 042312.
[6] S. Brierley and S. Weigert,Constructing mutually unbiased bases in dimension six, Phys.
Rev. A79(2009), 052316.
[7] P. Delsarte, J. M. Goethals, and J. J. Seidel,Orthogonal matrices with zero diagonal. II,
Canad. J. Math.23(1971), 816–832.
[8] T. Durt, B.-G. Englert, I. Bengtsson, and K. Życzkowski,On mutually unbiased bases, Int.
J. Quantum Inform.8(2010), 535–640.
[9] J. M. Goethals and J. J. Seidel,Orthogonal matrices with zero diagonal, Canad. J. Math.
19(1967), 1001–1010.
[10] P. Jaming, M. Matolcsi, P. Móra, F. Szöllősi, and M. Weiner,A generalized Pauli problem
and an infinite family of MUB-triplets in dimension 6, J. Phys. A: Math. Theor.42(2009),
245305.
[11] R. E. A. C. Paley,On orthogonal matrices, J. Math. Phys.12(1933), 311–320.
[12] J. J. Seidel,A survey of two-graphs, inColloquio Internazionale sulle Teorie Combinatorie
(Roma, 1973), Tomo I, Accad. Naz. Lincei (1976), 481–511.
[13] L. R. Welch,Lower bounds on the maximum cross correlation of signals, IEEE Trans.
Inform. Theory20(1974), 397–399.
[14] W. K. Wootters and B. D. Fields,Optimal state-determination by mutually unbiased
measurements, Ann. Physics191(1989), 363–381.
10
