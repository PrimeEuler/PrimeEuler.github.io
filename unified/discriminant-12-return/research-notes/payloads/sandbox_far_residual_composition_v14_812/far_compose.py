#!/usr/bin/env python3
"""Far finite-class residual composition, v14.585 handoff actions (3)-(4),
finite part: classes F1 = [F, T2) and F2 = [T2, 2T2) per sector.

Conventions identical to the audited v14.583 DM composition
(dm490/residual554/compose_residual_v14554.py):
- residual_i = S // (first + 2i - shift) - compact_i - seed_i
  (bare source 1/n even, 1/(n-1) odd, S = 2^256)
- upper() copied verbatim (directed sqrt at the S grid)
- physical error = compact l2 error + seed l2 error + bare floor error,
  bare = upper(count)/S
- transport charges were each charged exactly once in v14.442 and are
  NOT charged again here.

Inputs (hash-pinned by their certificates):
- changed compact action evaluated on far rows: far_compact.py certs
  work/far-compact-{sector}-{F1,F2}.json (buffer widths 30 F1 / 29 F2)
- noncompact seed assembly: far-seed-{sector}-{F1,F2}.json (width 30)

Outputs per class: work/{sector}-far-residual-{F1,F2}.bin (width-30
signed LE) + work/far-residual-{sector}-{F1,F2}.json; per sector a
summary work/far-residual-{sector}-summary.json combining F1+F2 in
exact l2 quadrature against the v14.583 far headroom (q - DM_hi^2 from
dm490/residual554/work/dm-residual-{sector}.json). The F3 tail
[S, infinity) is NOT evaluated here: scope flags stay false.
"""
import argparse, hashlib, json, sys
sys.set_int_max_str_digits(1000000)
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

S = 1 << 256
HERE = Path(__file__).parent
WORK = HERE / 'work'
DM_RESID = HERE.parent / 'residual554' / 'work'
SHIFT = {'even-v': 0, 'odd-v': 1}
CLASSES = ('F1', 'F2')
CHUNK = 131072
OUT_WIDTH = 30
LIMIT30 = (1 << (8 * OUT_WIDTH - 1)) - 1  # signed 30-byte range


def upper(q):
    assert q >= 0
    n = q.numerator * S * S
    d = q.denominator
    k = isqrt(n // d)
    if k * k * d < n:
        k += 1
    return F(k, S)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 23), b''):
            h.update(block)
    return h.hexdigest()


def decode(raw, width, count):
    assert len(raw) == width * count
    return [int.from_bytes(raw[i:i + width], 'little', signed=True)
            for i in range(0, len(raw), width)]


def load_cert(path):
    return json.loads(Path(path).read_text())


def class_inputs(sector, cls):
    cc = load_cert(WORK / f'far-compact-{sector}-{cls}.json')
    sc = load_cert(WORK / f'far-seed-{sector}-{cls}.json')
    assert cc['sector'] == sector and sc['sector'] == sector
    assert cc['far_residual_evaluated'] is False
    cb, sb = cc['point_buffer'], sc['point_buffer']
    assert cb['count'] == sb['count']
    assert cc['first_output_mode'] == sc['output_first_mode']
    assert cc['last_output_mode'] == sc['output_last_mode']
    return cc, sc


