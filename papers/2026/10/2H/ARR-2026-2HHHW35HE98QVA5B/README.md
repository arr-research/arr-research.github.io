# Exact values F(6)=14 and F(7)=17 for a function of Gowers and Long

For triples a,b in Z^3 write a <_2 b if a_i < b_i in at least two coordinates. Let F(n) be the maximal length of a sequence of triples in {1,...,n}^3 with a^i <_2 a^j whenever i<j. Gowers and Long conjecture F(n) <= n^{3/2} for all n and tabulate F(n) for n<=5. Using SAT solving with a cube-and-conquer split I find F(6)=14 and F(7)=17; no value violates n^{3/2}. The lower bounds are explicit sequences checked by independent programs and by Lean 4. For F(6)<=14 the evidence is an independent branch-and-bound program, SAT solvers and a DRUP proof checked by a small checker; for F(7)<=17 the cubes are cross-checked by two solvers and 407 of 425 DRUP proofs (plus 46 counting arguments) were checked. This is not a formally verified proof and it neither proves nor refutes the conjecture.

Canonical PDF: paper.pdf, 4 pages, SHA256 452ec24cbada7e8b3ccc9d6c4198e8e89db74c2f3bb8b8c1eb1e9af0c3796d89.

Supplement scripts and stored results are supplied byte-for-byte; follow their README and run in a writable copy. Review evidence and its limits: review/README.txt.
