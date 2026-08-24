# Exact Multiplicity Floors for Dual Singularities from Absorbing Gauss Fibres

Lluis Eriksson — Independent researcher  
August 24, 2026 — version 1.0

## Abstract

Let $X^d\subset\mathbb P^{d+1}_{\mathbb C}$ be a smooth hypersurface, let its Gauss map have complete reduced fibre $Z$ over a tangent hyperplane $W$, and assume that in the complete $\mathcal O_X(m)$ embedding the point span of $Z$ contains the order-$s$ osculating space at every support. We prove the sharp floor

$$
\operatorname{mult}_W(X^\vee)\ge s^d|Z|\ge s^d\binom{d+m}{d}.
$$

Absorption forces the equation of $W$ to have order at least $s+1$ at every support. The classical Dimca–Parusiński multiplicity–Milnor formula and the Milnor lower bound then give the first inequality, while the exact tangent-absorption theorem gives the binomial branch floor. We construct simultaneous equality examples with proper point span, exact reduced Gauss fibre, ordinary section singularities of multiplicity $s+1$, and the corresponding weighted tangent-cone cycle. The construction gives a sufficient, not minimal, hypersurface degree; no equality classification or exhaustive priority claim is made.

# Statement and scope

Let $`X^d\subset\mathbb P^{d+1}_{\mathbb C}`$ be a smooth hypersurface of degree $`D\geq2`$, let $`H=\mathcal O_X(1)`$, and let
``` math
\gamma_X:X\longrightarrow (\mathbb P^{d+1})^\vee
```
be the Gauss morphism. Its image is the dual hypersurface $`X^\vee`$. For $`\eta\in X^\vee`$, write $`W_\eta\subset\mathbb P^{d+1}`$ for the corresponding hyperplane and
``` math
Z_\eta=\bigl(\gamma_X^{-1}(\eta)\bigr)_{\mathrm{red}}.
```

Fix $`m\geq1`$. For a nonempty finite reduced $`Z\subset X`$, let
``` math
S_Z=\operatorname{Im}\!\left(
 H^0(Z,H^m|_Z)^*\longrightarrow H^0(X,H^m)^*\right).
```
For $`p\in X`$ and $`a\geq0`$, principal-parts evaluation gives the affine osculating block
``` math
\widehat\operatorname{Osc}^a_p(H^m)=\operatorname{Im}\!\left(
 H^0((a+1)p,H^m|_{(a+1)p})^*\longrightarrow H^0(X,H^m)^*\right).
```

<div class="definition">

**Definition 1**. For $`1\leq s\leq m`$, the set $`Z`$ is *point-span $`s`$-osculating-absorbing* if
``` math
\widehat\operatorname{Osc}^s_p(H^m)\subseteq S_Z\qquad(p\in Z).
```

</div>

Put
``` math
N_{d,m}=\binom{d+m}{d}.
```

<div id="thm:floor" class="theorem">

**Theorem 2** (Sharp dual-multiplicity floor). *Let $`\eta\in X^\vee`$ and $`Z=Z_\eta`$. If $`Z`$ is point-span $`s`$-osculating-absorbing for the complete $`H^m`$ embedding, then:*

1.  *$`X^\vee`$ has exactly $`|Z|`$ analytic branches at $`\eta`$ and
    ``` math
    |Z|\geq N_{d,m};
    ```*

2.  *for every $`p\in Z`$, the germ of $`X\cap W_\eta`$ has multiplicity at least $`s+1`$ and Milnor number $`\mu_p\geq s^d`$;*

3.  
    *``` math
    \operatorname{mult}_\eta(X^\vee)=\sum_{p\in Z}\mu_p
     \geq s^d|Z|\geq s^dN_{d,m};
    ```*

4.  *as a cycle in $`T_\eta((\mathbb P^{d+1})^\vee)`$, the affine tangent cone is
    ``` math
    C_\eta(X^\vee)=\sum_{p\in Z}\mu_p[T_\eta(p^\perp)].
    ```*

</div>

<div id="thm:sharpness" class="theorem">

