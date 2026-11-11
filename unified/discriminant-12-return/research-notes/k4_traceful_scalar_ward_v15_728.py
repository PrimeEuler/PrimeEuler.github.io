#!/usr/bin/env python3
"""v15.728: traceful K4 scalar source Ward and pressure-corrected P forcing.
Uses time-dependent source EL identities independently derived from the
archived full EH+solid scalar action in v15.713. The direct spatial
metric source +J_psi psi was absent for tracefree stresses, but is
mandatory for canonical scalar matter.
"""
import sympy as s
t,k,eta=s.symbols("tau k eta",positive=True,real=True)
JP=s.Function("J_Phi")(t);JB=s.Function("J_B")(t)
JS=s.Function("J_psi")(t)
A=2*s.sqrt(3)*k**4*t**3/(27*(1+k*k))
beta=(8*eta*(1+k*k)-3*k*k)/3
Epsi=-t*s.diff(JP,t)-s.sqrt(3)*JB-JS
F=(k*k*t*s.diff(JP,t)+s.sqrt(3)*k*k*JB+
   s.sqrt(3)*t*s.diff(JB,t)+s.sqrt(3)*JB)/(3*(1+k*k))
Fr=s.factor(F.subs(s.diff(JP,t),-(s.sqrt(3)*JB+JS)/t))
assert s.simplify(Fr-(-k*k*JS+s.sqrt(3)*(t*s.diff(JB,t)+JB))/(3*(1+k*k)))==0
forcing=s.factor(-Fr/A)
expected=3*s.sqrt(3)*JS/(2*k*k*t**3)-9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3)
assert s.simplify(forcing-expected)==0
assert s.simplify(forcing.subs(JS,0)+9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3))==0
# Scalar metric source terms in +--- convention (original v14.935).
# delta g00=2Phi; delta g0z=i k a B in opposite Fourier mode;
# delta gij=2a^2 psi deltaij. Hence J_phi=a^3 rho,
# J_B=i k a^4 T^(0z), J_psi=a^3 spatial_trace.
rho=s.Function("rho")(t);flux=s.Function("T_0z")(t)
ptr=s.Function("spatial_trace")(t)
a=t/s.sqrt(3)
mJP=a**3*rho;mJB=s.I*k*a**4*flux;mJS=a**3*ptr
energy=s.diff(rho,t)+3*rho/t+s.I*k*flux+ptr/t
assert s.simplify(t*s.diff(mJP,t)+s.sqrt(3)*mJB+mJS-t*a**3*energy)==0
ct,G2=s.symbols("chi_t grad_sq",real=True)
cR=(ct**2+G2/a**2)/2
cTrace=(3*ct**2-G2/a**2)/2
assert s.simplify(cTrace-3*cR+2*G2/a**2)==0
assert cTrace.subs(G2,0)==3*ct**2/2
print("PASS: traceful scalar ADM source Ward = FLRW energy conservation")
print("PASS: pressure-corrected K4 physical scalar forcing",expected)
print("WARNING: complete traceful Weyl transfer must include J_psi")
