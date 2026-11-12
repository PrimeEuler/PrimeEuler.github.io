#!/usr/bin/env python3
"""v15.810: local Minkowski S/V/TT first-order round-trip time.

Photon outgoing/return null paths, free endpoints and beam-splitter proper
clock all retained. Pure diffeo null and audited v15.794 TT limit.
The harmonic metric input is generic, NOT an on-shell K4 sourced FLRW
solution. Prepared zero coordinate position/velocity initial conditions
are gauge-specific; transform the mirror Cauchy data under diffeos.
"""
import sympy as sp
import numpy as np
from scipy.integrate import quad

T,U,E,R=sp.symbols("T U E R")
opt=(T-U)*(E-1)+(T+U)*(R-E)
mir=U*(2*E-1-R)
clock=T*(1-R)
assert sp.expand(opt+mir+clock)==0
assert sp.expand(opt+mir-T*(R-1))==0
# Here E=e^[i(lambda-omega)L], R=e^[-2i omega L].
# The above are the exact pure-gauge photon, worldline, clock pieces.

def F(z):
    return np.exp(1j*z/2)*np.sinc(z/(2*np.pi))

def response(omega,lam,L,te,Phi,Psi,V,H):
    """Metric h00=-2Phi, h0u=-V, huu=-2Psi+H,
    each multiplied by exp[-i omega t+i lam x_u].
    Endpoints initially have zero coordinate displacement/velocity at t=0
    in this chosen Newtonian/vector/TT gauge.
    """
    x=omega*L;y=lam*L;phase=np.exp(-1j*omega*te)
    out=L*phase*(-Phi-Psi-V+H/2)*F(y-x)
    back=L*phase*(-Phi-Psi+V+H/2)*np.exp(1j*(y-x))*F(-y-x)
    clk=2*L*phase*Phi*F(-2*x)
    # a_u=-i*(lam*Phi+omega*V)*exp[-i omega t+i lam x_u].
    alpha=-1j*(lam*Phi+omega*V)
    primitive=lambda t:(1-np.exp(-1j*omega*t)-1j*omega*t)/omega**2
    endpoints=alpha*(2*np.exp(1j*y)*primitive(te+L)
                     -primitive(te)-primitive(te+2*L))
    return out+back+clk+endpoints,(out,back,clk,endpoints)

def integral(fn,a,b):
    return quad(lambda z:np.real(fn(z)),a,b,epsabs=1e-12)[0]+1j*quad(
        lambda z:np.imag(fn(z)),a,b,epsabs=1e-12)[0]

for params in [
    (.9,.3,.7,0.,.18,-.07,.12,.05),
    (1.7,.8,.4,.33,-.2,.14,.04,.11),
    (2.,0.,.65,.4,.1,.08,.3,-.2),
]:
    omega,lam,L,te,Phi,Psi,V,H=params
    e=np.exp
    out=integral(lambda z:(-Phi-Psi-V+H/2)*e(
        -1j*omega*(te+z)+1j*lam*z),0,L)
    back=integral(lambda z:(-Phi-Psi+V+H/2)*e(
        -1j*omega*(te+L+z)+1j*lam*(L-z)),0,L)
    clk=integral(lambda z:Phi*e(-1j*omega*(te+z)),0,2*L)
    alpha=-1j*(lam*Phi+omega*V)
    primitive=lambda t:(1-e(-1j*omega*t)-1j*omega*t)/omega**2
    endpoints=alpha*(2*e(1j*lam*L)*primitive(te+L)
                     -primitive(te)-primitive(te+2*L))
    analytic,_=response(*params)
    assert abs(analytic-out-back-clk-endpoints)<2e-12
    print("PASS independent photon quadratures and free mirror/clock",params,
          "roundtrip",analytic)

omega,lam,L,te,H=1.3,.5,.4,.2,.15
tt,_=response(omega,lam,L,te,0,0,0,H)
old=.5*L*H*np.exp(-1j*omega*te)*(F((lam-omega)*L)
    +np.exp(1j*(lam-omega)*L)*F((-lam-omega)*L))
assert abs(tt-old)<1e-13
static,_=response(1e-5,.6,.3,0,0,0,.2,0)
assert abs(static)<1e-5
print("PASS pure gauge cancellation, v15.794 TT control, static V null")
print("SCOPE: local flat metric, no K4 FLRW source, no instrument calibration")
