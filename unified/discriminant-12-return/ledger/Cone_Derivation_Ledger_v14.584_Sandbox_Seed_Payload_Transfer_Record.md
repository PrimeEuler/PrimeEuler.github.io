# Cone Derivation Ledger v14.584 — Sandbox: v14.486 Seed-Action Payload Transferred to the Repository

Track: sandbox (Lane B exploratory/execution sandbox under little Euler).
Type: payload transfer record. Authorized by Jeremy's explicit line of
2026-10-18 ("run it and add the seed"), together with his standing rule
given the same day: when one of the other lanes is waiting on the
sandbox for something, give it to them without waiting on him.

## What was transferred

The complete v14.486 original-seed direct-middle action payload —
the last sandbox-resident input of the direct-middle chain — is now in
the repository at:

    unified/discriminant-12-return/payloads/direct_middle_seed_action_v14_486/

93 files: the two sector certificates whole, both action buffers split
into 700,000-byte chunks (.partNNN, 45 per sector), and manifest.json
(SHA-256 57be7d5be78cf7263ffc585c2560c1c174de0c4ff2585ffe141aa9c5ee19bbab).

| file | bytes | SHA-256 |
|---|---|---|
| even-v-dm-action.bin (reassembled) | 31,211,490 | c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1 |
| odd-v-dm-action.bin (reassembled) | 31,211,490 | f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c |
| dm-action-even-v.json | — | c791e6c527ebfa2750a589aba02f6c5439aa890973bfa2ec973f0930a63cbb76 |
| dm-action-odd-v.json | — | 63e17d6f4146aff11e503e03c8dcd59e0868ecd0145e515f62d501b9f3f00f49 |

The reassembled buffer hashes are exactly the values frozen in
v14.486; the certificates are byte-identical to the sandbox originals
(point ℓ² norms 3.6507291856956343e-4 even / 3.647341992152244e-4 odd;
error uppers 1.995334793914987e-13 / 1.9846246697473864e-13).

## Verification

Every one of the 93 files was pushed individually with fetch-back
SHA-256 verification (zero failures). Afterwards, every file was
re-fetched from the repository, re-hashed, and both buffers were
reassembled from the repository chunks alone: both match the frozen
v14.486 hashes exactly, and the repository manifest is byte-identical
to the staged manifest.

## Consequence

The byte-replay fence noted by Lane A and Audit since v14.554 is now
discharged: every input of the v14.488 and v14.583 residual
compositions — v14.552 changed compact action, v14.500 δ candidate,
v14.539 complete RHS, v14.543 fresh lifts, and now the v14.486 original
seed action — is repository-resident and independently replayable.
The v14.583 residual buffers and certificates remain sandbox-side at
the hashes frozen in v14.583; no claim in that entry changes.
