#!/usr/bin/env python3
"""v15.876: standard GR tidal quadratic coupling to a bound oscillator.

In a local Fermi orthonormal frame, geodesic deviation gives a tidal
acceleration proportional to -R_{0i0j} x^j. For a 1D nonrelativistic
bound coordinate choose xddot+(omega_e²+R(t))x=0 (sign convention fixed
by this equation). The tidal oscillator energy exchanges with a
time-dependent prescribed gravitational curvature according to
dE/dt=Rdot x²/2. Its energy is NOT conserved in the truncated
externally prescribed background; the source of the GW supplies work.
Physical GR GW R amplitude ~ h Ω²/2 in the weak field.

This is a conventional local comparator, not a full K4-Maxwell
quantum electron calculation and not a Cone coupling selector.
"""
import sympy as s
from scipy.constants import e,epsilon_0,m_e,m_p,G,hbar,pi
x,v,t,w,R,Omega=s.symbols('x v t omega R Omega',real=True)
stiffness=w*w+R*s.cos(Omega*t)
energy=(v*v+stiffness*x*x)/2
denergy=s.simplify(s.diff(energy,t)+s.diff(energy,x)*v+
                   s.diff(energy,v)*(-stiffness*x))
assert s.simplify(denergy+s.Rational(1,2)*R*Omega*
                   s.sin(Omega*t)*x*x)==0
# Hydrogen reference classical frequency and physical tidal magnitude
K=e**2/(4*pi*epsilon_0)
a0=hbar**2/(m_e*K)
w_e=(K/(m_e*a0**3))**.5
r_gravity=G*m_p/a0**3
force_ratio=r_gravity/w_e**2
assert 4.3e-40<force_ratio<4.5e-40
# Standard GW R(t)≈(h/2)*Omega² cos(Omega*t) (TT wave).
# Therefore |delta omega²| / omega_e²≈h Omega²/(2 omega_e²).
h=1e-21
low_omega=2*pi*100
low_eps=h*low_omega**2/(2*w_e**2)
res_omega=2*w_e
res_eps=h*res_omega**2/(2*w_e**2)
assert 1e-50<low_eps<2e-49
assert abs(res_eps-2*h)<1e-34
print('Bohr radius',a0,'classical Coulomb angular frequency',w_e)
print('proton gravity to Coulomb local tidal ratio',force_ratio)
print('illustrative GW 100 Hz h=1e-21 fractional stiffness',low_eps)
print('illustrative resonant GW angular frequency',res_omega)
print('illustrative resonant GW frequency (Hz)',res_omega/(2*pi))
print('illustrative h=1e-21 resonant fractional stiffness',res_eps)
print('PASS standard GR local tidal coupling and physical hierarchy')
print('SCOPE illustrative GW strain, not a measured source or Cone selector')
