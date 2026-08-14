# Algebraic Query Support for Unitary Oracles: Exact Hilbert Laws, Harmonic Spectra, and General-Tester Bounds

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Algebraic Query Support for Unitary Oracles
    Exact Hilbert Laws, Harmonic Spectra, and General-Tester
                            Bounds
                                             Lluis Eriksson

                                              August 2026


                                                 Abstract
          The usual dimension bound for discrimination with k calls to a d-level unitary oracle is
                                                2
      the ambient symmetric-tensor count k+dk −1 . It ignores polynomial relations satisfied by a
                                                   

      restricted oracle family. We show that the exact linear support exposed by k forward calls is
      instead the degree-k Hilbert function of the projective Zariski closure of that family. Every
      causally ordered k-query protocol consequently obeys a Hilbert-rank discrimination bound.
          For the noncentral, nontraceless fixed-angle qubit class U (n) = qI − irn · σ, n ∈ S 2 ,
         ̸ 0, this gives the exact quadratic law HX (k) = (k + 1)2 , rather than the unrestricted
      qr =
      cubic count k+33 . At the traceless endpoint the rank is
                                                                k+2
                                                                  2 , while a central class has rank
      one. We use the transitive orbit average and its constant leverage score to prove the stronger
      operational statement
                                           GEN
                                         Psucc  ≤ min{1, Dk /M }
      for every uniform M -hypothesis subset and every general   tester. Thus the2 fixed-angle promise
      refines the unrestricted general-tester numerator k+3  3     to Dk = (k + 1) . Beyond qubits, a
      selective phase oracle on an unknown ray in Cd has projective closure equal to a linearly
                                                               2
      transformed Segre variety. Its exact support is k+d−1
                                                         d−1      : the ambient degree d2 − 1 collapses
                                                  2       2
      to 2d − 2, and the two-query defect is d (d − 1) /4. We then diagonalize the continuous
      k-copy Bell frame exactly: its eigenvalues are finite Funk–Hecke sums indexed by spherical
      harmonics of ranks 0 ≤ ℓ ≤ k. This yields an exact purity and a participation dimension that
      grows only linearly in k, despite quadratic algebraic support. We prove that the continuous
      frame is tight in the interior only for one query at q 2 = 1/4; it is never tight there for k ≥ 2.
      Spherical 2k-designs inherit the same spectrum. Great-circle oracles form a conic subfamily
      with exact rank 2k + 1 and a closed Fourier spectrum. The results separate support rank,
      effective rank, and operational attainability. They do not assert that every full-rank ensemble
      attains the dimension bound or that every general process matrix has a laboratory realization.


1    Introduction
A k-query circuit can only create amplitudes that are homogeneous polynomials of degree
k in the entries of its oracle. The polynomial method is foundational in quantum query
complexity [1, 2]. In unitary channel discrimination, an analogous ambient count gives the
                   2
general bound k+dk −1 /M for M equiprobable d-dimensional unitary hypotheses [3]. That count
                      

is optimal without structural information about the oracle set. It is not intrinsic to a constrained
family.
    The missing datum is the homogeneous ideal of the oracle family. If the allowed projective
matrices lie on an algebraic variety X, every equation in I(X) removes a symmetric-tensor
direction. The surviving number of directions is exactly the Hilbert function HX (k) [4]. This
observation turns the ambient polynomial method into a geometry-sensitive query bound.



                                                      1
```

---

## Page 2

```text
Our main application is physically elementary but structurally nontrivial. Fix the eigenphases
of an SU (2) gate and vary only its rotation axis:

          U (n) = e−iθn·σ/2 = qI − ir n · σ,    q = cos(θ/2),   r = sin(θ/2),   n ∈ S2.           (1)

Here q, r ∈ R, q 2 + r2 = 1, and Tr U = 2q. Although channel representatives have an arbitrary
global phase, the promise itself is the phase-invariant quantity | Tr U |2 /4 = q 2 ; the displayed
representatives fix the SU (2) convention. Physically, the sphere describes a pulse with known
rotation angle and unknown field axis. This is a conjugacy class of fixed-angle qubit rotations,
a family also appearing in quantum learning of rotations about an unknown direction [5]. Its
nondegenerate projective closure is a quadric surface, so its k-query support grows as (k + 1)2 .
The result sharpens the unrestricted qubit count by
                                                           
                                   k+3            2      k+1
                                         − (k + 1) =            .                                (2)
                                     3                     3
At two queries this is a one-dimensional defect; at general k it is a cubic cumulative deficit.
   The contributions are:

   1. an oracle-variety theorem identifying exact causal query support with a Hilbert function,
      together with uniform and nonuniform causal bounds;

   2. the complete three-branch rank law for fixed-angle qubit rotations and the exact rank law
      for a great-circle restriction;

   3. an arbitrary-dimension law for rank-one selective-phase oracles, whose Segre geometry
      changes the ambient support exponent from d2 − 1 to 2d − 2;

   4. a transitive-orbit leverage theorem  refining the ultimate general-tester bound of Bavaresco–
      Murao–Quintino from k+3
                                   
                                 3   /M to  Dk /M on the fixed-angle class;

   5. a finite closed formula for every eigenvalue of the continuous k-copy frame, including
      endpoint cascades, exact purity, and effective rank;

   6. a sharp obstruction showing that one-query tightness does not persist at any interior angle
      for k ≥ 2;

   7. an exact positive-scalability criterion that distinguishes a dimension upper bound from its
      attainability by a fixed effective state family.

    The harmonic analysis, Hilbert functions, leverage inequality, and spherical designs used
