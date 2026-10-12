#!/usr/bin/env python3
"""Fresh finite lift for the actual infinite diagonal seed, with exact residual certification."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from suzuki_new_finite_lift import produce
from suzuki_exact_outward_certificate import read_snapshot,support_dot,subtract,operator_radius
from suzuki_exact_integer_source_action import ExactSource,norm2,dot,sqrt_upper
from suzuki_full_stationary_source_transport import PINS
from suzuki_trace_congruence_replay import inv,mul,tr
from suzuki_near_trial_lift_rhs import writebuffer

def load(root,rhsroot,sector):
 stem=f'joint-256000-{sector}.trace-256000.full';sp=root/(stem+'.zip');raw=(root/(stem+'.certificate.json')).read_bytes();assert hashlib.sha256(sp.read_bytes()).hexdigest()==PINS[sector][0] and hashlib.sha256(raw).hexdigest()==PINS[sector][1]
 meta,s,V,P=read_snapshot(sp);d=json.loads(raw);assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
 raw=(rhsroot/f'near-seed-refinement-{sector}.json').read_bytes();assert hashlib.sha256(raw).hexdigest()=={'even-v':'cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b','odd-v':'85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba'}[sector];cert=json.loads(raw);spec=cert['buffers']['lift-rhs'];buf=(rhsroot/spec['file']).read_bytes();assert len(buf)==spec['bytes'] and hashlib.sha256(buf).hexdigest()==spec['sha256']
 # Bind the actual full RHS by its immutable point hash; certificate must have the gate schema and bound.
 pins={'even-v':'b18bb86be4b94a1856e9f2016352a89b92aae7a9e729bdec2a6fa56772dcc37b','odd-v':'a0d9c1750bf677993e1b20cf27058c03dee8d4de228752d0a93c1a7015d4c133'}
 assert spec['sha256']==pins[sector] and cert['schema']=='cone.actual-residual-near-seed-refinement.v1' and F(cert['rational']['physical_lift_rhs_error_upper'])<F('4e-30')
 g={'bits':spec['bits'],'values':[int.from_bytes(buf[i:i+spec['width']],'little',signed=True) for i in range(0,len(buf),spec['width'])]};assert len(g['values'])==128000
 return meta,s,V,P,d,cert,g,hashlib.sha256(raw).hexdigest()
def certify(ctx,Z,sector,spec):
 meta,s,V,P,d,cert,g,rhssha=ctx
 print(sector,'exact complete physical finite lift certification',flush=True)
 res=subtract(ExactSource(s,meta['kernel_bits']).action(Z),g);gram=[[dot(a,b) for b in P] for a in P];Gi=inv(gram);proj=[[support_dot(p,res)] for p in P];q2=norm2(res)-mul(tr(proj),mul(Gi,proj))[0][0];assert q2>=0
 gn2=sum(dot(v,res)**2 for v in V[:6]);zn=sqrt_upper(norm2(Z),192);wn=sqrt_upper(F(d['graph_vector_norm2_rational']),192);da,_,_=operator_radius(s,meta['kernel_bits']);assert da==F(d['operator_radius_rational']);inp=da*zn+F(cert['rational']['physical_lift_rhs_error_upper']);qs=sqrt_upper(q2,192)+inp;ds=sqrt_upper(gn2,192)+wn*inp
 M=[[F(x) for x in r] for r in d['M_point_decimal']];J=[r[:6] for r in M[:6]];gamma=F('2.37e-13' if sector=='even-v' else '4.15e-12');rho=F(d['relative_trace_fro_upper_rational']);nu=rho/(1-rho);b={k:F(v) for k,v in d['bounds_rational'].items()};f=b['graph_residual_fro']/(1-rho);j=min(J[i][i]-sum(abs(J[i][k]) for k in range(6) if k!=i) for i in range(6));mn=max(sum(abs(v) for v in row) for row in M);alpha=b['assembly_J']+2*b['assembly_beta']+b['assembly_eta'];h=j-(b['assembly_J']+nu*(2+nu)*(mn+alpha)+f*f/gamma);assert h>0
 E=qs*qs/gamma+(ds/(1-rho)+f*qs/gamma)**2/h;grid=1<<192;E=F(-((-E.numerator*grid)//E.denominator),grid);charge=22*sqrt_upper(E,192);assert charge<F('2e-10')
 vals={'represented_lift_norm2':norm2(Z),'point_projected_residual_norm2':q2,'point_protected_dot_norm2':gn2,'physical_projected_residual_upper':qs,'physical_protected_dot_upper':ds,'operator_radius':da,'rhs_input_error_upper':F(cert['rational']['physical_lift_rhs_error_upper']),'combined_operator_and_rhs_input_error_upper':inp,'graph_floor':h,'inverse_energy_error_upper':E,'finite_lift_remote_action_charge_upper':charge}
 return {'schema':'cone.certified-refined-near-finite-lift.v1','sector':sector,'snapshot_sha256':PINS[sector][0],'primary_certificate_sha256':PINS[sector][1],'rhs_certificate_sha256':rhssha,'rhs_point_sha256':cert['buffers']['lift-rhs']['sha256'],'lift_buffer':spec,'rational':{k:str(v) for k,v in vals.items()},'display_approximate':{'energy_error':float(E),'finite_lift_remote_action_charge':float(charge),'lift_norm':float(zn)},'all_128000_physical_residual_coordinates_certified':True,'all_six_protected_components_retained':True,'physical_RHS_and_operator_errors_included_once':True,'finite_lift_certified':True,'finite_lift_action_charge_below_2e_minus10':charge<F('2e-10'),'whole_action_evaluated':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name in ('root','rhs-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--sector',choices=list(PINS),required=True);p.add_argument('--mode',choices=('produce','replay'),default='produce');a=p.parse_args();ctx=load(a.root,a.rhs_root,a.sector)
 a.output_root.mkdir(parents=True,exist_ok=True);certpath=a.output_root/f'refined-near-finite-lift-{a.sector}.json'
 if a.mode=='produce':
  Z=produce(ctx,a.sector);spec=writebuffer(a.output_root,a.sector,'refined-near-finite-lift',Z['values'],Z['bits'])
 else:
  previous=json.loads(certpath.read_text());spec=previous['lift_buffer'];raw=(a.output_root/spec['file']).read_bytes();assert len(raw)==spec['bytes'] and hashlib.sha256(raw).hexdigest()==spec['sha256'];Z={'bits':spec['bits'],'values':[int.from_bytes(raw[i:i+spec['width']],'little',signed=True) for i in range(0,len(raw),spec['width'])]};assert len(Z['values'])==128000
 d=certify(ctx,Z,a.sector,spec);serialized=json.dumps(d,indent=2,sort_keys=True)+'\n'
 if a.mode=='produce':certpath.write_text(serialized)
 else:assert certpath.read_text()==serialized,'independent exact replay disagrees'
 print(json.dumps(d['display_approximate']),flush=True)

