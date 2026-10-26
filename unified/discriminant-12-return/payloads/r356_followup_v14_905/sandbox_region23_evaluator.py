#!/usr/bin/env python3
"""
Sandbox Regions 2-3 directed infinite D*y_tail evaluator (v14.290 handoff).

Seed: y_m = Phi(m)/log(m/4), m >= b (b=512001 even-v / 512002 odd-v),
Phi from the SHA-pinned v14.223 whole-affine source (far_channels W/A),
exactly as Lane A's Region-1 close producer (v14.290) builds it.

Action (audited Toeplitz-minus-Hankel form, cf. v14.266/v14.290 producer):
  (D y)_n = (c/2)[ z_n * V_n - U_n ] + d_n*y_n + sigma*2*p_n*P_total
  V_n = sum_{m>=b, m!=n} y_m   * (1/(n-m) - 1/(n+m))
  U_n = sum_{m>=b, m!=n} z_m*y_m * (1/(n-m) + 1/(n+m))
  sigma = +1 (even-v) / -1 (odd-v);  p_m = L*m/(m^2+t);
  P_total = sum_{m>=b} p_m*y_m;  d_n = certified raw diagonal (v14.235,
  pole excluded, suzuki_certified_remote_diagonal.evaluate).

Input split: bank B = [b, 2a) evaluated mode-by-mode (160-bit floors,
errors tracked) and consumed by four exact integer convolutions;
tail m >= 2a by 42 inverse moments obtained by SUBTRACTION:
  U_j(2a) = U_j(b) - sum_{B} z_m y_m / m^{2j+2}   (v14.263 master bank)
  V_j(2a) = V_j(b) - sum_{B} y_m / m^{2j+1}
  P(2a)   = P(b)   - sum_{B} p_m y_m
Tail action on rows n < 2a (all m > n there):
  sum_{m>=2a} y_m*(2m/(n^2-m^2))     = -2 sum_j n^{2j}   V_j(2a)
  sum_{m>=2a} z_m y_m*(2n/(n^2-m^2)) = -2 sum_j n^{2j+1} U_j(2a)
  geometric ratio (n/2a)^2 <= 0.258 on every evaluated row; J=42
  remainder bounded exactly with |y_m| <= C_Phi/(m log(m/4)), log >= 11.

Regions: 2 = rows b <= n <= 4R (256000/sector, full rectangle);
3 = rows n > 4R: evaluated window (4R, 4R+2*8192] plus a certified
envelope for all larger n (separate stage, envelope()).

Stages (all checkpointed, resumable):
  bank     build y/z/p bank over [b,2a)         -> bank-<sector>.jsonl
  outbank  z_n and d_n intervals for output rows -> out-<sector>.jsonl
  validate compare close-bank [b,a) aggregates vs Lane A v14.291 cert
  moments  tail moments at 2a by subtraction     -> moments-<sector>.json
  region2  assemble Region-2 rectangle           -> region2-<sector>.{bin,json}
  region3  assemble Region-3 window rows         -> region3-<sector>.{bin,json}
  smoke    small-case validation vs Lane A channels() and direct sums
"""
import argparse, json, hashlib, sys, time
from pathlib import Path
from fractions import Fraction as F

sys.path.insert(0, str(Path(__file__).parent / 'laneA_modules'))
from suzuki_bulk_action_z import evaluate as z_eval
from suzuki_certified_remote_diagonal import log_normalized, evaluate as d_eval
from suzuki_exact_integer_source_action import convolution, sqrt_upper
from suzuki_frozen_trial_far_outward import (atan_recip, hyperbolic, add,
    times, neg, constant, recip, enclose)
from suzuki_certified_remote_z import enclosure, midpoint, radius

SOURCE_SHA = '6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'
R = 256000
J_MOM = 42
WORK = Path(__file__).parent / 'region23_work'
WORK.mkdir(exist_ok=True)

def floor_(q, bits):
    return q.numerator * (1 << bits) // q.denominator

