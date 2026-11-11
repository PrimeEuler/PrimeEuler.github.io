#!/usr/bin/env python3
"""v15.681: independent finite-cavity check for the two distinct GW/EM resonances.

Dimensionless fixed-wall cavity z in [0,pi], c=omega_c=1.
This is an ideal prescribed-metric/direct-Maxwell model, not a covariant
elastic-wall detector model.
"""
import sympy as s
import numpy as np

z,K,Om,h,B0,t = s.symbols("z K Omega h B0 t", real=True)
Q,m = s.symbols("Q m", positive=True)
pi=s.pi
f=s.sqrt(2/pi)*s.sin(z)
assert s.integrate(f*f,(z,0,pi)) == 1
assert s.integrate(s.diff(f,z)**2,(z,0,pi)) == 1

# Seeded/direct-conversion channel: static transverse B background.
eps=s.symbols("eps", real=True)
a=s.Function("a")(t,z); b=s.Function("b")(t,z)
Ay=B0*z+eps*a
factor=s.exp(2*eps*b)
wave=s.diff(factor*s.diff(Ay,t),t)-s.diff(factor*s.diff(Ay,z),z)
linear=s.simplify(s.diff(wave,eps).subs(eps,0))
assert s.simplify(linear-(s.diff(a,t,2)-s.diff(a,z,2)-2*B0*s.diff(b,z))) == 0

# Galerkin overlap for b=h exp[i(Kz-Omega t)] and a=A(t) sin z.
J=s.simplify(2/pi*s.integrate(s.sin(z)*s.exp(s.I*K*z),(z,0,pi),conds="none"))
Jclosed=s.simplify(2/pi*(1+s.exp(s.I*pi*K))/(1-K*K))
assert s.simplify((J-Jclosed).rewrite(s.sin)) == 0
assert s.limit(Jclosed,K,1) == s.I
assert s.simplify(Jclosed.subs(K,0)-4/pi) == 0

# For A''+(1/Q)A'+A = 2 i h B0 K J exp(-i Omega t):
# peak deltaB/B0 = 2 h |K J|/D and peak deltaE/B0 = Omega times this.
D=s.sqrt((1-Om**2)**2+(Om/Q)**2)
Btransfer_without_overlap=2*h*K/D
Etransfer_without_overlap=Om*Btransfer_without_overlap
assert s.simplify(Btransfer_without_overlap.subs({K:1,Om:1})-2*h*Q) == 0
assert s.simplify(Etransfer_without_overlap.subs({K:1,Om:1})-2*h*Q) == 0

# Unseeded single-mode parametric channel.
# Full complex spatial overlaps for a traveling pump exp[i(Kz-Omega t)].
M=s.simplify(s.integrate(f**2*s.exp(s.I*K*z),(z,0,pi),conds="none"))
S=s.simplify(s.integrate(s.diff(f,z)**2*s.exp(s.I*K*z),(z,0,pi),conds="none"))
C=s.simplify(2*(S-M)+Om**2*M)
assert s.limit(M,K,0)==1 and s.limit(S,K,0)==1
assert s.limit(M,K,2)==-s.Rational(1,2)
assert s.limit(S,K,2)==s.Rational(1,2)
C2=s.simplify(C.subs(Om,2))
C2closed=4*s.I*(1-s.exp(s.I*pi*K))/(pi*K)
assert s.simplify(C2-C2closed)==0
assert s.limit(C2,K,0)==4
assert s.limit(C2,K,2)==0

# Timelike pump on the 2:1 resonance: Omega=2, K=sqrt(4-m^2).
Ck4=s.simplify(C2.subs(K,s.sqrt(4-m**2)))
assert s.limit(Ck4/m**2,m,0)==-s.Rational(1,2)

def jabs(k):
    if abs(k-1.0)<1e-12:
        return 1.0
    return abs(complex(s.N(Jclosed.subs(K,k))))

def seeded_B_ratio(w,q=100.0,hh=1e-8):
    # Massless traveling GR comparator K=Omega=w.
    den=np.sqrt((1-w*w)**2+(w/q)**2)
    return 2*hh*w*jabs(w)/den

print("seeded fixed-wall cavity, massless traveling comparator K=Omega")
for w in (.95,.99,1.0,1.01,1.05):
    print(f"Omega={w:.2f}: deltaB_peak/B0={seeded_B_ratio(w):.9e}")
print("parametric 2:1: C(K=0)=4, C(K=2)=0, C(K=sqrt(4-m^2))=-m^2/2+O(m^4)")
print("PASS: omega_c seeded resonance and 2 omega_c parametric resonance independently verified")
