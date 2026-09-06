"""Independent N5 audit: explicit geometry, LR tableaux, rational certificates.

Does not import the author's Horn recursion, geometry, proposer or verifier.
Adapted from the independent cycle3 N4 LR review, replacing counting by
existence of a semistandard lattice-word tableau (the Horn criterion).
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations,product
from math import lcm,comb
from pathlib import Path
import argparse,hashlib,json,time,sys
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def E(a):return 2*(1-a[0])
def U(a):return sum(abs(x-Q(1,len(a))) for x in a)
def q(a):return E(a)-U(a)
def distance(a,b):return min(E(a)+U(b),U(a)+E(b))
def geometry(n):
 u=(Q(1,n),)*n
 vs={(k,l):(Q(n-l+k,n*k),)*k+(Q(1,n),)*(l-k)+(Q(0),)*(n-l) for k in range(1,n) for l in range(k,n)}
 edge=lambda a,b:tuple(sorted((a,b)))
 edges={edge(u,v) for v in vs.values()}
 for (k,l),(h,j) in combinations(vs,2):
  if k==h or l==j:edges.add(edge(vs[k,l],vs[h,j]))
 base=sorted({u}|set(vs.values()));assert len(base)==1+comb(n,2)
 assert len(edges)==n*(n-1)*(2*n-1)//6
 vertices=set(product(base,repeat=2))
 for fixed,(a,b) in product(base,sorted(edges)):
  qa,qb=q(a),q(b);target=q(fixed)
  if min(qa,qb)<target<max(qa,qb):
   t=(target-qa)/(qb-qa);x=tuple((1-t)*aa+t*bb for aa,bb in zip(a,b));assert q(x)==target
   vertices.update([(fixed,x),(x,fixed)])
 return base,edges,vertices
def partition(subset):return tuple(value-position for value,position in zip(reversed(subset),range(len(subset),0,-1)))
@lru_cache(None)
def lr_exists(left,content,outer):
 r=len(outer)
 if sum(left)+sum(content)!=sum(outer) or any(a>c or b>c for a,b,c in zip(left,content,outer)):return False
 cells=[(i,j) for i in range(r) for j in range(outer[i]-1,left[i]-1,-1)]
 assigned={};used=[0]*r
 def fill(pos):
  if pos==len(cells):return tuple(used)==content
  i,j=cells[pos]
  for symbol in range(r):
   if used[symbol]>=content[symbol]:continue
   if (i,j+1) in assigned and symbol>assigned[i,j+1]:continue
   if (i-1,j) in assigned and symbol<=assigned[i-1,j]:continue
   used[symbol]+=1
   if all(used[k]>=used[k+1] for k in range(r-1)):
    assigned[i,j]=symbol
    if fill(pos+1):used[symbol]-=1;del assigned[i,j];return True
    del assigned[i,j]
   used[symbol]-=1
  return False
 return fill(0)
def lr_triples(d):
 triples=[];counts=[]
 for r in range(1,d):
  subs=list(combinations(range(1,d+1),r));by_sum={};parts={s:partition(s) for s in subs}
  for K in subs:by_sum.setdefault(sum(K),[]).append(K)
  rows=[]
  for I,J in product(subs,repeat=2):
   a,b=sorted((parts[I],parts[J]))
   for K in by_sum.get(sum(I)+sum(J)-r*(r+1)//2,[]):
    if lr_exists(a,b,parts[K]):rows.append((I,J,K))
  triples.extend(rows);counts.append(len(rows));print('LR',r,len(rows),'cache',lr_exists.cache_info(),flush=True)
 return triples,counts
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--fresh-lr',action='store_true',help='Reconstruct all LR triples without reading cached rows.')
 args=parser.parse_args()
 started=time.monotonic();report=dict(status='STARTED',method='Independent explicit geometry and LR lattice-word tableaux; author generators not imported')
 def save(): (HERE/'independent_review.json').write_text(json.dumps(report,default=str,indent=2)+'\n',encoding='utf-8')
 save();cert=read(ROOT/'optimal_constant_N5_d10.json');base,edges,vertices=geometry(5)
 author_pairs={(tuple(map(Q,x['a'])),tuple(map(Q,x['b']))) for x in cert['certificates']}
 expanded=author_pairs|{(b,a) for a,b in author_pairs}
 assert expanded==vertices and len(vertices)==267 and len(author_pairs)==139
 cache_path=HERE/'lr_10_independent.json'
 cache=read(cache_path) if cache_path.exists() and not args.fresh_lr else None
 cache_matches=cache is not None and cache.get('generator_sha256')==sha(Path(__file__))
 if cache_matches:
  triples=[tuple(tuple(z) for z in t) for t in cache['triples']];counts=cache['counts'];print('reusing independent LR cache',flush=True)
  report.update(lr_source='cached',lr_cache_reason='matching generator hash')
 else:
  reason='--fresh-lr requested' if args.fresh_lr else ('generator hash changed' if cache is not None else 'cache absent')
  print('regenerating independent LR triples:',reason,flush=True)
  triples,counts=lr_triples(10)
  cache_path.write_text(json.dumps({'generator_sha256':sha(Path(__file__)),'counts':counts,'triples':triples},separators=(',',':'))+'\n',encoding='utf-8')
  report.update(lr_source='regenerated',lr_cache_reason=reason)
 save()
 author=read(ROOT/'horn_10.json');author_triples={tuple(tuple(z) for z in t) for t in author['triples']};ts=set(triples)
 assert ts==author_triples and counts==[55,1287,12140,46208,71973,46208,12140,1287,55] and len(ts)==191353
 print('all LR sets equal',len(ts),flush=True)
 # This direct indexed sum is independent of the proposer's compressed LP rows.
 arrs=[]
 for pos in range(3):
  a=np.full((len(triples),9),10,dtype=np.int64)
  for k,t in enumerate(triples):a[k,:len(t[pos])]=[v-1 if pos!=1 else 10-v for v in t[pos]]
  arrs.append(a)
 def primal(a,b,s):
  assert sum(a)==sum(b)==1 and tuple(sorted(a,reverse=True))==a and tuple(sorted(b,reverse=True))==b
  assert tuple(sorted(s,reverse=True))==s and min(s)>=0 and s[-1]==0 and len(s)==10
  lam=a+tuple(-x for x in reversed(b));den=lcm(*(x.denominator for x in s+lam));si=np.array([int(x*den) for x in s]+[0],dtype=np.int64);li=np.array([int(x*den) for x in lam]+[0],dtype=np.int64)
  assert max(abs(int(x)) for x in list(si)+list(li))*30<2**60
  slack=si[arrs[0]].sum(axis=1)-si[arrs[1]].sum(axis=1)-li[arrs[2]].sum(axis=1);minimum=int(slack.min());assert minimum>=0
  return Q(minimum,den)
 gamma=Q(113,152);results=[];contacts=[];all_slacks=[];witnesses={}
 for index,r in enumerate(cert['certificates']):
  a,b,s=(tuple(map(Q,r[k])) for k in ['a','b','common_spectrum']);lam=a+tuple(-x for x in reversed(b));D=distance(a,b);cost=sum(s)
  assert D==Q(r['D']) and cost==Q(r['exact_cost'])
  minimum=primal(a,b,s);primal(b,a,s)
  coeff=[Q(0)]*9;objective=Q(0)
  for term in r['dual_terms']:
   weight=Q(term['weight']);assert weight>=0
   if 'Horn_triple' in term:
    t=tuple(tuple(x) for x in term['Horn_triple']);assert t in ts;I,J,K=t
    for i in I:
     if i<10:coeff[i-1]+=weight
    for j in J:
     if j>1:coeff[10-j]-=weight
    objective+=weight*sum(lam[k-1] for k in K)
   else:
    i=term['ordering_index'];assert 1<=i<=8;coeff[i-1]+=weight;coeff[i]-=weight
  assert all(x<=1 for x in coeff) and [Q(x) for x in r['dual_nonnegative_residual']]==[1-x for x in coeff] and objective==cost
  slack=Q(3)-cost-gamma*D;assert slack>=0
  if D:assert Q(r['ratio'])==(Q(3)-cost)/D
  for pair in {(a,b),(b,a)}:
   witnesses[pair]=s;all_slacks.append((pair,slack))
   if slack==0:contacts.append(pair)
  results.append({'a':a,'b':b,'cost':cost,'D':D,'slack':slack,'minimum_Horn_slack':minimum,'dual_terms':len(r['dual_terms'])})
  if index%20==0:print('exact primal dual',index+1,flush=True)
 # Contact zero points are now checked independently, including each cut cell.
 e=(Q(1),)+(Q(0),)*4;u=(Q(1,5),)*5;A=(Q(13,20),)+(Q(7,80),)*4;B=(Q(1,2),Q(1,2),Q(0),Q(0),Q(0))
 assert set(contacts)=={(e,u),(u,e),(A,B),(B,A)}
 def member(v,k):return v[k-1]>=Q(1,5)>=v[k] if k<5 else v[-1]>=Q(1,5)
 cells=[]
 for k,l,orientation in product(range(1,6),range(1,6),[-1,1]):
  vc=[(a,b) for a,b in vertices if member(a,k) and member(b,l) and orientation*(q(a)-q(b))>=0]
  zero=[v for v in vc if v in set(contacts)]
  # Degenerate empty/non-full cells are retained; the bound only needs every contact hull included.
  assert len(zero)<=2
  if len(zero)==2:assert set(zero) in [{(e,u),(A,B)},{(u,e),(B,A)}]
  cells.append({'k':k,'l':l,'orientation':orientation,'vertices':len(vc),'zero_vertices':zero})
 midpoint=read(ROOT/'contact_midpoint.json');a,b,s=(tuple(map(Q,midpoint[k])) for k in ['a','b','s']);assert a==tuple((x+y)/2 for x,y in zip(e,A)) and b==tuple((x+y)/2 for x,y in zip(u,B));midmin=primal(a,b,s);D=distance(a,b);gap=3-sum(s)-gamma*D
 assert sum(s)==Q(69,40) and D==Q(19,20) and gap==Q(91,160)
 # Admissibility of the rank-two all-ambient lower-bound family (analytic proof in manuscript).
 for d in range(5,26):assert lr_exists(partition((1,3)),partition((1,d-1)),partition((2,d-1)))
 report.update(status='PASS',elapsed_seconds=time.monotonic()-started,coefficient=gamma,independent_base_vertices=len(base),independent_base_edges=len(edges),ordered_vertices=len(vertices),sign_classes=len(author_pairs),LR_counts=counts,LR_triples=len(triples),LR_equals_author=True,exact_primal_checks=2*len(author_pairs)*len(triples)+len(triples),exact_dual_checks=len(results),contacts=contacts,positive_vertex_min_slack=min(s for p,s in all_slacks if s>0),midpoint={'cost':sum(s),'D':D,'gap':gap,'minimum_Horn_slack':midmin},witnesses=results,cells=cells,source_hashes={p.name:sha(p) for p in [Path(__file__),ROOT/'optimal_constant_N5_d10.json',ROOT/'horn_10.json',ROOT/'contact_midpoint.json']},limits=['Analytic Horn sufficiency and general all-dimension claims require manuscript proof.','No external refereeing or bibliographic-priority certification.','Integer checks exactly verify explicit finite witnesses; they do not assert a polynomial total running time.'])
 save();print(json.dumps({k:v for k,v in report.items() if k not in ['witnesses','cells','source_hashes']},default=str,indent=2),flush=True)
if __name__=='__main__':main()
