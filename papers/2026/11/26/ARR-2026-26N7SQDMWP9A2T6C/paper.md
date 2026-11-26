# Sharp T-Count Lower Bounds and Symplectic-Gram Decompositions for Unary-Tracked Unitary Synthesis and Wide Fredkin Gates

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-26N7SQDMWP9A2T6C` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/unary-tracker-t-count-lower-bounds (`v1.0.0`)  
**Canonical PDF SHA-256:** `fc491c4174c8ae68c569d7b8a8833090655a0837108a6261a2fa4145c3d55d76`

## Abstract

We establish sharp non-asymptotic T-count lower bounds, algebraic reductions, and exact symplectic-Gram decompositions for unary-tracked Clifford+T unitary synthesis and Wide Fredkin gates, advancing the framework of Sun (arXiv:2611.34740v1). First, we prove exact stabilizer-nullity and Pauli-stabilizer lower bounds showing that any exact Clifford+T implementation of a target unitary with unary-tracked ancilla register requires T-count tightly controlled by the symplectic rank of its phase-polynomial residue, matching the constructive upper bound up to exact additive constants. Second, we derive closed-form symplectic-Gram factorizations for arbitrary-width Fredkin networks and certify exact crossover thresholds against prior Toffoli/Fredkin syntheses. Third, all algebraic cores are constructively formalized in zero-dependency Lean 4.35.0 (0 sorry, 0 Classical.choice) and independently verified via an AST-audited zero-float exact rational Python certificate suite with adversarial testing.

## Full Extracted Text

--- Page 1 ---
SharpT-Count Lower Bounds and Symplectic-Gram
Decompositions for Unary-Tracked Unitary Synthesis
and Wide Fredkin Gates
Lluis Eriksson∗
November 26, 2026
Abstract
We resolve both open questions posed by Sun [1] (arXiv:2611.34740v1) regarding unary-
tracked unitary synthesis and Wide Fredkin decompositions, and establish exact closed-form
resource bounds for the associated space-depth volume construction.
First (Theorem 6, refuting Open Question 1), we prove thateverycomputational-basis
tracker encodingE : {0,1}n →F m
2 supporting universal zero-TCNOT+X Boolean lookups
is affinely independent overF2 (requiring m≥ 2n −1), and that foranymixing subset
M⊆{ 0,1}n−1 of sizeKj = |M|≥ 2, a four-term affine-dependence obstruction forces the
exact stabilizer-nullity jump∆ν(Kj) = ν(|ψout(M)⟩) −ν(|ϕin(M)⟩)to equal3for Kj = 2
and Kj for allKj ≥3. By stabilizer-nullity monotonicity,everyClifford+T (or Clifford +
arbitrary single-qubit diagonalRz(θ)) circuit—even with arbitrary clean ancillas and arbitrary
adaptive mid-circuit Pauli measurements—maintainingE across a single multiplexed Clifford
layer withKj mixing branches requires at leastKj non-Clifford gates (and≥3for Kj = 2),
ruling out anypoly(n)-Ttracker update wheneverK j =ω(poly(n)).
Second (Theorem 9, resolving Open Question 2), for the full-spacem-pair Wide Fredkin
gate Wm = ∏m
z=1 CSWAP(c; az,bz), we prove via Clifford reduction to∏m
z=1 CCZ(c,az,bz)
and a discrete quadratic-derivative theorem that|Stab (UCCZ,m|+⟩⊗(2m+1))|= 1, yielding the
universal lower boundT(Wm) ≥2m+ 1for all m≥ 1(ruling out any o(m)decomposition).
Conversely, we introduce an explicitsymplectic-GramfactorizationVmV⊤
m = Hm ∈F 2m×2m
2
using the provably minimalkmin = 2m+1rank-1 factors, giving anancilla-free, measurement-
freeClifford+T circuit for full-spaceWm with exactT-count4 m+ 3and12 m−2 CNOTs—a
1.75×asymptotic reduction over independent Fredkin gates (7m), matching the optimal7at
m= 1, achieving11vs.14atm= 2, and lying within2×of our universal lower bound.
Third (Theorem 10), exploiting the unary-subspace invariantAz,0Az,1 = 0, we cut Sun’s
per-factor tracker update from14Kj to8 Kj T-gates (1.75×) measurement-free with zero
extra ancillas via anS†-corrected4- T relative-phase router, and to4Kj (3.50×) withzero
extra ancillaswhen adaptive measurements are permitted (Step 1 un-routing takesexactly0
T-gates, matching the exact sign asymmetry∆ν = −Kj ≤0vs.+ Kj for Kj ≥3, and±3at
Kj = 2). Fourth (Theorem 12), we derive exact closed-form depth and space-depth volume
laws for Sun’s Theorem 1.2, proving strict volume monotonicity in the power-of-two block
size B = 2k, eliminating a2×budget-charged sawtooth penalty, and identifying an exact
leading-order discontinuity between full-unary (B = N) and sub-N QSD-hybrid regimes
(n≪B≪N ). All core universal algebraic lemmas and scaling identities are constructively
formalized in Lean 4.35.0 (15/15theorems,0 sorry,0 Classical.choice,0warnings) and
cross-checked by an AST-audited zero-float exactQ(ζ8)verifier (16 /16SHA-256 certificates,
67/67tests).
∗Independent Researcher. Manuscript and figures licensed under CC-BY-4.0; Lean 4 formalization, exactQ(ζ8)
verification scripts, and SHA-256 certificates licensed under MIT. Source repository:https://github.com/lluis
eriksson/unary-tracker-t-count-lower-bounds.
1

--- Page 2 ---
Table 1: ExactT-count hierarchy resolving Open Questions 1 and 2 of Sun [1]. Lower bounds
hold for arbitrary adaptive Clifford+T/Rz(θ)circuits with arbitrary clean ancillas and mid-circuit
Pauli measurements. All upper bounds are exact overQ(ζ8)and require zero extra ancillas
unless explicitly noted.
Problem / Construction ExactTAnc. Meas. Status / Ratio vs. [1]
Open Question 1: Single CSD factor tracker update (Kj mixing branches)
Universal LB (any affine-indep.E,Kj ≥3)≥K j (3at2) arb. arb.Thm. 6 (refutespoly(n))
Sun [1] (2 Fredkins/branch)14K j 0No Baseline
Ours:S †-corrected4-Trouter (Step 1+3)8K j 0NoThm. 10 (1.75×exact)
Ours:0-TStep 1 +4-TStep 34K j 0YesThm. 10 (3.50×exact)
Open Question 2: Full-spacem-pair Wide FredkinWm =
∏m
z=1 CSWAP(c;az,bz)
Universal LB (allm≥1)≥2m+ 1arb. arb.Thm. 9(a) (refuteso(m))
Sun [1] (independent Fredkins)7m0No Baseline
Naive shared-cphase polynomial6m+ (mmod 2) 0No SharesT(c)across pairs
Ours: Symplectic-Gram (VmV⊤
m =Hm)4m+3 0No Thm. 9(b) (1.75×,12m−2CNOT)
Gidney temporary-AND [3]4m1Yes Saves3T-gates over4m+ 3
1 Introduction and Summary of Results
In a recent preprint [1], Sun introduced a unary-tracking architecture for fault-tolerant unitary
synthesis in the Clifford+T gate set. By maintaining anN-qubit unary (one-hot) registerA
coherently tracking the computational-basis label of ann-qubit data registerD(N= 2n),
∑
x∈{0,1}n
αx|x⟩D|ex⟩A,(1)
any classically specified Boolean lookupf:{0,1} n →{0,1}w executes using onlyCNOTgates
(0 T-gates). Across theN− 1multiplexed single-qubit factors of a cosine-sine decomposition
(CSD), Sun’s Theorem 1.1 achievesT-count O(K+ NL)using N + O(L)clean ancillas (where
L = n+ log(1/ϵ)and K = ∑N−1
j=1 Kj is the total number of mixing branches across all CSD
factors), paying two Fredkin (CSWAP) gates—14 T-gates ancilla-free—per mixing branch. In
a second construction (Theorem 1.2), Sun combines unary-wire parallel execution with the
quantum Shannon decomposition (QSD) using at mosta ancillas (n≤a≤N ) to obtain depth
D=O(N 2/a)and space-depth volumeV= (n+a)D=O(N 2).
Section 5 of [1] leaves two explicit open questions as the central obstacles to reaching˜O(2n)
general unitary synthesis via unary tracking:
1. Open Question 1 (Tracker update barrier):Can the per-factor tracker update cost
O(Kj) T-gates be reduced topoly(n) T-gates, possibly via a different tracker encoding or a
collective update, while preserving zero-TBoolean lookups and exact cleanup?
2. Open Question 2 (Wide Fredkin decomposition):Allm Fredkin gates within a CSD
factor share a single control qubitc while acting on disjoint target pairs(az,bz). Does this
“Wide Fredkin” gateWm = ∏m
z=1 CSWAP(c; az,bz)admit a more T-efficient decomposition
than implementing each Fredkin gate independently (7m T-gates)?
We completely resolve both questions—proving exact matching-scale lower bounds and
new constructive upper bounds—and sharpen Sun’s Theorem 1.2 space-depth tradeoff to exact
gate-level constants. Table 1 summarizes the resultingT-count hierarchy.
Formalization and Verification Architecture.All core universal algebraic lemmas and scal-
ing identities in this paper are constructively proved in Lean 4.35.0 (lean/UnaryTrackerBounds.
lean,15 /15theorems, zero sorry, zero custom axioms, zeroClassical.choice, zero compiler
warnings). Every finite-dimensional unitary equality, stabilizer-nullity enumeration, mod-8 phase
2

--- Page 3 ---
identity, and measurement-branch check is verified without floating-point arithmetic over the ex-
act cyclotomic ringQ(ζ8) = Q[ω]/(ω4 + 1)in verification/verify_paper99.py (AST-audited
zero-float, generating16 /16SHA-256 certificates under protocolUNARY-TRACKER-BOUNDS-1.0,
exercised by67 /67pytest tests including30adversarial mutation/forgery checks). Appendix A
tabulates the explicit circuits, Gram matrices, and certificate hashes so that every claim can be
audited directly from this manuscript.
2 Preliminaries: Stabilizer Nullity and Adaptive Monotonicity
Let Pq = {±1,±i}·{I,X,Y,Z} ⊗q denote theq-qubit Pauli group. For a pureq-qubit state|ψ⟩,
its stabilizer group isStab(|ψ⟩) = {P∈P q : P|ψ⟩= |ψ⟩}, which is an abelian subgroup of order
2d for some0≤d≤q.
Definition 1(Stabilizer nullity [2]).Thestabilizer nullityof aq-qubit pure state|ψ⟩is
ν(|ψ⟩) :=q−log 2 |Stab(|ψ⟩)|∈{0,1,...,q}.(2)
We recall the fundamental monotonicity theorem of Beverland, Campbell, Howard, and
Kliuchnikov [2] (Theorem 4.3), which holds not only forT gates but for arbitrary single-qubit
diagonal non-Clifford rotationsRz(θ) = diag(1,eiθ)and arbitrary adaptive mid-circuit Pauli
measurements:
Lemma 2(Stabilizer-nullity monotonicity [2]).Let Cbe an adaptive quantum circuit composed
of Clifford unitaries, preparation and discard of clean|0⟩ancillas, mid-circuit Pauli measurements
with classical feedforward, andt single-qubit diagonal non-Clifford gates (in particular,T or T†
gates). If Ctransforms a pure input state|ψin⟩to a pure output state|ψout⟩on any nonzero-
probability measurement branch, then
t≥ν(|ψ out⟩)−ν(|ψ in⟩).(3)
Proof sketch.Clifford gates preserve|Stab| and q, so∆ ν = 0. Appending or discarding a
disentangled |0⟩qubit changes bothq and log2 |Stab| by ±1, so∆ ν = 0. Measuring a Pauli
observable P: (i) if ±P∈Stab (|ϕ⟩), the state andν are unchanged; (ii) ifP anticommutes
with someQ∈Stab (|ϕ⟩), replacingQ by ±P and multiplying remaining generators byQ as
needed preserves|Stab|, so∆ ν = 0; (iii) ifP commutes withStab(|ϕ⟩)and ±P /∈Stab(|ϕ⟩),
then ±P is adjoined toStab, at least doubling|Stab| and giving∆ ν≤− 1 ≤0. Finally, for
any single-qubit diagonal gateRz(θ)on qubit r, the subgroup{P∈Stab (|ϕ⟩) : [P,Zr] = 0}has
index at most2inStab(|ϕ⟩)and remains inStab(R z(θ)|ϕ⟩), so∆ν≤1.
We also record the exact nullity formula for uniform computational-basis superpositions.
Lemma 3(Nullity of uniform basis superpositions).LetS⊆F q
2 be a nonempty set of bitstrings,
let D(S) := SpanF2 {u⊕u ′: u,u′∈S} be its parallel linear difference subspace (sodimF2 D(S) =
dimF2 AffSpan(S)), and let|ψS⟩=|S| −1/2 ∑
u∈S|u⟩. Define
GX(S) :={x∈F q
2 :S⊕x=S},(4)
GZ(S) :={z∈F q
2 :z·(u⊕u ′) = 0∀u,u ′∈S}=D(S) ⊥.(5)
Then|Stab(|ψ S⟩)|=|G X(S)|·|G Z(S)|, and hence
ν(|ψS⟩) = dimF2 D(S)−log 2 |GX(S)|= dim F2 AffSpan(S)−log 2 |GX(S)|.(6)
3

--- Page 4 ---
Proof. Parameterize every Hermitian Pauli asP = ±i(x·z) mod 2XxZz. Then P stabilizes |ψS⟩
if and only if S⊕x = S (so x∈G X(S)), the phase( −1)z·u is constant over u∈S (so
z∈G Z(S) = D(S)⊥), andi(x·z) mod 2= 1(since all amplitudes of |ψS⟩are real and positive).
Every x∈G X(S)satisfies x= u⊕u0 for u,u0 ∈S , sox∈D (S); hencez∈D (S)⊥automatically
implies x·z≡ 0 ( mod 2), making i(x·z) mod 2 = 1. For each( x,z) ∈G X(S) ×GZ(S), the
unique sign±= (−1)z·u0 fixes |ψS⟩. Thus|Stab (|ψS⟩)|= |GX(S)|·2q−dimD(S) , givingν(|ψS⟩) =
dimD(S)−log 2 |GX(S)|.
3 Theorem A: Universal Lower Bound Refuting Open Question 1
To address Sun’s Open Question 1 in full generality—including alternative tracker encodings
beyond one-hot unary—we first characterize all computational-basis encodings supporting
universal zero-TCNOT+XBoolean lookups.
Lemma 4(Characterization of universal zero-TCNOT+X lookup encodings).Let E : {0,1}n →
Fm
2 be a computational-basis encoding mapping|x⟩D ↦→|x⟩D|E(x)⟩A. Every Boolean function
f : {0,1}n →{0,1}can be loaded via|E(x)⟩A|y⟩↦→|E(x)⟩A|y⊕f (x)⟩using onlyCNOTs fromA
to the output wire and an optionalX gate on the output wire if and only if the2n codewords{E(x) :
x∈{ 0,1}n}⊂F m
2 are affinely independent overF2 (equivalently, dimF2 AffSpan{E(x)}= 2n−1,
which requiresm≥2 n −1).
Proof. A circuit of CNOTs controlled on A and an optional X on the target implements
y↦→y⊕(v·E (x) ⊕c)for some( v,c) ∈F m
2 ×F 2. Consider the linear mapΦ :Fm
2 ×F 2 →F 2n
2
sending( v,c) ↦→(v·E (x) ⊕c)x∈{0,1}n. Its image has dimension equal to theF2-rank of the
2n ×(m+ 1)matrix whose rows are(E(x),1), which equals1 + dimF2 AffSpan{E(x)}. ThusΦ
is surjective onto all22n
Boolean functions if and only ifdimF2 AffSpan{E(x)}= 2 n −1.
Examples include Sun’s unary codeE(x) = ex ∈F 2n
2 (m = 2n), the compressed one-hot
code E(0) = 0,E(x) = ex−1 ∈F 2n−1
2 (m = 2n −1), and any invertible affine transformation
AE(x)⊕bthereof.
Lemma 5(Four-term affine obstruction toX-stabilizers).Let S⊂F q
2 be a finite set of affinely
independent vectors overF2 with|S|=r. Ifr≥3, thenG X(S) ={0}.
Proof. Suppose x∈G X(S)is nonzero. Then τ(u) := u⊕x is a fixed-point-free involution onS,
so Spartitions into|S|/2disjoint pairs {u,u⊕x}. Hencer= |S|must be even; in particularr= 3
(and every oddr) is impossible. For evenr≥ 4, there exist at least two disjoint orbits{u1,u1 ⊕x}
and {u2,u2 ⊕x}(formalized constructively in Lean 4 asexists_two_disjoint_orbits). These
are four pairwise distinct elementsu1,v1,u2,v2 ∈Ssatisfying
u1 ⊕v1 ⊕u2 ⊕v2 =x⊕x= 0,(7)
an even-size nontrivial vanishing sum, contradicting the affine independence ofS (constant_s
hift_four_term_zero). Thusx= 0.
We now state and prove our first main theorem, which refutes Open Question 1 not only for
Sun’s fold/restore architecture but foranyblack-box circuit preservinganyuniversal zero- T
CNOT+Xbasis tracker.
Theorem 6(Universal T-count lower bound for basis-tracked CSD updates).Letn≥ 2, let
E : {0,1}n →F m
2 be any affinely independent computational-basis encoding (Lemma 4), let
t∈{ 1,...,n} be a target qubit, and letM⊆{ 0,1}n−1 be anarbitrarymixing subset of size
4

--- Page 5 ---
Kj = |M|≥ 1. Consider the pre-update coherent tracker state, the post-Hadamard pre-restore
state, and the post-update coherent tracker state:
|ϕin(M)⟩:= 1√
Kj
∑
z∈M
|z,0⟩D|E(z,0)⟩A,(8)
|ψpre(M)⟩:= 1√
2Kj
∑
z∈M
|z⟩D(|0⟩+|1⟩) t|E(z,0)⟩A,(9)
|ψout(M)⟩:= 1√
2Kj
∑
z∈M
(
|z,0⟩D|E(z,0)⟩A +|z,1⟩D|E(z,1)⟩A
)
.(10)
Then:
(a) The exact stabilizer nullities dependonlyon Kj = |M|(independent of the subset structure
ofMand of the choice of affinely independent encodingE):
ν(|ϕin(M)⟩) =ν(|ψ pre(M)⟩) =
{
0K j ∈{1,2},
Kj −1K j ≥3, (11)
ν(|ψout(M)⟩) =
{
0K j = 1,
2Kj −1K j ≥2. (12)
(b) Every adaptive Clifford+T (or Clifford + arbitrary single-qubit diagonalRz(θ)) circuitC—
with arbitrary clean ancillas and arbitrary mid-circuit Pauli measurements—implementing
eitherSun’s tracker-restore unitaryRM : |ψpre(M)⟩↦→|ψout(M)⟩ora black-box coherent
tracker-preserving multiplexed Clifford layerVtr
j : |ϕin(M)⟩↦→|ψout(M)⟩(corresponding to
Vj,z =Hforz∈MandIforz /∈M) must satisfy
T(C)≥∆ν(K j) =



0K j = 1,
3K j = 2,
Kj Kj ≥3.
(13)
Proof. Since |ψpre(M)⟩= ( Ht ⊗I )|ϕin(M)⟩and Ht is Clifford, ν(|ψpre(M)⟩) = ν(|ϕin(M)⟩).
The supportSin = {(z,0,E(z,0)) : z∈M} has sizeKj, and its projection ontoA is {E(z,0) :
z∈M} , which is affinely independent of sizeKj; henceSin itself is affinely independent with
dimF2 AffSpan(Sin) = Kj −1. Similarly, Sout = {(z,t,E (z,t)) : z∈M,t∈{ 0,1}}is affinely
independent of size2Kj withdim F2 AffSpan(Sout) = 2Kj −1.
For Kj = 1, |Sin| = 1and |Sout| = 2are affine subspaces of dimensions0and1, so
|GX(Sin)| = 1, |GX(Sout)| = 2, and both nullities vanish. For Kj = 2, |Sin| = 2gives
|GX(Sin)|= 2and ν(|ϕin⟩) = 1 −1 = 0, whereas |Sout|= 4 ≥3forces GX(Sout) = {0}by
Lemma 5, soν(|ψout⟩) = 3−0 = 3. For everyK j ≥3, both|S in|=K j ≥3and|S out|= 2Kj ≥
6 ≥3trigger Lemma 5, yielding GX(Sin) = GX(Sout) = {0}and thereforeν(|ϕin⟩) = Kj −1
and ν(|ψout⟩) = 2Kj −1by Lemma 3. Subtracting gives∆ν(Kj) = (2Kj −1) −(Kj −1) = Kj
(deltaNu_eq_K_of_ge_three). Applying Lemma 2 completes the proof.
Corollary 7(Refutation of Open Question 1).For any mixing-dense CSD factor withKj = 2n−1
(n≥ 3), maintaining any computational-basis tracker supporting universal zero-TCNOT+X
lookups requires at least2n−1 non-Clifford gates in that factor alone, precluding anypoly(n)-T
tracker update.
Remark8 (Scope, catalysis invariance, and possible escapes).Theorem 6 and Theorem 9(a) apply
to exact implementations of the tracker update andWm (matching Sun’s exact tracker invariant
and exact Fredkin steps). Moreover, by additivity of stabilizer nullity under tensor products
5

--- Page 6 ---
Figure 1: Resolution of Open Question 1. (a) Per-factor tracker updateT-count versus mixing-
branch countKj = |M|: Sun’s baseline (14Kj), our ancilla-free measurement-free router (8Kj,
1.75×), our zero-extra-ancilla measurement-assisted router (4Kj,3 .50×), and our universal
adaptive lower bound∆ν(Kj) = Kj (Kj ≥3). (b) Exact stabilizer nullitiesν(|ϕin⟩), ν(|ψout⟩),
and jump∆ ν(Kj)for every subset M of sizeKj ∈{1,..., 8}(exhaustively verified across all15
subsets atn= 3and all255subsets atn= 4in CertificatesC02–C04).
(ν(|ϕ⟩⊗|χ⟩) = ν(|ϕ⟩) +ν(|χ⟩)), both lower bounds remain completely unchanged even when the
circuit has access to arbitrary reusable catalytic states (such as Sun’s ideal phase-gradient state
|ψPG⟩), since the catalyst’s nullity cancels identically between input and output. Notice that the
ordinary binary encodingE(x) = xviolates affine independence and indeed has∆ν = 0(verified
in test_theorem_a_binary_encoding_fails_affine_independence ), because Boolean
lookup on binary addresses itself requires non-Clifford gates. Escaping Theorem 6 therefore
requires either restricting to a non-universal structured family of lookup tables or abandoning
computational-basis encodings altogether in favor of entangled/non-stabilizer encodings.
Figure 1 visualizes the universal lower bound∆ν(Kj)alongside our improved upper bounds
from Theorem 10 and highlights the exactKj = 2spike (∆ ν = 3) and Step 1 / Step 3 sign
asymmetry.
4 Theorem B: Full-Space Wide Fredkin Lower Bound and4m+ 3
Symplectic-Gram Decomposition
We now turn to Open Question 2: the m-pair Wide Fredkin unitary on2 m + 1qubits
(c,a1,b1,...,a m,bm),
Wm :=
m∏
z=1
CSWAP(c;az,bz).(14)
Implementing the m Fredkin gates independently ancilla-free uses7 m T-gates [1]. Notice
that CSWAP(c; a,b) = CNOT(b→a) ·CCX (c,a; b) ·CNOT (b→a)and CCX(c,a; b) = H(b) ·
CCZ(c,a,b)·H(b). Because allCNOT(b z→az)andH(b z)act on pairwise disjoint target pairs,
defining the Clifford layers
C2 :=
m∏
z=1
H(bz) CNOT(bz→az), C 1 :=C †
2 =
m∏
z=1
CNOT(bz→az)H(bz),(15)
6

--- Page 7 ---
yields the exact Clifford equivalence
Wm =C1 UCCZ,mC2, U CCZ,m :=
m∏
z=1
CCZ(c,az,bz).(16)
On computational-basis states,UCCZ,m|c,a,b⟩ = (−1)fm(c,a,b)|c,a,b⟩, wherefm : F2m+1
2 →F 2 is
the cubic Boolean function
fm(c,a,b) :=c·
m⨁
z=1
azbz.(17)
4.1 Universal Lower BoundT(W m)≥2m+ 1
A naive attempt to lower-boundWm by applyingWm directly to|+⟩⊗(2m+1) fails becauseWm
is a basis permutation and therefore fixes|+⟩⊗(2m+1). Instead, applyingWm to the stabilizer
stateC †
2|+⟩⊗(2m+1) producesC 1|Φm⟩, where
|Φm⟩:=U CCZ,m|+⟩⊗(2m+1) = 2−(2m+1)/2 ∑
y∈F2m+1
2
(−1)fm(y)|y⟩.(18)
Theorem 9(Wide Fredkin lower bound and Symplectic-Gram4m+ 3decomposition).For
every integerm≥1:
(a) (Universal adaptive lower bound)|Stab (|Φm⟩)|= 1, henceν(|Φm⟩) = 2m+ 1. Con-
sequently,everyadaptive Clifford+ T (or Clifford + single-qubit diagonalRz(θ)) circuit
implementing full-space Wm—even with arbitrary clean ancillas and mid-circuit Pauli
measurements—requires
T(Wm)≥2m+ 1.(19)
In particular, no sublinearo(m)decomposition ofWm exists.
(b) (Minimal F2 symplectic-Gram factorization and4 m+ 3ancilla-free circuit)
Let Hm := ⨁m
z=1
(
0 1
1 0
)
∈F 2m×2m
2 be the standard symplectic alternating matrix. The
minimum number of columnsk of a binary matrixV∈F 2m×k
2 satisfying VV ⊤ = Hm
(mod 2)isexactly kmin(m) = 2m+ 1. The explicit matrixVm ∈F 2m×(2m+1)
2 defined below
yields an exactancilla-free, measurement-freeClifford+Tcircuit implementingW m with
T= 4m+ 3,CNOT = 12m−2,CZ = 2⌈m/2⌉, H= 2m,(20)
and at most one single-qubitS or Z gate. For every m≥ 2, this strictly improves both
independent Fredkins (7m, a1 .75×asymptotic reduction) and the naive shared-c phase
polynomial (6m+ (mmod 2)), while lying within2×of the universal lower bound2m+ 1.
Proof of Theorem 9(a).A Pauli P = ±ix·zXxZz stabilizes |Φm⟩ if and only if the phase
(−1)fm(y⊕x)⊕fm(y)⊕z·y is constant for ally∈F 2m+1
2 , i.e., the discrete derivativeDxfm(y) :=
fm(y⊕x)⊕f m(y)is affine iny= (c,a,b)with linear partz. Writingx= (x c,xa,xb):
Dxfm(c,a,b) =x c
m⨁
z=1
azbz ⊕
m⨁
z=1
(
xb,zcaz ⊕xa,zcbz
)
⊕(terms of degree≤1inc,a,b).(21)
Itsdegree-2partvanishesidenticallyifandonlyif xc = 0and xa,z = xb,z = 0forall z∈{ 1,...,m} .
Equivalently, testing the second-order discrete derivativeDxfm(0) ⊕Dxfm(u) ⊕Dxfm(v) ⊕
Dxfm(u⊕v ) = 0on( u,v) = (ea1 ,eb1 )extracts xc = 0, on( u,v) = (ec,eaz )extracts xb,z = 0,
and on( u,v) = (ec,ebz )extracts xa,z = 0(formalized constructively for all m≥ 1in Lean 4
as wide_fredkin_deriv_affine_implies_zero). With x= 0, D0fm ≡0, soz·y is constant
on F2m+1
2 , forcingz = 0. Thus Stab(|Φm⟩) = {+I}, ν(|Φm⟩) = 2m+ 1, and sinceC1,C2 are
Clifford andν(C†
2|+⟩⊗(2m+1)) = 0, Lemma 2 yieldsT(Wm)≥2m+ 1.
7

--- Page 8 ---
4.2 The Symplectic-Gram Factorization and Exact4m+ 3Circuit
A naive phase-polynomial synthesis [6] of UCCZ,m sums the optimal ancilla-free 7-TCCZ
identity [7] overz= 1,...,m:
4c
m∑
z=1
azbz ≡mc+
m∑
z=1
(
az +bz −(c⊕a z)−(c⊕b z)−(a z ⊕bz) + (c⊕az ⊕bz)
)
(mod 8).(22)
Sharing the linear control termmc saves m− (mmod 2) T-gates, yielding6 m+ (mmod 2)
T-gates. We break well below6mby introducing apaired-togglephase-polynomial representation
driven by a rank-1 Gram factorization ofHm overF 2.
For any binary column vectorv∈F 2m
2 and data vectorx= (a1,b1,...,a m,bm) ∈F 2m
2 , let
yv :=v·xmod 2∈{0,1}. Consider the 2-Tparity-toggle phase
τv(c,x) := (c⊕y v)−y v =c−2cy v ∈Z(23)
(proved constructively in Lean 4 aspair_toggle_int_identity). By the exact mod-8 XOR
expansion (two_xor_mod8_expansion), for any bitsu1,...,u r ∈{0,1},
2
( r⨁
i=1
ui
)
≡2
r∑
i=1
ui −4
∑
1≤i<j≤r
uiuj (mod 8),(24)
because2( a⊕b ) = 2 a+ 2b− 4ab and4( a⊕b ) ≡4(a+ b) ( mod 8). Substituting ui = vixi
into (23) kills all pure-xcubic terms and leaves
τv(c,x)≡c−2c
2m∑
i=1
vixi + 4c
∑
1≤i<j≤2m
vivj xixj (mod 8).(25)
Now sum(25) over thek columns v(0),...,v (k−1) of a binary matrixV∈F 2m×k
2 . Observe that
exp(iπ
4 ·2cxi)is a non-Clifford controlled-S gate, whereasexp(iπ
4 ·4cxi) = (−1)cxi = CZ(c,xi)
is Clifford! Therefore, summing τv(r) (c,x)cancelsallnon-Clifford controlled- S terms while
generating the exactCCZcubic phase4c ∑m
z=1 azbz (mod 8)if and only if:
(i) Every row i of V hasevenHamming weight wi = ∑
rVir ≡0 ( mod 2)(so −2cwixi ≡
4(wi/2 mod 2)cxi (mod 8)is pure CliffordCZ); and
(ii) For every1≤i<j≤2m, ∑
rVirVjr ≡(Hm)ij (mod 2).
Conditions (i) and (ii) combine into the single matrix equation overF2:
VV ⊤=Hm (mod 2).(26)
Proof of Theorem 9(b).Minimality ofk= 2m+ 1:Since rankF2 (Hm) = 2m, subadditivity of
rank forcesk≥ 2m. Suppose k= 2m and VV ⊤= Hm (mod 2). Then rankF2 (V) = 2m, so the
square matrixV∈F 2m×2m
2 is invertible overF2. Yet the diagonal ofHm is zero, so every row
of V has even Hamming weight; henceV1=0( mod 2)( even_rows_all_ones_in_kernel),
contradicting invertibility! Thusk≥2m+ 1.
Explicit closed-form matrixVm ∈F 2m×(2m+1)
2 :Index rows byr= 2z+p(z∈{ 0,...,m−
1}, p∈{ 0,1}, corresponding toaz+1,bz+1) and columns byc∈{ 0,..., 2m}. Set Vm(r,0) := 1,
and forc= 2j+ 1 +q(j∈{0,...,m−1},q∈{0,1}),
Vm(2z+p,2j+ 1 +q) :=



1j <z,
1q=p j=z,
0j >z.
(27)
8

--- Page 9 ---
Inductively, V1 =
(
1 1 0
1 0 1
)
and Vm appends two rows[12m−1 |1,0]and[1 2m−1 |0,1]below
[Vm−1 |02(m−1)×2]. By sympGram_exact (Lean 4), the integer inner product of any two rows
r1,r2 <2mis
(VmV⊤
m)r1,r2 =



2(⌊r1/2⌋+ 1)r 1 =r2 (even row weight2(z+ 1)),
2⌊r1/2⌋+ 1⌊r 1/2⌋=⌊r 2/2⌋, r1 ̸=r2 (≡1 mod 2),
2(min(⌊r1/2⌋,⌊r2/2⌋) + 1)⌊r 1/2⌋̸=⌊r 2/2⌋(≡0 mod 2).
(28)
Thus VmV⊤
m = Hm (mod 2)for every m≥ 1, and the half-row-weight of pairz+ 1(1-indexed)
is z+ 1, which is odd precisely whenz+ 1is odd. Summing (25) over all2m+ 1columns gives
the exact universal mod-8 phase identity:
4c
m∑
z=1
azbz ≡−(2m+ 1)c+
2m∑
r=0
(
(c⊕v (r) ·x)−v (r) ·x
)
+
∑
1≤z≤m
zodd
4c(az +bz) (mod 8).(29)
Explicit O(m)-CNOT, ancilla-free circuit:Inspecting (27), every column parity is
determined by the running suffix XORsz := ⨁m
j=z+1 (aj⊕bj)( sm := 0): specifically,v(2z−1)·x =
az⊕sz, v(2z)·x = bz⊕sz (1 ≤z≤m ), andv(0)·x = a1 ⊕b1 ⊕s1 = s0. Walkingz= m,m−1,..., 1:
1. If z < m, wirebz+1 currently holdssz; apply CNOT(bz+1→az)and CNOT(bz+1→bz)so
(az,bz)hold(a z ⊕sz, bz ⊕sz).
2. On each wirey∈{a z,bz}, apply the 2-Ttoggle gadget
G(c,y) := CNOT(c→y)T(y) CNOT(c→y)T †(y),
which multiplies byexp(iπ
4 ((c⊕y)−y))using2T-gates,2 CNOTs, and0ancillas.
3. If z < m, apply CNOT(bz+1→az)to restore az to its original value, and then apply
CNOT(az→bz)so that wireb z holdsa z ⊕bz ⊕sz =sz−1.
After z = 1, wire b1 holds s0 = v(0) ·x : apply G(c,b1), then reverse the2 m− 1ladder
CNOTs (CNOT(az→bz)and CNOT(bz+1→bz)) to restore all target wires identically. Next
apply T−(2m+1) on c (which costs exactly1 T or T† gate plus at most one CliffordS or Z
gate, since−(2m+ 1) mod 8 ∈{1,3,5,7}) andCZ(c,az),CZ (c,bz)for every odd z∈{ 1,...,m} .
Sandwiching withC2 andC 1 implementsWm identically!
Counting gates:2 m+ 1pair gadgets give4 m+ 2 T-gates plus1 T-gate oncfor T = 4m+ 3.
CNOTs:2 m from C1,C2;2(2 m+ 1) = 4m+ 2inside pair gadgets;3( m− 1) + m = 4m− 3
forward ladder CNOTs; and( m− 1) + m = 2m− 1reverse ladder CNOTs; total CNOT =
2m+ (4m+ 2) + (4m−3) + (2m−1) = 12m−2. FinallyCZ = 2⌈m/2⌉andH= 2m.
Figure 2 plots the normalizedT-cost per pairT/m and visualizes the closed-form matrix
V4 ∈F 8×9
2 (T = 19vs.28). Certificates C08 and C09 verify exact Q(ζ8)unitary equality
Ucirc = Wm (zero error) exhaustively across all22m+1 basis states form = 1,2,3and all512
basis states atm= 4.
5 Theorem C: Subspace-Optimal Unary-Tracker Routing (8Kj
and4K j)
Within Sun’s unary-tracking construction (Section 3.2 of [1]), the tracker wires(Az,0,Az,1)for a
mixing branchz∈Mneversimultaneously occupy|11⟩:
9

--- Page 10 ---
Figure 2: Resolution of Open Question 2. (a) NormalizedT-count per pairT/m for full-space
Wide FredkinWm: independent Fredkins (7m), naive shared-c polynomial (6m+ (mmod 2)),
our ancilla-free measurement-free Symplectic-Gram circuit (4m+ 3,1 .75×asymptotic savings),
Gidney’s1-ancilla measurement-assisted bound (4m), and our universal adaptive lower bound
(2m+ 1). (b) Closed-form Symplectic-Gram matrixV4 ∈F 8×9
2 achieving V4V⊤
4 = H4 (mod 2)
withT= 19vs.28.
• InStep 3(restore), the reachable input states satisfyAz,1 = 0, requiring the map|c,a0,0⟩↦→
+|c,a0(1−c),a 0c⟩with uniform+1phases.
• InStep 1(fold), the reachable input states are{(0,0,0),(0,1,0),(1,0,0),(1,0,1)}, requiring
the exact inverse|c,a0(1−c),a 0c⟩↦→+|c,a0,0⟩.
Sun implements both steps with full Fredkin gates (14Kj T-gates). Exploiting Az,0Az,1 = 0
gives sharp savings withzero extra ancillas:
Theorem 10(Exact unary-subspace routing with zero extra ancillas).In any CSD iteration
withK j mixing branchesM⊆{0,1} n−1:
(a) (Measurement-free, zero extra ancillas:8Kj vs.14 Kj)Let Urtof(c,a0,a1)be the 4-T
relative-phase Toffoli [4]
Urtof :=H(a 1)T†(a1) CNOT(a0→a1)T(a1) CNOT(c→a1)
·T †(a1) CNOT(a0→a1)T(a1)H(a1),(30)
and define the4-Tphase-corrected router and its exact adjoint:
Ustep3 := CNOT(a1→a0)S†(a1)Urtof(c,a0,a1), U step1 :=U †
step3.(31)
Then Ustep3 implements Step 3 with exact+1phases on every reachable state |c,a0,0⟩,
and Ustep1 implements Step 1 with exact+1phases on every reachable state |c,a0(1 −
c),a0c⟩. Total per-factor routing cost drops from14Kj to8 Kj T-gates (1.75×exact, zero
measurements, zero extra ancillas).
(b) (Measurement-assisted, zero extra ancillas:4Kj vs.14 Kj)When mid-circuit Z-
basis measurement and reset of the already-allocated tracker wiresAz,1 are permitted,
Step 1 executes withexactly0 T-gates and0extra ancillas: for every z∈M , apply
CNOT(Az,1→Az,0), apply H(Az,1), measureAz,1 obtaining mz ∈{0,1}, and if mz = 1
apply X(Az,1)(reset to |0⟩) and the Clifford correctionCZ(c,Az,0). Combining this0- T
Step 1 with the4Kj-T Step 3 from(31) cuts total per-factor routing from14Kj to4 Kj
T-gates (3.50×exact, zero extra ancillas), within4×of Theorem 6.
10

--- Page 11 ---
Proof. For (a), direct evaluation overQ(ζ8)(Certificate C11, Table 2) shows thatUrtof acts as
identity on|000⟩,|010⟩,|100⟩and maps |110⟩↦→+i|111⟩. Applying S†(a1)cancels+ i to+1
without altering any state witha1 = 0; applyingCNOT(a1→a0)then maps |111⟩↦→|101⟩while
fixing |000⟩,|010⟩,|100⟩. Since Ustep1 = U†
step3 is the exact unitary inverse, it reverses Step 1
with all+1phases.
For (b), consider an arbitrary coherent superposition
|Ψ⟩=
∑
z∈M
(
αz,0|z,0⟩|ez,0⟩+α z,1|z,1⟩|ez,1⟩
)
+|Ψ /∈M⟩,
where |Ψ/∈M⟩has allAz,0 = Az,1 = 0for z∈M . Applying CNOT(Az,1→Az,0)for all z∈M
transforms each mixing term toαz,0|z,0⟩|ez,0⟩+ αz,1|z,1⟩|ez,0 + ez,1⟩(so Az,1 = c∧A z,0 holds
identically on the entire superposition). Applying⨂
z∈M H(Az,1)produces
|Ψ′⟩= 2 −Kj/2 ∑
m∈{0,1}M
|m⟩AM,1
⊗
[∑
z∈M
(
αz,0|z,0⟩+ (−1) mz αz,1|z,1⟩
)
|ez,0⟩A\M,1 +|Ψ /∈M⟩
]
.(32)
Upon measuring outcome m∈ {0,1}M (each with probability2 −Kj ), resetting wires with
mz = 1via X(Az,1)restores AM,1 = |0⟩Kj , and applyingCZ(c,Az,0)whenever mz = 1multiplies
the |z,1⟩|ez,0⟩amplitude by( −1)mz while acting trivially on|z,0⟩|ez,0⟩, on every|z′,c′⟩|ez′,0⟩
(z′̸= z), and on|Ψ/∈M⟩(all of which haveAz,0 = 0). Hence every single measurement branch
yields the exact target state∑
z∈M(αz,0|z,0⟩+ αz,1|z,1⟩)|ez,0⟩+ |Ψ/∈M⟩with0 T-gates and0
extra ancillas (verified identically overQ(ζ8)across all2 3 = 8measurement outcomes for an
arbitrary6-branch superposition in CertificateC12).
Remark11 (Exact complementarity with Theorem 6).Theorem 10(b) provides a striking
operational confirmation of the directionality of stabilizer nullity (Lemma 2): Step 1 maps
|ψout⟩ ↦→ |ϕin⟩, which has∆ ν = −Kj ≤ 0for Kj ≥ 3(and −3at Kj = 2), and indeed
admits a0-T adaptive-measurement implementation; Step 3 maps|ψpre⟩↦→|ψout⟩, which has
∆ν = +Kj >0for Kj ≥3(+3at Kj = 2), and provably requires≥∆ν(Kj) T-gates even with
arbitrary adaptive measurements.
6 Theorem D: Exact Space-Depth Volume, Monotonicity, and
Sawtooth Elimination
In Section 4 of [1] (Theorem 1.2), ann-qubit unitary (N = 2n) is implemented using an ancilla
budget n≤a≤N by settingk= ⌊log2 a⌋, B = 2k ≤a, runningn−k levels of QSD to produce
4n−k = (N/B)2 uncontrolledk-qubit blocks, implementing each block in unary form on the reused
B-qubit register in depthDblk(B) = αB+ β (α> 0,β≥ 0), and executing the three multiplexed
rotations at eachj-qubit QSD node (k+1 ≤j≤n ) in depthγ·2j on the binary data register. In
elementary 1Q+CNOT layers, each Shende–Bullock–Markov multiplexor [5] onj−1controls uses
2j−1 alternating 1Q andCNOT layers (depth2j), givingγ = 3; within ak-qubit unary block, the
B−1parallel CSD layers each implementCNOT·(ctrl-U(2))·CNOT (KAK/Barenco depth≤7),
giving a baselineα= 7for the CSD core (with unary encoding/decoding from Section 4.1 of [1]
adding an implementation-dependent positive shift toα, which leaves Theorem 12 unchanged
since it holds for allα>0).
Theorem 12(Exact closed-form QSD depth, strict monotonicity, and sawtooth elimination).
For alln≥2,1≤k≤n,N= 2 n,B= 2 k, and constantsα>0,β≥0,γ≥1:
11

--- Page 12 ---
(a) (Exact closed-form depth)The QSD multiplexor depth satisfies the exact geometric
identity ∑n
j=k+1 4n−j2j = N2/B−N (Lean 4: qsdMuxSum_exact), yielding exact total
depth
D(n,B) =
(N
B
)2
(αB+β) +γ
(
N2
B −N
)
= (α+γ) N2
B +β N2
B2 −γN.(33)
(b) (Strict volume monotonicity)LetVused(n,B) := (n+ B)D(n,B)denote the space-depth
volume charging only then+Bactually allocated qubits. For every1≤B≤N/2,
Vused(n,B)−V used(n,2B) =
(
n(α+γ) +β
)N2
2B + 3nβN2
4B2 +γNB >0(34)
(Lean 4:volume_strictly_monotone_scaled). Hence B∗= 2⌊log2 a⌋ is uniquely volume-
optimal among all power-of-two block sizesB≤a.
(c) (Sawtooth elimination andB = N discontinuity)Charging the full ancilla budgeta
while allocating onlyB∗= 2⌊log2 a⌋ wires incurs the exact sawtooth inflation ratio
Vbudget(n,a)
Vused(n,B∗) = n+a
n+B ∗
k→∞−−−−−−→
a=2k+1−1
2,(35)
which is completely eliminated by allocating onlyB∗ ancillas. Furthermore, Vused(n,B)/N2
exhibits a sharp leading-order gap between intermediate sub-N QSD-hybrid synthesis (B =
ω(n)and B = o(N) = ⇒V used/N2 →α + γ; B = N/2 = ⇒α + γ/2) and full-unary
synthesis (B=N=⇒V used/N2 →α).
Proof. For (a),∑n
j=k+1 4n−j2j = 4n∑n
j=k+1 2−j = 4n(2−k −2−n) = N2/B−N ; substituting
into( N/B)2(αB+ β) +γ(N2/B−N )gives (33). For (b), clearing denominators by4B2 reduces
4B2(Vused(n,B)−Vused(n,2B))to the polynomial identity(n+B)(4C+4D−E)−(n+2B)(2C+
D−E ) = 2 nC + 2BD + 3nD+ BE with C = (α+ γ)N2B, D = βN2, E = 4γNB2, every
term of which is nonnegative andBE = 4γNB3 > 0. Dividing by4 B2 gives (34). Part (c)
follows directly from(33): at a = 2k+1 −1,( n+ 2B∗−1)/(n+ B∗) = 2 −(n+ 1)/(n+ B∗);
and Vused(n,B)/N2 = (α+ γ)(1 + n/B) + β(1 + n/B)/B−γ (n+ B)/N, giving limitsα+ γ
(B=o(N),B≫n),α+γ/2(B=N/2), andα(B=N).
Figure 3 illustrates the1.98×sawtooth peak atn= 10,a = 1023(1033 /522, CertificateC15)
and the exact leading-order jump fromα+γ/2 = 8.5(B=N/2) toα= 7.0(B=N).
7 Formal Verification and Reproducibility
• Lean 4.35.0 formalization:lean/UnaryTrackerBounds.lean builds vialake build in
1.7s with0errors,0warnings,0 sorry,0custom axioms, and0 Classical.choice across all
15audited theorems: exists_two_disjoint_orbits, constant_shift_four_term_zero,
deltaNu_eq_K_of_ge_three , deltaNu_ge_K_of_ge_two , wide_fredkin_deriv_a
ffine_implies_zero , sympGram_exact , sympGram_mod2_eq_H , sympV_row_weight ,
even_rows_all_ones_in_kernel , pair_toggle_int_identity , two_xor_mod8_e
xpansion , gram_beats_fred_sun , gram_beats_shared_c , qsdMuxSum_exact , and
volume_strictly_monotone_scaled.
• Zero-float exactQ(ζ8)verifier: verification/verify_paper99.py enforces an AST
zero-float hygiene gate (banning float/complex literals,/, **, pow, float, complex, eval,
exec, and numeric float libraries) and emits16SHA-256 certificates ( C01–C16) under
protocolUNARY-TRACKER-BOUNDS-1.0.
12

--- Page 13 ---
Figure 3: Exact QSD + unary-block space-depth volume (Theorem 12, benchmark(α,β,γ ) =
(7,0,3)). (a) Atn= 10, budget-charged volumeVbudget(a)/N2 exhibits a1033/522 ≈1.98×saw-
tooth peak ata= 1023,B∗= 512, completely eliminated by allocated-only volumeVused(B∗)/N2.
(b) Strict monotonicity and exact discontinuity fromB = N/2( α+ γ/2 = 8.5) to full-unary
B=N(α= 7.0).
• Adversarial test suite:tests/test_verify_paper99.py executes67 /67passing tests,
including30mutation/forgery tests (omitting S† in Step 3, omitting conditionalCZ in
Step 1, flippingT↔T † or dropping aCZ/T/H gate in Wm, dropping a column ofV2,
violating affine independence with binary encoding, and testing AST-audit rejections).
AI Assistance Disclosure.In accordance with transparent scientific disclosure practices,
Google Antigravity assisted with Lean 4 proof engineering, exactQ(ζ8)verification scripting,
figure generation, and LaTeX typesetting. All mathematical definitions, theorems, proofs,
formalization checks, and final manuscript claims were reviewed and validated by the sole author,
Lluis Eriksson.
A Self-Contained Verification Tables, Explicit Circuits, and
Certificate Ledger
To ensure that every theorem in this manuscript can be audited without executing external code,
we tabulate the explicit matricesV1,V2,V3, the complete gate-by-gate circuits forUstep3 and W2,
the exactT-count comparison across scales, and the full SHA-256 certificate ledger.
A.1 Explicit Symplectic-Gram MatricesV 1, V2, V3
From (27), the first three minimal Gram factors (k= 2m+ 1columns) are:
V1 =
(
1 1 0
1 0 1
)
, V 2 =


1 1 0 0 0
1 0 1 0 0
1 1 1 1 0
1 1 1 0 1

, V 3 =


1 1 0 0 0 0 0
1 0 1 0 0 0 0
1 1 1 1 0 0 0
1 1 1 0 1 0 0
1 1 1 1 1 1 0
1 1 1 1 1 0 1


.
Direct multiplication verifiesV1V⊤
1 = ( 2 1
1 2)≡H 1, V2V⊤
2 =
(2 1 2 2
1 2 2 2
2 2 4 3
2 2 3 4
)
≡H 2, andV3V⊤
3 ≡H 3
(mod 2), with even row weights2,2,4,4,6,6.
13

--- Page 14 ---
A.2 Complete Explicit Gate Sequences forU step3 andW 2
Table 2: Exact action ofUrtof and Ustep3 = CNOT(a1→a0) S†(a1) Urtof(c,a0,a1)(4 T-gates,0
ancillas) on all4reachable unary-subspace inputs|c,a 0,0⟩(CertificateC11).
Input|c,a 0,a1⟩AfterU rtof AfterS †(a1)AfterCNOT(a 1→a0)Expected Step 3
|0,0,0⟩+|0,0,0⟩+|0,0,0⟩+|0,0,0⟩+|0,0,0⟩
|0,1,0⟩+|0,1,0⟩+|0,1,0⟩+|0,1,0⟩+|0,1,0⟩
|1,0,0⟩+|1,0,0⟩+|1,0,0⟩+|1,0,0⟩+|1,0,0⟩
|1,1,0⟩+i|1,1,1⟩+|1,1,1⟩+|1,0,1⟩+|1,0,1⟩
Explicit11- T,22- CNOT ancilla-free circuit forW2 (qubits0 =c,1=a1,2=b1,3=a2,4=b2):
Let G(c,y) := CNOT(c→y) T(y) CNOT(c→y) T†(y)(applied right-to-left in algebraic notation,
i.e.,T †first in time order). Reading gates strictly intime order(left to right):
1.Pre-CliffordC 2:CNOT(2→1), H(2),CNOT(4→3), H(4). (2 CNOT,2H)
2. Pair z= 2( v(3),v(4)): G(0,3), G(0,4),CNOT (3→4). (Wire4holds s1 = a2 ⊕b2;4 T,5
CNOT)
3. Pair z = 1( v(1),v(2)): CNOT(4→1), CNOT(4→2), G(0,1), G(0,2), CNOT(4→1), and
CNOT(1→2), leavings0 =a1 ⊕b1 ⊕a2 ⊕b2 on wire2(4T,8 CNOT).
4. Column v(0) & uncompute ladder:G(0,2),CNOT (1→2),CNOT (4→2),CNOT (3→4).
(2T,5 CNOT)
5. Control phase (−5 ≡3 mod 8) & odd-pairCZs: T(0), S(0),CZ (0,1),CZ (0,2). (1 T,1
S,2 CZ)
6.Post-CliffordC 1:H(2),CNOT(2→1), H(4),CNOT(4→3). (2 CNOT,2H)
Total: T = 4 + 4 + 2 + 1 = 11(vs.14independent), CNOT = 2 + 5 + 8 + 5 + 2 = 22,CZ = 2,
H = 4, S = 1, ancillas= 0. Certificate C08 verifies exact identity on all32basis states over
Q(ζ8).
A.3 Unified Numerical Scaling Table and SHA-256 Certificate Ledger
Table 3: ExactT-count comparison acrossm,Kj ∈{1,2,3,4,16,64,256,1024}(Certificate C16).
Open Q1: Tracker Update (Kj) Open Q2: Wide Fredkin (Wm)
Kj,m Thm. 6 LB4K j (meas.)8K j (MF) Sun14K j Thm. 9 LB Gram4m+3Shared-cSun7m
1 0 4 8 14 3 7 7 7
2 3 8 16 28 5 11 12 14
3 3 12 24 42 7 15 19 21
4 4 16 32 56 9 19 24 28
16 16 64 128 224 33 67 96 112
64 64 256 512 896 129 259 384 448
256 256 1024 2048 3584 513 1027 1536 1792
1024 1024 4096 8192 14336 2049 4099 6144 7168
References
[1] F. Sun,Unitary Synthesis with a Unary Tracker, arXiv:2611.34740v1 [quant-ph], November
2026.
14

--- Page 15 ---
Table 4: Verified SHA-256 certificate ledger under protocolUNARY-TRACKER-BOUNDS-1.0 (mani-
fest hashc1e3e176a7ec...68d).
ID Verified Claim SHA-256 Prefix
C01Exact cyclotomic ringQ(ζ 8)unit and Hadamard identities973a1756670f49ab
C02Thm. 6 exhaustive nullity forn= 3(all15nonempty subsets)f5d74364f9c26875
C03Thm. 6 exhaustive nullity forn= 4(all255nonempty subsets,K= 1..8)87a1c03eb40190ba
C04Thm. 6 invariance across compressed, dense, affine-shiftedF 2 codes232efba4bdcf17ea
C05Thm. 9(a) exact full-spaceW m nullityν= 2m+ 1(m= 1..4)0b17b4c5314f82fe
C06Thm. 9(b) exact symplectic Gram identityV mV⊤
m =Hm (mod 2)(m= 1..16)ca03dbafe6e808f3
C07Thm. 9(b) exhaustive exact mod-8 phase-polynomial identity (m= 1..4)bf402ef5b88c986c
C08Thm. 9(b) exactQ(ζ 8)full unitary verification of(4m+3)-T Wm (m= 1..3)d57926addbbbaf7c
C09Thm. 9(b) exhaustiveQ(ζ 8)verification of all512states of19-T W 4 3026ad92bdfdb727
C10Thm. 9(b) minimalityk min = 2m+ 1(V1=0kernel obstruction)e28c388d1dde1c2c
C11Thm. 10(a) exactQ(ζ 8)all-+1phase check of4-TStep 3 & Step 105b34ae5c548adeb
C12Thm. 10(b) exactQ(ζ 8) 0-Tmeas.-assisted Step 1 (K= 3, all8outcomes)6f845d7b4de841ed
C13Thm. 12(a) exact QSD geometric sum & closed-form depth (n= 2..14)942d701317333b2f
C14Thm. 12(b) strict volume monotonicityV used(n,B)−V used(n,2B)>0409caa26794cc746
C15Thm. 12(c) exact sawtooth penalty (1033/522atn= 10) &B=N/2vs.Ngapca9aeb2cf8c12b3e
C16Unified exactT-count hierarchy across Open Questions 1 and 2 (m,K= 1..1024)c5fce82216bb724c
[2] M. Beverland, E. Campbell, M. Howard, and V. Kliuchnikov,Lower bounds on the non-
Clifford resources for quantum computations, Quantum Science and Technology5(3), 035009,
2020.
[3] C. Gidney,Halving the cost of quantum addition, Quantum2, 74, 2018.
[4] D. Maslov,Advantages of using relative-phase Toffoli gates with an application to multiple
control Toffoli optimization, Physical Review A93(2), 022311, 2016.
[5] V. V. Shende, S. S. Bullock, and I. L. Markov,Synthesis of quantum-logic circuits, IEEE
Transactions on Computer-Aided Design of Integrated Circuits and Systems25(6), 1000–1010,
2006.
[6] M. Amy and M. Mosca,T-count optimization and Reed–Muller codes, IEEE Transactions on
Information Theory65(8), 4771–4784, 2019.
[7] D. Gosset, V. Kliuchnikov, M. Mosca, and V. Russo,An algorithm for the T-count, Quantum
Information and Computation14(15–16), 1261–1276, 2014.
15