**Theorem 3** (Simultaneous sharpness). *For every $`d,m\geq1`$, every $`1\leq s\leq m`$, and every
``` math
D\geq(s+2)N_{d,m}+1,
```
there exist a smooth integral degree-$`D`$ hypersurface $`X^d\subset\mathbb P^{d+1}`$, a hyperplane $`W`$, and $`Z=(\gamma_X^{-1}([W]))_{\mathrm{red}}`$ such that
``` math
|Z|=\dim S_Z=N_{d,m}<h^0(X,H^m),
```
$`Z`$ is point-span $`s`$-osculating-absorbing, and $`X\cap W`$ has precisely the points of $`Z`$ as singularities. At every $`p\in Z`$ the section singularity is ordinary of multiplicity $`s+1`$, so
``` math
\mu_p=s^d,\qquad
 \operatorname{mult}_{[W]}(X^\vee)=s^dN_{d,m},
```
and
``` math
C_{[W]}(X^\vee)=s^d\sum_{p\in Z}[T_{[W]}(p^\perp)].
```
In particular, every inequality in Theorem <a href="#thm:floor" data-reference-type="ref" data-reference="thm:floor">2</a> is sharp. When $`s=1`$, the $`N_{d,m}`$ branches are smooth and the tangent cone is the reduced union of the distinct hyperplanes $`p^\perp`$.*

</div>

The multiplicity identity used here is classical ; Dimca–Ilardi use the same bridge to study nodal hyperplane sections and normal-crossing points of duals . Accordingly, the factor $`s^d`$ is presented as an explicit local consequence of that classical theory, not as a new general principle about dual multiplicities. The contribution isolated here is the combination with point-span absorption: the resulting sharp binomial floor and the exact dual geometry of equality examples with proper point span. This comparison is selective, not a priority certification.

# Gauss fibres and branches

<div id="lem:normalization" class="lemma">

**Lemma 4** (Normalization by the Gauss map). *The Gauss morphism $`\gamma_X:X\to X^\vee`$ is finite and birational. Hence it is the normalization of $`X^\vee`$, and the number of analytic branches of $`X^\vee`$ at $`\eta`$ equals $`|Z_\eta|`$.*

</div>

<div class="proof">

*Proof.* If $`F`$ defines $`X`$, its first partial derivatives have no common zero on $`X`$ because $`X`$ is smooth. They define $`\gamma_X`$ and give
``` math
\gamma_X^*\mathcal O_{X^\vee}(1)=\mathcal O_X(D-1),
```
which is ample. A positive-dimensional fibre would make this line bundle trivial on a positive-dimensional complete subvariety, contradicting ampleness. Thus $`\gamma_X`$ is finite. Projective biduality identifies the unique tangency point over a general smooth point of $`X^\vee`$, so the map is birational. Since $`X`$ is smooth and therefore normal, it is the normalization. Complex algebraic local rings are excellent, normalization commutes with completion, and each completed local ring above $`\eta`$ is a power-series domain. The normalization fibre therefore indexes the analytic branches. ◻

</div>

The equality
``` math
\operatorname{Sing}(X\cap W_\eta)=Z_\eta
```
holds set-theoretically: a point of the hyperplane section is singular exactly when $`W_\eta`$ is tangent to $`X`$ there. Lemma <a href="#lem:normalization" data-reference-type="ref" data-reference="lem:normalization">4</a> makes this set finite, so all section singularities are isolated.

# Absorption forces high contact

<div id="lem:annihilator" class="lemma">

**Lemma 5** (Local annihilator consequence). *If $`Z`$ is point-span $`s`$-osculating-absorbing and $`a\in H^0(X,\mathcal I_Z\otimes H^m)`$, then
``` math
a_p\in\mathfrak m_{X,p}^{s+1}H^m_p\qquad(p\in Z).
```*

</div>

<div class="proof">

*Proof.* The annihilator of $`S_Z`$ is $`H^0(X,\mathcal I_Z\otimes H^m)`$. The annihilator of $`\widehat\operatorname{Osc}^s_p(H^m)`$ consists of sections whose germ vanishes modulo $`\mathfrak m_{X,p}^{s+1}`$. The inclusion $`\widehat\operatorname{Osc}^s_p(H^m)\subseteq S_Z`$ reverses under annihilators and gives the claim. ◻

</div>

<div id="prop:contact" class="proposition">

**Proposition 6** (Contact along an absorbing Gauss fibre). *Let $`\ell_\eta`$ be a linear equation for $`W_\eta`$. Under the hypotheses of Theorem <a href="#thm:floor" data-reference-type="ref" data-reference="thm:floor">2</a>,
``` math
(\ell_\eta|_X)_p\in\mathfrak m_{X,p}^{s+1}H_p
 \qquad(p\in Z).
```*

