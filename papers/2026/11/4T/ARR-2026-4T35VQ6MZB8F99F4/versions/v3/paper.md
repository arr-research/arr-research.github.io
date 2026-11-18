         Moment transfer and spectral bounds
                  for Boolean Doob kernels
                                      Lluis Eriksson

                        17 November 2026. Revision candidate


                                          Abstract
    For positive potentials on a Boolean cube, the stationary density of the noise Doob ker-
nel and its normalized weighting density are different nonlinear functions of the potential.
We give an admissible family for which the stationary critical moment is below two while
the weighting critical moment is above two, despite a fixed positive stationary floor and ex-
act marginals through order proportional to the square root of the dimension. This refutes
transfer of that numerical cap, not the existence of a larger uniform bound. A nonlinear
consequence of the stationary floor, combined with classical ordinary and reverse hypercon-
tractivity, gives explicit inverse-potential moments and weighting-moment bounds below a
computable finite threshold. Exact stationary matching then gives strong convergence of the
two densities throughout this subcritical range. The finite bootstrap crosses the exponent
needed for a dimension-free low-to-all operator bound. We obtain exponentially small error
on degrees up to a fixed positive fraction of the stationary matching order. Non-Perron modes
a fixed positive distance above the noise edge must concentrate on actual high-weighting sets
of exponentially small stationary probability. A tensor example rules out an unrestricted
high-degree hypercontractive repair; the high block for arbitrary potentials remains uncon-
trolled. For potentials supported on a binary linear-code Fourier algebra, we control every
invariant sector of the full Doob kernel. Under a distance–cardinality condition its gap tends
uniformly to the unweighted gap, for every positive quotient potential. Direct disjoint-block
estimates cover a sharper parameter regime. A standard simplex code supplies positive poten-
tials outside the disjoint-block class. Classical random linear coding extends this mechanism
to positive-rate families at every sufficiently large length, with an explicit exponential gap
estimate and normalized witnesses meeting any fixed stationary floor below one and the mo-
ment cap. Without marginal matching, the same stationary floor and critical cap also imply a
dimension-free weak Poincare inequality and polynomial variance decay for bounded observ-
ables of the actual chain. At noise one half, an additional smoothing step gives the summable
decay exponent 8/7 and a dimension-free O(N −1 ) mean-square bound for sample averages,
including uniform initialization. These bounded-observable results do not imply a full L2 gap.
For arbitrary-valued positive potentials with a fixed positive minimum after energy normal-
ization, the critical cap yields an explicit dimension-uniform full-chain gap, without matching
or an upper bound on the potential. The original stationary floor supplies the required mini-
mum for every two-level potential, recovering a full-gap class theorem. Any normalized family
with collapsing gaps and the fixed critical cap must have potential minima tending to zero. A
rare-set construction followed by exact Fourier correction and stable symmetric scaling shows
that even all original stationary hypotheses do not force a positive normalized minimum. A
critical hypercontractive sandwich and the proved stability of the reconstruction show that
this same family has actual gap converging exponentially to the unweighted gap. A different
exactly matched family has a noise denominator tending to zero and an unbounded pointwise
potential-to-denominator ratio, yet its entire spectrum converges exponentially to Boolean
noise. Thus neither a positive denominator floor nor a pointwise ratio ceiling follows from


                                              1
     the stationary assumptions. Noise smoothing of the actual potential preserves the station-
     ary floor, but a four-point construction shows that every nontrivial smoothing can destroy
     exact stationary matching even while the critical cap survives. Smoothing the stationary
     density itself preserves the admissible constraints. For sufficiently strong fixed smoothing, a
     derived higher moment and finite inverse-moment crossing give uniform convergence of the
     reconstructed chain’s entire spectrum to Boolean noise, exponentially in the matching degree.
     Fixed smoothing need not be a vanishing critical-norm perturbation of the original density.
     An exactly matched block-spike family disproves uniform stationary-variance upper compar-
     ison and two-sided Dirichlet-form equivalence between the original and regularized chains.
     Both full gaps in this family nevertheless tend to the noise gap. Direct spectral comparison
     with the original chain remains unresolved. The general stationary-gap question and critical
     weighting-moment bound remain open.


1    Setting and theorem map
Let µ be uniform probability on {−1, 1}L , L ≥ 1, and let 0 < ρ < 1 be fixed. Boolean prod-
uct noise is denoted by P = Pρ , with Pρ χS = ρ|S| χS for Walsh characters χS . Unqualified
expectations and norms use µ. For h > 0 set

                g = P h,    Z = Ehg,      π = hg/Z,     N = E(h/g),      r = (h/g)/N.

Both π and r have mean one. The Markov kernel

                                      K(x, y) = P (x, y)h(y)/g(x)
                                                                                       √
is reversible for π dµ. Its eigenvalues are positive: conjugation by multiplication by π identifies
it with M√h/g P M√h/g , a positive definite matrix. Its top eigenvalue is one and is simple because
all entries are positive. Write λ2 (K) for its second eigenvalue and gap(K) = 1 − λ2 (K). These
are finite Markov-chain quantities.
    The general question motivating this work fixes b, C > 0, puts
                                     1+ρ                       √
                                s=       ,       kL = min{L, ⌊C L⌋},
                                     1−ρ
and imposes
                       π ≥ b,        Eπ s ≤ 2,     EπχS = 0     (1 ≤ |S| ≤ kL ).                       (1)
The last condition concerns the actual stationary density, on the original labelled coordinates. It
is equivalent to uniform coordinate marginals of these orders. It does not assign exact marginals
to r.
    The results have distinct scopes. Section 2 gives one fixed ρ and floor for which the numerical
implication Eπ s ≤ 2 ⇒ Ers ≤ 2 fails even under all of (1). Section 3 treats every fixed ρ
and proves a dimension-free bound for ∥r∥t for 1 ≤ t < t+ (ρ) < s; with matching it proves
r − π → 0 in this range. Section 4 treats every positive potential on specified code algebras,
without a moment cap or floor for its spectral result. It controls the full chain, not only its
quotient. Section 5 relates the sharper disjoint-block bounds and the simplex example to these
conclusions. Section 6 proves positive-rate, all-large-length code existence with simultaneous
column separation, specializes the full-chain estimate exponentially, and gives actual normalized
stationary floor/cap witnesses. Sections 7–8 use the finite bootstrap to control the entire low-to-
all operator through a fraction of the matching degree, localize actual non-Perron eigenfunctions,

                                                   2
and exclude a generic tail-space repair. Section 9 derives weak relaxation without matching and
proves a summable rate and uniform-start estimation bound at ρ = 1/2. Section 10 proves
a full gap from a fixed positive potential minimum and the critical cap, without matching or
upper height restrictions, and derives the two-level class as a consequence of its stationary floor.
Propositions 10.3 and 10.5 show that neither floor and cap alone nor the full exact-matching
hypotheses supply that additional minimum, even under strong near-uniformity. Theorem 10.7
then proves that the exactly matched family retains the noise gap asymptotically, with exponential
error. Section 11 constructs the opposite denominator defect, with P h → 0 and h/P h → ∞ at
a point, while proving critical ratio convergence and full-spectrum stability for that new family.
Section 12 separates potential smoothing from stationary-density smoothing: the former preserves
the stationary floor but can break exact matching despite retaining the critical cap, whereas the
latter preserves the constraints. Section 13 proves full-spectrum convergence to Boolean noise for
the actual chain reconstructed after sufficiently strong fixed density smoothing, uniformly over
all admissible inputs. It also refutes a vanishing critical-norm perturbation premise. Section 14
realizes a failure of separate variance and form upper comparisons on actual admissible chains,
while controlling both full gaps. Direct comparison with the original spectrum remains open.
    The manuscript groups analytical sources 349, 350, 351, corrected 353B and 355 with the
separately audited 16 November low-to-full and dimension-free follow-ups A–D and the weak-
relaxation and estimation notes E–G, together with the 17 November two-level and positive-
background full-gap notes I and J and the vanishing-minimum notes K and L and their full-chain
classification M, together with the exact-matching regularization obstruction N and the density-
regularized full-spectrum theorem O, together with the actual separate-comparison obstruction
P and the small-denominator family and spectral classification Q. The total-variation estimate
from source 341 is proved again in Section 3. No spectral conclusion is inferred from moment
convergence alone. No assertion about a physical Yang–Mills gap or a continuum limit is made.


2    Failure of exact critical-cap transfer
Theorem 2.1. There are fixed ρ∗ ∈ (1/3, 1/2) and b∗ = 1/16 such that, for every fixed C > 0, a
sequence of strictly positive potentials satisfies (1) for every L and satisfies

            EπLs∗ < 2 < ErL
                          s∗
                               for all sufficiently large L,    s∗ = (1 + ρ∗ )/(1 − ρ∗ ).

Both displayed moments tend to two. This is not a divergent-moment or collapsing-gap example.

Proof. On a two-dimensional cube, in the order (++, +−, −+, −−), take

        H = (29/16, 1/4, 1/8, 29/16) = 1 + cx − cy + dxy,           c = 1/32,   d = 13/16.

Thus EH = 1. Put q = c(x − y), v = 2c2 = 1/512, w = d2 = 169/256. For an effective noise
parameter θ ≥ 0,

                  Gθ = Pθ H = 1 + θq + θ2 dxy,       Zθ = EHGθ = 1 + θv + θ2 w.
             √
Take hθ = H/ Zθ , πθ = HGθ /Zθ , and rθ = (H/Gθ )/E(H/Gθ ). These are actual densities from
the same potential. At θ = 0, both densities equal H, and differentiation gives

                               π0′ = H(q − v),       r0′ = −H(q − v).


                                                 3
Indeed EHq = v and (EH/Gθ )′θ=0 = −v. For each fixed t > 1, let

                                                31(1/4)t − 33(1/8)t − 2(29/16)t
                        Ct = EH t q − vEH t =                                   .
                                                             2048
This is strictly negative. To see this, f (t) = 31 4−t − 33 8−t has f ′ (t) = log 2 8−t (99 − 62 2t ) < 0
for t ≥ 1, whereas 2(29/16)t is increasing; at t = 1 both are 29/8. Consequently
                            d                            d
                              Eπ t = tCt < 0,              Ert = −tCt > 0.                           (2)
                            dθ θ 0                       dθ θ 0

    Let M (t) = EH t . Direct rational identities give M (2) = 851/512 < 2 and M (3) = 24425/8192 >
2. Strict convexity of x log x gives M ′ (1) = EH log H > 0, and M ′′ (t) = EH t (log H)2 > 0. Thus
there is a unique t∗ ∈ (2, 3) with M (t∗ ) = 2. Fix ρ∗ = (t∗ − 1)/(t∗ + 1), so its critical exponent is
precisely t∗ . Formula (2), with this exponent fixed, gives strict opposite inequalities around two
for all sufficiently small positive θ. No varying exponent or numerical root is used.
    For large L, let m = ⌊L/2⌋ and use two disjoint blocks B1 , B2 of size m, with an unused
coordinate when L is odd. Set zi = χBi and θ = ρm          ∗ . The variables z1 , z2 are uniform√and
independent; restricted to their algebra, Pρ∗ is exactly the two-bit Pθ . Use hL = H(z1 , z2 )/ Zθ .
Products, positive inverses and expectations on the quotient agree with those above, so these are
the required actual πL , rL .
    Their Fourier support is contained in {∅, B1 , B2 , B1 ∪ B2 }. In particular πL has exact
marginals through degree m − 1. Eventually m > kL , θ → 0, and min πL → min H = 1/8.
Choose a finite L0 after which the floor 1/16, the matching degree and the two strict moment
inequalities all hold. For the remaining finitely many L, put hL = 1. This defines a full admissi-
ble sequence. Continuity gives convergence of both moments to two. Section 5 shows that this
two-block family in fact has gap tending to 1 − ρ∗ .

    The following estimates distinguish two simpler classes: two-level potentials cannot produce
divergent critical weighting moments under a fixed stationary floor and cap, while product poten-
tials obey the stronger constant-one moment comparison. Section 10 further proves a dimension-
uniform full gap for the two-level class under the stationary floor and cap.
Proposition 2.2. Normalize EhP h = 1 and assume π ≥ b. If h takes at most two values, then
g ≥ b/2 and Erp ≤ (4/b3 )p Eπ p for every p ≥ 1. If h is a product of positive one-coordinate
factors, then Erp ≤ Eπ p for every p ≥ 1, without a floor assumption. The latter also holds for
products of factors on disjoint block parities, with their respective effective noise parameters.
Proof. Write a = Eh ≤ 1, the inequality following from the constant Fourier component of
          2
 P √ρ h       = 1. The floor implies h ≥ b/g, so a ≥ bE(1/g) ≥ b/a. Hence a2 ≥ b. Under π dµ,
          2
Eπ (1/g) = a and Eπ (1/g 2 ) = N , giving N ≥ a2 ≥ b. For a nonconstant two-level h, let h = m
on a set of mass q ∈ (0, 1) and h = M > m on its complement. Integrating the floor on the first
set gives mE(g1A ) ≥ bq, whence m ≥ bq. Also M (1 − q) ≤ a ≤ 1. Since g ≥ m and hg ≥ b with
h ≤ M , we get g ≥ max{bq, b(1 − q)} ≥ b/2. Thus r = π/(N g 2 ) ≤ 4π/b3 . The constant case is
immediate.
    For one bit, scaling removes an irrelevant constant, so take H = 1+tx, |t| < 1. The normalized
densities are π = 1 + Ax and r = 1 + Bx, where
                                        (1 + ρ)t              (1 − ρ)t
                                  A=             ,       B=            .
                                        1 + ρt2               1 − ρt2

                                                     4
Cross multiplication gives |B| ≤ |A|, since the difference of the two relevant positive numerators
is 2ρ(1 − t2 ) > 0. The function [(1 + c)p + (1 − c)p ]/2 is even and nondecreasing for c ∈ [0, 1)
and p ≥ 1. This proves the one-bit assertion. Tensorization of the noise, the energy, N and the
moments proves the product assertions.


3    Inverse moments and subcritical transfer
In this section scale h so Z = 1, put Q = P√ρ and set B = 21/s . Assume π = hg ≥ b > 0 and
Eπ s ≤ 2; necessarily b ≤ 1. Define

         R = 1 + ρ−1 ,                     D0 = 1 + ρ−3 ,                D∗ = 2ρ−2 + ρ−3 − 1,
                  sq/(s + q) − 1                                              1+ρ        2
                                                                                             q    
      F (q) = 1 +                ,                                       q± =       1 + ρ ± 1 + ρ2 .
                        ρ4                                                     ρ3

Let q0 = D∗ , qn+1 = F (qn ), and
                                         sqn                        sq+
         An = b−1 (B/b)n ,      tn =           ,           t+ =           ,            Kn = Bb−3 (B/b)2n .
                                       qn + 2s                    q+ + 2s

Theorem 3.1. For every L and n ≥ 0,

              N ≥ b,    gP g ≥ b,       g −1        ≤ b−1 ,       g −1        ≤ An ,     ∥r∥tn ≤ Kn .
                                               D0                        qn

Here q− < D∗ < q+ , qn ↑ q+ < ∞, and 1 < t0 < tn < t+ < s for n > 0. These conclusions need
no matching. If additionally EπχS = 0 for 1 ≤ |S| ≤ k, put
                                q
                         η0 =       max{ρ, (1 − ρ)/2} < 1,               ek = Bη0k+1 .

For 1 < t < tn ,
                                                                                  tn − t
                       ∥r − π∥t ≤ (2ek )α (Kn + B)1−α ,                  α=               .                  (3)
                                                                                t(tn − 1)
Thus for every fixed 1 < t < t+ , ∥r − π∥t → 0 whenever k → ∞, in particular for k = kL .

    We use the classical scalar Boolean hypercontractive inequalities [2]: for 1 < p ≤ q < ∞,
∥Pθ f ∥q ≤ ∥f ∥p when θ2 ≤ (p − 1)/(q − 1). For strictly positive f and finite β < α < 0,
reverse hypercontractivity gives ∥Pθ f ∥β ≥ ∥f ∥α when θ2 ≤ (1 − α)/(1 − β). Negative exponents
denote generalized means (Ef a )1/a , not norms. In particular ∥f ∥−a = 1/ f −1 a for a > 0. No
zero-exponent convention is needed in the uses below.
                                                                                           √
