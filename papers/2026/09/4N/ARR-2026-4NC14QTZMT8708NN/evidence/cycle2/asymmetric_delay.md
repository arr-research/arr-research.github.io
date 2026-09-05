# An exact asymmetric one-state error–delay law

Lluis Eriksson — research manuscript, 5 September 2026. This is a new local derivation relative to the inspected ARR predecessor and the prior symmetric calculation. Separate internal review and replay are recorded alongside the manuscript. No publication, external refereeing, or priority certification is claimed.

## Result and scope

Use the same model as `outputs/research/passive_delay.md`: square rational-inner matrices of McMillan degree at most one, one fixed input, free output phase, squared chordal node error, and global angular trace-delay peak at most T. The output targets are e2 at z=1 and e1 at z=e^(-ia), e^(ib), where 0<a,b<pi. Every result below covers every ambient port count N>=2.

Write u=cot(a/2)>0 and v=cot(b/2)>0. The main concrete asymmetric pattern is

    u=2, v=1;    repeated-target nodes (3-4i)/5 and i.

For T>=1 put

    p=(T+T^(-1))/2,  q=(T-T^(-1))/2,
    A(t)=(sqrt(t^2+p^2)+q)^2,
    D(t)=(2+t)(1-t).

There is a unique minimizer t_T of A(t)/D(t) on (-2,1). It belongs to (-1/2,0), and is equivalently the unique root in that interval of the **unsquared** equation

    2t D(t) = sqrt(t^2+p^2)(sqrt(t^2+p^2)+q)(-1-2t).       (1)

**Theorem A.** For this fixed asymmetric pattern, for every T>=1,

    E_(1,T)^2 = 1 / (2 + A(t_T)/D(t_T)).                    (2)

This is an exact algebraic law specified by a unique real root, not a numerical optimization prescription. An attaining two-port lossless matrix is constructed below and has peak exactly T. For 0<=T<1 the minimum is 1/sqrt(2). The same result holds after embedding in any number of ports. Moreover,

    lim_(T->infinity) T E_(1,T) = 3/2.                     (3)

At T=1, t_T=3-sqrt(10), and

    E_(1,1)^2=(sqrt(10)+1)/(2sqrt(10)+4).

At T=2, t_T is the unique root in (-271/1000,-270/1000) of

    20t^4+264t^3-697t^2-300t-25=0,

and E_(1,2)^2 is approximately 0.2581683140. Other quartic roots must not be substituted: the sign in (1) matters.

**Theorem B (all asymmetric gaps at the first nonzero cap).** Put gamma=(a+b)/2 and delta=(b-a)/2. At T=1,

    E_(1,1)^2=(1+cos(gamma))/(2+cos(delta)+cos(gamma)).      (4)

Thus the asymmetry cannot be absorbed into the geometric mean of the two cotangents while preserving the original global delay cap. For example u=3, v=1/3 gives repeated nodes (4-3i)/5 and (-4+3i)/5 and exact E^2=5/13. The geometric-mean substitution into the symmetric formula would give 1/3.

The general lemma below also gives a checkable exact law for further pairs (u,v) and caps T. It states explicitly when its lower bound is sharp. A complete classification for all asymmetric gaps and all T is not claimed.

## 1. Denominators as a two-dimensional ellipse

A nonconstant degree-one rational-inner matrix has one rank-one Blaschke–Potapov factor, with scalar zero alpha. Its trace delay is the Poisson kernel, so its global peak is (1+|alpha|)/(1-|alpha|). This classical fact is the only conversion between denominator shape and delay used here.

Set s=cot(phi/2), so z=(s+i)/(s-i), with z=1 represented by s=infinity. A routed column has a linear vector numerator and a common scalar linear denominator in z. After the substitution and an irrelevant common scale, write its squared numerator coordinates as nonnegative real quadratic polynomials Q_j(s), and their sum as

    H(s)=s^2+2Bs+C,                 M=[[1,B],[B,C]].

