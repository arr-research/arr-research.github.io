# Exact values for a finite Ramsey-type problem from Green's list (Problem 22): N_0(1)=9, N_0(2)=54, N_0(3)=774

For r >= 1 let N_0(r) be the least N such that every r-colouring of {1,...,N} contains x,y >= 3 (not necessarily distinct) with x+y and xy in {1,...,N} and of the same colour. This is the quantity in Problem 22 of Green's list of open problems. Using SAT solving I find N_0(1)=9, N_0(2)=54 and N_0(3)=774. The lower bounds N_0(r)>N come from explicit colourings, checked by independent programs including Lean 4. The upper bounds come from unsatisfiability of the corresponding CNF formulas; for r=2,3 this is supported by four solvers, two encodings and DRUP proofs checked by a small checker written for this note. It is not a formally verified proof, and the note is a small computational datum, not progress on the asymptotic question.

Canonical PDF: paper.pdf, 4 pages, SHA256 72283c31d62c199483987dbcbc1619db2cbb9e04c545ab816015433dfc73853e.

Supplement scripts and stored results are supplied byte-for-byte; follow their README and run in a writable copy. Review evidence and its limits: review/README.txt.
