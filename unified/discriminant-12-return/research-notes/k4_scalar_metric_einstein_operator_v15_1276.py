#!/usr/bin/env python3
"""Gravity v15.1276: derive scalar FLRW Einstein operators by direct
Christoffel/Ricci perturbation. Geometry only, not matter constraints."""
import sympy as s
t,z,k=s.symbols("t z k",real=True,positive=True)
phi=s.Function("Phi")(t); psi=s.Function("Psi")(t)
a=t/s.sqrt(3); w=s.exp(s.I*k*z)
coords=[t,s.Symbol("x"),s.Symbol("y"),z]
g=s.diag(-1,a*a,a*a,a*a)
h=s.diag(-2*phi*w,-2*a*a*psi*w,-2*a*a*psi*w,-2*a*a*psi*w)
gi=s.diag(-1,a**-2,a**-2,a**-2)
dgi=-gi*h*gi
simpl=lambda x:s.simplify(s.expand(x))
C={};dC={}
for i in range(4):
 for j in range(4):
  for l in range(4):
   C[i,j,l]=simpl(sum(gi[i,m]*(s.diff(g[m,l],coords[j])+s.diff(g[m,j],coords[l])-s.diff(g[j,l],coords[m]))/2 for m in range(4)))
   dC[i,j,l]=simpl(sum((dgi[i,m]*(s.diff(g[m,l],coords[j])+s.diff(g[m,j],coords[l])-s.diff(g[j,l],coords[m]))+gi[i,m]*(s.diff(h[m,l],coords[j])+s.diff(h[m,j],coords[l])-s.diff(h[j,l],coords[m])))/2 for m in range(4)))
def ricci(c):
 return s.Matrix(4,4,lambda i,j:simpl(sum(s.diff(c[l,i,j],coords[l])-s.diff(c[l,i,l],coords[j])+sum(c[l,l,m]*c[m,i,j]-c[l,j,m]*c[m,i,l] for m in range(4)) for l in range(4))))
r=ricci(C)
dr=s.Matrix(4,4,lambda i,j:simpl(sum(s.diff(dC[l,i,j],coords[l])-s.diff(dC[l,i,l],coords[j])+sum(dC[l,l,m]*C[m,i,j]+C[l,l,m]*dC[m,i,j]-dC[l,j,m]*C[m,i,l]-C[l,j,m]*dC[m,i,l] for m in range(4)) for l in range(4))))
R=simpl(sum(gi[i,j]*r[i,j] for i in range(4) for j in range(4)))
dR=simpl(sum(gi[i,j]*dr[i,j]+dgi[i,j]*r[i,j] for i in range(4) for j in range(4)))
Ein0=r-g*R/2
dEin=dr-h*R/2-g*dR/2
def mixed(i,j):
 return simpl(sum(gi[i,m]*dEin[m,j]+dgi[i,m]*Ein0[m,j] for m in range(4))/w)
common=t*t*s.diff(psi,t,2)+t*s.diff(phi,t)+3*t*s.diff(psi,t)+phi
targets={(0,0):6*(k*k*psi+t*s.diff(psi,t)+phi)/t**2,
         (0,3):-2*s.I*k*(t*s.diff(psi,t)+phi)/t,
         (3,3):2*common/t**2,
         (1,1):2*common/t**2+3*k*k*(psi-phi)/t**2,
         (1,2):s.Integer(0)}
assert s.simplify(R-6/t**2)==0
for ij,target in targets.items():
 found=mixed(*ij)
 assert s.simplify(found-target)==0,(ij,found-target)
 print(f"delta Gmixed {ij}: {s.factor(found)}",flush=True)
print("PASS scalar Einstein geometry 00,0z,zz,xx,xy")
print("OPEN coupled Maxwell+K4 constraints, vectors/tensors, time-dependent metric")
