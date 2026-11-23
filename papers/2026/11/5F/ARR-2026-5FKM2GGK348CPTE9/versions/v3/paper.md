# A Wronskian Identity for Antisymmetrized Sine Sums: unconditional denominator positivity via circular convolution, sharp monotonicity distinctions, and counterexamples to naive sine-series principles

> Machine-readable rendition extracted from the hash-identified canonical PDF (`paper.pdf`). Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
A Wronskian Identity for Antisymmetrized Sine Sums:
             unconditional denominator positivity via circular convolution,
    sharp monotonicity distinctions, and counterexamples to naive sine-series principles

                                               Lluis Eriksson

                                          23 November 2026 (v3)


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
      from a companion two-dimensional lattice gauge theory surface-positivity problem, we prove
      unconditionally for every 𝛽 > 0 that 𝐹𝐵 (𝑡) = −(𝑓 *4 )′ (𝑡)/(2𝐼1 (𝛽)4 ) > 0 on (0, 𝜋), where
      𝑓 (𝑡) = 𝑒𝛽 cos 𝑡 and 𝑓 *4 is its fourfold normalized circular convolution (Theorem 5). We sepa-
      rate precisely between: (a) strict decrease of the real-analytic ratio 𝐹𝐴 /𝐹𝐵 on (0, 𝜋) (equivalent
      to 𝑊 ≤ 0 and 𝑊 ̸≡ 0), (b) strict pointwise negativity 𝑊 (𝑡) < 0 on (0, 𝜋) (strictly stronger,
      as shown by 𝐹𝑏 = sin 𝑡, 𝐹𝑎 = 41 sin 2𝑡 + 18 sin 4𝑡 with 𝐹𝑎 /𝐹𝑏 = cos3 𝑡 and 𝑊 (𝜋/2) = 0), and
      (c) local negativity near 𝑡 = 𝜋 (implied by (a) in the real-analytic Bessel family, but strictly
      weaker under generic side conditions, as shown by 𝑎 = (6, 10, 24), 𝑏 = (6, 5, 2)). We also
      prove nonmonotonicity of 𝐹𝑎 /𝐹𝑏 for 𝑎 √     = (3, 4, 3), 𝑏 = (3, 2, 1) via two explicit opposite signs
      (𝑊 (𝜋/2) = −32 < 0 and 𝑊 (2𝜋/3) = 3 3 > 0), refuting any unrestricted sine-series analogue
      of the Biernacki–Krzyż principle even when 𝑏𝑚 > 0 decreases, 𝑎𝑚 /𝑏𝑚 strictly increases on
      the support, and 𝐹𝑏 > 0 on (0, 𝜋). The finite Wronskian identity (arbitrary 𝐾) is machine-
      checked in Lean 4/Mathlib (WronskianIdentity.lean, release yang-mills-archive-v1.0,
      commit 6b54eca695e96b3038ceda18276c4e28fb45983f), and every counterexample is an ex-
      act algebraic evaluation. The global Bessel sign conjecture remains open.


1     The Wronskian identity
Theorem 1 (Wronskian identity). Let (𝑎𝑚 )𝑚≥1 and (𝑏𝑚 )𝑚≥1 be real sequences satisfying
        𝑚(|𝑎𝑚 | + |𝑏𝑚 |) < ∞ (in particular, any finitely supported sequences). Set 𝐹𝑎 (𝑡) =
∑︀
∑︀𝑚≥1
           sin(𝑚𝑡) and 𝐹𝑏 (𝑡) = 𝑚≥1 𝑏𝑚 sin(𝑚𝑡). Then 𝐹𝑎 , 𝐹𝑏 ∈ 𝐶 1 (R) with termwise derivatives
                               ∑︀
   𝑚≥1 𝑎𝑚∑︀
𝐹𝑎′ (𝑡) = 𝑚≥1 𝑚𝑎𝑚 cos(𝑚𝑡) and 𝐹𝑏′ (𝑡) = 𝑚≥1 𝑚𝑏𝑚 cos(𝑚𝑡), the double series below converges
                                          ∑︀

