# The Reconstructed Theory Has One Mass: a Machine-Checked Volume-Uniform Spectral Gap with Exact Identification Against the Gibbs Sums

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2608.0018](https://www.ai.vixra.org/abs/2608.0018)  
**First submitted:** 2026-08-05T21:39:01+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2608.0018-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

For the spatial Z_2 (Ising-slice) system inside the Dobrushin window 2 tanh|beta| + 2 tanh|gamma| <= alpha < 1, we machine-check in Lean 4 an end-to-end chain from the Gibbs measure to the spectrum of the reconstructed transfer operator. (i) The Osterwalder-Schrader (site-form) reconstruction of the transfer operator is unitarily conjugate, by the explicit sqrt(w) boundary dressing, to the symmetrised Dobrushin kernel. (ii) The unnormalised Gibbs sums themselves are exact matrix elements of that operator's powers: gibbsPathSum(w,beta,N,A,B) = lambda^N , with the partition function the same shape at the dressed constant. These are identities, not bounds, and they hold at every real beta and every positive weight. (iii) There is one mass m > 0 such that for every spatial extent L the projected operator norm is at most e^{-m} and every mixed connected correlator obeys | - | <= ||u|| ||v|| (e^{-m})^n, the zero-time case included. (iv) The connecte two-point function of the normalised Gibbs measure decays at that same rate with a constant independent of the time depth; dividing by the partition function is licensed by a denominator floor uniform in N, which the positive cone supplies and the spectrum does not, since the spectral route controls only the even powers. (v) The N -> infinity limit state exists, is the vacuum state of the reconstructed operator, and does not depend on the strictly positive observable terminating the chain. (vi) The reconstructed operator is a reversible Markov chain -- stochastic and in detailed balance for pi = Omega^2, both proved -- and in that stationary state the connected correlator of bounded observables obeys |E_pi[f P^N g] - E_pi[f] E_pi[g]| <= K_f K_g (e^{-m})^N, with quantifier order "there exists m, for all L": no factor depending on the spatial extent. Summing over time separations gives a susceptibility bound K_f K_g / (1 - e^{-m}), independent of the cut-off and of the extent. The window is non-empty at an interacting point (beta = gamma = 1/10, alpha = 1/2), machine-checked, so none of these conditionals is vacuous. The analytic input is inherited: the mass is the one the Dobrushin corollary already produced, and the window is not widened. What the reconstruction contributes is the identification, the exact identities, and the normalisation in which both the rate and the constant lose their dependence on the volume.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2608.0018v1.pdf) — 2026-08-05T21:39:01+00:00
