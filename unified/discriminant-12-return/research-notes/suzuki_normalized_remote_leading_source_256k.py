#!/usr/bin/env python3
"""Dedicated exact-action normalized leading w1 solve on the actual 256k front."""
import argparse
import json
import base64
import hashlib
from pathlib import Path
import time
import mpmath as mp
import numpy as np
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator
from suzuki_normalized_joint_reduction_producer import frozen_normalizer,solve_joint,DPS,LD
from suzuki_ldd_source_operator import dot_columns,hp_parity_data_ld,split_mpf_ld
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_exact_integer_source_action import ExactBackend
from suzuki_exact_outward_certificate import p_families,write_snapshot,p_hash,P_HASHES
from suzuki_exact_leading_source_certificate import leading_rhs,certificate,capacity_interval

def frozen_basis(sector,modes,root):
    raw=(root/('frozen-base-P-'+sector+'.json')).read_bytes()
    meta=json.loads(raw)
    assert meta['schema']=='cone.exact-frozen-six-plane-binary64.v1'
    assert meta['sector']==sector and meta['rows']==2000 and meta['columns']==6
    assert meta['byte_order']=='little' and meta['layout']=='row-major'
    data=base64.b64decode(meta['binary64_rowmajor_base64'],validate=True)
    assert len(data)==96000
    assert hashlib.sha256(data).hexdigest()==meta['frozen_base_P_sha256']==P_HASHES[sector]
    P=np.zeros((len(modes),6),dtype=float)
    P[:2000]=np.frombuffer(data,dtype='<f8').reshape(2000,6)
    assert np.all(np.isfinite(P))
    return P,hashlib.sha256(raw).hexdigest()

def main():
    a=argparse.ArgumentParser();a.add_argument('--sector',choices=['even-v','odd-v'],required=True)
    a.add_argument('--cutoff',type=int,default=256000);a.add_argument('--anchor-root',type=Path,required=True)
    a.add_argument('--output',type=Path,required=True)
    a.add_argument('--frozen-P-root',type=Path,default=Path(__file__).resolve().parent/'payloads'/'frozen_base_P_actual256')
    a.add_argument('--preflight-only',action='store_true');k=a.parse_args()
    if k.cutoff!=256000:a.error('this dedicated producer requires cutoff 256000')
    started=time.monotonic()
    progress=lambda o:print(json.dumps({'sector':k.sector,'cutoff':k.cutoff,**o}),flush=True)
    modes=modes_for(k.sector,k.cutoff);P,basis_file_sha=frozen_basis(k.sector,modes,k.frozen_P_root)
    assert len(modes)==128000 and P.shape==(128000,6)
    assert int(modes[0])==(1 if k.sector=='even-v' else 2)
    assert int(modes[-1])==(255999 if k.sector=='even-v' else 256000)
    frozen_hash=p_hash(p_families(P))
    assert frozen_hash==P_HASHES[k.sector]
    if np.finfo(np.longdouble).nmant<63:raise RuntimeError('64-bit long-double significand required')
    normal=frozen_normalizer(k.sector,k.anchor_root,'0')
    assert normal['offset_scale']=='0'
    if k.preflight_only:
        check={'schema':'cone.actual256-leading-producer-preflight.v1','sector':k.sector,
               'cutoff':k.cutoff,'dimension':len(modes),'frozen_base_P_sha256':frozen_hash,
               'first_mode':int(modes[0]),'last_mode':int(modes[-1]),
               'frozen_basis_payload_sha256':basis_file_sha,
               'normalizer':normal,'longdouble_significand_bits':int(np.finfo(np.longdouble).nmant),
               'full_numerical_solve_executed':False}
        k.output.parent.mkdir(parents=True,exist_ok=True)
        k.output.write_text(json.dumps(check,indent=2,sort_keys=True)+'\n')
        print(json.dumps(check,indent=2,sort_keys=True));return
    ph,pl=dot_columns(P,None,P,None);_,_,gi=mp_inverse_split(ph,pl,DPS)
    gif=np.array([[float(gi[i,j]) for j in range(6)] for i in range(6)])
    _,proj,op,_=fixed_operator(modes,k.sector,P,gif)
    progress({'stage':'source scalar construction'})
    data=hp_parity_data_ld(modes,k.sector,dps=DPS,arch_terms=200,correction_terms=50)
    backend=ExactBackend(data);g,_,_=leading_rhs(backend.source,k.sector)
    gh=np.empty(len(modes),dtype=LD);gl=np.empty_like(gh)
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
