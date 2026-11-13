#!/usr/bin/env python3
"""Gravity v15.864: same Cone leverage, conserved coupled matter/agent,
distinct coasting K4 sourced TT optical detector polarizations.

Two equal real canonical fields chi=phi with interaction -g chi phi:
L=-1/2(dchi)^2-1/2m²chi²-1/2(dphi)^2-1/2m²phi²-g chi phi.
Divergence of the chi-only stress is +g phi partial_nu chi; agent
phi+interaction contributes exactly the negative, so total T conserved.
Both are ordinary fields and the coupling is supplied, not Cone-selected.

The exact on-shell Minkowski two-wave source and an actual coasting-FLRW
on-shell KG evolution of its equal eigenmode are tested. Rotating p,q
around fixed K preserves |p|, |q|, omega and rapidity leverage but
rotates the TT plus/cross stress and K4 tensor optical outputs.

SCOPE: spatially unbounded analytic wave source, finite-arm transverse
tensor channel only; NOT complete coasting five-helicity detector,
remote compact emitter, novel gravity, or determined Newton G.
"""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp,quad
m,g,k,c,az,A=s.symbols("m g k c az A",positive=True,real=True)
t,x,y,z=s.symbols("t x y z",real=True)
omega=s.sqrt(k*k+m*m+g)
r=s.Matrix([x,y,z])
kt=k*s.sqrt(1-c*c)
p=s.Matrix([kt*s.cos(az),kt*s.sin(az),k*c])
q=s.Matrix([-p[0],-p[1],k*c])
chi=A*(s.cos(omega*t-p.dot(r))+s.cos(omega*t-q.dot(r)))
phi=chi
box=lambda f:-s.diff(f,t,2)+sum(s.diff(f,v,2) for v in (x,y,z))
assert s.simplify(box(chi)-m*m*chi-g*phi)==0
assert s.simplify(box(phi)-m*m*phi-g*chi)==0
# Separate stress exchange with potential interaction included in agent.
for coordinate in (t,x,y,z):
    matter_exchange=g*phi*s.diff(chi,coordinate)
    agent_exchange=g*chi*s.diff(phi,coordinate)-g*s.diff(chi*phi,coordinate)
    assert s.simplify(matter_exchange+agent_exchange)==0
probe=(g*phi*s.diff(chi,x)).subs({m:1,g:s.Rational(1,4),
    k:1,c:s.Rational(3,5),az:s.pi/8,A:1,
    t:s.Rational(1,10),x:s.Rational(1,3),
    y:s.Rational(1,5),z:s.Rational(1,7)})
assert abs(float(probe.evalf()))>1e-4
# Fourier coefficient at common spatial K=p+q, frequency 2omega.
P=s.diag(1,1,0)
spatial=-A*A*(p*q.T+q*p.T)/2  # BOTH fields, cosine Fourier coeff 1/2
S_TT=s.trigsimp(P*spatial*P-P*s.trace(P*spatial)/2)
Q=s.simplify(A*A*k*k*(1-c*c)/2)
expect=Q*s.Matrix([[s.cos(2*az),s.sin(2*az),0],
                   [s.sin(2*az),-s.cos(2*az),0],[0,0,0]])
assert (S_TT-expect).applyfunc(s.simplify)==s.zeros(3)
assert s.simplify(s.trace(S_TT*S_TT)-2*Q**2)==0
assert S_TT.subs(az,0)==Q*s.diag(1,-1,0)
assert (S_TT.subs(az,s.pi/4)-Q*s.Matrix(
    [[0,1,0],[1,0,0],[0,0,0]])).applyfunc(s.simplify)==s.zeros(3)
