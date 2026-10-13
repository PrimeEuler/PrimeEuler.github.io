#!/usr/bin/env python3
"""Changed compact action on the gap before the patch far-series split."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from suzuki_exact_integer_source_action import convolution,sqrt_upper
from suzuki_bulk_action_z import evaluate
from suzuki_wider_correction_rhs import floor
N=128000;I=256000;M=264192;FIRST=I+M;COUNT=520191;S=1<<256
CAND={'even-v':'fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05','odd-v':'b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967'}
FAR={'even-v':'a5650821fd9fbe763017846994fb0e7637b56529576c0b4765b143f453506260','odd-v':'70d364a3b0e1240ab95acb1e10f9dd66163bf63e32a96159a206d6cd3bd8906b'}
PATCH={'even-v':'726c6bfeb55970fcb7f9fdcfcb1ce801b2e94e2e1e282c594f425049d085752e','odd-v':'bdad8088311e0ce66705b7500a4b886602de4cf8d8a575c0520412c6cb49f7bd'}
def sha(b):return hashlib.sha256(b).hexdigest()
def pinned(path,pin):
 raw=path.read_bytes();assert sha(raw)==pin;return json.loads(raw)
def rectangular_gap(x,zx,start,first=FIRST,count=COUNT,offset=I,bits=256):
 scale=1<<bits;last=first+count-1;m=len(x);assert first>=offset+m
 h=[0]+[scale//(2*k) for k in range(1,last-offset+1)]
 g=[scale//(2*(k+offset+start)) for k in range(last+m)]
 tx=convolution(x,h,first-offset,count);tz=convolution(zx,h,first-offset,count)
 hx=convolution(x[::-1],g,first+m-1,count);hz=convolution(zx[::-1],g,first+m-1,count)
 return [a+b for a,b in zip(tz,hz)],[a-b for a,b in zip(tx,hx)]
def checks():
 checked=0;bits=18;scale=1<<bits;c=F(2,3)
 for start in (1,2):
  for m in (3,6,9):
   offset=7;first=offset+m;count=m+3;x=[(-1)**j*(j+2) for j in range(m)];z=[j-4 for j in range(m)]
   u,v=rectangular_gap(x,[a*b for a,b in zip(x,z)],start,first,count,offset,bits)
   for r,i in enumerate(range(first,first+count)):
    n=2*i+start;zo=F(i+3,7);point=c*(zo*F(v[r],scale)-F(u[r],scale))/2
    direct=sum(c*(zo*(2*(offset+j)+start)-n*z[j])*x[j]/(n*n-(2*(offset+j)+start)**2) for j in range(m))
    assert abs(point-direct)<=F(60,scale)*sum(abs(a) for a in x);checked+=1
 return checked
def run(candidate,finite,finite_cert_sha,frontnear,patch,sector,out):
 start=1 if sector=='even-v' else 2
 fin=pinned(finite/f'wide-compact-near-middle-window-{sector}.json',finite_cert_sha);assert fin['candidate_sha256']==CAND[sector] and fin['compact_near_middle_window_output_rows_evaluated']
 sp=fin['patch_input_z_buffer'];raw=(finite/sp['file']).read_bytes();assert sha(raw)==sp['sha256'] and len(raw)==sp['bytes']==M*sp['width'] and sp['count']==M and sp['bits']==160
 z=[int.from_bytes(raw[j:j+sp['width']],'little',signed=True) for j in range(0,len(raw),sp['width'])]
 raw=(candidate/f'{sector}-wider-correction.bin').read_bytes();assert sha(raw)==CAND[sector] and len(raw)==18*M
 x=[int.from_bytes(raw[j:j+18],'little',signed=True) for j in range(0,len(raw),18)];zx=[a*b for a,b in zip(x,z)]
 f=pinned(frontnear/f'wider-front-near-far-{sector}.json',FAR[sector]);p=pinned(patch/f'far-patch-moments-{sector}.json',PATCH[sector]);assert p['candidate_sha256']==CAND[sector]
 assert f['sector']==p['sector']==sector and not f['finite_wider_patch_action_included'] and not f['infinite_seed_tail_action_included'] and f['actual_CI_lift_certificate_sha256']==fin['actual_CI_lift_certificate_sha256']
 firstmode=2*FIRST+start;lastmode=2*(FIRST+COUNT-1)+start;assert firstmode==fin['last_output_mode']+2 and lastmode==p['far_first_mode']-2
 fc=f['point_parameters'];pc=p['point_parameters'];c=F(fc['c']);L=F(fc['L']);t=F(fc['t']);alpha=fc['alpha'];P=F(pc['pole_moment']);assert all(fc[k]==pc[k] for k in ('c','L','t','alpha'))
 assert abs(c)<1 and max(abs(v) for v in z)<8*(1<<160)
 print(sector,'gap four exact patch convolutions begin',flush=True);u,v=rectangular_gap(x,zx,start);print(sector,'gap convolutions complete',flush=True)
 a=f['far_first_mode'];gam=[F(m['M_odd_rational'])/a**(2*j+2) for j,m in enumerate(f['moments'])];bet=[F(m['Z_even_rational'])/a**(2*j+1) for j,m in enumerate(f['moments'])]
 gs=[floor(q) for q in gam];bs=[floor(q) for q in bet];cc=floor(c);PF=F(fc['pole_moment']);C=1+sum(abs(q) for q in gam+bet)+abs(alpha*L*PF)+abs(c)+abs(PF)
 roundrow=F(100000,S)*C;values=[];direct=[]
 for r,i in enumerate(range(FIRST,FIRST+COUNT)):
  n=2*i+start;zr=evaluate(n);lo,hi=F(zr['lower_rational']),F(zr['upper_rational']);zo=F(floor((lo+hi)/2,160),1<<160);assert max(abs(lo-zo),abs(hi-zo))<F('1e-39') and abs(zo)<8
  delta=c*(zo*F(v[r],1<<416)-F(u[r],1<<576))/2+alpha*F(floor(L*n/(n*n+t)),S)*P
  ratio=a*S//n;tt=ratio*ratio//S;hg=hb=0
  for g,b in zip(reversed(gs),reversed(bs)):hg=g+tt*hg//S;hb=b+tt*hb//S
  frontpoint=F(cc*(floor(zo)*(tt*hg//S)//S-ratio*hb//S)//S,S)+alpha*F(floor(L*n/(n*n+t)),S)*PF
  if r in (0,COUNT//2,COUNT-1):
   du=sum((S//(2*(i-I-j))+S//(2*(i+I+j+start)))*zx[j] for j in range(M));dv=sum((S//(2*(i-I-j))-S//(2*(i+I+j+start)))*x[j] for j in range(M));assert du==u[r] and dv==v[r]
   exact=c*zo*sum(q*F(a,n)**(2*j+2) for j,q in enumerate(gam))-c*sum(q*F(a,n)**(2*j+1) for j,q in enumerate(bet))+alpha*L*n/(n*n+t)*PF
   assert abs(frontpoint-exact)<=roundrow;direct.append({'n':n,'all_264192_patch_inputs_match':True,'front_near_exact_retained_series_inside_rounding_bound':True})
  values.append(floor(delta+frontpoint))
  if (r+1)%16000==0:print(sector,'compact gap rows',r+1,'/',COUNT,flush=True)
 l1=F(sum(abs(q) for q in x),1<<160);eps=F(1,S);patchrow=(F('21e-38')+19*eps)*l1+2*F('1e-38')*abs(P)+16*eps*l1+eps;patcherror=sqrt_upper(F(COUNT),256)*patchrow
 fe=F(f['rational']['geometric_action_remainder_upper'])+F(f['physical_compact_far_parameter_charge_upper']);error=patcherror+fe+sqrt_upper(F(COUNT),256)*(roundrow+eps);assert error<F('3e-11')
 out.mkdir(parents=True,exist_ok=True);width=(max(abs(q).bit_length() for q in values)+8)//8;raw=b''.join(q.to_bytes(width,'little',signed=True) for q in values);name=f'{sector}-wider-compact-gap-action.bin';(out/name).write_bytes(raw)
 return {'schema':'cone.wider-compact-gap-action.v1','sector':sector,'candidate_sha256':CAND[sector],'finite_compact_certificate_sha256':finite_cert_sha,'patch_input_z_sha256':sp['sha256'],'front_near_far_certificate_sha256':FAR[sector],'far_patch_certificate_sha256':PATCH[sector],'new_lift_certificate_sha256':f['actual_CI_lift_certificate_sha256'],'first_output_mode':firstmode,'last_output_mode':lastmode,'complete_output_rows':COUNT,'buffer':{'file':name,'bits':256,'width':width,'bytes':len(raw),'count':COUNT,'sha256':sha(raw)},'rational':{'patch_direct_physical_error_upper':str(patcherror),'front_near_moment_physical_error_upper':str(fe),'normalized_Horner_per_row_error_upper':str(roundrow),'complete_compact_gap_error_upper':str(error)},'display_approximate':{'complete_compact_gap_error_upper':float(error)},'complete_direct_gap_checks':direct,'independent_exact_physical_kernel_rows':checks(),'diagonal_absent_beyond_support':True,'original_infinite_seed_action_included':False,'whole_residual_acceptance_certified':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--self-check',action='store_true')
 for name in ('candidate-root','finite-root','front-near-root','patch-root','output-root'):p.add_argument('--'+name,type=Path)
 p.add_argument('--finite-certificate-sha256');p.add_argument('--sector',choices=tuple(CAND));a=p.parse_args()
 if a.self_check:print({'exact_physical_gap_kernel_rows_verified':checks()})
 else:
  d=run(a.candidate_root,a.finite_root,a.finite_certificate_sha256,a.front_near_root,a.patch_root,a.sector,a.output_root);(a.output_root/f'wider-compact-gap-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d['display_approximate']),flush=True)
