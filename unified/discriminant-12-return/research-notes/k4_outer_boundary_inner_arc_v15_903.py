#!/usr/bin/env python3
"""v15.903: n+1 is outer diameter boundary, not presumed N=n+1 node count.
Compare inner half-circle arc, outer chord-endpoint arc and an outer
boundary mode with half-wavelength equal to inner half-arc.
"""
import sympy as s
import math
n,u=s.symbols("n u",positive=True)
Ri=u*s.sqrt(n)
Ro=u*(n+1)/2
half=s.pi*Ri
circle_circ=2*s.pi*Ro
gamma=s.simplify(circle_circ/(2*half))
assert s.simplify(gamma-(n+1)/(2*s.sqrt(n)))==0
assert s.simplify((half/Ro)-(2*s.pi*s.sqrt(n)/(n+1)))==0
assert s.simplify((Ro**2-(u*(n-1)/2)**2)-(u*s.sqrt(n))**2)==0

# If a conventional real periodic standing wave on the outer circle has
# adjacent zeros separated by half=pi*Ri, its integer azimuthal mode must
# be m=C_outer/(2*half)=gamma. For integer n, m integer only at n=1:
# rational sqrt(n) -> integer k; k^2+1=2mk -> k divides 1 -> k=1.
for N in range(1,101):
    gam=(N+1)/(2*math.sqrt(N))
    integer_mode=abs(gam-round(gam))<1e-12
    assert integer_mode==(N==1)
for N in (1,2,4,9,16):
    outer=(N+1)*math.asin(2*math.sqrt(N)/(N+1))
    inner=math.pi*math.sqrt(N)
    phase_on_outer=2*math.pi*math.sqrt(N)/(N+1)
    print(f"n={N} outer_chord_arc/u={outer:.10f} inner_half_arc/u={inner:.10f} mode={((N+1)/(2*math.sqrt(N))):.10f} outer_angle_for_inner_length={phase_on_outer:.10f}")
print("PASS: distinct outer chord arc, inner semicircle, outer-boundary periodic mode obstruction")
