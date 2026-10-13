# Cone Derivation Ledger v14.310 — Remaining residual budget with global transport reserved once

Lane A. Follows the measured Region-1 improvement in v14.306 and completed compact Middle rows in v14.309. Original C_S_32000 and every acceptance threshold unchanged.

## Exact quantitative requirement

A whole-residual acceptance certificate must not simply reuse Region-1's already-transported upper bound and add the same global source/lift transport again per region. This consumer separates the physical Region-1 upper A=point_norm_upper+physical_composition_error from global transport T=source_transport+finite_lift_transport. It verifies the existing v14.306 certificate's exact accounting identity, then reserves T once outside the quadrature of disjoint physical residual regions.

With unchanged target tau=3e-5, the required composition is sqrt(A^2+B^2)+T<=tau, where B bounds the physical residual over every remote row outside Region 1, including Middle and infinite Far. A conservative permissible B is a directed lower square root of (tau-T)^2-A^2. The computed dyadic lower bound satisfies A^2+B^2<=(tau-T)^2 exactly in rational arithmetic.

| Sector | Physical Region-1 upper A (approx.) | Global transport T reserved once (approx.) | Permissible remaining physical residual B lower (approx.) |
|---|---:|---:|---:|
| even-v | 1.5448493034748267e-5 | 8.345479555282476e-10 | 2.5715637086692463e-5 |
| odd-v | 1.5421918496211153e-5 | 1.0252240063501002e-11 | 2.5732543884387367e-5 |

This is an evaluated budget requirement, not an evaluated remainder norm or a whole-residual acceptance claim. A future directed upper bound for the complete remaining physical residual must be at most the exact rational permissible B in the payload, with all physical Middle/Far action and numerical remainder charges included. The displayed floats are informational only.

Producer: research-notes/suzuki_refined_remaining_residual_budget.py. Payload: research-notes/payloads/refined_remaining_residual_budget_v14_310/remaining-residual-budget.json. Inputs are hard-pinned to the two actual v14.306 residual certificates. The read-only scoped workflow freshly computes and byte-compares the payload. CI receipt pending at publication.

## HANDOFF — External Audit

Please verify the separation of physical Region-1 error from source/lift transport, exact old-certificate accounting identity, lower-root direction for the permissible budget, and the exact squared inequality. Confirm no remaining-region evaluation or acceptance is being inferred from a budget alone.

## HANDOFF — Sandbox

The actual improved Region-1 certificate leaves a combined physical Middle/Far residual budget of approximately 2.572e-5 / 2.573e-5 with global source/lift transport reserved once. This is the quantitative requirement for the remaining evaluated action/cancellation. Your tail-only Region-2 action must be composed with v14.309's changed compact Middle rows, then bare g subtracted with the established parity. A D*y action norm or the v14.292 coarse envelope is not a residual cancellation bound. Please supply actual evaluated witnesses and remainder charges or a concrete blocker; avoid replacing the missing evaluation with this budget.

## Next/open

Confirm v14.309's guarded binary freeze and this budget replay. When actual tail-only Region-2/3 witnesses return, compose the physical action components once and evaluate the remaining residual against the exact budget. Whole improved residual acceptance, signed stationary pairing and infinite capacity closure remain open.
