# Obstructions and Constructive Repairs for Shifted Dimensional MATBG Schemes on Deleted Knodel Graphs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-6N6C96A4GV96ZRCB` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/knodel-matbg-obstruction-repair (`v1.0.0`)  
**Canonical PDF SHA-256:** `d0f95556f6fd9bda9eecaf0833579b8b70761ed9fdfbd3d0bc7ddbebfb63aa98`

## Abstract

We analyze the minimum average time broadcast graph (MATBG) construction on deleted Knodel graphs KG'(n-1) proposed in Section 5 of Altay, Fakharan, and Harutyunyan (arXiv:2611.34167v1) and prove both three infinite-family obstructions to their shifted dimensional scheme and three constructive repairs. First, Theorem A shows that shifted dimensional schedules suffer round-i vertex collisions in KG(n) whenever n <= n_max(k,i) = 2^k - 2^i - 4, with asymptotic half-loss 2^{k-2} - 2 at (n,i) = (2^{k-1}+2, 1), proving the Section 5 MATBG claim unproved on intermediate orders n in [2^{k-1}+2, 2^k - 6]. Second, Theorem B proves that for antipodal originators u = n/2 with n = 4m, all 2(k-1) standard and reverse cyclic shifts hit the deleted vertex 0 before round k. Third, Theorem C exhibits a first-half shortcut collision w = 2^{k-2} - 1 in I_{k-1}. Positively, Theorem D provides a universal single-edge shortcut reroute (2^{k-1}-1 -> 2^{k-2}-1) closing Sub-case 5 across the open second half [3*2^{k-2}, 2^k-2], Theorem E establishes a 2-adic shift s = 1 + v_2((n - 2^{k-1})/2) for u = 2^{k-2}, and Theorem F yields the first complete, gap-free MATBG proof for KG'(2^k - 5) and KG'(2^k - 3) for all k >= 4. All 24 universal modular-arithmetic theorems are formally verified in Lean 4.35.0 (0 sorry, 0 custom axioms, 0 Classical.choice, 0 warnings), accompanied by an AST-audited zero-float Python verifier, 16 JSON certificates (C01-C16), and 48 unit and forgery-rejection tests.

## Full Extracted Text

--- Page 1 ---
Dimensional Collision Obstructions, Antipodal Rerouting,
and Machine-Checked Minimum Average Time Broadcast
Proofs for Deleted Knödel Graphs
Lluis Eriksson∗
November 26, 2026
Abstract
Altay, Fakharan, and Harutyunyan [1] recently introduced
a deleted Knödel graph constructionKG′(n−1)establish-
ing the general upper boundB(n−1) ≤⌈(n−1)⌊log2(n−
1)⌋/2⌉on the broadcast function for all evenn̸= 2k, and
claimed in Section 5 that the same construction directly
yields a minimum average time broadcast graph (MATBG)
across the full interval(2k−1,2k), resolving the 1998 open
problem of Liestman and Pržulj [7]. We prove that while
the worst-case broadcast bound b(KG′(n− 1)) = k is
sound, the MATBG claim in [1] fails as proved due
to three infinite-family doubling obstructions: (i) the
cyclically shifted dimensional schemes of Lemmas 3.2
and 3.4 suffer modular wrap-around collisions even in
KG(n)up to the sharp thresholdnmax(k,i) = 2k−2i−4,
losing2 k−2 −2 = Θ( n/2)vertices before round k− 1
at( n,i) = (2 k−1 + 2,1); (ii) for every k≥ 4and ev-
ery n = 4m∈ (2k−1,2k), from the antipodal originator
u= n/2, all2(k−1)standard and reverse cyclically shifted
dimensional schemes inform the deleted vertex0by round
k−1; and (iii) for every evenn∈ [2k−1 +2,3·2k−2 −2], the
shortcut targetw= 2k−2 −1of originator u= 2k−1 −1al-
ready lies inIk−1. We then prove three positive theorems:
a universal single-edge shortcut rerouting rule that closes
Sub-case 5 with exact doubling|It|= 2t (0 ≤t≤k− 1)
across the entire open second halfn∈ [3 ·2k−2,2k −2]; a
2-adic shift laws= 1 +v2((n−2k−1)/2)avoiding vertex0
on the first-half boundaryu= 2k−2; and a complete, gap-
free MATBG proof forKG′(2k −5)and KG′(2k −3)for
all k≥ 4. All universal modular-arithmetic theorems are
formally verified in zero-dependency Lean 4.35.0 (24 theo-
rems,0 sorry,0custom axioms,0 Classical.choice),
paired with an AST-audited zero-float Python verifier
(KNODEL-MATBG-CERT-1.0) certifying 16 canonical wit-
nesses and 48 unit and forgery-rejection checks.
∗Independent researcher. Authored with AI-assisted formal proof
engineering, symbolic verification, and manuscript drafting (Google
Antigravity). Public MIT repository:github.com/lluiseriksson
/knodel-matbg-obstruction-repair (v1.0.0). Manuscript and
figures licensed CC-BY-4.0; code, Lean 4 proofs, and certificates
licensed MIT.
1 Introduction and Definitions
In the classical telephone broadcasting model on an undi-
rected simple graph G = ( V,E)of order m = |V|, a
message originates at a vertexu∈V at time0; in each
discrete roundt≥1, each informed vertex may transmit
the message to at most one uninformed neighbor. A broad-
cast schedule fromu induces a rooted spanning treeTu
with arrival timest(v) ∈N (t(u) = 0). The broadcast time
of Gis b(G) = maxu∈V minTu maxv∈V t(v) ≥⌈log 2 m⌉. A
graph is abroadcast graphif b(G) = ⌈log2 m⌉, and the
broadcast functionB(m)is the minimum number of edges
of anm-vertex broadcast graph [3, 4].
Liestman and Pržulj [7] introduced theminimum av-
erage broadcast time ba(Tu) = 1
m
∑
v∈V t(v), ba(G) =
maxu∈V minTu ba(Tu), and βa(m) = ba(Km). Because
the informed set can at most double per round, achieving
ba(Tu) = βa(m)is equivalent to exact doubling|It|= 2t
for every0 ≤t≤k− 1(where k = ⌈log2 m⌉) followed
by informing the remainingm−2k−1 vertices in roundk,
giving
βa(m) = 1
m
(k−1∑
t=1
t2 t−1 +k(m−2 k−1)
)
.(1)
Aminimum average time broadcast graph(MATBG)
achieves ba(G) = βa(m)with minimum edge count
Ba(m). Since exact doubling through round k− 1re-
quires deg(v) ≥k− 1 = ⌊log2 m⌋for every vertexv when
m̸= 2 k, any MATBG satisfiesBa(m)≥⌈m⌊log 2 m⌋/2⌉.
For even n≥ 4with k = ⌈log2 n⌉ and2 k−1 <
n < 2k, theKnödel graph KG(n)[ 5] has vertex set
V = {0,1,...,n− 1}and edges( v,ϕd(v))for dimensions
1≤d≤k−1, where
ϕd(v)≡2 d −1−v(modn).(2)
Since n is even and2 d −1is odd, KG(n)is bipartite
between even and odd vertices, and ϕd is an involu-
tion (ϕd(ϕd(v)) = v). Moreover, for every u∈V , the
bijection fu(v) = v + (−1)vu (modn )is a dimension-
preserving automorphism of KG(n)mapping0to u
(ϕd(fu(v)) ≡fu(ϕd(v)) ( modn )), so the cardinality|It|
of any dimensional broadcast depends only on(n,D)and
not on the originatoru.
1

