# Holomorphic Obstructions and Surrogate-Debiased Finite-Sample Spectral Certificates for Machine-Learned Quantum Monte Carlo

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-2YMSYGRR9V9TBAJ8` (v1)  
**Intake Receipt:** `SUB-405F1872B2764D01`  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/qcqmc-spectral-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `7347d7cf703b6f9c7ff6a541f128be70ecf374509e9360be3d8c2439395fc09b`

## Abstract

Recent hybrid quantum-classical quantum Monte Carlo (QC-QMC) workflows accelerate classical postprocessing of randomized quantum measurements by compressing matchgate-shadow overlaps into differentiable machine-learning surrogates satisfying Slater-determinant equivariance f(Phi U) = det(U) f(Phi). We resolve two mathematical hazards introduced by such surrogates: non-physical bias and uncertified statistical error. First, we prove an elementary Grassmannian characterization (Theorem 2.1): for 1 <= eta < N, a C^1 GL(eta, C)-equivariant surrogate represents a physical fermionic trial state if and only if dbar f = 0, equivalently if and only if the anti-holomorphic Green's defect G^{dbar} vanishes identically, equivalently if and only if f annihilates all finite linear Slater-determinant syzygies. Left-projector affine backflow G0 + P_Phi A collapses to a fixed Slater determinant, whereas general affine-trace or nonlinear backflow neural quantum surrogates leave the physical Hilbert space, obey a sharp distance floor eta_Pl(f; S) = ||(I - S S^+) f_S^*||_2, and incur representation-dependent mixed-estimator bias even on zero-walker-error decompositions of the exact ground state (including unphysical energies strictly below E0). Second, we prove a sharp Mixed-Energy Variational-Boost Law and generalize it to Surrogate-Anchored Block Hausdorff Certificates for both ground-state upper bounds and oracle-free two-edge visible spectral-gap exclusion using only classical moments a_k and distribution-free Median-of-Means confidence boxes on linear shadow cross-moments Re(b_k) (with exact 3-design variance bound <= 4 a_{2k} for arbitrary complex states), paired with Prediction-Powered Inference (PPI) walker debiasing. Core algebraic, complex-projection, variational-boost, and complex spectral-measure conic-dual soundness theorems (16 symbols) are formally verified in Lean 4.35.0 (0 sorry, 0 Classical.choice, zero external dependencies), and all 4-site Hubbard dual certificates are verified in exact rational arithmetic (Q) via symmetry-checked pivoted LDL^T factorization over explicit rational moment enclosures.

## Full Extracted Text

--- Page 1 ---
Holomorphic Obstructions and Surrogate-Debiased
Finite-Sample Spectral Certificates for
Machine-Learned Quantum Monte Carlo
Lluis Eriksson*
November 24, 2026
Abstract
Recent hybrid quantum–classical quantum Monte Carlo (QC-QMC) workflows acceler-
ate classical postprocessing of randomized quantum measurements by compressing noisy
matchgate-shadow overlaps into differentiable machine-learning surrogates fθ(Φ) satisfying
Slater-determinant equivariance fθ(ΦU) = det(U)fθ(Φ) (Jiang et al., arXiv:2611.08151,
Nov. 2026). While this removes the O(N3NsNwNτ ) shadow-evaluation bottleneck, it intro-
duces two uncharacterized mathematical hazards: non-physical surrogate bias and uncertified
statistical error. We resolve both with exact, machine-verified theory. First, we give an
elementary, self-contained Grassmannian characterization (Theorem 2.1): for 1 ≤η < N,
a C1 GL(η,C )-equivariant overlap surrogate represents a physical fermionic trial state
|Ψ⟩ ∈Vη CN if and only if ¯∂fθ ≡ 0, equivalently if and only if the anti-holomorphic Green’s
defect G¯∂(Φ) vanishes identically, equivalently if and only if fθ annihilates all finite linear
Slater-determinant syzygies (whereas for η = N equivariance alone suffices). Left-projector
affine backflow G0 + PΦA collapses identically to a fixed Slater determinant (Remark 2.3),
whereas general affine-trace or nonlinear backflow neural quantum surrogates (NQS) leave the
physical Hilbert space, satisfy an exact sharp distance floorinf|Ψ⟩ ∥fS−vΨ∥2 = ∥(I−SS +)f∗
S∥2
(Theorem 2.4), and incur representation-dependent mixed-estimator bias even on zero-walker-
error decompositions of the exact ground state |Ψ0⟩—including unphysical energies strictly
below E0 (Theorem 2.5, demonstrated analytically and numerically on two-site Hubbard
with zero error on computational-basis determinants yet −0.971 bias on rotated walkers).
Second, to turn noisy QC-QMC mixed overlap/energy data into rigorous spectral guarantees,
we prove a sharp, universalMixed-Energy Variational-Boost Law(Theorem 3.1): for any
HermitianH⪯E maxIand unit states (|Ψ sur⟩,|Ψ T ⟩) with|b 0|<1 andE sur < Emax,
E0 ≤E sur − |⟨Ψsur|(EsurI−H)|Ψ T ⟩|2
(Emax −E sur)(1− |b0|2) ,
requiring neither measurement of ⟨ΨT |H|ΨT ⟩ nor variationality of the raw mixed energy.
Generalizing to degree d≥ 0 yieldsSurrogate-Anchored Block Hausdorff Certificates(Theo-
rem 4.1) for both ground-state upper bounds and oracle-free two-edge visible spectral-gap
exclusion using only classical moments ak and distribution-free Median-of-Means confidence
boxes on linear shadow cross-moments Re(bk), paired with Prediction-Powered Inference
(PPI) walker debiasing (Proposition 4.2). All core algebraic, complex-vector projection,
variational-boost, and complex spectral-measure conic-dual soundness theorems are formally
verified in Lean 4.35.0 (zero sorry, zero custom axioms, zero external dependencies), and
all numerical dual certificates on a 4-site Hubbard benchmark are independently verified
in exact rational arithmetic ( Q) via symmetry-checked pivoted LDL⊤ factorization over
explicit rational moment enclosures.
* Independent researcher (Sweden). Research, zero-dependency Lean 4 formalization, exact rational certificates,
and reproducible benchmarks prepared with AI assistance (Google Antigravity) and publicly archived at https:
//github.com/lluiseriksson/qcqmc-spectral-certificates.
1

--- Page 2 ---
1 Introduction and Positioning
Quantum–classical hybrid quantum Monte Carlo (QC-QMC) [ 5, 12] uses a correlated quantum
trial state |ΨT ⟩ prepared on quantum hardware to guide classical phaseless auxiliary-field QMC
(AFQMC) walks over Slater determinants |ϕ(Φ)⟩. Using Clifford matchgate classical shadows
[10, 4], trial overlaps fT (Φ) = ⟨ΨT |ϕ(Φ)⟩ can be estimated without interactive quantum–classical
feedback, but re-evaluating shadows across Nw walkers and Nτ imaginary-time steps scales as
O(N3NsNwNτ ). In a landmark advance, Jiang et al. [ 6] compressed matchgate-shadow data
into differentiable machine-learning surrogates fθ(Φ)—specifically a backflow neural quantum
surrogate (NQS) on the complex Grassmannian and a nonorthogonal configuration interaction
(NOCI) surrogate—enabling chemically accurate 40-qubit hardware demonstrations on Google’s
Willow processor.
This paradigm shift raises two fundamental mathematical questions that are not addressed
by empirical benchmarking alone:
1. Physical representability and mixed-estimator validity:Jiang et al. [ 6, Eq. (S2.19)]
enforce Slater-determinant equivariance fθ(ΦU) = det(U)fθ(Φ) by passing the orthogonal
projectorP Φ = Φ(Φ†Φ)−1Φ† into a backflow networkG θ(PΦ). Does equivariance guarantee
that fθ represents a valid quantum trial state |Ψ⟩ ∈Vη CN ? If not, what happens to
the mixed energy estimator Eθ
mix, which is exact and unbiased for any physical trial state
regardless of overlap accuracy when walkers sample|Ψ 0⟩?
2. Finite-sample certified spectral bounds from linear quantum shadows:Standard
phaseless AFQMC with an ML surrogate has uncertified systematic bias (both phaseless
and surrogate-induced) and is non-variational. Can one convertonlylinear quantum-shadow
cross-overlaps Re⟨Ψsur|Tk|ΨT ⟩ anchored to a classical physical surrogate |Ψsur⟩ into non-
asymptotic, distribution-free, independently checkable upper bounds on E0 and oracle-free
visible spectral-gap certificates—without assuming Gaussian noise or measuring quadratic
quantum momentsc k =⟨Ψ T |Tk|ΨT ⟩?
Literature positioning and explicit boundaries.Recent operator-algebraic SDP hierar-
chies establish certified bulk spectral-gap upper bounds [ 11], lower-gap qubit certificates [ 8], and
Euclidean correlator bootstraps [ 2], assuming exact operator relations or noiseless correlators.
Conversely, finite-sample Wishart–Loewner Hausdorff certificates [ 3] handle unknown covariance
under Gaussian random sketches Z = ⟨g, u⟩⟨g, v⟩, explicitly noting as an open limitation that
Gaussian sketches are not tied to an experimentally direct quantum shadow protocol. Our
contribution bridges these lines while keeping all claims strictly bounded:
 We donotclaim a general lower bound on the full Hamiltonian mass gap; our two-edge localizer
certifies spectrum strictly inside (θ1, θ2) for the spectral measure visible to span{|Ψsur⟩,|ΨT ⟩}.
By choosing θ2 = θcert from a certified single-edge ground-state bound ( λ0 > θcert), the
certified eigenvalue in (θ1, θcert) is provably distinct from the ground state without any oracle
knowledge ofE 0.
 We donotclaim that Backflow NQS fails empirically in all regimes of [ 6]; rather, we establish
the exact geometric mechanism (non-holomorphicity ¯∂fθ ̸= 0) by which equivariant backflow
breaks mixed-estimator unbiasedness, provide sharp derivative-free and derivative-based
witnesses (ηPl andG ¯∂), and provide projection and PPI debiasing remedies.
 Our distribution-free finite-sample shadow benchmark simulates exact Born-rule global Haar
(3-design) shadows on C|0⟩ ⊕ HD; extending the identical Median-of-Means confidence-box
interface to Clifford matchgate shadows [ 10] simply replaces the exact complex-safe 3-design
variance bound 4a2k with the matchgate shadow variance boundO(
√
NlogN).
2

--- Page 3 ---
2 Holomorphic Obstructions on the Complex Grassmannian
Let 1 ≤η≤N be integers and let Mfull
N,η := {Φ ∈C N×η : rank(Φ) = η}. Each Φ = [ ϕ1, . . . , ϕη] ∈
Mfull
N,η defines an unnormalized Slater determinant |ϕ(Φ)⟩ := ϕ1 ∧ ··· ∧ϕη ∈ Vη CN whose
components in the lexicographic computational basis {eI : I∈
 [N]
η

} are the η×η minors
det(ΦI). Consequently, for any physical trial state|Ψ⟩ ∈Vη CN , the overlap functional
fΨ(Φ) :=⟨Ψ|ϕ(Φ)⟩=
X
I∈([N]
η )
Ψ∗
I det(ΦI)
is holomorphic in Φ and satisfiesGL(η,C)-equivariance:
f(ΦU) = det(U)f(Φ)∀Φ∈ M full
N,η,∀U∈GL(η,C).(1)
In [6, Eq. (S2.19)–(S2.22)], a backflow neural quantum surrogate takes the form
fθ(Φ) = det

Gθ(PΦ)†Φ

, P Φ := Φ(Φ†Φ)−1Φ† ∈Gr(η, N),(2)
which enforces (1) because PΦU = PΦ. Following [ 6, Eq. (S2.22)], on the nonvanishing locus
{f̸= 0}define the anti-holomorphic Green’s defect matrix
G
¯∂
pq(Φ) :=− 1
f(Φ)
ηX
k=1
∂f
∂Φ∗
pk
(Φ) Φ∗
qk,1≤p, q≤N.(3)
Theorem 2.1(Holomorphic Characterization of Equivariant Overlap Surrogates).Let1 ≤η≤
Nand letf:M full
N,η →Csatisfy(1).
(i) Full-filling boundary (η = N):Without any regularity assumption, f(Φ) = f(IN ) det(Φ) =
⟨Ψ|ϕ(Φ)⟩for the unique state|Ψ⟩=f(I N )∗e[N] ∈ VN CN .
(ii) Nontrivial regime (1 ≤η < N):Assume f∈C 1(Mfull
N,η,C). The following are equivalent:
(a) Physical representability:there exists a unique |Ψ⟩ ∈Vη CN such that f(Φ) = ⟨Ψ|ϕ(Φ)⟩
for allΦ∈ Mfull
N,η.
(b) Holomorphicity / vanishing Green’s defect: ∂f
∂Φ∗
pk
(Φ) = 0for allΦ ∈ Mfull
N,η and all( p, k);
equivalently,G ¯∂(Φ) = 0for allΦwithf(Φ)̸= 0.
(c) Pl¨ ucker linearity:for every finite family {(αj, Φj)}m
j=1 satisfying Pm
j=1 αj|ϕ(Φj)⟩ = 0inVη CN , one has Pm
j=1 αjf(Φj) = 0.
Moreover, the equivalence (a)⇔(c) holds for arbitrary functionsfwithoutC 1 regularity.
Proof.Part (i) is immediate sinceM full
N,N =GL(N,C), sof(Φ) =f(I N Φ) = det(Φ)f(IN ).
For Part (ii), (a)⇒ (b) and (a) ⇒ (c) follow directly from multilinearity and holomorphicity of
Φ 7→ P
I Ψ∗
I det(ΦI). For (c) ⇒ (a), the computational basis determinants {eI : I∈
 [N]
η

} belong
to {|ϕ(Φ)⟩ : Φ ∈ Mfull
N,η} and span Vη CN ; condition (c) states precisely that |ϕ(Φ)⟩ 7→f(Φ)
extends unambiguously to a linear functional on Vη CN , which equals ⟨Ψ|·⟩ for a unique
|Ψ⟩ ∈Vη CN .
We next verify the internal equivalence in (b). LetW(Φ) ∈C N×η have entries Wpk = ∂f
∂Φ∗
pk
(Φ),
so G¯∂(Φ) = − 1
f(Φ) W(Φ)Φ† on U := {f̸ = 0}. Since f∈C 1 is continuous, U is open. Because Φ
has full column rankη, Φ† admits the right inverse Φ(Φ†Φ)−1, whence G¯∂(Φ) = 0 ⇐⇒W (Φ) = 0
at every Φ ∈U . On int(Uc) we have f≡ 0, so W≡ 0 there as well. Since U∪int (Uc) is open
and dense inM full
N,η andWis continuous,G ¯∂ ≡0 onUis equivalent toW≡0 on all ofM full
N,η.
3

--- Page 4 ---
Finally, we give an elementary, self-contained proof of (b) ⇒ (a) without invoking Hartogs
extension or Borel–Weil–Bott. Fix I0 = {1, . . . , η}and partition Φ =
 A
B

with A∈C η×η
and B∈C (N−η)×η . On the dense open chart UI0 = {detA̸ = 0 }, equivariance (1) gives
f(Φ) = det(A) gI0(Z) with Z := BA−1 ∈C (N−η)×η and gI0(Z) := f
 Iη
Z

. Because
 Iη
Z

∈ Mfull
N,η
forevery Z∈C (N−η)×η , gI0 is entire on C(N−η)×η ; similarly gJ is entire for every chart J∈
 [N]
η

.
For any chart J = (I0 \{r} ) ∪{η + s} (1 ≤r≤η , 1 ≤s≤N−η ) and any Φ whose I0 \{r} rows
equal the standard basis rows e⊤
k (k̸ = r) and whose ( η + s)-th row is w⊤ ∈C 1×η with wr ̸= 0,
permuting row η + s into position r via a permutation matrix P gives P AJ = Iη + er(w⊤ −e ⊤
r ).
Hence detA J =±w r, and by the Sherman–Morrison formula,
(P AJ )−1 =I η +e r

1−w r
wr
e⊤
r −
X
k̸=r
wk
wr
e⊤
k

,(4)
so rowrof (P A J )−1 equals 1
wr
 
e⊤
r − P
k̸=r wke⊤
k

while every other rowk̸=requalse ⊤
k .
We apply (4) to three families of affine linest∈C(taking|t| → ∞):
1. Column-wise degree ≤ 1:Fix Z0, column r, and nonzero z∈C N−η , and set Z(t) = Z0 + tze⊤
r .
Pick s with zs ̸= 0 and J = ( I0 \ {r}) ∪ {η+ s}. On Φ( t) =
  Iη
Z(t)

, we have w(t)r =
(Z0)sr + tzs = Θ(|t|) and w(t)k = (Z0)sk (k̸ = r) constant in t. By (4), row r of (P AJ (t))−1
is O(|t|−1) while all other rows are e⊤
k . Because t appears linearly only in column r of the
complementary block BJ (t), the product BJ (t)AJ (t)−1 = BJ (t)(P AJ (t))−1P stays uniformly
bounded as |t| → ∞. Thus |gI0(Z(t))| = |detA J (t)| · |gJ (BJ (t)AJ (t)−1)| = O(|t|), so by
single-variable Liouville’s theorem applied to ( gI0(Z(t)) −g I0(Z(0)))/t, gI0(Z(t)) is affine in
t.
2. Row-wise degree ≤ 1:Fix Z0, row s, and nonzero u∈C η, and set Z(t) = Z0 + tesu⊤. Pick
r with ur ̸= 0 and J = (I0 \ {r}) ∪ {η+ s}. On Φ( t) =
  Iη
Z(t)

, w(t)k = (Z0)sk + tuk, so
detA J (t) = ±((Z0)sr + tur) = O(|t|), every entry of ( P AJ (t))−1 in (4) is O(1), and BJ (t)
is completely independent of t. Hence BJ (t)AJ (t)−1 = O(1) and |gI0(Z(t))| = O(|t|), so
gI0(Z(t)) is affine int.
3. Alternating symmetry:If η≥ 2 and N−η≥ 2 (otherwise gI0(Z) already has only one row or
one column and is trivially a linear combination of 0 ×0 and 1 ×1 minors), take distinct rows
s1 ̸= s2 and distinct columns r1 ̸= r2, and set Z(t) = Z0 + t(es1 + es2)(er1 + er2)⊤. Multiply
Φ(t) =
  Iη
Z(t)

on the right by the unimodular matrix U = Iη −E r1,r2 (detU = 1), yielding
eΦ(t) := Φ(t)U=
  U
Z(t)U

withf( eΦ(t)) =f(Φ(t)) =g I0(Z(t)). Crucially, columnr 2 ofZ(t)U
equals (Z0):,r2 −(Z0):,r1 (independent of t), while t appears linearlyonlyin column r1 of eΦ(t)
(in rows η +s1 and η +s2). Choose chart J = (I0 \{r1})∪{η +s1} on eΦ(t): rows k∈I 0 \{r1}
of U are still e⊤
k , and row η +s1 has w(t)r1 = (Z0)s1,r1 +t with all w(t)k (k̸ = r1) independent
of t. By (4), detA J (t) = ±((Z0)s1,r1 + t) = O(|t|), row r1 of (P AJ (t))−1 decays as O(|t|−1),
and all other rows are e⊤
k . Since t appears linearly only in column r1 of BJ (t) (specifically at
row η+s2, while row r1 of U is the constant e⊤
r1 −e⊤
r2), BJ (t)AJ (t)−1 stays uniformly bounded
as |t| → ∞. Therefore |gI0(Z(t))| = |f(eΦ(t))| = |detA J (t)| · |gJ (BJ (t)AJ (t)−1)| = O(|t|), so
t7→g I0(Z(t)) has degree≤1.
Since gI0 is a polynomial of degree ≤ 1 in each row and column (by (1)–(2)), its t2 coefficient
along Z(t) in (3) is the sum of the coefficients of Zs1,r1Zs2,r2 and Zs1,r2Zs2,r1 (multiplying
any monomial in the remaining rows and columns), which must therefore vanish identically.
Thus gI0(Z) is alternating under transposition of any pair of rows or columns and is an
exact linear combination of minors of Z. By Jacobi’s complementary minor identity, det(A) ·
det((BA−1)S,R) = ±det (Φ(I0\R)∪(η+S) ), so f(Φ) = P
K∈([N]
η ) cK det(ΦK) on the dense open set
UI0, and by continuity on all ofM full
N,η.
4

--- Page 5 ---
Remark 2.2(Two-Spin Product Extension).For C1 spin-separated surrogates f(Φα, Φβ) on
Mfull
N,ηα ×Mfull
N,ηβ (1 ≤η α, ηβ ≤N ) equivariant under GL(ηα,C)×GL(ηβ,C) as in [6, Eq. (S2.19)],
applying Theorem 2.1 (Part (i) if ησ = N, Part (ii) if ησ < N) first to Φ α at fixed Φβ and then
to each resulting holomorphic GL(ηβ)-equivariant minor coefficient f(EI, Φβ) yields the identical
characterization: f(Φα, Φβ) = ⟨Ψ|ϕ(Φα) ⊗ϕ (Φβ)⟩ for a unique |Ψ⟩ ∈Vηα CN ⊗ Vηβ CN if and
only if∂f/∂Φ ∗
α ≡0 and∂f/∂Φ ∗
β ≡0.
Remark 2.3(Left-Projector Collapse vs. Non-Holomorphic Affine/Nonlinear Backflow).Not
every non-constant orbital map Gθ(PΦ) produces a non-holomorphic surrogate. If Gθ(PΦ) =
G0 +P ΦAisleft-projector affineinP Φ, then sinceP †
Φ =P Φ andP ΦΦ = Φ,
Gθ(PΦ)†Φ =G †
0Φ +A †PΦΦ = (G0 +A) †Φ,
so fθ collapses identically to the single fixed Slater determinant det[(G0 + A)†Φ] and is se-
cretly holomorphic. Conversely, general affine maps in PΦ that couple across orbitals via left
multipliers or scalar traces—such as G0 + BPΦA (when B does not commute with PΦ) or
G0 + κtr (MobsPΦ)Abf (Experiment 1 below)—as well as nonlinear backflow networks in PΦ
evade this collapse precisely by introducing genuine Φ ∗-dependence, which generically breaks
¯∂fθ = 0.
2.1 Exact Distance-to-Physical-States Witness and Mixed-Estimator Bias
Theorem 2.4(Pl¨ ucker-Kernel Distance Floor and Holomorphic Projection Restoration).Let
{Φ1, . . . ,Φm} ⊂ Mfull
N,η be any finite set of (possibly complex) walkers, let W∈C D×m (D =
 N
η

)
have columns |ϕ(Φa)⟩, and let S := W†W∈C m×m be their exact overlap Gram matrix with
Moore–Penrose pseudoinverse S+. For any overlap surrogate f with evaluation vector fS :=
(f(Φ1), . . . , f(Φm))⊤ ∈C m, define thePl¨ ucker-kernel witness
ηPl(f;S) :=
(Im −SS +)f∗
S

2 =
(Im −S ⊤(S⊤)+)fS

2.(5)
Then for every physical trial state|Ψ⟩ ∈ Vη CN with overlap vector(v Ψ)a :=⟨Ψ|ϕ(Φ a)⟩,
inf
|Ψ⟩∈Vη CN
∥fS −v Ψ∥2 =η Pl(f;S),
and the infimum is uniquely attained within Vm := span{|ϕ(Φa)⟩} by the holomorphic projection
|Ψproj
f ⟩:=W S+f∗
S =
mX
a,b=1
(S+)ab f(Φb)∗ |ϕ(Φa)⟩.(6)
In particular, for any Hermitian Hamiltonian H on Vη CN with ground-state energy E0 =
λmin(H), whenever |Ψproj
f ⟩ ̸= 0, its Rayleigh quotient Evar(f; S) :=
⟨Ψproj
f |H|Ψproj
f ⟩
⟨Ψproj
f |Ψproj
f ⟩ ≥E 0 is a strict
variational upper bound onE 0.
Proof. For any |Ψ⟩ ∈CD, ( vΨ)a = ⟨Ψ|ϕ(Φa)⟩ = ( W†Ψ)∗
a, so ∥fS −v Ψ∥2 = ∥f∗
S −W †Ψ∥2.
Because im(W†) = im(W†W) = im(S), the orthogonal projector onto im(W†) is Π S := SS+.
Decomposingf ∗
S = ΠSf∗
S + (Im −Π S)f∗
S, orthogonality gives
∥f∗
S −W †Ψ∥2
2 =∥(I m −SS +)f∗
S∥2
2 +∥SS +f∗
S −W †Ψ∥2
2 ≥η Pl(f;S) 2.
Setting |Ψproj
f ⟩ = W S+f∗
S yields W†Ψproj
f = SS+f∗
S, attaining exact equality; uniqueness inside
Vm = im(W) = ker(W†)⊥ holds because any two minimizers differ in ker(W†) ∩ Vm = {0}.
Note the complex conjugation f∗
S: for complex walkers (standard in AFQMC due to complex
Hubbard–Stratonovich fields),v Ψ ∈im(S ⊤) = im(S∗), whereasv ∗
Ψ ∈im(S).
5

--- Page 6 ---
Now consider a factorized fermionic Hamiltonian H = Ecore + ˆB0 + P
γ cγ ˆB2
γ with Hermitian
one-body matrices B0, Bγ and cγ ∈R [6, Eq. (S2.9)]. Following [ 6, Eq. (S2.21)], define the
Lie-derivative operators DB[f](Φ) := −i∂sf(eisBΦ)|s=0, D2
B[f](Φ) := −∂2
s f(eisBΦ)|s=0, and the
surrogate local-energy numerator
LH[f](Φ) :=E coref(Φ) +D B0[f](Φ) +
X
γ
cγD2
Bγ [f](Φ), E f
L(Φ) := LH[f](Φ)
f(Φ) .
By the chain rule, DB[f](Φ) = P
p,k
∂f
∂Φpk
(BΦ)pk −P
p,k
∂f
∂Φ∗
pk
(BΦ)∗
pk, reproducing [6, Eq. (S2.22)].
For any physical statef Ψ,L H[fΨ](Φ) =⟨Ψ|H|ϕ(Φ)⟩.
Theorem 2.5(Exact Mixed-Estimator Bias Decomposition).Let f = fΨ + r be any decom-
position of a C2 equivariant surrogate into a physical state overlap fΨ and a non-holomorphic
residual r. For any finite walker ensemble {(wi, Φi)}Nw
i=1 with f(Φi) ̸= 0, total weight Wtot :=PNw
i=1 wi ̸= 0, and represented state |eΨ⟩ := PNw
i=1
wi
f(Φi) |ϕ(Φi)⟩, the mixed energy estimator
Ef
mix := 1
Wtot
PNw
i=1 wiEf
L(Φi)satisfies
Ef
mix −E 0 = ⟨Ψ|(H−E 0)|eΨ⟩
Wtot
+ 1
Wtot
NwX
i=1
wi
f(Φi)
 
LH[r](Φi)−E 0r(Φi)

.(7)
Consequently, even on azero-walker-errorensemble representing the exact ground state ( |eΨ⟩ =
|Ψ0⟩), the first term vanishes identically while the second term leaves a generically nonzero,
representation-dependent non-holomorphic bias.
Proof.UsingW tot = P
i
wi
f(Φi) f(Φi) and linearity ofL H,
Wtot(Ef
mix −E 0) =
NwX
i=1
wi
f(Φi)
 
LH[f](Φi)−E 0f(Φi)

=
NwX
i=1
wi
f(Φi)
 
LH[fΨ](Φi)−E 0fΨ(Φi)

+
NwX
i=1
wi
f(Φi)
 
LH[r](Φi)−E 0r(Φi)

.
Since LH[fΨ](Φi) −E 0fΨ(Φi) = ⟨Ψ|(H−E 0)|ϕ(Φi)⟩, linearity of ⟨Ψ|(H−E 0)|·⟩ collapses the
first sum to⟨Ψ|(H−E 0)|eΨ⟩. Dividing byW tot gives (7).
3 Universal Mixed-Energy Variational-Boost Law
Because raw mixed energies Emix = ⟨Ψsur|H|ΨT ⟩
⟨Ψsur|ΨT ⟩ are non-variational (and can be complex when
|ΨT ⟩ is not an eigenstate), QC-QMC normally cannot certify E0 from mixed overlaps alone.
The following universal, sharp inequality resolves this directly; it may be viewed as a 2 × 2
Schur-complement upper-bound counterpart to Temple’s lower-bound inequality, replacing
second-moment H2 data with linear mixed residuals dH and an upper spectral enclosure Emax.
Theorem 3.1(Universal Mixed-Energy Variational-Boost Law).Let H be any Hermitian
operator on a finite-dimensional Hilbert space satisfying H⪯E maxI with ground-state energy
E0 = λmin(H). Let |Ψsur⟩,|ΨT ⟩ be unit vectors with overlap b0 := ⟨Ψsur|ΨT ⟩ satisfying |b0|< 1,
classical surrogate energy Esur := ⟨Ψsur|H|Ψsur⟩< E max, and linear mixed energy residual
dH :=⟨Ψ sur|(EsurI−H)|Ψ T ⟩(=b 0(Esur −E mix)whenb 0 ̸= 0). Then
E0 ≤E sur − |dH|2
(Emax −E sur)(1− |b0|2).(8)
6

--- Page 7 ---
Inequality (8) holds unconditionally (including for b0 = 0, complex Emix, and Emix > Esur)
and is sharp: letting A := EmaxI−H , S := span{|Ψsur⟩,|ΨT ⟩}, and A|S := PSAPS be the
2 × 2compression of A to S, equality holds for dH ̸= 0if and only if rank(A|S) = 1and
λmax(A|S) = Emax −E 0 (equivalently, S = span{|Ψ0⟩,|Ψmax⟩} with H|Ψ0⟩ = E0|Ψ0⟩ and
H|Ψmax⟩=E max|Ψmax⟩), and ford H = 0if and only ifE sur =E 0.
Proof. Set A := EmaxI−H⪰ 0 and λ := λmax(A) = Emax −E 0. Decompose |ΨT ⟩ =
b0|Ψsur⟩+
p
1− |b0|2 |w⟩ with ⟨Ψsur|w⟩ = 0 and ∥w∥2 = 1. Restricting A to S = span{|Ψsur⟩,|w⟩}
produces the 2×2 positive semidefinite matrix
M=
 α β
β∗ γ

⪰0, α:=⟨Ψ sur|A|Ψsur⟩=E max−Esur >0,|β|=|⟨Ψ sur|A|w⟩|= |dH|p
1− |b0|2 ,
where γ := ⟨w|A|w⟩ satisfies M⪰ 0 = ⇒αγ≥ |β| 2 and λI2 −M⪰ 0 = ⇒λ≥α ,
λ≥γ , and ( λ−α )(λ−γ ) ≥ |β|2. Suppose for contradiction that λ < α+ |β|2/α. Then
0 ≤λ−α <|β| 2/α (which forces |β|2/α >0) and, since γ≥ |β|2/α, 0 ≤λ−γ≤λ−|β| 2/α < α.
Multiplying these nonnegative inequalities gives (λ−α )(λ−γ ) < (|β|2/α)·α = |β|2, contradicting
(λ−α)(λ−γ) ≥ |β|2. Hence Emax−E0 = λ≥λ max(M) ≥α +|β|2/α, which rearranges to (8). For
sharpness when dH ̸= 0 (β̸ = 0), equality requires both λ = λmax(M) and λmax(M) = α+|β|2/α;
evaluating det((α + |β|2/α)I2 −M ) = (|β|2/α)(|β|2/α−γ ) ≤ 0 shows the latter holds if and
only if γ = |β|2/α, i.e., rank(M) = 1, and then the unit eigenvector of M with eigenvalue λ is a
ground state ofHwhile its orthogonal complement inSlies in ker(A) = ker(E maxI−H).
4 Surrogate-Anchored Block Hausdorff Certificates and Quan-
tum Shadow Protocol
Theorem 3.1 is the degree-0 instance of a full semidefinite moment hierarchy anchored to a classical
physical surrogate |Ψsur⟩. Given an oracle-free spectral enclosure Ebox
minI⪯H⪯E box
maxI (e.g., via
Gershgorin’s theorem), define the rescaled contraction T := (Ebox
maxI−H )/(Ebox
max −E box
min) ∈ [0, I]
and the 2×2 block Hausdorff moment sequence [9]
Bk :=
ak bk
b∗
k ck

:=
⟨Ψsur|Tk|Ψsur⟩ ⟨Ψsur|Tk|ΨT ⟩
⟨ΨT |Tk|Ψsur⟩ ⟨Ψ T |Tk|ΨT ⟩

, k= 0,1, . . . , K,
with a0 = c0 = 1 and bre
k := Re(bk) = Re⟨Ψsur|Tk|ΨT ⟩. Crucially, a0, . . . , aK are computed
classically, bre
0 , . . . , bre
K arepurely linearin |ΨT ⟩ (estimated directly from classical shadows), and
c1, . . . , cK ∈[0,1] may remain completelyunmeasured.
For degree d≥ 0, define the 2(d + 1)× 2(d + 1) shifted block-Hankel matrices (H(s)
d (B))i,j :=
Bi+j+s (0 ≤i, j≤d , s∈ {0, 1, 2}). For any spectral cutoff θ∈ [0, 1] and any gap window
0 ≤θ 1 ≤θ 2 ≤ 1, define the single-edge and two-edge gap dual functionals overreal symmetric
PSD matrix tuples (P, Q, R) and (P, Q, R, G)⊂S2(d+1)
+ :
Φedge(P, Q, R;θ)(B) :=⟨P, Hd(B)⟩+⟨Q, H(1)
d (B)⟩+⟨R, θHd(B)−H (1)
d (B)⟩,(9)
Φgap(P, Q, R, G;θ1, θ2)(B) := Φedge(P, Q, R; 1)(B)
+⟨G, H(2)
d (B)−(θ 1 +θ 2)H(1)
d (B) +θ 1θ2Hd(B)⟩,(10)
where ⟨M, X⟩:= tr(MX ). Because M∈S 2(d+1)
+ is real symmetric and Bk is Hermitian, the
symmetric off-diagonal pair in tr(MH (s)
d (B)) combines as M(i,0),(j,1)b∗
i+j+s + M(j,1),(i,0)bj+i+s =
2M(i,0),(j,1)bre
i+j+s; thus (9)–(10) expand identically as real linear functionals P
k(ca,kak +cb,kbre
k +
cc,kck) even when|Ψ sur⟩,|Ψ T ⟩are arbitrarycomplexvectors!
7

--- Page 8 ---
Theorem 4.1(Surrogate-Anchored Block Hausdorff Conic-Dual Soundness).Let T∈ [0, I]
have eigenbasis {et} and let µ = P
t
 ut
vt
 ut
vt
†δt (ut := ⟨Ψsur|et⟩, vt := ⟨ΨT |et⟩) be the2 × 2
spectral measure of arbitrary complex unit states( |Ψsur⟩,|ΨT ⟩)(so c0 = 1and0 ≤c k ≤ 1for
all k). Suppose( ak, bre
k )lie in the enclosure |ak −a q
k| ≤εa,k and |bre
k − ˆbk| ≤εb,k (0 ≤k≤K ,
εa,k, εb,k ≥0).
(i) Single-edge ground-state certificate ( K = 2d + 1):If real symmetric PSD matrices
P, Q, R⪰0satisfy
Medge :=c c,0 +
KX
k=0
 
ca,kaq
k +|c a,k|εa,k +c b,kˆbk +|c b,k|εb,k

+
KX
k=1
max(0, cc,k)<0,
thensupp(µ)̸⊆[0, θ]; henceλ max(T)> θandE 0 < Ebox
max −θ(E box
max −E box
min).
(ii) Two-edge visible spectral-gap certificate ( K = 2 d + 2,0 ≤θ 1 ≤θ 2 ≤ 1):If
real symmetric PSD matrices P, Q, R, G⪰0satisfy Mgap < 0(defined identically from
(10)), then supp(µ) ̸⊆ [0, θ1] ∪ [θ2, 1]; hence T possesses at least one eigenvalue visible to
span{|Ψsur⟩,|ΨT ⟩} strictly inside( θ1, θ2). In particular, setting θ2 := θcert from a certi-
fied single-edge bound ( λ0 > θcert) certifies anexcitedstate strictly inside( Ecert, Ebox
max −
θ1(Ebox
max −E box
min))with zero oracle knowledge ofE 0.
Given rational moment enclosures( aq
k, εa,k)and( ˆbk, εb,k), verifying symmetry and PSD-ness
of( P, Q, R, G) ⊂Q 2(d+1)×2(d+1) via exact rational pivoted LDL⊤ factorization and checking
M<0inQrequires zero floating-point trust.
Proof. Factoring any real symmetric PSD matrix M = P
r x(r)(x(r))⊤ (x(r) ∈R 2(d+1)) and
expanding Bk = P
t tk ut
vt
 ut
vt
† (so ak = P
t |ut|2tk, bre
k = P
t Re(utv∗
t )tk, ck = P
t |vt|2tk) yields
⟨M, H(s)
d (B)⟩=
X
r
X
t
ts

dX
i=0
 
x(r)
i,0 ut +x (r)
i,1 vt

ti

2
≥0.
Consequently, Φedge(P, Q, R; θ)(B) ≥ 0 whenever supp(µ) ⊆ [0, θ], and Φgap(P, Q, R, G; θ1, θ2)(B) ≥
0 whenever supp(µ) ⊆ [0, θ1] ∪ [θ2, 1] (as ( t−θ 1)(t−θ 2) ≥ 0 outside ( θ1, θ2)). Because
|ak −a q
k| ≤εa,k, |bre
k − ˆbk| ≤εb,k, and ck ∈ [0, 1], we have Φ( B) ≤ M< 0, yielding the
stated contradictions.
4.1 Distribution-Free Quantum Shadow Protocol and PPI Surrogate Debias-
ing
To ground the linear-moment confidence box in an experimentally concrete, non-Gaussian
measurement model, let |χ⟩ = (|0⟩ + |ΨT ⟩)/
√
2∈C| 0⟩ ⊕ HD (d := D + 1) as in [6, Eq. (S2.12)],
and apply C independent global Haar (or 3-design) randomized measurements ( Uc, bc) yielding
unbiased classical shadows ˆρ(c)
χ = (d + 1)U†
c |bc⟩⟨bc|Uc −I [4]. Setting |uk⟩ := Tk|Ψsur⟩ (classical,
∥uk∥2 = √a2k) and Ok := |uk⟩⟨0| + |0⟩⟨uk|, the single-shot linear estimator ˆb(c)
k := tr(ˆρ(c)
χ Ok) =
2(D+ 2) Re(⟨0|U †
c bc⟩⟨bc|Ucuk⟩) satisfies:
1.Exact unbiasedness:E[ ˆb(c)
k ] = Re⟨Ψsur|Tk|ΨT ⟩=b re
k .
2. Deterministic bound:If a2k = 0, then |uk⟩ = 0 and ˆb(c)
k ≡ 0; for a2k > 0, |0⟩ ⊥ |uk⟩ gives
|⟨0|U†
c bc⟩|2 +|⟨b c|Ucuk⟩|2/a2k ≤1, so AM–GM yields| ˆb(c)
k | ≤(D+ 2)√a2k almost surely.
8

--- Page 9 ---
3. Exact dimension-free 3-design variance:Because tr(Ok) = 0, tr(O2
k) = 2 a2k, and
tr(ρχO2
k) = 1
2 (a2k +|b k|2), exact 3-design Weingarten integration onC d (d=D+ 1) gives
E

(ˆb(c)
k )2
= d+ 1
d+ 2
 
tr(O2
k) + 2 tr(ρχO2
k)

= D+ 2
D+ 3
 
3a2k +|b k|2
≤4a 2k,(11)
where |bk|2 ≤a 2k by Cauchy–Schwarz (strict whenevera2k > 0). Thus Var(ˆb(c)
k ) = E[(ˆb(c)
k )2]−
(bre
k )2 ≤ 4a2k universally for arbitrarycomplexstates ( |Ψsur⟩,|ΨT ⟩) (and Var(ˆb(c)
k ) ≤ 3a2k
wheneverb k ∈R), completely independent of Hilbert-space dimensionD.
Proposition 4.2(Distribution-Free Median-of-Means Box and PPI Walker Debiasing).(i) For
any α∈ (0, 1), let B≥ ⌈8 ln((K + 1)/α)⌉ (odd) and suppose C≥B . Partition C i.i.d.
shadow snapshots into B disjoint blocks of size m = ⌊C/B⌋ ≥1, and let ˆbMoM
k be the coordi-
natewise median of block means. Given variance upper bounds σ2
k ≥Var (ˆb(c)
k )(e.g. σ2
k = 4a2k
by (11)), setting εb,k := 2
q
σ2
k/m guarantees P
 
∀0 ≤k≤K,| ˆbMoM
k −b re
k | ≤εb,k

≥ 1 −α
without Gaussianity or bounded-moment penalties.
(ii) When a linear cross-moment is evaluated as a population average h = 1
M
PM
a=1 gava over M
walkers (e.g. an NOCI expansion), let fθ beanyfrozen surrogate (possibly biased or non-
holomorphic), let( a1, . . . , amcal)be i.i.d. uniform drawswith replacementfrom {1, . . . , M},
and pair each draw ar with a conditionally independent unbiased shadow estimate ˆvar
(E[ˆvar |a r] = var , e.g. from disjoint shadow batches). The Prediction-Powered Inference
estimator [1]
bhPPI := 1
M
MX
a=1
gafθ(Φa) + 1
mcal
mcalX
r=1
gar
 
ˆvar −f θ(Φar )

is strictly unbiased (E[ bhPPI] =h) regardless of surrogate error, with exact variance
Var(bhPPI) = 1
mcal
Vara
 
ga(va −f θ(Φa))

+ 1
mcalM
MX
a=1
g2
a Var(ˆva |a).
Proof. For (i), Chebyshev’s inequality gives P(|¯bj,k −b re
k |> 2
q
σ2
k/m) ≤ 1/4 on each block
j∈ {1, . . . , B}. The median fails only if at least B/2 blocks fail; by Hoeffding’s inequality
for Bin(B, 1/4), P(Bin(B, 1/4) ≥B/ 2) ≤exp (−2B(1/2 − 1/4)2) = exp(−B/8) ≤α/ (K + 1)
[7]. A union bound over K + 1 coordinates completes (i). Part (ii) follows directly from i.i.d.
with-replacement sampling, conditional independence of {ˆvar }, linearity of expectation, and the
law of total variance.
5 Numerical Validation and Adversarial Falsification
All numerical results below are generated deterministically byscripts/run all experiments.py
and verified byscripts/verify all.py.
Experiment 1: Zero-walker-error Backflow NQS bias ( N = 4 , η= 2Hubbard).
Consider the two-site Hubbard model ( t = 1, U= 4, D =
 4
2

= 6, exact E0 = −0.828427) in its
exact factorized form H = B0 + U
2 N2
0 + U
2 N2
1 . We construct the smooth GL(2,C)-equivariant
affine-trace Backflow NQS (cf. Remark 2.3)
fκ(Φ) = det
h 
G0 +κtr(M obsPΦ)Abf
†Φ
i
,
9

--- Page 10 ---
Table 1: Experiment 1: Two-site Hubbard ( t = 1, U= 4, E0 = −0.828427). Equivariance
error is ≤ 2.1 × 10−15 throughout. Even with zero walker error, non-holomorphic backflow
(κ̸ = 0) produces severe representation-dependent bias strictly below E0 on rotated walkers while
appearing unbiased on computational determinants.
κ η Pl(fκ;S)∥G ¯∂(Φrot)∥F Ecomp
mix Erot
mix BiasE rot
mix −E 0 Evar(Ψproj
f )
−0.6 1.4985 0.2261−0.828427−1.382321−0.553894−0.247009
−0.4 0.9709 0.0929−0.828427−1.077142−0.248715−0.182251
0.0<10 −14 <10 −10 −0.828427−0.828427 +0.000000 +0.000000
+0.4 0.8909 0.0929−0.828427−1.077142−0.248715 +0.081345
+0.8 1.7467 0.4534−0.828427−1.799247−0.970820 +0.057433
−0.6 −0.4 −0.2 0.0 0.2 0.4 0.6 0.8
Backflow strength κ
−2.00
−1.75
−1.50
−1.25
−1.00
−0.75
−0.50
−0.25
0.00
Energy (Ha / hopping units)
(a) Zero-Walker-Error Mixed-Energy Bias
Exact E0 = −0.8284
Eθ
mix (comp. basis decomp.)
Eθ
mix (rotated decomp. of |Ψ0⟩)
Evar(Ψproj
f ) (restored)
Unphysical region (E < E0)
−0.6 −0.4 −0.2 0.0 0.2 0.4 0.6 0.8
Backflow strength κ
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75Non-physicality diagnostic
(b) Exact Non-Physicality Witnesses
Plücker-kernel witness ηPl(fκ; S)
Wirtinger defect ‖G ̄∂(Φrot)‖F
Figure 1: Experiment 1 ( N = 4, η= 2 Hubbard, E0 = −0.8284). (a) Exact zero-walker-error
mixed energy on computational-basis vs. rotated decompositions of |Ψ0⟩, alongside restored
variational energy Evar(Ψproj
f ). (b) Sharp Pl¨ ucker-kernel witnessηPl and Wirtinger defect ∥G¯∂∥F .
where G0 is the delocalized RHF singlet determinant and Mobs is the off-diagonal hopping
matrix. Because Mobs has zero diagonal, s(Φ) := tr(MobsPΦ) = 0 on every computational-
basis determinant; moreover [ PΦ, Nj] = 0 and [ Mobs, B0] = 0 (since B0 = −tMobs − U
2 I), so
s(eisNj Φ) ≡ 0 and ∂ss(eisB0Φ)|s=0 = 0, giving fκ zero overlap error and zero mixed-energy bias
on the computational-basis decomposition of |Ψ0⟩ (while the pointwise Wirtinger defect ∥G¯∂∥F
vanishes on the doubly-occupied determinants (0 , 2), (1, 3) yet already flags non-holomorphicity
with ∥G¯∂∥F = 2.2627 at κ = 0.8 on the dominant singly-occupied determinants (0, 3), (1, 2)). Yet
on a spin-orbital rotated exact decomposition of theexact sameground state |Ψ0⟩ (θrot = 0.37 rad,
zero walker error!), Table 1 and Figure 1 showEθ
mix plunging strictly below E0 (reaching −1.7992,
bias −0.9708 at κ = 0.8). Both the derivative-free Pl¨ ucker witness ηPl(fκ; S) (evaluated on
m = 12 complex walkers) and ∥G¯∂(Φrot)∥F detect the obstruction immediately, and holomorphic
projection (6) restores strict variationalityE var ≥E 0.
Experiment 2: Adversarial 10,000-trial audit of Theorem 3.1.Across 10 ,000 random
complex Hermitian Hamiltonians (d∈ [2, 13]) and random complex unit state pairs (|Ψsur⟩,|ΨT ⟩),
inequality (8) had 0/10,000violations(minimum slack Ecert −E 0 = 2 .58 × 10−4, median
boost 0.1504, max boost 3 .3951). On the sharp boundary witness H = diag(−1, 1), |Ψsur⟩ =
(cos 0.4,sin 0.4)⊤, |ΨT ⟩ = (1, 0)⊤ (S = span{|Ψ0⟩,|Ψmax⟩}), Esur = −0.696707 boosts to Ecert =
−1.000000000000 =E 0 (gap 0.00).
10

--- Page 11 ---
Table 2: Experiment 3: 4-site Hubbard chain (D = 36, E0 = −1.953145, RHF Esur = −0.472136).
Every Anchored (a, b) and Full (a, b, c) bound is independently verified in exact rational arithmetic
(Q) via symmetry-checked pivotedLDL ⊤ with explicit enclosureε a,k = 10−10 (k≥1).
εb DegreedClassical Krylov (a) Anchored (a, bonly) Full (a, b, c) Exact-Qmargin (a, b)
0.000 0−0.472136−0.870796−1.948452−4.31×10 −8
0.000 1−1.659517−1.906745−1.952736−1.78×10 −9
0.000 2−1.918123−1.948226−1.952929−7.74×10 −10
0.002 0−0.472136−0.831127−1.903284−4.60×10 −8
0.002 1−1.659517−1.713670−1.924538−2.38×10 −9
0.002 2−1.918123−1.918107−1.928063−3.20×10 −9
0.005 0−0.472136−0.774643−1.843284−3.97×10 −8
0.005 1−1.659517−1.659516−1.892758−1.48×10 −9
0.005 2−1.918123−1.918107−1.918120−3.20×10 −9
0.020 0−0.472136−0.555073−1.543283−3.66×10 −8
0.020 2−1.918123−1.918091−1.918104−7.58×10 −9
Experiment 3: 4-site Hubbard Block Hausdorff energy and oracle-free spectral-
gap certificates.On the 4-site 1D Hubbard chain at half-filling (8 spin-orbitals, D = 36,
t = 1, U= 4, E0 = −1.953145, E1 = −1.412899), Gershgorin’s theorem gives the oracle-free
enclosure [ −6, 14]. Anchoring to the classical RHF determinant |Ψsur⟩ (Esur = −0.472136,
overlap fidelity 0.7160) and an imaginary-time correlated quantum trial |ΨT ⟩ ∝e−0.6H|Ψsur⟩
(ET = −1.943285, b0 = 0 .8678), Table 2 and Figure 2 reportexact- Q-verifiedBlock Haus-
dorff upper bounds on E0 (with explicit rational classical-moment enclosure εa,k = 10 −10
for k≥ 1, absorbing double-precision evaluation and rational quantization) andoracle-free
two-edge visible spectral-gap certificates. At d = 0, usingonly( a0, a1) and linear cross-
moments (b0, b1) (zero ck measurements), Theorem 3.1/Theorem 4.1 certifies E0 ≤ −0.8708
(εb = 0), −0.8311 ( εb = 0 .002), and −0.7746 ( εb = 0 .005), improving on RHF by +0 .399,
+0.359, and +0 .303. At d = 1 , εb = 0 .002, the anchored certificate reaches E0 ≤ −1.7137,
strictly beating classical Krylov ( −1.6595) by +0 .0542 even under noisy linear shadows; at
d = 2, εb = 0, it reaches E0 ≤ −1.9482 (within 0 .0049 of exact E0). With adaptive rational
PSD shifts, at d = 2 and εb ≥ 0.002 the exact- Q anchored bound tightly tracks the floating-
point classical Krylov floor ( −1.918107 vs. −1.918123, quantization slack 1 .6 × 10−5) and is
strictly monotone in εb. For theoracle-freetwo-edge gap localizer ( d = 2, K= 6), we plug
θ2 := θcert = 67936019/85356906 ≈ 0.795905 (Ecert = −1.918107) directly from the exported
single-edge certificate hubbard4 edge d2 eps002.cert.json (which already proves λ0 > θ2
without knowing E0). The dominant excited singlet visible to |Ψsur⟩ sits at E8 = +1.9110
(weight 0.1528; level 3 at −0.5954 carries weight 0 .0033). At εb = 0.002, exact rational cer-
tificates refute [0, θ1] ∪ [θ2, 1] down to Ecut = +3.00 (exact-Q margin −1.11 × 10−6, exported
in hubbard4 gap d2 E30 eps002.cert.json; at εb = 0, margin −2.68 × 10−5), certifying an
excited state strictly inside ( −1.9181, +3.00) without any oracle, and cleanly failing to reject for
Ecut ≤+2.50.
Experiment 4: Authentic Born-rule shadow coverage and Backflow-NQS PPI de-
biasing.All three parts of Experiment 4 simulate exact Born-rule global Haar shadows on
C|0⟩ ⊕ HD via Mezzadri QR sampling (zero synthetic Gaussian noise proxies): (i) On the 4-site
Hubbard chain (D = 36, 20,000 shots), empirical single-shot variances [2 .901, 1.570, 0.923, 0.564]
for k = 0, 1, 2, 3 match the exact 3-design formula (11) ([2.904, 1.568, 0.921, 0.562]) to three signif-
icant figures and sit cleanly below the universal complex bound 4 a2k ([4.000, 2.162, 1.271, 0.776],
Figure 3a), while maximum single-shot magnitudes [10 .19, 7.49, 5.86, 4.62] obey ( D + 2)√a2k.
11

--- Page 12 ---
0.0000 0.0025 0.0050 0.0075 0.0100 0.0125 0.0150 0.0175 0.0200
Linear-shadow confidence half-width εb
−2.0
−1.8
−1.6
−1.4
−1.2
−1.0
−0.8
−0.6
−0.4
Certified upper bound Ecert ≥E0
(a) 4-Site Hubbard Certified Ground-State Bounds
Anchored (a, b) only, d = 0
Anchored (a, b) only, d = 1
Anchored (a, b) only, d = 2
Full (a, b, c), d = 2
Exact E0 = −1.9531
RHF Esur = −0.4721
2.02.53.03.54.0
Excited-state cutoff Ecut (certifying spectrum in (Ecert, Ecut))
10−6
10−5
10−4
10−3
Certified negative dual margin −Φgap > 0
(b) Oracle-Free Spectral-Gap Certificates (d = 2)
Exact-ℚ gap margin (εb = 0)
Exact-ℚ gap margin (εb = 0.002)
True dominant singlet E8 = +1.911
Figure 2: Experiment 3 (4-site Hubbard, D = 36). (a) Exact- Q-verified ground-state upper
bounds vs. linear-shadow confidence half-width εb (dotted lines: classical Krylov). (b) Oracle-free
exact-Q two-edge spectral-gap dual margins −Φgap using θ2 = θcert = 0.7959 (Ecert = −1.9181),
certifying an excited state strictly inside (−1.9181, Ecut).
(ii) Across 100 independent 2-site Hubbard campaigns ( C = 31,000 Born-rule shots/trial, B = 31
MoM blocks, α = 0.05, using universal σ2
k = 4a2k), the MoM box achieved 100 /100empirical
coverage( ≥ 95% target) and 100 /100valid exact- Q energy certificates( Ecert ≥E 0). At
this modest C = 31,000 shot budget, conservative MoM radii safely fall back to Esur (0/100 false
improvements), illustrating fail-closed behavior; crossing into strict RHF improvement requires
εb ≲ 0.02 (corresponding to Willow-scale 10 5–106 shots [6, Table S1.1]). (iii) On the 2-site Hub-
bard model ( D = 6), we generate M = 4,000 gauge-aligned rotated complex Slater-determinant
walkers {Φa} with purely classical RHF-based weights ga = 1 + 2|Re⟨ΨRHF|ϕ(Φa)⟩| and evaluate
a biased non-holomorphic Backflow NQS (0 .88 shrinkage plus κ = 0.5 backflow residual from
Experiment 1; surrogate-only bias −0.0868 on htrue = 0 .7050). Across 250 trials sampling
mcal = 80 walkers i.i.d. with replacement and measuring each calibration draw with Ccal = 256
independent Born-rule Haar shadows (5 ,120,000 total Born-rule shots), bhPPI eliminates bias
(−0.00139), achieves a 7 .40× variance reductionover raw Born-rule shadow subsampling
(RMSE = 0.0257 vs. 0.0701), yields an 11 .42× MSE reductionover the biased Backflow NQS
alone, and closely tracks the theoretical Proposition 4.2(ii) variance (6 .61 × 10−4 empirical vs.
5.79×10 −4 theoretical; Figure 3b).
6 Formal Verification Manifest and Reproducibility
To satisfy AIRR Gate 2 and Lean 4 Level L2 verification with strict specification transparency,
lean/QcQmcCert.lean (pinned to leanprover/lean4:v4.35.0 with zero external dependen-
cies) formally proves the algebraic, complex-vector orthogonal projection, 2 × 2 variational-
boost, and complex spectral-measure conic-dual soundness cores over an arbitrary linearly
ordered commutative field OrdField K (covering R and Q, with complex numbers represented
explicitly via ComplexK K). It builds cleanly via lake build in 2 .0 s with zero sorry and
zero warnings. Table 3 maps each Lean 4 theorem to its exact formalized scope and au-
dited axioms (via lean/AuditAxioms.lean); none require even Classical.choice. Complex-
analytic Grassmannian chart arguments (Theorem 2.1), Weingarten 3-design moments (11),
and Chebyshev/Hoeffding probability tails (Proposition 4.2) are proved analytically in prose.
All five exact rational dual certificates in results/rational certificates/ and all file di-
gests in SHA256SUMS.json are publicly archived at https://github.com/lluiseriksson/
12

--- Page 13 ---
k = 0 k = 1 k = 2 k = 3
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0Single-shot variance
(a) 4-Site Hubbard Born-Rule Shadow Variance (D = 36)
Empirical shadow variance (20k shots)
Exact 3-design theory
Universal bound 4a2k
Biased Backflow
NQS Only
Raw Subsampled
Haar Shadows
PPI Debiased
(Prop. 4.2)
0.00
0.02
0.04
0.06
0.08Estimation error
(b) Authentic Born-Rule PPI (7.4x Var. Reduction)
RMSE (250 trials)
|Empirical Bias|
Figure 3: Experiment 4 (100% authentic Born-rule global Haar shadows). (a) Empirical single-
shot variance vs. exact 3-design theory and universal bound 4 a2k on 4-site Hubbard ( D = 36,
20,000 shots). (b) Authentic Backflow-NQS PPI debiasing on 2-site Hubbard across 250 trials
(5.12 × 106 Born-rule shots; 7.40× variance reduction over raw shadows, 11.42× MSE reduction
over biased NQS).
Table 3: Auditable Claim-to-Theorem Manifest ( lean/QcQmcCert.lean, Lean v4.35.0, 0 sorry,
0 warnings).
Result Lean 4 Symbol (QcQmcCert.*) Exact Formalized Scope Audited Axioms
Remark 2.3linear projector collapseLeft-projectorG 0 +P Acollapse none
Theorem 2.4plucker kernel distance min, attained,
min complex
Real & ComplexK projection floor ∥g−
v∥2 ≥ ∥g⊥∥2
propext,
Quot.sound
Theorem 2.5mixed estimator bias decomp,
holomorphic zero bias,
nonholomorphic bias persists
Finite-walker algebraic bias split & eigen-
state residual persistence
propext,
Quot.sound
Theorem 3.1variational boost spectral bound,
hamiltonian, sharp
2 × 2 PSD spectral-edge bound, Hamil-
tonian form, rank-1 identity
none
Theorem 4.1(i)block hausdorff edge soundness,
edge soundness complex
Real & ComplexK spectral-measure single-
edge dual soundness
propext,
Quot.sound
Theorem 4.1(ii)block hausdorff gap soundness,
gap soundness complex
Real & ComplexK spectral-measure two-
edge gap dual soundness
propext,
Quot.sound
Theorem 4.1linear box upper boundBox transfer over|b− ˆb| ≤ε,c∈[0,1] none
Prop. 4.2(ii)ppi control variate unbiased Finite-population expectation identity
(algebraic core)
propext,
Quot.sound
qcqmc-spectral-certificates and replayed in one command viapython scripts/verify all.py.
7 Limitations and Continuation Frontier
We highlight four concrete limitations that define immediate next steps: (1) Theorem 2.1 (complex
Grassmannian holomorphicity) and the probabilistic tails/Weingarten moments of Section 4.1
are proved analytically in prose while Lean 4 formalizes the algebraic, complex-projection,
variational-boost, and complex conic-dual core; formalizing the complex-analytic Grassmannian
chart proof in Mathlib is left to future work. (2) At higher polynomial degree ( d≥ 3), monomial
Hankel bases become increasingly ill-conditioned under exact rationalLDL⊤ certification (though
adaptive shifts already reduce our d = 2 slack to 1.6 × 10−5 on 4-site Hubbard); switching to
Chebyshev-basis localizers Tk(T) should reduce condition numbers exponentially for high-degree
rational bounds. (3) Conservative Median-of-Means constants require large shot counts (10 5–106)
to beat strong classical baselines; integrating sharp Empirical-Bernstein / Catoni bounds with
matchgate shadow variance estimators is a high-leverage practical extension. (4) Two-edge gap
13

--- Page 14 ---
certification detects excited states visible to span{|Ψsur⟩,|ΨT ⟩} and cannot exclude symmetry
sectors strictly orthogonal to both states.
References
[1] Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan, and Tijana
Zrnic. Prediction-powered inference.Science, 382(6671):669–674, 2023.
[2] Minjae Cho, Barak Gabai, Henry W. Lin, Jessica Yeh, and Zechuan Zheng. Bootstrapping
euclidean two-point correlators, 2025.
[3] Lluis Eriksson. Finite-sample covariance-aware spectral-edge certificates from
noisy block moments. GitHub repository https://github.com/lluiseriksson/
finite-sample-spectral-certificates, 2026.
[4] Hsin-Yuan Huang, Richard Kueng, and John Preskill. Predicting many properties of a
quantum system from very few measurements.Nature Physics, 16:1050–1057, 2020.
[5] William J. Huggins, Bryan A. O’Gorman, Nicholas C. Rubin, David R. Reichman, Ryan
Babbush, and Joonho Lee. Unbiasing fermionic quantum monte carlo with a quantum
computer.Nature, 603:416–420, 2022.
[6] Tong Jiang, Andrew Zhao, Shashwat Kumar, Jigyasa Nigam, Eliott Rosenberg, Ryan
Babbush, Andrew D. Baczewski, William J. Huggins, and Joonho Lee. Machine learning
quantum data to accelerate quantum monte carlo, 2026. arXiv:2611.08151v2, November 17,
2026.
[7] G´ abor Lugosi and Shahar Mendelson. Mean estimation and regression under heavy-tailed
distributions: A survey.Foundations of Computational Mathematics, 19:1145–1190, 2019.
[8] Sujit Rao. A convergent hierarchy of spectral gap certificates for qubit hamiltonians, 2025.
[9] Konrad Schm¨ udgen.The Moment Problem, volume 277 ofGraduate Texts in Mathematics.
Springer, 2017.
[10] Kianna Wan, William J. Huggins, Joonho Lee, and Ryan Babbush. Matchgate shadows
for fermionic quantum simulation.Communications in Mathematical Physics, 404:629–700,
2023.
[11] Xiangling Xu, Matthias Sch¨ otz, Jie Wang, Victor Magron, Igor Klep, Omar Fawzi, and
Marc-Olivier Renou. The bulk spectral gap is certifiable from above but uncomputable
from below, 2026.
[12] Shiwei Zhang and Henry Krakauer. Quantum monte carlo method using phase-free random
walks with slater determinants.Physical Review Letters, 90(13):136401, 2003.
14