absolutely and uniformly on R, and for all 𝑡 ∈ R,

      (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) (𝑚 − 𝑛) sin((𝑚 + 𝑛)𝑡) + (𝑚 + 𝑛) sin((𝑛 − 𝑚)𝑡) = 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
 ∑︁                    [︀                                                     ]︀    [︀                          ]︀

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
                                         [︀                                                            ]︀
                                   = 2 𝑚 cos(𝑚𝑡) sin(𝑛𝑡) − 𝑛 sin(𝑚𝑡) cos(𝑛𝑡) =: 2 𝐺(𝑚, 𝑛).

Note that |𝐺(𝑚, 𝑛)| ≤ 𝑚 + 𝑛, 𝐺(𝑛, 𝑚) = −𝐺(𝑚, 𝑛), and 𝐺(𝑛, 𝑛) = 0. Moreover,
            ∑︁                         (︁ ∑︁                )︁(︁ ∑︁      )︁     (︁ ∑︁             )︁(︁ ∑︁         )︁
                  |𝑎𝑚 𝑏𝑛 | (𝑚 + 𝑛) =            𝑚|𝑎𝑚 |                |𝑏𝑛 | +             |𝑎𝑚 |             𝑛|𝑏𝑛 | < ∞,
          𝑚,𝑛≥1                         𝑚≥1                    𝑛≥1               𝑚≥1                 𝑛≥1

so every double sum below is absolutely convergent and may be rearranged freely by Fubini’s
theorem. Using the joint antisymmetry of (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) and 𝐺(𝑚, 𝑛) together with 𝐺(𝑛, 𝑛) = 0,
       ∑︁                                          ∑︁                                                  ∑︁
            (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) 2𝐺(𝑚, 𝑛) =                  (𝑎𝑚 𝑏𝑛 − 𝑎𝑛 𝑏𝑚 ) 𝐺(𝑚, 𝑛) = 2                            𝑎𝑚 𝑏𝑛 𝐺(𝑚, 𝑛)
     1≤𝑚<𝑛                                      𝑚,𝑛≥1                                                 𝑚,𝑛≥1
                                                  [︁(︁ ∑︁                       )︁(︁ ∑︁                     )︁
                                              =2              𝑚𝑎𝑚 cos(𝑚𝑡)                      𝑏𝑛 sin(𝑛𝑡)
                                                        𝑚≥1                        𝑛≥1
                                                            (︁ ∑︁                  )︁(︁ ∑︁                        )︁]︁
                                                        −             𝑎𝑚 sin(𝑚𝑡)                 𝑛𝑏𝑛 cos(𝑛𝑡)
                                                              𝑚≥1                         𝑛≥1
                                              = 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
                                                 [︀                            ]︀


Remark 2. Throughout this paper we define the scaled Wronskian with the factor of 2 matching
the right-hand side of (1):

                                  𝑊 (𝑡) := 2 𝐹𝑎′ (𝑡)𝐹𝑏 (𝑡) − 𝐹𝑎 (𝑡)𝐹𝑏′ (𝑡) .
                                                   [︀                                     ]︀

                                                                 𝑑
Wherever 𝐹𝑏 (𝑡) ̸= 0, the quotient rule gives 𝑊 (𝑡) = 2 𝐹𝑏 (𝑡)2 𝑑𝑡
                                                                                     (︀                     )︀
                                                                   𝐹𝑎 (𝑡)/𝐹𝑏 (𝑡) . Thus on any open
interval 𝐼 where 𝐹𝑏 ̸= 0, pointwise strict negativity 𝑊 (𝑡) < 0 on 𝐼 is equivalent to (𝐹𝑎 /𝐹𝑏 )′ (𝑡) < 0
on 𝐼, which is strictly stronger than strict decrease of 𝐹𝑎 /𝐹𝑏 on 𝐼 (see Proposition 6).


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
    𝐴𝑘 = 𝑟𝑘−1                (𝑗 + 1)𝑟𝑗2 ,                  4
                                                   𝐵𝑘 = 𝑘 𝑟𝑘−1 =𝑘                     ,            𝑐𝑚𝑛 = 𝐴𝑚 𝐵𝑛 − 𝐴𝑛 𝐵𝑚 .
               𝑗∈{𝑘−2, 𝑘}, 𝑗≥0
                                                                              𝐼1 (𝛽)4

Lemma 3 (Non-asymptotic super-exponential decay). For every 𝛽 > 0 and every integer 𝑘 ≥ 0,
                                                               (𝛽/2)𝑘
                                         0 < 𝐼𝑘 (𝛽) ≤                 𝐼0 (𝛽).
                                                                 𝑘!
