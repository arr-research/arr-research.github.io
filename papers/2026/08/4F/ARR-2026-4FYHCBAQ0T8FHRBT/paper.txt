           Prescribed Tjurina Algebras and Complete Spectra
                  in Osculating-Absorbing Gauss Fibres
                                                 Lluis Eriksson

                                               August 25, 2026


                                                     Abstract
          We prove a simultaneous realization theorem for point-span osculating-absorbing Gauss
      fibres in every dimension. Given the smallest permitted support and any list of isolated
      tangent-section germs of order at least s + 1, a smooth hypersurface of every degree
                                                   X
                                          D ≥1+        (τi + 2)
                                                             i


                                            P prescribed
      can be chosen whose fibre has exactly the       P completed Tjurina algebras. Its length
      and dual multiplicity are respectively i τi and i µi . For surfaces, the classical complete
      spectrum of ordinary plane multiple points then realizes every integer fibre length between
                                    2                            
                               m+2      3s + 4s − 3             m+2 2
                                                        and             s ,
                                 2           4                    2

      while the dual multiplicity stays fixed.
         We also give a short strong-Lefschetz construction of extremal three-variable Tjurina
      algebras. The explicit ordinary germs

                                    xs+1 + y s+1 + z s+1 + (x + y + z)s+2

      attain the value s(s + 2)(2s − 1)/3, classically computed by Wahl as the minimum for positive-
      weight deformations of the Fermat cone. Our proof combines an Euler-reduced universal
      lower bound with an initial-ideal comparison and Stanley’s theorem for C[x, y, z]/(xs , y s , z s ).
      This yields sharp absorbed threefold fibres at minimal reduced support. All statements are
      over C; the degree thresholds are sufficient and not claimed minimal.


1    Introduction
For an isolated hypersurface germ h ∈ C[[x1 , . . . , xd ]], its Tjurina and Milnor numbers are

                                  C[[x1 , . . . , xd ]]                        C[[x1 , . . . , xd ]]
                 τ (h) = dimC                            ,       µ(h) = dimC                         .
                                 (h, ∂1 h, . . . , ∂d h)                       (∂1 h, . . . , ∂d h)
Fixing the order of h leaves a nontrivial minimization problem for τ . A recent finite-jet argument
gives a universal family of lower bounds and determines the exact plane minimum [8]. In three
variables its specialization is
                                             s(s + 2)(2s − 1)
                                     τ (h) ≥                  ,
                                                    3
which is sharp. For s ≥ 3, the same value was already computed by Wahl as the minimum
on positive-weight deformations of the degree-s + 1 Fermat cone [15, Example 4.7]; see also [1,
Example 4.6]. We supply a short proof for the single uniform extremizer obtained by adding the
(s + 2)-nd power of a Lefschetz linear form. This is an explicit realization and a bridge to the
global application, not a priority claim for the numerical minimum.

                                                             1
    The main purpose is geometric. For a smooth hypersurface X d ⊂ Pd+1 , the completed local
algebra of a Gauss fibre at a point is the Tjurina algebra of the corresponding tangent-section
germ [5]. Point-span order-s osculating absorption in the complete m-uple embedding forces both
order at least s + 1 and at least d+m d   reduced support points [7, 8]. Combining the universal
floor with the explicit Lefschetz realization gives a sharp dimension-three fibre endpoint.
    For surfaces, the endpoint was already known. We strengthen it in a different direction.
Classical work on ordinary plane singularities says that every integral Tjurina number between
the sharp minimum and the Milnor number occurs [2, 3, 4]. We prove that arbitrary finite lists
of these germs can be installed simultaneously on an extremal absorbed Gauss fibre. Hence the
entire integer interval of fibre lengths occurs while the multiplicity of the dual hypersurface is
fixed.
    No exhaustive priority assertion is intended. The local plane spectrum, Wahl’s three-
