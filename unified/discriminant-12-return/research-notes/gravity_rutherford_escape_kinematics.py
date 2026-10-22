#!/usr/bin/env python3
"""Equal-mass elastic Rutherford escape geometry, independent of Suzuki compute.

This computes only the angular integral conditional on incident v,w.
For a physical rate still supply Maxwellian target w density, n*g*K/g^4
and the BPS-matched hard/soft separation. No invented normalization.
"""
import numpy as np
from scipy.integrate import quad

def escape_fraction(v,w,mu,r,theta):
    v,w=np.asarray(v,float),np.asarray(w,float)
    gvec=v-w
    g=np.linalg.norm(gvec)
    if g==0:
        return float(v@v >= 2*mu/r)
    khat=gvec/g
    V=(v+w)/2
    vp=V@khat
    vt=np.linalg.norm(V-vp*khat)
    a=V@V+g*g/4+g*vp*np.cos(theta)
    b=g*vt*np.sin(theta)
    if b<1e-14:
        return float(a>=2*mu/r)
    c=(2*mu/r-a)/b
    if c>=1:return 0.
    if c<=-1:return 1.
    return float(np.arccos(c)/np.pi)

def angular_factor(v,w,mu,r,theta_min=.1,breakpoint=None):
    def f(theta):
        return 2*np.pi*np.sin(theta)*escape_fraction(v,w,mu,r,theta)/(np.sin(theta/2)**4)
    pts=[breakpoint] if breakpoint is not None and theta_min<breakpoint<np.pi else None
    return quad(f,theta_min,np.pi,epsabs=1e-10,limit=350,points=pts)[0]

if __name__=="__main__":
    # mu=r=1; v_esc=sqrt(2); incoming test particle is bound at v=0.8.
    v=np.array([0.,.8,0.]);w=np.array([0.,3.,0.])
    V=(v+w)/2;g=np.linalg.norm(v-w)
    c=(V@V+g*g/4-2)/(g*np.linalg.norm(V))
    theta0=float(np.arccos(c))
    assert escape_fraction(v,w,1,1,theta0-.001)==0
    assert escape_fraction(v,w,1,1,theta0+.001)==1
    exact=4*np.pi*(1/np.sin(theta0/2)**2-1)
    for cutoff in [.01,.05,.1,.5]:
        value=angular_factor(v,w,1,1,cutoff,theta0)
        assert abs(value-exact)<1e-7
        print(f"theta_min={cutoff} angular escape factor={value:.12f}")
    print(f"threshold angle={theta0:.12f}; analytic factor={exact:.12f}")
    print("PASS; not a BPS-matched global numerical kernel")
