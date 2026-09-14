"""kappa6_table.py -- prints the 22 forms of certs/kappa6_certificate.json (gap coordinates), the reversal
partner of each, the number of extreme rays of its chamber and the support size of its Horn dual, as the
Markdown table of Section 6; also checks that the list is closed under reversal and that the chamber data are
as stated (rank 5, 5 or 6 rays, 112 rays in total, 522 Horn triples).  Written for the manuscript."""
import os, json
from fractions import Fraction as Q
HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, 'certs', 'kappa6_certificate.json')))
assert C['d'] == 6 and C['n_forms'] == 22 and C['horn_triple_count'] == 522
forms = [tuple(Q(x) for x in ch['q']) for ch in C['chambers']]
idx = {q: i + 1 for i, q in enumerate(forms)}
tot = 0
print("| r | q_r (gap coordinates) | rev | rays | dual |")
print("|---|---|---|---|---|")
for i, ch in enumerate(C['chambers']):
    q = forms[i]; rq = tuple(reversed(q)); assert rq in idx
    assert ch['rank'] == 5 and len(ch['rays']) in (5, 6) and len(ch['witness_s']) == len(ch['rays'])
    tot += len(ch['rays'])
    print(f"| {i+1} | ({', '.join(str(x) for x in q)}) | {idx[rq]} | {len(ch['rays'])} | {len(ch['dual_y'])} |")
assert tot == 112
print(f"\ntotal rays {tot}; every form's reversal is in the list; all chambers rank 5.  OK")
