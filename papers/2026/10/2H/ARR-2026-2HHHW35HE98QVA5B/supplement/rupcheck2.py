# Forward RUP checker with 2-watched literals + trail; deletions ignored. usage: rupcheck2.py cnf proof
import sys
def main(cnff,prf):
    cls=[]
    for l in open(cnff):
        if l[0] in 'pc': continue
        cls.append([int(x) for x in l.split()[:-1]])
    nv=max(abs(x) for c in cls for x in c)+1
    val=[0]*(2*nv+2)   # index lit+nv
    watch={}
    trail=[]
    def lv(l): return val[l+nv]
    def setl(l): val[l+nv]=1; val[-l+nv]=-1; trail.append(l)
    units=[]; conflict0=False
    def add(c):
        if len(c)==0: return 'empty'
        if len(c)==1: units.append(c[0]); return
        watch.setdefault(c[0],[]).append(c); watch.setdefault(c[1],[]).append(c)
    def prop(q):
        # q: index into trail
        while q<len(trail):
            l=trail[q]; q+=1; fl=-l
            ws=watch.get(fl,[]); keep=[]; i=0; confl=False
            while i<len(ws):
                c=ws[i]; i+=1
                if c[0]==fl: c[0],c[1]=c[1],c[0]
                if lv(c[0])==1: keep.append(c); continue
                for k in range(2,len(c)):
                    if lv(c[k])>=0:
                        c[1],c[k]=c[k],c[1]; watch.setdefault(c[1],[]).append(c); break
                else:
                    keep.append(c)
                    if lv(c[0])==-1: keep.extend(ws[i:]); confl=True; break
                    setl(c[0])
            watch[fl]=keep
            if confl: return True
        return False
    for c in cls: add(c)
    # level-0 propagation
    for u in units:
        if lv(u)==-1: print("trivially UNSAT"); return True
        if lv(u)==0: setl(u)
    if prop(0): print("CNF refuted by UP alone"); return True
    base=len(trail); n=0
    for l in open(prf):
        t=l.split()
        if not t or t[0]=='d': continue
        c=[int(x) for x in t]; assert c[-1]==0; c=c[:-1]
        # assume negation
        mark=len(trail); conf=False
        for x in c:
            if lv(-x)==1: continue
            if lv(-x)==-1: conf=True; break   # x already true -> trivially implied
            setl(-x)
        if not conf: conf=prop(mark)
        for l2 in trail[mark:]: val[l2+nv]=0; val[-l2+nv]=0
        del trail[mark:]
        if not conf: print("RUP FAIL at lemma",n,c); return False
        n+=1
        if not c: print("VERIFIED: empty clause derived by RUP;",n,"lemmas"); return True
        # add lemma; handle unit / watch validity
        if len(c)==1:
            if lv(c[0])==-1: print("VERIFIED: unit contradicts level 0;",n); return True
            if lv(c[0])==0:
                setl(c[0])
                if prop(len(trail)-1): print("VERIFIED: level-0 conflict;",n,"lemmas"); return True
        else:
            # order so watched lits are non-false if possible
            c.sort(key=lambda x:-lv(x))
            add(c)
            if lv(c[0])==-1: print("VERIFIED: lemma falsified at level 0;",n); return True
            if lv(c[1])==-1 and lv(c[0])==0:
                setl(c[0])
                if prop(len(trail)-1): print("VERIFIED: level-0 conflict;",n); return True
    print("NOT VERIFIED: proof ended w/o empty clause"); return False
sys.exit(0 if main(*sys.argv[1:3]) else 1)
