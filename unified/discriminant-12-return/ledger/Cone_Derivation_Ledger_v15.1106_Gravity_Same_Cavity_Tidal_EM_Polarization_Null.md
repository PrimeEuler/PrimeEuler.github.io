# Cone Derivation Ledger v15.1106 — Same-cavity two-polarization tidal energy-transfer null and normalized differential detector

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] equal-and-opposite first-order fractional tidal work for two phase-matched, degenerate transverse electromagnetic cavity polarizations exposed to the same finite plus-polarized gravitational strain; [N] the ratio -1 is exactly standard Maxwell+GR, not Cone-specific, and no frequency, phase or new G selected; [O] real finite boundary cavity elasticity, wall orientation, K4 constrained tidal source, damping, multiple physical couplings. **Live HEAD immediately prewrite:** 78338ded385b8df224f534daa45918cc6cd5cae4; no collision with prior Audit v15.1104 or Gravity v15.1105. Additive-only writes; no historical certified, Suzuki, Audit, Sandbox or Muse file edited.

## Parent gate, Audit and test apparatus
Latest independent external Audit Round 594/v15.1104, commit 901047a8e0e57f777f0c6a75d91efacbd75935b9, independently verified v15.1100–1103, all exact scripts passing. Gravity v15.1105, immediately preceding this gate, derived the exact *first-order weak-TT Maxwell action* for two transverse standing modes along x in a narrow-in-z ideal cavity while the plus-polarized gravitational pump travels along z:
L_y=1/2[(1+h)Qdot_y²-omega² Q_y²],
L_z=1/2[Qdot_z²-omega²(1-h)Q_z²].
This gate checks a same-apparatus polarization ratio/null, not another tidal source theory. Take a lossless slab cavity with perfectly conducting boundaries at fixed x, common frequency omega and equal normalized seed amplitude A, phase phi, with the same metric strain h(t) across the mode. This ideal slab ignores real z-boundary support and wall motion; real instrument design may spoil exact degeneracy.

## Gate 966 — first-order matched polarization work
For a smooth compact GW pulse with no strain before/after and in the fixed-wall, negligible-backreaction approximation, v15.1105 showed exact first-order perturbative energy work
Delta E_y/E0=+omega ∫h(t)sin(2omega t+2phi)dt+O(h²),
Delta E_z/E0=-omega ∫h(t)sin(2omega t+2phi)dt+O(h²).
For the *even* finite wavefront from Gravity v15.1102 define Hcos(2omega)=∫h(t)cos(2omega t)dt, yielding
**delta_y=+omega sin(2phi) Hcos(2omega)+O(h²)**,
**delta_z=-omega sin(2phi) Hcos(2omega)+O(h²)**.
At equal initial E0, the normalized **sum** delta_y+delta_z=0+O(h²), and differential delta_y-delta_z=2omega sin(2phi)Hcos+O(h²). When the common leading overlap is nonzero, their first-order **ratio** delta_y/delta_z=-1; at a spectral zero or phi=0 it is an indeterminate 0/0 and must not be reported as a measured -1. The sum-null and differential contrast follow automatically from the plus-TT traceless polarization acting on standard Maxwell stress. A cross-polarized GW would rotate/mix the two modes instead of this diagonal fixed-basis form.

## Gate 967 — how much can normalization remove?
The ratio -1 cancels the common strain amplitude, source G, and pulse shape *under the equal-frequency, equal-phase, equal-overlap, equal-boundary hypotheses*. This is mathematically a G-free dimensionless relation, but it is **not independent of standard Einstein–Maxwell theory** and therefore not a new Cone gravitational observable. The differential amplitude still contains the real, externally sourced tidal waveform Hcos (from v15.1102 with G inserted). A realistic physical cavity requires the GW's actual propagation direction, transverse plus/cross axes, polarization eigenfrequencies, wall motion and elasticity, background charges/fields, finite-Q damping, and wavefront gradients; none of these are determined by the arithmetic ±1/4 / ±1/2 mesh. If two EM phases differ, the cancellation generally fails:
delta_y+delta_z = omega Hcos[sin(2phi_y)-sin(2phi_z)].
If modes are empty classically, both remain empty in the homogeneous linear equations. Static electric/magnetic background linear forcing (inverse Gertsenshtein channel) is separate and requires power/charge sources.

## Gate 968 — provenance and next proposed work
Reproducer: research-notes/k4_same_cavity_polarization_tidal_null_v15_1106.py, commit 78338ded385b8df224f534daa45918cc6cd5cae4. Its core exact SymPy assertions were run locally and PASS: equal-seed sum-null, opposite-sign differential response, finite source waveform and noncancellation for differing phases. Independent Audit pending.

**Positive:** user's peak/turning-point insight now supports a concrete *differential polarimetric detector channel* with an internal null (same ideal cavity, two EM polarizations). **Negative:** this null is a conventional symmetry of the TT metric's Maxwell action, not the Cone scale/weld or a new physical coupling. **NEXT:** allow the cavity walls to move consistently with the tidal strain and explicitly compute how much of the ideal sum-null survives, then compare to standard Einstein–Maxwell+elastic-wall baseline. The physically meaningful test is whether any additional action-derived Cone vertex creates a nonzero *matched* deviation from the standard null after the same device/system conditions, not merely whether gravitational energy can pump EM.
**AUDIT HANDOFF:** validate equal-frequency/equal-seed assumptions and tracefree plus-TT Maxwell vertices, ratio only off spectral zeros, different seed phase violation, cubic/higher source corrections absent from first-order comparator, and clear distinction between this standard theory polarization null and any claimed Cone-specific selection.