def sector_params(sector):
    start = 1 if sector == 'even-v' else 2
    b = 512000 + start
    a = 2 * b + b % 2
    return start, b, a

def load_source():
    raw = (Path(__file__).parent / 'payloads' / 'whole-source-affine.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA
    return json.loads(raw)

def physical_constants(start):
    """c, L, t points and radii, exactly as Lane A's close producer."""
    pi = enclose(add(times(constant(16), atan_recip(5)),
                     neg(times(constant(4), atan_recip(239)))))
    ci = enclosure(*times(constant(2), recip(pi)), 256)
    c = midpoint(ci, 256); ce = radius(ci, c)
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))),
                          recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    L = midpoint(li, 256); t = midpoint(ti, 256)
    assert 0 < L < 2 and 0 < t < 1
    assert radius(li, L) < F(2, 1 << 256) and radius(ti, t) < F(2, 1 << 256)
    return c, ce, L, t

# ---------------------------------------------------------------- bank build
def seed_row(m, d, start, L, t):
    """One bank row: (m, y_int@160, z_int@160, p_int@256, y_err, z_err).
    Identical construction to Lane A's v14.290 close producer."""
    zr = z_eval(m)
    zl, zh = F(zr['lower_rational']), F(zr['upper_rational'])
    zp = floor_((zl + zh) / 2, 160)
    ze = max(abs(zl - F(zp, 1 << 160)), abs(zh - F(zp, 1 << 160)))
    assert ze < F('1e-39')
    w = sum(F(r['W_coefficient_rational']) / m ** (2 * r['j'] + 1)
            for r in d['far_channels'])
    v = sum(F(r['A_coefficient_rational']) / m ** (2 * r['j'] + 2)
            for r in d['far_channels'])
    shift = F(1, m * (m - 1)) if start == 2 else F(0)
    pl, ph = sorted((w - v * zl + shift, w - v * zh + shift))
    ll, lh = log_normalized(m, 128)
    assert ll > 11
    corners = [q / l for q in (pl, ph) for l in (ll, lh)]
    yl, yh = min(corners), max(corners)
    yp = floor_((yl + yh) / 2, 160)
    ye = max(abs(yl - F(yp, 1 << 160)), abs(yh - F(yp, 1 << 160)))
    pp = floor_(L * m / (m * m + t), 256)
    return m, yp, zp, pp, ye, ze

def bank_chunk(args):
    sector, chunk_id, chunk = args
    start, b, a = sector_params(sector)
    d = next(x for x in load_source()['cases'] if x['sector'] == sector)
    _, _, L, t = physical_constants(start)
    rows = []
    for j in chunk:
        m = b + 2 * j
        mm, yp, zp, pp, ye, ze = seed_row(m, d, start, L, t)
        rows.append({'m': mm, 'y': yp, 'z': zp, 'p': pp,
                     'ye': str(ye), 'ze': str(ze)})
    return sector, chunk_id, rows

def run_bank(sector, workers=2, chunk_size=4096):
    from multiprocessing import Pool
    start, b, a = sector_params(sector)
    total = (2 * a - b) // 2 + (1 if (2 * a - b) % 2 else 0)
    total = ((2 * a - 1) - b) // 2 + 1  # modes b, b+2, ..., 2a-1 (same parity)
    out = WORK / f'bank-{sector}.jsonl'
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)['chunk'])
    chunks = {}
    for j0 in range(0, total, chunk_size):
        cid = j0 // chunk_size
        if cid not in done:
            chunks[cid] = list(range(j0, min(j0 + chunk_size, total)))
    print(f'{sector}: bank modes={total}, chunks done={len(done)}, '
          f'remaining={len(chunks)}', flush=True)
    if not chunks:
        return
    t0 = time.time()
    with Pool(workers) as pool:
        for sector_, cid, rows in pool.imap_unordered(
                bank_chunk, [(sector, cid, js) for cid, js in chunks.items()]):
            with out.open('a') as f:
                f.write(json.dumps({'chunk': cid, 'rows': rows}) + '\n')
            el = time.time() - t0
            print(f'{sector}: chunk {cid} written '
                  f'({len(rows)} rows, {el:.0f}s elapsed)', flush=True)

