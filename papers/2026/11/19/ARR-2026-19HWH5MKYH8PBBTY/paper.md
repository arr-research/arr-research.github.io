# Exact Modular Obstruction Sieves, Direct F_2[X] Kernel-Orbit Factorizations, and Certified Power-Substitution Towers for Binary Irreducible Trinomials

> Machine-readable rendition extracted from the hash-identified canonical PDF. Mathematical typography may be degraded; cite and verify against `paper.pdf`.

## Page 1

```text
AIRR:ARR-2026-19HWH5MKYH8PBBTY | v1 | 2026-11-27
Exact Modular Obstruction Sieves, Direct F2[X]
Kernel-Orbit Factorizations, and Certified
Power-Substitution Towers for Binary Irreducible
Trinomials
Lluis Eriksson
Independent Researcher, AIRR.SCIENCE
lluiseriksson@gmail.com
November 27, 2026
Abstract
Extending the elliptic-curve irreducibility criterion of Fu, Li, and Zuo (arXiv:2611.34282v1)
for the binary trinomial family Tk(X) = X (4k +2)/3 + X + 1 ∈ F2[X] (k ∈ Z≥1, Mk = 4k + 3,
mk = (4k + 2)/3), we establish four constructive algebraic, number-theoretic, and machine-
checked results. First, we prove unconditionally in Lean 4.36.0 (20 theorems, 0 sorry, 0
Classical.choice) the exact arithmetic structure governing the k = 1 exception versus
k ≥ 2: 3mk + 1 = Mk, Mk ≡ 1 (mod 6), mk ≡ 2 (mod 4), and for every k ≥ 2 both
Mk ≡ 3 (mod 16) (forcing quadratic non-residuacity of 2) and mk ≡ 6 (mod 8) (passing
Swan’s parity filter), together with the Eisenstein norm identity Mk = (2k)2 + 3 · 12 and
exact collapse lcm(o, 6) = o whenever 6 | o. Second, we construct explicit infinite modular
obstruction families proving 7 | M3t+1 (composite for all t ≥ 1), 13 | M6t+5 (composite for
all t ≥ 0), and 19 | M9t+2 (composite for all t ≥ 1), establishing exact rational covering
densities of 1/2 on Z/6Z from {7, 13}, 5/9 on Z/18Z from {7, 13, 19, 37}, and 53/90 on Z/90Z
from {7, 13, 19, 37, 61}. Third, an AST-audited zero-float bit-packed F2[X] and deterministic
Lucas-certificate verifier issues 16 SHA-256 certificates (C01--C16): exact direct F2[X]
distinct-degree factorizations match the elliptic-curve kernel-orbit partition on composite
moduli (T4 splits cleanly as 2 + 12 + 72 = 86 for M4 = 7 · 37 and T5 as 4 + 26 + 312 = 342
for M5 = 13 · 79), deterministic Lucas primality and primitive-root certificates establish
irreducibility of Tk up to degree m15 = 357,913,942 (M15 = 1,073,741,827), and direct Rabin
tests certify single- and two-prime power-substitution towers up to degree 147.
1 Introduction and Problem Formulation
Sparse irreducible polynomials over F2 are central to finite-field arithmetic, coding theory, and
cryptography [3, 5, 6]. Recently, Fu, Li, and Zuo [1] established a remarkable elliptic-curve
characterization for the exponentially growing trinomial family
Tk(X) = X mk + X + 1 ∈ F2[X], mk = 4k + 2 3 , Mk = 4k + 3 (k ∈ Z≥1). (1)
By identifying the roots of Tk with automorphism orbits on the cyclic Mk-torsion kernels K± of
the supersingular curve E : y2 + y = x3 over F2, their Main Theorem A proves that for every
k ≥ 1, Tk is irreducible over F2 if and only if Mk is prime and lcm(ordMk (2), 6) = Mk − 1; their
Corollary 1.1 sharpens this for k ≥ 2 to requiring Mk prime and 2 a primitive root modulo Mk.
They further apply the classical composition criterion (Main Theorem B) to construct infinite
families of irreducible trinomials X Dt + X Rt + 1 in fixed reduced exponent classes.
In this work, we provide four machine-checked structural and computational extensions of [1]:
1
```

---

## Page 2

