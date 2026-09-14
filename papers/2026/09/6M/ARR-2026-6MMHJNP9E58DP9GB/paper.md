# One Fold for Haar Oriented Two-Planes in Every Dimension n ≥ 6: A Phase-Space Proof through a Fano Factor, an Integrating Factor and the Threshold $L_q=q(q-1)/8$

**Lluis Eriksson** (Independent researcher)

## Abstract

Let $L_q(\kappa)=q!\sum_{j\ge0}\kappa^{2j}/(q+2j)!$, $q=n-2$, be the normalizer of Haar oriented two-planes in $\mathbb R^n$, $m_q=L_q'/L_q$, and $H_q=m_q-\kappa m_q'$ the fold numerator of the stationary multiplier $\lambda_q=\kappa/(2m_q)$. The record ARR-2026-7H9FAPTBZA897AMJ proved that $H_q$ has exactly one positive zero for every $q\ge4$ through a one-change law for the coefficients of $L_q^2H_q$. We give a short independent proof by a different method: in the coordinates $(X,u)=(\kappa m_q,1/L_q)$ the inhomogeneous second-order equation of $L_q$ makes $\kappa H_q$ a polynomial, the transversality of a crossing is a second polynomial $T$, and $Q=T-(q-\tfrac12)\kappa H_q$ obeys a first-order linear equation whose forcing, on the zero set of $H_q$, changes sign exactly where $L_q=q(q-1)/8$. An integrating factor then excludes a zero before that point and a second zero after the first. Probabilistically, $\kappa H_q=4(\mathbb EJ-\operatorname{Var}J)$ for the index law of the series. The same argument gives no fold for $q=2,3$. A now redundant interval-arithmetic certificate and numerics are included.

## 1. Introduction

**Antecedents.** For a Haar oriented two-plane in $\mathbb R^n$ with signed Plücker coordinate $W=x\wedge y$, the record ARR-2026-7H9FAPTBZA897AMJ (below 7H9F) reduced the unrestricted Shannon rate–distortion function under squared ambient loss to a one-dimensional radial problem whose normalizer is
$$L_q(\kappa)=q!\sum_{j\ge0}\frac{\kappa^{2j}}{(q+2j)!}=(n-2)\int_0^1\cosh(\kappa x)(1-x)^{n-3}\,dx,\qquad q=n-2$$
(7H9F eqs. (11), (24)). Its complete phase diagram rests on one analytic fact: the stationary multiplier $\lambda_q(\kappa)=\kappa/(2m_q(\kappa))$, $m_q=L_q'/L_q$, has exactly one fold, i.e. the fold numerator $H_q=m_q-\kappa m_q'$ has exactly one positive zero. 7H9F proved this for every $q\ge4$ ($n\ge6$) as a consequence of its Theorem 8.2, the *one-change law*: writing $J_q=L_q^2H_q=\sum_r c_{q,r}\kappa^{2r-1}$, the coefficients satisfy $c_{q,r}<0$ for $2\le r<q$ and $c_{q,r}>0$ for $r\ge q$ (with $c_{4,3}=0$), proved by a likelihood-ratio ordering of a parity-truncated central binomial law and an exact tail estimate; the sign pattern of $H_q$ then follows because $y^{-q}\sum_rc_{q,r}y^r$ ($y=\kappa^2$) is strictly increasing from $-\infty$ to $+\infty$. The cases $n=3,4,5$ ($q=1,2,3$) are 7H9F Lemma 7.1, where $H_q>0$ on $(0,\infty)$ by explicit series of elementary functions. 7H9F Theorem 9.1 turns the one-zero statement into the complete high-dimensional phase: unique coexistence multiplier, one positive active radius above it, no later exchange or reentrance.

Two related records use a different tool. The published complex-projective one-fold paper ARR-2026-68BH5JDJCQ8XW8GT (below 68BH) proved one fold for ${}_1F_1(1;d;\kappa)$, $d\ge3$, from the first-order inhomogeneous equation $\kappa M'=(\kappa-d+1)M+(d-1)$ and a transversality argument in the plane $(M,\kappa)$; the unpublished manuscript [B3] extended this to ${}_1F_1(a;c;\kappa)$ by a Riccati reduction to the plane $(m,\kappa)$ and proved "one fold iff $c>2a$". For the oriented-two-plane normalizer, which satisfies a homogeneous *third-order* equation, [B3] Section 8 obtained only an exact identity, $H_q'+(3m_q+(2q+2)/\kappa)H_q=\Delta_q$, with an explicit $\Delta_q(m_q,\kappa)$, and numerics; it recorded the obstruction that at the fold the $O(q)$ terms of $\Delta_q$ cancel, so that no crude estimate of $m_q$ decides the sign, and left a second proof of 7H9F Theorem 8.2 as its first open question. The record ARR-2026-61Y0FFA39M8KMBJ5 (below 61Y0) treats $\mathrm{Gr}_{\mathbb C}(2,4)$, whose normalizer equals $L_4$, by a coefficient method and gives the numerical values at $q=4$ used in Section 7.

**Contribution.** We prove the one-zero statement of 7H9F Theorem 8.2 for every $q\ge4$ by a phase-space argument that uses no coefficient sign, no estimate of $m_q$ or $L_q$, and no numerical evaluation or a priori estimate at the unknown fold (Theorem 4.1). The ingredients are: (i) the inhomogeneous second-order equation (E2) of $L_q$, which descends from 68BH's first-order equation for ${}_1F_1(1;q+1;\kappa)$ because $L_q$ is its even part; (ii) the coordinates $(X,u)=(\kappa m_q,1/L_q)$, in which $\kappa H_q$ and the transversality of a crossing of $H_q=0$ are polynomials $h$ and $T$ (identities (C1)–(C6), all machine-checked with symbolic $q$); (iii) the function $Q=T-(q-\tfrac12)h$, which satisfies a first-order linear inhomogeneous equation $\dot Q+cQ=g+hB$ with $g=X^2(8-q(q-1)u)$, $B\ge0$ (Lemma 3.3); and (iv) the integrating factor $\kappa^{c}$, which shows that $H_q$ cannot reach $0$ from below while $L_q\le q(q-1)/8$ and cannot return to $0$ from above once $L_q>q(q-1)/8$. Probabilistically (Proposition 3.4), $\kappa H_q=4(\mathbb EJ-\operatorname{Var}J)$ for the index law $P(J=j)\propto\kappa^{2j}/(q+1)_{2j}$, so the fold is where the Fano factor of that law crosses $1$, and the threshold $L_q=q(q-1)/8$ is a condition on the boundary atom of a parity-conditioned Poisson law. The same argument with $c=2$, $\tfrac52$ recovers 7H9F Lemma 7.1 for $n=4,5$ (Corollary 5.1). We do **not** reprove the coefficient law $c_{q,r}\lessgtr0$ itself; what is reproved is its consequence, which is all that 7H9F Theorem 9.1 uses (Corollary 4.5). An auxiliary interval-arithmetic certificate of the pre-threshold sign for $4\le q\le200$ (Section 6), written before Step 1 of the proof was found, is retained as a redundant computational check with its historical floating-point control limitation stated explicitly.

