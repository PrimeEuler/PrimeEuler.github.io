#!/usr/bin/env python3
"""Gravity v15.1221 — exact K4 strain homogeneity, Maxwell active-tidal trace
and independent sign/provenance audit for the compact initial source.

Conventions: Einstein G_ab=kappa T_ab, signature (-,+,+,+),
R_{a0b0} orthonormal electric Riemann with tr(E)=R_00.
Physical Maxwell rho_phys=a^-4 rho_conformal.
Initial longitudinal STF constraints quoted from *standard GR*
Sandbox v15.1159 are an optional control, not a solved K4 STF sector.
No causal photon/mirror/clock calculation; no quarter-grid coupling.

Also repairs the prior v15.1198 final bare SymPy == check additively:
for symbolic expressions compare simplify(difference)==0.
"""
import sympy as s
x,y,z,eta,C,kap,a,R=s.symbols('x y z eta C kap a R',positive=True,real=True)
B=s.diag(x,y,z)
b=s.sqrt(x*y*z)
J=(x*x+y*y+z*z)/(x+y+z)**2-s.Rational(1,3)
F=C*b**s.Rational(2,3)*(1+eta*J)
degree=s.factor(x*s.diff(F,x)+y*s.diff(F,y)+z*s.diff(F,z)-F)
assert s.simplify(degree)==0
assert s.simplify(x*s.diff(J,x)+y*s.diff(J,y)+z*s.diff(J,z))==0
# In comoving local material frame T^mu_mu=-4F+2 B^IJ F_BIJ.
# rho=F, trace(T)=-rho+p1+p2+p3 ==> p1+p2+p3=-rho.
Ttrace=-4*F+2*(x*s.diff(F,x)+y*s.diff(F,y)+z*s.diff(F,z))
p_sum=s.simplify(Ttrace+F)
assert s.simplify(Ttrace+2*F)==0
assert s.simplify(p_sum+F)==0
# Einstein equation Ricci_00=kappa(T_00+T/2) in signature -+++.
# Background solid active density cancels; free EM is tracefree.
rhoEM,rhoK=s.symbols('rhoEM rhoK',real=True)
T00=rhoEM+rhoK
T=-2*rhoK # solid trace, Maxwell trace 0
Ricci00=s.expand(kap*(T00+T/2))
assert s.simplify(Ricci00-kap*rhoEM)==0
Aiso=Ricci00/3
# Compact initial Maxwell packet: normalized transverse-integrated conformal
# rho(z)=R0*(1-(z/c)^2)^6 on |z|<c, zero outside.
u,r=s.symbols('u r',real=True,positive=True)
g=(1-u*u)**6
G=s.factor(s.integrate(g,(u,0,r))/r)
assert s.simplify(s.diff(r*G,r)-g.subs(u,r))==0
assert s.limit(G,r,0)==1
assert s.simplify(G.subs(r,1)-s.Rational(1024,3003))==0
# For q!=0 initial-slice standard GR benchmark v15.1159:
S0=s.Rational(3,2)*kap*R/a**4 # STF full Riemann coefficient
W0=-kap*R/a**4
A0=kap*R/(3*a**4) # Einstein Ricci trace input
assert s.simplify(S0/W0+s.Rational(3,2))==0
assert s.simplify(A0/S0-s.Rational(2,9))==0
diff=s.expand((2*G+1)*S0/3+(G-1)*A0)
assert s.simplify(diff/S0-(8*G+1)/9)==0
assert s.factor((diff/S0).subs(r,1))==s.Rational(11195,27027)
assert s.factor((diff/S0).subs(r,s.Rational(1,2)))==s.Rational(9518623,13837824)
# Existing v15.1198 traveling source uses Jphi=+a^3 rho; at kappa C=1,
# a=tau/sqrt(3), so kappa rho/3=+sqrt(3) kappa J0 at tau=1 (kappa=1).
# Its declared A_iso=-sqrt(3) J0 is opposite. Do not silently reconcile.
J0=s.symbols('J0',real=True)
a0=1/s.sqrt(3)
source_Ricci_coeff=s.simplify((J0/a0**3)/3)
old_Aiso=-s.sqrt(3)*J0
assert s.simplify(source_Ricci_coeff+old_Aiso)==0
assert s.simplify(source_Ricci_coeff-old_Aiso)==2*s.sqrt(3)*J0
# Structural == issue repaired robustly: symbols may be algebraically equal
# without canonical structural equality after computing limits.
w=s.symbols('w',positive=True)
X=s.symbols('X')
geometric=((2*(s.exp(s.I*w)-1)/(s.I*w)+1)/3)*X
assert s.simplify(s.limit(geometric,w,0)-X)==0
print('PASS K4 exact degree-1 strain homogeneity and sum p_i=-rho')
print('PASS Einstein R00 source trace= kappa rho_EM, Aiso=kappa rho_EM/3')
print('PASS compact standard-GR initial spatial-proxy ratio (8G+1)/9')
print('ratio at r=1:',s.Rational(11195,27027))
print('SIGN AUDIT OPEN: v15.1198 Aiso=-sqrt3 J0 vs +sqrt3 J0 from Jphi=+a^3 rho in shared conventions')
print('OPEN K4 compact-packet nonzero-q STF and causal finite-arm detector')
