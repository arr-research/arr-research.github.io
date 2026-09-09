# One Fold, Unique Contact and the Complete Two-Piece Rate–Distortion Function of Rank-One Complex-Projective Born Prediction

**Lluis Eriksson** (Independent researcher)

9 September 2026 (internal workshop revision v004; received version 2 and deposited v003 preserved)

## Abstract

For a Haar-random pure state on $\mathbb{CP}^{d-1}$ with squared-Frobenius distortion on density-matrix reproductions, the exact rate–distortion function $R_d(D)$ is known (ARR-2026-1D2QYXPCVY9H7ANB) as a one-dimensional envelope over a radius $b\in[0,1]$ and a multiplier $\lambda$; first contact was proved there, but uniqueness of the positive branch and absence of later branch exchange were left open (its Remark 3.2). We close that remark for every finite $d\ge3$, in a note written to be read without the earlier record (only its envelope theorem is imported, with the elementary facts it rests on reproved here). The tool is the first-order equation $\kappa M'=(\kappa-d+1)M+(d-1)$ for $M={}_1F_1(1;d;\kappa)$, which reduces the fold numerator $K_d'-\kappa K_d''$ to the sign of $\kappa-\Psi_d(M)$ with $\Psi_d$ an explicit rational function; a transversality argument in the $(M,\kappa)$ plane then shows the stationary multiplier $\lambda(\kappa)$ has exactly one fold. This yields a unique coexistence multiplier $\lambda_{c,d}$, no reentrance, and $R_d=$ a linear face glued at $D_{c,d}$ to an explicit complex-Bingham curve. A computer-assisted theorem gives the one-change law for the fold-numerator coefficients; $d=2$ recovers the Dytso–Cardone sphere result.

## 1. Introduction

Let $X$ be Haar-distributed on $\mathbb{CP}^{d-1}$, $\rho_X=|x\rangle\langle x|$, and let a reproduction be any density matrix $\hat\rho$ produced by an arbitrary stochastic map of $X$; the cost is $\|\rho_X-\hat\rho\|_F^2$ and $R_d(D)=\inf\{I(X;\hat\rho):\mathbb{E}\|\rho_X-\hat\rho\|_F^2\le D\}$. Through the Born rule this is the classical information needed to predict the outcome statistics of Haar (or 2-design) measurements to squared error $D/(d(d+1))$.

**Antecedents.** The record ARR-2026-1D2QYXPCVY9H7ANB (*Exact Rate–Distortion Theory for Complex-Projective Born Prediction: Finite-Dimensional Bingham Frontiers, Thermodynamic Coexistence, and Worst-State Capacity*; below "1D2Q") proved, for $0\le D\le R_{0,d}^2=1-1/d$, the exact envelope $R_d(D)=\sup_{\lambda\ge0}\{\lambda(R_{0,d}^2-D)-\max_{0\le b\le1}G_{d,\lambda}(b)\}$ with $G_{d,\lambda}(b)=K_d(2\lambda b)-\lambda R_{0,d}^2b^2$, $K_d=\log{}_1F_1(1;d;\cdot)-\kappa/d$ (its Theorem 2.1, whose spectral input is the centred power-sum extremum of Brazitikos–Pandis [BP, Prop. 5.5]); every positive active radius is attained by a covariant complex-Bingham channel. Its Theorem 3.1 proved a discontinuous onset: for $d\ge3$ there is $0<\lambda_{c,d}<\lambda_{0,d}=d(d+1)/2$ at which $b=0$ and *some* $b_{c,d}>0$ are both global maximizers. Its Remark 3.2 explicitly does **not** assert uniqueness of the positive maximizer for larger $\lambda$, nor exclude a later branch exchange; consequently the finite-$d$ frontier was known only as an envelope, not as an explicit two-piece curve, and the asymptotics $\lambda_{c,d}=\alpha_*d-c_*\log d+O(1)$ (1D2Q Thm. 7.3) described a first contact, not *the* contact. Two sibling records did reach the complete statement in other geometries: ARR-2026-61Y0FFA39M8KMBJ5 (*Complete Rank-Two Born-Prediction Rate–Distortion on $\mathrm{Gr}_{\mathbb C}(2,4)$*; "61Y0", Lemma 6.1, Thm. 6.2, Cor. 6.3) via an explicit integer coefficient sequence with one sign change, and ARR-2026-7H9FAPTBZA897AMJ (*Complete Rate–Distortion Phase Diagram of Haar Oriented Two-Planes: One-Change Hypergeometric Coefficients, Unique Coexistence, and No Reentrance*; "7H9F", Thm. 8.2, Thm. 9.1) for oriented two-planes in $\mathbb R^n$, $n\ge6$, via a parity-truncated binomial window and a likelihood-ratio ordering. The 7H9F normalizer $L_q(\kappa)=\mathbb E\cosh(\kappa T)$, $T\sim\mathrm{Beta}(1,q)$, is the even part of the $\mathbb{CP}^{q}$ normalizer $M_{q+1}(\kappa)=\mathbb E e^{\kappa T}$, but its window argument does not transfer to the full (non-parity-truncated) window that appears here. Externally: for $d=2$ the problem is the real two-sphere and $R_2$ is the Dytso–Cardone curve [DC]; generalized Curie–Weiss models can have several first-order transitions (Eisele–Ellis [EE]), so uniqueness is not a generic fact; and the Kummer-ratio literature (Karp–Sitnik [KS], Kalmykov–Karp [KK], Sitnik [S]) studies monotonicity and Turán-type inequalities for ratios such as $M_{d+1}/M_d$, which is exactly $1-b_d(\kappa)$ below, but contains no statement about the fold of $\kappa/b_d(\kappa)$.

**Contribution.** (i) A first-order linear ODE for $M_d={}_1F_1(1;d;\kappa)$ (Lemma 3.1) that collapses the three-term fold numerator to a rational expression in $(M,\kappa)$ (Lemma 3.2). (ii) A phase-plane transversality theorem (Theorem 4.1): for every $d\ge3$ the stationary multiplier has exactly one fold, with the proved bounds $2(d-2)(d+1)/d\le\kappa_{f,d}<2d$ and $M_d(\kappa_{f,d})\ge d(d-1)/2$; no coefficient sign pattern is needed. (iii) The complete radial phase and the two-piece rate–distortion function at every finite $d\ge3$ (Theorem 5.1), closing 1D2Q Remark 3.2; the single statement imported from 1D2Q (Theorem A) is stated explicitly, and the elementary facts about $\mathrm{Beta}(1,d-1)$ that 1D2Q used are reproved in Lemma 2.1. (iv) The one-change coefficient law in the style of 61Y0/7H9F (Theorem 6.1): proved analytically for every $d$ and every index except two boundary indices for $3\le d\le35$, which are settled by an exact integer check; for $d\ge36$ an explicit tail bound closes them. (v) The $d=2$ corollary (no fold, continuous onset, Dytso–Cardone). Sections 7–9 give numerical tables, open questions, and reproducibility data.

**What this note is, and what a reader gains without 1D2Q.** This is a standalone note, not a continuation: Section 2 restates every object it uses ($M_d$, $K_d$, $G_{d,\lambda}$, the stationary parametrization (2.3)), proves in Lemma 2.1 the three elementary facts about $T\sim\mathrm{Beta}(1,d-1)$ that the earlier record used, and imports exactly one statement from 1D2Q, Theorem A (the envelope formula and the attainability of active radii), with the equation numbers of its proof. Lemma 3.1 itself is not new as a formula: it is a contiguous relation of Kummer's function specialized to first parameter $1$, where ${}_1F_1(0;d;\kappa)=1$ closes the recurrence into an inhomogeneous first-order equation (cf. [DLMF, §13.3]); we include its two-line series proof. What is new is what it buys. (1) The stationary radius becomes the elementary ratio $b_d=1-M_{d+1}/M_d$ and the three-term fold numerator $K_d'-\kappa K_d''$ becomes a rational function of $(M_d,\kappa)$ (Lemma 3.2), so the fold question is a sign problem for $\kappa-\Psi_d(M_d(\kappa))$ about a classical special function, with no rate–distortion context needed. (2) That sign problem is settled globally by a transversality argument in the $(M,\kappa)$ plane (Theorem 4.1): the curve $\kappa=\Psi_d(M)$ can be crossed by the graph of $\kappa(M)$ only in one direction on $(1,M_1)$ and only in the other on $(M_1,\infty)$, which forces exactly one crossing and gives explicit bounds on where it lies. This answers completely the one-parameter Curie–Weiss-type problem "maximize $K_d(2\lambda b)-\lambda(1-1/d)b^2$ over $b\in[0,1]$" for every $\lambda$ (Theorem 5.1(a)–(c)), a problem in which several first-order transitions are not excluded a priori [EE]. (3) The explicit two-piece rate–distortion function (Theorem 5.1(f)) is then the corollary of (2) and Theorem A. A reader who knows 1D2Q additionally obtains the closure of its Remark 3.2 and the identification of its first-contact asymptotics (Theorem 7.3 there) as *the* contact.

## 2. Setting and notation

Throughout $d\ge2$ is an integer, $\kappa>0$, and $T\sim\mathrm{Beta}(1,d-1)$ (density $(d-1)(1-t)^{d-2}$ on $[0,1]$). From 1D2Q eqs. (2)–(6):

$$M_d(\kappa)={}_1F_1(1;d;\kappa)=\sum_{j\ge0}\frac{\kappa^j}{(d)_j}=\mathbb E\,e^{\kappa T},\qquad K_d(\kappa)=\log M_d(\kappa)-\frac{\kappa}{d},\qquad R_{0,d}^2=1-\frac1d, \tag{2.1}$$

