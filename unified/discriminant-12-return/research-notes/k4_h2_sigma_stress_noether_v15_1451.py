#!/usr/bin/env python3
"""v15.1451: exact Noether/Bianchi stress identity for curved H2 sigma
crossed null waves, showing fifth-order sigma EOM residual implies
nonzero local divergence of free sigma stress.
Does NOT include full C F B or metric-variation stress.
"""
import sympy as s
A,B,a,b=s.symbols("A B a b",real=True)
phi=[a*s.sin(A),b*s.sin(B)]
D=1+sum(z*z for z in phi)
G=s.eye(2)-s.Matrix(phi)*s.Matrix(phi).T/D
def partial(z):return s.Matrix([s.diff(z,A)+s.diff(z,B),-s.diff(z,A),-s.diff(z,B)])
grad=[partial(z) for z in phi];sgn=[-1,1,1]
kin=s.factor(sum(G[i,j]*sum(sgn[m]*grad[i][m]*grad[j][m] for m in range(3))
   for i in range(2) for j in range(2)))
E=[s.factor(-2*s.diff(phi[i],A,B)-phi[i]*kin) for i in range(2)]
T=s.zeros(3)
for mu in range(3):
 for nu in range(3):
  T[mu,nu]=s.factor(sum(G[i,j]*sgn[mu]*grad[i][mu]*grad[j][nu]
   for i in range(2) for j in range(2))-(kin/2 if mu==nu else 0))
derivs=[lambda z:s.diff(z,A)+s.diff(z,B),
        lambda z:-s.diff(z,A),lambda z:-s.diff(z,B)]
for nu in range(3):
 divergence=s.factor(sum(derivs[mu](T[mu,nu]) for mu in range(3)))
 expected=s.factor(sum(G[i,j]*E[i]*grad[j][nu] for i in range(2) for j in range(2)))
 assert s.simplify(divergence-expected)==0
 print("nu",nu,"divT",divergence,flush=True)
print("PASS exact sigma stress Noether identity div T = G_AB E^A partial_nu phi^B")
print("NEGATIVE crossed leading sigma data are not an exact conserved source before nonlinear EOM correction")
print("OPEN full Einstein-Weyl-Maxwell-sigma stress including metric dependence of C F B")
