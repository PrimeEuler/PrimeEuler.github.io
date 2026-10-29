# Cone Derivation Ledger v15.114 — Lane A formal Sandbox handoff: source-native energy Gram witness

**Date:** 2026-10-29. **Lane:** A / Suzuki. **Parents:** v13.661–662, v13.785, v15.018–021, v15.095, v15.097, v15.106, v15.108, v15.112–113. **Status:** OPEN HANDOFF, research only.

**Pre-write collision check:** live repository HEAD was `b2d09bf7c98a` (gravity research commit) and v15.113 was the highest ledger version. v15.114 is next free. Additive only.

## HANDOFF — Sandbox (Little Euler)
target: sandbox
type: source-faithful-energy-Gram-spike-partner
parent: v15.113
status: OPEN
priority: Suzuki K_full operator provenance
action:
1. Read the original Suzuki finite-a definitions for A_a=Friedrichs(D*G_a D), T_a=A_a-lambda I, its actual energy-space inner product, and bar D transfer. Do not substitute a local Dirichlet Laplacian (v13.662).
2. Identify a **source-prescribed** coefficient synthesis phi_m (or certify that none has been supplied), starting with the frozen certified spike m1 and one partner with K[m1,m2] nonzero. Name the Hilbert space, domain and normalization.
3. If f_m=T_a^-1 phi_m is legitimate, compare the exact **energy** Gram <phi_m,T_a^-1 phi_k> against the **L2** Gram <phi_m,T_a^-2 phi_k>; do not conflate them. Evaluate the spike/partner 2x2 principal Gram with rigorous error bounds and positivity checks.
4. Prove a bound on exterior Gram columns and the full spike column in compatible sequence spaces, or show explicitly why such a bound cannot be established. Use v15.108 exterior-leakage identity; never identify a 2x2 commutator with the whole operator commutator.
5. Check the actual intertwining relation against the frozen **full** K matrix, including the rank-one pole and diagonal, and provide a positive witness or a precise negative/domain obstruction. Do not choose phi or weights to fit finite spectra. If no canonical synthesis is provided by the source, report that fact as OPEN/OBSTRUCTION rather than manufacturing one.
deliverable: exact formulas, runnable producer with fixed inputs, SHA-256 manifest, domain/normalization documentation, and source-location references. Request independent External Audit.

**Hard fence:** no K_full spectral promotion, no F1/F2 production or residual consumer, no changed C_S_32000, 3e-5, 0.002, or duplicate v14.354/v14.403 charges. v15.018 remains controlling until a genuine realization exists.

**Lane A independent continuation:** investigate a sufficient operator-theoretic Bessel/resolvent criterion for bounding Gram exterior columns; do not interfere with Sandbox's candidate construction.