Consequently, for every integer 𝑘 ≥ 1,
                                                        𝐼𝑘 (𝛽)   𝐼0 (𝛽) (𝛽/2)𝑘
                                   0 < 𝑟𝑘−1 =                  ≤               .
                                                        𝐼1 (𝛽)   𝐼1 (𝛽) 𝑘!

                                                               2
```

---

## Page 3

```text
In particular, for each fixed 𝛽 > 0,

                                          (𝛽/2)𝑚 4                                 (𝛽/2)𝑚 4
                            (︃       [︂             ]︂ )︃                      (︃     [︂        ]︂ )︃
                                 3
            𝐴𝑚 = 𝑂𝛽 𝑚                              ,              𝐵𝑚 = 𝑂𝛽        𝑚                       (𝑚 → ∞),
                                            𝑚!                                       𝑚!

so 𝑚≥1 𝑚𝑟 (𝐴𝑚 + 𝐵𝑚 ) < ∞ for every 𝑟 ≥ 0 (in particular 𝑟 = 1). Moreover, 𝐹𝐴 and 𝐹𝐵 extend
   ∑︀

to entire (hence real-analytic on R) 2𝜋-periodic odd functions.

                          = (𝑘+𝑗)!
               (︀𝑘+𝑗 )︀
Proof. Since      𝑗          𝑘! 𝑗! ≥ 1 for all 𝑘, 𝑗 ≥ 0, we have (𝑘 + 𝑗)! ≥ 𝑘! 𝑗!, whence

                                      ∞                     ∞
                                      ∑︁ (𝛽/2)𝑘+2𝑗   (𝛽/2)𝑘 ∑︁ (𝛽/2)2𝑗   (𝛽/2)𝑘
                          𝐼𝑘 (𝛽) =                 ≤                   =        𝐼0 (𝛽).
                                   𝑗=0
                                       𝑗! (𝑘 + 𝑗)!     𝑘! 𝑗=0 (𝑗!)2        𝑘!

Positivity follows termwise for 𝛽 > 0. For 𝑚 ≥ 1, 𝐵𝑚 = 𝑚𝑟𝑚−1       4    immediately gives 𝐵𝑚 =
             𝑚     4
𝑂𝛽 (𝑚[(𝛽/2) /𝑚!] ). For 𝐴𝑚 with 𝑚 ≥ 2, using (𝛽/2)          𝑚−1 /(𝑚 − 1)! = (2𝑚/𝛽) (𝛽/2)𝑚 /𝑚!
        2             2      𝑚    2         2          −2      𝑚
gives 𝑟𝑚−2 = 𝑂𝛽 (𝑚 [(𝛽/2) /𝑚!] ) while 𝑟𝑚 = 𝑂𝛽 (𝑚 [(𝛽/2) /𝑚!]2 ), so (𝑚 − 1)𝑟𝑚−2    2    + (𝑚 +
    2          3       𝑚    2                      2                        3    𝑚
1)𝑟𝑚 = 𝑂𝛽 (𝑚 [(𝛽/2) /𝑚!] ) and multiplying by 𝑟𝑚−1 yields 𝐴𝑚 = 𝑂𝛽 (𝑚 [(𝛽/2) /𝑚!]4 ). Since
| sin(𝑚𝑧)| ≤ 𝑒𝑚| Im 𝑧| on C and 𝑚3 [(𝛽/2)𝑚 /𝑚!]4 decays faster than 𝑒−𝑅𝑚 for every 𝑅 > 0, both
series converge locally uniformly on C to entire 2𝜋-periodic odd functions.

    We now prove unconditionally that 𝐹𝐵 (𝑡) > 0 on (0, 𝜋) for every 𝛽 > 0.

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
(𝑔 * ℎ)(𝑡) = 2𝜋   −𝜋 𝑔(𝑡 − 𝑢) ℎ(𝑢) 𝑑𝑢, differentiate under the integral sign, and change variables back
to 𝑠 = 𝑡 − 𝑢:
                                          ∫︁ 𝜋                                 ∫︁ 𝜋
                                  1                                        1
             (𝑔 * ℎ)′ (𝑡) =                      𝑔 ′ (𝑠) ℎ(𝑡 − 𝑠) 𝑑𝑠 =                𝑔 ′ (𝑠) ℎ(𝑡 − 𝑠) − ℎ(𝑡 + 𝑠) 𝑑𝑠,
                                                                                           [︀                   ]︀
                                 2𝜋        −𝜋                             2𝜋    0

