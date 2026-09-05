# Separate internal review of the exact LP certification wrapper

Reviewer: cycle3_quantum research agent, 5 September 2026. This agent did not construct the commutator algorithm or its certificates. This is a bounded internal AI review of `certified_constant.py` and the stored `optimal_constant_N4_d8.json`, not external refereeing. The previously reviewed N=4 manuscript was not reread.

**Disposition:** no substantive error found in the Horn conversion, the removal of the last spectrum coordinate, the dual signs, or the exact acceptance checks. The stored N=4, d=8 report passes an independent rational replay. Its coefficient is exactly 4/7.

## Mathematical formulation

For a common decreasing nonnegative spectrum s of two positive matrices R,S, the ordered spectrum of -S is (-s_d,...,-s_1). The Horn inequality for R+(-S), with target spectrum lambda, is

\[
 \sum_{i\in I}s_i-\sum_{j\in J}s_{d+1-j}
                  \ge \sum_{k\in K}\lambda_k.                 \tag{1}
\]

This agrees with the conventional decreasing-eigenvalue form in Fulton's primary exposition, Section 1, inequality (*IJK): [primary PDF](https://arxiv.org/pdf/math/9908012). The trace equality is automatic here: the construction has sum(a)=sum(b)=1, so sum(lambda)=0, while the two summand spectra have opposite sums.

Fixing s_d=0 loses no optimum. Given any feasible ordered nonnegative s, subtract s_d from every coordinate. At the matrix level this replaces R,S by R-s_d I,S-s_d I; positivity and their difference are preserved, and the objective decreases by d s_d. At the inequality level both sets I,J have the same size, so the translation cancels from every Horn row. Thus an optimum may always be chosen on this face.

The production row builder then has the correct indexing: `i<d` retains +s_i, while `j>1` retains -s_(d+1-j) at zero-based position `d-j`. The omitted terms are exactly the fixed s_d terms. Its ordering rows impose s_i>=s_(i+1) for i=1,...,d-2. The missing final ordering relation is s_(d-1)>=s_d=0 and is supplied by the nonnegative variable bounds. The target spectrum a, zeros, -reversed(b) is decreasing, including boundary zeros.

## Exact primal and dual witnesses

Write the reduced primal as min 1^T s subject to Ls>=r and s>=0. The code passes -L,-r to SciPy's upper-inequality interface. The corresponding exact dual is max r^T y with y>=0 and L^T y<=1. Therefore negating the reported inequality marginals is the correct sign convention.

The primal proposal is rationalized, then every component is checked nonnegative without a tolerance. A common denominator for the entire proposed spectrum and right-hand side turns all row tests into exact Python-integer comparisons. There is no machine-integer overflow in these checks and no rounded residual is accepted as zero.

For the dual, every retained rational weight is checked nonnegative. The code reconstructs L^T y and checks its components are at most one. The residual 1-L^T y is exactly the weight available on the nonnegative-variable inequalities. It need not reconstruct the solver's lower-bound marginals. Nor is a lower bound on L^T y required: the necessary condition is precisely L^T y<=1.

The resulting exact certificate is the weak-duality identity

\[
  \boldsymbol 1^Ts
   =y^TLs+(\boldsymbol 1-L^Ty)^Ts
   \ge y^Tr.                                                   \tag{2}
\]

Both nonnegativity conditions and primal feasibility are checked rationally. The final exact equality `sum(s)==objective` therefore proves optimality of the accepted proposal. A solver success flag alone is never sufficient for acceptance.

The filter `abs(marginal)<1e-9` affects only which candidate dual terms are proposed. Dropping a term can change the exact bound or break dual feasibility, particularly because a Horn row may have negative coefficients. The code subsequently recomputes and checks the complete surviving rational dual and exact objective equality, so either the filtered tuple is still a valid certificate or the run stops. The filter cannot promote an approximate equality or inequality into a certificate. The same reasoning covers denominator-limited rationalization: a modified proposal can pass only if it independently satisfies the exact conditions.

## Independent JSON replay

The reviewer wrote `algorithm_certificate_replay.py`. It does not call a solver, import `certified_constant.py`, or reuse that file's reduced row construction. It checks the stored witnesses with the full d-coordinate formula (1), reconstructs each dual linear form in full dimension and only then removes the fixed last coordinate. The Horn generator and the cell geometry remain the dependencies that had already received separate review.

The replay passed in approximately two seconds and recorded `algorithm_certificate_replay.json`:

* 48 primal/dual certificates cover all 89 ordered vertices after the a,b sign symmetry.
* All 8,752 Horn triples were reconstructed and all 420,096 full-dimension primal inequalities passed exactly.
* All 152 stored dual terms have valid indices and nonnegative rational weights; every residual and objective was reconstructed exactly.
* Every spectrum is decreasing and nonnegative, with last entry zero. Every listed cost, distance and nonzero-distance ratio agrees exactly with its formula.
* The single zero-distance representative has exact cost 5/2 and is correctly excluded from division.
* The minimum ratio is 4/7, attained by the stored boundary pair a=(5/8,1/8,1/8,1/8), b=(1/2,1/2,0,0). Its common spectrum is (3/4,1/2,1/8,1/8,0,0,0,0), giving cost 3/2 and distance 7/4.

The inspected source hash is `3850e6efc8d570aff94bd9fdee53e4927a0c745ab001768353aa4435d0bf3ffd`; the inspected certificate hash is `9290e0b6e8038f9ff9715b797c230675a4b2b668d6f45e9a24c834f8a4b4642f`. The replay source hash and all finite check counts are retained in its JSON.

## Limits retained

The wrapper is a checked floating-proposal implementation. Its own documentation correctly says it can stop if rationalization fails; it does not implement an exact rational LP oracle guaranteed to return a certificate for every input. The exact certificates prove the listed finite LP optima. The general cell reduction, Horn sufficiency and passage from finite vertices to the claimed global stability coefficient are the separately reviewed mathematical dependencies, not consequences of floating solver convergence. No further change is required for the inspected certification logic.
