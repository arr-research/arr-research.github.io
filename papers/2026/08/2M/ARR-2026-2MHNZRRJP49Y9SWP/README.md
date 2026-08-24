# ARR-2026-2MHNZRRJP49Y9SWP v1

This is a founder-owned ARR pilot record for Lluis Eriksson's research paper,
*The Exact Universal Rank Floor for Point-Span Tangent Absorption: Projection,
Fattening, and Common-Tangent Extremizers*.

## Files

- `paper.tex` is the canonical LaTeX source. SHA-256:
  `bdf18f2ca24b31b71259436e441f10ed90a013588df38a40af08a954e8f28b28`.
- `paper.pdf` is the inspected 9-page A4 rendering. SHA-256:
  `235bf613b5f3a1f9f7a81a6d4d0f0f027cadc7564d37f77643edfbd8a8cae7cd`.
- `paper.md` and `paper.txt` are machine-readable renditions extracted from
  that PDF. Mathematical typography may be degraded; verify against the
  canonical source and PDF.
- `src/repro/` preserves exact-arithmetic Python replays, deterministic JSON
  results, build instructions, release notes, and the separate Codex audit
  summary. The clean final LaTeX log is preserved in the release bundle.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, `CITATION.cff`, and
  `VERIFICATION.md` describe this exact version. ARR generates
  `MANIFEST.sha256` for the immutable release bundle.

## Evidence labels

- Source integrity: **pass**.
- Exact projection-floor replay: **pass**, 20 fixtures.
- Exact common-tangent local replay: **pass**, 6 fixtures.
- ARR reproducibility: **partial**; the supplied exact fixtures were rerun,
  but no independent implementation or global computational smoothness
  certificate was supplied.
- Bibliography: **not assessed** under an ARR protocol.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Human peer review and priority certification: **not assessed**.

A separate read-only Codex task found no fatal mathematical error, scored the
manuscript 6.60/10 on the author's requested scale, and confirmed “publish”
after minor revisions. This is an AI audit, not peer review or certification.

The author is also ARR's founder-editor. This conflict is explicit in the
metadata. Publication records preservation and technical checks; it does not
independently certify correctness, novelty, or priority.