using 𝑔 ′ (−𝑠) = −𝑔 ′ (𝑠) because 𝑔 is even. Because ℎ is 2𝜋-periodic, even, and strictly decreasing
on [0, 𝜋], there is a strictly increasing function ℎ̃ : [−1, 1] → R such that ℎ(𝜃) = ℎ̃(cos 𝜃) for all
𝜃 ∈ R. For any 𝑡, 𝑠 ∈ (0, 𝜋),

                                           cos(𝑡 − 𝑠) − cos(𝑡 + 𝑠) = 2 sin 𝑡 sin 𝑠 > 0,

so ℎ(𝑡 − 𝑠) − ℎ(𝑡 + 𝑠) = ℎ̃(cos(𝑡 − 𝑠)) − ℎ̃(cos(𝑡 + 𝑠)) > 0. Together with 𝑔 ′ (𝑠) < 0 on (0, 𝜋), the
integrand is strictly negative on all of (0, 𝜋), giving (𝑔 * ℎ)′ (𝑡) < 0.

Theorem 5 (Unconditional denominator positivity). For every 𝛽 > 0 and every 𝑡 ∈ (0, 𝜋),
                                                   ∞
                                                   ∑︁       𝐼𝑘 (𝛽)4             (𝑓 *4 )′ (𝑡)
                                 𝐹𝐵 (𝑡) =               𝑘           sin(𝑘𝑡) = −              > 0,
                                                  𝑘=1
                                                            𝐼1 (𝛽)4             2 𝐼1 (𝛽)4

where 𝑓 (𝑡) := 𝑒𝛽 cos 𝑡 and 𝑓 *4 := (𝑓 * 𝑓 ) * (𝑓 * 𝑓 ).

                                                                      3
```

---

## Page 4

```text
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
                          −(𝑓 *4 )′ (𝑡) = 2
                                              ∑︁
                                                    𝑘 𝐼𝑘 (𝛽)4 sin(𝑘𝑡) = 2 𝐼1 (𝛽)4 𝐹𝐵 (𝑡).
                                              𝑘=1

For 𝛽 > 0, 𝑓 ∈ 𝐶 ∞ (R) is 2𝜋-periodic, even, and satisfies 𝑓 ′ (𝑡) = −𝛽 sin 𝑡 𝑒𝛽 cos 𝑡 < 0 on (0, 𝜋).
Applying Lemma 4 to (𝑓, 𝑓 ) yields 𝑓 *2 even, 2𝜋-periodic, 𝐶 ∞ , and strictly decreasing on (0, 𝜋);
applying Lemma 4 once more to (𝑓 *2 , 𝑓 *2 ) gives (𝑓 *4 )′ (𝑡) < 0 on (0, 𝜋). Dividing by 2𝐼1 (𝛽)4 > 0
gives 𝐹𝐵 (𝑡) > 0 on (0, 𝜋).


3      Sharp monotonicity distinctions and the global conjecture
Let 𝑊 (𝑡) := 2[𝐹𝐴′ (𝑡)𝐹𝐵 (𝑡) − 𝐹𝐴 (𝑡)𝐹𝐵′ (𝑡)] be the Wronskian of Theorem 1 at (𝑎, 𝑏) = (𝐴, 𝐵). In
the companion note [4], the surface-positivity problem asks for 𝑊 (𝑡) < 0 in a punctured left
neighborhood of 𝑡 = 𝜋, and proves that the coefficient ratio 𝜙𝑚 = 𝐴𝑚 /𝐵𝑚 is strictly increasing
(𝑐𝑚𝑛 < 0 for all 𝑚 < 𝑛). By Theorem 5, 𝐹𝐴 /𝐹𝐵 is real-analytic and well-defined on all of (0, 𝜋),
with (𝐹𝐴 /𝐹𝐵 )′ = 𝑊/(2𝐹𝐵2 ).
    We clarify the exact implication structure among three candidate sign statements:
 (b) Pointwise global negativity: 𝑊 (𝑡) < 0 for all 𝑡 ∈ (0, 𝜋).

 (a) Weak global negativity / strict decrease: 𝑊 (𝑡) ≤ 0 for all 𝑡 ∈ (0, 𝜋) and 𝑊 ̸≡ 0 (equivalently,
     for real-analytic 𝐹𝐴 , 𝐹𝐵 with 𝐹𝐵 > 0, 𝐹𝐴 /𝐹𝐵 is strictly decreasing on (0, 𝜋)).

    (c) Near-𝜋 local negativity: there exists 𝛿 > 0 such that 𝑊 (𝑡) < 0 for all 𝑡 ∈ (𝜋 − 𝛿, 𝜋).
