# Claim ledger

| ID | Claim | Status | Dependency | Forbidden strengthening |
|---|---|---|---|---|
| C1 | List inclusion vector lies in `P(R^(ell))` | proved | projector inequality, Rado, Edmonds union | not an attainability theorem |
| C2 | `r_ell(A)=min_C(|A\C|+ell*d(C))` | proved | Rado rank plus union theorem | none |
| C3 | Arbitrary-prior cap and prefix formula | proved | matroid polytope/greedy | no generic equality claim |
| C4 | Soft rewards with `sum_i w_{ia}<=ell` obey same cap | proved | weighted projector inequality | weights must lie in `[0,1]` |
| C5 | Canonical process compression preserves probabilities | proved | fixed tester normalization | use unnormalised Choi convention |
| C6 | Uniform deficit `Delta_ell=max_C(|C|-ell*d(C))` | proved | C2 | obstruction only |
| C7 | Matroid-obstruction disappearance threshold `max_C ceil(|C|/d(C))` | proved | C6 | weaker than projector feasibility test; not sufficient |
| C8 | Regular simplex: one guess `(m-1)/m`, two guesses `1` | proved | exact tight/root frames | novelty not claimed for antidistinguishability alone |
| C9 | Union-full need not imply perfect list discrimination; uniform optimum `(2+1/sqrt(3))/3` | proved | exact qubit primal-dual exclusion SDP | known nonsufficiency context must be cited |
| C10 | Robust core-tail cap extends to every list budget | proved | core polytope plus tail domination | cap by 1; keep separate architecture suprema |
| C11 | Strict-flat fixture gives `.81` versus dimension cap `1` | proved | `U_(2,5) direct-sum U_(1,1)` | upper bound only |
| C12 | No matching all-subset Bayesian matroid-union theorem found | provisional | targeted primary-source-led search | never write `first` |
| C13 | Deterministic dephase--prepare channels reduce every fixed parallel quantum strategy to a transcript partition | proved | dephasing flag-genie | excludes coherent phase oracles and indefinite order |
| C14 | The adaptive optimum for the same family obeys the exact classical Bellman recursion | proved | backward induction with label-independent conditional memory | not a theorem for arbitrary entanglement-breaking channels |
| C15 | Laminar prefix family: `P_par=min(1,ell(q+1)/M)` and `P_ad=min(1,ell*2^q/M)` | proved | C13--C14 plus exact cell counts | list/feedback tradeoff, not quantum advantage |
| C16 | Complete UEB one-guess law `(Tr sqrt(rho_R))^2/D` | rederived prior art | Feng--Duan--Ji 2006; frame/dual proof | not claimed new |
| C17 | Complete UEB fixed-probe list cap `min(1,ell(Tr sqrt(rho_R))^2/D)` | proved | C16 plus list-to-guess reduction | cap need not be attained |
| C18 | Independent Weyl histories obey the exact `SER_0/PAR_0/PAR_Bell` trichotomy | proved | support cap plus explicit transcript/Bell strategies | resource definitions are part of the theorem |
| C19 | At `D=4`, rank-two fixed probe and `ell=2`, the exact value is `(2+sqrt(2))/4<1` | proved | sector pinching and covariant primal--dual certificate | fixed-probe statement only |

## Claims prohibited in a paper

- “The matroid cap is always attainable.”
- “Condition `|C|<=ell*d(C)` characterizes perfect list discrimination.”
- “Condition `|C|<=ell*d(C)` is a new or strongest exclusion feasibility test.”
- “State exclusion/list discrimination is new.”
- “The simplex antidistinguishing POVM is new.”
- “Nonsufficiency of rank/support conditions is new.”
- “The priority search proves novelty.”
- “The laminar family proves a quantum advantage.”
- “The laminar family separates indefinite causal order.”
- “`SER_0` means every sequential protocol.”
- “The UEB one-guess spectrum law is new.”
- “The UEB list cap is always attainable.”
- “The fixed rank-two example is optimized over all rank-two probes.”
- Any extension of the Weyl-history formulas to incomplete, nonuniform, or repeated-common-unitary ensembles without a new proof.
- Any general-tester statement mixing normalized and unnormalised Choi factors.
