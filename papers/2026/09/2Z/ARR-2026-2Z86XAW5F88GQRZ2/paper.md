# The inverse self-commutator cost at inertia $(m,3)$: tiling certificates, 3×3-block shifts and a padding phase

**Lluis Eriksson** (Independent researcher)

## Abstract

For a traceless Hermitian $F\in M_d(\mathbb C)$ let $\kappa_d(F)=\tfrac12\min\{\|C\|_{HS}^2: CC^*-C^*C=2F\}$. On the inertia-$(m,3)$ stratum ($m$ positive eigenvalues, three negative ones, $z$ zeros) we determine $\kappa_d$ as the maximum of an explicit finite set $S(m,z)$ of linear forms for $m=3,\dots,9$ and $z\le2$, by exact Horn "tiling" certificates below and $3\times3$-block weighted shifts above, the latter verified at every vertex of every chamber together with a convexity argument. The forms are costs of layerings; for the ordered family A the lower bound is proved for all $m$ and $z$ by Lidskii–Wielandt tail inequalities. Unlike inertia $(m,2)$, the value is not padding-invariant: for $m\equiv1,2\pmod3$ exactly one extra exposed form exists at $z=0$, so $\kappa_{m+3}>\kappa_{m+4}$ on an open set within the stated finite range. At an exact $m=4$ example, padding raises the minimum optimal rank from $4$ to $5$ while $\kappa_7=74/61>\kappa_8=73/61$. Six combinatorial families are conjectured to describe $S(m,z\ge1)$ for all $m$, with quadratic growth; they are tested numerically out of sample for $m=10,11$.

## 1. Introduction

