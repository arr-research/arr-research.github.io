# Rank-Two Complex Refutation of the Bapat-Sunder Conjecture, Exact O(n^3) Cauchy-Binet Spectral Decomposition, and Low-Dimensional Rigidity

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0XEYC4V6488M596J` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/bapat-sunder-rank2-complex-refutation-and-low-dim-rigidity (`v1.0.0`)  
**Canonical PDF SHA-256:** `d4acddbe870ae9fb50a415d6f27ae0d72a4721577b5a3b988a20b4721a6384cd`

## Abstract

The Bapat-Sunder conjecture (1985) asked whether every Hermitian positive semidefinite (PSD) matrix A satisfies per(A) I_n >= A o adj_per(A) := F_A in the Loewner order, known to hold for n <= 3 and refuted in higher rank over C at n = 7 (Drury 2016) and over R in higher dimension. We resolve the sharp rank-2 Hermitian regime through three exact structural theorems backed by constructive Lean 4.36.0 proofs and zero-float Gaussian-integer certificates. First, we show that F_A 1 = per(A) 1 identically (reducing the conjecture to lambda_max(F_A|_{1^perp}) <= per(A)), prove exact diagonal congruence invariance F_{D A D^*} = |det D|^2 F_A on (CP^1)^n, and establish an exact O(n^3) Cauchy-Binet elementary-symmetric-polynomial Gram factorization F_A = sum_{k=0}^{n-1} k!(n-1-k)! (U_k U_k^* + V_k V_k^*) >= 0 for every rank-2 PSD matrix A = u u^* + v v^*. Second, we establish exact n = 2 rigidity via per(A)||w||^2 - w^* F_A w = |b|^2 |w_1 - w_2|^2 >= 0, prove the exact n = 3 shift-Laplacian identity per(A_0 + t I_3)I_3 - F_{A_0 + t I_3} = (per(A_0)I_3 - F_{A_0}) + t L(|A_0|^{o 2}) reducing 3x3 Hermitian PSD rigidity to rank <= 2 (where F_{A_0}|_{1^perp} collapses to rank 2), derive the exact Fourier spectrum lambda_m = n^2(m-1)!(n-1-m)! r^{2m} on n-th root circulants proving sup_{r>0} lambda_max(F|_{1^perp})/per = (n-1)^{-1/n} < 1 for all n >= 3 (showing symmetry breaking is necessary), and prove exact boundary saturation on real balanced direct sums J_{2m} + z z^T = 2(J_m oplus J_m). Third, we exhibit explicit rank-2 Gaussian-integer complex refutations at n = 8 (per = 573,191,776,350,720, gap +648,442,380,656,640, Rayleigh ratio 1.01166), an ultra-compact s = 1 counterexample A_9 = J_9 + z_9 z_9^* at n = 9 (per = 6,088,320, gap +11,572,992, ratio 1.00433), a general n = 9 witness (per = 44,125,969,104,000, gap +28,015,262,426,880, ratio 1.00765), and a high-margin n = 10 counterexample (per = 120,756,089,364,480, gap +1,147,005,482,158,080, ratio 1.08557, spectral ratio 1.09508), each directly machine-checked over Z[i] inside Lean 4.36.0 and independently cross-verified against direct Gray-code Ryser permanents.

## Full Extracted Text

--- Page 1 ---
Rank-Two Complex Refutation of the Bapat–Sunder
Conjecture,
ExactO(n 3)Cauchy–Binet Spectral Decomposition,
and Low-Dimensional Rigidity
Lluis Eriksson∗
November 27, 2026
Abstract
For ann×n Hermitian positive semidefinite (PSD) matrixA = (aij), let FA := A◦
adjper(A)denote the Hadamard product ofA with its permanent cofactor matrix,(FA)ij =
aij per(A(i|j)). The Bapat–Sunder conjecture (1985) asked whetherper(A)In −FA ⪰0
holds universally, known to hold forn≤ 3and refuted in higher rank overC at n= 7by
Drury (2016) and more recently overR in higher dimension. Here we resolve the sharp
rank-2Hermitian PSD regime via three exact structural theorems backed by constructive
Lean 4.36.0 proofs and zero-float Gaussian-integer certificates. First, we observe that
FA1= per(A)1identically—reducing Bapat–Sunder to λmax(FA|1⊥) ≤per (A)—prove exact
diagonal congruence invarianceFDAD∗ = |detD|2FA rendering FA/per (A)a projective
invariant on( CP1)n at rank2, and establish an exact O(n3)Cauchy–Binet elementary-
symmetric-polynomial Gram factorizationFA = ∑n−1
k=0 k!(n− 1 −k)!(UkU∗
k + VkV∗
k ) ⪰0
for every rank-2PSD matrix A = uu∗+ vv∗. Second, we prove exactn = 2rigidity via
per(A)∥w∥2
2 −w∗FAw = |a12|2|w1 −w2|2 ≥0, establish the exactn = 3shift-Laplacian
identityper(A0 +tI3)I3 −FA0+tI3 = (per(A0)I3 −FA0 )+ tL(|A0|◦2)reducing3 ×3Hermitian
rigidity to rank≤2(where FA0 |1⊥ collapses to the rank-2operator3(V0,⊥V∗
0,⊥+ U2,⊥U∗
2,⊥)),
derive the exact circulant Fourier spectrumλm = n2(m−1)!(n−1 −m)!r2m on n-th roots
of unity proving supr>0 λmax(F|1⊥)/per = (n− 1)−1/n < 1for all n≥ 3(establishing
that phase/radial symmetry breaking is necessary), and prove exact boundary saturation
(λmax/per = 1) on real balanced direct sumsA= J2m +zzT = 2(Jm ⊕Jm). Third, we exhibit
explicit rank-2Gaussian-integer complex refutations atn= 8(per(A8) = 573,191,776,350,720,
exact integer gap+648,442,380,656,640 >0, Rayleigh ratio1.01166), an ultra-compacts= 1
witness A9 = J9 + z9z∗
9 at n = 9( per(A9) = 6,088,320, gap+11 ,572,992 > 0, ratio
1.00433), a general n = 9witness (ratio1 .00765), and a high-margins = 2witness at
n = 10(ratio1 .08557, spectral ratio1 .09508), while showing that stripping imaginary
parts immediately restores≤1on every witness. All three refutations (n = 8,9,10) are
directly computed and verified inside the Lean 4.36.0 kernel (20constructive theorems,
0 sorry,0 Classical.choice) and independently cross-checked against direct Gray-code
Ryser permanents overZ[i]in16zero-float Python certificates and56adversarial tests.
1 Introduction
In 1985, Bapat and Sunder [1] proved that ifA and B are n×n Hermitian positive semidefinite
(PSD) matrices, thenper(A◦B ) ≤per (A) ∏n
i=1 bii holds forn≤ 3, and conjectured that the
∗Independent Researcher. Research, formal verification in Lean 4.36.0, zero-float exact Gaussian-integer certifi-
cate generation, adversarial testing, and manuscript typesetting were conducted with transparent assistance from
Google Antigravity. Code is released under MIT; manuscript and figures under CC-BY-4.0. Repository:https:
//github.com/lluiseriksson/bapat-sunder-rank2-complex-refutation-and-low-dim-rigidity(v1.0.0).
1
AIRR:ARR-2026-0XEYC4V6488M596J v1  [Mathematical physics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
stronger matrix inequality
per(A)In −FA ⪰0,(F A)ij :=a ij per
(
A(i|j)
)
(1)
holds for everyn×n Hermitian PSD matrixA, whereA(i|j)is the( n−1) ×(n−1)submatrix
obtained by deleting row i and column j (so FA = A◦adj per(A)). The inequality (1) is
intimately tied to permanent-on-top, Lieb’s permanental dominance conjecture, and Schur-
product inequalities [2, 5, 4]. While (1) was proved unconditionally forn= 2and n= 3[1, 5],
Drury [3] shattered the complex conjecture atn= 7using a higher-rank Hermitian PSD Gram
matrix, and Chalmers [6] recently disproved Drury’s real-symmetric conjecture via a rank-4,
32×32integer Gram matrix.
A natural sharp question remained open:what is the minimum rank at which complex phases
alone already break(1), and what exact algebraic structure governs the rank-2regime?Rank-1
PSD matricesA= uu∗are completely rigid:per(A) =n! ∏
i|ui|2 and FA = per(A)
n Jn ⪯per (A)In
identically for alln. Thusrank2( A= uu∗+ vv∗) is the absolute minimal nontrivial rank! In
this paper we analyze rank-2Hermitian PSD matrices in exact arithmetic and prove three main
results:
1. Row-Sum Reduction,CP1 Invariance, andO(n3)Cauchy–Binet Gram Decom-
position (Theorem 1).Because FA1= per(A)1identically for every A∈C n×n,
λ= per(A)is always a trivial eigenvalue ofFA—which causes naive numerical optimization
of λmax(FA)/per (A)to stall on the flat plateau1whenever λmax(FA|1⊥) ≤per (A). Re-
stricting to1 ⊥, exploiting exact diagonal congruence invarianceFDAD∗ = |detD|2FA, and
deriving the exactO(n3)Cauchy–Binet elementary-symmetric-polynomial (ESP) Gram
factorization of FA makes exact rank-2spectral analysis both tractable and zero-float
certifiable.
2. Low-Dimensional Rigidity,tI3 Shift-Laplacian Reduction, Circulant Barrier,
and Real Saturation (Theorem 2).We give an exactn= 2quadratic identity, prove
the exactn= 3shift-Laplacian identityper(A0 + tI3)I3 −FA0+tI3 = (per(A0)I3 −FA0 ) +
tL(|A0|◦2)(reducing3 ×3Hermitian rigidity to rank≤2, whereFA0 |1⊥ collapses to rank
2), derive the exact closed-form Fourier eigenvalues ofFA on n-th roots of unity proving an
unconditional AM-GM barriersupr>0 λmax(F|1⊥)/per = (n−1)−1/n <1for every n≥ 3
and r >0, and show exact boundary saturationλmax/per = 1on real balanced direct
sumsA=J 2m +zzT = 2(Jm ⊕Jm).
3. Exact Gaussian-Integer Rank-2Complex Refutations atn= 8,9,10(Theorem 3).
Breaking phase and radial symmetry via1⊥-projected optimization and rounding toZ[i]
produces four zero-float rank-2counterexamples atn= 8,n= 9(both an ultra-compact
s= 1matrix A9 = J9 + z9z∗
9 with per(A9) = 6,088,320and a general witness), andn= 10
(Rayleigh ratio1 .08557, spectral ratio1.09508). Every witness is machine-checked directly
inside Lean 4.36.0 and independently cross-verified by direct Gray-code Ryser permanents
overZ[i], while stripping imaginary parts immediately restoresw∗Fw≤per·∥w∥ 2
2.
2 Row-Sum Reduction,CP1 Invariance, and ExactO(n3)Cauchy–
Binet Decomposition
Theorem 1(Universal Row-Sum Eigenpair, Diagonal Invariance, and Rank-2Gram Factoriza-
tion).LetA∈C n×n (n≥2) andF A :=A◦adj per(A).
(a) Universal row-sum eigenpair:FA1= per(A)1and1 TFA = per(A)1T identically. When A
is Hermitian,FA is Hermitian andper(A)In −FA ⪰0holds if and only if
λmax
(
FA|1⊥
)
≤per(A).(2)
2

--- Page 3 ---
(b) Exact diagonal congruence invariance:For every diagonal matrixD= diag(d1,...,d n)∈
Cn×n,
per(DAD∗) =|detD| 2 per(A), F DAD∗ =|detD| 2FA.(3)
In particular, for rank-2PSDA= uu∗+ vv∗ with( ui,vi) ̸= (0,0), the normalized operator
FA/per(A)depends only on then-tuple of projective points
(
[ui :vi]
)n
i=1 ∈(CP 1)n.
(c) Exact O(n3)Cauchy–Binet ESP Gram factorization:Let A = uu∗+ vv∗ (u,v∈C n).
Define the degree-n polynomial coefficientsck := [xk] ∏n
j=1(uj + xvj)(0 ≤k≤n ) and the
leave-one-out coefficientspi,k := [xk] ∏
j̸=i(uj + xvj)(1 ≤i≤n ,0 ≤k≤n− 1), together
with vectors(Uk)i :=uipi,k and(V k)i :=vipi,k inC n. Then
per(A) =
n∑
k=0
k! (n−k)!|ck|2,(4)
FA =
n−1∑
k=0
k! (n−1−k)!
(
UkU∗
k +VkV∗
k
)
.(5)
Consequently, FA ⪰0holds unconditionally for every rank-2PSD matrix A, and both
per(A)and FA are computable inO(n3)exact ring operations over any subringR⊆C (in
particularR=Z[i]).
Proof. Proof of(a).By Laplace expansion of the permanent along rowi, we have(FA1)i =∑n
j=1 aij per(A(i|j)) =per(A), and column expansion yields1TFA = per(A)1T. When A∗= A,
we haveA(j|i) =A(i|j)∗, henceper(A(j|i)) =per(A(i|j)) and( FA)ji = aij per(A(i|j)) = (FA)ij.
Thus FA is Hermitian, leavesC1and1 ⊥ invariant, and has eigenvalueper(A)on1; hence
per(A)In −FA ⪰0iff (2) holds.
Proof of(b).Each permutation σ∈S n contributes ∏n
r=1(drar,σ(r)dσ(r)) =|detD|2 ∏n
r=1 ar,σ(r)
to per(DAD∗). Similarly,( DAD∗)(i|j)removes factor di from rows anddj from columns, so its
permanent scales by
(∏
r̸=idr
)(∏
c̸=j dc
)
, and multiplying by(DAD∗)ij = diaijdj restores the
exact factor|detD|2 uniformly across all(i,j). Scaling row(ui,vi) ↦→(diui,divi)replaces A by
DAD∗, leavingFA/per(A)invariant on(CP 1)n.
Proof of(c).Write aij = uiuj + vivj. Expanding per(A) =∑
σ∈Sn
∏n
i=1(uiuσ(i) + vivσ(i))by
selecting the subsetS⊆ [n]of size k that takes thev-term and settingT = σ(S)(also of size k),
there arek!(n−k)!bijectionsσmappingS→TandS c →T c, each contributing
(∏
i∈S
vi
∏
i/∈S
ui
)(∏
j∈T
vj
∏
j/∈T
uj
)
.
Summing over all|S|= |T|= k factors as|ck|2, giving(4). Applying the identical expansion to
the(n−1)×(n−1)submatrixA(i|j)(rows[n]\{i}, columns[n]\{j}) gives
per
(
A(i|j)
)
=
n−1∑
k=0
k!(n−1−k)!p i,kpj,k.
Multiplying byaij =uiuj +vivj yields
(FA)ij =
n−1∑
k=0
k!(n−1−k)!
(
(uipi,k)(ujpj,k) + (vipi,k)(vjpj,k)
)
,
which is (5). Since eachUkU∗
k +VkV∗
k ⪰0,F A ⪰0immediately.
3

--- Page 4 ---
3 Low-Dimensional Rigidity, Circulant AM–GM Barrier, and
Real Balanced Saturation
Theorem 2(Low-Dimensional Rigidity, Circulant Spectrum, and Direct-Sum Saturation).
(a) Exact n = 2rigidity:For every2 ×2Hermitian matrix A =
(a b
¯b c
)
and every w =
(w1,w2)T ∈C 2,
per(A)∥w∥2
2 −w∗FAw=|b| 2 |w1 −w2|2 ≥0.(6)
(b) Exact n= 3shift-Laplacian identity and rank-2spectral collapse:For every3×3Hermitian
matrixA 0 = (aij)and every scalart∈R,
per(A0 +tI3)I3 −FA0+tI3 =
(
per(A0)I3 −FA0
)
+tL(|A 0|◦2),(7)
whereL(|A0|◦2) :=∑
1≤i<j≤3 |aij|2(ei −ej)(ei −ej)T ⪰0is the weighted graph Laplacian.
Consequently, writing any3 ×3Hermitian PSD matrix asA= A0 + λmin(A)I3 reduces the
3 ×3Bapat–Sunder theorem [1, 5] to rank≤2. Furthermore, on rank-2A0 = J3 + zz∗, the
k= 0U-term andk= 2V-term vanish on1⊥while( U1)⊥= −(V0)⊥and( V1)⊥= −(U2)⊥,
collapsingF A0 |1⊥ to the exact rank-2operator
FA0
⏐⏐
1⊥ = 3
(
(V0)⊥(V0)∗
⊥+ (U2)⊥(U2)∗
⊥
)
,(8)
and for any normalized3×3Hermitian correlation matrix A with modulir1,r2,r3 ∈[0,1],
P = r1r2r3, s1 = ∑ r2
i, s2 = ∑
i<j r2
ir2
j, andu= Pcosθ , all three2 ×2principal minors
ofper(A)I 3 −FA equal the convex quadraticD2(u) = 4u2 + 2s1u+ (s2 −P 2).
(c) Exact n-th root circulant Fourier spectrum and universal AM–GM barrier:Letn≥ 3,
r> 0, ω= e2πi/n, andAn(r) :=Jn + zz∗ with zj = rωj (0 ≤j≤n− 1). Then FAn(r) is
Hermitian circulant with exact eigenvalues on the Fourier basisfm = (ωjm)n−1
j=0 :
λ0 = per
(
An(r)
)
=n!(1+r 2n), λ m =n2(m−1)! (n−1−m)!r2m (1≤m≤n−1).(9)
In particular, atr= 1,λm/per (An(1)) = n
2(n−1)(n−2
m−1) ≤ n
2(n−1) <1, and acrossall r> 0
andalln≥3,
sup
r>0
λmax
(
FAn(r)|1⊥
)
per
(
An(r)
) = (n−1) −1/n <1,(10)
attained uniquely at(m= 1,r2n = (n−1) −1)and(m=n−1,r 2n =n−1).
(d) Exact direct-sum and real balanced boundary saturation:For any block direct sum
A = A1 ⊕A2 (A1 ∈C m1×m1 , A2 ∈C m2×m2 with per(A) > 0), FA = (per(A2)FA1 ) ⊕
(per(A1)FA2 ), so w = (m21m1 ,−m11m2 ) ∈1⊥ satisfies FAw = per(A)w. In particular,
the real rank-2balanced familyA= J2m + zzT = 2(Jm ⊕Jm)with z= (+1m,−1m)obeys
per(A) = (2mm!)2 andλ max(FA|1⊥)/per(A) = 1identically for everym≥1.
Proof. Proof of(a).For n = 2,per(A) = ac+ |b|2 and FA =
(ac|b| 2
|b|2 ac
)
, so per(A)I2 −FA =
|b|2(1−1
−1 1
)
, giving (6) (Leanthm01–thm02).
Proof of(b).Expanding per(A0 + tI3)and( FA0+tI3 )ij in powers oft: the t3 term inper(A0 +
tI3) −(FA0+tI3 )ii is t3 −t3 = 0, the t2 term is tr(A0)t2 −(aii + ∑
k̸=iakk)t2 = 0, and the
t1 term is∑
p<q(appaqq + |apq|2) −(aii
∑
k̸=iakk + per(A0(i|i))) = ∑
j̸=i |aij|2, while fori̸= j,
(FA0+tI3 )ij = aij(aijt+ per(A0(i|j))) =|aij|2t+ (FA0 )ij (Lean thm04–thm06). ForA0 = J3 + zz∗
(n = 3), U0 =1and V2 = (z1z2z3)1are multiples of1(hence annihilated on1 ⊥), while
(U1)i+ (V0)i = e1(z)and( V1)i+ (U2)i = e2(z)(Lean thm07), so projecting(5) onto1 ⊥combines
4

--- Page 5 ---
coefficients2 + 1 = 3on( V0)⊥ and1 + 2 = 3on( U2)⊥, yielding (8). Direct expansion of
M11M22 −|M12|2 on a3×3Hermitian correlation matrix yieldsD 2(u)(Leanthm08).
Proof of(c).For zj = rωj, the polynomial identity∏
l̸=j(1+xrωl) =1−(−xr)n
1+xrωj = ∑n−1
k=0 (−rωj)kxk
yields c0 = 1, cn = (−1)n−1rn, ck = 0for1 ≤k≤n− 1, hence per(An(r)) = n!(1 +r2n).
Moreover( Uk)j = (−r)kωjk = (−r)k(fk)j and( Vk)j = zj(Uk)j = (−1)krk+1(fk+1)j (indices
mod n). Substituting into(5) diagonalizes FAn(r) directly in the orthogonal Fourier basis{fm}
(∥fm∥2
2 = n): for m = 0,k = 0(U0) andk = n−1( Vn−1) contributen·(n−1)!(1 +r2n) =
per(An(r)); for1≤m≤n−1,k=m(U m) andk=m−1(V m−1) contribute
λm =n
(
m!(n−1−m)! + (m−1)!(n−m)!
)
r2m =n 2(m−1)!(n−1−m)!r 2m,
proving (9). Dividing byper(An(r))gives
λm
per(An(r)) = n
(n−1)
(n−2
m−1
)· r2m
1 +r2n.
By weighted AM–GM with weightsm
n and n−m
n ,
1 +r2n = m
n
(n
mr2n
)
+ n−m
n
( n
n−m
)
≥
(n
m
)m/n( n
n−m
)1−m/n
r2m,
so
r2m
1 +r2n ≤
(m
n
)m/n(n−m
n
)1−m/n
,
with equality iffr2n = m
n−m. Atm= 1(and symmetricallym= n−1under r↦→r−1),
(n−2
0
)
= 1
and the right-hand side multiplies n
n−1 to give exactly(n− 1)−1/n < 1. For2 ≤m≤n− 2
(n≥ 4),
(n−2
m−1
)
≥n− 2and
(m
n
)m/n(
1 −m
n
)1−m/n <1, while forn= 4(m= 2) direct evaluation
gives 4
3·2 ·1
2 = 1
3 <3−1/4, and for everyn≥ 5we have n
(n−1)(n−2
m−1) ≤ n
(n−1)(n−2) ≤ 5
12 <4−1/5 ≤
(n−1) −1/n. Thus (10) holds for everyn≥3.
Proof of(d).For A = A1 ⊕A2, deleting row i and column j from opposite blocks leaves
a rectangular-zero block whose permanent is0, while within block1we get per(A(i|j)) =
per(A1(i|j)) per(A2), so FA = (per(A2)FA1 ) ⊕(per(A1)FA2 ). Using FAr 1mr = per(Ar)1mr
yields FAw= per(A)w on w= (m21m1 ,−m11m2 ) ∈1⊥. When z= (+1m,−1m),1 +zizj = 2on
the twom×m diagonal blocks and0off-diagonal, so A= 2Jm ⊕2Jm with per(A) = (2mm!)2
(Lean thm14–thm15). Since each rank-1block satisfies F2Jm = per(2Jm)
m Jm ⪯per (2Jm)Im, we
haveFA ⪯per(A)I2m and henceλmax(FA|1⊥)/per(A) = 1identically.
4 Exact Gaussian-Integer Rank-Two Complex Refutations at
n= 8,9,10
Theorem 2(c) proves that symmetricn-th root rank-2configurations canneverviolate (1), while
naive optimization ofλmax(FA)/per (A)stalls on the flat eigenvalueper(A)along1. Maximizing
λmax(FA|1⊥)/per (A)directly over( CP1)n breaks phase and radial symmetry and reveals strict
complex rank-2violations starting at n= 8(λmax/per≈ 1.01956), growing rapidly atn= 9
(≈1.06660) andn= 10(≈1.09508), while multi-start optimization finds no rank-2complex
violation forn≤ 7and no rank-2real violation up to n = 16. Rounding to small Gaussian
integers yields exact, self-contained refutations overZ[i].
Theorem 3(Zero-Float Gaussian-Integer Rank-2Complex Refutations).The Bapat–Sunder
inequality per(A)In −FA ⪰0fails already for rank-2Hermitian PSD matricesA= uu∗+ vv∗∈
Z[i]n×n atn= 8,9,10:
5

--- Page 6 ---
Figure 1:Exact n-th root circulant spectrum and universal AM–GM radial bar-
rier (Theorem 2(c)).(a) Exact unit-circle Fourier eigenvalues λm(FAn(1))/per (An(1)) =
n
2(n−1)(n−2
m−1) across n = 4,6,8,12, peaking strictly below1at m = 1,n− 1. (b) Exact radial
amplitude curvesλ1(r)/per (An(r))across r> 0, each bounded tightly by its AM–GM supremum
(n−1) −1/n <1.
(a) Dimensionn= 8(general rank2, Leanthm16, Certificatecert08):Let
u8 = (3−i,−3−4i,−5,−4 + 3i,−1,−5,−2,−4−2i) T,
v8 = (1 + 5i,2−2i,−4−i,1,−5,4−i,5 +i,−1 + 5i) T,
w8 = (i,2 +i,2 + 5i,3−3i,−3 + 2i,−i,−2−i,−3−4i) T.
Then A8 = u8u∗
8 + v8v∗
8 has exact rank2( det([u8,v8]∗[u8,v8]) >0), permanentper(A8) =
573,191,776,350,720, squared norm∥w8∥2
2 = 97, and
w∗
8FA8 w8 −per(A8)∥w8∥2
2 = 56,248,044,686,676,480−55,599,602,306,019,840
= +648,442,380,656,640>0,(11)
giving exact Rayleigh ratio>1.01166(spectral ratioλ max(FA8 |1⊥)/per(A8)≈1.01562).
(b) Dimension n = 9ultra-compact s = 1witness A9 = J9 + z9z∗
9 (Lean thm17, Certifi-
catecert09):Let
z9 = (−1,−1 +i,1−2i,0,2 +i,0,−i,1,−2−i) T,
w9 = (−6,−9−4i,2−2i,8i,6−7i,8i,1 +i,8−i,−3−3i) T.
Thenper(A 9) = 6,088,320,∥w9∥2
2 = 439, and
w∗
9FA9 w9 −per(A9)∥w9∥2
2 = 2,684,345,472−2,672,772,480 = +11,572,992>0(12)
(Rayleigh ratio> 1.00432; spectral ratio≈1.00617). A second general n = 9witness
(Certificatecert10) achieves Rayleigh ratio>1.00764(spectral ratio≈1.02530).
(c) Dimension n= 10high-margin s= 2witness A10 = 4J10 + z10z∗
10 (Lean thm18, Certifi-
catecert11):With
z10 = (3−4i,−2−i,−3 + 3i,3 + 3i,2−i,−i,1,2i,−1,−3−3i) T,
w10 = (−1,2−i,2 + 2i,−1 + 2i,−2,−1−3i,−5−i,1 + 5i,4−3i,1) T,
A10 violates (1) with Rayleigh ratio> 1.08557(over8 .55%above unity; spectral ratio
≈1.09508).
6

--- Page 7 ---
Table 1: Zero-float certified rank-2complex refutations overZ[i](Certificates cert08–cert14,
Leanthm16–thm19).
WitnessnForm∥w∥ 2
2 Exactper(A)Exact gapw ∗Fw−per∥w∥ 2
2 RayleighRe-stripped
cert088u 8u∗
8 +v 8v∗
8 97 573,191,776,350,720 +648,442,380,656,640 1.01166 0.2071
cert099J 9 +z 9z∗
9 439 6,088,320 +11,572,992 1.00433 0.4486
cert109u 9u∗
9 +v 9v∗
9 83 44,125,969,104,000 +28,015,262,426,880 1.00765 0.2225
cert1110 4J 10 +z 10z∗
10 111 120,756,089,364,480 +1,147,005,482,158,080 1.08557 0.2356
Figure 2:Rank-2complex dimension threshold and phase-stripping restoration.
(a) Peak1 ⊥ spectral ratio across n = 2,..., 10: symmetric circulants stay strictly below
(n−1)−1/n <1, real balanced direct sums saturate1, and asymmetric complex rank-2matrices
first break unity atn= 8, with zero-floatZ[i]witnesses at n= 8,9,10. (b) Spectral ratios, exact
Z[i]Rayleigh ratios, and phase-stripped (Re) ratios across all four witnesses.
(d) Centering and phase-stripping restoration:Projecting each witness onto1 ⊥ via w⊥ =
nw−(∑
iwi)1preserves (and strictly improves whenever∑
iwi ̸= 0) the violation ratio,
whereas replacing all imaginary parts of(u,v)by0restores w∗FRew≤per (ARe)∥w∥2
2 (at
n= 9,s = 1in Leanthm19, and across all four witnesses in Certificatescert12–cert13).
Proof. Every claim in parts (a)–(d) is a finite identity overZ[i]. In Layer 1, Lean 4.36.0 directly
evaluates the exactO(n3)Cauchy–Binet ESP expressions(4)–(5) over Z[i]via decide in thm16–
thm19. In Layer 2,verification/verify_bapat_sunder_rank2.py independently builds the
full n×n Gaussian-integer matricesAn, computesper(An)and every( n−1)×(n−1)permanent
cofactor per(An(i|j))via direct Gray-code Ryser permanent overZ[i], asserts exact entrywise
equality FESP = FRyser, verifies exact rank2(det([u,v]∗[u,v]) >0, Certificatecert14), verifies
FA1= per(A)1, and certifies the exact integer gaps in Certificatescert08–cert13.
5 Formal Verification Architecture and Scope
Our verification artifact cleanly separates machine-checked algebraic identities and direct kernel
evaluations from prose analytic proofs and exact Python cross-checks:
• Layer 1 — Constructive Lean 4.36.0 Kernel( lean/BapatSunderRank2.lean):
Twenty theorems compiled withlean-DwarningAsError=true, zero external dependencies,
zero sorry, zerogrind, zeroClassical.choice, and no custom axioms beyond standard
constructive propext/Quot.sound (audited via#print axioms). Layer 1 formalizes the
exact n= 2quadratic identity and unconditional Bapat–Sunder bound (thm01–thm03),
7

--- Page 8 ---
Figure 3:Broken phase/radial geometry and full1⊥ spectra of counterexamples.(a)
Complex-plane coordinates ofz9 (s= 1, including the double zeroz4 = z6 = 0) andz10/2( s= 2)
contrasted with the unit circle. (b) Complete descending eigenvalues ofFA|1⊥/per (A)for the
n= 8,9,10witnesses: each exhibits a single clean outlier eigenvalue piercing the Bapat–Sunder
threshold1.
the exact n = 3shift-Laplacian identity, Laplacian PSDness, rank-21 ⊥ collapse, and
correlation discriminant identity (thm04–thm08), diagonal scaling invariance forn= 2,3
(thm09–thm10), circulant unit-circle and all-rbarriers (thm11–thm13), real balanced satura-
tion form= 1,..., 4and direct-sum eigenpairs (thm14–thm15), direct kernel evaluations of
all three Gaussian-integer rank-2refutations atn= 8,9,10and phase-stripping restoration
(thm16–thm19), and ESP-vs-direct-3×3permanent equivalence (thm20). The general-
n Cauchy–Binet proof (Theorem 1(c)), general-n weighted AM–GM circulant bound
(Theorem 2(c)), and general-n direct-sum argument (Theorem 2(d)) are proved in full
mathematical detail in Sections 2–3.
• Layer 2 — Zero-Float Python Verifier( verification/verify_bapat_sunder_
rank2.py): An AST-audited pure standard-library verifier using strictlyint and Fraction
(zero floats, zero numeric/, zero**, zerolimit_denominator), emitting16SHA-256 cer-
tificates incertificates/MANIFEST.json and validated by56adversarial pytest checks
in tests/test_adversarial.py. Crucially, Layer 2 independently cross-checks every
n = 2,..., 10Cauchy–Binet ESP matrix FESP entry-by-entry against direct Gray-code
Ryser permanent evaluation overZ[i], confirming exact agreement across all four refutations
(cert08–cert11).
References
[1] R. B. Bapat and V. S. Sunder,On majorization and Schur products, Linear Algebra Appl.
72(1985), 107–117.
[2] R. B. Bapat,An extension of a theorem of Gyires, Linear Multilinear Algebra19(1986),
273–279.
[3] S. W. Drury,A counterexample to a conjecture of Bapat and Sunder, Electron. J. Linear
Algebra31(2016), 69–70.
[4] M. Marcus and M. Newman,Inequalities for the permanent function, Ann. of Math. (2)75
(1962), 47–62.
8

--- Page 9 ---
[5] F. Zhang,Notes on Hadamard products of matrices, Linear Multilinear Algebra25(1989),
237–242.
[6] L. R. Chalmers,The Bapat–Sunder eigenvalue conjecture fails over the reals, preprint
arXiv:2611.23269, November 2026.
9
