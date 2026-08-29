# Verification record for ARR-2026-53CTRKDSP685PT51 v1

Date: 2026-08-29

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 307,076 bytes; SHA-256 `7e4716b232196b0b2f64892d180b32821d5c20c1924c3d948af0306c224d25dd`.
- PDF inspection found 11 A4 pages, no encryption, and no embedded JavaScript.
- All 11 pages were rendered with Poppler and visually inspected. Equations, the table, figure, references, page breaks, and margins are legible and complete.
- Three consecutive LuaLaTeX builds with `SOURCE_DATE_EPOCH=1787961600` and `FORCE_SOURCE_DATE=1` produced identical PDF bytes.
- `paper.md` and `paper.txt` were extracted mechanically from the exact canonical PDF; they are machine-reading renditions, not replacements for the mathematical typography.

## Numerical replay — pass within declared scope

The replay command completed successfully twice:

```text
python src/repro/verify_saturation_law.py
```

It reported:

```text
PASS: Loewner identity, Arb matrix witness, Schwarzian bridge, exact moments, monotone anisotropy, and finite-r bounds
figure_sha256=093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
certificate_sha256=17c83799f6581b5b602e29960b8660c15a186f36d2aedc225eb5c4d3f6ac8bc7
```

The figure and JSON hashes were stable across repeated runs. Arb at 256-bit precision certified the explicit indefinite matrix difference. The Loewner identity, bridge coefficients, monotonicity, and finite-radius inequalities are numerically checked only on the declared points or grids; the universal claims rely on the analytic proofs.

## Hostile audits

The retained V3 reports cover proof correctness, novelty, and primary literature. The proof audit accepted the bridge identity after one scope correction; the literature and novelty audits passed after explicit attribution to Cook–Hammerlindl–Tucker, Amari–Karakida–Oizumi, Chen–Mazumdar, and the version-specific adjacent work of Lam. The final post-audit edits implement those requested claim-boundary corrections and a bibliography layout adjustment.

These AI-assisted audits are evidence of adversarial checking, not independent peer review and not ARR protocol screening. ARR screening remains `not_assessed`.

## ARR labels and limitations

- Bibliography: **partial**. Primary links and directly overlapping sources were checked, but priority cannot be guaranteed absolutely.
- Reproducibility: **partial**. The replay and byte-rebuild passed, but the numerical grid is diagnostic and the analytic proof is not formally verified.
- Lean 4: **not applicable**. No formalization was supplied.
- Scientific scope: spectral functional calculus and isotropic Gaussian one-neuron models only; no claim about ordinary entrywise deep networks, global optimization, or non-Gaussian designs.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a technically valid founder-pilot publication, not independent editorial or scientific certification.
