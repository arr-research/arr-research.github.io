# Canonical and unrestricted observations in a finite checkerboard gradient model

Linked Working-paper v2; no acceptance or independent peer review. First exact-PDF involved AI importance5.00/10, overall5/10, major_revision, two material objections OPEN. Read the complete Model assessments and review context and the original protocol/serialization clarification. The14-page canonical PDF remains authoritative.

Canonical and unrestricted observations in a finite checkerboard
                        gradient model
                                           Lluis Eriksson
                                  THE ERIKSSON PROGRAMME

                                         11 November 2026


                                               Abstract
         We compare two classes of linear observations for a finite, source-weighted, two-channel
     checkerboard gradient form. For orthogonal alternating weak lines in dimensions three and
     four, the minimum restoring unrestricted rank is exactly Dn on all fields and (D − 1)(n − 2)
     on the actual coexact domain. For any fixed positive angle, an explicit transverse Fourier
     cutoff gives an unrestricted observation count of order n and a quadratic penalty inde-
     pendent of n, with constants depending on the angle and dimension. A real coexact
     counterexample shows that the mean-only orthogonal construction does not extend un-
     changed to small positive angles. In contrast, canonical original-channel rectangle means
     have a necessary ambient count of order nD−2 . This last argument does not apply to the
     coexact domain, because rectangular averaging need not preserve it. A further explicit coex-
     act witness excludes partitions whose every cell in either channel leaves a coordinate uncut.
     For an enlarged three-dimensional cyclic product-slice class, an explicit tagged-window
     cutoff proves a necessary inequality involving corner matching over every number of slices.
     Its restriction to nonwrapping canonical product slices gives a logarithmic count loss for
     fixed or bounded-motion cuts. A rapid helical grid in the cyclic extension fails through a
     short resonance; its wrapped complements are outside the nonwrapping canonical class. A
     separate construction with added chart-boundary cutoff centres excludes its nonwrapping
     refinement with 36n − 24 full rows. The general canonical coexact three-dimensional
     question, linear count versus a possible logarithmic loss, remains open. These are finite
     analytical results; we establish neither historical priority, formal verification nor a physical
     Yang–Mills spectral gap.


1    Problem and scope
Spectral coarse spaces that retain modes responsible for slow convergence are established
constructions; see Spillane et al. [1, 2]. The calculations here concern a particular finite
coefficient family and a restoring quadratic inequality. They do not prove a preconditioned
condition number bound or a new general principle of spectral enrichment. Our purpose is
to keep the coefficients, observed rows and domain explicit enough to compare their different
rank and count requirements.
    The manuscript consolidates the programme’s analytical sources 251–254, 256–259 and261C,
rather than presenting their corollaries as separate papers. A preceding working paper treats
broader canonical constructions [3]. The present manuscript is a proposed substantial revision
of the existing checkerboard working paper [4]. Its new PDF is ungraded at this source stage;
earlier assessments apply only to their original bytes.
    Fix an integer D ≥ 3, an even integer n ≥ 2, and c > 0. Write
                                                               c
                       X = (Z/nZ)D ,       V = nD ,     a=        ,    H = cn2 .
                                                              16D


                                                    1
We identify the original chart with {0, . . . , n − 1}D and retain all positive periodic labels
∂i f (x) = f (x + ei ) − f (x), including at n = 2. The source parity is p(x) = i xi (mod 2). For
                                                                               P

each parity l = 0, 1, let vl , sl ∈ R2 be an orthonormal pair. The two weak lines Rv0 , Rv1 have
principal angle θ ∈ (0, π/2]. Put
                                                       T
                                        B(x) = avp(x) vp(x) + Hsp(x) sTp(x) .

An original field is z = (z1 , . . . , zD ), with zr (x) ∈ R2 . All inner products and norms use
counting measure, summing sites, spatial components and internal channels. Define
                             X                                                      X
                   Q(z) =            (∂i zr (x))T B(x)∂i zr (x),          E(z) =            |∂i zr (x)|2 .      (1)
                             x,i,r                                                  x,i,r

The weights in (1) belong to the source x.
    For a real spatial one-form u, use the forward curl (d1 u)ij = ∂i uj − ∂j ui , with independent
indices i < j. Its adjoint is taken for counting measure on those independent components. Set
U0 = im(d∗1 ) and let U = U02 mean one copy for each original internal channel. This is the
actual coexact domain, not a substitute divergence-free space or an abstract low-energy band.
    For a domain A, a linear map C : A → F restores target c if

                               V −1 Q(z) + K∥Cz∥2 ≥ cV −1 ∥z∥2                   (z ∈ A)                        (2)

for some finite K ≥ 0. The lower bounds below also apply to any finite penalty Φ(Cz) with
Φ(0) = 0. The rank on U is always the actual restricted rank rank(C|U ).
    A canonical map uses a nonempty integer rectangle partition Pα of the original chart for
each original channel α = 1, 2, shared by all spatial components. Its rows and full count are

                (Cz)α,r,S = V −1/2 |S|−1/2
                                                      X
                                                            zr,α (x),     Nout = D(|P1 | + |P2 |).              (3)
                                                      x∈S

The rectangles are products of nonwrapping chart intervals. On the ambient space these
disjoint, nonzero rows are orthogonal and have rank Nout . On U , that equality is not presumed.
Unrestricted maps may instead use arbitrary real linear rows, including internal-channel
mixtures and nonlocal Fourier coefficients.


2    Actual strong components and their spectrum
Let S be the 2 × 2 matrix with rows sT0 , sT1 and put

                           Yl,r = sl · zr ,           δ = 1 − |s0 · s1 | = 1 − cos θ > 0.                       (4)

