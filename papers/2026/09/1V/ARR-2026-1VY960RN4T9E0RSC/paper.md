# One Fold if and only if the Overlap Law is Right-Skewed: A Riccati Criterion for Tilted Beta Normalizers, with Consequences for Rank-One Projective Rate–Distortion

**Lluis Eriksson** (Independent researcher)

## Abstract

For $M={}_1F_1(a;c;\kappa)$, the moment generating function of $X\sim\mathrm{Beta}(a,c-a)$, the stationary multiplier $\lambda(\kappa)=\kappa/(2b(\kappa))$ of the Curie–Weiss-type radial problem $\max_{0\le b\le1}\{K(2\lambda b)-\lambda R^2b^2\}$, $K=\log M-(a/c)\kappa$, folds where $H=K'-\kappa K''$ vanishes. We show that the logarithmic derivative $m=M'/M$ satisfies the Riccati equation $\kappa m'=a-(c-\kappa)m-\kappa m^2$, so that $H=m(1-m)\,(\Psi(m)-\kappa)$ with $\Psi$ an explicit rational function, and a transversality argument in the plane $(m,\kappa)$ proves: $H$ has exactly one positive zero if $c>2a$ (right-skewed overlap law) and none if $c\le2a$. This settles the second open question of ARR-2026-68BH5JDJCQ8XW8GT, gives the complete scalar radial phase and two-piece envelope for every $(a,c)$ with explicit fold bounds for $a\ge1$ (false for $a<1$), covers the Bessel family ${}_0F_1(;c;\kappa^2/4)$ (no fold), and yields "one fold iff $d\ge3$" for rank-one sources over $\mathbb R$, $\mathbb C$, $\mathbb H$. For the oriented-two-plane normalizer, which is third order, we give an exact identity and numerics only.

## 1. Introduction

**Antecedents.** The record ARR-2026-68BH5JDJCQ8XW8GT (*One Fold, Unique Contact and the Complete Two-Piece Rate–Distortion Function of Rank-One Complex-Projective Born Prediction*; below "68BH") proved that for $M_d={}_1F_1(1;d;\kappa)$, $d\ge3$, the fold numerator $H_d=K_d'-\kappa K_d''$ has exactly one positive zero (its Theorem 4.1), and derived from this, through the standing facts (H1)–(H6) of its Section 5, the complete radial phase and the two-piece rate–distortion function of Haar rank-one Born prediction on $\mathbb{CP}^{d-1}$ (its Theorem 5.1, closing Remark 3.2 of ARR-2026-1D2QYXPCVY9H7ANB, "1D2Q", whose Theorem 2.1 is the envelope formula). The tool there was the inhomogeneous first-order equation $\kappa M_d'=(\kappa-d+1)M_d+(d-1)$ (68BH Lemma 3.1), available because the first Kummer parameter equals $1$; 68BH's second open question asked for a criterion in $(a,c)$ for ${}_1F_1(a;c;\kappa)$, anticipating that "the $(M,\kappa)$ transversality argument must be replaced by one in a three-dimensional phase space". Sibling records reached one-fold statements in other geometries by coefficient sign patterns: ARR-2026-61Y0FFA39M8KMBJ5 ("61Y0", Lemma 6.1, Theorem 6.2, Corollary 6.3) for $\mathrm{Gr}_{\mathbb C}(2,4)$, and ARR-2026-7H9FAPTBZA897AMJ ("7H9F", Lemma 7.1, Theorems 7.2, 8.2, 9.1) for oriented two-planes in $\mathbb R^n$, whose normalizer $L_q=\mathbb E\cosh(\kappa T)$, $T\sim\mathrm{Beta}(1,q)$, $q=n-2$, is the even part of $M_{q+1}$. Phase-lifted coherent orbits (ARR-2026-6XH6JAS5ZA934A6J, "6XH6"; ARR-2026-6DJ302B1G38V4SHD, "6DJ3") have ${}_pF_{p+1}$ normalizers, the simplest being the Bessel function ${}_0F_1(;n;\kappa^2/4)$ (6XH6 Proposition 7.1, $k=1$). Externally: Kummer's equation, its integral representation and its large-argument expansion are DLMF §13.2, §13.4, §13.7 [DLMF13]; Kummer's second theorem, relating ${}_1F_1(\nu+\tfrac12;2\nu+1;2z)$ to $I_\nu(z)$, is DLMF 13.6.9; the reduction of a second-order linear equation to a first-order Riccati equation for the logarithmic derivative is classical [Ince]; the uniform law on $S^{n-1}$ has a smooth rate–distortion curve (Dytso–Cardone [DC]); generalized Curie–Weiss models may have several first-order transitions (Eisele–Ellis [EE]); the real and complex Bingham normalizers are ${}_1F_1(\tfrac12;\tfrac d2;\cdot)$ and ${}_1F_1(1;d;\cdot)$ (Bingham [B], Kent [K]); and the Kummer-ratio literature (Karp–Sitnik [KS], Kalmykov–Karp [KK]) concerns monotonicity of ratios such as $m=M'/M$, not the sign of $K'-\kappa K''$.

**Contribution.** (i) A one-parameter Riccati reduction (Theorem 3.1): for every $a>0$, $c>a$, the state needed to decide the sign of $H$ is $(m,\kappa)$, two-dimensional, not three. (ii) The criterion (Theorem 4.1): $H$ has exactly one positive zero if $c>2a$ and none if $c\le2a$; equivalently, one fold iff the overlap law $\mathrm{Beta}(a,c-a)$ is right-skewed. (iii) Explicit bounds on the fold for $a\ge1$ (Theorem 5.1), with counterexamples for $a<1$. (iv) The complete scalar radial phase and its two-piece envelope for every $(a,c)$ (Theorem 6.1), with a precise list of what must be imported to read the envelope as a rate–distortion function. (v) No fold for the Bessel family (Theorem 7.1, Proposition 7.2) and "one fold iff $d\ge3$" for rank-one sources over the three fields (Theorem 7.4). (vi) For the third-order oriented-two-plane normalizer, an exact identity $(\kappa^{2q+2}L_q^3H_q)'=\kappa^{2q+2}L_q^3\Delta_q$ and exact small-field signs (Section 8), but no new proof of 7H9F Theorem 8.2. 68BH's conventions are restated in Section 2 and every step of the chain to the envelope is written out. Findings of an independent adversarial review are incorporated (Section 7: the range $c\ge1/2$; Section 8: Proposition 8.2).

## 2. Setting