below are classical [6, 7]. The claimed contribution is their exact synthesis with algebraic
quantum-query support and general-tester discrimination. We do not claim new general theory
of spherical harmonics, algebraic varieties, or process matrices.
    Dimensional and linear-independence bounds for repeated gate identification are direct
antecedents [8, 9]. Likewise, the orbit-average domination mechanism is classical in covariant
quantum estimation [10] and appears explicitly in the ultimate general-tester proof of [3, Appendix
F]. Our new claim is therefore the exact promise-class numerator, its singular branch diagram, and
the accompanying all-k harmonic spectra—not a new tester formalism or a first orbit-domination
lemma.
    She and Yuen’s generalized polynomial method shows that a T -query unitary property test
has an acceptance polynomial of degree at most 2T and uses invariant theory to derive property-
testing lower bounds [2]. Our statement is complementary: it concerns the exact pure-state
span of k forward calls, uses the full homogeneous ideal rather than an invariant acceptance
polynomial, and feeds that span into finite-ensemble channel discrimination. We do not claim to
originate the unitary polynomial method.

                                                 2
```

---

## Page 3

```text
Table 1: Priority boundary: classical mechanisms versus the consequences derived here.
Source                   Established mechanism                    Present use or additional conclusion
Beals et al.; She–Yuen   Query amplitudes/acceptance prob-        The full oracle ideal gives the exact
                         abilities are low-degree polynomi-       pure-state support HX (k) and a finite-
                         als; invariant theory yields property-   ensemble rank converse.
                         testing bounds.
Bavaresco et al.         Ambient symmetric-tensor domina-         The orbit numerator is replaced by the
                         tion for general testers.                exact promise rank Dk , including all
                                                                  singular branches.
Funk–Hecke and spher-    Harmonic diagonalization and exact       Exact fixed-angle spectra, purity, end-
ical designs             cubature for polynomial kernels.         point cascades, and the all-k tightness
                                                                  obstruction.
Segre geometry           Rank-one matrices have coordinate        Selective-phase qudit oracles acquire
                                                                                 2
                         space H 0 (O(k, k)).                     support k+d−1      and a GEN discrimi-
                                                                             d−1
                                                                  nation cap.


   The k = 2 identity 10 → 9 was previously isolated for a specific 24-echo tetrahedral ensemble,
together with a causal saturation certificate, in [11]. Here it is one instance of an all-k law for
arbitrary fixed-angle subsets. The present work additionally treats the three singular branches,
compact-orbit general testers, exact continuous spectra, and the planar-axis restriction; it does
not reuse the special tetrahedral attainment certificate.


2    Forward-query model and projective oracle families
Let V be a finite-dimensional complex vector space containing the matrix entries of an oracle. A
unitary channel is unchanged by multiplying its implementing matrix by a global phase, so oracle
matrices naturally determine points of P(V ). Let U ⊂ P(V ) be a family of projective unitary
                        Z
matrices and let X = U denote its complex projective Zariski closure. Write
                                                            
                                 HX (k) = dimC C[V ]/I(X) k                                   (3)

for its degree-k Hilbert function.
    We use the standard forward-oracle model: each query inserts the same unknown unitary U ,
not U † and not a controlled version of an otherwise uncontrolled black box. Arbitrary known
isometries, ancillas, coherent feedback, and intermediate measurements are allowed. Intermediate
measurements can be deferred after adding a record system.
    We also use the general-tester model of Bavaresco–Murao–Quintino [3]. For a d-level unitary
let
                                             d−1
                                             X
                            |U ⟩⟩ = (I ⊗ U )     |a⟩|a⟩, JU = |U ⟩⟩⟨⟨U |.                    (4)
                                            a=0
Thus Tr JUP= d and TrO JU = I. A general k-copy tester is a family Ti ≥ 0 whose deterministic
sum W = i Ti obeys
                                Tr[W (C1 ⊗ · · · ⊗ Ck )] = 1                              (5)
for every tuple of channel Choi operators C1 , . . . , Ck . This feasible class contains parallel and
causally ordered testers and is the mathematical general-process class used in that reference. We
do not assume that every element has a laboratory realization.
Lemma 2.1 (Multilinear normal form). For every purified causally ordered circuit making k
forward calls to U , there is a fixed linear map L, independent of U , such that its final pure state
satisfies
                                            |ΨU ⟩ = L U ⊗k .                                      (6)

                                                   3
```

---

## Page 4

```text
Tensor-factor permutations, fixed input vectors, ancillary identities, and all intermediate isome-
tries are absorbed into L.
Proof. Expand the circuit in fixed bases. Every path amplitude contains exactly one matrix
entry from each oracle call and hence is a homogeneous degree-k polynomial in the entries of U .
Collecting its coefficients defines L. Purifying every known channel and coherently storing every
measurement outcome reduces the general causal circuit to this case without changing the best
final discrimination probability.


3    The oracle-variety query law
Theorem 3.1 (Hilbert query-support law). For every k ≥ 0,
                                                  
                         dim span{U ⊗k : [U ] ∈ U } = HX (k).                                     (7)

