# Cone Derivation Ledger v15.625 — Lane A: restore the already-derived all-mesh Casimir spectrum and EM/G quarter-sector classes

**Date:** 2026-11-10. **Origin:** user recalled that all mesh Casimirs were already computed during expansion. **Authoritative parents:** v15.135 §5 ("The Casimirs are different — correction, and the sector label"), v15.602 §§1–4 (all-q mesh theorem), v13.364 (scaled centered quadratic), v15.624 (overly restrictive sector-separation interpretation). **Status:** [D] existing exact algebra, restated; [C] interpretation/overclaim correction; [O] observed gravitational sector and source-derived Hamiltonian. **Prewrite live HEAD:** 81163d95efbe3f9be07a67d53e45c25da167d857, v15.625 collision check empty. Additive only; frozen Suzuki untouched.

## Recovered theorem, not a new discovery

The shared **formal geometric shell Casimir function** is C(j)=j(j+1), with mesh q≥1 and shell labels j=L/(2q), L nonnegative integer. Therefore the formula for every refined mesh is

**C_{q,L}=L(L+2q)/(4q²).**

The shell centering relation is C=(j+1/2)²−1/4; the centered +1/4 correction in this fixed **unit-step normalization** remains algebraically the same, but the *allowed eigenvalue spectrum* changes with q. Separately, if an operator's **transition step itself is rescaled** to δ, the quadratic completion is C_δ(j)=j(j+δ)=(j+δ/2)²−δ²/4 (v13.364); it is a different operator normalization/choice and should not be silently equated to C_{q,L}. This resolves the ambiguous phrase "all Casimirs": distinguish the shared geometric polynomial with q-dependent domain, the defected projected original-step ladder, and co-scaled closed SU(2) generators.

For q=1 (half-grid), j=L/2, C=L(L+2)/4. EM shells with j∈(1/2)Z_{≥0} yield C mod 1∈{0,3/4}. For q=2, j=L/4, the even L subset is exactly the EM half-grid, while **odd L** are the additional odd-quarter sector proposed for gravity: j∈{1/4,3/4,5/4,7/4,...} and C mod 1∈{5/16,13/16}. Those residue sets are disjoint from the EM values. Examples: C(1/4)=5/16, C(3/4)=21/16, C(5/4)=45/16, C(7/4)=77/16. This is exactly v15.135 §5's **independently derived Casimir spectral separation**; the same ledger entry records the user's earlier correction to its sandbox toy ring's supposed spectral indistinguishability.

The unit-step Casimir **defect operator** of v15.602 is C_def=j(j+1) Id−E, with projected original unit-step ladder failing to close on most quarter-grid states. This is not the same as the formal C(j) used in v15.135's sector-residue classification and is not necessarily the physical G-sector Casimir. A closed refined-step algebra (step 1/q) has rescaled Schwinger spin L/2 and Casimir L(L+2)/4 in rescaled units; that is yet another known construction. These distinctions matter but **do not erase the preexisting q-family Casimir formula or sector classes.**

## Correction to v15.624 and next gate

The phrase in v15.624 "its Casimir is a separate object" and "must be identified independently" was **too broad** if read as asserting the gravitational candidate's mathematical Casimir spectrum had never been derived. Correct statement:

1. **Already derived:** the q-family formula C_{q,L}, and for the quarter-only odd-L sector the different sixteenth-mod-one classes, all supplied by v15.135 and extended via v15.602.
2. **Still open:** whether this formal candidate spectrum arises from an independently justified gravitational generator/representation/Hamiltonian and produces a gravitational observable or coupling. The EM 1/4 *centering term* and the gravitational sector's *Casimir eigenvalues* are distinct concepts; do not infer that the G Casimir is 1/16 from cell halving.
3. **Further work:** use the v15.135 selector/parity χ and q=2 shell classes and compute direct-sum algebra/central idempotent/sector-change selection rules with exact finite matrices. Test whether the Casimir classification itself supplies a physical separation without new parameters, while preserving the proven spectrum as established data.

This entry is a correction/recall, not a new gravitational Casimir discovery, and does not reopen the Suzuki physical-quarter weld (still parked). Existing papers/audits/frozen objects unchanged.

**HANDOFF:** external-audit, gravity, sandbox. Confirm v15.135 §5 Casimir residue sets, all-q C_{q,L}, distinguish formal shell C from projected original-step C_def and co-scaled SU2 Casimir, and flag the overstatement in v15.624 without deleting historical files.