Throughout $a>0$, $c>a$, $\kappa>0$, and $X\sim\mathrm{Beta}(a,c-a)$ with density $x^{a-1}(1-x)^{c-a-1}/B(a,c-a)$ on $(0,1)$. By DLMF 13.4.1,
$$M(\kappa):=\mathbb E\,e^{\kappa X}={}_1F_1(a;c;\kappa)=\sum_{j\ge0}\frac{(a)_j}{(c)_j}\frac{\kappa^j}{j!},\qquad \mu:=\mathbb EX=\frac ac,\qquad R^2:=1-\mu. \tag{2.1}$$
$M$ is entire, positive and strictly increasing on $[0,\infty)$. Put $K(\kappa)=\log M(\kappa)-\mu\kappa$ (the cumulant generating function of $X-\mu$), $m=M'/M=\mathbb E_\kappa X$ (the tilted mean under the law $\propto e^{\kappa x}$), so $K'=m-\mu$ and $K''=m'=\mathrm{Var}_\kappa X>0$. The radial problem and its stationary parametrization are
$$G_\lambda(b)=K(2\lambda b)-\lambda R^2b^2\ (0\le b\le1),\qquad b(\kappa)=\frac{K'(\kappa)}{R^2}=\frac{m(\kappa)-\mu}{1-\mu},\qquad \lambda(\kappa)=\frac{\kappa}{2b(\kappa)}, \tag{2.2}$$
and the fold numerator and coexistence function are
$$H:=K'-\kappa K''=(m-\mu)-\kappa m',\qquad F:=2K-\kappa K'. \tag{2.3}$$
Direct differentiation gives $F'=H$, $\lambda'=H/(2R^2b^2)$, and at a stationary radius ($K'(\kappa)=R^2b$, $\lambda=\kappa/(2b)$) $G_\lambda(b)=F(\kappa)/2$ and $\partial_b^2G_\lambda(b)=-(2\lambda/b)H(\kappa)$ (`manuscript_checks.py`). For $a=1$, $c=d$ these are (2.1)–(2.4) of 68BH: $R^2=R_{0,d}^2=1-1/d$, $K=K_d$, $H=H_d$, $F=F_d$, $\lambda_0=d(d+1)/2$. The constant $R^2$ plays no role in the zero counts of $H$ and $F$; it fixes $b$ and $\lambda$.

*Sources with this overlap law.* For $x$ Haar on the unit sphere of $\mathbb F^d$ ($\mathbb F=\mathbb R,\mathbb C,\mathbb H$, $\beta=1,2,4$) and a fixed unit $u$, $|\langle x,u\rangle|^2\sim\mathrm{Beta}(\beta/2,\beta(d-1)/2)$, giving $(a,c)=(\tfrac12,\tfrac d2)$, $(1,d)$, $(2,2d)$: the real Bingham/Watson, complex Bingham and quaternionic normalizers $\mathbb E e^{\kappa|\langle x,u\rangle|^2}$. The case $\beta=2$ is the source of 1D2Q/68BH. Two symmetric families are treated in Sections 7–8: $Z_c(\kappa)={}_0F_1(;c;\kappa^2/4)$ (spheres) and $L_q$ (oriented two-planes).

## 3. The Riccati reduction

**Theorem 3.1.** For every $a>0$, $c>a$ and $\kappa>0$,
$$\kappa m'=a-(c-\kappa)m-\kappa m^2, \tag{3.1}$$
$$H=-\kappa m(1-m)+(c+1)(m-\mu)=m(1-m)\big(\Psi(m)-\kappa\big),\qquad \Psi(m):=\frac{(c+1)(m-\mu)}{m(1-m)}. \tag{3.2}$$
In particular $\operatorname{sign}H(\kappa)=\operatorname{sign}\big(\Psi(m(\kappa))-\kappa\big)$.

*Proof.* Kummer's equation $\kappa M''+(c-\kappa)M'-aM=0$ (DLMF 13.2.1) divided by $M$, with $M''/M=m'+m^2$, is (3.1). Then $H=(m-\mu)-\kappa m'=(m-\mu)-a+(c-\kappa)m+\kappa m^2=-\kappa m(1-m)+(c+1)m-(c+1)\mu$, using $a=c\mu$. The factorization is immediate. $\square$

This is the general-$(a,c)$ analogue of 68BH Lemma 3.2. No inhomogeneous first-order equation is needed: the logarithmic derivative of any solution of a second-order linear equation satisfies a first-order Riccati equation [Ince]. The relevant state is therefore $(m,\kappa)$, and 68BH's expectation of a three-dimensional phase space for $a\ne1$ was too pessimistic; the general even-part reduction in Section 8 instead uses three state variables, without asserting that this dimension is minimal.

**Lemma 3.2 (behaviour at the ends).** (i) With $\kappa_j$ the cumulants of $X$, for sufficiently small $|\kappa|$ we have $H=\sum_{j\ge3}\kappa_j(2-j)\kappa^{j-1}/(j-1)!$; hence
$$H(\kappa)=-\frac{\mu_3}{2}\kappa^2-\frac{\kappa_4}{3}\kappa^3+O(\kappa^4),\qquad \mu_3=\frac{2a(c-a)(c-2a)}{c^3(c+1)(c+2)}, \tag{3.3}$$
and at $c=2a$ (where $\mu_3=0$) the cubic coefficient is $-\kappa_4/3=1/(8(2a+1)^2(2a+3))>0$.
(ii) $m(\kappa)=1-(c-a)/\kappa+O(\kappa^{-2})$ and $\kappa m'\to0$; hence $H\to1-\mu>0$ as $\kappa\to\infty$. (iii) $\log M(\kappa)=\kappa-(c-a)\log\kappa+\log(\Gamma(c)/\Gamma(a))+o(1)$, so $F(\kappa)=R^2\kappa-2(c-a)\log\kappa+O(1)\to+\infty$. (iv) $m:(0,\infty)\to(\mu,1)$ is a $C^\infty$ increasing bijection.

*Proof.* (i) $K=\sum_{j\ge2}\kappa_j\kappa^j/j!$ termwise; the third central moment of $\mathrm{Beta}(a,c-a)$ from $\mathbb EX^r=(a)_r/(c)_r$ and $\kappa_4$ at $c=2a$ are the displayed values (`manuscript_checks.py`). (ii) DLMF 13.7.1 gives ${}_1F_1(\alpha;\gamma;\kappa)=e^\kappa\kappa^{\alpha-\gamma}\frac{\Gamma(\gamma)}{\Gamma(\alpha)}\big(1+\frac{(1-\alpha)(\gamma-\alpha)}{\kappa}+O(\kappa^{-2})\big)$; applying it to $m=\frac ac\,{}_1F_1(a+1;c+1;\kappa)/{}_1F_1(a;c;\kappa)$ gives the expansion of $m$, and (3.1) then gives $\kappa m'=a-cm+\kappa m(1-m)=O(\kappa^{-1})$. (iii) is the leading term of the same expansion; $F=2\log M-\mu\kappa-\kappa m$. (iv) $m'=\mathrm{Var}_\kappa X>0$, $m(0^+)=\mu$, and $m\to1$ by (ii). $\square$

## 4. The one-fold criterion

**Theorem 4.1.** Let $a>0$, $c>a$.

(A) If $c>2a$, then $H$ has exactly one positive zero $\kappa_f$, with $H<0$ on $(0,\kappa_f)$ and $H>0$ on $(\kappa_f,\infty)$; moreover $m_f:=m(\kappa_f)\ge\tfrac12$ and
$$\kappa_f=\Psi(m_f)\ \ge\ \Psi(\tfrac12)=\frac{2(c+1)(c-2a)}{c}. \tag{4.1}$$
Consequently $\lambda(\kappa)$ decreases strictly on $(0,\kappa_f]$ from $\lambda_0:=\lambda(0^+)=c(c+1)/(2a)$ to $\lambda_{\min}:=\lambda(\kappa_f)$ and increases strictly on $[\kappa_f,\infty)$ to $+\infty$.

(B) If $c\le2a$, then $H>0$ on $(0,\infty)$, and $\lambda$ increases strictly from $\lambda_0$ to $+\infty$.

*Proof.* By Lemma 3.2(iv) let $\kappa(m)$ be the inverse of $m(\kappa)$ on $(\mu,1)$ and set $D(m):=\Psi(m)-\kappa(m)$, so that $\operatorname{sign}H(\kappa)=\operatorname{sign}D(m(\kappa))$ by (3.2). By (3.1), $d\kappa/dm=1/m'(\kappa)=G(m,\kappa(m))$ with
$$G(m,\kappa):=\frac{\kappa}{a-cm+\kappa m(1-m)},\qquad D'(m)=\Psi'(m)-G(m,\kappa(m)).$$
The following are rational identities in $(a,c,m)$ (`manuscript_checks.py`):

(a) $\Psi'(m)=(c+1)\big[(m-\mu)^2+\mu(1-\mu)\big]/(m(1-m))^2>0$ on $(\mu,1)$.

(b) On the curve $\kappa=\Psi(m)$ the denominator of $G$ equals $m-\mu>0$, and $G(m,\Psi(m))=\Psi(m)/(m-\mu)$.

(c) $\Delta(m):=\Psi'(m)-G(m,\Psi(m))=-(c+1)(m-\mu)(1-2m)/(m(1-m))^2$; on $(\mu,1)$ it has the sign of $2m-1$.

(d) $\partial_\kappa G(m,\kappa)=(a-cm)/(a-cm+\kappa m(1-m))^2<0$ for $m>\mu$ wherever the denominator is nonzero; the denominator is affine and increasing in $\kappa$.

At a zero $m_0$ of $D$ one has $\kappa(m_0)=\Psi(m_0)$, hence $D'(m_0)=\Delta(m_0)$. From Lemma 3.2: (e) $D<0$ near $\mu^+$ iff $H<0$ near $0^+$ iff $\mu_3>0$ iff $c>2a$, while for $c\le2a$ $D>0$ near $\mu^+$ ($\mu_3<0$, or the positive cubic coefficient at $c=2a$); (f) $D>0$ near $1^-$ since $H\to1-\mu>0$.

*Case $c>2a$, i.e. $\mu<\tfrac12$.* Step 1 ($D<0$ on $(\mu,\tfrac12)$, $D(\tfrac12)\le0$): if $D\ge0$ somewhere in $(\mu,\tfrac12)$, let $m_*$ be the infimum of such points; by (e) $m_*>\mu$, $D(m_*)=0$ and $D<0$ before, so $D'(m_*)\ge0$; but $D'(m_*)=\Delta(m_*)<0$ by (c). Step 2 (on $[\tfrac12,1)$, $D<0\Rightarrow D'>0$): if $D(m)<0$ then $\kappa(m)>\Psi(m)$; the denominator of $G(m,\cdot)$ is positive at $\kappa(m)$ (it equals $\kappa m'>0$) and at $\Psi(m)$ (by (b)), hence on the whole segment $[\Psi(m),\kappa(m)]$, where (d) gives $G(m,\kappa(m))<G(m,\Psi(m))$; so $D'(m)>\Delta(m)\ge0$, strictly even at $m=\tfrac12$. Step 3: let $m_f:=\inf\{m\ge\tfrac12:D(m)\ge0\}$, which exists by (f); $D(m_f)=0$ and $D<0$ on $(\mu,m_f)$ by Step 1. If $D(m_2)<0$ for some $m_2>m_f$, let $m_3=\sup\{m\in[m_f,m_2]:D(m)\ge0\}$; then $D(m_3)=0$, $D<0$ on $(m_3,m_2]$, where Step 2 makes $D$ strictly increasing, so $D(m_2)>0$: contradiction. Thus $D\ge0$ on $[m_f,\infty)$, and a zero $m_0>m_f\ge\tfrac12$ would be a local minimum with $D'(m_0)=\Delta(m_0)>0$: impossible. Hence $D<0$ on $(\mu,m_f)$, $D>0$ on $(m_f,1)$, i.e. $H$ has the unique zero $\kappa_f=\kappa(m_f)$ with the stated signs, $m_f\ge\tfrac12$, and $\kappa_f=\Psi(m_f)\ge\Psi(\tfrac12)$ because $\Psi$ is increasing by (a); $\Psi(\tfrac12)$ is a direct evaluation. (A tangential zero at $m_f=\tfrac12$, where $\Delta=0$, is not excluded and does not affect the argument.)

*Case $c\le2a$, i.e. $\mu\ge\tfrac12$.* Now $\Delta>0$ on $(\mu,1)$ by (c) and $D>0$ near $\mu^+$ by (e). A first zero $m_*$ of $D$ would satisfy $D'(m_*)\le0$, contradicting $D'(m_*)=\Delta(m_*)>0$. So $D>0$, i.e. $H>0$, on $(0,\infty)$.

The statements on $\lambda$ follow from $\lambda'=H/(2R^2b^2)$, $\lambda(0^+)=R^2/(2K''(0))=R^2/(2v)$ with $v=\mathrm{Var}X=a(c-a)/(c^2(c+1))$, which equals $c(c+1)/(2a)$, and $\lambda(\kappa)=\kappa/(2b)>\kappa/2\to\infty$ since $b<1$. $\square$

*Remarks.* (1) For $a=1$, $c=d$, Theorem 4.1 reproduces 68BH Theorem 4.1 and Corollary 4.2, including the lower bound $2(d-2)(d+1)/d$; the phase plane differs ($(M,\kappa)$ there, $(m,\kappa)$ here), the argument is the same. (2) The threshold is forced by two facts that do not depend on the fine structure of $M$: the transversality sign $\Delta$ changes at $m=\tfrac12$ for every $(a,c)$, and a fold requires the trajectory to start below $\tfrac12$ ($\mu<\tfrac12$) with $H<0$ there ($\mu_3>0$); both say $c>2a$. (3) At the fold the tilted mean is at least $\tfrac12$, i.e. $b_f:=b(\kappa_f)\ge(c-2a)/(2(c-a))$.

## 5. Bounds on the fold for $a\ge1$, and their failure for $a<1$

**Theorem 5.1.** Let $c>2a$ and $a\ge1$. Then $\kappa(1-m(\kappa))<c-a$ for all $\kappa>0$, and
$$\tfrac12\le m_f<m_u:=\frac{a(c+1)}{c(a+1)},\qquad \frac{2(c+1)(c-2a)}{c}\le\kappa_f<\Psi(m_u)=c(a+1). \tag{5.1}$$

*Proof.* Write $Z(\kappa)=\int_0^1x^{a-1}(1-x)^{c-a-1}e^{\kappa x}dx=B(a,c-a)M(\kappa)$ and integrate by parts against $d[(1-x)^{c-a}]$: $(c-a)Z=-\int_0^1x^{a-1}e^{\kappa x}\,d\big[(1-x)^{c-a}\big]=\big[\,x^{a-1}e^{\kappa x}(1-x)^{c-a}\big]_{1}^{0}+\int_0^1(1-x)^{c-a}\big((a-1)x^{a-2}+\kappa x^{a-1}\big)e^{\kappa x}dx$. The boundary term is $[a=1]$ (it vanishes at $x=1$ and at $x=0$ for $a>1$), and for $a\ge1$ the remaining integrand is integrable ($x^{a-2}$ is integrable at $0$ iff $a>1$, and the term is absent for $a=1$). Dividing by $Z$,
$$c-a=\frac{[a=1]}{Z(\kappa)}+(a-1)\,\mathbb E_\kappa\!\Big[\frac{1-X}{X}\Big]+\kappa\,\mathbb E_\kappa[1-X]\qquad(a\ge1). \tag{5.2}$$
At $a=1$ the middle term in (5.2) is absent: it is not interpreted as zero times a divergent expectation. All three terms are $\ge0$ and the last is $>0$, so $\kappa(1-m)<c-a$. Now (3.2) can be rearranged as $H=m\big[(c-a)-\kappa(1-m)\big]+(a+1)m-(c+1)\mu$, hence $H>(a+1)m-(c+1)\mu\ge0$ whenever $m\ge m_u$. Therefore $m_f<m_u$; since $\mu<m_u<1$ (as $a<c$) and $\Psi$ is increasing, $\kappa_f=\Psi(m_f)<\Psi(m_u)$, and $\Psi(m_u)=c(a+1)$ is a rational identity (`manuscript_checks.py`). $\square$

For $a=1$, $c=d$, (5.1) is 68BH's $\kappa_{f,d}<2d$ and its Remark 3.3 ($b_f<\tfrac12$, equivalent to $m_f<(d+1)/(2d)$).

**Proposition 5.2 (failure for $a<1$).** For $a<1$ the identity (5.2) does not hold (the term $x^{a-2}$ is not integrable at $0$), the inequality $\kappa(1-m)\le c-a$ can fail, and the bound $\kappa_f<c(a+1)$ can also fail. Numerically (`checks_bounds.py`, `tables_ac.py`; independently reproduced in review): $\sup[\kappa(1-m)-(c-a)]$ over the tested grid is $2.46$ for $a=\tfrac14$, $1.15$ for $a=\tfrac12$, $0.41$ for $a=\tfrac34$, and $\le10^{-27}$ for $a=1$; and $(a,c)=(\tfrac12,2)$ has $\kappa_f=3.8790>3=c(a+1)$, $(1/4,1)$ has $\kappa_f=2.8009>1.25$ (Table 4). No upper bound on $\kappa_f$ is claimed for $a<1$; the lower bounds of (4.1) hold for every $a$.

## 6. Consequences for the rate–distortion chain

*Standing facts,* valid for all $a>0$, $c>a$, $\kappa>0$, $\lambda>0$ (the analogues of 68BH (H1)–(H6)):

(H1) $b'=m'/R^2>0$, $b(0^+)=0$, $b(\kappa)\to1$ (Lemma 3.2(iv)).

(H2) $K'(\kappa)=m-\mu<1-\mu=R^2$ because $X<1$ a.s.; hence $G_\lambda'(1)=2\lambda(K'(2\lambda)-R^2)<0$: $b=1$ is never stationary and never a maximizer.

(H3) For $b\in(0,1]$: $G_\lambda'(b)=0$ iff $b=b(\kappa)$ and $\lambda=\lambda(\kappa)$ with $\kappa=2\lambda b$; $\kappa\mapsto b(\kappa)$ is injective by (H1).

(H4) At such a radius $G_\lambda(b)=F(\kappa)/2$ and $G_\lambda''(b)=-(2\lambda/b)H(\kappa)$ (Section 2).

(H5) $F'=H$, $F(0)=0$, $F\to+\infty$ (Lemma 3.2(iii)).

(H6) $G_\lambda(b)=\lambda(2\lambda v-R^2)b^2+\tfrac43\lambda^3\mu_3b^3+O(b^4)$ with $v=a(c-a)/(c^2(c+1))$, $\lambda_0=R^2/(2v)=c(c+1)/(2a)$; so $0$ is a strict local maximum of $G_\lambda$ for $\lambda<\lambda_0$, a strict local minimum for $\lambda>\lambda_0$, and for $c>2a$ (where $\mu_3>0$) not a local maximum at $\lambda=\lambda_0$.

**Theorem 6.1 (complete scalar radial phase and envelope).** Let $a>0$, $c>a$, and define $\tilde c(\lambda):=\max_{0\le b\le1}G_\lambda(b)$ and, for $0<D\le R^2$, the envelope
$$\mathcal R(D):=\sup_{\lambda\ge0}\big\{\lambda(R^2-D)-\tilde c(\lambda)\big\}. \tag{6.1}$$

*(I) Case $c>2a$.* Let $\kappa_f$, $\lambda_{\min}$ be as in Theorem 4.1(A).
(a) The positive stationary radii of $G_\lambda$ are the $b(\kappa)$ with $\lambda(\kappa)=\lambda$: none for $\lambda<\lambda_{\min}$; one ($b(\kappa_f)$, degenerate, with gain $F(\kappa_f)/2<0$) at $\lambda_{\min}$; two, $b(\kappa_-)<b(\kappa_+)$ with $\kappa_-<\kappa_f<\kappa_+$, for $\lambda_{\min}<\lambda<\lambda_0$; one, $b(\kappa_+)$ with $\kappa_+>\kappa_f$, for $\lambda\ge\lambda_0$. Pre-fold radii are strict local minima, post-fold radii strict local maxima.
(b) $F$ decreases strictly on $(0,\kappa_f]$, is negative there, then increases strictly to $+\infty$: it has a unique positive zero $\kappa_c>\kappa_f$. Put $b_c=b(\kappa_c)$, $\lambda_c=\lambda(\kappa_c)$, $D_c=R^2(1-b_c^2)$, $R_c=\kappa_cK'(\kappa_c)-K(\kappa_c)=\lambda_cR^2b_c^2$.
(c) The global maximizers of $G_\lambda$ on $[0,1]$ are $\{0\}$ for $0<\lambda<\lambda_c$, $\{0,b_c\}$ at $\lambda_c$, $\{b(\kappa_+(\lambda))\}$ for $\lambda>\lambda_c$, where $\kappa_+(\lambda)>\kappa_c$ is the unique post-fold solution of $\lambda(\kappa)=\lambda$.
(d) $0<\lambda_{\min}<\lambda_c<\lambda_0$.
(e) On $(\lambda_c,\infty)$, $\lambda\mapsto b(\kappa_+(\lambda))$ is continuous and strictly increasing to $1$ (no reentrance); $\tilde c$ is convex with $R^2-\partial\tilde c(\lambda)=\{R^2\}$ for $\lambda<\lambda_c$, $[D_c,R^2]$ at $\lambda_c$, $\{D(\lambda)\}$ for $\lambda>\lambda_c$, $D(\lambda):=R^2(1-b(\kappa_+(\lambda))^2)$.
(f) $\mathcal R(D)=\lambda_c(R^2-D)$ for $D_c\le D\le R^2$, and $\mathcal R(D)=\kappa K'(\kappa)-K(\kappa)$ for $0<D<D_c$, where $\kappa>\kappa_c$ is the unique solution of $b(\kappa)=\sqrt{1-D/R^2}$; $\mathcal R(D)\to\infty$ as $D\downarrow0$.

*(II) Case $c\le2a$.* For $0<\lambda\le\lambda_0$ the unique global maximizer is $0$; for $\lambda>\lambda_0$ it is the unique positive stationary radius $b_+(\lambda)$, which increases continuously from $0$ (as $\lambda\downarrow\lambda_0$) to $1$: continuous onset, no coexistence, no reentrance. $\mathcal R(D)=\kappa K'(\kappa)-K(\kappa)$ for $0<D<R^2$ with $b(\kappa)=\sqrt{1-D/R^2}$.

*Proof.* (I)(a)–(e) follow the argument of 68BH Theorem 5.1(a)–(e), with the normalization of $\tilde c$ stated here, which uses only the sign pattern of $H$ (Theorem 4.1(A)), $F'=H$ and (H1)–(H6); we indicate the steps. (a) is (H3) with the counts from the monotonicity of $\lambda(\kappa)$ (the value $\lambda_0$ is a limit, not attained on $(0,\kappa_f]$), the local type from (H4), and the degenerate gain from (b). (b) is $F'=H$, $F(0)=0$, (H5). (c): a maximizer exists among $\{0\}$, $\{1\}$ and the interior stationary points; $1$ is excluded by (H2), pre-fold radii and the degenerate radius by (a); the only competitor of $0$ (gain $0$) is the post-fold radius, present iff $\lambda>\lambda_{\min}$, unique, with gain $F(\kappa_+(\lambda))/2$, whose sign is that of $\kappa_+(\lambda)-\kappa_c$ by (b); $\kappa_+$ is the inverse of the strictly increasing $\lambda|_{(\kappa_f,\infty)}$. (d): $\lambda_{\min}<\lambda_c$ from $\kappa_c>\kappa_f$; at $\lambda_0$ small radii have positive gain by (H6), so $0$ is not a global maximizer and (c) forces $\lambda_c<\lambda_0$. (e): the first claim is (c), (H1) and the monotonicity of $\kappa_+$; for fixed $b$, $\lambda\mapsto G_\lambda(b)$ is convex, so $\tilde c$ is convex, and Danskin's theorem gives $\partial\tilde c(\lambda)=\operatorname{conv}\{2bK'(2\lambda b)-R^2b^2:b\ \text{active}\}$, which at an active radius equals $R^2b^2$ (using $K'(\kappa)=R^2b$ for $b>0$) and at $b=0$ equals $0$. Thus $R^2-\partial\tilde c$ is exactly the stated distortion set.

(f) Fix $D\in(0,R^2]$. The function $\varphi(\lambda):=\lambda(R^2-D)-\tilde c(\lambda)$ is concave with $\partial\varphi(\lambda)=\{D_b-D:b\ \text{active at }\lambda\}$ convexified, where $D_b:=R^2(1-b^2)$ ($D_0=R^2$); it is maximized at $\lambda^*$ iff $D\in\operatorname{conv}\{D_b:b\ \text{active at }\lambda^*\}$. If $D_c\le D\le R^2$, take $\lambda^*=\lambda_c$: by (c) the active set is $\{0,b_c\}$, so $[D_c,R^2]\ni D$, and $\tilde c(\lambda_c)=0$, giving $\mathcal R(D)=\lambda_c(R^2-D)$. If $0<D<D_c$, by (e) there is a unique $\lambda^*>\lambda_c$ with $D(\lambda^*)=D$; its active radius is $b=b(\kappa)$, $\kappa=\kappa_+(\lambda^*)$, with $\tilde c(\lambda^*)=F(\kappa)/2=K(\kappa)-\kappa K'(\kappa)/2$ by (H4), so $\mathcal R(D)=\lambda^*R^2b^2-K(\kappa)+\kappa K'(\kappa)/2=\kappa K'(\kappa)-K(\kappa)$ (using $\lambda^*b=\kappa/2$ and $R^2b=K'(\kappa)$); and $b(\kappa)=\sqrt{1-D/R^2}$ has a unique solution $\kappa>\kappa_c$ by (H1). As $D\downarrow0$, $\kappa\to\infty$ and $\kappa K'-K=\kappa m-\log M\sim(c-a)\log\kappa\to\infty$ by Lemma 3.2. The two forms of $R_c$ agree because $F(\kappa_c)=0$.

(II) By Theorem 4.1(B), $\lambda(\kappa)>\lambda_0$ for all $\kappa>0$ and $\lambda$ is a bijection $(0,\infty)\to(\lambda_0,\infty)$. For $\lambda\le\lambda_0$, $G_\lambda'$ has no zero in $(0,1]$ and $G_\lambda'(1)<0$ (H2), so $G_\lambda$ is strictly decreasing and $0$ is the unique maximizer. For $\lambda>\lambda_0$ there is exactly one stationary $b_+\in(0,1)$; $G_\lambda''(0)>0$ (H6) and $G_\lambda'(1)<0$ give $G_\lambda'>0$ on $(0,b_+)$ and $<0$ on $(b_+,1]$; $b_+(\lambda)=b(\lambda^{-1}(\lambda))$ is continuous, increasing, tends to $0$ as $\lambda\downarrow\lambda_0$ and to $1$ as $\lambda\to\infty$. Then $R^2-\partial\tilde c(\lambda)=\{R^2\}$ for $\lambda\le\lambda_0$ and $\{R^2(1-b_+^2)\}$ for $\lambda>\lambda_0$, and the computation of (f) applies for every $0<D<R^2$. $\square$

**Corollary 6.2 ($\mathbb{CP}^{d-1}$).** For $(a,c)=(1,d)$, Theorem 6.1 is 68BH Theorem 5.1(a)–(e) and Corollary 5.2; with 68BH Theorem A (the 1D2Q envelope, resting on the Brazitikos–Pandis extremum), $\mathcal R=R_d$ is the two-piece rate–distortion function of 68BH Theorem 5.1(f). $\square$

**Remark 6.3 (what is proved, what must be imported).** Theorem 6.1 is a statement about the one-parameter problem $\max_b\{K(2\lambda b)-\lambda R^2b^2\}$ and its Legendre-type envelope, for which several first-order transitions are not excluded a priori [EE]. To read $\mathcal R$ as the rate–distortion function of a source with overlap law $\mathrm{Beta}(a,c-a)$ one needs, as in 68BH Section 2: (i) the fixed-norm spectral extremum, that the tilted normalizer at fixed report radius is maximized by the source-orbit direction (for $\mathbb{CP}^{d-1}$: Brazitikos–Pandis through 1D2Q Proposition A.1; for $\mathbb{RP}^{d-1}$, $\mathbb{HP}^{d-1}$ the analogous $\mathrm{Dirichlet}(\beta/2,\dots,\beta/2)$ statement is not in the corpus and is open); (ii) radiality of the tilted (posterior) mean at the maximizer (automatic for one-spike spectra); (iii) the Gibbs-dual envelope formula and attainment of active radii by covariant channels (1D2Q Theorem 2.1, 6XH6 eq. (4.3)). Given (i)–(iii), Theorem 6.1 yields the complete two-piece rate–distortion function, exactly as in 68BH Theorem 5.1(f). Nothing in Sections 3–5 depends on these imports.

## 7. Bessel family and real/quaternionic projective sources

Let $Z_c(\kappa):={}_0F_1(;c;\kappa^2/4)=\Gamma(c)(\kappa/2)^{1-c}I_{c-1}(\kappa)$, $c>0$ (DLMF 10.25.2). For $c>\tfrac12$, $Z_c(\kappa)=\mathbb E e^{\kappa Y}$ with $Y=2X-1$, $X\sim\mathrm{Beta}(c-\tfrac12,c-\tfrac12)$; for $c=\tfrac12$, $Z_{1/2}=\cosh\kappa$ ($Y=\pm1$); for $c=n/2$, $Y$ is a coordinate of the uniform law on $S^{n-1}$; for $c=n$, $Z_n$ is the normalizer of the phase-lifted $\mathbb{CP}^{n-1}$ coherent orbit (6XH6 Proposition 7.1 with $k=1$). Here $\mu=0$, $R^2=1$, $K=\log Z_c$, $m=Z_c'/Z_c$, $H_Z=m-\kappa m'$. From $zw''+cw'-w=0$ for $w={}_0F_1(;c;z)$ with $z=\kappa^2/4$:
$$\kappa Z_c''+(2c-1)Z_c'-\kappa Z_c=0,\qquad \kappa m'=\kappa(1-m^2)-(2c-1)m, \tag{7.1}$$
$$H_Z=\kappa(m^2-1)+2cm=(1-m^2)\big(\Psi_0(m)-\kappa\big),$$
with $\Psi_0(m)=2cm/(1-m^2)$ on $(0,1)$, and, on the curve $\kappa=\Psi_0(m)$, the denominator $\kappa(1-m^2)-(2c-1)m$ of $d\kappa/dm$ equals $m$, so
$$\Delta_0(m):=\Psi_0'(m)-\frac{\Psi_0(m)}{m}=\frac{4cm^2}{(1-m^2)^2}>0. \tag{7.2}$$
Also $H_Z(\kappa)=\kappa^3/(4c^2(c+1))+O(\kappa^5)>0$ near $0^+$ (`manuscript_checks.py`).

**Theorem 7.1 (no fold, $c\ge\tfrac12$).** For $c\ge\tfrac12$, $H_Z>0$ on $(0,\infty)$; the radial multiplier $\kappa/(2m(\kappa))$ increases strictly from $\lambda_0=c$ to $\infty$, and for $c>\tfrac12$ the complete radial phase and envelope are those of Theorem 6.1(II) under the full change of variables $(a_B,c_B)=(c-\tfrac12,2c-1)$, $\kappa_B=2\kappa_Z$, $\lambda_B=2\lambda_Z$, and $D_B=D_Z/2$: continuous onset, no coexistence.

*Proof.* For $c\ge\tfrac12$, $m=\mathbb E_\kappa Y\in(0,1)$ and $m'=\mathrm{Var}_\kappa Y>0$, so $\kappa(m)$ exists on $(0,1)$ and $D_0(m):=\Psi_0(m)-\kappa(m)$ has $D_0>0$ near $0^+$ and $D_0'=\Delta_0>0$ at any zero; a first zero would need $D_0'\le0$: there is none, so $H_Z>0$. The multiplier statement follows as in Theorem 4.1 ($\lambda_0=1/(2\mathrm{Var}Y)=c$). For $c>\tfrac12$, Kummer's second theorem (DLMF 13.6.9 with $\nu=c-1$) gives $Z_c(\kappa)=e^{-\kappa}{}_1F_1(c-\tfrac12;2c-1;2\kappa)$, i.e. $\log Z_c(\kappa)=K_{a',2a'}(2\kappa)$ with $a'=c-\tfrac12$ and $\mu'=\tfrac12$, whence $H_Z(\kappa)=2H_{a',2a'}(2\kappa)$ and $b_Z(\kappa)=b_{a',2a'}(2\kappa)$; this is the case $c'=2a'$ of Theorems 4.1(B) and 6.1(II). More explicitly, $R_Z^2=1$ whereas $R_B^2=1/2$, and $\lambda_B(2\kappa)=2\lambda_Z(\kappa)$. At fixed $b$, $G^Z_\lambda(b)=G^B_{2\lambda}(b)$, so $\tilde c_Z(\lambda)=\tilde c_B(2\lambda)$ and $\mathcal R_Z(D)=\mathcal R_B(D/2)$ for $0<D\le1$. The Beta onset $2c$ becomes the Bessel onset $c$. $\square$

**Proposition 7.2 ($0<c<\tfrac12$).** For $0<c<\tfrac12$, $H_Z>0$ on $(0,\infty)$ still holds, but $Z_c$ is not a moment generating function: $m(\kappa)$ exceeds $1$ for large $\kappa$ ($m=1+(1-2c)/(2\kappa)+O(\kappa^{-2})$; numerically $\max m=1.70$ for $c=0.1$), so "onset" and "radius" have no probabilistic meaning there.

*Proof.* $Z_c$ and $Z_c'$ have positive coefficients, so $m>0$. On the set $\{m<1\}$, (7.1) gives $\kappa m'=\kappa(1-m^2)+(1-2c)m>0$; at a point where $m=1$, $\kappa m'=1-2c>0$, so $m$ cannot cross $1$ downward and $\{m<1\}$ is an initial interval $(0,\kappa_1)$ ($\kappa_1\le\infty$). On it the argument of Theorem 7.1 applies verbatim (only $m'>0$, $m\in(0,1)$, $D_0>0$ near $0^+$ and (7.2) were used), so $H_Z>0$ there; on $[\kappa_1,\infty)$, $m\ge1$ and $H_Z=\kappa(m^2-1)+2cm>0$ trivially. The expansion of $m$ is DLMF 10.40.1. To exclude any probability MGF directly, its formal moments would give $\mathbb E Y^2=1/(2c)$ and $\mathbb E Y^4=3/(4c(c+1))$, hence $\operatorname{Var}(Y^2)=(2c-1)/(4c^2(c+1))<0$, a contradiction. $\square$

The restriction of Theorem 7.1 to $c\ge\tfrac12$ and the repair in Proposition 7.2 were requested by the adversarial review; all applications below have $c\ge1$.

**Corollary 7.3.** (i) *Spheres.* For $S^{n-1}\subset\mathbb R^n$, $n\ge2$ ($c=n/2$), the scalar radial problem has no fold: continuous onset at $\lambda_0=n/2$. Since $\mathbb E e^{\langle\kappa u,x\rangle}$ depends on $u$ only through $|u|$, the fixed-norm extremum (i) of Remark 6.3 is automatic, and the smooth curve is consistent with the Dytso–Cardone rate–distortion function [DC]; $n=3$ is 68BH Corollary 5.2. (ii) *Phase-lifted $\mathbb{CP}^{n-1}$ coherent states* (6XH6, $k=1$, $c=n$): the radial problem $\phi_s(b)=K(2sb)-sb^2$ of 6XH6 eq. (5.1) is the scalar problem with $(\mu,R^2)=(0,1)$, so 6XH6 Theorem 7.3(1) (negative fourth cumulant, continuous first activation) sharpens to the complete phase: no coexistence at any field. This source is the sphere $S^{2n-1}$ of (i). (iii) *Oriented two-planes in $\mathbb R^3$, $\mathbb R^4$* (7H9F, $q=1,2$): $L_1=\sinh\kappa/\kappa=Z_{3/2}(\kappa)$ and $L_2=Z_{3/2}(\kappa/2)^2$, so $H_{L_2}(\kappa)=H_{Z_{3/2}}(\kappa/2)$, and Theorem 7.1 gives a second proof of 7H9F Lemma 7.1 for $n=3,4$ (not for $n=5$). (iv) *The symmetric Beta case.* $c=2a$ is the Bessel family with $c'=a+\tfrac12$; in particular $\mathbb{RP}^1$, $\mathbb{CP}^1$, $\mathbb{HP}^1$ are $S^1$, $S^2$, $S^4$.

**Theorem 7.4 (rank-one sources over $\mathbb R$, $\mathbb C$, $\mathbb H$).** Let $\beta\in\{1,2,4\}$, $d\ge2$, and $(a,c)=(\beta/2,\beta d/2)$, the overlap law $|\langle x,u\rangle|^2$ of Haar unit vectors in $\mathbb F^d$. Then $\mu=1/d$, $R^2=1-1/d$, $\lambda_0=d(\beta d+2)/4$, and the scalar radial problem has exactly one fold iff $d\ge3$ (for all three fields), with $\kappa_f\ge(\beta d+2)(d-2)/d$ and $m_f\ge\tfrac12$; for $\beta\in\{2,4\}$ also $\kappa_f<\beta d(\beta+2)/4$ ($2d$ and $6d$); for $d=2$ the onset is continuous. Theorem 6.1 gives the complete radial phase in each case.

*Proof.* $|\langle x,u\rangle|^2$ is the ratio of a sum of $\beta$ squared real Gaussian coordinates to the sum of $\beta d$, hence $\mathrm{Beta}(\beta/2,\beta(d-1)/2)$; $c-2a=\beta(d-2)/2$; apply Theorems 4.1, 5.1 ($a=\beta/2\ge1$ iff $\beta\ge2$) and 6.1. $\square$

For $\beta=2$ this is 68BH; the real $d=3$ case already occurs in the Maier--Saupe analysis of Fatkullin--Slastikov [FS], Theorem 3 and Section 3.1, with $\kappa=-3r$ and $\lambda=1/(2\tau)$. The present contribution is the common arbitrary-$(a,c)$ criterion; no blanket priority claim is made for real or quaternionic special cases, and the rate–distortion reading awaits the extremum (i) of Remark 6.3.

## 8. The oriented-two-plane normalizer

Let $q\ge1$, $E(\kappa)=M_{q+1}(\kappa)={}_1F_1(1;q+1;\kappa)$, $O(\kappa)=E(-\kappa)$, $L_q=(E+O)/2$, $S=(E-O)/2$. Then $L_q(\kappa)=q!\sum_j\kappa^{2j}/(q+2j)!={}_1F_2(1;\tfrac{q+1}2,\tfrac{q+2}2;\kappa^2/4)=\mathbb E\cosh(\kappa T)$, $T\sim\mathrm{Beta}(1,q)$, the normalizer of Haar oriented two-planes in $\mathbb R^{q+2}$ (7H9F eqs. (11), (24)); $K_q=\log L_q$, $m_q=K_q'$, $H_q=m_q-\kappa m_q'$, $J_q=L_q^2H_q$ (7H9F eq. (25)), and 7H9F's multiplier is $\lambda_q=\kappa/(2m_q)$, i.e. $\mu=0$, $R^2=1$.

**Proposition 8.1 (exact structure).** (i) $\kappa L_q'=\kappa S-qL_q+q$ and $\kappa S'=\kappa L_q-qS$ (68BH Lemma 3.1 at $\pm\kappa$). (ii) $L_q$ satisfies the inhomogeneous second-order equation $\kappa^2L''+2q\kappa L'-(\kappa^2-q(q-1))L-q(q-1)=0$ (homogeneous only for $q=1$) and the homogeneous third-order equation
$$\kappa^2L'''+(2q+2)\kappa L''+\big(q(q+1)-\kappa^2\big)L'-2\kappa L=0. \tag{8.1}$$
(iii) In the variables $(s,u)=(S/L,1/L)$, $u^2\kappa J_q=-\kappa^2(1-s^2)+\kappa s(1+2qu)-q(1-u)(qu+2)$ with $\kappa s'=\kappa(1-s^2)-qsu$, $\kappa u'=-u(\kappa s+qu-q)$: the sign of $H_q$ depends on the three-dimensional state $(s,u,\kappa)$, equivalently $(m,m',\kappa)$, and this general-$q$ reduction does not supply a closed first-order Riccati equation for $m_q$. No minimal-order or nonexistence claim is made. Indeed the exceptional cases obey $m_1'=1-m_1^2-2m_1/\kappa$ and $m_2'=(1-m_2^2)/2-2m_2/\kappa$. (iv) Along the trajectory,
$$H_q'+\Big(3m_q+\frac{2q+2}{\kappa}\Big)H_q=\Delta_q(m_q,\kappa), \tag{8.2}$$
$$\Delta_q(m,\kappa):=-\kappa m(1-m^2)+(2q+5)m^2-2+\frac{(q+1)(q+2)m}{\kappa},$$
equivalently $\big(\kappa^{2q+2}L_q^3H_q\big)'=\kappa^{2q+2}L_q^3\,\Delta_q(m_q(\kappa),\kappa)$. Hence, if $\kappa\mapsto\Delta_q(m_q(\kappa),\kappa)$ is negative on $(0,\kappa_\Delta)$ and positive on $(\kappa_\Delta,\infty)$, then $H_q$ has exactly one positive zero, located after $\kappa_\Delta$.

*Proof.* (i) is linear algebra on $\kappa E'=(\kappa-q)E+q$ and $\kappa O'=q-(\kappa+q)O$; eliminating $S$ gives (ii), and differentiating removes the constant. (iii) is substitution. (iv): with $L''/L=m'+m^2$, $L'''/L=m''+3mm'+m^3$, (8.1) expresses $m''$ through $(m,m',\kappa)$; inserting it into $H_q'=-\kappa m''$ gives (8.2), and $(\kappa^{2q+2}L^3)'/(\kappa^{2q+2}L^3)=3m+(2q+2)/\kappa$. All identities are checked with symbolic $q$ in `sym_evenpart.py`, `sym_evenpart_ode.py`, `manuscript_checks.py`. For the last claim, $W:=\kappa^{2q+2}L_q^3H_q$ has $W(0^+)=0$ ($H_q=O(\kappa^3)$), decreases then increases, and $W\to+\infty$ since $H_q\to1$. $\square$

