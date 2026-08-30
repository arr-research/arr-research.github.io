# Reproduction

Run from the manuscript root:

```text
python -m pip install -r repro/requirements.txt
python repro/verify_saturation_law.py
python repro/finite_sample_phase_diagram.py
python repro/verify_v3_additions.py
python repro/radial_phase_transition.py
python repro/spectral_lexicography.py
python repro/verify_v4_additions.py
python repro/joint_spectral_resolution.py
python repro/verify_v5_additions.py
```

The replay checks the closed logistic Loewner determinant at declared points,
certifies the explicit matrix witness with 256-bit Arb balls, checks the
Gaussian and fixed-sphere Schwarzian coefficients, recomputes the
Gamma/polygamma moments and endpoint jets at declared integer and noninteger
powers, checks anisotropy on finite grids for `p=1,2`, verifies the
quantitative bridge and finite-radius brackets at declared points, and replays
the empirical block bounds for three fixed seeds. It regenerates the figure
and JSON certificate.

Expected deterministic artifact hashes:

```text
saturation_law.pdf
093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97

saturation_certificate.json
b40a9bb318b48206fc0c5c9fc592c7b699d48a26b9b12b4ecc4805cf6215b9d1

finite_sample_resolution.pdf
b95dd92231aa7a9ca67fca0fcfa0293f4d4f627882a1afdfb3ec1d7efb3675a4

finite_sample_resolution.json
4bd3e130d11670c3a51d51ff0a4d962078ae415e95f4e90260e23da9293f9def

radial_phase_transition.pdf
147d9c23cd1349fcad8085c8cde21da8232527b91be9f655bc09e6424ffc05d2

radial_phase_transition.json
26ed3f0460847f79296301d5ecf087694358de819d976c671415762cc76c1d9a

spectral_lexicography.pdf
4d71aedc9ea8d0140c4eef5dd10d9882a71988b33fa3b4290ca79c52c51c15d1

spectral_lexicography.json
93d226200a59e3772b11ead7563eeed9e69a3a1d77951deacab97f4a5f7813c2

joint_spectral_resolution.pdf
1dd16ea599c78a46645a544641274b0e8236d7d2424572db932a5c25b68d4eb5

joint_spectral_resolution.json
a961a7b695707d24315473aa228e2690d2a84621cff286238cc3319276e4a493
```

The v3 replay additionally checks the explicit sample constants, matching
lower-bound coefficients, spherical radius constants, and the fixed-seed
finite-sample certificate. The numerical replay is diagnostic. The universal statements are proved
analytically in the paper.

The v4 replay checks the exact constants in all three inverse-radius phases,
the explicit Gaussian-product confidence constants, the order-statistic
constants in the spectral-lexicography theorem, deterministic quadrature for
isotropic Gamma radii, and fixed-seed finite-r convergence of the bottom
projector. These diagnostics do not replace the analytic proofs.

The v5 replay checks the deterministic finite-hierarchy projector certificate
and its closed logistic spacing envelope over a fixed sample and radius grid.
A separate verifier checks the joint-threshold constants, 117 random
sample-wise hierarchy certificates, and the asymptotic angular-process
variance for `p=1,2`. The joint probability theorem and intrinsic angular-log
obstruction are analytic; the replays do not replace their proofs.

For a byte-reproducible manuscript PDF, set:

```text
SOURCE_DATE_EPOCH=1788048000
FORCE_SOURCE_DATE=1
```

then change to `src/` and run `lualatex main.tex` three times. Running from the
manuscript root does not resolve the figure paths used by the LaTeX source.