variable minimum, and the strong Lefschetz input are established results. The content here is
the prescribed-list realization under the absorption constraint, its complete global spectrum
consequence, and the direct Lefschetz extremizer used for the threefold endpoint.


2    The Euler-reduced lower bound in three variables
                         a
We use the convention    b = 0 for a < b, including negative upper indices.

Lemma 2.1 (Euler reduction). Let R = C[[x1 , . . . , xd ]] and h ∈ ms+1 . Put
                                                         d
                                                    1 X
                                      r =h−                 xi ∂i h.
                                                  s + 1 i=1

Then r ∈ ms+2 and
                              (h, ∂1 h, . . . , ∂d h) = (r, ∂1 h, . . . , ∂d h).

Proof. Euler’s identity cancels the homogeneous component of degree s + 1. The equality of
ideals follows directly from the displayed definition of r. Notice that the derivative generators
are not replaced by the derivatives of r.

Theorem 2.2 (Exact three-variable floor). Let s ≥ 1, and let h ∈ C[[x, y, z]] have an isolated
critical point and order at least s + 1. Then

                                                      s(s + 2)(2s − 1)
                                τ (h) ≥ Ts(3) :=                       .                      (1)
                                                             3
This is the best possible bound for every s.

Remark 2.3 (Historical scope). For s ≥ 3, Wahl computed the same sharp number in his study
of positive-weight deformations of xs+1 + y s+1 + z s+1 [15, Example 4.7]; Almirón records the
formula explicitly in [1, Example 4.6]. The lower-bound proof below applies to every isolated
germ of order at least s+1. Proposition 3.2 then gives a particularly uniform one-term extremizer.
We do not claim priority for the numerical minimum or for the abstract existence of extremal
positive-weight deformations.

Proof of the lower bound. Work in R/m2s , whose dimension is 2s+2
                                                                                   
                                                                    3 . By Lemma 2.1, the
Tjurina ideal has three generators of order at least s and one generator of order at least s + 2.
Their images are therefore spanned by at most
                                                      !         !
                                             s+2   s
                                           3     +
                                              3    3


                                                      2
coefficient multiples. Rank is at most the dimension of the source, so
                                      !                !         !
                               2s + 2    s+2   s                         s(s + 2)(2s − 1)
                    τ (h) ≥           −3     −                       =                    .
                                  3       3    3                                3
The Tjurina algebra surjects onto this truncated quotient. This proves the claim, including
s = 1, 2 under the binomial convention.


3      A strong-Lefschetz extremizer
Put ℓ = x + y + z and
                                   fs = xs+1 + y s+1 + z s+1 + ℓs+2 .                                      (2)
Its initial form is Fermat and defines a smooth plane curve. Thus fs is an ordinary isolated
hypersurface singularity of multiplicity s + 1, and µ(fs ) = s3 .
Lemma 3.1 (Lefschetz quotient). For s ≥ 1, let
                                      As = C[x, y, z]/(xs , y s , z s ).
Then
                                                  s(s + 2)(2s − 1)
                                 dimC As /(ℓs+2 ) =                .
                                                         3
Proof. For s = 1, the assertion is immediate from A1 = C, so assume s ≥ 2. The linear form
ℓ = x + y + z is a strong Lefschetz element of the monomial complete intersection As [14, 13]. If
Hj = dimC (As )j , multiplication by ℓs+2 from degree j − s − 2 to degree j has maximal rank.
Therefore
                           dim As /(ℓs+2 ) j = max{Hj − Hj−s−2 , 0}.
                                          

The Hilbert function of As is symmetric and unimodal with socle degree 3(s − 1). Its positive
difference Hj − Hj−s−2 occurs precisely for 0 ≤ j ≤ 2s − 1, and the difference is nonpositive
thereafter (eventually both terms vanish). Equivalently, the midpoint between j and j − s − 2
crosses the symmetry centre between 2s − 1 and 2s. Summing the positive part through degree
2s − 1, using Hj tj = (1 − ts )3 /(1 − t)3 , gives
              P

            2s−1
                                                !                !            !
             X                          2s + 2    s+2   s                             s(s + 2)(2s − 1)
                  (Hj − Hj−s−2 ) =             −3     −                           =                    .
            j=0
                                           3       3    3                                    3



