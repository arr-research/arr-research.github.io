# Independent internal review of the complete one-state error–delay law

Reviewed on 5 September 2026 by the inventory/review agent, separately from the agent that derived the passive manuscript. **Outcome: PASS after corrections; no unresolved mathematical objection within the stated model.** This is an independent internal agent review, not external refereeing, a proof-assistant certification, or a finding of bibliographic priority.

The reviewed source is `active_delay.md`, SHA-256 `690c4ce5b76f5d05a29e4f93ce6409e8f142187c1e5699c5713f1d1b7c4209ea`. The deriving agent's `verify_active_delay.py` has SHA-256 `d7c4293aba1fb98a526c2a569e45ff61249dc92cf4506ea79348578ecc7dd398`. The complete predecessor `outputs/cycle2/passive/asymmetric_delay.md` was read; its SHA-256 is `2e8aec0da0fd691fa7b91fb1ec01a9460695a5bab27c3d8ed7e382ef76b2e052`. All sections of the new manuscript and the full verifier were read. The later LaTeX conversion and final corrections were inspected. The last source delta changes the review-status sentence and correctly handles the inequality at $q=0$.

## 1. Model, reduction, and auxiliary ports

The conclusion concerns disk rational-inner matrices of McMillan degree at most one, one fixed input, phase-free chordal node errors, and the **angular trace-delay peak** defined in the manuscript. It is not a claim about an arbitrary physical delay convention, fixed output phases, or higher-degree networks.

The imported degree-one Blaschke–Potapov structure makes the nonconstant determinant a scalar Blaschke factor, with peak at least one. Thus the constant branch for $0\leq T<1$ is necessary. Its lower bound $1/2$ follows from the squared overlaps with the two orthogonal targets summing to at most one; the stated constant unitary attains it.

The Cayley coordinate and normalization of $H(s)=s^2+2Bs+C$ are valid: a stable scalar denominator is nonzero at the node represented by infinity. The eigenvalue-ratio condition gives the stated ellipse, including its singleton $M=I$ at $T=1$. Direct support optimization gives $A(t)$, $B_t$, and $C_t$ in (6). In particular the support point is unique for every real $t$, also in the singleton case.

For any number of ports, $Q$ is the intensity of the second output and $P=H-Q$ includes all other outputs. The desired first-output node errors imply the two endpoint inequalities for $Q$. These are necessary even when unused outputs carry intensity, so both lower certificates apply to every port count. Conversely, any globally nonnegative real quadratic is the squared modulus of one complex linear polynomial: for $R=as^2+2bs+c$, $a>0$, use

\[
\sqrt a\left(s+\frac ba+i\frac{\sqrt{ac-b^2}}a\right);
\]

if $a=0$, positivity forces $b=0$, and use the constant $\sqrt c$. Factoring $P$ and $Q$ separately therefore supplies a two-output column. The completion in Section 6 makes this converse global. No rank-one assumption about an unknown optimum or restriction on complex numerator coefficients enters the lower bound.

## 2. Inactive branch and the exact transition

The Lagrange identity for the leading coefficient of an arbitrary quadratic yields the old bound $e_L=(2+F(t_*))^{-1}$. Uniqueness of the stationary point follows by differentiating the numerator of $F'$: $A''D+2A>0$ on the node interval, with opposite endpoint signs. The symmetric case has $t_*=0$; for $u>v$, the sign comparison places it strictly between $m=(v-u)/2$ and zero.

At equality, the candidate $Q=(1-e_L)(s-t_*)^2$ and the unique supported denominator are forced. Expanding the residual gives

\[
\det P=\frac{F(u-B)(B+v)}{F+2}.
\]

Here $B>m$ when $u>v$, whereas $B=m=0$ when $u=v$. Thus positivity is exactly $B\geq-v$. Strict failure cannot leave the old value attained; the normalized feasible quadratic set is compact, and the equality conditions force the infeasible residual.