</div>

<div class="proof">

*Proof.* Every point of $`Z`$ lies in $`W_\eta`$. Fix $`p\in Z`$ and choose $`g_p\in H^0(X,H^{m-1})`$ nonzero at $`p`$, taking $`g_p=1`$ when $`m=1`$. The section $`\ell_\eta g_p`$ of $`H^m`$ vanishes at every support of $`Z`$. Lemma <a href="#lem:annihilator" data-reference-type="ref" data-reference="lem:annihilator">5</a> puts its germ in $`\mathfrak m_{X,p}^{s+1}H^m_p`$. The germ of $`g_p`$ is a unit, so division gives the displayed contact. ◻

</div>

This step explains why the factor $`s^d`$ in Theorem <a href="#thm:floor" data-reference-type="ref" data-reference="thm:floor">2</a> is not an extra geometric hypothesis. It is forced by the combination of a common tangent hyperplane and order-$`s`$ absorption.

# Milnor numbers and the dual multiplicity

<div id="lem:milnor" class="lemma">

**Lemma 7** (Milnor floor from order). *Let $`R=\mathbb C\{x_1,\ldots,x_d\}`$ with maximal ideal $`\mathfrak m`$, and let $`f\in\mathfrak m^{s+1}`$ have an isolated critical point at the origin. Then
``` math
\mu(f)=\dim_{\mathbb C}R/
 \left(\frac{\partial f}{\partial x_1},\ldots,
 \frac{\partial f}{\partial x_d}\right)\geq s^d.
```
Equality holds if the initial homogeneous form $`f_{s+1}`$ defines a smooth hypersurface in $`\mathbb P^{d-1}`$ (with the empty hypersurface convention for $`d=1`$).*

</div>

<div class="proof">

*Proof.* Let $`J`$ be the Jacobian ideal. Isolatedness makes $`J`$ $`\mathfrak m`$-primary. It is generated by a system of parameters in the regular local ring $`R`$, so $`\mu(f)=\operatorname{length}(R/J)=e(J)`$. Since $`J\subseteq\mathfrak m^s`$, monotonicity of Hilbert–Samuel multiplicity gives
``` math
e(J)\geq e(\mathfrak m^s)=s^d.
```
If $`f_{s+1}`$ is smooth projectively, its $`d`$ partial derivatives are a homogeneous regular sequence of degree $`s`$. The associated-graded intersection has length $`s^d`$, so the local Jacobian colength is $`s^d`$. ◻

</div>

Dimca’s multiplicity formula says that for a smooth complex hypersurface and a hyperplane section with isolated singularities,
``` math
\begin{equation}
\label{eq:dimca}
 \operatorname{mult}_\eta(X^\vee)=\sum_{p\in\operatorname{Sing}(X\cap W_\eta)}\mu_p.
\end{equation}
```
The refined tangent-cone statement is
``` math
\begin{equation}
\label{eq:tangent-cone}
 C_\eta(X^\vee)=\sum_p\mu_p[T_\eta(p^\perp)].
\end{equation}
```
Here $`p^\perp`$ is the hyperplane through $`\eta`$ in the dual projective space corresponding, under biduality, to $`p`$; the displayed component is its linear tangent space at $`\eta`$. Equivalently, projectivizing gives the cycle $`\sum_p\mu_p[\mathbb P(T_\eta(p^\perp))]`$ in the projectivized ambient tangent space.

For completeness, the branch contribution can also be read directly from the Gauss map. Choose analytic coordinates at $`p`$ in which $`X`$ is the graph
``` math
x_{d+1}=h(z_1,\ldots,z_d),\qquad h\in\mathfrak m^{s+1},
```
and $`W_\eta=(x_{d+1}=0)`$. Work in the analytic local rings $`A=\mathcal O^{\mathrm{an}}_{X^\vee,\eta}`$ and $`R=\mathcal O^{\mathrm{an}}_{X,p}\cong\mathbb C\{z_1,\ldots,z_d\}`$, and put $`I=\mathfrak m_\eta R`$. The local expression for the Gauss map gives, up to signs,
``` math
\begin{equation}
\label{eq:gauss-ideal}
 I=\left(
 h_1,\ldots,h_d,\ h-\sum_{i=1}^d z_i h_i
 \right),\qquad h_i=\frac{\partial h}{\partial z_i}.
\end{equation}
```
Thus, for $`J=(h_1,\ldots,h_d)`$,
``` math
J\subseteq I\subseteq\mathfrak m^s.
```
When the initial form $`h_{s+1}`$ is projectively smooth, $`J`$ is a parameter ideal with $`e(J)=s^d`$. Monotonicity and $`e(\mathfrak m^s)=s^d`$ then give
``` math
s^d=e(J)\geq e(I)\geq e(\mathfrak m^s)=s^d,
```
so the contribution of that normalization branch is exactly $`s^d`$. The finite-extension associativity formula for Hilbert–Samuel multiplicity recovers the sum over the points above $`\eta`$; see . Analytification and completion preserve the multiplicities in question. This is a local recovery of the classical multiplicity–Milnor formula in this ordinary case, included to make the equality mechanism in the examples explicit.