**Status.** Theorem 4.1 and Corollary 5.1 are proved; every identity of Section 3 is a short hand computation verified with symbolic $q$ by the author's and, independently, the reviewer's scripts. An adversarial review re-derived every step and found no gap; its corrections (a bibliographic slip on modified Struve and Lommel functions, the transcription of one table entry, the wording of two remarks and of the claim of independence) are incorporated. Literature searches (Section 9) found no prior Lyapunov-type argument for the sign of $K'-\kappa K''$ of a hypergeometric normalizer; a null search does not certify priority.

## 2. Setting

Throughout $q\ge1$ is an integer, $\kappa>0$, $z=\kappa^2$, and
$$L_q(\kappa)=\sum_{j\ge0}w_j\kappa^{2j},\qquad w_j=\frac{q!}{(q+2j)!}=\frac1{(q+1)_{2j}},\qquad K_q=\log L_q,\quad m_q=K_q',\quad H_q=m_q-\kappa m_q'. \tag{2.1}$$
$L_q$ is entire, even, with positive coefficients, $L_q(0)=1$, strictly increasing to $+\infty$ on $[0,\infty)$; $L_q={}_1F_2(1;\tfrac{q+1}2,\tfrac{q+2}2;\kappa^2/4)$. In Gaunt's normalized notation [Ga],
$$L_q(\kappa)=\Gamma\!\left(\frac{q+1}{2}\right)\Gamma\!\left(\frac{q+2}{2}\right)\left(\frac{2}{\kappa}\right)^{q-1/2}\widetilde t_{q-3/2,\,1/2}(\kappa),$$
so it is a power-rescaled normalized modified Lommel function of the first kind. For $q=1,2$ the corresponding normalized Lommel functions are first-kind modified Struve functions (using symmetry in the second parameter when $q=1$); thus $L_1=\sinh\kappa/\kappa$ and both cases are likewise power-rescaled Struve functions [BP1,Ga]. The radial problem of 7H9F (its Sections 6–9) is $\max_{0\le b\le1}\{K_q(2\lambda b)-\lambda b^2\}$; a positive stationary radius satisfies $b=m_q(\kappa)$, $\lambda=\lambda_q(\kappa):=\kappa/(2m_q(\kappa))$, and (7H9F eqs. (22), (29))
$$\lambda_q'(\kappa)=\frac{H_q(\kappa)}{2m_q(\kappa)^2},\qquad F_q:=2K_q-\kappa m_q,\qquad F_q'=H_q. \tag{2.2}$$
A *fold* of $\lambda_q$ is a zero of $H_q$; 7H9F's phase diagram uses only the sign pattern of $H_q$ (Corollary 4.5). We use the closed form $L_q=q!\,\kappa^{-q}C_q(\kappa)$ with $C_q(\kappa):=\sum_{k\ge q,\ k\equiv q\ (2)}\kappa^k/k!$, so that $C_q'=C_{q-1}$ and, for $q\ge2$, $C_{q-2}=C_q+\kappa^{q-2}/(q-2)!$; $C_q$ is $\cosh\kappa$ or $\sinh\kappa$ minus a polynomial of degree at most $q-2$, hence $C_q=\tfrac12e^\kappa\,(1+O(\kappa^{q-2}e^{-\kappa}))$.

**Phase-space variables.** With $\tau=\log\kappa$ and $\dot f:=df/d\tau=\kappa f'$,
$$u:=\frac1{L_q}\in(0,1),\qquad X:=\kappa m_q>0,\qquad h:=\kappa H_q,\qquad c:=q-\tfrac12. \tag{2.3}$$

**Lemma 2.1 (elementary facts).** (F1) $H_q=\gamma_q\kappa^3+O(\kappa^5)$ with $\gamma_q=-4(q^2-q-8)/\big((q+1)^2(q+2)^2(q+3)(q+4)\big)$; so $H_q<0$ near $0^+$ for $q\ge4$ and $H_q>0$ near $0^+$ for $q\le3$. (F2) $H_q\to1$ as $\kappa\to\infty$. (F3) $X>0$ for $\kappa>0$; $u$ is a strictly decreasing bijection of $(0,\infty)$ onto $(0,1)$. Hence for $q\ge4$ there is a unique $\kappa_L>0$ with
$$u(\kappa_L)=u_*:=\frac8{q(q-1)}<1,\quad\text{i.e.}\quad L_q(\kappa_L)=\frac{q(q-1)}8, \tag{2.4}$$
and $u>u_*$ on $(0,\kappa_L)$, $u<u_*$ on $(\kappa_L,\infty)$. (F4) $X\to0$, $u\to1$, $h\to0$ and $T\to0$ (with $T$ from (C3)) as $\kappa\to0^+$.

*Proof.* (F1) is series substitution (`sym_reduction.py`, `rev_sym.py`); the coefficients of $\kappa^0,\kappa^1,\kappa^2$ vanish. (F2): $m_q=C_{q-1}/C_q-q/\kappa$; put $\rho=C_{q-1}/C_q=1+O(\kappa^{q-2}e^{-\kappa})$. Then $\rho'=C_{q-2}/C_q-\rho^2=1-\rho^2+\kappa^{q-2}/((q-2)!\,C_q)$ and
$$\kappa m_q'=\kappa(1-\rho^2)+\frac{\kappa^{q-1}}{(q-2)!\,C_q}+\frac q\kappa\longrightarrow0,$$
so $H_q=m_q-\kappa m_q'\to1$ (for $q=1$ use $L_1=\sinh\kappa/\kappa$ directly). (F3): $L_q'$ has positive coefficients; $L_q$ increases strictly from $1$ to $\infty$; $q(q-1)/8>1$ iff $q\ge4$. (F4) is immediate from $m_q=O(\kappa)$ and $u\to1$. $\square$

