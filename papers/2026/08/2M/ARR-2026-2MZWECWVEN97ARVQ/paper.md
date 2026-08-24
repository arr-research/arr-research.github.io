# Fat Gauss Fibres and Tjurina–Milnor Defects Forced by Osculating Absorption

Lluis Eriksson — Independent researcher  
August 25, 2026 — version 1.0

## Abstract

Let $X^d\subset\mathbb P^{d+1}_{\mathbb C}$ be a smooth non-linear
hypersurface and let $\Gamma_\eta$ be the scheme-theoretic fibre of its Gauss
normalization over a tangent hyperplane. The completed local fibre algebra is
the Tjurina algebra of the tangent-section germ, while the classical dual
multiplicity is the sum of its Milnor numbers. Thus

``` math
\operatorname{mult}_\eta(X^\vee)-\operatorname{length}(\Gamma_\eta)
=\sum_p(\mu_p-\tau_p).
```

Under point-span order-$s$ osculating absorption in the complete
$\mathcal O_X(m)$ embedding, the fibre contains the order-$s$ fat point at
every reduced support and

``` math
\operatorname{length}(\Gamma_\eta)
\ge \binom{d+s-1}{d}\binom{d+m}{d}.
```

When $d(s-1)>s+1$, prescribed jets realize every integral defect from zero
through the extremal support size while all Milnor numbers remain $s^d$. The
degree threshold is sufficient rather than minimal. No exhaustive priority,
positive-characteristic, human-review, or formal-verification claim is made.

## Statement and scope

Let $`X^d\subset\mathbb P^{d+1}_{\mathbb C}`$ be a smooth hypersurface
of degree $`D\ge2`$. Write
``` math
\gamma_X:X\longrightarrow X^\vee\subset(\mathbb P^{d+1})^\vee
```
for the Gauss morphism. It is finite and birational, hence is the
normalization of the dual hypersurface; see, for example, Tevelev  and
the proof recalled in . For $`\eta=[W]\in X^\vee`$, put
``` math
\Gamma_\eta=X\times_{X^\vee}\operatorname{Spec}\kappa(\eta),
 \qquad Z=(\Gamma_\eta)_{\mathrm{red}}.
```
All fibre schemes in this paper are fibres over the reduced complex
point $`\eta`$; no claim about a scheme structure on a varying contact
locus is implicit.

Fix $`m\ge1`$, put $`H=\mathcal O_X(1)`$, and let
``` math
S_Z=\operatorname{Im}\!\left(
 H^0(Z,H^m|_Z)^*\longrightarrow H^0(X,H^m)^*\right).
```
Principal-parts evaluation defines the affine order-$`s`$ osculating
block
``` math
\widehat\operatorname{Osc}^s_p(H^m)=\operatorname{Im}\!\left(
 H^0((s+1)p,H^m|_{(s+1)p})^*
 \longrightarrow H^0(X,H^m)^*\right).
```

<div class="definition">

**Definition 1**. For $`1\le s\le m`$, the reduced fibre $`Z`$ is
*point-span $`s`$-osculating-absorbing* if
``` math
\widehat\operatorname{Osc}^s_p(H^m)\subseteq S_Z\qquad(p\in Z).
```

</div>

The first theorem separates three invariants that should not be
conflated: the cardinality of the reduced fibre, the length of the fibre
scheme, and the multiplicity of the dual. For an isolated analytic
hypersurface germ $`h`$, our conventions are
``` math
\mu(h)=\dim_\mathbb C\frac{\mathbb C\{z\}}{(\partial h)},
 \qquad
 \tau(h)=\dim_\mathbb C\frac{\mathbb C\{z\}}{(h,\partial h)}.
```

<div id="thm:local" class="theorem">

