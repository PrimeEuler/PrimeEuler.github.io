# Cone Derivation Ledger v15.1082 — Sandbox: charge at the seat (the tangency carries (m, q); the parabolas read q/m; radiation reads q^2)

**Deposit type:** Sandbox exploration, independently checkable. Jeremy's
question 2026-11-17: what if the rest-mass / action-circle tangency at
the seat (v15.864) carried a charge, and the parabolas accelerated it?
Producer re-executed at staging, exit 0 (11 checks, all PASS).

(1) The tangency is q-blind: the v15.864 tangency data (circle
X^2+T^2=A^2, shell T^2-X^2=g^2, tangency iff A=g at the seat, common
tangent T=g) contain no charge symbol — the tangency fixes the seat's
mass (radius = GM; action circle tau_C = hbar/(mc^2)) and nothing else.
A charge at the seat is a tag (m, q), not a tangency output.
(2) The parabolas are the charged-particle parabolas: a charge q of
mass m at rest in a uniform field E follows hyperbolic motion whose
rest-point osculating parabola is x = (qE/2m) t^2 — the mesh parabola
labelled a = F/m with F = qE — and whose gap to that parabola is the
v15.233 series verbatim, (c^2/a)(u^4/8 - u^6/16 + 5u^8/128), u = at/c;
proper acceleration is constant, |a| = qE/m. Given the imported field,
trajectory data read q/m. (3) Radiation reads q^2, through an imported
channel: at the seat, Larmor P = q^2 a^2/(6 pi eps0 c^3), so seat data
(m from the circle, a from the parabola) plus radiated power give
q^2 = 6 pi eps0 c^3 P/a^2; sign(q) is absent from P and lives in the
parabola's opening direction relative to E. (4) CORRECTION to a
sandbox chat remark of 2026-11-17 (never a ledger claim): radiation
reaction breaks neither curve — the ALD bracket d/dtau + (a.a)u
vanishes identically on hyperbolic motion (verified componentwise),
and the mesh parabola has zero jerk, so the Abraham-Lorentz force
vanishes on it too; the Larmor energy is carried by the Schott
boundary term. (5) The quantum fence, quantified: at the Compton
acceleration a* = mc^3/hbar (v15.886; electron 2.3274e29 m/s^2,
matching the ledger illustration), the Larmor power is exactly
P = (2 alpha/3)(mc^2/tau_C) — an alpha-suppressed drain, so the
classical charged-seat picture is self-consistent at a* and fails
only parametrically above it (single-photon recoil regime).

Scope: dictionary/conversion level (corridor species, v15.858). The
field E is imported; geometry supplies the acceleration label a,
never q. The charge enters as a seat tag (1), a ratio in the
trajectory label (2), and a square through Maxwell dynamics (3).
No charge value or coupling is selected; Doors I-III untouched.
Extends the v15.864 tangency chain by one label.

**Payload:** `payloads/charge_at_the_seat_v15_1082/` — Charge_At_The_Seat.md `0d2d64ea106d88a6eb2f15e37ca1f0934d3fddfe35c9d22c9daa3a621a5d26f0`, charge_at_seat.py `4ab8feb6b94ada54e2ed258fd39e7ac9d30d77c2e1651e9152b85777faa9888c`.