Clearly (b) =⇒ (a). Moreover, in the Bessel setting (where 𝑊 is entire by Lemma 3, hence
analytic across 𝑡 = 𝜋), if (a) holds then 𝑊 cannot vanish identically and its real zeros near 𝜋
are isolated, so (a) =⇒ (c) as well. Thus within the Bessel family we have the forward chain
(b) =⇒ (a) =⇒ (c). Under generic finite-support hypotheses (𝑏𝑚 > 0 decreasing, 𝑎𝑚 /𝑏𝑚
strictly increasing, 𝐹𝑏 > 0 on (0, 𝜋)), neither reverse implication holds: Proposition 6 shows
(a) ̸⇒ (b), and Proposition 9 shows (c) ̸⇒ (a). (These finite examples rule out generic reverse
implications, not Bessel-specific ones.)
Proposition 6 (Strict decrease allows isolated zeros of 𝑊 ). For 𝐹𝑏 (𝑡) = sin 𝑡 (positive on (0, 𝜋))
and 𝐹𝑎 (𝑡) = 41 sin(2𝑡) + 18 sin(4𝑡), we have

                                                    𝐹𝑎 (𝑡)
                                                           = cos3 𝑡,
                                                    𝐹𝑏 (𝑡)
which is strictly decreasing on (0, 𝜋), yet 𝑊 (𝑡) = 2 sin2 𝑡·(−3 cos2 𝑡 sin 𝑡) = −6 sin3 𝑡 cos2 𝑡 vanishes
at 𝑡 = 𝜋/2. In general, for real-analytic 𝐹𝐴 , 𝐹𝐵 with 𝐹𝐵 > 0 on (0, 𝜋), strict decrease of 𝐹𝐴 /𝐹𝐵
on (0, 𝜋) is equivalent to 𝑊 (𝑡) ≤ 0 on (0, 𝜋) with 𝑊 ̸≡ 0, whereas 𝑊 (𝑡) < 0 on all of (0, 𝜋) is the
strictly stronger assertion that (𝐹𝐴 /𝐹𝐵 )′ (𝑡) < 0 everywhere on (0, 𝜋).

                                                           4
```

---

## Page 5

```text
Proof. Using sin(2𝑡) = 2 sin 𝑡 cos 𝑡 and sin(4𝑡) = 4 sin 𝑡 cos 𝑡(2 cos2 𝑡 − 1),

                            𝐹𝑎 (𝑡)
                                   = 21 cos 𝑡 + 12 cos 𝑡(2 cos2 𝑡 − 1) = cos3 𝑡.
                            sin 𝑡
Hence (𝐹𝑎 /𝐹𝑏 )′ (𝑡) = −3 cos2 𝑡 sin 𝑡 ≤ 0 with unique zero at 𝑡 = 𝜋/2 in (0, 𝜋), so 𝐹𝑎 /𝐹𝑏 is strictly
decreasing while 𝑊 (𝜋/2) = 0. For real-analytic 𝐹𝐴 /𝐹𝐵 on the connected interval (0, 𝜋), if 𝑊 ≤ 0
and 𝑊 ̸≡ 0 then the zeros of (𝐹𝐴 /𝐹𝐵 )′ are isolated, so 𝐹𝐴 /𝐹𝐵 is strictly decreasing; conversely,
strict decrease forces (𝐹𝐴 /𝐹𝐵 )′ ≤ 0 and (𝐹𝐴 /𝐹𝐵 )′ ̸≡ 0.

