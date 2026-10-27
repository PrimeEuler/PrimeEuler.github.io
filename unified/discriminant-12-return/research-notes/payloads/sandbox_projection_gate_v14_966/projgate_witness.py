#!/usr/bin/env python3
"""Canonical operator-origin projection gate (v14.942) — witnesses.

W1  Sylvester identities for the frozen V/U channel maps, exact
    Fractions, random finite rational inputs.
W2  kappa at the spike mode m1 = b, recomputed exactly from the
    deposited ctgate constants.json rationals; asserted != 0.
W3  p_N > 0 in exact arithmetic at sample N (incl. F0 scale); the
    m = N coefficient of the row functional is exactly 2*sigma*p_N^2.
W4  The v14.936 spike's closed-form action at sample DM rows:
    CT_sp(N) = 0 would force z_N to one exact rational zeta(N);
    zeta(N) is compared with the CERTIFIED z_N enclosure
    (suzuki_bulk_action_z.evaluate) — outside it, so CT_sp(N) != 0
    is certified. The support clause was load-bearing.
W5  The full v14.936 phantom's channel action WITHOUT the support
    clause at sample DM rows (float64, evaluator's z model and
    channel formulas, direct chunked sums to m <= 2e8) plus a
    rigorous affine tail enclosure. [N] exhibit.
W6  (a) N*k_N(m1) -> kappa_{m1} numerically; (b) the Theorem's
    forced identity for z_m, evaluated at one DM row, mispredicts
    z_m by O(1) at large m (evaluator model). [N] support.
"""
import json, sys, random
from fractions import Fraction as F
from math import log, pi, sin, exp, sqrt
from pathlib import Path
import numpy as np

sys.set_int_max_str_digits(1000000)
HERE = Path(__file__).resolve().parent
CTGATE = HERE.parent / 'ctgate'
D12 = HERE.parents[2]
sys.path.insert(0, str(CTGATE))
sys.path.insert(0, str(D12))

from constants import z_mid_radius, floor_  # ctgate (imports evaluator)
from sandbox_region23_evaluator import load_source, physical_constants

OUT = {'W1': {}, 'W2': {}, 'W3': {}, 'W4': {}, 'W5': {}, 'W6': {}}
SRC = load_source()
CASES = {c['sector']: c for c in SRC['cases']}

# ---------------------------------------------------------------- W1
def Vmap(y, N):
    return sum(F(2 * m, N * N - m * m) * ym for m, ym in y.items() if m != N)

def Umap(a, N):
    return sum(F(2 * N, N * N - m * m) * am for m, am in a.items() if m != N)

rng = random.Random(20261026)
ok = True
for trial in range(60):
    sup = rng.sample(range(1, 40), 6)
    y = {m: F(rng.randint(-9, 9), rng.randint(1, 7)) for m in sup}
    a = {m: F(rng.randint(-9, 9), rng.randint(1, 7)) for m in sup}
    N = rng.choice([rng.randint(1, 45), sup[0]])
    M1 = sum(m * ym for m, ym in y.items())
    M0 = sum(a.values())
    lhsV = N * N * Vmap(y, N) - Vmap({m: m * m * ym for m, ym in y.items()}, N)
    rhsV = 2 * (M1 - (N * y[N] if N in y else 0))
    lhsU = N * N * Umap(a, N) - Umap({m: m * m * am for m, am in a.items()}, N)
    rhsU = 2 * N * (M0 - (a[N] if N in a else 0))
    ok &= (lhsV == rhsV) and (lhsU == rhsU)
OUT['W1'] = {'trials': 60, 'sylvester_V_exact': ok, 'sylvester_U_exact': ok}
assert ok

# ------------------------------------------------------- constants
CJ = json.loads((CTGATE / 'constants.json').read_text())

def rat(sec, key):
    return F(CJ[sec][key + '_rational'])

# ---------------------------------------------------------------- W2
for sec in ('even-v', 'odd-v'):
    sig = CJ[sec]['sigma']
    kap = -rat(sec, 'c') * rat(sec, 'z_m1_mid') + 2 * sig * rat(sec, 'L') * rat(sec, 'p_m1')
    assert kap == rat(sec, 'kappa') and kap != 0
    OUT['W2'][sec] = {'kappa': float(kap), 'kappa_nonzero_exact': True}

