# Independent review of the balanced-four coefficient and finite cell algorithm

Source reviewed in full: `work/cycle3/commutator/balanced_stability.md`, final reviewed SHA-256 `26869d8b74fc4ce32ae1ba93620235792bdfc095474f68960066e17423f2b26e`, 5 September 2026. The full initial reading covered SHA `b6fbf489e91be79e10c126651b35be157b6bc1ffc141167b0531d73be88751af`; the subsequent title/theorem-label clarification and formula (6) rewrite using ones/zeros vectors were then read and found mathematically equivalent. This review covers every statement and proof in Sections 1–7, the abstract and references, together with the pinned finite certificates. Later manuscript revisions are not automatically covered by this hash.

The balanced (4,4) coefficient **4/7 passes this independent review**. I found no mathematical gap in the finite vertex argument, the all-ambient sharpness sandwich, or the proposed general reduction, subject to the precise scope below. This is an independent agent review in the same model family, not independent human peer review or a proof-assistant verification.

The independent replay is `independent_lr_geometry_review.py`; its report is `independent_lr_geometry_review.json`. It imports neither the author's `geometry.py` nor the recursive Horn generator. It reconstructs the cell vertices and edges from their explicit formula and generates admissible Horn indices by Littlewood–Richardson skew-tableau counting. In dimension eight the 8,752 indices agree exactly with the author's recursive list, with counts 36, 462, 2120, 3516, 2120, 462, 36. The LR multiplicities are 8,499 ones, 247 twos and six threes. The independently constructed cut set has exactly 89 ordered vertices. All 778,928 rational Horn inequalities and all proposed stability inequalities pass. The report pins the inspected author certificate and the review script by SHA-256.

Classical Horn sufficiency remains imported. These finite computations verify its hypotheses, not its mathematical proof. The exact witnesses establish upper bounds on cost at all vertices; the sharp lower bound below supplies optimality of the coefficient without needing a dual certificate for every vertex cost.

## All-dimensional sharpness

Let R,S be positive semidefinite and isospectral with ordered spectrum s, with F=R−S. Loewner order F≤R and −F≤S gives s_4≥a_4 and s_2≥b_2. Apply the size-two Horn index

I={1,3}, J={1,d−1}, K={2,d−1}

to −F=S+(−R). Its index-sum condition holds, and its three recursive size-one tests are 2≤3, d≤d and 4≤d. Thus it is admissible for d≥4. In the spectra considered here there are at least four positive and two negative eigenvalues, so d≥6 and the selected target coordinates are b_2 and −a_2. Extra zeros do not change these positions.

The inequality is

s_1+s_3−s_2−s_d ≥ b_2−a_2.

Consequently tr(s) ≥ s_1+s_2+s_3+s_4 ≥ 3b_2−a_2+a_4+s_d ≥ 3b_2−a_2+a_4. No normalization s_d=0 is needed. For a=(5/8,1/8,1/8,1/8) and b=(1/2,1/2,0,0) this gives 3/2. The exact dimension-eight witness (3/4,1/2,1/8,1/8,0,0,0,0) has that trace, and zero extension supplies the same upper bound in every d≥8. The distance is 7/4.

For b_eta=(1/2−eta,1/2−eta,eta,eta), with 0<eta<1/8, the exact inertia is (4,4), D*=7/4−4eta, and the lower bound is 3/2−3eta. The proven global 4/7 inequality gives the upper bound 3/2+(16/7)eta. This sandwich proves that the deficit-to-distance ratio tends to 4/7 for each fixed ambient dimension d≥8, including every prescribed number d−8 of extra zeros. It does not assume general invariance of cost under zero padding.

## General cell geometry

Write Q_r={a_1≥...≥a_N≥0, sum a_i=1, a_r≥1/N≥a_{r+1}}, for 1≤r<N, and u=(1/N,...,1/N). Every a in Q_r other than u is uniquely expressible as

