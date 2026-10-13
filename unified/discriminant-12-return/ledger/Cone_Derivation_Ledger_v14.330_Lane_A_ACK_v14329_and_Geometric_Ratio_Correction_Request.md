# Cone Derivation Ledger v14.330 — Lane A ACK of v14.329 and geometric-ratio correction request

**Date:** 2026-10-13
**Track:** Lane A (Cone/Suzuki)
**Status:** [C] v14.329 read and acknowledged exactly once. Its byte-transfer conclusion is accepted, but its third cross-check contains a strict numerical-inequality error inherited from v14.292/v14.327 and requires Sandbox confirmation before the directed tail remainder is consumed.
**Parents:** v14.329, v14.328, v14.327, v14.292.
**Collision check:** immediately before this write, live `master` was `ae8cd05f25815359c07efa102a884409995cca84` (v14.329), and v14.330 was next-free.

---

Lane A accepts v14.329's two substantive conclusions:

1. the v14.327 summary statistics pass the pole-moment and pre-registration consistency checks described there; and
2. the four frozen row buffers remain unavailable, so byte-level verification and cancellation-sensitive composition are still blocked exactly as recorded in v14.328.

Lane A does **not** accept v14.329 §2(c)'s statement that the displayed endpoint ratios “match” the claimed bound `(n/2a)^2 <= 0.258`. Direct exact arithmetic gives

- even: `(1040384/2048006)^2 = 270599716864/1048582144009 = 0.25806248791289493...`;
- odd: `(1040386/2048008)^2 = 270600757249/1048584192016 = 0.25806297606751544...`.

Both values are strictly greater than `0.258`. Thus the rounded-down inequality in v14.292 §2 and repeated in v14.327 is false on the top of the evaluated Region-3 window, and v14.329's own decimal calculation actually exposes rather than validates that statement. A safe simple bound is `(n/2a)^2 < 0.258063` for the stated endpoints (or conservatively `< 0.259`).

This does not by itself show that the v14.327 buffers or charges are wrong: the private evaluator may have used the exact endpoint ratio or another outward upper bound internally, with `0.258` appearing only as imprecise ledger prose. Because the evaluator, certificates, and buffers are not accessible to Lane A, that distinction cannot be resolved here.

**Concrete next action:** Sandbox must state and expose the actual ratio bound used in the 42-moment tail-remainder calculation. If the evaluator used exact rowwise ratios or an outward bound at least `0.25806297606751544...`, publish that fact and the exact certificate field. If it used `0.258` as an upper bound, recompute the directed Region-2/3 remainder charges and freeze corrected certificates/buffers as necessary. Then transfer the exact four v14.327 buffers and certificates under the already-open v14.328 handoff.

Until that response lands, Lane A will not consume the stated Region-2/3 directed charges. `C_S_32000` and all acceptance thresholds remain unchanged. No whole-residual, stationary-pairing, or infinite-capacity claim is made.

HANDOFF
target: sandbox
type: correction-and-frozen-byte-transfer
parent: v14.330
sources: v14.292, v14.327, v14.329
status: open
action: confirm the exact outward geometric-ratio bound actually used by the evaluator; correct/recompute the remainder charges if 0.258 was used; then make the four frozen buffers and exact directed-charge certificates Lane-A-accessible
required-check: endpoint maxima must cover 0.25806248791289493... even and 0.25806297606751544... odd
preserve: hashes only if bytes remain unchanged; otherwise issue new hashes and explicitly supersede the affected v14.327 fields
next-on-return: Lane A will hash-verify, replay the ratio/remainder certificate, and perform rowwise residual composition without another user prompt

HANDOFF
target: external-audit
type: correction-notice
parent: v14.330
source: v14.329
status: open
action: amend the §2(c) verdict: the computed endpoint ratios are greater than 0.258; independently review the Sandbox response and revised/exact remainder certificate
