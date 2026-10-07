#!/usr/bin/env python3
"""Exact rational replay of the fixed-normalizer joint-residual gate.

Synthetic finite-dimensional systems only. Does not certify Cone source data.
Python standard library; all matrix identities use fractions.Fraction.
Decimal is used only for displaying/checking the Cauchy norm bound.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
import json
import random


def zeros(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


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
    """Exact symmetric elimination, including singular PSD matrices."""
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


def affine_reduction(a, g, v):
    last = len(v[0]) - 1
    out = mul(tr(v), mul(a, v))
    vg = mul(tr(v), g)
    for i in range(last + 1):
        out[i][last] -= vg[i][0]
        out[last][i] -= vg[i][0]
    return out


def reduction(a, g, c, offset, seed):
    n, k = len(a), len(c)
    complement = [row[k:] for row in a[k:]]
    ci = inv(complement)
    pc = c + zeros(n - k, k)
    rhs = mul(a[k:], pc)
    w = c + [[-x for x in row] for row in mul(ci, rhs)]
    ufront = mul(c, offset)
    urhs = add(g[k:], mul(rhs, offset), -1)
    u = ufront + mul(ci, urhs)
    exact_v = [wr + ur for wr, ur in zip(w, u)]
    exact_m = affine_reduction(a, g, exact_v)

    # Add independent complement errors to all seven trial columns.
    rng = random.Random(seed)
    delta = zeros(n, k + 1)
    for i in range(k, n):
        for j in range(k + 1):
            delta[i][j] = F(rng.randint(-3, 3), 10 ** (j + 5))
    trial = add(exact_v, delta)
    trial_m = affine_reduction(a, g, trial)
    residual = mul(a[k:], trial)
    for i in range(n - k):
        residual[i][-1] -= g[k + i][0]
    e = mul(tr(residual), mul(ci, residual))
    assert add(trial_m, exact_m, -1) == e
    assert psd(e)
    rr = mul(tr(residual), residual)
    assert psd(add(rr, e, -1))  # complement floor >= 1

    j = [row[:k] for row in exact_m[:k]]
    beta = [[-row[k]] for row in exact_m[:k]]
    eta = -exact_m[k][k]
    capacity_scalar = mul(tr(g), mul(inv(a), g))[0][0]
    assert eta + mul(tr(beta), mul(inv(j), beta))[0][0] == capacity_scalar
    return dict(m=exact_m, trial_m=trial_m, e=e, j=j,
                beta=beta, k=capacity_scalar, residual=residual)


def quadratic(a, x):
    return mul(tr(x), mul(inv(a), x))[0][0]


def dec(x):
    return D(x.numerator) / D(x.denominator)


def norm(a):
    return dec(sum((v * v for row in a for v in row), F(0))).sqrt()


def paired_quadratic(ae, ao, xe, xo):
    re, ro = inv(ae), inv(ao)
    da, dx = add(ao, ae, -1), add(xo, xe, -1)
    rexo, rexe = mul(re, xo), mul(re, xe)
    roxo, roxe = mul(ro, xo), mul(ro, xe)
    be = norm(da) * norm(roxo) * norm(rexo) + norm(dx) * (norm(rexo) + norm(rexe))
    bo = norm(da) * norm(roxe) * norm(rexe) + norm(dx) * (norm(roxo) + norm(roxe))
    actual = abs(dec(quadratic(ao, xo) - quadratic(ae, xe)))
    assert actual <= min(be, bo) + D('1e-90')
    return min(be, bo)


def run(seed):
    rng = random.Random(seed)
    n, k, old_n = 11, 6, 9
    b = [[F(rng.randint(-3, 3), 7) for _ in range(n)] for _ in range(n)]
    ae = add(mul(tr(b), b), eye(n))
    perturb = [[F(rng.randint(-2, 2), 700) for _ in range(n)] for _ in range(n)]
    bo = add(b, perturb)
    ao = add(mul(tr(bo), bo), eye(n))
    ge = [[F(rng.randint(-3, 3), 23)] for _ in range(n)]
    go = add(ge, [[F(rng.randint(-1, 1), 2300)] for _ in range(n)])
    c = zeros(k, k)
    for i in range(k):
        c[i][i] = F(10 ** (3 * i))
        if i + 1 < k:
            c[i][i + 1] = c[i][i] / 3
    # Congruence makes the protected source scales very small while the
    # fixed normalized matrices remain modest. The complement is unchanged.
    transform = eye(n)
    cinv = inv(c)
    for i in range(k):
        transform[i][:k] = cinv[i]
    ae = mul(tr(transform), mul(ae, transform))
    ao = mul(tr(transform), mul(ao, transform))
    ge = mul(tr(transform), ge)
    go = mul(tr(transform), go)
    offset = [[F(i + 1, 1000)] for i in range(k)]
    sectors = []
    for a, g, tag in ((ae, ge, 0), (ao, go, 1)):
        old = reduction([row[:old_n] for row in a[:old_n]], g[:old_n], c, offset, seed + tag)
        new = reduction(a, g, c, offset, seed + tag + 20)
        diff = add(old['m'], new['m'], -1)
        gram = [row[:k] for row in diff[:k]]
        tau = [[-row[k]] for row in diff[:k]]
        sigma = diff[k][k]
        z = add(old['beta'], tau, -1)
        anext = add(old['j'], gram, -1)
        assert anext == new['j'] and z == new['beta']
        phi = sigma + quadratic(anext, z) - quadratic(old['j'], old['beta'])
        assert phi == new['k'] - old['k']
        trial_diff = add(old['trial_m'], new['trial_m'], -1)
        diff_error = add(trial_diff, diff, -1)
        assert diff_error == add(old['e'], new['e'], -1)
        assert psd(add(old['e'], diff_error, -1))
        assert psd(add(diff_error, new['e']))
        sectors.append(dict(phi=phi, sigma=sigma, a=anext, z=z, j=old['j'], beta=old['beta']))
    e, o = sectors
    with localcontext() as ctx:
        ctx.prec = 110
        bound = abs(dec(o['sigma'] - e['sigma']))
        bound += paired_quadratic(e['a'], o['a'], e['z'], o['z'])
        bound += paired_quadratic(e['j'], o['j'], e['beta'], o['beta'])
        actual = abs(dec(o['phi'] - e['phi']))
        assert actual <= bound + D('1e-90')
        assert paired_quadratic(e['a'], e['a'], e['z'], e['z']) == 0
        return {'seed': seed, 'exact_joint_residual_identity': True,
                'exact_fixed_normalizer_transport': True,
                'exact_difference_loewner_bracket': True,
                'paired_bound_holds': True, 'common_mode_bound': '0',
                'paired_abs_difference': str(actual), 'paired_upper_bound': str(bound)}


def main():
    # v14.145 tau counterexample: simultaneous input errors create a mixed term.
    eps = F(1, 10)
    true_tau = F(1)
    approximate_tau = (1 + eps) ** 2
    old_bound = 2 * eps
    corrected_bound = 2 * eps + eps ** 2
    assert abs(approximate_tau - true_tau) > old_bound
    assert abs(approximate_tau - true_tau) == corrected_bound
    out = {'arithmetic': 'exact rational identities; Decimal norm displays only',
           'guardrail': 'Synthetic replay, not a source-operator outward certificate',
           'normalizer_diagonal_span': '1 to 1e15',
           'tau_mixed_term_counterexample': {'actual_error': '0.21',
               'v14145_bound_without_rounding_or_solve_error': '0.2',
               'corrected_bound': '0.21'},
           'cases': [run(s) for s in (19, 71, 193)]}
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
