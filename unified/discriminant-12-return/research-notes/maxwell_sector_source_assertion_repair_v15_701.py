#!/usr/bin/env python3
"""Additive repair for the v15.695 SymPy matrix-identity assertion.
Preserves the original historical script and Audit Round 542 finding.
"""
import sympy as s
u,v,w,x,g=s.symbols("u v w x g")
chi=s.diag(1,1,-1,-1)
P=(s.eye(4)+chi)/2
W=s.Matrix([[0,0,u,v],[0,0,w,x],[u,w,0,0],[v,x,0,0]])
delta=P*(g*W)*(g*W)*P-g*g*(P*W*W*P)
assert delta.applyfunc(s.expand)==s.zeros(4)
assert delta.applyfunc(s.simplify)==s.zeros(4)
assert s.simplify(chi*W+W*chi)==s.zeros(4)
print("PASS: v15.695 arbitrary-g matrix identity; mathematical equality not syntax")
