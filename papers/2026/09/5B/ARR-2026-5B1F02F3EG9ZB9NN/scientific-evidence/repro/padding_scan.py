"""padding_scan.py -- exact kappa_d at the minimizing pairs for many paddings d = 2N+z (primal = dual)."""
import sys, os, time
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hive_exact import HiveLP
from gen_AB_costs import A_N, B_N, u3, z_N
t0 = time.time()
for N, (a, b, lab) in {6: (A_N(6), B_N(6), '(A_6,B)'), 7: (u3(7), z_N(7), '(u_3,z_7)'), 8: (u3(8), z_N(8), '(u_3,z_8)')}.items():
    vals = []
    for z in range(0, 13 if N == 6 else 9):
        d = 2 * N + z; M = HiveLP(d)
        lam = list(a) + [Q(0)] * z + [-x for x in reversed(b)]
        c = M.certify(lam)
        assert c['primal']['cost'] == c['dual']['value']
        vals.append((d, str(c['primal']['cost'])))
    print(f"N={N} {lab}: exact kappa_d for d=2N..: {vals}  [{time.time()-t0:.0f}s]", flush=True)
