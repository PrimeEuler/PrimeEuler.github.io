#!/usr/bin/env python3
"""v15.1404: fixed-U null-affine spacing of nested EM/quarter/null Q-levels.
3:1 is invariant for three collinear points under ambient Lorentz action,
but selecting null line, physical flux density and Dirac boost is extra.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps=65
U,Y,beta,gamma=sp.symbols("U Y beta gamma",positive=True,real=True)
levels=[sp.S(0),sp.Rational(1,16),sp.Rational(1,4)]
V=[(Y**2+mu)/U for mu in levels]
P=[sp.Matrix([(U+v)/2,(U-v)/2,Y]) for v in V]
Q=lambda p:sp.factor(p[0]**2-p[1]**2-p[2]**2)
for p,mu in zip(P,levels):assert sp.simplify(Q(p)-mu)==0
assert sp.simplify((V[2]-V[1])/(V[1]-V[0]))==3
D1=P[1]-P[0];D2=P[2]-P[1]
assert sp.simplify(D2-3*D1)==sp.zeros(3,1)
assert sp.simplify(Q(D1))==0
Bty=sp.Matrix([[sp.cosh(beta),0,sp.sinh(beta)],[0,1,0],[sp.sinh(beta),0,sp.cosh(beta)]])
Btx=sp.Matrix([[sp.cosh(gamma),sp.sinh(gamma),0],[sp.sinh(gamma),sp.cosh(gamma),0],[0,0,1]])
B=Btx*Bty
assert sp.simplify(B.T*sp.diag(1,-1,-1)*B-sp.diag(1,-1,-1))==sp.zeros(3)
assert sp.simplify(B*(D2-3*D1))==sp.zeros(3,1)
Dirac=mp.mpf("2.26866143917643529e39");psi=mp.log(Dirac)/2
b=mp.mpf(".25");U0=b*mp.exp(psi)
Vv=[mp.mpf(0),b*b/U0,mp.mpf(".25")/U0]
assert mp.almosteq((Vv[2]-Vv[1])/Vv[1],mp.mpf(3))
eta_em=mp.log(U0/mp.mpf(".5"))
assert mp.almosteq(psi-eta_em,mp.log(2))
print("Dirac rapidity INPUT",mp.nstr(psi,29),"fixed U",mp.nstr(U0,23))
print("V null/q2/EM:",*[mp.nstr(a,24) for a in Vv])
print("same-U rapidity quarter",mp.nstr(psi,22),"EM",mp.nstr(eta_em,22),"difference",mp.nstr(mp.log(2),18))
print("PASS 3:1 null-affine intervals invariant under generic ambient boosts")
print("OPEN null-congruence/action selection and an actual physical flux/transition coefficient")