The row Gram matrix has eigenvalues 1 ± |s0 · s1 |. Thus S is invertible and ∥Sz∥2 ≥ δ∥z∥2 .
This is a proof coordinate; we will specify its resulting observations as actual original-field
rows. Dropping only nonnegative weak terms gives
                                                             X     X      X
            Q(z) ≥ HEstr (Y ),                Estr (Y ) =                      |Yl,r (x + ei ) − Yl,r (x)|2 .   (5)
                                                              l,r x:p(x)=l i

    For each residue s of parity l, define

                                Gl,s = {x :           i xi ∈ {s, s + 1}
                                                 P
                                                                           (mod n)}.

For each l these n/2 sets partition X. They include the wrap pair {n − 1, 0} where appropriate.
Put p = D − 1 and, for y ∈ (Z/nZ)p , set

        xs (y) = (y1 , . . . , yp , s −
                                          P
                                            i yi ),    u(y) = Yl,r (xs (y)),      t(y) = Yl,r (xs (y) + eD ).

                                                              2
These are bijections onto the actual source and destination layers. Since xs (y) + ei =
xs (y + ei ) + eD for i < D, the component energy is exactly
                             X                            X
                      Es =        |u(y) − t(y)|2 +               |u(y) − t(y + ei )|2 .          (6)
                             y                           y,i<D

Rungs and cross edges generate every source translation, and every target has a rung. The sets
Gl,s are therefore connected actual strong components. No labelled edge has been reassigned
or deduplicated.
    At a counting-orthonormal Fourier frequency k ∈ (Z/nZ)p , put Tk = 1 + pi=1 e2πiki /n .
                                                                                 P

The Hermitian symbol of (6) has diagonal D and off-diagonal entries −Tk and its conjugate.
Its eigenvalues are D − |Tk | and D + |Tk |. Expansion gives
                                   X
                 D2 − |Tk |2 =             |eiϑi − eiϑj |2 ,      ϑ0 = 0,        ϑi = 2πki /n.   (7)
                                 0≤i<j≤p

Consequently
                                                      p
                                                1 X
                                 D − |Tk | ≥          |1 − e2πiki /n |2 .                        (8)
                                               2D i=1
At nonzero k, at least one squared term is at least 4 sin2 (π/n) ≥ 16/n2 . At zero frequency the
eigenvalues are 0, 2D; the zero vector branch is precisely the common constant on both layers.
The other branch is also at least 8/(Dn2 ) for D ≥ 3, n ≥ 2. Finite Parseval therefore proves
                                              8
                                 Es (f ) ≥       ∥f − meanGl,s f ∥2 .                            (9)
                                             Dn2
Conjugate Fourier frequencies pair in the real space; real Nyquist frequencies obey the same
real matrix inequality. All formulas include n = 2 with its original positive labels.


3    Exact unrestricted ranks at the orthogonal angle
Assume D = 3 or 4, and fix the original basis by v0 = e1 , v1 = e2 , so channel 1 is strong
on odd starts and channel 2 on even starts. Let Rstr average each original channel and
spatial component over its correct strong components. This is an ambient counting-orthogonal
projection. Define Cstr by the normalized complete component means as in (3), replacing
rectangles by the corresponding Gl,s . There are Dn full rows and

                                     ∥Cstr z∥2 = V −1 ∥Rstr z∥2 .

Theorem 3.1. For the orthogonal family in D = 3, 4, the minimum unrestricted restoring
ambient rank is exactly Dn. The minimum actual coexact restoring rank is exactly (D−1)(n−2),
including zero at n = 2. The same displayed map Cstr attains both ranks and restores target c
with K = c on its fixed normalized rows.
Proof. Sum (9) over all original components. By (5),
                                               8
                                    Q(z) ≥       c∥(I − Rstr )z∥2 .
                                               D
Since 8/D ≥ 2 > 1, orthogonality gives Q(z) + c∥Rstr z∥2 ≥ c∥z∥2 on all original fields. This
proves the claimed normalized upper without any assertion about preservation of U .
    We next derive that preservation and the restricted rank for this particular map. For one
internal channel, write its sum-layer averages as

                                   Ar (t) = n−(D−1)
                                                            X
                                                                       zr (x).
                                                          P
                                                               xi =t


                                                     3
A coexact field has zero componentwise mean and backward divergence zero, by summing
adjoint differences and using d1 d0 = 0. Averaging the divergence over layer t shows that
F (t) = r Ar (t) satisfies F (t − 1) − F (t) = 0. Its total sum is zero, so F = 0. On a strong pair
        P

{s, s + 1} the projected value is [Ar (s) + Ar (s + 1)]/2. Hence Rstr z depends only on t = xi ,
                                                                                              P

has zero mean, has spatial sum zero pointwise, and is constant on the appropriate strong pairs
in each channel.
    Conversely, any real mean-zero spatial vector function of t whose spatial sum is zero is
actually coexact. At a nonzero diagonal frequency (j, . . . , j) the forward multipliers are the
common value ξi = e2πij/n − 1. For its coefficient u, i ui = 0, and hence i ξi ui = 0. The
                                                           P                      P

independent two-form coefficients
                                                 ξi uk − ξk ui
                                         ψik =               2
                                                               ,   i < k,                      (10)
                                                      i |ξi |
                                                    P


have actual curl adjoint u, since expansion yields

                              (d∗1 d1 u)r = (               2
                                                     i |ξi | )ur − ξr
                                                  P                   P
                                                                       i ξi ui .

There is no zero frequency; conjugation and the real Nyquist mode make the inverse two-form
real. Thus membership in im(d∗1 ) has been proved.
    Let W0 be these functions, additionally constant on each channel’s strong pairs. With
m = n/2, the scalar pair-constant mean-zero space has dimension m − 1. Choose D − 1 such
functions per channel and set the last to minus their sum. It follows that

               Rstr (U ) = W0 ,      dimR W0 = 2(D − 1)(m − 1) = (D − 1)(n − 2).

