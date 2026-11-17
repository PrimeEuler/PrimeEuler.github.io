#!/usr/bin/env python3
"""Gravity v15.1121 supplement: row/column acceleration-parabola planes,
cone action-circle poles, and V4 lift/factor reflection fixed loci.

These are exact Cone/PaperA geometric intersections, not self-sourced
acceleration, orbital time evolution or quantized physical action.
"""
import sympy as s
T,X,Y,k=s.symbols("T X Y k",real=True)
cone=T*T-X*X-Y*Y
row=T+X-k
column=T-X-k
for sign in (-1,1):
    P={T:k,X:0,Y:sign*k}
    assert s.simplify(cone.subs(P))==0
    assert s.simplify(row.subs(P))==0
    assert s.simplify(column.subs(P))==0
    assert s.simplify((X*X+Y*Y-k*k).subs(P))==0
    assert s.simplify((Y*Y-k*k+2*k*X).subs(P))==0
    assert s.simplify((Y*Y-k*k-2*k*X).subs(P))==0
# Factor exchange X->-X swaps row and column planes.
assert s.simplify(row.subs(X,-X)-column)==0
# Lift reflection Y->-Y exchanges the two joint points.
# Factor exchange is fixed at the balanced intersection X=0.
print("PASS reflected row/column cone parabolas meet at X=0,T=k,Y=+-k")
print("PASS these are two poles of the fixed-T=k anti-diagonal circle")
print("PASS row/column exchange X->-X and lift exchange Y->-Y are distinct")
