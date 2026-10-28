# Ledger v15.048 — Sandbox composite-triplet test: the Bloch amplitude does not derive the AM source's C (route closed; amplitude is an action coefficient, not a field norm)

**Lane:** Sandbox (little Euler), run at Jeremy's direction
2026-10-28 ("smash the door" scoped as the composite-triplet
test). **Parents:** v14.989/v14.996 (AM triplet, SVT certificate),
v14.990 (pair spinor), v15.014 (spinor-source test), v15.046
(door pointer), v14.916 (PARK). **Payload:**
`payloads/composite_triplet_test_v15_048/` (NOTE.md, composite.py).

## Question

The Bloch triplet of the pair spinor has amplitude |n| = |chi|^2,
slaved by purity and = 1 at the hbar-circle normalization. If the
gravity triplet were phi^I = chi^dagger sigma^I chi, would its
amplitude C (W = C A_B; kappaC = 1 currently a matching) be
derived?

## Results [D]

1. **Spinor-dynamics reading:** the source is chi itself
(v15.014 dynamics); the composite amplitude on the coasting
tracker is |chi|^2 = 2(ln tau)^2 — drifts (10.6 at tau = 10 ->
128 at tau = 3000) where a constant C is required; a homogeneous
Bloch vector is also anisotropic (preferred direction), not the
FLRW source.
2. **AM-functional reading:** W[phi] = C A_B[phi] — C factors out
identically for ANY phi, composite or elementary; the
substitution cannot reach it. Homogeneous composite: B = 0,
W = 0 (AM energy is spatial-gradient energy). Label-mimicking
hedgehog texture is exact (Bloch = (x, y, z) pointwise) but its
kinetic density is (2 + cos th)/(4r(1 + cos th)) ~ 1/r,
angle-dependent, string-singular at th = pi: inhomogeneous,
not C/a^2.

## Diagnosis and flags

Amplitude slaving constrains a FIELD NORM; C is an ACTION
COEFFICIENT (elastic modulus). Compositeness is structurally
incapable of reaching it; the "1 = 1" rhyme conflates a field
value at the hbar normalization with an action coefficient in
gravitational units. Spectrum check vs v14.996 (P = 3H,
Q tau^2 = 3k^2 + 4) NOT REACHED (presupposes the failed
background identification).
**Flags:** composite_triplet_route=CLOSED_NEGATIVE;
amplitude_nature=ACTION_COEFFICIENT_NOT_FIELD_NORM;
park_requirement_sharpened=MECHANISM_MUST_SLAVE_AN_ACTION_COEFFICIENT;
kappaC_matching=UNCHANGED; G_derived=false; Suzuki_quarter=PARKED.

## Handoffs

→ **external-audit:** verification of the payload.
→ **gravity lane:** the door was swung at under sandbox scope and
held; the sharpened park requirement is the residue — offered
for the record, no action requested.
