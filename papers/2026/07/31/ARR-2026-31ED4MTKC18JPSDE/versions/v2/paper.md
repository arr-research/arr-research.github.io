# Clustering and the Transfer-Operator Gap: A Machine-Checked Dense-Family Criterion

Text extraction of the exact accepted PDF; the PDF controls mathematical typography.

Clustering and the T ransfer-Operator Gap:
A Machine-Checked Dense-F amily Criterion
Observable-dependent prefactors are harmless
at a common exponential rate
Lluis Eriksson
Subsequent correction candidate – 10 September 2026
Abstract
Inside a Lean 4 formalization programme for four-dimensionalSU(Nc) lattice Y ang–Mills,
we machine-check the operator-theoretic criterion that stands between exponential decay of
a Euclidean correlator and a spectral gap of a transfer operator. Let T be a bounded
self-adjoint operator on a Hilbert space and Ω a unit vector fixed by T, so that TΩ = Ω ,
and put S = T − |Ω⟩⟨Ω|. Exponential decay at rate r of the connected two-point function
⟨v, T nv⟩ − |⟨Ω, v ⟩|2 at every v is equivalent to the operator-norm bound ∥S∥ ≤ r.
The substantive part is the dense-family criterion. W riting Dr = {v : ∃C, ∀n, ∥Snv∥ ≤
Crn}, we prove that Dr is a linear subspace and that its density alone forces ∥S∥ ≤ r,
the constants being entirely unconstrained: a family of observables whose span is dense,
each carrying its own finite constant, suﬀices. Consequently prefactors that grow with the
support of the observable — the shape cluster expansions produce — do not obstruct the
gap, provided the exponential rate is common to the family and the family spans densely .
Those two provisos are essential; without them the statement is false.
No mathematical novelty is claimed for the criterion itself, which we expect to be known
in the language of local spectral theory; what is offered is its mechanization, its packaging
for families of observables, and the consequence for prefactors. W e also record what the
formalization does not contain: no Osterwalder–Seiler Hilbert space for any gauge theory , no
reflection positivity of the Wilson measure, no identification of a Euclidean correlator with
a matrix element. Nothing here is a claim about the continuum limit or about the Clay
problem. All results are machine-checked with no sorry and no project axioms.
1 What is proved, and what is not
The gap in the chain
A lattice mass gap, in the sense of Osterwalder and Seiler [1], is a statement about the spectrum of
an operator: the transfer operator T obtained from the Euclidean measure by reflection positivity
satisfies 0 ≤ T ≤ 1, fixes the vacuum vector Ω, and has a spectral gap on Ω⊥. Exponential decay
of a Euclidean correlator is, by itself, a statement about a real-valued function of the separation.
The two are connected by a theorem, not by terminology .
Within the formalization programme this paper belongs to, that theorem was absent. The
terminal statement of the lattice assembly concludes about a function cov : N → R; the pro-
gramme contains no Hilbert space of states, no transfer operator, no reflection positivity , and no
spectrum. This paper supplies the autonomous half of the missing link: the operator-theoretic
1

