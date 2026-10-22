"""Ground kernels from classified occupations, with an arbitrary odd cycle."""
from pathlib import Path
import json,math,itertools
import sympy as sp
R=Path(__file__).parent

def profiles(a,s):
    m=len(a);q=2*s+2;nu=[0]*q;C=[[0]*q for _ in range(q)]
    b=[s-x for x in a];rr=[a[(i-1)%m]+a[i]+a[(i+1)%m] for i in range(m)]
    for i in range(m):
        r=rr[i];nu[r]+=b[i];C[r][r]+=b[i]*(b[i]-1)
        j=(i+1)%m;t=rr[j];C[r][t]+=b[i]*b[j];C[t][r]+=b[i]*b[j]
    return nu,C

def matrix(nu,C):
    q=len(nu);M=[[nu[i]*nu[j]-(nu[i] if i==j else 0) for j in range(q)] for i in range(q)]
    for i in range(q-1):
        for j in range(q-1):
            c=C[i][j]
            if c:
                M[i][j]-=c;M[i+1][j]+=c;M[i][j+1]+=c;M[i+1][j+1]-=c
    return M

def split_pattern(k,s,t,partial=None):
    a=[0]*(2*k+1);a[0]=t;a[1]=(s-1 if partial is None else s)-t
    for j in range(k-1):a[3+2*j]=s-(j==partial)
    return a

def endpoint_pattern(k,s,j):
    a=[0]*(2*k+1)
    for i in range(k):a[2*i]=s-(i==j)
    return a

def ground(k,s):
    q=2*s+2;M=[[0]*q for _ in range(q)];N=0
    patterns=[]
    for t in range(s):patterns.append((split_pattern(k,s,t),math.comb(s,t)*math.comb(s,s-1-t)))
    for j in range(k-1):
        for t in range(s+1):patterns.append((split_pattern(k,s,t,j),s*math.comb(s,t)**2))
    for j in range(k):patterns.append((endpoint_pattern(k,s,j),-s))
    for a,w in patterns:
        assert sum(a)==k*s-1
        e=sum(x*(x-1)//2 for x in a)+sum(a[i]*a[(i+1)%len(a)] for i in range(len(a)))
        assert e==(s-1)*(k*s-2)//2
        nu,C=profiles(a,s);Q=matrix(nu,C);N+=w
        for i in range(q):
            for j in range(q):M[i][j]+=w*Q[i][j]*(2*k+1)
    N*=2*k+1
    assert N==(2*k+1)*(math.comb(2*s,s-1)+(k-1)*s*math.comb(2*s,s)-k*s)
    return sp.Matrix(M),N

def symbolic_ground(s):
    # For k>=3, each extra full selected class and its following empty class
    # contributes s vertices of profile 2s and an internal ordered clique.
    # The far partial case occurs k-3 times; endpoint-far occurs k-2 times.
    k=sp.symbols('k',integer=True,positive=True);q=2*s+2
    M=sp.zeros(q)
    pats=[]
    for t in range(s):pats.append((split_pattern(4,s,t),math.comb(s,t)*math.comb(s,s-1-t)))
    for t in range(s+1):
        w=s*math.comb(s,t)**2
        pats.append((split_pattern(4,s,t,0),2*w))
        pats.append((split_pattern(4,s,t,1),(k-3)*w))
    pats.append((endpoint_pattern(4,s,0),-2*s))
    pats.append((endpoint_pattern(4,s,1),-(k-2)*s))
    for a,w in pats:
        nu,C=profiles(a,s);nu[2*s]+=(k-4)*s;C[2*s][2*s]+=(k-4)*s*(s-1)
        M+=w*sp.Matrix(matrix(nu,C))
    return M.applyfunc(sp.expand),k

if __name__=='__main__':
    # The supported standalone route reproduces the complete included package.
    import subprocess,sys
    raise SystemExit(subprocess.call([sys.executable,'-B',str(R/'verify_all.py')],cwd=R))
