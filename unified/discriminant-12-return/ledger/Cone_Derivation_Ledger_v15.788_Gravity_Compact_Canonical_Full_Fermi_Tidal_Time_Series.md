# Cone Derivation Ledger v15.788 — Gravity: time-evolving spatially compact canonical matter, full Fermi-frame electric Riemann versus electric Weyl

**Date:** 2026-11-12 US Eastern. **Parents:** v15.727–730 physically sourced canonical spectator and full pressure Ward, independently audited v15.750 evolving compact canonical source to S/V/T electric Weyl, v15.760–761 independently audited Weyl/Ricci detector obstruction, v15.787 direct-metric full local Fermi-Riemann scalar/vector/tensor transfer. **Immediately prewrite HEAD:** 1be7f587f5ffb91cad343bf6ead263e8218e04ea; ledger target path absent; additive-only; Suzuki/far-tail and historical certified assets preserved.

**Status:** [D] exact full-Riemann transfer formulas from v15.787 inserted into the existing v15.750 source dynamics, [N] same positive-energy compact matter source yields distinct full-Riemann and Weyl-only scalar/vector/tensor amplitudes with strong grid/time convergence, [N] still no Cone-specific residual relative to matched ordinary GR+elasticity, [O] finite-arm photon propagation, true far-field retarded detection, full tensor/helicity basis and calibrated physical source strength.

## Gate 402 — same canonical source and K4 equations, now complete local tidal readouts

Retain the identical v15.750 setup *without changing its matter field or source fitting*: a spatially compact C7 massless canonical scalar at tau0=1 on coasting FLRW **a=tau/sqrt3** with box L=8pi, packet cutoff radius R=7, initial chi=w_R[cos(2x)+cos(z)], chi_dot=-chi, and Fourier coefficient K=(2,0,1), k²=5. The scalar itself evolves by its exact Klein–Gordon Fourier mode functions. At each time compute physical energy density, isotropic pressure, momentum source, and their analytic time derivatives; the v15.728 **pressure-corrected** source Ward is checked. The same nonfitted source drives the constrained K4 scalar, vector and tensor modes with zero propagating-displacement initial data at tau0. The nondynamical sourced lapse/shift contacts are retained.

The old **Weyl** readouts were

**W_S=k²(Φ_N+Ψ_N)/(2a²)**,

**W_V=−i k B_V_dot/(4a)**,

**W_T=[tau² γ_T,ddot+tau γ_T,dot−3k²γ_T]/(12a²)**.

Insert the **direct metric-derived local full electric Riemann** formulas from v15.787, in the same scalar STF, transverse vector e1/n, and tensor plus bases:

**R_S=−k² Φ_N/a²**,

**R_V=−i k(B_V_dot+B_V/tau)/(2a)**,

**R_T=−(γ_T,ddot+2γ_T,dot/tau)/2**.

The actual leading small-arm Fermi relative geodesic acceleration is minus each full-Riemann projection times arm separation, not minus the Weyl-only component. Metric background a''=0 ensures the relevant background electric Riemann vanishes at the matched comoving frame, making first-order tetrad contact corrections irrelevant for this local comparison. These quantities are Fourier-normalized complex perturbation coefficients made real by conjugate ±K pairing, not global detector waveforms.

## Gate 403 — two-resolution numerical verification of all six curvature components

Repeat the independently audited v15.750 grid/test settings: **48³ with 21 source times**, and **64³ with 31 source times**, tau∈[1,1.35], eta=3/4, kappa=1. Obtain:

| τ=1.35, model-normalized component | 48³ / 21 | 64³ / 31 |
| --- | ---: | ---: |
| Scalar electric Weyl | +0.22587285 | +0.22587286 |
| Scalar full electric Riemann STF | −0.32852482 | −0.32852483 |
| Vector electric Weyl | +0.03260431 | +0.03260432 |
| Vector full electric Riemann off-diagonal | +0.00584980 | +0.00584981 |
| Tensor-plus electric Weyl | +0.12380786 | +0.12380788 |
| Tensor-plus full electric Riemann | −0.10246657 | −0.10246659 |

