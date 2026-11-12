#!/usr/bin/env python3
"""v15.751: exact logarithmic-time spectral control and K4 free Weyl tails.

K4 classical coasting Euler modes are NOT a Yang-Mills Hamiltonian mass gap.
The weighted Sturm-Liouville operator is unitarily equivalent to the
free 1D Laplacian and has continuous spectrum [0,infty), not a gap.
Source-free Weyl electric amplitudes decay tau^-3 for all three sectors.
"""
import sympy as sp
z,t,t0,nu,k,eta=sp.symbols('z tau tau0 nu k eta',positive=True,real=True)
u_fun=sp.Function('u')
u_t=u_fun(sp.log(t/t0));f=u_t/t
log_second=sp.diff(u_fun(z),z,2).subs(z,sp.log(t/t0))
L=sp.diff(f,t,2)+3*sp.diff(f,t)/t+(1+nu**2)*f/t**2
assert sp.simplify(L-(log_second+nu**2*u_t)/t**3)==0
# U: L2((0,infty),tau d tau) -> L2(R,dx), (Uf)(x)=tau f(tau)
A=-(t*t*sp.diff(f,t,2)+3*t*sp.diff(f,t)+f)
assert sp.simplify(A+log_second/t)==0
ell=sp.log(t/t0);free=sp.cos(nu*ell)/t
assert sp.simplify(sp.diff(free,t,2)+3*sp.diff(free,t)/t+(1+nu**2)*free/t**2)==0
nuS2=(8*eta-3)*(1+k*k)/3
nuV2=2*eta*(4+3*k*k)/3-1
nuT2=3*k*k+8*eta/3-1
assert sp.simplify((nuT2-nuV2)-3*(nuV2-nuS2))==0
cV2=2*eta/3;cL2=-sp.Rational(1,3)+8*eta/9
assert sp.simplify((1-cV2)-3*(cV2-cL2))==0
a=t/sp.sqrt(3)
ES=sp.factor(k*k/(2*a*a)*(t*t*sp.diff(free,t,2)+t*sp.diff(free,t)+k*k*free)/(3*(1+k*k)))
b=4*t/(sp.sqrt(3)*(4+3*k*k))
EV=sp.factor(-sp.I*k*sp.diff(b*sp.diff(free,t),t)/(4*a))
ET=sp.factor((t*t*sp.diff(free,t,2)+t*sp.diff(free,t)-3*k*k*free)/(12*a*a))
c=sp.cos(nu*ell);s=sp.sin(nu*ell)
expected=[
 k*k*((1+k*k-nu**2)*c+2*nu*s)/(2*(1+k*k)),
 sp.I*k*((nu**2-1)*c-2*nu*s)/(4+3*k*k),
 ((1-3*k*k-nu**2)*c+2*nu*s)/4]
for obs,r in zip((ES,EV,ET),expected):
    assert sp.simplify(t**3*obs-r)==0
case={eta:sp.Rational(3,4),k:sp.Integer(2)}
assert [sp.simplify(v.subs(case)) for v in (nuS2,nuV2,nuT2)]==[5,7,13]
for v in (nuS2,nuV2,nuT2):
    assert sp.limit(sp.sqrt((1+v).subs(case))/t,t,sp.oo)==0
print("PASS exact U A U^-1=-d_x^2, spectrum [0,infty)")
print("PASS conventional elasticity frequency-gap ratio 3")
print("PASS scalar/vector/tensor free electric Weyl = tau^-3 times bounded log oscillations")
print("PASS physical instantaneous frequency scales approach zero")
print("example nu_S^2,nu_V^2,nu_T^2=5,7,13")
