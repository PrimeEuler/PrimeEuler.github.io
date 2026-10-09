#!/usr/bin/env python3
"""Exact corner consumer, input contract, and zero-trial box obstruction."""
import argparse,hashlib,itertools,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
local=Path(__file__).resolve().parents[1]/'producers'
if local.is_dir():sys.path.insert(0,str(local))
from suzuki_trace_congruence_replay import display

def interval(x):
    x=tuple(F(t) for t in x);assert len(x)==2 and x[0]<=x[1];return x

def dyadic_outward(lo,hi,bits=192):
    scale=1<<bits
    return F(lo.numerator*scale//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)

def H(a,b,c,ke,ko):return a-b-c*(b*ke+a*ko+a*b)

def corners(box,fn):
    values=[fn(*x) for x in itertools.product(*box)];return min(values),max(values)

def enclose(c,ke,ko,ve,vo,ee,eo,h0=None):
    c,ke,ko,ve,vo=map(interval,(c,ke,ko,ve,vo));ee,eo=F(ee),F(eo)
    assert c[0]>0 and ee>=0 and eo>=0
    # Physical lambda>=0 cuts the outer box, including negative stationary v.
    le=(max(F(0),ve[0]),ve[1]+ee);lo=(max(F(0),vo[0]),vo[1]+eo)
    assert le[0]<=le[1] and lo[0]<=lo[1], 'inconsistent lambda bounds'
    direct=corners((le,lo,c,ke,ko),H)
    h0=interval(h0) if h0 is not None else corners((ve,vo,c,ke,ko),H)
    # Retain a producer-supplied correlated H0; enclose only the correction.
    rem=corners((ve,vo,c,ke,ko,(F(0),ee),(F(0),eo)),
        lambda a,b,c,k,l,x,y:x*(1-c*(l+b))-y*(1+c*(k+a))-c*x*y)
    decomposed=(h0[0]+rem[0],h0[1]+rem[1])
    out=(max(direct[0],decomposed[0]),min(direct[1],decomposed[1]))
    assert out[0]<=out[1], 'inconsistent paired inputs'
    return out

def checks():
    # Independent interior sampling includes v<0 and coefficient sign reversals.
    cases=[((F(1),F(2)),(F(0),F(1)),(F(0),F(1)),(F(-1),F(2)),(F(-2),F(1)),F(3),F(4)),
           ((F(3),F(4)),(F(-2),F(3)),(F(-3),F(2)),(F(0),F(1)),(F(0),F(2)),F(1),F(2))]
    count=0
    for c,ke,ko,ve,vo,ee,eo in cases:
        lo,hi=enclose(c,ke,ko,ve,vo,ee,eo)
        grid=lambda b:(b[0],sum(b)/2,b[1])
        for a,b,g,k,l,x,y in itertools.product(grid(ve),grid(vo),grid(c),grid(ke),grid(ko),grid((F(0),ee)),grid((F(0),eo))):
            if a+x<0 or b+y<0:continue
            value=H(a+x,b+y,g,k,l);assert lo<=value<=hi;count+=1
    # Independent closed-form point case, which must be enclosed exactly.
    exact=H(F(1,7),F(2,11),F(3,5),F(1,13),F(1,17))
    box=enclose((F(3,5),)*2,(F(1,13),)*2,(F(1,17),)*2,(F(1,7),)*2,(F(2,11),)*2,0,0)
    assert box==(exact,exact)
    residual_cap=(F('3e-5')+F('2e-10')+F('1e-10'))**2
    budget=F('2.9e-9')+F('1e-9')+F('1.00768e-9')+640*F('1e-18')
    assert residual_cap<F('1e-9') and budget<F('5e-9')
    assert (2*F('2e-10')+F('1e-10'))*F('0.01')==F('5e-12')
    return {'interior_exact_rational_checks':count,'negative_v_and_coefficient_sign_cases':2,'zero_gap_point_exact':True,
      'sufficient_residual_gap_cap_rational':str(residual_cap),
      'sufficient_DeltaQ_abs_upper_rational':str(budget),'sufficient_budget_lt_5e_minus9_exact':True}

def build(finite,transport,farroot):
    fraw=finite.read_bytes();traw=transport.read_bytes();f=json.loads(fraw);t=json.loads(traw)
    coeff=dyadic_outward(*map(F,f['C_S_interval_rational']))
    assert coeff[1]<=640
    endpoint={r['sector']:r for r in f['paired_capacity_endpoints']}
    trans={r['sector']:r for r in t['cases']};rows=[];ks={}
    for sector,short in [('even-v','even'),('odd-v','odd')]:
        e=endpoint[sector];point=F(e['capacity_point_rational']);err=F(e['capacity_error_upper_rational'])
        ki=dyadic_outward(point-err,point+err);assert 0<ki[0]<=ki[1]<F('2e-6');ks[sector]=ki
        path=farroot/('frozen256-'+short+'-far.json');raw=path.read_bytes();far=json.loads(raw)
        eta=F(trans[sector]['source_transport_eta_upper_rational'])
        lower=max(F(0),F(far['far_norm_lower_rational'])-eta)
        assert lower**2>F('1e-6')
        rows.append({'sector':sector,'finite_K_interval_rational':[str(x) for x in ki],
          'finite_inverse_transport_eta_rational':str(eta),
          'represented_far_input_sha256':hashlib.sha256(raw).hexdigest(),
          'exact_physical_far_residual_norm_lower_rational':str(lower),
          'exact_physical_far_residual_energy_lower_rational':str(lower**2),
          'exact_physical_far_residual_energy_lower_display':display(lower**2),
          'exact_far_energy_gt_1e_minus6':True,
          'remote_trial':None,'source_assembly_eta':None,'operator_action_delta':None,
          'stationary_v_interval':None,'residual_norm_upper':None})
    # y=0 has v=0 and r=rho. Any valid E_even must exceed 1e-6.
    # The independent epsilon box contains the corner (1e-6,0).
    corner=F('1e-6')*(1-coeff[1]*ks['odd-v'][1])
    assert corner>F('0.99e-6')>F('5e-9')
    return {'schema':'cone.paired-variational-input-contract.v1',
      'finite_input_sha256':hashlib.sha256(fraw).hexdigest(),
      'transport_input_sha256':hashlib.sha256(traw).hexdigest(),
      'C_S_interval_rational':[str(x) for x in coeff],
      'cases':rows,'exact_consumer_checks':checks(),
      'zero_trial_independent_box_required_positive_corner_lower_rational':str(corner),
      'zero_trial_independent_box_cannot_close_5e_minus9':True,
      'zero_trial_obstruction_scope':'A required corner in an independent epsilon box, not a lower bound on actual lambda or actual DeltaQ.',
      'numerical_remote_trial_ready':False,'infinite_capacity_tail_closed':False,
      'acceptance':'both endpoints from enclose() must lie in [-5e-9,5e-9]; all trial/source/operator bounds must first be supplied and certified.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--finite',type=Path,required=True);p.add_argument('--transport',type=Path,required=True);p.add_argument('--far-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=build(a.finite,a.transport,a.far_root);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'exact_checks':o['exact_consumer_checks'],'exact_far_lower_energy':[r['exact_physical_far_residual_energy_lower_display'] for r in o['cases']],'zero_trial_box_cannot_close':True,'remote_trial_ready':False},indent=2))
