#!/usr/bin/env python3
"""Gravity v15.1147 — magic angle, torsion–SU2 backaction.

H=p²/(2I)+I*omega²*q²/2-(hbar/2)*(Delta0+k*q)*Dz.
Initially prepared singlet; harmonic oscillator initially in ground state.
The exact spin-coherence visibility is
exp[-hbar*k²/(I*omega³)*sin²(omega*t/2)], provided the system
is closed, undamped, and spin branch force is linear in q.
The magnetic gradient and torsion parameters are external apparatus
inputs; this is standard spin-boson/forced oscillator physics.
"""
import sympy as s
th=s.symbols('theta',real=True)
magic=s.atan(s.sqrt(2))
assert s.simplify(s.sin(magic)**2-s.Rational(2,3))==0
assert s.simplify(s.cos(magic)**2-s.Rational(1,3))==0
assert s.simplify((3*s.cos(magic)**2-1)/2)==0
f=s.sin(th)*s.sin(2*th)
assert s.simplify(s.trigsimp(s.diff(f,th)).subs(th,magic))==0
assert s.simplify(s.trigsimp(f.subs(th,magic))-4/(3*s.sqrt(3)))==0
I=s.I; sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1); eye=s.eye(2); kron=s.kronecker_product
JA=kron(sz,eye)/2; JB=kron(eye,sz)/2
Dz=JA-JB; sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
assert s.simplify((sing.conjugate().T*Dz*sing)[0])==0
assert s.simplify((sing.conjugate().T*Dz**2*sing)[0])==1
Jax=kron(sx,eye)/2; Jay=kron(sy,eye)/2
Jbx=kron(eye,sx)/2; Jby=kron(eye,sy)/2
Lxy=(Jax+Jbx)**2+(Jay+Jby)**2
Dxy=(Jax-Jbx)**2+(Jay-Jby)**2
Cop=Lxy-Dxy
D0,k,t,hbar,Im,w,G,d,gamma=s.symbols(
    'Delta0 k t hbar Im omega G d gamma',positive=True,real=True)
F=hbar*k/2
alpha_sq=s.simplify(F**2/(2*Im*hbar*w**3)*(2-2*s.cos(w*t)))
exponent=s.simplify(2*alpha_sq)
assert s.simplify(exponent-hbar*k**2/(Im*w**3)*s.sin(w*t/2)**2)==0
visibility=s.exp(-exponent)
assert s.simplify(visibility.subs(t,0)-1)==0
assert s.simplify(visibility.subs(t,2*s.pi/w)-1)==0
assert s.simplify(visibility.subs(t,s.pi/w)-
    s.exp(-hbar*k**2/(Im*w**3)))==0
phase=s.symbols('phase',real=True)
V=s.symbols('V',real=True,nonnegative=True)
rho=s.zeros(4)
rho[1,1]=s.Rational(1,2);rho[2,2]=s.Rational(1,2)
rho[1,2]=-V*s.exp(I*phase)/2
rho[2,1]=-V*s.exp(-I*phase)/2
assert s.simplify(s.trace(rho)-1)==0
assert s.simplify(s.expand_complex(
    s.trace(rho*Cop)+2*V*s.cos(phase)))==0
assert s.simplify((sing.conjugate().T*F*Dz*sing)[0])==0
assert s.simplify((sing.conjugate().T*(F*Dz)**2*sing)[0]-F**2)==0
print('PASS magic angle P2=0, sensor optimum theta=atan(sqrt2)')
print('PASS quantum torsion/spin zero mean, nonzero torque variance')
print('PASS visibility=',visibility)
print('PASS Cxy=-2*visibility*cos(relative phase)')
print('CAUTION planar gradient angle != polar magic angle to B0')