The normalization is possible because the original denominator is nonzero at z=1. The actual circle denominator intensity is H(s)/(1+s^2); its maximum/minimum ratio is the eigenvalue ratio of M. Therefore the cap D(S)<=T is exactly

    lambda_max(M)/lambda_min(M) <= T^2.

For a constant router one may use M=I. For T>=1, using p,q above and p^2-q^2=1, the cap is equivalently

    B^2 + (C-(1+2q^2))^2/(4p^2) <= q^2.                 (5)

Indeed the eigenvalue-ratio condition is

    (1-C)^2+4B^2 <= ((T^2-1)/(T^2+1))^2(1+C)^2,

which rearranges to (5); the ellipse lies in the positive-definite region. The endpoint T=1 reduces to B=0,C=1.

For any real t, maximizing the linear functional H(t)=t^2+2Bt+C over this ellipse gives

    H(t) <= A(t)=(r+q)^2,             r=sqrt(t^2+p^2),    (6)
    B_t=qt/r,
    C_t=1+2q^2+2p^2q/r.

These displayed B_t,C_t attain (6), and for T>1 are its unique maximizer. For T=1 the ellipse is already a single point. No angular reparameterization is assumed to preserve peak delay: (5) is imposed in the original frequency coordinate.

## 2. A lower certificate valid in every number of ports

Let e denote squared worst-node error. The e2 intensity Q=Q_2 satisfies

    leading_coefficient(Q) >= 1-e,
    Q(-u) <= e H(-u),   Q(v) <= e H(v),   Q(s)>=0 for real s.

The last two inequalities follow even with extra output directions, since their power only increases the error from the e1 target.

For every polynomial R of degree at most two, and every -u<t<v, its leading coefficient obeys the Lagrange identity

    lc(R) = R(-u)/((u+v)(u+t))
          + R(v)/((u+v)(v-t)) - R(t)/((u+t)(v-t)).       (7)

Apply (7) to Q, drop its final nonpositive term, and apply it again to H, whose leading coefficient is one. With D(t)=(u+t)(v-t), this gives

    1-e <= e(1+H(t)/D(t)) <= e(1+A(t)/D(t)).

Consequently, for arbitrary u,v>0,

    E_(1,T)^2 >= 1/(2+F_*),
    F_* = min_(-u<t<v) F(t),   F(t)=A(t)/D(t).           (8)

This proof uses neither a restriction to real numerator coefficients nor an assumption that the routed column lies in the target plane.

## 3. The scalar minimum and the exact sharpness criterion

The function A is strictly convex: A''(t)=2+2q p^2/(t^2+p^2)^(3/2)>0. The function D is positive on (-u,v), with D''=-2. The numerator of F' is N=A'D-AD', and

    N'=A''D+2A>0.

Also F tends to infinity at both endpoints. Thus it has exactly one critical point t_*, which is its global minimum. If u>v, then t_* lies strictly between (v-u)/2 and 0; for u=v it is zero; the reflected statement holds for u<v. The claim follows by inspecting F' at zero and at the vertex of D.

The stationary equation is

    2tD = r(r+q)D'.                                      (9)

It can be made polynomial by squaring

    2tD-(t^2+p^2)D' = q sqrt(t^2+p^2) D',                (10)

but the unsquared sign condition must be retained. For algebraic parameters this is a quartic certificate plus a unique-root interval.

Use t=t_* in (6), and let H(s)=s^2+2B_t s+C_t. Put

    e=1/(2+F_*),   kappa=1-e,
    Q(s)=kappa(s-t)^2,   P(s)=H(s)-Q(s).                 (11)

At the stationary point, direct polynomial algebra gives

    H(-u)=(1+F_*)(u+t)^2,
    H(v) =(1+F_*)(v-t)^2.                                (12)

Thus (11) has exactly error e at all three required nodes, provided P is nonnegative everywhere. This global condition is essential; checking only the three node errors is insufficient.

For M positive definite,

    max_s (s-t)^2/H(s) = H(t)/det(M).

