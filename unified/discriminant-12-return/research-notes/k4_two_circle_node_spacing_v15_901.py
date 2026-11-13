#!/usr/bin/env python3
"""Gravity v15.901: conditional N=n+1 equally spaced phase stations.
Distinguish phase marks, standing-wave zeros, and physical frequency.
"""
import sympy as s
n,u,ell,L,M=s.symbols("n u ell L M",positive=True)
N=n+1
Ri=u*s.sqrt(n); Ro=u*(n+1)/2
gamma=s.factor(Ro/Ri)
dtheta=2*s.pi/N
arc_outer=s.simplify(Ro*dtheta)
arc_inner=s.simplify(Ri*dtheta)
assert s.simplify(arc_outer-s.pi*u)==0
assert s.simplify(arc_inner/(s.pi*u)-1/gamma)==0
assert s.simplify(2*Ro/u-(1+(Ri/u)**2))==0
# With physical lever arms ell*R, angular momentum conserved and node pattern transported.
omega_o=L/(M*(ell*Ro)**2)
omega_i=L/(M*(ell*Ri)**2)
f_o=N*omega_o/(2*s.pi)
f_i=N*omega_i/(2*s.pi)
assert s.simplify(f_i/f_o-gamma**2)==0
assert s.simplify((arc_outer/arc_inner)-gamma)==0
# For sin(m theta) nonzero integer m, number of distinct zeros on [0,2pi) is 2m.
for integer_n in range(1,10):
    integer_N=integer_n+1
    possible_sine_zero_count=integer_N%2==0
    print(f"n={integer_n} N={integer_N} outer-angle-step={float(2*s.pi/integer_N):.7f} "
          f"outer-arc/u={float(arc_outer/u):.7f} scalar-sine-{integer_N}-nodes={possible_sine_zero_count}")
print("PASS exact node spacing and skater passage-rate ratio; physical frequency remains unselected")