Indeed the forward inclusion was derived above, W0 ⊂ U by (10), and Rstr is the identity on
W0 . The kernels of Cstr |U and Rstr |U agree, so its actual rank is this dimension. Its ambient
rank is Dn, because all full rows are disjoint.
    Finally the full strong kernel consists of constants on each connected component and has
dimension Dn. Every field w in it has Q(w) = aE(w) ≤ 4Da∥w∥2 = c∥w∥2 /4, by the isometry
of forward shifts. Its intersection with U is exactly W0 , by the two preceding directions. Any
restoring linear map, with any finite penalty vanishing at zero, must be injective on each
corresponding low-energy subspace. A nonzero kernel vector there contradicts the target.
These give both sharp lower ranks and complete the proof.

    For n ≥ 4 a set Gl,s projects onto the full chart in every coordinate, but has size 2nD−1 < nD .
It cannot be a product rectangle: all its factors would then be full. Thus the attaining rows
are not canonical rectangle rows. The n = 2 component is the whole torus and is the stated
harmless exception. This special projection preserves U by proof; no such property is implied
for other block-averaging maps.


4    An explicit upper at any fixed positive angle
The angle assumption in Theorem 3.1 can be removed for an order-n unrestricted upper by
retaining transverse modes. We do not extend its exact minima to arbitrary angles.

Theorem 4.1. For all D ≥ 3 and θ ∈ (0, π/2], put
                          s         
                                  D                                                2c
                     R=               ,         L = min(n, 2R + 1),           K=      .
                       
                                 4δ 
                                                                                   δ



                                                         4
There is an unrestricted real map with 2DnLD−1 displayed rows satisfying

                              V −1 Q(z) + K∥Cz∥2 ≥ 2cV −1 ∥z∥2                             (11)

on all ambient fields and hence on U . Both unrestricted minimum restoring ranks have order
n as even n → ∞ at fixed D, θ > 0.

Proof. On each actual two-layer normal-coordinate component from Section 2, let P retain
both layer coefficients at frequencies

                            AR = {k : |ki |n ≤ R for every i < D},

where |ki |n is cyclic distance to zero. There are exactly LD−1 such frequencies. Conjugate
pairs produce sine and cosine real coordinates, and each self-conjugate character is counted
once. The real dimension is therefore 2LD−1 per component. The direct sum over all l, s, r is
an orthogonal projection in the Y norm.
    Outside the cube, some cyclic coordinate distance is at least R + 1 and at most n/2. Thus
(8) and sin(πq/n) ≥ 2q/n give the lower eigenvalue bound γ = 8(R + 1)2 /(Dn2 ). The upper
branch is at least D ≥ γ, because a nonempty tail implies γ ≤ 2/D. By Parseval,

                                   Estr (Y ) ≥ γ∥(I − P )Y ∥2 .

If the cube is the whole frequency torus, P = I and the zero-tail statement is automatic; no
nonexistent exterior mode is invoked. This includes n = 2.
    Choose a real orthonormal character basis on each retained layer and extend by zero to the
other components; denote the resulting vectors by bj . They are explicit counting-orthonormal
vectors in Y coordinates. Define actual original-field rows by

                          (Cz)j = V −1/2 ⟨bj , Yl,r ⟩,          Yl,r = sl · zr .

There are 2LD−1 rows per component, n/2 components per parity, two parities and D spatial
components. Consequently Nout = 2DnLD−1 and ∥Cz∥2 = ∥P Sz∥2 /V exactly. Our cutoff
yields Hγ ≥ 2c/δ = K. Therefore

           Q(z) + V K∥Cz∥2 ≥ K∥(I − P )Sz∥2 + K∥P Sz∥2 = K∥Sz∥2 ≥ 2c∥z∥2 .

The same conclusion holds for a full cube using only the observed term. Orthogonality is used
in the Y norm, followed by the proved singular-value bound in (4). We have not assumed that
P or S −1 P S preserves U ; the ambient inequality is restricted only after its proof.
    For the lower ranks, let Fl consist of mean-zero functions on Zn constant on the strong
pairs {l + 2j, l + 2j + 1}. Its dimension is m − 1, m = n/2. Choose independently fl,r ∈ Fl for
r < D, put fl,D = − r<D fl,r , and define original fields
                       P

                                                            P      !
                                               −1       f0,r ( xi )
                                  zr (x) = S                  P     .
                                                        f1,r ( xi )

This is injective and has real dimension (D − 1)(n − 2). Every original channel has zero mean
and pointwise spatial sum zero; the explicit real preimage (10) proves membership in U . All
actual strong normal differences vanish. Thus Q = aE ≤ c∥z∥2 /4 on this whole subspace.
Every restoring map must inject it. Dropping the mean and spatial-sum conditions gives Dn
independent ambient parameters with the same energy bound, and hence the ambient lower
rank Dn. Since R, K are independent of n at fixed D, θ, these lower ranks and the constructed
upper count give order n. The coexact lower is zero at n = 2; no positive endpoint lower is
asserted.

                                                    5
    The count constant and penalty diverge as θ → 0. At θ = 0 the matrix S is singular, and
the theorem does not follow by taking a limit. Even at a fixed angle, K is a coefficient on these
fixed normalized rows; it is not the condition number of the full operator. The observations
are nonlocal and can mix the original internal channels. No canonical upper has been obtained
from this construction.


5    Why complete component means do not suffice at small
     angles
