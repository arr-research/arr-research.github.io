# Verification report

Record: `ARR-2026-7D2BBEC8MJ8BM80S v1`  
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 13 A4 pages, 483,920 bytes.
- SHA-256: `ee51663a977f1932da74670956aafe39e6f43ac355c6d27b472a4285a2b3fe34`.
- The deposited PDF is byte-identical to the final audited version 0.6 build.
- The final pdfLaTeX build completed without undefined citations or references, overfull or underfull boxes, or substantive LaTeX warnings.
- All 13 pages were rendered after the final proof-interface revisions and visually inspected for clipping, overlap, missing glyphs, and page-order defects.
- The embedded PDF title identifies the same work; its author field is blank and is not represented as an independent authorship check.

## Numerical and package reproduction — partial

`src/repro/replay.py` completed successfully and terminated with `REPLAY: PASS`. It checks both removable SU(2) character endpoints, the character Gram matrix, heat-semigroup multiplier arithmetic, the unique sharp mode, and a reflected quadratic form. The observed maximum errors were `0` at the endpoints, approximately `2.731e-14` for orthogonality, and approximately `6.939e-18` for multiplier composition.

The supplied release manifest was verified before deposit, the canonical PDF inside the supplied release was byte-identical to this PDF, and `git bundle verify` reported a complete history containing the two cited commits. The complete network-fresh `reproduce.ps1` driver was not run end to end during this deposit; dependency download and third-party cache availability remain environment-dependent. The reproducibility label is therefore `partial`, not `pass`.

## Lean 4 — L2

- Toolchain: `leanprover/lean4:v4.29.0-rc6`, preserved with the exact Lake manifest.
- Commit `05c4ec316cb9aa295416670a2578b1c2e77e1c36`: `lake build Lean2dYangMills.SU2ClassTransferGap` completed successfully with 2,817 jobs.
- Commit `6dbb8cebc18ab2d65b6ae24af5216347c476df3f`: `lake build Lean2dYangMills` completed successfully with 3,097 jobs, including the fixed-boundary physical disk endpoint.
- The supplied `#print axioms` audit reports only `propext`, `Classical.choice`, and `Quot.sound` for the four scalar-gap endpoints.

This supports Lean L2: source, successful builds, and an axiom audit are preserved. It is not Lean L3. Elementary subdivision invariance, the PL radial-cut reduction, the general compact-group disk collapse, and the full Hilbert-space assembly are paper proofs rather than one monolithic formal theorem.

## Bibliography — not assessed

The bibliography is preserved in the manuscript and as `references.bib`. ARR did not perform an independent bibliography, priority, or novelty assessment for this version.

## Screening and review — not assessed

No ARR frontier-model screening or independent peer review was performed. External manuscript feedback informed revisions before deposit, but it is not represented as ARR peer review or scientific certification. The author is ARR's founder-editor; this conflict is disclosed in `metadata.json`.
