#!/usr/bin/env python3
"""v15.832: quadratic canonical spectator stress gauge-order control.

Let chi=epsilon chi1 with zero background, h=epsilon^2 h2, and
xi=epsilon^2 xi2. Then chi changes at epsilon^3 and T[chi] changes
at epsilon^4. The metric and K4 solid background do transform at
epsilon^2, so source stress invariance alone is NOT a full on-shell
gauge covariance proof for the coupled EH+solid model.
"""
import sympy as s
E=s.symbols("eps",real=True)
t,x=s.symbols("t x",real=True)
chi1=s.Function("chi1")(t,x)
T=s.Function("T")(t,x);U=s.Function("U")(t,x)
g0=s.Function("g0")(t,x)
chi=E*chi1
newchi=chi-E**2*(T*s.diff(chi,t)+U*s.diff(chi,x))
assert s.simplify(newchi-chi+E**3*(T*s.diff(chi1,t)+U*s.diff(chi1,x)))==0
for i in (t,x):
 for j in (t,x):
    old=s.diff(chi,i)*s.diff(chi,j)
    new=s.diff(newchi,i)*s.diff(newchi,j)
    difference=s.expand(new-old)
    assert difference.coeff(E,2)==0
    assert difference.coeff(E,3)==0
    assert difference.coeff(E,4)!=0
metric_shift=E**2*(T*s.diff(g0,t)+U*s.diff(g0,x))
assert s.expand(metric_shift).coeff(E,2)!=0
print("PASS canonical spectator first nonzero T at epsilon^2 remains gauge unchanged")
print("PASS leading T shift epsilon^4 vs metric/solid background shift epsilon^2")
print("SCOPE zero spectator background and xi=O(epsilon^2), not general gauge proof")
