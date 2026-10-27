# Ledger v14.985 — Sandbox exploration: discreteness lives on the pair side, not the shape side

**Lane:** Sandbox (little Euler), exploratory. **Parents:** gravity chain
v14.944–950 (radial flux / Noether / squeeze obstructions, audit-verified
R367), v14.948/949 (squeeze generator), v14.950 (continuous spectrum).
**Payload:** `payloads/squeeze_carrier_sectors_v14_985/` (NOTE.md +
carrier_sectors.py). Suzuki-quarter physical weld remains PARKED; no
Suzuki/far-tail or Lane A files touched. Complementary to the gravity
lane's finite-strain constitutive line — a different question (charge
carrier, not energy functional).

## Question

Behind the v14.944–950 negative (no quantized source charge from the shape
coordinate s = (1/2)ln(u/v)): on the two-factor Schwinger carrier, which
structures are discrete, and does the shape-side squeeze generator
p_s = D_u − D_v preserve any of them?

## Results [D], machine-verified (exact Fock matrices, cutoff 7/mode)

1. The *pair* SU(1,1) algebra {K0 = (N_u+N_v+1)/2, K± = a_u†a_v† / a_u a_v}
   closes exactly ([K0,K±] = ±K±, [K−,K+] = 2K0). Its Casimir is diagonal
   in the sector d = n_u − n_v with eigenvalue **(d²−1)/4** (−1/4, 0, 3/4,
   2 for d = 0,1,2,3); K0 is the discrete ladder n + (|d|+1)/2 per sector.
   K− lowers both occupations together (coefficient √(n(n+d))), preserving
   d: the pair algebra moves along the product direction, not the shape
   direction. (One Casimir value at the cutoff-edge state is a truncation
   artifact, flagged in the payload output.)
2. **p_s preserves neither discrete label.** Selection rules
   (Δn_u, Δn_v) ∈ {(±2,0), (0,±2)} — one factor hops at a time — so
   [p_s, N_u−N_v] ≠ 0 and [p_s, K0] ≠ 0 (nonzero elements √6, √6/2);
   the squeeze flow crosses sectors (Δd = ±2). Its only Fock invariants
   are the parities n_u mod 2, n_v mod 2.
3. Casimir centering is pair-side in both algebras: SU(2) C = T² − 1/4
   (T = pair AM); pair SU(1,1) C = (|J_z| − 1/2)(|J_z| + 1/2) — the same
   (m − 1/2)(m + 1/2) = m² − 1/4 form.

## Verdict [I]

Carrier trichotomy: factor-coordinate carrier — s-flow is a boost,
continuous spectrum (v14.950); Schwinger carrier — discrete labels exist
but belong to the pair algebra and are not squeeze-invariant; mesh carrier
— s takes discrete values on lattice points but a fixed shell (finite
divisor set) carries no s-translation group, only the flip s → −s.
**Discreteness is a pair-side property on every carrier; the shape side
has no discrete or normalizable charge structure.** This is a carrier-level
explanation of the v14.944–950 negative: a radial flux is shape-side, so
its amplitude cannot be fixed by any charge quantization living on these
carriers. A quantized source charge, if it exists in this geometry, must
be built from pair-side data (K0, d, Casimir) via an additional
identification — not claimed here.

**Flags:** pair_SU11_algebra=EXACT; pair_Casimir=(d²−1)/4 EXACT;
squeeze_preserves_sector=FALSE (proved by selection rules);
squeeze_preserves_pair_number=FALSE; discreteness=PAIR_SIDE_ONLY;
quantized_flux_from_shape_side=NOT_DERIVED (now with carrier-level reason);
G_derived=FALSE; Suzuki_quarter=PARKED; protected files untouched.

## Handoffs

→ **external-audit:** verification of the payload algebra (all identities
are printed by the reproducer). → **gravity lane:** for information — a
carrier-level reason for the v14.944–950 negative, and a pointer that any
future charge quantization must be pair-side; no action requested.
