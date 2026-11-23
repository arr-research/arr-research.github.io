# A Wronskian Identity for Antisymmetrized Sine Sums: unconditional denominator positivity via circular convolution, sharp monotonicity distinctions, and counterexamples to naive sine-series principles

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
A Wronskian Identity for Antisymmetrized Sine Sums:
             unconditional denominator positivity via circular convolution,
    sharp monotonicity distinctions, and counterexamples to naive sine-series principles

                                              Lluis Eriksson

                                        23 November 2026 (v2)


                                                 Abstract

      ∑︀ For real arrays (𝑎𝑚 )𝑚≥1 and (𝑏𝑚 )𝑚≥1 that are finitely supported, or summable with
        𝑚≥1 𝑚(|𝑎𝑚 | + |𝑏𝑚 |) < ∞, we prove the exact Wronskian identity
        ∑︁
              (𝑎𝑚 𝑏𝑛 −𝑎𝑛 𝑏𝑚 ) (𝑚−𝑛) sin((𝑚+𝑛)𝑡)+(𝑚+𝑛) sin((𝑛−𝑚)𝑡) = 2 𝐹𝑎′ (𝑡) 𝐹𝑏 (𝑡)−𝐹𝑎 (𝑡) 𝐹𝑏′ (𝑡) ,
                             [︀                                  ]︀  [︀                            ]︀

      1≤𝑚<𝑛
                       ∑︀
      where 𝐹𝑥 (𝑡) = 𝑚≥1 𝑥𝑚 sin(𝑚𝑡), with explicit Fubini justification of the rearrangement in the
      infinite-series case. Applying this identity to the modified-Bessel coefficient arrays (𝐴𝑚 , 𝐵𝑚 )
      from a companion two-dimensional lattice gauge theory surface-positivity problem, we first
      prove unconditionally for every 𝛽 > 0 that 𝐹𝐵 (𝑡) = −(𝑓 *4 )′ (𝑡)/(2𝐼1 (𝛽)4 ) > 0 on (0, 𝜋), where
      𝑓 (𝑡) = 𝑒𝛽 cos 𝑡 and 𝑓 *4 is its fourfold normalized circular convolution (Theorem 5), closing
      part (i) of v1’s Conjecture 3 without numerics. We then distinguish precisely between: (a)
      strict decrease of the real-analytic ratio 𝐹𝐴 /𝐹𝐵 on (0, 𝜋) (equivalent to 𝑊 ≤ 0 and 𝑊 ̸≡ 0),
      (b) strict pointwise negativity 𝑊 (𝑡) < 0 on (0, 𝜋) (strictly stronger, as shown by the finite
      example 𝐹𝑏 = sin 𝑡, 𝐹𝑎 = 41 sin 2𝑡 + 18 sin 4𝑡 with 𝐹𝑎 /𝐹𝑏 = cos3 𝑡 and 𝑊 (𝜋/2) = 0), and (c)
      local negativity near 𝑡 = 𝜋 (which is strictly weaker under generic side conditions, as shown
      by the finite counterexample 𝑎 = (6, 10, 24), 𝑏 = (6, 5, 2)). We also retain the hand-checkable
      counterexample 𝑎 = (3, 4, 3), 𝑏 = (3, 2, 1) refuting any unrestricted sine-series analogue of the
      Biernacki–Krzyż principle even when 𝑎𝑚 /𝑏𝑚 is strictly increasing on the support and 𝐹𝑏 > 0
      on (0, 𝜋). The finite Wronskian identity (arbitrary 𝐾) is machine-checked in Lean 4/Mathlib
      (WronskianIdentity.lean, zero sorry, standard axioms only), and every counterexample is
      an exact algebraic evaluation. The global Bessel sign conjecture 𝑊 (𝑡) < 0 on (0, 𝜋) remains
      open.


1     The Wronskian identity
Theorem 1 (Wronskian identity). Let (𝑎 )           𝑚 𝑚≥1    and (𝑏 )𝑚 𝑚≥1       be real sequences satisfying
             |   |𝑏   |)       ∞