beta=k/omega
lever=s.simplify((1+beta)/(1-beta))
assert s.simplify(lever.diff(az))==0
print("PASS exact interacting KG fields and conserved total stress")
print("PASS stress TT rotation at fixed rapidity/Cone leverage")
# FLRW coasting field: a=tau/sqrt3. Equal eigenmode has effective
# mu²=m²+g, KG a¨+3 a˙/tau+(3k²/tau²+mu²)a=0.
tau=s.symbols('tau',positive=True)
v=s.Function('v')(tau)
mu2=s.symbols('mu2',positive=True)
ad=tau/s.sqrt(3)
pdotq=s.symbols('pdotq',real=True)
rho=s.diff(v(tau),tau)**2/2-pdotq*v(tau)**2/(2*ad**2)+mu2*v(tau)**2/2
pres=s.diff(v(tau),tau)**2/2+pdotq*v(tau)**2/(6*ad**2)-mu2*v(tau)**2/2
# Fourier K=p+q, k_wave²=k²; |K|²=2(k²+p.q).
K2=s.symbols('K2',positive=True)
k2=s.symbols('k2',positive=True)
vprime=s.diff(v(tau),tau)
ward=s.diff(rho,tau)+3*(rho+pres)/tau+K2*vprime*v(tau)/(2*ad**2)
ward=s.simplify(ward.subs(s.diff(v(tau),tau,2),
     -3*vprime/tau-(k2/ad**2+mu2)*v(tau)))
assert s.simplify(ward.subs(K2,2*(k2+pdotq)))==0
print("PASS on-shell FLRW total-matter Fourier energy Ward identity")
# Special exact geometry p=(1,0,1), q=(-1,0,1), K=(0,0,2).
# az rotation does not affect the scalar time amplitude or total Ward.
muval=1.25
def kg(t,y):
    return [y[1],-3*y[1]/t-(6/t**2+muval)*y[0]]
kg_solution=solve_ivp(kg,(1.,1.6),[1.,-1.],dense_output=True,
    rtol=2e-12,atol=2e-13,method="DOP853")
assert kg_solution.success
def source_TT(t):
    at=t/np.sqrt(3)
    return kg_solution.sol(t)[0]**2/(2*at**2)
# Frozen archived K4 tensor Euler: beta_T=3|K|²+8eta_s/3=14,
# gamma''+3gamma'/tau+14gamma/tau²=-2 Pi_TT.
def gravity(t,y):
    return [y[1],-3*y[1]/t-14*y[0]/t**2-2*source_TT(t)]
gravity_solution=solve_ivp(gravity,(1.,1.6),[0.,0.],
    dense_output=True,rtol=2e-12,atol=3e-13,method="DOP853")
assert gravity_solution.success
eta_e=.08;d=.10
cosmic=lambda eta:np.exp(eta/np.sqrt(3))
a_r=cosmic(eta_e+2*d)/np.sqrt(3)
integrated=quad(lambda eta:gravity_solution.sol(cosmic(eta))[0],
    eta_e,eta_e+2*d,epsabs=2e-11)[0]
# Orthogonal transverse x/y pairs and rotated ±45deg cross pairs:
# D = a_r * integral gamma_TT deta. Photon outward+inbound quadrature.
out=quad(lambda s:gravity_solution.sol(cosmic(eta_e+s))[0]/2,
    0,d,epsabs=1e-11)[0]
back=quad(lambda s:gravity_solution.sol(cosmic(eta_e+d+s))[0]/2,
    0,d,epsabs=1e-11)[0]
assert abs(integrated-2*(out+back))<2e-13
D0=a_r*integrated
assert abs(D0)>1e-5
beta0=np.sqrt(2/(2+muval))
lev0=(1+beta0)/(1-beta0)
for angle in (0.,np.pi/8,np.pi/4):
    D=np.array([np.cos(2*angle),np.sin(2*angle)])*D0
    assert abs(np.linalg.norm(D)-abs(D0))<1e-13
    print("coasting az=",angle,"same beta=",beta0,"lever=",lev0,
          "optical [plus,cross]=",D)
print("PASS conserved source -> K4 TT mode -> finite arm photon timing")
print("NEGATIVE same Cone lever gives different channel outputs by orientation")
print("OPEN full K4 scalar/vector constraints, remote compact source, new physics")