equivalence, at the level of generality where it is a theorem, machine-checked, together with the
sharpening that determines what an application must supply .
Scope, stated in advance
The following are not established in this paper, nor anywhere in the Lean development ac-
companying it: reflection positivity of the Wilson gauge measure; the Gelfand–Naimark–
Segal quotient; the existence of a transfer operator for any gauge theory; the identification
E[A · θnB] = ⟨AΩ, T nBΩ⟩; density of any concrete family of gauge-invariant observables in the
fluctuation sector of any such space. Consequently nothing in this paper is a claim about Y ang–
Mills, about the continuum limit, or about the Clay problem, and no statement below should
be read as transferring importance from the subject matter of the programme to the theorems
proved here. The equivalence itself is classical; see Section 9.
2 Setting
Let H be a Hilbert space over R (Sections 3) or over C (Sections 4–5).
Definition 2.1 (transfer data) . A pair (T, Ω) with T a bounded operator on H and Ω ∈ H
is transfer data when T is symmetric, ∥Ω∥ = 1 , and TΩ = Ω . W e write P = |Ω⟩⟨Ω| for the
rank-one projection Pv = ⟨Ω, v ⟩ Ω and
S = T − P
for the vacuum-projected operator. These are the properties that reflection positivity is used to
produce; here they are hypotheses.
Definition 2.2 (connected two-point function). F orv ∈ H and n ∈ N,
Gv(n) = ⟨v, T nv⟩ − ⟨ v, Ω⟩⟨Ω, v ⟩.
The elementary reason the truncated correlator, and not the full one, is the object that sees
a gap is the following identity , which is proved by induction from SΩ = 0 and ⟨Ω, Sv ⟩ = 0 .
Lemma 2.3 (structural identity). F or transfer data and everyn ≥ 0, Sn+1v = Tn+1v−⟨Ω, v ⟩ Ω,
and hence Gv(n + 1) = ⟨v, S n+1v⟩.
3 The equivalence
Theorem 3.1 (clustering ⇐ ⇒ gap). Let (T, Ω) be transfer data on a real Hilbert space and
r ≥ 0. Then
∥S∥ ≤ r ⇐ ⇒ ∀ v ∈ H, ∃C, ∀n, |Gv(n)| ≤ C rn.
F or r ≥ 1 this is only a norm bound; it does not imply a positive transfer gap. Strict
contraction of the fluctuation sector requires r < 1. The case r = 0 is included and forces S = 0 .
T wo features of the statement are deliberate. First, the conclusion is an operator-norm
bound and not an assertion of the form ∃ m > 0; the latter shape admits vacuous witnesses,
and this programme’s own history contains one. Second, the statement is an equivalence, so it
cannot be weakened into vacuity in either direction.
2

Proof sketch. F orward. F or n ≥ 1, Lemma 2.3 gives |Gv(n)| = |⟨v, S nv⟩| ≤ ∥ v∥ ∥Sn∥ ∥v∥ ≤
∥v∥2rn; the n = 0 term is ∥v∥2 − |⟨Ω, v ⟩|2 ∈ [0, ∥v∥2] by Cauchy–Schwarz.
Backward, the case r = 0 . Lemma 2.3 at n = 1 gives 0 ≤ ∥Sv∥2 = Gv(2) ≤ Cv · 02 = 0 for
every v, so S = 0 and ∥S∥ ≤ 0.
Backward, the case r > 0. F orn ≥ 1 — and only for n ≥ 1, since Gv(0) ̸= ⟨v, S 0v⟩ in general
— Lemma 2.3 and self-adjointness give Gv(2n) = ⟨v, S 2nv⟩ = ∥Snv∥2, so clustering at even times
gives ∥Snv∥ ≤ √Cv rn pointwise. Banach–Steinhaus applied to {r−nSn : n ≥ 1} upgrades this
to ∥Sn∥ ≤ Mrn; and for symmetric S one has ∥S2∥ = ∥S∥2 — proved from Cauchy–Schwarz,
without the C∗-algebra API — hence ∥S∥2k
≤ Mr2k
for all k, and ∥S∥ ≤ r.
4 The sharp form: the constants do not matter
Theorem 3.1 assumes clustering at every vector. A cluster expansion never delivers that: it
bounds a family of observables. On a merely dense set, the elementary argument — extend
the quadratic-form bound by continuity — requires the constant to be uniformly quadratic,
Cv = K∥v∥2. That requirement is a property of that proof. It is not necessary .
Definition 4.1 (decay domain). F or a bounded operator S on H and r ≥ 0,
Dr(S) =
{
v ∈ H : ∃C ≥ 0, ∀n, ∥Snv∥ ≤ C rn }
.
(The Lean definition leaves r and C unconstrained in R and carries r ≥ 0 as a hypothesis at
each use site, which is why the subspace lemma below holds for either sign; the restriction here
is for readability .)
Lemma 4.2. Dr(S) is a linear subspace of H (a Submodule in the formalization).
Proof. Cu+v ≤ Cu + Cv and Cλv = |λ| Cv.
Lemma 4.2 contains the algebraic step that passes from a controlled family to its linear
span; the substantive mathematics is the functional-calculus argument of Theorem 4.3. What
the lemma buys is that per-observable constants, however fast they grow along any exhaustion
of the space, close up under linear combination with no uniformity whatsoever.
Theorem 4.3 (sharp form). Let S be a self-adjoint bounded operator on a complex Hilbert space
H ̸= 0 and r ≥ 0. If Dr(S) is dense in H, then ∥S∥ ≤ r. Consequently, if D ⊆ H has dense
span and every v ∈ D admits some finite Cv with ∥Snv∥ ≤ Cvrn for al l n, then ∥S∥ ≤ r.
Proof. Suppose ∥S∥ > r . The norm is attained on the spectrum, so there is λ0 ∈ σ(S) with
|λ0| = ∥S∥; choose r < c < |λ0| and set f(x) = max(0 , |x| − c), so that f vanishes on {|x| ≤ c}
and f(λ0) > 0. Define
kn(x) = f(x)
(max(c, |x|))2n .
The denominator is ≥ c2n > 0 for every real x, so kn is continuous with no case analysis and no
division by zero, even when 0 ∈ σ(S); and kn(x) x2n = f(x) identically , the even power letting
|x| stand in for x. Hence, in the continuous functional calculus, f(S) = kn(S) S2n, and on the
spectrum ∥kn∥∞ ≤ ∥S∥/c2n. F or v ∈ Dr(S),
∥f(S)v∥ = ∥kn(S) S2nv∥ ≤ ∥S∥
c2n Cv r2n = ∥S∥ Cv
(r
c
)2n
− − − →
n→∞
0,
3