All three *full local tidal* sector components are nonzero. The full scalar and tensor change sign relative to Weyl alone; the vector full tide is substantially smaller. Thus the three electric-Weyl numerical amplitudes from v15.750 are **not** an instrument's full Fermi gradiometer reading.

At τ=1, although **P=P_dot=f=f_dot=γ=γ_dot=0**, nonzero sourced lapse/shift contacts and second derivatives give 64³ values:

**Weyl [S,V,T]≈(+0.88249343,−0.47033198,−0.31118537)**,

**full electric Riemann [S,V,T]≈(−1.80489817,−0.94066397,+0.62237074)**.

This is an initial-value constraint/source-contact response, **not** a zero-past-source fully retarded detected wave.

Both grids agree within **2×10⁻⁶** on the displayed initial and final six curvature components. The 64³ analytic Fourier source conservation check retains the v15.750 maximum Ward residual **≈1.34×10⁻¹¹**, compared to ≈3.70×10⁻⁸ at 48³. Curvatures are computed from source-driven field accelerations and constraints rather than differencing numerically sampled Weyl values.

## Gate 404 — full local Fermi observable and the conventional-physics comparator

The local Fermi geodesic-deviation equation for freely falling test masses separated by a sufficiently short proper arm vector ξ is

**d²ξ^i/dT² = −R^i_(0j0) ξ^j**,

with full *electric Riemann*. The full-Riemann results above supply the relevant linearized metric-side curvature and implicitly the sum of physical Ricci sources when the original Einstein constraints are satisfied. They are not a complete realistic interferometer: the spatially compact source has not been propagated to a remote readout via light rays, and no finite-arm null-geodesic transfer/noise/environmental model is supplied. The scalar isotropic full-Riemann component, both vector helicities and the second TT cross component also require independent treatment in a generic multi-arm detector.

The matched GR comparator of independently audited v15.760 remains an **exact null** for Cone novelty at the level studied: using the identical Einstein–Hilbert+isotropic-solid action, matter source, elastic parameter, background, boundary conditions and metric-to-detector functional necessarily produces the identical S/V/T full-Riemann fields. No extra Cone-selected physical operator, coupling or scale has been introduced in the calculation. The dimensionless **2/3** continues to be the standard STF norm rather than a coupling constant.

**Reproducer:** research-notes/k4_compact_canonical_full_riemann_v15_788.py, additive commit **1be7f587f5ffb91cad343bf6ead263e8218e04ea**. The source is an additive transformation of the already audited v15.750 standalone reproducer: the entire matter propagation and K4 forced-mode integrations remain intact; only the v15.787 full-Riemann output channels and comparison assertions were inserted. Independently reconstructed and executed the transformed same-model numerical implementation locally to PASS for both grids, nonzero full tidal components, Fourier Ward checks and 48³/64³ convergence. No historical objects overwritten; no image generator.

**HANDOFF — external audit high priority:** independently re-execute v15.787 and v15.788 from their committed SHA files; compare v15.788's source evolution source-by-source to independently certified v15.750; verify vector shift sign, cosmic-time derivative and contact B_V/tau, scalar Φ_N vs Φ_N+Ψ_N distinction, tensor full Riemann derivative, local orthonormal tetrad and background coasting simplification, six numerical amplitudes, and the exact matched-action no-novelty result.

**NEXT:** an independently physically selected Cone interaction—not a relabeling of Einstein–Hilbert+elastic solid—is required before any matched-detector subtraction can be nonzero. In parallel, a finite-distance null-geodesic detector simulation with the same source is a useful physics implementation benchmark but cannot alone create new Cone gravity. Compare physical source-to-detector histories against an ordinary GR+solid control and report the null if matched.
