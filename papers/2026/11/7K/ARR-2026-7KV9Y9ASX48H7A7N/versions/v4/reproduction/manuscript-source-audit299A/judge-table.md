# Unit299 integration gate table

Exact target: 6f9b27f59e3b105a872c773ed4d38d027536655b; PR245 full-body normalized SHA25613bc8bdcebbc9c4c06a9f0366f540c95d512d397b94ae35f1cb413bf68327e78,1141 bytes.

| Gate | Finding | Analytical/integration reason |
|---|---|---|
| G1 | PASS | Active support, outside zero block, lambda2=0 and rank-one cases explicit. Any positive second eigenvalue has a real eigenvector with both nonzero signs, including multiplicity. No uniform-mean-zero shortcut. |
| G2 | PASS | p=1+rho=2s/(s+1), p/(2-p)=s. Restricted Holder gives each region's s-moment cost; endpoint HC inclusive. sqrt(r) Rayleigh quotient gives lambda1>=1 with uniform probability normalization. |
| G3 | PASS | Sharpness attaches to B*=2^(1/s), not the displayed positive-gap formula. B=1 gives r=1 and1-rho. Fixed rho,s,b, all dimensions and finite-size versus infimum distinctions explicit. |
| G4 | PASS | Actual unit298 single-site matrices reused with explicit sign-x convention. Critical quadratic cancellation and the bracketed tau coefficient correct; Ldelta4->0,Ldelta2->infinity. Balancing, Gram zeros, scalar Z and square AA*/A*A show actual top2->1. Earlier B>2 parameter constraint explicitly not imported. |
| G5 | PASS | ER^s=1 exactly; fixed interior moments vanish by t(t-s)/2 coefficient. theta=min1,s/2 keeps both exponents interior. Scalar cross bound valid for both y ranges, with a_L powers and Z_L^s retained. Er^s->2. |
| G6 | PASS | Dilution handles both sides of norm limit, nonzero denominator, epsilon->0. Exact boundary budget via Minkowski; signed sandwich perturbation vanishes. Weyl and exact spectral identity retain actual eigenvalue limits. Any fixedb<1 completed for allL by finite uniform prefix. |
| G7 | PASS | Prior theorems and historical assessment files preserved. Old PDF hash/grade retained as history, no299score. Classical sign splitting/HC credited; Aida/Biskup-Koenig comparisons scoped. No priority, formal/human/provider independence, physical/local/marginal claim imported. |
| Whole-paper integration | PASS | Complete1261-line source read; new proof matches accepted argument. Abstract and transitions distinguish strict regimes, preliminary quantitative bounds and exact budget including equality. Earlier first12 numbered results preserved. |
| Static references | PASS within source scope | 34labels, no duplicates, all ref/eqref and citation keys resolve. Standalone critical section occurs literally. This is not a TeX build check. |
| Package identity | PASS | All172unique bindings match raw Git and checkout bytes and are tracked. 181frozen subjects. 63added files,59evidence files;55historical files compared directly to originals with zero differences. |
| Historical formatting | DISCLOSED, NONBLOCKING | Read-only cr-at-eol diff check reports two original EOF blank lines; originals intentionally retained. No current new-section EOF finding. |
| PDF production/visual/scoring | OUTSIDE THIS AUDIT, PENDING | No build, PDF, rendered pages or score reviewed/created for299. Source acceptance cannot substitute for those separate steps. |
| External priority/technical isolation | UNESTABLISHED | Targeted primary readings and shared involved Codex context do not establish exhaustive novelty clearance or independent peer review. |

No gate was weakened or rewritten. No unresolved material mathematical or package blocker identified. Full objections, attempted falsifiers and limits are in full-report.md.
