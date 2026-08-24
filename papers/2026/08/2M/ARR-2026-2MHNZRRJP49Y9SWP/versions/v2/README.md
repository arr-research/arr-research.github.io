# ARR-2026-2MHNZRRJP49Y9SWP v2

This is a major revision of Lluis Eriksson's founder-owned ARR pilot record,
*The Exact Rank Floor for Point-Span Tangent Absorption in Arbitrary
Characteristic*. Version `v1` remains immutable and publicly addressable.

## Material revision

Version `v2` extends the exact binomial floor from characteristic zero to
smooth projective integral varieties over algebraically closed fields of
arbitrary characteristic. The positive-characteristic branch uses the
standard derivative/`p`-th-root argument for radical point ideals, explicitly
attributed to the planar observation of Bocci--Chiantini and to the
Zariski--Nagata differential-power literature. Proper-span sharpness remains
stated only over the complex numbers.

## Files

- `paper.tex` is the canonical LaTeX source. SHA-256:
  `1480283c47f0e25762353f3e032fb459f2091c036c5ce676dbe2ddd9fe70d0d4`.
- `paper.pdf` is the inspected 9-page A4 rendering. SHA-256:
  `af66e99f36e74234a53fa0ff3ba6895a84d14323b934e0faba252060079997ac`.
- `paper.md` and `paper.txt` are machine-readable renditions extracted from
  that PDF. Mathematical typography may be degraded; verify against the
  canonical source and PDF.
- `src/repro/` preserves exact-arithmetic Python replays, deterministic JSON
  results, the build report, release notes, research audit, referee report and
  clean final LaTeX log.
- `metadata.json`, `PROVENANCE.json`, `LICENSES.json`, `CITATION.cff`, and
  `VERIFICATION.md` describe this exact version. ARR generates
  `MANIFEST.sha256` for the immutable release bundle.

## Evidence labels

- Source integrity: **pass**.
- Exact projection-floor replay: **pass**, 20 rational fixtures.
- Exact common-tangent local replay: **pass**, 6 fixtures.
- Exact finite-field replay: **pass**, all 149 nonempty supports in
  `P^1(F_2)`, `P^1(F_3)`, and `P^2(F_2)` within stated degree cutoffs, plus two
  Frobenius-root fixtures.
- Fresh replay outputs match committed JSON byte for byte.
- ARR reproducibility: **partial**; the supplied exact fixtures were rerun,
  but no independent implementation or universal formal proof was supplied.
- Bibliography: **not assessed** under an ARR protocol.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Human peer review and priority certification: **not assessed**.

An independent read-only Codex referee found no P0. After corrections and a
focused re-review it scored the manuscript 8.4/10 with uncertainty 0.6 and
regarded the mathematics as publishable, while retaining priority uncertainty.
This is an AI audit, not peer review or certification.

The author is also ARR's founder-editor. This conflict is explicit in the
metadata. Publication records preservation and technical checks; it does not
independently certify correctness, novelty, or priority.
