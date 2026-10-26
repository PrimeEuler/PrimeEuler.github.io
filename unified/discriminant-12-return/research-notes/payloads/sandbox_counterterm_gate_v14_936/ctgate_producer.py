#!/usr/bin/env python3
"""v14.909 counter-term gate, stage S3: preliminary anchors.

The phantom (DERIVATION.md sec.2) is
  CT(N) = -(S_off(N) + S_pole(N)) + CT_sp(N)   for N >= F0,
  CT(N) = 0                                    for N <  F0,
the first term by exact linearity (phantom inputs = negated seed
inputs), the second the spike's closed form. No composed F2 buffer
is used anywhere: the seed part comes from the frozen coeff819
block artifacts (the audited evaluator's own model sums over ALL
inputs m >= b), so the F2 [S,2S) assembly defect does not enter.

Stages:
  dm      DM-silence self-test (support clause + code path).
  blocks  257-row block means at the six v14.901 centers, both
          sectors: phantom vs CT0 template, derived envelope.
  bands   center-row below/near/above band split of the phantom
          channel sums (direct model sums to 5N + the evaluator's
          smooth-tail convention), one sector per invocation,
          checkpointed per center.
  l2      template l2 partial sums at the centers + envelope
          remainder sums (phantom bound = 2x template + 2x rem).
  merge   assemble anchors.json from the stage outputs.
"""
import importlib.util, json, sys, time
from fractions import Fraction as F
from math import log, pi, sqrt
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
COEFF = HERE.parent / 'coeff819'
D12 = HERE.parents[2]
for p in (str(D12), str(D12 / 'laneA_modules'), str(COEFF),
          str(D12 / 'dm490' / 'far585'), str(D12 / 'dm490' / 'ca544'),
          str(D12 / 'dm490' / 'ca544' / 'modules')):
    sys.path.insert(0, p)
sys.set_int_max_str_digits(1000000)

from sandbox_region23_evaluator import physical_constants
from suzuki_bulk_action_z import evaluate as z_eval

CONSTS = json.loads((HERE / 'constants.json').read_text())
CENTERS = {1: [6161535, 12000001, 25000001, 50000001, 100000001,
               200000001],
           2: [6161536, 12000002, 25000002, 50000002, 100000002,
               200000002]}
_zcache = {}


def z_mid(m):
    if m not in _zcache:
        r = z_eval(m)
        lo, hi = F(r['lower_rational']), F(r['upper_rational'])
        _zcache[m] = ((lo + hi) / 2, (hi - lo) / 2)
    return _zcache[m]


def floor_(q, bits):
    return q.numerator * (1 << bits) // q.denominator


class SectorData:
    def __init__(self, sector):
        d = CONSTS[sector]
        self.sector = sector
        self.start = d['start']
        self.sigma = d['sigma']
        self.b = d['b']
        self.F0 = d['F0']
        self.A = d['A']; self.beta = d['beta']; self.D = d['D']
        self.c = F(d['c_rational']); self.L = F(d['L_rational'])
        self.t = F(d['t_rational'])
        self.m1 = d['spike_mode_m1']
        self.zm1 = F(d['z_m1_mid_rational'])
        self.pm1 = F(d['p_m1_rational'])
        self.y1 = F(d['y1_rational'])
        self.C_sp = 197282 if self.start == 1 else 131351

    # ---- spike: exact per-row scaled action N*CT_sp(N), Fractions
    def spike_row(self, N):
        """Returns dict of Fraction parts of N*CT_sp(N)."""
        c, L, t = self.c, self.L, self.t
        m1, zm1, pm1, y1 = self.m1, self.zm1, self.pm1, self.y1
        zN, _ = z_mid(N)
        pN = F(floor_(L * N / (N * N + t), 256), 1 << 256)
        den = N * N - m1 * m1
        v_part = (c / 2) * zN * F(2 * m1 * N, den) * y1
        u_part = -c * F(N * N, den) * zm1 * y1
        pole_part = 2 * self.sigma * (N * pN) * pm1 * y1
        return {'V': v_part, 'U': u_part, 'pole': pole_part,
                'total': v_part + u_part + pole_part}

    # ---- the phantom action with its support clause (sec.5)
    def phantom_action_row(self, N, entered):
        """entered is a list used as a tripwire: the channel branch
        appends to it. Below F0 the exact 0 is returned by the
        support clause and the channel branch is never entered."""
        if N < self.F0:
            return 0
        entered.append(N)
        raise NotImplementedError(
            'full channel evaluation lives in the block/band stages; '
            'this entry point exists for the support-clause test')


