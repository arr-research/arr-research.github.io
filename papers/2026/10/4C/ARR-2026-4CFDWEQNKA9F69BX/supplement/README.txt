Supplement for "Exact values for a finite Ramsey-type problem from Green's list (Problem 22)".
Not a verified artefact: see main.pdf, section "What is not done".
Requirements: Python 3 with python-sat (pysat) and ortools; Lean 4.35.0 (core, no Mathlib).
Encoding: variable v(n,k)=(n-1)*r+k+1, k=0..r-1; the CNFs n0_r{r}_N{N}.cnf have no symmetry breaking.

Reproduce:
  python verify.py                  CP-SAT, witnesses, CNFs, hashes.json (writes in cwd; slow for r=3, N=774)
  python n0b.py d 3 773 774         SAT/UNSAT, strict variant x>y ("s" = x>=y, the problem's definition)
  python mkproof.py n0_r3_N774.cnf  regenerates a .drup (Glucose4; may differ from the file included)
  python rupcheck2.py n0_r3_N774.cnf n0_r3_N774.drup        expect VERIFIED ... 2132 lemmas
  python rupcheck2.py n0_r2_N54.cnf n0_r2_N54.drup          expect VERIFIED ... 1 lemmas
  python rupcheck2.py n0_r3_N774.cnf falsa_sin_lemas.drup   expect RUP FAIL
  python rupcheck2.py n0_r3_N773.cnf n0_r3_N774.drup        expect RUP FAIL at lemma 1397
  falsa_vacia.drup is the line "0", run against n0_r2_N53.cnf (RUP FAIL);
  falsa_lema.drup is a false proof starting with the lemma "1 0" (RUP FAIL);
  the remaining false proof (empty clause directly for N=774) is the same file as falsa_vacia.drup run against n0_r3_N774.cnf.
  lean Green22.lean                 about 2 min, exit 0

G3k.lean + g3k.out: decide +kernel for the 773-witness did NOT finish (25 min timeout, exit 124).
INFORME.md is the original working log (Spanish); n0.py, n0c.py are earlier scripts (n0c.py is an unfinished helper, not used for the results).
SHA256SUMS in this folder is the original list; MANIFEST.sha256 is the manifest of this zip.
Colour witnesses: witness_r2_N53.txt, witness_r3_N773.txt (digit n = colour of n).
