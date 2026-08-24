# Verification report

- Record: `ARR-2026-3H0ZKWJMH18MH9FX v1`
- Protocol: `ARR-VERIFY-1.0`
- Canonical PDF SHA-256:
  `bf67bc3c4ae3f0b191c375691c375b93f9fdb3b70ce7f16f031bcb905324e16f`
- Canonical PDF size: `447420` bytes
- Canonical PDF geometry: 12 A4 pages
- Supplied reproducibility ZIP SHA-256:
  `abedc7b8fb8e84514e5a70c7574110efebeee0e7139224b6885aabd805099738`

## Checks performed

1. Recomputed the canonical PDF SHA-256, byte count, page count, title,
   authorship metadata, and A4 page geometry.
2. Compiled the preserved LaTeX source with MiKTeX `pdflatex` and `bibtex`.
   The final log contained no unresolved citations or references, undefined
   control sequences, overfull boxes, or underfull boxes.
3. Rendered all 12 pages with Poppler and visually inspected them for clipping,
   overlap, broken equations, malformed tables, missing text, and bibliography
   layout. No visual defect remained in the deposited PDF.
4. Ran `verify_full_spark_list_threshold.py --check`: **PASS**. It checks
   harmonic tight/full-spark fixtures, weighted Hodge identity resolution,
   unequal-norm strictly scalable Parseval examples, constructive compression
   to at most `r^2` outcomes, consecutive- and arithmetic-support thresholds,
   divisor fixtures, exact rank-two Weyl Bayes curves and covariant POVMs,
   the spectral error floor, the perturbation inequality, and counterexamples
   separating full spark from strict scalability.
5. Repeated write/check/write replay generation. The frozen certificate was
   byte-identical across runs with SHA-256
   `e535a8eb8e5d3eca086463a95e07ba8d182c6556acbc80f713ef7c1b50dc96f9`.
   The certificate schema records a rounded residual and threshold assertion
   instead of environment-dependent last-ulps floating output.
6. Built and verified the 17-file deterministic supplied archive. Its final
   SHA-256 is the value above. ARR independently packages the preserved pure
   files and canonical PDF in its immutable release.
7. Performed a targeted primary-source priority audit covering the direct
   learning-width/factor-width result, factor-width rank, exclusion SDPs,
   scalable and full-spark frames, exterior/cross-product tight-frame facts,
   group and optical exclusion, and dense-coding probe dependence. Exact-phrase
   and formula searches did not locate the paper's narrow result combination.
   This was not a complete ARR bibliography protocol or specialist novelty
   review.
8. Obtained a separate Codex-task assessment after source revision. It gave
   critical model feedback and a score under the requested scale; it is
   preserved under `src/audits/` but is not counted as ARR screening, peer
   review, or independent scientific evidence.

## Evidence labels

- Source integrity: **pass**.
- Reproducibility: **partial**. The executable evidence covers exact finite
  fixtures and formula identities; it does not formally prove all universal
  analytic theorems.
- Bibliography: **partial**. Targeted primary-source checks were performed,
  but no complete database or specialist audit is claimed.
- Lean 4: **not applicable**; no formalization was supplied.
- Frontier-model screening: **not assessed**.
- Peer review and independent scientific validation: **not assessed**.

ARR publication records technical preservation and the checks above. It is
not an independent finding that every theorem or novelty claim is correct.
