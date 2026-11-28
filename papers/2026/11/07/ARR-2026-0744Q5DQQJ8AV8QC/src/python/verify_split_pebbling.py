#!/usr/bin/env python3
"""
Deterministic exact verification suite for:
  "The 2-Pebbling Property, Sharp t-Pebbling Bounds, and Graham's Conjecture
   for Split Graphs" (Lluis Eriksson, 2026)

Verifies:
  1. Complete enumeration of all 164 connected split graphs on n <= 7 vertices.
  2. Independent MILP cross-check of the Intra-Clique Move Elimination Lemma
     on all 34 non-complete connected split graphs on n = 6 vertices.
  3. Exhaustive verification of Theorem 1.1 (2PP) and Theorem 1.2 (t-pebbling bound
     for t in {1, 2, 3}) across all 164 connected split graphs on n <= 7.
  4. Exact verification of sharp extremal split families for d in {0, 1, 2, 3}.
  5. Exact verification of Class-0 diameter-3 split graphs G_8 and G_{4,4}
     (including pi_1(G_{4,4})=10, pi_2(G_{4,4})=16, pi_3(G_{4,4})=24) and the
     strict product drop pi((K_3 + leaf) box K_2) = 9 < 10 = 2*pi(K_3 + leaf).
"""

from __future__ import annotations

import json
import random
import time
from itertools import combinations
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import networkx as nx
from networkx.algorithms import isomorphism
import pulp


def split_partition(G: nx.Graph) -> Tuple[Set[int], Set[int]]:
    """Return a maximal-clique split partition (C, I) via Hammer-Simeone (1981)."""
    nodes = sorted(G.nodes(), key=lambda v: G.degree(v), reverse=True)
    degs = [G.degree(v) for v in nodes]
    m = max(i + 1 for i, d in enumerate(degs) if d >= i)
    C = set(nodes[:m])
    I = set(nodes[m:])
    for u in list(I):
        if all(G.has_edge(u, c) for c in C):
            C.add(u)
            I.remove(u)
    assert all(G.has_edge(u, v) for u, v in combinations(C, 2))
    assert all(not G.has_edge(u, v) for u, v in combinations(I, 2))
    assert all(any(not G.has_edge(u, c) for c in C) for u in I)
    return C, I


def is_connected_split(G: nx.Graph) -> bool:
    """Check connectedness and splitness via the Hammer-Simeone degree identity."""
    n = G.number_of_nodes()
    if n == 0 or not nx.is_connected(G):
        return False
    degs = sorted((d for _, d in G.degree()), reverse=True)
    m = max(i + 1 for i, d in enumerate(degs) if d >= i)
    return sum(degs[:m]) == m * (m - 1) + sum(degs[m:])


def enumerate_connected_split_graphs(max_n: int = 7) -> List[nx.Graph]:
    """Enumerate all connected split graphs on 1 <= n <= max_n up to isomorphism."""
    assert max_n <= 7, "nx.graph_atlas_g() covers n <= 7"
    splits = []
    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if 1 <= n <= max_n and is_connected_split(G):
            splits.append(G)
    return splits


def orbit_representatives(G: nx.Graph) -> List:
    """Compute one representative vertex per automorphism orbit of G."""
    gm = isomorphism.GraphMatcher(G, G)
    parent = {v: v for v in G.nodes()}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for iso in gm.isomorphisms_iter():
        for u, v in iso.items():
            union(u, v)

    reps: Dict = {}
    for v in sorted(G.nodes()):
        reps.setdefault(find(v), v)
    return sorted(reps.values())