Consequently, the final states of every purified causal k-query circuit have linear span of dimension
at most HX (k).
Proof. The Veronese vector U ⊗k belongs to Symk (V ). Its annihilator inside Symk (V )∗ con-
sists exactly of homogeneous degree-k polynomials that vanish on U. Polynomial vanishing is
unchanged by Zariski closure, so the annihilator is I(X)k . Rank–nullity gives
                                  
                   dim span{U ⊗k } = dim Symk (V ) − dim I(X)k = HX (k).                 (8)

The circuit statement follows from theorem 2.1 because a fixed linear map cannot increase span
dimension.

    The support value in theorem 3.1 is operationally exposed by a causal parallel architecture:
feed the k calls with k Bell pairs. The resulting pure vector is |U ⟩⟩⊗k , and vectorization is
injective, so its hypothesis span has dimension exactly HX (k). Thus HX (k) is the maximum
causal support, not merely an upper bound on it.
Corollary 3.2 (Causal discrimination bounds). Let U1 , . . . , UM ∈ U have priors pi . Every
causal k-query protocol satisfies

                         Psucc ≤ min{1, pmax HX (k)},       pmax = max pi .                       (9)
                                                                      i

For uniform priors this becomes Psucc ≤ min{1, HX (k)/M }.
Proof. Let P project onto the span of the purified final hypothesis vectors and let {Mi } be the
final POVM. Since |Ψi ⟩⟨Ψi | ≤ P ,
                             X
                   Psucc =      pi Tr(Mi |Ψi ⟩⟨Ψi |)                                        (10)
                               i
                                    X
                           ≤ pmax       Tr(P Mi P ) = pmax Tr P ≤ pmax HX (k).                  (11)
                                    i




    If X has positive projective dimension s and degree ∆, its Hilbert polynomial gives
                                                ∆ s
                                     HX (k) =      k + O(k s−1 ).                               (12)
                                                s!
Thus the geometry of the oracle family fixes the exponent of accessible support. A necessary
asymptotic condition for perfect identification of M generic hypotheses is k ≳ (s!M/∆)1/s . It is
only necessary: positivity and the geometry of the finite ensemble can impose further obstructions.

                                                  4
```

---

## Page 5

```text
Remark 3.3 (Relation to the polynomial method). The fact that query amplitudes are low-
degree polynomials is classical in Boolean-oracle complexity [1]. Theorem 3.1 identifies the
exact quotient dimension after imposing the homogeneous ideal of a continuous matrix-oracle
                   2                                        2
family. For X = Pd −1 it reduces to the ambient count k+dk −1 used in the general unitary
                                                                

discrimination bound [3].


4    Transitive orbits: an ultimate general-tester bound
The Hilbert law above applies to arbitrary projective oracle families but is proved through causal
circuit amplitudes. Transitive unitary orbits admit a stronger statement because their leverage
score is constant.
Lemma 4.1 (Compact-orbit leverage). Let a compact group act transitively on a unitary orbit
{Ux : x ∈ Ω}, with invariant probability measure µ. Set
                                          Z
                             ⊗k
                  vx = |Ux ⟩⟩ ,     J k = |vx ⟩⟨vx | dµ(x), Dk = rank J k .            (13)
                                                Ω
Then, for every x,
                                           |vx ⟩⟨vx | ≤ Dk J k .                                 (14)
The constant Dk is the smallest orbit-independent constant for which this operator inequality
holds.
Proof. The orbit representation is unitary, so J k and its Moore–Penrose inverse commute with
                        +
it. Hence L(x) = ⟨vx |J k |vx ⟩ is constant. Averaging gives
                                                         +
                                       L(x) = Tr(J k J k ) = Dk .                                (15)
For A ≥ 0 and v ∈ ran A, Cauchy–Schwarz applied to A+1/2 v gives |v⟩⟨v| ≤ ⟨v|A+ |v⟩A. This
                                      +      +
proves equation (14). Applying ⟨vx |J k (·)J k |vx ⟩ to any uniform domination shows that its
constant cannot be smaller than Dk .

Theorem 4.2 (Ultimate bound on a transitive unitary orbit). Let U1 , . . . , UM be any finite
subset of a compact transitive unitary orbit and suppose the labels are equiprobable. Every general
k-copy tester satisfies                                   
                                       GEN             Dk
                                      Psucc  ≤ min 1,        .                                 (16)
                                                       M
                                           GEN ≤ min{1, p
For arbitrary priors, the safe variant is Psucc           max Dk }.

Proof. Write Ji = JUi and W = i Ti . By theorem 4.1, Ji⊗k ≤ Dk J k . Positivity and equation (5)
                                 P
give
                                            1 X
                                   Psucc =      Tr(Ti Ji⊗k )                                (17)
                                           M
                                                     i
                                               Dk              Dk
                                           ≤      Tr(W J k ) =    ,                              (18)
                                               M               M
because Tr(W JU⊗k
                x
                  ) = 1 for every x and hence also after averaging. Replacing each prior by pmax
proves the nonuniform bound.

    When Dk ≤ M , equality at Dk /M is not automatic. With Ai = Dk J k − Ji⊗k ≥ 0, it holds
for a given tester if and only if Tr(Ti Ai ) = 0 for every i. If P projects onto ran J k , this forces
                                                +            +
                                P Ti P = ci |J k vi ⟩⟨J k vi |,    ci ≥ 0,                       (19)
together with the deterministic-tester normalization. Thus full orbit span is necessary but not
sufficient for attaining the cap.

                                                         5
