import sys, time, numpy as np
sys.path.insert(0, '.')
import review_potapov_search as PS, review_exact_delta as R
L, seed, delta = 3, 101, 2
Ws_sym = R.random_frames(4, 2, L, seed)
Ws = [np.array(W.tolist(), dtype=complex) for W in Ws_sym]
zetas = [complex(zt) for zt in R.NODES[:L]]
print(f"=== instance L={L} seed {seed} (exact delta_Gr = {delta})  [L=3 stage only, rerun 2026-09-08]")
for d in range(0, delta + 1):
    best, dt = PS.search(4, 2, d, zetas, Ws, restarts=(120 if d < delta else 40), seed=d)
    print(f"  degree d={d}: best objective over restarts = {best:.3e}   ({dt:.0f}s)"); sys.stdout.flush()