so f(S) annihilates Dr(S), hence all of H by density and continuity . But ∥f(S)∥ ≥ | f(λ0)| > 0,
a contradiction. The second statement follows from Lemma 4.2, which places the span of D
inside Dr(S).
Self-adjointness is also essential. F or the backward shiftB on ℓ2(N), every finitely supported
vector belongs to Dr(B) for any fixed 0 < r < 1: its iterates eventually vanish, and a finite
constant bounds the preceding iterates. Those vectors are dense, yet ∥B∥ = 1 > r . This
example is a paper-level explanation of the hypothesis, not an additional Lean declaration.
The chosen formal proof and a direct alternative
The formal proof above uses continuous functional calculus. T wo tempting shortcuts do not
by themselves close the argument, but a pointwise dyadic estimate does give an elementary
alternative. The distinction is between the chosen formal implementation and mathematical
necessity .
Banach–Steinhaus does not apply. A dense subspace may be meagre — the algebraic span of a
countable family in an infinite-dimensional Hilbert space is — so the non-meagreness hypothesis
is not at hand, and pointwise bounds on such a set yield no uniform bound. This is exactly the
difference between Theorem 3.1, where the hypothesis is at every vector of H and completeness
pays for the uniformity , and Theorem 4.3, where it is not.
A pointwise argument with powers. F or a bounded self-adjoint S, Cauchy–Schwarz gives, for
every integer m ≥ 1,
∥Smv∥2 = |⟨v, S 2mv⟩| ≤ ∥ v∥ ∥S2mv∥.
Iterating with m = 1 , 2, 4, . . . gives, for k ≥ 1,
∥Sv∥ ≤ ∥ v∥1−2−k
∥S2k
v∥2−k
.
If v ∈ Dr(S) and r > 0, take its finite constant Cv in ∥Snv∥ ≤ Cvrn. F or v ̸= 0 , the case n = 0
implies Cv ≥ ∥v∥ > 0, and hence
∥Sv∥ ≤ ∥ v∥1−2−k
C2−k
v r − →r∥v∥.
The zero vector is immediate; if r = 0 , the estimate at n = 1 already gives Sv = 0 . Density
and continuity now imply ∥S∥ ≤ r. This is a paper-level alternative proof, valid over real or
complex Hilbert spaces, not a new Lean declaration. Strong convergence of powers alone would
not suﬀice: multiplication by x on L2[0, 1] has powers converging strongly to zero while their
norms remain one. That example does not defeat the common exponential-rate hypothesis used
above.
The resolvent route stal ls. A vector v ∈ D r(S) lies in the range of t − S for every t > r by
a Neumann series, but with a vector-dependent bound; and a self-adjoint operator with dense
range need not be invertible.
Continuous functional calculus supplies the formal proof retained here; the dyadic estimate
supplies a direct mathematical alternative. The existing theorem statements and formal sources
are unchanged.
Corollary 4.4 (support-exponential constants are not an obstruction). Let {As} be observables
whose span is dense in H, indexed so that As has support of size s, and suppose ∥SnAs∥ ≤ C(s) rn
for al l n, with a rate 0 ≤ r < 1 independent of s. Then ∥S∥ ≤ r, whatever the growth of C. In
particular C(s) = eκs is admissible.
4