Conjecture 7 (Global Wronskian negativity for the Bessel arrays). For every 𝛽 > 0:

 (a) (Weak/strict-decrease form) 𝑊 (𝑡) ≤ 0 for all 𝑡 ∈ (0, 𝜋) and 𝑊 ̸≡ 0 (equivalently, by Theo-
     rem 5 and real-analyticity, 𝐹𝐴 /𝐹𝐵 is strictly decreasing on (0, 𝜋)).

 (b) (Strong/pointwise form) 𝑊 (𝑡) < 0 for all 𝑡 ∈ (0, 𝜋) (equivalently, (𝐹𝐴 /𝐹𝐵 )′ (𝑡) < 0 every-
     where on (0, 𝜋)).


4    Counterexamples to naive sine-series monotonicity and local-
     to-global lifting
For power series with positive coefficients converging on a common interval (0, 𝑅) with nonvanish-
ing denominator, the Biernacki–Krzyż principle [1] asserts that monotonicity of 𝑎𝑚 /𝑏𝑚 transfers
to monotonicity of 𝑎𝑚 𝑥𝑚 / 𝑏𝑚 𝑥𝑚 . No unrestricted analogue holds for sine series in either di-
                      ∑︀        ∑︀

rection of monotonicity, even on finite supports where 𝑏𝑚 > 0 decreases, 𝑎𝑚 /𝑏𝑚 strictly increases
on {1, . . . , 𝐾}, and 𝐹𝑏 > 0 on (0, 𝜋).

Proposition 8 (Counterexample to unrestricted sine-series Biernacki–Krzyż). Let 𝑎 = (3, 4, 3)
and 𝑏 = (3, 2, 1) on indices 𝑚 ∈ {1, 2, 3} (with 𝑎𝑚 = 𝑏𝑚 = 0 for 𝑚 ≥ 4). On the support {1, 2, 3},
𝑏𝑚 is strictly decreasing and the coefficient ratio 𝑎𝑚 /𝑏𝑚 = (1, 2, 3) is strictly increasing; moreover

        𝐹𝑏 (𝑡) = 3 sin 𝑡 + 2 sin 2𝑡 + sin 3𝑡 = 2 sin 𝑡 (2 cos2 𝑡 + 2 cos 𝑡 + 1) > 0       ∀𝑡 ∈ (0, 𝜋),

since 2𝑦 2 + 2𝑦 + 1 = 2(𝑦 + 21 )2 + 12 > 0. Nevertheless,
                                                                        √
                       𝑊 (𝜋/2) = −32 < 0           and      𝑊 (2𝜋/3) = 3 3 > 0,

so 𝐹𝑎 /𝐹𝑏 is strictly decreasing at 𝑡 = 𝜋/2 and strictly increasing at 𝑡 = 2𝜋/3, hence non-monotone
on (0, 𝜋).

Proof. At 𝑡 = 𝜋/2: sin 𝑡 = 1, sin 2𝑡 = 0, sin 3𝑡 = −1, cos 𝑡 = 0, cos 2𝑡 = −1, cos 3𝑡 = 0, so
𝐹𝑎 (𝜋/2) = 3 − 3 = 0, 𝐹𝑏 (𝜋/2) = 3 − 1 = 2, 𝐹𝑎′ (𝜋/2) = −8,
                                                        √
                                                            and 𝐹𝑏′ (𝜋/2)
                                                                       √
                                                                          = −4, giving 𝑊 (𝜋/2) =
                                                          3              3
2[(−8) · 2 − 0 · (−4)] = −32 < 0. At 𝑡 = 2𝜋/3: sin 𝑡 = 2 , sin 2𝑡 = − 2 , sin 3𝑡 = 0, cos 𝑡 = − 21 ,
                                            √        √                   √     √
cos 2𝑡 = − 12 , cos 3𝑡 = 1, so 𝐹𝑎 = (3 − 4) 23 = − 23 , 𝐹𝑏 = (3 − 2) 23 =           3   ′   − 23 − 4 + 9 = 27 ,
                                                                √                  2 , 𝐹𝑎 = √
and 𝐹𝑏′ = − 32 − 2 + 3 = − 12 , giving 𝐹𝑎′ 𝐹𝑏 − 𝐹𝑎 𝐹𝑏′ =       3 3
                                                                and 𝑊 (2𝜋/3) = 3 3 > 0. (Mere
                                                                2
coefficient decrease does not in general force sine positivity, e.g. sin 𝑡 + sin 2𝑡 < 0 near 𝜋; see [2]
for Vietoris-type criteria, which is why we verify 𝐹𝑏 > 0 directly by factorization.)




                                                     5
