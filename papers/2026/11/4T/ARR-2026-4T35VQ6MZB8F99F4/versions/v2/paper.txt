    Stationary moment transfer, spectral windows and rigidity
                    for Boolean Doob kernels
                                            Lluis Eriksson

                             16 November 2026. Revision candidate


                                               Abstract
         For positive potentials on a Boolean cube, the stationary density of the noise Doob kernel
     and its normalized weighting density are different nonlinear functions of the potential. We
     give an admissible family for which the stationary critical moment is below two while the
     weighting critical moment is above two, despite a fixed positive stationary floor and exact
     marginals through order proportional to the square root of the dimension. This refutes transfer
     of that numerical cap, not the existence of a larger uniform bound. A nonlinear consequence
     of the stationary floor, combined with classical ordinary and reverse hypercontractivity, gives
     explicit inverse-potential moments and weighting-moment bounds below a computable finite
     threshold. Exact stationary matching then gives strong convergence of the two densities
     throughout this subcritical range. The finite bootstrap crosses the exponent needed for a
     dimension-free low-to-all operator bound. We obtain exponentially small error on degrees
     up to a fixed positive fraction of the stationary matching order. Non-Perron modes a fixed
     positive distance above the noise edge must concentrate on actual high-weighting sets of
     exponentially small stationary probability. A tensor example rules out an unrestricted high-
     degree hypercontractive repair; the high block itself remains uncontrolled. For potentials
     supported on a binary linear-code Fourier algebra, we control every invariant sector of the full
     Doob kernel. Under a distance–cardinality condition its gap tends uniformly to the unweighted
     gap, for every positive quotient potential. Direct disjoint-block estimates cover a sharper
     parameter regime. A standard simplex code supplies positive potentials outside the disjoint-
     block class. Classical random linear coding extends this mechanism to positive-rate families
     at every sufficiently large length, with an explicit exponential gap estimate and normalized
     witnesses meeting any fixed stationary floor below one and the moment cap. The general
     stationary-gap question and critical weighting-moment bound remain open.


1    Setting and theorem map
Let µ be uniform probability on {−1, 1}L , L ≥ 1, and let 0 < ρ < 1 be fixed. Boolean prod-
uct noise is denoted by P = Pρ , with Pρ χS = ρ|S| χS for Walsh characters χS . Unqualified
expectations and norms use µ. For h > 0 set

                g = P h,    Z = Ehg,      π = hg/Z,     N = E(h/g),       r = (h/g)/N.

Both π and r have mean one. The Markov kernel

                                     K(x, y) = P (x, y)h(y)/g(x)
                                                                                       √
is reversible for π dµ. Its eigenvalues are positive: conjugation by multiplication by π identifies
it with M√h/g P M√h/g , a positive definite matrix. Its top eigenvalue is one and is simple because

                                                    1
all entries are positive. Write λ2 (K) for its second eigenvalue and gap(K) = 1 − λ2 (K). These
are finite Markov-chain quantities.
    The general question motivating this work fixes b, C > 0, puts
                                    1+ρ                        √
                               s=        ,     kL = min{L, ⌊C L⌋},
                                    1−ρ
and imposes
                        π ≥ b,      Eπ s ≤ 2,      EπχS = 0      (1 ≤ |S| ≤ kL ).                     (1)
The last condition concerns the actual stationary density, on the original labelled coordinates. It
is equivalent to uniform coordinate marginals of these orders. It does not assign exact marginals
to r.
    The results have distinct scopes. Section 2 gives one fixed ρ and floor for which the numerical
implication Eπ s ≤ 2 ⇒ Ers ≤ 2 fails even under all of (1). Section 3 treats every fixed ρ and
proves a dimension-free bound for ∥r∥t for 1 ≤ t < t+ (ρ) < s; with matching it proves r−π → 0 in
this range. Section 4 treats every positive potential on specified code algebras, without a moment
cap or floor for its spectral result. It controls the full chain, not only its quotient. Section 5 relates
the sharper disjoint-block bounds and the simplex example to these conclusions. Section 6 proves
positive-rate, all-large-length code existence with simultaneous column separation, specializes
the full-chain estimate exponentially, and gives actual normalized stationary floor/cap witnesses.
Sections 7–8 use the finite bootstrap to control the entire low-to-all operator through a fraction of
the matching degree, localize actual non-Perron eigenfunctions, and exclude a generic tail-space
repair.
    The manuscript groups analytical sources 349, 350, 351, corrected 353B and 355 with the sep-
