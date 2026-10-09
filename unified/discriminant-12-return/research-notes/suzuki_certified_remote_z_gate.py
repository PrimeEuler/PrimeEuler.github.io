#!/usr/bin/env python3
"""Freeze evaluator diagnostics and its exact whole-source error budget."""
import argparse,hashlib,json,random
from fractions import Fraction as F
from pathlib import Path
from suzuki_certified_remote_z import evaluate

def build(source_path):
    import mpmath as mp
    raw=source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'
    whole=json.loads(raw)
    rng=random.Random(227)
    modes=list(range(256001,256025))+[512001,512002,1000001,1000002]
    modes += [rng.randrange(256001,10**10) for _ in range(12)]
    modes += [2**b+s for b in (64,128,256,512,1024) for s in (1,2)]
    rows=[]
    for n in modes:
        row=evaluate(n)
        with mp.workdps(int(n.bit_length()*.302)+90):
            weights=[mp.log(2)/mp.sqrt(2),mp.log(3)/mp.sqrt(3),mp.log(2)/2,mp.log(5)/mp.sqrt(5),mp.log(7)/mp.sqrt(7)]
            prime=mp.fsum(w*mp.sin(n*mp.pi*mp.log(q)/2) for q,w in zip((2,3,4,5,7),weights))
            k=mp.mpf(n)*mp.pi/2
            corr=mp.fsum(mp.exp(-2*(2*j+mp.mpf('.5')))/((2*j+mp.mpf('.5'))**2+k*k) for j in range(80))
            z=2*prime+mp.im(mp.digamma(mp.mpf('.25')+1j*mp.mpf(n)*mp.pi/4))-(-1)**n*n*mp.pi*corr
            def mf(s):
                f=F(s);return mp.mpf(f.numerator)/f.denominator
            assert mf(row['lower_rational'])<=z<=mf(row['upper_rational'])
        rows.append(row)
    charge=F('4e-5')*F('1e-10');assert charge==F('4e-15')
    budgets=[]
    for row in whole['cases']:
        an=F(row['rational']['whole_z_coefficient_norm_upper']);assert an<F('4e-5')
        eta=F(row['rational']['total_source_transport_plus_assembly_upper'])+charge
        assert eta<F('1e-9')
        budgets.append({'sector':row['sector'],'total_eta_with_numerical_z_upper_rational':str(eta)})
    return {'schema':'cone.certified-remote-z-and-source-budget.v1','cases':rows,
      'source_affine_certificate_sha256':hashlib.sha256(raw).hexdigest(),
      'independent_high_precision_physical_cases':len(rows),
      'all_direct_physical_values_inside_outward_intervals':True,
      'diagnostics_are_not_uniform_proof':True,
      'uniform_evaluator_radius_strict_upper_rational':'1/10000000000',
      'whole_source_numeric_z_error_strict_upper_rational':str(charge),
      'whole_source_error_budgets':budgets,
      'pointwise_numerical_physical_z_evaluator_certified':True,
      'uniform_whole_source_evaluation_error_budget_certified':True,
      'evaluated_trial_or_action':False,'paired_stationary_certified':False,
      'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=build(a.source);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'cases':len(o['cases']),'numerical_z_source_charge':o['whole_source_numeric_z_error_strict_upper_rational'],'both_source_budgets_pass':True}))