<div class="proof">

*Proof of Theorem <a href="#thm:floor" data-reference-type="ref" data-reference="thm:floor">2</a>.* Lemma <a href="#lem:normalization" data-reference-type="ref" data-reference="lem:normalization">4</a> gives the branch count. Order-$`s`$ absorption contains tangent absorption, so the exact point-span tangent floor gives
``` math
|Z|\geq N_{d,m}.
```
Proposition <a href="#prop:contact" data-reference-type="ref" data-reference="prop:contact">6</a> says that a local equation of the hyperplane section belongs to $`\mathfrak m_{X,p}^{s+1}`$. The critical point is isolated, hence Lemma <a href="#lem:milnor" data-reference-type="ref" data-reference="lem:milnor">7</a> gives $`\mu_p\geq s^d`$. Equations <a href="#eq:dimca" data-reference-type="eqref" data-reference="eq:dimca">[eq:dimca]</a> and <a href="#eq:tangent-cone" data-reference-type="eqref" data-reference="eq:tangent-cone">[eq:tangent-cone]</a> give all remaining assertions. ◻

</div>

<div class="remark">

**Remark 8** (Why the earlier rank term gives no refinement here). Suppose $`m\geq2s+1`$. Because $`Z\subset W_\eta`$, the equation of $`W_\eta`$ lies in the kernel of linear evaluation, so
``` math
r_1(Z):=\operatorname{rk}\bigl(H^0(X,H)\to H^0(Z,H|_Z)\bigr)\leq d+1.
```
The quotient
``` math
\frac{\binom{d+2s+1}{d}}{\binom{d+s}{d}}
 =\prod_{j=1}^d\frac{2s+1+j}{s+j}
```
is nondecreasing in $`s\geq1`$ term by term. At $`s=1`$ it equals $`(d+3)(d+2)/6\geq d+1`$. Hence
``` math
\binom{d+m}{d}\geq(d+1)\binom{d+s}{d}
 \geq r_1(Z)\binom{d+s}{d}.
```
Thus the rank-sensitive maximum in specializes exactly to $`N_{d,m}`$ for a Gauss fibre; presenting it as a stronger bound here would be misleading.

</div>

# Interpolation with prescribed ordinary jets

We now adapt the proper-span construction of ; its antecedent for ordinary double points is the author’s public proof note . The interpolation and extension architecture $`F=f+yG`$ is therefore not claimed as new here. The added points are the prescribed ordinary initial forms, the exact Gauss-fibre identity, and the resulting branch and dual-multiplicity calculation.

Let $`W\cong\mathbb P^d`$ and choose $`N=N_{d,m}`$ distinct points $`Z\subset W`$ such that
``` math
\begin{equation}
\label{eq:unisolvent}
 H^0(W,\mathcal O_W(m))\xrightarrow{\sim}H^0(Z,\mathcal O_Z(m)).
\end{equation}
```
Such sets exist because the evaluation lines of all points span the dual of $`H^0(W,\mathcal O_W(m))`$; select a basis. Very ampleness separates the supports.

<div id="lem:jets" class="lemma">

**Lemma 9** (Simultaneous jets from separators). *Let $`p_1,\ldots,p_t`$ be distinct points of $`\mathbb P^d`$ and let $`a_i\geq0`$. Restriction to the disjoint fat points is surjective in every degree
``` math
k\geq\sum_{i=1}^t(a_i+1)-1:
```
``` math
H^0(\mathbb P^d,\mathcal O(k))\longrightarrow
 \bigoplus_{i=1}^t
 H^0\bigl(\mathcal O(k)\otimes\mathcal O_{\mathbb P^d,p_i}/\mathfrak m_{p_i}^{a_i+1}\bigr).
```*

