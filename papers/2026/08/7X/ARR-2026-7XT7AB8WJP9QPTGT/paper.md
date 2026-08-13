# Certified Localized Weil Positivity Through Support 0.72: Multiband Schur Complements and a Complete Stieltjes Hierarchy

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
Certified Localized Weil Positivity Through Support 0.72:
 Multiband Schur Complements and a Complete Stieltjes
                        Hierarchy
                                                   Lluis Eriksson
                                               Independent Researcher
                                             lluiseriksson@gmail.com
                                                       August 2026


                                                          Abstract
         Suzuki’s localized Weil form is represented by a lower-bounded self-adjoint operator Aa on L2 (−a, a);
      nonnegativity for every a > 0 is equivalent to the Riemann hypothesis, while positivity at one fixed support is
      an unconditional and strictly weaker problem. We give a source-level interval certificate for the fixed-support
      inequality
                                                A0.72 ⪰ 5.890 × 10−17 I > 0.
      Nested-core monotonicity then gives the same scalar lower bound for every 0 < a ≤ 0.72. The proof is not
      a positive Ritz computation. It decomposes the exact prime-power translation graph through n = 4 into
      thirteen intervals, retains endpoint and singular directions as interval Gram matrices, and bounds the infinite
      complement by a mode-sensitive Schur estimate. The decisive split isolates degrees 12, . . . , 23, followed by
      [24, 176) and [176, ∞); both parity Schur matrices have 78 certified positive directions and no unresolved
      direction at 512-bit Arb precision. An independent shadow implementation, importing neither the project nor
      python-flint, reconstructs the prime-power graph and parity maps and reassembles the exported Schur balls
      with high-precision arithmetic; it is a wiring audit rather than a substitute for the Arb proof.
           Two analytic results explain why this certificate scales beyond a single matrix. First, the boundary potential
      − 12 log(1 − x2 ) has an exact Gauss–Stieltjes hierarchy whose finite approximants increase by explicit Schur
      squares and whose Markov remainder is a continuous square. At every fixed support this is a complete
      terminating strict-positivity hierarchy. Second, harmonic complement denominators admit a (1 + ε) Loewner
      Schur majorant with only Oε (log log M ) bands through degree M . The ingredients of Gaussian quadrature
      and operator antitonicity are classical; the contribution is their source-faithful integration with the arithmetic
      translations into a rigorous coercivity certificate. This is a bounded-support theorem, not a proof of the Riemann
      hypothesis.

Keywords. Weil quadratic form; Riemann zeta function; localized operator; interval arithmetic; Schur complement;
Gauss quadrature; Stieltjes function; Legendre expansion.


1     Statement, context, and claim boundary
Let QW denote the global Weil quadratic form in Suzuki’s additive logarithmic convention, and let QaW be its
closed restriction to functions supported in (−a, a). Suzuki constructs the representing self-adjoint operator Aa on
L2 (−a, a) and identifies
                                                                         QW (v)
                                    λa := min spec(Aa ) =       inf           2 .                                 (1)
                                                          0̸=v∈Cc∞ (−a,a) ∥v∥2

The form is continuous in a, positive for sufficiently small support, and the global Weil criterion asks for nonnegativity
at every support [5, 1, 2]. A finite-support lower bound is therefore meaningful but cannot by itself decide the
Riemann hypothesis.
    Our main result is the following computer-assisted theorem. All finite quantities in its proof are outward-rounded
real balls; floating eigenvectors are used only to propose a congruence and never to decide a sign.
Theorem 1.1 (localized coercivity). In Suzuki’s normalization of the global localized Weil form,

                                                A0.72 ⪰ 5.890 × 10−17 I > 0.                                                (2)

Consequently, for every 0 < a ≤ 0.72,
                                                    λa ≥ 5.890 × 10−17 .                                                    (3)



                                                              1
```

---

## Page 2

```text
The endpoint 0.72 is not claimed optimal. Among the primary sources we located, the previous explicit rigorous
localized radius is Yoshida’s a = (log 2)/2 result, reproduced and discussed by Bombieri [1, 2]. Connes–Consani
report larger numerical tests, and Kim et al. give a finite-element realization of Suzuki’s operator, but positive Ritz
values are upper bounds and do not certify coercivity [3, 6]. The present endpoint crosses the active prime-power
channels n = 2, 3, 4, since 4 < e1.44 < 5.
Remark 1.2 (not the semilocal scaling Hamiltonian). The operator in theorem 1.1 is only the self-adjoint
representative of Suzuki’s closed global localized form. We do not identify it with a semilocal Connes–Consani
operator: that formulation has a different sign convention, two moment constraints, multiplicative convolution, and
a globally normalized principal value. No operator ordering between different a is asserted, because the operators act
on different Hilbert spaces.


