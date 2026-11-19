Stationary concentration and local return in Boolean Doob chains
                                             Lluis Eriksson

        Supplement to Rank defects and spectral stability of Boolean Doob chains


                                                 Abstract
         For half-correlated Boolean noise, we study how a reversible change of transition probabilities
     affects the ordered spectrum when the stationary coordinate marginals are exactly uniform
     through increasing order. At the stationary moment endpoint we prove recovery under an
     exponential cutoff on the critical density tail. For every stationary moment order strictly above
     three and a fixed positive density floor, we identify a set of vertices on which local one-step
     return characterizes full spectral recovery. Its killed eigenvalue also determines the second
     eigenvalue up to exponential accuracy. Interpolating stationary densities in an existing shell
     construction gives chains with any prescribed finite number of correct leading noise bands and
     a persistent error lowerpin the spectrum. Without coordinate matching, the endpoint relaxation
     time is at most exp(C L log(2L)) in dimension L. Above the endpoint the spectral gap has a
     dimension-independent positive lower bound. For a two-valued stationary density, a bounded
     cubic moment gives a dimension-independent gap. The entire ordered spectrum varies from
     ordinary noise by at most Cb ∥π − 1∥3 without matching, and a two-coordinate example attains
     linear order. We extend both estimates to finitely many stationary levels whose uniform masses
     have comparable logarithms, with an explicit sufficient ratio bound. The gap also holds with
     variable heights under separate cubic envelopes on the exceptional sets. With unrestricted
     ratios, three exact stationary values suffice for exponential trapping even as the density tends
     to one in a fixed norm of order greater than three. Under linear-order marginal matching
     the trap persists at exponentially small distance from a three-valued law, whereas vanishing
     log-uniform distance from a two-valued law rules out an exponential trapping rate under the
     same floor and cubic cap. For stationary laws on binary linear quotients, fractional packing of
     coordinate bases gives a separate sufficient condition for exponential recovery. Three full bases
     suffice at the second moment and two suffice at any stationary moment order above 15/7. The
     stationary minimum may tend to zero.


1    Concentration required for failure at the stationary endpoint
Let µ be uniform on the binary L-cube. Write P = P1/2 , Q = P1/√2 , g = P h, π = hg, and
U = h/g, with h > 0 and Eµ π = 1. Let K(x, y) = P (x, y)h(y)/g(x) and let ∆ denote the
maximum absolute difference of the ordered eigenvalues of K and P , including multiplicities.
Assume π ≥ b > 0, ∥π∥p ≤ B, and exact uniformity of all stationary coordinate marginals through
order k → ∞. Throughout this section
                           √
                p = (17 + 4 13)/9,     q = 6p/(p − 3),        1/3 = 1/p + 2/q.

All norms use µ. All constants b, B are uniform along the sequence.




                                                     1
Endpoint concentration criterion. Fix rates, independently of dimension, satisfying
                                     6 log 2                  6 log 2 + 12τ
                            0<τ <            ,     0<σ<                     .
                                     q − 12                          p
Define
                      Ak = {g < e−τ k , π > eσk },        d∗ = lim sup ∥π1Ak ∥p .
                                                                   k→∞
If d∗ < b, then
                                                         B 2 d∗
                                      lim sup ∆ ≤                 .                            (EC1)
                                        k→∞            (b − d∗ )2
In particular, vanishing of the critical stationary moment on Ak suffices for full spectral recovery
at any diverging matching order. A condition involving the stationary density alone is

                                       Eµ [π p 1{π>eσk } ] −→ 0.                               (EC2)

Uniform integrability of π p implies (EC2). The converse fails even among exactly matched chains
with a fixed stationary floor.
   Since τ may approach its upper bound, (EC2) suffices for any fixed σ < 6 log 2/(6−p) with σ > 0.
Indeed 6q/[p(q − 12)] = 6/(6 − p). In particular it is enough that lim sup k −1 log2 ∥π∥∞ < 6/(6 − p).
For example, when π is constant on cosets of a linear map of rank s, each atom of the quotient has
probability 2−s and ∥π∥∞ ≤ B2s/p . Thus lim sup s/k < 6p/(6 − p) suffices, regardless of ambient
dimension or the ranks of disjoint column families.

Critical exponents without iteration. Put 1/u = 1/p+1/q and v = 1+4(u−1). Substitution
of 9p2 − 34p + 9 = 0 gives q = 4(1 + v) − 1. Forward hypercontractivity for P sends Lu to Lv
contractively. Reverse hypercontractivity with source exponent −v and target exponent −q gives
∥1/g∥q ≤ ∥1/h∥v : the ratio (1+v)/(1+q) is 1/4. The floor implies 1/h = g/π ≤ g/b. Consequently,

                                H := ∥1/g∥q ≤ b−1 ∥g∥v ≤ b−1 ∥h∥u .                            (EC3)

These inequalities hold in each finite dimension. Simply replacing ∥h∥u by BH would give no
uniform bound.

What matching controls. Let a = Eh, F = Qh and V = ∥F − a∥22 = 1 − a2 . By Cauchy–
Schwarz under
           √     h dµ, 1 ≤ aEπg. The high-degree part of g = QF above order k has norm at most
  −(k+1)/2   V in L2 . Matching annihilates
2                                       √ the lower nonconstant part against π − 1. Since p > 2,
it follows that V ≤ a(B + 1)2−(k+1)/2 V . This includes V = 0 and yields ∥g − 1∥2 ≤ CB 2−k/2
using 1 − a ≤ V . In fact ∥g − 1∥3 ≤ CB 2−k/2 because g − a = Q(F − a) and Q is contractive from
L2 to L3 .

A low denominator forces high denominators among its neighbors. The floor gives
g = P (π/g) ≥ bP (1/g). For T ≥ T0 = 4/b, put ST = {g > bT /2}. If g(x)−1 > T , then

                                 Px (STc ) ≤ (bT /2)P (1/g)(x) < 1/2.

The cubic estimate for g − 1 gives µ(ST ) ≤ CB,b 2−3k/2 T −3 . For any 1 < r < 4, choose m =
3/(4 − r) > 1 and ℓ = 4m − 3. Forward hypercontractivity of P from Lm to Lℓ and Markov’s
inequality give

                   µ{g −1 > T } ≤ 2ℓ ∥P 1ST ∥ℓℓ ≤ 2ℓ µ(ST )r ≤ CB,b,r 2−3rk/2 T −3r .         (EC4a)

                                                   2
This additional use of the floor controls the geometry of the exceptional set before applying (EC3).
   Write D = {g < e−τ k }. Choose r < 4 close enough to four that both (q−3r)τ < (3r/2) log 2 and
pσ < (3r/2) log 2 + 3rτ . This is possible by the two strict rate conditions and q > 12. Integrating
(EC4a) up to T = eτ k bounds the integral of g −q on {T0 < 1/g ≤ eτ k } by C2−3rk/2 (1 + e(q−3r)τ k ) =
o(1). On {1/g ≤ T0 } the reciprocal is bounded and converges to one in probability. Consequently

                            ∥g −1 1Dc ∥q → 1,       ∥(g −2 − 1)1Dc ∥q/2 → 0.                    (EC4)

On D \ Ak , ∥π1D\Ak ∥p ≤ eσk µ(D)1/p = o(1) by (EC4a) at T = eτ k . Hence d∗ = lim sup ∥π1D ∥p .

Absorption on the exceptional set.              Split h = π/g over Dc and D in (EC3). Hölder gives

                                   bH ≤ B∥g −1 1Dc ∥q + ∥π1D ∥p H.

If d∗ < b, then lim sup H ≤ B/(b − d∗ ) by (EC4). A second application of Hölder gives ∥U 1D ∥3 ≤
∥π1D ∥p H 2 . Also ∥π1D ∥3 ≤ Bµ(D)1/3−1/p → 0 and, by (EC4), ∥(U − π)1Dc ∥3 → 0. This proves
the bound on the right of (EC1) for lim sup ∥U − π∥3 .
    For completeness, ∥QMU −π Q∥ ≤ ∥U −π∥3 by forward 2-to-3 hypercontractivity. For Mπ−1 split
each factor of Q at Walsh degree j = ⌊k/2⌋. Matching kills the low-low term. Writing p′ = p/(p−1),
the remaining high factors have 2-to-2p′ norm at most θj+1 where θ = (2p′ − 1)/2 < 1: factor
                                                                          p