∑︀
      𝑚(|𝑎 𝑚   +    𝑚     <        (in particular,  any finitely   supported   sequences). Set 𝐹𝑎 (𝑡) =
∑︀𝑚≥1                                                                     1 (R) with termwise derivatives
                                                                      ∈
                                   ∑︀
      𝑎  sin(𝑚𝑡)
   𝑚≥1 𝑚∑︀        and    𝐹 𝑏 (𝑡) =        𝑏
                                      𝑚≥1 𝑚  sin(𝑚𝑡).  Then  𝐹 𝑎 , 𝐹𝑏   𝐶
  ′                                     ′      ∑︀
𝐹𝑎 (𝑡) = 𝑚≥1 𝑚𝑎𝑚 cos(𝑚𝑡) and 𝐹𝑏 (𝑡) = 𝑚≥1 𝑚𝑏𝑚 cos(𝑚𝑡), the double series below converges
absolutely and uniformly on R, and for all 𝑡 ∈ R,

      (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) (𝑚 − 𝑛) sin((𝑚 + 𝑛)𝑡) + (𝑚 + 𝑛) sin((𝑛 − 𝑚)𝑡) = 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
 ∑︁                    [︀                                                  ]︀      [︀                       ]︀

1≤𝑚<𝑛
                                                                                                           (1)



                                                      1
```

---

## Page 2

```text
Proof. Since |𝑎𝑚 sin(𝑚𝑡)| ≤ |𝑎𝑚 | ≤ 𝑚|𝑎𝑚 | and |𝑚𝑎𝑚 cos(𝑚𝑡)| ≤ 𝑚|𝑎𝑚 |, the Weierstrass 𝑀 -test
yields uniform convergence of 𝐹𝑎 , 𝐹𝑏 , 𝐹𝑎′ , 𝐹𝑏′ on R and validates termwise differentiation. For any
𝑚, 𝑛 ≥ 1, the product-to-sum identities give

         (𝑚 − 𝑛) sin((𝑚 + 𝑛)𝑡) + (𝑚 + 𝑛) sin((𝑛 − 𝑚)𝑡)
                                         [︀                                                              ]︀
                                  = 2 𝑚 cos(𝑚𝑡) sin(𝑛𝑡) − 𝑛 sin(𝑚𝑡) cos(𝑛𝑡) =: 2 𝐺(𝑚, 𝑛).

Note that |𝐺(𝑚, 𝑛)| ≤ 𝑚 + 𝑛, 𝐺(𝑛, 𝑚) = −𝐺(𝑚, 𝑛), and 𝐺(𝑛, 𝑛) = 0. Moreover,
            ∑︁                         (︁ ∑︁                )︁(︁ ∑︁      )︁     (︁ ∑︁           )︁(︁ ∑︁             )︁
                  |𝑎𝑚 𝑏𝑛 | (𝑚 + 𝑛) =            𝑚|𝑎𝑚 |                |𝑏𝑛 | +           |𝑎𝑚 |                 𝑛|𝑏𝑛 | < ∞,
          𝑚,𝑛≥1                         𝑚≥1                    𝑛≥1               𝑚≥1               𝑛≥1

so every double sum below is absolutely convergent and may be rearranged freely by Fubini’s
theorem. Using the joint antisymmetry of (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) and 𝐺(𝑚, 𝑛) together with 𝐺(𝑛, 𝑛) = 0,
       ∑︁                                          ∑︁                                                    ∑︁
            (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) 2𝐺(𝑚, 𝑛) =                 (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) 𝐺(𝑚, 𝑛) = 2                               𝑎𝑚 𝑏𝑛 𝐺(𝑚, 𝑛)
     1≤𝑚<𝑛                                      𝑚,𝑛≥1                                               𝑚,𝑛≥1
                                                  [︁(︁ ∑︁                       )︁(︁ ∑︁                       )︁
                                              =2             𝑚𝑎𝑚 cos(𝑚𝑡)                  𝑏𝑛 sin(𝑛𝑡)
                                                    𝑚≥1                            𝑛≥1
                                                            (︁ ∑︁                  )︁(︁ ∑︁                          )︁]︁
                                                        −             𝑎𝑚 sin(𝑚𝑡)              𝑛𝑏𝑛 cos(𝑛𝑡)
                                                              𝑚≥1                       𝑛≥1
                                              = 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
                                                 [︀                            ]︀


Remark 2. Wherever 𝐹𝑏 (𝑡) ̸= 0, the quotient rule gives
                                                                          𝑑                  𝐹𝑎 (𝑡)
                                                                                             (︂               )︂
                     𝑊 (𝑡) := 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) = 2 𝐹𝑏 (𝑡)2
                               [︀                            ]︀
                                                                                                    .
                                                                                          𝑑𝑡 𝐹𝑏 (𝑡)
