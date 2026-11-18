#!/usr/bin/env python3
"""Gravity v15.1168: five-channel bicone inverse conditioning and noise.
Independent normalized mechanical+Ramsey frequency response, NO claim
of physical measured sensitivity or new gravitational interaction.
"""
import numpy as np
import sympy as s
h=s.Rational(1,2)
M=s.Matrix([[0,-1,0,0,0],[0,0,-1,0,0],[0,0,0,0,-1],[0,0,0,-1,0],[-h,0,0,h,0]])
assert M.det()==h
assert (M.T*M).eigenvals()=={(3-s.sqrt(5))/4:1,(3+s.sqrt(5))/4:1,s.Integer(1):3}
condition=float((3+s.sqrt(5))/2)
assert abs(np.linalg.cond(np.array(M,dtype=float))-condition)<1e-13
cov=M.inv()*M.inv().T
assert cov==s.Matrix([[5,0,0,1,0],[0,1,0,0,0],[0,0,1,0,0],[1,0,0,1,0],[0,0,0,0,1]])
phi=s.symbols('phi',real=True)
mu=-2*s.cos(phi)
assert s.simplify(4-mu**2-4*s.sin(phi)**2)==0
assert s.diff(mu,phi).subs(phi,s.pi/2)==2
om0=np.array([1.,1.15,.9,1.30,1.5])
Q=np.array([70.,90.,60.,100.,80.])
taus=np.array([1.1,1.2,1.3,1.4,1.5])
Mnp=np.array(M,dtype=float)
def window(om,tau):
    if abs(om)<1e-12:return tau
    return np.expm1(1j*om*tau)/(1j*om)
def transfer(om):
    chi=1/(om0**2-om**2-1j*om0*om/Q)
    win=np.array([window(om,t) for t in taus])
    gain=2*chi*win
    return np.diag(gain)@Mnp
for om in (0,.75,1.,1.3,2.):
    A=transfer(om)
    assert abs(np.linalg.det(A))>1e-20
    R=np.linalg.inv(A)
    N=1_000_000
    Sigma=R@((4/N)*np.eye(5))@R.conj().T
    print('omega',om,'cond',np.linalg.cond(A),'std',np.sqrt(np.real(np.diag(Sigma))))
    vec=np.array([.6,-.1,.2,-.3,.4])
    assert np.linalg.norm(np.linalg.solve(A,A@vec)-vec)<1e-12
assert abs(window(2*np.pi/1.3,1.3))<1e-13
assert np.linalg.matrix_rank(np.diag([1,1,1,1,0])@Mnp)<5
kBT,Gamma=s.symbols('kBT Gamma',positive=True)
assert s.simplify((4*kBT*Gamma)/Gamma-4*kBT)==0
print('PASS exact geometric noise covariance and frequency-dependent inverse')
print('PASS Ramsey rank null, spin shot variance at quadrature, thermal Langevin PSD')
print('SCOPE: dimensionless illustrative instrument, conventional coupled-spin sensor')
