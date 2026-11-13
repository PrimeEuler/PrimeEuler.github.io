# Cone Derivation Ledger v15.882 — Gravity: can the null light ray's m/s tag fix the physical length in Gertsenshtein phase matching?

**Date:** 2026-11-13 US Eastern. **Parents:** Sandbox v15.859 leverage-split and v15.860 SI null-ray velocity tags; Muse/Sandbox EM and G transition mesh v15.866–869; Gravity Gertsenshtein standard field and scale-selector tests v15.877–880. **Prewrite live HEAD:** 39bcb4f9645e8aedde103f65fc1e8115e6c52b7b; target absent; additive only, previous certified and Suzuki records preserved.

**Question:** The +c and −c null-ray tags are in metres per second: do they supply the absolute physical scale missing from the EM-half/G-quarter quasi-phase-matching problem?

**Gate 526 — The m/s tag is a physical conversion, not a clock.** Sandbox v15.860's correct SI energy projections are U=E+pc and V=E−pc, which on massive E=gamma mc², p=gamma mv obey U/V=(c+v)/(c−v). For a null ray, distance and elapsed time are connected by z=ct; for a *specified physical period* T, the distance traversed is cT. However c alone has dimensions length/time and cannot select a nonzero length, frequency, spatial wavelength, or magnetic domain spacing. The null-limiting velocity v→c corresponds to the extreme of the kinematic leverage ratio, not a finite scale selector.

**Gate 527 — Derive the actual physically measured mismatch length.** A frequency omega and physically specified photon and graviton refractive indices n_gamma and n_g supply wavenumbers k_gamma=n_gamma omega/c and k_g=n_g omega/c (for propagation under those assumed dispersion laws). The relative wavenumber mismatch is

**Delta k=(n_gamma−n_g) omega/c**.

The complete beat phase is 2pi, so the physical beat length and sign-reversing square-wave magnetic QPM period in the ideal first-harmonic case are

**Lambda_QPM=2pi/|Delta k|=c/[f |n_gamma−n_g|]**, with f=omega/(2pi).

This is a measurable length provided f and the dispersion mismatch are independently supplied. For an incoming wave in vacuum with n_gamma=n_g=1, Delta k=0: no finite coherence-loss beat length exists, and constant-sign B already accumulates conversion coherently (to the weak-mixing limit). Assigning a finite reversal period from an unrelated coordinate q=1/4 in the exactly phase-matched vacuum case can even *reduce* conversion by sign cancellation.

**Gate 528 — check what other physics can provide a length.** A Compton length hbar/(mc) indeed gives a physical length but uses a separately specified mass m and action hbar. Similarly an actual atomic emission/transition frequency supplies the light-ray wavelength but is an independent quantum input. None is fixed by m/s tags or sector half/quarter arithmetic alone. The original EM squared half-step 1/4 and gravity mesh squared half-step 1/16 remain dimensionless and distinct. One may map a mesh half-step to a spatial point only after choosing the physical step length. This is the same scale obstruction as v15.880 but with the SI null-ray notation made explicit, not a novel force or prediction of G.

**Reproducibility:** Original SymPy script research-notes/k4_null_ms_tag_qpm_scale_v15_881.py, commit **4ed06391f3d8418af9a198b6c62545b7d981699e**, contains one caught *assertion target error*: the dimensionless ratio (beat/period)/(c/(n_gamma−n_g)) correctly equals **1** but its original assert mistakenly expects **0**. Do not run the original script as PASS. The strictly additive repair script research-notes/k4_null_ms_tag_qpm_scale_v15_882_replay.py, commit **39bcb4f9645e8aedde103f65fc1e8115e6c52b7b**, replaces this exact assertion in memory and then executes the remaining source. The algebraic expressions were independently verified; post-commit audit of the full replay is pending. No historical bytes were modified.

**Verdict:** [D] the physical speed c closes the *units* gap from time to distance, conditional on an independently supplied period, and turns the physical dispersion mismatch into a beat length. [N] it does not close the *absolute scale* gap by itself. [O] derive an independently justified frequency or length from the Cone sector dynamics and an actual photon–graviton dispersion/source, without importing a fitted physical mass or frequency as a hidden selector.

**HANDOFF external audit/Muse:** check the repaired v15.882 source with both k and beat identities, the signed-Delta versus positive-|Delta| distinction, and vacuum Delta=0 limiting behavior. Challenge any claim that fixed c implies a unique physical wavelength or that the m/s tag alone closes the Gertsenshtein QPM scale gate.