The quantity $\kappa_d(F)$ measures the cheapest realisation, in Hilbert–Schmidt norm, of a traceless Hermitian $F$ as a self-commutator $\tfrac12(CC^*-C^*C)$. Its theory has been developed in a line of records of the AI Research Record archive, cited by descriptive keys (identifiers in the reference list); everything used from them is restated here. [FourLevel] reduced $\kappa_d$ to a finite linear program over Horn inequalities (the *Horn program*, restated as (2.1)) and gave the four-level formula; [FiveLevel] the five-level formula; [OneSpike] the one-spike formula $\kappa_d=\sum_j j\,a_j$ when one sign has multiplicity one; [RankOnset] the rank-onset results and, in its Remark 3.3, the first example where zero padding lowers the value, $\lambda=(25,18,18,-10,-17,-17,-17)/7$ with $\kappa_7=74/7$ and $\kappa_8=73/7$. The immediate antecedent is the inertia-$(m,2)$ paper [Mtwo], which proved a dimension-free closed formula $\kappa_d=\max(F_0,\dots,F_{m-1},G_1,G_3,\dots)$ for every $m$ and every number of zeros (Theorem A there), described its chambers (Theorem B) and optimizers (Theorem C$'$), and asked in its Open question 1 what happens at inertia $(m,3)$: whether block shifts with $3\times3$ blocks attain the value and whether Horn triples adding two boxes to a rectangle certify it.

**Contribution.** We answer these questions on the inertia-$(m,3)$ stratum for $m\le9$ and $z\le2$ zeros ($d\le14$) and describe what changes. (i) The value is again the maximum of finitely many linear forms, each the cost of a *layering* of the spectrum into layers of size at most three (Theorem 1), and the finite counts of exposed forms are consistent with conjectural quadratic growth in $m$ ($10,18,26,34,45,59,69$ for $m=3,\dots,9$) in contrast with the linear count for inertia (m,2). (ii) Every form is certified below by a sum of Horn inequalities with multipliers one, each $s_t$ used at most once — a "tiling" — built, for $z\ge1$, from Lidskii–Wielandt inequalities and Pieri triples with $\lambda(J)$ a single row or column of at most three boxes; the $z=0$-only forms additionally use the non-Pieri shapes $(3,1)$ or $(2,1,1)$; for the ordered family A the certificate is explicit and dimension-free (Theorem 2, proved for all $m,z$). (iii) The value is attained by $3\times3$-block weighted shifts, verified as a linear program at every vertex of every chamber and extended to the chambers by convexity. (iv) Padding is *not* invariant: when $m\equiv1,2\pmod3$ there is exactly one extra exposed form at $z=0$ which is invalid after padding, so $\kappa_{m+3}>\kappa_{m+4}$ on an open set, and the exact $m=4$ example forces rank at least $m+1$ after padding; broader rank forcing is numerical evidence, as specified in Theorem 3(4). The padding example of [RankOnset] is the $m=4$ instance. (v) The exposed forms for $z\ge1$ are conjecturally the costs of six explicit families A–F of layerings, verified for $m\le9$ against the computed sets and out of sample for $m=10,11$ (Conjecture 4).

**Status, stated honestly.** Theorem 1 is proved with computer assistance for $m=3,\dots,9$, $z=0,1,2$, with exact lower certificates and exact upper-bound chain checks. This revised candidate adds exact lower certificates at $(8,2),(9,1),(9,2)$; these were only numerically validated in the received manuscript. Section 8 distinguishes the new author-side verification from historical reported computations. Theorem 2 is proved for all $m$ and $z$. Theorem 3 is proved for $m\le9$ (with exact rational strict inequalities at explicit points) and observed numerically for $m=10,11,12,13$. Conjecture 4 is a conjecture. The received manuscript reports an adversarial review that re-implemented every computational ingredient and upgraded the upper bound to exact arithmetic for $m\le8$ (extended to $m=9$ with its code for this manuscript); its corrections are incorporated (Section 8). Two literature searches (Section 10) found no prior closed formula on an inertia stratum and no prior block-shift or tiling-certificate method; the nearest works, Johnson–Ozawa–Schechtman [JOS13] and Angel–Schechtman [AS15], bound respectively $\|B\|\,\|C\|$ and $\|B\|\,\|C\|_2$ over factorisations $A=[B,C]$, where $\|\cdot\|$ here denotes operator norm and $\|\cdot\|_2$ Hilbert–Schmidt norm. Both objectives differ from the present constrained self-commutator cost. A null search does not certify priority.

## 2. Setting

Throughout $\|X\|^2=\operatorname{Tr}X^*X$ and $F\in M_d(\mathbb C)$ is Hermitian, traceless, with ordered spectrum $\lambda_1\ge\dots\ge\lambda_d$. On the inertia-$(m,3)$ stratum
$$\lambda=(a_1\ge\dots\ge a_m>0,\ 0^{z},\ -b_3,\ -b_2,\ -b_1),\qquad b_1\ge b_2\ge b_3>0.$$
$$\sum_ja_j=b_1+b_2+b_3=:P,\qquad d=m+z+3.$$
The spectrum index of $a_j$ is $j$; those of $-b_1,-b_2,-b_3$ are $d,d-1,d-2$. Since every statement is homogeneous we normalise $P=1$ when convenient. By $F\mapsto-F$ (which replaces $C$ by $C^*$) everything transfers to inertia $(3,n)$.

Given $C$ with $CC^*-C^*C=2F$, put $R=CC^*/2$, $S=C^*C/2$: they are PSD with the same spectrum $s_1\ge\dots\ge s_d\ge0$ (the *common spectrum*), $R-S=F$, $\tfrac12\|C\|^2=\sum_ts_t$, and conversely any such pair comes from $C=U\sqrt{2\Sigma}V^*$. Hence ([FourLevel] Theorem 2.2, [RankOnset] Proposition 2.2, [Mtwo] (2.1))
$$\kappa_d(F)=\min\Big\{\sum_{t<d}s_t:\ s_1\ge\dots\ge s_{d-1}\ge s_d=0,\ (s,-s^{\mathrm{rev}},\lambda)\ \text{Horn-feasible}\Big\},\tag{2.1}$$
where Horn-feasible means that $\alpha=(s_1,\dots,s_{d-1},0)$, $\beta=(0,-s_{d-1},\dots,-s_1)$ and $\gamma=\lambda$ are the spectra of Hermitian $R$, $-S$ and $F=R+(-S)$, i.e. satisfy the trace identity and every Horn inequality $\sum_{k\in K}\gamma_k\le\sum_{i\in I}\alpha_i+\sum_{j\in J}\beta_j$, $(I,J,K)\in T^d_r$ [Ho62,Kl98,KT99,Fu00]. In $s$-notation a triple reads
$$\sum_{i\in I,\,i<d}s_i-\sum_{j\in J,\,j>1}s_{d+1-j}\ \ge\ \sum_{k\in K}\lambda_k.\tag{2.2}$$
With $\lambda(I)=(i_r-r,\dots,i_1-1)$ the partition attached to $I=(i_1<\dots<i_r)$, (2.2) holds for all Hermitian triples whenever the Littlewood–Richardson coefficient $c^{\lambda(K)}_{\lambda(I)\lambda(J)}$ is nonzero (Klyachko [Kl98]); this necessity direction is all the lower bounds use. Sufficiency (Klyachko, Knutson–Tao) enters twice: in dimensions $n\le3$ inside the block-shift construction (Section 5), and in identifying the set of optimal common spectra with the optimal face of (2.1) (Section 6). Two facts about $\lambda\mapsto\kappa_d(\lambda)$ are used repeatedly: it is the value of a linear program in which $\lambda$ enters only the right-hand sides, hence convex and piecewise linear in $\lambda$ (so $\kappa_d-g$ is convex for every linear form $g$, and $\kappa_d$ is continuous on the closed stratum); and $\kappa_{d+1}(F\oplus0)\le\kappa_d(F)$ (pad $C$ by a zero row and column).

**Forms and canonical coordinates.** A *form* is a linear function $g(\lambda)=\sum_j\alpha_ja_j+\beta_1b_1+\beta_2b_2$ with integer coefficients, written $(\alpha_1,\dots,\alpha_m;\beta_1,\beta_2)$; the coefficient of $b_3$ is normalised to $0$ using $\sum a=\sum b$. A form is *valid* if $g\le\kappa_d$ on the stratum and *exposed* (relative to a set $S$ of valid forms) if it is the unique maximiser of $S$ on a nonempty open subset. Its *chamber* is $C_g=\{\lambda\ \text{in the stratum},\ P=1:\ g\ge h\ \forall h\in S\}$, a polytope.

**Layerings and costs.** A *layering* $L$ is an ordered partition of the multiset $\{-b_1,-b_2,-b_3,a_1,\dots,a_m\}$, possibly together with some of the zero eigenvalues, into layers $\Lambda_0,\Lambda_1,\dots,\Lambda_T$ of size at most $3$, with $\Lambda_0\subseteq\{-b_i\}$ and $\Lambda_T$ a nonempty set of $a$'s (and zeros). Write $t(x)$ for the index of the layer containing $x$, $\mathrm{tail}_u=\sum_{x\in\Lambda_u\cup\dots\cup\Lambda_T}x$, and
$$\operatorname{cost}(L)=\sum_{u=1}^{T}\mathrm{tail}_u .$$

**Lemma 2.1.** $\operatorname{cost}(L)=\sum_x t(x)\,x=\sum_j\big(t(a_j)-t(b_3)\big)a_j+\sum_i\big(t(b_3)-t(b_i)\big)b_i$, where $t(b_i):=t(-b_i)$.

*Proof.* $\sum_{u\ge1}\mathrm{tail}_u=\sum_x x\cdot\#\{u\ge1:u\le t(x)\}=\sum_xt(x)x$; adding $t(b_3)\big(\sum_ib_i-\sum_ja_j\big)=0$ gives the canonical coordinates. $\square$

Conversely a form $g$ with $\alpha_j=t(a_j)-t(b_3)$, $\beta_i=t(b_3)-t(b_i)$ for some nonnegative layer indices determines its *level layering* $L(g)$: the layers are the level sets of $t$, ordered by $t$, with the common shift fixed by $\min t=0$. Every exposed form found below has a level layering with layers of size at most three, $\Lambda_0$ consisting of $b$'s and $\Lambda_T$ of $a$'s. The *$b$-schedule* of a layering is $u=(t(b_1),t(b_2),t(b_3))$ and the *capacity* of layer $u\ge1$ is $c_u=\#\{i:t(b_i)<u\}$.

## 3. Statements

Let $S(m,z)$ be the set of exposed forms computed in Section 8 (files `closed_m{m}_z{z}.json`; the sets for $z=1,2$ coincide, and for $z=3$ when $m\le6$). Their sizes are:

| $m$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| $\lvert S(m,0)\rvert$ | 10 | 19 | 27 | 34 | 46 | 60 | 69 |
| $\lvert S(m,z\ge1)\rvert$ | 10 | 18 | 26 | 34 | 45 | 59 | 69 |

(For $m=2$ both sets have $5$ elements, matching the count $(3-1)+\lceil 3/2\rceil+1=5$ after swapping the inertia parameters of Theorem B of [Mtwo] at inertia $(3,2)$.)

**Theorem 1 (PROVED-COMPUTER-ASSISTED; $m=3,\dots,9$, $z=0,1,2$, $d\le14$).** On the whole stratum $\kappa_d=\max_{g\in S(m,z)}g$. Every $g\in S(m,z)$ is the cost of its level layering $L(g)$, and $\kappa_d=g$ on the chamber $C_g$; the chambers cover the stratum. The proof has two finite halves whose arithmetic status is:

| $(m,z)$ | $d$ | lower bound $\kappa_d\ge g$ | upper bound $\kappa_d\le g$ on $C_g$ |
|---|---|---|---|
| $m=3,\dots,9$, $z=0,1,2$ | $\le14$ | exact tiling certificates; the three formerly numerical cases were completed for this candidate (Sections 4 and 8) | exact rational vertices and exact chain LP; padding transfers the checked chains when the coefficient sets coincide (Section 5) |

"Exact tiling certificate" means: a list of Horn triples, each with LR coefficient $\ge1$ verified by two independent implementations (and membership in Fulton's $T^d_r$ for $d\le9$), whose $s$-forms have every coefficient $\le1$ and whose right sides sum, in integer arithmetic, to $g$. The received manuscript used a floating-point joint validity LP at $(8,2),(9,1),(9,2)$; a numerical tolerance is not a rigorous lower bound. The new certificates replace that step, while numerical discovery remains a way of proposing exact proof objects. The upper bound is, in all cases, the feasibility of one $3\times3$-block chain per chamber at every chamber vertex plus convexity (Section 5); the author's runs of it are floating point (qhull vertices, HiGHS chain LP) for all $787$ chambers and $8\,775$ vertices, the reviewer's exact (pycddlib/GMP) for $m\le8$, and the reviewer's code rerun at $m=9$ for this manuscript is exact as well, so the upper bound is exact for every $(m,z)$ of the theorem.

**Theorem 2 (PROVED, all $m\ge3$, $z\ge0$).** Let $L$ be a layering of family A: $b$-schedule $(0,u_2,u_3)$ with $u_2\le u_3$, and $a_1,a_2,\dots$ placed in order into the layers $u=1,2,\dots$, each layer $u<T$ receiving exactly $c_u$ of them, the last layer $T$ receiving the rest (at least one). Then $\kappa_d\ge\operatorname{cost}(L)$ on the stratum, with an explicit Lidskii–Wielandt certificate (Section 4.2). In particular $\kappa_d\ge\max_{A}\operatorname{cost}$ in every dimension.

**Theorem 3 (padding and rank; PROVED-COMPUTER-ASSISTED for $m\le9$, exact where stated).**

1. For $m=3,6,9$: $S(m,0)=S(m,1)=S(m,2)$ (and $=S(m,3)$ for $m=3,6$), so $\kappa_{m+3}(\lambda)=\kappa_{m+4}(\lambda\oplus0)=\kappa_{m+5}(\lambda\oplus0^2)$ on the stratum.
2. For $m=4,5,7,8$: $S(m,0)=S(m,1)\cup\{g_0^{(m)}\}$ with exactly one extra form,
$$g_0^{(4)}=(1,2,3,4;-2,-1),\qquad g_0^{(5)}=(1,2,3,3,4;-2,-1),$$
$$g_0^{(7)}=(1,2,2,3,3,4,5;-2,-1),\qquad g_0^{(8)}=(1,2,2,3,3,4,4,5;-2,-1),$$
the costs of the layerings
$$\{b_3\}\{b_2,a_1\}\{b_1,a_2\}\{a_3\}\{a_4\},\qquad \{b_3\}\{b_2,a_1\}\{b_1,a_2\}\{a_3,a_4\}\{a_5\},$$
$$\{b_3\}\{b_2,a_1\}\{b_1,a_2,a_3\}\{a_4,a_5\}\{a_6\}\{a_7\},\qquad \{b_3\}\{b_2,a_1\}\{b_1,a_2,a_3\}\{a_4,a_5\}\{a_6,a_7\}\{a_8\}.$$
This form is invalid for every $z\ge1$, and $\kappa_{m+3}(\lambda)>\kappa_{m+4}(\lambda\oplus0)$ on a nonempty open subset of the stratum: at the rational points of Section 6 the exact margins $g_0-\max S(m,1)$ are $1/40,1/60,1/120,1/150$. The value is padding-invariant for $z\ge1$ within the verified range ($S(m,1)=S(m,2)$; $=S(m,3)$ for $m\le6$).
3. (Exact, GMP.) At $a=(17,17,17,10)/61$, $b=(25,18,18)/61$ ($m=4$), $\kappa_7=74/61$ with an optimizer of rank $4=m$, while $\kappa_8=73/61$ and every optimizer of the padded problem has rank $\ge5=m+1$: the minimum of $s_5$ over the optimal face of (2.1) is $1/61$, and the value of (2.1) with $s_5=s_6=s_7=0$ imposed is $74/61=\kappa_7$. After $F\mapsto-F$ and scaling by $61/7$ this is the example of [RankOnset] Remark 3.3.
4. (Numerical.) The same pattern continues: at $z=0$ exactly one extra exposed form appears for $m=10,11,13$ (namely $(1,2,2,3,3,3,4,4,5,6;-2,-1)$, $(1,2,2,3,3,3,4,4,5,5,6;-2,-1)$, $(1,2,2,3,3,3,4,4,4,5,5,6,7;-2,-1)$), each invalid at $z=1$ by margins $0.033,0.030,0.026$, and none for $m=12$ in $600$ samples; on the region where $g_0>\max S(m,1)$, the rank-$m$-capped padded value exceeds the unrestricted value at $48/48$, $40/40$, $40/40$ sampled points ($m=4,5,7$), and equals $\kappa_{m+3}$ numerically. These finite samples do not prove a rank rule throughout the region or a statement about the ranks of every optimizer.

**Conjecture 4 (general $m$, $z\ge1$).** $S(m,z\ge1)$ is the set of costs of the layerings of the six families below, and $\kappa_d=\max$ over them for all $m\ge3$, $z\ge1$. Fix a $b$-schedule $u$ with $\min u=0$; layer $u\ge1$ has $c_u$ *slots*; concatenate the slots of layers $1,2,3,\dots$ and fill them, left to right, with an arrangement $\pi$ of $(a_1,\dots,a_m,*,*,*)$, where $*$ are virtual entries (value $0$, deleted at the end, so that the last layers may be partial); a *boundary* is the position between the last slot of a layer and the first of the next. Moves: $T_\beta$ transposes the two slots adjacent to boundary $\beta$; $F_\beta$ is the forward $3$-cycle $(x,y\mid z)\mapsto(y,z\mid x)$ on the two slots before and the one after $\beta$; $B_\beta$ the backward $3$-cycle $(x\mid y,z)\mapsto(z\mid x,y)$. Two rules apply to every family: the number of inversions of $\pi$ (virtual entries counting as $+\infty$) equals the number of inversions of the $b$-order, $\#\{i<j:t(b_i)>t(b_j)\}$, and the last layer contains no $b$. The families are:

- **A**$(u_2,u_3)$: $u=(0,u_2,u_3)$, $u_2\le u_3$, $\pi=$ identity; exposed iff $2u_3-u_2\le m-1$ ($u_2\ge1$) or $2u_3\le m-1$ ($u_2=0$), $u_2\le m-2$, and $m\ge4$ when $(u_2,u_3)=(0,0)$. Count $A(m)=\lfloor\tfrac{m-1}2\rfloor+1-[m=3]+(m-2)+\lfloor\tfrac{(m-2)^2}4\rfloor$.
- **B**$(u_2;\beta)$: $u=(0,u_2,u_2-1)$, $u_2\ge1$ ($b_3$ one layer before $b_2$), one transposition $T_\beta$ at a boundary ending a layer of index $\ge u_2$. Count $B(m)=\sum_{j=0}^{m-2}(\lfloor j/3\rfloor+1)$.
- **C**$(k;\beta)$: $u=(1,0,k)$, $k\ge1$ ($b_2$ alone in $\Lambda_0$, $b_1$ in layer $1$), one transposition at any boundary.
- **D**: $u=(1,0,0)$ ($\Lambda_0=\{b_2,b_3\}$, $\Lambda_1=\{b_1,a,a\}$): two transpositions at distinct boundaries, or one $F_\beta$.
- **E**: $u=(1,1,0)$ ($\Lambda_0=\{b_3\}$, $\Lambda_1=\{b_1,b_2,a\}$): two transpositions at distinct boundaries, or one $B_\beta$.
- **F**: $u=(2,1,0)$: exactly the two arrangements $(a_3,a_1,a_4,a_2,a_5,a_6,\dots)$ and $(a_2,a_3,a_4,a_1,a_5,a_6,\dots)$, i.e. $\{b_3\}\{b_2,a_3\}\{b_1,a_1,a_4\}\{a_2,a_5,a_6\}\dots$ and $\{b_3\}\{b_2,a_2\}\{b_1,a_3,a_4\}\{a_1,a_5,a_6\}\dots$.

The generator (`families2.py`) reproduces $S(m,1)$ exactly for $m=3,\dots,9$ with family counts A/B/C/D/E/F $=2,5,8,11,15,19,24$ / $2,3,5,7,9,12,15$ / $2,4,5,8,10,14,16$ / $1,2,3,3,4,6,6$ / $1,2,3,3,5,6,6$ / $2$, and predicts $|S(m)|=87,103,120,139,164$ for $m=10,\dots,14$ (quadratic growth, against the linear count of inertia $(m,2)$). Evidence beyond $m\le9$: at $m=10$ and $m=11$, $z=1$, the predicted sets pass random tests, validity and exposedness LPs and a chamber-vertex completeness check (Section 8), which gives numerical evidence for $\kappa_{14}=\max$ of the $87$ forms and $\kappa_{15}=\max$ of the $103$ forms; these out-of-sample cases are not asserted as proved here. What is not known: that the six families are exhaustive for general $m$, a general-$z$ proof of the Pieri tiles of families B–F, and any general-$m$ upper bound. Appendix A lists every form of $S(m,z)$ with its family and layering for $m\le6$.

## 4. Lower bounds

### 4.1 Tiling certificates

A *certificate* for a form $g$ in dimension $d$ is a list of Horn triples $(I,J,K)$ (each with $c^{\lambda(K)}_{\lambda(I)\lambda(J)}\ge1$) whose $s$-forms (2.2) sum to a linear combination of $s_1,\dots,s_{d-1}$ with every coefficient $\le1$ and whose right sides sum to $g$. Since $s_t\ge0$, $\sum_{t<d}s_t$ minus the summed left side is a nonnegative combination of the $s_t$, so every feasible $s$ of (2.1) has $\sum_{t<d}s_t\ge g$; an optimizer with $s_d>0$ is shifted as in [Mtwo] Corollary 4.6. Only Klyachko necessity is used, so a certificate is a proof of $\kappa_d\ge g$ for that $d$.

All certificates here are *tilings*: the multipliers are $1$ and each $s_t$ with $t\le m$ occurs exactly once with coefficient $+1$; the only negative terms are $-s_{d-1}$, $-s_{d-2}$ (and occasionally $+s_{m+1},+s_{m+2}$ on zero indices). Each triple is a *tile* of the form $+s[U]-s[N]\ge\sum_{k\in K}\lambda_k$ with $U\subseteq\{1,\dots,m+2\}$, $N\subseteq\{d-2,d-1\}$; the right side is a sum of consecutive $a$'s with at most three holes, minus some $b$'s. For every $(m,z)$ with $d\le12$ the certificates were found as the duals of a *restricted* Horn LP over a catalogue of such tiles (`catalogue.py`, `certs.py`), solved at the strict Chebyshev centre of each chamber, then checked exactly: the multipliers rounded to $1$ (they are within $10^{-6}$ of $1$; what is verified exactly is the integer identity), the tiles' right sides sum in integer arithmetic (using $\sum a=\sum b$) to $g$, every $s_t$ has total coefficient $\le1$, and every tile has LR coefficient $\ge1$ by two independent implementations (a tableau counter `lr.py` and the bialternant/Kostka formula `lr2.py`, cross-checked on $3000$ random triples) and, for $d\le9$, lies in Fulton's recursively generated $T^d_r$. The reviewer re-verified $36$ certificates ($149$ tiles) with a third LR implementation (Jacobi–Trudi + Pieri) and an own Fulton generator: $36/36$.

The tile types at $z\ge1$, by $\lambda(J)$, are: $\lambda(J)=\emptyset$ (Lidskii–Wielandt, including the Weyl tiles $s_j\ge a_j$ and $s_1\ge b_1$); $\lambda(J)=(1)$ (the lower Weyl tile $s_2\ge b_2$ and one-box Pieri tiles); $\lambda(J)=(1,1)$ ($s_3\ge b_3$ and two-box vertical strips); $\lambda(J)=(2)$ and $(3)$ (horizontal strips). Counts per $(m,z=1)$ for $m=3,\dots,8$: Lidskii–Wielandt $17,40,70,110,161,232$; row-type $8,16,24,33,50,71$; column-type $5,8,12,12,16,22$ (and $307/87/22$ at $m=9$, $z=0$). At $z=0$ the extra form $g_0^{(m)}$ needs, in addition, one or two tiles with $\lambda(J)=(3,1)$ ($m=4,7$) or $(2,1,1)$ ($m=5,8$) — the only non-Pieri shapes in the whole computation. The highest positive $s$-index used is $m+1$ ($z=0$) or $m+2$ ($z\ge1$), never $d-1$.

### 4.2 Family A: proof of Theorem 2

Let $L$ be as in Theorem 2, with layers $\Lambda_0,\dots,\Lambda_T$. For $u=1,\dots,T$ let $B_u\subseteq\{d-2,d-1,d\}$ be the spectrum indices of the $b$'s in layers $<u$ (so $|B_u|=c_u$), and $t_u$ the index of the first $a$ in layers $\ge u$; because the $a$'s are placed in order and every layer $u<T$ holds exactly $c_u$ of them, the $a$'s of layer $u$ are $a_{t_u},\dots,a_{t_u+c_u-1}$ and $t_{u+1}=t_u+c_u$.

*Tile $u$ for $u<T$*: the Lidskii–Wielandt triple $I=K=\{t_u,\dots,d\}\setminus B_u$, $J=\{1,\dots,r\}$, $r=|K|=d-t_u+1-c_u$. Here $\lambda(J)=0$ and $\lambda(I)=\lambda(K)$, so $c=1$; the sum condition $\sum I+\sum J=\sum K+r(r+1)/2$ is automatic. Its right side is $\sum_{k\in K}\lambda_k=\sum_{j\ge t_u}a_j-\sum_{i:\,t(b_i)\ge u}b_i=\mathrm{tail}_u$ (the zeros contribute nothing). Its left side is
$$\sum_{i\in[t_u,d-1]\setminus B_u}s_i-\sum_{i=d+1-r}^{d-1}s_i=s_{t_u}+\dots+s_{t_u+c_u-1}-\sum_{\beta\in B_u,\ \beta<d}s_\beta ,$$
because $d+1-r=t_u+c_u$ and the block $[t_u,t_u+c_u-1]$ lies in $[1,m-1]$, hence misses $B_u\subseteq\{d-2,d-1,d\}$.

*Tile(s) for $u=T$*: let $q=m-t_T+1\ge1$ be the number of $a$'s in the last layer. If $t_T+c_T-1\le m+z$ use the same Lidskii–Wielandt triple with $u=T$: right side $\sum_{j\ge t_T}a_j=\mathrm{tail}_T$ (all $b$'s are in $B_T$), left side $s_{t_T}+\dots+s_{t_T+c_T-1}-\sum_{\beta\in B_T,\beta<d}s_\beta$, whose positive block may run into the zero indices $m+1,\dots,m+z$ but not into $B_T$. Otherwise use the Weyl tiles $s_j\ge a_j$, $j=t_T,\dots,m$ ($I=K=\{j\}$, $J=\{1\}$), whose right sides also sum to $\mathrm{tail}_T$.

*Summation*: the positive blocks of the tiles are the consecutive, pairwise disjoint index sets $[t_u,t_{u+1}-1]$ ($u<T$) and $[t_T,\cdot]$; the negative terms involve only $s_{d-1},s_{d-2}$. Hence every $s_t$, $t<d$, has total coefficient $\le1$, and $\sum_u\mathrm{tail}_u=\operatorname{cost}(L)$ by definition. By Section 4.1, $\kappa_d\ge\operatorname{cost}(L)$. Nothing depends on $d$ except through the index bookkeeping, which is valid for every $z\ge0$. $\square$

The certificate is implemented LP-free in `familyA_cert.py` and verified exactly (sum condition, LR $=1$ by `lr2`, disjointness, integer identity of the form) for all $945$ (form, $z$) pairs with $m\le12$, $z\le4$. The reviewer re-derived the $s$-form and the identity independently. Its docstring mentions separate Weyl tiles for the $b$'s in $\Lambda_0$; the code emits none, because the $u=1$ tile with $B_1=\{d\}$ *is* $s_1\ge b_1$ (and with $B_1=\{d,d-1\}$ it is $s_1+s_2-s_{d-1}\ge b_1+b_2$), exactly as described above. The forms $F_k$ of [Mtwo] are the specialisation $b_3=0$ of family A. The argument uses only that every non-final layer is at full capacity, not $u_1=0$; but only the family-A layerings are exposed.

### 4.3 The Pieri tiles of families B–F

For families B–F the certificates are not dimension-free by inspection, but their tiles have only five shapes of $\lambda(J)$, and for each tile with $\lambda(J)$ a row $(k)$ or a column $(1^k)$ the Pieri rule [Fu97] gives $c^{\lambda(K)}_{\lambda(I)\lambda(J)}=1$ if $\lambda(K)/\lambda(I)$ is a horizontal (vertical) strip of $k$ boxes and $0$ otherwise. So a general-$z$ proof for a family reduces to two conditions per tile — the sum condition and the strip condition — as functions of the tail length; this was not carried out. Representative certificates at $m=5$, $z=1$ ($d=9$), one per family, read as follows (right sides in $a,b$; $s_1\ge b_1$ is written as $s_1\ge P-b_2-b_3$ etc.):

| family, form | tiles (left side $\ge$ right side) | $\lambda(I)$, $\lambda(J)$, $\lambda(K)$ of the non-Lidskii tile |
|---|---|---|
| B, $(-2,-1,0,1,2;3,-1)$ | $s_5\ge a_5$; $s_4+s_6-s_8\ge a_4+a_5-b_2$; $s_3\ge a_3+a_4+a_5-b_3-b_2$; $s_2\ge a_2+\dots+a_5-b_3-b_2$; $s_1\ge P-b_3-b_2$ | $(3^4),(1),(4,3,3,3)$ |
| C, $(-2,-1,-1,0,1;2,3)$ | $s_5\ge a_5$; $s_3+s_6-s_8\ge a_4+a_5-b_3$; $s_1+s_4-s_8\ge a_2+\dots+a_5-b_3$; $s_2\ge P-b_3-b_1$ | $(3,3,3,2),(1),(3^4)$; $(1^5),(1),(1^6)$ |
| D, $(1,1,2,3,2;-1,0)$ | $s_4\ge a_4$; $s_1+s_5+s_6-s_7-s_8\ge a_3+a_4+a_5$; $s_2\ge P-b_3-b_1$; $s_3\ge P-b_2-b_1$ | $(2^3),(2),(2^4)$ |
| E, $(1,2,2,3,3;-1,-1)$ | $s_4\ge a_4$; $s_5\ge a_5$; $s_1+s_2+s_6-s_7-s_8\ge a_2+\dots+a_5$; $s_3\ge P-b_2-b_1$ | $(1^3),(1,1),(1^5)$ |
| F, $(2,3,1,2,3;-2,-1)$ | $s_2\ge a_2$; $s_5\ge a_5$; $s_1+s_4-s_8\ge a_1+a_2+a_4+a_5-b_1$; $s_3\ge P-b_2-b_1$ | $(1^4),(2),(3,1,1,1)$ |

The one-box tiles such as $s_4+s_6-s_8\ge a_4+a_5-b_2$ ($I=(4,5,6,7)$, $J=(1,2,3,5)$, $K=(4,5,6,8)$) are the $(m,3)$ versions of the Pieri triples $(\mathrm{Pi})_i$ of [Mtwo] Lemma 4.3; the three-index tiles $s_1+s_5+s_6-s_7-s_8\ge a_3+a_4+a_5$ and $s_1+s_2+s_6-s_7-s_8\ge a_2+\dots+a_5$ add two boxes. The extra form at $z=0$, $m=4$, has the certificate $s_4\ge a_4$; $s_1\ge a_3+a_4$ ($I=J=(1,4)$, $K=(3,4)$, $\lambda=(2),(2),(2,2)$); $s_2+s_5-s_6\ge a_2+a_3+a_4-b_1$ ($I=(1,2,4,5)$, $J=(1,2,4,7)$, $K=(2,3,4,7)$, $\lambda(I)=(1,1)$, $\lambda(J)=(3,1)$, $\lambda(K)=(3,1,1,1)$); $s_3\ge P-b_2-b_1$ — the $(3,1)$ tile is the one that does not survive padding (its instantiation at $z'=1$ has no realisation with LR $\ge1$, in the reviewer's dimension-free search), consistent with Theorem 3.

Dimension-free evidence: the tile signatures $(K_a,K_b,U,N_{\mathrm{off}})$ (with $N$ measured from $d$) coincide between $z=1,2,3$ for every form when $m\le6$ (LP duals are not unique, so the few differences at $m=4,7$ are choices, not obstructions); and every tile of every $z=1$ certificate for $m=3,4,5$ ($30+64+106$ tiles) is realisable with LR $\ge1$ at $z'=2,3,4$ (reviewer's `tiles_dimfree2.py`). This supports, but does not prove, the general-$z$ validity of the B–F certificates.

