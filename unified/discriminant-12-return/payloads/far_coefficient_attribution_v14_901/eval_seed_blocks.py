#!/usr/bin/env python3
"""v14.819 task 2 (empirical side, block version): block means of
N*S(N) for the TRUE seed action (model inputs over ALL m >= b,
m != n) at block centers from the F1 window to n ~ 2e8, widening
the ln ln lever ~3.5x past the composed buffers. Blocks of 257
consecutive same-parity rows kill the D_osc / z_n oscillation
(block-mean residual <~ 3e-3); the m-grid is built once per block
and shared by all its output rows. m > K*n_max tail: smooth
nonprime-mean integrals (as in eval_seed_large.py) + negligible
Dirichlet-bound oscillatory parts. For centers inside F1/F2 the
buffer mean over the SAME rows is printed alongside (coverage).
"""
import json, sys, time
sys.set_int_max_str_digits(1000000)
from fractions import Fraction as F
from math import fsum, log, pi, sqrt, e
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
FAR = HERE.parent
D12 = FAR.parents[1]
for p in (str(FAR), str(D12 / 'laneA_modules'), str(D12),
          str(D12 / 'dm490' / 'ca544'), str(D12 / 'dm490' / 'ca544' / 'modules')):
    sys.path.insert(0, p)
from sandbox_region23_evaluator import out_row, physical_constants, \
    load_source

SRC = load_source()
S_BIG = 1 << 256
W_Q = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
TH_Q = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}
S0 = (1 / e) / (1 - np.exp(-4))


def z_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.full(n.shape, pi / 2) + (1 - 4 * sigma * S0) / (n * pi)
    for q in (2, 3, 4, 5, 7):
        tot = tot + 2 * W_Q[q] * np.sin(n * TH_Q[q])
    return tot


def d_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.log(n / 4) - 1.0 / (2 * n) \
        + 2 * (1.0 if int(n[0]) % 2 == 0 else -1.0) / (n * pi) ** 2
    # (-1)^n is constant on a parity block: use per-row parity
    sgn = np.where((n % 2) == 0, 1.0, -1.0)
    tot = np.log(n / 4) - 1.0 / (2 * n) + 2 * sgn / (n * pi) ** 2
    for q in (2, 3, 4, 5, 7):
        tot = tot - W_Q[q] * (2 - log(q)) * (
            np.cos(n * TH_Q[q]) + (2 / (n * pi)) * np.sin(n * TH_Q[q]))
    return tot


