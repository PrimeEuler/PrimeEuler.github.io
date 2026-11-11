# Cone Derivation Ledger v15.682 — Gravity lane: same-center degenerate Maxwell-mode dispersion discriminator

**Date:** 2026-11-11 US Eastern. **Parents:** v15.679 traveling tensor/EM phase matching and static-field seed; v15.680 finite fixed-wall cavity, seeded omega_c resonance and traveling 2:1 null; v15.681 normalization/translation audit showing the separated two-length 1D ratio loses its apparent O(m_T^2) phase and retains only O(m_T^4) internal amplitude sensitivity. **External audit:** Round 540 commit b18a21051d19bd3ed4215afe9eadf386e916644b confirmed v15.676/678/679/680 independently. **Status:** [D] calibrated on-resonance same-cavity mode ratio from the covariant cavity power formula; [D] exact vector Maxwell eigenmodes and exact prescribed-TT effective-current overlap in one centered PEC cube; [D] same-center O(m_T^2/omega^2) amplitude slope for a timelike prescribed tensor wave; [C] identification of that timelike prescribed tensor with the K4 elastic-gravity mode and its mechanical wall response; [N] no universal/parameter-free Cone coefficient and no quarter-grid temporal selector. **Immediately prewrite live HEAD:** 9f264850d40221a4975f4a3e542d7a92f83ea353. Collision searches found no v15.682 ledger entry or prior same-center ledger result. Frozen Suzuki certificates and prior audited objects untouched.

**External comparator:** Gué, Krokotsch, Moortgat-Pick, “Covariant eigenmode overlap formalism for gravitational wave signals in electromagnetic cavities,” JCAP 08 (2026) 058, arXiv:2602.08507. Their formalism expands the observed electromagnetic signal in normalized cavity eigenmodes, includes dynamic elastic boundaries and backreaction, and gives the on-resonance magnetostatic signal power in terms of the total bulk+boundary coupling. This gate uses their ordinary-GR cavity result as the experimental comparator; the K4 substitution is explicitly conditional.

## Gate 215 — calibrated same-cavity mode ratio cancels h, B0 and volume

For a monochromatic GW on an electromagnetic resonance, the covariant magnetostatic result is

**P_n = (1/2)(omega_n/Q_n^ext) V Q_n^2 |eta_n^bulk+eta_n^bdy|^2 B0^2 h^2.**

Define the experimentally calibrated quantity

**C_n = P_n Q_n^ext/(omega_n Q_n^2).**

For two modes a,b in the **same physical cavity** with the same static bias and incident wave,

**sqrt(C_a/C_b) = |eta_a^tot/eta_b^tot|.**

Thus the unknown strain amplitude h, static magnetic-field magnitude B0 and cavity volume V cancel. On resonance the total bulk+boundary coupling is the coordinate-consistent observable in the comparator formalism up to the stated O(1/Q) approximation. This ratio construction is conventional cavity electrodynamics, not a Cone prediction.

The high-frequency TT/free-fall limit is particularly clean: the TT boundary term vanishes for the standard massless comparator and the response is controlled by the bulk effective-current overlap. This suggests testing whether two *co-centered, degenerate* vector Maxwell modes can respond differently to K/omega without the baseline phase artifact found in v15.681.

## Gate 216 — exact co-centered PEC Maxwell pair has unequal K dependence

Take an ideal perfectly conducting cube

**(x,y,z) in [-pi/2,pi/2]^3**, **V=pi^3**, c=1,

and the two exact solenoidal electric eigenmodes

**E_17 = 2 zhat cos(x) cos(7y),**

**E_55 = 2 zhat cos(5x) cos(5y).**

Both obey the PEC tangential-E and normal-B boundary conditions. Their magnetic fields follow from curl E=-i omega B. Direct integration gives

**integral |E_17|^2 dV = integral |B_17|^2 dV = V,**

**integral |E_55|^2 dV = integral |B_55|^2 dV = V,**

and the modes are orthogonal. They are exactly degenerate:

**omega_17^2=1^2+7^2=50, omega_55^2=5^2+5^2=50.**

Now choose a uniform static magnetic bias **B0=B0 zhat** and a cross-polarized prescribed TT tensor wave propagating along +x,

**h_yz=h_zy=H(t,x), h=0, h_0mu=0.**

Applying the general linearized Maxwell effective current

**J_eff^mu = -(1/2)(partial_nu h) Fbar^(mu nu) - partial_nu(h^nu_rho Fbar^(rho mu)-h^mu_rho Fbar^(rho nu))**

to this tracefree background gives exactly

**J_eff^z = -B0 partial_x H**, with the other components zero.

For **H=h exp[i(omega t-Kx)]**, therefore **J_eff^z=i K B0 H**. The normalized TT bulk coupling contains a common factor K/omega multiplying the spatial overlap; that common factor cancels between the two degenerate modes. The exact geometry integrals are

