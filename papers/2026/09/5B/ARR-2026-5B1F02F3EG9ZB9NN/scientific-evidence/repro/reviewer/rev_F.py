"""rev_F.py -- (F) spot checks with MY float hive LP: kappa at (u3,z_N), (A_N,B), padding; D_* by the record's definition."""
import sys, time
from fractions import Fraction as Q
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # (repro copy: was the reviewer's scratchpad path)
from rev_lib import *
def A_N(N): return [Q(3 * N - 2, 4 * N)] + [Q(N + 2, 4 * N * (N - 1))] * (N - 1)
def B_N(N): return [Q(1, 2), Q(1, 2)] + [Q(0)] * (N - 2)
def u3(N): return [Q(1, 3)] * 3 + [Q(0)] * (N - 3)
def z_N(N): return [Q(4 * N - 3, 9 * N)] * 2 + [Q(N + 6, 9 * N * (N - 2))] * (N - 2)
t0 = time.time()
claimed = {7: Q(479, 315), 9: Q(43, 27), 10: Q(49, 30), 8: Q(169, 108), 6: Q(13, 9)}
gam = {7: Q(781, 740), 9: Q(23, 17), 10: Q(3, 2), 8: Q(317, 264)}
for N in (6, 7, 8, 9, 10):
    a, b = u3(N), z_N(N); d = 2 * N
    assert sum(a) == 1 and sum(b) == 1 and all(b[i] >= b[i+1] for i in range(N-1))
    lam = a + [-x for x in reversed(b)]
    v = hive_lp(lam); H = Q(N + 1, 2)
    D1 = E_(a) + U_(b); D2 = U_(a) + E_(b); Ds = min(D1, D2)
    print(f"N={N}: my hive LP kappa_{d}(u3,z_N) = {v:.10f}  claimed {claimed[N]} = {float(claimed[N]):.10f}  diff {abs(v-float(claimed[N])):.1e};"
          f"  E(a)+U(b)={D1} U(a)+E(b)={D2} D_*={Ds} (formula 4(7N-12)/(9N) = {Q(4*(7*N-12), 9*N)});"
          f"  ratio (H-kappa)/D_* = {(H-claimed[N])/Ds}" + (f" claimed {gam[N]}" if N in gam else ''))
for N in range(3, 15):
    a, b = A_N(N), B_N(N); d = 2 * N; lam = a + [-x for x in reversed(b)]
    v = hive_lp(lam); law = Q(3, 2) + ((N - 2) ** 2 // 4 - 1) * Q(N + 2, 4 * N * (N - 1))
    print(f"N={N:2d}: my hive LP kappa_{d}(A_N,B) = {v:.10f}  law {law} diff {abs(v-float(law)):.1e}; D_*(A_N,B) = {Dstar(a,b)} (=(5N-6)/(2N): {Q(5*N-6, 2*N)}), ratio {(Q(N+1,2)-law)/Dstar(a,b)}  [{time.time()-t0:.0f}s]", flush=True)
for N, (a, b) in {6: (A_N(6), B_N(6)), 7: (u3(7), z_N(7)), 10: (u3(10), z_N(10))}.items():
    vals = []
    for z in range(0, 4):
        d = 2 * N + z; lam = a + [Q(0)] * z + [-x for x in reversed(b)]
        vals.append((d, round(hive_lp(lam), 9)))
    print(f"N={N}: padded kappa_d by my hive LP: {vals}  [{time.time()-t0:.0f}s]", flush=True)
