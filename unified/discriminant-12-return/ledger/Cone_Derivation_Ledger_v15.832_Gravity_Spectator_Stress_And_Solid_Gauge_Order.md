# Cone Derivation Ledger v15.832 — Gravity: canonical spectator gauge-order validity and the unresolved K4 solid-background transformation

**Date:** 2026-11-12 US Eastern. **Parents:** canonical scalar stress from physical action v15.727; pressure-corrected scalar Ward v15.728–729; independently audited v15.818 source-to-optical five-helicity result; gauge corrections v15.821–822 and full 3D optical null/physical-source overlay v15.830–831. **Immediately prewrite HEAD:** 46fe132db780247f7d23491b97d3afca299a8cc1, target absent. Additive only, Suzuki protected paths untouched.

**Categories:** [D] exact perturbation-order argument that leading quadratic canonical-spectator source is invariant under metric-order infinitesimal diffeomorphism around zero scalar background; [N] does not establish generic gauge covariance of the K4 solid+metric field perturbation at the same order; [O] explicit action-first K4 solid/metric gauge transformation including source and constrained variables.

## Gate 453 — leading canonical-scalar stress and metric gauge order must not be confused

Use explicit amplitude bookkeeping rather than claiming the spectator's full stress is invariant under arbitrary finite coordinate changes. Let ε be the small ordinary canonical scalar amplitude and assume the background scalar vanishes:

**χ=ε χ1+O(ε³)**, **χ_background=0**.

Its stress from the canonical minimally coupled action is quadratic in χ:

**T[χ,g]=ε² T2[χ1,g0]+O(ε⁴)**,

because corrections from the induced metric, which itself begins at O(ε²), first enter T at O(ε⁴).

Take an infinitesimal background-coordinate diffeomorphism generator of the *same perturbative order as the sourced metric*

**ξ^μ=ε² ξ2^μ**.

Then the scalar transforms by pullback

**χ' = χ−ξ^μ∂_μ χ = εχ1 − ε³ ξ2^μ∂_μχ1+...**.

Consequently each derivative of χ changes at O(ε³), and a quadratic derivative product changes only at **O(ε⁴)**:

**(∂χ')_μ(∂χ')_ν − (∂χ)_μ(∂χ)_ν = O(ε⁴)**.

The coordinate-tensor Lie derivative of the already O(ε²) spectator T2 likewise contributes only at O(ε⁴) for ξ=O(ε²). Therefore the **leading spectator stress T2** is unaffected by the O(ε²) pure-gauge metric overlay employed in v15.830–831. This supports reusing the independently audited v15.818 physical source coefficients at that order rather than rerunning its expensive nonlinear source evolution under every small coordinate shift.

This argument depends crucially on the *zero spectator background* and the stated choice ξ=O(ε²). It does not apply to gauge generators taken of order ε or to a scalar with a nonzero cosmological homogeneous background, where lower-order source transformations may occur.

## Gate 454 — why the K4 elastic-solid gauge transformation remains an open dynamical proof

The **coasting background K4 solid** is not zero: its background gradients/stress determine the cosmology and its ordinary relativistic isotropic-solid perturbations. An order-ε² diffeomorphism changes the background metric at order ε² via **δg_μν=−ℒ_(ξ2)g0**, and also changes the solid's background fields and matter stress at that same order. The fact that the spectator stress T2 is unchanged at this order **does not** justify holding the solid perturbations fixed while changing the metric.

An action-first full gauge proof must transform **all K4 solid Stückelberg/phonon variables**, lapse, shift, spatial metric, source stress, emission and reflection event labels, and geodesic endpoint initial data consistently. Then it must verify that the Einstein plus solid constraints and the metric-to-optical worldline observable commute with this transformation. The already audited matched GR+solid comparator makes the expected outcome conventional diffeomorphism invariance, not an independently discovered Cone force.

## Gate 455 — exact algebraic verification and next open physics gate

The additive SymPy reproducer expands an arbitrary real two-coordinate scalar χ1 and ξ2=(T,U) with ε bookkeeping and verifies:
1. The source scalar first changes at ε³ under ξ=ε² ξ2.
2. Every bilinear derivative component (∂χ)_i(∂χ)_j changes first at ε⁴: its ε² and ε³ differences vanish identically.
3. The background metric shift occurs already at ε².

**Reproducer:** research-notes/k4_spectator_gauge_order_v15_832.py, commit **6878f126588fb8d1000a809f64c14446272b48fd**; equivalent local symbolic script executed PASS. This algebra does not explicitly reconstruct all Christoffels, lapse/shift and solid field shifts; this is a transparent perturbative order gate, not a full dynamic proof. No image generation, frozen-object rewrites or G insertion.

**HANDOFF — external audit:** re-run v15.830 3D numerical optical pure-gauge script, v15.831 nonzero source superposition, and this v15.832 SymPy scalar stress power counting. Independently verify that the v15.830 test includes *all* spatial shear ∂iUj+∂jUi and all event terms and that the differential false signal disappears if they are all kept. Require a separate original-K4-action perturbation transformation before marking *general on-shell cosmological gauge covariance* closed.

**NEXT:** derive the full K4 solid Stückelberg and metric gauge variations from the archived v14.935 action, then repeat the detector control for a genuinely remote source and observer. Unless an independently selected Cone operator/scale is produced, the **matched Einstein–Hilbert+relativistic isotropic-solid detector residual remains zero**.