```text
1. Constructive arithmetic invariants for the k = 1 vs. k ≥ 2 boundary: We prove in
Lean 4.36.0 (T01--T08, T16) the exact divisibility 3mk + 1 = Mk, the congruences Mk ≡ 1
(mod 6), mk ≡ 2 (mod 4), and for all k ≥ 2 both Mk ≡ 3 (mod 16) and mk ≡ 6 (mod 8),
along with the exact Eisenstein norm identity Mk = (2k)2 + 3 · 12 and exact lcm collapse
under 6 | o.
2. Unconditional infinite modular obstruction sieves: We prove in Lean 4.36.0
(T09--T15) infinite families of provably composite Mk (7 | M3t+1, 13 | M6t+5, 19 | M9t+2)
and exact rational covering densities eliminating 1/2 of all k ≥ 4 via {7, 13}, 5/9 via
{7, 13, 19, 37} (noting the exact overlap 4 ≡ 1 (mod 3) where 37’s residue is already covered
by 7), and 53/90 via {7, 13, 19, 37, 61} (C11--C13).
3. Direct F2[X] kernel-orbit factorization and massive-degree Lucas certificates: Us-
ing an AST-audited zero-float bit-packed F2[X] engine, we independently verify irreducibil-
ity of T1, T2, T3 (C01--C03), compute exact distinct-degree factorizations of composite T4
(2 + 12 + 72 = 86, C04) and T5 (4 + 26 + 312 = 342, C05) matching the kernel-orbit partition∑
1<d|Mk φ(d)/3 = mk, and issue deterministic Lucas primality and primitive-root certificates
proving irreducibility of T6, T8, T9, T14, T15 up to degree m15 = 357,913,942 (C06--C10).
4. Rabin-certified power-substitution towers: We verify reduced-class invariance in Lean 4
(T20) and directly certify single-prime and two-prime substitution towers from seeds X 2 +
X + 1, X 3 + X + 1, and X 6 + X + 1 via exact Rabin irreducibility tests (C14--C16).
2 Universal Congruences, Reciprocity Reduction, and Modular
Sieves
Theorem 2.1 (Arithmetic Invariants and Exact Reciprocity Preconditions; Lean T01--T08, T16).
For every integer k ≥ 1, set mk = (4k + 2)/3 and Mk = 4k + 3. Then:
1. 3 | (4k + 2), 3mk + 1 = Mk, Mk ≡ 1 (mod 6), mk ≡ 2 (mod 4), and Mk = (2k)2 + 3 · 12.
2. For every k ≥ 2, Mk ≡ 3 (mod 16) (hence Mk ≡ 3 (mod 8)) and mk ≡ 6 (mod 8).
3. For any integer o ≥ 1 with 6 | o, lcm(o, 6) = o.
Proof. Since 4 ≡ 1 (mod 3), induction yields 4k ≡ 1 (mod 3), giving 3mk = 4k +2 and 3mk +1 =
Mk. For k ≥ 1, 4k ≡ 4 (mod 6) implies Mk ≡ 1 (mod 6), and 3mk = 4k + 2 ≡ 2 (mod 4) implies
mk ≡ 2 (mod 4) (so T ′ k(X) = 1 in F2[X], proving Tk is always squarefree). For k ≥ 2, 16 | 4k
gives Mk ≡ 3 (mod 16) and 3mk ≡ 2 (mod 16), whence mk ≡ 6 (mod 8). Finally, 4k = (2k)2
gives Mk = (2k)2 + 3, and 6 | o implies gcd(o, 6) = 6 so lcm(o, 6) = o · 6/6 = o. All statements
are machine-checked in Lean 4.36.0 (T01--T08, T16).
Remark 2.2 (Elementary Mechanism Behind Corollary 1.1 of [1]). When Mk is prime and k ≥ 2,
Theorem 2.1(2) gives Mk ≡ 3 (mod 8), so quadratic reciprocity yields
(
2
Mk
)
= −1 and hence
2 | ordMk (2) (in contrast to k = 1, where M1 = 7 ≡ 7 (mod 8),
( 2
7
)
= +1, and ord7(2) = 3).
Simultaneously, by Gauss–Euler’s classical cubic residuacity criterion [2], 2 is a cubic residue
modulo a prime p ≡ 1 (mod 3) if and only if p = L2 + 27N 2 for integers L, N . Because the
representation p = a2 + 3b2 (a, b > 0) of a prime p ≡ 1 (mod 3) is unique and Theorem 2.1(1)
exhibits Mk = (2k)2 + 3 · 12 with b = 1 ̸≡ 0 (mod 3), 2 is never a cubic residue modulo any
prime Mk, forcing 3 | ordMk (2). Combining 2 | ordMk (2) and 3 | ordMk (2) gives 6 | ordMk (2), so
Theorem 2.1(3) collapses lcm(ordMk (2), 6) = ordMk (2) for all k ≥ 2.
Theorem 2.3 (Infinite Modular Obstruction Sieves; Lean T09--T15). For every integer t ≥ 0:
7 | M3t+1, 13 | M6t+5, 19 | M9t+2. (2)
2
```

