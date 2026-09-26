# Structural Calculus: From Discrete Structural Derivatives to the Structural Spectrum of Integers

Abel Liu — September 9, 2026

This is a machine-readable text extraction of the deposited PDF. Mathematical symbols and line breaks may be flattened; the unchanged `paper.pdf` is canonical.

   Structural Calculus: From Discrete Structural
  Derivatives to the Structural Spectrum of Integers
                                               Abel Liu

                                         September 9, 2026


                                               Abstract
         This paper establishes a discrete calculus framework acting on the internal structure of
     formal mathematical expressions. The fundamental premise is that mathematical expres-
     sions possess not only numerical semantics but also an internal syntax determined by their
     construction. Consequently, two expressions that are numerically equivalent are not neces-
     sarily identical as differential objects. To capture this distinction, we construct a free term
     algebra and define a structural derivative D upon it. Unlike classical calculus, D does not
     rely on limits; rather, it is recursively determined by local structural rules on expression
     trees.
         We establish four fundamental axioms of structural calculus. The cornerstone of this
     framework is the power node rule,

                                     D(U V ) = U V −1 + (U − 1)V ,

     which highlights exponentiation as the true bedrock of the theory by decomposing a power
     structure into two parallel discrete evolution directions. Under a strict structural normal-
     ization principle, trivial multiplications by the identity element are forbidden, while atomic
     integers are fundamentally embedded as degenerate power structures (e.g., 8 = 81 ). This
     leads to a striking departure from classical calculus: the structural derivative of an integer
     is not zero, but possesses its own non-trivial value (e.g., D(8) = 8).
         By introducing two commuting discrete shift operators, we express the structural deriva-
     tive as their sum and derive a binomial expansion for its higher-order iterations. As an
     application, we obtain an explicit formula for the n-th order structural derivative of xx ,
     yielding a novel combinatorial integer sequence. Furthermore, we extend the scope from
     individual expressions to the complete structural decompositions of integers. We define the
     structural spectrum Σ(n) and the total structural response R(n) for an integer n. This re-
     veals a profound structural dichotomy between primes and composites. Finally, we propose
     two natural arithmetic conjectures concerning the integrality and critical self-consistency of
     R(n), opening a new pathway from local structural rules to the global arithmetic properties
     of integers.

Keywords: Structural Calculus; Formal Expressions; Free Term Algebra; Discrete Derivative;
Expression Trees; Power Node; Leibniz Rule; Structural Spectrum; Integer Decompositions.


Contents
1 Introduction                                                                                         3

2 The Algebra of Formal Expressions and Fundamental Rules                                              3
  2.1 Expression Trees and Structural Equivalence . . . . . . . . . . . . . . . . . . . .              3
  2.2 The Four Fundamental Axioms . . . . . . . . . . . . . . . . . . . . . . . . . . . .              3

3 The Structural Derivative and the Primacy of Exponentiation                                          4
  3.1 Why the Derivative of an Integer is Not Zero . . . . . . . . . . . . . . . . . . . .             4

                                                   1


4 Higher-Order Structural Derivatives and Combinatorial Paths                                    4
  4.1 Discrete Shift Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   4
  4.2 The n-th Order Structural Derivative . . . . . . . . . . . . . . . . . . . . . . . . .     4
  4.3 Explicit Examples and Combinatorial Interpretation . . . . . . . . . . . . . . . .         5

5 Structural States and the Structural Spectrum of Integers                                      5
  5.1 Structural States and Response Rates . . . . . . . . . . . . . . . . . . . . . . . .       5
  5.2 The Structural Spectrum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      5

6 Total Structural Response and Arithmetic Conjectures                                           6
  6.1 Total Structural Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    6
  6.2 Two Fundamental Conjectures . . . . . . . . . . . . . . . . . . . . . . . . . . . .        6

7 Conclusion                                                                                     6




                                                2