Proof of the inverse-moment and bootstrap assertions. The preceding proof gives a = Eh ∈ [ b, 1]
and N ≥ b. Applying P to h ≥ b/g and using Jensen in each transition row yields

                             g ≥ bP (1/g) ≥ b/(P g),              g −1 ≤ (P g)/b.                            (4)

This is a consequence of the actual stationary floor, not an assumed bound on inf g. Since
∥Qh∥2 = 1 and P g = Pρ3/2 Qh, ordinary hypercontractivity gives ∥P g∥D0 ≤ 1, proving the
first inverse bound. Likewise g = P√ρ Qh gives ∥g∥R ≤ 1. The floor yields h−1 ≤ g/b, so
∥h∥−R ≥ b. Reverse hypercontractivity with α = −R, β = −D∗ and θ = ρ applies because
D∗ = (1 + R)/ρ2 − 1 > R. It gives ∥g∥−D∗ ≥ b, or g −1 D∗ ≤ b−1 . Also D∗ − D0 = 2(ρ−2 − 1) > 0.

                                                       5
   If q > s/(s − 1) and g −1 q ≤ A, put p = sq/(s + q) > 1. Holder applied to h = π/g gives
∥h∥p ≤ BA. As P g = Pρ2 h, hypercontractivity and (4) give

                                   g −1           ≤ b−1 ∥P g∥F (q) ≤ (B/b)A.
                                          F (q)

The map has

                        −ρ4 q 2 + (s − 1)(1 − ρ4 )q − s(1 − ρ4 )                          s2
          F (q) − q =                                            ,       F ′ (q) =               > 0.
                                       ρ4 (s + q)                                    ρ4 (s + q)2

The numerator has roots q− , q+ : its discriminant equals 4ρ2 s(1 − ρ4 ), and s(1 − ρ4 ) = (1 + ρ)2 (1 +
ρ2 ). Direct bounds show
                                                             q
              ρ3 (D∗ − q− ) = ρ − ρ2 − 2ρ3 + (1 + ρ) 1 + ρ2 ≥ (1 + 2ρ)(1 − ρ2 ) > 0,
                                                               q
              ρ3 (q+ − D∗ ) = −ρ + ρ2 + 2ρ3 + (1 + ρ) 1 + ρ2 ≥ 1 + ρ2 + 2ρ3 > 0.

Since D∗ > R = 2s/(s − 1), every step is valid. Monotonicity of F gives qn < qn+1 < q+ , and
continuity identifies the limit as q+ . Iteration gives An . Finally
                                                π             1  1  2
                                          r=        ,           = +
                                               N g2          tn  s qn

and Holder give ∥r∥tn ≤ b−1 BA2n = Kn . The inequalities between the tn follow from D∗ >
2s/(s − 1) and monotonicity of q 7→ sq/(q + 2s).

   For completeness we supply the stationary matching argument underlying (3); it does not
require a pointwise floor.
Lemma 3.2. Under energy normalization, if ∥π∥p ≤ Bp for a finite p > 1 + ρ and π has
exact marginals through degree k, set ηp2 = ρ max{1, 1/(p − 1)} < 1 and e = Bp ηpk+1 . Then
a2 ≥ (1 + e2 )−1 , a2 ≤ N ≤ 1, and ∥r − π∥1 ≤ 2e.
Proof. Put v = 1 − a2 = ∥Qh − a∥22 ≥ 0, and let Π>k be Walsh projection above degree k. We
have                                       √
                          ∥Π>k g∥p′ ≤ ηpk+1 v,    p′ = p/(p − 1).
For p′ ≤ 2 this is the high-degree multiplier
                                         √ ′ bound for Q, √  followed by norm monotonicity. For
 ′
p > 2, factor Q = Pt Pβ , where t = 1/ p − 1 and β = ρ/t = ηp < 1. Hypercontractivity
                     ′
sends Pt : L2 → Lp , and the high-degree multiplier of Pβ supplies the stated bound. The noise
                                                                                 ′
operators commute with Walsh projections; no norm bound for the projection on Lp is presumed.
                                                  √
Matching gives EπΠ≤k g = a. Hence Eπg ≤ a + e v. Cauchy–Schwarz for the measure h dµ gives
                                                  √
1 = (Ehg)2 ≤ aEhg 2 = aEπg. Therefore v/a ≤ e v. If v > 0, division yields v ≤ a2 e2 ; the v = 0
case is immediate. Thus a2 ≥ (1 + e2 )−1 and 2(1 − a) ≤ e2 .                            √
    For the upper bound on N , put u = h/g and A = M√u P M√u . The positive vector hg has
A-eigenvalue one. Perron–Frobenius and positive semidefiniteness therefore give ∥A∥ = 1. With
X = M√u Q, the matrices XX ∗ = A and X ∗ X = QMu Q have the same eigenvalues. Testing the
latter at the unit vector 1 yields N = Eu ≤ 1. Cauchy–Schwarz under π gives a2 ≤ N as above.
Since r = π/(N g 2 ),
                       √       √              √     √ 2              √
                    E rπ = a/ N ≥ a,            r − π 2 = 2(1 − a/ N ) ≤ e2 .

                                                         6
Multiply the difference of the square roots by their sum and apply Cauchy–Schwarz; the latter
sum has norm at most two. This gives ∥r − π∥1 ≤ 2e. Total variation is half this L1 distance,
not the entire distance.

Completion of Theorem 3.1. Apply Lemma 3.2 with p = s > 1 + ρ, Bp = B. Its parameter
becomes η0 in the theorem. Since tn < s, ∥r − π∥tn ≤ Kn + B. Interpolation between 1 and tn ,
with 1/t = α + (1 − α)/tn , gives (3). For each fixed t < t+ choose one finite n with t < tn before
taking L → ∞.

   The ceiling is a limitation of this particular iteration. Its starting exponent lies strictly
between the two fixed points and increases only to finite q+ . Moreover An = b−1 (B/b)n diverges
as n → ∞. We have neither a uniform estimate at q+ nor one at t+ . Even a finite inverse
bound at q+ would leave t+ < s. None of these facts disproves a different method for the critical
moment.


4    Full-chain estimates for code-supported potentials
Identify Walsh indices with vectors in FL
                                        2 , and let C be a nonzero binary linear code of dimension
n and minimum nonzero Hamming weight D ≥ 2. Set M = 2n and

                                                           1−δ               ρ+η              (1 − ρ2 )δ
                      ρ|c| < 1,
             X
       δ=                         η = M ρD/2 ,     α=          ,     BC =        ,   εgap =              .
            c∈C\{0}
                                                           1+δ               1−δ               ρ(1 − δ)

Theorem 4.1. For every strictly positive h whose Fourier support is contained in C, with no size
restriction on its quotient values,

                         max{0, ρ − εgap } ≤ λ2 (K) ≤ min{1, max{1 − α, BC }}.                               (5)

Both π and r have exact marginals through degree D − 1, and

                                            α2 ≤ r/π ≤ α−2 .                                                 (6)

For any sequence of such codes with fixed ρ and η → 0, gap(K) → 1 − ρ, uniformly over all
strictly positive quotient potentials. If additionally Eπ s ≤ 2, then Ers ≤ 2α−2s . The cap is needed
for this absolute moment bound, not for (5) or (6).

Proof. Choose a basis c1 , . . . , cn and put zi (x) = χci (x). This quotient map is surjective with
                                                                               P
equal fibers, and h(x) = H(z(x)) for a positive function H. Writing c(I) = i∈I ci , the quotient
noise density relative to uniform w is

                                                          ρ|c(I)| χI (z)χI (w).
                                                  X
                                    b0 (z, w) =
                                                  I⊆[n]

This is the actual positive stochastic quotient of product noise. In particular 1 − δ ≤ b0 ≤ 1 + δ.
With a = EH and G = P H on the quotient, a(1 − δ) ≤ G ≤ a(1 + δ). The quotient Doob kernel
has density b0 (z, w)H(w)/G(z) and minorizes α times the probability density H(w)/a. Thus its
oscillation contraction is at most 1 − α. Every nonconstant eigenfunction has nonzero oscillation,
so all its non-Perron eigenvalues have modulus at most 1 − α.
    It remains to control the other sectors, because the quotient spectrum alone is insufficient.
For each coset t + C, let Vt = χt {F (z) : F any quotient function}. These spaces are mutually

                                                          7
orthogonal under π dµ: products of quotient functions with π remain in the C algebra, and a
Walsh character outside C has zero expectation against that algebra. They span all 2L dimensions.
Multiplication by h and by 1/g preserves each sector, as does noise, so each is K-invariant. Under
the identification χt F ↔ F , its operator is

                                      H(w)
                                                                             ρ|t+c(I)| χI (z)χI (w).
                                                                        X
            Kt F (z) = Ew bt (z, w)        F (w),         bt (z, w) =
                                      G(z)                              I

For t ∈
      / C this is a signed kernel, not a Markov kernel. Choose a minimum-weight representative
with d = |t| ≥ 1. If d ≤ D/2, all other vectors in the coset have weight at least D − d ≥ D/2, so

                                        ρ|v| ≤ ρd + (M − 1)ρD/2 ≤ ρ + η.
                                 X

                                v∈t+C

If d > D/2, all weights exceed D/2 and the sum is at most η. Consequently |bt | ≤ ρ + η ≤ BC b0 ,
whence |Kt F | ≤ BC K0 |F |. Supremum norms bound every sector eigenvalue in modulus by
BC . Together with the quotient bound and the global Markov bound one this proves the upper
inequality in (5).
    For the lower inequality, any singleton ei is outside C because D ≥ 2. In bei − ρb0 , a codeword
not containing i contributes zero; a codeword containing i contributes coefficient (1 − ρ2 )ρ|c|−1 .
Hence
                                |bei − ρb0 | ≤ (1 − ρ2 )δ/ρ ≤ εgap b0 .
It follows that |Kei 1 − ρ| ≤ εgap . The original character χei has mean zero under π and norm one,
since π is in the C algebra. Its Rayleigh quotient is at least ρ − εgap . The variational principle
and positive definiteness yield the lower bound.
    The algebra of quotient functions is closed under multiplication and positive inversion. Thus
π and r are both C-supported; their unit means imply the stated exact marginals. Let Π = HG/Z
be the quotient stationary density. Then

                                                                   G−2
                                 EΠ G−2 = N/Z,            r/π =          .
                                                                  EΠ G−2

The interval a(1 − δ) ≤ G ≤ a(1 + δ) proves (6). Finally δ ≤ (M − 1)ρD ≤ ηρD/2 ≤ η. If η → 0,
then δ → 0, α → 1, BC → ρ and εgap → 0, uniformly in H. This proves the limiting and moment
assertions.


5     Disjoint blocks and a strictly larger potential class
5.1   The sharper direct block regime
Let L = nm + d with n ≥ 1, m ≥ 2 and d ≥ 0, and let h = H(z1 , . . . , zn ) > 0, where zi is
the parity of the ith disjoint block of size m. Residual coordinates are unused. This is a special
code algebra, but direct factorization yields better bounds than the coarse distance–cardinality
estimate.

Proposition 5.1. Put θ = ρm , ℓ = (1 − θ)n , u = (1 + θ)n , and

                                             ρ + ρm−1                       (1 − ρ2 )ρm−1
                    αb = ℓ/u,         βb =            ,       εgap,b =                    .
                                               1−θ                              1−θ

                                                     8
For every positive H,

          max{0, ρ − εgap,b } ≤ λ2 (K) ≤ min{1, max{1 − αb , βb }},                   αb2 ≤ r/π ≤ αb−2 .

Both densities have exact marginals through degree m − 1. If m → ∞ and nρm → 0, the gap
tends uniformly in H > 0 to 1 − ρ.
Proof. The quotient noise density is b0 (z, w) = i (1 + θzi wi ), so ℓ ≤ b0 ≤ u and aℓ ≤ G ≤ au.
                                                           Q

The same minorization and moment arguments as in Theorem 4.1 give the quotient and density
bounds, now with αb . For a sector representative, remove complete blocks from its support. Let
ji ∈ {0, . . . , m − 1} be its number of coordinates in block i, and e its residual weight. Factoring
the Fourier sum gives                             Y
                                   bt (z, w) = ρe   ρji + ρm−ji zi wi .
                                                                     

                                                       i
For ji = 0 the factor is that of b0 . If 1 ≤ ji ≤ m − 1, its absolute ratio to 1 + θzi wi is bounded
by βb : the numerator is at most ρji + ρm−ji ≤ ρ + ρm−1 . This last inequality follows because the
convex function x 7→ ρx + ρm−x attains its maximum on [1, m − 1] at an endpoint. If βb < 1, a
nontrivial sector with at least one interior factor therefore has |bt | ≤ βb b0 ; if it has only residual
support, its ratio is ρe ≤ ρ < βb . This bounds those eigenvalues. If βb ≥ 1, the global Markov
bound one already gives the stated upper bound; no invalid inequality βbj ≤ βb is used.
    For a singleton in one block, its factor differs from ρ(1 + θzi wi ) by (1 − ρ2 )ρm−1 zi wi . The
other factors are unchanged, yielding |bt − ρb0 | ≤ εgap,b b0 . The singleton Rayleigh argument gives
the lower bound. All nonzero vectors in the block code have weight at least m, giving matching.
Finally − log αb = n log[(1 + θ)/(1 − θ)] ≤ 4nθ once θ ≤ 1/2. Thus αb → 1, βb → ρ and εgap,b → 0
in the stated regime.

    Structural inclusion must not be confused with inclusion of the quantitative regimes. Theorem
4.1 applied to this code asks for 2n ρm/2 → 0, whereas Proposition 5.1 requires only nρm → 0
with m → ∞. We retain the direct bounds instead of claiming the coarser condition subsumes
them. In particular Proposition 5.1 with n = 2 applies to Theorem 2.1.

5.2    Simplex potentials outside disjoint-block representations
Proposition 5.2. For each j ≥ 2 put Lj = 2j − 1 and index coordinates by nonzero v ∈ Fj2 . The
binary simplex code
                            Cj = {ca : a ∈ Fj2 }, ca (v) = a · v,
has dimension j and every nonzero word has weight Dj = 2j−1 . It satisfies the asymptotic
condition in Theorem 4.1 forpevery fixed 0 < ρ < 1. On this length subsequence its matching
degree eventually exceeds ⌊C Lj ⌋ for every fixed C > 0. There are strictly positive potentials
supported on this code that cannot be represented as functions of disjoint equal-size block parities
of size m ≥ 2, even after coordinate permutations or enlargement of the disjoint-block algebra.
Proof. The map a 7→ ca is injective by inspection at the unit-vector coordinates. A nonzero linear
form takes the value one at exactly half the points of Fj2 , and the excluded zero vector has value
zero. Thus the dimension and weight assertions follow directly. Here
                                             j−1                        j−2
                             δj = (2j − 1)ρ2       ,           ηj = 2j ρ2     −→ 0.

In particular δj < 1 eventually. Also Dj − 1 = (Lj − 1)/2, proving the matching assertion on the
stated subsequence.

                                                           9
    Choose                               X
                       hj = 1 + εamp               χc ,        0 < εamp < 1/(2j − 1).
                                       c∈Cj \{0}

This is strictly positive, and its Fourier support is exactly Cj . The amplitude εamp is not the
spectral error εgap . If hj were a function of disjoint block parities, uniqueness of the Walsh
expansion would put Cj inside the linear span of those block indicators. Every word in that span
is constant within each block and vanishes on unused coordinates. But Cj separates every pair of
distinct coordinates v, w: choose a with a · (v + w) = 1. Also every coordinate is nonzero in some
codeword. Consequently no block can contain two coordinates and none can be unused. This
contradicts m ≥ 2, and is unchanged by coordinate permutations or by allowing more disjoint
blocks.

    The code construction is classical [4]; its elementary parameter proof is included to avoid
treating a coding reference as a new theorem. The strict separation is an existence statement for
the full-support positive potentials just exhibited. It does not hold for every potential in the code
algebra, since constants also belong to disjoint-block algebras. Nor does this argument assert
a prescribed stationary floor or moment cap for the displayed amplitude family. Its use here
is to establish that the full-chain code theorem covers positive potentials beyond the disjoint-
block class. Arbitrary invertible changes of the original Boolean coordinates are not permitted
replacements for permutations: they generally change Hamming weights and the noise operator.