def spot_check(sector, cls, first, shift, count, cwidth, swidth, rpath):
    rows = {0, 1, 2, count // 3, count // 2, count - 2, count - 1}
    rows |= {(k * 2654435761) % count for k in range(1, 17)}
    rows = sorted(rows)
    cpath = WORK / f'{sector}-far-compact-{cls}.bin'
    spath = WORK / f'{sector}-far-seed-{cls}.bin'
    with open(cpath, 'rb') as fc, open(spath, 'rb') as fs, \
            open(rpath, 'rb') as fr:
        for i in rows:
            fc.seek(i * cwidth)
            c = int.from_bytes(fc.read(cwidth), 'little', signed=True)
            fs.seek(i * swidth)
            s = int.from_bytes(fs.read(swidth), 'little', signed=True)
            fr.seek(i * OUT_WIDTH)
            r = int.from_bytes(fr.read(OUT_WIDTH), 'little', signed=True)
            assert r + c + s == S // (first + 2 * i - shift), \
                f'spot check failed {sector} {cls} row {i}'
    return {'rows_checked': rows, 'all_rows_match_bare_identity': True}


def compose_class(sector, cls, limit=None, outdir=None):
    outdir = outdir or WORK
    cc, sc = class_inputs(sector, cls)
    cb, sb = cc['point_buffer'], sc['point_buffer']
    count_full = cb['count']
    count = count_full if limit is None else min(limit, count_full)
    first = cc['first_output_mode']
    shift = SHIFT[sector]
    cpath, spath = WORK / cb['file'], WORK / sb['file']
    assert sha256_file(cpath) == cb['sha256'], f'compact sha {sector} {cls}'
    assert sha256_file(spath) == sb['sha256'], f'seed sha {sector} {cls}'

    rname = f'{sector}-far-residual-{cls}.bin'
    rpath = outdir / rname
    sumsq = 0
    max_abs = 0
    done = 0
    with open(cpath, 'rb') as fc, open(spath, 'rb') as fs, \
            open(rpath, 'wb') as fr:
        while done < count:
            take = min(CHUNK, count - done)
            craw = fc.read(cb['width'] * take)
            sraw = fs.read(sb['width'] * take)
            cvals = decode(craw, cb['width'], take)
            svals = decode(sraw, sb['width'], take)
            out = bytearray()
            for j, (c, s) in enumerate(zip(cvals, svals)):
                i = done + j
                r = S // (first + 2 * i - shift) - c - s
                assert -LIMIT30 <= r <= LIMIT30
                sumsq += r * r
                if abs(r) > max_abs:
                    max_abs = abs(r)
                out += r.to_bytes(OUT_WIDTH, 'little', signed=True)
                if limit is not None:
                    # exact Fraction cross-check, smoke mode only
                    ref = F(1, first + 2 * i - shift) - F(c, S) - F(s, S)
                    assert abs(F(r, S) - ref) <= F(2, S), \
                        f'fraction check failed row {i}'
            fr.write(out)
            done += take
    rsha = sha256_file(rpath)

    q = F(sumsq, S * S)
    point_hi = upper(q)
    point_lo = max(F(0), point_hi - F(1, S))
    assert point_lo * point_lo <= q <= point_hi * point_hi
    comp_error = F(cc['rational']['complete_far_compact_action_error_upper'])
    seed_error = F(sc['rational']['complete_l2_error_upper'])
    bare_error = upper(F(count)) / S
    physical_error = comp_error + seed_error + bare_error
    physical_lo = max(F(0), point_lo - physical_error)
    physical_hi = point_hi + physical_error

    checks = spot_check(sector, cls, first, shift, count,
                        cb['width'], sb['width'], rpath) \
        if limit is None else {'smoke_fraction_cross_check': True}

    out = {
        'schema': 'cone.far-residual-composition.v1',
        'handoff': 'v14.585 actions (3)-(4), finite far classes',
        'sector': sector,
        'row_class': cls,
        'output_count': count,
        'output_first_mode': first,
        'output_last_mode': first + 2 * (count - 1),
        'bare_source_formula': '1/n' if shift == 0 else '1/(n-1)',
        'compact_buffer_sha256': cb['sha256'],
        'seed_buffer_sha256': sb['sha256'],
        'compact_cert': f'far-compact-{sector}-{cls}.json',
        'seed_cert': f'far-seed-{sector}-{cls}.json',
        'residual_buffer': {'file': rname, 'bits': 256,
                            'width': OUT_WIDTH, 'count': count,
                            'bytes': count * OUT_WIDTH, 'sha256': rsha},
        'rational': {
            'point_norm_lower': str(point_lo),
            'point_norm_upper': str(point_hi),
            'compact_l2_error_upper': str(comp_error),
            'seed_l2_error_upper': str(seed_error),
            'bare_source_floor_error_upper': str(bare_error),
            'complete_physical_error_upper': str(physical_error),
            'physical_residual_lower': str(physical_lo),
            'physical_residual_upper': str(physical_hi),
        },
        'display_approximate': {
            'point_norm': float(point_hi),
            'physical_residual_upper': float(physical_hi),
            'max_abs_residual_over_S': float(F(max_abs, S)),
        },
        'direct_row_checks': checks,
        'far_finite_class_evaluated': True,
        'f3_tail_evaluated': False,
        'infinite_capacity_tail_closed': False,
        'whole_residual_acceptance_certified': False,
        'global_transport_charged_again': False,
    }
    cert_name = f'far-residual-{sector}-{cls}.json'
    (outdir / cert_name).write_text(
        json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'sector': sector, 'class': cls,
                      'rows': count,
                      'physical_upper': float(physical_hi)}))
    return out


