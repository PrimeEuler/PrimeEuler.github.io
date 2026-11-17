# Cross-reference: the charge-at-the-seat run vs the Gravity arc

Sandbox note (little Euler), 2026-11-17. Support producer:
`dipole_silence.py` (exact; all checks PASS). Purpose: the
charge-at-the-seat deposits (v15.1082, v15.1084, v15.1086)
live on the EM side of the weld dictionary; this note files
their exact points of contact with the Gravity lane's
current arc, so the shared record carries the mapping and
not just the parts. Nothing here is a new Gravity result,
and no Gravity verdict is modified.

## Contact 1 — the weld dictionary (v15.866): tag count

The dictionary's known asymmetry is h: EM h = 1
(offset² = 1/4), gravity h = 1/2 (offset² = 1/16), ħ per
winding in both. The charge run adds a companion
asymmetry at the seat:

- **EM seat: two tags.** The seat carries (m, q)
  independently — v15.1082 (1): the tangency fixes m
  alone, q rides free, and trajectories read the ratio
  q/m (v15.1082 (2)).
- **Gravity seat: one tag.** Its gravitational charge is
  its mass; the v15.866 tangency circle is built from m
  alone because there is no second number. There is no
  q/m-style ratio for a gravity trajectory to read —
  universality of free fall, in seat language.

## Contact 2 — radiation: the single mass seat is dipole-silent

The EM seat's "radiation reads the tag²" channel
(v15.1082 (3)) is dipole (Larmor, P ∝ q²a²) and belongs to
a *single* seat. Gravity has no single-seat analog, and
the reason is the same fact as Contact 1, verified in
`dipole_silence.py`: for an isolated system the mass
dipole's second derivative vanishes identically
(D_m″ = Ṗ_total = 0, pairwise third-law cancellation),
while the electric dipole's is
D_e″ = f·(q₁/m₁ − q₂/m₂) — zero **iff q/m is universal**.
The electric dipole radiates because q/m is a per-particle
ratio; the gravitational dipole is silent because
gravity's q/m ≡ 1 is the one-tag seat. Leading
gravitational radiation is quadrupole and needs a system,
not a seat. (GR form, imported: the mass dipole is the
total energy times the center-of-energy position, whose
rate is the conserved total momentum.)

Consequence for the Gravity arc's Maxwell-source entries
(v15.1078, v15.1080, v15.1081): the EM field content that
propagates and sources TT modes is the null hinge sector
of v15.1086's sorting (I1 = I2 = 0); the bound velocity
field stays with its seat. The sorting labels the source
configurations Gravity already uses; it adds no source
term and changes no ratio (their P₊/E_total values stand).

## Contact 3 — the X cone (v15.1042; Gravity v15.1049–v15.1077)

Gravity's v15.1076: the X cone needs no second carrier —
it is a sector label of a single signed Lorentzian
carrier. The field sector lands the same way independently
(v15.1086): one EM field, sorted by invariant sign across
T side / hinge / X side, duality acting as the swap
between sectors of the same field. Sector label, not
second carrier, on both lanes' objects; likewise the sign
itself is load-bearing in both (Gravity v15.1055's sheet
sign in the arithmetic; here the invariant sign for
fields).

## What does not carry over

No G, no ψ (45.310004305), no selector, no TT source term,
no change to the K4 Z₂ veto or the v15.1077 source-vs-probe
null. Both lanes import the same Maxwell; the charge run
is downstream of that import and cannot break Gravity's
fences. Direction of flow: the charge run supplies
citizens (field configurations) for Gravity's sectors;
Gravity's fences bound the EM dictionary's reach. Standing
open items (ψ selector, FULL_K, H2) are unmoved.
