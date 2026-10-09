#!/usr/bin/env python3
"""Exact convolution coefficients for the full-Z near-octave source."""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_exact_integer_source_action import convolution,dot,norm2,sqrt_upper
from suzuki_full_stationary_source_transport import combine,PINS
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
sys.set_int_max_str_digits(0)
BITS=256

def packhash(values,bits):
    width=max(1,(max(abs(x).bit_length() for x in values)+8)//8)
    raw=b''.join(x.to_bytes(width,'little',signed=True) for x in values)
    return {'bits':bits,'count':len(values),'width':width,'sha256':hashlib.sha256(raw).hexdigest()}

def convrows(x,z,start,bits=BITS):
    N=len(x);scale=1<<bits
    h=[0]+[scale//(2*k) for k in range(1,2*N)]
    g=[scale//(2*(k+start)) for k in range(3*N-1)]
    hx=convolution(x,h,N,N);gx=convolution(x[::-1],g,2*N-1,N)
    hz=convolution(z,h,N,N);gz=convolution(z[::-1],g,2*N-1,N)
    return [a-b for a,b in zip(hx,gx)],[a+b for a,b in zip(hz,gz)]

def selftest():
    cases=0
    for start in (1,2):
      for N in (2,3,7):
        x=[(-1)**j*(j+2) for j in range(N)];z=[(j-3)*x[j] for j in range(N)]
        u,v=convrows(x,z,start,12);scale=1<<12
        for k in range(N):
          i=N+k
          uh=sum((scale//(2*(i-j))-scale//(2*(i+j+start)))*x[j] for j in range(N))
          vh=sum((scale//(2*(i-j))+scale//(2*(i+j+start)))*z[j] for j in range(N))
          assert u[k]==uh and v[k]==vh;cases+=1
    return cases

def run(root,source_root,sector,buffer_root=None):
    short=sector.split('-')[0];stem=f'joint-256000-{sector}.trace-256000.full'
    raw=(root/(stem+'.zip')).read_bytes();assert hashlib.sha256(raw).hexdigest()==PINS[sector][0]
    sr=(source_root/f'full-stationary-source-{sector}.json').read_bytes();d=json.loads(sr)
    expected={'even-v':'40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80','odd-v':'41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f'}
    assert hashlib.sha256(sr).hexdigest()==expected[sector]
    meta,s,V,_=read_snapshot(root/(stem+'.zip'))
    Z=combine(V,[F(x) for x in d['q_rational']]);N=len(Z['values']);start=s['modes'][0]
    assert N==128000 and start in (1,2)
    assert packhash(Z['values'],Z['bits'])['sha256']==d['full_vector_binary_sha256']
    x=Z['values'];zx=[a*b for a,b in zip(s['z']['values'],x)]
    print(sector,'four exact near convolutions begin',flush=True)
    u,v=convrows(x,zx,start)
    ub=Z['bits']+BITS;vb=Z['bits']+s['z']['bits']+BITS
    c=F(s['c']['values'][0],1<<s['c']['bits']);P=dot(s['pole'],Z)
    pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
    hyp=enclose(hyperbolic(start==2));ell=times(times(constant(4),hyp),recip(pi))
    ti=times(recip(pi),recip(pi));L=sum(ell)/2;t=sum(ti)/2
    scale=1<<BITS;aa=[];ww=[]
    for k,(up,vp) in enumerate(zip(u,v)):
        n=2*(N+k)+start
        a=c*F(up,1<<ub)/2
        pole=L*n/(n*n+t)
        w=F(1,n-1 if start==2 else n)+c*F(vp,1<<vb)/2-s['alpha']*pole*P
        aa.append(a.numerator*scale//a.denominator)
        ww.append(w.numerator*scale//w.denominator)
    print(sector,'near coefficients complete',flush=True)
    if buffer_root is not None:
        buffer_root.mkdir(parents=True,exist_ok=True)
        for name,values in [('A',aa),('W',ww)]:
            spec=packhash(values,BITS)
            packed=b''.join(x.to_bytes(spec['width'],'little',signed=True) for x in values)
            assert hashlib.sha256(packed).hexdigest()==spec['sha256']
            (buffer_root/(sector+'-'+name+'.bin')).write_bytes(packed)
    l1=F(sum(abs(a) for a in x),1<<Z['bits'])
    # Exact physical remote z_n is retained; only finite scalars and kernels
    # are rounded. Point finite |z_m|<=11, |c|<1, |z_remote|<8.
    assert abs(c)<1 and max(abs(a) for a in s['z']['values'])<=11*(1<<s['z']['bits'])
    ez=ep=ec=F('1e-38')  # ep relaxed from audited 1e-39.
    rootN=sqrt_upper(F(N),192)
    # Absolute row bound uses |H|,|G|<=1 at the adjacent boundary.
    # Finite-z and c errors, pole-moment error, exact-kernel rounding,
    # and both stored coefficient roundings are charged separately.
    near_error=rootN*((ez+19*ec)*l1+19*l1/scale+9/scale)
    # Remote pole midpoint formula error: interval endpoints themselves
    # are checked; |dp| <= |dL|/n + Lmax |dt|/n^3.
    n0=256000+start
    dp=(ell[1]-ell[0])/n0+ell[1]*(ti[1]-ti[0])/n0**3
    assert dp<F('1e-90') and ell[1]<2 and ti[0]>0
    near_error+=rootN*(4*ep*l1/n0+2*dp*abs(P))
    an=sqrt_upper(F(sum(a*a for a in aa),scale*scale),192)
    wn=sqrt_upper(F(sum(w*w for w in ww),scale*scale),192)
    near_norm=wn+8*an+near_error
    assert near_error<F('1e-20')
    return {'schema':'cone.near-full-stationary-affine-source.v1','sector':sector,
      'source_snapshot_sha256':PINS[sector][0],'full_stationary_certificate_sha256':expected[sector],
      'first_near_mode':n0,'last_near_mode':512000-2+start,'near_count':N,
      'representation':'rho_hat(n)=W[n]-z_physical(n)*A[n] on R<n<=2R',
      'A_buffer':packhash(aa,BITS),'W_buffer':packhash(ww,BITS),
      'physical_remote_z_retained_exact':True,
      'scalar_caps_rational':{'finite_z':str(ez),'finite_pole':str(ep),'c':str(ec)},
      'kernel_bits':BITS,'coefficient_bits':BITS,
      'rational':{'near_assembly_error_upper':str(near_error),'A_norm_upper':str(an),'W_norm_upper':str(wn),'physical_near_source_norm_upper':str(near_norm)},
      'display_approximate':{'near_assembly_error_upper':float(near_error),'A_norm_upper':float(an),'W_norm_upper':float(wn),'physical_near_source_norm_upper':float(near_norm)},
      'exact_small_convolution_rows_checked':selftest(),
      'remote_scalar_numeric_evaluation_certified':False,'evaluated_infinite_trial':False,'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--sector',choices=list(PINS),required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--buffer-root',type=Path)
    a=p.parse_args();o=run(a.root,a.source_root,a.sector,a.buffer_root);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps(o['display_approximate'],indent=2))
