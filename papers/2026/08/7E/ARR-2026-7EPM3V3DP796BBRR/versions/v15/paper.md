# Rectangular observations for finite matrix gradients: observation classes and critical endpoints

**Working paper — not admitted to the AIRR accepted collection.**

Exact232B PDF:30pages,505936bytes,
SHA2565595e89c1bcbec1d9b1ae35053a76e6a962f67b45d5d1ac483e5b7a60c9b9be0.
First analytical AIassessment4.10/10,4native overallstars,criteria4/4/3/3/4.
Current native-format recommendation: **major_revision**, all THREE material entries
OPEN. The original conditional minor opinion, full reports, protocol clarification
and author response remain unchanged. Not blind, independent or human peer review.
Priority, practical usefulness and conditioning remain unestablished.

## Complete existing text rendition

The following is the supplied full30-page extraction, copied without rewriting its
mathematical content. Text extraction loses some mathematical typography; the exact
PDF and complete TeX in source-b/ remain authoritative for symbols. This Markdown
is an accessible text companion, not a new proof or substitute scientific artifact.
Source-freeze/predecessor status statements inside the text are dated history;
REVIEW-STATUS.md records the present exact-artifact distinctions.

```text
          Rectangular observations for finite matrix gradients:
               observation classes and critical endpoints
                                            Lluis Eriksson

        10 November 2026 — manuscript 232, offline integrated source candidate

                                                 Abstract
          We study which observation classes restore coercivity of actual finite forward gradient
      forms. Arbitrary finite symmetric onsite matrices admit coefficient-only common rectangular
      means with output dimension OD (h(1 + Fc (A))), where Fc (A) is a capped local eigenchannel
      budget and the finite penalty may depend on negative depth. On the actual flat coexact
      domain we derive the sharp universal common-partition rank bound g(D −1)(R−1), including
      its annihilator formula and an attaining fibre family. Explicit coexact low fields make product
      order necessary for common full-vector partitions. Component-adapted rectangles instead
      give an additive OD (h + Fc (A)) bound for component-block-diagonal coefficients and escape
      that obstruction on the same family. For constant internally coupled coefficients, fixed-basis
      channel-separable observations can again require super-additive actual coexact rank of sharp
      order ΘD (n2D−2 ); a cheap mixed observation demonstrates why that obstruction is basis
      dependent. The scalar weak critical endpoint has matching worst-case logarithmic upper
      and lower order. Complete scalar BV, weighted-gap, tree, matrix, coexact and endpoint
      proofs are included. The mechanisms are classical; priority, sharp profilewise ranks, efficient
      algorithms and physical or continuum transfer are not established.


1     Objects, principal results and scope
A small number of spatial averages can restore coercivity even when local coefficients are very
small or have negative channels. Two issues must be kept separate: how many averages are
needed, and how large a penalty must be placed on them. We control the first by a capped
coefficient budget while allowing the second to depend on the entire finite profile. At the scalar
weak endpoint a logarithmic loss in the coefficient scale is unavoidable in the worst case.

1.1   The actual finite form and observation rows
Except in the standalone coexact rank theorem, D ≥ 3, n ≥ 1 and h ≥ 1 are integers, c > 0,
                     X = (Z/nZ)D ,          V = nD ,       P = D/2,         r = Dh.
We represent X by the fixed chart {0, . . . , n − 1}D . For u : X → Rh the forward stack is
                                                              D
                                 du(x) = u(x + ei ) − u(x) i=1 ∈ Rr .
All additions in this expression are periodic. Given a finite real symmetric r × r matrix A(x) at
each original start x, define
                                                            ∥u∥2V = V −1
                             X                                             X
                  QA (u) =         du(x)T A(x)du(x),                           ∥u(x)∥2 .                (1)
                             x∈X                                           x


                                                    1
No common eigenbasis or sign assumption is imposed on A(x). For a scalar profile a > 0 we
write                               X
                           Qa (u) =   a(x)∥u(x + ei ) − u(x)∥2 .
                                            x,i

In particular, the coefficient is always evaluated at the forward start; it is never moved to the
endpoint or averaged over an edge.
    An integer rectangle is a nonempty product of consecutive intervals in the fixed chart. It
need not be a periodic rectangle crossing the chart boundary. For such a rectangle B define the
vector row                                               q
                      qB (u) = V −1/2 |B|−1/2
                                              X
                                                  u(x) = |B|/V meanB u.                        (2)
                                                  x∈B

For a partition R put CR u = (qB (u))B∈R , with the Euclidean product norm. Its output dimension
is h#R; on the full field space its rows are independent, so its rank equals that dimension. A
coefficient-only partition is fixed by the coefficient profile and deterministic geometric conventions
before the field u is chosen.

1.2   An arbitrary symmetric matrix theorem
The constants used below are intentionally conservative:

                        b = 2D ,     J = 2D,      Cext = 1 + J{2J(1 + 12J) + 1},
                     GD = 22D+10 D2 Cext
                                     2
                                         ,            BD = (2b + 3)bGPD ,                          (3)
                                           D−1  D
                            D        D                3
                                
                     αD =                                     .
                            2       D−2               4
Here GD is the scalar weighted-gap constant and BD is the resulting tree-count constant. Let
λj (x), 1 ≤ j ≤ r, be the eigenvalues of A(x), counted with multiplicity. Let ν0 count all its
nonpositive local eigenvalues over all x. Define

                                                          min{1, αD cP λj (x)−P }.
                                                  X
                          Fc (A) = ν0 +                                                            (4)
                                           x,j:λj (x)>0

These are local coefficient eigenvalues, not the eigenvalues of the global operator associated with
QA .

Theorem 1.1 (Capped-budget rectangular observations). For every profile A in (1) there is a
coefficient-only partition R into integer rectangles such that
                                              BD
                                                                                  
                       h#R ≤ 2Dh 1 + BD + max    , D + 1 Fc (A) .                                  (5)
                                              αD

There is a finite coefficient-dependent K such that, simultaneously for all u : X → Rh ,

                                    V −1 QA (u) + K∥CR u∥2 ≥ c∥u∥2V .                              (6)

One may take K = c + 4DL, with L explicitly defined in (28). Neither the partition nor K
depends on u.



                                                          2
    The budget caps the cost of each sufficiently small positive channel at one and assigns the
same unit cost to each nonpositive channel. Its count thus does not grow with negative depth.
The penalty K can grow with that depth; (6) makes no assertion that K = c for signed forms.
The elementary singleton partition has hV outputs and also admits a finite penalty for every
finite symmetric form. One may choose whichever of that partition and Theorem 1.1 has fewer
outputs. No optimal dimension, sharp coefficient, or efficient implementation is asserted.

1.3   The cost of a common full-vector partition
The dimension in Theorem 1.1 concerns a common partition with all h component means on
each spatial member. The following refinement shows why this measurement class can require a
product of h and the budget.

Theorem 1.2 (Necessary product order for common partitions). Fix D ≥ 3 and c > 0. For every
pair of integers m, h ≥ 1 there is an actual positive diagonal matrix profile on Xn , n = 3m + 3,
with exactly 2Dm weak direction-labelled channels and

                                        2Dm ≤ Fc (A) ≤ 2Dm + 1.

If a common partition R outputs all h means (2) and satisfies (6) for every general field
u : Xn → Rh with any finite quadratic penalty coefficient, then

                                                              hFc (A)
                                   rank CR = h#R ≥ hm ≥               .                        (7)
                                                              2D + 1
Thus no bound CD (h + Fc (A)) holds uniformly in h in this class: setting h = m makes the ratio of
necessary rank to h + Fc (A) diverge. Together with Theorem 1.1, this gives matching worst-case
hFc (A) order, up to dimensional constants, in joint h, Fc (A) growth. The lower family consists
of general vector fields and is not claimed to be coexact or divergence-free. It does not address
component-dependent partitions, channel-adapted means, or postprocessed measurement classes.

1.4   The scalar endpoint and the precise lower-bound domain
For a positive scalar profile let

                        µ = V −1
                                    X
                                        a(x),          Y (x) = µ/a(x),
                                    x
                                                                                               (8)
                 W (a, µ) = sup τ PX (Y > τ ), T (n, µ) = max{1, nD /(1 + µ)P },
                                    P
                            τ >0

where PX is normalized counting probability. The strict superlevel convention in this definition
is used throughout.

Theorem 1.3 (Weak endpoint upper bound). Suppose 1 ≤ a ≤ 2µ and W (a, µ) ≤ Mw , with µ
the actual arithmetic mean. For every h ≥ 1 there is a coefficient-only rectangular partition with
                                        n                             o
                       h#R ≤ 2Dh 1 + 2P cP BD [1 + P Mw log µ] T (n, µ)                        (9)

and
                         V −1 Qa (u) + c∥CR u∥2 ≥ c∥u∥2V      (u : X → Rh ).                  (10)


                                                   3
    To state the lower bound without an unspecified Hodge domain, fix g ≥ 1. A flat one-cochain
is U = (U1 , . . . , UD ) with Uj : X → Rg ; we regard it as an h = Dg component field in Qa . For
antisymmetric two-cochains Bij = −Bji : X → Rg , define

Di− f (x) = f (x)−f (x−ei ),                        Di− Bij ,
                                               X
                                   (δB)j = −                       Hcoex (X) = {δB : B antisymmetric}.
                                                i
                                                                                                 (11)
Backward divergence j Dj− Uj vanishes on this space by commutation and antisymmetry. The
                        P

energy on it is precisely the scalar component-gradient Qa (U ), with all its original forward starts;
no weighted curl identity is used to define or replace that energy.
Theorem 1.4 (Weak endpoint obstruction and worst-case order). Fix D ≥ 3, c > 0 and g ≥ 1.
For every integer m ≥ 1 there are nm , a profile am with actual mean µm , and an m-dimensional
real subspace Em ⊂ Hcoex (Xnm ) such that

            1 ≤ am ≤ 2µm ,         W (am , µm ) ≤ 1,
                                                          X
                                       Qam (U ) ≤ (c/4)         ∥U (x)∥2   (U ∈ Em ),              (12)
                                                            x
                                                                                          m
                                   T (nm , µm ) ≤ C(D, c),          EX (µm /am )P ≥            .
                                                                                        2P 16D
Suppose an observation C from a neighborhood of zero in Hcoex (Xnm ) to a finite-dimensional
real normed space F is differentiable at zero and C(0) = 0. Suppose also that Φ(y) ≤ K∥y∥2
near zero for some finite K, and that locally
                                   X
                               c       ∥U (x)∥2 ≤ Qam (U ) + Φ(C(U )).                             (13)
                                   x

Then DC(0)|Em is injective and dim F ≥ m. For this fixed-parameter sequence m is comparable
to 1 + log µm for large m. Thus the logarithmic loss in Theorem 1.3 has matching worst-case
order. This is not a claim of optimal rank for every individual profile.
    The centered, differentiable and local quadratic assumptions are part of the lower theorem.
Its penalty need not have a uniform bound as m varies. A common division of energy and
squared field norm by V gives the same rank conclusion. The full critical moment grows along
the lower family, so this family does not contradict the strong-moment scalar theorem.

1.5   Observation classes on the actual coexact domain
A coexact one-cochain has spatial components j = 1, . . . , D and internal channels α = 1, . . . , g.
Thus h = Dg; we identify its real components with pairs (j, α). For one internal channel write
U0 = im(d∗1 ), where

               (d1 u)ij = Di+ uj − Dj+ ui    (i < j),       Di+ f (x) = f (x + ei ) − f (x).

The adjoint uses counting inner products on independent i < j two-cochain coordinates. With
antisymmetric extension of those coordinates, (d∗1 B)j = i Di− Bji , exactly the domain (11).
                                                        P

With g channels the domain is U = U0g . A common volume normalization changes none of these
images or ranks.
   Three observation classes must be distinguished. A common full-vector partition retains
every component mean on each member. A component-adapted map chooses its own rectangle

                                                     4
partition for each real component. A channel-separable linear map may mix all sites and spatial
components within each fixed internal channel, but its rows do not mix distinct internal channels.
Component-adapted rows belong to this last class. A global internal rotation changes what
“channel-separable” means.

Theorem 1.5 (Sharp common-partition coexact rank). For this theorem alone let D ≥ 2,
n, g ≥ 1. For any partition into R nonempty subsets, its full-vector mean map satisfies

                                  rank(CR |U ) ≥ g(D − 1)(R − 1).                               (14)

The bound is sharp as a dimension-only bound: with n = R, coordinate-fibre partitions attain
equality for every R ≥ 1. No geometric hypothesis on the partition is required. For D ≥ 3 there
is a positive diagonal coefficient family, specified in (36), for which every restoring common
full-vector partition, with any penalty vanishing at zero, has

                                          h(D − 1)
                        rank(CR |U ) ≥              Fc (A),           κD = 2D 17D .             (15)
                                         4D(κD + 1)

For that family m ≥ 4, g = m, h = Dm and κD m ≤ Fc (A) ≤ κD m + 1. Hence product order is
necessary for actual restricted rank on the coexact domain, not just for the unrestricted output
dimension hR.

   Define the dimensional constants

                     aD = 2D(1 + BD ),          bD = 2D max{BD /αD , D + 1}.                    (16)

They must not be confused with the coefficient profile a(x) or the balanced-tree branching bound
b = 2D .

Theorem 1.6 (Additive component-adapted rectangles). Suppose D ≥ 3 and A(x) is block
diagonal by the actual real field component: A(i,k),(j,ℓ) (x) = 0 for k ̸= ℓ. Its D × D blocks may be
signed and may couple directions. There are coefficient-only rectangle partitions Rk , with rows

                          qk,B (u) = V −1/2 |B|−1/2
                                                      X
                                                            uk (x),     B ∈ Rk ,
                                                      x∈B

and a finite coefficient-dependent K ≥ c such that

                                                        V −1 QA (u) + K∥Cad u∥2 ≥ c∥u∥2V .
                    X
           Nout =       #Rk ≤ aD h + bD Fc (A),                                                 (17)
                    k

This is an all-field inequality. On the exact family of (36), a choice of such maps has

                             rank(Cad |U ) ≤ 2aD + bD Fc (A) = OD (m),                          (18)

whereas every restoring common full-vector partition has restricted rank at least (D − 1)m2 /4.
The component-block-diagonal coefficient hypothesis is retained; it is not asserted for arbitrary
coupled profiles.

   The next obstruction concerns a larger observation class but coupled coefficients. Its internal
dimension grows with the torus size.


                                                   5
Theorem 1.7 (A fixed-basis channel-separable obstruction). Let D ≥ 3, n ≥ 2, V = nD , g = V ,
h = Dg and d0 = (D − 1)(V − 1). There is an explicit constant positive coupled profile (61) with

                         h + Fc (A) ≤ LD V,      LD = D + D2 (1 + αD ),

for which every channel-separable linear observation C restoring c-coercivity on U with any
penalty Φ(0) = 0 has actual rank

                                                g(D − 1)(V − 1)
                                 rank(C|U ) ≥                   .                              (19)
                                                  2(1 + 8Dn2 )

Consequently no uniform CD (h + Fc (A)) bound holds in this fixed-basis channel-separable class,
even for positive constant coefficients. For the very same profile, cross-channel mixing admits a
restoring map of actual rank d0 = OD (h + Fc (A)) and penalty coefficient c. Thus this is neither
an obstruction for all linear observations nor a basis-invariant impossibility. It gives no fixed-g
impossibility.

   For this exact family, Appendix C constructs allowed channel-separable real-mode rows and
proves the matching minimum-rank order rmin = ΘD (n2D−2 ), with explicit dimensional constants
in Theorem C.1. Its finite penalty is K = c + (4DH)2 /c, with H = cn2 . These rows may be
nonlocal and are not claimed rectangular.

1.6   Classical predecessors, contribution and proof dependencies
This is an integrated successor source for the existing AIRR record ARR-2026-7EPM3V3DP796BBRR,
following its exact version 14 (manuscript 226C). It consolidates the same finite-gradient question
rather than presenting separate papers for its rank refinements. A new source is not the same
reviewed artifact as its predecessor.
    The scalar construction uses substantive classical predecessors: Cohen–DeVore–Petrushev–
Xu [3], Section 6 and Theorem 6.1, explicitly organize dyadic rings through final, branching
and chaining nodes; Brudnyi [2], Appendix II, gives weighted-tree/basic-path approximation
mechanisms, with ring covers in Appendix I. Those constructions are pertinent prior art, not
merely background mentions. The finite implementation here treats atomic coefficient mass,
odd integer subdivision, original-start edge weights and retained intra-ring interfaces. The
matrix application uses local spectral replacement and exact endpoint refinement; the coexact
applications use explicit low fields and restricted image rank. These are descriptions of the proved
adaptations, not proofs that no classical theorem already implies them. Historical priority, exact
equivalence/non-equivalence and exhaustive predecessor coverage remain unestablished. The
elementary forward maximum principle is explicitly attributed where it is used in Section 4.
    Frank [1], Theorems 2.1 and 3.1, provides the classical Cwikel/CLR and operator-valued
context. A weak multiplier condition there must be distinguished from the weak spatial coefficient
distribution here. Our matrix proof invokes no global CLR estimate. The positive αD normalizes
the cap; another fixed positive normalization changes the corresponding constants. Spectral
replacement, direct-sum spectra, BV, tree compression, layer cake and finite projection/rank
principles are classical. No new general principle is claimed.
    The central dependency map is as follows. Every named input is proved within this manuscript,
including the shared bump used by two different coefficient families.



                                                 6
    Result                       Proof dependencies and domain
    Scalar foundation            Appendix A: integer collars → BV extension → original-start
                                 weighted ring gap → compressed heavy chains → rectangular means,
                                 retaining intra-ring interfaces.
    Matrix upper                 Scalar foundation → Section 2: positive replacement, endpoint
                                 refinement and full signed correction; all fields.
    Common lower bounds          Section 3: general-field deltas. Section 4: closed-field decomposition,
                                 maximum principle and actual coexact low fields; these ranks are
                                 distinct.
    Adapted upper/escape         The h = 1 matrix theorem, exact block spectra and the forward
                                 torus gap, in Section 5.
    Weak endpoint                Scalar moment corollary plus layer cake for the upper; Lemma 6.1,
                                 geometric scales and derivative-kernel scaling for the actual coexact
                                 lower, in Section 6.
    Coupled obstruction          Actual coexact dimension and row-space projections inside that
                                 domain and real-mode upper rows with a finite Green trace; Appen-
                                 dices B–C. Internal dimension grows and the observation basis is
                                 fixed.

    The full-vector common partition, component-adapted partition and fixed-basis channel-
separable classes cannot be interchanged in a rank comparison. Restricted rank always means
the actual image dimension of the stated map on the stated domain. In particular the coexact
argument never substitutes the full-space count hR for restricted rank. All results concern
finite unit-spacing component-gradient forms. No interacting/covariant coefficient producer,
variable-weight curl identity, continuum construction or Yang–Mills solution follows. External
programme bookkeeping is omitted from the proof because it supplies no mathematical hypothesis
or inference here.


2     Positive replacement and exact rectangular refinement
We prove Theorem 1.1. Every step uses the actual matrix profile on the forward stack in (1). In
particular, positivity is used to discard wrap terms only after replacing the signed profile.

2.1    The spectral split and scalar inverse moment
Set
             1/P                                                X
      σ = αD c,         Sx = 1(−∞,σ] (A(x))Rr ,            N=       dim Sx ,   I = {x : Sx ̸= {0}}.
                                                                x

Here 1(−∞,σ] (A(x)) is the spectral projector. A degenerate eigenspace at the cutoff is selected in
full, so no choice of basis within it enters the construction. Every nonpositive channel is selected.
A positive selected channel contributes exactly one to the capped budget, and an unselected
channel contributes its uncapped inverse power. Consequently

                                                  λj (x)−P ,
                                       X
              Fc (A) = N + αD cP                                0 ≤ N ≤ Fc (A),    |I| ≤ N.           (20)
                                   x,j:λj (x)>σ

Equality λ = σ is included in N .
    Put T = σ + c(1 + N ) > σ. Replace every selected eigenvalue by T , leaving all unselected
eigenvalues and every local spectral subspace unchanged, and denote the resulting positive

                                                       7
definite matrix by AT (x). For N = 0 this changes nothing. With aT (x) = λmin (AT (x)) > 0,
pointwise matrix positivity gives
                                    QAT (u) ≥ QaT (u).                                 (21)
This controls the complete stacked vector, including all directional and internal mixing. It
requires no commutation between distinct matrices. Moreover, the largest eigenvalue of AT (x)−P
is at most its trace, hence

                                 aT (x)−P ≤ cP             tr(AT (x)−P )
                             X                      X
                        cP
                             x                         x
                                                               λj (x)−P + N (c/T )P
                                                        X
                                             = cP                                               (22)
                                                    λj (x)>σ
                                                  Fc (A) − N
                                             ≤               + 1.
                                                      αD

The last inequality uses T ≥ c(1 + N ) and N/(1 + N )P ≤ 1 for P ≥ 1. When N = 0 the extra
one is harmless.

2.2   The scalar partition is derived, not assumed
Theorem A.1 in Appendix A applies to every finite positive aT , without an arithmetic-mean,
lower-envelope or upper-envelope condition. Its partition R0 , combined with (21), satisfies

                                  c∥u∥2V ≤ V −1 QAT (u) + c∥CR0 u∥2 ,                           (23)

by summing the same scalar inequality over all h real components. If R0 = #R0 , its exact count
and (22) yield
                                        "                                               #
                                                                                   −P
                                                                      X
                                                                  P
                          R0 ≤ 2D 1 + (2b + 3)b(cGD )                     aT (x)
                                                                      x
                                                          Fc (A) − N
                                                                        
                                 ≤ 2D 1 + BD           1+                      .                (24)
                                                              αD
There is no auxiliary local-gap or extension hypothesis in this application: the scalar construction
and its gap are proved in the appendix.

2.3   Isolating every affected endpoint
Let
                                 D
                                 [
                     Z=I∪            (I + ei ),        |Z| ≤ (D + 1)|I| ≤ (D + 1)N,             (25)
                                 i=1

where the translations are periodic. We refine R0 so that each z ∈ Z is a singleton member.
Order Z lexicographically in the fixed chart. If z is not already a singleton, let R be its current
rectangle. Partition R \ {z} according to the first coordinate in which a point differs from z,
and according to whether it is smaller or larger in that coordinate. Earlier coordinates are fixed
to those of z, later coordinates range over their original intervals, and the differing coordinate
ranges below or above z. Each nonempty piece is an integer rectangle. There are at most 2D
such pieces. Adding {z} replaces one rectangle by at most 2D + 1, increasing the count by at


                                                           8
most 2D. Earlier isolated points lie in disjoint singleton members and remain intact. Thus the
final partition R satisfies

                           R := #R ≤ R0 + 2D|Z| ≤ R0 + 2D(D + 1)N.                                    (26)

A wrapping forward endpoint is simply its chart representative in Z; this causes no alteration of
the rectangle argument.
   For each original parent B and its final pieces Bk ,
                                 Xq                                    X
                      qB (u) =           |Bk |/|B| qBk (u),                 |Bk |/|B| = 1.
                                 k                                      k

Hilbert-space Cauchy with these exact weights proves

                                                         V −1
                                                                X
                     ∥CR0 u∥2 ≤ ∥CR u∥2 ,                             ∥u(z)∥2 ≤ ∥CR u∥2 .             (27)
                                                                z∈Z

The second assertion holds because each z ∈ Z contributes the singleton row V −1/2 u(z). The
remaining rows are still only component means on rectangles; no gradient or nonrectangular
observation has been introduced.

2.4   Charging the complete signed correction
Define the finite number
                                     
                                     0,                                    N = 0,
                              L=                                                                      (28)
                                           max         (T − λj (x)),       N > 0.
                                         x,j:λj (x)≤σ

The spectral construction gives 0 ≤ AT (x) − A(x) ≤ LI, with zero difference for x ∈  / I. This
is an operator inequality on all r coordinates; in particular it bounds all rotated off-diagonal
contributions together. It does not assign signs to individual cross terms. Therefore
                                                  X
                 0 ≤ QAT (u) − QA (u) ≤ L                ∥du(x)∥2
                                                  x∈I
                                                           "                                      #
                                                    X                        X
                                                                        2                     2
                                             ≤ 2L              D∥u(x)∥ +          ∥u(x + ei )∥        (29)
                                                    x∈I                       i
                                                         X
                                             ≤ 4DL             ∥u(z)∥2 .
                                                         z∈Z

Indeed each site has its own bad-start multiplicity at most D and at most D incoming direction-
labelled starts. All their endpoints belong to Z. This counts parallel edges at period two
separately, as required by the actual form. At n = 1 every difference vanishes and the estimate
remains valid. No periodic term has been dropped from the signed correction.
   Insert (29) into (23), divide the point sum by V , and use (27). This proves (6) with
K = c + 4DL. The count is
                                           BD
                                                                                         
                     hR ≤ 2Dh 1 + BD +        (Fc (A) − N ) + (D + 1)N
                                           αD
                           ≤ 2Dh [1 + BD + max{BD /αD , D + 1}Fc (A)] ,

using the nonnegativity of both N and Fc (A) − N . This completes the proof of Theorem 1.1.

                                                          9
Remark 2.1 (What the cap does and does not control). The only use of the budget after the
local spectral split is the exact identity (20). In particular its control of observation number is
compatible with arbitrarily negative selected eigenvalues, since the penalty absorbs the actual finite
correction. When N = 0, the correction vanishes and K = c. For a positive scalar profile the
sharper direct scalar construction also has K = c without selecting or replacing any channels.
For completeness, choose M = max{0, maxx [−λmin (A(x))]}, so M ≥ 0 and A(x) ≥ −M I for all
x. Then QA (u) ≥ −4DM x ∥u(x)∥2 , because x ∥du(x)∥2 ≤ 4D x ∥u(x)∥2 . For the singleton
                             P                    P                   P

partition ∥CR u∥2 = ∥u∥2V , so K = c + 4DM proves its asserted finite-penalty alternative. The
matrix construction establishes an existence bound with explicit constants, rather than a sharp
spectral rank formula.


3     Necessary product order for full-vector common partitions
We prove Theorem 1.2 by an explicit positive diagonal family. The proof concerns all vector
fields, as in Theorem 1.1, rather than the smaller coexact domain of the endpoint lower theorem.
It uses only local fields and finite-dimensional rank-nullity.

3.1    The coefficient family and every local channel
Let n = 3m + 3 and choose centers

                               xj = (3j + 1, 1, . . . , 1),    0 ≤ j < m.
                                                                      1/P
They lie away from the periodic wrap boundary. With σ = αD c, define

                  a0 = min{c/(8D), σ/2} > 0,              M = rnD ,         H = σM > σ.

In the canonical direction/component basis (i, k) of RDh let A(x) be diagonal, with entries
                                  (
                                  a0 , k = 1 and x ∈ {xj , xj − ei } for some j,
                     λi,k (x) =                                                                    (30)
                                  H, otherwise.

At a center all D direction channels for component one are weak; at an incoming start only
its specified direction/component channel is weak. All eigenvalues are positive. For each fixed
direction the starts xj and xj − ei are distinct. Across centers their first coordinates lie in disjoint
sets {3j, 3j + 1}. Channels with different direction labels remain distinct even when they share a
start. There are therefore exactly 2Dm weak channels.
    Since a0 ≤ σ/2, each weak channel has capped cost one in (4). Every other channel has
capped cost αD cP H −P = M −P . Thus, including all strong channels,

               Fc (A) = 2Dm + (M − 2Dm)M −P ,                 2Dm ≤ Fc (A) ≤ 2Dm + 1.              (31)

Indeed 0 ≤ M − 2Dm ≤ M and P > 1, so the tail is at most M 1−P ≤ 1. Increasing h increases
H and keeps this strong tail bounded; it introduces no uncontrolled h-sized budget contribution.
The choice of H is permitted by the arbitrary finite profile hypothesis.




                                                     10
3.2    The actual low space and the restriction rank
Let Uj (x) = 1{xj } (x)e1 , where e1 ∈ Rh is the first canonical unit vector. These fields are
orthonormal in counting units. Their only nonzero direction-labelled forward differences are −e1
at xj and +e1 at xj − ei , for each direction i. Both original starts are assigned coefficient a0 by
(30); there are no further wrap contributions. Consequently

                                           QA (Uj ) = 2Da0 ≤ c/4.

No nearest-neighbor edge joins distinct centers, and their gradient-start supports are disjoint.
Hence the quadratic cross terms vanish and
                                                                            X
   Lm = spanR {U0 , . . . , Um−1 },      dim Lm = m,     QA (U ) ≤ (c/4)        ∥U (x)∥2   (U ∈ Lm ).   (32)
                                                                            x

These are general vector functions. No divergence or coexact property is asserted for them.
   For any common partition R into R nonempty rectangles, its actual rows on this space are
                                                              

                            qB  tj Uj  = V −1/2 |B|−1/2 
                                X                           X
                                                              tj  e1 .
                                     j                            j:xj ∈B

Each rectangle supplies at most one scalar functional on Lm , so rank(CR |Lm ) ≤ R. If R < m,
rank-nullity gives a nonzero U ∈ Lm with CR U = 0. Coercivity with any finite quadratic penalty,
after multiplication by V , would imply
                                 X                                X
                             c       ∥U (x)∥2 ≤ QA (U ) ≤ (c/4)       ∥U (x)∥2 ,
                                 x                                x

a contradiction. Thus every successful common partition has R ≥ m. The same argument works
for any penalty on these linear observations with Φ(0) = 0, without a differentiability assumption
on that penalty.
    The full field-space rank is exactly hR, not merely a padded output
                                                                    p      dimension. To see this,
for each B choose a site z ∈ B. A field supported at z with value V |B| ek has observation ek
in row B and zero in every other row. These fields show surjectivity onto all hR row coordinates.
Therefore necessary genuine rank is at least hm. Since Fc (A) ≤ 2Dm + 1 ≤ (2D + 1)m, this
proves (7).

3.3    Joint growth and the measurement-class restriction
Set h = m. The necessary rank is at least m2 , while h + Fc (A) ≤ (2D + 1)m + 1. Their ratio
tends to infinity for fixed D, c. Thus a dimension-only CD (h + Fc (A)) bound fails for these
common full-vector partitions, even with arbitrary finite penalty. The product lower bound and
Theorem 1.1 have matching hFc (A) order along this family, since Fc (A) ≥ 2Dm makes 1 + Fc (A)
comparable to Fc (A). Sharp coefficients, additive constants and per-profile optimality are not
determined.
    The extra factor h measures the cost of retaining every component mean on every common
partition member; it does not count h independent tests of the one-component low space. The
argument does not apply to distinct componentwise partitions, projected or channel-adapted
rows, or compressed postprocessed outputs. It requires no external theorem about the rank of
those broader observation classes. These elementary rank and local-field arguments carry no
claim of historical priority, a new general principle, formal verification, or physical transfer.

                                                    11
4     Sharp rank on the actual coexact domain
The general-field obstruction in Section 3 counts full row rank hR. On a coexact domain those
rows have relations, so that count cannot simply be reused. We calculate their actual annihilator
instead.

4.1   Closed fields and the annihilator formula
For one internal channel, U0⊥ = ker d1 by finite adjoint duality. We first prove the real decompo-
sition
                  ker d1 = {constant vector fields} ⊕ im G,       (Gϕ)j = Dj+ ϕ.              (33)
Complexify and use the finite characters exp(2πik · x/n). At frequency k put qj (k) =
exp(2πikj /n) − 1. The closed equations are qi u      b j − qj u
                                                               bi = 0. If k ̸= 0, some qℓ =
                                                                                          ̸ 0, and the
equations force u
                b j = qj u
                         bℓ /qℓ for all j, including those with qj = 0. A coordinate-free choice of
potential is
                                   P
                                      j qj (k)ubj (k)
                          ϕ(k) = P
                           b
                                                   2
                                                       (k ̸= 0),     ϕ(0)
                                                                      b    = 0.
                                        j |qj (k)|

For real u this formula has conjugate symmetry, hence gives a real mean-zero ϕ. Its gradient
supplies every nonzero-frequency mode; the zero mode is a constant vector. Conversely constants
and gradients are closed. A periodic gradient has zero component means, so its intersection with
constant vectors is zero. The kernel of G consists of constants because forward coordinate steps
connect the torus. This proves (33), including n = 1. It also yields the useful real dimension
identity
                        dim U0 = DV − [D + (V − 1)] = (D − 1)(V − 1).                       (34)
Real and complex dimensions here agree by complexification of a real map; there is no doubling
from conjugate frequencies. Forward Nyquist symbols are −2, rather than the spurious zero of a
central difference.
   For a partition into R nonempty sets, let S be the R-dimensional scalar block-constant space
and W = S D . The adjoint range of its full mean map is W : all row scaling factors in (2) are
nonzero. Define the real potential space
                                            X
                                 F = {ϕ :       ϕ(x) = 0, Gϕ ∈ W }.
                                            x

Constants lie in W , and all gradient component means vanish. Therefore (33) gives the direct
sum
                              W ∩ U0⊥ = {constant vectors} ⊕ GF.
Since G is injective on mean-zero functions, this intersection has dimension D + dim F. The
adjoint of the restricted map is PU0 C ∗ . Finite rank-nullity consequently gives the exact formula

                                 rank(C|U0 ) = DR − D − dim F.                                   (35)

This formula is for the actual restricted image, not its listed output size.




                                                  12
4.2   Forward maximum principle and sharpness
Let L = j Dj+ . If a real ϕ satisfies Lϕ = 0, choose a site of global maximum. Every forward
         P

increment there is nonpositive and their sum is zero, so each is zero. Every forward neighbor is
another maximum. Iterating these steps reaches every torus site, including inverse movements
by periodic wrap. Thus ϕ is constant. At n = 1 this is immediate. This is the classical finite
irreducible-chain maximum principle; see Levin–Peres, Lemma 1.16 [4]. Here L = D(Pwalk − I)
for the uniform forward-coordinate walk. Neither reversibility nor aperiodicity is needed. We
claim no new maximum principle.
    For ϕ ∈ F, every component of Gϕ lies in S. Thus Lϕ ∈ S, with global sum zero by
telescoping. The maximum principle proves that

                                              L : F −→ S ∩ 1⊥

is injective. The target has dimension R − 1, since the global-sum functional on S is the nonzero
weighted sum of block values with weights |B|. Hence dim F ≤ R − 1. Substitution into (35)
proves (D − 1)(R − 1) for one channel. The input and output maps for g independent internal
channels are literal direct sums, so ranks add and prove (14).
     For sharpness set n = R and Ba = {x : x1 = a}. Every ϕ(x) = f (x1 ) with a f (a) = 0
                                                                                      P

belongs to F: its first forward derivative is constant on each fibre, and all others vanish. These
potentials form an (R − 1)-dimensional space. The preceding upper bound gives equality in (35),
and then equality in (14). At R = 1 the common global means vanish on the coexact domain
and both sides are zero. Sharpness concerns the allowed family of tori with n = R, not every
fixed pair (n, R).

4.3   A complete fixed-size coexact coefficient family
For the coefficient consequence we retain D ≥ 3 and m ≥ 4. Let L = 16, g = m, h = Dg,
n = m(L + 3) + 3 and V = nD . Use the compact product field in (42), with internal unit vector
e1 ∈ Rg , translated by

             qt = (1 + t(L + 3), 1, . . . , 1),      0 ≤ t < m,             Bt = qt + {0, . . . , L}D .

Lemma 6.1 and its preceding support proof apply to this exact field: the norm is nonzero,
the unit-gradient Rayleigh bound is KD /L2 , and every nonzero original forward start lies in
Bt . The last first-coordinate endpoint is m(L + 3) − 2 < n − 1, and the other endpoints are
L + 1 < n − 1. Successive boxes have two unused sites between them. Thus there are no wrap
collisions and complete field and gradient-start supports are disjoint. Their span Em ⊂ U is truly
m-dimensional. Only spatial components 1, 2 of internal channel 1 are active on Em .
                                  1/P
    Put r = Dh, M = rV , σ = αD c and define

                          a0 = min{σ/2, cL2 /(4KD )} > 0,                      H = σM,
                               A(i,j,α),(i′ ,j ′ ,α′ ) (x) = δii′ δjj ′ δαα′ λi,j,α (x),
                                         (                                                                (36)
                                           a0 , x ∈ t Bt , j ∈ {1, 2}, α = 1,
                                                         S
                          λi,j,α (x) =
                                           H, otherwise.

The triple denotes gradient direction, spatial field component and internal channel. This defines
an actual positive diagonal matrix on all r = D2 g gradient coordinates at every start. The

                                                         13
constant KD is the bump Rayleigh constant of Lemma 6.1, not the observation penalty. Every
nonzero derivative of each bump has coefficient a0 , so on Em
                                                X                         X
                      QA (U ) ≤ a0 (KD /L2 )         ∥U (x)∥2 ≤ (c/4)             ∥U (x)∥2 .                     (37)
                                                 x                            x

All norm and energy cross terms vanish by disjoint supports.
    The number of weak local direction/component/site channels is exactly W∗ = 2Dm(L+1)D =
κD m, with κD = 2D17D . This count includes zero-derivative entries assigned a0 ; none are
dropped. The boxes are disjoint and r ≥ 2D, so W∗ ≤ M . Each weak cap cost is one; every
strong cost is M −P . Hence the full budget is

                        Fc (A) = W∗ + (M − W∗ )M −P ∈ [κD m, κD m + 1].                                          (38)

The strong tail is bounded by M 1−P ≤ 1, using P > 1. No arithmetic-mean or envelope condition
is asserted for this matrix family.
    If a common partition with R members restores coercivity on U with Φ(0) = 0, its restriction
to Em has rank at most 2R. Indeed every row has only the two active real component coordinates
there. If 2R < m, a nonzero low-space kernel vector contradicts coercivity and (37), after
multiplying by V . Thus R ≥ ⌈m/2⌉. The sharp rank bound independently yields

            rank(CR |U ) ≥ g(D − 1)(⌈m/2⌉ − 1) ≥ g(D − 1)m/4 = h(D − 1)m/(4D).

Here ⌈m/2⌉ − 1 ≥ m/4 for m ≥ 4. Using Fc (A) ≤ (κD + 1)m proves (15) and completes
Theorem 1.5. With g = m, necessary rank is at least (D − 1)m2 /4 whereas h + Fc (A) ≤
(D + κD + 1)m. The all-field matrix upper bound restricts to U, giving the matching worst-case
product order up to dimensional constants. The universal rank theorem allows D = 2; this
coefficient application retains D ≥ 3 throughout.


5     Component-adapted rectangles and a structured escape
We prove Theorem 1.6 and compare maps on the same coefficient family and actual coexact
domain, without changing either energy.

5.1    Block spectra and a common finite penalty
Under the component-block-diagonal hypothesis, a fixed permutation of gradient coordinates
gives actual D × D blocks Ak (x) and
                                     h
                                     X                                  h
                                                                        X
                          QA (u) =         QAk (uk ),        Fc (A) =         Fc (Ak ).
                                     k=1                                k=1

The spectral identity holds because the full multiset is the disjoint union of block spectra,
including all nonpositive multiplicities and cap threshold equalities. No spatially varying rotation
is performed. For each actual block apply Theorem 1.1 with h = 1. Here h = 1 means a single
real scalar field with a D-coordinate gradient, not a single spatial direction. It supplies a partition
Rk with

                                      V −1 QAk (uk ) + Kk             |qk,B (u)|2 ≥ cV −1
                                                                X                              X
      #Rk ≤ aD + bD Fc (Ak ),                                                                      |uk (x)|2 ,
                                                               B∈Rk                            x


                                                        14
where Kk ≥ c is finite. All these partitions are fixed from their blocks before u is chosen. Taking
K = maxk Kk and summing proves (17). There is no rescaling of c or V by h. The constants
aD , bD depend only on D. On the full field space each component’s disjoint nonempty block
rows are independent, and different components have independent coordinates. Thus actual full
rank equals Nout ; on a constrained domain it may decrease. The coefficient-block hypothesis is
essential to this proof.

5.2   Root observations for the strong components
For n ≥ 2 the unweighted forward torus gradient has first nonzero Laplacian eigenvalue
                                       λ1 = 4 sin2 (π/n) ≥ 16/n2 .                            (39)
Indeed Fourier symbols give eigenvalues i 4 sin2 (πki /n); the least nonzero one has exactly one
                                             P

nonzero coordinate of smallest distance from zero. The chord bound sin t ≥ 2t/π on [0, π/2] gives
the inequality. Conjugate pairing gives the same real Poincare bound. The constant component
is handled separately, so no statement about a nonzero gap at n = 1 is needed. For the family
(36),
                            2/D
                   σ/c = αD = (3/4)2 [(D/2)(D/(D − 2))D−1 ]2/D ≥ 9/16.
Consequently Hλ1 ≥ 9crnD−2 ≥ c. Writing f = meanX f + f0 gives
                    V −1 H         |Di+ f (x)|2 + c| meanX f |2 ≥ cV −1
                             X                                            X
                                                                              |f (x)|2 .      (40)
                             x,i                                          x

The observation here is exactly qX (f ) = meanX f .
    Only the two real components (j, α) = (1, 1), (2, 1) are weak. Apply the h = 1 matrix theorem
to each, obtaining at most 2aD + bD (F1 + F2 ) ≤ 2aD + bD Fc (A) rows in total. Choose only
the root mean for each of the remaining h − 2 globally strong components. One maximum
of c and the two finite weak-component penalties yields an all-field inequality with at most
h − 2 + 2aD + bD Fc (A) outputs. Every real component of a coexact field has zero global sum,
since it is a sum of periodic backward differences. Hence all these h − 2 strong root rows vanish
identically on U. Restricting the already proved inequality to that domain gives
                                     rank(Cad |U ) ≤ 2aD + bD Fc (A).
This does not split a coexact spatial vector into independently variable spatial components, nor
assert independence of the remaining weak rows. It proves (18) and Theorem 1.6.
     For this same family hFc (A) ≥ DκD m2 and the adapted rank is at most 2aD + bD (κD m + 1).
Their ratio tends to zero. In contrast, Theorem 1.5 forces common full-vector maps to have
restricted rank at least (D − 1)m2 /4. Thus no positive uniform γD hFc (A) lower bound extends to
all component-adapted maps. Refining their different partitions to a common partition and adding
every vector component changes the map and can add the very rank charged by the common-class
lower bound. No optimal adapted rank, efficient algorithm or arbitrary coupled-matrix additive
theorem is inferred.


6     The weak critical endpoint
The positive and negative results use the same scalar original-start energy. The positive estimate
holds on every component field. The negative estimate is already forced on the precisely defined
coexact subspace (11).

                                                    15
6.1    Finite layer cake and the upper estimate
Since a ≥ 1, its actual mean obeys µ ≥ 1 and 0 < Y ≤ µ. For each value y in this finite
distribution,                         Z                     µ
                                          yP = P                τ P −1 1{τ <y} dτ.
                                                        0
Summing over X proves the exact identity
                                         Z µ
                       EX Y   P
                                  =P           τ P −1 PX (Y > τ ) dτ ≤ 1 + P Mw log µ.              (41)
                                          0

The contribution on (0, 1) is at most one, and on [1, µ] we use PX (Y > τ ) ≤ Mw τ −P . At µ = 1
the second integral is zero; in fact the actual mean and a ≥ 1 then force a ≡ 1. Atoms at strict
cutoffs change no ordinary integral. The envelope a ≤ 2µ is retained in the theorem but is not
needed for this step.
   Corollary A.2 in the appendix, with the actual moment M = EX Y P , gives

                                      h#R ≤ 2Dh[1 + 2P cP BD M ]T (n, µ),

and the normalized inequality (10) with penalty c. Substitution of (41) proves Theorem 1.3. Its
geometry and gap are supplied by the complete scalar construction, rather than by a separate
assumed certificate.

6.2    A compact product bump on the actual coexact domain
We now prove Theorem 1.4. Fix a unit vector e ∈ Rg . Define a globally C 1 function
                                                 (
                                                   s2 (1 − s)2 , 0 ≤ s ≤ 1,
                                        β(s) =
                                                   0,            s∈/ [0, 1].

We use β for the bump to distinguish it from the critical exponent P . Both β and β ′ vanish at
the endpoints. On [0, 1],

                      β ′ (s) = 2s(1 − s)(1 − 2s),                    β ′′ (s) = 2 − 12s + 12s2 .

Thus 0 ≤ β ≤ 1, |β ′ | ≤ 2, and β ′ is globally 2-Lipschitz: its interior second derivative has absolute
value at most two, and the zero extension has no derivative jump.
    For an integer L ≥ 16 divisible by 16, put
                                                  D
                                                  Y
                                       ψL (x) =         β(xi /L),           x ∈ ZD ,
                                                  i=1

and define the one-cochain

                     U1 = D2− ψL e,              U2 = −D1− ψL e,               Uj = 0    (j ≥ 3).   (42)

Taking B12 = ψL e, B21 = −ψL e and all other Bij = 0 in (11) gives exactly (42), including its
signs. Therefore U = δB and

                                      Dj− Uj = D1− D2− ψL e − D2− D1− ψL e = 0.
                              X

                                  j


                                                                16
Every component has zero mean by telescoping. The same identities hold exactly on any torus
large enough to contain this support away from wraps.
    The one-dimensional lattice sequence f (t) = β(t/L) is supported at t = 1, . . . , L − 1, and
D− f is supported at t = 1, . . . , L. It follows from the product formula that U is supported in
{0, . . . , L}D and vanishes on every lower coordinate face xi = 0. If Di+ Uj (x) ̸= 0, its original
start belongs to this same box. Indeed the only potentially external incoming start is xi = −1;
its next endpoint is on the zero lower face, so both field values vanish. Upper outgoing starts
xi = L can contribute and are included. In all other coordinates an external coordinate makes
both terms zero. This verifies the boundary-start condition needed below with no interior-only
energy convention.
                                                                       +        2    D
Lemma 6.1 (Finite bump constants). Let E1 (U ) =               x,i,j ∥Di Uj (x)∥ on Z . Then
                                                            P


                        E1 (U ) ≤ UD LD−4 ,                      UD = 32D 2D ,
                 X                                                           9
                      ∥U (x)∥2 ≥ ηD LD−2 ,                       ηD = D+12           .                (43)
                  x                                                   2    2562(D−1)

In particular, with KD = UD /ηD ,
                                                           X
                                     E1 (U ) ≤ (KD /L2 )       ∥U (x)∥2 .                             (44)
                                                           x

Proof. The Lipschitz bound on β ′ bounds each same-coordinate second finite difference by 2/L2 .
For different coordinates the product of two first differences is bounded by 4/L2 . All unused
factors have magnitude at most one. At most 2D component/direction pairs are nonzero; each
has at most (L + 1)D ≤ 2D LD original starts by the support analysis. The common squared
bound 16/L4 gives the first line of (43), including the upper outgoing starts.
     For the norm, take x2 = L/8 + 1, . . . , L/4, exactly L/8 sites, and xi ∈ [L/4, 3L/4] for every
i ̸= 2, at least L/2 sites each. On each backward step in coordinate two, the mean-value point
belongs to [1/8, 1/4], where β ′ ≥ 3/32. On the other coordinates β ≥ 1/256 on [1/4, 3/4]. Hence
                                                       3
                                         ∥U1 (x)∥ ≥       256−(D−1)
                                                      32L
on all these sites. Squaring and multiplying by (L/8)(L/2)D−1 gives the stated ηD . It is strictly
positive, so division yields (44).

6.3   Geometric scales, exact mean and the weak distribution
Choose an integer k ≥ 0 such that ε = 4−k satisfies εKD ≤ c/4. This choice depends on D, c
and is fixed while m varies. Put

       L0 = 2max{4,k} ,     Lj = 2j L0 (0 ≤ j < m),        L∗ = Lm−1 ,      n = 16L∗ ,   H = εL2∗ .   (45)

Every Lj is divisible by 16, and εL20 ≥ 1. Place boxes

         Bj = qj + {0, . . . , Lj }D ,   q0,1 = 1,    qj+1,1 = qj,1 + Lj + 3,    qj,i = 1 (i ≥ 2).

Their first-coordinate intervals have two unused sites between successive boxes. The rightmost
endpoint is j Lj + 3m − 2. Since j Lj < 2L∗ and m ≤ 2m−1 ≤ L∗ /16, this is less than
             P                         P


                                                      17
3L∗ + 1 < n. Other coordinates also lie strictly inside the chart. Thus no support or gradient-
start support collides periodically. Translate (42) into each Bj , obtaining U (j) . Their field
supports and their complete original gradient-start supports are disjoint.
    Define the actual scalar coefficient by
                                                 (
                                                     εL2j , x ∈ Bj ,
                                       a(x) =                                                            (46)
                                                            x∈
                                                                S
                                                     H,       / j Bj .

The boxes are disjoint and the top box has the same coefficient as the background. In particular
1 ≤ a ≤ H. Define its mean by its actual sum:

                           µ = V −1       a(x) = H − V −1
                                      X                           X
                                                                       |Bj |(H − εL2j ).                 (47)
                                      x                            j

This is not a freely adjusted normalization. With

                                                           2D
                                               Cvol =           ,
                                                        1 − 2−D

the geometric series and (Lj + 1)D ≤ 2D LD
                                         j imply


                                                     V −1
                      X                                     X
                           |Bj | ≤ Cvol LD
                                         ∗ ,                     |Bj | ≤ Cvol /16D < 1/2.
                       j                                     j

It follows that
                           H/2 ≤ µ ≤ H,           µ ≥ 1,           1 ≤ a ≤ H ≤ 2µ.                       (48)
The separate inequality µ ≥ 1 follows directly from a ≥ 1, including when H/2 < 1.
    We check W (a, µ) ≤ 1 with strict cutoffs. If 0 < τ ≤ µ/H, then τ ≤ 1 and τ P PX (Y > τ ) ≤ 1.
If τ > µ/H, the background and top box are absent. The boxes contributing to Y > τ satisfy
εL2j < µ/τ . If there is any such box, let j be the largest qualifying index. They form an initial
segment and have total volume at most Cvol LD   j . Consequently

                                τ P PX (Y > τ ) ≤ Cvol (µ/ε)P /V
                                                  ≤ Cvol LD         D
                                                          ∗ /(16L∗ ) < 1.                                (49)

If no box qualifies the probability is zero. Equality at a coefficient atom excludes that box under
the strict criterion and cannot increase the bound. This proves the weak distribution assertion
for every m, including m = 1.

6.4   The low space and every finite local quadratic penalty
Every nonzero gradient of U (j) has its original start in Bj , where (46) has coefficient εL2j . All
wrap terms vanish for these nonwrapping supports. Thus the complete energy, not merely its
interior contribution, is
                                                      X                            X
              Qa (U (j) ) = εL2j E1 (U (j) ) ≤ εKD          ∥U (j) (x)∥2 ≤ (c/4)        ∥U (j) (x)∥2 .   (50)
                                                        x                           x




                                                        18
The norm bound in Lemma 6.1 makes every U (j) nonzero. Disjoint field supports give norm
orthogonality; disjoint gradient-start supports give vanishing quadratic-energy cross terms. The
same inequality therefore holds on
                 Em = spanR {U (0) , . . . , U (m−1) } ⊂ Hcoex (X),               dim Em = m.
This proves an actual low subspace, with no local eigenfunction or gap assumption. From (45)
and (48),
                                                           q        D
                                         T (n, µ) ≤ 16 2/ε                .                       (51)

The right side is independent of m.
   For clarity the finite-dimensional obstruction is proved directly. If DC(0)|Em has a nonzero
kernel vector U , differentiability and C(0) = 0 imply C(tU ) = o(t). For sufficiently small t, the
assumed upper bound on the penalty gives
                                 Φ(C(tU )) ≤ K∥C(tU )∥2 = o(t2 ).
Apply (13) to tU , use the low-space inequality, and divide by t2 . Letting t → 0 would imply
                                     X                          X
                                 c       ∥U (x)∥2 ≤ (c/4)            ∥U (x)∥2 ,
                                     x                           x

a contradiction. Therefore the derivative is injective on Em and dim F ≥ rank(DC(0)|Em ) = m.
No uniformity of K between profiles was used. Positivity or differentiability of Φ is unnecessary;
only its stated finite quadratic upper bound is used. Common normalization of energy and field
norm changes none of this finite-dimensional argument.
    Finally, disjoint boxes, |Bj | ≥ LD
                                      j and µ ≥ H/2 give

                                          m−1
                                                            !P
                             P       −1
                                          X           µ               m(µ/ε)P    m
                   EX (µ/a) ≥ V                 LD
                                                 j               =            ≥ P D.              (52)
                                          j=0
                                                     εL2j               V      2 16

This establishes every part of (12) and explains why the strong-moment theorem is not contra-
dicted.

6.5   The matching order and its quantifiers
For fixed D, c, ε and L0 remain fixed. Equations (45) and (48) imply
                 log µ = 2(m − 1) log 2 + log(εL20 ) + θm ,                   − log 2 ≤ θm ≤ 0.   (53)
Thus m/(1 + log µ) → 1/(2 log 2). The lower bound just proved forces output dimension at least
a positive fixed-parameter multiple of 1 + log µ for large m. Theorem 1.3, with h = Dg, Mw = 1
and (51), gives an upper bound of the same order on these profiles. In particular, no bound
proportional to T (n, µ) o(log µ) can hold uniformly over the weak-bound class for the centered
differentiable/local-quadratic observations under discussion. This proves the final assertion of
Theorem 1.4.
    The conclusion is a worst-case comparison across profiles. It does not state that each profile
needs a logarithm or identify its minimal rank. The lower construction also does not cover a
nonzero observation baseline with an unrelated positive penalty at that baseline, nondifferentiable
encodings, or penalties outside the stated local quadratic class. Those assumptions matter to
the argument rather than merely to its presentation.

                                                     19
7    Model assessments and review context
Lluis Eriksson is the named author. Codex, exposed as an OpenAI system based on GPT-6,
assisted drafting and consolidation. The exact served backend and reasoning-effort setting are
unknown. The authoring role has read the retained predecessor review to address its editorial
findings; this is not a fresh numerical review or a request to improve its score.
    At the source-preparation freeze of 10 November 2026, no PDF of this integrated source
had been produced or assessed. The following gate status records that dated freeze, not a
statement about later document production. The separate source arguments incorporated here
have qualified analytical source-audit reports, but at that freeze the combined exact source still
required its own whole-source audit. Their AI roles share account/system, parent framing and
retained context; independence is not established. No blind, human or independent-model review
is claimed. In particular the changed coupled source 231B received its own exact-source audit
after the earlier source 231A; the later acceptance is not inferred from the earlier one. Its initially
pending integration gate was closed only after the actual complete 231B report arrived and was
read. The matching upper construction 233 likewise has a separate exact-source report. These
are source readings, not numerical assessments or formal certificates.

The predecessor assessment belongs to its exact artifact
The predecessor is manuscript 226C, source commit
                           2d3237501569f6afac8a44d524a5d6db59f63c39.
Its exact 20-page, 419,361-byte PDF has raw-file SHA-256
                               28cb2a7502e05cd8588aa6294f07a7eca
                                5e0e452cce1bf5e4f09e9ec3c89e1a6.
That artifact’s first numerical AI assessment assigned scientific importance 3.25/10, rendered as
3 native stars, with correctness/rigor/novelty/ significance/reproducibility criteria 4/4/2/3/3
on their five-star scales, and recommended minor revision. These numbers describe that old
PDF only. They are not inherited by the new source or any future PDF. Its original complete
scientific report has raw-byte SHA-256
                               bd00e31013a1bdbf1f2766b25665af17ab
                                 7792aae8fcdff3c50670393a1d7272.
The original report, response JSON, context, report-hash record and dated author response are
retained byte-for-byte in the accompanying input packet. The original response omitted a native
version UUID; a later documented projection added only that binding and changed no scientific
judgment. No new UUID, receipt, publication or assessment is created by this preparation.
     The predecessor review requested a closer comparison with CDPX Section 6 and Brudnyi
Appendix II, a clearer dependency guide, removal or definition of external programme shorthand,
and improved reference-page economy. This source identifies those constructive predecessors
explicitly, adds the proof dependency table, defines each observation class and coefficient fam-
ily, and keeps programme bookkeeping outside mathematical inferences. The bibliography is
consolidated with a compact standard layout. Its actual page economy and equation layout
remain unobserved until rendering; no visual fix or new score is presumed. The additions are
substantive sharp coexact rank, structured escape and coupled matching-order results, rather
than an attempt to regrade an unchanged paper. Conservative constants, unestablished priority,
absent practical algorithms and profile-dependent penalties remain limitations.

                                                  20
Complete evidence remains distinct from the proofs
SOURCE-INPUTS.json lists exact captured mathematical sources, the complete listed source-audit
reports and their context disclosures, the clarification to the dimension range of the coexact
coefficient application, and the predecessor’s original assessment/author response. Its hashes
identify raw bytes with no normalization. The scalar, matrix, general-field and weak-endpoint
proof files are retained from exact 226C captures. Prior long execution histories remain external
evidence, not premises of any new theorem. No selected old diagnostic, normal/optimized
agreement, or source verdict is represented as an all-size executable proof, formal certification,
two-fresh-clone replay or execution of the new arguments.
    The complete earlier 226B source rejection for an auxiliary missing nonnegative-depth
condition and the later corrected 226C source report are preserved unchanged among the listed
companions. The corrected optional singleton derivation here retains an explicitly nonnegative
spectral depth. Their original verdicts keep their original referents. No separate original pre-224
scalar-audit report is claimed to have been identified. The new Green-trace constant GD is
deliberately distinct from the inherited weighted-gap constant GD ; the source 233 audit requested
that notation repair on consolidation.
    This preparation performed editing, binary source capture, hashes and static text checks
only. It produced no scientific execution, build, Lean result, rendered PDF, native submission or
numerical grade. Full combined-source audit, document production and visual checks remain
separate gates.


A     Coefficient-selected rectangular means for arbitrary scalar
      profiles
This appendix gives the complete scalar construction used in the main proofs. It uses the original
positive-start scalar coefficient and retains the edges crossing rectangular observation pieces
inside a ring. It does not identify a variable-weight curl/divergence form with that gradient
form. The balanced-ring, BV and tree mechanisms are classical; historical originality of this
finite specialization is unestablished.

A.1    Statement and actual observations
Let integers D ≥ 3, n ≥ 1, and c > 0 be fixed, and put X = {0, . . . , n − 1}D . For any finite
scalar profile a(x) > 0 define

 P = D/2,    b = 2D ,   J = 2D,      Cext = 1 + J{2J(1 + 12J) + 1},        GD = 22D+10 D2 Cext
                                                                                            2
                                                                                               .

Write S(A) = x∈A a(x)−P and t = (cGD )−P /b. Every internal edge below keeps its original
               P

positive start, and all sums and norms initially use counting measure. Here Ea (f ; Ω) denotes
the sum over every chart-internal edge with both endpoints in Ω, weighted by its original
positive-start value a(x); E1 has unit weights. Thus the counting row qbB used at the end of this
appendix equals V 1/2 qB in the normalized notation of (2).

Theorem A.1. There is a partition R of X into nonempty axis-aligned integer rectangles,
determined by a and fixed geometric conventions alone, such that

                                #R ≤ 2D{1 + (2b + 3)S(X)/t},

                                                21
and, simultaneously for every real field f ,
               X                                            X    1 X        2   X
                           a(x)|f (x + ei ) − f (x)|2 + c               f (x) ≥ c     |f (x)|2 .   (54)
          i,x: x,x+ei ∈X                                    B∈R
                                                                |B| x∈B           x∈X

The original periodic energy also satisfies this inequality, by adding its nonnegative wrap terms.
For every integer h ≥ 1 real components the same partition has output dimension h#R and
penalty Φ(y) = c∥y∥2 .

Corollary A.2. For any reference value µ ≥ 1, if n−D x (µ/a(x))D/2 ≤ M , the actual
                                                                        P

normalized rectangular means have output dimension at most Crect T (n, µ), with K = c and

                                Crect = 2Dh{1 + (2b + 3)b(cGD )P 2P M }.

The exact arithmetic mean and envelope 1 ≤ a ≤ 2µ are unnecessary for this sufficiency. The
inverse-moment hypothesis is still assumed; it is not deduced from an arithmetic mean.

Proof. S(X) ≤ M nD µ−P ≤ 2P M max{1, nD /(1 + µ)P }, since µ ≥ 1. Insert 1/t = b(cGD )P into
the theorem. Apply its scalar inequality to each of the h real components.pDividing energy
and squared norms by V = nD gives observation rows V −1/2 |B|−1/2 B f = |B|/V meanB f .
                                                                        P

The all-field inequality restricts to divergence-zero fields, and linear means with the displayed
quadratic penalty supply the original local data.

A.2    Balanced integer nodes and actual collars
Split every coordinate interval with at least two sites into its floor/ceiling halves; a singleton
remains unchanged. Use coordinate order 1, . . . , D, lower before upper, and lexicographic order
on children. Each node has at most b children, and all side lengths differ by at most one. At
global depth k the nonempty intervals have lengths hk or hk + 1, until they are singletons, where
hk = max{1, ⌊n/2k ⌋}.
     Consider a proper descendant I of an ancestor Q, at global depth k, and set h0 = hk . Every
side of I belongs to [h0 , 2h0 ]. Every positive clearance from I to the boundary of Q is a union
of depth-k intervals, so is at least h0 . This uses the global h0 , not the smallest side of this
particular I: at odd sizes that substitution can be false. If every side of Q is at least two, a
proper descendant is shorter in every direction, so each axis has at least one positive clearance.
If the smallest side of Q is one, every side is one or two; each proper descendant is a corner
singleton. That small case is treated separately below.
     For the large case put Ω = Q\I. Expand I by exactly h0 on every face with positive clearance,
leaving a boundary-touching face unchanged, and call the resulting rectangle B. Its side lengths
ℓi lie in [2h0 , 4h0 ]. The collar A = B \ I is covered by the actual positive-clearance face slabs:
normal width h0 and all other sides those of B. There are between D and J = 2D slabs, each
contained in Ω. For slabs Si , Sj with distinct normals, direct product counting gives

                                     |Si |     ℓj               |Si |   ℓj
                                             =    ≤ 4,                =    ≤ 2.                    (55)
                                  |Si ∩ Sj |   h0               |Sj |   ℓi

Choose the first slab as root; attach every distinct-normal slab directly to it, and its opposite
slab, if present, through the first slab with a different normal. This tree has depth at most two.



                                                      22
A.3       An unweighted BV extension, with every hole-crossing edge
                                                                                                                 S |f − meanS f |
                                                                                                            P
For a finite product rectangle S of longest side at most 4h0 , write V1 (S) =
and let TVS (f ) be the sum of |df | over its actual internal edges. Then

                                            V1 (S) ≤ 2h0 TVS (f ).                                                           (56)

Indeed on an interval with m sites, averaging pair paths bounds the coefficient of its rth edge by
2r(m − r)/m ≤ m/2. Commuting coordinate-average projections contract L1 ; telescoping their
product and applying this interval inequality fibrewise proves (56), without an additional factor
D.
   Let mi be the mean on Si and let c0 be the root mean. Averaging on the actual intersection
and using (55) gives |Si ||mi − mj | ≤ 4{V1 (Si ) + V1 (Sj )}. For a depth-two path i, p, r, the second
edge costs the volume ratio |Si |/|Sp | ≤ 2, so
                                                                                            X
                     |Si ||mi − mr | ≤ 4V1 (Si ) + 12V1 (Sp ) + 8V1 (Sr ) ≤ 12                       V1 (Sj ).
                                                                                                 j

Direct paths satisfy the same safe upper bound. Covering A and counting each actual edge at
most J times yields, with PD = 2J(1 + 12J),
                           X                            X
                                |f − c0 | ≤ (1 + 12J)          V1 (Sj ) ≤ PD h0 TVA (f ).                                    (57)
                            A                             j

    At each positive-clearance hole face take the adjacent outside layer of width h0 , with tangential
sides those of I. It is contained in A. On a normal fibre its nearest value satisfies

                                |f (first) − c0 | ≤ h−1
                                                          X                     X
                                                     0            |f − c0 | +           |df |.
                                                          fibre                 fibre

Sum over all actual faces and use (57). The sum of hole-crossing jumps to the constant c0 is at
most J(PD + 1)TVA (f ). Fill I by c0 and leave f unchanged on Ω, obtaining fe on Q. Internal
hole differences vanish; the added variation consists precisely of these crossing faces. Therefore

                                          TVQ (fe) ≤ Cext TVΩ (f ).                                                          (58)

Boundary-touching faces create no exterior edge; at h0 = 1 the fibre gradient sum is zero. No
coefficient is extended, reflected, averaged or reassigned. In particular (58) makes no weighted
quadratic trace-extension claim.

A.4       Actual critical Sobolev and weighted gap on a ring
Here are the finite details needed to pass from BV to the original energy. For T ⊂ {0, . . . , m−1}D
with |T | ≤ mD /2, the occupied-fibre argument and the discrete projection inequality give

                                                                                                     ciso = D(1−2−1/D ) ≥ 12 .
          X
|∂T | ≥        |πi T |−D|T |/m ≥ D|T |(D−1)/D −D|T |/m ≥ ciso |T |(D−1)/D ,
           i

Each occupied nonfull fibre supplies an edge, while full fibres number at most |T |/m. The
projection inequality |T |D−1 ≤ i |πi T | is the finite Loomis–Whitney inequality; it follows from
                               Q




                                                          23
iterated Hölder. A singleton cube has only zero variance. Median parts, finite coarea and
Minkowski consequently imply

                                        inf ∥u − z∥D/(D−1) ≤ (2/ciso )TV(u)
                                        z

on the cube. On a rectangle of aspect at most two, fold a cube of its longest side onto it: in
each coordinate first visit the interval in order, repeat its final endpoint and reflect until the
prescribed length. Every vertex and edge has at most two preimages per coordinate; the initial
product block maps identically onto the rectangle. Restriction and the variation multiplicity at
most 2D give the safe constant Cfull = 2D+1 /ciso for that rectangle, still unweighted.
    Apply this bound and (58) to an indicator on Ω. For every real z, ∥1T −z∥s,Ω ≥ 12 min{|T |, |Ω\
T |}1/s , where s = D/(D − 1). Thus Ω has relative edge isoperimetric constant

                                                cΩ = ciso /(2D+2 Cext ).

Coarea gives ∥g∥s ≤ c−1
                     Ω TVΩ (g) for nonnegative g supported on at most half the vertices. With
a median mf of f , take w = (f − mf )+ or (mf − f )+ and put

                  α = 2(D − 1)/D,                 q = 2D/(D + 2),                 q ′ = 2D/(D − 2).

Then αs = 2 and (α − 1)q ′ = 2. The power-difference inequality, Hölder and degree at most 2D
yield
                                                ′
                              TV(wα ) ≤ 2αD1/q ∥dw∥q ∥w∥2α−1 .
                                                                                    ′
In fact the q ′ th power of the endpoint factor sums to at most 2q D x w(x)2 . Divide only when
                                                                                        P

w ̸= 0. The positive and negative truncated q-edge energies sum to at most the original one;
since 2/q ≥ 1, their squared bounds combine to give
                X                                   X                 2/q                     ′
                    |f − meanΩ f |2 ≤ KΩ2                     |df |q          ,   KΩ = 2αD1/q /cΩ .       (59)
                Ω                                   Ω edges

Only now use weights, on the original retained positive-start edges:
           X            2/q        X                      2/D
                |df |q          ≤             a(start)−D/2          Ea (f ; Ω) ≤ {DS(Ω)}2/D Ea (f ; Ω).
                                    Ω edges

Here q/(2 − q) = D/2, and at most D retained edges start at one vertex. Since α ≤ 2, ciso ≥ 1/2
and 2/q ′ + 2/D = 1, KΩ2 D2/D ≤ 22D+10 DCext  2 ≤ G . Full balanced rectangles obey the same
                                                     D
safe bound without removing a hole.
    For the small nodes with a singleton direction, Q, or Q minus a corner, is a connected graph
with at most b vertices whenever nonempty. Pair paths of length at most b − 1 give variance at
most b2 E1 . Each internal edge satisfies a(start)−D/2 ≤ S(Ω), so E1 ≤ S(Ω)2/D Ea . As GD ≥ b2 ,
this proves in every case
                                    X
                                        |f − meanΩ f |2 ≤ GD S(Ω)2/D Ea (f ; Ω).                          (60)
                                    Ω

A singleton has zero variance. Empty groups are never output.



                                                          24
A.5    Coefficient-only heavy-chain compression and complete count
Give each vertex mass a(x)−P and call a tree node heavy if its mass is strictly greater than t. If
the root is light, output it. Otherwise let L be the number of terminal heavy nodes and Bh the
number with at least two heavy children. Terminal heavy nodes are disjoint, so L ≤ S(X)/t.
Finite tree counting gives Bh ≤ L − 1. After contracting unary paths, there are at most Bh + L − 1
skeleton edges and possibly a root-leading chain; hence at most Bh + L ≤ 2L − 1 maximal unary
chains. The bound is on chains, not their unrestricted total length.
    At a unary node Q → Q′ the increment Q \ Q′ is the union of at most b − 1 light children, of
mass at most (b−1)t. Traverse a maximal chain from ancestor toward descendant, closing a group
when the cumulative mass first reaches t. A closed group is a balanced ancestor ring Qi \ Qj of
mass in [t, bt); a residual is output only if nonempty, and has mass less than t. Across all chains
the disjoint closed groups number at most S(X)/t, while residuals number at most 2L − 1. At
branching or terminal heavy internal nodes output each light child; at a heavy singleton terminal
output the singleton. Such cubes/singletons number at most b(Bh + L) ≤ b(2L − 1).
    These groups partition X: a unary ring excludes the endpoint heavy subtree, which is then
handled at the endpoint; branching processing recurses into every heavy child and outputs all
remaining children. Thus their total number is at most

                     S(X)/t + (2L − 1) + b(2L − 1) ≤ 1 + (2b + 3)S(X)/t.

Each nonsingleton group has mass at most bt = (cGD )−D/2 , so (60) gives residual gap at least c.
Heavy singleton mass may exceed this threshold, but its variance is zero and its mean captures
its entire norm.

A.6    Rectangular rows while retaining intra-ring interfaces
Partition Q \ I by the first coordinate outside I: preceding coordinates belong to I, the current
coordinate is below or above I, and later coordinates fill Q. This gives at most 2D nonempty
integer rectangles. Cubes and singletons require one rectangle. With qbA (f ) = |A|−1/2 A f ,
                                                                                           P

Cauchy gives qbΩ (f )2 ≤ B⊂Ω qbB (f )2 . The actual regional gap therefore implies
                        P

                                                 X
                                Ea (f ; Ω) + c         qbB (f )2 ≥ c∥f ∥2Ω .
                                                 B⊂Ω

Crucially Ea (f ; Ω) retains all edges between rectangular pieces of this same ring; no separate gap
is asserted for each piece. Distinct regions are disjoint, so summing discards only nonnegative
edges between different regions. The full energy dominates their internal sum. The count of
rectangles is at most 2D times the region count, proving Theorem A.1. The retained intra-ring
interfaces are part of the regional energy throughout.


B     Coupled coefficients and fixed-basis channel separation
This appendix proves Theorem 1.7. The direct-sum observation hypothesis is imposed in a
specified internal basis; the coefficient profile deliberately couples those channels in that basis.
The conclusion is not invariant under a change of separability basis.




                                                   25
B.1    The actual constant profile and its full budget
Fix D ≥ 3, n ≥ 2, V = nD and g = V . The domain is U = U0g and its one-channel dimension is
d0 = (D − 1)(V − 1) > 0 by (34). There are h = Dg real field components and r = D2 g gradient
                                    √
coordinates. Let v = (1, . . . , 1)/ g ∈ Rg and put

                      a = c/(16D),       H = cn2 ,          B = HIg − (H − a)vv T ,
                                                                                                    (61)
                                    A(i,j,α),(i′ ,j ′ ,β) = δii′ δjj ′ Bαβ .
Here i is the gradient direction, j the spatial one-cochain component, and α the internal channel.
This is a constant positive matrix with 0 < A ≤ HI; its actual energy is

                                                     Bαβ Di+ zjα (x)Di+ zjβ (x).
                                           X
                             QA (z) =
                                         x,i,j,α,β

The weak polarization v has eigenvalue a, and v ⊥ has eigenvalue H. There are D2 copies of B
at each start, so the full local multiplicities are D2 weak and D2 (g − 1) strong. None can be
removed when the tested field domain is restricted.
                  2/D
    Since σ/c = αD ≥ 9/16 and a/c = 1/(16D), every weak channel has cap cost one. A strong
channel has cost min{1, αD n−D }. Thus the exact full budget is

                  Fc (A) = D2 V [1 + (g − 1) min{1, αD n−D }] ≤ D2 (1 + αD )V.                      (62)

The minimum is retained in the identity; the inequality uses g = V = nD . The strong tail is
allowed to have order V , and is not claimed bounded independently of volume. Adding h = DV
gives h + Fc (A) ≤ LD V .

B.2    A projection inside the actual coexact space
Write the channel-separable observation as C = gα=1 Cα . Each Cα is an arbitrary finite real
                                                            L

linear map on one channel, restricted to U0 ; within that channel it may mix all sites and spatial
components. Let Rα be the counting orthogonal projection in U0 onto the representer space of
the restricted rows. This is a projection within the actual domain, not an unrestricted spatial
row-space projection. Therefore
                 M
            R=        Rα : U → U,     rank R = rC := rank(C|U ),               ker R = ker(C|U ).
                  α

The internal direct sum is legitimate. No decomposition of U0 by its individual spatial components
is assumed.
    Define the isometry T : U0 → U by (T f )α = vα f . Channel separation gives

                          T ∗ RT = g −1                      tr(T ∗ RT ) = rC /g.
                                           X
                                                Rα ,                                                (63)
                                            α

This real symmetric positive contraction has a real unit vector f ∈ U0 with Rayleigh quotient at
most its trace divided by dimension. As R is an orthogonal projection, there is consequently f
with
                            t := ∥RT f ∥2 ≤ rC /(gd0 ),    0 ≤ t ≤ 1.
Set u = (I − R)T f . Then u ∈ U, Cu = 0 and ∥u∥2 = 1 − t. The witness may depend on the
proposed observation map. Projections need not preserve locality, gradients, spatial components
or weak polarization; their preservation of U is enough.

                                                       26
B.3    The kernel witness and the necessary rank
For any periodic field, shifts are isometries, whence
                                      X
                                            ∥Di+ z∥2 ≤ 4D∥z∥2 .
                                       i

This counts every original forward start and wrap, including period two, with no further internal-
dimension factor. The constant weak polarization and the bound A ≤ HI give, respectively,

                            QA (T f ) ≤ 4Da,         QA (RT f ) ≤ 4DHt.

Positivity implies QA (x − y) ≤ 2QA (x) + 2QA (y), hence QA (u) ≤ 8Da + 8DHt. If

                     V −1 QA (z) + Φ(Cz) ≥ c∥z∥2V        (z ∈ U),     Φ(0) = 0,

apply this at the actual kernel vector u and multiply by V :

                                    c(1 − t) ≤ 8Da + 8DHt.

Since 8Da = c/2 and H = cn2 , this yields
                                      c − 8Da        1
                                 t≥           =              .
                                      c + 8DH   2(1 + 8Dn2 )
Combining with (63) proves (19). No division by 1 − t occurred; t = 1 is harmless. The penalty
may be nonlinear, and no differentiability, quadratic growth or uniform penalty bound was used.
Observations remain linear.
   For fixed D ≥ 3 the lower-bound expression has order n2D−2 , whereas h + Fc (A) ≤ LD nD .
Explicitly,
                                 rC         (D − 1)(V − 1)
                                         ≥                  −→ ∞.
                             h + Fc (A)     2LD (1 + 8Dn2 )
The divergence has order nD−2 , including D = 3, 4. This concerns growing g = V , a specified
internal basis and finite unit-spacing tori. It supplies no fixed-g or D = 2 impossibility and no
physical mass-gap inference.

B.4    The same profile admits a cheap mixed observation
Let W z = α vα zα . Since W T = I, this map surjects U onto U0 . Observe its values at every
           P

site and spatial component with rows V −1/2 (W z)j (x). The listed output has DV coordinates
but actual restricted rank is exactly d0 . The orthogonal splitting

                                           z = T W z + zstrong

stays in U, since constant internal combinations commute with the codifferential. They also
commute with forward differences. The split is orthogonal in norm and in coefficient energy.
Every real component of zstrong has zero mean, so the actual torus gap (39) gives

                       QA (zstrong ) ≥ H(16/n2 )∥zstrong ∥2 = 16c∥zstrong ∥2 .

The weak energy is nonnegative, and ∥Cweak z∥2 = V −1 ∥W z∥2 = V −1 ∥T W z∥2 . Therefore

                               V −1 QA (z) + c∥Cweak z∥2 ≥ c∥z∥2V .

                                                   27
Its actual rank d0 = OD (V ) = OD (h + Fc (A)) is additive in order on this family. A fixed
global internal rotation exposing v makes the cheap channel visible. Thus no all-linear or
basis-free obstruction follows. The profile in its original basis is not component-block-diagonal,
so Theorem 1.6 is not contradicted. This completes Theorem 1.7. Appendix C proves a matching
order for this precise family, rather than an all-profile upper bound.


C     Matching channel-separable order for the coupled family
The obstruction in Appendix B is sharp in order for its precise family and row class. We
construct a nonlocal, channel-separable map from real coexact Laplacian modes. This supplies
no general-profile upper bound and no rectangularity claim for these new rows.
    Let rmin be the minimum actual restricted rank among finite channel-separable linear maps
on U for which some penalty vanishing at zero restores c-coercivity for the fixed profile (61). This
class is nonempty: observe a complete basis of U, whose squared observations with coefficient c
control its norm since the energy is positive. Possible ranks are integers between zero and dim U,
so the minimum rank exists. Define a separate finite Green-trace constant

                                            GD = D 3D−1 /8.                                    (64)

It is distinct from the scalar weighted-gap constant GD in (3).
Theorem C.1 (Matching order in the fixed-basis class). For D ≥ 3, n ≥ 2, g = V = nD and
the exact profile (61),
                          D−1
                                  n2D−2 ≤ rmin ≤ (D − 1)(1 + 4GD )n2D−2 .                      (65)
                        4(1 + 8D)

The upper map constructed below has a finite quadratic penalty with K = c + (4DH)2 /c. Thus
rmin = ΘD (n2D−2 ) for this family and observation class. This is not an exact leading constant,
efficient algorithm, all-profile optimum or uniform-penalty result.

C.1    Real modes and the exact energy decomposition
The scalar forward torus Laplacian L = i (Di+ )∗ Di+ acts componentwise on spatial vectors. It
                                              P

is real symmetric and commutes with curl and its adjoint, hence preserves U0 . Its eigenvalue at
nonzero frequency k is                    X
                                 λ(k) = 4   sin2 (πki /n) > 0.
                                                    i
There are D − 1 coexact polarizations at every nonzero frequency and none at zero, by (33).
Conjugate pairs give 2(D − 1) real modes for those two frequencies, and self-conjugate frequencies
give D−1 real modes. Equivalently the real symmetric restriction has a real counting-orthonormal
eigenbasis fs , 1 ≤ s ≤ d0 = (D − 1)(V − 1), with this same full eigenvalue multiset. There is no
further real/complex factor of two. The torus estimate (39) and the symbols give

                                           16/n2 ≤ λs ≤ 4D.
              P                                 g
Expand zα =       s zα,s fs and put zs = (zα,s )α=1 . Orthonormality gives
                                     X                             X
                            ∥z∥2 =       ∥zs ∥2 ,       QA (z) =       λs zsT Bzs .            (66)
                                     s                             s


                                                        28
For the second identity, ⟨dfs , dft ⟩ = ⟨fs , Lft ⟩ = λt δst ; the constant internal matrix B does not
alter that calculation. It also holds within degenerate eigenspaces. No independence of the
individual spatial components as coexact domains is asserted.

C.2    Selected real coordinates and a strict kernel margin
For each real mode let
                                                           g(2c/λs − a)
                                                                       
                            ks = min g, max 0,                                  .                (67)
                                                              H −a

Observe V −1/2 zα,s for α ≤ ks . Each row uses one internal channel and may mix sites and spatial
components. The row representers eα fs are an orthonormal subset on U, so the actual restricted
rank is exactly                                  X
                                           rC =      ks .                                   (68)
                                                       s

The rows are selected from the fixed profile/mode data before the field. They extend to all fields
by the same inner products, but the inequality claimed here is on U.
   In a kernel field, the first ks internal coordinates of mode s vanish. If ks = g nothing remains.
Otherwise the remaining principal block of B is
                                                     H −a T
                                       HIg−ks −          11 ,
                                                       g

whose least eigenvalue is a + (H − a)ks /g. The ceiling in (67) implies λs [a + (H − a)ks /g] ≥ 2c
whenever its positive argument applies. If the maximum argument is zero, aλs ≥ 2c already. If
the outer truncation applies there is no unobserved part of that mode. Thus (66) proves the
strict kernel bound
                               QA (x) ≥ 2c∥x∥2 (x ∈ ker(C|U )).                               (69)
These are deliberately chosen whole real Laplacian modes; no commutation of an arbitrary
observation projection with the energy was assumed.

C.3    A finite penalty on all of the actual domain
Let R be the counting orthogonal projection onto the selected row space inside U, and split
z = x + y, x = (I − R)z, y = Rz. Then x is in the kernel, x ⊥ y, and ∥Cz∥2 = V −1 ∥y∥2 exactly.
The positive energy operator on U has norm at most M∗ = 4DH, from A ≤ HI and the full
gradient norm bound 4D. Dropping QA (y) ≥ 0, applying (69) and bounding the cross term gives

                                QA (x + y) ≥ 2c∥x∥2 − 2M∗ ∥x∥∥y∥
                                               ≥ c∥x∥2 − (M∗2 /c)∥y∥2 .

The last step is Young’s inequality. Hence the finite choice K = c + M∗2 /c yields

                                  V −1 QA (z) + K∥Cz∥2 ≥ c∥z∥2V .

The margin is 2c, not merely c: one unit of c was spent controlling the cross term. No uniform
or optimal penalty is inferred.


                                                    29
C.4    Ceiling count and the finite Green trace
Since a/H = 1/(16Dn2 ) < 1/2, H − a ≥ H/2. Whether the maximum argument is positive, zero
or truncated,
                                   4g                4g X −1
                         ks ≤ 1 + 2 ,      rC ≤ d0 + 2    λ .
                                  n λs               n s s
The ceiling cost is d0 , rather than gd0 . Choose centered integer representatives of each frequency
with |ki | ≤ n/2, taking only one Nyquist representative in each even coordinate. The sine chord
estimate gives λ(k) ≥ 16|k|22 /n2 . For N = ⌊n/2⌋, overcount nonzero frequencies by every integer
point on max-norm shells ℓ = 1, . . . , N . Each shell has at most

                    (2ℓ + 1)D − (2ℓ − 1)D ≤ 2D(2ℓ + 1)D−1 ≤ 2D 3D−1 ℓD−1

points. The first inequality follows by integrating DtD−1 over the interval of length two. On
that shell |k|2 ≥ ℓ. Since D ≥ 3, N      D−3 ≤ N D−2 ≤ nD−2 , including D = 3. Therefore the
                                  P
                                    ℓ=1 ℓ
complete finite sum satisfies
                                                         N
                                              n2
                                   λ(k)−1 ≤
                            X                           X
                                                 2D3D−1     ℓD−3 ≤ GD V.                        (70)
                            k̸=0
                                              16        ℓ=1

Odd sizes and Nyquist overcounting only enlarge this upper estimate. Multiplying by the real
coexact multiplicity gives s λ−1
                              s ≤ (D − 1)GD V . Thus
                          P


             rC ≤ (D − 1)(V − 1) + 4(D − 1)GD gV /n2 ≤ (D − 1)(1 + 4GD )n2D−2 .

Here g = V = nD and V ≤ n2D−2 . The estimate need not beat the trivial full dimension at
small sizes; the actual truncation still ensures rC ≤ gd0 .
    Finally Appendix B applies to every allowed map and any penalty vanishing at zero. With
V −1 ≥ V /2 and 1+8Dn2 ≤ (1+8D)n2 , its necessary bound is at least [(D−1)/(4(1+8D))]n2D−2 .
Combining proves (65). The mixed map of the preceding appendix still has actual rank d0 =
OD (V ) on this same profile. Matching the separable order therefore strengthens the fixed-basis
comparison without producing an all-linear, basis-free, fixed-g, all-profile or physical obstruction.
The Fourier, principal-block, Young and finite-shell mechanisms used here are classical; no
historical-priority or formal-execution claim is made.


References
[1] R. L. Frank, Cwikel’s theorem and the CLR inequality, arXiv:1206.3325v1 (2012), Theorems 2.1
    and 3.1. https://arxiv.org/abs/1206.3325v1.
[2] Yu. Brudnyi, Nonlinear Piecewise Polynomial Approximation and Multivariate BV spaces of a Wiener–
    L. Young Type. I, arXiv:1511.03971v1 (2015). https://arxiv.org/abs/1511.03971v1.
[3] A. Cohen, R. DeVore, P. Petrushev and H. Xu, Nonlinear approximation and the space BV (R2 ),
    American Journal of Mathematics 121 (1999), 587–628. Author PDF: https://people.math.sc.
    edu/pencho/Publications/BV9707.pdf.
[4] D. A. Levin and Y. Peres, with contributions by E. L. Wilmer, Markov Chains and Mixing Times,
    second edition, American Mathematical Society, 2017, Lemma 1.16. Author PDF: https://pages.
    uoregon.edu/dlevin/MARKOV/markovmixing.pdf.



                                                   30

```
