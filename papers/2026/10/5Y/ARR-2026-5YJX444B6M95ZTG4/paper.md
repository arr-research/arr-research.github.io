# Classical capacities and complementary simulation for qubit Davies channels

Extracted text; the canonical PDF controls mathematical notation.

Classical capacities and complementary simulation
for qubit Davies channels
Lluis Eriksson
17 October 2026 — Working paper
Abstract
We extend the thermal block entropy estimate for generalized amplitude damping to the full
qubit Davies region, including additional dephasing. The proof combines the triangular inequality
of Tang, Zhu, Bai and Wang with a controlled-puriﬁcation consequence of strong subadditivity:
a third vertex completes the ﬁxed-entropy decomposition used for the thermal boundary. The
resulting population-resolved bound holds with every ﬁnite-dimensional partner. It implies strong
superadditivity of the convex roof of output entropy, and hence arbitrary-partner additivity of
Holevo information and classical capacity for both the Davies channel and its complementary
channel. We give scalar convex-envelope formulas for both capacities. Every bipartite state sup-
ported on the two-dimensional Stinespring range has strongly additive entanglement of formation,
so its state entanglement cost requires no regularization. A scalar moment program evaluates that
formation functional for arbitrary input coherence. The state/channel correspondence, comple-
ment duality and existing axial convex-roof geometry are explicitly attributed to prior work. A
normalized reverse channel stays within the Davies region, allowing us also to remove regulariza-
tion from the parallel entanglement cost of the complementary channel. We obtain an elementary
rate in a known ﬂat-roof region and exhibit a nonunital example whose simulation cost strictly
exceeds the cost of its Choi state. Finite-block and numerical bounds support the results. The tri-
angular theorem remains an external dependency; the original channel’s simulation cost, adaptive
simulation and quantum capacity are not determined.
1 Channel family, antecedents and result
A qubit can relax toward a thermal population while its coherence decays faster than relaxation
alone requires. Write the corresponding channel as
Φa,b,λ
1 − p z
¯z p

=
1 − t(p) λz
λ¯z t (p)

, t (p) = a+ kp, k = 1 − a− b, (1)
where
a,b ≥ 0, a + b≤ 1, 0 ≤ λ2 ≤ k, λ ≥ 0. (2)
A ﬁxed phase of the coherence multiplier can be removed by an output unitary. The map is completely
positive: it is generalized amplitude damping followed by dephasing with multiplier λ/
√
k when
k> 0. The limiting case k= 0 is a constant diagonal-output channel.
The region ( 2) is the closure of the usual dissipative qubit Davies family, allowing degenerate
limits and exchange of the energy labels. Roga, Fannes and Życzkowski characterized these maps
and their single-use minimum output entropy [ 1]. At ﬁnite positive relaxation times their parameters
satisfy
k= e−t/T1 , λ = e−t/T2 , T 2 ≤ 2T1.
1

Here tin the exponents is time, whereas t(p) in ( 1) is an output population. We use ( 1) as the math-
ematical deﬁnition throughout. General phase-covariant qubit channels allow the larger complete-
positivity region λ2 ≤ k+ ab; that entire region is not claimed here.
The proof builds on two recent results. Tang et al. established strong additivity for qubit channels
admitting a pure output, using a triangular block entropy inequality [ 2]. OpenAI extended that
inequality to the thermal equality case and obtained strong additivity for generalized amplitude
damping [ 3]. In our parameters that boundary is λ2 = k. We add a third vertex to their ﬁxed-
entropy decomposition, proving the inequality for λ2 < kas well. The new vertex follows directly
from strong subadditivity, and is not a new entropy axiom. The scalar convex envelope is necessary
because extra dephasing need not preserve convexity of the pure-output entropy.
Several overlaps are already understood: unital qubit channels [ 5], entanglement-breaking chan-
nels [ 6], and the pure-output boundary [ 2]. Earlier work treated approximate Holevo additivity
for damping combined with dephasing [ 7]; its ordinary damping examples now also fall within the
pure-output theorem. Our contribution is the stated block extension and its additivity consequences
across the thermal interior. Roga explicitly listed Davies capacity additivity as open in 2011 [ 11,
Section 6, p. 78]; this historical statement is not a certiﬁcate of present priority. We do not claim a
new description of Davies dynamics or a new single-qubit minimum-entropy optimization. The state
formation and complementary-channel consequences below use the established Matsumoto–Shimono–
Winter correspondence [ 12], complement duality [ 15], and the regularized formation characterization
of state cost [ 13]. Hellmund and Uhlmann already analyzed the axial one-use convex roofs [ 16]; the
new operational step is the stated strong additivity, not rediscovery of those roofs.
The simulation result concerns the complementary channel and the parallel diamond-norm task
of Berta et al. [ 19]. Wilde already determined the cost of epolarizing channels, the complements of
depolarizing channels, even under sequential tests [ 20, Section IV.D]. More generally, the unital qubit
case is covered by the unital additivity and covariant channel/state machinery [ 5, 12, 20]. We do not
claim these cases as new. The additional nonunital region is useful precisely because the optimizing
reference input need not be a Bell pair; Section 6 gives an exact example. The scalar roof and the
parallel simulation theorem are antecedents; closure of the explicit reverse parameters lets us apply
the Davies range theorem to this diﬀerent bipartition.
All spaces below are ﬁnite dimensional. Let S(ρ) = −Trρln ρ be entropy in nats and put
h(p) = −pln p− (1 − p) ln(1 − p), g (u) = h
1 + √1 − 4u
2

