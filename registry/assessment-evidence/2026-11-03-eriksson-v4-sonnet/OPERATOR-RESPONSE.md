# Operator response to the first exact-v4 Sonnet assessment

3November2026. Exact reviewed PDF e5e9ddcf044ddcfab0e4cae8e2c6ac1a3dca39ff21bf23b20989aaff4b220e05,15pages. Same preparing Codex programme agent, acting under the author's instructions; not an independent referee, a new assessment, or an editorial acceptance. Author is also AIRR operator. Sonnet's2.00/10, major_revision, complete findings and three material objections are retained verbatim as rendered-text evidence. No second review or improved grade was requested.

## Frequency objection: two internal real coordinates are essential

The frozen PDF Section2 defines the real-linear isometry

    E_j(z)=(Re z)u+(Im z)v in component j,

where u,v are TWO distinct orthonormal internal vectors, not a single scalar coefficient. Section9, printedpage9, explicitly uses a in {1,i} and says that its quadratures are internal coordinates rather than supposedly independent scalar sine/cosine functions.

For 1<=s,t<=R<n, a,b in {1,i}, and i!=j, its fields are

    psi_(s,a)(x)=n^(-d/2) E_j(a exp(2pi*i*s*x_i/n)).

Their actual real counting inner product is

    <psi_(s,a),psi_(t,b)>
      = Re(conjugate(a)*b*n^(-d)*sum_x exp(2pi*i*(t-s)*x_i/n))
      = delta_(s,t)*Re(conjugate(a)*b)
      = delta_(s,t)*delta_(a,b).

The character sum concerns t-s, not t+s. Since s,t are distinct representatives strictly between0andn, the family is orthonormal even if t=n-s. For even n at s=n/2, the exponential is real, but multiplying by1and i maps it into u and v respectively, so the two real fields are still orthogonal and nonzero. Their divergence is zero because component j is independent of x_j.

Therefore the particular request to impose2R<n does NOT follow for the actual internal-coordinate construction printed in this PDF. Scalar sine/cosine aliasing would obstruct a different, one-internal-direction construction. This response only addresses the cited frequency/orthonormality objection; it is an analytic calculation, not a new Lean run or a full proof-dependency audit. The original quantified inequality and fixed-R argument remain subject to their other stated hypotheses.

## Quoted source-pin allegation: not located

The report names a purported malformed pin beginning1217ca39. That quoted substring was not found in either the frozen v4 TeX or its previously verified PDF text. The source-map anchors actually printed there can be inspected in the unchanged public files. This is an unconfirmed reviewer finding, not a demonstrated invalid pin. We do not infer from a failed textual match that every external source or formal dependency was independently checked.

## Remaining limitations and publication meaning

No new priority search, full independent Lean rebuild, interacting coefficient derivation, physical spectral gap or continuum construction was performed by this response. The report's limited source access, unknown participation/context, significance concerns and all other findings remain visible. A model assessment and this operator reply are neither human peer review nor AIRR admission. The manuscript bytes, earlier versions, preparing-agent sidecar and Sonnet score are unchanged. The preparing-agent7/10 used another disclosed rubric and is not pooled with the AIRR millennium-scale2.00.
