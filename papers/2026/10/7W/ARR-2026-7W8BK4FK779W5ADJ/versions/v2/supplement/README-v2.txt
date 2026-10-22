Supplement to version 2 (21 October 2026). Contains the version-1 supplement
files unchanged (README.txt, check_phase30.py, check_lyapunov30.py, their
recorded outputs, manifest.json from version 1) plus:

check_v2.py / check_v2_output.json: floating-point and 40-digit sanity checks
of Lemma 4 (critical pair), the Cartesian products of Corollary 8 for
k=1,2,3 with omega<0 and b<0, and the pairing identities for k=1,2,3.
Dependencies: numpy, mpmath. Run `python check_v2.py` in a writable folder;
it writes check_v2_output.json next to itself unless one exists.
Runtime about 35 s. None of this is a proof or an interval-certified result.

The finite-product example (check_phase30.py) is anecdotal. The Toeplitz
program (check_lyapunov30.py) is not used in version 2. manifest.json in this
archive describes the version-1 files only.
