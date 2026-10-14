#!/usr/bin/env python3
"""Sandbox evaluator: ORIGINAL infinite-seed-only action on the gap rows
1040385..2080765 (even-v) / 1040386..2080766 (odd-v), per Lane A HANDOFF
v14.351. Bank [b, T) with T = 4161531/4161532 (endpoint ratio <= 1/4 at
the final gap row); tail beyond T by 42 exact moments subtracted from the
v14.263 b-start master bank. Self rows are EXCLUDED from the offdiagonal
channels using the same represented reciprocal (floor(1/(2n), 256))
before the raw diagonal is added (v14.351 constraint; cf. v14.354).
No source/front/lift/refined-Near/finite-patch content: seed only.
"""
import argparse, gc, hashlib, json, sys, time
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'laneA_modules'))
sys.path.insert(0, str(Path(__file__).parent))
from sandbox_region23_evaluator import (
    J_MOM, R, WORK as WORK1, floor_, load_bank, load_master_moments,
    load_source, physical_constants, seed_row, sqrt_upper, out_row,
    channels_gen, L1_bank, P_bank_err)

WORK = Path(__file__).parent / 'gap351_work'
WORK.mkdir(exist_ok=True)


def gap_params(sector):
    start = 1 if sector == 'even-v' else 2
    b = 512000 + start
    a = 2 * b + b % 2
    G0 = 1040384 + start          # first gap output (step 2)
    G1 = 2080764 + start          # last gap output
    T = 4161530 + start           # first tail mode (same parity)
    return start, b, a, G0, G1, T


# ------------------------------------------------------------ bank segment 2
def seg_first_mode(sector):
    """First bank2 mode: two past the ACTUAL last stage-1 bank mode
    (parity-safe; the v1 formula (2a-1)+2 was wrong for odd-v, whose
    stage-1 bank ends at 2a-2)."""
    return load_bank(sector)[-1]['m'] + 2


def bank2_chunk(args):
    sector, chunk_id, js = args
    start, b, a, G0, G1, T = gap_params(sector)
    d = next(x for x in load_source()['cases'] if x['sector'] == sector)
    _, _, L, t = physical_constants(start)
    seg_first = seg_first_mode(sector)
    assert (seg_first - b) % 2 == 0
    rows = []
    for j in js:
        m = seg_first + 2 * j
        mm, yp, zp, pp, ye, ze = seed_row(m, d, start, L, t)
        rows.append({'m': mm, 'y': yp, 'z': zp, 'p': pp,
                     'ye': str(ye), 'ze': str(ze)})
    return sector, chunk_id, rows