class Sector:
    def __init__(self, sector):
        self.sector = sector
        self.start = 1 if sector == 'even-v' else 2
        self.sigma = 1 if sector == 'even-v' else -1
        self.b = 512000 + self.start
        case = next(x for x in SRC['cases'] if x['sector'] == sector)
        self.W = np.array([float(F(r['W_coefficient_rational']))
                           for r in case['far_channels']])
        self.A = np.array([float(F(r['A_coefficient_rational']))
                           for r in case['far_channels']])
        cc, ce, LL, tt = physical_constants(self.start)
        self.c, self.L, self.t = float(cc), float(LL), float(tt)
        self._P = None

    def model(self, m):
        j = np.arange(len(self.W), dtype=np.float64)
        pw = np.power(m[:, None], (-(2 * j + 1))[None, :])
        pv = np.power(m[:, None], (-(2 * j + 2))[None, :])
        w = pw @ self.W
        v = pv @ self.A
        z = z_float(m, self.sigma)
        shift = 1.0 / (m * (m - 1)) if self.sigma == -1 else 0.0
        y = (w - v * z + shift) / np.log(m / 4)
        return y, y * z

    def p_tot(self):
        if self._P is not None:
            return self._P
        tot = []
        M = 200_000_000
        m = np.arange(self.b, M, 2, dtype=np.float64)
        for i0 in range(0, len(m), 2_000_000):
            mb = m[i0:i0 + 2_000_000]
            y, _ = self.model(mb)
            tot.append(float(np.sum(self.L * mb / (mb * mb + self.t) * y)))
        tail = self.L * self.W[0] / (M * log(M / 4)) / 2 \
            * (1 + 1 / log(M / 4))
        self._P = fsum(tot) + tail
        return self._P

    def block(self, center, nrows=257, K=5):
        start, b, sigma = self.start, self.b, self.sigma
        rows = center + 2 * np.arange(-(nrows // 2), nrows // 2 + 1)
        n = rows.astype(np.float64)
        nmax = float(rows[-1])
        M = int(K * nmax) + start
        V = np.zeros(len(rows))
        U = np.zeros(len(rows))
        CH = 1_000_000
        G = 32
        for m0 in range(b, M, CH):
            mb = np.arange(m0, min(m0 + CH, M), 2, dtype=np.float64)
            y, zy = self.model(mb)
            msq = mb * mb
            for g0 in range(0, len(rows), G):
                nn = n[g0:g0 + G]
                den = nn[:, None] ** 2 - msq[None, :]
                kv = (2 * mb)[None, :] / den
                ku = (2 * nn)[:, None] / den
                # exclude m == n_i (den == 0 -> inf): zero those terms
                for ii, nv in enumerate(nn):
                    j = int((nv - m0) // 2)
                    if 0 <= j < len(mb) and mb[j] == nv:
                        kv[ii, j] = 0.0
                        ku[ii, j] = 0.0
                V[g0:g0 + G] += kv @ y
                U[g0:g0 + G] += ku @ zy
        # smooth tails beyond M (per-row n)
        W0 = self.W[0]
        lM = log(M / 4)
        Ut = -(pi * W0 / (4 * lM)) * np.log(1.0 / (1 - (n / M) ** 2)) / n
        Vt = -(W0 / (2 * lM)) * np.log((M + n) / (M - n)) / n
        V = V + Vt
        U = U + Ut
        z_n = z_float(n, sigma)
        d_n = d_float(n, sigma)
        y_n = self.model(n)[0]
        p_n = self.L * n / (n * n + self.t)
        Svals = self.c * (z_n * V - U) / 2 + d_n * y_n \
            + sigma * 2 * p_n * self.p_tot()
        NS = rows * Svals
        out = {'sector': self.sector, 'center': int(center),
               'nrows': nrows, 'NS_mean': float(np.mean(NS)),
               'NS_min': float(np.min(NS)), 'NS_max': float(np.max(NS)),
               'nV_mean': float(np.mean(rows * V)),
               'nU_mean': float(np.mean(rows * U)),
               'ndiag_mean': float(np.mean(rows * d_n * y_n)),
               'rows': [int(r) for r in rows],
               'NS_rows': [float(v) for v in NS]}
        # buffer comparison on the same rows, if inside F1/F2
        F0, T2, Sb = 4161532 + start, 8323062 + start, 16646126 + start
        for cls, lo, hi in (('F1', F0, T2), ('F2', T2, Sb)):
            if lo <= rows[0] and rows[-1] < hi:
                cert = json.loads((FAR / 'work'
                                   / f'far-seed-{self.sector}-{cls}.json')
                                  .read_text())
                pb = cert['point_buffer']
                raw = (FAR / 'work' / pb['file']).read_bytes()
                wdt = pb['width']
                bvals = []
                for r in rows:
                    i = (int(r) - cert['output_first_mode']) // 2
                    bvals.append(int.from_bytes(
                        raw[i * wdt:(i + 1) * wdt], 'little',
                        signed=True) / S_BIG)
                out[f'buffer_NS_mean_{cls}'] = float(np.mean(
                    rows * np.array(bvals)))
                out[f'eval_minus_buffer_{cls}'] = out['NS_mean'] \
                    - out[f'buffer_NS_mean_{cls}']
        return out


if __name__ == '__main__':
    sector = sys.argv[1]
    sec = Sector(sector)
    st = sec.start
    centers = [6161535 + (st - 1), 12000001 + (st - 1),
               25000001 + (st - 1), 50000001 + (st - 1),
               100000001 + (st - 1), 200000001 + (st - 1)]
    results = []
    for c0 in centers:
        t0 = time.time()
        r = sec.block(c0)
        r['seconds'] = round(time.time() - t0, 1)
        results.append(r)
        print(json.dumps({k: v for k, v in r.items()
                          if k not in ('rows', 'NS_rows')}), flush=True)
        (HERE / f'blocks_{sector}.json').write_text(
            json.dumps(results, indent=1))
    print('DONE', sector)
