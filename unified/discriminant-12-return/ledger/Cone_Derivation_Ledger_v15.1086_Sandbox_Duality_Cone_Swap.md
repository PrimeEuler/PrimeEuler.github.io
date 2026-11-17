# Cone Derivation Ledger v15.1086 — Sandbox: swapping E and B, and the T/X coupling (duality is the cone swap, by invariant sign)

**Deposit type:** Sandbox exploration, independently checkable; third
in the charge-at-the-seat run (v15.1082, v15.1084). Jeremy's questions
2026-11-17: (1) could you swap E for B and get the same results?
(2) could we couple E to the T cone and B to the X cone (v15.1042)?
Producer re-executed at staging, exit 0 (9 checks, all PASS).

(1) The swap works for the field algebra: under duality
D: E -> cB, B -> -E/c, both invariants flip sign (I1 = E^2 - c^2 B^2
and E.B), the complex combination F = I1 + 2ic(E.B) goes to -F, and
|F| is invariant under the full duality rotation group — every field
statement of v15.1082/v15.1084 replays with E and B exchanged, and
the radiation field (I1 = E.B = 0) is literally unchanged: the hinge
sector is self-dual. The price is at the seat: the dual of the seat's
field is at rest a pure magnetic Coulomb field (E = 0, B = -E'/c) —
the dual seat carries a magnetic charge, the parabolas replay under
the dual Lorentz force, and Dirac quantization (imported) prices the
dual coupling at alpha_g = n^2/(4 alpha) = 34.26 for n = 1, where the
electric seat's radiation was alpha-suppressed. Duality is a symmetry
of the field algebra, not of the seat tags nature supplies (no
monopole observed). (2) E->T / B->X as stated fails — v15.1084
already shows the velocity field's B is T-sector data (slaved to E by
tanh psi) and the radiation field's E is hinge data. The repair is a
sorting by the sign of I1, exactly as sign(uv) sorts pairs in
v15.1042, verified on this run's three field configurations:
I1 > 0 (electric-dominant, seat velocity field, I1 = E'^2) on the
T side; I1 = 0 (null, radiation) on the hinge; I1 < 0
(magnetic-dominant, dual seat field, I1 = -E'^2) on the X side.
Under this sorting, duality IS the T<->X swap map for field
configurations, with the hinge fixed. The working coupling is
invariant-sign <-> cone, not field-species <-> cone. Residual
coordinate filed undeveloped: a general field's (I1, E.B) enter
through F alone, with |F| the duality-invariant size and arg F a
phase on the duality circle — the field sector's own (size, angle)
pair data.

Scope: dictionary level; Maxwell and Dirac imported. The sorting is
a statement about field configurations, not a dynamics on either
cone. No coupling selected; Doors I-III untouched.

**Payload:** `payloads/duality_cone_swap_v15_1086/` — Duality_Cones.md `c13f7588216c5bcd8d5087a74d7393f236b066d23f7d34c0558f4922f9a7ac2d`, duality_cones.py `f0e46283e8dd0f9f9ca87b09be3aae7738bf17a81c868cea94dc447804a3355a`.
