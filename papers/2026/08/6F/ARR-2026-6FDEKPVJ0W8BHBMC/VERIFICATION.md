# Verification record for ARR-2026-6FDEKPVJ0W8BHBMC v1

Date: 2026-08-13  
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 476,279 bytes and has SHA-256 `f103ad4cc580704127d2696ccc18897695f9a7a4553357d9c4b74100621c1e8f`, matching the depositor-supplied values.
- PDF inspection found 14 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 14 rendered pages. The document is complete and legible, with one figure and two tables.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF. They are accessibility and machine-reading renditions, not replacements for the canonical mathematical typography.
- The frozen replay ZIP is 113,824 bytes and has SHA-256 `5bf74b40a90534c5ceff2ecfc7bacfefb05e6436928bae3a3fc52fbb465acb86`, matching the manuscript and delivery metadata.

## Reproducibility — partial

The four supplied Python commands completed successfully in 6.7 seconds on the ARR ingestion machine:

```text
python verify_grassmann_crossover.py
python verify_grassmann_spectral_switch.py --d 5 --r 2
python generate_d5r2_example.py
python verify_high_fidelity_grassmann_rdf.py --max-d 18 --order 128
```

Observed checks include:

- 1,558 exact weak/strong parameter pairs;
- equality of the Beta-moment and invariant `c2`/`c3` constants;
- complement antisymmetry and strong-field slope checks;
- the deterministic `d=5, r=2` comparator crossing;
- 81 exact high-fidelity cases through `d=18` and complement cases;
- equality of all three regenerated JSON outputs with the frozen JSON files, byte for byte.

This is labelled **partial**, not pass, because the scripts explicitly describe themselves as diagnostics and do not formally verify the paper's analytic global-optimality, nonanalyticity, or rate–distortion proofs.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no Lean formalization or kernel-checkable certificate was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