```

---

## Page 6

```text
5      Fixed-angle qubit rotations: three exact branches
In the Pauli basis, equation (1) has projective coordinates [x0 : x1 : x2 : x3 ] = [q : −irn1 : −irn2 :
−irn3 ].

Theorem 5.1 (Fixed-angle rank law). For k ≥ 1, define

                                Vk (q, r) = spanC {U (n)⊗k : n ∈ S 2 }.                           (20)

Then                                         
                                             
                                             (k + 1)2 ,    qr ̸= 0,
                                             
                                             
                                               k+2
                                                   
                             dim Vk (q, r) =     2   ,      q = 0, r ̸= 0,                        (21)
                                             
                                             
                                             
                                              1,            r = 0.
                                             

For qr ̸= 0, generic M axes have finite-ensemble rank min{M, (k + 1)2 }.

Proof. When qr ̸= 0, the projective closure is the smooth quadric

                                                       r2
                                    x21 + x22 + x23 = − 2 x20 ⊂ P3 .                              (22)
                                                       q

Its Hilbert series is (1 − t2 )/(1 − t)4 , whose degree-k coefficient is
                                                    
                                     k+3          k+1
                                              −          = (k + 1)2 .                             (23)
                                        3          3

Equivalently, the feature blocks are all symmetric monomials in L    n of degrees 0, . . . , k. Fischer
                                                                       k
decomposition identifies their restrictions to the sphere with
Pk                                                                     ℓ=0 Hℓ , of total dimension
                        2
  ℓ=0 (2ℓ + 1) = (k + 1) .
   If q = 0, only the homogeneous degree-k feature remains. The tensors n⊗k span Symk (C3 ): a
homogeneous polynomial vanishing on the real unit sphere vanisheson every nonzero real vector
by scaling and therefore vanishes identically. The dimension is k+22 . If r = 0, the class contains
one projective oracle. Finally, because the full evaluation span has the displayed finite dimension,
some set of that many axes is independent; nonvanishing of an evaluation minor is Zariski open,
which proves the generic finite-set statement.

   At the traceless endpoint U (−n) = −U (n), so antipodal axes implement the same unitary
channel. The physical promise space is therefore RP2 , not a sphere of distinct channel labels.
Counting both n and −n as different hypotheses would introduce an unavoidable label ambiguity
and cannot lead to perfect channel identification.

Corollary 5.2 (Ultimate fixed-angle query bound). For M equiprobable fixed-angle qubit hy-
potheses with qr ̸= 0,
                                                     (k + 1)2
                                                             
                                   GEN
                                  Psucc (k) ≤ min 1,            .                     (24)
                                                        M
                                     √
Perfect identification requires k ≥ ⌈ M ⌉ − 1. At q = 0 it instead requires k+2
                                                                               
                                                                             2   ≥ M.

Proof. The SU (2) conjugation action is transitive on the fixed-angle sphere, so theorem 4.2
applies with the ranks in theorem 5.1. The query conditions follow by requiring the relevant
numerator to be at least M . They are necessary, not sufficient.




                                                   6
```

---

## Page 7

```text
Table 2: Exact k-query support dimensions for the indicated qubit oracle families and singular
branches.
     Oracle geometry                  defining structure             support dimension
                                                                      k+3
     unrestricted projective matrices P3
                                                                          
                                                                        3
     fixed angle, qr ̸= 0             quadric surface                (k + 1)2
                                                                      k+2
                                                                          
     traceless fixed angle            homogeneous sphere features       2
     fixed-angle great circle         plane conic                    2k + 1
     traceless great circle           homogeneous binary features k + 1
     central class                    one point                      1


                   Algebraic and effective support                                           Bell-frame spectrum: k = 6, q2 = 1/4
            1750    ambient ( k +3 3 )                                                10−1
            1500    sphere (k + 1)2
                    circle 2k + 1
            1250    Reff at q 2 = 1/4

                                                                             ℓ
                                                                      eigenvalue λk
dimension




            1000
                                                                                      10−2
             750
             500
             250
               0                                                                      10−3
                          5            10           15           20                             0   1    2    3     4     5   6
                                     queries k                                                          harmonic rank ℓ

Figure 1: Left: unrestricted, fixed-sphere, and fixed-circle query dimensions, together with
the Bell-frame effective rank at q 2 = 1/4. The fixed-angle promise changes the general-tester
numerator from cubic to quadratic, while a planar-axis promise makes it linear. Right: the exact
harmonic eigenvalues at k = 6 illustrate why effective and algebraic ranks differ.


6            Rank-one phase oracles in arbitrary dimension
The qubit quadric is the first member of a higher-dimensional family with a more dramatic
support reduction. Let d ≥ 2, let |ψ⟩ ∈ Cd be an unknown unit vector, and consider the selective
phase oracle
                       Uψ = I + cPψ ,      Pψ = |ψ⟩⟨ψ|,    c = eiϑ − 1.                     (25)
It applies the known phase eiϑ to one unknown ray and acts as the identity on its orthogonal
complement. The promise is transitive under unitary conjugation.

Theorem 6.1 (Segre query-support law). For k ≥ 1, set

                                         Dd,k (c) = dim span{Uψ⊗k : |ψ⟩ ∈ Cd , ∥ψ∥ = 1}.                                          (26)

