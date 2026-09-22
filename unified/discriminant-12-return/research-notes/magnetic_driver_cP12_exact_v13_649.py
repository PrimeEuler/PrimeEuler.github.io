#!/usr/bin/env python3
"""Exact g^11/g^12 Dyson-log reduction to c_P,12(j)."""
import sympy as s
x,j=s.symbols('x j'); pi=s.pi
hx11=s.Rational(8445707,83494164234240)
hz12=s.Rational(31839895957,601157982486528000)
a10=-2*hx11; z11=-2*hz12
A=1-x/s.Integer(64)-3*x**2/s.Integer(2048)-341*x**3/s.Integer(3145728)-21745*x**4/s.Integer(3623878656)+a10*x**5
Q=s.Rational(1,8)+x/s.Integer(128)+61*x**2/s.Integer(196608)+937*x**3/s.Integer(452984832)-s.Rational(5033593,5218385264640)*x**4+z11*x**5
S=s.series(A*A+x*Q*Q,x,0,7).removeO()
F=s.series(s.sqrt(S),x,0,7).removeO()
p=s.series(A*A/S*s.cos(pi*(F-1)/2)**2,x,0,7).removeO().expand()
y=s.expand(1-p)
inf=sum((-1)**(k+1)*s.binomial(2*j,k)*y**k for k in range(1,7))
c12=s.factor(s.expand_func(s.series(inf,x,0,7).removeO().expand().coeff(x,6)))
print("hx11 =",hx11); print("hz12 =",hz12); print("a10 =",a10); print("z11 =",z11)
print("cP12 =",c12)
targets={s.Rational(1,2):s.Float('-2.46969713073e-8',30),s.Integer(1):s.Float('-1.47726959691e-7',30),s.Rational(3,2):s.Float('-3.04719066730e-7',30)}
for jj,t in targets.items():
    v=s.N(c12.subs(j,jj),30)
    print("j",jj,"analytic",v,"target",t,"difference",s.N(v-t,15))
