# Exact Shannon Capacity, Schrijver-Lovasz Collapse, and Characteristic-p Haemers Separations on Polar, Kneser, and Sporadic Strongly Regular Graphs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-1S2G8AAASW963AYW` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/shannon-capacity-polar-haemers-schrijver-gaps (`v1.0.0`)  
**Canonical PDF SHA-256:** `058e16bbaa8b731f0aedb02deefbd2cb2cfec1b63a9b1719f7e936980db87e9c`

## Abstract

We establish three exact algebraic-combinatorial theorems separating the Shannon capacity Theta(G), the characteristic-p Haemers minrank bound minrk_{F_p}(G), the real shifted-adjacency rank, and the semidefinite bounds of Lovasz (theta) and Schrijver (theta') across strongly regular graphs (SRGs) and polar orthogonality graphs. First, via an unconditional primal-dual squeeze using the entrywise non-negative Bose-Mesner matrix B* = (I + (1/(r+1))*A_bar)/n (weight x_2* = 1/(r+1) > 0, inner-distribution contribution a_2* = (n-1-k)/(r+1)), we prove that on every SRG G = srg(n,k,lambda,mu) (r >= 0 > s, with no symmetry assumptions), theta'(G) = theta(G) = 1 + (n-1-k)/(r+1) = -ns/(k-s) identically. On ternary polar SRGs NO_eps(2m+1,3) (m >= 2), this yields a three-way exponential hierarchy: F_3-Gram Haemers matrix M of rank 2m+1 (pinning exact alpha = Theta = minrk_{F_3} = 2m+1 when eps = (-1)^m and an exact F_3-discriminant-parity barrier alpha = 2m < rank_{F_3}(M) = 2m+1 when eps = -(-1)^m), theta' = theta = (3^m + 2 - eps)/2 = Theta(3^m), and real shifted-adjacency rank (3^(2m)+3)/4 or (3^m-1)^2/4 = Theta(9^m/4). Second, for Kneser graphs KG(m,2) (m >= 5) and every prime p, we prove the exact if-and-only-if dichotomy min_{c in F_p^*} rank_{F_p}(cI + A) = m - 1 = Theta(KG(m,2)) iff p | (m-4), and equals m otherwise (with sharp non-collapse at (m,p) = (6,5) despite 5 | (m-1), and universal non-collapse over Q and on the Petersen graph m=5 for every prime p). Third, we prove exponential F_2-Haemers vs. theta' = theta gaps on binary polar complements NO^eps(2m,2)^c for all m >= 4 (2m+1 vs. 2^m - 1 and 2^(m-1) + 2), certify zero-float Sturm primal Schrijver theta' lower bounds on the constant-capacity family NO_{sq/nsq}(3,p) (Theta <= 3 vs. theta' >= 43/13 > 3.30 on NO_nsq(3,17), theta' >= 7/2 on NO_sq(3,19), and exact theta' = theta = 19/5 = 3.8 on NO_sq(3,29)), and construct a zero-float sporadic SRG atlas featuring the Higman-Sims graph srg(100,22,0,6): over F_2, (I+A)^2 = I forces full rank 100, while over every odd prime p >= 3 and Q, rank(A - 2I) = 23 (certified for all p >= 5 by a 23x23 principal minor of det 2^22 * 3^2), pinning 22 <= alpha <= Theta(HS) <= 23 < 80/3 = theta' = theta < 100. All core identities are formally verified in Lean 4.36.0 (20 constructive theorems, 0 sorry, 0 Classical.choice) alongside 16 zero-float SHA-256 certificates and 56 adversarial pytest checks.

## Full Extracted Text

--- Page 1 ---
Exact Shannon Capacity, Schrijver–Lovász Collapse,
and Characteristic-pHaemers Separations on Polar,
Kneser, and Sporadic Strongly Regular Graphs
Lluis Eriksson∗
November 27, 2026
Abstract
We establish three exact algebraic-combinatorial theorems separating the Shannon capac-
ityΘ( G), the characteristic-pHaemers minrank boundminrkFp (G), the real shifted-adjacency
rank, and the semidefinite bounds of Lovász (ϑ) and Schrijver (ϑ′) across strongly regular
graphs (SRGs) and polar orthogonality graphs.
First (Theorem 1), we prove unconditionally via a primal–dual squeeze that onevery
strongly regular graphG= srg(n,k,λ,µ )with non-principal eigenvaluesr≥ 0 >s (including
graphs with trivial automorphism group), the Bose–Mesner matrixB∗ = 1
n(I + 1
r+1
¯A)
is entrywise non-negative (x∗
2 = 1
r+1 > 0) and primal feasible for Schrijver’s SDP with
inner-distribution contributiona∗
2 = n−1−k
r+1 , matching Lovász’s Hoffman upper bound and
forcing exact collapseϑ′(G) = ϑ(G) = 1 + (n− 1 −k)/(r+ 1) = −ns/(k−s ). Applying
this to the ternary polar graphsNOε(2m+ 1,3)( m≥ 2, ε∈{ +1,−1}) yields a sharp
three-way exponential hierarchy: theF3-Gram Haemers matrixM has rank2 m+ 1(pinning
exact α = Θ = minrkF3 = 2 m + 1whenever ε = ( −1)m and revealing an exact F3-
discriminant-parity barrierα= 2m<rank F3 (M) = 2m+ 1whenever ε= −(−1)m), whereas
ϑ′= ϑ= (3m +2 −ε)/2 = Θ(3m)and the minimum real shifted-adjacency rank is(32m +3)/4
(ε= +1) or(3 m −1) 2/4(ε=−1), i.e.,Θ(9 m/4).
Second (Theorem 2), we prove an exactif-and-only-ifcharacteristic-p shifted-adjacency
collapse dichotomy for Kneser graphsKG(m,2)(m≥5) overeveryprimep:
min
c∈F×
p
rankFp
(
cI+A(KG(m,2))
)
=m−1 = Θ(KG(m,2))⇐⇒p|(m−4),
and equalsm whenever p∤ (m−4)(including sharp non-collapse at( m,p) = (6,5)despite
5 |(m−1)and universal non-collapse overQ and on the Petersen graphm= 5for every
primep).
Third (Theorem 3), we establish exponentialF2-Haemers versusϑ′= ϑ separations on
binary polar complementsNOε(2m,2) for all m≥ 4(2 m+ 1vs.2 m −1and2 m−1 + 2),
zero-float Sturm-certified primal Schrijverϑ′lower bounds on the constant-capacity family
NOsq/nsq(3,p)(Θ ≤3vs. ϑ′≥43/13 >3.30on NOnsq(3,17), ϑ′≥7/2on NOsq(3,19), and
exact ϑ′= ϑ= 19/5 = 3.8on NOsq(3,29)), and an exact sporadic SRG atlas culminating
in the Higman–Sims graphsrg(100,22,0,6)(constructed from the Witt designS(3,6,22)):
over F2,( I+ A)2 = I forces full rank100, whereas overeveryodd prime p≥ 3and over
Q, rank(A− 2I) = 23(certified for all p≥ 5by an exact23 ×23principal minor of
determinant2 22 ·32), pinning22 ≤Θ(HS) ≤23 <80/3 = ϑ′= ϑ< 100. All core identities
are formalized in Lean 4.36.0 (20constructive theorems,0 sorry,0 Classical.choice)
alongside16zero-float SHA-256 certificates and56adversarial pytest checks.
∗Independent Researcher. Lean 4.36.0 proofs, verification scripts, and certificates are archived at
github.com/lluiseriksson/shannon-capacity-polar-haemers-schrijver-gaps.
1