```

---

## Page 6

```text
Proposition 9 (Near-𝜋 negativity does not force global negativity). Let 𝑎 = (6, 10, 24) and
𝑏 = (6, 5, 2) on indices 𝑚 ∈ {1, 2, 3} (zero for 𝑚 ≥ 4). Then on {1, 2, 3}, 𝑏𝑚 is strictly decreasing,
𝑎𝑚 /𝑏𝑚 = (1, 2, 12) is strictly increasing, and

        𝐹𝑏 (𝑡) = 6 sin 𝑡 + 5 sin 2𝑡 + 2 sin 3𝑡 = sin 𝑡 (8 cos2 𝑡 + 10 cos 𝑡 + 4) > 0   ∀𝑡 ∈ (0, 𝜋),

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
                 √                  √                                                   √
and 𝐹𝑏 (2𝜋/3) = ( 3/2)(2−5+4) = 3/2, giving 𝑊 (2𝜋/3) = 2· 34 · 4(−17)      · − 23 = 51 3 > 0.
                                                                            (︀    )︀
                                                                      12

Remark 10 (Structural moral and empirical numerical-precision heuristic). Propositions 8 and 9
show that coefficient-ratio monotonicity and denominator positivity alone cannot certify the sign
of 𝑊 , nor lift local near-𝜋 negativity to (0, 𝜋). As an empirical numerical diagnostic (archived
in docs/BF2-ATTACK-NOTES.md, not part of any proof), high-precision evaluations of the Bessel
arrays at large 𝛽 exhibit severe cancellation between even- and odd-index contributions: on sam-
pled grids, |𝑊 (𝑡)| reaches ∼ 2.9 · 10−8 at 𝛽 = 8 and ∼ 5.0 · 10−29 at 𝛽 = 32 while individual
partial sums remain of order 1. Accordingly, using ≥ 2.2𝛽 + 20 decimal working digits is a con-
servative empirical heuristic for numerical exploration, not a proven error bound. Analytically,
Theorem 5 already realizes 𝐹𝐵 as an exact circle-convolution derivative; a corresponding positive
kernel representation of −𝑊 (or total positivity of (𝐴; 𝐵) against the sine kernel) remains the
natural analytic route to Conjecture 7.


5    Verification and Reproducibility
The analytic proofs of Theorems 1 and 5, Lemmas 3 and 4, and Propositions 6, 8, and 9 are
completely self-contained and verifiable by hand from this document.
    In addition, the finite form of Theorem 1 (arbitrary 𝐾) is machine-checked in Lean 4 / Math-
lib in papers/wronskian-reduction/WronskianIdentity.lean inside https://github.com
/lluiseriksson/THE-ERIKSSON-PROGRAMME at archival release yang-mills-archive-v1.0
(commit 6b54eca695e96b3038ceda18276c4e28fb45983f, Lean v4.29.0-rc6, pinned Math-
lib 07642720480157414db592fa85b626dafb71355b): declarations bracket_eq_two_G, double_-
sum_eq_wronskian, pair_sum_eq_double_sum, and wronskian_identity, reporting zero sorry
and axiom readout [propext, Classical.choice, Quot.sound] (checked locally as a stan-
dalone Lean file outside YangMillsCore). As supplementary diagnostics (not proofs), Theorem 1
and Propositions 6, 8, and 9 were symbolically cross-checked in SymPy, and the convolution
identity in Theorem 5 was checked against 30-digit numerical quadrature at 𝛽 ∈ {0.5, 2.0}.

                                                      6
```

---

## Page 7

```text
Scope and Disclosure
Conjecture 7 remains open, and no claim is made regarding four-dimensional gauge theory or a
Yang–Mills mass gap. Large language models assisted manuscript preparation under author su-
pervision; author Lluis Eriksson administers AIRR (https://airr.science/), so no independent
editorial admission or peer review is claimed.


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

[5] L. Eriksson, The Eriksson Programme (Yang–Mills): Auditable Claim-to-Theorem Manifest, Certified
    Obstructions, and Continuation Frontier, AIRR ARR-2026-7DYZAEKGJP8FPTJ1 (2026), and https:
    //github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.




                                                     7
```
