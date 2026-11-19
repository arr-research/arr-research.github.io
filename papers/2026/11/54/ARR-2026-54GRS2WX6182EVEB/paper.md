       A sharp stationary moment threshold away from equality
               for Boolean Doob chains with two bases
                                             Lluis Eriksson

                                          19 November 2026


                                                Abstract
          For Boolean noise of correlation one half, consider a reversible Doob transform whose
      stationary law factors through a binary linear quotient with two disjoint column bases. Above
      stationary moment order 15/7, exact matching of increasing-order coordinate marginals gives
      full ordered spectral recovery by the previously established packing criterion. For every
      2 ≤ p < 15/7 we construct chains in the same class with exact matching through a linear
      fraction of the coordinates and exponential convergence of the stationary density to one in Lp ,
      yet with exponentially small spectral gap. The construction uses ordinary noise of correlation
      1/4 on a duplicated-coordinate quotient. A rare sphere traps the chain while most of the
      potential is supported near typical magnetizations. A convex correction on the two endpoints
      of each edge enforces exact moment matching even when the minimum density tends to zero.
      Conversely, at the second moment a uniformly bounded inverse stationary moment of order
      above 35/9 suffices for recovery at arbitrary rank. Without inverse control the equality case
      p = 15/7 remains open.


1    Setting and result
On {−1, 1}L let µ be uniform and let Pρ flip coordinates independently with probability (1 − ρ)/2.
For a strictly positive potential h write

                   Kh (x, y) = Pρ (x, y)h(y)/(Pρ h)(x),        πh = hPρ h/Eµ (hPρ h).

The stationary measure is ν = πh µ. Its reversible edge law is proportional to µ(x)Pρ (x, y)h(x)h(y).
Matching through degree k means that every nonconstant Walsh character of degree at most k
has zero ν-mean. Equivalently, the marginals on any k or fewer coordinates are uniform. Code
and matrix terminology uses the identification of signs with bits. The spectral gap is 1 − λ2 , with
eigenvalues in nonincreasing order and counted with multiplicity.

Theorem 1. At ambient correlation 1/2, for each fixed 2 ≤ p < 15/7 there exist β, c > 0 and
positive potentials in every sufficiently large even dimension L = 2r such that

          ∥πh − 1∥p ≤ e−cL ,        Eν χT = 0    (1 ≤ |T | ≤ ⌊βL⌋),        1 − λ2 (Kh ) ≤ e−cL .

The stationary law factors through the matrix [Ir Ir ]. Its displayed columns form two disjoint
bases. In particular the second eigenvalue differs from the ordinary ambient value 1/2 by at least
1/2 − e−cL .



                                                     1
    The positive result of [1, section 7] applies to any binary quotient admitting two disjoint
column bases. For p > 15/7, a uniformly bounded stationary Lp norm and matching through
order k → ∞ imply ordered spectral error O(e−cp k ), uniformly in rank. It assumes positivity
in each finite dimension. Theorem 1 proves that its strict moment threshold cannot be lowered
throughout this class. The construction allows a vanishing stationary minimum. Theorem 4 below
proves recovery at the second moment under a finite inverse moment, in particular under a fixed
positive floor.
    Our construction works more generally at quotient noise ρ. Put
                                         1−ρ                  ρ2
                                    j=       ,         b=          .
                                         1+ρ                1 − ρ2
Theorem 2. Fix 0 < ρ < 1 and 1 < p < ∞ with 1/p > j − 2b. For all sufficiently large r, on
the r-cube at correlation ρ, there are strictly positive potentials for which the three estimates of
Theorem 1 hold with r in place of L.
    At ρ = 1/4 we have j = 3/5, b = 1/15 and j − 2b = 7/15. For the lift to 2r coordinates, let
yi = xi xi+r and pull the quotient potential back along this map. Each yi experiences independent
correlation (1/2)2 . The stationary density pulls back exactly. A Walsh coefficient of the pullback
vanishes unless its index is a union of complete pairs; complete pairs give exactly the corresponding
quotient coefficient. Matching therefore holds to the stated ambient linear order, decreasing β if
needed. The centered indicator of the inverse image of a quotient trap has the same variance and
Dirichlet energy as its quotient indicator. This proves Theorem 1 from Theorem 2.