This follows from the Rayleigh quotient for the vector (1,-t), including the limiting value at infinity. For the maximizer (6), direct substitution gives

    det(M)/H(t)=p^2/(t^2+p^2).

Therefore P>=0 on the full real projective line if and only if

    t_*^2(1+F_*) <= p^2.                                (13)

**Sharpness lemma.** Whenever (13) holds, equality holds in (8), with an attained two-port solution. If (13) fails, (8) is strict. To see the last assertion, equality in the lower certificate would force Q(t_*)=0, both endpoint error constraints to be equalities, and H(t_*)=A(t_*). A nonnegative quadratic with that zero and the required leading coefficient is exactly (11), and the ellipse maximizer is unique. It violates P>=0. Compactness of the capped router class, or equivalently this compact quadratic parameter set after normalization, excludes unattained equality.

## 4. Proof of Theorem A for every T

For u=2,v=1, Section 3 gives -1/2<t_*<0. Also

    F_* <= F(0) = T^2/2.

Hence

    t_*^2(1+F_*) < (1+T^2/2)/4
                 < (T^2+2+T^(-2))/4 = p^2.

Thus (13) holds strictly for every T>=1. Equations (8) and (11) prove (2), with P strictly positive. This is a fixed asymmetric pattern across the entire delay range, not an angle-changing family chosen separately for each cap.

For the high-delay limit, t remains in the compact interval [-1/2,0]. Uniformly there, A(t)/T^2 tends to one. The maximum of D(t) is D(-1/2)=9/4. Thus F_*/T^2 tends to 4/9, proving (3). This also demonstrates why the geometric-mean prediction, whose limiting constant would be sqrt(2), is incorrect for this pattern.

## 5. Explicit lossless compilation

This construction spells out the classical completion rather than merely invoking existence. For Theorem A, P in (11) is strictly positive. Write

    P(s)=e s^2+2j s+k,
    j=B_t+kappa t,
    k=C_t-kappa t^2,
    eta=sqrt(k/e-(j/e)^2)>0.

Choose linear complex polynomials in the real variable s,

    q_R(s)=sqrt(kappa)(s-t),
    p_R(s)=sqrt(e)(s+j/e+i eta).

Their squared moduli sum to H(s). Convert to z-polynomials using

    s=i(z+1)/(z-1),
    q_z(z)=(z-1)q_R(i(z+1)/(z-1)),
    p_z(z)=(z-1)p_R(i(z+1)/(z-1)).

On the unit circle, |p_z|^2+|q_z|^2=4H(s)/(1+s^2)>0. Let h be its outer degree-at-most-one scalar spectral factor. If desired h is obtained explicitly from the constant and first Fourier coefficients of this positive trigonometric polynomial. With f^sharp(z)=z conjugate(f(1/conjugate(z))), define

    S(z)=1/h(z) [[p_z(z), -q_z^sharp(z)],
                 [q_z(z),  p_z^sharp(z)]].              (14)

Then S is analytic in the disk, unitary on the circle, and det(S)=h^sharp/h. There is no common zero of p_z and q_z: q_z has its zero at the real projective point s=t, while P(t)=H(t)>0. Therefore (14) has McMillan degree exactly one. The denominator ellipse is on its boundary, so the ratio of its extreme circle intensities is T^2 and its global Poisson delay peak is exactly T, including T=1 where the determinant zero is at zero. Embedding S as a block proves attainment for every N>=2.

For the general sharpness lemma, nonnegative P suffices for scalar factorization. The same argument gives degree one because p_z and q_z still have no common zero. Constants have error at least 1/sqrt(2), while every displayed nonconstant solution has strictly smaller error. For T<1 the Poisson peak lower bound excludes every nonconstant degree-one matrix, proving the stated constant branch.

## 6. A short independent proof of Theorem B