6    Positive-rate families at every sufficiently large length
The simplex example gives a transparent strict-class witness on a length subsequence. Classical
random linear coding also realizes the spectral mechanism at positive rate for every sufficiently
large length. The additional column conditions used below ensure strict separation from disjoint-
block representations for the same codes, rather than for separately chosen examples.
    Let H2 (d) = −d log2 d − (1 − d) log2 (1 − d) denote binary entropy.

Theorem 6.1. Fix 0 < ρ < 1, 0 < d < 1/2 and

                                                      d
                                                                             
                           0 < Rcode < min 1 − H2 (d), log2 (1/ρ) .                                       (7)
                                                      2

For every sufficiently large integer L there exists a binary linear code CL ⊂ FL
                                                                               2 with dimension
nL = ⌊Rcode L⌋, minimum distance DL ≥ ⌈dL⌉, and a generator matrix with nonzero, pairwise
distinct columns. Set

    a∗ = (d/2) log(1/ρ) − Rcode log 2 > 0,           EL = e−a∗ L ,        Cρ = max{1 + ρ, (1 − ρ2 )/ρ}.

For every strictly positive potential h supported on the Fourier algebra of this code, and all suffi-
ciently large L,
                                                             EL
                                 |gap(Kh ) − (1 − ρ)| ≤ Cρ        .                              (8)
                                                           1 − EL
The bound is uniform over all such positive h, with no amplitude, stationary floor or moment
assumption. Both π and r have exactly uniform labelled marginals through degree ⌈dL⌉ − 1.
    Moreover, for every fixed 0 < b < 1 and finite s > 1, there are potentials in these same
algebras, at every sufficiently large length, with energy one, π ≥ b and Eπ s ≤ 2, whose Fourier

                                                          10
support is the full code and which admit no disjoint equal-size block-parity representation with
block size at least two. In particular these witnesses satisfy (1) for its critical exponent and every
fixed C > 0, eventually, and have the gap estimate (8).

Proof. Both upper bounds in (7) are positive, so the allowed rate interval is nonempty. Put
n = ⌊Rcode L⌋, eventually at least one, and sample an n by L matrix G with independent fair
binary entries. This is a probabilistic existence argument, not an executed random search. For
each fixed nonzero a ∈ Fn2 , the entries of aG are independent fair bits. The different vectors aG
need not be independent. A union bound gives
                                                                    !
                                             n        −L
                                                            X       L
              Pr{∃a ̸= 0 : |aG| < dL} ≤ (2 − 1)2                        ≤ 2n−L(1−H2 (d)) .
                                                           0≤i<dL
                                                                    i

For the last step, since d < 1/2 and i ≤ dL,

                           di (1 − d)L−i ≥ ddL (1 − d)(1−d)L = 2−LH2 (d) .

Multiply this lower bound by Li , sum over the stated integer indices, and bound the corre-
                                   

sponding binomial probability sum by one. This proves the entropy bound without assuming dL
integral. The complement of the strict bad event gives weights at least ⌈dL⌉. In particular a
nonzero kernel vector is impossible, so G has full row rank and its row-image code has dimension
n.
    Each column is uniform in Fn2 . A second union bound gives

                                                                 L(L − 1) −n
                                                                                    
             Pr{a zero column or an equal pair of columns} ≤ L +          2 .
                                                                    2

The sum of these two error bounds tends to zero. Indeed the first is at most 2−L(1−H2 (d)−Rcode )
and the second is at most 2[L + L(L − 1)/2]2−Rcode L . For every sufficiently large integer L,
their sum is less than one, so a single matrix has simultaneously the distance, rank and column
properties. Select one for each such length. No efficient construction or nested family is asserted.
    For the resulting code, ML = 2nL and DL ≥ dL give

                       ηL = ML ρDL /2 ≤ EL ,       δL ≤ ML ρDL ≤ ηL ≤ EL .

Eventually DL ≥ 2 and δL < 1, so Theorem 4.1 applies to every positive code potential. For
EL ≤ min{1/2, ρ/2},
                                         2δL
                               1−α=           ≤ 2EL ≤ ρ,
                                       1 + δL
                                       ρ + ηL                 EL
                                B CL =        ≤ ρ + (1 + ρ)        ,
                                       1 − δL               1 − EL
                                       1 − ρ2 EL
                                εgap ≤              .
                                          ρ 1 − EL
The two sides of (5) therefore give (8); the clipping by zero and one only improves the estimates.
The matching assertion follows from the  √ same theorem and DL ≥ ⌈dL⌉. In particular this
matching degree eventually exceeds ⌊C L⌋ for every fixed C > 0.
   It remains to construct the admissible strict-class witnesses. Nonzero columns ensure that
every coordinate is active in some codeword; distinct columns ensure that every two coordinates

                                                 11
are separated by some codeword. For the latter, if the two columns are v ̸= w, choose a linear
functional detecting v + w ̸= 0. For 0 < τ < 1, choose
                                               τ      X
                                  h0 = 1 +                  χc .
                                            ML − 1 c∈C \{0}
                                                               L


Then 1 − τ ≤ h0 ≤ 1 + τ , and its Fourier support is exactly CL . If h0 were a function of
any number of disjoint equal-size block parities, its full support would force CL into the span of
their whole-block indicators. Every word in that span is constant within a block and zero on
unused coordinates. Pair separation excludes any block of size at least two, and activity excludes
residual coordinates. This rules out every representation allowed in Proposition 5.1, including
larger quotient algebras and coordinate permutations.
    For prescribed 0 < b < 1 and finite s > 1, choose τ > 0 sufficiently small that
                                                   2
                                             1+τ
                                         
                                  Aτ =                  ≤ min{1/b, 21/s }.
                                             1−τ
The right side exceeds one, so such a single positive τ , independent of L, exists. Positivity and
the Markov property put both h0 and          √ P h0 in [1 − τ, 1 + τ ]. Hence their product and its mean Z
lie in [(1 − τ )2 , (1 + τ )2 ]. Set h = h0 / Z. This preserves its support and kernel, gives EhP h = 1,
and yields
                                        h0 P h0
                          A−1τ ≤π =             ≤ Aτ ,      π ≥ b,       Eπ s ≤ Asτ ≤ 2.
                                           Z
Thus all assertions concern the same normalized potential and its actual stationary density. The
full-chain bound was already uniform in the potential and remains valid for these witnesses.

    The entropy-volume and random-linear-code ingredients are classical Gilbert–Varshamov ar-
guments [5]; the proof is included with the precise rounding and simultaneous column require-
ments used here. The rate Rcode is distinct from the inverse-moment exponent R of Section
3. The theorem supplies all-large-length positive-rate realizations of the code-restricted mech-
anism. It does not remove the code-algebra hypothesis, establish a general critical weighting
cap, or provide a collapsing example. The strict-class conclusion is existential for the specified
full-support potentials, not universal for all positive functions on the code. The prescribed-floor
witness assertion excludes b = 1 and makes no uniform endpoint claim as ρ approaches zero or
one.


7    Dimension-free spectral windows
Throughout this section, the noise parameter 0 < ρ < 1 and stationary floor b > 0 are fixed. On
the uniform Boolean cube, write P = Pρ , Q = P√ρ , g = P h, π = hg, u = h/g, and T = QMu Q.
We retain h > 0, EhP h = 1, π ≥ b, Eπ s ≤ 2, s = (1 + ρ)/(1 − ρ), and exact stationary matching
through degree k. These hypotheses are not removed below.
Lemma 7.1. For every fixed 0 < ρ < 1, a finite index n, independent of L, satisfies tn > 1 + ρ
in Theorem 3.1.
Proof. The inequality tn > 1 + ρ is equivalent to qn > qc := 2(1 + ρ)/ρ. Direct substitution in
the already defined bootstrap map gives
                                                   (1 − ρ2 )(3 − ρ2 )
                                  F (qc ) − qc =                      > 0.
                                                      ρ3 (2 − ρ)

                                                        12
The numerator of F (q) − q is a negative-leading quadratic with roots q− , q+ . Thus q− < qc < q+ .
Since qn increases to q+ , for some finite n, qn > qc . Fix such an index before taking dimension or
matching-degree limits.

                                                              pp0 < t < s, and ∥u∥t = N ∥r∥t ≤
   Set p0 = 1 + ρ, t = tn and Kt = Kn at this fixed index. Then
Kt by Lemma 3.2 and Theorem 3.1. With B = 21/s , η0 = max{ρ, (1 − ρ)/2}, e = Bη0k+1 ,
p = (p0 + t)/2, and α = (1/p − 1/t)/(1 − 1/t), the discrepancy satisfies
                                                           α(k+1)
  ∥u − π∥p ≤ ∆k := (2e)α (Kt + B)1−α + Be2 ≤ Cp η0                  ,       Cp = (2B)α (Kt + B)1−α + B 3 .

This uses u − π = N (r − π) + (N − 1)π, 1 − N ≤ e2 from Lemma 3.2, and interpolation in
Theorem 3.1. No endpoint estimate is used.
    For a polynomial F of degree at most d and finite r ≥ 2, classical Boolean hypercontractivity
gives                                          q
                              ∥QF ∥r ≤ max{1, ρ(r − 1)}d ∥F ∥2 .
Indeed, multiply each degree-j Fourier coefficient by Aj , A = ρ(r − 1), and then apply P1/√r−1 .
                                                                        p

The composition is Q and the first multiplier has L2 norm at most max(1, A)d on the polynomial
subspace. The multiplier for A > 1 is algebraic, not a Markov kernel. This standard argument is
the one used in O’Donnell, Theorem 9.21 [6].
   Let Rd be the orthogonal projection onto degrees at most d, including constants. Set
              pp0             p0 + min(s, 2)             sz                                             ρ
                                                                            q                      r
      r1 =          ,    z=                  ,   r2 =       ,    Ai =           ρ(ri − 1),    β=           .
             p − p0                 2                   s−z                                            z−1
Then A1 , A2 > 1 and 0 < β < 1.
Theorem 7.2. For 0 ≤ d ≤ k,

             ∥(T − P )Rd ∥2→2 = ∥Rd (T − P )∥2→2 ≤ εk,d := ∆k Ad1 + (B + 1)β k+1−d Ad2 .                       (9)

Proof. To prove this, write (T − P )F = Q[(u − π)QF ] + Q[(π − 1)QF ] for F = Rd F . The first
term is bounded by ∥u − π∥p ∥QF ∥r1 , using Q : Lp0 → L2 and Hölder’s inequality. The second
product has no Fourier coefficients below degree k + 1 − d. Factor Q = Pβ P√z−1 : the second
factor contracts Lz to L2 , and the first damps that support by β k+1−d . Hölder with s, r2 and
the polynomial bound complete the proof. The argument controls all low-degree inputs at once,
without summing individual columns or introducing a binomial factor. Self-adjointness gives the
row estimate.

   Choose
                                       α log(1/η0 ) log(1/β)
                                                                       
                        0 < c < min 1,             ,            ,                 d = ⌊ck⌋.
                                          log A1     log(A2 /β)
Then the right side of (9) is bounded by Cp η0α e−γ1 k + (B + 1)βe−γ2 k , where γ1 = α log(1/η0 ) −
c log A1 > 0 and γ2 = log(1/β) − c log(A2 /β) > 0. This dimension-free estimate requires only
k → ∞.
    The actual spectral representation is important here. With X = M√u Q, one has XX ∗ =
M√u P M√u and X ∗ X = T , so T has the actual spectrum of K and norm one. Its unit Perron
vector is w = Qh, since ∥Qh∥22 = 1 and T Qh = QMu P h = Qh. Lemma 3.2 gives ∥1 − w∥22 =
2(1 − Eh) ≤ e2 . For a unit non-Perron eigenvector ψ of T with λ ≥ ρ + ζ, fixed ζ > 0,

                                         ∥Rd ψ∥22 ≤ e2 + (εk,d /ζ)2 .

                                                     13
The nonconstant part follows by inverting λ − P on the low subspace; the constant part follows
from orthogonality to Qh and ∥1−Qh∥2 ≤ e. For 1 ≤ d ≤ min(k, L−1), let Hd = (I−Rd )T (I−Rd )
on the high subspace. The block comparison yields

                                     |λ2 (K) − max{ρ, ∥Hd ∥}| ≤ 2εk,d .

Indeed, the low diagonal and off-diagonal errors each have norm at most εk,d ; min-max applies to
the resulting self-adjoint perturbation. This is a reduction to the actual high block, not a bound
on its norm.


8    Necessary localization and a failed generic tail repair
Retain the setting of Section 7, with d = ⌊ck⌋, fixed ζ > 0, and all other parameters fixed. Let
Kf = λf be an √ actual real eigenfunction with λ ≥ ρ + ζ, normalized by Eπf = 0 and Eπf 2 = 1,
set ψ = Q(hf )/ λ. Then the exact pointwise identity is

                                               u|Qψ|2 = λπf 2 .

Writing δk = e2 + (εk,d /ζ)2 and U (M ) = {u > M }, with π(A) := E[π1A ] for sets A, gives

                                M (δk + ρd+1 )                            t/s′         ′               s
          E[πf 2 1U (M )c ] ≤                  ,      π(U (M )) ≤ BKt            M −t/s ,      s′ =       .
                                      λ                                                               s−1
Indeed ∥ψ∥2 = 1 and ⟨ψ, Qh⟩ = 0 follow from P (hf ) = λgf and the stationary normalization.
The multiplier formula gives ∥Qψ∥22 ≤ δk + ρd+1 ; integrate the identity on {u ≤ M }. For the
probability estimate, µ(U (M )) ≤ Ktt M −t and Hölder with ∥π∥s ≤ B complete the proof. With
γ0 = min{log(1/η0 ), γ1 , γ2 }, choose 0 < θ < min{log(1/ρ), 2γ0 /c} and M = eθd . As k → ∞, the
complement’s stationary squared mass tends to zero, while the stationary probability π(U (M )) is
                                         ′
          fixed constant times e−θtd/s . Both
at most a √                                √ strict restrictions on θ are needed for this argument.
At k ∼ C L, this is an exponential-in- L probability scale. It neither supplies a cut nor rules
out these modes.
   For completeness, this also forces divergence of each fixed higher stationary moment. For
                                                         t/s′
2 < ℓ < ∞, set ak = M (δk + ρd+1 )/λ → 0 and Ct = BKt . Hölder on the stationary probability
space gives, for all sufficiently large k,
                                      √                               θtd
                                                                                          
                                                   −(1/2−1/ℓ)
                       ∥f ∥Lℓ (π) ≥       1 − ak Ct             exp       (1/2 − 1/ℓ) .
                                                                       s′

Indeed, the squared mass on U (M ) is at least 1 − ak > 0, and is at most ∥f ∥2Lℓ (π) π(U (M ))1−2/ℓ .
This necessary growth is not a contradiction: no uniform upper bound on these eigenfunction
norms has been established. A generic tail-space Hölder repair is unavailable. For fixed 1 + 1/ρ <
q < ∞ and nonnegative integer cutoffs dL = o(L), set m = dL + 1, ℓ = L − m, and
                                                            L
                                                            Y   1 + ϵxj
                                      FL (x) = χ[m] (x)         √        .
                                                          j=m+1   1 + ϵ2

For sufficiently large L, this has unit L2 norm and no coefficients through degree dL . Its smoothed
norm is
                                                     √              √        1/q
                                 m/2 ℓ          ((1 + ρϵ)q + (1 − ρϵ)q )/2
                    ∥QFL ∥q = ρ      κ , κ=                √                      .
                                                              1 + ϵ2

                                                       14
The expansion log κ = 12 (ρ(q − 1) − 1)ϵ2 + O(ϵ4 ) makes κ > 1 for a sufficiently small fixed
ϵ ∈ (0, 1). Thus L−1 log ∥QFL ∥q → log κ > 0. This classical tensor sharpness mechanism refutes
a dimension-uniform L2 → Lq estimate on the entire high-degree space. It is not an admissible
Doob counterexample, and does not contradict same-exponent Lp → Lp tail smoothing [7, 8].
For the available t < s, one has 2t′ > 2s′ = 1 + 1/ρ, so this obstruction applies to the naive
Hölder attempt to control the remaining high block using only ∥u∥t . It does not apply to the
low-degree-input polynomial estimate used above.


