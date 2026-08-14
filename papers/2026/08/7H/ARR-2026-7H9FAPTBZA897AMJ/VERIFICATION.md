# Verification record for ARR-2026-7H9FAPTBZA897AMJ v2

Date: 2026-08-14

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 441,916 bytes and has SHA-256 `f8bd2e9ed5f8b166e014dd7b51578adc572dd603b37a82c1fde837b7d89488be`.
- PDF inspection found 16 A4 pages, one vector figure, no encryption, no forms, and no embedded JavaScript.
- All 16 rendered pages were visually inspected at 120 dpi. The title page, central coefficient theorem, uniform Gamma-tail lemma, figure/reproducibility section, and bibliography were additionally inspected at full resolution.
- The LaTeX/Biber build completed with no undefined citations or references, LaTeX/package warnings, or overfull/underfull boxes.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The deposited LaTeX, bibliography, vector figure, replay programs, frozen JSON diagnostics, and replay hash manifest were copied from the frozen author release and independently rehashed during ingestion.
- Version 2 has a new version identifier and explicitly supersedes version 1 while retaining the same permanent ARR record identifier.

## Reproducibility — partial

The declared self-contained replay command completed successfully on the ARR ingestion machine:

```text
powershell -ExecutionPolicy Bypass -File src/replay/replay_all.ps1
```

Observed checks include:

- 6,783 exact rational coefficient-sign checks;
- 297 exact boundary-tail checks;
- zero mismatches in the coefficient/binomial-reduction screen;
- exact tail-ratio and shifted-polynomial identities over the declared finite ranges;
- scalar coexistence diagnostics through `q=120`;
- deterministic figure generation; and
- verification of every artifact listed in `src/replay/REPLAY_ARTIFACTS.sha256`.

This is labelled **partial**, not pass, because the programs are bounded diagnostics. The all-dimensional coefficient law, uniqueness, no-reentrance, rate–distortion, and asymptotic claims depend on analytic proofs in the manuscript and are not independently formalized.

## Version and related-record scope

- Version 2 supersedes `arr:version:26cebded-ef67-454b-9922-75e69fc8b139`, the earlier all-field draft under the same public identifier.
- `ARR-2026-61Y0FFA39M8KMBJ5` remains a related complex rank-two companion, not a prior version and not the same research object.
- The present work concerns signed Pluecker-coordinate compression, not quantum rate–distortion, Born-probability prediction, or a derivation of Born's rule.

## Not assessed / not applicable

- Bibliographic integrity under ARR protocol: **not assessed**.
- Frontier-model screening: **not assessed**.
- Peer review: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable certificate was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