Q = P1/√2p′ −1 Pθ and apply the Walsh tail bound to Pθ . The same factorization bounds the low
factors by one. The three terms therefore contribute at most 3(B + 1)θj+1 . Finally QMU Q and
the symmetric conjugate of K are the two Gram products of M√U Q. Min–max gives (EC1).

Necessary joint concentration. If ∆ ≥ η > 0 along a subsequence, then for every fixed
admissible pair τ, σ along that subsequence,

                     lim inf ∥π1Ak ∥p ≥ tη ,       B 2 tη = η(b − tη )2 ,   0 < tη < b.

Indeed the right-hand side of (EC1) is strictly increasing from zero to infinity on [0, b). A further
subsequence below tη would contradict (EC1). This localizes both the large stationary density
and the small denominator to the same vertices. The bound is on the integral of the pth power;
their stationary probability can tend to zero.
                                        √
A separating example. Take n = ⌊ k⌋ disjoint blocks of k + 1 bits. Let S be the event that
every block parity is positive, m = 2−n , and prescribe

                                       π = 1 + m−1/p (1S − m).

This density has mean one and a fixed positive floor for all sufficiently large k. Its nonconstant
Walsh terms have degree at least k + 1 by the block-parity expansion. It is realizable as hP h by
                √ diagonal scaling of the strictly positive matrix P with row sums π(x). Here
positive symmetric
log ∥π∥∞ = O( k), so (EC2) holds. Yet E[π p 1S ] → 1 while µ(S) → 0, and E[π p+ϵ 1S ] → ∞
for every fixed ϵ > 0. The complement contributes a bounded critical moment. This example
separates the hypotheses on stationary integrability; the theorem allows general stationary laws
beyond this particular block geometry.




                                                     3
Relation to earlier work and review context. The forward and reverse inequalities are
classical inputs (Bonami; Mossel, Oleszkiewicz and Sen). The realization in the example uses
Sinkhorn’s prescribed-row-sum theorem. The programme’s stationary-moment paper and its
subsequent matching-order estimate supply the setting and the matching-energy argument. The
new step is absorption at the exact fixed exponent using the critical mass on the common exceptional
set. It gives a conditional endpoint theorem. Whether the original floor, moment bound and
matching alone force recovery is open. This source appendix has an author-side analytic check.
Exact-PDF assessment, independent review and publication remain pending.


2    A local return test for the full ordered spectrum
Keep the half-noise model, the uniform matching through order k, the stationary floor b and the
moment bound B of the preceding section. In this section any fixed finite p > 3 is allowed. Put
q = 6p/(p − 3), choose 0 < σ < τ < (log 2)/q, and set

                            D = {g < e−τ k },           A = D ∩ {π > eσk }.

Write ν = πµ, s = ∥1A K1A ∥2→2,ν and

                               RA = max Prν (X1 ∈ E | X0 ∈ E).
                                     ∅̸=E⊆A

Both quantities are zero for empty A. There exist c, C > 0, depending only on the displayed fixed
parameters, for which
                                                                                            q
s/4 − Ce−ck ≤ ∆ ≤ s + Ce−ck ,        |λ2 (K) − max(1/2, s)| ≤ Ce−ck ,            RA ≤ s ≤2RA − RA 2.

                                                                                               (LR1)
In particular the full ordered spectrum converges precisely when every subset of this specified
exceptional set has vanishing one-step return, uniformly over those subsets. The second eigenvalue
can converge to 1/2 even when the criterion for the full spectrum fails; the formula for λ2 by
itself only detects s above 1/2. The two-sided bound on ∆ does not require knowing which noise
eigenvalue is displaced.
    There is a more detailed reconstruction  with multiplicities. Form a list from the ordinary cube
eigenvalues (each 2−j occurs Lj times) and all eigenvalues of the killed matrix KAA on A. Sort in
                                

decreasing order and keep the first 2L entries. Each entry differs from the corresponding eigenvalue
of K by at most Ce−ck . The additional matrix has order |A| ≤ CB 2L−k , with an empty matrix
allowed.

Isolating the multiplier that survives matching. The matching-energy proof above gives
∥g − 1∥2 ≤ CB 2−k/2 also for this p. The floor and Jensen give 1/g ≤ P g/b, and P g = P(1/2)3/2 Qh
with ∥Qh∥2 = 1. Forward hypercontractivity therefore gives ∥1/g∥9 ≤ 1/b. On Dc ∩ {g < 1/2},
µ{g < 1/2} ≤ CB 2−k and g −2 ≤ e2τ k . Since qτ < log 2, the Lq/2 norm of (g −2 − 1) on that part
decays exponentially. On {g ≥ 1/2} the function g −2 − 1 is bounded, and its absolute value is at
most 16|g − 1|; interpolation with the L2 estimate gives exponential decay in Lq/2 there too. Thus
∥(U − π)1Dc ∥3 ≤ Ce−ck by 1/3 = 1/p + 2/q.
   On the remaining low-denominator vertices outside A, use the ninth inverse moment directly:
                                                Z
                           ∥U 1D\A ∥33 ≤ e3σk       g −6 dµ ≤ b−9 e−3(τ −σ)k .
                                                D


                                                    4
Also ∥π1D ∥3 ≤ Bµ(D)1/3−1/p ≤ Ce−ck . Together these bounds give ∥U 1Ac − π∥3 ≤ Ce−ck . The
signed low/high Walsh estimate for π − 1 above uses only p > 3. By 2-to-3 hypercontractivity,

                         ∥QMU Q − (P + S)∥ ≤ Ce−ck ,           S = QMU 1A Q.                      (LR2)

The two Gram products of M√U 1A Q identify ∥S∥ = s. In particular S is positive semidefinite
with s ≤ 1.

Separation from the ordinary low eigenmodes. Let Π project onto Walsh degrees at most
m = ⌊δk⌋, where 0 < δ < 1 is fixed with δ log 7 < (log 2)/12. The floor bound above gives
∥U ∥3/2 ≤ B/b2 since 1/p + 2/9 < 2/3. For a unit vector z in this low space, ∥Qz∥8 ≤ 7m/2 : apply
the ordinary 2-to-8 inequality to a polynomial with each degree j multiplied by 7j/2 . Hölder with
reciprocal exponents 2/3, 1/4, 1/12 gives

                               ⟨z, Sz⟩ ≤ (B/b2 ) 7m µ(A)1/12 ≤ Ce−ck .

Positivity bounds the norm of the off-diagonal block of S by ∥ΠSΠ∥1/2 ∥S∥1/2 . On the comple-
mentary space P has norm at most 2−(m+1) . Consequently QMU Q differs in operator norm by at
most Ce−ck from the block diagonal operator

                        P |ran Π ⊕ SH ,       SH = (I − Π)S(I − Π)|ran(I−Π) .

Its high-block norm sH differs from s by at most Ce−ck as well. For large k, the low block contains
1 once and 1/2 with its ordinary multiplicity. The high block is positive with top eigenvalue
sH ≤ 1. This proves the second-eigenvalue estimate by min–max and Gram conjugation. The
upper bound on ∆ follows directly from (LR2).
    To verify the reconstruction, work on two copies of the cube space and compare P ⊕ S to
(ΠP Π) ⊕ ((I − Π)S(I − Π)). The norm error is exponentially small by the same two block estimates.
After permuting subspaces the latter is the displayed block diagonal operator with 2L extra zeros.
Also S has the nonzero eigenvalues of KAA with their multiplicities, by the Gram identity. Thus
min–max on the doubled space identifies the first 2L sorted entries with the claimed precision.
The size bound follows from µ(A) ≤ CB 2−k .
    For the lower bound, if sH ≤ 4 2−m it is absorbed by the error. Otherwise choose j with
sH /4 < 2−j ≤ sH /2, so 1 ≤ j ≤ m. In the ordered noise spectrum, let i be the first index at level
2−j . The low block already supplies the i − 1 eigenvalues strictly above this level, all at least 21−j .
The high block supplies one more at least 21−j . Its addition raises the ith eigenvalue by at least
2−j . This proves the first bound despite the growing noise multiplicities. Enlarging C covers the
finitely many smaller matching orders.

A test phrased entirely in one-step probabilities. Testing with an indicator gives RA ≤ s.
For the reverse bound take a nonnegative unit top vector f for the killed chain, extended by zero
outside A. Under its full stationary pair law J, integration over the level sets of f 2 gives
                               1          2        2                 2
                               2 EJ |f (X) − f (Y ) | ≥ (1 − RA )∥f ∥2,ν .