9     Weak relaxation and estimation without matching
This section uses only the stationary floor and critical moment cap. It does not require exact
coordinate marginals. Normalize EhP h = 1, put ν = πµ with π = hg, and retain the actual
kernel K from Section 1. For real f set O = osc(f ) = max f − min f and
                                  1
       DK (f ) = ⟨f, (I − K)f ⟩ν = Em h(x)h(y)(f (x) − f (y))2 ,            m(x, y) = µ(x)P (x, y).
                                  2
Here m is a probability measure on pairs. Write DP for the same expression with the factor
h(x)h(y) removed. All constants below depend on the fixed noise and floor, and not on the
dimension or the potential. Within this section, N denotes the integer sample length, not the
weighting normalizer E(h/g) of Section 1; C and c below denote the local weak-Poincare constants,
not earlier matching or window constants.

9.1   An inverse edge moment and a weak Poincare inequality
Theorem 9.1. Assume h > 0, EhP h = 1, π ≥ b > 0, and Eπ s ≤ 2, where s = (1 + ρ)/(1 − ρ).
Define
                  1+ρ                       2ρ           1−a     1 + ρ2
             s′ =     , B = 21/s , a =            , p =        =        ,
                   2ρ                    (1 + ρ)2         a        2ρ
                                  ′                                                2
                C = B(1 − ρ)−1/s b−2a ,         c = C −1/a = b2 (1 − ρ)1+ρ 2−(1−ρ )/(2ρ) .
Then every real f , every ϵ > 0, and every integer n ≥ 0 satisfy

                                      Varν (f ) ≤ CDK (f )a O2(1−a) ,                                 (10)
                                                  −1 −p                 2
                                      Varν (f ) ≤ c    ϵ   DK (f ) + ϵO ,                             (11)
                                Varν (K n f ) ≤ O2 (1 + pcn)−1/p .                                    (12)

Proof. Let Q = P√ρ . Energy normalization gives ∥Qh∥2 = 1. Ordinary Boolean hypercontrac-
tivity, in the form Pθ : Lu → Lv for 1 < u ≤ v < ∞ when θ2 ≤ (u − 1)/(v − 1), gives ∥g∥R ≤ 1 for
R = 1 + 1/ρ, since g = Q(Qh). The original floor gives 1/h ≤ g/b, hence ∥1/h∥R ≤ b−1 . These
inverse moments are derived, not assumed.
    Set r0 = 1/ρ, w(x, y) = h(x)h(y), and v = h−r0 . A second use of hypercontractivity, Q :
L1+ρ → L2 , yields

                  Em w−r0 = ⟨v, P v⟩µ = ∥Qv∥22 ≤ ∥v∥21+ρ = ∥1/h∥2r
                                                                r0 (1+ρ) ≤ b
                                                                   0        −2r0
                                                                                 .

For O > 0, let z = (f (x) − f (y))2 /O2 ∈ [0, 1] and α = r0 /(1 + r0 ) = 1/(1 + ρ). Hölder’s inequality
gives
                       Em z ≤ (Em wz)α (Em w−r0 z)1−α ≤ (2DK (f )/O2 )α b−2α .

                                                      15
Consequently
                    DP (f ) ≤ 2α−1 b−2α DK (f )α O2(1−α) ≤ b−2α DK (f )α O2(1−α) .
We deliberately discard a factor at most one. The Walsh spectrum gives Varµ (f ) ≤ DP (f )/(1−ρ).
For mf = Eµ f , we have |f − mf | ≤ O and
                                                                 ′   1/s′                       ′
             Varν (f ) ≤ Eµ π(f − mf )2 ≤ B Eµ |f − mf |2s                   ≤ BO2/s Varµ (f )1/s .

Combining proves (10), since a = α/s′ . For y = Varν (f )/O2 and e = DK (f )/O2 , it says e ≥ cy 1+p .
If y ≤ ϵ, (11) is immediate; otherwise y ≤ c−1 ϵ−p e, proving the same assertion.
    For completeness, the discrete-time decay is derived directly. The conjugate M√h/g P M√h/g is
positive semidefinite, so the self-adjoint Markov operator K has spectrum in [0, 1]. For F = K n f
this implies
                        Varν (F ) − Varν (KF ) = ⟨F, (I − K 2 )F ⟩ν ≥ DK (F ).
Also osc(K n f ) ≤ O. Therefore yn = Varν (K n f )/O2 obeys yn+1 ≤ yn − cyn1+p . For positive
consecutive terms, convexity of t 7→ t−p gives
                               −p
                              yn+1 − yn−p ≥ p(yn − yn+1 )yn−p−1 ≥ pc.

Summing and using y0 ≤ 1 proves (12). If a variance vanishes, all subsequent variances vanish; if
O = 0, all statements are immediate.

9.2   Summable relaxation at noise one half
The floor identity used in Section 3 supplies a stronger inverse moment at ρ = 1/2. One additional
positive-moment smoothing step then makes the bounded-observable decay summable.

Theorem 9.2. Assume ρ = 1/2, h > 0, EhP h = 1, π ≥ b > 0 and Eπ 3 ≤ 2. Put

                               c∗ = b4 2−61/24 ,        CF = 3 + 32/c∗ .

For all real f and integers n ≥ 0,
                                                                        −8/7
                               Varν (K n f ) ≤ O2 1 + (7/8)c∗ n                 .

For the stationary chain (Xi ) with transition K and all integers N ≥ 1,
                                         −1
                                      1 NX
                                                         !
                                                                 CF O 2
                                  Var       f (Xi )          ≤          .
                                      N i=0                       N

Proof. The floor gives h ≥ b/g, hence g ≥ bP (1/g) ≥ b/(P g) by rowwise Jensen. Thus 1/g ≤
P g/b. Since P g = Pρ3/2 Qh and ∥Qh∥2 = 1, hypercontractivity at ρ = 1/2 gives ∥P g∥9 ≤ 1 and
∥1/g∥9 ≤ b−1 . With B = 21/3 , Hölder and h = π/g yield ∥h∥9/4 ≤ B/b. Hypercontractivity
P1/2 : L9/4 → L6 gives ∥g∥6 ≤ B/b. The original floor again implies

                                       ∥1/h∥6 ≤ H := B/b2 .

In the notation of the preceding proof, now set v = h−4 . Then

                            Em w−4 = ∥Qv∥22 ≤ ∥v∥23/2 = ∥1/h∥86 ≤ H 8 .

                                                   16
Repeating the edge comparison with α = 4/5, and again discarding 2α−1 ≤ 1, gives

                                        DP (f ) ≤ H 8/5 DK (f )4/5 O2/5 .

Use the noise gap 1/2 and the variance transfer with s′ = 3/2 to obtain

                      Varν (f ) ≤ C∗ DK (f )8/15 O14/15 ,                   C∗ = B 22/3 H 16/15 .
       −15/8
Here C∗      = b4 2−61/24 = c∗ . The discrete recursion in the preceding proof applies with a∗ =
8/15 and p∗ = (1 − a∗ )/a∗ = 7/8, proving the claimed decay.
   Center f by its ν-mean and let γj = Cov(f (X0 ), f (Xj )) = ⟨f, K j f ⟩ν . Positivity and self-
adjointness give
                                 0 ≤ γ2m+1 ≤ γ2m = Varν (K m f ).
With A = (7/8)c∗ , the decreasing bound satisfies
                                                    Z ∞
                            (1 + Am)−8/7 ≤                (1 + Ax)−8/7 dx = 7/A = 8/c∗ .
                      X

                      m≥1                             0


Consequently          X                               X
                            γj ≤ Varν (f ) + 2             Varν (K m f ) ≤ O2 (1 + 16/c∗ ).
                      j≥1                            m≥1

The exact finite-N covariance identity now gives
             −1                                PN −1
          1 NX
                            !
                                                   j=1 (N − j)γj
                                                                                                    2
                                                                                       P
                                    N γ0 + 2                       γ0 + 2 j≥1 γj   (3 + 32/c∗ )O
      Var       f (Xi )         =                    2
                                                                 ≤               ≤                      .
          N i=0                                    N                     N               N

No conditional summation or continuous-time substitution is used.

9.3   Uniform initialization and mean-square error
Corollary 9.3. Under the assumptions of Theorem 9.2, start the actual K-chain in the uniform
reference law µ. For every real f and integer N ≥ 1,
                                       
                                                  N −1
                                                                            !2 
                                           1      X                                    CF O 2
                             Eµ-start           f (Xi ) − ν(f )              ≤              .
                                           N i=0                                        bN

This is a mean-square error bound including any initialization bias.

Proof. For an initial law η, the finite-path likelihood ratio relative to the stationary path is exactly
                                           (N )
                                       dPη                                  η(x0 )
                                         (N )
                                                  (x0 , . . . , xN −1 ) =          .
                                       dPν                                  ν(x0 )

The transition factors cancel. Hence η ≤ M ν implies Eη Z ≤ M Eν Z for every nonnegative path
functional Z. For η = µ, the original floor supplies µ(x)/ν(x) = 1/π(x) ≤ 1/b. Apply this
comparison to the squared error and use Theorem 9.2; stationarity makes its variance equal to
its mean-square error about ν(f ).



                                                            17
   The required initial-density domination is proved from the floor for this specific initialization.
No dimension-free domination is asserted for a fixed starting vertex. The uniform-start estimator
need not be unbiased or stationary. No concentration inequality or optimality claim is made.
   These theorems concern oscillation-controlled observables. In particular, (10) applied to a
nonconstant eigenfunction only gives
                                                          p
                                            Varν (f )
                                                
                                      1−λ≥c                    .
                                            osc(f )2
The ratio may be arbitrarily small along a dimension-varying family. Thus these results do not
establish a dimension-uniform L2 (ν) gap, do not bound the killed operator of Section 8, and do
not remove matching from the stronger open spectral question.


10     Full gaps from a positive potential background
A fixed lower bound on the normalized potential allows arbitrary upper heights and arbitrarily
many values. We first prove this general sufficient condition and then recover the two-level class
from its stationary floor. The lower potential bound is not derived here for arbitrary potentials
satisfying the original stationary hypotheses.
Theorem 10.1. Fix 0 < ρ < 1 and 0 < a ≤ 1. Let h ≥ a on {−1, 1}L , L ≥ 1, normalize
EhPρ h = 1, and assume Eπ s ≤ 2, where π = hPρ h and s = (1 + ρ)/(1 − ρ). Then the actual
Doob kernel has
                                 gap(K) ≥ GJ (ρ, a) > 0
uniformly in L and h. No matching or upper bound on h is needed. The following explicit
constants suffice; all symbols are local:
                                                                        c
           s′ = s/(s − 1),       B = 21/s ,  c = a/2,    M = B/a,   η=     ,
                                                                       c+M
                                       (          !s )
                                              η2c
                               t = min 2−s ,           ,  ϵ = c2 t,
                                             4M
                                ′
                    c2 (1 − ρ)ϵs −1
               γ=                   ,   Φ∗ = min{η/2, γ},          GJ (ρ, a) = Φ2∗ /4.
                        2s′ B 2s′
The constants are positive and deliberately conservative.
Proof. Put P = Pρ , Q = P√ρ , g = P h, and ν = πµ. Since g ≥ a, the cap gives ∥h∥s ≤ B/a = M .
Write h = c + z, so z ≥ c > 0, ∥z∥s ≤ M , and g = c + P z.

Critical multiplication and the actual denominator. Ordinary hypercontractivity [10]
and 1/(1 + ρ) = 1/2 + 1/(2s) yield
                                    √                         √
                      ∥QM√z f ∥2 ≤ ∥ zf ∥1+ρ ≤ ∥z∥s1/2 ∥f ∥2 ≤ M ∥f ∥2 .

The same inequality for a function supported on C gives ∥Q1C ∥2→2 ≤ µ(C)1/(2s) . All operator
norms in this proof, except those explicitly assigned to L2 (ν), use L2 (µ) or its orthogonal direct
sum. Set A = M√z P M√z and R = MP z . Then 0 ⪯ A ⪯ M I. Reversibility also gives the exact
identity
                                                                              !2
                               1X                             v(x)      v(y)
              ⟨v, (R − A)v⟩µ =       µ(x)P (x, y)z(x)z(y) p         −p            ≥ 0.
                               2 x,y                           z(x)      z(y)

                                                 18
Thus A ⪯ R. With θ = c/(c + M ) = η and λ = M/(c + M ), convex combination gives

                                   A ⪯ θM I + (1 − θ)R = λ(cI + R).

Congruence and g = c + P z prove

                                         M1/√g AM1/√g ⪯ (1 − η)I.                                   (13)

This uses the nonconstant denominator exactly and assumes no upper bound on z.

An exact two-component representation. Let S = M√h/g P M√h/g , the conjugate of K
                    √
by the isometry f 7→ πf from L2 (ν) to L2 (µ). Define
                                        q              q            
                             Wf =              c/h f,       z/h f ,          W ∗ W = I.

For T = W SW ∗ , direct multiplication gives

                            Tij = M√h /g P M√h /g ,                      h0 = c,    h1 = z.
                                           i                j


In particular T11 is the operator in (13). Both W and W ∗ commute with the same set restriction
on each component. Hence the compressions satisfy

                              SCC = WC∗ TCC WC ,                     ∥SCC ∥ ≤ ∥TCC ∥.               (14)

The larger space supplies an exact identity for the original operator, not a new assumption or a
substitute chain.
                                   p
Small cuts.       The multiplier       c/g is at most one. Therefore

                       ∥T00,CC ∥ ≤ ∥1C P 1C ∥ ≤ µ(C)1/s ,                   ∥T11,CC ∥ ≤ 1 − η.

For the cross block factor P = Q2 . Bound the left diagonal multiplier by one and the far-right
                                          √
g −1/2 by c−1/2 . The latter commutes with z and 1C , without being moved through Q. Thus
                                                                             q
                       ∥T01,CC ∥ ≤ c−1/2 ∥1C Q∥ ∥QM√z 1C ∥ ≤                     M/c µ(C)1/(2s) .

If 0 < ν(C) ≤ ϵ, then π = hg ≥ a2 ≥ c2 gives µ(C) ≤ t. The diagonal blocks are bounded by
1/2 and 1 − η, respectively, while the cross block is bounded by η/2. Since 0 < η < 1/2, the
block-diagonal part has norm at most 1−η. The self-adjoint off-diagonal part has norm ∥T01,CC ∥,
so ∥TCC ∥ ≤ 1 − η/2.
    Define the actual outward stationary flow
                                         X
                          Fh (C) =                 µ(x)P (x, y)h(x)h(y) = DK (1C ).
                                       x∈C, y ∈C
                                              /
             √
The vector       π 1C has squared norm ν(C). Using (14) and conjugacy yields

                             Fh (C) = ν(C) − ⟨1C , K1C ⟩ν ≥ (η/2)ν(C).                              (15)

Every such cut is covered, regardless of the values of h within it.

                                                                19
Remaining cuts and the full gap. For ϵ ≤ ν(C) ≤ 1/2, the actual edge measure and h ≥ c
give
                     Fh (C) ≥ c2 DP (1C ) ≥ c2 (1 − ρ)µ(C)µ(C c ).
                                   ′
The cap implies ν(E) ≤ Bµ(E)1/s for every E. Hence
                                              ′                           ′
                           µ(C) ≥ (ν(C)/B)s ,          µ(C c ) ≥ (1/(2B))s ,

and consequently
                                                             ′
                                 Fh (C)   c2 (1 − ρ)ν(C)s −1
                                        ≥                    ≥ γ.
                                 ν(C)           2s′ B 2s′
Together with (15), these bounds imply Φ(K) ≥ Φ∗ for conductance Φ(K) = min0<ν(C)≤1/2 Fh (C)/ν(C).
The lazy reversible Cheeger theorem [13], applied to K = (I + K)/2, gives

                          gap(K)/2 ≥ 21 (Φ(K)/2)2 ,        gap(K) ≥ Φ2∗ /4.

All transformations are valid also for constant h and a = 1, because z ≥ c > 0. This proves the
theorem.

