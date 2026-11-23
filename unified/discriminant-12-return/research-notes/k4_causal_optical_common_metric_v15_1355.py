#!/usr/bin/env python3
"""Gravity v15.1355: first photon/free-endpoints/proper-clock observable
driven by same Maxwell+K4 metric as Audited v15.1353.
Linear-order background-null-path transfer, not exact geodesic shooting.
Full-gauge null and spatial convergence remain open.
"""
from pathlib import Path
import importlib.util
import numpy as np
from scipy.integrate import cumulative_trapezoid
from math import pi,sqrt

here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("core",here/"k4_independent_adm_momentum_v15_1351.py")
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)

def experiment(N=12,d=.045,amp=.1,neta=9,nt=7):
    eta=np.linspace(0,2*d,neta);times=np.exp(eta/sqrt(3));h=1/sqrt(3)
    fields=[]
    for tau in times:
        # Cauchy t=1 source is nonzero but assembled solver's cubic
        # spline requires strictly increasing times; extrapolate 1e-8.
        tbuild=max(tau,1+1e-8)
        metric=core.assemble(N,nt=nt,tf=tbuild,amplitude=amp)
        a=tbuild/sqrt(3)
        phi=-(metric["g00"]+1)/2
        bx=-metric["g0i"][0]/a
        sxx=metric["gij"][0,0]/a**2-1
        fields.append((phi,bx,sxx))
    freq=np.fft.fftfreq(N,d=4*pi/N)*2*pi
    m=np.fft.fftfreq(N)*N;parity=np.exp(1j*pi*m)
    def sample(f,x,dx=False):
        F=np.fft.fftn(f)/N**3
        yz=np.einsum("ijk,j,k->i",F,parity,parity)
        return float(np.real(np.dot(yz*(1j*freq if dx else 1),
                             np.exp(1j*freq*(x+2*pi)))))
    emitter=np.zeros((neta,3));mirror=np.zeros((neta,3))
    outgoing=np.zeros((neta,3));returning=np.zeros((neta,3))
    grad0=np.zeros(neta);gradd=np.zeros(neta)
    for j,(p,b,s) in enumerate(fields):
        emitter[j]=[sample(f,0) for f in (p,b,s)]
        mirror[j]=[sample(f,d) for f in (p,b,s)]
        outgoing[j]=[sample(f,eta[j]) for f in (p,b,s)]
        returning[j]=[sample(f,2*d-eta[j]) for f in (p,b,s)]
        grad0[j]=sample(p,0,True);gradd[j]=sample(p,d,True)
    # Both endpoints free-fall from zero perturbative displacement/velocity.
    # Same conformal-geodesic convention as archived v15.811.
    forcing=[
        -grad0+np.gradient(emitter[:,1],eta,edge_order=2)+h*emitter[:,1],
        -gradd+np.gradient(mirror[:,1],eta,edge_order=2)+h*mirror[:,1]
    ]
    endpoint_paths=[]
    for force in forcing:
        velocity=np.exp(-h*eta)*cumulative_trapezoid(
            np.exp(h*eta)*force,eta,initial=0)
        endpoint_paths.append(cumulative_trapezoid(velocity,eta,initial=0))
    xe,xm=endpoint_paths
    # Metric ds²/a²=−(1+2phi)deta²−2B_x deta dx+(1+sxx)dx².
    # Null first variations along background outward/return rays.
    o=-outgoing[:,0]-outgoing[:,1]+outgoing[:,2]/2
    r=-returning[:,0]+returning[:,1]+returning[:,2]/2
    halfway=(neta-1)//2
    flight=(np.trapezoid(o[:halfway+1],eta[:halfway+1])
           +np.trapezoid(r[halfway:],eta[halfway:]))
    boundary=2*xm[halfway]-xe[-1]-xe[0]
    # Proper emitter clock; physical emission event fixed at eta0=0.
    clock=np.trapezoid(times*emitter[:,0]/sqrt(3),eta)
    delta=times[-1]/sqrt(3)*(flight+boundary)+clock
    result=dict(N=N,d=d,neta=neta,amp=amp,
        reception_tau=float(times[-1]),
        photon_flight=float(flight),free_endpoint=float(boundary),
        emitter_proper_clock=float(clock),
        roundtrip_proper_time_correction=float(delta),
        max_emitter_lapse=float(np.max(abs(emitter[:,0]))),
        free_mirror_shift=float(xm[halfway]),
        free_emitter_shift=float(xe[-1]))
    print(result,flush=True)
    return result

if __name__=="__main__":
    x=experiment(12,neta=9,nt=7)
    y=experiment(12,neta=17,nt=7)
    z=experiment(16,neta=9,nt=7)
    w=experiment(12,neta=9,nt=7,amp=.05)
    zero=experiment(12,neta=9,nt=7,amp=0)
    assert abs(zero["roundtrip_proper_time_correction"])<1e-14
    assert abs(x["roundtrip_proper_time_correction"])>1e-7
    assert abs(x["roundtrip_proper_time_correction"]/w["roundtrip_proper_time_correction"]-4)<1e-6
    assert abs(x["roundtrip_proper_time_correction"]-y["roundtrip_proper_time_correction"])<1e-8
    print("PASS nonzero source-driven null/free-mirror/proper-clock transfer")
    print("OPEN spatial convergence, arbitrary 3+1 gauge null and exact ray shooting")
