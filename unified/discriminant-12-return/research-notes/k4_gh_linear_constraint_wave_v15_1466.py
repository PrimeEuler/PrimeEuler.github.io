#!/usr/bin/env python3
"""v15.1466 linear 3+1 generalized harmonic (GH) Einstein principal symbol,
gauge Ward and Fourier energy. NOT nonlinear Einstein-H2 simulation.
"""
import sympy as s
import numpy as np
w,k=s.symbols('w k',positive=True,real=True)
eta=s.diag(-1,1,1,1)
p=s.Matrix([-w,0,0,k]);pu=eta*p
xi=s.Matrix([s.Rational(1,3),2,-1,s.Rational(5,4)])
q=(p.T*eta*xi)[0]
barh=s.Matrix(4,4,lambda i,j:p[i]*xi[j]+p[j]*xi[i]-eta[i,j]*q)
C=s.simplify(barh*pu)
assert all(s.simplify(C[j]-(p.T*eta*p)[0]*xi[j])==0 for j in range(4))
assert all(s.simplify(C[j].subs(w,k))==0 for j in range(4))
TT=s.zeros(4);TT[1,1]=s.Rational(2,3);TT[2,2]=-s.Rational(2,3)
assert TT*pu==s.zeros(4,1)
P=s.Matrix([[0,k],[-k,0]])
assert P.T+P==s.zeros(2)
assert s.simplify(P*P+k*k*s.eye(2))==s.zeros(2)
N=24;z=np.arange(N)*2*np.pi/N
modes=np.fft.fftfreq(N,d=1/N)
f=np.sin(z)+.32*np.cos(3*z);F=np.fft.fft(f)
for t in [0,.3,1.7,3.]:
 ff=F*np.exp(-1j*modes*t)
 ft=np.fft.ifft(-1j*modes*ff).real
 fz=np.fft.ifft(1j*modes*ff).real
 assert np.max(abs(ft+fz))<2e-14
 energy=np.mean(ft*ft+fz*fz)
 assert abs(energy-(1+9*.32**2))<2e-14
 print('t=',t,'norm=',energy)
print('PASS GH linear gauge-null modes, diagonalisable wave principal symbol, conserved Fourier wave energy')
print('OPEN nonlinear Einstein-H2 metric evolution and covariant Weyl-Maxwell coupling')
