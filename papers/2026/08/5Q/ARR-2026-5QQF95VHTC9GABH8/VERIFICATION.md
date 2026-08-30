# Verification record for ARR-2026-5QQF95VHTC9GABH8 v1

Date: 2026-08-30

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 477,088 bytes; SHA-256
  `17b2361721027649b8ef5b98440032b91b5b04e89e2a9535fcbe7a27954ac1c5`.
- The final LaTeX and BibTeX logs contain no box, missing-character,
  unresolved-reference, or unresolved-citation warning.
- All eleven letter-sized pages were rendered with Poppler and visually
  inspected at high detail. No clipping, overlap, missing glyph, broken URL,
  or unreadable formula was found.
- `paper.md` and `paper.txt` are machine-readable renditions. The exact PDF
  and `paper.tex` remain authoritative.

## Exact scientific replay — pass within declared scope

The complete standalone command passed against the frozen 88-file tree:

```text
python -m pip install -r src/repro/requirements.txt
python src/repro/run_scientific_replay.py
```

Observed checks include all 33 sign-zero strata through dimension seven, 272
projected facets, 813 face generators, both orientations of 46 projected
equalities, the dependency-free dimension-eight witness, the complete
dimension-eight phase, the dimension-nine seed, exact order-18 and order-27
hive primal-dual certificates, and two independently implemented symbolic
coarse-grid transfers. The default replay finished with `PASS: complete
standalone Paper 32 scientific replay`.

The release ZIP was rebuilt twice from the frozen tree. Both copies had
SHA-256 `b3cbe79f237cbfd36d6dde1f7ed48896156576920d0cd629583dabb560c72e43`.
Its manifest has SHA-256
`7e5c660e1aef4953c8f0f669940c899d6d06b6d8f6d7d5757edd31b98ce92872`.

## Proof and literature boundary

The replay certifies exact finite Horn/polyhedral consequences and symbolic
hive coarse-graining conditional on the classical Horn/hive theorem. It does
not classify optimizer matrices or determine the exact value of `r_*(G_t)`.
The bounded bibliography audit compares adjacent 1986–2026 literature and the
two public ARR precursors. Bibliography is therefore labelled **partial**:
absence of a collision in a bounded search is not proof of priority.

## Reproducibility labels

- Bibliography: **partial**.
- Source integrity: **pass**.
- Reproducibility: **partial**, despite the complete exact replay, because the
  imported Horn/hive theorem and the analytic reduction are not formalized in
  a proof assistant.
- Lean 4: **not applicable**.
- PDF builds: visual/textual stability verified; byte determinism is not
  claimed because MiKTeX trailer metadata varies. The deposited hash is frozen.

## Conflict disclosure

The author and ARR founder-editor are the same person. This is a technically
validated founder-owned deposit, not independent peer review or a guarantee of
correctness or priority.