## 5. Upper bounds

### 5.1 $3\times3$-block weighted shifts

As in [Mtwo] Section 5.1: choose a layering $\Lambda_0,\dots,\Lambda_T$ of the nonzero spectrum together with some zeros (layers of size $\le3$ here), let $D_t=\operatorname{diag}\Lambda_t$, and take $C=\sum_{t=1}^TM_t$ block-bidiagonal with $M_t:\Lambda_{t-1}\to\Lambda_t$. Then $CC^*=\bigoplus_t2R_t$ ($R_t$ on $\Lambda_t$), $C^*C=\bigoplus_t2S_t$ ($S_t$ on $\Lambda_{t-1}$), and $CC^*-C^*C=2F$ iff
$$S_1=-D_0,\qquad R_t-S_{t+1}=D_t\ (1\le t<T),\qquad R_T=D_T,\qquad R_t\ \text{and}\ S_t\ \text{have the same nonzero spectrum}.\tag{5.1}$$
Given PSD $R_t,S_t$ with equal nonzero spectra, $M_t=V\sqrt{2\Sigma}W^*$ realises them; zeros of $F$ left outside the layers lie in $\ker C\cap\ker C^*$. The cost is $\tfrac12\|C\|^2=\sum_t\operatorname{Tr}S_t=\sum_{t=1}^T\mathrm{tail}_t=\operatorname{cost}(L)$ (inserted zeros change nothing), and $\operatorname{rank}C=\sum_t\operatorname{rank}S_t\le\sum_t\min(|\Lambda_{t-1}|,|\Lambda_t|)$. A layering is *feasible* at $\lambda$ if (5.1) has a solution; then $\kappa_d(\lambda)\le\operatorname{cost}(L)(\lambda)$.

