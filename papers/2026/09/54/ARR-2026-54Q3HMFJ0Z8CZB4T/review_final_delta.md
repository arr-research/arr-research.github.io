# Final internal audit: balanced inertia (4,4), contact theorem, and canonical PDF

**Status: PASS after one resolved reproduction correction. No unresolved material objection was found.** This is a separate internal agent review within the producing model family. For ARR provenance it is involved_in_manuscript, not independent human refereeing or statistical independence. It is not a numerical ARR assessment and assigns no Millennium score or stars.

Record: ARR-2026-54Q3HMFJ0Z8CZB4T, intended public v1.

- Final manuscript paper.md: SHA-256 **6262600d0d33eff5045bdc97ae3ce016f9818535e11106a3b1b5adac1cfabcf6**.
- Canonical commutator.pdf: SHA-256 **c4e21f587ecaafe4aa01e7b638e3f23b90263bfe77970a924b48625afbc52901**, 8 pages, 1,845,547 bytes.
- Previously reviewed source: SHA-256 26869d8b74fc4ce32ae1ba93620235792bdfc095474f68960066e17423f2b26e.

The complete final source was read and compared with the previously reviewed manuscript. All eight PDF pages, including mathematical content and references, were inspected. The review covers Theorems A–C, Lemmas 1–3, their dependencies, normalization, all-dimensional qualifications, reproduction instructions, and the source/PDF correspondence. Earlier independent geometry/Littlewood–Richardson evidence is retained with its original scope; the new contact certificates were checked afresh.

## 1. Theorem A and the underlying spectral geometry

The common-spectrum reduction is correct. Positive semidefinite isospectral R,S with difference F correspond to a realizing factor C; the objective is their common trace. In the ordered trace-zero chamber, the finite Horn polyhedron gives a polyhedral epigraph and a finite maximum of affine lower bounds. This establishes convexity and boundary continuity on that chamber. It does not assert matrix convexity or general invariance under appending zeros.

Lemma 1's alpha/beta coordinates satisfy two independent equalities on the nonzero base. A point with p positive alpha and q positive beta coordinates lies in a face of dimension p+q−2. The nonnegative support constraints and relative interior condition justify this count; the cases r=1 and r=N−1 cause no degeneracy. Vertices therefore have one positive coordinate of each kind. The stated vectors, base edges sharing an index, and apex edges follow. Their union has the claimed V and L.

Lemma 2 includes every new vertex of a hyperplane-cut product polytope: the intersection must lie on an original edge, and a product edge varies in only one factor. Edges contained in the cutting hyperplane create no further vertices. The explicit list is rational and the O(N^5) bound counts candidate pairs/Horn LPs, not total bit complexity or the size of the Horn system.

For Theorem A, D is affine on each cut cell and the cost is convex. Vertex inequalities extend by convexity. The only zero-distance pairs are the two opposite endpoint pairs, whose costs are exactly H. Mixing a positive-distance minimizing vertex with the uniform pair enters the exact inertia stratum and preserves its limiting positive denominator. The coefficient is therefore exact on that stratum. Positivity uses the positive general balanced estimate in Theorem 3 of the consolidated predecessor; rationality uses exact LP values, not floating-point proposals.

## 2. Theorem B and the corrected normalization

The 89 feasible spectra establish the forward bound by the cell argument. Zero-padding a realizing factor extends these upper cost bounds to every fixed d≥8. The all-dimensional lower obstruction at A,B is separate, so the proof does not assume that every cost is unchanged by padding.

Lemma 3 now unambiguously uses actual eigenvalues in its displayed inequality. For normalized sign lists, its equivalent statement is kappa(F)/P≥3b2−a2+a4. This is the correct homogeneity. The rank-two Horn family for −F yields s1+s3−s2−sd≥b2−a2; Loewner order yields s2≥b2 and s4≥a4. Adding them gives the claimed trace lower bound without setting sd to zero. The eigenvalue hypotheses themselves imply d≥6, within the stated d≥4 admissibility range.

At A=(5/8,1/8,1/8,1/8), B=(1/2,1/2,0,0), the lower bound is 3/2 and the rational witness has this trace. The exact-stratum perturbation has distance 7/4−4η and the displayed lower/upper cost sandwich. Thus the forward coefficient 4/7 is optimal for every fixed d≥8. The reverse coefficient 3/2 and its sharp family are correctly attributed to the predecessor, not asserted as a new theorem.

## 3. Theorem C: analytic check of the complete contact set

The proof uses the correct sign of curvature. On a cut cell,

\[
g_8=\frac52-\kappa_8-\frac47D_*
\]

is concave because kappa is convex and D is affine. The constant 5/2 remains fixed on the compact closure even where the actual inertia drops. Theorem B's vertex proof has already established g≥0 on that closure.

The new feasible spectra give positive lower bounds for the true gap at **85 of 89 vertices**, with minimum positive witness slack **1/7**. Four witness slacks vanish. A zero witness slack alone would not prove zero true gap; here the manuscript separately establishes the exact four costs using the one-spike formula and Lemma 3. This distinction is handled correctly.

If a zero-gap point is a convex combination of a cell's vertices, concavity bounds its gap below by the weighted sum of their nonnegative gaps. Every positively weighted vertex must consequently have zero true gap. Thus the point is in the convex hull of contact vertices of that same cell. The proof does not require global concavity across different distance cells.

