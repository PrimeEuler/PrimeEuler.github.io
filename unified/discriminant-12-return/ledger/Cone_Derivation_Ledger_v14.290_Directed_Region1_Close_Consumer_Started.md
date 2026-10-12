# Cone Derivation Ledger v14.290 — Directed infinite seed Region-1 close consumer started

Lane A. v14.288's continue nudge was acknowledged in v14.289. Jeremy explicitly clarified that a nudge authorizes work, and requested continuation. Live parent checked: fc5ee37058bfe466e64a9343f5a363e03176f05b. Original C_S_32000 and all acceptance thresholds unchanged.

## Implementation and actual start

Recovered the repository-backed source and dependencies after workspace maintenance. The corrected v14.285 compact Near/Middle row binaries are present in the live repository. Read v14.278's Sandbox scope/ownership note: its float prototype is not committed, and close action/pole and Regions 2–3 remain unevaluated. This additive Lane A implementation does not claim or reuse that inaccessible prototype.

Producer: research-notes/suzuki_infinite_seed_region1_close_action.py. It computes the actual physical seed y_m=Phi(m)/log(m/4) for all same-parity close inputs b<=m<a, where b=512001/512002 and a=1024003/1024004. W/A coefficients come from the unchanged SHA-pinned v14.223 source. Physical z_m intervals are evaluated freshly by the certified bulk consumer; exact rational Phi endpoints and directed log endpoints yield y intervals. Each represented point is floored at 160 bits and its uncertainty measured against both endpoints.

Four exact signed GMP integer convolutions then evaluate the Toeplitz/Hankel close-input action on every remote Region-1 output R<n<b: 128000 rows. Even-v has 256001 close inputs and odd-v has 256001. The exact pole on this finite close support is included. Three complete direct sums over every close input check the convolution outputs. The lower-limit a-start infinite far contribution is excluded explicitly, to be composed separately using v14.276 and v14.274.

Both sectors' seven-input/seven-output smoke rectangles executed successfully and matched all selected complete direct rows. These are algebra/arithmetic checks, not a full gate certificate. The full even-v run has actually started locally. The new read-only scoped workflow runs both complete sectors independently and uploads exact binary/certificate artifacts. Full-run results and durable hash-bound output publication are pending; no full close rectangle is claimed evaluated in this entry.

## Error accounting implemented

At same-parity offdiagonal gaps at least two, the certified kernel bound is 8/|n-m|<=4. Pole propagation contributes at most 8. The uniform row seed charge is therefore 12*M*max_y_error. With |z|<8, |c|<1 and directed pole-parameter errors, the deliberately loose scalar row charge is 100*(input_z_error+output_z_error+c_error+8*2^-256)*represented_seed_l1. Reciprocal channel and final row floor charge is 20*2^-256*l1+2^-256. Multiply the exact row sum by sqrt_upper(128000) for the complete l2 bound. The producer asserts this total is below 1e-25; this is an execution requirement, not a reported full-run result.

The pole uses directed L,t intervals, a 256-bit represented physical point, and the finite sum p_m*y_m. The producer retains separate false flags for far-input action, whole infinite action, stationary acceptance and capacity closure. The direct kernel formula is the already-audited Toeplitz-minus-Hankel identity; output/input offsets are explicit and independently checked by complete direct sums.

## HANDOFF — External Audit

Please review the additive close consumer's offsets, seed interval division, separate seed/physical-scalar/reciprocal charges, and finite close-support pole. The full scoped jobs will provide actual evaluated witnesses. This entry records implementation and computation start only; do not treat it as a completed or frozen numerical gate.

## HANDOFF — Sandbox

Lane A is now evaluating the missing Region-1 close rectangle and its finite close pole in this explicit namespace. Avoid duplicating that rectangle. Please focus on Regions 2–3's actual directed infinite D*y evaluation; retain the later-start far inputs as a separate contribution. Any unavailable code or publication restriction should be ledgered as a concrete blocker rather than closing an implementation handoff as a design acknowledgement.

## Next

Inspect both full close jobs, verify their certificates and binaries, then freeze actual outputs and compose with the directed a-start far moments once. Regions 2–3, whole residual acceptance, signed stationary pairing and infinite capacity closure remain open.
