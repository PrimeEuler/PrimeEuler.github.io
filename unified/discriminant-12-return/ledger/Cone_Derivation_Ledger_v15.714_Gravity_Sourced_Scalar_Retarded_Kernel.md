# Cone Derivation Ledger v15.714 — Gravity: exact retarded coasting K4 scalar response to a source-compatible ADM perturbation

**Date:** 2026-11-11 US Eastern. **Parents:** v14.930 exact cosmological tensor Euler exponents; v14.935 frozen K4 full SVT action and reported scalar dispersion; v15.712 full source-first scalar mixed action reconstruction; v15.713 exact sourced scalar P equation, Ward-like source compatibility and archived state-space reproducibility alert. **Status:** [D] exact scalar Euler Green function, Wronskian normalization, source convolution and power-law particular solutions on the stable coasting background; [C] physical realization of a source satisfying the archived ADM compatibility identity; [N] no externally normalized gauge-invariant physical scalar tide or unique Cone prediction. **Immediately prewrite HEAD:** 3e8774ccb915f9b48621d9c01b16ec0efed64e9c. Target v15.714 ledger path absent; additive-only, no Suzuki/far-tail modifications.

## Gate 314 — exact scalar mode logarithmic-time frequency

The sourced scalar equation derived from the original coasting K4 action at v15.713 is, for nonzero comoving k and formal ADM source compatibility,

**P_ddot + (3/tau)P_dot + beta/tau² P
   = -9(tau J_B_dot+J_B)/(2 k⁴ tau³)**,

with

**beta = [8 eta(1+k²)-3k²]/3
       = 1 + [(8 eta-3)(1+k²)/3]**.

On the stable interval **eta>3/8**, define

**nu = sqrt[(8 eta-3)(1+k²)/3] > 0**.

The homogeneous solution is exactly

**P_hom=tau^(-1)[A cos(nu log(tau/tau_0))+B sin(nu log(tau/tau_0))]**.

This is an exact mathematical mode shape in logarithmic coasting time, not a new quantum clock nor a lab-gravity oscillator selected by the quarter-grid. The scalar background mode k=0 is excluded because the source-first ADM constraints at v15.711 are singular there.

## Gate 315 — retarded Green kernel and derivative jump

For the differential operator

**L=partial_tau²+(3/tau)partial_tau+beta/tau²**,

the exact retarded Green function at tau>sigma is

**G_R(tau,sigma)=sigma²/(nu tau) sin[nu log(tau/sigma)]**,

and G_R=0 for tau<sigma. Direct symbolic verification gives

**L G_R=0** for tau != sigma,

**G_R(sigma+,sigma)=0**,

**partial_tau G_R(sigma+,sigma)=1**.

These are the correct causal initial-continuity and jump conditions for a unit delta forcing, in the prescribed cosmological time coordinate. At the marginal eta=3/8 limit nu→0 the kernel becomes

**G_edge(tau,sigma)=sigma²/tau log(tau/sigma)**,

which independently satisfies the critically repeated-root Euler equation and the unit jump. This limiting expression is included as a mathematical boundary check; the main sourced result is scoped to eta>3/8.

## Gate 316 — exact response functional and orientation/source cautions

For a prescribed compatible source history J_B(sigma), the response from zero initial data at tau_0 is

**P_src(tau) = -[9/(2 k⁴)] integral_(tau_0)^tau
    G_R(tau,sigma) [sigma J_B'(sigma)+J_B(sigma)]/sigma³ d sigma**.

Equivalently,

**P_src(tau) = -[9/(2k⁴ nu tau)] integral_(tau_0)^tau
 [sin(nu log(tau/sigma))/sigma] [sigma J_B'(sigma)+J_B(sigma)] d sigma**.

This is an exact source-dependent, retarded scalar response on the coasting background. The right-hand side is in the formal ADM Fourier-source normalization of v15.713: a *physically realized* source must still be covariantly conserved in the full K4 FLRW model, give a definite mapping to J_Phi/J_B and specify the detector's metric/tidal readout. Neither the source preparation nor the cosmological background fit is selected by the Cone mesh.

## Gate 317 — analytic source-shape witnesses and an exact formal forcing zero

For a formal power-law shift source **J_B(tau)=J_0 tau^r**, the forcing is proportional to

**tau J_B'+J_B=(r+1)J_0 tau^r**.

When nu>0 and real r, an exact particular solution is

**P_part(tau)= -[9(r+1)J_0/(2k⁴(r²+nu²))] tau^(r-1)**.

Direct substitution into the differential operator verifies it exactly. This is a useful benchmark for numerical source integrations. In particular **J_B ∝ tau^(-1)** gives identically zero P forcing because **d(tau J_B)/d tau=0**; it is a null of the **formal source-to-P forcing operator**, not evidence that a physical gravitational stress at that history produces no spacetime curvature or detector response. The lapse source must also obey the compatibility equation **tau J_Phi'+sqrt(3)J_B=0**.

**Conclusion:** mathematically, the sourced scalar response is now closed to a retarded Green function conditional on the v15.713 formal source. This is substantial improvement over the homogeneous source-free v14.935 analysis, while still no new source-independent G-free tidal observable or fixed EM–G quarter interaction is claimed.

**Reproducibility:** research-notes/k4_scalar_retarded_green_v15_714.py, additive commit 3e8774ccb915f9b48621d9c01b16ec0efed64e9c. Locally executed PASS on the homogeneous differential equation, unit derivative jump, eta boundary limit, exact power-law particular response and the J_B ∝ 1/tau formal forcing zero. No images, no protected object edits.

**HANDOFF:** external audit/gravity/sandbox: verify full v15.713 source-first Euler variation and the unresolved v14.935 state-space 0/0 finding before treating this Green function as a physical scalar response. Verify the retarded kernel/J convolution and power-law benchmark, and separately check the physical FLRW stress-energy conservation and Fermi tidal conversion. Do not confuse the formal shift-source shape null with a physical detector null or with an experimental prediction.

**NEXT:** construct a covariantly conserved K4-compatible localized source and carry its stress through the lapse/shift and solid field equations to a gauge-invariant local tidal response; then test whether the source residues allow independent observation of the three dispersive modes. Without that physical step the v15.706 ratio 3 remains an exact conventional-elasticity model relation.
