"""New finite lifts; certification uses complete frozen exact residual replay."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import argparse
from suzuki_exact_outward_certificate import read_snapshot,subtract,support_dot,operator_radius
from suzuki_exact_integer_source_action import ExactSource,norm2,dot,sqrt_upper
from suzuki_full_stationary_source_transport import combine,rounded,PINS
from suzuki_trace_congruence_replay import inv,mul,tr

def family_add(x,t):
 b=max(x['bits'],t['bits']);return {'bits':b,'values':[(a<<(b-x['bits']))+(c<<(b-t['bits'])) for a,c in zip(x['values'],t['values'])]}
def to_float(x):
 import numpy as np
 return np.array([float(F(a,1<<x['bits'])) for a in x['values']])
def from_float(x):
 return {'bits':256,'values':[int(F(*float(a).as_integer_ratio())*(1<<256)) for a in x]}
def point_project(source,P,Gi):
 coef=mul(Gi,[[support_dot(p,source)] for p in P]);b=source['bits']
 q={'bits':256,'values':[int(F(a,1<<b)*(1<<256)) for a in source['values']]}
 # Exact projection is only rounded AFTER combining all six corrections.
 stop=max(len(p['values']) for p in P)
 for i in range(stop):
  value=F(source['values'][i],1<<b)-sum((F(p['values'][i],1<<p['bits'])*coef[j][0] if i<len(p['values']) else F(0)) for j,p in enumerate(P))
  q['values'][i]=value.numerator*(1<<256)//value.denominator
 return q


def load_context(root,rhsroot,sector):
 stem=f'joint-256000-{sector}.trace-256000.full'
 sr=(root/(stem+'.zip')).read_bytes();pr=(root/(stem+'.certificate.json')).read_bytes()
 assert hashlib.sha256(sr).hexdigest()==PINS[sector][0] and hashlib.sha256(pr).hexdigest()==PINS[sector][1]
 meta,s,V,P=read_snapshot(root/(stem+'.zip'));d=json.loads(pr)
 assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
 cr=(rhsroot/f'new-near-trial-rhs-{sector}.json').read_bytes();pins={'even-v':'7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45','odd-v':'3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480'}
 assert hashlib.sha256(cr).hexdigest()==pins[sector];cert=json.loads(cr);spec=cert['buffers']['lift-rhs'];raw=(rhsroot/spec['file']).read_bytes()
 assert len(raw)==spec['bytes'] and hashlib.sha256(raw).hexdigest()==spec['sha256']
 g={'bits':spec['bits'],'values':[int.from_bytes(raw[j:j+spec['width']],'little',signed=True) for j in range(0,len(raw),spec['width'])]}
 assert len(g['values'])==128000
 return meta,s,V,P,d,cert,g,hashlib.sha256(cr).hexdigest()

def produce(ctx,sector):
 import numpy as np
 from scipy.fft import next_fast_len,rfft,irfft
 from scipy.sparse.linalg import LinearOperator,cg
 meta,s,V,P,d,cert,g,_=ctx;N=len(s['modes'])
 M=[[F(x) for x in row] for row in d['M_point_decimal']];J=[row[:6] for row in M[:6]];Ji=inv(J)
 gram=[[dot(a,b) for b in P] for a in P];Gi=inv(gram)
 p=np.zeros((N,6))
 for j,col in enumerate(P):p[:len(col['values']),j]=to_float(col)
 gif=np.array([[float(x) for x in row] for row in Gi])
 def proj(x):return x-p@(gif@(p.T@x))
 z=to_float(s['z']);diag=to_float(s['diag']);pole=to_float(s['pole']);c=float(F(s['c']['values'][0],1<<s['c']['bits']));n=np.array(s['modes']);L=next_fast_len(3*N-2)
 shifts=np.arange(-N+1,N);kt=np.zeros(2*N-1);kt[shifts!=0]=1/(2*shifts[shifts!=0]);kh=1/(2*(np.arange(2*N-1)+n[0]));tf=rfft(kt,L);hf=rfft(kh,L)
 def con(x,k):return irfft(rfft(x,L)*k,L)[N-1:2*N-1]
 def rawmv(x):return c/2*(z*(con(x,tf)-con(x[::-1],hf))-con(z*x,tf)-con((z*x)[::-1],hf))+c*z*x/(2*n)+diag*x+s['alpha']*pole*(pole@x)
 def mv(x):return proj(rawmv(proj(x)))+p@(gif@(p.T@x))
 op=LinearOperator((N,N),matvec=mv,dtype=float);engine=ExactSource(s,meta['kernel_bits'])
 q=[rounded(x[0]) for x in mul(Ji,[[dot(v,g)] for v in V[:6]])]
 vectors=V[:6]+[{'bits':0,'values':[0]*N}];Z=combine(vectors,q)
 for step in range(2):
  print(sector,'exact action before new complement refinement',step,flush=True)
  res=subtract(engine.action(Z),g);qres=point_project(res,P,Gi);rhs=-to_float(qres);iters=[0]
  delta,info=cg(op,rhs,rtol=2e-14,atol=0,maxiter=40000,callback=lambda _:iters.__setitem__(0,iters[0]+1));assert info==0,(sector,info)
  Z=family_add(Z,from_float(proj(delta)))
  r2=subtract(engine.action(Z),g);coeff=[rounded(-x[0]) for x in mul(Ji,[[dot(v,r2)] for v in V[:6]])]
  Z=family_add(Z,combine(vectors,coeff));print(sector,'complement CG iterations',iters[0],flush=True)
 return Z

def certify(ctx,Z,sector,packed,spec):
 meta,s,V,P,d,cert,g,rhssha=ctx
 print(sector,'certify complete physical lift residual by exact action',flush=True)
 res=subtract(ExactSource(s,meta['kernel_bits']).action(Z),g)
 gram=[[dot(a,b) for b in P] for a in P];Gi=inv(gram)
 projected=[[support_dot(p,res)] for p in P]
 q2=norm2(res)-mul(tr(projected),mul(Gi,projected))[0][0];assert q2>=0
 graph=[dot(v,res) for v in V[:6]];gn2=sum(x*x for x in graph)
 zn=sqrt_upper(norm2(Z),192);wn=sqrt_upper(F(d['graph_vector_norm2_rational']),192)
 da,_,_=operator_radius(s,meta['kernel_bits']);assert da==F(d['operator_radius_rational'])
 input_error=da*zn+F(cert['rational']['physical_lift_rhs_error_upper'])
 qs=sqrt_upper(q2,192)+input_error;ds=sqrt_upper(gn2,192)+wn*input_error
 M=[[F(x) for x in row] for row in d['M_point_decimal']];J=[row[:6] for row in M[:6]]
 gamma=F('2.37e-13' if sector=='even-v' else '4.15e-12');rho=F(d['relative_trace_fro_upper_rational']);nu=rho/(1-rho)
 b={k:F(v) for k,v in d['bounds_rational'].items()};f=b['graph_residual_fro']/(1-rho)
 j=min(J[i][i]-sum(abs(J[i][k]) for k in range(6) if k!=i) for i in range(6));mn=max(sum(abs(v) for v in row) for row in M)
 alpha=b['assembly_J']+2*b['assembly_beta']+b['assembly_eta'];a=b['assembly_J']+nu*(2+nu)*(mn+alpha)+f*f/gamma;h=j-a;assert h>0
 E=qs*qs/gamma+(ds/(1-rho)+f*qs/gamma)**2/h
 # Round the serialized energy upward; no display is used as a decision bound.
 grid=1<<192;E=F(-((-E.numerator*grid)//E.denominator),grid)
 lift=22*sqrt_upper(E,192);yn=F(cert['rational']['trial_norm_upper'])
 model=F('3.454e-8' if sector=='even-v' else '1.334e-10')*yn
 conditional=lift+model+F('3e-11')+F('5e-26')
 assert lift<F('5e-11' if sector=='even-v' else '2e-14') and conditional<F('2e-10')
 assert hashlib.sha256(packed).hexdigest()==spec['sha256']
 values={'represented_lift_norm2':norm2(Z),'point_projected_residual_norm2':q2,
  'point_protected_dot_norm2':gn2,'physical_projected_residual_upper':qs,
  'physical_protected_dot_upper':ds,'operator_radius':da,'rhs_input_error_upper':F(cert['rational']['physical_lift_rhs_error_upper']),
  'combined_operator_and_rhs_input_error_upper':input_error,'graph_floor':h,
  'inverse_energy_error_upper':E,'finite_lift_remote_action_charge_upper':lift,
  'trial_norm_upper':yn,'conditional_model_action_charge_upper':model,'conditional_total_action_upper':conditional}
 return {'schema':'cone.certified-new-near-trial-finite-lift.v1','sector':sector,
  'snapshot_sha256':PINS[sector][0],'primary_certificate_sha256':PINS[sector][1],
  'new_trial_rhs_certificate_sha256':rhssha,'new_trial_rhs_point_sha256':cert['buffers']['lift-rhs']['sha256'],
  'lift_buffer':spec,'rational':{k:str(v) for k,v in values.items()},
  'display_approximate':{'energy_error':float(E),'finite_lift_remote_action_charge':float(lift),'conditional_total_action':float(conditional)},
  'all_128000_full_physical_residual_coordinates_certified':True,
  'physical_rhs_error_included_once_in_residual':True,'physical_operator_error_included':True,
  'projected_and_all_six_protected_components_retained':True,'finite_lift_solve_certified':True,
  'old_sufficient_qs_ds_targets_met':qs<F('4e-19' if sector=='even-v' else '1e-18') and ds<F('8e-13'),
  'conditional_total_action_below_unchanged_2e_minus10':True,
  'remaining_total_output_arithmetic_reserved_rational':'3/100000000000',
  'remaining_output_arithmetic_achieved':False,'whole_remote_action_evaluated':False,
  'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}

def main():
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['produce','replay'],required=True)
 for name in ('root','rhs-root','witness-root','output'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=list(PINS),required=True);args=p.parse_args()
 ctx=load_context(args.root,args.rhs_root,args.sector)
 name=f'new-finite-lift-{args.sector}.bin'
 if args.mode=='produce':
  Z=produce(ctx,args.sector);width=(max(abs(v).bit_length() for v in Z['values'])+8)//8
  packed=b''.join(v.to_bytes(width,'little',signed=True) for v in Z['values'])
  args.witness_root.mkdir(parents=True,exist_ok=True);(args.witness_root/name).write_bytes(packed)
  spec={'file':name,'bits':Z['bits'],'width':width,'count':len(Z['values']),'bytes':len(packed),'sha256':hashlib.sha256(packed).hexdigest()}
 else:
  old=json.loads((args.witness_root/f'new-finite-lift-{args.sector}.json').read_text());spec=old['lift_buffer'];assert spec['file']==name
  packed=(args.witness_root/name).read_bytes();assert len(packed)==spec['bytes'] and hashlib.sha256(packed).hexdigest()==spec['sha256']
  assert spec['count']==128000 and spec['bytes']==spec['count']*spec['width']
  Z={'bits':spec['bits'],'values':[int.from_bytes(packed[j:j+spec['width']],'little',signed=True) for j in range(0,len(packed),spec['width'])]}
 result=certify(ctx,Z,args.sector,packed,spec)
 args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result['display_approximate']),flush=True)
if __name__=='__main__':main()
