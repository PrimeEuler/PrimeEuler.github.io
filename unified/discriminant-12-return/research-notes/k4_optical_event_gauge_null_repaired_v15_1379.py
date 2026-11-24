#!/usr/bin/env python3
"""v15.1379: repaired committed pure-gauge null using the exact archived v15.1355 optical transfer.
Physical source unchanged. T=A eta^3 cos(x), U=B eta^3 sin(x);
both coordinate generators and first derivatives vanish at emission.
"""
from pathlib import Path
import importlib.util
from math import pi,sqrt
import numpy as np
from functools import lru_cache
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('optical',root/'k4_causal_optical_common_metric_v15_1355.py')
optical=importlib.util.module_from_spec(spec)
spec.loader.exec_module(optical)
original=optical.core.assemble
@lru_cache(maxsize=96)
def cached(n,nt,tf,amplitude):
    return original(n,nt=nt,tf=tf,amplitude=amplitude)
optical.core.assemble=cached

def overlay(N,t,amplitude,A=.001,B=-.0007,**kwargs):
    base=cached(N,kwargs["nt"],t,amplitude)
    base={k:(v.copy() if isinstance(v,np.ndarray) else v) for k,v in base.items()}
    eta=sqrt(3)*np.log(t);a=t/sqrt(3);h=1/sqrt(3)
    x=(np.arange(N)-N//2)*4*pi/N
    c=np.cos(x)[:,None,None];s=np.sin(x)[:,None,None]
    Phi=-(3*A*eta**2+h*A*eta**3)*c
    V=(3*B*eta**2+A*eta**3)*s
    S=-2*(h*A+B)*eta**3*c
    base['g00']=base['g00']-2*Phi
    base['g0i'][0]=base['g0i'][0]-a*V
    base['gij'][0,0]=base['gij'][0,0]+a*a*S
    return base

def compare(neta=9,amplitude=.1,N=12,A=.001,B=-.0007):
    kwargs=dict(N=N,neta=neta,nt=7,amp=amplitude)
    baseline=optical.experiment(**kwargs)
    def shifted(n,nt,tf,amplitude):
        return overlay(n,tf,amplitude,A=A,B=B,nt=nt)
    optical.core.assemble=shifted
    try:transformed=optical.experiment(**kwargs)
    finally:optical.core.assemble=cached
    diff=transformed['roundtrip_proper_time_correction']-baseline['roundtrip_proper_time_correction']
    print('GAUGE TEST',dict(neta=neta,source_amplitude=amplitude,
        baseline=baseline['roundtrip_proper_time_correction'],transformed=transformed['roundtrip_proper_time_correction'],
        gauge_difference=diff),flush=True)
    return diff

if __name__=='__main__':
    a=compare(9,0.);b=compare(17,0.)
    assert abs(b)<1e-10 and 3<a/b<5
    x=compare(9,.1);y=compare(17,.1)
    assert abs(x-a)<1e-12 and abs(y-b)<1e-12
    print('PASS pure-gauge null and source-overlay invariance to O(dt²)')
    print('OPEN nonzero emission-event diffeo, continuum and arbitrary 3+1 gauge')
