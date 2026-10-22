import os, glob, hashlib, zipfile, shutil
src = r'C:\Trabajo\investigador-airr\ronda-12\gowerslong'
out = r'C:\Trabajo\investigador-airr\notas\gowerslong'
os.chdir(src)
readme = """Supplement: exact values F(6)=14 and F(7)=17 (Gowers-Long function), 21 Oct 2026.
Produced by Claude Sonnet 5.5 agents; no human review. See main.pdf, section 'What is not done'.

Python 3.12 with python-sat, ortools; Go for bnb.go and rup.go; Lean 4.35.0 for lean/Gowers.lean.
- common.py          lt2 and the direct sequence checker check_seq
- dfs.py             brute force n<=5 (dfs_out.txt)
- cp.py, cp_ls.py    CP-SAT (cp_out.jsonl, cp7.json = 17-witness; cp7_ge18.json = failed local search, UNKNOWN)
- sat.py             CaDiCaL with lazy cyclic-triple clauses (sat_out.jsonl; sat7_19.json is empty: timeout)
- cube.py, cube2.py, cube_skip.py   cube-and-conquer, n=7, m=18 (c7_18_*.jsonl: CaDiCaL and MapleChrono)
  validation: val_*.jsonl, val2_*.jsonl (n=5,6)
- bnb.go, bnb_out.txt   independent branch and bound, no SAT, F(1..6)
- proofcubes.py      Glucose4 DRUP proofs: n6 and the n7 cubes (proof_*.jsonl = logs; proof files NOT included, ~2.7 GB;
                     proofs_sha256.txt lists their SHA-256; rerun proofcubes.py to regenerate)
                     proofs_small/ contains n6_m15 (cnf + drup) and c1_3_3_5 for testing the checkers
- rup.go             Go forward RUP checker; rupcheck2.py = Python checker (too slow for n6_m15)
- verifyall.py       runs rup.exe on the proofs; verify_?.jsonl = results (407 of 425 n7 proofs verified; n6_m15 also verified)
- proof_summary.json counts
- falsos/            false proofs for c1_3_3_5 (all rejected); proofs_small/c1_3_3_5.cnf is the CNF
- bogus/             output of the buggy first run of the (1,1,2) subcubes (cubes with two fixed elements were
                     encoded contradictorily); also proof_n7_0.old / proof_n7_1/2.jsonl contain bogus c11_* entries of that run
                     (names starting c11_ with 0 lemmas); the valid ones are in proof_sub11_*.jsonl, proof_one11_122.jsonl
- lean/Gowers.lean   witnesses checked by native_decide and decide +kernel (lean Gowers.lean, exit 0)
- witness_n6.txt, witness_n7.txt
- ESTADO_AGENTE.txt, INFORME.md, pids.txt   work logs
Commands: python cube.py 7 18 cadical153 k 3 ; python proofcubes.py n6 ; go build rup.go ; rup file.cnf file.drup
"""
open('README_supp.txt', 'w').write(readme)
files = []
skip_dirs = {'proofs', 'paper', '__pycache__'}
for root, d, fs in os.walk('.'):
    d[:] = [x for x in d if x not in skip_dirs]
    for f in fs:
        p = os.path.join(root, f)
        if f.endswith('.exe') or f in ('nul',):
            continue
        files.append(p)
extra = {}
for n in ['n6_m15.cnf', 'n6_m15.drup', 'c1_3_3_5.cnf', 'c1_3_3_5.drup']:
    extra[os.path.join('proofs_small', n)] = os.path.join('proofs', n)
for f in glob.glob(os.path.join(out, 'witness_n*.txt')):
    pass
man = []
zp = os.path.join(out, 'supplement.zip')
if os.path.exists(zp):
    os.remove(zp)
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files):
        arc = os.path.normpath(p).replace('\\', '/')
        if arc == 'README_supp.txt':
            arc = 'README.txt'
        z.write(p, arc)
        man.append((hashlib.sha256(open(p, 'rb').read()).hexdigest(), arc))
    for arc, p in extra.items():
        z.write(p, arc.replace('\\', '/'))
        man.append((hashlib.sha256(open(p, 'rb').read()).hexdigest(), arc.replace('\\', '/')))
    z.writestr('MANIFEST.sha256', ''.join(f"{h} *{a}\n" for h, a in man))
print(len(man), os.path.getsize(zp))
