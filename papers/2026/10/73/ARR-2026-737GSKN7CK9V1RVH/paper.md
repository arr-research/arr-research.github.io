# An exact two-mean law for singleton-avoidance probabilities

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
An exact two-mean law for singleton–avoidance probabilities
                                           Lluis Eriksson

                               24 October 2026 — research draft


                                              Abstract
         We determine the infimum of P(X = 1, Z = 0) over finitely supported nonnegative
     integer-valued pairs with real-stable probability generating polynomial and prescribed means
     (α, b). In the positive region 0 < α < 2, 0 ≤ b < min(1, 2 − α), the answer is the smaller
     of a degree-two value and an explicit categorical–Poisson limit. For α ≤ 1 the limiting
     categorical trial has no X mass; for α > 1 and b > 0 it necessarily has positive X mass. A
     determinantal pinching preserves the coefficient and both means exactly. Three perturbations
     of a hypothetical finite global minimizer then exclude all intermediate Bernoulli block sizes,
     using an analytic estimate for large blocks and three elementary polynomial factorizations
     for the remaining sizes. The bound is sharp even for finite determinantal measures with
     Hermitian positive-contraction kernels, counted on two disjoint blocks. The formula concerns
     unrestricted finite degree and one singleton target; no application to a TSP approximation
     constant is asserted.

Draft status. The preceding exact draft received a single-model assessment recommending
minor revision. This corrected draft awaits a check of those changes and is not published. Exact
algebraic checks supplement the proofs below.


1    The exact envelope
A real polynomial is real stable if it is nonzero whenever all variables have positive imaginary
parts. Let S(α, b) consist of real-stable polynomials with nonnegative coefficients, P (1, 1) = 1,
and ∇P (1, 1) = (α, b). Degrees are finite but have no common bound. Define

                                      C(α, b) =      inf       [xz 0 ]P.
                                                   P ∈S(α,b)

These classes are nonempty for all nonnegative means: independent monomials times Bernoulli
factors realize every such pair. For the positive region put

            ε = 1 − b,                                             U = min(α, ε),                     (1)
           a1 = min{U, max{0, (2α − b)/4}},                        H = εα − (2α − b)a1 + 2a21 .       (2)

Define a∞ = 0 when α ≤ 1. For 1 < α < 2, set

                                                  2b(α − 1)
                          a∞ =                 p                           .                          (3)
                                 2−α+b+           (2 − α + b)2 + 4b(α − 1)

This includes b = 0. Finally put

                           J = ea∞ −α {ε(α − a∞ ) + a∞ (1 − α + a∞ )}.                                (4)




                                                    1
```

---

## Page 2

```text
Theorem 1. For α, b ≥ 0, the envelope is zero if α = 0, b ≥ 1, α ≥ 2, or α + b ≥ 2. At every
remaining point,
                               C(α, b) = min{H, J} > 0.                                  (5)
The value H is attained by a polynomial of degree at most two; J is approached by normalized
categorical–binomial products. The same infimum holds for disjoint-block counts of strongly
Rayleigh measures, and even when restricted to finite determinantal measures with Hermitian
positive-contraction kernels 0 ⪯ K ⪯ I.

    The zero cases in the theorem overlap harmlessly. The positive domain is precisely 0 < α < 2,
0 ≤ b < min(1, 2 − α). When α > 1, the quadratic vertex satisfies (2α − b)/4 − (α − 1) =
(4 − 2α − b)/4 > 0 in this domain, so the definition of a1 also respects the lower feasibility bound
a ≥ α − 1 for the degree-two realizer. This domain was already covered by refined positivity
estimates in Gurvits–Klein–Leake [5, Theorem 5.11 and Corollary 5.13]. Our question is the
exact value, including the competing finite and limiting mechanisms. We do not claim a new
positivity region.
    For α ≤ 1, the limiting branch simplifies to J = α(1−b)e−α . For α > 1, b > 0, a∞ ∈ (0, α−1):
using a pure Poisson block and a disjoint avoidance trial misses the smaller mixed limit. An
exact finite example illustrating that failure is given in Section 7.
    The deep input is Borcea–Brändén’s bivariate determinantal representation [1, Corollary 6.7].
The Bernoulli equalization argument is classical Hoeffding theory [3]; we give the needed proof.
Capacity productization in [4, 5] does not by itself assert exact preservation of our boundary
coefficient. These comparisons identify dependencies and scope, not worldwide originality.
Higher targets and several simultaneous positive target counts remain outside the theorem.