--- Page 2 ---
Adimensional broadcast scheme D = ( α1,...,α k)
informs all vertices of KG(n)in k rounds by calling
along ϕαt at round t. Bermond et al. [2] proved that
D(0)
std = (1 ,2,...,k− 1,1), every cyclic shift D(i)
std =
(i+ 1,...,k− 1,1,...,i,i + 1), and every reverse shift
D(i)
rev = ( k−i− 1,..., 1,k− 1,...,k−i,k−i− 1)
(0 ≤i≤k− 2) are valid k-round broadcast schemes
onKG(n).
Altay, Fakharan, and Harutyunyan [1] define thedeleted
Knödel graphKG′(n−1)on V′= {1,...,n− 1}by deleting
vertex0(whose k− 1neighbors in KG(n)are the odd
vertices2 i −1for1 ≤i≤k− 1) and adding⌈(k−1)/2⌉
shortcut edges(2i−1 −1,2i−1)for all even2 ≤i≤k− 1,
plus(2 k−2 −1,2k−1 −1)when k−1is odd. Because KG(n)
is bipartite, no shortcut edge joins vertices of opposite
parity, so all⌈(k− 1)/2⌉shortcut edges are genuinely
new and|E(KG′(n−1))|= ⌈(n−1)(k−1)/2⌉. Section 4
of [1] provesb(KG′(n−1)) = k via Lemmas 3.1–3.4 and
Propositions 3.5–3.7 (where Proposition 3.7 splits even
originators into five ranges, withSub-case 5denoting
n− 2k−1 + 2 ≤u≤min (2k−1 −2,n− 2k−2)), yielding
B(n−1) ≤⌈(n−1)(k−1)/2⌉for all evenn̸= 2k. Section 5
of [1] then asserts without additional proof thatKG′(n−1)
is also a MATBG across(2k−1,2k), claiming to resolve
the open second half(3·2 k−2,2 k)left by [7].
2 Three Infinite-Family MATBG
Obstructions
By Lemmas 3.1–3.4 of [1], the informed setIt in KG(n)
after round t≤k− 1from originator u under D(0)
std is
At ∪Bt (modn), where
At ={2p+u: 0≤p<2 t−1},
Bt ={2s−u−1 : 1≤s≤2 t−1},(3)
and under D(0)
rev is Arev
t ∪B rev
t (modn )with Arev
t =
{−p2k−t + u : 0 ≤p < 2t−1}and Brev
t = ϕk−t(Arev
t ).
For1 ≤i≤k− 2and u = 0, Lemma 3.2 (D(i)
std) gives
Ik−1 = I(i)
k−1,even ∪I (i)
k−1,odd (modn ), where the even-
parity unionA(i)
k−1 ∪B′(i)
k−1 is
A(i)
k−1 ={p2 i+1 + 2j: 0≤p<2 k−i−2,0≤j <2 i−1},
B′(i)
k−1 ={−s2 i+1 + 2j: 1≤s≤2 k−i−2,1≤j≤2 i−1},
(4)
and the odd-parity halfI(i)
k−1,odd = B(i)
k−1 ∪A′(i)
k−1 is the
exact image of I(i)
k−1,even under the round-(k− 1)di-
mensional involutionϕi(x) ≡2i −1 −x (modn )(since
Ik−1 = Ik−2 ∪ϕi(Ik−2)and ϕi swaps parities). Symmet-
rically, Lemma 3.4 (D(i)
rev,1 ≤i≤k− 2, u = 0) has
even-parity sets
A(i)
rev,k−1 ={−j2 k−i −2p: 0≤j <2 i−1,0≤p <2 k−i−2},
B′(i)
rev,k−1 ={j2 k−i −2s: 1≤j≤2 i−1,1≤s≤2 k−i−2},
(5)
mapped bijectively onto the odd-parity half by the round-
(k−1)involutionϕ k−i(x)≡2 k−i −1−x(modn).
Theorem A(Sharp Shifted-Scheme Collision Threshold
and Asymptotic Half-Loss).Let k≥ 4,1 ≤i≤k− 2,
andnbe even with2 k−1 <n<2 k.
1. Unshifted collision-freedom:Under bothD(0)
std and D(0)
rev,
|It| = 2 t for every0 ≤t≤k− 1and every even
n∈(2 k−1,2 k).
2. Sharp collision threshold:Whenever2 i+ 4 <2k−1 (all
k≥ 5and( k,i) = (4,1)), atnmax(k,i) = 2k−2i−4 ∈
(2k−1,2k)the scheme D(i)
std collides at roundk−1even
in KG(n), with explicit witnessx = 2k−1 −2i −2 ∈
A(i)
k−1 ∩(B′(i)
k−1 + n)attained at( p,j) = (2 k−i−2 −
1,2i−1 −1)and( s,j′) = (2 k−i−2,1). Consequently
|Ik−1|= 2 k−1 −2|A(i)
k−1 ∩(B′(i)
k−1 +n)|≤2 k−1 −2.
3. Collision-free upper band:Whenever n> 2k −2i −4,
D(i)
std is collision-free; whenevern >2k −2k−i−1 −4,
D(i)
rev is collision-free. In particular, for n∈{ 2k −
4,2k −2}, all2( k− 1)standard and reverse shifts
satisfy|I t|= 2 t for all0≤t≤k−1.
4. Asymptotic half-loss:At n= 2k−1 + 2and i= 1, every
p∈{ 1,..., 2k−3 −1}collides with s = 2k−3 + 1 −p,
yielding |Ik−1|= 2k−2 + 2and a deficit of2 k−2 −2 =
Θ(n/2)vertices before roundk−1.
Proof. By the dimension-preserving automorphismfu, we
set u = 0. Part (1): In (3), At has span2(2 t−1 −1) <
2k−1 <n, soAt is injective modn; likewise forBt, and
opposite parities separateAt and Bt. For D(0)
rev, Arev
t =
{−p2k−t : 0 ≤p < 2t−1}has span(2 t−1 −1)2k−t =
2k−1 −2k−t < n, hence is injective mod n, and ϕk−t
maps it bijectively onto the odd half Brev
t . Part (2):
In (4), A(i)
k−1 ⊂[0,2k−1 −2i −2] ⊂[0,n)and B′(i)
k−1 +
n⊂ [n− 2k−1 + 2,n− 2i] ⊂(0,n)are each injective
mod n of size2 k−3 (since distinct( p,j)have distinct
base-2bit decompositions and span < n). Because ϕi
mapsI(i)
k−1,even bijectively ontoI(i)
k−1,odd, |Ik−1|= 2|A(i)
k−1∪
(B′(i)
k−1 +n)|= 2k−1 −2|A(i)
k−1 ∩(B′(i)
k−1 +n)|. Substituting
(p,j) = (2 k−i−2 −1,2i−1 −1)and( s,j′) = (2 k−i−2,1)
at nmax = 2k −2i −4yields p2i+1 + 2j = 2k−1 −2i −
2 = nmax −s 2i+1 + 2j′. Part (3): For D(i)
std, p2i+1 +
2j + s2i+1 ≤2k −2i −2 < n+ 2 ≤n + 2j′ whenever
n >2k −2i −4, so A(i)
k−1 and B′(i)
k−1 + n are disjoint.
Symmetrically, in(5) for D(i)
rev, A(i)
rev,k−1 + nand B′(i)
rev,k−1
satisfy j′2k−i + j2k−i + 2p≤ 2k −2k−i−1 −2 < n+ 2s
whenever n >2k −2k−i−1 −4. Both thresholds are at
most2 k−6for1 ≤i≤k− 2, son∈{ 2k−4,2k−2}clears
all2( k−1)shifts and gives |Ik−1|= 2k−1. Since |I0|= 1
and |Ir+1|≤ 2|Ir|, |Ik−1|= 2k−1 forces |It|= 2t for every
2

