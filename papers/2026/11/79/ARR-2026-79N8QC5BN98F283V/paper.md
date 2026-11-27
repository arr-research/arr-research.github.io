# Exact Bloch-Sphere Surrogates, Heisenberg R_zz Entangler Leakage, and Token-Mixing Barriers for Multi-Head Quantum Neural Networks inside Large Language Models

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-79N8QC5BN98F283V` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/multihead-qnn-bloch-surrogate-entangler-leakage-and-token-mixing-barriers (`v1.0.0`)  
**Canonical PDF SHA-256:** `00492d270a07d7f939996c9e731aea4e3fd859b1094c60b5600f565d7b265c09`

## Abstract

Amoussou et al. (arXiv:2611.15250, Nov 2026) showed that a 145,281-parameter multi-head QNN (D = 2048, k = 32 heads, n_q = 8 qubits, L = 4 layers) can replace up to eight contiguous transformer blocks in Qwen3-30B-A3B and run on a 156-qubit IBM Heron processor, while leaving three empirical anomalies unexplained: collapse of the no-circuit mixer control (alpha -> 0.004) on sensitive Layer 1, superior perplexity of entangler-off and frozen-angle controls over trained entangled circuits, and failure of scattered replacements to compose on long-range tasks (LAMBADA). We resolve all three anomalies algebraically with 20 constructive Lean 4.36.0 theorems and 16 exact Q[i] certificates. First, entangler-off heads factorize into n_q decoupled SO(3) Bloch evolutions, giving an exact O(n_q L) classical surrogate reproducing all 1- and 2-qubit Pauli expectations with 64/3x state compression at n_q = 8. Second, we prove strict odd-parity L^2 orthogonality of M_2 tanh(M_1 x) against all even/bias components, and derive exact Heisenberg-picture R_zz leakage laws showing that interior 1-qubit {X,Y}_q leak sin^2(g_{q-1})sin^2(g_q), mixed {X,Y}Z leak sin^2(g_{q-1})cos^2(g_q), and interior transverse 2-qubit {X,Y}_q{X,Y}_{q+1} leak 1 - cos^2(g_{q-1})cos^2(g_{q+1}) into the 99.85% unmeasured weight >= 3 Pauli space (75% single-layer loss at gamma = pi/4, 100% extinction at pi/2, and 28/87 = 32.2% mean loss at n_q = 8). Third, we prove the exact conditional-variance token-mixing barrier E[Var(F_t(X) | x_t)] for any position-wise replacement and prove classical readout parameter dominance >= 2/3 whenever d_h >= 14 (131,072/145,281 = 90.22% in Qwen3-30B).

## Full Extracted Text

--- Page 1 ---
Exact Bloch-Sphere Surrogates, Heisenberg Rzz
Entangler Leakage,
and Token-Mixing Barriers for Multi-Head Quantum
Neural Networks
inside Large Language Models
Lluis Eriksson∗
November 27, 2026
Abstract
Amoussou, Aizpurua, Singh, Orús, and Jacobsen [ 1] recently demonstrated that a single
multi-head quantum neural network (QNN) with 145,281 trainable parameters ( D = 2048 ,
k = 32 heads, nq = 8 qubits, L = 4 layers) can replace up to eight contiguous trans-
former blocks inside Qwen3-30B-A3B and execute on a 156-qubit IBM Heron processor.
Their ablation study uncovered three striking empirical anomalies left open theoretically:
(i) deleting the quantum heads leaves a mixer-only control M2 tanh(M1x) whose residual
gate collapses ( α= 0 .0042–0.0056 on two of three seeds) and loses 3.5 perplexity points on
sensitive Layer 1; (ii) switching all Rzz entanglers oﬀ or freezing circuit angles consistently
beats the trained entangled circuit on held-out perplexity; and (iii) replacing scattered sensi-
tive blocks fails to compose and degrades long-range context tasks (LAMBADA). We resolve
all three anomalies algebraically from ﬁrst principles, backed by 20 constructive Lean 4.36.0
theorems and 16 zero-ﬂoat Q[i] certiﬁcates. First, when entanglers vanish ( γ = 0 ), ev-
ery nq-qubit, L-layer dense-angle-encoded head collapses identically to nq decoupled SO(3)
Bloch evolutions, yielding an exact O(nqL) classical surrogate reproducing all 1- and 2-qubit
Pauli expectations with 2 ·2nq /(3nq) = 64 /3× state compression at nq = 8 and zero 2nq
statevector cost. Second, we prove the exact odd-parity collapse of the mixer-only control
(gmix(−x) = −gmix(x) = ⇒ MSE(f,gmix) ≥ ∥feven∥2
L2 , strictly unable to ﬁt biases or even
nonlinearities) and derive the exact Heisenberg-pictureRzz leakage laws for every operator in
the open-chain local readout pool: interior 1-qubit {X,Y }q leak sin2 γq−1 sin2 γq into unmea-
sured weight-3 strings, interior mixed {X,Y }Z leak sin2 γq−1 cos2 γq, and interior transverse
2-qubit {X,Y }q{X,Y }q+1 leak 1− cos2 γq−1 cos2 γq+1 into unmeasured weight- 3 and weight-
4 strings ( 75% single-layer loss at γ = π/4, 100% extinction at γ = π/2, and 28/87 = 32 .2%
mean single-layer loss across all 87 open-chain pool observables at nq = 8 , where 99.85%
of the Pauli space is unmeasured). Third, we prove the exact conditional-expectation
Pythagorean token-mixing barrier infg E∥Ft(X) − g(xt)∥2
2 = E[Var(Ft(X) |xt)] for any
position-wise replacement and prove that the classical block-diagonal readout W(j) accounts
for at least 2/3 of all trainable parameters whenever dh ≥ 14 (131,072/145,281 = 90 .22% in
Qwen3-30B).
∗Independent Researcher. Research, constructive formal veriﬁcation in Lean 4.36.0, exact Q[i]
statevector and Heisenberg certiﬁcate veriﬁcation, adversarial testing, and manuscript typesetting
were conducted with transparent assistance from Google Antigravity. Code is released under
MIT; manuscript and ﬁgures under CC-BY-4.0. Repository: https://github.com/lluiseriksson/
multihead-qnn-bloch-surrogate-entangler-leakage-and-token-mixing-barriers (v1.0.0).
1
AIRR:ARR-2026-79N8QC5BN98F283V v1  [Quantum physics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
1 Introduction
Embedding variational quantum circuits inside production-scale large language models (LLMs)
faces an acute dimensional bottleneck: amplitude encoding requires O(D) circuit depth [ 7],
while naive angle encoding requires O(D) qubits [ 4]. Amoussou et al. [ 1] bridged this gap with
the multi-head QNN : partitioning D= 2 nqLkhidden activations across kindependent nq-qubit
heads coupled by constrained Sylvester–Hadamard linear mixers Mi = Λ i,2HΛi,1 (i= 1 ,2):
y = x+ αgΘ(x), g Θ(x) = M2 fQNN
(
tanh(M1x)
)
. (1)
Each head applies Llayers of dense angle encoding ( Ry,Rz on distinct features per layer), vari-
ational Rx(θ), and an open chain of nq − 1 nearest-neighbor Rzz (γj) entanglers, then measures
m local Pauli strings from the 13nq-element pool of 1-qubit {I,X,Y,Z } and nearest-neighbor
2-qubit {X,Y,Z }⊗2 observables, followed by a trainable dh × m linear readout W(j).
Deployed inside Qwen3-30B-A3B ( D = 2048 , nq = 8 , L= 4 , k = 32 , m= dh = 64 , 145,281
trainable parameters), the architecture revealed three sharp empirical puzzles [ 1, Sec. IV]:
1. On sensitive Layer 1, removing the quantum heads (leaving only y= x+ αM2 tanh(M1x))
drove α down to 0.0042–0.0056 on two of three seeds (and 0.0332 on the third) and
worsened WikiText-2 perplexity by +3.5 points ( 9.309 → 12.787).
2. Conversely, setting all Rzz entanglers to zero ( γ = 0 ), or freezing the circuits at small
initial or random angles while training the readout and mixers, outperformed the full
trained entangled module ( 8.994–9.077 vs. 9.230 on WikiText-2; 14.369–14.449 vs. 15.001
on C4).
3. Replacing N scattered sensitive blocks failed to compose ( 8.946 → 149.252 at N = 16 )
and forfeited long-range context recovery on LAMBADA.
In this paper we prove that all three empirical behaviors are exact algebraic consequences of
the architecture’s symmetry, Heisenberg-picture operator spreading, parameter allocation, and
position-wise locality:
• Theorem 1 (Exact O(nqL) Classical Bloch Surrogate): Zero-entangler heads factor-
ize identically into nq independent SO(3) Bloch trajectories reproducing all 1- and 2-qubit
pool observables with 64/3× state compression at nq = 8 and zero statevector simulation.
• Theorem 2 (Odd-Parity Collapse & Heisenberg Rzz Leakage): The no-circuit
control M2 tanh(M1x) is strictly odd and orthogonal to all even/bias target components,
whereas nonzero Rzz (γ) entanglers deterministically leak local Pauli signal into the 99.85%
unmeasured weight- ≥ 3 operator complement with exact closed-form trigonometric rates.
• Theorem 3 (Token-Mixing Barrier & Readout Dominance): Any position-wise
replacement faces an exact conditional-variance ﬂoor E[Var(Ft(X) |xt)], while the classical
readout W(j) consumes ≥ 2/3 of all parameters for dh ≥ 14 (90.22% in Qwen3-30B).
2 Exact Classical Bloch-Sphere Surrogate for Product Heads
Each head of [ 1] acts on dh = 2 nqL bounded inputs u = ( u(y)
q,ℓ ,u(z)
q,ℓ )q∈[nq],ℓ∈[L] via layer-wise
aﬃne maps ψq,ℓ = a(y)
q,ℓ u(y)
q,ℓ + b(y)
q,ℓ and ϕq,ℓ = a(z)
q,ℓ u(z)
q,ℓ + b(z)
q,ℓ . In the entangler-oﬀ control ( γj,ℓ = 0
for all j,ℓ), the head unitary factorizes as U(u,θ) = ⊗nq
q=1 Uq(uq,θq), where
Uq(uq,θq) =
1∏
ℓ=L
Rx(θq,ℓ) Rz(ϕq,ℓ) Ry(ψq,ℓ) ∈ SU(2). (2)
2

--- Page 3 ---
Theorem 1 (Exact O(nqL) Classical Bloch Surrogate and State Compression) . Let U(u,θ) =⊗nq
q=1 Uq be any entangler-oﬀ multi-head QNN circuit of depth L on nq qubits initialized in
|0⟩⊗nq , and let Rx(·),Ry(·),Rz(·) ∈ SO(3) denote the adjoint Bloch-sphere rotations.
(a) Exact SO(3) trajectory equivalence: Deﬁning r(0)
q = (0 ,0,1)T ∈ S2 and iterating
r(ℓ)
q = Rx(θq,ℓ) Rz(ϕq,ℓ) Ry(ψq,ℓ) r(ℓ−1)
q (ℓ= 1 ,...,L ), (3)
every single-qubit and two-qubit Pauli expectation satisﬁes the exact closed-form identities
⟨σ(α)
q ⟩ =
(
r(L)
q
)
α, ⟨σ(α)
q ⊗ σ(β)
q′ ⟩ =
(
r(L)
q
)
α
(
r(L)
q′
)
β (q̸= q′, α,β∈ {x,y,z }). (4)
Every intermediate vector preserves ∥r(ℓ)
q ∥2
2 = 1 identically (Lean thm01–thm03, Certiﬁ-
cate cert01).
(b) Exact multilinear trigonometric degree and zero cross-qubit mixing: Each coordinate
(r(L)
q )α is a multilinear trigonometric polynomial of degree at most 1 in each of the 2L
features assigned to qubit q and is identically independent of the remaining 2(nq − 1)L
features of the head.
(c) Exact classical complexity and Qwen3-30B compression: Evaluating all 13nq candidate
pool observables via (3)–(4) requires O(nqL) real arithmetic operations and 3nq real state
coordinates instead of 2 ·2nq real statevector amplitudes. At Qwen3-30B’s nq = 8 , this
gives exact state compression 512/24 = 64 /3 ≈ 21.33× (Lean thm04, Certiﬁcate cert02).
Proof. Since SU(2) acts on traceless Hermitian matrices r·σ by the double cover SU(2) → SO(3)
(Rµ(ϕ)(r ·σ)Rµ(ϕ)† = ( Rµ(ϕ)r) ·σ), induction over ℓ = 1 ,...,L gives ρ(L)
q = Uq|0⟩⟨0|U†
q =
1
2 (I + r(L)
q ·σ) with ∥r(L)
q ∥2 = 1 (Lean thm02–thm03). Because ρ(L) = ⊗nq
q=1 ρ(L)
q , taking
traces against σ(α)
q and σ(α)
q ⊗ σ(β)
q′ yields ( 4) immediately. Because each layer ℓ enters r(L)
q
through one linear matrix Rz(ϕq,ℓ)Ry(ψq,ℓ) whose entries are aﬃne in (cos ψq,ℓ,sin ψq,ℓ) and
(cos ϕq,ℓ,sin ϕq,ℓ), each feature appears with trigonometric degree at most 1, and distinct qubits
never couple. Certiﬁcate cert01 veriﬁes ( 4) identically over Q[i] against full 24-dimensional
statevector evolution across all 12 single-qubit and 27 two-qubit observables at nq = 4 ,L =
3.
3 Odd-Parity Mixer Collapse and Heisenberg Rzz Entangler
Leakage
Why did the no-circuit control M2 tanh(M1x) collapse ( α = 0 .0042–0.0056 on two of three
seeds; note that the non-trainable min-max rescaling buﬀers S,S−1 in Eq. (A1) of [ 1] are ﬁxed
constants, leaving gmix with zero trainable bias or even branch) on Layer 1, while turning oﬀ the
entanglers improved perplexity over trained entangled circuits? We prove two sharp algebraic
mechanisms acting in opposite directions.
Theorem 2 (Odd-Parity Collapse of Mixer-Only Controls and Exact Heisenberg Rzz Leakage
Laws).
(a) Odd-parity orthogonality of the no-circuit control: For any diagonals Λi,1,Λi,2, the mixer-
only map gmix(x) = M2 tanh(M1x) is strictly odd: gmix(−x) = −gmix(x) and gmix(0) = 0 .
Hence, for any centrally symmetric law P(x) = P(−x) and any target map f = feven+fodd,
where feven(x) = 1
2 (f(x) + f(−x)) includes all biases and even/quadratic terms,
Ex∼P
[
⟨gmix(x),feven(x)⟩
]
= 0 , Ex∼P
[
∥f(x) − gmix(x)∥2
2
]
≥ Ex∼P
[
∥feven(x)∥2
2
]
(5)
3

--- Page 4 ---
(Lean thm06–thm07, Certiﬁcate cert03). By contrast, even a single unentangled dense-
angle-encoded qubit generates nonzero bias ( I terms and ⟨Z⟩|x=0 = 1 ) and even cosine
modes cos(ax).
(b) Exact single-layer Heisenberg Rzz leakage laws: Let Uent = ∏nq−1
j=1 exp(−iγj
2 ZjZj+1) be
the open-chain entangler on nq ≥ 4 qubits, and deﬁne the unmeasured leakage fraction
of any Pauli string P as L(P) := ∑
wt(Q)≥3 c2
Q, where U†
entPUent = ∑
Q cQQ (∑
Q c2
Q =
1). Every operator in the open-chain local 1- and 2-qubit readout pool (i.e., excluding
wraparound ring pairs P1Qnq ) satisﬁes the exact closed-form leakage law (Lean thm08–
thm11, Certiﬁcates cert04–cert05):
L(Zq) = L(ZqZq+1) = L(X1) = L(Y1) = L(Xnq ) = L(Ynq ) = 0 , (6)
L(X1Z2) = L(Y1Z2) = L(Znq−1Xnq ) = L(Znq−1Ynq ) = 0 , (7)
L(Xq) = L(Yq) = sin 2 γq−1 sin2 γq (2 ≤ q≤ nq − 1), (8)
L(XqZq+1) = L(YqZq+1) = sin 2 γq−1 cos2 γq (2 ≤ q≤ nq − 1), (9)
L(ZqXq+1) = L(ZqYq+1) = cos 2 γq sin2 γq+1 (1 ≤ q≤ nq − 2), (10)
L(AqBq+1) = 1 − cos2 γq−1 cos2 γq+1
(
A,B ∈ {X,Y }, 2 ≤ q≤ nq − 2
)
, (11)
with boundary transverse bonds ( q = 1 or q = nq − 1) obeying L(A1B2) = sin 2 γ2 and
L(Anq−1Bnq ) = sin 2 γnq−2. In particular, at γj = π/2, every interior {X,Y }q and
{X,Y }q{X,Y }q+1 suﬀers 100% single-layer extinction out of the local readout pool (Cer-
tiﬁcate cert06).
(c) Operator-space census at nq = 8 : On nq = 8 qubits, the 12nq = 96 non-identity ring-pool
operators span only 96/65,535 = 0 .1465% of the Pauli space ( 21,813/21,845 = 99 .8535%
unmeasured; Lean thm12, Certiﬁcate cert07). Under independent uniform random an-
gles γj ∼ U[−π,π] (E[cos2 γj] = E[sin2 γj] = 1 /2), the exact expected single-layer leakage
summed across all 87 open-chain non-identity pool operators is 28 (28/87 = 32 .18% mean
loss, reaching 75% on all 20 interior transverse 2-qubit operators; Lean thm13, Certiﬁ-
cate cert08). Across L= 4 independent entangler steps, the iterated direct-channel (un-
mixed transverse) survival factor (cos2 γq−1 cos2 γq+1)L—neglecting single-qubit Z-branching
and weight- ≥ 3 →≤ 2 back-scattering (note that without interleaved single-qubit rotations,
commuting Rzz angles add coherently)—decays to (1/4)4 = 1 /256 < 0.4% at cos2 γ =
1/2, whereas small-angle initialization ( cos2 γ = 99 /100) preserves (99/100)8 > 92%
(Lean thm20, Certiﬁcate cert09).
Proof. For (a), since M1,M2 are linear and tanh is odd, gmix(−x) = −gmix(x). Pairing ±x
cancels ⟨gmix(x),feven(x)⟩+ ⟨gmix(−x),feven(−x)⟩= 0 (Lean thm06) and yields
∥f(x)− gmix(x)∥2
2 +∥f(−x)− gmix(−x)∥2
2 = 2 ∥feven(x)∥2
2 + 2∥fodd(x)− gmix(x)∥2
2 ≥ 2∥feven(x)∥2
2
(Lean thm07).
For (b), all Rzz (γj) commute pairwise, and a gate Rzz (γj) acts nontrivially on P iﬀ ZjZj+1
anticommutes with P. For an interior Xq (2 ≤ q ≤ nq − 1), only Rzz (γq−1) and Rzz (γq)
anticommute with Xq, yielding
U†
entXqUent = cq−1cqXq − sq−1cqZq−1Yq − cq−1sqYqZq+1 − sq−1sqZq−1XqZq+1,
where cj = cos γj, sj = sin γj. The unique weight- ≥ 3 term is −sq−1sqZq−1XqZq+1, prov-
ing ( 8) (Lean thm08–thm09). For XqZq+1 (q ≥ 2), Rzz (γq) maps XqZq+1 ↦→cqXqZq+1 − sqYq;
then Rzz (γq−1) yields cq−1cqXqZq+1 − cq−1sqYq − sq−1cqZq−1YqZq+1 − sq−1sqZq−1Xq, whose
unique weight- 3 term has squared amplitude s2
q−1c2
q, proving ( 9) (Lean thm11), and symmetri-
cally (10). For interior AqBq+1 (A,B ∈ {X,Y }, 2 ≤ q≤ nq − 2), ZqZq+1 commutes with AqBq+1
4

--- Page 5 ---
Figure 1: Exact Heisenberg-picture Rzz entangler leakage (Theorem 2). (a) Single-layer
Hilbert–Schmidt norm leaked into unmeasured weight- ≥ 3 Pauli strings as a function of uniform
entangler angle γ ∈ [0,π/2] across all operator classes. (b) Exact uniform-random leakage census
across all 87 open-chain non-identity local pool observables at nq = 8 , totaling 28/87 = 32 .2%
single-layer loss ( 75% on interior transverse 2-qubit operators; Certiﬁcate cert08).
(two anticommutations), while both exterior bonds Zq−1Zq and Zq+1Zq+2 anticommute with
it; expanding yields one weight- 2 term ( cq−1cq+1AqBq+1), two weight- 3 terms ( sq−1cq+1 and
cq−1sq+1), and one weight- 4 term ( sq−1sq+1), proving ( 11) (Lean thm10). Certiﬁcates cert04–
cert05 verify all 12+27 = 39 formulas identically via exact 16×16 unitary conjugation over Q[i].
Summing expected leakages under E[c2
j ] = E[s2
j ] = 1 /2 across the 87 open-chain non-identity
pool operators at nq = 8 gives 12(1
4 ) + 24( 1
4 ) + 8( 1
2 ) + 20( 3
4 ) = 28 (Lean thm13).
4 Token-Mixing Impossibility Barrier and Readout Parameter
Dominance
Every transformer block replaced in [ 1] applies causal self-attention across the token sequence
X = ( x1,...,x T ) ∈ RT ×D followed by a mixture-of-experts feed-forward network. By contrast,
the multi-head QNN ( 1) is strictly position-wise: yt = xt + αgΘ(xt) depends solely on xt
(∂yt/∂xs ≡ 0 for all s̸= t).
Theorem 3 (Position-Wise Token-Mixing Barrier and Classical Readout Dominance) .
(a) Exact conditional-variance token-mixing barrier: Let Ft(X) ∈ RD be the target output at
sequence position t of any transformer block (or contiguous N-block span) evaluated on a
random token sequence X = ( x1,...,x T ). For every measurable position-wise surrogate
g: RD → RD (quantum or classical, arbitrarily expressive),
E
[
∥Ft(X) − g(xt)∥2
2
]
= E
[
∥Ft(X) − E[Ft(X) |xt]∥2
2
]
+ E
[
∥E[Ft(X) |xt] − g(xt)∥2
2
]
≥ E
[
Var(Ft(X) |xt)
]
, (12)
with strict positivity whenever Ft(X) depends nontrivially on any earlier token xs (s<t )
(Lean thm14–thm15, Certiﬁcate cert11).
(b) Universal readout parameter dominance: In the multi-head QNN architecture with dh =
2nqL, D= kdh, and m= dh, the classical block-diagonal readout W(j) carries Pread = kd2
h
5

--- Page 6 ---
Figure 2: Direct-channel multi-layer attenuation and exact statevector local purity
collapse. (a) Iterated direct-channel (unmixed transverse) survival factor (cos4 γ)L across L=
1,..., 4 independent entangler steps (neglecting Z-branching and back-scattering): random/ π/4
angles decay to 1/256 (0.39%) at L = 4 , whereas small-angle initialization retains > 92%
(Certiﬁcate cert09). (b) Exact nq = 4 ,L = 2 statevector simulation over Q[i] conﬁrming strict
monotonic collapse of single-qubit Bloch purity ∑
q ∥rq∥2
2 from 4.00 (γ = 0 ) as entangler strength
increases (Certiﬁcate cert10).
Table 1: Uniﬁed algebraic resolution of the empirical anomalies in Amoussou et al. [ 1] (Certiﬁ-
cates cert01–cert15).
Empirical observation in [ 1] Exact algebraic mechanism Certiﬁed witness
No-circuit control collapses ( α→ 0.004) Odd-parity orthogonality (Thm 2(a)) ⟨gmix, feven⟩= 0 (cert03)
Entangler-oﬀ ( γ = 0 ) beats full QNN Zero leakage + SO(3) surrogate (Thm 1) 0% loss vs. 32.2%–75% (cert08)
Small-angle frozen beats full QNN Small γ ⇒ > 92% survival + readout 131,072/145,281 (cert02,09)
LAMBADA / scattered degradation Position-wise Var(Ft |xt) ﬂoor (Thm 3(a)) Irreducible MSE = w2 (cert11)
IBM Heron ( 156 q) execution 14/14/4 packing, 3 submits/tok, 0 swaps 392 Rzz /group ( cert15)
trainable parameters while all remaining components (mixers M1,M2, aﬃne encodings, Rx,
Rzz , and α) carry Pnon = 4 D+ (6nq − 1)Lk+ 1. For every nq,L,k ≥ 1 with dh ≥ 14,
Pread ≥ 2 Pnon =⇒ Pread
Pread + Pnon
≥ 2
3 (13)
(Lean thm16, Certiﬁcate cert12). At Qwen3-30B’s instantiation ( nq = 8 ,L = 4 ,k =
32,dh = 64 ), Pread = 131 ,072 out of 145,281 (90.22%; Lean thm05), while the two
Sylvester–Hadamard mixers compress dense 2048 × 2048 projections by an exact factor
of 1,024× (8,192 vs. 8,388,608; Lean thm17, Certiﬁcate cert13).
Proof. Part (a) is the conditional-expectation Pythagorean theorem: writing Ft − g(xt) = ( Ft −
µ(xt))+(µ(xt)−g(xt)) with µ(xt) := E[Ft(X) |xt], the cross term vanishes by the tower property
E[⟨Ft − µ(xt),µ(xt)− g(xt)⟩] = E[⟨E[Ft − µ(xt) |xt],µ(xt)− g(xt)⟩] = 0 (formalized algebraically
over equiprobable context pairs in Lean thm14–thm15, and veriﬁed on an exact causal attention
map with attention weight w yielding ﬂoor w2 in Certiﬁcate cert11). For (b), since Lk ≥ 1,
(nq − 1)Lk+1 ≤ nqLk, so Pnon = 8 nqLk+4nqLk+nqLk+(nq − 1)Lk+1 ≤ 14nqLk; multiplying
by 2 gives 2Pnon ≤ 14(2nqL)k= 14 dhk≤ d2
hk= Pread whenever dh ≥ 14 (Lean thm16).
Remark 1 (Design Prescriptions for Future Hybrid Quantum–Classical Transformers) . Theo-
rems 1–3 immediately prescribe three architectural ﬁxes for any successor to [ 1]: (1) retain
self-attention and replace only the position-wise MoE feed-forward sublayer ( 97% of block pa-
rameters, zero token-mixing barrier); (2) include an explicit bias/even branch in any classical
6

--- Page 7 ---
Figure 3: Readout dominance and position-wise token-mixing barrier (Theorem 3).
(a) Classical readout share Pread/Ptot vs. head width dh = 2 nqL, crossing 2/3 at dh = 14 and
reaching 90.22% in Qwen3-30B (Certiﬁcate cert12). (b) Irreducible position-wise MSE ﬂoor
Var(Ft |xt) = w2 for causal attention weight w (Certiﬁcate cert11).
mixer baseline so ablations separate parity eﬀects from circuit expressivity; and (3) either match
higher-weight Pauli readouts to the lightcone of Uent, or benchmark directly against the O(nqL)
classical Bloch surrogate of Theorem 1, which eliminates 2nq statevector simulation while match-
ing the entangler-oﬀ control identically.
5 Formal Veriﬁcation Architecture and Scope
• Layer 1 — Lean 4.36.0 Kernel (lean/MultiHeadQnnTheory.lean): Twenty con-
structive theorems compiled with -DwarningAsError=true, zero external imports, zero
sorry, zero grind, zero Classical.choice, and zero custom axioms (audited via #print
axioms). Layer 1 formalizes Pythagorean rational SO(3) norm conservation ( thm01–
thm03), nq = 8 state compression and Table I parameter accounting ( thm04–thm05), odd-
even orthogonality and Pythagorean MSE ﬂoors ( thm06–thm07), exact Hilbert–Schmidt
conservation and weight- ≥ 3 leakage identities for interior 1-qubit, mixed 2-qubit, and
transverse 2-qubit observables (thm08–thm11), nq = 8 unmeasured Pauli-space and uniform-
random leakage arithmetic ( thm12–thm13), the two-context token-mixing Pythagorean
barrier ( thm14–thm15), universal readout dominance for all dh ≥ 14 (thm16), Hadamard
mixer compression, Qwen3-30B block-fusion compression, IBM Heron packing, and L= 4
multi-layer survival gaps ( thm17–thm20). The continuous SU(2) → SO(3) double-cover
homomorphism, general- nq Pauli commutator algebra, and tower-property proof of ( 12)
are proved in full in Sections 2–4 and independently veriﬁed on ﬁnite multi-qubit registers
in Layer 2.
• Layer 2 — Zero-Float Q[i] Veriﬁer (verification/verify_multihead_qnn.py): An
AST-audited pure standard-library veriﬁer using strictly int and Fraction over Q[i] (zero
ﬂoats, zero numeric /, zero **, zero limit_denominator), emitting 16 SHA-256 certiﬁ-
cates in certificates/MANIFEST.json and validated by 56 adversarial pytest checks
in tests/test_adversarial.py. Layer 2 runs full 24-dimensional statevector simulation
over Q[i] to verify exact identity with the O(nqL) Bloch surrogate across 39 observables
(cert01), performs exact 16 × 16 unitary Heisenberg conjugation for all 12 single-qubit
and 27 nearest-neighbor two-qubit Paulis ( cert04–cert05), certiﬁes >99.999% near-π/2
extinction (cert06) and multi-layer Bloch purity collapse ( cert10), and checks all Qwen3-
7

--- Page 8 ---
30B/IBM Heron tables ( cert02, cert07–cert15).
References
[1] M. Amoussou, B. Aizpurua, S. Singh, R. Orús, and H.-A. Jacobsen, Multi-head quan-
tum neural networks: Replacing transformer blocks with NISQ modules inside a 30-billion-
parameter LLM, preprint arXiv:2611.15250v1, November 2026.
[2] M. Cerezo, G. Verdon, H.-Y. Huang, L. Cincio, and P. J. Coles, Challenges and opportuni-
ties in quantum machine learning , Nature Comput. Sci. 2 (2022), 567–576.
[3] M. Cerezo, M. Larocca, D. García-Martín, N. L. Diaz, P. Braccia, E. Fontana,
M. S. Rudolph, P. Bermejo, A. Ijaz, S. Thanasilp, E. R. Anschuetz, and Z. Holmes,
Does provable absence of barren plateaus imply classical simulability? , Nature Commun.
16 (2025), 7907.
[4] R. LaRose and B. Coyle, Robust data encodings for quantum classiﬁers , Phys. Rev. A 102
(2020), 032420.
[5] M. Larocca, S. Thanasilp, S. Wang, K. Sharma, J. Biamonte, P. J. Coles, L. Cincio,
J. R. McClean, Z. Holmes, and M. Cerezo, Barren plateaus in variational quantum com-
puting, Nature Rev. Phys. 7 (2025), 174–189.
[6] M. Schuld, R. Sweke, and J. J. Meyer, Eﬀect of data encoding on the expressive power of
variational quantum-machine-learning models , Phys. Rev. A 103 (2021), 032430.
[7] V. V. Shende, S. S. Bullock, and I. L. Markov, Synthesis of quantum-logic circuits , IEEE
Trans. Comput.-Aided Design Integr. Circuits Syst. 25 (2006), 1000–1010.
[8] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and
I. Polosukhin, Attention is all you need , in Advances in Neural Information Processing
Systems (NeurIPS) , Vol. 30, 2017.
8