2    Source normalization and nested-core monotonicity
We record the normalization because a wrong polar Gram changes the odd sector. Put
                                    Z
                            vb(z) =   v(x)eizx dx,   ve(x) = v(−x),   f = v ∗ ve.
                                       R

Then f (0) = ∥v∥22 . In the direct explicit-formula representation the polar contribution is
                                                                        Z
                              V+ V− + V− V+ = 2 Re(V+ V− ),       V± = v(x)e±x/2 dx,                                (4)

not |V+ |2 + |V− |2 . The scalar term is −(log(4π) + γ)∥v∥22 , while the arithmetic part is
                                               X Λ(n)                    
                                           −     √ f (log n) + f (− log n) .                                        (5)
                                                   n
                                               n≥2


For support [−a, a] the unsampled archimedean tail contributes the exact −2 atanh(e−2a )f (0) inside the archimedean
integral. These conventions agree with Suzuki’s global form and are independently exercised by the source code.
Proposition 2.1 (nested-core monotonicity). If 0 < a′ ≤ a, then λa′ ≥ λa . In particular, Aa ⪰ cI implies λa′ ≥ c
for all a′ ≤ a.

Proof. Extension by zero embeds Cc∞ (−a′ , a′ ) into Cc∞ (−a, a) and preserves both the L2 norm and the value of
the same global functional QW . The admissible Rayleigh quotients for the smaller interval are therefore a subset of
those for the larger interval. Apply (1). This compares scalar infima, not operators on different spaces.
   Thus the numerical-analytic burden is entirely at the largest endpoint. Continuity additionally implies that, if
the Riemann hypothesis is false, the negative set of λa is an upper open interval. A zero plateau is not excluded, so
no simple or transverse crossing is claimed.


3    The scale-free dominant operator
After scaling (−a, a) to (−1, 1), the dominant archimedean form is
                                                     Z 1
                                               1         w(x) − w(y)                       1
                 L = A2 + V,       (A2 w)(x) =                       dy,          V (x) = − log(1 − x2 ).           (6)
                                               2      −1   |x − y|                         2

The regional logarithmic Laplacian is exactly diagonal in the Legendre basis:
                                                                  n
                                                                  X 1
                                     A2 Pn = Hn Pn ,       Hn =             ,   H0 = 0,                             (7)
                                                                        k
                                                                  k=1

as established in the recent analysis of the interval logarithmic Laplacian [7]. The remaining bounded block contains
the scalar, smooth, and finitely many translation terms. For a = 0.72 its active arithmetic displacements are log 2/a,
log 3/a, and log 4/a; the last weight is −Λ(4)/2 = − log 2/2, not − log 4/2.
    Cutting the interval at all translation endpoints gives thirteen subintervals. Their pointwise translation graph
has components of sizes seven, four, and two. Local normalized Legendre coordinates turn every exact translation
between equal-length intervals into an identity block. The finite source keeps twelve local degrees on each interval.
Reflection reduces the resulting 156-dimensional source into two 78 × 78 parity blocks.



                                                            2
```

---

## Page 3

```text
Proposition 3.1 (exact third-window partition). Suppose

                                                1    9                     log 2                 log 3
                                 log 2 < a <      log ,            h2 =          ,       h3 =          .
                                                2    2                       a                     a
In the scaled interval [−1, 1], the ordered cut points are

                                −1, 1 − 2h2 , −1 + 2h2 − h3 , 1 − h3 , −1 − h2 + h3 ,
                                    1 − 3h2 + h3 , −1 + h2 , 1 − h2 , −1 + 3h2 − h3 ,
                                    1 + h2 − h3 , −1 + h3 , 1 − 2h2 + h3 , −1 + 2h2 , 1.

Numbering the resulting intervals 0, . . . , 12, translations by h2 , h3 , and 2h2 pair respectively

                                     (0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11), (6, 12),
                                     (0, 10), (1, 11), (2, 12),           (0, 12).

Hence the translation graph components are

                                    {0, 2, 4, 6, 8, 10, 12},           {1, 5, 7, 11},       {3, 9}.

All intervals in one component have the same length.
Proof. The endpoints are the orbit of {−1, 1} required to make the three translations map whole cells to whole
cells. Their consecutive differences repeat the three values

                                    2(1 − h2 ),        4h2 − h3 − 2,                 2h3 − h2 − 2.

The first is positive because a > log 2; the third is positive exactly when 2a < log(9/2); and the middle is then
positive as well because log(9/2) < log(16/3). This proves the ordering. Direct subtraction of paired endpoints
gives the three edge lists. Graph connectivity gives the components; their interval lengths are respectively the first,
second, and third displayed values. For a = 0.72, the window inequalities hold.
    Thus the arithmetic√term in the local orthonormal Legendre basis is an exact weighted graph matrix: every
listed n-edge is −Λ(n)/ n times an identity block. In particular, the sole n = 4 edge has coefficient − log 2/2. This
algebraic partition, rather than a sampled quadrature grid, is what the interval source generator encloses.

                                                             n=2            n=3            n=4

        7-cell component   0             2               4                   6               8             10   12


        4-cell component   1                             5                                   7                  11


        2-cell component   3                                                                                    9



