#!/usr/bin/env python3
"""Exact action circle and node frequency selector test.

An action per radian J=E/omega=hbar specifies no omega without E.
The sin action-phase wave has physical node spacing pi/omega.
The full phase period carries 2*pi*hbar action, whereas a radian
carries hbar. Both EM/G mesh fractions label dimensionless turns;
no physical node time follows unless an energy/clock is supplied.
"""
import sympy as s
E, hb, t, c, mass, q = s.symbols('E hbar t c mass q', positive=True)
omega=E/hb
node_time=s.pi/omega
period=2*s.pi/omega
assert s.simplify(node_time-period/2)==0
assert s.simplify(1/(2*node_time)-E/(2*s.pi*hb))==0
assert s.simplify(E*node_time-s.pi*hb)==0
assert s.simplify(E*period-2*s.pi*hb)==0
assert s.simplify(E*(hb/E)-hb)==0 # one radian, not one turn
assert s.simplify(omega.subs(E,mass*c*c)-mass*c*c/hb)==0
assert s.simplify((c*period).subs(E,mass*c*c)-2*s.pi*hb/(mass*c))==0
J=s.simplify(E/omega)
assert J==hb
for ratio in (s.Rational(1,2),2,3,10):
    # J constant while E and omega scale together.
    assert s.simplify((ratio*E)/(ratio*omega)-hb)==0
    assert s.simplify((s.pi/(ratio*omega))/node_time-1/ratio)==0
# Mesh node positions u=j*h/2 are coordinates, not physical times;
# t=T0*u adds an arbitrary dimensional scale T0.
T0, hstep, j=s.symbols('T0 hstep j',positive=True)
phys_node_spacing=T0*hstep/2
freq=s.simplify(1/(2*phys_node_spacing))
assert s.simplify(freq-1/(T0*hstep))==0
assert s.simplify((freq.subs(hstep,s.Rational(1,2)))/(freq.subs(hstep,1))-2)==0
# ratio 2 ONLY when the coordinate-to-time map T0 is shared.
print('PASS phase nodes separated by pi*hbar/E and f=E/h')
print('PASS full winding action=h; one-radian action=hbar')
print('PASS invariant J=hbar with arbitrary paired E/omega rescaling')
print('PASS EM/G half-step gives relative 2x rate ONLY under assumed common T0')
print('OPEN action circle supplies no unique energy or physical node clock')
