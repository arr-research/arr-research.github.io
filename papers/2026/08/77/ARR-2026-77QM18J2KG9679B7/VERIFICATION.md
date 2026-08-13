# Verification record for ARR-2026-77QM18J2KG9679B7 v1

Date: 2026-08-13
Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- The deposited PDF is 557,827 bytes and has SHA-256 `db6246f174d209eac2354b372af48649f1c55a9ced1d4ba9cdda59394aa8e668`, matching the depositor-supplied values and the PDF inside the reproducibility archive.
- PDF inspection found 23 A4 pages, no encryption, no forms, and no embedded JavaScript.
- Visual inspection covered all 23 rendered pages. The document is complete and legible, with four figures and two tables.
- `paper.md` and `paper.txt` were extracted mechanically from that exact PDF.
- The supplied reproducibility ZIP is 909,094 bytes and has SHA-256 `b409931a38b84ebb08f4672c8eb1d56a4679afc4495e951855317f1ee846c98a`.

## Reproducibility — partial

All three documented deterministic commands passed:

```text
python verification/finite_window_gap_certificates/verify_all.py
python verification/statistical_gap_boundary/certify_statistical_boundary.py
python verification/statistical_gap_boundary/verify_weighted_boundary.py
```

They verified exact recovery, the hidden-atom construction, the Chebyshev bound, archived ANNNI records for `L=6..16`, the statistical boundary certificate, and 2,000 deterministic polynomial competitors. The label remains **partial** because the scripts do not prove all analytic, statistical, and physical claims.

## Lean 4 — not assessed

The manuscript identifies commit `1e41144d7a563c12f89f9b2ad34fd90aa52149d8` of `lluiseriksson/lean-transfer-matrix` and limits the formal scope to the normalized endpoint hidden-atom mixture and its componentwise error bound. ARR retrieved the exact Lean source, axiom-audit file, toolchain, and pinned Mathlib revision and preserves them under `src/formal/`.

A local `lake build LeanTransferMatrix` attempt was stopped after 10 minutes because the initial Mathlib checkout had not completed and emitted no build result. Therefore ARR records **not assessed**, not L1: this version does not claim an independently reproduced kernel build. The source provenance remains available for a later verification-only update.

## Not assessed

- Bibliographic integrity: **not assessed**.
- Frontier-model screening: **not assessed**.

## Conflict disclosure

The author and current ARR founder-editor are the same person. No independent editorial or scientific assessment is claimed.