Then                                                      
                                                          
                                                          
                                                          1,                          c = 0,
                                                          
                                                             k+2
                                                                 
                                             Dd,k (c) =       2 ,                      d = 2, c = −2,                             (27)
                                                          
                                                           k+d−12 ,
                                                          
                                                          
                                                                d−1                    otherwise.
On the generic branch the support exponent is 2d − 2, rather than the unrestricted matrix exponent
d2 − 1.


                                                                      7
```

---

## Page 8

```text
Proof. Projective rank-one matrices form the Segre variety

                               Σd = Pd−1 × (Pd−1 )∗ ,→ P(End Cd ).                             (28)

The physical projectors are Zariski dense in Σd : equivalently, the U (d) orbit complexifies to the
dense GLd orbit of rank-one matrices with nonzero trace. Define the linear map

                                     Lc (X) = Tr(X)I + cX.                                     (29)

For Tr Pψ = 1, one has Lc (Pψ ) = Uψ . On the scalar and traceless summands of End Cd , the
eigenvalues of Lc are respectively c + d and c. Hence Lc is invertible unless c = 0 or c = −d.
    When it is invertible, the projective oracle closure is a linear image of Σd . Its degree-k
coordinate space is
                           H 0 (Σd , O(k, k)) ∼
                                              = Symk (Cd )∗ ⊗ Symk (Cd ),                    (30)
                    2
of dimension k+d−1
                d−1    . The Hilbert query-support law now gives the last line of equation (27).
    For a unit-modulus phase, c = −d can occur only when d = 2 and c = −2. Then Lc kills the
scalar coordinate and sends   the Bloch projectors onto the projective traceless space P2 , whose
                     k+2
                         
Hilbert function is 2 . Finally, c = 0 makes every oracle equal to I.

Corollary 6.2 (Qudit phase-oracle discrimination). For M equiprobable hypotheses from the
orbit in equation (25), every general k-copy tester obeys
                                   GEN
                                  Psucc ≤ min{1, Dd,k (c)/M }.                                 (31)

On the generic branch, perfect identification therefore requires

                                           k+d−1 2
                                               
                                                   ≥ M.                                        (32)
                                            d−1

At two queries the exact reduction from the unrestricted support is

                                        d + 1 2 d2 (d − 1)2
                                2         
                                d +1
                                      −        =            .                                  (33)
                                   2      2          4

Thus the qutrit support is 36 rather than 45, and the four-level support is 100 rather than 136.

Proof. The orbit is compact and transitive, so theorem 4.2 applies with theorem 6.1. Equation (33)
is an elementary simplification of the two displayed dimensions.

    For fixed d and large k, the generic support satisfies

                                                k 2d−2
                                Dd,k (c) =               + O(k 2d−3 ),                         (34)
                                             ((d − 1)!)2
                                      2                      2
whereas the unrestricted support is k d −1 /(d2 −1)!+O(k d −2 ). The promise therefore changes not
only a constant but the polynomial growth exponent. When d = 2, the generic Segre law reduces
to (k + 1)2 , and its exceptional phase c = −2 is exactly the traceless branch of theorem 5.1.


7    When is a support bound attained?
Rank alone does not construct a tester. The following statement concerns a fixed family of
effective pure states, after the query architecture has been chosen; it is not an existence theorem
for a causal architecture.



                                                   8
```

---

## Page 9

```text
Theorem 7.1 (Fixed-state scalability criterion). Let |ϕi ⟩ be normalized vectors with Gram matrix
K, common span projector P , and rank D. For uniform priors, their dimension bound D/M is
attained if and only if there are weights ci ≥ 0 such that
                                         X
                                             ci |ϕi ⟩⟨ϕi | = P.                              (35)
                                                   i

Equivalently, for C = diag(ci ),
                                                       KCK = K.                                               (36)
               P
In that case   i ci = D and Mi = ci |ϕi ⟩⟨ϕi | is an attaining POVM on the support.

Proof. The estimate Tr(Mi |ϕi ⟩⟨ϕi |) ≤ Tr(P Mi P ) is an equality only if the compressed positive
operator P Mi P is supported on Cϕi . Equality in the sum therefore forces P Mi P = ci |ϕi ⟩⟨ϕi |
and POVM completeness       gives equation (35). Conversely, equation (35) supplies a POVM with
            −1
               P
success M        i ci = D/M . Multiplying the frame identity by the analysis and synthesis maps
gives
P       equation (36); the reverse implication holds on the frame range. Taking the trace gives
   i ci = D.

    This criterion isolates three logically different resources: algebraic support D, the ability of a
circuit to realize useful vectors inside that support, and positive scalability of those vectors. A
full-rank evaluation table need not satisfy the last condition.


8    Exact harmonic spectrum of the continuous class
Use normalized one-query Bell/Choi vectors
                                             3
                                             X
                      |un ⟩ = q|0⟩ − ir            na |a⟩,            ⟨un |um ⟩ = a + b n · m,                (37)
                                             a=1

where a = q 2 , b = r2 , and a + b = 1. Define the continuous k-copy frame operator
                                          Z
                                     Fk =     |un ⟩⟨un |⊗k dω(n),                                             (38)
                                                       S2

with normalized area measure.

Theorem 8.1 (Funk–Hecke spectrum). If ab > 0, the nonzero eigenvalues of Fk are
                                             ×(2ℓ+1)
                                          λkℓ               ,        0 ≤ ℓ ≤ k,                               (39)