Proposition 3.2 (Equality family). For every s ≥ 1, the germ fs in (2) satisfies
                                                              s(s + 2)(2s − 1)
                              µ(fs ) = s3 ,       τ (fs ) =                    .
                                                                     3
Proof. Euler reduction applied to (2) gives
                                1                                   1 s+2
                        fs −       (x∂x fs + y∂y fs + z∂z fs ) = −     ℓ .
                               s+1                                 s+1
Hence ℓs+2 belongs to the Tjurina ideal Is . The lowest homogeneous forms of its three derivative
generators are nonzero multiples of xs , y s , z s . Thus the m-adic initial ideal satisfies
                                      inm (Is ) ⊇ (xs , y s , z s , ℓs+2 ).
Here inm (Is ) denotes the ideal generated by the lowest nonzero homogeneous forms of all elements
of Is . Length is preserved on passage to the associated graded algebra, so Lemma 3.1 yields
                                   τ (fs ) ≤ dimC As /(ℓs+2 ) = Ts(3) .
The reverse inequality is Theorem 2.2. Finally, the ordinary leading form gives µ(fs ) = s3 .

                                                       3
   The containment of initial ideals, rather than an asserted equality, is important. It supplies
only the upper bound needed to meet the universal lower bound.


4    Absorbed Gauss fibres
Let X d ⊂ Pd+1
            C   be a smooth non-linear hypersurface, let γX : X → X ∨ be its Gauss morphism,
and fix a tangent hyperplane η = [W ]. Write Γη for the scheme-theoretic fibre and Z = (Γη )red .
Let H = OX (1) and                                                 
                         SZ = Im H 0 (Z, H m |Z )∗ −→ H 0 (X, H m )∗ .
The support is point-span order-s osculating-absorbing if
                                        s
                                   d (H m ) ⊆ SZ
                                   Osc                          (p ∈ Z).
                                      p

    We recall two inputs, with their scopes. First, if hp is a local equation of X ∩ W at p, then
                                bΓ ,p ∼
                                O     = C[[z1 , . . . , zd ]]/(hp , ∂hp ).                    (3)
                                  η


Second, absorption in the complete m-uple embedding, with 1 ≤ s ≤ m, implies
                                                                             !
                                                                        d+m
                            hp ∈ ms+1
                                  p ,            |Z| ≥ Nd,m :=              .                 (4)
                                                                         d

These facts are proved in [5, 7, 8]; they are not reproved as new results here.

Corollary 4.1 (Sharp numerical floor in dimension three). Suppose d = 3 and Z is point-span
order-s osculating-absorbing in the complete H m embedding, where 1 ≤ s ≤ m. Then
                                                                                  !
                              s(s + 2)(2s − 1)       s(s + 2)(2s − 1) m + 3
                length(Γη ) ≥                  |Z| ≥                        .
                                     3                      3           3

Both factors can be attained simultaneously at sufficiently large ambient degree, as proved in
Theorem 6.2 below.

Proof. Sum Theorem 2.2 over (3), then apply (4).


5    Simultaneous realization
The following theorem isolates the interpolation argument used for both geometric consequences.
    General deformation-theoretic realization results for prescribed singularities have a substan-
tial literature, including [10]. The theorem below uses an elementary high-degree separator
construction because it must retain the common tangent hyperplane, unisolvent support, and
absorption constraint. Its separator–Bertini architecture already appears for two ordinary local
types in [5]; here we record the heterogeneous finite-determinacy version and do not claim a new
general method for prescribed singularities.

Theorem 5.1 (Prescribed Tjurina algebras on an extremal fibre). Let d ≥ 1, 1 ≤ s ≤ m, and
N = d+m
      d . Choose N isolated convergent hypersurface germs

                            gi ∈ C{z1 , . . . , zd },         ord(gi ) ≥ s + 1,