**Theorem 2** (Gauss fibre, Tjurina length, and dual defect). *Let
$`\eta=[W]\in X^\vee`$ and let $`h_p\in\mathbb C\{z_1,\ldots,z_d\}`$ be
a local equation of the tangent section $`X\cap W`$ at $`p\in Z`$. Then
``` math
\begin{align*}
 \widehat{\mathcal O}_{\Gamma_\eta,p}
 &\cong \mathbb C[[z_1,\ldots,z_d]]/(h_p,\partial_1h_p,\ldots,\partial_dh_p),\\
 \operatorname{length}(\Gamma_\eta)&=\sum_{p\in Z}\tau(h_p),\\
 \operatorname{mult}_\eta(X^\vee)&=\sum_{p\in Z}\mu(h_p).
\end{align*}
```
Consequently
``` math
\operatorname{mult}_\eta(X^\vee)-\operatorname{length}(\Gamma_\eta)
 =\sum_{p\in Z}\bigl(\mu(h_p)-\tau(h_p)\bigr)\ge0.       \tag{1}
```
Equality in *(1)* holds if and only if every $`h_p`$ is analytically
quasihomogeneous. Moreover,
``` math
\operatorname{Fitt}_0\Omega_{X/X^\vee,p}
   =(\det\operatorname{Hess}h_p)\subset\mathcal O_{X,p}^{\mathrm{an}}.       \tag{2}
```*

</div>

<div id="thm:floor" class="theorem">

**Theorem 3** (Fat-fibre floor forced by absorption). *Assume that $`Z`$
is point-span $`s`$-osculating-absorbing in the complete $`H^m`$
embedding. For every $`p\in Z`$ there is a closed immersion
``` math
\operatorname{Spec}(\mathcal O_{X,p}/\mathfrak m_{X,p}^s)\hookrightarrow\Gamma_\eta.
```
In particular, with $`N_{d,m}=\binom{d+m}{d}`$,
``` math
\operatorname{length}(\Gamma_\eta)
 \ge \binom{d+s-1}{d}|Z|
 \ge \binom{d+s-1}{d}N_{d,m}.                         \tag{3}
```
The local ramification equation in *(2)* has order at least $`d(s-1)`$
at every $`p\in Z`$. If $`s\ge2`$, the fibre scheme is nonreduced at
every support.*

</div>

The lower bound in (3) is not asserted to be optimal for $`s>1`$. Our
global examples instead show that all integral defects from zero through
the number of extremal supports occur while every local Milnor number
remains fixed at $`s^d`$.

<div id="thm:realization" class="theorem">

**Theorem 4** (Global realization of Tjurina–Milnor defects). *Let
$`d,m,s`$ be positive integers with $`1\le s\le m`$ and
``` math
d(s-1)>s+1.
```
Put $`N=N_{d,m}`$ and suppose
``` math
D\ge (s^d+2)N+1.                                      \tag{4}
```
For every integer $`q`$ with $`0\le q\le N`$, there exist a smooth
integral degree-$`D`$ hypersurface $`X^d\subset\mathbb P^{d+1}`$, a
hyperplane $`W`$, and $`\eta=[W]\in X^\vee`$ such that:*

1.  *$`Z=(\gamma_X^{-1}(\eta))_{\mathrm{red}}`$ has exactly $`N`$
    points;*

2.  *$`\dim S_Z=N< h^0(X,H^m)`$ and $`Z`$ is point-span
    $`s`$-osculating-absorbing;*

3.  *every tangent-section germ has Milnor number $`s^d`$; exactly $`q`$
    of them have Tjurina number $`s^d-1`$, and the others have Tjurina
    number $`s^d`$;*

4.  
    *``` math
    \operatorname{mult}_\eta(X^\vee)=s^dN,
     \qquad \operatorname{length}(\Gamma_\eta)=s^dN-q;
    ```*

5.  *the ramification equation has order exactly $`d(s-1)`$ at every
    point of $`Z`$.*

*The construction is existential up to nonempty Zariski-open choices.
The threshold *(4)* is not claimed to be minimal.*

</div>

# The local fibre ideal