2    Ordinary returns and transitions to typical magnetizations
Write m(x) = r−1 xi and I(d) = ((1 + d) log(1 + d) + (1 − d) log(1 − d))/2. For a small positive
                   P

constant d, let S be the sphere at magnetization dr = d + O(1/r) obtained by rounding the plus
count to the nearest integer. Let B = {|m| ≤ αd} with 0 < α < ρ, and write q = Pρ (x, S) for
x ∈ S, independent of x by symmetry. We use three estimates:
                           µ(S) ≤ e−rI(d)+O(1) ,       q ≥ exp[−rJ(d) − O(log r)],                (1)
                                         "                             !       #
                                              (ρ − α)2 d2
                    sup Pρ (x, B) ≤ exp −r                − Oρ (d3 ) + O(1) ,                     (2)
                     S                         1 − ρ2 2
                    sup Pρ (y, S) ≤ exp[−r(1 − ρα)2 d2 /2 + O(1)].                                (3)
                       B

Here J(d) = (1 + ρ)I(2d/(1 + ρ))/2 − I(d) = jI(d) + Oρ (d4 ). Bounds are applied with d, α fixed
before the dimension grows.
    For (1), the first estimate is the usual binomial bound. In a stationary noise edge the
probabilities of ++, +−, −+, −− are (a, z, z, a) with a = (1 + ρ)/4 and z = (1 − ρ)/4. Choose
the same nearest integer to rz for each off-diagonal count and fix the diagonals by the two
prescribed sphere margins. Stirling’s formula bounds the probability of this type below by
exp[−r(1 + ρ)I(2d/(1 + ρ))/2 − O(log r)]. All four limiting cell proportions are positive. Divide
by µ(S) and use transitivity. This return estimate also occurs in the earlier shell construction [2].
For (2), condition on the input x. The output signs have means ρxi and each variance 1 − ρ2 .
Their centered log moment generating functions at −u are (1 − ρ2 )u2 /2 + Oρ (u3 ) uniformly for
small u. Apply the exponential Markov bound with u = (ρ − α)d/(1 − ρ2 ). Finally, from B the
mean output magnetization is at most ραd. Hoeffding’s bound for independent signs at threshold
dr gives (3).

                                                   2
3    A trap with negligible stationary moment cost
Choose a constant ℓ satisfying

                               max(0, (j − 1/p)/2) < ℓ < min(j, b).

Such a choice follows from the strict hypothesis and j > 0. Choose α small enough that
(ρ − α)2 /(1 − ρ2 ) > ℓ and (1 − ρα)2 > j − ℓ. Since I(d) = d2 /2 + O(d4 ), choose d > 0 small enough
that the following inequalities all have strict exponential slack:

    J(d) − 2ℓI(d) < I(d)/p,      sup Pρ (x, B) ≤ e−r(ℓI(d)+η) ,   er(J(d)−ℓI(d)) sup Pρ (y, S) ≤ e−ηr
                                  S                                             B

for some η > 0 and all large r. The set B has complement of exponentially small uniform measure.
    Put P = Pρ , H0 = 1 on B and H0 = e−Dr elsewhere, where D is a fixed constant larger than
2 + |J(d)| + ℓI(d). Set

                      M = e−ℓI(d)r /q,       H = H0 + M 1S ,         W = HP H.

For x ∈ S, P H0 (x)/(M q) ≤ e−cr for some c > 0. The numerator bounds all contributions from
outside S. Consequently each row of the transformed kernel starting on S has exit probability at
most e−cr .
    We verify ∥W − 1∥p ≤ Ce−cr , allowing c to decrease from one estimate to the next. The
background obeys ∥H0 P H0 − 1∥p ≤ 2µ(B c )1/p , by contraction of P and 0 < H0 ≤ 1. Off S the
extra term is H0 M P 1S . On B it is exponentially small by (1) and (3), absorbing the polynomial
factor in the slack. Elsewhere off S it is at most e−Dr M , also exponentially small. On S we have
P H ≤ 2M q and H ≤ 2M eventually (use q ≤ 1). Hence

                                  e−2ℓI(d)r
           ∥1S W ∥p ≤ 4 µ(S)1/p             ≤ exp{r[J(d) − 2ℓI(d) − I(d)/p] + O(log r)}.
                                     q

The stationary density W/EW therefore converges to one exponentially in Lp . The very small
background outside B makes an additive correction to the density potentially incompatible with
positivity. We correct the potential itself.