.
Zero terms are interpreted by continuity. Deﬁne
v(p) = t(p)(1 − t(p)) − λ2p(1 − p), e (p) = g(v(p)), f = co e, (3)
where co e is the largest convex function below e on [0,1].
For a channel N, χ(N) denotes the maximum ensemble Holevo information in bits, Smin(N) =
minρS(N(ρ)), and
C(N) = sup
n≥1
1
nχ(N⊗n)
is its unassisted memoryless classical capacity, with arbitrary entangled block encodings and collective
output measurements [ 8, 9]. No preshared entanglement or feedback is assumed.
Theorem 1. For every channel Φ = Φ a,b,λ satisfying (2),
C(Φ) = χ(Φ) = 1
ln 2 max
0≤p≤1
{h(a+ kp) − f(p)}. (4)
2

An ensemble with at most four pure signals, consisting of at most two equally weighted opposite-phase
pairs within their respective populations, attains the one-use maximum. For every ﬁnite-dimensional
channel N,
χ(Φ ⊗ N ) = χ(Φ) + χ(N), (5)
Smin(Φ ⊗ N ) = min
p
e(p) + Smin(N), (6)
C(Φ ⊗ N ) = χ(Φ) + C(N). (7)
In particular χ(Φ⊗n) = nχ(Φ) for every n.
Theorem 1 states unrestricted Holevo additivity. The stronger ﬁxed-marginal convex-roof state-
ment is proved in Section 4. The partner’s classical capacity retains its regularization; we do not
replace C(N) by χ(N). Formula ( 4) is a scalar convex-envelope optimization, not a claimed elemen-
tary closed form.
2 The block entropy extension
We ﬁrst state precisely the external inequality used in the proof.
Lemma 2(Triangular entropy inequality, Tang et al.) . Let A,B,C have the same ﬁnite rectangular
shape, with squared Hilbert–Schmidt norms x,y,z summing to one. Then
S
A B
C 0
A B
C 0
∗
≥ xS(AA∗/x) + yS(BB∗/y) + zS(CC∗/z) + g(yz).
A zero-weight term is omitted.
This is the same-shape rectangular case of [ 2, Theorem 4.2], after permutation of block rows, also
stated and proved in [ 3, Theorem 2.1]. We invoke that result; it is not proved anew or attributed to
this paper.
The additional vertex uses only data processing for conditional entropy. Its two-label case also
follows from Amosov’s phase-damping estimate [ 10, Proposition 5], with partial trace as the partner
channel. We give the short puriﬁcation proof to ﬁx the direction of the entropy inequality; the vertex
estimate itself is not claimed as new.
Lemma 3(Controlled puriﬁcations). Let ρ= ( ρij) be a density matrix and let Xi be matrices of the
same shape with TrXiX∗
i = 1 . Then
S
0
@X
ij
ρij|i⟩⟨j| ⊗ XiX∗
j
1
A≥ S(ρ) +
X
i
ρiiS(XiX∗
i).
Proof. Vectorize Xi as a normalized vector |Xi⟩BE. The map V|i⟩ = |i⟩A|Xi⟩BE is an isometry. Thus
Ω = VρV ∗ has S(ABE)Ω = S(ρ), and its AB marginal is the matrix in the statement. Dephase A,
obtaining Ω′. Strong subadditivity implies that applying a channel to the conditioning system AB
cannot decrease S(E|AB) [4]. Consequently
S(AB)Ω − S(ABE)Ω ≥ S(AB)Ω′ − S(ABE)Ω′ .
The right side is P
iρiiS(XiX∗
i): the classical entropy of i cancels, and each conditional BE vector
is pure. Rearrangement proves the claim.
3

Theorem 4 (Thermal inequality with additional dephasing) . Let X,Y ∈ Cd×r satisfy TrXX∗ =
TrYY ∗ = 1 . Let α,β,η,δ,K ≥ 0 satisfy
α+ β+ η+ δ= 1 , αδ − βη ≥ K2.
For
T =
αXX∗ + βYY ∗ KXY ∗
KYX ∗ ηXX∗ + δYY ∗

, U 0 = α+ β, U 1 = η+ δ, u = U0U1 − K2,
one has
S(T) ≥ (α+ η)S(XX∗) + ( β+ δ)S(YY ∗) + g(u). (8)
Proof. The assumptions ensure positivity of T: its coherent part with diagonal blocks αXX∗,δYY ∗
is positive because αδ≥ K2, and the remaining diagonal blocks are positive.
Assume ﬁrst U0U1 >0 and u> 0. With U0,U1,K ﬁxed, the constraint becomes
βU1 + ηU0 ≤ u.
In the coeﬃcient order (α,β,η,δ ) the feasible triangle has vertices
A= ( K2/U1,u/U1,0,U1),
B = ( U0,0,u/U0,K2/U0),
C = ( U0,0,0,U1).
The original point has respective weights
wA = βU1/u, w B = ηU0/u, w C = 1 − wA − wB.
They are nonnegative. Each vertex retains the same row masses and oﬀ-diagonal scalar K, hence
the same u.
At A, write
TA = MAM∗
A, M A =
√αX √βY√
δY 0

.
Here
√
αδ= K and βδ = u, so Lemma 2 gives ( 8) at this vertex. At B use
MB =
√U0X 0√
δY √ηX

.
It satisﬁes MBM∗
B = TB; interchange its block rows to apply the triangular lemma, with corner-mass
product U0η= u.
At C, apply Lemma 3 to ρ=
 U0 K
K U1

and the pair X,Y . The scalar state has determinant uand
entropy g(u), giving the desired bound. Finally, entropy concavity applied to T = wATA + wBTB +
wCTC preserves g(u) and the aﬃne weights of the two block entropies.
If a row mass vanishes, K = 0 and the result is ordinary entropy concavity in the remaining
block. If u= 0 and both row masses are positive, the constraint forces β = η= 0 ; Lemma 3 applies
with a pure ρ. This also establishes all boundaries.
The estimate is sharp for every allowed scalar coeﬃcient tuple: setting X = Y gives T = ρ⊗XX∗,
so equality holds. The equality boundary αδ− βη = K2 is exactly the two-vertex thermal argument
in [ 3, Theorem 3.1]; the third vertex is needed to cover the inequality region.
4

