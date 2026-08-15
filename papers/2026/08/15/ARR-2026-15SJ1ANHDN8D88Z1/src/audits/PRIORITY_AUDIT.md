# Priority audit (primary-source led, provisional)

## Established ingredients

1. State exclusion---reporting information that rules out one or more source
   labels---is established.  Bandyopadhyay, Jain, Oppenheim, and Perry formulate
   conclusive exclusion as an SDP and study exact exclusion conditions in
   *Physical Review A* **89**, 022336 (2014), arXiv:1306.4683.  A list of
   candidates is the complement of an excluded set, so the operational task is
   not claimed as new.
2. Experimental multi-state elimination is established; for example Webb et
   al., *Physical Review Research* **5**, 023094 (2023), implement exact
   two-out-of-four elimination.  This is adjacent operational evidence, not a
   source of the matroid bound.
3. Zero-error quantum list decoding is direct prior art.  Dalai, Girardi, and
   Lami, arXiv:2601.09786v2 (2026), study pure-state classical--quantum
   channels and include list-size-two/trine behavior.  The regular-simplex
   fixture is not a novelty claim.
4. Stratton, Hsieh, and Skrzypczyk, *Physical Review A* **110**, L050601
   (2024), derive necessary projector/rank conditions for weak and strong
   k-state exclusion.  Their subsetwise projector condition is stronger than
   the trace/matroid obstruction used here.
5. Johnston, Russo, and Sikora, *Quantum* **9**, 1622 (2025), give exact
   Gram-matrix criteria and tight bounds for antidistinguishability.  Yao and
   Wang, *Physical Review A* **113**, 022205 (2026), treat group actions;
   Manna and Das Bhowmik, arXiv:2602.15452 (2026), treat higher-order and LOCC
   exclusion.  Nonsufficiency of rank data is not new.
6. Independent transversals of a family of sets/subspaces are governed by
   Rado's theorem: R. Rado, *A theorem on independence relations*, Quarterly
   Journal of Mathematics os-13, 83--89 (1942).
7. Matroid partition/union and the density criterion are classical: J. Edmonds,
   *Minimum partition of a matroid into independent subsets*, Journal of
   Research of the National Bureau of Standards B **69B**, 67--72 (1965), and
   J. Edmonds, *Matroid Partition*, in Mathematics of the Decision Sciences,
   Part I, AMS (1968), 335--345.
8. Independence-polytope rank inequalities and greedy linear optimization are
   classical matroid results (Edmonds, 1970).
9. General process testers and canonical tester normalizations are established
   by Chiribella, D'Ariano, and Perinotti, *Physical Review A* **80**, 022339
   (2009), and the canonical POVM construction is explicit in Sedlak et al.,
   *Physical Review A* **93**, 052323 (2016).
10. General/indefinite-order process discrimination is treated by Bavaresco,
   Murao, and Quintino, *Journal of Mathematical Physics* **63**, 042203
   (2022).
11. Adaptive advantages for channel discrimination, including
    entanglement-breaking examples, are established by Harrow, Hassidim,
    Leung, and Watrous, *Physical Review A* **81**, 032339 (2010).  Binary
    search and membership-query learning are classical; see Angluin,
    *Machine Learning* **2**, 319--342 (1988).
12. The complete-unitary-error-basis one-guess formula used here is
    essentially the optimal approximate dense-coding result of Feng, Duan,
    and Ji, *Physical Review A* **74**, 012310 (2006),
    DOI `10.1103/PhysRevA.74.012310`.  It is rederived for conventions, not
    claimed as a new theorem.

## Searches run on 2026-08-14

The web and arXiv-facing search covered:

- `quantum state list discrimination POVM list decoding exclusion`;
- `matroid state exclusion quantum`;
- `matroid union quantum discrimination`;
- `multiple guess quantum state discrimination`;
- `quantum hypothesis testing set-valued decision list size`;
- `minimum error quantum state exclusion subset output`;
- `general process discrimination list output tester`.
- `adaptive entanglement-breaking channel discrimination exact parallel`;
- `quantum list discrimination adaptive feedback binary prefix channels`;
- `optimal dense coding arbitrary pure entangled state success probability`;
- `unitary error basis list discrimination Schmidt spectrum`.

The search recovered the expected state-exclusion/elimination literature,
quantum list decoding in coding contexts, standard discrimination reviews, and
classical matroid-union sources.  It did not recover the specific statement
that the vector of true-label inclusion probabilities belongs to the union
power of a Rado support matroid, nor the arbitrary-prior maximum-weight cap.

## Defensible novelty boundary

Potentially new as a synthesis:

- the subset inequality `s(A)<=min_C(|A\C|+ell*d(C))`;
- identification of its right side as the rank of `R^(ell)`;
- the maximum-prior-weight union-independent cap for arbitrary priors;
- the support-congestion deficit and exact disappearance threshold;
- extension through canonical compression to general process testers;
- the soft-reward budget and robust core-tail extension.
- the exact all-depth list-valued laminar parallel/adaptive phase, including
  the reduction against arbitrary entangled parallel inputs and adaptive
  quantum memory;
- the UEB list-cap embedding, exact multitime Weyl wiring trichotomy, and the
  fixed-probe intermediate-spectrum nonattainment example.

Not new:

- state exclusion/elimination or list-valued decisions;
- Rado's theorem, matroid union, matroid polytopes, or greedy optimization;
- tester compression itself;
- regular-simplex/trine antidistinguishability as a standalone phenomenon.
- projector feasibility tests and nonsufficiency of rank-only conditions.
- adaptive channel advantage, binary search, or membership queries;
- complete unitary-error bases, dense coding, the Feng--Duan--Ji one-guess
  spectrum law, or Bell discrimination as standalone constructions.

The laminar phase is an exact resource comparison inside a fully specified
dephase--prepare family.  It is not a quantum advantage or a statement about
indefinite causal order.  The UEB section is new only in the narrower
list/multitime synthesis described above.

## Risk

Priority risk is **medium-high**.  The argument is short enough that an equivalent
bound may exist under the language of minimum-cost state exclusion, sparse
decision losses, fractional packing, or antidistinguishability.  Web search is
not a substitute for MathSciNet, zbMATH, Web of Science/Scopus, and a specialist
check.  Safe prose is “we derive” and “to our knowledge”; unsafe prose is
“first”, “unprecedented”, or “complete solution”.
