from fractions import Fraction as Q
import json
def add(a,b):return tuple(tuple(x+y for x,y in zip(ar,br)) for ar,br in zip(a,b))
def scale(s,a):return tuple(tuple(s*x for x in row) for row in a)
def transpose(a):return tuple(zip(*a))
def mul(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def tr(a):return sum(a[i][i] for i in range(len(a)))
def total(xs,n):
    out=tuple(tuple(Q(0) for j in range(n)) for i in range(n))
    for a in xs:out=add(out,a)
    return out
def kron(a,b):return tuple(tuple(a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)] for j in range(len(a)*len(b))) for i in range(len(a)*len(b)))
I=((Q(1),Q(0)),(Q(0),Q(1)));X=((Q(0),Q(1)),(Q(1),Q(0)));Z=((Q(1),Q(0)),(Q(0),Q(-1)))
dirs=[X,scale(-1,X),Z,scale(-1,Z)]
F=[scale(Q(1,4),add(I,n)) for n in dirs];tau=[scale(Q(1,2),add(I,n)) for n in dirs]
assert total(F,2)==I
def channel(a):return total((scale(tr(mul(f,a)),t) for f,t in zip(F,tau)),2)
def N(a):return channel(channel(a))
G=[scale(Q(1,4),add(I,scale(Q(1,2),n))) for n in dirs]
c=[Q(1,8)]*4;Omega=total((scale(v,t) for v,t in zip(c,tau)),2)
assert Omega==scale(Q(1,4),I) and tr(Omega)==Q(1,2)
units={(i,j):tuple(tuple(Q(r==i and s==j) for s in range(2)) for r in range(2)) for i in range(2) for j in range(2)}
J=tuple(tuple(N(units[i//2,j//2])[i%2][j%2] for j in range(4)) for i in range(4))
remainder=add(J,scale(-1,kron(I,Omega)))
integrated=total((kron(transpose(add(g,scale(-v,I))),t) for g,v,t in zip(G,c,tau)),4)
assert remainder==integrated
assert all(add(g,scale(-v,I))==scale(Q(1,4),t) for g,v,t in zip(G,c,tau))
bell=[(1,0,0,1),(1,0,0,-1),(0,1,1,0),(0,1,-1,0)]
evals=[Q(1,2),Q(1,4),Q(1,4),Q(0)]
for i,v in enumerate(bell):
    assert tuple(sum(remainder[r][k]*v[k] for k in range(4)) for r in range(4))==tuple(e*x for e,x in zip([evals[i]]*4,v))
    assert sum(x*x for x in v)==2
    for w in bell[:i]:assert sum(x*y for x,y in zip(v,w))==0
assert all(x>=0 for x in evals)
v=bell[-1];dual=tuple(tuple(Q(v[i]*v[j]) for j in range(4)) for i in range(4))
ptr_input=tuple(tuple(sum(dual[2*i+r][2*i+s] for i in range(2)) for s in range(2)) for r in range(2))
ptr_output=tuple(tuple(sum(J[2*r+i][2*s+i] for i in range(2)) for s in range(2)) for r in range(2))
assert ptr_input==I and ptr_output==I
assert tr(mul(J,dual))==tr(Omega)==Q(1,2)
def encode(a):return [[str(x) for x in row] for row in a]
print(json.dumps({'arithmetic':'Exact Fraction; no SDP solver','convention':'Unnormalized input-first Choi J=sum Eij tensor N(Eij); replacer Choi I tensor Omega','prefix_trace_factor':'1/2 (Bloch singular values1/2,0,1/2)','postprocessor':'same four-point planar measure-and-prepare channel','common_component_trace':'1/2','Omega':encode(Omega),'Choi':encode(J),'remainder':encode(remainder),'remainder_Bell_eigenvalues':[str(x) for x in evals],'dual':encode(dual),'dual_partial_trace':'I','dual_objective':'1/2','primal_dual_optimality_for_this_example':True,'scope':'Finite exact Choi and SDP primal/dual witness only; not general theorem/continuum certification or novelty audit.'},indent=2))
