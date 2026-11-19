#!/usr/bin/env python3
"""Gravity v15.1226: physical Maxwell-to-ADM signs and corrected K4 compact-packet
initial scalar tide. Correct the accidentally omitted Jphi'' term in the
v15.1222 substitution, which also misled independent Audit Round 615.
Source-first P/Bardeen formulas: v15.728–729; local Riemann: v15.787.
Status: transverse-integrated longitudinal nonzero-k initial-slice
model, NOT a causal three-dimensional detector or a quarter-grid coupling.
"""
import sympy as s
T,k,eta,J=s.symbols('t k eta J',positive=True,real=True)
p=s.Function('P')(T)
jp,js,jb=[s.Function(x)(T) for x in ('JPhi','Jpsi','JB')]
beta=(8*eta*(1+k*k)-3*k*k)/3
force=3*s.sqrt(3)*js/(2*k*k*T**3)-9*(T*s.diff(jb,T)+jb)/(2*k**4*T**3)
pdd=-3*s.diff(p,T)/T-beta*p/T**2+force
pddd=s.diff(pdd,T).subs(s.diff(p,T,2),pdd)
Phi=(T*T*s.diff(p,T,2)+2*T*s.diff(p,T))/(3*(1+k*k))
Phi+=s.sqrt(3)*(jp+js)/(2*T*(1+k*k))-3*s.diff(jb,T)/(2*k*k*(1+k*k))
Psi=(k*k*p-T*s.diff(p,T))/(3*(1+k*k))
Psi+=s.sqrt(3)*jp/(2*T*(1+k*k))+3*jb/(2*k*k*T*(1+k*k))
S=-3*k*k*Phi/T**2
Araw=s.diff(Psi,T,2)+2*s.diff(Psi,T)/T+s.diff(Phi,T)/T
Aiso=Araw+S/3
Ared=s.factor(Aiso.subs(s.diff(p,T,3),pddd).subs(s.diff(p,T,2),pdd))
Ward=T*s.diff(jp,T)+s.sqrt(3)*jb+js
# The exact general sourced trace identity, BEFORE setting any source to a number.
assert s.simplify(Ared+s.sqrt(3)*(jp+js)/(2*T**3)
                  -s.sqrt(3)*s.diff(Ward,T)/(2*T*T*(1+k*k)))==0
# Genuine Maxwell initial Cauchy jet: energy conformal R''=-k²R,
# Jphi=a³rho with a signed matter-action coefficient, Jphi(t)=J/t
# times a conformal profile f(sqrt3 ln t). f'(0)=0, f''(0)=-k²f.
jet={s.diff(jp,T,2):(2-3*k*k)*J,
     s.diff(jp,T):-J,s.diff(js,T):-J,
     s.diff(jb,T):s.sqrt(3)*k*k*J,
     jp:J,js:J,jb:s.Integer(0)}
A0=s.factor(Ared.xreplace(jet).subs(T,1))
assert s.simplify(A0+s.sqrt(3)*J)==0
# Demonstrate precisely how the erroneous v15.1222 coefficient was obtained:
# erase the required Jphi'' before substituting the initial values.
falsejet=dict(jet);falsejet[s.diff(jp,T,2)]=s.Integer(0)
Abad=s.factor(Ared.xreplace(falsejet).subs(T,1))
assert s.simplify(Abad-s.sqrt(3)*J*(k*k-4)/(2*(1+k*k)))==0
assert s.simplify(Abad.subs(k,2))==0
assert s.simplify(A0.subs(k,2))!=0
zeroP={p:0,s.diff(p,T):0,js:J,jb:0,
       s.diff(jb,T):s.sqrt(3)*k*k*J,jp:J,s.diff(jp,T):-J}
Phi0=s.factor(Phi.subs(s.diff(p,T,2),pdd).xreplace(zeroP).subs(T,1))
S0=s.factor(-3*k*k*Phi0)
assert s.simplify(S0-3*s.sqrt(3)*J*(k*k+2)/(2*(1+k*k)))==0
# Maxwell action variation, archived metric signature (+---):
# g00=1+2Phi; g0z=-a Bz; gxx=gyy=-a²(1-2psi);
# gzz=-a²(1-2psi-2Ezz). F01=e and F31=b.
a,e,b,ph,ps,ez,bz=s.symbols('a e b ph ps ez bz',real=True,positive=True)
g=s.diag(1,-a*a,-a*a,-a*a)
h=s.Matrix([[2*ph,0,0,-a*bz],[0,2*a*a*ps,0,0],
            [0,0,2*a*a*ps,0],[-a*bz,0,0,2*a*a*(ps+ez)]])
gi=g.inv();dgi=-gi*h*gi
F=s.zeros(4);F[0,1]=e;F[1,0]=-e;F[3,1]=b;F[1,3]=-b
f2=s.trace(F*gi*F*gi)
df=s.trace(F*dgi*F*gi+F*gi*F*dgi)
L1=s.factor(a**3*s.Rational(1,4)*(s.trace(gi*h)*f2/2+df))
rho=e*e/(2*a*a)+b*b/(2*a**4)
assert s.simplify(L1+a**3*rho*(ph+ps+ez)+e*b*bz)==0
# Thus JPhi=Jpsi=-a³rho, Ezz coefficient -a³rho, and Bz=-eb.
# Einstein R00 trace: Aiso=+rho/3 for kappa=1, with a0=1/sqrt3.
a0=1/s.sqrt(3)
assert s.simplify((-s.sqrt(3)*J).subs(J,-a0**3*rho)-rho/3)==0
# Initial K4 STF for the compact source Fourier coefficient:
# J(z)=-sqrt3*R0*g(z), width c=1 in kappa*C=1 units.
# (k²+2)/(k²+1)=1+1/(k²+1), inverse Fourier kernel
# K(z)=exp(-abs(z))/2, not the original compact envelope alone.
u=s.symbols('u',real=True)
gpoly=(1-u*u)**6
G=s.integrate(gpoly,(u,0,1))
Y0=s.integrate(s.exp(-u)*gpoly,(u,0,1))
Ybar=s.integrate((1-s.exp(-1)*s.cosh(u))*gpoly,(u,0,1))
# Normalize conformal transverse-integrated energy central value R0=1.
Scenter=-s.Rational(9,2)*(1+Y0)
Sbar=-s.Rational(9,2)*(G+Ybar)
Acenter=s.Integer(3);Abar=3*G
diff=s.factor(Abar-Acenter+2*Sbar/3+Scenter/3)
assert s.simplify(G-s.Rational(1024,3003))==0
assert abs(float(s.N(diff,36))+5.5533053868748155)<1e-12
assert abs(float(s.N(diff/Scenter,36))-0.9644213752034902)<1e-12
print('PASS physical +--- Maxwell signs and complete scalar Ward trace')
print('PASS original source second jet repairs v15.1222 spurious k=2 zero')
print('A_iso(1) =',A0,'incorrect omitted-derivative result =',Abad)
print('S_K4(k,1) =',S0)
print('PASS compact k!=0 initial STF Yukawa inverse Fourier and finite spatial proxy')
print('width=1, source R0=1: STF_center=',s.N(Scenter,16),
      'full spatial-arm difference=',s.N(diff,16))
print('OPEN 3D source, k=0/background, true causal photon/mirror/clock detector')
