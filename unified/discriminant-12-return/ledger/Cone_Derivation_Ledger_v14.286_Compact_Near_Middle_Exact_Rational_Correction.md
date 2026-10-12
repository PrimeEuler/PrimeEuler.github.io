# Cone Derivation Ledger v14.286 — compact Near/Middle exact-rational correction

Lane A correction to v14.285. Original `C_S_32000` and every acceptance threshold remain unchanged.

## CI result and correction

Scoped run `38283052402` independently reconstructed the hash-bound actual256 input and evaluated all 384000 compact Near/Middle rows in both sectors. Both jobs reached certificate emission and uploaded their exact outputs, but the byte-comparison step failed and the guarded freeze job correctly skipped.

The failure is confined to two exact-rational JSON fields. The v14.285 producer charges the two rounded reciprocal channels by

`20 * 2^-256 * ||x||_1 * sqrt_upper(384000)`.

The committed v14.285 certificates retained the earlier pre-correction reciprocal rational, while the committed producer emitted the displayed full-`l1` expression. The difference is far below binary64 display resolution but is not acceptable in a hash-bound certificate. This entry replaces, for each sector, `reciprocal_kernel_rounding_charge_upper` by the producer's exact rational and recomputes `complete_compact_near_middle_action_error_upper` as the exact sum of diagonal, parameter, reciprocal, and final-row charges.

An independent local Python 3.11 replay of the complete odd sector reproduces the v14.285 binary exactly:

- rows: `384000`
- bytes: `11520000`
- SHA256: `a3f17e99ad87819c28b8e6c328cbf446c8604e4bb72a8509dce3cf2c0432da55`

Thus no evaluated output row changes. The even-v and odd-v binary SHA256 values remain `ed4f9866247c53e4059c9872adfa4d6107af3b8a16db215a6d1c14640f89bc68` and `a3f17e99ad87819c28b8e6c328cbf446c8604e4bb72a8509dce3cf2c0432da55`. The displayed complete error uppers also remain `1.6083041941704035e-14` and `1.6068230397025636e-14`, both below the unchanged `3e-11` target.

The scoped workflow will replay both corrected certificates. The exact row buffers are not called durably frozen until that run succeeds and its guarded archive push lands.

## Scope and HANDOFF

This correction does not claim whole residual acceptance or infinite-tail closure. Every v14.285 scope flag remains unchanged.

HANDOFF — External Audit: verify that each corrected reciprocal rational equals `20 * 2^-256 * parameter_charge / 1e-34`, that each corrected total is the exact sum of its four constituent charges, and that both binary hashes are unchanged.

HANDOFF — Sandbox: no row-level input changed. Continue the separate actual infinite `D*y` close/pole and Regions 2–3 work; do not compose v14.285 until the corrected replay/archive receipt succeeds.

## Next/open

First await the corrected scoped replay and guarded buffer freeze. Then the next Lane A gate remains actual infinite `D*y`: close rows and pole, Regions 2–3, composition, full residual acceptance, signed stationary pairing, and infinite capacity closure.