arately audited 16 November low-to-full and dimension-free follow-ups A–D. The total-variation
estimate from source 341 is proved again in Section 3. No spectral conclusion is inferred from
moment convergence alone. No assertion about a physical Yang–Mills gap or a continuum limit
is made.


2    Failure of exact critical-cap transfer
Theorem 2.1. There are fixed ρ∗ ∈ (1/3, 1/2) and b∗ = 1/16 such that, for every fixed C > 0, a
sequence of strictly positive potentials satisfies (1) for every L and satisfies

            EπLs∗ < 2 < ErL
                          s∗
                                 for all sufficiently large L,      s∗ = (1 + ρ∗ )/(1 − ρ∗ ).

Both displayed moments tend to two. This is not a divergent-moment or collapsing-gap example.
Proof. On a two-dimensional cube, in the order (++, +−, −+, −−), take

         H = (29/16, 1/4, 1/8, 29/16) = 1 + cx − cy + dxy,             c = 1/32,     d = 13/16.

Thus EH = 1. Put q = c(x − y), v = 2c2 = 1/512, w = d2 = 169/256. For an effective noise
parameter θ ≥ 0,

                   Gθ = Pθ H = 1 + θq + θ2 dxy,         Zθ = EHGθ = 1 + θv + θ2 w.
             √
Take hθ = H/ Zθ , πθ = HGθ /Zθ , and rθ = (H/Gθ )/E(H/Gθ ). These are actual densities from
the same potential. At θ = 0, both densities equal H, and differentiation gives

                                 π0′ = H(q − v),        r0′ = −H(q − v).

                                                    2
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
divergent critical weighting moments under a fixed stationary floor and cap, while product po-
tentials obey the stronger constant-one moment comparison.

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


                                                     3
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

    We use the classical scalar Boolean hypercontractive inequalities [1]: for 1 < p ≤ q < ∞,
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

                                                       4
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

                                                         5
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

                                                          6
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

                                                     7
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

                                                           8
    Choose                               X
                       hj = 1 + εamp               χc ,       0 < εamp < 1/(2j − 1).
                                       c∈Cj \{0}

This is strictly positive, and its Fourier support is exactly Cj . The amplitude εamp is not the
spectral error εgap . If hj were a function of disjoint block parities, uniqueness of the Walsh
expansion would put Cj inside the linear span of those block indicators. Every word in that span
is constant within each block and vanishes on unused coordinates. But Cj separates every pair of
distinct coordinates v, w: choose a with a · (v + w) = 1. Also every coordinate is nonzero in some
codeword. Consequently no block can contain two coordinates and none can be unused. This
contradicts m ≥ 2, and is unchanged by coordinate permutations or by allowing more disjoint
blocks.

    The code construction is classical [3]; its elementary parameter proof is included to avoid
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
                                                                            
                           0 < Rcode < min 1 − H2 (d), log2 (1/ρ) .                                      (7)
                                                      2

For every sufficiently large integer L there exists a binary linear code CL ⊂ FL
                                                                               2 with dimension
nL = ⌊Rcode L⌋, minimum distance DL ≥ ⌈dL⌉, and a generator matrix with nonzero, pairwise
distinct columns. Set

    a∗ = (d/2) log(1/ρ) − Rcode log 2 > 0,           EL = e−a∗ L ,       Cρ = max{1 + ρ, (1 − ρ2 )/ρ}.

For every strictly positive potential h supported on the Fourier algebra of this code, and all suffi-
ciently large L,
                                                             EL
                                 |gap(Kh ) − (1 − ρ)| ≤ Cρ        .                              (8)
                                                           1 − EL