Choose analytic coordinates centred at $`p\in Z`$ in which
``` math
X:\quad w=h(z_1,\ldots,z_d),
 \qquad W:\quad w=0,
 \qquad h\in\mathfrak m^2.
```
The tangent hyperplane at $`(z,h(z))`$ has equation
``` math
Y-\sum_i h_i(z)Z_i+\left(\sum_i z_i h_i(z)-h(z)\right)=0.
```
On the dual chart where the coefficient of $`Y`$ is one, the Gauss map
is therefore, up to harmless signs,
``` math
z\longmapsto\left(h_1(z),\ldots,h_d(z),
 h(z)-\sum_i z_i h_i(z)\right).                         \tag{5}
```
The extension of the maximal ideal of $`\eta`$ is
``` math
\begin{align*}
 I_{\eta,p}
 &=\left(h_1,\ldots,h_d,h-\sum_i z_i h_i\right)\\
 &=\left(h,h_1,\ldots,h_d\right).                       \tag{6}
\end{align*}
```
The second equality uses only $`\sum z_i h_i\in(h_1,\ldots,h_d)`$; it is
not an Euler or quasihomogeneity argument.

The scheme in (6) is the first-jet singularity scheme of the section
$`X\cap W`$. This is the hypersurface specialization of the
jet-incidence description of Aluffi–Cukierman . We use (6) as a local
calculation, not as a new general theorem about discriminants.

Because $`\gamma_X`$ is finite, the section singularity is isolated.
Passing between the analytic local ring and its completion preserves
finite colength. Thus (6) proves the first two identities of
Theorem <a href="#thm:local" data-reference-type="ref"
data-reference="thm:local">2</a>. The third is Dimca’s classical
multiplicity–Milnor formula ; see also Parusiński  and the modern use in
Dimca–Ilardi . Since
``` math
(\partial h)\subset(h,\partial h),
```
one has $`\tau(h)\le\mu(h)`$. Equality is equivalent to
$`h\in(\partial h)`$, and Saito’s theorem identifies this with analytic
quasihomogeneity . This proves (1).

To prove (2), differentiate (5). The Hessian description of Gauss
ramification is classical; compare Piene . Here the exact Fitting
equality follows directly from the local presentation. The first $`d`$
rows are the Hessian matrix $`\operatorname{Hess}h`$, while the last row
is
``` math
d\!\left(h-\sum_i z_i h_i\right)=-\sum_i z_i\,dh_i.
```
It is therefore the $`(-z_1,\ldots,-z_d)`$-linear combination of the
first rows. The maximal minors presenting $`\Omega_{X/X^\vee,p}`$
generate exactly $`(\det\operatorname{Hess}h)`$.

<div class="remark">

**Remark 5**. The fibre length is
$`\operatorname{length}(R/I_{\eta,p})=\tau(h)`$. It is not the
Hilbert–Samuel multiplicity $`e(I_{\eta,p},R)`$, and neither invariant
should be identified merely from the common ideal of the fibre. In
particular, the global multiplicity–Milnor formula does not turn fibre
length into Milnor number.

</div>

# Absorption creates infinitesimal fibre thickness

We recall the annihilator argument in the form needed here.

<div id="lem:annihilator" class="lemma">

**Lemma 6** (Local annihilator consequence). *If $`Z`$ is point-span
$`s`$-osculating-absorbing and $`a\in H^0(X,\mathcal I_Z\otimes H^m)`$,
then
``` math
a_p\in\mathfrak m_{X,p}^{s+1}H_p^m\qquad(p\in Z).
```*

</div>

<div class="proof">

*Proof.* The annihilator of $`S_Z`$ is
$`H^0(X,\mathcal I_Z\otimes H^m)`$. The annihilator of
$`\widehat\operatorname{Osc}^s_p(H^m)`$ consists of sections whose germs
vanish modulo $`\mathfrak m_{X,p}^{s+1}`$. The defining containment of
osculating blocks reverses under annihilators and gives the assertion. ◻