Proposition 5.1. Let v0 = (1, 0), v1 = (cos θ, sin θ) and 0 < θ ≤ 1/4 radians. For every
even n ≥ 2 and D ≥ 3, there is a nonzero real z ∈ U annihilated by all complete strong-
component means, in any constant original-channel or normal-coordinate direction, with
Q(z)/(c∥z∥2 ) < 17/24. Any finite penalty vanishing at zero therefore fails to restore target c
for the map consisting only of those means.

Proof. Put w = (cos(θ/2), sin(θ/2)) and let zD (x) = w cos(2πx1 /n), zr = 0 for r ̸= D. At its
supported original frequencies ±e1 , only the first forward multiplier is nonzero and only the
                                                  P
Dth spatial field component is nonzero. Thus i ξi ui = 0, and formula (10), now with these
actual multipliers, constructs its real coexact preimage. At n = 2 the coincident Nyquist mode
and preimage are real.
   On any sum layer s, parameterize x = (y, s − y). Its cosine sum is
                                                     P

                                             n−1
                                             X
                                       D−2
                                   n                 cos(2πy1 /n) = 0.
                                             y1 =0

Hence every Gl,s mean vanishes, in every constant internal direction and every spatial compo-
nent. Normalization and linear combinations of these means do not change this conclusion.
    The bisector satisfies |vl · w|2 = cos2 (θ/2) and |sl · w|2 = sin2 (θ/2) for both parities. Thus
its source quadratic coefficient is the same number β = a cos2 (θ/2) + cn2 sin2 (θ/2) at every
site. The periodic cosine is an exact positive-Laplacian eigenfunction, so

                        Q(z)
                             = 4 sin2 (π/n) a cos2 (θ/2) + cn2 sin2 (θ/2) .
                                                                        
                        ∥z∥2


This retains the forward labels also at n = 2. Using sin t ≤ t and sin2 (π/n) ≤ 1 gives

                           Q(z)     1     2 2   1   π2   17
                               2
                                 ≤    + π  θ  ≤   +    <    < 1.
                           c∥z∥    4D           12 16    24

The last strict bound uses π 2 < 10. Since every observation is zero, the target fails for every
admitted penalty. The strong energy is positive at positive angle; it was not incorrectly set to
zero.

    This proposition refutes the unchanged mean-only extension for a specific angle interval.
It neither locates a sharp critical angle nor excludes the enriched observations in Theorem 4.1,
which retain transverse modes missed by these means.


6    A canonical ambient count lower bound
Return to the orthogonal original basis v0 = e1 , v1 = e2 . Let R be the canonical counting-
orthogonal block projection, so ker C = ker R and ∥Cz∥2 = ∥Rz∥2 /V .


                                                       6
Theorem 6.1. If a canonical map restores target c on all ambient fields, with any finite
penalty Φ(Cz) satisfying Φ(0) = 0, then
                                      3DV                             3D
                       Nout ≥                               ≥                    nD−2 .        (12)
                                22D+4 (1 + 8Dn2 )               22D+4 (1 + 8D)
The statement concerns the ambient count and rank. It does not assert this lower bound on the
actual coexact domain alone.
Proof. First suppose n ≥ 4. Set m = n/2, k = ⌊m/2⌋ and φ = 2πk/n ∈ [π/3, π/2]. On
sum residues put h(2j) = h(2j + 1) = cos(2φj). Choose a unit spatial vector b and set
                P
zr,2 (x) = br h( i xi ), zr,1 = 0. Every even-source strong difference of channel 2 vanishes. Finite
character sums give                             X
                                  ∥z∥2 = 2nD−1     cos2 (2φj) ≥ V /2.
                                                    j
The cyclic labelled difference identity on the m pair values yields
                              Q(z) = 2aD sin2 φ∥z∥2 ≤ (c/8)∥z∥2 .
The period-two pair cycle retains both forward labels, so this includes n = 4.
   Write A = (1 + e−iφ )/2, B = (1 − e−iφ )/2. The paired complex carrier is f (t) =
Aeiφt + Bei(φ+π)t and h = Re f . Its two frequencies are well-defined on Zn . √ Each interval
character sum is at most 2/|1 − eiω | ≤ 2 for these frequencies, and |A| + |B| ≤ 2. Factoring
over every original rectangle S gives
                                                            2
                                     X      X
                                           h(       xi )        ≤ 22D+1 .
                                     x∈S        i

For w = z/∥z∥, put t = ∥Rw∥2 . With the shared spatial-component partition and nonempty
cells,
                                22D+2 X 1        22D+2 Nout
                           t≤                 ≤             .
                                  V S∈P |S|         DV
                                                    2

The actual field u = (I − R)w has Cu = 0 and ∥u∥2 = 1 − t. Ambient restoration requires
Q(u) ≥ c(1 − t). On all ambient fields, B ≤ HI and forward-shift isometry imply Q(y) ≤
4DH∥y∥2 . Positivity of the form then gives
                       Q(w − Rw) ≤ 2Q(w) + 2Q(Rw) ≤ c/4 + 8Dcn2 t.
Consequently t ≥ 3/[4(1 + 8Dn2 )]. Combining these bounds proves the first inequality in (12);
the second follows from 1 + 8Dn2 ≤ (1 + 8D)n2 .
    At n = 2, use no nonexistent oscillatory pair mode. Each channel partition has at
least one cell, so Nout ≥ 2D. The first right-hand side of (12), divided by 2D, equals
3/[2D+5 (1 + 32D)] < 1. This proves the endpoint directly.
    In D = 4 the second constant is 1/11264. The earlier ambient canonical construction
in programme source 247, included in the public source package of [3], has count at most
225 n2 . Together these give order n2 for the ambient canonical class. Theorem 3.1 gives the
same-profile ambient unrestricted minimum 4n. These are comparisons of row classes on the
same domain, not comparisons of unlike domains. The earlier upper is a cited proved input,
not a result rederived here.
    The indispensable domain boundary in the lower proof is u = (I − R)w. Even if b is chosen