where
                                       Z 1
                                   1
                          λkℓ =           (a + bx)k Pℓ (x) dx                                                 (40)
                                   2   −1
                                       X k                       j!
                              =                  ak−j bj                        .                             (41)
                                              j          (j − ℓ)!!(j + ℓ + 1)!!
                                    ℓ≤j≤k
                                   j−ℓ even

                                                            Pk
Every displayed eigenvalue is positive and                      ℓ=0 (2ℓ + 1)λkℓ = 1. At a = 0, exactly the sectors
ℓ ≡ k (mod 2) survive.




                                                                 9
```

---

## Page 10

```text
Proof. The integral operator with the same nonzero spectrum as Fk has zonal kernel (a + bn · m)k .
Funk–Hecke diagonalizes it on each spherical harmonic space Hℓ and gives equation (40).
Expanding the binomial and using

                            1 1 j
                              Z
                                                          j!
                                  x Pℓ (x) dx =                                              (42)
                            2 −1                (j − ℓ)!!(j + ℓ + 1)!!

when j ≥ ℓ has the same parity as ℓ, and zero otherwise, proves equation (41). The j = ℓ
term proves positivity for ab > 0. The trace identity follows by evaluating the kernel on the
diagonal.

Proposition 8.2 (Exact purity and effective rank). For b > 0,

                               1 − (a − b)2k+1                              2b(2k + 1)
                    Tr Fk2 =                   ,           Reff (Fk ) =                   .     (43)
                                 2b(2k + 1)                               1 − (a − b)2k+1

For every fixed interior angle, Reff (Fk ) = 2b(2k + 1) + o(1) as k → ∞, whereas rank Fk = (k + 1)2 .

Proof. Using two independent axes and rotational invariance,
                                   ZZ
                               2
                           Tr Fk =      |⟨un |um ⟩|2k dω(n)dω(m)                                (44)

                                   1 1
                                     Z
                                 =        (a + bx)2k dx,                                        (45)
                                   2 −1

which integrates to equation (43), since a + b = 1. For 0 < a, b < 1 one has |a − b| < 1, giving
the asymptotic statement.

   Thus algebraic support and participation dimension have different scaling: the former is
quadratic and the latter linear. The exact frame entropy is also immediately available as
                                                k
                                                X
                                  S(Fk ) = −      (2ℓ + 1)λkℓ log λkℓ ,                         (46)
                                                ℓ=0

but no entropy optimality is asserted here.

8.1   Endpoint cascades
The rank jumps in equation (21) are resolved spectrally. As b ↓ 0,

                                               k!
                               λkℓ =                      ak−ℓ bℓ + O(bℓ+1 ),                   (47)
                                       (k − ℓ)!(2ℓ + 1)!!

so angular sectors disappear successively with harmonic rank. As a ↓ 0, sectors with k − ℓ even
have nonzero limits
                                                    k!
                                 λkℓ −→                          ,                          (48)
                                          (k − ℓ)!!(k + ℓ + 1)!!
whereas opposite-parity sectors vanish at least linearly in a = q 2 . More precisely, when k − ℓ is
odd,
                                             k!
                            λkℓ =                         a + O(a2 ).                         (49)
                                   (k − ℓ − 1)!!(k + ℓ)!!
Exactly k(k + 1)/2 dimensions disappear at the traceless endpoint.




                                                      10
```

---

## Page 11

```text
9    Interior tightness is a one-query phenomenon
Theorem 9.1 (Sharp interior tightness obstruction). For ab > 0, the continuous frame Fk is
tight on its support if and only if k = 1 and a = q 2 = 1/4. In particular, it is never tight for any
k ≥ 2 at an interior fixed angle.

Proof. For k = 1, equation (41) gives λ10 = a and λ11 = b/3, so equality holds exactly at a = 1/4.
Let k ≥ 2. Equality of the top two harmonic eigenvalues would force
                                      λk,k−1           a
                                             = (2k + 1) = 1.                                     (50)
                                       λk,k            b

At the resulting ratio a/b = 1/(2k + 1), direct evaluation of the next sector gives

                     λk,k−2   2k + 1                     k(2k + 3)
                            =          1 + (2k − 1)(a/b)2 =          > 1.                        (51)
                      λk,k      2                           2k + 1

The three sectors therefore cannot share one eigenvalue.

    At the traceless endpoint a = 0, the one-query frame is tight on its three-dimensional
support, while for k ≥ 2 its surviving sectors already have unequal top eigenvalues because
λk,k−2 /λk,k = (2k + 1)/2 ̸= 1. At the central endpoint a = 1 the frame has rank one and is
trivially tight for every k. These endpoint statements are separate from the interior theorem.

Corollary 9.2 (No positive reweighting restores Bell tightness). For ab > 0 and k ≥ 2, no finite
nonzero positive measure on the full fixed-angle orbit can make the k-copy Bell vectors a tight
frame on their complete (k + 1)2 -dimensional span.

Proof. Let Pℓ project onto the harmonic sector Hℓ . Transitivity makes ∥Pℓ u⊗k    2
                                                                              n ∥ independent of
n; its value is (2ℓ + 1)λkℓ . Therefore every positive weighted frame of total mass w has sector
trace w(2ℓ + 1)λkℓ . A scalar multiple of the full support projector would instead have sector
trace proportional to 2ℓ + 1, forcing all λkℓ to coincide. Theorem 9.1 excludes this for k ≥ 2.

