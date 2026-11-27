# Quantitative Stability of the Smoothed Regular Octagon, Exact Linear-vs.-Quadratic Perturbation Dichotomy, and Independent Zero-Float Bernstein Certification for the Reinhardt Conjecture

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-52ZZ2YZ1SE89RRDX` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/reinhardt-quantitative-stability-and-bernstein-audit (`v1.0.0`)  
**Canonical PDF SHA-256:** `7df1cbdc1f7f5dc8ff985cd775f8751780eace360b2bef4890aeb98632c9da70`

## Abstract

The ninety-two-year-old Reinhardt conjecture---asserting that the smoothed regular octagon K_oct uniquely minimizes maximal packing density among centrally symmetric planar convex disks, delta(K) >= delta_oct = (8 - 4*sqrt(2) - ln 2)/(2*sqrt(2) - 1)---was recently resolved in three announcements by Vu-Le, Schmutz, and Xue (arXiv:2611.21470v2), and unified in Thomas Hales' streamlined optimal-control proof (hexagon:2611.01057v1). Here we establish quantitative stability, perturbation-order separation, spectral characterization, and independent zero-float Bernstein certification across the Hales--Xue framework. First (Theorem 1), along Hales' four-arc closure quarter circle q_bar_0 = cos theta, q_bar_1 = sin theta, we compute the exact second-order stability curvature A_norm''(pi/4) = (340 - 132*sqrt(2) - (80 + 90*sqrt(2))*ln 2)/49 ~ 0.196914 and prove a global elementary quantitative stability law via an exact s-antiderivative (s = cos theta + sin theta): A_norm(cos theta, sin theta) - delta_oct >= c_s*(sqrt(2) - s) >= c_theta*(theta - pi/4)^2 with c_s = (125*sqrt(2) - 172)/98 and c_theta = c_s * 16*(sqrt(2) - 1)/pi^2, confining every four-arc disk below Xue's competitor ceiling C_*/2 = 180483/200000 inside |theta - pi/4| < 0.0050 rad (< 0.2863 deg). Second (Theorem 2), we prove that Hales' six-arc mixed family A_mix(v) is globally strictly convex (A_mix''(v) = 8*sqrt(3)/(v*(v+4)^2) > 0) with a strictly nonzero linear defect at v_max = 4*(4*sqrt(2) - 5)/7, establishing an exact linear-vs.-quadratic stability dichotomy between mixed-switch (Omega(v_max - v), Xue radius < 2.60e-5) and all-forward (Theta((theta - pi/4)^2)) perturbations of K_oct, while certifying the full regular-walk density and determinant spectrum N = 3m + 1 in {4, ..., 25} -> (pi/(2*sqrt(3)), 3/16). Third (Theorem 3), we independently reconstruct and certify in pure integer/rational arithmetic (zero float, zero math, zero sympy) all 576 tensor Bernstein coefficients of Hales' Claim V11 (exact maximum -12977579752000390297/84375000000000000000) and all 2,700 five-dimensional Bernstein coefficients of Claim V6 (exact minimum 23/768), and determine exact affine sensitivity margins revealing that Hales' parameters kappa_0 = 583/500 and r_0 = 2/9 are razor-sharp to within 0.018% and 0.565%, respectively. All finite integer/rational algebraic identities, Q(sqrt(2)) normalizations, and guard inequalities are formally proved by 20 constructive Lean 4.36.0 theorems (0 sorry, 0 Classical.choice), while transcendental interval brackets and full Bernstein reconstructions are sealed in 16 SHA-256 zero-float rational certificates and audited by 56 adversarial tests.

## Full Extracted Text

--- Page 1 ---
Quantitative Stability of the Smoothed Regular Octagon, Exact
Linear-vs.-Quadratic Perturbation Dichotomy, and Independent
Zero-Float Bernstein Certification for the Reinhardt Conjecture
Lluis Eriksson*
November 2026
Abstract
The ninety-two-year-old Reinhardt conjecture—asserting that the smoothed regular oc-
tagon Koct uniquely minimizes maximal packing density among centrally symmetric planar
convex disks, δ(K) ≥δ oct = (8 − 4
√
2−ln 2)/(2
√
2− 1)—was recently resolved in three
announcements by Vu-Le, Schmutz, and Xue (arXiv:2611.21470v2), and unified in Thomas
Hales’ streamlined optimal-control proof ( hexagon:2611.01057v1). Here we establish quan-
titative stability, perturbation-order separation, spectral characterization, and independent
zero-float Bernstein certification across the Hales–Xue framework. First (Theorem 1), along
Hales’ four-arc closure quarter circle ¯q0 = cosθ,¯q1 = sinθ , we compute the exact second-order
stability curvature A′′
norm(π/4) = (340 − 132
√
2− (80 + 90
√
2) ln 2)/49 ≈ 0.196914 and prove
a global elementary quantitative stability law via an exact s-antiderivative (s = cosθ + sinθ ):
Anorm(cosθ,sinθ ) −δ oct ≥c s(
√
2−s ) ≥c θ(θ−π/ 4)2 with cs = (125
√
2− 172)/98 and
cθ = cs · 16(
√
2− 1)/π2, confining every four-arc disk below Xue’s competitor ceiling C∗/2 =
180483/200000 inside |θ−π/ 4|< 0.0050 rad (< 0.2863◦). Second (Theorem 2), we prove that
Hales’ six-arc mixed familyAmix(v) is globally strictly convex (A′′
mix(v) = 8
√
3/(v(v+4)2) > 0)
with a strictly nonzero linear defect at vmax = 4(4
√
2− 5)/7, establishing an exact linear-vs.-
quadratic stability dichotomy between mixed-switch (Ω(vmax −v ), Xue radius < 2.60 ×10−5)
and all-forward (Θ((θ−π/ 4)2)) perturbations of Koct, while certifying the full regular-walk
density and determinant spectrum N = 3m+1 ∈ {4, . . . ,25} →(π/(2
√
3), 3/16). Third (The-
orem 3), we independently reconstruct and certify in pure integer/rational arithmetic (zero
float, zero math, zero sympy) all 576 tensor Bernstein coefficients of Hales’ Claim V11 (exact
maximum −12977579752000390297/84375000000000000000) and all 2 ,700 five-dimensional
Bernstein coefficients of Claim V6 (exact minimum 23 /768), and determine exact affine sensi-
tivity margins revealing that Hales’ parameters κ0 = 583/500 and r0 = 2/9 are razor-sharp to
within 0.018% and 0.565%, respectively. All finite integer/rational algebraic identities, Q(
√
2)
normalizations, and guard inequalities are formally proved by 20 constructive Lean 4.36.0
theorems (0 sorry, 0 Classical.choice), while transcendental interval brackets and full
Bernstein reconstructions are sealed in 16 SHA-256 zero-float rational certificates and audited
by 56 adversarial tests.
1 Introduction
In 1934, Reinhardt [ 6] conjectured that among all centrally symmetric planar convex disks
K⊂R 2, the smoothed regular octagon Koct uniquely (up to invertible affine transformations)
minimizes the maximal packing densityδ(K):
δ(K)≥δ oct := 8−4
√
2−ln 2
2
√
2−1 ≈0.9024141830.(1)
* Independent Researcher. Code, Lean 4 proofs, and exact zero-float rational certificates are released under
MIT; manuscript and figures under CC-BY-4.0.
1

--- Page 2 ---
Building on Mahler’s critical-hexagon reduction [ 5], Fejes T´ oth’s lattice equivalence [1], and the
optimal-control program of Hales [2, 3] and Hales–Vajjha, three complete proofs were announced
in November 2026 by Vu-Le, Schmutz, and Fei Xue [ 7], followed immediately by Thomas Hales’
unified streamlined proof [4].
In [4], every competitive normal trajectory reduces to a finite walk on the control triangle
with three regimes: (i) mixed periods containing both forward and reverse switches, eliminated
via marked-center local bounds (Section 8, Propositions 8.1–8.2, Lemmas 8.1 and 8.3, Claims V6–
V8); (ii) long all-forward periods ( N≥ 7), eliminated via an adjacent-angle winding certificate
(Lemma 9.1, Claim V11); and (iii) four-arc all-forward periods (Section 10, Lemmas 10.1–10.2),
parameterized by the open quarter circle ¯q2
0 + ¯q2
1 = 1, where Hales proves that the normalized
area Anorm(¯q0,¯q1) attains its unique minimum δoct at ¯q0 = ¯q1 = 1 /
√
2. Meanwhile, Xue’s
proof [7, Section 1.1] operates under the explicit rational competitor ceiling δL(D) ≤C ∗/2 =
180483/200000 = 0.902415.
Three quantitative and certification questions arise directly from [4, 7]:
1. Quantitative stability around Koct:Hales’ Lemma 10.2 ([ 4, Eq. (10.8)]) proves only
qualitative monotonicity ψ′(¯q1) < 0 on (0, 1/
√
2). What is the exact quadratic curvature
of Anorm(cosθ,sinθ ) at θ = π/4, does it satisfy a global elementary quantitative lower
bound across (0 , π/2), and what explicit neighborhood around Koct is forced by Xue’s
ceilingC ∗/2?
2. Mixed vs. forward perturbation order and regular walks:Along Hales’ explicit six-arc
mixed family approaching Koct ([4, Remark 8.3, Claim V5]), does the packing density
exhibit a strictly first-order linear defect (in contrast to the quadratic defect of four-arc
forward perturbations)? And how do the regular all-forward walks N = 3 m + 1 ([ 4,
Remark 9]) approach the circle density π/(2
√
3) and determinant limit 3 /16 relative to
Hales’ competitive cap 9193/50000?
3. Independent zero-float Bernstein certification and parameter sharpness:Can Hales’ core ten-
sor Bernstein positivity certificates—Claim V11 (576 coefficients in multidegree (5 , 5, 3, 3))
and Claim V6 (2 ,700 coefficients in five variables)—be independently reconstructed with-
out sympy, math, or floating-point arithmetic, and how close are Hales’ chosen rational
parameters (κ0 = 583/500,r 0 = 2/9) to the exact feasibility boundary?
We resolve all three questions completely in Theorems 1–3.
2 Main Results
In Hales’ four-arc closure coordinates [ 4, Lemma 10.1–10.2], every admissible four-arc all-
forward period has alternating arc factors ( q0, q1, q0, q1) with reciprocals ¯q0 = 1 /q0 = cosθ ,
¯q1 = 1/q1 = sinθ (θ∈ (0, π/2)), sum s(θ) := cosθ + sinθ∈ (1,
√
2], and normalized packing
density
Anorm(cosθ,sinθ) = 1
(s−1)(s+ 3)

4s(s−1) + 2(1 + cosθ)(1−sinθ) ln cosθ
+ 2(1−cosθ)(1 + sinθ) ln sinθ

.
(2)
Theorem 1(Exact Curvature and Global Quantitative Stability on the Four-Arc Closure
Circle).
(a) Exact stability curvature at Koct:The normalized packing density (2) attains its
2

--- Page 3 ---
unique minimumδ oct atθ=π/4with exact closed-form second derivative
d2
dθ2

θ=π/4
Anorm(cosθ,sinθ) = 340−132
√
2−(80 + 90
√
2) ln 2
49
∈(0.1969143,0.1969144).
(3)
(b) Global elementary quantitative stability and Xue competitor radius:Forevery
θ∈ (0, π/2), letting s = cosθ + sinθ , the excess density satisfies the global elementary
bounds
Anorm(cosθ,sinθ)−δ oct ≥c s
 √
2−cosθ−sinθ

≥c θ

θ− π
4
2
,(4)
where the exact constants are
cs := 125
√
2−172
98 ≈0.04874179, c θ :=c s · 16(
√
2−1)
π2 ≈0.03273000.
Consequently, every four-arc all-forward disk beating Fei Xue’s competitor ceiling C∗/2 =
180483/200000[ 7, Section 1.1] (with certified gap C∗/2 −δ oct ∈ (8.17002, 8.17003) × 10−7)
satisfies
θ− π
4
 <4.9962×10 −3 rad(<0.2863 ◦),
max
 
|¯q0 −2 −1/2|,|¯q1 −2 −1/2|

<3.5454×10 −3.
(5)
Theorem 2(Linear-vs.-Quadratic Perturbation Dichotomy and Regular-Walk Spectrum).
(a) Global strict convexity and linear defect of Hales’ six-arc mixed family:Along
Hales’ six-arc mixed family [ 4, Remark 8.3, Claim V5], parameterized by v∈ (0, vmax]
with vmax := 4
(2+
√
2)2−1 = 4(4
√
2−5)
7 ≈ 0.375345, the period area Amix(v) = 2
√
3δ mix(v)is
globally strictly convex:
A′′
mix(v) = 8
√
3
v(v+ 4) 2 >0∀v∈(0, v max],(6)
and approaches Aoct = Amix(vmax)with strictly nonzero first-order linear slope, yielding
the global linear stability bound
δmix(v)−δ oct ≥λ mix (vmax −v),
λmix := 1
4
 
(3 + 2
√
2) ln 2− 5 + 2
√
2
2
!
≈0.03143607.
(7)
Combined with Theorem 1, this establishes an exact linear-vs.-quadratic stability dichotomy
around Koct: Xue’s ceiling C∗/2confines mixed six-arc perturbations to vmax −v <
2.5990 × 10−5 (0.0069%of vmax, over190 × tighter in parameter distance than the four-arc
radius(5)).
(b) Certified regular-walk density and determinant spectrum:Along Hales’ regular
all-forward branch N = 3m + 1( m≥ 1, smoothed regular2 N-gons, [4, Remark 9]), exact
outward-rounded certification over m∈ {1, . . . ,8} (N∈ {4, 7, 10, . . . ,25}, Table 1) verifies
strict monotonic convergence δN ↑π/ (2
√
3) ≈ 0.90689968and detS N ↑ 3/16 = 0.1875,
with the exact determinant hierarchy
27
256 <detS 4 ≈0.180196< 9193
50000 <detS 7 ≈0.186108< . . . < 3
16,(8)
certifying that N = 4is the unique regular walk below Hales’ competitive determinant cap
9193/50000, confirming the lower bound27 /256([ 4, Lemma 11.1]) and Aoct ≈ 3.126054 < π
([4, Section 2.1]).
3

--- Page 4 ---
Theorem 3(Independent Zero-Float Bernstein Certification and Exact Sensitivity Audit).
(a) Independent pure-rational verification of Hales’ Claim V11 and Claim V6:
Using strictly pure-integer and exact rational collocation (nofloat, nomath, nosympy):
 All576 = 6 ×6×4×4tensor Bernstein coefficients of Hales’ adjacent-angle certificate [4,
Claim V11] in multidegree(5 , 5, 3, 3)at( κ0, r0) = (583/500, 2/9)are strictly negative,
with exact maximum
max
i∈[576]
ci(κ0, r0) =− 12977579752000390297
84375000000000000000 ≈ −0.15380835<0.
 All2 ,700 = 9 × 5 × 5 × 3 × 4tensor Bernstein coefficients of Hales’ five-dimensional
opposite-turn polynomial( L2 −B )/P [4, Claim V6] in exact multidegree(8 , 4, 4, 2, 3)
on[0 , 1]5 are strictly positive, with exact minimum23 /768 ≈ 0.029948and exact
maximum11/16.
(b) Exact affine sensitivity and parameter sharpness of Claim V11:Because the
Claim V11 certificate polynomial is separately affine in κ and r, its exact feasibility intervals
preserving strict negativity of all576Bernstein coefficients are( κmin,∞)at r = 2/9and
(rmin,∞)atκ= 583/500, with exact rational thresholds
κmin = 46959602180349654400000
40281410969445390120837 ≈1.16578841, κ 0 −κ min ≈2.1159×10 −4 (0.018%),
rmin = 11912668174415313643683
53911400000000000000000 ≈0.22096752, r 0 −r min ≈1.2547×10 −3 (0.565%).
In determinant terms ( detS <1/(4κ2)), Hales’ weights extend the cap only from0 .183884
(at κ0) to0 .183950(at κmin), while all six auxiliary box guards in Hales’ winding verifier
remain strictly satisfied at both boundary endpoints( κmin, r0)and( κ0, rmin), demonstrating
that Hales’ chosen rational parameters are near-optimal.
3 Proof of Theorem 1: Exact Curvature and Global s-Stability
Proof of Theorem 1. Write ¯q0 = cosθ , ¯q1 = sinθ , s = ¯q0 + ¯q1, and ψ(¯q1) := Anorm(
p
1−¯q2
1,¯q1).
By symmetry Anorm(cosθ,sinθ ) = Anorm(sinθ,cosθ ), it suffices to work on θ∈ (0, π/4] (where
0 <¯q1 ≤¯q0 and s∈ (1,
√
2]). From Hales [ 4, Eq. (10.8)], with c := 2 + 2¯q0 ¯q1 = 1 + s2 and
wc(x) := (2x+c) lnx
1−x ,
− d
dθAnorm(cosθ,sinθ) =−ψ ′(sinθ) cosθ= 2
 
(s+ 1)(w c(¯q0)−w c(¯q1)) +s(s−1)(¯q0 −¯q1)

(s+ 1)(s+ 3) 2 ,
(9)
where the factor ¯q0 = cosθin the denominator ofψ ′(¯q1) cancels identically!
For part (a), differentiate (9) at θ = π/4, where ¯q0 = ¯q1 = 1/
√
2, s =
√
2, c = 3, and
d
dθ (¯q0 −¯q1) = −
√
2. Using w′
3(1/
√
2) = 4
√
2−2−5 ln 2
3−2
√
2 and rationalizing (
√
2 + 3)2 = 11 + 6
√
2
(norm 112 − 2 · 62 = 49) together with (3 + 2
√
2)(11 − 6
√
2) = 9 + 4
√
2 (all integer arithmetic
verified in Lean Theorem 1 andcert01), we obtain
A′′
norm(π/4) = 2
√
2
 
(
√
2 + 1)w′
3(1/
√
2) +
√
2(
√
2−1)

(
√
2 + 1)(
√
2 + 3)2
= 2
√
2(4
√
2−2−5 ln 2)(9 + 4
√
2) + 4(3−2
√
2)(11−6
√
2)
49
= 340−132
√
2−(80 + 90
√
2) ln 2
49 ,
4

--- Page 5 ---
Figure 1:(a)Exact four-arc density excess Anorm(cosθ,sinθ ) −δ oct versus our global elementary
s-bound and quadratic bound (4) (cert01–cert03).(b)Exact linear-vs.-quadratic stability
dichotomy on log–log axes comparing Hales’ six-arc mixed family (slope 1, cert05–cert06)
against the four-arc forward family (slope 2) relative to Fei Xue’s competitor ceiling gap
8.17×10 −7 (cert04).
proving (3).
For part (b), Hales’ logarithmic derivative bound w′
c(x) ≥ c−2
2x = ¯q0 ¯q1
x ([4, Lemma 10.2])
together with the elementary inequality ln(¯q0/¯q1) = 2 artanh
 ¯q0−¯q1
¯q0+¯q1

> 2(¯q0−¯q1)
s gives
wc(¯q0)−w c(¯q1) =
Z ¯q0
¯q1
w′
c(x)dx≥¯q 0 ¯q1 ln ¯q0
¯q1
≥ 2¯q0 ¯q1(¯q0 −¯q1)
s = (s2 −1)(¯q0 −¯q1)
s ,
using 2¯q0 ¯q1 = s2 − 1 (Lean Theorem 2). Substituting into (9) and factoring (s + 1)(s2 − 1) +
s2(s− 1) = (s− 1)(2s2 + 2s + 1) (Lean Theorem 3), while observing ds
dθ = cosθ−sinθ = ¯q0 −¯q1,
yields the purely algebraic differential inequality
− d
dθAnorm(cosθ,sinθ)≥g(s) (s−1) ds
dθ, g(s) := 2(2s2 + 2s+ 1)
s(s+ 1)(s+ 3) 2 .
Direct differentiation gives g′(s) = −2(4s4+8s3+8s2+9s+3)
s2(s+1)2(s+3)3 < 0 for all s >0 (Lean Theorem 4,
cert12), so g(s) ≥g (
√
2) on [1 ,
√
2]. Integrating from θ to π/4 (i.e., u∈ [s,
√
2]) and usingR√
2
s (u−1)du= 1
2 (
√
2−s)(
√
2 +s−2)≥
√
2−1
2 (
√
2−s) (Lean Theorem 7) yields
Anorm(cosθ,sinθ)−δ oct ≥
√
2−1
2 g(
√
2) (
√
2−s) = 125
√
2−172
98 (
√
2−s)
(rationalized in Lean Theorems 5–6, cert02–cert03). Finally,
√
2−s = 2
√
2 sin2 π/4−θ
2

; by
concavity of sin on [0, π/8], sinu≥ sin(π/8)
π/8 u = 4
√
2−
√
2
π u, whence
√
2−s≥ 16(
√
2−1)
π2 (θ−π/ 4)2,
proving (4). Substituting Xue’s certified gap C∗/2 −δ oct < 8.17003 × 10−7 (cert04, Lean
Theorem 11) immediately gives |θ−π/ 4| ≤
p
(C∗/2−δ oct)/cθ < 4.9962 × 10−3 rad and (5)
(Figure 1(a)).
4 Proof of Theorem 2: Dichotomy and Regular-Walk Spectrum
Proof of Theorem 2. For part (a), along Hales’ six-arc mixed family [ 4, Remark 8.3, Claim V5]
(with ρ := 1 +
√
2, vmax = 4
(1+ρ)2−1 = 4(4
√
2−5)
7 , and ϕ(v) := v+4
(1+ρ)2v ≥ 1), the exact period area
5

--- Page 6 ---
Table 1: Certified regular all-forward walk spectrum N = 3m + 1 (2N-gon smoothed polygons,
[4, Remark 9]; outward-rounded pure-integer intervals of width<10 −10 incert07,cert13).
m N(2N-gon) Certified densityδ N Certified detS N Above cap 9193/50000?
1 4 (8-gon,K oct) 0.9024141830 0.1801960993 No (unique)
2 7 (14-gon) 0.9060517532 0.1861080691 Yes
3 10 (20-gon) 0.9066066235 0.1870179882 Yes
4 13 (26-gon) 0.9067656455 0.1872793158 Yes
5 16 (32-gon) 0.9068275491 0.1873811560 Yes
6 19 (38-gon) 0.9068565024 0.1874288232 Yes
7 22 (44-gon) 0.9068718167 0.1874540495 Yes
8 25 (50-gon) 0.9068806654 0.1874686316 Yes
∞Circle limitπ/(2
√
3)≈0.9068996821 3/16 = 0.1875000000 Yes
and its first derivative are
Amix(v) =
√
3
2
 
4 +v
 
3−ρ 2 ln 2−lnϕ(v)

,
A′
mix(v) =
√
3
2

3−ρ 2 ln 2−lnϕ(v) + 4
v+ 4

.
Differentiating once more using (lnϕ(v)) ′ = 1
v+4 − 1
v gives
A′′
mix(v) =
√
3
2
1
v − 1
v+ 4 − 4
(v+ 4) 2

=
√
3
2 · (v+ 4) 2 −v(v+ 4)−4v
v(v+ 4) 2 = 8
√
3
v(v+ 4) 2 >0
for all v >0 (numerator identity = 16 proved in Lean Theorem 10), establishing(6). At v = vmax,
ϕ(vmax) = 1 and 4
vmax+4 = 5+4
√
2
6+4
√
2 = 2
√
2−1
2 (Lean Theorem 8), so dividing A′
mix(vmax) by 2
√
3
gives δ′
mix(vmax) = 1
4
 5+2
√
2
2 − (3 + 2
√
2) ln 2

= −λmix < 0 (strict negativity proved in Lean
Theorem 9). By global convexity (6), the supporting tangent at vmax lies strictly below δmix on
(0, vmax), yielding (7) (cert05–cert06, Figure 1(b)).
For part (b), on Hales’ regular all-forward branch N = 3m + 1 (φ = mπ/N, q = 2 cosφ ,
p2 = 4q/(4 −q ), [ 4, Remark 9]), exact pure-integer outward-rounded interval evaluation of
δN = N
8 (3p2 −4−p2 lnq ) and detS N =
 2(2+q/4−lnq)
(4−q)2
2 sin2 φ over m = 1, . . . ,8 produces Table 1
(cert07,cert13–cert14, Lean Theorems 12 and 17, Figure 2(a)), certifying (8).
5 Proof of Theorem 3: Zero-Float Bernstein Certification and
Sensitivity
Proof of Theorem 3. For any univariate degreen, let Bn ∈Q (n+1)×(n+1) be the collocation matrix
(Bn)ij =
 n
j

(i/n)j(1 −i/n )n−j (0 ≤i, j≤n ). Since the Bernstein basis spans polynomials of
degree ≤n , Bn is invertible over Q (verified explicitly via BnB−1
n = I in pure Fraction Gauss–
Jordan elimination, test 49). For any multivariate polynomial P of multidegree (d1, . . . , dk) on
[0, 1]k, applying B−1
dr sequentially along each axis r = 1, . . . , kto the exact rational evaluations of
P on the tensor grid Qk
r=1{0, 1/dr, . . . ,1} recovers its unique exact tensor Bernstein coefficients.
For Hales’ Claim V11 [4, Section 11], the four sign polynomials on [0 .577, 0.81]2 ×[0.599, 1.1]2
have coordinate degree bounds (4 , 4, 2, 2), and multiplying by the four multiaffine corner-
interpolated nonnegative weight polynomials ω1, . . . , ω4 produces a polynomial PV11(κ, r; t) of
multidegree (5, 5, 3, 3) (576 coefficients). Pure-rational reconstruction at ( κ0, r0) = (583/500, 2/9)
recovers all 576 coefficients strictly negative with exact maximum ≈ −0.15380835 (displayed
6

--- Page 7 ---
Figure 2:(a)Exact regular-walk determinant spectrum detS N ↑ 3/16 (N = 3m + 1, cert07),
showing N = 4 (smoothed octagon) as the unique walk below Hales’ competitive cap 9193 /50000.
(b)Exact affine sensitivity of the largest of the 576 Claim V11 tensor Bernstein coefficients
versus κ0 (cert08–cert09), exposing the razor-sharp downward margin κ0 −κ min ≈ 2.12 ×10−4
(0.018%).
exactly in Theorem 3(a), cert08, Lean Theorems 13–14). Because PV11(κ, r; t) is affine in κ
(at fixed r0) and affine in r (at fixed κ0), each of the 576 Bernstein coefficients has the exact
form ci(κ) = a0,i + κa1,i (resp. d0,i + rd1,i). Solving all 576 exact linear inequalities ci(κ) < 0
(resp. < 0 in r) over Q proves a1,i < 0 on every active constraint (hence unbounded above) and
yields the exact rational infima κmin and rmin stated in Theorem 3(b), while verifying that all
six auxiliary box guards in Hales’ check winding.py remain strictly satisfied at both ( κmin, r0)
and (κ0, rmin) (cert09, Figure 2(b)).
For Hales’ Claim V6 [4, Section 11], the algebraic implication P = 0 =⇒M = 1, y= j =
0 =⇒L 2 −B = 1
4 − 1
4 = 0 shows that P divides L2 −B identically in Q[p1, p2, p3, p4, p5], and
coordinate degree inspection bounds the quotient ( L2 −B )/P on [0, 1]5 by exact multidegree
(8, 4, 4, 2, 3) (9 · 5 · 5 · 3 · 4 = 2,700 coefficients). Pure-rational tensor Bernstein inversion recovers
all 2,700 coefficients strictly positive with exact minimum 23 /768 and exact maximum 11 /16
(cert10, Lean Theorem 15).
6 Formal Verification and Reproducibility
All stability constants, interval brackets, and Bernstein certificates are verified by three comple-
mentary zero-trust artifacts with an explicit division of labor:
1. Constructive Lean 4.36.0 proof suite( lean/ReinhardtQuantitativeStability.
lean): 20 theorems compiling under lean -DwarningAsError=true with zero external
dependencies, zero sorry, zero Classical.choice, and zero custom axioms, formally prov-
ing all finite integer/rational algebraic identities, Q(
√
2) normalizations, and guard/margin
inequalities—namely the curvature and cs identities (Theorems 1–7, 18), six-arc mixed
convexity and linear slope negativity (Theorems 8–10), Xue’s ceiling gap and Hales’
determinant/parameter guards (Theorems 11–17), and Hales’ turn-positivity identities
(Theorems 19–20), using certified ln 2 rational brackets from cert01 and cert04 where
transcendental bounds enter.
2. AST-audited zero-float verifier:The script verify reinhardt stability.py inside
verification/ uses strictly int and Fraction (forbidding float, math, sympy, and
7

--- Page 8 ---
limit denominator), certifying all transcendental interval evaluations (including regular
walks to width < 10−10) and sealing 16 SHA-256 JSON certificates ( cert01–cert16),
including the full 576-coefficient Claim V11, 2,700-coefficient Claim V6, and auxiliary-guard
sensitivity reconstructions.
3. Adversarial test suite( tests/test_adversarial.py): 56 automated pytest checks
auditing zero-float AST compliance, SHA-256 manifest integrity, interval tightness (< 10−8
globally and < 10−10 on Table 1), Bernstein matrix inversion, all 16 certificates, and Lean 4
axiom purity.
AI Disclosure.Google Antigravity assisted with the four-arc curvature and s-antiderivative
proofs, the six-arc mixed convexity proof, independent pure-rational Bernstein reconstruction,
Lean 4 formalization, and manuscript drafting. All mathematical proofs, certificates, and claims
were audited and verified by Lluis Eriksson.
References
[1] L. Fejes T´ oth, “Some packing and covering theorems,”Acta Scientiarum Mathematicarum
(Szeged), vol. 12A, pp. 62–67, 1950.
[2] T. C. Hales, “On the Reinhardt conjecture,”Vietnam Journal of Mathematics, vol. 39,
pp. 287–307, 2011 (arXiv:1103.4518).
[3] T. C. Hales, “The Reinhardt conjecture as an optimal control problem,” preprint
arXiv:1703.01352, 2017.
[4] T. C. Hales, “Streamlining Three Recent Proofs of the Reinhardt Conjecture,” Hexagon
preprinthexagon:2611.01057v1, November 2026.
[5] K. Mahler, “On the minimum determinant and the circumscribed hexagons of a convex
domain,”Proc. Kon. Ned. Akad. Wet., vol. 50, pp. 692–703, 1947.
[6] K. Reinhardt, “ ¨Uber die dichteste gitterf¨ ormige Lagerung kongruenter Bereiche in der
Ebene und eine besondere Art konvexer Kurven,”Abhandlungen aus dem Mathematischen
Seminar der Universit¨ at Hamburg, vol. 10, pp. 216–230, 1934.
[7] F. Xue, “A proof of the Reinhardt conjecture,”arXiv:2611.21470v2, November 2026.
8
