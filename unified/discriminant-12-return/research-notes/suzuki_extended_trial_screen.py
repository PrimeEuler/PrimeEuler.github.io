#!/usr/bin/env python3
"""Exploratory finite extension screen. Floating choices are NOT certificates."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.fft import rfft,irfft,next_fast_len
from scipy.sparse.linalg import LinearOperator,cg
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_full_stationary_source_transport import combine,PINS
from suzuki_trace_congruence_replay import inv,mul
from suzuki_combined_far_action import buffer
from suzuki_new_finite_lift import to_float

def conv(x,k):
 L=next_fast_len(len(x)+len(k)-1)
 return irfft(rfft(x,L)*rfft(k,L),L)[:len(x)+len(k)-1]
def run(root,rhsroot,sourceroot,sector,multiple):
 sp=root/f'joint-256000-{sector}.trace-256000.full.zip';assert hashlib.sha256(sp.read_bytes()).hexdigest()==PINS[sector][0]
 meta,s,V,P=read_snapshot(sp);N=len(s['modes']);start=s['modes'][0]
 primary=json.loads((root/f'joint-256000-{sector}.trace-256000.full.certificate.json').read_text())
 src=json.loads((sourceroot/f'full-stationary-source-{sector}.json').read_text());Zfamily=combine(V,[F(a) for a in src['q_rational']]);Z=to_float(Zfamily)
 whole=json.loads((sourceroot/'whole-source-affine.json').read_text());far=next(x for x in whole['cases'] if x['sector']==sector)
 rc=json.loads((rhsroot/f'new-near-trial-rhs-{sector}.json').read_text());oldy=to_float(buffer(rhsroot,rc['buffers']['trial-near']))
 K=(multiple-1)*N;n=2*(N+np.arange(K))+start
 weights=[np.log(2)/np.sqrt(2),np.log(3)/np.sqrt(3),np.log(2)/2,np.log(5)/np.sqrt(5),np.log(7)/np.sqrt(7)]
 zr=np.pi/2+1/(n*np.pi)-(-1.)**start*4*np.exp(-1)/(1-np.exp(-4))/(n*np.pi)
 for q,w in zip((2,3,4,5,7),weights):zr+=2*w*np.sin(n*np.pi*np.log(q)/2)
 aa=np.zeros(K-N);ww=np.zeros(K-N);nf=n[N:]
 for row in far['far_channels']:
  j=row['j'];ww+=float(F(row['W_coefficient_rational']))/nf.astype(float)**(2*j+1)
  aa+=float(F(row['A_coefficient_rational']))/nf.astype(float)**(2*j+2)
 rho=ww-zr[N:]*aa
 if sector=='odd-v':rho+=1/(nf.astype(float)*(nf-1))
 y=np.concatenate((oldy,rho/np.log(nf/4)))
 z=to_float(s['z']);diag=to_float(s['diag']);pole=to_float(s['pole']);c=float(F(s['c']['values'][0],1<<s['c']['bits']));alpha=s['alpha']
 lp=4*(np.cosh(.5) if start==1 else np.sinh(.5))/np.pi;pr=lp*n/(n*n+np.pi**-2)
 h=np.zeros(N+K);h[1:]=1/(2*np.arange(1,N+K));g=1/(2*(np.arange(K+2*N-1)+start))
 hy=conv(y[::-1],h)[K:K+N][::-1];gy=conv(y[::-1],g)[N+K-1:N+K-1+N]
 hzy=conv((zr*y)[::-1],h)[K:K+N][::-1];gzy=conv((zr*y)[::-1],g)[N+K-1:N+K-1+N]
 rhs=c/2*(hzy-gzy-z*(hy+gy))+alpha*pole*(pr@y)
 from suzuki_new_finite_lift import produce,from_float
 # Floating RHS only chooses a probe; protected refinements use exact integer actions.
 chosen=produce((meta,s,V,P,primary,rc,from_float(rhs),'diagnostic-only'),sector)
 lift=to_float(chosen);history=['exact-action-protected-refinement','exact-action-protected-refinement']
 x=np.concatenate((Z-lift,y));zz=np.concatenate((z,zr));mm=np.concatenate((np.array(s['modes']),n));U=multiple*256000;a=2*U+start
 Pmom=pole@(Z-lift)+pr@y;LP=alpha*lp*Pmom
 from suzuki_new_finite_lift import family_add
 xf=family_add(Zfamily,{'bits':chosen['bits'],'values':[-v for v in chosen['values']]})
 yf=from_float(y);zf=from_float(zr);pf=from_float(pr)
 def dotfamily(a,b):return F(sum(v*w for v,w in zip(a['values'],b['values'])),1<<(a['bits']+b['bits']))
 exactZ0=dotfamily(s['z'],xf)+dotfamily(zf,yf)
 exactP=dotfamily(s['pole'],xf)+dotfamily(pf,yf)
 farpoint=json.loads((sourceroot/f'combined-far-action-{sector}.json').read_text())['point_parameters']
 exactC0=F(1)+F(s['c']['values'][0],1<<s['c']['bits'])*exactZ0-F(alpha)*F(farpoint['L'])*exactP
 C=[];D=[]
 for j in range(42):
  w=(mm/a)**(2*j);cj=c*np.dot(zz*x,w)-LP*(-np.pi**-2/a**2)**j;dj=-c*np.dot(x,(mm/a)*w)
  if j==0:cj=float(exactC0)
  C.append(cj);D.append(dj)
 # Normalized channels: Cj/a*(a/n)^(2j+1), Dj/a*(a/n)^(2j+2).
 def normpower(p):return np.sqrt(1/a**2+1/(2*(p-1)*a))
 cup=sum(abs(q)*normpower(4*j+2) for j,q in enumerate(C));d8=8*sum(abs(q)*normpower(4*j+4) for j,q in enumerate(D))
 lower=abs(C[0])/np.sqrt(2*a)-sum(abs(q)*normpower(4*j+2) for j,q in enumerate(C) if j>0)-d8
 return {'schema':'cone.floating-extended-trial-screen.v1','sector':sector,'support_multiple_R':multiple,'remote_count':K,'front_count':N,'Far_first_mode':a,'trial_norm_float':float(np.linalg.norm(y)),'lift_norm_float':float(np.linalg.norm(lift)),'leading_C_float':C[0],'leading_C_exact_rational_for_represented_probe':str(exactC0),'Far_triangle_lower_diagnostic':lower,'Far_triangle_upper_diagnostic':cup+d8,'CG_iterations':history,'certified':False,'physical_errors_included':False,'stationary_acceptance_met':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for q in ('root','rhs-root','source-root','output'):p.add_argument('--'+q,type=Path,required=True)
 p.add_argument('--sector',choices=list(PINS),required=True);p.add_argument('--multiple',type=int,default=4);a=p.parse_args()
 d=run(a.root,a.rhs_root,a.source_root,a.sector,a.multiple);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d),flush=True)