Indeed every nonempty positive level set lies in A, and its outward flow is at least 1 − RA times
√ stationary mass. Cauchy–Schwarz on (f (X) − f (Y ))(f (X) + f (Y )) bounds the left side by
its
  1 − s2 using stationarity and reversibility. This proves the last part of (LR1).


                                                   5
What nearly complete trapping requires in two ordinary noise steps. For x ∈ A, the
floor bound P (1/g)(x) ≤ g(x)/b implies Px (A) ≤ e−2τ k /b. Yet the stationary conditional return
under K may be much larger. For nonempty E ⊆ A, Cauchy–Schwarz under Px and the floor give
                                             b                  b Px (E c )2
                             Kx (E c ) ≥        Px (1E c /g) ≥               .
                                           g(x)                g(x) P g(x)
If λ2 (K) → 1, (LR1) supplies maximizing sets Ek with conditional return tending to one. Averaging
this last bound for x ∈ Ek gives Eν(·|Ek ) [(g P g)−1 ] → 0; hence g P g diverges in probability
under those conditional laws. Conversely a uniform upper bound g P g ≤ M on A gives s ≤
1 − b(1 − o(1))/M by the maximum killed row sum, for nonempty A. This rules out convergence
of the second eigenvalue to one in that regime.

A family with a correct spectral gap and incorrect lower bands. At half noise the
programme’s matched shell construction provides some fixed p0 > 3, a fixed floor, k = ⌊βL⌋,
∥πtrap − 1∥p0 ≤ e−c0 L , and λ2 → 1. Fix any 0 < a0 < 1. Interpolate the stationary densities by
πt = 1 + t(πtrap − 1), 0 ≤ t ≤ 1. They share all the matching, floor and moment estimates with
uniform constants. At each fixed dimension positive symmetric diagonal scaling gives the unique
ht > 0 satisfying ht P ht = πp t (here P ht is evaluated first). This scaling is continuous in t: each
ht (x) is bounded above by supt πt (x)/P (x, x), and the floor divided by the largest such upper
bound bounds every coordinate below. Any subsequential limit solves the same scaling equations,
so uniqueness gives continuity.
    Set N (t) = ∥QMht /(P ht ) Q − P ∥. This continuous quantity is zero at t = 0. By (LR2), |N (t) −
s(t)| ≤ Ce−ck uniformly in t, even though the exceptional vertex set can change discontinuously.
By (LR1), s(1) → 1. The intermediate value theorem gives tL with N (tL ) = a0 for every sufficiently
large L. For these chains
                     |λ2 (K) − max(1/2, a0 )| ≤ Ce−ck ,          ∆ ≥ a0 /4 − Ce−ck .
Moreover for every fixed j with 2−j > a0 , all the ordered eigenvalues in degrees 0 through j,
counted with the reference multiplicities, are within Ce−ck of their reference values. Indeed the
low block contains all those eigenvalues exactly, and the entire high block is below 2−j for large L.
In particular any prescribed finite number of leading Walsh bands can be asymptotically correct
while the full ordered spectrum has a fixed error. The available p0 comes from the matched shell
result below the stationary endpoint. This interpolation constructs no counterexample at the
endpoint itself.

Scope and provenance. The coarea estimate is the Dirichlet form argument underlying Goel,
Montenegro and Tetali’s spectral profile. The low-degree norm bound uses classical Boolean
hypercontractivity. The contribution here is the exponential operator approximation on a specific
joint tail and the eigenvalue count that converts a killed mode there into a defect of the full ordered
spectrum. The unrestricted endpoint still requires controlling returns for all subsets of that tail.
This is an analytic appendix with no exact-PDF assessment.


3    Global gap bounds without coordinate matching
Retain P = P1/2 , g = P h, π = hg, Eµ π = 1, π ≥ b > 0 and ∥π∥p ≤ B. In this section there is no
                                                                   √
assumption on any nonconstant Walsh coefficient. Write p∗ = (17 + 4 13)/9 and γ = 1 − λ2 (K),
for L ≥ 1.

                                                     6
Theorem. At p = p∗ ,                                    q
                                    γ ≥ exp[−Cb,B L log(2L)].                                     (G1)
In particular a gap of order exp(−cL) for fixed c > 0 is impossible at this exponent. For every
fixed p > p∗ there is a dimension-independent lower bound γ ≥ cb,B,p > 0. There are also ϵ0 , C > 0
depending only on b, B such that, uniformly for p∗ − ϵ0 ≤ p ≤ p∗ ,
                                                             q              
                              log(1/γ) ≤ C (p∗ − p)L +          L log(2L) .                       (G2)

The estimate controls cuts containing any number of distinct levels of h. At equality it leaves open
both a dimension-independent gap and recovery of the ordered spectrum under arbitrarily slow
matching.

Macroscopic cuts. Let J be the stationary edge probability and ν = πµ. The two-function
reverse hypercontractive inequality at correlation 1/2 with both input exponents 1/2 gives

                        J(E, E c ) = ⟨h1E , P (h1E c )⟩µ ≥ ∥h1E ∥1/2 ∥h1E c ∥1/2 .

Here ∥f ∥1/2 = (Eµ |f |)2 . For each nonempty set F , h ≥ b/g and conditional Jensen imply
                    p


               ∥h1F ∥1/2 ≥ bµ(F )2 (Eµ [g −1/2 | F ])2 ≥ bµ(F )2 /Eµ [g | F ] ≥ bµ(F )7/3 .

The last step uses ∥g∥3 = ∥Q(Qh)∥3 ≤ ∥Qh∥2 = 1. If 0 < ν(E) ≤ 1/2, then µ(E c ) ≥ (2B)−p/(p−1)
by Hölder, and ν(E) ≤ Bµ(E)1−1/p . Consequently

                           Φ(E) := J(E, E c )/ν(E) ≥ cb,B,p µ(E)4/3+1/p .                         (G3)

The constant stays positive uniformly on compact exponent intervals above one. If ∥KF F ∥ ≤ 1/2
for all µ(F ) ≤ e−s , all such small cuts have Φ(F ) ≥ 1/2 by the indicator test. The remaining cuts
satisfy (G3). Cheeger’s inequality γ ≥ 12 inf 0<ν(E)≤1/2 Φ(E)2 now yields log(1/γ) ≤ Cb,B,p (1 + s).
This step tests actual stationary returns, without postulating where the returning vertices or their
ordinary-noise neighbors lie.

Moment budget for the small cuts. Writing U = h/g, the floor and Jensen give 1/g ≤ P g/b
and ∥1/g∥9 ≤ 1/b. Given a bound Hj on ∥1/g∥qj , put 1/uj = 1/p + 1/qj . Hölder bounds
∥h∥uj ≤ BHj . Forward hypercontractivity bounds ∥g∥4uj −3 ≤ BHj ; 1/h ≤ g/b and reverse
hypercontractivity then give

              q0 = 9,      qj+1 = Fp (qj ) = 16pqj /(p + qj ) − 9,       Hj+1 ≤ (B/b)Hj .

All forward input exponents exceed one in a fixed neighborhood of p∗ . The larger root q∞ (p) of
q 2 + (9 − 15p)q + 9p = 0 is the limit of this increasing iteration there: Fp (9) > 9, Fp is increasing,
and Fp (q) > q between its two fixed points. Let 1/t∞ (p) = 1/p + 2/q∞ (p). Substitution gives
t∞ (p∗ ) = 3, and Fp′ ∗ (q∞ (p∗ )) = 16((p∗ − 3)/(p∗ + 3))2 < 1 (the prime denotes derivative in q).
After a fixed number of iterations the distances to the limiting root contract by a common factor
less than one throughout a sufficiently small closed neighborhood of p∗ . Indeed the root is smooth
and the finite iterates are continuous; first choose a contracting neighborhood and an iterate
entering its interior at p∗ , then shrink the parameter interval. Thus O(1 + log(1/δ)) iterations and
∥U ∥(1/p+2/qj )−1 ≤ BHj2 yield

                                 ∥U ∥t∞ (p)−δ ≤ Cδ −A       (0 < δ ≤ δ0 ).                        (G4)

                                                    7
All constants here are uniform on that interval. The simple attracting root has positive derivative in
p because ∂p Fp (q) > 0. It follows that t∞ is smooth and increasing, with 0 ≤ 3−t∞ (p) ≤ C0 (p∗ −p)
below p∗ .

