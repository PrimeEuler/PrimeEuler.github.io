# Cone Derivation Ledger v15.1413 — Cauchy-initialized H² Weyl-induced current: fixed-z projection issue

**Date:** 2026-11-24 evening Eastern (GitHub UTC Nov 25). **Lane:** Gravity/Cone. **Classification:** [PASS at fixed spatial z] properly reconstruct full spacetime-area tensor and prescribed TT Weyl current from the zero-Cauchy fifth-order sigma correction of v15.1412, yielding a nonzero transverse projected current on a fixed-z slice; [N PASS] spectral N16/24/32 and derivative-step checks and Maxwell oscillator work identity for the **fixed-z sourced surrogate**; **[CORRECTION REQUIRED AND PROVIDED IN v15.1414] this gate incorrectly treats the fixed-z Fourier qx=1,qy=1 source as if it were the full 3D q=(1,1,−1) Fourier coefficient. The physically correct Fourier projection is in v15.1414; use that result instead.** This explicit correction is additive, original files untouched. **Script** `research-notes/k4_cauchy_weyl_maxwell_v15_1413.py` SHA **691c5fb2cdbd8d2b2f61f942ddd1ad3ff80706ae**, exact committed-byte independent Audit replay pending.

## Gate 1350 — field and current construction

The v15.1412 nonlinear sigma correction is `u5=u5part−H_u,v5=v5part−H_v` with zero fifth-order field AND velocity initial values t=0. It no longer depends only on A=t−x and B=t−y, as the homogeneous H evolves the combined initial profile with Fourier spatial momentum magnitude `sqrt(kx²+ky²)`. Construct the full 4-gradient of the two real fields: time derivatives via symmetric step 2e−4, spatial x,y via exact periodic Fourier derivatives. Form the full `B_mu nu=(du_mu dv_nu−du_nu dv_mu)/sqrt(1+u²+v²)` and `K_mu nu=C_mu nu rho sigma B^rho sigma`, where C is computed from the physical **first-order TT vacuum GW** `hxx=cos(t−z), hyy=−cos(t−z)`. Compute current `J^nu=−∂mu K^mu nu` with both time and z centered differences and x,y spectral derivatives. Compare leading, exact normalized area with uncoupled sigma, particular sigma correction, and Cauchy-zero-initial correction.

At t=.7, amp=.3, fixed z=.26, the *fixed-z* Fourier harmonic (kx,ky)=(1,1), after projecting its spatial components using the ASSUMED 3D vector q=(1,1,−1), yielded norms:

| N² | leading | target-metric normalized | periodic particular | Cauchy-initialized |
|---:|---:|---:|---:|---:|
| 16² | .0664853909181 | .0650603864725 | .0650285827242 | .0650745946078 |
| 24² | .0664853909158 | .0650603864703 | .0650285827220 | .0650745946052 |
| 32² | .0664853909165 | .0650603864709 | .0650285827226 | .0650745946061 |

But this projects a *fixed-z slice*, which contains **both** TT Fourier z-harmonics e^{+iz} and e^{−iz}, onto a single hypothesized qz. Consequently none of these numbers is a properly Fourier-separated 3D transverse q=(1,1,−1) source! The internal field and tensor current computed at fixed z remain meaningful; this **mode interpretation** is withdrawn. A fixed-z Maxwell oscillator driven by the source yielded energy 4.1947680274e−6 at arbitrary coupling .05 and source-work discrepancy 5.59e−10, but this is only a **slice-surrogate oscillator**, not the correct physical 3D Fourier Maxwell mode.

**Immediate correction v15.1414:** use 3D z-harmonic projection *before* transverse projection, with distinct harmonic output 0.035962686 and Maxwell energy 1.52221858e−6. The direction-dependent current/energy remains nonzero, but numerical values change substantially. Preserve both records and flag the failure instead of silently correcting old code.

**AUDIT:** replay new v15.1413 and v15.1414 committed sources, check current tensor, real TT harmonic content, qz branch extraction, spatial Fourier normalization and Maxwell source-work; note v15.1413 is explicitly a failed projection comparator, NOT a physical 3D mode certification. **OPEN** genuine full nonlinear Einstein+Maxwell+sigma backreaction, source-side energy debit, finite localized corrections, and intrinsically selected quarter coupling.
