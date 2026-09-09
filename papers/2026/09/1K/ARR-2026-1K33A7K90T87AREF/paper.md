# The inverse self-commutator cost at inertia $(m,2)$: a dimension-free closed formula, block-shift optimizers and a Pieri certificate

**Lluis Eriksson** (Independent researcher)

9 September 2026 (internal workshop revision v004; received version 2 and deposited v003 preserved)

## Abstract

For a traceless Hermitian $F\in M_d(\mathbb C)$ let $\kappa_d(F)=\tfrac12\min\{\|C\|_{HS}^2: CC^*-C^*C=2F\}$. We give the exact value of $\kappa_d$ on the whole inertia-$(m,2)$ stratum (positive eigenvalues $a_1\ge\dots\ge a_m>0$, two negative eigenvalues $-b_2\ge -b_1$, any number of zeros) for every $m\ge2$ and every $d$: $\kappa_d=\max(F_0,\dots,F_{m-1},G_1,G_3,\dots)$ for explicit linear forms. The lower bound sums Lidskii–Wielandt and Weyl inequalities with one Pieri-type Horn triple (Littlewood–Richardson coefficient $1$); the upper bound is an explicit $2\times2$-block weighted shift whose feasibility is a one-parameter interval recursion. Both bounds are dimension-free, so the value is invariant under zero padding, and the chamber structure is explicit. Every optimizer has rank $m$ or $m+1$, the minimal optimal rank equals $\max(n_+,n_-)=m$ in every dimension, and rank $m+1$ occurs exactly in one open chamber after padding, where the optimal spectrum is not unique. By $F\mapsto-F$ the same formula covers inertia $(2,n)$.

## 1. Introduction: antecedents and contribution

The quantity $\kappa_d(F)$ measures the cheapest way, in Hilbert–Schmidt norm, to realise a prescribed traceless Hermitian $F$ as a self-commutator $\tfrac12(CC^*-C^*C)$; equivalently (Lemma 2.1 of [FourLevel]) as $\inf\|A\|_{HS}\|B\|_{HS}$ over Hermitian $A,B$ with $-i[A,B]=F$. Its theory has been developed in a series of records of the AI Research Record archive, cited here by descriptive keys (their ARR identifiers and titles are in the reference list); everything used from them is restated in this paper, so that it can be read without them. [FourLevel] reduced $\kappa_d$ to a finite linear program over Horn inequalities (the *Horn program*, Theorem 2.2 there, restated as (2.1) below) and gave the exact four-level formula (Theorem 3.1 there) $\kappa_4=\max\{\lambda_1-\lambda_3,\lambda_2-\lambda_4,\lambda_1-2\lambda_2-\lambda_3,\lambda_2+2\lambda_3-\lambda_4\}$. [FiveLevel] gave the twelve-term five-level formula (Theorem 3.1 there). [OneSpike] proved the one-spike formula $\kappa_d=\sum_j j\,b_j$ when one sign has multiplicity one (Theorem 3.1 there), with rigidity for balanced optima, and noted that the cost is not known in closed form on general sign patterns. [RankAdaptive] proved the rank-adaptive bound $P\le\kappa_d\le(\rho/2)P$, $\rho=\operatorname{rank}F$ (Theorem 1.1 there), and introduced the universal LR-one triples. [RankOnset] certified $r_*=r_0=\max(n_+,n_-)$ for $d\le7$ (Theorem 3.1 there), exhibited the first target ($d=8$, Theorem 4.1 there) whose optimizers all have rank above the inertia bound, and showed (Remark 3.3 there) that zero padding can lower the value: the spectrum $(25,18,18,-10,-17,-17,-17)/7$ has $\kappa_7=74/7$ but $\kappa_8=73/7$. [Ceiling] proved the sharp inertia ceiling $\kappa_d\le\frac{M+1}2P$, $M=\max(n_+,n_-)$ (Theorem 1 there).

**Contribution.** We treat the first stratum on which both signs have multiplicity larger than one: inertia $(m,2)$ (and, by $F\mapsto-F$, inertia $(2,n)$), with arbitrary zero padding. Theorem A gives the closed formula, Theorem B its chamber structure, and Theorem C$'$ the rank and uniqueness properties of optimizers. The proof has two elementary halves. The lower bound is a sum of classical Lidskii–Wielandt and Weyl inequalities plus one non-Lidskii Horn triple whose Littlewood–Richardson coefficient is $1$ by the Pieri rule; only the necessity direction of the Horn–Klyachko theorem is used. The upper bound is an explicit operator, a "$2\times2$-block weighted shift" generalising the cumulative-sum weighted shift of [RankAdaptive,OneSpike], whose feasibility reduces to a one-parameter recursion in $2\times2$ matrices. Both halves are independent of $d$, which is why the value is padding-invariant here although, as [RankOnset] showed, it is not in general; the *set of optimizers* is not padding-invariant even on this stratum (Section 7).

**Novelty, stated honestly.** Two web searches (Section 11) and the nine records of the line found no prior closed formula for this stratum and no prior use of block weighted shifts or of a Pieri certificate in this problem. The nearest literature on norms in commutator representations is the quantitative commutator theorem of Johnson–Ozawa–Schechtman [JOS13] and its Hilbert–Schmidt version by Angel–Schechtman [AS15]. For general factorisations $A=[B,C]$ of a zero-trace matrix, [JOS13] bounds the product of the two operator norms, whereas [AS15] uses the operator norm of $B$ and the Hilbert–Schmidt norm of $C$. Both objectives differ from the self-commutator cost with prescribed spectrum studied here. These searches do not certify priority.

## 2. Setting

Throughout, $\|X\|^2=\operatorname{Tr}X^*X$ and $F\in M_d(\mathbb C)$ is Hermitian with $\operatorname{Tr}F=0$ and ordered spectrum $\lambda_1\ge\dots\ge\lambda_d$. On the inertia-$(m,2)$ stratum we write
$$\begin{gathered}\lambda=(a_1\ge\dots\ge a_m>0,\;0^{z},\;-b_2,\;-b_1),\\  b_1\ge b_2>0,\\  \sum_{j}a_j=b_1+b_2=:P,\\  d=m+z+2,\end{gathered}$$
and use the notation
$$\begin{gathered}A_i:=\sum_{k\ge i}a_k\ (A_{m+1}=0),\\  E_i:=a_i+a_{i+2}+a_{i+4}+\cdots\ (E_{m+1}=E_{m+2}=0),\\  g_j:=a_j-a_{j+1}\ (j\text{ odd},\ a_{m+1}:=0),\\  g^*:=\max_{j\text{ odd}\le m}g_j.\end{gathered}$$
Note $A_i=E_i+E_{i+1}$, $E_i\ge E_{i+1}$, and $E_1-E_2=\sum_{j\text{ odd}}g_j\ge g^*$.

Given $C$ with $CC^*-C^*C=2F$, put $R=CC^*/2$ and $S=C^*C/2$. Then $R,S\succeq0$ have the same spectrum $s_1\ge\dots\ge s_d\ge0$ (the *common spectrum*), $R-S=F$, and $\tfrac12\|C\|^2=\operatorname{Tr}R=\sum_t s_t$. Conversely any pair $R,S\succeq0$ with equal spectra $R=U\Sigma U^*$, $S=V\Sigma V^*$ and $R-S=F$ comes from $C=U\sqrt{2\Sigma}V^*$. Hence ([FourLevel] Theorem 2.2, [RankOnset] Proposition 2.2, in the $s=p/2$ normalisation)
$$\kappa_d(F)=\min\Big\{\sum_{t<d}s_t:\ s_1\ge\dots\ge s_{d-1}\ge s_d=0,\ (s,\,-s^{\mathrm{rev}},\,\lambda)\ \text{Horn-feasible}\Big\},\tag{2.1}$$
where Horn-feasible means that $\alpha=(s_1,\dots,s_{d-1},0)$, $\beta=(0,-s_{d-1},\dots,-s_1)$, $\gamma=\lambda$ are the spectra of Hermitian $R$, $-S$, $F=R+(-S)$, i.e. satisfy all Horn inequalities $\sum_{k\in K}\gamma_k\le\sum_{i\in I}\alpha_i+\sum_{j\in J}\beta_j$, $(I,J,K)\in T^d_r$ [Ho62,Kl98,KT99,Fu00]. The normalisation $s_d=0$ is legitimate because subtracting $s_d\mathbf 1$ from $R$ and $S$ preserves positivity, equal spectra and $R-S=F$, and lowers the cost. The sign convention is $R-S=F$ with $R=CC^*/2$; replacing $C$ by $C^*$ swaps $R$ and $S$, so $\kappa_d(-F)=\kappa_d(F)$, which transfers every statement below to inertia $(2,n)$. Finally $P=\operatorname{Tr}F_+$, $r_0(F):=\max(n_+,n_-)$ and $r_*(F):=$ least rank of an HS-optimizer.

In $s$-notation a Horn triple $(I,J,K)$ reads
$$\sum_{i\in I,\ i<d}s_i-\sum_{j\in J,\ j>1}s_{d+1-j}\ \ge\ \sum_{k\in K}\lambda_k.\tag{2.2}$$
We write $\lambda(I)=(i_r-r,\dots,i_1-1)$ for the partition attached to $I=(i_1<\dots<i_r)$; by Klyachko's theorem [Kl98] the inequality (2.2) holds for all Hermitian triples whenever the Littlewood–Richardson coefficient $c^{\lambda(K)}_{\lambda(I)\lambda(J)}$ is nonzero. Only this necessity direction is load-bearing for Theorems A and B; Horn sufficiency (Klyachko, Knutson–Tao) enters only to identify the set of optimal common spectra with the optimal face of the linear program (2.1).

## 3. Statements

**Theorem A (inertia $(m,2)$, all $d$).** For every $m\ge2$, $z\ge0$ and every $(a,b)$ as in Section 2,
$$\kappa_d(F)=\Phi(a;b):=\max\Big(\max_{0\le k\le m-1}F_k,\ \max_{j\ \mathrm{odd},\ 1\le j\le m}G_j\Big),$$
with
$$\begin{gathered}F_k=k\,b_1+\sum_{j=1}^m c_k(j)\,a_j,\quad c_k(j)=\begin{cases}j-k,& j\le k,\\ \lceil (j-k)/2\rceil,& j\ge k,\end{cases}\\  G_j=b_2+\sum_{i=1}^m\Big\lfloor \frac i2\Big\rfloor a_i+(a_j-a_{j+1}).\end{gathered}$$
Equivalently, in tail-sum form,
$$\begin{gathered}F_0=\sum_{t\ \mathrm{odd}}A_t,\\  F_k=b_1+\sum_{j=2}^{k}(A_j-b_2)+\sum_{t\ge k+1,\ t-k\ \mathrm{odd}}A_t\ (k\ge1),\\  G_j=b_2+\sum_{i\ \mathrm{even}<j}A_i+a_j+A_{j+2}+\sum_{i\ \mathrm{even}\ge j+3}A_i .\end{gathered}$$
The value does not depend on $z$. The same formula gives $\kappa_d$ on the inertia-$(2,n)$ stratum (two positive eigenvalues $b_1\ge b_2$, negative eigenvalues $-a_1,\dots,-a_n$).