**G_17(K)=8 cos(pi K/2)/[7 pi^2 (K^2-1)],**

**G_55(K)=-8 cos(pi K/2)/[pi^2 (K^2-25)].**

Hence the signed overlap ratio is

**G_17/G_55=(25-K^2)/[7(K^2-1)].**

For the ordinary massless traveling comparator **K=omega=sqrt(50)**,

**|eta_17/eta_55| = 25/343.**

No cavity-center displacement or propagation baseline appears: both modes occupy the same volume and use the same physical origin.

## Gate 217 — same-center ratio restores a genuine quadratic timelike-dispersion slope

Define a baseline-normalized mode-ratio observable

**D = |eta_17/eta_55| / (25/343).**

Conditionally let the tensor wave be timelike at the same measured temporal frequency,

**K^2=omega^2-m_T^2=50(1-mu^2), mu=m_T/omega.**

In the neighborhood of the massless point, the exact ratio becomes

**D(mu) = (1-2 mu^2)/(1-(50/49)mu^2)**

and therefore

**D(mu)=1-(48/49)mu^2-(2400/2401)mu^4+O(mu^6).**

This is the key distinction from v15.681: **the O(m_T^2/omega^2) term survives in a same-center, translation-invariant amplitude ratio.** The earlier quartic result was not a universal no-go; it resulted from the special two-length 1D overlap whose first derivative vanished after the center phase was removed.

If the existing K4 local tensor dispersion is inserted conditionally,

**m_T^2=(8 eta/3)H^2, 3/8<eta<=3/2,**

then

**D_K4 = 1 - (128 eta/49)(H/omega)^2 + O[(H/omega)^4].**

This quantity is dimensionless and contains no inserted measured Newton G. It is experimentally distinguishable in principle from the standard massless value D_GR=1, provided the source and detector model really realize the assumed K4 tensor wave.

## Gate 218 — positive discriminator, negative Cone-selector verdict

This gate changes the finite-cavity conclusion in one precise way: a **co-centered multimode geometry can retain quadratic sensitivity to non-null tensor dispersion while canceling h, B0, Q calibration factors and placement phase**. That is a real analytical positive result of the prescribed-Maxwell calculation.

It still does **not** establish a new parameter-free Cone gravitational observable:

1. D measures a generic dispersion relation K/omega; a massive/non-null tensor wave from another theory, a medium-induced propagation effect, or an incorrectly modeled source could produce a similar shift.
2. The K4 coefficient contains eta and H. The Cone quarter/half lattice has not selected eta, tensor amplitude, source frequency, source phase or a temporal 2:1 relation.
3. The Gué et al. gauge-consistent boundary cancellation was derived for ordinary GR gravitational waves. The prescribed timelike TT Maxwell source above is exact as a linearized metric exercise, but identifying it with a physical K4 wave requires a K4-consistent detector-frame metric, polarization constraints and elastic-wall equation.
4. For any regime with omega/H >> 1, the conditional K4 signal remains suppressed as (H/omega)^2 even though the geometric ratio avoids the extra quartic penalty of v15.681.

Accordingly classify **D** as a **conditional G-free dispersion discriminator**, not yet a Cone prediction and not evidence that the 1/4 gravity mesh pumps the 1/2 EM mesh.

**Reproducibility:** research-notes/same_center_degenerate_maxwell_dispersion_v15_682.py, initial additive commit 7bac36a8aef12337af0e5ec33f5717e799caae91 and robustness repair 9f264850d40221a4975f4a3e542d7a92f83ea353. The script derives the effective current tensorially, verifies exact PEC electric/magnetic mode normalization and orthogonality, checks the analytic overlaps at the physical massless operating point, and proves the exact timelike ratio and -48/49 quadratic coefficient. The Piecewise repair only handles SymPy removable special branches at K=+-1,+-5; it does not change the physics. No figures and no Suzuki/protected-object modifications.

**HANDOFF:** independent audit/sandbox/gravity should verify: (i) the two exact PEC modes and normalization; (ii) J_eff^z=-B0 partial_x H for the cross-polarized tensor and static B0 zhat; (iii) the overlap ratio and massless 25/343 baseline; (iv) the exact -48/49 coefficient; (v) whether a K4 timelike tensor admits the assumed TT/free-fall detector-frame reduction or acquires extra polarization/boundary terms. Reject any claim that this ratio is uniquely Cone unless eta/source selection is separately derived.

**NEXT:** search the family of exactly degenerate same-cavity Maxwell mode pairs for the geometry derivative **partial_(K^2) ln|eta_a/eta_b|**. Determine whether the O(m_T^2/omega^2) coefficient is bounded at fixed nonzero massless coupling or can be made arbitrarily large only by tuning one baseline overlap toward a node. Then incorporate realistic mode Q/readout penalties. This decides whether the quadratic discriminator is merely algebraically nonzero or can be engineered into a robust experiment.