</div>

Let $`\ell_W`$ be a linear equation of $`W`$. For each $`p\in Z`$,
choose a section $`g_p\in H^0(X,H^{m-1})`$ nonzero at $`p`$, with
$`g_p=1`$ when $`m=1`$. The section $`\ell_Wg_p`$ of $`H^m`$ vanishes on
all of $`Z`$. Lemma <a href="#lem:annihilator" data-reference-type="ref"
data-reference="lem:annihilator">6</a> and division by the unit
$`(g_p)_p`$ give
``` math
(\ell_W|_X)_p\in\mathfrak m_{X,p}^{s+1}.                        \tag{7}
```
In the graph coordinates of
Section <a href="#sec:local" data-reference-type="ref"
data-reference="sec:local">2</a>, (7) is precisely
$`h_p\in\mathfrak m_p^{s+1}`$. Hence
``` math
I_{\eta,p}=(h_p,\partial h_p)\subset\mathfrak m_p^s.             \tag{8}
```
The reversed ideal inclusion in (8) gives the asserted closed immersion
$`\operatorname{Spec}(\mathcal O_{X,p}/\mathfrak m_p^s)\hookrightarrow\Gamma_\eta`$
and
``` math
\tau(h_p)\ge\operatorname{length}(\mathcal O_{X,p}/\mathfrak m_p^s)
 =\binom{d+s-1}{d}.                                      \tag{9}
```

Order-$`s`$ absorption contains tangent absorption. The exact support
floor from , ultimately based on the point-span rank theorem , is
``` math
|Z|\ge N_{d,m}.
```
Summing (9) proves (3). Finally, every Hessian entry belongs to
$`\mathfrak m_p^{s-1}`$, so its determinant belongs to
$`\mathfrak m_p^{d(s-1)}`$. The determinant is not the zero germ because
the finite birational Gauss map is generically separable over
$`\mathbb C`$. If $`s\ge2`$, (9) gives local fibre length greater than
one at every support. This completes the proof of
Theorem <a href="#thm:floor" data-reference-type="ref"
data-reference="thm:floor">3</a>.

# A defect-one isolated germ

The next calculation supplies the two analytic types used in the global
construction.

<div id="lem:defect" class="lemma">

**Lemma 7** (Fermat and defect-one germs). *Let $`s\ge1`$ and
``` math
f_0=\sum_{i=1}^d x_i^{s+1}.
```
Then $`\mu(f_0)=\tau(f_0)=s^d`$. If $`d(s-1)>s+1`$ and
$`\lambda\in\mathbb C^*`$, put
``` math
f_1=\sum_{i=1}^d x_i^{s+1}
      +\lambda\prod_{i=1}^d x_i^{s-1}.                  \tag{10}
```
Then
``` math
\mu(f_1)=s^d,
 \qquad \tau(f_1)=s^d-1.                                \tag{11}
```
For both germs the Hessian determinant has order exactly $`d(s-1)`$.*

</div>

<div class="proof">

*Proof.* For $`f_0`$ the gradient ideal is $`(x_1^s,\ldots,x_d^s)`$, and
Euler’s formula puts $`f_0`$ in that ideal. This gives the first
assertion.

Put $`r=\prod_i x_i^{s-1}`$ and $`k=d(s-1)`$. The hypothesis $`k>s+1`$
means that (10) has Fermat initial form. The initial forms of its
partial derivatives are $`(s+1)x_i^s`$ and form a homogeneous regular
sequence. Therefore the associated graded Milnor algebra has basis
``` math
x_1^{a_1}\cdots x_d^{a_d},\qquad 0\le a_i\le s-1,
```
and $`\mu(f_1)=s^d`$. The class of $`r`$ is nonzero and spans the socle.
In the Milnor algebra, Euler’s identity reads
``` math
0=\sum_i x_i\partial_i f_1=(s+1)[f_0]+k\lambda[r],
```
so
``` math
[f_1]=\left(1-\frac{k}{s+1}\right)\lambda[r]\ne0.
```
It spans a one-dimensional ideal. Quotienting the Milnor algebra by this
class proves $`\tau(f_1)=s^d-1`$. The leading Hessian determinant in
both cases is a nonzero scalar multiple of $`r`$, proving the final
assertion. ◻