**Theorem B (chambers and exposed forms).** Let $k^*:=\max\{k\ge1: E_{k+1}\ge b_2\}$ (defined when $b_2\le E_2$) and $j^*\in\arg\max_{j\text{ odd}}g_j$. Then
$$\kappa_d=\begin{cases}F_{k^*}, & 0<b_2\le E_2\ \ (\text{equivalently } E_{k^*+2}\le b_2\le E_{k^*+1}),\\ F_0, & E_2\le b_2\le E_1-g^*,\\ G_{j^*}, & E_1-g^*\le b_2\ (\le b_1).\end{cases}$$
Along the $F$-family $F_k\ge F_{k-1}\iff E_{k+1}\ge b_2$ (so $k\mapsto F_k$ is unimodal); along the $G$-family $G_j\ge G_{j'}\iff g_j\ge g_{j'}$; and $G_j\ge F_0\iff b_2\ge E_1-g_j$. The forms that are the unique maximiser at some point of the stratum ("exposed" forms) are exactly $F_1,\dots,F_{m-1}$, all $G_j$ ($j$ odd), and $F_0$ when $m\ge3$; their number is $(m-1)+\lceil m/2\rceil+[m\ge3]$, i.e. $2,5,6,8,9,11,12,14$ for $m=2,\dots,9$.

**Theorem C$'$ (rank and uniqueness of optimizers).** Let $C$ be an HS-optimizer, i.e. $CC^*-C^*C=2F$ and $\tfrac12\|C\|^2=\kappa_d(F)$, with common spectrum $s$.

1. $s_d=0$, $s_{d-1}=0$ and $s_t=0$ for $m+2\le t\le d-1$. Hence $\operatorname{rank}C\in\{m,m+1\}$, and $r_*(F)=r_0(F)=m$ on the stratum in every dimension $d$.
2. If $z=0$, or the maximum $\Phi$ is attained by some form other than $G_m$ with $m$ odd (in particular if $m$ is even or $b_2\le E_1-a_m$), then also $s_{m+1}=0$ and $\operatorname{rank}C=m$.
3. If $m$ is odd, $z\ge1$ and $b_2>E_1-a_m$ (the open $G_m$ chamber; inside the stratum this forces $a_m=g_m>g_j$ for every odd $j<m$, so $G_m$ is the unique maximiser), then optimizers of rank $m$ and of rank $m+1$ both exist.
4. The optimal common spectrum is unique for $m=2$ (all $z$) and for $m=3$ when $z=0$ or when $b_2\le E_1-a_3$; it is not unique for $m=3$, $z\ge1$, $b_2>E_1-a_3$. For every $m\ge4$ it is not unique on the open $F_{m-3}$ chamber $E_{m-1}<b_2<E_{m-2}$ whenever $a_{m-2}>a_{m-1}$.

In particular the value $\kappa_d$ is padding-invariant on the stratum but the optimizer set is not: rank-$(m+1)$ optimizers appear only after padding.

## 4. Lower bound

### 4.1 Dimension-free inequalities

All inequalities below are instances of (2.2) valid in every $d\ge m+2$.

**Lemma 4.1 (Lidskii–Wielandt instances).** For $I=K$ of size $r$ and $J=(1,\dots,r)$, $\lambda(J)=0$ and $c=1$; (2.2) becomes $\sum_{k\in K,k<d}s_k-\sum_{t=d-r+1}^{d-1}s_t\ge\sum_{k\in K}\lambda_k$ [Li50,Wi55]. The instances used are:

- $K=(1..d-1)$: $s_1\ge b_1$.
- $(T_j)$ $K=(j..d-1)$, $2\le j\le m$: $s_j\ge A_j-b_2$.
- $(\Pi_t)$ $K=(t..d-2)$, $1\le t\le m-1$: $s_t+s_{t+1}-s_{d-1}\ge A_t$.
- $(B_j)$ $K=\{j\}\cup(j+2..d-2)$, $j+2\le m$: $s_j+s_{j+2}-s_{d-1}\ge a_j+A_{j+2}$.
- (Weyl) $I=K=\{j\}$, $J=\{1\}$, i.e. the triple $(j;1;j)$: $s_j\ge a_j$ for $1\le j\le m$ (no other $s$-index occurs, since $J\setminus\{1\}=\emptyset$).

*Proof.* For $K=(t..d-2)$ the left side of (2.2) is $(s_t+\dots+s_{d-2})-(s_{t+2}+\dots+s_{d-1})=s_t+s_{t+1}-s_{d-1}$ and the right side is $\sum_{k=t}^{d-2}\lambda_k=A_t$ because the zeros contribute nothing; the other cases are identical computations. $\square$

**Lemma 4.2 (lower Weyl).** $I=(1..d-1)$, $J=K=[d]\setminus\{d-1\}$: $s_2\ge b_2$.

*Proof.* $\lambda(I)=0$, $\lambda(J)=\lambda(K)=(1)$, $c=1$; the sum condition $\sum I+\sum J=\sum K+r(r+1)/2$ holds with $r=d-1$. The left side of (2.2) is $(s_1+\dots+s_{d-1})-(s_1+s_3+\dots+s_{d-1})=s_2$ and the right side is $-\lambda_{d-1}=b_2$. It is the Weyl inequality $\lambda_{d-1}(F)\ge\lambda_d(R)+\lambda_{d-1}(-S)$. $\square$

**Lemma 4.3 (Pieri triple).** For even $i$ with $i+2\le d-1$ let $r=d-i-1$ and
$$I=\{i-1\}\cup(i+1..d-2),\qquad J=(1..d-i-2)\cup\{d-i\},\qquad K=(i..d-2).$$
Then $\lambda(I)=((i-1)^{r-1},i-2)$, $\lambda(J)=(1)$, $\lambda(K)=((i-1)^r)$, so $c^{\lambda(K)}_{\lambda(I)\lambda(J)}=1$ by the Pieri rule, and (2.2) reads
$$(\mathrm{Pi})_i:\qquad s_{i-1}+s_{i+2}-s_{d-1}\ \ge\ A_i ,$$
which for $i+2=d-1$ collapses to $s_{i-1}\ge A_i$.

*Proof.* The cardinalities are $d-i-1$ each; with $n=d-i$, $\sum I+\sum J-\sum K=-1+n+\binom{n-1}{2}=\binom n2=r(r+1)/2$. The partitions are read off from the definition ($i_r=d-2$ gives $i_r-r=i-1$, and so on down to $i_1-1=i-2$; in $J$ only the last index exceeds its position, by one). $\lambda(K)/\lambda(I)$ is a single box, so the Pieri rule gives $c=1$ [Fu97]. The left side of (2.2) is $s_{i-1}+(s_{i+1}+\dots+s_{d-2})-(s_{d-1}+\dots+s_{i+3})-s_{i+1}=s_{i-1}+s_{i+2}-s_{d-1}$, the right side $\sum_{k=i}^{d-2}\lambda_k=A_i$. $\square$

*Example ($d=6$, $i=2$).* Here $r=3$, $I=\{1,3,4\}$, $J=\{1,2,4\}$, $K=\{2,3,4\}$. The associated partitions, with trailing zeros retained, are $(1,1,0)$, $(1,0,0)$ and $(1,1,1)$. Adding one box in the third row is the unique Pieri step, so the coefficient is one. The sum condition is $8+7-9=6=3\cdot4/2$. With $s_6=0$, the left side of (2.2) is
$$ (s_1+s_3+s_4)+(-s_6-s_5-s_3)=s_1+s_4-s_5.$$
For inertia $(4,2)$ without padding, its right side is $a_2+a_3+a_4=A_2$. This gives the representative inequality $s_1+s_4-s_5\ge A_2$ with the complete Horn/Pieri data.