A cut of prescribed rarity. We recall the sparse-input estimate derived from Polyanskiy and
Samorodnitsky, Theorem 7 and Remark 3. For 1 ≤ s ≤ L/32, m = s/L, and µ(supp f ) ≤ e−s it
gives
                            ∥Qf ∥2 ≤ ∥f ∥a ,   a = 3/2 − κm
for an absolute κ > 0. To see the uniform choice of exponents, use time (log 2)/2 and entropy
parameter ηm for sufficiently small fixed η > 0. The support bound gives log(∥f ∥a /∥f ∥1 ) ≥
(1 − 1/a)s. Their exponent ODE has rate at least 2 + cηm since the increasing rate function has
expansion 2 + x/3 + O(x2 ) at zero. The output exponent is at least 1 + 2(a − 1) exp(cηm(log 2)/2),
which reaches two when κ is sufficiently small. Absolute values cover signed inputs.
    Let t = t∞ (p)−dm and 1/at = 1/2+1/(2t). There are absolute constants (or constants uniform
on the chosen interval) d, c1 , c2 > 0 such that if p ≤ p∗ and p∗ − p ≤ c1 m, then 1/a − 1/at ≥ c2 m.
Indeed 1/a − 2/3 ≥ (4κ/9)m, whereas 1/at − 2/3 = (3 − t)/(6t) ≤ (C0 (p∗ − p) + dm)/(6t); shrink
d, c1 and keep t > 2. Also take dm ≤ δ0 . For z of unit L2 (µ) norm and µ(F ) ≤ e−s , two
applications of Hölder now give
                        √
                  ∥Q(1F U z)∥22 ≤ µ(F )2(1/a−1/at ) ∥U ∥t ≤ Cm−A exp(−2c2 s2 /L).

Squaring and the Gram identity are accounted for in the displayed squared norm. Taking the
supremum bounds the stationary    p killed norm ∥KF F ∥.
    Choose s = D[(p∗ − p)L + L log(2L)] with D large enough that p∗ − p ≤ c1 s/L and that
the exponential dominates C(L/s)A with product at most 1/2 for all sufficiently large L. Then
choose ϵ0 small enough that s ≤ L/32 for all such large L, uniformly for 0 ≤ p∗ − p ≤ ϵ0 . Equation
(G3) proves (G2) and its endpoint specialization (G1). For bounded dimensions (G3) and the
single-atom lower bound µ(E) ≥ 2−L cover the remaining cases.
    For fixed p > p∗ decrease p if necessary to an exponent strictly between p∗ and the upper end of
the same neighborhood. Then (G4) gives ∥U ∥t ≤ M for a fixed t > 3. Ordinary hypercontractivity
and the Gram identity give ∥KF F ∥ ≤ ∥U 1F ∥3 ≤ M µ(F )1/3−1/t . A fixed value of s thus suffices in
(G3), proving the dimension-independent claim.
    The constants on the upper side can also be tracked. For ε = p − p∗ > 0 sufficiently small
the smooth root has strictly positive derivative, so t∞ (p) ≥ 3 + c3 ε. Choose t = 3 + c3 ε/2 in
(G4), which gives ∥U ∥t ≤ Cε−A . Since 1/3 − 1/t ≥ c4 ε, the preceding small-cut test holds at
s = Dε−1 log(2/ε) for a fixed sufficiently large D. Independently, monotonicity of probability
norms makes (G1) applicable at this same p. Hence
                                              q
                          log(1/γ) ≤ C min{ L log(2L), ε−1 log(2/ε)}.

Relation to the matched examples. The published shell and its supercubic source extension
demonstrate exponential trapping at lower stationary exponents. Their existence does not identify
p∗ as the sharp transition. The present bound controls all cuts at p∗ without exact matching. The
small-cut estimate uses the programme’s endpoint multiplier argument. The large-cut estimate
uses the classical reverse Boolean inequality. Their combination yields a global relaxation bound
rather than a comparison limited to exceptional sets selected by matching. This result has been
checked analytically in the drafting context.

                                                  8
4    A single stationary spike at the cubic moment
Keep half noise and put Y = 1/g. Suppose π = a off a set E of uniform mass m > 0, and that

                           b ≤ a ≤ 1,         a ≤ π ≤ M,          M m1/3 ≤ H.                   (S1)

The constants b, H are fixed across dimensions. The shape of E and the variation of π inside this
envelope are arbitrary. Every two-valued stationary density with a positive floor and bounded
cubic norm satisfies (S1), taking its higher level for E. The constant density gives ordinary noise
by uniqueness of positive scaling.

Theorem. Under (S1) the spectral gap is at least c(b, H) > 0, without coordinate matching.
For a two-valued stationary density there are two stronger conclusions. The ordered spectral
error satisfies ∆ ≤ Cb ∥π − 1∥3 without matching, and its linear order is sharp. If p > 3 is fixed,
∥π∥p ≤ B, and the stationary marginals match through order k, then the ordered spectral error is
at most Ce−ck , with constants depending only on b, B, p.

Two-step averaging on the spike. The floor π ≥ a and Jensen give Y ≤ P g/a. Since
P g = P 2 (πY ), writing T = P 2 gives the pointwise inequality Y ≤ T Y + (M/a)T (Y 1E ). The
unweighted term has coefficient one. Iteration and positivity give, for j = 0, 1, 2,
                                                           n
                                                           X
                              P j Y ≤ P j T n Y + (M/a)          P j T i (Y 1E ).               (S2)
                                                           i=1

As before ∥Y ∥9 ≤ 1/b. Choose n = 1 + ⌈log16 (1 + log(1/m))⌉ and v = 1 + 8 · 16n . Forward
hypercontractivity gives ∥P j T n Y ∥v ≤ 1/b, so its L8 norm on E is at most m1/8−1/v /b ≤ em1/8 /b.
For i ≥ 1, P j T i contracts L23/16 into L8 : two ordinary noise steps have correlation 1/4. An input
supported on E gains a factor md relative to its L8 norm, with d = 16/23 − 1/8 > 1/3. For m
sufficiently small in terms of b, H, (M/a)nmd ≤ (H/b)nmd−1/3 ≤ 1/2. In (S2) with j = 0 absorb
this term, then apply the result for j = 1, 2. With µE = µ(· | E) this gives ∥P j Y ∥8,µE ≤ Cb .
    Now g = P (πY ) and P g = T (πY ). The spike contributes at most CM md to ∥P g∥8,µE by the
same two-step bound. For ∥g∥3,µE , use the L3/2 -to-L3 contraction of P on Y 1E and its conditional
L8 bound; this contribution is at most CM m1/3 . The baseline contributions are controlled by
(S2), using πY ≤ aY + M Y 1E . We obtain

                               ∥Y ∥8,µE + ∥g∥3,µE + ∥P g∥8,µE ≤ Cb,H .                          (S3)

All subsets of the spike. For nonempty F ⊆ E put θ = ν(F )/(M m) and r(F ) = J(F, F )/ν(F ).
Then EµE [1F π/M ] = θ. Forward hypercontractivity of Q from L3/2 to L2 and Hölder in µE give

          J(F, F ) = ∥Q(h1F )∥22 ≤ M 2 m4/3 ∥Y ∥28,µE ∥1F π/M ∥224/13,µE ≤ CM 2 m4/3 θ13/12 .

Thus r(F ) ≤ CHθ1/12 . If r(F ) ≥ 1/2, then θ ≥ c > 0. The density of ν(· | F ) relative to µE is at
most 1/c, so (S3) bounds its mean of g P g. Also EµE P 1E ≤ m1/3 by the same forward inequality
on the indicator. Hence Eν(·|F ) P 1F c ≥ 1/2, reducing the fixed threshold on m if necessary.
Pointwise Cauchy–Schwarz under Px and the floor give Kx (F c ) ≥ b[Px (F c )]2 /(g(x)P g(x)). A
second Cauchy–Schwarz under ν(· | F ) yields
                                              (Eν(·|F ) P 1F c )2
                              1 − r(F ) ≥ b                       ≥ cb,H > 0.
                                               Eν(·|F ) [g P g]

                                                     9
In the other branch the exit is already at least 1/2. The coarea estimate in (LR1), whose killed-chain
part uses only reversibility and positivity, gives ∥KEE ∥ ≤ 1 − c′b,H .

The global gap. For any cut D, the positive Gram multipliers for D ∩ E and D \ E add. On
E c , U = aY 2 has a bounded L9/2 norm. Thus

                      ∥KDD ∥ ≤ ∥KEE ∥ + ∥U 1D\E ∥3 ≤ 1 − c′b,H + Cb µ(D)1/9 .

