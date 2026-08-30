# The Volume-Uniform Poincaré Walls: Machine-Checked Obstructions for Flat and Fluctuation-Sector Block-Poincaré Routes to Combes—Thomas Coercivity in Lattice Yang—Mills

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0042](https://www.ai.vixra.org/abs/2607.0042)  
**First submitted:** 2026-07-14T13:24:23+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0042-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Inside a Lean 4 formalization programme for four-dimensional SU(Nc) lattice Yang—Mills, we report two machine-checked negative results and the machine-checked infrastructure that makes them meaningful. The positive substrate is: (i) a fixed-volume Combes—Thomas chain for self-adjoint coercive finite-range lattice operators, instantiated on the flat gauge-fixed covariance of the physical shell, with coercivity constant c = min(1,a)/C_P fed by a proved fixed-volume flat Hodge/block-Poincaré inequality; and (ii) the concrete adjoint model of SU(n) — su(n) with the trace inner product, dim_R su(n) = n² − 1, and the isometric transport to Euclidean coordinates — so that the abstract adjoint-model interface has a concrete nontrivial inhabitant and the flat-lane results can be instantiated with the genuine matricial adjoint model. The first wall states that, under the block normalization actually used by the formalized chain, every flat Hodge/block-Poincaré constant obeys L^d/L² ≤ C_P on the fine torus of side LNu2032, hence the volume-uniform Poincaré gate is provably false for d ≥ 3 and Nc ≥ 2, and no positive coercivity constant survives all volumes through this route. The route consumed by the fixed-volume endpoint is therefore closed by theorem. A second wall stands in the fluctuation sector. For d ≥ 3 and a transported half-period square-wave mode on the exact fine side (2M)Nu2032, the formalization proves ||QA||² ≤ (2M)u207b¹||A||², the exact identity = 8((2M)Nu2032)u207b¹||A||², and therefore a Rayleigh numerator at most 9(2M)u207b¹||A||². Every quotient Poincaré constant is thus at least 2M/9, so the volume-uniform fluctuation-sector gate is also provably false for every positive Nu2032, d ≥ 3, Nc ≥ 2, and every adjoint model. Everything stated here is checked by Lean 4 against a pinned Mathlib, with zero sorry, zero project axioms, and a committed axiom-oracle transcript. A dependency record, theorem-artifact map, and reproduction instructions expose the complete proof chain. Both walls concern the current unscaled line-integral block map with the current unweighted coarse norm; neither gate is claimed to be necessary, equivalent, or exhaustive for Yang—Mills theory. No claim toward a continuum construction or a mass-gap theorem is made.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0042v1.pdf) — 2026-07-14T13:24:23+00:00
