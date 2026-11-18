#!/usr/bin/env python3
"""Gravity v15.1127: bicone misalignment as conventional tidal gradiometer.

Gravity: E_ij = d_i d_j Phi in a local freely falling frame.
For a transverse point-mass dumbbell Q=DeltaQ n⊗n, n=(cos θ,sin θ),
U=.5 E:Q, tau=-dU/dθ. Real torsional susceptibility is a separately
specified κ, inertia I, and damping Γ.
Quantum: paired SU2 transverse quadrupole Qs=J_Ax J_Bx-J_Ay J_By
couples |++> ↔ |--> but NOT singlet ↔ T0.
Any mechanical-angle -> Larmor-phase readout requires independently
calibrated transduction; no G or new operator derived.
"""
import sympy as s
t,g,DQ,kappa,Irot,Gamma,omega=s.symbols('theta g DeltaQ kappa Irot Gamma omega',real=True)
n=s.Matrix([s.cos(t),s.sin(t)])
tidal=s.diag(g,-g)
Q=DQ*n*n.T
U=s.trigsimp((tidal*Q).trace()/2)
torque=s.trigsimp(-s.diff(U,t))
assert s.trigsimp(U-g*DQ*s.cos(2*t)/2)==0
assert s.trigsimp(torque-g*DQ*s.sin(2*t))==0
assert s.simplify(torque.subs(t,0))==0
assert s.simplify(torque.subs(t,s.pi/4)-g*DQ)==0
chi=1/(kappa-Irot*omega**2-s.I*Gamma*omega)
assert s.simplify((kappa-Irot*omega**2-s.I*Gamma*omega)*chi)==1
# Spin one-half in C2 tensor C2; axis z follows Larmor B.
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1);unit=s.eye(2)
JA=[s.kronecker_product(p,unit)/2 for p in (sx,sy,sz)]
JB=[s.kronecker_product(unit,p)/2 for p in (sx,sy,sz)]
sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
trip0=s.Matrix([0,1,1,0])/s.sqrt(2)
pp=s.Matrix([1,0,0,0]);mm=s.Matrix([0,0,0,1])
Qspin=JA[0]*JB[0]-JA[1]*JB[1]
assert Qspin*sing==s.zeros(4,1)
assert Qspin*trip0==s.zeros(4,1)
assert Qspin*pp==mm/2 and Qspin*mm==pp/2
relative=JA[2]-JB[2]
assert relative*sing==trip0
print('PASS tidal quadrupole mechanical torque and 45-degree maximum')
print('PASS passive torsional susceptibility, spin rank-two selection')
print('U = g*DeltaQ/2*cos(2theta); tau = g*DeltaQ*sin(2theta)')
print('Qs couples ++ to --, not singlet to T0')
print('Caution: sensor transfer function and source metric not fixed by geometry')
