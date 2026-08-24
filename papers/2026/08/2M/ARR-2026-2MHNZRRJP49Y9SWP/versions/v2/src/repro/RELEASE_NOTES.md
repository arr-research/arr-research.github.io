# Scientific revision record

This candidate is a major scientific revision of
`ARR-2026-2MHNZRRJP49Y9SWP` rather than a new record. The theorem, notation,
and proof architecture remain those of the exact-floor paper; the base-field
scope of the principal result is enlarged and reaudited.

## Material changes relative to ARR v1

1. Extended the exact universal floor from characteristic zero to smooth
   varieties over an algebraically closed field of arbitrary characteristic.
2. Replaced the characteristic-zero derivative gap by a perfect-field lemma.
   For a minimal nonzero homogeneous form in a radical point ideal, either a
   first derivative lowers the degree or, in characteristic `p`, every
   derivative vanishes and the form is `G^p`; radicality then puts the
   lower-degree root `G` in the same ideal.
3. Kept the theorem restricted to algebraically closed fields. No statement is
   made over imperfect fields, nonreduced supports, singular varieties, or
   incomplete linear systems.
4. Reaudited the adapted projection in arbitrary characteristic: the center
   avoids the finite tangent and secant data; the map is finite; its tangent
   map is an isomorphism at every support; and the finite local map is etale
   there. Only the cotangent-space isomorphism is needed for transfer.
5. Corrected attribution after a primary-source check. Bocci--Chiantini,
   Remark 2.2, already gives the derivative/`p`-th-root dichotomy for planar
   point sets over an algebraically closed field of arbitrary characteristic;
   the manuscript identifies its use here as the dimension-independent form
   of that standard argument. It also cites Dao--De Stefani--Grifo--Huneke--
   Nunez-Betancourt for perfect-field differential powers and De Stefani--
   Grifo--Jeffries for mixed-characteristic context.
6. Kept the proper-span sharpness construction explicitly over the complex
   numbers; no positive-characteristic Bertini extremizer is asserted.
7. Added an exact modular replay. It exhausts all nonempty supports in
   `P^1(F_2)`, `P^1(F_3)`, and `P^2(F_2)` within stated degree cutoffs and
   separately records Frobenius-root fixtures.
8. Added a replay runner that regenerates all JSON results and requires
   byte-for-byte agreement with the committed evidence.
9. Tightened title, abstract, priority language, limitations, provenance, and
   replay scope. “In arbitrary characteristic” is used instead of a broader
   claim about arbitrary ground fields.
10. Responded to independent referee P2 comments by stating only the tangent-
    map property needed from projection, making the Bertini base-point-free
    locus explicit, treating smooth quadrics in characteristic two via the
    polar radical, defining `N` to include zero, and weakening “exact inputs”
    to “inputs used by this proof.”

## Publication gate

Independent adversarial review found no P0 and assigned 7.6/10 with uncertainty
+/-0.8 before the response above. Focused re-review, after one final residual
wording fix, assigns 8.4/10 +/-0.6 and regards the mathematics as publishable,
with priority uncertainty explicitly retained. Final three-pass compilation,
all-page rendering, deterministic packaging, ARR validation and CI remain
required. A local PDF or pull request is not a publication.
