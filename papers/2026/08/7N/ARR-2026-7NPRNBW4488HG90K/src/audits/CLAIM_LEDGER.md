# Claim ledger

| ID | Claim | Status | Evidence |
|---|---|---|---|
| C1 | Balanced one-matrix reduction and existence of an orthogonal equal-norm optimum | proved | Lemma 2.1; compactness, shear, reciprocal scaling |
| C2 | `kappa_d(F)=sum_j j b_j` on the one-positive cone, with sign reflection and zero padding | proved | Theorem 3.1; universal Horn triples plus weighted shift |
| C3 | Every balanced optimum has squared singular values `2 sum_{j=l}^n b_j` and rank `n` | proved | equality in every Horn-tail lower bound |
| C4 | Exact pairwise-dispersion identity and sharp `l1` stability constants | proved | Theorem 4.1; ordered cross-pair argument and equality families |
| C5 | `A_3(F)=12 sqrt(3) kappa_d(F)` for every finite-dimensional traceless Hermitian target | proved | Theorem 5.1; triangle area plus equilateral constructor |
| C6 | `A_4(F)=16 kappa_d(F)` for every finite-dimensional traceless Hermitian target | proved after correction | Theorem 5.2; shear/Gram determinant plus square constructor |
| C7 | `A_4/A_3=4/(3 sqrt(3))` for every nonzero target | proved | Corollary 5.3 |
| C8 | The one-spike expression does not extend by merging sign blocks | exact counterexample | `diag(5,1,-3,-3)`, Horn lower certificate and explicit factor |
| C9 | The inverse cost is strictly Schur-concave on each fixed-mass one-spike simplex | proved | Corollary 4.2; prefix-sum identity `kappa(F_b)=nP-sum_{k<n} B_k` |

## Corrected preliminary error

The viability memo used a false inequality involving the two diagonal norms.
The manuscript does not use it. The corrected proof controls the Gram area
`sqrt(ab-c^2)` after a commutator-preserving shear, and the replays include an
exact noncommuting counterexample to the discarded step.

## Nonclaims

- No closed formula for `kappa_d` when both sign multiplicities exceed one.
- No exact optimal action formula for five or more kicks.
- No classification of all optimizing matrices or all optimizing loops.
- No infinite-dimensional, operator-norm, higher-Magnus, or formalized proof.
- No established priority, peer review, or external scientific validation.