Corollary 10.2. Fix 0 < ρ < 1 and 0 < b < 1. Every normalized positive potential taking at
most two values and satisfying π ≥ b and Eπ s ≤ 2 obeys gap(K) ≥ GJ (ρ, b/2) > 0, without
matching or any additional restriction on the level ratio or geometry.
Proof. For a constant potential normalization gives h = 1. Otherwise let h = M0 on a set of
mass α ∈ (0, 1) and h = m0 < M0 on its complement. The constant Fourier component gives
Eh ≤ 1. Integrating the floor on the low set yields m0 ≥ b(1 − α). Since g ≤ M0 , the floor
there also gives m0 M0 ≥ b, while M0 α ≤ Eh ≤ 1 implies m0 ≥ bα. Thus h ≥ m0 ≥ b/2. Apply
Theorem 10.1.

    This recovers the two-level conclusion, with possibly weaker constants than the separately
preserved direct proof. Its geometric restriction has been replaced in the broader theorem by the
explicit sufficient condition h ≥ a; that condition is derived here only for the stated two-level
class.
    For any normalized family at fixed ρ with EπLs ≤ 2, a collapsing gap necessarily implies
minx hL (x) → 0. Otherwise a subsequence has a fixed positive minimum, contradicting Theo-
rem 10.1. This is a necessary mechanism, not the construction of such a family. The original
stationary floor and matching have not been shown to exclude it.

10.1    The stationary floor does not supply a potential minimum
The extra minimum in Theorem 10.1 cannot be derived from the stationary floor and cap alone,
even for three-level potentials. The following construction does not impose exact matching.
Proposition 10.3. Fix 0 < ρ < 1, 0 < b < 1 and any finite s > 1. There are energy-normalized
positive potentials hL such that πL = hL Pρ hL ≥ b and

                    ∥πL − 1∥s −→ 0,       ∥hL − 1∥2s −→ 0,          min hL −→ 0.

For all sufficiently large L, the potential has exactly three values, EπLs ≤ 2, and (Pρ hL )(x0 ) → ∞
at x0 = (1, . . . , 1). These are actual Doob kernels. No exact stationary matching is imposed here;
its critical-exponent spectral behavior is established below in Theorem 10.7.

                                                  20
Proof. Write p = (1 − ρ)/2 and q = (p + 1/2)/2, so p < q < 1/2. For Hamming distance D, set

     A = {y : 1 ≤ D(x0 , y) ≤ qL},     α = µ(A),       δ = 2−L ,   r = Pρ (x0 , A),   u = (1 − p)L .

The binomial distributions of D under µ and Pρ (x0 , ·), respectively, and Chebyshev’s inequality
give
                              1                                p(1 − p)
                    α≤             2
                                     → 0,     1−r ≤u+                    → 0.
                        4L(1/2 − q)                           L(q − p)2
For large L, A is nonempty and its complement contains points besides x0 . Also Pρ (y, x0 ) ≤ u
for every y, since p < 1/2. Put M = α−1/(4s) > 1 and β = (1 + b)/2. There is a unique 0 < t < 1
satisfying
                                 t(ut + M r + 1 − u − r) = β :
the left side is strictly increasing from zero, and at t = 1 it equals 1+(M −1)r > 1 > β. Moreover
t ≤ β/(M r) → 0. Define      √ H = t at x0 , H = M on A, and H = 1 elsewhere. With P = Pρ ,
Z = EHP H and h = H/ Z, we have H(x0 )(P H)(x0 ) = β and EhP h = 1 exactly. Positivity of
P and 1 − 1{x0 } ≤ H ≤ 1 + M 1A imply

             1 − 2δ + δu ≤ Z ≤ 1 + 2M α + M 2 ⟨1A , P 1A ⟩ ≤ 1 + 2M α + M 2 α −→ 1.

Outside x0 , H ≥ 1 and P H ≥ 1 − P (·, x0 ) ≥ 1 − u. Hence π = HP H/Z ≥ min{β, 1 − u}/Z ≥ b
eventually.
   For R = HP H, the same upper bound on H gives

                               R ≤ 1 + M 1A + M P 1A + M 2 1A P 1A .

Jensen’s inequality and invariance of µ give ∥P 1A ∥s ≤ α1/s ; also P 1A ≤ 1. Consequently

                    ∥(R − 1)+ ∥s ≤ 2M α1/s + M 2 α1/s = 2α3/(4s) + α1/(2s) → 0.

The lower bound outside x0 and R(x0 ) = β give ∥(1 − R)+ ∥s ≤ u + (1 − β)δ 1/s → 0. Thus
∥R − 1∥s → 0, and normalization yields ∥π − 1∥s → 0 and Eπ s → 1. Furthermore

                     ∥H − 1∥2s             2s          2s
                            2s = α(M − 1) + δ(1 − t) ≤ α
                                                              1/2
                                                                  + δ → 0.
                                                √                             √
It follows that ∥h − 1∥2s → 0 while min h = t/ Z → 0 and (P h)(x0 ) = β/(t Z) → ∞. Fill
any remaining small dimensions with h = 1. The actual kernel K(x, y) = P (x, y)h(y)/(P h)(x) is
stochastic, and µ(x)π(x)K(x, y) = µ(x)P (x, y)h(x)h(y) proves reversibility.

    For |f | ≤ 1, the construction gives |EπL f − Ef | ≤ ∥πL − 1∥1 → 0, uniformly over such tests.
This includes approximate marginal matching of every order, but no asymptotic error is set equal
to zero. The original question requires exact labelled matching. Vanishing minima are a necessary
condition for collapse supplied by Theorem 10.1, not a sufficient one; Proposition 10.3 supplies
no gap-collapse example. The construction uses classical binomial estimates and elementary
normalization. Its role here is to close this particular failed bridge; global priority and significance
are not established.




                                                  21
10.2    Exact matching does not restore the potential minimum
The approximate matching in Proposition 10.3 can be corrected exactly while preserving its ex-
ceptional small potential value. We first establish the needed finite-dimensional stability estimate.
Positive matrix scaling is classical; see the setup in Lee’s lecture [1]. The arguments needed here
are included in full.

Lemma 10.4. Let P be a strictly positive symmetric stochastic matrix on n points with uniform
probability µ. Every strictly positive mean-one density w has a unique positive solution of hP h =
w. If P is also positive semidefinite, and wτ = w0 + τ e ≥ b0 > 0 for 0 ≤ τ ≤ 1 with Ee = 0, the
corresponding solutions satisfy

                                                   ⌈ 21 log2 (n/b0 )⌉ + 2
                          ∥ log h1 − log h0 ∥∞ ≤                          ∥e∥∞ .
                                                              2b0
Proof. For v ∈ Rn , consider
                                   1X                          X
                        Fw (v) =         µ(x)P (x, y)evx +vy −   µ(x)w(x)vx .
                                   2 x,y                       x

The diagonal exponential terms make the Hessian positive definite; all other exponential terms
are convex. Thus Fw is strictly convex. Writing m = maxx vx and d = 21 minx µ(x)P (x, x) > 0,
we have Fw (v) ≥ de2m − m, because
                                        P
                                           µw = 1. Every sublevel set therefore has its maximum
coordinate bounded above. If any coordinate tends to −∞ while all coordinates are bounded
above, its strictly positive linear weight forces Fw → ∞. Thus sublevel sets are bounded, and a
unique minimizer exists. Its stationary equation is evx (P ev )(x) = w(x), proving existence and
uniqueness with h = ev . The positive definite Hessian and the implicit function theorem give
smooth dependence along the path wτ ; existence at every parameter and uniqueness join the
local solutions.
    For the actual kernel K(x, y) = P (x, y)h(y)/(P h)(x) with stationary ν = wµ, positive
                                                                                              −1/2
semidefiniteness of P implies that the spectrum of K lies in [0, 1]. Let ν∗ = minx ν(x), A = ν∗ ,
m = ⌈log2 A⌉ and T = (I − K)/2. The absolute row sum of T is 1 − K(x, x) ≤ 1, whereas its
L2 (ν) operator norm is at most 1/2. Hence

                                     ∥T j ∥∞→∞ ≤ min{1, A2−j }.
                                                            √
Here the second estimate follows from |f (x)| ≤ ∥f ∥L2 (ν) / ν∗ . The convergent series and its norm
bound give
                                                                                  
                                                               ∞
                     1X j                               1                  m+2
         (I + K)−1 =                   ∥(I + K)−1 ∥∞→∞ ≤ m +     A2−j  ≤
                                                              X
                           T ,                                                 .
                     2 j≥0                              2     j=m
                                                                            2

No Markov property of T or gap bound at the top of the spectrum is assumed. Differentiating
the defining pointwise equation gives
                                    d                    d
                                      log wτ = (I + Kτ ) log hτ .
                                   dτ                   dτ
Along the path ν∗ ≥ b0 /n and ∥d log wτ /dτ ∥∞ ≤ ∥e∥∞ /b0 . Integrating proves the displayed
estimate.

                                                   22
Proposition 10.5. For every fixed 0 < ρ < 1, 0 < b < 1 and C > 0, there is a sequence satisfying
all of (1), with energy normalization EhL Pρ hL = 1, such that, for s = (1 + ρ)/(1 − ρ),
          ∥πL − 1∥s → 0,       ∥hL − 1∥2s → 0,               hL (x0 ) → 0,       (Pρ hL )(x0 ) → ∞.
In particular min hL → 0. Theorem 10.7 classifies the actual gap of this family. Preservation of
three potential values is not asserted.
Proof. Apply Proposition 10.3 with the larger stationary floor b1 = (1 + b)/2, using its notation
π, h, R, Z, α, M, u, δ and β = (1 + b1 )/2. Its rare-set probability is exponentially small. Indeed,
exponential Markov applied to D ∼ Bin(L, 1/2) yields
                                                                     −λ L
                                                         "             #
                                                             λq 1 + e
                               α ≤ Pr(D ≤ qL) ≤ e                            .
                                                                   2
The bracket is one at λ = 0 and its logarithmic derivative there is q − 1/2 < 0; choose a fixed
small λ > 0 making it a ∈ (0, 1). The preceding proof also gives
        ∥R − 1∥1 ≤ 2M α + M 2 α + u + (1 − β)δ = 2α1−1/(4s) + α1−1/(2s) + u + (1 − β)δ.
Every term decays exponentially. Since |Z − 1| ≤ ∥R − 1∥1 and Z → 1, there are fixed A1 , c > 0
with ∥π − 1∥1 ≤ A1 e−cL for all sufficiently large L.
   Put k = kL as in (1), and subtract the nonconstant low-degree Fourier projection:
                                     X
                           eL = −             (EπχS )χS ,         wL = π + eL .
                                    1≤|S|≤k

Each coefficient has magnitude
                      √        at most ∥π − 1∥1 . The number of terms is at most kLk eventually,
whose logarithm is O( L log L) = o(L). Consequently
                            ϵL := ∥eL ∥∞ ≤ kLk A1 e−cL ,               LϵL → 0.
Orthogonality gives EwL = 1 and EwL χS = 0 for every 1 ≤ |S| ≤ k exactly. Along π + τ eL , the
floor is at least b1 − ϵL ≥ b eventually. Also ∥wL − 1∥s ≤ ∥π − 1∥s + ϵL → 0, so its moment is
eventually at most two.
    The noise matrix is strictly positive and positive definite, with Walsh eigenvalues ρ|S| > 0.
Lemma 10.4 provides a positive h  e L satisfying h
                                                 e L Pρ h
                                                        e L = wL , with

                                                  ⌈(L + log2 (1/b))/2⌉ + 2
                    ηL := ∥ log(h
                                e L /hL )∥∞ ≤                              ϵL → 0.
                                                             2b
Thus e−ηL hL ≤ he L ≤ eηL hL . The vanishing value at x0 and the divergent value of Pρ hL there
persist. Moreover
                                e L − hL ∥2s ≤ (eηL − 1)∥hL ∥2s → 0,
                               ∥h
so the potential norm convergence persists as well. Its energy is EwL = 1, and its actual stationary
density is exactly wL . Use h
                            e L = 1 in the finitely many earlier dimensions and rename the resulting
sequence hL .
    This refutes the proposed implication from the full original stationary hypotheses to a uniform
normalized potential minimum. It does not refute the spectral-gap question: the necessary
condition for collapse from Theorem 10.1 has been attained, not shown sufficient. Further full-
gap arguments must control the actual chain without deducing such a minimum. The finite
reconstruction is an analytic existence proof, not an executed matrix-scaling certificate; no claim
of global priority for its stability specialization is made.

                                                    23
10.3    The vanishing-minimum family retains the noise gap
The exact-matching construction above can be classified spectrally. Its small potential value does
not produce a collapsing gap. The proof uses an estimate for the actual ratio h/(P h), rather
than transferring stationary moment convergence directly to the spectrum.

Lemma 10.6. Put s = (1 + ρ)/(1 − ρ) and Q = P√ρ on the Boolean cube. For every real function
v and every positive potential H, put U = H/(P H). Then

                   ∥QMv Q∥2→2 ≤ ∥v∥s ,        | gap(KH ) − (1 − ρ)| ≤ ∥U − 1∥s .

More generally, every ordered eigenvalue of KH differs from the corresponding ordered eigenvalue
of P by at most ∥U − 1∥s .

Proof. The conjugate exponent is s′ = (1 + ρ)/(2ρ), so 2s′ = 1 + 1/ρ. Classical  p Boolean hyper-
                                                                           √
contractivity gives ∥Qf ∥2s′ ≤ ∥f ∥2 : its noise condition is the equality ρ = (2 − 1)/(2s′ − 1);
see Chapter 10.1 of [6]. Holder’s inequality with exponents s, 2s′ , 2s′ therefore gives

                      |⟨f, QMv Qg⟩| ≤ ∥v∥s ∥Qf ∥2s′ ∥Qg∥2s′ ≤ ∥v∥s ∥f ∥2 ∥g∥2 .

For the spectral assertion, the actual reversible conjugate of KH is S = M√U P M√U . Set X =
M√U Q. Then S = XX ∗ and T = X ∗ X = QMU Q. Both factors of X are invertible: U > 0 and
the Walsh eigenvalues of Q are positive. Thus X −1 SX = T and T has the full spectrum of the
actual chain. The first estimate yields

                           ∥T − P ∥2→2 = ∥QMU −1 Q∥2→2 ≤ ∥U − 1∥s .

The min–max principle compares every ordered eigenvalue of the two self-adjoint matrices. For
L ≥ 1, the second eigenvalue of P is ρ, proving the gap assertion, including its multiplicity.

Theorem 10.7. Fix 0 < ρ < 1, 0 < b < 1 and C > 0. The exactly matched family h
                                                                             e L constructed
in the proof of Proposition 10.5 satisfies

                                 | gap(Keh ) − (1 − ρ)| ≤ C1 e−c1 L
                                          L

for all sufficiently large L, with constants C1 < ∞ and c1 > 0 depending only on the fixed
parameters and construction choices. It satisfies all of (1), although its normalized minimum
tends to zero and (P h e L )(x0 ) tends to infinity.

Proof. Use the precursor H from Proposition 10.3, with s = (1 + ρ)/(1 − ρ), and retain its
α, δ, u, M, t. Since H ≥ 1 − 1{x0 } and P (y, x0 ) ≤ u for every y,

                                      G := P H ≥ 1 − u > 0

at every vertex, including x0 . No positive lower bound on t is needed. The disjoint exceptional
supports and Ls contraction of P give, with dL = α3/(4s) + δ 1/s ,

               ∥H − 1∥s ≤ α1/s (M − 1) + δ 1/s (1 − t) ≤ dL ,      ∥H − G∥s ≤ 2dL .

Consequently the scale-invariant ratio satisfies
                                                           2dL
                           ∥U − 1∥s = ∥(H − G)/G∥s ≤           =: ∆L .
                                                           1−u

                                                   24
Energy normalization does not change U . For the exact correction, Proposition 10.5 proves

                                         ⌈(L + log2 (1/b))/2⌉ + 2
          ηL = ∥ log(h
                     e L /hL )∥∞ ≤                                ϵL ,       ϵL ≤ kL LkL A1 e−cL .
                                                    2b
Positivity of P yields the corresponding multiplicative bounds for the denominators, hence

                                                           h
                                                           eL
                                    e−2ηL U ≤ U
                                              e :=              ≤ e2ηL U.
                                                         Ph
                                                          eL