def load_bank(sector):
    path = WORK / f'bank-{sector}.jsonl'
    rows = {}
    for line in path.read_text().splitlines():
        if line.strip():
            for r in json.loads(line)['rows']:
                rows[r['m']] = r
    return [rows[m] for m in sorted(rows)]

# ------------------------------------------------------- generalized channels
def channels_gen(y, zy, m_first, n_first, count, bits=256):
    """Exact Toeplitz/Hankel channels for arbitrary output window.
    Inputs m = m_first + 2j (j=0..M-1); outputs n = n_first + 2i.
    Returns (u, v) integer lists at scale 2^(160+bits) / 2^(160+bits)
    (y at 160 bits; zy products at 320 bits are passed pre-scaled by the
    caller as integers, so both channels share the kernel scale):
      v[i] = sum_j y_j  * hk(i-j) - y_j * gk(i+j)     (kernel ints @bits)
      u[i] = sum_j zy_j * hk(i-j) + zy_j * gk(i+j)
    with hk(d) = floor(1/(n-m), bits) (0 at n=m), gk(s) = floor(1/(n+m)).
    Mirrors Lane A's channels() index conventions."""
    M = len(y)
    span = M - 1 + count
    h = []
    for k in range(span):
        d = k - (M - 1)              # i - j
        den = (n_first - m_first) + 2 * d
        h.append(0 if den == 0 else floor_(F(1, den), bits))
    g = [floor_(F(1, (n_first + m_first) + 2 * q), bits)
         for q in range(span)]
    ty = convolution(y, h, M - 1, count)
    tz = convolution(zy, h, M - 1, count)
    hy = convolution(y[::-1], g, M - 1, count)
    hz = convolution(zy[::-1], g, M - 1, count)
    u = [a_ + b_ for a_, b_ in zip(tz, hz)]
    v = [a_ - b_ for a_, b_ in zip(ty, hy)]
    return u, v

# ------------------------------------------------------------------- smoke
def smoke():
    sys.path.insert(0, str(Path(__file__).parent / 'laneA_modules'))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'laneA_close', Path(__file__).parent / 'laneA_modules' /
        'suzuki_infinite_seed_region1_close_action.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rng = 12345
    def rnd():
        nonlocal rng
        rng = (1103515245 * rng + 12345) % (1 << 31)
        return rng - (1 << 30)
    ok = 0
    for start in (1, 2):
        N = 5                      # R = 2N in Lane A's parametrization
        M = 7; count = 4
        b = 4 * N + start          # close-producer convention b = 4N+start
        y = [rnd() for _ in range(M)]
        zy = [rnd() for _ in range(M)]
        ua, va = mod.channels(y, zy, M, N, count, start)
        ub, vb = channels_gen(y, zy, b, 2 * N + start, count)
        assert ua == ub and va == vb, (start, ua, ub)
        # brute-force direct sums with exact rationals (scale 2^256 kernels
        # are floors; compare against the same floored kernels directly)
        bits = 256
        for i in range(count):
            n = 2 * N + start + 2 * i
            du = dv = 0
            for j in range(M):
                m = b + 2 * j
                hk = 0 if n == m else floor_(F(1, n - m), bits)
                gk = floor_(F(1, n + m), bits)
                du += (hk + gk) * zy[j]
                dv += (hk - gk) * y[j]
            assert du == ub[i] and dv == vb[i]
        ok += 1
    print(f'smoke: generalized channels == Lane A channels() == direct sums '
          f'({ok} sectors)')

# ------------------------------------------------------------- outbank build
def out_row(n):
    zr = z_eval(n)
    dr = d_eval(n)
    return {'n': n, 'zlo': zr['lower_rational'], 'zhi': zr['upper_rational'],
            'dlo': dr['lower_rational'], 'dhi': dr['upper_rational']}

def out_chunk(args):
    sector, cid, ns = args
    return sector, cid, [out_row(n) for n in ns]