3 Population-resolved bound and capacity
Lemma 5. Let N be any ﬁnite-dimensional channel and |ψ⟩ = √1 − p|0⟩|ψ0⟩ + √p|1⟩|ψ1⟩, where
the nonzero branches are normalized. Then
S((Φ ⊗ N )(ψ)) ≥ e(p) + (1 − p)S(N(ψ0)) + pS(N(ψ1)). (9)
No orthogonality of the conditional vectors is required.
Proof. For Kraus operators Lj of N, form the matrices with columns Xj = Ljψ0 and Yj = Ljψ1.
Their squared Hilbert–Schmidt norms are one. The output has the form in Theorem 4, with
α= (1 − p)(1 − a), β = pb, η = (1 − p)a, δ = p(1 − b), K = λ
p
p(1 − p).
Here αδ− βη = kp(1 − p) ≥ K2, α+ η = 1 − p, and u = v(p). Apply ( 8). At p = 0 ,1 only one
product branch remains and the formula follows directly.
For clarity, the convex envelope can be written as
f(p) = min
0≤q,r,s≤1
(1−s)q+sr=p
{(1 − s)e(q) + se(r)}. (10)
Indeed the minimum of
R
edµ over probability measures with mean p is attained by compactness.
This minimum is the lower convex envelope. An extreme minimizing measure has at most two support
points: weights on three distinct support points admit a nonzero signed perturbation preserving total
mass and mean. Equivalently, each lower supporting line of the convex hull of the graph needs at
most two contact points. Continuity of e includes endpoint and one-point cases.
Proof of Theorem 1. Reﬁning any signal ensemble into pure states does not decrease its Holevo
information. A pure qubit with population phas output entropy e(p), independently of its phase. If
an ensemble has mean population ¯p, dephasing its average output increases entropy, and convexity
of f ≤ e gives
(ln 2)χ(ensemble) ≤ h(a+ k¯p) −
X
ℓ
wℓe(pℓ) ≤ h(a+ k¯p) − f(¯p).
Conversely choose q,r,s attaining ( 10). At population quse √1 − q|0⟩± √q|1⟩, each with probability
(1 −s)/2; at population r use the analogous pair, each with probability s/2. The average is diagonal
with population p, and the average output entropy is f(p). Maximizing over p proves the single-use
formula and the four-signal bound.
For a pure ensemble {wℓ,ψℓ} on the input of Φ ⊗ N , apply Lemma 5 to every signal. The
branch outputs of N with probabilities wℓ(1 −pℓ),wℓpℓ form a valid ensemble. Its average is exactly
the second output marginal ¯ωB. Subadditivity bounds the entropy of the full average output by
h(a+ k¯p) + S(¯ωB). Subtracting the average of ( 9) yields
(ln 2)χ(joint ensemble ) ≤ h(a+ k¯p) − f(¯p) + (ln 2) χ(N).
The single-use formula and product ensembles prove ( 5). The same one-step inequality bounds every
pure output entropy below by minpe(p) + Smin(N); entropy concavity handles mixed inputs, and
products attain the bound. This proves ( 6).
Iteration of ( 5) gives χ(Φ⊗n⊗ N⊗n) = nχ(Φ) + χ(N⊗n). Taking the regularized capacity proves
(7), including C(Φ) = χ(Φ).
5

4 Entanglement formation in the dilation range
For any ﬁnite channel M deﬁne its convex roof of output entropy, in nats, by
bSM(ρ) = min
ρ=∑
j wj ψj
X
j
wjS(M(ψj)),
where the ψj are pure states. If V : C2 → B⊗ E is a Stinespring isometry of Φ, then
FΦ(σ) := bSΦ(σ) = EF(VσV ∗). (11)
Here EF denotes bipartite state entanglement of formation in nats. Equation ( 11) is the standard
channel/state correspondence [ 12]. Each pure component of a state supported on ran V lies in that
range and therefore pulls back to a pure qubit; this also gives a direct proof of the equality.
An elementary observation strengthens the population argument. Every qubit state σ=
 1−p z
¯z p

is a mixture of pure states with the same population p: two opposite phases, with suitably unequal
weights, realize every |z| ≤
p
p(1 − p). Their output entropies are all e(p). Thus
f(p) ≤ FΦ(σ) ≤ e(p). (12)
The upper bound, rather than equality with f, is what is needed next.
Theorem 6(Strong convex-roof superadditivity) . For every ﬁnite-dimensional channel N and every
joint input state ρAA′ ,
bSΦ⊗N (ρ) ≥ bSΦ(ρA) + bSN (ρA′ ). (13)
The same assertion holds with Φ replaced by any complementary channel Φc.
Proof. For a pure ρ = ψ, Lemma 5 bounds its output entropy by e(p) plus the average output
entropies of the conditional A′ branches. By ( 12), the ﬁrst term is at least bSΦ(ψA). Those branches
decompose ψA′ , so their average is at least bSN (ψA′ ). For mixed ρ, apply this to a minimizing pure
decomposition and use convexity of both marginal roofs.
For the complement, let Nc be a complementary channel to N. For pure ψ, purity of the complete
Stinespring output gives
S((Φc ⊗ N )(ψ)) = S((Φ ⊗ N c)(ψ)).
Apply Lemma 5 to the right side. Its conditional branches are pure, so S(Nc(ψj)) = S(N(ψj)). Thus
the same one-step inequality holds for Φc. Its pure-output entropy is again e(p), and the preceding
argument applies. This use of complement duality is standard [ 14, Theorem 1, equations (6) and
(9)]; see also [ 15].
For a ﬁxed input σ, the maximal ensemble Holevo information is (S(M(σ)) − bSM(σ))/ln 2.
Subadditivity of the mean output entropy and ( 13) therefore give its subadditivity at arbitrary joint
input marginals, with equality at product input states. This is stronger than the unconstrained
maximum in Theorem 1; it uses the established convex-roof framework of [ 12], not an equivalence
asserted without its needed hypotheses.
Corollary 7(State entanglement cost) . Let ω= VσV ∗. For every ﬁnite-dimensional bipartite state
ΩBB′EE′ with ΩBE = ω,
EF(ΩBB′:EE′ ) ≥ EF(ωB:E) + EF(ΩB′:E′ ).
6