**Proposition 8.2 (exact small-field signs; found and verified in review).** Along the trajectory, $\Delta_q(m_q(\kappa),\kappa)$ and $H_q$ are even and odd in $\kappa$ respectively, with
$$[\kappa^0]\Delta_q=0,\qquad [\kappa^2]\Delta_q=-\frac{4(2q+5)(q^2-q-8)}{(q+1)^2(q+2)^2(q+3)(q+4)}, \tag{8.3}$$
$$[\kappa^1]H_q=0,\qquad [\kappa^3]H_q=-\frac{4(q^2-q-8)}{(q+1)^2(q+2)^2(q+3)(q+4)}.$$
Since $q^2-q-8<0$ for $q\le3$ and $>0$ for $q\ge4$, both $\Delta_q$ and $H_q$ are positive near $0^+$ for $q\le3$ and negative for $q\ge4$.

*Proof.* Series substitution in (8.2) (`manuscript_checks.py`, `reviewer/rev_last.py`). $\square$

*Numerical evidence* (`scan_evenpart.py`, `checks_bounds.py`; independently reproduced in review with a 4500-point grid). For $q=1,2,3$: $\Delta_q>0$ on the whole grid and $H_q$ has no zero (consistent with 7H9F Theorem 7.2). For $4\le q\le60$: $\Delta_q$ changes sign exactly once, at $\kappa_\Delta$ slightly below the fold; $H_q$ and $F_q$ have exactly one zero each. Values: $q=4$: $\kappa_f=4.415714051$, $\kappa_c=5.541056361$ (the values printed in 61Y0 Section 6, whose normalizer $12(2\cosh\kappa-2-\kappa^2)/\kappa^4$ equals $L_4$; checked), $\kappa_\Delta=4.1619$; $q=5$: $\kappa_f=7.61354$, $\kappa_\Delta=7.2901$; $q=10$: $\kappa_f=19.37353$, $\kappa_\Delta=18.9911$; $q=30$: $\kappa_f=59.99529$, $\kappa_\Delta=59.5975$; $q=60$: $\kappa_f=119.9999987$. The identity (8.2) holds at the located folds to $6\cdot10^{-26}$.

