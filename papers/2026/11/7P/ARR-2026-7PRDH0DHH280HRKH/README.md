# From the Gibbs Weight to the Spectral Gap: A Complete Machine-Checked Osterwalder-Seiler Chain for the Z_2 Lattice Gauge Chain

- **AIRR identifier:** `ARR-2026-7PRDH0DHH280HRKH` (`v1`)
- **Record type:** `research_paper`
- **Canonical artifact:** `paper.pdf` (`117363` bytes, SHA-256 `8b52725dfa42a40b119b4dc4a34dd4b5b326fc11bca2cd008dfa384f3675f3c4`)
- **Source repository:** https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/yang-mills-archive-v1.0/papers/os-chain-z2

## Scope & Disclosure

A mass gap is a statement about the spectrum of an operator, whereas a lattice gauge theory is specified by a measure. This paper reports a complete formal verification in Lean 4 with mathlib of the Osterwalder-Seiler reconstruction passage for the Z_2 lattice gauge chain: from the Boltzmann weight exp(beta s) through reflection positivity, the Gelfand-Naimark-Segal space, the normalized transfer operator, and the identification theorem to the exact two-point correlation E_n[f(sigma_0)f(sigma_n)] = (tanh beta)^n, with verified non-vacuum eigenvalue tanh beta, spectral gap 1 - tanh beta > 0, and mass -log(tanh beta) > 0 for beta > 0. The underlying mathematics is textbook; the contribution is a machine-checked end-to-end composition proving that every interface composes without hidden assumptions. Limits are stated explicitly: one Z_2 variable per time slice (2x2 transfer operator, no spatial extent), fixed finite size (not volume-uniform), definite pairing (trivial GNS quotient), and no claim regarding SU(N), the continuum limit, or the Yang-Mills mass gap.

Author Lluis Eriksson owns and administers AIRR (`airr.science`); accordingly, no independent editorial admission or human peer review is claimed for this working-paper deposit. Exact-PDF frontier-model assessments are recorded in `registry/model-assessments.json`.