Corollary 4.4 is the reason the sharp form matters for the programme this paper belongs to.
The volume-uniform area law of [ 5] carries a constant of the form Nc e|supp|·4d K , exponential in
the edge support of the loop, while its decay rate is the support-independent polymer activity
rate; and the connecting-cluster estimate of the same programme has a support-independent
constant but covers only a local, non-total family . A natural reading of that pair is that the two
horns cannot be closed simultaneously , so that a total family must carry growing constants and
the gap must fail volume-uniformly . Corollary 4.4 shows that reading is false: the growth of the
constant is irrelevant, and only the uniformity of the rate is load-bearing.
W e stress the limited role of that citation. The area-law theorem is used here only to
motivate the shape of an observable-dependent constant. It does not supply a dense family in
any Osterwalder–Seiler space, it does not supply the time-direction correlator, it does not supply
a common rate on such a family , and it does not supply the identification with Tn. Nothing in
this paper brings a mass gap closer to being deduced from an area law.
5 The bridge in its own objects, and volume-uniformity
Theorem 4.3 is about a bare self-adjoint operator. Composing it with Definitions 2.1–2.2 gives
the bridge in the form an application would consume.
Theorem 5.1 (sharp bridge) . Let (T, Ω) be transfer data on a complex Hilbert space H ̸= 0
with T self-adjoint, and let r ≥ 0. Then ∥S∥ ≤ r if and only if there is a set D ⊆ H with dense
span such that every v ∈ D admits some finite C with |Gv(n)| ≤ C rn for al l n.
Theorem 5.2 (volume-uniformity). Let (Ti, Ωi) be transfer data on complex Hilbert spaces
Hi ̸= 0 , i ranging over any index set, and let 0 < r < 1 be a common rate for which each
i admits a family as in Theorem 5.1 — with per-observable constants that need not be related
across i or within it. Then, with m = − log r > 0,
∥Ti − |Ωi⟩⟨Ωi|∥ ≤ e−m for every i.
No uniform control of the constants Cv,i is assumed. The only cross-volume quantitative
input is the common rate r; once that rate is fixed, Theorem 5.1 yields the same operator-norm
bound for every i, its conclusion being a bound whose constant never sees the index. Thus m
is a common exponential contraction exponent. Interpreting it as a Hamiltonian mass bound
additionally requires a positive transfer operator represented as Ti = e−Hi and the relevant
Hamiltonian construction. Self-adjointness alone permits negative transfer eigenvalues. No such
gauge-theory transfer operator or Hamiltonian is constructed here.
6 Non-vacuity
Every statement above is exhibited with inhabitants in which the fluctuation sector is nonzero,
so that none of them is satisfied only in the degenerate one-dimensional case.
Proposition 6.1. Let Ω, w be orthonormal in H and 0 < r < 1. Then T = r id + (1 − r)P is
transfer data with
∥T − |Ω⟩⟨Ω|∥ = r exactly, T − |Ω⟩⟨Ω| ̸= 0 , − log r > 0.
The hypotheses are discharged concretely in R2 and in C2 with Ω = e0, w = e1, so the family is
inhabited.
5