Thus on any open interval 𝐼 where 𝐹𝑏 ̸= 0, pointwise strict negativity 𝑊 (𝑡) < 0 on 𝐼 is equiv-
alent to (𝐹𝑎 /𝐹𝑏 )′ (𝑡) < 0 on 𝐼, which is strictly stronger than strict decrease of 𝐹𝑎 /𝐹𝑏 on 𝐼 (see
Proposition 6).


2    The Bessel arrays and unconditional denominator positivity
We recall the modified-Bessel coefficient arrays from the companion note [4] (AIRR record ARR-
                                                                                      (𝛽/2)𝜇+2𝑗
2026-72G1SSCNNG8YDVC2; programme context in [5]). For 𝛽 > 0, let 𝐼𝜇 (𝛽) = ∞
                                                                               ∑︀
                                                                                 𝑗=0 𝑗! Γ(𝜇+𝑗+1) be
the modified Bessel function of the first kind, set 𝑟𝑘 = 𝐼𝑘+1 (𝛽)/𝐼1 (𝛽) for 𝑘 ≥ 0, and define for
𝑘 ≥ 1,

          2
                     ∑︁                                                       𝐼𝑘 (𝛽)4
    𝐴𝑘 = 𝑟𝑘−1               (𝑗 + 1)𝑟𝑗2 ,                   4
                                                   𝐵𝑘 = 𝑘 𝑟𝑘−1 =𝑘                     ,           𝑐𝑚𝑛 = 𝐴𝑚 𝐵𝑛 − 𝐴𝑛 𝐵𝑚 .
              𝑗∈{𝑘−2, 𝑘}, 𝑗≥0
                                                                              𝐼1 (𝛽)4

Lemma 3 (Non-asymptotic super-exponential decay). For every 𝛽 > 0 and every integer 𝑘 ≥ 0,

                                                               (𝛽/2)𝑘
                                         0 < 𝐼𝑘 (𝛽) ≤                 𝐼0 (𝛽).
                                                                 𝑘!
                                  𝑘
Consequently 𝑟𝑘−1 ≤ 𝐼𝐼01 (𝛽) (𝛽/2)                                           𝑚     4 (up to a
                                                                                                    (︀                     )︀
                         (𝛽) 𝑘! ∑︀, both 𝐴𝑚 and 𝐵𝑚 decay at least as 𝑂 ((𝛽/2) /𝑚!)
polynomial factor in 𝑚), and 𝑚≥1 𝑚(𝐴𝑚 + 𝐵𝑚 ) < ∞ for every 𝛽 > 0. Moreover, 𝐹𝐴 and 𝐹𝐵
extend to entire (hence real-analytic on R) 2𝜋-periodic odd functions.

                                                               2
```

---

## Page 3

```text
= (𝑘+𝑗)!
               (︀𝑘+𝑗 )︀
Proof. Since      𝑗          𝑘! 𝑗! ≥ 1 for all 𝑘, 𝑗 ≥ 0, we have (𝑘 + 𝑗)! ≥ 𝑘! 𝑗!, whence
                                     ∞                                ∞
                                     ∑︁ (𝛽/2)𝑘+2𝑗              (𝛽/2)𝑘 ∑︁ (𝛽/2)2𝑗   (𝛽/2)𝑘
                          𝐼𝑘 (𝛽) =                         ≤                     =        𝐼0 (𝛽).
                                     𝑗=0
                                            𝑗! (𝑘 + 𝑗)!          𝑘! 𝑗=0 (𝑗!)2        𝑘!

Positivity follows termwise for 𝛽 > 0. Substituting into 𝐴𝑚 and 𝐵𝑚 gives the stated factorial-
fourth-power bound, which implies 𝑚≥1 𝑚𝑟 (𝐴𝑚 + 𝐵𝑚 ) < ∞ for every 𝑟 ≥ 0 and absolute
                                     ∑︀

convergence of the complex trigonometric series on all of C (since | sin(𝑚𝑧)| ≤ 𝑒𝑚| Im 𝑧| ).

   We now prove unconditionally that 𝐹𝐵 (𝑡) > 0 on (0, 𝜋) for every 𝛽 > 0, closing part (i) of v1’s