and put
                                                 N
                                                 X
                                            E=         (τ (gi ) + 2).
                                                 i=1


                                                        4
If
                                                       D ≥ E + 1,                                           (5)
then there exist a smooth integral hypersurface X ⊂ Pd+1 of degree D, a hyperplane W , and a
tangent hyperplane point η = [W ] ∈ X ∨ such that:
               −1
     (i) Z = (γX  (η))red consists of exactly N points and dim SZ = N < h0 (X, H m );

 (ii) Z is point-span order-s osculating-absorbing;

(iii) the tangent-section germ at the i-th point is contact equivalent to gi , hence
                                         bΓ ,p ∼
                                         O η i = C[[z1 , . . . , zd ]]/(gi , ∂gi );



 (iv)
                                                N                                           N
                                                                        multη (X ∨ ) =
                                                X                                           X
                            length(Γη ) =              τ (gi ),                                   µ(gi ).
                                                i=1                                         i=1

The degree bound (5) is sufficient and is not asserted to be minimal.

Proof. Choose N points Z ⊂ W =     ∼ Pd for which degree-m evaluation is an isomorphism. One
explicit choice in an affine chart is the simplex lattice
                                                                               X
                             [1 : i1 : · · · : id ],         ij ∈ Z≥0 ,             ij ≤ m;
                                                                                j

multivariate Newton interpolation proves unisolvence.
    Put ai = τ (gi ) + 1. Isolated hypersurface germs are contact (τ + 1)-determined [9, Corol-
lary 2.24]; prescribing the ai -jet therefore fixes the contact class of gi . The elementary separator
product makes
                                                                  N
                                                                  M
                                  H 0 (Pd , O(D)) −→                    OPd ,pi /mpaii +1
                                                                  i=1
surjective once                                X
                                       D≥           (ai + 1) − 1 = E − 1.
                                                i
                                                                  a +1
Indeed, an ai -jet at pi can be multiplied by j̸=i ℓijj , where ℓij vanishes at pj and is a unit at
                                                         Q

pi . The stronger bound (5) leaves one degree after the product
                                              N
                                                a +1
                                              Y
                                                       i
                                     Pu =           ℓi,u ,          deg Pu = E,
                                              i=1

so the affine system with the prescribed jets generates first jets at every u ∈ W \ Z.
    A member singular at a specified u ∈ W \ Z imposes d + 1 linear conditions, while dim W = d.
Hence a general degree-D equation f on W is smooth away from Z and has exactly the chosen
contact types at Z.
    Embed W = V (y) in Pd+1 and set

                            FG = f + yG,                 G ∈ H 0 (Pd+1 , O(D − 1)).

Choose G general and nonzero at Z. Then X = V (FG ) is smooth: at Z its normal derivative is
                                         ̸ 0; and off W the singular-point incidence has fibre
G(p) ̸= 0; on W \ Z this follows from df =
codimension d + 2 > dim Pd+1 = d + 1. The smooth hypersurface is connected and therefore
integral. Locally on X, y = −f /G, so the tangent-section germs are contact equivalent to the
prescribed germs.

                                                              5
    The singular locus of X ∩ W is  exactly Z, hence the reduced Gauss fibre over [W ] is exactly Z.
                              d+m
Each τ (gi ) ≥ 1, while N = d ≥ m + 1; hence D ≥ E + 1 > m, and degree-m ambient forms
identify with H 0 (X, H m ). A form vanishing on Z restricts to zero on W by unisolvence, and is
consequently divisible by y. Along X, y = −f /G has order at least s + 1 at every support point.
The reverse-annihilator criterion gives order-s absorption, while evaluation gives dim SZ = N .
Properness follows from h0 (X, H m ) = d+m+1
                                           d+1   > N.
    Finally, (3) gives the length formula. The dual multiplicity formula is the sum of the local
