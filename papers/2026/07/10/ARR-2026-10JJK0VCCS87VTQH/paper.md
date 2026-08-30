# A Machine-Checked Reflection-Positivity Framework for Z_N Lattice Gauge Theory, with the Z_2 Wilson Instance

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0073](https://www.ai.vixra.org/abs/2607.0073)  
**First submitted:** 2026-07-27T21:33:38+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0073-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We machine-check, in Lean 4 with no sorry and no project axioms, theOsterwalder-Seiler reflection positivity of a lattice gauge theory with finiteabelian gauge group. The development is organised so that the three ingredientsare separated and each is proved on its own: an analytic step, a geometric step,and the single place where a property of the Boltzmann factor is actually used.The analytic step is that a crossing kernel of the formK(x,y) = sum_i c_i phi_i(x) conj(phi_i(y)) with c_i >= 0 is positivesemidefinite, that this class is closed under products, and that it is closedunder conjugation by a positive diagonal. Formulating the hypothesis as anon-negative combination of characters rather than as non-negativity of Fouriercoefficients removes any need for Bochner's theorem on a finite abelian groupand for the Schur product theorem: the development uses no spectral and nomatrix-positivity API.The geometric step is a splitting of the configuration space across thereflection plane under which the reflection is the swap and the Gibbs weightfactors as w(x) w(y) K(x,y). We prove that the Osterwalder-Seiler pairing of anobservable of one half against its reflection is then exactly the quadratic formof w(x) K(x,y) w(y), so that reflection positivity follows from the analyticstep.The physical step is the instance. For Z_2 the Wilson factor exp(beta s),s = +-1, expands in the two characters with coefficients(exp(beta) +- exp(-beta))/2, both non-negative exactly when beta >= 0; so theZ_2 Wilson crossing kernel is positive semidefinite at non-negative coupling. Asingle endpoint combines a gauge system with a nontrivial time reflection, aconcrete splitting, that weight at positive coupling, and the conclusion; itsplaquette straddles the reflection plane, so the entire Gibbs weight is thecrossing kernel. It is a two-edge system, and a full temporal box is nottreated. For Z_N with N > 2 the coefficients are discrete Bessel-type sums andtheir non-negativity is not established here.We are explicit about what is absent: no Gelfand-Naimark-Segal quotient, notransfer operator, no identification of a Euclidean correlator with a matrixelement, and therefore no mass gap. Nothing here is a claim about SU(N), thecontinuum limit, or the Clay problem.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0073v1.pdf) — 2026-07-27T21:33:38+00:00