Conjecture 3 analytically.
Lemma 4 (Circular convolution preserves even strict decrease). Let 𝑔, ℎ ∈ 𝐶 1 (R) be 2𝜋-periodic
and even, and suppose 𝑔 ′ (𝑠) < 0 and ℎ′ (𝑠) < 0 for all 𝑠 ∈ (0, 𝜋). Define their normalized circular
convolution
                                              1 𝜋
                                                 ∫︁
                               (𝑔 * ℎ)(𝑡) :=         𝑔(𝑠) ℎ(𝑡 − 𝑠) 𝑑𝑠.
                                             2𝜋 −𝜋
Then 𝑔 * ℎ ∈ 𝐶 1 (R) is 2𝜋-periodic, even, and satisfies (𝑔 * ℎ)′ (𝑡) < 0 for all 𝑡 ∈ (0, 𝜋).
Proof. Periodicity   and evenness follow by the substitution 𝑠 ↦→ −𝑠. By periodicity we may write
              1 ∫︀ 𝜋
(𝑔 * ℎ)(𝑡) = 2𝜋 −𝜋 𝑔(𝑡 − 𝑢) ℎ(𝑢) 𝑑𝑢, differentiate under the integral sign, and change variables back
to 𝑠 = 𝑡 − 𝑢:
                                     ∫︁ 𝜋                                    ∫︁ 𝜋
                                 1                                      1
             (𝑔 * ℎ)′ (𝑡) =                  𝑔 ′ (𝑠) ℎ(𝑡 − 𝑠) 𝑑𝑠 =                  𝑔 ′ (𝑠) ℎ(𝑡 − 𝑠) − ℎ(𝑡 + 𝑠) 𝑑𝑠,
                                                                                         [︀                   ]︀
                                2𝜋    −𝜋                               2𝜋     0

using 𝑔 ′ (−𝑠) = −𝑔 ′ (𝑠) because 𝑔 is even. Because ℎ is 2𝜋-periodic, even, and strictly decreasing
on [0, 𝜋], there is a strictly increasing function ℎ̃ : [−1, 1] → R such that ℎ(𝜃) = ℎ̃(cos 𝜃) for all
𝜃 ∈ R. For any 𝑡, 𝑠 ∈ (0, 𝜋),

                                      cos(𝑡 − 𝑠) − cos(𝑡 + 𝑠) = 2 sin 𝑡 sin 𝑠 > 0,

so ℎ(𝑡 − 𝑠) − ℎ(𝑡 + 𝑠) = ℎ̃(cos(𝑡 − 𝑠)) − ℎ̃(cos(𝑡 + 𝑠)) > 0. Together with 𝑔 ′ (𝑠) < 0 on (0, 𝜋), the
integrand is strictly negative on all of (0, 𝜋), giving (𝑔 * ℎ)′ (𝑡) < 0.

Theorem 5 (Unconditional denominator positivity). For every 𝛽 > 0 and every 𝑡 ∈ (0, 𝜋),
                                               ∞
                                               ∑︁        𝐼𝑘 (𝛽)4             (𝑓 *4 )′ (𝑡)
                                𝐹𝐵 (𝑡) =             𝑘         4
                                                                 sin(𝑘𝑡) = −              > 0,
                                               𝑘=1
                                                         𝐼1 (𝛽)              2 𝐼1 (𝛽)4

where 𝑓 (𝑡) := 𝑒𝛽 cos 𝑡 and 𝑓 *4 := (𝑓 * 𝑓 ) * (𝑓 * 𝑓 ).
Proof. By the Jacobi–Anger expansion [3, 10.35.2], 𝑓 (𝑡) = 𝑒𝛽 cos 𝑡 = 𝑘∈Z 𝐼𝑘 (𝛽)𝑒𝑖𝑘𝑡 with 𝐼−𝑘 (𝛽) =
                                                                                                ∑︀

𝐼𝑘 (𝛽), converging uniformly on R. Under normalized circular convolution, Fourier coefficients
multiply, so the 𝑘-th Fourier coefficient of 𝑓 *4 is 𝐼𝑘 (𝛽)4 :
                                                                       ∞
                                        𝑓 *4 (𝑡) = 𝐼0 (𝛽)4 + 2
                                                                       ∑︁
                                                                             𝐼𝑘 (𝛽)4 cos(𝑘𝑡).
                                                                       𝑘=1

