#!/usr/bin/env python3
"""Action-precision physical scalar diagnostics and exact remainder budget."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from suzuki_certified_remote_z import evaluate
def build(source_gate):
    import mpmath as mp
    raw=source_gate.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='f37bbb3e33d51c04fea345ab45774c327f75efa8a23312be96bdd0695529d94d'
    old=json.loads(raw);rows=[]
    bern=[F(1),F(-1,2),F(1,6),F(0),F(-1,30),F(0),F(1,42),F(0),F(-1,30)]
    assert sum(abs(F(comb(8,j))*bern[j]) for j in range(9))<13
    s8=128*factorial(8)*F(16,15)**9;assert s8<10**7
    rem=13*F(4,3*256000)**8+F(1024*10**7,3**9*256000**9)
    assert rem<F('1e-39')
    xi=F('1e-39');tau=F(5*10**14)*xi
    model_z_operator_error=3*xi+42*tau+tau*tau
    model_z_action_error=F('2e-3')*model_z_operator_error
    assert model_z_action_error<F('5e-26')
    for oldrow in old['cases']:
        n=int(oldrow['n']);row=evaluate(n,action_precision=True)
        assert F(row['radius_upper_rational'])<F('1e-39')
        with mp.workdps(int(n.bit_length()*.302)+130):
            nn=mp.mpf(n);k=nn*mp.pi/2
            weights=[mp.log(2)/mp.sqrt(2),mp.log(3)/mp.sqrt(3),mp.log(2)/2,mp.log(5)/mp.sqrt(5),mp.log(7)/mp.sqrt(7)]
            prime=mp.fsum(w*mp.sin(nn*mp.pi*mp.log(q)/2) for q,w in zip((2,3,4,5,7),weights))
            corr=mp.fsum(mp.exp(-2*(2*j+mp.mpf('.5')))/((2*j+mp.mpf('.5'))**2+k*k) for j in range(100))
            exact=2*prime+mp.im(mp.digamma(mp.mpf('.25')+1j*nn*mp.pi/4))-(-1)**n*nn*mp.pi*corr
            def mf(s):
                q=F(s);return mp.mpf(q.numerator)/q.denominator
            assert mf(row['lower_rational'])<exact<mf(row['upper_rational'])
        rows.append(row)
    return {'schema':'cone.action-precision-physical-z.v1','cases':rows,
      'original_scalar_gate_sha256':hashlib.sha256(raw).hexdigest(),
      'B8_polynomial_coefficient_absolute_sum_lt_13':True,
      'exponential_S8_upper_rational':str(s8),'uniform_analytic_remainder_upper_rational':str(rem),
      'uniform_total_radius_strict_upper_rational':str(xi),
      'remote_z_inverse_weighted_coupling_error_upper_rational':str(tau),
      'remote_z_only_model_operator_error_upper_rational':str(model_z_operator_error),
      'remote_z_only_model_action_error_upper_rational':str(model_z_action_error),
      'all_50_original_physical_reference_values_inside':True,
      'default_source_mode_regression_must_match_original_gate':True,
      'finite_lift_rhs_or_solve_certified':False,'remote_D_diagonal_certified':False,
      'evaluated_trial_or_action':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source-gate',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    o=build(a.source_gate);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print('50 action-precision physical intervals and exact remainder checks passed.')
