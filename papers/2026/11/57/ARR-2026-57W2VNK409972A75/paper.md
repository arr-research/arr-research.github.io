# Exact Walled Brauer Spectral Collapse, the d_min = 8 Impossibility Barrier, Closed-Form All-d >= 8 NPT Bound-Entangled Werner Families, and Equivariant Branch Uniqueness

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-57W2VNK409972A75` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper142-npt-bound-entanglement-barriers (`v1.0.1`)  
**Canonical PDF SHA-256:** `e2b15ee8a1531c0859a5d8b56f6ebc4f99fb10117cee1fe57c554135f384e872`

## Abstract

Faisal (2026, arXiv:2611.34921v1) proved that negative partial transpose (NPT) bound entanglement exists by exhibiting a single Werner state rho = (23 I - 3 SWAP)/1448 (alpha = -3/23 < -1/8) on C^8 x C^8 and a 4096 x 4096 Hermitian witness Q satisfying four operator inequalities (2a)-(2d) checked via U(1)^8 diagonal blocks of sizes up to 42. We resolve the five main structural, dimensional, infinite-family, high-dimension depth, and uniqueness questions left open by Faisal via four exact, machine-checked theorems backed by 20 constructive Lean 4.36.0 theorems (zero external imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-float exact-rational SHA-256 certificates, and 56 adversarial tests: (1) Exact Walled Brauer B_{3,1}(d) Spectral Collapse & Twirling Completeness: Haar averaging over U* x U x U* x U* preserves (2a)-(2d) and collapses the d^4 x d^4 problem without loss of generality into the 17-dimensional Hermitian walled Brauer algebra B_{3,1}(d), reducing (2a)-(2c) to five d-independent U(d)-isotypic blocks of sizes (1, 1, 2, 3, 3) (four for d = 3) and (2d) to 6 linear equations identically forcing row/col 0 of both 3x3 blocks of J - Q to vanish; (2) Exact Dimensional Phase Transition (d_min = 8 Impossibility Barrier) & d = 8 Sharpening: 33 exact rational strictly positive-definite SDP dual certificates tiling a_M in [0, 1] across d in {3, 4, 5, 6, 7} (16 subintervals for d = 7) together with an algebraic a_M >= 1 tail proof establish that no (L, M, Q) satisfying (2a)-(2d) can certify an NPT Werner state for any d <= 7 (proving d_min = 8 sharply), while an explicit rational witness at d = 8 sharpens Faisal's state to rho_8* = (151 I - 20 SWAP)/9504 (alpha = -20/151 < -3/23); (3) Closed-Form Infinite Family for ALL d >= 8 & High-Dimension Separation up to d = 400: constructive polynomial reflection in s = d - 8 >= 0 inside Lean 4 proves all 28 Sylvester minors across J+Q, J-Q, and Q^{Gamma_in} are strictly positive for every integer d >= 8, certifying the closed-form infinite NPT bound-entangled Werner family rho_d = ((5d+7)I - 6 SWAP)/(d(5d^2+7d-6)) (alpha(d) = -6/(5d+7) < -1/d), while five exact rational primal witnesses at d in {16, 36, 64, 100, 400} constructively certify c_I(d) < sqrt(7d) (reaching c_I(400) ~ 51.53, 7.76x deeper than -1/d at d = 400), corroborating a numerical SDP fit c_I*(d) ~ 2.31 sqrt(d); and (4) 4-Branch U(d)-Equivariant Uniqueness Barrier & Exact White-Noise Thresholds: we prove (X^T, X) with b_L < 0, b_M > 0 is the unique U(d)-equivariant CP branch capable of certifying NPT bound entanglement and establish exact white-noise depolarizing robustness p_max(d, alpha) = d(1 + d*alpha)/(alpha*(d^2 - 1)), raising d = 8 tolerance by an exact +35% from 8/189 (~4.23%) to 2/35 (~5.71%), and growing to p_max = d(d-7)/(6(d^2-1)) -> 1/6 for our closed-form family (>87% at d = 400).

## Full Extracted Text

--- Page 1 ---
Exact Walled Brauer Spectral Collapse, the dmin = 8
Impossibility Barrier, Closed-Form All- d ≥ 8 NPT
Bound-Entangled Werner Families, and Equivariant
Branch Uniqueness
Lluis Eriksson
Independent Researcher ( ORCID: 0009-0006-7494-9040 )
November 27, 2026
Abstract
Faisal [ 6] recently proved that negative partial transpose (NPT) bound entanglement
exists by exhibiting a single Werner state ρ = 23I−3 SWAP
1448 (α = −3/23 < −1/8) on C8 ⊗
C8 and a 4096 × 4096 Hermitian witness Q = 1
40
∑
π∈S4
mπBπ satisfying four operator
inequalities (2a)–(2d) checked via U(1)8 diagonal phase blocks of sizes up to 42. That
breakthrough left open why local dimension d = 8 is required, whether smaller dimensions
d ≤ 7 admit analogous witnesses, whether NPT bound-entangled Werner states exist for all
d ≥ 8, how deeply α can penetrate past the PPT boundary −1/d, and whether any other
U(d)-equivariant local-map branch can succeed. We resolve all ﬁve questions via four exact,
machine-checked theorems backed by 20 constructive Lean 4.36.0 theorems (zero external
imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-ﬂoat
exact-rational SHA-256 certiﬁcates, and 56 adversarial tests:
1. Exact Walled Brauer B3,1(d) Spectral Collapse & Twirling Completeness: We
prove that Haar averaging over ¯U ⊗ U ⊗ ¯U ⊗ ¯U preserves (2a)–(2d) and collapses the
d4 × d4 operator problem without loss of generality into the 17-dimensional Hermitian
walled Brauer algebra B3,1(d), reducing (2a)–(2c) to ﬁve d-independent U(d)-isotypic
blocks of sizes (1, 1, 2, 3, 3) (four blocks for d = 3 ) and (2d) to exactly 6 linear equations
whose satisfaction identically forces row/column 0 of both 3× 3 blocks of J − Q to vanish.
2. Exact Dimensional Phase Transition ( dmin = 8 Impossibility Barrier) &
d = 8 Sharpening: Partitioning aM ∈ [0, 1] into 33 rational subintervals across
d ∈ {3, 4, 5, 6, 7} (16 for d = 7 ) with exact rational strictly positive-deﬁnite SDP dual
certiﬁcates—together with an algebraic proof that aM ≥ 1 always forces cI ≥ d—we
prove that no (L, M, Q) satisfying (2a)–(2d) can certify an NPT Werner state for any
d ≤ 7 (establishing dmin = 8 sharply). At d = 8 , an explicit rational witness certiﬁes
ρ∗
8 = 151I−20 SWAP
9504 (α = −20/151 ≈ − 0.13245 < −3/23), strictly deepening Faisal’s
threshold by 7/3473.
3. Closed-Form Inﬁnite Family for ALL d ≥ 8 & High-Dimension Separation
up to d = 400 : Fixing (aL, aM ) = (5 /3, 1/2) and qk(d) = ak/d + bk/d2 (+c0/d2 for
q0), we prove via constructive polynomial reﬂection in s = d − 8 ≥ 0 inside Lean 4
that all 28 Sylvester leading principal minors across J + Q, J − Q, and QΓin are strictly
positive for every integer d ≥ 8, certifying the explicit inﬁnite NPT bound-entangled
Werner family ρd = (5d+7)I−6 SWAP
d(5d2+7d−6) (α(d) = − 6
5d+7 < − 1
d ). Furthermore, ﬁve exact
rational primal witnesses at d ∈ {16, 36, 64, 100, 400}constructively certify cI(d) <
√
7 d
(reaching cI(400) = 12881729
250000 ≈ 51.53, penetrating 7.76× deeper than −1/d at d = 400 ),
corroborating a numerical SDP ﬁt c∗
I(d) ∼ 2.31
√
d.
4. 4-Branch U(d)-Equivariant Uniqueness Barrier & Exact White-Noise Thresh-
olds: We prove that (XT , X) with bL < 0, bM > 0 is the unique U(d)-equivariant CP
map branch capable of certifying NPT bound entanglement (both isotropic branches are
1-copy distillable whenever NPT, while opposite-sign (XT , X) always yields cI + dcS ≥
1
AIRR:ARR-2026-57W2VNK409972A75 v1  [Quantum information]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
bL(d2 − 1)|bM | > 0, strictly PPT). Every Werner state on [αcert(d), −1/d) is NPT
bound entangled, and under white-noise depolarization Dp, the exact robustness ceil-
ing pmax(d, α) = d(1+dα)
α(d2−1) rises by an exact +35% at d = 8 from Faisal’s 8/189 ≈ 4.23%
to 2/35 ≈ 5.71% (and grows to pmax = d(d−7)
6(d2−1) → 1
6 for our closed-form family, exceeding
87% at d = 400 ).
AI Assistance Disclosure. This manuscript, its constructive Lean 4.36.0 formalization, and
its AST-audited exact-rational veriﬁcation suite were developed by Lluis Eriksson with inter-
active assistance from Google Antigravity for symbolic derivation, SDP dual synthesis, formal
proof veriﬁcation, and typesetting. Every mathematical claim, Lean theorem, and zero-ﬂoat
rational certiﬁcate was mechanically veriﬁed; the author takes full responsibility for all results.
1 Introduction and Preliminaries
Whether bound entangled quantum states with negative partial transpose (NPT) exist—
resolving whether the Peres–Horodecki positive partial transpose (PPT) criterion [ 16, 10] coin-
cides with undistillability under two-way LOCC [ 2]—stood for nearly three decades as one of
the central open problems in quantum information theory [ 3, 4, 15, 11]. Following major recent
advances on k-copy undistillability of Werner states [ 23, 8, 18, 7, 1, 12, 20, 19] and a secret-key
bound-entanglement framework in dimension 10 [14], Islam Faisal [ 6] proved ED(ρ) = 0 for the
NPT Werner state ρ = 23I−3 SWAP
1448 on C8 ⊗ C8 (with Bell-ﬁdelity ceiling 1+
√
2
4 under arbitrary
separable operations, implying nonadditivity and nonconvexity of ED [17, 5, 21]).
Faisal’s proof [ 6] factors ρ⊗n ∝ C ⊗n(|un⟩⟨un|) through a product C = L ⊗ M of two U(d)-
equivariant completely positive (CP) maps on d × d matrices,
L(X) = aLTr(X)I + bLXT , M (X) = aM Tr(X)I + bM X, (1)
and exhibits a single-copy Hermitian Choi matrix Q on (Cd)⊗4 (ordered as Alice input 0, Bob
input 1, Alice output 2, Bob output 3) satisfying four conditions relative to J := JL⊗M [22]:
(2a) J + Q ⪰ 0, (2b) J − Q ⪰ 0, (2c) QΓin ⪰ 0, (2d) (J − Q)(|u⟩ ⊗I) = 0 , (2)
where |u⟩ = ∑d
i=1 |i, i⟩ and Γin denotes partial transposition on input systems (0, 1). Be-
cause (2a)–(2d) yield all-copy block positivity of Ωv,w without requiring C itself to be com-
pletely copositive [ 13], any feasible (L, M, Q) whose output C(|u⟩⟨u|) ∝ cII + cSSWAP sat-
isﬁes cI + dcS < 0 (i.e., Werner parameter α := cS/cI < −1/d) immediately certiﬁes that
ρ(d, α) := I+α SWAP
d2+dα is NPT bound entangled with ED(ρ(d, α)) = 0 and Bell ﬁdelity ≤ 1+
√
2
4 [6,
Lemmas 4–6].
Scaling L and M by positive constants ﬁxes bL = −1, bM = +1 (for the unique productive
sign branch established in Section 5), where complete positivity of L (JL = aLI − SWAP ⪰ 0)
and M (JM = aM I + |u⟩⟨u| ⪰0) holds if and only if aL ≥ 1 and aM ≥ 0. In this normalization,
C(|u⟩⟨u|) = cII − SWAP, c I = d aLaM + aL − aM , α = − 1
cI
, (3)
so ρ(d, α) is NPT if and only if cI < d (with Faisal’s d = 8 choice aL = 5 /3, aM = 18 /37 giving
cI = 23 /3 < 8, α = −3/23). Table 1 summarizes how our four theorems resolve the structural,
dimensional, inﬁnite-family, and uniqueness questions left open by [ 6].
2 Exact Walled Brauer B3,1(d) Spectral Collapse and Twirling
Completeness
For every permutation π ∈ S4 (ordered lexicographically as π0 = (0 , 1, 2, 3), . . . , π23 =
(3, 2, 1, 0)), let Uπ be the permutation unitary on (Cd)⊗4 and Bπ := ( Uπ)Γ1 its partial transpose
2

--- Page 3 ---
Table 1: Summary of results extending Faisal [ 6].
Question Faisal [6] This Paper
Symmetry Abelian U(1)8 phase blocks
of sizes (1, 3, 6, 22, 42) at
d = 8
Full U(d) twirling into 17-dim walled
Brauer B3,1(d): ﬁve d-independent blocks
(1, 1, 2, 3, 3) and 6 linear (2d) equations
(Thm. 2.1)
Minimal
dimension dmin
Single witness at d = 8
(α = −3/23); d ≤ 7
unaddressed
Exact rational dual certiﬁcates prove
cI > d for ALL d ∈ {3, 4, 5, 6, 7},
establishing dmin = 8 sharply; sharpened
ρ∗
8 reaches α = −20/151 (Thm. 3.1)
All d ≥ 8 & high- d
depth
Only d = 8 certiﬁed Closed-form rational family certiﬁes
ρd = (5d+7)I−6 SWAP
d(5d2+7d−6) for all d ≥ 8 (proved
in Lean 4 for all s = d − 8 ∈ N); exact
rational witnesses at
d ∈ {16, 36, 64, 100, 400}certify
cI(d) <
√
7d (Thm. 4.1)
Uniqueness &
robustness
Single sign branch (XT , X);
no noise threshold stated
Proves (XT , X) (bL < 0, bM > 0) is the
unique U(d)-equivariant branch; exact
white-noise threshold pmax = d(1+dα)
α(d2−1) rises
+35% at d = 8 (8/189 → 2/35) (Thm. 5.1)
on the second tensor factor (system 1, Bob’s input), so that B†
π = Bπ−1 and Bπ commutes with
¯U ⊗ U ⊗ ¯U ⊗ ¯U for all U ∈ U(d) [6, Appendix A]. Pairing each permutation with its inverse
yields 10 involutions (π = π−1) and 7 inverse pairs ( {π, π−1}), forming a 17-element Hermitian
basis {B0, . . . , B16}of the Hermitian subspace of the walled Brauer algebra B3,1(d):
Q =
16∑
k=0
qkBk, J = ( aLaM )B0 + aLB4 − aM B11 − B13, (4)
where B0 = I02 ⊗ I13, B4 = I02 ⊗ |u⟩⟨u|13, B11 = SWAP02 ⊗ I13, and B13 = SWAP02 ⊗ |u⟩⟨u|13
(the complete 17-element permutation-pair index table is given explicitly in Appendix A).
Theorem 2.1 (Walled Brauer Spectral Collapse, Twirling Completeness, and (2d) Nullspace) .
For every integer d ≥ 3 and L(X) = aLTr(X)I − XT , M(X) = aM Tr(X)I + X:
1. Haar-Twirling Completeness: If any Hermitian operator Q on (Cd)⊗4 satisﬁes (2), then
its Haar twirl
Q :=
∫
U(d)
( ¯U ⊗ U ⊗ ¯U ⊗ ¯U) Q ( ¯U ⊗ U ⊗ ¯U ⊗ ¯U)†dU
lies in spanR{B0, . . . , B16} ⊂ B3,1(d) and satisﬁes all four conditions (2).
2. Exact d-Independent (1, 1, 2, 3, 3) Block Decomposition (Lean thm01, Cert. C01): An
operator M(x) = ∑16
k=0 xkBk is positive semideﬁnite on (Cd)⊗4 if and only if ﬁve symmetric
polynomial-in-d blocks B0(x) ∈ R1×1, B1(x) ∈ R1×1 (omitted at d = 3 , where the anti-
symmetric 3-box irrep ∧3 C3 ⊗ C3 has no (1, 1, 1; 1) summand of B3,1(3)), B2(x) ∈ R2×2,
B3(d, x) ∈ R3×3, and B4(d, x) ∈ R3×3 are positive semideﬁnite. Moreover, swapping input
systems 0 ↔ 1 maps QΓin unitarily to ∑16
k=0 qγ(k)Bk, where γ is the 5-transposition involution
(2 11)(3 12)(4 15)(8 9)(13 16) .
3. 6-Equation Collapse of (2d) and Identical Nullspace in B3, B4 (Lean thm02–thm05,
Certs. C02–C04): Condition (2d) holds if and only if (j0 = aLaM , aL, aM , q0, . . . , q16) satisﬁes
3

--- Page 4 ---
the six linear equations
dq5 + q0 + q7 + q10 − j0 = 0 , dq6 + q1 + q8 + q9 = 0 , dq 7 + q2 + q11 + q14 + aM = 0 ,
dq8 + q3 + q12 + q16 = 0 , dq 9 + q3 + q12 + q13 + 1 = 0 , dq 10 + q4 + q14 + q15 − aL = 0 .
(5)
Whenever (5) holds, row 0 and column 0 of both B3(d, J − Q) and B4(d, J − Q) vanish
identically for every d, leaving 2 × 2 lower-right blocks.
Proof. (1) Let VU := ¯U ⊗U ⊗ ¯U ⊗ ¯U. Since J commutes with VU for every U ∈ U(d), conjugation
by VU preserves the PSD cones J + Q ⪰ 0 and J − Q ⪰ 0. On the partial-transposed operator
QΓin , the input action ¯U ⊗ U transposes to U ⊗ ¯U, so (VU QV †
U )Γin = ( U ⊗ ¯U ⊗ ¯U ⊗ ¯U)QΓin (U ⊗
¯U ⊗ ¯U ⊗ ¯U)†⪰ 0; averaging over the compact group U(d) preserves convexity of all three PSD
cones (2a)–(2c). For (2d), since ( ¯U ⊗ U)|u⟩= |u⟩for all U ∈ U(d), we have VU (|u⟩ ⊗I) =
(|u⟩ ⊗ I)( ¯U ⊗ ¯U), so (J − VU QV †
U )(|u⟩ ⊗ I) = VU (J − Q)(|u⟩ ⊗ I)( ¯U ⊗ ¯U)† = 0 , and Haar
integration preserves (2d). By mixed Schur–Weyl duality for ¯U ⊗ U ⊗ ¯U ⊗ ¯U, the commutant
of {VU : U ∈ U(d)} is precisely the walled Brauer algebra B3,1(d) = span C{Bπ : π ∈ S4};
Hermiticity forces ˜qπ = ˜qπ−1 , placing Q in spanR{B0, . . . , B16}.
(2) By mixed Schur–Weyl duality for the action of ¯U ⊗ U ⊗ ¯U ⊗ ¯U on (Cd)⊗4 (equivalently
U⊗3 ⊗ ¯U up to global conjugation), the commutant B3,1(d) decomposes into ﬁve simple matrix
blocks for all d ≥ 4 labeled by the walled-Brauer bipartitions ([1]; [3]), ([1]; [1, 1, 1]), ([1]; [2, 1])
(the three uncontracted sectors of multiplicities 1, 1, 2) and the two single-contraction sectors
(∅; [2]) and (∅; [1, 1]) (multiplicities 3, 3). Since the real symmetric matrix dimensions sum
to 1 + 1 + 3 + 6 + 6 = 17 (Lean thm01), the ﬁve reduced Gram-congruent blocks B0, . . . , B4
listed explicitly in Appendix A capture the full PSD cone of the 17-dimensional Hermitian
subspace for all d ≥ 4 (at d = 3 , the ([1]; [1, 1, 1]) sector has zero dimension in B3,1(3) because∧3 C3 ∼= det, so B1 is absent and only B0, B2, B3, B4 appear). Applying Γin and conjugating by
SWAP01 converts Bπ = ( Uπ)Γ1 into Bs01πs01 , inducing the exact 5-transposition involution γ
(Lean thm01, Cert. C01).
(3) Expanding (J −Q)(|u⟩⊗|c2, c3⟩) in the six distinct tensor-contraction orbits of {Bπ(|u⟩⊗
I)}π∈S4 yields ( 5) directly (veriﬁed directly on (Cd)⊗4 for d ∈ {3, 4, 5}in Cert. C02). Denoting
the left-hand sides of ( 5) by E0, . . . , E5, direct polynomial expansion of B3(d, J−Q) and B4(d, J−
Q) from Appendix A yields the six universal identities
B3(d, J − Q)0,0 = −(d(E0 + E1) + E2 + E3 + E4 + E5),
B3(d, J − Q)0,1 = −(d(E2 + E3) + E0 + E1 + E4 + E5),
B3(d, J − Q)0,2 = −(d(E4 + E5) + E0 + E1 + E2 + E3),
B4(d, J − Q)0,0 = −(d(E0 − E1) + E2 − E3 − E4 + E5),
B4(d, J − Q)0,1 = −(d(E2 − E3) + E0 − E1 + E4 − E5),
B4(d, J − Q)0,2 = −(d(E4 − E5) − E0 + E1 + E2 − E3),
proved universally for all d ∈ Z in Lean thm02–thm03 and Cert. C04. As an immediate sanity
check, evaluating all 28 Sylvester leading principal minors of Faisal’s normalized d = 8 witness
(aL = 5 /3, aM = 18 /37, qk = mπk /4440) over Z certiﬁes (2a)–(2d) in milliseconds without any
42 × 42 matrices (Lean thm04–thm05, Cert. C03).
3 Exact Dimensional Phase Transition ( dmin = 8) and d = 8
Sharpening
By Theorem 2.1, searching over all (L, M, Q) satisfying ( 2) for a ﬁxed local dimension d reduces
to minimizing cI = d aLaM + aL − aM over (aL, aM , q0, . . . , q16) ∈ R19 subject to aL ≥ 1,
4

--- Page 5 ---
aM ≥ 0, the 6 equalities ( 5), and PSD of the reduced blocks for J + Q, J − Q, and QΓin .
The only nonlinearity is the single bilinear product j0 = aLaM . On any rational subinterval
aM ∈ [ℓ, u] ⊂ [0, 1], since aL ≥ 1 > 0, every feasible tuple satisﬁes the exact linear McCormick
envelope
s0 = aL −1 ≥ 0, s 1 = aM −ℓ ≥ 0, s 2 = u−aM ≥ 0, s 3 = j0 −ℓaL ≥ 0, s 4 = uaL −j0 ≥ 0,
(6)
yielding a pure linear semideﬁnite program in x = ( j0, aL, aM , q0, . . . , q16) ∈ R20 whose dual cer-
tiﬁcates verify global lower bounds (or infeasibility) over Q with zero numerical approximation.
Theorem 3.1 (Sharp dmin = 8 Impossibility Barrier and Sharpened d = 8 Witness ρ∗
8).
1. Exact Impossibility for ALL d ∈ {3, 4, 5, 6, 7}(Lean thm06, Certs. C05–C07): For every
local dimension d ∈ {3, 4, 5, 6, 7}, no tuple (L, M, Q) of the form (1)–(2) certiﬁes an NPT
Werner state: every feasible pair satisﬁes cI ≥ d (with strict inequality cI > d for all aM ∈
[0, 1] and all (aL, aM ) ̸= (1 , 1)). Consequently, dmin = 8 is the exact minimal local dimension
of Faisal’s witness architecture.
2. Sharpened C8 ⊗ C8 Witness ρ∗
8 (Lean thm07–thm09, Cert. C08): At d = 8 , choosing
aL = 161
100 , aM = 1
2 and the explicit 17-entry rational vector q∗
8 ∈ Q17 printed in Appendix A
(Table 3, cleared denominator 640 000) satisﬁes (2) with strictly positive Sylvester minors
across all blocks and certiﬁes the strictly deeper NPT bound-entangled Werner state
ρ∗
8 = 151I − 20 SWAP
9504 , α ∗
8 = − 20
151 ≈ − 0.132450 < − 3
23 ≈ − 0.130435, (7)
improving Faisal’s Werner parameter by an exact gap of 20
151 − 3
23 = 7
3473 (and nearly saturating
the numerical SDP optimum α∗(8) ≈ − 0.132595).
Proof. (1) First, if aM ≥ 1, then since aL ≥ 1 and d ≥ 2, the identity
cI − d = d aLaM + aL − aM − d = ( aL − 1)(daM + 1) + ( d − 1)(aM − 1) ≥ 0
proves cI ≥ d unconditionally (with strict inequality cI > d unless aL = aM = 1 , which gives
α = −1/d, strictly PPT; Lean thm06).
Second, for aM ∈ [0, 1], by Theorem 2.1(1)–(2) it suﬃces to bound the linear SDP relax-
ation ( 6) over a ﬁnite rational tiling 0 = t0 < t 1 < ···< t K = 1 . On each subinterval [ℓ, u], a
rational dual tuple (λ ∈ Q5
≥0, ν ∈ Q6, {Yc ≻ 0}) (with strict positive deﬁniteness veriﬁed by
exact rational Sylvester minors) satisﬁes either:
• Infeasibility mode (ﬁrst interval [0, t1]): ∑
c⟨Yc, Ac,v⟩+ ( ST λ)v + ( ET ν)v = 0 for all v =
0, . . . , 19 with strictly positive constant − ∑
c⟨Yc, Cc⟩ −ST
constλ − ET
constν > 0, contradicting
primal feasibility Mc(x) ⪰ 0, s(x) ≥ 0, E(x) = 0 ; or
• Lower-bound mode (remaining intervals [tr, tr+1]): ∑
c⟨Yc, Ac,v⟩+ (ST λ)v + (ET ν)v = (obj) v
(where obj = ( d, 1, −1, 0, . . . , 0)), proving by weak duality cI(x) ≥ − ∑
c⟨Yc, Cc⟩ −ST
constλ −
ET
constν > d for every feasible x.
Across 33 exact rational dual certiﬁcates stored in certificates/
d_le_7_dual_witnesses.json and checked with zero ﬂoating-point arithmetic in Certs. C05–
C07, all 20 dual equality residuals vanish identically over Q, all multipliers satisfy λi ≥ 0,
all dual blocks have strictly positive Sylvester minors, and the certiﬁed global lower bounds
strictly exceed d in every dimension:
Dimension d Subintervals Infeasible [0, t1] Min certiﬁed dual cI Threshold d Margin cI − d
3 3 [0, 1/5] (+31.83) 4.4985 3 +1.4985
4 3 [0, 1/5] (+32.16) 5.1073 4 +1.1073
5 4 [0, 1/4] (+26.48) 5.6655 5 +0.6655
6 7 [0, 1/4] (+23.79) 6.3004 6 +0.3004
7 16 [0, 1/4] (+21.47) 7.0272 7 +0.0272
5

--- Page 6 ---
Figure 1: (a) Exact dimensional phase transition at dmin = 8 : certiﬁed rational dual lower
bounds strictly exceed cI = d for all d ≤ 7 (Theorem 3.1), whereas our closed-form inﬁnite
family ( cI = (5 d + 7)/6, Theorem 4.1) and sharpened ρ∗
8 (cI = 151 /20) lie strictly inside the
NPT region cI < d for all d ≥ 8. (b) Exact rational dual lower-bound proﬁle across all 16
subintervals tiling aM ∈ [0, 1] at d = 7 (minimum cI ≥ 7.0272 > 7 on [27/50, 14/25]).
Thus cI > d on [0, 1] and cI ≥ d on [1, ∞ ) for all d ∈ {3, 4, 5, 6, 7}.
(2) At d = 8 , aL = 161 /100 ≥ 1, aM = 1 /2 ≥ 0, we have cI = 8 ·161
100 ·1
2 + 161
100 − 1
2 = 151
20 < 8,
giving α∗
8 = −20/151, trace 151 ·64 − 20 ·8 = 9504 , eigenvalues 131/9504, 171/9504 > 0, and
(ρ∗
8)Γ|u⟩= − 9
9504 |u⟩= − 1
1056 |u⟩< 0. Clearing denominators by 640 000, Lean thm07–thm09 and
Cert. C08 verify exact satisfaction of ( 5), exact vanishing of row/column 0 of B3, B4 in J − Q,
and strict positivity of all 28 Sylvester minors.
4 Closed-Form Inﬁnite Family for ALL d ≥ 8 and High-
Dimension Depth Scaling
Trivially embedding an 8 × 8 bound-entangled state into Cd ⊗ Cd breaks U(d) ⊗ U(d) symmetry
and does not produce a Werner state. We now construct a single closed-form rational witness
Qinf (d) ∈ B3,1(d) that certiﬁes an explicit NPT bound-entangled Werner state in every local
dimension d ≥ 8 simultaneously, and we complement it with ﬁve exact rational high- d primal
witnesses up to d = 400 corroborating a numerical O(1/
√
d) depth scaling.
Theorem 4.1 (Closed-Form All- d ≥ 8 NPT Bound-Entangled Family & Constructive High- d
Separation).
1. Explicit Inﬁnite Family for Every Integer d ≥ 8 (Lean thm10–thm15, Certs. C09–C13):
Fix aL = 5 /3, aM = 1 /2, and deﬁne the rational vector qinf (d) ∈ Q17 by
q0(d) = a0 + b0
d + c0
d2 , q k(d) = ak
d + bk
d2 (k = 1 , . . . , 16), (8)
with exact integer-scaled numerators 1500 ak, 1500 bk, and 1500 c0 = 3819 listed in Table 2.
Then (L, M, Qinf (d)) satisﬁes all four conditions (2) for every integer d ≥ 8, certifying the
closed-form inﬁnite family of NPT bound-entangled Werner states
ρd = (5d + 7)I − 6 SWAP
d(5d2 + 7d − 6) , α (d) = − 6
5d + 7 < − 1
d (∀d ≥ 8), (9)
each having ED(ρd) = 0 and two-qubit separable-operation Bell ﬁdelity ≤ 1+
√
2
4 .
6

--- Page 7 ---
Table 2: Exact integer-scaled coeﬃcients 1500 ak and 1500 bk (1500 c0 = 3819 ) for the all- d ≥ 8
closed-form witness ( 8) with (aL, aM ) = (5 /3, 1/2).
k 0 1 2 3 4 5 6 7 8
1500 ak 402 357 −240 444 −1308 848 0 −750 0
1500 bk −3510 −3150 2058 −2943 10617 1760 1143 −357 2568
k 9 10 11 12 13 14 15 16 1500 c0
1500 ak −1500 2500 3165 −3459 2433 −2568 7338 447 —
1500 bk 582 −3462 −4644 9975 −7032 2586 −13203 −7032 3819
2. Constructive High- d Separation ( d ≤ 400) & Numerical
√
d Fit
(Cert. C16): Five explicit exact rational primal witnesses in certificates/
asymptotic_primal_witnesses.json constructively certify cI(d) <
√
7 d at
d ∈ { 16, 36, 64, 100, 400}, reaching α = − 250000
12881729 ≈ − 0.01941 at d = 400 (7.76×
deeper than the PPT threshold −1/400 = −0.0025). These rigorous ﬁnite- d certiﬁcates cor-
roborate a numerical SDP scaling ﬁt c∗
I(d) ∼ 2.31
√
d (obtained by setting aM (d) ≈ 1.45/
√
d),
while proving an all- d Θ(1/
√
d) asymptotic law remains open.
Proof. (1) With aL = 5 /3 and aM = 1 /2, ( 3) gives cI(d) = 5
6 d + 5
3 − 1
2 = 5d+7
6 , which satisﬁes
cI(d) < d ⇐⇒ 5d + 7 < 6d ⇐⇒ d ≥ 8 (note that d = 7 hits the exact PPT boundary
α(7) = −1/7). For every d ≥ 8, the trace is (5d + 7)d2 − 6d = d(5d2 + 7d − 6) > 0, both state
eigenvalues 5d+1
Z(d) , 5d+13
Z(d) are strictly positive, and ρΓ
d |u⟩= − d−7
Z(d) |u⟩< 0 (Lean thm11, Cert. C13).
To certify ( 2) simultaneously for all integers d ≥ 8, substitute d = 8+ s (s ∈ N) and multiply
J and qinf (d) by the strictly positive scalar 1500 d2. Every coordinate becomes an exact integer
polynomial in s of degree ≤ 2:
• All six residual polynomials of ( 5) vanish identically in Z[s] (Lean thm10, Cert. C09), and
consequently all six row- 0 entries of B3, B4 for 1500 d2(J − Q) vanish identically in Z[s]
(Lean thm14).
• Expanding all 28 Sylvester leading principal minors across the ﬁve blocks of 1500 d2(J + Q)
(10 minors, degrees 2–10 in s), 1500 d2(J −Q) (8 minors on B0, B1, B2 and the lower-right 2×2
subblocks of B3, B4, degrees 2–7), and 1500 d2QΓin (10 minors, degrees 2–9) yields integer
polynomials P(s) = ∑m
r=0 crsr ∈ Z[s] in which every single coeﬃcient satisﬁes cr ≥ 0 with
c0 > 0!
• Hence P(s) > 0 for every integer s ≥ 0 (i.e., every d ≥ 8), proved via constructive polynomial
reﬂection in Lean thm12–thm15 and independently conﬁrmed over Q[s] in Certs. C10–C12.
By Theorem 2.1 and [ 6, Lemmas 4–6], ρd is NPT bound entangled for every integer d ≥ 8.
(2) For the constructive Θ(1/
√
d) witnesses at d ∈ {16, 36, 64, 100, 400}, exact zero-ﬂoat
veriﬁcation of (2d) and all 28 Sylvester minors in Cert. C16 conﬁrms: d = 16 : cI = 517133
50000 ≈ 10.34
(cI/
√
d ≈ 2.59); d = 36 : cI = 471367
31250 ≈ 15.08 (2.51); d = 64 : cI = 4987101
250000 ≈ 19.95 (2.49);
d = 100 : cI = 49937
2000 ≈ 24.97 (2.50); d = 400 : cI = 12881729
250000 ≈ 51.53 (2.58), every one satisfying
c2
I < 7d.
5 4-Branch U(d)-Equivariant Uniqueness Barrier and White-
Noise Robustness
Every U(d)-equivariant linear map Λ : Md(C) → Md(C) falls into one of two symmetry classes:
covariant maps satisfying Λ(UXU †) = UΛ(X)U†for all U ∈ U(d) take the form X ↦→aTr(X)I+
bX (Choi matrix aI + b|u⟩⟨u|, CP iﬀ a ≥ 0, a + db ≥ 0), whereas conjugate-covariant maps
satisfying Λ(UXU †) = ¯UΛ(X)UT take the transpose form X ↦→aTr(X)I + bXT (Choi matrix
7

--- Page 8 ---
Figure 2: (a) Certiﬁed NPT depth |α(d)|versus the PPT threshold 1/d: our all- d ≥ 8 closed-
form family achieves 6
5d+7 uniformly, while exact rational witnesses at d ∈ {8, 16, 36, 64, 100, 400}
track the numerical SDP ﬁt (2.31
√
d)−1, penetrating 7.76× deeper than 1/d at d = 400 .
(b) Stabilized normalized inverse depth cI(d)/
√
d across exact rational witnesses (strictly below√
7 ≈ 2.646 for all ﬁve high- d witnesses d ≥ 16 in Cert. C16; at d = 8 , cI(8)/
√
8 = 151
20
√
8 ≈ 2.669).
aI + b SWAP, CP iﬀ a ≥ |b|). Up to exchanging Alice and Bob, a local pair (L, M) therefore
falls into four branches: (X, X), (XT , XT ), (XT , X) with bL > 0, bM < 0, or (XT , X) with
bL < 0, bM > 0 (since bLbM ≥ 0 on (XT , X) gives cS ≥ 0, immediately PPT).
Theorem 5.1 (4-Branch Uniqueness Barrier, Convex Werner Intervals, and White-Noise Ro-
bustness).
1. Uniqueness of the (XT , X) Negative-bL Branch (Lean thm16–thm17, Cert. C14):
• Branches (X, X) and (XT , XT ) map |u⟩⟨u|to an isotropic operator cII+cu|u⟩⟨u|(cI ≥ 0);
whenever NPT ( cu > c I), its maximally entangled ﬁdelity F = cI +dcu
d(dcI +cu) strictly exceeds
1/d, so the state is 1-copy distillable [ 9, 4].
• Branch (XT , X) with bL > 0, bM < 0 satisﬁes aL ≥ bL > 0 and aM ≥ d|bM |, forcing
cI + dcS = aL(daM − |bM |) + bL(aM − d|bM |) ≥ bL(d2 − 1)|bM |> 0,
so its output is always strictly PPT (separable).
Hence Faisal’s (XT , X) branch with bL < 0, bM > 0 (up to Alice–Bob swap) is the unique
U(d)-equivariant local-map branch capable of certifying NPT bound entanglement.
2. Certiﬁed Werner Intervals & Exact White-Noise Threshold (Lean thm18–thm20,
Cert. C15): Whenever ρ(d, αcert) is certiﬁed NPT bound entangled ( αcert < −1/d), every
Werner state ρ(d, α) with α ∈ [αcert, −1/d) is NPT bound entangled. Equivalently, under the
depolarizing white-noise channel Dp(ρ) := (1 − p)ρ + p I
d2 , Dp(ρ(d, α)) remains NPT bound
entangled if and only if
0 ≤ p < p max(d, α) := d(1 + dα)
α(d2 − 1) . (10)
At d = 8 , our sharpened witness ρ∗
8 (α = −20/151) raises the certiﬁed white-noise tol-
erance by an exact +35% (ratio 27/20), from Faisal’s pmax(8, −3/23) = 8
189 ≈ 4.23% to
pmax(8, −20/151) = 2
35 ≈ 5.71%. For our all- d ≥ 8 closed-form family (9), pmax
(
d, − 6
5d+7
)
=
d(d−7)
6(d2−1) → 1
6 as d → ∞ (and our d = 400 exact witness tolerates > 87% white noise).
8

--- Page 9 ---
Figure 3: (a) Exact certiﬁed white-noise depolarizing robustness pmax at d = 8 : our sharpened
witness ρ∗
8 achieves 2
35 ≈ 5.71%, an exact +35% gain over Faisal’s 8
189 ≈ 4.23% (Theorem 5.1).
(b) Growth of certiﬁed white-noise tolerance pmax(d) for d ≥ 8: the closed-form family rises
monotonically toward 1/6 ≈ 16.67%, while exact rational Θ(1/
√
d) witnesses exceed 75% by
d = 100 (and 87% at d = 400 ).
Proof. (1) Applying (L ⊗ M) to |u⟩⟨u|= ∑
i,j |i⟩⟨j| ⊗ |i⟩⟨j|: when both maps carry X (or both
carry XT ), (X ⊗ X)(|u⟩⟨u|) = |u⟩⟨u|and (XT ⊗ XT )(|u⟩⟨u|) = |u⟩⟨u|, yielding an isotropic
operator cII + cu|u⟩⟨u|where cI ≥ 0 follows from PSD on the (d2 − 1)-dimensional orthogonal
complement of |u⟩. Its partial transpose is cII + cuSWAP, which is NPT iﬀ cu > c I (since
PSD of the state requires cI + dcu ≥ 0, ruling out cu < −cI). Whenever cu > c I and d ≥ 2,
(cI + dcu) − (dcI + cu) = ( d − 1)(cu − cI) > 0 (Lean thm17), so F = cI +dcu
d(dcI +cu) > 1
d, which is
1-copy distillable [ 9, 4]. On the (XT , X) branch with bL > 0, bM < 0, CP of L and M requires
aL ≥ bL > 0 and aM ≥ d|bM |> 0. Expanding cI = daLaM − aL|bM |+ bLaM and cS = −bL|bM |
gives cI +dcS = aL(daM −|bM |)+ bL(aM − d|bM |) ≥ bL(d2 − 1)|bM |> 0 (Lean thm16, Cert. C14),
so the partial transpose eigenvalue on |u⟩is strictly positive.
(2) For any α ∈ [αcert, −1/d), writing ρ(d, α) = (1 − t)ρ(d, αcert) + t ρ(d, −1/d) yields exact
convex weights t ∈ [0, 1) (Lean thm20). Because ρ(d, −1/d) is separable [ 23], any LOCC distilla-
tion protocol for ρ(d, α) can be simulated on ρ(d, αcert) by local mixing with the separable state
ρ(d, −1/d), forcing ED(ρ(d, α)) ≤ ED(ρ(d, αcert)) = 0 (indeed, mixing with I
d2 is a local depo-
larizing channel!). Direct calculation gives Dp(ρ(d, α)) = ρ(d, αp) with αp = (1−p)dα
d+pα ; solving
αp = −1/d yields ( 10) identically (Lean thm18), with α ≤ αp < −1/d for all 0 ≤ p < p max(d, α).
Substituting (8, −3/23), (8, −20/151), and (d, −6/(5d + 7)) gives 8
189 , 2
35 , ratio 27
20 , and d(d−7)
6(d2−1)
(Lean thm19, Cert. C15).
6 Formal Veriﬁcation Architecture and Reproducibility
All algebraic reductions, d = 8 Sylvester certiﬁcations, all- d ≥ 8 symbolic positivity proofs, d ≤ 7
exact rational dual certiﬁcates, uniqueness inequalities, and white-noise thresholds are veriﬁed
across three independent layers (while Haar-twirling completeness and the LOCC simulation
argument are proved in Sections 2 and 5):
1. Constructive Lean 4.36.0 Formalization: 20 theorems ( thm01–thm20) in lean/
NPTBoundEntanglementBarriers.lean compiling under lean -DwarningAsError=true
with zero external imports, zero sorry, zero grind, zero Classical.choice, and zero
9

--- Page 10 ---
warnings—including full computational polynomial reﬂection over Z[s] proving all 28
Sylvester minors strictly positive for every integer d = 8 + s ≥ 8.
2. AST-Audited Zero-Float Python Veriﬁer: Pure standard-library code ( int, Fraction)
in verification/verify_npt_bound_entanglement.py self-auditing its AST (0 ﬂoat vi-
olations) and emitting 16 canonical SHA-256 certiﬁcates ( C01–C16) across four modes—
including exact veriﬁcation of all 33 rational SDP duals for d ∈ {3, 4, 5, 6, 7}and 5 high-d ratio-
nal primal witnesses up to d = 400 —with manifest SHA-256 49651e4871bc91b7da32647d7fe20c36
da7ef042b9f26650f7504750e55f4afa.
3. Adversarial Test Suite: 56 pytest checks in tests/test_adversarial.py covering posi-
tive certiﬁcation, boundary perturbations, tampered dual rejection, and high- d asymptotic
scaling.
References
[1] K. Bharti, R. Gajjala, and T. Haug. Two-copy nondistillability of Werner states: Sharp
partial-trace inequalities and ﬁnite-copy extensions. arXiv:2607.24479, 2026.
[2] Eric Chitambar, Debbie Leung, Laura Mančinska, Maris Ozols, and Andreas Winter. Every-
thing you always wanted to know about LOCC (but were afraid to ask). Communications
in Mathematical Physics , 328:303–326, 2014.
[3] David P. DiVincenzo, Peter W. Shor, John A. Smolin, Barbara M. Terhal, and Ashish V.
Thapliyal. Evidence for bound entangled states with negative partial transpose. Physical
Review A , 61:062312, 2000.
[4] Wolfgang Dür, J. Ignacio Cirac, Maciej Lewenstein, and Dagmar Bruß. Distillability and
partial transposition in bipartite systems. Physical Review A , 61:062313, 2000.
[5] Tilo Eggeling, Karl Gerd H. Vollbrecht, Reinhard F. Werner, and Michael M. Wolf. Distill-
ability via protocols respecting the positivity of partial transpose. Physical Review Letters ,
87:257902, 2001.
[6] Islam Faisal. Bound entanglement with negative partial transpose exists.
arXiv:2611.34921v1 [quant-ph], 2026. Preprint, November 25, 2026.
[7] T. C. Fraser, F. Huber, B. Pozsgay, and I. Vona. On the two-copy distillability of Werner
states and a new partial trace inequality. arXiv:2607.24309, 2026.
[8] J. Fu, L. Gao, and S.-J. Park. A solution to 2-copy distillability of Werner states.
arXiv:2607.21367, 2026.
[9] Michał Horodecki, Paweł Horodecki, and Ryszard Horodecki. Inseparable two spin- 1
2 den-
sity matrices can be distilled to a singlet form. Physical Review Letters , 78:574–577, 1997.
[10] Michał Horodecki, Paweł Horodecki, and Ryszard Horodecki. Mixed-state entanglement
and distillation: Is there a “bound” entanglement in nature? Physical Review Letters ,
80:5239–5242, 1998.
[11] Paweł Horodecki, Łukasz Rudnicki, and Karol Życzkowski. Five open problems in quantum
information theory. PRX Quantum , 3:010101, 2022.
[12] I. MacCormack and N. Bao. Three copies of the Werner state: The sharp curve in di-
mensions three and four and a bound in every dimension. Preprint, October 23, 2026,
2026.
10

--- Page 11 ---
[13] Alexander Müller-Hermes, David Reeb, and Michael M. Wolf. Positivity of linear maps
under tensor powers. Journal of Mathematical Physics , 57:015202, 2016.
[14] OpenAI. Entanglement with zero distillable secret key in local dimension ten. Preprint,
September 27, 2026, 2026.
[15] Łukasz Pankowski, Marco Piani, Michał Horodecki, and Paweł Horodecki. A few steps more
towards NPT bound entanglement. IEEE Transactions on Information Theory , 56:4085–
4100, 2010.
[16] Asher Peres. Separability criterion for density matrices. Physical Review Letters , 77:1413–
1415, 1996.
[17] Peter W. Shor, John A. Smolin, and Barbara M. Terhal. Nonadditivity of bipartite distil-
lable entanglement follows from a conjecture on bound entangled Werner states. Physical
Review Letters, 86:2681–2684, 2001.
[18] Z. Song and L. Chen. A partial-trace matrix inequality and Werner-state distillability.
arXiv:2607.23416, 2026.
[19] T. S. Tomar. Equality cases and every-copy results for the Werner endpoint inequality.
Hexagon preprint 2611.00466v1, November 15, 2026, 2026.
[20] T. S. Tomar. Undistillability of Werner states from three, four and ﬁve copies. Hexagon
preprint 2611.00464v1, November 15, 2026, 2026.
[21] Karl Gerd H. Vollbrecht and Michael M. Wolf. Activating distillation with an inﬁnitesimal
amount of bound entanglement. Physical Review Letters , 88:247901, 2002.
[22] John Watrous. The Theory of Quantum Information . Cambridge University Press, Cam-
bridge, 2018.
[23] Reinhard F. Werner. Quantum states with Einstein-Podolsky-Rosen correlations admitting
a hidden-variable model. Physical Review A , 40:4277–4281, 1989.
A Explicit Walled Brauer Basis, Five Reduced Blocks, and q∗
8
To make Theorems 2.1, 3.1, and 4.1 completely self-contained within this manuscript, we list
the exact 17-element Hermitian basis pairing, all ﬁve reduced block matrices B0, . . . , B4, and all
17 rational coordinates of q∗
8.
17-Element Hermitian Basis Map. Ordering S4 lexicographically as π0 =
(0, 1, 2, 3), . . . , π23 = (3 , 2, 1, 0) (matching [ 6, Appendix A] with 0-based indices), the 17
Hermitian generators Bk = ∑
i∈Gk (Uπi )Γ1 correspond to the 10 involutions and 7 inverse pairs:
G0 = {0}, G1 = {1}, G2 = {2}, G3 = {3, 4}, G4 = {5},
G5 = {6}, G6 = {7}, G7 = {8, 12}, G8 = {9, 18}, G 9 = {10, 13},
G10 = {11, 19}, G 11 = {14}, G 12 = {15, 20}, G 13 = {16}, G14 = {17, 22},
G15 = {21}, G16 = {23}.
The input-swap partial-transpose involution γ swaps (2, 11), (3, 12), (4, 15), (8, 9), (13, 16) and
ﬁxes the remaining 7 indices {0, 1, 5, 6, 7, 10, 14}.
11

--- Page 12 ---
Five Reduced U(d)-Isotypic Blocks B0, . . . , B4. For any x = ( x0, . . . , x16) ∈ R17 and local
dimension d ≥ 3:
B0(x) = [ x0 + x1 + x11 + 2x12 + x15], B1(x) = [ x0 − x1 − x11 + 2x12 − x15] ( d ≥ 4),
B2(x) =
(
6x0 + 6x1 − 3x11 − 6x12 − 3x15 3x11 − 3x15
3x11 − 3x15 2x0 − 2x1 + x11 − 2x12 + x15
)
,
and the two symmetric 3 × 3 blocks B3(d, x) and B4(d, x) have upper-triangular entries:
(B3)00 = d2(x5 + x6) + d(x0 + x1 + 2(x7 + x8 + x9 + x10))
+ x2 + 2x3 + x4 + x11 + 2x12 + x13 + 2x14 + x15 + x16,
(B3)01 = d2(x7 + x8) + d(x2 + x3 + x5 + x6 + x9 + x10 + x11 + x12 + x14 + x16)
+ x0 + x1 + x3 + x4 + x7 + x8 + x9 + x10 + x12 + x13 + x14 + x15,
(B3)02 = d2(x9 + x10) + d(x3 + x4 + x5 + x6 + x7 + x8 + x12 + x13 + x14 + x15)
+ x0 + x1 + x2 + x3 + x7 + x8 + x9 + x10 + x11 + x12 + x14 + x16,
(B3)11 = d2(x2 + x16) + d(x0 + 2x3 + 2x7 + 2x8 + 2x14 + x15)
+ x1 + x4 + x5 + x6 + 2x9 + 2x10 + x11 + 2x12 + x13,
(B3)12 = d2(x3 + x14) + d(x1 + x2 + x4 + x7 + x8 + x9 + x10 + x12 + x13 + x16)
+ x0 + x3 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x14 + x15,
(B3)22 = d2(x4 + x13) + d(x0 + 2x3 + 2x9 + 2x10 + x11 + 2x14)
+ x1 + x2 + x5 + x6 + 2x7 + 2x8 + 2x12 + x15 + x16,
and
(B4)00 = d2(x5 − x6) + d(x0 − x1 + 2(x7 − x8 − x9 + x10))
+ x2 − 2x3 + x4 + x11 − 2x12 − x13 + 2x14 + x15 − x16,
(B4)01 = d2(x7 − x8) + d(x2 − x3 + x5 − x6 + x9 − x10 + x11 − x12 + x14 − x16)
+ x0 − x1 + x3 − x4 + x7 − x8 − x9 + x10 + x12 + x13 − x14 − x15,
(B4)02 = d2(x9 − x10) + d(x3 − x4 − x5 + x6 + x7 − x8 + x12 + x13 − x14 − x15)
− x0 + x1 + x2 − x3 − x7 + x8 + x9 − x10 + x11 − x12 + x14 − x16,
(B4)11 = d2(x2 − x16) + d(x0 + 2x3 + 2x7 − 2x8 − 2x14 − x15)
+ x1 + x4 + x5 − x6 + 2x9 − 2x10 + x11 − 2x12 − x13,
(B4)12 = d2(x3 − x14) + d(x1 + x2 + x4 − x7 + x8 + x9 − x10 − x12 − x13 − x16)
+ x0 + x3 − x5 + x6 + x7 − x8 − x9 + x10 − x11 + x12 − x14 − x15,
(B4)22 = d2(x4 − x13) + d(x0 + 2x3 − 2x9 + 2x10 − x11 − 2x14)
+ x1 + x2 + x5 − x6 − 2x7 + 2x8 − 2x12 + x15 − x16.
Explicit Sharpened d = 8 Witness q∗
8. Table 3 lists all 17 exact rational coordinates of q∗
8
(Theorem 3.1(2), (aL, aM ) = (161 /100, 1/2), α∗
8 = −20/151, common denominator 640 000).
Table 3: Exact integer-scaled coordinates 640 000 (q∗
8)k for the sharpened d = 8 witness ρ∗
8 =
151I−20 SWAP
9504 .
k 0 1 2 3 4 5 6 7 8
640 000 (q∗
8 )k 192 −64 0 64 0 56234 7291 −42296 18024
k 9 10 11 12 13 14 15 16 —
640 000 (q∗
8 )k −76288 107432 136192 −115136 85376 −117824 288768 −29120 —
12
