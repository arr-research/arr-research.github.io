Explicit cocycles for graph Hall algebras -- candidate 2, 4 November 2026.
Scope: finite labelled undirected multigraphs, loops allowed; coefficients F2.
Candidate 1 remains preserved. This extends its simple-graph scope; it is not
a separate paper. Exact source model: Toury arXiv2609.16849v1 section4 pp12-13.
New background: Contreras/Mehta/Stern arXiv2311.15342v2 examples3.9,5.11;
ordered partitions and their symmetries are prior art, not our novelty claim.

Python3.10+, no dependencies, from this directory:
  python verify.py
  python verify_extension.py
Do not use -O (assertions). Stored JSON outputs provide exact controls on 14
fixtures, 1742 positive-degree product comparisons. Inner additive checks flag
ring_isomorphism_checked=false describes additive subroutine only. The outer
record lists actual cup/Hall comparisons modulo coboundaries. Self-pairings
are checked; full off-diagonal Kronecker pairing is justified in the proof.

Run pdflatex twice on manuscript.tex. Final 5-page PDF visually reviewed;
no overfull or undefined references in final log. SHA256SUMS identifies the
frozen version. No Git commit SHA is asserted for this artifact snapshot.

Proof and code are from the same Codex assistant context. No independent
review, formal proof verification, worldwide priority determination, stars,
editorial acceptance or public release is asserted. Author is Lluis Eriksson,
also founder/operator/editor of AIRR; this conflict is disclosed in the PDF.
No scores from any other version apply. Private receipt, if any, is stored
separately under the cycle data checkpoint, not inside this immutable package.