$$G_{d,\lambda}(b)=K_d(2\lambda b)-\lambda R_{0,d}^2b^2\ (0\le b\le1),\qquad c_d(\lambda)=-\lambda R_{0,d}^2+\max_{0\le b\le1}G_{d,\lambda}(b). \tag{2.2}$$

$K_d$ is the cumulant generating function of $T-1/d$, so $K_d'(\kappa)=\mathbb E_\kappa T-1/d$ and $K_d''(\kappa)=\mathrm{Var}_\kappa T>0$ under the tilted law $\propto e^{\kappa t}$. Write $m_d=M_d'/M_d=K_d'+1/d$. The stationary equation $G_{d,\lambda}'(b)=0$ for $b>0$ reads, with $\kappa=2\lambda b$, $K_d'(\kappa)=R_{0,d}^2b$; hence the positive stationary radii are parametrized by $\kappa$:

$$b_d(\kappa)=\frac{K_d'(\kappa)}{R_{0,d}^2}=\frac{d\,m_d(\kappa)-1}{d-1},\qquad \lambda_d(\kappa)=\frac{\kappa}{2b_d(\kappa)}, \tag{2.3}$$

(1D2Q eq. (110)). Define the fold numerator, the coexistence function and the polynomial-series numerator

$$\begin{aligned}H_d&=K_d'-\kappa K_d'',\qquad F_d=2K_d-\kappa K_d',\\ N_d&:=M_d^2H_d=M_dM_d'-\kappa M_dM_d''+\kappa M_d'^2-\frac{M_d^2}{d}\\&=\sum_{n\ge0}c_{d,n}\kappa^n.\end{aligned}\tag{2.4}$$

Then $F_d'=H_d$, $\lambda_d'=H_d/(2R_{0,d}^2b_d^2)$, and at a stationary radius $G_{d,\lambda}(b_d(\kappa))=F_d(\kappa)/2$ and $\partial_b^2G_{d,\lambda}=-(2\lambda/b)H_d(\kappa)$ (direct differentiation; the three identities are rechecked symbolically in `sym_check.py`). We drop the index $d$ when harmless.

**Theorem A (imported; 1D2Q Theorem 2.1 and its proof, eqs. (106)–(112)).** Let $d\ge2$. (A1) For $0\le D\le R_{0,d}^2$,
$R_d(D)=\sup_{\lambda\ge0}\{\lambda(R_{0,d}^2-D)-\max_{0\le b\le1}G_{d,\lambda}(b)\}$.
(A2) If $\lambda>0$ and $b\in(0,1]$ is a global maximizer of $G_{d,\lambda}$ ("active"), then with $\kappa=2\lambda b$ the covariant channel $dP_{X|U=u}/d\mu_d=e^{\kappa|\langle x,u\rangle|^2}/M_d(\kappa)$, $U$ Haar, has posterior mean $(1-b)I/d+b\rho_u$ and attains the pair $D_b=R_{0,d}^2(1-b^2)$, $I_b=\kappa m_d(\kappa)-\log M_d(\kappa)=\lambda(R_{0,d}^2-D_b)-\max_vG_{d,\lambda}(v)$.
(A3) Mixing channels with probabilities $t_i$ independent of $X$ achieves distortion $\sum_i t_iD_i$ and information at most $\sum_i t_iI_i$. Retaining the independent flag as an auxiliary output gives equality for the information of that enlarged output; discarding the flag cannot increase information. Equality for the rate-distortion frontier used below follows from the matching converse bound.
For $d\ge3$ the spectral input rests on Brazitikos–Pandis [BP, Proposition 5.5] through 1D2Q Proposition A.1; it bounds centered power sums at fixed Euclidean norm. The interface and the information-theoretic steps needed here are detailed below; the cited extremal inequality itself remains an external theorem. The three elementary facts that 1D2Q also used (its eqs. (10), (11), (15)) are reproved here:

*Dependency and proof interface for Theorem A.* For a centered real spectrum $a$ with $\sum a_i^2=1$, maximizers of a power sum $p_j(a)=\sum a_i^j$ have at most three distinct coordinates: their Lagrange equation $j x^{j-1}=\alpha+\beta x$ has at most two real roots for odd $j\ge3$ by convexity, and at most three for even $j\ge4$ by its derivative. The cases $j=1,2$ are fixed by the constraints. The grouped-coordinate inequality [BP, Proposition 5.5] therefore gives $|p_j(a)|\le p_j(w)$ for odd $j$ and $p_j(a)\le p_j(w)$ for even $j$, where $w$ is the centered unit-norm spectrum with one positive spike. Newton's expansion
$$h_n(a)=\sum_{m_1+2m_2+\cdots=n}\prod_{j=1}^n\frac{p_j(a)^{m_j}}{m_j!\,j^{m_j}}$$
implies $h_n(a)\le h_n(w)$: bound each summand by its absolute value, then use the nonnegative power sums of $w$. Haar squared coordinates have the $\mathrm{Dirichlet}(1,\ldots,1)$ law, so for a Hermitian $A$ with spectrum $a$,
$$\mathbb E_\mu e^{t x^*Ax}=\sum_{n\ge0}\frac{h_n(a)t^n}{(d)_n}.$$
The series is absolutely convergent; scaling the fixed norm extends the comparison to every traceless $A$ and $t\ge0$. Thus at fixed $\|A\|_F=bR_{0,d}$ the Laplace transform is bounded by that of $A=b(\rho_u-I/d)$.

For any density-matrix reproduction $y$, set $A=y-I/d$ and $S_x=\rho_x-I/d$. Then $0\le b=\|A\|_F/R_{0,d}\le1$, and the preceding bound gives
$$Z_\lambda(y):=\int e^{-\lambda\|S_x-A\|_F^2}\,d\mu(x)\le \exp\{-\lambda R_{0,d}^2+G_{d,\lambda}(b)\}\le e^{c_d(\lambda)}.$$
Nonnegativity of relative entropy of $P_{X|y}$ against $e^{-\lambda\|S_x-A\|^2}\mu/Z_\lambda(y)$ yields $I(X;y)+\lambda\mathbb E\|\rho_X-y\|_F^2\ge-c_d(\lambda)$. This proves the lower bound in (A1). The finite-information case suffices; infinite information is automatic.

Every positive active radius at finite $\lambda$ is interior by $G'_{d,\lambda}(1)<0$ (H2), and hence $K_d'(\kappa)=R_{0,d}^2b$. The displayed Bingham posterior has mean $(1-b)I/d+b\rho_u$ by unitary symmetry and $\mathbb E_\kappa |\langle X,u\rangle|^2=m_d(\kappa)$. The posterior-mean identity gives $D_b=R_{0,d}^2(1-b^2)$, and direct integration of its log density gives $I_b=\kappa m_d-\log M_d$. The map $u\mapsto(1-b)I/d+b\rho_u$ is injective on projective space for $b>0$, so the same information is obtained with density-matrix output. This proves (A2); independence of the mixture flag and data processing give (A3). The radial analysis of Sections 4 and 5(a)-(e) uses no envelope equality. Its active channels, together with (A3), attain the lower bound for all distortions in Theorem 5.1(f) and Corollary 5.2, completing (A1) without circularity. This verifies the use of the earlier envelope theorem here while retaining [BP] as the stated external mathematical input.

*Clarification of the external power-sum input.* We use the non-strict bound of [BP, Proposition 5.5]. Its arXiv v1 proof, p.31, contains the erroneous estimate $75/64<1$ for $n=5$. The local argument is repaired by retaining the exponent $k\ge3$: with its notation $w^2=1/2$, $s^2=4/5$ and $q=t/w=1/\sqrt{10}<1/3$, the finite geometric sum satisfies
$$\frac{S(w)}{s^{2k}}<\frac{2}{1-q}\left(\frac58\right)^k<3\left(\frac58\right)^3=\frac{375}{512}<1.$$
This restores that estimate for $n=5,k\ge3$ and leaves the separately treated quartic cases unchanged. For $n=3,k=2$, the normalized fourth moment is identically $1/2$; the non-strict inequality required here is unaffected. We import no uniqueness assertion for that exceptional case. This local repair does not replace the remainder of the cited proof.

**Lemma 2.1 (elementary facts on $\mathrm{Beta}(1,d-1)$).** Let $d\ge2$.
(i) $M_d(\kappa)=(d-1)\int_0^1e^{\kappa t}(1-t)^{d-2}\,dt$ equals the series in (2.1), and $M_d$ is entire.
(ii) $\mathbb ET=1/d$, $v_d:=\mathrm{Var}\,T=\dfrac{d-1}{d^2(d+1)}$, $\mu_{3,d}:=\mathbb E(T-1/d)^3=\dfrac{2(d-1)(d-2)}{d^3(d+1)(d+2)}$; hence $K_d(\kappa)=\frac{v_d}{2}\kappa^2+\frac{\mu_{3,d}}{6}\kappa^3+O(\kappa^4)$ and, with $\kappa=2\lambda b$,
$$G_{d,\lambda}(b)=\lambda\big(2\lambda v_d-R_{0,d}^2\big)b^2+\tfrac43\lambda^3\mu_{3,d}\,b^3+O(b^4). \tag{2.5}$$
(iii) $\log M_d(\kappa)=\kappa-(d-1)\log\kappa+\log\Gamma(d)+\log P_d(\kappa)$ with $P_d(\kappa)=1-e^{-\kappa}\sum_{j=0}^{d-2}\kappa^j/j!\in(0,1)$ and $P_d(\kappa)\to1$; in particular $\log M_d(\kappa)=\kappa-(d-1)\log\kappa+\log\Gamma(d)+o(1)$ as $\kappa\to\infty$.

*Proof.* (i) Termwise, $(d-1)\int_0^1t^j(1-t)^{d-2}dt=(d-1)B(j+1,d-1)=j!\,(d-1)!/(d-1+j)!=j!/(d)_j$. (ii) The same integral gives $\mathbb ET^k=k!/(d)_k$, so $\mathbb ET=1/d$, $\mathbb ET^2=2/(d(d+1))$, $\mathbb ET^3=6/(d(d+1)(d+2))$; expanding $\mathbb E(T-1/d)^2$ and $\mathbb E(T-1/d)^3$ gives $v_d$ and $\mu_{3,d}$, and the second and third cumulants of $T-1/d$ are its second and third central moments; (2.5) follows from $G_{d,\lambda}(b)=K_d(2\lambda b)-\lambda R_{0,d}^2b^2$. (iii) Substituting $t=1-s$ and $u=\kappa s$, $M_d(\kappa)=(d-1)e^\kappa\kappa^{1-d}\int_0^\kappa e^{-u}u^{d-2}du=\Gamma(d)e^\kappa\kappa^{1-d}P_d(\kappa)$, where $\int_0^\kappa e^{-u}u^{d-2}du=(d-2)!\,P_d(\kappa)$ by repeated integration by parts. $\square$

(These are 1D2Q eqs. (10), (11) and (15); the symbolic expansion (2.5) is rechecked in `h6_remark63_check.py`.)

## 3. Exact reductions

**Lemma 3.1 (first-order equation).** $\kappa M_d'=(\kappa-d+1)M_d+(d-1)$. Consequently
$$b_d(\kappa)=1-\frac{d\,(M_d-1)}{\kappa M_d}=1-\frac{M_{d+1}(\kappa)}{M_d(\kappa)},\qquad \kappa K_d'(\kappa)=\kappa R_{0,d}^2-(d-1)+\frac{d-1}{M_d(\kappa)}. \tag{3.1}$$

*Proof.* With $a_j=1/(d)_j$ one has $a_{j-1}=(d-1+j)a_j$, so the $\kappa^j$ coefficient of the right side is $a_{j-1}-(d-1)a_j=j\,a_j$ for $j\ge1$ and $-(d-1)+(d-1)=0$ for $j=0$, matching $\kappa M'$. Dividing by $\kappa M$ gives $m_d=1-(d-1)(M-1)/(\kappa M)$, and (2.3) gives the first form of $b_d$; the second follows from $d(M_d-1)/\kappa=\sum_{i\ge0}d\kappa^i/(d)_{i+1}=M_{d+1}$. Finally $\kappa K'=\kappa m_d-\kappa/d$. $\square$

Differentiating Lemma 3.1 gives Kummer's equation $\kappa M''+(d-\kappa)M'-M=0$, so no independent input is used below.

**Lemma 3.2 (rational reduction).** Put
$$\begin{aligned}\tilde N_d(\kappa)&:=(\kappa-2d)M_d^2+d(\kappa-d+3)M_d+d(d-1)\\&=M_d(M_d+d)\big(\kappa-\Psi_d(M_d)\big),\\ \Psi_d(M)&:=\frac{d(M-1)(2M+d-1)}{M(M+d)}.\end{aligned}\tag{3.2}$$
Then $N_d=\dfrac{d-1}{d\,\kappa}\tilde N_d$; hence $\operatorname{sign}H_d(\kappa)=\operatorname{sign}\big(\kappa-\Psi_d(M_d(\kappa))\big)$.

*Proof.* Let $P=\kappa M'=AM+(d-1)$ with $A=\kappa-d+1$; Kummer's equation gives $\kappa^2M''=\kappa M-(d-\kappa)P$. Then
$\kappa N_d=MP-M(\kappa M-(d-\kappa)P)+P^2-\kappa M^2/d=(2-A)MP+P^2-\kappa(1+1/d)M^2$. Expanding $P$: $(2-A)M(AM+d-1)+(AM+d-1)^2=2AM^2+(d-1)(A+2)M+(d-1)^2$, and $2A-\kappa(d+1)/d=\frac{d-1}{d}(\kappa-2d)$, $(d-1)(A+2)=\frac{d-1}{d}\,d(\kappa-d+3)$, $(d-1)^2=\frac{d-1}{d}\,d(d-1)$. The factorization in (3.2) is an identity of rational functions (checked in `sym_check.py`), and $M_d>1$ on $\kappa>0$. $\square$

*Remark 3.3.* Substituting $\kappa=$ from (3.1) one also finds $\tilde N_d=\kappa M_d\,[(2b_d-1)M_d+(d-1)b_d+1]$, so $H_d>0$ wherever $b_d\ge1/2$; every zero of $H_d$ has $b_d<1/2$.

**Proposition 3.4 (closed coefficients).** For $n\ge0$ let $T=2d-2+n$, $u_n=\binom{T-1}{d-2}$, $W_{n-1}=\sum_{k=d-1}^{d-2+n}\binom{T-1}{k}$ (so $W_{-1}=0$). Then
$$[\kappa^n]\tilde N_d=\frac{(d-1)!^2}{T!}\,\hat c_{d,n},\qquad \hat c_{d,n}=(n-2d-2)\,W_{n-1}+\frac{d}{d-1}\,n(n+2d)\,u_n, \tag{3.3}$$
and $c_{d,n}=\frac{d-1}{d}\frac{(d-1)!^2}{(2d-1+n)!}\hat c_{d,n+1}$. Moreover $\hat c_{d,0}=\hat c_{d,1}=\hat c_{d,2}=0$ and $\hat c_{d,3}=-\frac{(2d+1)(d-2)}{(d+1)(d+2)}\binom{2d}{d}$, i.e. $[\kappa^3]\tilde N_d=-\frac{d-2}{d^2(d+1)(d+2)}$.

*Proof.* With $a_j=(d-1)!/(d-1+j)!$, $[M^2]_n=\sum_{i+j=n}a_ia_j=\frac{(d-1)!^2}{T!}\sum_{k=d-1}^{d-1+n}\binom{T}{k}=\frac{(d-1)!^2}{T!}W_n$. For $n\ge1$, $[\kappa^n]\tilde N_d=[M^2]_{n-1}-2d[M^2]_n+d\,a_{n-1}+d(3-d)a_n$; multiplying by $T!/(d-1)!^2$ gives $TW_{n-1}-2dW_n+dT\binom{T-1}{d-1}+d(3-d)\binom{T}{d-1}$. Pascal's rule and the symmetry $\binom{T-1}{d-1+n}=\binom{T-1}{d-2}$ give $W_n=2W_{n-1}+2u_n$, while $\binom{T-1}{d-1}=u_n\frac{d-1+n}{d-1}$ and $\binom{T}{d-1}=u_n\frac{T}{d-1}$. Collecting, the $W_{n-1}$ coefficient is $T-4d=n-2d-2$ and the $u_n$ coefficient is $\frac{d}{d-1}[T(n+2)-4(d-1)]=\frac{d}{d-1}n(n+2d)$. The case $n=0$ is $-2d+d(3-d)+d(d-1)=0$. The special values follow from $W_0=\binom{2d-2}{d-1}$, $W_1=2\binom{2d-1}{d-1}$, $W_2=\binom{2d}{d}\frac{3d+1}{d+1}$ and $u_3=\binom{2d}{d}\frac{d(d-1)}{(d+1)(d+2)}$. $\square$

Formula (3.3) is verified against the three-term definition in exact rational arithmetic for $2\le d\le40$, $0\le n\le400$ (`verify_signs.py`) and for $2\le d\le12$, $n\le60$ (`check_formula.py`).

## 4. One fold for every $d\ge3$

**Theorem 4.1.** Let $d\ge3$. $H_d$ has exactly one positive zero $\kappa_{f,d}$; $H_d<0$ on $(0,\kappa_{f,d})$ and $H_d>0$ on $(\kappa_{f,d},\infty)$. Moreover
$$M_d(\kappa_{f,d})\ \ge\ M_1:=\frac{d(d-1)}2,\qquad \frac{2(d-2)(d+1)}{d}=\Psi_d(M_1)\ \le\ \kappa_{f,d}\ <\ 2d. \tag{4.1}$$
Hence $\lambda_d$ decreases strictly on $(0,\kappa_{f,d}]$ from $\lambda_{0,d}=d(d+1)/2$ (its limit at $0^+$) to $\lambda_{\min,d}:=\lambda_d(\kappa_{f,d})$ and increases strictly on $[\kappa_{f,d},\infty)$ to $+\infty$.

*Proof.* $\kappa\mapsto M_d(\kappa)$ is analytic and strictly increasing ($M'=\mathbb E[Te^{\kappa T}]>0$), a bijection $(0,\infty)\to(1,\infty)$; let $\kappa(M)$ be its $C^\infty$ inverse and $D(M):=\kappa(M)-\Psi_d(M)$. By Lemma 3.2, $\operatorname{sign}H_d(\kappa)=\operatorname{sign}D(M_d(\kappa))$, so it suffices to show that $D$ has exactly one zero $M_f$ on $(1,\infty)$, with $D<0$ before and $D>0$ after. By Lemma 3.1, $d\kappa/dM=1/M'(\kappa)=\Phi(M,\kappa):=\kappa/(\kappa M-(d-1)(M-1))$, so
$$D'(M)=\Phi(M,\kappa(M))-\Psi_d'(M).$$
At a zero $M_0$ of $D$,
$$D'(M_0)=\Delta(M_0):=\Phi(M_0,\Psi_d(M_0))-\Psi_d'(M_0).$$
The following are rational identities in $(M,d)$, obtained by direct computation (`sym_check.py`):

(a) On the curve $\kappa=\Psi_d(M)$: $\kappa M-(d-1)(M-1)=\frac{(d+1)M(M-1)}{M+d}>0$ for $M>1$, and $\Phi(M,\Psi_d(M))=\frac{d(2M+d-1)}{(d+1)M^2}$.

(b) $\Psi_d'(M)=\frac{d[(d+3)M^2+2(d-1)M+d(d-1)]}{M^2(M+d)^2}>0$ for $M\ge1$.

(c) $\Delta(M)=\dfrac{d\,(M-1)^2\,(2M-d(d-1))}{(d+1)M^2(M+d)^2}$: negative on $(1,M_1)$, zero at $M_1=d(d-1)/2$, positive on $(M_1,\infty)$.

(d) $\partial_\kappa\Phi(M,\kappa)=-\frac{(d-1)(M-1)}{(\kappa M-(d-1)(M-1))^2}<0$ for $M>1$ wherever the denominator is nonzero.

(e) $D<0$ on $(1,1+\varepsilon)$ for some $\varepsilon>0$: by Proposition 3.4, $\tilde N_d(\kappa)=-\frac{d-2}{d^2(d+1)(d+2)}\kappa^3+O(\kappa^4)<0$ for small $\kappa>0$ when $d\ge3$, i.e. $\kappa<\Psi_d(M_d(\kappa))$.

(f) $2d-\Psi_d(M)=\frac{d[(d+3)M+d-1]}{M(M+d)}>0$, so $\Psi_d<2d$ and $D(M)\to+\infty$ as $M\to\infty$.

*Step 1: $D<0$ on $(1,M_1)$ and $D(M_1)\le0$.* Suppose $D(M)\ge0$ for some $M\in(1,M_1)$ and let $M_*=\inf\{M\in(1,M_1):D(M)\ge0\}$. By (e), $M_*\ge1+\varepsilon$; by continuity $D(M_*)=0$ and $D<0$ on $(1,M_*)$, so $D'(M_*)\ge0$. But $D'(M_*)=\Delta(M_*)<0$ by (c). Contradiction; continuity gives $D(M_1)\le0$.

*Step 2: on $[M_1,\infty)$, $D(M)<0$ implies $D'(M)>0$.* If $D(M)<0$ then $\kappa(M)<\Psi_d(M)$. The denominator of $\Phi(M,\cdot)$ is affine in $\kappa$, equals $\kappa M'(\kappa)>0$ at $\kappa=\kappa(M)$ and is positive at $\kappa=\Psi_d(M)$ by (a); hence it is positive on the whole segment $[\kappa(M),\Psi_d(M)]$, where (d) applies, so $\Phi(M,\kappa(M))>\Phi(M,\Psi_d(M))$ and $D'(M)>\Delta(M)\ge0$ by (c).

*Step 3: exactly one zero.* Let $M_f=\inf\{M\ge M_1:D(M)\ge0\}$, which exists by (f); then $D(M_f)=0$ and, by Step 1 and the definition, $D<0$ on $(1,M_f)$. We claim $D>0$ on $(M_f,\infty)$. If $D(M_2)<0$ for some $M_2>M_f$, let $M_3=\sup\{M\in[M_f,M_2]:D(M)\ge0\}$; then $D(M_3)=0$ and $D<0$ on $(M_3,M_2]$, so by Step 2 $D$ is strictly increasing there and $D(M_2)>D(M_3)=0$, a contradiction. Thus $D\ge0$ on $[M_f,\infty)$. If $D(M_0)=0$ for some $M_0>M_f\ge M_1$, then $M_0$ is a local minimum of $D$, so $D'(M_0)=0$, whereas $D'(M_0)=\Delta(M_0)>0$ by (c). Hence $D>0$ on $(M_f,\infty)$. (When $D(M_1)=0$ this gives $M_f=M_1$; the argument does not need to distinguish the cases.)

Therefore $\kappa_{f,d}:=\kappa(M_f)$ is the unique positive zero of $H_d$, with the stated signs. Since $M_f\ge M_1$ and $\kappa_{f,d}=\Psi_d(M_f)$ with $\Psi_d$ increasing (b) and bounded by $2d$ (f), (4.1) follows; $\Psi_d(M_1)=2(d-2)(d+1)/d$ is a direct evaluation. The monotonicity of $\lambda_d$ follows from $\lambda_d'=H_d/(2R_{0,d}^2b_d^2)$, $\lambda_d(0^+)=R_{0,d}^2/(2K_d''(0))=R_{0,d}^2/(2v_d)=d(d+1)/2$, and $\lambda_d(\kappa)\ge\kappa/2\to\infty$. $\square$

**Corollary 4.2 ($d=2$).** $H_2>0$ on $(0,\infty)$; $\lambda_2$ increases strictly from $\lambda_{0,2}=3$ to $+\infty$.

*Proof.* Now $M_1=1$, so $\Delta>0$ on $(1,\infty)$ by (c). Proposition 3.4 gives $\hat c_{2,m}=(m-6)(2^{m+1}-2)+2m(m+4)$, so $\hat c_{2,3}=0$, $\hat c_{2,4}=4$, and $\tilde N_2(\kappa)=\kappa^4/180+O(\kappa^5)>0$: $D>0$ near $1^+$. If $D$ had a zero, the first one, $M_*$, would satisfy $D'(M_*)\le0$ (approached from $D>0$) and $D'(M_*)=\Delta(M_*)>0$. $\square$

## 5. The chain to the rate–distortion function

Standing facts, valid for $d\ge2$ and all $\kappa>0$, $\lambda>0$:

(H1) $b_d'=K_d''/R_{0,d}^2>0$; $b_d(0^+)=0$; $b_d(\kappa)\to1$ as $\kappa\to\infty$ (by (3.1), since $d(M-1)/(\kappa M)\to0$).

(H2) $K_d'(\kappa)=\mathbb E_\kappa T-1/d<R_{0,d}^2$ because $T<1$ a.s.; hence $G_{d,\lambda}'(1)=2\lambda(K_d'(2\lambda)-R_{0,d}^2)<0$, so $b=1$ is never stationary and never a maximizer.

(H3) For $b\in(0,1]$: $G_{d,\lambda}'(b)=0\iff b=b_d(\kappa)$ and $\lambda=\lambda_d(\kappa)$ with $\kappa=2\lambda b$; the map $\kappa\mapsto b_d(\kappa)$ is injective by (H1).

(H4) At such a stationary radius $G_{d,\lambda}(b)=F_d(\kappa)/2$ and $G_{d,\lambda}''(b)=-(2\lambda/b)H_d(\kappa)$.

(H5) $F_d'=H_d$, $F_d(0)=0$, and by (3.1) and Lemma 2.1(iii), $F_d(\kappa)=R_{0,d}^2\kappa-2(d-1)\log\kappa+O(1)\to+\infty$.

(H6) $G_{d,\lambda}(0)=0$, $G'_{d,\lambda}(0)=0$, $G''_{d,\lambda}(0)=2\lambda(2\lambda v_d-R_{0,d}^2)$ and $G'''_{d,\lambda}(0)=8\lambda^3\mu_{3,d}$, by (2.5). Since $R_{0,d}^2/(2v_d)=d(d+1)/2=\lambda_{0,d}$: for $\lambda<\lambda_{0,d}$ the radius $0$ is a strict local maximum of $G_{d,\lambda}$, and for $\lambda>\lambda_{0,d}$ a strict local minimum. At $\lambda=\lambda_{0,d}$ the quadratic term vanishes and the dimensions differ: for $d\ge3$, $\mu_{3,d}>0$, so $G_{d,\lambda_{0,d}}(b)=\frac43\lambda_{0,d}^3\mu_{3,d}b^3+O(b^4)>0$ for all small $b>0$ and $0$ is *not* a local maximum; for $d=2$, $\mu_{3,2}=0$ and $K_2(\kappa)=\log\big(\sinh(\kappa/2)/(\kappa/2)\big)$ gives $G_{2,3}(b)=-\frac{9}{20}b^4+\frac{9}{35}b^6+O(b^8)$, so $0$ remains a strict local maximum at $\lambda=\lambda_{0,2}=3$ (in agreement with Corollary 5.2, where $0$ is the unique global maximizer for every $\lambda\le3$). Only the cases $\lambda<\lambda_{0,d}$, $\lambda>\lambda_{0,d}$ and ($d\ge3$, $\lambda=\lambda_{0,d}$) are used below.

**Theorem 5.1 (complete radial phase and two-piece RDF, $d\ge3$).** Let $\kappa_f=\kappa_{f,d}$, $\lambda_{\min}=\lambda_d(\kappa_f)$ be as in Theorem 4.1.

(a) *Stationary radii.* For $\lambda>0$ the positive stationary radii of $G_{d,\lambda}$ are the $b_d(\kappa)$ with $\lambda_d(\kappa)=\lambda$: none for $\lambda<\lambda_{\min}$; exactly one, $b_d(\kappa_f)$, for $\lambda=\lambda_{\min}$; two, $b_d(\kappa_-)<b_d(\kappa_+)$ with $\kappa_-<\kappa_f<\kappa_+$, for $\lambda_{\min}<\lambda<\lambda_{0,d}$; exactly one, $b_d(\kappa_+)$ with $\kappa_+>\kappa_f$, for $\lambda\ge\lambda_{0,d}$. A pre-fold radius ($\kappa<\kappa_f$) is a strict local minimum, a post-fold radius ($\kappa>\kappa_f$) a strict local maximum, and the degenerate radius at $\lambda=\lambda_{\min}$ (where $H_d(\kappa_f)=0$) has gain $G=F_d(\kappa_f)/2<0=G_{d,\lambda}(0)$.

(b) *Unique contact.* $F_d$ decreases strictly on $(0,\kappa_f]$, is negative there, then increases strictly to $+\infty$; it has a unique positive zero $\kappa_c=\kappa_{c,d}>\kappa_f$. Put $b_c=b_d(\kappa_c)$, $\lambda_c=\lambda_d(\kappa_c)$, $D_c=R_{0,d}^2(1-b_c^2)$, $R_c=\kappa_cK_d'(\kappa_c)-K_d(\kappa_c)$.

(c) *Global maximizers.* The set of global maximizers of $G_{d,\lambda}$ on $[0,1]$ is $\{0\}$ for $0<\lambda<\lambda_c$; $\{0,b_c\}$ for $\lambda=\lambda_c$; $\{b_d(\kappa_+(\lambda))\}$ for $\lambda>\lambda_c$, where $\kappa_+(\lambda)>\kappa_c$ is the unique post-fold solution of $\lambda_d(\kappa)=\lambda$. (At $\lambda=0$, $G_{d,0}\equiv0$ and every $b\in[0,1]$ is a maximizer.)

(d) $0<\lambda_{\min}<\lambda_c<\lambda_{0,d}$.

(e) *No reentrance.* On $(\lambda_c,\infty)$, $\lambda\mapsto b_d(\kappa_+(\lambda))$ is continuous and strictly increasing to $1$, so the active distortion $D(\lambda)=R_{0,d}^2(1-b_d(\kappa_+(\lambda))^2)$ decreases strictly from $D_c$ to $0$. The function $c_d$ of (2.2) is convex with $-\partial c_d(\lambda)=\{R_{0,d}^2\}$ for $0<\lambda<\lambda_c$, $[D_c,R_{0,d}^2]$ at $\lambda_c$, $\{D(\lambda)\}$ for $\lambda>\lambda_c$.

(f) *Two-piece rate–distortion function.*
$$R_d(D)=\begin{cases}+\infty,& D=0,\\[2pt] \kappa K_d'(\kappa)-K_d(\kappa), & 0<D<D_c,\\[2pt] \lambda_c\,(R_{0,d}^2-D), & D_c\le D\le R_{0,d}^2,\\[2pt] 0,& D\ge R_{0,d}^2,\end{cases}$$
where, on $0<D<D_c$, $\kappa>\kappa_c$ is the unique solution of $b_d(\kappa)=\sqrt{1-D/R_{0,d}^2}$ and $\kappa K_d^{\prime}(\kappa)-K_d(\kappa)=\kappa m_d(\kappa)-\log M_d(\kappa)$. The middle piece is attained by the covariant complex-Bingham channel of field $\kappa$ and the linear face by an independently flagged mixture of the trivial channel and the field-$\kappa_c$ channel. The pieces meet at $D_c$ with value $R_c=\lambda_cR_{0,d}^2b_c^2=\kappa_cR_{0,d}^2b_c/2$.

*Proof.* (a) By (H3) the positive stationary radii at $\lambda$ correspond bijectively to solutions $\kappa>0$ of $\lambda_d(\kappa)=\lambda$, and Theorem 4.1 gives the counts: on $(0,\kappa_f]$, $\lambda_d$ is strictly decreasing with values in $[\lambda_{\min},\lambda_{0,d})$ (the value $\lambda_{0,d}$ is a limit, not attained); on $[\kappa_f,\infty)$ it is strictly increasing onto $[\lambda_{\min},\infty)$. The local type follows from (H4) and the sign of $H_d$; at $\kappa_f$, (H4) and (b) give $G=F_d(\kappa_f)/2<0$.

(b) $F_d'=H_d$ has the sign pattern of Theorem 4.1, $F_d(0)=0$, and (H5). So $F_d<0$ on $(0,\kappa_f]$ and $F_d$ increases strictly from $F_d(\kappa_f)<0$ to $+\infty$ on $[\kappa_f,\infty)$: one zero $\kappa_c>\kappa_f$, with $F_d<0$ on $(\kappa_f,\kappa_c)$ and $F_d>0$ on $(\kappa_c,\infty)$.

(c) Fix $\lambda>0$. $G_{d,\lambda}$ is continuous on $[0,1]$, so a maximizer exists among $\{0\}\cup\{1\}\cup\{\text{interior stationary points}\}$; $b=1$ is excluded by (H2), pre-fold radii by (a) (a strict local minimum of a nonconstant analytic function is not a global maximum), and the degenerate radius at $\lambda_{\min}$ by (a). So the only competitors of $0$ (gain $0$) are post-fold radii, present iff $\lambda>\lambda_{\min}$, unique, equal to $b_d(\kappa_+(\lambda))$ with gain $F_d(\kappa_+(\lambda))/2$ by (H4). Since $\kappa_+$ is the inverse of the strictly increasing $\lambda_d|_{(\kappa_f,\infty)}$, it is continuous and strictly increasing; by (b) the gain is $<0$, $=0$, $>0$ according as $\kappa_+(\lambda)<\kappa_c$, $=\kappa_c$, $>\kappa_c$, i.e. $\lambda<\lambda_c$, $=\lambda_c$, $>\lambda_c$ (note $\lambda_c=\lambda_d(\kappa_c)>\lambda_d(\kappa_f)=\lambda_{\min}$, so the range $\lambda\le\lambda_{\min}$ is included in $\lambda<\lambda_c$).

(d) $\lambda_{\min}<\lambda_c$ was just shown. By (H6), at $\lambda=\lambda_{0,d}$ small positive radii have positive gain, so $0$ is not a global maximizer there; by (c) this forces $\lambda_{0,d}>\lambda_c$.

(e) The first sentence follows from (c), (H1) and the monotonicity of $\kappa_+$. For each fixed $b$, $\lambda\mapsto K_d(2\lambda b)-\lambda R_{0,d}^2(1+b^2)$ is convex ($K_d$ convex), so $c_d$ is convex as a maximum of convex functions, and Danskin's theorem gives $\partial c_d(\lambda)=\operatorname{conv}\{2bK_d'(2\lambda b)-R_{0,d}^2(1+b^2): b\text{ active}\}$; at an active $b>0$, $K_d'(\kappa)=R_{0,d}^2b$ turns the derivative into $-R_{0,d}^2(1-b^2)=-D_b$, and at $b=0$ it is $-R_{0,d}^2$ (1D2Q (112)). Insert the active sets from (c).

(f) $R_d(D)=0$ for $D\ge R_{0,d}^2$ (trivial channel) and $R_d(0)=+\infty$ (zero distortion forces $\hat\rho=\rho_X$ a.s., and $I(X;X)=+\infty$ for the continuous $X$; quantitatively, 1D2Q Prop. 3.3). Let $0<D<D_c$. By (H1) and (c)–(e), $b_d$ maps $(\kappa_c,\infty)$ increasingly onto $(b_c,1)$, so there is a unique $\kappa>\kappa_c$ with $b_d(\kappa)=\sqrt{1-D/R_{0,d}^2}$; put $\lambda=\lambda_d(\kappa)>\lambda_c$. By (c), $b_d(\kappa)$ is the unique global maximizer of $G_{d,\lambda}$, hence active, and $\kappa=2\lambda b_d(\kappa)$. By (A2) the covariant channel attains distortion $D$ at information $I=\kappa m_d(\kappa)-\log M_d(\kappa)=\lambda(R_{0,d}^2-D)-\max_vG_{d,\lambda}(v)$. The right side is the expression inside the supremum of (A1) at this $\lambda$, so $R_d(D)\ge I$; attainment gives $R_d(D)\le I$. Finally $\kappa m_d-\log M_d=\kappa(K_d'+1/d)-K_d-\kappa/d=\kappa K_d'-K_d$. Let $D_c\le D\le R_{0,d}^2$. Taking $\lambda=\lambda_c$ in (A1), where $\max G_{d,\lambda_c}=0$ by (c), gives $R_d(D)\ge\lambda_c(R_{0,d}^2-D)$. Conversely both $0$ and $b_c$ are active at $\lambda_c$; by (A2) the field-$\kappa_c$ channel attains $(D_c,R_c)$ with $R_c=\lambda_c(R_{0,d}^2-D_c)$ and the trivial channel attains $(R_{0,d}^2,0)$; by (A3) their flagged mixture with weight $t=(R_{0,d}^2-D)/(R_{0,d}^2-D_c)$ achieves distortion $D$ with information at most $\lambda_c(R_{0,d}^2-D)$; the preceding lower bound forces equality. The two expressions for $R_c$ agree because $F_d(\kappa_c)=0$ means $K_d(\kappa_c)=\kappa_cK_d'(\kappa_c)/2$, and $\lambda_cR_{0,d}^2b_c^2=\kappa_cR_{0,d}^2b_c/2=\kappa_cK_d'(\kappa_c)/2$. $\square$

*Consequences.* The multiplier $\lambda_{c,d}$ of 1D2Q Theorem 3.1 is the $\lambda_c$ above, its coexisting positive radius is unique and equals $b_c$, and the asymptotics of 1D2Q Theorem 7.3 describe *the* contact. This closes 1D2Q Remark 3.2 for every finite $d\ge3$. By (4.1), $\kappa_f=2d-O(1)$ and, by Remark 3.3, $b_d(\kappa_f)<1/2$, so $\lambda_{\min}=\kappa_f/(2b_d(\kappa_f))>\kappa_f$; numerically $\lambda_{\min}-2d\to0$, matching the birth of stationary points at $\alpha=2$ in 1D2Q Theorem 5.1.

**Corollary 5.2 ($d=2$).** For $0<\lambda\le3$ the unique global maximizer of $G_{2,\lambda}$ is $0$; for $\lambda>3$ it is the unique positive stationary radius, which tends to $0$ as $\lambda\downarrow3$ (continuous onset). Consequently $R_2(D)=\kappa K_2'(\kappa)-K_2(\kappa)$ with $b_2(\kappa)=\sqrt{1-2D}$ for $0<D<1/2$, which is the Dytso–Cardone formula $R_2=\eta r-\log(\sinh\eta/\eta)$, $r=\coth\eta-1/\eta$, under $\kappa=2\eta$.

*Proof.* By Corollary 4.2, $\lambda_2(\kappa)>3$ for all $\kappa>0$ and $\lambda_2$ is a bijection $(0,\infty)\to(3,\infty)$. For $\lambda\le3$, $G'_{2,\lambda}$ has no zero in $(0,1]$ and $G'_{2,\lambda}(1)<0$ (H2), so $G_{2,\lambda}$ is strictly decreasing and $0$ is the unique maximizer. For $\lambda>3$ there is exactly one stationary $b_+\in(0,1)$; $G''(0)>0$ by (H6) and $G'(1)<0$ give $G'>0$ on $(0,b_+)$ and $G'<0$ on $(b_+,1]$. Theorem A applies verbatim (it holds for $d=2$), and the proof of (f) goes through with $D_c$ replaced by $R_{0,2}^2=1/2$. Finally $M_2(\kappa)=(e^\kappa-1)/\kappa$ gives $K_2(\kappa)=\log(\sinh\eta/\eta)$, $b_2=2K_2'=\coth\eta-1/\eta$ and $\kappa K_2'=\eta r$. $\square$

## 6. The coefficient sign law

Theorem 4.1 did not use the coefficients $c_{d,n}$. The following statement, in the format of 61Y0 Lemma 6.1 and 7H9F Theorem 8.2, is nevertheless of independent interest and gives a second (Descartes-type) proof of one fold.

**Theorem 6.1 (one-change law).** Let $d\ge3$ and $N_d=\sum_nc_{d,n}\kappa^n$ as in (2.4). Then $c_{d,0}=c_{d,1}=0$,
$$c_{d,n}<0\ \ (2\le n\le n_d),\qquad c_{d,n}>0\ \ (n>n_d),\qquad n_d=\begin{cases}2d-1,&d=3,4,\\ 2d,&d\ge5.\end{cases}$$
For $d=2$: $c_{2,0}=c_{2,1}=c_{2,2}=0$ and $c_{2,n}>0$ for $n\ge3$. *Status:* proved for all $d\ge2$ and all $n$, except that for $3\le d\le35$ the two indices $n\in\{2d-1,2d\}$ are settled by an exact integer computation (`tail_cases.py`, which covers $3\le d\le60$); for $d\ge36$ these indices are covered by the analytic bound in Lemma 6.2(iv).

By Proposition 3.4, $\operatorname{sign}c_{d,n}=\operatorname{sign}\hat c_{d,n+1}$; we work with $m=n+1$. For $3\le m\le2d+1$ put
$$q_m:=\frac{W_{m-1}}{u_m},\qquad g_m:=\frac{d\,m(m+2d)}{(d-1)(2d+2-m)}.$$
Since $m-2d-2<0$ for $m\le2d+1$, (3.3) gives $\hat c_{d,m}<0\iff q_m>g_m$ for $m\le2d+1$, while for $m\ge2d+2$ both terms of (3.3) are nonnegative and the second is positive, so $\hat c_{d,m}>0$.

**Lemma 6.2.** Let $d\ge3$.

(i) *Recursion.* $q_{m+1}=\dfrac{2(d+m)}{2d-2+m}(q_m+1)$ for $m\ge1$, and $q_3=\dfrac{(d+2)(3d+1)}{d(d-1)}$.

(ii) *Base.* $q_3-g_3=\dfrac{(2d+1)(d-2)}{d(d-1)(2d-1)}>0$.

(iii) *Sub-solution.* $\Pi(m,d):=\dfrac{2(d+m)}{2d-2+m}(g_m+1)-g_{m+1}=\dfrac{m(m-1)(2d^2-dm-d-2)}{(d-1)(2d+1-m)(2d+2-m)}$, which is $\ge0$ for integers $3\le m\le2d-2$ and $<0$ for $m\in\{2d-1,2d\}$.

(iv) *Boundary indices.* $q_{2d}\ge\prod_{k=d-2}^{2d-3}\frac{4d-3-k}{k+1}$ and $q_{2d+1}\ge\prod_{k=d-2}^{2d-2}\frac{4d-2-k}{k+1}$; every factor is $\ge1$ and the $\lfloor d/2\rfloor+1$ factors with $k\le3d/2-2$ are $\ge5/3$. Hence $q_{2d},q_{2d+1}\ge(5/3)^{\lfloor d/2\rfloor+1}$. Also $g_{2d}=\frac{4d^3}{d-1}<g_{2d+1}=\frac{d(2d+1)(4d+1)}{d-1}\le9d^2$ for $d\ge16$, and $(5/3)^{\lfloor d/2\rfloor+1}\ge9d^2$ for all $d\ge36$ (false for $d=34,35$).

*Proof.* (i) Pascal's rule with the symmetry $\binom{T-1}{d-1+m}=\binom{T-1}{d-2}$ gives $W_m=2W_{m-1}+2u_m$, and $u_{m+1}/u_m=(2d-2+m)/(d+m)$; divide. The value of $q_3$ uses $W_2$ and $u_3$ from Proposition 3.4. (ii) Direct: the numerator of $q_3-g_3$ over $d(d-1)(2d-1)$ is $(3d+1)(d+2)(2d-1)-3d^2(2d+3)=2d^2-3d-2$. (iii) The factorization is a rational identity (`induction_check.py`); for $3\le m\le2d$ the denominator is positive and the sign is that of $2d^2-dm-d-2$, which equals $d-2\ge0$ at $m=2d-2$ and $-2$ at $m=2d-1$, and is decreasing in $m$. (iv) For $m=2d$, $T-1=4d-3$ and the window $W_{2d-1}=\sum_{k=d-1}^{3d-2}\binom{4d-3}{k}$ contains the central term $k=2d-2$; keeping only it, $q_{2d}\ge\binom{4d-3}{2d-2}/\binom{4d-3}{d-2}=\prod_{k=d-2}^{2d-3}\frac{4d-3-k}{k+1}$ by telescoping $\binom{N}{j+1}/\binom{N}{j}=\frac{N-j}{j+1}$. A factor is $\ge1$ iff $k\le2d-2$, and for $k\le3d/2-2$ it is $\ge\frac{5d-2}{3d-2}\ge\frac53$; the number of integers $k\in[d-2,3d/2-2]$ is $\lfloor d/2\rfloor+1$. The case $m=2d+1$ ($T-1=4d-2$, central term $k=2d-1$, factors $\ge\frac{5d}{3d-2}\ge\frac53$ for $k\le3d/2-2$) is identical. $g_{2d+1}\le9d^2\iff d^2-15d-1\ge0\iff d\ge16$. For the last claim, $(5/3)^{19}>16400>9\cdot37^2=12321$ covers $d=36,37$, and passing from $d$ to $d+2$ multiplies the left side by $5/3$ and the right side by $((d+2)/d)^2\le(38/36)^2<1.12$. $\square$

*Proof of Theorem 6.1.* Since $\Pi\ge0$ for $m\le2d-2$ and $q\mapsto\frac{2(d+m)}{2d-2+m}(q+1)$ is increasing, (i)–(iii) give by induction $q_m>g_m$, i.e. $\hat c_{d,m}<0$, for $3\le m\le2d-1$ and every $d\ge3$. For $m\ge2d+2$, $\hat c_{d,m}>0$ as noted. The remaining indices are $m\in\{2d,2d+1\}$ (i.e. $n\in\{2d-1,2d\}$). For $d\ge36$, Lemma 6.2(iv) gives $\min(q_{2d},q_{2d+1})\ge(5/3)^{\lfloor d/2\rfloor+1}\ge9d^2\ge g_{2d+1}>g_{2d}$, so $\hat c_{d,2d}<0$ and $\hat c_{d,2d+1}<0$, i.e. $n_d=2d$. For $3\le d\le35$, `tail_cases.py` compares $q_m$ and $g_m$ in exact integer arithmetic: $q_{2d}>g_{2d}$ for all $3\le d\le60$, and $q_{2d+1}>g_{2d+1}$ exactly for $5\le d\le60$, failing at $d=3,4$; this gives $n_d=2d$ for $5\le d\le35$ and $n_d=2d-1$ for $d=3,4$. Together with $\hat c_{d,0}=\hat c_{d,1}=\hat c_{d,2}=0$ (Proposition 3.4) and $c_{d,n}\propto\hat c_{d,n+1}$, the sign pattern is complete. For $d=2$, (iii) is vacuous and $\hat c_{2,m}=(m-6)(2^{m+1}-2)+2m(m+4)$ is $0$ at $m=3$ and positive for $m\ge4$ (it is $4,28,120,\dots$ and the first term is $\ge0$ from $m=6$ on). $\square$

*What the finite check covers.* Exactly the $66$ integer inequalities $q_{2d}>g_{2d}$ and $q_{2d+1}\gtrless g_{2d+1}$ for $3\le d\le35$; each is a comparison of two explicit rationals built from binomial sums (`fractions.Fraction`, `math.comb`). Independently, `verify_signs.py` recomputes every $c_{d,n}$ from the three-term definition in exact rational arithmetic for $2\le d\le40$, $n\le400$ and confirms the pattern and the values of $n_d$. The single central term already suffices analytically from $d\ge11$ ($m=2d+1$) and $d\ge10$ ($m=2d$), so the check could be shortened by summing a few more central terms; we did not pursue this.

*Remark 6.3 (Descartes route).* Theorem 6.1 gives a second proof of the one-zero statement of Theorem 4.1 (without the bounds (4.1)), computer-assisted for $3\le d\le35$. Write $\tilde N_d(\kappa)=\sum_{m\ge3}a_m\kappa^m$ (entire, by Lemma 2.1(i)) with $a_m<0$ for $3\le m\le n_d+1$ and $a_m>0$ for $m\ge n_d+2$ (Theorem 6.1 with $\operatorname{sign}a_m=\operatorname{sign}c_{d,m-1}$). Then
$$Q(\kappa):=\frac{\tilde N_d(\kappa)}{\kappa^{\,n_d+1}}=\sum_{3\le m\le n_d+1}a_m\kappa^{m-n_d-1}+\sum_{m\ge n_d+2}a_m\kappa^{m-n_d-1}$$
is a sum of negative multiples of nonpositive powers (the first sum, which contains the negative constant $a_{n_d+1}$) and of positive multiples of positive powers (the second sum). Termwise differentiation (legitimate on $(0,\infty)$ for an entire function divided by a monomial) gives $Q'(\kappa)=\sum_m(m-n_d-1)a_m\kappa^{m-n_d-2}$, in which every term is $\ge0$ and the terms with $m\ge n_d+2$ are $>0$: $Q$ is strictly increasing on $(0,\infty)$. Since $n_d+1\ge6>3$, the term $a_3\kappa^{2-n_d}$ forces $Q(\kappa)\to-\infty$ as $\kappa\downarrow0$, and $Q(\kappa)\to+\infty$ as $\kappa\to\infty$. Hence $Q$, and so $\tilde N_d$ and $H_d$, has exactly one positive zero, with $H_d<0$ before it and $H_d>0$ after. (This is the standard argument that a power series with one coefficient sign change has at most one positive zero, and the closing step of 7H9F Theorem 8.2. Version 1 of this note misdescribed $Q$ as "a negative constant plus a series with positive coefficients": the negative-power terms are present; they do not spoil the monotonicity because their derivatives are positive. `h6_remark63_check.py` checks $Q'>0$ on a grid for $d=3,\dots,6$.)

*Remark 6.4 (why the 7H9F window argument does not transfer).* In 7H9F the coefficient is a parity-truncated central window mean of the form "$r-\mathbb E\,\delta^2$", controlled by a likelihood-ratio ordering in the window size. Here Lemma 3.1 collapses the three-term expression to a *full* window mass $W_{m-1}$ against a single boundary binomial $u_m$; the sign question becomes window mass versus boundary mass, monotone enough for the sub-solution induction up to $m=2d-1$, with the last two indices exponentially safe.

## 7. Numerical illustration

`chain_numerics.py` (mpmath, 60 digits; 220-step bisection for $\kappa_f$ on $[\kappa_1,2d]$ with $\kappa_1=2(d-2)(d+1)/d$, and for $\kappa_c$ on $(\kappa_f,20d+50]$) gives the values below, printed to 12–14 significant digits; `repro/chain_values_50digits.txt` lists every quantity to 50 digits for fourteen values of $d$. All rows satisfy the proved relations $\kappa_1\le\kappa_f<2d$, $M_d(\kappa_f)\ge d(d-1)/2$, $b_d(\kappa_f)<1/2$, $\kappa_f<\kappa_c$, $\lambda_{\min}<\lambda_c<\lambda_{0,d}$ (asserted in the script).

Table 1: the fold and the bounds (4.1).

| $d$ | $\kappa_1$ | $\kappa_f$ | $2d-\kappa_f$ |
|---|---|---|---|
| 3 | 2.66666666667 | 3.2327088362698 | 2.76729 |
| 5 | 7.2 | 8.4315508759981 | 1.56845 |
| 17 | 31.7647058824 | 33.907100295951 | 0.0928997 |
| 100 | 197.96 | 199.99999999999 | $9.68\cdot10^{-12}$ |

Table 2: the fold radius and the minimal multiplier.

| $d$ | $M_d(\kappa_f)$ | $d(d-1)/2$ | $b_d(\kappa_f)$ | $\lambda_{\min}$ |
|---|---|---|---|---|
| 3 | 4.0410906 | 3 | 0.301630225423 | 5.3587282768762 |
| 5 | 21.107032 | 10 | 0.43508469636 | 9.6895511914568 |
| 17 | 3643.6645 | 136 | 0.498767685262 | 33.990875208891 |
| 100 | $1.0640\cdot10^{15}$ | 4950 | $0.5-2.4\cdot10^{-14}$ | $200-1.9\cdot10^{-13}$ |

Table 3: the contact.

| $d$ | $\kappa_c$ | $b_c$ | $\lambda_c$ | $\lambda_{0,d}$ |
|---|---|---|---|---|
| 3 | 4.3442853031 | 0.400331536002 | 5.42585945949 | 6 |
| 5 | 11.6440880518 | 0.573491039097 | 10.1519354776 | 15 |
| 17 | 52.4714515166 | 0.676014299873 | 38.8094242433 | 153 |
| 100 | 340.64385837 | 0.706438271107 | 241.099521574 | 5050 |

Table 4: the contact point of the rate–distortion function.

| $d$ | $D_c$ | $R_c$ | $\lambda_c/d$ |
|---|---|---|---|
| 3 | 0.559823107522 | 0.579718136073 | 1.8086198 |
| 5 | 0.53688642246 | 2.67111206245 | 2.0303871 |
| 17 | 0.511063215405 | 16.6924477931 | 2.2829073 |
| 100 | 0.495935519424 | 119.118709893 | 2.4109952 |

The $d=3$ and $d=5$ rows agree to $\le5\cdot10^{-9}$, and the $d=17$ row to all printed digits, with an independent brute-force maximization of $G_{d,\lambda}$ over a grid in $b$ (no use of $H_d$, $F_d$, $\Psi_d$ or Lemma 3.1) performed by the adversarial reviewer; the two-piece formula agrees with a brute-force evaluation of the supremum in (A1) to $10^{-14}$ or better at sample points on both pieces. An external recomputation (AIRR workshop, 2026-09-08; 75-digit arithmetic, roots of $H_d$ and $F_d$ evaluated through the Kummer derivatives $M_d'={}_1F_1(2;d+1;\kappa)/d$, $M_d''=2\,{}_1F_1(3;d+2;\kappa)/(d(d+1))$, i.e. without Lemma 3.1 or $\Psi_d$) reproduced $\kappa_f$, $\lambda_{\min}$, $\kappa_c$, $b_c$, $\lambda_c$, $D_c$, $R_c$ for $d=3,5,17,100$ to its printed 20 digits; `workshop_recheck.py` repeats that route at 70 digits and agrees with the $\Psi$-route values of `chain_values_50digits.txt` to 50 significant digits, and confirms the located roots by direct quadrature of the tilted $\mathrm{Beta}(1,d-1)$ moments (residuals $\le10^{-43}$ for $d\le17$ and $\le10^{-11}$ for $d=100$, where the quadrature itself is the limiting error). At $d=100$, $\lambda_c/d=2.4110$ versus $\alpha_*-c_*\log d/d=2.4104$ (1D2Q Thm. 7.3, $\alpha_*=2.455407\ldots$, $c_*=0.977136\ldots$).

The v003 workshop also compared the Kummer-derivative values with direct quadrature after dividing the integrand by its mode value, using 85-digit arithmetic and intervals split around the mode. For $d=3,5,17,100$, the differences in $K_d$, $K_d^{\prime}$ and $K_d^{\prime\prime}$, and both fold/contact residuals, were below $10^{-65}$. This scaling removes the tiny-integral accuracy loss of the earlier $d=100$ quadrature. These are numerical comparisons, not certified interval error bounds. The exact inputs and outputs are included in the revision evidence.

## 8. Open questions

1. *Higher rank.* For rank-$r$ projectors on $\mathrm{Gr}_{\mathbb C}(r,d)$ the analogue of Theorem A needs a global matrix-Bingham (HCIZ) spectral extremum at fixed Frobenius norm, known only for $\mathrm{Gr}_{\mathbb C}(2,4)$ (61Y0) and in a weak/strong-field sense elsewhere; and the radial normalizer is a matrix-argument ${}_1F_1$ for which no first-order equation of the type of Lemma 3.1 is available. Whether the one-fold property persists is open.
2. *Matrix-Jacobi normalizers.* Lemma 3.1 exists because $M_d$ has a single numerator parameter; for ${}_1F_1(a;c;\kappa)$ with $a>1$ (Jacobi-type overlap laws $\mathrm{Beta}(a,c-a)$) the reduction produces a second-order relation and the $(M,\kappa)$ transversality argument must be replaced by one in a three-dimensional phase space. A clean criterion in terms of $(a,c)$ for exactly one fold would unify 7H9F ($L_q$ = even part of $M_{q+1}$) and the present result.
3. *General Bingham fixed-norm extremum.* The spectral input of Theorem A (one positive spike maximizes the projective Laplace transform at fixed traceless norm, all degrees) is the Brazitikos–Pandis extremum. A direct proof adapted to the tilted $\mathrm{Beta}$ structure, or an extension to all rank-$r$ Dirichlet partition functions, would remove the only external black box of this line.
4. Not addressed here, as in 1D2Q: a matching third-order coding theorem and the uniform double scaling $d\to\infty$, $D\downarrow0$.

## 9. Reproducibility

All scripts are in `repro/` next to this file, with a `README.md` listing commands, expected final lines and wall times (Python 3.12.6, sympy 1.14.0, mpmath 1.3.0; `python run_all.py` runs everything and writes `runtimes.txt`).

| script | certifies | arithmetic | time |
|---|---|---|---|
| `sym_check.py` | Lemma 3.2, identities (a)–(f) of Theorem 4.1, $\hat c_{d,3}$, with $d$ symbolic | sympy exact | 2.0 s |
| `check_formula.py` | $N_d=\frac{d-1}{d\kappa}\tilde N_d$ and (3.3) coefficientwise, $2\le d\le12$, $n\le60$ | `Fraction` | 0.3 s |
| `verify_signs.py` | (3.3) against the three-term definition and the sign pattern of Theorem 6.1, $2\le d\le40$, $n\le400$ | `Fraction` | 80.6 s |
| `induction_check.py` | factorization of $\Pi(m,d)$ and its sign table, $3\le d\le60$ | sympy | 3.3 s |
| `tail_cases.py` | recursion (i) for $d\le29$; the boundary comparisons of Theorem 6.1 for $3\le d\le60$; the central-term and $(5/3)^{\lfloor d/2\rfloor+1}$ bounds | exact integers | 0.1 s |
| `boundary_exact.py` | the 66 boundary comparisons as explicit rationals $q_m$, $g_m$, $\hat c_{d,m}$ (written to `boundary_exact.txt`) | `Fraction` | 0.1 s |
| `h6_remark63_check.py` | expansion (2.5) with $d,\lambda$ symbolic; $G_{2,3}(b)=-\frac9{20}b^4+\frac9{35}b^6+O(b^8)$; $Q'>0$ in Remark 6.3 for $d=3,\dots,6$ | sympy; mpmath 30 digits | 2.9 s |
| `chain_numerics.py` | Section 7 tables (14 values of $d$), the asserted inequalities, `chain_values_50digits.txt` | mpmath, 60 digits | 1.4 s |
| `workshop_recheck.py` | the 66 signs from the three-term definition; Section 7 values by the Kummer-derivative route (70 digits) against the workshop's 20 digits and `chain_values_50digits.txt`; quadrature residuals | `Fraction`; mpmath | 2.2 s |

No proof step depends on floating point. The proof of Theorem 4.1 and Theorem 5.1 uses only Lemmas 2.1, 3.1–3.2, the rational identities (a)–(f) (which are one-line hand computations, machine-checked for safety), and Theorem A. Theorem 6.1 depends on `tail_cases.py` for $3\le d\le35$ as stated; the 66 exact rationals it compares are listed in `boundary_exact.txt`, so the finite part of that proof can be checked by hand or by any exact-arithmetic system.

## Changes in internal revision v004 (9 September 2026)

1. Documented and repaired a local arithmetic error in the proof of the external power-sum inequality [BP], with the exact arXiv version and page identified. No main theorem statement changed.
2. Corrected the reproduction runner to propagate subprocess failures and made the expected symbolic identities and coefficient signs mandatory assertions. The nine programs were executed successfully in the audit supplement; the 66 proof-critical signs were also reconstructed separately with exact arithmetic.
3. Preserved the earlier deposited v003 and all its evidence. The current PDF is a new revision prepared for formal assessment, not an editorial acceptance.

## Changes in internal revision v003 (8 September 2026)

1. Added a proof interface for the imported envelope: the precise centered power-sum hypothesis, the Haar/Dirichlet Laplace comparison, the entropy lower bound and active-channel attainment. The cited Brazitikos-Pandis extremal inequality remains an external theorem.
2. Corrected (A3): forgetting an independent mixture flag gives an information upper bound; the matching converse supplies equality on the frontier.
3. Replaced an imprecise moving-target limit notation by the corresponding difference.
4. Kept table captions with their tables and added a scaled-quadrature check that avoids tiny-integral loss at $d=100$; results and limits are recorded separately.
5. Qualified historical AI-review and computation provenance.

## Changes in version 2 (8 September 2026)

Version 2 answers the evaluation of the AIRR workshop of 8 September 2026 (its items for this note are numbered W1–W4 below). Version 1 is kept as `paper_v1.md`.

1. (W1) *Remark 6.3.* Version 1 claimed that $\tilde N_d(\kappa)/\kappa^{n_d+2}$ is "a negative constant plus a series with positive coefficients". This is false: after division there are negative coefficients on negative powers, a positive constant and positive coefficients on positive powers. The remark now divides by $\kappa^{n_d+1}$, differentiates termwise (every term of $Q'$ is $\ge0$, the negative-power terms contributing positive derivatives), and uses the left limit $-\infty$; the conclusion (one zero, one sign change) is unchanged, and Theorem 4.1 never depended on it. Checked on a grid by `h6_remark63_check.py`.
2. (W2) *Fact (H6).* Version 1 stated "$0$ is a strict local maximum iff $\lambda<\lambda_{0,d}$" for all $d\ge2$. At $d=2$, $\lambda=\lambda_{0,2}=3$ this is false: $\mu_{3,2}=0$ and $G_{2,3}(b)=-\frac9{20}b^4+\frac9{35}b^6+O(b^8)$, so $0$ remains a strict local maximum, as Corollary 5.2 already implied. (H6) now separates $\lambda<\lambda_{0,d}$, $\lambda>\lambda_{0,d}$ and $\lambda=\lambda_{0,d}$, the last split into $d\ge3$ (cubic term, not a local maximum) and $d=2$ (quartic term, strict local maximum), and records which cases are used. The expansion is now derived in Lemma 2.1 (new) and checked symbolically.
3. (W3) *Table and title page.* The single twelve-column table of Section 7 overlapped in the PDF; it is replaced by four tables of at most five columns (Tables 1–4), with the values recomputed at 60 digits and listed to 50 digits in `repro/chain_values_50digits.txt`. The bisection of `chain_numerics.py` was replaced by a fixed 220-step bisection because `mpmath.findroot(..., 'bisect')` stopped at about 28 correct digits, short of the 50 digits announced in version 1 (the printed 10-digit values were unaffected). The duplicated date on the title page is removed (the date is set by the rendering metadata only).
4. (W4) *Framing and self-containment.* The introduction now says explicitly that the note is standalone, which single statement it imports (Theorem A), that Lemma 3.1 is a contiguous relation of Kummer's function whose novelty lies in its use, and what a reader gains without 1D2Q. Lemma 2.1 (new) reproves the facts previously cited as 1D2Q eqs. (10), (11), (15); the direct reason for $R_d(0)=+\infty$ is added in the proof of Theorem 5.1(f). The note is deliberately not merged with 1D2Q.
5. *Verification of the workshop's checks.* Its 66 boundary sign comparisons and its 75-digit fold/contact values for $d=3,5,17,100$ were recomputed by routes independent of both the workshop's script and version 1's scripts (`workshop_recheck.py`, `boundary_exact.py`); all agree (Section 7).

No theorem statement changed. The proofs of Theorems 4.1, 5.1 and 6.1 are unchanged except for the explicit case split in (H6), which they use only in the cases $\lambda<\lambda_{0,d}$, $\lambda>\lambda_{0,d}$ and ($d\ge3$, $\lambda=\lambda_{0,d}$).

## AI-assistance statement

The received version declares substantial generative-AI assistance in drafting, mathematical derivations, code and review, attributed there to “Claude Fable 5.1” (Anthropic). That historical model identity, the reported review sessions and their independence have not been authenticated by this workshop. Historical descriptions of an “author” or “reviewer” script identify the supplied files, not a verified independent editorial review. OpenAI Codex assisted with the present private workshop revision: checking arguments and sources, correcting identified errors, running the checks recorded in the accompanying revision report, and preparing the PDF. Numerical checks support only their tested instances. This assistance is not an independent human peer review or a formal AIRR model-assessment report. Lluis Eriksson is the declared author and AIRR founder/operator; this conflict must be handled by the separate editorial process. Scientific authorship and approval remain with the author.

## References

[1D2Q] L. Eriksson, *Exact Rate–Distortion Theory for Complex-Projective Born Prediction: Finite-Dimensional Bingham Frontiers, Thermodynamic Coexistence, and Worst-State Capacity*, ARR-2026-1D2QYXPCVY9H7ANB, v1, 2026-08-13.

[61Y0] L. Eriksson, *Complete Rank-Two Born-Prediction Rate–Distortion on $\mathrm{Gr}_{\mathbb C}(2,4)$: All-Field Matrix–Bingham Rigidity and a Unique Coexistence Transition*, ARR-2026-61Y0FFA39M8KMBJ5, v1, 2026-08-13.

[7H9F] L. Eriksson, *Complete Rate–Distortion Phase Diagram of Haar Oriented Two-Planes: One-Change Hypergeometric Coefficients, Unique Coexistence, and No Reentrance*, ARR-2026-7H9FAPTBZA897AMJ, v2, 2026-08-14.

[BP] S. Brazitikos and C. Pandis, *Sharp Inequalities for Symmetric Polynomials, Hunter's Conjecture, and Moments of Exponential Random Variables*, arXiv:2512.12254v1 [math.PR], 2025 (Proposition 5.5; local estimate clarified in Section 2).

[DLMF] NIST Digital Library of Mathematical Functions, Chapter 13 (Confluent Hypergeometric Functions), §13.3 (recurrence relations and derivatives), https://dlmf.nist.gov/13.3.

[DC] A. Dytso and M. Cardone, *Uniform Distribution on $(n-1)$-Sphere: Rate-Distortion under Squared Error Distortion*, arXiv:2401.04248 [cs.IT], 2024.

[EE] T. Eisele and R. S. Ellis, *Multiple phase transitions in the generalized Curie–Weiss model*, J. Stat. Phys. 52 (1988), no. 1–2, 161–202.

[KS] D. Karp and S. M. Sitnik, *Log-convexity and log-concavity of hypergeometric-like functions*, J. Math. Anal. Appl. 364 (2010), 384–394.

[KK] S. I. Kalmykov and D. B. Karp, *Log-convexity and log-concavity for series in gamma ratios and applications*, arXiv:1211.2882 [math.CA], 2012.

[S] S. M. Sitnik, *A conjecture on monotonicity of a ratio of Kummer hypergeometric functions*, arXiv:1207.0936 [math.CA], 2012.
