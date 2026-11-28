"""
Exact zero-float integer & F_2[X] polynomial verifier for binary irreducible
trinomials T_k(X) = X^{(4^k+2)/3} + X + 1, Fu-Li-Zuo elliptic-curve order
criterion (arXiv:2611.34282v1), modular covering sieves, and power-substitution
infinite families.

Strict AST purity: zero float literals, zero '/', zero '**', zero floating-point
libraries. Every computation uses exact Python integers and bit-packed F_2[X].
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any


def q(num: int, den: int = 1) -> tuple[int, int]:
    """Reduced exact rational pair (num, den) with den > 0."""
    if den == 0:
        raise ZeroDivisionError("Zero denominator")
    if den < 0:
        num = -num
        den = -den
    g = math.gcd(abs(num), den)
    return (num // g, den // g)


def ipow(base: int, exp: int) -> int:
    """Exact integer exponentiation without '**'."""
    if exp < 0:
        raise ValueError("Negative exponent")
    res = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res *= b
        b *= b
        e >>= 1
    return res


def pow_mod(base: int, exp: int, mod: int) -> int:
    """Exact modular exponentiation via binary squaring."""
    if mod <= 0 or exp < 0:
        raise ValueError("Invalid mod or exp")
    if mod == 1:
        return 0
    res = 1
    b = base % mod
    e = exp
    while e > 0:
        if e & 1:
            res = (res * b) % mod
        b = (b * b) % mod
        e >>= 1
    return res


def canonical_json_sha256(obj: Any) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# ---------------------------------------------------------------------------
# Exact bit-packed F_2[X] polynomial arithmetic (100% exact Z bitmasks)
# ---------------------------------------------------------------------------


def poly_deg(a: int) -> int:
    """Degree of a in F_2[X], with deg(0) = -1."""
    return a.bit_length() - 1


def poly_mod(a: int, b: int) -> int:
    """Exact remainder of a mod b in F_2[X]."""
    if b == 0:
        raise ZeroDivisionError("Polynomial division by zero")
    db = b.bit_length() - 1
    while a.bit_length() - 1 >= db:
        a ^= b << ((a.bit_length() - 1) - db)
    return a


def poly_divmod(a: int, b: int) -> tuple[int, int]:
    """Exact quotient and remainder (q, r) of a divided by b in F_2[X]."""
    if b == 0:
        raise ZeroDivisionError("Polynomial division by zero")
    db = b.bit_length() - 1
    quo = 0
    rem = a
    while rem.bit_length() - 1 >= db:
        sh = (rem.bit_length() - 1) - db
        quo ^= 1 << sh
        rem ^= b << sh
    return quo, rem


def poly_mul_mod(a: int, b: int, mod: int) -> int:
    """Exact product (a * b) mod mod in F_2[X]."""
    a = poly_mod(a, mod)
    b = poly_mod(b, mod)
    res = 0
    dm = mod.bit_length() - 1
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        if a.bit_length() - 1 >= dm:
            a ^= mod
        b >>= 1
    return poly_mod(res, mod)


def poly_gcd(a: int, b: int) -> int:
    """Exact GCD in F_2[X]."""
    while b:
        a, b = b, poly_mod(a, b)
    return a


def poly_trinomial(m: int, n: int) -> int:
    """Construct X^m + X^n + 1 in F_2[X] for m > n >= 1."""
    if not (m > n >= 1):
        raise ValueError("Require m > n >= 1")
    return (1 << m) | (1 << n) | 1


def poly_deriv_f2(f: int) -> int:
    """Formal derivative f'(X) in F_2[X]: keeps odd-degree terms shifted down by 1."""
    res = 0
    bit = 1
    tmp = f >> 1
    while tmp:
        if tmp & 1:
            res |= 1 << (bit - 1)
        tmp >>= 2
        bit += 2
    return res


def factorize_int(n: int) -> dict[int, int]:
    """Exact prime factorization of positive integer n via trial division."""
    if n < 1:
        raise ValueError("Require n >= 1")
    fac: dict[int, int] = {}
    x = n
    d = 2
    while d * d <= x:
        while x % d == 0:
            fac[d] = fac.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    return fac


