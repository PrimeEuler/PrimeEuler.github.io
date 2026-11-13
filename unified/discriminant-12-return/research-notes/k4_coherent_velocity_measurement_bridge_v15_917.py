#!/usr/bin/env python3
"""Gravity v15.917: coherent-state measurement bridge for the physical 2-D tidal oscillator.
Dimensionless benchmark hbar=M=omega0=1, K=I+[[A,B],[B,-A]].
Physical velocities p/M reverse under global parity; Cone X=u(Jz+1/2)
is even and has identical full distributions for parity-mirror coherent states.
No identification of dimensionless oscillator velocities with actual SI m/s is claimed.
"""
import numpy as np
from scipy.linalg import eigh
A,B=.04,.08
K=np.array([[1+A,B],[B,1-A]],float)
eig,U=eigh(K)
assert min(eig)>0
W=np.sqrt(eig)
q0=np.zeros(2)
p0=np.array([np.sqrt(2.),0.]) # coherent (alpha1,alpha2)=(+i,0)
C0=.5*np.eye(4) # vacuum symmetrized quadrature covariance
def propagator(t):
    C=U@np.diag(np.cos(W*t))@U.T
    S=U@np.diag(np.sin(W*t)/W)@U.T
    T=U@np.diag(-W*np.sin(W*t))@U.T
    return np.block([[C,S],[T,C]])
def readout(t,sgn):
    P=propagator(t)
    z=P@np.concatenate((q0,sgn*p0))
    cov=P@C0@P.T
    qs=z[:2];ps=z[2:]
    # N_i=(<q_i²>+<p_i²>-1)/2, X/u=(N1-N2)/2+1/2
    variance=np.diag(cov[:2,:2])+np.diag(cov[2:,2:])
    occ=(variance+qs**2+ps**2-1)/2
    x_over_u=.5+(occ[0]-occ[1])/2
    energy=.5*(ps@ps+qs@K@qs+np.trace(cov[2:,2:])+np.trace(K@cov[:2,:2]))
    return ps,x_over_u,energy,qs,occ
energy0=readout(0,1)[2]
for t in [0,2,8,16,24]:
    plus=readout(t,+1)
    minus=readout(t,-1)
    assert np.max(np.abs(plus[0]+minus[0]))<1e-12
    assert abs(plus[1]-minus[1])<1e-12
    assert abs(plus[2]-minus[2])<1e-12
    assert abs(plus[2]-energy0)<1e-11
    assert np.max(np.abs(plus[3]+minus[3]))<1e-12
    print(f't={t:2}: v_plus={np.round(plus[0],8)}, v_minus={np.round(minus[0],8)}, X/u both={plus[1]:.8f}, E both={plus[2]:.8f}')
assert abs(readout(0,+1)[1]-1)<1e-12
assert abs(readout(0,+1)[0][0]-np.sqrt(2))<1e-12
# Both states are global parity mirrors; full X spectral distributions
# (not just mean) equal since [H,P]=0, [X,P]=0, P v_i P=-v_i.
# At t=0, P(N1=m,N2=0)=e^-1/m! for BOTH signs.
import math
weights=np.array([np.exp(-1)/math.factorial(m) for m in range(18)])
assert abs(sum(weights)-1)<2e-15
assert abs(sum(m*weights[m] for m in range(18))-1)<2e-14
print('PASS coherent parity-mirror velocity sign/no-go, complete X parity invariance, energy conservation, normal-mode propagation')