Consequently, for every ﬁnite bipartite state τ,
EF(ω⊗ τ) = EF(ω) + EF(τ),
EC(ω) = FΦ(σ)/ln 2,
EC(ω⊗ τ) = FΦ(σ)/ln 2 + EC(τ).
Here EC is asymptotic LOCC state entanglement cost in ebits.
Proof. Positivity and the support of the ﬁrst marginal imply that Ω is supported on ran V ⊗B′ ⊗E′.
Lift it through V and use Theorem 6 with N = TrE′ . The three roofs are exactly the three formation
quantities displayed. For product states, product pure decompositions attain the reverse inequality.
Iteration gives EF(ω⊗n) = nEF(ω), and more generally EF(ω⊗n⊗ τ⊗n) = nEF(ω) + EF(τ⊗n). The
state-cost theorem EC(ρ) = lim nEF(ρ⊗n)/(nln 2) [13] proves both cost statements.
These are states in a Stinespring range, not generally Choi states. The result does not evaluate
entanglement cost for simulating the channel. At the GAD boundary the same corollary follows
from OpenAI’s one-step inequality and the standard correspondence; our block extension supplies
the remaining Davies region.
For completeness the required one-use formation functional has a scalar moment description. This
is a convenient version of the known axial convex-roof problem [ 16], not a claim that its geometry is
new.
Proposition 8. With r(q) =
p
q(1 − q) and σ=
 1−p z
¯z p

,
FΦ(σ) = min
µ
Z
e(q) dµ(q) :
Z
qdµ = p,
Z
r(q) dµ≥ |z|

, (14)
where µ ranges over probability measures on [0,1]. In particular FΦ(diag(1 − p,p)) = f(p).
Proof. A pure decomposition of σ induces a population measure; the triangle inequality for its
coherences gives the moment constraint. Conversely, given such a measure, put R =
R
rdµ. At
every population choose the same average phase factor z/R, with the sign convention matching the
upper-right matrix entry. Two opposite phases with probabilities (1 + |z|/R)/2,(1 − |z|/R)/2 realize
that factor and leave the entropy integral unchanged. If R= 0 , necessarily z = 0 and the endpoint
mixture suﬃces. Compactness gives a minimizing measure. An extreme minimizer can have at most
three populations: four supported pieces admit a nonzero signed weight perturbation preserving
normalization, the population moment and the radius moment. This also supplies a ﬁnite ensemble.
For z= 0 the constraint is vacuous, reducing the program to the convex envelope.
Formula ( 14) is an optimization formula, not an elementary closed form. For example, the
suﬃcient condition D ≥ 0, 4AD ≥ B2, with v(q) = A+ Bq + Dq2, makes e convex and then
FΦ(σ) = e(p) for every coherence. This is the ﬂat-roof regime already identiﬁed by Hellmund and
Uhlmann [ 16, Theorem 2 and Sections IV.C–D]. One quick veriﬁcation is that √v is a norm of an
aﬃne two-vector under this condition, while g(x2) is convex and nondecreasing [ 17, 16]. We do not
claim this criterion or the ﬂat roof as new. Outside that regime, ( 14) retains the coherence constraint
even though additivity still holds.
5 Classical capacity of the complementary channel
The complementary output is the environment output of a pure Stinespring dilation, including
puriﬁcation of a mixed reservoir when necessary. It is not automatically the experimentally accessible
7

part of a thermal bath. Its minimal dimension is at most four. To compute its entropy at a diagonal
input, choose unit vectors u,v in an environment sector of dimension two, and orthogonal vectors
e+,e− orthogonal to that sector, with ⟨v,u⟩ = λ/
p
(1 − a)(1 − b). A dilation is
V|0⟩ =
√
1 − a|0⟩|u⟩ + √a|1⟩|e+⟩,
V|1⟩ =
√
b|0⟩|e−⟩ +
√
1 − b|1⟩|v⟩.
The positivity constraint makes the prescribed inner product feasible. If its denominator vanishes
then λ= 0 and the irrelevant overlap may be chosen arbitrarily. Tracing the environment gives ( 1).
For input diag(1 − p,p) the environment spectrum is
a(1 − p), bp, w(p) +
p
w(p)2 − 4d(p)
2 , w(p) −
p
w(p)2 − 4d(p)
2 , (15)
where
w(p) = (1 − a)(1 − p) + (1 − b)p, d (p) = p(1 − p)((1 − a)(1 − b) − λ2).
Indeed the remaining block is the mixture of |u⟩⟨u| and |v⟩⟨v| with the indicated trace and determi-
nant. Let HE(p) be the entropy in nats of the four probabilities in ( 15).
Theorem 9. For every qubit Davies channel in (2),
C(Φc) = χ(Φc) = 1
ln 2 max
0≤p≤1
{HE(p) − f(p)}.
At most two opposite-phase population pairs attain the one-use maximum. For every ﬁnite-
dimensional N,
χ(Φc ⊗ N ) = χ(Φc) + χ(N),
C(Φc ⊗ N ) = χ(Φc) + C(N),
Smin(Φc ⊗ N ) = min
p
e(p) + Smin(N).
Proof. For Uθ = diag(1 ,eiθ), let Wθ act as the identity on u,v and with phases e−iθ,eiθ on e+,e−.
Then VUθ = ( Uθ ⊗ Wθ)V. Hence Φc is phase covariant, and averaging the input phase cannot
decrease its output entropy. At mean population p that entropy is therefore at most HE(p), while
the mean pure-output entropy is at least f(p). The same opposite-phase ensemble used in Theorem 1
attains both bounds.
The proof of Theorem 6 established the full one-step inequality for Φc. Repeating the branch-
ensemble proof of Theorem 1, with HE replacing h ◦ t, gives the arbitrary-partner Holevo and
minimum-entropy identities. Regularization gives the capacity identity.
The function HE is concave, being entropy along an aﬃne family of states; therefore HE−f is con-
cave. A sampled lower hull fN gives the same one-sided discretization error as Proposition 14, since
only the error in f enters that argument. The limits provide useful checks: an identity channel has a
constant complement of capacity zero, whereas a constant qubit-output channel has complementary
capacity one bit.
8