2    Exact coefficient preservation
Proposition 2. For P ∈ S(α, b) of exact degree D ≥ 1, there is a product Q = D
                                                                                  Q
                                                                                 i=1 (ci +ai x+bi z)
with nonnegative entries, ai + bi + ci = 1, and ai + bi > 0, having the same means and coefficient
[xz 0 ] as P .

Proof. The representation in [1] gives P = ± det(xA + zB + C) with real symmetric D by
D matrices, A, B ⪰ 0. The coefficient of tD in P (t, t) is positive and is ± det(A + B). Thus
G = A + B ≻ 0 and the sign is positive. Since

                      P (t, t) = det G det(tI + G−1/2 CG−1/2 ) > 0     (t > 0),

the symmetric matrix G−1/2 CG−1/2 has no negative eigenvalue. Hence C ⪰ 0. Now A+B +C ≻
0 has determinant one; congruence by its inverse square root preserves P and normalizes the
sum to I. Jacobi’s polynomial identity yields

                 ∂x P (1, 1) = tr A,   ∂z P (1, 1) = tr B,   [xz 0 ]P = tr(adj(C)A).

The last identity also holds for singular C. Diagonalize C and replace A, B by their diagonals in
that basis. This preserves both traces and tr(adj(C)A), since adj(C) is diagonal. The diagonal
entries are the required ai , bi , ci . Their sums are one, and A + B ≻ 0 implies ai + bi > 0. The
determinant becomes Q.

    No inverse of C is used. The proposition preserves a coefficient and means, not the full
distribution or higher coefficients. The converse inclusion holds because the displayed products
themselves are stable.




                                                  2
```

---

## Page 3

```text
3    Reduction to one categorical trial and an equal block
Throughout this section 0 < b < min(1, 2 − α) and 0 < α < 2. For k ≥ 2, 0 ≤ a ≤ U , put

               Gk (a) = a(1 − u)k + (ε − a)(α − a)(1 − u)k−1 ,       u = (α − a)/k.              (6)

For k = 1, use the same polynomial formula on max(0, α − 1) ≤ a ≤ U . These values are
realized by
                            (ax + bz + ε − a)(1 − u + ux)k .                       (7)
A factor with u = 0 can be dropped.

Lemma 3. Fix a finite number of Bernoulli slots, their total mean m < 2, and nonnegative
weights A, C. A minimum of AP(S = 0) + CP(S = 1) can be chosen with all fractional Bernoulli
parameters equal and at most one parameter equal to one.

Proof. The fixed-slot feasible set is compact. Among its minimizers choose one with fewest
fractional parameters. For two such parameters u, v with fixed sum, the objective is affine in
uv. A positive coefficient forces an endpoint, a zero coefficient permits an endpoint with fewer
fractional entries, and a negative coefficient forces u = v. Thus all fractional entries are equal.
There is at most one deterministic one because the total mean is less than two. Zero entries
may be removed.

   The fixed number of slots is chosen before applying compactness; only afterwards do we take
the infimum over all finite slot counts.

Proposition 4. C(α, b) equals the infimum of all the values in (6), including the stated k = 1
domain.
                                                                          P      Q
Proof. Use Proposition 2. At fixed constants ci , the target coefficient i ai j̸=i cj is linear on
0 ≤ ai ≤ 1 − ci , i ai = α. A vertex has at most one coordinate strictly between its bounds.
                   P

Therefore a minimizing replacement has at most one factor containing both x and z. This
reasoning remains valid when some constants vanish.
    If there is a mixed factor, write a for its x mass and t for the sum of pure z masses. Merging
the latter into 1 − t + tz decreases the coefficient, since their constant product is at least 1 − t.
The mixed factor becomes ax + (b − t)z + ε − a + t. For the remaining pure x block write P0 , P1
for its zero and one probabilities; its mean is α − a < 2. The objective is

                    (1 − t){aP0 + (ε − a + t)P1 },      max(0, a − ε) ≤ t ≤ b.

This is concave in t, so an endpoint is no larger. At t = 0, a ≤ U , and Lemma 3 gives an equal
block, except possibly for a deterministic one. In that case α ≥ 1, a ≤ α − 1, and the objective
is at least
                            (ε − a)(2 − α + a) ≥ δ,     δ = 2 − α − b.
