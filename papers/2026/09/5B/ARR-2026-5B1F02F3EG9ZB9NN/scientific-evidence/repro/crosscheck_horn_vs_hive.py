"""crosscheck_horn_vs_hive.py -- ties the hive-LP certificates to the explicit Horn program and to the
certified 22-form formula:
  (1) d=6: for every pair of W_3 the exact hive kappa (from certs/gamma_N3.json) must equal the exact 22-form max
      (from certs/kappa6_certificate.json) -- two independently certified exact objects;
  (2) d=6 and d=8: float Horn LP (522 / 8752 triples, HiGHS) vs exact hive kappa at every pair of W_3 / W_4 (tolerance 1e-9);
  (3) random rational spectra in d=6,7: exact hive kappa (primal = dual) vs float Horn LP.
"""
import sys, os, json, time
from fractions import Fraction as Q
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# (repro copy) check_horn_lp.py is copied next to this file; the original import path was ../../../scratch_A_inverse_commutator
from check_horn_lp import kappa_lp, horn_rows
from hive_exact import HiveLP

def gaps(lam): return [lam[i] - lam[i + 1] for i in range(len(lam) - 1)]

t0 = time.time()
K6 = json.load(open('certs/kappa6_certificate.json'))
forms = [[Q(x) for x in ch['q']] for ch in K6['chambers']]
def kappa6_formula(lam):
    g = gaps(lam); return max(sum(q[i] * g[i] for i in range(5)) for q in forms)
G3 = json.load(open('certs/gamma_N3.json'))
bad = 0
for P in G3['pairs']:
    a = [Q(x) for x in P['a']]; b = [Q(x) for x in P['b']]; lam = a + [-x for x in reversed(b)]
    if kappa6_formula(lam) != Q(P['kappa']): bad += 1
print(f"(1) d=6: 22-form max vs hive-certified kappa at {len(G3['pairs'])} pairs of W_3: {bad} mismatches")
rows6 = horn_rows(6); rows8 = horn_rows(8)
worst = 0
for P in G3['pairs']:
    a = [Q(x) for x in P['a']]; b = [Q(x) for x in P['b']]; lam = a + [-x for x in reversed(b)]
    worst = max(worst, abs(kappa_lp([float(x) for x in lam], rows6)[0] - float(Q(P['kappa']))))
print(f"(2) d=6: float Horn LP (522 rows) vs exact hive kappa on W_3: max |diff| = {worst:.1e}")
G4 = json.load(open('certs/gamma_N4.json')); worst = 0
for P in G4['pairs']:
    a = [Q(x) for x in P['a']]; b = [Q(x) for x in P['b']]; lam = a + [-x for x in reversed(b)]
    worst = max(worst, abs(kappa_lp([float(x) for x in lam], rows8)[0] - float(Q(P['kappa']))))
print(f"(2) d=8: float Horn LP (8752 rows) vs exact hive kappa on W_4 ({len(G4['pairs'])} pairs): max |diff| = {worst:.1e}")
rng = np.random.default_rng(11); rows7 = horn_rows(7)
for d, rows in ((6, rows6), (7, rows7)):
    M = HiveLP(d); worst = 0; nfail = 0
    for _ in range(40):
        v = [Q(int(x), 12) for x in rng.integers(-30, 31, size=d)]
        v = sorted(v, reverse=True); m = sum(v) / d; lam = [x - m for x in v]
        c = M.certify(lam)
        if c['primal'] is None or c['dual'] is None or c['primal']['cost'] != c['dual']['value']: nfail += 1; continue
        worst = max(worst, abs(kappa_lp([float(x) for x in lam], rows)[0] - float(c['primal']['cost'])))
        if d == 6 and kappa6_formula(lam) != c['primal']['cost']: nfail += 1
    print(f"(3) d={d}: 40 random rational spectra: exact hive kappa (primal=dual) vs float Horn LP max |diff| = {worst:.1e}; failures = {nfail}" + (" (also checked against the 22-form max exactly)" if d == 6 else ""))
print(f"[{time.time()-t0:.1f}s]")