*What remains open.* The single sign change of $\Delta_q$ along the trajectory is numerical. At the fold the $O(q)$ terms of $\Delta_q$ cancel and $\Delta_q(m_f,\kappa_f)=O(1)$, so no crude bound on $m_q(\kappa)$ certifies the sign change; a proof along this route needs $m_q$ to $O(1/q)$ accuracy near $\kappa\approx2q$. The displayed general-$q$ reduction has not established the single sign change required to adapt Section 4; this is a limitation of the present method, not an impossibility theorem. We therefore claim no new proof of 7H9F Theorem 8.2 or Theorem 9.1 ($n\ge6$); what the present method recovers of 7H9F is $n=3,4$ (Corollary 7.3(iii)). A further numerical observation: the tilted variance $V_q=K_q''$ is unimodal on the grid for $q\ge4$ and decreasing for $q=3$; since $H_q=\kappa(\bar V_q-V_q)$ with $\bar V_q(\kappa)=\kappa^{-1}\int_0^\kappa V_q$ the running mean, unimodality of $V$ is a sufficient condition for one fold (and monotone decrease for none), unproved for $L_q$. Not covered by any result here: 7H9F for $q\ge3$, Slater orbits with $k\ge2$ (${}_{k-1}F_k$), coherent orbits with $p\ge2$ (${}_pF_{p+1}$, 6XH6/6DJ3) and Grassmann rank $r\ge2$ (matrix-argument ${}_1F_1$, 68BH open question 1); there the coefficient methods of 61Y0 Lemma 6.1 and 7H9F Theorem 8.2 remain the only proofs.