Milnor numbers; see [12] for the classical dual-multiplicity result and [5, 6] for its use in this
fibre setting.


6     Complete surface spectra and sharp threefold fibres
Set                                          $                 %
                                             3s2 + 4s − 3
                                     Ts(2) =              .
                                                  4
An ordinary plane germ of multiplicity s + 1 has Milnor number s2 , and its Tjurina number
                              (2)
assumes every integer from Ts through s2 [4, Theorem 5.1]; that theorem in turn attributes the
spectrum to the classical sources recorded there. We use this local result rather than claiming it.
                                                                                        m+2
Theorem 6.1 (Complete absorbed surface spectrum). Let 1 ≤ s ≤ m, put N =                 2 , and
assume
                               D ≥ (s2 + 2)N + 1.
For every integer L satisfying
                                        N Ts(2) ≤ L ≤ N s2 ,
there exist a smooth integral surface X ⊂ P3 of degree D and a point-span order-s osculating-
absorbing Gauss fibre with

                     |Z| = N,       length(Γη ) = L,         multη (X ∨ ) = N s2 .

More strongly, Theorem 5.1 realizes any specified list of N ordinary plane germs of multiplicity
s + 1, including their completed Tjurina algebras.
                      (2)                                           (2)
Proof. Write L − N Ts = r1 + · · · + rN with 0 ≤ ri ≤ s2 − Ts . Such a decomposition exists
                                                                                   (2)
by a greedy choice. For each i, choose an ordinary plane germ with Tjurina number Ts + ri ,
using the cited complete local spectrum, and apply Theorem 5.1 with d = 2.

Theorem 6.2 (Sharp absorbed threefold fibres). Let 1 ≤ s ≤ m, put
                                        !
                                 m+3                       s(s + 2)(2s − 1)
                            N=       ,           Ts(3) =                    ,
                                  3                               3

and assume
                                      D ≥ Ts(3) + 2 N + 1.
                                                       

Then there exist a smooth integral threefold X ⊂ P4 of degree D and a point-span order-s
osculating-absorbing Gauss fibre such that

                   |Z| = N,       length(Γη ) = Ts(3) N,        multη (X ∨ ) = s3 N.

Thus Corollary 4.1 is sharp simultaneously in local length and reduced support size.

Proof. Apply Theorem 5.1 with d = 3 and all prescribed germs equal to fs . Proposition 3.2
supplies their Tjurina and Milnor numbers.

                                                  6
7    Scope, reproducibility, and open directions
The argument is over C. Euler division by s + 1, contact determinacy, the stated Gauss-fibre
inputs, and strong Lefschetz are used in that setting. No positive-characteristic extension is
asserted.
    The replay accompanying the paper has three deliberately separated layers. Exact binomial
arithmetic checks the formula and maximizing truncation for 1 ≤ s ≤ 50. Exact rational matrix
ranks check the relevant Lefschetz maps for 1 ≤ s ≤ 8. Sparse quotient computations over two
large prime fields directly check the displayed germ for 2 ≤ s ≤ 7. These finite fixtures test the
implementation and examples; they do not prove the universal theorems.
    The paper identifies the Euler-reduced floor with Wahl’s sharp value in three variables and
realizes it by the displayed Lefschetz family; no analogous assertion is made in four or more
variables. Classification of all equality germs is also open. For higher dimensions a recent,
non-refereed preprint gives stronger asymptotic ratio estimates and Fermat-deformation families
[11]; it is not used here. The global degree thresholds come from transparent separator products
and are probably far from optimal. The surface spectrum fixes only numerical length and dual
multiplicity unless the stronger prescribed-list statement is invoked; different Tjurina algebras of
the same length need not be isomorphic.


8    Conclusion
The prescribed-list theorem turns local Tjurina data into exact absorbed Gauss fibres at minimal
reduced support. In the plane case it upgrades endpoint sharpness to the full integer spectrum
at fixed dual multiplicity. In three variables, Euler reduction and strong Lefschetz give a direct
uniform representative of Wahl’s sharp value and hence an exact global endpoint for threefold
hypersurfaces. Equality classification, higher-variable sharpness, and optimal ambient degrees
remain distinct problems.