Corollary 9.3 (Transfer to spherical designs). If a finite weighted axis set is a spherical 2k-design,
its discrete k-copy Bell frame equals Fk and has exactly the spectrum in theorem 8.1. Hence no
such equal-weight frame is tight for k ≥ 2 at an interior angle.

Proof. Every matrix entry of the frame integrand is a polynomial of total degree at most 2k in
the axis coordinates. The design identity therefore replaces the integral exactly by the finite
weighted sum.

   The corollary does not say that every design is a transitive group orbit, nor that no alternative
query input can attain the general-tester dimension cap.


10     Planar-axis oracles: conic rank and Fourier spectrum
Restrict the axis to n(φ) = (cos φ, sin φ, 0). The projective closure is a plane conic. This is a
control promise in which the unknown field axis is known a priori to lie in a plane (two available
quadratures), rather than a separate physical memory resource.

Theorem 10.1 (Great-circle law). For ab > 0,
                                                     
                    dim span{U (n(φ))⊗k : φ ∈ [0, 2π)} = 2k + 1.                                 (52)




                                                 11
```

---

## Page 12

```text
The continuous frame has Fourier eigenvalues
                         X k                 
                                                    j
                                                         
                µkm =              ak−j bj 2−j            ,             −k ≤ m ≤ k.             (53)
                                j               (j − m)/2
                          |m|≤j≤k
                         j−m even

All are positive. At a = 0, only modes m ≡ k (mod 2) survive and the rank becomes k + 1.

Proof. The kernel is (a+b cos(φ−ψ))k . Its Fourier support is contained in −k, . . . , k, and the j =
|m| term is nonzero when ab > 0, proving exact rank 2k + 1. Expanding cosj θ = 2−j (eiθ + e−iθ )j
gives equation (53). If a = 0, only j = k remains.

   At a = 0, antipodal points again differ only by global phase, so the physical channel
family is RP1 . Distinct-hypothesis counts must quotient this identification before applying a
perfect-discrimination criterion.
   Because rotations around the normal act transitively on the circle, theorem 4.2 also gives
                                      
                                      min{1, (2k + 1)/M }, ab > 0,
                                      
                            GEN,circ
                          Psucc      ≤ min{1, (k + 1)/M },   a = 0,                        (54)
                                      
                                       1/M,                  b = 0.
                                      

   The circle is an explicit warning against inferring support dimension from the number of
continuous parameters alone: both the sphere and the circle are infinite families, but their Hilbert
functions are respectively quadratic and linear.


11     Operational consequences and comparisons
For nondegenerate fixed-angle qubit oracles, the accessible support hierarchy is
                                                              
                                                         k+3
                          Reff (Fk ) ≤ rank Fk ≤                    .                           (55)
                          | {z }       | {z }               3
                            Θ(k)        (k+1)2         | {z }
                                                       unrestricted ambient

Each quantity answers a different question. The first measures spectral participation of one
canonical continuous Bell encoding; the second is the maximum algebraic support exposed by
the oracle family; the third ignores the fixed-angle relation.
    For example, M = 24 generic fixed-angle hypotheses cannot be perfectly identified with fewer
than four forward queries, because (k + 1)2 < 24 for k ≤ 3. This is a necessary query lower
bound, not a four-query construction. At k = 2, the family-specific support cap is 9/M , whereas
the unrestricted qubit cap is 10/M . The all-k deficit in equation (2) shows that this is the first
member of a growing sequence rather than an isolated accident. The earlier tetrahedral-echo
paper [11] proves this k = 2 defect for one nontransitive 24-label ensemble and, crucially, certifies
causal attainment there. The present result generalizes the support defect to all k and arbitrary
fixed-angle subsets, extends the bound to the transitive-orbit GEN class, and adds the singular
branch laws and exact sphere/circle spectra; it makes no new claim about that ensemble’s
adaptive certificate.
    More sharply, the class-to-ambient ratio is

                                    (k + 1)2       6(k + 1)     6
                                      k+3
                                           =                  ∼ .                              (56)
                                      3
                                                (k + 2)(k + 3)  k

Thus the promise removes an asymptotically dominant fraction of the ambient query space, not
merely a fixed finite defect.


                                                  12
```

---

## Page 13

```text
The contrast with the unrestricted result is operational,      not merely a rank calculation.
Bavaresco–Murao–Quintino prove the ambient k+3
                                                        
                                                     3    /M cap for general qubit testers [3]; theo-
rem 4.2 replaces its numerator by the exact coordinate-ring      rank of the transitive fixed-angle
promise. For the full sphere the reduction is k+1
                                                    
                                                  3    dimensions, while the circle promise reduces
the numerator further to 2k + 1.
    The higher-dimensional selective-phase family shows that the mechanism is not peculiar to a
                                                                             2
quadric surface. Its Segre closure changes the support growth from Θ(k d −1 ) to Θ(k 2d−2 ). For
fixed d, the corresponding necessary query scale for M generic labels drops from the ambient
degree count to k ≳ ((d − 1)!2 M )1/(2d−2) ; this remains a converse, not a universal attaining
construction.
    Fixed-angle rotation learning [5] studies a different task: a direction is encoded in a spin
system and later used to implement a target rotation. The present task is minimum-error
identification from repeated black-box gate calls. The common conjugacy-class geometry explains
the shared use of SU (2) covariance, but neither result implies the other.


