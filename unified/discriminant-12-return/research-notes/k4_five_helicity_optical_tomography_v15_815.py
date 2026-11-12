#!/usr/bin/env python3
"""v15.815: five-helicity local tidal and FLRW optical detector tomography.
9 arms, 5 differential readouts, 5 independent metric polarizations:
S, V_e, V_b, T_plus, T_cross.
This is conventional supplied metric response, not Cone-specific dynamics.
"""
import sympy as s
import numpy as np
from scipy.integrate import quad
n=s.Matrix([2/s.sqrt(5),0,1/s.sqrt(5)])
e=s.Matrix([1/s.sqrt(5),0,-2/s.sqrt(5)])
b=s.Matrix([0,1,0])
P=lambda u:u*u.T
pol=[n*n.T-s.eye(3)/3,n*e.T+e*n.T,n*b.T+b*n.T,
     e*e.T-b*b.T,e*b.T+b*e.T]
arms=[n,e,b,(n+e)/s.sqrt(2),(n-e)/s.sqrt(2),
      (n+b)/s.sqrt(2),(n-b)/s.sqrt(2),
      (e+b)/s.sqrt(2),(e-b)/s.sqrt(2)]
pairs=[(0,1),(1,2),(3,4),(5,6),(7,8)]
local=s.Matrix([[s.simplify(s.trace((P(arms[i])-P(arms[j]))*p))
    for p in pol]for i,j in pairs])
expect=s.Matrix([[1,0,0,-1,0],[0,0,0,2,0],
    [0,2,0,0,0],[0,0,2,0,0],[0,0,0,0,2]])
assert local==expect and local.det()==16
assert local.inv()*local==s.eye(5)
print("PASS exact 5-helicity local Fermi projector matrix, det=16")
vectors=[np.array(v,float).ravel() for v in (n,e,b)]
nk,ek,bk=vectors
arm=[np.array(u,float).ravel() for u in arms]
K=np.sqrt(5)*nk
h=1/np.sqrt(3);a0=1/np.sqrt(3)
def F(z):return np.exp(1j*z/2)*np.sinc(z/(2*np.pi))
def J(t,w):
    return ((1-np.exp(-1j*w*t))/(1j*w)-
       (np.exp(-1j*w*t)-np.exp(-h*t))/(h-1j*w))/h
def comp(u,j):
    E=float(np.dot(ek,u));B=float(np.dot(bk,u))
    if j==0:return 1.,.4,0.,0.
    if j==1:return 0.,0.,E,0.
    if j==2:return 0.,0.,B,0.
    if j==3:return 0.,0.,0.,E**2-B**2
    return 0.,0.,0.,2*E*B
def harmonic(u,j,w=1.2,d=.13):
    lam=np.dot(K,u);phi,psi,v,tt=comp(u,j)
    x=w*d;y=lam*d
    O=d*(-phi-psi-v+tt/2)*F(y-x)
    I=d*(-phi-psi+v+tt/2)*np.exp(1j*(y-x))*F(-y-x)
    accel=-1j*lam*phi+(-1j*w+h)*v
    M=accel*(2*np.exp(1j*y)*J(d,w)-J(2*d,w))
    C=a0*phi*(np.exp((h-1j*w)*2*d)-1)/(h-1j*w)
    return a0*np.exp(2*h*d)*(O+I+M)+C
def integrate(fn,lo,hi):
    return quad(lambda t:np.real(fn(t)),lo,hi,epsabs=2e-11)[0]+1j*quad(
      lambda t:np.imag(fn(t)),lo,hi,epsabs=2e-11)[0]
def independent(u,j,w=1.2,d=.13):
    lam=np.dot(K,u);phi,psi,v,tt=comp(u,j)
    O=integrate(lambda z:(-phi-psi-v+tt/2)*np.exp(1j*(lam-w)*z),0,d)
    I=integrate(lambda z:(-phi-psi+v+tt/2)*np.exp(
        1j*(lam-w)*d-1j*(lam+w)*z),0,d)
    accel=-1j*lam*phi+(-1j*w+h)*v
    def shift(t):
        return integrate(lambda z:accel*(1-np.exp(-h*(t-z)))/h*
                         np.exp(-1j*w*z),0,t)
    M=2*np.exp(1j*lam*d)*shift(d)-shift(2*d)
    C=integrate(lambda z:a0*phi*np.exp((h-1j*w)*z),0,2*d)
    return a0*np.exp(2*h*d)*(O+I+M)+C
A=np.array([[harmonic(u,j) for j in range(5)] for u in arm])
Ai=np.array([[independent(u,j) for j in range(5)] for u in arm])
assert np.max(abs(A-Ai))<3e-12
D=np.zeros((5,9))
for row,(i,j) in enumerate(pairs):D[row,i]=1;D[row,j]=-1
M=D@A
sv=np.linalg.svd(M)[1]
assert sv[-1]>1e-3 and np.linalg.matrix_rank(M)==5
assert np.max(abs(np.linalg.inv(M)@M-np.eye(5)))<2e-13
for i,j in [(2,0),(2,3),(2,4),(3,0),(3,3),(3,4),
             (4,0),(4,3)]:
    assert abs(M[i,j])<1e-12
assert abs(M[1,1])>1e-4 and abs(M[1,2])>1e-4
print("PASS causal free-mirror photon path & proper clock against 45 independent quadratures")
print("FINARM_MATRIX",M.tolist())
print("SINGULAR_VALUES",sv.tolist())
print("DETERMINANT",np.linalg.det(M))
print("PASS: full rank, exact symmetry nulls and finite-arm transverse-vector mixing")
print("SCOPE: supplied harmonic metric, not sourced K4 extra helicities or new Cone physics")