## 9. Numerical verification

`scan_ac.py` (mpmath, 30 digits) counts the positive zeros of $H$ and $F$ on a 301-point geometric $\kappa$-grid up to $15c+50$ with bisection to $10^{-25}$, for $a\in\{\tfrac12,1,\tfrac32,2,3,5\}$, $c\in(a,a+60]$ in steps of $\tfrac12$ plus the boundary values $c=2a-\tfrac12,2a-\tfrac1{10},2a,2a+10^{-3},2a+10^{-2},2a+\tfrac1{10}$ (744 pairs): the counts are $1,1$ for every $c>2a$ and $0,0$ for every $c\le2a$, never more; $\kappa_f<\kappa_c$, $m_f\ge\tfrac12$ and $\kappa_f\ge2(c+1)(c-2a)/c$ hold in every fold case; $m$ computed through the Kummer derivatives ${}_1F_1(a+1;c+1;\cdot)$, ${}_1F_1(a+2;c+2;\cdot)$ and through the Riccati equation (3.1) agree to $\le10^{-24}$ relative. The adversarial review reproduced this on an independent grid ($a\in\{0.3,0.7,1,2.5,4\}$, $c-2a\in\{-1,-0.1,0.1,1,10,40\}$) with the same outcome. `tables_ac.py` (40 digits, 200-step bisection, Kummer-derivative route only) produces the tables below and asserts every proved relation of Theorems 4.1, 5.1 and 6.1 in each row.

