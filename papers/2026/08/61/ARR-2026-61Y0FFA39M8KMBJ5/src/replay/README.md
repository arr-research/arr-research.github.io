# Lightweight reproduction

From the workspace root, run:

```powershell
python work/tenth_paper/verify_balanced_grassmann_rdf.py --output work/tenth_paper/repro/balanced_grassmann_verification.json
python work/tenth_paper/repro/verify_complete_radial_phase.py
python work/tenth_paper/repro/make_frontier_figure.py
```

The verifier checks the pair-sum norm transform, exact complete-homogeneous
inequalities on a rational simplex mesh, exact second/fourth moments, an
independent Schur-versus-divided-difference normalizer identity, numerical
quadrature against the elementary overlap normalizer, and the diagnostic
coexistence root.  The second verifier checks the exact closed formula for the
fold-numerator coefficients through degree 160, verifies every exceptional
coefficient exactly, and reports high-precision fold/contact residuals.  The
all-degree sign argument and scalar uniqueness proof remain analytic and are
printed in the paper.

All commands are single-process, bounded, and normally finish in under ten
seconds combined on a desktop CPU.  The release manifest records byte hashes;
no network service, random search, branch-and-bound, or large-memory job is
used.