7 What remains
Within the abstract implication isolated here, the remaining bridge obligations are: reflection
positivity of the Wilson gauge measure in the time direction; the GNS quotient and the transfer
operator with 0 ≤ T ≤ 1 and TΩ = Ω ; the identification of the Euclidean correlator with
a matrix element; and density , in the fluctuation sector of the resulting space, of a family of
gauge-invariant observables for which a clustering estimate at a common rate is available. Each is
classical mathematics [1, 2] that has not, to our knowledge, been mechanized; none is established
here.
W e do not claim that list is exhaustive for any particular notion of “mass gap” . Depending
on the formulation one may additionally need uniqueness of the vacuum, control of the rate at
all times rather than along a subsequence, the correct gauge-invariant sector, the relation to
a Hamiltonian, and a volume or lattice-spacing limit. What we do claim is that the criterion
proved above is one obligation that is now discharged, and that the prefactor question is not
among the remaining ones.
Remark 7.1 (a boundary of the formalization, not of the mathematics) . Theorem 3.1 is for-
malized over a real Hilbert space and Theorems 4.3–5.2 over a complex one. The reason is that
the library’s continuous functional calculus for self-adjoint elements is derived from the complex
case and is unavailable for operators on a real space, and the library contains no complexification
of a real inner-product space. The two are separate instantiations of one argument; the transport
between them is not formalized here and is not claimed. This is a boundary of the formalization,
not of the mathematics.
8 F ormalization architecture
The development is three modules and runs in one direction:
projection identities → elementary equivalence → decay subspace
→ continuous cut-off → sharp bridge.
What the library did not provide. T wo absences shaped the design. Mathlib has no
complexification of a real inner-product space, and its continuous functional calculus for self-
adjoint elements is derived from the complex case, so it is unavailable for operators on a real
Hilbert space. The formal proof of Theorem 3.1 uses no functional calculus and is stated over
R; the formal proofs of Theorems 4.3 and 5.1 use it and are stated over C. This split reflects the
chosen implementation and available tooling, not a mathematical necessity . The direct argument
in Section 4 is paper-level; no new formal transport between the real and complex statements is
claimed (Remark 7.1).
T wo devices that may be reusable. First, the C∗ step ∥S2∥ = ∥S∥2 for symmetric S is
proved directly from Cauchy–Schwarz (norm_sq_of_symm), so the real-case module depends on
no C∗-algebra API at all. Second, the cut-off quotient is defined as kn(x) = f(x)/(max(c, |x|))2n
rather than f(x)/x2n: the denominator is bounded below by c2n > 0 at every real x, so continuity
needs no case analysis and no division by zero can occur even when 0 lies in the spectrum,
while the even power makes the factorisation kn(x) x2n = f(x) hold identically , with no side
6

condition. Both are small, and both removed what would otherwise have been the fragile parts
of the argument.
What verification actually costs. Building the three modules and their closure takes 8160
jobs; the full core root takes 8415. The difference is not the interesting quantity: because the
modules import Mathlib wholesale, essentially the entire cost in both cases is Mathlib, retrieved
from cache. The lane’s own content is three module compilations. W e record this because a
“minimal verification target” would be misleading here — it would not meaningfully reduce the
work a referee must do, and the 8415 figure should be read as evidence of integration into the
core, not as a measure of this paper’s size.
9 Reproducibility , verification links, and provenance
F reeze
All statements are machine-checked in Lean 4 (toolchain leanprover/lean4:v4.29.0-rc6)
against Mathlib pinned to commit 07642720480157414db592fa85b626dafb71355b. The freeze
is the source tree at commit ad9c93d793fa0b082f2373c2aea3ea5b99f9c6b8; lake build
YangMillsCore completes with 8415 jobs in the recorded historical build. The oracle driver
enumerates the declarations it checks; its coverage is not asserted here to include every declara-
tion reachable from the core root. The final linked transcript records 2304 answers: 22 report
no axiom dependencies, and the other 2282 have axiom sets [propext, Classical.choice,
Quot.sound], [propext, Quot.sound] or [propext]. All recorded sets are subsets of the three
listed axioms, including the empty set; no recorded answer includes sorryAx or a project axiom.
These are historical transcript observations, not a new build of this candidate.
Theorem-to-artifact map
The three modules are YangMills/OS/TransferGap.lean (real case), YangMills/OS/Dense
Clustering.lean (sharp form) and YangMills/OS/SharpBridge.lean (sharp bridge); the
column below names the module by initial.
Statement here Lean name Mod.
Def. 2.1 (P, S) vacuumProjection, projectedTransfer T
Def. 2.2 (Gv) connCorr T
transfer data VacuumTransfer T
Lem. 2.3 projected_pow_succ, connCorr_eq T
Thm. 3.1 clustering_iff_gap T
∥S2∥ = ∥S∥2, proved by hand norm_sq_of_symm T
elementary dense form gap_of_dense_clustering T
Def. 4.1 decayDomain D
Lem. 4.2 decaySubmodule D
cut-off and factorisation cutOff, cutOffQuot, cutOffQuot_mul_pow,
cutOffQuot_le
D
Thm. 4.3 norm_le_of_dense_decayDomain,
norm_le_of_span_dense_decay
D
Thm. 5.1 sharp_clustering_iff_gap S
7