Table 1: the fold and the bounds of Theorems 4.1 and 5.1 ($\kappa_1=2(c+1)(c-2a)/c$; the columns $c(a+1)$ and $m_u$ apply for $a\ge1$ only).

| $(a,c)$ | source | $\kappa_1$ | $\kappa_f$ | $c(a+1)$ | $m_f$ | $m_u$ | $\lambda_{\min}$ |
|-----------|---------|-----------|---------------|---------|----------|----------|---------------|
| $(1/2,3/2)$ | $\mathbb{RP}^2$ | 1.66667 | 2.178287975 | – | 0.549065 | – | 3.365743198 |
| $(1/2,2)$ | | 3 | 3.879009872 | – | 0.567380 | – | 4.583233767 |
| $(1/2,5)$ | $\mathbb{RP}^9$ | 9.6 | 11.62828791 | – | 0.573922 | – | 11.04133789 |
| $(1,3)$ | $\mathbb{CP}^2$ | 2.66667 | 3.232708836 | 6 | 0.534420 | 0.666667 | 5.358728277 |
| $(1,5)$ | $\mathbb{CP}^4$ | 7.2 | 8.431550876 | 10 | 0.548068 | 0.6 | 9.689551191 |
| $(1,17)$ | $\mathbb{CP}^{16}$ | 31.7647 | 33.90710030 | 34 | 0.528252 | 0.529412 | 33.99087521 |
| $(2,6)$ | $\mathbb{HP}^2$ | 4.66667 | 5.277112966 | 18 | 0.521455 | 0.777778 | 9.350549631 |
| $(3,9)$ | | 6.66667 | 7.295434543 | 36 | 0.515543 | 0.833333 | 13.34623024 |
| $(5,65)$ | | 111.692 | 113.4549685 | 390 | 0.506602 | 0.846154 | 121.8673998 |
| $(1,2.001)$ | | 0.0029995 | 0.0037492 | 4.002 | 0.500062 | 0.749875 | 3.002499797 |

