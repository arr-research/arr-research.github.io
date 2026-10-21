Interior-zero complexity of polynomial differentiation residuals
Lluis Eriksson. Supplement to candidate4, 18 October2026.

Python3 dependencies: numpy, mpmath, sympy, scipy. Copy scripts into a new
writable directory without their JSON outputs and run separately. Each script
refuses to overwrite its output. These exact bytes were executed previously;
the same involved Astra reviewer reproduced them in the recorded dossiers.
Packaging here does not claim a new execution. Preserve source bytes when
comparing script_sha256. Ignore timestamps and wall_seconds in reproduction;
floating values can vary with numerical library versions.

verify_schur.py: 84 exact projected Newton identities,480 sampled geometric
checks,23 binomial identities,rational constants and10 finite certificates.
check_circle23.py: nine complete exact coefficient Parseval ratios and six
floating local-window Mathieu diagnostics. No global numerical optimization.
check_single25.py: exact Jacobian and moments,12 high-precision parameter
configurations using an implicit solver. The explicit branch formula in the
paper was separately checked by the reviewer in all34 classes at two scales.
check_single_barrier26.py: reciprocal-moment identities and rational threshold
cases supporting the universal one-root proof; no norm computation.
check_fixed_count27.py:72 exact reciprocal identities and path recurrences.
Its older all-degree-threshold H bound is retained as an additional check;
the manuscript uses the stronger-scope positive-semicircle argument instead.
check_barrier27b.py:80 rational H cases and15180 integer saturation selections.
check_positive27c.py:eight exact positive-kernel identities and115 H cases.
check_factor27d.py:90 exact stable-factor/self-inversive-cofactor cases and
the unpaired-exterior-root negative control.
check_norm29.py:eight degrees and two full grids per degree, up to10000017.
High-precision parameters are converted to double precision; tiny weights
are masked. The cancellation-free formula approximates the exact family
but is not literally the residual of the fully rounded polynomial. Agreement
between grids does not bound shared errors. These are floating diagnostics,
not interval-certified norms. Fourier quadrature is exact only with exact
parameters and arithmetic. The included figure reports those diagnostics
against the analytic family constant, not a universal optimality claim.

All-degree inequalities, moment-cone existence, budget diagonalization and
norm asymptotics rely on the manuscript's analytic proofs. Finite tests do
not establish these universal statements or worldwide priority. The audits
are calculations by the same involved model reviewer, not a blind review,
an independent human report, or formal verification. No third-party papers,
private repository metadata, access credentials or internal prompts are
included in this public supplement.

Manuscript/text CC BY4.0; authored code Apache2.0; generated data CC0.
