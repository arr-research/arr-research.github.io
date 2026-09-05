"""Exact cell geometry for balanced spectral distance, independent of Horn LPs."""
from fractions import Fraction as Q
from itertools import combinations, product

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))

def rank(rows):
    if not rows:return 0
    a=[list(map(Q,row)) for row in rows];r=0
    for k in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][k]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r]
        v=a[r][k];a[r]=[x/v for x in a[r]]
        for j in range(r+1,len(a)):
            v=a[j][k];a[j]=[x-v*y for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r

def solve(rows,rhs):
    n=len(rhs);a=[list(map(Q,row))+[Q(y)] for row,y in zip(rows,rhs)]
    for k in range(n):
        i=next((i for i in range(k,n) if a[i][k]),None)
        if i is None:return None
        a[k],a[i]=a[i],a[k];v=a[k][k];a[k]=[x/v for x in a[k]]
        for j in range(n):
            if j!=k:
                v=a[j][k];a[j]=[x-v*y for x,y in zip(a[j],a[k])]
    return tuple(row[-1] for row in a)

def E(a):return 2*(1-a[0])
def U(a):return sum(abs(x-Q(1,len(a))) for x in a)
def q(a):return E(a)-U(a)
def D(a,b):return min(E(a)+U(b),U(a)+E(b))

def cells(N):
    dim=N-1
    one=(Q(1),)+(Q(0),)*dim
    forms=[tuple(Q(int(i==j)) for j in range(N)) for i in range(1,N)]
    forms.append((Q(1),)+(Q(-1),)*dim)
    base=[sub(forms[i],forms[i+1]) for i in range(N-1)]+[forms[-1]]
    result=[]
    for r in range(1,N):
        rows=base+[sub(forms[r-1],scale(Q(1,N),one)),sub(scale(Q(1,N),one),forms[r])]
        vertices=set()
        for ids in combinations(range(len(rows)),dim):
            x=solve([rows[i][1:] for i in ids],[-rows[i][0] for i in ids])
            if x is not None and all(dot(row,(Q(1),)+x)>=0 for row in rows):
                vertices.add(x+(1-sum(x),))
        edges=[]
        for a,b in combinations(sorted(vertices),2):
            common=[row[1:] for row in rows if dot(row,(Q(1),)+a[:-1])==dot(row,(Q(1),)+b[:-1])==0]
            if rank(common)==dim-1:edges.append((a,b))
        result.append({'r':r,'rows':rows,'vertices':sorted(vertices),'edges':edges})
    return result

def cut_vertices(N):
    cs=cells(N)
    base=sorted(set(a for c in cs for a in c['vertices']))
    edges=sorted(set(e for c in cs for e in c['edges']))
    vertices=set(product(base,repeat=2));extra=[]
    for a,(b,c) in product(base,edges):
        qa,qb,qc=q(a),q(b),q(c)
        if min(qb,qc)<qa<max(qb,qc):
            t=(qa-qb)/(qc-qb)
            x=add(scale(1-t,b),scale(t,c))
            assert q(x)==qa
            vertices.add((a,x));vertices.add((x,a))
            extra.append({'fixed':a,'edge':(b,c),'t':t,'point':x})
    return sorted(vertices),cs,extra