12      Reproducibility and scope
The accompanying exact-arithmetic verifier checks, for a configurable range of k, the Hilbert-rank
identities, every rational Funk–Hecke eigenvalue at rational a, trace and purity, endpoint ranks,
great-circle Fourier coefficients, and the tightness obstruction. It is a finite symbolic audit, not a
computer proof of the general theorems.
    The scope is deliberately precise:

      the Hilbert-function support identity is a causal forward-query theorem for arbitrary
       projective families; the stronger general-tester cap is proved only for compact transitive
       unitary orbits by constant leverage;

      the general-tester class is the mathematical optimization class of [3]; no claim is made that
       every general process matrix is physically realizable;

      support rank is not automatically an achievable success probability; theorem 7.1 is a
       criterion for a fixed effective state family, not a universal circuit synthesis theorem;

      the continuous spectrum concerns the Bell/Choi parallel frame; it does not optimize all
       inputs or all adaptive circuits;

      spherical harmonics, Funk–Hecke theory, Hilbert functions, and spherical designs are
       classical ingredients, as is the rank-one leverage inequality;

      controlled-U , calls to U † , postselection, and different oracle models require new feature
       spaces and are not covered;

      no noise robustness, experimental resource count, or asymptotic statistical estimation
       theorem is inferred from exact algebraic rank.

AI assistance. OpenAI Codex assisted with symbolic exploration, literature triage, drafting,
and reproducibility checks. The author is responsible for the definitions, proofs, claims, citations,
and final manuscript.


13      Conclusion
Quantum query support is controlled by the algebraic geometry of the oracle family, not only
by the size of its ambient matrix space. The degree-k Hilbert function gives the exact exposed


                                                 13
```

---

## Page 14

```text
dimension and therefore a direct causal discrimination bound. On a compact transitive orbit,
constant leverage upgrades the same rank to an ultimate general-tester cap. Fixed-angle qubit
rotations provide a complete case study: quadratic generic support, a separate traceless branch,
exact harmonic and Fourier spectra, linear participation rank, and a sharp failure of multi-query
Bell tightness. Rank-one phase oracles show in arbitrary dimension that the same framework can
reduce the ambient support exponent from d2 − 1 to 2d − 2. The resulting separation between
ambient rank, promise-variety rank, spectral participation, and operational attainability supplies
a portable framework for other constrained unitary orbits.


References
 [1] Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca, and Ronald de Wolf. Quantum lower
     bounds by polynomials. Journal of the ACM, 48(4):778–797, 2001. https://doi.org/10.1145/
     502090.502097.
 [2] Adrian She and Henry Yuen. Unitary property testing lower bounds by polynomials. In 14th Innova-
     tions in Theoretical Computer Science Conference (ITCS 2023), volume 251 of Leibniz International
     Proceedings in Informatics, pages 96:1–96:17, 2023. https://doi.org/10.4230/LIPIcs.ITCS.2023.
     96.
 [3] Jessica Bavaresco, Mio Murao, and Marco Túlio Quintino. Unitary channel discrimination be-
     yond group structures: Advantages of sequential and indefinite-causal-order strategies. Journal of
     Mathematical Physics, 63(4):042203, 2022. https://doi.org/10.1063/5.0075919.
 [4] David Eisenbud. Commutative Algebra: with a View Toward Algebraic Geometry, volume 150 of
     Graduate Texts in Mathematics. Springer, 1995. https://doi.org/10.1007/978-1-4612-5350-1.
 [5] Yin Mo and Giulio Chiribella. Quantum-enhanced learning of rotations about an unknown direction.
     New Journal of Physics, 21:113003, 2019. https://doi.org/10.1088/1367-2630/ab4d9a.
 [6] R. T. Seeley. Spherical harmonics. The American Mathematical Monthly, 73(4, Part 2):115–121,
     1966. https://doi.org/10.1080/00029890.1966.11970927.
 [7] Philippe Delsarte, Jean-Marie Goethals, and Johan J. Seidel. Spherical codes and designs. Geometriae
     Dedicata, 6:363–388, 1977. https://doi.org/10.1007/BF03187604.
 [8] Anthony Chefles, Akira Kitagawa, Masahiro Takeoka, Masahide Sasaki, and Jason Twamley. Unam-
     biguous discrimination among oracle operators. Journal of Physics A: Mathematical and Theoretical,
     40(33):10183–10213, 2007. https://doi.org/10.1088/1751-8113/40/33/016.
 [9] Giulio Chiribella, Giacomo Mauro D’Ariano, and Martin Roetteler. Identification of a reversible
     quantum gate: Assessing the resources. New Journal of Physics, 15:103019, 2013. https://doi.
     org/10.1088/1367-2630/15/10/103019.
[10] Giulio Chiribella, Giacomo Mauro D’Ariano, Paolo Perinotti, and Massimiliano F. Sacchi. Maximum
     likelihood estimation for a group of physical transformations. International Journal of Quantum
     Information, 4(3):453–472, 2006. https://doi.org/10.1142/S0219749906002018.
[11] Lluis Eriksson. Two-query chirality in tetrahedral quantum echoes: Exact parallel readout, a nine-
     dimensional query defect, and a certified adaptive advantage, 2026. ARR-2026-5KS70GV7KK9DYA69,
     https://arr-research.github.io/papers/ARR-2026-5KS70GV7KK9DYA69/.




                                                   14
```
