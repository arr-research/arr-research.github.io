# A Wronskian Identity for Antisymmetrized Sine Sums: the surface-positivity problem as sine-series ratio monotonicity, and a counterexample to the naive monotonicity principle

- **AIRR identifier:** `ARR-2026-5FKM2GGK348CPTE9` (`v1`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`297473` bytes, SHA-256 `cb17dff7dd149534f3be05fc28c6b543eaf4a00d8409fcc80eb555946ec17452`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/wronskian-reduction

## Scope & Disclosure

For real arrays (a_m) and (b_m) (finitely supported, or summable with sum m(|a_m|+|b_m|) < infinity), we prove the exact two-line identity collapsing the antisymmetrized double sum sum_{1<=m<n} (a_m b_n - a_n b_m)[(m-n)sin((m+n)t) + (m+n)sin((n-m)t)] to the Wronskian 2[F_a'(t)F_b(t) - F_a(t)F_b'(t)] of the sine series F_x(t) = sum_m x_m sin(mt). Consequently, the open surface-positivity problem of the companion modified-Bessel phi-lemma note is equivalent (conditioned on F_b > 0) to global strict monotonicity of a ratio of two explicit sine series on (0, pi). We refute a naive Biernacki-Krzyz analogue for sine series via a hand-checkable counterexample: a = (3,4,3), b = (3,2,1), strictly increasing coefficient ratios (1,2,3), F_b(t) = 2 sin(t)(2 cos^2(t) + 2 cos(t) + 1) > 0 on (0, pi), yet W(2 pi/3) = 3 sqrt(3)/2 > 0. The finite Wronskian identity (arbitrary K) is machine-checked in Lean 4/Mathlib with zero sorry and standard axioms only; nothing beyond the identity and exact algebraic counterexamples is claimed.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed for this working-paper deposit. Exact-PDF frontier-model assessments are recorded in `registry/model-assessments.json`.
