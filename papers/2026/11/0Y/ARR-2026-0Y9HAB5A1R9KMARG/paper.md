# Birational Quartic Descent, Infinite Duplication Towers, Elementary 2-Descent Rank-Zero Proofs, Group-Law Duality, and Constructive Fermat Descent for Pythapotent Hypotenuse-Leg Pairs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0Y9HAB5A1R9KMARG` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper144-pythagorean-hl-pairs (`v1.0.1`)  
**Canonical PDF SHA-256:** `32cb25c93626b006283b0692aa47421894eeddef4093286b37d6f9ae4088eb8b`

## Abstract

Halbeisen, Hungerbuhler, and Shamsi Zargar (2026, arXiv:2611.34902v1) introduced pythapotent hypotenuse-leg pairs (hl-pairs) of degree h, reducing pythapotency to positive Mordell-Weil rank of the elliptic curve Gamma_{c^h, d^h}: y^2 = x(x + c^(2h))(x - d^(2h)), proving universal pythapotency for h in {1, 3} (Corollaries 8-9), giving a quartic family for h = 2 (Corollary 10), and relying on Magma to assert rank(Gamma_{5^2, 4^2}(Q)) = 0. We establish four self-contained, elementary, machine-checked theorems backed by 20 constructive Lean 4.36.0 theorems (zero external imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-float SHA-256 certificates, and 56 adversarial tests: (1) Explicit Birational Isomorphism Psi: Q_1 -> E_12, Degree-4 Morphism Phi = -[2] o Psi, Quartic Unification, & Infinite Duplication Tower (h = 2): we exhibit the genuine birational isomorphism Psi(m, n, q) = (2(q+n^2)/m^2, 4n(q+n^2)/m^3) from Q_1: 3m^4 + n^4 = q^2 onto E_12: Y^2 = X^3 - 12X with rational inverse Psi^(-1)(X, Y) = (m/n = 2X/Y, q/n^2 = 2X^3/Y^2 - 1), show Phi = -[2] o Psi, unify all four Corollary 10 quartics under (m, n) -> (m+n, m-n), and prove that the duplication endomorphism (m', n', q') = (2mnq, |3m^4 - n^4|, 9m^8 + 18m^4n^4 + n^8) preserves (gcd(m,n)=1, opposite parity, 3 nmid n) while strictly growing q' > q and c' > c; (2) 4-Adic/8-Adic Corollary 10 Obstructions & Elementary Magma-Free 2-Descent Rank-Zero Theorem: we prove mod-4 and mod-8 Corollary 10 obstructions and prove via elementary complete 2-descent that rank(Gamma_{C,A}(Q)) = 0 whenever C = p^k (p = 5 mod 8 prime), A = 2^s (s >= 3), and Q = C^2 + A^2 is prime, yielding the first Magma-free proof that (5, 4) is not pythapotent of degree 2 (C=25, A=16, Q=881); (3) Exact Lemma 5-6 Group-Law Identity (R = +[2]P), Crossed Remark-1 Norm Conservation, Symmetry Dichotomy, & Non-2-Divisibility Barrier: we prove R = +[2]P identically in both coordinates, formalize Remark 1's crossed norm law, contrast Corollary 8 symmetry with Corollary 9 hypotenuse ordering 2c^2 - a^2 < 2c^2 - b^2 iff b < a, and prove that universal points of Corollaries 8, 9, and 10 never lie in [2]Gamma_{c^h, d^h}(Q); and (4) Constructive Fermat Infinite Descent, Elementary Lemma 2 (h=1, 2|h), & Torsion-3/4 Boundary: proving both x^4 + y^4 != z^2 and x^4 - y^4 != z^2 constructively in Lean 4 from Euclidean gcd square-factoring, we prove Lemma 2 (h=1, 2|h) and cd != square without Darmon-Merel, exclude rational 4-torsion, and establish the exact 3-division identity psi_3(x) = 4x^2(x+C^2)(x-A^2) - (x^2 + C^2 A^2)^2.

## Full Extracted Text

--- Page 1 ---
Birational Quartic Descent, Inﬁnite Duplication
Towers, Elementary 2-Descent Rank-Zero Proofs,
Group-Law Duality, and Constructive Fermat
Descent for Pythapotent Hypotenuse–Leg Pairs
Lluis Eriksson
Independent Researcher
ORCID: 0009-0006-7494-9040
November 27, 2026
Abstract
Halbeisen, Hungerbühler, and Shamsi Zargar [ 4] recently introduced pythapotent
hypotenuse–leg pairs (hl-pairs) of degree h: positive integer pairs (c,d) with c2 − d2 = e2 >0
admitting a Pythagorean pair (k,l) ̸∼(d,e) (k2 + l2 = □) such that (chk)2 − (dhl)2 =
□ >0. Reducing degree- h pythapotency to positive Mordell–Weil rank of the elliptic curve
Γch,dh : y2 = x(x+ c2h)(x− d2h), they proved universal pythapotency for h∈ {1,3}(Corol-
laries 8–9), gave a quartic suﬃcient family for h = 2 (Corollary 10), and reported Magma
rank computations on (5,3) and (5,4) (including rank(Γ52,42 (Q)) = 0 ). We establish four
self-contained, elementary, and machine-checked structural theorems resolving all unproved
algebraic assertions, Magma-only rank-zero barriers, group-law ambiguities, and external
descent dependencies in [ 4], backed by 20 constructive Lean 4.36.0 theorems (zero external
imports, zero sorry, zero Classical.choice, zero warnings), 16 AST-audited zero-ﬂoat
SHA-256 certiﬁcates, and 56 adversarial tests:
1. Explicit Birational Isomorphism Ψ : Q1
∼
− → E12, Degree-4 Morphism Φ =
−[2] ◦Ψ, Quartic Uniﬁcation, & Inﬁnite Duplication Tower ( h = 2 ): Clos-
ing the unproved claim on p. 11 of [ 4], we exhibit the genuine birational isomorphism
Ψ(m,n,q ) =
(2(q+n2)
m2 ,4n(q+n2)
m3
)
from Q1 : 3 m4+n4 = q2 to E12 : Y2 = X3−12Xwith ra-
tional inverse Ψ− 1(X,Y ) =
(m
n = 2X
Y , q
n2 = 2X3
Y 2 −1
)
(and show the degree- 4 descent mor-
phism Φ(m,n,q ) =
( q2
m2n2 ,q(3m4− n4)
m3n3
)
factors as Φ = −[2]◦Ψ), unify all four Corollary 10
quartics via Remark 2’s (m,n) ↦→(m+ n,m− n) identity, and prove that the polynomial
duplication endomorphism (m′,n′,q′) = (2 mnq,|3m4 −n4|,9m8 +18m4n4 +n8) preserves
gcd(m,n) = 1 , opposite parity, and 3 ∤ n while strictly growing q′ > qand c′ > c(e.g.
(2,1,7) ↦→(28,47,2593) ↦→ ···), constructively generating an inﬁnite primitive degree-2
pythapotent tower.
2. 4-Adic/8-Adic Corollary 10 Obstructions & Elementary Magma-Free 2-
Descent Rank-Zero Theorem for Γ52,42 : We prove mod-4 obstructions blocking
opposite-parity Case 1 quartics and a mod-8 obstruction blocking every primitive Case 2
hl-pair with b≡ 4 (mod 8) (i.e. 4 |b and 8 ∤ b, explaining why (5,4) fails Corollary 10).
Using elementary complete 2-descent, we prove that whenever C = pk (p ≡ 5 (mod 8)
prime), A = 2 s (s ≥ 3), and Q = C2 + A2 is prime (automatically Q ≡ 1 (mod 8)
and (Q/p) = +1 ), every non-torsion 2-descent homogeneous space fails locally at 2 or
p, forcing dimF2 Sel(2)(ΓC,A) = 2 and rank(ΓC,A(Q)) = 0 —giving the ﬁrst elementary,
Magma-free proof that (5,4) is not pythapotent of degree 2 (C = 25 ,A = 16 ,Q = 881 ).
3. Exact Lemma 5–6 Group-Law Identity ( R = +[2] P), Crossed Norm Conser-
vation, Symmetry Dichotomy, & Non-2-Divisibility Barrier: We prove that the
canonical algebraic composition of Lemmas 5 and 6 equals +[2]P identically in both x-
and y-coordinates (so positive-root Lemma 6 yields sgn(jwl)[2]P), formalize Remark 1’s
1
AIRR:ARR-2026-0Y9HAB5A1R9KMARG v1  [Number theory]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
norm conservation law, contrast Corollary 8’s (d ↔ e)-symmetry with Corollary 9’s hy-
potenuse ordering 2c2 − a2 <2c2 − b2 ⇐⇒ b<a , and prove that the universal points of
Corollaries 8 (preimage Q), 9 ( P0,P0 + T0,P0 + T1), and 10 ( P) never lie in [2]Γch,dh(Q).
4. Constructive Fermat Inﬁnite Descent, Elementary Lemma 2 ( h= 1 and 2 |h),
& Torsion-3/4 Algebraic Boundary: Proving both x4 + y4 ̸= z2 and x4 − y4 ̸=
z2 constructively in Lean 4 from Euclidean gcd square-factoring, we prove Lemma 2
of [ 4] for h = 1 and all even h ≥ 2 and cd ̸= □ without Darmon–Merel [ 1], certify
the absence of rational 4-torsion constructively, and prove the exact 3-division identity
ψ3(x) = 4 x2(x+C2)(x−A2)−(x2+C2A2)2 ruling out rational 3-torsion via square-divisor
elimination.
AI Assistance Disclosure. This research manuscript, its constructive Lean 4.36.0 formal-
ization, and its exact-rational Python veriﬁcation suite were developed by Lluis Eriksson with
interactive assistance from Google Antigravity for proof exploration, formal veriﬁcation, and
typesetting. All mathematical proofs, formal Lean theorems, and exact-rational certiﬁcates
were mechanically veriﬁed; the author takes full responsibility for all claims.
1 Introduction and Preliminaries
Extending their earlier studies of paired Pythagorean pairs [ 2, 3], Halbeisen, Hungerbühler,
and Shamsi Zargar [ 4] deﬁned a hypotenuse–leg pair (hl-pair) to be a pair (c,d) ∈ Z2
>0 with
c2 − d2 = e2 for some integer e > 0 (so (d,e,c ) is a Pythagorean triple), and called (c,d)
pythapotent of degree h≥ 1 if there exists a Pythagorean pair (k,l) ∈ Z2
>0 (k2 + l2 = □) not a
rational multiple of (d,e) such that (chk,dhl) is an hl-pair:
c2 − d2 = e2 >0, k 2 + l2 = j2, (chk)2 − (dhl)2 = w2 >0. (1)
To every hl-pair (c,d) and degree h≥ 1, [ 4] associates the elliptic curve
ΓC,A : y2 = x3 + (C2 − A2)x2 − C2A2x = x(x+ C2)(x− A2), C := ch, A := dh. (2)
Using Mazur’s torsion theorem [ 5], Darmon–Merel [ 1], and Mordell’s presentation of Euler’s
quartic [ 6], Proposition 3 and Theorem 4 of [ 4] establish Γch,dh(Q)tors ∼= Z/2Z× Z/2Z and prove
that (c,d) is pythapotent of degree h if and only if rank(Γch,dh(Q)) > 0. Corollaries 8 and 9
show every hl-pair is pythapotent of degrees h = 1 and h = 3 , while Corollary 10 establishes
degree-2 pythapotency whenever c2 + εcd+ d2 = q2 (ε ∈ {1,−1}), remarking without proof
(p. 11) that the resulting quartics are birational to Y2 = X3 − 12X of rank 1, and relying on
Magma to assert rank(Γ52,42 (Q)) = 0 (p. 8).
Table 1 summarizes how our four main theorems close these algebraic, arithmetic, group-law,
and constructive-descent gaps.
2 Birational Descent, Quartic Uniﬁcation, and Inﬁnite Duplica-
tion Tower for Corollary 10
Writing a primitive Pythagorean triple as (a,b,c ) = ( m2 − n2,2mn,m2 + n2) (m > n >0,
gcd(m,n) = 1 , m̸≡n (mod 2) ), Corollary 10 of [ 4] reduces c2 + εcd+ d2 = q2 to four quartics:
Q1 : 3 m4 + n4 = q2 and Q2 : m4 + 3n4 = q2 in Case 1 ( d= a), and Q±
3 : m4 ± 2m3n+ 6m2n2 ±
2mn3 + n4 = q2 in Case 2 ( d= b).
Theorem 2.1 (Birational Descent to E12, Quartic Uniﬁcation, and Constructive Duplication
Tower).
2

--- Page 3 ---
Table 1: Summary of results extending Halbeisen, Hungerbühler, and Shamsi Zargar [ 4].
Topic Halbeisen et al. [ 4] This Paper
Corollary 10
(h= 2 ) quartics
States birationality to E12
on p. 11 without explicit
maps or proof
Explicit birational isomorphism
Ψ : Q1
∼
− →E12 (with rational Ψ− 1) and
Φ = −[2] ◦Ψ, Remark-2 uniﬁcation of all
4 quartics, and invariant-preserving
inﬁnite duplication tower (Thm. 2.1)
Rank 0 of Γ52,42 Reported via Magma
computation (p. 8); no
local obstruction analysis
Mod-4 / mod-8 obstructions for Cor. 10;
Magma-free complete 2-descent proving
rank(ΓC,A(Q)) = 0 for all C = pk
(p≡ 5 mod 8 ), A= 2 s (s≥ 3),
Q= C2 + A2 prime, including Γ52,42
(Thm. 3.1)
Lemmas 5–6 &
Cor. 8–10 points
Maps P ↦→(k,l) ↦→R
(x(R) = x([2]P)); y-sign
and 2-divisibility
unanalyzed
Exact algebraic identity R= +[2] P (both
coordinates); Remark-1 norm law; Cor. 8
symmetry vs. Cor. 9 asymmetry;
non-2-divisibility barrier for Cor. 8, 9, 10
(Thm. 4.1)
Lemma 2 &
Prop. 3 torsion
Invokes Darmon–Merel [ 1],
Mazur [ 5], and Euler [ 6]
Constructive Lean 4 Fermat descent
(x4 ± y4 ̸= z2) proving Lemma 2 ( h= 1 ,
2 |h), cd̸= □, no 4-torsion, and exact
ψ3(x) identity (Thm. 5.1)
1. Explicit Birational Isomorphism Ψ : Q1
∼− →E12 & Degree-4 Morphism Φ = −[2] ◦Ψ
(Lean thm01–thm02, Cert. C01): For any nonzero m,n,q ∈ Z satisfying 3m4 + n4 = q2 (with
q+ n2 ̸= 0 ), the map
Ψ(m,n,q ) :=
(
2(q+ n2)
m2 , 4n(q+ n2)
m3
)
(3)
is a genuine birational isomorphism from Q1 : 3 m4 + n4 = q2 onto E12 : Y2 = X3 − 12X,
with rational inverse
Ψ−1(X,Y ) : m
n = 2X
Y , q
n2 = 2X3
Y2 − 1. (4)
Moreover, the degree- 4 rational descent morphism
Φ(m,n,q ) :=
(
q2
m2n2 , q(3m4 − n4)
m3n3
)
(5)
maps Q1 → E12 and factors identically as Φ = −[2] ◦Ψ (with squared-coordinate recovery
m2
n2 = s3+Y
6s , n2
m2 = s3−Y
2s for s= q/(mn)).
2. Remark-2 Quartic Uniﬁcation (Lean thm03, Cert. C02): Under the linear involution
(m,n) ↦→(m+ n,m − n),
3(m+ n)4 + (m− n)4 = 4( m4 + 2m3n+ 6m2n2 + 2mn3 + n4), (6)
(m+ n)4 + 3(m− n)4 = 4( m4 − 2m3n+ 6m2n2 − 2mn3 + n4),
establishing explicit rational equivalences Q+
3 ∼= Q1 and Q−
3 ∼= Q2 ∼= Q1 (swapping m↔ n).
3. Invariant-Preserving Inﬁnite Duplication Tower (Lean thm04–thm05, Certs. C01,
C03–C04): For every positive integer solution (m,n,q ) to 3m4 + n4 = q2 with 3m4 ̸= n4,
deﬁne
m′:= 2 mnq, n ′:= |3m4 − n4|, q ′:= 9 m8 + 18m4n4 + n8. (7)
3

--- Page 4 ---
Then 3(m′)4+(n′)4 = ( q′)2, q′>q, and the triple of arithmetic invariants (gcd(m,n) = 1 , m+
n≡ 1 (mod 2) , 3 ∤ n) is preserved identically at every step. Consequently, setting ck := m2
k +
n2
k, ak := |m2
k − n2
k|, and εk := sgn( mk − nk) ∈ {1,−1}yields c2
k + εkckak + a2
k = q2
k; iterating
from (m0,n0,q0) = (2 ,1,7) ↦→(28,47,2593) ↦→ ···constructively generates inﬁnitely many
distinct primitive degree- 2 pythapotent hl-pairs (beginning (5,3) and (2993,1425)).
Proof. (1) Set M := m4, N := n4, and S := q+ n2. Since q2 = 3 M + N, we have S2 − 3M =
q2 + 2 n2q+ N − (q2 − N) = 2 n2S, whence (2S)3 − 12(2S)M = 8 S(S2 − 3M) = 16 n2S2 =
(4nS)2 (Lean thm01); dividing by m6 veriﬁes Ψ(m,n,q ) ∈ E12. For the rational inverse, 2X
Y =
4S/m2
4nS/m3 = m
n and 2X3
Y 2 − 1 = 16S3/m6
16n2S2/m6 − 1 = S−n2
n2 = q
n2 (Lean thm02), conﬁrming Ψ−1 ◦Ψ = id .
Conversely, for any (X,Y ) ∈ E12 with Y ̸= 0 (so Y2 = X3 − 12X), setting t := 2 X/Y
and u := 2 X3/Y2 − 1 = ( X3 + 12 X)/Y2 satisﬁes 3t4 + 1 = (48 X4 + ( X3 − 12X)2)/Y4 =
(X3 + 12X)2/Y4 = u2 (hence Ψ−1(E12) ⊂ Q1), and 2(u+ 1)/t2 = (4 X3/Y2)/(4X2/Y2) = X,
4(u+ 1) /t3 = (8 X3/Y2)/(8X3/Y3) = Y, verifying Ψ ◦Ψ−1 = id with zero square roots. For
Φ, (3M − N)2 = (3 M + N)2 − 12MN = q4 − 12MN gives q2(3M − N)2 = q6 − 12q2MN
(Lean thm01), and direct evaluation of the duplication formula on E12 at (X,Y ) = Ψ( m,n,q )
gives x([2]Ψ) = (3X2−12)2
4Y 2 − 2X = q2
m2n2 and y([2]Ψ) = − q(3m4−n4)
m3n3 , so Φ = −[2] ◦Ψ (Cert. C01),
with q3 ± q(3M − N) = 6 qM,2qN (Lean thm02).
(2) Expanding (m±n)4 = m4 ±4m3n+6m2n2 ±4mn3 +n4 and forming 3(m+n)4 +(m−n)4
and (m+ n)4 + 3(m− n)4 gives ( 6) directly (Lean thm03, Cert. C02).
(3) Setting X := m4,Y := n4 so q2 = 3 X+ Y, we have 3(m′)4 + (n′)4 = 48 XY(3X+ Y)2 +
(3X− Y)4 = 81 X4 + 324X3Y + 342X2Y2 + 36XY3 + Y4 = (9 X2 + 18XY + Y2)2 = ( q′)2, and
q′= (3 X+ Y)2 + 12XY = q4 + 12XY > q(Lean thm04). Moreover, since c2
k = ( m2
k + n2
k)2 ∈
[1
3 q2
k,2q2
k] (as m4
k + n4
k ≤ c2
k ≤ 2(m4
k + n4
k) and 1
3 q2
k ≤ m4
k + n4
k ≤ q2
k) while qk+1 > q4
k, we have
c2
k+1 ≥ 1
3 q2
k+1 > 1
3 q8
k > 2q2
k ≥ c2
k (for all qk ≥ 7), so the hypotenuses ck are strictly increasing
and all generated primitive hl-pairs (ck,ak) are pairwise distinct. For invariant preservation:
since m′= 2 mnq is even while n′= |3m4 − n4| ≡ 3m4 − n4 ≡ m+ n ≡ 1 (mod 2) , opposite
parity is preserved; since n′= |3m4 − n4| ≡ ±n4 ≡ ± 1 ̸≡0 (mod 3) whenever 3 ∤ n, 3 ∤ n′is
preserved (Lean thm04). For coprimality, let p be a prime dividing gcd(m′,n′). Since n′is odd
and 3 ∤ n′, p /∈ {2,3}. Thus p |mnq. If p |m or p |n, then p |(3m4 − n4) forces p to divide
both m and n, contradicting gcd(m,n) = 1 . If p |q, then p |(3m4 + n4) and p |(3m4 − n4)
force p|6m4 and p|2n4; as p /∈ {2,3}, p|gcd(m,n) = 1 , contradiction. Hence gcd(m′,n′) = 1 .
Finally, (m2 + n2)2 + (m2 + n2)(m2 − n2) + ( m2 − n2)2 = 3 m4 + n4 (Lean thm05), so replacing
m2 − n2 by ε|m2 − n2|(ε = sgn( m− n)) gives c2
k + εkckak + a2
k = q2
k, satisfying Corollary 10
of [ 4] (Certs. C01, C03).
3 Modular Obstructions and Elementary 2-Descent Rank-Zero
Theorem for ΓC,A
Halbeisen et al. [ 4] (p. 8) used Magma to report rank(Γ52,42 (Q)) = 0 , proving (5,4) is not
pythapotent of degree 2. We ﬁrst isolate the elementary congruential obstructions explaining
why Corollary 10 fails on (5,4) and half of all Case 1 parameters, and then prove an inﬁnite
family of elementary, Magma-free complete 2-descent rank-zero theorems covering Γ52,42 .
Theorem 3.1 (Modular Obstructions and Elementary 2-Descent Rank-Zero Family) .
1. Corollary 10 Congruential Obstructions (Lean thm06–thm07, Cert. C05):
• If m is odd and n is even, then 3m4 + n4 ≡ 3 (mod 4) , so Q1 has no integer solution;
symmetrically, if m is even and n is odd, then m4 + 3 n4 ≡ 3 (mod 4) , so Q2 has no
integer solution.
4

--- Page 5 ---
Figure 1: (a) Quadruple-exponential height growth ( log10 qk and log10 ck) of the invariant-
preserving duplication tower ( 7) seeded at (2,1,7) (Theorem 2.1). (b) Genuine birational image
Ψ(2,1,7) = (4 ,4) and degree- 4 morphism images Φ(2,1,7) = −[2]Ψ(2,1,7) = ( 49
4 ,329
8 ) and
Φ(28,47,2593) on E12 : Y2 = X3 − 12X.
• For every primitive Case-2 hl-pair (c,b) with b ≡ 4 (mod 8) (i.e. 4 |b and 8 ∤ b, equiva-
lently 2 |mn and 4 ∤ mn, such as (5,4)), c2 ± cb+ b2 ≡ 5 (mod 8) , so Corollary 10 fails
for both ε= ±1.
2. Elementary Complete 2-Descent Rank-Zero Theorem (Lean thm08–thm10,
Certs. C06–C08): Let p ≡ 5 (mod 8) be prime, k ≥ 1, s ≥ 3, C := pk, A := 2 s, and
suppose Q:= C2 + A2 is prime. Then automatically Q≡ 1 (mod 8) and (Q/p) = +1 , and
among all 16 real-solvable 2-descent homogeneous spaces of ΓC,A : y2 = x(x+ C2)(x− A2),
all 12 non-torsion cosets are locally unsolvable at 2 or p:
• every coset with δ∈ {±2,±2p}fails modulo p (since (2/p) = −1 and (Q/p) = +1 );
• every coset with δ∈ {±p,±2p}fails 2-adically across all three coprime valuation regimes
(2 ∤ u, 2 ∥u, and 4 |u,2 ∤ v).
Hence |Sel(2)(ΓC,A)|= 4 = |ΓC,A(Q)[2]|, forcing rank(ΓC,A(Q)) = 0 .
3. Magma-Free Proof for (5,4) at h= 2 (Lean thm10, Cert. C06): Specializing Part (2) to
(p,k,s ) = (5 ,2,4) gives C = 25 , A= 16 , and Q= 25 2 + 162 = 881 (prime, 881 ≡ 1 (mod 8) ,
881 ≡ 1 (mod 5) ), proving unconditionally and without Magma that rank(Γ52,42 (Q)) = 0 , so
(5,4) is not pythapotent of degree 2.
Proof. (1) Every odd integer satisﬁes x4 ≡ 1 (mod 4) and every even integer satisﬁes x4 ≡ 0
(mod 4) , whereas squares are 0 or 1 (mod 4) (Lean thm06). For c odd and b≡ 4 (mod 8) , we
have c2 ≡ 1, cb ≡ 4, and b2 ≡ 0 (mod 8) , giving c2 ± cb+ b2 ≡ 5 (mod 8) , impossible since
squares mod 8 lie in {0,1,4}(Lean thm07).
(2) Note that C = pk is odd and 8 |A= 2 s (s≥ 3), so Q= C2 +A2 ≡ 1+0 = 1 (mod 8) and
Q≡ (2s)2 (mod p), whence the Legendre symbol (Q/p) = +1 holds automatically (Cert. C08).
For complete 2-descent on ΓC,A : y2 = x(x+ C2)(x− A2) with gcd(C,A) = 1 (Silverman–
Tate [ 7]), any rational point P = ( x,y) (y ̸= 0 ) has x with square denominator (since any
prime q with negative odd vq(x) would force odd vq(y2) = 3 vq(x)), so writing x= δu2/v2 with
gcd(u,v) = 1 , gcd(δ,v) = 1 (v >0) and squarefree (δ,d1,d2) (δd1d2 = □) gives the homogeneous
space
δu2 + C2v2 = d1w2
1, δu 2 − A2v2 = d2w2
2. (8)
Because gcd(u,v) = gcd( δ,v) = 1 , the pairwise gcd bounds gcd(δu2,δu2 + C2v2) |C2 = p2k,
gcd(δu2,δu2 − A2v2) |A2 = 2 2s, and gcd(δu2 + C2v2,δu2 − A2v2) |Q (with Q prime, Q ∤ 2p)
5

--- Page 6 ---
restrict the prime support of the squarefree triples:
• 2 divides neither d1 (if 2 |u then 2 ∤ v and C is odd, so δu2 + C2v2 is odd) nor Q, hence
v2(δ) = v2(d2) ∈ {0,1}and v2(d1) = 0 ;
• pdivides neither d2 (if p|uthen p∤ v and p∤ A, so δu2 − A2v2 is coprime to p) nor Q, hence
vp(δ) = vp(d1) ∈ {0,1}and vp(d2) = 0 ;
• Q cannot divide δ, so vQ(d1) = vQ(d2) ∈ {0,1}.
By real solvability of ( 8): if δ >0, then δu2 + C2v2 > 0 forces d1 > 0, whence d2 > 0 (since
δd1d2 = □ > 0); if δ <0, then δu2 − A2v2 < 0 forces d2 < 0, whence d1 > 0. Thus there
are exactly 2 × 23 = 16 real-solvable triples (δ,d1,d2): 4 come from the 2-torsion subgroup
ΓC,A(Q)[2]—namely O ↦→ (1,1,1), (0,0) ↦→(−1,1,−1), (A2,0) ↦→(1,Q,Q ), and (−C2,0) ↦→
(−1,Q, −Q)—and 12 are non-torsion ( δ∈ {±2,±p,±2p}, vQ ∈ {0,1}).
To check Qℓ-solvability (ℓ∈ {2,p}) of the projective curve ( 8) in (u: v: w1 : w2): ﬁrst, the
hyperplane at inﬁnity v= 0 requires δ/d1,δ/d2 ∈ (Q×
ℓ )2, which fails for all 12 non-torsion cosets
(for δ = ±2, (δ/d1 mod p) = ( ±2/p) = −1; for δ = ±p, δ/d2 = pQ−vQ ≡ 5 (mod 8) /∈ (Q×
2 )2;
for δ = ±2p, v2(δ/d1) = 1 is odd). Second, any Qℓ-point with v ̸= 0 scales homogeneously to
(u,v) ∈ Z2
ℓ with min(vℓ(u),vℓ(v)) = 0 , which forces w1,w2 ∈ Zℓ (since d1,d2 are squarefree, so
vℓ(diw2
i ) ≥ 0 = ⇒ vℓ(wi) ≥ 0). We now eliminate all 12 non-torsion triples in Zℓ:
(a) Mod-p elimination of δ = ±2 (4 cosets): Here d1 ∈ {1,Q} satisﬁes (d1/p) = +1 , while
d2 = sgn( δ) ·2QvQ satisﬁes (d2/p) = ( ±2/p) = −1 (since p≡ 5 (mod 8) , so (−1/p) = +1
and (2/p) = −1). If p ∤ u, reducing the ﬁrst equation ±2u2 + C2v2 = d1w2
1 modulo p
gives ±2u2 ≡ d1w2
1 (mod p), contradicting (±2u2/p) = −1 versus (d1w2
1/p) ∈ {0,+1}
(Lean thm08). If p |u, then p ∤ v (as gcd(u,v) = 1 ), so reducing the second equation
±2u2 − A2v2 = d2w2
2 modulo p gives −A2v2 ≡ d2w2
2 (mod p), contradicting (−A2v2/p) =
(−1/p) = +1 (as p∤ A) versus (d2w2
2/p) ∈ {0,−1}. Thus both p∤ uand p|ufail locally at
p.
(b) 2-adic elimination of δ = ±p (4 cosets): Here d1 ∈ {p,pQ} ≡ 5 (mod 8) and d2 =
sgn(δ) ·QvQ ≡ sgn(δ) (mod 8) . Multiplying the second equation by sgn(δ) yields pu2 −
sgn(δ)A2v2 = |d2|w2
2 with |d2| ≡1 (mod 8) and 64 |A2. We split into the three exhaustive
coprime 2-adic valuation cases (Lean thm09):
• 2 ∤ u: pu2 ≡ 5 (mod 8) , forcing |d2|w2
2 ≡ 5 (mod 8) , impossible since |d2| ≡1 (mod 8)
and w2
2 mod 8 ∈ {0,1,4}.
• 2 ∥u: writing u= 2 u1 (2 ∤ u1), 4 |(pu2 −sgn(δ)A2v2) forces 2 |w2 (w2 = 2 w′
2). Dividing
by 4 gives pu2
1 − sgn(δ)(A/2)2v2 = |d2|(w′
2)2; since 4 |(A/2) (as 8 |A), this reduces mod
8 to 5 ≡ |d2|(w′
2)2 (mod 8) , impossible.
• 4 |u: by gcd(u,v) = 1 , v is odd, so 8 |pu2 and C2v2 ≡ 1 (mod 8) . The ﬁrst equation
then gives d1w2
1 ≡ 1 (mod 8) , impossible since d1 ≡ 5 (mod 8) implies d1w2
1 mod 8 ∈
{0,4,5}.
(c) 2-adic elimination of δ = ±2p (4 cosets): Here d1 ∈ {p,pQ} ≡ 5 (mod 8) and d2 =
sgn(δ) ·2QvQ (|d2|/2 ≡ 1 (mod 8) ). If 2 ∤ u, the second equation ±2pu2 − A2v2 = d2w2
2
divided by 2 gives pu2 − sgn(δ)(A2/2)v2 = ( |d2|/2)w2
2 =⇒ 5 ≡ (|d2|/2)w2
2 (mod 8) (as
32 |A2/2), impossible. If 2 |u, then v is odd and 8 |2pu2, so the ﬁrst equation gives
d1w2
1 ≡ C2v2 ≡ 1 (mod 8) , impossible since d1 ≡ 5 (mod 8) .
Thus only the 4 torsion cosets survive local solvability, proving |Sel(2)(ΓC,A)| = 4 and
rank(ΓC,A(Q)) = 0 .
(3) Immediate from Part (2) with p= 5 , k= 2 , s= 4 , C = 25 , A= 16 , Q= 881 (Lean thm10,
Cert. C06).
6

--- Page 7 ---
Figure 2: (a) Complete 16-coset 2-descent elimination matrix on Γ52,42 : all 12 non-torsion cosets
fail locally at 2 or 5, proving rank = 0 without Magma (Theorem 3.1). (b) Certiﬁed rank-zero
instances of the generalized family C = pk (p ≡ 5 (mod 8) ), A = 2 s (s ≥ 3), Q = C2 + A2
prime.
4 Exact Lemma 5–6 Group-Law Identity, Crossed Duality, and
Non-2-Divisibility Barrier
Theorem 4 of [ 4] links rational points on ΓC,A to Pythagorean pairs (k,l) via Lemma 5 ( P ↦→
(k,l)) and Lemma 6 ( (k,l) ↦→R), observing that x(R) = x([2]P) without establishing the y-
coordinate identity or checking whether the universal points of Corollaries 8–10 are divisible by
2 in Γch,dh(Q).
Theorem 4.1 (Group-Law Identity, Crossed Norm Conservation, Symmetry Dichotomy, and
Non-2-Divisibility).
1. Exact Lemma 5–6 Group-Law Identity (Lean thm11, Cert. C09): Let P = ( x1,y1) ∈
ΓC,A(Q) with y1 ̸= 0 , and deﬁne the signed polynomials
k:= x2
1 + C2A2, l := 2 Cy1, j := x2
1 + 2C2x1 − C2A2, w := C(x2
1 − 2A2x1 − C2A2).
Then k2 + l2 = j2, (Ck)2 − (Al)2 = w2, and the Lemma 6 point R:=
(C2k2
l2 , C2kjw
l3
)
equals
+[2]P identically in both coordinates (when positive roots |j|,|w|,|l|are taken in Lemma 6,
R+ = sgn( jwl) [2]P).
2. Crossed Remark-1 Norm Conservation & Corollary 8–9 Symmetry Dichotomy
(Lean thm12–thm13, Certs. C10–C11): Under Remark 1’s duality (l′,k′) := ( Ck,Al), setting
(ˆk,ˆl) := ( Ck′,Al′) = ( CAl,CAk ) satisﬁes (Ck′)2 + (Al′)2 = ˆk2 + ˆl2 = C2A2(k2 + l2), while
(Ck)2 − (Al)2 = w2 implies (l′)2 − (k′)2 = w2. Moreover, Corollary 8’s universal pair
(d4 + d2e2 + e4,2c2de) is strictly (d ↔ e)-symmetric (identical for Case 1 and Case 2),
whereas Corollary 9’s pair (d2,2ce) has hypotenuse 2c2 − d2, strictly breaking symmetry via
2c2 − a2 <2c2 − b2 ⇐⇒ b<a .
3. Non-2-Divisibility Barrier for Corollaries 8, 9, and 10 (Lean thm14–thm15,
Cert. C12): For every hl-pair (c,d):
• Corollary 8’s preimage Q= ( −cd,−cde) ∈ Γc,d(Q) does not lie in [2]Γc,d(Q);
• Corollary 9’s universal point P0 = ( c4d2,c4d2e(c2+d2)) and its torsion translates P0+(0,0)
and P0 + (−c6,0) do not lie in [2]Γc3,d3 (Q);
• Corollary 10’s point P = ( −εcd3,cd3eq) does not lie in [2]Γc2,d2 (Q) for either ε∈ {1,−1}.
7

--- Page 8 ---
Figure 3: (a) Corollary 9 symmetry breaking: Case 1 (c,a) vs. Case 2 (c,b) hypotenuse 2c2 − d2
across primitive Pythagorean triples (Theorem 4.1). (b) The 3-division polynomial ψ3(x) =
4x2(x+ C2)(x− A2) − (x2 + C2A2)2 on Γ5,3, strictly negative at all three 2-torsion points
(Theorem 5.1).
Proof. (1) Expanding j2 − k2 = 4 C2(x3
1 + ( C2 − A2)x2
1 − C2A2x1) = 4 C2y2
1 = l2 and
(Ck)2 − (Al)2 = C2(k2 − 4A2y2
1) = w2 (Lean thm11) veriﬁes the pair identities. For
the elliptic duplication formula on y2 = x3 + ( C2 − A2)x2 − C2A2x, the tangent slope is
λ= 3x2
1+2(C2−A2)x1−C2A2
2y1
, giving x([2]P) = λ2 − (C2 − A2) − 2x1 = (x2
1+C2A2)2
4y2
1
= C2k2
l2 and
y([2]P) = λ(x1 − x([2]P)) − y1
= (x2
1 + C2A2)(x2
1 + 2C2x1 − C2A2)(x2
1 − 2A2x1 − C2A2)
8y3
1
= C2kjw
l3 ,
proving R= +[2] P identically (Cert. C09).
(2) Both algebraic norm identities and (d2)2 + (2 ce)2 = (2 c2 − d2)2 follow directly from
d2 + e2 = c2 (Lean thm12–thm13, Certs. C10–C11).
(3) By the duplication identities (2) of [ 4], every point S = ( xS,yS) ∈ [2]ΓC,A(Q) must have
xS, xS + C2, and xS − A2 all rational squares (in particular xS ≥ 0).
• For Corollary 8’s Q= ( −cd,−cde): x(Q) = −cd< 0 is not a square in Q (Lean thm15).
• For Corollary 9’s P0 = ( c4d2,... ) on Γc3,d3 : x(P0) + c6 = c4(c2 + d2) being a rational square
forces c2 + d2 = □ (Lean thm14), contradicting Theorem 5.1(2). For the torsion translates:
x(P0 + (0 ,0)) = −c6d6/(c4d2) = −c2d4 < 0, and x(P0 + ( −c6,0)) = −c6 + c6(c6+d6)
c4(c2+d2) =
−c2d2(c2 − d2) = −c2d2e2 <0, neither a square.
• For Corollary 10’s P = ( −εcd3,... ) on Γc2,d2 : if ε = +1 , x(P) = −cd3 < 0; if ε = −1,
x(P) = cd3 = ( cd)d2 being a rational square forces cd = □ (Lean thm15), contradicting
Theorem 5.1(2).
5 Constructive Fermat Descent, Elementary Lemma 2, and
Torsion-3/4 Algebraic Boundary
Lemma 2 and Proposition 3 of [ 4] cite Darmon–Merel [ 1], Mazur [ 5], and Mordell [ 6] even in the
elementary regimes h = 1 and 2 |h. We prove Fermat’s two quartic descents completely con-
structively inside Lean 4.36.0 (using only Euclidean gcd coprime square-factoring and primitive
Pythagorean parametrization, with zero external libraries), and derive self-contained proofs of
8

--- Page 9 ---
Lemma 2 ( h = 1 , 2 |h), cd ̸= □, the absence of 4-torsion, and the exact 3-division algebraic
boundary.
Theorem 5.1 (Constructive Fermat Descent, Elementary Lemma 2, and Torsion-3/4 Certiﬁ-
cation).
1. Constructive Fermat Inﬁnite Descent (Lean thm16–thm17, Cert. C13): Neither x4 +
y4 = z2 nor x4 − y4 = z2 has any solution in positive integers x,y,z ∈ Z>0.
2. Elementary Lemma 2 ( h = 1 and 2 |h) & Non-Square Product (Lean thm18,
Cert. C14): For every hl-pair (c,d) and every h ∈ {1} ∪2Z>0, c2h + d2h ̸= □, and cd ̸= □
(with no reliance on Darmon–Merel [ 1]).
3. Constructive 4-Torsion Elimination & 3-Division Polynomial Identity (Lean
thm19–thm20, Certs. C15–C16): On ΓC,A (C,A> 0):
• No rational point has order 4 whenever C2 + A2 ̸= □ (in particular, for every hl-pair and
h∈ {1} ∪2Z>0).
• The 3-division polynomial ψ3(x) := 3 x4 + 4(C2 − A2)x3 − 6C2A2x2 − C4A4 satisﬁes the
exact identity
ψ3(x) = 4 x2(x+ C2)(x− A2) − (x2 + C2A2)2. (9)
Consequently, any rational point P = ( x,y) of order 3 on ΓC,A satisﬁes 4xy2 = ( x2 +
C2A2)2, forcing x= t2 >0 to be an integer square with t|C2A2 (ruling out 3-torsion by
ﬁnite square-divisor evaluation on any concrete curve, and reducing generally to Euler’s
r4 + r2s2 + s4 = □ via Remark 3 of [ 4]).
Proof. (1) First, if gcd(a,b) = 1 and ab = n2 (a,b,n ∈ N), setting g1 := gcd( a,n) gives g2
1 |a
(since g2
1 |n2 = aband gcd(g2
1,b) = 1 ) and a|g2
1 (writing a= g1a′,n = g1n′with gcd(a′,n′) = 1
forces a′|g1), proving a= g2
1 and symmetrically b= g2
2 with zero prime factorization. Applying
this to primitive Pythagorean triples a2 + b2 = c2 (2 |b) via c+a
2 ·c−a
2 = ( b/2)2 yields coprime
m>n> 0 with a= m2 − n2, b= 2 mn, c= m2 + n2.
• For x4 +y4 = z2 (strong induction on z, Lean thm16): stripping gcd(x,y) reduces to primitive
(x2)2 + (y2)2 = z2 (WLOG 2 |y). Parametrizing gives x2 + n2 = m2, y2 = 2 mn, z= m2 + n2;
parametrizing x2 + n2 = m2 gives n = 2 rs, m = r2 + s2 with m,r,s pairwise coprime and
m(rs) = ( y/2)2. Hence m = ( z′)2, r = ( x′)2, s = ( y′)2, yielding (x′)4 + ( y′)4 = ( z′)2 with
z′≤ m<z .
• For y4 + z2 = x4 (strong induction on x, Lean thm17): stripping gcd(x,y) reduces to
gcd(y2,z) = 1 . If 2 |z, parametrizing gives y2 = m2 − n2, x2 = m2 + n2, yielding
n4 + (xy)2 = m4 with m<x . If 2 ∤ z (so 2 |y), parametrizing gives y2 = 2 mn, x2 = m2 + n2,
so {m,n}= {s2,2r2}and (s2)2 +(2r2)2 = x2. Parametrizing a second time gives s2 = a2 −b2,
r2 = ab, x= a2 + b2, whence a= u2,b = v2, and v4 + s2 = u4 with u<x .
(2) If c2 − d2 = e2 and c2 + d2 = z2, multiplying gives c4 − d4 = ( ez)2, contradicting Part (1).
For even h = 2 k, c2h + d2h = ( ck)4 + ( dk)4 ̸= □ directly by Part (1). If cd = z2, letting
g = gcd( c,d) and c = gc1,d = gd1,e = ge1 yields c1d1 = ( z/g)2 with gcd(c1,d1) = 1 , hence
c1 = u2,d1 = v2, and v4 + e2
1 = u4, again contradicting Part (1) (Lean thm18, Cert. C14).
(3) If P = ( x1,y1) has order 4, then [2]P ∈ {(0,0),(−C2,0),(A2,0)} with x([2]P) =
(x2
1+C2A2)2
4y2
1
>0, ruling out (0,0) and (−C2,0) immediately (Lean thm19 certiﬁes (x2
1 +C2A2)2 >
0, −C2 < 0, and the A2 + C2 = C2 + A2 reduction); at (A2,0), the duplication identity (2)
of [ 4] forces x([2]P) + C2 = A2 + C2 = □, impossible by Part (2). Finally, expanding
4x2(x + C2)(x − A2) − (x2 + C2A2)2 gives ( 9) identically (Lean thm20, Cert. C15). Since
x(x+ C2)(x− A2) = y2 on ΓC,A, ψ3(x) = 0 ⇐⇒ 4xy2 = ( x2 + C2A2)2, forcing x >0 to be
a rational square. By the rational root theorem on 3x4 + ··· −C4A4 = 0 , the denominator of
x divides 3; since 3 is not a square, x = t2 ∈ Z>0 with t |C2A2 (veriﬁed with zero roots on
Γ5,3,Γ5,4,Γ13,5,Γ25,16 in Cert. C16).
9

--- Page 10 ---
6 Formal Veriﬁcation Architecture and Reproducibility
All algebraic identities, modular and 2-adic obstructions, Euclidean square-factoring, primitive
Pythagorean parametrization, Fermat quartic inﬁnite descents, and torsion reductions are ver-
iﬁed across three layers (while Mordell–Weil complete 2-descent homomorphisms and rational-
root divisibility arguments are proved in full in Sections 2–5):
1. Constructive Lean 4.36.0 Formalization: 20 theorems ( thm01–thm20) in lean/
PythagoreanHLPairsBarriers.lean compiling under lean -DwarningAsError=true with
zero external imports, zero sorry, zero grind, zero Classical.choice, and zero warnings.
2. AST-Audited Zero-Float Python Veriﬁer: Pure standard-library code ( int, Fraction)
in verification/verify_pythagorean_hl_pairs.py self-auditing its AST (0 ﬂoat viola-
tions) and emitting 16 canonical SHA-256 certiﬁcates ( C01–C16) across four modes, with
manifest SHA-256 640d215f71c572c37cec8cf0722e7a8e1494ca0ea51cec6f6bb48ee3df278ac1.
3. Adversarial Test Suite: 56 pytest checks in tests/test_adversarial.py covering posi-
tive veriﬁcation and adversarial boundary cases across all four theorems.
References
[1] Henri Darmon and Loïc Merel. Winding quotients and some variants of Fermat’s last theo-
rem. Journal für die Reine und Angewandte Mathematik , 490:81–100, 1997.
[2] Lorenz Halbeisen and Norbert Hungerbühler. Pairing pythagorean pairs. Journal of Number
Theory, 233:467–480, 2022.
[3] Lorenz Halbeisen, Norbert Hungerbühler, and Arman Shamsi Zargar. Pairing powers of
pythagorean pairs. Indagationes Mathematicae , 36:903–911, 2025.
[4] Lorenz Halbeisen, Norbert Hungerbühler, and Arman Shamsi Zargar. Pairing powers of
Pythagorean pairs II. arXiv preprint arXiv:2611.34902v1 , November 2026.
[5] Barry Mazur. Modular curves and the Eisenstein ideal. Publications Mathématiques de
l’IHÉS, 47:33–186, 1977.
[6] Louis J. Mordell. Diophantine Equations . Academic Press, London, 1969.
[7] Joseph H. Silverman and John Tate. Rational Points on Elliptic Curves . Springer-Verlag,
New York, 2nd edition, 2015.
10