Indeed the left side is concave on [0, α − 1] and its endpoint values are ε(2 − α) and δ; their
difference is b(α − 1) ≥ 0. The value δ = G1 (α − 1) is feasible. The empty block has a = α ≤ ε
and is included with u = 0.
    At t = b, or with no mixed factor to start with, the objective is ε times a pure Bernoulli
one-probability of mean α. Equal blocks give Gk (0); the deterministic alternative is at least
ε(2 − α) ≥ δ when it exists. At the other possible endpoint t = a − ε > 0 one has a > ε > α − 1,
so α − a < 1. Then

                            a(1 − a + ε)P0 ≥ a(1 − a + ε)(1 − α + a)
                                            ≥ ε(1 − α + ε) = G1 (ε).


                                                 3
```

---

## Page 4

```text
For the second inequality subtract the right side and factor:
                                (a − ε){(1 − a)(1 − α + a) + ε} ≥ 0.
Here a ≤ 1, and ε < a ≤ α makes G1 (ε) feasible. All reductions are thus dominated by the
scalar union. Conversely, (7) realizes every scalar value.


4    The limit and the two boundaries
Uniformly on a ∈ [0, U ], Gk (a) tends to
                               L(a) = ea−α {ε(α − a) + a(1 − α + a)}.                                  (8)
For example, for k ≥ 4 and 0 ≤ µ = α − a < 2,
                                                             µ2
                             |k log(1 − µ/k) + µ| ≤                 ≤ 4/k.
                                                        2k(1 − µ/k)
Together with (6) this proves uniform convergence, including when a varies with k. The sign of
L′ (a) is the sign of
                                 a2 + (2 − α + b)a − b(α − 1).
It is increasing on a ≥ 0. Its minimum occurs at zero for α ≤ 1, and otherwise at (3), strictly
between zero and α − 1. Thus min L = J. Also min G1 = H.
    We will exclude any global scalar minimum below both H and J. Uniform convergence
ensures that such an infimum is attained in a finite collection of compact scalar families: the
large-k tail is separated from it by a positive gap. At a = U = α the value is α = G1 (α) ≥ H.
At a = U = ε, µ = α − ε = 1 − δ ∈ [0, 1), and
                         Gk (ε) = ε(1 − µ/k)k ≥ ε(1 − µ) = εδ = G1 (ε) ≥ H.
