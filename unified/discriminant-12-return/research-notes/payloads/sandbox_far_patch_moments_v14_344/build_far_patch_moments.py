#!/usr/bin/env python3
"""Sandbox far-patch moment package (ledger v14.344 handoff).

Finite wider-patch-only far-action moments from the exact v14.341
correction bytes. For outputs n >= N0 (strictly beyond twice the maximum
correction mode), the additive patch action (kernel + pole, diagonal term
zero beyond the support) is

    (D delta_y)_n = c*z_n*sum_j M_j/n^(2j+2) - c*sum_j Z_j/n^(2j+1)
                    + alpha * (L n/(n^2+t)) * P_delta

with M_j = sum_m m^(2j+1) delta_y(m),  Z_j = sum_m zhat_m delta_y(m) m^(2j),
P_delta = sum_m phat_m delta_y(m), zhat/phat the 256-bit floor
representations defined below. K = 42 moments; the geometric remainder is
bounded by the exact identity tail with ratio r0 = (M/N0)^2 < 1/4.

Conventions mirror Lane A's compact Far producer
(suzuki_refined_near_compact_far_action.py): L, t are the 256-bit
enclosure midpoints of 4*atanh(1/5..)-style constants (here ell = log 4
for start==1 / log(9/2)... exactly as in their code via hyperbolic()),
z_m enclosures from suzuki_bulk_action_z.evaluate, represented as
zint_m = floor(zpoint_m, 256) with exact per-mode error
err_m = max(|lo - zint/2^256|, |hi - zint/2^256|).
"""
import argparse, hashlib, json, os, sys, time
from pathlib import Path
from fractions import Fraction as F

sys.path.insert(0, '/home/hatch/workspace/d12/laneA_modules')
from suzuki_bulk_action_z import evaluate as z_eval
from suzuki_frozen_trial_far_outward import (atan_recip, hyperbolic, add,
                                             times, neg, constant, recip,
                                             enclose)
from suzuki_certified_remote_z import enclosure, midpoint, radius
from suzuki_near_trial_lift_rhs import floor as floor_bits

ROOT = Path('/home/hatch/workspace/d12/farpatch344')
CAND = Path('/home/hatch/workspace/d12/wider339/out')
K = 42
CASES = {
    'even-v': dict(start=1, first=512001, last=1040383, N0=2080767,
                   cand_sha='fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05'),
    'odd-v': dict(start=2, first=512002, last=1040384, N0=2080768,
                  cand_sha='b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967'),
}
C_RATIONAL = F(13864350910074216710003485116231801335863,
               21778071482940061661655974875633165533184)
ALPHA = {'even-v': 2, 'odd-v': -2}


def digest(b):
    return hashlib.sha256(b).hexdigest()


def sqrt_upper(q, bits=192):
    from math import isqrt
    assert q >= 0
    numerator = q.numerator << (2 * bits)
    r = isqrt(numerator // q.denominator)
    if r * r * q.denominator < numerator:
        r += 1
    out = F(r, 1 << bits)
    assert out * out >= q
    return out


def load_candidate(sector):
    cfg = CASES[sector]
    raw = (CAND / f'{sector}-wider-correction.bin').read_bytes()
    assert digest(raw) == cfg['cand_sha'] and len(raw) == 4755456
    vals = [int.from_bytes(raw[i:i + 18], 'little', signed=True)
            for i in range(0, len(raw), 18)]
    assert len(vals) == 264192
    modes = [cfg['first'] + 2 * i for i in range(264192)]
    assert modes[-1] == cfg['last']
    return modes, vals


def lt_params(start):
    pi = enclose(add(times(constant(16), atan_recip(5)),
                     neg(times(constant(4), atan_recip(239)))))
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))),
                          recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    L, t = midpoint(li, 256), midpoint(ti, 256)
    return L, t, radius(li, L), radius(ti, t)


