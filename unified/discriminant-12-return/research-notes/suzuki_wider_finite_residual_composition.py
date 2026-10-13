#!/usr/bin/env python3
"""Actual changed finite residual; original infinite-tail action included once."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,base64
from suzuki_returned_tail_residual_composition import read,upper,norm,write
S=1<<256
SOURCE={'even-v':'40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80','odd-v':'41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f'}
LIFT={'even-v':'98df9edfee779854e540192a2941d43e44ab85556598c6b76b7d48f0e0e50df3','odd-v':'99a741a41932261569db364698f5998a52204fdf1aad872e972afa0857075075'}
TAIL1={'even-v':'af8ddb14f7499856b55a1904d715157cb6047ba46982ab3502b4b36d48fc8490','odd-v':'38c1dbd4c95fa810eebe1c7c001b90107305e69785e919c1e2703e83f8e29604'}
CAND={'even-v':'fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05','odd-v':'b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967'}
def sha(b):return hashlib.sha256(b).hexdigest()
def pinned(path,pin):
 b=path.read_bytes();assert sha(b)==pin;return json.loads(b)
def decode(raw,spec):
 assert len(raw)==spec['bytes']==spec['count']*spec['width'] and sha(raw)==spec['sha256'] and spec['bits']==256
 return [int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])]
def run(compact,compact_cert_sha,compact_buffer_sha,tail1,tail23,source,lift,sector,out):
 start=1 if sector=='even-v' else 2;shift=start-1
 cert=pinned(compact/f'wide-compact-near-middle-window-{sector}.json',compact_cert_sha);spec=cert['buffer']
 assert cert['schema']=='cone.wider-compact-near-middle-window-action.v1' and cert['sector']==sector and cert['candidate_sha256']==CAND[sector]
 assert cert['actual_CI_lift_certificate_sha256']==LIFT[sector] and cert['full_source_certificate_sha256']==SOURCE[sector]
 assert cert['artificial_Hankel_self_removed_with_same_reciprocal'] and cert['compact_near_middle_window_output_rows_evaluated'] and not cert['infinite_seed_tail_action_included']
 assert cert['first_output_mode']==256000+start and cert['last_output_mode']==1040382+start and cert['complete_output_rows']==392192 and spec['count']==392192 and spec['sha256']==compact_buffer_sha
 cp=decode((compact/spec['file']).read_bytes(),spec)
 t1=pinned(tail1/f'region1-close-plus-far-action-{sector}.json',TAIL1[sector]);sp=t1['composed_action_buffer'];tp=decode((tail1/sp['file']).read_bytes(),sp)
 assert len(tp)==128000 and t1['output_first_mode']==256000+start and t1['far_input_action_included_once'] and t1['far_pole_included_once']
 errors=[F(t1['rational']['composed_region1_action_l2_error_upper'])]
 manifest,msha=read(tail23,'manifest.json');tail_hashes=[TAIL1[sector]]
 for region,count,first in ((2,256000,512000+start),(3,8192,1024000+start)):
  d,dsha=read(tail23,f'region{region}-action-{sector}.json');sp=d['point_buffer'];ms=manifest['buffers'][sp['file']]
  raw=base64.b64decode(b''.join((tail23/p).read_bytes() for p in ms['parts']),validate=True)
  assert len(raw)==ms['bytes'] and sha(raw)==ms['sha256'] and sp['count']==d['output_count']==count and d['output_first_mode']==first
  assert F((first+2*(count-1))**2,d['tail_start']**2)<F('0.258063')
  tp+=decode(raw,sp);errors.append(F(d['rational']['complete_l2_error_upper']));tail_hashes.append(dsha)
 assert len(tp)==len(cp)==392192
 residual=[S//(256000+start+2*i-shift)-a-b for i,(a,b) in enumerate(zip(cp,tp))]
 old_source=pinned(source/f'full-stationary-source-{sector}.json',SOURCE[sector]);new_lift=pinned(lift/f'wider-correction-finite-lift-{sector}.json',LIFT[sector]);assert new_lift['finite_lift_certified'] and new_lift['rhs_point_sha256']=={'even-v':'c47680677bc4a13ba9658bac2c1ebcf47da6b97181e0547f8f29bdf42f3da134','odd-v':'72636f6caff65201c9831f5d84d9f001d24db15d44b725ad309bfa71bcbcd144'}[sector]
 T=F(old_source['rational']['whole_remote_source_transport_upper'])+F(new_lift['rational']['finite_lift_remote_action_charge_upper'])
 C=F(cert['rational']['complete_compact_near_middle_window_action_error_upper']);assert C<F('3e-11')
 E=upper(sum(e*e for e in errors));bare=upper(F(392192))/S;error=C+E+bare
 lo,hi=norm(residual);physical_hi=hi+error;physical_lo=max(F(0),lo-error);true_hi=physical_hi+T;true_lo=max(F(0),physical_lo-T)
 out.mkdir(parents=True,exist_ok=True);buffers={};bounds={};cursor=0
 for label,count,e in zip(('Near','Middle','Far-window'),(128000,256000,8192),errors):
  values=residual[cursor:cursor+count];l,h=norm(values);region_error=C+e+upper(F(count))/S
  bounds[label]={'point_lower':str(l),'point_upper':str(h),'physical_subset_lower':str(max(F(0),l-region_error)),'physical_subset_upper':str(h+region_error)}
  buffers[label]=write(out,sector,'wider-'+label.lower()+'-residual',values);cursor+=count
 assert cursor==392192
 allowance=F(0)
 if true_hi<F('3e-5'):
  q=(F('3e-5')-T)**2-physical_hi**2;assert q>0;allowance=max(F(0),upper(q)-F(1,S));assert allowance**2<=q
 vals={'finite_point_norm_lower':lo,'finite_point_norm_upper':hi,'compact_finite_output_error_upper':C,'old_infinite_seed_finite_output_error_upper':E,'bare_source_floor_error_upper':bare,'complete_finite_physical_error_upper':error,'finite_physical_residual_lower':physical_lo,'finite_physical_residual_upper':physical_hi,'source_transport_upper':F(old_source['rational']['whole_remote_source_transport_upper']),'new_lift_transport_upper':F(new_lift['rational']['finite_lift_remote_action_charge_upper']),'global_source_and_new_lift_transport_once':T,'finite_evaluated_Schur_residual_lower':true_lo,'finite_evaluated_Schur_residual_upper':true_hi,'certified_beyond_window_physical_residual_allowance':allowance}
 return {'schema':'cone.wider-finite-residual-composition.v1','sector':sector,'new_compact_certificate_sha256':compact_cert_sha,'new_compact_buffer_sha256':compact_buffer_sha,'original_infinite_seed_action_certificate_sha256':tail_hashes,'tail_manifest_sha256':msha,'source_certificate_sha256':SOURCE[sector],'new_lift_certificate_sha256':LIFT[sector],'candidate_sha256':CAND[sector],'buffers':buffers,'region_bounds':bounds,'rational':{k:str(v) for k,v in vals.items()},'display_approximate':{k:float(v) for k,v in vals.items()},'global_transport_added_once_outside_regional_quadrature':True,'source_bare_formula':'1/n' if start==1 else '1/(n-1)','finite_subset_upper_below_3e_minus5':true_hi<F('3e-5'),'finite_subset_lower_above_3e_minus5':true_lo>F('3e-5'),'beyond_window_residual_evaluated':False,'whole_residual_acceptance_certified':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('compact-root','tail1-root','tail23-root','source-root','lift-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--compact-certificate-sha256',required=True);p.add_argument('--compact-buffer-sha256',required=True);p.add_argument('--sector',choices=tuple(SOURCE),required=True);a=p.parse_args()
 d=run(a.compact_root,a.compact_certificate_sha256,a.compact_buffer_sha256,a.tail1_root,a.tail23_root,a.source_root,a.lift_root,a.sector,a.output_root)
 (a.output_root/f'wider-finite-residual-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d['display_approximate']),flush=True)
