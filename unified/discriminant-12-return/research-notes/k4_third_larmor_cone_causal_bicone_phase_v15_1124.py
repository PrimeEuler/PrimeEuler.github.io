#!/usr/bin/env python3
"""Gravity v15.1124: third Larmor-spin precession cone versus common
circle of two causal cones and previous doubled SU(2) bicone.
Two carriers require an embedding; Larmor precession is Euclidean
spin orientation, not an independent Lorentzian causal null cone.
"""
import sympy as s
sx=s.Matrix([[0,1],[1,0]]); sz=s.diag(1,-1); ident=s.eye(2)
Ja=s.kronecker_product(sz,ident)/2
Jb=s.kronecker_product(ident,sz)/2
Delta,t=s.symbols('Delta t',real=True)
H=-Delta/2*(Ja-Jb)
sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
trip0=s.Matrix([0,1,1,0])/s.sqrt(2)
U=s.diag(*[s.exp(-s.I*t*H[k,k]) for k in range(4)])
assert s.simplify(U*sing-(s.cos(Delta*t/2)*sing+s.I*s.sin(Delta*t/2)*trip0))==s.zeros(4,1)
assert s.simplify((sing.T.conjugate()*U*sing)[0]-s.cos(Delta*t/2))==0
assert s.simplify((trip0.T.conjugate()*U*sing)[0]-s.I*s.sin(Delta*t/2))==0
# In the causal-pair common rest frame, cone intersection is
# at time coordinate T=R and spatial rho=R. Auxiliary spin cone
# with axis identified with T: rho=(T-Ts) tan(alpha) on forward branch.
alpha,R,Ts=s.symbols('alpha R Ts',positive=True,real=True)
assert s.simplify(((R-Ts)*s.tan(alpha)-R).subs(Ts,R-R/s.tan(alpha)))==0
# For Ts=0 and alpha=pi/4 this 'third' cone is identical to
# the first null cone, not an independent additional geometrical constraint.
assert s.simplify(((R-Ts)*s.tan(alpha)-R).subs({Ts:0,alpha:s.pi/4}))==0
w,th,ph=s.symbols('Omega theta phi0',real=True)
n=s.Matrix([s.sin(th)*s.cos(w*t+ph),s.sin(th)*s.sin(w*t+ph),s.cos(th)])
assert s.trigsimp(n.dot(n)-1)==0
assert s.trigsimp(s.diff(n,t).dot(n))==0
# Equal frequencies remove the relative-spin Hamiltonian:
assert H.subs(Delta,0)==s.zeros(4)
# If Delta*t=2pi*k, singlet returns up to global sign;
# continuous singlet preservation needs Delta=0.
k=s.symbols('k',integer=True)
assert s.simplify(s.sin(s.pi*k))==0
print('PASS third Larmor orientation cone and conditional causal-circle coincidence')
print('PASS doubled SU2 singlet-triplet relative Larmor mixing')
print('P_sing(t)=cos^2((Omega_A-Omega_B)*t/2)')
print('No physical time clock or SU2 representation follows from spatial circle gluing')
