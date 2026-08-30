# Hostile reproducibility audit — v4

Date: 2026-08-30

Verdict: **PASS locally within declared scope**. Public release verification is recorded separately after publication.

## Canonical candidate

- Path: `output/pdf/The_Schwarzian_Bridge_in_a_Single_Sigmoid_Neuron_v4.pdf`
- Bytes: `585942`
- SHA-256: `aeacddbe03c1e1152987f99025b7311384fafdf470ef87db4b30f39c51a4ad2d`
- `pdfinfo`: 28 A4 pages, PDF 1.5, no encryption, no JavaScript, no forms, no suspects.
- A settled LuaLaTeX rebuild with `SOURCE_DATE_EPOCH=1788048000` and `FORCE_SOURCE_DATE=1` reproduced identical bytes.
- All 28 pages were rendered at 144 dpi with Poppler. Four contact sheets and the new theorem/figure pages were inspected visually; no clipping, overflow, broken glyphs, blank pages, or unreadable figures were found.

`qpdf` was not installed on this host; `pdfinfo`, Poppler rendering, LaTeX log review, and byte-rebuild checks supplied the available PDF checks.

## Replay sequence

The documented sequence passed:

```text
python repro/verify_saturation_law.py
python repro/finite_sample_phase_diagram.py
python repro/verify_v3_additions.py
python repro/radial_phase_transition.py
python repro/spectral_lexicography.py
python repro/verify_v4_additions.py
```

Stable generated-artifact hashes:

```text
093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97  saturation_law.pdf
b40a9bb318b48206fc0c5c9fc592c7b699d48a26b9b12b4ecc4805cf6215b9d1  saturation_certificate.json
b95dd92231aa7a9ca67fca0fcfa0293f4d4f627882a1afdfb3ec1d7efb3675a4  finite_sample_resolution.pdf
4bd3e130d11670c3a51d51ff0a4d962078ae415e95f4e90260e23da9293f9def  finite_sample_resolution.json
147d9c23cd1349fcad8085c8cde21da8232527b91be9f655bc09e6424ffc05d2  radial_phase_transition.pdf
26ed3f0460847f79296301d5ecf087694358de819d976c671415762cc76c1d9a  radial_phase_transition.json
4d71aedc9ea8d0140c4eef5dd10d9882a71988b33fa3b4290ca79c52c51c15d1  spectral_lexicography.pdf
93d226200a59e3772b11ead7563eeed9e69a3a1d77951deacab97f4a5f7813c2  spectral_lexicography.json
```

## Scope

The quadrature and fixed-seed figures are diagnostics. They do not prove the asymptotic, probability, or priority claims. The analytic proofs are not formally verified, and no external independent reproduction is claimed.