</div>

For the family (10), the plane case first satisfies $`2(s-1)>s+1`$ at
$`s=4`$. Its corresponding fixture is
``` math
f_1=x^5+y^5+x^3y^3,\qquad \mu(f_1)=16,\quad\tau(f_1)=15. \tag{12}
```
It is included in the exact replay accompanying the paper. Equation (12)
is also a counterexample to the stronger but false bound
$`\tau\ge s^d`$.

# Simultaneous analytic types from prescribed jets

We give the construction in enough detail to isolate its degree
bookkeeping. Its interpolation and extension architecture is adapted
from the preceding proper-span construction . Compare also the
squared-point independence criterion of Ballico–Chiantini . The general
fact that isolated hypersurface singularities can be realized in a
hyperplane section of a smooth hypersurface is classical ; what is
controlled below is the exact support, absorption, two simultaneous
analytic types, defect ladder, and an explicit sufficient degree.

<div id="lem:jets" class="lemma">

**Lemma 8** (Simultaneous jets from separators). *Let $`p_1,\ldots,p_t`$
be distinct points of $`\mathbb P^d`$ and let $`a_i\ge0`$. If
``` math
k\ge\sum_{i=1}^t(a_i+1)-1,
```
then restriction is surjective:
``` math
H^0(\mathbb P^d,\mathcal O(k))\longrightarrow
 \bigoplus_{i=1}^t
 H^0\!\left(\mathcal O(k)\otimes\mathcal O_{\mathbb P^d,p_i}/\mathfrak m_{p_i}^{a_i+1}\right).
```*

</div>

<div class="proof">

*Proof.* For $`i\ne j`$, choose a linear form $`\ell_{ij}`$ vanishing at
$`p_j`$ and nonzero at $`p_i`$. The product
``` math
P_i=\prod_{j\ne i}\ell_{ij}^{a_j+1}
```
kills every other target and is a unit at $`p_i`$. Forms of degree
$`a_i`$ realize all order-$`a_i`$ jets at $`p_i`$; multiplying them by
$`P_i`$ isolates that target. The common degree is at most
$`\sum_j(a_j+1)-1`$. Multiplication by a form nonzero at all supports
raises the degree. ◻

</div>

Choose $`N=N_{d,m}`$ distinct points $`Z\subset W\cong\mathbb P^d`$ such
that
``` math
H^0(W,\mathcal O_W(m))\xrightarrow{\sim}H^0(Z,\mathcal O_Z(m)).       \tag{13}
```
Such a set exists because the evaluation lines of all points span the
dual of $`H^0(W,\mathcal O_W(m))`$; choose a basis among them. Set
``` math
a=s^d+1,\qquad E=(a+1)N=(s^d+2)N.
```
The binomial theorem gives $`d(s-1)\le s^d-1<a`$, so the perturbation
term in $`f_1`$ is visible in the prescribed $`a`$-jet. At each point
prescribe the $`a`$-jet of either $`f_0`$ or $`f_1`$ from Lemma
<a href="#lem:defect" data-reference-type="ref"
data-reference="lem:defect">7</a>, choosing $`f_1`$ at exactly $`q`$
supports. Lemma <a href="#lem:jets" data-reference-type="ref"
data-reference="lem:jets">8</a> supplies a section
$`f_*\in H^0(W,\mathcal O_W(D))`$ with those jets. Let
``` math
V=H^0(W,\mathcal I_{(a+1)Z}(D)),\qquad \mathcal A=f_*+V.
```

<div id="prop:section" class="proposition">

