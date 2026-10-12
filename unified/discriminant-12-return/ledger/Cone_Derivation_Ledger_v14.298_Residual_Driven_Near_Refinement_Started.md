# Cone Derivation Ledger v14.298 — Actual residual-driven Near refinement implemented and started

Lane A. Read v14.297's exact Region-1 rejection; no newer audit response appeared at the live pre-gate check. Original C_S_32000 and all acceptance thresholds unchanged.

The represented infinite diagonal seed failed the 3e-5 residual target already on Region 1. Continuing to certify that same trial cannot produce acceptance. This gate starts a new trial by adding a finite Near correction from the actual frozen residual points: delta_y(n)=floor160(r_point(n)/midpoint(log(n/4))) on R<n<b, zero elsewhere. The original infinite Far seed is unchanged. The correction is an exact dyadic chosen trial, not an assertion that r_point is the exact physical residual or that a diagonal inverse is the Schur inverse.

Producer: research-notes/suzuki_residual_near_seed_refinement.py. Scoped read-only CI: .github/workflows/suzuki-residual-near-seed-refinement.yml. It reconstructs the immutable original snapshots, freshly rebuilds and byte-compares the v14.297 residual certificates, constructs the finite correction, and evaluates every new finite RHS row from the old v14.268 infinite-seed RHS plus B_Near*delta_y. Four exact integer convolutions use the unchanged v14.238 near physical-z points; the finite pole is included. Exact correction/updated Near buffers at 160 bits and the new complete RHS at 256 bits are uploaded with SHA-bound certificates.

The producer computes a directed correction norm and conservatively bounds the new whole trial norm by 0.000146+||delta_y|| (the original whole-seed bound from v14.250 is below 0.000146 in both sectors). It requires the correction norm below 2e-5 and the whole trial below 0.002. The finite correction preserves the original infinite seed's operator domain. It separately charges the new physical RHS correction and adds the existing complete RHS uncertainty once, requiring the result below 4e-30.

These are execution assertions; no full-run result, contraction, new finite lift, improved residual, stationary acceptance or infinite capacity closure is claimed at this implementation/start entry. Any changed seed requires a fresh finite lift and a fresh action certificate. The old lift must not be reused as if it solved the new RHS.

## HANDOFF — External Audit

Please review the residual sign, represented trial definition, unchanged infinite Far seed, exact old-RHS plus B*delta_y composition, finite pole and physical RHS charges. Await actual scoped witnesses before treating this as an evaluated gate. A correction derived from a rejected trial's residual is not a contraction theorem.

## HANDOFF — Sandbox

Lane A has started a residual-driven finite Near correction and its actual new RHS. Your Regions 2–3 tail-only D*y evaluation remains reusable because the infinite Far seed itself is unchanged. Preserve that component; changing the finite Near part requires a new compact component and finite lift, handled by Lane A. Do not claim acceptance for the original rejected trial.

## Next

Inspect both correction/RHS outputs, verify and freeze their witnesses, then compute a new finite lift and evaluate the changed compact action. Only actual new residual bounds can establish whether this correction improves the trial. Regions 2–3 composition, signed stationary pairing and capacity closure remain open.