Figure 1: Exact translation graph of the thirteen interval cells. Each row is one pointwise connected component;
edge colors record the prime-power channel. The layout is schematic, while the vertex labels and edge set are the
exact data used by the source generator.


4     An exact Gauss–Stieltjes hierarchy
The positive boundary potential can be retained rather than paid as a norm. Set y = x2 . The elementary Stieltjes
identity
                                                     1 1 y
                                                       Z
                                             V (x) =             dt                                           (8)
                                                     2 0 1 − ty
leads to a hierarchy that we now make explicit. Let (tj , wj )m
                                                              j=1 be the m-node Gauss–Legendre rule on [0, 1] and
define
                                                        m
                                                    1X            x2
                                         Rm (x) =          wj          .                                       (9)
                                                    2 j=1 1 − tj x2



                                                                   3
```

---

## Page 4

```text
Theorem 4.1 (exact Stieltjes hierarchy). For 0 < |x| < 1,

                                         0 < R1 (x) < R2 (x) < · · · < V (x),                                       (10)
                                                                 Rm (1) = Hm ,                                      (11)

where the endpoint value means the finite rational limit. If pm (t) = Pm (2t − 1) and qm (y) = y m pm (1/y), then
                                                       Z 1                        2
                                                   1              x2m+1 pm (t)
                                  V (x) − Rm (x) =                      √               dt.                         (12)
                                                   2    0       qm (x2 ) 1 − tx2

Let Jm be the shifted-Legendre Jacobi matrix, with diagonal 1/2 and links

                                                        k
                                             ak = p                 .
                                                 2 (2k − 1)(2k + 1)

Then
                                                     x2 T
                                          Rm (x) =     e (I − x2 Jm )−1 e0 ,                                        (13)
                                                     2 0
and, writing Am = I − x2 Jm and

                                                 x2
                                      sm = 1 −      − x4 a2m eTm−1 A−1
                                                                    m em−1 > 0,
                                                 2
one has the positive increment
                                                            x6 a2m T         2
                                    Rm+1 (x) − Rm (x) =            em−1 A−1
                                                                         m e0 .                                     (14)
                                                             2sm
             / [0, 1], Gaussian exactness applied to (pm (z)2 − pm (t)2 )/(z − t) gives the classical Markov identity
Proof. For z ∈
                                                                
                                          Z 1                         Z 1
                                               dt     X wj                 pm (t)2
                                 pm (z)2          −             =                dt.
                                           0 z−t       j
                                                          z − tj        0   z−t

Put z = x−2 and rearrange to obtain (12). The endpoint identity follows by applying Gaussian exactness to
                                                       R1
(1 − pm (t))/(1 − t) and the standard Legendre integral −1 (1 − Pm (s))/(1 − s) ds = 2Hm . The spectral theorem for
Gaussian quadrature gives (13). Since Jm is the leading principal block of Jm+1 and its spectrum is inside (0, 1),
block inversion gives (14). Positivity of the Schur complement proves strict nesting.
   The Gauss–Legendre/Padé theory itself is classical [8, 9]. The point here is that its positive remainder and
positive increments match exactly the boundary potential of the localized Weil operator.
Corollary 4.2 (fixed-support completeness). Let La,m = A2 + Rm + Ba and La = A2 + V + Ba , where Ba is the
bounded scalar, smooth, and arithmetic block at fixed support. Then, for every fixed eigenvalue index k,

                                                 λk (La,m ) ↗ λk (La ).

In particular, La ≻ 0 if and only if La,m ≻ 0 for some finite m.
Proof. The forms increase pointwise by theorem 4.1. The harmonic diagonal Hn → ∞ and a bounded perturbation
give compact resolvent. Monotone convergence of closed forms and the min–max principle give eigenvalue convergence
[11, 12]. Strict positivity of La leaves a positive first-eigenvalue margin reached at finite m; the converse is the
pointwise operator order.

   This hierarchy does not settle a semidefinite zero-ground case and offers no support-uniform bound as a → ∞;
those qualifications prevent any RH conclusion.


5      Mode-sensitive Schur complements
We isolate the operator inequality that turns rigorous component Grams into a full infinite-dimensional certificate.

Theorem 5.1 (degree-resolved Schur majorant). Let H = H0 ⊕ H1 and
                                                     
                                                A B
                                         T =            = T ∗.
                                                B∗ D



                                                            4
```

---

## Page 5

```text
Nested Gauss--Stieltjes lower hierarchy                                                             Mode-sensitive Schur denominators at a = 0.72
            1.75          ()
                         Vx              ()
                                       R4 x
                                                                                                                6 × 100
                         R1(x)         R8(x)

            1.50         R2(x)
                                                                                                                4 × 100




                                                                                      complement denominator
                                                                                                                3 × 100
            1.25
                                                                                                                2 × 100
            1.00
