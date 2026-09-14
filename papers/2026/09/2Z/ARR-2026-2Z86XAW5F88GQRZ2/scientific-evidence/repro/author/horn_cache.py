"""Generate and cache Horn triples T^d_r (Fulton recursion) as pickle, d up to 9."""
import sys, pickle, time, os
from check_horn_lp import horn_t
d = int(sys.argv[1])
fn = f"horn_d{d}.pkl"
if os.path.exists(fn): print("exists"); sys.exit()
t0 = time.time(); T = {r: horn_t(r, d) for r in range(1, d)}
pickle.dump(T, open(fn, "wb")); print(d, {r: len(v) for r, v in T.items()}, sum(len(v) for v in T.values()), f"{time.time()-t0:.0f}s")