**Proposition 9** (A section with exactly the prescribed singularities).
*If $`D\ge E+1`$, there is $`f\in\mathcal A`$ such that
$`V(f)\subset W`$ is smooth away from $`Z`$ and has at the supports
precisely the prescribed contact-equivalence classes.*

</div>

<div class="proof">

*Proof.* Greuel–Lossen–Shustin prove that an isolated germ is contact
$`(\tau+1)`$-determined . Both germs have $`\tau\le s^d`$, so their
prescribed $`a=s^d+1`$ jets determine their contact classes.

Fix $`u\in W\setminus Z`$. For every $`p\in Z`$, choose a hyperplane
$`\ell_{p,u}`$ through $`p`$ but not $`u`$. The section
``` math
A_u=\prod_{p\in Z}\ell_{p,u}^{a+1}
```
has degree $`E`$, belongs to $`\mathcal I_{(a+1)Z}`$, and is a unit on
the first neighbourhood of $`u`$. Since $`D-E\ge1`$, multiplication by
$`A_u`$ shows that $`V`$ surjects onto the first jets at $`u`$. Thus the
affine condition $`j^1_u f=0`$ has codimension $`d+1`$ in
$`\mathcal A`$. Its incidence over the $`d`$-dimensional base
$`W\setminus Z`$ has dimension at most $`\dim\mathcal A-1`$. A member
outside its closure is smooth away from $`Z`$; finite determinacy gives
the claimed germs at $`Z`$. ◻

</div>

Embed $`W=V(y)`$ in $`\mathbb P^{d+1}`$ and lift $`f`$ independently of
$`y`$. For $`G\in H^0(\mathbb P^{d+1},\mathcal O(D-1))`$, put
``` math
F_G=f+yG.
```

<div id="prop:extension" class="proposition">

**Proposition 10** (Smooth extension and exact Gauss support). *There is
$`G`$, nonzero at every point of $`Z`$, such that $`X=V(F_G)`$ is smooth
and integral and
``` math
(\gamma_X^{-1}([W]))_{\mathrm{red}}=Z.
```
At each $`p\in Z`$, the section germ $`W|_X`$ is contact equivalent to
the prescribed germ of $`f`$.*

</div>

<div class="proof">

*Proof.* On $`W\setminus Z`$, smoothness follows from
Proposition <a href="#prop:section" data-reference-type="ref"
data-reference="prop:section">9</a>. At $`p\in Z`$, one has
$`dF_G=G(p)\,dy`$, so $`G(p)\ne0`$ makes $`X`$ smooth. Off $`W`$,
multiplication by the unit $`y`$ and the first-jet generation of
$`\mathcal O(D-1)`$ show that the singularity condition has codimension
$`d+2`$ in the space of $`G`$’s over a $`(d+1)`$-dimensional base. The
closure of the incidence image is therefore a proper closed subset of
the space of $`G`$’s. Avoid it together with the finitely many
hyperplanes $`G(p)=0`$.

The hypersurface sequence and $`H^1(\mathbb P^{d+1},\mathcal O(-D))=0`$
give $`H^0(X,\mathcal O_X)=\mathbb C`$, so the smooth hypersurface is
connected and hence integral. Its section by $`W`$ is $`V(f)`$ and has
singular locus exactly $`Z`$. If a point maps under the Gauss map to
$`[W]`$, it lies in its tangent hyperplane $`W`$; within $`W`$, this
happens exactly where $`V(f)`$ is singular. This proves the exact
reduced fibre identity. Locally on $`X`$,
``` math
y=-f/G,
```
which differs from $`f`$ by a unit and therefore has the prescribed
contact class. ◻

</div>

# Proof of the realization theorem