potential




                                                                                                                                                                    dn= Hn − H12 + d12
                                                                                                                                                                    certified band floors
            0.75                                                                                                      100




                                                                                                                                                                                    8192: explicit end
            0.50                                                                                               6 × 10−1
            0.25                                                                                               4 × 10−1
                                                                                                               3 × 10−1




                                                                                                                                               176
                                                                                                                                   24
            0.00                                                                                               2 × 10−1
                   0.0           0.2           0.4         0.6       0.8        1.0                                         101             102               103                                   104
                                                     |x|                                                                                       Legendre degree

Figure 2: Left: exact nested lower approximants to the logarithmic boundary potential. Right: harmonic
denominators and the three registered floors in the support-0.72 Schur certificate. The plots illustrate proved
formulas; no sampled curve decides a sign.


Suppose {Pn }n≥N are mutually orthogonal projections summing to the identity on H1 and
                                              X
                                         D⪰        d n Pn , dn > 0.                                                                                                                                 (15)
                                                                             n≥N

Then
                                                                                                      X (BPn )(BPn )∗
                                                                 BD−1 B ∗ ⪯ R∗ :=                                                       .                                                           (16)
                                                                                                                              dn
                                                                                                  n≥N

For consecutive bands Ij = [mj , mj+1 ), define
                                                                           X 1 X
                                                                   RP =           (BPn )(BPn )∗ .
                                                                           j
                                                                             d mj
                                                                                       n∈Ij


If dn is increasing and dn ≤ (1 + ε)dmj on Ij , then

                                                                           R∗ ⪯ RP ⪯ (1 + ε)R∗ .                                                                                                    (17)

If dn = Hn + c > 0, a greedy partition through degree M uses at most
                                                           
                                            log(dM −1 /dN )
                                      1+                      = Oε (log log M )                                                                                                                     (18)
                                              log(1 + ε)

bands.

Proof. Inverse antitonicity on positive operators applied to (15) gives D−1 ⪯
                                                                               P −1
                                                                                  dn Pn , hence (16). On a band,
d−1
 n  ≤  d−1
        mj ≤ (1+ε)d  −1
                     n  ; multiply by each positive Gram and sum. Greedy band starts make successive denominators
grow geometrically, and HM ∼ log M gives (18).
Lemma 5.2 (interval congruence judge). Let S = S ∗ on Rr , and let X be a real square matrix. If interval
arithmetic proves
                           X T X ⪯ uI,    X T SX ⪰ gI,     0 < g, u < ∞,
then X is invertible as soon as a positive lower bound for X T X is also certified, and
                                                                                                               g
                                                                                   S⪰                            I.                                                                                 (19)
                                                                                                               u
It is enough to establish both matrix inequalities by outward-rounded Gershgorin bounds.
Proof. For z = Xy, one has y T X T SXy ≥ g∥y∥2 and ∥z∥2 = y T X T Xy ≤ u∥y∥2 . The positive lower Gram bound
makes X onto, so (19) holds for every z.




                                                                                                 5
```

---

## Page 6

```text
Lemma 5.3 (full block coercivity). For the block operator in theorem 5.1, suppose

                            D ⪰ dI,        A − BD−1 B ∗ ⪰ sI,              ∥B∥ ≤ b,         d, s > 0.

Then                                                                       −1
                                                          (1 + b/d)2
                                                      
                                                                       1
                                               T ⪰                   +           I.                                (20)
                                                              s        d
                                                  √
If BB ∗ ⪯ G, the computable substitution b ≤          Tr G is valid.
Proof. Put w = v + D−1 B ∗ u. Block Gaussian elimination gives

                                           ⟨(u, v), T (u, v)⟩ ≥ s∥u∥2 + d∥w∥2 .

Moreover ∥(u, v)∥ ≤ (1 + b/d)∥u∥ + ∥w∥. Weighted Cauchy–Schwarz proves (20). The trace bound follows from
∥B∥2 = ∥BB ∗ ∥ ≤ Tr G.
    This theorem does not require D to preserve the individual degree spaces. That point is essential: (15) is a form
inequality, and inverse antitonicity supplies the comparison without an invariance assumption. The Schur–Feshbach
principle then says that positivity of A − RP suffices for positivity of T . The two lemmas state exactly how an
interval sign on that finite Schur matrix is transported back to a scalar lower bound for the full operator.


6      The support-0.72 certificate
6.1    Frozen architecture
We now list every load-bearing parameter. The finite source uses the exact thirteen-interval graph and twelve local
Legendre modes per interval. The complement starts at local degree 12, the explicitly enclosed tail ends at 8192,
the analytic smooth expansion has order 47, and all proof balls use 512-bit precision. The successful partition is

                                  [12, 13), . . . , [23, 24),       [24, 176),        [176, ∞).                    (21)