Since ∥U ∥s ≤ 1 + ∆L , it follows that
                    e − 1∥s ≤ ∆L + (e2ηL − 1)(1 + ∆L ) = e2ηL ∆L + e2ηL − 1.
                   ∥U                                                                                (16)

The preceding construction proves α ≤ aL for fixed a < 1; also u = ((1 + ρ)/2)L and δ = 2−L .
Finally log(kL LkL ) = o(L), so ϵL ≤ exp(−cL + o(L)). This is an upper bound, with no lower
bound on ϵL asserted or needed. The factor multiplying ϵL in the estimate for ηL is O(L). Thus
the right side of (16) is bounded by C1 e−c1 L for a possibly smaller positive rate c1 . Lemma 10.6
now gives the asserted actual-gap estimate. The finitely many dimensions filled with h = 1 do
not affect the limit.

    The classical sandwich estimate supplies no general bound on ∥h/(P h)−1∥s from (1). Here the
all-vertex denominator estimate is proved directly for the particular precursor, and the nonlinear
reconstruction has proved multiplicative stability. This closes the constructed vanishing-minimum
family as a candidate collapse mechanism while preserving its counterexample to deriving a
potential minimum. The unrestricted stationary-gap question remains open.


11     Vanishing denominators without spectral collapse
The preceding family has small potential values but a uniformly positive noise denominator.
We next rule out deriving a positive denominator floor from the original hypotheses. The same
construction shows why excluding individual points with a large ratio is too strong a proposed
remedy.

Theorem 11.1. Fix 0 < ρ, b < 1 and C > 0. There are energy-normalized positive potentials h
                                                                                          eL