1     Introduction
In traditional mathematics, an expression is primarily identified by its numerical value. For
instance, 6, 2 × 3, and 1 + 5 all denote the same numerical entity. Furthermore, in classical
calculus, the derivative of a constant is identically zero. However, this perspective entirely
discards the syntactic and structural information inherent in how a mathematical object is
constructed.
    This paper introduces Structural Calculus, a novel discrete mathematical framework that
treats the internal construction of expressions as the primary object of study. In this framework,
expressions are modeled as finite rooted trees, and differentiation is redefined as a local structural
evolution on these trees. We demonstrate that exponentiation serves as the fundamental bedrock
of this calculus, leading to the counterintuitive but mathematically consistent result that the
structural derivative of an integer is not zero. By analyzing the complete set of structural
decompositions of an integer, we define its structural spectrum and propose new arithmetic
conjectures that bridge discrete operator calculus and number theory.


2     The Algebra of Formal Expressions and Fundamental Rules
2.1     Expression Trees and Structural Equivalence
Let A be an alphabet of symbols containing variables, constants, and formal parameters. We
define the set of terms T recursively:
    (i) Every basic symbol in A is a term in T .
 (ii) If F, G ∈ T , then (F + G), (F − G), (F G), and (F G ) are in T .
   Every term can be uniquely represented as a finite rooted tree, where leaves correspond to
basic symbols and internal nodes correspond to the operators +, −, ×, and ∧ .
Definition 2.1 (Structural Equivalence). Two terms F, G ∈ T are structurally equivalent,
denoted F ∼
          =str G, if and only if they are isomorphic as labeled rooted trees.
    It is evident that numerical equality does not imply structural equivalence. If we define
the standard numerical evaluation map ev : T −→ R, we have ev(6) = ev(2 × 3) = 6, but
6≁ str 2 × 3. This separation of numerical semantics and structural syntax is the cornerstone of
  =
our theory.

2.2     The Four Fundamental Axioms
The structural derivative D is a linear operator on the free term algebra E = K(T ) . Its action
is entirely governed by the following four fundamental axioms:
Axiom 2.2 (Linearity for Addition and Subtraction).
                                    D(F ± G) = D(F ) ± D(G).                                      (1)
Axiom 2.3 (Leibniz Rule for Multiplication).
                                 D(F · G) = D(F ) · G + F · D(G).                                 (2)
Axiom 2.4 (The Power Node Rule).

                                   D(U V ) = U V −1 + (U − 1)V .                                  (3)

This is the most critical and disruptive rule. It decomposes a power node into two parallel
structural evolution directions: the “exponent descent” (U V −1 ) and the “base descent” ((U −
1)V ).

                                                   3


Axiom 2.5 (Structural Normalization). The expression trees must be in their most reduced
form. The system strictly eliminates all redundant parenthesization and trivial multiplications
by the identity element (1).


3     The Structural Derivative and the Primacy of Exponentiation
3.1   Why the Derivative of an Integer is Not Zero
In classical calculus, the derivative of a constant is zero. In structural calculus, we assert that
the structural derivative of an integer is not zero; it inherently possesses its own
non-trivial value.
    This profound departure stems from the fact that exponentiation is the true bedrock
of this calculus. Under Axiom 4 (Structural Normalization), trivial multiplicative structures
involving the identity element, such as 8 × 1 or 8 × 1 × 1, are strictly excluded from the set of
valid structural states. An integer cannot be artificially inflated by multiplying it by 1.
    However, representing an integer as a degenerate power structure with an exponent of 1 is
fundamentally permitted and required as the base structural form. That is, any atomic integer
N is intrinsically embedded as:
                                              N = N1
    Applying Axiom 3 (The Power Node Rule) to 8 = 81 , we obtain:

                     D(8) = D(81 ) = 81−1 + (8 − 1)1 = 80 + 71 = 1 + 7 = 8.                    (4)

    Thus, D(8) = 8. We do not need to artificially postulate that “the derivative of a constant is
itself.” This result emerges naturally and inevitably as the degenerate case of the Power Node
Rule when the exponent is 1. This demonstrates the profound self-consistency of structural
calculus: a single core rule governs the entire universe of expressions.