4    Exact marginals by tilting both ends of an edge
Lemma 3. Let P be a reversible positive semidefinite Markov operator for a finite uniform
measure µ, let H > 0, and let π be its normalized stationary density as above. Let ϕ1 , . . . , ϕN be
distinct nonconstant orthonormal Walsh characters on a cube. If N ε is sufficiently small, where
ε = ∥π − 1∥1 , there exists f in their span with ∥f ∥∞ ≤ CN ε such that Hef has zero stationary
mean for every listed character. Constants are absolute.

Proof. Use the normalized symmetric edge law J of H.                                      s·(Φ(X)+Φ(Y )) .
                                                  √ For Φ = (ϕi )i define ψ(s) = log EJ e
Its gradient at zero has Euclidean norm at most 2 N ε. The tilt by s is exactly the
                                                                                  √ edge law of
Hes·Φ , with marginal νs . For any Euclidean unit v, put F = v · Φ. Then |F | ≤ N , Eµ F = 0,
Eµ F 2 = 1, and

                  v ⊤ ∇2 ψ(s)v = 2 Varνs F + 2 CovJs (F (X), F (Y )) ≥ 2 Varνs F.


                                                   3
The covariance is nonnegative: the centered quadratic form of the edge law is that of P applied
to the potential times the centered function, divided by its normalization.
                                                              √             At zero, the variance is
at least 1 − N ε − N ε2 . In the Euclidean ball of radius 1/(4 N ) the marginal density relative to
ν0 is at least e−1 , by the two endpoint factors and their normalization. The variance comparison
follows by minimizing the squared distance to a constant. Thus the Hessian is bounded below
by an absolute positive multiple of the identity throughout this ball. For N ε sufficiently small,
Taylor’s inequality gives ψ(s) > ψ(0) on its √   boundary. The minimum is interior, and strong
convexity bounds its distance from zero by C N ε. At that minimum the gradient is twice the
vector of stationary character means. Taking f = s · Φ proves the bound.

    Use all characters of degrees 1 through ⌊βr⌋. Their number is at most exp[rHbin (β)] for
0 < β < 1/2 (natural entropy). Choose β sufficiently small using the exponential L1 estimate.
Then ∥f ∥∞ is exponentially small. The new stationary density differs from the old by a pointwise
factor between e−4∥f ∥∞ and e4∥f ∥∞ . The Lp conclusion follows. Each transition changes by at
most e2∥f ∥∞ as a ratio; the small exit probability survives. The corrected stationary mass of S is
at most ∥πnew ∥p µ(S)1−1/p = o(1). Testing the gap variational formula with the centered indicator
of S gives a gap at most supx∈S K(x, S c )/(1 − νnew (S)). This proves Theorem 2.


5    Recovery with a finite inverse stationary moment
The counterexample uses a deep depression of the stationary density. A finite inverse moment
suffices to exclude it even when the pointwise minimum tends to zero. We record the positive
result in the same two-base class.
Theorem 4. Let the ambient correlation be 1/2. Suppose that π factors through a linear quotient
with two disjoint full column bases, matches through degree k, and satisfies ∥π∥2 ≤ B and
∥π −1 ∥s ≤ D for fixed s > 35/9. Then the maximum difference between corresponding ordered
eigenvalues of Kh and P1/2 is at most Ce−ck , with constants depending only on B, D, s. In
particular a fixed positive floor suffices at the second moment for any rank.
Proof. Normalize h by EhP h = 1, and set P = P1/2 , Q = P1/√2 , g = P h, F = Qh, U =
h/g = π/g 2 . Then ∥F ∥2 = 1. The positive scaling h inherits the quotient symmetry from π by
uniqueness: the positive diagonal of P makes the stationary-scaling functional strictly convex
                                                                                   −4
in log h [2]. Two disjoint bases give the quotient contraction Pλ : La → L1+(a−1)λ for a > 1.
This is ordinary forward hypercontractivity in the first basis followed by the same estimate in
the second, with any remaining column noise a contraction [1]. Thus ∥g∥5 = ∥QF ∥5 ≤ 1. Jensen
gives g −1 = 1/P (π/g) ≤ P (g/π). Set 1/a = 1/5 + 1/s. Then
                            ∥g −1 ∥q ≤ D,     q = 1 + 16(a − 1) > 20.