with spatial sum zero so that w is coexact, a rectangular block projection need not preserve
U . Thus u has not been shown coexact, and applying a coexact target inequality to it would
be invalid. The argument supplies no canonical coexact n2 lower in D = 4. In D = 3 the
canonical coexact question of O(n) versus a logarithmic loss also remains open; Theorem 4.1
does not settle it.

                                                        7
7    A coexact falsifier for uncut rectangular cells
Proposition 7.1. In the orthogonal family, let n ≥ 4 be even. If every cell of the canonical
partition of either original internal channel has at least one full coordinate interval, that map
cannot restore target c on U with any finite penalty vanishing at zero. The full coordinate
direction may differ from cell to cell; the other channel may even observe all sites.

Proof. Choose the indicated channel α and its strong-source parity p1 = 1, p2 = 0. Set
m = n/2 ≥ 2 and
                                         2π (t − pα ) mod n
                                                          
                          Fα (t) = cos                         .
                                         m         2
It is constant on each correct strong pair, including the wrap pair, has zero sum and is nonzero.
Put zr,α (x) = br Fα ( i xi ) for b = (1, −1, 0, . . . , 0), and set the other channel to zero. The
                      P

mean is zero and the spatial sum is zero. Formula (10) constructs its actual real coexact
preimage. Its strong differences vanish, so Q(z) = aE(z) ≤ c∥z∥2 /4.
     For any cell in that channel, fix all coordinates except a complete one. As the complete
coordinate varies, the sum residue runs through every element of Zn once. Its Fα sum is zero;
summing the remaining cell coordinates preserves zero. Thus every spatial mean in that cell
vanishes. The same field works simultaneously for all cells, irrespective of which coordinate is
full. The other channel is identically zero. Therefore Cz = 0 and the nonzero coexact field
contradicts the target.

    A necessary condition is consequently that each original channel have at least one cell
proper in every coordinate. This is not sufficient, gives no asymptotic logarithmic count lower,
and does not exclude arbitrary O(n) partitions with all coordinates cut. At n = 2 the scalar
zero-mean one-pair space vanishes; the proposition deliberately excludes that case.


8    Temporal matching of product slice corners
We now restrict to D = 3, 4 | n, n ≥ 32, and the orthogonal internal basis. Thus a = c/48
and H = cn2 . This section concerns the actual coexact domain U = U02 and the original mean
normalization, but permits an enlarged observation class: cyclic intervals may wrap in the fixed
chart. We call this the cyclic extension. Section 1’s canonical class uses nonwrapping chart
intervals and is not redefined here. Every nonwrapping product-slice partition is a member of
this extension, so restricting the theorem to those partitions gives a canonical necessary bound.
The rapid example below belongs only to the cyclic extension. This supplies no unrestricted
lower bound for every canonical partition.
    At each longitudinal slice x1 = i, let {Ji,j }j and {Ki,k }k be nonempty cyclic interval
partitions of Zn whose product of factor counts is the same integer q for every i. The cells
of channel 1 are {i} × Ji,j × Ki,k . Their full spatial-row count is 3nq. The second channel
can use any permitted partition. Write Ei for the product of the terminal endpoints of the
two interval partitions, so that Ei has exactly q distinct transverse points. For K ≥ 1, let SK
be the maximum over cyclic i of the minimum bottleneck matching distance between Ei and
Ei+K , using the periodic transverse ℓ1 metric. These extrema exist over finite sets. We impose
no common labelling around the cycle.

Theorem 8.1. Put L = log((n/4 + 1)/3). If for some integer K ≥ 1,

                     L ≥ 218 qAK ,                                2
                                        AK = max{16K, 9K + 6SK + SK },                        (13)

there exists a real nonzero z ∈ U with every original mean zero and Q(z) < 7c∥z∥2 /16. In
particular, no finite quadratic penalty on those means can restore target c. Consequently

                                                8
recovery requires
               L < 218 q max{16K, 9K + 6SK + SK
                                              2
                                                }                    for every integer K ≥ 1.   (14)
The assertion permits K ≥ n and includes the longitudinal seam.
   We give the constructive proof, including the norm and original-source energy bounds. No
assumed capacity estimate, projection invariance or coexact gap is used as an input.

8.1    A finite transverse cutoff
Let Y = Z2n , R = n/4, and let ρp be periodic ℓ∞ distance from p ∈ Y . Set
                          fp (y) = min{1, max{0, L−1 log((ρp (y) + 1)/3)}}.
It is zero for ρp ≤ 2 and one for ρp ≥ R. We claim
                             X                         64                          4n2
                                      |∂h fp (y)|2 ≤      ,        ∥1 − fp ∥2Y ≤       .        (15)
                            y,h=2,3
                                                       L                           L2

For a nonconstant edge, the smaller radius is 2 ≤ r < R. There are 8r + 4 ≤ 32r forward-
labelled edges crossing that square boundary, disregarding direction. Since r + 1 ≤ R ≤ n/4,
no antipodal ambiguity enters this count. Each scalar increment is at most 1/((r + 1)L). Thus
the energy is at most
                            32 R−1
                               X      r       32 log(R + 1)    64
                             2            2
                                            ≤        2
                                                            ≤ ,
                            L r=2 (r + 1)           L          L
where R ≥ 8 gives log(R + 1) ≤ 2L. For the norm, group sites by (R + 1)/2j+1 < ρp + 1 ≤
(R + 1)/2j , j ≥ 0. Each group has at most 4(R + 1)2 /4j sites and deficit at most (j + 1) log 2/L.
The latter estimate holds also where clipping makes fp = 0. Since j≥0 (j + 1)2 /4j = 80/27 < 4
                                                                   P

