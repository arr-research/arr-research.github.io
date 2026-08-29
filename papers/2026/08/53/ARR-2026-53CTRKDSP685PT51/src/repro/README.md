# Reproduction

Run from the manuscript root:

```text
python -m pip install -r repro/requirements.txt
python repro/verify_saturation_law.py
```

The replay checks the closed logistic Loewner determinant at declared points,
certifies the explicit matrix witness with 256-bit Arb balls, checks the two
logistic Schwarzian-bridge coefficients, recomputes the sensitivity moments,
tests positivity and monotonicity on a declared grid, verifies the finite-radius
brackets, and regenerates the figure and JSON certificate.

Expected deterministic artifact hashes:

```text
saturation_law.pdf
093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97

saturation_certificate.json
17c83799f6581b5b602e29960b8660c15a186f36d2aedc225eb5c4d3f6ac8bc7
```

The numerical replay is diagnostic. The universal statements are proved
analytically in the paper.

For a byte-reproducible manuscript PDF, set:

```text
SOURCE_DATE_EPOCH=1787961600
FORCE_SOURCE_DATE=1
```

and run `lualatex` twice on `src/main.tex`.
