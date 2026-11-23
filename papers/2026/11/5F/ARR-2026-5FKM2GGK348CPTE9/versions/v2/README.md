# A Wronskian Identity for Antisymmetrized Sine Sums: unconditional denominator positivity via circular convolution, sharp monotonicity distinctions, and counterexamples to naive sine-series principles (v2)

- **AIRR identifier:** `ARR-2026-5FKM2GGK348CPTE9` (`v2`, supersedes `v1`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`372457` bytes, SHA-256 `c0dbb3e9fe508cfbeb8cee993b7a08f8a74bd3dccac3d7f7668e266b5ccc1990`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/wronskian-reduction

## Revision Summary (v2)

Proves denominator positivity F_B > 0 on (0,pi) unconditionally via circular convolution, separates strict decrease from pointwise W < 0 and local near-pi negativity from global negativity with exact counterexamples, adds non-asymptotic Bessel decay and Fubini justification, and fixes proof typesetting.

## Scope & Disclosure

For real arrays (a_m) and (b_m) satisfying sum m(|a_m|+|b_m|) < infinity, we prove the exact Wronskian identity collapsing the antisymmetrized sine double sum to 2[F_a'(t)F_b(t) - F_a(t)F_b'(t)] with explicit Fubini justification. Applying this to the modified-Bessel arrays (A_m, B_m) of the companion two-dimensional lattice gauge surface-positivity problem, this v2 revision proves unconditionally for every beta > 0 that F_B(t) = -(f^{*4})'(t)/(2 I_1(beta)^4) > 0 on (0, pi) via fourfold normalized circular convolution of f(t) = exp(beta cos t), closing part (i) of v1's Conjecture 3 analytically, together with a non-asymptotic super-exponential Bessel decay bound. We separate precisely between strict decrease of the real-analytic ratio F_A/F_B (W <= 0 and W not identically zero), strict pointwise negativity W < 0 (strictly stronger, illustrated by F_a/F_b = cos^3 t with W(pi/2)=0), and local near-pi negativity (strictly weaker under generic side conditions, shown by a=(6,10,24), b=(6,5,2)), while retaining the exact counterexample a=(3,4,3), b=(3,2,1) to unrestricted sine-series Biernacki-Krzyz. The finite Wronskian identity is machine-checked in Lean 4/Mathlib; the global Bessel Wronskian negativity conjecture remains open.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