and R + 1 ≤ n/2, the deficit norm is at most 16(R + 1)2 /L2 ≤ 4n2 /L2 . This proves (15).
Telescoping a shortest lattice path also gives
                                                                            q
                            ∥fp (· + u) − fp′ ∥Y ≤ (|u|1 + d(p, p′ )) 64/L.                     (16)
Here |u|1 can be any chosen integer representative length, and all seams are periodic.

8.2    Tagged windows and their translation cost
Fix K and write S = SK . At slice i take the tagged list Fi = {(j, p) : 0 ≤ j < K, p ∈ Ei+j }.
Repeated spatial points keep their tags, so its size is exactly Kq even if K ≥ n. Match Fi
to Fi+1 by keeping the designated (K − 1)q shared entries at the same spatial position and
matching the remaining q outgoing entries to Ei+K with distance at most S. Some replaced
entries can also be stationary; no claim about the total number of stationary matches is needed.
Define
                                      η(i, y) = min fp (y).
                                                        (j,p)∈Fi

It lies in [0, 1] and vanishes within radius 2 of Ei . Squared maximum is bounded by the sum
of squares, so (15) gives
                                      ∥1 − η∥2X ≤ 4KqV /L2 .                             (17)
For two equally indexed real lists, | min a − min b| ≤ max |a − b|. Using the designated matching
and (16),
                                                         64q
                    ∥η(i + 1, · + u) − η(i, ·)∥2Y ≤          {(K − 1)|u|21 + (|u|1 + S)2 }
                                                          L
                                                         64q
                                                       =     (K|u|21 + 2|u|1 S + S 2 ).         (18)
                                                          L

                                                          9
With no longitudinal shift, identity matching of all Kq entries instead gives 64Kq|u|21 /L.
Summing either bound over i adds a factor n. The window is only a cutoff recipe; the observed
cells remain the original q cells per slice.

8.3   Actual coexact membership and observation zeros
Put δh f (x) = f (x) − f (x − eh ). For a real periodic Ψ, take ϕ = δ2 δ3 Ψ and the actual two-form
potential ψ23 = ϕ, ψ12 = ψ13 = 0. Since ∂h∗ = −δh , direct adjunction yields
                                d∗1 ψ = (0, δ2 δ32 Ψ, −δ22 δ3 Ψ) = P Ψ.
Every component has zero full sum by telescoping. Summing the second component on a cell
telescopes to four corner values of δ3 Ψ; the third gives the negative four corner values of δ2 Ψ.
Predecessors of initial endpoints are terminal endpoints of the preceding interval. Hence all
relevant corners are in Ei , including wrap cells. A whole-cycle factor cancels identically.
    Use the period-four wave Ψ0 (x) = sin(π(x1 +x2 +x3 )/2), and set Ψ = ηΨ0 . At every corner,
η and its backward transverse neighbors vanish. Thus both required differences of Ψ vanish
there. Every channel 1 mean of P Ψ is exactly zero, with its original positive normalization.
Take channel 2 identically zero. This constructs an actual real z = (P Ψ, 0) ∈ U annihilating
all observed rows.

8.4   Nonzero norm and original energy
Direct period-four differences give
                        z0 = P Ψ0 = (0, w, −w),          w = (2, −2, −2, 2).
Thus |z0 (x)|2 = 8, ∥z0 ∥2 = 8V , and at every original odd source all ∂h z0 vanish, including
across seams because 4 | n. For a finite convolution T = r ar τ r , where τ r is translation by r,
                                                             P

subtraction gives                              X
                            T (ηΨ0 ) − ηT Ψ0 =     ar (τ r η − η)τ r Ψ0 .
                                                    r
Each nonzero component of P has coefficient absolute sum at most 8, longitudinal shift 0 and
transverse radius at most 3. Since |Ψ0 | ≤ 1, the no-longitudinal translation bound yields
                               ∥P (ηΨ0 ) − ηz0 ∥2 ≤ 73728nKq/L.                               (19)
Each component of ∂2 P or ∂3 P has coefficient absolute sum at most 16 and transverse radius at
most 4. Its squared translation factor is at most 16K. Each component of ∂1 P has coefficient
absolute sum at most 16, longitudinal shifts 0 or 1 and transverse radius at most 3. Its factors
                                      2
are bounded by 9K andp 9K + 6S + S respectively. Consequently each derivative commutator
has norm at most 16 64nqAK /L. Restricting to original odd sources where η∂h z0 = 0, and
summing the six squared component bounds,
                               X
                                       |∂h (P Ψ)(x)|2 ≤ 98304nqAK /L.                         (20)
                             x odd,h

These are the original strong sources; no weight has been shifted.
   By (17), (19) and n ≤ V ,
                                                                         
                         ∥P Ψ − z0 ∥2 ≤ 64Kq/L2 + 147456Kq/L V.

The threshold and AK ≥ 16K imply L ≥ 222√     Kq. The                             −38
                                                              √ above is at most 2 +9/256 <
                                                     √ coefficient
2. Reverse triangle therefore gives ∥P Ψ∥ > 8V − 2V = 2V . In particular the constructed
field, not just its potential, is nonzero. Multiplying (20) by H = cn2 gives
                      Qstrong (z) ≤ 98304cV qAK /L ≤ 3cV /8 < 3c∥z∥2 /16.

                                                  10
Every directional forward difference has norm at most 2∥z∥, so Qweak (z) ≤ 12a∥z∥2 = c∥z∥2 /4.
Adding proves Theorem 8.1. Any quadratic penalty vanishes on the identically zero observation
vector.