6 Parallel simulation of the complementary channel
This section concerns the resources needed to simulate N = Φ c, with its full Stinespring output. Let
GM(σ) = EF((idR⊗M)(ψσ)), E ch
F (M) = max
σ
GM(σ),
where ψσ is a puriﬁcation and EF uses nats. Reference isometries do not aﬀect this deﬁnition. The
parallel simulation cost Epar
C is the asymptotic number of shared ebits per use required by LOCC
protocols whose simulated tensor-power channel converges in diamond norm; classical communication
is free. The theorem of Berta et al. gives
Epar
C (M) = lim
n→∞
Ech
F (M⊗n)
nln 2 . (16)
This operational theorem is external [ 19, Theorem 12]. Sequential or adaptive tests constitute a
diﬀerent task [ 20].
We recall two standard formation facts. The Kraus characterization is
GM(σ) = inf
{Lj }
X
j
Tr(LjσL∗
j)S
 
LjσL∗
j
Tr(LjσL∗
j)
!
,
with zero branches omitted. Pure-state ensemble decompositions of the puriﬁed output correspond
to Kraus representations; one ﬁrst argues on the support of σ and extends the representation or
takes continuous limits at singular inputs. For every ﬁxed representation the entropy perspective is
concave in σ. Its inﬁmum is concave as well: bound each component of a mixture by its own inﬁmum
before taking the inﬁmum over the common representation. Thus GM is concave. It is continuous
by continuity of ﬁnite-dimensional EF and of the canonical puriﬁcation constructed from √σ, so
a maximum exists. Covariance and local-unitary invariance then imply that GΦc has a diagonal
maximizer, by averaging the input phase.
The other fact is subadditivity of channel formation [ 2, Appendix C]:
Ech
F (M ⊗ L) ≤ Ech
F (M) + Ech
F (L). (17)
For completeness, choose Kraus decompositions optimal, or arbitrarily close to optimal, for the two
marginal input states of a joint puriﬁed input. Their product yields an admissible pure decompo-
sition of the joint output. For its classical Kraus labels I,J and quantum outputs B,B′, entropy
subadditivity and conditioning give
S(BB′|IJ) ≤ S(B|IJ) + S(B′|IJ) ≤ S(B|I) + S(B′|J).
Completeness of the other instrument makes each ﬁnal term the corresponding local Kraus objective.
Maximizing over inputs proves ( 17).
Theorem 10 (Complementary simulation) . For every Davies channel Φ in (2) and every ﬁnite
channel M,
Ech
F (Φc ⊗ M) = Ech
F (Φc) + Ech
F (M),
Epar
C (Φc) = Ech
F (Φc)/ln 2,
Epar
C (Φc ⊗ M) = Ech
F (Φc)/ln 2 + Epar
C (M).
9

An exact scalar formula is
Epar
C (Φc) = 1
ln 2 max
0≤p≤1
fp(t(p)), (18)
where fp is the lower convex envelope of the pure-output entropy for the reversed Davies parameters
ap = pb
1 − t, b p = (1 − p)a
t , k p = kp(1 − p)
t(1 − t) , λ 2
p = λ2p(1 − p)
t(1 − t) , t = t(p). (19)
Endpoint and constant pure-output exceptions are speciﬁed in the proof.
Proof. For 0 <p< 1 and 0 <t< 1, apply the dilation of Section 5 to half of √1 − p|00⟩ + √p|11⟩.
Grouping the resulting pure vector by its B output gives an isometry Wp from a qubit to RE:
Wp|0⟩ =
p
(1 − p)(1 − a)|0⟩|u⟩ + √pb|1⟩|e−⟩√1 − t ,
Wp|1⟩ =
p
(1 − p)a|0⟩|e+⟩ +
p
p(1 − b)|1⟩|v⟩√
t .
Its columns are orthonormal. Tracing E gives a qubit channel Ψp with parameters ( 19); in particular
1 − ap − bp = kp and 0 ≤ λ2
p ≤ kp. This is the key closure property. The reference–environment
output state is exactly
ωp = (id R⊗Φc)(ψp) = Wpdiag(1 − t,t)W∗
p.
Corollary 7 therefore gives strong formation additivity for ωp with every ﬁnite bipartite partner, and
GΦc (diag(1 − p,p)) = fp(t).
Choose a diagonal input maximizing GΦc and an optimizing puriﬁed input for M, with output
state τ. Product inputs, together with the established state additivity, give
Ech
F (Φc ⊗ M) ≥ EF(ωp ⊗ τ) = Ech
F (Φc) + Ech
F (M).
Equation ( 17) proves equality. Iteration and ( 16) prove both operational identities and ( 18).
At p = 0 ,1 the reference is pure and G = 0 ; a zero maximizing formation value also gives the
product lower bound by local discard. If t= 0 or 1 at an interior p, the original channel is constant
with pure output. Its complement is isometric, G(diag(1 −p,p)) = h(p) and its cost is one ebit. Pure
maximal entanglement gives its strong product lower bound. These cases deﬁne the missing values
of ( 18); all other boundary cases follow from the displayed construction or continuity.
This proof uses an optimizing reference–output state in a diﬀerent Stinespring range; complement
duality alone does not transfer simulation cost. The construction is the standard normalized reverse-
channel (weighted-transpose or Petz) construction [ 21], with its explicit Davies parameters veriﬁed
here. At the GAD boundary the same deduction uses the antecedent one-step inequality [ 3]. The
added dephasing and nonunital parameters are the extension.
Corollary 11 (An elementary rate) . Put x= λ2 and
c(a,b) = k+ 2ab− 2
p
ab(k+ ab).
If c(a,b) ≤ x≤ k, then
Epar
C (Φc) = h
1 + λ
2

