#!/usr/bin/env python3
"""Gravity v15.879: distinguish Gertsenshtein phase transfer vs phase locking.

The frozen ordinary Einstein-Maxwell four-channel WKB Hamiltonian is
Hermitian. In the uniform equal-photon-dispersion limit, its photon
transfer map T(z) is a complex scalar times a REAL orthogonal polarization
rotation: T dagger T=P(z) I. It transmits the source phase, but cannot
select or attract an initially unspecified phase. Any polarization sign
is basis-convention dependent; physical Stokes parameters covary.

For a varying B orientation and unequal photon refractive indices, the
full 4-vector still propagates unitarily; incoming-state overlaps
and norms remain invariant, so there is no closed lossless global
phase attractor. Conditional photon-only states can filter phases
without violating this statement, and are not themselves a lock.

Distinct positive control: a PHYSICAL sign-reversing B(z) field with
period selected by the externally supplied photon/graviton detuning
can quasi-phase-match conversion. In a detuned case with integral
multiple full beat lengths, uniform-field conversion nearly cancels,
while the sign-reversed field coherently accumulates signal. This is
standard externally selected wave-mixing, NOT a Cone mesh law.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

def H(mu,delta,theta,split=0):
    c=mu*np.array([[np.sin(theta),-np.cos(theta)],
                    [np.cos(theta),np.sin(theta)]])
    out=np.zeros((4,4))
    out[:2,:2]=np.diag([delta+split/2,delta-split/2])
    out[:2,2:]=c
    out[2:,:2]=c.T
    assert np.max(abs(out-out.T))<1e-14
    return out

def stokes(z):
    z=z/np.linalg.norm(z)
    return np.array([abs(z[0])**2-abs(z[1])**2,
       2*np.real(np.conj(z[0])*z[1]),2*np.imag(np.conj(z[0])*z[1])])

mu,delta,length,angle=.083,.14,14.,.31
U=expm(-1j*H(mu,delta,angle)*length)
T=U[:2,2:]
P=np.trace(T.conj().T@T).real/2
assert np.linalg.norm(T.conj().T@T-P*np.eye(2))<1e-13
assert abs(P-.582856549)<2e-9
for phase in np.linspace(-2.7,2.7,11):
    v=np.array([1,np.exp(1j*phase)])/np.sqrt(2)
    output=T@v
    # Real rotation induced by external B: normalized photon Stokes
    # is exactly the rotated incoming gravitational polarization.
    rot=np.array([[np.sin(angle),-np.cos(angle)],
                  [np.cos(angle),np.sin(angle)]])
    assert np.linalg.norm(stokes(output)-stokes(rot@v))<1e-12
    assert abs(np.vdot(output,output).real-P)<1e-12
# A small phase error is not attracted to the quarter-turn phase:
# normalized transferred doublet distances remain unchanged.
for perturb in (.01,.001,.0001):
    a=np.array([1,1j])/np.sqrt(2)
    b=np.array([1,1j*np.exp(1j*perturb)])/np.sqrt(2)
    assert abs(np.linalg.norm(T@(a-b))/np.linalg.norm(a-b)
               -np.sqrt(P))<1e-12
    ia=np.r_[np.zeros(2,complex),a]
    ib=np.r_[np.zeros(2,complex),b]
    assert abs(np.vdot(U@ia,U@ib)-np.vdot(ia,ib))<1e-12

def varying_H(z):
    return H(.083*(1+.32*np.sin(z/3)),.14+.06*np.sin(z/4),
             .31+.6*np.sin(z/5),.03*np.sin(z/2))
def complex_rhs(z,y):
    a=y[:4]+1j*y[4:]
    b=-1j*varying_H(z)@a
    return np.r_[b.real,b.imag]
def propagate(v):
    res=solve_ivp(complex_rhs,(0.,25.),np.r_[v.real,v.imag],
                  rtol=1e-11,atol=2e-13,method='DOP853')
    assert res.success
    return res.y[:4,-1]+1j*res.y[4:,-1]
a=np.array([0,0,1,1j],complex)/np.sqrt(2)
b=np.array([0,0,1,1j*np.exp(.1j)],complex)/np.sqrt(2)
ua,ub=propagate(a),propagate(b)
assert abs(np.vdot(ua,ub)-np.vdot(a,b))<3e-10
assert abs(np.vdot(ua,ua).real-1)<3e-10
assert abs(np.vdot(ub,ub).real-1)<3e-10
# Positive quasi-phase matching control: physical B sign switches.
# detuning delta=0.8; L=8*pi/delta = four full beat wavelengths.
# Choose B(z) sign(cos(delta*z)) to make the Born mixing integrand
# mu(z)*exp(i delta z) add instead of cancel.
m=.002;d=.8;L=8*np.pi/d
N=1000
dz=L/N
W=np.eye(2,dtype=complex)
for j in range(N):
    z=(j+.5)*dz
    sign=1 if np.cos(d*z)>=0 else -1
    step=np.array([[d,m*sign],[m*sign,0]],float)
    W=expm(-1j*step*dz)@W
uniform=expm(-1j*np.array([[d,m],[m,0]])*L)
P_qpm=abs(W[0,1])**2
P_uniform=abs(uniform[0,1])**2
P_born=(m*(2/np.pi)*L)**2
assert abs(P_qpm/P_born-1)<.02
assert P_qpm>100*P_uniform
assert np.linalg.norm(W.conj().T@W-np.eye(2))<3e-11
print('PASS uniform mixing transfers phase without a quarter-phase attractor')
print('PASS nonuniform Hermitian model preserves full-state inner products')
print('P uniform',P_uniform,'P real-B-flip',P_qpm,
      'weak-mixing analytic QPM',P_born)
print('PASS externally prescribed B sign flips quasi-phase-match conversion')
print('NEGATIVE no action-derived Cone EM-half/G-quarter phase selector')