All sufficiently small cuts have return bounded away from one, at a threshold independent of m, L.
Larger cuts of stationary mass at most one half obey (G3) at p = 3, as Eµ π 3 ≤ 1 + H 3 . If m
exceeds the smallness threshold used above, M is bounded in terms of b, H, and the L9/2 argument
applies on the whole cube. Cheeger’s inequality proves the global gap in both cases.

Full recovery for two stationary values. Now π = M on E. In the small-m regime (S3) gives
∥U 1E ∥3 ≤ CM m1/3 . Write δ = ∥π − 1∥3 . We prove the quantitative bound ∆ ≤ Cb δ. As ∆ ≤ 1, it
suffices to take δ small in terms of b. With u = Eh and V = 1 − u2 = ∥Qh
                                                                       √ − u∥22 , Cauchy–Schwarz
                                                                                            √
gives √1 = (Ehg)2 ≤ uE(hg 2 ) = uE(πg). Subtracting u2 gives V ≤ uδ V since ∥g − u∥2 ≤ V .
Thus V ≤ δ and 1 − u ≤ δ 2 . Applying forward hypercontractivity to Qh − u yields ∥g − u∥3 ≤ δ
and ∥P g − u∥9 ≤ δ. On {g ≥ b/2} the inverse square is Lipschitz in g. On A = {g < b/2}, Jensen
gives P g ≥ b/g > 2, so Y ≤ 2(P g − u)/b there and µ(A) ≤ δ 9 . Consequently

                                       ∥Y 2 − 1∥3 ≤ Cb (δ + δ 2 + δ 3 ).

If M ≤ 2, multiplication by π now gives ∥U −π∥3 ≤ Cb δ. If M > 2, then M m1/3 ≤ 2(M −1)m1/3 ≤
2δ. Hence m ≤ δ 3 , and for sufficiently small δ we may use (S3) with H = 2. On E both ∥U 1E ∥3
and ∥π1E ∥3 are Ob (δ), and off E we have π = a ≤ 1. In both cases ∥U − 1∥3 ≤ Cb δ. The Gram
comparison ∆ ≤ ∥QMU −1 Q∥ ≤ ∥U − 1∥3 finishes the upper bound.
    The linear order is sharp. pIn dimension two let χ = χ1 χ2 be the parity character. For
0 < t < 1 take h = (1 + tχ)/ 1 + t2 /4. Then π = 1 + ϵχ, √       with ϵ = (5t/4)/(1 + t2 /4), and
U = (1+tχ)/(1+tχ/4). On the span of χ1 , χ2 , Q multiplies by 1/ 2 and MU has eigenvector χ1 +χ2
with eigenvalue (1 + t)/(1 + t/4). Thus QMU Q has a nonleading eigenvalue (1 + t)/(2(1 + t/4)) < 1.
As the ordinary second eigenvalue is 1/2,

                                          ∆                3t        3
                             lim inf            ≥ lim              =    .
                               t↓0     ∥π − 1∥3    t↓0 8(1 + t/4)ϵ   10

The example obeys every fixed floor b < 1 for sufficiently small t.

Visibility in stationary moment measurements. The same example shows a loss of one
order when a spectral edge is read from a single coordinate. In the stationary inner product define
Cj (i, ℓ) = ⟨χi , K j χℓ ⟩ν , i, ℓ = 1, 2. These are population lag moments. The coordinates are centered
by symmetry. The functions χ1 ± χ2 are orthogonal (their supports are disjoint), with squared
norms 2(1 ± ϵ). Directly applying K on their supports gives eigenvalues λ± = (1 ± t)/(2(1 ± t/4)).
Consequently

          Cj (1, 1) = 12 [(1 + ϵ)λj+ + (1 − ϵ)λj− ],        Cj (1, 2) = 21 [(1 + ϵ)λj+ − (1 − ϵ)λj− ].

The diagonal differs from 2−j by O(t2 ) uniformly over every integer j ≥ 0. Indeed the expression
is even, and its second derivative is uniformly bounded on |t| ≤ 1/4: each eigenvalue lies in

                                                       10
a compact subinterval of (0, 1), and the polynomial factors in j from two differentiations are
dominated by geometric decay. The order is attained at lag one, where expansion gives C1 (1, 1) =
1/2 + 3t2 /8 + O(t4 ). In contrast the two-channel population pencil (C1 , C0 ) gives λ± exactly,
since its two common directions have quotients λ± . The ordinary second eigenvalue moves by
at least a constant times t. Thus even the entire single-coordinate autocorrelation sequence in
absolute sup norm cannot yield a locally Lipschitz estimate of the spectral edge on this family.
A two-channel pencil resolves the splitting with bounded conditioning as t → 0 since C0 has
eigenvalues 1 ± ϵ. This compares population observables, with no sampling model assumed. It
connects to the programme’s two-channel spectral moment certificates, which use a different
covariance and sampling model.

Matching above the cubic order. For the exponential estimate let D = {|g − 1| > 2−k/8 }.
The matching-energy argument gives µ(D) ≤ CB 2−3k/4 . On Dc , ∥(U − π)1Dc ∥3 ≤ CB 2−k/8 for
large k. If m ≤ e−αk , then M m1/3 ≤ Bm1/3−1/p is exponentially small, and the L9/2 bound on
E c handles D \ E. If m > e−αk then M ≤ Beαk/p and ∥(U − π)1D ∥3 ≤ Cb M µ(D)1/9 . Choose
0 < α < p log(2)/12. Both bounds decay exponentially; bounded k is covered by contraction.
Finally QMπ−1 Q is exponentially small by the matched low/high split for p > 3.

Scope. The stationary-moment manuscript treats a two-level potential. Here the two values
belong to hP h; the reconstructed h may take many values. The published shell shows why cubic
convergence alone cannot yield this conclusion for an unrestricted stationary law. The argument
for the gap permits multiple heights on the exceptional set under (S1) and controls each of its
subsets. The unrestricted stationary endpoint remains open.


5    Several exceptional stationary levels
Let E1 , . . . , EN be disjoint nonempty subsets of the cube, mi = µ(Ei ) and m = maxi mi . Assume
π = a off their union, b ≤ a ≤ 1, and a ≤ π ≤ Mi on Ei . Fix N, b, H, κ independently of dimension,
with b > 0, and assume
                                1/3                                       √
                           Mi mi ≤ H,       m i ≥ mκ ,     1 ≤ κ < 21 − 8 5.                   (F1)

The restriction compares logarithms of uniform masses. The mass and height ratios may diverge.
The sets have arbitrary geometry.

Theorem. Under (F1) the spectral gap is bounded below by a positive constant depending
only on N, b, H, κ. If π is constant on each Ei , then ∆ ≤ CN,b,κ ∥π − 1∥3 without coordinate
matching. For arbitrary allowed heights, cubic convergence gives full recovery, and uniform
integrability of the cubed densities suffices under diverging matching order. With a fixed p > 3
and ∥π∥p ≤ B, matching through order k instead gives ∆ ≤ Ce−ck with constants depending only
on N, b, H, κ, p, B; for exact levels one may take H = B.
                                                                                            −1/3
    For example, take disjoint sets of masses 2−n and 2−2n in dimension 2n for n ≥ 2. Add mi
                                                           P 2/3
to a common background on each set, choosing a = 1 − i mi for normalization. For large n
the floor exceeds 1/2 and the cubic moment stays bounded. Both sets together violate any fixed
single-spike envelope (S1): the maximum times their combined mass to the power 1/3 grows at
least as 2n/3 . Here (F1) applies with κ = 2.


                                                11
                                                      √
Control between different levels. Set r = 12 5 − 15 > 9, s = (r√+ 15)/16, T = P 2 , and
η = 1/s − 1/3 − κ/r. Then η > 0 because r(16/(r + 15) − 1/3) = 21 − 8 5. Differentiation shows
this choice maximizes the right side over r > 6; this is a limit of the estimate, not a necessary
restriction for a gap. For every ℓ ≥ 1, j ≥ 0, P j T ℓ contracts Ls into Lr . Let Z = maxi ∥Y ∥r,µi ,
Y = 1/g, µi = µ(· | Ei ). The contribution from an individual level to any other satisfies
                                                          1/s
                         Mi ∥P j T ℓ (Y 1Ei )∥r,µv ≤ Mi mi m−1/r
                                                            v    Z ≤ Hmη Z.                      (F2)

