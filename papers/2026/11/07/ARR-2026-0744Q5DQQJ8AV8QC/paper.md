# The 2-Pebbling Property, Sharp t-Pebbling Numbers, and Graham's Conjecture for Split Graphs

**Author:** Lluis Eriksson  
**AIRR Identifier:** `ARR-2026-0744Q5DQQJ8AV8QC` (v1)  
**Date:** 2026-11-28  
**Repository:** https://github.com/lluiseriksson/split-graph-2pebbling (`v1.0.2`)  

## Abstract

We resolve three open structural questions in graph pebbling for the class of connected split graphs. First, we prove that every connected split graph satisfies Chung's 2-pebbling property (and hence the odd 2-pebbling property), showing that no split graph is a Lemke graph. Second, we establish the sharp diameter-exponential t-pebbling bound pi_t(G) <= pi(G) + 2^{diam(G)}(t - 1) for every connected split graph G and every integer t >= 1, and exhibit infinite families attaining equality in every diameter d in {0, 1, 2, 3} (both non-Class-0 and Class-0 diameter-3 split graphs), alongside the Class-0 diameter-3 family G_{4,4} showing strict sub-maximal gaps pi_t(G_{4,4}) = 8t < pi_1(G_{4,4}) + 8(t - 1) for t >= 2. Third, combining the 2-pebbling property with classical product theorems and a new budget-parameterized cube-lifting lemma for the M-odd 2-pebbling property, we prove Graham's pebbling conjecture pi(G box H) <= pi(G)pi(H) whenever G is any connected split graph and H is any tree, complete graph, hypercube Q_d, complete bipartite graph, or complete multipartite graph. The proofs are completely self-contained and purely combinatorial, resting on an Intra-Clique Move Elimination Lemma that compresses every minimum-length t-pebbling sequence into a layered DAG of depth at most 3, paired with an optimal bipartite parity-flow routing analysis and exact conservation identity. An independent exact Python verification suite stress-tests all 164 connected split graphs on n <= 7 and higher-order extremal constructions.