The first and last finite-band denominator bounds, together with the far-tail bound, are

              d12 ≥ 0.2209732158977950,         d24 ≥ 0.8937207154406235,              d176 ≥ 2.868300416471574.   (22)

The twelve degreewise bounds increase monotonically between d12 and d23 ≥ 0.8520540487739568.

                          proof item                                    frozen value
                          support and active prime powers               a = 0.72; n = 2, 3, 4
                          translation components                        7 + 4 + 2 = 13 intervals
                          local source degrees                          0, . . . , 11 on every interval
                          source/parity dimensions                      156 = 78 + 78
                          explicit complement range                     12 ≤ n < 8192
                          smooth/self remainder endpoints               47 and 32768
                          pointwise subdivisions                        1024
                          ball precision                                512 bits

6.2    Fail-closed finite reduction
The aggregate [12, 176) coupling Gram is generated independently from twelve nonzero degreewise Grams on
[12, 24). The residual [24, 176) Gram is formed as an Arb interval subtraction, not by subtracting floating midpoints.
Endpoint flux, adjacent singular, other-tail, and directional self-tail contributions enter as Grams before the final
Schur subtraction.
    For each parity π, the verifier performs the following fixed sequence.
                                                                [12,176)
1. It encloses the source matrix Aπ , the aggregate Gram Gπ              , the independently generated degree Grams
      [m,m+1)
   Gπ         for 12 ≤ m < 24, and the far-tail Gram.
               [24,176)    [12,176)  P23     [m,m+1)
2. It forms Gπ          = Gπ        − m=12 Gπ         as an Arb matrix subtraction, retaining every entry radius.
3. It subtracts the fourteen band corrections using the registered degreewise lower endpoints and the far-tail
   endpoint in (22), together with the endpoint, singular, smooth, and self-tail budgets, to obtain one interval
   Schur matrix Sπ .
4. A floating midpoint eigensystem proposes Xπ . The sign decision is then repeated entirely in Arb: positive lower
   Gram for XπT Xπ , strict Gershgorin positivity for XπT Sπ Xπ , and the transport in theorem 5.2.


                                                                6
```

---

## Page 7

```text
5. Any nonpositive denominator, noninvertible Gram, overlapping Gershgorin disc, metadata mismatch, or unre-
   solved coercive lower endpoint aborts rather than returning a sign.


                                  Table 1: Final interval adjudication at a = 0.72.
                             sector negative positive unresolved            Schur lower
                             even             0         78             0   1.550 × 10−14
                             odd              0         78             0   4.368 × 10−11


6.3    Return to the full Hilbert space
For each parity, a floating midpoint eigenbasis proposes a change of basis. The verifier then proves with Arb that its
Gram is positive, so the change is invertible, and that the congruent Schur interval is strictly Gershgorin positive.
Finally, an interval upper bound on the squared norm of the change of basis transports the lower bound to the
original coordinates. The block reconstruction, including the complement and coupling norm, gives respectively
5.890 × 10−17 and 1.652 × 10−13 in the even and odd sectors. The smaller number proves (2) by Lemma 5.3; this last
step charges the norm of the source–complement coupling and is not an inference from the finite Schur eigenvalue
alone.
Remark 6.1 (why a finite eigenvalue is insufficient). Rayleigh–Ritz gives upper bounds on the lowest eigenvalue.
The proof instead certifies a lower bound on the full complement, encloses the source-to-tail coupling, and proves
positivity of the resulting interval Schur matrices. Every omitted infinite direction is charged before the sign is
decided.


7     Reproducibility and falsification gates
The proof source starts from repository commit 3d997887ccf4e056607c4488a708181db1d507ef; the release in-
cludes the complete source snapshot and the audited accumulator patches that produced format version 3. Two
interval proof objects and the final JSON record have the registered names and SHA-256 digests
• theta-schur-a072-d12-p47-tail8192-v3.npz:
  fab69bc8fa1d21ac0d3faca85d317ec5655fd991e7af29329329be4e5f8c1ebb;
• theta-near-band-a072-d12-to24-by-degree-p512-v3.npz:
  9119dbd4bad1a3c0de406445bbcb537e7c6d10fc6010f7a9d90ea79ae561751c;
• theta-schur-a072-multiband-to24-by-degree-v3.json:
  63b0dd91dab9fe7a00b734644c7a0400c2240a51cc25e6dde42751208dfc4f08.
