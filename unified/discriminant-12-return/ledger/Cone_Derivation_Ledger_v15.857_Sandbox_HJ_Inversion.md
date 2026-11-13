# Cone Derivation Ledger v15.857 — Sandbox: Hamilton–Jacobi inversion on the cone's phase field (force from energy, executed; the dictionary selects nothing)

**Deposit type:** Sandbox exploration, independently checkable. Jeremy's
question and go-ahead 2026-11-13: a force transfers energy (joules),
energy × time is action (the cone's joule-second circles) — shouldn't
force be derivable from the energy? This executes the strongest form of
that route, the Hamilton–Jacobi inversion scoped but left unexecuted at
v15.489. Producer re-executed at staging, exit 0; payload snapshot's
title block records the staging state of the note.

## (a) The cone's field inverts to its own law, exactly

Abel inversion of the constant-force family's action function — the
bouncer J(E) = (4√2/(3a√m))·E^{3/2} (v15.469) — with kernel integrals
π/2 and 2 exact, returns the turning-point function x_tp(U) = U/(ma)
symbolically: the recovered potential is U(x) = ma·x, the linear
potential whose slope is the family's own acceleration times m. Direct
HJ on the cone's abbreviated action S(x,E) agrees identically:
U := E − (∂ₓS)²/(2m) = F·x (sympy, exact). The inversion is faithful —
it returns precisely the law whose action was fed to it.

## (b) The dictionary is impartial: controls

Harmonic data J(E) = 2πE/ω inverts symbolically to the quadratic well
(exact match). Kepler radial data: J_r(E) log-log slope measured
−0.5000, turning point r_t = k/|E| reading off U(r) = −k/r. Numeric
round trips (U → J by quadrature → Abel → width) close at 1.0×10⁻³
(linear) and 1.7×10⁻⁸ (harmonic). Phase field and potential are one
datum in two coordinates; each family returns its own law and no
other — Newton's potential is unreachable from the cone's data for the
same reason the cone's law is unreachable from Kepler's.

## (c) The family's constant passes through as a supplied real

At a = 1, 2, 7 the recovered slope is m·a each time: the inversion
determines the law's form from the family and leaves the family's
constant untouched in the output — Door III's shape appearing inside
dynamics.

## Verdict and scope

Force is derivable from the energy data in the only sense it ever is —
from the energy as a function (the complete phase field), via an exact
inversion that returns the generating family. This closes the HJ route
and stands as the fourth exhibit of the input/output direction
(v15.277 Kepler audit; v15.487 force-law scan; v15.489 phase readout):
the cone's action machinery is complete and faithful, and it
transports laws without selecting them. The selector that would choose
the family is not in the dictionary — now shown at the HJ level, not
merely scoped.

**Payload:** `payloads/hj_inversion_v15_857/` — HJ_Inversion.md `987c9ba79b8a4228b24e78f5ba29b8ca1dec533b94ebda4ca24674d480f6b007`, hj_inversion.py `bf1bcbe67567bd7b1a49a1225dbf1af8504b34fcb4829cc2aab3c778cbbfb448`.
