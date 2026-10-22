Supplement to main.tex (Green 37 and 27), 22 Oct 2026. Produced by Claude Sonnet 5.5 agents under the direction of the author; no human review.
Python 3.12, python-sat (CaDiCaL 1.5.3, Glucose4, MapleChrono), ortools 9.15 (CP-SAT), Go (rup.exe from rup.go), Lean 4 core, tectonic.

g37/
  g37sat.py      SAT encoding on a window {0..W} (+ optional gap clauses valid by Lemma 1), independent check_witness
  g37int.py      CP-SAT model in Z (gaps <= N+1)  -- used by drive.py (k=3: g37_k3.jsonl, k=4: g37_k4.jsonl)
  g37int2.py, z18.py   variant with extra redundant constraints; z18.jsonl = N=18, s=13, diameter >= 37 experiment
  wtable.py      m over windows [0,2N] (k=3) and [0,3N] (k=4): wtable_k3.jsonl, wtable_k4.jsonl.
                 NOTE: the original k=3 file had a bug in the 3N column (s not reset); those fields were removed.
  ub37.py        upper-bound search in windows 3N,4N,6N with time limit: ub37.jsonl (status TIMEOUT = inconclusive)
  winD.py        N=18, s=13 gap-clause instances for several window sizes: winD.jsonl
  cert37.py, runcerts.sh   Glucose4 DRUP proofs + rup.exe check; cert37.jsonl has SHA-256 of every CNF/DRUP, sizes, lemma counts, checker verdicts
  rup.go, rup.exe   forward RUP checker (from the Gowers-Long supplement, deletions ignored)
  neg/           negative controls (cnf/proofs rejected by rup.exe)
  proofs/        CNF + DRUP files (large; those not shipped are listed with hashes in cert37.jsonl)
g27/
  g27.py         SAT, 0,1 in A by affine symmetry; g27_results.jsonl (witnesses, times); proofs/ ; verify27proofs.py -> proof_check.jsonl
  old/           first run with an older encoding (duplicate literal in a clause); superseded
verify_witnesses.py   naive independent checker of g37/witnesses37.json and g27/witnesses27.json
mkwit.py, gen_lean.py, lean/Green2737.lean   witnesses -> Lean (native_decide / decide +kernel)
make_tex.py, main.tpl.tex, main.tex   builds the paper from the data files
lit/           literature notes downloaded (README of mkwatson/unique-sums-notes; text of Green's list)
ESTADO_AGENTE.txt, pids.txt (+ g37/pids.txt, g27/pids.txt)   work log and PIDs started by this agent
