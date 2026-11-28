"""AST-pure zero-float exact-Q/Z verifier for M7-3:
Universal O(1) Closed-Form Evaluation of z_{w-1}(x), Dual Gap-Closing Optimal BIBD/RBIBD Families,
and Even-t Residual-Degree Refinement for (n, t, w, w-2)-CPECC Codes
(strictly advancing Liu, Zhang, Yu, Zhang, and Ji, arXiv:2611.34386v1).
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import gcd
from typing import Any


def canonical_json_sha256(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def comb2(n: int) -> int:
    if n < 2:
        return 0
    return (n * (n - 1)) // 2


def interval_dist(w: int, q: int, x: int) -> int:
    """Distance from integer x to interval I_q = [q*(w - 2), q*(w - 1)]."""
    lo = q * (w - 2)
    hi = q * (w - 1)
    if x < lo:
        return lo - x
    if x > hi:
        return x - hi
    return 0


def z_closed_form(w: int, x: int) -> int:
    """Theorem 1: Universal exact O(1) closed form for z_{w-1}(x) for ALL w >= 4, x >= 0."""
    if w < 4 or x < 0:
        raise ValueError("require w >= 4 and x >= 0")
    p = x // (w - 1)
    left = x - p * (w - 1)
    right = (p + 1) * (w - 2) - x
    if right < 0:
        right = 0
    return left if left < right else right


def z_direct_definition(w: int, x: int) -> int:
    """Direct minimization min_{q >= 0} dist(x, [q*(w-2), q*(w-1)]) per Liu et al. Eq. (24)."""
    if w < 4 or x < 0:
        raise ValueError("require w >= 4 and x >= 0")
    q_max = x // (w - 2) + 2
    best = interval_dist(w, 0, x)
    for q in range(1, q_max + 1):
        d = interval_dist(w, q, x)
        if d < best:
            best = d
    return best


def verify_z_closed_form_grid(w_min: int = 4, w_max: int = 40, x_max: int = 180) -> dict[str, Any]:
    """Exhaustively certify z_closed_form(w, x) == z_direct_definition(w, x) over grid."""
    if w_min < 4 or w_max < w_min or x_max < 1:
        raise ValueError("invalid grid bounds")
    checked = 0
    mismatches = 0
    zero_count = 0
    positive_count = 0
    for w in range(w_min, w_max + 1):
        for x in range(1, x_max + 1):
            checked += 1
            zc = z_closed_form(w, x)
            zd = z_direct_definition(w, x)
            if zc != zd:
                mismatches += 1
            if zc == 0:
                zero_count += 1
            else:
                positive_count += 1
    return {
        "w_min": w_min,
        "w_max": w_max,
        "x_max": x_max,
        "pairs_checked": checked,
        "mismatches": mismatches,
        "zero_values": zero_count,
        "positive_values": positive_count,
        "exact_match": mismatches == 0,
    }


def liu_frobenius_threshold(w: int) -> int:
    """Liu et al. Theorem 4.12 / 4.15 Frobenius threshold: (w - 3) * floor((w - 2) / 3) - 1."""
    if w < 4:
        raise ValueError("w must be >= 4")
    return (w - 3) * ((w - 2) // 3) - 1


def audit_gap_closing_families(w_min: int = 4, w_max: int = 30) -> dict[str, Any]:
    """Theorem 2: Audit BOTH coprime realizable gap-closing optimal RBIBD/BIBD families inside
    Liu et al.'s open gap w - 3 <= t < (w - 3) * floor((w - 2) / 3) - 1:
      - Family A: t + 1 = ell * (w - 3), 2 <= ell <= floor((w - 1) / 3), gcd(ell, 2w - 5) == 1, (n, 2w - 4, 1)-RBIBD
      - Family B (BRAND-NEW DUAL): t + 1 = ell * w, 1 <= ell <= floor((w - 2) / 3):
          * ell == 1: (n, 2w - 1, 1)-BIBD (no resolvability, no coprimality restriction; enters open gap for ALL w >= 8!)
          * ell >= 2: gcd(ell, 2w - 2) == 1 (odd ell coprime to w - 1), (n, 2w - 1, 1)-RBIBD
    """
    if w_min < 4 or w_max < w_min:
        raise ValueError("invalid w range")
    fam_a_all = []
    fam_a_gap = []
    fam_b_all = []
    fam_b_gap = []
    for w in range(w_min, w_max + 1):
        frob = liu_frobenius_threshold(w)
        # Family A: 2 <= ell <= (w - 1) // 3 AND gcd(ell, 2w - 5) == 1 (so t >= 2w - 7 >= w - 3 and RBIBD congruences compatible!)
        for ell in range(2, (w - 1) // 3 + 1):
            if gcd(ell, 2 * w - 5) != 1:
                continue
            t = ell * (w - 3) - 1
            if t < w - 3:
                continue
            k = 2 * w - 4
            z_val = z_closed_form(w, t + 1)
            lhs_edges = ell * comb2(k)
            rhs_edges = (2 * w - 3) * (t + 1) + z_val
            if z_val != ell or lhs_edges != rhs_edges:
                raise RuntimeError(f"Family A identity failed at w={w}, ell={ell}")
            in_gap = (w - 3 <= t) and (t < frob)
            rec = {
                "family": "A_2w_minus_4",
                "w": w,
                "ell": ell,
                "t": t,
                "block_size_k": k,
                "z_val": z_val,
                "edges_per_codeword": lhs_edges,
                "frobenius_threshold": frob,
                "coprime_verified": True,
                "strictly_inside_open_gap": in_gap,
            }
            fam_a_all.append(rec)
            if in_gap:
                fam_a_gap.append(rec)

        # Family B: 1 <= ell <= (w - 2) // 3, with ell == 1 (BIBD only!) OR gcd(ell, 2w - 2) == 1 (RBIBD!)
        for ell in range(1, (w - 2) // 3 + 1):
            if ell >= 2 and gcd(ell, 2 * w - 2) != 1:
                continue
            t = ell * w - 1
            k = 2 * w - 1
            z_val = z_closed_form(w, t + 1)
            lhs_edges = ell * comb2(k)
            rhs_edges = (2 * w - 3) * (t + 1) + z_val
            if z_val != ell or lhs_edges != rhs_edges:
                raise RuntimeError(f"Family B identity failed at w={w}, ell={ell}")
            in_gap = (w - 3 <= t) and (t < frob)
            rec = {
                "family": "B_2w_minus_1",
                "w": w,
                "ell": ell,
                "t": t,
                "block_size_k": k,
                "z_val": z_val,
                "edges_per_codeword": lhs_edges,
                "frobenius_threshold": frob,
                "coprime_verified": True,
                "strictly_inside_open_gap": in_gap,
                "bibd_only_sufficient": ell == 1,
            }
            fam_b_all.append(rec)
            if in_gap:
                fam_b_gap.append(rec)

    return {
        "w_min": w_min,
        "w_max": w_max,
        "family_A_total": len(fam_a_all),
        "family_A_in_open_gap": len(fam_a_gap),
        "family_A_first_gap_w": fam_a_gap[0]["w"] if fam_a_gap else None,
        "family_B_total": len(fam_b_all),
        "family_B_in_open_gap": len(fam_b_gap),
        "family_B_first_gap_w": fam_b_gap[0]["w"] if fam_b_gap else None,
        "family_A_gap_samples": fam_a_gap[:12],
        "family_B_gap_samples": fam_b_gap[:12],
    }


def build_td_q_plus_1_q_even_t2_code(q: int) -> dict[str, Any]:
    """Theorem 3 Part 2: Explicitly construct TD(q + 1, q) = (w + 2)-GDD of type (w + 1)^(w + 2)
    from AG(2, q) + slope infinity (equivalently PG(2, q) minus one point!) for any odd prime q = w + 1 >= 7!

    Points (n = q * (q + 1)):
      - Groups G_0, ..., G_{q-1} of size q: vertical columns {(x, y) : y in F_q} for each x in F_q
      - Group G_q of size q: slope points {inf_m : m in F_q}
    Blocks (q^2 blocks of size q + 1 = w + 2):
      - For every (m, c) in F_q^2: line {(x, (m*x + c) mod q) : x in F_q} union {inf_m}!
    Codewords (M = q^2 + (q + 1)/2):
      - Each of the q^2 blocks K_{w+2} is a codeword;
      - Pair the q + 1 = w + 2 (even!) groups into (w + 2)/2 paired-clique codewords 2 * K_{w+1}!
    Attains EXACT EQUALITY with Liu et al. Theorem 3.4 bound h_3(q*(q+1), q-1, 2)!
    """
    if q < 7 or q % 2 == 0:
        raise ValueError("q must be an odd prime >= 7")
    for d in range(2, q):
        if d * d > q:
            break
        if q % d == 0:
            raise ValueError(f"q={q} is not prime")
    w = q - 1
    t = 2
    n = q * (q + 1)
    # Groups: G_x = (x*q + y for y in range(q)) for x in 0..q-1; G_q = (q*q + m for m in range(q))
    groups = [tuple(x * q + y for y in range(q)) for x in range(q)]
    groups.append(tuple(q * q + m for m in range(q)))
    blocks: list[tuple[int, ...]] = []
    for m in range(q):
        for c in range(q):
            pts = [x * q + ((m * x + c) % q) for x in range(q)] + [q * q + m]
            blocks.append(tuple(sorted(pts)))

    codewords: list[list[tuple[int, ...]]] = [[blk] for blk in blocks]
    for j in range(0, q + 1, 2):
        codewords.append([groups[j], groups[j + 1]])

    ver = verify_concrete_block_cpecc_code(n, t, w, codewords, exhaustive_hot_sets=(q == 7))
    h3_val = liu_thm34_h3(n, w, t)
    return {
        "q": q,
        "w": w,
        "t": t,
        "n": n,
        "num_blocks": len(blocks),
        "num_paired_group_codewords": (q + 1) // 2,
        "num_codewords": len(codewords),
        "liu_h3": h3_val,
        "attains_exact_h3": len(codewords) == h3_val,
        "verification": ver,
    }


def B_wt(w: int, t: int) -> int:
    """Liu et al. Theorem 3.3 lower bound B(w, t) = C(w + floor(t/2) - 1, 2) + C(w + ceil(t/2), 2)."""
    if w < 4 or t < 1:
        raise ValueError("invalid w, t")
    a = w + (t // 2) - 1
    b = w + ((t + 1) // 2)
    return comb2(a) + comb2(b)


def liu_thm34_h3(n: int, w: int, t: int) -> int:
    """Exact Liu et al. Theorem 3.4 upper bound h_3 for t < w - 3."""
    if n < w + t or t >= w - 3 or t < 1:
        raise ValueError("require n >= w + t and 1 <= t < w - 3")
    k = w + t
    q1 = (n // k) * ((n - 1) // (k - 1))
    # Wait: Johnson bound is floor((n / k) * floor((n - 1) / (k - 1)))!
    # Check exact formula from Liu et al. Theorem 3.4:
    # h_3 = floor(n/(w+t) * floor((n-1)/(w+t-1))) + floor((n*(n-1) - floor(n/(w+t)*floor((n-1)/(w+t-1)))*(w+t)*(w+t-1)) / (2 * B(w, t)))
    # Wait: let's check both integer interpretations carefully!
    j_bound = (n * ((n - 1) // (k - 1))) // k
    rem_edges_2 = n * (n - 1) - j_bound * k * (k - 1)
    if rem_edges_2 < 0:
        rem_edges_2 = 0
    return j_bound + rem_edges_2 // (2 * B_wt(w, t))


def verify_even_t_residual_jump(w: int, r: int) -> dict[str, Any]:
    """Theorem 3: Exact even-t (t = 2r < w - 3) residual-degree jump & optimal GDD attainment!

    For t = 2r (1 <= r, w >= 2r + 4):
      1. B(w, 2r) = (w + r - 1)^2 (exact perfect square!).
      2. If a K_{w+2r}-free codeword graph G with delta(G) >= w - 1 and Property A(2r) has
         Delta(G) <= w + r - 2 (strictly below the 2-clique ceiling w + r - 1),
         then Liu et al.'s Eq. (13) forces:
           n_G >= ceil((2r + 1) * (w + r - 1) / r),
           e(G) >= ceil((w - 1) * n_G / 2)  (and at r = 1, 3*K_w attains n_G = 3w, e(G) = 3*C(w, 2) > w^2!).
      3. For a (w + 2r)-GDD of type (w + r)^u with u = 2m < 2*(w + r - 1):
         - Each block K_{w+2r} is a codeword;
         - Pairing the u = 2m disjoint groups K_{w+r} into m pairs yields m additional codewords (each 2*K_{w+r}!),
         - Total codewords = (u*(u-1)*(w+r)^2)/((w+2r)*(w+2r-1)) + m,
           attaining EXACT EQUALITY with Liu et al. Theorem 3.4 h_3 whenever (w+2r)*(w+2r-1) | u*(u-1)*(w+r)^2
           and u = 2m < 2*(w + r - 1) (because residual edges = 2m * C(w+r, 2) = m*(w+r)*(w+r-1) and
           floor(m*(w+r)/(w+r-1))? Wait: 2*e_res / (2*B) = m*(w+r)*(w+r-1) / (w+r-1)^2 = m*(w+r)/(w+r-1) -> floor = m when m < w+r-1!!).
    """
    t = 2 * r
    if r < 1 or w < t + 4:
        raise ValueError("require r >= 1 and w >= 2r + 4 (so t < w - 3)")
    b_val = B_wt(w, t)
    sq_val = (w + r - 1) * (w + r - 1)
    if b_val != sq_val:
        raise RuntimeError("B(w, 2r) != (w + r - 1)^2")
    n_min = ((2 * r + 1) * (w + r - 1) + r - 1) // r
    # Exact edge lower bound from delta(G) >= w - 1 on >= n_min vertices:
    e_deg_lb = ((w - 1) * n_min + 1) // 2
    # Exact 3*K_w edge count at r = 1
    e_3kw = 3 * comb2(w) if r == 1 else None
    strict_jump_over_B = e_deg_lb > b_val

    # Check exact h_3 attainment condition for (w+2r)-GDD of type (w+r)^u with u = 2m < 2*(w+r-1)
    # Using exact divisibility for (w+2r)-GDD of type g^u (g = w + r):
    #   (1) (u - 1) * g == 0 (mod k - 1), where k = w + 2r
    #   (2) u * (u - 1) * g^2 == 0 (mod k * (k - 1))
    g = w + r
    k = w + 2 * r
    valid_ms = []
    for m in range(1, w + r - 1):
        u = 2 * m
        if ((u - 1) * g) % (k - 1) == 0 and (u * (u - 1) * g * g) % (k * (k - 1)) == 0:
            n_pts = u * g
            num_blocks = (u * (u - 1) * g * g) // (k * (k - 1))
            total_cw = num_blocks + m
            # Compare against exact Johnson + residual bound:
            # Wait: for a GDD, num_blocks = n*(n - g) / (k*(k-1)), while Johnson bound uses floor((n-1)/(k-1)).
            # Check exact residual edges after num_blocks cliques K_k:
            # e_res = u * C(g, 2) = m * g * (g - 1); floor(e_res / B(w, 2r)) = floor(m * (w+r) / (w+r-1)) = m!
            res_div = (m * g * (g - 1)) // b_val
            if res_div != m:
                raise RuntimeError("residual floor mismatch")
            # Also check exact equality with Liu et al. Theorem 3.4 h_3(n_pts, w, t)!
            h3_val = liu_thm34_h3(n_pts, w, t)
            valid_ms.append({
                "m": m,
                "u": u,
                "n": n_pts,
                "gdd_blocks": num_blocks,
                "paired_group_codewords": m,
                "total_codewords": total_cw,
                "liu_h3": h3_val,
                "attains_exact_h3": total_cw == h3_val,
            })

    return {
        "w": w,
        "r": r,
        "t": t,
        "B_w_2r": b_val,
        "perfect_square_verified": b_val == sq_val,
        "residual_n_min": n_min,
        "residual_e_lb": e_deg_lb,
        "threshold_w_strict": 2 * r * r + 2,
        "strict_jump_over_B": strict_jump_over_B,
        "exact_tie_at_boundary": (w == 2 * r * r + 1 and e_deg_lb == b_val),
        "e_3Kw_at_r1": e_3kw,
        "attaining_gdd_instances": valid_ms,
    }


def build_affine_plane_rbibd(p: int) -> dict[str, Any]:
    """Construct the exact affine plane AG(2, p) = (p^2, p, 1)-RBIBD for prime p!
    Points: (x, y) in F_p^2 indexed by x*p + y in {0..p^2 - 1}.
    p + 1 parallel classes:
      - slopes m in {0..p-1}: lines y = m*x + c (c in F_p),
      - vertical class: lines x = c (c in F_p).
    """
    if p < 2:
        raise ValueError("p must be prime >= 2")
    for d in range(2, p):
        if d * d > p:
            break
        if p % d == 0:
            raise ValueError(f"p={p} is not prime")
    n = p * p
    parallel_classes: list[list[tuple[int, ...]]] = []
    for m in range(p):
        pclass = []
        for c in range(p):
            blk = tuple(sorted(x * p + ((m * x + c) % p) for x in range(p)))
            pclass.append(blk)
        parallel_classes.append(pclass)
    vert_class = []
    for c in range(p):
        blk = tuple(sorted(c * p + y for y in range(p)))
        vert_class.append(blk)
    parallel_classes.append(vert_class)
    return {
        "p": p,
        "n": n,
        "block_size": p,
        "num_parallel_classes": p + 1,
        "total_blocks": p * (p + 1),
        "parallel_classes": parallel_classes,
    }


def verify_concrete_block_cpecc_code(
    n: int,
    t: int,
    w: int,
    codewords: list[list[tuple[int, ...]]],
    exhaustive_hot_sets: bool = True,
) -> dict[str, Any]:
    r"""Exhaustively verify all CPECC axioms on a concrete block-union cooling code:
    Each codeword C_i is a union of pairwise disjoint blocks B_{i,1}, ..., B_{i,ell} (cliques K_k),
    representing all w-subsets contained inside any block B_{i,j} of C_i.

    Checks:
      1. Property B(w): every block has size >= w, blocks within each codeword are pairwise disjoint.
      2. Property C(w-2): ANY two blocks from DISTINCT codewords intersect in at most 1 wire
         (guaranteeing pairwise Hamming distance >= 2w - 2 > 2(w - 2) between any two w-weight vectors
         from distinct codewords!).
      3. Property A(t): for EVERY t-subset T of [n] (checked exhaustively when exhaustive_hot_sets=True,
         and proved analytically via pigeonhole sum_j (|B_{i,j}| - (w - 1)) > t!), every codeword C_i
         has at least one block B_{i,j} with |B_{i,j} \ T| >= w!
    """
    if n < w + t or w < 4 or t < 1:
        raise ValueError("invalid parameters")
    # 1. Verify internal disjointness & block sizes + edge count
    all_pairs_seen: set[tuple[int, int]] = set()
    total_edges = 0
    pigeonhole_ok = True
    for cw in codewords:
        used_in_cw: set[int] = set()
        slack_sum = 0
        for blk in cw:
            if len(blk) < w:
                return {"valid": False, "reason": "block smaller than w"}
            for v in blk:
                if v < 0 or v >= n or v in used_in_cw:
                    return {"valid": False, "reason": "invalid or overlapping vertex inside codeword"}
                used_in_cw.add(v)
            slack_sum += len(blk) - (w - 1)
            # Check edge-disjointness across ALL codewords (which is equivalent to pairwise intersection <= 1!)
            for i in range(len(blk)):
                for j in range(i + 1, len(blk)):
                    u, v = (blk[i], blk[j]) if blk[i] < blk[j] else (blk[j], blk[i])
                    if (u, v) in all_pairs_seen:
                        return {"valid": False, "reason": f"pair {(u, v)} covered by two codewords -> violates Property C(w-2)!"}
                    all_pairs_seen.add((u, v))
                    total_edges += 1
        if slack_sum <= t:
            pigeonhole_ok = False

    # Optional exhaustive check of ALL C(n, t) hot-wire sets T
    hot_sets_checked = 0
    if exhaustive_hot_sets:
        for hot in combinations(range(n), t):
            hot_sets_checked += 1
            hot_set = set(hot)
            for cw in codewords:
                ok = False
                for blk in cw:
                    if sum(1 for v in blk if v not in hot_set) >= w:
                        ok = True
                        break
                if not ok:
                    return {"valid": False, "reason": f"hot set {hot} breaks Property A(t)"}

    # Compare against Theorem 4.6 upper bound when t >= w - 3
    thm46_ub = None
    attains_thm46 = None
    if t >= w - 3:
        denom = (2 * w - 3) * (t + 1) + z_closed_form(w, t + 1)
        thm46_ub = comb2(n) // denom
        attains_thm46 = len(codewords) == thm46_ub

    return {
        "valid": pigeonhole_ok,
        "n": n,
        "t": t,
        "w": w,
        "num_codewords": len(codewords),
        "total_edges_covered": total_edges,
        "max_possible_edges": comb2(n),
        "edge_pack_exact": total_edges == comb2(n),
        "pigeonhole_property_A_verified": pigeonhole_ok,
        "exhaustive_hot_sets_checked": hot_sets_checked,
        "thm46_upper_bound": thm46_ub,
        "attains_exact_thm46_optimum": attains_thm46,
    }
