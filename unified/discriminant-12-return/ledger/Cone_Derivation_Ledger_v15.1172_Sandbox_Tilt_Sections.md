# Cone Derivation Ledger v15.1172 — Sandbox: tilt on top — cutting-plane sections of the gridded cone, e = √2 sin γ exact, tilt a continuum modulus over the grid

**Deposit type:** Sandbox build, independently checkable
(producer re-executed from the staged payload copy;
6 checks ALL PASS). Origin: Jeremy's extension call
after v15.1167, "factors, then tilt on top" — part 2,
tilt (part 1 is v15.1171). Setup: the cone surface
(u,v) ↦ (T, X, Y) = ((u+v)/2, (u-v)/2, √(uv)),
T² = X² + Y²; cutting plane T cos γ + Y sin γ = c —
the tilt the e(t) line (v15.1110-1160) made dynamical
in the continuum, now put on the grid.

**The tilt-eccentricity relation is exact.** The
section conic is identically c²cos 2γ - X² -
cos 2γ·s² - 2c sin 2γ·s = 0 (symbolic), an ellipse
with a_X = c/√(cos 2γ), a_s = c/cos 2γ, hence
**e = √2 sin γ** — 0 at γ = 0, 1 at γ = 45° (the
parabola). Numeric extents reproduce e at 10°, 20°,
30° to 12 decimals. The e(t) deposits' e is √2 sin γ
in this parametrization; tilt and eccentricity are
one degree of freedom, its grid-side formula now
filed.

**Field response on tilted sections.** Section
Dirichlet energy per unit X-extent, computed on
lattice shell points at nine tilts 0°-40°, for two
filed fields of v15.1167: the worldline-sourced
min(u,v) falls 1.9718 → 1.2667 (fit coefficient
-0.8814 in e²); the massless wave falls 0.5490 →
0.4754 (-0.1088 in e²). Both decrease with tilt and
both carry a genuine e² term — filed as a CONTRAST
with v15.1110's U_B(e), which had no e² term (pure
quartic): that was a self-consistent sourced field
energy, this is a restriction functional of fixed
fields; different functionals, different tilt
response, neither quotes for the other.

**Tilt is not a grid symmetry.** At k=4, exactly 48
of the 384 signed factor permutations preserve the
cone form A — S₄ times the overall sign; independent
sign flips break the pair form (the build's first
draft assumed 384; the enumeration is the correction,
filed in the note). A continuous tilt (boost mixing
s₀, z₁ at θ = 0.1) moves the lattice point (1,0,0,0)
to y₁ = 1.074582 ∉ ℤ⁴: boosts preserve the grid at
no angle. Tilt therefore lives over the grid as an
external continuous modulus whose sections the grid
samples — tilt dynamics, if wanted, must be supplied
as a collective coordinate with its own inertia (the
e(t) pattern), not extracted from grid symmetries.

**Scope:** sections and restriction energies on the
k=2 cone; symmetry statements at k=4. No tilted
evolution (boost-breaking makes it an interpolation
scheme, not an exact one — the filed reason it is
absent), no tilt dynamics, no interactions. Corridor
species: dictionary/transport; tilt is supplied, not
selected, like ρ and the doors' residues.

**Payload:** `payloads/tilt_sections_v15_1172/` — Tilt_Sections.md `4603680b35f9400ab10b6d63ce31048a5cbc88e499d1e53c38055f23d6de62dd`, tilt_sections.py `3a7c15d05683d9a002c57036acba8f2d0f0e659e01c4e17cb4907310b1e3569a`.