By Jensen Y ≤ P g/a, hence Y ≤ T Y + a−1 i Mi T (Y 1Ei ). Iterate n = 1 + ⌈log16 (1 +
                                                      P
                                                                                n
log(1/ mini mi ))⌉ times as in (S2). The unrestricted term P j T n Y has L1+8·16 norm at most 1/b, so
its conditional Lr norm on each level is at most e/b. By (F2), Z ≤ e/b+(nN H/b)mη Z. For all suffi-
ciently small m, n = Oκ (1 + log(1 + log(1/m))) and the coefficient is at most 1/2. Applying the iter-
ated bound also with j = 2 controls T Y on every level. Since P g = T (πY ) ≤ aT Y + i Mi T (Y 1Ei ),
                                                                                     P

we have                                                     
                                    max ∥Y ∥r,µi + ∥P g∥r,µi ≤ C.                               (F3)
                                    i

The conditional estimate does not require pointwise control on g. When m is bounded below, all
the Mi are bounded by (F1) and we use the ambient ∥Y ∥9 ≤ 1/b instead.

Cut escape, including transitions between levels. We prove the uniform gap by contra-
diction along a sequence. If m is bounded below, (G3) and the global L9/2 bound on U = πY 2
give the gap as in the one-spike proof. Pass therefore to m → 0. Extract a subsequence along
which every ratio mi /mj has a limit in [0, ∞]. Group indices with finite nonzero limiting ratio.
Each group C denotes the union of its levels, with mass mC and height bound MC = maxi∈C Mi
                                                                            1/3
(indices in this maximum refer to the group). Along this subsequence MC mC ≤ HC < ∞, and
(F3) holds also under µC = µ(· | C).
    For ∅ ̸= F ⊂ C write vF = ν(F ), θF = vF /(MC mC ) and RF = J(F, F )/vF . As in (S3) and
its cut estimate, using ∥Y ∥8,µC ≤ C gives
                                                      1/3 1/12
                                        RF ≤ CMC mC θF                .
                                                                1/3
Thus if RF stays bounded below then θF and MC mC both stay bounded below, and vF is
                  2/3
comparable to mC . Moreover ν(· | F ) has density at most 1/θF relative to µC . Under this
conditional stationary law, the expectations of P g and P (h1F ) are uniformly bounded: for the
latter,
                                          −1/3                        1/3
                       ∥P (h1F )∥3,µC ≤ mC MC ∥Y 1C ∥3/2 ≤ CMC mC .
                   1/3
Also EµC P 1C ≤ mC by ordinary hypercontractivity. Consequently, for a fixed sufficiently large
A and all large dimensions, at least half the conditional stationary mass has P g ≤ A, P (h1F ) ≤ A
and P 1F c ≥ 1/2, by Markov’s inequality. On those vertices if g > 2A, then Kx (F ) ≤ 1/2.
Otherwise the row escape bound from (S3) and its proof gives Kx (F c ) ≥ b/(8A2 ). Hence RF stays
bounded away from one.
    If the union admitted cuts F with RF → 1, split them into FC = F ∩ C. Pass to limits of their
diagonal return fractions RFC , taking zero for empty pieces. The positive semidefinite edge form
gives
                                  p        Xq
                                    RF ≤         RFC ν(FC )/ν(F ).
                                            C



                                                 12
Groups with vanishing diagonal return contribute o(1). Of those with positive limiting return,
the one with the largest mass dominates all the others: their cut masses are comparable to their
              2/3
respective mC , and distinct groups have mass ratios tending to zero or infinity. The dominant
summand stays bounded away from one by the preceding row argument. This contradicts RF → 1
(if there are no such groups the sum tends to zero). The killed norm on the union is therefore
bounded away from one along the extracted subsequence by (LR1). Off the union, ∥U ∥9/2 restricted
there is at most 1/b2 . Adding Gram multipliers as in the one-spike proof controls all small cuts.
Larger cuts obey (G3) since Eπ 3 ≤ 1 + N H 3 . Cheeger’s inequality now precludes a sequence with
gap tending to zero.

Full spectral estimates. For exact levels take Mi = π|Ei . Put δ = ∥π − 1∥3 . For the
Lipschitz estimate it suffices to take δ ≤ 1, when H = 2 works. Away from levels above two,
                                                                                    1/3
the preceding section proved ∥π(Y 2 − 1)1{π≤2} ∥3 ≤ Cb δ. On each higher level, Mi mi ≤ 2δ;
                             1/3
(F3) gives ∥U 1Ei ∥3 ≤ CMi mi . If m is bounded below the same conditional L6 control follows
from ∥Y ∥9 ≤ 1/b and (F1). Sum the finitely many contributions and use the Gram inequality
∆ ≤ ∥U − 1∥3 . The parity example in the previous section retains sharpness of the linear order for
the full class.

Variable heights within levels. The gap statement allowed variable heights from the outset.
The same hypotheses yield a quantitative transfer for the entire spectrum even when constant
heights are unavailable. Put α = 1 − 6/r > 0. For any set D in the small-m regime, conditional
Hölder on Ei with 1/u = 1/3 − 2/r and (F3) give
                                     1/3                     1/3
                  ∥U 1Ei ∩D ∥3 ≤ Cmi ∥π1D ∥u,µi ≤ C(Mi mi )1−α ∥π1Ei ∩D ∥α3 .

Here 3/u = α. Off the exceptional union use the ambient L9/2 bound. When m stays above the
absorption threshold, the same ambient bound holds everywhere. For either regime,

                             ∥U 1D ∥3 ≤ CN,b,H,κ ∥π1D ∥α3 + µ(D)1/9 .
                                                                    
                                                                                              (F4)

In particular full recovery without matching holds if δ = ∥π − 1∥3 → 0. For a rate on {π > 2},
in the small-m regime use the preceding levelwise inequality there (the background is at most
one) and π ≤ 2|π − 1|. On {π ≤ 2} use the inverse estimate from the one-spike section. In the
remaining, bounded-height regime use that inverse estimate globally. This gives ∆ ≤ C(δ + δ α ).
    There is also a matched result at the cubic order: uniform integrability of π 3 under µ and
k → ∞ imply full spectral recovery for variable heights satisfying (F1). Indeed (F4) transfers that
uniform integrability to U 3 . The matched bad set D = {|g − 1| > 2−k/8 } has exponentially small
mass since the cubic cap implies a bounded second moment. The L3 norm of U − π on D therefore
tends to zero; outside D it is exponentially small. To bound QMπ−1 Q at order three let A project
onto Walsh degrees at most ⌊k/2⌋. The low-low block vanishes by matching of products. In each
remaining block at least one high factor Q(I − A) has L2 operator norm at most 2−k/4 . Truncate
π − 1 at a fixed height T > 1, keeping its values on {π ≤ T }. The bounded part in each such block
costs at most (T + 1)2−k/4 , and the tail costs at most ∥π1{π>T } ∥3 by Q : L2 → L3 and the L2
contractions A, I − A before Q. Take first the limit in k, then in T . Min–max proves the claim.
For p > 3 and ∥π∥p ≤ B, the same proof is exponential: in (F4) use ∥π1D ∥3 ≤ Bµ(D)1/3−1/p ,
and take T = 2k/8 in the spectral blocks, whose tail is at most B p/3 T 1−p/3 . No bound on the
within-level oscillation is needed.


                                                13
   The published trapping family has a fixed floor and converges in cubic norm. This theorem
implies that it admits no representation satisfying (F1) with uniform parameters. The theorem
uses ordinary Boolean hypercontractivity; Polyanskiy and Samorodnitsky give stronger estimates
on small supports. Whether such an improvement removes the logarithmic mass comparison is
open here.


6    Three stationary values suffice for exponential trapping
The rarity comparison in (F1) cannot be discarded, even for exact levels. For every κ > 64/9 and
every fixed floor 0 < b < 1 there are a fixed p > 3, σ > 0 and arbitrarily large dimensions with
exactly three stationary density values such that

                       π ≥ b,      ∥π − 1∥p ≤ e−σL ,      1 − λ2 (K) ≤ e−σL .                    (T1)

All one-coordinate stationary marginals are uniform. The two exceptional levels have uniform
masses mS < mC with mS ≥ mκC . Together with (S1), this identifies three as the smallest number
of stationary values allowing loss of the uniform gap under a fixed floor and bounded cubic moment.
The assertions about the number of levels do not impose higher-order marginal matching.

