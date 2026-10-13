# Cone Derivation Ledger v14.328 — Lane A ACK of v14.326/v14.327 and composition-byte transfer blocker

**Date:** 2026-10-13
**Track:** Lane A (Cone/Suzuki)
**Status:** [N] v14.326 and v14.327 read in full and acknowledged exactly once; the Sandbox tail-action evaluation is accepted as the returned component certificate, but its frozen row bytes are not available in the Lane A runtime or repository.
**Parents:** v14.327, v14.326, v14.324, v14.310, v14.309.
**Collision check:** immediately before this write, live `master` was `3502c8f86b79f28c8af0b8f87d3dbc4ee7242305` (v14.327), and v14.328 was next-free.

---

Lane A accepts v14.326 as authorization to continue the already scoped work. It is a liveness note only and supplies no new mathematical or numerical evidence.

Lane A receives v14.327's evaluated Sandbox tail-only action certificate:

- Region 2: 256,000 same-parity rows per sector, 7,680,000-byte signed 30-byte / 256-fractional-bit buffers, SHA256 `01049b9491c91ff49a640964cb878da6fdcacd08542eddc5d345944cb8edf390` (even) and `e0dfb52f4255d8f13a1f312b6ae772d6e57d077810d620e4e4bd44eab21621a9` (odd), with directed ℓ² charges `6.690496712075973e-15` and `6.64847658308963e-15`.
- Region 3 window: 8,192 same-parity rows per sector, 245,760-byte buffers in the same schema, SHA256 `4705c6a0cf10b35d3050ba21c4a347ebe0c7ba393734225112da7eeafec992d2` (even) and `29f39fd719d45690fb5240d0dc31e4c3241a482591a715501e04dbfbd1c1bfc7` (odd), with directed ℓ² charges `1.3877527063693985e-16` and `1.3872495730166127e-16`.
- The v14.292 beyond-window ACTION envelope is retained only as an action bound, not promoted to a cancellation-aware residual bound.

**Concrete next action:** hash-verify the four frozen buffers, compose their row values once with the frozen v14.309 compact-Middle action and the exact bare source on the same lattice, accumulate directed residual norms, compare with the unchanged v14.310 sector budgets, and then determine whether a stronger beyond-window residual certificate is required.

**Same-run execution result / precise blocker:** Lane A inspected the available workspace and repository payload namespaces after reading v14.327. None of the four buffers, the exact rational certificates, or the evaluator output directory is present. v14.327 explicitly says they remain only in the independent Sandbox workspace `~/workspace/d12/region23_work/` and are not committed. Hashes, lengths, norms, and schemas cannot substitute for row bytes in a cancellation-sensitive composition. Therefore the composition arithmetic cannot be executed honestly in this runtime. This is a byte-transfer/access blocker, not a mathematical rejection of v14.327.

Jeremy's standing 2026-10-12 instruction authorizes continuation of the scoped Lane A work and its necessary additive implementation, verification, and ledger publication. Lane A does not silently broaden that into access to or publication of files held only by the independent Sandbox runtime. The smallest transfer needed is the four already-frozen buffers plus their exact directed-charge certificates; Sandbox code publication is not required for Lane A's immediate composition.

`C_S_32000` and every acceptance threshold remain unchanged. No whole-residual, stationary-pairing, or infinite-capacity claim is made. `stationary_acceptance_met = False`; `infinite_capacity_tail_closed = False`.

HANDOFF
target: sandbox
type: required-frozen-byte-transfer
parent: v14.328
source: v14.327
status: open
action: place the four v14.327 hash-bound Region-2 and Region-3-window buffers, together with their exact directed-charge certificates, in a Lane-A-accessible additive repository payload namespace or another ledger-accessible transfer mechanism authorized for this scoped computation
requirements: preserve the exact v14.327 hashes, lengths, signed-30-byte schema, 256 fractional bits, row ordering, lattice endpoints, and certificate provenance; do not regenerate or silently replace bytes
next-on-return: Lane A will hash-verify and perform the rowwise remaining-residual composition without another user prompt
