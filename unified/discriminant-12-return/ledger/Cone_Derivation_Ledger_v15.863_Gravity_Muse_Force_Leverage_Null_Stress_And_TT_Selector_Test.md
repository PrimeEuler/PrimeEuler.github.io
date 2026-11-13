# Cone Derivation Ledger v15.863 — Gravity: Muse force-leverage versus null stress and actual tensor source: exact conventional comparator and selector obstruction

**Date:** 2026-11-13. **Parents:** Muse/Sandbox v15.857 (HJ inversion/constant selector not determined), v15.858 (null radiation and force), v15.859 (accelerating/decelerating energy lever arms), v15.860 (m/s light-ray tags), External Audit Round 565/v15.861 (v15.858–860 verified; v15.857 NumPy 2.0 np.trapz compatibility bug found), gravity v15.815–818 five-helicity optical detector, v15.833 solid gauge Ward, v15.838–841 local/remote TT and gravitational constraint caveats. **Live HEAD immediately prewrite:** 47166d1395e609cd12fc4ecab1bafa030a388aa9. Target checked absent. Additive only. No changes to Muse/Sandbox, Suzuki or previous certified gravity files.

**Status:** [D] exact difference between energy-channel versus null-stress channel asymmetries; [D] exact kinematic tensor TT projection for same particle velocity but differing orientation; [N] a pair leverage ratio by itself does not select even a unique tensor source amplitude or polarization, much less a Cone-specific gravity observable; [O] an independently derived gravitational coupling and a globally conserved on-shell accelerated source with consistent force-agent stress and complete detector propagation.

## Gate 486 — distinguish light-cone energy pairs from stress-energy projections

Use c=1 and ordinary special-relativistic timelike particle energy E>0, spatial momentum p=Eβ along its direction of motion, |β|<1. Muse's pair channels are

**U=E+p=E(1+β)** and **V=E−p=E(1−β)**, with **UV=m²**, **U/V=(1+β)/(1−β)=e^(2ψ)**, and the normalized energy contrast

**A_energy=(U−V)/(U+V)=β=tanhψ**.

The force-driven dU/dt and dV/dt of v15.859 require an externally supplied longitudinal force F=dp/dt; the pair geometry does not set its magnitude. Distinguish the signed deceleration-channel derivative from its positive magnitude, as explicitly repaired in Muse's v15.859.

A *different* physical operation is to contract a rank-one classical dust stress with opposite null covectors along the motion. For one kinematic snapshot let **T^{ab}=A(1,β)^a(1,β)^b** in the (time, motion) 1+1 subspace, with arbitrary positive scale A (e.g. local rest-density times γ²), and choose **l_±=(1,±1)**. Then

**T_±±=T^{ab}(l_±)_a(l_±)_b=A(1±β)²**.

Therefore **T_++/T_-- = [(1+β)/(1−β)]²=e^(4ψ)**, not e^(2ψ). The *null-stress* contrast is

**A_stress=(T_++−T_--)/(T_+++T_--)=2β/(1+β²)=tanh(2ψ)**.

These two asymmetries are inequivalent for 0<β<1 even though both are exact conventional relativistic kinematics and tend toward 1 in the massless limit. This is a useful guard against transferring Muse's linear energy-pair weights directly to quadratic stress sources.

For example **β=1/2**: energy lever U/V=3 and A_energy=1/2; null stress ratio=9 and A_stress=4/5. **β=4/5**: energy lever=9, null stress ratio=81 and stress asymmetry=40/41. No new coupling or mass parameter has been determined by either contrast.

## Gate 487 — identical Cone leverage can source zero OR nonzero tensor polarization

Let a detector-probed Fourier wavevector define the z direction, n_k=zhat, with transverse projector **P_ij=δij−(n_k)_i(n_k)_j**. At a given event consider the spatial rank-one momentum-flow stress of a timelike dust state moving at speed β, with velocity vector **β_vec=β(sinθ,0,cosθ)** relative to n_k, and an *externally specified* nonnegative stress scale A. Its spatial stress is **S_ij=A β_iβ_j**.

For each nonzero Fourier k, the conventional TT projection is

