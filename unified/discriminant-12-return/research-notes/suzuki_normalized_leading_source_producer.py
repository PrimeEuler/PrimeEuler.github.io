#!/usr/bin/env python3
"""Direct exact-action normalized source solve for finite leading w1 capacity."""
import argparse
import json
from pathlib import Path
import time
import mpmath as mp
import numpy as np
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator
from suzuki_normalized_joint_reduction_producer import frozen_normalizer,solve_joint,DPS,LD
from suzuki_ldd_source_operator import dot_columns,hp_parity_data_ld,split_mpf_ld
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_exact_integer_source_action import ExactBackend
from suzuki_exact_outward_certificate import p_families,write_snapshot
from suzuki_exact_leading_source_certificate import leading_rhs,certificate,capacity_interval

def main():
    a=argparse.ArgumentParser();a.add_argument('--sector',choices=['even-v','odd-v'],required=True)
    a.add_argument('--cutoff',type=int,default=32000);a.add_argument('--anchor-root',type=Path,required=True)
    a.add_argument('--output',type=Path,required=True);k=a.parse_args()
    assert k.cutoff==32000
    started=time.monotonic()
    progress=lambda o:print(json.dumps({'sector':k.sector,'cutoff':k.cutoff,**o}),flush=True)
    modes=modes_for(k.sector,k.cutoff);P=embedded_P(k.sector,modes)
    ph,pl=dot_columns(P,None,P,None);_,_,gi=mp_inverse_split(ph,pl,DPS)
    gif=np.array([[float(gi[i,j]) for j in range(6)] for i in range(6)])
    _,proj,op,_=fixed_operator(modes,k.sector,P,gif)
    progress({'stage':'source scalar construction'})
    data=hp_parity_data_ld(modes,k.sector,dps=DPS,arch_terms=200,correction_terms=50)
    backend=ExactBackend(data);g,_,_=leading_rhs(backend.source,k.sector)
    gh=np.empty(len(modes),dtype=LD);gl=np.empty_like(gh)
    normal=frozen_normalizer(k.sector,k.anchor_root,'0')
    k.output.parent.mkdir(parents=True,exist_ok=True)
    trace=k.output.with_suffix('.trace.json.gz');snapshot=k.output.with_suffix('.full.zip')
    with mp.workdps(DPS):
        for i,value in enumerate(g['values']):
            gh[i],gl[i]=split_mpf_ld(mp.mpf(value)/mp.mpf(2)**g['bits'])
        progress({'stage':'direct normalized leading RHS solve'})
        row=solve_joint(P,op,proj,backend.action_arrays,gh,gl,mp.matrix(normal['T']),
                        mp.matrix(normal['v']),1,progress,normal,trace)
    vectors=backend.last_inputs
    cert=certificate(backend.source,vectors,p_families(P),normal,k.sector,
                     backend.engine.kernel_bits,backend.last_outputs)
    assert cert['all_six_numerical_targets_met']
    trace_cert=row['represented_trial_trace_certificate']
    assert cert['frozen_base_P_sha256']==trace_cert['frozen_base_P_sha256']
    assert cert['relative_trace_fro_upper_rational']==trace_cert['relative_defect_fro_upper_rational']
    cert['leading_capacity_interval']=capacity_interval(cert)
    sha=write_snapshot(snapshot,backend.source,vectors,p_families(P),normal,k.sector,0,backend.engine.kernel_bits)
    k.output.with_suffix('.certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    out={'schema':'cone.normalized-leading-source-payload.v1','sector':k.sector,'cutoff':k.cutoff,
         'normalizer':normal,'certificate':cert,'snapshot_sha256':sha,
         'source_definition':cert['physical_leading_source_contract']['source_definition'],
         'elapsed_seconds':time.monotonic()-started,'infinite_capacity_tail_closed':False}
    k.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'leading_capacity':cert['leading_capacity_interval']['point_display'],
                      'capacity_error':cert['leading_capacity_interval']['error_upper_display'],
                      'all_caps_pass':True}),flush=True)
if __name__=='__main__':main()