### 5.2 Chain feasibility as a linear program, and its convexity

Fix a *symbolic* layering (layers are lists of symbols $b_i$, $a_j$, $0$), and let $n_t=|\Lambda_t|\le3$. For a Hermitian $n\times n$ sum $\gamma=\operatorname{spec}(\alpha+\beta)$ the Horn conditions are the trace identity and the inequalities indexed by $T^n_r$, $1\le r<n$: for $n=2$ the three Weyl inequalities, for $n=3$ the twelve inequalities of $T^3_1\cup T^3_2$ (six Weyl and six Ky Fan–Lidskii type). These are necessary (Weyl, Lidskii, Horn) and sufficient for every $n$ (Klyachko [Kl98], Knutson–Tao [KT99]; see Fulton [Fu00]); here only $n\le3$ is needed. Consider the linear program in the variables $\sigma^{(t)}\in\mathbb R^3$, $t=1,\dots,T$:
$$\sigma^{(t)}_1\ge\sigma^{(t)}_2\ge\sigma^{(t)}_3\ge0,\quad \sigma^{(t)}_k=0\ \text{for}\ k>\min(n_{t-1},n_t),\quad \sigma^{(1)}=(-\Lambda_0)^{\downarrow},\quad \sigma^{(T)}=\Lambda_T^{\downarrow},$$
$$\big(\sigma^{(t)}|_{n_t},\ (-\Lambda_t)^{\downarrow},\ \sigma^{(t+1)}|_{n_t}\big)\ \text{satisfies the Horn conditions in dimension } n_t\quad(1\le t<T),\tag{5.2}$$
where $x^{\downarrow}$ is the decreasing rearrangement padded with zeros to length $3$ and $|_{n}$ the first $n$ entries.

**Lemma 5.1 (chain feasibility is the LP).** The layering is feasible at $\lambda$ iff (5.2) is feasible, and then $\sigma^{(t)}$ is the spectrum of $S_t$ (and of $R_t$).

*Proof.* If (5.1) has a solution, $\sigma^{(t)}:=\operatorname{spec}S_t$ satisfies (5.2): the rank cap because $S_t$ lives on $\Lambda_{t-1}$ and $R_t$, with the same nonzero spectrum, on $\Lambda_t$; the step conditions because $S_{t+1}=R_t+(-D_t)$ is a Hermitian sum on $\Lambda_t$ (Horn necessity). Conversely let $\sigma$ satisfy (5.2). By Lemma 5.0 of [Mtwo] — feasibility depends on the past only through $\operatorname{spec}S_t$, since $R_t$ may be *any* PSD matrix on $\Lambda_t$ with the nonzero spectrum of $S_t$ — construct inductively: $S_1=-D_0$; given $S_t$ with spectrum $\sigma^{(t)}$, Horn sufficiency in dimension $n_t$ provides a PSD $R_t$ on $\Lambda_t$ with spectrum $\sigma^{(t)}|_{n_t}$ such that $R_t-D_t$ has spectrum $\sigma^{(t+1)}|_{n_t}\ge0$; set $S_{t+1}=R_t-D_t$. At the end $\sigma^{(T)}=\Lambda_T^{\downarrow}$ lets us take $R_T=D_T$. $\square$

**Lemma 5.2 (convexity).** For a fixed symbolic layering, the set of $\lambda$ in the closed stratum at which it is feasible is convex.

*Proof.* On the closed stratum ($a$ and $b$ ordered, all entries $\ge0$) the decreasing rearrangement of a layer is a *fixed linear* function of $\lambda$: within $-\Lambda_t$ the $b$'s come first in index order, then the zeros, then the $-a_j$ in reverse index order, and this order never changes; likewise $(-\Lambda_0)^{\downarrow}$ and $\Lambda_T^{\downarrow}$. Hence every constraint of (5.2) is linear in $(\lambda,\sigma)$ jointly, the feasible set is a polyhedron in $(\lambda,\sigma)$-space, and the set of feasible $\lambda$ is its projection, which is convex. $\square$

The isospectral condition in (5.1) is not convex in matrix space; the argument never uses matrix space, only spectra. The encoding (5.2) is `layering_lp.feasible` (author, HiGHS) and `chain_own.chain_feasible_exact` (reviewer, exact rational LP over the reviewer's own $T^n_r$, $n\le3$); the reviewer checked the author's encoding line by line (rank caps, ordering, trace, terminal condition).

**Corollary 5.3.** If $g\in S(m,z)$ and one symbolic layering with $\operatorname{cost}=g$ is feasible at every vertex of the polytope $C_g$, then $\kappa_d\le g$ on $C_g$; combined with $\kappa_d\ge\max S$ this gives $\kappa_d=g$ on $C_g$, and since the chambers cover the stratum, $\kappa_d=\max S$ everywhere.

### 5.3 Chamber-vertex verification

For every $g\in S(m,z)$ the vertices of $C_g$ were enumerated — exact brute force over constraint subsets for $m\le4$ and qhull `HalfspaceIntersection` for $m\ge5$ (author), exact rational enumeration with pycddlib/GMP for $m\le8$ (reviewer), with identical counts — and the level layering $L(g)$, or $L(g)$ with one zero inserted, was tested at each vertex (`coverage_vertices.py`; reviewer `chain_own.py`). Vertex counts per chamber set:

| $m$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 | total |
|---|---|---|---|---|---|---|---|---|
| $z=0$ | 50 | 122 | 218 | 320 | 510 | 756 | 969 | 2945 |
| $z=1$ and $z=2$ | 50 | 117 | 212 | 320 | 501 | 746 | 969 | 2915 each |

In total $787$ chambers ($265+261+261$) and $8\,775$ vertices. In $779$ chambers the base layering $L(g)$ is feasible at every vertex; in the remaining eight it is not, but one layering with a single zero inserted is (Section 5.4). Runtimes: $\le27$ s per $(m,z)$ for the author's float run; seconds for $m\le7$, $85$–$112$ s per $(m,z)$ at $m=8$ and $542$–$546$ s per $(m,z)$ at $m=9$ for the exact run (the $m=9$ rows were pending when the review was written and were completed for this manuscript with the reviewer's script, `chain_m9.py`; all $3\times969$ vertices exact, every chamber covered, no zero insertion at $m=9$).

### 5.4 The eight chambers with an inserted zero