--- Page 2 ---
1 Introduction
For a finite simple graphG= (V,E), letα(G)denote its independence number and letG⊠k denote
its k-fold strong graph product. Introduced by Shannon [7] to model zero-error communication
over noisy channels, theShannon capacityofGis
Θ(G) := sup
k≥1
α
(
G⊠k)1/k = lim
k→∞
α
(
G⊠k)1/k.
DeterminingΘ( G)exactly is notoriously difficult even on small structured graphs, and sits at
the heart of asymptotic spectrum theory [8]. Three foundational upper-bound families govern
the subject:
1.Lovász’s semidefinite boundϑ(G)[5]:Computable via semidefinite programming,ϑis
multiplicative under strong products (ϑ(G⊠H ) = ϑ(G)ϑ(H)) and satisfiesα(G) ≤Θ(G) ≤
ϑ(G). For anyk-regular graph onnvertices with smallest adjacency eigenvalueλmin(A) <0,
Lovász [5, Theorem 9] proved the Hoffman ratio upper boundϑ(G) ≤−nλmin/(k−λ min),
with equality on every edge-transitive or strongly regular graph.
2. Schrijver’s strengthened SDP bound ϑ′(G)[ 6]:Adding entrywise non-negativity
constraints to Lovász’s primal SDP yieldsα(G)≤ϑ′(G)≤ϑ(G): specifically,
ϑ′(G) = max
{
⟨J,B⟩:B⪰0, B≥0,tr(B) = 1, B ij = 0forij∈E(G)
}
.
Although ϑ′is not known to boundΘ(G)in full generality, it frequently improvesϑ(G)on
irregular or multi-class graphs.
3. Haemers’s field-rank boundminrkF(G)[ 3, 4]:Over any field F, a matrixM∈F V×V
fits G if Mvv ̸= 0for every v∈V and Muv = 0whenever u̸= v are non-adjacent inG.
Defining minrkF(G) := min{rankF(M) : MfitsG} and the shifted-adjacency restriction
minrkshift
F (G) := minc∈F×rankF(cI+ A(G)), Haemers [3] proved submultiplicativity under
Kronecker products and henceΘ(G) ≤minrk F(G) ≤minrk shift
F (G)for every fieldF. Because
minrkF depends sensitively on the characteristic ofF, finite-field rank bounds can beat
ϑ(G)—and even real rank bounds—by arbitrarily large factors [3, 1].
Despite four decades of study, the exact interplay between Schrijver’sϑ′, characteristic-
p Haemers bounds, real shifted-adjacency rank, and discriminant-parity obstructions across
canonical strongly regular families [2] has lacked a unified, formally verified treatment. In this
paper we prove three self-contained theorems that pin down these separations with complete
algebraic exactness:
• Theorem 1proves universal Schrijver–Lovász collapseϑ′(G) = ϑ(G)onallstrongly regular
graphs, and derives the exact three-way exponential hierarchyO(m) ≪Θ(3m) ≪Θ(9m/4)
plus the exactF3-discriminant-parity obstruction on ternary polar SRGsNOε(2m+ 1,3).
• Theorem 2establishes the exact divisibility criterionp| (m−4)governing characteristic-p
shifted adjacency collapse on Kneser graphsKG(m,2)for allm≥5and all primesp.
• Theorem 3resolves binary polar complementsNOε(2m,2) , certifies zero-float Sturm primal
Schrijver ϑ′lower bounds on the constant-capacity familyNOsq/nsq(3,p), and presents an
exact sporadic SRG atlas featuring the dramatic even-vs.-odd characteristic split on the
Higman–Sims graph (rankF2(I + A) = 100vs. rankFp(A− 2I) = 23for every odd prime
p≥3).
2

