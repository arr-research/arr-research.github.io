# B3: clarification accompanying the assessed candidate

This author-side clarification accompanies, and does not replace or alter, the 14-page PDF with SHA-256 `810df760794f04ec3d423f157d6c6e4a30f9651545d636994fc5ce35eebdb654`. It was prepared with Codex assistance after the two preserved local assessments. Neither this note nor a model recommendation is an editorial acceptance. The original minor-revision recommendation remains preserved; disposition is pending.

## Closely related Watson-ratio results

Add the following reference to the related-work discussion:

Suvrit Sra and Dmitrii Karp, *The multivariate Watson distribution: Maximum-likelihood estimation and other aspects*, Journal of Multivariate Analysis 114 (2013), 256–269. DOI: [10.1016/j.jmva.2012.08.010](https://doi.org/10.1016/j.jmva.2012.08.010). [Author-hosted article](https://optml.mit.edu/papers/2013_sra_karp_jmva.pdf).

Their equation (3.5) gives the logarithmic-derivative Riccati equation, Theorem 3.1 gives monotonicity of the general Kummer ratio, and Theorem 3.2 supplies inverse-ratio bounds for all c > a > 0. These are prior results, not novelty claims of B3. B3's proposed contribution concerns the global positive-zero count of the centered quantity H = K' − κK'' and its scalar radial consequences. This citation clarifies that comparison; it does not assert an exhaustive priority search. A further 2024 bounds article located by the reviewer could not be fully inspected, and that limitation remains in the review.

## Domain in the proof of Theorem 4.1

In Step 3, the interval written `[m_f, infinity)` is `[m_f, 1)`. Throughout that argument, m is the tilted mean of a variable supported in (0,1), and the inverse trajectory has domain (μ,1).

## The optional tangency remark

The theorem's stated weak lower bounds remain valid. Its remark allowing a possible zero at m_f = 1/2 can be sharpened as follows. In the notation of the proof,

\[
\Psi(m)=\frac{(c+1)(m-\mu)}{m(1-m)},\qquad
G(m,\kappa)=\frac{\kappa}{c\mu-cm+\kappa m(1-m)},\qquad
D(m)=\Psi(m)-\kappa(m).
\]

At a hypothetical zero D(1/2) = 0, the transversality identity gives D'(1/2) = Δ(1/2) = 0. Since κ' = G(m,κ), differentiating D' = Ψ' − G(m,κ(m)) at that point gives D'' = Δ': the difference between the two derivatives is G_κ D', which vanishes there. Thus

\[
D''(1/2)=16(c+1)(1-2\mu)>0 \quad (c>2a).
\]

Taylor's formula would make D positive immediately to the left of 1/2, contradicting Step 1. Therefore m_f > 1/2 and the associated lower bound for κ_f can also be strict. This is a strengthening of the weak inequalities printed in the assessed PDF, not a change needed to make them true.

## The endpoint λ = 0

The stationary-radius and ordinary subdifferential statements in Section 6 are for λ > 0, as stated in its standing facts. At λ = 0, G_0(b) = 0 for every b in [0,1], so all radii maximize; the positive-λ uniqueness assertion is not extended to that endpoint. Also, c-tilde is identically zero for sufficiently small nonnegative λ and has right derivative zero at zero. For 0 < D < R² the objective in (6.1) has positive right derivative R² − D at zero, so its maximizing λ is positive. For D = R² the supremum is zero and is attained at λ = 0 as well as along the zero-gain interval. These endpoint conventions leave the displayed envelope unchanged.

## Verification and scope

The tangency identity was checked exactly in the preserved Astra candidate review's `independent.py` and is re-derived above. The reference was inspected directly in its author-hosted primary article. No manuscript bytes, reproduction results or model scores were changed. This note is intended to accompany the exact PDF and its reports if the genuine intake and separate editorial/publication gates are completed.
