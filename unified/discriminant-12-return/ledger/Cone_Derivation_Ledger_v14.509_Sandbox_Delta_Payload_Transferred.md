# Cone Derivation Ledger v14.509 — Sandbox: delta payload transferred to the repository (v14.503 handoff answered)

**Timestamp:** 2026-10-16 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.503 (payload handoff), v14.500/v14.502 (candidate + clarification), v14.508 (Audit R296 byte-level replay).
**Status:** transfer record. On Jeremy's explicit authorization (2026-10-16), the exact v14.500 artifacts are now repository-accessible. No recomputation or replacement: the deposited bytes are the certified bytes.

## Payload

Location: `unified/discriminant-12-return/payloads/direct_middle_delta_candidate_v14_500/`

- `even-v-dm-correction.bin` and `odd-v-dm-correction.bin` (17,686,511 bytes each; width 17; 1,040,383 rows), stored as 26 chunks of 700,000 bytes per buffer (repo payload convention), reassembling exactly to SHA-256 even `c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2`, odd `e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776`;
- `dm-correction-even-v.json` (SHA-256 `99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911`) and `dm-correction-odd-v.json` (SHA-256 `c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703`);
- `manifest.json` (SHA-256 `d4691fe4e4cbd2ac390e6530b79a4388c6385a20a962a3b66a305be0505d1a75`) binding the payload to v14.500/v14.502, with per-chunk hashes, the consumed v14.488 residual hashes, and the pinned log-module hash.

All 55 files were byte-verified on push (fetch-back SHA-256 match per file).

## Independent replay already completed

Audit R296 (v14.508) reassembled both buffers from the deposited chunks, decoded all rows, and reproduced correction ℓ¹, exact norm², norm upper, the whole-trial triangle sum, and the cap-pass exactly as Fractions, with the v14.403 base term verified directly — no defect. One scope limitation stands, unchanged and accepted: the one-quantum enclosure against the v14.488 point-residual buffers cannot be replayed from the repository, because those buffers were not part of the v14.503 transfer request and remain in the sandbox workspace (hashes frozen in v14.488/v14.490).

## Bookkeeping note

Two entries share the number v14.507 (Lane A's ACK of v14.505 and Audit R295's blocker confirmation); per standing practice both are retained, and R296's replay entry took v14.508. Collision resolution remains with the audit thread; this entry simply records the fact.

## Disposition

The v14.503 HANDOFF is answered and closed. Lane A's next gate is unblocked on the sandbox side: byte-verify/replay (done independently by R296), then the new complete RHS, fresh lift, and fresh support-aware action/residual evaluation. All closure flags remain false; no threshold or charge invariant changes.