8.5   Count consequences and a rapidly moving grid
For fixed cuts, S1 = 0 and A1 = 16. With bounded one-step corner motion, A1 stays bounded
as well. In either class, (14) forces q to grow at least proportionally to L, and hence requires
order n log n full channel 1 rows. This conclusion is restricted to these product classes, including
their nonwrapping canonical subclasses. Arbitrary canonical rectangle partitions and rapidly
moving product partitions remain outside this count conclusion.
    In the cyclic extension, large adjacent motion does not itself guarantee recovery. For n = 2m ,
m ≥ 5, let κ = n/4 + 2 and ti = κi mod n. Use the singleton {ti } and its cyclic complement
for the first transverse factor, and {0} and its complement for the second. Use these partitions
in both original channels. There are 24n full rows and Ei = {ti , ti − 1} × {0, n − 1}, so q = 4.
The identity 4κ = n + 8 gives S4 ≤ 8 and A4 ≤ 148. For L ≥ 220 · 148, the theorem gives an
invisible real nonzero coexact field below target. Such dyadic sizes exist, but the threshold is
enormous and is not a practical crossover estimate.
    The adjacent bottleneck is exactly κ: the next corner with first transverse coordinate ti + κ
is at least that far from each old corner, since κ < n/2 − 1; translation realizes that maximum
distance. Also gcd(κ, n) = 2, so the orbit visits n/2 positions. This is a rapidly moving cyclic
family with a short resonance. For an interior singleton, its cyclic complement wraps and is
not one of the nonwrapping chart intervals in Section 1. Splitting a wrapped cell into chart
rectangles introduces separate means; invisibility of their sum does not imply invisibility of
each refined mean. Thus neither this 24n count nor its failure is transferred to that chart
refinement. The theorem does not assert that every rapidly moving O(n) family fails.

8.6   A separate counterexample for nonwrapping chart cells
The previous cyclic example does not imply failure of its chart refinement. We now construct a
new cutoff that annihilates every refined mean separately. This gives a counterexample inside
the original nonwrapping canonical class.

Proposition 8.2. Let n = 2m , m ≥ 5, κ = n/4 + 2 and ti = κi mod n. At slice i partition
the second-coordinate chart into the nonempty members of [0, ti − 1], {ti } and [ti + 1, n − 1],
and the third coordinate into {0} and [1, n − 1]. Use these nonwrapping product cells in both
original channels, with first coordinate {i}. Their exact full count is 36n − 24. If

                                         L ≥ 218 · 6 · 148,                                    (21)

there is a real nonzero z ∈ U with each of these original means zero and Q(z) < 7c∥z∥2 /16.
This particular canonical family therefore cannot restore target c with any finite quadratic
observation penalty.

Proof. Since gcd(κ, n) = 2, the orbit visits each even position twice. Thus ti = 0 occurs twice,
ti = n − 1 never occurs, and all other ti are interior. There are four cells per channel at the
two zero slices and six at each other slice. Counting all spatial rows in both channels gives
2 · 3{2 · 4 + (n − 2) · 6} = 36n − 24.
     For interior ti , the actual terminal second-coordinate endpoints are ti − 1, ti , n − 1; for
ti = 0 they are 0, n − 1. The third-coordinate endpoints are 0, n − 1. Let Gi be the six-entry
tagged list obtained from ti , ti − 1 mod n, n − 1, each paired with those two third-coordinate
endpoints. It covers every actual corner, including the extra chart boundary. At ti = 0 some


                                                11
positions coincide but retain their tags. Six is a covering-list count, not an assertion of six
cells at every slice.
    The identity 4κ = n + 8 gives a same-tag matching from Gi to Gi+4 : four entries translate
by (8, 0) and two are stationary. Form the 24-entry window Fi from Gi , Gi+1 , Gi+2 , Gi+3
and let η(i, y) be the minimum of the associated radial functions fp . The designated 18
shared entries remain stationary between consecutive windows; the six replaced entries have
displacement at most8. Directly using (15) and the minimum inequality gives

                                     ∥1 − η∥2X ≤ 4 · 4 · 6V /L2 ,
                                                   64 · 6
                   ∥η(i + 1, · + u) − η(i, ·)∥2Y ≤        {4|u|21 + 16|u|1 + 64}.
                                                     L
Without longitudinal shift the bound is 64 · 4 · 6|u|21 /L. These explicit estimates remain valid
with repeated centres. We have not applied the constant-cell-count theorem to this varying
four/six-cell map.
    Set Ψ = ηΨ0 and use the actual potential and field z = (P Ψ, 0) from the preceding proof.
At every actual refined corner, η and its backward transverse neighbours vanish. For each
individual chart interval, its initial-endpoint predecessor is a terminal endpoint of the preceding
interval, with −1 = n − 1 at the chart boundary. Every one of the four corners in the telescoped
cell sum is therefore covered by Gi . Both needed first differences of Ψ vanish there, so each
separately normalized refined mean is zero. No zero sum on a union is used to infer zero sums
on its pieces. The actual curl-adjoint formula proves real membership in U .
    For the convolution shifts used by P and its derivatives, the translation factors are bounded
by A = max{64, 36 + 48 + 64} = 148. The same coefficient sums, now applied to the explicit
six-centre estimates above, give

                        ∥P (ηΨ0 ) − ηz0 ∥2 ≤ 73728n · 4 · 6/L,
                       X
                               |∂h (P Ψ)(x)|2 ≤ 98304n · 6 · 148/L,
                     x odd,h

                                ∥P Ψ − z0 ∥2 ≤ (64 · 24/L2 + 147456 · 24/L)V.
                               22                                        −38 + 9/256 < 2,
            √ implies L ≥ 2 · 24. The last coefficient is at most 2
Threshold (21)
so ∥P Ψ∥ > 2V . The field itself is nonzero. Multiplying the strong estimate by the
original H = cn2 bounds strong energy by 3cV /8 < 3c∥z∥2 /16; weak energy is at most
12a∥z∥2 = c∥z∥2 /4. This proves the strict 7c/16 bound. All observation penalties vanish on
the zero mean vector.

   This is a newly constructed invisible field for this particular nonwrapping refinement. It
