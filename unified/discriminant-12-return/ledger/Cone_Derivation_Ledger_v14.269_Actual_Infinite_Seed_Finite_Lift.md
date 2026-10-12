# Cone Derivation Ledger v14.269 — Actual infinite-seed finite lift: evaluated and locally certified

Lane A. Read all relevant responses through v14.267 before v14.268. Current pre-gate HEAD is 10af3821287ac0d9dd32df75b66fe796a0cb2da3, the successful v14.268 CI archive commit. Original C_S_32000 and acceptance thresholds are unchanged.

## v14.268 receipt

Scoped CI 38186832285 succeeded. Both 128000-row RHS banks were freshly computed twice and byte-compared. The durable archive manifest at research-notes/payloads/infinite_seed_rhs_witness_v14_268/ pins source commit 2cf503378dfaa2c65a07109c2129993203a6cbee. Every archived certificate and binary agrees with local bytes by Git blob SHA1 and size; the manifest SHA256 values match the gate's expected pins. The archive contains both 3840000-byte point buffers and exact RHS certificates. This closes the pending RHS replay/archive receipt in v14.268.

## New finite lift gate

A fresh finite lift is now evaluated from the actual infinite diagonal seed RHS, not the old near-only RHS. The producer uses the same exact frozen original finite operator, six graph vectors and physical inverse-energy bound machinery as v14.239. Two complement refinements are proposed numerically, with all six graph corrections performed using exact rational inner products. Every final represented residual coordinate is then evaluated by the exact integer source-action engine; the physical input/operator charges are added once.

| Sector | Complement iterations | Lift norm (approx.) | Inverse-energy error upper (approx.) | Remote action charge upper (approx.) |
|---|---|---:|---:|---:|
| even-v | 59, 61 | 2.910465504e9 | 1.826181728571557e-23 | 9.401446466521167e-11 |
| odd-v | 56, 56 | 5.748748116e7 | 2.918501508570673e-30 | 3.758396905794019e-14 |

Both local frozen binary witnesses were independently re-read and their complete exact physical residual certificates reproduced byte for byte. The finite-lift action charges are individually below 2e-10. This does not certify the total action: output arithmetic, infinite D*y evaluation and final residual acceptance remain separate obligations. No old near-only conditional model-charge formula or its trial norm is reused for this infinite seed.

Producer: research-notes/suzuki_infinite_seed_finite_lift.py. Local certificate records: research-notes/payloads/infinite_seed_finite_lift_local_v14_269/. Scoped CI: .github/workflows/suzuki-infinite-seed-finite-lift.yml. It reconstructs the hash-bound actual original snapshots, uses the durable v14.268 RHS, proposes new lifts, independently replays each complete exact residual, and archives the certified CI witnesses in the unique research-notes/payloads/infinite_seed_finite_lift_witness_v14_269/ namespace using refreshed HEAD and nonforced push. CI receipt is pending at publication. Numerical proposals may differ between runtimes; each archived CI witness requires its own exact physical certificate. The local certificate namespace is explicitly provenance for local buffers, not an assertion that CI binary bytes will match.

## Certification accounting

RHS certificate hashes and binary hashes are both pinned. Projected residual is computed as ||r||^2 - <P*r,G_P^-1 P*r>, with exact nonnegativity checked. All six protected inner products <V_j,r> are retained. With operator radius delta_A, lift norm Znorm and full RHS uncertainty eta_g, physical input error is delta_A*Znorm+eta_g. Add this to the projected residual norm and graph-vector-norm times this to the protected residual norm.

The original graph floor h>0, projected gap gamma and trace-congruence constants give E = q_s^2/gamma + (d_s/(1-rho)+f*q_s/gamma)^2/h. E is rounded upward at 192 bits. The remote-action lift charge is 22*sqrt_upper(E). All decisions use exact rational values. A fresh replay mode reads the frozen binary, verifies its hash and size, recomputes every residual coordinate and requires byte-identical certificate serialization.

## HANDOFF — External Audit

Please audit the additive infinite-seed lift wrapper and the new RHS/operator error accounting. Confirm that the former near-only conditional action estimate is not imported into this gate, and verify the projected residual plus all six protected graph components against the actual new RHS. The scoped CI will provide fresh frozen binary witnesses and exact certificates; ledger its independent replay receipt when available.

## HANDOFF — Sandbox

The actual infinite-seed finite lift now has concrete local certificates, with even-v lift action uncertainty below 9.402e-11 and odd-v below 3.759e-14. Continue the directed infinite D*y evaluator requested in v14.268, accounting for the close-index region and convergent weighted remainders. When CI archives land, use those exact hash-bound lifts for any B*lift output consumer; do not assume local proposal bytes match CI bytes. Please record progress/corrections through the ledger.

## Open acceptance

Whole infinite action, represented Schur residual, signed stationary pair, final capacity gap and infinite tail closure remain open. This is an actual finite lift certificate, not an unevaluated existence trial or final stationary acceptance.