4     Higher-Order Structural Derivatives and Combinatorial Paths
4.1   Discrete Shift Operators
Consider the formal subspace generated by power terms uv . We define two discrete shift opera-
tors:
                         Eu−1 (uv ) = (u − 1)v ,  Ev−1 (uv ) = uv−1 .                      (5)
The Power Node Rule can then be elegantly rewritten as:

                                        D = Ev−1 + Eu−1 .                                      (6)

Crucially, these two operators commute: Eu−1 Ev−1 = Ev−1 Eu−1 . This commutativity implies that
the order of structural evolution (whether we descend the base first or the exponent first) does
not affect the final structural state.

4.2   The n-th Order Structural Derivative
Because the operators commute, we can directly apply the binomial theorem to compute higher-
order derivatives.

Theorem 4.1. For any n ∈ N, the n-th order structural derivative is given by:

                                      n (︃ )︃
                                     ∑︂   n
                                  n
                                 D =         (Eu−1 )k (Ev−1 )n−k .                             (7)
                                          k
                                       k=0


                                                4


    Applying this to the self-referential expression xx , we obtain a completely explicit formula:
                                           n (︃ )︃
                                     n   x
                                          ∑︂   n
                                 D [x ] =         (x − k)x−n+k .                                    (8)
                                               k
                                             k=0


4.3   Explicit Examples and Combinatorial Interpretation
The binomial coefficients nk are not arbitrary; they represent the exact number of discrete
                           (︁ )︁

structural evolution paths. In(︁ n)︁ steps, choosing k times to descend the base and n − k times to
descend the exponent yields nk identical final structures.
    Let us examine two explicit examples:

Example 4.2 (First-Order Derivative, n = 1).
                        (︃ )︃              (︃ )︃
                   x      1          x−1     1
               D[x ] =       (x − 0)     +      (x − 1)x = xx−1 + (x − 1)x .                        (9)
                          0                  1

This perfectly mirrors the core Power Node Rule.

Example 4.3 (Second-Order Derivative, n = 2).
                        (︃ )︃               (︃ )︃              (︃ )︃
                 2 x      2           x−2     2          x−1     2
               D [x ] =       (x − 0)     +      (x − 1)     +      (x − 2)x
                          0                   1                  2                              (10)
                               x−2             x−1            x
                           =x        + 2(x − 1)      + (x − 2) .

              this at x = n generates a novel combinatorial integer sequence An = D [n ] =  n   n
∑︁nEvaluating
     (︁n)︁     k
  k=0 k (n − k) , with initial terms A1 = 1, A2 = 3, A3 = 10, A4 = 41, A5 = 196, . . .


5     Structural States and the Structural Spectrum of Integers
5.1   Structural States and Response Rates
We now extend our focus from individual expressions to the integer itself. For an integer n > 1,
let States(n) be the set of all valid, normalized structural representations of n (e.g., for n = 4,
the states are 4, 2 × 2, and 22 ). Note that 4 × 1 is excluded by Axiom 4.
    To measure the “structural activity” of a state F ∈ States(n), we define its structural response
rate:
                                          ev(D(F ))     ev(D(F ))
                                  ρ(F ) =            =            .                             (11)
                                            ev(F )          n
    For multiplicative structures F = G·H, the Leibniz rule implies a strict additivity of response
rates:
                                    ρ(G · H) = ρ(G) + ρ(H).                                    (12)
Conversely, power structures exhibit non-linear responses. For F = am (a, m ≥ 2):

                                 am−1 + (a − 1)m                1 m
                                                           (︃     )︃
                            m                         1
                        ρ(a ) =                     = + 1−           .                          (13)
                                        am            a         a

5.2   The Structural Spectrum
Definition 5.1 (Structural Spectrum). The structural spectrum of an integer n is defined as
the set of response rates of all its valid structural states:

                                 Σ(n) = {ρ(F ) : F ∈ States(n)} .                               (14)

                                                   5


    This definition reveals a profound structural dichotomy in number theory:
    • Primes (e.g., 2, 3, 5) possess no non-trivial multiplicative decompositions. Their structural
      spectrum is always the singleton Σ(p) = {1}, representing an absolute “ground state.”

    • Composites (e.g., 4, 8, 27) possess rich non-trivial decompositions. For example, Σ(4) =
      {1, 2, 34 } and Σ(8) = {1, 2, 3, 58 , 47 }. They exhibit multiple “excited states.”