def run_bank2(sector, workers=1, chunk_size=4096):
    from multiprocessing import Pool
    start, b, a, G0, G1, T = gap_params(sector)
    seg_first = seg_first_mode(sector)
    total = (T - 2 - seg_first) // 2 + 1
    out = WORK / f'bank2-{sector}.jsonl'
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)['chunk'])
    chunks = {j0 // chunk_size: list(range(j0, min(j0 + chunk_size, total)))
              for j0 in range(0, total, chunk_size)
              if j0 // chunk_size not in done}
    print(f'{sector}: bank2 modes={total} ({seg_first}..{T - 2}), '
          f'done={len(done)}, remaining={len(chunks)}', flush=True)
    if not chunks:
        return
    t0 = time.time()
    with Pool(workers) as pool:
        for sector_, cid, rows in pool.imap_unordered(
                bank2_chunk, [(sector, cid, js) for cid, js in chunks.items()]):
            with out.open('a') as f:
                f.write(json.dumps({'chunk': cid, 'rows': rows}) + '\n')
            print(f'{sector}: bank2 chunk {cid} ({time.time() - t0:.0f}s)',
                  flush=True)


def load_full_bank(sector):
    start, b, a, G0, G1, T = gap_params(sector)
    rows = {r['m']: r for r in load_bank(sector)}
    p2 = WORK / f'bank2-{sector}.jsonl'
    for line in p2.read_text().splitlines():
        if line.strip():
            for r in json.loads(line)['rows']:
                rows[r['m']] = r
    bank = [rows[m] for m in sorted(rows)]
    assert bank[0]['m'] == b and bank[-1]['m'] == T - 2
    assert len(bank) == (T - 2 - b) // 2 + 1
    assert all(bank[i + 1]['m'] - bank[i]['m'] == 2
               for i in range(len(bank) - 1))
    return bank


# ------------------------------------------------------------------ outbank
def out_chunk(args):
    sector, cid, ns = args
    return sector, cid, [out_row(n) for n in ns]


def run_outbank(sector, workers=1, chunk_size=2048):
    from multiprocessing import Pool
    start, b, a, G0, G1, T = gap_params(sector)
    ns = list(range(G0, G1 + 1, 2))
    out = WORK / f'out-gap-{sector}.jsonl'
    done = set()
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)['chunk'])
    chunks = {j0 // chunk_size: ns[j0:j0 + chunk_size]
              for j0 in range(0, len(ns), chunk_size)
              if j0 // chunk_size not in done}
    print(f'{sector}: gap outbank rows={len(ns)}, done={len(done)}, '
          f'remaining={len(chunks)}', flush=True)
    if not chunks:
        return
    t0 = time.time()
    with Pool(workers) as pool:
        for sector_, cid, rows in pool.imap_unordered(
                out_chunk, [(sector, cid, js) for cid, js in chunks.items()]):
            with out.open('a') as f:
                f.write(json.dumps({'chunk': cid, 'rows': rows}) + '\n')
            print(f'{sector}: out chunk {cid} ({time.time() - t0:.0f}s)',
                  flush=True)


def load_outbank_gap(sector):
    rows = {}
    for line in (WORK / f'out-gap-{sector}.jsonl').read_text().splitlines():
        if line.strip():
            for r in json.loads(line)['rows']:
                rows[r['n']] = r
    return rows


# ------------------------------------------------------------- tail moments
def tail_moments_T(sector):
    """U_j(T), V_j(T), P(T) intervals by subtraction of the full bank
    [b, T) from the v14.263 b-start master bank (same construction and
    radius accounting as the v14.292 tail_moments, longer bank)."""
    start, b, a, G0, G1, T = gap_params(sector)
    bank = load_full_bank(sector)
    ey = max(F(r['ye']) for r in bank)
    ez = max(F(r['ze']) for r in bank)
    ymax = max(abs(F(r['y'], 1 << 160)) for r in bank)
    err_zy = 8 * ey + ymax * ez + ey * ez
    Ubar, Vbar, Ptail = load_master_moments(sector)
    out = {'sector': sector, 'T': T, 'U': [], 'V': []}
    NB = len(bank)
    for j in range(J_MOM):
        accU = 0; accV = 0
        for r in bank:
            m = r['m']
            accU += (r['z'] * r['y'] * (1 << 2048)) // m ** (2 * j + 2)
            accV += (r['y'] * (1 << 2048)) // m ** (2 * j + 1)
        sU = F(accU, 1 << (2048 + 320))
        sV = F(accV, 1 << (2048 + 160))
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
        print(f'{sector}: moment {j + 1}/{J_MOM}', flush=True)
    sP = F(sum(r['p'] * r['y'] for r in bank), 1 << 416)
    radP = (Ptail[1] - Ptail[0]) / 2 + \
        (2 * L1_bank(bank) * F(1, 1 << 256) + P_bank_err(bank))
    midP = (Ptail[0] + Ptail[1]) / 2 - sP
    out['P'] = (str(midP - radP), str(midP + radP))
    (WORK / f'momentsT-{sector}.json').write_text(json.dumps(out))
    print(f'{sector}: tail moments at T={T} written')
    return out


# ----------------------------------------------------------------- assemble
def channels_chunked(y, zy, m_first, n_first, count, seg=400000):
    """channels_gen over bank segments, summed exactly. The channel map
    is linear in the input bank and channels_gen already accepts an
    arbitrary segment start, so the integer outputs are identical to
    the single full-bank call; only the peak convolution workspace
    shrinks (the full-bank call was SIGKILLed twice on 2026-10-13:
    1.82M modes x 520k outputs on a 7.7 GB box)."""
    M = len(y)
    u = [0] * count
    v = [0] * count
    for j0 in range(0, M, seg):
        j1 = min(j0 + seg, M)
        us, vs = channels_gen(y[j0:j1], zy[j0:j1], m_first + 2 * j0,
                              n_first, count)
        for i in range(count):
            u[i] += us[i]
            v[i] += vs[i]
        del us, vs
        gc.collect()
        print(f'channels segment [{j0}, {j1}) done', flush=True)
    return u, v


def assemble_gap(sector):
    start, b, a, G0, G1, T = gap_params(sector)
    sigma = 1 if start == 1 else -1
    count = (G1 - G0) // 2 + 1
    assert count == 520191
    bank = load_full_bank(sector)
    mom = json.loads((WORK / f'momentsT-{sector}.json').read_text())
    assert mom['T'] == T
    U = [(F(lo), F(hi)) for lo, hi in mom['U']]
    V = [(F(lo), F(hi)) for lo, hi in mom['V']]
    Plo, Phi_ = F(mom['P'][0]), F(mom['P'][1])
    Ptail_pt = (Plo + Phi_) / 2
    rad_Ptail = (Phi_ - Plo) / 2
    outb = load_outbank_gap(sector)
    # ---- tail-series truncation (defect fix, 2026-10-14) ----
    # The master-minus-bank moment midpoints are construction noise
    # once the interval radius reaches the midpoint (even-v: j >= 20);
    # evaluated anyway, the j-th noise term is amplified by n**(2j)
    # and poisons large output rows (first assembly: last row -1435
    # vs true ~1e-6; the honest radius sum reported error 6.9e8).
    # Retain only informative terms and bound the omitted remainder
    # geometrically (RemV/RemU with r**J in place of r**42; the S1/S2
    # envelopes bound sum_{m>T} |y_m|/m^2 resp. |zy_m|/m^3 sums and
    # T**(2J) * M_J <= those sums for every J, so the same envelopes
    # serve at any truncation point).
    def _informative_terms(moms, n_max):
        J = 0
        for j, (lo, hi) in enumerate(moms):
            mid = (lo + hi) / 2
            rad = (hi - lo) / 2
            if rad > abs(mid):
                break
            if F(n_max * n_max) ** j * rad > F(1, 10 ** 13):
                break
            J = j + 1
        return J
    J_V = _informative_terms(V, G1)
    J_U = _informative_terms(U, G1)
    JST = min(J_V, J_U)
    assert JST >= 8, (sector, J_V, J_U)
    print(f'{sector}: tail series truncated at J*={JST} '
          f'(informative terms: V {J_V}, U {J_U} of {J_MOM})',
          flush=True)
    c, ce, L, t = physical_constants(start)
    y = [r['y'] for r in bank]
    zy = [r['z'] * r['y'] for r in bank]
    ey = max(F(r['ye']) for r in bank)
    ez = max(F(r['ze']) for r in bank)
    ymax = max(abs(F(r['y'], 1 << 160)) for r in bank)
    err_zy = 8 * ey + ymax * ez + ey * ez
    l1 = L1_bank(bank)
    Pbank = F(sum(r['p'] * r['y'] for r in bank), 1 << 416)
    rad_Pbank = P_bank_err(bank) + l1 * F(1, 1 << 256)
    Ptot_pt = Pbank + Ptail_pt
    rad_Ptot = rad_Pbank + rad_Ptail
    bank_count = len(bank)
    del bank            # records no longer needed; frees ~2 GB before the
    gc.collect()        # channel convolutions (peak-memory fix)
    print(f'{sector}: channels over {bank_count} bank modes, '
          f'{count} outputs (chunked)...', flush=True)
    u_int, v_int = channels_chunked(y, zy, b, G0, count)
    print(f'{sector}: channels done', flush=True)
    # ---- self-row exclusion (exact, same represented reciprocal) ----
    for i in range(count):
        n = G0 + 2 * i
        jn = (n - b) // 2
        gk = floor_(F(1, 2 * n), 256)
        v_int[i] += gk * y[jn]
        u_int[i] -= gk * zy[jn]
    print(f'{sector}: self rows excluded on all {count} rows', flush=True)
    env = json.loads((WORK1 / f'envelope-{sector}.json').read_text())
    C = F(env['rational']['Phi_C'])
    Mtot = bank_count
    from suzuki_certified_remote_diagonal import log_normalized
    logN_hi = log_normalized(4 * Mtot, 256)[1]
    S1 = (C / 11) * (F(1, T * T) + F(1, 2 * T))
    S2 = (C / 11) * (F(1, T ** 3) + F(1, 4 * T * T))
    vals = []
    max_charge = F(0)
    checks = []
    ckpt = WORK / f'gap-assemble-{sector}.ckpt.jsonl'
    if ckpt.exists():
        for line in ckpt.read_text().splitlines():
            if not line.strip():
                continue
            try:
                blk = json.loads(line)
            except json.JSONDecodeError:
                break
            vals.extend(int(x) for x in blk['vals'])
            mc = F(blk['max_charge'])
            if mc > max_charge:
                max_charge = mc
            checks = blk['checks']
        print(f'{sector}: resumed, {len(vals)} rows restored', flush=True)
    for i in range(len(vals), count):
        n = G0 + 2 * i
        ob = outb[n]
        zlo, zhi = F(ob['zlo']), F(ob['zhi'])
        z_pt = (zlo + zhi) / 2
        rad_z = (zhi - zlo) / 2
        dlo, dhi = F(ob['dlo']), F(ob['dhi'])
        d_pt = (dlo + dhi) / 2
        rad_d = (dhi - dlo) / 2
        tV = F(0); tU = F(0); rtV = F(0); rtU = F(0)
        npow = F(1)
        for j in range(JST):
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
        r = F(n * n, T * T)
        rJ = r ** JST / (1 - r)
        RemV = 2 * S1 * rJ
        RemU = 16 * n * S2 * rJ
        Kr = 1 + logN_hi + F(Mtot, n + b)
        V_bound = Kr * ymax + abs(tV) + rtV + RemV
        U_bound = 8 * Kr * ymax + abs(tU) + rtU + RemU
        y_pt = F(y[(n - b) // 2], 1 << 160)
        p_pt = F(floor_(L * n / (n * n + t), 256), 1 << 256)
        point = c * (z_pt * V_pt - U_pt) / 2 + d_pt * y_pt \
            + sigma * 2 * p_pt * Ptot_pt
        vals.append(floor_(point, 256))
        ch = F(0)
        ch += (abs(c) / 2) * Kr * (ey * zhi + err_zy)
        ch += (abs(c) / 2) * (zhi * (rtV + RemV) + rtU + RemU)
        ch += (abs(c) / 2) * rad_z * V_bound
        ch += (ce / 2) * (zhi * V_bound + U_bound)
        ch += (abs(c) / 2) * F(1, 1 << 255) * (zhi * l1 + 8 * l1)
        ch += rad_d * abs(y_pt) + dhi * ey
        ch += 2 * (abs(p_pt) * rad_Ptot + F(1, 1 << 250) * abs(Ptot_pt))
        ch += F(1, 1 << 256)
        if ch > max_charge:
            max_charge = ch
        if i in (0, count // 2, count - 1):
            # from-definition direct check: bank sums with m != n in BOTH
            # kernels, integer-exact against the corrected channels
            du = dv = 0
            for j_ in range(len(y)):
                m = b + 2 * j_
                if m == n:
                    continue
                hk = floor_(F(1, n - m), 256)
                gk = floor_(F(1, n + m), 256)
                du += (hk + gk) * zy[j_]
                dv += (hk - gk) * y[j_]
            assert du == u_int[i] and dv == v_int[i], (sector, i)
            checks.append({'output_index': i, 'n': n,
                           'all_bank_input_terms_match_m_ne_n': True})
            print(f'{sector}: direct check row {i} (n={n}) OK', flush=True)
        if (i + 1) % 26000 == 0:
            print(f'{sector}/gap: rows {i + 1}/{count}', flush=True)
            with open(ckpt, 'a') as fh:
                fh.write(json.dumps(
                    {'vals': [str(x) for x in vals[-26000:]],
                     'max_charge': str(max_charge),
                     'checks': checks}) + '\n')
    err = sqrt_upper(F(count), 256) * max_charge
    width = max(1, (max(abs(x).bit_length() for x in vals) + 8) // 8)
    raw = b''.join(x.to_bytes(width, 'little', signed=True) for x in vals)
    (WORK / f'{sector}-gap-action.bin').write_bytes(raw)
    spec = {'file': f'{sector}-gap-action.bin', 'bits': 256, 'width': width,
            'count': len(vals), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}
    l2_pt = (sum(float(F(v, 1 << 256)) ** 2 for v in vals)) ** 0.5
    rend = F(G1 * G1, T * T)
    res = {'schema': 'cone.infinite-seed-gap-action.v1',
           'sector': sector, 'output_first_mode': G0,
           'output_last_mode': G1, 'output_count': count,
           'bank_first_mode': b, 'bank_last_mode': T - 2,
           'bank_count': bank_count, 'tail_start': T,
           'endpoint_ratio_at_final_output': str(rend),
           'endpoint_ratio_le_quarter': rend <= F(1, 4),
           'self_rows_excluded_with_represented_reciprocal': True,
           'tail_series_terms_used': JST,
           'tail_series_moments_computed': J_MOM,
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
    (WORK / f'gap-action-{sector}.json').write_text(
        json.dumps(res, indent=2, sort_keys=True) + '\n')
    ckpt.unlink(missing_ok=True)
    print(json.dumps({'sector': sector, 'rows': count,
                      'l2_error': float(err), 'l2_norm': l2_pt}))
    return res


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('stage', choices=('bank2', 'outbank', 'moments', 'gap'))
    p.add_argument('--sector', choices=('even-v', 'odd-v'), required=True)
    p.add_argument('--workers', type=int, default=1)
    a_ = p.parse_args()
    if a_.stage == 'bank2':
        run_bank2(a_.sector, a_.workers)
    elif a_.stage == 'outbank':
        run_outbank(a_.sector, a_.workers)
    elif a_.stage == 'moments':
        tail_moments_T(a_.sector)
    elif a_.stage == 'gap':
        assemble_gap(a_.sector)