Table 2: the contact ($D_c/R^2=1-b_c^2$; $R_c=\lambda_cR^2b_c^2$).

| $(a,c)$ | $\kappa_c$ | $b_c$ | $\lambda_c$ | $\lambda_0$ | $D_c/R^2$ | $R_c$ |
|-----------|---------------|----------|---------------|---------|----------|----------|
| $(1/2,3/2)$ | 2.922626590 | 0.429029 | 3.406094244 | 3.75 | 0.815934 | 0.417964 |
| $(1/2,2)$ | 5.258427922 | 0.557080 | 4.719631691 | 6 | 0.689662 | 1.098513 |
| $(1/2,5)$ | 16.75539491 | 0.686037 | 12.21173305 | 30 | 0.529354 | 5.172667 |
| $(1,3)$ | 4.344285303 | 0.400332 | 5.425859459 | 6 | 0.839735 | 0.579718 |
| $(1,5)$ | 11.64408805 | 0.573491 | 10.15193548 | 15 | 0.671108 | 2.671112 |
| $(1,17)$ | 52.47145152 | 0.676014 | 38.80942424 | 153 | 0.543005 | 16.69245 |
| $(2,6)$ | 7.106601272 | 0.375200 | 9.470425005 | 10.5 | 0.859225 | 0.888798 |
| $(3,9)$ | 9.837403413 | 0.363856 | 13.51826860 | 15 | 0.867609 | 1.193132 |

Table 3: no fold for $c\le2a$ (the minimum of $H$ is taken on the grid, which starts at $\kappa=10^{-3}$ where $H\sim\kappa^3$).

| $(a,c)$ | source | zeros of $H$ | zeros of $F$ | $\min H$ | $\lambda_0$ |
|---|---|---|---|---|---|
| $(1,2)$ | $S^2$ | 0 | 0 | $2.8\cdot10^{-12}$ | 3 |
| $(2,4)$ | $S^4$ | 0 | 0 | $7.1\cdot10^{-13}$ | 5 |
| $(1/2,1)$ | $S^1$ | 0 | 0 | $7.8\cdot10^{-12}$ | 2 |
| $(3/10,3/5)$ | | 0 | 0 | $1.4\cdot10^{-11}$ | 1.6 |

Table 4: the upper bound $\kappa_f<c(a+1)$ of Theorem 5.1 for $a<1$, where it is not proved: violated in three of the four cases.

| $(a,c)$ | $\kappa_f$ | $c(a+1)$ | ratio |
|---|---|---|---|
| $(1/4,1)$ | 2.8008995 | 1.25 | 2.2407 |
| $(1/2,2)$ | 3.8790099 | 3 | 1.2930 |
| $(1/2,10)$ | 22.328044 | 15 | 1.4885 |
| $(3/4,3)$ | 4.9219982 | 5.25 | 0.9375 |

The $(1,3)$ row reproduces 68BH Tables 1–3 ($\kappa_f=3.2327088363$, $\kappa_c=4.3442853031$, $\lambda_c=5.42585945949$); the $q=4$ even-part values of Section 8 reproduce 61Y0.

## 10. Open questions

1. A proof that $\Delta_q(m_q(\kappa),\kappa)$ changes sign once (Section 8), or a three-dimensional transversality argument in $(s,u,\kappa)$ for the quadratic-in-$\kappa$ sign function of Proposition 8.1(iii); either would give a second proof of 7H9F Theorem 8.2 for $q\ge4$.
2. An upper bound on $\kappa_f$ for $a<1$ (real projective spaces), where (5.2) is unavailable.
3. The $\mathrm{Dirichlet}(\beta/2,\dots,\beta/2)$ fixed-norm extremum (real and quaternionic analogue of Brazitikos–Pandis) needed to turn Theorem 7.4 into rate–distortion functions for $\mathbb{RP}^{d-1}$, $\mathbb{HP}^{d-1}$.
4. Whether the tilted variance $\mathrm{Var}_\kappa X$ is unimodal in $\kappa$ for every ${}_1F_1(a;c)$ with $c>2a$ (an alternative proof of Theorem 4.1 and a natural conjecture for ${}_pF_{p+1}$ normalizers).
5. Whether "one fold iff right-skewed" persists for matrix-argument ${}_1F_1$ (68BH open question 1).