6     Total Structural Response and Arithmetic Conjectures
6.1    Total Structural Response
We define the total structural response R(n) as the sum of the response rates over all valid
structural states of n:
                                             ∑︂
                                   R(n) =           ρ(F ).                              (15)
                                              F ∈States(n)

    Let us compute R(n) for small integers:
    • For n = 4: R(4) = 1 + 2 + 34 = 15
                                     4 = 3.75.

    • For n = 8: R(8) = 1 + 2 + 3 + 58 + 47 = 67
                                              8 = 8.375.

   Notice that R(4) < 4, while R(8) > 8. The function R(n) − n changes sign, which naturally
motivates the following arithmetic conjectures.

6.2    Two Fundamental Conjectures
Conjecture 6.1 (Integrality of the Structural Spectrum (Conjecture A)). Does there exist an
integer n > 1 such that its total structural response R(n) is an exact integer? That is,

                                       ∃n > 1,    R(n) ∈ Z.                                   (16)

Conjecture 6.2 (Structural Criticality (Conjecture B)). Does there exist a special integer n > 1
such that its total structural response exactly equals its numerical value? That is,

                                       ∃n > 1,    R(n) = n.                                   (17)

    If such an integer exists, we term it a Structural Critical Integer. Conjecture B implies
Conjecture A. The existence of a structural critical integer would mean that the numerical
scale of the integer perfectly balances the total “structural energy” generated by all its possible
internal decompositions. While finite computations show R(n) − n crossing zero between n = 4
and n = 8, the discrete nature of n prevents us from concluding the existence of a root without
further rigorous analysis.


7     Conclusion
This paper has established Structural Calculus, a discrete mathematical framework that differ-
entiates expressions based on their internal syntactic trees rather than their numerical values.
We formalized the theory through four fundamental axioms, establishing exponentiation as the
foundational bedrock. By enforcing structural normalization, we demonstrated that the struc-
tural derivative of an integer is inherently non-zero (e.g., D(8) = 8), emerging naturally from
the degenerate power rule.
    We derived explicit formulas for higher-order structural derivatives, revealing a beautiful
combinatorial path-counting structure. Furthermore, by extending the derivative to the space

                                                 6


of all valid structural decompositions of an integer, we introduced the structural spectrum and
the total structural response R(n). This led to the proposal of two novel arithmetic conjectures
regarding the integrality and critical self-consistency of R(n).
    The research pathway established herein transitions from local expression tree rules to global
arithmetic properties of integers:

Formal Expressions −→ Structural Derivative −→ Structural States −→ Structural Spectrum −→ R(n) −→ Ar

Future work will focus on rigorously enumerating States(n), analyzing the asymptotic growth
of R(n), and computationally searching for structural critical integers.


References
 [1] G.-C. Rota, Finite Operator Calculus, Academic Press, 1975.

 [2] S. Roman, The Umbral Calculus, Academic Press, 1984.

 [3] J. Riordan, Combinatorial Identities, John Wiley & Sons, 1968.

 [4] R. P. Stanley, Enumerative Combinatorics, Vol. 1, Cambridge University Press, 2012.

 [5] P. Flajolet and R. Sedgewick, Analytic Combinatorics, Cambridge University Press, 2009.

 [6] R. L. Graham, D. E. Knuth and O. Patashnik, Concrete Mathematics, Addison-Wesley,
     1994.

 [7] H. S. Wilf, Generatingfunctionology, A K Peters, 2006.

 [8] T. M. Apostol, Introduction to Analytic Number Theory, Springer, 1976.

 [9] OEIS Foundation Inc., The On-Line Encyclopedia of Integer Sequences, https://oeis.org,
     2026.




                                                7