By Lemma 3, termwise differentiation is justified uniformly on R and yields
                                                     ∞
                                     *4 ′
                                                     ∑︁
                              −(𝑓 ) (𝑡) = 2                𝑘 𝐼𝑘 (𝛽)4 sin(𝑘𝑡) = 2 𝐼1 (𝛽)4 𝐹𝐵 (𝑡).
                                                     𝑘=1


                                                                   3
```

---

## Page 4

```text
For 𝛽 > 0, 𝑓 ∈ 𝐶 ∞ (R) is 2𝜋-periodic, even, and satisfies 𝑓 ′ (𝑡) = −𝛽 sin 𝑡 𝑒𝛽 cos 𝑡 < 0 on (0, 𝜋).
Applying Lemma 4 to (𝑓, 𝑓 ) yields 𝑓 *2 even, 2𝜋-periodic, 𝐶 ∞ , and strictly decreasing on (0, 𝜋);
applying Lemma 4 once more to (𝑓 *2 , 𝑓 *2 ) gives (𝑓 *4 )′ (𝑡) < 0 on (0, 𝜋). Dividing by 2𝐼1 (𝛽)4 > 0
gives 𝐹𝐵 (𝑡) > 0 on (0, 𝜋).


3    Sharp monotonicity distinctions and the global conjecture
Let 𝑊 (𝑡) := 2[𝐹𝐴′ (𝑡)𝐹𝐵 (𝑡) − 𝐹𝐴 (𝑡)𝐹𝐵′ (𝑡)] be the Wronskian of Theorem 1 at (𝑎, 𝑏) = (𝐴, 𝐵). In
the companion note [4], the surface-positivity problem asks for 𝑊 (𝑡) < 0 in a left neighborhood
of 𝑡 = 𝜋, and proves that the coefficient ratio 𝜙𝑚 = 𝐴𝑚 /𝐵𝑚 is strictly increasing (𝑐𝑚𝑛 < 0
for all 𝑚 < 𝑛). By Theorem 5, 𝐹𝐴 /𝐹𝐵 is real-analytic and well-defined on all of (0, 𝜋), with
(𝐹𝐴 /𝐹𝐵 )′ = 𝑊/(2𝐹𝐵2 ).
    We clarify two logical distinctions that were blurred in v1. First, strict decrease of 𝐹𝑎 /𝐹𝑏 is
not equivalent to pointwise strict negativity 𝑊 < 0.

Proposition 6 (Strict decrease allows isolated zeros of 𝑊 ). For 𝐹𝑏 (𝑡) = sin 𝑡 (positive on (0, 𝜋))
and 𝐹𝑎 (𝑡) = 41 sin(2𝑡) + 18 sin(4𝑡), we have

                                             𝐹𝑎 (𝑡)
                                                    = cos3 𝑡,
                                             𝐹𝑏 (𝑡)

which is strictly decreasing on (0, 𝜋), yet 𝑊 (𝑡) = 2 sin2 𝑡·(−3 cos2 𝑡 sin 𝑡) = −6 sin3 𝑡 cos2 𝑡 vanishes
at 𝑡 = 𝜋/2. In general, for real-analytic 𝐹𝐴 , 𝐹𝐵 with 𝐹𝐵 > 0 on (0, 𝜋), strict decrease of 𝐹𝐴 /𝐹𝐵
on (0, 𝜋) is equivalent to 𝑊 (𝑡) ≤ 0 on (0, 𝜋) with 𝑊 ̸≡ 0, whereas 𝑊 (𝑡) < 0 on all of (0, 𝜋) is the
strictly stronger assertion that (𝐹𝐴 /𝐹𝐵 )′ (𝑡) < 0 everywhere on (0, 𝜋).

Proof. Using sin(2𝑡) = 2 sin 𝑡 cos 𝑡 and sin(4𝑡) = 4 sin 𝑡 cos 𝑡(2 cos2 𝑡 − 1),

                            𝐹𝑎 (𝑡)
                                   = 21 cos 𝑡 + 12 cos 𝑡(2 cos2 𝑡 − 1) = cos3 𝑡.
                            sin 𝑡