They are the chambers, at $z=1$ and at $z=2$, of
$$(1,1,2,3;-1,0)\ [m=4,\ \text{D}],\qquad (1,2,2,3,3;-1,-1)\ [m=5,\ \text{E}],$$
$$(1,1,2,2,2,3,4;-1,0)\ [m=7,\ \text{D}],\qquad (1,2,2,2,3,3,4,4;-1,-1)\ [m=8,\ \text{E}],$$
with feasible chains
$$\{b_2,b_3\}\{b_1,a_1,a_2\}\{a_3,0\}\{a_4\},\qquad \{b_3\}\{b_1,b_2,a_1\}\{a_2,a_3,0\}\{a_4,a_5\},$$
$$\{b_2,b_3\}\{b_1,a_1,a_2\}\{a_3,a_4,a_5\}\{a_6,0\}\{a_7\},\qquad \{b_3\}\{b_1,b_2,a_1\}\{a_2,a_3,a_4\}\{a_5,a_6,0\}\{a_7,a_8\}:$$
the zero goes into the penultimate layer. These are exactly the $m\equiv1,2\pmod3$ cases where $z=0$ has the extra form $g_0^{(m)}$; at $z=0$ every base chain is feasible on its (smaller) chamber. After padding $g_0^{(m)}$ is no longer valid, the neighbouring chamber grows, and on the new part the base chain — whose rank is at most $m$ by the bound of Section 5.1 (e.g. $2+1+1$ for the $m=4$ chain) — fails, while the chain with a zero has rank at most $m+1$. This is the $(m,3)$ analogue of Theorem C$'$(3) of [Mtwo], and it matches the exact rank forcing of Theorem 3(3).

**Explicit matrices.** `construct_C.py` turns the argmax layering at a point into a chain by the LP (5.2) with maximal Horn slack, solves each step (a $2\times2$ step in closed form, a $3\times3$ step with a rank-one target by the secular equation, otherwise by least squares on the characteristic polynomial polished on the eigenvalues), and assembles $C=\sum_t M_t$ with each rectangular $M_t$ embedded in its corresponding off-diagonal block (real, block bidiagonal). At $500$ points per $(m,z)$, $m=3,\dots,9$, $z=0,1$ ($7000$ matrices; a quarter from a tie-heavy law, every eighth point with an exact tie), all points were constructed; $\max|CC^{\mathsf T}-C^{\mathsf T}C-2F|$ has median $\le3\cdot10^{-15}$ and exceeds $10^{-9}$ at $5$ points ($\le3.0\cdot10^{-6}$, near-degenerate steps); $|\tfrac12\|C\|^2-\max S|\le8\cdot10^{-14}$ except at those points. The zero-inserted chain was needed at $45/10/6/3$ of $500$ points for $m=4/5/7/8$ at $z=1$ and never at $z=0$ or for $m=3,6,9$. $\operatorname{rank}C=m$ everywhere else, except that the maximal-slack interior chain has rank $m+1$ at $52$–$58$ of $500$ points for $m=3$ and at $2$–$14$ for $m=5$, where rank-$m$ optimizers nevertheless exist (Section 6). The reviewer's own constructor reproduces this at $28$ points ($m\le7$).

## 6. Padding and rank: proof of Theorem 3

*Sets.* $S(m,z)$ for $z=0,1,2$ (and $z=3$, $m\le6$) were computed by the closure loop of Section 8; comparing the files gives (1) and the identity $S(m,0)=S(m,1)\cup\{g_0^{(m)}\}$ in (2), the sets $S(m,1)$, $S(m,2)$ (and $S(m,3)$) being identical. By Theorem 1, $\kappa_{m+3+z}=\max S(m,z)$, which gives the padding invariance statements.

*Strict decrease, exactly.* For $m=4,5,7,8$ take the rational point (rounded strict Chebyshev centre of the chamber of $g_0^{(m)}$ in $S(m,0)$, renormalised to $P=1$; `exact_strict.py`):
$$\begin{aligned}m=4:\quad a&=(57/200,\,157/600,\,143/600,\,43/200),\\ b&=(107/300,\,1/3,\,31/100);\end{aligned}$$
$$\begin{aligned}m=5:\quad a&=(7/30,\,13/60,\,1/5,\,11/60,\,1/6),\\ b&=(7/20,\,1/3,\,19/60);\end{aligned}$$
$$\begin{aligned}m=7:\quad a&=(1/6,\,19/120,\,3/20,\,43/300,\,27/200,\,19/150,\,3/25),\\ b&=(41/120,\,1/3,\,13/40);\end{aligned}$$
$$\begin{aligned}m=8:\quad a&=(11/75,\,17/120,\,27/200,\,77/600,\,73/600,\,23/200,\,13/120,\,31/300),\\ b&=(17/50,\,1/3,\,49/150).\end{aligned}$$
There $g_0^{(m)}=401/300,\ 29/20,\ 41/24,\ 277/150$ and $\max S(m,1)=787/600,\ 43/30,\ 17/10,\ 46/25$, margins $1/40,1/60,1/120,1/150$. Now $\kappa_{m+3}\ge g_0^{(m)}$ by its exact tiling certificate ($d=m+3\le11$), and $\kappa_{m+4}=\max S(m,1)$ exactly ($d=m+4\le12$, exact lower bound; exact upper bound by Theorem 1). Hence $\kappa_{m+3}(\lambda)>\kappa_{m+4}(\lambda\oplus0)$ at these points, and by continuity of both sides on an open set. Since $\kappa_{m+3+z}(\lambda\oplus0^z)\le\kappa_{m+4}(\lambda\oplus0)<g_0^{(m)}(\lambda)$ for every $z\ge1$, $g_0^{(m)}$ is invalid in every padded dimension. At the padding example $a=(17,17,17,10)/61$, $b=(25,18,18)/61$ one has $g_0^{(4)}=74/61$ and $\max S(4,1)=73/61$.

*Rank, exactly.* By Horn sufficiency in dimension $d$, every feasible $s$ of (2.1) is the common spectrum of some $C$, and every optimizer has $s_d=0$ (otherwise shifting lowers the cost), so the set of optimal common spectra is the optimal face of (2.1), and $\operatorname{rank}C=\#\{t:s_t>0\}$. The reviewer's GMP linear programs over the full Fulton lists ($2062$ triples for $d=7$, $8752$ for $d=8$) at the integer spectrum $(17,17,17,10,[0],-18,-18,-25)$ give: $\kappa_7\cdot61=74$ with an optimal $s=(27,18,18,10,1,0)$ and $\min s_5$ on the optimal face $=0$, so a rank-$4$ optimizer exists (rank $\ge4$ is the inertia obstruction, [RankOnset] Lemma 2.1); $\kappa_8\cdot61=73$ with $s=(26,18,18,10,1,0,0)$, $\min s_5$ on the optimal face $=1$, so every optimizer has rank $\ge5$; and the minimum of (2.1) with $s_5=s_6=s_7=0$ is $74$. This is (3). The author's float scan (`rank_scan.py`, $150$ random points per $(m,z)$, $m\le7$, $z\le1$) finds minimal optimal rank $m$ at every random point except one $m=4$, $z=1$ point of rank $5$, and the tail-maximising optimizer of rank $m+1$ at $2$–$35\%$ of points; the reviewer's sampling of the region $\{g_0^{(m)}>\max S(m,1)\}$ gives (4).

*Beyond $m\le9$ (numerical).* At $z=0$ the predicted set of Conjecture 4 is exceeded at $4/1200$ points for $m=10$ and $1/1200$ for $m=11$ (by up to $2.4\cdot10^{-2}$), each time with the single dual form listed in (4); the reviewer confirmed each to be valid at $z=0$ (joint LP, $\min(\kappa-g)\ge-3.5\cdot10^{-15}$), invalid at $z=1$ ($-0.0333$, $-0.0303$) and exposed relative to the predicted set (chamber radius $3.9\cdot10^{-3}$, $3.4\cdot10^{-3}$), found the $m=13$ continuation (valid at $z=0$, invalid at $z=1$ by $0.0256$, radius $2.3\cdot10^{-3}$), and no extra form at $m=12$ in $600$ samples. The layerings of these forms all have schedule $(2,1,0)$ with the $a$'s in order, $\{b_3\}\{b_2,a_1\}\{b_1,a_2,a_3\}$ followed by triples and a shrinking tail; a rule "extra form iff $3$ does not divide $m$" is observed up to $m=13$ and not proved.

## 7. Consistency checks

*Reduction to inertia $(m,2)$.* Restricting the forms of $S(m,z\ge1)$ to $b_3=0$ must reproduce $\Phi=\max(F_k,G_j)$ of [Mtwo] Theorem A, since $\kappa$ is continuous. Exactly (reviewer, `m2_reduction.py`, $m=4,5$): every $(m,2)$ form $F_0,\dots,F_{m-1}$, $G_1,G_3,\dots$, reduced modulo $\sum a=b_1+b_2$, belongs to $S(m)|_{b_3=0}$, and on each $(m,2)$ chamber the exact maximum of $h-\varphi$ over $h\in S(m)$ is $0$ (GMP LPs), so $\max S|_{b_3=0}=\Phi$ identically. Numerically (author), $\max S(m,z\ge1)|_{b_3=0}=\Phi$ to $2\cdot10^{-15}$ at $3000$ random points per $m\le9$. The family-A forms restrict to the $F_k$.

*Reduction to one spike.* At $b_2=b_3=0$ the value is $\sum_jj\,a_j$ ([OneSpike] Theorem 3.1); after restriction and elimination of $b_1=\sum_j a_j$, this form occurs among the restrictions of $S(m)$ and dominates every other form on that face (exact for $m=4,5$; $4\cdot10^{-15}$ at random points for $m\le9$).

*Rank-adaptive bound.* $P\le\kappa_d$ ([RankAdaptive] Theorem 1.1) is a universal lower bound. The family-A layering $\{b_1,b_2,b_3\}\{a_1,a_2,a_3\}\{a_4,a_5,a_6\}\dots$ has cost $\sum_{j=1}^m\lceil j/3\rceil a_j$, which is strictly larger than $P$ on the open stratum when $m\ge4$. This stronger form, rather than the all-ones form, is exposed in the verified range (and conjecturally for all $m\ge4$).

*Fresh samples.* Independently of the chamber argument, $\kappa_d$ (hive LP, [KT99] honeycomb encoding, calibrated against the explicit Horn LP for $d\le9$) was compared with $\max S(m,z)$ at $2000$ fresh points per $(m,z)$ for $m=3,\dots,9$, $z\in\{0,1,3\}$ ($d\le14$), seven sampling laws including tie-heavy, dominant-$a_1$, flat-$b$ and the neighbourhood of the padding example: with default HiGHS tolerances the signed gap $\kappa-\max S$ is $\le6.2\cdot10^{-15}$ (never a missing form) while $\max S-\kappa$ reaches $2.5\cdot10^{-7}$ at a few near-tie points; every such point re-solved with feasibility tolerances $10^{-10}$ gives $|\kappa-\max S|\le2.2\cdot10^{-15}$. For $(9,2)$ the original run used an older script without the re-solve and left a residual of $1.8\cdot10^{-7}$; the rerun with the re-solve procedure for this manuscript (`verify_formula2.py 9 9 2000 2 2026`, 13 s) re-solves $17$ points and leaves $|\kappa-\max S|\le1.3\cdot10^{-15}$, and the reviewer's independent tight run gives $5.3\cdot10^{-15}$. The reviewer's own hive LP at $250$ points for each of the $21$ pairs $m=3,\dots,9$, $z\le2$ agrees with $\max S$ to $6\cdot10^{-15}$, and his explicit Horn LP ($d\le9$) to $1.1\cdot10^{-15}$.