The bound is uniform over all such positive h, with no amplitude, stationary floor or moment
assumption. Both π and r have exactly uniform labelled marginals through degree ⌈dL⌉ − 1.
    Moreover, for every fixed 0 < b < 1 and finite s > 1, there are potentials in these same
algebras, at every sufficiently large length, with energy one, π ≥ b and Eπ s ≤ 2, whose Fourier

                                                          9
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

                                                 10
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
guments [4]; the proof is included with the precise rounding and simultaneous column require-
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

                                                        11
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
the one used in O’Donnell, Theorem 9.21 [5].
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

                                                     12
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

                                M (δk + ρd+1 )                                t/s′         ′               s
          E[πf 2 1U (M )c ] ≤                  ,      π(U (M )) ≤ BKt                M −t/s ,      s′ =       .
                                      λ                                                                   s−1
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
                                      √                                   θtd
                                                                                              
                                                   −(1/2−1/ℓ)
                       ∥f ∥Lℓ (π) ≥       1 − ak Ct             exp           (1/2 − 1/ℓ) .
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

                                                       13
The expansion log κ = 12 (ρ(q − 1) − 1)ϵ2 + O(ϵ4 ) makes κ > 1 for a sufficiently small fixed
ϵ ∈ (0, 1). Thus L−1 log ∥QFL ∥q → log κ > 0. This classical tensor sharpness mechanism refutes
a dimension-uniform L2 → Lq estimate on the entire high-degree space. It is not an admissible
Doob counterexample, and does not contradict same-exponent Lp → Lp tail smoothing [6, 7].
For the available t < s, one has 2t′ > 2s′ = 1 + 1/ρ, so this obstruction applies to the naive
Hölder attempt to control the remaining high block using only ∥u∥t . It does not apply to the
low-degree-input polynomial estimate used above.


9    Positioning, failed routes and remaining question
Ordinary and reverse hypercontractivity are classical tools. Mossel, Oleszkiewicz and Sen ex-
plicitly state the Boolean reverse inequality, including negative exponents and tensorization, in
equation (1.2) [1]. The use here is the floor-derived identity gP g ≥ b and its particular exponent
iteration; we do not claim a new hypercontractive inequality. Representation-based decomposition
of reversible chains is also classical; Boyd, Diaconis, Parrilo and Xiao discuss commuting symme-
tries and spectral reduction [2]. Our sector estimates explicitly retain all cosets and compare their
signed kernels to the quotient kernel. The binary simplex construction is not original. Entropy-
volume estimates and random-linear-code existence are classical Gilbert–Varshamov tools; the
simultaneous column condition used here is verified directly rather than attributed as an extra
clause of the coding theorem [4].
    The bounded primary check supporting this draft reads the relevant statements just cited, not
the entire related literature. Targeted searches did not establish the priority of the specific mo-
ment counterexample, the quantitative iteration or the uniform code-potential estimates. Search
results about “Doob graphs” concern a different object from the Doob transform used here and
do not establish overlap or novelty. The results in this draft are proved as stated; mathematical
correctness, originality and relevance remain separate questions. No claim of first discovery or
frontier classification is made.
    The evidence supplement preserves unsuccessful routes rather than replacing their records.
Proposition 2.2 excludes divergent critical weighting moments for two-level potentials and exact-
cap failure for product potentials. The finite fixed point in Section 3 obstructs only the specified
iteration. Theorem 2.1 refutes the exact numerical cap, while its own moments remain bounded
and its gap remains asymptotically unweighted. A generic pair of densities close in total variation
is not a counterexample unless both arise from the same h and satisfy the stationary hypotheses.
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

                                                  14
matching gives strong subcritical convergence and the low-to-all operator control of Section 7,
but does not settle this endpoint. The actual high block beyond degree ⌊ck⌋ remains uncontrolled.
Section 8 identifies actual high-h/P h sets carrying the squared mass of any non-Perron mode a
fixed positive distance above the noise edge; no bound on their killed return operator is assumed
or proved. Even an endpoint moment bound would still require a justified spectral argument
for the general question. The code theorem excludes a concrete structured family of collapsing
mechanisms, not all stationary densities satisfying (1).


