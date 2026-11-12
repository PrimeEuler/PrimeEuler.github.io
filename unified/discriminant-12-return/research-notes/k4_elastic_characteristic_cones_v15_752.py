#!/usr/bin/env python3
"""v15.752: classical K4 elastic mode characteristic cones/arrival relations.
The resulting ratio is conventional relativistic elasticity, not a Cone
unique gravitational prediction. Source-to-detector metric constraints
and physical readout are separate from propagation principal symbols.
"""
import sympy as s
eta,t,t0=s.symbols("eta tau tau0",positive=True,real=True)
cT2=s.Integer(1)
cV2=2*eta/3
cS2=-s.Rational(1,3)+8*eta/9
assert s.simplify((cT2-cV2)-3*(cV2-cS2))==0
assert s.simplify(cV2-cS2-(3-2*eta)/9)==0
assert s.simplify(cT2-cV2-(3-2*eta)/3)==0
for e in (s.Rational(3,8),s.Rational(3,4),s.Rational(3,2)):
    cs=float(cS2.subs(eta,e));cv=float(cV2.subs(eta,e))
    assert 0<=cs<=cv<=1
# Characteristic comoving radial speed dr/dtau=c_i/a, a=tau/sqrt3.
dt=s.sqrt(3)*s.log(t/t0)
rs=s.sqrt(cS2)*dt;rv=s.sqrt(cV2)*dt;rt=dt
assert s.simplify((rt**2-rv**2)-3*(rv**2-rs**2))==0
r=s.symbols("r",positive=True,real=True)
arrival=lambda speed_squared:t0*s.exp(r/(s.sqrt(3)*s.sqrt(speed_squared)))
assert s.simplify((r/(s.sqrt(3)*s.sqrt(cV2)))/(r/s.sqrt(3))-1/s.sqrt(cV2))==0
assert s.simplify((r/(s.sqrt(3)*s.sqrt(cS2)))/(r/s.sqrt(3))-1/s.sqrt(cS2))==0
case={eta:s.Rational(3,4)}
assert [s.simplify(v.subs(case)) for v in (cS2,cV2,cT2)]==[s.Rational(1,3),s.Rational(1,2),1]
# Fourier k_phys^2 slopes of v15.706, times 3 as a=tau/sqrt3.
assert s.simplify(3*cS2-(-1+8*eta/3))==0
assert s.simplify(3*cV2-2*eta)==0
print("PASS: K4 principal-cone speeds and isotropic-elasticity comparator")
print("PASS: coasting wavefront radii sqrt3*c_i*ln(t/t0)")
print("PASS: squared front-radius difference ratio 3")
print("eta=3/4, cS/cV/cT:",[s.sqrt(v.subs(case)) for v in (cS2,cV2,cT2)])
print("NOTE: front arrival is not automatically a detectable Weyl signal")
