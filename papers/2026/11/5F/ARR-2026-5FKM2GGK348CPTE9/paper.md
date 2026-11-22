# A Wronskian Identity for Antisymmetrized Sine Sums: the surface-positivity problem as sine-series ratio monotonicity, and a counterexample to the naive monotonicity principle

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
A Wronskian Identity for Antisymmetrized Sine Sums:
the surface-positivity problem as sine-series ratio monotonicity, and a counterexample to
                             the naive monotonicity principle

                                               Lluis Eriksson

                                                  July 2026


                                                   Abstract
                                                                                    ∑︀
          For real arrays (𝑎𝑚 )𝑚≥1 , (𝑏𝑚 )𝑚≥1 (finitely supported, or summable with    𝑚(|𝑎𝑚 | +
      |𝑏𝑚 |) < ∞) we record the exact identity
        ∑︁
              (𝑎𝑚 𝑏𝑛 −𝑎𝑛 𝑏𝑚 ) (𝑚−𝑛) sin((𝑚+𝑛)𝑡)+(𝑚+𝑛) sin((𝑛−𝑚)𝑡) = 2 𝐹𝑎′ (𝑡) 𝐹𝑏 (𝑡)−𝐹𝑎 (𝑡) 𝐹𝑏′ (𝑡) ,
                             [︀                                       ]︀  [︀                       ]︀

      1≤𝑚<𝑛
                      ∑︀
      where 𝐹𝑥 (𝑡) = 𝑚 𝑥𝑚 sin(𝑚𝑡): the antisymmetrized double sum is a Wronskian of two sine
      series. The proof is two lines. As a consequence, the open surface-positivity problem of the
      companion 𝜙-lemma note — the sign of exactly such a double sum built from modified-Bessel
      coefficient arrays — is equivalent to the strict monotonicity of a ratio of two explicit sine
      series, and high-precision numerics indicate that the true statement is global: the Wronskian
      is negative on all of (0, 𝜋), not merely near 𝑡 = 𝜋. One might hope this follows from the
      companion result that the coefficient ratio 𝑎𝑚 /𝑏𝑚 is strictly increasing, in analogy with the
      Biernacki–Krzyż principle for power series. It does not: we give a hand-checkable coun-
      terexample — 𝑎 = (3, 4, 3), 𝑏 = (3, 2, 1), coefficient ratio (1, 2, 3) strictly increasing, 𝑏 strictly
      decreasing with 𝐹𝑏 > 0 on (0, 𝜋) by the √explicit factorization 𝐹𝑏 = 2 sin 𝑡 (2 cos2 𝑡+2 cos 𝑡+1),
      yet the Wronskian at 𝑡 = 2𝜋/3 equals 3 3/2 > 0 — so no analogue of Biernacki–Krzyż holds
      for sine series, and the surface problem cannot be closed by coefficient-ratio monotonicity
      alone. We state the resulting conjecture precisely, record the numerical phenomenology (near-
      perfect parity-mirror cancellation of relative size 𝑒−𝑐𝛽 , 𝑐 ≈ 2.1, with a working-precision
      warning), and identify the structural route we consider most promising. The identity is
      machine-checked in Lean 4/Mathlib (finite form, arbitrary 𝐾; no sorry, standard axiom or-
      acle), and the counterexamples are exact algebraic evaluations; nothing beyond the identity
      and the counterexamples is claimed.


1     The identity
Theorem 1 (Wronskian identity). Let (𝑎𝑚 ), (𝑏𝑚 ) be real arrays, finitely supported (or with
         𝑚 | + |𝑏𝑚 |) < ∞, in which case all series below converge absolutely and uniformly). Set
