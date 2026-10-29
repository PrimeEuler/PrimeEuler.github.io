#!/usr/bin/env python3
"""v15.111 handoff, part 2: constrained evaluation of the averaged quadratic
Hamiltonian source <H2> (v15.111 simplified form) on the source-corrected
v14.996 scalar solutions.

Method: execute scalar_final2.py's own solve chain verbatim (repo payload
bytes) in a namespace; take PhiS (lapse alpha), solB (shift scalar),
solpsi, solpsid from it; eliminate pi'' via the reduced oscillator
pi'' = -P pi' - Q pi, P = 3/t, Q = (3k^2+4)/t^2; re-verify the ORIGINAL
EL_B/EL_Phi residuals vanish on the reconstruction; then evaluate the
single-mode spatial averages in <H2> with the scalar_adm2 ansatz
dictionary and assemble the exact on-shell quadratic form in the free
data (pi, pi').

Mode dictionary (scalar_adm2 ansatz, perturbation amplitudes; cos/sin
single mode in z, <cos^2> = <sin^2> = 1/2, <cos sin> = 0):
  lapse field      alpha(x) = PhiS * cos(kz)
  metric scalar    psi(x)   = solpsi * cos(kz)
  shift covector   N_z = -a k B sin(kz)  =>  beta^z = N_z / a^2
                   = -(k/a) solB * sin(kz)          (linear order)
  theta = div beta = d_z beta^z = -(k^2/a) solB * cos(kz)
  triplet disp.    dphi(x)  = (pi/k) sin(kz)        (phi3 = z + dphi)
  div pi           = d_z dphi = pi * cos(kz)
  |grad pi|^2 avg  = (1/2) pi^2
  |psi_dot| etc.   cos-mode amplitudes solpsid.
Background: a = t/sqrt(3), conformal H = a'/a = 1/t, a^-2 = 3/t^2.
<H2> formula: v15.111 (simplified by the exact <theta^2 - Sij Sij> = 0
cancellation; independently verified in fourier_hessian_check.py;
formula itself verified by Audit R402).
"""
import sympy as sp

SRC = open("scalar_final2.py").read()
ns = {}
exec(compile(SRC, "scalar_final2.py", "exec"), ns)  # producer chain, verbatim

t, k = ns["t"], ns["k"]
pi_f = ns["pi"]; psi_f = ns["psi"]
dd = lambda f: sp.Derivative(f, t)
pdd = sp.Derivative(pi_f, (t, 2)); pd_ = dd(pi_f)
P, Q = ns["P"], ns["Q"]
assert sp.simplify(P - 3 / t) == 0 and sp.simplify(Q - (3 * k**2 + 4) / t**2) == 0
pdd_sol = -P * pd_ - Q * pi_f

solpsi = ns["solpsi"]
# solpsid from the producer still contains pi''; eliminate it on-shell
solpsid = sp.expand(ns["solpsid"].subs(pdd, pdd_sol))
solpsid = sp.simplify(sp.together(solpsid))
expect_psid = (-(k**2 + 2) * pd_ - ((3 * k**2 + 4) / t) * pi_f) / (3 * k**2 * (k**2 + 1))
assert sp.simplify(solpsid - expect_psid) == 0, "psi_dot closed form mismatch"
print("[D] psi     =", solpsi)
print("[D] psi_dot =", solpsid, " (pi'' eliminated; pi' coeff -> -2/(3k^2) as k->0: the v15.110 1/k^2 pole)")

def on_shell(expr):
    e = expr.subs({psi_f: solpsi, dd(psi_f): solpsid})
    e = sp.expand(e).subs(pdd, pdd_sol)
    return sp.simplify(sp.together(e))

alpha = on_shell(ns["PhiS"])          # lapse amplitude
Bsol = on_shell(ns["solB"])           # shift-scalar amplitude
print("[D] alpha =", alpha)
print("[D] B     =", Bsol)

# independent residual re-check: producer-identical computation
# (scalar_final2's own full_sub pattern, re-executed here)
EB0, EP0 = ns["EB0"], ns["EP0"]
_solpsid_raw = ns["solpsid"]
def full_sub(expr):
    e = expr.subs({psi_f: solpsi, dd(psi_f): _solpsid_raw})
    e = sp.expand(e).subs(pdd, pdd_sol)
    return sp.simplify(e)
