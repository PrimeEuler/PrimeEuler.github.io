#!/usr/bin/env python3
"""Gravity v15.1126 — Larmor cone transverse quadratic vs paired bicone.

Prior exact sources: Jx_Jy_V4_Quarter_Shift_Findings, v15.955
(state-center/midpoint), v14.863, v15.1123-1125.
The operator Jxy² is J²-Jz², not a separate central SU2 Casimir.
For each j=1/2, Jxy²=1/2 I; paired Lxy²/Axy² discriminate
singlet versus triplet and track imposed differential Zeeman phase.
"""
import sympy as s
I=s.I
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
eye=s.eye(2)
J_A=[s.kronecker_product(g,eye)/2 for g in (sx,sy,sz)]
J_B=[s.kronecker_product(eye,g)/2 for g in (sx,sy,sz)]
L=[J_A[i]+J_B[i] for i in range(3)]
D=[J_A[i]-J_B[i] for i in range(3)]
Lxy=s.simplify(L[0]**2+L[1]**2)
Dxy=s.simplify(D[0]**2+D[1]**2)
assert J_A[0]**2+J_A[1]**2==s.eye(4)/2
assert J_B[0]**2+J_B[1]**2==s.eye(4)/2
assert s.simplify(Lxy+Dxy-2*s.eye(4))==s.zeros(4)
sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
trip0=s.Matrix([0,1,1,0])/s.sqrt(2)
assert Lxy*sing==s.zeros(4,1) and Lxy*trip0==2*trip0
assert Dxy*sing==2*sing and Dxy*trip0==s.zeros(4,1)
assert s.simplify(D[2]*sing-trip0)==s.zeros(4,1)
p=s.symbols('p',real=True)
state=s.cos(p/2)*sing+I*s.sin(p/2)*trip0
assert s.simplify((state.conjugate().T*state)[0]-1)==0
valL=s.trigsimp((state.conjugate().T*Lxy*state)[0])
valD=s.trigsimp((state.conjugate().T*Dxy*state)[0])
assert s.simplify(valL-(1-s.cos(p)))==0
assert s.simplify(valD-(1+s.cos(p)))==0
# Individual spin-j coherent state: E(Jxy²)=j+j(j-1/2)sin²(theta).
j,theta=s.symbols('j theta',real=True,positive=True)
coherent=s.expand_trig(j*(j+1)-(j*j*s.cos(theta)**2+j*s.sin(theta)**2/2))
assert s.trigsimp(coherent-j-j*(j-s.Rational(1,2))*s.sin(theta)**2)==0
assert s.simplify(coherent.subs(j,s.Rational(1,2))-s.Rational(1,2))==0
# For paired pure singlet each individual spin expectation is 0:
for op in J_A+J_B:
    assert s.simplify((sing.conjugate().T*op*sing)[0])==0
print("PASS: individual j=1/2 Jxy²=1/2 I, no Larmor aperture observable")
print("PASS: Lxy²+Dxy²=2 I, singlet/triplet opposite transverse channels")
print("PASS: relative Zeeman phase p=(Omega_A-Omega_B)t gives", valL, valD)
print("CONDITION: independent spinor Hamiltonian and clock; no causal-circle selector")
