#!/usr/bin/env python3
"""Explicit compact 1/n remote trials and certified scalar lower bounds."""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
sys.set_int_max_str_digits(0)
local=Path(__file__).resolve().parents[1]/'producers'
if local.is_dir():sys.path.insert(0,str(local))
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_trace_congruence_replay import display
from suzuki_paired_variational_acceptance import H,corners,interval

def floor(x,bits=384):
    s=1<<bits;return F(x.numerator*s//x.denominator,s)
def ceiling(x,bits=384):return -floor(-x,bits)
def sqrt_lower(x,bits=192):
    q=F(isqrt((x.numerator<<(2*bits))//x.denominator),1<<bits)
    assert q*q<=x;return q

def build(root,transport,contract):
    raw=transport.read_bytes();tr=json.loads(raw)
    eta={r['sector']:F(r['source_transport_eta_upper_rational']) for r in tr['cases']}
    rows=[]
    for sector,short in [('even-v','even'),('odd-v','odd')]:
        path=root/('frozen256-'+short+'-far.json');data=path.read_bytes();o=json.loads(data)
        n0=o['first_far_mode'];count=256000;end=n0+2*(count-1)
        assert n0>=512001 and end<=1024000<2**20
        Ulo=(F(1,n0)-F(1,n0+2*count))/2
        Uhi=F(1,n0*n0)+(F(1,n0)-F(1,end))/2
        assert Ulo>0 and Uhi>=Ulo
        # Independent full-band dyadic summation checks both parity endpoints.
        grid=1<<192
        direct_lo=sum(grid//(n*n) for n in range(n0,end+1,2))
        direct_hi=direct_lo+count
        assert Ulo<=F(direct_lo,grid)<=F(direct_hi,grid)<=Uhi
        # Exact constants in the physical arch integration-by-parts proof.
        assert F(19,24)*F(81,2)+F(3,2)*F(81**2,2)<5000
        assert F(40168,3*n0)<1
        first=o['combined_even_inverse_power_channels'][0]
        alo,ahi=map(F,first['combined_Z_pole_interval_rational'])
        alo,ahi=floor(alo),ceiling(ahi)
        rem=ceiling(sum((F(v) for v in o['norm_charges_rational'].values()),F(0))-F(first['norm_charge_rational']))
        assert rem>=0
        loss=ceiling((rem+eta[sector])/sqrt_lower(Ulo))
        amplitude=floor(alo-loss);assert amplitude>0
        scale=amplitude/58
        # For y=scale/n on the finite band: source pairing >= amplitude ||u||²,
        # S form <=D form<=58 ||y||², S form >=||y||².
        vlo=floor(amplitude*amplitude*Ulo/58)
        pair_upper=ceiling(ahi*Uhi+(rem+eta[sector])*sqrt_upper(Uhi,bits=192))
        vhi=ceiling(2*scale*pair_upper-scale*scale*Ulo)
        ynorm=ceiling(scale*sqrt_upper(Uhi,bits=192))
        assert vlo>F('5e-9') and vhi>=vlo and ynorm<F('0.01')
        small=scale/4
        small_lo=floor((2*small*amplitude-58*small*small)*Ulo)
        small_hi=ceiling(2*small*pair_upper-small*small*Ulo)
        gap_lower=floor(vlo-small_hi)
        assert gap_lower>F('1e-9')
        rows.append({'sector':sector,'far_input_sha256':hashlib.sha256(data).hexdigest(),
          'first_mode':n0,'last_mode':end,'step':2,'mode_count':count,
          'trial_definition':'y(n)=scale/n on the stated parity band; zero elsewhere',
          'trial_scale_rational':str(scale),'reference_norm2_interval_rational':[str(Ulo),str(Uhi)],
          'direct_band_norm2_dyadic_interval_rational':[str(F(direct_lo,grid)),str(F(direct_hi,grid))],
          'all_256000_band_terms_independently_checked':True,
          'nonleading_source_norm_upper_rational':str(rem),
          'source_transport_eta_rational':str(eta[sector]),
          'trial_norm_upper_rational':str(ynorm),'trial_norm_upper_display':display(ynorm),
          'stationary_v_interval_rational':[str(vlo),str(vhi)],
          'stationary_v_interval_display_approximate':[display(vlo),display(vhi)],
          'actual_lambda_lower_rational':str(vlo),'actual_lambda_gt_5e_minus9_exact':True,
          'quarter_scale_trial_rational':str(small),
          'quarter_scale_stationary_v_interval_rational':[str(small_lo),str(small_hi)],
          'quarter_scale_gap_lower_rational':str(gap_lower),
          'quarter_scale_gap_lower_display':display(gap_lower),
          'quarter_scale_gap_exceeds_sufficient_1e_minus9_budget_exact':True,
          'remote_residual_norm_upper':None,'operator_action_delta':None})
    craw=contract.read_bytes();cc=json.loads(craw)
    ck={r['sector']:interval(r['finite_K_interval_rational']) for r in cc['cases']}
    paired=corners((interval(rows[0]['stationary_v_interval_rational']),
                    interval(rows[1]['stationary_v_interval_rational']),
                    interval(cc['C_S_interval_rational']),ck['even-v'],ck['odd-v']),H)
    assert paired[0]<-F('2.9e-9') and paired[1]>F('2.9e-9')
    small_pair=corners((interval(rows[0]['quarter_scale_stationary_v_interval_rational']),
                    interval(rows[1]['quarter_scale_stationary_v_interval_rational']),
                    interval(cc['C_S_interval_rational']),ck['even-v'],ck['odd-v']),H)
    assert -F('2.9e-9')<=small_pair[0]<=small_pair[1]<=F('2.9e-9')
    return {'schema':'cone.compact-far-variational-trial.v1',
      'transport_input_sha256':hashlib.sha256(raw).hexdigest(),
      'finite_contract_input_sha256':hashlib.sha256(craw).hexdigest(),
      'physical_raw_band_D_operator_upper_rational':'58','cases':rows,
      'stationary_paired_H0_interval_rational':[str(floor(paired[0])),str(ceiling(paired[1]))],
      'stationary_paired_H0_interval_display_approximate':[display(paired[0]),display(paired[1])],
      'current_stationary_enclosure_meets_sufficient_2_9e_minus9_budget':False,
      'quarter_scale_paired_H0_interval_rational':[str(floor(small_pair[0])),str(ceiling(small_pair[1]))],
      'quarter_scale_paired_H0_interval_display_approximate':[display(small_pair[0]),display(small_pair[1])],
      'quarter_scale_meets_stationary_budget_but_fails_gap_budget_exact':True,
      'trial_domain_certified_by_finite_support':True,
      'both_actual_parity_capacities_exceed_5e_minus9_exact':True,
      'full_variational_acceptance_contract_ready':False,'infinite_capacity_tail_closed':False,
      'scope':'Positive nonzero trial and individual capacity lower bounds; no paired correction sign or residual gap upper bound.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--far-root',type=Path,required=True);p.add_argument('--transport',type=Path,required=True);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=build(a.far_root,a.transport,a.contract);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps([{'sector':r['sector'],'v_interval':r['stationary_v_interval_display_approximate'],'trial_norm':r['trial_norm_upper_display']} for r in o['cases']],indent=2))
