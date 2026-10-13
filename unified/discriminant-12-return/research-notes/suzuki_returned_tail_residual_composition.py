#!/usr/bin/env python3
"""Compose returned tail rows with refined compact action; no beyond-window closure."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,json,hashlib,base64
from suzuki_bulk_action_z import evaluate as z_eval
PINS={"refined-near-compact-middle-even-v.json":"a13faa4276600c7dae5f39d62b36435a293d4c0d","refined-near-compact-middle-odd-v.json":"9e2ea1df382648d69622bffa065b14823b119823","remaining-residual-budget.json":"a25c510f64c44d6c138920b05db057ed24c52272","refined-compact-far-even-v.json":"9f84dff5f130329be813ad28d1d76188f38734f9","refined-compact-far-odd-v.json":"20112f2574ff6cb17bd5aec7adc97f0bca1c859a","envelope-even-v.json":"e862f5c96d7e27b5c99317cf0b2a6023cdfe7370","envelope-odd-v.json":"20e373d29facc07ca1e5bba7a5ca3149ed04e393","manifest.json":"72c80b7f4665a4dc7e3311ea8454aa34bb26a353","region2-action-even-v.json":"e6619adfe5ecac374560dd726885e653be749755","region2-action-odd-v.json":"29c4be6ae8347b89fcb2f5ff65d966f5464afcd8","region3-action-even-v.json":"222e59e066829440ace423bfd180f5157126c890","region3-action-odd-v.json":"c055f2d36f306d5a54e251c8af40480a8e6094d6","refined-region1-residual-even-v.json":"40240d75d0835da3a8daa7fc0adacc23d1d45fe2","refined-region1-residual-odd-v.json":"efd1ef405bf5c3562f39406fde185550f01e9b9f"}
BITS=256;S=1<<BITS
def upper(q):
 assert q>=0
 n=q.numerator*S*S;d=q.denominator;k=isqrt(n//d)
 if k*k*d<n:k+=1
 return F(k,S)
def floor(q):return q.numerator*S//q.denominator
def read(root,name):
 raw=(root/name).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==PINS[name]
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def ints(raw,count):
 assert len(raw)==30*count
 return [int.from_bytes(raw[i:i+30],'little',signed=True) for i in range(0,len(raw),30)]
def pointbuf(root,spec):
 raw=(root/spec['file']).read_bytes();assert len(raw)==spec['bytes'] and hashlib.sha256(raw).hexdigest()==spec['sha256'];assert spec['bits']==256 and spec['width']==30
 return ints(raw,spec['count'])
def write(root,sector,label,v):
 width=max(1,(max(abs(x).bit_length() for x in v)+8)//8);raw=b''.join(x.to_bytes(width,'little',signed=True) for x in v);name=f'{sector}-{label}.bin';(root/name).write_bytes(raw)
 return {'file':name,'bits':256,'width':width,'count':len(v),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def norm(v):
 q=F(sum(x*x for x in v),S*S);h=upper(q);l=max(F(0),h-F(1,S));assert l*l<=q<=h*h
 return l,h
def run(payloads,sector,out):
 tailroot=payloads/'sandbox_tail_regions23_v14_327';mroot=payloads/'refined_compact_middle_v14_309';froot=payloads/'refined_trial_region1_and_far_v14_306'
 manifest,msha=read(tailroot,'manifest.json');certs={};tb={};provenance={}
 for region,count in ((2,256000),(3,8192)):
  cert,sha=read(tailroot,f'region{region}-action-{sector}.json');spec=cert['point_buffer'];mspec=manifest['buffers'][spec['file']]
  raw=base64.b64decode(b''.join((tailroot/x).read_bytes() for x in mspec['parts']),validate=True)
  assert len(raw)==mspec['bytes']==spec['bytes'] and hashlib.sha256(raw).hexdigest()==mspec['sha256']==spec['sha256']
  assert spec['bits']==256 and spec['width']==30 and spec['count']==cert['output_count']==count
  assert all(r['all_bank_input_terms_match'] for r in cert['complete_direct_row_checks'])
  assert 0<F(cert['rational']['complete_l2_error_upper'])<F('1e-12')
  # The accepted v14.331 exact-ratio method: verify the actual endpoint, not the false 0.258 shorthand.
  last=cert['output_first_mode']+2*(count-1);ratio=F(last*last,cert['tail_start']**2);assert ratio<F('0.258063')
  certs[region]=cert;tb[region]=ints(raw,count);provenance[f'region{region}_certificate_sha256']=sha
 mid,misha=read(mroot,f'refined-near-compact-middle-{sector}.json');cv=pointbuf(mroot,mid['buffer'])
 assert mid['complete_output_rows']==256000 and mid['first_output_mode']==certs[2]['output_first_mode']
 fc,fcsha=read(froot,f'refined-compact-far-{sector}.json');assert fc['physical_scalar_parameter_errors_included'] and not fc['infinite_seed_tail_action_included']
 r1,r1sha=read(froot,f'refined-region1-residual-{sector}.json');budget,bsha=read(payloads/'refined_remaining_residual_budget_v14_310','remaining-residual-budget.json')
 case=next(x for x in budget['cases'] if x['sector']==sector);T=F(case['rational']['global_source_and_lift_transport_reserved_once'])
 assert T==F(r1['rational']['source_transport_upper'])+F(r1['rational']['finite_lift_transport_upper'])
 shift=1 if sector=='odd-v' else 0
 r2=[S//(certs[2]['output_first_mode']+2*i-shift)-cv[i]-tb[2][i] for i in range(256000)]
 l2,h2=norm(r2);e2=F(mid['rational']['complete_compact_near_middle_action_error_upper'])+F(certs[2]['rational']['complete_l2_error_upper'])+upper(F(256000))/S
 # Point compact Far evaluation at the returned Region-3 window. Use normalized Horner, with an explicit rounding charge.
 a=certs[3]['output_first_mode'];assert a==fc['far_first_mode'];par=fc['point_parameters'];c=F(par['c']);L=F(par['L']);t=F(par['t']);P=F(par['pole_moment']);alpha=par['alpha']
 gam=[F(m['M_odd_rational'])/a**(2*j+2) for j,m in enumerate(fc['moments'])]
 bet=[F(m['Z_even_rational'])/a**(2*j+1) for j,m in enumerate(fc['moments'])]
 gs=[floor(x) for x in gam];bs=[floor(x) for x in bet];cc=floor(c);PP=floor(P)
 C=1+sum(abs(x) for x in gam+bet)+abs(alpha*L*P)+abs(c)+abs(P)
 roundrow=F(100000,S)*C
 rv=[];checks=[]
 for i in range(8192):
  n=a+2*i;x=a*S//n;tt=x*x//S;hg=hb=0
  for g,b in zip(reversed(gs),reversed(bs)):hg=g+tt*hg//S;hb=b+tt*hb//S
  z=z_eval(n);zl,zh=F(z['lower_rational']),F(z['upper_rational']);zp=(zl+zh)/2;assert abs(zp)<8 and max(zp-zl,zh-zp)<F("1e-39")
  zi=floor(zp);pole=floor(L*n/(n*n+t));point=cc*(zi*(tt*hg//S)//S-x*hb//S)//S+alpha*pole*PP//S
  if i in (0,4096,8191):
   exact=c*zp*sum(gam[j]*F(a,n)**(2*j+2) for j in range(42))-c*sum(bet[j]*F(a,n)**(2*j+1) for j in range(42))+alpha*L*n/(n*n+t)*P
   assert abs(F(point,S)-exact)<=roundrow
   checks.append({'n':n,'exact_retained_point_agrees_with_integer_Horner':True})
  rv.append(S//(n-shift)-point-tb[3][i])
 l3,h3=norm(rv)
 e3=F(certs[3]['rational']['complete_l2_error_upper'])+F(fc['rational']['geometric_action_remainder_upper'])+F(fc['physical_compact_far_parameter_charge_upper'])+upper(F(8192))*(roundrow+F(1,S))
 p1h=F(r1['rational']['point_norm_upper'])+F(r1['rational']['physical_composition_error_upper']);p1l=max(F(0),F(r1['rational']['point_norm_lower'])-F(r1['rational']['physical_composition_error_upper']))
 p2h=h2+e2;p2l=max(F(0),l2-e2);p3h=h3+e3;p3l=max(F(0),l3-e3)
 finite_hi=upper(p1h*p1h+p2h*p2h+p3h*p3h)+T
 finite_lo=max(F(0),upper(p1l*p1l+p2l*p2l+p3l*p3l)-F(1,S)-T)
 remaining_hi=upper(p2h*p2h+p3h*p3h);remaining_lo=max(F(0),upper(p2l*p2l+p3l*p3l)-F(1,S))
 out.mkdir(parents=True,exist_ok=True);bufs={'Middle-residual':write(out,sector,'middle-residual',r2),'Far-window-residual':write(out,sector,'far-window-residual',rv)}
 vals={'physical_middle_residual_lower':p2l,'physical_middle_residual_upper':p2h,'physical_far_window_residual_lower':p3l,'physical_far_window_residual_upper':p3h,'middle_action_and_source_floor_error_upper':e2,'far_window_action_and_numerical_error_upper':e3,'evaluated_remaining_physical_residual_lower':remaining_lo,'evaluated_remaining_physical_residual_upper':remaining_hi,'global_transport_reserved_once':T,'finite_evaluated_Schur_residual_lower':finite_lo,'finite_evaluated_Schur_residual_upper':finite_hi}
 return {'schema':'cone.returned-tail-refined-residual-composition.v1','sector':sector,'manifest_sha256':msha,'compact_middle_certificate_sha256':misha,'compact_far_certificate_sha256':fcsha,'region1_residual_certificate_sha256':r1sha,'budget_certificate_sha256':bsha,**provenance,'buffers':bufs,'rational':{k:str(v) for k,v in vals.items()},'display_approximate':{k:float(v) for k,v in vals.items()},'far_window_exact_point_checks':checks,'ratio_method':'exact per-row r=n^2/tail_start^2, as corrected in v14.331','global_transport_added_once':True,'finite_subset_above_3e_minus5':finite_lo>F('3e-5'),'finite_subset_upper_below_3e_minus5':finite_hi<F('3e-5'),'beyond_window_residual_evaluated':False,'whole_residual_acceptance_certified':False,'infinite_capacity_tail_closed':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--payload-root',type=Path,required=True);p.add_argument('--sector',choices=('even-v','odd-v'),required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();d=run(a.payload_root,a.sector,a.output_root);(a.output_root/f'returned-tail-residual-{a.sector}.json').write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps(d['display_approximate']),flush=True)