satisfying all of (1) such that, at the all-plus vertex x0 , for a constant ε > 0,
                     e L (x0 ) ∼ eεL ,
                     h                          e L )(x0 ) ∼ e−εL ,
                                             (P h                        eL (x0 ) −→ 1.
                                                                         π

Thus UeL (x0 ) ∼ e2εL , where U eL = h        e L ). Nevertheless there are constants A < ∞, a > 0
                                      e L /(P h
such that, for all sufficiently large L,

            ∥π
             eL − 1∥s + U
                        eL − 1           ≤ Ae−aL ,          max |λj (Keh ) − λj (P )| ≤ Ae−aL .
                                     s                     1≤j≤2L        L



Eigenvalues are ordered with multiplicities. In particular the full gap tends to 1 − ρ. Constants
and the eventual threshold may depend on the fixed parameters; no uniformity as ρ approaches
its endpoints is claimed.




                                                      25
Proof. We use the classical Bernoulli concentration bound, including unequal parameters: if S
sums L independent Bernoulli variables, then
                                                                           2
                    Pr(S − ES ≥ tL), Pr(S − ES ≤ −tL) ≤ e−2t L                     (t > 0).

Here is the needed proof. The log moment-generating function of a centered Bernoulli variable has
value and first derivative zero at zero; its second derivative is the variance of a tilted Bernoulli law,
at most 1/4. Integrating twice bounds it by λ2 /8 for every real λ. Independence and exponential
Markov at λ = ±4t give the two bounds. No equal-parameter assumption is used.
    Put
          1−ρ                      1 − ρ2               1+b
     p=       ,    q = p + ρp =           ,    a0 =         ,     δ = min{ρp/16, ρ2 /16},           r0 = 2δ/ρ.
           2                         2                   2
Let d(x) be the Hamming distance from x0 and define

                                    BL = {x : |d(x)/L − p| ≤ δ},
                                    AL = {x : |d(x)/L − q| ≤ 2δ},
                                    DL = {x : (P 1BL )(x) > 1 − a0 }.

In this proof DL is a set. We have r0 ≤ p/8, q − p ≥ 16δ and 1/2 − q ≥ 8δ. Thus AL and BL are
disjoint. Conditional on x, the next noise step has independent coordinate flips and

                                          Ex d(Y ) = pL + ρd(x).

For x ∈ BL this mean lies between (q − ρδ)L and (q + ρδ)L, so
                                                2                                    2
                       P (x, AL ) ≥ 1 − 2e−2δ L ,            P (x0 , BL ) ≥ 1 − 2e−2δ L .

If d(x)/L ≥ r0 , the mean is at least (p+2δ)L and the upper boundary of BL is (p+δ)L. Therefore
                  2
P (x, BL ) ≤ e−2δ L . For all sufficiently large L,

                                     x0 ∈ DL ⊂ {x : d(x)/L < r0 }.

The last ball is disjoint from both shells, since r0 < p − δ.
   Choose the strictly positive constant

                                         2δ 2 , 2(p − r0 )2 , 2(q − 2δ − p)2 ,
                             (                                                              )
                   c = min                                                                      .
                               2(1/2 − q − 2δ)2 , 2(1/2 − p − δ)2 , 2(1/2 − r0 )2

Under uniform measure d(x) is binomial with mean L/2, whereas under P (x0 , ·) it is binomial
with mean pL. The concentration bounds and the containment of DL consequently give

                  µ(AL ), µ(BL ), µ(DL ) ≤ e−cL ,
                  P (x0 , AL ), P (x0 , DL ) ≤ e−cL ,
                               P (x0 , BLc ) ≤ 2e−cL ,          inf P (x, AL ) ≥ 1 − 2e−cL .                     (17)
                                                               x∈BL

These estimates include shell boundaries and the return to x0 .



                                                        26
   Set ε = c/(16s), M = eεL , and EL = AL ∪ DL . Define the actual potential and its product by
               
               M        on EL ,
               
                                                                                           √
          H=     M −1    on BL ,           G = P H,         R = HG,     Z = ER,       h = H/ Z.
               
               
               1        elsewhere,

Always M −1 ≤ H, G ≤ M . On EL , R ≥ 1. On BL , G ≥ M P 1AL , hence R ≥ 1 − 2e−cL ≥ a0
eventually. Outside EL ∪ BL , one has H = 1 and x ∈   / DL , whence G(x) ≥ 1 − P (x, BL ) ≥ a0 .
Thus R ≥ a0 at every vertex.
   At x0 ∈ DL , splitting the noise expectation over the three regions gives

                  G(x0 ) = M −1 P (x0 , BL ) + P (x0 , (BL ∪ EL )c ) + M P (x0 , EL ).

Consequently
                     P (x0 , BL ) ≤ M G(x0 ) ≤ 1 + 2M e−cL + 2M 2 e−cL −→ 1,
because 2ε < c. Hence G(x0 ) ∼ M −1 , R(x0 ) → 1, and H(x0 )/G(x0 ) ∼ M 2 .
   For finite r ≥ 1 write dr,L = ∥H − 1∥r . The support bounds in (17) imply

                        dr,L ≤ M (2e−cL )1/r + e−cL/r ,           ∥G − 1∥r ≤ dr,L .

The second inequality is noise contraction. Hölder therefore gives

                                ∥R − 1∥s ≤ d2s,L (1 + d2s,L ) + d2s,L .

Since ε < c/(2s), this error decays exponentially, as does |Z −1|. Thus π = R/Z has exponentially
small ∥π − 1∥s , Eπ s → 1, and eventually π ≥ b1 := (a0 + b)/2 > b. Normalization preserves
h(x0 ) ∼ M , (P h)(x0 ) ∼ M −1 and π(x0 ) → 1.
   Crucially, for U = H/G, use the proved dimension-dependent bound G ≥ M −1 , not a fixed
denominator floor. It gives

                            ∥U − 1∥s ≤ M ∥H − G∥s ≤ 2M ds,L
                                        ≤ 2 21/s e−(c/s−2ε)L + 2e−(c/s−ε)L .                      (18)

Both rates are positive. Lemma 10.6 controls the entire actual spectrum by this ratio error.
   It remains to impose exact matching. Subtract the finite Walsh sum
                                        X
                            eL = −               (EπχS )χS ,       π
                                                                   e = π + eL .
                                      1≤|S|≤kL


Each coefficient is at most ∥π − 1∥1 , and for all large L there are at most kL LkL = exp(o(L)) terms.
Therefore ξL = ∥eL ∥∞ is exponentially small after decreasing the positive rate. Orthogonality
gives exact mean one and all requested zero coefficients. The path π + τ eL has floor b eventually,
and ∥πe − 1∥s remains exponentially small, giving the eventual cap two.
    Lemma 10.4 reconstructs the unique positive h      e with hP
                                                              e h e=π e and gives

                                                      ⌈(L + log2 (1/b))/2⌉ + 2
                         ηL := log(h/h)
                                   e              ≤                            ξL .
                                            ∞                    2b



                                                       27
This is exponentially small. Positivity of P transfers the same multiplicative bounds to P h
                                                                                           e and
P h, preserving the pointwise asymptotics, including the exponentially small denominator. Also
e−2ηL U ≤ Ue ≤ e2ηL U , so
                               e − 1 ≤ e2ηL ∥U − 1∥ + e2ηL − 1.
                               U
                                          s             s

Combining this with (18) and Lemma 10.6 proves the claimed norm and full-spectrum bounds.
Polynomial factors and the subexponential Walsh count are absorbed by a smaller positive ex-
ponential rate. Fill all finitely many early dimensions with h
                                                             e = 1, preserving every original
constraint.

    Theorem 11.1 refutes a dimension-uniform positive P h floor and a uniform pointwise ceiling
for h/P h, even under exact matching. It does not refute an aggregate killed-return or cut-
flow estimate. Small denominators and large ratios at individual vertices coexist here with a
full spectrum approaching Boolean noise. The original gap question remains open; no original
hypothesis was removed.


12     Regularization and exact stationary matching
The noise formula of Definition 2.46 and Proposition 2.47 in [6] makes smoothing a natural
candidate operation. Smoothing the potential, however, does not commute with its nonlinear
stationary-density construction. The following statements separate a preserved inequality from
a failed exact equality.

Proposition 12.1. Let h > 0 satisfy EhP h = 1 and hP h ≥ b > 0. For 0 ≤ τ ≤ 1 put
                                                                      p
              Hτ = Pτ h,       Zτ = EHτ P Hτ ,            hτ = Hτ / Zτ ,          πτ = hτ P hτ .

Then πτ ≥ b for every τ . No marginal-matching or moment assumption is needed for this
assertion.

Proof. The noise kernels commute. Cauchy–Schwarz in each probability row of Pτ therefore gives
                                                       √    2
                          Hτ P Hτ = (Pτ h)Pτ (P h) ≥ Pτ hP h ≥ b.

By Walsh Parseval,
                                          ρ|S| τ 2|S| h(S)           ρ|S| h(S)
                                      X                          X
                                                           2                  2
                           0 < Zτ =                   b      ≤            b     = 1.
                                      S                          S

The constant-character multiplier is one, including at τ = 0. Dividing the pointwise inequality
by Zτ proves the result.

Theorem 12.2. Fix 0 < ρ < 1, 0 < b < 1, L ≥ 3 and 1 ≤ k ≤ L − 2, and put s = (1 + ρ)/(1 − ρ).
There is a positive potential h with EhP h = 1 such that its stationary density has exact uniform
labelled marginals through order k, while
                                               √
                             πτ ≥ b,    Eπτs ≤ 2 < 2 (0 ≤ τ ≤ 1).

For one specified coordinate j, the same potential satisfies Eπτ χ{j} ̸= 0 for every 0 < τ < 1. Thus
every nontrivial smoothing loses even a first marginal while the stationary floor and critical cap
survive for this constructed family.


                                                     28
                                                 / A, and put B = A ∪ {j}, α = ρm and
Proof. Choose A ⊆ [L] with m = |A| = k + 1 and j ∈
β = ρm+1 . Fix the dimension-independent number
                                             1 1 − b log 2
                                                              
                                     ϵ = min  ,     ,              >0
                                             8 4      64s

and define w = 1+ϵ(χA +χB ). This density has mean one and w ≥ 1−2ϵ ≥ max{3/4, (1+b)/2} >
b. Its only nonconstant Walsh coefficients are at A and B, whose degrees exceed k, so it has the
required labelled marginals. We next realize it as the stationary density of an actual positive
potential rather than treating the density and potential as independent.
    Under uniform input, y = χA and z = xj are independent uniform signs. Since their coordi-
nate sets are disjoint, Boolean ρ-noise induces on (y, z) the exact product kernel Q = Pα ⊗ Pρ .
In particular
                                   P [f (χA , xj )] = (Qf )(χA , xj )
for every function f on these four points. The eigenvalues of Q are 1, α, ρ, β; all entries are strictly
positive. Apply Lemma 10.4 on this four-point space to the path wt = 1 + tϵ(y + yz), 0 ≤ t ≤ 1.
It is bounded below by 1/2. The unique positive solutions gt Qgt = wt start from g0 = 1 and obey

                                ⌈ 12 log2 (4/(1/2))⌉ + 2                          log 2
                ∥ log g1 ∥∞ ≤                            ∥ϵ(y + yz)∥∞ = 8ϵ =: η ≤       .
                                           2(1/2)                                  8s

The inverse estimate uses four points, not 2L , and is uniform as α becomes small. The lift
h = g1 (χA , xj ) consequently satisfies hP h = w, EhP h = 1, and e−η ≤ h ≤ eη .
    Every Hτ =                                                   −2η ≤ Z ≤ e2η and π ≤ e4η . Thus
   s     4sη
                 √ Pτ h and P Hτ lies in the same interval, so e        τ            τ
Eπτ ≤ e      ≤ 2 for all τ . Proposition 12.1 supplies the floor for all τ . At τ = 1 these are the
original stationary density and its cap.
    Write the unique four-character expansion

                           h = c + dχ{j} + eχA + f χB ,         c = Eh > 0.

Equating the three indicated coefficients in hP h = w gives

                                       (1 + ρ)cd + (α + β)ef = 0,                                  (19)
                                       (1 + α)ce + (ρ + β)df = ϵ,                                  (20)
                                       (1 + β)cf + (ρ + α)de = ϵ.                                  (21)

If e = 0, equation (19) forces d = 0, contradicting (20). If f = 0, the same equation again forces
d = 0, contradicting (21). Hence ef ̸= 0. Now

                                Hτ = c + τ dχ{j} + τ m eχA + τ m+1 f χB .

Using (19) in the χ{j} coefficient of Hτ P Hτ proves the exact identity

                                                (α + β)ef 2m+1
                                   Eπτ χ{j} =            (τ    − τ ).                              (22)
                                                   Zτ
For 0 < τ < 1 this is nonzero, since m ≥ 2, ef ̸= 0 and α + β, Zτ > 0. No perturbative remainder
or numerical nonzero test is used. At τ = 0 the normalized density is uniform, and at τ = 1 it is
the original exactly matched density.

                                                    29
                                                   √
    For fixed C > 0, the required kL = min{L, ⌊C L⌋} eventually belongs to [1, L − 2]. Apply
the theorem in those dimensions and use h = 1 in the finitely many remaining dimensions. This
gives the claimed obstruction within the original growing matching regime. No uniform lower
bound on the magnitude of (22) is asserted: α tends to zero as kL grows. Exact matching is the
equality that fails. The constructed potentials have a fixed positive minimum, so they are not a
collapsing-gap family.
    The distinction between potential and density regularization is essential. For wτ = Pτ π,
stochasticity preserves mean one and the floor, Jensen’s inequality and invariance of µ give
Ewτs ≤ Eπ s , and the Walsh formula preserves every zero low-degree coefficient. Lemma 10.4 then
supplies the unique actual positive potential uτ with uτ P uτ = wτ . These elementary invariances
do not compare the gaps of Kh and Kuτ . A dimension-uniform spectral comparison under the
original hypotheses remains unproved; it cannot be replaced by assuming a positive minimum for
the reconstructed potential or a lower bound on P h.


13     Full spectrum after stationary-density regularization
We now control the reconstructed chain on the regularized side of the comparison left open in
Section 12. The result is uniform over every admissible input density; no code algebra or lower
bound for its potential is imposed. It does not compare the reconstructed chain back to the
original chain.
    Fix 0 < ρ, b < 1, and put s = (1 + ρ)/(1 − ρ) and B = 21/s . The constants in this section are
fixed before the dimension, density, matching order and smoothing parameter. Define

            q0 = 2ρ−2 + ρ−3 − 1,                                            Q∗ = 8s,
                      (                                )
                                    2Q2∗                                               σq/(σ + q) − 1
            σ = max       4s,                               ,          Fσ (q) = 1 +                   .
                              (1 − ρ4 )(q     0 − 1)                                         ρ4

Starting at q0 , set qn+1 = Fσ (qn ) only until its first crossing qn∗ ≥ Q∗ . Take n∗ = 0 if q0 ≥ Q∗ .
The proof below establishes that this crossing is finite. Set

             A∗ = b−1 (B/b)n∗ ,                                            C∗ = b−1 BA2∗ ,
                         √
             θin = min{1, s − 1},                                      θout = min{1, (s − 1)−1/2 },
                            (             s         )
                                              s−1                                   1
              τ∗ = 21 min    θin θout ,                 ,                   γ=          .
                                              σ−1                                2s − 1

In particular, τ∗ > 0 and τ∗ ≤ 1/2. For an integer k ≥ 0, write

               ek = Bρ(k+1)/2 ,           Ek = (2ek )γ (C∗ + B)1−γ + (B + 1)2−(k+1) + e2k .               (23)

Theorem 13.1 (Uniform full spectrum on the regularized side). Let L ≥ 1, 0 ≤ k ≤ L, and let
π be a positive mean-one density on the cube with

                        π ≥ b,            Eπ s ≤ 2,             EπχS = 0    (1 ≤ |S| ≤ k).

For every 0 ≤ τ ≤ τ∗ , put w = Pτ π. There is a unique positive u with uP u = w. The
actual Doob kernel Ku (x, y) = P (x, y)u(y)/(P u)(x) has stationary density w, which satisfies the



                                                                30
same floor, critical cap and exact matching conditions. Its eigenvalues, ordered decreasingly with
multiplicities, satisfy

              |λj (Ku ) − λj (P )| ≤ Ek       (1 ≤ j ≤ 2L ),          | gap(Ku ) − (1 − ρ)| ≤ Ek .

The error decays√exponentially in k, uniformly in L, π, τ for fixed ρ, b. At k = kL in (1) it decays
exponentially in L for each fixed C > 0.
Proof. Reconstruction and a derived stronger moment. Stochasticity, Jensen’s inequality and
the Walsh multipliers give Ew = 1, w ≥ b, Ews ≤ 2 and the same zero coefficients through
degree k. Lemma 10.4 supplies the unique positive solution of uP u = w, with EuP u = 1. Its
dimension-dependent stability estimate is not used here. Ordinary hypercontractivity [2, 6] and
τ 2 ≤ (s − 1)/(σ − 1) give
                                      ∥w∥σ ≤ ∥π∥s ≤ B.                                      (24)
This stronger norm bound is derived, not an additional premise. It does not assert Ewσ ≤ 2.
    A finite inverse-moment crossing. Put g = P u and Q = P√ρ . Then ∥Qu∥2 = 1 and ∥g∥R ≤ 1
for R = 1 + ρ−1 , by ordinary hypercontractivity applied to g = Q(Qu). The floor ug ≥ b gives
u−1 ≤ g/b, or ∥u∥−R ≥ b in generalized-mean notation. Reverse hypercontractivity, including
its negative-exponent range [2], applies since ρ2 = (1 + R)/(1 + q0 ). Thus g −1 q0 ≤ b−1 . All
functions are strictly positive on a finite space. The floor and rowwise Jensen also give

                              g ≥ bP (1/g) ≥ b/(P g),                g −1 ≤ P g/b.

If g −1 q ≤ Aq and q > σ/(σ − 1), Hölder with p = σq/(σ + q) > 1 gives ∥u∥p = ∥w/g∥p ≤ BAq .
Since P g = Pρ2 u, ordinary hypercontractivity then yields

                                          g −1                ≤ (B/b)Aq .                            (25)
                                                     Fσ (q)

This iteration uses the newly derived exponent σ, not the original critical exponent’s fixed-point
formula.
   For q0 ≤ q < Q∗ , direct algebra and the choice of σ give

                                            (1 − ρ4 )(q − 1) − q 2 /(σ + q)
                             Fσ (q) − q =
                                                          ρ4
                                            (1 − ρ4 )(q0 − 1)
                                          ≥                   =: d > 0.
                                                  2ρ4
Here q0 > 2, while σ ≥ 4s > 4, so every input before the first crossing satisfies q > σ/(σ − 1).
If q0 < Q∗ , absence of a crossing would give qn ≥ q0 + nd for all n, a contradiction. In fact
n∗ ≤ ⌈(Q∗ − q0 )/d⌉. If q0 ≥ Q∗ no step is needed. At the first crossing the last valid step has
already proved
                                  g −1    ≤ A∗ ,    qn∗ ≥ 8s.
                                               qn∗

No assertion about further iterates is required. For U = u/g = w/g 2 , N = EU and r = U/N ,
Hölder gives
                                          2
                ∥U ∥2s ≤ ∥w∥4s g −1            ≤ BA2∗ ,           ∥r∥2s ≤ C∗ ,       ∥w∥2s ≤ B,      (26)
                                          8s

where N ≥ b is justified independently in the next paragraph.

                                                          31
    Actual normalization and matching rigidity. Let a = Eu = Eg and v = 1 − a2 = ∥Qu − a∥22 .
The floor gives a ≥ bE(1/g) ≥ b/a, so a2 ≥ b. Cauchy–Schwarz under w dµ gives N = Ew (g −2 ) ≥
(Ew (g −1 ))2 = a2 . For the other bound, the reversible conjugate S = M√U P M√U has Perron
eigenvalue one and positive spectrum. With X = M√U Q, the matrices S = XX ∗ and T =
X ∗ X = QMU Q are similar because X is invertible. Thus ∥T ∥2→2 = 1 and testing at the unit
constant gives N ≤ 1. This proves b ≤ a2 ≤ N ≤ 1 without any perturbation estimate.
    For completeness, the matching argument of Lemma 3.2 can be used directly with exponent
                                                              ′                    √
σ. Since σ ′ < 2, the degree-> k part of g = Q(Qu) has Lσ norm at most ρ(k+1)/2 v. Exact
                                                    √
matching gives EwΠ≤k g = a, hence Ewg ≤ a + ek v. Cauchy–Schwarz under u dµ gives 1 =
                                                 √
(Eug)2 ≤ aEug 2 = aEwg. Consequently
                            √            v ≤ aek v, including v = 0, and a2 ≥ (1 + e2k )−1 . The
                  √
actual identity E rw = a/ N ≥ a yields
                        √        √      2
                            r−       w 2 ≤ 2(1 − a) ≤ e2k ,      ∥r − w∥1 ≤ 2ek .

Interpolation with (26) gives
                                                                           1
                        ∥r − w∥s ≤ (2ek )γ (C∗ + B)1−γ ,           γ=          .             (27)
                                                                        2s − 1
    Closeness to the constant and the full spectrum. Factor Pτ = Pθout Pβ Pθin , where β =
τ /(θin θout ) ≤ 1/2. The input map contracts Ls to L2 : use hypercontractivity if s < 2, and
the identity with norm monotonicity if s ≥ 2. The output contracts L2 to Ls : use hypercontrac-
tivity if s > 2, and the identity with norm monotonicity if s ≤ 2. The Fourier support of π − 1
lies above degree k, so the middle map contracts its L2 norm by β k+1 . Therefore

                                       ∥w − 1∥s ≤ (B + 1)2−(k+1) .

This also holds at τ = 0, where the mean-zero part vanishes. Using U − 1 = N (r − w) + N (w −
1) + (N − 1), N ≤ 1 and 1 − N ≤ e2k /(1 + e2k ) ≤ e2k gives ∥U − 1∥s ≤ Ek . The critical sandwich
estimate of Lemma 10.6 gives

                        ∥T − P ∥2→2 = ∥QMU −1 Q∥2→2 ≤ ∥U − 1∥s ≤ Ek .
                                               ′
Indeed, 2s′ = 1 + ρ−1 and Q : L2 → L2s is a contraction, so Hölder bounds |E(U − 1)(Qf )(Qℓ)|
by ∥U − 1∥s for arbitrary unit L2 functions. This controls the full operator. The self-adjoint
min–max principle compares every ordered eigenvalue of T and P ; the exact similarity above
identifies the spectrum of T with that of Ku . No uniform condition number for X is used. Since
λ2 (P ) = ρ for L ≥ 1, the gap bound follows. All three terms of (23) decay exponentially in k for
fixed ρ, b. At k = L the high-degree space is zero; at k = 0 the same argument uses mean one.
These endpoints do not require a separate assumption.

Proposition 13.2 (Fixed smoothing need not be a small density perturbation). Fix C > 0 and
0 ≤ τ < 1. There are energy-normalized positive potentials hL satisfying all of (1) such that

                                            ∥πL − Pτ πL ∥s −→ ε > 0.

Proof. Take ε = min{(1 − b)/2, (B − 1)/2} > 0. For all sufficiently large L, one has kL < L.
Set πL = 1 + εχ[L] in those dimensions. It has mean one, minimum at least (1 + b)/2 > b,
maximum at most (1 + B)/2 < B, and no nonconstant Fourier coefficients below degree L. In
particular EπLs < 2 and the required matching holds. Lemma 10.4 realizes it as hL P hL for a

                                                      32
positive energy-normalized potential. Use hL = 1 in the remaining finitely many dimensions.
Since |χ[L] | = 1,
                              ∥πL − Pτ πL ∥s = ε(1 − τ L ) −→ ε.


    This refutes only the uniformly vanishing Ls premise for a transfer argument. It does not
refute a spectral comparison: the parity family itself belongs to an already controlled code class.
Theorem 13.1 establishes the regularized spectrum on its specified interval, which excludes τ = 1.
Neither a comparison with the original spectrum nor an extension to every τ < 1 is inferred.


14     Failure of separate variance and form comparison
The regularized spectrum does not supply a uniform comparison of the stationary variances. The
obstruction below concerns actual chains, including their nonlinear reconstructed potentials. For
an energy-normalized positive potential v, write
                                 1     X
                        Ev (f ) = Ex∼µ   P (x, y)v(x)v(y)(f (x) − f (y))2 .
                                 2     y

This is the Dirichlet form of Kv in stationary measure vP v dµ.
Theorem 14.1 (Separate-comparison obstruction). Fix 0 < ρ, b < 1, C > 0, and 0 ≤ τ < 1.
There are positive energy-normalized potentials hL , uL , with

                             πL = hL P hL ,     wL = uL P uL = Pτ πL ,

both satisfying (1), and events AL , such that, for fL = 1AL ,

                             VarπL (fL )              EhL (fL )
                                         −→ ∞,                  −→ ∞.
                             VarwL (fL )              EuL (fL )
Nevertheless both indicator Rayleigh quotients tend to one, and both full-chain gaps tend to 1 − ρ.
The family can be chosen with ∥πL − wL ∥s → c > 0 and with πLs not uniformly integrable, despite
EπLs < 2.
Proof. Put B = 21/s and c = min{(1 − b)/2, (B − 1)/4} > 0. For all sufficiently large L, set

                    d = kL + 1,      n = ⌊L/d⌋,       p = 2−n ,    t = cp−1/s .

                                                            and set A =√{z1 = · · · = zn = 1}.
Take n disjoint blocks of size d, let zi be their parities, √
Remaining coordinates are unused. Thus µ(A) = p, d ∼ C L, and n ∼ L/C. Define

                                        π = 1 + t(1A − p).

It has mean one and π ≥ 1 − c > b. Moreover

                    ∥π∥s ≤ 1 + t(p1/s + p) = 1 + c(1 + p1−1/s ) ≤ 1 + 2c < B.

The expansion 1A = p ni=1 (1 + zi ) has nonconstant Fourier support only on unions of complete
                       Q

blocks, whose weights are at least d > kL . This proves every labelled matching condition. The
density w = Pτ π has the same mean, stationary floor, cap and matching, by positivity, Ls

                                                 33
contraction and the diagonal Fourier action. Lemma 10.4 gives the unique positive solutions
hP h = π and uP u = w, automatically of energy one. In the finitely many excluded dimensions
take h = u = 1 and any nontrivial event.
   The exact smoothed density is
                                                     " n                      #
                                                      Y
                                                                    d
                                   w(z) = 1 + tp             (1 + τ zi ) − 1 .
                                                         i=1

For 0 ≤ ϵ < 1 the maximum absolute deviation of this product from one is (1 + ϵ)n − 1: its two
extremes are (1 ± ϵ)n , whose sum is at least two. Hence

                 ∥w − 1∥∞ ≤ tp (1 + τ d )n − 1 ≤ cp1−1/s exp(nτ d ) − 1 −→ 0.
                                                                                    


Here nτ d → 0 for each fixed τ < 1, including τ = 0. No assertion uniform in τ approaching one
is required.
    Both reconstructed potentials belong to the same block-parity algebra. Indeed translations
having parity one on each block, and arbitrary translations on unused coordinates, leave π and
w invariant and commute with P . Translating a positive reconstructed potential therefore gives
another solution of the same equation. Uniqueness in Lemma 10.4 proves invariance. The trans-
lation orbits are exactly the parity fibers, so h = H(z) and u = J(z).
    We record actual return probabilities for either reconstructed potential. Write H for any
positive block-parity potential of energy one and G = P H. Put

                        θ = ρd ,        ℓ = (1 − θ)n ,       v = (1 + θ)n ,       a = EH.

The quotient noise transition from z to z ′ is p i (1 + θzi zi′ ). Its density relative to uniform
                                                             Q

quotient measure lies between ℓ and v. Consequently
                                                                            ℓ2       v2
                     aℓ ≤ G ≤ av,             v −1 ≤ a2 ≤ ℓ−1 ,                ≤ G2 ≤ .
                                                                            v         ℓ
The middle bounds use 1 = EHG. If q is the stationary mass of A, then q = pH(+)G(+). The
return probability from any point of A to the whole fiber A is
                                                    pvH(+)    vq     v2
                          rA = KH (x, A) =                 =       ≤    q.
                                                     G(+)    G(+)2   ℓ2

This is not a single-vertex holding probability. Since nρd → 0, both ℓ and v tend to one. For the
two chains the stationary event masses are
                                                                    h                        i
             qπ = p[1 + t(1 − p)] ∼ tp −→ 0,                 qw = p 1 + tp (1 + τ d )n − 1        ∼ p.

Thus qπ /qw ∼ t → ∞ and both actual return probabilities rπ , rw tend to zero. Reversibility gives
exactly
                       Varπ (1A ) = qπ (1 − qπ ), Eh (1A ) = qπ (1 − rπ ),
and the analogous identities with w, u. Both displayed ratios in the theorem are therefore asymp-
totic to t = c2n/s , whereas each Rayleigh quotient tends to one.
    To control the full gaps, apply Proposition 5.1, which includes all nonconstant ambient sectors
and unused coordinates, to H and J. In its notation the lower and upper bounds are

                         max{0, ρ − εd } ≤ λ2 ≤ min{1, max{1 − α, β}},

                                                         34
where, eventually d ≥ 2,
                                     !n
                            1 − ρd                 ρ + ρd−1            (1 − ρ2 )ρd−1
                     α=                   ,   β=            ,   εd =                 .
                            1 + ρd                  1 − ρd                1 − ρd

These tend to 1, ρ, 0, respectively. No upper bound on the heights of H or J enters this propo-
sition. Hence both full gaps tend to 1 − ρ. This conclusion for this particular family and every
fixed τ < 1 does not enlarge the universal smoothing interval in Theorem 13.1.
    Finally, ∥t1A ∥s = c and
                                   ∥tPτ 1A ∥s ≤ tp(1 + τ d )n −→ 0,
so the reverse triangle inequality gives ∥π − w∥s → c. Directly,

                       Eπ s = (1 − p)(1 − tp)s + p[1 + t(1 − p)]s −→ 1 + cs .

For every fixed threshold R, the value of π s on A eventually exceeds R, while its contribution
to this expectation tends to cs . Thus πLs is not uniformly integrable (interpreting the random
variables through their laws on the varying cubes).

     For clarity, a usual separate-comparison route to a gap transfer would require both Varπ (f ) ≤
V Varw (f ) and Eu (f ) ≤ DEh (f ) uniformly. Theorem 14.1 disproves its variance premise. It also
disproves an upper bound Eh ≤ D′ Eu , and hence two-sided form equivalence. It does not disprove
Eu ≤ DEh , a direct Rayleigh-quotient comparison, or the original gap conjecture. In particular
it is not a counterexample to comparison results whose hypotheses include a common invariant
measure, such as the setting described in [11]. The useful remaining route must retain the joint
energy and variance information, rather than impose the disproved separate variance bound.


15     Positioning, failed routes and remaining question
Ordinary and reverse hypercontractivity are classical tools. Mossel, Oleszkiewicz and Sen ex-
plicitly state the Boolean reverse inequality, including negative exponents and tensorization, in
equation (1.2) [2]. The use here is the floor-derived identity gP g ≥ b and its particular exponent
iteration; we do not claim a new hypercontractive inequality. Representation-based decomposition
of reversible chains is also classical; Boyd, Diaconis, Parrilo and Xiao discuss commuting symme-
tries and spectral reduction [3]. Our sector estimates explicitly retain all cosets and compare their
signed kernels to the quotient kernel. The binary simplex construction is not original. Entropy-
volume estimates and random-linear-code existence are classical Gilbert–Varshamov tools; the
simultaneous column condition used here is verified directly rather than attributed as an extra
clause of the coding theorem [5].
    Weak Poincare inequalities and subgeometric convergence are established tools. Andrieu, Lee,
Power and Wang [11] compare kernels with a common invariant measure using tails of a pointwise
comparison weight; their Theorem 36 permits oscillation as a controlling functional. Section 9
instead compares the actual and reference edge measures and then transfers variance using the
stationary cap. The inverse edge moment is derived from the nonlinear floor. This specialization
and its explicit constants do not constitute a claim to invent weak Poincare comparison or prove
priority. The background framework and its breadth are also discussed in [12]. Our bounded read-
ing of the former covers Proposition 35, Theorem 36 and its proof, Remark 37 and the abstract;
for the latter it covers the abstract, introduction and comparison context. The proofs above


                                                     35
include the discrete recursion and covariance summation explicitly. Ordinary hypercontractivity
uses the parameter range stated in [10].
    The positive-background proof in Section 10 also uses classical hypercontractivity and Cheeger
comparison. The cited lazy reversible inequality is Theorem 3.5 of Peres’ notes [13]; its statement
and lower-bound proof on PDF pages 6–7 were inspected. We apply it to (I + K)/2 and record
the resulting conservative constant explicitly. The model-specific steps retain the actual noncon-
stant denominator, use an exact two-component compression and control every small stationary
cut. The lower potential is assumed in the general theorem and derived only for its two-level
consequence. No new Cheeger inequality or global priority claim is made. The bounded primary
check supporting this draft reads the relevant statements just cited, not the entire related liter-
ature. Targeted searches did not establish the priority of the specific moment counterexample,
the quantitative iteration or the uniform code-potential estimates. Search results about “Doob
graphs” concern a different object from the Doob transform used here and do not establish overlap
or novelty. The results in this draft are proved as stated; mathematical correctness, originality
and relevance remain separate questions. No claim of first discovery or frontier classification is
made.
    The regularized-spectrum theorem combines those classical inequalities with positive symmet-
ric reconstruction and the finite-dimensional min–max principle. Its additional stationary expo-
nent is obtained from the original cap by noise contraction, and the subsequent inverse-moment
iteration is proved to cross a fixed supercritical target in finitely many steps. The critical sand-
wich acts on the full operator rather than only a Fourier window. The bounded primary checks
for this step cover equations (1.1)–(1.2) of [2] and the Hypercontractivity Theorem in Chapter
10.1, printed page 284, of [6]. Targeted primary-domain searches about Doob stationary-density
smoothing and Boolean matrix scaling did not establish priority or absence of overlap. We make
no optimal-smoothing or new hypercontractive-inequality claim. The evidence supplement pre-
serves unsuccessful routes rather than replacing their records. Proposition 2.2 excludes divergent
critical weighting moments for two-level potentials and exact-cap failure for product potentials.
The finite fixed point in Section 3 obstructs only the specified iteration. Theorem 2.1 refutes the
exact numerical cap, while its own moments remain bounded and its gap remains asymptotically
unweighted. A generic pair of densities close in total variation is not a counterexample unless
both arise from the same h and satisfy the stationary hypotheses.
    The historical source 353A had a false strict-class-separation claim based on three disjoint
blocks A, B, C and the code generated by A∪B and B∪C. Its two quotient coordinates can indeed
be written as products of the three disjoint block parities, so every such potential already belongs
to the larger three-block algebra allowed in Proposition 5.1. The corrected source 353B preserves
that failed claim and its adverse audit, keeps the valid core code theorem, and substitutes the
simplex witness of Proposition 5.2. Lack of a disjoint basis for one chosen code is not enough to
prove absence of a larger disjoint-block representation.
    The single remaining research question is whether (1), at fixed ρ, b, C, forces a uniformly
positive full-chain gap or allows an admissible collapsing family. One unresolved bridge is a finite
dimension-independent bound on Ers . Under energy normalization,

                                Ers = N −s E π s g −2s ,
                                                     
                                                            N ≥ b.

The portion with g > 1 is controlled by the stationary cap. The joint small-g contribution is
not controlled at the critical exponent by the finite inverse moments above. Additional exact
matching gives strong subcritical convergence and the low-to-all operator control of Section 7,
but does not settle this endpoint. For arbitrary positive potentials, the actual high block beyond

                                                 36
degree ⌊ck⌋ remains uncontrolled. Section 8 identifies actual high-h/P h sets carrying the squared
mass of any non-Perron mode a fixed positive distance above the noise edge; no general bound on
their killed return operator is assumed or proved. Section 10 proves killed control and a full gap
with an additional fixed positive minimum of the normalized potential, and derives that minimum
for the two-level class. It does not derive the minimum from (1) in general. Even an endpoint
moment bound would still require a justified spectral argument for the general question. The
code theorem and Theorem 10.1 exclude their stated classes of collapsing mechanisms, not all
stationary densities satisfying (1). Under the critical cap, collapse requires normalized potential
minima tending to zero; Proposition 10.5 realizes that behavior under all original hypotheses.
Theorem 10.7 rules out gap collapse for this particular family by a full operator-norm estimate.
Theorem 11.1 further refutes a derived positive P h floor and pointwise ratio ceiling. Its different
family has P h → 0 at one point but exponentially stable full spectrum; a small-denominator point
alone is not a killed-return or cut-flow obstruction. Theorem 12.2 excludes uncorrected potential
smoothing as an invariance argument for exact matching. Theorem 13.1 controls every eigenvalue
of the actual reconstructed chain after sufficiently strong stationary-density smoothing, with the
extra moment derived rather than assumed. Proposition 13.2 excludes a uniformly vanishing
critical-norm perturbation argument. Theorem 14.1 also excludes a uniform separate variance
upper comparison and two-sided form equivalence, even though both full gaps of its actual block-
spike family tend to the noise gap. It does not exclude the reverse form bound or a direct Rayleigh
comparison. A remaining approach must derive joint energy and variance control on the small-
P h, high-h/P h region from the original assumptions. No uniform comparison of the original and
reconstructed gaps is inferred. The full-gap question remains open.
    Related gap criteria do not by themselves certify the novelty of this specialization. Gross [14],
in Notation 2.1 and Theorem 2.2, uses a Riemannian Dirichlet generator, a reference logarith-
mic Sobolev inequality and exponential moments of an additive Schrodinger potential to obtain
transformed coercive inequalities. We have not established a reduction of the present discrete
normalized kernel to that theorem. Wang [15], Theorem 1.1, characterizes spectral gaps of er-
godic Markov operators using tail norms. That qualitative criterion does not replace the explicit
uniform all-cut estimate proved here. Our comparison reads those statements and adjacent defi-
nitions, not either full proof or the entire related literature; no priority or non-overlap conclusion
follows.


16     Model assessments and review context
The predecessor is the public Working paper ARR-2026-4T35VQ6MZB8F99F4, version 1 [9].
Its exact PDF and first model-assessment report remain preserved separately. This revision
incorporates new proofs and does not inherit that PDF’s score, verdict or review status. An
assessment of this version, if issued, applies only to the exact artifact hash and context named
in its complete accompanying report. Working-paper deposit, model assessment, human peer
review and editorial acceptance are distinct.
    This successor preserves the integrated positive-background and vanishing-minimum argu-
ments of notes I–L, their actual full-chain classification M, and note N as Section 12. It retains
note O as Section 13 and retains note P as Section 14, retaining the distinction between full spec-
tral control after density regularization and the unresolved original-chain comparison. The first
analytic audits of N and O passed at their respective frozen source hashes without required correc-
tions; both complete reports are preserved. O was assessed at commit 4086adaf, with exact raw
source and report digests in the accompanying manifest. The audit checked the finite exponent

                                                 37
crossing, endpoint cases, full-spectrum similarity and the norm-perturbation counterexample. Its
source verdict is not a grade or assessment of this integrated text. This successor integrates
that previously audited result; its inclusion does not confer an assessment on the integrated
manuscript. The first analytic audit of P passed at commit 011130c6 without objections; its
frozen source and complete report are retained. It checked actual reconstruction, whole-fiber re-
turn probabilities, the directions of the failed comparisons, both full-chain gap limits, and failure
of critical uniform integrability. This source-level audit is not an assessment of the present inte-
gration or of a PDF. M uses a classical critical sandwich estimate; its quantified application to the
constructed family closes that particular collapse route. Its source and eventual PDF require new
exact-artifact reports. The preceding integration in Section 10 replaced the direct two-level proof
with the broader theorem and its two-level consequence; the original direct proof and constants
remain preserved separately. The earlier source and its complete audit reports remain preserved
separately. This successor source and any eventual PDF require their own exact-artifact reports;
earlier grades are not transferred.
    This revision adds note Q as Section 11. Its first analytic source audit passed at commit
c2efb6bc without blocking or nonblocking objections; the frozen source, complete report and
bounded primary-source positioning are preserved by exact digests in the accompanying manifest.
It checked the two shells and return region, the floor at every point, the vanishing denominator,
critical ratio estimates, exact correction, actual reconstruction and full-spectrum comparison.
This is a source-level verdict, not an assessment of this new integration or a PDF. Concentra-
tion and the hypercontractive sandwich are classical; no global priority claim is made for the
construction. Its integration requires its own exact-artifact report.
    Earlier analytical sources 349, 350, 351, corrected 353B and 355 received separate-role source
audits. The added A–G research notes and notes I and J were also audited at their frozen hashes;
their full reports are retained in the evidence packet. Notes I and J received analytic passes
with no blocking objections under their distinct stated hypotheses. The separate first analytic
reports for K, L, M, N, O, P and Q are retained with the current source packet; each verdict
must be read at its own exact hash and is not a PDF assessment. Their exact sources and full
reports are identified by SHA256 digests in the accompanying manifest; those verdicts are not
assessments of this integrated text or a rendered PDF. These reports concern the named source
bytes and do not by themselves certify the integrated manuscript or its eventual rendered PDF.
The discarded 353A scope claim, the previous column-count bound, and the terminal rejection
of an overbroad follow-up README sentence are preserved. That README was corrected to
restrict localization to stationary-mean-zero modes; the underlying C/D statements already had
that hypothesis.
    The first analytic audit of M recorded one nonblocking notation correction: its exponential
error statement is an upper bound, not an equality. Theorem 10.7 incorporates that correction
explicitly. The frozen note, original full report and adjacent correction are retained. The sep-
arately produced and assessed PDF from source commit 8efcb73b does not contain notes E–Q
and does not assess this successor source. Its numerical assessment is not transferred to this
manuscript. This source has not yet been compiled or visually reviewed as a new PDF.
    Preparation and source auditing use Codex roles in the same provider workflow, with inher-
ited context and a shared filesystem. Exact serving backend/version and effective reasoning effort
are not independently attested. No blind, human, provider-independent or organizationally inde-
pendent review is claimed. The user-requested model alias is not evidence of the actual backend.
Full reports retain objections and context rather than only a favorable verdict.
    The new results were derived analytically. No numerical experiment, executed mathematical


                                                 38
search or Lean verification is claimed for them. Document production, when performed, estab-
lishes rendering and artifact provenance rather than mathematical correctness. Classical inputs
are attributed with their bounded reading scope; originality and significance are not certified by
source correctness. The general stationary-gap and critical-moment questions remain open.


References
 [1] J. R. Lee, Entropy, convexity, and matrix scaling, CSE 599S, Winter 2016, updated
     24 January 2016, Section 2 setup. https://homes.cs.washington.edu/~jrl/teaching/
     cse599swi16/notes/lecture1.pdf.

 [2] E. Mossel, K. Oleszkiewicz and A. Sen, On reverse hypercontractivity, arXiv:1108.1210v5
     (2012), introduction, equations (1.1)–(1.2). https://arxiv.org/pdf/1108.1210.

 [3] S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, Symmetry Analysis of Reversible Markov
     Chains, author-hosted manuscript revised 29 November 2004, introduction and symmetry
     setup. https://web.stanford.edu/~boyd/papers/pdf/symmetry.pdf.

 [4] M. Wootters, CS250/EE387: Error Correcting Codes, Problem Set 1, Winter 2025, Section
     2.4 (simplex-code construction). https://web.stanford.edu/class/archive/cs/cs250/
     cs250.1254/Homework/HW1/hw1.pdf.

 [5] V. Guruswami, Introduction to Coding Theory, Notes 2: Gilbert–Varshamov bound, CMU,
     January 2010, Lemma 5 and Theorem 8, including their proofs. https://www.cs.cmu.edu/
     ~venkatg/teaching/codingtheory/notes/notes2.pdf.

 [6] R. O’Donnell, Analysis of Boolean Functions, corrected May 2021 arXiv edition, Definition
     2.46 and Proposition 2.47, PDF page 55; Theorem 9.21 and its proof, printed p. 262; Chapter
     10.1 Hypercontractivity Theorem, printed p. 284. https://arxiv.org/pdf/2105.10386.

 [7] S. Heilman, E. Mossel and K. Oleszkiewicz, Strong Contraction and Influences in Tail Spaces,
     introduction and same-exponent heat-smoothing statements. https://www.stevenheilman.
     org/~heilman/papers/hmo.pdf.

 [8] A. Volberg, Tail spaces estimates on Hamming cube and Bernstein–Markov inequality,
     arXiv:2208.00472v4, introduction and Section 2. https://arxiv.org/pdf/2208.00472.

 [9] L. Eriksson, Stationary-to-weighting moment transfer and spectral rigidity for Boolean
     Doob kernels, AIRR Working paper ARR-2026-4T35VQ6MZB8F99F4, version 1 (2026).
     Not peer reviewed or editorially accepted by AIRR. https://airr.science/papers/
     ARR-2026-4T35VQ6MZB8F99F4/versions/v1/.

[10] R. O’Donnell, Analysis of Boolean Functions, Lecture 16: The Hypercontractivity The-
     orem, CMU, Theorem 1.1. https://www.cs.cmu.edu/~odonnell/boolean-analysis/
     lecture16.pdf.

[11] C. Andrieu, A. Lee, S. Power and A. Q. Wang, Comparison of Markov chains via weak
     Poincare inequalities with application to pseudo-marginal MCMC, Annals of Statistics 50(6),
     3592–3618 (2022), Proposition 35, Theorem 36 and Remark 37. doi:10.1214/22-AOS2241.
     https://awllee.github.io/papers/AOS2241.pdf.


                                               39
[12] C. Andrieu, A. Lee, S. Power and A. Q. Wang, Weak Poincare Inequalities for Markov
     chains: theory and applications, arXiv:2312.11689v1 (2023), abstract and introductory con-
     text. https://arxiv.org/abs/2312.11689v1.

[13] Y. Peres, Aspects of Markov chains, Definition 3.4 and Theorem 3.5, including the
     lazy reversible lower-bound proof, PDF pages 6–7. https://sites.math.duke.edu/~rtd/
     CPSS2009/peres6.pdf.

[14] L. Gross, Invariance of intrinsic hypercontractivity under perturbation of Schrodinger opera-
     tors, arXiv:2412.20282v2 (2025), Notation 2.1 and Theorem 2.2. https://arxiv.org/html/
     2412.20282v2.

[15] F.-Y. Wang, Criteria of Spectral Gap for Markov Operators, arXiv:1305.4460v6 (2013), in-
     troductory tail-norm definitions and Theorem 1.1. https://arxiv.org/html/1305.4460v6.




                                               40