## 8. Verification

*Discovery and closure (author).* Hive-LP duals at $1500+9000$ random points per $(m,z)$, $m\le7$, $z\le4$, rationalised, then filtered by the validity LP and the exposedness (chamber-radius) LP (`m3_forms.py`, `m3_gather.py`, `m3_analyze.py`, `m3_tools.py`); then the closure loop `m3_closure.py` (validity + exposedness filter, chamber vertices, hive LP at every vertex, new dual forms at any gap, repeat) for $m=2,\dots,9$, $z\le2$ ($z\le3$ for $m\le6$): every set closes in one iteration with maximal vertex gap $\le1.8\cdot10^{-14}$ and no new form (`closure_all.log`, `closure_z2.log`). The vertex-gap check is the same argument as Corollary 5.3 with $\kappa_d-g$ convex in place of a chain, and historically supplied numerical completeness evidence for $(8,2)$, $(9,1)$, $(9,2)$. In this candidate, completeness instead follows rigorously from the exact lower certificates and the exact chain upper bound; floating-point vertex gaps alone are not treated as proof. Horn-LP duals over the full Fulton lists ($522,2062,8752,39716$ triples for $d=6,\dots,9$) confirmed the tiling structure of the certificates before the catalogue was built (`m3_horn_duals.py`, `duals_m*_z*.log`).

*Certificates (author).* `certs.py m z` for all $d\le12$ (`certs_all.log`, $\le14$ s each): $10/10,\dots,69/69$ forms certified; tile counts as in Section 4.1. `familyA_cert.py 12 4` (2 s): $945$ exact family-A certificates.

*Coverage (author).* `coverage_vertices.py m z` for $m\le9$, $z\le2$ (`coverage_all.log`, `coverage_m*_z*.json`): $787$ chambers, $8\,775$ vertices, every chamber covered by a single chain feasible at all its vertices; the eight zero-insertions of Section 5.4. Matrices: `construct_C.py` (Section 5.4; $3$–$175$ s per $(m,z)$; `construct_all.log` contains one duplicated $m=8$ line and one superseded $m=5$, $z=0$ line from an earlier solver version, which are not counted). Rank: `rank_scan.py` (`rank_all.log`; the entries "(7,6)" there are a threshold artefact). Families: `families2.py` reproduces $S(m,1)$ for $m\le9$; `test_pred.py` at $m=10$, $z=1$: $1200$ points, $|\kappa-\max\mathrm{pred}|\le6.2\cdot10^{-15}$ with the predicted $87$ forms.

*Independent review (reviewer, own code in `repro/reviewer/`).* Tools written from scratch and calibrated first: Fulton recursion for $T^n_r$ ($3,12,41,142,522,2062,8752,39716$ triples for $n=2,\dots,9$, same counts as the author); LR coefficients by Jacobi–Trudi + Pieri, agreeing with $T^n_r$ membership on all $5521$ sum-condition triples with $n\le7$ and with `lr.py`, `lr2.py` on $1500$ random triples; Horn LP and hive LP in an own encoding agreeing to $10^{-14}$; exact rational LP and vertex enumeration (pycddlib); known values $\kappa_4(3,-1,-1,-1)=6$, $\kappa_5(4,-1^4)=10$, $\kappa_7=74/7$, $\kappa_8=73/7$ reproduced. Results: (a) `tiles_check.py`: $36$ certificates, $149$ tiles, all verified; dimension-free instantiation of tile signatures realisable at $z'=3$ ($24/24$), $z'=1$ ($79/82$, the three failures being the special tiles of the $z=0$-only forms) and $z'=0$ ($102/104$, two $z\ge1$ tiles with $U\ni m+1$ colliding with $N\ni d-2$ at $d'=m+3$, i.e. not meant for $z=0$); `tiles_dimfree2.py` as in Section 4.3. (b) `chain_own.py`: exact vertices and exact chain LP, $m=3,\dots,8$, $z\le2$ — identical vertex counts, identical eight zero-insertions. (c) `formula_check.py`, `extra_checks.py`: Section 7. (d) `padding_check.py`: Theorem 3(3) exactly and numerical rank-forcing samples on the new part for $m=4$; `extra_checks.py` for $m=5,7$. (e) `exposed_m5.py`: all $27$ ($z=0$) and $26$ ($z=1$) forms at $m=5$ have chamber radius $\ge1.7\cdot10^{-2}$ with $\kappa=g$ at the centre, and each is the unique argmax at least once in $6000$ samples. (f) `pred_m11.py`, `complete_m11.py`, `extra_checks.py`, `z0_extra.py`: Conjecture 4 at $m=10,11,12$ ($200$–$300$ points each, $|\kappa-\max\mathrm{pred}|\le7\cdot10^{-15}$); at $m=11$ all $103$ forms valid ($\min(\kappa-g)\ge-4.6\cdot10^{-15}$) and exposed (radius $\ge5.65\cdot10^{-3}$); chamber-vertex completeness at $m=10$ ($87$ chambers, $1353$ vertices, gap $\le3.0\cdot10^{-14}$) and $m=11$ ($103$ chambers, $1781$ vertices, $\le4.6\cdot10^{-14}$); the $z=0$ extras of Theorem 3(4). (g) `m2_reduction.py`: Section 7. (h) `construct_own.py`: $28$ explicit matrices. The review's reporting corrections (exact certificates only for $d\le12$; vertex total $8\,775$; the $(9,2)$ residual; the convexity argument via Horn sufficiency and Lemma 5.0; the family-A docstring; rank evidence for $m=5,7$; "multipliers rounded to $1$ and verified exactly") are applied throughout.

*Reruns for this manuscript* (`repro/run_fast.sh`, 2026-09-13, one core; logs and timings in `repro/logs/`): `verify_formula2.py 9 9 2000 2 2026` (14 s), `certs.py 4 1` (1 s), `familyA_cert.py 12 4` (1 s), `families2.py 3 9`, `coverage_vertices.py 4 1` (23 s), `test_pred.py 10 1 300` (3 s); reviewer's `tiles_check.py`, `m2_reduction.py`, `padding_check.py` (8 s), `chain_own.py 5` (3 s), `pred_m11.py` (7 s), `complete_m11.py` (13 s), `exposed_m5.py` (4 s); and `exact_strict.py` (Section 6). All outputs agree with the quoted ones. Reviewer's exact chain check at $m=9$ (`chain_m9.py z`, $542$, $544$, $546$ s for $z=0,1,2$; `logs/chain_own_m9_z{z}.log`): $969$ exact vertices each, every chamber covered by its base chain.


*Author-side exact completion for this revised candidate (14 September 2026).* The supplied catalogue was run at $(m,z)=(8,2),(9,1),(9,2)$, producing respectively $59$, $69$, $69$ explicit integer tiling certificates. Their tile counts are $325$, $416$, $416$ (Lidskii–Wielandt / row / column counts $232/71/22$, $307/87/22$, $307/87/22$); every multiplier is one, every total $s_t$ coefficient is at most one, every right-hand side equals the target form exactly, and both LR implementations give the same positive coefficient. The frozen objects are `author/certs_m8_z2.json`, `author/certs_m9_z1.json`, `author/certs_m9_z2.json`. The standalone `verify_all_tilings.py` checks these together with all supplied certificates without loading any pickle: $875$ certificates and $4\,342$ tiles pass, of which $787$ certificates cover Theorem 1 and $88$ cover the additional $z=3$, $m\le6$ checks.

The fresh exact upper-bound replay computed $3\,922$ chamber-vertex incidences for $m=3,\dots,8$, $z=0,1$, and $969$ for $m=9,z=0$. Every chamber admits one chain, with one zero required in the four padded chambers listed in Section 5.4. The $z=2$ upper bounds follow by inserting an unused zero into the already checked $z=1$ constructions; their coefficient sets coincide exactly. At $m=9$, all three coefficient sets coincide and every checked $z=0$ chain is a base chain, which pads to the two higher dimensions. Thus the fresh proof covers all upper cases without claiming that duplicate executions were performed. The exact padding LPs, four strict-decrease margins, $945$ family-A instances, $526$ rational strict exposedness witnesses, and all $90$ Appendix A form/layering rows were checked again. A fresh $1\,380$-point numerical hive comparison had maximal absolute discrepancy $8.44\cdot10^{-15}$; a $28$-matrix numerical construction had maximum commutator residual $4.2\cdot10^{-6}$ and cost residual $5.6\cdot10^{-7}$. These numerical checks are diagnostic, not proof objects. Logs and verification records are in `repro/fresh-20260914/`. This is author-side correction and verification, not a new independent assessment of this revised PDF.

## 9. Open questions

1. *A general-$m$ upper bound.* The $3\times3$ chain has no one-parameter recursion like Lemma 5.2 of [Mtwo]; the chain LP (5.2) at chamber vertices is the substitute. A closed description of the chain-feasibility regions of the families A–F would prove Conjecture 4's upper bound.
2. *General-$z$ validity of the B–F tiles* by the Pieri strip condition per tile family (Section 4.3).
3. *Exhaustiveness of the six families* and the origin of the quadratic count; a formula for $|S(m)|$.
4. *The padding rule.* Prove that an extra exposed form exists at $z=0$ iff $3$ does not divide $m$, identify its layering for all $m$, and prove the rank-$(m+1)$ forcing on the new part in general.
5. *Inertia $(m,n)$, $n\ge4$.* Whether $n\times n$-block shifts attain and tiles with $\lambda(J)$ of at most $n$ boxes certify; the $d=8$ inertia-$(4,4)$ phase of [RankOnset] Theorem 4.1 shows that rank $\max(n_+,n_-)$ cannot persist.
6. *Optimizers.* A classification of chambers by minimal optimal rank and by uniqueness of the optimal spectrum (only sampled here).

## 10. Reproducibility

