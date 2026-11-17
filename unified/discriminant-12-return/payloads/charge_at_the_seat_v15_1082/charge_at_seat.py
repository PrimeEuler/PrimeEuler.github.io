#!/usr/bin/env python3
"""
charge_at_seat.py -- charge-at-the-seat check (sandbox, 2026-11-17).

Question (Jeremy, 2026-11-17): what if the rest-mass / action-circle
tangency at the seat (v15.864) carried a charge, and the parabolas
accelerated it?

Checks (exact, sympy; SI where stated, c=1 where stated):

A. Tangency is q-blind. The v15.864 tangency data -- circle
   X^2+T^2=A^2, shell T^2-X^2=g^2, tangency iff A=g at the seat
   (0,g), common tangent T=g -- contain no charge symbol. A charge
   pinned at the seat is a tag (m,q); the tangency fixes m only.

B. Uniform-E completion. A charge q (mass m) starting at rest in a
   uniform electric field E (parallel) has p = qEt and
       x(t) = (mc^2/qE)( sqrt(1+(qEt/mc)^2) - 1 ),
   whose rest-point osculating parabola is x = (qE/2m) t^2 -- the
   mesh parabola labelled a = F/m with F = qE -- and whose gap to
   that parabola is exactly the v15.233 series
   (c^2/a)(u^4/8 - u^6/16 + 5u^8/128), u = at/c.

C. Proper acceleration of the hyperbolic motion is constant,
   |a| = g = qE/m (c=1 worldline check: u.u=1, a.a=-g^2).

D. Radiation reaction does NOT break either curve (this corrects
   the chat remark of 2026-11-17 09:58, which said a radiating
   charge's true motion is neither curve exactly). The ALD
   self-force is proportional to the part of da/dtau along the
   spatial direction; on hyperbolic motion da/dtau = -(a.a) u
   exactly (purely along u), so the ALD bracket vanishes
   identically. Nonrelativistically the Abraham-Lorentz force is
   m*tau0*jerk, and the parabola has jerk 0. Both curves are
   reaction-free; the radiated Larmor energy is carried by the
   Schott acceleration-energy boundary term, not by work against
   a reaction force.

E. Larmor readout. P = q^2 a^2/(6 pi eps0 c^3) (SI, at the seat
   where coordinate acceleration = proper acceleration). Hence
   trajectory data (a from the parabola label, m from the action
   circle) plus radiated power determine q^2 = 6 pi eps0 c^3 P/a^2.
   Sign(q) is absent from P; it lives in the parabola's opening
   direction relative to E.

F. Quantum fence, quantified. At the Compton acceleration
   a* = mc^3/hbar (the v15.886 scale), the Larmor power is
       P = (2 alpha/3) * (mc^2 / tau_C),   tau_C = hbar/(mc^2),
   i.e. radiation drains the rest energy at a fraction 2alpha/3
   per Compton time -- alpha-suppressed, so the classical
   charged-seat picture is self-consistent at a* and only fails
   parametrically above it (single-photon recoil regime).

Scope: dictionary/conversion level (corridor species, v15.858).
The field E is imported; geometry supplies a, never q. Nothing
here selects a charge value or a coupling.
"""
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


# ---------- A. tangency is q-blind ----------
X, T, A, g = sp.symbols("X T A g", positive=True)
q, m, E, t, c = sp.symbols("q m E t c", positive=True)
circ = X**2 + T**2 - A**2
shell = T**2 - X**2 - g**2
# intersections: 2X^2 = A^2 - g^2 -> X=0 iff A=g
check("A1 circle-shell tangency at the seat iff A=g",
      sp.simplify(((A**2 - g**2) / 2).subs(A, g)) == 0)
check("A2 q is not a symbol of the tangency data (circle, shell)",
      q not in circ.free_symbols and q not in shell.free_symbols)