The active boundary calculation correctly uses $\tau=-pv/\sqrt{q^2-v^2}$ only when the square root exists and the stationary-root comparison lies in the node interval. If $\tau\leq-u$, comparison is immediate without substituting an exterior point into an interval argument. For $q\leq v$, the bound $B_t\geq-q\geq-v$ handles the entire region, including $q=0$. For $v<q\leq\sqrt2v$, the remaining sign is negative. For larger $q$, substitution at $\tau$ gives exactly the numerator whose zero is $U_c(v,q)$.

Writing $w=\sqrt{q^2-v^2}>v$ gives a useful independent monotonicity check:

\[
\frac{U_c}{v}=\frac{2[1+\sqrt{1+(v^2+1)/w^2}]}{1-v^2/w^2}-1.
\]

This decreases strictly from infinity to three. Consequently there is one finite transition precisely when $u>3v$. The radical formula selects the larger root of the squared equation. The retained unsquared sign is $(u-v)Q-2uv^2>0$; the transition polynomial is negative both at $2v^2$ and at the zero of this sign expression. Its larger root has the required sign, while the other root is extraneous. Thus squaring has not added a phase.

## 3. Active branch and the positive dual

Put $x=e/(1-e)$, $d=(u+v)/2$. The relation $L=d(1-x)/\sqrt x$ gives the proposed zeros

\[
t=v-L\sqrt x,\qquad r=v+L/\sqrt x.
\]

Expansion of $Q_0+P_0$ gives $(s-v)^2+L^2$, the cap-supporting denominator. The two endpoint ratios are $x$ and $-x$, and the leading coefficients give the error at infinity. This proves feasibility at all frequencies, not merely at the three test nodes. The branch condition is equivalent to $\sqrt x\geq v/w$, hence $t\leq\tau$.

The dual weights in (18) satisfy all three moment equations of (19) and the first-moment support identity (20). They were independently recovered by solving these linear equations, rather than copied as assumed identities. Their signs have an analytic proof: $h-\tau>0$, $\nu\geq0$, $\mu>0$, and $\lambda_->0$. In particular, direct simplification gives

\[
\lambda_+=\frac{r+t-2\tau}{2(h-\tau)}>0,
\]

because $t+r>2v>0>2\tau$. This also proves $\lambda_0>0$. The strict active phase has $\nu>0$; it vanishes at the boundary.

The coefficient of $H(\tau)$ is $e+\nu>0$, so ellipse support gives the correct inequality direction in (21). Its equality constant is $\lambda_0(1-e)$, checked independently. For an arbitrary feasible value $\varepsilon<e$, the moment identity and the nonnegative terms $P(r),Q(t)$ then imply

\[
(e-\varepsilon)(\lambda_0+W)\leq0,
\]

where $W>0$. This is a global lower certificate and closes the region that the predecessor explicitly left open. It does not require the unknown $P,Q$ to have rank one. Positivity of the node weights forces all node constraints at equality. Support uniqueness and $Q(t)=0$, together with its leading coefficient, determine $H,Q$, including at the boundary where $\nu=0$. The uniqueness claim is correctly restricted to $T\geq1$.

## 4. Compiler and edge cases

The corrected compiler uses a degree-zero constant unitary for $T<1$. This distinction is operationally necessary: applying the degree-one sharp completion to constant column polynomials would produce determinant $z$ and peak one. The original interface exposed exactly this problem; the author corrected it and added explicit constant-cap cases. The independent checker records both determinants and the correct constant unitarity.

For either nonconstant optimizer, the scalar factors satisfy the global identity $p_zp_z^\sharp+q_zq_z^\sharp=h_zh_z^\sharp$. The denominator coefficients obey $|h_0|^2-|h_1|^2=4\Delta>0$, proving absence of closed-disk poles. Formula (23) is therefore inner, with determinant $h_z^\sharp/h_z$, degree exactly one, and the claimed analytic peak. The cap ellipse is saturated by both branches. The case $h_1=0$ is included: its determinant has a zero at zero and peak one. The numerator factors cannot have a common zero because $P(t)=H(t)>0$. Constant unitary changes of bases and identity padding establish the claimed arbitrary-input, arbitrary-port realization.

