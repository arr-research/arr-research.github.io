"""Extended dimension-free test: ALL tiles of ALL certificates at z=1 (m=3..8) instantiated at z' = 2,3,4 (d' <= 13), and all tiles
of the z=0 certificates instantiated at z'=1,2 -- validity by own LR >= 1 only (Klyachko necessity), no T-membership needed."""
import os; AUTHOR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "author")); REVIEWER_DIR = os.path.dirname(os.path.abspath(__file__))  # repro: these replace absolute paths in the original review scripts
import sys, json, itertools, time
sys.path.insert(0, REVIEWER_DIR)
from tiles_check import instantiate
W = AUTHOR_DIR
t0 = time.time()
for z, zps in ((1, (2, 3, 4)), (0, (1, 2))):
    for m in range(3, 9):
        if f"certs_m{m}_z{z}.json" not in __import__('os').listdir(W): continue
        C = json.load(open(f"{W}/certs_m{m}_z{z}.json")); stats = {zp: [0, 0] for zp in zps}; badforms = {zp: set() for zp in zps}
        for gk, cert in C.items():
            for t in cert['tiles']:
                for zp in zps:
                    if m + zp + 3 > 13: continue
                    stats[zp][0] += 1
                    if instantiate(tuple(t['Ka']), tuple(t['Kb']), tuple(t['U']), tuple(t['Noff']), m, zp) is not None: stats[zp][1] += 1
                    else: badforms[zp].add(gk)
        print(f"certs z={z} m={m}: " + "; ".join(f"z'={zp}: {v[1]}/{v[0]} tiles realisable, forms with a non-realisable tile: {sorted(badforms[zp])}" for zp, v in stats.items() if v[0]) + f"  ({time.time()-t0:.0f}s)", flush=True)
