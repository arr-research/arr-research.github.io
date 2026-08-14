# Claim ledger

| ID | Claim | Status | Dependency / risk |
|---|---|---|---|
| C1 | Fixed-\(W\) tester outcomes are exactly POVMs on \(\operatorname{supp}W\) after Moore--Penrose compression. | PROVED | Standard canonical tester construction; singular support handled. |
| C2 | The compression preserves every conditional probability and yields normalized effective states. | PROVED | Uses tester normalization \(\operatorname{Tr}WJ_i=1\). |
| C3 | Global GEN optimum equals a maximum of ordinary state-discrimination optima over physical deterministic \(W\). | PROVED | Requires the actual deterministic comb cone, not arbitrary PSD \(W\). |
| C4 | For mixed processes, correct-label probabilities lie in the independence polytope of the Rado matroid of process support subspaces. | PROVED | Support projections, singleton cap, Rado rank formula; common linear normalization only lowers subspace-sum dimensions. |
| C5 | \(P_{\rm GEN}\) is at most the maximum prior weight of an independent support transversal; rank-one reduces to a linearly independent oracle subfamily. | PROVED | Rado/Edmonds matroid theorem plus greedy telescoping. |
| C6 | Matroid-bound equality is equivalent to effective/original rank saturation at every sorted-prior prefix with a strict drop. | PROVED | Exact Abel-summation audit. |
| C7 | The matroid bound implies \(P_{\rm GEN}\le\Pi_{D_E}(p)\). | PROVED | Dimension-only state inequality due to Shah (2025); independent proof included. |
| C8 | Equality in the coarser dimension bound for fixed \(W\) is exactly the threshold-prior weighted-frame condition. | PROVED | Positive priors; tie set cannot be omitted. |
| C9 | Uniform equality is positive Parseval scalability, equivalently \(KCK=K\). | PROVED | Coefficients satisfy \(0\le c_i\le1\). |
| C10 | A projective promise \(X\) gives \(D_E\le H_X(k)\) and thus \(P_{\rm GEN}\le\Pi_{H_X(k)}(p)\). | PROVED | Same ordinary unitary channel in \(k\) slots; rank-one Choi tensors. |
| C11 | Perfect GEN discrimination iff some physical deterministic \(W\) obeys \(V^\dagger WV=I\). | PROVED | Linear SDP feasibility once deterministic constraints are written. |
| C12 | The diagonal-unitary prior fixture has exact GEN optimum .8. | PROVED / VERIFIED | \(D_E=2\), top-two bound .8, Bell strategy attains. |
| C13 | The distinct-unitary matroid fixture has exact GEN optimum .8 while the top-three bound is .9. | PROVED / VERIFIED | Choi relation exact; greedy basis \(I,Z,X\); Bell strategy attains. |
| C14 | The state top-priors theorem is new. | REJECTED | Already explicit in Shah, arXiv:2512.02477. |
| C15 | The matroid tester theorem is absent from all prior literature. | UNRESOLVED | Targeted search only; do not make an absolute novelty claim. |
| C16 | The same Hilbert-function bound holds unchanged for mixed/noisy process hypotheses. | REJECTED AS STATED | Rado support bound survives, but the rank-one coordinate-ring/Hilbert argument does not. |
| C17 | Distinct qubit phase gates together with one or two off-diagonal Pauli gates realize the matroid (U_{2,L}\oplus U_{c,c}), and its greedy weight is exact in the stated Bell-resolvable prior chamber. | PROVED / VERIFIED | One-query normalized Choi vectors; the chamber is sufficient, not necessary. |
| C18 | The equal-prior trine-plus-(X) family has exact general-tester optimum (1-a), while the total-span top-(D_E) relaxation is (3a), for (1/4<a<1/3). | PROVED / VERIFIED | Canonical trine PGM plus the orthogonal Choi complement assigned to (X); all four hypothesis effects are nonzero. |
| C19 | The trine PGM or symmetric-state measurement is new. | REJECTED | Classical symmetric-state/SRM machinery; Ban et al. (1997), Eldar--Forney (2001), and Weir et al. (2018) are cited. |
| C20 | Any positive low-rank cores give the robust ceiling beta(core)+sum_i p_i epsilon_i, capped at one. | PROVED / VERIFIED | Positive core/residual split, subset support inequality, and Abel telescoping; finite full-rank-noise fixture included. |
| C21 | Valid process admixture of weight eta weakens the core certificate by at most eta. | PROVED / VERIFIED | Special case of C20 using tester normalization of the noise process. |
| C22 | The mixed-support greedy certificate can be computed by linear matroid intersection in O(M N R^2 log R) arithmetic operations using a straightforward prefix implementation. | PROVED / DOCUMENTED | Rado reduction to linear/partition matroid intersection and Cunningham (1986); not claimed optimal. |
| C23 | The released Moore--Penrose fixture exercises a singular normalization. | VERIFIED | W=diag(1,2,0); canonical POVM sums to its support projector. |

## Mandatory language controls

- Say “rank-one process hypotheses” in every main dimension theorem.
- Say “physical deterministic tester/comb cone”; never optimize over an
  unrestricted positive normalization.
- Credit Shah for the pure-state prior-majorization inequality.
- Use “we combine/derive/lift”, not “we discover the top-priors bound”.
- Treat absence in a targeted search as provisional, not proof of novelty.
- Call the robust result a core-dependent upper bound, not an optimized noisy
  discrimination formula.
