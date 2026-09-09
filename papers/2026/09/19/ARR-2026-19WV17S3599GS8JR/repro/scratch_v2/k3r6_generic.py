import sys, time, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scratch_D2_review"))
sys.path.insert(0, '.')
import review_exact_delta as R
# generic k=3, r=6 for L=4,5,6: prediction of the graph-witness theorem (r=2k): k*floor(L/2) = 6, 6, 9
for L, seed in [(4, 701), (5, 702), (6, 703)]:
    Ws = R.random_frames(6, 3, L, seed)
    t0 = time.time()
    R.run(f"k=3 N=6 L={L} generic seed {seed}", 6, 3, R.NODES[:L], Ws, expect=3*(L//2), verbose=True, emax=6)
    print(f"  elapsed {time.time()-t0:.1f}s"); sys.stdout.flush()
