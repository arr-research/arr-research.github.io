# Exact Sharp Thresholds, Piecewise-Algebraic Squaring Laws, and Machine-Checked Thermodynamic Mass-Gap Certificates for the Reflection-Positive Purity Bootstrap

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-5WBVP6JNVD8AESDD` (v1)  
**Intake Receipt:** `SUB-43DDF09DAA8F83BD`  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/sharp-purity-bootstrap (`v1.0.0`)  
**Canonical PDF SHA-256:** `0ba835e534d582c59f2f0595570a97e9851a1762960eb2e12c1164431896d670`

## Abstract

The reflection-positive purity bootstrap certifies a thermodynamic-limit spectral gap Delta_inf > 0 for interacting quantum lattice Hamiltonians from finite-size Euclidean partition-function purities, yet existing formulations rely on conservative defect cutoffs (u <= 0.01 in 1D and 1 - Q <= 1/(2a^2) in d spatial dimensions with a = 2^(d+1) - 1) and a flat gap ceiling Delta_inf > log(2)/beta_0. We derive the exact extremal laws and sharp stability boundaries of the purity bootstrap in arbitrary dimension d >= 1 and construct a machine-checked, zero-floating-point-trust certification pipeline. First, we solve the simplex squaring minimization problem inf{sum w_i^4 / (sum w_i^2)^2 : sum w_i = 1, sum w_i^2 = p} in closed piecewise-algebraic form on all of (0,1]; on (1/2,1] this coincides with h_1*(p) = 1 - (1-p)^2/(2p^2) via a three-line pure ring-algebra proof, accompanied by the uniquely attained spectral-gap ratio e^(beta Delta) >= (1 + sqrt(2p - 1))^2 / (2(1-p)). Second, using the exact staggered space-time plaquette identity in a cyclic Gauss-Seidel recurrence, we derive the exact algebraic uniform threshold 2 p^(2a) = (1-p)(sum_{j=0}^{a-1} p^j)^2, widening the 1D uniform basin by 12.73x (u_c*(1) = 0.127311) and enlarging the single-Q threshold by 3.26x to 7.63x for d = 1..5 (asymptotically 8x, scaling as 4/(a(a+1))). Third, we prove an exact doubly-exponential contraction bound yielding Delta_inf >= (1/(2^N beta_0)) log(1/(K_d(u_N) u_N)) for all intervening even hypercube lengths l >= L_0, breaking the log(2)/beta_0 ceiling. All 16 core algebraic theorems and lemmas are formalized in zero-dependency Lean 4 (v4.35.0, zero sorry, zero Classical.choice), paired with a zero-float-trust exact-Q verifier (including rational logarithm mass-gap bounds) benchmarked on the 1D TFIM (2.24x-4.72x closer to h_c=1, up to 9.03x tighter gaps), ferromagnetic g=2 Kramers-Wannier sector duality, 2D (D=3) lattices, and synthetic noisy intervals. On interacting spin chains, we prove an su(3) determinant obstruction showing that the Spin-1 AKLT chain violates bond-reflection positivity for every U in U(3), and certify exact-Q thermodynamic gaps on two provably bond-RP non-integrable chains—Spin-1 Heisenberg with single-ion anisotropy (L_0=4->8) and Spin-1/2 dimerized Heisenberg (L_0=6->12)—where Grover's u <= 0.01 fails at every tested parameter.

## Full Extracted Text

--- Page 1 ---
Exact Sharp Thresholds, Piecewise-Algebraic
Squaring Laws, and Machine-Checked
Thermodynamic Mass-Gap Certificates for the
Reflection-Positive Purity Bootstrap
Lluis Eriksson∗
November 24, 2026
Abstract
The reflection-positive purity bootstrap introduced for the Haldane-gap proof [14, 17]
and extended to higher dimensions, quasi-degenerate ground states, fermions, and tensor
networks by Grover [7] certifies a thermodynamic-limit spectral gap∆∞> 0from finite-
size Euclidean partition-function puritiesS and T. Existing analyses rely on conservative
defect cutoffs (u≤ 0.01in d = 1and1 −Q≤ 1/(2a2)in d spatial dimensions with
a = 2 d+1 −1) and yield a flat gap ceiling∆ ∞ > (log 2)/β0 insensitive to the actual
purity margin. Here we derive theexactextremal laws and sharp stability boundaries
of the purity bootstrap in arbitrary dimensiond≥ 1and build a machine-checked, zero-
floating-point-trust certification pipeline. First, we solve the simplex squaring minimization
problem inf{∑ w4
i/(∑ w2
i)2 : wi ≥0, ∑ wi = 1, ∑ w2
i = p}in closed piecewise-algebraic
form on all of(0 ,1]; on(1 /2,1]it collapses to h∗
1(p) = 1 −(1 −p)2/(2p2)via a three-
line pure ring-algebra proof, accompanied by the uniquely attained spectral-gap enclosure
eβ∆ ≥(1+ √2p−1 )2/(2(1−p)). Second, exploiting the exact staggered space-time plaquette
identity in a cyclic Gauss–Seidel recurrence, we derive the algebraic uniform threshold
pc(d) = 1 −u∗
c(d)solving2 p2a = (1 −p)(∑a−1
j=0 pj)2, widening the 1D uniform basin by
12.73×(u∗
c(1) = 0.127311) and enlarging the single-ratioQ threshold by3 .26×to7 .63×
across d= 1,..., 5(asymptotically8 ×, scaling as4/(a(a+ 1))vs.1 /(2a2)). Third, we prove
an exact doubly-exponential contraction bound yielding∆∞≥ 1
2Nβ0
log(1/(Kd(uN)uN))for
allintervening even hypercube lengths ℓ≥L 0, breaking the(log 2)/β0 ceiling by arbitrarily
large factors. We formalize all 16 core algebraic theorems and lemmas in zero-dependency
Lean 4 (v4.35.0, zerosorry, zeroClassical.choice), verify rational logarithm mass-gap
bounds strictly overQ, and benchmark across the 1D transverse-field Ising model (2.24×–
4.72×closer tohc = 1, up to9.03×tighter gaps), theg= 2ferromagnetic phase via exact
Kramers–Wannier sector duality, 2D (D= 3) lattices, and synthetic noisy intervals (0 false
certifications across 200 critical and 200 near-boundary trials). On interacting spin chains,
we prove ansu(3)determinant obstruction showing that the Spin-1 AKLT chain violates
bond-reflection positivity for everyU∈U (3), and certify exact-Q thermodynamic gaps on two
provably bond-reflection-positive non-integrable chains—Spin-1 Heisenberg with single-ion
anisotropy (L0 = 4 →8) and Spin-1/2 dimerized Heisenberg (L0 = 6 →12)—where Grover’s
u≤0.01fails at every tested parameter.
1 Introduction
Establishing a uniform spectral gap∆∞= lim infL→∞(E1(L)−E0(L)) >0in the thermodynamic
limit of interacting quantum many-body lattice Hamiltonians is a central open problem in
∗Independent researcher (Sweden). Research, zero-dependency Lean 4 proofs, exact rational (Q) certificate
verifiers, and numerical benchmarks prepared with AI assistance (Google Antigravity) and publicly archived at
https://github.com/lluiseriksson/sharp-purity-bootstrap.
1

--- Page 2 ---
mathematical physics [8, 9, 1, 2]. Classical finite-size criteria such as Knabe’s bound [11] and its
modern refinements [6, 13, 3] require the Hamiltonian to be frustration-free, excluding generic
frustrated or non-commuting models such as the spin-1Heisenberg antiferromagnet.
Arecentbreakthrough—thereflection-positive purity bootstrap[14,17]—circumventsfrustration-
freeness by exploiting Osterwalder–Schrader reflection positivity [15, 5] of the Euclidean partition
function Z(L1,...,L d; β) = Tr(e−βHL1,...,Ld ). Writing normalized partition-function ratios (“pu-
rities”) in spatial and temporal directions,
S(L,β) := Z(2L,β)
Z(L,β) 2 , T(L,β) := Z(L,2β)
Z(L,β) 2 ,(1)
reflectionpositivityensuresthatboth S(L,β) = ∑
iw2
i/(∑
iwi)2 (forthespatialtransferoperator)
and T(L,β)(for the Gibbs transfer operator e−βHL) are purities of nonnegative probability
distributions w= (wi)on the unit simplex, hence lie in(0,1]. Doubling along an axis squares the
underlying spectrum (wi ↦→w2
i), driving the purity closer to1, while passing across orthogonal
axes incurs a plaquette penalty. Grover [7] systematically generalized this bootstrap to arbitrary
spatial dimensiond≥ 1( D= d+ 1space-time axes), quasi-degenerate ground states (g≥ 2),
fermionic parity sectors, and tensor-network states.
Despite its elegance, the current purity bootstrap suffers from four structural bottlenecks
that severely limit practical certification on finite lattices:
1. Loose squaring and gap-from-purity inequalities.Prior bounds use suboptimal lower
envelopes for∑ w4
i/(∑ w2
i)2 and for the gap ratiow0/w1, losing a factor of up to2in the
purity defect at every doubling step.
2. Conservative multi-axis thresholds.Grover [7] requiresu≤ 0.01in d= 1and1 −Q≤
1/(2a2)in d spatial dimensions (where a = 2 d+1 −1), discarding over90%of the true
certifiable region in 1D and a factor of up to8×in higher dimensions due to simultaneous
(Jacobi) rather than sequential (Gauss–Seidel) multi-axis updates.
3. Flat thermodynamic gap ceiling.Because existing proofs terminate onceT(L,β)crosses
a fixed constant, they produce the flat bound∆∞>(log 2)/β0, which actuallydegradesas
1/β0 when one lowers temperature to enter the bootstrap basin—even when the initial purity
defect is10 −6!
4. Unverified floating-point and finite-sample certification.Numerical partition func-
tions from exact diagonalization, tensor networks, or Monte Carlo carry floating-point
rounding or statistical error; without monotone interval propagation and exact rational
verification, a near-boundary rounding error could falsely certify a gapless critical point.
Summary of Contributions.We resolve all four bottlenecks with exact extremal mathemat-
ics, zero-dependency Lean 4 machine verification, and exact-Qnumerical certificates:
• Exact Piecewise-Algebraic Squaring Law & Gap Enclosures (Section 2):Theo-
rem 2.1 characterizes the global infimumh∗(p) = inf{∑ w4
i/(∑ w2
i)2 : ∑ wi = 1, ∑ w2
i = p}
across all p∈ (0,1]; on(1 /2,1], it coincides with the rational envelopeh∗
1(p) = 1 −(1 −
p)2/(2p2), which admits a purely algebraic three-line proof (Theorem 2.2). Theorem 2.3
establishes the uniquely sharp spectral-gap ratiow0/w1 ≥(1 + √2p−1) 2/(2(1−p)).
• Exact D-Dimensional Cyclic Gauss–Seidel Thresholds (Section 3):Leveraging the
exact staggered space-time plaquette identity in a cyclic Gauss–Seidel iteration (Theorem 3.1),
we prove that the uniform stability boundarypc(d) = 1 −u∗
c(d)is the unique root in(1/2,1)
of2 p2a = (1 −p)(∑a−1
j=0 pj)2, yieldingu∗
c(1) = 0.127311(12 .73×vs.0 .01). For the single-
ratio hypercube invariantQ, eliminating redundant leading-axis factors yields Theorem 3.2,
improving1 −Q∗
c(d)by3 .26×to7 .63×for d= 1,..., 5and asymptotically8 ×(4/(a(a+ 1))
vs.1/(2a 2)).
2

--- Page 3 ---
• Unbounded Asymptotic Gap Bounds & Intervening Lengths (Section 4):Theo-
rem 4.1 proves explicit doubly-exponential decayKduN+m ≤(KduN)2m
, certifying∆ ∞≥
1
2N β0
log(1/(Kd(uN)uN))—scaling asΩ( log(1/u0)/β0)and breaking the( log 2)/β0 ceiling.
Theorem 4.2 and Proposition 4.3 transfer this exact lower bound from dyadic lengths2nL0 to
everyintervening even hypercube lengthℓ≥L 0, and Corollary 4.4 handles the ferromagnetic
1D TFIM via exact Kramers–Wannier sector duality.
• Machine-Checked Lean 4 Formalization, Exact-Q Verifier & Bond-RP Bench-
marks (Sections 5–6):All 16 core algebraic theorems and lemmas listed in Table 1 are for-
malized in zero-dependency Lean 4 (v4.35.0, 0sorry, 0Classical.choice). Theorem 5.1
guarantees fail-closed finite-sample interval propagation and sound downward-quantized
Q-certification including exact rational logarithm bounds. We benchmark the pipeline on the
1D TFIM, prove ansu(3)determinant no-go obstruction for bond-RP of the Spin-1 AKLT
chain, and certify exact-Q gaps on two genuinely bond-RP non-integrable spin chains (Spin-1
Heisenberg+D and Spin-1/2 dimerized Heisenberg), plus 2D (D= 3) lattices and synthetic
noisy intervals.
2 Exact Piecewise-Algebraic Squaring Law and Gap Enclosures
Let∆ +
∞:= {w = (wi)i≥0 : wi ≥0, ∑
iwi = 1}denote the countable probability simplex (for
finite transfer matrices, all but finitely manywi vanish), with purityp(w) := ∑
iw2
i ∈(0,1]and
fourth momentq(w) := ∑
iw4
i. Under one axis doubling, the normalized weights transform as
wi ↦→w2
i/p(w), so the doubled purity isp′(w) =q(w)/p(w) 2.
Theorem 2.1(Exact Piecewise-Algebraic Squaring Law on(0,1] ).For every p∈ (0,1], let
k=⌊1/p⌋∈N ≥1 so thatp∈
(1
k+1 ,1
k
]
, and define
ak(p) := k+
√
k((k+ 1)p−1)
k(k+ 1) , b k(p) := 1−
√
k((k+ 1)p−1)
k+ 1 .(2)
Then over all probability distributionsw∈∆ +
∞ satisfying ∑
iw2
i =p,
inf
w∈∆+
∞∑
w2
i =p
∑
iw4
i
p2 =h ∗(p) := kak(p)4 +bk(p)4
p2 ,(3)
and the infimum is uniquely attained (up to permutation and zero padding) by the(k+ 1)-point
spectrumw∗= (ak(p),...,a k(p)  
ktimes
,bk(p),0,0,...).
Proof. Fix p∈ (0,1]and consider minimizing f(w) = ∑m
i=1 w4
i over the compact setKm(p) =
{w∈R m
≥0 : ∑
iwi = 1, ∑
iw2
i = p}for arbitrarym≥k + 1. First, if all positive coordinates of
a minimizerw are equal (wi = 1/r on its support of sizer), thenp= 1/r is an exact reciprocal
integer (r = k) and Cauchy–Schwarz gives∑ w4
i ≥(∑ w2
i)2/r = p3 = k(1/k)4, matching(3)
with bk(1/k) = 0. Otherwise, w has at least two distinct positive coordinates, so the gradients
(1,..., 1)and(2 w1,..., 2wm)are linearly independent on the positive support (LICQ holds).
By Karush–Kuhn–Tucker stationarity,w admits multipliersλ,µ∈R such that every positive
coordinatew i >0satisfies the depressed cubic
g(wi) := 4w3
i −2µwi −λ= 0.(4)
Since a depressed cubic has at most two positive roots, every positive coordinate ofw takes
at most two distinct valuesa > b >0. By Rolle’s theorem ong(x) = 4x3 −2µx−λ (whose
derivativeg′(x) = 12x2 −2µhas a single positive zero), we haveg′(a) = 12a2 −2µ> 0and g′(b) =
3

--- Page 4 ---
12b2 −2µ< 0. If w contained s≥ 2copies of b, then the perturbation vectorδ with(+1 ,−1)on
twob-coordinates and0elsewhere lies in the tangent subspace{δ: ∑ δi = 0, ∑ wiδi = 0}of both
equality constraints; by LICQ, the second-order necessary condition requires the Lagrangian
Hessian form∑
i(12w2
i −2µ)δ2
i = 2(12b2 −2µ) ≥0, contradictingg′(b) <0. Hence s≤ 1, so any
minimizer has support(a,...,a 
r
,b)witha≥b≥0.
Eliminating b= 1 −ra from ra2 + b2 = p gives r(r+ 1)a2 −2ra+ (1 −p) = 0. Positivity of
b= 1−ra≥ 0forces1 /p≥r (withr= 1/pwhenb= 0), whilerealrootsrequire r((r+1)p−1) ≥0,
i.e., r≥⌈ 1/p⌉− 1. For non-integer1 /p this uniquely selectsr = k = ⌊1/p⌋, and for integer
1/p= k the boundary valueb= 0agrees continuously with r= k−1at a= b= 1/k. Taking
the larger roota≥b yields (2). Since this lower bound is independent ofm, passing tom→∞
proves (3) over all of∆+
∞; moreover, uniqueness on∆+
∞follows because any minimizerw∈ ∆+
∞
with three distinct positive coordinates (or two copies of a non-maximal positive value) would
violate the finite-support KKT conditions when fixing all remaining coordinates.
When p∈ (1/2,1]( k= 1), the square roots in(2) cancel identically, yielding a rational lower-
bound envelopeh∗
1(p)that coincides with h∗(p)on(1 /2,1]and admits a three-line elementary
proof requiring no calculus (formalized over arbitrary ordered fields in Lean 4; see Table 1).
Theorem 2.2(Three-Line Algebraic Squaring Law on(1/2,1] ).For every finite or countable
distributionw∈∆ +
∞ with purityp= ∑
iw2
i >0,
∑
i
w4
i ≥p 2 −(1−p) 2
2 ,equivalently
∑
iw4
i
p2 ≥h ∗
1(p) := 1− (1−p) 2
2p2 .(5)
Moreover: (i)h∗
1(p) = h∗(p)for all p∈ (1/2,1]and equality holds identically on every two-level
spectrum( a,1 −a); (ii) h∗
1(p)is strictly increasing on(0 ,1]; and (iii) writingu = 1 −p, the
defect contracts quadratically as1−h∗
1(1−u) = u2
2(1−u)2 .
Proof. Let P1 := ∑
i<j wiwj and P2 := ∑
i<j(wiwj)2. Expanding( ∑
iwi)2 = 1and( ∑
iw2
i)2 = p2
yields the two exact identities
1−p= 2P 1, p 2 −
∑
i
w4
i = 2P2.
Since every termwiwj ≥0, we haveP2 = ∑
i<j(wiwj)2 ≤
(∑
i<j wiwj
)2 = P2
1 = (1 −p)2/4, with
equality whenever at most one pair(i,j)is nonzero (i.e., any two-level spectrum). Multiplying
by2gives p2 −∑
iw4
i ≤(1 −p)2/2, which rearranges immediately to(5). Monotonicity ofh∗
1(p)
on(0,1]follows since(1−p)/p=p −1 −1is strictly decreasing and nonnegative.
Notice thath∗
1(p)provides a valid lower bound forall p∈ (0,1](though it is sharp only
on(1 /2,1], where it agrees withh∗(p), and becomes nonpositive belowp=
√
2−1 ≈0.414).
Compared to naive bounds of the form1−u′≥1 −u2/(1 −u)2 or linear defect relaxations, the
exact factor of1
2 in1 −h∗
1(1 −u) = u2
2(1−u)2 doubles the permissible defect at every single step.
For brevity, we writeh∗(p) = h∗
1(p)throughout Sections 3–5, where all intermediate purities lie
strictly in(1/2,1].
We next derive the exact sharp extraction of the spectral gap∆ =E1 −E0 from a Gibbs
purityp=T(L,β) = ∑
iw2
i wherew i =e−βEi/Z(L,β)are sortedw 0 ≥w1 ≥···≥0.
Theorem 2.3(Sharp Gap-from-Purity and Tail-Mass Enclosures).Let w∈ ∆+
∞ with w0 ≥
w1 ≥···≥0and purityp= ∑
i≥0 w2
i. Then:
(a)w 0 ≥p and1 −p≥ 2w0(1 −w0), hence(2 w0 −1)2 ≥2p−1. In particular, forp∈ (1/2,1],
w0 ≥ 1 + √2p−1
2 ,
∑
i≥1
wi = 1−w 0 ≤ 1−√2p−1
2 .(6)
4

--- Page 5 ---
(b) Ifp∈(1/2,1)andw 1 >0, then
eβ∆ = w0
w1
≥ 2w2
0
1−p ≥ (1 + √2p−1) 2
2(1−p) .(7)
Every inequality in(6)–(7) is attained with exact equality on two-level spectra(w0,1 −w0).
Proof. Since wi ≤w 0 for all i≥ 1, p = w2
0 + ∑
i≥1 w2
i ≤w 0(w0 + ∑
i≥1 wi) = w0. Next,∑
i≥1 w2
i ≤(∑
i≥1 wi)2 = (1 −w0)2, sop≤w 2
0 + (1 −w0)2 = 1 −2w0(1 −w0), giving1 −p≥
2w0(1−w0). Multiplying by2and subtracting from1yields(2 w0 −1)2 = 1−4w0(1−w0) ≥2p−1.
Since w0 ≥p > 1/2, taking the positive square root gives(6). Finally, w1 ≤1 −w0 implies
2w0w1 ≤2w0(1 −w0) ≤1 −p, so dividing byw1(1 −p)/w0 >0gives w0/w1 ≥2w2
0/(1 −p), and
substituting (6) gives (7).
As p→ 1−, (7) gives w0/w1 ≥ 2
1−p(1 −O(1 −p)), which is asymptotically2×tighter in the
ratio (an additive+(log 2)/β improvement in∆) than the elementary boundw0/w1 ≥p/(1 −p)
and exact on two-level spectra. All four algebraic core lemmas of Theorem 2.3 are Lean-verified
(Table 1).
3 Cyclic Gauss–Seidel Recurrence and SharpD-Dimensional
Thresholds
3.1 Exact Space-Time Plaquette Identity and 1D Cyclic Gauss–Seidel Boot-
strap
Consider a reflection-positive 1D quantum lattice Hamiltonian with Euclidean partition functions
Z(L,β) >0for even lengths L and β >0, with spatial purityS(L,β) = Z(2L,β)/Z(L,β)2 ∈
(0,1]and temporal purityT(L,β) =Z(L,2β)/Z(L,β) 2 ∈(0,1]. On any elementary space-time
plaquette( L,β) →(2L,2β), direct algebraic cancellation (Lean:plaquette_exact_identity)
gives the exact identity
S(L,2β)T(L,β) 2 = Z(2L,2β)
Z(L,β) 4 =T(2L,β)S(L,β) 2.(8)
Because T(L,β) ≤1by reflection positivity,(8) immediately yields the sharp plaquette transfer
inequality (Lean:plaquette_lower_bound)
S(L,2β)≥S(L,β) 2 T(2L,β).(9)
Crucially, note that S(L,2β)doesnotsatisfy S(L,2β) ≥S (L,β)2 in general (we verified
counterexamples withS(L,2β)/S(L,β)2 ≈0.981 <1on reflection-positive two-mode transfer
matrices); the factorT(2L,β)in (9) is sharp and indispensable.
Now define the diagonalized scale-doubled sequence
Sn :=S(2 nL0,2 nβ0), T n :=T(2 n+1L0,2 nβ0), n≥0.
Applying (9) to(2 nL0,2nβ0)yields S(2nL0,2n+1β0) ≥S 2
nTn. Doubling the spatial axis from
2nL0 to2 n+1L0 at fixed2n+1β0 squares the spatial transfer-matrix spectrum, so by Theorem 2.2
and monotonicity ofh∗:
Sn+1 =S(2 n+1L0,2 n+1β0)≥h ∗(
S(2nL0,2 n+1β0)
)
≥h ∗(S2
nTn).(10)
Next, applying the transposed plaquette identity to(2n+1L0,2nβ0)uses thealready-updated
spatial puritySn+1:
T(2n+2L0,2 nβ0) = T2
n Sn+1
S(2n+1L0,2 nβ0)2 ≥T 2
nSn+1.
5

--- Page 6 ---
Doubling the temporal axis from2nβ0 to2 n+1β0 at fixed length2 n+2L0 squares the Gibbs
spectrum, yielding the exactcyclic Gauss–Seidelupdate:
Tn+1 =T(2 n+2L0,2 n+1β0)≥h ∗(T2
nSn+1).(11)
Theorem 3.1(1D Cyclic Gauss–Seidel Bootstrap and Exact Uniform Threshold).Define
Φ(1)
GS(s,t) =
(
h∗(s2t), h∗(t2h∗(s2t))
)
.
(a) Inductive Soundness & Monotonicity (Table 1).If0<s0 ≤S0 and0 <t0 ≤T0, and
every iterate( sk,tk) = (Φ(1)
GS)k(s0,t0)for k≤N remains strictly positive with intermediate
products in(0,1], thens k ≤Sk andt k ≤Tk for allk≤N.
(b) Exact Uniform Stability Threshold.Along the symmetric diagonals0 = t0 = p, the
map converges to(1,1)if and only if p>p c(1) := 1 −u∗
c(1), wherepc(1)is the unique root
in(1/2,1)ofh ∗(p3) =p, equivalently the polynomial equation
2p6 = (1−p)
(
1 +p+p 2)2,(12)
giving pc(1) = 0.8726892136 ... and u∗
c(1) = 0.1273107864 ... —a 12.73×wider uniform
threshold than Grover’su≤0.01[7].
(c) Anisotropic Basin.Even when s0 < pc(1),( s0,t0)lies in the exact certifiable gapped
basinB(1)
gap whenevert 0 >tcrit(s0)(e.g.,s 0 = 0.80,t0 >0.9675, ors 0 = 0.785,t0 >0.9950).
Proof. Part (a) follows by induction from(10)–(11) and monotonicity ofh∗on(0 ,1]. For (b), at
a fixed point(p,p)ofΦ (1)
GS, both coordinates satisfyp= h∗(p3) = 1−(1−p3)2/(2p6). Rearranging
1 −p = (1 −p)2(1 +p+ p2)2/(2p6)and cancelling1 −p> 0gives (12). On(1 /2,1), the left-hand
side2 p6 is strictly increasing from1/32to2, while(1 −p)(1 +p+ p2)2 = (1 −p3)(1 +p+ p2)has
derivative−(3p2)(1+p+p2)+(1−p3)(1+2p) <0for allp∈ (0.65,1)(and2 p6 <(1−p)(1+p+p2)2
on(1 /2,0.65]), ensuring a unique rootpc(1) ≈0.8726892136. SinceΦ (1)
GS is componentwise strictly
increasing,p>p c(1)impliesh ∗(p3)>p, forcing(s n,tn)↑(1,1)monotonically.
3.2 General D-Dimensional Cyclic Bootstrap and8×Single-Q Improvement
In d spatial dimensions (D= d+ 1space-time axes with initial extents⃗L0 = (L0,0,...,L 0,D−1)
where L0,D−1 = β0), let pk(⃗L) := Z(⃗L+ Lkek)/Z(⃗L)2 ∈(0,1]denote the axis- k purity at
geometry ⃗L. Crucially, to obtain exact telescoping across allD orthogonal axes, we track the
staggered staircasestate vector at doubling scalen≥0:
p(n)
k :=p k
(
2n+1L0,0, ...,2 n+1L0,k−1,2 nL0,k, ...,2 nL0,D−1
)
, k= 0,...,D−1.(13)
Direct substitution yields the exactD-dimensional telescoping hypercube identity
Q(n) :=
D−1∏
j=0
(
p(n)
j
)2D−1−j
= Z(2n+1⃗L0)
Z(2n⃗L0)2D .(14)
Fork= 0, comparingZ(2n+1⃗L0)alongthedoubledaxis0against Z(2n+1L0,0,2nL0,1,..., 2nL0,D−1)
via the exactD-dimensional plaquette identity gives
p0
(
2nL0,0,2 n+1L0,1, ...,2 n+1L0,D−1
)
≥ Z(2n+1⃗L0)
Z(2n⃗L0)2D =
D−1∏
j=0
(
p(n)
j
)2D−1−j
,
since all denominator purities on the intervening hypercube faces lie in(0 ,1]. Doubling
axis0from2 nL0,0 to2 n+1L0,0 then squares the axis-0transfer-matrix spectrum, yielding
6

--- Page 7 ---
p(n+1)
0 ≥h∗(∏D−1
j=0 (p(n)
j )2D−1−j )
. Advancing cyclically along axesk= 0,1,...,D− 1shifts the
staircase window by one axis at each step, yielding the exact cyclic Gauss–Seidel recurrence on
(p0,...,p D−1):
pnew
k =h ∗
(D−1∏
j=0
˜p2D−1−j
k,j
)
,˜p k =
(
pk,...,p D−1, pnew
0 ,...,p new
k−1
)
,(15)
where the exponents sum toa:= ∑D−1
j=0 2j = 2D −1 = 2 d+1 −1.
Theorem 3.2(Sharp D-Dimensional Uniform and Single-Q Thresholds).Let D= d+ 1 ≥2
anda= 2 D −1.
(a) Exact Uniform Threshold.A uniform initial staircasep0 = ··· = pD−1 = p converges
to(1 ,..., 1)under the cyclic Gauss–Seidel map(15) if and only ifp>p c(d) = 1 −u∗
c(d),
wherepc(d)is the unique root in(1/2,1)of
2p2a = (1−p)


a−1∑
j=0
pj


2
,sou ∗
c(d) = 2
a2 +O
(1
a3
)
.(16)
(b) Exact Single-Q Contraction and8×Asymptotic Gain (Table 1).For the telescoping
hypercube invariantQ= ∏D−1
j=0 p2D−1−j
j ∈(0,1], at stepk∈{ 0,...,D− 1}of (15) the old
trailing product satisfies∏D−1
j=k p2D−1−j
j ≥Q, whence raising to2k yields
pnew
k ≥h ∗
(
Q2k
k−1∏
r=0
(pnew
r )2k−1−r
)
.(17)
Consequently, Qnew ≥ΨD(Q) := ∏D−1
k=0 (qk(Q))2D−1−k
, whereqk(Q)is defined recursively by
the right-hand side of(17). The exact single-Q stability threshold1 −Q∗
c(d)(unique root of
ΨD(Q) =Qon the valid domain where allqk >1/2) satisfies
1−Q ∗
c(d) = 4
a(a+ 1) +O
(1
a3
)
∼8· 1
2a2 (d→∞),(18)
delivering an asymptotic8×enlargement over Grover’s threshold1−Q≤ 1/(2a2)[ 7] (3.26×
atd= 1,5.28×atd= 2,6.56×atd= 3,7.26×atd= 4,7.63×atd= 5).
Proof. For part (a), settingpnew
k = p in (15) gives p = h∗(pa) ⇐⇒ (p−a −1)2 = 2(1 −p),
which rearranges to (16). Uniqueness of the root pc(d) ∈(1/2,1)for every a≥ 3follows
immediately by convexity:L(p) := (p−a−1)2 is strictly convex on(0,1]with L(1) = 0,L′(1) = 0,
whereas R(p) := 2(1 −p)is linear with R(1) = 0,R′(1) = −2 <0, andL(1/2) = (2a −1)2 ≥
49 > 1 = R(1/2), so L−R has a unique zero in(1 /2,1). Substituting p = 1 −u yields
2(1−2au+O(u 2)) =a2u(1−(a−1)u+O(u 2)), sou∗
c(d) = 2/a2 +O(a−3).
For part (b), writeQ= HkRk where Hk = ∏k−1
j=0 p2D−1−j
j ∈(0,1]and Rk = ∏D−1
j=k p2D−1−j
j .
Since Hk ≤1, we haveQ≤R k, hence Q2k
≤R 2k
k = ∏D−1
j=k p2D−1−(j−k)
j (verified in Lean 4 as
hypercube_Q_step_sound). Multiplying by the already-updated prefix∏k−1
r=0 (pnew
r )2k−1−r
and
invoking monotonicity ofh∗yields (17). To extract the exact leading asymptotics ofΨD(1 −ϵ),
set Q = 1 −ϵ with ϵ = O(a−2). Since Q2k
= 1 −2kϵ+ O(22kϵ2), induction on k shows
1 −qk = 1
2 (2kϵ)2 + O(23kϵ3) = 22k−1ϵ2 + O(ϵ3)(the updated prefix defects areO(ϵ2), subleading
to2 kϵ). Therefore,
1−Ψ D(1−ϵ) =
D−1∑
k=0
2D−1−k(1−q k) +O(a3ϵ3) = ϵ2
2
D−1∑
k=0
2D−1+k +O(a3ϵ3)
= 2D−1(2D −1)
2 ϵ2 +O(a3ϵ3) = a(a+ 1)
4 ϵ2 +O(a3ϵ3).
7

--- Page 8 ---
Equating1 −ΨD(1−ϵ) = ϵyields ϵ∗
c = 4/(a(a+1))+ O(a−3), which is asymptotically8×(1/(2a2)).
Physically, two independent factors of2and4combine: our sharp h∗ saves a factor of2per
squaring, and replacing Grover’s simultaneous boundQa by the exact trailing-product power
Q2k
replaces ∑
k2D−1−ka2 = a3 by ∑
k2D−1−k22k = a(a+ 1)/2, saving an additional factor of
4.
4 Doubly-Exponential Decay, Unbounded Gap Bounds, and
Intervening Lengths
4.1 Breaking the(log 2)/β 0 Ceiling
Once a finite numberN of exact Gauss–Seidel steps brings the maximum axis defectuN :=
max0≤j<D(1 −p(N)
j )into the quadratic contraction zone, we obtain an explicit, unbounded
thermodynamic mass-gap lower bound.
Theorem 4.1(Explicit Doubly-Exponential Contraction and Unbounded Mass Gap).Let
p(N) = (p(N)
0 ,...,p (N)
D−1)be valid lower bounds on the space-time purities at doubling scaleN
(lengths2 NL0, inverse temperature2Nβ0), with defectuN = maxj(1 −p(N)
j ) ∈(0,1/2)and
pmin = 1−u N. Define the explicit rational contraction constant
Kd(uN) := a2
2p2a
min
(a= 2 d+1 −1), ρ N :=K d(uN)uN.(19)
If ρN < 1, then for everym≥ 0the defects satisfy uN+m+1 ≤K d(uN) u2
N+m, and therefore
(Lean:doubly_exponential_contraction):
uN+m ≤ 1
Kd(uN) ρ2m
N ∀m≥0.(20)
Consequently, along the dyadic sequenceLn = 2nL0, the thermodynamic mass gap satisfies
∆dyad := lim infn→∞ ∆(2nL0)≥ 1
2Nβ0
log
( 1
ρN
)
= 1
2Nβ0
log
( 1
Kd(uN)uN
)
.(21)
Proof. Suppose un ≤uN (sop(n)
j ≥1−un ≥pmin for allj). By inner induction over the cyclic axis
updates k= 0,...,D− 1: assuming the already-updated prefix satisfiesp(n+1)
r ≥1−un ≥pmin for
r<k , Bernoulli’s inequality ensures thea-fold productΠ k = ∏
j ˜p2D−1−j
k,j satisfies pa
min ≤Πk ≤1
and1−Π k ≤aun. Applying Theorem 2.2 yields
1−p (n+1)
k ≤ (1−Π k)2
2Π2
k
≤ a2u2
n
2p2a
min
=K d(uN)u2
n ≤ρ Nun < un ≤u N,
closing the inner induction onk and provingun+1 ≤Kd(uN)u2
n ≤uN. Outer induction onm
(Lean: doubly_exponential_contraction) then givesKduN+m ≤(KduN)2m
= ρ2m
N . At scale
n= N + m, the temporal purity at lengthLn+1 = 2n+1L0 and inverse temperatureβn = 2nβ0
satisfies1−T(L n+1,βn)≤u N+m. Applying Theorem 2.3(b) yields
∆(Ln+1)≥ 1
βn
log
(
2(1−u N+m)2
uN+m
)
≥ 1
2N+mβ0
log
(
2Kd(uN)(1−u N+m)2
ρ2m
N
)
.
Takinglim inf m→∞cancels theO(2 −m)prefactor logarithm and leaves (21) identically.
Unlike Grover’s flat bound∆ ∞ > (log 2)/β0, equation (21) grows without bound as
Ω(log(1/u0)/β0)when the initial defectu0 →0. In particular, when a model is deeply gapped
(u0 ∼e−β0∆), 1
β0
log(1/u0) = Θ(∆)recovers a constantO(1)fraction of the true physical mass
gap independent ofβ0!
8

--- Page 9 ---
4.2 Transfer from Dyadic Scales to All Intervening Even Lengths andg= 2
Phases
A subtle mathematical requirement in any doubling bootstrap is ensuring that the gap does
not collapse on non-dyadic system sizesℓ /∈{2nL0}. The following theorem transfers the exact
rate (21) toeveryintervening even hypercube length ℓ≥L 0 with zero loss in the asymptotic
exponent.
Theorem 4.2(1D Intervening-Length Purity Transfer).Let d= 1. For any even lengthℓ∈
[L,2L]with L= 2nL0, letµβ and µ2β denote the largest eigenvalues (spectral radii) of the positive
spatial transfer matrices at inverse temperaturesβ and2 β, so thatZ(L′,β) = µL′
β (1 + R(L′,β))
with R(L′,β) ≥0. Since µ2β ≤µ 2
β (following immediately from Z(L′,2β) ≤Z (L′,β)2 as
L′→∞),ℓ≤2Limplies(µ 2β/µ2
β)2L ≤(µ2β/µ2
β)ℓ, and therefore
T(ℓ,β)≥ T(2L,β)
(
1 +R(ℓ,β)
)2(
1 +R(2L,2β)
).(22)
In particular, ifSn ≥1 −un and Tn ≥1 −un satisfy the doubly-exponential contraction(20),
then R(ℓ,βn) ≤ un
2(1−un)2 and R(2L,2βn) ≤ un+1
2(1−un+1)2 for every evenℓ∈ [2nL0,2n+1L0], so the
exact lower bound(21)holds foralleven lengths:
∆∞ := lim inf
ℓ→∞
ℓeven
∆(ℓ)≥ 1
2Nβ0
log
( 1
K1(uN)uN
)
.(23)
Proof. Using Z(ℓ,2β) ≥µℓ
2β, Z(ℓ,β) ≤(1 + R(ℓ,β))µℓ
β, Z(2L,2β) ≤(1 + R(2L,2β))µ2L
2β, and
Z(2L,β)≥µ 2L
β , we obtain
T(2L,β)
(1 +R(ℓ,β)) 2(1 +R(2L,2β)) ≤ 1
(1 +R(ℓ,β)) 2
(
µ2β
µ2
β
)2L
≤ 1
(1 +R(ℓ,β)) 2
(
µ2β
µ2
β
)ℓ
≤ Z(ℓ,2β)
Z(ℓ,β) 2 =T(ℓ,β).
Thisexactalgebraicchainismachine-checkedinLean4( intervening_length_purity_transfer).
Now fixn = N + m with L = 2nL0, βn = 2nβ0, and any evenℓ∈ [L,2L]. Writing the spa-
tial transfer-matrix eigenvalues at inverse temperatureβn as λ0 = µβn ≥λ 1 ≥···≥ 0, the
remainder R(ℓ,βn) = ∑
α≥1(λα/λ0)ℓ is monotonically nonincreasing inℓ. Since Sn = S(L,βn)
is the purity of the normalized weightsw(L)
α = λL
α/Z(L,βn), Theorem 2.3(a) gives1−w(L)
0 ≤
(1−S n)/(2w(L)
0 )≤u n/(2(1−u n))and hence
R(ℓ,βn)≤R(L,β n) = 1−w (L)
0
w(L)
0
≤ un
2(1−u n)2 .
Similarly, Sn+1 = S(2L,2βn) ≥1 −un+1 implies R(2L,2βn) ≤u n+1/(2(1 −un+1)2) = O(u2
n).
Substituting these bounds together withT(2L,βn) = Tn ≥1 −un into (22) yields1 −T(ℓ,βn) ≤
(2 + o(1))un ≤ 3un for all sufficiently large n uniformly in ℓ∈ [2nL0,2n+1L0]. Applying
Theorem 2.3(b) at inverse temperatureβn = 2N+mβ0 gives
∆(ℓ)≥ 1
2N+mβ0
log
(
2(1−3u N+m)2
3uN+m
)
≥ 1
2N+mβ0
log
(
2K1(uN)(1−3u N+m)2
3ρ2m
N
)
,
and takinglim infℓ→∞(m→∞ ) eliminates theO(2−m)prefactor logarithm, establishing (23)
identically.
9

--- Page 10 ---
Proposition 4.3(Extension to Intervening Even Hypercubes ind≥ 2).Let d≥ 2and suppose
the D-dimensional staircase purities satisfy(20) with ρN = Kd(uN)uN < 1. Then for every
sequence of even hypercubes(ℓ,...,ℓ )with ℓ∈ [2n+1L0,2n+2L0]( n = N + m), the temporal
purityT(ℓ,...,ℓ;β n)obeys1−T(ℓ,...,ℓ;β n)≤O(u n), and consequently
∆∞ := lim inf
ℓ→∞
ℓeven
∆(ℓ,...,ℓ)≥ 1
2Nβ0
log
( 1
Kd(uN)uN
)
.(24)
Proof. We transfer from the dyadic hypercube(2L,..., 2L)( L= 2n+1L0, β = βn = 2nβ0) to
(ℓ,...,ℓ )one spatial axis at a time (j = d−1,d− 2,..., 0), keeping a fixedβn. At stagej, the
other spatial axes are fixed at(2L,..., 2L,ℓ,...,ℓ ), and applying the 1D algebraic inequality(22)
along axisj bounds both the temporal purityT and every remaining spatial puritypi (i<j )
at the new mixed geometry in terms of the axis-j remainders Rj at lengthsL and2 L (note
that (22) holds identically when the role ofβ→ 2β is played by doubling any orthogonal
spatial axisi < j!). At the initial stage (j = d−1), the scale-(n+ 1)staircase purities give
pi(2n+1L0,... ; βn) ≥1 −O(un)via the exact plaquette step, and each axis reduction multiplies
the purity by1 −O(un)(since Rj(ℓ) ≤R j(L) ≤O (1 −pj)at the mixed geometry). After d
finite steps, alldspatial axes reachℓwith1 −T (ℓ,...,ℓ ; βn) ≤Cdun for ad-dependent constant
Cd. Taking 1
2N+m β0
log(2(1 −CduN+m)2/(CduN+m))and letting m→∞ cancels logCd/2m →0
and yields (24).
Corollary 4.4(Ferromagnetic 1D TFIM (g= 2Doublet) via Kramers–Wannier Sector Duality).
Consider the periodic ferromagnetic 1D transverse-field Ising chainH(h) = −∑L
i=1 ZiZi+1 −
h∑L
i=1 Xi with h∈ (0,1), whose ground state is asymptoticallyg = 2-fold degenerate. Naive
restriction to the odd-parity partition functionZodd(L,β)can fail spatial reflection positivity
(Sodd >1). However, exact Kramers–Wannier duality [12, 7] establishes exact isospectral sector
equivalences betweenH(h)and the dual paramagnetic chainHdual := hH(1/h)( hdual = 1/h> 1,
dual inverse temperatureβdual =hβ):
(Ferro, PBC, even)∼= (Dual, PBC, even),(Ferro, APBC, even) ∼= (Dual, PBC, odd).
Since Hdual is reflection-positive in both space and time with unique paramagnetic ground state,
certifying a dual exact-Q purity-bootstrap boundγdual >0at( L0,βdual)rigorously certifies the
uniform spectral gap ofHdual,∆ dual = lim infℓ→∞(Edual
1 (ℓ) −Edual
0 (ℓ)) ≥γdual/β0. By the exact
sector isomorphism above, this directly lower-bounds both the single-kink antiperiodic excitation
gap (∆kink = 2(1 −h)) and the even-sector periodic excitation gap above theg= 2doublet (which
for periodic 1D TFIM is the two-kink gap∆PBC = 4(1−h)>∆ kink).
5 Machine-Checked Lean 4 Formalization and Exact-Q Interval
Certification
To eliminate floating-point rounding bugs and hidden proof gaps, we decouple numerical partition-
function evaluation from thermodynamic-limit certification via a fail-closed two-layer architecture:
1. Zero-Dependency Lean 4 Kernel (lean/PurityBootstrap.lean).All 16 core theorems
are formalized parametrically over an arbitrary linearly ordered commutative fieldOrdField
K (simultaneously instantiating bothR and Q) with zero external dependencies (no Mathlib),
zero sorry, and zeroClassical.choice. Table 1 provides the complete Claim-to-Theorem
Manifest audited bylean/AuditAxioms.lean.
2. Zero-Float-Trust Exact-Q Certificate Verifier (src/purity_bootstrap.py).Given
finite-sample or numerical purity estimatesˆpj with certified error radiusϵj ≥0, we form
exact rational lower boundsp(0)
j = ⌊(ˆpj −ϵj) ·109⌋/109 ∈Q . At every cyclic Gauss–Seidel
10

--- Page 11 ---
Table 1:Claim-to-Theorem Verification Manifest(leanprover/lean4:v4.35.0, 0 external
dependencies, 0sorry, 0Classical.choice). Every symbol is checked bylake build && lake
env lean AuditAxioms.lean.
Paper Result Lean 4 Symbol (PurityBootstrap.lean) Scope Formalized Audited Axioms
Thm. 2.2squaring_inequality_k1
∑
w4
i ≥p2 −(1−p) 2/2on∆ + propext, Quot.sound
Thm. 2.2squaring_inequality_k1_sharpExact equality on all 2-level spectra none
Thm. 2.2squaring_inequality_ratioNormalizedq/p 2 ≥h∗(p)forp>0propext, Quot.sound
Thm. 2.2, 5.1hStar_monotone0<p≤q≤1⇒h ∗(p)≤h ∗(q)none
Thm. 2.3(a)dominant_weight_ge_purityDominant weightw 0 ≥ppropext, Quot.sound
Thm. 2.3(a)purity_defect_ge_two_w0_tailSharp defect1−p≥2w 0(1−w 0)none
Thm. 2.3(a)sharp_discriminant_lower_bound(2w 0 −1) 2 ≥2p−1none
Thm. 2.3(b)sharp_gap_ratio_boundw 0/w1 ≥2w2
0/(1−p)none
Eq. (8)plaquette_exact_identityS 01T2
00 =T10S2
00 none
Eq. (9)plaquette_lower_boundS 2
00T10 ≤S01 none
Thm. 3.1(a)gs_1d_step_soundSingle 1D cyclic GS step soundness none
Thm. 3.1(a)gs_1d_induction_soundN-step inductive 1D GS soundness none
Thm. 3.1, 5.1gs_1d_monotoneComponentwise interval monotonicity none
Thm. 3.2(b)hypercube_Q_step_soundQ 2k
≤R2k
k in arbitraryDnone
Thm. 4.1doubly_exponential_contractionu n+1 ≤Cu2n ⇒Cun ≤(Cu0)2n
propext, Quot.sound
Thm. 4.2intervening_length_purity_transferExactT(ℓ,β)transfer bound (22) none
step, h∗
1(q)is evaluated in exact arbitrary-precisionQ (fractions.Fraction) and soundly
roundeddownwardto denominator10 12 (⌊x· 1012⌋/1012 ≤x ). Crucially, even the final
thermodynamic mass-gap lower bound∆Q
cert ∈Q is verified with zero floating-point trust:
writing x= 1/ρN = 2kr with k∈N and r∈ [1,2) ∩Q , every omitted term in the positive
series logx = klog 2 + 2∑∞
j=0
t2j+1
r
2j+1 (tr = (r−1)/(r+ 1) ∈[0,1/3)) is strictly positive, so the
M-term rational partial sum gives a provable exact-Q lower boundlogQ(1/ρN) <log (1/ρN),
and the verifier checksγQ
lb ≤log Q(1/ρN)/2N and∆ Q
cert ≤γ Q
lb/β0 strictly inQ (rejecting any
tampered rational or float gap field).
Theorem 5.1(Soundness of Downward-Quantized Exact-Q and Interval Certification).Suppose
true finite-size purities satisfyptrue
j ≥p(0)
j ∈Q∩ (1/2,1](with probability at least1 −α for finite-
sample confidence intervals). If the downward-quantized exact-Q trace( p(0),...,p (N) )satisfies
p(n+1)
k ≤h∗
1(Π(n)
k )for every stepn<N and axisk, with all intermediate products>1/2, satisfies
0 <uN and Kd(uN)uN <1in Q, and satisfies0 <∆Q
cert ≤log Q(1/(Kd(uN)uN))/(2Nβ0)in Q,
then∆ Q
cert is a valid lower bound on∆∞ (with probability at least1−α).
Proof. Immediate by induction from hStar_monotone, gs_1d_monotone, and Theorem 4.1:
downward quantization at each step only decreasesp(n+1)
k , which preserves the invariantp(n)
k ≤
ptrue,(n)
k at every subsequent step.
6 Numerical Experiments and Benchmarks
Allexperimentsaredeterministicallyreproducedby python scripts/run_all_experiments.py
and independently checked bypython scripts/verify_all.py, which replays all 7 exported
.cert.json files strictly overQ (including exact rational logarithm mass-gap bounds) with zero
floating-point trust.
6.1 Experiment 1: 50,000-Trial Falsification Audit and SharpD-Dimensional
Thresholds
We first subjected Theorem 2.1 and Theorem 2.3 to an adversarial 50,000-trial stress test across
Dirichlet distributions of dimensionm∈ [2,15]and concentration α∈ [10−1.5,10], covering
11

--- Page 12 ---
Table 2:Exact D-Dimensional Critical Purity-Defect Thresholdsvs. Grover [7] (a=
2d+1 −1), comparing like-for-like hypercube-product defects1−Q alongside per-axis uniform
defectsu ∗
c(d).
d(D)aPer-Axisu ∗c(d)Uniform1−p c(d)a UniformQ-Gain Single-Q1−Q ∗c(d)Grover1/(2a 2)Single-QGain
1 (2) 31.2731×10 −1 3.3537×10 −1 11.29×† 1.8100×10 −1 5.5556×10 −2 3.26×
2 (3) 73.1474×10 −2 2.0057×10 −1 19.66×5.3913×10 −2 1.0204×10 −2 5.28×
3 (4) 157.8294×10 −3 1.1122×10 −1 50.05×1.4585×10 −2 2.2222×10 −3 6.56×
4 (5) 311.9543×10 −3 5.8840×10 −2 113.1×3.7797×10 −3 5.2029×10 −4 7.26×
5 (6) 634.8836×10 −4 3.0305×10 −2 240.6×9.6100×10 −4 1.2598×10 −4 7.63×
†In d= 1, uniformQ-Gain compares1 −pc(1)3 = 0.3354against Grover’s 1D uniform box1−0.993 = 0.0297(per-axis gain
12.73×); ford≥ 2, both UniformQ-Gain and Single-QGain compare against Grover’s1/(2a2)(corresponding per-axis gain
vs.1−(1− 1
2a2 )1/a is21.5×atd= 2to244.2×atd= 5).
0.80 0.85 0.90 0.95 1.00
Initial spatial purity S(L0, β0)
0.70
0.75
0.80
0.85
0.90
0.95
1.00
Initial temporal purity T(2L0, β0)
(a) Anisotropic 1D Purity-Bootstrap Basin
Exact Gauss–Seidel boundary ∂(1)
gap
Certifiable gapped basin (1)
gap
Grover cutoff u ≤ 0.01
Uniform root pc(1) = 0.8727
1D TFIM (L0 = 4, h = 2.0)
1 2 3 4 5
Spatial dimension d (D = d + 1 space-time axes)
10−4
10−3
10−2
10−1
Max certifiable hypercube defect 1 − Q
(b) Sharp D-Dim Thresholds (3.3 × –7.6 ×  Single-Q)
Ours: uniform product 1 − pc(d)a
Ours: single-Q worst-case 1 − Q *
c (d)
Grover (2026): 1/(2a2)
Figure 1:(a)Exact anisotropic 1D Gauss–Seidel certifiable basinB(1)
gap compared to Grover’s
uniform boxu≤ 0.01(top-right corner). The green star marks the exact-Q certified 1D TFIM
witness at( L0 = 4,β0 = 2,h = 2.0)with S0 = 0.8656 < pc(1) = 0 .8727.(b)Like-for-like
hypercube-product defect thresholds1 −pc(d)a (uniform) and1 −Q∗
c(d)(worst-case single-Q)
across d = 1,..., 5, demonstrating the3 .26×–7.63×(asymptotically8 ×) single-Q gain and
19.7×–240.6×uniform gain over Grover’s1/(2a2).
k = ⌊1/p⌋ ∈ {1,..., 14}. We observed0/50,000squaring-law violations (minimum slack
−1.11 ×10−15) and0/50,000gap-ratio violations (minimum relative slack −8.77 ×10−13,
computed via the cancellation-free identity1−p=w 0(1−w 0) + ∑
i≥1 wi(1−w i)).
Table 2 and Figure 1 present dimensionally consistent comparisons of our exact uniform and
single-Q critical thresholds against Grover [7] across spatial dimensionsd= 1,..., 5. In d= 1,
our per-axis uniform thresholdu∗
c(1) = 0.127311is 12.73×wider than Grover’s0.01(and our
uniform product defect1 −pc(1)3 = 0.3354is11 .29×wider than1 −0.993 = 0.0297), while our
anisotropic basin boundary∂B(1)
gap (Figure 1a) even certifies states withS0 <pc(1)—illustrated
by the 1D TFIM atL0 = 4,β0 = 2,h = 2.0( S0 = 0.8656 <0.8727, T0 = 0.9538), which certifies
∆∞≥0.3739over Q. In higher dimensions (d≥ 2), comparing like-for-like hypercube-product
defects1 −Q against Grover’s1 /(2a2), our worst-case single-Q gain climbs monotonically
from3 .26×(d = 1) and5 .28×(d = 2) to7 .63×(d = 5), converging to the theoretical8×
asymptote (18), while for uniform staircase purities1−pc(d)a exceeds1 /(2a2)by19 .66×(d= 2)
up to240.6×(d= 5).
12

--- Page 13 ---
Table 3:1D TFIM Exact-Q Thermodynamic Gap Sweep at(L0 = 8,β0 = 4)(∆ exact =
2(h− 1)). Every certified entry passes independent zero-float-trustQ verification including
rational logarithm bounds.
h∆ exact S0 T0 NOurs∆ cert (Q) Grover∆ cert Tightness Gain
1.40 0.80 0.8765 0.8964 50.1040fails∞
1.50 1.00 0.9197 0.9489 40.3079fails∞
1.80 1.60 0.9762 0.9947 30.6955fails∞
2.00 2.00 0.9883 0.9989 20.8716fails∞
2.25 2.50 0.9948 0.9998 21.08290.17336.25×
2.50 3.00 0.9974 1.0000 21.26650.17337.31×
3.00 4.00 0.9993 1.0000 21.56430.17339.03×
1.4 1.6 1.8 2.0 2.2 2.4 2.6 2.8 3.0
Transverse field h (hc = 1)
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Thermodynamic mass gap Δ∞
(a) 1D TFIM Certified Gap (L0 = 8, β0 = 4)
Exact gap Δexact = 2(h −1)
Ours: exact-ℚ certified Δ∞
Grover (2026): log(2)/β0
L0 = 4
β0 = 2
L0 = 8
β0 = 4
L0 = 16
β0 = 8
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Distance to quantum critical point hmin −1 (b) Critical-Point Approach (2.2 × –4.7 ×  Closer)
Ours: hmin −hc (exact-ℚ)
Grover (u ≤0.01): hmin −hc
Figure 2:(a)1D TFIM thermodynamic mass gap certified over exactQ at( L0 = 8,β0 = 4),
tracking∆ exact = 2(h−1)and beating Grover’s flatlog(2)/β0 = 0.1733ceiling by up to9 .03×.
(b)Distance to the critical pointhmin−1across three lattice scales, demonstrating a2.24×–4.72×
closer approach to criticality.
6.2 Experiment 2: 1D Transverse-Field Ising Model Phase Diagram and
Critical Approach
We benchmarked our exact-Q certifier on the periodic 1D transverse-field Ising modelH(h) =
−∑L
i=1 ZiZi+1 −h ∑L
i=1 Xi (quantum critical pointhc = 1, exact paramagnetic thermodynamic
gap∆ exact = 2(h−1)[ 16]). Partition functions are evaluated via Kaufman’s exact four-sector
Jordan–Wigner formula [10] in cancellation-freelog1p/expm1 arithmetic, cross-checked against
full2 L-dimensional exact diagonalization atL∈{ 4,6,8}and h∈{ 0.5,1.0,1.3,2.0}to within
5.3×10 −14 across all 12 checks.
Figure 2 and Table 3 present two key comparisons:
• Critical-point approach:At( L0 = 4,β0 = 2), our exact-Q bootstrap certifies gappedness
down to hmin = 1.8408vs. Grover’s hmin = 4.9659—4.72×closer to hc = 1in distance
hmin −1. At( L0 = 8,β0 = 4), hmin = 1.3788vs.2 .0461( 2.76×closer); at( L0 = 16,β0 = 8),
hmin = 1.1834vs.1.4116(2.24×closer).
• Breaking the( log 2)/β0 ceiling:At( L0 = 8 ,β0 = 4), Grover’s bound is frozen at
log(2)/4 = 0.1733for allh≥2.05and fails to certify anything forh≤2.0. In contrast, our
Theorem 4.1 certifies∆∞≥0.1040already at h= 1.4, climbs smoothly to1.0829at h= 2.25
(6.25×tighter),1 .2665at h= 2.5(7 .31×tighter), and1.5643at h= 3.0( 9.03×tighter than
Grover).
13

--- Page 14 ---
6.3 Experiment 3: Bond-RP No-Go for AKLT, Strictly Bond-RP Interacting
Chains, and Ferromagneticg= 2Duality
Before applying the purity bootstrap to interacting quantum spin chains, one must verify spatial
reflection positivity [5]—a nontrivial physical prerequisite. Strikingly, the celebrated Spin-1
AKLT chain [1] fails this prerequisite completely:
Proposition 6.1( su(3)Determinant Obstruction to Bond-Reflection Positivity of AKLT).
Consider the Spin-1 bilinear–biquadratic bond interactionhbiq(c) =S i·Si+1 +c(Si·Si+1)2 (which
equals2 HAKLT up to a constant shift atc= 1/3). Expanding−hbiq(c) = c0I⊗I+∑8
a,b=1 JabTa⊗Tb
in an orthonormal Hermitian Gell-Mann basis{Ta}8
a=1 of su(3)yields eigenvalues −(2 −c)
(multiplicity3, dipole) and −c (multiplicity5, quadrupole), whence det(J) = (2 −c)3c5. For
every c∈ (0,2)—in particular AKLT (c= 1/3, det(J) = 125/6561 ≈+1.905 ×10−2 >0)—and
everyanti-unitary bond reflectionΘ( A) = UAU† (U∈U (3)), the reflected interaction matrix
M(U) =JAd(U) TSconj satisfies
det
(
M(U)
)
= det(J)·(+1)·(−1) 3 =−det(J)<0,
becauseAd(U) ∈SO (8)has determinant+1while complex conjugation Sconj flips the3imaginary
Gell-Mann generators. Thus M(U)can never be positive semidefinite for any U∈U (3).
Conversely, for c≤ 0(isotropic Heisenberg c = 0and negative-biquadratic c <0), choosing
Uy = eiπSy
yields M(Uy)with eigenvalues {2 −c (×3),−c (×5)}≥ 0, guaranteeing strict
bond-reflection positivity.
Direct continuous-time evaluation of the exact Fröhlich–Israel–Lieb–Simon (FILS) bond-
reflection Gram matrixGbond on L= 4at β = 1(verified in tests/test_suite.py) confirms
Proposition 6.1 decisively: AKLT (c= +1/3) hasλmin(Gbond) = −0.5016 <0(violating bond-
RP), whereas Spin-1 Heisenberg (c = 0, λmin = +1.6143), Spin-1 Heisenberg with single-ion
anisotropy D = 6.0( λmin = +1.085 ×10−4), Spin-1 negative-biquadraticc = −0.5( λmin =
+1747.5), and the Spin-1/2dimerized antiferromagnetic Heisenberg chain atδ = 0.5( λmin =
+0.0865) are all strictly positive definite (Gbond ≻0).
We therefore benchmark our exact-Q bootstrap ontwo genuinely interacting, non-
integrable, provably bond-reflection-positive spin chainsusing exactSz-blocked full-
spectrum diagonalization:
1. 1D Spin-1 Heisenberg Chain with Single-Ion Anisotropy: H(D) = ∑L
i=1
(
Si ·
Si+1 + D(Sz
i)2)
at L0 = 4 →2L0 = 8(3 8 = 6 ,561states), β0 = 2 .0. Because( Sz
i)2
is on-site and invariant underUy(·)U†
y, H(D)is translation-invariant and strictly bond-
RP for allD∈R . As shown in Figure 3(a), our exact-Q bootstrap certifies a rigorous
thermodynamic mass gap starting atD= 4.5(∆ ∞≥0.1140, anisotropicS0 = 0.8032 <pc(1),
T0 = 0.9783), climbing to∆∞ ≥0.3974( D = 5.0), ∆∞≥0.7245 (D = 6.0, exported as
spin1_aniso_D6p0_L4_exact_gap.cert.json), and∆∞≥1.1651 (D= 8.0, S0 = 0.9589,
T0 = 0.99997), whereas Grover’su≤0.01fails at every singleD∈[4,8]!
2. 1D Spin-1/2Dimerized Antiferromagnetic Heisenberg Chain: H(δ) = ∑L
i=1(1 +
(−1)iδ)S i ·Si+1 at L0 = 6 →2L0 = 12(2 12 = 4,096states), β0 = 6.0. Reflection across al-
ternating bonds yields a positive 2-site unit-cell transfer operatorK = T1/2
strongTweakT1/2
strong ⪰
0( Gbond ≻ 0), so Z(2m,β) = Tr(Km)is strictly reflection-positive for all even L =
2m. Our exact-Q bootstrap certifies∆ ∞ ≥0.0161( δ = 0.35, anisotropic S0 = 0.8047),
∆∞ ≥ 0.1361( δ = 0 .40), ∆∞≥0.2863 (δ = 0 .50, L = 12gap1 .1890, exported as
spinhalf_dimerized_d0p5_L6_exact_gap.cert.json), and∆∞≥0.4442 (δ= 0.60,S0 =
0.9721, T0 = 0.9962), whereas Grover (u≤ 0.01) againfails across the entire sweep
δ∈[0.30,0.60].
14

--- Page 15 ---
4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0
Single-ion anisotropy D in H(D) = ∑(Si ⋅ Si + 1 + D(Sz
i )2)
0
1
2
3
4
5
6
Thermodynamic mass gap Δ∞
(a) Strictly Bond-RP Spin-1 H(D) (L0 = 4 → ∞)
Spin-1 H(D) (L0 = 4, β0 = 2): exact-ℚ Δ∞
Spin-1 H(D) exact ED gap (L = 8)
Grover (u ≤ 0.01): fails at all D ∈ [4, 8]
0.000 0.025 0.050 0.075 0.100 0.125 0.150 0.175
2D hypercube purity defect 1 − Q(L0, β0)
0
1
2
3
4
5
Certified dimensionless gap β0Δ∞
(b) 2D (D = 3) Certified Gap vs. Defect 1 − Q0
Ours: exact-ℚ 2D bound β0Δ∞
Grover 2D (1 − Q ≤ 1/98): log 2
Figure 3:(a)Exact- Q thermodynamic mass-gap certification on the strictly bond-RP interacting
Spin-1 chainH(D) = ∑(Si ·Si+1 + D(Sz
i)2)purely from L0 = 4,2L0 = 8exact diagonalization
(β0 = 2), climbing to∆∞≥1.1651at D= 8while Grover (u≤ 0.01) fails across allD∈ [4,8].
(b)2D (d= 2,D = 3) exact-Q certified dimensionless gapβ0∆∞vs. uniform hypercube defect
1−Q 0, certifying up to1−Q0 = 0.19and reaching8.23×Grover’s flatlog 2bound.
Honest Finite-Size Boundary (Isotropic Spin-1 Heisenberg Chain,D= 0).At D= 0,
H(0)is strictly bond-RP (λmin(Gbond) = +1.6143 >0), yet its correlation length isξ≈ 6.03
sites [18]. EvaluatingL0 = 4 <ξ at β0 = 8gives S(4,8) = 0.0051 <1/2(while T(8,8) = 0.9502),
confirming honestly thatL0 = 4is physically too small to enter the bootstrap basin for isotropic
Spin-1 Heisenberg; larger initial blocksL0 ≳ 16(as computed in [14]) are required before the
spatial transfer matrix becomes purity-dominated.
Ferromagnetic 1D TFIM (g= 2Quasi-Degenerate Doublet).Applying Corollary 4.4
at L0 = 8,β0 = 4in the ferromagnetic phaseh∈{ 0.4,0.5,0.6}certifies uniform exact-Q lower
bounds on the dual / single-kink excitation gap∆kink = 2(1 −h)(and hence also on the
periodic two-kink excitation gap∆PBC = 4(1 −h)above the g = 2doublet):∆ dual ≥0.5258
(∆kink = 1.20,∆ PBC = 2.40) ath= 0.4,∆ dual ≥0.3573(∆ kink = 1.00,∆ PBC = 2.00) ath= 0.5
(exported as tfim1d_ferro_h0p5_g2_twist.cert.json), and∆ dual ≥0.1487(∆ kink = 0.80,
∆PBC = 1.60) at h = 0.6. Independently measured finite-size doublet splittings confirm the
expected exponential decayδL ∝hL (δ8 = 1.46 ×10−3, δ12 = 7.25 ×10−5, δ16 = 3.87 ×10−6 at
h= 0.5). Ath= 0.7,T dual = 0.7461exits the(L 0 = 8,β0 = 4)basin and honestly abstains.
6.4 Experiment 4: 2D (D = 3) Exact-Q Certificates and Synthetic Noisy
Interval Audit
Figure 3(b) benchmarks our exact-QD = 3cyclic Gauss–Seidel certifier on 2D reflection-positive
hypercubes across uniform hypercube defects1−Q0 ∈[0.001,0.190](with exact-Q certificate
exported at1 −Q0 = 0.050). Whereas Grover’s 2D cutoff1−Q≤ 1/98 = 0.0102fails above
0.0102and saturates at β0∆∞= log 2 = 0.6931, our exact-Q certifier reachesβ0∆∞≥5.7057
at1 −Q0 = 0.001( 8.23×tighter) and remains strictly certified all the way to1−Q0 = 0.190
for uniform purities (18.6×larger defect; up to1−Q∗
c(2) = 0.0539,5 .28×Grover, even under
worst-case single-Qanisotropy).
Finally, we audited Theorem 5.1 in a 200-trial synthetic Gaussian-noise estimation campaign
(mimicking finite-sample QMC purity estimators) with Bonferroni-adjusted conservative lower
intervalsˆp−2.576σ stat:
• Gapped 1D TFIM (h = 2.0, L0 = 8,β0 = 4,∆ exact = 2.0):At σstat = 0.005(radius
15

--- Page 16 ---
0.0129),200/200trials certified validly (median∆ cert = 0.6292 ≤2.0); even at large noise
σstat = 0 .015(radius0 .0386, nearly4 ×Grover’s entire0 .01tolerance),200/200trials
certified validly (median∆cert = 0.3974≤2.0).
• Near-boundary adversarial control (Strue = Ttrue = 0.871 < pc(1) = 0.8727, σstat =
0.005): 0/200false certifications (100% fail-closed soundness).
• Gapless critical control (h= 1.0,∆ exact = 0.0, σstat = 0.015): 0/200false certifications
(100% fail-closed soundness).
7 Discussion, Limitations, and Scope
Our results establish that the reflection-positive purity bootstrap is dramatically sharper than
previously realized: exact simplex optimization, staggered cyclic Gauss–Seidel multi-axis updates,
and doubly-exponential contraction together widen certifiable basins by an order of magnitude
and eliminate the(log 2)/β0 ceiling, all backed by zero-dependency Lean 4 proofs and zero-float-
trust exact-Qreplayable certificates.
Three honest boundaries define the scope of our current work: (i) reflection positivity in all
D space-time directions is a stringent physical prerequisite—as demonstrated starkly by our
su(3)determinant obstruction (Proposition 6.1) ruling out bond-RP for the Spin-1 AKLT chain
and all positive-biquadratic chainsc∈ (0,2), alongside generic sign-problematic fermionic or
chiral models; (ii) as demonstrated by our isotropic Spin-1 Heisenberg diagnostic atL0 = 4, the
initial lattice scaleL0 must still exceed the correlation lengthξ for spatial purities to enter the
basin—our sharper thresholds reduce the requiredL0 and β0 substantially, but cannot bypass
ξ; and (iii) in our 2D (D= 3) experiment we verified the exact-Q multi-axis recurrence across
uniform and single-Q defect regimes rather than running a full 2D QMC simulation, leaving
coupling to debiased finite-sample QMC estimators [4] as a natural next step for certifying 2D
bilayer Heisenberg and anisotropic spin-1phases.
References
[1] Ian Affleck, Tom Kennedy, Elliott H. Lieb, and Hal Tasaki. Rigorous results on valence-bond
ground states in antiferromagnets.Physical Review Letters, 59(7):799–802, 1987.
[2] Ian Affleck, Tom Kennedy, Elliott H. Lieb, and Hal Tasaki. Valence bond ground states in
isotropic quantum antiferromagnets.Communications in Mathematical Physics, 115(3):477–
528, 1988.
[3] Anurag Anshu. Improved local spectral gap thresholds for lattices of finite dimension.
Physical Review B, 101(16):165104, 2020.
[4] Antigravity Frontier Research Agent. Holomorphic obstructions and surrogate-
debiased finite-sample spectral certificates for machine-learned quantum monte carlo.
AIRR.SCIENCE Deposit SUB-7DC055DD25EB761E; companion code athttps://github.
com/lluiseriksson/qcqmc-spectral-certificates, 2026.
[5] Jürg Fröhlich, Robert Israel, Elliott H. Lieb, and Barry Simon. Phase transitions and
reflection positivity. I. general theory and long range order.Communications in Mathematical
Physics, 62(1):1–34, 1978.
[6] David Gosset and Evgeny Mozgunov. Local gap threshold for frustration-free spin systems.
Journal of Mathematical Physics, 57(9):091901, 2016.
16

--- Page 17 ---
[7] Tarun Grover. Extensions of the Haldane gap proof: Higher dimensions, near degeneracy,
fermions and tensor-network states.arXiv preprint arXiv:2611.07400, November 2026.
[8] F. D. M. Haldane. Continuum dynamics of the 1-D Heisenberg antiferromagnet: Identifica-
tion with theO(3)nonlinear sigma model.Physics Letters A, 93(9):464–468, 1983.
[9] F. D. M. Haldane. Nonlinear field theory of large-spin Heisenberg antiferromagnets:
Semiclassically quantized solitons of the one-dimensional easy-axis Néel state.Physical
Review Letters, 50(15):1153–1156, 1983.
[10] Bruria Kaufman. Crystal statistics. II. partition function evaluated by spinor analysis.
Physical Review, 76(8):1232–1243, 1949.
[11] Stefan Knabe. Energy gaps and elementary excitations for certain VBS-quantum antiferro-
magnets.Journal of Statistical Physics, 52(3–4):627–638, 1988.
[12] H. A. Kramers and G. H. Wannier. Statistics of the two-dimensional ferromagnet. Part I.
Physical Review, 60(3):252–262, 1941.
[13] Marius Lemm and Evgeny Mozgunov. Spectral gaps of frustration-free spin systems with
boundary.Journal of Mathematical Physics, 60(5):051901, 2019.
[14] OpenAI Science Team. Computer-assisted reflection-positive purity bootstrap for the
Haldane gap in spin-1 quantum spin chains. Technical Research Note, September 2026,
2026. Introduced the reflection-positive partition-function purity doubling argument.
[15] Konrad Osterwalder and Robert Schrader. Axioms for Euclidean Green’s functions.Com-
munications in Mathematical Physics, 31(2):83–112, 1973.
[16] Pierre Pfeuty. The one-dimensional Ising model with a transverse field.Annals of Physics,
57(1):79–90, 1970.
[17] Hal Tasaki. A note on the purity-bootstrap proof of the Haldane gap. Online Research Notes,
Gakushuin University, 2026. Exposition and rigorous formulation of the reflection-positive
purity doubling bootstrap in 1D.
[18] Steven R. White and David A. Huse. Numerical renormalization-group study of low-
lying eigenstates of the antiferromagneticS = 1Heisenberg chain.Physical Review B,
48(6):3844–3852, 1993.
17
