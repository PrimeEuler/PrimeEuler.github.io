#!/usr/bin/env python3
"""Exact trace repair and conservative finite-inverse/source transport."""
import argparse, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as F
local_producers=Path(__file__).resolve().parents[1]/'producers'
if local_producers.is_dir(): sys.path.insert(0,str(local_producers))
from suzuki_exact_outward_certificate import read_snapshot, support_dot
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_trace_congruence_replay import inv,mul,l1,display

def run(root):
    rows=[]
    for sector,gamma in [('even-v',F('2.37e-13')),('odd-v',F('4.15e-12'))]:
        stem='joint-256000-'+sector+'.trace-256000.full'
        snap=root/(stem+'.zip'); cert=root/(stem+'.certificate.json')
        meta,source,V,P=read_snapshot(snap)
        c=json.loads(cert.read_text())
        gram=[[support_dot(a,b) for b in P] for a in P]
        h=mul(inv(gram),[[support_dot(a,b) for b in V] for a in P])
        target=mul([[F(x) for x in row] for row in meta['normalizer']['T']],
                   [[F(x)] for x in meta['normalizer']['v']])
        hw=[row[:6] for row in h]
        d=mul(inv(hw),[[row[6]-t[0]] for row,t in zip(h,target)])
        assert mul(hw,d)==[[row[6]-t[0]] for row,t in zip(h,target)]
        dn=sqrt_upper(sum((row[0]**2 for row in d),F(0)))
        wn=sqrt_upper(F(c['graph_vector_norm2_rational']))
        repair=wn*dn
        s=F(c['bounds_rational']['source_residual_l2'])
        f=F(c['bounds_rational']['graph_residual_fro'])
        residual=s+f*dn
        error=residual/gamma
        total=repair+error
        # Physical cross-block norm <=23, as proved in the accompanying ledger.
        eta=23*total
        rows.append({'sector':sector,'snapshot_sha256':hashlib.sha256(snap.read_bytes()).hexdigest(),
          'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),
          'trace_repair_coefficients_rational':[str(row[0]) for row in d],
          'trace_repair_identity_exact':True,
          'trace_repair_norm_upper_rational':str(repair),
          'corrected_projected_residual_upper_rational':str(residual),
          'finite_fullQ_floor_rational':str(gamma),
          'finite_inverse_transport_norm_upper_rational':str(total),
          'finite_inverse_transport_norm_upper_display':display(total),
          'remote_source_transport_eta_upper_rational':str(eta),
          'remote_source_transport_eta_upper_display':display(eta),
          'corrected_finite_energy_error_upper_rational':str(residual**2/gamma)})
    return {'schema':'cone.exact-finite-trial-transport.v1','cases':rows,
      'physical_cross_block_norm_upper_rational':'23',
      'infinite_capacity_tail_closed':False,
      'scope':'Transport charge only; represented infinite residual still requires near/far construction.'}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--root',type=Path,required=True);a.add_argument('--output',type=Path,required=True)
    v=a.parse_args();o=run(v.root);v.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps([{k:r[k] for k in ('sector','finite_inverse_transport_norm_upper_display','remote_source_transport_eta_upper_display')} for r in o['cases']],indent=2))
