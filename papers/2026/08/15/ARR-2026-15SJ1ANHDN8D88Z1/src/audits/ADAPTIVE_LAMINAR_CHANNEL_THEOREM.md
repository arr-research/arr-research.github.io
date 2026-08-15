# Exact adaptive--parallel list separation for laminar query channels

## 1. Deterministic classical channels inside the quantum model

Let `E={1,...,M}` be the hypothesis set, `X` a finite input alphabet, and
`Y` a finite output alphabet.  Hypothesis `i` specifies the entanglement-
breaking channel

```text
N_i(tau)=sum_{x in X} <x|tau|x> |f_i(x)><f_i(x)|,
```

where `f_i:X->Y` is deterministic.  A list decoder may return at most `ell`
labels.

For a deterministic parallel query tuple `x=(x_1,...,x_q)`, write

```text
c_x(i)=(f_i(x_1),...,f_i(x_q)),
C_z(x)={i:c_x(i)=z}.
```

Define, for nonnegative prior weights `w_i`,

```text
B_ell(x;w)=sum_z sum of the ell largest weights in C_z(x),
```

with all weights used if the cell has fewer than `ell` labels.

### Theorem A (exact architecture reduction)

For the channel family above:

1. The optimum of every `q`-use parallel quantum strategy, allowing an
   arbitrary entangled input and reference system, is

   ```text
   P_parallel^(ell)(q)=max_{x in X^q} B_ell(x;p).
   ```

2. The optimum of every causally ordered adaptive quantum strategy obeys the
   exact Bellman recursion

   ```text
   V_0(w)=sum of the ell largest entries of w,
   V_q(w)=max_{x in X} sum_{y in Y} V_{q-1}(w * 1_{f_i(x)=y}),
   P_adapt^(ell)(q)=V_q(p).
   ```

3. For a fixed parallel tuple, the output supports form the partition matroid
   `direct_sum_z U_{1,|C_z|}`.  Its `ell`-fold union has rank

   ```text
   r_ell(E)=sum_z min(ell,|C_z|),
   ```

   and the Bayesian matroid-union cap is exactly `B_ell(x;p)`.  Thus the cap is
   attained cell by cell, rather than merely being an outer relaxation.

### Proof

For deterministic basis inputs, the outputs are the orthogonal classical
states `|c_x(i)>`; within each response cell no measurement can distinguish
the labels, and between cells they are perfectly distinguishable.  Reporting
the `ell` largest-prior labels in every cell proves item 3 and attains
`B_ell`.

For a general parallel input on `X^q tensor R`, each use first measures its
input in the fixed basis.  Adjoin a classical genie flag containing the full
measurement tuple `x`.  Conditional on that flag, the reference state is
independent of the unknown label and the only label dependence is the
deterministic response word `c_x(i)`.  Revealing the flag cannot lower the
success probability, hence the original strategy is bounded by a convex
combination of `B_ell(x;p)`, and therefore by its maximum.  A deterministic
basis tuple attains the maximum.

For a sequential strategy, reveal at every round the measured input symbol as
well as the already classical output.  Conditional on the complete transcript,
the residual quantum memory is fixed by the strategy and is independent of
the label inside the surviving response cell.  Backward induction therefore
reduces the strategy to a randomized classical decision tree.  At each node,
linearity makes an extreme deterministic query optimal.  The terminal value is
the sum of the `ell` largest surviving prior weights, and conditioning on the
next classical output gives the displayed Bellman recursion.  Deterministic
query trees attain every step of the recursion.

The proof covers arbitrary ancillas and coherent controls, but not indefinite-
causal-order process matrices.  It also does not cover coherent unitary oracle
access to `f_i`, inverse queries, or controlled bypass.

## 2. The complete laminar-tree phase diagram

Fix integers `h>=1` and `0<=s<=h`, put

```text
M=2^h, ell=2^s,
E={0,1}^h,
X={binary prefixes v: |v|<h}.
```

For a leaf `u` and prefix `v`, define

```text
f_u(v)=1 iff u begins with v1,
```

and `f_u(v)=0` otherwise.  Thus input `v` asks membership in the right child
of the subtree rooted at `v`.  The queried subsets `A_v={u:f_u(v)=1}` form a
laminar family.

### Theorem B (exact parallel--adaptive phase diagram)

For uniform priors and every number `q>=0` of uses,

```text
P_parallel^(ell)(q)=min(1, ell*(q+1)/M),
P_adapt^(ell)(q)=min(1, ell*2^q/M).
```

Consequently the exact query thresholds for perfect `ell`-list success are

```text
q_parallel^*=M/ell-1=2^(h-s)-1,
q_adapt^*=log_2(M/ell)=h-s.
```

For one-label discrimination this is an exponential separation:
`2^h-1` parallel uses versus `h` adaptive uses.

### Proof: parallel upper bound

Any `q` chosen query sets belong to a laminar family.  A family of `q`
laminar subsets partitions its universe into at most `q+1` nonempty membership
cells: insert the sets one at a time in inclusion order; each new set lies
inside one existing cell and can split only that cell.  By Theorem A, a cell
contributes at most `ell/M` to uniform list success.  Therefore

```text
P_parallel^(ell)(q)<=min(1,ell*(q+1)/M).
```

### Proof: parallel attainment

Let `d=h-s`, so the target cell size is `ell=2^s`.  Query the internal nodes
in breadth-first order through depth `d-1`.  After exactly `2^d-1=M/ell-1`
queries, the membership signatures are precisely the `2^d` length-`d` prefix
blocks, each containing `ell` leaves.  Before saturation, every added right-
child query splits one current block into two blocks, both still containing at
least `ell` leaves.  Hence after `q<=2^d-1` queries there are exactly `q+1`
cells, all of size at least `ell`, so each contributes exactly `ell/M`.

### Proof: adaptive upper bound and attainment

A depth-`q` binary decision tree has at most `2^q` terminal transcripts.  Each
terminal list contains at most `ell` labels, so uniform success is at most
`min(1,ell*2^q/M)`.  Starting at the empty prefix, query the current prefix
`v`.  Because the prior answers certify that the leaf lies below `v`, response
`1` selects child `v1` and response `0` selects child `v0`.  After `q` rounds
there are exactly `2^q` prefix cells of equal size `M/2^q`; reporting any
`ell` labels in the reached cell attains the bound until `q=d`, when the cell
size is `ell` and success becomes one.

## 3. Scope and novelty boundary

- Binary search, laminar set systems, deterministic decision trees, and the
  fact that adaptive membership queries can outperform nonadaptive ones are
  classical and must be credited rather than claimed new.
- The paper-level contribution is the exact quantum-channel reduction against
  arbitrary parallel entanglement and adaptive quantum memory, its exact
  realization by the matroid-union support law, and the closed list-valued
  architecture phase diagram in one family.
- The channels are entanglement-breaking.  The separation is therefore an
  input/adaptivity effect, not a quantum advantage, entanglement advantage,
  causal-order advantage, or memory lower bound for general processes.
- No statement is made for indefinite causal order, coherent phase oracles,
  noisy channels, approximate promises, or asymptotic channel coding.
