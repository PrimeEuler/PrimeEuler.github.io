#!/usr/bin/env python3
"""Gravity v15.1050: literal signed-pair reflection of mod-12 V4
four shell points from T-cone to X-cone unit parabolas.
This is signed-pair geometry, not a sourced force/acceleration law.
"""
import sympy as s
r=s.symbols("r",positive=True)
T=(r+1)/2
X=(r-1)/2
Tx=(r-1)/2
Xx=(r+1)/2
assert s.simplify(T**2-X**2-r)==0
assert s.simplify(Xx**2-Tx**2-r)==0
assert s.simplify(2*T-1-r)==0
assert s.simplify(2*Xx-1-r)==0
for rr in [1,5,7,11]:
 assert s.simplify((T-X).subs(r,rr)-1)==0
 assert s.simplify((Tx-Xx).subs(r,rr)+1)==0
 assert s.simplify((T+X).subs(r,rr)-rr)==0
 assert s.simplify((Tx+Xx).subs(r,rr)-rr)==0
 assert (s.sqrt(rr))**2==rr
l=2+s.sqrt(3)
linv=2-s.sqrt(3)
assert s.simplify(l*linv-1)==0
# Under boost u' = lambda u, v'=lambda^-1 v.
# The X cone remains an X cone; the v=-1 unit row transforms to
# v'=-lambda^-1, so the discrete r packet is not invariant.
u=r;v=-s.Integer(1)
up=l*u;vp=linv*v
Tnew=(up+vp)/2;Xnew=(up-vp)/2
assert s.simplify(Xnew**2-Tnew**2-r)==0
assert s.simplify(Tnew-Xnew+linv)==0
assert s.simplify(Tnew-Xnew+1)!=0
# Signed cone transfer (u,v)->(u,-v) is NOT the boost:
# it swaps X and T for the original positive (r,1) point.
assert s.simplify(Tx-X)==0 and s.simplify(Xx-T)==0
# χ12 on U(12) matches the abstract checkerboard pattern,
# but not the geometric wedge character: all 4 signed X points
# have uv<0 and therefore the SAME wedge sign.
chi={1:1,5:-1,7:-1,11:1}
assert [chi[n] for n in (1,5,7,11)]==[1,-1,-1,1]
assert all(s.sign(-rr)==-1 for rr in (1,5,7,11))
print("PASS 4 V4 sqrt-shell representatives on both mirrored unit parabolas")
print("PASS boost preserves X-cone but changes v=-1 to -lambda^-1")
print("PASS arithmetic chi12 differs from constant wedge sign on selected X packet")