The first artifact is a deterministic outward upgrade of the allowlisted pre-refactor aggregate: its intrinsic radii are
rounded up, one centre ulp is added, and the exact smooth remainder is rounded up. An independent corrected
replay has identical component midpoints and strictly nonzero aggregate Grams. The second artifact is the directly
regenerated degreewise [12, 24) family; the third is the theorem record. Format version 3 records the corrected
list accumulation and centred-binary64 export, and rejects both earlier artifact schemas. Metadata checks include
support, degrees, partition, smooth order, and precision. The release wrapper additionally checks all expected keys,
78 × 78 shapes, numeric finiteness, nonnegative radii, the JSON theorem schema, and the three byte hashes before
accepting a replay. Format version 3 also widens every stored radius by one ulp of its binary64 centre, so the cache
encloses both the Arb ball and the centre-conversion displacement. A mismatch fails closed.
     The proof is falsifiable at several levels: a nonpositive complement denominator aborts; a nonpositive change-of-
basis Gram aborts; any overlapping Gershgorin ball is unresolved rather than rounded positive; any hash mismatch
rejects the frozen record; and parity reconstruction is checked independently against the unreduced source. The
release includes the allowlisted predecessor, the conservative upgrader, the fresh provenance replay, and their
comparison record; these are proof objects, not untracked assumptions.
     The frozen environment is Python 3.12.6, python-flint 0.9.0, NumPy 2.5.1, SciPy 1.18.0, and mpmath 1.3.0. The
heavy component generators were run on a Colab Pro+ CPU runtime at 512-bit Arb precision; the aggregate replay
took approximately 80 minutes on that runtime. The final verifier takes about two seconds and the independent
shadow audit about nine seconds on the stated desktop environment. The public source is the linked repository
commit. The exact archive accompanying this manuscript is Certified_Localized_Weil_Positivity_Through_
Support_0_72_Reproducibility.zip, with SHA-256
                                         b5ace98f5ac8951c3939ee85c4c34563
                                         668861b0c23ca3751e7e4d5b17eb2645.

Its README prints both replay commands; the terminal acceptance command is
                                       python repro/verify_release.py repro.



                                                             7
```

---

## Page 8

```text
8     Relation to previous work and limitations
Yoshida and Bombieri established the localized variational setting and a first explicit support result [1, 2]. Connes–
Consani and Connes–Consani–Moscovici developed operator and spectral-triple realizations of Weil positivity [3, 4].
Suzuki’s screw-function framework supplies the precise self-adjoint operator certified here [5]. Kim et al. numerically
instantiate that operator and show the severe resolution problem in its lowest branch [6].
    Classical inputs are not novelty claims: Gaussian quadrature, Padé/Markov remainders, Jacobi resolvents,
operator inverse antitonicity, Schur complements, and monotone convergence of forms are standard [8, 9, 10, 11, 12].
The contributions are:
1. a source-faithful coercivity certificate for the complete operator at support 0.72, rather than a positive compression;
2. a mode-sensitive arithmetic Schur construction that retains the exact prime-power graph through n = 4 and
   closes both parity sectors;
3. the specialization of the exact Stieltjes hierarchy to Suzuki’s boundary potential, including a terminating
   strict-positivity hierarchy at fixed support; and
4. a multiband theorem showing that harmonic inverse tails can be controlled with doubly logarithmic storage.
    The result has sharp logical limits. It does not prove positivity beyond 0.72, does not establish support-uniform
constants, does not prove RH, does not identify zeta zeros as eigenvalues of Aa , and does not turn numerical
agreement with known zeros into a premise. Further isolated endpoints would extend the unconditional interval but
would not by themselves solve the uniform-support problem. A global advance needs a source-side stratification
whose finite Schur sign remains controlled as new prime powers enter.


A      Source-to-Gram specification
This appendix makes the software boundary explicit. It is normative for the certificate: every term subtracted from
the finite source is listed with its mathematical sign and the routine that encloses it.

A.1     Finite source
Let Ir be the thirteen intervals of Proposition 3.1 and let erj be the normalized local Legendre mode of degree
j < 12 on Ir . Write ℓr = |Ir |. The scale-free diagonal-block entries used by the generator are
                       
                                      j
                                    X             1
                                                              − log 2 − log(ℓr /2), j = k,
                       
                       
                        H j +   1 +
                       
                       
                                    m=1
                                         m(2m − 1)(2m + 1)
                 (r)
               Djk =                                                                                       (23)
                         p
                            (2j + 1)(2k + 1)
                                             ,                                     j ̸= k, j + k even,
                        |j − k|(j + k + 1)
                       
                       
                       
                       
                       0,                                                          j + k odd.
Cross-interval entries are exact Legendre moments of the logarithmic kernel. The smooth archimedean remainder is
expanded through power 47. If up2 denotes the two successive outward binary64 roundings used at generation and
adjudication, its charged scalar is
                                    2 (2a/3)48      2a48 /48!
                                                               
                   rsm := up2 2a               +                    = 9.2437306756331 × 10−16 .            (24)
                                    3 1 − 2a/3 1 − a2 /(49 · 50)
This is an unsigned Schur-norm upper bound, not a fitted error estimate. Thus the unreduced source has the
auditable decomposition
                                                                          X Λ(n)
                    Asrc = D + Kcross + Ksmooth − log a + log(2π) + γ I −         √ An ,              (25)
                                                                          n=2,3,4
                                                                                   n