---

## Page 3

```text
Figure 1: Left: Landscape of Tk(X) for 1 ≤ k ≤ 20 showing all 8 Lucas-certified irreducible
prime indices k ∈ {1, 2, 3, 6, 8, 9, 14, 15} (blue, marked P) up to degree m15 = 357,913,942, versus
12 composite moduli (red). Right: Exact bit-packed F2[X] distinct-degree factorizations of T4
(C04: 2 + 12 + 72 = 86) and T5 (C05: 4 + 26 + 312 = 342), matching the exact kernel-orbit
partition ∑ 1<d|Mk φ(d)/3 = mk.
In particular, M3t+1 is strictly composite for all t ≥ 1 (k ≥ 4), M6t+5 is strictly composite for
all t ≥ 0 (k ≥ 5), and M9t+2 is strictly composite for all t ≥ 1 (k ≥ 11). Consequently, among
integers k ≥ 4, the primes {7, 13} unconditionally eliminate 3/6 = 1/2 of all indices (k ≡ 1, 4, 5
(mod 6)), the primes {7, 13, 19, 37} eliminate exactly 10/18 = 5/9 of all indices on Z/18Z, and
adjoining 61 (k ≡ 18 (mod 30)) eliminates exactly 53/90 on Z/90Z.
Proof. Since 43 = 64 ≡ 1 (mod 7), 46 = 4096 ≡ 1 (mod 13), and 49 = 262,144 ≡ 1 (mod 19),
base cases M1 = 7, M5 = 1027 = 13 · 79, and M2 = 19 propagate inductively to (2) (Lean
T09--T11). Strict monotonicity of 4k gives M3t+1 ≥ M4 = 259 > 7 for t ≥ 1 and M6t+5 ≥ M5 =
1027 > 13 for t ≥ 0 (Lean T12--T13). Exhaustive evaluation on Z/6Z and Z/18Z establishes the
exact counts 3/6 = 1/2 and 10/18 = 5/9 (Lean T14--T15); notice that 37 | M18t+4 contributes
0 new residues because 4 ≡ 1 (mod 3) is already blocked by 7, and 19’s residue 11 (mod 18) is
already blocked by 13, leaving 8 surviving classes {0, 3, 6, 8, 9, 12, 14, 15} (mod 18) (which indeed
contain every prime Mk for 4 ≤ k ≤ 20: k ∈ {6, 8, 9, 14, 15}!). Adding 61 | M30t+18 lifts the exact
elimination count on Z/90Z from 50/90 to 53/90 (C13).
3 Exact F2[X] Kernel-Orbit Factorizations and Massive-Degree
Certificates
For composite Mk = pq with distinct primes p, q ≡ 1 (mod 6), the cyclic torsion kernel K− ∼=
Z/MkZ decomposes by element order d ∈ {p, q, pq} into disjoint invariant sets of cardinalities
φ(p) = p−1, φ(q) = q−1, and φ(pq) = (p−1)(q−1). Quotienting by the 6-element automorphism
group U and doubling across S−⊔S+ under Frobenius [1] predicts that the roots of Tk(X) partition
into invariant subsets of exact sizes
p − 1
3 + q − 1 3 + (p − 1)(q − 1) 3 = pq − 1 3 = mk. (3)
Our zero-float bit-packed F2[X] distinct-degree factorization engine directly tests (3) without
invoking any elliptic-curve machinery:
3
```

---

## Page 4