Hence (𝐹𝑎 /𝐹𝑏 )′ (𝑡) = −3 cos2 𝑡 sin 𝑡 ≤ 0 with unique zero at 𝑡 = 𝜋/2 in (0, 𝜋), so 𝐹𝑎 /𝐹𝑏 is strictly
decreasing while 𝑊 (𝜋/2) = 0. For real-analytic 𝐹𝐴 /𝐹𝐵 on the connected interval (0, 𝜋), if 𝑊 ≤ 0
and 𝑊 ̸≡ 0 then the zeros of (𝐹𝐴 /𝐹𝐵 )′ are isolated, so 𝐹𝐴 /𝐹𝐵 is strictly decreasing; conversely,
strict decrease forces (𝐹𝐴 /𝐹𝐵 )′ ≤ 0 and (𝐹𝐴 /𝐹𝐵 )′ ̸≡ 0.

   Second, global negativity on (0, 𝜋) strictly implies near-𝜋 negativity, and no reverse local-to-
global implication follows from the generic side conditions alone (see Proposition 9 below). We
therefore state the global conjecture as a strengthening of the original near-𝜋 problem, not as an
equivalence:
Conjecture 7 (Global Wronskian negativity for the Bessel arrays). For every 𝛽 > 0:

 (a) (Weak/strict-decrease form) 𝑊 (𝑡) ≤ 0 for all 𝑡 ∈ (0, 𝜋) and 𝑊 ̸≡ 0 (equivalently, by Theo-
     rem 5 and real-analyticity, 𝐹𝐴 /𝐹𝐵 is strictly decreasing on (0, 𝜋)).

 (b) (Strong/pointwise form) 𝑊 (𝑡) < 0 for all 𝑡 ∈ (0, 𝜋) (equivalently, (𝐹𝐴 /𝐹𝐵 )′ (𝑡) < 0 every-
     where on (0, 𝜋)).




                                                     4
```

---

## Page 5

```text
4    Counterexamples to naive sine-series monotonicity and local-
     to-global lifting
For power series with positive coefficients converging on a common interval (0, 𝑅) with nonvanish-
ing denominator, the Biernacki–Krzyż principle [1] asserts that monotonicity of 𝑎𝑚 /𝑏𝑚 transfers
                       𝑎𝑚 𝑥𝑚 / 𝑏𝑚 𝑥𝑚 . No unrestricted analogue holds for sine series, even on
                    ∑︀         ∑︀
to monotonicity of
finite supports where 𝑏𝑚 > 0 decreases, 𝑎𝑚 /𝑏𝑚 strictly increases on the support {1, . . . , 𝐾}, and
𝐹𝑏 > 0 on (0, 𝜋).

Proposition 8 (Counterexample to unrestricted sine-series Biernacki–Krzyż). Let 𝑎 = (3, 4, 3)
and 𝑏 = (3, 2, 1) on indices 𝑚 ∈ {1, 2, 3} (with 𝑎𝑚 = 𝑏𝑚 = 0 for 𝑚 ≥ 4). On the support {1, 2, 3},
𝑏𝑚 is strictly decreasing and the coefficient ratio 𝑎𝑚 /𝑏𝑚 = (1, 2, 3) is strictly increasing; moreover

        𝐹𝑏 (𝑡) = 3 sin 𝑡 + 2 sin 2𝑡 + sin 3𝑡 = 2 sin 𝑡 (2 cos2 𝑡 + 2 cos 𝑡 + 1) > 0         ∀𝑡 ∈ (0, 𝜋),

since 2𝑦 2 + 2𝑦 + 1 = 2(𝑦 + 21 )2 + 12 > 0. Yet at 𝑡 = 2𝜋/3,
                     √                 √                                                    √
            𝐹𝑎 = − 23 ,       𝐹𝑏 =      3
                                       2 ,   𝐹𝑎′ = 72 ,   𝐹𝑏′ = − 12 ,   𝐹𝑎′ 𝐹𝑏 − 𝐹𝑎 𝐹𝑏′ = 3 2 3 > 0,
               √
so 𝑊 (2𝜋/3) = 3 3 > 0 and 𝐹𝑎 /𝐹𝑏 is strictly increasing at 𝑡 = 2𝜋/3.
                                     √           √
                                  3                3
