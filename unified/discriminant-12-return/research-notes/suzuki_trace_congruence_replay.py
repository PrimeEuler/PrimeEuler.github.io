#!/usr/bin/env python3
"""Exact rational trace repair; synthetic identities and frozen midpoint replay.

Only the synthetic checks certify identities. Frozen decimals are exact replay
inputs, not certified enclosures of the large-vector/source calculation.
Python standard library only. Decimal is used for display, never decisions.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random


def zeros(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(r) for r in zip(*a)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def scale(a, s):
    return [[s * x for x in row] for row in a]


def inv(a):
    n = len(a)
    z = [row[:] + ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if z[i][j])
        z[j], z[pivot] = z[pivot], z[j]
        p = z[j][j]
        z[j] = [x / p for x in z[j]]
        for i in range(n):
            if i != j:
                c = z[i][j]
                z[i] = [x - c * y for x, y in zip(z[i], z[j])]
    return [row[n:] for row in z]


def psd(a):
    z = [row[:] for row in a]
    assert z == tr(z)
    for j in range(len(z)):
        p = z[j][j]
        if p < 0:
            return False
        if not p:
            if any(z[i][j] for i in range(j + 1, len(z))):
                return False
            continue
        for i in range(j + 1, len(z)):
            for k in range(j + 1, len(z)):
                z[i][k] -= z[i][j] * z[j][k] / p
    return True


def affine(a, g, v):
    out = mul(tr(v), mul(a, v))
    vg = mul(tr(v), g)
    for i in range(len(out)):
        out[i][-1] -= vg[i][0]
        out[-1][i] -= vg[i][0]
    return out


def residual(a, g, v, k):
    out = mul(a[k:], v)
    for i in range(len(out)):
        out[i][-1] -= g[k + i][0]
    return out


def congruence(m, l):
    return mul(tr(l), mul(m, l))


def capacity(m):
    k = len(m) - 1
    j = [row[:k] for row in m[:k]]
    b = [[row[k]] for row in m[:k]]
    return -m[k][k] + mul(tr(b), mul(inv(j), b))[0][0]


def repair(t, v, defect):
    k = len(t)
    relative = mul(inv(t), defect)
    e = [row[:k] for row in relative]
    s = [[row[k]] for row in relative]
    # Sum of absolute entries is an exact rational upper bound on Frobenius
    # and operator norms; no rounded square root is used to establish rho<1.
    rho = sum((abs(x) for row in relative for x in row), F(0))
    assert rho < 1
    c = inv(add(eye(k), e))
    w = scale(mul(c, s), -1)
    l = [cr + wr for cr, wr in zip(c, w)] + [[F(0)] * k + [F(1)]]
    target = [row + off for row, off in zip(t, mul(t, v))]
    h = add(target, defect)
    assert mul(h, l) == target
    assert l[-1] == eye(k + 1)[-1]
    nu = rho / (1 - rho)
    delta = add(l, eye(k + 1), -1)
    assert psd(add(scale(eye(k + 1), nu * nu), mul(tr(delta), delta), -1))
    return l, rho, nu


def l1(a):
    return sum((abs(x) for row in a for x in row), F(0))


def fro2(a):
    return sum((x * x for row in a for x in row), F(0))


def display(x, root=False):
    with localcontext() as ctx:
        ctx.prec = 50
        y = Decimal(x.numerator) / Decimal(x.denominator)
        return str(y.sqrt() if root else y)


def synthetic(seed):
    rng = random.Random(seed)
    n, k = 11, 6
    b = [[F(rng.randint(-3, 3), 7) for _ in range(n)] for _ in range(n)]
    a = add(mul(tr(b), b), eye(n))
    t = zeros(k, k)
    for i in range(k):
        t[i][i] = F(10 ** (3 * i))
        if i + 1 < k:
            t[i][i + 1] = t[i][i] / 3
    transform = eye(n)
    ti = inv(t)
    for i in range(k):
        transform[i][:k] = ti[i]
    a = congruence(a, transform)
    g = mul(tr(transform), [[F(rng.randint(-3, 3), 23)] for _ in range(n)])
    offset = [[F(i + 1, 1000)] for i in range(k)]
    ci = inv([row[k:] for row in a[k:]])
    rhs = mul(a[k:], t + zeros(n - k, k))
    w = t + scale(mul(ci, rhs), -1)
    u = mul(t, offset) + mul(ci, add(g[k:], mul(rhs, offset), -1))
    stationary = [wr + ur for wr, ur in zip(w, u)]
    relative = [[F(rng.randint(-3, 3), 10000) for _ in range(k + 1)]
                for _ in range(k)]
    defect = mul(t, relative)
    front = add(stationary[:k], defect)
    complement = add(stationary[k:],
                     [[F(rng.randint(-3, 3), 1000) for _ in range(k + 1)]
                      for _ in range(n - k)])
    trial = front + complement
    l, rho, nu = repair(t, offset, defect)
    corrected = mul(trial, l)
    assert corrected[:k] == stationary[:k]
    m = affine(a, g, trial)
    mc = affine(a, g, corrected)
    assert mc == congruence(m, l)
    r = residual(a, g, trial, k)
    rc = residual(a, g, corrected, k)
    assert rc == mul(r, l)
    assert mul(tr(rc), rc) == congruence(mul(tr(r), r), l)
    error = add(mc, affine(a, g, stationary), -1)
    assert error == mul(tr(rc), mul(ci, rc))
    assert psd(error)
    assert capacity(mc) == capacity(m)
    f, s = l1([row[:k] for row in r]), l1([[row[k]] for row in r])
    fc, sc = f / (1 - rho), s + f * nu
    assert fro2([row[:k] for row in rc]) <= fc * fc
    assert fro2([[row[k]] for row in rc]) <= sc * sc
    # Rational upper bounds also check the conservative assembly inflation.
    assembly_error = scale(eye(k + 1), F(1, 10**8))
    mhat = add(m, assembly_error)
    alpha, magnitude = l1(assembly_error), l1(mhat)
    alpha_c = alpha + nu * (2 + nu) * (magnitude + alpha)
    difference = add(mhat, mc, -1)
    assert psd(add(scale(eye(k + 1), alpha_c**2),
                   mul(tr(difference), difference), -1))
    # Bottom-row preservation is essential to the affine congruence claim.
    bad = eye(k + 1)
    bad[-1][-1] = F(2)
    assert affine(a, g, mul(trial, bad)) != congruence(m, bad)
    return {"seed": seed, "all_exact_identities_and_bounds_pass": True,
            "nonpreserving_bottom_row_counterexample": True,
            "relative_defect_l1_cap": display(rho)}


def frozen(path):
    raw = path.read_bytes()
    payload = json.loads(raw)
    normalizer = payload['normalizer']
    t = [[F(x) for x in row] for row in normalizer['T']]
    v = [[F(x)] for x in normalizer['v']]
    row = payload['rows'][0]
    defect = [[F(x) for x in r] for r in row['protected_trace_coefficient_defect_midpoint']]
    l, rho, nu = repair(t, v, defect)
    m = [[F(x) for x in r] for r in row['M_trial_midpoint']]
    gram = [[F(x) for x in r] for r in row['residual_gram_midpoint']]
    mc, gc = congruence(m, l), congruence(gram, l)
    assert mc == tr(mc) and gc == tr(gc)
    assert capacity(mc) == capacity(m)
    digest = json.dumps([[str(x) for x in r] for r in mc], separators=(',', ':'))
    return {"file": path.name, "sha256": hashlib.sha256(raw).hexdigest(),
            "cutoff": row['cutoff'], "sector": row['sector'],
            "serialized_trace_repair_exact": True,
            "serialized_capacity_unchanged_exact": True,
            "relative_defect_l1_cap_midpoint": display(rho),
            "congruence_displacement_cap_midpoint": display(nu),
            "M_congruence_change_fro_midpoint": display(fro2(add(mc, m, -1)), True),
            "residual_gram_congruence_change_fro_midpoint": display(fro2(add(gc, gram, -1)), True),
            "corrected_serialized_M_fraction_sha256": hashlib.sha256(digest.encode()).hexdigest()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--payload-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    cases = [synthetic(s) for s in (19, 71, 193)]
    rows = [frozen(args.payload_root / f'joint-{cutoff}-{sector}.json')
            for cutoff in (64000, 128000) for sector in ('even-v', 'odd-v')]
    result = {"schema": "cone.trace-affine-congruence-replay.v1",
              "arithmetic": "Fraction for all identities and decisions; Decimal display only",
              "passed": True, "synthetic_cases": cases, "frozen_midpoint_rows": rows,
              "guardrail": "No outward trace/source/assembly/residual cap inferred from midpoint decimals; original frozen files unchanged."}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