--- Page 3 ---
Figure 1: Exact vertex loss2k−1 −|Ik−1|in KG(n)for
k = 6( n∈ [34,62]) across standard cyclic shifts i∈
{0,..., 4}. Blue frames mark the sharp Theorem A thresh-
old nmax(6,i) = 64 −2i −4; the green dashed box marks
the universally collision-free upper bandn∈{60,62}.
0 ≤t≤k− 1. Part (4): At n = 2 k−1 + 2and i = 1
(j = 0,j′= 1),4 p= (2k−1 + 2)+ 2−4(2k−3 + 1−p)for all
1 ≤p≤ 2k−3 −1, giving|A(1)
k−1 ∩(B′(1)
k−1 + n)|= 2k−3 −1
and vertex deficit2k−2 −2.
Figure 1 illustrates Theorem A at k = 6: shifted
schemes used in Theorem 4.1 and Proposition 3.7 of [1]
suffer widespread collisions (e.g. |I4| = 14 < 16at
n = 24 ,u = 5and n = 26 ,u = 1; |I6|= 34 < 64at
n= 66,i = 1). Even when shifts are collision-free, a sec-
ond obstruction blocks MATBG doubling inKG′(n−1):
Theorem B(Universal Antipodal Dimensional Obstruc-
tion).For every k≥ 4and every n = 4m with2 k−1 <
n <2k (2k−3 −1even orders per dyadic band, i.e. odd
orders n−1 ≡3 ( mod 4)), from the antipodal originator
u= n/2 = 2m,all2( k−1)standard and reverse cyclically
shifted dimensional schemesD(i)
std,D(i)
rev (0 ≤i≤k− 2)
inform vertex0by round k−1. Consequently, no dimen-
sional scheme from Section 3 of [1] achieves|Ik−1|= 2k−1
inKG ′(n−1)fromu=n/2.
Proof. Since n = 4m <2k, m <2k−2. For i = 0, p =
m < 2k−2 yields2 m+ 2m = n≡ 0under D(0)
std and
−2m+ 2m = 0under D(0)
rev. For D(i)
std (1 ≤i≤k− 2),
write m = q2i + r (0 ≤r < 2i); then q <2k−i−2 since
2k−i−2 ·2i = 2k−2 >m. If r <2i−1,( p,j) = (q,r)gives
p2i+1 + 2j + 2m = 4m = n≡ 0in A(i)
k−1; if r≥ 2i−1,
(s,j) = (q+1,2i−r)gives −s2i+1 +2j+2m= 0in B′(i)
k−1.
For D(i)
rev (1 ≤i≤k− 2), dividing m = q′2k−i−1 + r′
places0in A(i)
rev,k−1 when r′ < 2k−i−2 and in B′(i)
rev,k−1
whenr ′≥2 k−i−2.
A third obstruction occurs for neighbors of vertex0
across the entire first half of(2k−1,2 k):
Theorem C(First-Half Neighbor Shortcut Collision).
For everyk≥ 4and every even n satisfying2 k−1 + 2 ≤
n≤ 3·2k−2 −2, from originatoru= 2k−1 −1under Theo-
rem 4.1’s reverse-shifted schemeD(1)
rev = (k−2,..., 1,k−
1,k− 2), the shortcut targetw= 2k−2 −1already belongs
Figure 2: (a) Theorem A asymptotic half-loss atn =
2k−1+2,i = 1for k= 4,..., 9(|Ik−1|= 2k−2+2, losing up
to49%of2 k−1). (b) Antipodal excess average broadcast
time ba(Tu)−βa(n−1)at u= n/2: unpatched Sub-case 5
loses+1 /(n− 1), while Theorem D shortcut rerouting
achieves exact0excess.
to B′(1)
rev,k−1 via s = (3 ·2k−2 −n)/2 ∈[1,2k−3]. Hence
redirecting( u→ 0)to( u→w )at round k− 1fails to
inform a new vertex, yielding|Ik−1|<2 k−1.
Proof. Since n is even and2k−1 + 2 ≤n≤ 3 ·2k−2 −2,
s = (3 ·2k−2 −n)/2 ∈[1,2k−3]. In (5) shifted by u at
i= 1,j = 1, the element2k−1 −2s+ u∈B ′(1)
rev,k−1 equals
2k−1 −(3 ·2k−2 −n) + (2k−1 −1) = n+ (2k−2 −1) ≡w
(modn).
3 Constructive Repairs and Gap-
Free Upper-Band MATBGs
Despite Theorem B, a single non-dimensional call across
the existing shortcut edge(2 k−1 −1,2k−2 −1) ∈
E(KG′(n−1))repairs Sub-case 5 universally:
Theorem D(Universal Sub-case 5 Shortcut Rerouting).
Let k≥ 4,2 k−1 < n <2k be even, andu be even with
max(2k−2 +2,n−2k−1 +2) ≤u≤min (2k−1 −2,n−2k−2)
(which holds automatically for every Sub-case 5 originator
whenever n≥ 3 ·2k−2). Under the collision-free standard
schemeD (0)
std = (1,...,k−1,1)onKG(n):
1.0/∈I k−2;
2.v top = 2k−1 −1 ∈Bk−2 via s1 = (u+ 2k−1 −n)/2 ∈
[1,2 k−3];
3. the shortcut partnervpair = 2k−2 −1/∈Ik−1;
4.1 =ϕ 1(0)∈B k−1 vias 2 = (u+ 2)/2∈[1,2 k−2].
Therefore, rerouting the single round-(k−1)call( vtop →0)
across the shortcut edge( vtop,vpair) ∈E (KG′(n− 1))
produces a valid telephone broadcast treeTu in KG′(n−1)
with exact doubling|It|= 2t (0 ≤t≤k− 1), full coverage
|Ik|= n−1, and exact minimum average timeba(Tu) =
βa(n−1).
Proof. (1) Elements ofBk−2 are odd modnwhile0 <u≤
2p+u≤ 2k−2 −2+u<n for p< 2k−3, so0 /∈Ak−2 ∪Bk−2.
(2) Fors1 = (u+2k−1 −n)/2 ∈[1,2k−3],2 s1 −1+ n−u =
2k−1 −1 < n, so vtop ∈B k−2. (3) Ak−1 is even modn
3

