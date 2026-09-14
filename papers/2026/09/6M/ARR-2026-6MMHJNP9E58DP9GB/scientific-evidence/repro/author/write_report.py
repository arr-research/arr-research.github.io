"""Writes cycle3/report_B4_two_planes_fold.md (the deliverable required by BRIEF_CYCLE3.md).
Run:  python write_report.py [Q_MAX_CERTIFIED]
"""
import sys, io, os

qmax = sys.argv[1] if len(sys.argv) > 1 else "60"
here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, "..", "..", "report_B4_two_planes_fold.md")

TEXT = r"""# Report B4_two_planes_fold — a phase-space proof of one fold for oriented two-planes (cycle 3)

Agent: Claude Fable 5.1 (no fallback occurred). Date: 2026-09-14. Work dir: `cycle3/work/B4_two_planes_fold/`.
Status: COMPLETE. Main result: THEOREM (analytic, every q >= 4, no estimates, no coefficient signs): H_q has exactly one
positive zero. Independent proof of 7H9F Theorem 8.2 (n >= 6); the same argument gives 7H9F Lemma 7.1 for n = 4, 5.
A resumed agent: read Section 0, then Section 3 (the proof), Section 5 (scripts), Section 7 (open).

## 0. State
- [x] Inputs read: brief; B3 manuscript Sections 3, 4, 8, 10; review_B3 Section 7; 7H9F Sections 7-9 (Lemma 7.1, Thm 8.2, Thm 9.1).
- [x] Reduction (C1)-(C6) and the Lyapunov bracket B: sympy with symbolic q (`sym_reduction.py`, 6 s), plus a termwise check
      of the second-order equation from the series.
- [x] THEOREM (Section 3): two-sided Lyapunov argument with Q := T - (q - 1/2) kappa H and threshold u = 8/(q(q-1)).
- [x] Numerical sanity checks of every intermediate inequality of the proof along trajectories (`verify_lyapunov.py`).
- [x] Redundant computer-assisted certificate (interval arithmetic) of the pre-threshold sign for 4 <= q <= QMAX (`certify_neg.py`).
- [x] Probabilistic reformulations (Fano factor of the index law; parity-window Poisson); numerics; literature.
- [ ] Nothing pending for the theorem. Open items are extensions (Section 7).

## 1. Setting (B3 Section 8)
L = L_q(kappa) = q! sum_j kappa^{2j}/(q+2j)! = sum_j z^j/(q+1)_{2j}, z = kappa^2, q = n-2;  m = L'/L,  H = H_q = m - kappa m',
u := 1/L,  X := kappa m,  tau := log kappa,  h := kappa H.  The multiplier of 7H9F is lambda_q = kappa/(2 m_q), so
lambda_q' = H_q/(2 m_q^2): folds of lambda_q are the zeros of H_q.
Inhomogeneous second-order equation (E2):  kappa^2 L'' + 2 q kappa L' - (kappa^2 - q(q-1)) L - q(q-1) = 0
(B3 Prop 8.1(ii); re-verified here termwise from the series: the coefficient of kappa^{2j} is
[2j(2j-1) + 4qj + q(q-1)] w_j - w_{j-1} = 0 because (q+2j)(q+2j-1) w_j = w_{j-1}).  Its derivative is B3's third-order
equation (8.1) (checked).  Closed form: L_q = q! kappa^{-q} C_q(kappa), C_q = tail sum_{k >= q, k = q mod 2} kappa^k/k! of the
cosh (q even) or sinh (q odd) series, with C_q' = C_{q-1}.

Facts used.
(F1) For q >= 4, H_q < 0 on some (0, eps): H_q is odd and analytic at 0 with [kappa^1] H_q = 0 and
     [kappa^3] H_q = -4(q^2-q-8)/((q+1)^2(q+2)^2(q+3)(q+4)) < 0 (B3 Prop 8.2, re-derived from the series here; equivalently g_2
     below), so kappa^3 is the leading term.  For q <= 3 the coefficient is positive.
(F2) H_q -> 1 as kappa -> infinity.  Proof from the closed form: rho := C_{q-1}/C_q = 1 + O(kappa^{q-2} e^{-kappa}) since
     C_q = (e^kappa/2)(1 + O(kappa^{q-2}e^{-kappa})) and likewise C_{q-1}; m = rho - q/kappa; from C_q'' = C_{q-2} = C_q + kappa^{q-2}/(q-2)!,
     kappa m' = kappa(1 - rho^2) + kappa^{q-1}/((q-2)! C_q) + q/kappa -> 0.  Hence H = m - kappa m' -> 1 (only H > 0 for large kappa is used).
(F3) X > 0 for kappa > 0 (L' has positive coefficients); u = 1/L is strictly decreasing from u(0+) = 1 to 0 (L strictly increasing,
     L -> infinity).  So for q >= 4 there is a unique kappa_L > 0 with u(kappa_L) = u_* := 8/(q(q-1)) < 1, i.e. L_q(kappa_L) = q(q-1)/8.
(F4) T -> 0 and h -> 0 as kappa -> 0+ (X -> 0, u -> 1).

## 2. The reduction (PROVED; every identity machine-checked with symbolic q in `sym_reduction.py`)
(C1) h = X^2 + (2q+1) X + q(q-1)(1-u) - kappa^2.
     Consequently kappa H = (kappa m - kappa m_+)(kappa m + kappa m_+ + 2q + 1) with m_+(kappa) the positive root of
     kappa^2 m^2 + (2q+1) kappa m + q(q-1)(1-u) - kappa^2 = 0: H has the sign of m - m_+(kappa), and the zero set of H is the set of
     crossings of the trajectory m(kappa) with the explicit curve m_+(kappa) (u = 1/L_q(kappa) is elementary).
(C2) dX/dtau = 2X - h,   du/dtau = -X u.   (Closed 2-D system: dX/dtau = kappa^2 - X^2 - (2q-1) X - q(q-1)(1-u).)
(C3) kappa^2 Delta_q = T + (X+2) h,   T := 2 X^2 + q(q-1) u X - 2 q(q-1)(1-u)   (Delta_q is B3's transversality function).
(C4) dT/dtau = X^2 (8 - q(q-1) u) - h (4X + q(q-1) u).
(C5) dh/dtau = T - (2X + 2q - 1) h.
(C6) (B3 (8.2), re-checked) H' + (3m + (2q+2)/kappa) H = Delta_q.
At a zero of H: H' = Delta_q = T/kappa^2 (from (C3), (C6)); the crossing is upward iff T > 0.

Probabilistic reading (PROVED, elementary).  Let J have the law P(J=j) proportional to z^j/(q+1)_{2j} (the index law of the series L_q,
an exponential family in theta = log z).  Then E J = X/2, Var J = d(E J)/dtheta and
        kappa H_q = 4 (E J - Var J):    H_q < 0  <=>  Var J > E J  (Fano factor of the index law > 1).
Equivalently, with K ~ Poisson(kappa) conditioned on A = {K >= q, K = q mod 2} (K = q + 2J):
        E[K(K-1) | A] = kappa^2 + q(q-1) P(K = q | A)      (exact: sum_{k in A} k(k-1) kappa^k/k! = kappa^2 sum_{k in A-2} kappa^k/k!),
        u = P(K = q | A),   X = E[K - q | A],   kappa H_q = 2 E[K - q | A] - Var(K | A).
The fold is where the conditional variance equals twice the conditional excess mean, and the threshold u_* = 8/(q(q-1)) is a
condition on the mass of the boundary atom K = q.  (7H9F's parity-truncated binomial law concerns the coefficients c_{q,r};
this parity-window Poisson law is attached to the function.)

## 3. The theorem and its proof
Throughout q >= 4, c := q - 1/2, and
        Q := T - c h            (a function of the state (X, u, kappa), evaluated along the trajectory).
**Lemma L (the Lyapunov identity).**  dQ/dtau = X^2 (8 - q(q-1) u) - c Q + h B,   B := (2c-4) X + c(2q-1-c) - q(q-1) u,
and B >= 0 for all kappa > 0.
Proof.  (C4), (C5) and -cT = -cQ - c^2 h give the identity (sympy).  For c = q - 1/2: 2c - 4 = 2q - 5 > 0, X > 0, and
c(2q-1-c) = (q - 1/2)^2 >= q(q-1) >= q(q-1) u since u <= 1.  QED
Consequences.  Where h <= 0 and u >= u_*:  dQ/dtau <= -cQ,  i.e. (e^{c tau} Q)' <= e^{c tau} X^2 (8 - q(q-1)u) <= 0.
               Where h >= 0 and u <= u_*:  dQ/dtau >= -cQ,  i.e. (e^{c tau} Q)' >= e^{c tau} X^2 (8 - q(q-1)u) >= 0.
Both inequalities are strict for kappa not equal to kappa_L (X > 0, u strictly monotone).

**Step 1 (before the threshold): h < 0 on (0, kappa_L].**
Suppose not, and let kappa_* := inf{kappa in (0, kappa_L] : h(kappa) >= 0}.  By (F1) kappa_* > 0, h < 0 on (0, kappa_*) and h(kappa_*) = 0.
On (0, kappa_*] we have h <= 0 and u >= u(kappa_L) = u_* (F3), so (e^{c tau} Q)' <= e^{c tau} X^2 (8 - q(q-1) u) <= 0 there, with strict
inequality on (0, kappa_*) (u > u_* for kappa < kappa_L).  Since e^{c tau} Q -> 0 as tau -> -infinity (F4, c > 0),
e^{c tau_*} Q(kappa_*) = integral_{-infinity}^{tau_*} (e^{cs} Q)' ds < 0.  Hence T(kappa_*) = Q(kappa_*) + c h(kappa_*) = Q(kappa_*) < 0.
But h < 0 on (0, kappa_*) and h(kappa_*) = 0 force dh/dtau(tau_*) >= 0, while (C5) gives dh/dtau(tau_*) = T(kappa_*) < 0.  Contradiction.  QED
Consequently the first zero kappa_f of H (which exists by (F1), (F2)) satisfies kappa_f > kappa_L, so u < u_* on [kappa_f, infinity).

**Step 2 (after the threshold): no zero of H in (kappa_f, infinity).**
Put g := X^2 (8 - q(q-1) u) > 0 on [kappa_f, infinity).  H < 0 on (0, kappa_f) and H(kappa_f) = 0 give H'(kappa_f) >= 0, i.e.
T(kappa_f) = kappa_f^2 Delta_q(kappa_f) >= 0.  A double zero is impossible: if H(kappa_f) = H'(kappa_f) = 0 then T = h = 0 there and by
(C3)-(C5) d(kappa^2 Delta_q)/dtau = dT/dtau + (X+2) dh/dtau + h dX/dtau = g > 0, so Delta_q'(kappa_f) > 0; differentiating (C6) at a point
with H = H' = 0 gives H''(kappa_f) = Delta_q'(kappa_f) > 0, so H > 0 on a punctured neighbourhood, contradicting H < 0 before kappa_f.
Hence H > 0 immediately after kappa_f.  If H had a zero after kappa_f, let kappa_1 be the first (zeros are isolated: H is real-analytic
and nonconstant); then h >= 0 on [kappa_f, kappa_1] and u <= u_*, so (e^{c tau} Q)' >= e^{c tau} g > 0 there and
Q(kappa_1) > Q(kappa_f) e^{-c(tau_1 - tau_f)} = T(kappa_f) e^{-c(tau_1 - tau_f)} >= 0.  But h(kappa_1) = 0, so
Q(kappa_1) = T(kappa_1) = kappa_1^2 H'(kappa_1) <= 0 because H reaches 0 from above.  Contradiction.  QED

**THEOREM (PROVED, every integer q >= 4, i.e. n >= 6).**  H_q = m_q - kappa m_q' has exactly one positive zero kappa_f; H_q < 0 on
(0, kappa_f), H_q > 0 on (kappa_f, infinity), H_q'(kappa_f) > 0, and kappa_f > kappa_L where L_q(kappa_L) = q(q-1)/8.  Hence the
oriented-two-plane multiplier lambda_q(kappa) = kappa/(2 m_q(kappa)) has exactly one fold, and 7H9F Theorem 9.1 (complete
high-dimensional phase, unique coexistence, no reentrance) follows with this proof in place of 7H9F Theorem 8.2.
Proof.  Steps 1 and 2, (F1), (F2).  QED

**Corollary (q = 2, 3; 7H9F Lemma 7.1 for n = 4, 5).**  For q in {2, 3}, H_q > 0 on (0, infinity).
Proof.  Take c = 2 (q = 2) or c = 5/2 (q = 3); then 2c - 4 >= 0 and c(2q-1-c) >= q(q-1) (2*1 = 2 = q(q-1) for q = 2; 25/4 >= 6 for q = 3),
so B >= 0 again.  Here q(q-1) <= 6 < 8, so g = X^2(8 - q(q-1)u) > 0 for all kappa > 0, and H_q > 0 near 0+ (F1).  If H_q had a zero,
let kappa_1 be the first; on (0, kappa_1] h >= 0, so (e^{c tau} Q)' >= e^{c tau} g > 0 and, with e^{c tau} Q -> 0 at -infinity,
Q(kappa_1) = T(kappa_1) > 0; but H reaches 0 from above, so T(kappa_1) = kappa_1^2 H'(kappa_1) <= 0.  Contradiction.  QED
(q = 1, n = 3, is B3 Theorem 7.1 / 7H9F's explicit series; the bracket B cannot be made nonnegative with q(q-1) = 0.)

Remarks.
(i) What is new relative to B3 Section 8: the coordinates (X, u) = (kappa m, 1/L) in which the transversality sign at a crossing is the
polynomial T(X, u), the Lyapunov function Q = T - (q - 1/2) kappa H whose tau-derivative has the sign-definite forcing
X^2 (8 - q(q-1) u) on the zero surface, and the threshold u = 8/(q(q-1)) that splits (0, infinity) into a region where Q is pushed
down (so H cannot come up to 0) and a region where Q is pushed up (so H cannot come down to 0).  No estimate of m_q, L_q or the
fold position is used anywhere; B3's obstruction ("at the fold the O(q) terms of Delta_q cancel") disappears because the argument never
evaluates anything at the fold.
(ii) The constant 8 is intrinsic: for any function Q~ with Q~ = T on {h = 0}, dQ~/dtau|_{h=0} = X^2(8 - q(q-1)u) + (dQ~/dh) T.
(iii) Byproducts: T < 0 along the trajectory on (0, kappa_L] (Step 1 gives Q < 0 and h < 0 there); T > 0 on [kappa_f, infinity);
kappa_L < kappa_f, and in fact the sign change of Delta_q along the trajectory and the sign change of T lie in (kappa_L, kappa_f).
(iv) Method for third-order normalizers: the reduction uses only that L is the even part of a solution of a first-order inhomogeneous
linear equation (giving (E2)).  The recipe -- write the fold numerator as kappa H = P(X, u, kappa) with (X, u) = (kappa m, 1/L), compute
the transversality polynomial T and the forcing on {h = 0}, find c with B >= 0 -- is mechanical and is the "method for third-order
normalizers" asked for in the brief; whether a sign-definite forcing exists for pF_{p+1} normalizers is open (Section 7).

## 4. Numerical sanity checks of the proof (not part of the proof; `verify_lyapunov.py`, mpmath 30 digits)
For q in {4, 5, 6, 10, 30, 60}, on 200-point grids up to 4q + 40: Q < 0 and (e^{c tau}Q)' <= 0 on (0, kappa_L]; Q > 0 and
(e^{c tau}Q)' > 0 on [kappa_f, 4q+40]; H < 0 on (0, kappa_L], H > 0 after kappa_f; min B = 0.30 (q=4) ... 2.20 (q=60); the identity for
(e^{c tau}Q)' agrees with a finite difference to 1e-57.  For q = 2, 3 with c = 2, 5/2: H > 0, Q > 0, (e^{c tau}Q)' > 0 on (0, 60].
Reference values (`num_phi.py`, agree with B3 Section 8 / review_B3 to all printed digits):
| q | kappa_f | kappa_Delta | kappa_L | L_q(kappa_f) | T(kappa_f) | m(kappa_f) |
|---|---|---|---|---|---|---|
| 4 | 4.415714051 | 4.161910 | 3.469051 | 1.9334 | 0.173 | 0.3005 |
| 5 | 7.613543394 | 7.290145 | 6.045574 | 4.3697 | 1.415 | 0.3982 |
| 6 | 10.25463377 | 9.904743 | 8.174269 | 8.478 | 3.448 | 0.4386 |
| 10 | 19.37353191 | 18.991063 | 15.384999 | 62.88 | 14.02 | 0.4865 |
| 20 | 39.94164751 | 39.545885 | 30.744399 | 2529 | 38.84 | 0.4993 |
| 30 | 59.99529121 | 59.597519 | 44.788910 | 6.8e4 | 59.86 | 0.5000 |
| 40 | 79.99966909 | 79.601279 | 58.215300 | 1.7e6 | 79.99 | 0.5000 |
kappa_L/q: 0.87 (q=4), 1.21 (5), 1.36 (6), 1.54 (10), 1.55 (15), 1.49 (30), 1.43 (50), 1.31 (120), 1.26 (200); kappa_f ~ 2q.
The margin at the threshold is small only for q = 4 (kappa_L H(kappa_L) = -0.01442, H(kappa_L) = -0.004158), which is why no estimate-based proof was found in B3;
the Lyapunov argument does not see this margin.

## 5. Scripts (all in `cycle3/work/B4_two_planes_fold/`; Python 3.12, sympy 1.14, mpmath 1.3)
| script | what | arithmetic | time |
|---|---|---|---|
| `sym_reduction.py` | (E2) termwise from the series, (E3) = (E2)', (C1)-(C6), B3 (8.2), the bracket B, [kappa^3]H_q, g_2, g_3 | sympy, symbolic q | 6 s (`--phi` adds a slow optional series, unused) |
| `verify_lyapunov.py` | Section 4 sanity checks of every inequality in the proof | mpmath 30 digits | 90 s |
| `num_phi.py q ...` | kappa_f, kappa_Delta, kappa_L, u(kappa_f), T(kappa_f), margins | mpmath 60 digits, positive series | ~20 s per q |
| `certify_neg.py q1 q2 ...` | redundant rigorous interval-arithmetic certificate of Step 1's conclusion H_q < 0 on (0, kappa_L] (Lemma S for small z, adaptive mean-value continuation to a certified upper bound of z_L; `mpmath.iv`, outward rounding) | interval, 40 digits | 60 s (q=4), 6-40 s (q >= 7); certified 4 <= q <= QMAX with no failure (`certify_*.log`) |
| `margins.py`, `lemma_c_check.py`, `t_signchange.py` | exploratory numerics from before the proof was found (relative margins of Var J > E J; an estimate-based Lemma C covering kappa <= 0.44q; sign change of T) | mpmath | 7 s, 2 s, 60 s |
| `write_report.py` | writes this report | - | - |
Lemma S (used only by the certificate): with y = z/((q+1)(q+2)), c2 = (q^2-q-8)/((q+3)(q+4)), G := S0 S1 - S0 S2 + S1^2 = S0^2 kappa H/4
satisfies G <= -c2 y^2 + (4y)^3/(1-4y) < 0 for y < c2/(64 + 4c2), from g_2 = -(q^2-q-8)/((q+1)^2(q+2)^2(q+3)(q+4)) and
|g_r| <= r(r+1)^2 ((q+1)(q+2))^{-r} <= (4/((q+1)(q+2)))^r for r >= 3.  Also found: g_3 = -4(q-4)/((q+1)^2(q+2)^2(q+4)(q+5)(q+6)),
vanishing at q = 4 exactly as 7H9F's c_{4,3} = 0.

## 6. Classification
- THEOREM (analytic, every q >= 4): one fold, with the byproducts of Remark (iii).  PROVED.
- Corollary q = 2, 3: no fold.  PROVED.
- PROVED-COMPUTER-ASSISTED (redundant): H_q < 0 on (0, kappa_L] for 4 <= q <= QMAX by outward-rounded interval arithmetic.
- NUMERICAL: Section 4 tables.
- No conjecture remains for the oriented-two-plane problem itself.

## 7. Open
1. pF_{p+1} normalizers of phase-lifted coherent orbits (6XH6/6DJ3) and Slater orbits (k-1 F k): find the analogue of (E2) (an
   inhomogeneous lower-order equation) and test whether the forcing on {h = 0} is sign-definite with a threshold in a single state
   variable.  Not attempted.
2. Grassmann rank r >= 2 (matrix-argument 1F1; 68BH open question 1): not touched.
3. The exact leading coefficient of T on the zero locus (numerically ~ 3/4 of [kappa^2]Delta_q) is unimportant and was not derived.

## 8. Independent adversarial review (2026-09-14)
A second Claude Fable 5.1 agent (no fallback), given only this report, re-derived (E2) termwise, (C1)-(C5), Lemma L with general c,
the double-zero identity and H'' = Delta' with its own sympy script (symbolic q; residuals 0), audited every step of Steps 1-2 and the
Corollary (sign directions of hB in both regions, the inf argument, the limit e^{c tau}Q -> 0, strictness, (F1)-(F3)), and reproduced the
sign claims numerically for q = 4, 7, 12 and q = 2, 3 (40 digits, own code).  Verdict: CORRECT.  Its four cosmetic remarks ([kappa^1]H = 0
should be stated in (F1); exponent q-2 in (F2); the isolated-zeros remark is redundant; kappa_L H(kappa_L) = -0.01442, not -0.012) are
incorporated above.

## 9. Literature (WebSearch 2026-09-14; a null result does not certify priority)
- Karp-Sitnik, *Log-convexity and log-concavity of hypergeometric-like functions*, JMAA 364 (2010), arXiv:0902.3073; Karp, *Turan's
  inequality for the Kummer function of the phase shift of two parameters* (J. Math. Sci. 2011): log-concavity / Turan inequalities in the
  parameters (a, c), not in the argument; nothing about K' - kappa K''.
- Baricz-Pogany, *Functional inequalities for modified Struve functions* I, II (arXiv:1301.5423, 1301.5635); modified Lommel functions
  (Results Math. 2021): monotonicity of ratios via the Biernacki-Krzyz quotient-of-power-series lemma.  L_q = 1F2(1;(q+1)/2,(q+2)/2;kappa^2/4)
  is a modified Struve function only for q = 2, a Lommel-type function in general; none of these results concerns the sign of the fold
  numerator, the Fano factor of the index law, or a Lyapunov function of the present kind.
- Fano factor / over-dispersion of power-series distributions: only applied (neuroscience) hits; no theorem on a single crossing of
  Var/E for log-concave weight sequences.
- Parity-conditioned Poisson (K >= q, K = q mod 2): no hit; closest are lower-truncated Poisson moment formulas (Geyer's notes,
  zero-truncated Poisson).  The identity E[K(K-1)|A] = kappa^2 + q(q-1) P(K=q|A) appears to be new in this context (elementary).
"""

with io.open(target, "w", encoding="utf-8") as f:
    f.write(TEXT.replace("QMAX", qmax))
print("wrote", os.path.abspath(target), "with QMAX =", qmax)
