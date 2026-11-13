#!/usr/bin/env python3
"""Gravity v15.877: standard Einstein-Maxwell Gertsenshtein mixing baseline.

Linearized Maxwell cross stress for B=(Bx,By,0) and plane-wave
E=(Ex,Ey,0), b_wave=z cross E=(-Ey,Ex,0) gives:
  T_plus=Bx*Ey+By*Ex, T_cross=-Bx*Ex+By*Ey.
With canonical normalized WKB photon/graviton amplitudes
(Ax,Ay,hplus,hcross) and transverse magnetic orientation theta:
 H=[ Delta I_2, C ; C.T, 0 ],
 C=mu [[sin theta,-cos theta],[cos theta,sin theta]].
C.T*C=mu² I, yielding two identical ordinary 2x2 mixing channels.
Test conversion P=(4mu²/(Delta²+4mu²))
 *sin²[L sqrt(Delta²+4mu²)/2].
Mesh labels 1/2 and 1/4 are not inserted as couplings. They can
label input phase, not change the total uniform-field probability.
Scope: weak background field, homogeneous WKB and unitary 4-channel
propagation; nonuniform control retains Hermitian Hamiltonian.
NOT a full backreacted K4+Maxwell gravitational initial-value solution.
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
Bx,By,Ex,Ey=sp.symbols('Bx By Ex Ey',real=True)
B=sp.Matrix([Bx,By,0]); bw=sp.Matrix([-Ey,Ex,0])
S=-(B*bw.T+bw*B.T)+sp.eye(3)*(B.dot(bw))
assert sp.simplify((S[0,0]-S[1,1])/2-(Bx*Ey+By*Ex))==0
assert sp.simplify(S[0,1]+Bx*Ex-By*Ey)==0
mu,theta=sp.symbols('mu theta',real=True)
C=mu*sp.Matrix([[sp.sin(theta),-sp.cos(theta)],
                [sp.cos(theta),sp.sin(theta)]])
assert (C.T*C-mu**2*sp.eye(2)).applyfunc(sp.trigsimp)==sp.zeros(2)
assert (C.subs(theta,0)-mu*sp.Matrix([[0,-1],[1,0]])).applyfunc(
   sp.simplify)==sp.zeros(2)
def H(mu0,d,angle):
    c=mu0*np.array([[np.sin(angle),-np.cos(angle)],
                    [np.cos(angle),np.sin(angle)]])
    out=np.zeros((4,4));out[:2,:2]=d*np.eye(2)
    out[:2,2:]=c;out[2:,:2]=c.T
    return out
def probability(mu0,d,length):
    v=np.sqrt(4*mu0**2+d**2)
    return 4*mu0**2/v**2*np.sin(length*v/2)**2
for angle in [0,np.pi/8,np.pi/4,np.pi/2]:
    for shift in [0,np.pi/4,np.pi/2]:
        for detune in [0,.14,.6]:
            initial=np.array([0,0,np.cos(shift),np.sin(shift)],complex)
            out=expm(-1j*H(.083,detune,angle)*14)@initial
            assert abs(np.vdot(out[:2],out[:2]).real-
                       probability(.083,detune,14))<2e-14
            assert abs(np.vdot(out,out).real-1)<2e-14
for shift in [0,np.pi/4,np.pi/2]:
    initial=np.array([0,0,1,np.exp(1j*shift)],complex)/np.sqrt(2)
    out=expm(-1j*H(.083,.14,.3)*14)@initial
    assert abs(np.vdot(out[:2],out[:2]).real-
               probability(.083,.14,14))<2e-14
assert abs(probability(.083,0,np.pi/(2*.083))-1)<2e-14
for d in [.2,1.2]:
    approx=(1e-5*7.8)**2*np.sinc(d*7.8/(2*np.pi))**2
    assert abs(probability(1e-5,d,7.8)-approx)<1e-13
def Hz(z):
    return H(.07*(1+.2*np.sin(z/2)),.13+.04*np.cos(z/3),
             .3*np.sin(z/4))
def ode(z,y):
    a=y[:4]+1j*y[4:]
    b=-1j*Hz(z)@a
    return np.r_[b.real,b.imag]
init=np.array([0,0,1/np.sqrt(2),1j/np.sqrt(2)],complex)
sol=solve_ivp(ode,[0,17],np.r_[init.real,init.imag],
    method='DOP853',rtol=1e-11,atol=2e-13)
assert sol.success
z=sol.y[:4,-1]+1j*sol.y[4:,-1]
assert abs(np.vdot(z,z).real-1)<2e-10
print('PASS Maxwell stress polarization map')
print('PASS two-channel mixing and phase-independent total conversion')
print('PASS no detuning resonance and weak-mixing sinc')
print('PASS path-ordered nonuniform mixing energy conservation')
print('Example P(.083,.14,14)=',probability(.083,.14,14))
print('NEGATIVE no EM 1/2 or gravity 1/4 selection of mu,Delta,L')
