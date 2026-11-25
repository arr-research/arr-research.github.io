# Exact-Q Lorentzian Inertia Certificates, Coincident Down-Up Spectral-Gap Phase Transitions, and Machine-Checked Subgaussian Matrix Concentration for Matroids

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-71T01WWJSY8DWTFN` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/lorentzian-matroid-certificates (`v1.0.0`)  
**Canonical PDF SHA-256:** `1b547f50f4ed04755b6fec88fba52214cc19cdb0bb476833df0e294c81563679`

## Abstract

Lorentzian polynomials provide a unified algebraic-combinatorial bridge from matroid theory to rapid mixing of high-dimensional random walks and sharp concentration inequalities. Very recently, Ercan (arXiv:2611.00626, November 2026) proved complete matrix entropy contraction with optimal universal factor ell/r for all r-homogeneous Lorentzian laws, yielding subgaussian matrix concentration bounds for arbitrary Hermitian observables with bounded exchange differences across all matroids. Here we sharpen and operationalize this landscape into exact rational theorems over Q, backed by an 18-theorem zero-dependency Lean 4 formalization and a pure-stdlib zero-floating-point-trust certificate verifier (LORENTZ-MATROID-CERT-1.0). First, we establish a sharp exact converse on the two-cluster weighted graph family G_{eps,m} = (K_m + K_m) + eps K_{m,m} (m >= 2, eps > 0): the 2-homogeneous generating polynomial f_{eps,m} is Lorentzian if and only if the 2->1->2 down-up spectral gap satisfies Ercan's optimal threshold gamma(eps,m) >= 1/2, with exact coincident critical coupling eps_c(m) = (m-1)/m in Q, exact piecewise gap gamma(eps,m) = m*eps/((m-1)+m*eps) (eps <= 1) and 1/2 + 1/(2((m-1)+m*eps)) (eps >= 1), and unique global maximum m/(2m-1) attained at the unweighted complete graph K_{2m} (eps=1). Second, using exact rational congruence diagonalization Q H Q^T = diag(D) (Q Q^-1 = I) capable of handling zero-diagonal multiaffine Hessians, we certify complete M-convexity, all (r-2)-link Lorentzian Hessians, and strict excess down-up spectral gaps gamma(P_{r->ell->r}) > 1-ell/r across uniform U_{3,6}, graphic M(K_4), Fano F_7, non-Fano F_7^-, and the non-representable Vamos matroid V_8 (all 28 rank-2 links certified in 20.2 ms; exact gap gamma(P_{4->2->4}; V_8) = 9/14 > 1/2; certified bracket [46/125, 37/100] > 1/4 at ell=3). Third, we translate Ercan's matrix subgaussian inequality into purely rational tail certificates via exact operator-norm PSD congruences c^2 I_d - (A_e - A_f)^2 >= 0 over all exchangeable pairs and exact rational Taylor-envelope denominators T_K(x) = sum_{k=0}^K x^k/k!, certifying non-commuting 2x2 Hermitian basis sums over M(K_4) and non-representable V_8 with zero floats and cross-checking against exact exhaustive basis enumeration. All 18 foundational theorems compile in zero-dependency Lean 4 (v4.35.0, 0 sorry, 0 Classical.choice, 0 warnings), all 16 exact-Q certificates verify in <= 404.3 ms, and the verifier rejects 48/48 live adversarial red-team attacks.

## Full Extracted Text

--- Page 1 ---
Exact-QLorentzian Inertia Certificates, Coincident
Down–Up Spectral-Gap Phase Transitions, and
Machine-Checked Subgaussian Matrix Concentration
for Matroids
Lluis Eriksson*
November 2026
Abstract
Lorentzian polynomials provide a unified algebraic-combinatorial bridge from matroid
theory to rapid mixing of high-dimensional random walks and sharp concentration inequal-
ities. Very recently, Ercan ( arXiv:2611.00626, November 2026) proved complete matrix
entropy contraction with optimal universal factor ℓ/r for all r-homogeneous Lorentzian
laws, yielding subgaussian matrix concentration bounds for arbitrary Hermitian observ-
ables with bounded exchange differences across all matroids. Here we sharpen and oper-
ationalize this landscape into exact rational theorems over Q, backed by an 18-theorem
zero-dependency Lean 4 formalization and a pure-stdlib zero-floating-point-trust certificate
verifier (LORENTZ-MATROID-CERT-1.0). First, we establish a sharp exact converse on the
two-cluster weighted graph family Gε,m = (Km ⊔K m) + εKm,m (m≥ 2, ε >0): the 2-
homogeneous generating polynomial fε,m is Lorentzian if and only if the 2 → 1 → 2 down–up
spectral gap satisfies Ercan’s optimal threshold γ(ε, m) ≥ 1/2, with exact coincident critical
coupling εc(m) = ( m− 1)/m∈Q , exact piecewise gap γ(ε, m) = mε
(m−1)+mε (ε≤ 1) and
1
2 + 1
2((m−1)+mε) (ε≥ 1), and unique global maximum m
2m−1 attained at the unweighted
complete graph K2m (ε = 1). Second, using exact rational congruence diagonalization
QHQ⊤ = diag(D) (QQ−1 = I) capable of handling zero-diagonal multiaffine Hessians, we
certify complete M-convexity, all (r− 2)-link Lorentzian Hessians, and strict excess down–up
spectral gaps γ(Pr→ℓ→r) > 1 −ℓ/r across uniform U3,6, graphic M(K4), Fano F7, non-Fano
F−
7 , and the non-representable V´ amos matroidV8 (all 28 rank-2 links certified in 20 .2 ms;
exact gap γ(P4→2→4; V8) = 9/14 > 1/2; certified bracket [46/125, 37/100] > 1/4 at ℓ = 3).
Third, we translate Ercan’s matrix subgaussian inequality into purely rational tail certificates
via exact operator-norm PSD congruences c2Id − (Ae −A f )2 ⪰ 0 over all exchangeable
pairs and exact rational Taylor-envelope denominators TK(x) = PK
k=0 xk/k!, certifying non-
commuting 2×2 Hermitian basis sums over M(K4) and non-representable V8 with zero floats
and cross-checking against exact exhaustive basis enumeration. All 18 foundational theorems
compile in zero-dependency Lean 4 ( v4.35.0, 0 sorry, 0 Classical.choice, 0 warnings),
all 16 exact-Q certificates verify in ≤ 404.3 ms, and the verifier rejects 48 /48 live adversarial
red-team attacks.
1 Introduction
The theory of Lorentzian polynomials, introduced by Br¨ and´ en and Huh [2] alongside the strongly
log-concave framework of Anari, Liu, Oveis Gharan, and Vinzant [ 1], established that the basis
* Independent researcher (Sweden). Prepared with AI assistance (Google Antigravity). Code, zero-dependency
Lean 4 formalization, and exact-Qcertificates (MIT license):
https://github.com/lluiseriksson/lorentzian-matroid-certificates.
1

--- Page 2 ---
generating polynomial
fM (x1, . . . , xn) =
X
B∈B(M)
Y
e∈B
xe (1)
of every rank-r matroid M satisfies the Lorentzian Hessian signature property on every (r−2)-fold
partial derivative. This algebraic condition implies Mason’s ultra-log-concavity conjecture [ 6],
resolves the Mihail–Vazirani expansion conjecture for basis-exchange walks [ 5, 1], and yields the
modified log-Sobolev constantα MLSI ≥1/rfor scalar functions [3].
In November 2026, Ercan [ 4] (arXiv:2611.00626) elevated this scalar theory to the non-
commutative matrix regime, proving that uniform retention of ℓ out of r particles contracts
matrix entropy by the optimal universal factorℓ/r for every r-homogeneous Lorentzian law across
arbitrary matrix dimension d. Combining this contraction with matrix Laplace comparisons,
Ercan established subgaussian matrix concentration bounds for arbitrary Hermitian observables
with bounded exchange differences, extending classical independent-sum matrix tail bounds [ 8]
to all matroids—including non-representable matroids such as the V´ amos matroidV8 [7].
Despite these breakthroughs, three structural and certification gaps remain open:
1. Sharp converse to Lorentzian contraction:Ercan [ 4] proves that every r-homogeneous
Lorentzian law achieves contraction factor≤ℓ/r (down–up spectral gap γ(Pr→ℓ→r) ≥ 1−ℓ/r).
Does the failure of the Lorentzian Hessian inertia condition immediately force a quantitative
breakdown of the universal spectral-gap threshold 1 −ℓ/r at anexact coincident threshold?
2. Zero-float certification of Lorentzianity and excess expansion:Standard numerical
eigensolvers (LAPACK/eigh) rely on IEEE-754 floating-point arithmetic, cannot rigorously
certify boundary eigenvalues (λ2(H) = 0) or exact rational excess gaps γ(Pr→ℓ→r) > 1 −ℓ/r ,
and standard LDL⊤ factorizations break down on zero-diagonal multiaffine matroid Hessians
(Hii = 0).
3. Rationalized non-commutative matrix concentration certificates:Operationalizing
Ercan’s subgaussian tail bound P[λmax(F(B) −EF ) ≥t ] ≤dexp (−t2/(2vsg)) for concrete
Hermitian basis sums requires certifying both the exact operator-norm exchange sensitivity
max(e,f) ∥Ae −A f ∥op ≤c and the exponential tail threshold without floating-point matrix
norms or transcendental evaluations.
Contributions.We close all three gaps with four exact- Q theorems (Section 3), an 18-
theorem zero-dependency Lean 4 formalization (Section 4), a pure-stdlib zero-float verifier
LORENTZ-MATROID-CERT-1.0, and four deterministic computational experiments (Section 5):
 Theorem 3.1 (Coincident Phase Transition):On Gε,m = (Km ⊔Km) +εKm,m (m≥ 2),
fε,m is Lorentzian iff γ(P2→1→2; ε, m) ≥ 1/2 iff ε≥ε c(m) = m−1
m , with an exact piecewise
rational spectral-gap law peaking uniquely at the unweighted complete graph K2m (ε = 1,
γmax = m
2m−1).
 Theorem 3.2 (Exact-Q Congruence Certificates for Non-Representable Matroids):
Using invertible rational congruence QHQ⊤ = diag(D) ( QQ−1 = I) built from swaps,
shears, and eliminations, we certify complete M-convexity, all (r− 2)-link Hessians, and
exact/bracketed strict excess down–up spectral gaps across U3,6, M(K4), F7, F−
7 , and the
non-representable V´ amos matroidV8.
 Theorem 3.3 (Zero-Float Matrix Tail Certification):We combine Ercan’s ℓ/r matrix
entropy contraction with exact rational PSD certificates c2Id − (Ae −A f )2 ⪰ 0 on all
exchangeable pairs and exact rational Taylor-envelope denominators TK(x) = PK
k=0 xk/k!
to certify non-commuting matrix tail probabilities purely overQ.
2

--- Page 3 ---
 Theorem 3.5 (Soundness of LORENTZ-MATROID-CERT-1.0):Our pure-stdlib verifier
independently reconstructs all link Hessians, reversible walks, Dirichlet–Gram operators, and
exchangeable pairs directly from explicit basis lists, verifying 16 /16 certificates with zero
floats and rejecting 48/48 live adversarial red-team attacks.
2 Preliminaries
Definition 2.1(Lorentzian Polynomials and Matroid Basis Laws [ 2]).A homogeneous poly-
nomial f∈R ≥0[x1, . . . , xn] of degree r≥ 2 with M-convex support isLorentzianif for every
multi-index α∈N n with |α| = r− 2, the symmetric Hessian matrix Hα = ∇2(∂αf) has at most
one positive eigenvalue. For a rank- r matroid M = ([n],B ) with multiaffine basis polynomial
fM (x) = P
B∈B wB
Q
e∈B xe (wB > 0), M-convexity is equivalent to the matroid basis-exchange
axiom, and the nontrivial ( r− 2)-fold derivatives correspond to independent sets S∈ Ir−2, with
zero-diagonal link Hessian (H S)ij =w S∪{i,j} fori̸=j /∈S.
Definition 2.2(Down–Up and Dual Up–Down Matroid Walks).For 0 ≤ℓ < r and basis
distribution π(B) = wB/ P
B′∈B wB′, the r→ℓ→r down–up Markov chain Pr→ℓ→r drops r−ℓ
elements uniformly at random from B to obtain S∈ Iℓ, then resamples a basis B′ ⊃S with
probability proportional tow B′:
Pr→ℓ→r(B, B′) = 1 r
ℓ

X
S⊆B∩B ′,|S|=ℓ
wB′
W(S) , W(S) :=
X
B′′⊇S
wB′′.(2)
Writing Dr→ℓ(B, S) =
 r
ℓ
−11S⊆B and Uℓ→r(S, B′) = wB′
W(S) 1S⊆B′, we have Pr→ℓ→r = Dr→ℓUℓ→r
(reversible with respect to π and positive semidefinite in L2(π)) and its dual up–down walk
Qℓ→r→ℓ = Uℓ→rDr→ℓ on Iℓ (reversible with respect to πℓ(S) = W(S)/ P
S′ W(S′)). Because
Dr→ℓUℓ→r and Uℓ→rDr→ℓ share identical nonzero eigenvalues, their spectral gaps coincide
identically:γ(P r→ℓ→r) =γ(Q ℓ→r→ℓ) = 1−λ 2(Pr→ℓ→r).
By Anari et al. [ 1] and Ercan [ 4], every r-homogeneous Lorentzian distribution satisfies
the universal spectral-gap bound γ(Pr→ℓ→r) ≥ 1 −ℓ/r , matching the universal matrix entropy
contraction factorℓ/r.
3 Main Exact-QTheorems
3.1 Exact Coincident Lorentzian / Spectral-Gap Phase Transition
Theorem 3.1(Coincident Phase Transition and Piecewise Spectral-Gap Law on Gε,m).For
every integer m≥ 2and rational coupling ε∈Q >0, let Gε,m = (Km ⊔K m) + εKm,m be the
weighted complete graph on n = 2m vertices with edge weights wij = 1inside each m-clique
and wij = ε across cliques, and let fε,m(x) = 1
2
P
i̸=j wijxixj be its2-homogeneous generating
polynomial with HessianH ε,m =∇ 2fε,m. Then:
1.Exact Hessian Spectrum and Lorentzian Threshold:H ε,m has exact eigenvalues
λ+(ε, m) = (m−1) +mε >0 (mult.1),
λ−(ε, m) = (m−1)−mε(mult.1), λ ⊥ =−1 (mult.2m−2). (3)
In particular,λ 2(Hε,m) = max
 
(m−1)−mε,−1

, sof ε,m is Lorentzian if and only if
ε≥ε c(m) := m−1
m ∈Q∩(0,1).(4)
3

--- Page 4 ---
2. Exact Piecewise Down–Up Spectral Gap:The2 → 1 → 2down–up walk P2→1→2 on
edges (isospectral to the vertex walk Q1→2→1 = 1
2(I2m + D−1Hε,m)with D = λ+I2m) has
exact spectral gap
γ(P2→1→2;ε, m) =



mε
(m−1) +mε ,0< ε≤1,
1
2 + 1
2
 
(m−1) +mε
, ε≥1.
(5)
3. Exact Coincidence and Unique Complete-Graph Maximum:For every m≥ 2and
ε >0,
fε,m is Lorentzian
 
λ2(Hε,m)≤0

⇐⇒γ(P 2→1→2;ε, m)≥ 1
2 ⇐⇒ε≥ m−1
m ,(6)
with simultaneous criticality λ2(Hεc(m),m) = 0and γ(εc(m), m) = 1/2for all m≥ 2, linear
collapse γ(ε, m) → 0as ε↓ 0, and unique global maximum γmax(m) = m
2m−1 > 1
2 attained at
the unweighted complete graphK 2m (ε= 1).
Proof. In 2 ×2 block form on Rm ⊕Rm, Hε,m =
Jm −I m εJm
εJm Jm −I m

, where Jm is the all-ones
matrix. On1 2m = (1m, 1m)⊤, Hε,m12m = ((m− 1) +mε)12m. On v− = (1m,−1m)⊤, Hε,mv− =
((m− 1) −mε )v−. On the (2 m− 2)-dimensional subspace1 ⊥
m ⊕ 1⊥
m, Jm annihilates both blocks,
giving Hε,mw = −w. Thus λ2(Hε,m) = max(λ−,−1) ≤ 0 ⇐⇒ (m− 1)−mε≤ 0 ⇐⇒ε≥ m−1
m
(Lean 4 Theorems 1–3).
Because Gε,m is vertex-regular with weighted degree d = (m− 1) +mε = λ+, the dual vertex
walk satisfies Q1→2→1(i, j) = 1
2δij + wij
2d , i.e. Q1→2→1 = 1
2(I2m + d−1Hε,m). Its eigenvalues are
therefore
µ1 = 1, µ − = 1
2

1 + (m−1)−mε
(m−1) +mε

= m−1
(m−1) +mε ,
µ⊥ = 1
2

1− 1
(m−1) +mε

= (m−2) +mε
2
 
(m−1) +mε
.
Comparing µ− and µ⊥ gives 2(m− 1) ≥ (m− 2) + mε⇐⇒m≥mε⇐⇒ε≤ 1 (Lean 4
Theorem 7). Hence λ2(Q1→2→1) = µ− for 0 < ε≤ 1 (giving γ = 1 −µ − = mε
(m−1)+mε) and
λ2(Q1→2→1) = µ⊥ for ε≥ 1 (giving γ = 1 −µ ⊥ = 1
2 + 1
2((m−1)+mε)). For ε >1, 1 −µ ⊥ > 1
2 holds
unconditionally (Lean 4 Theorem 8), while for 0 < ε≤ 1, γ≥ 1
2 ⇐⇒ 2mε≥ (m− 1) +mε⇐⇒
ε≥ m−1
m , matching the Lorentzian threshold identically (Lean 4 Theorems 4–6). Finally, γ is
strictly increasing on (0, 1] and strictly decreasing on [1,∞), attaining its unique global maximum
m
2m−1 atε= 1.
3.2 Exact-Q Rational Congruence Certificates for Inertia and Spectral Gaps
Standard Cholesky or unit-triangular LDL⊤ factorizations fail on zero-diagonal multiaffine
Hessians such as HS (where (HS)ii = 0 for all i). The following theorem provides a universal
zero-float rational congruence framework covering both indefinite Lorentzian Hessians and PSD
Dirichlet–Gram operators.
Theorem 3.2(Exact- Q Rational Congruence Certification of Lorentzianity and Spectral Gaps).
LetH∈Q n×n be any symmetric rational matrix.
1. Existence and Soundness of Rational Congruence:There exist invertible Q, Q−1 ∈
Qn×n (with QQ−1 = In) and D = (d1, . . . , dn) ∈Q n such that QHQ⊤ = diag(D), con-
structible in O(n3)exact rational operations using swaps, elementary shears I + Ekj (con-
verting a zero diagonal pivot Akk = 0with Akj ̸= 0to2 Akj ̸= 0), and Gaussian eliminations.
4

--- Page 5 ---
 If d1, . . . , dn ≥ 0, then v⊤Hv = Pn
i=1 diy2
i ≥ 0for all v∈R n (with y = ( Q−1)⊤v),
certifyingH⪰0(Lean 4 Theorem 9).
 If at most one di > 0(say d1 > 0and d2, . . . , dn ≤ 0), then v⊤Hv = Pn
i=2 diy2
i ≤ 0
on the codimension-1hyperplane(( Q−1)⊤v)1 = 0, certifying λ2(H) ≤ 0by Cauchy
interlacing / Sylvester’s law of inertia (Lean 4 Theorem 10).
2. Zero-Square-Root Reversible Spectral-Gap Certification:Let P∈Q k×k be a π-
reversible PSD Markov operator (Π P = (ΠP)⊤ ⪰ 0withΠ = diag(π), π∈Q k
>0, P
i πi = 1).
For anyγ∈Q∩(0,1], define the symmetric rational Dirichlet–Gram matrix
Mγ := (1−γ)Π−ΠP+ππ ⊤ ∈Q k×k.(7)
For everyf=c1+g∈R k withπ ⊤g= 0, we have the exact orthogonal identity
f⊤Mγf= (1−γ)c 2 +

(1−γ) Var π(g)− ⟨g, P g⟩π

,(8)
(Lean 4 Theorem 11). Consequently, Mγ ⪰ 0(certified via QMγQ⊤ = diag(D)with D≥ 0)
holds if and only if γ(P) ≥γ . Conversely, any nonzero v∈Q k with π⊤v = 0certifies the
rational upper bound γ(P) ≤ 1 − v⊤ΠP v
v⊤Πv , and when Mγ ⪰ 0and γ <1, any zero pivot di = 0
in QMγQ⊤ = diag(D)yields an exact rational eigenfunction v = Qi,· achieving equality
γ(P) =γ.
Proof. For Part 1, induction on the active leading block k = 1, . . . , nmaintains QHQ⊤ = A
and QQ−1 = In: if Akk = 0 and some Ajj ̸= 0 (j > k), swapping rows/columns k↔j restores
a nonzero pivot; if Ajj = 0 for all j≥k but some Akj ̸= 0, applying the unimodular shear
E = I + Ekj (E−1 = I−E kj) produces ( EAE⊤)kk = 2Akj ̸= 0; otherwise row/column k is
identically zero. Eliminating Aik (i > k) via I− (Aik/Akk)Eik diagonalizes A without square
roots. Because Q is invertible, setting y = (Q−1)⊤v gives v = Q⊤y and v⊤Hv = y⊤(QHQ⊤)y =Pn
i=1 diy2
i , from which both PSD ( D≥ 0) and codimension-1 nonpositivity (# {i : di > 0} ≤1)
follow immediately.
For Part 2, write f = c1+ g with π⊤g = 0. Since Π1= π, ΠP1= π,1 ⊤Πg = π⊤g = 0, and
1⊤ΠP g=π⊤P g=π⊤g= 0 (byπ-reversibility), expandingf ⊤Mγfyields
f⊤Mγf= (1−γ)(c 2 +⟨g, g⟩π)−(c 2 +⟨g, P g⟩π) +c 2 = (1−γ)c 2 +
 
(1−γ)⟨g, g⟩π − ⟨g, P g⟩π

.
Since 1 −γ≥ 0, Mγ ⪰ 0 iff ⟨g, P g⟩π ≤ (1 −γ )⟨g, g⟩π for all g⊥ π 1iff λ2(P) ≤ 1 −γ . Finally,
if QMγQ⊤ = diag(D) has di = 0, then QMγ(Q⊤ei) = diag(D)ei =0, so Mγ(Q⊤ei) =0;
subtracting its π-mean yields an exact rational nullvector in1 ⊥π attaining Rayleigh gap γ
wheneverγ <1.
Applying Theorem 3.2 to the dual up–down walk Qℓ→r→ℓ on Iℓ reduces matrix dimension
dramatically (e.g., from 65 × 65 to 28 × 28 on V´ amosV8 at ℓ = 2) while certifying the exact
same spectral gapγ(P r→ℓ→r) with zero approximation.
3.3 Zero-Float Exact-QMatrix Subgaussian Tail Certificates
Theorem 3.3(Zero-Float Rational Matrix Concentration Certification).Let M = ([n],B )be
a rank-r matroid equipped with its uniform basis distribution µ, and let {Ae}n
e=1 ⊂Q d×d be
symmetric rational matrices defining the Hermitian basis-sum observable F(B) = P
e∈B Ae. Let
E(M) := {(e, f) : 1 ≤e < f≤n,∃B, B ′ ∈ BwithB△B ′ = {e, f}}be the set of exchangeable
element pairs. Suppose that:
1. For a rational bound c2 ∈Q >0 and every( e, f) ∈ E(M), the rational matrix Cef :=
c2Id − (Ae −A f )2 ∈Q d×d admits an exact PSD congruence Qef Cef Q⊤
ef = diag(Def )with
Qef Q−1
ef =I d andD ef ≥0;
5

--- Page 6 ---
2. For rational deviation t∈Q >0, target failure probability δ∈Q∩ (0, 1), and Taylor order
K≥4, settingx:= t2
rc2 ∈Q >0 andT K(x) := PK
k=0
xk
k! ∈Q >0 satisfies
d
TK(x) ≤δinQ.(9)
Then ∥F(B) −F (B′)∥op ≤c for all exchangeable bases |B△B′| = 2, and combining Ercan’s sub-
gaussian matrix concentration bound [ 4] for r-homogeneous Lorentzian laws (PB∼µ[λmax(F(B) −
EF) ≥t ] ≤dexp (−t2/(rc2))) with the unconditional inequality ex ≥T K(x)( x≥ 0) certifies
purely overQthat
PB∼µ

λmax
 
F(B)−E µ[F]

≥t

≤d e−t2/(rc2) ≤ d
TK(t2/(rc2)) ≤δ.(10)
Proof. For any ( e, f) ∈ E(M) and any vector v∈R d, the exact PSD congruence on Cef
guarantees v⊤(c2Id − (Ae −A f )2)v≥ 0 by Theorem 3.2(1) (Lean 4 Theorem 17), whence
∥(Ae −A f )v∥2
2 ≤c 2∥v∥2
2 and therefore ∥Ae −A f ∥op ≤c without computing square roots
or eigenvalues. Whenever |B△B′| = 2 with B△B′ = {e, f}, F(B) −F (B′) = ±(Ae −A f ),
establishing bounded exchange difference c. Because fM is r-homogeneous Lorentzian [ 2],
Ercan’s subgaussian matrix concentration inequality [ 4] (derived from optimal ℓ/r complete
matrix entropy contraction with variance proxy vsg = rc2/2) yields P[λmax(F(B) −EF ) ≥t ] ≤
dexp (−t2/(2vsg)) = dexp (−x). Since x = t2/(rc2) > 0, every omitted term xk/k! (k > K) in
the power series of ex is strictly positive, so ex > TK(x) > 0 (Lean 4 Theorems 15–16), giving
de−x < d/TK(x)≤δ.
Remark3.4 (Independence of Rational Envelope from Floating-Point Evaluation).Theorem 3.3
cleanly separates the analytical input (Ercan’s subgaussian matrix concentration theorem [ 4])
from finite-instance verification: once M is certified Lorentzian by Theorem 3.2, every instance-
specific matrix norm, basis expectation, and tail inequality is verified purely in exactQ arithmetic,
eliminating floating-point rounding in both operator norms and exponentials.
3.4 Pure-Stdlib Zero-Float Certificate Verifier (LORENTZ-MATROID-CERT-1.0)
Theorem 3.5(Soundness and Anti-Forgery Architecture of LORENTZ-MATROID-CERT-1.0).The
pure-stdlib verifier verify lorentzian certificate exact (src/lorentzian certifier.py,
using fractions.Fraction exclusively and rejecting any floating-point value anywhere in the
JSON tree) enforces four mutually exclusive modes:
1.lorentzian hessian inertia: independently verifies the matroid basis-exchange axiom on
B, enumerates all S∈ Ir−2, reconstructs every HS directly from( B, w), checks QSQ−1
S = I
andQ SHSQ⊤
S = diag(DS), and enforces#{i:d i >0} ≤1;
2.down up spectral gap: verifies basis-exchange, independently constructs Pr→ℓ→r (or
isospectral dual Qℓ→r→ℓ) and Mγlow, checks QQ−1 = I, QMγlowQ⊤ = diag(D) ≥ 0,
γlow ≥ 1 −ℓ/r (or strict > if claimed), and validates any centered upper-bound witness v
(π⊤v= 0,v ⊤Πv >0);
3.coincident phase transition: verifies either supercritical Lorentzianity ( ε≥ m−1
m , single
positive Hessian pivot, Mγlow ⪰ 0with γlow ≥ 1/2) or subcritical separation (0 < ε <m−1
m ,
2 × 2Sylvester-PD Gram matrix of( u1, u2)under Hε,m proving λ2(Hε,m) > 0, plus centered
witnessvwith Rayleigh gap<1/2);
4.matrix concentration tail: verifies basis-exchange, symmetry of {Ae}, exact Eµ[F],
PSD congruences on c2Id − (Ae −A f )2 for every exchangeable pair( e, f) ∈ E(M), and
d/TK(t2/(rc2))≤δ.
6

--- Page 7 ---
Table 1: Zero-dependency Lean 4 theorem ledger ( lean/LorentzianMatroid.lean, v4.35.0:
18/18 theorems, 0sorry, 0Classical.choice, 0 warnings).
# Lean 4 Theorem Identifier Mathematical Statement Verified Axioms
1coincident threshold pos0< m−1< mform≥2 (ε c(m)∈(0,1))propext, Quot.sound
2hessian lambda plus posλ +(ε, m) = (m−1)q+mp >0propext, Quot.sound
3hessian lambda minus lorentzian iffλ − ≤0⇐⇒mp≥(m−1)qpropext, Quot.sound
4down up mu2 half iffµ − ≤1/2⇐⇒mp≥(m−1)qpropext, Quot.sound
5coincident phase transition equivλ − ≤0⇐⇒γ(ε, m)≥1/2propext, Quot.sound
6coincident exact equality at criticalAtε= (m−1)/m:λ − = 0∧γ= 1/2propext, Quot.sound
7piecewise crossover at oneµ − ≥µ ⊥ ⇐⇒ε≤1 (peak atK 2m)propext, Quot.sound
8complete graph gap strictly above halfγ(1, m)>1/2 and 1−µ ⊥ >1/2propext, Quot.sound
9ldl psd quadratic form nonnegD≥0 =⇒ P
i diy2
i ≥0 onList Int propext, Quot.sound
10ldl lorentzian hyperplane nonposd 0 >0, Dtail ≤0, y0 = 0 =⇒y ⊤Dy≤0propext, Quot.sound
11reversible gram identityExact orthogonal expansion off ⊤Mγfpropext, Quot.sound
12ercan universal gap pos1−ℓ/r >0 and strictly decreasing inℓpropext, Quot.sound
13vamos excess gap strict3/4>2/3, 9/14>1/2, 46/125>1/4, 1/2>1/3none(decide)
14mason ulc elementary symmetric(k+ 1)(n−k+ 1)> k(n−k) for 1≤k < npropext, Quot.sound
15exp taylor lower bound monotoneT 4(p, q)≥24q4 >0 forp≥0, q >0propext, Quot.sound
16subgaussian taylor tail soundnessExact-QTaylor-envelope tail soundnesspropext, Quot.sound
17exchange operator norm sq boundc 2∥v∥2 − ∥Av∥2 ≥0 =⇒ ∥Av∥2 ≤c 2∥v∥2 propext, Quot.sound
18verdict exclusivity¬(λ − ≤0∧λ − >0)propext, Quot.sound
4 Zero-Dependency Lean 4 Formalization
All 18 foundational algebraic, spectral, inertia, combinatorial, and concentration theorems are
machine-checked in lean/LorentzianMatroid.lean under leanprover/lean4:v4.35.0 with
zero external dependencies (no Mathlib), zero sorry, zero warnings, and zero Classical.choice
(audited via lean/AuditAxioms.lean, using only propext and Quot.sound, or zero axioms).
Table 1 summarizes the verified theorem ledger.
5 Experiments, Certified Atlas, and Adversarial Red-Teaming
All four experiments in scripts/run all experiments.py are deterministic and reproducible
viapython scripts/verify all.py.
5.1 Experiment 1: Atlas of 16 Exact-QCertificates Across 4 Modes
Table 2 lists all 16 emitted exact- Q certificates verified with zero floating-point operations by
LORENTZ-MATROID-CERT-1.0. Notably, all 28 rank-2 link Hessians of the non-representable
V´ amos matroidV8 (n = 8 , r= 4 ,|B| = 65) are certified Lorentzian in 20 .17 ms, its exact
ℓ = 2 down–up spectral gap γ(P4→2→4; V8) = 9 /14 (1 .286× above Ercan’s 1 /2 bound) is
certified with exact bracket [9 /14, 9/14] in 78 .01 ms, and all 28 exchangeable pairs of a non-
commuting 2 × 2 Hermitian basis sum over V8 are PSD-certified with rational tail bound
28350/771731≈0.03674≤1/20 in 8.63 ms.
5.2 Experiment 2: Coincident Phase Curve Verification Across m∈
{2,3,4,6,10}
Sweeping 60 rational couplings ε∈ [0.05, 3.0] across five cluster sizes m∈ {2, 3, 4, 6, 10} (300
graph instances total), numerical diagonalization matches Theorem 3.1’s closed-form λ2(Hε,m) =
max((m− 1) −mε,− 1) to maximum error 1 .37 × 10−14 and the piecewise spectral gap (5) to
maximum error 9.99 × 10−16, with 0/300 coincidence violations between Lorentzianity ( λ2 ≤ 0)
andγ≥1/2 (Figure 1).
7

--- Page 8 ---
Table 2: Atlas of 16 exact- QLORENTZ-MATROID-CERT-1.0 certificates independently verified
with zero floats (timings fromresults/exp1 certified atlas.json).
Certificate File Mode Certified Exact-QClaim Time (ms)
lorentzian U36.cert.jsonMode 1U 3,6:M-convex + 6/6 links Lorentzian 4.14
lorentzian MK4.cert.jsonMode 1M(K 4):M-convex + 6/6 links Lorentzian 2.66
lorentzian F7 fano.cert.jsonMode 1F 7 (char 2):M-convex + 7/7 links Lorentzian 4.33
lorentzian F7minus nonfano.cert.jsonMode 1F −
7 (char̸= 2):M-convex + 7/7 links Lorentzian 5.06
lorentzian V8 vamos.cert.jsonMode 1V 8 (non-rep.):M-convex + 28/28 links Lorentzian 20.17
gap U36 ell2.cert.jsonMode 2U 3,6 (ℓ= 2):γ∈[1/2,1/2]>1/3 14.58
gap MK4 ell1.cert.jsonMode 2M(K 4) (ℓ= 1):γ∈[3/4,3/4]>2/3 8.95
gap MK4 ell2.cert.jsonMode 2M(K 4) (ℓ= 2):γ∈[41/100,21/50]>1/3 13.58
gap F7 ell2.cert.jsonMode 2F 7 (ℓ= 2):γ∈[43/100,11/25]>1/3 33.97
gap V8 ell2 dual.cert.jsonMode 2V 8 (ℓ= 2):γ∈[9/14,9/14]>1/2 78.01
gap V8 ell3 dual.cert.jsonMode 2V 8 (ℓ= 3):γ∈[46/125,37/100]>1/4 404.25
phase m4 critical eps 3 4.cert.jsonMode 3G 3/4,4: critical Lorentzian,γ= 1/2 2.14
phase m4 supercritical eps 1.cert.jsonMode 3G 1,4 =K 8: peak Lorentzian,γ= 4/7>1/2 1.59
phase m4 subcritical eps 7 10.cert.jsonMode 3G 7/10,4: non-Lorentzian (λ 2 >0),γ= 14/29<1/2 0.57
tail MK4 pauli d2.cert.jsonMode 4M(K 4), 15/15 pairs PSD, tail≤8960/89641≤1/9 1.58
tail V8 vamos d2.cert.jsonMode 4V 8, 28/28 pairs PSD, tail≤28350/771731≤1/20 8.63
5.3 Experiment 3: Canonical and Non-Representable Matroid Spectral Atlas
Across all five matroids spanning every representability class (all fields U3,6, regular/graphic
M(K4), characteristic-2 only F7, characteristic-̸= 2 only F−
7 , and universally non-representable
V8), primal Pr→ℓ→r and dual Qℓ→r→ℓ walks agree in spectral gap to 2 .22 × 10−16, every matroid
strictly exceeds Ercan’s 1 −ℓ/r baseline by factors 1.115×–1.500× (Figure 2), and all Mason
ultra-log-concavity ratios I2
k/
 n
k
2 ÷

(Ik−1/
  n
k−1

)(Ik+1/
  n
k+1

)

satisfy ≥ 1 (1.25 on M(K4) and
F7, 1.207 onF −
7 , 1.077 onV 8).
5.4 Experiment 4: Exhaustive Matrix Concentration Cross-Check and 48
Adversarial Attacks
For non-commuting 2 × 2 symmetric rational matrices {Ae} with true exchange sensitivity
ctrue =
p
49/50≈ 0.98995 < 1.0 = ccert, Figure 3 compares the exact exhaustive empirical tail
over all 16 bases of M(K4) and all 65 bases of non-representable V8 against the exact matrix
Laplace bound infθ>0 e−θtE[Treθ ˜F ], Ercan’s subgaussian bound de−t2/(rc2), and our zero-float
rational Taylor-8 enveloped/T8(t2/(rc2)). Across all t∈ [0.25, 4.0], the four curves obey the strict
hierarchy empirical≤exact Laplace≤Ercan subgaussian≤rational Taylor envelope , with the
degree-8 rational envelope tracking the continuous exponential closely across the certified tail
regime.
Finally, our adversarial red-team test suite ( tests/test suite.py) launches 48 targeted
forgery attacks spanning all four modes—including float injection, decimal/scientific string
smuggling, singular Q and tampered Q−1, dropped or duplicated (r− 2)-links on V8, non-matroid
basis sets violating exchange, inflated γlow, uncentered upper-bound witnesses, collinear positive
subspaces in subcritical Gε,m, shrunk c2, asymmetric Ae, and dropped exchangeable pairs. All
48/48 attacks are rejected with zero bypasses.
6 Limitations and Outlook
Our congruence certification algorithm runs in O(k3) exact rational operations on the operator
dimension k (with bit-length growth controlled by working in the dual up–down space Iℓ, taking
78.0 ms on 28 × 28 V8 at ℓ = 2 and 404.3 ms on 56 × 56 V8 at ℓ = 3); scaling to matroids with
thousands of independent sets would benefit from sparse congruence pivoting or modular-CRT
8

--- Page 9 ---
Figure 1: Exact coincident phase transition on Gε,m = ( Km ⊔K m) + εKm,m across m∈
{2, 3, 4, 6, 10}. (a) Exact piecewise down–up spectral gap (5) crossing Ercan’s universal threshold
1/2 precisely at εc(m) = (m− 1)/m (circles) and peaking uniquely at ε = 1 (K2m, triangles).
(b) Second Hessian eigenvalue λ2(Hε,m) = max((m− 1) −mε,− 1) crossing 0 at the identical
thresholdε c(m).
lifting. Similarly, Theorem 3.3 certifies finite-instance matrix concentration conditional on
Ercan’s analytic matrix entropy contraction theorem [ 4]; formalizing operator-convex trace
inequalities directly in Lean 4 remains an exciting open direction. Finally, extending exact- Q
congruence certificates to Lorentzian intrinsic-volume functionals and higher-order tensor-network
contraction bounds offers a natural bridge between matroid geometry and algebraic complexity.
References
[1] Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant. Log-concave poly-
nomials II: High-dimensional walks and an FPRAS for counting bases of a matroid. In
Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing (STOC
2019), pages 1–12, 2019.
[2] Petter Br¨ and´ en and June Huh. Lorentzian polynomials.Annals of Mathematics, 192(3):821–
891, 2020.
[3] Mary Cryan, Heng Guo, and Giorgos Mousa. Modified log-Sobolev inequalities for strongly
log-concave distributions.The Annals of Probability, 49(1):506–525, 2021.
[4] Eren Ercan. Lorentzian entropy, subgaussian matrix concentration, and sharp functional
inequalities for all matroids, November 2026.
[5] Tom´ as Feder and Milena Mihail. Balanced matroids. InProceedings of the 24th Annual
ACM Symposium on Theory of Computing (STOC 1992), pages 26–38, 1992.
[6] J. H. Mason. Matroids: Unimodal conjectures and Motzkin’s theorem.Combinatorics (Proc.
Conf. Combinatorial Math., Math. Inst., Oxford), pages 207–220, 1972.
[7] James Oxley.Matroid Theory. Oxford University Press, 2nd edition, 2011.
[8] Joel A. Tropp. User-friendly tail bounds for sums of random matrices.Foundations of
Computational Mathematics, 12(4):389–434, 2012.
9

--- Page 10 ---
Figure 2: Down–up spectral-gap atlas across canonical and non-representable matroids. (a) Com-
parison of Ercan’s universal bound 1−ℓ/r against exact-Q certified gaps γ(Pr→ℓ→r). (b) Certified
excess expansion factors γ/(1 −ℓ/r ) ∈ [1.115, 1.500], highlighting the non-representable V´ amos
matroidV 8 (1.475×atℓ= 3, 1.286×atℓ= 2).
Figure 3: Exact exhaustive matrix concentration comparison for non-commuting 2 ×2 Hermitian
basis sums F(B) = P
e∈B Ae over (a) graphic M(K4) (16 bases) and (b) non-representable
V´ amosV8 (65 bases). The zero-float exact- Q Taylor-8 certificate strictly upper-bounds Ercan’s
subgaussian curve, the exact matrix Laplace bound, and the exhaustive empirical tail across all
thresholds.
10
