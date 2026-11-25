#!/usr/bin/env python3
"""Gravity v15.1477: exact nonlinear harmonic 4D Einstein-H2 sigma
and independent nonzero Weyl pp wave, no Maxwell-area excitation.
Metric (w,z,x,y): ds²=-2dw dz+H(w,x,y)dw²+dx²+dy².
"""
import sympy as s
w,z,x,y=s.symbols("w z x y",real=True)
a,e,kappa=s.symbols("a e kappa",real=True)
coords=[w,z,x,y];f=a*s.sin(w);df=s.diff(f,w)
H=-kappa*df**2*(x*x+y*y)/2+e*s.cos(w)*(x*x-y*y)
g=s.Matrix([[H,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
inv=s.Matrix([[0,-1,0,0],[-1,-H,0,0],[0,0,1,0],[0,0,0,1]])
assert g*inv==s.eye(4) and g.det()==-1
contracted=[s.simplify(-sum(s.diff(inv[i,j],coords[j]) for j in range(4))) for i in range(4)]
assert contracted==[0,0,0,0]
Gamma={}
for r in range(4):
 for m in range(4):
  for n in range(m,4):
   val=s.simplify(sum(inv[r,l]*(s.diff(g[l,n],coords[m])+s.diff(g[l,m],coords[n])-s.diff(g[m,n],coords[l])) for l in range(4))/2)
   if val!=0:Gamma[r,m,n]=val
assert set(Gamma)=={(1,0,0),(1,0,2),(1,0,3),(2,0,0),(3,0,0)}
assert s.simplify(Gamma[1,0,0]+s.diff(H,w)/2)==0
assert s.simplify(Gamma[1,0,2]+s.diff(H,x)/2)==0
assert s.simplify(Gamma[2,0,0]+s.diff(H,x)/2)==0
G=lambda i,j,k:Gamma.get((i,min(j,k),max(j,k)),s.Integer(0))
Ric=s.zeros(4)
for m in range(4):
 for n in range(4):
  expr=0
  for q in range(4):
   expr+=s.diff(G(q,m,n),coords[q])-s.diff(G(q,m,q),coords[n])
   for p in range(4):
    expr+=G(q,m,n)*G(p,q,p)-G(q,m,p)*G(p,n,q)
  Ric[m,n]=s.trigsimp(s.simplify(expr))
assert Ric[0,0]==s.simplify(-s.diff(H,x,2)/2-s.diff(H,y,2)/2)
assert Ric[0,0]==kappa*df**2
assert all(Ric[i,j]==0 for i in range(4) for j in range(4) if (i,j)!=(0,0))
assert s.simplify(s.trace(inv*Ric))==0
u=s.sinh(f);du=s.diff(u,w)
assert s.simplify(du**2/(1+u**2)-df**2)==0
boxu=s.simplify(sum(s.diff(inv[i,j]*s.diff(u,coords[j]),coords[i]) for i in range(4) for j in range(4)))
assert boxu==0
Cwx=s.trigsimp(-s.diff(H,x,2)/2-Ric[0,0]/2)
Cwy=s.trigsimp(-s.diff(H,y,2)/2-Ric[0,0]/2)
assert s.simplify(Cwx+e*s.cos(w))==0
assert s.simplify(Cwy-e*s.cos(w))==0
print("PASS harmonic gauge, Einstein-H2 sigma EOM, Ricci, and independent nonzero Weyl")
for ww in (0,s.pi/3):
 vals={a:s.Rational(3,25),e:s.Rational(1,50),kappa:s.Rational(3,1000),w:ww,x:s.Rational(1,4),y:s.Rational(1,5)}
 print("sample",ww,"Ric_ww",float(Ric[0,0].subs(vals)),"C_wxwx",float(Cwx.subs(vals)),"H",float(H.subs(vals)))
print("NEGATIVE area pullback B=0 since second H2 coordinate is constant; no EM conversion")
print("OPEN 3D GH constrained numerical evolution and full Weyl-Maxwell coupling")
