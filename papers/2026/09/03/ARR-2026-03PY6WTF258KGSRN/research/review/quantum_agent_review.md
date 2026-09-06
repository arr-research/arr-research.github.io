# Separate internal review of the two-state routing manuscript

6 September 2026. Reviewer: the cycle-four quantum research agent, separate from the passive manuscript's constructing agent. Author: Lluis Eriksson.

**Outcome: PASS for the stated theorems after one small hypothesis correction.** I read the entire mathematical source and its proofs. I found no remaining mathematical issue that blocks the current statements. This is a separate internal agent review, not a human referee report or a formal verification.

Reviewed manuscript: `paper.md`, SHA-256 `a4d59c248eab267df4fcf746f0fc493fa77853a27aed1ab6259986290a0bc2d2`.

The source is titled *Two-state exact routing: algebraic feasibility and sharp delay-two rigidity*. Its general acute optimum is explicitly left open. The cubic construction is correctly stated as a globally certified attainable upper bound, and this review does not upgrade it to unrestricted optimality.

## Proof reading

1. **Arbitrary port count and exact degree.** A common polynomial denominator of degree at most two makes every component outside the two target rays vanish identically after its three distinct boundary zeros. The two remaining projective numerators cannot have degree below two: one must vanish at both repeated nodes and remain nonzero at the exceptional one. The primitive column therefore exhausts the full degree-two state budget. The containing square inner matrix has the same two determinant factors, including their multiplicities. No additional hidden determinant delay can fit within that budget. This justifies reduction of every achievable delay function to two ports, not only construction of some two-port examples.

2. **Monic spectral factor and stability.** The exceptional-node normalization yields a monic quadratic numerator for the exceptional component and a linear numerator for the repeated component. The absent cubic power coefficient forces the denominator's linear coefficient to be purely imaginary. The root calculation and connected-region argument establish exactly `Y>0` and `V>K^2`. The residual quadratic PSD condition is necessary and sufficient for a single complex linear numerator. Exact service prevents a numerator cancellation at either repeated node. The completion has determinant `h*/h`, is analytic in the correct half-plane, and has degree exactly two.

3. **Quartic cap and infinity.** The delay formula retains the translation-dependent angular factor. Multiplying by its strictly positive denominator makes a global cap equivalent to nonnegativity of the displayed quartic over all real coordinates. Its leading coefficient handles the point at infinity. The three-by-three Gram parametrization has the right coefficients, covers lower-degree degeneracies, and is equivalent to univariate nonnegativity. These polynomial constraints are not jointly convex in the design parameters; the source correctly says so. The quantifier-elimination statement is an in-principle algebraic computability assertion, not an efficiency estimate.

4. **Existence and delay-two locus.** A degree-two determinant has two nonnegative Poisson contributions and winding mean two. A fixed peak cap bounds both disk zeros away from the unit circle. The Potapov directions and constant unitary parameters are compact at fixed port count, so exact interpolation persists in a minimizing limit. The first two Fourier moments force both determinant zeros to vanish when the peak equals the mean. The elementary numerator maximum then gives precisely equal gaps at least a right angle. The provided factor realizes the entire stated equality locus, including its boundary.

5. **Quantitative gap and geometric lower bound.** The Fourier coefficients of the nonnegative defect are bounded by its mean, giving the stated bound on the first two zero moments and then the denominator's uniform distance from one. The numerator overshoot inequality has the correct normalization at the exceptional node. Splitting the proof at the case where the denominator bound reaches one is necessary and correctly done. The quadratic inversion gives the displayed positive gap. The Fubini–Study speed bound follows from the variance of a positive Wigner–Smith matrix and the half-range inequality; its integration and strictness argument agree with the degree-two mean.

6. **Acute construction.** The shifted cubic has exactly one positive root by its sign pattern, and the rational parametrization selects the correct root interval. The cap residual is a nonnegative square and vanishes at the two claimed peak locations. The improvement over the double-pole construction is strictly positive on the stated acute interval. For the named `w=11/5` example, I independently differentiated the delay as a function of `x=t^2` and obtained

   `-40 sqrt(11) (x-11) (7x+11) / (25x^2+66x+121)^2`.

   It is positive before 11 and negative afterwards on the nonnegative axis. The actual maximum is therefore exactly `9/sqrt(11)`, including comparison with zero and infinity, independently of the constructor's quartic-square identity.

## Correction made during review

The preceding source hash `de752c83dbc6778d97fd23705fd1ca6c4224602a67c144f2db76bb106442e777` described (15) as equivalent to (4) but did not explicitly retain `Y>0` in (15). Squaring `Y` in the remaining inequalities would otherwise admit the unstable sign. I requested its explicit inclusion; the constructor added it and reran the constructing checks. The final hash above contains the correction. A negative-`Y` test is included in the separate verifier. No other correction was required by this review.

## Independent computation

Run the following from the passive package directory:

```text
python review/quantum_agent_checks.py
```

The script requires SymPy and writes `review/quantum_agent_checks.json`. It verifies the frozen source hash before executing and does not import the constructing verifier or the numerical exploration.

All **144 checks passed**. They include three fixtures selected first by their actual upper-half-plane pole locations, then transformed directly to disk determinant zeros. The fixtures include a genuinely asymmetric denominator with unequal imaginary pole parts, a strictly positive residual power quadratic with `V>d^2`, and the delay-two attainment region. Exact boundary matrices and disk Poisson kernels are compared with the proposed delay formula at six rational boundary coordinates each. Endpoint routing, zero location, stability and residual-power negative controls are checked. The acute fixture is certified by its independently factored derivative. The general cubic is recovered from stationary differentiation. An algebraic expression for the numerator overshoot is separately checked:

`M = (sqrt((1+u^2)(1+v^2)) + abs(uv-1))/2`.

This expression confirms `M=1` exactly at `u=v<=1`; five exact fixtures check the gap inversion and its equality locus. The finite fixtures are supplementary to the universal proof reading, not a substitute for it.

## Scope and remaining limits

No PDF layout or visual audit is included in this report; the parent task handles that separately. I did not establish worldwide bibliographic priority, audit every cited source anew, perform proof-assistant verification, or prove the unrestricted symmetric acute optimum. Numerical searches in `exploration.json` were not used as evidence for a global theorem. No publication or external communication was performed by this reviewer.
