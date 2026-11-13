#!/usr/bin/env python3
"""v15.871: Muse's EM 1/2 rate crowns vs EM 1/4 rate minima.

Test *both* a common physical wave with h=1 and a sector-rescaled
phase dictionary h_EM=1, h_G=1/2. The same coordinate x=1/4
is a sin-derivative minimum for the EM wave and a sin-derivative
maximum for the gravity-rescaled phase. This is a phase-dictionary
identity, NOT observed EM-gravity coupling, force law or rate selector.

For x(t)=A sin(omega t), max velocity at displacement zero/node,
zero velocity at extrema; restoring force F=m x_ddot is ZERO at
nodes and maximal at extrema. Power F*v vanishes at both.
Do not conflate max RATE with max FORCE or max POWER.
"""
import sympy as s
x,h,A,omega,m=s.symbols("x h A omega m",positive=True,real=True)
phase=2*s.pi*x/h
wave=A*s.sin(phase)
rate=s.diff(wave,x)
acc=s.diff(rate,x)
rhat=s.simplify(h*rate/(2*s.pi*A))
assert s.simplify(rhat-s.cos(phase))==0
# At EM h=1: half-turn node (rate crown), quarter antinode (rate zero).
# At G h=1/2: x=1/4 is the sector's *half-turn* node.
for step,coordinate,expected_rate,expected_acc in (
  (s.Integer(1),s.Rational(1,2),-1,0),
  (s.Integer(1),s.Rational(1,4),0,-1),
  (s.Rational(1,2),s.Rational(1,4),-1,0),
  (s.Rational(1,2),s.Rational(1,8),0,-1)
):
    values={h:step,x:coordinate}
    assert s.simplify(rhat.subs(values)-expected_rate)==0
    assert s.simplify(acc.subs(values)/(A*(2*s.pi/step)**2)-expected_acc)==0
# The normalized first derivative depends on the phase, NOT on the
# physical or dimensional time unless dphase/dt is independently set.
assert s.simplify((rhat.subs(h,1)).subs(x,s.Rational(1,4)))==0
assert s.simplify((rhat.subs(h,s.Rational(1,2))).subs(x,s.Rational(1,4))+1)==0
t=s.symbols("t",real=True)
position=A*s.sin(omega*t)
velocity=s.diff(position,t)
force=m*s.diff(position,t,2)
power=s.simplify(force*velocity)
assert s.simplify(force+m*omega**2*position)==0
for ph,V,F in ((0,1,0),(s.pi/2,0,-1),(s.pi,-1,0),
               (3*s.pi/2,0,1)):
    values={t:ph/omega}
    assert s.simplify(velocity.subs(values)/(A*omega)-V)==0
    assert s.simplify(force.subs(values)/(m*A*omega**2)-F)==0
    assert s.simplify(power.subs(values))==0
energy=s.simplify(m*velocity**2/2+m*omega**2*position**2/2)
assert s.simplify(s.diff(energy,t))==0
assert s.simplify(power+m*A**2*omega**3*s.sin(2*omega*t)/2)==0
# At t=pi/(4 omega) the instantaneous power is nonzero (in magnitude
# maximum), whereas it is zero at both rate extrema and turning points.
assert s.simplify(power.subs(t,s.pi/(4*omega))
          +m*A**2*omega**3/2)==0
print("PASS EM h=1 half-turn max sine-rate, quarter-turn zero sine-rate")
print("PASS sector G h=1/2 maps x=1/4 to its rate crown, not the EM crown")
print("PASS harmonic force maximal where velocity zero; power zero at both")
print("PASS kinetic + potential constant, no force or G selector imported")