rB = full_sub(EB0.subs({ns["Phi"]: ns["PhiS"].subs({psi_f: solpsi, dd(psi_f): _solpsid_raw}),
                        ns["B"]: ns["solB"]}))
rP = full_sub(EP0.subs({ns["Phi"]: ns["PhiS"].subs({psi_f: solpsi, dd(psi_f): _solpsid_raw}),
                        ns["B"]: ns["solB"]}))
print("[D] residual EL_B(orig) on reconstruction:", rB)
print("[D] residual EL_Phi(orig) on reconstruction:", rP)
assert rB == 0 and rP == 0

a = t / sp.sqrt(3)
H = 1 / t
theta = -(k**2 / a) * Bsol            # cos-mode amplitude of div beta
half = sp.Rational(1, 2)
avg = {
    "gradpsi2": half * k**2 * solpsi**2,
    "psid2": half * solpsid**2,
    "alpha_psid": half * alpha * solpsid,
    "psi_psid": half * solpsi * solpsid,
    "alpha2": half * alpha**2,
    "psi_theta": half * solpsi * theta,
    "psid_theta": half * solpsid * theta,
    "alpha_theta": half * alpha * theta,
    "pidot_minus_beta2": half * (pd_ / k + (k / a) * Bsol) ** 2,
    "matter": half * pi_f**2 + 2 * pi_f * solpsi + 6 * solpsi**2,
}
H2 = (-10 / a**2 * avg["gradpsi2"] + 6 * avg["psid2"]
      + 24 * H * (avg["alpha_psid"] - avg["psi_psid"]) + 18 * H**2 * avg["alpha2"]
      - 12 * H * avg["psi_theta"] + 4 * avg["psid_theta"] + 8 * H * avg["alpha_theta"]
      - sp.Rational(2, 3) * avg["pidot_minus_beta2"] - (2 / (3 * a**2)) * avg["matter"])
H2 = sp.simplify(sp.together(sp.expand(H2)))
print("[D] <H2>_on-shell =", H2)

# quadratic-form coefficients in the free data (pi, pi')
def coeff(e, x, y):
    return sp.simplify(sp.expand(e).coeff(x * y) if x != y else
                       sp.expand(e).coeff(x, 2))
c_pp = sp.simplify(H2.coeff(pi_f, 2))
rem = sp.expand(H2 - c_pp * pi_f**2)
c_pd = sp.simplify(rem.coeff(pd_, 1) / pi_f) if rem.coeff(pd_, 1) != 0 else sp.Integer(0)
# robust extraction: polynomial in (pi, pi') of degree 2
poly = sp.Poly(sp.expand(H2), pi_f, pd_)
c_pi2 = poly.coeff_monomial(pi_f**2)
c_pip = poly.coeff_monomial(pi_f * pd_)
c_pd2 = poly.coeff_monomial(pd_**2)
assert sp.simplify(H2 - (c_pi2 * pi_f**2 + c_pip * pi_f * pd_ + c_pd2 * pd_**2)) == 0
print("[D] quadratic form: <H2> = A*pi^2 + B*pi*pi' + C*pi'^2")
print("    A =", sp.factor(c_pi2))
print("    B =", sp.factor(c_pip))
print("    C =", sp.factor(c_pd2))
identically_zero = (c_pi2 == 0 and c_pip == 0 and c_pd2 == 0)
print("[D] identically zero on-shell?", identically_zero)
for nm, cc in (("A", c_pi2), ("B", c_pip), ("C", c_pd2)):
    print(f"    k->0: t^2*{nm} ->", sp.limit(cc * t**2, k, 0),
          "| k^2-scaled:", sp.limit(cc * t**2 * k**2, k, 0))
with open("h2_certificate.txt", "w") as f:
    f.write(f"alpha = {alpha}\nB = {Bsol}\ntheta_amp = {theta}\n")
    f.write(f"psi = {solpsi}\npsi_dot = {solpsid}\n")
    f.write(f"A(pi^2) = {c_pi2}\nB(pi pi') = {c_pip}\nC(pi'^2) = {c_pd2}\n")
    f.write(f"identically_zero = {identically_zero}\n")
print("h2_certificate.txt written")