def phase_moments(sector):
    """Exact M_j, P_delta, and z-independent aggregates. No z evaluations."""
    cfg = CASES[sector]
    modes, vals = load_candidate(sector)
    L, t, radL, radt = lt_params(cfg['start'])
    # M_j = sum_m m^(2j+1) * dy_int  (integer sums; value = M_j / 2^160)
    power = [1] * len(modes)
    moments_num = []
    for j in range(K):
        s = sum(m * v * w for m, v, w in zip(modes, vals, power))
        moments_num.append(s)
        power = [w * m * m for w, m in zip(power, modes)]
        print(sector, 'M moment', j + 1, '/', K, flush=True)
    # P_delta from 256-bit floors of L*m/(m^2+t)
    p_num = 0
    for m, v in zip(modes, vals):
        p_num += floor_bits(L * m / (m * m + t), 256) * v
    l1_int = sum(abs(v) for v in vals)
    s1_int = sum(abs(v) * m for m, v in zip(modes, vals))
    sumsq = sum(v * v for v in vals)
    out = {
        'sector': sector, 'L': str(L), 't': str(t),
        'L_radius': str(radL), 't_radius': str(radt),
        'c': str(C_RATIONAL), 'alpha': ALPHA[sector],
        'moments_M_numerators': [str(s) for s in moments_num],
        'pole_P_numerator': str(p_num),
        'l1_int': str(l1_int), 's1_int': str(s1_int), 'sumsq_int': str(sumsq),
    }
    (ROOT / f'moments-{sector}.json').write_text(json.dumps(out, indent=1))
    print(sector, 'moments phase done', flush=True)


_ZSTATE = {}


def _zblock(task):
    sector, bidx, modes_block, vals_block = task
    zints = []
    err_frac = F(0)   # sum |dy_m| * err_m  (exact)
    sz0 = F(0)        # sum (|zhat_m| + err_m) * |dy_m|
    max_err = F(0)
    for m, v in zip(modes_block, vals_block):
        row = z_eval(m)
        lo, hi = F(row['lower_rational']), F(row['upper_rational'])
        zp = (lo + hi) / 2
        zi = floor_bits(zp, 256)
        rep = F(zi, 1 << 256)
        err = max(abs(lo - rep), abs(hi - rep))
        zints.append(zi)
        if err > max_err:
            max_err = err
        err_frac += F(abs(v), 1 << 160) * err
        sz0 += (abs(rep) + err) * F(abs(v), 1 << 160)
    return {'sector': sector, 'bidx': bidx, 'zints': zints,
            'err_frac': err_frac, 'sz0': sz0, 'max_err': max_err}


