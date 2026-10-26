#!/usr/bin/env python3
"""v14.819 task 3 (remainder side): signed moments M_1, M_{z,2},
Zbar from the certified remote-z decomposition, and the sharp
remainder prediction vs the empirical N*C(N) - c_inf gap.

Zbar: z(n) = sum_{q in (2,3,4,5,7)} 2 w_q sin(theta_q(n))
+ nonprime(n), w_q = log q / sqrt(q) (w_4 = log 2 / 2), from
laneA_modules/suzuki_certified_remote_z.py (R = 256000).
|trig| <= 2*sum(wp_q + dw_q) exactly (|sin| <= 1, weights are the
module's certified intervals). sup_{n>R} |nonprime(n)| <= pi/2 +
3e-5: its psi part is pi/2 - atan(1/(n pi)) - Im(wi)/2 + Bernoulli
w2-power corrections with |wi| <= 1/(n pi/4) <= 5e-6, atan <= 1.3e-6,
Bernoulli terms <= 1e-11, and the moment correction corr <=
16/(n pi)(1 + o(1)) <= 2e-5 (module's precise_nonprime).
"""
import json, sys
sys.set_int_max_str_digits(1000000)
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mz_eval as mz
import suzuki_certified_remote_z as rz

pi, pp, weights, phases, s0, sp = rz.constants(512)
trig = sum(2 * (wp + dw) for wp, dw in weights)
Zbar = trig + pi[1] / 2 + F(3, 100000)
print('Zbar =', float(Zbar), ' (trig part', float(trig), ')')

# sanity: certified enclosures at sample n must lie inside Zbar
for n in (256001, 1000003, 16646125, 10**9 + 7):
    e = rz.evaluate(n, action_precision=True)
    assert abs(F(e['lower_rational'])) < Zbar
    assert abs(F(e['upper_rational'])) < Zbar
print('z enclosure spot checks inside Zbar: OK')

for sector in ('even-v', 'odd-v'):
    s, start, components, pins = mz.changed.load_components(
        *mz.ROOTS, sector)
    M1 = F(0)
    Mz2 = F(0)
    for cpt in components:
        xv, zv = cpt['x']['values'], cpt['z']['values']
        xb, zb = cpt['x']['bits'], cpt['z']['bits']
        off = cpt['offset']
        M1 += F(sum(x * (2 * (off + j) + start)
                    for j, x in enumerate(xv)), 1 << xb)
        Mz2 += F(sum(x * z * (2 * (off + j) + start) ** 2
                     for j, (x, z) in enumerate(zip(xv, zv))),
                 1 << (xb + zb))
    d = json.loads((HERE / f'mz-{sector}.json').read_text())
    da = d['display_approximate']
    c, alpha, L, P, t = (F(d['rational'][k]) for k in
                         ('c', 'alpha', 'L', 'P', 't'))
    c_inf = F(d['rational']['c_inf'])
    out = {
        'schema': 'cone.far-coefficient-remainder.v1',
        'handoff': 'v14.819 task 3 (remainder side)',
        'sector': sector,
        'rational': {'M_1': str(M1), 'M_z2': str(Mz2),
                     'Zbar': str(Zbar)},
        'display_approximate': {'M_1': float(M1), 'M_z2': float(Mz2),
                                'Zbar': float(Zbar)},
        'note': ('Sharp remainder via the v14.819 exact identity: '
                 'N*(C(N) - c_inf/N) = c*z_N*M_1*N/(N^2-m^2 sum) '
                 '- c*M_z2/(N^2-m^2 sum) - alpha*L*P*t/(N^2+t) + '
                 'higher signed-moment terms; leading terms '
                 'c*z_N*M_1/N - c*M_z2/N^2 - alpha*L*P*t/N^2. '
                 'Absolute A_1/A_2 bound is rigorous but lossy '
                 '(~4.5e4 at F2 scales, even sector).'),
    }
    (HERE / f'remainder-{sector}.json').write_text(
        json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(sector, 'M_1 =', float(M1), ' M_z2 =', float(Mz2))
print('DONE')
