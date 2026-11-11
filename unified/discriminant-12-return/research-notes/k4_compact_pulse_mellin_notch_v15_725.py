#!/usr/bin/env python3
"""v15.725: a compact conserved common pulse can notch one K4 eigenfrequency.

Given smooth compact b0, D=tau d/dtau, choose
 b=(D^2-2D+1+nu_target^2)b0.
Its logarithmic Mellin transfer to postpulse Euler waves is multiplied
by nu_target^2-nu^2, so one sector can be exactly dark after the source
ends while other channels are excited. This is a source spectral-filter
identity, not a distinctive Cone gravity coupling.
"""
import sympy as s
from scipy.integrate import quad
from math import sqrt,log,sin,cos
x=s.symbols("x",positive=True,real=True)
nu,nu0=s.symbols("nu nu0",real=True)
weight=x**(-2-s.I*nu)
assert s.simplify(-s.diff(x*weight,x)/weight-(1+s.I*nu))==0
assert s.simplify((1+s.I*nu)**2-2*(1+s.I*nu)
                  +1+nu0**2-(nu0**2-nu**2))==0
assert s.simplify((-s.I*nu)*(-s.I*nu-1))!=0
# Compact C^5 numerical witness obtained by applying two derivatives
# to a C^7 polynomial bump. The Mellin zero theorem applies equally
# to a C_infinity compact bump.
D=lambda f:x*s.diff(f,x)
base=10000*(x-1)**8*(2-x)**8
notch=s.factor(D(D(base))-2*D(base)+6*base)
target=20000*(x-2)**6*(x-1)**6*(
    115*x**4-342*x**3+255*x**2-12*x+12)
assert s.factor(notch-target)==0
bpp=s.lambdify(x,s.diff(notch,x,2),"numpy")
k=2.;eta=.75;t=3.;kap=1.
qs=-1/6;qv=sqrt(1/18);qt=1/12;Dnum=4+3*k*k
nus={"scalar":sqrt(5),"vector":sqrt(7),"tensor":sqrt(13)}
cs={"scalar":-3*qs/(2*k*k),"vector":-2j*qv/k,
    "tensor":-2*kap*qt}
results={}
for name,v in nus.items():
    C=quad(lambda z:bpp(z)*cos(v*log(z)),1,2,epsabs=1e-9)[0]
    S=quad(lambda z:bpp(z)*sin(v*log(z)),1,2,epsabs=1e-9)[0]
    spectral=sqrt(C*C+S*S)
    ss=quad(lambda z:bpp(z)*sin(v*log(t/z)),1,2,epsabs=1e-9)[0]
    cc=quad(lambda z:bpp(z)*cos(v*log(t/z)),1,2,epsabs=1e-9)[0]
    y=cs[name]*ss/(v*t)
    yp=cs[name]*(cc-ss/v)/t**2
    ypp=-3*yp/t-(1+v*v)*y/t**2
    results[name]=(y,yp,ypp)
    assert spectral<1e-8 if name=="scalar" else spectral>1e-3
    print(name,"MELLIN_WEIGHT",spectral,"FREE_RESPONSE",y)
p,pd,pdd=results["scalar"]
fv,fvd,fvdd=results["vector"]
gt,gtd,gtdd=results["tensor"]
a=t/sqrt(3)
ES=k*k/(2*a*a)*(t*t*pdd+t*pd+k*k*p)/(3*(1+k*k))
EV=-1j*k*(4/(sqrt(3)*Dnum))*(fvd+t*fvdd)/(4*a)
ET=(t*t*gtdd+t*gtd-3*k*k*gt)/(12*a*a)
assert abs(ES)<1e-8
assert abs(EV)>1e-6 and abs(ET)>1e-6
print("PASS: scalar postpulse eigenmode notched but vector/tensor Weyl nonzero")
print("ELECTRIC_WEYL_AFTER_PULSE",ES,EV,ET)
print("CAUTION: exact zero relies on a tuned signed stress pulse")