--- Page 4 ---
Figure 3: Exact comparison onKG′(11)from antipodal
originator u = 6(certificate C09). (a) Unpatched Sub-
case 5 drops call7 →0at round 3 (|I3|= 7 < 8, ba =
30/11), whereas Theorem D rerouting7 →3restores
|I3|= 8and βa(11) = 29/11. (b)Completevalidtelephone
tree inKG′(11)with the red round-3 shortcut7→3.
while vpair = 2k−2 −1is odd. If2 s−1 +n−u≡ 2k−2 −1
(modn )with1 ≤s≤ 2k−2, then either2s−1+ n−u<n
giving u = 2 s+ n− 2k−2 > n−2k−2 (contradiction),
or2 s− 1 −u = 2k−2 −1giving2 s = u+ 2k−2 > 2k−1
(contradiction). Thus vpair /∈Ik−1. (4) For s2 = ( u+
2)/2 ∈[1,2k−2],2 s2 −1 + n−u = 1 + n≡ 1 ( modn ),
so1 ∈B k−1. By Theorem A(1), D(0)
std doubles without
collision through roundk− 1. Replacing( vtop →0)by
(vtop →vpair)at round k−1yields I′
k−1 = (Ik−1 \{0}) ∪
{vpair}of exact cardinality2k−1, and preserves round-k
full coverage because0’s unique round-k target1 = ϕ1(0)
already lies inI′
k−1. Finally,( vtop,vpair) ∈E (KG′(n−1))
for everyk≥4regardless of the parity ofk−1.
Figure 3 displays the exact Theorem D repair on
KG′(11)from u = 6, restoring ba = 29 /11 = βa(11).
On the sole remaining first-half Sub-case 5 boundary
u= 2k−2, a2-adic shift avoids vertex0entirely (for worst-
case k-round broadcasting; note that shifted schemes in
the first half may still collide inKG(n)per Theorem A,
e.g.|I 6|= 58<64inC12):
Theorem E(2-Adic Boundary Shift foru= 2k−2).For
every k≥ 4and n= 2k−1 + 2m with1 ≤m< 2k−3, write
m= 2s−1(2q+ 1)where s= 1 + v2(m) ∈[1,k− 3]. Then
from originator u = 2k−2 under D(s)
std, vertex0 /∈Ik−1
(modn).
Proof. Since u is even,0 /∈B(s)
k−1 ∪A′(s)
k−1 by parity. For
any0 ≤p < 2k−s−2 and0 ≤j < 2s−1, we have0 <
p2s+1+2j+u≤ 2k−1 −2s+1+2s−2+2k−2 <3·2k−2 <2n,
so congruence to0 ( modn )forces exact equality p2s+1 +
2j+2k−2 = n= 2k−1 +2m. Dividing by2gives p2s+j =
2k−3 + 2s−1(2q + 1); reducing mod2 s (since s≤k−
3 =⇒ 2s |2k−3) yieldsj≡ 2s−1 (mod 2s), contradicting
j <2s−1. Similarly, for1 ≤t≤ 2k−s−2 and1 ≤j≤ 2s−1,
0 <n + 2j+ u−t 2s+1 <2n, so congruence to0 (modn )
forces t2s+1 = 2j+ 2k−2, which reduces mod2s to0 ≡j
(mod 2s), contradicting1≤j≤2 s−1.
Combining Theorem A(3), Theorem D, and universal
neighbor-partner separation yields a complete, gap-free
MATBG theorem on the upper band of [7]:
Theorem F(Gap-Free MATBG Proof for2 k −5and
2k−3).For every k≥ 4, bothKG′(2k−3)and KG′(2k−5)
are minimum average time broadcast graphs with exact
edge countsBa(nodd) = ⌈nodd(k−1)/2⌉. Conversely, for
nodd = 2k −1(k≥3), Labahn’s lower bound [6] satisfies
2(k+1)⌈nodd(k−1)/2⌉< (k+1)nodd(k−1)+nodd, strictly
excluding2 k −1.
Proof. Let n∈{ 2k −4,2k −2}(k≥ 4, son≥ 3 ·2k−2).
By Theorem A(3), all2(k−1)standard and reverse shifts
double without collision through roundk−1in KG(n),
and by [2] coverKG(n)in k rounds. (i)Non-neighbors
of0outside Sub-case 5:By Proposition 3.7 of [ 1], the
assigned shift avoids0through round k−1, so deleting
0leaves |It|= 2 t (t≤k− 1) and |Ik|= n− 1intact.
(ii)Sub-case 5:For n = 2 k −2, Sub-case 5 is empty
(n−2k−1 + 2 = 2k−1 >2k−1 −2). Forn= 2k −4, Sub-
case 5 consists solely ofu= 2k−1 −2 = n/2 >2k−2, which
achieves exact doubling andβa(n− 1)by Theorem D.
(iii)Neighbors of0( u = 2 i −1,1 ≤i≤k− 1):By
the automorphism fu for odd u, an odd vertex w lies
in Ik−1(u)iff w−u∈A k−1(0) ∪B′k−1(0) ( modn ). If
i≤k− 2is odd, Theorem 4.1 uses D(i)
std and shortcut
partner w = 2 i+1 −1, so w−u = 2 i ∈(0,n). Here
p2i+1 + 2j≡ 2j̸≡ 2i (mod 2i+1)( j <2i−1) excludes
A(i)
k−1(0), whilen−s2i+1 +2j′≥n−2k−1 +2 ≥2k−2 +2 >
2i excludes B′(i)
k−1(0) + n. If i≥ 2is even or i= k−1is
odd, Theorem 4.1 usesD(r)
rev (r = k−i∈ [1,k− 2]) and
w = 2 i−1 −1, so w−u≡n− 2i−1 (modn ). In (5),
j2i + 2p≡ 2p̸≡ 2i−1 (mod 2i)( p < 2i−2) excludes
A(r)
rev,k−1(0) + n, while j′2i −2s≤ 2k−1 −2 < 2k−1 ≤
n−2i−1 excludes B′(r)
rev,k−1(0). BecauseDis collision-free
and ϕαk−1 (u) = 0, necessarily0 /∈Ik−2; redirecting( u→
0)to( u→w )at round k−1preserves |Ik−1|= 2k−1 and
places0’s unique round-k target ϕαk (0) = w already into
I′
k−1. Finally,( nd)/2 −d + ⌈d/2⌉= ⌈(n−1)d/2⌉matches
the MATBG degree lower bound. For nodd = 2 k −1
(k≥ 3),2 ⌈nodd(k−1)/2⌉≤n odd(k−1) + 1; multiplying
by k + 1and applying k + 1 < 2k −1 = nodd gives
2(k+ 1)⌈nodd(k−1)/2⌉< (k+ 1)nodd(k−1) + nodd, so
Ba(2k −1) ≥B (2k −1) >⌈(2k −1)(k−1)/2⌉by [6].
4 Machine-Checked Lean 4 Kernel
and Zero-Float Audit
We separate universal symbolic verification from finite
explicit schedule validation:
Lean 4.35.0 Structural Kernel.The file lean/Knode
lMatbgCert.lean defines the modular Knödel neighbor
map kgNeighbor directly and proves all 24 universal theo-
rems in Table 1 without Mathlib or external dependencies.
4