def ddf_factor_degrees(f: int) -> list[list[int]]:
    """
    Distinct-degree factorization of a squarefree polynomial f in F_2[X].
    Returns sorted list of [degree, multiplicity] pairs such that sum(d*c) = deg(f).
    """
    if poly_gcd(f, poly_deriv_f2(f)) != 1:
        raise ValueError("Polynomial is not squarefree over F_2")
    h = f
    x_pow = 2  # X
    degs: list[list[int]] = []
    d = 1
    while poly_deg(h) >= 2 * d:
        x_pow = poly_mul_mod(x_pow, x_pow, h)  # X^{2^d} mod h
        g = poly_gcd(x_pow ^ 2, h)
        gd = poly_deg(g)
        if gd > 0:
            if gd % d != 0:
                raise AssertionError("DDF degree divisibility violated")
            degs.append([d, gd // d])
            h, rem = poly_divmod(h, g)
            if rem != 0:
                raise AssertionError("DDF exact division failed")
            x_pow = poly_mod(x_pow, h) if h > 1 else 0
        d += 1
    if poly_deg(h) > 0:
        degs.append([poly_deg(h), 1])
    return degs


def rabin_is_irreducible(f: int) -> bool:
    """
    Exact Rabin irreducibility test in F_2[X]:
    f (deg m >= 1) is irreducible iff X^{2^m} == X mod f and
    gcd(X^{2^{m/q}} - X, f) == 1 for every prime q | m.
    """
    m = poly_deg(f)
    if m < 1:
        return False
    if m == 1:
        return True
    if (f & 1) == 0:
        return False
    primes = sorted(factorize_int(m).keys())
    exps = sorted({m // p for p in primes})
    cur_exp = 0
    x_pow = 2  # X^{2^0} = X
    for target in exps:
        while cur_exp < target:
            x_pow = poly_mul_mod(x_pow, x_pow, f)
            cur_exp += 1
        if poly_gcd(x_pow ^ 2, f) != 1:
            return False
    while cur_exp < m:
        x_pow = poly_mul_mod(x_pow, x_pow, f)
        cur_exp += 1
    return x_pow == 2


def poly_x_pow_mod(exp: int, f: int) -> int:
    """Compute X^exp mod f in F_2[X] via binary squaring."""
    res = 1
    base = poly_mod(2, f)
    e = exp
    while e > 0:
        if e & 1:
            res = poly_mul_mod(res, base, f)
        base = poly_mul_mod(base, base, f)
        e >>= 1
    return res


def irreducible_poly_order(f: int) -> int:
    """Exact multiplicative order of a root of irreducible f in F_{2^m}^*."""
    m = poly_deg(f)
    if not rabin_is_irreducible(f):
        raise ValueError("Polynomial must be irreducible")
    n_star = (1 << m) - 1
    fac = factorize_int(n_star)
    ord_val = n_star
    for p in sorted(fac.keys()):
        while ord_val % p == 0 and poly_x_pow_mod(ord_val // p, f) == 1:
            ord_val //= p
    return ord_val


# ---------------------------------------------------------------------------
# Deterministic Lucas primality + multiplicative order certificates
# ---------------------------------------------------------------------------


def verify_lucas_primality_and_ord2(M: int) -> dict[str, Any]:
    """
    Deterministically certify primality of M > 2 and compute exact ord_M(2).
    Uses exact trial factorization of M - 1 and verifies a primitive root g
    (preferring g = 2 when possible) by Lucas's theorem:
      g^{M-1} == 1 (mod M) and g^{(M-1)/q} != 1 (mod M) for all prime q | (M-1).
    """
    if M < 3 or M % 2 == 0:
        return {"M": M, "is_prime": False, "smallest_factor": 2 if M % 2 == 0 else None}
    # Check small factors first
    d = 3
    while d * d <= M and d <= 100000:
        if M % d == 0:
            return {"M": M, "is_prime": False, "smallest_factor": d, "cofactor": M // d}
        d += 2
    fac = factorize_int(M - 1)
    # Verify product of prime powers equals M - 1
    prod_check = 1
    for p, e in fac.items():
        # recursively verify each prime factor p is prime (by trial division)
        td = 2
        while td * td <= p:
            if p % td == 0:
                raise AssertionError(f"Non-prime factor {p}")
            td += 1 if td == 2 else 2
        prod_check *= ipow(p, e)
    if prod_check != M - 1:
        raise AssertionError("Factorization product mismatch")

    primes = sorted(fac.keys())
    witness_g = None
    for g in (2, 3, 5, 6, 7, 10, 11, 13, 17, 19, 23, 29, 31):
        if g >= M:
            break
        if pow_mod(g, M - 1, M) != 1:
            return {"M": M, "is_prime": False, "fermat_witness": g}
        if all(pow_mod(g, (M - 1) // p, M) != 1 for p in primes):
            witness_g = g
            break
    if witness_g is None:
        raise RuntimeError(f"Could not find small Lucas witness for {M}")

    # Compute exact ord_M(2)
    ord2 = M - 1
    for p in primes:
        while ord2 % p == 0 and pow_mod(2, ord2 // p, M) == 1:
            ord2 //= p

    lcm_val = math.lcm(ord2, 6)
    return {
        "M": M,
        "is_prime": True,
        "lucas_primitive_root_witness": witness_g,
        "M_minus_1_factorization": [[p, e] for p, e in sorted(fac.items())],
        "ord_M_2": ord2,
        "index_M_minus_1_over_ord2": (M - 1) // ord2,
        "lcm_ord2_6": lcm_val,
        "fu_li_zuo_criterion_holds": lcm_val == M - 1,
        "is_2_primitive_root": ord2 == M - 1,
    }


def verify_tk_certificate(cert_id: str, k: int, run_f2_ddf: bool = False) -> dict[str, Any]:
    """Build exact certificate for T_k(X) = X^{(4^k+2)/3} + X + 1."""
    if k < 1:
        raise ValueError("Require k >= 1")
    q4 = ipow(4, k)
    if (q4 + 2) % 3 != 0:
        raise AssertionError("4^k + 2 must be divisible by 3")
    m = (q4 + 2) // 3
    M = q4 + 3
    lucas = verify_lucas_primality_and_ord2(M)
    out: dict[str, Any] = {
        "cert_id": cert_id,
        "mode": "tk_criterion",
        "k": k,
        "m_degree": m,
        "M_modulus": M,
        "M_mod_6": M % 6,
        "M_mod_8": M % 8,
        "m_mod_8": m % 8,
        "lucas_audit": lucas,
        "predicted_irreducible": bool(lucas.get("fu_li_zuo_criterion_holds", False)),
    }
    if run_f2_ddf:
        f = poly_trinomial(m, 1)
        ddf = ddf_factor_degrees(f)
        deg_sum = sum(d * c for d, c in ddf)
        if deg_sum != m:
            raise AssertionError("DDF degree sum mismatch")
        f2_irred = (len(ddf) == 1 and ddf[0] == [m, 1])
        if f2_irred != out["predicted_irreducible"]:
            raise AssertionError("Fu-Li-Zuo criterion vs F_2[X] DDF mismatch")
        out["f2_ddf_degrees"] = ddf
        out["f2_direct_irreducible"] = f2_irred
        out["f2_matches_criterion"] = True
    return out


def modular_sieve_certificate(cert_id: str, primes: list[int], k_min_check: int = 4) -> dict[str, Any]:
    """
    Compute exact modular covering sieve of composite M_k = 4^k + 3
    for a finite set of odd primes p (with -3 in <4> mod p).
    """
    rules: list[dict[str, Any]] = []
    period = 1
    for p in primes:
        # Find multiplicative order of 4 mod p and first k0 >= 1 with 4^k0 == -3 mod p
        cur = 4 % p
        target = (-3) % p
        k0 = None
        ord4 = None
        for step in range(1, p):
            if cur == target and k0 is None:
                k0 = step
            if cur == 1:
                ord4 = step
                break
            cur = (cur * 4) % p
        if k0 is None or ord4 is None:
            raise ValueError(f"Prime {p} never divides 4^k + 3")
        rules.append({"prime": p, "residue": k0 % ord4, "modulus": ord4})
        period = math.lcm(period, ord4)

    covered = 0
    covered_residues: list[int] = []
    for r in range(period):
        if any(r % rule["modulus"] == rule["residue"] for rule in rules):
            covered += 1
            covered_residues.append(r)

    # Verify explicitly on concrete k in [k_min_check, k_min_check + period - 1]
    verified_composites = 0
    for r in covered_residues:
        k_val = r
        while k_val < k_min_check:
            k_val += period
        M_val = ipow(4, k_val) + 3
        hit_p = [rule["prime"] for rule in rules if M_val % rule["prime"] == 0 and M_val > rule["prime"]]
        if not hit_p:
            raise AssertionError(f"Sieve residue {r} failed at k={k_val}")
        verified_composites += 1

    elim_frac = q(covered, period)
    surv_frac = q(period - covered, period)
    return {
        "cert_id": cert_id,
        "mode": "modular_sieve",
        "primes": primes,
        "rules": rules,
        "lcm_period": period,
        "covered_count": covered,
        "eliminated_density_exact": list(elim_frac),
        "surviving_density_exact": list(surv_frac),
        "verified_composite_instances": verified_composites,
    }


def power_substitution_certificate(
    cert_id: str, deg_seed: int, mid_seed: int, sub_primes: list[int], exponent_tuples: list[list[int]]
) -> dict[str, Any]:
    """
    Certify Fu-Li-Zuo Main Theorem B (power substitution composition criterion)
    for seed trinomial f(X) = X^D + X^R + 1 over F_2[X]:
    For each prime l in sub_primes, verify l | e and l does not divide (2^D - 1)/e,
    where e = ord(f), guaranteeing f(X^t) is irreducible for every product t of powers
    of primes in sub_primes; then directly verify Rabin irreducibility on all
    requested exponent_tuples!
    """
    seed = poly_trinomial(deg_seed, mid_seed)
    if not rabin_is_irreducible(seed):
        raise ValueError("Seed trinomial is not irreducible")
    e_ord = irreducible_poly_order(seed)
    group_size = (1 << deg_seed) - 1
    index_val = group_size // e_ord
    admissible_audit = []
    for ell in sub_primes:
        cond1 = (e_ord % ell == 0)
        cond2 = (index_val % ell != 0)
        cond3 = (ell != 2)
        if not (cond1 and cond2 and cond3):
            raise ValueError(f"Prime {ell} fails composition criterion for seed ({deg_seed},{mid_seed})")
        admissible_audit.append(
            {
                "prime": ell,
                "divides_order": cond1,
                "coprime_to_index": cond2,
                "admissible_infinite_tower": True,
            }
        )

    members = []
    for exps in exponent_tuples:
        t = 1
        for ell, a in zip(sub_primes, exps):
            t *= ipow(ell, a)
        m_sub = deg_seed * t
        n_sub = mid_seed * t
        f_sub = poly_trinomial(m_sub, n_sub)
        irred = rabin_is_irreducible(f_sub)
        if not irred:
            raise AssertionError(f"Substituted trinomial X^{m_sub}+X^{n_sub}+1 unexpectedly reducible")
        members.append(
            {
                "exponents": exps,
                "multiplier_t": t,
                "degree": m_sub,
                "mid_exponent": n_sub,
                "rabin_irreducible": True,
            }
        )

    return {
        "cert_id": cert_id,
        "mode": "power_substitution_family",
        "seed_degree": deg_seed,
        "seed_mid": mid_seed,
        "seed_order_e": e_ord,
        "seed_index": index_val,
        "admissible_primes": admissible_audit,
        "certified_members": members,
    }
