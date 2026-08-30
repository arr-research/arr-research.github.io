# A Machine-Verified Bijective Proof of the Rooted Child-Factorial Catalan Identity over Spanning Trees of the Complete Graph

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0001](https://www.ai.vixra.org/abs/2607.0001)  
**First submitted:** 2026-07-02T19:14:41+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0001-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

Let K n+1 be the complete graph on the vertex set {0, 1, ..., n}, and for a spanning tree T of K n+1 , rooted at 0, let c T (v) denote the number of children of the vertex v. We prove the exact identity: the sum, over all spanning trees T of K n+1 , of the product over vertices v of c T (v)! equals n! C n , where C n is the n-th Catalan number. Equivalently, the normalized sum (n+1)((n+1)!) -1 times the weighted tree sum equals C n exactly. The proof is bijective: pairs consisting of a spanning tree together with a linear ordering of every child set are placed in explicit bijection with vertex-labeled plane trees on n+1 nodes whose root carries the label 0. The identity arises as the exact "second-Ursell" normalization constant in the author's audit-first programme on four-dimensional SU(N) Yang-Mills existence and mass gap, where it had been isolated as a named open proposition in a public challenge repository; the present paper is self-contained combinatorics and makes no claim about that programme. The entire proof has been formalized in Lean 4 against a pinned Mathlib snapshot: the headline declarations compile with no sorry, and the kernel's axiom oracle reports exactly [propext, Classical.choice, Quot.sound]. All artifacts, including a pinned continuous-integration replay of the full verification, are public.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0001v1.pdf) — 2026-07-02T19:14:41+00:00