where An is the identity-block adjacency matrix of the printed n-edge list. No quadrature is used in (25).
   Reflection sends erj to (−1)j e12−r,j . Hence the parity isometries U± : R78 → R156 have paired columns
                                     2−1/2 erj ± (−1)j e12−r,j ,
                                                               
                                                                     0 ≤ r < 6,                                      (26)
                                                                                                    T
together with the even, respectively odd, modes of the central interval. The implementation checks U± U± = I,
  T                                                                      T
U+  U− = 0, and reconstructs the unreduced spectrum before exporting U±    Asrc U± .

A.2     Complement rows and positive Grams
For a target interval t and complement degree q ≥ 12, let vtq ∈ R156 collect the coefficients of the exact second-Green
map from all source modes into that target mode. Its self-block entry is
                                                            p
                                                              (2q + 1)(2j + 1)
                                       (vtq )tj = 1q+j even                    ,                                   (27)
                                                            (q − j)(q + j + 1)

                                                            8
```

---

## Page 9

```text
and the adjacent and separated entries are the corresponding exact Legendre–Green integrals, with the orientation
factor (−1)q+j when the source lies to the left. The finite band Gram is therefore, before parity reduction,
                                                             12 X
                                                             X
                                                      GJ =                  T
                                                                       vtq vtq ⪰ 0.                                              (28)
                                                             t=0 q∈J

All cross terms between different source intervals are retained inside each outer product. Formula (28) is evaluated
independently for each singleton band J = [q, q + 1), 12 ≤ q < 24.
    The endpoint-flux Gram retains rows p±  t at every interval endpoint and uses the exact weights
                                       M −1
                                       X         2q + 1
                                                           (p+ − (−1)q p−    +       q − T
                                                                        t )(pt − (−1) pt ) ,                                     (29)
                                              2q 2 (q + 1)2 t
                                       q=N

plus the positive M −2 remainder. We now define the coefficient appearing in the adjacent-singular row without
reference to software. On a source interval of length ℓr , write
                             r
                     (r)       2j + 1                                      (r)      (r)
                   fj (u) =           Pj (2u/ℓr − 1),                    fej (u) = fj (−u),                (30)
                                 ℓr
                             r
                     (t)       2k + 1
                    gk (u) =          Pk (1 − 2u/ℓt ),               0 ≤ u ≤ ℓt .                          (31)
                                 ℓt
Set                                                                                                 Z ℓt
                         1   h
                                             (r)                    (r)
                                                                             i
                                                                                           kj               (t)
          Rjt←r (u) := −         (ℓt − 2u)(fej )′ (u) + u(ℓt − u)(fej )′′ (u) ,           Ct←r :=          gk (u)Rjt←r (u) du.   (32)
                        2                                                                             0

           P in (32) are polynomials, so the generator expands them in monomials and evaluates the integral
All functions
exactly as p,q gkp Rjq ℓp+q+1
                        t     /(p + q + 1) in Arb. The adjacent-singular row is then
                                                                         t←r
                                                   p
                                              X      (2q + 1)(2k + 1) Ckj
                                    stq,j = −                                  ,                       (33)
                                                  q(q + 1) − k(k + 1) q(q + 1)
                                                      k<12

summed over both neighbours r = t ± 1 before squaring. Finally, the retained self-regularized row is
                                                 p
                                                    (2q + 1)(2j + 1)j(j + 1)
                                rqj = 1q−j even                               .                                                  (34)
                                                [q(q + 1) − j(j + 1)]q(q + 1)
Analytic remainders of (33) and (34) enter as positive diagonal Grams; the remaining non-directional map is
bounded by the smaller of its Arb spectral estimate and the Schur row–column norm.


Table 2: Normative source-to-Gram map. Every listed object is checked for shape, finiteness, nonnegative radii,
and its registered metadata.
 object                      mathematical content                       generator / exported field
 finite source               (25), then (26)                            arb_third_window_source.build_arb_third_window_
                                                                        source; source_even/odd_*
 degree band                 complete rows (28), including              arb_third_window_near_tail_gram.build_arb_third_
                             smooth map                                 window_near_tail_gram; band_i_even/odd_*
 endpoint flux               (29) and positive remainder                arb_third_window_flux_gram.build_arb_third_
                                                                        window_flux_gram; flux_even/odd_*
 adjacent singular           both neighbours combined before            arb_third_window_singular_gram.build_arb_third_
                             the Gram                                   window_singular_gram; singular_even/odd_*
 directional self            (34) and diagonal remainder                arb_third_window_self_gram.build_arb_third_
                                                                        window_self_gram; self_even/odd_*
 other tail                  adjacent/separated analytic                arb_third_window_other_tail.certify_third_
                             comparison matrix                          window_other_tail; other_tail_norm
 final sign                  multiband Schur, Arb                       third_window_multiband_schur_certificate.
                             congruence–Gershgorin,                     certify_third_window_multiband_schur
                             Lemma 5.3


