#!/usr/bin/env python3
"""v15.811: FLRW coasting conformal scalar/vector/tensor roundtrip transfer.

Harmonic metric inputs supplied externally, not sourced from actual K4
field evolution yet. Photon paths, comoving/free mirrors with Hubble
friction, and receiver proper clock enter consistently at first order.
Background conformal scale factor a(eta)=a0*exp(h*eta), h=1/sqrt3.
Boundary conditions: freely falling mirror coordinate displacement
and velocity zero at eta_e=0 in the chosen metric gauge. Not a
far-field, complete gauge-invariant optical instrument simulation.
"""
import numpy as np
from scipy.integrate import quad
h=1/np.sqrt(3)
def F(z):
    return np.exp(1j*z/2)*np.sinc(z/(2*np.pi))
def J(t,w,h):
    # Green solution x''+h*x'=A exp(-i w eta), zero data at eta=0.
    return ((1-np.exp(-1j*w*t))/(1j*w)
         -(np.exp(-1j*w*t)-np.exp(-h*t))/(h-1j*w))/h
def amplitude(w,l,d,ph,ps,v,tt,h=h,a0=1.):
    # For metric ds²=a²[-(1+2Phi)deta²-2V_i deta dxi
    #                +((1-2Psi)deltaij+Hij)dxidxj].
    # x=w*d, y=l*d=(k dot arm)*d.
    x=w*d;y=l*d
    out=d*(-ph-ps-v+tt/2)*F(y-x)
    back=d*(-ph-ps+v+tt/2)*np.exp(1j*(y-x))*F(-y-x)
    # Free mirror: delta x''+h delta x' =
    #  -partial_u Phi + V_u' + h V_u.
    source=-1j*l*ph+(-1j*w+h)*v
    move=source*(2*np.exp(1j*y)*J(d,w,h)-J(0,w,h)-J(2*d,w,h))
    # Beam-splitter clock proper-time correction at fixed conformal eta.
    clock=a0*ph*(np.exp((h-1j*w)*2*d)-1)/(h-1j*w)
    ret=a0*np.exp(2*h*d)*(out+back+move)
    return ret+clock,(out,back,move,clock)
def complex_quad(fn,a,b):
    return quad(lambda z:np.real(fn(z)),a,b,epsabs=1e-12)[0]+1j*quad(
           lambda z:np.imag(fn(z)),a,b,epsabs=1e-12)[0]
for par in [(1.1,.4,.6,.15,-.09,.08,.1),
            (1.8,.8,.4,-.2,.14,.04,.11),
            (2.,0.,.55,.1,.08,.3,-.2)]:
    w,l,d,ph,ps,v,tt=par
    out=complex_quad(lambda s:(-ph-ps-v+tt/2)*np.exp(
        1j*(l-w)*s),0,d)
    back=complex_quad(lambda s:(-ph-ps+v+tt/2)*np.exp(
        1j*(l-w)*d-1j*(l+w)*s),0,d)
    source=-1j*l*ph+(-1j*w+h)*v
    # Independent numerical integration of the free mirror Green kernel.
    def displacement(t):
        return complex_quad(lambda s:source*(
            1-np.exp(-h*(t-s)))/h*np.exp(-1j*w*s),0,t)
    mir=2*np.exp(1j*l*d)*displacement(d)-displacement(2*d)
    clk=complex_quad(lambda s:ph*np.exp((h-1j*w)*s),0,2*d)
    ref=np.exp(2*h*d)*(out+back+mir)+clk
    calc,_=amplitude(*par)
    assert abs(calc-ref)<3e-12
    print("PASS independent conformal null-path/mirror/clock quadrature",par,calc)
def flat(w,l,d,ph,ps,v,tt):
    x=w*d;y=l*d
    force=-1j*(l*ph+w*v)
    J0=lambda t:(1-np.exp(-1j*w*t)-1j*w*t)/w**2
    return (d*(-ph-ps-v+tt/2)*F(y-x)
          +d*(-ph-ps+v+tt/2)*np.exp(1j*(y-x))*F(-y-x)
          +2*d*ph*F(-2*x)
          +force*(2*np.exp(1j*y)*J0(d)-J0(0)-J0(2*d)))
for h0 in [1e-2,1e-3,1e-4]:
    par=(1.1,.4,.6,.15,-.09,.08,.1)
    result,_=amplitude(*par,h=h0)
    assert abs(result-flat(*par))<.12*h0
    print("PASS flat-space limit",h0)
print("PASS coasting FLRW photon path, free mirrors, proper clock")
print("SCOPE: metric transfer only, no sourced K4 history inserted yet")
