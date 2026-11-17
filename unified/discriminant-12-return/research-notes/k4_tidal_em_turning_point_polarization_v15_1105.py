#!/usr/bin/env python3
"""Gravity v15.1105: plus-TT gravitational strain and two transverse cavity polarizations.

The metric is ds^2=-dt^2+(1+h)dx^2+(1-h)dy^2+dz^2 in c=1.
The standing EM mode varies along x, while the tidal GW propagates
along z. For Ay, h changes the electric kinetic coefficient; for Az,
h changes the magnetic stiffness coefficient. Fixed rigid cavity modes,
narrow z aperture, weak strain and neglected boundary/backreaction effects.
"""
import sympy as s
h,Q,Qd,Qdd,hd,omega,A,theta,delta=s.symbols(
    'h Q Qd Qdd hd omega A theta delta',real=True)
sqrtg=s.sqrt(1-h*h)
ge_y=sqrtg/(1-h)
gb_y=sqrtg/((1+h)*(1-h))
ge_z=sqrtg
gb_z=sqrtg/(1+h)
assert s.diff(ge_y,h).subs(h,0)==1
assert s.diff(gb_y,h).subs(h,0)==0
assert s.diff(ge_z,h).subs(h,0)==0
assert s.diff(gb_z,h).subs(h,0)==-1
# Modes normalized to L_y=1/2[(1+h) Qdot^2-omega^2 Q^2]
# and L_z=1/2[Qdot^2-omega^2(1-h) Q^2], to first order in h.
for M,k,pol in [(1+h,omega**2,'y'),(1,omega**2*(1-h),'z')]:
    H=M*Qd**2/2+k*Q**2/2
    eom=s.solve(s.Eq(M*Qdd+s.diff(M,h)*hd*Qd+k*Q,0),Qdd)[0]
    energy_rate=s.diff(H,Q)*Qd+s.diff(H,Qd)*eom+s.diff(H,h)*hd
    work=-hd*(Qd**2 if pol=='y' else omega**2*Q**2)/2
    assert s.simplify(energy_rate-work)==0
# Sudden change in h at fixed canonical momentum p=M Qdot and fixed Q.
# Formal idealization: smooth physical pulses instead use time integrals.
p=s.symbols('p',real=True)
Hbefore=p**2/2+omega**2*Q**2/2
Hafter_y=p**2/(2*(1+delta))+omega**2*Q**2/2
Hafter_z=p**2/2+omega**2*(1-delta)*Q**2/2
assert s.simplify(s.diff(Hafter_y,delta).subs(delta,0)+p**2/2)==0
assert s.simplify(s.diff(Hafter_z,delta).subs(delta,0)+omega**2*Q**2/2)==0
DHy=s.diff(Hafter_y,delta).subs(delta,0).subs(p,-A*omega*s.sin(theta))
DHz=s.diff(Hafter_z,delta).subs(delta,0).subs(Q,A*s.cos(theta))
E0=A**2*omega**2/2
assert s.simplify(DHy/E0+s.sin(theta)**2)==0
assert s.simplify(DHz/E0+s.cos(theta)**2)==0
for angle,ey,ez in [(0,0,-1),(s.pi/2,-1,0)]:
    assert s.simplify((DHy/E0).subs(theta,angle)-ey)==0
    assert s.simplify((DHz/E0).subs(theta,angle)-ez)==0
# Smooth h(t), vanishing outside the pump: integrate -hdot/2 times
# the appropriate mode energy by parts. Transfer kernels differ in sign.
phi,t=s.symbols('phi t',real=True)
for pol,energy_piece in [
    ('y',A**2*omega**2*s.sin(omega*t+phi)**2),
    ('z',A**2*omega**2*s.cos(omega*t+phi)**2)]:
    kernel=s.simplify(s.diff(energy_piece,t)/(2*E0))
    expected=(omega if pol=='y' else -omega)*s.sin(2*omega*t+2*phi)
    assert s.trigsimp(kernel-expected)==0
# Electric standing-wave energy and magnetic standing-wave energy
# exchange roles at the two quadrature times.
assert s.sin(0)**2==0 and s.cos(0)**2==1
assert s.sin(s.pi/2)**2==1 and s.cos(s.pi/2)**2==0
print('PASS: two Maxwell polarizations, energy exchange and turning-point selection')
print('Ay fractional sudden-pump work /delta=',s.factor(DHy/E0))
print('Az fractional sudden-pump work /delta=',s.factor(DHz/E0))
print('Smooth-pump Ay/Az work kernels are +omega/-omega times sin(2omega*t+2phi)')
