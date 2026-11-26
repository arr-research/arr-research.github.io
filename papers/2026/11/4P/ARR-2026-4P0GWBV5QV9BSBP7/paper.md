# Exact Dicke-State Moments, Certified Single-Round Amplification, and Subquadratic Reversible Routing for Asymptotic Quantum Many-Body Scars

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-4P0GWBV5QV9BSBP7` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/qmbs-dicke-sharp-moments-routing (`v1.0.2`)  
**Canonical PDF SHA-256:** `e81f6234e06f7b7a4793e4cd9e4ca37138aa8ede398718fb1b9598c303edb017`

## Abstract

We resolve three quantitative and algorithmic gaps in the unified Dicke-state preparation protocol for exact and asymptotic quantum many-body scars (AQMBS) of Asari, Kunimi, and Nikuni (arXiv:2611.33987v1). First (Theorem A), we derive exact closed-form without-replacement rational formulas for the fourth and sixth moments of Z(l) on Dicke states |D_n^{M'}> across all four cosine power-sum resonance classes, proving uniformly for all M' >= 2, 1 <= n <= M'-1, and 1 <= l <= M'-1 that kappa_4 <= 3 (4x sharper than Asari et al.'s Hoeffding bound 12, with unique finite equality at (M',n,l)=(4,2,2)), kappa_6 < 15 (8x sharper than 120), and kappa_6 - kappa_4^2 < 6. Second (Theorem B), projecting sin(sX) onto the optimal linear multiple (1 - (kappa_4/6)s^2)sX yields the universal non-asymptotic infidelity bound 1 - F(s) <= s^4(4 + 3s^2)/(6(2 - s^2)^2) for all 0 < s < sqrt(2) and envelope s^2 - s^4 <= p_succ(s) <= s^2. At Asari et al.'s operating point s = 0.495, this improves the bare p_succ lower bound by 37.94x (to 0.18499), certifies single-round Grover amplification p_amp^(1) >= 0.94488 with zero overshoot uniformly over all (M',n,l) (21.8x above the prior bound), and sharpens uniform infidelity by 13.01x (to 0.01538); at s = 0.45, it certifies 1 - F <= 0.00975 < 0.01 uniformly with p_succ >= 0.16149 (25.84x above Eq. S11). Third (Theorem C), we construct a collision-free MSB-to-LSB binary-shift reversible routing circuit for both Onsager and DWC spacer-insertion maps Phi^{-1} using exactly B(BL - 2^B + 1) = O(M log^2 n) Stage-2 Fredkin gates plus at most B(2M' + 3L) = O(M log n) Stage-1/3 prefix-sum Toffoli gates with zero ancilla leakage, improving asymptotically by Theta(M/log^2 n) over the unpruned Theta(M^2) conveyor for all 3 <= n <= M'-2 and by Theta(n/log^2 n) over the pruned displacement benchmark 0.5*n*(2M'-n-1) whenever n = omega(log^2 n) (half-filling crossovers at M'=184 Stage-2 / M'=382 total 3Q gates, reaching 7.53x Stage-2 / 5.45x total 3Q reductions at M'=4096). All explicit six-partition formulas and eight branch polynomials for Theorem A(ii)-(iii) are included in Appendix A for standalone manuscript verification; the algebraic cores are constructively formalized in Lean 4.35.0 (18 theorems, 0 sorry, 0 Classical.choice, 0 warnings), backed by 16 SHA-256 exact rational certificates (QMBS-DICKE-SHARP-1.0) and an AST-audited zero-float verifier (53/53 tests passing).

## Full Extracted Text

--- Page 1 ---
Exact Dicke-State Moments, Certified Single-Round
Amplification, and Subquadratic Reversible Routing
for Asymptotic Quantum Many-Body Scars
Lluis Eriksson
Independent Researcher (AIRR.SCIENCE Frontier Verification Lab)
https://github.com/lluiseriksson/qmbs-dicke-sharp-moments-routing
November 26, 2026
Abstract
Asari, Kunimi, and Nikuni [1] recently introduced a unified quantum algorithm that
prepares exact and asymptotic quantum many-body scar (AQMBS) states across the spin-
1 XY, domain-wall-conserving (DWC), and Onsager scar models via block encoding of a
cosine-modulated operatorZ(l) = ∑M′
j=1 fj(l)Zj on Dicke states|DM′
n ⟩, followed by amplitude
amplification and a reversible routing isometryΦ−1. Three theoretical gaps remain in their
analysis: (i) sampling-with-replacement Hoeffding relaxations inflate the normalized fourth and
sixth moments toκ4 ≤12and κ6 ≤120, collapsing the rigorous success-probability guarantee
at their operating points= 0.495to psucc ≥0.00488; (ii) the target infidelity1−F≤ 0.01
at s= 0.495is verified only numerically for small chains (M′≤12), while their conservative
analytical schedule guarantees onlypsucc ≥√ε/16; and (iii) for intermediate scar indices
3 ≤n≤M ′−2, no reversible routing circuitΦ−1 better than aΘ(M2)-gate Fredkin conveyor
is identified.
We resolve all three gaps with three original theorems. First (Theorem A), we derive exact
closed-form without-replacement rational formulas for⟨Z(l)4⟩and ⟨Z(l)6⟩across all four cosine-
sum resonance classes, proving uniformly for allM′≥2,1 ≤n≤M ′−1, and1 ≤l≤M ′−1
that κ4 ≤3(4 ×sharper, with unique finite equality at(M′,n,l ) = (4,2,2)), κ6 < 15(8 ×
sharper), andκ6 −κ2
4 <6. Second (Theorem B), projectingsin(sX)onto the optimal linear
multiple(1 −κ4
6 s2)sX yields the uniform non-asymptotic infidelity bound1−F(s) ≤s4(4+3s2)
6(2−s2)2
for all0 < s <
√
2 and the two-sided envelopes2 −s4 ≤p succ(s) ≤s 2. At s = 0 .495,
this improves the rigorous psucc bound by37 .94×(to0 .18499), certifies p(1)
amp ≥0.94488
in a single Grover round with zero overshoot uniformly over all(M′,n,l )(21 .8×above
the prior bound), and sharpens the uniform infidelity bound by13.01×(to0 .01538); at
s= 0.45, it certifies1 −F≤ 0.00975 <0.01uniformly with psucc ≥0.16149(25 .84×above
Eq. (S11)) andp(1)
amp ≥0.8949. Third (Theorem C), we construct a strictly order-preserving,
collision-free MSB-to-LSB binary-shift reversible routing circuit for both Onsager and DWC
spacer-insertion mapsΦ−1 using exactlyB(BL−2B+ 1) = O(Mlog 2 n)Stage-2 Fredkin gates
plus at mostB(2M′+ 3L) =O(Mlogn)Stage-1/3 prefix-sum Toffoli gates with zero ancilla
leakage, improving asymptotically byΘ(M/log 2 n)over the unprunedΘ( M2)conveyor for all
3 ≤n≤M ′−2and byΘ( n/log 2 n)over the pruned sitewise-displacement lower benchmark
1
2 n(2M′−n− 1)whenever n = ω(log2 n)(achieving permanent half-filling crossovers at
M′= 184for Stage-2 Fredkins and M′= 382for total 3-qubit gates, and7 .53×Stage-2 /
5.45×total 3-qubit gate reductions atM′= 4096). All explicit six-partition formulas and
eight branch polynomials for Theorem A(ii)–(iii) are tabulated in Appendix A for standalone
verification from this manuscript; the algebraic cores of Theorems A–C are constructively
formalized in Lean 4.35.0 (18 theorems, 0sorry, 0Classical.choice), while the real-analytic
trigonometric Taylor lifting in Theorem B is proved analytically and audited alongside 16
SHA-256 exact rational certificates (QMBS-DICKE-SHARP-1.0) via an AST-verified zero-float
Python suite (53/53 tests passing).
1

--- Page 2 ---
1 Introduction and Summary of Contributions
Quantum many-body scars (QMBS) and asymptotic quantum many-body scars (AQMBS) [4, 6]
violate strong eigenstate thermalization via polynomially vanishing energy variances∆E2 =
O(M−2)and correspondingly slow relaxation times. In a recent breakthrough, Asari, Kunimi,
and Nikuni [1] unified state preparation for exact and asymptotic scar towers in the spin-1XY,
domain-wall-conserving (DWC), and Onsager scar models by mapping each constrained tower
onto a Dicke manifold|DM′
n ⟩(prepared deterministically via e.g. [2]) on an effective chain of
lengthM ′, applying a single-ancilla block encoding
UBE =HaeiτZa⊗Z(l) Ha, Z(l) =
M′
∑
j=1
fj(l)Zj, f j(l) = cos
(πl(2j−1)
2M′
)
,(1)
postselecting on|1⟩a (or amplifying viaK Grover rounds [3]) to obtain|˜A⟩∝sin [τZ(l)]|DM′
n ⟩,
and finally applying a reversible routing isometryΦ−1 = D◦S◦R to map effective-chain bitstrings
to physical constrained configurations.
While [1] establishesK = O(1)asymptotic scaling, its Supplemental Material (SM A.1 and
SM B.2) leaves three quantitative and algorithmic bottlenecks open:
1. LooseHoeffdingmomentbounds:Ratherthancomputingtheexactwithout-replacement
fourth and sixth moments ofZ(l)on |DM′
n ⟩, Ref. [1] invokes Hoeffding’s with-replacement
inequality [5] (Lemma SA.1) together with⟨Z(l)2⟩≥n , obtaining ⟨Z(l)4⟩≤ 12n2 and
⟨Z(l)6⟩≤ 120n3 (normalized ratiosκ4 ≤12, κ6 ≤120). At their recommended operating
point s= τ⟨Z(l)2⟩1/2 = 0.495(Eq. (12)), this collapses their rigorous success-probability
lower bound (Eq. (S15)) topsucc ≥s2 −4s4 = 0.004876, which guarantees onlyp(1)
amp ≥0.0433
after one Grover round (requiring up toK = 11rounds worst-case) despite true values
psucc ∈[0.19,0.23].
2. Unproved uniform fidelity ats= 0.495and conservative τ(ε)schedule:Bounding
1 −F by the unscaled distance∥sin (τZ) −τZ∥2/∥τZ∥2 gives1 −F≤ 10
3 s4 = 0.2001at
s = 0 .495(Eq. (S9)). Consequently, Ref. [ 1] verifies1 −F≤ 0.01at s = 0 .495only
numerically forM′≤12, falling back to a conservativeτ = ε1/4/(2√n)(Eq. (S11)) that
guarantees onlypsucc ≥√ε/16(0.00625atε= 0.01).
3. Quadratic routing bottleneck for intermediaten:In SM B.2, Ref. [1] constructs
Θ(M)-gate ladders only forn= 2and DWC half filling (n= M′−1), explicitly noting that
for intermediate scar indices3≤n≤M ′−2they have identified no reversible implementation
of R more efficient than theΘ(M2)-gate Fredkin conveyor—causing noisy prepared-state
fidelity atn = 3,M = 12to drop from0 .66to0 .37(DWC) and0 .43(Onsager) in their
Table S2.
Table 1 summarizes our three breakthroughs resolving all three bottlenecks.
2 Theorem A: Exact Without-Replacement Dicke Moments and
Universal Kurtosis Bounds
For any M′ ≥ 2,1 ≤n≤M ′−1, and1 ≤l≤M ′−1, let T⊂ {1,...,M ′}be drawn
uniformly among all
(M′
n
)
subsets of sizen. Because ∑M′
j=1 fj(l) = 0, the eigenvalue ofZ(l)on
basis state|T⟩is λT = −2 ∑
j∈T fj(l), and its exactk-th moment isµk := ⟨DM′
n |Z(l)k|DM′
n ⟩=
(−2)kET[(∑
j∈T fj(l))k]. Writepr := ∑M′
j=1 fj(l)r. By Eq. (S4) of [1], p1 = 0, p2 = M′/2, and the
2

--- Page 3 ---
Table 1: Quantitative comparison between Asari, Kunimi, and Nikuni [1] and Theorems A–C of
this work.
Quantity / Metric Asari et al. [1] This Work (Theorems A–C) Gain
Normalized kurtosisκ4 ≤12(Eq. S7)≤3(eq. iff(4,2,2))4×exact
Normalized sixth momentκ6 ≤120(Eq. S8)<15(uniform)8×exact
Projection varianceκ6 −κ2
4 N/A (10
3 s4 coeff.)<6( 1
6 s4 leading)20×leading
Barep succ lower bound (s= 0.495)0.004876(Eq. S15)0.184988(s 2 −s4)37.94×
CertifiedK= 1Groverp (1)
amp (s= 0.495)0.0433≥0.94488(no overshoot)21.8×
Uniform infidelity1−F(s= 0.495)≤0.20012(Eq. S9)≤0.01538(Thm. B)13.01×
Certifiedp succ atε= 0.01 0.00625(Eq. S11)0.16149(s= 0.45)25.84×
Asymptoticp succ(ε)(ε→0) √ε/16 2 √ε−4ε32×
Reversible routerR(3≤n≤M ′ −2)Θ(M 2)unprunedO(Mlog 2 n)total 3Q gatesΘ(M/log 2 n)
tuple(p 3,p4,p6)falls into exactly four exact rational resonance classes:
(
p3/M′, p4/M′, p6/M′)
=



(0,1/4,1/8)if4l= 2M ′ (branchR4),
(0,3/8,9/32)if6l= 2M ′ (branchR6),
(−1/4,3/8,11/32)if3l= 2M ′ (branchR3),
(0,3/8,5/16)otherwise(branchG).
(2)
Note thatµ2 = 2n(M′−n)
M′−1 is invariant across all four branches, andµk is invariant under the bit-flip
symmetryn↔M ′−n. Define the normalized momentsκ4 :=µ4/µ2
2 andκ 6 :=µ6/µ3
2.
Theorem A(Exact Dicke-State Moments and Universal Sharp Bounds).For every integer
M′ ≥2, every excitation number1 ≤n≤M ′−1, and every harmonic1 ≤l≤M ′−1, let
u:=n(M ′−n)andv := (M′−2n) 2 =M ′2 −4u∈[0,(M ′−2) 2].
(i)Exact fourth-moment kurtosis (4×sharpening):For all(M ′,n,l),
3−κ 4(M′,n,l) =



3
[
(M′−2n) 2 +M ′(M′−2)
]
4u(M′−2) >0 (4l̸= 2M ′, M′≥3),
3(M′−2n) 2 +M ′(M′−4)
2u(M′−3) ≥0 (4l= 2M ′, M′≥4),
2 (M ′= 2, n= 1, l= 1).
(3)
In particular,κ4(M′,n,l ) ≤3uniformly, with equality if and only if(M′,n,l ) = (4,2,2)
(whereµ2 = 8/3,µ 4 = 64/3,κ 4 = 3,κ 6 = 9, andκ6 −κ2
4 = 0).
(ii)Exact sixth-moment ratio (8×sharpening):Uniformly over all(M ′,n,l),
κ6(M′,n,l)<15.(4)
(iii)Exact orthogonal-projection variance bound:Uniformly over all(M′,n,l),
0≤κ 6(M′,n,l)−κ 4(M′,n,l) 2 <6.(5)
All three constants(3,15,6)are asymptotically tight: at fixed fillingn/M′= ρ∈ (0,1), κ4 →3,
κ6 →15, andκ 6 −κ2
4 →6asM ′→∞.
Proof. Let ar := n(n−1)···(n−r+1)
M′(M′−1)···(M′−r+1) denote ther-th falling-factorial sampling probability (with
ar = 0for r>n ). Expanding( ∑
j∈T fj)4 into distinct-index partitions and eliminating all sums
via p1 = 0yields s4 = p4, s3,1 = −p4, s2,2 = p2
2 −p4, s2,1,1 = 2p4 −p2
2, ands1,1,1,1 = 3p2
2 −6p4,
hence
µ4 = 16
[
a1s4 +a2(4s3,1 + 3s2,2) + 6a3s2,1,1 +a4s1,1,1,1
]
.(6)
3

--- Page 4 ---
Dividing byµ2
2 = 4u2
(M′−1)2 and substitutingp4 = c4M′gives remarkable algebraic cancellations: for
c4 = 3/8(4 l̸= 2M′, soM′≥3), the factor(M′−3)cancels identically, givingκ4 = 3(M′−1)(2u−M′)
2u(M′−2) ;
forc4 = 1/4(4 l= 2M′, M′≥4), the factor(M′−2)cancels identically, givingκ4 = (M′−1)(3u−2M′)
u(M′−3) .
Using4 u= M′2 −(M′−2n)2 immediately produces the manifestly nonnegative sum-of-squares
identities(3), provingκ4 ≤3withuniquefiniteequalityat( M′,n,l ) = (4,2,2)(Lean4Theorems2–
4). ForM′= 2,n = 1,l = 1, f1 = −f2 = 1/
√
2 gives λ2
T ≡2, henceκ4 = κ6 = 1and κ6 −κ2
4 = 0.
Forµ6, expanding(∑
j∈T fj)6 over all 11 integer partitions of6and reducing each distinct-index
sum via p1 = 0(all 11 explicit sums sλ andΣ 1,..., Σ6 are listed in Appendix A and verified
via the conservation check∑
λ⊢6 cλsλ = p6
1 = 0) expresses µ6 = 64 ∑6
r=1 arΣr(p2,p3,p4,p6)as
an exact rational function of(M′,n)on each branch (2). On every branch, clearing positive
denominators in15 −κ6 and6 −(κ6 −κ2
4)and substituting u = (M′2 −v)/4yields an exact
quadratic polynomial inv= (M ′−2n) 2 ∈[0,D]withD= (M ′−2) 2:
Q(M′,v) =A(M ′) +B(M ′)v+C(M ′)v2,(7)
whose explicit coefficients(A,B,C )across all eight branch-bound pairs are tabulated in Table 3
of Appendix A. By the exact algebraic identity (Lean 4 Theorem 1)
D·Q(M ′,v) = (D−v)Q(M ′,0) +vQ(M ′,D) +
(
−C(M′)
)
Dv(D−v),(8)
whenever Q(M′,0) > 0, Q(M′,D) > 0, and−C(M′) ≥0, strict positivityQ(M′,v) > 0holds
for everyv∈ [0,D](i.e., every1 ≤n≤M ′−1). Substituting M′= k+ M0 (k≥ 0) produces
polynomials with strictly positive constant terms and all nonnegative coefficients ink (tabulated
explicitly in Table 4 of Appendix A) at the following thresholds:
• BranchG(M0 = 4): both15 −κ6 and6 −(κ6−κ2
4)have −C(k+4) >0(Lean 4 Theorems 5–6).
•BranchR 4 (M0 = 6): both have−C(k+ 6)>0(Lean 4 Theorems 7–8).
•BranchR 6 (M0 = 9): both have−C(k+ 9)>0(Lean 4 Theorems 9–10).
• Branch R3:15 −κ6 has −C(k+ 12) >0( M0 = 12, Lean 4 Theorem 11);6−(κ6 −κ2
4)has
−C(k+ 27)>0(M 0 = 27, Lean 4 Theorem 12).
All remaining finite cases below these thresholds—namelyM′= 2on R4, M′= 3on R6 (l= 1:
κ4 = 3/2,κ6 = 9/4,κ6 −κ2
4 = 0) and R3 (l = 2: κ4 = 3/2,κ6 = 11/4,κ6 −κ2
4 = 1/2; branch
Gdoes not occur atM′= 3), M′= 4on R4 (including(4 ,2,2)in certificate C01), M′= 6on
R6, andM′∈{6,9,12,15,18,21,24}on R3 (all genericM′∈{4,5}cases are already covered by
Theorems 5–6)—are closed exhaustively in Lean 4 Theorem 13 and independently cross-checked
for allM′∈{2,..., 12}in our exact rational test suite. Finally,κ6 −κ2
4 = ET[(x3
T −κ4xT)2] ≥0
by nonnegativity of variance, and atn= M′/2the leading powers ofM′give κ4 = 3 −O(1/M′),
κ6 = 15−O(1/M ′), andκ6 −κ2
4 = 6−O(1/M ′).
3 Theorem B: Optimal-Projection Infidelity Bound and Certified
Single-Round Amplification
Let xT := λT/µ1/2
2 so thatET[x2
T] = 1, ET[x4
T] = κ4, andET[x6
T] = κ6, and sets:= τµ1/2
2 >0.
By Eq. (S13) of [1],
psucc(s) =E T[sin2(sxT)], F(s) =
(
ET[xT sin(sxT)]
)2
ET[sin2(sxT)] .(9)
The critical inefficiency of Eq. (S9) in [1] is geometric: it bounds1−F (s)by the squared distance
from sin(sxT)to the unscaled vector sxT, which retains the full collinear cubic contraction
4

--- Page 5 ---
Figure 1: Theorem A exact Dicke-state moments across system sizesM′and resonance branches.
(a) Exact kurtosisκ4 ≤3achieves a4 ×improvement over the Hoeffding boundκ4 ≤12of [1],
attaining equality uniquely at(M′,n,l ) = (4,2,2)(orange diamond). (b) Exact normalized sixth
momentκ6 <15(8×sharper than120) and orthogonal-projection varianceκ 6 −κ2
4 <6.
−1
6 s3κ4xT and therefore incurs coefficientκ6/36instead of the orthogonal residual(κ6 −κ2
4)/36.
Optimizing the scalar projection factor(1−a)cancels the collinear component completely.
Theorem B(Optimal-Projection Uniform Infidelity and CertifiedK = 1Amplification).For
everyM ′≥2,1≤n≤M ′−1,1≤l≤M ′−1, and everys∈(0,
√
2):
(i)Universal non-asymptotic infidelity bound:
1−F(s)≤
s4
36 (κ6 −κ2
4) + s6
360 κ4κ6
(
1− κ4
6 s2)2 ≤ s4(4 + 3s2)
6(2−s 2)2 .(10)
(ii)Two-sided bare success-probability envelope:
s2 −s4 ≤s 2 −κ4
3 s4 ≤p succ(s)≤s 2.(11)
(iii) Zero-overshoot single-round Grover certification:Whenever0 <s< 1/2, we have
psucc(s) ≤s2 <1/4, and one round of amplitude amplification (K = 1) satisfies uniformly
over all(M ′,n,l):
p(1)
amp(s) =psucc(s)
(
3−4p succ(s)
)2 ≥(s 2 −s4)
(
3−4(s 2 −s4)
)2.(12)
(iv)Concrete operating points and universalε-schedule:
• At Asari et al.’s Eq. (12) points = 0 .495: psucc ∈[0.184988,0.245025] ⊂(0,1/4)
(37.94×sharper than Eq. (S15)’s0.004876), p(1)
amp ≥0.944884(21 .8×sharper than
0.0433), and1−F≤0.015383(13.01×sharper than Eq. (S9)’s0.200124).
• At s= 0.45:1 −F≤ 0.009746 <0.01uniformly for all( M′,n,l )with psucc ≥0.161494
(25.84×sharper than Eq. (S11)’s
√
0.01/16 = 0.00625) andp(1)
amp ≥0.894907.
• For any targetε∈ (0,0.01], settings(ε) = (4ε)1/4 rigorously certifies1 −F≤ε and
psucc ≥2√ε−4ε (8×sharper asε→ 0than Eq. (S11)’s intermediate√ε/4 −ε/4, and
32×sharper than its final√ε/16bound).
5

--- Page 6 ---
Proof. For any nonzero vectorsu1,u2,1 −|⟨u1|u2⟩|2/(∥u1∥2∥u2∥2) ≤∥u2 −u1∥2/∥u1∥2. Taking
u2 = sin(sxT)and u1 = (1 −a)sxT with a∈ [0,1), note first thatu2 ̸= 0for all s∈ (0,
√
2):
for s∈ (0,1)this follows from psucc ≥s 2 −s4 > 0, while fors∈ [1,
√
2)having sin(sxT) ≡0
would force|xT|≥π/s wherever xT ̸= 0and thus κ4 = ET[x4
T] ≥(π2/s2)ET[x2
T] > π2/2 > 3,
contradicting Theorem A. We expand
(
siny−(1−a)y
)2 =a2y2 −2ay(y−siny) + (y−siny) 2.(13)
By repeated integration of1−cost≥ 0on t≥ 0(and odd symmetry), two elementary pointwise
inequalities hold globally forall y∈R :( y−siny )2 ≤y 6/36and y(y−siny ) ≥y 4/6 −y6/120.
Sincea≥0, substitutingy=sx T and takingET[·]gives
ET
[
(sin(sxT)−(1−a)sx T)2]
≤s 2
[
a2 −a
3s2κ4 +
(1
36 + a
60
)
s4κ6
]
.(14)
Dividing by∥u1∥2 = (1 −a)2s2 and choosinga= κ4
6 s2 ∈(0,1)(valid for s2κ4 <6, which holds for
all s<
√
2 since κ4 ≤3) cancelsa2 −a
3 s2κ4 = −s4
36 κ2
4 and yields the first inequality in(10). Its
numerator is strictly increasing inκ6 −κ2
4, κ4, andκ6, while its denominator(1−κ4
6 s2)2 is strictly
decreasing inκ4; inserting the Theorem A uniform boundsκ4 ≤3, κ6 < 15, and κ6 −κ2
4 < 6
immediately produces
s4
36 ·6 + s6
360 ·45
(
1− s2
2
)2 =
s4
6 + s6
8
(2−s2)2
4
= s4(4 + 3s2)
6(2−s 2)2 .(15)
For (ii), the pointwise inequalitiesy2 −y4/3 ≤sin 2 y≤y 2 (∀y∈R ) together withET[x2
T] = 1
and κ4 ≤3give (11). For (iii), recall that one Grover iterate maps success probabilityp= sin2 θ
top (1)
amp = sin2(3θ) =p(3−4p) 2 [3]. For0≤p 1 ≤p2 ≤1/4, the cubic identity
p2(3−4p 2)2 −p1(3−4p 1)2 = (p2 −p1)
[
(3−4p 1 −4p2)2 −16p1p2
]
≥0(16)
holds because3 −4p1 −4p2 ≥1 ≥√16p1p2 (formalized in Lean 4 Theorem 14). Sinces< 1/2
implies psucc(s) ≤s2 <1/4, monotonicity immediately yields(12). Finally, part (iv) follows by
exact rational evaluation ats= 99/200and s= 9/20(Lean 4 Theorem 15; certificatesC09–C10),
and forε∈ (0,0.01]with s= (4ε)1/4 we haves2 = 2√ε≤ 1/5, whence 4+3s2
6(2−s2)2 ≤ 4.6
6·3.24 < 1
4 and
thus1−F≤s 4/4 =ε.
4 Theorem C: Collision-Free Subquadratic Reversible Routing
forΦ −1
In the DWC and Onsager scar models, the routing isometryΦ−1 = D◦S◦R maps a weight-
n computational-basis bitstring x = ( x0,...,x M′−1) ∈ {0,1}M′
n (n≥ 1) with excitations at
0 ≤q 1 <···< q n < M′ by shifting thek-th excitation right byk− 1sites (inserting a spacer
|0⟩after every|1⟩for Onsager, lengthL= M′+ n; and outputting the non-adjacent weight-n
configuration onM′+ n−1qubits for DWC). Observe first an exact structural unification: in
the Onsager expansiony = ROns(x) ∈{0,1}M′+n (0 ↦→0,1 ↦→10), the final qubityM′+n−1 is
identically0for every weight- n input withn≥ 1(if xM′−1 = 1, it is the trailing spacer of10;
if xM′−1 = 0, it is the routed bitxM′−1 = 0), and the prefixy[0..M′+ n−2]has its n ones at
exact DWC positionsqk + k−1. Thus thesameOnsager router ROns on L= M′+ n data wires
directly implements RDWC with bit[L− 1]returning deterministically to |0⟩as a single clean
ancilla! Let cj := ∑
i<j xi ∈{0,...,n} be the exclusive prefix weight and setB := ⌈log2(n+ 1)⌉
so that0 ≤c0 ≤c1 ≤···≤c M′−1 ≤n< 2B with zero counter overflow (including whenn is a
power of two).
6

--- Page 7 ---
Figure 2: Theorem B non-asymptotic performance guarantees. (a) Optimal-projection uniform
infidelity upper bound closely tracks the Gaussian limit Eq. (S14), improving by13 .0×at
s = 0 .495and rigorously certifying1 −F≤ 0.00975 < 0.01at s = 0 .45. (b) Bare success
probability psucc ≥s2 −s4 (37.9×sharper ats= 0.495) and zero-overshoot single-round Grover
probabilityp(1)
amp ≥0.945(21.8×jump over Eq. (S15)).
Theorem C(Collision-Free Reversible MSB-to-LSB Binary-Shift Router).LetL= M′+ n and
B = ⌈log2(n+ 1)⌉. LetR act on a data registerbit[0..L−1]initialized to( x0,...,x M′−1,0,..., 0)
paired withB-bit shift ancillas reg[0..L− 1][0..B− 1]and2 B temporary prefix-counter/carry
scratch ancillas, all initialized to|0⟩. Consider the three-stage reversible circuit:
1. Prefix-shift initialization:Sweep j = 0,...,M ′−1, XORing theB-bit running counter
cj = ∑
i<j xi into reg[j]via B CNOTs and incrementing the counter controlled onbit[j]via
a standard ripple-carry incrementer (B counter+ B carry ancillas; at most2B Toffolis per
site, ≤2BM′ Toffolis total), then uncomputing the counter from the fixed known weightn
via≤BX gates.
2. MSB-to-LSB radix routing:Forb= B−1,B− 2,..., 0, iteratep in decreasing order
fromL−1−2 b down to0and apply:
(a)B Fredkin (CSWAP) gates controlled onreg[p][b]swapping
(
bit[p],{reg [p][r]}r̸=b
)
with(
bit[p+ 2 b],{reg[p+ 2 b][r]}r̸=b
)
;
(b) one unconditionalSWAPgate on
(
reg[p][b],reg[p+ 2 b][b]
)
.
3. Spacer-masked uncomputation:Sweep p= 0,...,L− 1using the same B-bit running
counter Pp = ∑
q<pbit[q]( ≤2B Toffolis per site): atp= 0XOR P0 = 0(no-op), and at
p≥ 1XOR Pp into reg[p]controlled on bit[p− 1] = 0( B Toffolis per site, total≤3BL
Toffolis), then reset the counter from the fixed weightn.
Then for every weight-ninputx∈{0,1} M′
n (n≥1):
(i) Universal collision freedom:At every radix stage b∈{ 0,...,B− 1}, the pre-stage
positions p(b)
j = j+ ⌊cj/2b+1⌋2b+1 and post-stage positionsp(b−1)
j = j+ ⌊cj/2b⌋2b satisfy
p(r)
j′ −p(r)
j ≥j ′−j≥ 1for all j <j′(r∈{b,b− 1}), and every target control bitreg[p+ 2b][b]
is strictly0prior to each swap step.
(ii) Exact unified Onsager/DWC output and zero ancilla leakage:Upon completion,
bit[0..L−1] = ROns(x)identically, bit[0..L−2] = RDWC(x)with bit[L−1] = |0⟩determin-
istically, and allLB shift ancillas plus2B temporary prefix-counter/carry ancillas return
deterministically to|0⟩.
7

--- Page 8 ---
(iii)Subquadratic 3-qubit gate complexity:Stage 2 uses exactly
NFredkin(L,B) =B
(
BL−(2 B −1)
)
=O(Mlog 2 n)(17)
Fredkin gates (andBL−2B + 1plain SWAPs), while Stages 1 and 3 add at mostNS1+S3 ≤
B(2M′+ 3L) = O(Mlogn )Toffoli gates, giving total 3-qubit countNtotal ≤NFredkin(L,B) +
NS1+S3 =O(Mlog 2 n)for both Onsager and DWC. Consequently:
• Against theunprunedΘ( M2)Fredkin conveyor of [1] (whose fixed gate sequence depends
only on M), the router achievesΘ(M/log 2 n)asymptotic gate reduction across all
intermediate indices3≤n≤M ′−2.
• Against theprunedsitewise-displacement lower benchmark Ndisp(M′,n) = 1
2 n(2M′−
n−1) = Θ(nM′), the router achievesΘ(n/log 2 n)asymptotic reduction in every super-
polylogarithmic sectorn= ω(log2 n)(in particular at every fixed fillingn/M′= ρ∈
(0,1); for fixed smalln≤ 2B2, Ndisp is already linear inM′). At half filling (n= M′/2,
L= 3M′/2), Stage-2 Fredkins crossNdisp permanently atM′= 184(12 ,635 <12,650,
reaching2 .74×at M′= 1024and7 .53×at M′= 4096), while the conservative total
3-qubit count Ntotal (including all Stage-1/3 Toffolis) crossesNdisp permanently at
M′= 382(54 ,496 <54,626, reaching1.87×at M′= 1024,3 .17×at M′= 2048, and
5.45×atM ′= 4096).
Proof. Since j <j′ =⇒c j ≤cj′ and integer division by2r+1 is monotone,⌊cj/2r+1⌋≤⌊c j′ /2r+1⌋,
so
p(r)
j′ −p(r)
j = (j′−j) +
(⌊cj′
2r+1
⌋
−
⌊ cj
2r+1
⌋)
2r+1 ≥j ′−j≥1(18)
holds for everyr≥− 1(Lean 4 Theorem 16), hence both before (r= b) and after (r= b−1) stage
b. Thus no two items collide after stageb. Consequently, prior to stageb, if an active item atphas
reg[p][b] = 1, slotp+ 2b cannot hold any non-moving item (as that would collide with the moved
item after stageb); it can only be empty or hold another mover withreg[p+ 2b][b] = 1. Iterating p
in decreasing order processesp+ 2b before p, so by downward inductionreg[p+ 2b][b] = 0and the
entire bundle atp+ 2b is(0 ,0)whenever reg[p][b] = 1. Step 2(a) therefore moves allB non-control
qubits reversibly top+ 2b, and becausereg[p+ 2b][b] = 0, the unconditional SWAP in Step 2(b)
maps(1 ,0) ↦→(0,1)and(0 ,0) ↦→(0,0), completing the exact reversible shift of the(1 +B)-qubit
bundle without extra ancillas.
After stageb= 0, every sitej sits atq(j) = j+ cj carrying( xj,cj), and every unoccupied slot
is a spacer carrying(0,0). Because cj′ ≥cj + xj, we haveq(j) + xj <q(j′)for all j <j′(Lean 4
Theorem 17): thus wheneverxj = 1, slot q(j) + 1is strictly empty (spacer0), no two1s are
adjacent, and a slotpis a spacer iffp≥ 1∧bit[p−1] = 1. Moreover, the final slotL−1 = M′+n−1
always holds0for n≥ 1(either the trailing spacer ofxM′−1 = 1or the routed bitxM′−1 = 0),
so bit[0..L−2] = RDWC(x)identically. Because all spacers carrybit = 0, the output prefix sum
Pq(j) = ∑
q<q(j) bit[q]equals cj identically on every non-spacer slot, and sincePp ≤n< 2B the B-
bit running counter never overflows. Stage 3 therefore resets allLB shift ancillas deterministically
to |0⟩, and the fixed known weightn resets theB-bit counter to|0⟩at the end of both Stages 1
and 3. Summing B(L− 2b)over b = 0,...,B− 1gives NFredkin(L,B) = B(BL− (2B −1)),
while the ripple-carry prefix sweeps use at most2BM′ Toffolis in Stage 1 and3BL Toffolis in
Stage 3 (increment plusbit[p− 1] = 0-controlled copy). Comparing against the conservative
pruned displacement budget Ndisp(M′,n) = ∑M′−1
j=1 min(j,n) = 1
2 n(2M′−n− 1) = Θ( nM′)
(strictly below the unprunedΘ(M2)conveyor of [1], which uses≈7
8 M′2 Fredkins at half filling)
establishes both the asymptoticΘ(n/log 2 n)gain for n = ω(log2 n)and the exact half-filling
crossovers atM′= 184(Stage 2, Lean 4 Theorem 18) andM′= 382(total 3-qubit gates, where
34,632 + 19,864 = 54,496<54,626).
Remark1 (Depth, space–time trade-offs, and in-place DWC variant).In Stage 2, the2b congruence
classes modulo2 b are disjoint, yielding∑B−1
b=0 ⌊(L− 1)/2b⌋< 2L sequential bundle-shift steps.
8

--- Page 9 ---
Figure 3: Theorem C subquadratic reversible routingΦ−1 vs. the conservative pruned displacement
benchmark Ndisp = 1
2 n(2M′−n− 1)of [ 1]. (a) Exact Stage-2 Fredkin counts at half filling
(n = M′/2, Onsager L = 3 M′/2) cross Ndisp permanently at M′ = 184(12 ,635 < 12,650),
reaching2 .74×reduction atM′= 1024and7 .53×at M′= 4096(including all Stage-1/3 Toffolis,
total 3-qubit gates cross atM′ = 382and reach5 .45×at M′ = 4096). (b) Stage-2 Fredkin
reduction ratio across constant filling fractionsn/M′∈{1/2,1/4,1/8}.
Because each bundle shift executesB Fredkin gates sharing the single control qubitreg[p][b]plus
one SWAP, the elementary circuit depth without control fan-out is<2(B+ 1)L= O(Mlogn )
(reducible toO(Mlog logn )with per-step O(log logn)-depth control fan-out acrossB targets)
using( L+ 2)B = O(Mlogn )clean ancillas (plus one deterministic|0⟩trailing wirebit[L−1]for
DWC). If one instead omits the single trailing DWC wire and routes in-place onLDWC = M′+n−1
wires withsj = min(cj,n− 1)and BDWC = ⌈log2 n⌉(as also verified in certificateC14), Stages 1
and 3 must still use aB = ⌈log2(n+ 1)⌉-bit running counter plus an equality flag[Pp = n]to avoid
overflow whenn= 2BDWC, raising Stage-1/3 overhead to≤5B(M′+ LDWC)Toffolis—making the
unified 1-ancilla construction of Theorem C strictly simpler and lower in total 3-qubit gate count.
Note also that Stage 2’s in-place decreasing-psweep cannot itself be parallelized to polylogarithmic
depth (a contiguous run ofΘ(M)sites with odd cj forms aΘ( M)-length dependency chain at
b= 0); achievingO(log2 M)depth instead requires replacing Stage 2 with an out-of-place butterfly
or parallel monotone-packing network. For small NISQ chains or fixed constantn≤ 2B2, a pruned
conveyor or particle ladder uses fewer gates, whereas in the fault-tolerant extensive-filling regime
(n/M′= ρ> 0; M′≥184for Stage-2 Fredkins andM′≥382for total 3-qubit gates atρ= 1/2)
Theorem C achieves a strictly growingΘ(M/log 2 M)gate advantage over both unpruned and
pruned conveyors.
5 Formal Verification in Lean 4.35.0 and Exact Rational Certifi-
cates
To eliminate any possibility of algebraic sign errors, floating-point rounding artifacts, or hidden
ancilla leakage, every algebraic core of Theorems A–C is independently verified at two layers:
1. Constructive Lean 4.35.0 formalization (lean/QmbsDickeSharp.lean):Compiles with
0 sorry, 0 warnings, andzero Classical.choice (all 18 theorems depend exclusively
on axioms⊆{propext,Quot.sound}, with 3 theorems axiom-free). We implement a self-
contained univariate integer polynomial reflection engine (evalP, addP, mulP, compP) so that
all eight concave-quadratic positivity theorems across branchesG,R4,R6,R3 (Theorems 5–
12) and the complete finite-threshold closure (Theorem 13) verify constructively in seconds
9

--- Page 10 ---
Table 2: Representative exact rational certificates inQMBS-DICKE-SHARP-1.0 (all 16 SHA-256
verified by the AST-audited zero-float verifier).
ID Class Parameters Exact Certified Result
C01 moment(4,2,2)(R 4)κ 4 = 3(unique eq.),κ 6 = 9, var= 0
C05 moment(12,6,1)(G)κ 4 = 11/4 = 2.75, var= 15367/3888≈3.9524
C06 moment(24,12,16)(R 3)κ 4 = 23/8 = 2.875, var= 23805/4864≈4.8941<6
C08 moment(1000,500,1)(G)κ 4 = 2.9970,κ 6 = 14.9550, var= 5.9730
C09 op_points= 99/200 = 0.495p succ ≥0.18499(37.94×),p (1)
amp ≥0.94488,1−F≤0.01538
C10 op_points= 9/20 = 0.45 1−F≤0.00975<0.01,p succ ≥0.16149(25.84×)
C13 routerOnsager,M ′ = 6(64 states) 0 collisions, 0 ancilla leak, max 87 Fredkins
C14 routerDWC,M ′ = 6(63 states) 0 collisions, 0 ancilla leak, max 78 Fredkins
C15 routerOnsager,M ′ = 8,n= 4(70 states) Asari Fig. S2(b) exact unitary replay PASS
C16 routerM ′ ∈{128...4096},n=M ′/2 1.001×(184),2.74×(1024),4.50×(2048),7.53×(4096)
alongside exact sum-of-squares kurtosis bounds (Theorems 2–4), Grover monotonicity
(Theorem 14), operating-point inequalities (Theorem 15), and MSB-to-LSB collision freedom,
spacer isolation, and exact crossover/scaling bounds (Theorems 16–18). We explicitly
delineate the formalization boundary: Lean 4.35.0 proves the algebraic integer/natural-
number cores of Theorems A–C, while the real-analytic trigonometric Taylor inequalities
(y−siny)2 ≤y6/36and y(y−siny) ≥y4/6−y6/120in Theorem B are established analytically
in Section 3.
2. AST-audited zero-float exact rational verifier (src/qmbs_dicke_verifier.py):Per-
forms an AST self-audit rejecting all floating-point/complex literals,/ and ** operators,
pow() calls, and floating-point libraries, then independently replays 16 SHA-256 certificates
(C01–C16, Table 2) andMANIFEST.sha256, including exhaustive gate-by-gate unitary circuit
replay of Theorem C on all 64 Onsager states (M′= 6), all 63 DWC states (M′= 6), and
all 70 half-filling states (M′= 8,n = 4) with zero-collision and zero-ancilla-leak assertions.
The test suite (tests/test_qmbs_dicke.py) passes 53/53 tests, including 30 adversarial
forgery attacks (boolean-as-int smuggling across moment/operating-point/router fields, tam-
pered moments, overshoot operating points, router metadata tampering, and AST float/pow
injection).
6 Conclusion
By replacing with-replacement Hoeffding relaxations with exact without-replacement Dicke-state
moments, optimizing the linear projection in block-encoded infidelity estimation, and exploiting
monotone prefix-shift collision freedom in radix routing, we have resolved all three theoretical and
algorithmic gaps in the unified Dicke-based AQMBS preparation framework of [1]. The resulting
closed-form bounds rigorously certify single-round Grover amplification (p(1)
amp ≥0.94488) across
all chain lengths and excitation sectors, while theO(Mlog 2 n)-gate MSB-to-LSB router eliminates
the quadratic routing bottleneck for constrained scar models in the fault-tolerant regime.
Reproducibility and Transparency.All Lean 4.35.0 proofs, AST-audited zero-float verifi-
cation code, 16 SHA-256 certificates, test suites, and figure scripts are publicly archived under
the MIT license (manuscript and figures under CC-BY-4.0) athttps://github.com/lluiser
iksson/qmbs-dicke-sharp-moments-routing . Computational prototyping, Lean proof-script
drafting, and manuscript editing were assisted by Google Antigravity; all mathematical proofs,
formal checks, and verification outputs were independently validated by the author.
10

--- Page 11 ---
References
[1] Yuki Asari, Masaya Kunimi, and Tetsuro Nikuni. Unified preparation of exact and asymptotic
quantum many-body scars from Dicke states.arXiv preprint arXiv:2611.33987, 2026.
[2] Andreas Bärtschi and Stephan Eidenbenz. Deterministic preparation of Dicke states. In
Fundamentals of Computation Theory (FCT 2019), volume 11651 ofLecture Notes in Computer
Science, pages 126–139. Springer, 2019.
[3] Gilles Brassard, Peter Høyer, Michele Mosca, and Alain Tapp. Quantum amplitude amplifica-
tion and estimation.Contemporary Mathematics, 305:53–74, 2002.
[4] Lorenzo Gotta, Sanjay Moudgalya, and Leonardo Mazza. Asymptotic quantum many-body
scars.Physical Review Letters, 131(19):190401, 2023.
[5] Wassily Hoeffding. Probability inequalities for sums of bounded random variables.Journal of
the American Statistical Association, 58(301):13–30, 1963.
[6] Masaya Kunimi, Yasuyuki Kato, and Hosho Katsura. Systematic construction of asymptotic
quantum many-body scar states and their relation to supersymmetric quantum mechanics.
Physical Review Research, 7(4):043107, 2025.
A Explicit Sixth-Moment Partition Sums and Branch Polynomi-
als
ForcompletestandaloneverifiabilityofTheoremA(ii)–(iii)directlyfromthismanuscript, wedisplay
all 11 distinct-index partition sumssλ (forp 1 = 0) enteringµ6 = 64 ∑6
r=1 arΣr(p2,p3,p4,p6):
s6 =p6, s 5,1 =−p6,
s4,2 =p4p2 −p6, s 3,3 =p2
3 −p6,
s4,1,1 = 2p6 −p4p2, s 3,2,1 = 2p6 −p4p2 −p2
3,
s2,2,2 =p3
2 −3p4p2 + 2p6, s 3,13 =−6p6 + 3p4p2 + 2p2
3,
s2,2,1,1 =−6p6 + 5p4p2 + 2p2
3 −p3
2, s 2,14 = 24p6 −18p4p2 −8p2
3 + 3p3
2,
s16 =−120p6 + 90p4p2 + 40p2
3 −15p3
2,
withΣ 1 = s6,Σ 2 = 6s5,1 +15s4,2 +10s3,3,Σ 3 = 15s4,1,1 +60s3,2,1 +15s2,2,2,Σ 4 = 20s3,13 +45s2,2,1,1,
Σ5 = 15s2,14 , andΣ 6 =s16 (satisfying ∑6
r=1 Σr =p6
1 = 0identically).
Substituting (2), clearing positive denominators (2u2(M′−3)(M′−2)and4 u2(M′−3)(M′−2)2
on G; u2(M′−5)(M′−3)and u2(M′−5)(M′−3)2 on R4;4 u2(M′−5)(M′−4)(M′−2)and
2u2(M′−5)(M′−4)(M′−2)2 on R6,R3), and settingu= (M′2 −v)/4yields the exact quadratic
numerators Q(M′,v) = A(M′) +B(M′)v+C(M′)v2 (scaled by16) in Table 3 and their manifestly
positive shifted expansions atM′=k+M 0 (k≥0) in Table 4.
11

--- Page 12 ---
Table 3: Exact branch polynomialsQ(M′,v) = A(M′) + B(M′)v+ C(M′)v2 for15 −κ6 and
6−(κ 6 −κ2
4)(writingMforM ′).
Branch Bound Exact PolynomialsA(M),B(M),C(M)
G15−κ 6 A= 90M5 −530M4 + 980M3 −640M2 + 160M;B= 60M 2 −180M;C= 150−90M
G6−varA= 108M 6 −880M5 + 2676M4 −3760M3 + 2448M2 −640M;
B= 48M3 −240M2 + 288M;C=−108M 2 + 336M−276
R4 15−κ6 A= 30M5 −286M4 + 760M3 −512M2 + 128M;B= 60M 3 −180M2 −120M;
C= 210−90M
R4 6−varA= 18M 6 −228M5 + 1002M4 −1848M3 + 1344M2 −384M;
B= 36M4 −192M3 + 228M2 + 120M;C=−54M 2 + 228M−270
R6 15−κ6 A= 180M6 −2124M5 + 8592M4 −13944M3 + 8688M2 −2112M;
B=−840M 2 + 2280M;C=−180M 2 + 1500M−2040
R6 6−varA= 54M 7 −756M6 + 4026M5 −10308M4 + 13320M3 −8304M2 + 2112M;
B=−36M 4 −24M3 + 612M2 −840M;C=−54M 3 + 552M2 −1314M+ 960
R3 15−κ6 A= 180M6 −2076M5 + 8208M4 −12936M3 + 7632M2 −1728M;
B=−80M 4 + 400M3 −1400M2 + 2520M;C=−100M 2 + 1340M−1960
R3 6−varA= 54M 7 −732M6 + 3786M5 −9420M4 + 11784M3 −7056M2 + 1728M;
B=−40M 5 + 244M4 −704M3 + 1292M2 −1080M;
C=−14M 3 + 392M2 −1114M+ 880
Table 4: Shifted coefficient vectors[c0,c1,...,c d]of P(k) = ∑ cjkj at M′= k+ M0 (k≥ 0) for
Q0 = A(M′), Qend = Q(M′,(M′−2)2), and−C(M′). Every entry is strictly positive (certifying
Theorem A(ii)–(iii) via (8) for allM′≥M0).
Branch BoundM 0 Shifted Positive Coefficient Vectors (Q0,Q end,−C) ink=M ′ −M0
G15−κ 6 4Q 0:[9600,21600,17840,6900,1270,90];Q end:[7200,15600,11600,3600,400];−C:
[210,90]
G6−var4Q 0:[22272,60672,65744,36496,10996,1712,108];Q end:
[13248,35328,35696,17296,4048,368];−C:[660,528,108]
R4 15−κ6 6Q 0:[9120,23360,16192,4696,614,30];Q end:[16800,29120,15232,3136,224];−C:
[330,90]
R4 6−var6Q 0:[12384,44256,41952,17880,3882,420,18];Q end:
[21600,44640,32064,10560,1632,96];−C:[846,420,54]
R6 15−κ6 9Q 0:[17130960,15915252,6038652,1199328,131712,7596,180];Q end:
[7311360,6162432,2033472,328848,26112,816];−C:[3120,1740,180]
R6 6−var9Q 0:[35668080,38142636,17251014,4281102,630132,55056,2646,54];Q end:
[12042240,11870208,4799232,1020096,120384,7488,192];−C:[5520,4500,906,54]
R3 15−κ6 12Q 0:[169827840,104825664,26747568,3612408,272448,10884,180];Q end:
[53123840,29200864,6363728,687568,36848,784];−C:[280,1060,100]
R3 6−var27Q 0:[330812910000 ,92768460300,11141381106,742858734,29698140,711888,9474,54];
Qend:[37626160000,9250612800,946863456,51648432,1583472,25872,176];−C:
[18992,10564,742,14]
12