/ln 2.
A Bell input maximizes channel formation in this region.
10

Proof. The threshold c is the known Hellmund–Uhlmann ﬂat-concurrence threshold, a suﬃcient
condition for the entropy roof used here [ 16, Equation (29) and Section V.B]. With L= p(1−p)/(t(1−
t)), the reverse parameters satisfy kp = Lk, apbp = Lab, λ2
p = Lx, and hence c(ap,bp) = Lc(a,b).
Their entropy roof is therefore ﬂat in the stated region. Direct substitution yields
fp(t) = ep(t) = g((1 − x)p(1 − p)).
The maximum is at p = 1 /2, proving the formula. The exceptional constant pure-output case has
the same value one; continuity covers the remaining endpoints.
The threshold itself is an antecedent, not a new convex-roof criterion or a necessary boundary
for entropy ﬂatness or for this simulation formula. For example, a = 0 .1,b = 0 .3,λ2 = 0 .5 has
complementary parallel cost about 0.600876037 ebits per use. This determines the complementary
simulation rate, not the simulation cost of Φ.
There is also a suﬃcient low-coherence regime with a simpler optimization. Deﬁne the classical
conditional entropy
J(p) = h(p) + (1 − p)h(a) + ph(b) − h(a+ kp).
The endpoint mixture in every reversed roof gives fp(t) ≤ J(p), by the classical entropy chain rule.
If p0 maximizes J, is interior, and has 0 <t0 = t(p0) <1, then
λ2 ≤ k2p0(1 − p0)
t0(1 − t0) =⇒ Epar
C (Φc) = J(p0)/ln 2. (20)
Indeed, the quadratic coeﬃcient of the reversed determinant at p0 is L(λ2 − Lk2) ≤ 0. Since g is
increasing and concave, ep0 is concave. Its convex envelope is its endpoint chord, attaining the upper
bound J(p0). Equation ( 20) is suﬃcient; no complete transition diagram is asserted.
Proposition 12 (Strict separation from Choi-state cost) . For a = 1 /10,b = 3 /10,λ2 = 1 /10, let
N = Φ c and let JN be its normalized Choi state. Then
Epar
C (N) >EC(JN ).
In particular a Bell input does not maximize Ech
F (N).
Proof. At p= 1 /2 the reversed parameters have ap = 1 /4, bp = 1 /8, kp = 5 /8 and λ2
p = 5 /48. The
quadratic coeﬃcient is 5/48 − 25/64 = −55/192 <0, so it remains negative in an open interval of p.
There the endpoint-chord argument gives GN (p) = J(p) exactly. But
J′(1/2) = h(3/10) − h(1/10) − 3
5 ln(3/2) = 1
10 ln
2639
77

>0,
because 1259712 >823543. Thus an input with p> 1/2 has strictly larger formation than the Choi
input. Theorem 10 identiﬁes the channel cost with its maximum formation, whereas Corollary 7,
applied to W1/2, identiﬁes the Choi-state cost with its formation.
Consequently this channel cannot be simulated exactly by LOCC using one copy of its own
Choi state per call: preparing many such states at their state cost would contradict the strict
inequality. Other resource states are not excluded. The example has λ2 >ab and is nonunital, so it
does not merely restate the covariant epolarizing example of [ 20]. Approximate sampled values are
0.704192652 ebits at the Bell input and 0.704712865 near p= 0 .516949108; the strict proof does not
use these values.
11

7 Finite-block consequences
The preceding result also applies to nonidentical channels in ( 2). Write ei,fi,ti for the corresponding
functions of channel Φi.
Corollary 13. For every state ρ on n qubits, with marginal excitation probabilities pi,
S((Φ1 ⊗ · · · ⊗ Φn)(ρ)) ≥
nX
i=1
fi(pi).
Proof. For a pure input split at the ﬁrst site and use ( 9). Apply induction on each conditional
remaining state and combine its populations using convexity of each fi. At the ﬁrst site e1 ≥
f1. A pure-state decomposition, entropy concavity and convexity of the fi give the mixed-input
statement.
This yields an exact accounting of the Holevo deﬁcit. Let a pure ensemble have output states ωℓ,
mean ¯ω, populations piℓ and means ¯pi. Put
ci = (ln 2) χ(Φi), σ =
O
i
diag ¯ωi, R ℓ = S(ωℓ) −
X
i
fi(piℓ) ≥ 0.
Using quantum relative entropy in nats, direct subtraction gives
X
i
ci − (ln 2)χ(ensemble) =
X
i
[ci − h(ti(¯pi)) + fi(¯pi)]
+ D(¯ω∥σ) +
X
ℓ
wℓRℓ (21)
+
X
i
"X
ℓ
wℓfi(piℓ) − fi(¯pi)
#
.
Every term is nonnegative. In particular, D(¯ω∥σ) = P
ih(ti(¯pi)) − S(¯ω). The support convention
is harmless: a zero marginal basis probability gives zero support of ¯ω on that sector. Equation ( 21)
is a consequence of the population bound and standard relative-entropy identities. It extends the
usual ﬁnite-block deﬁcit method, including that used for amplitude damping in [ 2]; it does not imply
uniqueness of optimizers or a uniform positive gap.
8 Scalar computation and examples
The envelope in ( 10) can be evaluated by the lower convex hull of the sampled curve. The next
bound makes the discretization error explicit, separately from ﬂoating-point error.
Proposition 14. Suppose e is L-Lipschitz on [0,1]. For a uniform grid of mesh 1/N, let fN be the
lower convex envelope of its sampled points, linearly extended between hull vertices. If
CN = 1
ln 2 max
p
{h(a+ kp) − fN(p)},
then
CN ≤ C(Φ) ≤ CN + L
2Nln 2 .
12

