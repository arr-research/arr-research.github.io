"""Independent bounded review: geometric vertices and LR-tableau Horn rows.

Does not import the author's active-set or recursive Horn enumerators.
All arithmetic used for mathematical checks is rational/integer arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def norm_to_uniform(a):
    return sum(abs(x-F(1,3)) for x in a)


def q(a):
    return 2*(1-a[0])-norm_to_uniform(a)


def distance(a,b):
    return min(2*(1-a[0])+norm_to_uniform(b),
               2*(1-b[0])+norm_to_uniform(a))


def lerp(x,y,t):
    return tuple((1-t)*a+t*b for a,b in zip(x,y))


def geometric_vertices():
    e=(F(1),F(0),F(0)); v=(F(2,3),F(1,3),F(0))
    u2=(F(1,2),F(1,2),F(0)); u=(F(1,3),)*3
    triangles=((e,v,u),(u2,v,u))
    all_vertices=set(); counts=[]
    for first,second in product(triangles,repeat=2):
        original=set(product(first,second)); cut=set()
        edges=[]
        for a0,a1 in combinations(first,2):
            for b in second:edges.append(((a0,b),(a1,b)))
        for b0,b1 in combinations(second,2):
            for a in first:edges.append(((a,b0),(a,b1)))
        assert len(edges)==18
        for (a0,b0),(a1,b1) in edges:
            z0=q(a0)-q(b0); z1=q(a1)-q(b1)
            if z0*z1<0:
                t=-z0/(z1-z0)
                assert 0<t<1
                a=lerp(a0,a1,t); b=lerp(b0,b1,t)
                assert q(a)==q(b)
                cut.add((a,b))
        for sign in (1,-1):
            cell={x for x in original if sign*(q(x[0])-q(x[1]))>=0}|cut
            counts.append(len(cell)); all_vertices.update(cell)
    w=(F(2,3),F(1,6),F(1,6))
    r=(F(7,12),F(5,24),F(5,24))
    t=(F(7,12),F(1,3),F(1,12))
    expected=set(product((e,v,u2,u),repeat=2))
    for a,b in ((w,v),(r,u2),(t,u2)):
        expected.update(((a,b),(b,a)))
    assert all_vertices==expected and len(all_vertices)==22
    return all_vertices,counts


def partition(I):
    # Schubert partition, using one-based subset indices.
    return tuple(x-j for x,j in zip(reversed(I),range(len(I),0,-1)))


@lru_cache(None)
def lr_coefficient(alpha,beta,gamma):
    if sum(alpha)+sum(beta)!=sum(gamma):return 0
    if any(x>y for x,y in zip(alpha,gamma)):return 0
    n=len(gamma)
    cells=[(r,c) for r in range(n)
           for c in range(gamma[r]-1,alpha[r]-1,-1)]
    tableau={}; used=[0]*n

    def recurse(i):
        if i==len(cells):return int(tuple(used)==beta)
        row,col=cells[i]; total=0
        for value in range(n):
            if used[value]==beta[value]:continue
            if (row,col+1) in tableau and value>tableau[row,col+1]:continue
            if (row-1,col) in tableau and value<=tableau[row-1,col]:continue
            used[value]+=1
            # Lattice-word condition on every prefix of the reading word.
            if all(used[j]>=used[j+1] for j in range(n-1)):
                tableau[row,col]=value
                total+=recurse(i+1)
                del tableau[row,col]
            used[value]-=1
        return total

    return recurse(0)


def tableau_horn(d):
    rows=[]; counts=[]
    for r in range(1,d):
        sets=list(combinations(range(1,d+1),r)); before=len(rows)
        for I,J,K in product(sets,repeat=3):
            c=lr_coefficient(partition(I),partition(J),partition(K))
            if c:rows.append((I,J,K,c))
        counts.append(len(rows)-before)
    return rows,counts


def main():
    vertices,counts=geometric_vertices()
    rows,horn_counts=tableau_horn(6)
    assert horn_counts==[21,126,228,126,21] and len(rows)==522
    input_path=ROOT/'balanced_three_certificate.json'
    data=json.loads(input_path.read_text())
    found=set(); witness_reports=[]
    for row in data['witnesses']:
        a=tuple(map(F,row['a'])); b=tuple(map(F,row['b']))
        s=tuple(map(F,row['s'])); found.add((a,b))
        assert len(s)==6 and sum(a)==sum(b)==1
        assert all(x>=y>=0 for x,y in zip(a,a[1:]))
        assert all(x>=y>=0 for x,y in zip(b,b[1:]))
        assert all(x>=y>=0 for x,y in zip(s,s[1:]))
        lam=tuple(sorted(a+tuple(-x for x in b),reverse=True))
        negative=tuple(-x for x in reversed(s))
        slacks=[sum(s[i-1] for i in I)+sum(negative[j-1] for j in J)
                -sum(lam[k-1] for k in K) for I,J,K,_ in rows]
        assert min(slacks)>=0
        D=distance(a,b)
        assert D==F(row['D']) and sum(s)==F(row['trace_upper_bound'])
        slack=2-sum(s)-F(17,36)*D
        assert slack>=0
        witness_reports.append({'a':row['a'],'b':row['b'],'D':str(D),
                                'trace':str(sum(s)),'stability_slack':str(slack),
                                'minimum_Horn_slack':str(min(slacks))})
    assert found==vertices
    a=(F(7,12),F(5,24),F(5,24)); b=(F(1,2),F(1,2),F(0))
    lower=sum(max(x,y) for x,y in zip(a,b))
    assert lower==F(31,24) and distance(a,b)==F(3,2)
    assert distance(a,b)/(2-lower)==F(36,17)
    report={'status':'PASS',
            'method_vertices':'Two triangles per sign list; product edges cut by q(a)=q(b)',
            'method_Horn':'Littlewood-Richardson skew tableaux, independently of Horn recursion',
            'cell_vertex_counts_geometry_order':counts,'vertices':22,
            'Horn_counts':horn_counts,'Horn_inequalities_checked':22*522,
            'Horn_max_LR_coefficient':max(c for I,J,K,c in rows),
            'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'sharp_ratio':'36/17','witnesses':witness_reports}
    (ROOT/'independent_balanced_review_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k!='witnesses'})


if __name__=='__main__':main()
