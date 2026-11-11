#!/usr/bin/env python3
"""v15.711: source-first scalar lapse/shift auxiliary Hessian in frozen K4.

Sets propagating scalar psi,E,P to zero ONLY to isolate the Phi/B
quadratic Hessian. This determines shifts of sourced constraints but
NOT the complete source-to-propagating-scalar Green function.
"""
import sympy as s
eps,a,adot,kappa,C,eta,k=s.symbols("eps a adot kappa C eta k",positive=True)
Phi,Bz,Bzz,B=s.symbols("Phi Bz Bzz B")
JP,JB=s.symbols("J_Phi J_B")
N2=1+2*eps*Phi+eps**2*Bz**2
N=s.sqrt(N2)
LEH=a*(-6*adot**2+4*eps*adot*Bzz)/(2*kappa*N)
R=(1+2*eps*Phi)/N2
Jsolid=(2+R**2)/(2+R)**2-s.Rational(1,3)
LM=-a*C*(1+2*eps*Phi)**s.Rational(1,3)*N2**s.Rational(1,6)*(1+eta*Jsolid)
q2=lambda u:s.expand(s.series(u,eps,0,3).removeO()).coeff(eps,2)
L2=s.factor(q2(LEH)+q2(LM))
assert s.simplify(q2(Jsolid))==0
hand=a/(2*kappa)*(-9*adot**2*Phi**2+3*adot**2*Bz**2-4*adot*Phi*Bzz)+a*C*(Phi**2/2-Bz**2/6)
assert s.simplify(L2-hand)==0
Lf=s.expand(L2.subs({Bz:-k*B,Bzz:-k*k*B}))
H=s.hessian(Lf,(Phi,B)).applyfunc(s.factor)
Hhand=s.Matrix([[a*(kappa*C-9*adot**2)/kappa,2*a*adot*k*k/kappa],
  [2*a*adot*k*k/kappa,a*k*k*(9*adot**2-kappa*C)/(3*kappa)]])
assert (H-Hhand).applyfunc(s.simplify)==s.zeros(2)
on={a:1/s.sqrt(3),adot:1/s.sqrt(3),C:1,kappa:1}
Hon=H.subs(on)
det=s.factor(Hon.det())
assert s.simplify(det+4*k*k*(1+k*k)/9)==0
Jvec=s.Matrix([JP,JB])
delta=-Hon.inv()*Jvec
assert (Hon*delta+Jvec).applyfunc(s.simplify)==s.zeros(2,1)
contact=-s.Rational(1,2)*(Jvec.T*Hon.inv()*Jvec)[0]
print("PASS: exact scalar source-before-constraint Hessian for k>0")
print("HESSIAN=",H)
print("COASTING_DET=",det)
print("DELTA_PHI_B=",delta.applyfunc(s.factor))
print("SOURCE_CONTACT=",s.factor(contact))
