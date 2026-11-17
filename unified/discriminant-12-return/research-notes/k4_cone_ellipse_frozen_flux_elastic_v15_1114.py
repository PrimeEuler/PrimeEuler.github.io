#!/usr/bin/env python3
"""Gravity v15.1114: focus-locked cone ellipse as flux-frozen ideal conductor.

Explicit material affine map from a reference circular cylinder, ideal-MHD
E+v cross B=0, a positive elastic/kinetic action and the anchoring gate.
An ideal conductor/magnetized elastic medium is assumed; this does NOT
establish force balance, finite-wall surface current, or K4 tidal dynamics.
"""
import sympy as s
x,y,z,t=s.symbols('x y z t',real=True)
e=s.Function('e')(t)
C=s.symbols('C',positive=True)
D=1-e**2
A=C/D; B=C/s.sqrt(D); d=-C*e/D
q=(y-d)**2/A**2+z**2/B**2
v=s.Matrix([0,s.diff(d,t)+s.diff(A,t)/A*(y-d),s.diff(B,t)/B*z])
assert s.simplify(s.diff(q,t)+v[1]*s.diff(q,y)+v[2]*s.diff(q,z))==0
# x-directed potential: material level sets are frozen in.
psi=s.Function('amp')(x)*s.Function('F')(q)
Ex=-s.diff(psi,t); By=s.diff(psi,z); Bz=-s.diff(psi,y)
Bvec=s.Matrix([0,By,Bz]); Evec=s.Matrix([Ex,0,0])
assert (Evec+v.cross(Bvec)).applyfunc(s.simplify)==s.zeros(3,1)
assert s.simplify(s.diff(By,y)+s.diff(Bz,z))==0
# Cauchy frozen flux under affine deformation.
Jac=A*B/C**2
assert s.simplify((A/C)/Jac-C/B)==0
assert s.simplify((B/C)/Jac-C/A)==0
# For static derivatives replace time-dependent e(t) by real coordinate.
e=s.symbols('eta',real=True)
D=1-e**2; A=C/D; B=C/s.sqrt(D); d=-C*e/D
Ms=s.symbols('M_mat',positive=True)
Ae=s.diff(A,e); Be=s.diff(B,e); de=s.diff(d,e)
Mmat=s.factor(Ms*(de**2+(Ae**2+Be**2)/4))
assert s.simplify(Mmat.subs(e,0)-Ms*C**2)==0
# Uniform isotropic linearly elastic material, small-strain approximation.
lam,mu,V=s.symbols('lambda mu V',positive=True)
strain_y=A/C-1; strain_z=B/C-1
Uelastic=s.factor(V*(lam*(strain_y+strain_z)**2/2+
                      mu*(strain_y**2+strain_z**2)))
small=s.series(Uelastic,e,0,6).removeO()
assert s.simplify(s.expand(small)-
    V*e**4*(s.Rational(9,8)*lam+s.Rational(5,4)*mu))==0
assert s.simplify(s.diff(Uelastic,e,2).subs(e,0))==0
# Audited electromagnetic shape mass and magnetic energy (v15.1112).
K,csq=s.symbols('K csq',positive=True)
M_em=K*C**2/csq*(18+55*e**2+18*e**4)/(18*D**s.Rational(7,2))
U_B=K*(2-e**2)/(2*s.sqrt(D))
Iplus=-K*e**2/s.sqrt(D)
assert s.simplify(M_em.subs(e,0)-K*C**2/csq)==0
assert s.simplify(s.diff(U_B,e,2).subs(e,0))==0
assert s.simplify(s.diff(Iplus,e).subs(e,0))==0
# Anchor to a fixed reference: stiffness κ measured in energy/length².
kappa=s.symbols('kappa',positive=True)
Uanchor=kappa*d**2/2
assert s.simplify(s.diff(Uanchor,e,2).subs(e,0)-kappa*C**2)==0
M0=s.simplify((M_em+Mmat).subs(e,0))
omega2=s.simplify(s.diff(U_B+Uelastic+Uanchor,e,2).subs(e,0)/M0)
assert s.simplify(omega2-kappa/(Ms+K/csq))==0
# Standard TT EM coupling creates a parametric stiffness modulation.
h=s.symbols('h',real=True)
Ueff=U_B+Uelastic+Uanchor-h*Iplus/2
keff=s.simplify(s.diff(Ueff,e,2).subs(e,0))
assert s.simplify(keff-(kappa*C**2+h*K))==0
assert s.simplify(s.diff(Ueff,e).subs(e,0))==0
# Matter quadrupole in a separate, physically Fermi-frame description:
# Do not add its h_ddot tidal potential to a TT-gauge action naively.
Qmat=s.simplify(Ms*(d**2+(A**2-B**2)/4))
assert s.simplify(Qmat-s.Rational(5,4)*Ms*d**2)==0
assert s.simplify(s.diff(Qmat,e).subs(e,0))==0
# The compact axially varying magnetic field Bphi=f(x)b(r) produces
# an EM force JxB with nonzero curl: scalar pressure alone cannot balance.
rad=s.symbols('rad',positive=True)
fx=s.Function('f')(x); br=s.Function('b')(rad)
B2=fx**2*br**2
Fx=-s.diff(B2,x)/2
Fr=-s.diff(B2,rad)/2-B2/rad
curl_forcing=s.simplify(s.diff(Fr,x)-s.diff(Fx,rad))
assert s.simplify(curl_forcing+2*fx*s.diff(fx,x)*br**2/rad)==0
print('PASS frozen flux advection and ideal E+v cross B=0')
print('PASS material inertia, quartic elastic energy, anchor frequency')
print('PASS Fermi material quadrupole and pressure-only force-balance no-go')
print('M_mat(0):',Mmat.subs(e,0),'M_EM(0):',M_em.subs(e,0))
print('U_el leading:',small)
print('omega0^2:',omega2,'k_eff:',keff)
print('matter quadrupole:',Qmat)
print('force-balance curl:',curl_forcing)
