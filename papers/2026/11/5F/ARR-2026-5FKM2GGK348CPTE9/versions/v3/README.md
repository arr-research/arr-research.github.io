# A Wronskian Identity for Antisymmetrized Sine Sums: unconditional denominator positivity via circular convolution, sharp monotonicity distinctions, and counterexamples to naive sine-series principles (v3)

- **AIRR identifier:** `ARR-2026-5FKM2GGK348CPTE9` (`v3`, supersedes `v2`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`375255` bytes, SHA-256 `515233f29284deab2ba873718e8006bae1167ec20a9be5b05394841035d2cefd`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/wronskian-reduction

## Revision Summary (v3)

v3 resolves all minor polish notes from gpt-6.2-sol on v2: adds the explicit second sign evaluation W(pi/2) = -32 < 0 in Proposition 8 alongside W(2pi/3) = 3*sqrt(3) > 0 to prove nonmonotonicity with two opposite signs, explicitly starts the r_{k-1} consequence in Lemma 3 at k >= 1 with explicit O_beta decay rates, completes the Bessel implication diagram, labels Remark 10 digit counts as empirical heuristics, and pins the exact repository release and commit hash.

## Scope & Disclosure

For real arrays (a_m) and (b_m) satisfying sum m(|a_m|+|b_m|) < infinity, we prove the exact Wronskian identity collapsing the antisymmetrized sine double sum to W(t) = 2[F_a'(t)F_b(t) - F_a(t)F_b'(t)] with explicit Fubini justification. Applying this to the modified-Bessel arrays (A_m, B_m) of the companion two-dimensional lattice gauge surface-positivity problem, we prove unconditionally for every beta > 0 that F_B(t) = -(f^{*4})'(t)/(2 I_1(beta)^4) > 0 on (0, pi) via fourfold normalized circular convolution of f(t) = exp(beta cos t), together with non-asymptotic super-exponential Bessel decay bounds. We establish the exact implication chain in the real-analytic Bessel family while showing via exact finite counterexamples that generic reverse implications fail: F_a/F_b = cos^3 t (W(pi/2)=0), a=(6,10,24), b=(6,5,2) (near-pi negative yet W(2pi/3)=51*sqrt(3)>0), and a=(3,4,3), b=(3,2,1) (non-monotone via two opposite signs W(pi/2)=-32<0 and W(2pi/3)=3*sqrt(3)>0). The finite Wronskian identity is machine-checked in Lean 4/Mathlib (release yang-mills-archive-v1.0); the global Bessel Wronskian negativity conjecture remains open.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed. Exact-PDF OpenRouter assessments (`openai/gpt-6.2-sol` and `anthropic/claude-opus-4.8`) are recorded in `registry/model-assessments.json`.
