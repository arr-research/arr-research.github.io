# Conditional Mutual Information and Petz Recovery in a Z2 Lattice Gauge Ground State

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2601.0111](https://www.ai.vixra.org/abs/2601.0111)  
**First submitted:** 2026-01-27T17:45:18+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2601.0111-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We study approximate quantum Markov structure in a Z2 lattice gauge ground state using the conditional mutual information (CMI) I(A:C|B(w)) and the performance of Petz recovery across a family of tripartitions (A, B(w), C) parameterized by a buffer width w. We consider a 2x4 plaquette lattice with open boundaries and qubits on links, restricted to a gauge-invariant (Gauss-law) physical sector, at coupling g = 1.0. For each w we compute reduced density matrices, the entropies entering the CMI, and a Petz-recovered state sigma_ABC = (id_A (x) R^Petz_{B->BC})(rho_AB), reporting fidelity F(rho_ABC, sigma_ABC) via the recovery error E_rec(w) = -log F. The Overleaf project includes the plot, a formatted table, raw CSV outputs, and a hash-based manifest; the appendix typesets raw artifacts. We also report numerical cross-checks (dense vs. low-rank method agreement and trace stability) to support validity. v2 (no v1 number is changed): the star-operator definition is corrected -- with the Hamiltonian convention used here (single-link Z terms), the Gauss stars must be G_s = prod Z_l; v1's printed prod X_l anticommutes with the Z_l terms of H (the code used the consistent convention: an independent reconstruction from the manifest alone reproduces the CSV ground energy to 7x10^{-15} and every CMI of Table 1 to machine precision); two interpretive remarks are added -- the CMI rise at w = 2 tracks the shrinking traced-out complement (|D|: 8 -> 2 -> 0), so the profile is not a shielding-decay curve, and the w = 2 ~ w = 3 plateau is the buffer-saturation identity of the companion 2601.0050 (v2); the apparent Petz-over-CMI excess at w = 1 (E_rec > I) is shown to be the delta = 10^{-6} regularization floor -- regenerating with delta = 10^{-12} restores E_rec <= I at every w in the regenerated dataset; and a verification suite replicates the full pipeline from the manifest data alone.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2601.0111v1.pdf) — 2026-01-27T17:45:18+00:00
- [v2](https://www.ai.vixra.org/pdf/2601.0111v2.pdf) — 2026-07-05T21:44:34+00:00
