PORTABLE INDEPENDENT REVIEW CHECKS

These checks concern candidate-proof-reviewed.txt and clifford-supplement-reviewed.txt,
not any later main.tex. Both texts retain exactly the hashes used in the review.

From this directory, with Python 3 and NumPy, SciPy, and SymPy installed, run:

    python -B independent_checks.py
    python -B clifford_checks.py

Only one SOURCE assignment was changed in each original checker: the absolute
development path was replaced with ROOT / the reviewed text filename. ROOT is
the directory containing the checker, so the commands also work from another
current directory. clifford_checks.py imports the independent_checks.py beside it.
No mathematical check, tolerance, seed, hash or expected result was changed.

The original checkers and report remain outside this folder, unchanged.
portable-audit.json records original and portable hashes and the two successful
executions. Each script writes its own JSON diagnostics and numbered reviewed text
in this directory; the tests do not need network access or any external manuscript.
Third-party PDF papers are not included. The review report lists their public URLs.

Review limitations remain unchanged: requested Astra/xhigh with reused context;
no independently attested effective model; no formal proof certification and no
numerical score. Finite numerical diagnostics complement the analytic review.