Statement here Lean name Mod.
Thm. 5.2 volumeUniform_sharp_gap (and
volumeUniform_gap, real case)
S, T
Prop. 6.1 exists_vacuumTransfer_gap,
euclidean_two_dim_vacuumTransfer_gap
T
Prop. 6.1 (complex) exists_vacuumTransferC_gap,
euclidean_two_dim_vacuumTransferC_gap
S
Oracle transcripts and build root
• Core root: YangMillsCore.lean.
• Oracle driver: oracle_check.lean.
• T ranscript at the real-case commit: ORACLE-20260727-34696985.txt .
• T ranscript at the sharp-form commit: ORACLE-20260727-a0ce50ea.txt .
• T ranscript at the sharp-bridge commit: ORACLE-20260727-e5d76dae.txt .
• Governance and scope record: docs/O-BRIDGE-CHARTER.md and docs/O-BRIDGE-AUDIT
-20260727.md.
The transcripts were produced at the three code commits after which they are named; those
commits were replayed over two intervening documentation-only commits before publication,
and the replay is recorded together with the byte-level equality of the three module blobs.
Provenance and prior art
The equivalence between exponential clustering and a gap of the transfer operator is classical
and no novelty is claimed for it: it is the standard argument of constructive field theory [ 2, 3],
and the lattice-gauge transfer operator together with its positivity is due to Osterwalder and
Seiler [1].
W e make no claim of mathematical novelty for Theorem 4.3 either. Its content —
that conceptually , Dr(S) is the spectral subspace ran E([−r, r]) of a self-adjoint S, so that its
density forces σ(S) ⊆ [−r, r]. That identification is offered as the conceptual reading and is not
separately formalized here; what the Lean development contains is the norm criterion itself, as
the theorem-to-artifact map above records. Criteria of this kind are standard material in local
spectral theory [4], where lim supn ∥Snv∥1/n is the local spectral radius at v and the sets on which
it is bounded are the local spectral subspaces. W e have not located the precise statement in
the form used here and have not performed an exhaustive search; rather than assert priority we
state the expectation that it is known, and we invite the closest antecedent. What we do claim
is the mechanization, the packaging of the criterion for families of observables with per-member
constants, and Corollary 4.4, which is the consequence that matters for cluster expansions and
which we have not seen drawn.
The volume-uniform area law whose constant shape motivates Corollary 4.4 is [5], the formal
antecedent within the same programme; its role here is motivational only , as stated in Section4.
8

References
[1] K. Osterwalder and E. Seiler, Gauge field theories on a lattice , Ann. Physics 110 (1978),
440–471.
[2] J. Glimm and A. Jaffe, Quantum Physics: A F unctional Integral Point of View , 2nd ed.,
Springer, 1987; in particular §19.
[3] B. Simon, The P(ϕ)2 Euclidean (Quantum) Field Theory, Princeton University Press, 1974.
[4] K. B. Laursen and M. M. Neumann, An Introduction to Local Spectral Theory , London
Mathematical Society Monographs New Series 20, Clarendon Press / Oxford University
Press, 2000.
[5] L. Eriksson, A volume-uniform area law for lattice Y ang–Mil ls, machine-checked ,
ai.viXra.org:2607.0005.
[6] L. de Moura and S. Ullrich, The Lean 4 theorem prover and programming language, CADE 28
(2021), 625–635.
[7] The mathlib Community ,The Lean mathematical library, CPP 2020, 367–381.
[8] A. Jaffe and E. Witten, Quantum Y ang–Mil ls theory, Clay Mathematics Institute Millennium
Problem description, 2000.
AIRR revision disclosure. This subsequent T eX candidate addresses the bounded correc-
tions in the GPT-6 Astra High referee report on the preceding exact AIRR PDF. Astra remains
involved in the manuscript. The accompanying correction JSON identifies that assessed PDF,
the source hashes and every replacement. Historical formal sources, build records and numerical
evidence retain their original provenance. No new Lean build or numerical rerun is claimed for
these corrections. The local operator compiled this new PDF after the source audit; no existing
PDF assessment transfers to it. This compiled candidate requires its own exact-byte assessment.
No editorial decision is made here.
9