does not retroactively validate a split-cell inference for the old cyclic field. The threshold is
enormous and unoptimized, and no general impossibility of canonical O(n) partitions or global
canonical logarithmic lower bound follows.


9    Interpretation and remaining question
The sharp orthogonal ranks count the actual strong kernel and its explicitly derived coexact
image. Positive-angle enrichment pays a deteriorating singular-value comparison by retaining
finitely many transverse modes per component. The temporal matching theorem supplies an
actual invisible coexact field for the cyclic product-slice extension, including a rapidly moving
resonant example outside the nonwrapping canonical class. The separate chart-refinement
construction adds the previously missing boundary corners and gives a new counterexample
within that class. These restricted quantifiers do not settle the general canonical count optimum.


                                                  12
The small-angle counterexample explains why that enrichment cannot simply be replaced by
an assertion that the old means still suffice. The canonical ambient lower instead uses a real
oscillatory carrier and an actual ambient kernel projection. Its failure to transfer to U is an
explicit domain obstruction, not a technical detail that can be omitted.
     The remaining question is whether, for the orthogonal D = 3 family and actual U , canonical
original-channel integer rectangle partitions admit O(n) full count with some finite size-
dependent quadratic penalty, or whether the known logarithmic upper loss is unavoidable. The
mean supports and Fourier rows used in the unrestricted theorems are not permitted substitutes.
No theorem here establishes a size-uniform canonical penalty, efficient implementation or a
full-operator condition number. All results concern a finite toy gradient family. The continuum
and physical Yang–Mills mass gap remain open; the programme’s PR29 accounting remains
20/41, with TermSource=0.


10     Model assessments and review context
The analytical source texts 251–254, 256–259 and261C received complete involved AI source
readings. Their exact source bytes, full reports, objections and context must remain in the
reproducibility package. The temporal proof uses the designated shared-slot wording specified
in the retained 259 clarification. These readings are not human peer reviews, blind readings,
independent provider samples or Lean verification. The exposed source reviewer identity was
Codex, based on the OpenAI GPT-6 family; exact served backend, version and reasoning effort
were not exposed. Reviewers shared account, infrastructure and programme context and had
prior involvement.
    At this source stage the proposed revision has no exact-PDF numerical assessment, success-
ful production claim or visual-review claim. No grade is assigned or inherited. The existing
255B version 1 PDF has SHA256
           d45a17a4142204628189441b9133aa1027b0d7577a56dc5de6c576d2af6102e7

Its first exact-PDF assessment recorded importance 4.00/10, overall 4/10 stars, recommendation
major_revision and three material objections open. Those are historical facts about that
version, not predetermined grades or objection states for a successor. Its full original report
must be retained unchanged. A new version requires its genuine first assessment of the exact
new PDF; repeated samples to improve a grade are not evidence of scientific progress.
     Analytical correctness is separate from originality and relevance. Spectral enrichment is
established literature. The finite radial cutoff, minimum inequality and window-cover mecha-
nisms are elementary; historical priority of this particular application remains unestablished.
The huge sufficient threshold is not a demonstrated practical regime. Neither a deposit nor
Working-paper status constitutes editorial acceptance or human peer review.


Reproducibility and provenance
Scientific inputs are frozen programme sources 251–254, 256–259 and261C. The source archive
must retain their raw bytes, complete analytical reports and context, this manuscript’s mapping,
the frozen Git commit and all actual production logs. In particular the temporal theorem is
derived in source 259 at the frozen commit
     2f370a7da850b8066a9afe95c523e49bd1ef725e

Its full audit and clarification were integrated unchanged through merge
     8485cfb2b8b11bb5acd240d8a0b133457bbfe2a1


                                              13
The separate nonwrapping refinement construction is frozen at
      1a01fa019069e0f5a7392601ddb3c7a3febe222d

The separate golden-orbit working derivation 260 is excluded from this manuscript: no
unreviewed frontier result is promoted here.
    Linux compilation, extraction and page rendering are production checks; they do not
certify mathematics or transfer a model score. No such build or exact-PDF review is claimed
at this draft-source stage. Subsequent production and review facts belong to dated sidecars
linked to the exact PDF hash. The original published version remains immutable. The frozen
production source is fb3ba8d2c0ae52d4a2e909b0fb2df02b2f953bc4.


References
[1] N. Spillane, V. Dolean, P. Hauret, F. Nataf, C. Pechstein and R. Scheichl, A robust two-level
    domain decomposition preconditioner for systems of PDEs, C. R. Acad. Sci. Paris, Ser. I 349
    (2011), 1255–1259. doi:10.1016/j.crma.2011.10.021.
[2] N. Spillane, V. Dolean, P. Hauret, F. Nataf, C. Pechstein and R. Scheichl, Abstract robust coarse
    spaces for systems of PDEs via generalized eigenproblems in the overlaps, Numer. Math. 126 (2014),
    741–770. doi:10.1007/s00211-013-0576-y.
[3] L. Eriksson, Canonical rectangle observations for matrix gradients: fixed weak spaces and checker-
    board counterexamples, AIRR Working paper, ARR-2026-5XANPRA7E891Q9FZ, version 1 (2026).
    https://airr.science/papers/ARR-2026-5XANPRA7E891Q9FZ/versions/v1/.
[4] L. Eriksson, Canonical and unrestricted observations in a finite checkerboard gradient model,
    AIRR Working paper, ARR-2026-597T88D7WZ98HR0Z, version 1 (2026). https://airr.science/
    papers/ARR-2026-597T88D7WZ98HR0Z/versions/v1/.




                                                 14