def phase_z(sector):
    """Checkpointed parallel z phase: Z_j moments + z error aggregates."""
    from multiprocessing import Pool
    cfg = CASES[sector]
    modes, vals = load_candidate(sector)
    ckpt_path = ROOT / f'zckpt-{sector}.json'
    done = {}
    if ckpt_path.exists():
        done = json.loads(ckpt_path.read_text())
    err_frac = F(done.get('err_frac', '0'))
    sz0 = F(done.get('sz0', '0'))
    max_err = F(done.get('max_err', '0'))
    finished = set(done.get('blocks', []))
    zint_dir = ROOT / f'zints-{sector}'
    zint_dir.mkdir(exist_ok=True)
    BLOCK = 2048
    tasks = []
    for bidx, i0 in enumerate(range(0, len(modes), BLOCK)):
        if bidx in finished:
            continue
        tasks.append((sector, bidx, modes[i0:i0 + BLOCK], vals[i0:i0 + BLOCK]))
    print(sector, 'z blocks remaining:', len(tasks), 'of',
          (len(modes) + BLOCK - 1) // BLOCK, flush=True)
    t0 = time.time()
    with Pool(1) as pool:  # one sector per process; sectors run concurrently
        for res in pool.imap_unordered(_zblock, tasks, chunksize=1):
            bidx = res['bidx']
            err_frac += res['err_frac']
            sz0 += res['sz0']
            max_err = max(max_err, res['max_err'])
            (zint_dir / f'block{bidx:04d}.json').write_text(
                json.dumps(res['zints']))
            finished.add(bidx)
            ckpt_path.write_text(json.dumps({
                'err_frac': str(err_frac), 'sz0': str(sz0),
                'max_err': str(max_err), 'blocks': sorted(finished)}))
            print(sector, 'block', bidx, 'done; elapsed',
                  round(time.time() - t0), 's', flush=True)
    print(sector, 'z phase complete', flush=True)


def phase_zmoments(sector):
    """Z_j = sum_m zint_m * dy_int * m^(2j) from the saved zint blocks."""
    cfg = CASES[sector]
    modes, vals = load_candidate(sector)
    zint_dir = ROOT / f'zints-{sector}'
    BLOCK = 2048
    zints = []
    for bidx, i0 in enumerate(range(0, len(modes), BLOCK)):
        zints += json.loads((zint_dir / f'block{bidx:04d}.json').read_text())
    assert len(zints) == len(modes)
    power = [1] * len(modes)
    zmom = []
    for j in range(K):
        s = sum(z * v * w for z, v, w in zip(zints, vals, power))
        zmom.append(s)
        power = [w * m * m for w, m in zip(power, modes)]
        print(sector, 'Z moment', j + 1, '/', K, flush=True)
    out = {'sector': sector, 'moments_Z_numerators': [str(s) for s in zmom]}
    (ROOT / f'zmoments-{sector}.json').write_text(json.dumps(out, indent=1))
    print(sector, 'zmoments done', flush=True)


def _load_zints(sector):
    modes, vals = load_candidate(sector)
    zint_dir = ROOT / f'zints-{sector}'
    BLOCK = 2048
    zints = []
    for bidx, i0 in enumerate(range(0, len(modes), BLOCK)):
        zints += json.loads((zint_dir / f'block{bidx:04d}.json').read_text())
    assert len(zints) == len(modes)
    return modes, vals, zints


def _direct_row(task):
    sector, n = task
    cfg = CASES[sector]
    modes, vals, zints = _load_zints(sector)
    mom = json.loads((ROOT / f'moments-{sector}.json').read_text())
    zmom = json.loads((ROOT / f'zmoments-{sector}.json').read_text())
    L, t = F(mom['L']), F(mom['t'])
    c, alpha = C_RATIONAL, ALPHA[sector]
    row = z_eval(n)
    lo, hi = F(row['lower_rational']), F(row['upper_rational'])
    zp = (lo + hi) / 2
    rad_n = (hi - lo) / 2
    assert abs(zp) < 8
    # retained series (kernel part) in exact rationals
    ret = F(0)
    for j in range(K):
        Mj = F(int(mom['moments_M_numerators'][j]), 1 << 160)
        Zj = F(int(zmom['moments_Z_numerators'][j]), 1 << 416)
        ret += c * zp * Mj / n ** (2 * j + 2) - c * Zj / n ** (2 * j + 1)
    P = F(int(mom['pole_P_numerator']), 1 << 416)
    pole = alpha * (L * n / (n * n + t)) * P
    # direct sums over represented values, integer form, floor at 512 bits
    A = zp.numerator
    Bq = zp.denominator.bit_length() - 1
    assert (1 << Bq) == zp.denominator
    den_common = (1 << (416 + Bq))
    s_dir = 0
    s_tail = 0
    n84 = n ** 84
    for m, v, zi in zip(modes, vals, zints):
        tnum = v * (A * m * (1 << 256) - n * zi * (1 << Bq))
        tden = den_common * (n * n - m * m)
        s_dir += (tnum << 512) // tden
        s_tail += (tnum * m ** 84 << 512) // (tden * n84)
    direct = c * F(s_dir, 1 << 512)
    tail = c * F(s_tail, 1 << 512)
    check_error = 2 * abs(c) * F(len(modes), 1 << 512)
    assert abs(direct - ret - tail) <= check_error
    return {'sector': sector, 'n': n, 'zpoint': str(zp),
            'z_radius': str(rad_n), 'retained_kernel': str(ret),
            'pole_part': str(pole), 'direct_kernel': str(direct),
            'exact_tail': str(tail), 'check_error': str(check_error),
            'identity_holds': True}


def phase_checks():
    from multiprocessing import Pool
    tasks = []
    for sector, cfg in CASES.items():
        N0 = cfg['N0']
        tasks += [(sector, N0), (sector, N0 + 16384), (sector, 3 * N0)]
    with Pool(2) as pool:
        results = pool.map(_direct_row, tasks)
    out = {}
    for r in results:
        out.setdefault(r['sector'], []).append(r)
        print(r['sector'], 'direct row', r['n'], 'verified', flush=True)
    (ROOT / 'checks.json').write_text(json.dumps(out, indent=1))
    print('checks done', flush=True)


def phase_cert(sector):
    cfg = CASES[sector]
    mom = json.loads((ROOT / f'moments-{sector}.json').read_text())
    zmom = json.loads((ROOT / f'zmoments-{sector}.json').read_text())
    zck = json.loads((ROOT / f'zckpt-{sector}.json').read_text())
    checks = json.loads((ROOT / 'checks.json').read_text())[sector]
    L, t = F(mom['L']), F(mom['t'])
    radL, radt = F(mom['L_radius']), F(mom['t_radius'])
    c, alpha = C_RATIONAL, ALPHA[sector]
    M, N0, b = cfg['last'], cfg['N0'], cfg['first']
    l1 = F(int(mom['l1_int']), 1 << 160)
    S1 = F(int(mom['s1_int']), 1 << 160)
    sz0 = F(zck['sz0'])
    errz = F(zck['err_frac'])
    max_err = F(zck['max_err'])
    patch_norm = sqrt_upper(F(int(mom['sumsq_int']), 1 << 320), 192)
    r0 = F(M * M, N0 * N0)
    assert N0 > M and r0 <= F(1, 4)  # odd sector endpoint is exactly 1/4
    r0_42 = r0 ** 42
    P = F(int(mom['pole_P_numerator']), 1 << 416)
    # geometric remainder envelopes (derived in the certificate text)
    def geo_row(n):
        return abs(c) * r0_42 * (8 * S1 + n * sz0) / (n * n - M * M)
    sum4 = (1 / (1 - r0) ** 2) * (1 + F(N0, 6)) / N0 ** 4
    sum2 = (1 / (1 - r0) ** 2) * (1 + F(N0, 2)) / N0 ** 2
    geo_l2 = abs(c) * r0_42 * sqrt_upper(
        2 * (8 * S1) ** 2 * sum4 + 2 * sz0 ** 2 * sum2, 192)
    # input-z envelope, counted once
    def inz_row(n):
        return abs(c) * n * errz / (n * n - M * M)
    inz_l2 = abs(c) * errz / (1 - r0) * sqrt_upper((1 + F(N0, 2)) / N0 ** 2, 192)
    # pole envelope, counted once
    dP = l1 * (F(1, 1 << 256) + radL / b + (L + radL) * radt / b ** 3)
    Phat = abs(P) + dP
    def pole_row(n):
        pn = L * n / (n * n + t)
        return abs(alpha) * (pn * dP + Phat * (radL / n + (L + radL) * radt / n ** 3))
    pole_l2 = abs(alpha) * (L * dP + Phat * radL + Phat * (L + radL) * radt / N0 ** 2) \
        * sqrt_upper((1 + F(N0, 2)) / N0 ** 2, 192)
    total_l2 = geo_l2 + inz_l2 + pole_l2
    # verify the rowwise geometric bound at the check rows
    for chk in checks:
        n = chk['n']
        assert abs(F(chk['exact_tail'])) <= geo_row(n) + F(chk['check_error'])
    moments = [{'j': j,
                'M_odd_rational': str(F(int(mom['moments_M_numerators'][j]), 1 << 160)),
                'Z_even_rational': str(F(int(zmom['moments_Z_numerators'][j]), 1 << 416))}
               for j in range(K)]
    cert = {
        'schema': 'cone.sandbox-far-patch-moments.v1',
        'sector': sector,
        'task': 'v14.344 HANDOFF - Sandbox: finite wider-patch-only far-action moment package',
        'candidate_sha256': cfg['cand_sha'],
        'support': {'first_mode': cfg['first'], 'last_mode': M, 'step': 2,
                    'count': 264192},
        'far_first_mode': N0, 'K': K,
        'action_formula': 'c*z_n*sum(M_j/n^(2j+2)) - c*sum(Z_j/n^(2j+1)) '
                          '+ alpha*(L*n/(n^2+t))*P_delta, for n >= far_first_mode; '
                          'kernel+pole only (diagonal term is zero beyond the support)',
        'moments': moments,
        'point_parameters': {'c': str(c), 'alpha': alpha, 'L': str(L),
                             't': str(t), 'pole_moment': str(P)},
        'z_representation': 'zhat_m = floor(midpoint(z enclosure), 256) at every '
                            'support mode, from suzuki_bulk_action_z.evaluate; '
                            'err_m = max(|lo-zhat|, |hi-zhat|) exact',
        'rational': {
            'patch_norm_upper': str(patch_norm),
            'patch_l1': str(l1),
            'ratio_endpoint_r0': str(r0),
            'ratio_r0_pow_42': str(r0_42),
            'geometric_remainder_row_at_N0': str(geo_row(N0)),
            'geometric_remainder_l2_upper': str(geo_l2),
            'input_z_error_sum': str(errz),
            'input_z_max_mode_error': str(max_err),
            'input_z_row_at_N0': str(inz_row(N0)),
            'input_z_l2_upper': str(inz_l2),
            'pole_moment_error_upper': str(dP),
            'pole_row_at_N0': str(pole_row(N0)),
            'pole_l2_upper': str(pole_l2),
            'total_far_error_l2_upper': str(total_l2)},
        'display_approximate': {
            'ratio_endpoint_r0': float(r0),
            'geometric_remainder_row_at_N0': float(geo_row(N0)),
            'geometric_remainder_l2_upper': float(geo_l2),
            'input_z_row_at_N0': float(inz_row(N0)),
            'input_z_l2_upper': float(inz_l2),
            'pole_row_at_N0': float(pole_row(N0)),
            'pole_l2_upper': float(pole_l2),
            'total_far_error_l2_upper': float(total_l2),
            'pole_moment': float(P)},
        'remainder_derivation': 'Exact identity 1/(n^2-m^2) = sum_{j<42} m^(2j)/'
                                'n^(2j+2) + (m/n)^84/(n^2-m^2). Row tail bounded by '
                                '|c| r0^42 (8*S1 + n*Sz0)/(n^2-M^2) with S1 = sum '
                                '|dy_m| m, Sz0 = sum (|zhat_m|+err_m) |dy_m|, |z_n| <= 8. '
                                'l2 sums use n^2-M^2 >= n^2 (1-r0) and integral '
                                'comparison sum_{step2, n>=N0} n^-4 <= (1+N0/6)/N0^4, '
                                'n^-2 <= (1+N0/2)/N0^2. Input-z error counted once via '
                                'the full kernel: |c| n E_z/(n^2-M^2), E_z = sum '
                                'err_m |dy_m|. Pole error counted once: floor error '
                                'l1*2^-256 plus L/t midpoint-radius propagation '
                                'l1 (radL/b + (L+radL) radt/b^3), output side via '
                                '|dp_n| <= radL/n + (L+radL) radt/n^3.',
        'complete_direct_far_checks': checks,
        'input_z_and_pole_uncertainty_counted_once': True,
        'diagonal_term_included': False,
        'whole_residual_acceptance_claimed': False,
        'stationary_acceptance_met': False,
        'infinite_capacity_tail_closed': False,
    }
    outdir = ROOT / 'out'
    outdir.mkdir(exist_ok=True)
    (outdir / f'far-patch-moments-{sector}.json').write_text(
        json.dumps(cert, indent=2, sort_keys=True) + '\n')
    print(sector, 'cert done:', cert['display_approximate'], flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('phase', choices=('moments', 'z', 'zmoments', 'checks', 'cert'))
    p.add_argument('sector', choices=list(CASES) + ['both'], nargs='?',
                   default='both')
    a = p.parse_args()
    ROOT.mkdir(parents=True, exist_ok=True)
    if a.phase == 'moments':
        phase_moments(a.sector)
    elif a.phase == 'z':
        phase_z(a.sector)
    elif a.phase == 'zmoments':
        phase_zmoments(a.sector)
    elif a.phase == 'checks':
        phase_checks()
    else:
        for s in (('even-v', 'odd-v') if a.sector == 'both' else (a.sector,)):
            phase_cert(s)
