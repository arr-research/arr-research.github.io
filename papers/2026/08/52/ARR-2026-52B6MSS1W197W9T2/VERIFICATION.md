# Verification record for ARR-2026-52B6MSS1W197W9T2 v1

Date: 2026-08-13
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 375,083 bytes and has SHA-256 `b18ba2f0f56cc8934b95454f4e145b15b19b0b82b463e7de93fb55ac420e0c89`.
- The hash and byte count match both the supplied file and the asset in GitHub Release `v2.8-ai-vixra-submission`.
- PDF inspection found 9 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 9 rendered pages. The document is complete and legible, with one figure and two tables.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF.

## Reproducibility — partial

The release identifies frozen source commit `1d9fb43692c1a5ef07ffc90775e0726ee1882183`. An archive of that exact commit was used, not the current working tree. Both paper-specific independent verifiers passed:

```text
python verification/verify_unified_routing_table_memory.py
python verification/verify_detector_rank_hierarchy.py
```

The checks validate the occupancy law fixtures, a fresh direct-sum dual construction, canonical certificate digests, detector-rank cases, and declared numerical tolerances. The label remains **partial** because executable fixtures and numerical checks do not prove the complete analytic interpolation theory.

## Not assessed / not applicable

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.
- Lean 4: **not applicable**; no formalization was supplied.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
