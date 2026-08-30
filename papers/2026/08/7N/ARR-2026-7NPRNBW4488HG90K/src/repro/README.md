# Independent four-kick replay

Run from the Paper 28 root:

```text
python repro/run_replay.py
```

The runner executes two genuinely separate routes.  The Gram checker uses
only Python's standard library and performs all matrix and Gram calculations
with `fractions.Fraction`; its pseudorandom fixtures use a fixed seed.  The
constructor checker instead uses exact SymPy square roots and complex
Hermitian matrices.  Both JSON outputs are byte-deterministic, and the runner
fails closed if either frozen SHA-256 drifts.

It checks:

1. 160 balanced rational quadrilaterals in dimensions two and three (half
   general and half centrally symmetric), including the exact flux/diagonal
   identity;
2. the orthogonal-shear and Gram-determinant certificate needed for the
   corrected universal lower bound;
3. an exact noncommuting counterexample to the invalid intermediate
   inequality in the preliminary viability memo; and
4. one-spike square constructors for dimensions 1--12, plus repeated
   eigenvalues, sign reflection, and zero padding.

Expected output SHA-256:

```text
7095534026866159b37de40e2055b30ca9e765401a38f3fca4809bac2bf3d9cd  repro/results/four_kick_gram.json
b455b13c193dfbe101bf53632da046ff08575d507b7c104286470f9af0c35b5a  repro/results/symbolic_constructors.json
```

The package was frozen with Python 3.12.6, pypdf 6.4.0, and SymPy 1.14.0.
Install the pinned nonstandard dependencies with
`python -m pip install -r repro/requirements.txt` if needed.  `pypdf` is used
only by the release-container verifier; the rational replay itself remains a
standard-library implementation.