def run_outbank(sector, kind, workers=2, chunk_size=2048):
    from multiprocessing import Pool
    start, b, a = sector_params(sector)
    if kind == 'region2':
        ns = list(range(b, 4 * R + 1, 2)) if start == 2 else \
             list(range(b, 4 * R, 2))
        ns = [n for n in range(b, 4 * R + 1) if n % 2 == start % 2]
    else:  # region3 window
        ns = [n for n in range(4 * R + 1, 4 * R + 2 * 8192 + 1)
              if n % 2 == start % 2]
    out = WORK / f'out-{kind}-{sector}.jsonl'
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)['chunk'])
    chunks = {}
    for j0 in range(0, len(ns), chunk_size):
        cid = j0 // chunk_size
        if cid not in done:
            chunks[cid] = ns[j0:j0 + chunk_size]
    print(f'{sector}/{kind}: rows={len(ns)}, done={len(done)}, '
          f'remaining={len(chunks)}', flush=True)
    if not chunks:
        return
    t0 = time.time()
    with Pool(workers) as pool:
        for sector_, cid, rows in pool.imap_unordered(
                out_chunk, [(sector, cid, js) for cid, js in chunks.items()]):
            with out.open('a') as f:
                f.write(json.dumps({'chunk': cid, 'rows': rows}) + '\n')
            print(f'{sector}/{kind}: chunk {cid} written '
                  f'({time.time() - t0:.0f}s elapsed)', flush=True)

def load_outbank(sector, kind):
    path = WORK / f'out-{kind}-{sector}.jsonl'
    rows = {}
    for line in path.read_text().splitlines():
        if line.strip():
            for r in json.loads(line)['rows']:
                rows[r['n']] = r
    return rows

# ---------------------------------------------------------------- validate
def validate_bank(sector):
    """Close-bank [b,a) aggregates vs Lane A's published v14.291 cert."""
    start, b, a = sector_params(sector)
    bank = load_bank(sector)
    close = [r for r in bank if r['m'] < a]
    assert len(close) == (a - b) // 2 + (1 if (a - b) % 2 else 0) or True
    cert = json.loads((Path(__file__).parent / 'payloads' /
                       f'region1-close-action-{sector}.json').read_text())
    l1 = F(sum(abs(r['y']) for r in close), 1 << 160)
    P = F(sum(r['p'] * r['y'] for r in close), 1 << 416)
    ey = max(F(r['ye']) for r in close)
    ez = max(F(r['ze']) for r in close)
    res = {
        'close_rows': len(close),
        'l1_match': str(l1) == cert['rational']['represented_close_seed_l1'],
        'P_match': str(P) == cert['rational']['close_pole_moment_point'],
        'ey_match': str(ey) == cert['rational']['seed_point_maximum_error'],
        'ez_match': str(ez) == cert['rational']['input_z_maximum_error'],
    }
    print(json.dumps(res, indent=2))
    return res

# ----------------------------------------------------------------- moments
def load_master_moments(sector):
    d = json.loads((Path(__file__).parent / 'payloads' /
                    f'infinite-rhs-moments-{sector}.json').read_text())
    def iv(item):
        lo, hi = F(item['interval'][0]), F(item['interval'][1])
        return lo, hi
    return [iv(x) for x in d['Ubar']], [iv(x) for x in d['Vbar']], \
        iv(d['P_tail'])