Proof. At 𝑡 = 2𝜋/3: sin 𝑡 =         , sin 2𝑡 = −     , sin 3𝑡 = 0; cos 𝑡 = − 12 , cos 2𝑡 = − 12 , cos 3𝑡 = 1.
                      √      √ 2               √ 2     √
Hence 𝐹𝑎 = (3 − 4) 23 = − 23 , 𝐹𝑏 = (3 − 2) 23 = 23 , 𝐹𝑎′ = − 23 − 4 + 9 = 72 , and 𝐹𝑏′ = − 32 − 2 + 3 =
− 12 . (Mere coefficient decrease does not in general force sine positivity, e.g. sin 𝑡 + sin 2𝑡 < 0 near
𝜋; see [2] for Vietoris-type criteria, which is why we verify 𝐹𝑏 > 0 directly by factorization.)

Proposition 9 (Near-𝜋 negativity does not force global negativity). Let 𝑎 = (6, 10, 24) and
𝑏 = (6, 5, 2) on indices 𝑚 ∈ {1, 2, 3} (zero for 𝑚 ≥ 4). Then on {1, 2, 3}, 𝑏𝑚 is strictly decreasing,
𝑎𝑚 /𝑏𝑚 = (1, 2, 12) is strictly increasing, and

        𝐹𝑏 (𝑡) = 6 sin 𝑡 + 5 sin 2𝑡 + 2 sin 3𝑡 = sin 𝑡 (8 cos2 𝑡 + 10 cos 𝑡 + 4) > 0         ∀𝑡 ∈ (0, 𝜋),

since 102 − 4 · 8 · 4 = −28 < 0. Near 𝑡 = 𝜋, setting 𝑡 = 𝜋 − 𝜀 yields 𝑊 (𝜋 −√𝜀) = −8𝜀3 + 𝑂(𝜀5 ) < 0
for all sufficiently small 𝜀 > 0. Nevertheless, at 𝑡 = 2𝜋/3, 𝑊 (2𝜋/3) = 51 3 > 0. Thus any proof
of Conjecture 7 from near-𝜋 negativity must invoke Bessel-specific structure beyond these generic
side conditions.

Proof. Using sin 2𝑡 = 2 sin 𝑡 cos 𝑡 and sin 3𝑡 = sin 𝑡(4 cos2 𝑡 − 1) gives 𝐹𝑏 (𝑡)/ sin 𝑡 = 6 + 10 cos 𝑡 +
2(4 cos2 𝑡 − 1) = 8 cos2 𝑡 + 10 cos 𝑡 + 4 > 0. Similarly 𝐹𝑎 (𝑡)/ sin 𝑡 = 96 cos2 𝑡 + 20 cos 𝑡 − 18. Writing
𝑦 = cos 𝑡 ∈ (−1, 1), the quotient 𝑞(𝑦) = 𝐹𝑎 /𝐹𝑏 = (96𝑦 2 + 20𝑦 − 18)/(8𝑦 2 + 10𝑦 + 4) has derivative

                                     2(400𝑦 2 + 528𝑦 + 130)   4(200𝑦 2 + 264𝑦 + 65)
                         𝑞 ′ (𝑦) =                          =                       .
                                        (8𝑦 2 + 10𝑦 + 4)2       (8𝑦 2 + 10𝑦 + 4)2

Since 𝑑𝑦/𝑑𝑡 = − sin 𝑡 < 0, the sign of 𝑊 (𝑡) = 2𝐹𝑏 (𝑡)2 𝑞 ′ (cos 𝑡)(− sin 𝑡) is opposite to the sign
of 𝑝(𝑦) := 200𝑦 2 + 264𝑦 + 65. At 𝑦 = −1 (𝑡 = 𝜋), 𝑝(−1) = 1 > 0, confirming 𝑊 (𝜋 − 𝜀) =
−8𝜀3 + 𝑂(𝜀5 ) < 0 for small 𝜀 > 0. At 𝑡 = 2𝜋/3 (𝑦 = −1/2), 𝑝(−1/2) = 50 −√132 + 65 = −17 < 0,
                 √                  √                                                       √
and 𝐹𝑏 (2𝜋/3) = ( 3/2)(2−5+4) = 3/2, giving 𝑊 (2𝜋/3) = 2· 34 · 4(−17)              3
                                                                             (︀      )︀
                                                                      1 2  ·    − 2     = 51  3 > 0.



                                                           5
