# Priority audit

## Primary collision set

The following sources are mandatory comparisons, not optional background.

1. N. Johnston, B. Lovitz, V. Russo, and J. Sikora, *The Complexity of
   Perfect Quantum State Classification*, arXiv:2510.20789 (2025).  It defines
   `k`-learnability as exactly the present perfect candidate-list task and
   proves that learning width equals Gram-matrix factor width.  This is the
   direct general feasibility criterion and is not claimed new here.
2. N. Johnston, S. Moein, and S. Plosker, *The Factor Width Rank of a Matrix*,
   arXiv:2405.11556v2 (2025), studies the minimum number of sparse rank-one
   terms in a factor-width decomposition.  Together with conic
   Caratheodory, it makes the present `r^2` outcome compression a standard
   corollary rather than a novelty claim.  The finite nullspace-elimination
   routine supplied here is a constructive implementation, not a new bound.
3. S. Bandyopadhyay, R. Jain, J. Oppenheim, and C. Perry, *Conclusive
   Exclusion of Quantum States*, Phys. Rev. A 89, 022336 (2014).  It formulates
   exclusion of arbitrary subsets as an SDP.  The task itself and the
   multi-state-exclusion reduction are prior art.
4. N. Johnston, V. Russo, and J. Sikora, *Tight bounds for
   antidistinguishability and circulant sets of pure quantum states*, Quantum
   9, 1622 (2025).  It gives Gram-matrix and circulant criteria for excluding
   one state.
5. A. Diebra, S. Llorens, E. Bagan, G. Sentis, and R. Munoz-Tapia, *Quantum
   state exclusion for group-generated ensembles of pure states*, Physical
   Review Research 8, L012001 (2026), DOI 10.1103/2k5d-bprn.  It solves the
   one-state group-orbit problem, not the retained-list threshold here.
6. E. Stratton, C.-Y. Hsieh, and P. Skrzypczyk, *Operational interpretation
   of the Choi rank through exclusion tasks*, Phys. Rev. A 110, L050601
   (2024).  Its projector inequality is explicitly separated from the new
   threshold.
7. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, J. Fourier
   Anal. Appl. 18, 1167--1194 (2012), arXiv:1110.3548.  Full-spark and harmonic
   frame facts are prior.
8. G. Ivanov, *Tight frames and related geometric problems*,
   arXiv:1804.10055.  The fact that cross products of a tight frame form a
   tight frame is close to the exterior identity and must be credited.
9. M. Dalai, F. Girardi, and L. Lami, arXiv:2601.09786v2 (2026), on
   asymptotic zero-error list capacity for classical--quantum channels.  Its
   block-length capacity problem is distinct from the one-shot fixed-codebook
   feasibility law here.
10. J. Crickmore et al., Phys. Rev. Research 2, 013256 (2020), DOI
   10.1103/PhysRevResearch.2.013256, and J. W. Webb et al., Phys. Rev.
   Research 5, 023094 (2023), DOI 10.1103/PhysRevResearch.5.023094, give the
   theory and optical realization of two-out-of-four state elimination.
11. S. Mozes, J. Oppenheim, and B. Reznik, Phys. Rev. A 71, 012311 (2005),
   and S. Wu et al., Phys. Rev. A 73, 042311 (2006), establish that
   deterministic dense-coding performance depends on the detailed partially
   entangled probe, not merely its Schmidt rank.
12. G. Kutyniok, K. A. Okoudjou, F. Philipp, and E. K. Tuley, *Scalable
    Frames*, Linear Algebra Appl. 438, 2225--2238 (2013), DOI
    10.1016/j.laa.2012.10.046, introduces and characterizes positive/strict
    frame scalability.  Scalability itself is therefore classical; the claim
    here is its use with full spark and the weighted Hodge decoder to close
    the quantum-list threshold.
13. Y. C. Eldar and G. D. Forney, Jr., *On Quantum Detection and the
    Square-Root Measurement*, IEEE Trans. Inf. Theory 47, 858--872 (2001),
    DOI 10.1109/18.915636, proves optimal square-root measurements for
    geometrically uniform pure-state ensembles.  Covariant state
    discrimination is used, not claimed new; the target here is the
    list-valued regular-polygon curve.
14. A. S. Holevo, *Statistical Decision Theory for Quantum Systems* (1973),
    and H. P. Yuen, R. S. Kennedy, and M. Lax, *Optimum Testing of Multiple
    Hypotheses in Quantum Detection Theory* (1975), supply the standard
    decision-SDP background for the scalar smallest-eigenvalue witness.

## Search result and novelty boundary

The earlier audit omitted arXiv:2510.20789; that omission is corrected here.
Consequently neither the cone/factor criterion nor the notion of learning
width is part of the novelty claim.  Targeted searches for `full spark tight
frame antidistinguishability`,
`strictly scalable full spark quantum state exclusion`, `exterior power tight
frame state exclusion`, and `quantum list decoding full spark` did not surface
the exact evaluation `N-r+1`, its weighted Hodge POVM, or the global
divisor-branch Weyl optimum `d/r`, or the closed rank-two list curve.  This is
evidence only, not a priority proof.  The 2014 exclusion SDP is general enough
to contain the problem formally, while the 2025 group/circulant papers may
contain special cases not visible in abstracts.

The defensible novelty target is therefore narrow:

```text
the exact learning-width evaluation for strictly scalable full-spark ray
ensembles, its weighted exterior-power decoder, the consecutive-support Weyl
frontier, the globally optimized divisor-branch value d/r, and the exact
rank-two Weyl Bayes curve.
```

Factor width, the general feasibility criterion, and no individual classical
ingredient should be advertised as new.

## Audit conclusion

The primary sources above were inspected at theorem/scope level, and targeted
exact-phrase and formula searches were run for the threshold, the Hodge POVM,
and the Weyl frontier.  No exact collision was located.  This is a scoped
priority audit, not an exhaustive proof of novelty.  The manuscript therefore
uses `we prove`, explicitly credits every classical ingredient, and makes no
`first` claim.