Ordinary shell probabilities. Write z(x) = L−1 xi and I(t) = ((1 + t) log(1 + t) + (1 −
                                                         P

t) log(1 − t))/2. For attainable t > 0, µ{|z| = t} = exp[−LI(t) + O(log L)] and I(t) = t2 /2 + O(t4 ).
From z(x) = s, one half-noise step has magnetization mean s/2. For |t|, |s| = O(d) write w = t−s/2.
The probability of landing at the exact attainable t is between

              exp[−L(2w2 /3 + O(d3 )) − O(log L)] and        exp[−L(2w2 /3 − O(d3 ))].           (T2)

For the lower bound the two groups of input signs have output-plus probabilities 3/4 and 1/4.
Raise each by w/2 (a negative shift is allowed). Round the first group’s output count to an integer
and choose the second to give exactly the prescribed total. Each group has size comparable to L.
Stirling’s bounds for both binomial terms give the two relative entropies with O(log L) error. Each
divergence is 2w2 /3 + O(d3 ) by Taylor expansion. For the upper bound, the centered log moment
generating function per output sign is 3v 2 /8 + O(|v|3 ) for a tilt v of either sign; use v = 4w/3.
The constants are uniform for the shell locations used below.

Two prescribed exceptional densities. Choose rational u < 3/8 sufficiently close to 3/8 that
u−2 < κ. Choose k0 strictly between
                              2
                   2
                   3 (u − 1/4)    and   min{ 23 (1/2 − u)2 , u2 /12, (u − 1/8)2 /2}.             (T3)

Such an interval exists: at 3/8 the first two square-distance rates coincide, the other two upper
bounds are strictly larger, and moving u to the left separates the first two rates. Choose a fixed
ω > 0 small enough that 23 (u − 1/4 + ω/2)2 < k0 and ω < 1/2 − u. Choose e > 0 so small that
each of the gaps in (T3), the new gap after adding ω/2, the number ω 2 /2, and (7/8)2 /2 − 1/6
exceeds 10e. Take 0 < γ < min(e, 1/32). Finally take rational d > 0 sufficiently small that all
strict inequalities below survive the O(d3 ) errors in (T2). Take L along multiples making both
positive shells attainable. Set

                 S = {|z| = d},      C = {|z| = ud},       B = { ||z| − d/2| ≤ ωd }.


                                                 14
For x ∈ S, q = Px (S) is independent of x. By (T2) and Hoeffding’s bound,
                                     2      3                               2
                                e−(d /6+O(d ))L−O(log L) ≤ q ≤ 2e−d L/8 .

Prescribe the density itself by
           2                    2                                                          1 − mC MC − mS MS
MC = ek0 d L ,      MS = e−γd L /q,         π = MC 1C +MS 1S +a1(S∪C)c ,              a=                     .
                                                                                              1 − mC − mS
                          1/3                                                                         1/3
Since k0 < u2 /12, MC mC decays exponentially. The corresponding exponent for MS mS is at
most −γd2 + O(d3 ), also strictly negative. Thus a → 1 and the cubic distance decays exponentially.
The same strict inequalities hold with 1/p in place of 1/3 for some fixed p > 3 near three. The
upper bound on q ensures MS > MC > 1 eventually. Sign reversal gives exact one-coordinate
marginals. The limit of log mS / log mC is I(d)/I(ud), which tends to u−2 as d ↓ 0, so (after fixing
sufficiently small d) mS ≥ mκC eventually.

Recovering the potential from the prescribed law. The unique positive solution hP h = π
follows by strict convexity and coercivity of the finite symmetric scaling functional in log coordinates
(as in the published shell proof). Permutations and global sign reversal preserve this solution. In
particular h, g = P h are constant on each of S, C, denoted by subscripts. Put δ2 = ∥π − 1∥2 . The
variance proof in the one-spike section uses only the stationary second norm of the perturbation
                                                    √          √                             1/3
and yields ∥g − 1∥3 ≤ δ2 + δ22 . Here δ2 = O(MC mC + MS mS ). After division by mC the two
exponential rates are bounded above by k0 d2 − I(ud)/6 and d2 /6 + O(d3 ) − I(d)/2 + I(ud)/3, both
strictly negative for small pd. Therefore gC = 1 + o(1) and hC = (1 + o(1))MC . On S positivity
and gS ≥ qhS imply hS ≤ MS /q ≤ 1/q.
    For y ∈ B, the lower bound (T2) aimed at the appropriately signed component of C gives
Py (C) ≥ exp[−( 23 (u − 1/4 + ω/2)2 d2 + O(d3 ))L − O(log L)]. Since g(y) ≥ hC Py (C) and π(y) = a,
for large L,
                                                           2
                                           sup h ≤ e−4ed L .                                        (T4)
                                                B
This depression in the potential is a consequence of the two prescribed high stationary values.

Escape from the rarer level. For x ∈ S let D = Px (h1S c ). The smallness of h on B alone
would not control atypical transitions. To bound them set T = P 2 , Y = 1/g. The floor a gives
Y ≤ P g/a = T h/a by Jensen. Because h = aY off the exceptional levels,

                                    Y ≤ T Y + a−1 (hC T 1C + hS T 1S ).

Iterate n = 1 + ⌈log16 (1 + L)⌉ times. The ambient bound ∥Y ∥9 ≤ 1/a and hypercontractivity give
                       n
∥T n Y ∥∞ ≤ 2L/(1+8·16 ) /a ≤ 2/a. Bounding separately the landing regions C, B, and ordinary
background outside B, and using positivity in the iterated terms, gives the explicit estimate
                                                             n
                                                             X
                                                    c
                                                                   hC Px2i+1 (C) + hS Px2i+1 (S) .
                                                                                               
                 D ≤ hC Px (C) + sup h + 2Px (B ) +                                                         (T5)
                                    B                        i=1

The one-step term for C decays with exponent at least ( 23 (1/2 − u)2 − k0 )d2 − O(d3 ) by (T2),
                                                                                          2 2
including the more distant opposite-sign component. The third term costs at most 4e−ω d L/2 .
For every odd step 2i + 1 ≥ 3 the signs are independent given x, with magnetization mean of
                                                                                      2 2
magnitude at most d/8. Hoeffding bounds the two probabilities in the sum by 2e−(u−1/8) d L/2 and

                                                        15
       2 2
2e−(7/8) d L/2 respectively. Multiplication by hC ∼ MC and hS ≤ 1/q preserves strict exponential
                                                                   2
decay. With the chosen slack and n = O(log L), (T5) gives√D ≤ e−ed L .
                                                                       2
    Finally gS = qhS + D and gS hS = MS imply gS ≥ qMS = e−γd L/2 . Hence Kx (S c ) =
                   2
D/gS ≤ e−(e−γ/2)d L on the whole shell. The centered shell indicator in the Rayleigh quotient
gives 1 − λ2 (K) ≤ Kx (S c )/(1 − MS mS ), proving (T1).

Exact matching and the number of approximate levels. There is a corresponding obstruc-
tion with exact matching through a positive fraction of the coordinates. Let π0 be the three-valued
law just constructed. For sufficiently small fixed β > 0, subtract from π0 its nonconstant Walsh
coefficients of orders at most ⌊βL⌋ to obtain π1 . Each coefficient is bounded by ∥π0 − 1∥1 , and
their number is at most eLH(β) , where H is binary entropy in natural units. By (T1) we can
choose H(β) < σ/2. Thus π1 is exactly matched, normalized, and ∥π1 − π0 ∥∞ ≤ e−σL/2 . Its floor
tends to one and its supercubic norm distance still tends exponentially to zero.
    For completeness, let two normalized densities v0 , v1 have floor b0 > 0 and logarithmic
distance ϵ = ∥ log(v1 /v0 )∥∞ ≤ 1. Along their straight-line interpolation, ∥v̇t /vt ∥∞ ≤ eϵ − 1 ≤
2ϵ. Logarithmic differentiation of ht P ht = vt gives (I + Kt ) ∂t log ht = v̇t /vt . The operator
At = (I − Kt )/2 has absolute row sums at most one. Positivity of the noise quadratic form
gives stationary L2 norm at  √ most 1/2. Since the smallest stationary mass is at least b0 2−L ,
   j
∥At ∥∞→∞ ≤ min(1, 2L/2−j / b0 ). The inverse is 12 j≥0 Ajt , so ∥ log(h1 /h0 )∥∞ ≤ Cb0 (L + 1)ϵ. In
                                                    P

