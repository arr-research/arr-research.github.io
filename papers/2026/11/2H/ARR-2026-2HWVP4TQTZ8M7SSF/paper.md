# Exact Radial Excursion Thresholds, p-Band Tower Conservation, the Unconditional Las Vegas Omega(N log log log N) Octave-Decision Barrier, and 172-Order-of-Magnitude Outer Threshold Sharpening for Almost-Linear Single-Source Shortest Paths

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-2HWVP4TQTZ8M7SSF` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/paper136-almost-linear-sssp-barriers (`v1.0.0`)  
**Canonical PDF SHA-256:** `39f061da5b6c2ebf36c7eae0d43291c40f4af0c4af9e99f23d1dc702347d179c`

## Abstract

Following Iman Gholami and MohammadTaghi Hajiaghayi's breakthrough O(m + n log log log n) randomized comparison-addition algorithm for undirected real-weighted single-source shortest paths (arXiv:2611.34911v1), we establish four exact structural, lower-bound, and non-asymptotic threshold results backed by 20 constructive Lean 4.36.0 theorems (0 sorry, 0 Classical.choice, 0 warnings), 16 AST-audited zero-float SHA-256 certificates, and 56 adversarial tests: (1) Exact generalized radial excursion threshold and tightness: combining both flanks of a radial geodesic peak under detour ratio d_e <= alpha * w_e yields the two-sided lower bound L >= (2M - J_x - J_y)/(1 + alpha), proving the exact critical shell ratio K_crit(alpha) = 2/(1 - alpha) with a tight 3-vertex witness at equality; at alpha = 1/2, K_crit(1/2) = 4, minimal integer K = 5, and minimal power-of-two K = 8 (halving Lemma 8.1's K = 16, reducing Lemma 8.2's bottleneck constant 4K^2 h by 4x and K^4 by 16x); (2) p-band disjoint-set and multi-pass MST tower conservation: extending Lemma 3.6 to arbitrary fixed p >= 1 rank bands yields W_p(k, Q) <= pQ + k(b_1 + p - 1) = O(pQ + k log^(p) k), proving that disjoint-set and MST subroutines push strictly below log log log k (e.g., p = 4 achieves O(Q + k log^(4) k)); (3) Unconditional Las Vegas Omega(N log log log N) octave-decision barrier: combining exact binary-tree external path length epl(T) >= (k+2)L - 2^(k+1), dyadic midpoint injectivity (L >= M^N), and Yao's minimax principle proves that every Las Vegas linear comparison-addition algorithm classifying N real weights into M = Theta(log log N) dyadic octaves requires at least N * floor(log_2 M) = Omega(N log log log N) expected comparisons; and (4) Moore 2-core peeling halving and 172-order outer threshold sharpening: halving Lemma 6.2's critical-edge witness path length from 4*ceil(log_2(t+2))+3 to 2r (girth > 2r+1, 3*2^r - 2 > t) while tightening |E| <= 2t - 3, and certifying inside Lean 4 that Algorithm 8's N > L_N^64 guard activates only at N_0(64) = 589^64 + 1 (~1.938e177), whereas b = L_N^4 already absorbs t*log^4(t+2) = O(N) and drops the exact crossover >172 orders of magnitude to N_0(4) = 17^4 + 1 = 83,522 (and local 2*L_N^4 to 209,953).

## Full Extracted Text

--- Page 1 ---
Exact Radial Excursion Thresholds,p-Band Tower
Conservation,
the Unconditional Las VegasΩ(Nlog log logN)
Octave-Decision Barrier,
and 172-Order-of-Magnitude Outer Threshold
Sharpening
for Almost-Linear Single-Source Shortest Paths
Lluis Eriksson
Independent Researcher
github.com/lluiseriksson/paper136-almost-linear-sssp-barriers
November 27, 2026
Abstract
In a landmark breakthrough for the real-weighted comparison–addition model, Gho-
lami and Hajiaghayi [ 7] solved undirected single-source shortest paths (SSSP) in O(m +
nlog log logn ) expected time, surpassing the O(mα(m, n) + nmin{logn,log logr} ) bound of
Pettie–Ramachandran [9], the O(m√lognlog logn ) bounds of Duan–Mao–Shu–Yin [ 3] and
Yan [12], and the O(m√logn (log lognlog log logn )1/4) bound of Kadria–Roditty [ 8]. Four
structural questions remained open: (i) what is theexactsharp shell-ratio threshold forbidding
radial geodesic excursions (where Lemma 8.1 uses K = 16); (ii) whether the log log logn
overhead originates in the 3-band disjoint-set/MST hierarchy (Lemmas 3.5–3.6) or in an
intrinsic real-register decision bottleneck; (iii) whether the critical-edge witness path length of
Lemma 6.2 can be halved while tightening |E| ≤2t; and (iv) what exact graph size activates
Algorithm 8’s outerN > L64
N guard (LN :=⌈log 2(N+ 2)⌉).
We answer all four questions with complete mathematical proofs whose core algebraic,
combinatorial, tree-depth, and threshold kernels are machine-checked by 20 constructive
Lean 4.36.0 theorems (zero sorry, zero Classical.choice, zero external imports) alongside
an AST-audited zero-float exact-rational verifier generating 16 SHA-256 certificates and passing
56 adversarial tests:
1. Exact Generalized Radial Excursion Threshold & Tightness.Combining both
flanks of a radial geodesic peak yields the two-sided lower bound L≥ 2M−Jx−Jy
1+α under
detour ratio de ≤αw e, proving the exact critical threshold Kcrit(α) = 2
1−α with a tight
3-vertex witness at equality. At α = 1
2 , this gives Kcrit(1/2) = 4, minimal integer K = 5,
and minimal power-of-two K = 8 (halving Lemma 8.1’s K = 16, cutting Lemma 8.2’s
bottleneck constant 4K 2hby 4×andK 4 by 16×).
2.p -Band Tower Conservation Law.Extending Lemma 3.6 to any fixed p≥ 1 rank
bands gives exact work Wp(k, Q) ≤pQ + k(b1 + p− 1) = O(pQ + klog (p) k), proving that
disjoint-set/MST subroutines push arbitrarily far down the iterated-logarithm hierarchy
(p= 4 already achievesO(Q+klog (4) k)) and arenotthe source of the log log lognwall.
3. Unconditional Las VegasΩ( Nlog log logN )Octave-Decision Barrier.Via exact
binary-tree external path length epl(T) ≥ (k + 2)L− 2k+1 (2k ≤L ), dyadic midpoint
injectivity (L≥M N ), and Yao’s minimax principle, we prove thateveryLas Vegas linear
comparison–addition decision tree classifying N real weights into M = Θ(log logN ) dyadic
octaves incurs expected depth≥N⌊log 2 M⌋= Ω(Nlog log logN).
1
AIRR:ARR-2026-2HWVP4TQTZ8M7SSF v1  [Mathematical physics]  27 Nov 2026  ·  AIRR.SCIENCE

--- Page 2 ---
4. Moore 2-Core Peeling Halving & 172-Order-of-Magnitude Outer Threshold
Sharpening.Exact minimum-degree-3 Moore BFS peeling halves Lemma 6.2’s critical-
edge witness path length from g = 4⌈log2(t + 2)⌉ + 3 (girth ≥g + 2) to g = 2r (girth
≥ 2r + 2 > 2r + 1, where 3 · 2r − 2 > t) while tightening |E| ≤2t− 3. Inside Lean 4, we
certify that Algorithm 8’s N > L64
N guard falls back to O(N2 + m) scan-Dijkstra up to
N0(64) = 58964 + 1 ≈ 1.938 × 10177, whereas b = L4
N already absorbs tlog 4(t + 2) = O(N)
and drops the exact crossover by > 172 orders of magnitude to N0(4) = 174 + 1 = 83,522
(and local 2L4
N to 209,953).
1 Introduction
Since Dijkstra’s algorithm [1] and Fibonacci heaps [6] established the O(m+nlogn ) sorting barrier
for real-weighted SSSP, a central question in graph algorithms has been how close comparison–
addition algorithms can approach Thorup’s linear-time O(m+n) integer-weight bound [11]. Pettie
and Ramachandran [9] broke the sorting barrier for sparse real-weighted undirected graphs; recent
breakthroughs by Duan, Mao, Shu, and Yin [ 3, 2, 4], Yan [ 12], and Kadria and Roditty [ 8]
successively reduced the exponent of logn , culminating in Gholami and Hajiaghayi’s randomized
Las Vegas O(m+nlog log logn ) undirected SSSP algorithm [7] (built on FRT-style tree metrics [5],
Tarjan-style banded union–find [10], and dyadic octave calendars).
In this work we isolate the exact algebraic thresholds, lower-bound bottlenecks, and non-
asymptotic crossovers governing every component of [7].
2 Exact Generalized Radial Excursion Threshold and Tightness
In Lemmas 7.2 and 8.1 of [ 7], every surviving radial edge e = xy carries a detour certificate
de ≤αw e (α = 1
2 in [7]), obeys the radial deletion test we ≤J x + Jy + de, and satisfies the
auxiliary triangle inequality |Ju −J v| ≤we + de ≤ (1 +α)we for the owner coordinate J. Gholami
and Hajiaghayi apply this Lipschitz bound on onlyoneflank from an endpoint to the peak M,
requiring K > 3+α
1−α (= 7 at α = 1
2 ) and fixing K = 16. Exploitingbothflanks halves the exact
critical threshold and yields a tight characterization.
Theorem 2.1(Exact Generalized Radial Excursion Threshold and 3-Vertex Tightness).Let
α = p/q∈ [0, 1)( p, q∈N ,0 ≤p < q ), and let P = ( v0, . . . , vℓ)be a radial segment with
endpoint coordinates Jx = Jv0, Jy = Jvℓ, peak coordinate M = maxi Jvi > 0, and total length
L= Pℓ
i=1 w(vi−1, vi), where every edge satisfiesd e ≤αw e and|J u −J v| ≤(1 +α)we.
1. Two-Sided Peak Lower Bound (Leanthm01):Splitting P at a peak vertex z (Jz = M)
intoL=L xz +L zy yields
L≥ M−J x
1 +α + M−J y
1 +α = 2M−J x −J y
1 +α .(1)
2. Exact Critical Shell Ratio (Leanthm02, thm05, Certs. C01, C03–C04):Every surviving
radial edge obeysw e ≤ 1
1−α(Jx +J y). WheneverJ x, Jy ≤M/Kwith
K > Kcrit(α) := 2
1−α ,(2)
the certified pivot detour strictly shortens P: Jx + Jy + αL < L, forbidding P from appearing
on any shortest path.
3. 3-Vertex Tightness (Leanthm03, Cert.C01):At K = Kcrit(α), the 3-vertex path x−z−y
with Jx = Jy = 1, M = Kcrit(α) = 2
1−α, and w(x, z) = w(z, y) = M−1
1+α = 1
1−α satisfies
|Jz −J x| = (1 + α)w(x, z)and exact equality Jx + Jy + αL = L. Thus Kcrit(α)cannot be
reduced by anyε >0.
2

--- Page 3 ---
Figure 1: (a) Exact two-sided radial excursion threshold Kcrit(α) = 2
1−α versus the one-sided
Lemma 8.1 style bound 3+α
1−α, highlighting Kcrit(1/2) = 4, minimal power-of-two K = 8, and
Lemma 8.1’sK= 16 (Theorem 2.1). (b) Resulting 2×, 4×, and 16×constant reductions.
4. Sharpening Lemma 8.1 fromK = 16to K = 8(Lean thm04, Cert. C02):At α = 1
2 ,
Kcrit(1/2) = 4, the minimal valid integer shell ratio is K = 5, and the minimal power-of-two
shell ratio is K = 8, cutting Lemma 8.2’s bottleneck constant4 K2h by4 × (from1024 h to
256h) andK 4 by16×(from65,536to4,096).
Proof. (1) Telescoping |Ju −J v| ≤(1 + α)we from x to z gives M−J x ≤ (1 + α)Lxz, and from z
to y gives M−J y ≤ (1 + α)Lzy; summing yields (1 + α)L≥ 2M−J x −J y (cleared-denominator
form in Leanthm01).
(2) Under the deletion test we ≤J x + Jy + αwe, rearranging gives (1 −α )we ≤J x + Jy
(Lean thm05). For the excursion, Jx + Jy ≤ 2M
K < (1 −α )M whenever K > 2
1−α. Multiplying by
2 and rearranging gives (1 + α)(Jx + Jy) < (1 −α )(2M−J x −J y) ≤ (1 −α )(1 + α)L, so dividing
by 1 +α >0 yieldsJ x +J y <(1−α)L, i.e.J x +J y +αL < L(Leanthm02).
(3) Clearing denominators by multiplying all lengths by q−p > 0 gives Jx = Jy = q−p ,
M = 2q, Lxz = Lzy = q: then KJx = K(q−p ) = 2q = M, q(M−J x) = q(q + p) = (q + p)Lxz,
and (q−p)(L xz +L zy) = 2q(q−p) =q(J x +J y) identically (Leanthm03).
(4) Substituting p = 1, q= 2 gives Kcrit(1/2) = 4, so K = 5 is the minimal valid integer and
K = 8 is the minimal valid power of two; 4 · 162 = 1024 = 4 · (4 · 82) and 164 = 65536 = 16 · 84
(Leanthm04).
3p -Band Disjoint-Set and Multi-Pass MST Tower Conservation
Lemma 3.6 of [ 7] partitions union-by-rank heights into p = 3 bands with b3 = Lk + 1, b2 =
⌈log2(b3 + 1)⌉, and b1 = ⌈log2(b2 + 1)⌉ = Θ(log log logk) to achieve O(Q + klog log logk ) work for
Q operations on k items (matching Lemma 3.5’s 3-pass MST). We prove that this conservation
law extends verbatim to arbitrary fixed p≥ 1 bands, demonstrating that union–find and MST are
notthe cause of the log log lognterm.
Theorem 3.1( p-Band Tower Conservation Law).Let k≥ 1, Q≥ 0, and let0 = b0 < b1 ≤ ··· ≤bp
be integer rank-band boundaries with2 bp > ksatisfying the tower-collapse invariant bi −bi−1 ≤ 2bi−1
for every2≤i≤p.
1. Exponential Rank-Count Bound (arithmetic kernel in Leanthm06, Cert. C07):
Every root first attaining rank r has at least2 r descendants, so at most ⌊k/2r⌋ vertices ever
reach rankr.
3

--- Page 4 ---
2. Exact p-Band Work Conservation (Leanthm07–thm10, Certs. C05–C06, C08):Charg-
ing at most p band-hops per operation and at most bi −bi−1 reparentings to each vertex reaching
rankb i−1 bounds total work by
Wp(k, Q;b)≤pQ+kb 1 +
pX
i=2
 k
2bi−1

(bi −b i−1)≤pQ+k(b 1 +p−1).(3)
Setting bp = Lk + 1and bi−1 = ⌈log2(bi + 1)⌉ gives b1 = Θ(log(p) k): for p = 3this recovers
Lemma 3.6’s3 Q+k(b1 +2) = O(Q+klog (3) k), while any fixed p≥ 4strictly beats log log logk
(e.g. p = 4gives4 Q+k(b1+3) = O(Q+klog (4) k)); reaching b1 = O(1)via fixed bands takes p =
Θ(log∗ k)bands ( O((Q+k) log∗ k)), whereas full path compression reaches O((Q+k)α(k))[ 10].
Proof. (1) By induction on rank promotions, every root first attaining rank r has at least 2 r
original items, and the sets at first promotions of distinct roots to rank r are pairwise disjoint.
Thus if c distinct roots reach rank r, then c· 2r ≤k , which gives c≤ ⌊k/2r⌋ (the division
implication is checked in Leanthm06).
(2) For each upper band i∈ {2, . . . , p}, since bi −b i−1 ≤ 2bi−1 and ⌊k/2bi−1⌋ ·2bi−1 ≤k ,
we have ⌊k/2bi−1⌋(bi −b i−1) ≤k (Lean thm07). Induction over the p− 1 upper bands yieldsPp
i=2⌊k/2bi−1⌋(bi −b i−1) ≤ (p− 1)k (Lean thm08–thm10), giving Wp ≤pQ + k(b1 + p− 1). With
bi−1 = ⌈log2(bi + 1)⌉, 2bi−1 ≥b i + 1 > bi −b i−1, so the invariant holds automatically for every
p≥1.
4 Unconditional Las VegasΩ( Nlog log logN )Octave-Decision Bar-
rier
Where, then, does the nlog log logn cost in [ 7] genuinely live? In Lemmas 7.3 and 8.4, each
of N vertices must locate its real-valued radius rv (and upper marker Rv) inside a dyadic grid
spanning M = Θ(log(b + 4)) = Θ(log logN ) octaves [2j, 2j+1) using only comparison–addition
operations on opaque real registers (no bit-extraction or integer-logarithm instructions). We
prove an unconditional Las Vegas lower bound showing thatnorandomized comparison–addition
algorithm can classify N real weights into M dyadic octaves in fewer than N⌊log2 M⌋ expected
comparisons.
Theorem 4.1(Unconditional Las Vegas Octave-Decision Barrier).Consider the comparison–
addition linear decision tree model overRN , where each internal node branches on a linear inequality
⟨a, x⟩ ≤c(a∈R N , c∈R), and an M-octave classifier outputs for every input x∈ [1, 2M )N the
exact vectoroct(x) = (⌊log 2 x1⌋, . . . ,⌊log2 xN ⌋)∈ {0, . . . , M−1}N .
1. Exact Binary-Tree External Path Length (Leanthm11–thm12, Cert. C09):Every
binary decision treeTwithL≥1leaves and everyk∈Nobeys
epl(T)≥(k+ 2)L−2 k+1,(4)
with equality on complete/almost-complete trees (verified exhaustively across all Catalan trees
up toL= 10). WheneverL≥2 k,epl(T)≥kL.
2. Dyadic Midpoint Injectivity (Cert. C11; power-of-two cardinality step in
Lean thm13):Let MN := {3
2 · 2j : 0 ≤j < M}N be the grid of MN dyadic octave midpoints.
No two distinct points x, y∈ MN can reach the same leaf of any valid linear decision tree T;
henceL(T)≥M N .
3. Las Vegas Expected-Depth Lower Bound (weighted-tree kernel in Leanthm14–thm15,
Certs. C10, C12):ForanyLas Vegas probability distribution D over valid linear decision
4

--- Page 5 ---
Figure 2: (a) p-band disjoint-set lowest threshold b1(k, p) for p = 2, 3, 4, proving union–find/MST
push down to O(log(p) k) (Theorem 3.1). (b) Exact minimum expected comparison depth
(k+2)L−2k+1
L across distinct octave profilesL=M N (Theorem 4.1).
trees (rational weightsw i ≥0, P
i wi =W >0) withM≥2 b,
max
x∈MN
ET∼D [depthT (x)]≥E x∼Unif(MN ), T∼D[depthT (x)]≥ (k+ 2)M N −2 k+1
MN ≥bN,(5)
where k = ⌊Nlog 2 M⌋ ≥bN . For Gholami–Hajiaghayi’s grid width bsep = Le
N (e≥ 1),
M = ⌈log2(Le
N + 4)⌉ = Θ(elog logN ), forcingΩ( Nlog log logN )expected comparisons for
every Las Vegas octave classifier.
Proof. (1) We prove (k + 2)L(T) ≤epl (T) + 2k+1 for all T and all k∈N by structural induction
on T (Lean thm11). If T is a leaf ( L = 1 ,epl = 0), then k + 2 ≤ 2k+1 holds for all k≥ 0.
If T = node(T1, T2): for k = 0, L(u) ≤epl (u) + 1 holds by induction for every tree u, so
2(L1 + L2) ≤epl 1 + epl2 +L1 + L2 + 2 = epl(T) + 21; for k = m + 1, applying the induction
hypothesis at m to T1 and T2 and summing gives (m + 3)(L1 + L2) = (m + 2)L1 + (m + 2)L2 +
L1 + L2 ≤epl 1 + epl2 +L1 + L2 + 2 · 2m+1 = epl(T) + 2m+2. If L≥ 2k, then 2 k+1 ≤ 2L, so
epl(T)≥(k+ 2)L−2L=kL(Leanthm12).
(2) Each leaf ℓ of a linear decision tree corresponds to a convex polyhedron Pℓ ⊆R N (an
intersection of open/closed halfspaces). If two distinct midpoints x, y∈ MN lay in Pℓ, then Pℓ
would contain the entire line segment [ x, y], on which oct(·) takes at least two distinct values
(since xi ̸= yi implies [xi, yi] crosses an octave boundary 2 j), contradicting validity of the output
at leaf ℓ. Thus x7→leaf T (x) is injective on MN , forcing L(T) ≥M N (and 2bN ≤L (T) whenever
M≥2 b, Leanthm13).
(3) For every valid tree Ti, let T′
i be the binary tree obtained by deleting all unreached leaves
not in leafTi(MN ) and contracting every resulting degree-1 internal node onto its surviving
child. Pruning never increases the depth of any retained leaf and leaves exactly MN leaves,
so P
x∈MN depthTi(x) ≥epl (T′
i ) ≥ (k + 2)MN − 2k+1 ≥bN·M N by Part (1). Taking the
wi-weighted convex combination over T′
i yields P
i wi epl(T′
i ) ≥W·bN·M N (the weighted-tree
expectation inequality on pruned trees with L(T′
i ) ≥M N is checked in Lean thm14), and the
maximum over x∈ MN is at least the uniform average. Finally, when M≥e· 2c with e≥ 1
and c = ⌊log2 log2 LN ⌋ = Θ( log log logN), we have M≥ 2c (Lean thm15), establishing the
Ω(Nlog log logN) barrier.
5

--- Page 6 ---
5 Moore 2-Core Peeling Halving and 172-Order Outer Threshold
Sharpening
Finally, we sharpen two non-asymptotic parameters of [ 7]: Lemma 6.2’s critical-edge witness path
length g = 4⌈log2(t + 2)⌉+ 3 (which implies girth ≥g + 2), and Algorithm 8’s outer fallback guard
N≤L 64
N .
Theorem 5.1(Moore 2-Core Peeling Halving and Exact Outer/Local Thresholds).Let LN :=
⌈log2(N+ 2)⌉forN≥1.
1. Halved Critical-Edge Witness Path Length & Tighter|E| ≤2t− 3(Moore count and
peeling arithmetic in Leanthm16–thm17, Cert. C13):In any simple graph G = (V, E)
on t≥ 2vertices with witness path length g = 2r (hence girth ≥g + 2 = 2r + 2 > 2r + 1),
where r := min{r≥ 0 : 3 · 2r − 2 > t}= ⌈log2
t+3
3 ⌉ (halving Lemma 6.2’s witness path length
4⌈log2(t + 2)⌉ + 3), every nonempty induced subgraph has a vertex of degree ≤ 2, whence
|E| ≤2t− 3 < 2t. (The Petersen graph on t = 10vertices with girth5attains3 · 22 − 2 = 10,
showing tightness of the Moore threshold.)
2. Exact Outer Guard of Algorithm 8 (Leanthm18, Cert. C14):The exact minimum
vertex count satisfyingN > L64
N is
N0(64) = 589 64 + 1≈1.938×10 177 (LN0(64) = 589,178 decimal digits).(6)
Foreverygraph with N≤ 58964 vertices (over10 97 times the number of atoms in the observable
universe), Algorithm 8 executes Line 5 (O(N 2 +m)scan-based Dijkstra).
3. 172-Order-of-Magnitude Sharpening viab = L4
N & Exact Local Guard (Leanthm19–
thm20, Certs. C14–C16):Replacing b = L64
N by b = L4
N keeps the Steiner-closed pivot count
t≤max{ 1, 2⌊N/L4
N ⌋} = O(1 + N/L4
N )small enough to absorb tlog 4(t + 2) = O(N)across
Lemma 6.8 and all outer-hierarchy steps of Lemma 8.4, while dropping the exact outer crossover
by>172orders of magnitude to
N0(4) = 17 4 + 1 = 83,522 (L N0(4) = 17).(7)
Similarly, the exact minimum vertex count for the local construction guard N > 2L4
N is
Nloc = 2·18 4 + 1 = 209,953(L Nloc = 18).
Proof. (1) Suppose a nonempty induced subgraph H⊆G has minimum degree ≥ 3. A breadth-
first tree rooted at any v∈V (H) of depth r has no cycles (since girth > 2r + 1), so it contains 1
vertex at depth 0, ≥ 3 vertices at depth 1, and ≥ 3 · 2j−1 vertices at depth j∈ {1, . . . , r}, totaling
at least 1 + Pr
j=1 3 · 2j−1 = 3 · 2r − 2 > tdistinct vertices (closed form proved by induction in
Lean thm16), a contradiction. Repeatedly deleting a vertex of degree ≤ 2 peels t− 2 vertices down
to 2 remaining vertices (at most 1 edge), bounding |E| ≤2(t− 2) + 1 = 2t− 3 < 2t (arithmetic
verified in Leanthm17).
(2)–(3) An integer N≥ 1 has LN = L iff 2L−1 − 2 < N≤ 2L − 2. Thus an integer with
LN = L satisfies N > cLe iff 2L − 2 > cLe, i.e. 2L > cLe + 2, in which case the minimal witness is
N0 = cLe +1. Inside the Lean 4 kernel, thm18 verifies 2L ≤L 64 +2 forevery1 ≤L≤ 588 alongside
2588 < 58964 + 3 ≤ 2589, proving N0(64) = 58964 + 1. Likewise, thm19 certifies 2L ≤L 4 + 2 for all
1 ≤L≤ 16 and 216 < 83,522 + 2 ≤ 217, proving N0(4) = 83,522; and thm20 certifies 2L ≤ 2L4 + 2
for all 1≤L≤17 and 2 17 <209,953 + 2≤2 18, provingN loc = 209,953.
6 Formal Verification Architecture and Reproducibility
All results are independently verified across three layers (with the Lean 4 layer formalizing
all algebraic, band-conservation, binary-tree external path length, weighted-tree expectation,
6

--- Page 7 ---
Table 1: Exact comparison of Gholami–Hajiaghayi [ 7] parameters against our sharpened bounds
and lower bounds.
Component Gholami–Hajiaghayi [7] Our Exact Result Improvement / Barrier
Outer shell ratioK(α=12)K= 16 (Lem. 8.1)K crit= 4, pow-2K= 8 4×smaller 4K2h, 16×smallerK4
Disjoint-set / MST bandsp= 3:O(Q+klog(3)k) Fixedp:O(pQ+klog (p)k) Not the log(3)nbottleneck
M-octave classificationO(Nlog log logN) upper≥N⌊log2M⌋Las Vegas Unconditional tight barrier
Critical-edge witness / edgesg= 4⌈log2(t+ 2)⌉+ 3,|E| ≤2t g= 2⌈log2 t+33 ⌉,|E| ≤2t−3>2×shorter witness, tighter|E|
Outer thresholdN > LeN e= 64:N0 = 58964+ 1e= 4:N 0 = 174+ 1 = 83,522>172 orders of magnitude drop
Local thresholdN >2L4N “absolutely bounded” ExactN loc= 209,953 Exact machine-checked crossover
Figure 3: (a) Exact minimum-degree-3 Moore 2-core witness path length g = 2 r (girth >
2r + 1) versus Lemma 6.2’s g = 4 ⌈log2(t + 2)⌉ + 3 (Theorem 5.1). (b) Exact outer guard
crossover log10 N0(e) across e∈ [2, 64], demonstrating the > 172-order-of-magnitude reduction
from 58964 + 1≈1.94×10 177 to 83,522.
Moore-count, and exact integer-threshold kernels, while geometric polyhedron convexity and
graph-peeling reductions are proved in full in Sections 4–5):
1. Constructive Lean 4.36.0 Formalization:20 theorems ( thm01–thm20) in lean/
AlmostLinearSSSPBarriers.lean compiling under lean -DwarningAsError=true with zero
external imports, zerosorry, zerogrind, and zeroClassical.choice.
2.AST-Audited Zero-Float Python Verifier:Pure standard-library code (int,Fraction)
in verification/verify sssp barriers.py, self-auditing its AST and emitting 16 canonical
SHA-256 certificates (C01–C16) across four modes, with manifest SHA-256 b13717af85567f5e
094a39696a2bdf2256cb0587f4febaf2975f24c7ae7eca50.
3. Adversarial Test Suite:56 pytest checks in tests/test adversarial.py covering positive
verification and adversarial counterexamples across all four modes.
AI Assistance Disclosure.Portions of the algebraic derivations, Lean 4 formalization, zero-
float verification tooling, and manuscript preparation were developed using Google Antigravity.
All theorems, formal proofs, exact rational certificates, and adversarial tests were independently
audited and verified, and the author takes full responsibility for all mathematical content.
References
[1] Edsger W. Dijkstra. A note on two problems in connexion with graphs.Numerische
Mathematik, 1:269–271, 1959.
7

--- Page 8 ---
[2] Ran Duan, Jiayi Mao, Xiao Mao, Xinkai Shu, and Longhui Yin. Breaking the sorting barrier
for directed single-source shortest paths. InProceedings of the 57th Annual ACM Symposium
on Theory of Computing (STOC 2025), pages 36–44. ACM, 2025.
[3] Ran Duan, Jiayi Mao, Xinkai Shu, and Longhui Yin. A randomized algorithm for single-source
shortest path on undirected real-weighted graphs. In64th IEEE Annual Symposium on
Foundations of Computer Science (FOCS 2023), pages 484–492. IEEE Computer Society,
2023.
[4] Ran Duan, Xiao Mao, Xinkai Shu, and Longhui Yin. A faster directed single-source shortest
path algorithm. In53rd International Colloquium on Automata, Languages, and Programming
(ICALP 2026), volume 374 ofLIPIcs, pages 81:1–81:23, 2026.
[5] Jittat Fakcharoenphol, Satish Rao, and Kunal Talwar. A tight bound on approximating
arbitrary metrics by tree metrics.Journal of Computer and System Sciences, 69(3):485–497,
2004.
[6] Michael L. Fredman and Robert Endre Tarjan. Fibonacci heaps and their uses in improved
network optimization algorithms.Journal of the ACM, 34(3):596–615, 1987.
[7] Iman Gholami and MohammadTaghi Hajiaghayi. Linear single-source shortest path, almost.
arXiv preprint arXiv:2611.34911v1, November 2026.
[8] Avi Kadria and Liam Roditty. A faster undirected single-source shortest path algorithm.
arXiv preprint arXiv:2609.15247, 2026.
[9] Seth Pettie and Vijaya Ramachandran. A shortest path algorithm for real-weighted undirected
graphs.SIAM Journal on Computing, 34(6):1398–1431, 2005.
[10] Robert Endre Tarjan. Efficiency of a good but not linear set union algorithm.Journal of the
ACM, 22(2):215–225, 1975.
[11] Mikkel Thorup. Undirected single-source shortest paths with positive integer weights in linear
time.Journal of the ACM, 46(3):362–394, 1999.
[12] Shuyi Yan. Lossless derandomization for undirected single-source shortest paths and approxi-
mate distance oracles. In2026 SIAM Symposium on Simplicity in Algorithms (SOSA), pages
404–412. SIAM, 2026.
8
