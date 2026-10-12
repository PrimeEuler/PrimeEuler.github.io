#!/usr/bin/env python3
"""Directed a-start Region-1 far action and composition with v14.291 close rows."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
from suzuki_bulk_action_z import evaluate as z_eval
from suzuki_near_trial_lift_rhs import floor,writebuffer
from suzuki_exact_integer_source_action import sqrt_upper
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure

PINS={
 'moments':{'even-v':'d141dcdaafcd6b4d45315d17d009b7fd60953ae9b5707b1ac50c068b72c6a02d','odd-v':'c9ece88832d67f5c4a803d8063dc53bb41b037f4c42e75433424137dbf95179e'},
 'close_json':{'even-v':'551dab1fe43871db22630a9afad706f0c30ef71eb8c97b7fd8cb52bf2256dedb','odd-v':'dbf0caa2c9d841cb3417df463bfb99d19c07d9658a09f1deabe05e408d2e5271'},
 'close_bin':{'even-v':'abb858deb7344c99b578a7983b702e0c7207b1ce11ad899310fb054363ad7b59','odd-v':'1d290adc9d9b680b9c6ba0fb5483e90b4a0da6a399831fc25de333fc4e0087cf'},
 'remainder':'e8d00dc1b299c033bd49354e564e92bcad9d5526b32c972e2fc6ee2431eed65c'}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def interval(row):return tuple(F(x) for x in row['interval'])
def mul(a,b):
 q=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]];return min(q),max(q)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,q):return (a[0]*q,a[1]*q) if q>=0 else (a[1]*q,a[0]*q)
def poly(rows,x):
 h=interval(rows[-1])
 for row in reversed(rows[:-1]):h=plus(scale(h,x),interval(row))
 return h
def read_close(root,sector):
 jp=root/f'region1-close-action-{sector}.json';rawj=jp.read_bytes();assert sha(rawj)==PINS['close_json'][sector]
 cert=json.loads(rawj);s=cert['point_buffer'];bp=root/s['file'];raw=bp.read_bytes()
 assert sha(raw)==s['sha256']==PINS['close_bin'][sector] and len(raw)==s['bytes']
 vals=[int.from_bytes(raw[i:i+s['width']],'little',signed=True) for i in range(0,len(raw),s['width'])]
 assert len(vals)==s['count']==128000 and s['bits']==256
 return cert,vals
def run(moments_path,remainder_path,close_root,sector,out,limit=None):
 raw=moments_path.read_bytes();assert sha(raw)==PINS['moments'][sector];mom=json.loads(raw)
 rr=remainder_path.read_bytes();assert sha(rr)==PINS['remainder'];rem=json.loads(rr)
 rcase=next(x for x in rem['cases'] if x['sector']==sector)
 close,closevals=read_close(close_root,sector);start=1 if sector=='even-v' else 2
 a=mom['first_tail_mode'];assert a==1024002+start and close['excluded_far_input_first_mode']==a
 assert [x['j'] for x in mom['Ubar']]==list(range(42))==[x['j'] for x in mom['Vbar']]
 assert rcase['J']==42 and rcase['first_far_input_mode']==a and rcase['remote_region1_output_count']==128000
 pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
 ci=enclosure(*times(constant(2),recip(pi)),256)
 li=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi)),256)
 ti=enclosure(*times(recip(pi),recip(pi)),256)
 alpha=2 if sector=='even-v' else -2;P=interval(mom['P_tail']);count=128000 if limit is None else min(limit,128000)
 far=[];composed=[];maxrad=F(0);checks=[]
 for i in range(count):
  n=256000+start+2*i;q=F(n,a);x=q*q
  U=scale(poly(mom['Ubar'],x),q);V=poly(mom['Vbar'],x)
  zr=z_eval(n);z=(F(zr['lower_rational']),F(zr['upper_rational']))
  bracket=plus(U,scale(mul(z,V),-1));off=scale(mul(ci,bracket),F(1,a))
  # p_n=L*n/(n^2+t), monotone increasing in L and decreasing in t.
  p=(li[0]*n/(n*n+ti[1]),li[1]*n/(n*n+ti[0]));total=plus(off,scale(mul(p,P),alpha))
  point=floor((total[0]+total[1])/2,256);pf=F(point,1<<256)
  rad=max(abs(total[0]-pf),abs(total[1]-pf));maxrad=max(maxrad,rad)
  far.append(point);composed.append(closevals[i]+point)
  if i in (0,count//2,count-1):checks.append({'output_index':i,'mode':n,'directed_interval_contains_represented_point':total[0]<=pf<=total[1]})
  if (i+1)%16000==0:print(sector,'directed later-start Region1 rows',i+1,'/',count,flush=True)
 out.mkdir(parents=True,exist_ok=True);fs=writebuffer(out,sector,'region1-far-action',far,256);cs=writebuffer(out,sector,'region1-close-plus-far-action',composed,256)
 # The moment/scalar interval radius is uniformized over rows; v14.274 supplies the omitted geometric tail.
 interval_l2=sqrt_upper(F(count),256)*maxrad;geom_l2=F(rcase['rational']['far_offdiagonal_remainder_l2_upper'])
 close_l2=F(close['rational']['complete_close_action_l2_error_upper']);total_l2=close_l2+interval_l2+geom_l2
 return {'schema':'cone.infinite-seed-region1-close-plus-far-action.v1','sector':sector,
  'moments_sha256':PINS['moments'][sector],'weighted_remainder_sha256':PINS['remainder'],
  'close_certificate_sha256':PINS['close_json'][sector],'close_buffer_sha256':PINS['close_bin'][sector],
  'output_first_mode':256000+start,'output_count':count,'full_rectangle_evaluated':limit is None,
  'first_far_input_mode':a,'K':42,'far_action_buffer':fs,'composed_action_buffer':cs,
  'formula':'(c/a)*(sum q^(2j+1) Ubar_j-z_n sum q^(2j) Vbar_j)+alpha*p_n*P_tail, q=n/a; plus v14.274 geometric remainder',
  'rational':{'maximum_retained_far_interval_radius':str(maxrad),'retained_far_interval_l2_upper':str(interval_l2),
   'far_geometric_remainder_l2_upper':str(geom_l2),'close_action_l2_error_upper':str(close_l2),
   'composed_region1_action_l2_error_upper':str(total_l2)},'directed_row_checks':checks,
  'close_action_included':True,'far_input_action_included_once':True,'far_pole_included_once':True,
  'regions_2_3_included':False,'whole_infinite_action_evaluated':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('moments','remainder','close-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=('even-v','odd-v'),required=True);p.add_argument('--limit',type=int);a=p.parse_args()
 d=run(a.moments,a.remainder,a.close_root,a.sector,a.output_root,a.limit)
 (a.output_root/f'region1-close-plus-far-action-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'sector':a.sector,'rows':d['output_count'],'error':float(F(d['rational']['composed_region1_action_l2_error_upper']))}),flush=True)
