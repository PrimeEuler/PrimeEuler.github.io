#!/usr/bin/env python3
"""Gravity v15.1318: independently derive the vector metric Einstein tensor
and K4 offdiagonal stress, then close sourced momentum and yz equations.
Linearized on coasting FLRW; conditional on archived sourced vector Euler
and transverse Maxwell Ward. Not a complete 3D numerical metric solver.
"""
import sympy as s
t,z,k=s.symbols('t z k',positive=True,real=True)
v=s.Function('B')(t); f=s.Function('f')(t); flux=s.Function('F')(t); stress=s.Function('T')(t)
a=t/s.sqrt(3); w=s.exp(s.I*k*z)
coords=[t,s.Symbol('x'),s.Symbol('y'),z]
g=s.diag(-1,a*a,a*a,a*a); h=s.zeros(4); h[0,2]=h[2,0]=-a*v*w
gi=s.diag(-1,a**-2,a**-2,a**-2); dgi=-gi*h*gi
C={};dC={}
for i in range(4):
 for j in range(4):
  for l in range(4):
   X=lambda m:s.diff(g[m,l],coords[j])+s.diff(g[m,j],coords[l])-s.diff(g[j,l],coords[m])
   Y=lambda m:s.diff(h[m,l],coords[j])+s.diff(h[m,j],coords[l])-s.diff(h[j,l],coords[m])
   C[i,j,l]=s.simplify(sum(gi[i,m]*X(m)/2 for m in range(4)))
   dC[i,j,l]=s.simplify(sum((dgi[i,m]*X(m)+gi[i,m]*Y(m))/2 for m in range(4)))
R0=s.zeros(4);dR=s.zeros(4)
for i in range(4):
 for j in range(4):
  b=0; db=0
  for l in range(4):
   b+=s.diff(C[l,i,j],coords[l])-s.diff(C[l,i,l],coords[j])
   db+=s.diff(dC[l,i,j],coords[l])-s.diff(dC[l,i,l],coords[j])
   for m in range(4):
    b+=C[l,l,m]*C[m,i,j]-C[l,j,m]*C[m,i,l]
    db+=dC[l,l,m]*C[m,i,j]+C[l,l,m]*dC[m,i,j]-dC[l,j,m]*C[m,i,l]-C[l,j,m]*dC[m,i,l]
  R0[i,j]=s.simplify(b);dR[i,j]=s.simplify(db)
scalar=s.simplify(s.trace(gi*R0));dscalar=s.simplify(s.trace(gi*dR+dgi*R0))
G0=R0-g*scalar/2;dG=dR-h*scalar/2-g*dscalar/2
def mixed(i,j):
 return s.factor(sum(gi[i,m]*dG[m,j]+dgi[i,m]*G0[m,j] for m in range(4))/w)
g0y=s.sqrt(3)*k*k*v/(2*t)
gyz=s.sqrt(3)*s.I*k*(t*s.diff(v,t)+2*v)/(2*t*t)
assert s.simplify(mixed(0,2)-g0y)==0
assert s.simplify(mixed(2,3)-gyz)==0
assert s.simplify(scalar-6/t**2)==0
print('PASS direct Christoffel-to-Einstein vector 0y and yz')
# Original solid: F=C (det B)^1/3 (1+eta [tr B²/(tr B)²-1/3]).
b,coef,eta,eps,q=s.symbols('b C eta eps q',positive=True)
D=-s.I*k*q
B=s.Matrix([[b,0,0],[0,b,b*eps*D],[0,b*eps*D,b]])
tr=s.trace(B);tr2=s.trace(B*B);J=tr2/tr**2-s.Rational(1,3)
pot=coef*B.det()**s.Rational(1,3)*(1+eta*J)
grad=pot*(B.inv()/3+eta*(2*B/tr**2-2*tr2*s.eye(3)/tr**3)/(1+eta*J))
M=s.eye(3);M[1,2]=eps*D
Tmat=2*b*M.T*grad*M-pot*s.eye(3)
solidyz=s.factor(s.diff(Tmat[1,2],eps).subs(eps,0))
assert s.simplify(solidyz+4*s.I*eta*coef*b*k*q/9)==0
print('PASS solid action offdiagonal spatial stress')
den=4+3*k*k
V=4*t*s.diff(f,t)/(s.sqrt(3)*den)+18*flux/(t*t*den)
momsrc=3*s.sqrt(3)*flux/t**3+s.Rational(2,3)*(s.diff(f,t)-s.sqrt(3)*V/t)
assert s.simplify(g0y.subs(v,V)-momsrc)==0
fdot=-s.I*s.sqrt(3)*k*stress/t
fdd=-3*s.diff(f,t)/t-den*f/(2*t*t)-18*s.I*stress/(k*t**4)
Vdot=s.diff(V,t).subs({s.diff(f,t,2):fdd,s.diff(flux,t):fdot})
space=s.sqrt(3)*s.I*k*(t*Vdot+2*V)/(2*t*t)
spatialsrc=9*stress/t**4-s.I*k*f/t**2
assert s.simplify(space-spatialsrc)==0
print('PASS evolved vector Einstein 0y/y-z sourced equations')
print('OPEN TT sector, full metric, causally realized detector, continuum')
