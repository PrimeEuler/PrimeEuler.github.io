#!/usr/bin/env python3
"""Actual finite-front RHS update for a supplied wider correction; does not construct it."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from suzuki_exact_integer_source_action import convolution,sqrt_upper
from suzuki_bulk_action_z import evaluate
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure,midpoint,radius
N=128000;I=2*N;M=264192;S=1<<256
ZIP={'even-v':'da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5','odd-v':'6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453'}
OLD={'even-v':'cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b','odd-v':'85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba'}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def floor(q,b=256):return q.numerator*(1<<b)//q.denominator

def rectangular_transpose(y,zy,start,n=N,offset=I,bits=256):
 m=len(y);scale=1<<bits
 h=[0]+[scale//(2*q) for q in range(1,offset+m)]
 g=[scale//(2*(q+start)) for q in range(offset+m+n-1)]
 ty=convolution(y[::-1],h,offset+m-n,n)[::-1];tz=convolution(zy[::-1],h,offset+m-n,n)[::-1]
 hy=convolution(y[::-1],g,offset+m-1,n);hz=convolution(zy[::-1],g,offset+m-1,n)
 return [a-b for a,b in zip(tz,hz)],[a+b for a,b in zip(ty,hy)]

def self_check():
 checked=0;bits=40;scale=1<<bits;c=F(2,3)
 for start in (1,2):
  for n in (2,3,7):
   for m in (3,7,11):
    offset=2*n;y=[(-1)**j*(j+2) for j in range(m)];z=[(-1)**j*(j%5+1) for j in range(m)];u,v=rectangular_transpose(y,[a*b for a,b in zip(y,z)],start,n,offset,bits)
    for i in range(n):
     nf=2*i+start;zf=(-1)**i*(i%7+1)
     direct=c*sum(F((zf*(2*(offset+j)+start)-nf*z[j])*y[j],nf*nf-(2*(offset+j)+start)**2) for j in range(m))
     point=c*F(u[i]-zf*v[i],2*scale)
     assert abs(point-direct)<=F(20,scale)*sum(abs(a) for a in y);checked+=1
 return checked

def readbuf(root,spec):
 raw=(root/spec['file']).read_bytes();assert len(raw)==spec['bytes'] and sha(raw)==spec['sha256'];return [int.from_bytes(raw[j:j+spec['width']],'little',signed=True) for j in range(0,len(raw),spec['width'])]
def write(root,sector,label,values,bits):
 width=(max(abs(v).bit_length() for v in values)+8)//8;raw=b''.join(v.to_bytes(width,'little',signed=True) for v in values);name=f'{sector}-{label}.bin';(root/name).write_bytes(raw)
 return {'file':name,'bits':bits,'width':width,'count':len(values),'bytes':len(raw),'sha256':sha(raw)}
def run(snapshot,oldroot,candidate,width,candidate_sha,sector,out):
 # Candidate bytes and SHA must be supplied from the actual returned handoff, never guessed.
 raw=candidate.read_bytes();assert sha(raw)==candidate_sha and len(raw)==M*width
 delta=[int.from_bytes(raw[j:j+width],'little',signed=True) for j in range(0,len(raw),width)];assert len(delta)==M
 oldraw=(oldroot/f'near-seed-refinement-{sector}.json').read_bytes();assert sha(oldraw)==OLD[sector];old=json.loads(oldraw);spec=old['buffers']['lift-rhs'];assert spec['bits']==256;oldg=readbuf(oldroot,spec);assert len(oldg)==N
 assert sha(snapshot.read_bytes())==ZIP[sector]
 from suzuki_exact_outward_certificate import read_snapshot
 _,s,_,_=read_snapshot(snapshot);start=1 if sector=='even-v' else 2;assert s['modes'][0]==start and len(s['modes'])==N
 b=512000+start;end=b+2*(M-1);assert end==(1040383 if start==1 else 1040384)
 dn=sqrt_upper(F(sum(v*v for v in delta),1<<320),256);trial=F(old['rational']['new_whole_trial_norm_upper'])+dn;assert trial<F('0.002')
 pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))));li=enclosure(*times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi)),256);ti=enclosure(*times(recip(pi),recip(pi)),256);L=midpoint(li,256);t=midpoint(ti,256);assert 0<L<2 and 0<t<1 and radius(li,L)<F(2,S) and radius(ti,t)<F(2,S)
 z=[];pole=[];maxze=F(0)
 for j in range(M):
  n=b+2*j;r=evaluate(n);lo,hi=F(r['lower_rational']),F(r['upper_rational']);zp=floor((lo+hi)/2,160);maxze=max(maxze,abs(lo-F(zp,1<<160)),abs(hi-F(zp,1<<160)));z.append(zp);pole.append(floor(L*n/(n*n+t)))
  if (j+1)%16000==0:print(sector,'wider correction physical-z rows',j+1,'/',M,flush=True)
 assert maxze<F('1e-39') and max(abs(v) for v in z)<8*(1<<160)
 zy=[a*b for a,b in zip(z,delta)];u,v=rectangular_transpose(delta,zy,start);P=F(sum(a*b for a,b in zip(pole,delta)),1<<416);c=F(s['c']['values'][0],1<<s['c']['bits']);updated=[];checks=[]
 for i in range(N):
  zf=F(s['z']['values'][i],1<<s['z']['bits']);pf=F(s['pole']['values'][i],1<<s['pole']['bits']);q=c*(F(u[i],1<<576)-zf*F(v[i],1<<416))/2+s['alpha']*pf*P;updated.append(oldg[i]+floor(q))
  if i in (0,N//2,N-1):
   du=sum((S//(2*(I+j-i))-S//(2*(I+j+i+start)))*zy[j] for j in range(M));dv=sum((S//(2*(I+j-i))+S//(2*(I+j+i+start)))*delta[j] for j in range(M));assert du==u[i] and dv==v[i];checks.append({'front_index':i,'all_264192_correction_inputs_match':True})
 l1=F(sum(abs(v) for v in delta),1<<160);eps=F(1,S);row=(F('21e-38')+19*eps)*l1+2*F('1e-38')*abs(P)+16*eps*l1+eps;error=sqrt_upper(F(N),256)*row+F(old['rational']['physical_lift_rhs_error_upper']);assert error<F('4e-30')
 out.mkdir(parents=True,exist_ok=True);buf=write(out,sector,'wider-correction-lift-rhs',updated,256)
 return {'schema':'cone.supplied-wider-correction-finite-rhs.v1','sector':sector,'snapshot_sha256':ZIP[sector],'old_trial_RHS_certificate_sha256':OLD[sector],'candidate_point_sha256':candidate_sha,'candidate_bits':160,'candidate_count':M,'candidate_first_mode':b,'candidate_last_mode':end,'buffers':{'lift-rhs':buf},'rational':{'represented_wider_correction_norm_upper':str(dn),'new_whole_trial_norm_upper':str(trial),'physical_lift_rhs_error_upper':str(error),'maximum_correction_input_z_error':str(maxze)},'complete_direct_front_checks':checks,'small_exact_physical_kernel_checks':self_check(),'display_approximate':{'correction_norm':float(dn),'trial_norm_upper':float(trial),'RHS_error':float(error)},'all_128000_new_RHS_rows_evaluated':True,'finite_correction_preserves_domain':True,'new_finite_lift_certified':False,'new_residual_evaluated':False,'whole_residual_acceptance_certified':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--self-check',action='store_true');p.add_argument('--snapshot',type=Path);p.add_argument('--old-root',type=Path);p.add_argument('--candidate',type=Path);p.add_argument('--candidate-width',type=int);p.add_argument('--candidate-sha256');p.add_argument('--sector',choices=('even-v','odd-v'));p.add_argument('--output-root',type=Path);a=p.parse_args()
 if a.self_check:print(json.dumps({'exact_physical_kernel_rows_verified':self_check()}))
 else:
  assert all(v is not None for v in (a.snapshot,a.old_root,a.candidate,a.candidate_width,a.candidate_sha256,a.sector,a.output_root));d=run(a.snapshot,a.old_root,a.candidate,a.candidate_width,a.candidate_sha256,a.sector,a.output_root);(a.output_root/f'wider-correction-RHS-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d['display_approximate']),flush=True)