# ---------------------------------------------------------------- W3
for sec in ('even-v', 'odd-v'):
    start = CJ[sec]['start']; sig = CJ[sec]['sigma']
    c, ce, L, t = physical_constants(start)
    rows = {}
    for N in (1, 2, CJ[sec]['b'], 2080767 + (start - 1), CJ[sec]['F0'] - 2,
              CJ[sec]['F0'], 10**7):
        if (N - start) % 2: continue
        pN = F(floor_(L * N / (N * N + t), 256), 1 << 256)
        assert pN > 0
        rows[str(N)] = {'p_N_positive_exact': True,
                        'diag_coeff_2sig_pN2_nonzero': bool(2 * sig * pN * pN != 0)}
    OUT['W3'][sec] = rows

# ---------------------------------------------------------------- W4
for sec in ('even-v', 'odd-v'):
    sig = CJ[sec]['sigma']; start = CJ[sec]['start']
    c = rat(sec, 'c'); L = rat(sec, 'L'); t = rat(sec, 't')
    m1 = CJ[sec]['spike_mode_m1']; y1 = rat(sec, 'y1')
    zm1 = rat(sec, 'z_m1_mid'); pm1 = rat(sec, 'p_m1')
    res = {}
    for N in (1000000 + start, 2080766 + start, 3000000 + start, CJ[sec]['F0'] - 2):
        den = N * N - m1 * m1
        coef_zN = (c / 2) * y1 * F(2 * m1, den)          # multiplies z_N
        rest = (c / 2) * y1 * F(-2 * N, den) * zm1 \
            + 2 * sig * F(floor_(L * N / (N * N + t), 256), 1 << 256) * pm1 * y1
        assert coef_zN != 0
        zeta = -rest / coef_zN                            # z_N forced by CT_sp(N)=0
        mid, rad = z_mid_radius(N)
        margin = abs(zeta - mid) - rad
        ctsp = coef_zN * mid + rest
        res[str(N)] = {'zeta': float(zeta), 'z_mid': float(mid),
                       'z_radius': float(rad), 'margin_over_enclosure': float(margin),
                       'CT_sp_at_mid': float(ctsp), 'certified_nonzero': bool(margin > 0)}
        assert margin > 0, (sec, N, float(zeta), float(mid), float(rad))
    OUT['W4'][sec] = res

# ---------------------------------------------------------------- W5
WQ = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
THQ = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}
S0 = (1 / exp(1)) / (1 - exp(-4))
ZBAR = 7.4232946911477145

def z_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.full(n.shape, pi / 2) + (1 - 4 * sigma * S0) / (n * pi)
    for q in (2, 3, 4, 5, 7):
        tot = tot + 2 * WQ[q] * np.sin(n * THQ[q])
    return tot

M_BIG = 200_000_000
CH = 4_000_000