particular every stationary edge weight changes by a factor between e−2Cb0 (L+1)ϵ and e2Cb0 (L+1)ϵ ,
and every variance, written as an infimum over constant centerings, changes by a factor between
e−ϵ and eϵ . Taking Dirichlet quotients gives

                                       gap(K1 )
                                 log            ≤ 2Cb0 (L + 1)ϵ + ϵ.                            (T6)
                                       gap(K0 )

Applied to the projected law this preserves the exponential gap upper bound. The three exact
levels refer to the reference law; the matched law lies exponentially close to those levels.
    Conversely, suppose a density is within o(1) in log sup norm of a normalized two-valued
reference with uniform floor and bounded cubic norm. The one-spike theorem and (T6) imply
log(1/ gap(K)) = o(L); distance O(1/L) gives a uniform positive gap. Thus an exponential trap
with a fixed positive rate is impossible even at vanishing logarithmic distance from two such levels,
whereas exponentially accurate three-level approximation already allows it under linear-order
matching. The unrestricted sufficient stationary exponent is unchanged by this construction.

Consequences and comparison.
                          √          For the two-exceptional-level cubic gap problem, (F1) proves
sufficiency for κ < 21 − 8 5. Equation (T1) excludes uniform sufficiency for every κ > 64/9.
Neither endpoint is decided. The earlier shell started with several potential bands and then
corrected the stationary marginals through linear order. Here the stationary law has precisely
three values by construction; the reciprocal estimate (T5) controls its reconstructed transition
rows. Ordinary Hamming sphere noise estimates are studied, for example, by Kirshner and
Samorodnitsky. The present argument does not decide the unrestricted matched endpoint.


7    Fractional basis packing and a direct inverse moment
Use the notation of the rank paper, with P = P1/2 , Q = P1/√2 , g = P h, π = hg, Eπ = 1 and
U = h/g. Let A have full row rank and let π be a function of Ax. By uniqueness of positive


                                                  16
symmetric scaling, h and g are functions of Ax as well. A fractional packing of weight t assigns
weights wJ ≥ 0 to column bases J of A, with J wJ = t and J∋i wJ ≤ 1 for each input column
                                             P              P

i. Repeated columns have separate capacities.
    Suppose ∥π∥p ≤ B for fixed 2 ≤ p < ∞, and the stationary marginals match the uniform law
through degree k. If t is fixed and

                                        1     2  2t − 1
                                          + t   < t     ,                                         (P1)
                                        p 4 −1   2 +1

then the entire ordered spectrum differs from that of P by at most CB,p,t e−cp,t k , with cp,t > 0.
No stationary√minimum uniform in dimension is assumed. In particular, at p = 2 it suffices that
t > log2 (2 + 5), so three disjoint full bases suffice. At t = 2 it suffices that p > 15/7, which
includes the programme’s stationary moment endpoint. The strict boundary in (P1) is not decided.

Allocating noise time. On the quotient, the noise contributed by column i acts by retaining
or translating by that column. Its multipliers are 1 and λ. Thus two factors in the same column
multiply their correlations. Allocate a factor of correlation λwJ in each column of J to basis J,
omitting zero weights. The unused capacity is another commuting noise factor. Each basis acts as
ordinary product noise on the entire quotient in its own coordinates. Successive applications of
forward hypercontractivity give contraction from a > 1 to 1 + (a − 1)λ−2t . For a positive input and
0 < a < 1, reverse hypercontractivity gives the lower bound from a to 1 − (1 − a)λ−2t , including
negative target orders. This follows by using the successive equality exponents of the classical
inequalities. If an intermediate order vanishes, use the geometric mean by continuity; all functions
are strictly positive on the finite quotient. Leftover noise contracts forward norms and increases
the generalized reverse norm by Jensen. These steps use the usual time convention for Boolean
noise (Bonami and Mossel, Oleszkiewicz and Sen, Remark 1.13). Fractional base packing itself is
classical, for example Dynamic Matroids, Base Packing and Covering.

Start with the potential. The normalization ∥Qh∥2 = 1 implies ∥g∥2 ≤ 1. Since Eπ = 1
and ∥π∥2 ≤ B, Cauchy–Schwarz gives µ{π ≥ 1/2} ≥ 1/(4B 2 ). Also µ{g > 4B} ≤ 1/(16B 2 ). On
an intersection of measure at least 3/(16B 2 ), we thus have h = π/g ≥ 1/(8B). For every fixed
a > 0, this bounds ∥h∥a from below solely in terms of a, B. In particular, for 0 < q < 4t − 1, use
a = 1 − (1 + q)4−t and the reverse estimate on P h, directly, to obtain ∥g −1 ∥q ≤ CB,t,q . This spends
the full noise time on the potential and requires neither a floor on π nor matching in this step.

Ambient operator comparison. Choose q < 4t − 1 and s > 1 so that

                                        1 2 1 2t − 1
                                         + < < t     .
                                        p q s 2 +1

Then U = π/g 2 is uniformly bounded in Lv for 1/v = 1/p + 2/q < 1/s. For any nonnegative
nonzero quotient weight W , the unique positive unit leading eigenvector of QMW Q is invariant
under all translations in ker A. Forward hypercontractivity on this vector, with 2s/(s − 1) < 1 + 2t ,
bounds ∥QMW Q∥ ≤ ∥W ∥s on the full cube. Zero weights satisfy the same bound.
   The matching-energy estimate of the rank paper gives ∥g − 1∥2 ≤ CB 2−k/2 . On Ek = {|g − 1| >
2−k/8 } the measure is at most CB 2−3k/4 . Hölder bounds ∥(U − π)1Ek ∥s by a constant times
µ(Ek )1/s−1/v . Outside Ek , |U − π| ≤ C2−k/8 π for large k. The multiplier bound applied to |U − π|
therefore gives exponential decay of ∥QMU −π Q∥.

                                                  17
                                                 √                           √
    By the strict inequality for 1/p, take
                                       √   λ > 1/ 2 sufficiently close to 1/ 2 that 2p/(p − 1) ≤
1 + λ−2t ; take λ < 1. Set θ = 1/( 2λ) < 1. The same positive multiplier argument gives
∥Pλ M|π−1| Pλ ∥ ≤ B + 1, hence the same bound for its signed counterpart. In Q = Pλ Pθ split the Pθ
factors at degree j = ⌊k/2⌋. The low-low term against π − 1 is zero by matching; the other three
terms each have norm at most (B + 1)θj+1 . Thus ∥QMU Q − P ∥ decays exponentially. The two
Gram products of M√U Q identify the spectrum of the first operator with that of the stationary
Doob chain. The claimed comparison follows by min–max. For p = 2, writing u = 2t , (P1) reduces
to u2 − 4u − 1 > 0. For t = 2 it reduces to 1/p < 7/15.

Separation from the four-family rank estimate. In each of n ≥ 2 independent rank-two
blocks use five columns of types (1, 0), (0, 1), (1, 1) with multiplicities 2, 2, 1. Assign total weights
3/2, 1/2, 1/2 to the three distinct pairs of types in the order (1, 2), (1, 3), (2, 3), spreading each
uniformly over the available copies. Each column uses exactly its unit capacity. Normalize the
block weights to probabilities, take their product across blocks, and multiply by 5/2. This is a
fractional packing of global bases of weight 5/2. The coordinate count 5n and the basis size 2n
also give the matching upper bound. The full code forces the four-family rank defect to be at least
⌈2n − 5n/4⌉ by the support formula of the rank paper.
    For an explicit matched law, choose z in the code nonzero in every block and a basis e1 , . . . , e2n
consisting of words supported on single blocks. Take 0 < ϵn < 1 tending to zero and set
                                                     2n
                                                                    !
                                        1 − ϵn      X
                                  π =1−        χz +     χz+ei .
                                        2n + 1      i=1

Every nonzero word in one block weighs at least three. All displayed characters therefore have
degree at least 3(n − 1). They are distinct, their differences span the code, and π has mean one and
takes values between ϵn and two, attaining the lower bound at the origin. Finite positive symmetric
scaling realizes this law. Taking k = 3n − 4 makes the old four-family bound vacuous, whereas (P1)
gives exponential recovery at p = 2. The example separates the two sufficient estimates on the
intrinsic code. It makes no exclusivity claim about all other stability methods. The unrestricted
endpoint without quotient information remains open.


Model assessments and review context
Codex assisted with the mathematical derivation, comparison with primary sources, and source
checks in the programme’s research chat. This supplement uses the previously constructed shell
as an explicit input to the interpolation argument. Its typeset version awaits a first exact-PDF
assessment. No numerical score or independent referee report has been obtained for this supplement.




                                                   18
