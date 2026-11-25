# Machine-Checked Exact Combinatorial Certificates for Input-Oblivious Unambiguous Hierarchies, Krentel Lex-Max OGTD Collapse, and Single-Query Promise Elimination

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-68VR3XCP679YZVAR` (v1)  
**License:** CC-BY-4.0 (manuscript), MIT (verification repository)  
**Verification Repository:** https://github.com/lluiseriksson/oblivious-unambiguous-hierarchy-certificates (`v2.0.0`)  
**Canonical PDF SHA-256:** `83fbbfdad2e8f77f2a65c1ca90e64678e54b1c50c8a97fdee5f05baa685a071b`

## Abstract

Edward A. Hirsch (arXiv:2611.33126, November 24, 2026) established sharp structural collapses for input-oblivious unambiguous hierarchies built over OUP, proving that OUH subseteq P^{TALLY cap NP} subseteq P_||^{ONP} (Theorem 4.1, Corollary 4.2), that OUH^bullet subseteq OGTD[NP] = OUGTD[FP^{ONP}, co-ONP, P] subseteq OUM via Krentel lexicographically-largest transcripts (Lemma 3.1, Theorem 5.1), that the oblivious unambiguous dot-operator hierarchy collapses completely to exists^{ou}.co-OUP = OUP U co-OUP (Theorem 6.2, Corollary 6.3), that a single loose prOUP query reduces to a standard OUP query (OUP^{prOUP[1]} = OUP^{OUP[1]}, Lemma 6.4, Theorem 6.5), and that SOUP = OUP cap co-OUP (Proposition 6.6). We present a machine-checked, zero-floating-point formalization and finite combinatorial certificate auditor for the order-theoretic, pigeonhole, and oracle-consistency core of these results. An 18-theorem zero-dependency Lean 4 kernel (ObliviousUnambiguousHierarchy.lean, Lean 4.35.0; 0 sorry, 0 warnings, 0 Classical.choice, 11 zero-axiom theorems) formalizes Cantor pairing injectivity and upper bounds, inductive tally-census uniqueness, oblivious bit-by-bit witness extraction, Krentel lex-max transcript soundness, inductive ONP prefix-search bit recovery, co-ONP unique testing, fixed-pair refutation and dot-operator collapse soundness, single-loose-query in-promise forcing, and SOUP shared-witness tagging. OUH-CERT-1.0 audits four exact finite modes across 16 canonical certificates (0.038-0.789 ms) and rejects 60/60 live adversarial forgeries.

## Full Extracted Text

--- Page 1 ---
Machine-Checked Exact Combinatorial Certificates for
Input-Oblivious Unambiguous Hierarchies, Krentel Lex-Max
OGTD Collapse, and Single-Query Promise Elimination
Lluis Eriksson*
November 25, 2026
Abstract
Edward A. Hirsch (arXiv:2611.33126, November 24,
2026) established sharp structural collapses for input-
oblivious unambiguous hierarchies built over OUP, prov-
ing that the language-oracle hierarchy satisfies OUH⊆
PTALLY∩NP ⊆P ONP
∥ (Theorem 4.1, Corollary 4.2), that
the loose promise-oracle hierarchy collapses into OUH • ⊆
OGTD[NP] = OUGTD[FP ONP,co-ONP,P]⊆OUM via
Krentel lexicographically-largest transcripts (Lemma 3.1,
Theorem 5.1), that the oblivious unambiguous dot-
operator hierarchy collapses to∃ ou ·co-OUP = OUP∪
co-OUP (Theorem 6.2, Corollary 6.3), that a single loose
prOUP query reduces to an OUP query (OUP prOUP[1] =
OUPOUP[1], Lemma 6.4, Theorem 6.5), and that SOUP =
OUP∩co-OUP (Proposition 6.6). We present a
standalone, zero-dependencyLean 4.35.0formalization
(ObliviousUnambiguousHierarchy.lean) of 18 finite
combinatorial, order-theoretic, and oracle-consistency
theorems (0sorry, 0 warnings, 0Classical.choice,
11 zero-axiom theorems), paired with a pure-stdlib zero-
float finite verifier (OUH-CERT-1.0) auditing four formally
specified modes across 16 canonical certificates (0.038–
0.789 ms) and rejecting 60/60 live adversarial forgeries.
1 Introduction
Input-oblivious complexity classes [3, 1] restrict nondeter-
ministic witnesses to depend only on the input lengthn
rather than the individual instancex∈ {0,1} n. Combin-
ing obliviousness with unambiguity yields OUP, where all
positive instances of lengthnshare a single unique wit-
nessw n. Building on the loose unambiguous hierarchy of
Hirsch and Sokolov [5], Hirsch [4] proved that the result-
ing hierarchies OUH (language oracles) and OUH • (loose
* Independent researcher; code, Lean 4 proofs, and certificates:
MIT license; manuscript and figures: CC-BY-4.0. Prepared with
transparent AI assistance via Google Antigravity; all Lean 4 the-
orems, verifiers, and tests were independently compiled and ver-
ified locally. Repository:https://github.com/lluiseriksson/
oblivious-unambiguous-hierarchy-certificates.
promise oracles) collapse dramatically:
OUH⊆P TALLY∩NP ⊆P ONP
∥ ,
OUH• ⊆OGTD[NP]
= OUGTD[FPONP,co-ONP,P]⊆OUM,
(1)
while at the base levels∃ ou ·co-OUP = OUP∪co-OUP,
OUPprOUP[1] = OUPOUP[1], and SOUP = OUP∩co-OUP.
Contributions and Explicit Scope.We formally ver-
ify and audit thefinite combinatorial, order-theoretic, and
oracle-consistency coreof [4]. We explicitly donotformal-
ize polynomial-time oracle Turing machines, asymptotic
advice polynomials, or uniform circuit encodings inside
Lean 4; all complexity-class inclusions remain Hirsch’s [4]:
1.Zero-dependency Lean 4 kernel
(§3):18 constructive theorems in
ObliviousUnambiguousHierarchy.lean
(Lean 4.35.0 [2]), 0sorry, 0 warnings,
0Classical.choice, and11 zero-axiom the-
orems, with every formal signature and inductive
predicate stated in Table 1.
2.Pure-stdlib exact verifier (§4):OUH-CERT-1.0, for-
mally specified in Definition 2, auditing four finite
truth-table modes with zero floating-point arithmetic.
3.Empirical atlas & red-team audit (§5):16 canon-
ical certificates (0.038–0.789 ms on Windows 11 /
Python 3.13), four exact sweeps (q= 2..8,h= 4..12,
|Πout|= 1..6), and 60/60 rejected live adversarial forg-
eries.
2 Formal Definitions and Combi-
natorial Core
Definition 1(Oblivious Classes, Operators, and Pair-
ing [4]).For length-ninputsx∈ {0,1} n and polynomial-
length witnessesw∈ {0,1} p(n):
ONP(obliviousNP):L∈ONPiff a polynomial-time
Vand length-only advicew n satisfyx∈L⇐⇒
V(x, wn) = 1andx /∈L⇒ ∀w, V(x, w) = 0.co-ONP
is the complement class.
OUP(obliviousUP):L∈OUPiffL∈ONPand on
every non-empty sliceL∩ {0,1} n,w n is theuniquew
accepted for anyx∈ {0,1}n (ifL∩{0,1} n =∅, nowis
1

--- Page 2 ---
accepted).prOUPis the promise-problem analogue on
Π = (ΠYES,Π NO).
TALLY: unary languages over{1} ∗.SOUP(symmetric
OUP):L∈SOUPiff a single unique length-nwitness
wn certifiesbothx∈Landx /∈L;SOUP SOUP denotes
SOUPwith aSOUPoracle.
OGTD[C](oblivious generate-test-decide):Lis decided
by a triple(G, T, D)with generatorG(1 n)outputting
advicea∈Out G(n), testerTwithOut G(n)⊆Acc T (n),
and deciderD(x, a) =L(x)for alla∈Acc T (n).
OUGTD[F,T,D]further enforces|Acc T (n)| ≤1;OUM
denotes oblivious unambiguous Merlin–Arthur/advice
classes containingOUGTD[FP ONP,co-ONP,P].
Doubled Cantor pairing:cantor 2(a, b) := (a+b)(a+
b+ 1) + 2bfora, b∈N, which is injective and satisfies
cantor2(a, b)< k(k+ 1)whenevera+b < k.
Four exact finite invariants with explicit preconditions
drive (1):
1.Tally census & bit extraction (Lemma 2.8, Theo-
rem 4.1):Knowing the census countc m =|C m|of
a finite setC m ⊆ {0,1}m, any subsetS⊆C m with
|S|=c m equalsC m uniquely. Given an OUP veri-
fierVwith unique witnessw n on a non-empty length-n
slice, thepparallel tally predicatesW i ⇐⇒ ∃x, w:
V(x, w) = 1∧wi = 1 recoverw n bit-for-bit (and return
0p whenL∩ {0,1}n =∅).
2.Krentel lex-max transcript (Lemma 3.1):LetG(1 n) be
a deterministic depth-qadaptive query tree whosej-th
query depends only on the length-(j−1) answer prefix
a<j, and leta ∗ ∈ {0,1}q be the true oracle transcript
(so every 0-bit ofa ∗ queries a NO instance). Define
R(a) to hold iff every 1-bit ofaqueries a YES instance
(matchingG(1 n) along prefixa <j). At the first mis-
match indexjbetween anya∈Randa ∗, the pre-
fixesa <j =a ∗
<j issue the identicalj-th query; since
a∗
j = 0 implies a NO instance whereasa j = 1 cer-
tifies a YES instance, necessarilya j = 0<1 =a ∗
j ,
soa < lex a∗. Hencea ∗ is the unique lexicographical
maximum ofR, recovered inqONP prefix probes and
uniquely accepted by the co-ONP tester
T(a)⇐⇒R(a)∧ ∀b∈ {0,1} q,(a <lex b⇒ ¬R(b)).
(2)
3.Fixed-pair dot-operator collapse (Theorem 6.2):Sup-
poseL(x)⇐⇒ ∃ ouw∈ {0,1}p R(x, w) (p≥1) where
R∈OUP via verifierVwith unique length-oblivious
witnessv N (V((x, w), v)⇐⇒ ¬R(x, w)∧v=v N).
Since at most onew∈ {0,1} p satisfiesR(0 n, w), at
least one of (0 n,0 p) and (0 n,1 p) lies in R. Conse-
quently, the collapsed verifier
V ′(x,(w, v)) :=
 
V((0 n,0 p), v)∨V((0 n,1 p), v)

∧ ¬V((x, w), v) (3)
pinsv=v N on anchor 0 n and transfersv N by
length-obliviousness to arbitraryx∈ {0,1} n, forcing
¬V((x, w), vN)⇐⇒R(x, w) and accepting solely
(wn, vN).
4.Single loose query &SOUPtagging (Lemma 6.4,
Proposition 6.6):For a single-query machineV O(x, w)
queryingq(x, w) with outcomesv 0 =V 0(x, w), v1 =
V 1(x, w), define the sensitive setT={(x, w) :v 0 ̸=
v1}. Loose oracle consistency across all extensionsO
of Π = (Π YES,Π NO) requiresV O0 (x, w) =V O1 (x, w)
wheneverq(x, w)/∈Π YES ∪Π NO, forcingq(T)⊆
ΠYES ∪Π NO; insensitive pairs (v 0 =v 1) eliminate the
query entirely. ForL∈OUP∩co-OUP with verifiersY
(unique witnessw Y forL) andZ(unique witnessw Z
for L), tagging Tag(b, w) := (b= 1∧Y(0 n, w))∨(b=
0∧Z(0 n, w)) pins a unique pair (b ∗, w∗) on 0 n; by
length-obliviousness, everyx∈ {0,1}n is decided using
thesamewitness (b ∗, w∗) viaY(x, w ∗) whenb ∗ = 1 or
¬Z(x, w∗) whenb ∗ = 0.
3 Zero-Dependency Lean 4.35.0
Kernel
We formalize 18 constructive theorems in
lean/ObliviousUnambiguousHierarchy.lean
(Lean 4.35.0, zero external libraries), audited via
lean/AuditAxioms.leanwith 0 warnings, 0sorry,
0Classical.choice, and 0Lean.ofReduceBool(11
zero-axiom theorems, Table 1). Auxiliary inductive
definitions in the module are:
cantor2a b:= (a+b)(a+b+ 1) + 2b;popcount:
List Bool→Ncountstrueentries;BoolSubsets c
holds pointwise on equal-length lists (si =true⇒c i =
true).
LexLta bis MSB-first strict lexicographic order on
equal-lengthList Bool;CertifiedAgainsta t
enforces inductively on equal-length lists that
(a0 =true⇒t 0 =true)∧(a 0 =t 0 ⇒
CertifiedAgainsta ′ t′).
4 Formal Specification of
OUH-CERT-1.0
The pure-stdlib verifierOUH-CERT-1.0
(src/ouh certifier.py,src/ouh exact.py) uses
integer and boolean truth-table arithmetic exclusively, re-
cursively rejecting IEEE-754 floats, booleans-as-integers,
unknown keys, duplicate entries, invalid bitstrings, and
vacuous witnesses across four formally specified modes:
Definition 2(OUH-CERT-1.0JSON Schemas &
Acceptance Predicates).Every certificate contains
schema="OUH-CERT-1.0",mode,cert id, and mode-
specific fields accepted iff:
1.Mode 1 (tallycensus and oblivious extraction):
Given bit-lengths(n, p), universe sizeh, tally bits
Cm ∈ {0,1}h, subsetS⊆C m, and anOUPtruth
tableV:{0,1} n × {0,1}p → {0,1}, accepts iff
S⊆C m ∧ |S|=|Cm| ⇒S=C m,cantor 2 is injective
on claimed pairs,Vhas at most one accepting witness
2

--- Page 3 ---
Table 1: Complete 18-theorem Lean 4.35.0 kernel inObliviousUnambiguousHierarchy.lean(0sorry, 0 warnings,
0Classical.choice, 11 zero-axiom theorems), listing exact formal signatures and statements.
# Lean 4 Theorem Identifier Exact Formalized Type / Statement Ref. [4] Axioms
1cantor pairinginjective cantor2a 1 b1 =cantor2a2 b2 ⇒a1 =a2 ∧b1 =b2 Lem. 2.8[p, Q]
2tally censussubsetexact∀s, c:List Bool,BoolSubsets c⇒popcounts=popcountc⇒s=cLem. 2.8[p, Q]
3tally censusbitdetermined BoolSubsets c⇒popcounts=popcountc⇒s[i]? =c[i]? Lem. 2.8[p, Q]
4obliviouswitnessbitextractionV(x 0, wn)∧(∀x, w, V(x, w)⇒w=wn)⇒((∃x, w, V(x, w)∧bitw i)⇐⇒bitwn i) Thm. 4.1none
5obliviousemptyslicezerowitness(∀x, w,¬V(x, w))⇒ ¬(∃x, w, V(x, w)∧bitw i=true) Thm. 4.1none
6lex maxtranscriptsoundandunique∀a, a∗ :List Bool,CertifiedAgainsta a∗ ⇒a=a∗∨LexLta a∗ Lem. 3.1[p]
7prefix searchbitrecovery(∃r,CertifiedAgainst(p++true::r) (p++b::t))⇐⇒b=trueLem. 3.1[p]
8co onptesteruniqueacceptance|a 1|=|a2|=q∧T R(a1)∧TR(a2)⇒a1 =a2 (TR(a) :=R(a)∧ ∀b, a <lexb⇒ ¬R(b)) Lem. 3.1[p, Q]
9ogtd chaininclusionsound(∀a,Out Ga⇒AccT a)∧(∀a,AccT a⇒ ∀x, D x a=L x)⇒OutGa⇒D x a=L xDef. 2.4none
10dot opfixedpairrefutationw 0 ̸=w1 ∧(∀u, v, R(x0, u)⇒R(x0, v)⇒u=v)∧Dec(R(x0, w0))⇒ ¬R(x0, w0)∨ ¬R(x0, w1) Thm. 6.2none
11dot opcollapseuniquewitnessV-uniq(v N)∧(¬R⇒V(·, vN))∧R-uniq(wn)∧Dec(R)∧V′(x,(w, v))⇒w=wn∧v=v N Thm. 6.2none
12dot opcollapsesoundness(¬R(x 0, w0)∨ ¬R(x0, w1))∧(V(·, vN)⇐⇒ ¬R)∧(L⇐⇒R(·, wn))∧Dec⇒(L(x)⇐⇒V′(x,(wn, vN))) Thm. 6.2none
13dot opuniondistributive(∃w, C(w)∨D(w))⇐⇒(∃w, C(w))∨(∃w, D(w)) Cor. 6.3none
14singleloosequeryinpromisev 0 ̸=v1 ∧(¬P⇒v0 =v1)∧(P∨ ¬P)⇒PLem. 6.4none
15singleloosequeryinsensitiveelimv0 =v1 ⇒ ∀b:Bool,(ifbthenv1 elsev0) =v0 Thm. 6.5none
16soup sharedwitnesstagexact(Y⇐⇒L∧w=w Y)∧(Z⇐⇒ ¬L∧w=wZ)∧Dec(L x0)⇒ ∃!(b∗, w∗),Tag(b∗, w∗) Prop. 6.6none
17soup selflowcomposition(P 1(w1)⇐⇒w1 =w∗1)∧(P2(w∗1, w2)⇐⇒w2 =w∗2)⇒(P1(w1)∧P2(w1, w2)⇐⇒w1 =w∗1 ∧w2 =w∗2) Prop. 6.6none
18krenteltranscriptspacebounds∀a, b, k:N, a+b < k⇒cantor2a b < k(k+ 1) Lem. 2.8[p, Q]
Axiom key:none= zero axioms (11);[p]=[propext](2);[p, Q]=[propext, Quot.sound](5). Dec(P) denotes explicit decidability hypothesisP∨ ¬P.
across allx, and bit-by-bit tally extraction recoversw n
(or0 p on empty slices).
2.Mode 2 (krentel lex max ogtd cert):Given adap-
tive query depthq∈[2,8], explicit prefix-deterministic
query mapQ:{0,1} <q →U, and NP-oracle indicator
O:U→ {0,1}, exhaustively enumerates all2 q tran-
scripts, computesR={a:∀j, a j = 1⇒O(Q(a <j)) =
1}, and accepts iffa ∗ = maxlex R, allqprefix probes
matcha ∗, and|{a:T(a)}|= 1under(2).
3.Mode 3 (dot operator collapse exact):Given
(n, p, r)(p≥1) and finite truth tables forR(x, w)and
innerOUPverifierV((x, w), v)for R, accepts iffV
accepts solelyv N on R,Raccepts at most onew n,
(0n,0 p)∈ R∨(0 n,1 p)∈ R, andV ′ in(3)accepts solely
(wn, vN)forx∈L.
4.Mode 4 (single loose query and soup exact):
Given promise partition(Π YES,Π NO,Π out), single-
query verifier(q(x, w), V 0, V1), and complementary
OUPverifiers(Y, Z)for(L, L), exhaustively replays all
2|Πout| consistent oracle extensionsO, accepting iffV O
is consistent across all extensions,q(T)⊆Π YES∪ΠNO,
insensitive pairs eliminate the query, andTag(b, w)on
0n yields a unique shared witness(b ∗, w∗)deciding all
x∈ {0,1}n.
5 Empirical Atlas and Red-Team
Audit
Runningscripts/run all experiments.py(Win-
dows 11, Python 3.13 pure-stdlib) produces 16 canonical
certificates (4 per mode) and four exact combinatorial
sweeps, audited end-to-end byscripts/verify all.py
with SHA-256 verification across all 41 tracked repository
files.
Krentel Transcripts and Tally Census (Fig. 1).
Across adaptive depthsq= 2. . .8 (2 q = 4. . .256),|R|
spans 7 (sparse), 55 (balanced), and 104 (dense) tran-
Figure 1: (a) Exact Lemma 3.1 Krentel certified tran-
script count|R|across depthsq= 2. . .8 (sparse, bal-
anced, dense regimes) versus 2 q total transcripts andq
ONP prefix probes. (b) Exact Lemma 2.8 tally-census
collapse from
  h
cm

same-size subsets to exactly 1 certified
subset (h= 4. . .12).
scripts atq= 8, yet in 100% of instances ONP prefix
search recoversa ∗ inqprobes and tester (2) achieves
|AccT |= 1. In Mode 1 (0.038–0.084 ms), exact bit-by-bit
tally extraction recovers both non-empty witnesses (up to
n= 4, p= 6,|L|= 11) and empty-slice 0 5, while census
uniqueness collapses
 12
6

= 924 same-size subsets (out of
212 = 4096) to 1.
Dot Collapse, Loose Extensions, andSOUP
(Fig. 2).In Mode 3 (0.068–0.183 ms), fixed-pair refuta-
tion collapses up to 22+3 = 32 witness pairs to (wn, vN) at
(n, p, r) = (4,2,3) (|L|= 9). In Mode 4 (0.117–0.789 ms),
exhaustive auditing across up to 25 = 32 consistent exten-
sions (and 2 6 = 64 in Experiment 3, 0.653 ms) confirms
that all 24/32 insensitive pairs querying Π out are safely
eliminated while every sensitive pair lies strictly inside
ΠYES ∪Π NO, and certifies Proposition 6.6 shared SOUP
witnesses for both 0 n ∈L(1|wY) and 0 n /∈L(0|wZ).
Replay Atlas and Red-Team Audit (Fig. 3, Ta-
ble 2).All 16 canonical certificates replay in 0.038–
0.789 ms with zero floats. Our adversarial suite
3

--- Page 4 ---
Figure 2: (a) Theorem 6.2 dot-operator collapse across
(n, p, r): fixed-pair refutation collapses 2 p+r candidate
pairs to exactly 1 unique witness (w n, vN). (b) Exhaus-
tive Lemma 6.4 loose-oracle audit across|Π out|= 1. . .6
(2. . .64 consistent extensions, 0.128–0.653 ms).
Figure 3: (a) Exact zero-float replay latency across all
16 canonicalOUH-CERT-1.0certificates (0.038–0.789 ms).
(b) Red-team adversarial audit rejecting 60/60 live forgery
attacks across all modes.
(tests/test suite.py) tests 60 live forgery attacks—
including float/bool type confusion, ambiguous or non-
oblivious witnesses (e.g. two distinctw 1 ̸=w 2 accepted in
Mode 1), tampered Krentel prefix probes (Mode 2), vacu-
ous or mismatched dot-collapse pairs (Mode 3), sensitive
queries leaking into Π out and non-complementary SOUP
verifiers (Mode 4)—achieving60/60 rejectionswith zero
bypasses.
6 Conclusion
We delivered an 18-theorem zero-dependency Lean 4
kernel (11 zero-axiom theorems, 0Classical.choice)
with full formal specifications and the exact finite ver-
ifierOUH-CERT-1.0for the finite combinatorial core
of Hirsch’s input-oblivious unambiguous hierarchy col-
lapses [4]. Mechanizing uniform polynomial-time oracle
Turing machines in Lean 4 to bridge these finite combi-
natorial lemmas to asymptotic complexity-class inclusions
remains open.
References
[1] Scott Aaronson and Andrew Drucker. A full charac-
terization of quantum advice.SIAM Journal on Com-
puting, 43(3):1131–1183, 2014.
Table 2: Summary of all 16 canonicalOUH-CERT-1.0cer-
tificates (representative witnesses) and 60/60 adversarial
audit.Verification Mode Concrete Certified Range ms Red-Team
M1: Tally Census & Extraction (4)h≤12 ( 126
=924→1),n≤4, p≤6, 05empty 0.038–0.084 12/12M2: Krentel Lex-Max & OUGTD (4)q∈[2,8],|R| ∈ {7,55,104},|AccT|=1 0.050–0.133 12/12M3: Dot-Operator Collapse (4) (n, p, r)≤(4,2,3), 32→1 unique (wn, vN) 0.068–0.183 12/12M4: Loose Query & SOUP (4) 25=32 ext., 24/32 insens.,1|wY/0|wZ0.117–0.789 14/14Global Schema / Type / Bitstring Float, bool-as-int, duplicate, bad bits – 10/10
Total (16 certs) All 4 finite mechanisms of [4] 0.038–0.789 60/60
[2] Leonardo de Moura and Sebastian Ullrich. The Lean
4 theorem prover and programming language. In
Automated Deduction – CADE 28, pages 625–635.
Springer, 2021.
[3] Lance Fortnow, Rahul Santhanam, and Ryan
Williams. Fixed-polynomial size circuit bounds. In
Proceedings of the 24th Annual IEEE Conference on
Computational Complexity (CCC), pages 19–26, 2009.
[4] Edward A. Hirsch. A note on input-oblivious unam-
biguous hierarchies.arXiv preprint arXiv:2611.33126,
2026.
[5] Edward A. Hirsch and Dmitry Sokolov. On the unam-
biguous polynomial hierarchy and promise problems.
Information Processing Letters, 115(2):317–322, 2015.
4
