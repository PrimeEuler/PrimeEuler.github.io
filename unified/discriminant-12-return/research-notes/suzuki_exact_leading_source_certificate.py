#!/usr/bin/env python3
"""Exact leading-coupling certificate, separate from the paired 1/n source."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import suzuki_exact_outward_certificate as base
from suzuki_exact_integer_source_action import ExactSource,dot,frac,norm2,sqrt_upper
from suzuki_trace_congruence_replay import inv,mul,tr,display,capacity
from suzuki_frozen_trial_far_outward import add,neg,times,recip,constant,enclose,atan_recip,hyperbolic,power,magnitude
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)

def leading_rhs(source,sector,bits=256):
    pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
    k=times(times(constant(-8 if sector=='odd-v' else 8),enclose(hyperbolic(sector=='odd-v'))),recip(pi))
    mid=(k[0]+k[1])/2;kp=F(mid.numerator*(1<<bits)//mid.denominator,1<<bits)
    ce=frac(source['c']['values'][0],source['c']['bits'])
    assert all(abs(frac(x,source['pole']['bits']))<2 for x in source['pole']['values'])
    values=[]
    for z,p in zip(source['z']['values'],source['pole']['values']):
        q=-ce*frac(z,source['z']['bits'])+kp*frac(p,source['pole']['bits'])
        values.append(q.numerator*(1<<bits)//q.denominator)
    kerr=max(abs(kp-k[0]),abs(kp-k[1]));ez,ep,ec=(base.CAPS[x] for x in ('z','pole','c'))
    per=abs(ce)*ez+ec*(11+ez)+abs(kp)*ep+kerr*(2+ep)+F(1,1<<bits)
    radius=sqrt_upper(F(len(values)))*per
    contract={'source_definition':'w1=-c*z+alpha*(4*h/pi)*pole over every finite mode',
              'k_physical_interval_rational':[str(x) for x in k],'k_point_rational':str(kp),
              'per_coordinate_physical_radius_rational':str(per),'rhs_l2_radius_rational':str(radius),
              'rhs_dyadic_bits':bits,'source_scalar_parents':['v14.123','v14.165','v14.168']}
    return {'bits':bits,'values':values},radius,contract

def certificate(source,vectors,p,normalizer,sector,kernel_bits=256,actions=None):
    cutoff=2*len(source['modes']);assert 8000<=cutoff<=256000
    if actions is None:
        engine=ExactSource(source,kernel_bits);actions=[engine.action(v) for v in vectors]
    # Base RHS is identically zero; only operator/graph/trace geometry is reused.
    # Every source-dependent term, charge and flag is recomputed below.
    out=base.certificate(source,vectors,p,normalizer,sector,cutoff,kernel_bits,actions)
    g,dg,contract=leading_rhs(source,sector)
    gram=[[dot(a,b) for b in p] for a in p];gi=inv(gram)
    m=[[dot(vectors[i],actions[j]) for j in range(7)] for i in range(7)]
    vg=[dot(v,g) for v in vectors]
    for i in range(7):m[i][6]-=vg[i];m[6][i]-=vg[i]
    assert m==tr(m)
    raw=base.subtract(actions[6],g);q=[[base.support_dot(pc,raw)] for pc in p]
    r6=norm2(raw)-mul(tr(q),mul(gi,q))[0][0];assert r6>=0
    w2=F(out['graph_vector_norm2_rational']);u2=F(out['source_trial_norm2_rational'])
    wn,un=sqrt_upper(w2),sqrt_upper(u2);da=F(out['operator_radius_rational'])
    b={k:F(v) for k,v in out['bounds_rational'].items()};round_charge=F(1,10**100)
    b['assembly_beta']=da*wn*un+dg*wn+6*round_charge
    b['assembly_eta']=da*u2+2*dg*un+round_charge
    b['source_residual_l2']=sqrt_upper(r6)+da*un+dg
    checks={k:b[k]<=base.TARGETS[k] for k in base.TARGETS}
    checks['relative_trace']=F(out['relative_trace_fro_upper_rational'])<=F('1e-20')
    out.update({'schema':'cone.exact-leading-source-outward-certificate.v1','remote_start':0,
                'physical_leading_source_contract':contract,
                'fullQ_floor_rational':str(F('2.37e-13' if sector=='even-v' else '4.15e-12')),
                'fullQ_floor_parents':['v14.174','v14.175','v14.177'],
                'M_point_decimal':[[base.decimal_floor(x) for x in row] for row in m],
                'source_vector_radius_rational':str(dg),
                'bounds_rational':{k:str(v) for k,v in b.items()},'bounds_display':{k:display(v) for k,v in b.items()},
                'point_projected_residual_norm2_rational':out['point_projected_residual_norm2_rational'][:6]+[str(r6)],
                'checks_exact':checks,'all_six_numerical_targets_met':all(checks.values()),
                'guardrail':'Full finite leading source only; not the paired 1/n source. Independent source-contract audit required. Infinite parity capacity remainder not certified.'})
    return out

def capacity_interval(cert):
    assert cert['schema']=='cone.exact-leading-source-outward-certificate.v1'
    assert cert['all_six_numerical_targets_met']
    m=[[F(x) for x in row] for row in cert['M_point_decimal']]
    j=min(m[i][i]-sum(abs(m[i][k]) for k in range(6) if k!=i) for i in range(6))
    q=sum(abs(m[i][6]) for i in range(6));mn=max(sum(abs(x) for x in row) for row in m)
    caps={k:F(v) for k,v in cert['bounds_rational'].items()}
    rho=F(cert['relative_trace_fro_upper_rational']);nu=rho/(1-rho);gamma=F(cert['fullQ_floor_rational'])
    alpha=caps['assembly_J']+2*caps['assembly_beta']+caps['assembly_eta']
    charge=nu*(2+nu)*(mn+alpha);f=caps['graph_residual_fro']/(1-rho)
    s=caps['source_residual_l2']+caps['graph_residual_fro']*nu
    a=caps['assembly_J']+charge+f*f/gamma
    b=caps['assembly_beta']+charge+f*s/gamma
    c=caps['assembly_eta']+charge+s*s/gamma
    assert j>a
    error=c+b*(2*q+b)/(j-a)+a*q*q/(j*(j-a));point=capacity(m)
    return {'point_rational':str(point),'error_upper_rational':str(error),
            'interval_rational':[str(point-error),str(point+error)],'point_display':display(point),
            'error_upper_display':display(error),'J_lower_rational':str(j),
            'stationary_block_errors_rational':{'a':str(a),'b':str(b),'c':str(c)}}

def main():
    p=argparse.ArgumentParser();p.add_argument('--snapshot',required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    a=p.parse_args();meta,s,v,P=base.read_snapshot(a.snapshot)
    assert meta['remote_start']==0 and meta['normalizer']['offset_scale']=='0'
    o=certificate(s,v,P,meta['normalizer'],meta['sector'],meta['kernel_bits'])
    o['leading_capacity_interval']=capacity_interval(o)
    raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'all_targets_met':o['all_six_numerical_targets_met'],
                      'leading_capacity':o['leading_capacity_interval']['point_display'],
                      'capacity_error':o['leading_capacity_interval']['error_upper_display']},indent=2))
if __name__=='__main__':main()
