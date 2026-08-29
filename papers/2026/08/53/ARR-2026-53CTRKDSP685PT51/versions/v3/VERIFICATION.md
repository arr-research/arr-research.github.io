# Verification record for ARR-2026-53CTRKDSP685PT51 v3

Date: 2026-08-29

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 467,516 bytes; SHA-256 `4a6d9fc2b36b9ef1efdf30373175ce49bf412543e30acd944501f150791aef45`.
- PDF inspection found 22 A4 pages, no encryption, suspects, or embedded JavaScript.
- All 22 pages were rendered with Poppler and visually inspected. Equations, theorem blocks, both figures, the priority table, references, page breaks, and margins are legible and complete.
- Settled LuaLaTeX builds with `SOURCE_DATE_EPOCH=1787961600` and `FORCE_SOURCE_DATE=1` produced identical PDF bytes.
- `paper.md` and `paper.txt` were extracted mechanically from the exact canonical PDF.

## Numerical replay — pass within declared scope

Run from `src/`:

```text
python repro/verify_saturation_law.py
python repro/finite_sample_phase_diagram.py
python repro/verify_v3_additions.py
```

The main replay passes the Loewner identity, 256-bit Arb witness, local and spherical bridges, all-power moments and endpoint checks, finite-radius brackets, and three fixed-seed empirical block realizations. The v3 replay passes the explicit `C_p` constants, matching-lower coefficients, spherical `Q_R` constants, and finite-sample certificate. The phase script regenerates the figure and JSON at seed `2026082917` with 320 repetitions per sample size.

Stable generated-artifact hashes:

```text
saturation_law.pdf                 093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
saturation_certificate.json       b40a9bb318b48206fc0c5c9fc592c7b699d48a26b9b12b4ecc4805cf6215b9d1
finite_sample_resolution.pdf      b95dd92231aa7a9ca67fca0fcfa0293f4d4f627882a1afdfb3ec1d7efb3675a4
finite_sample_resolution.json     4bd3e130d11670c3a51d51ff0a4d962078ae415e95f4e90260e23da9293f9def
```

The numerical grids and fixed-seed simulation are diagnostics. They do not replace the analytic probability, uniformity, lower-bound, or asymptotic proofs.

## Hostile audits

Three v3 audits independently covered proof correctness, primary-literature priority, and reproducibility. Initial objections identified an unsupported bottom-eigenspace lower claim, an overstrong radial-scalar statement, an omitted second-moment line in the confidence lower bound, terminology around the dyadic shell and regularly varying sharpness, and one replay instruction error. All were corrected. Differential proof and novelty close-outs are PASS; reproducibility is PASS locally, with public-record verification required after release.

These AI-assisted audits are evidence of adversarial checking, not independent peer review or formal verification. ARR screening remains `not_assessed`.

## ARR labels and limitations

- Bibliography: **partial**. Directly overlapping primary sources were checked; absolute priority cannot be guaranteed.
- Reproducibility: **partial**. Replays and byte-rebuild pass, but the proofs are not formally verified and simulations do not calibrate theorem probabilities.
- Lean 4: **not applicable**.
- Scientific scope: sharp complexity is for a pointwise fixed-oracle Gram matrix under bilateral relative Loewner loss. The uniform theorem covers one full dyadic shell and pays a covering logarithm. No matching lower threshold is proved for the ordinary bottom eigenspace, and no new labeled minimax estimator is claimed.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a technically valid founder-pilot publication, not independent editorial or scientific certification.
