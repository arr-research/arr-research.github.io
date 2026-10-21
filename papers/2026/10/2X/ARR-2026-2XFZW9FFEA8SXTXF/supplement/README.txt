Supplement: Finite convex interpolation for polynomial Lyapunov existence
Lluis Eriksson, 18 October 2026. Candidate3.

These programs accompany the analytic proofs and exact examples. They do
not implement a general certified polynomial-time optimizer, root-isolation
algorithm, quantifier-elimination procedure, or proof assistant.

To reproduce, copy a program and needed data into a fresh working folder,
install requirements.txt, and run Python, for example:
 python -X utf8 -B check38.py
Historical JSON outputs are in results/. Compare mathematical fields,
excluding timestamps. Programs produce new JSON beside themselves; some
refuse an existing output. Keep the archived results untouched.

Programs added in candidate3:
 check36.py: polar identities, Fourier signs, boundary factors and box margins.
 check36a.py: common rational certificate and exact Lie derivative margin.
 check37.py: rational Pick kernels, convex combinations, Hermite inner ball,
             rational PSD diagnostics and error bookkeeping.
 check38.py: irrational simple/double residues, exact normalized functional
             perturbations on18 Cayley kernels,4 residue-recursion cases.
The original36 stability certificate is field-dependent; the paper uses
the stronger COMMON rational certificate verified by36a. Both are valid
and their historical outputs are distinguished. The general analytic and
complexity arguments require the written proofs, not just these tests.

Earlier exact programs, retained with byte-identical outputs:
 verify_certificate33.py and check_table33.py need degree-obstruction-33.json
beside the script. They check Sturm chains, Lie coefficients, rational
evaluation identities, and the printed degree2/4/6 exclusions. No optimizer.
 check_rational_example32b.py: rational Groebner/FGLM elimination and Sturm
counting, together with the analytic compactness argument in the paper.
 check_pick32.py and check_hierarchy31.py: exact identities and floating
diagnostics. Their executable content is unchanged from earlier candidates.
The M1 repair changed a comment in check_pick32.py, not its AST.

Numerical failures and discovery history are preserved, not proof bounds.
Hierarchy:15 solves,9optimal/6optimal_inaccurate. Pick:8 primal/dual pairs,
3 inaccurate primal and2 inaccurate dual. Of six nonlinear constrained
starts FIVE FAILED INFEASIBLE; one apparent local success was not a bound.
The jet feasible set is convex, despite its quadratic Pick representation;
the old nonconvex label was corrected in minor1. No optimizer was rerun
for that repair or for this supplement assembly.
Discovery33 searched degrees2/4/6/8, including an inaccurate degree6 solve;
rounding denominators100 and1000 failed before10000 passed. Exact subsequent
programs verify the fixed degree8 coefficients and exclusion nodes.

The complexity theorems use dense explicit input and rational tolerances.
They approximate a VALUE, not an exact equality decision or a certificate
whose degree/output size is guaranteed polynomial. Classical GLS and
complex-root refinement algorithms are cited, not reimplemented here.
The uniform coefficient-region theorem uses theoretical quantifier
elimination. The angular-zero result is a sufficient obstruction, not
a complete all-degree classification in that larger class.

No external copyrighted source PDFs, credentials or private data are
included. Review reports are separate exact-artifact records; the same
involved model reviewer is not an additional independent or human vote.
License: CC BY4.0 with the manuscript.