## 3. The reduction

**Proposition 3.1 (the inhomogeneous second-order equation).** For every $q\ge1$,
$$\kappa^2L_q''+2q\kappa L_q'-\big(\kappa^2-q(q-1)\big)L_q-q(q-1)=0. \tag{E2}$$

*Proof.* The coefficient of $\kappa^{2j}$, $j\ge1$, on the left is $[2j(2j-1)+4qj+q(q-1)]w_j-w_{j-1}=(q+2j)(q+2j-1)w_j-w_{j-1}=0$, and the constant term is $q(q-1)w_0-q(q-1)=0$. $\square$

(E2) is [B3] Proposition 8.1(ii); it is the even part of 68BH's first-order equation $\kappa E'=(\kappa-q)E+q$ for $E={}_1F_1(1;q+1;\kappa)$ after elimination of the odd part, and its $\kappa$-derivative is the homogeneous third-order equation (8.1) of [B3]. Only (E2) is used below.

**Proposition 3.2 (identities).** Along $\kappa\mapsto(X(\kappa),u(\kappa))$, for every $q\ge1$:
$$h=X^2+(2q+1)X+q(q-1)(1-u)-\kappa^2, \tag{C1}$$
$$\dot X=2X-h,\qquad \dot u=-Xu, \tag{C2}$$
$$\kappa^2\Delta_q=T+(X+2)h,\qquad T:=2X^2+q(q-1)uX-2q(q-1)(1-u), \tag{C3}$$
$$\dot T=X^2\big(8-q(q-1)u\big)-h\big(4X+q(q-1)u\big), \tag{C4}$$
$$\dot h=T-(2X+2q-1)h, \tag{C5}$$
$$H_q'+\Big(3m_q+\frac{2q+2}\kappa\Big)H_q=\Delta_q,\qquad \Delta_q:=-\kappa m_q(1-m_q^2)+(2q+5)m_q^2-2+\frac{(q+1)(q+2)m_q}\kappa. \tag{C6}$$
Moreover $\dot h=\kappa(H_q+\kappa H_q')$ and $\ddot h=\kappa^3H_q''+3\kappa^2H_q'+\kappa H_q$.

*Proof.* Divide (E2) by $L_q$ and use $L_q''/L_q=m_q'+m_q^2$: $\kappa^2m_q'=\kappa^2-X^2-2qX-q(q-1)(1-u)$. Then $h=X-\kappa^2m_q'$ is (C1); $\dot X=X+\kappa^2m_q'=2X-h$ after eliminating $\kappa^2$ through (C1); $\dot u=-\kappa L_q'/L_q^2=-Xu$. Differentiating (C1) with (C2) and eliminating $\kappa^2$ again gives (C5); differentiating $T$ gives (C4). (C6) is [B3] eq. (8.2), and (C3) is (C6) rewritten in $(X,u,h)$; both need the derivative of (E2). The last two formulas are $h=\kappa H_q$ differentiated. All identities are verified with symbolic $q$ in `sym_reduction.py` and, independently, `rev_sym.py`; the residual of each is $0$. $\square$

*Reading of (C1) and (C3).* By (C1), $h=(X-X_+)(X+X_++2q+1)$ where $X_+(\kappa)$ is the positive root of $X^2+(2q+1)X+q(q-1)(1-u)-\kappa^2=0$ (the constant term is negative for every $\kappa>0$: comparing $L_q-1$ with $\kappa^2L_q/((q+1)(q+2))$ termwise, $w_j\le w_{j-1}/((q+1)(q+2))$, gives $1-u\le\kappa^2/((q+1)(q+2))$, so the constant term is at most $-2(2q+1)\kappa^2/((q+1)(q+2))$): the zeros of $H_q$ are the crossings of the trajectory $X(\kappa)$ with the explicit curve $X_+(\kappa)$. At a zero of $H_q$, (C5) and the formula for $\dot h$ give $\kappa^2H_q'=\dot h=T$: **$T$ is the transversality of the crossing**, and by (C3) it equals $\kappa^2\Delta_q$ there, matching [B3]. The dynamics (C2) is a closed system in $(X,u,\tau)$; $\kappa^2$ enters only through (C1).

**Lemma 3.3 (the first-order equation for $Q$).** Let $Q:=T-c\,h$ with a constant $c$. Then
$$\dot Q+cQ=g+hB,\qquad g:=X^2\big(8-q(q-1)u\big),\qquad B:=(2c-4)X+c(2q-1-c)-q(q-1)u, \tag{3.1}$$
equivalently $\dfrac{d}{d\tau}\big(e^{c\tau}Q\big)=e^{c\tau}(g+hB)$ with $e^{c\tau}=\kappa^c$. For $c=q-\tfrac12$ and $q\ge3$, $B=(2q-5)X+\tfrac14+q(q-1)(1-u)>\tfrac14$ for all $\kappa>0$; for $(q,c)=(2,2)$, $B=2(1-u)\ge0$.

*Proof.* From (C4), (C5) and $-cT=-cQ-c^2h$: $\dot Q=g-h(4X+q(q-1)u)-cQ-c^2h+c(2X+2q-1)h$, which is (3.1). For $c=q-\tfrac12$: $2c-4=2q-5$ and $c(2q-1-c)=(q-\tfrac12)^2=q(q-1)+\tfrac14$. $\square$

The forcing $g+hB$ is the whole mechanism: on the zero set $\{h=0\}$ it reduces to $g$, whose sign is that of $u_*-u$, i.e. of $\kappa-\kappa_L$; off the zero set the term $hB$ has the sign of $h$. The constant $8$ is forced: for any $\tilde Q$ agreeing with $T$ on $\{h=0\}$, $\dot{\tilde Q}|_{h=0}=g+(\partial\tilde Q/\partial h)\,T$, so the forcing on the zero set is $g$ up to a multiple of the transversality itself (a heuristic, not used).

**Proposition 3.4 (probabilistic reading).** Let $J$ have the law $P(J=j)=w_jz^j/L_q$, $j\ge0$ (an exponential family in $\theta=\log z$), and let $K\sim\mathrm{Poisson}(\kappa)$ be conditioned on $A_q=\{K\ge q,\ K\equiv q\ (\mathrm{mod}\ 2)\}$, so that $K=q+2J$ in law. Then
$$\mathbb EJ=\frac X2,\qquad \operatorname{Var}J=\frac{d\,\mathbb EJ}{d\theta}=\frac\kappa4(m_q+\kappa m_q'),\qquad \kappa H_q=4\big(\mathbb EJ-\operatorname{Var}J\big), \tag{3.2}$$
$$u=P(K=q\mid A_q),\qquad X=\mathbb E[K-q\mid A_q],\qquad \kappa H_q=2\,\mathbb E[K-q\mid A_q]-\operatorname{Var}(K\mid A_q), \tag{3.3}$$
$$\mathbb E[K(K-1)\mid A_q]=\kappa^2+q(q-1)\,P(K=q\mid A_q). \tag{3.4}$$
Hence $H_q<0$ iff the Fano factor $\operatorname{Var}J/\mathbb EJ$ exceeds $1$, the fold is where the conditional variance of $K$ equals twice its conditional excess mean, and the threshold (2.4) is $P(K=q\mid A_q)=8/(q(q-1))$.

*Proof.* $\mathbb EJ=zL_q'(z)/L_q$ in the variable $z$ equals $\kappa L_q'(\kappa)/(2L_q)=X/2$; $d/d\theta=\tfrac\kappa2\,d/d\kappa$ gives the variance; then $4(\mathbb EJ-\operatorname{Var}J)=2X-\kappa m_q-\kappa^2m_q'=\kappa H_q$. $P(A_q)=e^{-\kappa}\kappa^qL_q/q!$, so $P(K=q\mid A_q)=1/L_q$. For (3.4) and $q\ge2$, $\sum_{k\in A_q}k(k-1)\kappa^k/k!=\kappa^2\sum_{k\in A_q-2}\kappa^k/k!$ and $A_q-2=A_q\cup\{q-2\}$, while $\kappa^2P(K=q-2)/P(K=q)=q(q-1)$. For $q=1$ the same identity follows directly because the extra formal index is $-1$, its Poisson mass is zero, and $q(q-1)=0$. $\square$

7H9F's parity-truncated binomial law concerns the coefficients $c_{q,r}$; the law of Proposition 3.4 is attached to the function itself. We are not aware of a theorem on a single crossing of the Fano factor of a power-series distribution with log-concave weights; the present proof gives one for the weights $1/(q+1)_{2j}$.

## 4. Main theorem and proof

**Theorem 4.1.** Let $q\ge4$ ($n=q+2\ge6$) and let $\kappa_L$ be defined by (2.4). Then $H_q$ has exactly one positive zero $\kappa_f$; $H_q<0$ on $(0,\kappa_f)$, $H_q>0$ on $(\kappa_f,\infty)$, $H_q'(\kappa_f)>0$, and $\kappa_f>\kappa_L$. Consequently $\lambda_q=\kappa/(2m_q)$ is strictly decreasing on $(0,\kappa_f]$ and strictly increasing on $[\kappa_f,\infty)$: exactly one fold.

Throughout this section $c=q-\tfrac12$, $Q=T-ch$, $g$ and $B$ are as in Lemma 3.3, and $B>\tfrac14$.

**Lemma 4.2 (Step 1: no zero before the threshold).** $h<0$ on $(0,\kappa_L]$.

*Proof.* Suppose not and let $\kappa_*:=\inf\{\kappa\in(0,\kappa_L]:h(\kappa)\ge0\}$. The set is closed in $(0,\kappa_L]$, so the infimum is attained and $h(\kappa_*)\ge0$; by (F1) $\kappa_*>0$ and $h<0$ on $(0,\kappa_*)$, so by continuity $h(\kappa_*)=0$. On $(0,\kappa_*]$ we have $h\le0$, hence $hB\le0$, and $u\ge u(\kappa_L)=u_*$ by (F3), hence $g=X^2(8-q(q-1)u)\le0$; by (3.1),
$$\frac{d}{d\tau}\big(e^{c\tau}Q\big)=e^{c\tau}(g+hB)\le0\quad\text{on }(0,\kappa_*],\qquad<0\ \text{on }(0,\kappa_*)$$
(strictly because $X>0$ and $u>u_*$ for $\kappa<\kappa_L$). Since $e^{c\tau}Q=\kappa^cQ\to0$ as $\tau\to-\infty$ by (F4) and $c>0$, integration gives $e^{c\tau_*}Q(\kappa_*)=\int_{-\infty}^{\tau_*}\frac d{ds}(e^{cs}Q)\,ds<0$ (the improper integral of a sign-definite integrand converges because the left side is finite). Hence $T(\kappa_*)=Q(\kappa_*)+c\,h(\kappa_*)=Q(\kappa_*)<0$. But $h<0$ on $(0,\kappa_*)$ and $h(\kappa_*)=0$ force $\dot h(\tau_*)\ge0$, while (C5) gives $\dot h(\tau_*)=T(\kappa_*)-0<0$. Contradiction. $\square$

**Lemma 4.3 (Step 2: no second zero).** Let $\kappa_f$ be the first positive zero of $H_q$ (it exists by (F1), (F2), and $\kappa_f>\kappa_L$ by Lemma 4.2). Then $H_q'(\kappa_f)>0$, and $H_q$ has no zero in $(\kappa_f,\infty)$.

*Proof.* Since $\kappa_f>\kappa_L$, (F3) gives $u<u_*$ on $[\kappa_f,\infty)$, so $g>0$ there. $H_q<0$ on $(0,\kappa_f)$ and $H_q(\kappa_f)=0$ give $H_q'(\kappa_f)\ge0$, i.e. $T(\kappa_f)=\kappa_f^2H_q'(\kappa_f)\ge0$ by the reading of (C5). A double zero is impossible: if $H_q(\kappa_f)=H_q'(\kappa_f)=0$ then $h=T=0$ there, and differentiating (C5) once more, $\ddot h=\dot T-(2X+2q-1)\dot h-h\,\tfrac{d}{d\tau}(2X+2q-1)=\dot T=g>0$ at $\kappa_f$ by (C4); but $\ddot h=\kappa^3H_q''$ at such a point, so $H_q$ would have a strict local minimum with value $0$, contradicting $H_q<0$ before $\kappa_f$. Hence $T(\kappa_f)>0$ and $H_q>0$ immediately after $\kappa_f$. Suppose $H_q$ has a zero in $(\kappa_f,\infty)$ and let $\kappa_1$ be the first one: the zeros of the nonconstant real-analytic function $H_q$ are isolated and cannot accumulate at $\kappa_f$. On $[\kappa_f,\kappa_1]$ we have $h\ge0$, hence $hB\ge0$, and $g>0$, so $\frac d{d\tau}(e^{c\tau}Q)\ge e^{c\tau}g>0$ there and
$$Q(\kappa_1)>Q(\kappa_f)\,e^{-c(\tau_1-\tau_f)}=T(\kappa_f)\,e^{-c(\tau_1-\tau_f)}>0 .$$
But $h(\kappa_1)=0$, so $Q(\kappa_1)=T(\kappa_1)=\kappa_1^2H_q'(\kappa_1)\le0$ because $H_q$ reaches $0$ from above. Contradiction. $\square$

*Proof of Theorem 4.1.* Existence of $\kappa_f$ and $\kappa_f>\kappa_L$: (F1), (F2), Lemma 4.2. Uniqueness, the signs, and $H_q'(\kappa_f)>0$: Lemma 4.3. The statement on $\lambda_q$ is (2.2) with $m_q>0$. $\square$

**Remarks 4.4.** (i) *What is used.* Only (E2), the positivity of the coefficients of $L_q$, the sign of $\gamma_q$ in (F1), and $H_q\to1$. No numerical evaluation or a priori estimate at the unknown fold is required; the obstruction recorded in [B3] Section 8 (cancellation of the $O(q)$ terms of $\Delta_q$ at the fold) does not arise because the sign of $T$ is never needed on an interval, only at $\kappa_*$ and $\kappa_1$, where it comes from the integrating factor, and at $\kappa_f$, where it comes from $H_q'(\kappa_f)\ge0$. The two halves of the argument are mirror images: before $\kappa_L$ the forcing pushes $\kappa^cQ$ down, so $H_q$ cannot come up to $0$; after $\kappa_f>\kappa_L$ it pushes $\kappa^cQ$ up, so $H_q$ cannot come down to $0$.
(ii) *Byproducts.* $T=Q+ch<0$ on $(0,\kappa_L]$ (Step 1 gives $Q<0$ there) and $T\ge Q>0$ on $[\kappa_f,\infty)$; by (C3) the same signs hold for $\Delta_q$ along the trajectory. Hence *every* sign change of $T$ or of $\Delta_q$ lies in $(\kappa_L,\kappa_f)$. That there is exactly one (numerically true, [B3] Section 8) is neither proved nor needed.
(iii) *Relation to 7H9F Theorem 8.2.* Theorem 4.1 is the one-zero conclusion of that theorem, obtained without its coefficient law; it does not prove the law $c_{q,r}<0$ ($2\le r<q$), $c_{q,r}>0$ ($r\ge q$), which remains 7H9F's.
(iv) *Recipe for other normalizers.* Write the fold numerator as $\kappa H=P(X,u,\kappa)$ with $(X,u)=(\kappa m,1/L)$ using the lowest-order inhomogeneous equation available; compute the transversality polynomial $T=\dot h|_{h=0}$ and its forcing $\dot T|_{h=0}$; look for $c$ with $B\ge0$ and a forcing whose sign is governed by one monotone state variable. Whether this succeeds for other third-order normalizers is open (Section 8).

**Corollary 4.5 (the chain to 7H9F Theorem 9.1).** For every $n\ge6$, the conclusions of 7H9F Theorem 9.1 (exactly one fold of $\lambda_q$; a unique positive zero $\kappa_c>\kappa_f$ of $F_q$; $0<\lambda_c<n(n-1)/4$; below $\lambda_c$ the zero radius is the unique global radius, at $\lambda_c$ exactly $0$ and $b_c=m_q(\kappa_c)$ are active, above it one positive radius is uniquely active, and there is no later exchange or reentrance; the two-piece rate–distortion function (30) of 7H9F) hold with Theorem 4.1 in place of 7H9F Theorem 8.2.

*Proof.* 7H9F's proof of Theorem 9.1 (its Section 9) uses from Theorem 8.2 only that $H_q$ has a unique positive zero with $H_q<0$ before and $H_q>0$ after, through $\lambda_q'=H_q/(2m_q^2)$ and $F_q'=H_q$. Its other inputs — $F_q(0)=0$, $F_q(\kappa)=\kappa-2q\log\kappa+O(1)\to\infty$ (7H9F Proposition 11.1), the identities $\phi_\lambda(b)=F_q(\kappa)/2$ and $\phi_\lambda''(b)=2\lambda(\kappa m_q'/m_q-1)$ at a stationary radius, the inactivity of $b=1$, and the positivity of the fourth cumulant for $n\ge6$ — are independent of Theorem 8.2. Theorem 4.1 supplies exactly the sign pattern. $\square$

## 5. The corollary for $q=2,3$

**Corollary 5.1 (7H9F Lemma 7.1 for $n=4,5$).** For $q\in\{2,3\}$, $H_q>0$ on $(0,\infty)$; $\lambda_q$ is strictly increasing and has no fold.

*Proof.* Take $c=2$ for $q=2$ and $c=\tfrac52$ for $q=3$; by Lemma 3.3, $B=2(1-u)\ge0$ and $B=X+\tfrac14+6(1-u)>0$ respectively. Since $q(q-1)\le6<8$, $g=X^2(8-q(q-1)u)>0$ for every $\kappa>0$ (there is no threshold), and $H_q>0$ near $0^+$ by (F1) ($q^2-q-8=-6,-2$). If $H_q$ had a zero, let $\kappa_1$ be the first; on $(0,\kappa_1]$, $h\ge0$, so $\frac d{d\tau}(e^{c\tau}Q)\ge e^{c\tau}g>0$, and with $e^{c\tau}Q\to0$ at $-\infty$ we get $Q(\kappa_1)>0$, i.e. $T(\kappa_1)=Q(\kappa_1)>0$; but $H_q$ reaches $0$ from above, so $T(\kappa_1)=\kappa_1^2H_q'(\kappa_1)\le0$. Contradiction. $\square$

For $q=1$ ($n=3$), $B=(2c-4)X+c(1-c)$. Since $X$ runs from $0$ to $+\infty$, global nonnegativity would require both $c\ge2$ and $c(1-c)\ge0$, which is impossible. This integrating-factor choice therefore does not cover $q=1$; that case is 7H9F's explicit series for $J_3$ or the Bessel-family theorem of [B3] ($L_1={}_0F_1(;\tfrac32;\kappa^2/4)$).

## 6. The interval-arithmetic certificate (redundant)

Before Lemma 4.2 was found, the conclusion $H_q<0$ on $(0,\kappa_L]$ was checked for individual $q$ by an interval-enclosure computation (`certify_neg.py`, `mpmath.iv`, 40 digits). Since Lemma 4.2 now proves it for every $q\ge4$, this computation is auxiliary and redundant; we record its scope and its floating-point limitation. The author-side repair supplement `repro/candidate2/certify_neg_outward.py` places the two sign-critical comparisons in outward-rounded interval arithmetic and was freshly rerun for selected $q$.

Put $S_r(z)=\sum_{j\ge0}j^rw_jz^j$ ($r=0,\dots,3$; $S_0=L_q$) and $G(z):=S_0S_1-S_0S_2+S_1^2=S_0^2\,\kappa H_q/4$ by (3.2). The certificate proves $G<0$ on $(0,z_L^+]$ with $z_L^+\ge z_L=\kappa_L^2$.

*Small $z$, analytic.* $G=\sum_{r\ge2}g_rz^r$ with $g_2=-(q^2-q-8)/((q+1)^2(q+2)^2(q+3)(q+4))$ (exact, `sym_reduction.py`) and, for $r\ge3$, $|g_r|=|\sum_{i+j=r}w_iw_j\,j(1-j+i)|\le r(r+1)^2((q+1)(q+2))^{-r}\le(4/((q+1)(q+2)))^r$, using $w_i\le((q+1)(q+2))^{-i}$. With $y=z/((q+1)(q+2))$ and $c_2=(q^2-q-8)/((q+3)(q+4))$,
$$G(z)\le-c_2y^2+\frac{(4y)^3}{1-4y}<0\qquad\text{for }0<y<y_0:=\frac{c_2}{64+4c_2}$$
(Lemma S; exact rational arithmetic). This settles $\kappa\to0^+$, where interval enclosures of $G$ would not resolve the sign. The continuation starts at $z_0(1-10^{-30})<z_0:=y_0(q+1)(q+2)$, so there is no gap.

*Enclosures.* $S_r(z)$ is enclosed by the interval partial sum of $N$ terms plus $[0,2N^rw_Nz^N]$, valid when $\rho_N=z/((q+2N+1)(q+2N+2))\le\tfrac1{16}$: the term ratios decrease, $(N+i)^r\le N^r8^i$ for $r\le3$, and $\sum_i(8\rho_N)^i\le2$. All series have positive terms, so this is a rigorous enclosure. $z_L^+$ is found by bisection until the interval *lower* bound of $S_0$ exceeds $q(q-1)/8$; since $S_0$ is increasing, $z_L\le z_L^+$.

*Continuation.* $G'=(S_1^2+S_0S_2+S_1S_2-S_0S_3)/z$, so on $[a,b]$, $\sup|G'|\le M(a,b):=(S_0S_2+S_1^2+S_0S_3+3S_1S_2)(b)/a$ (all $S_r$ positive and increasing), and $G\le\overline G(a)+(b-a)M(a,b)$ on $[a,b]$ with $\overline G(a)$ the interval upper bound. Nodes are chosen adaptively (step $\approx|\overline G(a)|/(2M)$, halved until the bound is negative) and chain exactly from the first node to $z_L^+$; the bound certifies every real point of each $[a,b]$, not only the nodes.

*Coverage and cost.* Every $q$ with $4\le q\le200$ is certified (`certify_4_100.log`, `certify_101_200.log`, all `ok`); $q=4$ needs $52{,}820$ nodes ($68$–$86$ s) because $M$ is about $10^4$ times larger than $\sup|G'|$ near $z_0$ (no cancellation in the majorant while $G'=O(z)$), larger $q$ need $900$–$10{,}400$ nodes and $6$–$131$ s; the total is about $1.75$ h. Earlier runs before a rounding fix of $z_0$ (`old_runs/`) give the same numbers digit for digit. The reviewer reran a byte-identical copy for $q=4,10,37,60$ (identical output), dumped the $52{,}820$ nodes for $q=4$ and checked that they chain ($\max|a_{i+1}-b_i|=0$), recomputed at $80$ digits with plain arithmetic the certified bounds at three nodes (e.g. node $0$: $\overline G=-8.818\cdot10^{-8}$ against $G(a)=-8.818\cdot10^{-8}$, $M=6.7\cdot10^{-2}$ against $\sup|G'|=5.3\cdot10^{-6}$), Lemma S on $39$ points of $(0,z_0)$ for $q=4,10$, and $S_0(z_L^+)-\tfrac32=+1.4\cdot10^{-7}$ for $q=4$.

*Rigor caveat and repaired control.* In the historical script, two decisive comparisons — the final test $\overline G(a)+(b-a)M<0$ and the ratio test $\rho_N\le\tfrac1{16}$ — are evaluated in high-precision floating point rather than as outward-rounded intervals. The printed margins make a changed verdict implausible, but those runs alone do not justify the phrase "every operation is outward-rounded." The candidate-2 supplement instead forms both comparison expressions as `mpmath.iv` intervals and accepts only when the relevant interval upper endpoint has the required sign. Its fresh selected-$q$ runs are a targeted control; the historical $q=4,\ldots,200$ sweep was not rerun with the repaired script. None of these computations is used in Theorem 4.1.

## 7. Numerical table

Values from `num_phi.py` (mpmath positive series; closed form and series agree to $10^{-20}$), confirmed by the reviewer's independent series code to all printed digits. The candidate-2 wrapper `verify_lyapunov_60.py` sets `mp.dps = 60` *after* importing `num_phi` and prints the effective precision, avoiding the imported module's reset of the global context. $\kappa_\Delta$ is the (numerically unique) sign change of $\Delta_q$ along the trajectory.

| $q$ | $\kappa_L$ | $\kappa_f$ | $\kappa_\Delta$ | $L_q(\kappa_f)$ | $T(\kappa_f)$ |
|---:|---:|---:|---:|---:|---:|
| 4 | 3.469051 | 4.415714051 | 4.161910 | 1.9334 | 0.173 |
| 5 | 6.045574 | 7.613543394 | 7.290145 | 4.3697 | 1.415 |
| 6 | 8.174269 | 10.25463377 | 9.904743 | 8.478 | 3.448 |
| 10 | 15.384999 | 19.37353191 | 18.991063 | 62.88 | 14.02 |
| 20 | 30.744399 | 39.94164751 | 39.545885 | 2529 | 38.84 |
| 30 | 44.788910 | 59.99529121 | 59.597519 | $6.8\cdot10^4$ | 59.86 |
| 40 | 58.215297 | 79.99966909 | 79.601279 | $1.7\cdot10^6$ | 79.99 |
| 60 | 84.029603 | 119.9999987 | 119.601067 | $9.6\cdot10^8$ | 120.00 |

The $q=4$ fold $\kappa_f=4.415714051$ is the value printed in 61Y0 Section 6 (whose normalizer $12(2\cosh\kappa-2-\kappa^2)/\kappa^4$ equals $L_4$). Further observations, all numerical: $\kappa_f/q\to2$ (to all printed digits from $q=40$ on, consistent with $m_q\approx1-q/\kappa$ and $m_q(\kappa_f)\to\tfrac12$: $0.3005,\ 0.3982,\ 0.4386,\ 0.4865,\ 0.4993,\ 0.5000$ for $q=4,5,6,10,20,30$); $\kappa_L/q$ rises from $0.87$ ($q=4$) to a maximum near $1.55$ ($q\approx12$) and decreases slowly ($1.43$ at $q=50$, $1.26$ at $q=200$, $1.13$ at $q=1000$); the margin $H_q(\kappa_L)$ is $-4.2\cdot10^{-3}$ at $q=4$ and grows in absolute value ($-0.77$ at $q=1000$). The small $q=4$ margin is why no estimate-based proof was found in [B3]; the argument of Section 4 does not see it. Sanity checks of every inequality used in the proof along trajectories (`verify_lyapunov.py`, $30$ digits, $q\in\{4,5,6,10,30,60\}$, $200$-point grids up to $4q+40$; the reviewer-authored `rev_num.py`, reported at $50$ digits for $q=4,\dots,60,80,100,150,200,400$): $Q<0$ on $(0,\kappa_L]$, and $\frac d{d\tau}(e^{c\tau}Q)<0$ there for every $\kappa>0$, including $\kappa=\kappa_L$ because $g=0$ but $hB<0$; equality is approached only as $\kappa\to0^+$. After the fold, $Q>0$ and $\frac d{d\tau}(e^{c\tau}Q)>0$ on the checked interval; $T(\kappa_f)=\kappa_f^2H_q'(\kappa_f)$ numerically; there is one sampled sign change of $H_q$; and $\inf B=\tfrac14$ is approached as $\kappa\to0$. The candidate-2 fresh 60-digit wrapper also checks $q=2,3$ and the Poisson identity (3.4). These are numerical controls, not proofs of unsampled intervals or of a universal claim.

## 8. Open questions

1. *Third-order normalizers in general.* The phase-lifted coherent orbits of [6XH6] and [6DJ3] have ${}_pF_{p+1}$ normalizers and Slater orbits have ${}_{k-1}F_k$ normalizers, all of order $\ge3$. Does each admit an inhomogeneous lower-order equation playing the role of (E2), and is the forcing on the zero set of the fold numerator sign-definite with a threshold in a single monotone state variable, as in (3.1)? Not attempted.
2. *A unified criterion with the Riccati case.* For ${}_1F_1(a;c)$ the fold count is decided in the plane $(m,\kappa)$ by transversality ([B3]: one fold iff $c>2a$); here it is decided by an integrating factor in $(X,u,\kappa)$. Is there a single Lyapunov-type criterion, e.g. a condition on the Fano factor of the index law of a general power-series normalizer, that contains both?
3. *Grassmann rank $r\ge2$* (matrix-argument ${}_1F_1$; 68BH open question 1): untouched.
4. Uniqueness of the sign change of $T$ or $\Delta_q$ in $(\kappa_L,\kappa_f)$ (Remark 4.4(ii)), and the exact leading coefficient of $T$ on the zero locus (numerically about $\tfrac34$ of $[\kappa^2]\Delta_q$): unimportant for the theorem, not derived.
5. A theorem on a single crossing of $\operatorname{Var}J/\mathbb EJ$ for power-series distributions with log-concave weight sequences, of which Proposition 3.4 with Theorem 4.1 is one instance.

## 9. Reproducibility and literature

All material is in `repro/` next to this file (Python 3.12, sympy 1.14, mpmath 1.3). `repro/author/` is the preserved historical author package, and `repro/reviewer/` is the preserved historical reviewer package. Their provenance and claims of independence are author supplied and were not independently authenticated during candidate-2 repair. `repro/candidate2/` contains the repair supplement: the outward-interval version of the two decisive certificate comparisons, the wrapper that restores and reports 60-digit precision after imports, a local copy of `num_phi.py`, and fresh logs from the repair run. The historical all-$q$ certificate logs remain unchanged.

The script map is as follows. `sym_reduction.py` checks (E2) termwise, its derivative, (C1)–(C6), the bracket $B$, (F1), $g_2$ and $g_3$ with symbolic $q$ (about 5 s). `verify_lyapunov.py` performs the historical 30-digit trajectory checks (about 7 s), while `num_phi.py q ...` generates the table values (historically reported as about 16 s per $q$). `certify_neg.py q ...` is the historical 40-digit interval-enclosure computation (44–86 s for $q=4$, 6–131 s otherwise). The candidate-2 scripts `verify_lyapunov_60.py` and `certify_neg_outward.py` respectively restore and report 60-digit precision after imports and put the two decisive certificate comparisons in outward interval arithmetic. The exploratory scripts `margins.py`, `lemma_c_check.py` and `t_signchange.py` are not proof inputs. Preserved `reviewer/` scripts provide the historical second implementation described above.

No step of the proofs depends on floating point: Theorem 4.1 and Corollary 5.1 use the identities of Section 3, each a short hand computation machine-checked for safety, and Lemma 2.1.

*Literature* (web searches of 2026-09-14 by the author agent and the reviewer). Karp–Sitnik [KS] and Karp [Ka] prove log-concavity and Turán-type inequalities for Kummer and hypergeometric-like functions in their *parameters*. Baricz–Pogány [BP1] use coefficient-ratio and power-series quotient arguments for modified Struve functions; [BP2] develops integral-representation and second-kind comparisons; Gaunt [Ga] proves functional inequalities and monotonicity results for normalized modified Lommel functions of the first kind. None of those cited results concerns the sign of $K'-\kappa K''$, the Fano factor of the index law, or a Lyapunov function of the present kind. Searches for over-dispersion of power-series distributions returned applied (neuroscience) hits only, and searches for the parity-conditioned Poisson law $\{K\ge q,\ K\equiv q\}$ returned only lower-truncated Poisson moment formulas; the identity (3.4) is elementary and appears to be new in this context. Generalized Curie–Weiss models with several transitions [EE] are the classical background of the radial problem; DLMF Chapters 11 and 13 [DLMF] are the standard references for the special functions named. The historical search account is author supplied; candidate-2 repair checked the cited primary papers for these narrower attributions but does not claim exhaustive priority.

## AI-assistance statement

The mathematics, code and original text of this manuscript were produced by Claude Fable 5.1 agents (Anthropic) working under the direction of the author, who set the problem, selected the line of records and is responsible for the claims. The original package reports a research agent, an adversarial reviewer agent and a manuscript-assembly agent; that historical account and the stated serving identities were supplied by the author and were not independently authenticated in this repair. Candidate-2 was prepared by a configured GPT-5.6 Sol agent at medium reasoning effort as author-side revision assistance. It corrected the threshold sign statement, the $q=1$ obstruction, cross-references, the normalized Lommel relation and literature distinctions, precision initialization, and the scope and implementation of the auxiliary certificate; it also ran fresh targeted checks and assembled the revised PDF. This repair is not a scientific assessment of the revised hash. The manuscript has not been peer reviewed by humans.

## References

- [7H9F] L. Eriksson, *Complete Rate–Distortion Phase Diagram of Haar Oriented Two-Planes: One-Change Hypergeometric Coefficients, Unique Coexistence, and No Reentrance*, AI Research Record, ARR-2026-7H9FAPTBZA897AMJ, v2, 2026-08-14. Cited: eqs. (11), (22), (24), (25), (29), (30); Lemma 7.1, Theorem 7.2, Lemma 8.1, Theorem 8.2, Theorem 9.1, Proposition 11.1.
- [68BH] L. Eriksson, *One Fold, Unique Contact and the Complete Two-Piece Rate–Distortion Function of Rank-One Complex-Projective Born Prediction*, AI Research Record, ARR-2026-68BH5JDJCQ8XW8GT, v004, 2026-09-09. Cited: Lemma 3.1 (first-order equation), Theorem 4.1, open question 1.
- [61Y0] L. Eriksson, *Complete Rank-Two Born-Prediction Rate–Distortion on $\mathrm{Gr}_{\mathbb C}(2,4)$: All-Field Matrix–Bingham Rigidity and a Unique Coexistence Transition*, AI Research Record, ARR-2026-61Y0FFA39M8KMBJ5, v1, 2026-08-13. Cited: Section 6 (values at $q=4$).
- [B3] L. Eriksson, *One Fold if and only if the Overlap Law is Right-Skewed: A Riccati Criterion for Tilted Beta Normalizers, with Consequences for Rank-One Projective Rate–Distortion*, unpublished manuscript, 13 September 2026. Cited: Theorems 3.1, 4.1, 7.1; Section 8 (Proposition 8.1(ii), (iv), eq. (8.2), Proposition 8.2, the numerical sign change of $\Delta_q$); open question 1.
- [6XH6] L. Eriksson, *Exact Classical Rate–Distortion for Phase-Lifted Generalized Coherent States: Cartan-Product Laplace Rigidity, Universal Radial Envelopes, and Slater-Determinant Transitions*, AI Research Record, ARR-2026-6XH6JAS5ZA934A6J, v1, 2026-08-14.
- [6DJ3] L. Eriksson, *Universal Semiclassical Coexistence in Classical Compression of Phase-Lifted Coherent States: Dimension-Normalized Contacts and a Matched High-Fidelity Boundary Layer*, AI Research Record, ARR-2026-6DJ302B1G38V4SHD, v1, 2026-08-14.
- [KS] D. Karp, S. M. Sitnik, Log-convexity and log-concavity of hypergeometric-like functions, *J. Math. Anal. Appl.* 364 (2010) 384–394; arXiv:0902.3073.
- [Ka] D. B. Karp, Turán's inequality for the Kummer function of the phase shift of two parameters, *J. Math. Sci. (N.Y.)* 178 (2011) 178–186.
- [BP1] Á. Baricz, T. K. Pogány, Functional inequalities for modified Struve functions, *Proc. Roy. Soc. Edinburgh Sect. A* 144 (2014) 891–904; arXiv:1301.5423.
- [BP2] Á. Baricz, T. K. Pogány, Functional inequalities involving modified Struve functions, *Math. Inequal. Appl.* 17 (2014) 1387–1398; arXiv:1301.5635.
- [Ga] R. E. Gaunt, Functional inequalities and monotonicity results for modified Lommel functions of the first kind, *Results Math.* 77 (2022), doi:10.1007/s00025-021-01538-8; arXiv:2002.07430.
- [EE] T. Eisele, R. S. Ellis, Multiple phase transitions in the generalized Curie–Weiss model, *J. Stat. Phys.* 52 (1988) 161–202.
- [DLMF] NIST Digital Library of Mathematical Functions, https://dlmf.nist.gov/, Chapter 11 (Struve and related functions, §11.2, §11.9) and Chapter 13 (confluent hypergeometric functions, §13.2). Release 1.2.x.
