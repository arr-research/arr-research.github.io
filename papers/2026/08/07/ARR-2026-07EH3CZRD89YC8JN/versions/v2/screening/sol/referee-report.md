# Referee report: Lossless Calibration Is Stored Memory

## Recommendation and score

**Recommendation:** Accept  
**Score:** 4.4/10 (strong on the supplied scale)  
**Overall stars:** 4/5

I read all 16 pages of the exact deposited PDF with SHA-256 `341c673d6613533931cbc0fc817cf946d178e390cde818221c19b33c304a4167`. I found no material mathematical defect. The paper is correct, carefully qualified, and unusually reproducible. Its principal limitation is novelty: the proof combines classical inner-function factorization, determinant multiplicity, minor-degree bounds, and the Wigner-Smith phase-volume identity, and it acknowledges close overlap with the author's preceding routing and reservoir manuscripts. Within that boundary, the protected signal/loss formulation and near-optimal application form a coherent and useful contribution.

## Main theorem and proof assessment

Theorem 4.1 is valid. Boundary unitarity gives

`G(zeta)^* G(zeta) + C(zeta)^* C(zeta) = I`,

so the lossless calibration subspace is exactly `ker C(zeta)`. At a strict stop, `||G(zeta_*)|| < 1`, hence `C(zeta_*)^* C(zeta_*)` is positive definite. Therefore `C(zeta_*)` has full column rank, `ell >= m`, and a fixed `m x m` row minor `C_I` is nonzero. At each calibration node, the calibration subspace lies in the kernel of this same minor. Lemma 3.1 then gives determinant-zero multiplicity at least `k_j`; distinct nodes let these multiplicities add. Lemma 3.2 bounds the total finite zeros of any nonzero minor by the full McMillan degree. This proves `sum k_j <= n` without changing the selected rows from node to node.

The local determinant lemma is elementary and correct, including nongeneric rank defects. The exterior-power proof of Lemma 3.2 is also sound under the manuscript's analytic-disc convention: a minimal degree-`n` square inner function has `n` rank-one Blaschke-Potapov factors; the induced factor on an exterior power again has a common scalar denominator of degree at most `n`, so any reduced entry, equivalently any minor, has numerator degree at most `n`. The alternative realization proof makes the same budget plausible without relying solely on factorization notation.

The strict-stop hypothesis is logically necessary. If the protected block is isometric everywhere, then the complementary loss block can vanish identically and degree-zero transparent wiring admits arbitrarily many nominal calibrations. The manuscript states this counterexample explicitly.

## Wigner-Smith law

The sign convention in Theorem 5.1 is consistent with the analytic-disc choice: for the elementary delay `S(z)=z`, `Q=-i S^* dS/dtheta=1`. The product rule `Q_AB=B^*Q_A B+Q_B` preserves positivity and trace additivity. Each degree-one factor contributes a Poisson-kernel rank-one term of integral `2 pi`, which yields

`(2 pi)^(-1) integral tr Q = wind det S = n`.

The subsequent peak bounds follow directly from a maximum being at least the average and from `tr Q <= N lambda_max(Q)` for positive semidefinite `Q`. The continuous-frequency map is properly qualified: the dimensionless unit-circle result becomes a physical time-delay statement only after fixing the Mobius frequency map.

## Sharpness, robustness, and six-port application

The sharpness construction in Proposition 6.1 is exact. The balanced `2m`-port completion has signal and loss blocks `(1+z^M)I/2` and `(1-z^M)I/2`; it has `M` calibration nodes of charge `m`, a perfect stop, determinant winding `mM`, and constant trace delay `mM`.

Theorem 7.1 correctly invokes Rouche's theorem only on pairwise-disjoint, pole-free closed regions with a strict boundary margin. It preserves the complex zero count of one fixed loss minor, which is enough for the degree lower bound even though the perturbed zeros need not stay on the physical boundary. Proposition 7.2 is also correct: a degree-one scalar all-pass can produce an arbitrarily dense collection of approximate pass samples in a small arc while retaining a perfect stop elsewhere. Thus no degree theorem can depend only on the number of unseparated approximate samples.

For the six-port family, direct calculation confirms that `U_rev(z) U(z)=z^2 I`, so at each root of `B_g-1`, the stated direction `v=U(z)e_g` is lossless and acquires the common phase `z^2`. The three root sets are disjoint. The determinant factorization gives exact McMillan degree `3S+6`, calibration charge `3S`, and an additive-six gap from the universal optimum. At `z=-1`, the phase offsets mean the stop is strict rather than exactly zero; this agrees with the reported stop norms and loss determinants. The imported irreducibility result uses `3(S-1)` selected full-spark nodes from the larger set of `3S` roots and its stated stop bound is below one for `S>=5`, so the application is internally consistent.

The delay formula `tr Q_S(theta)=6+3S(1-r_S^2)/|e^{i theta}-r_S|^2` has integral `3S+6` and peak `6+3S(2e^{alpha S}-1)`. The exponentially high peak is a property of this sharply concentrated construction, while the universal theorem only forces the integral and a much weaker peak lower bound. The manuscript maintains that distinction.

## Physical interpretation