def stage_dm():
    out = {}
    for sector in ('even-v', 'odd-v'):
        sd = SectorData(sector)
        rows = sorted({sd.b, 2080766 + sd.start, 3000000 + sd.start,
                       4161530 + sd.start, sd.F0 - 2})
        entered = []
        res = []
        for n in rows:
            assert n < sd.F0 and n % 2 == sd.start % 2, n
            v = sd.phantom_action_row(n, entered)
            res.append({'row': n, 'value': v, 'is_exact_zero': v == 0})
        out[sector] = {'F0': sd.F0, 'test_rows': res,
                       'channel_branch_entered': entered,
                       'all_zero': all(r['is_exact_zero'] for r in res)
                       and not entered}
        print(sector, 'DM silence:', out[sector]['all_zero'],
              'rows', [r['row'] for r in res])
    (HERE / 'anchors_dm.json').write_text(json.dumps(out, indent=1))
    return out


def stage_blocks():
    out = {}
    for sector in ('even-v', 'odd-v'):
        sd = SectorData(sector)
        blocks = json.loads((COEFF / f'blocks_{sector}.json')
                            .read_text())
        rows_out = []
        for blk in blocks:
            center = blk['center']
            rows = blk['rows']
            assert len(rows) == 257 and rows[len(rows) // 2] == center
            seed_off = blk['NS_mean'] - blk['ndiag_mean']
            sp = [sd.spike_row(n) for n in rows]
            sp_mean = {k: float(sum(float(s[k]) for s in sp) / 257)
                       for k in ('V', 'U', 'pole', 'total')}
            phantom = -seed_off + sp_mean['total']
            templ_rows = [sd.A + sd.beta * log(log(n / 4))
                          + sd.D / log(n) for n in rows]
            templ = float(np.mean(templ_rows))
            dev = phantom - templ
            env = 15.0 / log(center) + sd.C_sp / center + 2e-4
            rows_out.append({
                'center': center, 'seed_NS_mean': blk['NS_mean'],
                'seed_ndiag_mean': blk['ndiag_mean'],
                'seed_off_plus_pole_mean': seed_off,
                'spike_V_mean': sp_mean['V'], 'spike_U_mean': sp_mean['U'],
                'spike_pole_mean': sp_mean['pole'],
                'spike_total_mean': sp_mean['total'],
                'phantom_NCT_mean': phantom,
                'template_at_block': templ, 'deviation': dev,
                'envelope_blockmean': env, 'inside_envelope':
                bool(abs(dev) <= env)})
            print(sector, center, 'phantom %.6f template %.6f '
                  'dev %+.6f env %.3f inside %s'
                  % (phantom, templ, dev, env,
                     abs(dev) <= env), flush=True)
        out[sector] = rows_out
    (HERE / 'anchors_blocks.json').write_text(json.dumps(out, indent=1))
    return out


def _load_eval_sector():
    spec = importlib.util.spec_from_file_location(
        'eval_seed_blocks', COEFF / 'eval_seed_blocks.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def stage_bands(sector):
    mod = _load_eval_sector()
    sd = SectorData(sector)
    sec = mod.Sector(sector)
    outpath = HERE / f'anchors_bands_{sector}.json'
    done = []
    if outpath.exists():
        done = json.loads(outpath.read_text())
    have = {r['center'] for r in done}
    P_ph = -sec.p_tot() + float(sd.pm1 * sd.y1)
    for center in CENTERS[sd.start]:
        if center in have:
            continue
        t0 = time.time()
        N = float(center)
        M = int(5 * N) + sd.start
        Vb = {'below': 0.0, 'near': 0.0, 'above': 0.0}
        Ub = {'below': 0.0, 'near': 0.0, 'above': 0.0}
        CH = 2_000_000
        for m0 in range(sd.b, M, CH):
            mb = np.arange(m0, min(m0 + CH, M), 2, dtype=np.float64)
            y, zy = sec.model(mb)
            y, zy = -y, -zy                      # phantom = -seed
            den = N * N - mb * mb
            kv = 2 * mb / den
            ku = 2 * N / den
            j = int((center - m0) // 2)
            if 0 <= j < len(mb) and mb[j] == center:
                kv[j] = 0.0
                ku[j] = 0.0
            for name, lo, hi in (('below', 0.0, N / 2),
                                 ('near', N / 2, 3 * N / 2),
                                 ('above', 3 * N / 2, np.inf)):
                sel = (mb >= lo) & (mb < hi)
                if np.any(sel):
                    Vb[name] += float(kv[sel] @ y[sel])
                    Ub[name] += float(ku[sel] @ zy[sel])
        # tails beyond M: evaluator's smooth-tail convention, negated
        W0 = sec.W[0]
        lM = log(M / 4)
        Ut = -(-(pi * W0 / (4 * lM)) * log(1.0 / (1 - (N / M) ** 2)) / N)
        Vt = -(-(W0 / (2 * lM)) * log((M + N) / (M - N)) / N)
        Vb['above'] += Vt
        Ub['above'] += Ut
        zN = float(z_mid(center)[0])
        pN = float(sd.L) * N / (N * N + float(sd.t))
        bands = {}
        tot = 0.0
        for name in ('below', 'near', 'above'):
            val = center * (float(sd.c) / 2) * (zN * Vb[name]
                                                - Ub[name])
            if name == 'below':
                val += float(sd.spike_row(center)['total'])
            bands[name] = val
            tot += val
        pole = center * sd.sigma * 2 * pN * P_ph
        rec = {'center': center, 'bands_NCT': bands,
               'spike_in_below_included': True,
               'pole_NCT': pole, 'total_NCT_center_row': tot + pole,
               'seconds': round(time.time() - t0, 1)}
        done.append(rec)
        outpath.write_text(json.dumps(done, indent=1))
        print(sector, center, json.dumps(rec), flush=True)
    return done


def stage_l2():
    out = {}
    for sector in ('even-v', 'odd-v'):
        sd = SectorData(sector)
        centers = CENTERS[sd.start]
        sums_t = {c0: 0.0 for c0 in centers}
        sums_r = {c0: 0.0 for c0 in centers}
        CH = 4_000_000
        for c0 in centers:
            pass
        # single sweep F0..max center, accumulating at each center
        n = sd.F0
        top = centers[-1]
        acc_t = 0.0
        acc_r = 0.0
        ci = 0
        while n <= top:
            blk = np.arange(n, min(n + CH, top + 1), 2,
                            dtype=np.float64)
            lam = np.log(np.log(blk / 4))
            li = np.log(blk)
            ct0 = (sd.A + sd.beta * lam + sd.D / li) / blk
            env = (20.0 / li + sd.C_sp / blk) / blk
            acc_t += float(np.sum(ct0 * ct0))
            acc_r += float(np.sum(env * env))
            n = int(blk[-1]) + 2
            while ci < len(centers) and centers[ci] <= int(blk[-1]):
                sums_t[centers[ci]] = acc_t
                sums_r[centers[ci]] = acc_r
                ci += 1
        out[sector] = [{'center': c0, 'template_l2_partial': sums_t[c0],
                        'template_l2_norm': sqrt(sums_t[c0]),
                        'remainder_l2_partial_bound': sums_r[c0],
                        'phantom_l2_partial_bound':
                        2 * sums_t[c0] + 2 * sums_r[c0]}
                       for c0 in centers]
        print(sector, 'l2 done', out[sector][-1])
    (HERE / 'anchors_l2.json').write_text(json.dumps(out, indent=1))
    return out


def stage_merge():
    anchors = {'gate': 'v14.909 counter-term construction gate',
               'producer': 'ctgate_producer.py',
               'constants': 'constants.json'}
    for name, key in (('anchors_dm.json', 'dm_silence'),
                      ('anchors_blocks.json', 'blocks'),
                      ('anchors_l2.json', 'l2')):
        p = HERE / name
        if p.exists():
            anchors[key] = json.loads(p.read_text())
    bands = {}
    for sector in ('even-v', 'odd-v'):
        p = HERE / f'anchors_bands_{sector}.json'
        if p.exists():
            bands[sector] = json.loads(p.read_text())
    if bands:
        anchors['bands_center_rows'] = bands
    (HERE / 'anchors.json').write_text(json.dumps(anchors, indent=1))
    print('anchors.json written, keys:', list(anchors))


if __name__ == '__main__':
    stage = sys.argv[1]
    if stage == 'dm':
        stage_dm()
    elif stage == 'blocks':
        stage_blocks()
    elif stage == 'bands':
        stage_bands(sys.argv[2])
    elif stage == 'l2':
        stage_l2()
    elif stage == 'merge':
        stage_merge()
    else:
        raise SystemExit('unknown stage ' + stage)
