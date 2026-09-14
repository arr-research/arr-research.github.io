# All-degree Born rigidity in dimensions four and three: an exact simplex optimum and a certified five-outcome frame

**Lluis Eriksson** (Independent researcher)

## Abstract

For an equal-trace rank-one POVM seed $F$ on $\mathbb{CP}^{d-1}$ the all-degree Born-rigidity gap is $\gamma(F)=\inf_{k\ge 2}g_k(F)$, where $g_k$ is the squared singular value of the orbit-normalisation operator on the projective harmonic sector of degree $k$, and $\Gamma_d$ is its supremum over outcome-simple seeds. A previous record proved $\Gamma_d=d-6/(d+1)$, attained only by an orthonormal basis, for $d\ge 5$, and left $d=3,4$ open. We prove an explicit tail bound $|Q_{n,d}(t)|\le(1-t)^{-(d-2)}/\binom{n+d-2}{n}$ for the normalised zonal function (a two-line corollary of Koornwinder's Laplace-type integral) and use it to settle $d=4$ exactly: $\Gamma_4=22018975/7340032=2.999847\ldots$, attained only by the regular five-outcome simplex, with the minimising degree $k=6$. In $d=3$ we prove $77/45<\Gamma_3\le 9/5$, certify $\Gamma_3\ge 1.776009937964733$ by an explicit five-outcome frame in exact arithmetic, and locate numerically a strict local maximum $1.7760099429996636\ldots$ with five tied degrees $4,8,9,12,16$.

## 1. Introduction

Fix a finite rank-one POVM seed $F=\{(w_i,x_i)\}_{i=1}^N$ in $\mathbb C^d$ and rotate it by every unitary. Under the homogeneous-response ansatz, normalisation on this orbit constrains a scalar ray response $f$ on $\mathbb{CP}^{d-1}$, and the strength of that constraint on the harmonic sector of degree $k$ is a number $g_k(F)$ (the record [Rec], Theorem 3.1). The optimal $L^2$ inverse constant off the affine trace-one quadratic sector is $\gamma(F)^{-1/2}$ with $\gamma(F)=\inf_{k\ge 2}g_k(F)$ ([Rec], Definition 3.2 and Theorem 3.3). The design question of [Rec] is: among outcome-simple equal-trace seeds, which seed has the largest gap $\Gamma_d=\sup_F\gamma(F)$? Its Theorem 5.2 answers this for $d\ge 5$: $\Gamma_d=d-6/(d+1)$, attained only by an orthonormal basis (ONB). The proof compares the ONB with the $N=d+1$ regular simplex at degree $k=3$ and kills $N\ge d+2$ by the ceiling $\gamma\le d^2/N$; the degree-three comparison reverses sign in $d=3$ and $d=4$ ([Rec], Section 7.1), and the record explicitly makes no claim there.

This paper settles $d=4$ and narrows $d=3$.

**Theorem A** ($d=4$). $\Gamma_4=22018975/7340032=2.999847276\ldots$, attained exactly and only by the regular five-outcome projective simplex ($w_i=4/5$, $|\langle x_i,x_j\rangle|^2=1/16$); the minimising degree is $k=6$. The ONB, with $\gamma=14/5$, is not optimal: $\gamma^{\mathrm{simp}}-\gamma^{\mathrm{ONB}}=7334427/36700160=0.19984727\ldots$

The proof is exact: rational arithmetic for the degrees $2\le k\le 10$ and an analytic tail bound (Lemma T) for $k\ge 11$. For tail control we give a self-contained two-line consequence of Koornwinder's Laplace-type integral representation of Jacobi polynomials (DLMF 18.10.3). This convenient bound is not claimed as new: Haagerup–Schlichtkrull [HS14], equation (20), already implies a stronger explicit bound in the integer-parameter range used here (Section 3). Our contribution is the exact low-dimensional optimisation and the certified three-dimensional construction, rather than a new Jacobi inequality. A second, structural observation is that the outcome count $N=5$ is rigid in $\mathbb C^4$ ([Rec], Lemma 5.1(ii)): there is no positive-dimensional family to optimise over, so the theorem reduces to one exact spectrum.

**Dimension three.** The picture that emerges is: $\Gamma_3$ is numerical (a five-outcome frame with no visible symmetry), $\Gamma_4$ is the simplex, $\Gamma_d$ is the ONB for $d\ge 5$. In $d=3$ we prove that the simplex has $\gamma=77/45$ (minimum at $k=4$), that every seed with $N\ge 6$ outcomes has $\gamma\le 3/2$ (the ONB value), that $\Gamma_3\le 9/5$, and that the supremum is attained. Five-outcome seeds form a four-dimensional family (Naimark complement: five unit Bloch vectors with zero sum, modulo rotations). We exhibit an explicit frame in that family, specified by Bloch vectors with coordinates in $\mathbb Q(\sqrt q)$, and certify in exact integer arithmetic that its gap is at least $1.776009937964733$. Hence $\Gamma_3\ge 1.776009937964733>77/45>3/2$: in $d=3$ neither the ONB nor the simplex is optimal and the maximiser has $N=5$. The conjectured value, $\Gamma_3=1.77600994299966361808\ldots$, and the identity of the proposed maximiser (optimum B, five tied degrees $4,8,9,12,16$, all Karush–Kuhn–Tucker multipliers positive) are numerical, supported by four differential-evolution runs and 270 local multistarts, and stated as such.

**Status, stated honestly.** Lemma T and Theorem A are proved (Theorem A computer-assisted with exact rational arithmetic; no floating point enters). In $d=3$, the ceiling $9/5$, the simplex value $77/45$, the reduction to $N=5$ and the lower bound $1.776009937964733$ are proved (the last computer-assisted, exact). The value of $\Gamma_3$ and the global optimality of B are numerical. An independent adversarial review (Section 6) re-derived every proof and recomputed every number with its own code; its three corrections (a wrong rational for the ONB–simplex difference, a missing multistart census, one citation year) are incorporated. The literature account was corrected in this revision to acknowledge the stronger explicit estimate already implied by [HS14], equation (20). The searches described in Section 6 did not locate the exact low-dimensional all-degree results; a null search does not certify priority.

## 2. Setting

Everything is as in [Rec]; we restate what is used. Let $d\ge 3$. A *seed* is $F=\{(w_i,x_i)\}_{i=1}^N$ with $x_i$ unit vectors in $\mathbb C^d$ (representatives of points of $\mathbb{CP}^{d-1}$), $w_i>0$ and $\sum_iw_iP_{x_i}=I_d$ ([Rec], Definition 2.1). It is *equal-trace* if $w_i=d/N$ for all $i$ and *outcome-simple* if the rays $x_i$ are pairwise distinct. $\mathcal F_d$ is the class of finite outcome-simple equal-trace seeds, modulo unitary equivalence and relabelling. Weights are not free in this class; the unequal-weight problem is outside it ([Rec], Section 7.3).

Let $H_k$ be the projective harmonic sector of degree $k$: the restrictions to the unit sphere of harmonic polynomials of bidegree $(k,k)$, the $U(d)$-irreducible of highest weight $(k,0,\ldots,0,-k)$. Its normalised zonal function is
$$Q_{k,d}(t)=\frac{P_k^{(d-2,0)}(2t-1)}{\binom{d+k-2}{k}},\qquad Q_{k,d}(1)=1,$$
a Koornwinder disk polynomial in the overlap $t=|\langle x,y\rangle|^2$. The spectral formula ([Rec], Theorem 3.1) is
$$g_k(F)=\sum_{i,j=1}^Nw_iw_j\,Q_{k,d}\big(|\langle x_i,x_j\rangle|^2\big),\tag{2.1}$$
and the gap is $\gamma(F)=\inf_{k\ge 2}g_k(F)$ ([Rec], Definition 3.2). Degree $k=1$ is excluded because $g_1=0$ for every POVM (completeness is equivalent to $g_1=0$), so $\inf_{k\ge 1}g_k$ would vanish identically; degree $0$ is the trace normalisation. Finally $\Gamma_d=\sup_{F\in\mathcal F_d}\gamma(F)$.

Two facts from [Rec] are used and were re-derived. First, ([Rec], Lemma 5.1) an equal-trace seed has $N\ge d$; $N=d$ forces an ONB with $w_i=1$; $N=d+1$ forces the regular projective simplex, unique up to unitary equivalence and phases, with $w_i=d/(d+1)$ and $|\langle x_i,x_j\rangle|^2=1/d^2$ for $i\ne j$ (the Gram matrix is $\frac{d+1}{d}(I-uu^*)$ with $|u_i|^2=1/(d+1)$; rephasing makes $u$ constant). This is the classical statement that an equiangular tight frame of $d+1$ vectors is the simplex, the Welch-bound-saturating case $(N-d)/(d(N-1))=1/d^2$ [Tr05, FJMP18, We74]. Second, the ONB spectrum ([Rec], (10)):
$$g_k^{\mathrm{ONB}}(d)=d\Big[1+(d-1)\frac{(-1)^k}{\binom{d+k-2}{k}}\Big],\qquad \gamma^{\mathrm{ONB}}(d)=g_3^{\mathrm{ONB}}(d)=d-\frac{6}{d+1},\tag{2.2}$$
the odd-degree values increasing in $k$ and the even-degree values exceeding $d$. For the simplex, $g_k^{\mathrm{simp}}(d)=\frac{d^2}{d+1}\big[1+d\,Q_{k,d}(1/d^2)\big]$.

## 3. Lemma T: an explicit tail bound for the zonal function

**Lemma T.** For $d\ge 3$, $0\le t<1$ and every $n\ge 0$,
$$|Q_{n,d}(t)|\le\frac{(1-t)^{-(d-2)}}{\binom{n+d-2}{n}}.\tag{3.1}$$
At $t=0$ this is an equality: $Q_{n,d}(0)=(-1)^n/\binom{n+d-2}{n}$.

*Proof.* (a) *Integral representation.* Let $K=U(d-1)\subset U(d)$ be the stabiliser of $e_1$. Put $a=e_1+e_2$, $b=e_1-e_2$, so $\langle a,b\rangle=0$, and $h(\xi)=(\langle\xi,a\rangle\langle b,\xi\rangle)^n$ on $\mathbb C^d$, with $\langle\cdot,\cdot\rangle$ linear in the first slot. Then $h$ is bihomogeneous of bidegree $(n,n)$ and harmonic: with $\Delta=4\sum_j\partial^2/\partial\xi_j\partial\bar\xi_j$,
$$\Delta h=4n^2\Big(\sum_j\bar a_jb_j\Big)(\langle\xi,a\rangle\langle b,\xi\rangle)^{n-1}=4n^2\langle b,a\rangle(\cdots)^{n-1}=0 .$$
Hence $h$ restricted to the sphere descends to $\mathbb{CP}^{d-1}$ and lies in $H_n$. The $K$-average $\xi\mapsto\int_Kh(k\xi)\,dk$ is a $K$-invariant element of $H_n$, hence a scalar multiple of the zonal function $\xi\mapsto Q_{n,d}(|\xi_1|^2)$; evaluating at $e_1$ (fixed by $K$, $h(e_1)=1$, $Q_{n,d}(1)=1$) shows that the scalar is $1$. Write $t=|\xi_1|^2$, $\xi'=(\xi_2,\ldots,\xi_d)$, so $|\xi'|^2=1-t$, and $w=(k\xi')_1/|\xi'|$. For Haar-random $k\in U(d-1)$, $w$ is the first coordinate of a uniform point on the unit sphere of $\mathbb C^{d-1}$, so $u=|w|^2\sim\mathrm{Beta}(1,d-2)$ (density $(d-2)(1-u)^{d-3}$ on $[0,1]$) with a uniform phase independent of $u$. Since $h(k\xi)=\big[|\xi_1|^2-|(k\xi')_1|^2+2i\,\mathrm{Im}\big((k\xi')_1\bar\xi_1\big)\big]^n$,
$$Q_{n,d}(t)=\mathbb E[z^n],\qquad z=t-(1-t)u+2i\sqrt{t(1-t)}\,\sqrt u\cos\varphi,\tag{3.2}$$
with $u\sim\mathrm{Beta}(1,d-2)$ and $\varphi\sim\mathrm{Unif}[0,\pi]$ independent. This is Koornwinder's Laplace-type integral (DLMF 18.10.3 [DLMF], with $\alpha=d-2>\beta=0>-1/2$, whose constant $2\Gamma(\alpha+1)/(\sqrt\pi\,\Gamma(\alpha-\beta)\Gamma(\beta+\tfrac12))$ reduces to $2(d-2)/\pi$ and whose measure $(1-r^2)^{d-3}r\,dr\,d\varphi$ becomes, with $u=r^2$, the product measure above), proved in [Ko74, As74] and in the group-theoretic form used here in [Ko73]. Independently of the literature, (3.2) was verified as an exact polynomial identity in $t$ for $0\le n\le 40$ and $d=3,4,5,6$ (script `s2`, Section 8), which covers every degree that enters Theorem A exactly.

*(b) Bound.* $|z|^2=(t-(1-t)u)^2+4t(1-t)u\cos^2\varphi\le(t+(1-t)u)^2\le 1$. Hence, with $v=t+(1-t)u$, $1-u=(1-v)/(1-t)$, $du=dv/(1-t)$,
$$\begin{aligned}
|Q_{n,d}(t)|&\le\mathbb E\big[(t+(1-t)u)^n\big]\\
&=(d-2)(1-t)^{-(d-2)}\int_t^1v^n(1-v)^{d-3}\,dv\\
&\le(d-2)(1-t)^{-(d-2)}B(n+1,d-2).
\end{aligned}$$
and $(d-2)B(n+1,d-2)=n!(d-2)!/(n+d-2)!=1/\binom{n+d-2}{n}$. At $t=0$, $z=-u$ and $\mathbb E[(-u)^n]=(-1)^n/\binom{n+d-2}{n}=P_n^{(d-2,0)}(-1)/\binom{n+d-2}{n}$. $\square$

The lemma holds for all $n\ge 0$; the thresholds "$k\ge 11$" and "$k\ge 14$" below are only where (3.1) beats a specific exact value. Numerically, over $d\in\{3,\ldots,6\}$, a grid of $t$ and $n\le 400$, the ratio $|Q_{n,d}(t)|\binom{n+d-2}{n}(1-t)^{d-2}$ equals $1$ only at $t=0$ and is at most $0.9212$ for $t>0$ (reviewer's script `r2b`).

**Corollary 3.1** (ceiling with a rate). For an outcome-simple equal-trace seed with $N$ outcomes, $g_k(F)\to d^2/N$ as $k\to\infty$; hence $\gamma(F)\le d^2/N$. *Proof.* In (2.1) the diagonal terms contribute $\sum_iw_i^2=N(d/N)^2=d^2/N$ since $Q_{k,d}(1)=1$; each off-diagonal overlap is $<1$ by outcome-simplicity, and $Q_{k,d}(t)\to 0$ by (3.1) because $\binom{k+d-2}{k}\to\infty$. Then $\gamma=\inf_{k\ge 2}g_k\le\lim_kg_k$. $\square$

This recovers [Rec], Lemma 4.1 and Proposition 4.2 with an explicit rate and without Darboux asymptotics. The Bernstein-type inequality of Chow–Gatteschi–Wong [CGW94] is stated for $-\tfrac12\le\alpha,\beta\le\tfrac12$ (DLMF 18.14.3) and does not cover $\alpha=d-2\ge 1$; the main uniform inequality of Haagerup–Schlichtkrull [HS14], Theorem 1.1, assumes $\alpha,\beta\ge0$. More directly, their normalisation on page 1 and equation (20) on page 6 give $|g_n^{(\alpha,\beta)}(x)|\le1$ for nonnegative integer parameters. Setting $\alpha=d-2$, $\beta=0$ and $x=2t-1$ cancels their gamma-function prefactor and yields
$$|Q_{n,d}(t)|\le\frac{(1-t)^{-(d-2)/2}}{\binom{n+d-2}{n}}.\tag{3.3}$$
This is stronger than (3.1) for $0<t<1$ and $d\ge3$. Thus Lemma T follows from an existing explicit estimate; we retain its elementary integral proof and the conservative thresholds based on (3.1). The generalised Jacobi-weight questions of [EMN94] are related background, and are not needed for this argument.

## 4. Theorem A: dimension four

**Theorem A.** $\Gamma_4=22018975/7340032=2.999847276\ldots$, attained exactly by the regular five-outcome projective simplex ($w_i=4/5$, $|\langle x_i,x_j\rangle|^2=1/16$ for $i\ne j$), which is the unique maximiser in $\mathcal F_4$ up to unitary equivalence, phases and relabelling. The minimum over degrees is attained only at $k=6$, where $Q_{6,4}(1/16)=-7345637/469762048=-0.0156369\ldots$ In particular the ONB ($\gamma=14/5$) is not optimal in $d=4$, and
$$\gamma^{\mathrm{simp}}(4)-\gamma^{\mathrm{ONB}}(4)=\frac{22018975}{7340032}-\frac{14}{5}=\frac{7334427}{36700160}=0.19984727\ldots$$

*Proof.* By [Rec], Lemma 5.1, a seed in $\mathcal F_4$ has $N=4$ (ONB), $N=5$ (simplex) or $N\ge 6$.

(i) $N=4$: by (2.2), $\gamma^{\mathrm{ONB}}(4)=\min_k4[1+3(-1)^k/\binom{k+2}{k}]=14/5$ at $k=3$ (values $6,\ 14/5,\ 24/5,\ 24/7,\ 31/7,\ 11/3,\ldots$ for $k=2,3,\ldots$).

(ii) $N\ge 6$: by Corollary 3.1, $\gamma\le 16/N\le 8/3<14/5$.

(iii) $N=5$: the seed is the simplex and $g_k=\frac{16}{5}\big[1+4Q_{k,4}(1/16)\big]$. The exact values, computed with a three-term recurrence in rational arithmetic and cross-checked against `sympy.jacobi` (author's `s1`, `s2`; reviewer's `r1`), are given in Table 1.

| $k$ | $g_k^{\mathrm{simp}}(4)$ exact | decimal |
|---|---|---|
| 2 | $33/8$ | $4.1250000$ |
| 3 | $49/16$ | $3.0625000$ |
| 4 | $1563/512$ | $3.0527344$ |
| 5 | $49041/14336$ | $3.4208287$ |
| 6 | $22018975/7340032$ | $2.9998473$ |
| 7 | $219021/65536$ | $3.3419952$ |
| 8 | $104799063/33554432$ | $3.1232555$ |
| 9 | $4754959807/1476395008$ | $3.2206556$ |
| 10 | $608283021429/188978561024$ | $3.2187938$ |

Table 1: exact spectrum of the five-outcome simplex in $\mathbb C^4$, degrees $2\le k\le 10$.

Exact comparison of the entries gives $\min_{2\le k\le 10}g_k=g_6$, with $g_k>g_6$ for every other $k$ in this range (the script checks $2\le k\le 400$, redundantly). For $k\ge 11$, Lemma T with $t=1/16$, $d=4$ gives
$$|Q_{k,4}(1/16)|\le\Big(\frac{16}{15}\Big)^2\frac{2}{(k+1)(k+2)}\le\Big(\frac{16}{15}\Big)^2\frac{1}{78}=0.014587<0.0156369=-Q_{6,4}(1/16),$$
so $g_k>g_6$ for all $k\ge 11$. The exact check cannot stop earlier: at $k=10$ the Lemma T bound is $(16/15)^2/66=0.017239>0.015637$, so $k=10$ must be, and is, compared exactly. Therefore $\gamma^{\mathrm{simp}}(4)=g_6=22018975/7340032$, attained at $k=6$ only.

(iv) $22018975/7340032=2.99985>14/5>8/3$. The simplex is the unique $N=5$ class, so it is the unique maximiser and $\Gamma_4=22018975/7340032$. $\square$

*What is exact and what is finite.* Everything in the proof is exact rational arithmetic or analytic; the finite parts are the ten values of Table 1 and, as a redundant check of the zonal-function identification, the symbolic identity (3.2) for $n\le 40$. No floating-point number enters Theorem A.

*Remark (correction to the working brief).* The brief for this problem asked for a finite optimisation over a "four-parameter family of five-outcome frames in $d=4$". No such family exists: $N=d+1$ equal-trace seeds are rigid ([Rec], Lemma 5.1(ii)). The four-dimensional family lives in $d=3$, $N=5$ (Section 5).

## 5. Dimension three

### 5.1 Proved facts: ceiling, simplex, reduction to five outcomes

**Proposition 5.1.** In $d=3$: (a) every seed with $N\ge 6$ has $\gamma\le 9/6=3/2=\gamma^{\mathrm{ONB}}(3)$; (b) the ONB has $\gamma=3/2$ (at $k=3$); (c) the regular simplex ($N=4$, $w_i=3/4$, overlaps $1/9$) has $\gamma^{\mathrm{simp}}(3)=77/45=1.7111\ldots$, attained only at $k=4$, where $Q_{4,3}(1/9)=-97/1215$; (d) $\Gamma_3=\max\big(77/45,\ \sup_{N=5}\gamma\big)\le 9/5$, and the supremum over $N=5$ is attained; hence $\Gamma_3$ is attained, by the simplex or by a five-outcome seed.

*Proof.* (a) is Corollary 3.1; (b) is (2.2) with $d=3$: $g_k=3[1+2(-1)^k/(k+1)]$, minimum $3/2$ at $k=3$. (c) $g_k=\frac94[1+3Q_{k,3}(1/9)]$; exact values for $2\le k\le 13$ (script `s1`; the two smallest are $77/45$ at $k=4$ and $90863/45927=1.9784$ at $k=6$) give the minimum $g_4$; for $k\ge 14$, Lemma T gives $|Q_{k,3}(1/9)|\le\frac{9}{8}\cdot\frac{1}{k+1}\le\frac{9}{120}=0.075<0.079835=-Q_{4,3}(1/9)$, while at $k=13$ the bound is $0.08036$, so $k=13$ is inside the exact range. (d) With $N=5$ the ceiling is $9/5$; $77/45<9/5$ and $3/2<77/45$ give the first statement. Attainment: the $N=5$ family is compact (Section 5.2), each $g_k$ is continuous, so $\gamma=\inf_kg_k$ is upper semicontinuous and attains its supremum on a compact set. $\square$

### 5.2 The five-outcome family: Naimark complement and Bloch vectors

Let $X\in\mathbb C^{3\times 5}$ have unit columns $x_i$ with $XX^*=\frac53I_3$ (equal trace, $w_i=3/5$). The Gram matrix $G=X^*X$ equals $\frac53P$ with $P$ a rank-three orthogonal projection, and $\frac53(I_5-P)$ is the Gram matrix of five vectors $y_i\in\mathbb C^2$ with $|y_i|^2=\frac53(1-\frac35)=\frac23$ and $\langle x_i,x_j\rangle=-\langle y_i,y_j\rangle$ for $i\ne j$. Writing $y_iy_i^*=\frac13(I_2+n_i\cdot\sigma)$ with unit Bloch vectors $n_i\in S^2$,
$$|\langle x_i,x_j\rangle|^2=|\langle y_i,y_j\rangle|^2=\frac49\cdot\frac{1+n_i\cdot n_j}{2}=\frac29(1+n_i\cdot n_j),\qquad\sum_iy_iy_i^*=\frac53I_2+\frac13\Big(\sum_in_i\Big)\cdot\sigma ,$$
so tightness of the $y$'s is $\sum_in_i=0$. Conversely five unit Bloch vectors with zero sum give a tight frame in $\mathbb C^2$ whose complementary Gram $\frac53I_5-\frac53P'$ is the Gram of a five-outcome equal-trace seed in $\mathbb C^3$. The overlaps satisfy $|\langle x_i,x_j\rangle|^2\le 4/9<1$, so every such seed is outcome-simple. By (2.1) the objective depends only on the Gram matrix $(n_i\cdot n_j)$:
$$g_k=\frac{9}{25}\Big[5+2\sum_{i<j}Q_{k,3}(t_{ij})\Big],\qquad t_{ij}=\frac29(1+n_i\cdot n_j),\qquad g_k\to\frac95 .\tag{5.1}$$
For optimisation of the objective, the parameter space $\{(n_1,\ldots,n_5)\in(S^2)^5:\sum n_i=0\}/O(3)$ is compact of dimension $10-3-3=4$. The unitary action on Bloch vectors corresponds to $SO(3)$; quotienting by $O(3)$ additionally identifies conjugate configurations, which have the same overlaps and objective. This extra identification does not affect the supremum or attainment. The exact parametrisation used in all searches (no penalty term): $n_1,n_2,n_3$ free, $s=n_1+n_2+n_3$ with $|s|\le 2$, $n_{4,5}=-s/2\pm v$ with $v\perp s$, $|v|^2=1-|s|^2/4$; seven angles, three of them redundant under $SO(3)$.

### 5.3 Numerical optimum B and the second local maximum A

*Global search.* `s3` (scipy `differential_evolution`, population $40\times 7$, Sobol initialisation, up to $3000$ generations, tolerance $10^{-12}$, then four rounds of Nelder–Mead and Powell; $300$ degrees during the search, $2000$ for the final spectrum; $20$–$25$ minutes per seed) was run with four seeds. Seeds $0$ and $1$ converged to $\gamma=1.776009943000$ with five tied degrees $k=4,8,9,12,16$ (*optimum B*); seeds $2$ and $3$ to $\gamma=1.775372547336$ with tied degrees $5,6,8,12,18$ (*optimum A*). Both exceed the simplex value $77/45=1.7111$ and the earlier penalty-method value $1.77194$ of this line, which was not exactly feasible ($|\sum n_i|=8\cdot 10^{-5}$).

*Multistart census.* `s3b` draws random feasible starts and runs three rounds of Nelder–Mead and Powell on each (about $37$ s per start). Three batches were run: batch 1 (default seed, $30$ starts, $1114$ s) and batch 2 (seeds $21$–$24$; $34,32,24,30$ starts, $4456$ s) log the ten best values per batch; batch 3 (seeds $31$–$34$; $27,26,26,29$ starts, $5241$ s) logs every local optimum with its active set. Table 2 gives the full census of batch 3.

| count | $\gamma$ | active degrees |
|---|---|---|
| 20 | 1.7760099 | 4, 8, 9, 12, 16 (B) |
| 1 | 1.7760099 | 8, 9, 12, 16 (B, not fully converged) |
| 23 | 1.7753725 | 5, 6, 8, 12, 18 (A) |
| 3 | 1.7752–1.7754 | subsets of the ties of A (not fully converged) |
| 11 | 1.7714479 | 5, 6, 9, 18, 29 |
| 2 | 1.7698530 | 4, 6, 9, 18, 29 |
| 3 | 1.7698108 | 4, 6, 8, 18, 29 |
| 1 | 1.7697419 | 4, 6, 8, 16, 20 |
| 2 | 1.7684799 | 5, 6, 8, 16, 22 |
| 21 | 1.7677921 | 3, 5, 6, 16, 22 |
| 2 | 1.7674484 | 5, 6, 8, 11, 20 |
| 1 | 1.7674007 | 5, 6, 8, 11, 18 |
| 6 | 1.7665272 | 3, 5, 6, 9, 22 |
| 1 | 1.7649654 | 4, 5, 9, 12, 18 |
| 5 | 1.7568215 | 3, 6, 9, 12, 16 |
| 1 | 1.7544253 | 3, 5, 9, 12, 16 |
| 5 | 1.7675–1.7699 | two to four ties only (not fully converged) |

Table 2: census of the $108$ local optima of batch 3 (seeds $31$–$34$), values rounded to $7$ digits, grouped by active set.

In batches 1 and 2 the ten best values per batch were $6/9/6/5/7$ hits of B and $3/1/4/5/2$ hits of A (batch 1, then seeds $21,22,23,24$), plus two isolated values, $1.77589251$ (batch 1) and $1.77539759$ (seed 24), that did not recur in the per-start census of batch 3 and are most plausibly incompletely converged points near A or B; they were not refined. Over all $270$ multistarts (including the reviewer's independent $12$-start run, Section 6: three hits of B, four of A, two of $1.7677921$, one of $1.7674484$, two of $1.7568215$), B was the best value in every batch, was reached at least $56$ times, and no value above $1.7760099430$ was ever observed. The landscape is rich: fourteen distinct five-tie values above $1.75$ were returned, all with the generic "five active degrees in four degrees of freedom" structure (only A and B were subjected to the KKT analysis below).

*Refinement to 40 digits* (`s6`, mpmath, $40$ digits). Gauss–Newton with a pseudo-inverse on the four tie equations converges quadratically from the float optimum (residual $10^{-28}$ after one step, then $0$ at working precision):
$$\gamma_B=1.77600994299966361808274335434298818\ldots\quad(g_4=g_8=g_9=g_{12}=g_{16}),$$
$$\gamma_A=1.77537254733646573261448304592585103\ldots\quad(g_5=g_6=g_8=g_{12}=g_{18}).$$
At B the next degrees are $g_5=1.77614303734$, $g_6=1.77692094836$, $g_{22}=1.77831392549$; at A, $g_9=1.77935107582$, $g_{29}=1.78036182092$. The Gram matrix $(n_i\cdot n_j)$ of B is given in Table 3 to $20$ digits (the $40$-digit data are in `s6_refined_B.json`; those of A in `s6_refined.json`).

| $(i,j)$ | $n_i\cdot n_j$ |
|---|---|
| (1,2) | $-0.67842266787263714880$ |
| (1,3) | $0.60176255795439951187$ |
| (1,4) | $-0.59255829171541443911$ |
| (1,5) | $-0.33078159836634792396$ |
| (2,3) | $0.15386171600661905357$ |
| (2,4) | $-0.04298464090164038497$ |
| (2,5) | $-0.43245440723234151981$ |
| (3,4) | $-0.94165867347132659257$ |
| (3,5) | $-0.81396560048969197287$ |
| (4,5) | $0.57720160608838141664$ |

Table 3: Bloch Gram matrix of optimum B, $t_{ij}=\frac{2}{9}(1+n_i\cdot n_j)$.

All ten entries are distinct; no symmetry is visible; `mpmath.findpoly` and `identify` find no algebraic relation of degree $\le 8$ with coefficients up to $10^6$ for $\gamma_A$, $\gamma_B$, the Gram entries or their power sums, apart from $\sum_{i<j}n_i\cdot n_j=-5/2$, which is forced by $\sum n_i=0$.

*First-order optimality (KKT).* At B the $5\times 7$ matrix of gradients of the active $g_k$ with respect to the seven angles has rank $4$ (singular values $1.476,\ 0.407,\ 0.336,\ 0.123,\ 2\cdot 10^{-26}$; the three-dimensional null space is the $SO(3)$ orbit), and the multipliers solving $\sum_k\lambda_k\nabla g_k=0$, $\sum_k\lambda_k=1$ are
$$\lambda=(0.10633,\ 0.24897,\ 0.21648,\ 0.12593,\ 0.30229)\quad\text{for }k=(4,8,9,12,16),$$
all strictly positive, with residual $3\cdot 10^{-26}$. (The preserved historical output carries a hard-coded header "$k=5,6,8,12,18$" copied from the run for A; the multipliers listed here belong to B. The revised script now derives its labels from the actual active set.) At A: rank $4$, $\lambda=(0.0197,\ 0.5875,\ 0.0424,\ 0.0796,\ 0.2707)$ for $k=(5,6,8,12,18)$. The relevant exact criterion is conditional: if an exact tied point has positive multipliers and active gradients spanning the four-dimensional tangent space of the quotient, then $0$ lies in the interior of their convex hull. For every nonzero tangent direction $v$ some active $k$ then has $\langle\nabla g_k,v\rangle<0$; otherwise the positive weighted sum would force all inner products to vanish, contradicting the rank. Compactness of the unit tangent sphere makes the decrease uniform, so this criterion yields a strict local maximum without second-order analysis. The computed ranks and multipliers support this vertex structure for A and B, but do not certify an exact root or the hypotheses of the criterion. For B, the non-active degrees are numerically separated by at least $1.3\cdot10^{-4}$ and the Lemma-T tail beyond degree $2000$ is at least $1.79559$. The four tie equations are polynomial of degree $\le16$ (B) or $\le18$ (A) in the ten overlaps, subject to the Gram constraints. Their numerically nonsingular quotient Jacobian is consistent with isolated algebraic solutions; no exact algebraic isolation is claimed.

### 5.4 Exact certified lower bound

From the $40$-digit point B, `s5` builds an exact frame $F_B^{\mathrm{ex}}$: $n_1,n_2,n_3$ are rational unit vectors (stereographic images of rational points with denominator $10^8$), $w$ is a rational vector orthogonal to $s=n_1+n_2+n_3$, and $n_{4,5}=-s/2\pm\sqrt q\,w$ with $q=(1-|s|^2/4)/|w|^2\in\mathbb Q$, $q>0$; unit norms and $\sum n_i=0$ hold identically and were asserted in exact rational arithmetic. All overlaps $t_{ij}$ then lie in $\mathbb Q(\sqrt q)$, and `s4int` evaluates $g_k$ for $2\le k\le 600$ exactly in $\mathbb Z[\rho]$ up to an integer scale, $\rho=\sqrt{q_nq_d}$, by the integer-scaled three-term recurrence (no gcd, no floating point), replaces $\rho$ by an integer enclosure (`isqrt`, $40$ digits, the side chosen by the sign of the $\rho$-coefficient) and floors to $10^{-30}$. The tail uses Lemma T with $d=3$: for $k>600$,
$$g_k\ \ge\ \frac{9}{25}\Big[5-\frac{2S}{k+1}\Big]\ \ge\ \frac{9}{25}\Big[5-\frac{2S}{602}\Big]\ \ge\ 1.78533,\qquad S=\sum_{i<j}(1-t_{ij})^{-1}\le 12.2591 .$$
The result ($14$ s on rerun) is
$$\gamma(F_B^{\mathrm{ex}})\ \ge\ \frac{177600993796473305296398794157}{10^{29}}=1.776009937964733\ldots,$$
the minimum over $k$ occurring at $k=9$; the five near-tied degrees $9,16,12,4,8$ all lie in $[1.7760099379,\ 1.7760099493]$. The reviewer's independent $60$-digit evaluation of the same exact frame gives $g_9=1.776009937964733053$, consistent with the certificate to every printed digit.

**Theorem B** ($d=3$, proved, computer-assisted). $\Gamma_3\ge 1.776009937964733>77/45>3/2$. Consequently, in $d=3$ the ONB and the simplex are both non-optimal, and every maximiser of $\gamma$ on $\mathcal F_3$ (which exists by Proposition 5.1) has exactly five outcomes. Together with Proposition 5.1(d), $1.776009937964733\le\Gamma_3\le 9/5$.

A test of the certificate pipeline on the triangular bipyramid (three equatorial Bloch vectors plus the poles) returns exactly $1.545185185\ldots$, the value known for that configuration from the earlier experiments.

### 5.5 What a proof of $\Gamma_3=\gamma_B$ would need

The only upper bound is the ceiling $9/5$. Global optimality of B is numerical. A proof would need a certified global bound $\sup_F\min(g_4,g_8,g_9,g_{12},g_{16})\le\gamma_B$ over the four-dimensional family, i.e. a certified global optimisation of the minimum of five polynomials of degree $\le 16$ in the ten Gram entries (or in the seven angles), for instance by interval branch-and-bound on the $(n_1,n_2,n_3,\psi)$-box or by a Lasserre/SOS relaxation, together with an algebraic identification of the point B from its four tie equations. Neither was attempted. A direct interval-arithmetic evaluation of the certificate was tried and abandoned: the forward three-term recurrence amplifies interval widths exponentially (`s4iv`, kept for the record), which is why the certificate works in exact integers instead.

## 6. Verification

*Independent review.* A second agent, working from the report and the record and writing its own code, re-derived Lemma T from DLMF 18.10.3 with the constants recomputed, re-derived the bound, and confirmed numerically that the ratio in (3.1) never exceeds $1$ (`r2b`: own three-term recurrence cross-checked against `mpmath.jacobi` to $10^{-42}$; $d=3,\ldots,6$; $n\le 400$). It recomputed Table 1 with `sympy.jacobi` (`r1`) and the Lemma T thresholds ($0.017239$ at $k=10$, $0.014587$ at $k=11$ in $d=4$; $0.08036$ at $k=13$, $0.075$ at $k=14$ in $d=3$), re-derived the $N=5$ rigidity in $\mathbb C^4$ and the $N\ge 6$ exclusion, checked the exact feasibility of the certified frame in rational arithmetic, re-ran the integer certificate (identical output) and evaluated the exact frame and the $40$-digit point B independently at $60$ digits (`r3`), reproduced the KKT multipliers and the rank-$4$ structure from ambient central-difference gradients projected to the constraint manifold (`r5`, and a sampled minimum of $\max_k(-\partial_vg_k)=0.0108$ over $20000$ random unit tangent directions, a diagnostic rather than an all-directions proof), and ran its own $12$-start multistart with its own parametrisation and `scipy.special.eval_jacobi` (`r4`), reaching $\gamma_B$ to $12$ digits. Its corrections, all incorporated: the rational $1466335/7340032$ given for $\gamma^{\mathrm{simp}}-\gamma^{\mathrm{ONB}}$ in the report was wrong (the correct value is $7334427/36700160$; the decimal was right); the multistart census was missing; the Koornwinder addition-formula paper is dated $1973$, not $1972$; and the header of the multiplier line in `s6_out_B.txt` is mislabelled (Section 5.3). None affects a verdict.

*Labelling.* Theorem A is exact: rational arithmetic for $2\le k\le 10$, Lemma T for $k\ge 11$; the degree $k=10$ needs the exact check because the Lemma T bound is $0.01724$ there, above $0.01564$. The $d=3$ value $1.7760099429996636\ldots$ is numerical; the exact certified statement is $\Gamma_3\ge 1.776009937964733$.

*Literature.* Four searches were made ($2026$-$09$-$14$). (1) Koornwinder's Laplace-type integral: [Ko74], [As74], the group-theoretic addition formula [Ko73], and DLMF 18.10.3 (source Askey [As75], eq. (4.20)); The original search did not identify the consequence of [HS14], equation (20); the present revision corrects that omission with (3.3). Lemma T is a convenient weaker estimate with a self-contained proof, not a new inequality. (2) Bernstein-type bounds: [CGW94] (range $-\tfrac12\le\alpha,\beta\le\tfrac12$, not applicable), [HS14], [EMN94]. (3) Gleason-type and frame-function literature: Benedetto–Koprowski–Nolan [BKN20], Moretti–Pastorello [MP13], Caves–Fuchs–Manne–Renes [CFMR04], Saini–Kiukas–Burgarth–Gilchrist [SKBG26] (condition number of the frame operator on the Born sector only); none formulates the all-degree objective $\gamma$ or its optimisers in $d=3,4$. (4) Frames: the uniqueness of the $(d+1)$-vector equiangular tight frame [Tr05, FJMP18], the Welch bound [We74], SIC-POVMs [RBSC04] (which have $g_2=0$ by [Rec], Section 6, and are irrelevant to the maximisation). *Novelty note.* Theorem A is, to our knowledge, new, but its ingredients are standard and its difficulty is modest; its value lies in closing a case that [Rec] left open using established analytic tools. The $d=3$ results are a certified lower bound plus a numerical picture.

## 7. Open questions

1. *The value of $\Gamma_3$.* Prove $\Gamma_3=\gamma_B$ (Section 5.5), or find a better upper bound than $9/5$.
2. *Algebraic nature of B.* The numerical candidate B satisfies four tie equations of degree $\le16$ in the overlaps to the reported precision. Can an exact solution be isolated and its algebraic degree determined, and does it have a hidden symmetry that the Gram matrix does not display?
3. *Why five active degrees.* At every local maximum found, exactly $\dim+1=5$ degrees are active (the generic vertex structure). Is there a configuration where fewer degrees tie with a degenerate (non-vertex) maximum?
4. *Unequal weights.* [Rec], Section 7.3, leaves the weighted problem open in every dimension; in $d=3,4$ the present rigid or four-dimensional pictures may change.
5. *Dimension two.* [Rec] notes that in $d=2$ the ONB has an infinite odd-degree kernel and the trine has positive gap; $\Gamma_2$ is untouched here.

## 8. Reproducibility

The package `repro/` (relative to this manuscript) contains `author/` (the original research scripts and finished per-start logs of multistart seeds $31$–$34$, with the diagnostic-only revision edits recorded in `SOURCE-DIFF.patch`), `reviewer/` (the six independent scripts `r1_exact.py`, `r2_lemmaT.py`, `r2b_lemmaT.py`, `r3_exactframe.py`, `r4_opt.py`, `r5_kkt.py`, with two paths made package-relative and marked `REPRO`), `run_fast.sh`, `logs/` and `README.md`. Environment: Python 3.12, numpy 2.5.1, scipy 1.18, sympy 1.14, mpmath 1.3.

Author's scripts: `s1_exact_simplex_spectra.py` (exact $g_k$ of ONB and simplex, $d=3,4$, $k\le 400$; $1$ s), `s2_zonal_integral_identity.py` (identity (3.2) as exact polynomials in $t$, $n\le 40$, $d=3,\ldots,6$; $154$ s on rerun), `s3_d3_N5_global.py` (differential evolution, $20$–$25$ min per seed, not rerun; outputs kept), `s3b_d3_multistart.py` (multistart; not rerun; all logs kept), `s4int_d3_exact_certificate.py` (integer certificate; $14$ s), `s4iv_d3_interval_certificate.py` (failed interval attempt, kept), `s5_rationalise_and_certify.py` (rational frame from the $40$-digit point, then the certificate; $16$ s), `s6_tie_refine_mp.py` ($40$-digit refinement and multipliers; $4$–$5$ s), `s7_identify_and_rank.py` (rank and `findpoly`; $3$ s), `tally.py` (census). `run_fast.sh` reruns everything except `s3` and `s3b` into `logs/`, with times in `logs/timings.txt`; the rerun of `s6` from the raw seed-$0$ point followed by `s5` reproduced the exact frame specification byte for byte (`logs/timings.txt`, last line), so the certificate is reproducible from the float optimum without any stored intermediate. Reviewer's scripts rerun in $4$–$20$ s each; `r2_lemmaT.py` (direct `mpmath.jacobi` at high degree) fails with a hypergeometric convergence error at $k\approx 400$ and was superseded by `r2b_lemmaT.py` (recurrence), both kept; `r4_opt.py` takes about $10$ min and its output `r4_seed7.txt` is included.

### Revision verification and precision boundary

The revision includes fresh replay logs under `repro/revision_logs/`, separate from all preserved historical logs. The exact certificate uses integer and rational arithmetic; its rational output, rather than a floating-point diagnostic, is authoritative. `s6` uses 40-digit mpmath arithmetic and central differences at step $10^{-15}$; `r3` evaluates rational and decimal-string inputs at 60 digits. `r5` forms finite differences with mpmath but converts the final gradient and constraint calculations to NumPy binary64; its rank and multiplier results are numerical. Its random-direction sample cannot certify a minimum over all directions, and the ambient tangent space includes rotations.

As a cross-check during original-version preassessment, a newly written four-coordinate Bloch parametrisation, binomial Jacobi formula and 80-digit root calculation reproduced the printed B value and positive multipliers, with tie residual about $4.8\cdot10^{-80}$. This is numerical corroboration, not an interval or algebraic-isolation certificate. No new global search, proof of $\Gamma_3=\gamma_B$, intake assessment or editorial decision is implied. The revision replay records list precisely which supplied scripts were executed again.

## AI-assistance statement

The mathematics, computations and text of this manuscript were produced by Claude Fable 5.1 agents (Anthropic) working under the direction of the author, who set the problem, selected the line of records and is responsible for the claims. One agent carried out the research (Lemma T, Theorem A, the $d=3$ searches, the exact certificate) and wrote the report on which this manuscript is based; a second, independent agent performed an adversarial review with its own implementations of every computational ingredient and found the corrections incorporated here; a third agent wrote this text, completed the multistart census, assembled the reproducibility package and reran the fast scripts. No fallback to another model occurred in any of these sessions. The manuscript has not been peer reviewed by humans. After that author-supplied Fable workflow, a configured Astra High agent performed a fresh local preassessment of the original PDF, SHA-256 `ade85760907efcbeb0db82db9f194a5822e329680eae7abea33a6284c15bea80`, and then assisted with the present bounded revision. That original assessment does not assess this revised PDF. The revision corrects literature attribution, qualifies numerical local-optimality statements, clarifies the conjugation quotient and fixes diagnostic labels; it does not alter Theorems A or B. Historical Fable model identity and execution claims above are author-supplied, not independently certified by this revision.

## References

- [Rec] L. Eriksson, *Orthogonal Measurements Maximize All-Degree Born Rigidity among Equal-Trace Rank-One POVM Orbits in Dimension Five and Above*, AI Research Record, ARR-2026-0DZQ2WNKPW8GCTPA (2026). Cited: Definition 2.1 (seeds), Theorem 3.1 (spectral formula (2.1)), Definition 3.2 ($\gamma=\inf_{k\ge 2}g_k$; $g_1=0$), Theorem 3.3 (inverse constant $\gamma^{-1/2}$), Lemma 4.1 and Proposition 4.2 (ceiling), Lemma 5.1 (ONB at $N=d$, simplex rigidity at $N=d+1$), (10)–(11) (ONB spectrum), Theorem 5.2 ($\Gamma_d=d-6/(d+1)$ for $d\ge 5$), Section 7.1 (failure of the degree-three comparison in $d=3,4$), Section 7.3.
- [DLMF] NIST Digital Library of Mathematical Functions, §18.10(ii), eq. 18.10.3 (Laplace-type integral for Jacobi polynomials) and §18.14, eq. 18.14.3, https://dlmf.nist.gov/18.10, https://dlmf.nist.gov/18.14.
- [Ko73] T. H. Koornwinder, The addition formula for Jacobi polynomials and spherical harmonics, *SIAM J. Appl. Math.* 25 (1973) 236–246.
- [Ko74] T. H. Koornwinder, Jacobi polynomials II. An analytic proof of the product formula, *SIAM J. Math. Anal.* 5 (1974) 125–137.
- [As74] R. Askey, Jacobi polynomials I. New proofs of Koornwinder's Laplace type integral representation and Bateman's bilinear sum, *SIAM J. Math. Anal.* 5 (1974) 119–124.
- [As75] R. Askey, *Orthogonal Polynomials and Special Functions*, CBMS-NSF Regional Conference Series in Applied Mathematics 21, SIAM, 1975, eq. (4.20).
- [CGW94] Y. Chow, L. Gatteschi, R. Wong, A Bernstein-type inequality for the Jacobi polynomial, *Proc. Amer. Math. Soc.* 121 (1994) 703–709.
- [EMN94] T. Erdélyi, A. P. Magnus, P. Nevai, Generalized Jacobi weights, Christoffel functions, and Jacobi polynomials, *SIAM J. Math. Anal.* 25 (1994) 602–614.
- [HS14] U. Haagerup, H. Schlichtkrull, Inequalities for Jacobi polynomials, *Ramanujan J.* 33 (2014) 227–246; arXiv:1201.0495.
- [Tr05] J. A. Tropp, Complex equiangular tight frames, *Proc. SPIE* 5914, Wavelets XI (2005) 591401.
- [FJMP18] M. Fickus, J. Jasper, D. G. Mixon, J. Peterson, Equiangular tight frames that contain regular simplices, *Linear Algebra Appl.* 555 (2018) 98–138.
- [We74] L. R. Welch, Lower bounds on the maximum cross correlation of signals, *IEEE Trans. Inform. Theory* 20 (1974) 397–399.
- [RBSC04] J. M. Renes, R. Blume-Kohout, A. J. Scott, C. M. Caves, Symmetric informationally complete quantum measurements, *J. Math. Phys.* 45 (2004) 2171–2180.
- [CFMR04] C. M. Caves, C. A. Fuchs, K. Manne, J. M. Renes, Gleason-type derivations of the quantum probability rule for generalized measurements, *Found. Phys.* 34 (2004) 193–209; arXiv:quant-ph/0306179.
- [MP13] V. Moretti, D. Pastorello, Generalized complex spherical harmonics, frame functions, and Gleason theorem, *Ann. Henri Poincaré* 14 (2013) 1435–1443; arXiv:1205.4504.
- [BKN20] J. J. Benedetto, P. J. Koprowski, J. S. Nolan, A generalization of Gleason's frame function for quantum measurement (2020), arXiv:2001.06738.
- [SKBG26] R. Saini, J. Kiukas, D. Burgarth, A. Gilchrist, Completeness stability of quantum measurements, *Phys. Rev. A* 113 (2026) 012424; arXiv:2506.11539.