# ---------- B. uniform-E motion and the v15.233 gap ----------
a = q * E / m  # parabola label: a = F/m with F = qE
z = sp.symbols("z")
sqrt_series = sp.series(sp.sqrt(1 + z), z, 0, 5).removeO()  # through z^4
u = sp.symbols("u", positive=True)
# x_hyp = (c^2/a)( sqrt(1+u^2) - 1 ), u = at/c ; x_par = (c^2/a) u^2/2
x_hyp_u = (c**2 / a) * (sqrt_series.subs(z, u**2) - 1)
x_par_u = (c**2 / a) * u**2 / 2
gap = sp.expand(x_par_u - x_hyp_u)
gap_ref = (c**2 / a) * (u**4 / 8 - u**6 / 16 + 5 * u**8 / 128)
check("B1 gap(parabola - hyperbola) == v15.233 series "
      "(c^2/a)(u^4/8 - u^6/16 + 5u^8/128)",
      sp.simplify(gap - gap_ref) == 0)
check("B2 osculating parabola is x = (qE/2m) t^2 (label a = qE/m)",
      sp.simplify(x_par_u.subs(u, a * t / c) - (q * E / (2 * m)) * t**2) == 0)

# ---------- C. constant proper acceleration (c=1) ----------
tau, gg = sp.symbols("tau g", positive=True)
tt = sp.sinh(gg * tau) / gg
xx = (sp.cosh(gg * tau) - 1) / gg
u0, u1 = sp.diff(tt, tau), sp.diff(xx, tau)
a0, a1 = sp.diff(u0, tau), sp.diff(u1, tau)
check("C1 u.u = +1 (c=1)", sp.simplify(u0**2 - u1**2) == 1)
check("C2 a.a = -g^2: proper acceleration constant, |a| = g = qE/m",
      sp.simplify(a0**2 - a1**2 + gg**2) == 0)

# ---------- D. ALD bracket vanishes on hyperbolic motion ----------
da0, da1 = sp.diff(a0, tau), sp.diff(a1, tau)
aa = a0**2 - a1**2  # = -g^2
check("D1 da/dtau + (a.a) u == 0 componentwise: jerk purely along u, "
      "ALD self-force vanishes on hyperbolic motion",
      sp.simplify(da0 + aa * u0) == 0 and sp.simplify(da1 + aa * u1) == 0)
# nonrelativistic Abraham-Lorentz force ~ jerk; parabola a = const -> jerk 0
jerk = sp.diff(a * t**2 / 2, t, 3)
check("D2 mesh parabola has zero jerk (AL force m*tau0*jerk = 0)",
      sp.simplify(jerk) == 0)

# ---------- E. Larmor readout ----------
P, eps0 = sp.symbols("P eps0", positive=True)
q2 = 6 * sp.pi * eps0 * c**3 * P / a**2
check("E1 Larmor inversion consistent: P(q^2) == P with "
      "q^2 = 6 pi eps0 c^3 P / a^2",
      sp.simplify(q2 * a**2 / (6 * sp.pi * eps0 * c**3) - P) == 0)

# ---------- F. drain fraction at the Compton acceleration ----------
hbar, alpha = sp.symbols("hbar alpha", positive=True)
astar = m * c**3 / hbar
# q^2/(4 pi eps0) = alpha hbar c  =>  q^2/(6 pi eps0) = (2/3) alpha hbar c
P_star = (sp.Rational(2, 3) * alpha * hbar * c) * astar**2 / c**3
tau_C = hbar / (m * c**2)
ratio = sp.simplify(P_star / (m * c**2 / tau_C))
check("F1 at a=a*: P = (2 alpha/3) x (rest energy per Compton time)",
      sp.simplify(ratio - sp.Rational(2, 3) * alpha) == 0)

# ---------- numeric illustration (not gated beyond a*) ----------
e_charge = 1.602176634e-19
m_e = 9.1093837015e-31
c_si = 299792458.0
hbar_si = 1.054571817e-34
astar_e = m_e * c_si**3 / hbar_si
print(f"ILLUSTRATION electron: a* = {astar_e:.4e} m/s^2 "
      f"(ledger v15.886: 2.327e29)")
check("F2 electron a* matches v15.886 illustration 2.327e29 (1%)",
      abs(astar_e / 2.327e29 - 1) < 0.01)
E_ill = 1e9  # V/m
a_ill = e_charge * E_ill / m_e
print(f"ILLUSTRATION electron in E=1e9 V/m: a = qE/m = {a_ill:.4e} m/s^2, "
      f"a/a* = {a_ill/astar_e:.3e}")

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
