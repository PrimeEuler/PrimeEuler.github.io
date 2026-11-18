#!/usr/bin/env python3
"""Gravity v15.1151: matched-source bicone detector and tidal polarimetry.
Source response E_K4 is NOT available absent sourced Einstein+solid ADM
constraints and boundary data; matching E implies identical outputs.
"""
import sympy as s
th,e0,gp,gx,DQ=s.symbols('th e0 gp gx DQ',real=True)
n=s.Matrix([s.cos(th),s.sin(th)])
E=s.Matrix([[e0+gp,gx],[gx,e0-gp]])
U=s.trigsimp(DQ*(n.T*E*n)[0]/2)
assert s.trigsimp(U-DQ*(e0+gp*s.cos(2*th)+gx*s.sin(2*th))/2)==0
torque=s.trigsimp(-s.diff(U,th))
assert s.trigsimp(torque-DQ*(gp*s.sin(2*th)-gx*s.cos(2*th)))==0
assert s.simplify(torque.subs({gp:0,gx:0}))==0
magic=s.atan(s.sqrt(2))
second=magic+s.pi/4
M=s.simplify(s.trigsimp(s.Matrix([
 [s.sin(2*magic),-s.cos(2*magic)],
 [s.sin(2*second),-s.cos(2*second)]])))
expected=s.Matrix([[2*s.sqrt(2)/3,s.Rational(1,3)],
 [-s.Rational(1,3),2*s.sqrt(2)/3]])
assert s.simplify(M-expected)==s.zeros(2)
assert s.simplify(M.det()-1)==0
assert s.simplify(M.T*M-s.eye(2))==s.zeros(2)
P1,X1,P2,X2=s.symbols('P1 X1 P2 X2',real=True)
G0,kappa,In,Gamma,omega,gamma,d,W,phase=s.symbols(
 'G0 kappa In Gamma omega gamma d W phase',real=True)
chi=1/(kappa-In*omega**2-s.I*Gamma*omega)
cal=-2*s.sin(phase)*gamma*G0*d*s.sin(th)*W*chi*DQ
def readout(plus,cross):
 return s.simplify(cal*(plus*s.sin(2*th)-cross*s.cos(2*th)))
residual=s.simplify(readout(P2,X2)-readout(P1,X1))
assert s.simplify(residual-readout(P2-P1,X2-X1))==0
assert s.simplify(residual.subs({P2:P1,X2:X1}))==0
print('PASS isotropic null, two-angle polarimetry, matched-source zero')
print('normalized polarimetry matrix:',M)
print('unknown sourced-K4 detector residual:',residual)
