# Verification record for ARR-2026-53CTRKDSP685PT51 v4

Date: 2026-08-30

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 585,942 bytes; SHA-256 `aeacddbe03c1e1152987f99025b7311384fafdf470ef87db4b30f39c51a4ad2d`.
- PDF inspection found 28 A4 pages, no encryption, suspects, forms, or embedded JavaScript. `qpdf` was unavailable, so structural inspection used Poppler metadata and text/render checks.
- All 28 pages were rendered with Poppler and visually inspected. Equations, theorem blocks, all four figures, the priority table, references, page breaks, and margins are legible and complete.
- Settled LuaLaTeX builds with `SOURCE_DATE_EPOCH=1788048000` and `FORCE_SOURCE_DATE=1` produced identical PDF bytes.
- `paper.md` and `paper.txt` were extracted mechanically from the exact canonical PDF.

## Numerical replay — pass within declared scope

Run from `src/`:

```text
python repro/verify_saturation_law.py
python repro/finite_sample_phase_diagram.py
python repro/verify_v3_additions.py
python repro/radial_phase_transition.py
python repro/spectral_lexicography.py
python repro/verify_v4_additions.py
```

The main and v3 replays pass the Loewner identity, 256-bit Arb witness, local and spherical bridges, all-power moments, finite-radius brackets, explicit `C_p` constants, matching-lower coefficients, spherical `Q_R` constants, and the finite-sample certificate. The v4 replays check all three exact inverse-radius phase constants, the explicit Gaussian-product confidence constants, spectral order-statistic constants, deterministic Gamma-radius quadrature, and fixed-seed finite-r convergence of the bottom projector.

Stable generated-artifact hashes:

```text
saturation_law.pdf                 093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
saturation_certificate.json       b40a9bb318b48206fc0c5c9fc592c7b699d48a26b9b12b4ecc4805cf6215b9d1
finite_sample_resolution.pdf      b95dd92231aa7a9ca67fca0fcfa0293f4d4f627882a1afdfb3ec1d7efb3675a4
finite_sample_resolution.json     4bd3e130d11670c3a51d51ff0a4d962078ae415e95f4e90260e23da9293f9def
radial_phase_transition.pdf       147d9c23cd1349fcad8085c8cde21da8232527b91be9f655bc09e6424ffc05d2
radial_phase_transition.json      26ed3f0460847f79296301d5ecf087694358de819d976c671415762cc76c1d9a
spectral_lexicography.pdf          4d71aedc9ea8d0140c4eef5dd10d9882a71988b33fa3b4290ca79c52c51c15d1
spectral_lexicography.json         93d226200a59e3772b11ead7563eeed9e69a3a1d77951deacab97f4a5f7813c2
```

The numerical grids and fixed-seed simulation are diagnostics. They do not replace the analytic probability, uniformity, lower-bound, or asymptotic proofs.

## Hostile audits

Three v4 audits independently covered proof correctness, bounded primary-literature novelty, and reproducibility. Corrections include explicit attribution of the deterministic scaled-SVD flag mechanism to Stewart (1984), restriction of the projector theorem to the iterated fixed-`d,n` limit actually proved, separation of fixed-confidence from stated `1/delta` complexity, and removal of any claim that the shell logarithm is nonintrinsic. Differential proof, novelty, and reproducibility close-outs are PASS locally, with public-record verification required after release.

These AI-assisted audits are evidence of adversarial checking, not independent peer review or formal verification. ARR screening remains `not_assessed`.

## ARR labels and limitations

- Bibliography: **partial**. Directly overlapping primary sources were checked; absolute priority cannot be guaranteed.
- Reproducibility: **partial**. Replays and byte-rebuild pass, but the proofs are not formally verified and simulations do not calibrate theorem probabilities.
- Lean 4: **not applicable**.
- Scientific scope: sharp oracle-Gram complexity is pointwise and uses bilateral relative Loewner loss. The uniform theorem covers one full dyadic shell and pays a covering logarithm. The bottom-projector theorem uses the iterated limit with fixed `d,n` before `r` tends to infinity; it is not a joint finite-`r` theorem. No labeled minimax estimator or removal of the shell logarithm is claimed.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a technically valid founder-pilot publication, not independent editorial or scientific certification.
