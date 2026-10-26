#!/usr/bin/env python3
"""v14.909 gate, stage S4: pure-affine variant constants (DERIVATION
sec.9). Evaluates, on the sector input lattice m >= b (step 2),

  Z3  = sum_m z_m / (m^3 * l_m),     Pi3 = sum_m p_m / (m^3 * l_m),
  c2  = -c * Z3 + 2*sigma*L * Pi3,  W1' = delta / c2,

with z_m the float model of the deposited evaluator
(eval_seed_blocks.z_float, the coeff819 working model of the
certified z) and p_m = L*m/(m^2+t) in float. Direct summation to
M = 4e7; tails enclosed as derived in DERIVATION sec.9 notes:
the Z3 tail is (pi/2)*T + trig/O(1/m) parts, T the step-2 sum of
1/(m^3 l_m) beyond M, T = (1/2)*I*(1+O(1/M)) with
I = int_M^inf dx/(x^3 ln(x/4)) = (1/(2 M^2 L_M))(1 - 1/(2 L_M))
+ O(1/(M^2 L_M^3)); trig tail <= 1.6e-23 per mode by summation by
parts; Pi3 tail <= L/(6 M^3 l_M) ~ 2e-25. Net effect: c2 known to
~1e-6 relative, far inside the gate envelope; W1' is DEFINED as
delta/c2 with c2 this series value.
"""
import importlib.util, json, sys
from math import log, pi
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
COEFF = HERE.parent / 'coeff819'
D12 = HERE.parents[2]
for p in (str(D12), str(D12 / 'laneA_modules'), str(COEFF)):
    sys.path.insert(0, p)

spec = importlib.util.spec_from_file_location(
    'eval_seed_blocks', COEFF / 'eval_seed_blocks.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

CONSTS = json.loads((HERE / 'constants.json').read_text())
M = 40_000_000


def run(sector):
    d = CONSTS[sector]
    start, sigma, b = d['start'], d['sigma'], d['b']
    L, t, c = d['L'], d['t'], d['c']
    Mend = M + start
    z3 = 0.0
    pi3 = 0.0
    CH = 2_000_000
    for m0 in range(b, Mend, CH):
        mb = np.arange(m0, min(m0 + CH, Mend), 2, dtype=np.float64)
        lm = np.log(mb / 4)
        z = mod.z_float(mb, sigma)
        w = 1.0 / (mb ** 3 * lm)
        z3 += float(np.sum(z * w))
        pi3 += float(np.sum((L * mb / (mb * mb + t)) * w))
    LM = log(Mend / 4)
    I = (1.0 / (2 * Mend ** 2 * LM)) * (1 - 1.0 / (2 * LM))
    T = 0.5 * I
    tail_z3 = (pi / 2) * T
    tail_bound = abs(tail_z3) * (1.0 / LM ** 2) + 5 * 1.6e-23 \
        + L / (6 * Mend ** 3 * LM)
    z3_tot = z3 + tail_z3
    c2 = -c * z3_tot + 2 * sigma * L * pi3
    W1 = d['delta'] / c2
    return {'sector': sector, 'M_direct': Mend, 'Z3_direct': z3,
            'Z3_tail_mean': tail_z3, 'tail_bound_abs': tail_bound,
            'Z3': z3_tot, 'Pi3': pi3, 'c2': c2, 'W1_prime': W1,
            'y1prime_at_b': W1 / b ** 3,
            'delta': d['delta']}


if __name__ == '__main__':
    out = {s: run(s) for s in ('even-v', 'odd-v')}
    (HERE / 'z3.json').write_text(json.dumps(out, indent=1) + '\n')
    for s, r in out.items():
        print(s, 'Z3=%.6e Pi3=%.6e c2=%.6e W1p=%.6e'
              % (r['Z3'], r['Pi3'], r['c2'], r['W1_prime']))
    print('z3.json written')
