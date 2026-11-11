# Cone Derivation Ledger v15.717 — Gravity: conserved FLRW source satisfies the K4 scalar ADM Ward identity and drives the physical scalar mode

**Date:** 2026-11-11, US Eastern. **Parents:** v14.928 EH+elastic solid, v14.935 scalar action/ADM conventions, v15.713 sourced scalar compatibility and recovered P mode, v15.714 retarded scalar Green function, v15.716 globally FLRW-covariantly conserved tilted traceless Fourier stress and 2/3 norm theorem. **Status:** [D] exact covariant-energy/ADM constraint-compatibility equivalence for tracefree source and explicit source-compatible scalar forcing; [C] linear external source realization by a physical matter action and ADM/cos-mode Fourier matching; [N] no gauge-invariant curvature detector transfer nor unique gravity 2/3 coupling. **Immediately prewrite HEAD:** 57c72ef3f4673fcc43a000db8c8720fe1d3f90ad. v15.717 ledger absent; all commits additive, protected Suzuki/far-tail untouched.

## Gate 322 — match cosmological covariant conservation to the scalar lapse/shift source Ward identity

Recall the v15.713 constraint recovered by varying the *time-dependent* K4 scalar reduced action with formal lapse/shift sources J_Phi, J_B:

**tau dJ_Phi/dtau + sqrt(3) J_B = 0**.

Use the exact coasting FLRW external stress of v15.716, with spatial stress trace zero and Fourier phase exp(+ikz). Its energy conservation is

**rho_dot +3H rho + i k T^(0z)=0**, **H=1/tau**, for stress components defined contravariantly in cosmic time.

The scalar metric mode with *opposite* Fourier phase exp(-ikz) has, in the v14.935 scalar ADM conventions, **delta g_00=2 Phi** and **delta g_0z=-a partial_z B=+i k a B**. The conventional metric source contraction (1/2) a³ T^(mu nu) delta g_(mu nu), paired at opposite wavevectors, therefore supplies

**J_Phi=a³ rho**, **J_B=i k a⁴ T^(0z)**,

up to common normalization conventions of real Fourier amplitudes. Since **sqrt(3) a=tau**,

**tau J_Phi_dot+sqrt(3) J_B
=tau a³ [rho_dot+3H rho+i k T^(0z)] =0**.

Thus, for this **tracefree** external stress class, the earlier Ward-like scalar source constraint follows exactly from standard FLRW energy-momentum conservation. In particular, the scalar direct metric source proportional to the isotropic spatial trace vanishes, so no omitted direct psi term spoils this restricted matching. Other stress classes with trace/pressure source couplings require a fresh full source-action analysis.

**Fourier-phase caution:** the original v14.935 code used a real cos-mode substitution B_z=-k B; the complex derivation here explicitly pairs the exp(+ikz) source with exp(-ikz) metric so derivative and current phases are consistent. The numerical conversion from physical stress components to J depends on whether one uses real/complex mode conventions and global signature. Both coefficients must use the same choice. The result should be independently audited against the full physical source action before assigning absolute detector amplitudes.

## Gate 323 — explicit nonzero conserved common-source example

Use v15.716's fixed normalized generic tilted axis

**n=(sqrt(1/2),sqrt(1/3),sqrt(1/6))**,

and **Q0_ij=sigma(n_i n_j-delta_ij/3)**, with a=tau/sqrt(3).

Then the covariantly conserved stress components give

**rho=k² sigma/(4 tau²)+rho0/tau³**,

**T^(0z)=i k sigma/(4 tau³)**,

with all other momentum/stress components obtained from the v15.716 formula. The resulting scalar source coefficients are

**J_Phi=sqrt(3)[k² sigma tau+4 rho0]/36**,

**J_B=-k² sigma tau/36**,

and satisfy the exact K4 auxiliary compatibility identity for arbitrary sigma and rho0. The source has generic nonzero T, V, and S **stress** projectors, but this does not prove all three independently propagate or appear in a remote detector. The covariant completion is a prescribed perturbative stress field, not an independently derived localized, positive-energy matter action.

## Gate 324 — source-first physical scalar P equation gains an explicit forcing

From v15.713, for the nonzero comoving k coasting scalar in original ADM normalization,

**P_ddot+(3/tau)P_dot+[beta/tau²]P
=-9[tau J_B_dot+J_B]/[2 k⁴ tau³]**,

where **beta=[8 eta(1+k²)-3k²]/3=1+(8 eta-3)(1+k²)/3**.

The conserved tilted source has **J_B=-k² sigma tau/36**, so the right-hand side reduces exactly to

**sigma/(4 k² tau²)**.

A time-independent particular solution therefore exists:

**P_part=sigma/(4 k² beta)**,

for eta>3/8 and k>0, with beta>1. It solves the sourced Euler equation exactly and is a convenient analytic benchmark for v15.714's Green function. This particular solution does not impose retarded zero initial data; a retarded solution requires adding the homogeneous part to match initial conditions.

The rho0/tau³ component contributes to J_Phi but drops out of this **P-mode** forcing. This does not imply zero metric curvature from that component; physical gravitational potentials, background conditions and detector readout have not been computed.

## Gate 325 — the 2/3 reappearance survives but is not yet a coupling

The same source has exact three-space STF norm

**tr(Q0²)=2 sigma²/3**.

This 2/3 is independent of direction and is the algebraic norm underlying v15.708's summed T/V/S source projection strengths. It is physically separate from beta, the scalar source forcing coefficient **1/4**, and the time-dependent Green kernel: none of those coefficients becomes 2/3 by this derivation. The Archimedes parabolic-segment 2/3 remains a separate exact geometric result without a derived field-theory map. We have identified a rigorous *reason* one 2/3 recurs across angular projectors; we have not deduced a new universal 2/3 gravitational coupling.

**Result:** a nontrivial bridge between exact FLRW covariant source conservation and the previously formal K4 ADM scalar Ward constraint, followed by a closed analytic source-driven scalar displacement. This advances the source-first program beyond pure kinematic projector overlaps. The required final step is still gauge-invariant metric/tidal transfer and an independently motivated physical source action. The v15.713 original v14.935 psi-elimination reproducibility alert remains open for external audit; these equations derive directly from the EH+solid action, not by adopting the broken 0/0 step.

**Reproducibility:** research-notes/k4_flrw_scalar_source_ward_v15_717.py, commit 57c72ef3f4673fcc43a000db8c8720fe1d3f90ad, executed locally to PASS. It verifies exact FLRW conservation, opposite-phase metric/source Fourier pairing, Ward relation, tracefree metric scalar-source contraction, forcing simplification, and constant particular solution. v15.716 independently verified all four stress-divergence equations by direct Christoffel computation.

**HANDOFF:** external audit/gravity/sandbox: (i) check source and metric Fourier phase pairing and g_0z shift conventions against frozen v14.935, (ii) verify the tracefree-source Ward reduction and note how it changes with traceful stress, (iii) independently check the P particular solution and full time-dependent variation, (iv) scrutinize the v15.713 archived state-space 0/0 finding; (v) do not mistake mathematical stress conservation for a physical localized matter realization or identified Einstein-solid tidal detector observable.

**NEXT:** reconstruct the actual scalar metric potential/curvature for this conserved Fourier source using the sourced lapse/shift and the full constrained background field equations, then compare the vector and tensor responses to the same source. A source-independent dimensionless observable must survive explicit mode amplitudes, source geometry and conventional relativistic elasticity, not merely inherit 2/3 from the STF norm.