```

---

## Page 6

```text
Remark 10 (Structural moral and numerical precision). Propositions 8 and 9 show that coefficient-
ratio monotonicity and denominator positivity alone cannot certify the sign of 𝑊 , nor lift local
near-𝜋 negativity to (0, 𝜋). Quantitatively, high-precision scans of the Bessel arrays (archived
at docs/BF2-ATTACK-NOTES.md) display parity-mirror cancellation between even- and odd-index
sums of relative magnitude ≈ 𝑒−𝑐𝛽 (𝑐 ≈ 2.1, corresponding to roughly 𝑐𝛽/ ln 10 ≈ 0.91𝛽 lost
decimal digits; e.g. 𝑊 ≈ −2.9 · 10−8 at 𝛽 = 8 and −5.0 · 10−29 at 𝛽 = 32 on sampled grids).
Maintaining ≥ 𝛽 + 20 (conservatively 2.2𝛽 + 20) working digits prevents catastrophic cancellation
on tested grids, though grid samples never constitute a continuum proof. Theorem 5 already
realizes 𝐹𝐵 as an exact circle-convolution derivative; a corresponding positive kernel representation
of −𝑊 (or total positivity of (𝐴; 𝐵) against the sine kernel) remains the natural analytic route
to Conjecture 7.


5    Verification
Theorem 1 (finite form, arbitrary 𝐾) is machine-checked in Lean 4 / Mathlib
(WronskianIdentity.lean, accompanying papers/wronskian-reduction in https://github
.com/lluiseriksson/THE-ERIKSSON-PROGRAMME): declarations bracket_eq_two_G, double_-
sum_eq_wronskian, pair_sum_eq_double_sum, and wronskian_identity, each with zero sorry
and axiom readout [propext, Classical.choice, Quot.sound]. Symbolically, Theorem 1 was
checked in SymPy for generic arrays at 𝐾 ≤ 5 (exact algebraic zero after trigonometric expan-
sion), numerically evaluated at 𝐾 = 7 at rational inputs with 40-digit precision (residual < 10−35 ,
a high-precision numerical check rather than exact rational arithmetic), and compared against
the direct Bessel double sum at 𝐾 = 90, 𝛽 = 8, 𝑡 ∈ {0.5, 1.5, 2.6, 𝜋 − 0.1}. Propositions 6, 8, and
9 are exact algebraic evaluations (also cross-checked in SymPy), and the convolution identity in
Theorem 5 was independently cross-checked by 30-digit numerical quadrature at 𝛽 ∈ {0.5, 2.0}.

Scope and Disclosure
This v2 revision addresses all material objections raised by v1’s independent assessments (ARR-
2026-5FKM2GGK348CPTE9 v1). Conjecture 7 remains open, and no claim is made regarding four-
dimensional gauge theory or a Yang–Mills mass gap. Large language models assisted manuscript
preparation under author supervision; author Lluis Eriksson administers AIRR (https://airr
.science/), so no independent editorial admission is claimed.


References
[1] M. Biernacki and J. Krzyż, On the monotonity of certain functionals in the theory of analytic functions,
    Ann. Univ. Mariae Curie-Skłodowska Sect. A 9 (1955), 135–147.

[2] R. Askey and J. Steinig, Some positive trigonometric sums, Trans. Amer. Math. Soc. 187 (1974),
    295–307.

[3] F. W. J. Olver et al., NIST Digital Library of Mathematical Functions, §§10.35, 10.41; https://dlmf
    .nist.gov/10.35, https://dlmf.nist.gov/10.41.

[4] L. Eriksson, A weighted Turán-type monotonicity lemma for modified Bessel functions via the calibrated
    Amos bound, with an application to the ordering of a surface expansion in two-dimensional lattice gauge
    theory, AIRR ARR-2026-72G1SSCNNG8YDVC2 (2026).



                                                     6
```

---

## Page 7

```text
[5] L. Eriksson, The Eriksson Programme (Yang–Mills): Machine-Checked Lattice Gauge Foundations,
    Certified Obstructions, and the Open Frontier, AIRR ARR-2026-7DYZAEKGJP8FPTJ1 (2026), and https:
    //github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.




                                                 7
```
