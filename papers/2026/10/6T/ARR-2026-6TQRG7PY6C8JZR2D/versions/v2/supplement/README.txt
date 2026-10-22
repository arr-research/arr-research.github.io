A sharp circle-root residual barrier and its collapse with one interior zero
Lluis Eriksson. Supplement to candidate3, 18 October2026.

Python3 dependencies: mpmath, sympy, scipy. Copy the three scripts into an
empty writable directory and run them separately. They refuse to overwrite
their output files. All were already executed and reproduced in the
identified source audits; packaging did not trigger a new execution.

verify_schur.py: 84 exact projected Newton identities, 480 sampled geometric
checks, 23 binomial identities, rational constants and 10 finite certificates.
check_circle23.py: nine COMPLETE EXACT coefficient Parseval ratios, plus
six floating local-window Mathieu diagnostics. The latter are not a global
minimization proof. The redundant rational-membership assertion is harmless
and preserved to retain the reviewed script bytes.
check_single25.py: exact Jacobian4692/5 and moments, 12 high-precision
single-root configurations, slope and degree checks. It uses an implicit
parameter solver, independently of the explicit formulas in the manuscript.
No quadrature is performed and no full norm asymptotic is numerically certified.
The separate Astra audit additionally checks all34 degree classes at two
scales, including the positive-square-root formula; that audit is distinct
from these author scripts and is not claimed as a new execution here.

To compare reproduction, omit created_at; script_sha256 identifies the exact
script. Floating diagnostics can vary with package versions. Exact algebra
and rational Parseval outputs are exact. Computations do not prove the
arbitrary-order cone, all-degree statements, asymptotics or historical
priority. Those depend on the manuscript's analytic proofs and cited
classical Mathieu expansion. No third-party papers or private repository
metadata are redistributed. Same involved model reviewer; no human peer
review or formal proof certification is implied.

Manuscript/text CC BY4.0; authored code Apache2.0; generated data CC0.
