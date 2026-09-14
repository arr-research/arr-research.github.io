"""uz_kappa_scan.py -- exact kappa_{2N}(u_3, -z_N^rev) for N = 6..16 (hive primal = dual), compared with the two closed
forms suggested by the certified values: P1(N) = (15N^2-28N-60)/(9N(N-2)) (value of the N=7,8,9 template pattern) and
P2(N) = (16N^2-31N-114)/(9N(N-2)) (quadratic through N=9..12).  Also gamma-candidate 9N(H_N-kappa)/(4(7N-12))."""
import sys, os, time
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hive_exact import HiveLP
from gen_AB_costs import u3, z_N
t0 = time.time()
for N in range(6, 17):
    d = 2 * N; M = HiveLP(d); a, b = u3(N), z_N(N)
    lam = list(a) + [-x for x in reversed(b)]
    c = M.certify(lam); assert c['primal']['cost'] == c['dual']['value']
    k = c['primal']['cost']
    P1 = Q(15 * N * N - 28 * N - 60, 9 * N * (N - 2)); P2 = Q(16 * N * N - 31 * N - 114, 9 * N * (N - 2))
    H = Q(N + 1, 2); Dst = Q(4 * (7 * N - 12), 9 * N); g = (H - k) / Dst
    print(f"N={N:2d} kappa_{{{d}}}(u_3,z_N) = {str(k):>10}  P1={str(P1):>10} {'=' if P1==k else '!='}  P2={str(P2):>10} {'=' if P2==k else '!='}   (H-kappa)/D_* = {g} = {float(g):.6f}  [{time.time()-t0:.1f}s]", flush=True)