∑︀
  𝑚 𝑚(|𝑎∑︀
𝐹𝑎 (𝑡) = 𝑚≥1 𝑎𝑚 sin(𝑚𝑡) and likewise 𝐹𝑏 . Then, for all 𝑡 ∈ R,

      (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) (𝑚 − 𝑛) sin((𝑚 + 𝑛)𝑡) + (𝑚 + 𝑛) sin((𝑛 − 𝑚)𝑡) = 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
 ∑︁                    [︀                                                     ]︀    [︀                          ]︀

1≤𝑚<𝑛
                                                                                                               (1)
Proof. The product-to-sum formulas give, for any 𝑚, 𝑛,
                                                      [︀                                           ]︀
(𝑚−𝑛) sin((𝑚+𝑛)𝑡)+(𝑚+𝑛) sin((𝑛−𝑚)𝑡) = 2 𝑚 cos(𝑚𝑡) sin(𝑛𝑡)−𝑛 sin(𝑚𝑡) cos(𝑛𝑡) =: 2𝐺(𝑚, 𝑛),

                                                           1
```

---

## Page 2

```text
and 𝐺 is antisymmetric with 𝐺(𝑛, 𝑛) = 0. Since (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) is antisymmetric as well,
∑︁                                      ∑︁                      [︁∑︁                   ∑︁               ∑︁                 ∑︁
      (𝑎𝑚 𝑏𝑛 −𝑎𝑛 𝑏𝑚 ) 2𝐺(𝑚, 𝑛) = 2           𝑎𝑚 𝑏𝑛 𝐺(𝑚, 𝑛) = 2          𝑎𝑚 𝑚 cos(𝑚𝑡)        𝑏𝑛 sin(𝑛𝑡)−       𝑎𝑚 sin(𝑚𝑡)        𝑏𝑛 𝑛 cos(𝑛
𝑚<𝑛                                  𝑚,𝑛                            𝑚                  𝑛                  𝑚                𝑛

which is 2[𝐹𝑎′ 𝐹𝑏 − 𝐹𝑎 𝐹𝑏′ ].

Remark 2. Equivalently: wherever 𝐹𝑏 ̸= 0, the left side of (1) equals 2𝐹𝑏2 · (𝐹𝑎 /𝐹𝑏 )′ . Sign
questions about the antisymmetrized double sum are exactly monotonicity questions about the
ratio of the two sine series — with the Wronskian form remaining meaningful (and division-free)
across zeros of 𝐹𝑏 .


2      The surface-positivity problem, reduced
We recall the objects of the companion note [4] (which proved the coefficient-ratio monotonicity
used below; the wider programme context is in [6]). For 𝛽 > 0 let 𝑟𝑘 = 𝐼𝑘+1 (𝛽)/𝐼1 (𝛽) with 𝐼𝜇
the modified Bessel function of the first kind, and for 𝑘 ≥ 1
                            ∑︁
                 2
           𝐴𝑘 = 𝑟𝑘−1                (𝑗 + 1)𝑟𝑗2 ,              4
                                                      𝐵𝑘 = 𝑘 𝑟𝑘−1 ,          𝑐𝑚𝑛 = 𝐴𝑚 𝐵𝑛 − 𝐴𝑛 𝐵𝑚 .
                      𝑗∈{𝑘−2, 𝑘}, 𝑗≥0

The arrays satisfy the summability hypothesis of Theorem 1 for every 𝛽 > 0: by the standard
large-order asymptotics 𝐼𝑘 (𝛽) ∼ (𝛽/2)𝑘 /𝑘! [3, 10.41.1], the ratios 𝑟𝑘 decay super-exponentially
in 𝑘, hence so do 𝐴𝑚 and 𝐵𝑚 , and 𝑚 𝑚(𝐴𝑚 + 𝐵𝑚 ) < ∞. The open positivity problem is
                                     ∑︀

𝑊 (𝑡) < 0 for 𝑡 near 𝜋, where 𝑊 is the left side of (1) with (𝑎, 𝑏) = (𝐴, 𝐵). By Theorem 1,

𝑊 (𝑡) = 2 𝐹𝐴′ (𝑡)𝐹𝐵 (𝑡) − 𝐹𝐴 (𝑡)𝐹𝐵′ (𝑡) ,
            [︀                               ]︀                ∑︁                               ∑︁
                                                    𝐹𝐴 (𝑡) =         𝐴𝑚 sin(𝑚𝑡),   𝐹𝐵 (𝑡) =           𝐵𝑚 sin(𝑚𝑡).
                                                               𝑚≥1                              𝑚≥1

   Two facts sharpen the picture. First, the companion note proved 𝑐𝑚𝑛 < 0 for all 𝑚 < 𝑛
(the coefficient ratio 𝜙𝑚 = 𝐴𝑚 /𝐵𝑚 is strictly increasing) [4]. Second, high-precision numerics
(mpmath, 30–100 significant digits, truncation-stable) indicate that the Wronskian is strictly
negative on all of (0, 𝜋), at every 𝛽 tested (𝛽 ∈ {0.5, 2, 8, 32}, grids of 𝑡/𝜋 from 0.05 to 0.99),
and that 𝐹𝐵 > 0 on (0, 𝜋). The 𝜀-window form of the original problem is thus the boundary
shadow of a global statement, which we now record as the target.
Conjecture 3 (global ratio monotonicity). For every 𝛽 > 0: (i) 𝐹𝐵 > 0 on (0, 𝜋), and (ii) 𝐹𝐴 /𝐹𝐵
is strictly decreasing on (0, 𝜋). Given (i), part (ii) is equivalent to 𝑊 (𝑡) < 0 on (0, 𝜋), by
𝑊 = 2𝐹𝐵2 (𝐹𝐴 /𝐹𝐵 )′ ; the Wronskian form 𝑊 < 0 is the division-free statement and is what the
numerics test.


3      The naive principle fails
For power series with positive coefficients, the Biernacki–Krzyż principle [1] states that if 𝑎𝑚 /𝑏𝑚
                      𝑎𝑚 𝑥𝑚 / 𝑏𝑚 𝑥𝑚 is increasing on (0, 1). Given 𝜙𝑚 = 𝐴𝑚 /𝐵𝑚 increasing
                   ∑︀         ∑︀
is increasing then
and 𝑊 < 0 numerically, it is tempting to conjecture the sine-series analogue: coefficient ratio
increasing ⇒ ratio of sine series decreasing on (0, 𝜋) (the sign flip suggested by the boundary
behaviour at 𝑡 = 𝜋). This is false, even under strong positivity side conditions.



                                                        2
```

---

## Page 3

```text
Proposition 4 (counterexample, hand-checkable). Let 𝑎 = (3, 4, 3) and 𝑏 = (3, 2, 1) (all further
entries zero). Then: the coefficient ratio 𝑎𝑚 /𝑏𝑚 = (1, 2, 3) is strictly increasing; and 𝐹𝑏 (𝑡) =
3 sin 𝑡+2 sin 2𝑡+sin 3𝑡 = 2 sin 𝑡 (2 cos2 𝑡+2 cos 𝑡+1) > 0 on (0, 𝜋), since the quadratic 2𝑦 2 +2𝑦 +1
has negative discriminant. (We note in passing that mere coefficient decrease does not imply
sine positivity — sin 𝑡 + sin 2𝑡 < 0 near 𝑡 = 𝜋 — which is why we give the factorization rather
than cite a general positivity theorem; for genuine positivity criteria of Vietoris type see [2].)
And yet at 𝑡 = 2𝜋/3,
             √            √                                                     √     √       √
    𝐹𝑎 = − 23 ,    𝐹𝑏 =     3
                           2 ,   𝐹𝑎′ = 27 ,   𝐹𝑏′ = − 12 ,   𝐹𝑎′ 𝐹𝑏 − 𝐹𝑎 𝐹𝑏′ = 7 4 3 − 43 = 3 2 3 > 0.

Hence 𝐹𝑎 /𝐹𝑏 is strictly increasing at 𝑡 = 2𝜋/3: no Biernacki–Krzyż analogue holds for sine
series.
                                 √                  √
                                     3                3                        1              1
Proof. At 𝑡 = 2𝜋/3: sin 𝑡 =            , sin 2𝑡 = −  2 ,√sin 3𝑡√= 0; cos 𝑡 = − 2 , cos 2𝑡 = − 2 , cos 3𝑡 = 1.
                        √          √2
Then 𝐹𝑎 = (3 − 4) 23 = − 23 , 𝐹𝑏 = (3 − 2) 23 = 23 , 𝐹𝑎′ = 3(− 12 ) + 8(− 12 ) + 9 = 72 , 𝐹𝑏′ =
3(− 21 ) + 4(− 12 ) + 3 = − 21 ; combine.

   An even smaller example, with the Wronskian form: 𝑎 = (1, 2, 3, 4), 𝑏 = (1, 1, 1, 1) gives
𝐹𝑎′ 𝐹𝑏 − 𝐹𝑎 𝐹𝑏′
             = 4 at 𝑡 = 𝜋/2 (there 𝐹𝑏 vanishes, so this violates 𝑊 ≤ 0 though not ratio-
monotonicity on a domain of positivity — which is why Proposition 4 carries the decreasing-𝑏
condition).
Remark 5 (the moral, in the spirit of the parity barrier). As with the parity barrier for decoupling
inequalities [5], a bounded amount of structural data — here, the monotonicity of the coefficient
ratio, even together with positivity of 𝐹𝑏 — cannot certify the global sign. Whatever proves
Conjecture 3 must consume more of the Bessel structure of (𝐴𝑚 , 𝐵𝑚 ) than the order of 𝜙𝑚 .
This is consistent with the quantitative phenomenology: the even- and odd-parity halves of
𝑊 (𝜋 − 𝜀) cancel to relative accuracy ≈ 𝑒−𝑐𝛽 with 𝑐 ≈ 2.03–2.17 (true totals e.g. −2.9 · 10−8 at
𝛽 = 8; −5.0 · 10−29 at 𝛽 = 32; −5.1 · 10−95 at 𝛽 = 100), so any estimate that discards the exact
structure loses the sign entirely; numerical exploration below ≈ 2.2𝛽+20 working digits sees pure
rounding noise. The route we consider most promising: 𝑟𝑘2 and 𝑟𝑘4 are ratios of Bessel products
with integral (Schläfli/heat-kernel) representations, so 𝐹𝐴 and 𝐹𝐵 admit kernel representations
on the circle; a positive integral representation of −(𝐹𝐴 /𝐹𝐵 )′ — or a total-positivity property
of the array (𝐴; 𝐵) against the sine kernel — would close Conjecture 3 where coefficient-order
arguments provably cannot.


4    Verification
Theorem 1 was verified symbolically (sympy) for generic coefficients at 𝐾 ≤ 5 (residual 0 after
trigonometric normalisation) and at 𝐾 = 7 by exact rational substitution (residual < 10−35 at
40 digits, four random points), and numerically against the direct double sum for the Bessel
arrays at 𝐾 = 90, 𝛽 = 8, at 𝑡 ∈ {0.5, 1.5, 2.6, 𝜋 − 0.1} (ratio 1.0 to all displayed digits). The
counterexample values of Proposition 4 are exact algebraic evaluations. The global sign scan of
𝑊 and the parity-mirror measurements are as in the companion note. Scripts and sources are
archived at
    https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME (docs/BF2-ATTACK-NOTES.md,
                               papers/wronskian-reduction).


                                                        3
```

---

## Page 4

```text
Theorem 1 (finite form, arbitrary 𝐾) is moreover machine-checked in Lean 4/Mathlib (file
WronskianIdentity.lean accompanying this note; checked with lake env lean against Lean
4.30.0-rc2, Mathlib commit cd3b69b): bracket_eq_two_G (the trigonometric collapse), double_sum_eq_wronsk
(the product structure), pair_sum_eq_double_sum (the antisymmetrization) and wronskian_identity
(the theorem). The axiom oracle returns Lean’s three standard axioms for all four; no sorry:

’wronskian_identity’ depends on axioms:
    [propext, Classical.choice, Quot.sound]

(exit code 0; likewise for the three lemmas).

Acknowledgements
This note is part of an audit-first research programme whose records, Lean sources and numerical
suites are public at https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME. Nothing
is claimed about Conjecture 3 beyond its equivalence to the original surface-positivity problem
and the failure of the naive route; nothing is claimed about four-dimensional gauge theory.


References
[1] M. Biernacki and J. Krzyż, On the monotonity of certain functionals in the theory of analytic func-
    tions, Ann. Univ. Mariae Curie-Skłodowska Sect. A 9 (1955), 135–147.

[2] R. Askey and J. Steinig, Some positive trigonometric sums, Trans. Amer. Math. Soc. 187 (1974),
    295–307.

[3] F. W. J. Olver et al., NIST Digital Library of Mathematical Functions, §§10.29, 10.41; https://
    dlmf.nist.gov/10.29, https://dlmf.nist.gov/10.41.

[4] L. Eriksson, A weighted Turán-type monotonicity lemma for modified Bessel functions via the cali-
    brated Amos bound, with an application to the ordering of a surface expansion in two-dimensional
    lattice gauge theory, July 2026; https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/
    tree/main/papers/phi-lemma.

[5] L. Eriksson, Parity barriers for decoupling inequalities, July 2026; https://github.com/
    lluiseriksson/THE-ERIKSSON-PROGRAMME/tree/main/papers/parity-barriers.

[6] L. Eriksson, THE MASTER MAP: an audit-first navigation guide to the conditional construction
    of 4D 𝑆𝑈 (𝑁 ) Yang–Mills with mass gap, ai.viXra:2602.0096, and the programme repository https:
    //github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.




                                                  4
```
