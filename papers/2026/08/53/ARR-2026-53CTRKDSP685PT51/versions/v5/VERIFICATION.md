# Verification record for ARR-2026-53CTRKDSP685PT51 v5

Date: 2026-08-30

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 660,109 bytes; SHA-256 `f90a308999b00697245dc87b0588efa162f8e380ed69f5c7454eff660b381e0d`.
- PDF inspection found 33 A4 pages, no encryption, suspects, forms, or embedded JavaScript. Structural inspection used Poppler metadata and text/render checks.
- All 33 pages were rendered with Poppler and visually inspected. Equations, theorem blocks, all five figures, the priority table, references, page breaks, and margins are legible and complete.
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
python repro/joint_spectral_resolution.py
python repro/verify_v5_additions.py
```

The main and v3 replays pass the Loewner identity, 256-bit Arb witness, local and spherical bridges, all-power moments, finite-radius brackets, explicit `C_p` constants, matching-lower coefficients, spherical `Q_R` constants, and the finite-sample certificate. The v4 replays check all three exact inverse-radius phase constants, the explicit Gaussian-product confidence constants, spectral order-statistic constants, deterministic Gamma-radius quadrature, and fixed-seed finite-r convergence of the bottom projector. The v5 replays check the finite hierarchy certificate, joint-threshold constants, 117 randomized hierarchy instances, and the angular-process variance for `p=1,2`.

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
joint_spectral_resolution.pdf      1dd16ea599c78a46645a544641274b0e8236d7d2424572db932a5c25b68d4eb5
joint_spectral_resolution.json     a961a7b695707d24315473aa228e2690d2a84621cff286238cc3319276e4a493
```

The numerical grids and fixed-seed simulation are diagnostics. They do not replace the analytic probability, uniformity, lower-bound, or asymptotic proofs.

## Hostile audits

Three v5 audits covered proof correctness, bounded primary-literature novelty, and reproducibility. The audit closed the two principal v4 referee objections by adding a conservative joint finite-`r`, finite-`n` bottom-projector theorem and an iterated-limit angular lower bound with the intrinsic `sqrt(log R)` factor. Exterior-power, inverse-Gaussian, perturbation, probability-budget, and Gaussian-process proof chains received differential PASS close-outs.

These AI-assisted audits are evidence of adversarial checking, not independent peer review or formal verification. ARR screening remains `not_assessed`.

## ARR labels and limitations

- Bibliography: **partial**. Directly overlapping primary sources were checked; absolute priority cannot be guaranteed.
- Reproducibility: **partial**. Replays and byte-rebuild pass, but the proofs are not formally verified and simulations do not calibrate theorem probabilities.
- Lean 4: **not applicable**.
- Scientific scope: sharp oracle-Gram complexity is pointwise and uses bilateral relative Loewner loss. The finite-saturation projector theorem is an explicit conservative sufficient condition, not a matching crossover. The angular theorem is an iterated-limit lower bound; a matching finite-sample upper/lower theorem remains open. No labeled minimax estimator is claimed.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a technically valid founder-pilot publication, not independent editorial or scientific certification.
