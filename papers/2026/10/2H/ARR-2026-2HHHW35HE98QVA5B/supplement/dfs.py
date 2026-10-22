# independent brute force: DFS over sequences, with memo-free branch&bound. n<=5
import sys,itertools
from common import *
def F(n):
    T=list(itertools.product(range(1,n+1),repeat=3))
    best=[0,None]
    def rec(seq,cand):
        if len(seq)>best[0]: best[0]=len(seq);best[1]=list(seq)
        if len(seq)+len(cand)<=best[0]: return
        for i,t in enumerate(cand):
            nc=[u for u in cand if u!=t and lt2(t,u)]
            seq.append(t);rec(seq,nc);seq.pop()
    rec([],T)
    return best
for n in range(1,int(sys.argv[1])+1):
    b=F(n);print(n,b[0],b[1],check_seq(b[1],n),flush=True)
