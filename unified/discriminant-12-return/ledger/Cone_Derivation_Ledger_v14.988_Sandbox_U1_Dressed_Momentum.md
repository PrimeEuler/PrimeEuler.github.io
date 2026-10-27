# Ledger v14.988 — Sandbox test: U(1) ħ-unit-circle derivation — quantizes the AM/GM-dressed momentum, not the bare s-flux

**Lane:** Sandbox (little Euler), exploratory, on the owner's question
(2026-10-27): can the quantized source charge be derived from U(1) being
the ħ unit circle? **Parents:** v14.620 (ħ unit circle; owner's framing),
v14.731 (dyon quarter via Misner periodicity), v14.944–950 (flux/Noether
negative chain), v14.985 (carrier sectors). **Payload:**
`payloads/u1_unit_circle_v14_988/` (NOTE.md + gudermannian.py; an
identically-contented copy sits under `u1_unit_circle_v14_986/`, deposited
minutes before v14.986 was taken by the gravity lane's finite-strain
entry — numbering collision on the payload directory name only).
Suzuki-quarter weld PARKED; no protected files touched.

## Results [D], machine-verified

For a factor pair (n, k), the unit-circle encoding
z = ((n−k) + 2i√(nk))/(n+k) has angle φ with **cos φ = tanh s,
sin φ = sech s** for s = (1/2)ln(n/k) — the Gudermannian bridge between
the pair's circular and hyperbolic parametrizations (dφ/ds = −sech s;
∫sech s ds = π per orientation; the swapped pair covers the other
semicircle). The dressing factor is **cosh s = (n+k)/(2√(nk)) = AM/GM**
(the γ of v14.621; e.g. 5/4 at the (1,4) crossing).
(φ̃, L) with φ̃ = π − φ and **L = cosh(s)·p_s** is an exact canonical pair
({φ̃, L} = 1, machine-checked); unitarily L is the circle momentum
−iℏ∂_φ̃ (measure sech s ds), so U(1) single-valuedness — phase = action/ħ
on U(1), the owner's v14.620 principle — gives **L ∈ ℏℤ**. Same mechanism
as the dyon's Misner derivation (v14.731).

## Interpretation [I/O]

The flux chain v14.944–950 tested the bare shift charge Q_s = ∫π_s; s is
hyperbolic and p_s is a boost, so that negative was correct — about the
undressed variable. The U(1)-quantizable charge is the dressed field
momentum **Q_φ = −∫cosh(s)π_s d³x**. On the isotropic k4 background
(s₀ = 0) cosh s₀ = 1 and the two charges coincide, so the distinction is
invisible in all background analyses to date; for anisotropic
configurations the homogeneous s-charge would sit in units ℏ·sech(s₀).
**Not derived:** that the physical k4 radial source charge (v14.944's Φ)
is Q_φ — that identification is the precise remaining conjecture. No
coupling of Q_φ to stress-energy is shown; the φ-parametrized field
theory (kinetic functions differ from the s-form by the cosh²s Jacobian)
is not built. G_derived=FALSE.

**Flags:** Gudermannian_dictionary=EXACT; dressed_momentum_quantization=
DERIVED_FROM_U1_SINGLE_VALUEDNESS; bare_s_flux_quantization=FALSE
(consistent with v14.944–950); source_equals_Q_phi=CONJECTURE_OPEN;
Suzuki_quarter=PARKED; protected files untouched.

## Handoffs

→ **external-audit:** verification of the payload identities.
→ **gravity lane:** for information — the U(1) route quantizes a dressed
charge that coincides with the s-flux only at s = 0; whether the lane's
source is that charge is the open identification. No action requested.
