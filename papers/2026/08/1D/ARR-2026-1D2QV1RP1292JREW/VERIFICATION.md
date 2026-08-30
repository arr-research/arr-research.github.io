# Verification record for ARR-2026-1D2QV1RP1292JREW v1

Date: 2026-08-30

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical PDF: 455,967 bytes; SHA-256 `106e6011a9506b6f64ac04fdc6d991e11bae7db3b4bf7c76cad33825e2190337`.
- PDF inspection found nine A4 pages, no encryption, and no embedded JavaScript.
- Poppler rendered every page at 150 dpi; all nine pages were visually inspected.
  Equations, theorem boxes, table, references, page breaks, links, and margins are
  legible and complete, with no clipping or overlap.
- Two consecutive pdfTeX builds completed without undefined references, undefined
  citations, or overfull boxes. PDF byte identity across toolchains is not claimed.
- `paper.md` and `paper.txt` were extracted mechanically from the exact canonical
  PDF and are machine-reading renditions, not replacements for its typography.

## Exact-arithmetic replay — pass within declared scope

The standard-library replay completed in isolated Python:

```text
python -I src/repro/verify_extremal_tax.py --max-d 20 --output src/repro/verification.recheck.json
```

It reported:

```text
PASS: exact zero-padded one-spike upper/lower match for every rank in d=2..20
PASS: all flat two-sign adjacent-swap checks
PASS: free-module weighted-shift identity and exact block-order averages
```

The script uses explicit failures and deliberately rejects `python -O`. It checks
weighted-shift algebra, exact block-permutation averages, strict adjacent-swap
deficits, and summed one-spike Horn bounds. These finite computations audit
algebra and indexing; they do not prove the arbitrary-dimensional theorem.

## Proof and literature audits

The retained proof audit found no counterexample after correcting rank notation,
attainment, floor removal, Horn indexing, and zero padding. The final manuscript
also writes out the convention-sensitive subset-to-partition map and the exact
Littlewood--Richardson unit coefficient. Primary bibliographic records directly
adjacent to the topic were checked and added, including Fong, Maher,
Filonov--Safarov, Gil, and Zhang. The bibliography remains **partial**: exhaustive
priority is neither possible nor claimed.

Two independent version-locked frontier audits of earlier candidates found no
material objection and requested only bounded clarifications. The frozen v1 PDF
incorporates all of them: Fong's corrected title, balanced units for Weiss's
example, an explicit kernel-support step in Proposition 3.1, the permanent ARR
path and SHA-256 of the replay, and literal nonzero hypotheses where the objective
is defined. Because those edits changed the canonical hash, ARR did not reuse an
earlier score; the final artifact is assessed separately under the exact hash
above.

## ARR labels and limitations

- Bibliography: **partial**. Directly overlapping primary sources were checked,
  but absolute priority is not certified.
- Reproducibility: **partial**. The replay and clean extraction pass, but the
  analytic proof and imported Horn theorem are not formalized.
- Lean 4: **not applicable**. No formalization is supplied.
- Scientific scope: finite-dimensional matrices with the unnormalized
  Hilbert--Schmidt norm. No general interior formula, upper-endpoint stability
  modulus, operator-norm result, infinite-factor theorem, or physical resource
  model is claimed.

## Conflict disclosure

The author and ARR founder-editor are the same person. The deposit records a
technically valid founder-owned publication, not independent editorial or
scientific certification.