References
 [1] P. Almirón, On the quotient of Milnor and Tjurina numbers for two-dimensional isolated hy-
     persurface singularities, Math. Nachr. 295 (2022), 1254–1263. doi:10.1002/mana.202100371.
 [2] J. Briançon, M. Granger, and P. Maisonobe, Le nombre de modules du germe de courbe
     plane xa + y b = 0, Math. Ann. 279 (1988), 535–551. doi:10.1007/BF01456286.
 [3] S. Canino, A. Gimigliano, and M. Idà, On the Jacobian scheme of a plane curve, Comm.
     Algebra 53 (2025), 582–592. doi:10.1080/00927872.2024.2384056.
 [4] S. Canino, A. Gimigliano, and M. Idà, On the Jacobian scheme of a plane curve,
     arXiv:2302.07042v2 (2024), especially Theorem 5.1 and Remark 5.8. https://arxiv.org/
     abs/2302.07042.
 [5] L. Eriksson, Fat Gauss Fibres and Tjurina–Milnor Defects Forced by Osculating Absorp-
     tion, ARR-2026-2MZWECWVEN97ARVQ, v1 (2026). https://arr-research.github.
     io/papers/ARR-2026-2MZWECWVEN97ARVQ/.
 [6] L. Eriksson, Exact multiplicity floors for dual singularities from absorbing Gauss fi-
     bres, ARR-2026-0WAPCGQHNC82S8VJ, v1 (2026). https://arr-research.github.io/
     papers/ARR-2026-0WAPCGQHNC82S8VJ/.
 [7] L. Eriksson, Exact Higher-Osculating Rank Floors over Arbitrary Fields, ARR-
     2026-66Q8M61AA196T8BC, v2 (2026). https://arr-research.github.io/papers/
     ARR-2026-66Q8M61AA196T8BC/versions/v2/.

                                                 7
 [8] L. Eriksson, Euler-Reduced Tjurina Floors for Osculating-Absorbing Gauss Fibres,
     ARR-2026-5XEX8EX0629R997Y, v2 (2026). https://arr-research.github.io/papers/
     ARR-2026-5XEX8EX0629R997Y/versions/v2/.

 [9] G.-M. Greuel, C. Lossen, and E. Shustin, Introduction to Singularities and Deformations,
     Springer Monographs in Mathematics, Springer, 2007. doi:10.1007/3-540-28419-2.

[10] G.-M. Greuel and U. Karras, Families of varieties with prescribed singularities, Compos.
     Math. 69 (1989), 83–110. https://www.numdam.org/item/CM_1989__69_1_83_0/.

[11] X. Ma and Y. Zuo, The quotient of Milnor number by Tjurina number of hypersurface
     singularities in arbitrary characteristic, arXiv:2604.17757v1 (2026), non-refereed preprint.
     https://arxiv.org/abs/2604.17757.

[12] A. Parusiński, Multiplicity of the dual variety, Bull. Lond. Math. Soc. 23 (1991), 429–436.
     doi:10.1112/blms/23.5.429.

[13] H. V. N. Phuong and Q. H. Tran, A new proof of Stanley’s theorem on the strong Lefschetz
     property, Colloq. Math. 173 (2023), 1–8. doi:10.4064/cm8987-11-2022.

[14] R. P. Stanley, Weyl groups, the hard Lefschetz theorem, and the Sperner property, SIAM J.
     Algebraic Discrete Methods 1 (1980), 168–184. doi:10.1137/0601021.

[15] J. M. Wahl, A characterization of quasi-homogeneous Gorenstein surface singularities,
     Compos. Math. 55 (1985), 269–288, especially Example 4.7. https://www.numdam.org/
     item/CM_1985__55_3_269_0/.




                                               8
