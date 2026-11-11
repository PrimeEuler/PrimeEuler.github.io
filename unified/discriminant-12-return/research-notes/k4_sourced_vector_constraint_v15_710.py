#!/usr/bin/env python3
"""v15.710: source-first vector ADM shift of frozen K4 action (v14.935).

Reconstructs v14.935 vector_sector.py quadratic expansion, adds +J Bv
to the UNREDUCED action, eliminates Bv, computes constrained vector
propagation and the source-to-shift pole residue. J is a formal local
ADM source coefficient, NOT a covariantly normalized physical detector.
"""
import sympy as sp
eps,a,adot,kappa,C,eta,k=sp.symbols("eps a adot kappa C eta k",positive=True)
B,ft,fz,f=sp.symbols("Bv ft fz f")
J=sp.symbols("J")
def ser(x,n=3):return sp.expand(sp.series(x,eps,0,n).removeO())
Bb,F,Z=eps*B,eps*ft,eps*fz
detb=-a*a*(1+Bb**2)
gi00=ser(-a*a/detb)
gi0y=ser(-Bb/(a*(1+Bb**2)))
giyy=ser(1/detb)
gixx=-1/a**2;gizz=-1/a**2
Byy=ser(-(gi00*F**2+2*gi0y*F*(1+Z)+giyy+gizz*Z**2))
Byz=ser(-gizz*Z)
Bzz=-gizz;Bxx=-gixx
detM=ser(Bxx*(Byy*Bzz-Byz**2))
b_s=ser(sp.sqrt(detM))
trM=ser(2*Bxx+Byy)
trM2=ser(2*Bxx**2+Byy**2+2*Byz**2)
J_s=ser(trM2/trM**2-sp.Rational(1,3))
sqrtg=ser(a**3*sp.sqrt(1+Bb**2))
Lm=ser(-sqrtg*C*b_s**sp.Rational(2,3)*(1+eta*J_s))
Lm2=sp.expand(Lm).coeff(eps,2)
Le2=a*k*k/(4*kappa)*B**2+3*a*adot**2/(2*kappa)*B**2
f_t=sp.Symbol("f_t")
L=sp.expand(Lm2.subs({fz:-k*f,ft:f_t}))+Le2
A=sp.factor(sp.diff(L,B,2))
D=sp.factor(sp.diff(L,B).subs(B,0))
assert sp.simplify(sp.diff(L,B)-(A*B+D))==0
B0=sp.factor(-D/A)
BJ=sp.factor(-(D+J)/A)
assert sp.simplify(BJ-B0+J/A)==0
R0=sp.simplify(L.subs(B,B0))
RJ=sp.simplify((L+J*B).subs(B,BJ))
assert sp.simplify(sp.expand(RJ-R0+J*D/A+J*J/(2*A)))==0
K=sp.factor(sp.diff(R0,f_t,2))
G=sp.factor(-sp.diff(R0,f,2))
assert sp.simplify(A-a*(-2*C*kappa+18*adot**2+3*k**2)/(6*kappa))==0
assert sp.simplify(B0-4*C*a*f_t*kappa/(-2*C*kappa+18*adot**2+3*k**2))==0
assert sp.simplify(K-2*C*a**3*(-2*C*kappa+6*adot**2+k**2)/(-2*C*kappa+18*adot**2+3*k**2))==0
assert sp.simplify(G-4*C*a*eta*k**2/9)==0
kp=sp.symbols("k_phys",positive=True)
background={C:1,kappa:1,adot:1/sp.sqrt(3),a:1/sp.sqrt(3),k:kp/sp.sqrt(3)}
expected=sp.Rational(8,3)*eta+sp.Rational(2,3)*eta*kp**2
assert sp.simplify((G/K).subs(background)-expected)==0
bcoeff=sp.factor(sp.diff(B0,f_t))
assert sp.simplify(B0-bcoeff*f_t)==0
omega=sp.symbols("omega",real=True)
# With Fourier e^{-i omega t}, the f E-L equation gives:
# (G-K omega^2) f = i omega bcoeff J; B=bcoeff f_t-J/A.
B_over_J=sp.factor(omega**2*bcoeff**2/(G-K*omega**2)-1/A)
residue=sp.factor(-(G/K)*bcoeff**2/K)
assert sp.simplify(residue+G*bcoeff**2/K**2)==0
print("PASS: original K4 vector shift constraint and exact sourced elimination")
print("SHIFT_B0=",B0)
print("SHIFT_BJ=",BJ)
print("CONSTRAINT_A=",A)
print("POLE_OMEGA2=",sp.factor(G/K))
print("B_OVER_J=",B_over_J)
print("RESIDUE_OMEGA2=",residue)