10    Model assessments and review context
The predecessor is the public Working paper ARR-2026-4T35VQ6MZB8F99F4, version 1 [8].
Its exact PDF and first model-assessment report remain preserved separately. This revision
incorporates new proofs and does not inherit that PDF’s score, verdict or review status. An
assessment of this version, if issued, applies only to the exact artifact hash and context named
in its complete accompanying report. Working-paper deposit, model assessment, human peer
review and editorial acceptance are distinct.
    Earlier analytical sources 349, 350, 351, corrected 353B and 355 received separate-role source
audits. The added A–D research notes were also audited at their frozen hashes; their full reports
are retained in the evidence packet. These reports concern the named source bytes and do not by
themselves certify the integrated manuscript or its eventual rendered PDF. The discarded 353A
scope claim, the previous column-count bound, and the terminal rejection of an overbroad follow-
up README sentence are preserved. That README was corrected to restrict localization to
stationary-mean-zero modes; the underlying C/D statements already had that hypothesis.
    Preparation and source auditing use Codex roles in the same provider workflow, with inher-
ited context and a shared filesystem. Exact serving backend/version and effective reasoning effort
are not independently attested. No blind, human, provider-independent or organizationally inde-
pendent review is claimed. The user-requested model alias is not evidence of the actual backend.
Full reports retain objections and context rather than only a favorable verdict.
    The new results were derived analytically. No numerical experiment, executed mathematical
search or Lean verification is claimed for them. Document production, when performed, estab-
lishes rendering and artifact provenance rather than mathematical correctness. Classical inputs
are attributed with their bounded reading scope; originality and significance are not certified by
source correctness. The general stationary-gap and critical-moment questions remain open.


References
[1] E. Mossel, K. Oleszkiewicz and A. Sen, On reverse hypercontractivity, arXiv:1108.1210v5
    (2012), introduction, equations (1.1)–(1.2). https://arxiv.org/pdf/1108.1210.

[2] S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, Symmetry Analysis of Reversible Markov
    Chains, author-hosted manuscript revised 29 November 2004, introduction and symmetry
    setup. https://web.stanford.edu/~boyd/papers/pdf/symmetry.pdf.

[3] M. Wootters, CS250/EE387: Error Correcting Codes, Problem Set 1, Winter 2025, Section
    2.4 (simplex-code construction). https://web.stanford.edu/class/archive/cs/cs250/
    cs250.1254/Homework/HW1/hw1.pdf.



                                               15
[4] V. Guruswami, Introduction to Coding Theory, Notes 2: Gilbert–Varshamov bound, CMU,
    January 2010, Lemma 5 and Theorem 8, including their proofs. https://www.cs.cmu.edu/
    ~venkatg/teaching/codingtheory/notes/notes2.pdf.

[5] R. O’Donnell, Analysis of Boolean Functions, corrected May 2021 arXiv edition, Theorem
    9.21 and its proof, printed p. 262. https://arxiv.org/pdf/2105.10386.

[6] S. Heilman, E. Mossel and K. Oleszkiewicz, Strong Contraction and Influences in Tail Spaces,
    introduction and same-exponent heat-smoothing statements. https://www.stevenheilman.
    org/~heilman/papers/hmo.pdf.

[7] A. Volberg, Tail spaces estimates on Hamming cube and Bernstein–Markov inequality,
    arXiv:2208.00472v4, introduction and Section 2. https://arxiv.org/pdf/2208.00472.

[8] L. Eriksson, Stationary-to-weighting moment transfer and spectral rigidity for Boolean
    Doob kernels, AIRR Working paper ARR-2026-4T35VQ6MZB8F99F4, version 1 (2026).
    Not peer reviewed or editorially accepted by AIRR. https://airr.science/papers/
    ARR-2026-4T35VQ6MZB8F99F4/versions/v1/.




                                              16
