# Scientific checks — B4_two_planes_fold candidate 2

**UTC review window:** 2026-09-14T17:20Z–2026-09-14T17:33Z  
**Exact PDF SHA-256:** `ba8900141816e9f257783a1fd90ea9c92a1f2fc94bb7b681731bb05704f73e44`  
**Recommendation:** accept

## Main-claim audit

The theorem reduces the fold numerator to a two-state trajectory. From (E2), the definitions `X=kappa m`, `u=1/L`, and `h=kappa H` give (C1), `dot X=2X-h`, and `dot u=-Xu`. Differentiation gives `dot h=T-(2X+2q-1)h` and `dot T=X^2(8-q(q-1)u)-h(4X+q(q-1)u)`. For `Q=T-(q-1/2)h`, direct collection yields

`dot Q + (q-1/2)Q = X^2(8-q(q-1)u) + h[(2q-5)X+1/4+q(q-1)(1-u)]`.

For q>=4 the bracket is strictly positive. Before `L=q(q-1)/8`, both forcing terms are nonpositive whenever `h<=0`, so the integrating factor makes `Q<0` and prevents a first upward crossing. The first crossing therefore occurs after the threshold. There the zero-set forcing is positive; a zero with zero derivative would have positive second derivative and contradict negativity immediately before it. Once the strict upward crossing occurs, the same integrating factor prevents a return. The proof handles endpoints and strictness correctly.

The q=2,3 corollary uses a positive zero-set forcing everywhere and an appropriate nonnegative bracket. Its first-zero contradiction is also valid.

## Fresh execution

Before execution, the Python sources were inspected for deserialization, shell invocation, subprocesses, and writes. No pickle/cache loading or process execution was present in the selected scripts. Their only relevant generated-data writes were avoided except in the separate workcopy.

At `2026-09-14T17:29:17.5834757Z`, the supplied symbolic script and candidate-2 60-digit wrapper were run with `C:/Python312/python.exe -X utf8` from `work/sol-preassessment/B4_two_planes_fold`. They ended at `2026-09-14T17:29:32.9215882Z` with exit code 0.

Key output:

```text
(E3) = d/dkappa (E2): OK
(C1) OK
(C2) OK
(C3) OK
(C4) OK
(C5) OK
B3 (8.2) OK
(C6) OK
[kappa^3] H_q = -4*(q**2 - q - 8)/((q + 1)**2*(q + 2)**2*(q + 3)*(q + 4))
(E2) verified termwise from the series: OK
mp.dps=60 (set after importing num_phi)
q=4,5,6,10,30,60: Q<0 pre=True; dQe<=0 pre=True; Q>0 post=True; dQe>0 post=True; signs h=True
q=2,3: h>0 all=True; Q>0 all=True; dQe>0 all=True
maximum reported finite-difference relative error: 2.9e-57
maximum reported Poisson-identity absolute residual: 6.8e-57
```

The exact PDF was also extracted independently (`pdftotext -layout`): 12 pages and 42,895 characters. The title, theorem, disclosure, and bibliography are present and consistent with `paper.md`.

## Literature and reproducibility scope

The primary-source abstracts of Karp–Sitnik (arXiv:0902.3073), Baricz–Pogány (arXiv:1301.5423 and 1301.5635), and Gaunt (arXiv:2002.07430) support the manuscript's narrow statement that these works concern parameter log-convexity, quotient monotonicity, Turán inequalities, and special-function bounds rather than this fold numerator and Lyapunov construction. This is evidence for novelty, not an exhaustive priority certification.

The universal theorem is analytic and does not depend on the historical all-q interval certificates. I did not replay the corrected certificate for every q=4,...,200. I also did not inspect the earlier AIRR records, so the imported ingredients of Corollary 4.5 remain unchecked in this assessment.

## Disclosure

`independence=involved_in_manuscript`. The same model family participated in manuscript revision. This assessment used a fresh delegated task context with other reports withheld. That is not technical memory isolation or an independent human review. This is a local scientific preassessment only and does not accept, deposit, publish, authorize public release, or create an intake receipt.
