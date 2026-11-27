# Sharp Non-Asymptotic Quantum Query Lower Bounds for k-Sum and Element Distinctness via Exact Tensor-Projector Adversary Duals and Stirling Spectral Multiplicities

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-3SVAT6TJ6V9NAVH6` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/quantum-query-exact-adversary-and-collision-sharp-bounds (`v1.0.0`)  
**Canonical PDF SHA-256:** `d3ed06864b5dc72a33ad447665ddf3d95444cc3a0cca590ff83a44e6392c3b97`

## Abstract

We establish explicit, zero-O(.) non-asymptotic quantum query lower bounds for k-Sum over any finite abelian group G of order q and for Element Distinctness, backed by constructive Lean 4.36.0 formalization and zero-float rational LDL^T matrix certificates. First, for every k >= 1 and single-subset tensor projector H_S(alpha) = sum_{T subseteq S} alpha_{|T|} E_T (alpha_0 = 1, alpha_k = 0), we prove the exact minimax query-difference identity ||H_S(alpha) o Delta_i||_op = ((q-1)/q) max_j |alpha_j - alpha_{j+1}| >= (q-1)/(qk), establish that the witness-hyperplane Gram operator H_S P_{E_S} H_S^T = (H_S Pi_{E_S})(H_S Pi_{E_S})^T (for H_S = I_{q^k} - E_1^{otimes k}, P_{E_S} = Pi_{E_S} Pi_{E_S}^T) has exact nonzero eigenvalues m/q (1 <= m <= min(k, q)) with Stirling multiplicities S_2(k, m) prod_{j=1}^{m-1}(q - j) (yielding ||H_S P_{E_S} H_S^T||_op = min(k, q)/q identically for both k-Sum and Element Distinctness, equaling k/q whenever q >= k), and prove that (H_S(lin) o Delta_i) Pi_{E_S} is an exact scaled isometry of squared norm (q-1)/(q^2 k^2) while ||(H_S o Delta_i) Pi_{E_S}||_op^2 <= (q-1)/q^2 with exact trace (q-1)^k/q^2. Second, combining the truncated-ramp block adversary Gamma_S = (H_S otimes B_S^{(d)}) (Pi_{E_S} otimes I) with Bonferroni unique-solution counting (q >= (4k+1) C(n,k), rho = C(n,k)/q) cancels q completely and yields an explicit non-asymptotic adversary lower bound with certified constants c_2 > 0.428 (n^{2/3}), c_3 > 0.341 (n^{3/4}), and c_4 > 0.299 (n^{4/5}). Third, for every total Boolean function f : G^n -> {0,1}, we give a self-contained proof of the positive-weight certificate barrier ADV^+(f) <= sqrt(C_0(f) C_1(f)) <= sqrt(C_1(f) n), prove exact tightness ADV^+(TH_k^n) = sqrt(k(n-k+1)) on k-Threshold, and certify exact finite-n crossovers where the negative-weight bound strictly pierces sqrt(kn). Twenty constructive Lean 4.36.0 theorems (0 sorry, 0 Classical.choice), 16 zero-float Python certificates, and 56 adversarial tests accompany the manuscript.

## Full Extracted Text

--- Page 1 ---
Sharp Non-Asymptotic Quantum Query Lower
Bounds fork-Sum
and Element Distinctness via Exact Tensor-Projector
Adversary Duals
and Stirling Spectral Multiplicities
Lluis Eriksson∗
November 27, 2026
Abstract
Quantum query lower bounds fork-Sum (Ω(nk/(k+1))) and Element Distinctness (Ω(n2/3))
are landmark separations beyond the positive-weight adversary barrierADV+ ≤O (√n),
originally proved via polynomial methods [1, 4] and negative-weight adversary duals [6],
and recently revisited via elementary state-difference arguments [5]. Yet standard proofs
suppress explicit leading constants inside asymptoticO(·)notation and rarely determine
the finite dimension n∗ at which negative-weight bounds overtake the positive-weight
barrier. We establish three exact, zero-O(·)structural theorems backed by constructive
Lean 4.36.0 proofs and zero-float rationalLDLT certificates. First, for every k≥ 1and
finite abelian group G of order q≥ 2, we prove that the single-subset tensor projector
HS(α) = ∑
T⊆S α|T|ET (α0 = 1, αk = 0) satisfies the exact minimax query-difference
law ∥HS(α) ◦∆i∥op = q−1
q max0≤j≤k−1 |αj −αj+1|≥ q−1
qk (uniquely attained by the linear
ramp αj = 1 −j/k), while the binary cutoffHS = Iqk −E⊗k
1 restricted via column inclu-
sionΠ ES (PES := ΠES ΠT
ES ) to the solution hyperplaneES = {y∈G k : ∑
j∈S yj = 0}
(and identically for Element Distinctness y1 = y2 at k = 2) yields a Gram operator
HSPES HT
S = (HSΠES )(HSΠES )T with exact nonzero eigenvaluesm/q (1 ≤m≤min (k,q))
andStirling multiplicities S2(k,m) ∏m−1
j=1 (q−j ), implying ∥HSPES HT
S ∥op = min(k,q)/q
identically (equalingk/q whenever q≥k ). Second, combining the truncated-ramp block
adversaryΓ S = ( HS ⊗B (d)
S )(ΠES ⊗I G[n]\S )with Bonferroni unique-solution counting
(q≥ (4k+ 1)
(n
k
)
, ρ=
(n
k
)
/q) cancelsq completely and delivers an explicit non-asymptotic
bound ADV±≥(1−ρ−√kρ)
[
(1−ρ)
((d+k−2
k−1
)
/
(n
k
)
+ k(n−k)
nd2
)]−1/2
valid for alln≥k +1and
1 ≤d≤n−k , certifying explicit constantsc2 >0.428( n2/3, large-q limit0 .514), c3 >0.341
(n3/4, limit0 .408), and c4 > 0.299( n4/5, limit0 .357). Third, for every total Boolean function f : G^n -> {0,1}, we give a self-contained
4-line proof of the positive-weight certificate barrierADV+(f) ≤
√
C0(f)C1(f)≤
√
C1(f)n,
prove exact tightnessADV+(THn
k) =
√
k(n−k+ 1) on k-Threshold, and certify exact finite
crossovers (under four-digit rational square-root bounds) where Theorem 2 strictly pierces√
kn: n∗= 1,290( k = 2), n∗= 668( k = 3), and n∗= 571( k = 4). Twenty constructive
Lean 4.36.0 theorems (0sorry,0 Classical.choice),16zero-float Python certificates, and
56adversarial tests accompany the paper.
∗Independent Researcher. Research, formal verification in Lean 4.36.0, zero-float exact rationalLDLT and
Stirling certificate verification, adversarial testing, and manuscript typesetting were conducted with transparent
assistance from Google Antigravity. Code is released under MIT; manuscript and figures under CC-BY-4.0. Repos-
itory: https://github.com/lluiseriksson/quantum-query-exact-adversary-and-collision-sharp-bounds
(v1.0.0).
1
AIRR:ARR-2026-3SVAT6TJ6V9NAVH6 v1  [Mathematical physics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
1 Introduction
Given oracle access to an inputx= (x1,...,x n) ∈Gn over a finite abelian groupG of order
q = |G|, thek-Sum problem(k-SUMn,G, k≥ 2) asks whether there exists ak-element subset
S⊆ [n]satisfying ∑
j∈S xj = 0, whileElement Distinctness( EDn,G) asks whether there exist
distinct indicesi̸= j with xi −xj = 0. In the bounded-error quantum query model (two-sided
error ε∈ [0,1/2)), the optimal query complexity isΘ(n2/3)for Element Distinctness [3, 1, 4]
andΘ( nk/(k+1))for k-Sum over sufficiently large groups [6, 5], sharply surpassing theΘ(√n)
ceiling imposed on all positive-weight adversary bounds by the certificate-size barrier [2, 9].
By the generalized (negative-weight) adversary theorem of Høyer, Lee, and Špalek [7]
(proven tight up to constants by Reichardt [8]), for any Boolean functionf : D→{ 0,1}
(D=X 0 ⊔X1 ⊆Gn) and any nonzero real matrixΓ∈RX0×X1 ,
Qε(f)≥ 1−2
√
ε(1−ε)
2 ADV±(f),ADV ±(f) := sup
Γ̸=0
∥Γ∥op
maxi∈[n] ∥Γ◦∆ i∥op
,(1)
where(∆ i)x,y =1[ xi ̸= yi]is the i-th coordinate-difference indicator and◦denotes the Hadamard
product. Motivated by Belovs–Špalek’s adversary construction [6] and the recent elementary
state-difference proof of Ambainis and Kokainis [5], we isolate the exact finite-dimensional
spectral algebra behind (1) and obtain three completely explicit, zero-O(·)results:
1. Exact Tensor-Projector Minimax Law and Stirling Spectral Multiplicities
(Theorem 1).We determine the exact query-difference operator norm of any Hamming-
weight tensor projectorHS(α)on Gk, prove thatHSPES HT
S (PES := ΠES ΠT
ES ) splits into
rank-1shift-equivalence classes with exact nonzero eigenvaluesm/q (1 ≤m≤min (k,q))
and Stirling multiplicitiesS2(k,m) ∏m−1
j=1 (q−j )(equally valid for k-Sum and Element
Distinctness), and prove that(HS(lin)◦∆ i)ΠES is an exact scaled isometry.
2. Zero-O(·)Non-AsymptoticΩ( nk/(k+1))Lower Bounds with Exactq-Cancellation
(Theorem 2).Combining the truncated-ramp block adversaryΓS = (HS ⊗B(d)
S )(ΠES ⊗
IG[n]\S )withexactBonferroniunique-solutioncounting( q≥ (4k+1)
(n
k
)
)cancels qidentically
between numerator and denominator, yielding closed-form rational lower bounds valid for
every finiten≥k+ 1and explicit leading constantsc k.
3. Positive-Weight Certificate Barrier, k-Threshold Tightness, and Certified
Crossovers (Theorem 3).We give a self-contained proof ofADV+(f) ≤
√
C0(f)C1(f)≤√
C1(f)n, certify exact equality onk-Threshold THn
k, and pinpoint the exact finite dimen-
sions n∗where Theorem 2 strictly pierces
√
kn (n∗= 1,290for k= 2,668for k= 3,571
fork= 4).
2 Exact Tensor-Projector Spectrum and Stirling Multiplicity
Law
Let G be any finite abelian group of orderq≥ 2. On CG (identified with Cq), define the
orthogonal projectorsE0 := 1
q Jq (onto C1q) andE1 := Iq −E0 (onto1 ⊥
q ), and let∆ := Jq −Iq
be the single-coordinate difference matrix. For anyk-element subsetS⊆ [n]and any subset
T⊆S , write ET :=
(⨂
j∈T E1
)
⊗
(⨂
j∈S\T E0
)
on CGS
, so ∑
T⊆S ET = Iqk. Given a weight
vector α= (α0,...,α k) ∈R k+1, defineHS(α) := ∑
T⊆S α|T|ET , and denote byHS := Iqk −E⊗k
1
the binary cutoff (α0 = ··· = αk−1 = 1, αk = 0) and byHS(lin)the linear ramp (αj = 1 −j/k).
LetΠ ES ∈{0,1}qk×qk−1
denote the column inclusion isometry for the solution hyperplane
ES := {y∈G S : ∑
j∈S yj = 0}(size |ES|= qk−1), or atk = 2for the Element Distinctness
2

--- Page 3 ---
hyperplane EED
S := {y∈G 2 : y1 −y2 = 0 }, and let PES := Π ES ΠT
ES ∈{0,1}qk×qk
be the
corresponding diagonal orthogonal projector ontoCES .
Theorem 1(Tensor-Projector Minimax Law, Stirling Spectrum, and Hyperplane Isometry).
For every finite abelian groupGof orderq≥2and everyk≥1:
(a) Single-coordinate cancellation and minimax ramp law:OnCq,( E0 + E1) ◦∆ = 0and
E0 ◦∆ = q−1
q E0 −1
q E1. Hence for everyα∈R k+1 withα 0 = 1,α k = 0and everyi∈S,
∥HS(α)◦∆ i∥op = q−1
q max
0≤j≤k−1
|αj −αj+1| ≥q−1
qk ,(2)
with equality if and only ifαj = 1−j/kis the linear rampH S(lin).
(b) Exact witness annihilation and Stirling spectral multiplicities:For both k-Sum (ES)
and Element Distinctness (EED
S , k = 2), HS|1ES ⟩= 1
q |1Gk⟩identically. Moreover, the
qk ×qk Gram operatorHSPES HT
S = (HSΠES )(HSΠES )T has rankqk−1 and exact nonzero
eigenvaluesm/q(1≤m≤min(k,q)) with multiplicities
mult
(m
q
)
=S 2(k,m)
m−1∏
j=1
(q−j)
(
1≤m≤min(k,q)
)
,(3)
where S2(k,m)denotes the Stirling number of the second kind (and∏m−1
j=1 (q−j ) = 0for
m>q). In particular,
min(k,q)∑
m=1
mult
(m
q
)
=qk−1,tr
(
HSPES HT
S
)
= qk −(q−1) k
q ,∥H SPES HT
S ∥op = min(k,q)
q
(4)
(equalingk/qwheneverq≥k).
(c) Exact hyperplane query-difference Gram identities:For every i∈S , the linear ramp
satisfies the exact scaled-isometry identity
(
(HS(lin)◦∆ i)ΠES
)T (
(HS(lin)◦∆ i)ΠES
)
= q−1
q2k2 Iqk−1 ,(5)
while the binary cutoffHS = Iqk −E⊗k
1 gives Gbin
i := ((HS ◦∆i)ΠES )T ((HS ◦∆i)ΠES )
with exact tracetr(Gbin
i ) = (q−1)k
q2 and exact operator-norm bound
(HS ◦∆ i)ΠES
2
op ≤ q−1
q2 .(6)
Proof. Proof of(a).Since E0 + E1 = Iq and∆has zero diagonal,( E0 + E1) ◦∆ = 0, while
E0 ◦∆ = 1
q (Jq −Iq) = E0 −1
q (E0 + E1) = q−1
q E0 −1
q E1 (Lean thm01–thm02). Pairing each
R⊆S\{i}withR∪{i}inH S(α)yields
HS(α)◦∆ i =
∑
R⊆S\{i}
(α|R|−α|R|+1)
(
(E0 ◦∆) i ⊗ER
)
.
Because the projectors ER are mutually orthogonal and∥E0 ◦∆∥op = max(q−1
q ,1
q ) = q−1
q ,
the exact norm equality in(2) follows; telescoping ∑k−1
j=0 (αj −αj+1) = α0 −αk = 1gives
maxj |αj −αj+1|≥1/kwith equality iffα j −αj+1 = 1/k(Leanthm03–thm04).
Proof of(b).Let {χs : s∈ ˆGk}be the orthonormal Fourier character basis ofCGk
(since
G is finite abelian, ˆG ∼= G). On the subgroup hyperplane ES = {y∈G k : ∑k
j=1 yj = 0 },
3

--- Page 4 ---
Figure 1:Exact Stirling spectral multiplicities and two-part cutoff trade-off.(a)
Normalized eigenvalue multiplicitiesmult(m/q)/qk−1 = S2(k,m) ∏m−1
j=1 (q−j)/qk−1 of HSPES HT
S
at q= 5for k= 3(1 ,12,12) andk= 4(1 ,28,72,24) (Theorem 1(b), Certificatecert04). (b)
Two-part query-difference trade-off atn = 5,000, k = 2: balancing Part 1 (
(d
1
)
/
(n
2
)
) against
Part 2 (2(n−2)
nd2 ) isolates the sharp minimum atd∗= 368≍n 2/3.
the restriction χs|ES equals χs′|ES if and only ifs′−s = a1k for some a∈ ˆG. Thus PES =
ΠES ΠT
ES (as an operator onCGk
) is block-diagonal across theqk−1 shift-equivalence classes
[s] = {s+ a1k : a∈ ˆG}, acting on each class as1
q |u[s]⟩⟨u[s]|where |u[s]⟩= ∑
a∈ˆG |χs+a1k⟩.
In Fourier space,HS = Iqk −E⊗k
1 is the diagonal projector retaining precisely thoses∈ ˆGk
with at least one zero coordinate. Inside the shift class[s], an elements+ a1k has a zero
coordinate iff −a∈{s 1,...,s k}; hence the number of surviving basis states in[s]is exactly
m(s) := |{s1,...,s k}|∈{ 1,...,min (k,q)}. Therefore HS|u[s]⟩has squared normm(s), making
HSPES HT
S = ∑
[s]
1
q (HS|u[s]⟩)(HS|u[s]⟩)∗an orthogonal sum of rank-1operators with eigenvalues
m(s)/q. The number of tupless∈ ˆGk with m distinct coordinates isS2(k,m) ∏m−1
j=0 (q−j ),
and dividing by the shift-class sizeq yields (3). For EED
S = {y1 −y2 = 0}, the shift classes
are {(s1 + a,s2 −a)}, which have the identical countm(s) = |{s1,−s2}| ∈ {1,2}, so the
spectrum is identical. In particular, the uniquem = 1class[0]corresponds to |1ES ⟩, giving
HS|1ES ⟩= 1
q |1Gk⟩.
Proof of(c).Fixing i∈S , every y∈E S is uniquely determined by yS\{i} ∈G k−1 via
yi = −∑
r∈S\{i}yr (or y1 = y2 for ED). ForHS(lin),( HS(lin) ◦∆i) = 1
k (E0 ◦∆)i ⊗IGS\{i}. For
any y,y′∈ES, the( y,y′)-entry of(( HS(lin) ◦∆i)ΠES )T ((HS(lin) ◦∆i)ΠES )vanishes whenever
yS\{i} ̸= y′
S\{i}, and fory = y′ equals 1
k2
∑
xi̸=yi
1
q2 = q−1
q2k2 , proving(5). For HS = Iqk −E⊗k
1 ,
(HS ◦∆ i) = (E0 ◦∆) i ⊗E⊗(S\{i})
1 , so
(HS ◦∆ i)ΠES
2
op ≤
(
(E0 ◦∆) i ⊗IGS\{i}
)
ΠES
2
op = q−1
q2 ,
since E⊗(S\{i})
1 is a contraction (and direct diagonal summation overy∈E S yields trace
q−1
q2 tr(E⊗(k−1)
1 ) = (q−1)k
q2 ; Leanthm05and Certificatecert06).
4

--- Page 5 ---
3 Explicit Zero-O(·)Non-AsymptoticΩ(n k/(k+1))Bounds
Let k≥ 2, n≥k + 1, andd∈{ 1,...,n−k} . For eachk-subset S⊆ [n], define the truncated
linear-ramp operator on the complement[n]\S:
B(d)
S :=
∑
W⊆[n]\S
|W|<d
(
1− |W|
d
)
EW ,Γ S :=
(
HS ⊗B(d)
S
)˜ΠES ,(7)
where ˜ΠES := Π ES ⊗IG[n]\S restricts columns to {y∈G n : ∑
j∈S yj = 0 }(or yu = yv for
EDn,G at k = 2). Let X0 ⊆G n be the set of zero-instances (nok-subset sums to0, resp. all
coordinates distinct), and letXuniq
1 ⊆Gn be the set of unique-solution one-instances (precisely
one k-subset S(y)satisfies the equation). Since every y∈X uniq
1 belongs to a uniqueES(y) ,
the horizontal block concatenationΓ := [ΓS]|S|=k restricts cleanly to a valid adversary matrix
Γres := ΠX0 ΓΠXuniq
1
∈R X0×Xuniq
1 .
Theorem 2(Zero-O(·)Non-Asymptotic Quantum Query Lower Bound fork-Sum and Element
Distinctness).Let k≥ 2, n≥k + 1, d∈{ 1,...,n−k} , and letG be any finite abelian group of
order q≥ (4k+ 1)
(n
k
)
, settingρ:=
(n
k
)
/q∈
(
0, 1
4k+1
]
. Then for bothk-SUMn,G (all k≥ 2) and
EDn,G (k= 2):
(a) Exact two-part query-difference upper bound:For every coordinatei∈[n],
∥Γres ◦∆ i∥2
op ≤ ∥Γ◦∆i∥2
op ≤ q−1
q2
(
d+k−2
k−1
)
+ k
q
(
n−1
k
)(q−1
q
)2 1
d2 .(8)
(b) Exact Bonferroni–Cauchy–Schwarz norm lower bound:
∥Γres∥op ≥
√(n
k
)
q
1−ρ− √kρ√1−ρ >0.(9)
(c) Exact q-cancelled non-asymptotic adversary bound:Combining (8) and (9) cancels q
identically (since q−1
q <1and
(n−1
k
)
/
(n
k
)
= n−k
n ), giving
ADV± ≥ 1−ρ− √kρ√(1−ρ)
((d+k−2
k−1
)
(n
k
) + k(n−k)
nd2
),(10)
and henceQε ≥1−2
√
ε(1−ε)
2 ADV±. Choosing d=
⌈(2
k−1
)1/(k+1)nk/(k+1)⌉
gives ADV±≥
(ck −o(1))nk/(k+1) with certified constants (Certificatecert14): c2 >0.428at ρ= 1/79
(large-q limit2 −1/6/
√
3≈ 0.514), c3 > 0.341at ρ = 1/119(limit1 /
√
6≈ 0.408), and
c4 >0.299atρ= 1/159(limit0.357).
Proof. Proof of(a).SinceΠ X0 andΠ Xuniq
1
areorthogonalprojections, ∥Γres◦∆i∥2
op ≤∥Γ◦∆i∥2
op =
∑
|S|=k(ΓS ◦∆i)(ΓS ◦∆i)T 
op. Split the sum overS into Part 1 (i∈S ) and Part 2 (i /∈S).
For Part 1 (i∈S),B (d)
S does not touch coordinatei, so
ΓS ◦∆ i =
(
(HS ◦∆ i)⊗B (d)
S
)˜ΠES .
By Theorem 1(c),∥(HS ◦∆i)ΠES ∥2
op ≤q−1
q2 , and becauseHS ◦∆i = (E0 ◦∆)i ⊗E⊗(S\{i})
1 acts
strictly on the weight-(k−1)subspace E⊗(S\{i})
1 outside i, the row-space of(ΓS ◦∆i)(ΓS ◦∆i)T
5

--- Page 6 ---
is supported strictly on Fourier subspacesET whose projectionR:= T\{i} satisfies S\{i}⊆R
and |R\(S\{i})|≤d− 1(hence |R|≤d + k−2). Fixing anyR⊆ [n] \{i}of sizer≤d + k−2,
at most
(r
k−1
)
≤
(d+k−2
k−1
)
subsets S∋i satisfy S\{i}⊆R , and each contributes operator norm
at most q−1
q2 (since0 ≤1 −|W|/d≤ 1). Because distinct subspacesER ⊗C G(i)
are pairwise
orthogonal, the Part 1 sum has operator norm at mostq−1
q2
(d+k−2
k−1
)
.
For Part 2 (i /∈S), HS does not touch coordinatei, soΓ S ◦∆i = (HSΠES ) ⊗(B(d)
S ◦∆i).
By Theorem 1(a),∥B(d)
S ◦∆i∥op = q−1
qd , and sinceq≥ (4k+ 1)
(n
k
)
> k, Theorem 1(b) gives
∥HSΠES ∥2
op = ∥HSPES HT
S ∥op = k
q . Summing the operator norms over all
(n−1
k
)
subsets S̸∋i
via the triangle inequality gives the Part 2 termk
q
(n−1
k
)(q−1
q
)2 1
d2 , proving (8).
Proof of(b).By the union bound, |Gn \X0|≤
(n
k
)
qn−1 = ρqn, so|X0|≥ (1 −ρ)qn. For any
two distinct k-subsets S̸= S′, the defining linear equations∑
j∈S yj = 0and ∑
j∈S′yj = 0
(and likewiseyu = yv vs. yu′ = yv′ for {u,v}̸ = {u′,v′}) are linearly independent overG since
S′\S̸ = ∅; thus|ES ∩ES′|= qn−2 identically. By Bonferroni’s union bound over the
(n
k
)
−1
subsetsS ′̸=S,
|Xuniq
1 |=
∑
|S|=k
|Xuniq
1 ∩ES| ≥
(
n
k
)(
qn−1 −
((n
k
)
−1
)
qn−2
)
≥(1−ρ)
(
n
k
)
qn−1 = (1−ρ)ρq n.
For everyy∈X uniq
1 with unique witnessS, because HT
S |1Gk⟩= |1Gk⟩and( B(d)
S )T |1Gn−k⟩=
|1Gn−k⟩(as α0 = β0 = 1and E1|1q⟩= 0), we obtain ⟨1Gn|Γ|y⟩= ⟨1Gn|HS ⊗B (d)
S |y⟩= 1.
Hence ⟨1Gn|Γ|1Xuniq
1
⟩= |Xuniq
1 |. Moreover, by Theorem 1(b) and ∥B(d)
S ∥op ≤1, ∥Γ∥2
op =
∑
|S|=k(HSPES HT
S ) ⊗(B(d)
S )2
op ≤
(n
k
)k
q = kρ. Writing1 X0 =1 Gn −1Gn\X0 and applying
Cauchy–Schwarz yields
∥Γres∥op ≥
⟨1X0 |Γ|1Xuniq
1
⟩
√
|X0||Xuniq
1 |
≥
|Xuniq
1 |−
√
|Gn \X0|∥Γ∥op
√
|Xuniq
1 |
√
|X0||Xuniq
1 |
≥
√|Xuniq
1 |
|X0| −
√
|Gn \X0|
|X0|
√
kρ≥
√
(1−ρ)ρ−ρ
√
k
1−ρ = √ρ1−ρ− √kρ√1−ρ .
Sinceρ≤ 1
4k+1 , Leanthm11proves(1−ρ) 2 >3kρ>kρ, ensuring1−ρ− √kρ>0.
Proof of(c).Dividing (9) by the square root of(8) cancels
√
1/q identically, and bounding
q−1
q <1with
(n−1
k
)
/
(n
k
)
= n−k
n yields (10). Setting d= xnk/(k+1) gives
(d+k−2
k−1
)
/
(n
k
)
+ k(n−k)
nd2 ∼
k
n2k/(k+1) (xk−1 + x−2), minimized uniquely atxopt = ( 2
k−1 )1/(k+1), yielding the certified constants
in Certificatecert14.
4 Positive-Weight Certificate Barrier,k-Threshold Tightness,
and Finite-nSeparation
Forf : D→{ 0,1}(D⊆G n), letC0(f)and C1(f)denote its0- and1-certificate complexities, and
let ADV+(f) := supΓ≥0,Γ̸=0 ∥Γ∥op/max i ∥Γ◦∆i∥op be the positive-weight adversary bound [2, 9].
Theorem 3(Positive-Weight Certificate Barrier, Exactk-Threshold Tightness, and Certified
Crossovers).
(a) Exact positive-weight certificate barrier:For every Boolean functionf:D→{0,1},
ADV+(f)≤
√
C0(f)C1(f)≤
√
C1(f)n.(11)
6

--- Page 7 ---
(b) Exact tightness onk-Threshold:For every1 ≤k≤n , the Boolean threshold function
THn
k(x) =1[ |x|≥k ]has C1(THn
k) = k, C0(THn
k) = n−k + 1, and its Hamming-1positive-
weight adversary on{|x|= k− 1}×{|y| = k}achieves exact equalityADV+(THn
k) =√
k(n−k+ 1) =
√
C0(THn
k)C1(THn
k).
(c) Certified finite-nseparation beyond
√
kn:Since C1(k-SUMn,G) = k (and C1(EDn,G) = 2),
ADV+ ≤
√
kn holds unconditionally, whereas Theorem 2 strictly pierces
√
kn at the
certified zero-float crossovers (Certificatecert13, under four-digit rational square-root
bounds
√
2/79<0.1592,
√
3/119<0.1588,
√
4/159<0.1587; Leanthm17–thm19):
•k = 2(2-Sum / Element Distinctness, ρ= 1/79): n∗= 1,290( d∗= 149, ADV±≥
50.800 > 50.794 =
√
2n∗); at n = 5 ,000, ADV± ≥ 125.23 > 100.00 =
√
2n
(Leanthm17).
•k = 3(3-Sum, ρ= 1/119): n∗= 668( d∗= 131, ADV±≥44.777 >44.766 =
√
3n∗);
atn= 1,000,ADV ±≥60.54>54.77 =
√
3n(Leanthm18).
•k = 4(4-Sum, ρ= 1/159): n∗= 571( d∗= 147, ADV±≥47.801 >47.791 =
√
4n∗);
atn= 1,000,ADV ±≥74.83>63.25 =
√
4n(Leanthm19).
Proof. Proof of(a).LetΓ ∈R X0×X1
≥0 be any nonzero nonnegative matrix, and letu∈R X0
≥0,
v∈R X1
≥0 be unit nonnegative principal singular vectors (existing by Perron–Frobenius on
ΓT Γ), so ∥Γ∥op = uT Γv. For each x∈X 0 choose a0-certificate C0(x) ⊆[n]with |C0(x)|≤
C0(f), and for eachy∈X 1 choose a1-certificate C1(y) ⊆[n]with |C1(y)|≤C 1(f). Because
f(x) = 0 ̸= 1 = f(y), x and y must disagree on at least one coordinatei∈C 0(x) ∩C1(y), so
Γxy ≤∑
i∈C0(x)∩C1(y)(Γ ◦∆i)xy. Defining u(i)
x := ux1[i∈C 0(x)]and v(i)
y := vy1[i∈C 1(y)]and
applying Cauchy–Schwarz gives
∥Γ∥op ≤
n∑
i=1
(u(i))T (Γ◦∆ i)v(i) ≤
(
max
i∈[n]
∥Γ◦∆ i∥op
) n∑
i=1
∥u(i)∥2∥v(i)∥2
≤
(
max
i∈[n]
∥Γ◦∆ i∥op
)
√
n∑
i=1
∥u(i)∥2
2
√
n∑
i=1
∥v(i)∥2
2 ≤
(
max
i∈[n]
∥Γ◦∆ i∥op
)√
C0(f)C1(f),
since ∑n
i=1 ∥u(i)∥2
2 = ∑
x |C0(x)|u2
x ≤C0(f)∥u∥2
2 =C0(f)and likewise forv.
Proof of(b)and(c).On THn
k, the Hamming-1bipartite adjacency matrixB between X0 =
{|x|= k− 1}and X1 = {|y| = k}is biregular with degrees d0 = n−k + 1and d1 = k,
so ∥B∥op =
√
k(n−k+ 1) , while eachB◦ ∆i is a partial matching of norm1(Lean thm16,
Certificate cert09). Part (c) follows directly from cross-multiplied integer evaluation of(10) in
Leanthm17–thm19and Certificatescert10–cert13.
5 Formal Verification Architecture and Scope
Our verification artifact transparently delineates machine-checked algebraic identities from prose
spectral proofs and exact rational matrix certificates:
• Layer 1 — Constructive Lean 4.36.0 Kernel(lean/QuantumQueryAdversaryKSum.
lean): Twenty theorems compiled withlean-DwarningAsError=true, zero external depen-
dencies, zerosorry, zerogrind, zeroClassical.choice, and no custom axioms beyond
standard constructivepropext/Quot.sound (audited via#print axioms). Layer 1 formal-
izes the single-coordinate Hadamard cancellation, ramp minimax bounds, and hyperplane
Gram norm decomposition (thm01–thm05), Stirling multiplicity sum and trace identities
7

--- Page 8 ---
Table 1: Zero-float non-asymptotic Theorem 2 lower bounds vs. the positive-weight barrier
√
kn
(Certificatescert10–cert13).
ProblemnCutoffd ρ=
(n
k
)
/qADV ±
Thm 2(lb)ADV + ≤
√
knRatioADV ±/
√
kn
2-Sum /ED(k= 2)1,000 126 1/79 42.83 44.72 0.958
2-Sum /ED(k= 2)1,290 ∗ 149 1/7950.8050.791.0001
2-Sum /ED(k= 2)5,000 368 1/79125.23100.001.252
2-Sum /ED(k= 2)100,000 2,714 1/79922.68447.212.063
3-Sum (k= 3)668 ∗ 131 1/11944.7844.771.0002
3-Sum (k= 3)1,000 178 1/11960.5454.771.105
3-Sum (k= 3)10,000 1,000 1/119340.85173.211.968
4-Sum (k= 4)571 ∗ 147 1/15947.8047.791.0002
4-Sum (k= 4)1,000 232 1/15974.8363.251.183
4-Sum (k= 4)10,000 1,460 1/159473.19200.002.366
Figure 2:Certified non-asymptoticΩ( nk/(k+1))bounds vs. positive-weight barriers√
kn.(a) Explicit zero-O(·)Theorem 2 curves acrossn∈ [102,105]for k= 2,3,4plotted against
the dotted positive-weight ceilings
√
kn. (b) Separation ratioADV±
Thm 2/
√
kn piercing unity at
exact crossoversn∗= 1,290(k= 2),668(k= 3), and571(k= 4).
for k = 2,3,4( thm06–thm10), the Bonferroni positivity inequality3kCq <(q−C )2 for
q≥ (4k+ 1)C (thm11), exact binomial and cutoff balance identities (thm12–thm14), the
Cauchy–Schwarz kernel andk-Threshold biregularity (thm15–thm16), cross-multiplied
integer certifications of finite-n separation at n = 5 ,000( k = 2), n = 1 ,000( k = 3),
and n = 1,000( k = 4) (thm17–thm19), and exact error-amplification bounds (thm20).
The operator-norm shift-class spectral decomposition (Theorem 1(b)), general-n block-
adversary norm bounds (Theorem 2), and Perron–Frobenius barrier proof (Theorem 3(a))
are proved in full mathematical detail in Sections 2–4.
• Layer 2 — Zero-Float Python Verifier(verification/verify_quantum_query_
adversary.py): An AST-audited pure standard-library verifier using strictlyint and
Fraction (zero floats, zero numeric/, zero **, zero limit_denominator), emitting16
SHA-256 certificates incertificates/MANIFEST.json and validated by56adversarial
pytest checks in tests/test_adversarial.py. Layer 2 independently builds exact
rational matrices overQ for finite groups (including non-cyclicZ2 ×Z 2), certifies exact
operator-norm upper bounds via zero-float rationalLDLT Cholesky factorizations (cert02,
cert04–cert07), verifies exact Stirling power-trace momentstr(Gr), verifies exact k-
Threshold biregular matchings (cert09), and computes exact rational crossovers and
8

--- Page 9 ---
Figure 3:Exact k-Threshold tightness and explicit asymptotic constantsck.(a) Exact
attainment ADV+(THn
k)/√n =
√
k(n−k+ 1)/n across n = 6 ,12,20(Theorem 3(b)). (b)
Explicit leading constantsck in ADV±≥cknk/(k+1) for k = 2,..., 8at fixed ρ= 1/(40k− 1)
(Certificatecert14) and in the large-qlimitρ→0 +.
constants (cert10–cert15).
References
[1] S. Aaronson and Y. Shi,Quantum lower bounds for the collision and the element distinctness
problems, J. ACM51(2004), no. 4, 595–605.
[2] A. Ambainis,Quantum lower bounds by quantum arguments, J. Comput. System Sci.64
(2002), no. 4, 750–767.
[3] A. Ambainis,Quantum walk algorithm for element distinctness, SIAM J. Comput.37
(2007), no. 1, 210–239 (FOCS 2004).
[4] A. Ambainis,Polynomial degree and lower bounds in quantum complexity: Collision and
element distinctness with small range, Theory Comput.1(2005), 37–46.
[5] A. Ambainis and M. Kokainis,Elementary proofs of quantum lower bounds for element
distinctness andk-sum, preprint arXiv:2610.32693, October 2026.
[6] A. Belovs and R. Špalek,Adversary lower bound for the k-sum problem, inProc. 4th
Innovations in Theoretical Computer Science (ITCS 2013), ACM, pp. 323–328.
[7] P. Høyer, T. Lee, and R. Špalek,Negative weights make adversaries stronger, inProc. 39th
Annual ACM Symposium on Theory of Computing (STOC 2007), pp. 526–535.
[8] B. W. Reichardt,Reflections for quantum query algorithms, inProc. 22nd Annual ACM-
SIAM Symposium on Discrete Algorithms (SODA 2011), pp. 560–569.
[9] R. Špalek and M. Szegedy,All quantum adversary methods are equivalent, Theory Comput.
2(2006), 1–18 (ICALP 2005).
9
