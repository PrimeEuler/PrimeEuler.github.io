# Charge at the seat — the tangency carries (m, q), the parabolas read q/m, radiation reads q²

Sandbox note (little Euler), 2026-11-17. Producer:
`charge_at_seat.py` (sympy, exact; all checks PASS, exit 0).
Question (Jeremy, 2026-11-17): what if the rest-mass /
action-circle tangency at the seat (v15.864) carried a
charge, and the parabolas accelerated it?

## Results

**A. The tangency is q-blind.** The v15.864 tangency data
(circle X²+T²=A², shell T²−X²=g², tangency iff A=g at the
seat, common tangent T=g) contain no charge symbol: the
tangency fixes the seat's mass (radius = GM, action circle
τ_C = ħ/mc²) and nothing else. A charge at the seat is a
*tag* (m, q) the seat carries, not a quantity the tangency
produces.

**B. The parabolas are the charged-particle parabolas.**
A charge q of mass m starting at rest in a uniform field
E (parallel) follows the hyperbolic motion
x(t) = (mc²/qE)(√(1+(qEt/mc)²) − 1), whose rest-point
osculating parabola is x = (qE/2m)t² — exactly the mesh
parabola labelled a = F/m with F = qE — and whose gap to
that parabola is the v15.233 series verbatim,
(c²/a)(u⁴/8 − u⁶/16 + 5u⁸/128), u = at/c. The proper
acceleration is constant, |a| = qE/m (c=1 worldline check:
u·u = 1, a·a = −g²). So the parabola through a charged
seat is labelled by (q/m)E: same seat, different charge,
different parabola — given the imported field E, the
trajectory data read q/m.

**C. Radiation reads q² — through an imported channel.**
At the seat (coordinate acceleration = proper
acceleration), Larmor gives P = q²a²/(6πε₀c³), so seat
data (m from the circle, a from the parabola) plus
radiated power determine q² = 6πε₀c³P/a². Sign(q) is
absent from P; it lives in the parabola's opening
direction relative to E. This is α-shaped data (q²/ħc)
arriving through Maxwell dynamics, not through geometry.

**D. Correction — radiation reaction breaks neither
curve.** A remark in the sandbox chat (2026-11-17,
pre-check) held that a radiating charge's true motion is
neither the parabola nor the hyperbola exactly. The check
refutes that: the ALD self-force is proportional to
ȧ + (a·a)u, and on hyperbolic motion ȧ = −(a·a)u exactly
(verified componentwise), so the self-force vanishes
identically; nonrelativistically the Abraham–Lorentz
force is mτ₀·jerk and the mesh parabola has jerk 0. Both
curves are reaction-free while radiating; the Larmor
energy is carried by the Schott acceleration-energy
boundary term, not by work against a reaction force. The
chat remark is withdrawn and replaced by this paragraph.

**E. The quantum fence, quantified.** At the Compton
acceleration a* = mc³/ħ (the v15.886 scale; electron
a* = 2.3274×10²⁹ m/s², matching the ledger illustration),
the Larmor power is exactly

    P = (2α/3) · (mc²/τ_C),   τ_C = ħ/(mc²):

radiation drains one rest energy per Compton time at a
fraction 2α/3 — α-suppressed. The classical charged-seat
picture is therefore self-consistent at a* and fails only
parametrically above it, where single-photon recoil (the
q² channel becoming stochastic) takes over. Illustration:
an electron in E = 10⁹ V/m has a = 1.7588×10²⁰ m/s²,
a/a* = 7.6×10⁻¹⁰ — deep inside the classical regime.

## Scope

Dictionary/conversion level (corridor species, v15.858).
The field E is imported; geometry supplies the
acceleration label a, never q. The charge enters as a
seat tag (A), a ratio in the trajectory label (B), and a
square through an imported dynamical channel (C). Nothing
here selects a charge value or a coupling; Doors I–III
untouched. Extends the v15.864 tangency chain by one
label; corrects one sandbox chat remark (D), which was
never a ledger claim.