```text
Figure 2: Left: Exact rational densities of composite Mk = 4k + 3 eliminated by modular
covering sieves (C11--C13): 1/3 from {7}, 1/2 from {7, 13}, 5/9 from {7, 13, 19, 37}, and 53/90
from {7, 13, 19, 37, 61}. Right: Complete residue elimination map on Z/18Z showing the 10
blocked classes and 8 surviving classes (which contain every prime Mk in 4 ≤ k ≤ 20).
• For k = 4 (m4 = 86, M4 = 259 = 7 · 37, C04): direct F2[X] DDF yields exactly three
irreducible factors of degrees 2, 12, and 72, matching (7 − 1)/3 = 2, (37 − 1)/3 = 12, and
6 · 36/3 = 72 (2 + 12 + 72 = 86, Lean T18).
• For k = 5 (m5 = 342, M5 = 1027 = 13 · 79, C05): direct F2[X] DDF yields exactly three
irreducible factors of degrees 4, 26, and 312, matching (13 − 1)/3 = 4, (79 − 1)/3 = 26, and
12 · 78/3 = 312 (4 + 26 + 312 = 342, Lean T18).
For larger indices k ∈ {6, 8, 9, 14, 15}, direct F2[X] Rabin testing of degree m15 ≈ 3.58 × 108
is computationally prohibitive, whereas Fu–Li–Zuo’s criterion reduces irreducibility to a deter-
ministic Lucas primality and primitive-root certificate on Mk = 4k + 3: given the complete prime
factorization Mk − 1 = ∏ i qei i (each qi deterministically verified prime), certifying 2Mk −1 ≡ 1
(mod Mk) and 2(Mk −1)/qi ̸≡ 1 (mod Mk) for every qi | (Mk − 1) simultaneously proves that Mk is
prime and that ordMk (2) = Mk − 1. Certificates C06--C10 execute this deterministic verification
in milliseconds for all five primes M6 = 4099, M8 = 65,539, M9 = 262,147, M14 = 268,435,459,
and M15 = 1,073,741,827, certifying irreducibility of T15(X) = X 357,913,942 + X + 1 over F2
(conditional on [1, Main Theorem A]).
4 Certified Power-Substitution Towers over F2[X]
For an irreducible seed trinomial f (X) = X D + X R + 1 ∈ F2[X] with root multiplicative order
e | (2D − 1), the composition criterion ([1, Main Theorem B], [3]) guarantees that f (X t) =
X Dt + X Rt + 1 is irreducible over F2 for every odd integer t whose prime factors ℓ satisfy ℓ | e and
ℓ ∤ (2D − 1)/e, while preserving the reduced exponent class (D/ gcd(D, R), R/ gcd(D, R)) (proved
constructively in Lean T20). Certificates C14--C16 audit the exact order e, index (2D − 1)/e, and
direct Rabin irreducibility [4] across three towers:
• C14: Seed X 2 + X + 1 (e = 3, index 1, ℓ = 3): X 2·3s + X 3s + 1 certified irreducible for
s ∈ {0, 1, 2, 3} (degrees 2, 6, 18, 54).
• C15: Seed X 3 + X + 1 (e = 7, index 1, ℓ = 7): X 3·7s + X 7s + 1 certified irreducible for
s ∈ {0, 1, 2} (degrees 3, 21, 147).
• C16: Seed X 6 +X +1 (e = 63 = 32 ·7, index 1, ℓ ∈ {3, 7}): two-prime lattice X 6·3a7b +X 3a7b +1
certified irreducible across (a, b) ∈ {(0, 0), (1, 0), (0, 1), (2, 0), (1, 1)} (degrees 6, 18, 42, 54, 126).
4
```

---

## Page 5