The cell incidence is exact: e and A belong only to Q1; B only to Q2; u to Q1,Q2,Q3. Their q values are −3/2,0,0,3/2 respectively. Including both distance orientations produces 18 cut cells: **10 have no contact vertex, 6 have one, and 2 have two**. The only nonsingleton hulls are the segment joining (e,u) to (A,B) and its factor exchange. In particular, the two opposite one-spike contacts cannot lie together in the same oriented cut cell.

At the first segment's midpoint, the proposed spectrum is ordered, nonnegative, Horn feasible, and has trace 25/16. The distance is 7/8, so g8≥7/16. Each half-segment lies in the same cut cell. Concavity from the midpoint to its respective zero endpoint gives

\[
g_8(t)\geq\frac78\min\{t,1-t\}>0,\qquad0<t<1.
\]

This excludes every other point of both candidate hulls. No numerical LP optimality assertion at the midpoint is needed.

For d≥8, padding gives kappa_d≤kappa_8, hence g_d≥g_8. Therefore no new contact can appear. The four existing contacts remain exact: the two one-spike costs are dimension independent and the A,B cost has Lemma 3's all-dimensional lower bound. Factor exchange corresponds to sign reversal and preserves both cost and distance. Thus precisely the four stated pairs remain. None has both final sign coordinates positive, proving strictness everywhere on the exact inertia-(4,4) stratum. This is compatible with optimality of 4/7 as a boundary infimum.

## 4. Executed evidence and reproduction correction

The following computations were executed in this final review:

- The author's verify_contacts.py: PASS, 787,680 exact Horn checks.
- review_final_delta_check.py: PASS, independently enumerating Horn triples by the prior reviewer's LR-tableau code and rebuilding geometry from explicit formulas. It imports neither the author's geometry module nor the recursive Horn generator, runs no LP, and checks the 89 new vertex witnesses plus midpoint: **787,680 exact inequalities**, simplex/order conditions, slacks, and all cell incidences.
- algorithm_certificate_replay.py: PASS on the stored 48 rational primal/dual certificates, covering 89 ordered vertices, 420,096 Horn inequalities and 152 dual terms. This supports the tabulated exact vertex costs; Theorem C only needs feasible upper witnesses and its analytic contact lower bounds.

The independent helper's hash equals the version already reviewed in cycle 3. Existing unchanged 89-vertex bound evidence and general geometry counts were inherited rather than repeatedly regenerated. No Lean build or formal proof replay was run.

One reproduction error was reported and corrected by the manuscript author: certified_constant.py uses **NumPy/SciPy**, not SymPy, to propose solutions. Its subsequent rational primal/dual checks determine acceptance. The final Section 8 now says this accurately; requirements.txt pins NumPy 2.5.1 and SciPy 1.18.0, matching the inspected runtime. The four standalone replays named in Section 8 use the standard library, including their local dependencies. The optional floating-point proposal generator was read but not rerun; it is not needed to replay stored certificates.

## 5. Canonical PDF correspondence

The canonical PDF was opened and all eight pages inspected. The independent Poppler rendering of its actual bytes matches every previously inspected page PNG pixel for pixel. The PDF has readable page numbering, formulas and proof transitions; no missing symbol, clipped formula, omitted paragraph, or material layout error was found.

All **35 display blocks** match the source and rendering ledger exactly after whitespace/tag separation. Tags 1–15 are present in order. After removing the image-rendered math, Markdown styling, page footers and layout whitespace according to the documented checker, all **13,677 extractable prose characters** agree exactly; there are no text differences. Mathematical glyphs and formulas were checked visually, not inferred from that text comparison.

The PDF embeds math as raster fragments. Consequently ordinary PDF text extraction omits formulas; paper.md must accompany it as the full machine-readable mathematical source, and an extracted paper.txt must not be described as a complete mathematical rendition. This is a documented format limitation, not a discrepancy between the inspected PDF and source. The correspondence evidence is in review_pdf_correspondence.py/json.

## 6. Dependencies, claims, and limitations

The inspected consolidated predecessor is ARR-2026-24M24KDPZK8HDBQ9 v1, canonical PDF hash 15b54435c01a4972af77db0277c7f99fc21afb43be3bbc56b1884b76bb53bf30. Its source Section 2, Theorem 3, Sections 5.3–5.4 and their relevant arguments were read in this review for the one-spike cost, positive balanced estimate, continuity and reverse sharpness. Other parts of that paper were not comprehensively re-audited here.

The prior review's targeted primary-source checks are inherited: Fulton, Theorem 1 and equations (8)–(10), for Horn indexing and sufficiency; Knutson–Tao for saturation machinery; Angel–Schechtman for the distinct general-commutator objective. Classical Horn sufficiency is imported, not proved by these finite computations. No new exhaustive literature search or bibliographic-priority finding was made.

The finished manuscript keeps these boundaries visible: no claim of general matrix convexity, general zero-padding invariance, total polynomial-time complexity, explicit coefficients for N≥5, a general interior cost formula, or a classification of all realizing matrices. Within the stated ordered spectral problem, the three theorems and their proof dependencies pass this internal audit.

This report pins the final source and PDF. Subsequent mathematical or PDF edits would require a documented additional review; this report must not be silently reassigned to different hashes. It is scientific internal screening evidence, not an ARR numerical-score response or independent editorial acceptance.
