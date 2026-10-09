#!/usr/bin/env python3
"""Exact arithmetic for the near/far energy-weighted transport theorem."""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
local=Path(__file__).resolve().parents[1]/'producers'
if local.is_dir():sys.path.insert(0,str(local))
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_trace_congruence_replay import inv,mul,display

def rational_checks():
    # Independent exact block example: non-diagonal positive C and Schur >=I.
    C=[[F(2),F(1)],[F(1),F(3)]];B=[[F(1),F(2)],[F(3),F(-1)]]
    Bt=list(map(list,zip(*B)));T=mul(B,mul(inv(C),Bt))
    D=[[T[i][j]+F(i==j) for j in range(2)] for i in range(2)]
    e=[[F(2,7)],[F(-3,11)]];b=mul(B,e)
    energy=mul(list(map(list,zip(*e))),mul(C,e))[0][0]
    # Rowwise dual energy inequality and Schur positivity, exact fractions.
    for i in range(2):assert b[i][0]**2 <= energy*T[i][i] <= energy*D[i][i]
    return {'non_diagonal_block_example_exact':True,'near_row_dual_energy_checks':2}

def run(path):
    raw=path.read_bytes();o=json.loads(raw);R=256000;N=128000;cut=2**128
    assert cut>2*R and 128<R
    # ln(cut)=128 ln2<128; proved diagonal+offdiagonal cap <400.
    near_cap=F(400);far_hs2=F(1024*N,cut)
    rows=[]
    for r in o['cases']:
        gamma=F(r['finite_fullQ_floor_rational'])
        energy=F(r['corrected_finite_energy_error_upper_rational'])
        repair=F(r['trace_repair_norm_upper_rational'])
        near=sqrt_upper(near_cap*energy,bits=192)
        far=sqrt_upper(far_hs2*energy/gamma,bits=192)
        eta=23*repair+near+far
        old=F(r['remote_source_transport_eta_upper_rational'])
        assert eta<old and eta<F('2e-10')
        rows.append({'sector':r['sector'],'finite_energy_error_upper_rational':str(energy),
          'trace_repair_source_charge_rational':str(23*repair),
          'near_energy_source_charge_rational':str(near),
          'far_energy_source_charge_rational':str(far),
          'source_transport_eta_upper_rational':str(eta),
          'source_transport_eta_upper_display':display(eta),
          'source_transport_eta_squared_upper_rational':str(eta**2),
          'source_transport_eta_squared_upper_display':display(eta**2),
          'improvement_factor_lower_rational':str(old/eta),
          'eta_lt_2e_minus10_exact':True})
    return {'schema':'cone.energy-weighted-source-transport.v1',
      'input_sha256':hashlib.sha256(raw).hexdigest(),'analytical_split_mode':str(cut),
      'near_D_operator_upper_rational':str(near_cap),
      'far_B_squared_hilbert_schmidt_upper_rational':str(far_hs2),
      'exact_block_checks':rational_checks(),'cases':rows,
      'infinite_capacity_tail_closed':False,
      'scope':'Exact constrained finite-inverse transport only; remote source assembly and remote trials remain open.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=run(a.input);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps([{'sector':r['sector'],'eta':r['source_transport_eta_upper_display']} for r in o['cases']],indent=2))