The isolated inactive root, its unsquared sign, and the separate symmetric and $T=1$ cases make the algebraic compiler well specified. The numerical implementation uses high precision and root isolation as a computational supplement; its floating-point tolerances are not the proof of positivity for arbitrary parameters.

The following limits are consistent with the formulas and the predecessor: $T=1$ at all gaps; $u=v=c$ giving $c^2/(T^2+2c^2)$; absence of a finite transition at $u=3v$; the stated divergence of $T_c$ as $u\downarrow3v$; the fixed-$T>1$ limit as $v\downarrow0$; and error tending to $1/2$ as $u\to\infty$ at fixed cap. Boundary-node limits are limits of the stated positive-gap problem, not an enlargement of its hypotheses. The high-delay active expansion was checked by direct symbolic series. Subtracting the inactive expansion gives the positive coefficient $d^2(u-3v)^2/(4T^4)$, as claimed; these expansions hold at fixed gaps and need not be uniform under simultaneous parameter scaling.

## 5. Independent exact replay and resolved findings

`independent_review_checks.py` neither imports nor executes the deriving agent's verifier. It uses SymPy exact arithmetic and independently parameterized rational points on the active hyperboloid. Its report is `independent_review_checks.json`.

- Eight groups of universal symbolic identities passed: independently solved dual moments, the quadratic identity, denominator decomposition, endpoint equalities, positive endpoint-weight factorization, support constant, transition polynomial with root separation, and the active asymptotic series.
- Eighteen exact rational examples cover nine boundary and nine strict active points across $T=3/2,2,5$. Each checks the phase condition, dual signs, complete polynomial losslessness identity, outer factor, and exact global cap equality.
- Three independent symmetric inactive examples check polynomial completion, including $T=1$.
- A symbolic regression distinguishes the incorrect degree-one completion of a constant column from the corrected constant unitary.

All checks passed. These examples supplement the quantified analytic review above; they do not substitute a finite parameter sample for its proof. The deriving agent's separate replay and numerical cases were inspected as its evidence, not relabeled as this review's independent computation.

Four substantive review corrections are resolved in the pinned source: the constant-branch completion interface; the general factorization of both nonnegative quadratics, including zero leading coefficient; the symmetric equality $B=m=0$; and the non-strict inequality needed at $q=0$. No change to the stated optimal value or active dual was required. The source also now describes this review separately from the deriving agent's replay.

## 6. References and limits of the conclusion

The inherited structural ingredients are classical. The inspected primary text on [rectangular para-unitary rational functions](https://arxiv.org/html/1410.0283v2) supports the use of unitary completion and Blaschke–Potapov structure; its convention must be translated to the disk convention used here. The official [1998 magnitude-filter-design chapter record](https://web.stanford.edu/~boyd/papers/magdes.html) confirms the established role of convex reformulation and spectral factorization. These are context for the reduction, not independent publication of the new formula.

The primary abstracts of [rational minimax approximation via convex optimization](https://arxiv.org/abs/2308.06991) and [degree-preserving semidefinite QSP methods](https://arxiv.org/abs/2608.30937) were checked for the manuscript's limited comparisons. Their settings differ from this one-state phase-free routing problem. Those checks do not establish exhaustive novelty and do not constitute full proof audits of the cited papers.

The new result is established relative to the fully inspected cycle-2 manuscript: its failed-residual region is replaced by an explicit feasible optimizer, a positive universal dual, a unique transition, and a global two-port compiler. No external priority claim, human peer review, Lean replay, or experiment is implied by this PASS. The accompanying JSON pins the sources and verification artifacts so later edits can be distinguished from the reviewed revision.
