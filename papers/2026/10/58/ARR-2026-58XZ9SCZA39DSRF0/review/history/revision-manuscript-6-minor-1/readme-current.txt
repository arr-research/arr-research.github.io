Constant-gap entanglement distillation and a spectral criterion for noise-universal communication
Lluis Eriksson, 18 October 2026. Manuscript-6, minor correction 1.

Run scripts with Python -B in a separate writable copy; they write their JSON results beside themselves. Compare mathematical results after excluding timestamps. For spectral-checks-11.json only, also exclude script_sha256: the preserved historical record identifies the pre-comment-correction script. The distributed script changes only that comment; its Python AST and all mathematical results are identical. The two script hashes are explained below.
verify_escape.py: 200 original finite-matrix diagnostics; its old continuity table is NOT the current Table 1.
verify_extension_2.py: 500 cases for hidden-branch, hashing and finite pinching inequalities; its old table is also NOT the current Table 1.
verify_mismatch_1.py: 120 reset cases for phase averaging, parity Kraus, fixed-A entropy, chain rule and survivor hashing. Its direct Kraus calculation is for one source copy.
verify_general_noise_2.py: 240 cases of arbitrary bipartite noise (120) and separable matching-marginal noise (120), with full finite phase average, survivor/seed bounds and the log2(5) loss.
verify_table_3.py: current Table 1, evaluated at 100 decimal digits, rounded upward to six decimal places.
These finite diagnostics are not proofs of asymptotic coding, security, capacities or global novelty. The operational proof, bootstrap and order of limits are in the manuscript.
Python 3.12.14; numpy 2.2.6; scipy 1.18.0; mpmath 1.3.0. Numerical libraries can change floating-point residuals.
No external source PDF or private review is included. AI assistance is disclosed. Original manuscript and supplement: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ .

New in manuscript-4:
verify_reduction_seed_3.py: 1000 cases for arbitrary-marginal dominated pure-component reduction seeds, including singular marginals.
verify_mixed_correlated_4.py: 480 cases for mixed maximally correlated useful components, seed inequalities and survivor entropy.
verify_diagonal_invariant_5.py: 264 LDOI and control states; block entropies, phase twirl and scalar constants. These are algebra checks, not simulations of distillation rates.

New in manuscript-5: verify_minimax_6.py runs offline: 65 exact rational coefficient/spectrum cases and45 numerical parameter cases, with an independent Weyl construction and direct isotropic block spectra. The scalar postprocessing samples only require positive Choi overlap and are not random TP-channel samples. No coding, security, capacity or novelty is certified by these checks. The manuscript includes standard twirling/derandomization arguments separately. Run verification scripts in a copied scratch folder; verify_minimax_6.py refuses to overwrite an existing record.

New in manuscript-6: verify_spectral11.py and spectral-checks-11.json contain the scalar spectral diagnostics. Requirements: numpy, scipy, mpmath; no network. Run a copy in a scratch directory, where it writes spectral-checks-11.json. The only change from the audited private script is a corrected comment identifying its transpose convention; Python ASTs are identical. The diagnostic record is unchanged. Counts: 200 diagonal spectra, 200 complex pinching cases, 2807 scalar positivity checks, 25 variational comparisons, 5 high-precision maxima, 42 finite entropy constructions, 15 divergent-tail cases. These do not prove an infinite-dimensional capacity, historical novelty or formal verification. External source PDFs and private model-review records are not distributed here.

Spectral script provenance: historical script SHA-256 b29b84d1edb3346ac65c18a16a724b5efb2ff0d3ceb85cc868fa6cbc4be36003; distributed comment-corrected script SHA-256 8982b8e039b74237dd7cff9b5e08e785de62fcc1a4d2a841a2f2725c7942beb3. Reproduction changes created_at and script_sha256, and no mathematical field. The historical output is intentionally preserved.