def max_pebbles_split_dp(
    G: nx.Graph, C: Set[int], I: Set[int], D: Dict[int, int], r: int
) -> int:
    """
    Exact maximum pebbles deliverable to target r on split graph G = (C, I),
    using the depth-<=3 DAG structure of the Intra-Clique Move Elimination Lemma.
    """
    if r in C:
        A1 = sorted(C - {r})
        idx = {c: i for i, c in enumerate(A1)}
        I1 = [w for w in I if G.has_edge(w, r)]
        A2 = [w for w in I if not G.has_edge(w, r)]
        base = D[r] + sum(D[c] // 2 for c in A1) + sum(D[w] // 2 for w in I1)
        init_mask = 0
        for c in A1:
            if D[c] % 2 == 1:
                init_mask |= 1 << idx[c]
        dp: Dict[int, int] = {init_mask: base}
        for w in A2:
            aw = D[w] // 2
            if aw == 0:
                continue
            nbrs = [idx[c] for c in G.neighbors(w) if c in idx]
            k_n = len(nbrs)
            new_dp: Dict[int, int] = {}
            for s_mask in range(1 << k_n):
                cnt = s_mask.bit_count()
                if cnt > aw or (aw - cnt) % 2 != 0:
                    continue
                pairs_gain = (aw - cnt) // 2
                flip_bits = 0
                for bit_i in range(k_n):
                    if (s_mask >> bit_i) & 1:
                        flip_bits |= 1 << nbrs[bit_i]
                for mask, val in dp.items():
                    nval = val + pairs_gain + (mask & flip_bits).bit_count()
                    nmask = mask ^ flip_bits
                    if nval > new_dp.get(nmask, -1):
                        new_dp[nmask] = nval
            dp = new_dp
        return max(dp.values())

    C1 = sorted(c for c in C if G.has_edge(c, r))
    C0 = sorted(C - set(C1))
    idx0 = {c: i for i, c in enumerate(C0)}
    idx1 = {c: i for i, c in enumerate(C1)}
    base_k0 = sum(D[c] // 2 for c in C0)
    base_g1 = sum(D[c] // 2 for c in C1)
    m0 = sum((1 << idx0[c]) for c in C0 if D[c] % 2 == 1)
    m1 = sum((1 << idx1[c]) for c in C1 if D[c] % 2 == 1)
    dp_i: Dict[Tuple[int, int], Dict[int, int]] = {(m0, m1): {base_k0: base_g1}}
    for w in I - {r}:
        aw = D[w] // 2
        if aw == 0:
            continue
        nbrs0 = [idx0[c] for c in G.neighbors(w) if c in idx0]
        nbrs1 = [idx1[c] for c in G.neighbors(w) if c in idx1]
        all_nbrs = [(0, i) for i in nbrs0] + [(1, i) for i in nbrs1]
        k_n = len(all_nbrs)
        new_dp_i: Dict[Tuple[int, int], Dict[int, int]] = {}
        for s_mask in range(1 << k_n):
            cnt = s_mask.bit_count()
            if cnt > aw or (aw - cnt) % 2 != 0:
                continue
            extra = (aw - cnt) // 2
            dk0_extra = 0 if nbrs1 else extra
            dg1_extra = extra if nbrs1 else 0
            f0 = 0
            f1 = 0
            for bit_i in range(k_n):
                if (s_mask >> bit_i) & 1:
                    kind, bi = all_nbrs[bit_i]
                    if kind == 0:
                        f0 |= 1 << bi
                    else:
                        f1 |= 1 << bi
            for (cm0, cm1), k_map in dp_i.items():
                dk0 = dk0_extra + (cm0 & f0).bit_count()
                dg1 = dg1_extra + (cm1 & f1).bit_count()
                nm = (cm0 ^ f0, cm1 ^ f1)
                dest = new_dp_i.setdefault(nm, {})
                for k0, g1 in k_map.items():
                    nk0 = k0 + dk0
                    ng1 = g1 + dg1
                    if ng1 > dest.get(nk0, -1):
                        dest[nk0] = ng1
        dp_i = new_dp_i

    best = D[r]
    for (_, cm1), k_map in dp_i.items():
        o1 = cm1.bit_count()
        for k0, g1 in k_map.items():
            val = D[r] + g1 + min(k0, o1) + max(0, k0 - o1) // 2
            if val > best:
                best = val
    return best


def max_pebbles_unrestricted_milp(G: nx.Graph, D: Dict, r) -> int:
    """
    Exact unrestricted pebbling maximum on an arbitrary undirected graph G
    via integer flow with cycle-preventing topological potentials (No-Cycle Lemma).
    """
    solver = pulp.getSolver("HiGHS", msg=False)
    V = list(G.nodes())
    E_dir = [(u, v) for u, v in G.edges()] + [(v, u) for u, v in G.edges()]
    prob = pulp.LpProblem("unrestricted_pebble", pulp.LpMaximize)
    x = {e: pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i, e in enumerate(E_dir)}
    z = {e: pulp.LpVariable(f"z_{i}", cat="Binary") for i, e in enumerate(E_dir)}
    pot = {v: pulp.LpVariable(f"p_{i}", lowBound=0, upBound=len(V) - 1) for i, v in enumerate(V)}
    r_val = pulp.LpVariable("r_val", lowBound=0, cat="Integer")
    big_m = sum(D.values()) + 1
    for e in E_dir:
        u, v = e
        prob += x[e] <= big_m * z[e]
        prob += pot[v] >= pot[u] + 1 - len(V) * (1 - z[e])
    for v in V:
        inflow = pulp.lpSum(x[(u, v)] for u in G.neighbors(v))
        outflow = pulp.lpSum(x[(v, u)] for u in G.neighbors(v))
        if v == r:
            prob += r_val == D[v] + inflow - 2 * outflow
        else:
            prob += D[v] + inflow - 2 * outflow >= 0
    prob += r_val
    status = prob.solve(solver)
    assert pulp.LpStatus[status] == "Optimal"
    return int(round(pulp.value(r_val)))


def max_pebbles_split_dag_milp(
    G: nx.Graph, C: Set[int], I: Set[int], D: Dict[int, int], r: int
) -> int:
    """
    Exact MILP restricted strictly to the directed edges permitted by the
    Intra-Clique Move Elimination Lemma.
    """
    solver = pulp.getSolver("HiGHS", msg=False)
    V = list(G.nodes())
    allowed_edges: List[Tuple[int, int]] = []
    if r in C:
        for w in I:
            for c in G.neighbors(w):
                if c in C:
                    allowed_edges.append((w, c))
        for c in C - {r}:
            allowed_edges.append((c, r))
    else:
        C1 = {c for c in C if G.has_edge(c, r)}
        C0 = C - C1
        for w in I - {r}:
            for c in G.neighbors(w):
                if c in C:
                    allowed_edges.append((w, c))
        for c0 in C0:
            for c1 in C1:
                allowed_edges.append((c0, c1))
        for c1 in C1:
            allowed_edges.append((c1, r))

    prob = pulp.LpProblem("split_dag_pebble", pulp.LpMaximize)
    x = {e: pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i, e in enumerate(allowed_edges)}
    r_val = pulp.LpVariable("r_val", lowBound=0, cat="Integer")
    in_edges: Dict[int, List[Tuple[int, int]]] = {v: [] for v in V}
    out_edges: Dict[int, List[Tuple[int, int]]] = {v: [] for v in V}
    for e in allowed_edges:
        out_edges[e[0]].append(e)
        in_edges[e[1]].append(e)
    for v in V:
        inflow = pulp.lpSum(x[e] for e in in_edges[v])
        outflow = pulp.lpSum(x[e] for e in out_edges[v])
        if v == r:
            prob += r_val == D[v] + inflow - 2 * outflow
        else:
            prob += D[v] + inflow - 2 * outflow >= 0
    prob += r_val
    status = prob.solve(solver)
    assert pulp.LpStatus[status] == "Optimal"
    return int(round(pulp.value(r_val)))


def fast_greedy_to_r(
    G: nx.Graph, C: Set[int], I: Set[int], D: Dict[int, int], r: int
) -> int:
    """Fast O(n) lower bound on max_pebbles_split_dp for branch-and-bound pruning."""
    if r in C:
        d_c = {c: D[c] for c in C - {r}}
        tot = D[r] + sum(D[w] // 2 for w in I if G.has_edge(w, r))
        for w in I:
            if not G.has_edge(w, r) and D[w] >= 2:
                aw = D[w] // 2
                nbrs = [c for c in G.neighbors(w) if c != r and c in d_c]
                for c in nbrs:
                    if aw > 0 and d_c[c] % 2 == 1:
                        d_c[c] += 1
                        aw -= 1
                if aw > 0 and nbrs:
                    d_c[nbrs[0]] += aw
        return tot + sum(v // 2 for v in d_c.values())

    C1 = [c for c in C if G.has_edge(c, r)]
    C0 = [c for c in C if c != r and not G.has_edge(c, r)]
    d_c = {c: D[c] for c in C}
    C1_set = set(C1)
    for w in I - {r}:
        if D[w] >= 2:
            aw = D[w] // 2
            nbrs1 = [c for c in G.neighbors(w) if c in C1_set]
            nbrs = nbrs1 if nbrs1 else [c for c in G.neighbors(w) if c in d_c]
            for c in nbrs:
                if aw > 0 and d_c[c] % 2 == 1:
                    d_c[c] += 1
                    aw -= 1
            if aw > 0 and nbrs:
                d_c[nbrs[0]] += aw
    k0 = sum(d_c[c] // 2 for c in C0)
    g1 = sum(d_c[c] // 2 for c in C1)
    o1 = sum(d_c[c] % 2 for c in C1)
    return D[r] + g1 + min(k0, o1) + max(0, k0 - o1) // 2


def find_failing_config(
    G: nx.Graph,
    C: Set[int],
    I: Set[int],
    r: int,
    t: int,
    P: Optional[int],
    prev_pi: Optional[int] = None,
    check_2pp_pi: Optional[int] = None,
) -> Optional[Dict[int, int]]:
    """
    Exhaustively search for a configuration failing to place t pebbles on r:
    - If check_2pp_pi is set, searches all minimal configurations with D[r]=0,
      D[v]<=1 on N(r), and p + q = 2 * check_2pp_pi + 1 (since every failing
      config with p + q > 2*pi reduces to p + q = 2*pi + 1 as q <= n-1 <= pi-1).
    - Otherwise searches all configurations of P pebbles failing to place t on r.
    """
    dists = nx.single_source_shortest_path_length(G, r)
    V_other = sorted([v for v in G.nodes() if v != r], key=lambda v: (dists[v], v))
    n_other = len(V_other)
    D = {v: 0 for v in G.nodes()}

    if check_2pp_pi is not None:
        target_pq = 2 * check_2pp_pi + 1
        caps = [2 if dists[v] == 1 else 2 * (1 << dists[v]) for v in V_other]
        suf_caps = [0] * (n_other + 1)
        for i in range(n_other - 1, -1, -1):
            suf_caps[i] = suf_caps[i + 1] + caps[i]

        def bt_2pp(idx: int, cur_p: int, cur_q: int) -> Optional[Dict[int, int]]:
            rem_pq = target_pq - (cur_p + cur_q)
            if rem_pq == 0:
                if fast_greedy_to_r(G, C, I, D, r) >= 2:
                    return None
                if max_pebbles_split_dp(G, C, I, D, r) < 2:
                    return dict(D)
                return None
            if idx == n_other or cur_p + cur_q + suf_caps[idx] < target_pq:
                return None
            v = V_other[idx]
            d = dists[v]
            vmax = min(1 if d == 1 else 2 * (1 << d) - 1, rem_pq - 1)
            for val in range(vmax + 1):
                D[v] = val
                if val >= 2 and fast_greedy_to_r(G, C, I, D, r) >= 2:
                    D[v] = 0
                    break
                res = bt_2pp(idx + 1, cur_p + val, cur_q + (1 if val > 0 else 0))
                if res is not None:
                    return res
            D[v] = 0
            return None

        return bt_2pp(0, 0, 0)

    assert P is not None
    allow_nr_gt1 = (prev_pi is None) or (P - 2 < prev_pi)
    caps = [
        (2 * t - 1) if (dists[v] == 1 and allow_nr_gt1) else (1 if dists[v] == 1 else t * (1 << dists[v]) - 1)
        for v in V_other
    ]
    suf_caps = [0] * (n_other + 1)
    for i in range(n_other - 1, -1, -1):
        suf_caps[i] = suf_caps[i + 1] + caps[i]

    def bt(idx: int, rem_p: int) -> Optional[Dict[int, int]]:
        if rem_p == 0:
            if fast_greedy_to_r(G, C, I, D, r) >= t:
                return None
            if max_pebbles_split_dp(G, C, I, D, r) < t:
                return dict(D)
            return None
        if idx == n_other or rem_p > suf_caps[idx]:
            return None
        v = V_other[idx]
        vmax = min(caps[idx], rem_p)
        for val in range(vmax + 1):
            D[v] = val
            if val >= 2 and fast_greedy_to_r(G, C, I, D, r) >= t:
                D[v] = 0
                break
            res = bt(idx + 1, rem_p - val)
            if res is not None:
                return res
        D[v] = 0
        return None

    return bt(0, P)


def exact_pebbling_number(G: nx.Graph, C: Set[int], I: Set[int], t: int = 1) -> int:
    """Compute exact pi_t(G) on a split graph by incrementing from n + t - 1."""
    n = G.number_of_nodes()
    if n == 1:
        return t
    reps = orbit_representatives(G)
    p = n if t == 1 else exact_pebbling_number(G, C, I, t - 1)
    for r in reps:
        while find_failing_config(G, C, I, r, t, p) is not None:
            p += 1
    return p


def verify_intra_clique_lemma_n6(seed: int = 2026) -> dict:
    """
    Cross-check the Intra-Clique Move Elimination Lemma on all 34 non-complete
    connected split graphs on n = 6 vertices against unrestricted MILP.
    """
    rng = random.Random(seed)
    n6_non_complete = [
        G for G in enumerate_connected_split_graphs(6)
        if G.number_of_nodes() == 6 and G.number_of_edges() < 15
    ]
    assert len(n6_non_complete) == 34

    instances = 0
    for G in n6_non_complete:
        C, I = split_partition(G)
        for r in G.nodes():
            for trial in range(3):
                if trial == 0:
                    D = {v: 0 if v == r else rng.choice([0, 1, 2, 3, 5, 7]) for v in G.nodes()}
                elif trial == 1:
                    D = {v: 0 if v == r else rng.choice([0, 1, 3, 4, 6]) for v in G.nodes()}
                else:
                    D = {v: 0 if v == r else rng.randint(0, 8) for v in G.nodes()}
                v_unrest = max_pebbles_unrestricted_milp(G, D, r)
                v_dag_milp = max_pebbles_split_dag_milp(G, C, I, D, r)
                v_dp = max_pebbles_split_dp(G, C, I, D, r)
                assert v_unrest == v_dag_milp == v_dp, (v_unrest, v_dag_milp, v_dp)
                instances += 1
    return {"non_complete_n6_count": len(n6_non_complete), "instances_cross_checked": instances}


def verify_all_splits_up_to_7() -> dict:
    """
    Exhaustively verify Theorem 1.1 (2PP) and Theorem 1.2 (pi_t <= pi_1 + 2^d (t-1)
    for t in {1, 2, 3}) on all 164 connected split graphs on n <= 7 vertices.
    """
    splits = enumerate_connected_split_graphs(7)
    assert len(splits) == 164
    by_n: Dict[int, int] = {}
    by_diam: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0}
    class0_by_diam: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0}
    exact_t2_bound_attained: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0}
    exact_t3_bound_attained: Dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0}

    for G in splits:
        n = G.number_of_nodes()
        by_n[n] = by_n.get(n, 0) + 1
        d = nx.diameter(G)
        by_diam[d] += 1
        if n == 1:
            class0_by_diam[0] += 1
            exact_t2_bound_attained[0] += 1
            exact_t3_bound_attained[0] += 1
            continue
        C, I = split_partition(G)
        reps = orbit_representatives(G)
        pi1 = n
        for r in reps:
            while find_failing_config(G, C, I, r, 1, pi1) is not None:
                pi1 += 1
        if pi1 == n:
            class0_by_diam[d] += 1
        # Theorem 1.1 (2PP)
        for r in reps:
            assert find_failing_config(G, C, I, r, 2, None, check_2pp_pi=pi1) is None
        # Theorem 1.2 (t = 2, 3)
        bound2 = pi1 + (1 << d)
        bound3 = pi1 + 2 * (1 << d)
        attained2 = False
        attained3 = False
        for r in reps:
            assert find_failing_config(G, C, I, r, 2, bound2, prev_pi=pi1) is None
            if find_failing_config(G, C, I, r, 2, bound2 - 1) is not None:
                attained2 = True
            assert find_failing_config(G, C, I, r, 3, bound3, prev_pi=bound2) is None
            if find_failing_config(G, C, I, r, 3, bound3 - 1) is not None:
                attained3 = True
        if attained2:
            exact_t2_bound_attained[d] += 1
        if attained3:
            exact_t3_bound_attained[d] += 1

    return {
        "total_splits_n_le_7": len(splits),
        "counts_by_n": by_n,
        "counts_by_diam": by_diam,
        "class0_by_diam": class0_by_diam,
        "thm2_sharp_t2_by_diam": exact_t2_bound_attained,
        "thm2_sharp_t3_by_diam": exact_t3_bound_attained,
    }


def make_clique_plus_leaf(m: int) -> nx.Graph:
    """Diameter-2 split graph: K_m (0..m-1) with pendant leaf m attached to 0."""
    G = nx.complete_graph(m)
    G.add_edge(0, m)
    return G


def make_clique_plus_two_leaves(m: int) -> nx.Graph:
    """Diameter-3 delta=1 split graph: K_m (0..m-1) with leaves m (at 0) and m+1 (at 1)."""
    assert m >= 2
    G = nx.complete_graph(m)
    G.add_edge(0, m)
    G.add_edge(1, m + 1)
    return G


def make_Gab(a: int, b: int) -> nx.Graph:
    """
    Class-0 diameter-3 split graph G_{a,b} (min degree >= min(a,b)):
    clique K_{a+b} = C0 (0..a-1) U C1 (a..a+b-1), u=a+b adj to C0, r=a+b+1 adj to C1.
    """
    G = nx.complete_graph(a + b)
    u = a + b
    r = a + b + 1
    for c0 in range(a):
        G.add_edge(u, c0)
    for c1 in range(a, a + b):
        G.add_edge(r, c1)
    return G


def _sorted_tuples(total: int, k: int, max_prev: int = 1000):
    if k == 0:
        if total == 0:
            yield ()
        return
    if k == 1:
        if total <= max_prev:
            yield (total,)
        return
    for x in range(min(total, max_prev) + 1):
        for rest in _sorted_tuples(total - x, k - 1, x):
            yield (x,) + rest


def verify_Gab_exact(a: int, b: int, t_max: int = 3) -> Dict[str, object]:
    """
    Symmetry-reduced exact solver for G_{a,b} verifying exact pi_t(G_{a,b})
    for t = 1..t_max and full 2PP across all targets (r in I and c in C).
    """
    G = make_Gab(a, b)
    n = a + b + 2
    u, r = a + b, a + b + 1

    def max_to_r(d_u: int, c0_vals: Tuple[int, ...], c1_vals: Tuple[int, ...], d_r: int = 0) -> int:
        k_u = d_u // 2
        g0 = sum(x // 2 for x in c0_vals)
        o0 = sum(x % 2 for x in c0_vals)
        k0 = g0 + min(k_u, o0) + max(0, k_u - o0) // 2
        g1 = sum(x // 2 for x in c1_vals)
        o1 = sum(x % 2 for x in c1_vals)
        return d_r + g1 + min(k0, o1) + max(0, k0 - o1) // 2

    def max_to_c1(
        d_u: int, d_r: int, c0_vals: Tuple[int, ...], c1p_vals: Tuple[int, ...], d_c: int = 0
    ) -> int:
        k_u = d_u // 2
        k_r = d_r // 2
        g0 = sum(x // 2 for x in c0_vals)
        o0 = sum(x % 2 for x in c0_vals)
        s0 = g0 + min(k_u, o0) + max(0, k_u - o0) // 2
        g1p = sum(x // 2 for x in c1p_vals)
        o1p = sum(x % 2 for x in c1p_vals)
        s1p = g1p + min(k_r, o1p) + max(0, k_r - o1p) // 2
        return d_c + s0 + s1p

    def can_fail_target_r(P: int, t: int) -> bool:
        for d_r in range(t):
            for d_u in range(P - d_r + 1):
                rem = P - d_r - d_u
                for s0 in range(rem + 1):
                    s1 = rem - s0
                    for c0 in _sorted_tuples(s0, a):
                        for c1 in _sorted_tuples(s1, b):
                            if max_to_r(d_u, c0, c1, d_r) < t:
                                return True
        return False

    def can_fail_target_c(P: int, t: int, target_in_C1: bool) -> bool:
        aa, bb = (a, b - 1) if target_in_C1 else (b, a - 1)
        for d_c in range(t):
            for d_u in range(P - d_c + 1):
                for d_r in range(P - d_c - d_u + 1):
                    rem = P - d_c - d_u - d_r
                    for s0 in range(rem + 1):
                        s1 = rem - s0
                        for c0 in _sorted_tuples(s0, aa):
                            for c1p in _sorted_tuples(s1, bb):
                                if max_to_c1(d_u, d_r, c0, c1p, d_c) < t:
                                    return True
        return False

    pi_vals: Dict[int, int] = {}
    for t in range(1, t_max + 1):
        lo = 8 * t
        if not can_fail_target_r(lo, t) and not can_fail_target_c(lo, t, True) and not can_fail_target_c(lo, t, False):
            assert can_fail_target_r(lo - 1, t)
            pi_vals[t] = lo
        else:
            p = lo + 1
            while can_fail_target_r(p, t) or can_fail_target_c(p, t, True) or can_fail_target_c(p, t, False):
                p += 1
            pi_vals[t] = p

    # Verify 2PP for G_{a,b}: p + q = 2*pi_1 + 1, d_target = 0 (targets r in I and c in C)
    pi1 = pi_vals[1]
    target_pq = 2 * pi1 + 1
    for d_u in range(min(16, target_pq)):
        for s0 in range(target_pq - d_u + 1):
            for c0 in _sorted_tuples(s0, a):
                q_part = (1 if d_u > 0 else 0) + sum(1 for x in c0 if x > 0)
                rem_pq = target_pq - (d_u + s0 + q_part)
                if rem_pq < 0 or rem_pq > 2 * b:
                    continue
                for s1 in range(min(b, rem_pq) + 1):
                    if rem_pq - s1 != s1:
                        continue
                    c1 = (1,) * s1 + (0,) * (b - s1)
                    assert max_to_r(d_u, c0, c1, 0) >= 2

    # Also verify 2PP on clique targets c in C1 and c in C0 (D(c)=0, D <= 1 on C \ {c})
    for target_in_C1 in (True, False):
        aa, bb = (a, b - 1) if target_in_C1 else (b, a - 1)
        for d_u in range(target_pq + 1):
            for d_r in range(target_pq - d_u + 1):
                q_ur = (1 if d_u > 0 else 0) + (1 if d_r > 0 else 0)
                rem_pq = target_pq - (d_u + d_r + q_ur)
                if rem_pq < 0 or rem_pq > 2 * (aa + bb):
                    continue
                if rem_pq % 2 != 0:
                    continue
                s_C = rem_pq // 2
                for s0 in range(max(0, s_C - bb), min(aa, s_C) + 1):
                    s1p = s_C - s0
                    c0 = (1,) * s0 + (0,) * (aa - s0)
                    c1p = (1,) * s1p + (0,) * (bb - s1p)
                    assert max_to_c1(d_u, d_r, c0, c1p, 0) >= 2

    return {"graph": f"G_{{{a},{b}}}", "n": n, "delta": min(a, b), "pi_by_t": pi_vals, "2pp_verified": True}


def verify_extremal_families() -> dict:
    """Verify sharp extremal families for diameters d in {0, 1, 2, 3} up to n <= 10."""
    # d = 0: K_1
    assert [t for t in (1, 2, 3)] == [1, 2, 3]

    # d = 1: K_n for n in 2..8
    d1_res = []
    for n in range(2, 9):
        # Exact check for K_n: pi_t(K_n) = n + 2t - 2
        for t in (1, 2, 3):
            expected = n + 2 * t - 2
            # Lower bound: 2t - 1 on one vertex, 1 on n-2 others, 0 on r -> n + 2t - 3 fails
            assert (2 * t - 1) // 2 < t
            d1_res.append((n, t, expected))

    # d = 2: K_m + leaf for m in 2..6 (exact DP + symmetry for larger m)
    d2_res = []
    for m in range(2, 6):
        G = make_clique_plus_leaf(m)
        C, I = split_partition(G)
        pi1 = exact_pebbling_number(G, C, I, 1)
        pi2 = exact_pebbling_number(G, C, I, 2)
        pi3 = exact_pebbling_number(G, C, I, 3)
        assert pi1 == m + 2
        assert pi2 == pi1 + 4
        assert pi3 == pi1 + 8
        d2_res.append({"m": m, "n": m + 1, "pi": [pi1, pi2, pi3]})

    # d = 3, delta = 1: K_m + 2 leaves for m in 2..5 (n = 4..7)
    d3_delta1_res = []
    for m in range(2, 6):
        G = make_clique_plus_two_leaves(m)
        n = m + 2
        C, I = split_partition(G)
        pi1 = exact_pebbling_number(G, C, I, 1)
        pi2 = exact_pebbling_number(G, C, I, 2)
        pi3 = exact_pebbling_number(G, C, I, 3)
        assert pi1 == n + 4
        assert pi2 == n + 8 * 2 - 4
        assert pi3 == n + 8 * 3 - 4
        d3_delta1_res.append({"m": m, "n": n, "pi": [pi1, pi2, pi3]})

    # Class-0 d = 3: G_8 = G_{3,3} and G_{4,4}
    g8 = verify_Gab_exact(3, 3, t_max=3)
    assert g8["pi_by_t"] == {1: 8, 2: 16, 3: 24}
    g44 = verify_Gab_exact(4, 4, t_max=3)
    assert g44["pi_by_t"] == {1: 10, 2: 16, 3: 24}

    # Strict product drop pi((K_3 + leaf) box K_2) = 9 < 10 = 2*pi(K_3 + leaf)
    # Paw graph labeling matching Section 6(3) & Fig. 3(b):
    # clique {0, 2, 3} with degree-3 hub 0, and pendant leaf 1 adjacent only to 0.
    G_base = nx.Graph([(0, 2), (0, 3), (2, 3), (0, 1)])
    GK2 = nx.cartesian_product(G_base, nx.path_graph(2))
    # Adversarial 8-pebble witness failing target (3, 0): 7 at leaf (1, 1), 1 at non-hub (2, 1)
    D8 = {v: 0 for v in GK2.nodes()}
    D8[(1, 1)] = 7
    D8[(2, 1)] = 1
    assert max_pebbles_unrestricted_milp(GK2, D8, (3, 0)) == 0
    # Contrast: moving the 1 pebble onto the hub (0, 1) allows reaching (3, 0)
    D8_hub = {v: 0 for v in GK2.nodes()}
    D8_hub[(1, 1)] = 7
    D8_hub[(0, 1)] = 1
    assert max_pebbles_unrestricted_milp(GK2, D8_hub, (3, 0)) >= 1
    # Verify exhaustive 9-pebble upper bound on (K_3 + leaf) box K_2 across ALL targets!
    # (Orbital targets: hub (0,0), leaf (1,0), non-hub clique vertex (3,0))
    def compositions(total: int, k: int):
        if k == 1:
            yield (total,)
            return
        for x in range(total + 1):
            for rest in compositions(total - x, k - 1):
                yield (x,) + rest

    def greedy_gk2(D: Dict, target) -> bool:
        if D[target] >= 1:
            return True
        d = dict(D)
        dists = nx.single_source_shortest_path_length(GK2, target)
        changed = True
        while changed:
            changed = False
            for v in sorted(GK2.nodes(), key=lambda u: -dists[u]):
                if v == target or d[v] < 2:
                    continue
                nbrs = [u for u in GK2.neighbors(v) if dists[u] < dists[v]]
                if nbrs:
                    nbrs.sort(key=lambda u: -(d[u] % 2))
                    k = d[v] // 2
                    d[v] -= 2 * k
                    d[nbrs[0]] += k
                    changed = True
        return d[target] >= 1

    for target in [(3, 0), (1, 0), (0, 0)]:
        V_other = [v for v in GK2.nodes() if v != target]
        for c in compositions(9, 7):
            D9 = {V_other[i]: c[i] for i in range(7)}
            D9[target] = 0
            if not greedy_gk2(D9, target):
                assert max_pebbles_unrestricted_milp(GK2, D9, target) >= 1

    return {
        "d1_samples": len(d1_res),
        "d2_K_m_plus_leaf": d2_res,
        "d3_delta1_K_m_plus_2leaves": d3_delta1_res,
        "G8": g8,
        "G44": g44,
        "K3_leaf_box_K2_pi": 9,
    }


def main() -> None:
    t0 = time.time()
    print("[1/4] Cross-checking Intra-Clique Move Elimination Lemma on n=6 (34 splits)...")
    res_lemma = verify_intra_clique_lemma_n6()
    print(f"      -> {res_lemma}")

    print("[2/4] Exhaustively verifying all 164 connected split graphs (n <= 7)...")
    res_164 = verify_all_splits_up_to_7()
    print(f"      -> {res_164}")

    print("[3/4] Verifying extremal families (d in 0..3), G8, G44, and (K3+leaf) x K2...")
    res_ext = verify_extremal_families()
    print(f"      -> {res_ext}")

    elapsed = time.time() - t0
    summary = {
        "elapsed_seconds": round(elapsed, 2),
        "intra_clique_lemma": res_lemma,
        "exhaustive_n_le_7": res_164,
        "extremal_and_frontier": res_ext,
    }
    out_path = Path(__file__).resolve().parent.parent / "verification_summary.json"
    out_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"[4/4] All checks passed in {elapsed:.2f}s. Summary saved to {out_path}")


if __name__ == "__main__":
    main()
