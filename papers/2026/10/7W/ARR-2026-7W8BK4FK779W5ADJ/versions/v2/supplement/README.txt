A sharp polynomial Lyapunov threshold for a stable cubic family
Lluis Eriksson. Supplement to manuscript 1, 18 October 2026.

This archive contains authored numerical diagnostics and their recorded
outputs. The theorems are proved analytically in the manuscript. These
programs do not prove global positivity, minimal degree or priority.

Python 3 dependencies: numpy, sympy, cvxpy (CLARABEL solver), matplotlib.
Copy the chosen .py file into a NEW writable directory without its output
JSON and run it there. The program refuses to overwrite existing results.
The plot creates a new figure/ directory and refuses to replace it.
The output-path changes from the earlier audited author programs are
documented in adaptation-record.json. Mathematical code is unchanged.

check_phase30.py: two exact symbolic identities, five sampled critical
boundary profiles, and a finite product with 2048 quadratic factors (degree
4096) evaluated at 8192 angles. Positive sampled margin is not an interval
certificate for all angles. Its quantiles are floating approximations.
The stored JSON retains its original date and historical wording about
an awaited audit. A later audit by the same involved Astra reviewer was
received; this is neither independent human nor formal verification.

check_lyapunov30.py: 18 necessary finite Toeplitz moment relaxations. The
JSON field "degree" denotes MOMENT TRUNCATION ORDER, not the degree of a
Lyapunov polynomial. Nine recorded solver statuses are optimal and nine
optimal_inaccurate; those statuses have deliberately been preserved.
No solver value is used as a proof of existence or of the exact threshold.
The stored results are historical outputs, not claimed new executions.
Reproductions can differ with solver/library versions and precision.

plot_phase.py: draws the analytically proved threshold and the earlier
Liu--Fitzsimmons obstruction. It is an explanatory plot, not an experiment.

The finite product sample is illustrative, not degree-optimal. The explicit
degree upper bound in the paper is sufficient and nonoptimal; the lower
degree divergence result has no claimed matching rate. The cubic family,
its stability and the earlier counterexample are credited to Liu and
Fitzsimmons. Binary-form sums of squares and earlier unbounded-degree
phenomena are classical prior results, explicitly credited in the paper.

No third-party full texts, private paths, credentials or review prompts
are distributed here. Manuscript/text CC BY 4.0; authored code Apache 2.0;
generated data CC0.
