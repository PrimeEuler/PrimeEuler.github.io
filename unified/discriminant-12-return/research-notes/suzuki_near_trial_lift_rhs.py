#!/usr/bin/env python3
"""A compact represented near seed and all physical finite-lift RHS rows.

This is a NEW probe RHS, not an old source or a claimed stationary trial.
"""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_exact_integer_source_action import convolution,sqrt_upper
from suzuki_full_stationary_source_transport import PINS
from suzuki_bulk_action_z import evaluate
from suzuki_certified_remote_diagonal import log_normalized
from suzuki_frozen_trial_far_outward import atan_recip,hyperbolic,add,times,neg,constant,recip,enclose
from suzuki_certified_remote_z import enclosure,midpoint,radius

def digest(b):return hashlib.sha256(b).hexdigest()
def floor(q,bits):return q.numerator*(1<<bits)//q.denominator
def transpose_rows(x,z,start,bits=256):
    N=len(x);scale=1<<bits
    h=[0]+[scale//(2*j) for j in range(1,2*N)]
    g=[scale//(2*(j+start)) for j in range(3*N-1)]
    hx=convolution(x[::-1],h,N,N)[::-1];gx=convolution(x[::-1],g,2*N-1,N)
    hz=convolution(z[::-1],h,N,N)[::-1];gz=convolution(z[::-1],g,2*N-1,N)
    return [a-b for a,b in zip(hz,gz)],[a+b for a,b in zip(hx,gx)]

def algebra_checks():
    count=0
    for start in (1,2):
        for N in (2,3,7):
            x=[(-1)**j*(j+2) for j in range(N)];z=[(j-3)*x[j] for j in range(N)]
            u,v=transpose_rows(x,z,start,12);scale=1<<12
            for j in range(N):
                uu=sum((scale//(2*(N+k-j))-scale//(2*(N+k+j+start)))*z[k] for k in range(N))
                vv=sum((scale//(2*(N+k-j))+scale//(2*(N+k+j+start)))*x[k] for k in range(N))
                assert u[j]==uu and v[j]==vv;count+=1
    return count

def writebuffer(root,sector,name,values,bits):
    width=max(1,(max(abs(x).bit_length() for x in values)+8)//8)
    raw=b''.join(x.to_bytes(width,'little',signed=True) for x in values)
    filename=f'{sector}-{name}.bin';(root/filename).write_bytes(raw)
    return {'file':filename,'bits':bits,'width':width,'count':len(values),'bytes':len(raw),'sha256':digest(raw)}

def run(root,numerical_root,sector,out):
    stem=f'joint-256000-{sector}.trace-256000.full'
    snapshot=root/(stem+'.zip');assert digest(snapshot.read_bytes())==PINS[sector][0]
    primary=(root/(stem+'.certificate.json')).read_bytes()
    assert digest(primary)==PINS[sector][1]
    d=json.loads(primary);assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
    _,s,_,_=read_snapshot(snapshot);N=len(s['modes']);start=s['modes'][0]
    assert N==128000 and start in (1,2)
    cr=(numerical_root/f'numerical-near-source-{sector}.json').read_bytes()
    pins={'even-v':'5b1aa36fe37e8b5b5c7d29f49946f50b81c09302cc11e7cea1cde3e9d009c3d4','odd-v':'28d3215e550093f1a56d6617a75545ef4c3ea519d6a1ac011c127f1e84ead37c'}
    assert digest(cr)==pins[sector];cert=json.loads(cr);spec=cert['point_buffer']
    raw=(numerical_root/f'{sector}-rho-near.bin').read_bytes()
    assert digest(raw)==spec['sha256'] and len(raw)==spec['bytes']
    rho=[int.from_bytes(raw[j:j+spec['width']],'little',signed=True) for j in range(0,len(raw),spec['width'])]
    pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
    ell=times(times(constant(4),enclose(hyperbolic(start==2))),recip(pi));ti=times(recip(pi),recip(pi))
    li=enclosure(*ell,256);tt=enclosure(*ti,256);L=midpoint(li,256);t=midpoint(tt,256)
    assert radius(li,L)<F(2,1<<256) and radius(tt,t)<F(2,1<<256) and ell[1]<2
    yy=[];zz=[];pp=[];maxrad=F(0)
    for i,r in enumerate(rho):
        n=2*(N+i)+start
        logpoint=sum(log_normalized(n,128))/2;assert logpoint>11
        yy.append(floor(F(r,1<<128)/logpoint,160))
        row=evaluate(n);lo,hi=F(row['lower_rational']),F(row['upper_rational'])
        zpoint=(lo+hi)/2;zint=floor(zpoint,160)
        maxrad=max(maxrad,max(abs(lo-F(zint,1<<160)),abs(hi-F(zint,1<<160))))
        zz.append(zint);pp.append(floor(L*n/(n*n+t),256))
        if (i+1)%16000==0:print(sector,'new seed and action-z rows',i+1,'/',N,flush=True)
    assert maxrad<F('1e-39') and max(abs(z) for z in zz)<8*(1<<160)
    assert max(abs(z) for z in s['z']['values'])<11*(1<<s['z']['bits'])
    assert max(abs(p) for p in s['pole']['values'])<2*(1<<s['pole']['bits'])
    l1=F(sum(abs(y) for y in yy),1<<160)
    ynorm=sqrt_upper(F(sum(y*y for y in yy),1<<320),192)
    assert ynorm<F('0.0001')
    print(sector,'four new transpose convolutions begin',flush=True)
    zy=[z*y for z,y in zip(zz,yy)];u,v=transpose_rows(yy,zy,start)
    c=F(s['c']['values'][0],1<<s['c']['bits']);assert abs(c)<1
    P=F(sum(p*y for p,y in zip(pp,yy)),1<<416)
    gg=[]
    for j,(up,vp) in enumerate(zip(u,v)):
        zf=F(s['z']['values'][j],1<<s['z']['bits']);pf=F(s['pole']['values'][j],1<<s['pole']['bits'])
        g=c*(F(up,1<<576)-zf*F(vp,1<<416))/2+s['alpha']*pf*P
        gg.append(floor(g,256))
    # Complete l2 physical RHS error, excluding the finite solve itself.
    eps=F(1,1<<256);ep=4*eps
    rowerror=(F('21e-38')+19*eps)*l1+2*F('1e-38')*abs(P)+4*ep*l1+eps
    rhs_error=sqrt_upper(F(N),192)*rowerror
    # Already certified sqrt(G)<5e14 and inverse-energy coupling chi<21.
    weighted_error=5*10**14*rhs_error;propagated=22*weighted_error
    assert rhs_error<F('1e-30') and propagated<F('1e-18')
    # Six COMPLETE rounded-kernel direct sums at first, middle and last front rows.
    checks=[];scale=1<<256
    for j in (0,N//2,N-1):
        du=sum((scale//(2*(N+k-j))-scale//(2*(N+k+j+start)))*zy[k] for k in range(N))
        dv=sum((scale//(2*(N+k-j))+scale//(2*(N+k+j+start)))*yy[k] for k in range(N))
        assert du==u[j] and dv==v[j]
        zf=F(s['z']['values'][j],1<<s['z']['bits']);pf=F(s['pole']['values'][j],1<<s['pole']['bits'])
        direct=c*(F(du,1<<576)-zf*F(dv,1<<416))/2+s['alpha']*pf*P
        assert floor(direct,256)==gg[j]
        checks.append({'front_index':j,'physical_mode':2*j+start,'all_128000_terms_match':True})
    out.mkdir(parents=True,exist_ok=True)
    buffers={name:writebuffer(out,sector,name,vals,bits) for name,vals,bits in [('trial-near',yy,160),('action-z-near',zz,160),('lift-rhs',gg,256)]}
    return {'schema':'cone.new-compact-near-trial-lift-rhs.v1','sector':sector,
        'snapshot_sha256':PINS[sector][0],'near_source_certificate_sha256':digest(cr),
        'near_source_point_sha256':spec['sha256'],'first_near_mode':256000+start,'last_near_mode':512000-2+start,
        'trial_definition':'y(n)=floor_160(rho_near_point(n)/midpoint(log_normalized(n,128))) on Near, zero elsewhere',
        'rhs_definition':'g=B_Near_physical^* y; every finite front row included; pole retained',
        'buffers':buffers,'rational':{'trial_norm_upper':str(ynorm),'trial_l1':str(l1),
            'maximum_action_z_point_error_upper':str(maxrad),'physical_lift_rhs_error_upper':str(rhs_error),
            'inverse_energy_rhs_error_upper':str(weighted_error),'future_remote_action_rhs_charge_upper':str(propagated)},
        'display_approximate':{'trial_norm_upper':float(ynorm),'physical_lift_rhs_error_upper':float(rhs_error),
            'future_remote_action_rhs_charge_upper':float(propagated)},
        'direct_complete_front_rows':checks,'small_transpose_rows_verified':algebra_checks(),
        'new_trial_dependent_rhs_evaluated':True,'trial_admissible_by_finite_support':True,
        'trial_far_component_present':False,'finite_lift_solve_certified':False,
        'whole_remote_action_evaluated':False,'stationary_acceptance_met':False,'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('root','numerical-root','output-root'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--sector',choices=list(PINS),required=True);a=p.parse_args()
    o=run(a.root,a.numerical_root,a.sector,a.output_root)
    (a.output_root/f'new-near-trial-rhs-{a.sector}.json').write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps(o['display_approximate'],indent=2),flush=True)