## 11. Reproducibility

All scripts are in `repro/` next to this file (Python 3.12.6, sympy 1.14.0, mpmath 1.3.0; `python run_all.py` runs everything, writes `<name>.out` and `runtimes.txt`, and fails on any assertion; `--fast` skips the four slow scripts). The original scripts and their supplied outputs remain preserved in the original delivery. This candidate corrects the even-part sign in `sym_riccati.py`, makes the geometric-plus-linear grids execute as intended, and adds normalization/scaling checks; the four reviewer scripts are in `repro/reviewer/`; `manuscript_checks.py` and `tables_ac.py` were written for this manuscript.

| script | certifies | arithmetic | time |
|------------------------|----------------------------------------------|--------------|------|
| `sym_riccati.py` | (3.1)–(3.2), identities (a)–(d), $\Psi(\tfrac12)$, small-$\kappa$ coefficients (3.3), the ${}_0F_1$ reduction (7.1)–(7.2), the $(L,S)$ system | sympy exact | 33 s |
| `sym_evenpart.py` | Proposition 8.1(i),(iii); small-$\kappa$ order of $\kappa J_q$ | sympy exact | 2 s |
| `sym_evenpart_ode.py` | Proposition 8.1(ii),(iv) with symbolic $q$ | sympy exact | 2 s |
| `manuscript_checks.py` | 47 named symbolic checks of selected identities and finite Taylor coefficients, plus the candidate correction checks; including (5.2)'s integrand, Kummer's second theorem to $O(\kappa^{10})$, (8.3), $L_4$ = the 61Y0 normalizer | sympy exact | 153 s |
| `scan_evenpart.py` | zero counts of $H_q$, $F_q$ for $q\le20,25,30,40,50,60$; (8.2) at the folds | mpmath 30 digits | 4 s |
| `checks_bounds.py` | $\kappa(1-m)<c-a$ for $a\ge1$ and its failure for $a<1$; (5.2) numerically; sign changes of $\Delta_q$ (`delta_signchanges.json`); unimodality of $V_q$ | mpmath 30 digits | 24 s |
| `scan_ac.py` | the 744-pair scan of Section 9 (`scan_ac.json`, `scan_ac.out`) | mpmath 30 digits | 146 s |
| `tables_ac.py` | Tables 1–4 and the asserted relations | mpmath 40 digits | 160 s |
| `reviewer/rev_*.py` (four scripts) | the reviewer's independent re-derivations: symbolic identities (`rev_sym`), independent $(a,c)$ grid (`rev_num`), $L_q$ ODEs and sign changes (`rev_even`), (8.3) and the ${}_0F_1$ small-$c$ behaviour (`rev_last`) | sympy; mpmath 30 digits | 34, 90, 30, 99 s |

The timings above describe supplied historical runs. The 744-case scan described in Section 9 used the original 301-point geometric grid: its intended linear extension was empty. The corrected scripts now expose actual grid sizes; the new bounded corrected-grid run and its precise coverage are recorded in `candidate_checks.json`. Numerical scripts are diagnostic except where explicit assertions enforce their tested predicates; exit status alone does not prove a global sign law. Finite Taylor matches are not exact functional identities.

No proof step depends on floating point: Theorems 3.1, 4.1, 5.1, 6.1, 7.1, 7.4 and Propositions 7.2, 8.1, 8.2 use only the rational identities listed, with selected algebraic steps and Taylor coefficients checked by the listed programs, and the cited DLMF expansions.

## AI-assistance statement

The author reports that the original manuscript, derivations, code and numerical checks were produced by Claude Fable 5.1 agents (Anthropic) working under the author's direction, in two roles: an author agent (report of 2026-09-12) and an independent adversarial review agent (review of 2026-09-13), whose findings (the range $c\ge\tfrac12$ in Theorem 7.1, Proposition 7.2, Proposition 8.2, the independent numerical grid) are incorporated with attribution. The attributions to 61Y0 and 6XH6 were checked against the deposited records during preparation of this manuscript. No human peer review has taken place; numerical checks support only their tested instances. On 14 September 2026, fresh local OpenAI gpt-6-astra High and gpt-5.6-sol Medium preassessments examined the supplied exact PDF. Astra identified the normalization, exceptional Riccati, scaling, source-grid and novelty corrections; Sol identified the Proposition 5.2 wording and table-caption mismatch. Codex applied these in this separate candidate and reran the affected checks. These local preassessments are not private-intake reports or human editorial decisions. The original Fable identity and execution are author-supplied provenance. Scientific responsibility rests with the author.

## References

[68BH] L. Eriksson, *One Fold, Unique Contact and the Complete Two-Piece Rate–Distortion Function of Rank-One Complex-Projective Born Prediction*, ARR-2026-68BH5JDJCQ8XW8GT, revision v004, 2026-09-09.

[1D2Q] L. Eriksson, *Exact Rate–Distortion Theory for Complex-Projective Born Prediction: Finite-Dimensional Bingham Frontiers, Thermodynamic Coexistence, and Worst-State Capacity*, ARR-2026-1D2QYXPCVY9H7ANB, v1, 2026-08-13.

[61Y0] L. Eriksson, *Complete Rank-Two Born-Prediction Rate–Distortion on $\mathrm{Gr}_{\mathbb C}(2,4)$: All-Field Matrix–Bingham Rigidity and a Unique Coexistence Transition*, ARR-2026-61Y0FFA39M8KMBJ5, v1, 2026-08-13.

[7H9F] L. Eriksson, *Complete Rate–Distortion Phase Diagram of Haar Oriented Two-Planes: One-Change Hypergeometric Coefficients, Unique Coexistence, and No Reentrance*, ARR-2026-7H9FAPTBZA897AMJ, v2, 2026-08-14.

[6XH6] L. Eriksson, *Exact Classical Rate–Distortion for Phase-Lifted Generalized Coherent States: Cartan-Product Laplace Rigidity, Universal Radial Envelopes, and Slater-Determinant Transitions*, ARR-2026-6XH6JAS5ZA934A6J, v1, 2026-08-14.

[6DJ3] L. Eriksson, *Universal Semiclassical Coexistence in Classical Compression of Phase-Lifted Coherent States: Dimension-Normalized Contacts and a Matched High-Fidelity Boundary Layer*, ARR-2026-6DJ302B1G38V4SHD, v1, 2026-08-14.

[DLMF13] NIST Digital Library of Mathematical Functions, Chapter 13 (Confluent Hypergeometric Functions): §13.2 (eq. 13.2.1, Kummer's equation; 13.2.2), §13.4 (eq. 13.4.1, integral representation), §13.6 (eq. 13.6.9, Kummer's second theorem), §13.7 (eq. 13.7.1, large-argument expansion); Chapter 10, eqs. 10.25.2 and 10.40.1. https://dlmf.nist.gov/.

[Ince] E. L. Ince, *Ordinary Differential Equations*, Dover, New York, 1956, Chapter II (the Riccati equation and its linearization).

[DC] A. Dytso and M. Cardone, *Uniform Distribution on $(n-1)$-Sphere: Rate-Distortion under Squared Error Distortion*, arXiv:2401.04248 [cs.IT], 2024.

[EE] T. Eisele and R. S. Ellis, *Multiple phase transitions in the generalized Curie–Weiss model*, J. Stat. Phys. 52 (1988), 161–202.

[B] C. Bingham, *An antipodally symmetric distribution on the sphere*, Ann. Statist. 2 (1974), 1201–1225.

[K] J. T. Kent, *The complex Bingham distribution and shape analysis*, J. Roy. Statist. Soc. Ser. B 56 (1994), 285–299.

[KS] D. Karp and S. M. Sitnik, *Log-convexity and log-concavity of hypergeometric-like functions*, J. Math. Anal. Appl. 364 (2010), 384–394.

[KK] S. I. Kalmykov and D. B. Karp, *Log-convexity and log-concavity for series in gamma ratios and applications*, arXiv:1211.2882 [math.CA], 2012.

[FS] I. Fatkullin and V. Slastikov, *Critical points of the Onsager functional on a sphere*, preprint, 12 January 2005, Theorem 3 and Section 3.1. https://www.math.cmu.edu/CNA/Publications/publications2005/005abs/05-CNA-005.pdf