</div>

<div class="proof">

*Proof.* For $`i\ne j`$, choose a linear form $`\ell_{ij}`$ vanishing at $`p_j`$ and nonzero at $`p_i`$. The product
``` math
P_i=\prod_{j\ne i}\ell_{ij}^{a_j+1}
```
kills every other target and is a unit at $`p_i`$. Degree-$`a_i`$ forms realize all order-$`a_i`$ jets at $`p_i`$. Their products with $`P_i`$ have common degree $`\sum_j(a_j+1)-1`$ and isolate arbitrary data at $`p_i`$. Summing over $`i`$ proves surjectivity in that degree. Multiplication by a form nonzero at all supports raises the degree. ◻

</div>

For every $`p\in Z`$, choose a homogeneous form
``` math
q_p\in\operatorname{Sym}^{s+1}(\mathfrak m_{W,p}/\mathfrak m_{W,p}^2)
```
whose projective zero locus in $`\mathbb P(T_pW)`$ is smooth. Put
``` math
E=(s+2)N,
```
and fix $`D\geq E+1`$. Lemma <a href="#lem:jets" data-reference-type="ref" data-reference="lem:jets">9</a> supplies $`f_0\in H^0(W,\mathcal O_W(D))`$ whose class at every $`p`$ is $`q_p`$ modulo $`\mathfrak m_{W,p}^{s+2}`$ and whose lower terms vanish. Let
``` math
V=H^0(W,\mathcal I_{(s+2)Z}(D)),\qquad \mathcal A=f_0+V.
```

<div id="prop:section" class="proposition">

**Proposition 10** (A section with exactly the prescribed singularities). *There is $`f\in\mathcal A`$ such that $`V(f)\subset W`$ is smooth away from $`Z`$. At every $`p\in Z`$ it has an ordinary isolated hypersurface singularity of multiplicity $`s+1`$ and Milnor number $`s^d`$.*

</div>

<div class="proof">

*Proof.* Fix $`q\in W\setminus Z`$. For every $`p\in Z`$, choose a hyperplane $`\ell_{p,q}`$ through $`p`$ and not through $`q`$, and set
``` math
A_q=\prod_{p\in Z}\ell_{p,q}^{s+2}.
```
It has degree $`E`$, belongs to the ideal of $`(s+2)Z`$, and is a unit on the first neighbourhood $`2q`$. Since $`D-E\geq1`$, multiplication by $`A_q`$ proves that
``` math
V\longrightarrow H^0(2q,\mathcal O_{2q}(D))
```
is surjective. Therefore the affine condition $`j_q^1f=0`$ has codimension $`d+1`$ in $`\mathcal A`$. Its incidence over the $`d`$-dimensional base $`W\setminus Z`$ has dimension at most $`\dim\mathcal A-1`$. Choose $`f`$ outside the closure of its image. The fixed jets $`q_p`$ give the asserted ordinary singularities, and Lemma <a href="#lem:milnor" data-reference-type="ref" data-reference="lem:milnor">7</a> gives $`\mu_p=s^d`$. ◻

</div>

# Smooth hypersurfaces and exact Gauss fibres

Embed $`W=V(y)`$ as a hyperplane in $`\mathbb P^{d+1}`$ and lift $`f`$ independently of $`y`$. Put
``` math
U=H^0(\mathbb P^{d+1},\mathcal O(D-1)),\qquad F_G=f+yG\quad(G\in U).
```

<div id="prop:extension" class="proposition">

**Proposition 11** (Smooth extension). *There is $`G\in U`$, nonzero at every point of $`Z`$, such that $`X=V(F_G)`$ is a smooth integral hypersurface. Moreover
``` math
\operatorname{Sing}(X\cap W)=Z,
 \qquad
 (\gamma_X^{-1}([W]))_{\mathrm{red}}=Z.
```*

</div>

<div class="proof">

*Proof.* On $`y\ne0`$, multiplication by $`y`$ is a unit on first neighbourhoods and $`\mathcal O(D-1)`$ generates first jets. For fixed $`q`$ in that $`(d+1)`$-dimensional open set, the affine condition $`j_q^1(f+yG)=0`$ has codimension $`d+2`$ in $`U`$. The corresponding incidence has dimension at most $`\dim U-1`$, so the closure of its image is proper. Avoid it together with the finitely many hyperplanes $`G(p)=0`$.

