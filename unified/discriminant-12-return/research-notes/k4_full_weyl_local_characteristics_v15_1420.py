#!/usr/bin/env python3
"""v15.1420: exact full 4D vacuum TT Weyl local principal test.
Frozen linearized vacuum curvature; at H2 apex grad_y(v)=s,
fluctuations A_y(t,x) and u(t,x) have local interaction
L_int=+g epsilon s A_t u_t, and speeds (1 +/- g eps s)^(-1/2).
Not a self-consistent Einstein-H2-Maxwell solution or causal front.
"""
import sympy as S
eta=S.diag(-1,1,1,1)
h=S.diag(0,1,-1,0); k=S.Matrix([-1,0,0,1])
R={};C={}
for i in range(4):
 for j in range(4):
  for a in range(4):
   for b in range(4):
    value=S.expand((-k[a]*k[j]*h[i,b]-k[b]*k[i]*h[j,a]+k[b]*k[j]*h[i,a]+k[a]*k[i]*h[j,b])/2)
    R[i,j,a,b]=value
    C[i,j,a,b]=value*eta[i,i]*eta[j,j]*eta[a,a]*eta[b,b]
for i in range(4):
 for j in range(4):
  assert S.simplify(sum(eta[a,a]*R[a,i,a,j] for a in range(4)))==0
assert (C[0,2,0,2],C[0,2,1,2],C[1,2,1,2])==(-S.Rational(1,2),0,0)
omega,q,g,epsilon,s=S.symbols("omega q g epsilon s",real=True)
p=S.Matrix([-omega,q,0,0])
M=S.Matrix([S.factor(sum(C[a,nu,b,2]*p[a]*p[b] for a in range(4) for b in range(4))) for nu in range(4)])
assert M==S.Matrix([0,0,-omega**2/2,0])
z=g*epsilon*s;K=S.Matrix([[1,z],[z,1]])
det=S.factor((omega**2*K-q*q*S.eye(2)).det())
assert S.simplify(det-(omega**2*(1+z)-q*q)*(omega**2*(1-z)-q*q))==0
for val in [S.Rational(1,100),S.Rational(1,10),S.Rational(1,4)]:
 print("abs(gs epsilon)",val,"speeds",float(1/S.sqrt(1+val)),float(1/S.sqrt(1-val)))
print("TT vacuum Ricci zero, C^(0y0y),C^(0yxy),C^(xyxy)=",
 C[0,2,0,2],C[0,2,1,2],C[1,2,1,2])
print("source polarization mixing M^nu=",list(M))
print("PASS full 4D Weyl fixed-background characteristic subblock")
print("NEGATIVE full coupled metric constraints, EFT UV front and physical q2 selector open")
