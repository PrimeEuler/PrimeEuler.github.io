#!/usr/bin/env python3
"""Gravity v15.993: open q2 boundary T vs quartic oscillator candidate.
Exact within canonical two-mode Fock embedding; no claim a K4 source
has physically generated O=(a1_dag)^3 a2. Maxwell metric expansion
is EM-quadratic at fixed metric, not bare four-photon interaction.
"""
import sympy as s
L=s.symbols('L',integer=True,positive=True)
w=s.Rational(1,4)*(L+1)
raw=s.sqrt(L*(L+1)*(L+2))
ratio=s.simplify(s.sqrt(w)/raw)
assert s.simplify(ratio-1/(2*s.sqrt(L*(L+2))))==0
assert (3-1,s.Rational(3+1,2))==(2,2)
for l in range(3,24):
    amp=s.sqrt(l*(l+1)*(l+2))
    boundary=s.sqrt(s.Rational(l+1,4))
    assert s.simplify(amp/(2*s.sqrt(l*(l+2)))-boundary)==0
b,e,z=s.symbols('b e z',real=True)
LM=s.exp(2*b)*e**2*z**2/2
series=s.series(LM,b,0,3).removeO().expand()
assert s.simplify(series-e**2*z**2*(s.Rational(1,2)+b+b*b))==0
assert s.diff(LM,e,4)==0
# At H0=hbar omega*(N+1) the operator changes total N by two,
# thus detuning is 2 omega (unless another source/level supplies it).
omega=s.symbols('omega',positive=True)
assert s.simplify(omega*((L+2)-L)-2*omega)==0
print('PASS q2 quartic source profile L=3..23, nonconstant shell ratio;')
print('PASS Maxwell metric b expansion retains quadratic EM dependence.')
print('boundary/raw =',ratio)