The resulting $`X`$ is smooth on $`y\ne0`$. At a point of $`W\setminus Z`$ lying on $`X`$, the tangential first jet of $`f`$ is nonzero by Proposition <a href="#prop:section" data-reference-type="ref" data-reference="prop:section">10</a>. At $`p\in Z`$, the normal first jet is $`G(p)\ne0`$. Thus $`X`$ is smooth everywhere. The hypersurface sequence and $`H^1(\mathbb P^{d+1},\mathcal O(-D))=0`$ give $`H^0(X,\mathcal O_X)=\mathbb C`$, so $`X`$ is connected; a smooth connected scheme is integral.

The hyperplane section is $`V(f)`$, hence has singular locus exactly $`Z`$. A point of $`X\cap W`$ belongs to the Gauss fibre over $`[W]`$ precisely when the section is singular there. A point outside $`W`$ cannot have $`W`$ as tangent hyperplane because a tangent hyperplane contains its point. This proves the exact fibre identity. ◻

</div>

At $`p\in Z`$, the local equation on $`X`$ is
``` math
y=-f/G\in\mathfrak m_{X,p}^{s+1},
```
and its initial form is the nonzero scalar multiple $`-q_p/G(p)`$. Thus $`X\cap W`$ has precisely the ordinary singularities already prescribed.

<div class="proof">

*Proof of Theorem <a href="#thm:sharpness" data-reference-type="ref" data-reference="thm:sharpness">3</a>.* Use Proposition <a href="#prop:extension" data-reference-type="ref" data-reference="prop:extension">11</a>. Since $`D>m`$, restriction is an isomorphism
``` math
H^0(\mathbb P^{d+1},\mathcal O(m))\xrightarrow{\sim}H^0(X,\mathcal O_X(m)).
```
Let a section on $`X`$ vanish on $`Z`$ and let $`Q`$ be its ambient lift. By <a href="#eq:unisolvent" data-reference-type="eqref" data-reference="eq:unisolvent">[eq:unisolvent]</a>, $`Q|_W=0`$, so $`Q=yR`$. Since $`y\in\mathfrak m_{X,p}^{s+1}`$ at every support, $`Q`$ vanishes on $`(s+1)Z`$. The reverse kernel inclusion is automatic, hence the annihilator criterion proves order-$`s`$ absorption. Unisolvence gives
``` math
|Z|=\dim S_Z=N.
```
The ambient degree-$`m`$ space has dimension $`\binom{d+m+1}{d+1}>N`$, so the point span is proper.

The exact Gauss fibre is Proposition <a href="#prop:extension" data-reference-type="ref" data-reference="prop:extension">11</a>; the section singularities have Milnor number $`s^d`$. Dimca’s formulas <a href="#eq:dimca" data-reference-type="eqref" data-reference="eq:dimca">[eq:dimca]</a>–<a href="#eq:tangent-cone" data-reference-type="eqref" data-reference="eq:tangent-cone">[eq:tangent-cone]</a> give the stated dual multiplicity and tangent-cone cycle. When $`s=1`$, each section singularity is $`A_1`$, the Gauss map is immersive at its support, and the corresponding dual branch is smooth. The tangent hyperplanes $`p^\perp`$ are distinct because the supports are distinct. ◻

</div>

# Context, reproducibility, and limitations

The identity $`\operatorname{mult}_W(X^\vee)=\sum\mu_p`$ and its tangent-cone refinement are not new; they are attributed respectively to Dimca and , with broader multiplicity results due to Parusiński , and belong to the classical projective-duality and discriminant framework . Dimca–Ilardi prove that a generic smooth hypersurface in $`\mathbb P^n`$, $`n\geq3`$, has a dual normal-crossing point of multiplicity $`n`$, arising from $`n`$ nodes in a hyperplane section . They also emphasize the classical fact that isolated singularity hyperplane sections can be extended to smooth hypersurfaces. The present construction uses that freedom subject to the additional unisolvence and absorption constraints.

