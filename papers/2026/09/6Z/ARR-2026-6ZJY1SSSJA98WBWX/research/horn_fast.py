"""Vectorized evaluation of the classical recursive Horn definition.

Integer arithmetic throughout. Arrays accelerate filtering only; there is no
relaxation or symmetry assumption in the enumeration.
"""
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json, time
import numpy as np

@lru_cache(None)
def horn(r,d):
    subsets=list(combinations(range(1,d+1),r))
    bysum={}
    for k,K in enumerate(subsets): bysum.setdefault(sum(K),[]).append(k)
    candidates=np.array([(i,j,k) for i,I in enumerate(subsets) for j,J in enumerate(subsets)
                         for k in bysum.get(sum(I)+sum(J)-r*(r+1)//2,[])],dtype=np.int32)
    if not len(candidates):return ()
    subs=np.array(subsets,dtype=np.int32)
    for p in range(1,r):
        for A,B,C in horn(p,r):
            a=subs[:,np.array(A)-1].sum(axis=1)
            b=subs[:,np.array(B)-1].sum(axis=1)
            c=subs[:,np.array(C)-1].sum(axis=1)
            i,j,k=candidates.T
            candidates=candidates[a[i]+b[j]<=c[k]+p*(p+1)//2]
    return tuple((subsets[i],subsets[j],subsets[k]) for i,j,k in candidates)

def generate(d,path):
    started=time.monotonic();triples=[];counts=[]
    for r in range(1,d):
        rows=horn(r,d);counts.append(len(rows));triples.extend(rows)
        print('Horn',d,r,len(rows),'seconds',round(time.monotonic()-started,2),flush=True)
    Path(path).write_text(json.dumps({'dimension':d,'counts':counts,'triples':triples},separators=(',',':'))+'\n')
    return triples

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--dimension',type=int,default=10)
    args=parser.parse_args()
    generate(args.dimension,Path(__file__).with_name(f'horn_{args.dimension}.json'))
