#!/usr/bin/env python3
"""v14.819 task 3 closure: (i) rigorous uniform remainder bound for
N*C(N) - c_inf from the SIGNED moments (sharpens the lossy A_1/A_2
form of the handoff sec.1 by ~3 orders at F2 scales); (ii) empirical
accounting: the observed gap NC_emp - c_inf over the F2 top octave
vs the sharp identity's leading terms, block by block.

Identity (v14.819 sec.1, exact): with M_k = sum_j x_j m_j^k,
M_zk = sum_j x_j z_j m_j^k, M = max_j m_j, N > M:
  C(N) - c_inf/N = c*z_N*sum_j x_j m_j/(N^2-m_j^2)
                   - (c/N)*sum_j x_j z_j m_j^2/(N^2-m_j^2)
                   - alpha*L*P*t/(N*(N^2+t))
and 1/(N^2-m^2) = 1/N^2 + m^2/(N^2 (N^2-m^2)) gives the split
  sum_j x_j m_j/(N^2-m_j^2)  = M_1/N^2 + R3,  |R3| <= A_3/(N^2 (N^2-M^2))
  sum_j x_j z_j m_j^2/(N^2-m_j^2) = M_z2/N^2 + R4, |R4| <= A_4/(N^2 (N^2-M^2))
with A_k = sum |x_j| m_j^k, A_zk = sum |x_j z_j| m_j^k (dyadic points).
Hence |N*C(N) - c_inf| <= B(N) :=
  c*Zbar*(|M_1|/N + A_3/(N (N^2-M^2)))
  + c*(|M_z2| + A_4/(N^2-M^2))/N^2 + |alpha| L P t/(N^2+t).
"""
import json, sys
sys.set_int_max_str_digits(1000000)
from fractions import Fraction as F
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mz_eval as mz

S_BIG = 1 << 256
BLK = 1 << 16


def z_float(n, sigma):
    tot = np.pi / 2 + (1 - 4 * sigma * (1 / np.e) / (1 - np.exp(-4))) \
        / (n * np.pi)
    for q in (2, 3, 4, 5, 7):
        w = np.log(2) / 2 if q == 4 else np.log(q) / np.sqrt(q)
        tot = tot + 2 * w * np.sin(n * np.pi * np.log(q) / 2)
    return tot


def abs_moments(sector):
    s, start, components, pins = mz.changed.load_components(
        *mz.ROOTS, sector)
    A3 = F(0); A4 = F(0); Mmax = 0
    for cpt in components:
        xv, zv = cpt['x']['values'], cpt['z']['values']
        xb, zb = cpt['x']['bits'], cpt['z']['bits']
        off = cpt['offset']
        a3 = 0; a4 = 0
        for j, (x, z) in enumerate(zip(xv, zv)):
            m = 2 * (off + j) + start
            a3 += abs(x) * m ** 3
            a4 += abs(x * z) * m ** 4
            if m > Mmax:
                Mmax = m
        A3 += F(a3, 1 << xb)
        A4 += F(a4, 1 << (xb + zb))
    return A3, A4, Mmax


def run(sector):
    d = json.loads((HERE / f'mz-{sector}.json').read_text())
    r = json.loads((HERE / f'remainder-{sector}.json').read_text())
    R = d['rational']; RR = r['rational']
    c = F(R['c']); alpha = F(R['alpha']); L = F(R['L']); P = F(R['P'])
    t = F(R['t']); c_inf = F(R['c_inf'])
    M1 = F(RR['M_1']); Mz2 = F(RR['M_z2']); Zbar = F(RR['Zbar'])
    start = d['start']; shift = 0 if sector == 'even-v' else 1
    sigma = 1 if sector == 'even-v' else -1

    A3, A4, Mmax = abs_moments(sector)
    cf, M1f, Mz2f = float(c), float(M1), float(Mz2)
    Zf, A3f, A4f = float(Zbar), float(A3), float(A4)
    pole = abs(float(alpha)) * float(L) * float(P) * float(t)

    def bound(N):
        N = float(N)
        return (cf * Zf * (abs(M1f) / N + A3f / (N * (N * N - Mmax ** 2)))
                + cf * (abs(Mz2f) + A4f / (N * N - Mmax ** 2)) / N ** 2
                + pole / (N * N + float(t)))

    # empirical per-block NC + predicted remainder, mz_eval block set
    cert = json.loads((mz.WORK / f'far-compact-{sector}-F2.json')
                      .read_text())
    pb = cert['point_buffer']
    raw = (mz.WORK / pb['file']).read_bytes()
    w, count = pb['width'], pb['count']
    first = cert.get('first_output_mode') or cert['output_first_mode']
    vals = np.array([int.from_bytes(raw[i:i + w], 'little', signed=True)
                     for i in range(0, len(raw), w)], dtype=object)
    rows = []
    gaps = []
    for b0 in range(count // 2, count - BLK + 1, BLK):
        seg = np.array([float(v) for v in vals[b0:b0 + BLK]]) / S_BIG
        n = first + 2 * (b0 + np.arange(BLK))
        N = n - shift
        nc_blk = float(np.mean(seg * N))
        zbar_blk = float(np.mean(z_float(n.astype(np.float64), sigma)))
        pred = (cf * float(np.mean(z_float(n.astype(np.float64), sigma)
                                   / N)) * M1f
                - cf * Mz2f * float(np.mean(1.0 / N ** 2))
                - float(alpha) * float(L) * float(P) * float(t)
                * float(np.mean(1.0 / (N ** 2 + float(t)))))
        rows.append({'block_start_row': b0, 'N_mean': float(np.mean(N)),
                     'NC_block': nc_blk, 'zbar_block': zbar_blk,
                     'pred_gap': pred, 'obs_gap': nc_blk - float(c_inf),
                     'resid': (nc_blk - float(c_inf)) - pred})
        gaps.append(nc_blk - float(c_inf))
    out = {
        'schema': 'cone.far-coefficient-task3-validation.v1',
        'handoff': 'v14.819 task 3',
        'sector': sector,
        'c_inf_float': float(c_inf),
        's_inf_target_float': float(F(d['rational']['s_inf_target'])),
        'A_3_float': A3f, 'A_z4_float': A4f, 'M_max_mode': Mmax,
        'bound_at': {str(N): bound(N) for N in
                     (2 * Mmax, 14500000, 10 ** 8, 10 ** 9)},
        'lossy_A1A2_bound_at_14500000': float(
            abs(c) * (Zbar * F(R['A_1']) / 14500000
                      + F(R['A_2']) / 14500000 ** 2) / F(3, 4)),
        'blocks': rows,
        'mean_obs_gap': float(np.mean(gaps)),
        'mean_pred_gap': float(np.mean([x['pred_gap'] for x in rows])),
        'max_abs_block_resid': float(np.max([abs(x['resid'])
                                             for x in rows])),
    }
    (HERE / f'task3-{sector}.json').write_text(
        json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'sector': sector, 'A_3': A3f, 'A_z4': A4f,
                      'M_max': Mmax,
                      'bound@2M': bound(2 * Mmax),
                      'bound@1.45e7': bound(14500000),
                      'bound@1e8': bound(10 ** 8),
                      'mean_obs_gap': out['mean_obs_gap'],
                      'mean_pred_gap': out['mean_pred_gap'],
                      'max_block_resid': out['max_abs_block_resid'],
                      'NC_emp_check': float(np.mean(
                          [x['NC_block'] for x in rows]))}, indent=1))


if __name__ == '__main__':
    for sec in ('even-v', 'odd-v'):
        run(sec)
    print('DONE')