The normalizing role of the Gauss map and the earlier large-fibre construction also occur in the author’s public notes . Those notes do not state the branch count or dual multiplicity computed here; they are nevertheless direct authorial antecedents rather than independent validation. The exact tangent floor is invoked from ; the higher-block estimate and the underlying proper-span construction are invoked from , to which the exact reduced Gauss-fibre and dual-singularity calculations are added here. These are papers by the same author and are not independent external validation.

The accompanying replay `repro/verify_dual_multiplicity.py` checks finite monomial Jacobian quotients, 105 binomial/multiplicity cases, 100 rank-collapse cases, and selected simplex evaluation matrices using integer and rational arithmetic. The byte-stable runner is `repro/run_all_replays.py`. These scripts do not mechanize the incidence arguments, projective duality, Dimca’s formula, or literature priority.

The limitations are material.

- The dual-singularity theorem is over $`\mathbb C`$. No positive- characteristic Milnor, inseparable Gauss-map, or wild-ramification extension is asserted.

- The support is the complete reduced Gauss fibre, not an arbitrary subset. Its scheme-theoretic fibre can be nonreduced and is not classified.

- The degree $`D\geq(s+2)N_{d,m}+1`$ is a transparent sufficient threshold, not a minimality result.

- For $`s=1`$ the tangent cone is a reduced arrangement of distinct hyperplanes. It is not called a simple normal-crossing divisor when the number of branches exceeds the ambient dimension.

- No analytic classification of the dual branches, equality classification, exhaustive priority review, human peer review, or formal verification is claimed.

# Conclusion

Osculating absorption in a Gauss fibre forces more than many coincident tangent points. It forces the common tangent hyperplane to have order $`s+1`$ contact at every support, converting the exact point-span rank floor into the sharp dual-singularity floor
``` math
\operatorname{mult}_W(X^\vee)\geq s^d\binom{d+m}{d}.
```
The previously developed prescribed-jet construction realizes equality while keeping the point span proper and the reduced Gauss fibre exact; the new use made of it here is the dual-singularity calculation. The result ties finite reduced span rank, osculating contact, Milnor numbers, normalization branches, and dual multiplicity in one sharp construction. Minimal ambient degree and the geometry of equality configurations remain open.

<div class="thebibliography">

99

A. Dimca, *Milnor numbers and multiplicities of dual varieties*, Rev. Roumaine Math. Pures Appl. **31** (1986), no. 6, 535–538.

A. Dimca, *Topics on Real and Complex Singularities*, Advanced Lectures in Mathematics, Friedr. Vieweg & Sohn, Braunschweig, 1987.

A. Dimca and G. Ilardi, *On the duals of smooth projective complex hypersurfaces*, Publ. Mat. **68** (2024), 431–438. <https://doi.org/10.5565/PUBLMAT6822404>

A. Parusiński, *Multiplicity of the dual variety*, Bull. London Math. Soc. **23** (1991), no. 5, 429–436. <https://doi.org/10.1112/blms/23.5.429>

L. Eriksson, *The exact rank floor for point-span tangent absorption in arbitrary characteristic*, ARR-2026-2MHNZRRJP49Y9SWP, v3 (2026). <https://arr-research.github.io/papers/ARR-2026-2MHNZRRJP49Y9SWP/versions/v3/>

L. Eriksson, *Exact floors and proper-span extremizers for higher osculating absorption*, ARR-2026-66Q8M61AA196T8BC, v2 (2026). <https://arr-research.github.io/papers/ARR-2026-66Q8M61AA196T8BC/versions/v2/>

L. Eriksson, *The ordinary Gauss map is finite birational*, proof note B218 (2026). <https://github.com/lluiseriksson/hodge-conjecture-research-front/blob/main/proofs/B218-gauss-map-finite-birational.md>

L. Eriksson, *Special Gauss fibers can be arbitrarily large*, proof note B219 (2026). <https://github.com/lluiseriksson/hodge-conjecture-research-front/blob/main/proofs/B219-arbitrarily-large-special-gauss-fibers.md>

I. M. Gelfand, M. M. Kapranov, and A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhäuser, Boston, 1994.

S. L. Kleiman, *Tangency and duality*, in *Proceedings of the 1984 Vancouver Conference in Algebraic Geometry*, CMS Conf. Proc. **6**, Amer. Math. Soc., 1986, 163–225.

O. Zariski and P. Samuel, *Commutative Algebra, Volume II*, Graduate Texts in Mathematics 29, Springer, 1975. <https://doi.org/10.1007/978-3-662-29244-0>

</div>