Apply Propositions <a href="#prop:section" data-reference-type="ref"
data-reference="prop:section">9</a>
and <a href="#prop:extension" data-reference-type="ref"
data-reference="prop:extension">10</a>. Since $`D>m`$, restriction gives
``` math
H^0(\mathbb P^{d+1},\mathcal O(m))\xrightarrow{\sim}H^0(X,H^m).
```
If a degree-$`m`$ ambient form $`Q`$ vanishes on $`Z`$, (13) says that
$`Q|_W=0`$, so $`Q=yR`$. At every support, $`y|_X=-f/G`$ has order
$`s+1`$. Therefore every section of $`H^m`$ vanishing on $`Z`$ vanishes
to order $`s+1`$ at each support. The reverse-annihilator argument of
Lemma <a href="#lem:annihilator" data-reference-type="ref"
data-reference="lem:annihilator">6</a> proves order-$`s`$ absorption.

Equation (13) also gives
``` math
\dim S_Z=N.
```
This span is proper because
``` math
h^0(X,H^m)=\binom{d+m+1}{d+1}>\binom{d+m}{d}=N.
```

Each prescribed germ has Milnor number $`s^d`$. Exactly $`q`$ have
Tjurina number $`s^d-1`$ and the others have Tjurina number $`s^d`$.
Theorem <a href="#thm:local" data-reference-type="ref"
data-reference="thm:local">2</a> now gives
``` math
\begin{align*}
 \operatorname{mult}_{[W]}(X^\vee)&=Ns^d,\\
 \operatorname{length}(\Gamma_{[W]})&=(N-q)s^d+q(s^d-1)=Ns^d-q.
\end{align*}
```
Over $`\mathbb C`$, both $`\mu`$ and $`\tau`$ are invariants of analytic
contact equivalence; see . For the Hessian assertion, the interpolation
gives $`f-f_i\in\mathfrak m^{a+1}`$ with $`a+1>s+1`$, and on $`X`$ one
has $`y|_X=uf`$ for the unit $`u=-1/G`$. Thus the degree-$`(s+1)`$
initial form of $`y|_X`$ is the Fermat form of $`f_i`$, up to the
nonzero scalar $`u(0)`$ and the invertible linear part of a coordinate
change. Its initial Hessian determinant remains nonzero of degree
$`d(s-1)`$. Lemma <a href="#lem:defect" data-reference-type="ref"
data-reference="lem:defect">7</a> now gives the claimed exact order and
completes the proof of
Theorem <a href="#thm:realization" data-reference-type="ref"
data-reference="thm:realization">4</a>.

# Context, reproducibility, and limitations

We use the scheme-theoretic jet-incidence formulation of
Aluffi–Cukierman ; the multiplicity–Milnor identity is due to Dimca ,
with broader results by Parusiński ; and the equality criterion
$`\mu=\tau`$ is Saito’s theorem . The point-span floor and the
prescribed-jet extension architecture are authorial antecedents , not
independent validation. The contribution claimed here is limited to the
exact combination of the absorption-forced fat-fibre and ramification
bounds with the explicit simultaneous defect realization at the stated
sufficient degree.

The accompanying script uses exact rational arithmetic to compute local
Macaulay quotients for the defect-one fixtures
$`(d,s)=(2,4),(3,3),(4,2)`$, verify the predicted Milnor and Tjurina
numbers, check the Euler and initial Hessian terms in (12), and audit
finite grids of the displayed integer formulae. It does not mechanize
analytic coordinates, finite determinacy, incidence dimension counts, or
literature priority.

The limitations are material:

- Everything is over $`\mathbb C`$. No positive-characteristic extension
  of the Milnor, Saito, or separability arguments is asserted.

- The fibre is the complete scheme-theoretic fibre of the Gauss
  normalization over one reduced dual point. Arbitrary subsets of its
  support are not covered.

- The lower length floor (3) is not proved sharp for $`s>1`$. The
  realization theorem controls a different, near-Milnor range of
  lengths.

- Formula (2) describes the Fitting ramification scheme on the normal
  source. No identification of its image with a canonical branch or
  discriminant scheme on the nonnormal dual is claimed.