Proof. The piecewise-linear interpolant eeN satisﬁes |eeN − e| ≤ L/(2N): at relative position θ in
a cell the error is at most 2Lθ(1 − θ)/N. Taking lower convex envelopes preserves uniform error
bounds. Moreover fN ≥ f, because mixtures of sampled populations form a subset of all mixtures;
and co eeN = fN. Thus 0 ≤ fN − f ≤ L/(2N), which gives the claim.
For parameters with m= min pv(p) >0, write
v(p) = A+ Bp+ Dp2, A = a(1 − a), B = k(1 − 2a) − λ2, D = λ2 − k2.
The minimum is found from the endpoints and any interior vertex of this quadratic. A valid Lipschitz
constant is
L= max {|B|,|B+ 2D|}g′(m), g ′(m) = 2 atanh √1 − 4m√1 − 4m ,
with limit 2 at m= 1 /4. The function g′ is nonincreasing; this follows by diﬀerentiating atanh x/x.
When m= 0 one can instead use uniform continuity; the displayed ﬁnite- Lbound is not asserted at
that boundary.
For k >0, on a hull segment of slope s, the maximizing population is the projection onto that
segment of
p= (1 + exp( s/k))−1 − a
k .
This follows by setting kln((1 − t)/t) = s and using concavity. The case k= 0 has zero capacity.
A strict interior example is
a= 1
10, b = 3
10, k = 3
5, λ 2 = 1
2.
It is nonunital, has additional dephasing, and is not entanglement breaking. In fact the Choi partial
transpose is positive exactly when λ2 ≤ ab, which fails here. Its Choi rank is four, and min v =
5/56 >0, so it admits no pure output. The example is therefore not covered merely by the unital,
entanglement-breaking, pure-output or λ2 = k boundary cases.
a b λ2 capacity (bits, approximate) mean population
0.10 0.30 0.60 0.503934607 0.468332
0.10 0.30 0.50 0.407849860 0.470350
0.10 0.30 0.10 0.296671803 0.471876
0.02 0.30 0.514624 0.436551160 0.441065
These are reproducible ﬂoating-point illustrations on a grid with N = 200000 , not machine-certiﬁed
intervals. Proposition 14’s exact-arithmetic error bounds are below 3.8 × 10−6 bits for these cases,
before rounding error. The last example’s sampled hull optimizer mixes population 0 with approx-
imately 0.958865, illustrating why a single population pair need not suﬃce. No exact three-signal
necessity or global transition boundary is inferred from that numerical observation. For the same
four channels, a separate computation with N = 60000 gives complementary capacities approxi-
mately 0.492274059, 0.562095952, 0.906804474 and 0.469017072 bits. Direct Stinespring matrices
reproduce ( 15) and the phase covariance in 500 random cases, with maximum entry or eigenvalue
error below 5.0 × 10−16. These are ﬂoating-point illustrations, not machine-certiﬁed intervals. For
a= 0 .02,b = 0 .30,λ2 = 0 .514624, a sampled version of ( 14) at p= 0 .44 gives state formation costs
about 0.466960 ebits at z = 0 , 0.467338 at z = 0 .25, and 0.469937 at z = 0 .45. The coherence
constraint matters; the scalar roof f(p) alone does not describe all states. The linear program uses
20001 population samples and reconstructs a feasible phase ensemble up to numerical tolerance; no
continuous optimization certiﬁcate is claimed.
13

