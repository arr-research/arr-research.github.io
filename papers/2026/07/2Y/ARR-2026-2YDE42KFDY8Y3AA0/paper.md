# The Vacuum Was Never Absent: A Machine-Checked Perron Theorem for Strictly Positive Kernels, and the Coupled-Slice Vacuum at Every Spatial Extent

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0085](https://www.ai.vixra.org/abs/2607.0085)  
**First submitted:** 2026-07-29T06:36:35+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0085-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Two companion papers established, for a Z_2 lattice gauge slice with a spatialcoupling, that the elementary route to the vacuum stops, and that the naturalreplacement - the Hilbert projective metric - is blind to the coupling anddegenerates in the volume. Both had to work around the same absence: the pinnedmathlib carries no Perron-Frobenius theorem. The first paper could therefore onlysay the vacuum had become unavailable; the second had to build its dominationbound from scratch, and could exhibit the vacuum in closed form only at two sites.This paper discharges that dependency. For a strictly positive kernel on a finitenonempty type we prove, in Lean 4 with mathlib: a strictly positive eigenvectorEXISTS; its eigenvalue is strictly positive; any two strictly positiveeigenvectors are proportional and share their eigenvalue; and every realeigenvector for that eigenvalue is a scalar multiple of it. Together with thedomination theorem of the companion paper this gives the Perron statement thelane needs: the eigenvalue is the spectral radius.The existence proof does not use a fixed-point theorem, because the pinnedmathlib revision contains none. It maximises r over the compact set of pairs(r,x) with x in the simplex and r x <= A x; maximality forces equality, since astrict inequality anywhere would let one further application of A produce anadmissible pair with a larger r. The bound that keeps the set compact is obtainedby summing the constraint: r = r * sum x <= sum (A x).The application is the point. At EVERY spatial extent, and for EVERY strictlypositive weight on the source configuration - the class that contains the coupledkernel of the first paper - the vacuum exists, is unique up to scale, and carriesthe spectral radius. The obstruction of that paper was never an absence; it wasan unavailability, and it was an unavailability of one route rather than of theobject.NO SPECTRAL GAP IS PROVED HERE, uniform in the volume or otherwise, and none isclaimed. Nothing in this paper is a claim about SU(N), the continuum limit, orthe Yang-Mills mass gap.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0085v1.pdf) — 2026-07-29T06:36:35+00:00