- The degree threshold (4) is deliberately sufficient and may be far
  from minimal. No classification of equality cases or exhaustive
  priority review is claimed.

- The computational replay certifies only its finite fixtures and
  arithmetic grids. It is not formal proof or human peer review.

# Conclusion

Osculating absorption thickens a special Gauss fibre scheme, not merely
its reduced support. The thickness is measured locally by Tjurina
algebras, while the singularity of the dual is measured by Milnor
numbers. Their difference is exactly the total quasihomogeneity defect
of the tangent section singularities. The resulting dictionary
``` math
\text{fat Gauss fibre}\longleftrightarrow\sum\tau_p,
 \qquad
 \text{dual multiplicity}\longleftrightarrow\sum\mu_p
```
both prevents a common numerical conflation and yields the global floor
proved here under the specific absorption hypothesis. Prescribed finite
jets show that the two invariants can be separated one unit at a time
across an extremal large fibre. The optimal Tjurina floor and the
minimal ambient degree are not determined here.

<div class="thebibliography">

99

P. Aluffi and F. Cukierman, *Multiplicities of discriminants*,
Manuscripta Math. **78** (1993), 245–258.
<https://doi.org/10.1007/BF02599311>

E. Ballico and L. Chiantini, *On the Terracini locus of projective
varieties*, Milan J. Math. **89** (2021), 1–17.
<https://doi.org/10.1007/s00032-020-00324-5>

A. Dimca, *Milnor numbers and multiplicities of dual varieties*, Rev.
Roumaine Math. Pures Appl. **31** (1986), no. 6, 535–538.

A. Dimca, *Topics on Real and Complex Singularities*, Advanced Lectures
in Mathematics, Friedr. Vieweg & Sohn, Braunschweig, 1987.
[doi:10.1007/978-3-663-13903-4](https://doi.org/10.1007/978-3-663-13903-4)

A. Dimca and G. Ilardi, *On the duals of smooth projective complex
hypersurfaces*, Publ. Mat. **68** (2024), 431–438.
<https://doi.org/10.5565/PUBLMAT6822404>

L. Eriksson, *The exact rank floor for point-span tangent absorption in
arbitrary characteristic*, ARR-2026-2MHNZRRJP49Y9SWP, v3 (2026).
<https://arr-research.github.io/papers/ARR-2026-2MHNZRRJP49Y9SWP/versions/v3/>

L. Eriksson, *Exact floors and proper-span extremizers for higher
osculating absorption*, ARR-2026-66Q8M61AA196T8BC, v2 (2026).
<https://arr-research.github.io/papers/ARR-2026-66Q8M61AA196T8BC/versions/v2/>

L. Eriksson, *Exact multiplicity floors for dual singularities from
absorbing Gauss fibres*, ARR-2026-0WAPCGQHNC82S8VJ, v1 (2026).
<https://arr-research.github.io/papers/ARR-2026-0WAPCGQHNC82S8VJ/>

G.-M. Greuel, C. Lossen, and E. Shustin, *Introduction to Singularities
and Deformations*, Springer Monographs in Mathematics, Springer, 2007.
<https://doi.org/10.1007/3-540-28419-2>

A. Parusiński, *Multiplicity of the dual variety*, Bull. London Math.
Soc. **23** (1991), no. 5, 429–436.
<https://doi.org/10.1112/blms/23.5.429>

R. Piene, *Polar classes of singular varieties*, Ann. Sci. Ècole Norm.
Sup. (4) **11** (1978), no. 2, 247–276.
<https://doi.org/10.24033/asens.1346>

K. Saito, *Quasihomogene isolierte Singularitäten von Hyperflächen*,
Invent. Math. **14** (1971), 123–142.
<https://doi.org/10.1007/BF01405360>

E. A. Tevelev, *Projective Duality and Homogeneous Spaces*,
Encyclopaedia of Mathematical Sciences 133, Springer, 2005.
<https://doi.org/10.1007/b138367>

</div>
