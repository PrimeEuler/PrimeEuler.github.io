#!/usr/bin/env python3
"""v15.821: FLRW pure-diffeomorphism optical endpoint and five-arm null.

An infinitesimal passive gauge shift eta'=eta+T, x'=x+U induces
Phi=-(T_eta+H*T), Psi_arm=H*T+partial_x U,
V_arm=U_eta-partial_x T in the projected conformal metric.
The detector observable includes the transformed physical emission
event, the null photon round trip, free test-mass worldlines, and the
emitter's proper clock. This is an explicit pure-gauge null, not a
general gauge-covariance theorem for all K4 perturbations.
"""
import numpy as np
from scipy.integrate import quad
H=1/np.sqrt(3)
def Q(f,lo,hi):
    return quad(lambda t:np.real(f(t)),lo,hi,epsabs=2e-12)[0]+1j*quad(
        lambda t:np.imag(f(t)),lo,hi,epsabs=2e-12)[0]
def run(A,B,omega,lam,d,eta_e):
    e=lambda t,x:np.exp(-1j*omega*t+1j*lam*x)
    T=lambda t,x:A*t**3*e(t,x)
    U=lambda t,x:B*t**3*e(t,x)
    Td=lambda t,x:A*(3*t*t-1j*omega*t**3)*e(t,x)
    Ud=lambda t,x:B*(3*t*t-1j*omega*t**3)*e(t,x)
    Udd=lambda t,x:B*(6*t-6j*omega*t*t-omega**2*t**3)*e(t,x)
    phi=lambda t,x:-Td(t,x)-H*T(t,x)
    psi=lambda t,x:H*T(t,x)+1j*lam*U(t,x)
    v=lambda t,x:Ud(t,x)-1j*lam*T(t,x)
    vd=lambda t,x:Udd(t,x)-1j*lam*Td(t,x)
    acc=lambda t,x:-1j*lam*phi(t,x)+vd(t,x)+H*v(t,x)
    for t in (.13,.34,.57):
        assert abs(acc(t,d)-(Udd(t,d)+H*Ud(t,d)))<2e-12
    # Green geodesic with zero perturbative position/velocity at eta=0.
    def geoshift(t,x):
        return Q(lambda s:(1-np.exp(-H*(t-s)))/H*acc(s,x),0,t)
    assert abs(geoshift(eta_e+d,d)-U(eta_e+d,d))<2e-11
    assert abs(geoshift(eta_e+2*d,0)-U(eta_e+2*d,0))<2e-11
    out=Q(lambda s:-phi(eta_e+s,s)-psi(eta_e+s,s)-v(eta_e+s,s),0,d)
    back=Q(lambda s:-phi(eta_e+d+s,d-s)-psi(eta_e+d+s,d-s)
           +v(eta_e+d+s,d-s),0,d)
    mirrors=2*geoshift(eta_e+d,d)-geoshift(eta_e,0)-geoshift(eta_e+2*d,0)
    ae=np.exp(H*eta_e);ar=np.exp(H*(eta_e+2*d))
    clock=Q(lambda s:np.exp(H*s)*phi(s,0),eta_e,eta_e+2*d)
    Te=T(eta_e,0);Tr=T(eta_e+2*d,0)
    assert abs(out+back+mirrors-(Tr-Te))<2e-11
    assert abs(clock-(-ar*Tr+ae*Te))<2e-11
    # The fixed coordinate emission label is NOT the physical event!
    fixed_label=ar*(out+back+mirrors)+clock
    event_correction=(ar-ae)*Te
    physical=fixed_label+event_correction
    assert abs(physical)<2e-11
    if eta_e>0 and A!=0:assert abs(fixed_label)>1e-7
    return fixed_label,event_correction,physical
if __name__=="__main__":
    cases=[(.17,.12,1.1,.8,.23,0.),(.17,.12,1.1,.8,.23,.08),
           (.30,-.21,.6,1.3,.4,.2),(0.,.45,1.8,.4,.12,.08),
           (.10,0.,1.9,.9,.35,.2)]
    for c in cases:
        fixed,ev,full=run(*c)
        print("CASE",c,"fixed-coordinate",fixed,"physical-event term",ev,
              "invariant",full)
    # Full nine-arm local spatial-shift projections, five DIFFERENCES.
    K=np.array([2.,0.,1.]);n=K/np.sqrt(5.)
    ee=np.array([1.,0.,-2.])/np.sqrt(5.)
    b=np.array([0.,1.,0.])
    arms=[n,ee,b,(n+ee)/np.sqrt(2),(n-ee)/np.sqrt(2),
          (n+b)/np.sqrt(2),(n-b)/np.sqrt(2),
          (ee+b)/np.sqrt(2),(ee-b)/np.sqrt(2)]
    X=np.array([.12,-.06,.08]);A=.17;te=.08;d=.075
    fixed=[run(A,float(u@X),1.1,float(K@u),d,te)[0] for u in arms]
    pairs=[(0,1),(1,2),(3,4),(5,6),(7,8)]
    differences=np.array([fixed[i]-fixed[j] for i,j in pairs])
    assert np.max(abs(differences))<2e-11
    assert abs(fixed[0])>1e-8
    print("PASS five differential gauge nulls",differences)
    print("PASS independent FLRW photon/free-mirror/clock/event identities")
    print("SCOPE: pure gauge along arm, not complete K4 cosmological gauge proof")
