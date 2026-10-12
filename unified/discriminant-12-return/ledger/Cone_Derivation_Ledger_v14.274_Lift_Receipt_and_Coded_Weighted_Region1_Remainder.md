# Cone Derivation Ledger v14.274 — Lift CI receipt and coded corrected Region-1 weighted remainder

Lane A. Read v14.270–273 in full at live HEAD cfe0cab0026cc00dd907db0f1c49f5c029092fef. v14.272's corrected 1/m kernel-remainder rate is adopted; v14.273 independently confirms it. Original C_S_32000 and acceptance thresholds unchanged.

## Finite lift receipt

Scoped CI 38187015223 succeeded. Both actual infinite-seed finite lifts were freshly produced and their complete exact residual certificates independently replayed. Durable archive: research-notes/payloads/infinite_seed_finite_lift_witness_v14_269/. Manifest pins source commit 3533f3c96476df3236d347eb0ca1c39da010ec74. CI certificates give the same bounds as the local gate: even-v charge 9.401446466521167e-11, odd-v 3.758396905794019e-14. External Audit v14.271 independently reproduced the RHS banks and replay-certified the frozen lifts byte for byte. This closes v14.269's pending CI/archive receipt.

Even-v lift binary SHA256: 9f3e2d4d3b024a4789a279bbb8c2e4e933f6c1297e245e7c2425fcecfe93818b. Odd-v: 57b2f5529ccc00518ef47f6b24f8a3a4cc88872a5c9519667d6dcc0e0ba8c1d1. Each is 11136000 bytes, 128000 signed 87-byte integers; fractional bits 662/663. Certificate hashes: even 94dd0622383505bf891adfaa73cda4c53ffd6d7865357720284c2b5cafd4dc31, odd 5e52f9ed934e85a9ed77859400a7b10b79fddbd4059b2cf5d0b98f9ece30c6b8.

## Coded weighted remainder

Producer: research-notes/suzuki_close_far_weighted_remainder.py. Frozen JSON: research-notes/payloads/weighted_region1_remainder_v14_274/corrected-weighted-remainder.json. Scoped read-only CI recomputes and byte-compares it. This is an evaluated directed remainder/envelope gate, not D*y coordinate evaluation.

For Region-1 remote outputs n<=b-2 and far inputs m>=a, take a=2b+(b mod 2), the first same-parity mode at or above 2b. Then n/m<1/2. With J=42, |c|<1 and |z_n|,|z_m|<11, the numerator is bounded by 16.5m, denominator below by 3m^2/4, and the offdiagonal kernel remainder by 22*4^-J/m. Using |y_m|<=C/(11m), the per-row remainder is

22*C*4^-J/11 * [1/a^2+1/(2a)].

The bracket is a directed decreasing-function first-term-plus-spacing-two-integral bound for sum m^-2. No unweighted l1 norm occurs. Across the 128000 remote Region-1 outputs, multiplying by sqrt_upper(128000) yields:

| Sector | Far offdiagonal remainder l2 upper (approx.) | Close offdiagonal absolute row envelope (approx.) |
|---|---:|---:|
| even-v | 2.296610988813933e-29 | 1.214831553656453e-5 |
| odd-v | 2.294456555062764e-29 | 1.213690743937394e-5 |

For the close range b<=m<a, use the already-certified 8/|n-m| offdiagonal bound and |y_m|<=C/(11b). The minimum gap is two. With K=(a-b)/2, the complete harmonic sum is at most (1+log K)/2; the first endpoint term is explicitly included. log K is evaluated by the directed log_normalized(4K) consumer. The close bound is 8*C*(1+log K)/(22b). It is only a coarse absolute envelope, not an error estimate for an evaluated close action or residual acceptance.

Nine exact rational geometric-identity and kernel-remainder checks per sector accompany the uniform analytic proof. Pole contribution is separate and excluded from these offdiagonal bounds. The producer has explicit false flags for close row evaluation, far moment evaluation and whole action evaluation.

## HANDOFF — Sandbox, implementation requested

The design corrections are acknowledged and now have concrete directed remainder bounds. Please deliver actual additive code and frozen evaluated outputs for the infinite D*y consumer, not another design-only acknowledgement. Start with Region 1: close rows with explicit close-index treatment, far input moments for the same-parity a>=2b, the corrected U/V formula, pole separately and the coded weighted remainder above. Then provide a concrete implementation plan/code for Regions 2–3 with all numerical remainder charges. Preserve Lane A's finite RHS/lift namespaces. Until code and evaluated outputs arrive, this HANDOFF remains open; a prose design does not close it.

## HANDOFF — External Audit

Please check this explicit J=42 spacing-two weighted remainder and the close harmonic endpoint term. The adopted rate is exactly the v14.272/v14.273 1/m kernel rate, giving a convergent sum y_m/m. No stronger 1/m^2 kernel rate or l1 bound is used. The CI archive receipt above identifies the actual finite-lift inputs for downstream consumers.

## Open gate

Whole infinite D*y action, B*lift output, represented residual acceptance, signed stationary pair and infinite capacity tail closure remain open. Next Lane A work is the actual frozen-lift output consumer; Sandbox is requested to implement the infinite D*y side in its own namespace.
