#!/usr/bin/env python3
"""v14.819 task 3: five-component compact functionals M_z, A_1, A_2, P
and c_inf = -c*M_z + alpha*L*P, from the hash-pinned ca544 inputs.

- Components loaded via the producer's own changed.load_components
  (all pins asserted inside).
- P recomputed by the producer's own changed.prep into a scratch dir
  and compared field-by-field with the pinned prep-{sector}.json.
- M_z / A_1 / A_2 by exact integer sums over the dyadic component
  points (the same points the producer action is defined with);
  perturbation to true-z M_z bounded by sum_j |x_j| * 2^-zbits_j.
- Empirical validation: block means of N*C(N) over the F2 top octave
  from the composed far-compact buffers, and of N*S(N) from the seed
  buffers; the identity 1 - c_inf - s_emp must reproduce the
  composed residual's rho_emp (v14.812-S RESULTS.md).
"""
import json, sys
sys.set_int_max_str_digits(1000000)
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAR = HERE.parent
D12 = FAR.parents[1]
CA544 = D12 / 'dm490' / 'ca544'
R = D12 / 'refined_far' / 'payloads'
for p in (str(CA544), str(CA544 / 'modules'), str(D12 / 'laneA_modules'),
          str(FAR), str(D12)):
    if p not in sys.path:
        sys.path.insert(0, p)

import suzuki_direct_middle_changed_compact_action as changed

ROOTS = (R / 'exact_outward_run_37827949740',
         R / 'refined_near_trial_and_lift_v14_300',
         CA544 / 'inputs' / 'gap',
         R / 'full_stationary_source_v14_213',
         CA544 / 'inputs' / 'old_finite',
         CA544 / 'inputs' / 'candidate',
         D12 / 'dm490' / 'lift541' / 'out',
         D12 / 'dm490' / 'rhs511' / 'out',
         D12 / 'dm490' / 'out')
WORK = FAR / 'work'
S = 1 << 256


def emp_block_mean(sector, kind, cls):
    """Mean of N * action(N) over the top-octave blocks of class cls,
    from the composed buffers (physical values = int / 2^256)."""
    if kind == 'compact':
        cert = json.loads((WORK / f'far-compact-{sector}-{cls}.json')
                          .read_text())
    else:
        cert = json.loads((WORK / f'far-seed-{sector}-{cls}.json')
                          .read_text())
    pb = cert['point_buffer']
    raw = (WORK / pb['file']).read_bytes()
    w, count = pb['width'], pb['count']
    first = cert.get('first_output_mode') or cert['output_first_mode']
    shift = 0 if sector == 'even-v' else 1
    vals = [int.from_bytes(raw[i:i + w], 'little', signed=True)
            for i in range(0, len(raw), w)]
    BLK = 1 << 16
    blocks = []
    for b0 in range(count // 2, count - BLK + 1, BLK):
        seg = vals[b0:b0 + BLK]
        blocks.append(sum(v * (first + 2 * (b0 + k) - shift)
                          for k, v in enumerate(seg)) / (BLK * S))
    return sum(blocks) / len(blocks), len(blocks)


def run(sector):
    s, start, components, pins = changed.load_components(*ROOTS, sector)
    prep_re = changed.prep(ROOTS, sector, HERE / 'prep_replay')
    prep_pin = json.loads((CA544 / 'work' / f'prep-{sector}.json')
                          .read_text())
    for k in ('pole_pairing_P', 'compact_l1', 'Lpoint', 'tpoint'):
        assert prep_re[k] == prep_pin[k], f'prep mismatch {k}'
    assert prep_re['input_pins'] == prep_pin['input_pins']
    assert prep_re['component_offsets_counts'] == \
        prep_pin['component_offsets_counts']

    P = F(prep_pin['pole_pairing_P'])
    L, t = F(prep_pin['Lpoint']), F(prep_pin['tpoint'])
    c = F(s['c']['values'][0], 1 << s['c']['bits'])
    alpha = F(s['alpha'])
    assert abs(c) < 1

    Mz = F(0)
    A1 = F(0)
    A2 = F(0)
    zpert = F(0)
    per_comp = []
    for cpt in components:
        xv, zv = cpt['x']['values'], cpt['z']['values']
        xb, zb = cpt['x']['bits'], cpt['z']['bits']
        off = cpt['offset']
        mz_n = sum(z * x for z, x in zip(zv, xv))
        a1_n = sum(abs(x) * (2 * (off + j) + start)
                   for j, x in enumerate(xv))
        a2_n = sum(abs(x * z) * (2 * (off + j) + start) ** 2
                   for j, (x, z) in enumerate(zip(xv, zv)))
        mz_c = F(mz_n, 1 << (xb + zb))
        a1_c = F(a1_n, 1 << xb)
        a2_c = F(a2_n, 1 << (xb + zb))
        l1_c = F(sum(abs(x) for x in xv), 1 << xb)
        Mz += mz_c
        A1 += a1_c
        A2 += a2_c
        zpert += l1_c * F(1, 1 << zb)
        per_comp.append({'name': cpt['name'], 'offset': off,
                         'count': len(xv), 'x_bits': xb, 'z_bits': zb,
                         'M_z': str(mz_c), 'M_z_float': float(mz_c),
                         'A_1_float': float(a1_c),
                         'A_2_float': float(a2_c)})
    l1 = sum(F(sum(abs(v) for v in cp['x']['values']),
               1 << cp['x']['bits']) for cp in components)
    assert l1 == F(prep_pin['compact_l1'])

    c_inf = -c * Mz + alpha * L * P
    target = 1 - c_inf  # = 1 + c*M_z - alpha*L*P, the s_inf target

    nc_emp, nb1 = emp_block_mean(sector, 'compact', 'F2')
    ns_emp, nb2 = emp_block_mean(sector, 'seed', 'F2')
    out = {
        'schema': 'cone.far-coefficient-compact-functionals.v1',
        'handoff': 'v14.819 task 3',
        'sector': sector,
        'start': start,
        'prep_recomputed_and_matches_pin': True,
        'rational': {
            'c': str(c), 'alpha': str(alpha), 'L': str(L), 't': str(t),
            'P': str(P), 'M_z': str(Mz), 'A_1': str(A1), 'A_2': str(A2),
            'z_point_perturbation_bound_on_M_z': str(zpert),
            'c_inf': str(c_inf), 's_inf_target': str(target),
        },
        'display_approximate': {
            'c': float(c), 'alpha': float(alpha), 'L': float(L),
            't': float(t), 'P': float(P), 'M_z': float(Mz),
            'A_1': float(A1), 'A_2': float(A2),
            'z_perturbation_bound': float(zpert),
            'c_inf': float(c_inf), 's_inf_target': float(target),
            'empirical_NC_F2_top_octave': nc_emp,
            'empirical_NS_F2_top_octave': ns_emp,
            'empirical_rho_identity': 1 - nc_emp - ns_emp,
        },
        'components': per_comp,
        'whole_residual_acceptance_certified': False,
    }
    (HERE / f'mz-{sector}.json').write_text(
        json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'sector': sector,
                      'c_inf': float(c_inf),
                      'NC_emp': nc_emp,
                      'NS_emp': ns_emp,
                      'rho_identity_emp': 1 - nc_emp - ns_emp,
                      'target_s_inf': float(target)}, indent=1))
    return out


if __name__ == '__main__':
    for sec in ('even-v', 'odd-v'):
        run(sec)