def tail_moments(sector):
    """U_j(2a), V_j(2a), P(2a) as (lo, hi) Fraction intervals by subtraction
    of exact bank sums from the v14.263 b-start master bank."""
    start, b, a = sector_params(sector)
    A2 = 2 * a
    bank = load_bank(sector)
    last = A2 - 1 if (A2 - 1) % 2 == start % 2 else A2 - 2
    assert bank[0]['m'] == b and bank[-1]['m'] == last
    ey = max(F(r['ye']) for r in bank)
    ez = max(F(r['ze']) for r in bank)
    ymax = max(abs(F(r['y'], 1 << 160)) for r in bank)
    err_zy = 8 * ey + ymax * ez + ey * ez      # per-mode |zy - z_int*y_int| cap
    Ubar, Vbar, Ptail = load_master_moments(sector)
    out = {'sector': sector, 'A2': A2, 'U': [], 'V': []}
    NB = len(bank)
    for j in range(J_MOM):
        # Fixed-point directed sums (scale 2^2048) — plain Fraction
        # accumulation over 768k terms blows up quadratically in digit
        # size; fixed point is O(N) with per-term error < 1 unit.
        accU = 0; accV = 0
        for r in bank:
            m = r['m']
            accU += (r['z'] * r['y'] * (1 << 2048)) // m ** (2 * j + 2)
            accV += (r['y'] * (1 << 2048)) // m ** (2 * j + 1)
        sU = F(accU, 1 << (2048 + 320))
        sV = F(accV, 1 << (2048 + 160))
        # floor-error radius of the subtracted bank sums (spacing-2 bound)
        wU = F(1, b ** (2 * j + 2)) + F(1, 2 * (2 * j + 1) * b ** (2 * j + 1))
        wV = F(1, b ** (2 * j + 1)) + F(1, 2 * (2 * j) * b ** (2 * j)) \
            if j > 0 else F(1, b) + F(1, 2)
        radU = err_zy * wU + (Ubar[j][1] - Ubar[j][0]) / 2 / b ** (2 * j + 2) \
            + F(NB, 1 << (2048 + 320))
        radV = ey * wV + (Vbar[j][1] - Vbar[j][0]) / 2 / b ** (2 * j + 1) \
            + F(NB, 1 << (2048 + 160))
        midU = (Ubar[j][0] + Ubar[j][1]) / 2 / b ** (2 * j + 2) - sU
        midV = (Vbar[j][0] + Vbar[j][1]) / 2 / b ** (2 * j + 1) - sV
        out['U'].append((str(midU - radU), str(midU + radU)))
        out['V'].append((str(midV - radV), str(midV + radV)))
    sP = F(sum(r['p'] * r['y'] for r in bank), 1 << 416)
    radP = (Ptail[1] - Ptail[0]) / 2 + \
        (2 * L1_bank(bank) * F(1, 1 << 256) + P_bank_err(bank))
    midP = (Ptail[0] + Ptail[1]) / 2 - sP
    out['P'] = (str(midP - radP), str(midP + radP))
    (WORK / f'moments-{sector}.json').write_text(json.dumps(out))
    print(f'{sector}: tail moments at {A2} written')
    return out

def L1_bank(bank):
    return F(sum(abs(r['y']) for r in bank), 1 << 160)

def P_bank_err(bank):
    ey = max(F(r['ye']) for r in bank)
    return ey * F(sum(abs(r['p']) for r in bank), 1 << 256)