def phantom_dm_action(sec, N):
    case = CASES[sec]
    start = CJ[sec]['start']; sig = CJ[sec]['sigma']; b = CJ[sec]['b']
    c = CJ[sec]['c']; L = CJ[sec]['L']; t = CJ[sec]['t']; y1 = CJ[sec]['y1']
    W = np.array([float(F(r['W_coefficient_rational'])) for r in case['far_channels']])
    A = np.array([float(F(r['A_coefficient_rational'])) for r in case['far_channels']])
    V = U = P = 0.0
    m_lo = b
    while m_lo <= M_BIG:
        m_hi = min(m_lo + 2 * CH, M_BIG + 1)
        m = np.arange(m_lo, m_hi, 2, dtype=np.float64)
        r = 1.0 / (m * m)
        # Horner in r: sum_j W_j r^j, sum_j A_j r^j
        wsum = np.zeros_like(m); asum = np.zeros_like(m)
        for j in range(len(W) - 1, -1, -1):
            wsum = wsum * r + W[j]
            asum = asum * r + A[j]
        wsum /= m            # sum_j W_j m^{-(2j+1)}
        asum /= (m * m)      # sum_j A_j m^{-(2j+2)}
        zm = z_float(m, sig)
        yhat = wsum - asum * zm
        if sig < 0:
            yhat = yhat + 1.0 / (m * (m - 1))
        yhat = -yhat
        yhat[m == CJ[sec]['spike_mode_m1']] += y1
        ym = yhat / np.log(m / 4)
        pm = L * m / (m * m + t)
        P += float(np.sum(pm * ym))
        den = N * N - m * m
        keep = (m != N)
        V += float(np.sum((2 * m / den)[keep] * ym[keep]))
        U += float(np.sum((2 * N / den)[keep] * (zm * ym)[keep]))
        m_lo = m_hi
    zN_mid, zN_rad = z_mid_radius(N)
    zN = float(zN_mid)
    pN = L * N / (N * N + t)
    act = (c / 2) * (zN * V - U) + 2 * sig * pN * P
    # ---- rigorous tail enclosure (m > M_BIG), affine bound |yhat| <= Cyh/m.
    # Per-term scaling m^{-(2j+1)} <= b^{-2j}/m (raw W_j, A_j reach ~1e110;
    # the b^{-2j}-scaled sums are tame: ~1.14 and ~8433).
    rb = 1.0 / (b * b)
    sW = float(np.sum(np.abs(W) * rb ** np.arange(len(W))))
    sA = float(np.sum(np.abs(A) * rb ** np.arange(len(A))))
    Cyh = sW + ZBAR * sA / b + 2.0 / b
    lM = log(M_BIG / 4)
    fac = 1.0 / (1.0 - (N / M_BIG) ** 2)
    s2 = 1.0 / (2 * (M_BIG - 2)) + 1.0 / M_BIG**2     # >= sum_{m>M, step2} 1/m^2 (safe overestimate)
    s3 = 1.0 / (2 * M_BIG**2)
    tailV = (2 * Cyh / lM) * fac * s2
    tailU = (2 * N * ZBAR * Cyh / lM) * fac * s3
    tailP = (L * Cyh / lM) * s2
    enc = (c / 2) * (ZBAR * tailV + tailU + float(zN_rad) * abs(V)) + 2 * pN * tailP
    return {'N': N, 'N_times_action': float(N * act), 'action': float(act),
            'enclosure_on_N_times_action': float(N * enc),
            'V': V, 'U': U, 'P_tot': P, 'tail_enclosure': float(enc)}

for sec, rows in (('even-v', (2080767, 4161531)), ('odd-v', (2080768, 4161532))):
    OUT['W5'][sec] = [phantom_dm_action(sec, N) for N in rows]
    for r_ in OUT['W5'][sec]:
        assert abs(r_['N_times_action']) > r_['enclosure_on_N_times_action'], r_

# ---------------------------------------------------------------- W6
for sec in ('even-v', 'odd-v'):
    sig = CJ[sec]['sigma']; c = CJ[sec]['c']; L = CJ[sec]['L']; t = CJ[sec]['t']
    m1 = CJ[sec]['spike_mode_m1']; zm1 = CJ[sec]['z_m1']; pm1 = CJ[sec]['p_m1']
    kap = CJ[sec]['kappa']
    conv = {}
    for N in (100_000, 1_000_000, 10_000_000, 100_000_000):
        zN = float(z_float(np.array([float(N)]), sig)[0])
        pN = L * N / (N * N + t)
        kN = c * (m1 * zN - N * zm1) / (N * N - m1 * m1) + 2 * sig * pN * pm1
        conv[str(N)] = float(N * kN)
    # (b) forced identity from DM row N0: predict z_m, compare with model
    N0 = CJ[sec]['F0'] - 2
    zN0 = float(z_float(np.array([float(N0)]), sig)[0])
    pN0 = L * N0 / (N0 * N0 + t)
    pred = {}
    start = CJ[sec]['start']
    for m in (1_000_000 + start, 10_000_000 + start, 100_000_000 + start, 400_000_000 + start):
        pm = L * m / (m * m + t)
        zpred = (zN0 / N0) * m + (2 * sig * pN0 / (c * N0)) * pm * (N0 * N0 - m * m)
        ztrue = float(z_float(np.array([float(m)]), sig)[0])
        pred[str(m)] = {'z_model': ztrue, 'z_forced': float(zpred),
                        'abs_error': float(abs(ztrue - zpred))}
    OUT['W6'][sec] = {'Nk_N_m1_toward_kappa': conv, 'kappa': kap,
                      'forced_identity_prediction': pred}

(HERE / 'witness.json').write_text(json.dumps(OUT, indent=1))
print(json.dumps(OUT, indent=1)[:6000])
print('ALL WITNESS CHECKS PASSED')
