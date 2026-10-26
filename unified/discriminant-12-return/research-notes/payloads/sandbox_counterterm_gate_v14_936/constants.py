#!/usr/bin/env python3
"""v14.909 counter-term gate, stage S1: full-precision constants.

Sources (all frozen, hash-pinned upstream):
- W_0 exact rational: coeff819/w0_exact.json (from the pinned
  payloads/whole-source-affine.json, sha asserted by load_source()).
- c_inf exact rational: coeff819/mz-{sector}.json (v14.817 identity
  c_inf = -c*M_z + alpha*L*P, exact Fractions).
- K_sigma, gamma_sigma: the stored full-precision pinned-beta fits
  of the v14.901 return, RE-DERIVED here from the frozen block
  artifacts coeff819/blocks_{sector}.json by the same least-squares
  as coeff819/fit_blocks.py (beta pinned at W_0/2, regressors
  (1, -ln ln(n/4), 1/ln n)); asserted against the values recorded
  in the run log of 2026-10-26.
- c, L, t: physical_constants() of the deposited evaluator
  (~/workspace/d12/sandbox_region23_evaluator.py), exact Fraction
  midpoints at 2^256 -- the same constants the seed producer uses.
- Spike mode m_1: first mode of the sector input lattice with
  |z_mid(m_1)| >= 1, z from the certified enclosure
  (suzuki_bulk_action_z.evaluate, radius < 1e-39);
  p_{m_1} = floor(L*m_1/(m_1^2+t), 256)/2^256 exactly as seed_row.
- kappa = -c*z_mid(m_1) + 2*sigma*L*p_{m_1} (Fraction);
  y_1 = delta/kappa with delta = 1 - c_inf - W_0 (exact Fraction).
"""
import json, sys
from fractions import Fraction as F
from math import log
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
COEFF = HERE.parent / 'coeff819'
D12 = HERE.parents[2]
sys.path.insert(0, str(D12))
sys.path.insert(0, str(D12 / 'laneA_modules'))
sys.set_int_max_str_digits(1000000)

from sandbox_region23_evaluator import load_source, physical_constants
from suzuki_bulk_action_z import evaluate as z_eval

SRC = load_source()  # asserts the pinned source SHA-256

RECORDED = {  # pinned-fit values recorded from fit_blocks.py, 2026-10-26
    'even-v': {'K': 2.5527139612295247, 'gamma': -0.35474258710667983},
    'odd-v': {'K': 2.5522359590515484, 'gamma': -0.38075887760049554},
}


def pinned_fit(sector, W0f):
    d = json.loads((COEFF / f'blocks_{sector}.json').read_text())
    pts = np.array([r['center'] for r in d], dtype=np.float64)
    NS = np.array([r['NS_mean'] for r in d])
    X = np.log(np.log(pts / 4.0))
    li = 1.0 / np.log(pts)
    A = np.column_stack([np.ones_like(X), li])
    coef, *_ = np.linalg.lstsq(A, NS + (W0f / 2) * X, rcond=None)
    resid = NS - (coef[0] - (W0f / 2) * X + coef[1] * li)
    return {'K': float(coef[0]), 'gamma': float(coef[1]),
            'rms': float(np.sqrt(np.mean(resid ** 2))),
            'max_abs': float(np.max(np.abs(resid))),
            'centers': [int(x) for x in pts]}


def z_mid_radius(m):
    r = z_eval(m)
    lo, hi = F(r['lower_rational']), F(r['upper_rational'])
    return (lo + hi) / 2, (hi - lo) / 2


def floor_(q, bits):
    return q.numerator * (1 << bits) // q.denominator


def sector_constants(sector):
    start = 1 if sector == 'even-v' else 2
    sigma = 1 if sector == 'even-v' else -1
    b = 512000 + start
    F0 = 4161532 + start
    w0 = json.loads((COEFF / 'w0_exact.json').read_text())[sector]
    W0 = F(w0['W_0_rational'])
    mz = json.loads((COEFF / f'mz-{sector}.json').read_text())
    c_inf = F(mz['rational']['c_inf'])
    assert abs(float(c_inf) - mz['display_approximate']['c_inf']) < 1e-15
    fit = pinned_fit(sector, float(W0))
    assert abs(fit['K'] - RECORDED[sector]['K']) < 1e-12, fit
    assert abs(fit['gamma'] - RECORDED[sector]['gamma']) < 1e-12, fit
    K, gamma = fit['K'], fit['gamma']
    beta = W0 / 2
    A = 1 - float(c_inf) - K
    D = -gamma
    delta = 1 - c_inf - W0            # exact Fraction
    C_off = K - float(W0)             # = TASK2B C_off, audited
    c, ce, L, t = physical_constants(start)
    # spike mode: first lattice mode with |z_mid| >= 1
    m = b
    while True:
        zm, zr = z_mid_radius(m)
        if abs(zm) >= 1:
            break
        m += 2
    assert zr < F('1e-39'), zr
    p1 = F(floor_(L * m / (m * m + t), 256), 1 << 256)
    kappa = -c * zm + 2 * sigma * L * p1
    y1 = delta / kappa
    # induced constant error from the z midpoint: |dc| <= c*zr/|kappa| * delta
    kappa_err = abs(delta) * c * zr / (kappa * kappa)
    return {
        'sector': sector, 'start': start, 'sigma': sigma, 'b': b, 'F0': F0,
        'W_0_rational': str(W0), 'W_0': float(W0),
        'beta_rational': str(beta), 'beta': float(beta),
        'c_inf_rational': str(c_inf), 'c_inf': float(c_inf),
        'K': K, 'gamma': gamma, 'fit_rms': fit['rms'],
        'fit_max_abs': fit['max_abs'], 'fit_centers': fit['centers'],
        'A': A, 'D': D,
        'delta_rational': str(delta), 'delta': float(delta),
        'C_off': C_off,
        'c_rational': str(c), 'c': float(c),
        'L_rational': str(L), 'L': float(L),
        't_rational': str(t), 't': float(t),
        'spike_mode_m1': m, 'z_m1_mid_rational': str(zm),
        'z_m1_radius_rational': str(zr), 'z_m1': float(zm),
        'p_m1_rational': str(p1), 'p_m1': float(p1),
        'kappa_rational': str(kappa), 'kappa': float(kappa),
        'kappa_induced_const_err_bound': float(kappa_err),
        'y1_rational': str(y1), 'y1': float(y1),
    }


if __name__ == '__main__':
    out = {s: sector_constants(s) for s in ('even-v', 'odd-v')}
    (HERE / 'constants.json').write_text(json.dumps(out, indent=1) + '\n')
    for s, d in out.items():
        print(s, 'A=%.15f D=%.15f delta=%.15f m1=%d z=%.6f kappa=%.6f '
              'y1=%.10f fit_rms=%.2e' % (d['A'], d['D'], d['delta'],
              d['spike_mode_m1'], d['z_m1'], d['kappa'], d['y1'],
              d['fit_rms']))
    print('constants.json written')