--- Page 3 ---
2 Universal SRG Collapse and Ternary Polar Hierarchy
Recall that a strongly regular graphG= srg(n,k,λ,µ )(0 <k <n− 1) has adjacency matrix
A satisfying A2 = kI + λA+ µ(J−I−A ), with principal eigenvaluek and non-principal
eigenvalues r≥ 0 >s solving x2 −(λ−µ )x−(k−µ ) = 0(so µ= k+ rs, r+ s= λ−µ , and
k(k−λ−1) =µ(n−1−k)) [2].
For m≥ 2, let V = F2m+1
3 carry the standard non-degenerate quadratic formQstd(x) =∑2m+1
i=1 x2
i withsymmetricbilinearform ⟨x,y⟩= ∑2m+1
i=1 xiyi (mod 3). Partitionthenon-isotropic
points ofPG(2m,3)into V1 := {[x] : Qstd(x) = 1}and V2 := {[x] : Qstd(x) = 2}. Connecting two
distinct points iff⟨x,y⟩̸≡ 0 ( mod 3)produces the two ternary polar non-orthogonality SRGs
NOε(2m+ 1,3)( ε∈{ +1,−1}) onnε = 1
2 3m(3m + ε)vertices, where V1 realizes signε= (−1)m
and V2 realizes signε= −(−1)m (in particular, atm= 2, V1 is NO+(5,3)on45vertices and V2
isNO −(5,3)on36vertices) [2].
Theorem 1(Universal SRG Schrijver Collapse and Ternary Polar Hierarchy).
(a) Universal SRG collapseϑ′ = ϑ:For every strongly regular graph G = srg(n,k,λ,µ )
with non-principal eigenvaluesr≥ 0 >s, Schrijver’s bound collapses identically to Lovász’s
bound:
ϑ′(G) =ϑ(G) = 1 + n−1−k
r+ 1 = −ns
k−s .(1)
(b) Three-way exponential separation onNOε(2m+ 1,3):For every m≥ 2and ε∈
{+1,−1}, the ternary polar graphG= NOε(2m+ 1,3)satisfies:
minrkF3(G)≤rank F3(M) = 2m+ 1
(
Mij :=⟨vi,vj⟩mod 3
)
,(2)
ϑ′(G) =ϑ(G) = 3m + 2−ε
2 ,(3)
min
c∈R
rankR
(
cI+A(G)
)
=
{
(32m + 3)/4ifε= +1,
(3m −1) 2/4ifε=−1. (4)
Consequently, for allm≥3(ε= +1) and allm≥2(ε=−1),
Θ(G)≤minrk F3(G)≤2m+ 1<ϑ ′(G) =ϑ(G) = Θ(3 m)<rank min
R (G) = Θ(9m/4),
where rankmin
R (G) := minc∈R rankR(cI+ A(G)). Moreover, even the unweighted0/1shift
I + A(G) ≡M ◦2 (mod 3)collapses to rank at most
(2m+2
2
)
= O(m2)over F3 (attaining
exact rank15atm= 2,cert01–cert02).
(c)Exact capacity vs. discriminant-parity barrier:OnNO ε(2m+ 1,3):
•Whenε= (−1) m (Qstd = 1),α(G) = Θ(G) = minrk F3(G) = 2m+ 1.
• When ε = −(−1)m (Qstd = 2), α(G) = 2 m <2m+ 1, because any2m+ 1mutually
orthogonal vectors of norm2would have Gram determinant22m+1 ≡2 ( mod 3), con-
tradicting the fact thatdet(P⊤P) = ( detP)2 ̸≡2 ( mod 3). In particular, NO−(5,3)
exhibits the strict four-level chainα= 4 <rank F3(M) = 5 <ϑ′= ϑ= 6 <rank min
R = 16
withΘ≤minrk F3 ≤5(cert02).
Proof. (a)Let ¯A = J−I−A be the adjacency matrix of the complement¯G (degree kbar =
n−1 −k >0). Its eigenvalues arekbar on1, ¯r= −1 −s >0, and ¯s= −1 −r≤− 1on1 ⊥.
Consider the Bose–Mesner matrix
B∗:= 1
n
(
I+x ∗
2 ¯A
)
, x ∗
2 := 1
r+ 1 >0
3

--- Page 4 ---
(strictly positive sincer≥ 0, Leanthm01). Its eigenvalues are1
n(1 + kbar
r+1 ) >0, 1
n(1 + −1−s
r+1 ) >0,
and 1
n(1 + −1−r
r+1 ) = 0, so B∗ ⪰0. Moreover, B∗ is entrywise non-negative (sincex∗
2 > 0),
satisfies tr(B∗) = 1, and vanishes on every edge ofG (since ¯Aij = 0for ij∈E (G)). Thus B∗is
unconditionally primal feasible for Schrijver’s SDP [6]—with no symmetry or automorphism-
group assumption whatsoever—yielding the lower bound
ϑ′(G)≥⟨J,B ∗⟩= 1 +a ∗
2 = 1 + n−1−k
r+ 1 , a ∗
2 :=x∗
2kbar = n−1−k
r+ 1 .
On the other hand, Lovász’s Theorem 9 [5] gives the upper boundϑ′(G) ≤ϑ(G) ≤−ns/(k−s ).
Cross-multiplying by(k−s)(r+ 1)gives
(k−s)
(
(r+ 1) + (n−1−k)
)
−(r+ 1)(−sn) =µ(n−1−k)−k(k−λ−1) = 0
using µ= k+ rs and λ= µ+ r+ s (formally verified in Leanthm02), squeezingϑ′(G) = ϑ(G)
identically and proving (1).
(b)Let q := 3m and q1 := 3m−1. The orthogonality complementG of NOε(2m+ 1,3)is
strongly regular with parametersn= q(q+ε)/2, kbar = q1(q−ε)/2, andλbar = µbar = q1(q1−ε)/2
(satisfying the SRG quadratic equation identically, Leanthm05), with non-principal eigenvalues
±q1 [2]. Passing toGyieldsr=q 1 −1ands=−q 1 −1, so (1) immediately gives
ϑ′(G) =ϑ(G) = 1 + q1(3q1 −ε)/2
q1
= 3m + 2−ε
2
(Lean thm03–thm04). For theF3-Haemers bound, letU∈F n×(2m+1)
3 have rows given by canonical
representatives vi ∈F 2m+1
3 of the vertices ofG. The Gram matrix M := UU⊤ ∈F n×n
3 has
Mii = Qstd(vi) ∈{1,2}(nonzero inF3) andMij = ⟨vi,vj⟩= 0whenever i̸= j are non-adjacent,
so M fits G over F3 and minrkF3(G) ≤rank F3(M) = 2m+ 1(since the rows ofU span F2m+1
3
and Qstd is non-degenerate; verified explicitly form= 2in cert03). Furthermore, sincea2 = 1
for everya∈F ×
3 , expanding( ∑
a vawa)2 = ∑
a v2
aw2
a + 2∑
a<b(vavb)(wawb)over F3 yields the
Veronese factorization
I+A(G)≡M ◦2 = Φ(U)DΦ(U) ⊤ (mod 3),
whereΦ : F2m+1
3 →F (2m+2
2 )
3 sends v↦→(v2
a; vavb)a<b and D = diag(1,..., 1,2,..., 2), immedi-
ately cappingrank F3(I+A(G))≤
(2m+2
2
)
.
For the real shifted-adjacency rank(4), the eigenspace multiplicitiesm¯r,m¯sof G satisfy
m¯r+m¯s= n−1and q1(m¯r−m¯s) = −kbar = −q1(q−ε)/2, givingm¯r= 1
2 (n−1−(q−ε)/2) <m¯s.
Killing the larger non-principal eigenspace ofG (eigenvalue r = q1 −1, multiplicitym¯s) via
c= −r minimizes rankR(cI+ A(G))at1 + m¯r, which simplifies to(q2 + 3)/4for ε= +1and
(q−1)2/4for ε= −1(Lean thm09). The strict inequalities2m+ 1 <ϑ<rank min
R for allm≥ 3
(ε = +1) and all m≥ 2( ε = −1) are formally proved by induction in Lean (thm06, thm07,
thm10) and tabulated throughm= 10incert04.
(c)When ε= (−1)m (Qstd = 1), the2 m+ 1standard basis vectorse1,...,e 2m+1 ∈F 2m+1
3
satisfy Qstd(ei) = 1and ⟨ei,ej⟩= 0( i̸= j), forming an independent set of size2m+ 1matching
the Haemers upper bound (2), hence α = Θ = minrkF3 = 2 m+ 1. When ε = −(−1)m
(Qstd = 2), suppose for contradiction thatw1,...,w 2m+1 were mutually orthogonal vectors with
Qstd(wi) = 2. Letting P∈F (2m+1)×(2m+1)
3 have columnswi, we would haveP⊤P = 2I2m+1,
so( detP)2 = det(2I2m+1) = 22m+1 ≡2 ( mod 3), impossible since every square inF3 is0or1
(Lean thm08). Conversely, pairing coordinates intom orthogonal2-planes yields2 m mutually
orthogonal norm-2vectors( e2t−1 + e2t,e2t−1 −e2t)(1 ≤t≤m ), provingα(G) = 2m exactly
(cert02).
4

--- Page 5 ---
Figure 1:(a)Three-way exponential hierarchy on NO+(2m+ 1,3): F3-Gram Haemers bound
2m+ 1 = O(m), Lovász–Schrijverϑ = ϑ′= (3m + 1)/2 = Θ(3m), and minimum real shifted-
adjacency rank(3 2m + 3)/4 = Θ(9m/4).(b)Exponential separation ratio ϑ/(2m+ 1)for both
signs, highlighting the exactm= 2four-level separation on NO−(5,3)( α= 4 <rank F3(M) =
5<ϑ= 6<rank min
R = 16).
3 Exact Characteristic-p Haemers Dichotomy for Kneser Graphs
KG(m,2)
Form≥ 5, the Kneser graphKG(m,2)has vertex set
([m]
2
)
(size n=
(m
2
)
), with two2-subsets
adjacent iff they are disjoint. It is strongly regular with parameterssrg(
(m
2
)
,
(m−2
2
)
,
(m−4
2
)
,
(m−3
2
)
),
eigenvalues r = 1(multiplicity
(m
2
)
−m) and s = −(m− 3)(multiplicity m− 1), and exact
Erdős–Ko–Rado independence number and Lovász–Schrijver capacityα = Θ = ϑ′ = ϑ =
m− 1[ 5, 2]. By contrast, over Q (characteristic0), the minimum shifted-adjacency rank
minc∈Q×rankQ(cI+A(KG(m,2)))is strictly larger, namelym(attained atc= −1). Remarkably,
passing to prime characteristicp triggers an exact arithmetic collapse if and only ifp| (m−4).
Theorem 2(Exact Characteristic- p Haemers Dichotomy forKG(m,2)).For every integer
m≥5and every primep, the shifted-adjacency Haemers rankminrk shift
Fp (KG(m,2))satisfies:
min
c∈F×
p
rankFp
(
cI+A(KG(m,2))
)
=
{
m−1 = Θ(KG(m,2))ifp|(m−4),
mifp∤(m−4). (5)
In every case, the minimum is achieved atc≡− 1 ( modp ), whereas every shiftc̸≡− 1 ( modp )
satisfies rankFp(cI + A) ≥
(m
2
)
−m≥m > m− 1forall m≥ 5(in particular, the Petersen
graphm= 5collapses fornoprimep).
Proof. Let N∈{ 0,1}(m
2 )×m be the edge-vertex incidence matrix of the complete graphKm, so
row e= {i,j} of N equals ei + ej. Then( NN⊤)e,f = |e∩f|∈{ 0,1,2}, which equals2if e= f,
1if |e∩f| = 1, and0if e∩f = ∅(i.e., e∼f in KG(m,2)). Therefore, overZ, we have the exact
identity
A(KG(m,2))−I=J (m
2 ) −NN ⊤ (6)
(verified explicitly form= 5,..., 12in cert05). Moreover,N1m = 21(m
2 ). We split the analysis
ofc≡−1 (modp)by the parity ofp:
Case 1: p is an odd prime.Because Km contains a triangleK3 whose3 ×3incidence
submatrix has determinant2 ̸≡0 ( modp ), and every vertexi is expressed incolFp(N⊤)via
5

--- Page 6 ---
2ei = (ei + ej) + (ei + ek) −(ej + ek), we haverankFp(N) = m. Using1 (m
2 ) = 1
2 N1m over Fp,
equation (6) factors completely throughN:
A−I=N
(1
4Jm −Im
)
N⊤ overF p.
Since N has full column rankm, rankFp(A−I ) = rankFp(Jm −4Im). Over Z, the symmetric
m×m matrix Gm := Jm−4Im has determinantdetZ(Gm) = (−4)m−1(m−4)(eigenvalue −4with
multiplicity m−1on1 ⊥
m and m−4on1 m). Reducing modulo an odd primep(so gcd(p,4) = 1,
Lean thm11), Gm is invertible overFp iff p∤ (m− 4); and since Gm = −4Im +1 m1⊤
m is a
rank-1perturbation of the invertible matrix−4Im, its rank drops by at most1whenp| (m−4)
(regardless of whetherp|m ). Hence rankFp(A−I ) = m− 1iff p| (m− 4), and equalsm
otherwise.
Case 2: p= 2.Over F2, equation(6) reads A+ I = J+ NN⊤. The row spacecolF2(N⊤) ⊂
Fm
2 is the( m−1)-dimensional even-weight hyperplaneWeven := {v∈F m
2 : ∑ vi ≡0 ( mod 2)},
while kerF2(N) = span{1m}(since N1m = 21 ≡0). Hence rankF2(NN⊤) = dim(Weven) −
dim(Weven ∩span{1m}), which equalsm− 2if1 m ∈W even (i.e.,2 |m ) and m− 1if2 ∤m .
Next,1 (m
2 ) /∈colF2(N)for all m≥ 5: if Nv =1over F2, thenvi + vj ≡1for every pair {i,j},
impossible on any triangle{1,2,3}since( v1 + v2) + (v2 + v3) + (v3 + v1) = 0 ̸= 3 ≡1 ( mod 2).
Because NN⊤ is symmetric withcolF2(NN⊤) ⊆col F2(N)and1 (m
2 ) /∈colF2(N), adding the
symmetric rank-1matrixJ=11 ⊤strictly increases the rank by1:
rankF2(A+I) = rank F2(NN⊤) + 1 =
{
(m−2) + 1 =m−1if2|m⇐⇒2|(m−4),
(m−1) + 1 =mif2∤m⇐⇒2∤(m−4)
(Leanthm12).
Non-collapsing shifts c̸≡ −1 ( modp ).For p = 2, c∈F ×
2 forces c = 1 ≡ −1, so
only odd primesp admit c̸≡− 1 ( modp ). For odd p, let E1 := kerFp(N⊤) ⊂F (m
2 )
p . Since
1(m
2 ) = 1
2 N1m ∈col Fp(N), everyw∈E 1 automatically satisfies1 ⊤w = 1
2 1⊤
m(N⊤w) = 0and
hence( A−I )w = (J−NN ⊤)w = 0by (6). Therefore( cI+ A)w = (c+ 1)w for allw∈E 1.
Becausec+ 1̸≡0 (modp),cI+Aacts as an invertible scalar onE 1, so
rankFp(cI+A)≥dim Fp(E1) =
(
m
2
)
−rank Fp(N) =
(
m
2
)
−m≥m>m−1
forevery m≥ 5(including the Petersen graphm= 5, where
(5
2
)
−5 = 5 >4; formally proved
for allm≥5in Leanthm13and verified acrossm= 5,...,12incert06–cert07).
Remark 1.Theorem 2 reveals a sharp arithmetic subtlety: atm = 6, even though p = 5
divides α(KG(6,2)) = m−1 = 5, rankF5(cI+ A)stays strictly at6, while p= 2(which divides
m−4 = 2) collapses immediately to5(Leanthm14, Figure 2(a)).
4 Binary Polar SRGs, Constant-Capacity Family, and Sporadic
SRG Atlas
We now extend our exact framework to characteristic2(binary polar SRGs), to non-SRG
constant-capacity polar graphs in dimension3using Sturm-certified primal Schrijver bounds,
and to the classical sporadic SRGs—Clebsch, Schläfli complement, and Higman–Sims.
Theorem 3(Binary Polar Gaps, Constant-CapacityNO(3,p), and Sporadic SRG Atlas).
6

--- Page 7 ---
Figure 2:(a)Exact characteristic- p Haemers matrixminc∈F×
p
rankFp(cI+ A(KG(m,2)))across
m= 5,..., 15and p∈{ 2,3,5,7,11}: green cells satisfyp| (m−4)and collapse to m−1 = Θ,
whereas white cells equalm. The orange box highlights the sharp non-collapse at(m,p) = (6,5)
despite5 |(m−1).(b)Shift-rank separation between c= −1and c̸= −1 ( modp )(with green
collapse markers starting atm= 6, since no prime divides5−4 = 1).
(a) Binary polar complementsNOε(2m,2) :Let V = F2m
2 carry the hyperbolic (ε = +1,
Q+(x) = ∑m−1
i=0 x2ix2i+1) or elliptic (ε= −1, Q−(x) = x2
0 +x0x1 +x2
1 +∑m−1
i=1 x2ix2i+1) non-
degenerate quadratic form with symplectic polarizationB(x,y) = ∑m−1
i=0 (x2iy2i+1 + x2i+1y2i)
(mod 2). Let Gε := NOε(2m,2) be the orthogonality graph on{x∈V : Qε(x) = 1}(distinct
x,yadjacent iffB(x,y) = 0). ThenI+A(G ε) =J+BoverF 2, so
Θ(Gε)≤rank F2
(
I+A(G ε)
)
≤2m+ 1,(7)
while exact SRG collapse (Theorem 1(a)) yields
ϑ′(G+) =ϑ(G+) = 2m −1 (m≥3), ϑ ′(G−) =ϑ(G−) = 2m−1 + 2 (m≥2),
producing strict exponential separations2m+ 1 <ϑ′(G−) <ϑ′(G+)forevery m≥ 4(Lean
thm15–thm17,cert09–cert11).
(b) Constant-capacity NOsq/nsq(3,p)with Sturm-certified primal ϑ′ bounds:For every
odd prime p≥ 5, define NOsq(3,p)(resp. NOnsq(3,p)) on projective lines in F3
p with
Q(v) = v2
0 + v2
1 + v2
2 a nonzero square (resp. nonsquare) modp, adjacent iff⟨u,v⟩̸≡ 0
(modp). Then:
• For every odd primep≥ 5, α(NOsq(3,p)) = Θ(NOsq(3,p)) = minrkFp(NOsq(3,p)) = 3,
whereas α(NOnsq(3,p)) = 2(by discriminant obstruction det(gI3) = g3 /∈(F×
p )2) with
Θ(NOnsq(3,p))≤minrk Fp ≤3.
• Exact annihilating polynomialsP( ¯A) = 0(verified across all columns of the complement
adjacency matrix ¯A) combined with exact rational Sturm root isolation proveΛI+ ¯A⪰ 0
and hence primal Schrijverϑ′(G)≥1 +k bar/Λ, certifying:
ϑ′(
NOnsq(3,17)
)
≥43
13 >3.30, ϑ ′(
NOsq(3,19)
)
≥7
2 = 3.5,
ϑ′(
NOsq(3,29)
)
=ϑ
(
NOsq(3,29)
)
= 19
5 = 3.8,
all strictly exceedingΘ≤3(Leanthm18,cert12–cert13).
7

--- Page 8 ---
(c) Exact sporadic SRG atlas and Higman–Sims odd-vs.-even split:Exact zero-float
construction, integer minor determinants, and rank verification establish (Leanthm19–thm20,
cert14–cert16):
• Clebsch srg(16,5,0,2): α= 5, minrkshift
Fp = rankQ(A−I ) = ϑ′= ϑ= 6foreveryprime
p (certified by an exact unimodular6×6principal minor of A−I of determinant−1).
• Schläfli complementsrg(27,10,1,5)(cf. [3]): α= 6, minrkshift
Fp = rankQ(A−I ) =
7 < 9 = ϑ′ = ϑ foreveryprime p (certified for all oddp by an exact7 ×7principal
minor of determinant4, plus directF2 rank7).
• Higman–Sims srg(100,22,0,6): ϑ′= ϑ= 80/3 ≈26.67, α≥ 22(neighborhood of any
vertex, since HS is triangle-free). OverF2, the SRG equationA2 +6A−16I = 6J reduces
to A2 ≡0 ( mod 2), forcing(I+A)2 ≡I (mod 2)and hencefull rank rankF2(I+A) = 100.
In sharp contrast, overeveryodd primep≥ 3and over Q, rankFp(A−2I) = 23(certified
for all p≥ 5by the23 ×23principal minor on {∗}∪N (∗)of exact determinant2 22 ·32,
plus directF3 rank23), pinning
22≤α(HS)≤Θ(HS)≤23< 80
3 =ϑ′(HS) =ϑ(HS)<100 = rank F2(I+A).(8)
Proof. (a)On {Qε(x) = 1 }⊂F 2m
2 , since B(x,x) = 0identically for a symplectic form in
characteristic2, the matrix Mxy := 1 + B(x,y) ( mod 2)satisfies Mxx = 1and Mxy = 1 ⇐⇒
B(x,y) = 0 ⇐⇒x∼y in Gε, i.e.,I+ A(Gε) = J+ B. Because B is a2 m-dimensional bilinear
form onF2m
2 , rankF2(B) ≤2m, and adding the rank-1matrixJ givesrankF2(I+A(Gε)) ≤2m+1
(attained with equality form = 3,4on G+ in cert09 and form = 2,3,4on G− in cert10).
Setting q2 := 2m−2, the exact SRG parameters ofG+ (m≥ 3) aren= 2q2(4q2 −1), k= 4q2
2 −1,
r = q2 −1, s = −2q2 −1, while for G− (m≥ 2) they are n = 2 q2(4q2 + 1), k = 4 q2
2 −1,
r= 2q2 −1, s= −q2 −1[ 2]. Substituting into(1) yields ϑ′(G+) = ϑ(G+) = 4q2 −1 = 2m −1
andϑ ′(G−) =ϑ(G−) = 2q2 + 2 = 2m−1 + 2(Leanthm15–thm16), strictly exceeding2m+ 1for
allm≥4by induction (Leanthm17).
(b)Over Fp, the3-column coordinate matrixU∈F n×3
p yields the rank-3Gram matrixUU⊤
fitting NOsq/nsq(3,p), provingΘ ≤minrk Fp ≤3. ForNOsq(3,p), the standard basis{e1,e2,e3}
has Q(ei) = 1 ∈(F×
p )2 and forms a size-3independent set, giving α = Θ = minrkFp = 3.
ForNOnsq(3,p), if three mutually orthogonal vectorsw1,w2,w3 ∈F 3
p all had nonsquare norm,
rescaling them by elements ofF×
p so thatQ(wi) = g (a fixed nonsquare) would yieldP⊤P = gI3
and hence( detP)2 = g3 /∈(F×
p )2, a contradiction; since¯k> 0for all p≥ 5, an orthogonal pair
exists andα(NO nsq(3,p)) = 2(verified explicitly atp= 17incert12).
To certify rigorous zero-floatlowerbounds onϑ′(G)(and hence onϑ(G)), observe that for any
k-regular graphG on n vertices with complement adjacency matrix¯A (degree kbar = n−1 −k)
and any rationalΛ > 0, ifΛ I + ¯A⪰ 0(equivalently λmin( ¯A) ≥−Λ), then B := 1
n(I + 1
Λ
¯A)
satisfies B⪰ 0, B≥ 0, tr(B) = 1, andBij = 0on E(G), hence is primal feasible for Schrijver’s
SDP and unconditionally certifiesϑ(G) ≥ϑ′(G) ≥⟨J,B⟩ = 1 + kbar/Λ. Whenever an explicit
integer polynomialP∈Z [x]satisfies P( ¯A) = 0, every eigenvalue of¯A is a root ofP, so exact
rational Sturm root isolation proving zero real roots ofP on( −∞,−Λ)certifiesΛ I+ ¯A⪰ 0
with zero floating-point error!
• On NOnsq(3,17)( n= 136,kbar = 9), the exact degree-9polynomialP17( ¯A) = 0is verified on
all136columns and has0real roots below −Λ = −39/10by Sturm’s theorem, certifying
ϑ′≥1 + 9/(39/10) = 43/13>3.307(cert12).
• On NOsq(3,19)( n= 171,kbar = 10), the exact degree-10polynomialP19( ¯A) = 0is verified
on all171columns and has0real roots below −4, certifying ϑ′ ≥1 + 10/4 = 7 /2 = 3 .5
(cert13).
8

--- Page 9 ---
Figure 3:(a)Binary polar complements NOε(2m,2) : F2-Haemers bound2 m+ 1versus Lovász–
Schrijver ϑ = ϑ′ = 2 m −1( ε = +1) and2 m−1 + 2( ε = −1), crossing for allm≥ 4.(b)
Constant-capacity NO(3,p)(exact Sturm-certified primal ϑ′ lower bounds43 /13,7/2,19/5)
and sporadic SRG atlas comparingα(G), certified Fp-Haemers upper bounds, and ϑ′ ≤ϑ ,
highlighting Higman–Sims’s off-scaleF2-rank100versus odd-prime rank23.
• On NOsq(3,29)( n= 435,kbar = 14), the exact degree-14polynomialP29( ¯A) = 0is verified
on all435columns, satisfies P29(−5) = 0, and has0real roots strictly below−5, certifying
λmin( ¯A) = −5and primalϑ′≥1+14/5 = 19/5 = 3.8; becauseO(3,29)acts vertex-transitively
on Gand edge-transitively on¯G, Lovász [5, Theorems 8–9] givesϑ( ¯G) = −435(−5)/(14+5) =
435·5/19andϑ(G) = 435/ϑ( ¯G) = 19/5, pinning exactϑ′=ϑ= 19/5 = 3.8(cert13).
(c)We construct the Clebsch graph directly as the folded5-cube onF4
2 (Hamming distance
1or4), the Schläfli complement directly from the27lines on a cubic surface (Haemers’s classic
7 < 9example [ 3]), and the Higman–Sims graph directly from the Witt designS(3,6,22)
(combining the21extended lines ofPG(2,4)with the56-element PSL(3,4)-orbit of the canonical
conic-plus-nucleus hyperovalH0, cert14–cert16). For Clebsch,rankQ(A−I ) = 6and the6 ×6
principal submatrix on{0,1,2,3,4,8}has exact determinant−1, forcingrankFp(A−I ) = 6for
everyprimep. For Schläfli c,rank Q(A−I) = 7and the7×7principal submatrix on{0,...,6}
has exact determinant4, forcing rankFp(A−I ) = 7for all odd primes p, matching directF2
elimination (rankF2(A+I) = 7).
For Higman–Simssrg(100,22,0,6), the eigenvalues are221,277,(−8)22, so(1) yields ϑ′= ϑ=
100 ·8/(22 + 8) = 80/3(Lean thm20). Its adjacency matrix satisfiesA2 + 6A−16I = 6J over Z.
Reducing modulo2annihilates6 A,16 I, and6 J, yieldingA2 ≡0 ( mod 2), whence( I+ A)2 =
I+2A+A2 ≡I (mod 2): thusI+Ais an involution overF2 of full rank100. By contrast,A−2I
annihilates the77-dimensional eigenspace ofr = 2, sorankFp(A−2I) ≤rank Q(A−2I) = 23
for every primep. On the23vertices {∗}∪N (∗)(where N(∗)is a size-22independent set),
the23 ×23principal submatrix of A−2I is
(−21 ⊤
22
122 −2I22
)
, whose Schur-complement determinant
over Z is( −2)22(−2 + 22/2) = 222 ·32 = 37,748,736( cert16, Leanthm20), which is nonzero
modulo every primep≥ 5; combined with direct verificationrankF3(A−2I) = 23, this proves
rankFp(A−2I) = 23foreveryodd primep≥3and establishes (8).
5 Formal Verification and Reproducibility
All algebraic identities, SRG parameter equations, Sturm root-isolation proofs, and finite-
field/rational rank certifications are verified by a two-layer zero-trust stack:
9

--- Page 10 ---
Table 1: Summary of exact independence number, certifiedFp-Haemers upper bounds, Lovász–
Schrijver bounds, and real/other ranks across Theorems 1–3.
Graph Family / Instance ExactαCertifiedFp-Haemers UB Lovász–Schrijverϑ′≤ϑReal / Other Rank Certificate
NO+(2m+ 1,3)(meven)2m+ 1 2m+ 1(F3Gram, exact)ϑ′=ϑ= (3m+ 1)/2 (3 2m+ 3)/4(R)cert01,cert03–04NO−(5,3)(n= 36)4 5(F 3Gram)ϑ ′=ϑ= 6 16(R),15(F 3I+A)cert02–03KG(m,2)(m≥5)m−1m−1iffp|(m−4)(shift)ϑ ′=ϑ=m−1m(Qandp∤(m−4))cert05–08
NO+(2m,2)(m≥3) —≤2m+ 1(F 2shift)ϑ ′=ϑ= 2m−1 7,9(m= 3,4,F 2)cert09,cert11
NO−(2m,2)(m≥2) —≤2m+ 1(F 2shift)ϑ ′=ϑ= 2m−1+ 2 5,7,9(m= 2,3,4,F2)cert10–11NOnsq(3,17)(n= 136)2 3(F 17Gram)ϑ ′≥43/13≈3.31Deg-9Sturm certcert12NOsq(3,19)(n= 171)3 3(F 19Gram, exact)ϑ ′≥7/2 = 3.5Deg-10Sturm certcert13NOsq(3,29)(n= 435)3 3(F 29Gram, exact)ϑ′=ϑ= 19/5 = 3.8Deg-14,λmin(¯A) =−5cert13Clebschsrg(16,5,0,2) 5 6(allp, shift)ϑ ′=ϑ= 6 6(Q),det 6×6=−1cert15Schläflicsrg(27,10,1,5) 6 7(allp, shift)ϑ ′=ϑ= 9 7(Q),det 7×7= 4cert14Higman–Simssrg(100,22,0,6)≥22 23(all oddp, shift)ϑ′=ϑ= 80/3≈26.67 100(F2),det23= 222·32 cert16
1. Lean 4.36.0 (lean/ShannonCapacityPolarHaemers.lean):20constructive theorems
(thm01–thm20) compiled underlean -DwarningAsError=true with zero external depen-
dencies, zero sorry, zero Classical.choice, and zero custom axioms, formalizing the
universal SRG Schrijver–Lovász algebraic identity, the ternary polar SRG equations, induc-
tive exponential hierarchies, theF3 discriminant-parity obstruction, the Kneser odd-prime,
binary parity, andm≥ 5eigenspace-dimension proofs, the binary polar ϑ formulas and
m≥ 4separation, and the exact primal Schrijver and minor-determinant inequalities for
NOsq/nsq(3,p), Schläfli complement, Clebsch, and Higman–Sims.
2. Zero-Float Python Verifier:The pure standard-library verifierverification/verify_
shannon_polar_haemers.py (int/Fraction, self-audited via AST for zero floating-point
constants, zero/, zero**, and zerolimit_denominator) generates16deterministic SHA-256
certificates withMANIFEST.jsonSHA-256 digest
dedd1043ef3944cfdb7b8d959df00729df0b5de784ed9e50971d075ea1f0803f
independently cross-checked by56adversarial unit tests (tests/test_adversarial.py).
AI Assistance Disclosure.Manuscript drafting, algebraic exploration, Lean 4 formalization,
zero-float verification scripting, and adversarial test construction were carried out by the author
using Google Antigravity, with every mathematical claim independently verified by Lean 4.36.0
and exact rational/finite-field certificates.
References
[1] N. Alon,The Shannon capacity of a union, Combinatorica18(1998), no. 3, 301–310.
[2] A.E.BrouwerandH.VanMaldeghem,Strongly Regular Graphs, EncyclopediaofMathematics
and its Applications182, Cambridge University Press, Cambridge, 2022.
[3] W. H. Haemers,On some problems of Lovász concerning the Shannon capacity of a graph,
IEEE Trans. Inform. Theory25(1979), no. 2, 231–232.
[4] W. H. Haemers,An upper bound for the Shannon capacity of a graph, inAlgebraic Methods
in Graph Theory, Vol. I (Szeged, 1978), Colloq. Math. Soc. János Bolyai25, North-Holland,
Amsterdam, 1981, pp. 267–272.
[5] L. Lovász,On the Shannon capacity of a graph, IEEE Trans. Inform. Theory25(1979),
no. 1, 1–7.
[6] A. Schrijver,A comparison of the Delsarte and Lovász bounds, IEEE Trans. Inform. Theory25
(1979), no. 4, 425–429.
10

--- Page 11 ---
[7] C. E. Shannon,The zero error capacity of a noisy channel, IRE Trans. Inform. Theory2
(1956), no. 3, 8–19.
[8] J. Zuiddam,The asymptotic spectrum of graphs and the Shannon capacity, Combinatorica39
(2019), no. 5, 1173–1184.
11