The rate discussion is appropriately conditional. For a stationary input spectrum `j_- I <= J <= j_+ I`, a lossless input direction maps to a unit output direction and preserves at least `j_-` in the congruence `GJG^*`; a stop with `||G||<=epsilon` has rate norm at most `j_+ epsilon^2`. This is a deterministic transfer-matrix consequence once the weak-coupling Markov model is assumed. The paper does not claim a universal conversion from degree to energy or thermodynamic work, and its limitations section correctly excludes active, time-varying, infinite-dimensional, and non-Markovian escape routes.

## Reproduction and falsification

The documented replay was executed from a scratch copy with Python bytecode disabled. Both the generator and corrected validator exited zero; the input hashes remained unchanged. It regenerated all six listed orders, including 57 calibration zeros and degree 63 at `S=19`, and reproduced the reported strict stops, adaptive Wigner-Smith integrals, perturbation contours, and random-minor campaign.

I also wrote and ran a separate audit. Its final exact-arithmetic stage checked 228 minors of rational 3-by-3 Potapov products with one through five noncommuting rank-one factors and found no reduced numerator exceeding the factor-count budget. Direct six-port checks at `S=5,9,19` found all `3S` roots, unitarity residuals below `1.2e-14`, strict-stop signal norms `0.05268`, `0.008711`, and `9.68e-5`, integral values `21`, `33`, and `63`, and the stated peaks. A degree-one construction achieved 100 samples above `0.9999992` while having a perfect stop, reproducing the negative result for unstructured approximate samples.

The first audit run failed. Its failures were traced to two harness errors: it measured the unreduced determinant numerator before cancelling the shared denominator, and it used an incorrect sign in one assembled six-port block. That run is retained. A second floating-point reduction exposed severe cancellation conditioning, so the final minor test was replaced by exact rational arithmetic. These are test-harness failures and limitations, not evidence against the manuscript.

The numerical evidence does not constitute a formal proof, a continuous contour certificate, authentication of historical execution provenance, or an independent minimal state-space/Smith-McMillan computation. The analytic arguments carry those claims.

## Novelty and literature boundary

The primary literature supports the manuscript's attribution of the underlying machinery. Alpay, Jorgensen, and Lewkowicz characterize rational para-unitary functions through realizations and Blaschke-Potapov products parameterized by McMillan degree. Tabak and Mabuchi interpret degree-one Blaschke factors as cavity modes in passive quantum networks with delays. Gough and Zhang give the passive quantum linear-system realization setting. Wigner and Smith establish the phase-derivative/lifetime framework. Ball and Kang treat low-McMillan-degree tangential interpolation. These sources make clear that factorization, degree counting, and lifetime matrices are prior art.

The strongest new claim is therefore the protected-block consequence: exact isometry on arbitrary node-varying input subspaces creates complementary-loss nullity, one strict stop supplies a single nonzero minor, and the total nullity is forced below full-network degree and integrated delay. The coefficient-sharp family, qualified analytic robustness, and additive-six irreducible application strengthen this package. I regard this as a strong synthesis and application rather than a foundational new factorization or delay theorem.

## Nonmaterial observations

No correction is required for validity. Two small presentation refinements would help a future version:

1. Add a compact dependency table marking which claims are proved here, imported from the earlier reservoir paper, or classical. Section 11 contains this information in prose, but a table would make the novelty boundary easier to audit.
2. Where Section 10 says "independent polynomial root count," qualify that this means a distinct computational method within the same supplied package, not independent provenance or an independent reviewer execution.

## Sources consulted

- Daniel Alpay, Palle Jorgensen, and Izchak Lewkowicz, *Characterizations of rectangular (para)-unitary rational functions*, arXiv:1410.0283 / Opuscula Mathematica 36 (2016): https://arxiv.org/abs/1410.0283
- John E. Gough and Guofeng Zhang, *On realization theory of quantum linear systems*, arXiv:1311.1375 / Automatica 59 (2015): https://arxiv.org/abs/1311.1375
- Gil Tabak and Hideo Mabuchi, *Trapped Modes in Linear Quantum Stochastic Networks with Delays*, EPJ Quantum Technology 3:3 (2016): https://doi.org/10.1140/epjqt/s40507-016-0041-9
- Eugene P. Wigner, *Lower Limit for the Energy Derivative of the Scattering Phase Shift*, Physical Review 98 (1955): https://doi.org/10.1103/PhysRev.98.145
- Felix T. Smith, *Lifetime Matrix in Collision Theory*, Physical Review 118 (1960): https://doi.org/10.1103/PhysRev.118.349
- Joseph A. Ball and Jeongook Kang, *Matrix polynomial solutions of tangential Lagrange-Sylvester interpolation conditions of low McMillan degree*, Linear Algebra and its Applications 137-138 (1990): https://doi.org/10.1016/0024-3795(90)90145-3
- John E. Gough and Matthew R. James, *The Series Product and Its Application to Quantum Feedforward and Feedback Networks*, IEEE Transactions on Automatic Control 54 (2009): https://doi.org/10.1109/TAC.2009.2031205

No other assessment, score, coordinator history, or candidate report was consulted. No incidental assessment-report exposure occurred.