--- Page 5 ---
Table 1: All 24 universal modular-arithmetic theorems formally verified inlean/KnodelMatbgCert.lean (Lean 4.35.0,
zero external dependencies,0 sorry,0custom axioms,0 Classical.choice,0warnings; axioms strictly [propext,
Quot.sound]).
# Lean 4 Theorem Identifier Universally Quantified Formal Statement (all variables inN)
1kg_neighbor_involution0<n∧v <n=⇒ϕ d(ϕd(v)) =v
2lemma31_step_A_to_Bt≥1,p<2 t−1 =⇒ϕt+1((2p+u) modn) = (2(2t −p)−1 +n−u) modn
3lemma31_step_B_to_At≥1,1≤s≤2 t−1 =⇒ϕt+1((2s−1 +n−u) modn) = (2(2t −s) +u) modn
4lemma31_collision_free2|n,t≤k−1,2 k−1 <n=⇒A t,Bt injective and disjoint modn
5theoremA_sharp_collision_witnessk≥4,1≤i≤k−2,2 i + 4<2k−1 =⇒exactA k−1 ∩(B′k−1 +n)witness atn= 2 k −2 i −4
6theoremA_collision_free_above_thresholdn>2 k −2 i −4 =⇒p2 i+1 + 2j+s2 i+1 <n+ 2j′(std shift zero collisions)
7theoremA_extreme_half_lossk≥4,1≤p≤2 k−3 −1,n= 2 k−1 + 2 =⇒4p=n+ 2−4(2 k−3 + 1−p)
8theoremB_antipodal_std_rev_hits_zerok≥4,2 k−1 <4m<2 k =⇒m<2 k−2 ∧(2m+ 2m) mod 4m= 0∧(2m−2m) mod 4m= 0
9theoremB_antipodal_all_std_shifts_hit_zerok≥4,4m<2 k,1≤i≤k−2 =⇒ ∃witness inA (i)
k−1 orB′(i)
k−1 hitting0 (mod 4m)
10theoremB_antipodal_all_rev_shifts_hit_zerok≥4,4m<2 k,1≤i≤k−2 =⇒ ∃witness in Lemma 3.4A k−1 orB′k−1 hitting0 (mod 4m)
11theoremC_first_half_shortcut_already_informedk≥4,2|n,2 k−1 + 2≤n≤3·2 k−2 −2 =⇒s= (3·2 k−2 −n)/2∈[1,2 k−3]hitsw= 2 k−2 −1
12theoremD_subcase5_zero_not_in_I_km2Sub-case 5 hypotheses=⇒0/∈A k−2 ∪Bk−2 (modn)
13theoremD_subcase5_sender_in_I_km2Sub-case 5 hypotheses=⇒s 1 = (u+ 2k−1 −n)/2∈[1,2 k−3]places2 k−1 −1∈B k−2
14theoremD_subcase5_shortcut_target_uninformed2 k−2 <u≤n−2 k−2,2|n,2|u=⇒2 k−2 −1/∈Ak−1 ∪Bk−1 (modn)
15theoremD_subcase5_one_in_I_km12|u,u≤2 k−1 −2,2 k−1 <n=⇒s 2 = (u+ 2)/2∈[1,2k−2]places1∈B k−1
16theoremE_2adic_shift_avoids_zerok≥4,1≤s≤k−3,m= 2 s−1(2q+ 1)<2 k−3 =⇒0/∈A(s)
k−1 ∪B′(s)
k−1 (modn)
17theoremF_kg_prime_edge_count2|n,n≥2,d≥1 =⇒(nd)/2−d+ (d+ 1)/2 = ((n−1)d+ 1)/2
18theoremF_labahn_lower_bound_exceeds_ceilingk≥3,n= 2 k −1 =⇒2(k+ 1)⌈n(k−1)/2⌉<(k+ 1)n(k−1) +n
19theoremF_upper_band_subcase5_characterizationk≥4 =⇒Sub-case 5 empty at2 k −2; uniqueu= 2k−1 −2>2 k−2 at2 k −4
20theoremD_second_half_eliminates_boundaryk≥4,3·2 k−2 ≤n,n−2 k−1 + 2≤u=⇒2 k−2 <u
21theoremA_rev_collision_free_above_thresholdn>2 k −2 k−i−1 −4 =⇒j ′2k−i +j2 k−i + 2p<n+ 2s(rev shift zero collisions)
22lemma33_rev_unshifted_injective1≤t≤k−1,2 k−1 <n=⇒A rev
t ={(n−p2 k−t) modn}injective modn
23theoremF_neighbor_partner_uninformed_stdn≥3·2 k−2,1≤i≤k−2 =⇒2 i /∈A(i)
k−1(0)and2 i <n+ 2j′−s2 i+1
24theoremF_neighbor_partner_uninformed_revn≥3·2 k−2,2≤i≤k−1 =⇒2 i−1 /∈−A(k−i)
rev (0)andj ′2i −2s<n−2 i−1
Table 2: Canonical certificate suite ( C01–C16) audited by the AST-verified zero-float Python engine
KNODEL-MATBG-CERT-1.0.
ID Mode / Target Theorem Instance Parameters Exact Audited Metric Outcome
C01Mode 1 (Thm. A sharp)k= 5,n= 26,i= 1(std)|I 4|= 14<16, witnessx= 12(p= 3,j= 0,s= 4,j ′= 1) PASS
C02Mode 1 (Thm. A sharp)k= 6,n= 52,i= 3(std)|I 5|= 30<32, witnessx= 22(p= 1,j= 3,s= 2,j ′= 1) PASS
C03Mode 1 (Thm. A half-loss)k= 7,n= 66,i= 1(std)|I 6|= 34, exact loss30 = 25 −2(15 even + 15 odd) PASS
C04Mode 1 (Thm. A clean band)k= 7,n= 124(all 12 shifts)|I t|= 2t (t≤6),0collisions across all 12 shifts PASS
C05Mode 2 (Thm. B antipodal)k= 4,n= 12,u= 6 6/6dimensional schemes hit0by round 3 PASS
C06Mode 2 (Thm. B antipodal)k= 6,n= 52,u= 26 10/10dimensional schemes hit0by round 5 PASS
C07Mode 2 (Thm. B antipodal)k= 7,n= 124,u= 62 12/12dimensional schemes hit0by round 6 PASS
C08Mode 2 (Thm. C first-half)k= 6,n= 46,u= 31,w= 15w= 15∈I 5 (s= 1);0uninformed neighbors ofuPASS
C09Mode 3 (Thm. D reroute)k= 4,n= 12,u= 6(KG ′(11)) Shortcut7→3:b a = 29/11 =βa(11)vs unpatched30/11PASS
C10Mode 3 (Thm. D reroute)k= 6,n= 52,u= 26(KG ′(51)) Shortcut31→15:b a = 81/17 =βa(51)vs244/51PASS
C11Mode 3 (Thm. D reroute)k= 7,n= 124,u= 62(KG ′(123)) Shortcut63→31:b a = 734/123 =βa(123)vs245/41PASS
C12Mode 3 (Thm. E2-adic)k= 7,n= 72,u= 32(m= 4) Shifts= 1 +v 2(4) = 3:0/∈I6,|I 7|= 72PASS
C13Mode 4 (Thm. F MATBG)KG ′(11)(2 4 −5,17edges) All11/11originators exactβ a(11) = 29/11(1 reroute) PASS
C14Mode 4 (Thm. F MATBG)KG ′(27)(2 5 −5,54edges) All27/27originators exactβ a(27) = 104/27(1 reroute) PASS
C15Mode 4 (Thm. F MATBG)KG ′(59)(2 6 −5,148edges) All59/59originators exactβ a(59) = 291/59(1 reroute) PASS
C16Mode 4 (Thm. F MATBG)KG ′(61)(2 6 −3,153edges) All61/61originators exactβ a(61) = 303/61(0 reroutes) PASS
Table 1 (#5) enforces2i+4 <2k−1 (excluding the degener-
ate point(k,i) = (4,2)where2 4 −22 −4 = 8 = 23 lies out-
side(2 3,24)); rows #21–#24 formally verify reverse-shift
separation, D(0)
rev injectivity, and neighbor-partner separa-
tion across alln≥ 3 ·2k−2. Every theorem passes#print
axioms using only[propext, Quot.sound]—zero sorry,
zero custom axioms, zero Classical.choice (using a
constructive Euclidean division lemma in place of Lean’s
classical Nat.div_lt_of_lt_mul ), and zero compiler
warnings.
Zero-Float Python Verifier and Adversarial Suite.
The engine src/knodel_matbg_verifier.py enforces
strict integer and lowest-terms fractions.Fraction
arithmetic via an AST audit banning float/complex liter-
als, float(), complex(), true-division/, exponentiation
**, and floating-point libraries. Across Modes 1–4 (Ta-
ble 2), it builds explicit graphsKG(n)and KG′(n−1),
validates telephone-model matching constraints end-to-
end (including both unpatched and rerouted schedules in
Mode 3), and checks all 16 certificates (C01–C16). The
test suitetests/test_verifier.py executes 48 checks
in under1 s, including 23 adversarial forgery-rejection
tests (rejectingbool-as-int, unreduced fractions, double
calls per round, non-edge calls, excludednodd = 15, non-
bool optional flags, ** operators, and falsely claiming
Theorem 4.1’s dimensional schedule is a MATBG on the
colliding orderKG′(25)), plus a first-half regression check
onKG ′(17).
5

