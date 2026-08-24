# Verification record for ARR-2026-2MHNZRRJP49Y9SWP v3

Date: 2026-08-24

Protocol: `ARR-VERIFY-1.0`

## Source integrity — pass

- Canonical `paper.tex`: 32,873 bytes; SHA-256
  `1480283c47f0e25762353f3e032fb459f2091c036c5ce676dbe2ddd9fe70d0d4`.
- Rendered `paper.pdf`: 429,891 bytes; SHA-256
  `af66e99f36e74234a53fa0ff3ba6895a84d14323b934e0faba252060079997ac`.
- PDF inspection found 9 A4 pages. The three-pass MiKTeX log contains no
  LaTeX warnings, undefined references, or overfull/underfull boxes.
- All 9 pages were rendered and visually inspected for cropping, overlap,
  missing glyphs, unreadable mathematics, and broken layout.
- `paper.md` and `paper.txt` were mechanically extracted from this exact PDF.
- The clean final log is preserved at `src/repro/paper.log`.

## Exact replay — pass

The deposited runner was executed:

```text
python src/repro/run_all_replays.py
```

It regenerated every JSON result in a temporary directory and required
byte-for-byte agreement with the committed files. Version v3 explicitly opens
JSON outputs with `newline="\n"`; this removed the CRLF/LF host dependence found
by rerunning the downloaded v2 release on Windows. The corrected runner passed
there with all regenerated files identical to the committed LF files.

- Projection-floor replay: 20/20 exact rational fixtures passed, covering
  `1 <= d <= 4`, `1 <= m <= 5`, up to `binom(d+m,d)=126`, plus deleted-node
  falsification boundaries.
- Common-tangent replay: 6/6 exact local fixtures passed, checking equal value
  and double-point ranks and the second-order normal-coordinate mechanism.
- Perfect-field replay: all 7 nonempty supports in `P^1(F_2)`, all 15 in
  `P^1(F_3)`, and all 127 in `P^2(F_2)` passed within the stated degree
  cutoffs; two explicit Frobenius-root fixtures in characteristics 2 and 3
  also passed.

## ARR reproducibility label — partial

ARR reran the supplied exact fixtures and checked their deterministic JSON
outputs. The scripts are diagnostic witnesses, not the universal proof. No
independent implementation, global computational smoothness certificate, or
formal proof was supplied. The public label is therefore `partial`, not
`pass`.

## Independent Codex audit — not protocol screening

A separate read-only Codex referee found no P0. It initially scored the draft
7.6/10 with uncertainty 0.8, requested attribution and exposition corrections,
and on focused re-review scored the corrected mathematics 8.4/10 with
uncertainty 0.6. The report is preserved at
`src/repro/EXTERNAL_CODEX_AUDIT.md`. This is not `ARR-SCREEN-1.0`, human peer
review, formal verification, or priority certification.

## Not assessed and limitations

- Bibliographic integrity under an ARR protocol: **not assessed**.
- Frontier-model screening under `ARR-SCREEN-1.0`: **not assessed**.
- Lean 4: **not applicable**; no formalization was supplied.
- Human peer review, independent reproduction, novelty, and publication
  priority: **not assessed**.
- The exact theorem is restricted to smooth projective integral varieties over
  algebraically closed fields and nonempty finite reduced supports.
- No descent to imperfect fields is claimed.
- Proper-span sharpness is retained over the complex numbers only.
- The Bertini construction proves existence; the replay checks local algebra
  and does not certify global smoothness of a particular explicit member.

## Conflict disclosure

The author and ARR founder-editor are the same person. No independent
editorial or scientific certification is claimed.