At T=1 every nonconstant degree-one denominator is constant. Thus w(phi)=|f_2(e^(i phi))|^2 is an affine function of x(phi)=(cos(phi),sin(phi)), is nonnegative, and is at most one. Constants also have this property. Set

    n=(cos(delta),sin(delta)),   l=cos(delta),   k=cos(gamma).

The repeated-node chord has n dot x=k and n dot x(0)=l>k. There are positive A_-,A_+ and B with

    x(0)=A_- x(-a)+A_+ x(b)-B(-n),
    A_-+A_+=1+B,    B=(l-k)/(1+k).

To verify positivity, resolve tangent components: A_+-A_-=-sin(delta)/sin(gamma). Positivity follows from gamma>|delta| and

    (1+l)/(1+k) > |sin(delta)|/sin(gamma).

Apply the affine identity to w. At squared error e, w(0)>=1-e, w(-a),w(b)<=e, and w(-n)>=0. Therefore

    1-e <= (1+B)e,

which is exactly (4), even in extra ports.

An attaining intensity is

    w(phi)=(1+cos(phi-delta))/(2+l+k).

It has the three required active errors and stays in [0,1], since l+k=2cos(a/2)cos(b/2)>0. Both w and 1-w are nonnegative degree-one trigonometric polynomials, and their scalar spectral factors give the degree-one matrix (14) with constant h. This independently proves the entire T=1 asymmetric formula.

## 7. Antecedents and limits

The inspected local predecessor is [Projective Memory and Resonant Bottlenecks in Passive Spectral Routing](https://arr-research.github.io/papers/ARR-2026-6M3VGTXZ6W8JW9C9/), v1, local `src/manuscript/main.tex`. Its resonant-border theorem, degree-preserving planar completion, and explicit limitations were read. It establishes attained positive error under finite caps but explicitly leaves numerical positive minimax values beyond degree zero unclaimed. The earlier related direct-sum routing record is [ARR-2026-52B6MSS1W197W9T2](https://arr-research.github.io/papers/ARR-2026-52B6MSS1W197W9T2/); it supplies an occupancy antecedent, not the finite-cap minimax calculation here. The prior local symmetric theorem and its replay were also read.

[Alpay–Jorgensen–Lewkowicz, arXiv:1410.0283v2](https://arxiv.org/html/1410.0283v2), Sections 2–3, supplies classical completion and Blaschke–Potapov context. Its reflected-disk stability convention must be converted. [Bolotnikov, arXiv:1609.09843](https://arxiv.org/pdf/1609.09843) treats scalar unimodular boundary interpolation with degree restrictions. These sources do not establish bibliographic novelty of the constrained minimax law. No exhaustive filter-design or constrained rational-approximation literature search has been performed.

The new local mathematical content is the original-coordinate denominator ellipse, the Lagrange lower certificate with its exact sharpness condition, the all-T asymmetric fixed-node law (2), and the all-gap T=1 formula (4). Positive quadratic factorization and lossless completion are imported classical ingredients. Sending three nodes to symmetric positions by a Möbius map is not itself a new theorem, and does not preserve a fixed global angular delay cap; the ellipse calculation is what retains that constraint here.

For an exact illustration, the real translation s -> s+1/2 sends the main pattern's cotangent nodes (-2,1) to (-3/2,3/2), fixing the exceptional point at infinity. Its disk automorphism has zero alpha=(1-4i)/17 and peak (9+sqrt(17))/8>1. Thus even the T=1 class is changed by that symmetrization. Reusing the symmetric formula at the unchanged numerical cap is invalid.

This manuscript does not classify the regime where (13) fails, degrees two and above, nonorthogonal targets, fixed output phase, loss, laboratory time delay, linewidth, Q factor, or energy. Additional repeated nodes are not automatically harmless: their errors must be checked against (11). The exact memory remains two and border memory one for a three-node binary table, an old consequence rather than a new claim. Symbolic replay is not formal proof verification.

Lluis Eriksson directed the research programme. OpenAI Codex assisted with proof development, symbolic and numerical computation, source comparison, internal review and drafting.
