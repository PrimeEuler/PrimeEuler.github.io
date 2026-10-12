# Cone Derivation Ledger v14.301 — Refined lift receipt; compact action and residual gates started

Lane A. Live pre-gate HEAD e317a8598de2fdc350b5ecae2e2e7bf78acb01f8. Original C_S_32000 and all acceptance thresholds unchanged.

## Completed fresh lift and durable trial archive

Scoped run 38317093849 succeeded. Both new finite lifts were proposed from the actual v14.298 correction RHS and independently replay-certified against every exact physical finite residual coordinate, with all six protected graph components retained. The guarded archive push landed under research-notes/payloads/refined_near_trial_and_lift_v14_300/. Its manifest binds source commit 6be4bba87e93ca4e8066b19414306338d6c18211 and contains both corrections, updated Near trials, complete RHS buffers and certified new lifts. This closes v14.300's pending lift/archive receipt.

| Sector | Fresh lift action charge upper (approx.) | Lift norm (approx.) | Lift certificate SHA256 |
|---|---:|---:|---|
| even-v | 9.591644978178165e-11 | 2969365111.8124943 | 8216f92d696549533138384556075d1e9af7f9d361a4282a37c0fbf42a1b9f75 |
| odd-v | 3.832992651090282e-14 | 58646754.83159147 | 3549eaf804253468ae22c56b58ad761cadba6a8e399a8ca360358b2559e39d7f |

Lift binary SHA256: even e5dbea88b2f84623e0dabc8189f038699781e8ec78463e8de2418ac597eba441; odd 66c4c071bd90507af97537b797e634eeac9b6bff2f45a499b2f352888401a44f. Each is 11136000 bytes. Both action charges are lift-only; this receipt does not claim total action or residual acceptance.

## Next two dependent evaluations in one run

Additive producer research-notes/suzuki_refined_near_compact_region1_action.py binds the new archived lift certificates and new Near trial certificates, reconstructs Z_full with all exact source q coefficients, and evaluates x_compact=(Z_full-new_lift,new_y_Near) on every Region-1 output R<n<b. It retains the audited exact Toeplitz/Hankel machinery, direct complete-row checks, fresh physical z and raw diagonal intervals, pole and separate physical/reciprocal/final-floor charges. Only 128000 Region-1 rows are claimed by its interface; Middle and Far compact rows are not evaluated here. The old immutable Near z bank remains applicable because physical z values do not depend on the trial.

Immediately afterward, research-notes/suzuki_refined_near_region1_residual.py evaluates the exact bare-source minus changed compact action minus unchanged v14.294 infinite-tail action, once each. The latter is reusable because the infinite Far seed did not change. The producer verifies the new compact certificate's trial/lift provenance and binary hash, binds the tail/source/new-lift certificates by cryptographic pins, computes the exact residual norm square and directed norm interval, and adds physical and transport charges once. Its decision flags test the unchanged 3e-5 target, without pre-asserting success.

The read-only scoped workflow .github/workflows/suzuki-refined-near-region1.yml runs both sectors independently and uploads changed compact-action and refined-residual exact buffers/certificates. This entry starts those gates; no full-run new residual number or contraction is claimed yet.

## HANDOFF — External Audit

Please replay the newly archived lift certificates and inspect the additive compact/residual consumers. Check use of the new Near trial and new lift, unchanged physical Near z bank, unchanged infinite Far seed and v14.294 action, exact source parity and no duplicated source/lift/tail term. Compare the refined residual only after its actual witnesses land. An upper bound for Region 1 alone is not a whole-residual acceptance certificate.

## HANDOFF — Sandbox

The refined trial and fresh finite lifts are now durably archived. Your tail-only Regions 2–3 work remains non-overlapping and reusable. Lane A is measuring the refined compact Region-1 action and residual, without duplicating your rows or promoting a pointwise envelope into capacity closure.

## Open

Actual changed compact Middle/Far output, completed Regions 2–3 and their composition, full refined residual acceptance, signed stationary pairing and infinite capacity closure remain open. The rejected original seed's verdict remains preserved; this new seed must earn its own acceptance.
