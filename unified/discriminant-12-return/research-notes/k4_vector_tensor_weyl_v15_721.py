#!/usr/bin/env python3
"""v15.721: local conformal vector/tensor Weyl and coasting K4 source response.
Source Q is a component of the conserved tilted tracefree Fourier stress
of v15.716. Vector is source-first using the v14.935 vector action.
Tensor response uses the v14.928 EH+solid TT quadratic action.
A stationary conformal-vector particular response has zero electric,
but nonzero magnetic, Weyl. Not a global detector forecast.
"""
import sympy as s
k,t,eta,kappa=s.symbols("k tau eta kappa",positive=True,real=True)
Q=s.symbols("Q",nonzero=True)
a=t/s.sqrt(3);D=4+3*k*k
K=2*t**3*k*k/(3*s.sqrt(3)*D)
G=4*t*eta*k*k/(9*s.sqrt(3))
b=4*t/(s.sqrt(3)*D)
A=t*D/(6*s.sqrt(3))
J=s.I*k*t*Q/6
assert s.simplify(G/K-2*eta*D/(3*t*t))==0
f0=-3*s.I*Q/(eta*k*D)
assert s.simplify(G*f0+s.diff(b*J,t))==0
B0=s.factor(-J/A)
assert s.simplify(B0+s.I*s.sqrt(3)*k*Q/D)==0
w,V=s.symbols("omega V",real=True)
g=s.diag(1,-1,-1,-1)
q=s.Matrix([-w,0,0,k]);h=s.zeros(4);h[0,2]=h[2,0]=V
def R(a,b,c,d):
    return s.expand((-q[b]*q[c]*h[a,d]-q[a]*q[d]*h[b,c]
      +q[a]*q[c]*h[b,d]+q[b]*q[d]*h[a,c])/2)
def W(a,b,c,d):
    Ric=s.Matrix(4,4,lambda i,j:s.expand(sum(g[m,m]*R(m,i,m,j)
                                  for m in range(4))))
    Sc=s.expand(sum(g[m,m]*Ric[m,m] for m in range(4)))
    return s.expand(R(a,b,c,d)-s.Rational(1,2)*(
      g[a,c]*Ric[d,b]-g[a,d]*Ric[c,b]-g[b,c]*Ric[d,a]+g[b,d]*Ric[c,a])
      +Sc/6*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
assert s.simplify(W(0,2,0,3)-k*w*V/4)==0
assert s.simplify(W(0,3,2,3)-k*k*V/4)==0
assert s.diff(B0,t)==0
assert s.simplify(-k*k*B0/(4*a*a))!=0
# Tensor mode Lgamma=-2 kappa Pi_T with Pi_T=Q/t².
mcoef=3*k*k+8*eta/3
Tpart=s.factor(-2*kappa*Q/mcoef)
assert s.simplify(mcoef*Tpart+2*kappa*Q)==0
h=s.zeros(4);h[1,1]=-V;h[2,2]=V
assert s.simplify(W(0,1,0,1)+(k*k+w*w)*V/4)==0
assert s.simplify(W(0,2,0,2)-(k*k+w*w)*V/4)==0
print("PASS: K4 sourced vector pole and constant particular response")
print("PASS: electric vector Weyl zero for constant conformal shift, magnetic nonzero")
print("PASS: source-driven K4 tensor particular and TT Weyl")
print("B_vector=",B0,"f_vector=",f0,"gamma_T=",Tpart)
