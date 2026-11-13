#!/usr/bin/env python3
"""Gravity v15.880 — Can EM/G half/quarter lattice fix physical QPM scale?

Exact weak-coupling Fourier coefficient of sign[cos(2pi*z/Lambda)]
versus mismatch Delta. Tests physical length selector, harmonic leakage,
and four-period exact two-state unitary comparison with Born limit.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

h,j=sp.symbols('h j',positive=True)
assert sp.simplify((h*(j+sp.Rational(1,2)))**2-(h/2)**2-h*h*j*(j+1))==0
assert sp.simplify((h*h/4).subs(h,1)-sp.Rational(1,4))==0
assert sp.simplify((h*h/4).subs(h,sp.Rational(1,2))-sp.Rational(1,16))==0
Nperiods=4
L=2*math.pi*Nperiods
cuts=np.array([0.]+[math.pi/2+n*math.pi for n in range(2*Nperiods)]+[L])
assert all(np.diff(cuts)>0)
def integral(delta):
    ans=0j
    for a,b in zip(cuts[:-1],cuts[1:]):
        sign=1 if math.cos((a+b)/2)>0 else -1
        ans+=sign*(np.exp(1j*delta*b)-np.exp(1j*delta*a))/(1j*delta) if abs(delta)>1e-12 else sign*(b-a)
    return ans
for n in (1,3,5,7):
    got=integral(n)/L
    target=2*(-1)**((n-1)//2)/(math.pi*n)
    assert abs(got-target)<1e-13,(n,got,target)
for n in (0.5,1.5,2,4,6):
    assert abs(integral(n)/L)<1e-13
def normalized_amplitude(delta,lambda0):
    return integral(delta*lambda0/(2*math.pi))/L
assert abs(normalized_amplitude(1,2*math.pi)-normalized_amplitude(2,math.pi))<1e-13
assert abs(normalized_amplitude(1,2*math.pi))>0.6
assert abs(normalized_amplitude(1,math.pi))<1e-13
def matrix_transfer(delta,mu):
    U=np.eye(2,dtype=complex)
    for a,b in zip(cuts[:-1],cuts[1:]):
        sign=1 if math.cos((a+b)/2)>0 else -1
        U=expm(-1j*np.array([[delta,mu*sign],[mu*sign,0]])*(b-a))@U
    assert np.linalg.norm(U.conj().T@U-np.eye(2))<1e-12
    return abs(U[0,1])**2
for delta in (1.,3.):
    mu=1e-4
    exact=matrix_transfer(delta,mu)
    approx=(mu*abs(integral(delta)))**2
    assert abs(exact/approx-1)<1e-5,(delta,exact,approx)
    print('delta',delta,'normalized amplitude',integral(delta)/L,
          'normalized intensity',abs(integral(delta)/L)**2,
          'full P',exact,'Born P',approx)
for delta in (.5,1.5,2.,5.):
    print('delta',delta,'normalized intensity',abs(integral(delta)/L)**2)
print('PASS squared half-step EM=1/4 G=1/16 distinct')
print('PASS QPM Fourier odd harmonics and even-harmonic null')
print('PASS rescaling invariance Delta Lambda and exact unitary weak mixing')
print('NEGATIVE mesh h_EM/h_G ratio fixes NO absolute Lambda or Delta')
