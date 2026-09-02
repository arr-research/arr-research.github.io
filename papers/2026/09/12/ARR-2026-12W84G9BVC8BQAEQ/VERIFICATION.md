# Verification record for ARR-2026-12W84G9BVC8BQAEQ v1

Date: 2026-09-02

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 21,272 bytes; SHA-256
  `3fe985b56fb83278d16fbbf55975a77d4964b87311ef4490c74fea8766b7fe1a`.
- All seven A4 pages were rendered with Poppler 26.05.0 at 140–160 dpi and
  visually inspected. No clipping, overlap, missing content, or unreadable
  table was found.
- `paper.md` and `paper.txt` are machine-readable renditions; the frozen PDF
  is the canonical rendered artifact and the Python builder is the source of
  truth.

## Exact replay — pass within declared finite scope

From a clean extraction, `MANIFEST.sha256` had zero mismatches. The following
standard-library commands passed under Python 3.12.6:

```text
python -I replay/verify_exact_frontier_p21_p32.py
python -I replay/verify_p53_independent.py
python -I replay/verify_p53_exact_endpoint.py
python -I replay/verify_p53_endpoint_nogo.py
python -I replay/verify_lr_frontier_bundle.py
```

The first command checks twelve exact primal hives, twelve matching
unrestricted duals, and twelve strict predecessor-rank duals. The independent
p=53 replay reconstructs all hive row and variable indices separately from the
primary verifier. The Farkas replay proves the former trace-8843 integer
candidate infeasible. Optimized Python is explicitly refused.

The deterministic release ZIP has SHA-256
`a241d2a82059cdfbd922cd5808ed339ab6d549385150fa7efb7f396a7e9478c9`.

## Boundary

The replay verifies exact finite Horn/hive consequences conditional on the
classical Horn--Klyachko theorem and hive model. It does not prove an all-p
recurrence, classify all optimizer matrices, or formalize the imported theorem
in a proof assistant. Bibliographic comparison is partial, not exhaustive.

## Labels

- Bibliography: **partial**.
- Source integrity: **pass**.
- Reproducibility: **partial** because the imported analytic and Horn/hive
  reductions are not formally verified end to end.
- Lean 4: **not applicable**.
- Screening/model assessment: **not assessed**.

## Conflict disclosure

The author and ARR founder-editor are the same person. This is a technically
validated founder-owned deposit, not independent peer review or a guarantee of
correctness or priority.
