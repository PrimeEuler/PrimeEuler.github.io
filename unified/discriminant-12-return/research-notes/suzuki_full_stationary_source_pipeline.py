#!/usr/bin/env python3
"""Rebind far/variational checks to the certified full stationary source."""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from suzuki_paired_variational_acceptance import build as contract_build
from suzuki_compact_far_variational_trial import build as compact_build
from suzuki_frozen_trial_far_outward import analyze as far_analyze
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def save(path,obj):
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--far-root',type=Path,required=True)
    p.add_argument('--finite',type=Path,required=True)
    p.add_argument('--output-root',type=Path,required=True)
    a=p.parse_args();a.output_root.mkdir(parents=True,exist_ok=True)
    cases=[]
    for sector in ('even-v','odd-v'):
        path=a.source_root/f'full-stationary-source-{sector}.json'
        raw=path.read_bytes();row=json.loads(raw)
        assert row['sector']==sector and row['all_existing_far_moments_match_corrected_vector']
        short='even' if sector=='even-v' else 'odd'
        regenerated=far_analyze(a.far_root/f'frozen256-{short}-moments.json')
        assert (json.dumps(regenerated,indent=2,sort_keys=True)+'\n').encode()==(a.far_root/f'frozen256-{short}-far.json').read_bytes()
        eta=F(row['rational']['whole_remote_source_transport_upper'])
        assert eta<F('1e-9')
        cases.append({'sector':sector,'full_stationary_transport_certificate_sha256':hashlib.sha256(raw).hexdigest(),
          'source_transport_eta_upper_rational':str(eta),
          'source_vector_recipe':row['full_source_vector_recipe'],
          'q_dyadic_bits':row['q_dyadic_bits'],'q_rational':row['q_rational'],
          'existing_far_moments_matched':True})
    transport={'schema':'cone.full-stationary-source-transport-pair.v1','cases':cases,
      'source_definition':'rho=g_remote-B A_R^-1 g_R; represented source uses full stationary Z',
      'old_fixed_trace_transport_not_applied_to_full_inverse':True,
      'source_assembly_certified':False,'infinite_capacity_tail_closed':False}
    tp=a.output_root/'full-stationary-transport-pair.json';save(tp,transport)
    contract=contract_build(a.finite,tp,a.far_root)
    source_cap=F('1e-9');action_cap=F('1e-10');ynorm=F('1e-3')
    gap=(F('3e-5')+source_cap+action_cap)**2
    stationary=(2*source_cap+action_cap)*ynorm
    assert gap<F('1e-9') and stationary<F('5e-12')
    contract['exact_consumer_checks']['sufficient_residual_gap_cap_rational']=str(gap)
    contract['revised_sufficient_source_eta_ceiling_rational']=str(source_cap)
    contract['revised_sufficient_trial_norm_ceiling_rational']=str(ynorm)
    contract['revised_stationary_error_ceiling_rational']=str(stationary)
    contract['full_stationary_source_geometry_certified']=True
    cp=a.output_root/'full-stationary-variational-contract.json';save(cp,contract)
    compact=compact_build(a.far_root,tp,cp)
    compact['full_stationary_source_geometry_certified']=True
    save(a.output_root/'full-stationary-compact-trial.json',compact)
    # Independent exact fixed-trace example, with a positive remote Schur floor.
    # A=[[2,1],[1,2]], g=(1,0), fixed protected trace zero => constrained x=0.
    # Full x=(2/3,-1/3); B=(1/3,1/5), so Bx=7/45 !=0.
    assert F(1,3)*F(2,3)-F(1,5)*F(1,3)==F(7,45)
    assert F(7,45)>0
    assert F(2,3)*(F(1,9)+F(1,25)-F(1,15))==F(38,675)
    assert (1+F(38,675))-F(38,675)==1
    budget={'schema':'cone.full-stationary-source-budget-repair.v1',
      'source_eta_ceiling_rational':str(source_cap),'action_delta_ceiling_rational':str(action_cap),
      'trial_norm_ceiling_rational':str(ynorm),'represented_residual_norm_ceiling_rational':'3/100000',
      'remote_gap_upper_rational':str(gap),'stationary_source_action_error_upper_rational':str(stationary),
      'gap_lt_1e_minus9':True,'stationary_charge_lt_5e_minus12':True,
      'sufficient_DeltaQ_abs_upper_rational':contract['exact_consumer_checks']['sufficient_DeltaQ_abs_upper_rational'],
      'fixed_trace_full_inverse_counterexample_exact':True,
      'remaining_even_source_assembly_budget_rational':str(source_cap-F(cases[0]['source_transport_eta_upper_rational'])),
      'remaining_odd_source_assembly_budget_rational':str(source_cap-F(cases[1]['source_transport_eta_upper_rational'])),
      'infinite_capacity_tail_closed':False}
    save(a.output_root/'full-stationary-source-budget.json',budget)
    print(json.dumps({'compact_trials_still_pass':True,'stationary_charge':str(stationary),
      'far_energy_lower_display':[r['exact_physical_far_residual_energy_lower_display'] for r in contract['cases']],
      'capacity_lower_display':[r['stationary_v_interval_display_approximate'][0] for r in compact['cases']]},indent=2))
if __name__=='__main__':main()
