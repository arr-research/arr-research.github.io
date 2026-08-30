# Exact Stabilization by Additive GKLS Control Is Impossible at a Leaky Boundary

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0029](https://www.ai.vixra.org/abs/2607.0029)  
**First submitted:** 2026-07-12T23:00:29+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0029-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

The tangent cone of quantum state space at a rank-deficient density matrix is known to have a positive exterior block, and recent work identifies all of its directions with Lindbladian velocities. We derive a quantitative stabilization consequence of this geometry. Let rho be a finite-dimensional target with support projector P, set Q = 1 - P, and let an uncontrolled GKLS generator L have outward support-leakage rate a = Tr[Q L(rho)] > 0. Every additive GKLS controller, including a bounded time-dependent controller, has its own nonnegative outward rate at rho and therefore cannot cancel a. Consequently, no finite-rate additive Markovian controller can keep the system exactly at the target. The conclusion persists for arbitrary finite-dimensional autonomous ancillas, provided the adverse system generator remains additive and local to the system.Under induced trace-norm bounds ||L|| <= M and ||K_t|| <= Gamma, we prove the dynamic corridor inequality limsup ||rho_t - rho||_1 >= 2a/(M + Gamma), without assuming convergence to a stationary state. An autonomous Poisson-reset generator supplies a matching inverse-rate upper bound, establishing the order-optimal minimax law Theta(Gamma^{-1}).For a soft-filter dual-rail SSH family, the microscopic leakage coefficient scales as exp[-(2m + q)ell + o(ell)], whereas the ideal logical disturbance scales as exp[-4m ell + O(1)]. We derive the exact controller-growth threshold g_min = max{0, 2m - q}. Thus, below the filter threshold q = 2m, retaining ideal logical accuracy requires an exponentially growing autonomous correction intensity.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0029v1.pdf) — 2026-07-12T23:00:29+00:00
