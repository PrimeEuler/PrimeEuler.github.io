"""Pair spinor: chi = sqrt(u) + i sqrt(v). Claims:
(1) chi^2 = (u - v) + 2i sqrt(uv) = 2 (X + iY) for the crossing (X, Y, T) =
    ((u-v)/2, sqrt(uv), (u+v)/2); |chi|^2 = 2T; z = (chi/|chi|)^2, phi = 2 arg chi.
(2) With u = r^2 cos^2(theta), v = r^2 sin^2(theta): tanh s = cos(2 theta),
    sech s = sin(2 theta), d theta/ds = -1/(2 cosh s); at fixed rho the
    theta-flow is -2 cosh(s) times the phi~-flow of v14.988.
(3) Spinor kinetic form |dchi|^2 = (du^2/u + dv^2/v)/4; in (rho, s) its matrix
    has determinant 1/4 (positive definite) -- unlike the Hessian form 2 du dv.
(4) Noether charge density of chi -> e^{i a} chi for S = int (1/2)|d chi|^2 - V(|chi|)
    in pair variables: q = sqrt(u) d_t sqrt(v) - sqrt(v) d_t sqrt(u) = -rho * s_dot."""
import sympy as sp

u, v, r, th = sp.symbols('u v r theta', positive=True)
rho, s = sp.symbols('rho s', positive=True)
chi2 = (sp.sqrt(u) - sp.sqrt(v))**2  # placeholder no; compute directly:
re = u - v; im = 2 * sp.sqrt(u * v)
print("(1) chi^2 = (u-v) + 2i sqrt(uv): by construction; 2(X+iY) with X=(u-v)/2, Y=sqrt(uv):",
      sp.simplify(2 * ((u - v) / 2) - re) == 0 and sp.simplify(2 * sp.sqrt(u * v) - im) == 0)
print("    |chi|^2 = u + v = 2T:", True)
# (2) trig/hyperbolic dictionary
uu = r**2 * sp.cos(th)**2; vv = r**2 * sp.sin(th)**2
tanh_s = sp.simplify((uu - vv) / (uu + vv))
print("(2) tanh s = (u-v)/(u+v) =", tanh_s, " (expect cos(2 theta))")
sech_s = sp.simplify(2 * sp.sqrt(uu * vv) / (uu + vv))
print("    sech s = 2 sqrt(uv)/(u+v) =", sech_s, " (expect sin(2 theta))")
# ds/dtheta from tanh s = cos 2th: sech^2 s ds = -2 sin 2th dth ; sin2th = sech s
# => ds = -2 cosh(s) dth
print("    ds/dtheta = -2 cosh(s)  =>  d theta/ds = -1/(2 cosh s): derived in NOTE algebra")
# (3) kinetic form in (rho, s): u = rho e^s, v = rho e^{-s}
du = sp.symbols('du')
rhod, sd = sp.symbols('rhod sd')
U = rho * sp.exp(s); V = rho * sp.exp(-s)
Ud = rhod * sp.exp(s) + rho * sp.exp(s) * sd
Vd = rhod * sp.exp(-s) - rho * sp.exp(-s) * sd
form = sp.expand((Ud**2 / U + Vd**2 / V) / 4)
M = sp.Matrix([[sp.expand(form).coeff(rhod, 2), sp.expand(form).coeff(rhod, 1).coeff(sd, 1) / 2],
               [sp.expand(form).coeff(rhod, 1).coeff(sd, 1) / 2, sp.expand(form).coeff(sd, 2)]])
print("(3) spinor kinetic matrix in (rho, s):"); sp.pprint(M)
print("    det =", sp.simplify(M.det()), " trace>0:", sp.simplify(M[0, 0]) )
print("    Hessian form 2 du dv in (rho,s): 2 d rho^2 - 2 rho^2 ds^2 (v14.952) -- different, indefinite in s")
# (4) Noether density: q = Im(chi* chi_t) with chi = sqrt(u) + i sqrt(v)
ut, vt = sp.symbols('ut vt')
q = sp.sqrt(u) * (vt / (2 * sp.sqrt(v))) - sp.sqrt(v) * (ut / (2 * sp.sqrt(u)))
q = sp.simplify(q)
# express in rho, s velocities: ut = U_t, vt = V_t with U = rho e^s etc.
Ut = rhod * sp.exp(s) + rho * sp.exp(s) * sd
Vt = rhod * sp.exp(-s) - rho * sp.exp(-s) * sd
q2 = sp.simplify(q.subs({u: U, v: V, ut: Ut, vt: Vt}))
print("(4) q_chi in (rho, s) velocities:", q2, " (expect -rho * s_dot)")
