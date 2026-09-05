# Independent internal screening of the final passive article

5 September 2026. Reviewer: a separate Codex agent from the agent deriving the passive revision. Decision: **PASS — no material mathematical, computational, or source/PDF correspondence objection found within the scope below.** This is internal screening, not external refereeing, an external priority assessment, or an independent Astra evaluation requested by the user. No score is assigned.

## Exact objects reviewed

- Article: `active_delay.md`, SHA-256 `ea3318557e3a8c6a7d0eb49296da8b0f624c1a77caada094d516488ef4e8f403`.
- Final PDF: `../pdfs/passive.pdf`, thirteen pages, SHA-256 `e82792511520f394d2f67eb603b3b97e89e61911c7ed588436855f1fe416f51a`.
- Deriving-agent verifier: `verify_active_delay.py`, SHA-256 `e8b2ed0049f618bc7907c3523ab969ea96cce199cfdef8784b1c70fbf83fd2e1`.

The complete final article and all thirteen rendered pages were read. The new mathematical attack concentrated on Theorem 2 and Section 8, equations (28)–(36): completeness of the inverse reduction, uniqueness of the cubic root, feasibility at the clamp, the sign of the active inverse, the error threshold, and the discontinuity at the first permitted nonconstant delay. The forward law, positivity certificate, compiler and limits were checked against the retained earlier review and by rerunning its separate exact checker in the new directory. Frozen earlier evidence was not edited.

## Mathematical assessment of the inverse

**Completeness of the one-parameter reduction.** The inverse proof uses the already established forward theorem and its uniqueness statement; it does not assume the conclusion of the inverse theorem. For fixed $t$, the inactive support function increases strictly with $T$. Evaluating the smaller-cap function at the larger-cap minimizer proves strict increase of its minimum, hence strict decrease of the error. The active expression is strictly decreasing because $L$ increases, and the expressions meet continuously at the sole transition. Thus every target strictly below $e_1$ determines exactly one cap above one. Its optimal quadratic $Q$ has rank one and all three node errors active, as required by the forward certificate.

Solving the two endpoint equations afresh with leading coefficient of $H$ fixed to one gives precisely equation (31). Expansion recovers the stated signs of $B$ and $C$. Conversely, every feasible parameter in this family gives a two-port router with the three target errors exactly. Therefore restricting the delay minimization to this family loses no unrestricted optimizer.

**Positivity and the clamp.** Direct determinants give

\[
\det H_{\rm matrix}=(g-1)(d^2-gy^2),\qquad
\det P_{\rm matrix}=\frac{g-1}{g+1}(d^2-g^2y^2).
\]

The leading coefficient of $P$ is positive. Hence its exact feasibility interval is $[-d/g,d/g]$. Since $g>1$, the denominator remains strictly positive even at both endpoints, with determinant at least $d^2(g-1)^2/g$. Thus clipping the unconstrained minimizer to the positive endpoint introduces no denominator singularity. The smaller interval is the residual-positivity constraint; substituting $d/\sqrt g$ as its endpoint would have been incorrect.

**Cubic uniqueness and derivative sign.** Differentiating the trace divided by twice the square root of the determinant gives equation (33), including its negative sign and its factor two. For $m<0$, $G(0)>0$ and the stated value at $d/\sqrt g$ is strictly negative. On the positive interval, $G'$ is strictly increasing. A strictly convex function with those endpoint signs crosses zero exactly once there; any later crossing would force a positive value at the right endpoint. On the negative interval the rewritten expression $s(A_g-gs^2)-2md^2$ is positive. Therefore $p$ decreases to that one root and increases afterward. When $m=0$, its factorization gives the minimum at zero. The formula $\min(y_0,d/g)$ and the sign test at $d/g$ follow.

**Active sign and threshold.** There is no omitted square-root branch in equation (34). Independently, put $L=d(g-1)/\sqrt g$ and define the initially signed quantity $\widetilde w=(L^2-1-v^2)/(2L)$. Direct substitution gives

\[
G(d/g)=\frac{2dL}{g}(\widetilde w-v\sqrt g).
\]

Thus the active-or-boundary sign condition forces $\widetilde w\ge v\sqrt g>0$, selecting $L=p+w$ with the positive root $w$. At equality, $w^2=gv^2$ and $q^2=(g+1)v^2$, so $\varepsilon_c=1/(g+1)=v^2/q^2$. This independently verifies equation (35) and its squared-error interpretation. Strict decrease of the forward error gives the claimed orientation of targets around the transition. The regimes $u\le3v$ and $u>3v$ agree with the forward phase classification.

**Exceptional targets and attainment.** The target zero is unattainable at any finite cap because each forward value is positive. A constant router attains squared error $1/2$ with actual peak zero. Every nonconstant router has peak at least one. The exact $T=1$ Rayleigh-quotient formula gives $0<e_1<1/2$. Hence the inverse is zero at targets at least $1/2$, one on $[e_1,1/2)$, and strictly greater than one below $e_1$. This accounts for both equality endpoints and the jump. Reflection and the symmetric formula are consistent with the stated open-angle hypotheses.

## Computational evidence and scope

`inverse_independent_checks.py` was written for this review and imports no deriving-agent verifier. It solves the endpoint equations symbolically, derives both determinants and the derivative numerator, verifies the active-sign identity above, and checks four exact inactive/active/boundary/symmetric fixtures. Exact Sturm counts test the root and clamp classification in 74 further rational parameter cases. Exact comparisons immediately above and below $e_1$ exercise the first-cap decision without tolerances. The report is `inverse_independent_checks.json`: PASS.

The preserved earlier separate checker was copied to `independent_review_checks.py` and rerun against the new source. It again reconstructs the dual weights from moment equations, verifies the global polynomial completion and delay identities, and checks eighteen rational active/boundary fixtures and three symmetric inactive fixtures: PASS. Its degree-zero regression confirms that constants bypass the degree-one sharp completion. This is reused independent evidence, not a newly claimed derivation by the present reviewer.

The deriving agent's exact inverse interface was inspected for branch semantics. It uses rational comparisons, exact root counts and rational isolating intervals. Its numerical convenience interface uses tolerances and is explicitly labeled numerical; those tolerances are not accepted as exact certificates. Symbolic root output is explicitly bound to its isolating interval. The analytic argument, rather than the finite fixture set, supplies the arbitrary-parameter conclusions.

## PDF correspondence and readability

The final PDF hash and source hash agree with the build ledger. All 86 display formulas were compared with the source ledger, including the complete sequence of numbered equations (1)–(36). All six distinct external links in the source are present in the PDF. The final source and bibliography are present through the authorship disclosure.

All thirteen final pages were visually checked. Pages 1–3 were first read before the references-only rewrite and then verified pixel-identical to their final renders; pages 4–13 were read directly from the final renders. The inverse is complete on pages 10–12. Its root interval, derivative, clamp, threshold and fixture all render correctly. The compact reference page remains readable. No clipped equation, missing inequality, lost paragraph, overlap or missing terminal page was found. Details are recorded in `pdf_source_correspondence.json`.

The review accepts the classical degree-one inner-factor structure as the stated antecedent and does not reopen external bibliographic priority. It is not a formal proof-assistant verification. No change to the final mathematical source or PDF is requested.