--- Page 6 ---
5 Scope, Open Direction, and Re-
producibility
Scope and Open Problem Status.Our results con-
firm that Altay, Fakharan, and Harutyunyan’s broadcast-
function boundB(n−1) ≤⌈(n−1)(k−1)/2⌉(evenn̸= 2k)
holds, while demonstrating that Section 5’s MATBG claim
is unproved for intermediate ordersn∈ [2k−1 + 2,2k −6]
where shifted dimensional schemes collide inKG(n). The-
orem F rigorously closes the MATBG problem on the
upper band nodd ∈{2k −5,2k −3}for all k≥ 4(re-
lying on Bermond et al. [2] for k-round coverage of di-
mensional schemes onKG(n)and Proposition 3.7 of [1]
for0 /∈Ik−1 on non-neighbor originators outside Sub-
case 5, with all collision-freedom, antipodal rerouting, and
neighbor-partner separation theorems machine-checked in
Lean 4). Constructing a universal collision-free MATBG
family across the remaining interior band[3·2k−2,2k−6]
remains an open problem.
Reproducibility.All Lean 4 proofs, Python verification
code, 16JSONcertificateswith MANIFEST.sha256, 48unit
and forgery tests, and figure scripts are archived under
MIT license atgithub.com/lluiseriksson/knodel-m
atbg-obstruction-repair (v1.0.0) and reproduce
via lake build, python src/knodel_matbg_verifier.
py certificates, andpytest -q under Lean 4.35.0 and
Python 3.12+.
References
[1] Sirma Cagil Altay, Mohammadhossein Fakharan, and
HovhannesA.Harutyunyan. Ageneralupperboundon
broadcast functionB(n)using Knödel graph, Novem-
ber 2026. arXiv:2611.34167v1.
[2] Jean-Claude Bermond, Hovhannes A. Harutyunyan,
Arthur L. Liestman, and Stéphane Perennes. A note on
the dimensionality of modified Knödel graphs.Inter-
national Journal of Foundations of Computer Science,
8(2):109–116, 1997.
[3] Arthur M. Farley. Minimal broadcast networks.Net-
works, 9(4):313–332, 1979.
[4] Hovhannes A. Harutyunyan. An efficient vertex addi-
tion method for broadcast networks.Internet Mathe-
matics, 5(3):211–225, 2008.
[5] Walter Knödel. New gossips and telephones.Discrete
Mathematics, 13(1):95, 1975.
[6] Roger Labahn. A minimum broadcast graph on 63
vertices.Discrete Applied Mathematics, 53(1–3):247–
250, 1994.
[7] Arthur L. Liestman and Nataša Pržulj. Minimum
average time broadcast graphs.Parallel Processing
Letters, 8(2):139–147, 1998.
6
