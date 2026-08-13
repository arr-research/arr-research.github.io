# Reproducibility package

This lightweight package accompanies *Exact Rate--Distortion Theory for
Complex-Projective Born Prediction*. It contains two independent scalar
replays. Neither script is used as a proof.

## Requirements

- Python 3.12 or later
- NumPy
- SciPy
- Matplotlib

## Exact commands

Run from the directory containing the scripts:

```text
python verify_frontier.py
python verify_thermodynamic_limit.py --max-d 100 --output-dir .
```

The first command evaluates the exact finite-dimensional scalar max/sup
formula for dimensions 2, 3, 4, and 5. It writes
`frontier_verification.json`, `scalar_envelope.pdf`, and
`scalar_envelope.png`.

The second command evaluates the thermodynamic constants and the bounded
finite-dimensional first-contact problem up to dimension 100. It writes
`thermodynamic_diagnostics.json`, `thermodynamic_frontier.pdf`, and
`thermodynamic_frontier.png`.

Both runs use one process and bounded one-dimensional optimization. The first
enforces a 30-second ceiling and is configured below 64 MiB of numerical
arrays. The second refuses dimensions above 250.

## Scientific boundary

The JSON files and figures are deterministic diagnostics. They do not prove
the all-degree spectral extremum, the Gibbs/Danskin converse and achievability,
the thermodynamic Laplace principle, or the source-universal capacity theorem.
Those arguments are analytic and contained in the manuscript.
