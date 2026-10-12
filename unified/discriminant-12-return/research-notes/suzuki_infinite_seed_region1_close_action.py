#!/usr/bin/env python3
"""Directed Region-1 close-input action and pole; excludes far inputs."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_bulk_action_z import evaluate as z_eval
from suzuki_certified_remote_diagonal import log_normalized
from suzuki_exact_integer_source_action import convolution,sqrt_upper
from suzuki_near_trial_lift_rhs import floor,writebuffer
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure,midpoint,radius
SOURCE='6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6'

def channels(y,zy,M,N,count,start,bits=256):
 # Input mode b+2j, output mode R+start+2i: n-m=2(i-j-N), N=R/2.
 S=1<<bits;offset=M-1+N
 h=[floor(F(1,2*(k-offset)),bits) if k!=offset else 0 for k in range(count+M-1)]
 g=[floor(F(1,2*(q+3*N+start)),bits) for q in range(count+M-1)]
 # h index for i-j is i-j+M-1; offset shifts the physical gap by -N.
 ty=convolution(y,h,M-1,count);tz=convolution(zy,h,M-1,count)
 hy=convolution(y[::-1],g,M-1,count);hz=convolution(zy[::-1],g,M-1,count)
 return [a+b for a,b in zip(tz,hz)],[a-b for a,b in zip(ty,hy)]

def run(source,sector,out,limit=None):
 raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE;whole=json.loads(raw);d=next(x for x in whole['cases'] if x['sector']==sector)
 start=1 if sector=='even-v' else 2;N=128000;b=512000+start;a=2*b+b%2;M=(a-b)//2;count=N
 if limit is not None:M=min(M,limit);count=min(count,limit)
 pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))));ci=enclosure(*times(constant(2),recip(pi)),256);c=midpoint(ci,256);ce=radius(ci,c)
 li=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi)),256);ti=enclosure(*times(recip(pi),recip(pi)),256);L=midpoint(li,256);t=midpoint(ti,256);assert 0<L<2 and 0<t<1;assert radius(li,L)<F(2,1<<256) and radius(ti,t)<F(2,1<<256)
 y=[];z=[];p=[];ey=F(0);ez=F(0)
 for j in range(M):
  m=b+2*j;zr=z_eval(m);zl,zh=F(zr['lower_rational']),F(zr['upper_rational']);zp=floor((zl+zh)/2,160);ze=max(abs(zl-F(zp,1<<160)),abs(zh-F(zp,1<<160)));assert ze<F('1e-39')
  w=sum(F(r['W_coefficient_rational'])/m**(2*r['j']+1) for r in d['far_channels']);v=sum(F(r['A_coefficient_rational'])/m**(2*r['j']+2) for r in d['far_channels']);shift=F(1,m*(m-1)) if start==2 else F(0)
  pl,ph=sorted((w-v*zl+shift,w-v*zh+shift));ll,lh=log_normalized(m,128);assert ll>11
  corners=[q/l for q in (pl,ph) for l in (ll,lh)];yl,yh=min(corners),max(corners);yp=floor((yl+yh)/2,160);ye=max(abs(yl-F(yp,1<<160)),abs(yh-F(yp,1<<160)));ey=max(ey,ye);ez=max(ez,ze)
  y.append(yp);z.append(zp);p.append(floor(L*m/(m*m+t),256))
  if (j+1)%16000==0:print(sector,'directed close seed rows',j+1,'/',M,flush=True)
 assert max(abs(q) for q in z)<8*(1<<160)
 l1=F(sum(abs(q) for q in y),1<<160);P=F(sum(q*v for q,v in zip(p,y)),1<<416);zy=[q*v for q,v in zip(z,y)]
 print(sector,'four exact close-action convolutions',flush=True);u,v=channels(y,zy,M,N,count,start)
 vals=[];checks=[];zout_err=F(0)
 for i in range(count):
  n=256000+start+2*i;zr=z_eval(n);zl,zh=F(zr['lower_rational']),F(zr['upper_rational']);zp=F(floor((zl+zh)/2,160),1<<160);zout_err=max(zout_err,abs(zl-zp),abs(zh-zp));pn=F(floor(L*n/(n*n+t),256),1<<256)
  point=c*(zp*F(v[i],1<<416)-F(u[i],1<<576))/2+(2 if start==1 else -2)*pn*P;vals.append(floor(point,256))
  if i in (0,count//2,count-1):
   du=dv=0
   for j in range(M):
    hk=floor(F(1,2*(i-j-N)),256);gk=floor(F(1,2*(i+j+3*N+start)),256);du+=(hk+gk)*zy[j];dv+=(hk-gk)*y[j]
   assert du==u[i] and dv==v[i];checks.append({'output_index':i,'all_close_input_terms_match':True})
  if (i+1)%16000==0:print(sector,'directed close output rows',i+1,'/',count,flush=True)
 assert zout_err<F('1e-39');eps=F(1,1<<256)
 # Offdiagonal exact kernel bound <=8/|n-m|<=4, since gaps are at least two.
 # Separate pole <=8; total propagation of y uncertainty <=12 M ey per row.
 seedrow=12*M*ey
 # Two reciprocal magnitudes <=1/2, |z|<8, |c|<1. Generous directed scalar cap.
 scalarrow=100*(ez+zout_err+ce+8*eps)*l1
 roundingrow=20*eps*l1+eps
 err=sqrt_upper(F(count),256)*(seedrow+scalarrow+roundingrow)
 assert err<F('1e-25')
 out.mkdir(parents=True,exist_ok=True);spec=writebuffer(out,sector,'region1-close-action',vals,256)
 return {'schema':'cone.infinite-seed-region1-close-action.v1','sector':sector,'source_sha256':SOURCE,'first_close_input_mode':b,'excluded_far_input_first_mode':a,'close_input_count':M,'output_first_mode':256000+start,'output_count':count,'full_rectangle_evaluated':limit is None,'point_buffer':spec,'rational':{'seed_point_maximum_error':str(ey),'input_z_maximum_error':str(ez),'output_z_maximum_error':str(zout_err),'represented_close_seed_l1':str(l1),'close_pole_moment_point':str(P),'seed_uncertainty_row_charge':str(seedrow),'physical_scalar_row_charge':str(scalarrow),'reciprocal_and_row_rounding_charge':str(roundingrow),'complete_close_action_l2_error_upper':str(err)},'complete_direct_row_checks':checks,'close_pole_included':True,'far_input_action_included':False,'whole_infinite_action_evaluated':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--sector',choices=('even-v','odd-v'),required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--limit',type=int);a=p.parse_args();d=run(a.source,a.sector,a.output_root,a.limit);(a.output_root/f'region1-close-action-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps({'sector':a.sector,'rows':d['output_count'],'error':float(F(d['rational']['complete_close_action_l2_error_upper']))}),flush=True)