The triple $(\mathrm{Pi})_i$ is not of Lidskii–Wielandt type (neither $I$ nor $J$ is an initial segment $(1..r)$). Its membership in Fulton's recursively defined $T^d_r$ was checked directly for $d\le 8$ (author's generator) and $d\le 9$ (reviewer's independent generator), and $c=1$ for $d\le12$ by both LR implementations. Several Horn triples share the $s$-form $s_{i-1}+s_{i+2}-s_{d-1}$ — for instance the Lidskii–Wielandt triple $I=K=\{i-1,i+2\}$, $J=(1,2)$, whose right side is only $\lambda_{i-1}+\lambda_{i+2}$; the exhaustive enumeration of $T^d_r$ in `pieri_triples_search.py` lists all of them for $d\le9$ ($6$; $12,40$; $32,24$; $94,48,160$ triples for $d=6,\dots,9$ and $i=2,4,\dots$) and confirms that $(\mathrm{Pi})_i$ is the only one whose right side is $A_i$. That a triple outside the Lidskii–Wielandt family is genuinely needed is visible in the linear program: restricted to the Lidskii–Wielandt-type triples ($I=K$, $J=(1..r)$ or $J=K$, $I=(1..r)$, which include all Weyl inequalities), the Horn LP (2.1) falls short of $\Phi$ by up to $11\%$ at $G$-chamber points in $d=6,7$ (same script, floating-point HiGHS).

### 4.2 Certificates

A *certificate* for a form is a list of the inequalities above whose sum has every $s_t$-coefficient at most $1$ on the left and exactly the form on the right. Since $\sum_{t<d}s_t$ minus the certificate's left side is a nonnegative combination of the $s_t$, every feasible $s$ then has cost $\ge$ the form.

**Proposition 4.4 (certificate for $F_k$).**

- $k=0$: add $\Pi_1,\Pi_3,\Pi_5,\dots$, ending with $s_m\ge a_m$ if $m$ is odd. The sum is $\sum_{t\le m}s_t-Ns_{d-1}\ge A_1+A_3+\dots=F_0$, $N$ the number of $\Pi$'s.
- $k\ge1$: add $[s_1\ge b_1]$, $T_2,\dots,T_k$, and $\Pi_{k+1},\Pi_{k+3},\dots$, ending with $s_m\ge a_m$ if $m-k$ is odd. The sum is $\sum_{t\le m}s_t-Ns_{d-1}\ge b_1+\sum_{j=2}^k(A_j-b_2)+\sum_{t\ge k+1,\ t-k\text{ odd}}A_t=F_k$.

Each index $1,\dots,m$ occurs exactly once, no index above $m$ occurs with positive coefficient, and $\sum_{t<d}s_t=[\text{left side}]+\sum_{m<t<d}s_t+Ns_{d-1}\ge F_k$.

**Proposition 4.5 (certificate for $G_j$, $j$ odd).** Add $[s_2\ge b_2]$, $(\mathrm{Pi})_i$ for every even $i<j$, then $B_j$ (replaced by $s_j\ge a_j$ if $j+2>m$), then $\Pi_{j+3},\Pi_{j+5},\dots$ (the last replaced by $s_m\ge a_m$ if needed). The indices used are $2$; $\{1,4\},\{3,6\},\dots,\{j-2,j+1\}$; $\{j,j+2\}$; $\{j+3,j+4\},\dots$ — each of $1,\dots,m$ at most once — and the sum is
$$\sum_{t\le m}s_t\ (+\,s_{m+1})\ -Ns_{d-1}\ \ge\ b_2+\sum_{i\text{ even}<j}A_i+a_j+A_{j+2}+\sum_{i\text{ even}\ge j+3}A_i=G_j .$$
The term $+s_{m+1}$ is present exactly when $j=m$ is odd and $z\ge1$: it comes from $(\mathrm{Pi})_{m-1}$, whose $s_{i+2}=s_{m+1}$ collapses against $-s_{d-1}$ only when $z=0$. It is harmless for the lower bound (the coefficient is still $\le1$), but it matters for rigidity (Section 7).

*Proof of both propositions.* Direct addition; the index bookkeeping is as displayed and the right sides are the tail-sum forms of Theorem A. The tail-sum and closed forms coincide: expanding $A_j-b_2=b_1-(a_1+\dots+a_{j-1})$ in $F_k$ gives coefficient $-(k-i)=i-k$ for $a_i$, $i\le k$, and $\#\{t\in[k+1,i]:t-k\text{ odd}\}=\lceil (i-k)/2\rceil$ for $i\ge k$; the count for $G_j$ is similar (verified symbolically for $m\le9$ in `symbolic.py`). $\square$

**Corollary 4.6.** $\kappa_d(F)\ge\Phi(a;b)$ for all $m\ge2$, $z\ge0$.

*Proof.* Let $C$ be feasible with common spectrum $s$ (not necessarily $s_d=0$). The shifted pair $R-s_d\mathbf 1$, $-(S-s_d\mathbf 1)$ has spectra $\alpha,\beta$ built from $s'=s-s_d$ with $s'_d=0$ and sums to $F$, so all inequalities of 4.1 hold for $s'$, and $\tfrac12\|C\|^2=\sum_{t\le d}s_t\ge\sum_{t<d}s'_t\ge$ every form. $\square$

### 4.3 Write-outs for $m=4$

The reviewer's independent re-derivation (`my_cert.py`, own Fulton generator and own LR coefficients by the bialternant formula) produced all $168$ certificates for $m\le7$, $z\in\{0,1,2,5\}$; the case $m=4$ at $z=0,1,5$ ($d=6,7,11$) reads as follows, $b_1$ eliminated via $b_1=P-b_2$.

$F_2$:

| inequality | $(I;J;K)$ | $s$-form | right side |
|----|--------------|-------|---------|
| $s_1\ge b_1$ | $(1..d{-}1;\,1..d{-}1;\,1..d{-}1)$ | $s_1$ | $a_1+a_2+a_3+a_4-b_2$ |
| $T_2$ | $(2..d{-}1;\,1..d{-}2;\,2..d{-}1)$ | $s_2$ | $a_2+a_3+a_4-b_2$ |
| $\Pi_3$ | $(3..d{-}2;\,1..d{-}4;\,3..d{-}2)$ | $s_3+s_4-s_{d-1}$ | $a_3+a_4$ |
| sum | | $s_1+s_2+s_3+s_4-s_{d-1}$ | $a_1+2a_2+3a_3+3a_4-2b_2=F_2$ |

For $d=6,7,11$ the three $\Pi_3$ triples are $((3,4);(1,2);(3,4))$, $((3,4,5);(1,2,3);(3,4,5))$ and $((3..9);(1..7);(3..9))$.

$G_3$:

| inequality | $(I;J;K)$ | $s$-form | right side |
|----|--------------|-------|---------|
| $s_2\ge b_2$ | $(1..d{-}1;\ 1..d{-}2,d;\ 1..d{-}2,d)$ | $s_2$ | $a_1+a_2+a_3+a_4-b_1$ |
| $(\mathrm{Pi})_2$ | $(1,3..d{-}2;\ 1..d{-}4,d{-}2;\ 2..d{-}2)$ | $s_1+s_4-s_{d-1}$ | $a_2+a_3+a_4$ |
| Weyl | $(3;1;3)$ | $s_3$ | $a_3$ |
| sum | | $s_1+s_2+s_3+s_4-s_{d-1}$ | $b_2+a_2+2a_3+a_4=G_3$ |

For $d=6,7,11$ the Pieri triples are $((1,3,4);(1,2,4);(2,3,4))$, $((1,3,4,5);(1,2,3,5);(2,3,4,5))$ and $((1,3,\dots,9);(1,\dots,7,9);(2,\dots,9))$. In all cases the only index above $m=4$ is $d-1$ with coefficient $-1$. The Weyl row is the Lidskii–Wielandt instance $I=K=\{3\}$, $J=\{1\}$ of Lemma 4.1, as in the reviewer's listing `my_cert.log` (version 1 misprinted it as $(3;3;3)$, which is not a Horn triple: $3+3\ne3+1$).

Each certificate is an exact dual-feasible vector of the program (2.1) (all multipliers $1$ in $s$-units, $1/2$ in the $p$-units of [FourLevel]) with dual objective equal to the form; together with the primal points of Section 5 this shows that the LP value equals the form at every point of its chamber without any floating-point computation. The certificates coincide with the HiGHS dual solutions extracted by `horn_duals_pad.py`.

## 5. Upper bound: $2\times2$-block weighted shifts

### 5.1 The construction

Partition the nonzero spectrum (optionally together with some zeros) into ordered *layers* $\Lambda_0,\Lambda_1,\dots,\Lambda_T$ of size $1$ or $2$, with $\Lambda_0$ nonpositive and $\Lambda_T$ nonnegative, and let $D_t=\operatorname{diag}\Lambda_t$. Take $C=\sum_{t=1}^TM_t$ block-bidiagonal with $M_t:\Lambda_{t-1}\to\Lambda_t$. Then $CC^*=\bigoplus_tM_tM_t^*=:\bigoplus 2R_t$ (with $R_t$ on $\Lambda_t$) and $C^*C=\bigoplus_tM_t^*M_t=:\bigoplus 2S_t$ ($S_t$ on $\Lambda_{t-1}$), so $CC^*-C^*C=2F$ iff
$$\begin{gathered}S_1=-D_0,\\  R_t-S_{t+1}=D_t\ (1\le t<T),\\  R_T=D_T,\\  R_t\ \text{and}\ S_t\ \text{have the same nonzero spectrum}.\end{gathered}\tag{5.1}$$
Conversely, given PSD $R_t,S_t$ with equal nonzero spectra, $M_t=V\sqrt{2\Sigma}W^*$ realises them. The cost is
$$\tfrac12\|C\|^2=\sum_{t=1}^T\operatorname{Tr}S_t=\sum_{t=1}^T\Big(-\sum_{u<t}\operatorname{Tr}D_u\Big),$$
a sum of layer partial sums — the block analogue of the excursion cost of [RankAdaptive]. With singleton layers only this is the weighted shift of [RankAdaptive,OneSpike]. Eigenvalues of $F$ (zeros) not placed in any layer are left outside: $C$ vanishes on their span, which lies in $\ker C\cap\ker C^*$, and (5.1) on the layers is then equivalent to $CC^*-C^*C=2F$ on all of $\mathbb C^d$. We use three families of layerings:

- $\mathcal L(F_0)$: $\{-b_1,-b_2\},\{a_1,a_2\},\{a_3,a_4\},\dots$;
- $\mathcal L(F_k)$, $k\ge1$: $\{-b_1\},\{a_1\},\dots,\{a_{k-1}\},\{a_k,-b_2\},\{a_{k+1},a_{k+2}\},\dots$;
- $\mathcal L(G_j)$, $j$ odd: $\{-b_2\}$ followed by the consecutive pairs of $(a_0,a_1,\dots,a_m)$, $a_0:=-b_1$, with $a_j$ and $a_{j+1}$ transposed: $\{-b_1,a_1\},\{a_2,a_3\},\dots,\{a_{j-3},a_{j-2}\},\{a_{j-1},a_{j+1}\},\{a_j,a_{j+2}\},\{a_{j+3},a_{j+4}\},\dots$ (for $j=1$: $\{-b_1,a_2\},\{a_1,a_3\},\{a_4,a_5\},\dots$; for $j=m$: the pairs of $(a_0,\dots,a_{m-2})$ followed by $\{a_{m-1}\},\{a_m\}$).

A trailing odd element forms a singleton layer. The layer partial sums are $A_1,A_3,\dots$ for $\mathcal L(F_0)$; $b_1,\ A_2-b_2,\dots,A_k-b_2,\ A_{k+1},A_{k+3},\dots$ for $\mathcal L(F_k)$; and $b_2,\ A_2,A_4,\dots,A_{j-1},\ a_j+A_{j+2},\ A_{j+3},A_{j+5},\dots$ for $\mathcal L(G_j)$. Hence $\mathrm{cost}(\mathcal L(X))=X$ for each form $X$ (tail-sum form; verified symbolically for $m\le9$). In all three families $\operatorname{rank}C=\sum_t\operatorname{rank}R_t\le m$.

### 5.2 Feasibility as an interval recursion

**Lemma 5.0 (feasibility depends only on the spectra of the $S_t$).** Fix a layering. By (5.1) the traces are forced, $\operatorname{Tr}S_t=-\sum_{u<t}\operatorname{Tr}D_u$ and $\operatorname{Tr}R_t=\operatorname{Tr}S_t$, and $R_t$ may be *any* PSD matrix on $\Lambda_t$ with the nonzero spectrum of $S_t$ (given $S_t=W\Sigma W^*$ and such an $R_t=V\Sigma V^*$, $M_t=V\sqrt{2\Sigma}W^*$ realises the pair); in particular $\operatorname{rank}S_t\le|\Lambda_t|$ is necessary. Hence the set of matrices $S_{t+1}=R_t-D_t\succeq0$ attainable at step $t$ depends on the past only through the spectrum of $S_t$, and for a two-element layer $\Lambda_{t-1}$ the only free datum is the smaller eigenvalue $\sigma_2(S_t)$ (the larger one is $\operatorname{Tr}S_t-\sigma_2$). A layering is feasible iff the recursion of Lemmas 5.1–5.2, started at $\Lambda_0$, has a nonempty set of attainable $\sigma_2$ at every layer and meets the terminal condition at $\Lambda_T$; and because Lemma 5.2 is exact in both directions, every value in each attainable interval is realised by some solution of (5.1) — this is used in Section 7.

**Lemma 5.1 (step lemma).** Let $R\succeq0$ be $2\times2$ with eigenvalues $\sigma_1\ge\sigma_2$ and $D=\operatorname{diag}(\delta,\delta')$, $\delta\ge\delta'$. With $\tau_1\ge\tau_2$ the eigenvalues of $R-D$, $\tau_1+\tau_2=\sigma_1+\sigma_2-\delta-\delta'$ and, as the eigenbasis of $R$ rotates, $\tau_2$ takes exactly the values in $[\sigma_2-\delta,\ \min(\sigma_1-\delta,\sigma_2-\delta')]$.

*Proof.* With $R$ the rotation of $\operatorname{diag}(\sigma_1,\sigma_2)$ by angle $\theta$ and $x=\cos^2\theta$,
$$\det(R-D)=(\sigma_2-\delta)(\sigma_1-\delta')+(\sigma_1-\sigma_2)(\delta-\delta')\,x,$$
affine and nondecreasing in $x\in[0,1]$; the trace is fixed, so $\tau_2=\tfrac12(\tau-\sqrt{\tau^2-4\det})$ is continuous and monotone in $x$ and ranges over the interval between its values at $x=0$ (eigenvalues $\sigma_2-\delta,\sigma_1-\delta'$) and $x=1$ (eigenvalues $\sigma_1-\delta,\sigma_2-\delta'$). The endpoints are the three Weyl bounds. $\square$

Track, for each layer, the *state* $(\operatorname{Tr},[lo,hi])$: the trace of $S_t$ (forced: $\operatorname{Tr}S_t=-\sum_{u<t}\operatorname{Tr}D_u$) and the set of attainable second eigenvalues $\sigma_2$ of $S_t$ (a $2\times2$ matrix when $|\Lambda_{t-1}|=2$; we always have $lo\le hi\le\operatorname{Tr}/2$).

