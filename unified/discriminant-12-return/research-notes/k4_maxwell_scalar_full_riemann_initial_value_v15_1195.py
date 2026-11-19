#!/usr/bin/env python3
"""Gravity v15.1195: pressure-corrected null Maxwell scalar to full Fermi Riemann.

Uses historic K4 v15.728/729 for P+Phi_N/Psi_N and v15.787's *corrected*
analytic full scalar electric Riemann (refer to additive repair v15.792).
Two boundary choices: eternal particular solution and constrained initial-
value solution at tau0=1 with P=Pdot=0. The Maxwell wave already exists at
tau0, so this is NOT a zero-past-source retarded experiment. Strict k>0.
"""
import sympy as s
tau,k,eta,J0=s.symbols('tau k eta J0',positive=True,real=True)
I=s.I
w=s.sqrt(3)*k
nu2=(8*eta-3)*(1+k*k)/3
lam=-1-I*w
D=lam**2+nu2
J=J0*tau**(-1-I*w)
JB=I*k*J
assert s.simplify(tau*s.diff(J,tau)+s.sqrt(3)*JB+J)==0
force=3*s.sqrt(3)*J/(2*k*k*tau**3)-9*(tau*s.diff(JB,tau)+JB)/(2*k**4*tau**3)
assert s.simplify(force+3*s.sqrt(3)*J/(k*k*tau**3))==0
Ppart=-3*s.sqrt(3)*J0*tau**(-2-I*w)/(k*k*D)
beta=nu2+1
assert s.simplify(s.diff(Ppart,tau,2)+3*s.diff(Ppart,tau)/tau+beta*Ppart/tau**2-force)==0
def potentials(P):
    Phi=(tau*tau*s.diff(P,tau,2)+2*tau*s.diff(P,tau))/(3*(1+k*k))
    Phi+=s.sqrt(3)*2*J/(2*tau*(1+k*k))-3*s.diff(JB,tau)/(2*k*k*(1+k*k))
    Psi=(k*k*P-tau*s.diff(P,tau))/(3*(1+k*k))
    Psi+=s.sqrt(3)*J/(2*tau*(1+k*k))+3*JB/(2*k*k*tau*(1+k*k))
    return Phi,Psi
Phi,Psi=potentials(Ppart)
a2=tau*tau/3
W=s.factor(k*k*(Phi+Psi)/(2*a2))
R=s.factor(-k*k*Phi/a2)
A=s.diff(Psi,tau,2)+2*s.diff(Psi,tau)/tau+s.diff(Phi,tau)/tau
norm=J0*tau**(-4-I*w)
CW=9*(I*(2*eta-3)*k-s.sqrt(3))/(4*eta*(1+k*k)-6*k*k+3*s.sqrt(3)*I*k)
assert s.simplify(W-CW*norm)==0
CR=s.factor(s.simplify(R/norm))
Cphi=s.factor(s.simplify(Phi/(J0*tau**(-2-I*w))))
assert s.simplify(CR+3*k*k*Cphi)==0
# Ricci completion: Q=nn-I/3, Weyl=W Q, Ricci_STF=(3Phi+Psi)k²/a² Q
Ricci_STF=k*k*(3*Phi+Psi)/a2
assert s.simplify(R-W+Ricci_STF/2)==0
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
assert s.trace(Q)==0 and s.trace(Q*Q)==s.Rational(2,3)
# Full Riemann electric matrix is A I +R nn; tracefree R Q.
Full=s.diag(A,A,A+R)
assert s.simplify(Full-s.eye(3)*s.trace(Full)/3-R*Q)==s.zeros(3)
# A bounded post-initial-slice response to Maxwell wave already populated at tau=1.
sig=s.symbols('sig',real=True)
nu=s.sqrt(nu2)
F0=-3*s.sqrt(3)*J0/k**2
z=F0/D*(s.exp(lam*sig)-s.cos(nu*sig)-lam*s.sin(nu*sig)/nu)
assert s.simplify(s.diff(z,sig,2)+nu2*z-F0*s.exp(lam*sig))==0
assert s.simplify(z.subs(sig,0))==0
assert s.simplify(s.diff(z,sig).subs(sig,0))==0
Pinitial=z.subs(sig,s.log(tau))/tau
assert s.simplify(Pinitial.subs(tau,1))==0
assert s.simplify(s.diff(Pinitial,tau).subs(tau,1))==0
Phir,Psir=potentials(Pinitial)
Rinitial=-k*k*Phir/a2
match=s.Rational(3,4)
kmatch=s.sqrt(s.Rational(1,2))
v=lambda e:complex(s.N(e.subs({eta:match,k:kmatch,J0:1}),14))
assert abs(v(CW)-complex(-3.7115374447904514,2.727411870290969))<1e-10
assert abs(v(CR)-complex(5.567306167185677,-0.909137290096453))<1e-10
print('Weyl transfer coefficient',v(CW))
print('full Riemann STF transfer coefficient',v(CR))
print('initial-value R_STF(tau=1)',complex(s.N(Rinitial.subs({eta:match,k:kmatch,J0:1,tau:1}),12)))
print('initial-value R_STF(tau=2)',complex(s.N(Rinitial.subs({eta:match,k:kmatch,J0:1,tau:2}),12)))
print('PASS corrected traceful full scalar Riemann, Ricci completion, finite initial-value Green solution')
print('OPEN source E-shear Ward, full Maxwell homogeneous component, compact apparatus, physical quarter coupling')