```text
Figure 3: Left: Rabin-certified degrees along the single-prime power-substitution towers C14
(X 2·3s + X 3s + 1) and C15 (X 3·7s + X 7s + 1). Right: Rabin-certified degrees across the two-prime
substitution lattice C16 (X 6t + X t + 1, t = 3a7b, seed order e = 63).
5 Certificate Suite, Verification Boundary, and Reproducibility
Table 1 summarizes all 16 SHA-256 certificates generated by the AST-audited zero-float verifier
src/binary_trinomial_verifier.py and validated by 71 adversarial pytest checks alongside
20 Lean 4.36.0 theorems.
Table 1: Summary of the 16 canonical SHA-256 certificates (BINARY-TRINOMIAL-CERT-1.0).
IDs Mode Parameters Exact Certified Outcome
C01--C03 Dual F2[X] + Lucas k = 1, 2, 3 (m = 2, 6, 22) Prime Mk = 7, 19, 67; irred. (ord7(2) = 3)
C04 Direct F2[X] DDF k = 4, m4 = 86, M4 = 7 · 37 Factor degrees [2, 12, 72] (sum = 86)
C05 Direct F2[X] DDF k = 5, m5 = 342, M5 = 13 · 79 Factor degrees [4, 26, 312] (sum = 342)
C06--C08 Deterministic Lucas k = 6, 8, 9 (M = 4099, 65539, 262147) Prime Mk , ordMk (2) = Mk − 1 (Tk irred.)
C09--C10 Deterministic Lucas k = 14, 15 (m15 = 357,913,942) Prime Mk , ordMk (2) = Mk − 1 (Tk irred.)
C11--C13 Modular Sieve {7, 13}, {7, 13, 19, 37}, +{61} Eliminated densities 1/2, 5/9, 53/90
C14--C15 Single-Prime Tower Seeds (2, 1) ℓ = 3; (3, 1) ℓ = 7 Rabin-certified degs 2..54 and 3..147
C16 Two-Prime Lattice Seed (6, 1), e = 63, ℓ ∈ {3, 7} Rabin-certified degs 6, 18, 42, 54, 126
Explicit Verification Boundary. To maintain strict separation of trust boundaries, our ver-
ification is partitioned into three disjoint layers:
1. Universally proved in Lean 4.36.0 (T01--T20, 0 sorry, 0 Classical.choice,
warnings-as-errors): exact divisibility 3mk + 1 = Mk, universal congruences Mk ≡ 1
(mod 6), mk ≡ 2 (mod 4), Mk ≡ 3 (mod 16) and mk ≡ 6 (mod 8) (k ≥ 2), Eisenstein norm
Mk = (2k)2 + 3, infinite modular obstructions 7 | M3t+1, 13 | M6t+5, 19 | M9t+2, strict
compositeness families, exact sieve densities 1/2 and 5/9, lcm(o, 6) = o collapse under 6 | o,
degree-sum identities for C04--C05, and reduced-class invariance under power substitution.
2. Verified over explicit finite instances by the AST-audited zero-float Python veri-
fier (C01--C16, 71 adversarial pytest checks): direct bit-packed F2[X] DDF and Rabin
irreducibility tests for T1 . . . T5 and substitution towers C14--C16, deterministic Lucas pri-
mality and primitive-root certificates for M6, M8, M9, M14, M15, and the 5-prime covering
sieve mod 90 (C13).
3. Imported from cited literature: Fu–Li–Zuo’s elliptic-curve equivalence between irre-
ducibility of Tk and primality/order of Mk [1, Main Theorem A] (used to translate the de-
terministic Lucas certificates C06--C10 into polynomial irreducibility at degrees mk ≥ 1366),
5
```

---

## Page 6

```text
Gauss–Euler’s cubic residuacity criterion [2], and the classical power-substitution composition
theorem [3, 1].
Archived Artifact Digests. The immutable source artifacts bundled with this record carry
the following exact SHA-256 digests:
• lean/BinaryTrinomialsCert.lean:
SHA-256: 9b218e889d72121b0217a5e7d917780ca46208dcfcb9f5f50f595561eacef926
• src/binary_trinomial_verifier.py:
SHA-256: fb84298f9f7018963a187ad3e5e1a824e6981c6414071d5acc4518f640779551
• certificates/MANIFEST.json:
SHA-256: 2bf21d117125511647f1e157d87de5461dc86790121ef8be2adb3bfc2d7c1c15
AI Assistance Disclosure. This manuscript, the Lean 4.36.0 proof script, the zero-float
Python verifier, and the adversarial test suite were developed with assistance from Google Anti-
gravity; all Lean proofs were independently machine-checked by the Lean 4.36.0 kernel, and all
computational certificates were generated and audited deterministically without floating-point
arithmetic.
References
[1] Siyuan Fu, Zhiming Li, and Huaiqing Zuo. Irreducible trinomials over the binary field: an
elliptic-curve criterion and explicit families, November 2026. arXiv:2611.34282v1.
[2] Kenneth Ireland and Michael Rosen. A Classical Introduction to Modern Number Theory.
Springer-Verlag, 2nd edition, 1990.
[3] Rudolf Lidl and Harald Niederreiter. Finite Fields. Cambridge University Press, 2nd edition,
1997.
[4] Michael O. Rabin. Probabilistic algorithms in finite fields. SIAM Journal on Computing,
9(2):273–280, 1980.
[5] Richard G. Swan. Factorization of polynomials over finite fields. Pacific Journal of Mathe-
matics, 12(3):1099–1106, 1962.
[6] Neal Zierler. Primitive trinomials whose degree is a Mersenne exponent. Information and
Control, 15(1):67–69, 1969.
6
```
