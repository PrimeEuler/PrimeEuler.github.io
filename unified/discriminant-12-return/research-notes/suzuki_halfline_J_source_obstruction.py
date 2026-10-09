#!/usr/bin/env python3
"""Exact rational charges for J half-line leakage and slow-source mismatch."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from suzuki_frozen_trial_far_outward import atan_recip,add,neg,times,constant
from suzuki_trace_congruence_replay import display

def analyze():
    pi=add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239))))
    pi_hi=F(22,7);assert 0<pi[0]<=pi[1]<pi_hi
    boxes=[]
    for a in (1,2,3,7,16):
        energy=sum((sum((1/(pi_hi*(F(r+k)+F(1,2))*(a+2*k))
                         for k in range(a)),F(0)))**2 for r in range(a))
        lower=1/(36*pi_hi*pi_hi*a)
        assert energy>=lower
        boxes.append({'a':a,'finite_positive_box_energy_lower_rational':str(energy),
                      'uniform_box_lower_rational':str(lower),'comparison_exact':True})
    sources=[]
    for a,ratio_cap in ((32001,F(1,125)),(256001,F(7,2500))):
        norm_lower=F(1,2*a)
        norm_upper=F(1,a*a)+F(1,2*a)
        leakage=1/(36*pi_hi*pi_hi*a)
        frac_lower=leakage/norm_upper
        assert frac_lower>F(1,180)
        diff_ratio2=F(2,a)+F(4,3*a*a)+F(8,a**3)
        assert diff_ratio2<=ratio_cap**2
        mismatch2=(2-ratio_cap)*norm_lower
        sources.append({'a':a,'source_norm2_lower_rational':str(norm_lower),
                        'source_norm2_upper_rational':str(norm_upper),
                        'halfline_leakage_energy_lower_rational':str(leakage),
                        'halfline_leakage_energy_lower_display':display(leakage),
                        'leakage_fraction_lower_rational':str(frac_lower),
                        'leakage_fraction_gt_1_over_180_exact':True,
                        'gradient_norm_ratio_upper_rational':str(ratio_cap),
                        'J_source_mismatch_energy_lower_rational':str(mismatch2),
                        'J_source_mismatch_energy_lower_display':display(mismatch2),
                        'raw_leakage_energy_gt_5e_minus9_exact':leakage>F('5e-9')})
    return {'schema':'cone.halfline-J-source-obstruction.v1',
            'pi_upper_22_over_7_verified_by_rational_Machin_interval':True,
            'positive_box_checks':boxes,'source_charges':sources,
            'bilateral_to_halfline_leakage_operator_norm_analytic':1,
            'compressed_unitarity_defect_operator_norm_analytic':1,
            'norm_one_proof_is_analytic_not_finite_section_extrapolation':True,
            'actual_residual_rho_and_remote_inverse_not_replaced_by_simple_u':True,
            'infinite_capacity_tail_closed':False}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    p.add_argument('--reference',type=Path);a=p.parse_args();o=analyze()
    raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'source_charges':o['source_charges'],
                      'leakage_operator_norm_analytic':1,
                      'infinite_capacity_tail_closed':False},indent=2))
if __name__=='__main__':main()