a=(1−t)u+t b, t=1−N a_N>0,

where b_N=0 and b belongs to Q_r. Hence Q_r is a pyramid over its section a_N=0.

On that base put x_i=a_i−1/N for i≤r, and y_j=1/N−a_j for j>r. The x_i are nonnegative decreasing and the y_j nonnegative increasing, with y_N=1/N and equal total excess and deficit. Use nonnegative successive differences alpha_k=x_k−x_{k+1}, with x_{r+1}=0, and beta_l=y_{l+1}−y_l, with y_r=0. Here 1≤k≤r≤l<N. They satisfy precisely

sum_l beta_l=1/N, and sum_k k alpha_k=sum_l (N−l) beta_l.

Both an alpha and a beta must be positive. A vertex has exactly one positive alpha and one positive beta; otherwise the two linear equations leave a nonzero feasible perturbation on its positive support. Conversely each such pair is a feasible vertex. Setting beta_l=1/N and alpha_k=(N−l)/(Nk) gives

v_kl=((N−l+k)/(Nk) repeated k times, 1/N repeated l−k times, 0 repeated N−l times).

This also proves the face and edge description: the support inequalities give the face lattice of the product of simplices Delta_(r−1) × Delta_(N−r−1). Distinct base vertices are adjacent exactly when they share k or l. The pyramid adds an edge from u to every base vertex. Across all r, the union has

V=1+binom(N,2), E=binom(N,2)+2 binom(N,3)=N(N−1)(2N−1)/6.

The base is combinatorially a product of simplices; an affine-product assertion is unnecessary and should not be substituted without proof.

On each Q_r, U(a)=sum|a_i−1/N| and E(a)=2(1−a_1) are affine. On Q_r×Q_s the two orientations of D* are affine and their equality is q(a)=q(b), q=E−U. A single hyperplane cut of a polytope introduces vertices only where it crosses an edge, unless an edge lies in the hyperplane, in which case its endpoints suffice. Every edge of a product is vertex×edge or edge×vertex. Thus the explicitly enumerated set consists of all products of base vertices plus strict crossing points of q(a)=q(b) along these product edges, including the symmetric orientation. No intersection in the relative interior of a higher-dimensional face can become a vertex after only one cut. This proves completeness of the construction, not just the observed small-N counts.

There are at most V^2+2VE=O(N^5) resulting vertices. The review also checked the explicit count formula and construction for N=2,...,8, yielding cut counts 4,22,89,267,628,1354,2611. These finite checks supplement the argument; they do not replace it.

## Exact gamma_(N,d) algorithm and required qualifications

Fix N≥2 and d≥2N. The ordered target (a,0_(d−2N),−reverse(b)) depends linearly on (a,b). The fixed-dimensional spectral cost kappa_d is convex and polyhedral by the Horn linear program. On every cut cell D* is affine and nonnegative. If gamma is the minimum of (H_N−kappa_d(v))/D*(v) over the finitely many cut vertices with D*(v)>0, then concavity of H_N−kappa_d and affinity of D* prove the inequality throughout every cell. The D*=0 vertices cause no problem: the known ceiling gives nonnegative deficit there. They are precisely the two spike/flat orientations.

Conversely, each vertex with D*>0 can be approached by strictly positive a,b via mixing both lists with u. Fixed-dimension polyhedral continuity gives convergence of both cost and distance, so the infimum over the exact-inertia stratum equals this finite minimum. The established extremizer classification implies positive deficit away from the two zero-distance endpoints and therefore gamma>0. Rational LP optima and rational vertices imply rational gamma.

The reduction uses O(N^5) **Horn LPs**. It does not establish polynomial total running time or a polynomial-sized Horn system: dimension d can make each LP large. The exact algorithm must evaluate the actual LP optimum at each vertex, or provide matching primal/dual certificates where needed. Arbitrary primal upper witnesses alone generally certify a lower bound for gamma, not its exact value. Balanced N=4 is exact because the separate dimension-independent boundary sandwich supplies the matching upper bound for gamma.