def sector_summary(sector, f1, f2):
    dm = load_cert(DM_RESID / f'dm-residual-{sector}.json')
    dr = {k: F(v) for k, v in dm['rational'].items()}
    q = dr['beyond_gap_budget_q']
    headroom_sq = dr['far_headroom_squared']
    assert headroom_sq == q - dr['physical_residual_upper'] ** 2
    far_sq = (F(f1['rational']['physical_residual_upper']) ** 2
              + F(f2['rational']['physical_residual_upper']) ** 2)
    far_hi = upper(far_sq)
    remaining_sq = headroom_sq - far_sq
    out = {
        'schema': 'cone.far-residual-composition-sector-summary.v1',
        'handoff': 'v14.585 actions (3)-(4), finite far classes',
        'sector': sector,
        'rational': {
            'beyond_gap_budget_q': str(q),
            'dm_physical_residual_upper':
                str(dr['physical_residual_upper']),
            'far_headroom_squared_before_far': str(headroom_sq),
            'far_finite_physical_upper': str(far_hi),
            'far_finite_squared_upper': str(far_sq),
            'remaining_headroom_squared_after_finite_far':
                str(remaining_sq),
        },
        'display_approximate': {
            'far_finite_physical_upper': float(far_hi),
            'far_headroom_before_far': float(headroom_sq) ** 0.5,
            'remaining_headroom_after_finite_far':
                float(remaining_sq) ** 0.5 if remaining_sq > 0 else None,
        },
        'finite_far_within_headroom': bool(remaining_sq > 0),
        'f3_tail_evaluated': False,
        'whole_residual_acceptance_certified': False,
    }
    (WORK / f'far-residual-{sector}-summary.json').write_text(
        json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'sector': sector, 'summary': out['display_approximate']
                      | {'within_headroom':
                         out['finite_far_within_headroom']}}))
    return out


def class_done(sector, cls):
    cert_path = WORK / f'far-residual-{sector}-{cls}.json'
    if not cert_path.exists():
        return None
    cert = load_cert(cert_path)
    cc, sc = class_inputs(sector, cls)
    if cert['compact_buffer_sha256'] != cc['point_buffer']['sha256']:
        return None
    if cert['seed_buffer_sha256'] != sc['point_buffer']['sha256']:
        return None
    if sha256_file(WORK / cc['point_buffer']['file']) \
            != cc['point_buffer']['sha256']:
        return None
    if sha256_file(WORK / sc['point_buffer']['file']) \
            != sc['point_buffer']['sha256']:
        return None
    rb = cert['residual_buffer']
    rpath = WORK / rb['file']
    if not rpath.exists() or sha256_file(rpath) != rb['sha256']:
        return None
    print(json.dumps({'sector': sector, 'class': cls,
                      'skipped': 'cert + buffer verified on disk'}))
    return cert


def run_sector(sector):
    certs = {}
    for cls in CLASSES:
        certs[cls] = class_done(sector, cls) or compose_class(sector, cls)
    return sector_summary(sector, certs['F1'], certs['F2'])


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--sector', required=True,
                    choices=('even-v', 'odd-v'))
    ap.add_argument('--limit', type=int, default=None,
                    help='smoke mode: first N rows of F1 only, to work/smoke/')
    a = ap.parse_args()
    if a.limit is not None:
        smoke = WORK / 'smoke'
        smoke.mkdir(parents=True, exist_ok=True)
        compose_class(a.sector, 'F1', limit=a.limit, outdir=smoke)
        print('SMOKE OK')
    else:
        run_sector(a.sector)