To handle a = 0, we record the classical univariate boundary explicitly.
Lemma 5. For a finite sum of independent Bernoulli variables of mean α, 0 < α < 2, the
infimum of its one-probability is
                                    (
                                        αe−α ,                      0 < α ≤ 1,
                          M (α) =
                                        min{αe−α , α(1 − α/2)},     1 < α < 2.
Proof. Lemma 3 reduces the objective to equal blocks or one deterministic success. The
latter gives at least 2 − α, which exceeds α(1 − α/2) by (2 − α)2 /2. Equal blocks have
q(k) = α(1−α/k)k−1 . For α ≤ 1, q(k) > αe−α for every finite feasible k, by log(1−t) > −t/(1−t);
the deterministic k = 1 endpoint is separate. For α > 1, extend k to real k ≥ 2 and put t = α/k.
Direct differentiation gives
              d log q                                   t + (1 − t) log(1 − t) X          tj
    (1 − t)           = t2 {R(t) − 1/α},      R(t) =                          =                    .
                dk                                                t2            j≥0
                                                                                    (j + 1)(j + 2)

R increases with t, so the derivative sign decreases as k increases. A critical point can only be
a maximum. The infimum is therefore at k = 2 or k → ∞, as stated.

   At a = 0, Lemma 5 excludes a value below min(H, J). For α ≤ 1 its lower bound is J. For
α > 1 the Poisson bound is L(0) ≥ J, while the quadratic bound εα(1 − α/2) is at least H. To
check the latter, put d = 2 − α, δ = d − b. The unconstrained quadratic branch is
                                 Q = δ − (b + 2δ)2 /8 = αδ/2 − b2 /8;
H = Q if b ≤ 2δ, and H = E := εδ otherwise. The differences from these two branches are
respectively bα(α − 1)/2 + b2 /8 > 0 and ε(b − d2 /2) > 0; in the clipped branch b ≥ 2d/3 > d2 /2.

                                                    4
```

---

## Page 5

```text
5     Three variations exclude intermediate finite blocks
Assume a scalar value lies below min(H, J), and select an attained global minimum V as above.
It has k ≥ 2, 0 < a < U , and p = (α − a)/k ∈ (0, 1). Lemma 3 and the deterministic bound in
Proposition 4 show that every finite admissible product with the fixed means (α, b) has value at
least V . This applies also after changing a or appending a zero Bernoulli slot; both types of
perturbation below are therefore covered. Write µ = kp, q = ε − a, y = (k + 1)p, and B = 2 − y.
    First change a to a + t and one pure probability p to p − t, keeping b fixed. This preserves the
two means and is feasible for small t of either sign. Dividing its linear and quadratic coefficients
by the positive factor (1 − p)k−2 gives

                            S = B(a − p) − b(µ − 1) = 0,           B ≥ 0.

If B = 0, then µ = 2 − p > 1 and S < 0, impossible. Set β = b/B > 0. Stationarity gives

                    a = p + β(µ − 1),                        q = (1 − p)(1 − β),
                    α = y + β(µ − 1),                        δ = B − β(1 − p),                   (9)
                                k
                  Gk = (1 − p) (y − β),                      b = βB.

Second perturb two pure probabilities to p + t, p − t. The coefficient of their product is a
positive factor times a(1 − p) + q(µ − 2) = (1 − p)(β − B). Since their product decreases by t2 ,
minimality requires β ≤ B. Third split one probability into p − t, t, 0 < t < p, using a new slot.
The exact objective change is

                            t(p − t)(1 − p)k−2 {a(1 − p) + q(y − 2)}.

The bracket equals (1 − p)(p − δ) by stationarity, hence δ ≤ p. Combining both necessary
conditions gives
                         B − p ≤ β(1 − p) ≤ B(1 − p),      B ≤ 1.
Equality B = 1 forces β = 1 and b = 1, excluded. Thus

                                                                                 (n + 1)B − 2
 0 < B < 1,    n = k + 1 ≥ 3,       p = (2 − B)/n,    max(0, ℓ) ≤ β ≤ B,    ℓ=                . (10)
                                                                                  n−2+B
This deduction does not require α > 1.

5.1   The quadratic branch remains feasible
Before comparing with H, its branch formula must be justified also when the original mean is
below one. At a stationary point,

                             2α − b = 4 − 2B + β(2 − 3B − 2p) > 0.

Indeed, if the coefficient of β is negative, use β ≤ B and p ≤ (2 − B)/3 to bound it below by
4 − 7B 2 /3 − 4B/3 > 1/3; the other sign is immediate. Thus a∗ = (2α − b)/4 is positive and at
most α. Furthermore a∗ − (α − 1) = (4 − 2α − b)/4 > 0. Only the constraint a∗ ≤ ε may clip it.
Consequently at these points
                        (
                          Q, b ≤ 2δ,
                   H=                      Q = δ − (b + 2δ)2 /8,    E = (1 − b)δ.              (11)
                          E, b ≥ 2δ,

The identity Q − E = −(b − 2δ)2 /8 ≤ 0 also proves H ≤ E even if the formal endpoint a = ε
would not have been feasible before imposing the stationary conditions.


                                                  5
```

---

## Page 6

```text
5.2   All k ≥ 5
The ratio (y − β)/(1 − βB) decreases with β; its derivative is −(y − 1)2 /(1 − βB)2 . Hence
                         Gk             2(1 − y/n)n−1
                            ≥ An (y) :=               ,           1 < y < 2.
                          ε                 3−y
For n ≥ 6,
                                    An (y) ≥ min(y/n, 2 − y).                                   (12)
To prove this, put y∗ = 2n/(n + 1). On [1, y∗ ] the logarithmic derivative of An (y)/(y/n) is
−(n − 1)/(n − y) + 1/(3 − y) − 1/y < 0. On [y∗ , 2) that of An (y)/(2 − y) is −(n − 1)/(n − y) +
1/(3 − y) + 1/(2 − y) > 0: here y∗ ≥ 3/2, 1/(2 − y) ≥ 2, and (n − 1)/(n − y) ≤ 2. The minimum
ratio is at y∗ and equals
                                        (n + 1)2 n − 1 n−1
                                                        
                                  Rn =                        .
                                          n+3      n+1
R6 = 3125/3087 > 1, and for real n ≥ 6,
                d log Rn    4   1   2           n2 − 17
                         ≥    −   −    =                       > 0,
                   dn      n+1 n+3 n−1   (n − 1)(n + 1)(n + 3)
using log(1−u) ≥ −u/(1−u). This proves (12). Since δ ≤ min(p, B), it gives Gk ≥ εδ = E ≥ H,
contradicting the violating minimum.

5.3   The three remaining sizes
Under (10), the exact factorizations in Appendix A prove Gk ≥ H for n = 3, 4, 5. Thus no finite
global minimum can lie below both H and J. The uniform-convergence argument proves the
lower bound everywhere. Conversely (7) with k = 1, a = a1 attains H and with a = a∞ , k → ∞
approaches J. This proves (5) for b > 0.


6     Zero region, boundary and determinantal sharpness
At b = 0, nonnegative coefficients force P to be univariate in x. Its real nonpositive roots factor
it into normalized Bernoulli factors; Lemma 5 proves exactly (5). At α = 0 the target coefficient
vanishes. If b ≥ 1, a factor z ensures its vanishing, with remaining means realized independently.
If α ≥ 2, use a factor x2 . For 1 < α < 2 and b ≥ 2 − α, use
                                                             2
                                       (α/2)x + (1 − α/2)z
and an independent z-only count of mean b − (2 − α). These cover the remaining zero cases.
Positivity inside the stated region follows also from the formula: each feasible degree-two product
has positive target value, and the limiting prefactor in (4) is positive.
    Here a finite determinantal measure means one with a Hermitian kernel 0 ⪯ K ⪯ I; such
measures are strongly Rayleigh [2, Proposition 3.5]. If a strongly Rayleigh measure counts
disjoint blocks A, B, identifying the variables in each block and setting the other variables to
one produces a bivariate stable polynomial with the same means and event. Conversely every
categorical factor c + ax + bz is realized on a two-point block by the determinantal kernel
                                              √ !
                                         a      ab
                                K= √                ,     0 ⪯ K ⪯ I.
                                         ab     b
Its probabilities are c, a, b, 0 for neither, the first point, the second point and both. Independent
blocks realize the products in (7); one-point Bernoulli blocks suffice for pure factors. The
upper constructions therefore belong to the determinantal class, which itself lies in the strongly
Rayleigh class [2]. This proves the sharpness assertion of Theorem 1. Additional avoided blocks
can all be identified with z; only the sum of their expected counts is then prescribed.

                                                 6
```

---

## Page 7

```text
7    A mixed limit and the boundary of the result
At α = 13/10, b = 3/10, the pure-Poisson candidate is (91/100)e−13/10 and the degree-two value
is 199/800. The valid finite product
                                                                        100
                                           x   3z 3          247   3x
                                                     
                                             +   +               +
                                           10 10 5           250 250
has coefficient                        99 
                                 247           41   3
                                                        
                                                  −          = 0.2478080145 . . . ,
                                 250           50 2500
strictly below both naive candidates. The exponential comparison can be certified by rational
Taylor bounds; this finite example
                              √        is not used as proof of the main theorem. The correct
exceptional mass is a∞ = ( 34 − 5)/10. A further tempting shortcut would compare Gk (a)
to G1 (a) and L(a) at the same a; that assertion is false. For α = 1, b = 13/20, a = 1/5, k = 3,
G3 = 484/3375 is smaller than both G1 = 4/25 and L = (8/25)e−4/5 . The global quadratic
minimum, however, is 391/3200 < G3 . The proof therefore requires a global minimizer and
feasible perturbations, rather than a pointwise block-size comparison.
    The theorem does not give a fixed-degree envelope, classify all equality cases, preserve higher
coefficients under pinching, or handle several positive targets simultaneously. Its limiting branch
denotes an infimum approached by finite polynomials, not a finite polynomial identified with
a Poisson law. The univariate ingredients are classical; the determinantal representation is a
cited deep theorem. Neither a new TSP approximation ratio nor exhaustive priority is asserted.

AI and responsibility disclosure. The named author directed substantial OpenAI Codex
assistance in derivation, writing and exact algebraic work. GPT-6 Astra xhigh audits used
shared files and declared reused context. These checks are not independent human peer review
or formal proof-assistant verification. The exact preceding draft and its single-model assessment
are retained separately; this revision does not itself constitute a new full assessment. The author
is responsible for the submitted text and claims.


A     Three exact small-block comparisons
Here n = 3, 4, 5, p = (2 − B)/n, and the constraints are (10). Write t = β and

                     G = (1 − p)n−1 (2 − B − t),             δ = B − t(1 − p),    b = tB.

Let Q, E be as in (11). The branch threshold is

                               2B
                     T =                ;         H = Q (t ≤ T ),        H = E (t ≥ T ).
                           B + 2(1 − p)

The identity G − Q = (2 − B)2 Pn /Dn holds with

                  P3 = t2 + 4t + 4 − 8B,                                          D3 = 72,
                  P4 = 2t2 + (6 − B)t + 4 − 8B − B 2 ,                            D4 = 64,
                             2                           2
                  P5 = 225t + (588 − 128B − 8B )t
                           + 324 − 656B − 112B 2 − 8B 3 ,                         D5 = 5000.

Each Pn increases with t ≥ 0, 0 < B < 1. At t = 0 and B ≤ 2/(n + 1) its nonconstant-in-B
expression is nonnegative: for n = 3 it is 4 − 8B; for n = 4 its decreasing value at 2/5 is 16/25;



                                                      7
```

---

## Page 8

```text
for n = 5 its decreasing value at 1/3 is 2500/27. For B ≥ 2/(n + 1), evaluate at t = ℓ:
                               B(2 − B)3 (2B − 1)
                  (G − Q)n=3 =                     ,
                                   18(B + 1)2
                               B(2 − B)3 (B 2 + 19B − 2)
                  (G − Q)n=4 =                            ,
                                      64(B + 2)2
                               (2 − B)3 (B 4 + 28B 3 + 343B 2 + 60B + 18)
                  (G − Q)n=5 =                                            .
                                               625(B + 3)2
These are nonnegative on the respective ranges. Thus G ≥ Q throughout the relaxed feasible
set.
     For the clipped branch, G − E is concave in t, with second derivative −2B(1 − p) < 0. Its
feasible interval is [max(0, ℓ, T ), B]. If nonempty, T ≤ B implies B ≥ Bc = 4/(n + 2). At t = B
its values are
                  n=3:     (1 − B)(B + 1)(3B 2 − 4B + 2)/9,
                  n=4:     (1 − B)(9B 3 − 2B 2 − 4B + 8)/32,
                  n=5:     (1 − B)(2B 4 + 149B 3 − 17B 2 − 34B + 162)/625.
They are positive: complete the square in the first, and bound the negative terms by 6 and 51
respectively in the last two. At the lower endpoint T , Q = E and the preceding comparison
applies. If the lower endpoint is instead ℓ > T , the exact values are
                         (1 − B)Rn (B)
                                        ,    (d3 , d4 , d5 ) = (9, 64, 625),
                         dn (B + n − 2)
where
                      R3 = B 3 + 18B 2 − 12B − 2,
                      R4 = B 4 + 12B 3 + 128B 2 − 48B − 16,
                      R5 = B 5 + 20B 4 + 150B 3 + 1290B 2 − 180B − 102.
Each increases for B ≥ Bc : the positive linear term in its derivative already dominates the sole
negative constant. Their values at Bc are 54/125, 1024/81, and 4143750/16807, all positive.
Concavity now gives G ≥ E on the clipped interval. This proves all three remaining comparisons.
The displayed identities are rational polynomial identities; their checks require no numerical
minimization or sampled sign inference.


References
[1] J. Borcea and P. Brändén. Multivariate Pólya–Schur classification problems in the Weyl
    algebra. Proc. London Math. Soc. 101 (2010), 73–104. arXiv:math/0606360v6, Corollary 6.7.
[2] J. Borcea, P. Brändén and T. M. Liggett. Negative dependence and the geometry of
    polynomials. J. Amer. Math. Soc. 22 (2009), 521–567. arXiv:0707.2340.
[3] W. Hoeffding. On the distribution of the number of successes in independent trials. Ann.
    Math. Statist. 27 (1956), 713–721. Journal record.
[4] L. Gurvits and J. Leake. Capacity lower bounds via productization. STOC 2021, 847–858.
    ECCC TR20-110.
[5] L. Gurvits, N. Klein and J. Leake. From trees to polynomials and back again: New capacity
    bounds with applications to TSP. ICALP 2024, 79:1–79:20. arXiv:2311.09072v2.


                                               8
```