No external priority search was conducted in this review. The balanced-four theorem and the general reduction should be compared with the existing local spectral-LP framework when making novelty claims.

## Review of the finished manuscript

The finished Lemma 1 uses the equivalent full-cone alpha/beta parameterization with `sum beta<=1/N`. Its nonzero vertices must saturate that bound by a scaling argument. For fixed nonempty positive supports of sizes p and q on the base, the two equality rows are independent because one has a nonzero alpha column and the other has only beta columns. The strictly positive point is in the relative interior of its support face, so its face dimension is exactly p+q−2. This validates both the vertex and edge assertions, including the one-dimensional and simplex endpoint cases r=1 and r=N−1.

Section 2's epigraph argument is valid with the ordered trace-zero chamber as the declared domain. Projection of its finite polyhedron is again a polyhedron. Upward closure in the cost coordinate leaves finitely many affine lower bounds, together with domain constraints; finiteness throughout the chamber makes their maximum the value function there. This proves continuity at the boundary relative to that closed chamber. It does not invoke the false matrix-convexity claim or general zero-padding invariance.

Theorem A correctly restricts N≥2 and d≥2N. The denominator is nonzero at the minimizing vertex; mixture with u therefore preserves a positive limiting denominator. The quoted positive lower stability coefficient in Theorem 3 of the exact predecessor [ARR v1](https://arr-research.github.io/papers/ARR-2026-24M24KDPZK8HDBQ9/) justifies positivity uniformly before optimizing. Rationality uses exact LP optima, not the exploratory numerical proposals. The manuscript explicitly separates O(N^5) LP count from dependence of each Horn program on d.

Theorem B correctly uses the 89 primal witnesses for its global lower stability estimate, then the separate lower obstruction and exact perturbation to prove optimality in each fixed ambient dimension. The reverse coefficient is appropriately attributed to Theorem 3 and Section 5.4 of the predecessor. Lemma 3 is valid for all its stated spectra; its requirement of four positive and two negative eigenvalues already implies d≥6, within the admissible d≥4 Horn family.

Primary-source check on 5 September 2026: [Fulton, full text](https://arxiv.org/pdf/math/9908012), printed pages 4–5, equations (8)–(10) and Theorem 1, contains the index convention and sufficiency used here. [Knutson–Tao](https://arxiv.org/abs/math/9807160) is the cited saturation/Horn machinery. [Angel–Schechtman](https://arxiv.org/abs/1503.07980) studies a general commutator with a mixed operator/Hilbert–Schmidt product estimate, supporting the manuscript's distinction of objectives. These targeted source checks do not establish global bibliographic priority or validate every item in the author's separate search log.

The nonblocking editorial recommendation has been resolved in the final reviewed hash: the title and theorem label now use “balanced inertia (4,4)”. This avoids confusion with the earlier dimension-four inverse-commutator problem. The replacement of formula (6)'s underbraces by vectors of indicated lengths preserves exactly the same coordinates. No blocking mathematical finding or unresolved editorial correction remains in this review.

## Final presentation revision

The final prose-math conversion was read in full together with its 73 recorded substitution entries and the presentation script. Every substitution preserves its mathematical meaning. The independent reverse-conversion script recovered the exact previously reviewed manuscript SHA-256 d862633c133f480d4a0ada1bdc6275a2be7094a6df09fc59da9406be5bd1a1e9, while preserving every display-equation block. Thus the final source SHA-256 26869d8b74fc4ce32ae1ba93620235792bdfc095474f68960066e17423f2b26e differs only by the inspected presentation operations. No computational replay of unchanged mathematical certificates was needed. The independent evidence is independent_presentation_check.py and independent_presentation_check.json. This check concerns source equivalence, not PDF rendering.