The directory `repro/` accompanying this manuscript contains: `author/` — the supplied scripts, JSON files and logs (legacy pickles are omitted; proof replay rebuilds the small Fulton lists in memory), from the author's working directory, augmented by three new certificate files and the missing $m=3$, $z=2,3$ set aliases (`cycle2/work/A3_inertia_m3/`), including `closed_m{m}_z{z}.json` (the sets $S(m,z)$), `certs_m{m}_z{z}.json` (every tiling certificate), `coverage_m{m}_z{z}.json`, `pred_m{m}.json` ($m\le14$) and the logs quoted above; `reviewer/` — the reviewer's scripts and logs, with the only modification that two absolute paths were replaced by paths relative to `repro/` (marked in the source), plus `chain_m9.py`, a wrapper running the reviewer's exact chain check at $m=9$ one $z$ per process; `exact_strict.py` (Section 6); `run_fast.sh` and `logs/` with the reruns and timings; and `README.md` with commands, runtimes and expected final lines. Dependencies: Python 3.12, `numpy`, `scipy` (HiGHS, qhull), `pycddlib` (GMP) for the exact reviewer scripts. Literature queries (2026-09-13, three WebSearch queries on the Hilbert–Schmidt inverse self-commutator cost with prescribed spectrum, on block weighted shifts with prescribed self-commutator spectrum and Pieri certificates, and on follow-ups to Angel–Schechtman) returned only commutator norm inequalities, almost-commuting matrices, limiting Horn inequalities (arXiv:2410.08907), weighted-shift spectral theory, and [JOS13,AS15].

## AI-assistance statement

The received materials attribute their mathematics, computations and text to Claude Fable 5.1 agents (Anthropic) working under the direction of the author, who set the problem, selected the line of records and is responsible for the claims. A first agent performed the discovery computations and was interrupted by a usage limit; a second agent resumed from its files and completed the certificates, the coverage and the families; a third, independent agent carried out an adversarial review with its own implementations of every ingredient (Fulton recursion, Littlewood–Richardson coefficients, Horn and hive LPs, exact rational LPs and vertex enumeration), upgraded the upper bound to exact arithmetic for $m\le8$ (its script was rerun at $m=9$ for this manuscript), strengthened the conjecture at $m=10,11$ and listed the reporting corrections applied here; a fourth agent wrote this text, added the exact strict-decrease points of Section 6, ran the reviewer's exact check at $m=9$ and reran the fast scripts. The received materials also report that no fallback occurred; the historical model identities, independence and absence of fallback have not been independently attested. The author-side corrections and exact-certificate completion of this candidate used a fresh native OpenAI Codex task configured as `gpt-6-astra` with high reasoning and no forked conversation history. This configuration is recorded by dispatch metadata; technical context isolation and separate provider-side attestation are not claimed. The exact source and PDF hashes distinguish this candidate from the locally preassessed original. This revised candidate has not yet received a fresh exact-hash model assessment or human peer review.

\begingroup
\footnotesize

## Appendix A. The exposed forms for $m\le6$

Forms in canonical coordinates $(\alpha_1,\dots,\alpha_m;\beta_1,\beta_2)$, with family, $b$-schedule and level layering; the sets are $S(m,z\ge1)$, and the $z=0$-only forms are appended. Larger $m$: `repro/author/closed_m{m}_z{z}.json`.

$m=3$ ($10$ forms):

| form | fam. | $u$ | layering |
|---|---|---|---|
| $(-1,0,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_1\}\{b_3,a_2\}\{a_3\}$ |
| $(0,0,1;1,1)$ | A | $(0,0,1)$ | $\{b_1,b_2\}\{b_3,a_1,a_2\}\{a_3\}$ |
| $(0,1,1;1,0)$ | A | $(0,1,1)$ | $\{b_1\}\{b_2,b_3,a_1\}\{a_2,a_3\}$ |
| $(0,1,2;1,-1)$ | B | $(0,2,1)$ | $\{b_1\}\{b_3,a_1\}\{b_2,a_2\}\{a_3\}$ |
| $(1,0,1;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_2\}\{a_1,a_3\}$ |
| $(1,2,1;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_3\}\{a_2\}$ |
| $(2,1,1;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_2,a_3\}\{a_1\}$ |
| $(2,2,1;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_3\}\{a_1,a_2\}$ |
| $(2,3,1;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_3\}\{b_1,a_1\}\{a_2\}$ |
| $(3,1,2;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_2\}\{b_1,a_3\}\{a_1\}$ |

$m=4$ ($18$ forms, plus one at $z=0$):

| form | fam. | $u$ | layering |
|---|---|---|---|
| $(-1,0,0,1;2,1)$ | A | $(0,1,2)$ | $\{b_1\}\{b_2,a_1\}\{b_3,a_2,a_3\}\{a_4\}$ |
| $(-1,0,1,0;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_1\}\{b_3,a_2,a_4\}\{a_3\}$ |
| $(-1,0,1,1;2,0)$ | A | $(0,2,2)$ | $\{b_1\}\{a_1\}\{b_2,b_3,a_2\}\{a_3,a_4\}$ |
| $(-1,0,1,2;2,-1)$ | B | $(0,3,2)$ | $\{b_1\}\{a_1\}\{b_3,a_2\}\{b_2,a_3\}\{a_4\}$ |
| $(0,-1,0,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_2\}\{b_3,a_1,a_3\}\{a_4\}$ |
| $(0,0,1,1;1,1)$ | A | $(0,0,1)$ | $\{b_1,b_2\}\{b_3,a_1,a_2\}\{a_3,a_4\}$ |
| $(0,1,1,1;1,0)$ | A | $(0,1,1)$ | $\{b_1\}\{b_2,b_3,a_1\}\{a_2,a_3,a_4\}$ |
| $(0,1,1,2;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_1\}\{a_2,a_3\}\{a_4\}$ |
| $(0,1,2,1;1,-1)$ | B | $(0,2,1)$ | $\{b_1\}\{b_3,a_1\}\{b_2,a_2,a_4\}\{a_3\}$ |
| $(1,0,1,1;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_2\}\{a_1,a_3,a_4\}$ |
| $(1,1,1,2;0,0)$ | A | $(0,0,0)$ | $\{b_1,b_2,b_3\}\{a_1,a_2,a_3\}\{a_4\}$ |
| $(1,1,2,3;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_1,a_2\}\{a_3\}\{a_4\}$ |
| $(1,2,1,2;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_3\}\{a_2,a_4\}$ |
| $(2,1,1,2;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_2,a_3\}\{a_1,a_4\}$ |
| $(2,1,2,3;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_2\}\{a_1,a_3\}\{a_4\}$ |
| $(2,2,1,2;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_3\}\{a_1,a_2,a_4\}$ |
| $(2,3,1,2;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_3\}\{b_1,a_1,a_4\}\{a_2\}$ |
| $(3,1,2,2;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_2\}\{b_1,a_3,a_4\}\{a_1\}$ |
| $(1,2,3,4;-2,-1)$ | $z=0$ only | $(2,1,0)$ | $\{b_3\}\{b_2,a_1\}\{b_1,a_2\}\{a_3\}\{a_4\}$ |

$m=5$ ($26$ forms, plus one at $z=0$):

| form | fam. | $u$ | layering |
|---|---|---|---|
| $(-2,-1,-1,0,1;2,3)$ | C | $(1,0,3)$ | $\{b_2\}\{b_1,a_1\}\{a_2,a_3\}\{b_3,a_4\}\{a_5\}$ |
| $(-2,-1,0,0,1;3,1)$ | A | $(0,2,3)$ | $\{b_1\}\{a_1\}\{b_2,a_2\}\{b_3,a_3,a_4\}\{a_5\}$ |
| $(-2,-1,0,1,1;3,0)$ | A | $(0,3,3)$ | $\{b_1\}\{a_1\}\{a_2\}\{b_2,b_3,a_3\}\{a_4,a_5\}$ |
| $(-2,-1,0,1,2;3,-1)$ | B | $(0,4,3)$ | $\{b_1\}\{a_1\}\{a_2\}\{b_3,a_3\}\{b_2,a_4\}\{a_5\}$ |
| $(-1,-1,0,0,1;2,2)$ | A | $(0,0,2)$ | $\{b_1,b_2\}\{a_1,a_2\}\{b_3,a_3,a_4\}\{a_5\}$ |
| $(-1,0,0,1,1;2,1)$ | A | $(0,1,2)$ | $\{b_1\}\{b_2,a_1\}\{b_3,a_2,a_3\}\{a_4,a_5\}$ |
| $(-1,0,1,0,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_1\}\{b_3,a_2,a_4\}\{a_3,a_5\}$ |
| $(-1,0,1,1,1;2,0)$ | A | $(0,2,2)$ | $\{b_1\}\{a_1\}\{b_2,b_3,a_2\}\{a_3,a_4,a_5\}$ |
| $(-1,0,1,2,1;2,-1)$ | B | $(0,3,2)$ | $\{b_1\}\{a_1\}\{b_3,a_2\}\{b_2,a_3,a_5\}\{a_4\}$ |
| $(0,-1,0,1,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_2\}\{b_3,a_1,a_3\}\{a_4,a_5\}$ |
| $(0,0,1,1,1;1,1)$ | A | $(0,0,1)$ | $\{b_1,b_2\}\{b_3,a_1,a_2\}\{a_3,a_4,a_5\}$ |
| $(0,1,1,1,2;1,0)$ | A | $(0,1,1)$ | $\{b_1\}\{b_2,b_3,a_1\}\{a_2,a_3,a_4\}\{a_5\}$ |
| $(0,1,1,2,1;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_1\}\{a_2,a_3,a_5\}\{a_4\}$ |
| $(0,1,2,1,2;1,-1)$ | B | $(0,2,1)$ | $\{b_1\}\{b_3,a_1\}\{b_2,a_2,a_4\}\{a_3,a_5\}$ |
| $(1,0,1,1,2;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_2\}\{a_1,a_3,a_4\}\{a_5\}$ |
| $(1,1,1,2,2;0,0)$ | A | $(0,0,0)$ | $\{b_1,b_2,b_3\}\{a_1,a_2,a_3\}\{a_4,a_5\}$ |
| $(1,1,2,2,3;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_2\}\{a_3,a_4\}\{a_5\}$ |
| $(1,1,2,3,2;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_1,a_2\}\{a_3,a_5\}\{a_4\}$ |
| $(1,2,1,2,2;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_3\}\{a_2,a_4,a_5\}$ |
| $(1,2,1,2,3;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_1,a_3\}\{a_2,a_4\}\{a_5\}$ |
| $(1,2,2,3,3;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_1\}\{a_2,a_3\}\{a_4,a_5\}$ |
| $(2,1,1,2,2;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_2,a_3\}\{a_1,a_4,a_5\}$ |
| $(2,1,2,3,2;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_2\}\{a_1,a_3,a_5\}\{a_4\}$ |
| $(2,2,1,2,3;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_3\}\{a_1,a_2,a_4\}\{a_5\}$ |
| $(2,3,1,2,3;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_3\}\{b_1,a_1,a_4\}\{a_2,a_5\}$ |
| $(3,1,2,2,3;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_2\}\{b_1,a_3,a_4\}\{a_1,a_5\}$ |
| $(1,2,3,3,4;-2,-1)$ | $z=0$ only | $(2,1,0)$ | $\{b_3\}\{b_2,a_1\}\{b_1,a_2\}\{a_3,a_4\}\{a_5\}$ |