A.3       One-line reconstruction of the certificate
With η = 0.2, ρ = 10−4 , and ϵoth the certified other-tail norm, define
                                 Gstr = 2(Gflux + Gsing ),                                                                       (35)
                                                                          −1                   −1
                                                                                                    )ϵ2oth I.
                                                                                      
                             Gtail = (1 + ρ) (1 + η)Gstr + (1 + η              )Gself + (1 + ρ                                   (36)


                                                                  9
```

---

## Page 10

```text
For each parity the exact matrix submitted to the interval sign test is
                                                         23  [m,m+1)            [24,176)
                                                         X  Gπ                 Gπ              Gtail,π
                               Sπ = Asrc,π − rsm I −                       −               −           .                        (37)
                                                        m=12
                                                                  dm             d24            d176
                                                                                P23
The residual band is formed as an interval subtraction G[24,176) = G[12,176) − m=12 G[m,m+1) . Thus (37) fixes
every sign, denominator, and remainder used in Table 1.
   For completeness, Table 3 prints the three outward endpoints inserted in Lemma 5.3: s is the certified Schur lower
bound, d the complement lower bound, and b the coupling-norm upper bound. Substitution into (20) reproduces
the last column directly.


                                          Table 3: Full-block transport constants.
      sector                      s (lower)               d (lower)                b (upper)                 full lower bound
      even      1.5503334138073538 10   −14
                                               0.220973215897795         3.364050436902478           5.890068275105137 10−17
      odd        4.368297840510665 10−11       0.220973215897795        3.3712214851682476          1.6529959078469627 10−13



B     Independent reconstruction audit
The release contains independent_reference_audit.py. It imports neither project modules nor python-flint.
From the printed cut points it reconstructs all eleven prime-power edges, verifies the 78 + 78 parity isometries,
loads only the raw component balls, and independently evaluates (36)–(37) with 100-decimal mpmath arithmetic.
Weyl’s inequality is then applied using the maximum radius row sum. The shadow margins are

                 λmin (M+ ) − ∥R+ ∥∞ > 6.3113 × 10−14 ,               λmin (M− ) − ∥R− ∥∞ > 4.3738 × 10−11 .

This implementation is intentionally not invoked by the Arb proof and does not replace its directed-rounding
guarantee. Its role is orthogonal: it makes a wrong edge list, parity convention, residual-band sign, balance factor, or
denominator fail through a separately written assembly path. The corrected source replay additionally regenerates
the component Grams from the explicit formula, rather than merely rereading the registered NPZ objects.


AI assistance disclosure
AI tools assisted with literature discovery, adversarial proof checking, software inspection, and manuscript prepa-
ration. The author selected the claims, reviewed the mathematical arguments and executable evidence, and is
responsible for the final text and any remaining errors.


References
 [1] H. Yoshida, On Hermitian forms attached to zeta functions, in Zeta Functions in Geometry, Adv. Stud. Pure Math. 21 (1992),
     281–325.
 [2] E. Bombieri, Remarks on Weil’s quadratic functional in the theory of prime numbers, I, Rend. Lincei Mat. Appl. 11 (2000),
     183–233.
 [3] A. Connes and C. Consani, Spectral triples and ζ-cycles, Enseign. Math. 69 (2023), 93–148.
 [4] A. Connes, C. Consani and H. Moscovici, Zeta spectral triples, arXiv:2511.22755 (2025).
 [5] M. Suzuki, Weil’s quadratic form via the screw function, arXiv:2606.09096 (2026).
 [6] T. Kim, Y. Hong, M. Kim, S. Choi, J. Jang, J. Shin and M. Kim, A numerical realization of Suzuki’s Weil-quadratic-form
     operator: the Archimedean spectral law, its universality, and an operator form of Weil’s positivity criterion, arXiv:2607.24830
     (2026).
 [7] M. R. Rosenzweig and S. J. Stanfill, On the fundamental solutions of two nonlocal parabolic equations related to logarithmic
     Laplacians, arXiv:2606.04225 (2026).
 [8] G. H. Golub and J. H. Welsch, Calculation of Gauss quadrature rules, Math. Comp. 23 (1969), 221–230.
 [9] H. Fawzi, J. Saunderson and P. A. Parrilo, Semidefinite approximations of the matrix logarithm, Found. Comput. Math. 19 (2019),
     259–296.
[10] E. V. Haynsworth, Determination of the inertia of a partitioned Hermitian matrix, Linear Algebra Appl. 1 (1968), 73–81.
[11] B. Simon, A canonical decomposition for quadratic forms with applications to monotone convergence theorems, J. Funct. Anal. 28
     (1978), 377–385.
[12] T. Kato, Perturbation Theory for Linear Operators, Springer, 1995.




                                                                10
```
