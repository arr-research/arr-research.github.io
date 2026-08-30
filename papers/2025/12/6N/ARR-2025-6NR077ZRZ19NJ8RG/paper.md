# Beyond Gaussianity: Extending the Clustering-Recovery Bridge

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2512.0101](https://www.ai.vixra.org/abs/2512.0101)  
**First submitted:** 2025-12-31T01:06:02+00:00 (source displays no timezone)  
**Latest declared source version:** v2  
**ARR mirror:** [v2 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2512.0101-v2.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We formulate a non-Gaussian, finite-volume and uniform-in-Lambda version of the Clustering-Recovery bridge for interacting lattice systems. We introduce an explicit collar geometry, a CMI formulation via Fawzi-Renner, and an operational (Heisenberg-picture) quasi-locality strengthening for the recovery map. Version 2 corrects one identity: v1's "CMI as relative entropy" equation equated I(A:C|B) with the relative entropy to the normalized Markov-product state; the exact identity holds for the unnormalized product M = exp(log rho_AB + log rho_BC - log rho_B), and the normalized version underestimates the CMI by -log Z >= 0 (Z <= 1 by Lieb's triple-matrix inequality). We also fix the Fawzi-Renner factor: with the squared-fidelity convention used throughout, the bound is I(A:C|B) >= -log F (not -2 log F). All numerical claims of v1 (Petz slope table; prefactor-slope trade-off; crossover w*=3) have been independently reproduced from scratch by a NumPy-only verification script that ships with this paper.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2512.0101v1.pdf) — 2025-12-31T01:06:02+00:00
- [v2](https://www.ai.vixra.org/pdf/2512.0101v2.pdf) — 2026-07-05T06:24:25+00:00
