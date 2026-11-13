#!/usr/bin/env python3
"""Gravity v15.933: phase-sensitive q=2/bicone comparator.
An assumed sector-odd interaction is NOT derived from a gravity field.
Explicit exact SymPy checks plus independent SciPy Rabi propagation.
"""
import sympy as s
import numpy as np
from scipy.linalg import expm

sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-s.I],[s.I,0]])
sz=s.diag(1,-1)
g,delta,phi,t=s.symbols('g delta phi t',real=True)
H=delta*sz/2+g*(s.cos(phi)*sx+s.sin(phi)*sy)
assert sz*sx+sx*sz==s.zeros(2)
assert sz*sy+sy*sz==s.zeros(2)
ket=s.Matrix([1,0]); H0=H.subs(delta,0)
Ut=s.eye(2)*s.cos(g*t)-s.I*H0/g*s.sin(g*t)
psi=Ut*ket
Ux=s.trigsimp(s.simplify((s.conjugate(psi).T*sx*psi)[0]))
pop=s.trigsimp(s.simplify(s.conjugate(psi[1])*psi[1]))
assert s.trigsimp(Ux-s.sin(phi)*s.sin(2*g*t))==0
assert s.trigsimp(pop-s.sin(g*t)**2)==0
alpha=s.symbols('alpha',real=True)
V=s.diag(s.exp(-s.I*alpha/2),s.exp(s.I*alpha/2))
diff=(V*H*V.conjugate().T-H.subs(phi,phi+alpha)).applyfunc(lambda z:z.rewrite(s.exp))
assert s.simplify(s.expand_trig(diff))==s.zeros(2)
# E1 even sector bright state |e>, quarter sector |q>, ground |0>.
d,theta=s.symbols('d theta',real=True)
D=s.Matrix([[0,d,0],[d,0,0],[0,0,0]])
Chi=s.diag(1,1,-1)
assert Chi*D*Chi==D
ground=s.Matrix([1,0,0])
bright=s.Matrix([0,s.cos(theta),s.sin(theta)])
dark=s.Matrix([0,-s.sin(theta),s.cos(theta)])
Ab=(ground.T*D*bright)[0]
Ad=(ground.T*D*dark)[0]
assert Ab==d*s.cos(theta) and Ad==-d*s.sin(theta)
assert s.trigsimp(Ab**2+Ad**2-d*d)==0
for det,gg in [(0,.1),(.5,.1),(.5,.02)]:
    Om=np.hypot(gg,det/2)
    for time in (0.,1.,3.,8.):
        h=np.array([[det/2,gg],[gg,-det/2]],dtype=complex)
        p=expm(-1j*h*time)@np.array([1.,0.])
        assert abs(abs(p[1])**2-(gg/Om)**2*np.sin(Om*time)**2)<1e-12
    print('detuning',det,'g',gg,'Pmax',(gg/Om)**2)
print('PASS exact parity, phase-covariant Ux, E1 borrowed strength, ordinary Rabi')
