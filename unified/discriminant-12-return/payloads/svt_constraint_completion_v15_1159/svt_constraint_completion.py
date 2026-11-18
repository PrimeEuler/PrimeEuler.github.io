#!/usr/bin/env python3
"""
svt_constraint_completion.py -- item 3, second half (sandbox,
2026-11-18): solve the scalar/vector ADM constraints on the
initial slice for v15.1085's compact-Maxwell longitudinal
Fourier mode, completing the electric Weyl beyond
v15.1083's TT-only jet (the gap v15.1085 Gate 911 filed).

Filed sources (v15.1085 Gate 909, wavevector q || z, initial
slice, conformal orthonormal components):
  T00 = R,  T0i = 0,  Tij = diag(P, -P, R),
  P/R = (b^2-a^2)/(b^2+a^2)  (3/5 at a:b = 1:2; 0 at a = b),
  TT projection diag(P, -P, 0);  trace Tii = R (EM stress
  traceless: -T00 + Tii = 0);  scalar STF S_L = 2R/3.
Filed Ward jet (Gate 910): R'(0) = 0, S_z'(0) = -i q R,
R''(0) = -q^2 R.  Filed TT jet (v15.1083):
W_+(q,0) = kappa P0 / (2 a0^4).

Method (standard linearized ADM/Newtonian-gauge GR,
IMPORTED; conventions stated once): longitudinal gauge
ds^2 = a^2[-(1+2Phi) deta^2 + (1-2Psi) dx^2], signature
(-,+,+,+), G = kappa T, conformal densities as filed
(physical stresses carry a^-4; constraint sources enter
with a^-2 in conformal form, matching v15.1083's source
scaling). At eta = 0 the momentum constraint with
T0i = 0 gives Psi' + H Phi = 0, eliminating the H terms
from the Hamiltonian constraint:
  Psi(q,0)  = -kappa a0^-2 R / (2 q^2).
The traceless longitudinal ij equation with scalar
anisotropic stress Pi^S (Tij_STF = (zhat zhat - I/3) Pi^S,
so Pi^S = (3/2) S_L = R):
  Phi - Psi = -kappa a0^-2 Pi^S / q^2 = -kappa a0^-2 R/q^2.
Scalar electric Weyl (tidal) for the mode:
  E^S_ij = -(1/(2 a^2)) (di dj - delta_ij nabla^2/3)(Phi+Psi).
Vector sector: transverse momentum constraint is
homogeneous with zero source for this data at eta = 0
(v15.1085: vector momentum and anisotropy vanish on the
initial slice for this orientation) -> vector potential
and vector Weyl vanish at eta = 0 for this data.
"""
import sympy as sp

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

q, R, P, kappa, a0 = sp.symbols("q R P kappa a0", positive=True)
i = sp.I

# C1: SVT split of the filed stress
T = sp.diag(P, -P, R)
trace = sp.trace(T)
iso = (trace / 3) * sp.eye(3)
STF = T - iso
TT = sp.diag(P, -P, 0)
# scalar STF for q||z is (zhat zhat - I/3) Pi^S; its zz entry:
SL = STF[2, 2]
check("C1a trace Tii = R (EM traceless: -T00+Tii = 0)",
      sp.simplify(trace - R) == 0)
check("C1b scalar STF S_L = Tzz - Tii/3 = 2R/3 (nonzero even at P=0)",
      sp.simplify(SL - 2 * R / 3) == 0)
_dec = (iso + sp.diag(-(2 * R / 3) / 2, -(2 * R / 3) / 2, 2 * R / 3) + TT) - T
check("C1c stress = isotropic + scalar STF + TT, TT zz entry = 0",
      all(sp.simplify(e) == 0 for e in _dec) and TT[2, 2] == 0)

# C2: Ward jet re-verification (Gate 910 algebra)
eta = sp.symbols("eta")
Rf = sp.Function("R")(eta); Sz = sp.Function("Sz")(eta)
# equations: R' = -i q Sz ; Sz' = -i q Tzz, Tzz(0)=R0, Sz(0)=0
R0 = sp.symbols("R0", positive=True)
Szp0 = -i * q * R0
Rp0 = -i * q * 0
Rpp0 = -i * q * Szp0
check("C2 Ward jet: R'(0)=0, Sz'(0)=-iqR, R''(0)=-q^2 R",
      Rp0 == 0 and sp.simplify(Szp0 + i * q * R0) == 0
      and sp.simplify(Rpp0 + q**2 * R0) == 0)

# C3: constraint solve at eta = 0
Psi = -kappa * a0**-2 * R / (2 * q**2)
PiS = sp.Rational(3, 2) * SL          # = R
Phi_minus_Psi = -kappa * a0**-2 * PiS / q**2
Phi = Psi + Phi_minus_Psi
check("C3a Pi^S = (3/2) S_L = R", sp.simplify(PiS - R) == 0)
check("C3b Phi = 3 Psi (anisotropic stress splits the potentials)",
      sp.simplify(Phi - 3 * Psi) == 0)
PhiPlusPsi = sp.simplify(Phi + Psi)
check("C3c Phi + Psi = -2 kappa a0^-2 R / q^2 (forced by R, not P)",
      sp.simplify(PhiPlusPsi + 2 * kappa * a0**-2 * R / q**2) == 0)

# C4: scalar electric Weyl at eta = 0 for the mode e^{iqz}
# E^S_ij = -(1/(2 a0^2)) (di dj - delta_ij nabla^2/3)(Phi+Psi);
# di dj -> -q_i q_j ; nabla^2 -> -q^2 ; q = (0,0,q)
def E_scalar(ii):
    qi = q if ii == 2 else 0
    return sp.simplify(-(1 / (2 * a0**2)) * (-qi * qi + q**2 / 3) * PhiPlusPsi)
Ezz, Exx = E_scalar(2), E_scalar(0)
check("C4a E^S_zz = -2 kappa R / (3 a0^4)", sp.simplify(Ezz + 2 * kappa * R / (3 * a0**4)) == 0)
check("C4b E^S_xx = E^S_yy = +kappa R / (3 a0^4); scalar Weyl traceless",
      sp.simplify(Exx - kappa * R / (3 * a0**4)) == 0
      and sp.simplify(2 * Exx + Ezz) == 0)

# C5: completed vs TT-only at the filed ratios
Wplus = kappa * P / (2 * a0**4)     # v15.1083 initial TT jet (xx)
Exx_total = sp.simplify(Wplus + Exx)
ratio_12 = sp.simplify(Exx_total.subs(P, sp.Rational(3, 5) * R) / (kappa * R / a0**4))
check("C5a at a:b=1:2 (P=3R/5): completed E_xx = (19/30) kappa R/a0^4 "
      "vs TT-only (3/10)", ratio_12 == sp.Rational(19, 30))
check("C5b at a=b (P=0): TT jet vanishes, scalar tide survives: "
      "E_zz = -2 kappa R/(3 a0^4) != 0",
      sp.simplify(Wplus.subs(P, 0)) == 0 and sp.simplify(Ezz) != 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