$m=6$ ($34$ forms, no extra at $z=0$):

| form | fam. | $u$ | layering |
|---|---|---|---|
| $(-3,-2,-1,0,0,1;4,1)$ | A | $(0,3,4)$ | $\{b_1\}\{a_1\}\{a_2\}\{b_2,a_3\}\{b_3,a_4,a_5\}\{a_6\}$ |
| $(-3,-2,-1,0,1,1;4,0)$ | A | $(0,4,4)$ | $\{b_1\}\{a_1\}\{a_2\}\{a_3\}\{b_2,b_3,a_4\}\{a_5,a_6\}$ |
| $(-3,-2,-1,0,1,2;4,-1)$ | B | $(0,5,4)$ | $\{b_1\}\{a_1\}\{a_2\}\{a_3\}\{b_3,a_4\}\{b_2,a_5\}\{a_6\}$ |
| $(-2,-1,-1,0,0,1;3,2)$ | A | $(0,1,3)$ | $\{b_1\}\{b_2,a_1\}\{a_2,a_3\}\{b_3,a_4,a_5\}\{a_6\}$ |
| $(-2,-1,-1,0,1,0;2,3)$ | C | $(1,0,3)$ | $\{b_2\}\{b_1,a_1\}\{a_2,a_3\}\{b_3,a_4,a_6\}\{a_5\}$ |
| $(-2,-1,0,-1,0,1;2,3)$ | C | $(1,0,3)$ | $\{b_2\}\{b_1,a_1\}\{a_2,a_4\}\{b_3,a_3,a_5\}\{a_6\}$ |
| $(-2,-1,0,0,1,1;3,1)$ | A | $(0,2,3)$ | $\{b_1\}\{a_1\}\{b_2,a_2\}\{b_3,a_3,a_4\}\{a_5,a_6\}$ |
| $(-2,-1,0,1,1,1;3,0)$ | A | $(0,3,3)$ | $\{b_1\}\{a_1\}\{a_2\}\{b_2,b_3,a_3\}\{a_4,a_5,a_6\}$ |
| $(-2,-1,0,1,2,1;3,-1)$ | B | $(0,4,3)$ | $\{b_1\}\{a_1\}\{a_2\}\{b_3,a_3\}\{b_2,a_4,a_6\}\{a_5\}$ |
| $(-1,-2,-1,0,0,1;2,3)$ | C | $(1,0,3)$ | $\{b_2\}\{b_1,a_2\}\{a_1,a_3\}\{b_3,a_4,a_5\}\{a_6\}$ |
| $(-1,-1,0,0,1,1;2,2)$ | A | $(0,0,2)$ | $\{b_1,b_2\}\{a_1,a_2\}\{b_3,a_3,a_4\}\{a_5,a_6\}$ |
| $(-1,0,0,1,1,1;2,1)$ | A | $(0,1,2)$ | $\{b_1\}\{b_2,a_1\}\{b_3,a_2,a_3\}\{a_4,a_5,a_6\}$ |
| $(-1,0,0,1,1,2;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_1\}\{b_3,a_2,a_3\}\{a_4,a_5\}\{a_6\}$ |
| $(-1,0,1,0,1,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_1\}\{b_3,a_2,a_4\}\{a_3,a_5,a_6\}$ |
| $(-1,0,1,1,1,2;2,0)$ | A | $(0,2,2)$ | $\{b_1\}\{a_1\}\{b_2,b_3,a_2\}\{a_3,a_4,a_5\}\{a_6\}$ |
| $(-1,0,1,2,1,2;2,-1)$ | B | $(0,3,2)$ | $\{b_1\}\{a_1\}\{b_3,a_2\}\{b_2,a_3,a_5\}\{a_4,a_6\}$ |
| $(0,-1,0,1,1,1;1,2)$ | C | $(1,0,2)$ | $\{b_2\}\{b_1,a_2\}\{b_3,a_1,a_3\}\{a_4,a_5,a_6\}$ |
| $(0,0,1,1,1,2;1,1)$ | A | $(0,0,1)$ | $\{b_1,b_2\}\{b_3,a_1,a_2\}\{a_3,a_4,a_5\}\{a_6\}$ |
| $(0,1,1,1,2,2;1,0)$ | A | $(0,1,1)$ | $\{b_1\}\{b_2,b_3,a_1\}\{a_2,a_3,a_4\}\{a_5,a_6\}$ |
| $(0,1,1,2,1,2;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_1\}\{a_2,a_3,a_5\}\{a_4,a_6\}$ |
| $(0,1,1,2,2,3;1,-1)$ | B | $(0,2,1)$ | $\{b_1\}\{b_3,a_1\}\{b_2,a_2,a_3\}\{a_4,a_5\}\{a_6\}$ |
| $(0,1,2,1,2,2;1,-1)$ | B | $(0,2,1)$ | $\{b_1\}\{b_3,a_1\}\{b_2,a_2,a_4\}\{a_3,a_5,a_6\}$ |
| $(1,0,1,1,2,2;0,1)$ | C | $(1,0,1)$ | $\{b_2\}\{b_1,b_3,a_2\}\{a_1,a_3,a_4\}\{a_5,a_6\}$ |
| $(1,1,1,2,2,2;0,0)$ | A | $(0,0,0)$ | $\{b_1,b_2,b_3\}\{a_1,a_2,a_3\}\{a_4,a_5,a_6\}$ |
| $(1,1,2,2,3,2;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_2\}\{a_3,a_4,a_6\}\{a_5\}$ |
| $(1,1,2,3,2,2;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_1,a_2\}\{a_3,a_5,a_6\}\{a_4\}$ |
| $(1,2,1,2,2,3;0,-1)$ | B | $(0,1,0)$ | $\{b_1,b_3\}\{b_2,a_1,a_3\}\{a_2,a_4,a_5\}\{a_6\}$ |
| $(1,2,1,2,3,2;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_1,a_3\}\{a_2,a_4,a_6\}\{a_5\}$ |
| $(1,2,2,3,3,2;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_1\}\{a_2,a_3,a_6\}\{a_4,a_5\}$ |
| $(2,1,1,2,2,3;-1,0)$ | D | $(1,0,0)$ | $\{b_2,b_3\}\{b_1,a_2,a_3\}\{a_1,a_4,a_5\}\{a_6\}$ |
| $(2,1,2,3,2,3;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_2\}\{a_1,a_3,a_5\}\{a_4,a_6\}$ |
| $(2,2,1,2,3,3;-1,-1)$ | E | $(1,1,0)$ | $\{b_3\}\{b_1,b_2,a_3\}\{a_1,a_2,a_4\}\{a_5,a_6\}$ |
| $(2,3,1,2,3,3;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_3\}\{b_1,a_1,a_4\}\{a_2,a_5,a_6\}$ |
| $(3,1,2,2,3,3;-2,-1)$ | F | $(2,1,0)$ | $\{b_3\}\{b_2,a_2\}\{b_1,a_3,a_4\}\{a_1,a_5,a_6\}$ |

\endgroup

## References

- [Mtwo] L. Eriksson, *The inverse self-commutator cost at inertia (m,2): a dimension-free closed formula, block-shift optimizers and a Pieri certificate*, AI Research Record, ARR-2026-1K33A7K90T87AREF (2026). Cited: (2.1)–(2.2), Theorems A–C$'$, Lemma 4.3 (Pieri triples), Corollary 4.6, Section 5.1 (block shifts), Lemma 5.0 (memorylessness), Open question 1.
- [FourLevel] L. Eriksson, *The Exact Four-Level Inverse Commutator Cost: Horn–Littlewood–Richardson Facets, Rank Transitions, and Sharp Loop Synthesis*, AI Research Record, ARR-2026-3M1EEG1T689ADSMW (2026). Cited: Theorem 2.2 (Horn program).
- [FiveLevel] L. Eriksson, *The Exact Five-Level Inverse Commutator Cost: Twelve Horn Chambers, Optimal Rank, and the Sharp 5/2 Resource Tax*, AI Research Record, ARR-2026-37B8R0QTA894GTFF (2026).
- [OneSpike] L. Eriksson, *One-Spike Inverse Self-Commutators and Exact Three-versus-Four-Kick Curvature Synthesis*, AI Research Record, ARR-2026-7NPRNBW4488HG90K (2026). Cited: Theorem 3.1.
- [RankOnset] L. Eriksson, *Sharp Onset and Unbounded Growth of Norm-Optimal Self-Commutator Rank*, AI Research Record, ARR-2026-5QQF95VHTC9GABH8 (2026). Cited: Lemma 2.1, Proposition 2.2, Remark 3.3 (padding example), Theorem 4.1.
- [RankAdaptive] L. Eriksson, *Sharp Rank-Adaptive Bounds for Inverse Self-Commutators*, AI Research Record, ARR-2026-1D2QV1RP1292JREW (2026). Cited: Theorem 1.1.
- [Ho62] A. Horn, Eigenvalues of sums of Hermitian matrices, *Pacific J. Math.* 12 (1962) 225–241.
- [Kl98] A. A. Klyachko, Stable bundles, representation theory and Hermitian operators, *Selecta Math. (N.S.)* 4 (1998) 419–445.
- [KT99] A. Knutson, T. Tao, The honeycomb model of $GL_n(\mathbb C)$ tensor products I: proof of the saturation conjecture, *J. Amer. Math. Soc.* 12 (1999) 1055–1090.
- [Fu00] W. Fulton, Eigenvalues, invariant factors, highest weights, and Schubert calculus, *Bull. Amer. Math. Soc.* 37 (2000) 209–249.
- [Fu97] W. Fulton, *Young Tableaux*, LMS Student Texts 35, Cambridge University Press, 1997 (Pieri rule).
- [Li50] V. B. Lidskii, On the characteristic numbers of the sum and product of symmetric matrices, *Dokl. Akad. Nauk SSSR* 75 (1950) 769–772.
- [Wi55] H. Wielandt, An extremum property of sums of eigenvalues, *Proc. Amer. Math. Soc.* 6 (1955) 106–110.
- [JOS13] W. B. Johnson, N. Ozawa, G. Schechtman, A quantitative version of the commutator theorem for zero trace matrices, *Proc. Natl. Acad. Sci. USA* 110 (2013) 19251–19255.
- [AS15] O. Angel, G. Schechtman, The Hilbert–Schmidt version of the commutator theorem for zero trace matrices, *Bull. London Math. Soc.* 47 (2015) 715–719; arXiv:1503.07980.
