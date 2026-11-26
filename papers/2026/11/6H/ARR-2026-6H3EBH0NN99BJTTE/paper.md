# Exact Dilogarithm Higher-Loop Collapse, All-Moments Gravitational-Clock Tauberian Law, and Matter-Content Sign Barrier in Null-Cone Quantum Gravity

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6H3EBH0NN99BJTTE` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/null-cone-gravity-sharp-resummation-tauberian (`v1.0.0`)  
**Canonical PDF SHA-256:** `5d220b3c5631f564ff0bca051e9dbf9c137776de08acbb0f31881e66566d2eb0`

## Abstract

We establish three exact analytical, quantitative, and structural advances over Chandrasekaran's null-cone algebraic quantization of four-dimensional gravity (arXiv:2611.34924v1). First (Theorem 1), for the nonperturbative graviton pair amplitude A(s) = Li_2(e^{-2i/s})/(2s^2) (s = A/(4 G_N hbar)), we prove exact higher-loop collapse of the real part Re A(s) = pi^2/(12 s^2) - pi/(2 s^3) + 1/(2 s^4) across the entire macroscopic regime s >= 1/pi (zero corrections at order G_N^5 and above), characterize the infinite sequence of Planckian C^0 cusps at s_m = 1/(pi m) with exact derivative jump -pi^5 m^4, derive a strictly negative convergent Clausen-Bernoulli remainder series for Im A(s) yielding certified non-asymptotic two-sided rational brackets, and determine the exact UV mode cutoff N_eff(s) = (e^{1-gamma_E}/2) s matching perturbative and nonperturbative logarithms. Second (Theorem 2), we generalize the clock-Tauberian analysis of causal-diamond black-hole entropy to an exact all-moments Beta(alpha, 1) law mu_p = alpha/(alpha + p) (recovering Footnote 23 at p = 2), prove a universal Golden-Ratio clock-variance ceiling Var_infty(U) <= phi^{-5} = (5 sqrt(5) - 11)/2 attained uniquely at alpha_* = phi^{-1}, upgrade the qualitative o(log <s>) remainder to an explicit non-asymptotic finite-ell entropy envelope, audit pure gravity (q = 257/302, x^2 = 257/347, Var = 520425/31647788), and prove a sharp Matter-Content Sign Barrier: any 4D theory with fixed-mass logarithmic coefficient c_mass <= -1/2 (including pure Einstein-Yang-Mills for all n_V >= 20, such as SU(5), SO(10), and E_8) cannot admit a power-law clock trace with q in (0, 1). Third (Theorem 3), we sharpen the one-loop focusing entropy prefactor from linear O(C) to optimal O(C^{1/4}) via an exact quartic AM-GM identity (a 2.68x improvement at C = 1 and 73.4x at C = 100), strictly tighten the symplectic-area focusing bound from e(1 + log R) to e log R (and R for R <= e), and prove exact exponential UV-cutoff error bounds for the two-sided shear and Raychaudhuri area-fluctuation correlators. All algebraic and combinatorial cores are formalized constructively in zero-dependency Lean 4.35.0 (18 theorems, 0 sorry, 0 Classical.choice) and verified by an AST-audited zero-float Python verifier issuing 16 SHA-256 certificates and passing 66/66 tests.

## Full Extracted Text

--- Page 1 ---
Exact Dilogarithm Higher-Loop Collapse, All-Moments
Gravitational-Clock Tauberian Law, and
Matter-Content
Sign Barrier in Null-Cone Quantum Gravity
Lluis Eriksson∗
November 26, 2026
Abstract
In a recent monograph, Chandrasekaran (arXiv:2611.34924v1) constructs an algebraic
quantization of four-dimensional Lorentzian gravity on intersecting null cones, deriving a
finite nonperturbative graviton pair amplitudeA(s) = Li2(e−2i/s)/(2s2), a causal-diamond
gravitational-clock Tauberian formula reproducing the Bekenstein–Hawking entropy and
Ashoke Sen’s106 /45one-loop Schwarzschild logarithmic correction, one-loop focusing bounds
on logd(s), and a two-sided shear correlator across disconnected horizons. We establish
three exact analytical, quantitative, and structural advances over this framework. First
(Theorem 1), we prove that on the entire macroscopic regimes = A/(4GNℏ) ≥1/π, the
real part collapses identically to the degree-4polynomialℜA(s) = π2
12s2 − π
2s3 + 1
2s4 (zero
perturbative corrections at orderG5
N and beyond), while at every Planckian area resonance
sm = 1/(πm)( m∈Z ≥1) it exhibits aC0 cusp with exact first-derivative jump−π5m4. For
ℑA(s), we derive a strictly negative convergent Clausen–Bernoulli remainder series yielding
certified non-asymptotic two-sided rational brackets at everys> 1/π, and determine the exact
effective UV mode cutoffNeff(s) = 1
2 e1−γE s≈ 0.7631026 s matching the finite-N perturbative
cubic divergence to the nonperturbative logarithm. Second (Theorem 2), we upgrade the
clock-Tauberian analysis to an exact all-momentsBeta(α,1)law µp = α/(α+p)( α= q/(1−q),
recovering Footnote 23 atp = 2), prove a universal Golden-Ratio clock-variance ceiling
Var∞(ˆ¯u∗/ℓ) ≤φ−5 = (5
√
5−11)/2 ≈0.090170attained uniquely at α∗= φ−1, replace the
qualitative o(log⟨ˆs⟩)entropy remainder with an explicit non-asymptotic finite-ℓ two-sided
envelope, audit pure gravity (q = 257/302, x2 = 257/347, Var = 520425/31647788), and
establish a sharpMatter-Content Sign Barrier: any 4D theory with fixed-mass logarithmic
coefficient cmass ≤−1/2—including pure Einstein–Yang–Mills for allnV ≥20(such as SU(5),
SO(10), andE8)—cannot admit a power-law clock trace withq∈(0,1). Third (Theorem 3),
we sharpen the one-loop focusing entropy prefactor from linearO(C)to optimal O(C1/4)via
an exact quartic AM–GM identity (2.68×sharper at C = 1,73 .4×at C = 100), strictly
tighten the symplectic-area focusing bound frome(1 +logR)to elogR (and Rfor1 ≤R≤e ),
and prove exact exponential UV-cutoff error bounds for the two-sided shear and Raychaudhuri
area-fluctuation correlators. All algebraic and combinatorial cores are formalized constructively
in zero-dependency Lean 4.35.0 (18theorems,0 sorry,0 Classical.choice) and verified by
an AST-audited zero-float Python verifier issuing16SHA-256 certificates and passing66/66
tests.
∗Independent researcher. Authored by Lluis Eriksson with AI-assisted formal verification, exact-arithmetic
software generation, and mathematical drafting (Google Antigravity). Manuscript and figures licensed CC-
BY-4.0; verification repository, Lean 4 formalization, and exact rational certificates licensed MIT athttps:
//github.com/lluiseriksson/null-cone-gravity-sharp-resummation-tauberian.
1

--- Page 2 ---
1 Introduction
Chandrasekaran’s null-cone quantization of four-dimensional general relativity [1] addresses several
foundational problems of Lorentzian quantum gravity directly from first-order Palatini–Plebański
variables on intersecting null cones: ultraviolet finiteness of a resummed graviton pair overlap
(Section 4.3), finite dimensionality of causal-diamond Hilbert spaces and recovery of the Bekenstein–
Hawking entropy plus Sen’s one-loop logarithmic correction [2] via a gravitational clock operator
ˆ¯u∗ (Section 5.3), one-loop focusing bounds on graviton state countsd(s)and symplectic areas
(Appendix D.3), and restoration of two-sided horizon correlators from entangled disconnected
caps (Section 5.4).
Several key analytical estimates in [1] are left qualitative, asymptotic, or specialized to pure
gravity. In this paper we prove exact, non-asymptotic, and sharp upgrades across all three pillars:
1. Exact dilogarithm resummation and Planckian non-analyticity (Section 2):We
prove exact vanishing of all perturbative loop orders≥G5
N in ℜA(s)for s≥ 1/π, locate all
Planckian cuspssm = 1/(πm)with exact derivative jump−π5m4, derive strictly sign-definite
convergent Clausen–Bernoulli two-sided brackets forℑA(s), and compute the exact UV
matching constantNeff(s)/s=e 1−γE/2.
2. All-moments Tauberian Beta-law, Golden-Ratio variance ceiling, finite-ℓ bounds,
and Matter-Content Sign Barrier (Section 3):We generalize Footnote 23 of [1]
from p= 2to all moments p> 0, establish the universal variance boundVar∞(U) ≤φ−5,
provide an explicit finite-ℓentropy error envelope, and prove that the clock-Tauberian power
law breaks down sharply whenever Sen’s 4D fixed-mass coefficient satisfiescmass ≤−1/2
(nV ≥20in pure Einstein–Yang–Mills).
3. Sharp focusing constants and exponential shear-correlator UV bounds (Sec-
tion 4):We optimize the bosonic focusing partition parameterβin Appendix D.3 of [1] from
linear O(C)to optimal O(C1/4), strictly improve the symplectic-area bounde(1 +logR)for
everyR≥1, and derive exact exponential UV-cutoff error bounds on Eqs. (5.76)–(5.77b).
Table 1 summarizes our quantitative advances over [1].
Table 1: Summary of exact and non-asymptotic advances over Chandrasekaran [1].
Quantity / Section Chandrasekaran (arXiv:2611.34924v1) This Work (Theorems 1–3)
ℜA(s)(Eq. 4.33) Qualitative convergence fors>0ExactO(G 4
N)collapse (s≥1/π); cusps
sm = 1/(πm), jump−π5m4
ℑA(s)−ilogs/s 3 leading behavior Exact Clausen–BernoulliQbrackets;
Neff(s) = 1
2 e1−γE s
Clock moments (Fn. 23)p= 2only (q= 2x 2/(1 +x2)) Allp>0:µ p =α/(α+p),Var ∞≤φ−5
Entropy remainder
(Eq. 5.65)
Qualitativeo(log⟨ˆs⟩)Explicit two-sided finite-ℓintegral envelope
4D matter coupling
(Eq. 5.69)
Pure gravity (106/45,q= 257/302) Exact Sign Barrierc mass >−1/2(n V ≤19in
EYM)
Focusinglogd(s)
(Eq. D.46c)
≲ϵ 1 + (sQ∗)3/4 (O(C)prefactor) Optimal 4π
3·51/4 C1/4(sQ∗)3/4 (2.68×atC= 1)
Symplectic area (Eq. D.52b)e(1 + logR)Strictly sharper:R(R≤e),elogR(R>e)
Two-sided shear
(Eqs. 5.76–77)
ExactΛ =∞integral only Exponential UV cutoff errorO(Λe −πΛ)
2 Exact Dilogarithm Collapse and Clausen–Bernoulli Bounds
In Section 4.3 of [1] (Eq. 4.33), the connected overlap of quadratic graviton pair insertions with
affine-shift phasee−ik/s (s=A/(4G Nℏ)>0) sums absolutely to
A(s) := Li2(e−2i/s)
2s2 = 1
2s2
∞∑
k=1
e−2ik/s
k2 ,(1)
2

--- Page 3 ---
whereas differentiating termwise prior to summing yields the logarithmic UV divergence−i
s3 HN =
−i
s3
∑N
k=1 k−1 at orderG3
N (Eq. 4.34). We establish the exact analytic structure of both real and
imaginary parts across alls>0.
Theorem 1(Higher-loop collapse, Planckian cusps, Clausen–Bernoulli brackets, and UV match-
ing).Lets>0,θ:= 2/s,m:=⌊1/(πs)⌋∈Z ≥0, and ˜θ:=θ−2πm∈[0,2π).
(a)Exact real-part higher-loop collapse and Planckian cusps:For everys>0,
ℜA(s) = 1
2s2
(
π2
6 −π
2
˜θ+ 1
4
˜θ2
)
.(2)
In particular, across the entire macroscopic regimes≥ 1/π (A≥ 4
πGNℏ, m= 0), ℜA(s)
collapses identically to a three-term polynomial in1/s∝GN:
ℜA(s) = π2
12s2 − π
2s3 + 1
2s4 (∀s≥1/π),(3)
so every perturbative correction at orderGk
N (k≥ 5) vanishes identically. Moreover,
2s2ℜA(s)attains its global minimum −π2/12at smin = 2 /π and vanishes on[1 /π,∞)
precisely at the two rootsszero,2 = 2 /(π(1 + 1/
√
3)) ≈0.40360and szero,1 = 2 /(π(1 −
1/
√
3)) ∈ (4/π,5/π) ≈ 1.50626(the outermost macroscopic zero). At each Planckian
resonance sm = 1 /(πm)( m∈Z ≥1), ℜAis continuous with valueℜA(sm) = π4m2
12 but
non-differentiable, having exact one-sided derivative jump
lim
s→s+
m
(ℜA)′(s)−lim
s→s−
m
(ℜA)′(s) =−π5m4.(4)
(b) Convergent Clausen–Bernoulli series and non-asymptotic brackets:For every
s>1/π,
ℑA(s) =− 1
s3
(
1 + ln s
2
)
−
∞∑
n=1
cn
s2n+3 , c n := |B2n|2 2n
2n(2n+ 1)! >0,(5)
with exact leading coefficients c1 = 1
18 , c2 = 1
900 , c3 = 1
19845 , and c4 = 1
340200 . Ev-
ery magnitude an(s) := cn/s2n+3 is strictly positive and satisfies the strict ratio decay
an+1(s)/an(s) <(πs)−2 <1for all n≥ 1. Consequently, for every truncation orderM≥ 1
and everys>1/π,
−
M∑
n=1
an(s)− aM+1 (s)
1−(πs) −2 <ℑA(s) + 1 + ln(s/2)
s3 <−
M∑
n=1
an(s).(6)
(c) Exact UV cutoff matching law:Matching Eq. (4.34) of [1] (−i
s3 HN) to the leading
nonperturbative logarithm in(5)fixes the unique effective UV mode cutoff
Neff(s) = e1−γE
2 s, e1−γE
2 ∈[0.763102555,0.763102557],(7)
yielding
⏐⏐ℑA(s) +H⌊Neff(s)⌋/s3⏐⏐=O(s−4)ass→∞(verified inC02,C04).
Proof. For (a), the standard Fourier series of the second Bernoulli polynomialB2(x) = x2 −x+1/6
on x∈ [0,1]reads ∑∞
k=1
cos(2πkx)
k2 = π2B2(x)[ 3]. Setting x= ˜θ/(2π) ∈[0,1)and dividing by2 s2
gives (2), which collapses to(3) whenever0 < θ≤2π, i.e. s≥ 1/π. Writing u = ˜θ/π∈ [0,2],
2s2ℜA(s) = π2
12 (3u2 −6u+2) = π2
12 (3(u−1)2 −1)(formalized in Lean 4 asreal_part_minimum_sos
and real_part_zero_bracket), yielding the global minimum atu= 1( s= 2/π) and the zeros
3

--- Page 4 ---
u = 1 ±1/
√
3. At sm = 1 /(πm), θ(s±
m) = 2 πm∓ 0+, so ˜θ(s+
m) = 2 π− where g′(˜θ) = + π/2
and ˜θ(s−
m) = 0 + where g′(˜θ) = −π/2for g(θ) = π2
6 −π
2 θ+ 1
4 θ2. Differentiating g(˜θ(s))
2s2 gives
(ℜA)′(s) =−g(˜θ)
s3 −g′(˜θ)
s4 ; sincegis continuous acrosss m, the jump is−π/2−(−π/2)
s4m
=−π5m4.
For (b),ℑLi 2(e−iθ) = −∑∞
k=1
sin(kθ)
k2 = −Cl 2(θ). Since Cl′
2(θ) = −ln (2 sin(θ/2)) = −lnθ +
∑∞
n=1
|B2n|
2n(2n)! θ2n on0 < θ <2π, termwise integration gives the classical Bernoulli expansion
Cl2(θ) = θ(1 −lnθ ) + ∑∞
n=1
|B2n|
2n(2n+1)! θ2n+1 [3], valid absolutely on0 < θ <2π (s > 1/π).
Substitutingθ= 2/sand negating yields (5). By Euler’s identity|B 2n|/(2n)! = 2ζ(2n)/(2π)2n,
an+1(s)
an(s) = ζ(2n+ 2)
ζ(2n) · n(2n+ 1)
(n+ 1)(2n+ 3) · 1
(πs)2 < 1
(πs)2 ,
because ζ(2n)strictly decreases with n≥ 1and n(2n+ 1) <(n+ 1)(2n+ 3)(Lean 4: clausen_
bernoulli_ratio_strict). Bounding the negated tail by−∑∞
j=0 aM+1 (s)(πs)−2j proves (6).
For (c),HN = lnN +γE+O(1/N)matches1 + ln(s/2)uniquely when lnN +γE = 1 +ln(s/2),
giving (7). Figure 1 illustrates both the Planckian cusp structure and the rapid geometric
tightening of the Clausen–Bernoulli brackets.
Figure 1:Dilogarithm higher-loop collapse and Clausen–Bernoulli brackets.(a) Rescaled
real part2 s2ℜA(s)showing exact collapse onto the O(G4
N)polynomial for s≥ 1/π, global
minimum −π2/12at s = 2 /π, and Planckian C0 cusps at sm = 1 /(πm)with jump −π5m4.
(b) Certified non-asymptotic bracket width onℑA(s)from (6) for M∈{ 1,2,4,6}, reaching
<10 −16 ats= 10,M= 6(certificateC04).
3 All-Moments Clock Tauberian Law, Golden-Ratio Ceiling, and
Matter-Content Sign Barrier
In Section 5.3 of [1], the causal-diamond thermal traceZ(ℓ) := ∑
¯u∗,i≤ℓe−si defines the normalized
clock momentsµp(ℓ) := Eℓ[(ˆ¯u∗/ℓ)p]( p> 0). When µ1(ℓ) →q∈ (0,1), Eq. (5.58) giveslogZ(ℓ) =
[α+ o(1)] log(ℓ/ℓ0)with α := q/(1 −q ) > 0, yielding the causal-diamond entropyS(ρD) =
⟨ˆA⟩
4GNℏ + α
2 log⟨ˆs⟩+ o(log⟨ˆs⟩)(Eq. 5.65). In Footnote 23 (Eqs. 5.60–5.61), Chandrasekaran derives
the p = 2identity q = 2x2/(1 + x2)where x2 = limµ2(ℓ), and in Eqs. (5.67c)–(5.69) obtains
q= 257/302and fixed-mass logarithmic coefficientc mass = α
2 −1
2 = 106/45for pure 4D gravity.
Theorem 2(All-moments Beta-law, Golden-Ratio variance ceiling, finite-ℓenvelope, and Matter–
Content Sign Barrier).Let Z(ℓ) = ∑
¯u∗,i≤ℓe−si >0be nondecreasing with nonnegative spectrum
¯u∗,i ≥0, and letα:=q/(1−q)>0forq∈(0,1).
4

--- Page 5 ---
(a) Exact universalp-th moment identity andBeta(α,1)law:For every real p> 0and
everyℓ>0, Stieltjes integration by parts gives
µp(ℓ) = 1− p
ℓpZ(ℓ)
∫ℓ
0
tp−1Z(t)dt,(8)
and for any0 <a<b and0 ≤u≤ℓ , the generalized kernel identityua = ub/ℓb−a + (b−
a)
∫ℓ
u ubt−(b−a+1) dt holds (recovering Eq. (5.60) at(a,b) = (1,2)). Whenever µ1(ℓ) →q∈
(0,1), the normalized clockUℓ := ˆ¯u∗/ℓ converges in distribution toBeta(α,1)with exact
all-moments law
lim
ℓ→∞
µp(ℓ) = α
α+p = q
q+p(1−q) (∀p>0),(9)
recovering Footnote 23 (p = 2: x2 = q/(2 −q) ⇐⇒q = 2x2/(1 + x2)) and Footnote 24
(Pr(ˆs≤as∗)→a α/2) as immediate corollaries.
(b) Golden-Ratio universal clock-variance ceiling:Across all α >0(equivalently all
q∈ (0,1)), the limiting clock varianceVar∞(U) = µ2 −µ2
1 = α
(α+1)2(α+2) = q(1−q)2
2−q satisfies
the exact sharp ceiling
Var∞(U)≤φ −5 = 5
√
5−11
2 ≈0.0901699437,(10)
attained uniquely atα∗= φ−1 = (
√
5−1)/2( q∗= φ−2 = (3 −
√
5)/2), certified algebraically
by the exactZ[
√
5]norm factorization
(
2(x+y) 2(x+ 2y)−11xy 2)2 −125x2y4 = 4(x2 +xy−y 2)2(x2 + 6xy+ 4y2)≥0.(11)
(c) Quantitative non-asymptotic finite-ℓ entropy envelope:Set∆ ent(ℓ,ℓ0) := ln Z(ℓ)
Z(ℓ0) −
αln ℓ
ℓ0
. If|µ1(t)−q|≤ε(t)<1−qfor allt∈[ℓ 0,ℓ], then unconditionally
∆ent(ℓ,ℓ0)≥ −
∫ℓ
ℓ0
ε(t)
(1−q)(1−q+ε(t))
dt
t + ln 1−q−ε(ℓ 0)
1−q+ε(ℓ) ,
∆ent(ℓ,ℓ0)≤
∫ℓ
ℓ0
ε(t)
(1−q)(1−q−ε(t))
dt
t + ln 1−q+ε(ℓ 0)
1−q−ε(ℓ) .
(12)
(d) Pure-gravity audit and 4D Matter-Content Sign Barrier:For 4D pure gravity
(cmass = 106/45), α = 257/45and q = 257/302, fixing the exact implied geometric ratio
x2 = 257/347 ≈0.740634and clock variance Var∞(U) = 520425 /31647788 ≈0.016444.
More generally, for 4D Schwarzschild coupled tonS massless scalars, nW = 2 nF Weyl
fermions, andnV gauge vectors, Sen’s local fixed-mass coefficient [2] is
cmass(nS,nW,nV) = 4nS + 7nW −52nV + 848
360 .(13)
Because q∈ (0,1)strictly requires α= 2cmass + 1 >0, a power-law clock trace existsif and
only if
cmass >−1
2 ⇐⇒52n V <1028 + 4nS + 7nW.(14)
In pure Einstein–Yang–Mills (nS = nW = 0), this fails sharply for everynV ≥20(ruling
out pure SU(5)with nV = 24, SO(10)with nV = 45, and E8 with nV = 248), whereas
Einstein–Maxwell (nV = 1) and the massless Standard Model (nS = 4,nW = 45,nV = 12)
lie inside the admissible phase (Table 2).
5

--- Page 6 ---
Proof. For(a), writingZ(ℓ) = ∑
¯u∗,i≤ℓe−si, eachtermsatisfies ℓp−¯up
∗,i = p
∫ℓ
¯u∗,i tp−1 dt, sosumming
over ¯u∗,i ≤ℓ and exchanging sum and integral givesℓpZ(ℓ)(1−µp(ℓ)) = p
∫ℓ
0 tp−1Z(t) dt, proving(8)
(discrete version formalized for all spectra in Lean 4 asdiscrete_stieltjes_moment_identity).
Differentiating F(ℓ) := 1
ℓ
∫ℓ
0 Z(t) dt = (1 −µ1(ℓ))Z(ℓ)yields Eq. (5.57a) of [1], ℓF′(ℓ)/F(ℓ) =
µ1(ℓ)/(1 −µ1(ℓ)) →α , so by Karamata’s representation theorem [4] F and Z are regularly
varying of indexα> 0. By Karamata’s integration theorem,
∫ℓ
0 tp−1Z(t) dt∼ ℓpZ(ℓ)
α+p , so(8) gives
µp(ℓ) →1 − p
α+p = α
α+p, matching all moments ofBeta(α,1)on the compact interval[0,1](hence
convergence in distribution).
For (b), setting α = x/y (x,y > 0), Var∞(U) ≤φ −5 = 2 /(11 + 5
√
5)is equivalent to
2(x+ y)2(x+ 2y) −11xy2 ≥5
√
5xy2. Since2( x+ y)2(x+ 2y) −11xy2 = 2x3 + 8x2y−xy 2 + 4y3
and AM–GM gives8x2y+ 4y3 ≥2
√
32xy2 = 8
√
2xy2 > 11xy2 (as128 > 121), the left-hand
side is strictly positive for allx,y >0. Squaring both sides yields(11), whose nonnegativity and
unique equality locusx2 + xy−y 2 = 0( α= φ−1) are formalized in Lean 4 (golden_ratio_var
iance_ceiling_norm_identity,golden_ratio_variance_norm_nonneg).
For (c), writingln Z(ℓ)
Z(ℓ0) = ln F(ℓ)
F(ℓ0) + ln 1−µ1(ℓ0)
1−µ1(ℓ) and integrating µ1(t)
1−µ1(t) − q
1−q = µ1(t)−q
(1−q)(1−µ1(t))
from ℓ0 to ℓ using |µ1(t) −q|≤ε (t)and monotonicity of u↦→u/(1 −u)(Lean 4: tauberian_in
tegrand_monotone) yields (12) immediately.
For (d), Sen’s 4D Schwarzschild local heat-kernel coefficient in∆S = 1
90 (2nS + 7nF −26nV +
424) logrh [2] becomes(13) in terms oflogsb = 2 logrh + O(1)and nW = 2nF. The fixed-mass
change of variablesdsb/s1/2
b ∝dM in Eq. (5.69) of [1] imposes α
2 −1
2 = cmass, soα= 2cmass + 1 >
0 ⇐⇒(14) (Lean 4: pure_gravity_one_loop_exact_audit , matter_content_sign_barrie
r_eym,matter_content_benchmarks_exact; Figure 2).
Figure 2:Golden-Ratio clock-variance ceiling and 4D Matter-Content Sign Barrier.
(a) Exact limiting clock varianceVar∞(U) = q(1 −q)2/(2 −q)vs. q∈ (0,1), bounded universally
by φ−5 ≈0.09017(unique peak at q∗ = φ−2). (b) Fixed-mass logarithmic coefficientcmass vs.
massless vector countnV: pure Einstein–Yang–Mills crosses the exact clock barriercmass = −1/2
sharply betweennV = 19(admissible) and nV = 20(forbidden), ruling out pureSU(5), SO(10),
andE 8 (certificateC08).
4 Sharp Focusing Entropy Constants and Two-Sided Shear Cor-
relator UV Bounds
Finally, we sharpen the quantitative focusing bounds in Appendix D.3 and the two-sided horizon
correlator Eqs. (5.76)–(5.77b) of [1].
6

--- Page 7 ---
Table 2: Exact one-loop 4D Schwarzschild clock-Tauberian parameters across physical matter
models (certificateC08,n W = 2nF Weyl fermions).
Model(n S,nW,nV)c mass α= 2cmass + 1q= α
α+1 x2 = α
α+2 Var∞(U)Status
Pure Gravity(0,0,0) 106/45 257/45 257/302 257/347 0.016444Admissible
Einstein–Maxwell(0,0,1) 199/90 244/45 244/289 122/167 0.017712Admissible
Massless Standard Model(4,45,12) 37/24 49/12 49/61 49/73 0.025976Admissible
Pure EYM boundary(0,0,19)−7/18 2/9 2/11 1/10 0.066942Admissible
Pure EYM threshold(0,0,20)−8/15−1/15— — —Sign Barrier
PureSU(5)YM(0,0,24)−10/9−11/9— — —Sign Barrier
PureSO(10)YM(0,0,45)−373/90−328/45— — —Sign Barrier
Theorem 3(Optimal focusing entropy prefactor, sharpened symplectic-area bound, and expo-
nential shear-correlator UV bounds).
(a) Optimal one-loop focusing entropy constant (upgrading Eqs. D.45–D.46):Let
{νi >0}be any graviton focusing spectrum satisfying the mode-counting boundN(ν) := |{i:
νi ≤ν}|≤C(sν) 3 for allν >0. Then for everyβ >0,
logd(s)≤βQ ∗−
∑
i
log(1−e −βνi)≤βQ ∗+ π4
15 C
(s
β
)3
.(15)
Optimizing overβ >0attains its unique global minimum atβ∗=
(π4C
5
)1/4(s3/Q∗)1/4, giving
the sharp bound
logd(s)≤ 4π
3·5 1/4 C1/4 (sQ∗)3/4 ≈2.80121C 1/4 (sQ∗)3/4,(16)
improving the linear-in-C prefactor1 + π4
15 C of Eq. (D.46b) (β = (s3/Q∗)1/4) by a factor of
2.68×atC= 1and73.4×atC= 100.
(b) Strict tightening of the symplectic-area focusing bound (Eq. D.52b):For every area
ratio R:= A∗(D)/AP ≥1, optimizingt↦→Rt/t over t∈ (0,1]replaces Chandrasekaran’s
e(1 + logR)(fromt= (1 + logR) −1) by the strictly sharper piecewise bound
h(R) := min
t∈(0,1]
Rt
t =
{
Rif1≤R≤e,
elogRifR>e, strictly<e(1 + logR) (∀R≥1),(17)
yielding
∫
P D(y)2 dA≤ 8(1−ϵ)AP
ϵ h(R)(strictly beating e(1 + logR)for every R≥ 1, and
saving a full additiveefor allR≥e).
(c) Exponential UV-cutoff convergence of the two-sided shear and Raychaudhuri
correlators (Eqs. 5.76–5.77b):For affine separationsuL,uR > 0and dimensionless
graviton frequency cutoffΛ > 0, define G(Λ)
σ (−uL,uR) := − c⊥
uLuR
∫Λ
0
νcos(νln(u L/uR))
sinh(πν) dν.
ThenG (∞)
σ (−uL,uR) =− c⊥
(uL+uR)2 and
⏐⏐G(Λ)
σ (−uL,uR)−G (∞)
σ (−uL,uR)
⏐⏐≤ c⊥
uLuR
· 2e−πΛ
1−e −2πΛ
(Λ
π + 1
π2
)
.(18)
Consequently, the connected Raychaudhuri area-fluctuation correlator⟨∂2
uL
ˆA(2)
L ∂2
uR
ˆA(2)
R ⟩c =
2G2
σ obeys the exact relative error bound
⏐⏐(
G(Λ)
σ
)2 −
(
G(∞)
σ
)2⏐⏐
(
G(∞)
σ
)2 ≤2δ+δ 2, δ:= (uL +uR)2
uLuR
· 2e−πΛ
1−e −2πΛ
(Λ
π + 1
π2
)
,(19)
where the geometric boost amplification factor(uL + uR)2/(uLuR) ≥4attains its unique
minimum4at the symmetric cutu L =uR (Figure 3).
7

--- Page 8 ---
Proof. For (a), expanding−log (1 −e−βνi) = ∑∞
m=1
1
me−mβνi and integrating by parts against
N(ν)≤C(sν) 3 yields
−
∑
i
log(1−e −βνi) =
∞∑
m=1
β
∫∞
0
e−mβνN(ν)dν≤
∞∑
m=1
6βCs3
(mβ)4 = 6Cζ(4)
(s
β
)3
= π4
15C
(s
β
)3
.
Setting A := βQ∗ and B := π4
15 C(s/β)3, our exact quartic polynomial identity27(A+ B)4 −
256A3B = ( A− 3B)2(27A2 + 14AB + 3B2) ≥0(Lean 4: focusing_amgm_quartic_exact ,
focusing_amgm_quartic_nonneg ) proves( A+ B)4 ≥ 256
27 A3B = 256π4
405 C(sQ∗)3 with unique
equality atA= 3B⇐⇒β=β ∗, yielding (16).
For (b), differentiatinglog(Rt/t) = tlogR−logt gives logR = 1 /t, hence t∗ = 1 /logR .
When R>e , t∗∈(0,1)is the unique interior minimizer with valueelogR<e (1 + logR); when
1 ≤R≤e , Rt/t decreases on(0 ,1], so its minimum isR at t= 1, which satisfiesR<e (1 + logR)
strictly for everyR≥1.
For (c), writingL= ln(uL/uR), standard Fourier evaluation shows that
∫∞
0
νcos(νL)
sinh(πν) dν equals
1
4 sech2(L/2) = uLuR
(uL+uR)2 (and atL = 0, expanding 1
sinh(πν) = 2 ∑∞
k=0 e−(2k+1)πν directly yields
2
π2
∑∞
k=0(2k+ 1)−2 = 1
4 , verified inC12). For the tailν≥ Λ, sincesinh(πν) = 1
2 eπν(1 −e−2πν) ≥
1
2 eπν(1−e −2πΛ)and|cos(νL)|≤1,
⏐⏐⏐⏐
∫∞
Λ
νcos(νL)
sinh(πν) dν
⏐⏐⏐⏐≤ 2
1−e −2πΛ
∫∞
Λ
νe−πν dν= 2e−πΛ
1−e −2πΛ
(Λ
π + 1
π2
)
,
proving (18). Finally,( G(Λ)
σ )2 −(G(∞)
σ )2 = ∆G(2G(∞)
σ + ∆G)(Lean 4: raychaudhuri_correla
tor_error_exact) and( uL + uR)2 −4uLuR = (uL −uR)2 ≥0( two_sided_shear_symmetric_
minimum) prove (19).
Figure 3:Optimal focusing entropy prefactor and two-sided shear UV convergence.
(a) Comparison of the Appendix D.3 focusing prefactor1 +π4
15 C vs. our optimalC1/4 prefac-
tor (16) (2.68×sharper atC = 1,73 .4×at C = 100). (b) Guaranteed exponential decay of the
Raychaudhuri relative error(19) vs. graviton frequency cutoffΛ, crossing10−6 atΛ ≈5.5for
symmetric cuts (uL =uR, certificateC11–C12).
5 Formal Verification Architecture and Scope
All algebraic, combinatorial, and exact-rational claims are machine-checked across two independent
formal layers:
8

--- Page 9 ---
1. Constructive Lean 4.35.0 Formalization (lean/NullConeGravitySharp.lean ):
18zero-dependency theorems building cleanly in1 .6s with0 sorry,0custom axioms,0
Classical.choice, and0warnings. These certify the Clausen–Bernoulli strict ratio decay
and leading coefficients, the scaled real-part quadratic minimum and zero bracket, the
cross-multiplied µ1 −µp moment identity and Footnote 23 recovery, the exactZ[
√
5]norm
identity and nonnegativity for the Golden-Ratio variance ceiling, the pure-gravity audit and
Matter-Content Sign Barrier (nV ≤19vs. nV ≥20, plus Einstein–Maxwell and Standard
Model benchmarks), Tauberian integrand monotonicity, the exact quartic AM–GM focusing
identity, symmetric-cut optimality, Raychaudhuri error amplification, and discrete Stieltjes
summation by parts for arbitrary spectra.
2. AST-Audited Zero-Float Rational Verifier (verification/verify_paper103.py ):
Pure Python standard-library verifier (fractions.Fraction, int) audited by its own AST
walker (C16) to forbid all float/complex literals,/, **, float, pow, getattr, and numerical
libraries. All transcendental constants (π, ln 2, e, γE,
√
5) and evaluations (lnx, expx) are
enclosed in certified alternating/Taylor rational brackets. The verifier issues16SHA-256
certificates under protocolNULL-CONE-QG-SHARP-1.0 (Table 3,MANIFEST.json SHA-256:
a5a73d2478822f9f...8eacbaba) and passes66/66pytest checks in3 .05s (including28live
adversarial rejection tests and an independent zero-float Fourier cross-check ofℑA(10)).
Delineation of scope.Classical analytic inputs—the Fourier series ofB2(x)and Cl2(θ)[ 3],
Karamata’s regular-variation theorems [4], and Sen’s 4D Schwarzschild local heat-kernel coeffi-
cient [2]—are standard theorems invoked with full proofs of every new deduction in Sections 2–4,
while every algebraic identity, rational constant bracket, matter-content classification, and finite-
scale error bound is machine-verified in Lean 4.35.0 and exactQ. In particular, our Matter-Content
Sign Barrier (Theorem 2(d)) applies to the fixed-mass power-law clock traceZ(ℓ) ∼ℓα (α> 0,
q∈ (0,1)); resolving how the null-cone quantization behaves whencmass ≤−1/2(e.g., saturation
to q= 0or nonperturbative breakdown of local heat-kernel scaling) is an important open question
for matter-coupled extensions of [1].
A Cryptographic Certificate Ledger
Table 3: SHA-256 certificate ledger for protocolNULL-CONE-QG-SHARP-1.0 (MANIFEST.json SHA-
256:a5a73d2478822f9ffab17f64562d2f48e2a20d07eda725628e070b098eacbaba).
ID SHA-256 Prefix (16 hex) Scope Certified in Zero-Float ExactQ
C01 27d922a3ae3e2363Exact BernoulliB 2 ...B 20 and Clausen coefficientsc1 ...c 10
C02 8fd09f7a174648cdCertified rational brackets forπ,ln 2,e,γ E,
√
5,Neff(s)/s
C03 fef34582b2f0a6faReal-part higher-loop collapse (s≥1/π) and Planckian cuspsm= 1...5
C04 e905754acc527f0eNon-asymptotic Clausen–Bernoulli brackets forℑA(s), Fourier check & UV match
C05 3149b940ff3963c8All-momentsBeta(α,1)law and Footnote 23p= 2recovery
C06 134fe8b15120a758Golden-Ratio clock-variance ceilingVar ∞(U)≤φ −5 (21test points)
C07 a44112f829f0b2f1Discrete Stieltjes all-moments identity and finite-ℓentropy envelope
C08 dac00467b697026ePure-gravity audit and 4D Matter-Content Sign-Barrier catalog
C09 4c01072ab9651caeOptimal Appendix D.3 focusing prefactor (C 1/4) vs. Eq. (D.46b) (O(C))
C10 7b6a99932567522cStrictly sharpened symplectic-area bound (R∈[1,10 8])
C11 9bc0e631402d48b8Two-sided shear correlator exponential UV-cutoff error bounds (Eq. 5.76)
C12 720d21c53ee64920Raychaudhuri area-fluctuation UV bound and exactu L =uR series check
C13 35d0a31ca92e4b2aFootnote 24 horizon-area band probabilities in(s ∗/4,s∗/2]
C14 d87e2e796251a559Generalized(a,b)-moment kernel andBeta(α,1)moment-ratio invariants
C15 3dafad00cc5073c9Crossover scales ofℜA(s): first cusp, global minimum, exact zeros
C16 93d5b3f2255110afSelf-referential AST zero-float and exact-arithmetic security audit
9

--- Page 10 ---
References
[1] V. Chandrasekaran,An algebraic quantization of gravity from the null cone, arXiv:2611.34924v1
[hep-th], November 25, 2026.
[2] A. Sen,Logarithmic corrections to Schwarzschild and other non-extremal black hole entropy in
different dimensions, JHEP04(2013) 156 [arXiv:1205.0971].
[3] L. Lewin,Polylogarithms and Associated Functions, North-Holland, New York (1981).
[4] N. H. Bingham, C. M. Goldie, and J. L. Teugels,Regular Variation, Encyclopedia of Mathe-
matics and its Applications, Vol. 27, Cambridge University Press (1987).
10