This gain is the reason for the inverse moment hypothesis. By Hölder, U is bounded in Lv for
1/v = 1/2 + 2/q < 3/5.
   For clarity, the comparison from moments to the spectrum can be carried out on the full
cube. Put a0 = Eh and V = ∥F − a0 ∥22 = 1 − a20 . Cauchy–Schwarz gives 1√= (Ehg)2 ≤ a0 E(πg).
Since g = QF and π − 1 has only degrees > k, we have V ≤ a0 B 2−(k+1)/2 V . Thus ∥g − 1∥2 ≤
CB 2−k/2 . On E = {|g − 1| > 2−k/8 }, uniform measure is at most CB 2−3k/4 . Consequently
∥(U − π)1E ∥5/3 ≤ Cµ(E)3/5−1/v (here v < 2). Off E, |U − π| ≤ C2−k/8 π for large k.
   For each nonnegative quotient weight W , ∥QMW Q∥ ≤ ∥W ∥5/3 on the full cube. Indeed, its
positive leading eigenvector for W ≠ 0 is invariant under kernel translations by uniqueness, so

                                                 4
the quotient L2 → L5 estimate bounds its quadratic form. It follows
                                                                 √ that ∥QMU −π Q∥ −4    decays
exponentially. For the signed comparison choose λ = 3/4, θ = 1/( 2λ) < 1. Since 1 + λ ≥ 4,
the same positive multiplier argument bounds ∥Pλ Mπ−1 Pλ ∥ by ∥π − 1∥2 using |π − 1|. Split each
Pθ in Q = Pθ Pλ at degree ⌊k/2⌋. The low–low form vanishes by matching, and each other block
carries a decaying factor θ⌊k/2⌋+1 . Thus ∥QMU Q − P ∥ is exponentially small. The reversible
conjugate of Kh is M√U P M√U . It has the same eigenvalues as QMU Q by the two Gram products
of M√U Q. Min–max completes the comparison.

    The number 35/9 is sufficient; we do not assert necessity. In particular the traps of Theorem 1
at p = 2 cannot have a uniformly bounded inverse stationary moment of any fixed order above
35/9.


6    Scope and antecedents
The rare-sphere joint type and calibration by its return probability are shared with [2]. There,
compensation bands preserve a uniform floor and the all-correlation conclusion reaches some
moment above (1 + ρ)/(1 − ρ). Here the potential on the bulk complement can be arbitrarily
small. This permits the full one-step cost b and the range 1/p > j − 2b. The correction in
Lemma 3 works with the edge law even when the density has a very small minimum. On a
quotient obtained by repeating each coordinate t times, ambient correlation 1/2 gives ρ = 2−t
and j − 2b = (2t − 1)/(2t + 1) − 2/(4t − 1). Our sharp-threshold claim concerns two bases and
fixed p ≥ 2 away from equality. At equality the proof has no strict interval for ℓ. The available
rank-dependent recovery criterion [3] is consistent with these traps; it imposes an additional
condition on the rank relative to the matching order.
    Classical results of Kirshner and Samorodnitsky [4] describe near extremality of spheres under
ordinary Boolean noise. Reverse hypercontractivity [5] underlies the earlier sufficient packing
estimate. These are inputs and comparisons for finite chains. Our result concerns the transformed
stationary law, exact marginals and the gap of its actual kernel. We make no literature-wide
priority claim.


Model assessments and review context
OpenAI Codex assisted with the construction, proof and manuscript in the programme research
chat. Any assessment accompanying a deposit refers to the bytes and version identified in that
record. The arguments here are analytic. The author administers AIRR.


References
[1] L. Eriksson, Stationary concentration and local return in Boolean Doob chains, AIRR working
    paper, v1, section 7.
[2] L. Eriksson, A metastable Hamming shell with exactly matched stationary marginals, public
    v1; subsequent source, section 6.
[3] L. Eriksson, Controlling the denominator by the weight enumerator, source revision, 2026.
[4] N. Kirshner and A. Samorodnitsky, A moment ratio bound for polynomials and some extremal
    properties of Krawchouk polynomials and Hamming spheres, arXiv:1909.11929.

                                                5
[5] E. Mossel, K. Oleszkiewicz and A. Sen, On reverse hypercontractivity, arXiv:1108.1210.




                                               6
