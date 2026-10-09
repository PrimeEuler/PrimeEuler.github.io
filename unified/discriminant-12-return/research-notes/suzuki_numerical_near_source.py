#!/usr/bin/env python3
"""Evaluate every near-octave source row with the certified physical z."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from suzuki_certified_remote_z import evaluate
from suzuki_exact_integer_source_action import sqrt_upper
sys.set_int_max_str_digits(0)
PINS={'even-v':'90f45412062618233c6b78ccd201c8822933c2b0779a04537c673b3cc089a83f','odd-v':'ce8fde3246e8dd584a92e78a1b4a677434d253db687f5b06728c2a703a4b5a56'}

def run(cert_root,buffer_root,source_root,sector,output_root):
    raw=(cert_root/f'near-source-{sector}.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==PINS[sector]
    near=json.loads(raw);sr=(source_root/f'full-stationary-source-{sector}.json').read_bytes()
    assert hashlib.sha256(sr).hexdigest()==near['full_stationary_certificate_sha256']
    full=json.loads(sr);arrays=[]
    for name in ('A','W'):
        spec=near[name+'_buffer'];rawbuf=(buffer_root/(sector+'-'+name+'.bin')).read_bytes()
        assert hashlib.sha256(rawbuf).hexdigest()==spec['sha256'] and len(rawbuf)==spec['count']*spec['width']
        assert spec['bits']==256
        arrays.append([int.from_bytes(rawbuf[i:i+spec['width']],'little',signed=True) for i in range(0,len(rawbuf),spec['width'])])
    aa,ww=arrays;N=len(aa);assert N==128000
    scale=1<<128;values=[];sum2=0;maxradius=F(0)
    for i,(a,w) in enumerate(zip(aa,ww)):
        n=near['first_near_mode']+2*i
        z=evaluate(n);lo,hi=F(z['lower_rational']),F(z['upper_rational']);center=(lo+hi)/2
        maxradius=max(maxradius,(hi-lo)/2)
        rho=F(w,1<<256)-F(a,1<<256)*center
        value=rho.numerator*scale//rho.denominator
        values.append(value);sum2+=value*value
        if (i+1)%16000==0:print(sector,'certified numerical rows',i+1,'/',N,flush=True)
    point_norm=sqrt_upper(F(sum2,scale*scale),192)
    evaluation=sqrt_upper(F(N),192)/scale+F('1e-10')*F(near['rational']['A_norm_upper'])
    error=evaluation+F(near['rational']['near_assembly_error_upper'])
    true_error=error+F(full['rational']['whole_remote_source_transport_upper'])
    assert evaluation<F('4e-15') and maxradius<F('1e-10')
    packed=b''.join(x.to_bytes(17,'little',signed=True) for x in values)
    output_root.mkdir(parents=True,exist_ok=True);(output_root/(sector+'-rho-near.bin')).write_bytes(packed)
    return {'schema':'cone.certified-numerical-near-source.v1','sector':sector,
      'near_affine_certificate_sha256':PINS[sector],
      'full_source_certificate_sha256':hashlib.sha256(sr).hexdigest(),
      'first_mode':near['first_near_mode'],'last_mode':near['last_near_mode'],'count':N,
      'point_buffer':{'bits':128,'width':17,'bytes':len(packed),'sha256':hashlib.sha256(packed).hexdigest()},
      'rational':{'point_norm_upper':str(point_norm),'numerical_z_and_output_rounding_error_upper':str(evaluation),
        'represented_Z_source_error_upper':str(error),'true_full_inverse_source_error_upper':str(true_error),
        'true_source_near_norm_upper':str(point_norm+true_error),'maximum_z_radius_upper':str(maxradius)},
      'display_approximate':{'point_norm':float(point_norm),'numeric_error':float(evaluation),'true_near_norm':float(point_norm+true_error)},
      'all_128000_physical_rows_evaluated':True,'output_rounding_charged':True,
      'far_source_numerical_rows_enumerated':False,'evaluated_trial_or_action':False,
      'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('cert-root','buffer-root','source-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--sector',choices=list(PINS),required=True)
    a=p.parse_args();o=run(a.cert_root,a.buffer_root,a.source_root,a.sector,a.output_root)
    (a.output_root/f'numerical-near-source-{a.sector}.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps(o['display_approximate'],indent=2))
