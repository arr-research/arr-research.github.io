# Hostile proof audit — v5

Verdict: **PASS within the stated scopes**. This is an AI-assisted adversarial audit, not formal verification or independent peer review.

## Referee blockers addressed

The v4 referee score of 5.40/10 identified two mathematical gaps between the manuscript's strongest qualitative claims and its quantitative theorems: no joint finite-\(r\), finite-\(n\) spectral-resolution theorem, and no rigorous source for the angular \(\sqrt{\log R}\) obstruction. Version 5 addresses both without claiming a sharp finite-sample crossover.

## Proof-chain audit

1. **Exterior-power lexicography (Lemma 8.5).** The operator-norm limit of each normalized exterior power is rank one. Products of leading eigenvalues therefore converge to the corresponding products of weights; division gives adjacent eigenvalue separation. The inverse Pluecker identity and principal-angle product then imply convergence of every leading spectral projector. The bottom eigenspace follows from the \((d-1)\)-plane case.
2. **Gaussian inverse law (Lemma 8.6).** A measurable rotation \(Q(z)\), with \(Q(0)=I_m\), reduces a deterministic or independent right-hand side to the first coordinate. Conditional orthogonal invariance preserves a standard Gaussian matrix independent of \(z\). A unit normal to the last \(m-1\) rows gives \(\|Y^{-1}z\|=\|z\|/|G|\), with \(G\sim N(0,1)\) independent of \(z\).
3. **Deterministic hierarchy perturbation (Lemma 8.7).** Splitting \(H=A+R\), the kernel of the first \(d-1\) rank-one terms is one-dimensional and the least positive eigenvalue of \(A\) is at least \(a_m s_{\min}(X_0)^2\). Positivity of \(R\), Rayleigh--Ritz, and an eigenbasis expansion give the stated projector bound whenever \(\eta<1\).
4. **Joint finite-saturation theorem (Theorem 8.9).** The proof conditions on three explicit events: the first \(d-1\) ordered magnitudes are sufficiently separated, their Gaussian row block is well conditioned through Lemma 8.6, and the full design has bounded operator norm. Union bounds match the displayed failure budget. On the event, Lemma 8.7 yields the stated projector error and the teacher-direction estimate follows by the triangle inequality.
5. **Intrinsic angular logarithm (Theorem 8.11).** The proof is intentionally iterated: first \(n\to\infty\) on every fixed finite grid, then \(R\to\infty\). The two-dimensional tangent block has the exact variance constant displayed in the paper. A separated grid has uniformly bounded normalized overlap; Sudakov minoration and Borell concentration give a maximum of order \(\sqrt{\log R}\), which transfers through the fixed-grid CLT.

## Boundary conditions checked

- The joint theorem is a conservative sufficient condition, not a matching phase transition.
- The angular theorem is an iterated-limit lower bound, not a finite-\(n\) uniform upper bound.
- No result assumes that empirical eigenvalue ordering is inherited automatically from pointwise population asymptotics.
- The logistic and all-power profile hypotheses remain explicit; no claim is made for arbitrary activations.

No proof-blocking defect was found after the final corrections.
