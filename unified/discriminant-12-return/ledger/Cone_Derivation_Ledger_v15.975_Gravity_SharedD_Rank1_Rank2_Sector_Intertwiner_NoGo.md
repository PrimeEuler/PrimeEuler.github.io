# Cone Derivation Ledger v15.975 — Matched outer n+1 circle: rank-1 and rank-2 SU2 coupling selection rules for EM versus quarter closed shells

**Date:** 2026-11-14 US Eastern, Gravity lane. **Parents:** v14.700 and v15.630 standard rank-1/rank-2 rotor tensor selection, v15.524–525 tidal Wigner–Eckart coefficients, v15.624/625 physical Casimir distinction, v15.951 common D, v15.973 distinct conventional EM and co-scaled quarter Schwinger irreps, v15.974 relative Berry Chern degree D and no full SU2 intertwiner. **Redundancy:** the Clebsch–Gordan triangle/weight-parity selection rules are standard and previously examined; the new application is their explicit intersection with the user-selected **same physical outer diameter** dictionary where the closed q2 shell has 2D states. **Latest prewrite HEAD:** 6d624067ee1881c71e2744f1fea6c75857c783e5 (exact reproducer). Target absent. Additive-only; Suzuki, Audit, Sandbox and frozen objects unchanged.

**Status:** [D] exact representation-theoretic low-rank obstruction; [C] assumes an integer-rank tensor under a *common physical SU2* and that the two closed oscillator carriers are the actual EM and gravitational fields; [N] no observed tensor source, physical cross-sector selection or kinetic coupling.

## Gate 766 — the shared-D map forces an increasing true spin gap

At fixed outer geometric diameter D=n+1≥2, the closed conventional Schwinger EM carrier has N_e=D−1, ordinary SU2 spin **j_e=(D−1)/2** and dimension D. The co-scaled quarter-grid oscillator has N_q=2D−1, ordinary SU2 spin **j_q,phys=(2D−1)/2**, dimension 2D. Its geometric coordinate is j_q,geom=j_q,phys/2=(2D−1)/4. The correct **ordinary-SU2** spin gap is therefore

**Delta j_phys=j_q,phys−j_e=D/2**.

Do not instead compare j_q,geom with j_e in a Clebsch–Gordan triangle: the half-step rescaled generators do NOT share the same ordinary Lie bracket without undoing the rescaling. The resulting increasing spin gap is not an independent physical prediction; it is the direct consequence of selecting the closed q2 oscillator representation with twice as many nodes at fixed geometric D.

## Gate 767 — conventional EM rank-1 and tidal rank-2 cannot reach arbitrary D

For a spherical irreducible tensor T^(k) of **integer** angular rank k acting between SU2 irreps, a potentially nonzero reduced matrix element requires **|j_q−j_e|≤k≤j_q+j_e** and the spin parity condition **j_q−j_e∈Z**. For the current pair, |Delta j|=D/2. A conventional rank-1 tensor is allowed by these *necessary* conditions **only at D=2**. A conventional rank-2 tensor is allowed **only at D=2 and D=4**. At every odd D, Delta j is half-integer so **no integer-rank tensor** may connect these two closed irreps under a single standard SU2 action. For even D≥6, reaching the other sector demands an integer tensor rank at least D/2, not a low-order EM dipole or tidal quadrupole.

Sample D=2: (j_e,j_q)=(1/2,3/2), k=1 or 2 potentially allowed. D=3: (1,5/2), k=1 or 2 forbidden by half-integer representation parity. D=4: (3/2,7/2), k=2 potentially allowed but k=1 forbidden. D=5: (2,9/2), all integer ranks forbidden. D=6: (5/2,11/2), k≥3 required. **Allowed** means only that Clebsch–Gordan symmetry does not force zero; actual reduced matrix elements can still vanish and their magnitude/phase is independent physical input.

The rank conclusion is SCOPED: if the two named sectors do not transform under one common physical SU2 representation, or the field is a spinor/half-integer tensor, these ordinary angular rules do not apply as stated. That case requires its own physical symmetry assignment and compatible charge/statistics. Under a genuinely spin-2 tidal *spacetime* perturbation acting on physical detector degrees of freedom, there is no automatic assumption that the above oscillator pseudospin is physical angular momentum; this comparison is conditional on identifying them.

## Gate 768 — Berry charge alone does not evade the operator obstruction

The relative prequantum Chern number from v15.974 equals D, which is twice the ordinary spin gap D/2; that is standard for CP1 quantization. A nonzero relative monopole bundle curvature by itself does NOT construct an allowed low-rank covariant operator. A charge-D polynomial section can produce a chosen nonequivariant injection of the D-dimensional EM carrier into the 2D-dimensional q2 carrier, but selects a direction and cannot be a full SU2 intertwiner. This exactly illustrates why line-bundle patch compatibility and a physical interaction source are separate gates. The constant co-scaled geometric Casimir-radius difference **3/16** is not an independent compensating tensor rank and does not override Clebsch–Gordan.

## Verification and verdict

**Reproducer:** `research-notes/k4_sharedD_rank12_CG_no_go_v15_975.py`, additive commit **6d624067ee1881c71e2744f1fea6c75857c783e5**. Independently executed matching exact Fraction checks for D=2..100 and tensor ranks k=1,2; PASS. External Audit pending.

**Positive:** the shared-D geometric dictionary implies a completely explicit, falsifiable **selection-rule pattern** if both closed q2 and EM oscillator carriers are actual angular SU2 sectors. **Negative:** low-rank EM and tidal drivers are forbidden for the overwhelming majority of shared diameters under that hypothesis; the few symmetry-allowed D still have unselected amplitudes. Thus the simplest Berry-relative-connection construction does not supply a universal physical gravity–EM converter or measure of a new Casimir kinetic energy.

**NEXT/HANDOFF Audit/Muse:** independently verify angular triangle and integer-spin-parity conditions, especially D odd; challenge the common-SU2 *physical* premise (Schwinger pseudospin vs physical rotations). If the correspondence is physically motivated via Spin(4), Taub–NUT or explicit field action, derive the source tensor and its matrix elements with no adjustable scales; otherwise treat this as an exact representation-theoretic negative and stop the unsourced quarter-connection branch.
