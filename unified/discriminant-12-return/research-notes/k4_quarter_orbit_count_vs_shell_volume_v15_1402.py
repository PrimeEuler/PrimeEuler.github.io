#!/usr/bin/env python3
"""v15.1402: finite closed-q2 versus EM SU2 state count and KKS orbit areas.
State density is not the ambient EM–q2 hyperboloid annulus area.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
jE=(D-1)/2
jQ=(2*D-1)/2
assert s.simplify(2*jE+1-D)==0
assert s.simplify(2*jQ+1-2*D)==0
ratio=s.simplify(jQ/jE)
assert s.simplify(ratio-2-1/(D-1))==0
assert s.limit(ratio,D,s.oo)==2
assert s.simplify(2*D/D)==2
for d in (2,3,4,5,10,100):
 print('D',d,'EM_states',d,'q2_states',2*d,'orbit_ratio',ratio.subs(D,d))
print('PASS q2/EM state count 2, SU2 KKS symplectic orbit ratio 2+1/(D-1)')
print('NEGATIVE neither canonical state count nor orbit area generally equals 3:1 volume-shell partition')
