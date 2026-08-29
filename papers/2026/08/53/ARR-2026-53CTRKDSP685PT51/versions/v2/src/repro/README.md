# Reproduction

Run from the manuscript root:

```text
python -m pip install -r repro/requirements.txt
python repro/verify_saturation_law.py
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
```

The numerical replay is diagnostic. The universal statements are proved
analytically in the paper.

For a byte-reproducible manuscript PDF, set:

```text
SOURCE_DATE_EPOCH=1787961600
FORCE_SOURCE_DATE=1
```

and run `lualatex` three times on `src/main.tex`.
