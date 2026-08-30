# Machine-Checked Rooted-Tree Majorants for Polymer Expansions with Holes

**Author:** Lluis Eriksson  
**Original archive:** [ai.vixra:2607.0025](https://www.ai.vixra.org/abs/2607.0025)  
**First submitted:** 2026-07-11T21:28:54+00:00 (source displays no timezone)  
**Latest declared source version:** v1  
**ARR mirror:** [v1 PDF](https://github.com/arr-research/arr-research.github.io/releases/download/AIVIXRA-LATEST-2026-08-30/ai-vixra-2607.0025-v1.pdf)

> Historical import; not assessed under the ARR frontier-model hostile-audit gate.

## Abstract

We present a machine-checked quantitative toolkit for cluster expansions of polymer systems with excluded regions (holes), in the discrete cube geometry of Balaban-Dimock renormalization-group analyses. Five Lean 4 theorems, checked against a pinned Mathlib revision, provide: (i) the identity sum_T prod_v c_T(v)! = n! C_n for child factorials over spanning trees of the complete graph K_(n+1), with the rooted-tree majorant 4^n as corollary; (ii) a marked-root leaf summation for the tree-graph majorant of an Ursell-type expansion with holes, with the moment constant M paid once at the root and closed leaf ratio 4M^2 per additional vertex, together with its Catalan-sharpened form M^(2n+1) C_n (a gain of order n^(3/2) in the n-th coefficient); and (iii) a target-preserving orderwise bound in which the target union itself survives until the modified-metric exponential is extracted. A certified companion (interval arithmetic, 120-bit precision, committed transcript with a committed reproduction witness) tabulates the smallness gate and encloses every derived constant. Non-vacuity is machine-checked: a concrete hole family satisfying every hypothesis is exhibited in Lean, and the two distinct hypothesis sets among the polymer-facing theorems are both instantiated at it with a strictly positive weight. Each claim is labelled with its verification layer: exact (Lean theorem), certified (interval transcript), or paper-level.

## Source version history

- [v1](https://www.ai.vixra.org/pdf/2607.0025v1.pdf) — 2026-07-11T21:28:54+00:00