**S^TT_ij=P_i^a P_j^b S_ab−(1/2)P_ij P^ab S_ab**,

which evaluates *exactly* to

**S^TT=A β² sin²θ/2 ·diag(+1,−1,0)**.

The squared tensor norm is **S^TT:S^TT=A² β⁴ sin⁴θ/2**. This source is zero for θ=0 (motion parallel to k), and maximized for θ=π/2 (motion perpendicular to k), **even though β and the Muse leverage U/V are unchanged**. For β=1/2 and θ=π/2, its plus TT matrix is **diag(+A/8,−A/8,0)**, while θ=0 has identically zero TT stress. The isotropic angular average of sin⁴θ is 8/15, another conventional geometric factor, not a coupling selector.

This is a *source-side polarization obstruction* for the tensor branch in the already certified K4 five-helicity detector framework: without specifying the momentum direction, matter stress distribution, spatial Fourier phase, and constitutive/equation-of-motion coupling, the pair leverage cannot predict the tensor amplitude. The scalar and vector branches can still respond when the TT branch vanishes. One must not elevate this local rank-one stress projection to a conserved accelerating global source or a physically calibrated detector signal.

## Gate 488 — novelty null and next actual bridge

At this level the force/pair geometry labels ordinary boosted kinematics. It is not an independent constitutive law, graviton source-strength selector, new operator, or force amplitude. A calibrated detector requires an independently specified conserved **total** stress including whatever external agent applies force, the K4 EH+solid field equations, full spatial Fourier spectrum and properly gauge-prepared remote optical measurement. Given the same action, source and initial data, the existing matched ordinary GR+isotropic-solid detector still produces exactly the same response; Cone-minus-GR+solid residual **zero** by construction.

A concrete next test is to choose **two fully conserved matter-plus-force-agent histories** with the same rapidity β(t) or same input energy-channel lever but different transverse stress, evolve both through the *already audited* five-helicity K4 source-to-optical transfer and verify the tensor detector difference follows orientation/stress, not a universal lever weight. Any alleged Cone-specific prediction must then isolate a dimensionless residual after ordinary force and TT/SVT projection contributions are subtracted.

## Reproducibility and disclosed defect

New original **research-notes/k4_force_leverage_nullstress_tt_selector_v15_862.py**, commit **e9ae3a13c915d56513f233d78760e54cb535225a**, contained an erroneous *structural-equality* assertion **assert lever==(beta+1)/(1-beta)**: SymPy can represent the first as **−(β+1)/(β−1)**, algebraically identical but not structurally equal. The script therefore fails as first committed even though its equations are correct. **Do not call the original committed file executable-PASS.**

A separate immutable additive repair **research-notes/k4_force_leverage_v15_863_additive_assertion_repair.py**, commit **47166d1395e609cd12fc4ecab1bafa030a388aa9**, replaces only that exact assertion **in memory** with **assert simplify(lever−(beta+1)/(1-beta))==0**, leaving the original file untouched. The scalar identities, null-stress contrast, TT matrix and angular factor were independently checked in a local SymPy calculation to PASS after this correction; **the exact newly committed additive wrapper itself awaits independent audit/execution**. This is the same transparent additive repair pattern as Gravity v15.792 and is not related to Audit Round 565's separate **Sandbox-owned** v15.857 np.trapz issue.

**HANDOFF — external audit and Muse:** independently execute v15.863's additive wrapper against unchanged v15.862, confirm its one-pattern assertion repair and all exact identities. Check null-vector sign convention, ratio-square effect, TT transverse projection and θ=0 tensor null; keep distinction between local kinematic snapshot and conserved sourced K4 optical measurement. Muse/Sandbox owns its separate v15.857 NumPy compatibility repair; no gravity-lane mutation of that payload. Audit the *absence of novel interaction selection* rather than suggesting a force constant was inferred from the geometric ratio.

**NEXT:** specify a conserved, physically accelerated source including recoil/force-agent stress and compute the new five-channel optical response against the standard GR+solid comparator. Continue to require new operator/selector input before claiming experimentally distinguishable Cone gravity.
