# Swapping E and B, and the T/X coupling — duality IS the cone swap, once fields are sorted by invariant sign

Sandbox note (little Euler), 2026-11-17; third in the
charge-at-the-seat run (v15.1082, v15.1084). Producer:
`duality_cones.py` (sympy, exact; all checks PASS, exit 0).
Jeremy's questions: (1) could you swap E for B and get the
same results? (2) could we couple E to the T cone and B to
the X cone (v15.1042)?

## 1. The swap: yes for the field algebra, at a price

Under the duality map D: E → cB, B → −E/c, both field
invariants flip sign (I1 = E²−c²B² → −I1, E·B → −E·B),
the complex combination ℱ = I1 + 2ic(E·B) goes to −ℱ,
and |ℱ| is invariant under the whole duality rotation
group (all verified). Every field statement of v15.1082 /
v15.1084 therefore replays verbatim with E and B
exchanged — and the radiation field, having I1 = E·B = 0,
is not merely replayed but literally unchanged: the hinge
sector is self-dual.

The price is at the seat. Applying D to the seat's field
gives, in the rest frame, E = 0 and B = −E′/c: a pure
magnetic Coulomb field. The dual seat carries a **magnetic
charge**. The parabolas replay too (a magnetic charge in
a B field obeys the dual Lorentz force, same osculation),
and the Larmor readout replays with q_m² — but Dirac
quantization (imported) prices that coupling at
α_g = n²/(4α) ≈ 34.26 for n = 1: where the electric seat's
radiation was α-suppressed (v15.1082, part E), the dual
seat's would be enormous. And the world's seats are
electric: no monopole has been observed. Duality is a
symmetry of the field algebra, not of the seat tags
nature actually supplies.

## 2. E→T / B→X: fails as stated; the repair is a sorting

As stated, the coupling contradicts v15.1084: the
velocity field's B is T-sector data (slaved to E by
tanh ψ, not an independent X-sector object), and the
radiation field's E is hinge data (not T-sector). Neither
field species belongs to a single cone.

What does sort by cone is the **sign of the invariant**,
exactly as sign(uv) sorts pairs in v15.1042 — verified on
the three field configurations this run has built:

    I1 > 0   electric-dominant   T side    seat velocity field (I1 = E′²)
    I1 = 0   null                hinge     radiation field
    I1 < 0   magnetic-dominant   X side    dual seat field (I1 = −E′²)

And under this sorting the answer to question (1) becomes
geometric: **duality is the T↔X swap map for field
configurations, with the hinge fixed.** The working
coupling is not E↔T, B↔X; it is invariant-sign ↔ cone.

One coordinate remains: a general field also carries
I2 = E·B, and the pair (I1, I2) enters physics only
through ℱ, whose modulus |ℱ| is duality-invariant and
whose argument is the duality angle. In pair language the
field sector has its own (size, angle) data — |ℱ| as the
seat-like invariant, arg ℱ as a phase on the duality
circle — filed as a dictionary observation, not developed.

## Scope

Dictionary level; Maxwell and Dirac imported, as before.
The sorting is a statement about field configurations,
not a dynamics on either cone; the cones acquire no new
citizens with equations of motion. Nothing is selected;
Doors I–III untouched.
