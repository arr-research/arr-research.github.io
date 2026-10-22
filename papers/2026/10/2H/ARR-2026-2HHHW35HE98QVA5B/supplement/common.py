import itertools
def lt2(a,b): return sum(1 for i in range(3) if a[i]<b[i])>=2
def check_seq(seq,n):
    """independent checker: all coords in [1,n], pairwise a_i <_2 a_j for i<j (distinctness implied)"""
    if any(not(1<=c<=n) for t in seq for c in t): return False
    return all(lt2(seq[i],seq[j]) for i in range(len(seq)) for j in range(i+1,len(seq)))
