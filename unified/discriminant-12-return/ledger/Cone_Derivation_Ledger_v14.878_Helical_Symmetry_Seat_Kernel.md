# Cone Derivation Ledger v14.878 — Helical symmetry diagonalizes the rotating scalar seat response

Date 2026-10-25. Parents v14.872–874, v14.877. Research note research-notes/Larmor_Helical_Symmetry_Diagonal_Seat_Kernel.md commit f63f5b3859ab1438e5290f2e335415ce95d177f4. Additive only; Suzuki/far-tail untouched.

[D conditional circular Gaussian model] The reflected-charge model with common rigid circular motion about X, fixed Ω, spherically symmetric Gaussian profiles, and seat δ transforming as a spatial scalar under rotations about X, has joint rotation/time-shift (helical) covariance. Vacuum Maxwell action and Coulomb/transverse Green functions preserve the same covariance. Therefore the complete Maxwell-reduced quadratic kernel for δ is time-translation invariant, K(t,t')=K(t−t'), and frequency diagonal. Individual source Fourier components contain ω+nΩ sidebands; after integrating over all wavevector orientations and vector components, these are INTERNAL channels of a single diagonal scalar self-energy, not necessarily Floquet off-diagonal coupling. This explicitly corrects the loose Floquet interpretation in v14.872–873. Static Coulomb curvature is unchanged by common source rotation; transverse equal-time magnetostatic energy correction is in v14.877.

[I/O] This reduction requires rotationally isotropic surroundings, rigid circular motion and prescribed constant Ω; external transverse lab anisotropy, changing drive phase, walls, and support structures may break symmetry and require genuine Floquet matrix. Retarded scalar kernel at finite Ω and its resonance pole are not numerically evaluated; no physical eigenmode, G or Higgs follows.

Flags: helical_time_translation_symmetry=EXACT_CONDITIONAL; reduced_scalar_frequency_diagonal=TRUE; individual_source_sidebands=TRUE; forced_Floquet_matrix=NOT_NECESSARY; finite_rotation_pole=OPEN; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: helical-rotation-scalar-kernel
parent: v14.878
status: open
action: Check helical covariance of the full conserved Gaussian rho/J, isotropic Maxwell reduction, and distinction between Fourier-sidebands and off-diagonal Floquet coupling; flag environment/sourcing assumptions. Protect Suzuki/far-tail.
deliverable: scoped audit verdict.
