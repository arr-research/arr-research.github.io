# Verification record for ARR-2026-53CTRKDSP685PT51 v2

Date: 2026-08-29

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 386,279 bytes; SHA-256 `32bd46179e26475b5563666f2fc4a1230fdb5fcd77643db8d6f7850963952d90`.
- PDF inspection found 17 A4 pages, no encryption, suspects, or embedded JavaScript.
- All 17 pages were rendered with Poppler and visually inspected. Equations, theorem blocks, the priority table, figure, references, page breaks, and margins are legible and complete.
- Four settled LuaLaTeX builds with `SOURCE_DATE_EPOCH=1787961600` and `FORCE_SOURCE_DATE=1` produced identical PDF bytes.
- `paper.md` and `paper.txt` were extracted mechanically from the exact canonical PDF; they are machine-reading renditions, not replacements for the mathematical typography.

## Numerical replay — pass within declared scope

The replay command completed successfully twice:

```text
python src/repro/verify_saturation_law.py
```

It reported:

```text
PASS: Loewner/Arb witness; spherical and quantitative bridge grids; all-p moment/endpoint test points; p=1,2 anisotropy grids; three fixed-seed empirical block realizations; and finite-r brackets
figure_sha256=093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97
certificate_sha256=a5442d5840a08ed1394e21f8f4d82f7947ba35ba7bd6cc5e9cf00d4df0c3618a
```

The figure and JSON hashes were stable across repeated runs. Arb at 256-bit precision certified the explicit indefinite matrix difference. The replay checks only declared points, grids, and three fixed empirical realizations; it does not calibrate theorem probabilities or replace the analytic all-p, concentration, angle, or lower-bound proofs.

## Hostile audits

The retained V5 reports independently cover proof correctness, algebra/replay scope, and current primary literature. Mandatory fixes added a quantitative empirical gap for the angle rate, dominated endpoint remainders, a sixth-moment scope clarification, exact replay wording, and priority citations to Ostrovskii--Bach, Fisher et al., Ojo--Olapade, Chardon v3, and Chen--Mazumdar. Differential re-audits close with ACCEPT/PASS and no unresolved critical objection. Earlier V3 reports are retained only as version-lineage history.

These AI-assisted audits are evidence of adversarial checking, not independent peer review and not ARR protocol screening. ARR screening remains `not_assessed`.

## ARR labels and limitations

- Bibliography: **partial**. Primary links and directly overlapping sources were checked, but priority cannot be guaranteed absolutely.
- Reproducibility: **partial**. The replay and byte-rebuild passed, but the numerical grid is diagnostic and the analytic proof is not formally verified.
- Lean 4: **not applicable**. No formalization was supplied.
- Scientific scope: the empirical and global saturation results remain Gaussian and pointwise at a fixed teacher. The spherical theorem is local only. There is no claim about ordinary entrywise deep networks, global optimization, a matching `Omega(rd)` lower bound, or a minimax estimator theorem.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a technically valid founder-pilot publication, not independent editorial or scientific certification.