**Lemma 5.2 (interval recursion).** If $\sigma_2$ ranges over $[lo,hi]$ and the next layer is the pair $\{\delta\ge\delta'\}$, the set of attainable $\tau_2\ge0$ for $S_{t+1}=R_t-D_t$ is the interval
$$[lo',hi']=\Big[\max(0,\,lo-\delta),\ \min\big(hi-\delta',\ \operatorname{Tr}-\delta-lo,\ (\operatorname{Tr}-\delta-\delta')/2\big)\Big],$$
and the layer is feasible iff $lo'\le hi'$. Transitions with singletons: $\Lambda_0=\{-b\}$ gives state $(b,[0,0])$ and $\Lambda_0=\{-b_1,-b_2\}$ gives $(b_1+b_2,[b_2,b_2])$; a singleton $\{\delta\}$ after a pair requires $0\in[lo,hi]$ (rank-one $S_t$) and leads to the scalar $\operatorname{Tr}-\delta\ge0$, whose successor pair starts from $[0,0]$; the last layer $\{\delta,\delta'\}$ requires $\delta'\in[lo,hi]$, and a last singleton is automatic given the trace.

*Proof.* For fixed $\sigma=\sigma_2$ the fibre is $[\max(0,\sigma-\delta),\min(\operatorname{Tr}-\delta-\sigma,\sigma-\delta')]$ by Lemma 5.1, nonempty iff $\sigma\in[\delta',\operatorname{Tr}-\delta]$. Over the effective domain $[\max(lo,\delta'),\min(hi,\operatorname{Tr}-\delta,\operatorname{Tr}/2)]$ the endpoints vary continuously and the fibres are nonempty, so their union is an interval; its lower end is $\max(0,lo-\delta)$ (as $\delta'\le\delta$) and its upper end is the maximum of the concave function $\sigma\mapsto\min(\operatorname{Tr}-\delta-\sigma,\sigma-\delta')$ over the domain, which is the minimum of the three displayed quantities. If $lo'\le hi'$ then $hi'\ge0$ forces $hi\ge\delta'$, $lo\le\operatorname{Tr}-\delta$ and $\delta'\le\operatorname{Tr}-\delta$, so the effective domain is nonempty and the formula is exact. The singleton rules are the rank-one cases of (5.1). $\square$

The recursion is implemented exactly (rational arithmetic) in `layer_chain.feasible` and, independently with the explicit domain intersection, in the reviewer's `my_construct.forward`; the two agree on all $2708$ boundary-heavy exact points of `adversarial.py`.

**Lemma 5.3 (pair chains from $lo=0$).** Consider a state $(\operatorname{Tr},[0,h])$ followed by pair layers $\{\delta_1\ge\delta'_1\},\dots,\{\delta_q\ge\delta'_q\}$ of nonnegative numbers, possibly followed by singleton layers of nonnegative numbers, with $\operatorname{Tr}$ the total of all these layers. The chain is feasible iff $h\ge\sum_{i=1}^q\delta'_i$.

*Proof.* Since $lo=0$ propagates ($\max(0,0-\delta)=0$), write $h_1=h$ and $h_{i+1}=\min(h_i-\delta'_i,\ \operatorname{Tr}_i-\delta_i,\ (\operatorname{Tr}_i-\delta_i-\delta'_i)/2)$, $\operatorname{Tr}_i$ the trace before pair $i$. Let $N_i=\sum_{i'\ge i}\delta'_{i'}$. If $h_i\ge N_i$ then $h_{i+1}\ge N_{i+1}$: the first term by hypothesis; $\operatorname{Tr}_i-\delta_i$ is the sum of everything after $\delta_i$, which contains all later $\delta'$; and $(\operatorname{Tr}_i-\delta_i-\delta'_i)/2\ge N_{i+1}$ because the later layers contain, besides the $\delta'_{i'}$, the $\delta_{i'}\ge\delta'_{i'}$. Hence all $h_i\ge0$, and the terminal condition ($\delta'_q\in[0,h_q]$ for a pair end, $h_{q+1}\ge0$ for a singleton end) holds. Conversely $h_{i+1}\le h_i-\delta'_i$ gives $h_q\le h-\sum_{i<q}\delta'_i$, so the terminal condition forces $h\ge N_1$. $\square$

### 5.3 Closed-form feasibility regions

**Proposition 5.4.** Inside the stratum ($0<b_2\le b_1$):

1. $\mathcal L(F_k)$, $k\ge1$, is feasible iff $E_{k+2}\le b_2\le E_{k+1}$.
2. $\mathcal L(G_j)$ is feasible iff $b_2\ge E_1-g_j$; inside the stratum this forces $g_j=g^*$.
3. $\mathcal L(F_0)$ is feasible iff $E_2\le b_2\le E_1-g^*$.

*Proof of 1.* The singleton chain $\{-b_1\},\{a_1\},\dots,\{a_{k-1}\}$ has scalars $b_1,\ b_1-a_1,\dots,\ A_k-b_2$, nonnegative iff $b_2\le A_k$. The mixed layer $\{a_k,-b_2\}$ ($\delta=a_k$, $\delta'=-b_2$) starts from $(A_k-b_2,[0,0])$ and by Lemma 5.2 yields $(A_{k+1},[0,h])$ with $h=\min(b_2,\ A_{k+1}-b_2,\ A_{k+1}/2)=\min(b_2,A_{k+1}-b_2)$. The remaining pairs $\{a_{k+1},a_{k+2}\},\dots$ have $\sum\delta'=E_{k+2}$, so by Lemma 5.3 the layering is feasible iff $\min(b_2,A_{k+1}-b_2)\ge E_{k+2}$, i.e. iff $E_{k+2}\le b_2\le A_{k+1}-E_{k+2}=E_{k+1}$; this implies $b_2\le A_k$, so the singleton chain is nonnegative whenever the whole layering is feasible. Boundary cases: for $k=m-1$ there is no pair after the mixed layer, only the singleton $\{a_m\}$, and Lemma 5.3 with $q=0$ gives feasibility iff $h\ge0$, i.e. iff $b_2\le A_m=E_m$, in agreement with $E_{m+1}=0$; when $m-k$ is odd the chain ends with the singleton $\{a_m\}$, covered by Lemma 5.3. (When $b_2=A_{k+1}/2$ the third term of the recursion, not the second, is the binding one after the first pair; it never causes infeasibility, which is all that is needed.)

*Proof of 2.* Let $j\ge3$. After $\{-b_2\}$ the state is $(b_2,[0,0])$; the pair $\{-b_1,a_1\}$ ($\delta=a_1$, $\delta'=-b_1$) gives $(A_2,[0,h])$ with $h=\min(b_1,\ b_2-a_1,\ (P-a_1)/2)=b_2-a_1$, the other two terms being dominated because $b_2\le b_1$. The later pairs have $\delta'$-values $a_3,a_5,\dots,a_{j-2},\ a_{j+1},\ a_{j+2},\ a_{j+4},\dots$, which sum to $E_3-(a_j-a_{j+1})=E_3-g_j$ (for $j=m$ the trailing $\{a_{m-1}\},\{a_m\}$ are singletons and the sum is $E_3-a_m$). The tail of the chain is: for $m$ odd and $j\le m-2$, pairs only (the last pair is $\{a_{m-1},a_m\}$); for $m$ even and $j\le m-3$, pairs followed by the singleton $\{a_m\}$; for $j=m-1$ ($m$ even), the pairs end with $\{a_{m-2},a_m\}$ and the singleton $\{a_{m-1}\}$ follows; for $j=m$ ($m$ odd), the pairs end with $\{a_{m-3},a_{m-2}\}$ and the two singletons $\{a_{m-1}\},\{a_m\}$ follow (the scalar after the first singleton is $a_m\ge0$, the last singleton is automatic). In each case the $\delta'$-sum is $E_3-g_j$ as displayed, the layer entries are nonnegative and the trace is the total, so Lemma 5.3 applies: feasible iff $b_2-a_1\ge E_3-g_j$, i.e. $b_2\ge E_1-g_j$. For $j=1$ the first pair is $\{-b_1,a_2\}$, $h=\min(b_1,\ b_2-a_2,\ (P-a_2)/2)=b_2-a_2$ by the same argument, the later $\delta'$-sum is $E_3$, and the condition is $b_2\ge a_2+E_3=E_1-g_1$ (for $m=2$ the tail is the single singleton $\{a_1\}$ and $E_3=0$). Finally $E_1-g_j\le b_2\le P/2=(E_1+E_2)/2$ gives $\sum_{j'\ne j}g_{j'}<g_j$ or equality, so $g_j=g^*$.

*Proof of 3.* The initial state is $(A_1,[b_2,b_2])$ (this uses $b_2\le b_1$). Let $(A_{2t+1},[lo_t,hi_t])$ be the state before the pair $\{a_{2t+1},a_{2t+2}\}$. By Lemma 5.2, $lo_t=\max\big(0,\ b_2-(a_1+a_3+\dots+a_{2t-1})\big)$ and
$$hi_t=\min\left\{\begin{gathered}b_2-(a_2+\dots+a_{2t}),\\ A_{2r}-lo_{r-1}-(a_{2r+2}+\dots+a_{2t}),\\ \tfrac12A_{2r+1}-(a_{2r+2}+\dots+a_{2t})\ \ (1\le r\le t)\end{gathered}\right\}.$$
*Induction for the displayed endpoints.* Empty sums are zero, and all dotted sums above advance by two. At $t=0$ the minimum contains only $b_2$, so $lo_0=hi_0=b_2$. Applying Lemma 5.2 to the next nonterminal pair gives
$$\begin{aligned}
lo_{t+1}&=\max(0,lo_t-a_{2t+1}),\\
hi_{t+1}&=\min\{hi_t-a_{2t+2},\ A_{2t+2}-lo_t,\ \tfrac12 A_{2t+3}\}.
\end{aligned}$$
The first identity proves the formula for $lo_{t+1}$. Subtracting $a_{2t+2}$ from every candidate in $hi_t$ appends that term to each even-indexed tail sum; the other two candidates are precisely the displayed terms with $r=t+1$ and an empty tail. This proves the closed form by induction at every retained state. Equivalently the formulas can be unfolded algebraically before testing feasibility; the terminal and intermediate checks below show that none of the required intervals is empty on the stated region.

*Terminal conditions.* For $m$ even the last layer is the pair $\{a_{m-1},a_m\}$ and requires $lo_{q-1}\le a_m\le hi_{q-1}$, $q=m/2$; for $m$ odd the last layer is the singleton $\{a_m\}$ and requires $lo_q=0\le hi_q$, $q=(m-1)/2$. The $lo$ condition is $b_2\le a_1+a_3+\dots+a_{m-3}+a_m=E_1-g_{m-1}$ ($m$ even) or $b_2\le a_1+\dots+a_{m-2}=E_1-g_m$ ($m$ odd). In the $hi$ condition the first term gives $b_2\ge E_2$; the $r$-th middle term gives, after simplifying $A_{2r}-(a_{2r+2}+a_{2r+4}+\dots)=a_{2r}+E_{2r+1}$, the condition $b_2\le a_1+a_3+\dots+a_{2r-3}+a_{2r}+E_{2r+1}=E_1-g_{2r-1}$ for $j=2r-1=1,3,\dots$ ($r\le q-1$ for $m$ even, $r\le q$ for $m$ odd); the third terms are automatic since $A_{2r+1}=E_{2r+1}+E_{2r+2}\ge2E_{2r+2}$. Together the terminal conditions are exactly $E_2\le b_2\le E_1-g_j$ for every odd $j\le m$, and they are necessary.
*Intermediate conditions.* $lo_t\le hi_t$ for $t$ before the terminal index. If $lo_t=0$ each term of $hi_t$ exceeds the corresponding terminal term, so the terminal conditions suffice. If $lo_t=b_2-(a_1+\dots+a_{2t-1})>0$ then also $lo_{r-1}>0$ for $r\le t$ ($lo$ is nonincreasing), and the three conditions become: for the first term, $a_1+a_3+\dots+a_{2t-1}\ge a_2+\dots+a_{2t}$, automatic; for the middle term with index $r$, after substituting $lo_{r-1}$,
$$A_{2r}-(a_{2r+2}+\dots+a_{2t})+(a_1+\dots+a_{2r-3})+(a_1+\dots+a_{2t-1})\ \ge\ 2b_2,$$
whose left side minus $P$ equals $\sum_{i<r}(a_{2i-1}-a_{2i})+\sum_{i=r}^{t-1}(a_{2i+1}-a_{2i+2})\ge0$, so it holds because $2b_2\le P$; for the third term, put $O_t=\sum_{i=1}^t a_{2i-1}$. Since $A_{2r+1}=P-\sum_{i=1}^r(a_{2i-1}+a_{2i})$, the exact identity is
$$\begin{aligned}
\frac12A_{2r+1}-\sum_{i=r+1}^t a_{2i}+O_t-b_2
&=\frac P2-b_2+\frac12\sum_{i=1}^r(a_{2i-1}-a_{2i})\\
&\quad+\sum_{i=r+1}^t(a_{2i-1}-a_{2i})\ \ge0.
\end{aligned}$$
The first term is nonnegative because $P=b_1+b_2$ and $b_1\ge b_2$; the remaining differences are nonnegative by the ordering of the $a_i$. Empty sums are zero, so this includes $r=t$ and all equality cases. Thus the third candidate for $hi_t$ is at least $lo_t=b_2-O_t$. Thus the intermediate conditions in the case $lo_t>0$ are consequences of the stratum condition $b_2\le b_1$ and not of the terminal conditions alone; on the stratum they are harmless. (For $m=2$ there is no intermediate step: the single pair $\{a_1,a_2\}$ is terminal and requires $b_2=lo_0\le a_2\le hi_0=b_2$, i.e. $b_2=a_2=E_2=E_1-g_1$, the degenerate $F_0$ region.) $\square$

All three regions were re-derived independently by the reviewer's recursion (`my_construct.forward`) and are checked against the exact recursion on a fine rational grid with every tie and boundary case, $m\le10$ (`coverage_exact.py`, Section 9).

**Proposition 5.5 (coverage).** For every $(a,b)$ in the stratum some layering is feasible, and its cost is $\Phi(a;b)$.

*Proof.* Since $E_{m+1}=0<b_2$: if $b_2\le E_2$ then $k^*=\max\{k\ge1:E_{k+1}\ge b_2\}\le m-1$ exists and $E_{k^*+2}\le b_2\le E_{k^*+1}$, so $\mathcal L(F_{k^*})$ is feasible; if $E_2\le b_2\le E_1-g^*$, $\mathcal L(F_0)$ is feasible; if $b_2\ge E_1-g^*$, $\mathcal L(G_{j^*})$ is feasible. The three intervals cover $(0,\infty)$ because $E_2\le E_1-g^*$. The cost of the feasible layering is its form, which is $\le\Phi\le\kappa_d$ by Corollary 4.6, while the layering shows $\kappa_d\le$ its cost. $\square$

*Proof of Theorem A.* Corollary 4.6 and Proposition 5.5 give $\kappa_d=\Phi$ in $d=m+z+2$ for every $z$; neither depends on $z$. The $(2,n)$ case follows from $\kappa_d(-F)=\kappa_d(F)$. $\square$

Because the regions in Proposition 5.4 are exact (both directions), the feasibility region of each layering coincides with the chamber of its form in Theorem B, and exactly the argmax layerings are feasible at every point — a fact checked at $400$ exact points per $m\le8$, $300$ per $m\le13$, and at $9567$ grid points for $m\le10$ that include every breakpoint $E_k$, $E_1-g_j$, $b_1=b_2$, flat and tied spectra (`coverage_exact.py`). The end-to-end construction of $C$ (backward choice of the $\sigma_2$'s, rotation angles from the affine determinant, SVD blocks) gives residuals $\|CC^*-C^*C-2F\|$ and $|\tfrac12\|C\|^2-\Phi|$ at the $10^{-14}$ level away from tie points and $\le2\cdot10^{-8}$ at exact ties, with $\operatorname{rank}C=m$.

## 6. Chambers and exposedness: proof of Theorem B

From the tail-sum forms, $F_1-F_0=b_1-E_1=E_2-b_2$ and, for $k\ge2$, $F_k-F_{k-1}=(A_k-b_2)+\sum_{t\ge k+1,\,t-k\text{ odd}}A_t-\sum_{t\ge k,\,t-k\text{ even}}A_t=-b_2+a_{k+1}+a_{k+3}+\dots=E_{k+1}-b_2$. Since $E_{k+1}$ is nonincreasing in $k$, $k\mapsto F_k$ increases while $E_{k+1}\ge b_2$ and decreases afterwards: unimodal with maximum at $k^*$ when $b_2\le E_2$ and at $k=0$ when $b_2\ge E_2$. From the closed forms $G_j-G_{j'}=g_j-g_{j'}$, and since $F_0=\sum_i\lceil i/2\rceil a_i=\sum_i\lfloor i/2\rfloor a_i+E_1$, $G_j-F_0=b_2-E_1+g_j$. Hence for $b_2\le E_2$ the maximum is $F_{k^*}$ (as $E_2\le E_1-g^*$ gives $F_0\ge G_j$ for all $j$); for $E_2\le b_2\le E_1-g^*$ it is $F_0$; for $b_2\ge E_1-g^*$ it is $G_{j^*}$. This proves the chamber description.

*Exposedness.* $F_k$ ($1\le k\le m-1$) is the unique maximiser on the open interval $E_{k+2}<b_2<E_{k+1}$: there $F_{k'}-F_{k'-1}=E_{k'+1}-b_2$ is $>0$ for $k'\le k$ and $<0$ for $k'>k$, and $F_0>G_j$ for every $j$ because $b_2<E_2\le E_1-g_j$. The interval lies inside the stratum because $E_{k+1}\le E_2\le P/2$, and it is nonempty iff $E_{k+1}>E_{k+2}$. Here the correct alternating-sum identities are $E_{k+1}-E_{k+3}=a_{k+1}$ and $E_{k+1}-E_{k+2}=(a_{k+1}-a_{k+2})+(a_{k+3}-a_{k+4})+\cdots$, the last term being $a_m>0$ when $m-k$ is odd (version 1 wrote $E_{k+1}-E_{k+2}=a_{k+1}$, which is false: for $a=(4,3,2,1)$ and $k=1$, $E_2-E_3=2\ne a_2=3$). So the open $F_k$ chamber is nonempty whenever $a_{k+1}>a_{k+2}$ or $m-k$ is odd, and empty exactly when $m-k$ is even and every pair satisfies $a_{k+1+2t}=a_{k+2+2t}$ for $0\le t<(m-k)/2$; an exposing point exists for every $k$, e.g. for $a=(m,m-1,\dots,1)$, where $E_{k+1}-E_{k+2}\ge1$. $F_0$ is the unique maximiser on $E_2<b_2<E_1-g^*$, nonempty iff $\sum_{j\text{ odd}}g_j>g^*$, i.e. iff at least two odd gaps are positive, possible iff $m\ge3$; for $m=2$, $E_2=E_1-g_1=a_2$ and at that point $F_0=F_1=G_1$, so $F_0$ is never a unique maximiser (indeed $F_0\le\max(F_1,G_1)$ since $F_0-F_1=b_2-a_2$ and $F_0-G_1=a_2-b_2$). $G_j$ is the unique maximiser when $b_2>E_1-g_j$ and $g_j>g_{j'}$ for $j'\ne j$; a point with $E_1-g_j<b_2\le P/2$ exists iff $\sum_{j'\ne j}g_{j'}<g_j$, which is realised by $a_1=\dots=a_j=1$, $a_{j+1}=\dots=a_m=\varepsilon$ (all $a_i=1$ when $j=m$). This gives the count $(m-1)+\lceil m/2\rceil+[m\ge3]$; exact unique-argmax sampling ($20000$ rational points per $m$, `rank_more.py`) and the LP-dual counts in `forms_m*_pad*.json` return the same numbers $2,5,6,8,9,11,12,14$. $\square$

For example, $a=(4,3,3,1,1)$ and $k=1$ give $E_2=E_3=4$: the open $F_1$ chamber is empty although the tail $(3,3,1,1)$ is not constant. The corrected criterion follows because $E_{k+1}-E_{k+2}$ is a sum of nonnegative pair differences, plus the positive unpaired last term when $m-k$ is odd. It does not change the formula for the cost or the global count of exposed forms, which asserts existence over varying spectra.

*When are the $G$-forms active?* Since $G_{j^*}\ge F_0\iff b_2\ge E_1-g^*$ and $b_2\le P/2=(E_1+E_2)/2$ on the stratum, some $G_j$ attains $\Phi$ at some point of the stratum iff $E_1-g^*\le P/2$, i.e. iff $\sum_{j\ne j^*}g_j\le g^*$ (the largest odd gap is at least the sum of the others); a $G_j$ is the *unique* maximiser somewhere iff this inequality is strict. When it holds with equality, the $G$-forms are active exactly on the line $b_1=b_2$, where they tie with $F_0$: for $m=3$, $a=(2,1,1)$, $b_1=b_2=2$ one has $g_1=g_3=1$ and $F_0=G_1=G_3=5$. In particular, if all $\lceil m/2\rceil$ odd gaps are equal to some $g$: for $m\in\{3,4\}$ (two odd gaps) the $G$-forms are active only at $b_1=b_2$, tied with $F_0$; for $m\ge5$ and $g>0$ they are never active; and if $g=0$ ($m$ even, $a_{2i-1}=a_{2i}$ for all $i$) then $E_1=E_2=P/2$ and every $G_j$ ties with $F_0$ at $b_1=b_2$. Version 1 stated that the $G$-forms are never active when all odd gaps are equal and $m\ge3$; that statement omitted these tie cases.

## 7. Rank and uniqueness: proof of Theorem C$'$

**Inertia bound.** For any feasible $C$ and $x\in\ker C^*$, $\langle 2Fx,x\rangle=-\|Cx\|^2\le0$, so $F\preceq0$ on a subspace of dimension $d-\operatorname{rank}C$, whence $\operatorname{rank}C\ge n_+=m$; symmetrically $\operatorname{rank}C\ge n_-$. This is the inertia obstruction, Lemma 2.1 of [RankOnset].

**(1) and (2).** Let $C$ be an optimizer with common spectrum $s$. Then $\sum_{t\le d}s_t=\sum_{t<d}(s_t-s_d)+d\,s_d\ge\Phi+d\,s_d$ by Corollary 4.6 applied to $s-s_d$, so $s_d=0$. Let $X$ be any form attaining $\Phi$ and consider its certificate, whose left side is $L(s)=\sum_{t\in U}s_t-Ns_{d-1}$ with $U\subseteq\{1,\dots,m+1\}$ the indices used with coefficient $+1$ and $N\ge0$ the number of $-s_{d-1}$ terms (possibly $N=0$, e.g. for $F_{m-1}$). Then $\sum_{t<d}s_t-L(s)=\sum_{t<d,\ t\notin U}s_t+Ns_{d-1}\ge0$ and $L(s)\ge X=\Phi=\sum_{t<d}s_t$, so every coordinate $s_t$ with $t<d$, $t\notin U$ vanishes (and $s_{d-1}=0$ also when $N\ge1$). For every $F_k$ and every $G_j$ with $j<m$, and for $G_m$ with $z=0$, the used indices are $\subseteq\{1,\dots,m\}$ together with $-s_{d-1}$: hence $s_t=0$ for $m<t<d$ and $\operatorname{rank}C=m$. For $G_m$ with $m$ odd and $z\ge1$ the used indices are $\{1,\dots,m+1\}$ and $-s_{d-1}$ with $d-1\ge m+2$: hence $s_t=0$ for $m+2\le t\le d-1$, and $s_{m+1}$ is unconstrained by this argument. In all cases $d-1\notin U$ (as $d-1\ge m+1$, with equality only when $z=0$, where the $s_{m+1}$ term collapsed), so $s_{d-1}=0$ and $\operatorname{rank}C=\#\{t:s_t>0\}\in\{m,m+1\}$. If some form other than $G_m$ attains $\Phi$ its certificate forces $s_{m+1}=0$; this covers $m$ even, $z=0$, and every point where $G_m$ is not the unique maximiser, in particular $b_2\le E_1-a_m$ (where $G_m\le F_0$). The block construction has rank $m$, so $r_*=r_0=m$ in every $d$, extending the $d\le7$ certificate of [RankOnset] (Theorem 3.1 there) to the whole stratum. The two cases (2) and (3) are exhaustive: for $m$ odd and $z\ge1$, either $b_2\le E_1-a_m$, where $G_m\le F_0$ and (2) applies, or $b_2>E_1-a_m$, the open $G_m$ chamber of (3).

**(3) Rank-$(m+1)$ optimizers.** The preceding certificate leaves $s_{m+1}$ free in this case; the following construction determines whether positive values are attainable. Let $m$ be odd, $z\ge1$, and use the layering
$$\mathcal L'_m:\qquad \{-b_2\},\ \{-b_1,a_1\},\ \{a_2,a_3\},\ \dots,\ \{a_{m-3},a_{m-2}\},\ \{a_{m-1},0\},\ \{a_m\},$$
i.e. $\mathcal L(G_m)$ with one zero eigenvalue placed inside the penultimate layer; the remaining zeros are left outside (they span $\ker C\cap\ker C^*$). Its cost is still $G_m$. Number the layers $\Lambda_0=\{-b_2\}$, $\Lambda_1=\{-b_1,a_1\}$, $\dots$, $\Lambda_{T-1}=\{a_{m-1},0\}$, $\Lambda_T=\{a_m\}$, $T=(m+3)/2$. By Lemma 5.3 (the $\delta'$-values after the first pair are $a_3,\dots,a_{m-2},0$) it is feasible iff $b_2-a_1\ge E_3-a_m$, i.e. $b_2\ge E_1-a_m$, the closed $G_m$ region. Its rank is $\sum_t\operatorname{rank}R_t=\sum_t\operatorname{rank}S_t$, where $\operatorname{rank}S_1=\operatorname{rank}S_T=1$ ($S_1=b_2$; $S_T$ must have rank one because $\Lambda_T$ is a singleton) and $\operatorname{rank}S_t=1+[\sigma_2(S_t)>0]$ for $2\le t\le T-1$. For $2\le t\le T-2$ the layer $\Lambda_t$ following $S_t$ is a pair $\{a_{2t-2},a_{2t-1}\}$ with $\delta'_t=a_{2t-1}>0$, and the fibre of Lemma 5.2 is nonempty only when $\sigma_2(S_t)\ge\delta'_t>0$; so these $S_t$ have rank $2$ in every solution, and
$$\operatorname{rank}C=1+\sum_{t=2}^{T-2}2+\operatorname{rank}S_{T-1}+1=m+[\sigma_2(S_{T-1})>0],$$
where $S_{T-1}$ lives on $\{a_{m-3},a_{m-2}\}$ (on $\{-b_1,a_1\}$ when $m=3$). Its successor $\{a_{m-1},0\}$ is followed by the singleton $\{a_m\}$, which needs $\tau_2(S_T)=0$; from $\sigma_2(S_{T-1})=\sigma$ this is attainable iff $\sigma-a_{m-1}\le0\le\min(a_m-\sigma,\sigma)$ (Lemma 5.1 with $\operatorname{Tr}S_{T-1}=a_{m-1}+a_m$), i.e. iff $\sigma\in[0,a_m]$. So rank $m+1$ is attainable iff the upper end $h$ of the $\sigma_2$-interval of $S_{T-1}$ is positive, and $\sigma=0$ always gives rank $m$. When $b_2>E_1-a_m$ the induction of Lemma 5.3 runs with strict inequalities ($h_1>N_1$, and every later term exceeds $N_{i+1}$ by at least $a_m>0$ or by $\tfrac12(\sum(\delta-\delta')+a_m)>0$), so $h>N=0$. When $b_2=E_1-a_m$, $h\le h_1-\sum_{i<q}\delta'_i=(b_2-a_1)-(E_3-a_m)=0$, consistent with (2) since $G_m=F_0$ there. This proves (3); both directions are checked exactly on the grid of `coverage_exact.py` for odd $m\le9$.

**Example (the reviewer's counterexample to the original rank claim).** $\lambda=(2,2,\tfrac32,0,-\tfrac52,-3)$: $m=3$, $z=1$, $a=(2,2,\tfrac32)$, $b=(3,\tfrac52)$, $g_1=0$, $g_3=\tfrac32$, $E_1-g_3=2<b_2=\tfrac52\le b_1$. The forms are $F_0=7$, $F_1=\tfrac{13}2$, $F_2=\tfrac{11}2$, $G_1=6$, $G_3=\tfrac{15}2=\kappa_6$. The $G_3$ certificate is $[s_2\ge b_2]+(\mathrm{Pi})_2+[s_3\ge a_3]$, i.e. $s_2\ge\tfrac52$, $s_1+s_4-s_5\ge\tfrac72$, $s_3\ge\tfrac32$; every $s(t)=(\tfrac72-t,\tfrac52,\tfrac32,t,0,0)$, $0\le t\le\tfrac12$, makes all three tight with cost $\tfrac{15}2$. The endpoints $t=0,\tfrac12$ (and $t=\tfrac14$) satisfy all $522$ Horn inequalities of $d=6$ exactly (`rank_test.py`, `nonunique_check.py`, rational arithmetic, two independent Horn generators), hence so does every $t\in[0,\tfrac12]$ by convexity of the Horn polyhedron; the LP maximum of $s_4$ at cost $\tfrac{15}2$ is exactly $\tfrac12$. The layering $\mathcal L'_3=\{-\tfrac52\},\{-3,2\},\{2,0\},\{\tfrac32\}$ with $\sigma_2(S_2)=\tfrac14$ (the midpoint of the admissible interval $[0,\tfrac12]$) can be solved in closed form (`exact_rank4_matrix.py`): $R_1=\begin{pmatrix}p&q\\ q&\frac52-p\end{pmatrix}$ with $q^2=p(\frac52-p)$ is rank one, and $\det(R_1-D_1)=\frac{13}{16}$ forces $p=\frac{11}{80}$; $R_2=\begin{pmatrix}u&w\\ w&\frac72-u\end{pmatrix}$ with spectrum $\{\frac{13}4,\frac14\}$ and $\det(R_2-D_2)=0$ forces $u=\frac{99}{32}$, $w^2=\frac{455}{1024}$. In the basis ordered $(-b_2,-b_1,a_1,a_2,0,a_3)$ the resulting real matrix is
$$C=\begin{pmatrix}0&0&0&0&0&0\\[2pt] \frac{\sqrt{110}}{20}&0&0&0&0&0\\[2pt] \frac{3\sqrt{210}}{20}&0&0&0&0&0\\[2pt] 0&\frac{15+91\sqrt{165}}{480}&\frac{39\sqrt{35}-5\sqrt{231}}{480}&0&0&0\\[2pt] 0&\frac{5\sqrt{3003}-3\sqrt{455}}{480}&\frac{15\sqrt{13}+7\sqrt{2145}}{480}&0&0&0\\[2pt] 0&0&0&-\frac{\sqrt{35}}{4}&-\frac{\sqrt{13}}{4}&0\end{pmatrix},$$
numerically $C_{21}=0.5244$, $C_{31}=2.1737$, $C_{42}=2.4665$, $C_{43}=0.3224$, $C_{52}=0.4375$, $C_{53}=0.7881$, $C_{64}=-1.4790$, $C_{65}=-0.9014$. For this $C$, $CC^{\mathsf T}-C^{\mathsf T}C-2F=0$ *exactly* (verified symbolically), $\tfrac12\|C\|^2=\tfrac{15}2=\Phi$, $\operatorname{rank}C=4=m+1$, and the common spectrum is $(\tfrac{13}4,\tfrac52,\tfrac32,\tfrac14,0,0)$. The exact entries evaluated in double precision give residual $1.4\cdot10^{-15}$, and the floating-point construction of `my_construct.py` gives $4.8\cdot10^{-15}$; the four-decimal display alone gives $2.1\cdot10^{-4}$, so the full-precision entries (`repro/data/rank4_optimizer_exact.json` and `rank4_optimizer_30digits.txt`, 30 significant digits) are needed to reproduce the residual. The same construction gives rank-$(m+1)$ optimizers for $m=5,7$ with $z=1$ (`rank_more.py`, residuals $3\cdot10^{-15}$, $7\cdot10^{-15}$; e.g. $m=5$: $s=(2.7,2.4,1.7,1.2,0.9,0.2,0,0)$). For $z=0$ the same $\lambda$ without the zero has $(\mathrm{Pi})_2$ reading $s_1\ge A_2$ and every optimizer has rank $3$.

**(4) Uniqueness.** By Horn sufficiency the optimal common spectra are the points of the optimal face of (2.1). *$m=2$:* in the $F_1$ chamber ($b_2\le a_2$) the certificate is $[s_1\ge b_1]+[s_2\ge a_2]$ and tightness gives $s=(b_1,a_2,0,\dots)$; in the $G_1$ chamber ($b_2\ge a_2$) it is $[s_2\ge b_2]+[s_1\ge a_1]$, giving $s=(a_1,b_2,0,\dots)$; unique for all $z$. *$m=3$:* $F_2$ ($b_2\le a_3$): $s=(b_1,A_2-b_2,a_3,0,\dots)$. $F_1$ ($a_3\le b_2\le a_2$): $s_1=b_1$, $s_2+s_3=A_2=a_2+a_3$ with $s_4=\dots=0$; the Weyl inequalities $s_2\ge a_2$, $s_3\ge a_3$ pin $s=(b_1,a_2,a_3,0,\dots)$. $F_0$ ($a_2\le b_2\le E_1-g^*$): $s_1+s_2=P$, $s_3=a_3$; with $s_1\ge b_1$ and $s_2\ge b_2$ this pins $s=(b_1,b_2,a_3,0,\dots)$. $G_1$ ($b_2\ge a_2+a_3$): $s_2=b_2$, $s_1+s_3=a_1+a_3$, pinned by Weyl to $(a_1,b_2,a_3,0,\dots)$. $G_3$ with $z=0$: $s=(A_2,b_2,a_3,0,0)$. All these pinning inequalities hold in every $d$, so the optimal spectrum is unique for $m=3$ whenever $z=0$ or $b_2\le E_1-a_3$, and (3) shows non-uniqueness in the open $G_3$ chamber for $z\ge1$ (the family $s(t)$ above, or in general $(A_2-\sigma,b_2,a_3,\sigma,0,\dots)$ with $\sigma\in[0,\min(h,a_3)]$). *$m\ge4$:* take $k=m-3\ge1$ and a point of the open $F_{m-3}$ chamber $a_{m-1}=E_{m-1}<b_2<E_{m-2}=a_{m-2}+a_m$ with $a_{m-2}>a_{m-1}$. In $\mathcal L(F_{m-3})$ the layer after the mixed layer is the pair $\{a_{m-2},a_{m-1}\}$, followed by the singleton $\{a_m\}$. Its state is $(A_{m-2},[0,h])$ with $h=\min(b_2,A_{m-2}-b_2)>a_{m-1}$, and the singleton requires $\tau_2=0$, attainable from $\sigma_2=\sigma$ iff $\sigma\in[a_{m-1},\min(a_{m-2},a_{m-1}+a_m)]$. Every $\sigma\in[a_{m-1},\min(a_{m-2},a_{m-1}+a_m,h)]$, a nondegenerate interval, is attainable and gives an optimizer with common spectrum containing the pair $(A_{m-2}-\sigma,\sigma)$; distinct $\sigma$ give distinct spectra. (The corresponding $F_{m-3}$ certificate ends with $\Pi_{m-2}$ and $[s_m\ge a_m]$, whose tightness $s_{m-2}+s_{m-1}=A_{m-2}$ leaves exactly this one degree of freedom; the "free split" of a certificate alone does not prove non-uniqueness, the construction does.) For $m=4$, $a=(4,3,2,1)$, $b_2=\tfrac52$: $s=(\tfrac{15}2,6-\sigma,\sigma,1,0,0)$ is Horn-feasible for $\sigma=2,\tfrac94,\tfrac52$ (all $522$ inequalities, `nonunique_check.py`), cost $\tfrac{29}2=F_1$. LP scans find non-unique optimal spectra at $37/60$ random points for $m=4$, $z=0$ (active forms $F_1,G_1,G_3$; reviewer) and at $25/40$ ($m=4$) and $37/40$ ($m=6$) random points (author), at $3/80$ and $2/40$ points for $m=3$ with $z=1,2$ (all in the $G_3$ chamber), and never for $m=2$ or for $m=3$, $z=0$. $\square$

*Remark (quantifier).* "Every optimizer" refers to HS-optimizers of $\tfrac12\|C\|^2$ under $CC^*-C^*C=2F$. In the two-operator formulation $\inf\|A\|\|B\|$, unbalanced product optimizers $(sA,s^{-1}B)$ give $C=sA+is^{-1}B$ of larger rank already for $F=\operatorname{diag}(1,-1)$, as noted in the audit of [OneSpike]; the rank statements here are for the self-commutator formulation.

## 8. Consistency checks

**$m=2$ versus the four-level formula.** On $\lambda=(a_1,a_2,-b_2,-b_1)$: $\lambda_1-\lambda_3=a_1+b_2=G_1$, $\lambda_2-\lambda_4=a_2+b_1=F_1$, $\lambda_1-2\lambda_2-\lambda_3=G_1-2a_2$, $\lambda_2+2\lambda_3-\lambda_4=F_1-2b_2$, and $F_0=P\le\max(F_1,G_1)$ (Section 6). So $\Phi=\max(F_1,G_1)$ coincides identically with [FourLevel] Theorem 3.1; here $\kappa_4=\max(\lambda_1-\lambda_3,\lambda_2-\lambda_4)$.

**$m=3$ versus the twelve five-level terms.** The gap forms $q_1,\dots,q_6$ and their reversals of [FiveLevel] Theorem 3.1, written as spectral forms on $\lambda=(a_1,a_2,a_3,-b_2,-b_1)$, are (sympy, `symbolic.py`, `d5_dominated_terms.py`): five of them are our forms, $\rho q_5=\lambda_3-\lambda_4-\lambda_5=F_0$, $\rho q_2=\lambda_2+\lambda_3-\lambda_5=F_1$, $\rho q_4=-\lambda_1+\lambda_3-2\lambda_5=F_2$, $q_6=\lambda_1+\lambda_3-\lambda_4=G_1$, $\rho q_3=\lambda_2+2\lambda_3-\lambda_4=G_3$; the other seven are dominated termwise by a single form on the stratum, hence exactly:
$$\begin{aligned}
q_1&=2\lambda_1-2\lambda_2-\lambda_3+\lambda_5=G_1-3a_2-3a_3, & \rho q_1&=-\lambda_1+\lambda_3+2\lambda_4-2\lambda_5=F_2-2b_2,\\
q_2&=\lambda_1-\lambda_3-\lambda_4=G_1-2a_3, & q_3&=\lambda_2-2\lambda_3-\lambda_4=G_3-4a_3,\\
q_4&=2\lambda_1-\lambda_3+\lambda_5=G_1-a_2-3a_3, & q_5&=\lambda_1+\lambda_2-\lambda_3=F_0-3a_3,\\
\rho q_6&=\lambda_2-\lambda_3-\lambda_5=F_1-2a_3.
\end{aligned}$$
(`verify_mn2.py` PART3 also checks both formulas against $\Phi$ at $3000$ exact stratum points each.)

**One-spike limit.** At $b_2=0$, $E_{m+1}=0\le b_2\le E_m$ selects $F_{m-1}=(m-1)P+\sum_{j<m}(j-m+1)a_j+a_m=\sum_j j\,a_j$, the one-spike formula of [OneSpike] Theorem 3.1 after $F\mapsto-F$; the certificate and the layering $\mathcal L(F_{m-1})$ remain valid at $b_2=0$, and the extension is also forced by continuity of $\kappa_d$ on the chamber ([FourLevel] Theorem 2.2, [Ceiling] Section 2).

**Reduction $a_m\to0$.** At $a_m=0$ the forms of $\Phi_m$ reduce to those of $\Phi_{m-1}$ except $F_{m-1}$, which becomes $F_{m-2}-b_2<F_{m-2}$, and (for $m$ odd) $G_m$, which becomes $G_{m-2}-g_{m-2}\le G_{m-2}$; so $\Phi_m|_{a_m=0}=\Phi_{m-1}$, as padding invariance requires.

**Padding.** The example of [RankOnset] Remark 3.3, $(25,18,18,-10,-17,-17,-17)/7$ with $\kappa_7=74/7\ne\kappa_8=73/7$, has inertia $(3,4)$ and lies outside both the $(m,2)$ stratum and its mirror $(2,n)$; it does not contradict Theorem A. On our stratum the value is padding-invariant, while Section 7 shows that the optimizer set is not.

## 9. Exact verification

All checks use rational arithmetic unless stated otherwise.

*Author's scripts* (`verify_mn2.py 8`, `lr.py`, `layer_chain.py 13 300`). `lr.py`: the criterion $c^{\lambda(K)}_{\lambda(I)\lambda(J)}>0$ reproduces Fulton's recursive $T^d_r$ exactly for $d\le7$ (counts $3;\ 6,6;\ 10,21,10;\ 15,56,56,15;\ 21,126,228,126,21;\ 28,252,751,751,252,28$) and gives $c=1$ for the Pieri triples for $d\le12$. PART1: for every form, $m\le8$, $z\in\{0,1,2\}$ ($675$ triples), the certificate list is generated and checked for the sum condition, $c\ge1$, membership in $T^d_r$ for $d\le8$, all left coefficients $\le1$, and right side $=$ form. PART2: at $400$ exact points per $m\le8$, feasibility of each layering $\iff$ its closed-form region, the argmax layering is feasible, chambers as in Theorem B. PART2b: explicit $C$ at $60$ points per $m\le8$ with residuals $\le2\cdot10^{-8}$ (float eigensolves at ties; $10^{-14}$ elsewhere) and rank $m$. PART3: the $d=4$ and $d=5$ formulas at $3000$ points each; the one-spike limit for $m\le8$. `layer_chain.py`: $300$ random exact points per $m\le13$, no point without a feasible layering, histogram of the number of feasible layerings.

*Reviewer's scripts* (independent implementations; the author's code was imported only for comparison). `my_horn.py`: own Fulton generator and own LR coefficients (bialternant formula, Jacobi–Trudi), agreeing on the counts above. `my_cert.py`: all $168$ certificates for $m\le7$, $z\in\{0,1,2,5\}$, with a different elimination of $b_1$; the systematic scan lists exactly the nine certificates with a $+s_{m+1}$ term ($G_3$, $G_5$, $G_7$ at $z=1,2,5$). `my_construct.py`, `adversarial.py`: own interval recursion agreeing with the author's on $2708$ exact boundary-heavy points ($b_1=b_2$, every $b_2=E_k$, every $b_2=E_1-g_j$, flat $a$, ties, $a_m=10^{-6}$, one dominant $a_1$, geometric $a$, $m\le12$), no point without a feasible layering; $732$ explicit matrices at boundary points with residuals $\le8.4\cdot10^{-9}$ and rank $m$. `symbolic.py`: all identities of Theorem B and of Section 8 symbolically for $m\le9$. `lp_checks.py`: an own float Horn LP at $600$ random points for each of nine $(m,z)$ pairs ($5400$ points, $d\le7$) agrees with $\Phi$ to $10^{-9}$ and returns exactly the forms $F_k,G_j$ as dual gradients; uniqueness scans as quoted in Section 7. `rank_test.py`, `rank_more.py`: the exact rank-$4$ certificate and the rank-$(m+1)$ optimizers for $m=3,5,7$; exposed-form counts. The hive-LP duals of `mn2_forms.py` (m $\le9$, $z\le2$) were the original source of the conjectured forms.

*Scripts added in version 2* (all in `repro/`, run by `run_all.py`). `exact_rank4_matrix.py`: the rank-$4$ optimizer of Section 7 in closed form (sympy), residual exactly zero, entries written to `data/` with 30 significant digits. `coverage_exact.py`: for $2\le m\le10$, on a rational grid of $9567$ points containing every breakpoint $E_k$, $E_1-g_j$ and $b_1=b_2$, flat, tied, geometric and dominant-gap spectra, exact checks of cost $=$ form, feasibility $\iff$ region for every layering (Proposition 5.4), coverage (Proposition 5.5), the chambers and comparison identities of Theorem B, the feasibility and rank-$(m+1)$ criteria of Theorem C$'$(3) for odd $m$, the nondegenerate family of Theorem C$'$(4) for $m\ge4$, and the corrected activity criterion for the $G$-forms of Section 6. `pieri_triples_search.py`: exhaustive enumeration of $T^d_r$ ($d\le9$) of all Horn triples sharing the $s$-form of $(\mathrm{Pi})_i$, and the Lidskii–Wielandt-only LP comparison of Section 4.1. The workshop's own script `check_horn.py` (Fulton recursion up to $d=7$, $200$ float LPs, exact Horn checks of the six spectra of Section 7) was rerun on the author's machine and reproduces its published output (maximal LP discrepancy $7.1\cdot10^{-15}$; log in `logs/taller_check_horn.json`).

The received version reports that its reruns (`repro/run_all.py`) reproduce the outputs quoted above; its reported runtimes are listed in `repro/README.md`. The present workshop's own reruns and their limits are itemized separately in the v003 revision report and verification records; the full runner was not repeated in this revision.

## 10. Open questions

1. *Inertia $(m,3)$ and beyond.* The certificate here uses one Pieri-type triple per even index; a natural guess is that inertia $(m,n)$ requires triples adding $n-1$ boxes to a rectangle, and that block shifts with blocks of size up to $n$ attain. Neither is known; the $d=8$ example of [RankOnset] with $r_*>r_0$ has inertia $(4,4)$ and shows that the rank-$m$ block picture cannot persist unchanged.
2. *A general interior formula* for $\kappa_d$ on the ordered chamber remains open beyond $d=5$; the present result is the first infinite family of strata with a closed formula in which both signs have multiplicity $>1$.
3. *Balanced stability constants $\gamma_N$.* The optimal forward coefficients of [Ceiling,Bal44,Bal55] are known exactly for $N=2,\dots,5$ ($1/2$, $17/36$, $4/7$, $113/152$). Hive-LP computations reported in the author's line notes give the *numerical* values $\gamma_6=9/10$, $\gamma_7=781/740$, $\gamma_8=317/264$, $\gamma_9=23/17$, $\gamma_{10}=3/2$, with the extremal family switching at $N=7$ from the $(A_N,B)$ pairs to a $(u_3,z_N)$ family; these are numerical only, without exact certificates.
4. *Classification of optimizers* for $m\ge4$: which chambers have a unique optimal spectrum, and a description of the optimal face.
5. *Which Horn triples are needed in general?* On this stratum all facets are certified by Lidskii–Wielandt, Weyl and a single Pieri family; whether the facets of $\kappa_d$ on every stratum admit certificates with LR coefficient $1$ and bounded "distance from Lidskii" is open.

## 11. Reproducibility

The directory `repro/` accompanying this manuscript contains the author's scripts (`lr.py`, `layer_chain.py`, `verify_mn2.py`, `hive_core.py`, `check_horn_lp.py`, `mn2_forms.py`, `conj_formula.py`, `horn_duals_pad.py`), the reviewer's scripts (`my_horn.py`, `my_cert.py`, `my_construct.py`, `rank_test.py`, `rank_more.py`, `lp_checks.py`, `adversarial.py`, `symbolic.py`) with their logs, two small scripts written for this manuscript (`nonunique_check.py`, `d5_dominated_terms.py`), the three scripts added in version 2 (`exact_rank4_matrix.py`, `coverage_exact.py`, `pieri_triples_search.py`) with the data files they write in `data/`, the workshop script `check_horn.py` and its output, a runner `run_all.py`, and `README.md` with commands, measured runtimes and the expected final lines of every script. Dependencies: Python 3, `numpy`, `scipy` (HiGHS), `sympy`. Literature searches (2026-09-07, two queries on the inverse self-commutator problem with prescribed spectrum and on block weighted shifts / Horn certificates) returned only generic material on almost-commuting matrices, commutator norm inequalities and Horn expositions.

## AI-assistance statement

The received version declares substantial generative-AI assistance in drafting, mathematical derivations, code and review, attributed there to “Claude Fable 5.1” (Anthropic). That historical model identity, the reported review sessions and their independence have not been authenticated by this workshop. Historical descriptions of an “author” or “reviewer” script identify the supplied files, not a verified independent editorial review. OpenAI Codex assisted with the present private workshop revision: checking arguments and sources, correcting identified errors, running the checks recorded in the accompanying revision report, and preparing the PDF. Numerical checks support only their tested instances. This assistance is not an independent human peer review or a formal AIRR model-assessment report. Lluis Eriksson is the declared author and AIRR founder/operator; this conflict must be handled by the separate editorial process. Scientific authorship and approval remain with the author.

The deposited v003 was subsequently assessed in actual OpenAI Codex calls by gpt-6-astra and gpt-5.6-sol on 9 September 2026. Their original reports and subsequent clarifications are retained. Both sets of comments informed this v004 revision; Astra had also participated in earlier manuscript preparation. A separate reviewing context does not erase that history. Neither the v003 reports nor this disclosure constitute approval of the revised v004 artifact.

## Changes in internal revision v004 (9 September 2026)

1. Expanded the third candidate inequality in Proposition 5.4(3) into its exact sum of ordered differences, including empty sums and equality cases. The general identity has a direct derivation and supplementary symbolic checks.

Expanded the induction for both interval endpoints in Proposition 5.4(3) and supplied the complete d=6, i=2 Horn/Pieri example, including partitions, coefficient and both sides of the inequality.

The earlier deposited v003 and its model reports are retained. This revision responds to their findings; it is not a final acceptance.

## Changes in internal revision v003 (8 September 2026)

1. Corrected the exact criterion for an empty open $F_k$ chamber: equality within each indicated pair, not constancy of the entire tail.
2. Added the exact counterexample $(4,3,3,1,1)$ and the nonnegative-sum proof of the corrected criterion.
3. Made the unpadded case an explicit alternative in Theorem C'(2), rather than implying that it forces a different active form.
4. Clarified the rank argument and qualified historical AI-review provenance. The main cost formula is unchanged.
5. Distinguished the operator-norm objective in [JOS13] from the mixed operator/Hilbert–Schmidt objective in [AS15], and completed the latter's bibliographic entry.

## Changes in version 2 (8 September 2026)

Version 2 answers the items of the external workshop evaluation (TALLER-0004); the workshop's page numbers refer to the version-1 PDF.

1. *(Item: page 9, Section 6, identity $E_{k+1}-E_{k+2}=a_{k+1}$.)* Accepted: the identity was false ($a=(4,3,2,1)$, $k=1$ gives $E_2-E_3=2\ne3$). The exposedness argument now uses the correct identities $E_{k+1}-E_{k+3}=a_{k+1}$ and $E_{k+1}-E_{k+2}=\sum(\text{pair gaps})\,(+a_m)$, characterises exactly when the open $F_k$ chamber is empty, and exhibits explicit exposing spectra. Theorems A, B, C$'$ are unchanged.
2. *(Item: page 6, Weyl row $(3;3;3)$.)* Accepted: the triple is $(3;1;3)$ ($I=K=\{3\}$, $J=\{1\}$), as in Lemma 4.1 and in the reviewer's `my_cert.log`; the Weyl item of Lemma 4.1 now states $I,J,K$ explicitly. No other certificate display was affected.
3. *(Item: last sentence of Section 6.)* Accepted: the sentence is replaced by the exact criterion "some $G_j$ is active somewhere on the stratum iff $\sum_{j\ne j^*}g_j\le g^*$, uniquely iff strict", with the tie cases (including the workshop's example $a=(2,1,1)$, $b_1=b_2=2$, $F_0=G_1=G_3=5$) spelled out.
4. *(Item: page 11 matrix at full precision.)* Accepted: the rank-$4$ optimizer is now given in closed form (square roots of integers), with residual exactly zero; the workshop's residual $2.15\cdot10^{-4}$ from the four-decimal print is reproduced and explained; data files with 30 significant digits and the script are in `repro/`.
5. *(Item: re-audit of Sections 5.2–5.3 and of Theorem C$'$.)* No mathematical error was found in Lemmas 5.1–5.3, Proposition 5.4 or Proposition 5.5, but the exposition was tightened: a new Lemma 5.0 states why feasibility reduces exactly to the interval recursion; the proofs of Proposition 5.4 list every tail case ($k=m-1$; $j=1$, $j=m-1$, $j=m$; $m$ even/odd; $m=2$); the rank bookkeeping in the proof of Theorem C$'$(3) was corrected (version 1 wrote $\operatorname{rank}C=1+2\#\{\dots\}+1$; the correct count is $\operatorname{rank}C=m+[\sigma_2(S_{T-1})>0]$, because every earlier $S_t$ has rank $2$ in any solution), a misleading parenthetical in the proof of (1)–(2) was removed, and the exhaustiveness of cases (2)/(3) is stated. A new exact-arithmetic script (`coverage_exact.py`) checks all these statements on a fine rational grid with all ties and boundaries for $m\le10$.
6. *(Item: dependence on internal record codes.)* The antecedent records are cited by descriptive keys with theorem numbers and are restated where used; the reference list gives their titles and ARR identifiers. The sentence citing a script (`find_triples.py`) that was not part of the reproducibility package was replaced by a verifiable statement backed by `pieri_triples_search.py`.
7. The workshop's `check_horn.py` was rerun and agrees with its published results (Section 9). The reproducibility package was completed (README with expected outputs, data files, logs).

## References

- [FourLevel] L. Eriksson, *The Exact Four-Level Inverse Commutator Cost: Horn–Littlewood–Richardson Facets, Rank Transitions, and Sharp Loop Synthesis*, AI Research Record, ARR-2026-3M1EEG1T689ADSMW (2026). Cited: Lemma 2.1 (two-operator reduction), Theorem 2.2 (Horn program), Theorem 3.1 (four-level formula).
- [FiveLevel] L. Eriksson, *The Exact Five-Level Inverse Commutator Cost: Twelve Horn Chambers, Optimal Rank, and the Sharp 5/2 Resource Tax*, AI Research Record, ARR-2026-37B8R0QTA894GTFF (2026). Cited: Theorem 3.1 (five-level formula).
- [RankAdaptive] L. Eriksson, *Sharp Rank-Adaptive Bounds for Inverse Self-Commutators*, AI Research Record, ARR-2026-1D2QV1RP1292JREW (2026). Cited: Theorem 1.1 (rank-adaptive bound), the weighted-shift construction of Section 4.
- [OneSpike] L. Eriksson, *One-Spike Inverse Self-Commutators and Exact Three-versus-Four-Kick Curvature Synthesis*, AI Research Record, ARR-2026-7NPRNBW4488HG90K (2026). Cited: Theorem 3.1 (one-spike formula and rigidity).
- [RankOnset] L. Eriksson, *Sharp Onset and Unbounded Growth of Norm-Optimal Self-Commutator Rank*, AI Research Record, ARR-2026-5QQF95VHTC9GABH8 (2026). Cited: Lemma 2.1 (inertia obstruction), Proposition 2.2 (Horn program in the $s$-normalisation), Theorem 3.1 ($r_*=r_0$ for $d\le7$), Theorem 4.1 (the $d=8$ phase), Remark 3.3 (padding example).
- [Ceiling] L. Eriksson, *Sharp inertia ceilings and optimal stability for inverse self-commutators*, AI Research Record, ARR-2026-24M24KDPZK8HDBQ9 (2026). Cited: Theorem 1 (inertia ceiling), Section 2 (continuity), Theorem 3 (balanced stability constants).
- [Bal44] L. Eriksson, *Polynomial vertex reduction and optimal stability at balanced inertia (4,4)*, AI Research Record, ARR-2026-54Q3HMFJ0Z8CZB4T (2026).
- [Bal55] L. Eriksson, *Optimal stability and all equality cases at balanced inertia (5,5)*, AI Research Record, ARR-2026-6ZJY1SSSJA98WBWX (2026).
- [Ho62] A. Horn, Eigenvalues of sums of Hermitian matrices, *Pacific J. Math.* 12 (1962) 225–241.
- [Kl98] A. A. Klyachko, Stable bundles, representation theory and Hermitian operators, *Selecta Math. (N.S.)* 4 (1998) 419–445.
- [KT99] A. Knutson, T. Tao, The honeycomb model of $GL_n(\mathbb C)$ tensor products I: proof of the saturation conjecture, *J. Amer. Math. Soc.* 12 (1999) 1055–1090.
- [Fu00] W. Fulton, Eigenvalues, invariant factors, highest weights, and Schubert calculus, *Bull. Amer. Math. Soc.* 37 (2000) 209–249.
- [Fu97] W. Fulton, *Young Tableaux*, LMS Student Texts 35, Cambridge University Press, 1997 (Pieri rule).
- [Li50] V. B. Lidskii, On the characteristic numbers of the sum and product of symmetric matrices, *Dokl. Akad. Nauk SSSR* 75 (1950) 769–772.
- [Wi55] H. Wielandt, An extremum property of sums of eigenvalues, *Proc. Amer. Math. Soc.* 6 (1955) 106–110.
- [We12] H. Weyl, Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen, *Math. Ann.* 71 (1912) 441–479.
- [JOS13] W. B. Johnson, N. Ozawa, G. Schechtman, A quantitative version of the commutator theorem for zero trace matrices, *Proc. Natl. Acad. Sci. USA* 110 (2013) 19251–19255.
- [AS15] O. Angel, G. Schechtman, The Hilbert–Schmidt version of the commutator theorem for zero trace matrices, *Bull. London Math. Soc.* 47 (2015), no. 4, 715–719; doi:10.1112/blms/bdv045; arXiv:1503.07980.
