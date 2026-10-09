#!/usr/bin/env python3
"""Exact budgets for a near-exact / far-channel whole remote Schur model."""
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
PINS={'even-v':'e726b54aa728d598e0046b332af7e10dd6afcd5adcf370f2fdbb91e2ca7340e9',
      'odd-v':'5692ac1b3bf7f4bfb627d158149dfd3c9432b49336251d05c467a04bc3f6cfec'}
R=256000; N=128000; T=2**256
def up(q,bits=192):
    s=1<<bits
    return F(-((-q.numerator*s)//q.denominator),s)
def sqrt_up(q,bits=192):
    assert q>=0
    s=1<<bits;v=math.isqrt(q.numerator*s*s//q.denominator)
    if v*v*q.denominator<q.numerator*s*s:v+=1
    return F(v,s)
def disp(n,m,zn,zm,c):
    return c*(zn*m-n*zm)/F(n*n-m*m)
def algebra_checks():
    count=0
    for cutoff in (7,19,64):
        for m in (1,cutoff//2,cutoff):
            for n in (2*cutoff+1,3*cutoff+2,8*cutoff+5):
                for terms in (1,2,3,7):
                    for zn,zm in ((F(2,3),F(-4,5)),(F(-7,3),F(11,7)),(F(0),F(5,4))):
                        c=F(7,11);L=F(13,17);t=F(2,19);alpha=F(-2)
                        pole=lambda k:L/(k*(1+t/F(k*k)))
                        w1=-c*zm+alpha*L*pole(m)
                        model=w1/n+alpha*pole(m)*(pole(n)-L/n)
                        for k in range(terms):
                            model+=c*zn*m**(2*k+1)/F(n**(2*k+2))
                            if k: model-=c*zm*m**(2*k)/F(n**(2*k+1))
                        exact=disp(n,m,zn,zm,c)+alpha*pole(n)*pole(m)
                        rem=disp(n,m,zn,zm,c)*F(m,n)**(2*terms)
                        assert exact-model==rem
                        assert abs(rem)<=F(20,n)*F(cutoff,n)**(2*terms)
                        count+=1
    inverse_checks=0
    # Full finite inverse, including a non-unit protected trace u.
    for c,b,h,u,e in ((F(2),F(3),F(1,7),F(5),F(2,11)),
                       (F(1,1000),F(-2,7),F(1,10**12),F(10**8),F(-1,13)),
                       (F(7,3),F(5,9),F(2),F(1,100),F(3,17))):
        A00=h+b*b/c;det=h*c
        ai00=c/det;ai01=-b/det;ai11=A00/det
        w0=u;w1=-b*u/c+e;f=c*abs(e)
        j=h*u*u+c*e*e;lower=j-f*f/c
        G=1/c+(sqrt_up(w0*w0+w1*w1)+f/c)**2/lower
        assert G>=ai00 and G>=ai11
        assert (G-ai00)*(G-ai11)-ai01*ai01>=0
        ws=-b*u/c
        assert ai00==u*u/lower
        assert ai01==u*ws/lower
        assert ai11==1/c+ws*ws/lower
        for s0,s1 in ((F(1,9),F(-2,13)),(F(7,11),F(3,17)),(F(-1,5),F(0))):
            exact_energy=ai00*s0*s0+2*ai01*s0*s1+ai11*s1*s1
            protected=abs(w0*s0+w1*s1)+f*abs(s1)/c
            energy_bound=s1*s1/c+protected*protected/lower
            assert exact_energy<=energy_bound
        inverse_checks+=1
    return {'exact_channel_remainder_identities':count,
            'nonunit_trace_full_inverse_examples':inverse_checks,
            'trace_aware_residual_energy_examples':3*inverse_checks}
def row(cert_path,terms):
    raw=cert_path.read_bytes();d=json.loads(raw);sector=d['sector']
    assert hashlib.sha256(raw).hexdigest()==PINS[sector]
    assert d['cutoff']==R and d['remote_start']==0
    assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
    gamma=F(d['fullQ_floor_rational']);rho=F(d['relative_trace_fro_upper_rational'])
    assert 0<=rho<1
    caps={k:F(v) for k,v in d['bounds_rational'].items()}
    matrix=[[F(x) for x in r] for r in d['M_point_decimal']]
    j=min(matrix[i][i]-sum(abs(matrix[i][k]) for k in range(6) if k!=i) for i in range(6))
    nu=rho/(1-rho)
    alpha=caps['assembly_J']+2*caps['assembly_beta']+caps['assembly_eta']
    mn=max(sum(abs(x) for x in r) for r in matrix)
    trace=nu*(2+nu)*(mn+alpha)
    f=caps['graph_residual_fro']/(1-rho)
    a=caps['assembly_J']+trace+f*f/gamma
    assert a==F(d['leading_capacity_interval']['stationary_block_errors_rational']['a'])
    assert j==F(d['leading_capacity_interval']['J_lower_rational'])
    assert j>a
    w=sqrt_up(F(d['graph_vector_norm2_rational']))/(1-rho)
    G=up(1/gamma+(w+f/gamma)**2/(j-a))
    chi2=up(400+F(1024*N,T)*G);chi=sqrt_up(chi2)
    assert chi<21
    # Geometric remainder applies only beyond twice R; near coupling is exact.
    hs2=F(50)*(1+F(1,R))*F(1,2**(4*terms))
    tau=sqrt_up(G*hs2)
    epsilon=up(2*chi*tau+tau*tau)
    lo,hi=map(F,d['leading_capacity_interval']['interval_rational'])
    assert 0<lo<hi
    midpoint=(lo+hi)/2;radius=(hi-lo)/2
    first=2*R+(1 if sector=='even-v' else 2)
    U=F(1,first*first)+F(1,2*first)
    coefficient_error=up(radius*U)
    combined=up(epsilon+coefficient_error)
    trial_norm=F('1e-3')
    action=up(combined*trial_norm)
    quadratic=up(combined*trial_norm*trial_norm)
    assert epsilon<F('1e-8') and combined<1
    assert action<F('1e-10')
    remaining=F('1e-10')-action
    projected_target=F('4e-19' if sector=='even-v' else '1e-18')
    graph_dot_target=F('8e-13')
    energy_target=up(projected_target**2/gamma+
        (graph_dot_target/(1-rho)+f*projected_target/gamma)**2/(j-a))
    assert energy_target<F('2e-24') and chi+tau<21
    lift_action=up((chi+tau)*sqrt_up(energy_target))
    other_action=F('3e-11')
    total_action=up(action+lift_action+other_action)
    assert total_action<F('1e-10')
    stationary=up(2*F('2e-10')*trial_norm+trial_norm*total_action)
    assert stationary<F('5e-12')
    result={'sector':sector,'certificate_sha256':PINS[sector],
      'finite_full_A_inverse_norm_upper':G,'finite_exact_stationary_J_floor_lower':j-a,
      'exact_coupling_A_inverse_half_norm2_upper':chi2,
      'geometric_remainder_HS_norm2_upper':hs2,
      'inverse_weighted_remainder_norm_upper':tau,
      'whole_S_geometric_model_operator_error_upper':epsilon,
      'far_u_norm2_upper':U,'M11_exact_midpoint':midpoint,
      'M11_interval_radius':radius,'far_M11_midpoint_operator_error_upper':coefficient_error,
      'combined_geometric_and_M11_operator_error_upper':combined,
      'trial_norm_ceiling':trial_norm,'combined_action_error_upper_at_trial_ceiling':action,
      'combined_quadratic_error_upper_at_trial_ceiling':quadratic,
      'remaining_action_error_budget_for_other_channels':remaining,
      'model_S_floor_lower':1-combined,
      'finite_lift_projected_residual_target':projected_target,
      'finite_lift_represented_graph_dot_target':graph_dot_target,
      'finite_lift_energy_error_target_upper':energy_target,
      'finite_lift_remote_action_error_target_upper':lift_action,
      'other_action_arithmetic_target':other_action,
      'total_action_error_upper_if_targets_met':total_action,
      'stationary_source_and_action_error_upper_if_targets_met':stationary}
    out={k:(str(v) if isinstance(v,F) else v) for k,v in result.items()}
    out['display_approximate']={k:format(float(v),'.12g') for k,v in result.items() if isinstance(v,F)}
    return out
def build(root,terms):
    assert terms>0
    rows=[row(root/f'leading-256000-{s}.certificate.json',terms) for s in ('even-v','odd-v')]
    return {'schema':'cone.near-exact-far-channel-schur-model-budget.v1',
      'cutoff':R,'far_start_even':2*R+1,'far_start_odd':2*R+2,
      'geometric_terms':terms,'far_channel_count':2*terms+1,'proof_only_global_split_mode':str(T),
      'near_rows_retained_exact':True,'bare_remote_D_retained_exact':True,
      'algebra_checks':algebra_checks(),'cases':rows,
      'higher_channel_and_near_cross_arithmetic_certified':False,
      'finite_lift_targets_achieved':False,
      'M11_midpoint_error_charge_optional_for_cached_far_block':True,
      'infinite_remote_trial_constructed':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--payload-root',type=Path,required=True)
    p.add_argument('--terms',type=int,default=42)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=build(a.payload_root,a.terms)
    a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps([{'sector':r['sector'],'bounds':r['display_approximate']} for r in o['cases']],indent=2))
