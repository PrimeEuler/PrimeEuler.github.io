#!/usr/bin/env python3
"""Exact represented Region-1 residual norm with directed physical/transport charges."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_near_trial_lift_rhs import writebuffer
PINS={"full-stationary-source-budget.json":"d5043959fae503df60631ef896377339ee3e5e6d","full-stationary-source-even-v.json":"c2e60dfcc4cef40df0de442542d048aca1c1b639","full-stationary-source-odd-v.json":"b5b347c4ff6b7977b57c69adc11279cb95398d8d","infinite-seed-compact-near-middle-even-v.json":"74f088ba44d0c2e665708d0c652d0efa7d5dc52a","infinite-seed-compact-near-middle-odd-v.json":"060a66c3f0ea5a9c0d48d30d986f8905c44f1dd9","infinite-seed-finite-lift-even-v.json":"871657c1351eda694687b4efda9fd5f9db331c2a","infinite-seed-finite-lift-odd-v.json":"9d78c953230a658a29c151fabe2d2b88b4e3b217","region1-close-plus-far-action-even-v.json":"ccb022846d19600fb79abb931741d1ec9174d4eb","region1-close-plus-far-action-odd-v.json":"863d87fbb4d51b6f5de4bbc94cfd4b7ed32dfa11"}
def load(root,name):
 raw=(root/name).read_bytes()
 assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==PINS[name]
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def buffer(root,spec):
 raw=(root/spec['file']).read_bytes();assert len(raw)==spec['bytes'] and hashlib.sha256(raw).hexdigest()==spec['sha256']
 assert spec['bits']==256
 vals=[int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])]
 assert len(vals)==spec['count'];return vals
def run(compactroot,tailroot,liftroot,sourceroot,sector,out):
 cc,csha=load(compactroot,f'infinite-seed-compact-near-middle-{sector}.json')
 tc,tsha=load(tailroot,f'region1-close-plus-far-action-{sector}.json')
 lc,lsha=load(liftroot,f'infinite-seed-finite-lift-{sector}.json')
 sc,ssha=load(sourceroot,f'full-stationary-source-{sector}.json')
 assert cc['physical_scalar_parameter_errors_included'] and not cc['infinite_seed_tail_action_included']
 assert tc['full_rectangle_evaluated'] and tc['far_input_action_included_once']
 cv=buffer(compactroot,cc['buffer']);tv=buffer(tailroot,tc['composed_action_buffer'])
 N=128000;S=1<<256;start=1 if sector=='even-v' else 2;assert len(cv)==384000 and len(tv)==N
 assert cc['first_output_mode']==tc['output_first_mode']==256000+start
 # g is the exact bare source, not rho's already-eliminated affine expansion.
 vals=[S//(256000+start+2*i-(1 if start==2 else 0))-cv[i]-tv[i] for i in range(N)]
 q=F(sum(v*v for v in vals),S*S);hi=sqrt_upper(q,256);lo=max(F(0),hi-F(1,S));assert lo*lo<=q<=hi*hi
 # The compact all-384000-row error is safely applied to this 128000-row subset.
 comp=F(cc['rational']['complete_compact_near_middle_action_error_upper'])
 tail=F(tc['rational']['composed_region1_action_l2_error_upper'])
 source_round=sqrt_upper(F(N),256)/S;physical=comp+tail+source_round
 # Same conservative source and finite inverse-energy transport as v14.248.
 source_transport=F(sc['rational']['whole_remote_source_transport_upper'])
 lift_transport=F(lc['rational']['finite_lift_remote_action_charge_upper'])
 total=physical+source_transport+lift_transport
 lower=max(F(0),lo-total);upper=hi+total
 out.mkdir(parents=True,exist_ok=True);spec=writebuffer(out,sector,'region1-residual',vals,256)
 return {'schema':'cone.actual-infinite-seed-region1-residual.v1','sector':sector,'compact_certificate_sha256':csha,'tail_certificate_sha256':tsha,'lift_certificate_sha256':lsha,'source_certificate_sha256':ssha,'point_buffer':spec,'output_first_mode':256000+start,'output_count':N,'formula':'r=g-D(compact)-D(infinite_seed_tail); g=1/n even-v,1/(n-1) odd-v; no extra lift or source moment','rational':{'represented_point_norm2':str(q),'point_norm_lower':str(lo),'point_norm_upper':str(hi),'compact_subset_action_error_upper':str(comp),'tail_region1_action_error_upper':str(tail),'bare_source_floor_error_upper':str(source_round),'physical_composition_error_upper':str(physical),'source_transport_upper':str(source_transport),'finite_lift_transport_upper':str(lift_transport),'complete_transport_upper':str(total),'true_Schur_region1_residual_lower':str(lower),'true_Schur_region1_residual_upper':str(upper)},'display_approximate':{'point_norm':float(hi),'true_region1_lower':float(lower),'true_region1_upper':float(upper)},'region1_above_unchanged_3e_minus5_target':lower>F('3e-5'),'region1_upper_below_3e_minus5':upper<F('3e-5'),'whole_residual_evaluated':False,'regions2_3_included':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('compact-root','tail-root','lift-root','source-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=('even-v','odd-v'),required=True);a=p.parse_args()
 d=run(a.compact_root,a.tail_root,a.lift_root,a.source_root,a.sector,a.output_root)
 (a.output_root/f'region1-residual-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 print(json.dumps(d['display_approximate']),flush=True)

