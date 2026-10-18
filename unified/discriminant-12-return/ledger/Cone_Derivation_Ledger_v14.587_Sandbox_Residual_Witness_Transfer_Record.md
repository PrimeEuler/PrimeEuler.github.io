# Cone Derivation Ledger v14.587 — Sandbox: v14.583 Residual Witness Payload Transferred to the Repository

Track: sandbox (Lane B exploratory/execution sandbox under little Euler).
Type: payload transfer record, discharging action (1) of the v14.585
HANDOFF (far-residual-certification-and-direct-middle-witness-replay).
Executed under Jeremy's 2026-10-18 standing rule: when one of the other
lanes is waiting on the sandbox for something, give it to them without
waiting on him.

## What was transferred

The exact v14.583 direct-middle residual witnesses — both residual
buffers and both certificates — are now in the repository at:

    unified/discriminant-12-return/payloads/direct_middle_residual_v14_583/

93 files: both buffers split into 700,000-byte chunks (.partNNN, 45 per
sector), both certificates whole, and manifest.json (SHA-256
a42e488d8557e2dd41e9ce675d2733225265b9573cf8f5f622d8cab826c0d219).

| file | bytes | SHA-256 |
|---|---|---|
| even-v-direct-middle-residual.bin (reassembled) | 31,211,490 | 8c6d880c40fc9a3fd4fb0d8da76e737b86457e1ff71e3bd092552e73eb4e0c36 |
| odd-v-direct-middle-residual.bin (reassembled) | 31,211,490 | 5606cc01d675aec1920c2cb887bcf5d3d2b1df20bd1a655cbee0fa51dd245316 |
| dm-residual-even-v.json | — | 96bc942e1119a4dc24d5a8c03ae25138e14bae34c0a62d5f3f8acbaf5a3661dc |
| dm-residual-odd-v.json | — | 0648b71e80a73f49c0b8234d216cfe11fe1a0c4aaefe0a10addbf49fe8dce2b8 |

These are exactly the witness hashes frozen in v14.583 and v14.585.

## Transfer integrity, stated plainly

The push was interrupted once by a host restart after 61 of 93 files;
a resumable driver completed the remainder (each push fetch-back
byte-verified). One chunk (odd-v part039) required a re-push after its
first post-restart attempt failed on a connection error; the re-push
landed and fetch-back verified (also observed independently in Audit
Round 320, §1 note). After completion, every one of the 93 files was
re-fetched from the repository and re-hashed, and both buffers were
reassembled from the repository chunks alone: zero chunk mismatches,
both whole-buffer hashes exactly as frozen above, repository manifest
byte-identical to the staged manifest.

## Status of the v14.585 handoff

Action (1) (this transfer) is discharged. Action (2) (independent
replay) has been discharged by External Audit Round 320 (v14.586) with
a stronger method than requested: full from-scratch recomputation of
all 2,080,766 rows, zero mismatches, all certificate identities exact.
Actions (3)–(4) — the two-sector far-residual construction and
certification from modes 4161533/4161534 through infinite support
against the remaining headroom — remain open and are the sandbox's
next work item. No far, whole-residual, stationary, or
infinite-capacity claim is made here.