9 Veriﬁcation, dependence and scope
The proof uses Lemma 2 as an external result and gives all subsequent matrix and channel arguments
explicitly. Some minimum-output-entropy subregions are also covered by Fukuda’s composition
criterion [ 18]; that criterion is not a generic closure theorem for unrestricted Holevo additivity under
composition. A root-agent exploratory screen tested 16000 random rectangular block instances
without a violation. Separately, an Astra candidate audit tested 9000 block instances, their 27000
vertex instances, 1200 channel outputs with arbitrary ﬁnite partner samples, and 300 ensembles. Its
smallest residual was of order 10−14 in equality cases. These ﬂoating-point tests are error-ﬁnding
aids, not proofs.
A tempting alternative argument—that extra dephasing must increase the block entropy by at
least the scalar entropy increase—failed a numerical check and is not used. The valid argument
preserves the scalar entropy across the three vertices and invokes concavity only after their separate
estimates.
The present family excludes the permitted phase-covariant region λ2 >1−a−band channels with
negative longitudinal multiplier. We determine the state costs in Corollary 7 and the complemen-
tary parallel simulation cost in Theorem 10. We do not determine the original channel’s simulation
cost, adaptive simulation cost, quantum or private capacity, interacting multiqubit Davies dynam-
ics, or ﬁnite-error coding rates. Memoryless use is essential to the operational interpretation. No
claim of exhaustive literature coverage or worldwide priority accompanies the stated extension; its
mathematical scope is explicit and its immediate antecedents are identiﬁed.
AI assistance and review. The author directed an AI-assisted research process. Codex devel-
oped the extension, proofs, exposition and scalar calculations. A separately dispatched reviewer
requested as GPT-6 Astra with xhigh eﬀort audited frozen proof dossiers and an earlier capacity-
only manuscript. The reviewer has prior involvement and is not blind to the work. A subsequent
integrated version was also reviewed. The present version further adds complementary parallel sim-
ulation, reverse-channel closure and the strict Choi-cost separation; every manuscript assessment
must identify its exact input version, and an earlier assessment does not automatically apply to
these additions. Model runtime identity was not independently attested. No human peer review or
predetermined numerical grade is claimed.
Availability. The supplement contains the proof dossier, numerical scripts and reports, and source-
retrieval metadata. Original implementation code is released under CC0; the manuscript is oﬀered
under CC BY 4.0. External papers retain their authorship and licences. The scalar scripts do not
implement directed-rounding interval certiﬁcation.
References
[1] W. Roga, M. Fannes and K. Życzkowski, Davies maps for qubits and qutrits , Reports on Mathematical
Physics 66, 311–329 (2010). arXiv:0911.5607v2, Sections 3.1–3.3.
[2] Z. Tang, C. Zhu, G. Bai and X. Wang, Classical capacity and entanglement cost of the amplitude damping
channel, arXiv:2609.28592v1 (2026), Theorem 4.2 and Section 5.
[3] OpenAI, Classical capacity and entropy inequalities for generalized amplitude damping , 24 September
2026, Theorems 2.1 and 3.1, Corollary 1.2. OpenAI mathematics repository . Retrieved 17 October 2026;
PDF SHA256 recorded in the supplement.
14

[4] E. H. Lieb and M. B. Ruskai, Proof of the strong subadditivity of quantum-mechanical entropy , Journal
of Mathematical Physics 14, 1938–1941 (1973). doi:10.1063/1.1666274.
[5] C. King, Additivity for unital qubit channels , Journal of Mathematical Physics 43, 4641–4653 (2002).
doi:10.1063/1.1500791.
[6] P. W. Shor, Additivity of the classical capacity of entanglement-breaking quantum channels , Journal of
Mathematical Physics 43, 4334–4340 (2002). arXiv:quant-ph/0201149.
[7] F. Leditzky, E. Kaur, N. Datta and M. M. Wilde, Approaches for approximate additivity of the Holevo
information of quantum channels , Physical Review A 97, 012332 (2018). arXiv:1709.01111.
[8] A. S. Holevo, The capacity of the quantum channel with general signal states , IEEE Transactions on
Information Theory 44, 269–273 (1998). arXiv:quant-ph/9611023.
[9] B. Schumacher and M. D. Westmoreland, Sending classical information via noisy quantum channels ,
Physical Review A 56, 131–138 (1997). doi:10.1103/PhysRevA.56.131.
[10] G. G. Amosov, On estimating the output entropy of a tensor product of the quantum phase-damping chan-
nel with an arbitrary channel , Problems of Information Transmission 49, 224–231 (2013). arXiv:1301.2886,
Proposition 5.
[11] W. Roga, Entropy of quantum channel in the theory of quantum information , PhD thesis,
arXiv:1108.5065v3 (2011), Sections 5.6 and 6.
[12] K. Matsumoto, T. Shimono and A. Winter, Remarks on additivity of the Holevo channel capacity
and of the entanglement of formation , Communications in Mathematical Physics 246, 427–442 (2004).
arXiv:quant-ph/0206148v4, Sections 4–5.
[13] P. M. Hayden, M. Horodecki and B. M. Terhal, The asymptotic entanglement cost of preparing a quantum
state, Journal of Physics A 34, 6891–6898 (2001). arXiv:quant-ph/0008134, Theorem 1.
[14] A. S. Holevo, On complementary channels and the additivity problem , arXiv:quant-ph/0509101v3 (2005),
Theorem 1.
[15] C. King, K. Matsumoto, M. Nathanson and M. B. Ruskai, Properties of conjugate channels with ap-
plications to additivity and multiplicativity , Markov Processes and Related Fields 13, 391–423 (2007).
arXiv:quant-ph/0509126v3.
[16] M. Hellmund and A. Uhlmann, Concurrence and entanglement entropy of stochastic 1-qubit maps , Phys-
ical Review A 79, 052319 (2009). arXiv:0903.1340, Sections IV.C–D and V.
[17] W. K. Wootters, Entanglement of formation of an arbitrary state of two qubits , Physical Review Letters
80, 2245–2248 (1998). arXiv:quant-ph/9709029.
[18] M. Fukuda, Extending additivity from symmetric to asymmetric channels , Journal of Physics A 38, L753–
L758 (2005). arXiv:quant-ph/0505022v4.
[19] M. Berta, F. G. S. L. Brandão, M. Christandl and S. Wehner, Entanglement cost of quantum channels ,
IEEE Transactions on Information Theory 59, 6779–6795 (2013). arXiv:1108.5357v3, Theorem 12.
[20] M. M. Wilde, Entanglement cost and quantum channel simulation , Physical Review A 98, 042338 (2018).
arXiv:1807.11939v3, Sections II–IV.
[21] H. Barnum and E. Knill, Reversing quantum dynamics with near-optimal quantum and classical ﬁdelity ,
Journal of Mathematical Physics 43, 2097–2106 (2002). arXiv:quant-ph/0004088v1, Equation (4), for the
normalized reversal construction.
15