#!/usr/bin/env python3
"""Combine near affine rows and physical far channels, retaining remote z."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from suzuki_frozen_trial_far_outward import analyze,root_upper,sigma
from suzuki_exact_integer_source_action import sqrt_upper
sys.set_int_max_str_digits(0)
BITS=256
def up(q):return F(-((-q.numerator*(1<<192))//q.denominator),1<<192)
def midpoint(interval):
    q=sum(interval)/2;return F(q.numerator*(1<<BITS)//q.denominator,1<<BITS)
def run(root,near_root,source_root):
    cases=[]
    for short in ('even','odd'):
        sector=short+'-v'
        nr=(near_root/f'near-source-{sector}.json').read_bytes();near=json.loads(nr)
        sr=(source_root/f'full-stationary-source-{sector}.json').read_bytes();source=json.loads(sr)
        assert hashlib.sha256(sr).hexdigest()==near['full_stationary_certificate_sha256']
        mr=(root/f'frozen256-{short}-moments.json').read_bytes();mom=json.loads(mr)
        assert hashlib.sha256(mr).hexdigest()==source['far_moments_input_sha256']
        fr=(root/f'frozen256-{short}-far.json').read_bytes();far=json.loads(fr)
        assert (json.dumps(analyze(root/f'frozen256-{short}-moments.json'),indent=2,sort_keys=True)+'\n').encode()==fr
        pi=[F(x) for x in far['pi_interval_rational']];ci=[2/pi[1],2/pi[0]];c=midpoint(ci)
        dc=max(abs(c-ci[0]),abs(c-ci[1]));n0=far['first_far_mode']
        error=F(0);channels=[];far_A_norm=F(0)
        for row,m in zip(far['combined_even_inverse_power_channels'],mom['moments']):
            j=row['j'];assert j==m['j']
            ai=[F(x) for x in row['combined_Z_pole_interval_rational']];w=midpoint(ai)
            da=max(abs(w-ai[0]),abs(w-ai[1]))
            M=F(m['M_odd_rational']);ac=c*M
            far_A_norm+=abs(ac)*root_upper(sigma(4*j+4,n0))
            error+=da*root_upper(sigma(4*j+2,n0))+8*dc*abs(M)*root_upper(sigma(4*j+4,n0))
            channels.append({'j':j,'W_coefficient_rational':str(w),'A_coefficient_rational':str(ac)})
        error+=F(far['norm_charges_rational']['kernel_geometric'])+F(far['norm_charges_rational']['pole_geometric'])
        ne=F(near['rational']['near_assembly_error_upper']);assembly=up(sqrt_upper(ne*ne+error*error,192))
        transport=F(source['rational']['whole_remote_source_transport_upper']);total=up(transport+assembly)
        nn=F(near['rational']['physical_near_source_norm_upper']);fn=F(far['far_norm_upper_rational'])
        rho=up(sqrt_upper(nn*nn+fn*fn,192)+transport)
        assert assembly<F('4.04e-13') and total<F('1e-9') and rho<F('2e-3')
        # Repeat exact degree certificate with actual whole-source norm.
        C=575;L=F(11);a=F(1,576);b=F(586,11);x=(a+b)/(b-a);u,v=x.numerator,x.denominator
        J=2400;p0,p1=1,u
        for k in range(2,J+1):p0,p1=p1,2*u*p1-v*v*p0
        residual=F(v**J,p1)*(1+F(2*C*J*J)/(L*(b-a)))*rho
        assert residual<F('1e-7')<F('3e-5')
        trial_norm=up(rho+residual)  # S>=I: y=S^-1(rho-r).
        assert trial_norm<F('2e-3')
        near_A_norm=F(near['rational']['A_norm_upper'])
        whole_A_norm=up(sqrt_upper(near_A_norm**2+far_A_norm**2,192))
        assert whole_A_norm<F('4e-5')
        numeric_z_charge=whole_A_norm*F('1e-7')
        assert total+numeric_z_charge<F('1e-9')
        cases.append({'sector':sector,'near_certificate_sha256':hashlib.sha256(nr).hexdigest(),
          'source_certificate_sha256':hashlib.sha256(sr).hexdigest(),'far_certificate_sha256':hashlib.sha256(fr).hexdigest(),
          'far_first_mode':n0,'far_representation':'W(n)-z_physical(n)*A(n)+odd/(n*(n-1))',
          'far_W_power':'2j+1','far_A_power':'2j+2','far_channels':channels,
          'odd_source_shift_retained_exact':short=='odd',
          'rational':{'near_error_upper':str(up(ne)),'far_error_upper':str(up(error)),
            'whole_affine_assembly_error_upper':str(assembly),'total_source_transport_plus_assembly_upper':str(total),
            'true_whole_source_norm_upper':str(rho),'exact_degree_2400_residual_upper':str(up(residual)),
            'exact_degree_2400_trial_norm_upper':str(trial_norm),
            'whole_z_coefficient_norm_upper':str(whole_A_norm),
            'conditional_remote_z_evaluation_error_upper':str(up(numeric_z_charge)),
            'conditional_total_eta_with_z_cap_1e_minus7':str(up(total+numeric_z_charge))},
          'display_approximate':{'assembly_error':float(assembly),'total_eta':float(total),'whole_source_norm':float(rho),'degree_2400_residual':float(residual),'degree_2400_trial_norm':float(trial_norm)}})
    gap=(F('3e-5')+F('1e-9')+F('2e-10'))**2
    stationary=(2*F('1e-9')+F('2e-10'))*F('2e-3')
    assert gap<F('1e-9') and stationary<F('5e-12')
    assert F('3.454e-8')*F('2e-3')+F('6e-11')<=F('1.291e-10')<F('2e-10')
    assert F('1.334e-10')*F('2e-3')+F('6e-11')<F('6.027e-11')<F('2e-10')
    return {'schema':'cone.whole-affine-full-stationary-source.v1','cases':cases,
      'whole_source_affine_representation_certified':True,'total_eta_lt_1e_minus9_both':True,
      'true_whole_source_norm_lt_2e_minus3_both':True,'physical_remote_z_retained_exact':True,
      'remote_scalar_numeric_evaluation_certified':False,'evaluated_infinite_trial':False,
      'exact_degree_2400_trial_norm_lt_2e_minus3_both':True,
      'original_1e_minus3_trial_norm_target_achieved':False,
      'revised_sufficient_contract':{'trial_norm_ceiling_rational':'1/500',
        'source_eta_ceiling_rational':'1/1000000000','action_delta_ceiling_rational':'1/5000000000',
        'residual_gap_upper_rational':str(gap),'stationary_error_upper_rational':str(stationary),
        'conditional_model_action_even_upper_rational':'1291/10000000000000',
        'conditional_model_action_odd_upper_rational':'6027/100000000000000',
        'new_finite_lift_targets_achieved':False,'remote_action_arithmetic_achieved':False},
      'paired_stationary_certified':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('root','near-root','source-root','output'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();o=run(a.root,a.near_root,a.source_root);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps([r['display_approximate'] for r in o['cases']],indent=2))