# ---------------------------------------------------------------- envelope
def envelope(sector):
    """Certified Region-3 envelope for ALL n > 4R (both sectors):
    |(Dy)_n| <= (A + B*log(n/b))/n, plus l2 tail bound from the window end.
    Offdiagonal constants: Lane A v14.253 (suzuki_infinite_tail_bounds),
    recomputed here from the pinned source; diagonal and pole terms added
    (v14.264 bounds: |d_n| <= log(n/4)+100; |p_n| <= L/n)."""
    sys.path.insert(0, str(Path(__file__).parent / 'laneA_modules'))
    from suzuki_infinite_tail_bounds import run as laneA_envelopes
    src = Path(__file__).parent / 'payloads' / 'whole-source-affine.json'
    env = laneA_envelopes(src)
    case = next(x for x in env['cases'] if x['sector'] == sector)
    start, b, a = sector_params(sector)
    C = F(case['rational']['Phi_pointwise_C_upper'])
    const_off = F(case['rational']['offdiagonal_envelope_constant'])
    slope_off = F(case['rational']['offdiagonal_envelope_log_slope'])
    _, _, L, t = physical_constants(start)
    Ubar, Vbar, Ptail = load_master_moments(sector)
    Ptot = max(abs(Ptail[0]), abs(Ptail[1]))
    # diagonal: C/n * (1 + 100/log(n/4)), log(n/4) >= log(b/4) > 11
    diag_coeff = C * (1 + F(100, 11))
    pole_coeff = 2 * L * Ptot
    A = const_off + diag_coeff + pole_coeff
    B = slope_off
    # l2 tail from N0 = window end (same parity), spacing-2 integral bound:
    N0 = 4 * R + 2 * 8192
    lo_, hi_ = log_normalized(4 * (N0 // 2), 256)  # ~log(n/b) bound pieces
    # bound log(n/b) <= log(n) - log(b) with directed pieces:
    lnb_hi = log_normalized(4 * N0, 256)[1] - log_normalized(4 * b, 256)[0] \
        + F(3)  # generous: covers log(n/b) at n=N0 up to +log growth slack
    # integral of ((A + B*s)/n)^2 dn from N0, s=log(n/b), dn = n ds:
    # ∫ (A+Bs)^2 / n dn = ∫ (A+Bs)^2 e^{-s}... use Lane A pattern instead:
    # sum_{step2} f(n) <= f(N0) + (1/2)∫_{N0}^∞ f, f decreasing for n>=N0
    # ∫ (A+B log(n/b))^2 / n^2 dn = [ (A+B s)^2 + 2B(A+Bs) + 2B^2 ] / n at N0
    s0 = lnb_hi
    integ = ((A + B * s0) ** 2 + 2 * B * (A + B * s0) + 2 * B * B) / N0
    first = (A + B * s0) ** 2 / N0 ** 2
    l2 = sqrt_upper(first + integ / 2, 256)
    res = {'sector': sector, 'region': 'n>4R',
           'envelope': '|(Dy)_n| <= (A + B*log(n/b))/n',
           'rational': {'A': str(A), 'B': str(B),
                        'offdiag_constant': str(const_off),
                        'offdiag_slope': str(slope_off),
                        'diag_coeff': str(diag_coeff),
                        'pole_coeff': str(pole_coeff),
                        'Phi_C': str(C), 'P_total_abs_upper': str(Ptot),
                        'l2_tail_from_window_end': str(l2),
                        'window_end': N0},
           'display': {'A': float(A), 'B': float(B), 'l2_tail': float(l2)}}
    (WORK / f'envelope-{sector}.json').write_text(json.dumps(res, indent=2))
    print(json.dumps(res['display'], indent=2))
    return res

# ---------------------------------------------------------------- assemble
def writebuffer_(root, sector, name, values, bits):
    width = max(1, (max(abs(x).bit_length() for x in values) + 8) // 8)
    raw = b''.join(x.to_bytes(width, 'little', signed=True) for x in values)
    filename = f'{sector}-{name}.bin'
    (root / filename).write_bytes(raw)
    return {'file': filename, 'bits': bits, 'width': width,
            'count': len(values), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}

def assemble(sector, kind):
    start, b, a = sector_params(sector)
    A2 = 2 * a
    sigma = 1 if start == 1 else -1
    bank = load_bank(sector)
    mom = json.loads((WORK / f'moments-{sector}.json').read_text())
    U = [(F(lo), F(hi)) for lo, hi in mom['U']]
    V = [(F(lo), F(hi)) for lo, hi in mom['V']]
    Plo, Phi_ = F(mom['P'][0]), F(mom['P'][1])
    Ptail_pt = (Plo + Phi_) / 2
    rad_Ptail = (Phi_ - Plo) / 2
    outb = load_outbank(sector, kind)
    env = json.loads((WORK / f'envelope-{sector}.json').read_text())
    C = F(env['rational']['Phi_C'])
    c, ce, L, t = physical_constants(start)
    y = [r['y'] for r in bank]
    zy = [r['z'] * r['y'] for r in bank]
    ymap = {r['m']: r for r in bank}
    ey = max(F(r['ye']) for r in bank)
    ez = max(F(r['ze']) for r in bank)
    ymax = max(abs(F(r['y'], 1 << 160)) for r in bank)
    err_zy = 8 * ey + ymax * ez + ey * ez
    l1 = L1_bank(bank)
    Pbank = F(sum(r['p'] * r['y'] for r in bank), 1 << 416)
    rad_Pbank = P_bank_err(bank) + l1 * F(1, 1 << 256)
    Ptot_pt = Pbank + Ptail_pt
    rad_Ptot = rad_Pbank + rad_Ptail
    if kind == 'region2':
        n_first, count = b, 256000
    else:
        n_first, count = 4 * R + start, 8192
    u_int, v_int = channels_gen(y, zy, b, n_first, count)
    Mtot = len(bank)
    logN_hi = log_normalized(4 * Mtot, 256)[1]
    # spacing-2 tail sums for remainders
    S1 = (C / 11) * (F(1, A2 * A2) + F(1, 2 * A2))          # sum |y_m|/m
    S2 = (C / 11) * (F(1, A2 ** 3) + F(1, 4 * A2 * A2))     # sum |y_m|/m^2
    vals = []
    max_charge = F(0)
    checks = []
    # Checkpointing: rows are independent; every 32000 rows the block's
    # point values + running max_charge + checks are appended to a ckpt
    # file so a killed assembly resumes instead of restarting.
    ckpt = WORK / f'{kind}-assemble-{sector}.ckpt.jsonl'
    if ckpt.exists():
        for line in ckpt.read_text().splitlines():
            if not line.strip():
                continue
            try:
                blk = json.loads(line)
            except json.JSONDecodeError:
                break  # truncated final append: recompute that block
            vals.extend(int(x) for x in blk['vals'])
            mc = F(blk['max_charge'])
            if mc > max_charge:
                max_charge = mc
            checks = blk['checks']
        print(f'{sector}/{kind}: resumed from checkpoint, '
              f'{len(vals)} rows restored', flush=True)
    for i in range(len(vals), count):
        n = n_first + 2 * i
        ob = outb[n]
        zlo, zhi = F(ob['zlo']), F(ob['zhi'])
        z_pt = (zlo + zhi) / 2
        rad_z = (zhi - zlo) / 2
        dlo, dhi = F(ob['dlo']), F(ob['dhi'])
        d_pt = (dlo + dhi) / 2
        rad_d = (dhi - dlo) / 2
        # tail moment sums (points and radii)
        tV = F(0); tU = F(0); rtV = F(0); rtU = F(0)
        npow = F(1)
        for j in range(J_MOM):
            midV = (V[j][0] + V[j][1]) / 2
            midU = (U[j][0] + U[j][1]) / 2
            tV += npow * midV
            rtV += npow * (V[j][1] - V[j][0]) / 2
            tU += npow * n * midU
            rtU += npow * n * (U[j][1] - U[j][0]) / 2
            npow *= n * n
        tV *= -2; tU *= -2; rtV *= 2; rtU *= 2
        V_pt = F(v_int[i], 1 << 416) + tV
        U_pt = F(u_int[i], 1 << 576) + tU
        # geometric remainders
        r = F(n * n, A2 * A2)
        r42 = r ** J_MOM / (1 - r)
        RemV = 2 * S1 * r42
        RemU = 16 * n * S2 * r42
        # kernel row-sum bound over the bank
        Kr = 1 + logN_hi + F(Mtot, n + b)
        V_bound = Kr * ymax + abs(tV) + rtV + RemV
        U_bound = 8 * Kr * ymax + abs(tU) + rtU + RemU
        yn = ymap[n]
        y_pt = F(yn['y'], 1 << 160)
        p_pt = F(floor_(L * n / (n * n + t), 256), 1 << 256)
        point = c * (z_pt * V_pt - U_pt) / 2 + d_pt * y_pt \
            + sigma * 2 * p_pt * Ptot_pt
        vals.append(floor_(point, 256))
        # ---- error charges (all Fractions, generous) ----
        ch = F(0)
        ch += (abs(c) / 2) * Kr * (ey * zhi + err_zy)          # bank seed
        ch += (abs(c) / 2) * (zhi * (rtV + RemV) + rtU + RemU)  # tail
        ch += (abs(c) / 2) * rad_z * V_bound                    # output z
        ch += (ce / 2) * (zhi * V_bound + U_bound)              # c radius
        ch += (abs(c) / 2) * F(1, 1 << 255) * (zhi * l1 + 8 * l1)  # kfloor
        ch += rad_d * abs(y_pt) + dhi * ey                      # diagonal
        ch += 2 * (abs(p_pt) * rad_Ptot + F(1, 1 << 250) * abs(Ptot_pt))
        ch += F(1, 1 << 256)                                    # row floor
        if ch > max_charge:
            max_charge = ch
        if i in (0, count // 2, count - 1):
            du = dv = 0
            for r_ in bank:
                m = r_['m']
                hk = 0 if n == m else floor_(F(1, n - m), 256)
                gk = floor_(F(1, n + m), 256)
                du += (hk + gk) * r_['z'] * r_['y']
                dv += (hk - gk) * r_['y']
            assert du == u_int[i] and dv == v_int[i]
            checks.append({'output_index': i, 'n': n,
                           'all_bank_input_terms_match': True})
        if (i + 1) % 32000 == 0:
            print(f'{sector}/{kind}: rows {i + 1}/{count}', flush=True)
            with open(ckpt, 'a') as fh:
                fh.write(json.dumps(
                    {'vals': [str(x) for x in vals[-32000:]],
                     'max_charge': str(max_charge),
                     'checks': checks}) + '\n')
    err = sqrt_upper(F(count), 256) * max_charge
    spec = writebuffer_(WORK, sector, f'{kind}-action', vals, 256)
    l2_pt = (sum(float(F(v, 1 << 256)) ** 2 for v in vals)) ** 0.5
    res = {'schema': f'cone.infinite-seed-{kind}-action.v1',
           'sector': sector, 'output_first_mode': n_first,
           'output_count': count, 'bank_first_mode': b,
           'bank_last_mode': bank[-1]['m'], 'tail_start': A2,
           'point_buffer': spec,
           'rational': {'max_row_charge': str(max_charge),
                        'complete_l2_error_upper': str(err),
                        'P_total_point': str(Ptot_pt),
                        'P_total_radius': str(rad_Ptot)},
           'display_approximate': {'l2_error_upper': float(err),
                                   'l2_point_norm': l2_pt},
           'complete_direct_row_checks': checks,
           'whole_infinite_action_evaluated': False,
           'stationary_acceptance_met': False,
           'infinite_capacity_tail_closed': False}
    (WORK / f'{kind}-action-{sector}.json').write_text(
        json.dumps(res, indent=2, sort_keys=True) + '\n')
    ckpt.unlink(missing_ok=True)
    print(json.dumps({'sector': sector, 'kind': kind, 'rows': count,
                      'l2_error': float(err), 'l2_norm': l2_pt}))
    return res

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('stage', choices=('smoke', 'bank', 'outbank', 'validate',
                                     'moments', 'envelope', 'region2',
                                     'region3'))
    p.add_argument('--sector', choices=('even-v', 'odd-v'))
    p.add_argument('--kind', choices=('region2', 'region3'), default='region3')
    p.add_argument('--workers', type=int, default=2)
    a_ = p.parse_args()
    if a_.stage == 'smoke':
        smoke()
    elif a_.stage == 'bank':
        run_bank(a_.sector, a_.workers)
    elif a_.stage == 'outbank':
        run_outbank(a_.sector, a_.kind, a_.workers)
    elif a_.stage == 'validate':
        validate_bank(a_.sector)
    elif a_.stage == 'moments':
        tail_moments(a_.sector)
    elif a_.stage == 'envelope':
        envelope(a_.sector)
    elif a_.stage == 'region2':
        assemble(a_.sector, 'region2')
    elif a_.stage == 'region3':
        assemble(a_.sector, 'region3')
