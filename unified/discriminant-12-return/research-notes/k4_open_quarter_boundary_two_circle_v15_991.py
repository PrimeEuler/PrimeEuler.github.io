#!/usr/bin/env python3
"""v15.991: original-unit-step q=2 projected open ladder, NOT
the closed 2D SU2 co-scaled representation of v15.989.
Reproduces v15.602 cross-shell boundary bridge T*T=2E; contrasts
conditional dynamical exchange and free physical coupling.
"""
import sympy as s
for L in range(3,16):
    j=s.Rational(L,4)
    jp=j+s.Rational(1,2)
    w=s.Rational(L+1,4)
    A=s.zeros(L+1)
    M=s.diag(*[-j+s.Rational(i,2) for i in range(L+1)])
    for i in range(L-1):
        m=-j+s.Rational(i,2)
        A[i+2,i]=s.sqrt((j-m)*(j+m+1))
    Am=A.T
    E=s.simplify(j*(j+1)*s.eye(L+1)-(A*Am+Am*A)/2-M*M)
    T=s.zeros(L+3,L+1)
    T[0,1]=s.sqrt(w)
    T[L+2,L-1]=s.sqrt(w)
    assert s.simplify(T.T*T-2*E)==s.zeros(L+1)
    assert E.rank()==2 and T.rank()==2
    assert all(s.simplify(E[i,i]-(w/2 if i in (1,L-1) else 0))==0 for i in range(L+1))
    assert s.simplify((jp+s.Rational(1,2))-(j+s.Rational(1,2))-s.Rational(1,2))==0
    assert s.simplify(jp*(jp+1)-j*(j+1)-j-s.Rational(3,4))==0
    # odd/even shell parity unchanged: L' = L+2
    assert (L+2)%2==L%2
    if L==3:
        assert E==s.diag(0,s.Rational(1,2),s.Rational(1,2),0)
        assert (j,jp)==(s.Rational(3,4),s.Rational(5,4))
# If physical coupling g and detuning delta are independently supplied,
# each 2-level edge pair has Rabi frequency sqrt(delta^2+4*g^2*w).
g,delta,t=s.symbols('g delta t',real=True)
w=s.symbols('w',positive=True)
H=s.Matrix([[-delta/2,g*s.sqrt(w)],[g*s.sqrt(w),delta/2]])
assert s.simplify(H**2-(delta**2/4+g**2*w)*s.eye(2))==s.zeros(2)
prob=(4*g*g*w/(delta*delta+4*g*g*w))*s.sin(t*s.sqrt(delta**2+4*g*g*w)/2)**2
assert s.simplify(prob.subs(g,0))==0
print('PASS q2 original-step open ladder L=3..15; T†T=2E, 2-circle R shift, parity, conditional Rabi.')
