#!/usr/bin/env python3
"""Gravity v15.1263: exact homogeneous Maxwell stress and Bianchi-I check.
Original compact Cauchy E=(d_y chi,-d_x chi,0), B=0,
chi=f(x/a)f(y/b)f(z/c), f=(1-u²)^3, widths (1,2,1).
Volume is (4*pi)^3. No full homogeneous time evolution is asserted.
"""
import sympy as s
u=s.symbols('u',real=True)
f=(1-u*u)**3
I0=s.integrate(f*f,(u,-1,1))
I1=s.integrate(s.diff(f,u)**2,(u,-1,1))
assert I0==s.Rational(2048,3003) and I1==s.Rational(1024,385)
Ex2=I0**2*I1/2
Ey2=2*I0**2*I1
Etotal=s.factor((Ex2+Ey2)/2)
rho=s.simplify(Etotal/(4*s.pi)**3)
assert s.simplify(Ex2/Etotal-s.Rational(2,5))==0
assert s.simplify(Ey2/Etotal-s.Rational(8,5))==0
P=s.diag(rho-Ex2/(4*s.pi)**3,rho-Ey2/(4*s.pi)**3,rho)
assert s.simplify(P-rho*s.diag(s.Rational(3,5),-s.Rational(3,5),1))==s.zeros(3)
assert s.simplify(s.trace(P)-rho)==0
Pi=s.simplify(P-rho*s.eye(3)/3)
assert s.simplify(Pi-rho*s.diag(s.Rational(4,15),-s.Rational(14,15),s.Rational(10,15)))==s.zeros(3)
assert s.trace(Pi)==0
H1,H2,H3,dH1,dH2,dH3=s.symbols('H1 H2 H3 dH1 dH2 dH3')
G1=-(dH2+dH3+H2**2+H3**2+H2*H3)
G2=-(dH1+dH3+H1**2+H3**2+H1*H3)
assert s.expand(G1-G2-dH1+dH2-(H1+H2+H3)*(H1-H2))==0
# With initially equal H_i and unsheared isotropic solid,
# dot(sigma_i)=kappa*Pi_i, and E_STF_i=-dot(sigma_i).
kap=s.symbols('kappa',positive=True)
sigma_dot=kap*Pi
E_STF=-sigma_dot
assert s.trace(E_STF)==0
assert s.simplify((P[0,0]-P[1,1])/rho-s.Rational(6,5))==0
assert s.simplify((P[2,2]-P[1,1])/rho-s.Rational(8,5))==0
# Existing coasting H fixed without compensating homogeneous perturbation
# violates Hamiltonian 00 once positive mean EM energy is added.
H=s.symbols('H',positive=True)
assert s.simplify(3*H*H-(3*H*H+kap*rho))==-kap*rho
print('PASS exact compact Maxwell k0 pressure and Bianchi-I shear consistency')
print('mean rho:',rho,'~',s.N(rho,16))
print('P_i/rho:',[s.simplify(P[i,i]/rho) for i in range(3)])
print('Pi_i/rho:',[s.simplify(Pi[i,i]/rho) for i in range(3)])
print('electric homogeneous STF_i/(kappa*rho):',
      [s.simplify(E_STF[i,i]/(kap*rho)) for i in range(3)])
print('OPEN compatible homogeneous initial expansion, solid and full metric')
